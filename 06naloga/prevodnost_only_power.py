import statsmodels.api as sm
import numpy as np

import matplotlib.pyplot as plt


def hi(fit_tocke,prave_tocke,napaka,st_param):
    return (sum(((fit_tocke-prave_tocke)/napaka)**2))   /(len(prave_tocke)-(st_param))


def hi_matrika(matrika,pravetocke,utez):
    mod_wls = sm.WLS(pravetocke, matrika,weights=utez)
    res_wls = mod_wls.fit()
    parametri=res_wls.params

    return (hi(np.dot(matrika,parametri),y,napaka,len(parametri)))


def chi_squared(tocne,fit):
    return sum(((tocne-fit)/tocne)**2)


y=np.array([41.6 , 37.7875 , 36.4975 , 35.785 , 34.53 , 42.345 , 39.5375 , 37.3525 , 36.36 , 33.915],dtype=float)
temp=np.array([100 ,  161 , 227 , 270 , 362 , 90 , 149 , 206 , 247 , 352],dtype=float)
moc=np.array([545 , 602 , 538 , 550 , 522 , 276 , 275 , 274 , 274 , 272],dtype=float)
napaka=np.array([0.16 , 0.16 , 0.16 , 0.16 , 0.16 , 0.28 , 0.28 , 0.28 , 0.28 , 0.28],dtype=float)
w=1/(napaka**2)
W=np.diag(w)

print('testna:')
n=len(y)
A=np.array(np.vstack([np.ones(n),temp,temp**3,temp**4,moc,moc**2,moc**3]).T)

#[ 6.86201953e+05  -1.00845488e+04   6.01867466e+01  -1.86938703e-01   3.19466082e-04  -2.85541432e-07   1.04530523e-10]

resitve_lubej=np.array([-42,-0.0643,5.18*10**(-7),-8.79*10**(-10),0.63,-0.0013,9.14*10**(-7)])




print('drugi primer')

y=np.array([41.6 , 37.7875 , 36.4975 , 35.785 , 34.53 , 42.345 , 39.5375 , 37.3525 , 36.36 , 33.915],dtype=float)
temp=np.array([100 ,  161 , 227 , 270 , 362 , 90 , 149 , 206 , 247 , 352],dtype=float)
moc=np.array([545 , 602 , 538 , 550 , 522 , 276 , 275 , 274 , 274 , 272],dtype=float)
napaka=np.array([0.16 , 0.16 , 0.16 , 0.16 , 0.16 , 0.28 , 0.28 , 0.28 , 0.28 , 0.28],dtype=float)
w=1/(napaka**2)


n=len(y)


A=np.array([np.ones(n)])
B=A

hi_podatki=[]

hi_podatki.append(hi_matrika(B.T,y,w))
B=np.vstack((A,temp))
hi_podatki.append(hi_matrika(B.T,y,w))
B=np.vstack((A,moc))
hi_podatki.append(hi_matrika(B.T,y,w))
indeks=['(0,0)','(1,0)','(0,1)']





for i in range(8):
    A=np.vstack((A,temp**(i+1)))

    B=A
    for j in range(7-i):
        B=np.vstack((B,moc**(j+1)))
        #print('-\n',B)
        hi_podatki.append(hi_matrika(B.T,y,w))
        list='('+str(i+1)+','+str(j+1)+')'
        indeks.append(list)
        if i==1 and j==3:
            mod_wls = sm.WLS(y, B.T,weights=w)
            res_wls = mod_wls.fit()


            parametri=res_wls.params
            fit_ddata=np.dot(B.T,parametri)
            print(res_wls.summary())
            print('chi',chi_squared(y,fit_ddata))



print(indeks)
x1=[i for i in range(len(hi_podatki))]

a=min(hi_podatki)
print(a)
#a=0.876
plt.plot(hi_podatki)
plt.grid()
plt.xticks(x1,indeks, rotation='vertical')
plt.xlabel('kombinacija')
plt.ylabel(r'$\chi^2$')
plt.yscale('log')
plt.show()

# plt.plot(abs(fit_ddata-y))
# plt.grid()
# plt.yscale('log')
# plt.show()