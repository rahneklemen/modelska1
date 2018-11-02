## PORAZDELITEV ODDAJANJA MODELSKE NALOGE ZA LETO 2011
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def gaussian(x, mu, sig):
    return (2*sig**2*np.pi)**-0.5*np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))


def kolmogorov_d(por_prava,por_data):
    kol_d=0
    for i in range(len(por_prava)):
        d_temp=abs(por_prava[i]-por_data[i])
        if d_temp>kol_d:
            kol_d=d_temp
    return kol_d



def vrsta_to_min(seznam):
    min=0
    for i in range(len(seznam)):
        if i==0:
            min+=int(seznam[0])*60
        if i==1:
            min+=int(seznam[1])
        if i==2:
            min+=(int(seznam[2])/60)
    return min

def kumulativna(hist):
    norma=sum(hist)
    a=0
    kumul=[]
    for i in hist:
        # print(a)
        a+=(i/norma)
        kumul.append(a)
    return kumul

def d_h(prava,moja):
    chi=0
    # print(moja)

    for i in range(len(prava)):
        chi+=((prava[i]-moja[i])**2/prava[i])

    kumul_prava=kumulativna(prava)
    kumul_moja=kumulativna(moja)

    d=0
    for i in range(len((kumul_moja))):
        if abs(kumul_moja[i]-kumul_prava[i])>d:
            d=abs(kumul_moja[i]-kumul_prava[i])

    return chi,d

vse_ure=[]

##leto 2011:
matrika=[]
vse_ure11=[]
for i in range(12):
    vrstica=[]
    ime='podatki/mod_tm11_1'+str(i+1).zfill(2)+'.dat'
    # print(ime)

    f = open(ime, 'r',encoding='utf-8')
    data_file=f.readlines()
    for vrsta in data_file:
        vrsta=vrsta.strip('\n')
        if vrsta[0]=='-':
            vrsta=vrsta.strip('-')
            vrsta=vrsta.split(':')
            minute=-1*vrsta_to_min(vrsta)
        else:
            vrsta=vrsta.split(':')
            minute=vrsta_to_min(vrsta)
        # print(vrsta)
        vrstica.append(minute)
        vse_ure11.append(minute)
        vse_ure.append(minute)
    matrika.append(vrstica)
# [print(x) for x in matrika]

##2013:
matrika13=[]
vse_ure13=[]

for i in range(6):
    vrstica=[]
    ime='podatki/mod_tm13_1'+str(i+1).zfill(2)+'.dat'
    # print(ime)

    f = open(ime, 'r',encoding='utf-8')
    data_file=f.readlines()
    for vrsta in data_file:
        vrsta=vrsta.strip('\n')
        if vrsta[0]=='-':
            vrsta=vrsta.strip('-')
            vrsta=vrsta.split(':')
            minute=-1*vrsta_to_min(vrsta)
        else:
            vrsta=vrsta.split(':')
            minute=vrsta_to_min(vrsta)
        # print(vrsta)
        vrstica.append(minute)
        vse_ure13.append(minute)
        vse_ure.append(minute)
    matrika13.append(vrstica)
# [print(x) for x in matrika]

##2010:
matrika10=[]
vse_ure10=[]

for i in range(13):
    vrstica=[]
    ime='podatki/mod_tm10_1'+str(i+1).zfill(2)+'.dat'
    # print(ime)

    f = open(ime, 'r',encoding='utf-8')
    data_file=f.readlines()
    for vrsta in data_file:
        vrsta=vrsta.strip('\n')
        if vrsta[0]=='-':
            vrsta=vrsta.strip('-')
            vrsta=vrsta.split(':')
            minute=-1*vrsta_to_min(vrsta)
        else:
            vrsta=vrsta.split(':')
            minute=vrsta_to_min(vrsta)
        # print(vrsta)
        vrstica.append(minute)
        vse_ure10.append(minute)
        vse_ure.append(minute)
    matrika10.append(vrstica)
# [print(x) for x in matrika]





##---------------------------------------



# plt2.hist(vse_ure10,cumulative=True ,normed=True ,histtype='step',bins=(len(vse_ure10)))
# plt2.hist(vse_ure11,cumulative=True , normed=True,histtype='step',bins=(len(vse_ure11)))
# plt2.hist(vse_ure13,cumulative=True ,normed=True ,histtype='step',bins=(len(vse_ure13)))
# plt.legend(['leto 2010','leto 2011','leto 2013'],loc=2)
# plt.xlabel('čas oddaje (min)')
# plt.ylabel('delež oddanih nalog')
# plt2.grid()
# plt.savefig('kumulativna_oddaje_nalog_posamezna_leta.png')
# plt2.show()

print(len(vse_ure))
cas,sirina=norm.fit(vse_ure)
print('čas,širina')
print(cas,sirina)


stolpci=10

hist1, x_predalcki = np.histogram(vse_ure, bins=stolpci)
x_tocke=[]

for i in range(stolpci):
    x_tocke.append((x_predalcki[i]+x_predalcki[i+1])/2)

gauss_pravi=gaussian(x_tocke,cas,sirina)*len(vse_ure)/stolpci*(x_predalcki[-1]-x_predalcki[0])
# print(gauss_pravi)

x=np.arange(x_tocke[0],x_tocke[-1],5)
gauss2=gaussian(x,cas,sirina)*len(vse_ure)/stolpci*(x_predalcki[-1]-x_predalcki[0])
print(gauss2)




plt.ylabel('število oddanih nalog')
plt.xlabel('čas [min]')
plt.plot(x_tocke,hist1,'o-',label='časi oddaj')
plt.plot(x,gauss2,label='Gauss fit')
plt.grid()
plt.savefig('oddaje_nalog_gauss.png')
plt.show()

a1,b1=d_h(gauss_pravi,hist1)

print(a1)
print(b1*np.sqrt(len(vse_ure)))