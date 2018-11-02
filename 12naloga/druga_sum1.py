##brez šuma!!!!!!!!!!!!!
import matplotlib.pyplot as plt
import numpy as np

x=[]
x1=[]
x2=[]
x3=[]


f = open('signal0.dat', 'r',encoding='utf-8')
data_file=f.readlines()


for vrsta in data_file:
    x.append(float(vrsta))

f = open('signal1.dat', 'r',encoding='utf-8')
data_file=f.readlines()


for vrsta in data_file:
    x1.append(float(vrsta))


f = open('signal2.dat', 'r',encoding='utf-8')
data_file=f.readlines()


for vrsta in data_file:
    x2.append(float(vrsta))



f = open('signal3.dat', 'r',encoding='utf-8')
data_file=f.readlines()


for vrsta in data_file:
    x3.append(float(vrsta))


frekvencno=np.fft.fft(x)

print(len(frekvencno))
plt.plot(x)
# plt.plot(x1)
# plt.plot(x2)
# plt.plot(x3)
plt.grid()

plt.title('izhodni signal')
plt.xlabel('čas')
plt.savefig('druga_izhodni_signal.png')
plt.show()

plt.plot(frekvencno)
plt.show()

sum_1=[10 for i in range(len(frekvencno))]

tau=16
r=[]

for i in range(len(frekvencno)):
    r.append(np.exp(-i/tau)/(2*tau))
for i in range(int(len(frekvencno)/2)):
    r[-i]=r[i]
# print(fi)

R=np.fft.fft(r)

plt.plot(r)
plt.show()

invert=np.fft.ifft(frekvencno/R)



plt.plot(invert)
plt.grid()
plt.xlabel('čas')
plt.title('vhodni signal')

plt.savefig('druga_vhodni_signal.png')
plt.show()
    


