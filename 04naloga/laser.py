import matplotlib.pyplot as plt
import numpy as np


n=2000
h=1/100

def m(t,A,F):
    return r-p*A*(F+1)

def g(t,A,F):
    return F/p*(A-1)
    
    
def laser(A0,F0):
    atomi=[0 for i in range(n)]
    fotoni=[0 for i in range(n)]
    x=[i*h for i in range(n)]
    
    atomi[0]=A0
    fotoni[0]=F0
    
    
    for i in range(1,n):
        #print(i)
        cas=x[i-1]
        a=atomi[i-1]
        f=fotoni[i-1]
        #print('z,l:\t',a,f,cas)
        
        k1=h*m(cas,a,f)
        l1=h*g(cas,a,f)
        #print('k1,l2',k1,l1)
        
        k2=h*m(cas+h/2,a+k1/2,f+l1/2)
        l2=h*g(cas+h/2,a+k1/2,f+l1/2)
        
        k3=h*m(cas+h/2,a+k2/2,f+l2/2)
        l3=h*g(cas+h/2,a+k2/2,f+l2/2)
        
        k4=h*m(cas+h,a+k3,f+l3)
        l4=h*g(cas+h,a+k3,f+l3)
        
        K=(k1+2*k2+2*k3+k4)/6
        L=(l1+2*l2+2*l3+l4)/6
        #print(K,L)
        atomi[i]=a+K
        fotoni[i]=f+L
        #print(zajec[i],lisica[i])
        #print([zajec,lisica])
    return [atomi,fotoni,x]

r=5
p=0.2

A0=0.03
F0=0.1

[st_atomov,st_fotonov,cas]=laser(A0,F0)
print(len(st_atomov),len(st_fotonov),len(cas))

##plot stevila atomov, fotonov, v odvisnosti od casa:
naslov='r= '+str(r)+'  p= '+str(p)+'\n'+r' $A_0=$'+str(A0)+r' $F_0=$'+str(F0)
plt.plot(cas,st_atomov,cas,st_fotonov)
plt.legend(['#atomov','#fotonov'])
plt.title(naslov)
plt.grid()
plt.xlabel('čas')
plt.ylabel('')
naslov=naslov.replace(' ','_')
naslov=naslov.replace('.','_')
naslov=naslov.replace('\n','_')
naslov=naslov.replace('$','_')
naslov=naslov.replace('\t','_')
naslov=naslov+'.png'
print(naslov)
plt.savefig(naslov)
plt.show()


##fazni diagram:
# naslov='Fazni diagram'
# plt.plot(st_atomov,st_fotonov)
# plt.title(naslov)
# plt.xlabel('# atomov')
# plt.ylabel('# fotonov')
# plt.grid()
# plt.show()


def frekvenca():
    1
    
    
