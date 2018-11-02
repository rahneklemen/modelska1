import statsmodels.api as sm
import numpy as np
import scipy.stats as chisqr


import matplotlib.pyplot as plt


def hi(fit_tocke,prave_tocke,napaka,st_param):
    return (sum(((fit_tocke-prave_tocke)/napaka)**2))   /(len(prave_tocke)-(st_param))


def hi_matrika(matrika,pravetocke,utez):
    mod_wls = sm.WLS(pravetocke, matrika,weights=utez)
    res_wls = mod_wls.fit()
    parametri=res_wls.params


    return (hi(np.dot(matrika,parametri),y,napaka,len(parametri)))



y=np.array([41.6 , 37.7875 , 36.4975 , 35.785 , 34.53 , 42.345 , 39.5375 , 37.3525 , 36.36 , 33.915],dtype=float)
temp=np.array([100 ,  161 , 227 , 270 , 362 , 90 , 149 , 206 , 247 , 352],dtype=float)
moc=np.array([545 , 602 , 538 , 550 , 522 , 276 , 275 , 274 , 274 , 272],dtype=float)
napaka=np.array([0.16 , 0.16 , 0.16 , 0.16 , 0.16 , 0.28 , 0.28 , 0.28 , 0.28 , 0.28],dtype=float)
w=1/(napaka**2)
W=np.diag(w)


n=len(y)


A=np.array([np.ones(n)])
B=A

hi_podatki=[]
deg_of_fredom=[]

hi_podatki.append(hi_matrika(B.T,y,w))
deg_of_fredom.append(len(y)-len(B))
B=np.vstack((A,temp))
hi_podatki.append(hi_matrika(B.T,y,w))
deg_of_fredom.append(len(y)-len(B))
B=np.vstack((A,moc))
hi_podatki.append(hi_matrika(B.T,y,w))
indeks=['(0,0)','(1,0)','(0,1)']
deg_of_fredom.append(len(y)-len(B))



skupaj=3


while(skupaj<=9):

    for i in range(1,10):

        A=np.vstack((A,moc**(i+1)))
        B=A

        skupaj+=1

        skupaj2=skupaj


        for j in range(1,10):

            B=np.vstack((B,temp**(j+1)))
            C=B
            C2=B

            skupaj2+=1

            skupaj3=skupaj2

            for k in range(1,10):

                C=np.vstack((C,moc*temp**k))
                C2=np.vstack((C2,temp*moc**k))
                skupaj3+=1

                if skupaj3<=11:
                    hi_podatki.append(hi_matrika(C.T,y,w))
                    indeks.append('('+str(i)+','+str(j+1)+',t'+str(k)+')')
                    deg_of_fredom.append(len(y)-len(C))
                    #print(len(C))


                    hi_podatki.append(hi_matrika(C2.T,y,w))
                    indeks.append('('+str(i)+','+str(j)+',m'+str(k)+')')
                    deg_of_fredom.append(len(y)-len(C))


stevec=0
for i in hi_podatki:
    if i<0.877:
        stevec+=1
print(stevec)
print(min(hi_podatki))

x1=[i for i in range(len(indeks))]
plt.plot(hi_podatki)
plt.yscale('log')
plt.grid()
plt.xticks(x1,indeks, rotation='vertical')
plt.title(r'potence $TP$')
plt.xlabel('kombinacija')
plt.ylabel(r'$\chi^2_{red}$')
plt.yscale('log')


plt.show()











