
'''
Translated from Octave code at: http://www.ecs.shimane-u.ac.jp/~kyoshida/lpeng.htm
and placed under MIT licence by Enzo Michelangeli with permission explicitly
granted by the original author, Prof. Kazunobu Yoshida  

-----------------------------------------------------------------------------
Copyright (c) 2010, Kazunobu Yoshida, Shimane University, and Enzo Michelangeli, 
IT Vision Limited

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
-----------------------------------------------------------------------------

Usage:
 
 optx,zmin,is_bounded,sol,basis = lp(c,A,b)
 
  This program finds a solution of the standard linear programming problem:
    minimize    z = c'x
    subject to  Ax = b, x >= 0
  using the two phase method, where the simplex method is used at each stage.
  Returns the tuple:
    optx: an optimal solution.
    zmin: the optimal value. 
    is_bounded: True if the solution is bounded; False if unbounded.
    sol: True if the problem is solvable; False if unsolvable.
    basis: indices of the basis of the solution.
    
  All the non-scalar data types are numpy arrays.   
'''
from numpy import *
import warnings

class NamedTuple(tuple):
    def __new__(cls, values, names):
        self = tuple.__new__(cls, values)
        for value, name in zip(values, names):
            setattr(self, name, value)
        return self

class Solution(NamedTuple):
    _fields = []
    def __new__(cls, *a, **kw):
        values = list(a)
        for name in cls._fields[len(values):]:
            values.append(kw.pop(name))
        if len(values) != len(cls._fields) or kw:
            raise ValueError("Invalid arguments")
        return NamedTuple.__new__(cls, values, cls._fields)

    def __repr__(self):
        return "%s%s" % (self.__class__.__name__, 
                         NamedTuple.__repr__(self))

class LPSolution(Solution):
    """
    Solution to a linear programming problem

    Attributes
    ----------
    x
        The optimal solution
    min
        The optimal value
    is_bounded
        True if the solution is bounded; False if unbounded
    solvable
        True if the problem is solvable; False if unsolvable
    basis
        Indices of the basis of the solution.
    """
    _fields = ['x', 'min', 'is_bounded', 'solvable', 'basis']

class LPWarning(RuntimeWarning):
    pass

def lp(c, A, b):
    m,n = A.shape
    for i in xrange(m):
        if b[i] < 0.0:
            A[i,:] = -A[i,:]
            b[i] = -b[i]
    d = -sum(A, axis=0)
    w0 = sum(b)
    # H = [A b;c' 0;d -w0];
    #H = bmat('A b; c 0; d -w0') 
    ''''''
    H = vstack([     #  The initial _simplex table of phase one
         hstack([A, array([b]).T]), # first m rows
         hstack([c, 0.]),   # last-but-one
         hstack([d, -w0])]) # last
    ''''''
    indx = arange(n)
    basis = arange(n, n+m)
    #H, basis, is_bounded = _simplex(H, basis, indx, 1)
    is_bounded = _simplex(H, basis, indx, 1)
    if H[m+1,n] < -1e-10:   # last row, last column
        sol = False
        warnings.warn('Unsolvable LP problem', LPWarning)
        optx = []
        zmin = []
        is_bounded = False
    else:
        sol = True
        j = -1
        for i in xrange(n):
            j = j+1
            if H[m+1,j] > 1e-10:
                H[:,j] = []
                indx[j] = []
                j = j-1
        #H(m+2,:) = [] % delete last row
        H = H[0:m+1,:]
        if size(indx) > 0:
        # Phase two
            #H, basis, is_bounded = _simplex(H,basis,indx,2);
            is_bounded = _simplex(H,basis,indx,2);
            if is_bounded:
                optx = zeros(n+m);
                n1,n2 = H.shape;
                for i in xrange(m):
                    optx[basis[i]] = H[i,n2-1]
                # optx(n+1:n+m,1) = []; % delete last m elements
                optx = optx[0:n] 
                zmin = -H[n1-1,n2-1]    #  last row, last column
            else:
                optx = []
                zmin = -Inf
        else:
            optx = zeros(n+m);
            zmin = 0;
    return LPSolution(optx, zmin, is_bounded, sol, basis)  

def _simplex(H,basis,indx,s):
    '''
      [H1,basis,is_bounded] = _simplex(H,basis,indx,s)
      H: simplex table (MODIFIED).
      basis: the indices of basis (MODIFIED).
      indx: the indices of x.
      s: 1 for phase one; 2 for phase two.
      H1: new simplex table.
      is_bounded: True if the solution is bounded; False if unbounded.
    '''
    if s == 1:
        s0 = 2
    elif s == 2:
        s0 = 1
    n1, n2 = H.shape
    sol = False
    while not sol:
        # [fm,jp] = min(H(n1,1:n2-1));
        q = H[n1-1, 0:n2-1] # last row, all columns but last
        jp = argmin(q)
        fm = q[jp]
        if fm >= 0:
            is_bounded = True    # bounded solution
            sol = True
        else:
            # [hm,ip] = max(H(1:n1-s0,jp));
            q = H[0:n1-s0,jp]
            ip = argmax(q)
            hm = q[ip]
            if hm <= 0:
                is_bounded = False # unbounded solution
                sol = True
            else:
                h1 = zeros(n1-s0)
                for i in xrange(n1-s0):
                    if H[i,jp] > 0:
                        h1[i] = H[i,n2-1]/H[i,jp]
                    else:
                        h1[i] = Inf
                ip = argmin(h1)
                minh1 = h1[ip]
                basis[ip] = indx[jp]
                if not _pivot(H,ip,jp):
                    raise ValueError("the first parameter is a Singular matrix") 
    return is_bounded

def _pivot(H,ip,jp):
    # H is MODIFIED
    n, m = H.shape
    piv = H[ip,jp]
    if piv == 0:
        #print('singular')
        return False
    else:
        H[ip,:] /= piv
        for i in xrange(n):
            if i != ip:
                H[i,:] -= H[i,jp]*H[ip,:]
    return True


######### Unit test section #########

from numpy.testing import *

def test_lp():
    probs = [
        {
            'A': array([
                [2.,  5., 3., -1.,  0.,  0.],
                [3., 2.5, 8.,  0., -1.,  0.],
                [8.,10.,  4.,  0.,  0., -1.]]),
            'b': array([185., 155., 600.]),
            'c': array([4., 8., 3., 0., 0., 0.]),
            'result': [
                    array([ 66.25, 0., 17.5, 0., 183.75, 0.]),
                    317.5,
                    True,
                    True,
                    array([2, 0, 4])            
                ]
        } # add other test cases here...
    ]

    for prob in probs:
        optx, zmin, bounded, solvable, basis = lp(prob['c'],prob['A'],prob['b'])
        expected_res = prob['result']
        assert_almost_equal(optx, expected_res[0])
        assert_almost_equal(zmin, expected_res[1])
        assert_equal(bounded, expected_res[2])
        assert_equal(solvable, expected_res[3])
        assert_equal(basis, expected_res[4])


    

c=array([20,10,15])
A = array([[3,2,5],[2,1,1],[1,1,3],[5,2,4]])
b = array([55, 26, 30, 57] )
   
optx,zmin,is_bounded,sol,basis = lp(c,A,b)
