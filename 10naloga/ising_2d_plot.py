import random
import matplotlib.pyplot as plt
import numpy as np

def pbc(i,velikost):
    if i>=velikost:
        return 0
    if i<0:
        return velikost-1
    else:
        return i

def energija(mreza,zunanje):
    N=len(mreza)
    vsota=0
    for i in range(len(mreza)):
        for j in range(len(mreza)):
            vsota+=(-(mreza[i][pbc(j+1,N)]+mreza[i][pbc(j-1,N)]+mreza[pbc(i+1,N)][j]+mreza[pbc(i-1,N)][j])-zunanje)*mreza[i][j]
    return vsota/(len(mreza))**2


def energija_kvadrat(mreza,zunanje):
    vsota=0
    N=len(mreza)
    for i in range(N):
        for j in range(len(mreza)):
            vsota+=((-(mreza[i][pbc(j+1,N)]+mreza[i][pbc(j-1,N)]+mreza[pbc(i+1,N)][j]+mreza[pbc(i-1,N)][j])-zunanje)*mreza[i][j])**2
    return vsota/(len(mreza))**2


def kapaciteta(mreza,temperatura,zunanje):
    return (energija_kvadrat(mreza,zunanje)-energija(mreza,zunanje)**2)/(temperatura**2)


def magnetizacija_kvadrat(matrika):

    vsota = 0
    for vrsta in range(len(matrika)):
        for stolpec in range(len(matrika[0])):
            vsota += matrika[vrsta][stolpec]**2
    return vsota / ((len(matrika)) ** 2)


def susceptibilnost(mreza,temperatura):
    return (magnetizacija_kvadrat(mreza)-magnetizacija(mreza)**2)/temperatura




def ena_nic():
    return random.choice([-1,1])

def magnetizacija(matrika):
    vsota = 0
    for vrsta in range(len(matrika)):
        for stolpec in range(len(matrika[0])):
            vsota += matrika[vrsta][stolpec]
    return vsota / ((len(matrika)) ** 2)



def ising(N,temperatura,zunanje_polje):
    mreza=[ [ena_nic() for i in range(N)] for j in range(N)]
    mcs=0
    nakljucna=np.random.random(N**2*200)
    while (mcs<5):
        for i in range(N):

            for j in range(N):
                # print(j,i)
                # print(pbc(j,N),pbc(i,N))
                delta=(-1*(mreza[i][pbc(j+1,N)]+mreza[i][pbc(j-1,N)]+mreza[pbc(i+1,N)][j]+mreza[pbc(i-1,N)][j])-zunanje_polje)*mreza[i][j]
                #print(delta)
                if nakljucna[i+j+mcs]<np.exp(2*delta/temperatura):
                    mreza[i][j]*=-1
        mcs+=1
    return mreza





plt.matshow(ising(50,3,0),  cmap=plt.cm.gray)
plt.colorbar()
plt.show()