from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

x=[]
y=[]


f = open('farmakoloski.dat', 'r',encoding='utf-8')
data_file=f.readlines()

i=0
for vrsta in data_file:
    print(i)
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

n=len(x)
y_napaka=[3 for i in range(n)]

def f(x, a, y0,p):
    return y0*(x**p)/(x**p+a**p)
    
def hi(x_data,y_data,y_error,a,y0,p):
    vsota=0
    for i in range(len(x_data)):
        vsota+=((f(x_data[i],a,y0,p)-y_data[i])/y_error[i])**2
    return vsota
    
popt, pcov = curve_fit(f, x, y,sigma=y_napaka)
a=popt[0]
y0=popt[1]
p=popt[2]
x1=np.arange(0,1000,0.1)
y1=f(x1,a,y0,p)

print('hi',hi(x,y,y_napaka,a,y0,p))
print(popt,'\n a, y0, p \n',pcov)
ax2  = plt.subplot(1,1,1)
plt.text(0.500, 1.05, r'nelinearno prilagajanje: $y=\frac{y_0 x^p}{a^p+x^p}$',
         horizontalalignment='center',
         fontsize=20,
         transform = ax2.transAxes)
# plt.title(r'nelinearno prilagajanje: $y=\frac{y0 x^p}{a^p+x^p}$',transform = ax2.transAxes)
plt.errorbar(x,y,yerr=y_napaka)
plt.plot(x1,y1,'r')
plt.legend(['meritve','prilagajanje'],loc=7)
plt.xscale('log')
plt.xlabel('doza')
plt.ylabel('odziv')
plt.grid()
plt.savefig('dodatno_parameter.png')
plt.show()