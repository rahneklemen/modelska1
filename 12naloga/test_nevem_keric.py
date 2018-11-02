import matplotlib.pyplot as plt
import numpy as np

def dekonvolucija(tabela):
    f=np.fft.fft(tabela)
    r=np.arange(len(tabela))
    tau=30

    for i in range(len(r)):
        r[i]=np.exp(-i/tau)/tau
    R=np.fft.fft(r)

    return np.fft.ifft(f/R)

def cela_vrsta(tabelica):
    dekonv=[]
    for i in tabelica:
        dekonv.append(dekonvolucija(i))
    return dekonv


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






plt.matshow(matrika1, cmap=plt.cm.gray)
plt.show()




