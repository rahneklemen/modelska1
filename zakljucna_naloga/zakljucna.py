import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib as mpl
from matplotlib import ticker



def rezina(razdalja,sirina,x,y,z):
    x_koordinata=[]
    y_koordinata=[]
    for i in range(len(z)):
        if razdalja-sirina<z[i]<razdalja+sirina:
            x_koordinata.append(x[i])
            y_koordinata.append(y[i])

    return x_koordinata,y_koordinata



def polozaj_abs_nevtronov(prosta_pot,n):
    xpolozaj = []
    ypolozaj = []
    zpolozaj = []


    x = np.zeros(n)
    y = np.random.rand(n)
    z = np.random.rand(n)

    r = -1 * prosta_pot * np.log(1 - np.random.rand(n))
    fi = np.random.rand(n) * 2 * np.pi
    t = np.arccos(2 * np.random.rand(n) - 1)




    for i in range(n):
        x_nov = x[i] + r[i] * np.cos(fi[i]) * np.sin(t[i])
        y_nov = y[i] + r[i] * np.sin(fi[i]) * np.sin(t[i])
        z_nov = z[i] + r[i] * np.cos(t[i])

        if 0<x_nov<1 and 0<y_nov<1 and 0 < z_nov <1 :
            xpolozaj.append(x_nov)
            ypolozaj.append(y_nov)
            zpolozaj.append(z_nov)
    print('ena sestina')
    x = np.ones(n)
    y = np.random.rand(n)
    z = np.random.rand(n)

    r = -1 * prosta_pot * np.log(1 - np.random.rand(n))
    fi = np.random.rand(n) * 2 * np.pi
    t = np.arccos(2 * np.random.rand(n) - 1)

    for i in range(n):
        x_nov = x[i] + r[i] * np.cos(fi[i]) * np.sin(t[i])
        y_nov = y[i] + r[i] * np.sin(fi[i]) * np.sin(t[i])
        z_nov = z[i] + r[i] * np.cos(t[i])

        if 0<x_nov<1 and 0<y_nov<1 and 0 < z_nov <1 :
            xpolozaj.append(x_nov)
            ypolozaj.append(y_nov)
            zpolozaj.append(z_nov)

    y = np.zeros(n)
    x = np.random.rand(n)
    z = np.random.rand(n)

    r = -1 * prosta_pot * np.log(1 - np.random.rand(n))
    fi = np.random.rand(n) * 2 * np.pi
    t = np.arccos(2 * np.random.rand(n) - 1)

    for i in range(n):
        x_nov = x[i] + r[i] * np.cos(fi[i]) * np.sin(t[i])
        y_nov = y[i] + r[i] * np.sin(fi[i]) * np.sin(t[i])
        z_nov = z[i] + r[i] * np.cos(t[i])

        if 0<x_nov<1 and 0<y_nov<1 and 0 < z_nov <1 :
            xpolozaj.append(x_nov)
            ypolozaj.append(y_nov)
            zpolozaj.append(z_nov)

    y = np.ones(n)
    x = np.random.rand(n)
    z = np.random.rand(n)

    r = -1 * prosta_pot * np.log(1 - np.random.rand(n))
    fi = np.random.rand(n) * 2 * np.pi
    t = np.arccos(2 * np.random.rand(n) - 1)

    for i in range(n):
        x_nov = x[i] + r[i] * np.cos(fi[i]) * np.sin(t[i])
        y_nov = y[i] + r[i] * np.sin(fi[i]) * np.sin(t[i])
        z_nov = z[i] + r[i] * np.cos(t[i])

        if 0<x_nov<1 and 0<y_nov<1 and 0 < z_nov <1 :
            xpolozaj.append(x_nov)
            ypolozaj.append(y_nov)
            zpolozaj.append(z_nov)

    z = np.zeros(n)
    y = np.random.rand(n)
    x = np.random.rand(n)

    r = -1 * prosta_pot * np.log(1 - np.random.rand(n))
    fi = np.random.rand(n) * 2 * np.pi
    t = np.arccos(2 * np.random.rand(n) - 1)

    for i in range(n):
        x_nov = x[i] + r[i] * np.cos(fi[i]) * np.sin(t[i])
        y_nov = y[i] + r[i] * np.sin(fi[i]) * np.sin(t[i])
        z_nov = z[i] + r[i] * np.cos(t[i])

        if 0<x_nov<1 and 0<y_nov<1 and 0 < z_nov <1 :
            xpolozaj.append(x_nov)
            ypolozaj.append(y_nov)
            zpolozaj.append(z_nov)

    z= np.ones(n)
    y = np.random.rand(n)
    x = np.random.rand(n)

    r = -1 * prosta_pot * np.log(1 - np.random.rand(n))
    fi = np.random.rand(n) * 2 * np.pi
    t = np.arccos(2 * np.random.rand(n) - 1)

    for i in range(n):
        x_nov = x[i] + r[i] * np.cos(fi[i]) * np.sin(t[i])
        y_nov = y[i] + r[i] * np.sin(fi[i]) * np.sin(t[i])
        z_nov = z[i] + r[i] * np.cos(t[i])

        if 0<x_nov<1 and 0<y_nov<1 and 0 < z_nov <1 :
            xpolozaj.append(x_nov)
            ypolozaj.append(y_nov)
            zpolozaj.append(z_nov)


    return xpolozaj,ypolozaj,zpolozaj







print('zakljucil streljanje nevtronov')




prosta_pot=0.1
n=10**5
x,y,z=polozaj_abs_nevtronov(prosta_pot,n)
a,b=rezina(0.5,0.1,x,y,z)

print('zakljucil rezino')
naslov='porazdelitev_lamda_'+str(prosta_pot).replace('.','_')+'n_'+str(n)+'.png'
# ,norm = mpl.colors.LogNorm()
plt.hist2d(a,b, bins=50)
plt.title('porazdelitev absorpcije nevtronov v preseku kocke\n'+r'$\lambda =$ '+str(prosta_pot))
cb=plt.colorbar(format='%d')
tick_locator = ticker.MaxNLocator(nbins=5)
cb.locator = tick_locator
cb.update_ticks()
cb.set_label('število absorbiranih nevtronov')
plt.savefig(naslov)
plt.show()







###3d narisana kocka
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(x0,y0,z0)
# plt.show()