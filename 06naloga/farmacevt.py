import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import numpy as np
from scipy import stats
from scipy import odr

x=[]
y=[]


f = open('farmakoloski.dat', 'r',encoding='utf-8')
data_file=f.readlines()

i=0
for vrsta in data_file:
    #print(i)
    if i>0:
        #print(type(vrsta))
        #print(vrsta)
        vrsta=vrsta.strip('\n')
        podatki=vrsta.split('\t')
        #print(podatki)
        x.append(float(podatki[0]))
        y.append(float(podatki[1]))
    i=i+1
print(x,y)


f.close()


x_os=1/np.array(x)
y_os=1/np.array(y)

n=len(x_os)


y_napaka=[3 for i in range(n)]

y_os_napake=3*(y_os**2)

A=np.vstack([x_os,np.ones(n)]).T
print(A)

print(np.linalg.lstsq(A,y_os)[0])
resitev=np.linalg.lstsq(A,y_os)[0]
k=resitev[0]
m=resitev[1]
x1=np.arange(0,1,0.1)
y1=k*x1+m



# a=9180
# b=-705
# y2=a*x1+b
# print(x1,y1)
#plt.yscale('log')
#plt.xscale('log')
# plt.plot(x_os,y_os,'o',)
# plt.errorbar(x_os,y_os,yerr=y_os_napake)
# plt.plot(x1,y1,x1,y2)
# plt.grid()
# plt.show()

x3=np.array(x)

y0=1/m
a=k*y0

print(k,m,a,y0)

y3=y0*x3/(x3+a)

print(a,y0)


hi=0
for i in range(n):
    delna=((y[i]-y3[i])/y_napaka[i])**2
    hi=hi+delna
print(hi)


print('hi kvadrat:',hi)
plt2.errorbar(x,y,yerr=y_napaka)
plt2.plot(x3,y3)
# plt2.xscale('log')
plt2.grid()
plt2.show()