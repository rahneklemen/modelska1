import numpy as np
import matplotlib.pyplot as plt

t=[]
m=[]
sus=[]
kapac=[]


ener=[]
energ_kvadrat=[]

s0=[]
s1=[]
s5=[]
s10=[]

c0=[]
c1=[]
c5=[]
c10=[]

m0=[]
m1=[]
m5=[]
m10=[]





f=open('podatki_magnetizacija.txt','r')
vrstice=f.readlines()
for vrsta in vrstice:
    podatki=(vrsta.strip('\r\n')).split('\t')
    # print(vrsta)
    if podatki!=['']:
        print(podatki)

        t.append(float(podatki[0]))
        m0.append(float(podatki[1]))
        m1.append(float(podatki[2]))
        m5.append(float(podatki[3]))
        m10.append(float(podatki[4]))

f.close()



f=open('podatki_specificna.txt','r')
vrstice=f.readlines()
for vrsta in vrstice:
    podatki=(vrsta.strip('\r\n')).split('\t')
    # print(vrsta)
    if podatki!=['']:
        print(podatki)


        c0.append(float(podatki[1]))
        c1.append(float(podatki[2]))
        c5.append(float(podatki[3]))
        c10.append(float(podatki[4]))

f.close()


f=open('podatki_susceptibilnost.txt','r')
vrstice=f.readlines()
for vrsta in vrstice:
    podatki=(vrsta.strip('\r\n')).split('\t')
    # print(vrsta)
    if podatki!=['']:
        print(podatki)

        s0.append(float(podatki[1]))
        s1.append(float(podatki[2]))
        s5.append(float(podatki[3]))
        s10.append(float(podatki[4]))

f.close()






plt.plot(t,s0,'o',label='H=0')
plt.plot(t,s1,'+',label='H=0.1')
plt.plot(t,s5,'D',label='H=0.5')
plt.plot(t,s10,'*',label='H=1')

plt.legend()
plt.axvline(x=2.269,color='r')
plt.ylabel('susceptibilnost')
plt.xlabel('temperatura')
plt.grid()
plt.savefig('susceptibilnost_tudi_zunanje.png')
plt.show()


plt.plot(t,m0,'o',label='H=0')
plt.plot(t,m1,'+',label='H=0.1')
plt.plot(t,m5,'D',label='H=0.5')
plt.plot(t,m10,'*',label='H=1')

plt.legend()
plt.axvline(x=2.269,color='r')
plt.ylabel('magnetizacija')
plt.xlabel('temperatura')
plt.grid()
plt.savefig('magneizacija_tudi_zunanje2.png')
plt.show()


plt.plot(t,c0,'o',label='H=0')
plt.plot(t,c1,'+',label='H=0.1')
plt.plot(t,c5,'D',label='H=0.5')
plt.plot(t,c10,'*',label='H=1')

plt.legend()
plt.axvline(x=2.269,color='r')
plt.ylabel('specifična toplota')
plt.xlabel('temperatura')
plt.grid()
plt.savefig('specificna_tudi_zunanje.png')
plt.show()

