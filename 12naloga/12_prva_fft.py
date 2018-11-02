from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

x=[]


f = open('val2.dat', 'r',encoding='utf-8')
data_file=f.readlines()


for vrsta in data_file:
    # print(i)
    # print(type(vrsta))
    # print(vrsta)
    x.append(float(vrsta))


frekvencno=abs(np.fft.fft(x)**2)

f = open('val3.dat', 'r',encoding='utf-8')
data_file=f.readlines()


for vrsta in data_file:
    # print(i)
    # print(type(vrsta))
    # print(vrsta)
    x.append(float(vrsta))


f2=abs(np.fft.fft(x))**2
f2=f2/np.amax(f2)
frekvencno=frekvencno/np.amax(frekvencno)
plt.plot(frekvencno)
plt.plot(f2)
plt.grid()
plt.legend(['val2.dat','val3.dat'],loc=2)
plt.ylabel(r'$|\mathcal{F}|^2$')
plt.xlabel('frekvenca')
plt.xlim(xmax=256)
plt.title('normiran frekvenčni spekter')
plt.savefig('prva_naloga_1.png')
plt.show()
