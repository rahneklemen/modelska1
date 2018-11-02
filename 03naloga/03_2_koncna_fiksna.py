#optimizacija hitrosti
import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt


def v(t,v_0):
    l=1
    t_0=1
    lamda=6/(t_0**3)*(l-v_0*t_0)

    return -lamda/4*t**2+lamda/2*t_0*t+v_0

x=np.arange(0,1.1,0.01)
y=v(x,0.7)
y2=v(x,2)
x=x*100

def dolzina(x,zacetna_hit,konc):
    N=len(x)-1
    return sum(x)-zacetna_hit/2-konc/2-N




def funkcija(tocke_hitrost,zacet_speed,koncna):

    n=len(tocke_hitrost)
    vsota1=0

    #zacetno
    vsota1+=0.5*((tocke_hitrost[0]-zacet_speed))**2

    for i in range(n-1):
        vsota1+=((tocke_hitrost[i+1]-tocke_hitrost[i]))**2
    vsota1+=0.5*((koncna-tocke_hitrost[-1]))**2

    return vsota1

def optimizacija(zacetna_hitrost,konec,N):
    hitrost=np.ones(N-1)*zacetna_hitrost
    opt=optimize.minimize(funkcija,hitrost,args=(zacetna_hitrost,konec),constraints=({'type': 'eq', 'fun': lambda x: sum(x)+konec/2+zacetna_hitrost/2-N})).x
    return np.append([zacetna_hitrost],np.append(opt,[konec]))

N=100
vk=2

res=optimizacija(1,vk,N)
print(dolzina(res,1,2))

res2=optimizacija(1.5,vk,N)
print(dolzina(res2,1.5,2))

res3=optimizacija(0.5,vk,N)


res4=optimizacija(0.7,vk,N)
print(dolzina(res4,0.7,2))
# print(res4)
# print(sum(res4))

# plt.plot(x,y,'-')
# plt.plot(x,y2,'-')
x=np.arange(0,1.01,0.01)
print(len(x))
print(len(res))

naslov='numericno_fiskna_koncna_n_'+str(N)+'vk_'+str(vk)+'.png'
plt.plot(x,res3,label=r'$v(0)=0.5$')
plt.plot(x,res4,label=r'$v(0)=0.7$')
plt.plot(x,res,label=r'$v(0)=1$')
plt.plot(x,res2,label=r'$v(0)=1.5$')
plt.legend(loc=2)
plt.grid()
plt.ylabel('hitrost')
plt.xlabel('čas')
plt.title(r'numerična minimizacija pri fiksni končni hitrosti $v(1)=2$')
plt.savefig(naslov)
plt.show()
