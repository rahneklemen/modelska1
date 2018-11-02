import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def d(r,t):
    return -(r*t-np.sqrt(1-r**2*(1-t**2)))

def sevanje(lamda):
    n=100000
    r=(np.random.rand(n))**(1/3)
    t=np.random.rand(n)*2-1
    
    zarek=d(r,t)
    
    pot=-lamda*np.log(1-np.random.rand(n))
        
    N=0
    M=n
    for i in range(n):
        if pot[i]<zarek[i]:
            N+=1
    return 1-N/M

# print(sevanje(10000000))
x=np.arange(0.1,20,0.2)
print(x)
y=[]
for i in x:
    y.append(sevanje(i))
    
print(y)
plt.plot(x,y,'-o')
plt.grid()
plt.ylabel('delež pobeglih fotonov')
plt.xlabel(r'$\lambda$-povprečna prosta pot')
plt.savefig('9_druga.png')
# plt.xscale('log')
plt.show()