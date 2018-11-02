import numpy as np
import matplotlib.pyplot as plt
from nitime import algorithms as alg










st_tock=512

delta_tocke=2*np.pi/st_tock
print(1/delta_tocke)
x=np.arange(0,2*np.pi,delta_tocke)


delta=15
osnovna=75
st_polov=20

signal=np.sin(osnovna*x)+np.sin((osnovna+delta)*x)

print(delta_tocke*osnovna/2/np.pi,delta_tocke*(osnovna+delta)/2/np.pi)
a, b = alg.AR_est_YW(signal, st_polov)
spekter = alg.autoregressive.AR_psd(a, b)



normalizacija_spekter=spekter[1]/sum(spekter[1])


plt.plot(spekter[0]/2/np.pi,normalizacija_spekter,'o-')
plt.ylabel('gostota moči')
plt.xlabel('frekvenca')
plt.grid()
plt.savefig('sin_2_frekvenci_osnovno')
plt.show()

print(len(signal))

def test_sort(seznam):
    for i in range(len(seznam)):

        for j in range(len(seznam)-i-1):
            if seznam[j]>seznam[j+1]:
                swap=seznam[j]
                seznam[j]=seznam[j+1]
                seznam[j+1]=swap
    return seznam



a=[6,3,2,8,9,-9,-5,0,-8]
print(test_sort(a))

def sortiraj(seznam):
    nov=[]
    indeks=0
    min=seznam[0][0]


    for i in range(len(seznam)):

        for j in range(len(seznam) - i -1):

            if seznam[j][0] > seznam[j + 1][0]:
                swap = seznam[j]
                seznam[j] = seznam[j + 1]
                seznam[j + 1] = swap
                # print(swap)
    return  seznam






from peakdetect import *




def prepoznava(podatki):

    stevilo=0
    peaks = peakdetect(normalizacija_spekter, lookahead=4)


    tocke=[]
    for i in peaks[0]:
        tocke.append(i)
    for i in peaks[1]:
        tocke.append(i)
    # print('-----')
    # print(peaks)
    seznam_vrhov=sortiraj(tocke)
    # print(seznam_vrhov)
    # print('-----')

    max=[]

    for indeks in range(len(seznam_vrhov)):
        # print(peaks[0][indeks][1])

        if seznam_vrhov[indeks][1]>0.01:
            # print(peaks[0][indeks][1])
            max.append([indeks,seznam_vrhov[indeks][1]])
            stevilo+=1
    # print(max)
    if stevilo==1:
        return False
    if stevilo==2:
        # print(max[0][0],max[1][0])
        if max[0][0]==max[1][0]+1:
            return False
        # print(seznam_vrhov[max[0][0]+1][1])
        # print(seznam_vrhov[max[0][0]][1])
        # print(seznam_vrhov[max[1][0]][1])
        # print(max[0][0])
        # print(max[1][0])
        if max[0][0]+2==max[1][0] and seznam_vrhov[max[0][0]+1][1]<(seznam_vrhov[max[0][0]][1]+seznam_vrhov[max[1][0]][1])/4:
            return True
        else:
            return False



    if stevilo>2:
        return False


locljivost=[]
poli=[]
st_tock=512

delta_tocke=2*np.pi/st_tock
print(1/delta_tocke)
x=np.arange(0,2*np.pi,delta_tocke)


osnovna=75



for st_polov in range(10,200):
    for delta in np.arange(3.7,15,0.025):
        signal = np.sin(osnovna * x) + np.sin((osnovna + delta) * x)
        a, b = alg.AR_est_YW(signal, st_polov)
        spekter = alg.autoregressive.AR_psd(a, b)
        normalizacija_spekter=spekter[1]/sum(spekter[1])
        if prepoznava(normalizacija_spekter)==True:
            print(delta,st_polov)
            poli.append(st_polov)
            locljivost.append((delta))
            break

# plt.plot(poli,locljivost)
# plt.xlabel('# polov')
# plt.ylabel(r'$ločljivost-\Delta \omega$')
# plt.grid()
# plt.savefig('locljivost_mem_stevilo_polov.png')
# plt.show()


plt.plot(poli,locljivost)
plt.xlabel('# polov')
plt.ylabel(r'$ločljivost-\Delta \omega$')
plt.grid()
plt.xscale('log')
plt.savefig('locljivost_mem_stevilo_polov_log.png')
plt.show()

