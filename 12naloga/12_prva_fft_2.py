import matplotlib.pyplot as plt
import numpy as np

x=[]


f = open('val3.dat', 'r',encoding='utf-8')
data_file=f.readlines()

i=0
for vrsta in data_file:
    # print(i)
    # print(type(vrsta))
    # print(vrsta)
    x.append(float(vrsta))
    i=i+1



frekvencno=abs(np.fft.fft(x)**2)
print(len(frekvencno))
N=len(frekvencno)
plt.plot(frekvencno)
plt.show()


##okno:

okno=np.hanning(N)
okno2=np.bartlett(N)
okno3=np.blackman(N)

frekvencno=frekvencno/np.amax(frekvencno)
frekvencno1=abs(np.fft.fft(x*okno)**2)
frekvencno1=frekvencno1/np.amax(frekvencno1)
frekvencno2=abs(np.fft.fft(x*okno2)**2)
frekvencno2=frekvencno2/np.amax(frekvencno2)
frekvencno3=abs(np.fft.fft(x*okno3)**2)
frekvencno3=frekvencno3/np.amax(frekvencno3)



plt.plot(okno)
plt.plot(okno2)
plt.plot(okno3)
plt.grid()
plt.title('okenske funkcije')
plt.legend(['Hanning','Bartlett','Blackman'])
plt.savefig('prva_naloga_okenske_funkcije.png')
plt.show()


plt.plot(frekvencno)
plt.plot(frekvencno1)
plt.plot(frekvencno2)
plt.plot(frekvencno3)

plt.legend(['brez','Hanning','Bartlett','Blackman'])
plt.yscale('log')
plt.grid()
plt.ylabel(r'$|\mathcal{F}|^2$')
plt.xlabel('frekvenca')

plt.savefig('prva_naloga_okenske.png')
plt.show()