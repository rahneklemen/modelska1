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


x = []

f = open('borza.dat', 'r', encoding='utf-8')
data_file = f.readlines()

for vrsta in data_file:
    x.append(float(vrsta))

f.close()

#napoved:


polovica=int(len(x)/2)

print(polovica)
podatki=x[:polovica]
st_koef=20


a,b=alg.AR_est_YW(np.array(podatki),st_koef)


# y2=aproksimacija(x,a,ii)
y3=aproksimacija(podatki,a,polovica)


plt.plot(x,label='meritev')
plt.plot(y3,label='napoved N='+str(st_koef))
plt.legend(title='borza')
plt.grid()
plt.axvline(x=polovica-1,color='r')
plt.xlim(xmax=len(y3))

plt.savefig('napoved_borza'+str(st_koef)+'.png')
plt.show()


