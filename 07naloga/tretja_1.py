from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt2





f = open('korozija.txt', 'r',encoding='utf-8')
data_file=f.readlines()
x=[]
y=[]
i=0
for vrsta in data_file:
    # print(i)
    vrsta=vrsta.strip('\n')
    # print(vrsta)
    podatki=vrsta.split(' ')
    #print(podatki)
    x.append(float(podatki[0]))
    y.append(float(podatki[1]))
    i=i+1
print(x)
print(y)

# plt2.plot(x,y)
# plt.title('test')
# plt2.show()


def f(x, a,b,c):
    return a*(np.exp(x/b)-np.exp(-x/c))

def hi(x_data,y_data,f,a,b,c):
    vsota=0
    n=len(x_data)
    for i in range(n):
        vsota+=(y_data[i]-f(x_data[i],a,b,c))**2
    return vsota/(n-3-1)

def hi2(y_data,y_fit):
    n=len(y_data)
    vsota=0
    for i in range(n):
        vsota+=(y_data[i]-y_fit[i])**2
    return vsota/n
    
popt, pcov = curve_fit(f, x, y,p0=(0.001,30,20),maxfev=10000)
a=popt[0]
b=popt[1]
c=popt[2]

x1=np.arange(-100,100,0.1)
y1=f(x1,a,b,c)
print('hi kvadra',hi(x,y,f,a,b,c))
print('hi2 kvadra',hi2(y,y1))
print(popt,'\n a, b, c \n',np.sqrt(pcov))
plt.plot(x,y,'o')
plt.plot(x1,y1)
# plt.yscale('log')
plt.legend(['meritve',r'$I=I_0 [\exp{\frac{U}{U_a}}- \exp{-\frac{U}{U_b}}]$'],loc=2)
plt.grid()
plt.xlabel('napetost')
plt.ylabel('tok')


plt.savefig('tretja_1.png')
plt.show()

