import numpy as np
import matplotlib.pyplot as plt
import random
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import time
from mpl_toolkits.mplot3d import Axes3D

def lcg(n):
    '''

    generator random stevik na podlagi linear congruential generator:
    x_i+1 = (a*x_i + c )mod_m

    a = 1140671485
    c = 128201163
    m = 2**24


    Returns
    -------
    seznam - array n random stevilk med 0 in 1
    Parameters
    ----------
    n - stevilo generiranih random stevk

    Returns
    -------
    seznam - array n random stevilk med 0 in 1

    '''
    a = 1103515245
    c = 123454
    m = 2**32

    x0=random.randint(1,100)
    # print(x0)
    seznam=[]

    for i in range(n):
        x0=(a*x0+c) % m
        seznam.append(x0/m)
    return seznam
#

def funkcija_histogram(seznam, stevilo_binov):
    stevilo_binov=stevilo_binov+1
    hist=np.zeros(stevilo_binov)
    normalizacija=len(seznam)
    for stevilka in seznam:
        indeks=int(stevilka*stevilo_binov)
        hist[indeks]+=1
    hist=hist/normalizacija
    return hist


def histogram(stevilke,predalckov):
    N=len(stevilke)
    porazdelitev=np.zeros(predalckov)

    for k in stevilke:
        porazdelitev[int(k//(1/predalckov))]+=1
    #normalizacija:
    porazdelitev=porazdelitev/(N/predalckov)
    return porazdelitev

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


def porazdelitev_d_h(stevilo_iteracij,stevilo_stevk,stevilo_predalckov):
    D=[]
    chi=[]

    for i in range(stevilo_iteracij):
        a,b=d_h(np.ones(stevilo_predalckov),histogram(np.random.random(stevilo_stevk),stevilo_predalckov))
        D.append(b*np.sqrt(stevilo_stevk))
        chi.append(a*stevilo_stevk/stevilo_predalckov)
    return D,chi

def porazdelitev_d_h2(stevilo_iteracij,stevilo_stevk,stevilo_predalckov):
    D=[]
    chi=[]

    for i in range(stevilo_iteracij):
        a,b=d_h(np.ones(stevilo_predalckov),histogram(lcg(stevilo_stevk),stevilo_predalckov))
        D.append(b*np.sqrt(stevilo_stevk))
        chi.append(a*stevilo_stevk/stevilo_predalckov)
        # print(a,b)
    return D,chi

def povprecje(seznam):
    return sum(seznam)/len(seznam)

def varianca(seznam):
    x=povprecje(seznam)
    vsota=0
    for j in seznam:
        vsota+=(x-j)**2
    return  np.sqrt(vsota)/np.sqrt(len(seznam))




##------------------------------------------------------------------------------------------------
##prva naloga, prvi del: samo porazdelitev

#
# N=100
# predal=10
#
# x=[i/(predal+1) for i in range(predal)]
# a1=np.random.random(N)
# b1=lcg(N)
#
# a=funkcija_histogram(a1,predal)
# b=funkcija_histogram(b1,predal)
#
# naslov='enakomerna_porazdelitev_N'+str(N)+'.png'
#
# plt.title('enakomerno porazdeljena števila, N='+str(N))
# plt.hist(a1,range =(0,1),normed = True,histtype = 'step',label='vgrajeni')
# plt.hist(b1,range =(0,1),normed =True,histtype = 'step',label='lcg')
# plt.grid()
# plt.legend(loc=3)
# plt.ylabel(r'$\frac{dN}{dx}$')
# plt.xlabel('x_i')
#
# plt.savefig(naslov)
# plt.show()


##------------------------------------------------------------------------------------------------
##prva naloga drugi delo-porazdelitev chi in D
#
#
#
# ##c1,d1 vrajeni
# ##c12,d12 lcg
# for i in range(2,5):
#     stevilo_chi=1000
#     stevilo_random=10**i
#     stevilo_binov=10
#     d1,c1=porazdelitev_d_h(stevilo_chi,stevilo_random,stevilo_binov)
#     d12,c12=porazdelitev_d_h2(stevilo_chi,stevilo_random,stevilo_binov)
#
#     naslov='potazdelitev_chi_N_'+str(stevilo_random)+'.png'
#     naslov2=r'porazdelitev $\chi^2$, N='+str(stevilo_random)
#
#     plt.title(naslov2)
#     plt.hist(c1,bins=20,normed=True,histtype = 'step',label='vgrajeni')
#     plt.hist(c12,bins=20,normed=True,histtype = 'step',label='lcg')
#     plt.legend()
#     plt.xlabel(r'$\chi^2$')
#     plt.ylabel(r'$\frac{dP}{d\chi^2}$')
#     plt.grid()
#
#     plt.savefig(naslov)
#     plt.show()
#
#     naslov='potazdelitev_DsqrtN_'+str(stevilo_random)+'.png'
#     naslov2=r'porazdelitev $D\sqrt{N}$, N='+str(stevilo_random)
#     plt.title(naslov2)
#     plt.hist(d1,bins=20,normed=True,histtype = 'step',label='vgrajeni')
#     plt.hist(d12,bins=20,normed=True,histtype = 'step',label='lcg')
#     plt.legend()
#     plt.xlabel(r'$(D\sqrt{N}$')
#     plt.ylabel(r'$\frac{dP}{d(D\sqrt{N})}$')
#     plt.grid()
#
#     plt.savefig(naslov)
#     plt.show()
#     print('stevilo N=',stevilo_random)
#     print(povprecje(d1),varianca(d1))
#     print(povprecje(c1),varianca(c1))
#
#     print(povprecje(d12),varianca(d12))
#     print(povprecje(c12),varianca(c12))
#



##------------------------------------------------------------------------------------------------
##prva naloga tretji delo test za dvodimenzionalno

##stevilo nakljucnih točk:
n=100

##velikost mreže:
n_bins=10

x=np.random.random(n)
y=np.random.random(n)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


predalcki=[i/n_bins for i in range(n_bins+1)]
hist, xedges, yedges = np.histogram2d(x, y, bins=(predalcki,predalcki),normed='True')
print(hist)
print(xedges)

# print(len(xedges))
# print(predalcki)
# print(len(predalcki))
# print(len(hist))
# elements = (len(xedges) - 1) * (len(yedges) - 1)
# xpos, ypos = np.meshgrid(xedges[:-1], yedges[:-1])
#
# xpos = xpos.flatten()
# ypos = ypos.flatten()
# zpos = np.zeros(elements)
# dx = 1/n_bins * np.ones_like(zpos)
# dy = dx.copy()
# dz = hist.flatten()
#
#
#
# ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')
#
#
# plt.title('stevilo generiranih točk:'+str(n))
# naslov='porazdelitev2D_N_'+str(n)+'.png'
# plt.savefig(naslov)
# plt.show()




def chi_2d(matrika_prava,matrika_meritev,stevilo_stevk):
    chi=0
    for i in range(len(matrika_prava)):
        for j in range(len(matrika_prava[0])):
            chi+=((matrika_prava[j][i]-matrika_meritev[j][i])**2/matrika_prava[j][i])
    return chi*stevilo_stevk/len(matrika_meritev)/len(matrika_meritev[0])


for j in range(3,6):
    chi=[]

    for i in range(1000):
        n=10**j

        ##velikost mreže:
        n_bins=10

        x=np.random.random(n)
        y=np.random.random(n)


        predalcki=[i/n_bins for i in range(n_bins+1)]
        hist, xedges, yedges = np.histogram2d(x, y, bins=(predalcki,predalcki),normed='True')



        analiticna=np.array([ [1 for i in range(n_bins)] for j in range(n_bins)])




        # print(analiticna)
        chi.append(chi_2d(analiticna,hist,n))
    print('N=',n)
    print('povprecje')
    print(povprecje(chi))
    print('variacija:',varianca(chi))






