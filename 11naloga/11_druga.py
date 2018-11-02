##matrika prehodov

from scipy.stats import poisson
import random
import matplotlib.pyplot as plt
import numpy as np

##definranje funkcij:

def populacija(tabela):
    vsota=0
    for i in range(len(tabela)):
        vsota+=i*tabela[i]
    return vsota

def transposed(matrix):
   return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def izumrli_cas(N,dt,beta_roj,beta_smrt):
    dolzina=N+10
    matrika=np.zeros((dolzina,dolzina))
    matrika[0][0]=1
    
    # r=np.random.poisson(dolzina*beta_roj*dt)/dolzina
    # s=np.random.poisson(dolzina*beta_smrt*dt)/dolzina
    
    r=dolzina*beta_roj*dt
    s=dolzina*beta_smrt*dt
    matrika[dolzina-1][dolzina-1]=1-s-r
    matrika[dolzina-2][dolzina-1]=s
    
    
    for i in range(1,dolzina-1):
        # r=np.random.poisson(i*beta_roj*dt)
        # s=np.random.poisson(i*beta_smrt*dt)
        r=i*beta_roj*dt
        s=i*beta_smrt*dt
        
        print(s,r)
        matrika[i-1][i]=s
        matrika[i][i]=1-s-r
        matrika[i+1][i]=r
    
    
    plt.matshow(transposed(matrika))
    plt.colorbar()
    plt.show()
    
    print('----')
    ##generirajmo začetno porazdelitev:
    
    vektor=np.zeros(dolzina)
    vektor[N]=1
    
    ##pa začnimo s nalogo:
    # print(matrika)
    # print(matrika.dot(vektor))
    rezultat=[]
    stevilo=[]
    ura=[]
    vektor1=vektor
    i=0
    a=N
    totalni_porazdelitev=[]
    
    while (a>1):
        a=populacija(vektor)
        if i%10==0:
            print(i,a)
            rezultat.append(vektor)
        totalni_porazdelitev.append(vektor)
        vektor=matrika.dot(vektor)
        
        stevilo.append(a)
        ura.append(i*dt)
        i+=1
    
    
    prva=int(40)
    druga=int(i//20)
    tretja=int(i//10)
    cetrtina=int(i//5)
    predzadnja=int(i//2)
    zadnja=int((i-1))
    
    print(prva,druga,tretja,cetrtina,predzadnja,zadnja)
    plt.plot(totalni_porazdelitev[0])
    plt.plot(totalni_porazdelitev[prva])
    plt.plot(totalni_porazdelitev[druga])
    plt.plot(totalni_porazdelitev[tretja])
    plt.plot(totalni_porazdelitev[cetrtina])
    plt.plot(totalni_porazdelitev[predzadnja])
    plt.plot(totalni_porazdelitev[zadnja])
    plt.grid()
    plt.ylabel('verjetnost')
    plt.xlabel('vektor populacije')
    plt.ylim(ymax=0.5)
    plt.savefig('test.png')
    plt.show()

    cajt=[i*0.01 for i in range(600)]
    analiticna=[250*np.exp(-i*0.01) for i in range(600)]
    
    plt.plot(ura,stevilo)
    plt.xlabel('Čas')
    plt.ylabel('populacija')
    # plt.plot(cajt,analiticna)
    plt.legend(['matrika prehodov', 'analitična'])
    plt.grid()
    plt.savefig('matrika_porazdelitev_beta_0.png')
    plt.show()
    return rezultat,stevilo
    
##definirajmo parametre:
N=250
dolzina=300

dt=0.001
beta_roj=0
beta_smrt=1

ponovitev=3000

##pognana funkcija

matrika,ljudje=izumrli_cas(N,dt,beta_roj,beta_smrt)

plt.matshow(transposed(matrika))
plt.colorbar()
plt.xlabel('čas')
plt.ylabel('verjetnostni vektor')
plt.savefig('matrika_porazdelitve_beta_0.png')
plt.show()

# plt.plot(vektor)
# plt.plot(vektor1)
# plt.plot(vektor2)
# plt.show()
# 

# 
# matrika2=[rezultat[i] for i in range(len(rezultat)) if i%25==0]
# lala=transposed(matrika2)
# 
# plt.matshow(matrika2)
# plt.colorbar()
# plt.show()