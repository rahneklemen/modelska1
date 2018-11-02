import random
import matplotlib.pyplot as plt
import numpy as np

def povprecje(seznam):
    return sum(seznam)/len(seznam)

def varianca(seznam):
    x=povprecje(seznam)
    vsota=0
    for j in seznam:
        vsota+=(x-j)**2
    return  np.sqrt(vsota)/np.sqrt(len(seznam))

def energija(tabela,k):
    vsota=0
    for i in range(len(tabela)-1):
        vsota+=tabela[i]+k/2*(tabela[i]-tabela[i+1])**2
    return vsota
    
def sprememba_energije(tabela,n,delta,k):
    if tabela[n]==-12:
        return 0
    return delta+k/2*((-tabela[n-1]+tabela[n]+delta)**2+(-tabela[n+1]+tabela[n]+delta)**2-(-tabela[n-1]+tabela[n])**2-(-tabela[n+1]+tabela[n])**2)
    
def tezisce(podatki):
    return sum(podatki)/len(podatki)



def veriznica(podatki,vzmet,temperatura):
    sprememba=0
    while(sprememba<50000):
        polozaj=random.randint(1,len(podatki)-2)
        
        spremeni_visino=random.choice([-1,1])
        
        delta_energije=sprememba_energije(podatki,polozaj,spremeni_visino,vzmet)
        
        if delta_energije<0:
            podatki[polozaj]=podatki[polozaj]+spremeni_visino
        # elif delta_energije==0:
        #     podatki[polozaj]=-12
        else:
            ksi=np.random.rand()
            if ksi<np.exp(-1*delta_energije/temperatura):
                # print('delam')
                podatki[polozaj]=podatki[polozaj]+spremeni_visino
        sprememba+=1
    return podatki
    
    
    
    
    
##oblika veriznice za razlicne temperature:
# dolzina=18
# visina=[0 for i in range(dolzina)]
# visina[0]=0
# visina[dolzina-1]=0
#
# temp=1
# lala=veriznica(visina,1,temp)
#
# visina=[0 for i in range(dolzina)]
# lala2=veriznica(visina,1,temp*100)
# visina=[0 for i in range(dolzina)]
# lala3=veriznica(visina,1,temp*50)
#
# naslov1='veriznica_k_'+str(1)+'.png'
# naslov2='oblika verižnice pri različnih tremperaturah'
#
# plt.title(naslov2)
# plt.plot(lala,'-o',label=r'$T=1$')
# plt.plot(lala3,'-o',label=r'$T=50$')
# plt.plot(lala2,'-o',label=r'$T=100$')
# plt.grid()
# plt.legend(loc=9)
# plt.savefig(naslov1)
# plt.show()

##oblika veriznice za razlicne $K$
#
# dolzina=18
# visina=[0 for i in range(dolzina)]
# visina[0]=0
# visina[dolzina-1]=0
#
# temp=1
# lala=veriznica(visina,1,temp)
#
# visina=[0 for i in range(dolzina)]
# lala2=veriznica(visina,5,temp)
# visina=[0 for i in range(dolzina)]
# lala3=veriznica(visina,10,temp)
#
# naslov1='veriznica_temp_'+str(temp)+'.png'
# naslov2=r'oblika verižnice pri različnih vrednostih $K$'
#
# plt.title(naslov2)
# plt.plot(lala,'-o',label=r'$K=1$')
# plt.plot(lala2,'-o',label=r'$K=5$')
# plt.plot(lala3,'-o',label=r'$K$=10')
# plt.grid()
# plt.legend(loc=10)
# plt.savefig(naslov1)
# plt.show()




##odvisnost energije od temperature

x=[0.1,1,50,100,200,300,400,500,600,800,1000,1200,1500,1800,2000,2500]
y=[]
y_err=[]


for i in x:
    temporary=[]
    for j in range(20):
        visina = np.zeros(18)
        if j==10:
            print(10)
        temporary.append(energija(veriznica(visina,1,i),1))
    y.append(povprecje(temporary))
    y_err.append(varianca(temporary))


plt.errorbar(x,y,yerr=y_err)

plt.title('odvisnost ravnovesne energije v odvisnosti od temperature')
plt.ylabel('Energija')
plt.xlabel('Temperatura')
plt.grid()

plt.savefig('eviosnost_energije_od_energije_veriznica.png')
plt.show()






#
# print(x)
# y=np.ones(len(x))
# y1=[]
# x1=[]
# k=1
#
# for j in range(len(x)):
#     temp_temp=[]
#     for l in range(10):
#         print(j,l)
#         temp_temp.append(energija(veriznica(visina,k,x[j]),k))
#     y[j]=sum(temp_temp)/len(temp_temp)
#     y1.append(temp_temp)
#     x1.append(x[j])
#
# plt.plot(x1,y1,'ob')
# plt.plot(x,y,'-r')
# plt.grid()
# # plt.legend([)
#
# plt.xlabel('temperatura')
# plt.ylabel('energija')
# plt.title('temperaturna odvisnost energije   k='+str(k))
# plt.savefig('temperatuna_odvisnost_veriznica'+'k_'+str(k)+'.png')
# # plt.xscale('log')
# plt.show()