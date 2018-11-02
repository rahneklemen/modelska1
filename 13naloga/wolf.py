import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from nitime import algorithms as alg


def aproksimacija(podatki,seznam_koeficientov,iteracij):
    for i in range(iteracij):
        vsota=0
        for j in range(len(seznam_koeficientov)):
            vsota+=podatki[-j-1]*seznam_koeficientov[j]
        podatki.append(vsota)
    return podatki



x=[]

f = open('Wolf_number.dat', 'r',encoding='utf-8')
data_file=f.readlines()

j=0
for vrsta in data_file:
    podatki=vrsta.split(' ')
    for i in range(len(podatki)):
        x.append(float(podatki[-1]))



#napoved:


polovica=int(len(x)/2)
print(polovica)
podatki=x[:polovica]
st_koef=2000


a,b=alg.AR_est_YW(np.array(podatki),st_koef)


# y2=aproksimacija(x,a,ii)
y3=aproksimacija(podatki,a,polovica)


plt.plot(x,label='meritev')
plt.plot(y3,label='napoved N='+str(st_koef))
plt.legend(title='Wolfova številka')
plt.grid()
plt.axvline(x=polovica,color='r')
plt.xlim(xmax=len(y3))
plt.savefig('napoved_wolf'+str(st_koef)+'.png')
plt.show()
