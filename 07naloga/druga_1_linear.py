from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np





f = open('ledvice.dat', 'r',encoding='utf-8')
data_file=f.readlines()
x=[]
y=[]
y_napaka=[]
i=0
for vrsta in data_file:
    # print(i)
    if i>0:
        # print(type(vrsta))
        # print(vrsta)
        vrsta=vrsta.strip('\n')
        # print(vrsta)
        podatki=vrsta.split('\t')
        #print(podatki)
        x.append(float(podatki[0]))
        y.append(np.log(float(podatki[1])))
    i=i+1
print(x)
print(y)

def f(x, a,b):
    return a-b*x

def hi(x_data,y_data,f,a,b):
    vsota=0
    n=len(x_data)
    for i in range(n):
        vsota+=(y_data[i]-f(x_data[i],a,b))**2
    return vsota/n

def hi2(y_data,y_fit):
    n=len(y_data)
    vsota=0
    for i in range(n):
        vsota+=(y_data[i]-y_fit[i])**2
    return vsota/n
    
popt, pcov = curve_fit(f, x, y,p0=(0,0.1),maxfev=100)
a=popt[0]
b=popt[1]

x1=np.arange(0,2160,0.1)
y1=f(x1,a,b)
print('hi kvadra',hi(x,y,f,a,b))
print('hi2 kvadra',hi2(y,y1))
print(popt,'\n a, b, c \n',pcov)
plt.plot(x,y,'o')
plt.plot(x1,y1)
# plt.xscale('log')
plt.grid()
# plt.xlim(0,2160)
# plt.ylim(0,14000)
plt.xlabel('čas')
plt.ylabel('log[N (število sunkov)]')
plt.savefig('druga_1_linearno.png')
plt.show()

