import matplotlib.pyplot as plt
import numpy as np

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

    '''

    m = len(matrika[0])
    n = len(matrika)
    B = np.zeros(shape=(m, m))

    for i in range(m):
        for j in range(m):
            vsota = 0
            for k in range(n):
                vsota = vsota + matrika[k][i] * matrika[k][j] / (y_error[k] ** 1)
            B[i][j] = vsota

    y_param = matrika[0]
    for i in range(m):
        vsota = 0
        for j in range(n):
            vsota = vsota + y_data[j] * matrika[j][i] / (y_error[j] ** 1)
        y_param[i] = vsota

    parametri = np.linalg.solve(B, y_param)

    reg_tocke = matrika.dot(parametri)
    #-------
    # reg2=[]
    # #para2=parametri
    # para2=[-43,-0.0643,5.15*10**-7,-8.79*10**-10,0.63,-0.0013,9.14*10**-7]
    # for i in range(len(matrika)):
    #     vsota=0
    #     for j in range(len(matrika[0])):
    #         if i==0:
    #             print(matrika[i][j]*para2[j])
    #         vsota+=matrika[i][j]*para2[j]
    #     reg2.append(vsota)
    #
    # print('sosedovi_podatki',reg2)

    #-------
    # print('matrika nova', B)
    print('regresijske tocke', reg_tocke)
    print('prave tocke:', y_data)
    hi = 0
    for i in range(n):
        delna = ((y_data[i] - reg_tocke[i]) / y_error[i]) ** 2
        hi = hi + delna

    kov = np.linalg.inv(B)
    return [parametri, hi, kov, reg_tocke]


##zacetek programa:

y = np.array([41.600, 37.7875, 36.4975, 35.785, 34.53, 42.345, 39.5375, 37.3525, 36.36, 33.915])
temp = np.array([100, 161, 227, 270, 362, 90, 149, 206, 247, 352],dtype=float)
moc = np.array([545, 602, 538, 550, 522, 276, 275, 274, 274, 272],dtype=float)
napaka = np.array([0.16, 0.16, 0.16, 0.16, 0.16, 0.28, 0.28, 0.28, 0.28, 0.28])

n = len(y)

print(len(y), len(moc), len(temp), len(napaka))

A = np.vstack([np.ones(n), temp, temp**3, temp**4, moc, moc**2 , moc**3]).T
print(A)


print('matrika:\n')
print(A, '\n')

print('\n napaka:')
print(napaka)

print('para',A[0])

print('pravi podatki',y)
resitev = lin_reg_error(A, y, napaka)

print('koeficienti:',resitev[0])

print('primerjava s pravo resitvijo')

tocke = A.dot(resitev[0])

print(tocke)
plt.plot(tocke)
plt.plot(y)
plt.show()


print('--------------')
resitev=np.linalg.lstsq(A,y)
print(resitev)

fit_tocke=A.dot(resitev[0])

print('fit',fit_tocke)


