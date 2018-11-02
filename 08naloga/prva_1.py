import numpy as np
import matplotlib.pyplot as plt
import random


def chi(por_prava,por_data):
    vsota=0

    for i in range(len(por_prava)):
        vsota+=((por_prava[i]-por_data[i])**2)/por_prava[i]
    return vsota

def kolmogorov_d(por_prava,por_data):
    kol_d=0
    for i in range(len(por_prava)):
        d_temp=abs(por_prava[i]-por_data[i])
        if d_temp>kol_d:
            kol_d=d_temp
    return kol_d

def kumulativna(data,prava,stevilo_vseh_stevk):
    data_kum = np.cumsum(data)/stevilo_vseh_stevk
    prava_kum = np.cumsum(prava)/stevilo_vseh_stevk

    return data_kum,prava_kum

def generator_porazdelitve(tabela, stevilo_binov):
    stevilo=len(tabela)
    porazdelitev_enak_prava=np.ones(stevilo_binov)*stevilo/stevilo_binov
    porazdelitev_enak_data=np.zeros(stevilo_binov)

    for stevka in tabela:
        indeks=int(stevka*stevilo_binov)
        porazdelitev_enak_data[indeks]+=1
    return porazdelitev_enak_data,porazdelitev_enak_prava


def porazdelitev(stevilo_iteracij,stevilo_random_stevk,stevilo_predalsckov):
    chi_stevke=[]
    d_stevke=[]
    for i in range(stevilo_iteracij):
        data=np.random.rand(stevilo_random_stevk)
        a,b=generator_porazdelitve(data,stevilo_predalsckov)
        kumul_a,kumul_b=kumulativna(a,b,stevilo_random_stevk)
        c=chi(b,a)
        d=kolmogorov_d(kumul_b,kumul_a)
        d_stevke.append(d)
        chi_stevke.append(c)
    return chi_stevke,d_stevke


a1,a2=generator_porazdelitve(np.random.rand(1000),100)

a,b=kumulativna(a1,a2,100)

plt.plot(a)
plt.plot(b)
plt.show()

pora_chi,pora_d=porazdelitev(100,35,10)
print('chi kvadrat',sum(pora_chi)/len(pora_chi))
plt.hist(pora_chi,bins=10)
plt.show()

print('kolmogorov',sum(pora_d)/len(pora_d))
plt.hist(pora_d,bins=10)
plt.show()




