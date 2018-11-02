import numpy as np
import matplotlib.pylab as plt
from scipy import signal

def desumiraj(x):
    frekvencno=np.fft.fft(x)
    f2=abs(frekvencno)**2
    N=len(x)
    # print(len(f2))

    vsota=0
    mejna=30
    # print(len(x),len(f2))
    #

    M=int(N/2)
    for i in range(mejna,M):
        vsota+=f2[i]
    povprecje=vsota/(M-mejna)


    tau=30
    r=[]
    fi=[]
    for i in range(N):
        fi.append(f2[i]/(f2[i]+povprecje))
        r.append(np.exp(-(N-i)/tau)/tau)
    # for i in range(int(N/2)):
    #     r[-i]=r[i]

    R=np.fft.fft(r)

    # print(len(frekvencno))
    # print(len(R))

    return np.fft.ifft(frekvencno/R)


##branje datoteke
y=[]

f = open('N20.txt', 'r')
data_file=f.readlines()

for vrsta in data_file:
    lala=vrsta.strip(' \n')
    hah=lala.split(' ')
    y.append(hah)


vrsta=[]
for i in y:
    for j in i:
        vrsta.append(float(j))
matrika=np.array(vrsta).reshape(256,313)



# print(matrika)
# plt.matshow(matrika, cmap=plt.cm.gray)
# plt.show()



matrika2=matrika.T

plt.matshow(matrika,cmap=plt.cm.gray)
plt.colorbar()
plt.savefig('1.png')
plt.show()


prava=[]
for i in matrika2:
    prava_vrsta=(desumiraj(i))
    # b=np.amax(prava_vrsta)
    prava.append((prava_vrsta))


matrika2=1*np.real(prava)

# for i in range(len(matrika2)):
#     for j in range(len(matrika2[0])):
#         if prava[i][j]<0:
#             matrika2[i][j]=255



matrika=matrika2.T

print(matrika2[1],matrika2[20])
plt.matshow(-1*matrika, cmap=plt.cm.gray)
plt.title('moja funkcija')
plt.colorbar()
# plt.axes.get_a
plt.savefig('1_1.png')
plt.show()




