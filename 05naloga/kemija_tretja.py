import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
##funkcije

def f(x,y,z,w,lam):
    return -2*x*w+2*lam*y*z
    
    
def g(x,y,z,w,lam):
    return x*w-lam*y*z


def h(x,y,z,w,lam):
    return -2*lam*y*z

def e(x,y,z,w,lam):
    return -x*w

 
##Runge-kutta-4
def rk4(prva0,druga0,tretja0,cetrta0,n,dt,lam):
    
    prva=[0 for i in range(n)]
    druga=[0 for i in range(n)]
    tretja=[0 for i in range(n)]
    cetrta=[0 for i in range(n)]
    
    cas=[i*dt for i in range(n)]
    
    prva[0]=prva0
    druga[0]=druga0
    tretja[0]=tretja0
    cetrta[0]=cetrta0
    
    for i in range(1,n):
        #print(i)
        t=cas[i-1]
        a=prva[i-1]
        b=druga[i-1]
        c=tretja[i-1]
        d=cetrta[i-1]
        #print('z,l:\t',a,f,cas)
        
        k1=dt*f(a,b,c,d,lam)
        l1=dt*g(a,b,c,d,lam)
        m1=dt*h(a,b,c,d,lam)
        n1=dt*e(a,b,c,d,lam)
        #print('k1,l2',k1,l1)
        
        k2=dt*f(a+k1/2,b+l1/2,c+m1/2,d+n1/2,lam)
        l2=dt*g(a+k1/2,b+l1/2,c+m1/2,d+n1/2,lam)
        m2=dt*h(a+k1/2,b+l1/2,c+m1/2,d+n1/2,lam)
        n2=dt*e(a+k1/2,b+l1/2,c+m1/2,d+n1/2,lam)
        
        k3=dt*f(a+k2/2,b+l2/2,c+m2/2,d+n2/2,lam)
        l3=dt*g(a+k2/2,b+l2/2,c+m2/2,d+n2/2,lam)
        m3=dt*h(a+k2/2,b+l2/2,c+m2/2,d+n2/2,lam)
        n3=dt*e(a+k2/2,b+l2/2,c+m2/2,d+n2/2,lam)
        
        k4=dt*f(a+k3,b+l3,c+m3,d+n3,lam)
        l4=dt*g(a+k3,b+l3,c+m3,d+n3,lam)
        m4=dt*h(a+k3,b+l3,c+m3,d+n3,lam)
        n4=dt*e(a+k3,b+l3,c+m3,d+n3,lam)
        
        K=(k1+2*k2+2*k3+k4)/6
        L=(l1+2*l2+2*l3+l4)/6
        M=(m1+2*m2+2*m3+m4)/6
        N=(n1+n2*2+n3*2+n4)/6
        #print(K,L)
        
        prva[i]=a+K
        druga[i]=b+L
        tretja[i]=c+M
        cetrta[i]=d+N
        #print(zajec[i],lisica[i])
        #print([zajec,lisica])
    return [prva,druga,tretja,cetrta,cas]
    

def cas(vrednosti,casovna):
    zacetna_vrednost=vrednosti[0]
    meja=zacetna_vrednost/2
    for i in range(len(vrednosti)):
        if vrednosti[i]<meja:
            print(i)
            return casovna[i]


def skala():
    mejni_cas=[0 for i in range(100)]
    delez=[i/100 for i in range(100)]
    for i in range(100):
        [koncA1,koncA2,koncA3,koncA4,time]=rk4(pogoj1,pogoj2,pogoj3,pogoj4,n,dt,i/100)
        mejni_cas[i]=cas(koncA3,time)
    return [mejni_cas,delez]


lamda=1

pogoj1=1
pogoj2=0
pogoj3=0.8
pogoj4=1

n=100000
dt=1/10000






[koncA1,koncA2,koncA3,koncA4,time]=rk4(pogoj1,pogoj2,pogoj3,pogoj4,n,dt,lamda)
naslov=r'$x_0=$'+str(pogoj1)+r' $y_0=$'+str(pogoj2)+r' $z_0=$'+str(pogoj3)+r' $w_0=$'+str(pogoj4)
print(naslov)
plt.title(naslov)
plt.plot(time,koncA1,time,koncA2,time,koncA3,time,koncA4)
plt.ylim([0,1.05])
podnaslov=r'$\lamda=$'+str(lamda)
plt.legend(['x','y','z','w'],title=podnaslov)
plt.grid()

naslov=naslov.replace('$','_')
naslov=naslov.replace('.','_')
naslov=naslov.replace('=','_')
naslov=naslov.replace('$','_')
naslov=naslov.strip('_')
print(naslov)
naslov=naslov+'.png'
plt.savefig(naslov)
plt.show()