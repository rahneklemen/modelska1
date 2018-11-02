#optimizacija hitrosti
import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt




def dolzina(x,zacetna_hit):
    N=len(x)-1
    return sum(x)-x[-1]/2-zacetna_hit/2-N




def funkcija(tocke_hitrost,zacet_speed,beta,limit):

    n=len(tocke_hitrost)
    dt=1/(n)
    vsota1=0

    #zacetno
    vsota1+=0.5*((tocke_hitrost[0]-zacet_speed))**2

    for i in range(n-1):
        vsota1+=((tocke_hitrost[i+1]-tocke_hitrost[i]))**2
    vsota1+=0.5*((tocke_hitrost[i]-tocke_hitrost[i-1]))**2

    for i in range(n-1):
        vsota1+=np.exp(beta*(tocke_hitrost[i]-limit))*dt
    vsota1+=0.5*np.exp(beta*(tocke_hitrost[n-1]-limit))*dt


    return vsota1

def optimizacija(zacetna_hitrost,beta,limit,N):
    hitrost=np.ones(N)*zacetna_hitrost
    opt=optimize.minimize(funkcija,hitrost,args=(zacetna_hitrost,beta,limit),constraints=({'type': 'eq', 'fun': lambda x: sum(x)-x[-1]/2+zacetna_hitrost/2-N})).x
    return np.append([zacetna_hitrost],opt)




# #Kako sprememba bete vpliva na trajektorijo
# max=1
# N=100
# x=np.arange(0,1.01,0.01)
#
# res=optimizacija(2,1,max,N)
# print(dolzina(res,2))
#
# res2=optimizacija(2,0,max,N)
# print(dolzina(res2,1))
#
# res3=optimizacija(2,3,max,N)
# print(dolzina(res3,0.5))
#
# res4=optimizacija(2,0.5,max,N)
# print(dolzina(res4,0.7))
# print(res4)
# print(sum(res4))
#
# plt.plot(x,res2,label=r'$\beta = 0$')
# plt.plot(x,res4,label=r'$\beta = 0.5$')
# plt.plot(x,res,label=r'$\beta = 1$')
# plt.plot(x,res3,label=r'$\beta = 3$')
#
# plt.ylabel('hitrost')
# plt.xlabel('čas')
# plt.title(r'omejitev hitrosti, $v_{MAX}=1$')
# plt.grid()
# plt.legend()
# plt.savefig('omejitev_hitrosti_v_max_konstantna.png')
# plt.show()

#kako vpliva V_MAX na frajektorijo:

beta=2
N=100
x=np.arange(0,1.01,0.01)

res=optimizacija(2,beta,1,N)
print(dolzina(res,2))

res2=optimizacija(2,beta,0.6,N)
print(dolzina(res2,1))

res3=optimizacija(2,beta,2,N)
print(dolzina(res3,0.5))

res4=optimizacija(2,beta,3,N)
print(dolzina(res4,0.7))
print(res4)
print(sum(res4))

plt.plot(x,res2,label=r'$v_{MAX} = 0.6$')
plt.plot(x,res,label=r'$v_{MAX} = 1$')
plt.plot(x,res3,label=r'$v_{MAX} = 2$')
plt.plot(x,res4,label=r'$v_{MAX} = 3$')

plt.ylabel('hitrost')
plt.xlabel('čas')
plt.title(r'omejitev hitrosti, $\beta =2$')
plt.grid()
plt.legend()
plt.savefig('omejitev_hitrosti_beta_konstantna.png')
plt.show()