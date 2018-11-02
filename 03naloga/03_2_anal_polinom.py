#optimizacija hitrosti
import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt




def dolzina(x,zacetna_hit):
    N=len(x)-1
    return sum(x)-x[-1]/2-zacetna_hit/2-N




def funkcija(tocke_hitrost,zacet_speed,limit):

    n=len(tocke_hitrost)
    dt=1/(n)
    vsota1=0

    #zacetno
    vsota1+=0.5*((tocke_hitrost[0]-zacet_speed))**2

    for i in range(n-1):
        vsota1+=((tocke_hitrost[i+1]-tocke_hitrost[i]))**2
    vsota1+=0.5*((tocke_hitrost[i]-tocke_hitrost[i-1]))**2

    for i in range(n-1):
        vsota1+=1/(tocke_hitrost[i]-limit)*dt
    vsota1+=0.5*1/((tocke_hitrost[n-1]-limit))*dt


    return vsota1

def optimizacija(zacetna_hitrost,limit,N):
    hitrost=np.ones(N)*zacetna_hitrost
    opt=optimize.minimize(funkcija,hitrost,args=(zacetna_hitrost,limit),constraints=({'type': 'eq', 'fun': lambda x: sum(x)-x[-1]/2+zacetna_hitrost/2-N})).x
    return np.append([zacetna_hitrost],opt)

max=1.5
res=optimizacija(2,max,10)
print(dolzina(res,2))

res2=optimizacija(2,max*2,10)
print(dolzina(res2,1))

res3=optimizacija(0.5,max,10)
print(dolzina(res3,0.5))

res4=optimizacija(0.5,max*2,10)
print(dolzina(res4,0.7))
print(res4)
print(sum(res4))



plt.plot(res,'o')
plt.plot(res2,'-')
plt.plot(res3,'o-')
plt.plot(res4,'^')
plt.show()
