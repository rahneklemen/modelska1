#optimizacija hitrosti
import scipy.optimize as optimize
import numpy as np
from math import exp
import matplotlib.pyplot as plt

def hitrost(v,v0,vK,lamda,v_max,beta):
    x0=v0
    b=len(v)
    dt=1/(b+1)
    #print(v)
    
    vsota=0
    for i in range(b):
        if i==0:
            delna=(1/2*((v[i]-v0)/dt)**2+lamda*v[i])*exp(-beta*(v[i]-v_max))
        elif i<b-1 and i>0:
            delna=(((v[i]-v[i-1])/dt)**2+lamda*v[i])*exp(-beta*(v[i]-v_max))
        elif i+1==b:
            delna=(1/2*((v[i]-v[i-1])/dt)**2+lamda*v[i])*exp(-beta*(v[i]-v_max))
        vsota=vsota+delna*dt
    return vsota


def integral(v,v0):
    return (sum(v)-0.5*v[-1]+0.5*v0)/(len(v))


def bisekcija(x,spodnja,zgornja):
    n=len(x)
    x0=1
    vK=1
    lamda=(spodnja+zgornja)/2
    v_max=10
    beta=0.0
    dt=1/(n)
    
    resitev=optimize.minimize(hitrost,a,args=(x0,vK,lamda,v_max,beta,)).x
    # testno=resitev.x
    # print(testno)
    #print(resitev)
    
    vsota=integral(resitev,x0)
    # print('dolzina',n,'vsota:\t',vsota,'\tlamda\t:',lamda)
    if vsota>1:
        return bisekcija(resitev,lamda,zgornja)
    elif vsota<0.999995:
        return bisekcija(resitev,spodnja,lamda)
    else:
        # print('rešitev',resitev.x)
        # vektor=resitev.x
        print('tule sem')
        # print(testno)
        # print(type(testno))
        return resitev
    

n=100
a=[1/n*x for x in range(n)]
print(a)

vector_hitrost=bisekcija(a,-100,100)



print('hitrost\t\t',vector_hitrost)

#najprej yos, potem x os

plt.plot(a,vector_hitrost,'-o')
plt.grid()
plt.show()
