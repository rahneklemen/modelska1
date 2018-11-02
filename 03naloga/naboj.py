#definiraj funkcijo, ki ima za vnos 2d x n array dolzine-2 polarna kota

import scipy.optimize as optimize
import numpy as np

def f(seznam):
    vsota=0
    for i in range(len(fi)):
        for j in range(i):
            razdalja=abs(np.sqrt(2-2*(np.sin(fi[i])*np.sin(theta[j])*np.cos(fi[i]-fi[j])+ np.cos(theta[i]) * np.cos( theta[j] ) )))
            vsota=vsota + razdalja
    return vsota


test=for (int x=0; x<length; x = x+step)
print(test)
n=8
for i in range(n):
    if i==0:
        kot1=()
    if i<0:
        kot1=kot1+()

kot2=kot1
print(kot1)
#potrebno še pogoj
for i in range(n):
    kot1[i]=np.pi/n*i
    kot2[i]=np.pi/n*i

print(kot1,'\n',kot2)


x0=kot1


result = optimize.minimize(f,)
print(result)
# print(result)
#potem se 3d plot za razlicne n

