#optimizacija hitrosti
import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt


def v(t,v_0):
    l=1
    t_0=1
    lamda=6/(t_0**3)*(l-v_0*t_0)

    return -lamda/4*t**2+lamda/2*t_0*t+v_0

x=np.arange(0,1.1,0.1)
y=v(x,0.7)
y2=v(x,2)


def dolzina(x,zacetna_hit):
    N=len(x)-1
    return sum(x)-x[-1]/2-zacetna_hit/2-N




def funkcija(tocke_hitrost,zacet_speed):

    n=len(tocke_hitrost)
    dt=1/(n-1)
    vsota1=0

    #zacetno
    vsota1+=0.5*((tocke_hitrost[0]-zacet_speed))**2

    for i in range(n-1):
        vsota1+=((tocke_hitrost[i+1]-tocke_hitrost[i]))**2
    vsota1+=0.5*((tocke_hitrost[i]-tocke_hitrost[i-1]))**2

    return vsota1

def optimizacija(zacetna_hitrost,N):
    hitrost=np.ones(N)*zacetna_hitrost
    opt=optimize.minimize(funkcija,hitrost,args=zacetna_hitrost,constraints=({'type': 'eq', 'fun': lambda x: sum(x)-x[-1]/2+zacetna_hitrost/2-N})).x
    return np.append([zacetna_hitrost],opt)

N=10
res=optimizacija(2,N)
print(dolzina(res,2))

res2=optimizacija(1,N)
print(dolzina(res2,1))

res3=optimizacija(0.5,N)
print(dolzina(res3,0.5))

res4=optimizacija(0.7,N)
print(dolzina(res4,0.7))
print(res4)
print(sum(res4))

print(len(x))
print(len(res))

naslov='primerjava_anal_num_n_'+str(N)+'.png'
plt.plot(x,y2,'-',label=r'analitična $v(0)=2$')
plt.plot(x,res,'o',label=r'numerična $v(0)=2$')
# plt.plot(res2)
# plt.plot(res3)
plt.plot(x,y,'-',label=r'analitična $v(0)=0.7$')
plt.plot(x,res4,'o',label=r'analitična $v(0)=0.7$')
plt.legend()
plt.grid()
plt.title('primerjava analitične rešitve z numerični minimizacijo')
plt.ylabel('hitrost')
plt.xlabel('čas')
plt.savefig(naslov)
plt.show()
