import random
import matplotlib.pyplot as plt
import numpy as np


def  sipanje_nevtronov_simple(n,lamda):
    debelina=1
    
    pot=-lamda*np.log(1-np.random.rand(n))
    
    M=0
    sipanje=0
    nesipan=0
    porazdelitev_sipanj=[]
    for i in range(n):
        stevilo_sipanj=0
        x=pot[i]
        if x>debelina:
            nesipan+=1
            porazdelitev_sipanj.append(0)
        while (x<debelina):
            sipanje+=1
            stevilo_sipanj+=1
            smer=np.random.rand()-0.5
            if smer<0:
                pot2=-lamda*np.log(1-np.random.rand())
                x-=pot2
                if x<0:
                    M+=1
                    porazdelitev_sipanj.append(stevilo_sipanj)
                    break
            if smer>0:
                pot2=-lamda*np.log(1-np.random.rand())
                x+=pot2
    
    print(sipanje,nesipan,nesipan+sipanje)
    print('odbojnost',M/n,'prepustnost',1-M/n)
    return M/n, porazdelitev_sipanj

# R,porazdelitev=sipanje_nevtronov_simple(100000,0.5)

# plt.title('sipanje naprej/nazaj\n'+'prosta pot: '+ str(0.5)+'   debelina plasti: 1')
# plt.hist(porazdelitev,bins=np.arange(0, 30 + 1, 1),normed=True)
# plt.xlabel('število sipanj')
# plt.ylabel('deleš sipanih nevtronov')
# plt.grid()
# plt.savefig('9_3_naprej.png')
# plt.show()

x=np.arange(0.1,5,0.2)
print(x)
y=[]
n=100000
for i in x:
    # print(y)
    a,b=sipanje_nevtronov_simple(n,i)
    y.append(a)

naprej=y
    
# print(y)
plt.plot(x,y,'-o')
plt.grid()
plt.title('sipanje naprej/nazaj\n'+'debelina: 1   stevilo nevtronov: 100000')
plt.ylabel('R-odbojnost')
plt.xlabel(r'$\lambda$-povprečna prosta pot')
plt.savefig('9_3_naprej_lamda.png')
# plt.xscale('log')
plt.show()