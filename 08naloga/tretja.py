##primerjava box-muller in konvoluccijskega generatorja za generiranje gaussove porazdelitve
from numpy import random, sqrt, log, sin, cos, pi
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from datetime import datetime


####testiranje gauss porazdelitve:
def povprecje(seznam):
    return sum(seznam)/len(seznam)

def varianca(seznam):
    x=povprecje(seznam)
    vsota=0
    for j in seznam:
        vsota+=(x-j)**2
    return  np.sqrt(vsota)/np.sqrt(len(seznam))


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


# transformation function
def gauss1(n):
    u1 = random.rand(n)
    u2 = random.rand(n)
    z1 = sqrt(-2 * log(u1)) * cos(2 * pi * u2)
    return z1


def gauss2(n):
    a = np.array([])
    for i in range(n):
        vsota = sum(random.rand(12)) - 6
        a = np.append(a, vsota)
        # print(a)
    return a

#tretja-plotanje porazdelitve
#
#
# m = 100
# stolpci=10
#
# z1 = gauss1(m)
# k1 = gauss2(m)
# #
# hist1, x_predalcki = np.histogram(z1, bins=stolpci,normed=True)
# # hist1, x_predalcki = np.histogram(z1, bins=stolpci)
# hist2, x_predalcki = np.histogram(k1,x_predalcki,normed=True)
# # hist2, x_predalcki = np.histogram(k1,x_predalcki)
#
# x_tocke=[]
#
# for i in range(stolpci):
#     x_tocke.append((x_predalcki[i]+x_predalcki[i+1])/2)
#
#
# gauss_tocno=norm.pdf(x_tocke)
#
# plt.plot(x_tocke,hist1,label='1')
# plt.plot(x_tocke,hist2,label='2')
# plt.plot(x_tocke,gauss_tocno/2,label='tocna')
# plt.legend()
# plt.show()
#
#
#
# if min(k1)<min(z1):
#     a=min(k1)
# else:
#     a=min(z1)
#
# if max(k1)<max(z1):
#     b=max(z1)
# else:
#     b=max(k1)
#
#
#
#
#
# x_gauss=np.arange(a,b,(b-a)/100)
# y_gauss=norm.pdf(x_gauss)
#


# ime='boxmark_konvolucija_gauss_n_'+str(m)+'.png'
# plt.hist(z1, histtype='step', bins=stolpci, normed=True,label='Boxmark-Muller')
# plt.hist(k1, color='r', histtype='step', bins=stolpci, normed=True,label='konvolucija')
# plt.plot(x_gauss,y_gauss,label='analitična')
# plt.legend()
# plt.grid()
# plt.savefig(ime)
# plt.show()



##tretja-vrednost chi D

for k in range(3,6):
    m=10**k
    stolpci=50
    chi1=[]
    D1=[]

    chi2=[]
    D2=[]
    for j in range(50):
        z1 = gauss1(m)
        k1 = gauss2(m)
        hist1, x_predalcki = np.histogram(z1, bins=stolpci)
        hist2, x_predalcki = np.histogram(k1, x_predalcki)
        x_tocke=[]

        for i in range(stolpci):
            x_tocke.append((x_predalcki[i]+x_predalcki[i+1])/2)
        gauss_tocno=norm.pdf(x_tocke)*m/stolpci*(x_predalcki[-1]-x_predalcki[0])
        # print(x_tocke)

        a1,b1=d_h(gauss_tocno,hist1)

        chi1.append(a1)
        D1.append(b1*np.sqrt(m))

        a2,b2=d_h(gauss_tocno,hist2)
        chi2.append(a2)
        D2.append(b2*np.sqrt(m))

    print('-------------------\nN=',m,'stolpci',stolpci)
    print('boxmark:')
    print('chi')
    print(povprecje(chi1),varianca(chi1))
    print('D')
    print(povprecje(D1),varianca(D1))

    print('konvolucija:')
    print('chi')
    print(povprecje(chi2),varianca(chi2))
    print('D')
    print(povprecje(D2),varianca(D2))