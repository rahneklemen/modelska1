import numpy as np
from datetime import datetime
import matplotlib.pylab as plt
from lcg import *

def random_n(n):
    return [random.random() for i in range(n)]

N=8

cas_lcg=[]
cas_vgr=[]

stevilo=[10**i for i in range(N)]




for i in range(N):
    a=10**i
    startTime = datetime.now()
    np.random.random(a)
    cas_vgr.append((datetime.now() - startTime).total_seconds())

for i in range(N):
    a=10**i
    startTime = datetime.now()
    lcg(a)
    cas_lcg.append((datetime.now() - startTime).total_seconds())

print(len(cas_vgr),len(cas_lcg),len(stevilo))

plt.plot(stevilo,cas_vgr,'o-',label='vgrajeni')
plt.plot(stevilo,cas_lcg,'o-',label='lcg')
plt.legend(loc=2)

plt.yscale('log')
plt.ylabel('čas [s]')

plt.xlim(xmin=10**2)
plt.xscale('log')
plt.xlabel('število stevk')
plt.grid()
plt.savefig('casovna_odvisnost.png')



plt.show()




