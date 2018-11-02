import matplotlib.pyplot as plt
import numpy as np






def poisci_parametre(A,meritve,napake_meritev):
    w=1/(napake_meritev**2)

    W=np.diag(w)

    B1=np.linalg.inv(np.dot(A.T,A))


    B2=np.dot(A.T,meritve)

    C=np.dot(B1,B2)
    napake_koeficientov=np.sqrt(np.abs(np.diagonal(B1)))
    hi=sum(((meritve-np.dot(A,C))/napake_meritev)**2)/(len(meritve)-len(C))
    # print('procentna napaka',(y-np.dot(A,C))/y*100)
    print(len(meritve),len(C),hi)
    return C,napake_koeficientov,hi




def fitanje():
    y=[41.6 , 37.7875 , 36.4975 , 35.785 , 34.53 , 42.345 , 39.5375 , 37.3525 , 36.36 , 33.915]
    temp=[100 ,  161 , 227 , 270 , 362 , 90 , 149 , 206 , 247 , 352]
    moc=[545 , 602 , 538 , 550 , 522 , 276 , 275 , 274 , 274 , 272]

    y=np.array(y,dtype=float)
    temp_np=np.array(temp,dtype=float)
    moc_np=np.array(moc,dtype=float)

    napaka_np=np.array([0.16 , 0.16 , 0.16 , 0.16 , 0.16 , 0.28 , 0.28 , 0.28 , 0.28 , 0.28],dtype=float)
    # napaka2=np.array([ 0.28 , 0.28 , 0.28 , 0.28 , 0.28 , 0.16 , 0.16 , 0.16 , 0.16 , 0.16 ],dtype=float)


    n=len(y)

    matrika_moc=np.array([moc_np])
    matrika_temp=np.array([temp_np])

    for i in range(2,10):
        matrika_temp=np.vstack((matrika_temp,temp_np**i))
        matrika_moc=np.vstack((matrika_moc,moc_np**i))



    print('bla')

    hi_red=[]
    potence=[]
    st_koef=[]
    for i in range(n-1):
        matrika=np.array([np.ones(n)])

        if i != 0:
            matrika=np.vstack((matrika,matrika_moc[:i]))
        matrika2=matrika
        for j in range(n-i-2):
            if j != 0:
                matrika=np.vstack((matrika2,matrika_temp[:j]))
            # print(matrika.T)
            a,b,c=poisci_parametre(matrika.T,y,napaka_np)
            # print(c,i,j,a)
            # print(i,j)
            hi_red.append(c)
            tekst='('+str(i)+','+str(j)+')'
            potence.append(tekst)
            st_koef.append(j+i)



    return hi_red,potence,st_koef

##zacetek programa:

y=np.array([41.6 , 37.7875 , 36.4975 , 35.785 , 34.53 , 42.345 , 39.5375 , 37.3525 , 36.36 , 33.915],dtype=float)
temp=np.array([100 ,  161 , 227 , 270 , 362 , 90 , 149 , 206 , 247 , 352],dtype=float)
moc=np.array([545 , 602 , 538 , 550 , 522 , 276 , 275 , 274 , 274 , 272],dtype=float)
napaka=np.array([0.16 , 0.16 , 0.16 , 0.16 , 0.16 , 0.28 , 0.28 , 0.28 , 0.28 , 0.28],dtype=float)
w=1/(napaka**2)
W=np.diag(w)

print('testna:')
n=len(y)
A=np.array(np.vstack([np.ones(n),moc,moc**2,moc**3,moc**4,moc**5,moc**6]).T)
#[ 6.86201953e+05  -1.00845488e+04   6.01867466e+01  -1.86938703e-01   3.19466082e-04  -2.85541432e-07   1.04530523e-10]
# A=np.array(np.vstack([np.ones(n),temp,temp**3,temp**4,moc,moc**2,moc**3]).T)
print('moja:')
print(A)

a,b,c=poisci_parametre(A,y,np.ones(n))
print('testna na polinom 6:')
print(a)

tocke=np.linalg.lstsq(A,y)[0]
print(tocke)
print('konec polinom 6:')

plt.plot(y)
plt.plot(np.dot(A,a))
plt.plot(np.dot(A,tocke))
plt.legend(['meritve','fit','lsqrt'])
plt.show()
print('lsqr:')



print('tesnta')

y,x,stevilka=fitanje()

urejeno_stevka=[]
urejeno_indeks=[]
urejeno_hi=[]

for i in range(len(x)):
    for j in range(len(x)):
        if stevilka[j]==i:
            urejeno_hi.append(y[j])
            urejeno_indeks.append(x[j])

print(urejeno_indeks)
print(urejeno_hi)


y=urejeno_hi
x=urejeno_indeks

x1=[i for i in range(len(y))]
plt.plot(x1,y)
plt.xticks(x1,x, rotation='vertical')
plt.grid()
plt.ylabel(r'$\chi^2$')
plt.xlabel('indeks (moč,temperatura)')

# plt.savefig('samo_potence.png')
plt.show()

plt.plot(x1,y)
plt.xticks(x1,x, rotation='vertical')
plt.grid()
plt.yscale('log')
plt.ylabel(r'$\chi^2$')
plt.xlabel('indeks (moč,temperatura)')
# plt.savefig('samo_potence_log.png')
plt.show()

