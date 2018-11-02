from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

x=[]


f = open('val3.dat', 'r',encoding='utf-8')
data_file=f.readlines()


for vrsta in data_file:
    # print(i)
    # print(type(vrsta))
    # print(vrsta)
    x.append(float(vrsta))


frekvencno=abs(np.fft.fft(x)**2)
frekvencno=frekvencno/np.amax(frekvencno)

f2=abs(np.fft.fft(x,128))**2
f2=f2/np.amax(f2)

f3=abs(np.fft.fft(x,32))**2
f3=f3/np.amax(f3)


time1=np.arange(32)*16
time2=np.arange(128)*4


plt.plot(frekvencno)
plt.plot(time2,f2)
plt.plot(time1,f3)
plt.grid()
plt.legend(['512','128','32'],loc=2)
plt.ylabel(r'$|\mathcal{F}|^2$')
plt.xlabel('frekvenca')
plt.xlim(xmax=256)
plt.title('val3.dat')
plt.savefig('prva_naloga_2.png')
plt.show()
