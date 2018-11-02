

import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np






##xy ravnina oz. kot fi
# R=10
# fi=np.pi/9*7/5*2.214
# theta=np.pi*13/7/3*11/20
# print(theta)
#
#
#
# Tx=R*np.cos(fi)
# Ty=R*np.sin(fi)
#
#
# print(Tx,Ty)
#
#
# fi0=np.random.uniform(np.pi/2+fi,3/2*np.pi*+fi)
#
# print(fi,fi0)
#
# r1=1
# r2=3
#
# #T0-tocka sredisce velike kocke; cos(fi0) in sin(fi0) sta "smerna" vektorja sredisce do tocke trka na krogli
# Tx0=Tx-(r1+r2)*np.cos(fi0)
# Ty0=Ty-(r1+r2)*np.sin(fi0)
#
# #velikost projekcije vpadnega vektorja na smerni vektor
# velikost_proj=Tx*np.cos(fi0)+Ty*np.sin(fi0)
#
# #vektor projekcije na smer sredisca krogel
# prx=velikost_proj*np.cos(fi0)
# pry=velikost_proj*np.sin(fi0)
#
# #smer novega vektorja
# Tx2=Tx-2*prx
# Ty2=Ty-2*pry
#
# #konca tocka novega vektorja (zacetna je Tx,ty):
# Tx3=Tx+Tx2
# Ty3=Ty+Ty2
#
#
#
# R=1
# print('projekcija',velikost_proj)
#
# circle1=plt.Circle((Tx,Ty),r1,color='b')
# circle2=plt.Circle((Tx0,Ty0),r2,color='b')
# plt.gcf().gca().add_artist(circle1)
# plt.gcf().gca().add_artist(circle2)
#
# plt.plot([0,Tx],[0,Ty],'r')
# plt.plot([Tx,Tx0],[Ty,Ty0],'r')
# plt.plot([Tx,Tx3],[Ty,Ty3],'g')
# # plt.xlim([0,15])
# # plt.ylim([5,20])
#
# plt.grid()
# plt.show()



##ravnina xz kot theta:
#
# R=10
# theta=np.pi*13/7/3*11/20
#
# Tx=R*np.sin(theta)
# Tz=R*np.cos(theta)
#
# print(Tx,Tz)
# print(theta)
# print('mejna kota',np.pi/2+theta,3/2*np.pi+theta)
# theta0=np.random.uniform(np.pi/2+theta,3/2*np.pi+theta)
#
# print(theta,theta0)
#
# r1=1
# r2=3
#
# #T0-tocka sredisce velike kocke; cos(fi0) in sin(fi0) sta "smerna" vektorja sredisce do tocke trka na krogli
# Tx0=Tx-(r1+r2)*np.sin(theta0)
# Tz0=Tz-(r1+r2)*np.cos(theta0)
#
# print('x:',np.cos(theta0),'\ty:',np.sin(theta0))
#
# #velikost projekcije vpadnega vektorja na smerni vektor:skalarni produkt vektroja in normirana smer.
# velikost_proj=-(Tx*np.sin(theta0)+Tz*np.cos(theta0))
# print(velikost_proj)
# #vektor projekcije na smer sredisca krogel
# prx=velikost_proj*np.sin(theta0)
# prz=velikost_proj*np.cos(theta0)
#
# #smer novega vektorja
# Tx2=Tx+2*prx
# Tz2=Tz+2*prz
#
# # #konca tocka novega vektorja (zacetna je Tx,ty):
# Tx3=Tx+Tx2
# Tz3=Tz+Tz2
# #
# #
# #
# # R=1
# # print('projekcija',velikost_proj)
#
# circle1=plt.Circle((Tx,Tz),r1,color='b')
# circle2=plt.Circle((Tx0,Tz0),r2,color='b')
# plt.gcf().gca().add_artist(circle1)
# plt.gcf().gca().add_artist(circle2)
#
# plt.plot([0,Tx],[0,Tz],'r')
# plt.plot([Tx,Tx0],[Tz,Tz0],'r')
# # plt.plot([0,prx],[0,prz],'m')
# plt.plot([Tx,Tx3],[Tz,Tz3],'g')
#
# plt.grid()
# plt.show()

###3dimenzije

x=[0]
y=[0]
z=[0]

R=10
r1=1
r2=5


alfa=np.random.rand()*np.pi*2
radij=np.random.rand()**(0.5)

fi1=np.arctan((radij*np.sin(alfa))/np.sqrt(1-radij**2))
theta1=np.arccos(radij*np.cos(alfa))

theta=np.random.uniform(0,np.pi)
fi=np.arccos(2*np.random.rand()-1)



fi0=(fi+np.pi+fi1)

theta0=(theta+theta1+np.pi/2)%(2*np.pi)
print('theta0_do max 2pi:\t',theta0)
if theta0>np.pi:
    theta0=2*np.pi-theta0



print('min/max',theta0-np.pi/2,theta0+np.pi/2)

print('theta0:\t',theta0,'theta\t',theta,'theta1\t',theta1)



print('min/max fi',fi-np.pi,fi+np.pi)
print('fi0',fi0,'fi',fi,'fi1',fi1)



Tx=R*np.cos(fi)*np.sin(theta)
Ty=R*np.sin(fi)*np.sin(theta)
Tz=R*np.cos(theta)

x.append(Tx)
y.append(Ty)
z.append(Tz)


# Tx0=Tx-(r1+r2)*np.cos(fi0)
# Ty0=Ty-(r1+r2)*np.sin(fi0)

# theta0=0
##sredisce krogle:
Tx1=Tx-(r1+r2)*np.cos(fi0)*np.sin(theta0)
Ty1=Ty-(r1+r2)*np.sin(fi0)*np.sin(theta0)
Tz1=Tz-(r1+r2)*np.cos(theta0)

# x.append(Tx1)
# y.append(Ty1)
# z.append(Tz1)

##normiran smer od sredisca dveh krogel:

normx=np.cos(fi0)*np.sin(theta0)
normy=np.sin(fi0)*np.sin(theta0)
normz=np.cos(theta0)




##projekcija vpadnega delca na normiran vektor

proj=(Tx*normx+Ty*normy+Tz*normz)*-1

print(proj)
print(Tx,Ty,Tz)
print(normx,normy,normz)

x.append(2*Tx+2*proj*normx)
y.append(2*Ty+2*proj*normy)
z.append(2*Tz+2*proj*normz)



fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
X,Y,Z=x,y,z
ax.plot_wireframe(X,Y,Z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.quiver((x[-1]),(y[-1]),(z[-1]),(Tx+2*proj*normx),(Ty+2*proj*normy),(Tz+2*proj*normz),length=10)
ax.scatter(Tx1,Ty1,Tz1, s=np.pi*(r2*15)**2, c='green', alpha=0.75)
ax.scatter(Tx,Ty,Tz, s=np.pi*(r1*10)**2, c='blue', alpha=0.75)
ax.scatter(0,0,0, s=50, c='green', alpha=0.75)
plt.show()





##izracun povprecne proste poti nevtrona
# gostota=10**6
# NA=6*10**23
# A=12
# r0=1.25*10**(-15)
#
#
#
# pot=1/(np.sqrt(2)*gostota/A*NA*A**(2/3) * np.pi*r0**2)
# print('pot',pot)
# print('presek',A**(2/3) * np.pi*r0**2/10**(-28))

##porazdelitev tock na sferi
# n=1000
# alfa=np.random.rand(n)*np.pi*2
# radij=np.random.rand(n)**(0.5)
# fi=np.arctan((radij*np.sin(alfa))/np.sqrt(1-radij**2))
# theta=np.arccos(radij*np.cos(alfa))
# x1=radij*np.cos(alfa)
# y1=radij*np.sin(alfa)
# z1=np.zeros(n)

#
#
# x=np.cos(fi)*np.sin(theta)
# y=np.sin(fi)*np.sin(theta)
# z=np.cos(theta)
#
#
#
# fig=plt.figure()
# ax=fig.add_subplot(111,projection='3d')
#
#
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
#
# ax.set_xlim([-1,1])
# ax.set_ylim([-1,1])
# ax.set_zlim([-1,1])
#
# ax.scatter(x,y,z,s=1)
#
# plt.savefig('porazdelitev_tock_trka_na_jedru.png')
# plt.show()
#
# fig=plt.figure()
# ax=fig.add_subplot(111,projection='3d')
#
#
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
#
# ax.set_xlim([-1,1])
# ax.set_ylim([-1,1])
# ax.set_zlim([-1,1])
#
# ax.scatter(x,y,z,s=1)
#
# plt.show()















