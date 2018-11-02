import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


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
                vsota = vsota + matrika[k][i] * matrika[k][j] / (y_error[k] ** 2)
            B[i][j] = vsota

    y_param = matrika[0]
    for i in range(m):
        vsota = 0
        for j in range(n):
            vsota = vsota + y_data[j] * matrika[j][i] / (y_error[j] ** 2)
        y_param[i] = vsota

    parametri = np.linalg.solve(B, y_param)

    reg_tocke = matrika.dot(parametri)
    # print('matrika nova', B)
    # print('regresijske tocke', reg_tocke)
    # print('prave tocke:', y_data)
    hi = 0
    for i in range(n):
        delna = ((y_data[i] - reg_tocke[i]) / y_error[i]) ** 2
        hi = hi + delna

    kov = np.linalg.inv(B)
    return [parametri, hi, kov, reg_tocke]


    ##konec funkcije
def linearna(x, k1, n1):
    return k1 * x + n1


x = []
y = []

f = open('farmakoloski.dat', 'r', encoding='utf-8')
data_file = f.readlines()

i = 0
for vrsta in data_file:
    if i > 0:
        vrsta = vrsta.strip('\n')
        podatki = vrsta.split('\t')
        x.append(float(podatki[0]))
        y.append(float(podatki[1]))
    i = i + 1
print(x, y)

f.close()

x_os = 1 / np.array(x)
y_os = 1 / np.array(y)

n = len(x_os)
y_napaka = np.array([3 for i in range(n)])
y_os_napaka =  3* y_os ** 2
#y_os_napaka = y_os_napaka * y_napaka

# print(y_os_napaka)

A = np.vstack([np.ones(n), x_os]).T
# print('matrika A:\n', A)
# print('moja funkcija', lin_reg_error(A, y_os, y_os_napaka))
#
# print('konec moje funkcije \n\n\n\n')

linearno_data = lin_reg_error(A, y_os, y_os_napaka)


print('upam da z napako',linearno_data)
print('konc podatkov')


resitev=linearno_data[0]
# print('vektor', resitev)
tocke = A.dot(resitev)

tocke = 1 / tocke

# print('\ntočke:', tocke)
hi = 0
for i in range(n):
    delna = ((y[i] - tocke[i]) / y_napaka[i]) ** 2
    hi = hi + delna

print(hi)

k = resitev[1]
n = resitev[0]

y0 = 1 / n
a = k * y0
print('kov matrika',linearno_data[2])

delta_y=np.sqrt(linearno_data[2][0][0])*y0**2
napaka_a=np.sqrt((y0*np.sqrt(linearno_data[2][1][1]))**2+(delta_y*k)**2)
napaka_a2=np.sqrt((np.sqrt(linearno_data[2][0][0])*k/n**2)**2+(np.sqrt(linearno_data[2][1][1])/n)**2)
print('napake',delta_y, napaka_a,napaka_a2)
print('koeficienti', k, n, a, y0)

x_range = np.arange(0, 1000, 0.1)
y_range = y0 * x_range / (x_range + a)


plt.plot(x_range,y_range)
plt.xscale('log')
plt.errorbar(x,y,yerr=y_napaka,fmt='',color='r')
plt.grid()
plt.xlabel('doza')
plt.ylabel('odziv')
plt.title('linearna regresija')
plt.savefig('linearna1.png')
plt.show()

v=np.arange(0.001,1.001,0.01)
u=[]
for i in v:
    u.append(linearna(i,k,n))

plt.plot(v,u)
plt.plot(x_os,y_os,'o')
plt.yscale('log')
plt.xscale('log')
#plt.plot(x_os,y_os,'o')
# plt.errorbar(x_os,y_os,yerr=y_os_napaka,fmt='',color='r')
# plt.ylim([10**-16,10**5])
plt.grid()
plt.xlabel('v')
plt.ylabel('u')
plt.savefig('linarna2.png')
plt.show()


####primer nelinearnega fitanja s linearno funkccijpo:








############# primer nelinearnega fitanja:

def f(x, a, y0):
    return (y0*x)/(x+a)


def hi(x_data,y_data,y_error,y0,a):
    vsota=0
    for i in range(len(x_data)):
        vsota+=((f(x_data[i],a,y0)-y_data[i])/y_error[i])**2
    return vsota




###





#######risanje:
# plt.plot(x_range,y_range,'g')
# plt.plot(x1,'r')
# plt.show()
# plt.errorbar(x,y,yerr=y_napaka,fmt='',color='b')
# plt.title('linearno vs nelinearno prilagajanje')
# plt.legend(['linearno','nelinearno','meritve'],loc=7)
# plt.xlabel('doza')
# plt.ylabel('odziv')
#
# # plt.yscale('log')
# plt.xscale('log')
# plt.grid()
# plt.savefig('primerjava-line-nelinearno11111.png')
# plt.show()
