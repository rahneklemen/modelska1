#optimizacija hitrosti-periodicni robni pogoji
import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt


def v(t,v0):
    return -6*(1-v0)*t**2+6*(1-v0)*t+v0

x=np.arange(0,1.01,0.01)
y=v(x,0.7)
y2=v(x,2)
x=x

def dolzina(x,zacetna_hit):
    N=len(x)-1
    return sum(x)-x[-1]/2-zacetna_hit/2-N




def funkcija(tocke_hitrost,zacet_speed):

    n=len(tocke_hitrost)
    vsota1=0

    #zacetno
    vsota1+=0.5*((tocke_hitrost[0]-zacet_speed))**2

    for i in range(n-1):
        vsota1+=((tocke_hitrost[i+1]-tocke_hitrost[i]))**2
    vsota1+=0.5*((zacet_speed-tocke_hitrost[i+1]))**2

    return vsota1

def optimizacija(zacetna_hitrost,N):
    hitrost=np.ones(N-1)*zacetna_hitrost
    opt=optimize.minimize(funkcija,hitrost,args=zacetna_hitrost,constraints=({'type': 'eq', 'fun': lambda x: sum(x)+zacetna_hitrost-N})).x
    return np.append([zacetna_hitrost],np.append(opt,[zacetna_hitrost]))


res=optimizacija(2,100)
print(dolzina(res,2))

res2=optimizacija(1,100)
print(dolzina(res2,1))

res3=optimizacija(0.5,100)
print(dolzina(res3,0.5))

res4=optimizacija(0.7,100)
print(dolzina(res4,0.7))
print(res4)
print(sum(res4))

# plt.plot(x,y,'-')
# plt.plot(x,y2,'-')
plt.plot(x,res,label=r'$v(0)=v(1)=2$')
plt.plot(x,res2,label=r'$v(0)=v(1)=1$')
plt.plot(x,res4,label=r'$v(0)=v(1)=0.7$')
plt.plot(x,res3,label=r'$v(0)=v(1)=0.5$')

plt.title('periodični robni pogoji')
plt.ylabel('hitrost')
plt.xlabel('čas')
plt.grid()
plt.legend(loc=9)
plt.savefig('periodicni_robni_pogoji.png')


plt.show()
