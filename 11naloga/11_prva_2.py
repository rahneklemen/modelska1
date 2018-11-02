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



# cas,populacija=izumrtje(25,5,4,0.001)
# cas2,populacija2=izumrtje(25,5,4,0.01)
# cas3,populacija3=izumrtje(25,5,4,0.1)
# cajt=[i*0.01 for i in range(500)]
# analiticna=[25*np.exp(-i*0.01) for i in range(500)]
# 
# plt.plot(cas,populacija)
# plt.plot(cas2,populacija2)
# plt.plot(cas3,populacija3)
# plt.plot(cajt,analiticna)
# plt.title(r' $\beta_s=5$    $\beta_r=4$   $ N_0=25$')
# plt.ylabel('populacija')
# plt.xlabel('čas')
# plt.legend(['dt=0.001','dt=0.01','dt=0.1','analitična'])
# plt.grid()
# plt.savefig('populacija_umiranje_rojstvo_preprosto_25.png')
# plt.show()
# 
# 
# 
# cas,populacija=izumrtje(250,5,4,0.001)
# cas2,populacija2=izumrtje(250,5,4,0.01)
# cas3,populacija3=izumrtje(250,5,4,0.1)
# 
# cajt=[i*0.01 for i in range(700)]
# analiticna=[250*np.exp(-i*0.01) for i in range(700)]
# 
# plt.plot(cas,populacija)
# plt.plot(cas2,populacija2)
# plt.plot(cas3,populacija3)
# plt.plot(cajt,analiticna)
# plt.title(r' $\beta_s=5$    $\beta_r=4$  $ N_0=250$')
# plt.ylabel('populacija')
# plt.xlabel('čas')
# plt.legend(['dt=0.001','dt=0.01','dt=0.1','analitična'])
# plt.grid()
# plt.savefig('populacija_umiranje_rojstvo_preprosto_250.png')
# plt.show()




##porazdelitev izumrlih časov N=250
izumrli_cas=[]
izumrli_cas2=[]
izumrli_cas3=[]

for i in range(1000):
    # print(i)
    if i%100==0:
        print(i)
    a,b=izumrtje(250,5,4,0.1)
    a2,b2=izumrtje(250,5,4,0.01)
    a3,b3=izumrtje(250,5,4,0.001)
    izumrli_cas.append(a[-1])
    izumrli_cas2.append(a2[-1])
    izumrli_cas3.append(a3[-1])
    

plt.hist(izumrli_cas,bins=30,normed=True,histtype='step')
plt.hist(izumrli_cas2,bins=30,normed=True,histtype='step')
plt.hist(izumrli_cas3,bins=30,normed=True,histtype='step')
plt.xlabel('čas izumrtja')
plt.ylabel('število')
plt.grid()
plt.title(r'porazdelitev izumrlega časa   $\beta_s=5$    $\beta_r=4$   $N_0=250$')
plt.legend(['dt=0.1','dt=0.01','dt=0.001'])
plt.savefig('porazdelitev_umrlirojstvocas_250.png')
plt.show()





##porazdelitev izumrlih časov N=25
izumrli_cas=[]
izumrli_cas2=[]
izumrli_cas3=[]

for i in range(1000):
    # print(i)
    if i%100==0:
        print(i)
    a,b=izumrtje(25,5,4,0.1)
    a2,b2=izumrtje(25,5,4,0.01)
    a3,b3=izumrtje(25,5,4,0.001)
    izumrli_cas.append(a[-1])
    izumrli_cas2.append(a2[-1])
    izumrli_cas3.append(a3[-1])
    

plt.hist(izumrli_cas,bins=30,normed=True,histtype='step')
plt.hist(izumrli_cas2,bins=30,normed=True,histtype='step')
plt.hist(izumrli_cas3,bins=30,normed=True,histtype='step')
plt.xlabel('čas izumrtja')
plt.ylabel('število')
plt.grid()
plt.title(r'porazdelitev izumrlega časa   $\beta_s=5$    $\beta_r=4$    $N_0=25$')
plt.legend(['dt=0.1','dt=0.01','dt=0.001'])
plt.savefig('porazdelitev_umrlirojstvocas_25.png')
plt.show()



