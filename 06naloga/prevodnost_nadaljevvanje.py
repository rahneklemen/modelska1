import matplotlib.pyplot as plt
import numpy as np


def poisci_parametre(A,meritve,napake_meritev):
    w=1/napake_meritev**2
    W=np.diag(w)

    B1=np.linalg.inv(np.dot(A.T,np.dot(W,A)))


    B2=np.dot(A.T,np.dot(W,meritve))

    C=np.dot(B1,B2)
    napake_koeficientov=np.sqrt(np.diagonal(B1))
    hi=sum(((meritve-np.dot(A,C))/napake_meritev)**2)/(len(meritve)-len(C))
    # print('procentna napaka',(y-np.dot(A,C))/y*100)
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

    for i in range(2,5):
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
        for j in range(n-i-1):
            if j != 0:
                matrika=np.vstack((matrika2,matrika_temp[:j]))
            matrika3=matrika
            # print(matrika.T)
            print('stevilo',i+1+j)
            if i+j+1<n:
                for k in range(n-i-j-1):
                    # print(k,n-j-i)
                    matrika3=np.vstack((matrika3,1/(temp_np**(k+1))))
                    a,b,c=poisci_parametre(matrika3.T,y,napaka_np)
                    print(c,i,j,k)
                    hi_red.append(c)
                    tekst='('+str(i)+','+str(j)+')'
                    potence.append(tekst)
                    st_koef.append(j+i+k+1)
            else:
                    matrika3=np.vstack((matrika3,1/(temp_np**(k+1))))
                    a,b,c=poisci_parametre(matrika3.T,y,napaka_np)
                    print(c,i,j,k)
                    hi_red.append(c)
                    tekst='('+str(i)+','+str(j)+')'
                    potence.append(tekst)
                    st_koef.append(j+i+k+1)




    return hi_red,potence,st_koef

##zacetek programa:

# y=np.array([41.6 , 37.7875 , 36.4975 , 35.785 , 34.53 , 42.345 , 39.5375 , 37.3525 , 36.36 , 33.915],dtype=float)
# temp=np.array([100 ,  161 , 227 , 270 , 362 , 90 , 149 , 206 , 247 , 352],dtype=float)
# moc=np.array([545 , 602 , 538 , 550 , 522 , 276 , 275 , 274 , 274 , 272],dtype=float)
# napaka=np.array([0.16 , 0.16 , 0.16 , 0.16 , 0.16 , 0.28 , 0.28 , 0.28 , 0.28 , 0.28],dtype=float)
# w=1/napaka**2
# W=np.diag(w)




print('tesnta')
y,x,stevilka=fitanje()

urejeno_stevka=[]
urejeno_indeks=[]
urejeno_hi=[]

# for i in range(len(x)):
#     for j in range(len(x)):
#         if stevilka[j]==i:
#             urejeno_hi.append(y[j])
#             urejeno_indeks.append(x[j])
#
# print(urejeno_indeks)
# print(urejeno_hi)
#
#
# y=urejeno_hi
# x=urejeno_indeks


plt.plot(y)


# plt.savefig('samo_potence.png')
plt.show()

