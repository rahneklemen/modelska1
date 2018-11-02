import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


x = []
y = []
v=[]
u=[]
u_error=[]


f = open('farmakoloski.dat', 'r', encoding='utf-8')
data_file = f.readlines()

i = 0
for vrsta in data_file:
    if i > 0:
        vrsta = vrsta.strip('\n')
        podatki = vrsta.split('\t')
        x.append(float(podatki[0]))
        v.append(1/float(podatki[0]))

        y.append(float(podatki[1]))
        u.append(1/float(podatki[1]))
        u_error.append(3/(float(podatki[1])**2))

    i = i + 1

f.close()

def f(x,a,b):
    return a*x/(x+b)

def linearno(v,y0,a):
    '''

    Parameters
    ----------
    x - data
    y0 - parameter1
    a - parameter2

    Returns
    -------
    a/(y0*x)+1/y0

    '''

    return a/y0*v+1/y0

# fitanje=curve_fit(linearno, v, u,sigma=u_error)
#
#
# print(fitanje)

fitanje=curve_fit(linearno, v, u,sigma=u_error)

a,b=fitanje[0]


print('prvi arraj vrednost, drugi arraj kvadrat napake na diagonali matrike')
print(fitanje)

y_fit=[]
for i in range(len(y)):
    y_fit.append(f(x[i],a,b))



plt.plot(x,y_fit,'o')
plt.errorbar(x,y,yerr=3)
plt.grid()
plt.show()







