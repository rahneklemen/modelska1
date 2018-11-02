##zajci in lisice

import random
import matplotlib.pyplot as plt
import numpy as np





def zl(Z,L,alfa,beta,gamma,delta,dt):
    # print(alfa,beta,gamma,delta)
    # print(dt)
    ura=0
    
    zajci=[Z]
    lisice=[L]
    cas=[ura]
    i=0
    while(Z>0 and L>0):
        a1=np.random.poisson(Z*alfa*dt)-np.random.poisson(L*Z*beta*dt)
        # print('ok')
        b1=-np.random.poisson(L*gamma*dt)+np.random.poisson(L*Z*delta*dt)
        
        Z+=a1
        L+=b1
        ura+=dt
        
        zajci.append(Z)
        lisice.append(L)
        cas.append(ura)
        i+=1
    # print(i)
    return zajci,lisice,cas

l=50
z=200

a=5
b=4
g=5
d=4

delta_t=0.0001


zajci,lisice,cas=zl(z,l,a,b,g,d,delta_t)

plt.plot(cas,zajci)
plt.plot(cas,lisice)
plt.legend(['zajci','lisice'])
plt.ylabel('populacija')
plt.xlabel('čas')
plt.grid()
plt.savefig('zajci_lisice_populacija.png')
plt.show()

plt.plot(lisice,zajci)
plt.grid()
plt.xlabel('zajci')
plt.ylabel('lisice')
plt.savefig('zajcki_lisice_fazni.png')
plt.show()




porazdelitev=[]

for i in range(5000):
    zajci,lisice,cas=zl(z,l,a,b,g,d,delta_t)
    porazdelitev.append(cas[-1])

plt.hist(porazdelitev,bins=30,normed=True,histtype='step')
plt.xlabel('čas izumrtja')
plt.ylabel('število')
plt.grid()
plt.savefig('porazdelitev_zajcki_izumrli_cas.png')
plt.show()


povprecje=sum(porazdelitev)/len(porazdelitev)
print(povprecje)

##izumrli čas za zajce in lisice:
# izumrli_cas=[]
# izumrli_cas2=[]
# izumrli_cas3=[]
# 
# for i in range(1000):
#     # print(i)
#     if i%100==0:
#         print(i)
#     a,b=izumrtje(250,1,0,0.1)
#     a2,b2=izumrtje(250,1,0,0.01)
#     a3,b3=izumrtje(250,1,0,0.001)
#     izumrli_cas.append(a[-1])
#     izumrli_cas2.append(a2[-1])
#     izumrli_cas3.append(a3[-1])
#     
# 
# plt.hist(izumrli_cas,bins=30,normed=True,histtype='step')
# plt.hist(izumrli_cas2,bins=30,normed=True,histtype='step')
# plt.hist(izumrli_cas3,bins=30,normed=True,histtype='step')
# plt.xlabel('čas izumrtja')
# plt.ylabel('število')
# plt.grid()
# plt.title(r'porazdelitev izumrlega časa  $N_0=250$')
# plt.legend(['dt=0.1','dt=0.01','dt=0.001'])
# plt.savefig('porazdelitev_umrlicas_250.png')
# plt.show()

