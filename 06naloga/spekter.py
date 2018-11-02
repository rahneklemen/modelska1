import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm



def lin_reg_error(matrika, y_data, y_error):
    '''linearna regresija nad matriko, z nedoločenostjo y tock v y_error.
    Funkcija vrne parametre linearnega fitanja v parametri, ter vrednost hi kvadrat v hi.
    
    Matrika kov je kovariančna matrika. Diagonalni elementi so !kvadrat! napake pripadajocega parametra.
    Izvendiagonalni elementi so korelacija med i in j-tim parametrom.
    
    [parametri,hi,kov] = lin_reg_error(matrika,y_data,y_error)
    

    matrika naj bo naslednje oblike:
    [ 1.          1.        ]
    [ 1.          0.5       ]
    [ 1.          0.14285714]
    [ 1.          0.1       ]
    [ 1.          0.05      ]
    [ 1.          0.01428571]
    [ 1.          0.005     ]
    [ 1.          0.001     ]
    
    dodaj še njihove napake, oz. kovariancno matriko'''

    m = len(matrika[0])
    n = len(matrika)
    B = np.zeros(shape=(m, m))

    for i in range(m):
        for j in range(m):
            vsota = 0
            for k in range(n):
                vsota = vsota + matrika[k][i] * matrika[k][j] * (y_error[k] ** -2)
            B[i][j] = vsota

    y_param = matrika[0]
    for i in range(m):
        vsota = 0
        for j in range(n):
            vsota = vsota + y_data[j] * matrika[j][i] * (y_error[j] ** -2)
        y_param[i] = vsota

    parametri = np.linalg.solve(B, y_param)

    reg_tocke = matrika.dot(parametri)
    print('matrika nova', B)
    print('regresijske tocke', reg_tocke)
    print('prave tocke:', y_data)
    hi = 0
    for i in range(n):
        delna = ((y_data[i] - reg_tocke[i]) / y_error[i]) ** 2
        hi = hi + delna

    kov = np.linalg.inv(B)
    return [parametri, hi, kov]
    ##konec funkcije


f = open('CdL3_linfit.norm', 'r', encoding='utf-8')
branje = f.readlines()
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []

for vrstica in branje:
    if vrstica[0] != '#':
        a = vrstica[2:]
        b = a.strip('\n')
        a = b.split(' ')
        l = [x for x in a if x != '']
        # print(l)
        x1.append(float(l[0]))
        x2.append(float(l[1]))
        x3.append(float(l[2]))
        x4.append(float(l[3]))
        x5.append(float(l[4]))
        #x1 energija
        #x2 krovna plast
        #x3 sredica
        #x4 GSH
        #x5 pectin

#prvi fit

A = np.vstack([x4, x5]).T



#drugi fit

A = np.vstack([x4, x5]).T
B = A.T



#neki plot
# plt.plot(x1, x4, x1, x5)
# plt.legend(['standard Cd-S', 'standard Cd-O'],loc=4)
# plt.grid()
# plt.xlabel('energija')
# plt.ylabel(r'$\frac{dj}{dE}$')
# plt.savefig('standard_specter.png')
# plt.show()
#
#
#
# plt.plot(x1, x2, x1, x3)
# plt.legend(['krovna plast ', 'sredica'],loc=4)
# plt.grid()
# plt.xlabel('energija')
# plt.ylabel(r'$\frac{dj}{dE}$')
# plt.savefig('meritve_specter.png')
# plt.show()



mod_wls = sm.WLS(x3, A,)
res_wls = mod_wls.fit()
parametri=res_wls.params

print(res_wls.summary())


razlika1=x2-np.dot(A,parametri)


mod_wls = sm.WLS(x2, A,)
res_wls = mod_wls.fit()
parametri=res_wls.params

print(res_wls.summary())


razlika2=x3-np.dot(A,parametri)

# razlika2=razlika2/x3
# razlika1=razlika1/x2
plt.plot(x1,razlika1,x1,razlika2)
plt.grid()
plt.legend(['krovna plast ', 'sredica'])
plt.xlabel('energija')
plt.ylabel('razlika med linearnim prilagajanjem in meritvijo')
plt.savefig('razlika_spekter.png')
plt.show()

