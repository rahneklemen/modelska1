from  scipy.signal import wiener
import numpy as np
import matplotlib.pylab as plt
from scipy.ndimage.filters import convolve
from scipy import signal

y=[]

f = open('N00.txt', 'r')
data_file=f.readlines()

for vrsta in data_file:
    lala=vrsta.strip(' \n')
    hah=lala.split(' ')
    y.append(hah)

vrsta=[]

for i in y:
    for j in i:
        vrsta.append(float(j))
print(vrsta)
print(len(vrsta))

matrika=np.array(vrsta).reshape(256,313)

print(matrika)
plt.matshow(matrika, cmap=plt.cm.gray)
plt.savefig('orginal.png')
plt.show()


tau=30
filter=[]
for i in range(313):
    filter.append(np.exp(-i/tau)/tau)
for i in range(int(313/2)):
    filter[-i]=filter[i]


matrika1=[]


prava=[]
for i in matrika:
    vrsta1=convolve(i,filter)
    matrika1.append(vrsta1)
    prava_vrsta=wiener(i)
    # b=np.amax(prava_vrsta)
    prava.append((prava_vrsta))



plt.matshow(prava, cmap=plt.cm.gray)
plt.show()

prava=wiener(matrika,noise=2)
plt.matshow(prava, cmap=plt.cm.gray)
plt.savefig('zadnja.png')
plt.show()

print(len(filter))
filter2=[]
for i in range(256):
    filter2.append(filter)
gauss_denoised = signal.fftconvolve(matrika, filter2)

plt.matshow(gauss_denoised, cmap=plt.cm.gray)
plt.show()