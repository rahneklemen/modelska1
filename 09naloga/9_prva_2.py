import numpy as np
import random
import matplotlib.pyplot as plt
import time
from mpl_toolkits.mplot3d import Axes3D






n=5000
n_bins=100


r=np.random.rand(n)
t=np.random.rand(n)
p=np.random.rand(n)

fi=p*2*np.pi
theta=np.arccos(2*t-1)
radij=r**(1/6)



x=np.array([])
y=np.array([])
z=np.array([])
r=np.array([])
t=np.array([])
p=np.array([])
N=0
M=0
for i in range(n):
    a=radij[i]*np.cos(fi[i])*np.sin(theta[i])
    b=radij[i]*np.sin(fi[i])*np.sin(theta[i])
    c=radij[i]*np.cos(theta[i])
    M+=1
    if (a-0.5)**2+b**2>0.25:
    # print('sda')
        N+=1
        x=np.append(x,a)
        y=np.append(y,b)
        z=np.append(z,c)
        razdalja=np.sqrt(a**2+b**2+c**2)
        r=np.append(r,razdalja)
        t=np.append(t,np.arccos(c/razdalja))
        p=np.append(p,np.arctan(b/a))
        
    
print(len(x),len(r))
print(N/M*4*np.pi/3)


##3d narisan izrezana krogla
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x,y,z)
plt.title('število generiranih točk: '+str(n))
ax.set_xlabel('x os')
ax.set_ylabel('y os')
ax.set_zlabel('z os')
plt.savefig('9_prva_1.png')
plt.show()

# values_radij,indices_radij=np.histogram(r,bins=n_bins,range=(0,1),normed=True)
# values_fi,indices_fi=np.histogram(p,bins=n_bins,range=(0,2*np.pi),normed=True)
# values_theta,indices_theta=np.histogram(t,bins=n_bins,range=(0,np.pi),normed=True)
# 
# print(len(values_radij),len(indices_radij))
# plt.hist(r,normed=True,bins=n_bins)
# # plt.hist(radij,normed=True,bins=n_bins)
# plt.plot(indices_radij[:-1],values_radij)
# plt.plot(indices_theta[:-1],values_theta)
# plt.plot(indices_fi[:-1],values_fi)
# plt.grid()
# # plt.hist(radij,normed=True,bins=n_bins)
# plt.show()


# vol1=((indices_radij[:-1])).dot(values_radij)/n_bins
# vol2=((indices_fi[:-1])).dot(values_fi)/n_bins*2*np.pi
# vol3=((indices_theta[:-1])).dot(values_theta)/n_bins*np.pi
# 
# volumen=vol1*vol2*vol3
# 
# print(vol1,vol2,vol3,volumen)
# 
# vol1=(np.ones(len(values_radij))).dot(values_radij)/n_bins
# vol2=(np.ones(len(values_fi))).dot(values_fi)/n_bins*2*np.pi
# vol3=(np.ones(len(values_theta))).dot(values_theta)/n_bins*np.pi
# 
# volumen=vol1*vol2*vol3
# 
# print(vol1,vol2,vol3,volumen)

tez=sum(x)/len(x)
tocnost_tez=np.sqrt(abs(sum(x**2)/(n**2)-tez**2)/n)
tez_y=sum(y)/len(y)
tocnost_y=np.sqrt(abs(sum(y**2)/(n**2)-tez_y**2)/n)
tez_z=sum(z)/len(z)
tocnost_z=np.sqrt(abs(sum(z**2)/(n**2)-tez_z**2)/n)
print(tez,tez_y,tez_z)
print(tocnost_tez,tocnost_y,tocnost_z)





    