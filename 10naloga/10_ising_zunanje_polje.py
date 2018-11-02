import random
import matplotlib.pyplot as plt
import numpy as np

def ena_nic():
    return random.choice([-1,1])



def delta_energija(matrika,xpos,ypos,H):
    a=matrika[ypos][xpos]
    b=matrika[ypos][xpos+1]+matrika[ypos][xpos-1]+matrika[ypos+1][xpos]+matrika[ypos-1][xpos]
    # print((b*a)*ising)
    return 2*((b*a)*(-1)-H*a)*(-1)





def ising(n,temperatura,zunanje):
    spini=[[ena_nic() for j in range(n+2)] for i in range(n+2)]
    # spini=[[1 for j in range(n+2)] for i in range(n+2)]

    

    sprememba=0

    
    while(sprememba<10):
        for x in range(1,n+1):

            for y in range(1,n+1):

                delta=(spini[x+1][y]+spini[x-1][y]+spini[x][y+1]+spini[x][y-1]+zunanje)*spini[x][y]

                if delta<0:
                    # print(spini[y][x])
                    spini[x][y]*=-1
                elif np.random.rand()<np.exp(-2*delta/temperatura):
                    # print(delta, 'sredinski: ', spini[x][y], 'okolica: ', spini[x + 1][y], spini[x - 1][y],spini[x][y + 1], spini[x][y - 1], 'exp ', np.exp(-2 * delta / temperatura))
                    spini[x][y] *= -1


        sprememba+=1
    # print(meja)
    return spini
    


n=50
temperatura=5
zunanje_polje=1

mreza=ising(n,temperatura,zunanje_polje)
# kapa=kapaciteta(mreza,J,temperatura)



naslov='zunanje'+str(zunanje_polje)+'T'+str(temperatura)+'plus.png'



plt.matshow(mreza,  cmap=plt.cm.gray)
plt.xlim(1,n-1)
plt.ylim(1,n-1)
plt.xlabel('T='+str(temperatura)+'\nH='+str(zunanje_polje))

plt.savefig(naslov)
plt.show()





