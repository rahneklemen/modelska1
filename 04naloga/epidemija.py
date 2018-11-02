import matplotlib.pyplot as plt
import numpy as np

N=20000
h=1/100



##zacetni pogoji:
# D0=0.5
# O0=0.4
# I0=0.1


##funkcije:

def D(t,D,O,I,A,B):
    return -A*D*O

def O(t,D,O,I,A,B):
    return A*D*O-B*O

def I(t,D,O,I,A,B):
    return B*O
    


##runge-kutta 4 funkcija:
def epidemija(D0,O0,I0,A,B):
    dovzetni=[0 for i in range(n)]
    okuzeni=[0 for i in range(n)]
    imuni=[0 for i in range(n)]
    #print(len(imuni))
    x=[i*h for i in range(n)]
    #print(len(x))
    skupaj=[0 for i in range(n)]
    
    
    dovzetni[0]=D0
    okuzeni[0]=O0
    imuni[0]=I0
    skupaj[0]=D0+O0+I0
    
    
    
    for i in range(1,n):
        #print(i)
        
        cas=x[i-1]
        a=dovzetni[i-1]
        b=okuzeni[i-1]
        c=imuni[i-1]
        
        #print('z,l:\t',a,f,cas)
        
        k1=h*D(cas,a,b,c,A,B)
        l1=h*O(cas,a,b,c,A,B)
        m1=h*I(cas,a,b,c,A,B)
        #print('k1,l2',k1,l1)
        
        k2=h*D(cas+h/2,a+k1/2,b+l1/2,c+m1/2,A,B)
        l2=h*O(cas+h/2,a+k1/2,b+l1/2,c+m1/2,A,B)
        m2=h*I(cas+h/2,a+k1/2,b+l1/2,c+m1/2,A,B)
        
        k3=h*D(cas+h/2,a+k2/2,b+l2/2,c+m2/2,A,B)
        l3=h*O(cas+h/2,a+k2/2,b+l2/2,c+m2/2,A,B)
        m3=h*I(cas+h/2,a+k2/2,b+l2/2,c+m2/2,A,B)
        
        k4=h*D(cas+h,a+k3,b+l3,c+m3,A,B)
        l4=h*O(cas+h,a+k3,b+l3,c+m3,A,B)
        m4=h*I(cas+h,a+k3,b+l3,c+m3,A,B)
        
        K=(k1+2*k2+2*k3+k4)/6
        L=(l1+2*l2+2*l3+l4)/6
        M=(m1+2*m2+2*m3+m4)/6
        
        #print(K,L)
        dovzetni[i]=a+K
        okuzeni[i]=(b+L)*1
        imuni[i]=c+M
        skupaj[i]=a+b+c+K+L+M
        #print(zajec[i],lisica[i])
        #print([zajec,lisica])
    return [dovzetni,okuzeni,imuni,skupaj,x]


##parametri:
par_A=1
par_B=0.1


# 
n=2000
#[dovzetni,okuzeni,imuni,skupaj,x]=epidemija(0.900,0.100,0,par_A,par_B)
#print([dovzetni,okuzeni,imuni])
#print(skupaj)

def max_epidemije(zacetno_okuzenih,par_A,par_B):
    stevilo_postelj=[0 for i in range(100)]
    cas_postelj=[0 for i in range(100)]
    cepljenih=[0 for i in range(100)]
    for i in range(100):
        cepljeni=i/100
        cepljenih[i]=cepljeni
        zdravi=1-cepljeni-zacetno_okuzenih
        if zdravi<0:
            break
        [dovzetni,okuzeni,imuni,skupaj,y]=epidemija(zdravi,zacetno_okuzenih,cepljeni,par_A,par_B)
        maksimum=max(okuzeni)
        polozaj=okuzeni.index(maksimum)
        stevilo_postelj[i]=maksimum
        cas_postelj[i]=y[polozaj]
        #print(max(okuzeni),y[polozaj],cepljenih)
    print(cepljenih)
    print(stevilo_postelj,cepljenih)
    return [stevilo_postelj,cas_postelj,cepljenih]

zdravi=0.4
zacetno_okuzenih=0.2
cepljeni=0.4
[dovzetni,okuzeni,imuni,skupaj,x]=epidemija(zdravi,zacetno_okuzenih,cepljeni,par_A,par_B)


naslov='D(0)='+str(zdravi)+' O(0)='+str(zacetno_okuzenih)+' I(0)='+str(cepljeni)
#print(len(x),len(dovzetni))
plt.plot(x,dovzetni,x,okuzeni,x,imuni,x,skupaj)
plt.legend(['dovzetni','okuzeni','imuni','skupaj'])
plt.title(naslov)
plt.grid()
plt.xlabel('čas')
plt.ylabel('')
naslov=naslov.replace('.','_')
naslov=naslov.replace('=','_')
naslov=naslov.replace(' ','_')
naslov=naslov+'.png'
#plt.savefig(naslov)
plt.show()

    
##polozaj, kje potrebno max postelj in koliko

zacetek_okuzenih=0.1
[postelje1,cas_max1,delez_cepljenih1]=max_epidemije(zacetek_okuzenih,par_A,par_B)

zacetek_okuzenih=0.3
[postelje2,cas_max2,delez_cepljenih2]=max_epidemije(zacetek_okuzenih,par_A,par_B)

zacetek_okuzenih=0.5
[postelje3,cas_max3,delez_cepljenih3]=max_epidemije(zacetek_okuzenih,par_A,par_B)

# #potreben postelje:
# naslov='epidemija'
# plt.plot(delez_cepljenih1,postelje1,delez_cepljenih2,postelje2,delez_cepljenih3,postelje3)
# plt.title(naslov)
# plt.legend(['0.1','0.3','0.5'],title='začetno okuzenih')
# plt.grid()
# plt.xlabel('delež imunih na začetku')
# plt.ylabel('stevilo postelj potrebnih na vrhuncu epidemije')
# plt.savefig('potreben_postelje.png')
# plt.show()

#potreben cas postelj po izbruhu epidemije
# naslov='epidemija'
# plt.plot(delez_cepljenih1,cas_max1,delez_cepljenih2,cas_max2,delez_cepljenih3,cas_max3)
# plt.title(naslov)
# plt.legend(['0.1','0.3','0.5'],title='začetno okuzenih')
# plt.grid()
# plt.xlabel('delež imunih na začetku')
# plt.ylabel('čas kdaj pride vrhunec epidemije po izbruhu')
# plt.savefig('potreben_cas_postelje.png')
# plt.show()

##fazni diagram:
# naslov='Fazni diagram'
# plt.plot(st_atomov,st_fotonov)
# plt.title(naslov)
# plt.xlabel('# atomov')
# plt.ylabel('# fotonov')
# plt.grid()
# plt.show()

##določitev frekvence:

#spreminjajmo zacetnos stevilo
# t=20
# 
# for i in range(t):
#     [zajec,lisica]=zajci_lisice(zajec0,lisica0)
    


