import random
import matplotlib.pyplot as plt
import numpy as np

def nev_sipanje(n,lamda):
    debelina=1
    pot=-lamda*np.log(1-np.random.rand(n))
    st_sipanj=0
    sipani_nevtroni=0
    M=0
    porazdelitev_st_sipanj=[]
    for i in range(n):
        x=pot[i]
        stevilo_sipanj=0
        if x>debelina:
            sipani_nevtroni+=1
            porazdelitev_st_sipanj.append(0)
        while (x<debelina):
            st_sipanj+=1
            stevilo_sipanj+=1
            kot=(2*np.random.rand()-1)
            pot2=-lamda*np.log(1-np.random.rand())
            x+=pot2*kot
            if x<0:
                porazdelitev_st_sipanj.append(stevilo_sipanj)
                M+=1
                break
    print(st_sipanj/n,sipani_nevtroni/n)
    print('odbojnost',M/n,'prepustnost',1-M/n)
    return M/n, porazdelitev_st_sipanj
    
    

# R,porazdelitev=nev_sipanje(100000,0.5)

# plt.title('izotropni model\n'+'prosta pot: '+ str(0.5)+'   debelina plasti: 1')
# plt.hist(porazdelitev,bins=np.arange(0, 30 + 1, 1),align='mid',normed=True)
# plt.xlabel('število sipanj')
# plt.ylabel('deleš sipanih nevtronov')
# plt.grid()
# plt.savefig('9_3_izotropni.png')
# plt.show()

x=np.arange(0.1,5,0.2)
print(x)
y=[]
n=100000
for i in x:
    # print(y)
    a,b=nev_sipanje(n,i)
    y.append(a)
    
izo=y
# print(y)
plt.plot(x,y,'-o')
plt.grid()
plt.title('sipanje izotropno\n'+'debelina: 1   stevilo nevtronov: 100000')
plt.ylabel('R-odbojnost')
plt.xlabel(r'$\lambda$-povprečna prosta pot')
plt.savefig('9_3_izo_lamda.png')
# plt.xscale('log')
plt.show()