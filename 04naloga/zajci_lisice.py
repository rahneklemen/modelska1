import matplotlib.pyplot as plt
import numpy

n=2000
h=1/100



def f(t,z,l,alfa):
    return alfa*z*(1-l)

def g(t,z,l,gama):
    return gama*l*(z-1)
    
    
def zajci_lisice(z0,l0,prvi_parameter,drugi_parameter):
    zajec=[0 for i in range(n)]
    lisica=[0 for i in range(n)]
    x=[i*h for i in range(n)]
    
    zajec[0]=z0
    lisica[0]=l0
    
    
    for i in range(1,n):
        #print(i)
        cas=x[i-1]
        z=zajec[i-1]
        l=lisica[i-1]
        #print('z,l:\t',z,l)
        
        k1=h*f(cas,z,l,prvi_parameter)
        l1=h*g(cas,z,l,drugi_parameter)
        #print('k1,l2',k1,l1)
        
        k2=h*f(cas+h/2,z+k1/2,l+l1/2,prvi_parameter)
        l2=h*g(cas+h/2,z+k1/2,l+l1/2,drugi_parameter)
        
        k3=h*f(cas+h/2,z+k2/2,l+l2/2,prvi_parameter)
        l3=h*g(cas+h/2,z+k2/2,l+l2/2,drugi_parameter)
        
        k4=h*f(cas+h,z+k3,l+l3,prvi_parameter)
        l4=h*g(cas+h,z+k3,l+l3,drugi_parameter)
        
        K=(k1+2*k2+2*k3+k4)/6
        L=(l1+2*l2+2*l3+l4)/6
        #print(K,L)
        zajec[i]=z+K
        lisica[i]=l+L
        #print(zajec[i],lisica[i])
        #print([zajec,lisica])
    return [zajec,lisica,x]





def frekvenca(tabela,tabela_cas):
    zacetna=tabela[0]
    j=0
    if tabela[0]<tabela[1]:
        for i in range(1,len(tabela)):
            if tabela[i-1]<zacetna<tabela[i]:
                return tabela_cas[i]
    if tabela[0]>tabela[1]:
        for i in range(1,len(tabela)):
            if tabela[i-1]>zacetna>tabela[i]:
                return tabela_cas[i]
            






##fazni diagram:
# a=0.5
# b=2
# a2=1
# b2=1
# a3=2
# b3=0.5
# a4=3
# b4=2
# 
# lisica0=1.2
# zajec0=0.8
# zajec20=2
# lisica20=3
# zajec30=0.5
# lisica30=3
# zajec40=1
# lisica40=0.1
# 
# 
# [zajec,lisica]=zajci_lisice(zajec0,lisica0,a,b)
# [zajec2,lisica2]=zajci_lisice(zajec0,lisica0,a2,b2)
# [zajec3,lisica3]=zajci_lisice(zajec0,lisica0,a3,b3)
# [zajec4,lisica4]=zajci_lisice(zajec0,lisica0,a4,b4)
##plot stevila zajce, lisic, v odvisnosti od casa:
# naslov=r'$\alpha=$'+str(alfa)+'\t$\gamma=$'+str(gama)+'\nl(0)='+str(lisica0)+'  '+'z(0)='+str(zajec0)
# 
# plt.plot(x,lisica4,x,zajec4)
# plt.legend(['#lisic','#zajcev'])
# plt.title(naslov)
# plt.grid()
# plt.xlabel('čas')
# plt.ylabel('')
# #plt.yscale('log')
# naslov='alfa'+str(a)+'gama'+str(b)+'l0'+str(lisica0)+'z0'+str(zajec0)
# naslov=naslov.replace('.','-')
# naslov='sadfasfasthtrththfas.png'
# plt.savefig(naslov)
# 
# plt.show()



# naslov='fazni diagram pri z(0)='+str(zajec0)+' l(0)='+str(lisica0)
# plt.plot(zajec,lisica,zajec2,lisica2,zajec3,lisica3,zajec4,lisica4)
# plt.legend([r'$\alpha$='+str(a)+r' $\gamma=$'+str(b),r'$\alpha$='+str(a2)+r' $\gamma=$'+str(b2),r'$\alpha$='+str(a3)+r' $\gamma=$'+str(b3),r'$\alpha$='+str(a4)+r' $\gamma=$'+str(b4)])
# 
# plt.title(naslov)
# plt.xlabel('#zajcev')
# plt.ylabel('#lisic')
# plt.grid()
# naslov1=naslov.replace('.','_')
# naslov='fazni-diagram-konstantni-zacetni-pogoji.png'
# plt.savefig(naslov)
# plt.show()




##določitev frekvence:


perioda=[]
perioda2=[]
perioda3=[]
zacetna_vrednost=[]
for i in range(100):
    a=0.5
    b=2
    
    a2=2
    b2=0.5
    
    a3=1
    b3=1
    
    zajec0=1
    lisica0=(i+1)/10
    [zajec,lisica,casovna_os]=zajci_lisice(zajec0,lisica0,a,b)
    [zajec2,lisica2,casovna_os2]=zajci_lisice(zajec0,lisica0,a2,b2)
    [zajec3,lisica3,casovna_os3]=zajci_lisice(zajec0,lisica0,a3,b3)
    
    perioda.append(frekvenca(zajec,casovna_os))
    perioda2.append(frekvenca(zajec2,casovna_os2))
    perioda3.append(frekvenca(zajec3,casovna_os3))
    
    zacetna_vrednost.append(lisica0)
    
    
    
naslov='odvisnost periode od začetnih pogojev, zajec(0)=1'
plt.plot(zacetna_vrednost,perioda,zacetna_vrednost,perioda2,zacetna_vrednost,perioda3)

plt.legend([r'$\alpha=0.5$ $\gamma=2$',r'$\alpha=2$ $\gamma=0.5$',r'$\alpha=1$ $\gamma=1$'])

plt.title(naslov)
plt.xlabel('zacetna vrednost')
plt.ylabel('perioda')
plt.grid()
naslov='frekvencna_odvisnost.png'
plt.savefig(naslov)
plt.show()