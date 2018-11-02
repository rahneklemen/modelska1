import random
import matplotlib.pyplot as plt
import numpy as np


def izumrtje(N,beta_smrt,beta_roj,dt):
    ura=0
    
    populacija=[N]
    cas=[ura]
    i=0
    while(N>0):
        delta=np.random.poisson(N*beta_smrt*dt)
        delta2=np.random.poisson(N*beta_roj*dt)
        # print(delta)
        N-=delta
        N+=delta2
        ura+=dt
        populacija.append(N)
        cas.append(ura)
        i+=1
    
    return cas,populacija



cas,populacija=izumrtje(25,1,0,0.001)
cas2,populacija2=izumrtje(25,1,0,0.01)
cas3,populacija3=izumrtje(25,1,0,0.1)
cajt=[i*0.01 for i in range(600)]
analiticna=[25*np.exp(-i*0.01) for i in range(600)]

plt.plot(cas,populacija)
plt.plot(cas2,populacija2)
plt.plot(cas3,populacija3)
plt.plot(cajt,analiticna)
plt.title(r' $\beta_s=1$  $ N_0=25$')
plt.ylabel('populacija')
plt.xlabel('čas')
plt.legend(['dt=0.001','dt=0.01','dt=0.1','analitična'])
plt.grid()
plt.savefig('populacija_umiranje_preprosto_25.png')
plt.show()

plt.plot(cas,populacija)
plt.plot(cas2,populacija2)
plt.plot(cas3,populacija3)
plt.plot(cajt,analiticna)
plt.title(r'logaritemska skala $\beta_s=1$  $ N_0=25$')
plt.ylabel('populacija')
plt.xlabel('čas')
plt.yscale('log')
plt.ylim(ymin=0.1)
plt.legend(['dt=0.001','dt=0.01','dt=0.1','analitična'])
plt.grid()
plt.savefig('populacija_umiranje_preprosto_25_log.png')
plt.show()

cas,populacija=izumrtje(250,1,0,0.001)
cas2,populacija2=izumrtje(250,1,0,0.01)
cas3,populacija3=izumrtje(250,1,0,0.1)

cajt=[i*0.01 for i in range(700)]
analiticna=[250*np.exp(-i*0.01) for i in range(700)]

plt.plot(cas,populacija)
plt.plot(cas2,populacija2)
plt.plot(cas3,populacija3)
plt.plot(cajt,analiticna)
plt.title(r' $\beta_s=1$  $ N_0=250$')
plt.ylabel('populacija')
plt.xlabel('čas')
plt.legend(['dt=0.001','dt=0.01','dt=0.1','analitična'])
plt.grid()
plt.savefig('populacija_umiranje_preprosto_250.png')
plt.show()

plt.plot(cas,populacija)
plt.plot(cas2,populacija2)
plt.plot(cas3,populacija3)
plt.plot(cajt,analiticna)
plt.title(r'logaritemska skala $\beta_s=1$  $ N_0=250$')
plt.ylabel('populacija')
plt.xlabel('čas')
plt.yscale('log')
plt.ylim(ymin=0.1)
plt.legend(['dt=0.001','dt=0.01','dt=0.1','analitična'])
plt.grid()
plt.savefig('populacija_umiranje_preprosto_250_log.png')
plt.show()


izumrli_cas=[]

for i in range(1000):
    # print(i)
    a,b=izumrtje(250,5,1,0.01)
    c=a[-1]
    izumrli_cas.append(c)

plt.hist(izumrli_cas,bins=20,normed=True)
plt.grid()
plt.xlabel('čas izumrtja')
plt.ylabel('število')
plt.show()


