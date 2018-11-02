import matplotlib.pyplot as plt
import numpy as np

##funkcije

def f(HBr,H2,Br2,k,m):
    return k*H2*np.sqrt(Br2)/(m+(HBr/Br2))
    

 
##Runge-kutta-4
def rk4(H2_0,HBr_0,Br2_0,n,dt,k,m):
    
    prva=[0 for i in range(n)]
    druga=[0 for i in range(n)]
    tretja=[0 for i in range(n)]
    cas=[i*dt for i in range(n)]
    
    prva[0]=HBr_0
    druga[0]=H2_0
    tretja[0]=Br2_0
    

    for i in range(1,n):
        #print(i)
        t=cas[i-1]
        a=prva[i-1]
        b=druga[i-1]
        c=tretja[i-1]
        #print('z,l:\t',a,f,cas)
        
        k1=dt*f(a,b,c,k,m)
        #print('k1,l2',k1,l1)
        l1=-2*dt*f(a,b,c,k,m)
        m1=-2*dt*f(a,b,c,k,m)
        
        
        k2=dt*f(a+k1/2,b+l1/2,c+m1/2,k,m)
        l2=-2*dt*f(a+k1/2,b+l1/2,c+m1/2,k,m)
        m2=-2*dt*f(a+k1/2,b+l1/2,c+m1/2,k,m)
        
        
        k3=dt*f(a+k2/2,b+l2/2,c+m2/2,k,m)
        l3=-2*dt*f(a+k2/2,b+l2/2,c+m2/2,k,m)
        m3=-2*dt*f(a+k2/2,b+l2/2,c+m2/2,k,m)
        
        
        k4=dt*f(a+k3,b+l3,c+m3,k,m)
        l4=-2*dt*f(a+k3,b+l3,c+m3,k,m)
        m4=-2*dt*f(a+k3,b+l3,c+m3,k,m)
        
        
        K=(k1+2*k2+2*k3+k4)/6
        L=(l1+2*l2+2*l3+l4)/6
        M=(m1+2*m2+2*m3+m4)/6
        #print(K,L)
        
        prva[i]=a+K
        druga[i]=b+L
        tretja[i]=c+M
        #print(zajec[i],lisica[i])
        #print([zajec,lisica])
    return [prva,druga,tretja,cas]
    
D=0.8
R1=0.01
delez=R1*D/(1+R1)
HBr_zacetek=1-D
H2_zacetek=delez
Br2_zacetek=delez/R1

n=20000
dt=1/100
razmerje_konc=H2_zacetek/Br2_zacetek

print(razmerje_konc)
k_1=1


m=2.5

[koncA1,koncA_A,koncB,time]=rk4(H2_zacetek,HBr_zacetek,Br2_zacetek,n,dt,k_1,m)


R=1
delez=R*D/(1+R)
HBr_zacetek=1-D
H2_zacetek=delez
Br2_zacetek=delez/R
[koncA2,koncA_A,koncB,time]=rk4(H2_zacetek,HBr_zacetek,Br2_zacetek,n,dt,k_1,m)


R=100
delez=R*D/(1+R)
HBr_zacetek=1-D
H2_zacetek=delez
Br2_zacetek=delez/R
[koncA3,koncA_A,koncB,time]=rk4(H2_zacetek,HBr_zacetek,Br2_zacetek,n,dt,k_1,m)


naslov=r'k=1 m=2.5 D='+str(D)


plt.plot(time,koncA1,time,koncA2,time,koncA3)
plt.title(naslov)
plt.xlabel('čas')
plt.ylabel(r'$[HBr_2]$')
plt.legend([r'$\alpha=0.01$',r'$\alpha=1$',r'$\alpha=100$'])
plt.grid()

# plt.xlim(xmax=4)
naslov='druga_druga_D_'+str(D)+'.png'
naslov=naslov.replace('.','_')
plt.savefig(naslov)
plt.show()