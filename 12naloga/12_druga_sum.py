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


for vrsta in data_file:
    x.append(float(vrsta))
    x_original.append(float(vrsta))
    i=i+1



f0=np.fft.fft(x)
f1=np.fft.fft(x1)
f2=np.fft.fft(x2)
f3=np.fft.fft(x3)

f00=abs(f0)**2
f11=abs(f1)**2
f22=abs(f2)**2
f33=abs(f3)**2

##fi:
mejna=50
vsota=0
for i in range(mejna,N):
    vsota+=f00[i]
povprecje=vsota/(N-mejna)

vsota=0
for i in range(mejna,N):
    vsota+=f11[i]
povprecje1=vsota/(N-mejna)

vsota=0
for i in range(mejna,N):
    vsota+=f22[i]
povprecje2=vsota/(N-mejna)

vsota=0
for i in range(mejna,N):
    vsota+=f33[i]
povprecje3=vsota/(N-mejna)


print(len(f0))
##prenosna funkcija:
fi=[]
fi1=[]
fi2=[]
fi3=[]
tau=16
r=[]


for i in range(N):
    fi.append(f00[i]/(f00[i]+povprecje))
    fi1.append(f11[i]/(f11[i]+povprecje1))
    fi2.append(f22[i]/(f22[i]+povprecje2))
    fi3.append(f33[i]/(f33[i]+povprecje3))
    r.append(np.exp(-i/tau)/(2*tau))
for i in range(N):
    r.append(2*i)
# print(fi)

R=np.fft.fft(r)
print(N)
print(len(R))


##inverzna fft:
# invert=np.fft.ifft(f/R)
invert1=np.fft.ifft(f1/R*fi1)
invert2=np.fft.ifft(f2/R*fi2)
invert3=np.fft.ifft(f3/R*fi3)
# print(invert2)
plt.plot(invert)
plt.plot(invert1)
plt.plot(invert2)
plt.plot(invert3)
plt.legend(['brez šuma','malo','malo več','izbris šuma'])
plt.savefig('12_2_izbris_suma.png')
# plt.legend(['sum_blocno_povprecje','original data'])
plt.show()


    


