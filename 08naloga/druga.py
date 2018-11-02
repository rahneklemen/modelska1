import numpy as np
import random
import matplotlib.pyplot as plt
import time


# def data2hist_fi(stevilke,razdelckov):
#     deljenec=np.pi*2/razdelckov
#     dolzina=len(stevilke)
#     histogram_data=[0 for i in range(razdelckov)]
#     vrednost=[(i)*deljenec for i in range(razdelckov)]
#     
#     for i in range(dolzina):
#         stevilka=stevilke[i]
#         indeks=int(stevilka//deljenec)
#         histogram_data[indeks]+=1
#         # print(indeks)
#     return [histogram_data,vrednost]
# 
# 
# def data2hist_theta(stevilke,razdelckov):
#     deljenec=np.pi/razdelckov
#     dolzina=len(stevilke)
#     histogram_data=[0 for i in range(razdelckov)]
#     vrednost=[(i)*deljenec for i in range(razdelckov)]
#     
#     for i in range(dolzina):
#         stevilka=stevilke[i]
#         indeks=int(stevilka//deljenec)
#         histogram_data[indeks]+=1
#         # print(indeks)
#     return [histogram_data,vrednost]





n=100000
fi=[]
theta=[]

zacetni_cas=time.time()

for i in range(n):
    r=np.random.rand()
    p=np.random.rand()
    
    fi.append(r*2*np.pi)
    theta.append(np.arccos(2*p-1))



values_fi,indices_fi=np.histogram(fi,bins=100,range=(0,2*np.pi),normed=True)



x=indices_fi[:-1]
for i in range(len(x)):
    x[i]=(indices_fi[i]+indices_fi[i+1])/2



# plt.hist(fi,bins=100,normed=True)
# plt.grid()
# plt.plot(indices_fi[:-1],values_fi,'o')
# plt.plot(x,values_fi)
# plt.show()


values_theta,indices_theta=np.histogram(theta,bins=100,range=(0,np.pi),normed=True)




x_os=np.arange(0,np.pi,0.01)
y_os=np.sin(x_os)/2

plt.title(r'porazdelitev po kotu $\theta$'+'\t n='+str(n))
plt.hist(theta,normed=True,bins=100)
plt.xlabel(r'$\theta$',fontsize=20)
plt.ylabel(r'$\frac{dP}{d \theta}$',fontsize=20)
plt.grid()
plt.xlim(0,np.pi)
plt.plot(x_os,y_os,'r')
plt.legend(['analitično','generator'])

plt.savefig('porazdelitev_theta'+'n_'+str(n)+'.png')
plt.show()


x=indices_theta[:-1]
for i in range(len(x)):
    x[i]=(indices_theta[i]+indices_theta[i+1])/2

# print(indices_fi[0])
# print(indices_theta[0])

##povprecje fi in theta

print(indices_theta[:-1].dot(values_theta)/100*np.pi,'theta...')

print(np.cos(indices_theta[:-1]).dot(values_theta)/100*np.pi,'povp cos theta?')

print(indices_fi[:-1].dot(values_fi)/100*2*np.pi,'fi...')

print(np.cos(indices_fi[:-1]).dot(values_fi)/100*2*np.pi,'povp cos fi?')
print(np.sin(indices_fi[:-1]).dot(values_fi)/100*2*np.pi,'povp sin fi?')

print(np.sin(indices_theta[:-1]).dot(values_theta)/100*np.pi,'povp sin theta?, prava je pi/4')

print((3*np.cos(indices_theta[:-1])**2-1).dot(values_theta)/100*np.pi,'pricakovan Y20')

print((np.cos(indices_theta[:-1])**2).dot(values_theta)/100*np.pi,'povp cos kvadrat theta?')


print((np.cos(indices_fi[:-1])**2).dot(values_fi)/100*2*np.pi,'povp cos kvadrat fi?')



# cos_theta=np.cos(values_theta)
# plt.plot(values_theta)
# plt.show()
# 
# 
# plt.hist(fi,bins=100)
# plt.show()
    