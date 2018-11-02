import random
import matplotlib.pyplot as plt
import numpy as np


def ena_nic():
    return random.choice([-1,1])



def magnetizacija(matrika):
    return sum(map(sum, matrika))/(len(matrika)**2)
    
def ising(n,temperatura,zunanje):
    spini=[[ena_nic() for j in range(n+2)] for i in range(n+2)]
    
    sprememba=0

    
    while(sprememba<1000):
        for i in range(1,n+1):
            for j in range(1,n+1):
                delta=-spini[i][j]*(spini[i-1][j]+spini[i+1][j]+spini[i][j+1]+spini[i][j-1]+zunanje)
                #print(delta)
                ksi=np.random.rand()
                # print(ksi)
                if ksi>np.exp(2*delta/temperatura):
                    # print('delam')
                    spini[i][i]*=-1
        sprememba+=1

    return spini
    


n=50
temperatura=0.5
H=0

mreza=ising(n,temperatura,H)


naslov='n'+str(temperatura)+'zunaje'+str(n)+'.png'



plt.matshow(mreza,  cmap=plt.cm.gray)
plt.savefig(naslov)
plt.colorbar()
plt.show()



