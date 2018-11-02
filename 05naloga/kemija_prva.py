import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import numpy as np
##funkcije

def f(A,A_A,B,r1,r2):
    #print(-p*A**2+q*A*A_A)
    return -A*(A-r1*A_A)
    
    
def g(A,A_A,B,r1,r2):
    return A*(A-r1*A_A)-r1*r2*A_A


def h(A,A_A,B,r1,r2):
    return r1*r2*A_A
    
def aa_a(aa,r1,r2):
    return -(r2*aa*aa)/(r2+aa)
    
def A_a(aa,r1,r2):
    return aa*aa/(r1*(aa+r2))

    
def rk_apr(prva0,druga0,n,dt,r1,r2):
    print(n)
    aaa=[0 for i in range(n)]
    aaa_a=[0 for i in range(n)]
    cas_a=[i*dt for i in range(n)]
    
    aaa[0]=prva0
    aaa_a[0]=A_a(prva0,r1,r2)
    
    for i in range(1,n):
        t=cas_a
        a=aaa[i-1]
        
        k1a=dt*aa_a(a,r1,r2)
        
        k2a=dt*aa_a(a+k1a/2,r1,r2)
        
        k3a=dt*aa_a(a+k2a/2,r1,r2)
        
        k4a=dt*aa_a(a+k3a,r1,r2)
        
        ka=(k1a+2*k2a+2*k3a+k4a)/6
        
        aaa[i]=a+ka
        aaa_a[i]=A_a(a+ka,r1,r2)
        
    return [aaa,aaa_a,cas_a]
 
##Runge-kutta-4
def rk4(prva0,druga0,tretja0,n,dt,r1,r2):
    print(n)
    prva=[0 for i in range(n)]
    druga=[0 for i in range(n)]
    tretja=[0 for i in range(n)]
    
    cas=[i*dt for i in range(n)]
    
    prva[0]=prva0
    druga[0]=druga0
    tretja[0]=tretja0

    for i in range(1,n):
        #print(i)
        t=cas[i-1]
        
        a=prva[i-1]
        b=druga[i-1]
        c=tretja[i-1]
        #print('z,l:\t',a,f,cas)
        
        k1=dt*f(a,b,c,r1,r2)
        l1=dt*g(a,b,c,r1,r2)
        m1=dt*h(a,b,c,r1,r2)
        #print('k1,l2',k1,l1)
        
        k2=dt*f(a+k1/2,b+l1/2,c+m1/2,r1,r2)
        l2=dt*g(a+k1/2,b+l1/2,c+m1/2,r1,r2)
        m2=dt*h(a+k1/2,b+l1/2,c+m1/2,r1,r2)
        
        k3=dt*f(a+k2/2,b+l2/2,c+m2/2,r1,r2)
        l3=dt*g(a+k2/2,b+l2/2,c+m2/2,r1,r2)
        m3=dt*h(a+k2/2,b+l2/2,c+m2/2,r1,r2)
        
        k4=dt*f(a+k3,b+l3,c+m3,r1,r2)
        l4=dt*g(a+k3,b+l3,c+m3,r1,r2)
        m4=dt*h(a+k3,b+l3,c+m3,r1,r2)
        
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
    

def razlika(prvi_seznam,drugi_seznam):
    diferenca=[0 for i in range(len(prvi_seznam))]
    for i in range(len(prvi_seznam)):
        diferenca[i]=abs(prvi_seznam[i]-drugi_seznam[i])
    return diferenca
        
        
A_zacetek=1
A_A_zacetek=0
B_zacetek=0

n=500000
dt=1/10000

# p=1
# q=100
# r=1

razmerje1=1000
razmerje2=0.1



##razlika med stacionarno aproksimacijo in analitično rešitvijo

razmerje2_1=10
razmerje2_2=1
razmerje2_3=0.1

[koncA_1,koncA_A_1,koncB,time]=rk4(A_zacetek,A_A_zacetek,B_zacetek,n,dt,razmerje1,razmerje2_1)
[koncA_2,koncA_A_2,koncB,time]=rk4(A_zacetek,A_A_zacetek,B_zacetek,n,dt,razmerje1,razmerje2_2)
[koncA_3,koncA_A_3,koncB,time]=rk4(A_zacetek,A_A_zacetek,B_zacetek,n,dt,razmerje1,razmerje2_3)

[aaaaaaaa1,aaaaaa_a1,casssss]= rk_apr(A_zacetek,A_A_zacetek,n,dt,razmerje1,razmerje2_1)
[aaaaaaaa2,aaaaaa_a2,casssss]= rk_apr(A_zacetek,A_A_zacetek,n,dt,razmerje1,razmerje2_2)
[aaaaaaaa3,aaaaaa_a3,casssss]= rk_apr(A_zacetek,A_A_zacetek,n,dt,razmerje1,razmerje2_3)

#print(aaaaaa_a)
razlika_list1=razlika(koncA_1,aaaaaaaa1)
razlika_list2=razlika(koncA_2,aaaaaaaa2)
razlika_list3=razlika(koncA_3,aaaaaaaa3)


plt.plot(time,razlika_list1,time,razlika_list2,time,razlika_list3)
plt.legend([r'$r_2=10$',r'$r_2=1$',r'$r_2=0.1$'])
plt.grid()
plt.xlabel('čas')
plt.title('absolutna napaka')
naslov='absolutna_napak_'+str(n)+'.png'
plt.savefig(naslov)
plt.show()





##plot analitične rešitve
#[koncA,koncA_A,koncB,time]=rk4(A_zacetek,A_A_zacetek,B_zacetek,n,dt,razmerje1,razmerje2)
# plt.plot(time,koncA,time,koncA_A,time,koncB)
# naslov=r'$q/p=$'+str(razmerje1)+r' $r/qA(0)=$'+str(razmerje2)
# plt.title(naslov)
# plt.xlabel('čas')
# plt.ylabel('koncentracija')
# plt.legend(['a','a*','b=c'],title='koncentracije')
# plt.grid()
# naslov=naslov.replace(' ','_')
# naslov=naslov.replace('$','')
# naslov=naslov.replace('=','_')
# naslov=naslov.replace('/','_')
# naslov=naslov.replace('.','_')
# naslov=naslov+'.png'
# print(naslov)
# plt.savefig(naslov)
# plt.show()
# 


##plot povecave
# razmerje2_1=10
# razmerje2_2=1
# razmerje2_3=0.1
# 
# [koncA,koncA_A_1,koncB,time]=rk4(A_zacetek,A_A_zacetek,B_zacetek,n,dt,razmerje1,razmerje2_1)
# [koncA,koncA_A_2,koncB,time]=rk4(A_zacetek,A_A_zacetek,B_zacetek,n,dt,razmerje1,razmerje2_2)
# [koncA,koncA_A_3,koncB,time]=rk4(A_zacetek,A_A_zacetek,B_zacetek,n,dt,razmerje1,razmerje2_3)
# 
# plt2.plot(time,koncA_A_1,time,koncA_A_2,time,koncA_A_3)
# naslov='povečava a*'
# plt2.title(naslov)
# plt2.xlabel('čas')
# plt2.ylabel('koncentracija a*')
# plt2.legend([r'$r_2=10$',r'$r_2=1$',r'$r_2=0.1$'])
# plt2.grid()
# naslov='povecaca_binarana'
# naslov=naslov+'.png'
# print(naslov)
# plt2.savefig(naslov)
# plt2.show()
