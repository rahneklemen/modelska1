def to_binary(n):
    s=[]
    if not isinstance(n,int):
        raise TypeError('Integer expected, got {} of type {}'.format(n,type(n)))
    
    if n==0:
        return '0'
    if n<0:
        return '-'+to_binary(-n)
    while(n>0):
        s.append(n%2)
        n//=2
    return ''.join(map(str, reversed(s)))