#sevanje dipola

import numpy as np
import random
import matplotlib.pyplot as plt
import time

n=10000

def f(x):
    return (np.cos(x)**3-3*np.cos(x)+2)/4


def f2(x):
    return (x**3-x*3+2)/4



##-------
def bisekcija(a,b,x):
    e=10e-10
    c=(a+b)/2
    epsilon=(f(c)-x)
    # print(epsilon,'\t c:',c)
    if abs(epsilon)<e:
        print(c)
        return c
    elif epsilon<0:
        c=bisekcija(c,b,x)
        # print(epsilon,'\t c:',c)
    else:
        c=bisekcija(a,c,x)
    return c
    
    
def bisection(a,b,x):
    e=10e-10
    c=(a+b)/2
    epsilon=(f(c)-x)*-1
    # print(epsilon,'\t c:',c)
    while abs(epsilon)>e:
        epsilon=(f(c)-x)*-1
        # print(epsilon,'\t c:',c)
        if epsilon<0:
            b=c
        else:
            a=c
        c=(a+b)/2
    return c


# ##-------------------
# a=bisekcija(0,np.pi,0.6)
# print('c:\t',a)
# # print('bisekcija vrednost f():',f(a))
#
# a=bisection(0,np.pi,0.6)
# print('c:\t',a)
# print('vrednost f():',f(a))
# ##------konec preverajnaja bisekcije ce deluje
# random_stevilke = np.random.rand(n)
#
# plt.hist(random_stevilke,bins=100)
# plt.show()
#
# for i in range(n):
#     a=random_stevilke[i]
#
# x=np.arange(-np.pi,np.pi,0.01)
#
#
#
# y=f(x)
# y2=-(x**3-x*3-2)/4
# y3=(x**3-x*3+2)/4
#
# plt.plot(x,y,x,y2,x,y3)
#
# plt.grid()
# plt.legend(['theta','cosx','-coszheta'])
# plt.show()


# 
# y_b=[]
# for i in range(len(x)):
#     if x[i]>0 and x[i]<1:
#         resitev=bisection(0,np.pi,x[i])
#         # print(resitev)
#         y_b.append(resitev)
#
# n=10000
# dipol=[]
# for i in range(n):
#     dipol.append(bisection(0,np.pi,random.random()))
#
#
# x=np.arange(0,np.pi,0.01)
# y=np.sin(x)**3*3/4
# plt.hist(dipol,bins=100,normed=True)
# plt.plot(x,y,'r',linewidth=1.5)
# plt.grid()
# plt.title('število izsevanih fotonov='+str(n))
# plt.xlabel(r'$\theta$',fontsize=20)
# plt.ylabel(r'$\frac{dP_{dipol}}{d\theta}$',fontsize=20)
# plt.xlim(0,np.pi)
# plt.savefig('dipol_theta_'+str(n)+'.png')
# plt.show()





#
#
# values_theta,indices_theta=np.histogram(dipol,bins=100,range=(0,np.pi),normed=True)
#
# x=indices_theta[:-1]
# for i in range(len(x)):
#     x[i]=(indices_theta[i]+indices_theta[i+1])/2
#
#
# print(indices_theta[:-1].dot(values_theta)/100*np.pi,'theta...')
#
# print(np.cos(indices_theta[:-1]).dot(values_theta)/100*np.pi,'povp cos theta pride 0')
#
# print(indices_fi[:-1].dot(values_fi)/100*2*np.pi,'fi...')
#
# print(np.cos(indices_fi[:-1]).dot(values_fi)/100*2*np.pi,'povp cos fi, prisde 0')
#
# print(np.sin(indices_theta[:-1]).dot(values_theta)/100*np.pi,'povp sin theta?, 0.8???')
#
# print((0.25*np.sqrt(5/np.pi)*(3*np.cos(indices_theta[:-1])**2-1).dot(values_theta)/100*np.pi),'pricakovan Y20')
#
# print((np.cos(indices_theta[:-1])**2).dot(values_theta)/100*np.pi,'povp cos kvadrat theta prqavilno 0.2=1/5')
#
#
# print((np.cos(indices_fi[:-1])**2).dot(values_fi)/100*2*np.pi,'povp cos kvadrat fi? ok 0.5=1/2')

def variacija_momentov(n):
    
    dipol=[]
    for i in range(n):
        dipol.append(bisection(0,np.pi,random.random()))
    
    values_theta,indices_theta=np.histogram(dipol,bins=100,range=(0,np.pi),normed=True)
    
    x=indices_theta[:-1]
    for i in range(len(x)):
        x[i]=(indices_theta[i]+indices_theta[i+1])/2
    
    return (0.25*np.sqrt(5/np.pi)*(3*np.cos(indices_theta[:-1])**2-1).dot(values_theta)/100*np.pi)



potence=np.arange(1.5,6.5,0.5)
print(potence)

x=[]
y=[]
for i in potence:
    print(i)
    a=int(10**i)
    print('stevilo fotonov:',a)
    x.append(a)
    povpr=[]
    for k in range(5):
        povpr.append(abs(variacija_momentov(a)+0.12615662610100800241235747611828))
    y.append(sum(povpr)/len(povpr))
    # y.append(abs(variacija_momentov(a)+0.12615662610100800241235747611828))

plt.plot(x,y,'o-')
plt.grid()
plt.xlabel('stevilo naključnih smeri')
plt.title('razlika med analitično in simulacijo')
# plt.yticks([-0.11,-0.115,-0.12,-0.13,-0.126])
plt.ylabel(r'log|$<Y_{20}>-\frac{1}{2\sqrt{2 \pi}}$|')
plt.xscale('log')
plt.yscale('log')
plt.savefig('hitrost_variacije.png')
plt.show()







