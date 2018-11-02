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

def sipanje(fi, theta):

    #random tocka na preseku jedra:
    alfa = np.random.rand() * np.pi * 2
    radij = np.random.rand() ** (0.5)
    #transformacija tocke iz preseka na povrsino sfere:
    fi1 = np.arctan((radij * np.sin(alfa)) / np.sqrt(1 - radij ** 2))
    theta1 = np.arccos(radij * np.cos(alfa))

    #transformacija kota (fi1, theta1), tako da tocka trka na sferi gleda nevtron
    fi0 = (fi + np.pi + fi1)
    theta0 = (theta + theta1 + np.pi / 2) % (2 * np.pi)
    if theta0 > np.pi:
        theta0 = 2 * np.pi - theta0

    #tocka trka s jedrom
    Tx = np.cos(fi) * np.sin(theta)
    Ty = np.sin(fi) * np.sin(theta)
    Tz = np.cos(theta)


    # Tx0=Tx-(r1+r2)*np.cos(fi0)
    # Ty0=Ty-(r1+r2)*np.sin(fi0)

    # theta0=0
    r1=1
    r2=(12)**(1/3)

    ##sredisce krogle:
    Tx1 = Tx - (r1 + r2) * np.cos(fi0) * np.sin(theta0)
    Ty1 = Ty - (r1 + r2) * np.sin(fi0) * np.sin(theta0)
    Tz1 = Tz - (r1 + r2) * np.cos(theta0)

    # x.append(Tx1)
    # y.append(Ty1)
    # z.append(Tz1)

    ##normirana smer od sredisca dveh krogel:

    normx = np.cos(fi0) * np.sin(theta0)
    normy = np.sin(fi0) * np.sin(theta0)
    normz = np.cos(theta0)

    ##projekcija vpadnega delca na normiran vektor

    proj = (Tx * normx + Ty * normy + Tz * normz) * -1
    # print(proj)
    #smer odbitega nbevtrona
    x= Tx + 2 * proj * normx
    y = Ty + 2 * proj * normy
    z =  Tz + 2 * proj * normz

    #dolzina vektorja
    normalizacija=np.sqrt(x**2+y**2+z**2)

    return np.arctan(y/x) , np.arccos(z/(normalizacija))


def polozaj_abs_nevtronov(prosta_pot,prosta_pot_sipanje,n):
    xpolozaj = []
    ypolozaj = []
    zpolozaj = []


    x = np.zeros(n)
    y = np.random.rand(n)
    z = np.random.rand(n)

    r = -1 * prosta_pot * np.log(1 - np.random.rand(n))
    fi = np.random.rand(n) * 2 * np.pi
    t = np.arccos(2 * np.random.rand(n) - 1)

    rs = -1 * prosta_pot_sipanje * np.log(1 - np.random.rand(n))


    for i in range(n):
        if rs[i]>r[i]:
            x_nov = x[i] + r[i] * np.cos(fi[i]) * np.sin(t[i])
            y_nov = y[i] + r[i] * np.sin(fi[i]) * np.sin(t[i])
            z_nov = z[i] + r[i] * np.cos(t[i])

            if 0<x_nov<1 and 0<y_nov<1 and 0 < z_nov <1 :
                xpolozaj.append(x_nov)
                ypolozaj.append(y_nov)
                zpolozaj.append(z_nov)

        else:
            a=fi[i]
            b=t[i]
            pot=rs[i]
            radijsipanje=rs[i]

            #tocka sipanja
            x_nov = x[i] + radijsipanje * np.cos(a) * np.sin(b)
            y_nov = y[i] + radijsipanje * np.sin(a) * np.sin(b)
            z_nov = z[i] + radijsipanje * np.cos(b)

            while(0<x_nov<1 and 0<y_nov<1 and 0<z_nov<1):

                pot_dodatna=-1 * prosta_pot_sipanje * np.log(1 - np.random.rand())
                pot += pot_dodatna

                #nova smer nevtrona, a,b sta kota phi in theta
                a,b= sipanje(a,b)

                x_nov=x_nov + pot_dodatna* np.cos(a)*np.sin(b)
                y_nov= y_nov + pot_dodatna * np.sin(a) * np.sin(b)
                z_nov=z_nov + pot_dodatna * np.cos(b)

                if pot > r[i]:
                    #razdalja od sipanja do absorpcije:
                    r_do_sipanja= pot_dodatna - (pot - r[i])
                    #tocka absorpcije:
                    x_nov = x_nov + r_do_sipanja * np.cos(a) * np.sin(b)
                    y_nov = y_nov + r_do_sipanja * np.sin(a) * np.sin(b)
                    z_nov = z_nov + r_do_sipanja * np.cos(b)

                    if 0 < x_nov < 1 and 0 < y_nov < 1 and 0 < z_nov < 1:
                        xpolozaj.append(x_nov)
                        ypolozaj.append(y_nov)
                        zpolozaj.append(z_nov)
                        break
                else:
                    #razdalja do novega sipanja: pot_dodatna
                    #tocka absorpcije:
                    x_nov = x_nov + pot_dodatna * np.cos(a) * np.sin(b)
                    y_nov = y_nov + pot_dodatna * np.sin(a) * np.sin(b)
                    z_nov = z_nov + pot_dodatna * np.cos(b)

    print('\t 1/6')
    x = np.ones(n)
    y = np.random.rand(n)
    z = np.random.rand(n)

    r = -1 * prosta_pot * np.log(1 - np.random.rand(n))
    fi = np.random.rand(n) * 2 * np.pi
    t = np.arccos(2 * np.random.rand(n) - 1)

    rs = -1 * prosta_pot_sipanje * np.log(1 - np.random.rand(n))

    for i in range(n):
        if rs[i] > r[i]:
            x_nov = x[i] + r[i] * np.cos(fi[i]) * np.sin(t[i])
            y_nov = y[i] + r[i] * np.sin(fi[i]) * np.sin(t[i])
            z_nov = z[i] + r[i] * np.cos(t[i])

            if 0 < x_nov < 1 and 0 < y_nov < 1 and 0 < z_nov < 1:
                xpolozaj.append(x_nov)
                ypolozaj.append(y_nov)
                zpolozaj.append(z_nov)

        else:
            a = fi[i]
            b = t[i]
            pot = rs[i]
            radijsipanje = rs[i]

            # tocka sipanja
            x_nov = x[i] + radijsipanje * np.cos(a) * np.sin(b)
            y_nov = y[i] + radijsipanje * np.sin(a) * np.sin(b)
            z_nov = z[i] + radijsipanje * np.cos(b)

            while (0 < x_nov < 1 and 0 < y_nov < 1 and 0 < z_nov < 1):

                pot_dodatna = -1 * prosta_pot_sipanje * np.log(1 - np.random.rand())
                pot += pot_dodatna

                # nova smer nevtrona, a,b sta kota phi in theta
                a, b = sipanje(a, b)

                x_nov = x_nov + pot_dodatna * np.cos(a) * np.sin(b)
                y_nov = y_nov + pot_dodatna * np.sin(a) * np.sin(b)
                z_nov = z_nov + pot_dodatna * np.cos(b)

                if pot > r[i]:
                    # razdalja od sipanja do absorpcije:
                    r_do_sipanja = pot_dodatna - (pot - r[i])
                    # tocka absorpcije:
                    x_nov = x_nov + r_do_sipanja * np.cos(a) * np.sin(b)
                    y_nov = y_nov + r_do_sipanja * np.sin(a) * np.sin(b)
                    z_nov = z_nov + r_do_sipanja * np.cos(b)

                    if 0 < x_nov < 1 and 0 < y_nov < 1 and 0 < z_nov < 1:
                        xpolozaj.append(x_nov)
                        ypolozaj.append(y_nov)
                        zpolozaj.append(z_nov)
                        break
                else:
                    # razdalja do novega sipanja: pot_dodatna
                    # tocka absorpcije:
                    x_nov = x_nov + pot_dodatna * np.cos(a) * np.sin(b)
                    y_nov = y_nov + pot_dodatna * np.sin(a) * np.sin(b)
                    z_nov = z_nov + pot_dodatna * np.cos(b)

    y = np.zeros(n)
    x = np.random.rand(n)
    z = np.random.rand(n)

    print('\t 2/6')

    r = -1 * prosta_pot * np.log(1 - np.random.rand(n))
    fi = np.random.rand(n) * 2 * np.pi
    t = np.arccos(2 * np.random.rand(n) - 1)

    rs = -1 * prosta_pot_sipanje * np.log(1 - np.random.rand(n))

    for i in range(n):
        if rs[i] > r[i]:
            x_nov = x[i] + r[i] * np.cos(fi[i]) * np.sin(t[i])
            y_nov = y[i] + r[i] * np.sin(fi[i]) * np.sin(t[i])
            z_nov = z[i] + r[i] * np.cos(t[i])

            if 0 < x_nov < 1 and 0 < y_nov < 1 and 0 < z_nov < 1:
                xpolozaj.append(x_nov)
                ypolozaj.append(y_nov)
                zpolozaj.append(z_nov)

        else:
            a = fi[i]
            b = t[i]
            pot = rs[i]
            radijsipanje = rs[i]

            # tocka sipanja
            x_nov = x[i] + radijsipanje * np.cos(a) * np.sin(b)
            y_nov = y[i] + radijsipanje * np.sin(a) * np.sin(b)
            z_nov = z[i] + radijsipanje * np.cos(b)

            while (0 < x_nov < 1 and 0 < y_nov < 1 and 0 < z_nov < 1):

                pot_dodatna = -1 * prosta_pot_sipanje * np.log(1 - np.random.rand())
                pot += pot_dodatna

                # nova smer nevtrona, a,b sta kota phi in theta
                a, b = sipanje(a, b)

                x_nov = x_nov + pot_dodatna * np.cos(a) * np.sin(b)
                y_nov = y_nov + pot_dodatna * np.sin(a) * np.sin(b)
                z_nov = z_nov + pot_dodatna * np.cos(b)

                if pot > r[i]:
                    # razdalja od sipanja do absorpcije:
                    r_do_sipanja = pot_dodatna - (pot - r[i])
                    # tocka absorpcije:
                    x_nov = x_nov + r_do_sipanja * np.cos(a) * np.sin(b)
                    y_nov = y_nov + r_do_sipanja * np.sin(a) * np.sin(b)
                    z_nov = z_nov + r_do_sipanja * np.cos(b)

                    if 0 < x_nov < 1 and 0 < y_nov < 1 and 0 < z_nov < 1:
                        xpolozaj.append(x_nov)
                        ypolozaj.append(y_nov)
                        zpolozaj.append(z_nov)
                        break
                else:
                    # razdalja do novega sipanja: pot_dodatna
                    # tocka absorpcije:
                    x_nov = x_nov + pot_dodatna * np.cos(a) * np.sin(b)
                    y_nov = y_nov + pot_dodatna * np.sin(a) * np.sin(b)
                    z_nov = z_nov + pot_dodatna * np.cos(b)

    print('\t 3/6')

    y = np.ones(n)
    x = np.random.rand(n)
    z = np.random.rand(n)

    r = -1 * prosta_pot * np.log(1 - np.random.rand(n))
    fi = np.random.rand(n) * 2 * np.pi
    t = np.arccos(2 * np.random.rand(n) - 1)

    rs = -1 * prosta_pot_sipanje * np.log(1 - np.random.rand(n))

    for i in range(n):
        if rs[i] > r[i]:
            x_nov = x[i] + r[i] * np.cos(fi[i]) * np.sin(t[i])
            y_nov = y[i] + r[i] * np.sin(fi[i]) * np.sin(t[i])
            z_nov = z[i] + r[i] * np.cos(t[i])

            if 0 < x_nov < 1 and 0 < y_nov < 1 and 0 < z_nov < 1:
                xpolozaj.append(x_nov)
                ypolozaj.append(y_nov)
                zpolozaj.append(z_nov)

        else:
            a = fi[i]
            b = t[i]
            pot = rs[i]
            radijsipanje = rs[i]

            # tocka sipanja
            x_nov = x[i] + radijsipanje * np.cos(a) * np.sin(b)
            y_nov = y[i] + radijsipanje * np.sin(a) * np.sin(b)
            z_nov = z[i] + radijsipanje * np.cos(b)

            while (0 < x_nov < 1 and 0 < y_nov < 1 and 0 < z_nov < 1):

                pot_dodatna = -1 * prosta_pot_sipanje * np.log(1 - np.random.rand())
                pot += pot_dodatna

                # nova smer nevtrona, a,b sta kota phi in theta
                a, b = sipanje(a, b)

                x_nov = x_nov + pot_dodatna * np.cos(a) * np.sin(b)
                y_nov = y_nov + pot_dodatna * np.sin(a) * np.sin(b)
                z_nov = z_nov + pot_dodatna * np.cos(b)

                if pot > r[i]:
                    # razdalja od sipanja do absorpcije:
                    r_do_sipanja = pot_dodatna - (pot - r[i])
                    # tocka absorpcije:
                    x_nov = x_nov + r_do_sipanja * np.cos(a) * np.sin(b)
                    y_nov = y_nov + r_do_sipanja * np.sin(a) * np.sin(b)
                    z_nov = z_nov + r_do_sipanja * np.cos(b)

                    if 0 < x_nov < 1 and 0 < y_nov < 1 and 0 < z_nov < 1:
                        xpolozaj.append(x_nov)
                        ypolozaj.append(y_nov)
                        zpolozaj.append(z_nov)
                        break
                else:
                    # razdalja do novega sipanja: pot_dodatna
                    # tocka absorpcije:
                    x_nov = x_nov + pot_dodatna * np.cos(a) * np.sin(b)
                    y_nov = y_nov + pot_dodatna * np.sin(a) * np.sin(b)
                    z_nov = z_nov + pot_dodatna * np.cos(b)

    z = np.zeros(n)
    y = np.random.rand(n)
    x = np.random.rand(n)

    print('\t 4/6')

    r = -1 * prosta_pot * np.log(1 - np.random.rand(n))
    fi = np.random.rand(n) * 2 * np.pi
    t = np.arccos(2 * np.random.rand(n) - 1)

    rs = -1 * prosta_pot_sipanje * np.log(1 - np.random.rand(n))

    for i in range(n):
        if rs[i] > r[i]:
            x_nov = x[i] + r[i] * np.cos(fi[i]) * np.sin(t[i])
            y_nov = y[i] + r[i] * np.sin(fi[i]) * np.sin(t[i])
            z_nov = z[i] + r[i] * np.cos(t[i])

            if 0 < x_nov < 1 and 0 < y_nov < 1 and 0 < z_nov < 1:
                xpolozaj.append(x_nov)
                ypolozaj.append(y_nov)
                zpolozaj.append(z_nov)

        else:
            a = fi[i]
            b = t[i]
            pot = rs[i]
            radijsipanje = rs[i]

            # tocka sipanja
            x_nov = x[i] + radijsipanje * np.cos(a) * np.sin(b)
            y_nov = y[i] + radijsipanje * np.sin(a) * np.sin(b)
            z_nov = z[i] + radijsipanje * np.cos(b)

            while (0 < x_nov < 1 and 0 < y_nov < 1 and 0 < z_nov < 1):

                pot_dodatna = -1 * prosta_pot_sipanje * np.log(1 - np.random.rand())
                pot += pot_dodatna

                # nova smer nevtrona, a,b sta kota phi in theta
                a, b = sipanje(a, b)

                x_nov = x_nov + pot_dodatna * np.cos(a) * np.sin(b)
                y_nov = y_nov + pot_dodatna * np.sin(a) * np.sin(b)
                z_nov = z_nov + pot_dodatna * np.cos(b)

                if pot > r[i]:
                    # razdalja od sipanja do absorpcije:
                    r_do_sipanja = pot_dodatna - (pot - r[i])
                    # tocka absorpcije:
                    x_nov = x_nov + r_do_sipanja * np.cos(a) * np.sin(b)
                    y_nov = y_nov + r_do_sipanja * np.sin(a) * np.sin(b)
                    z_nov = z_nov + r_do_sipanja * np.cos(b)

                    if 0 < x_nov < 1 and 0 < y_nov < 1 and 0 < z_nov < 1:
                        xpolozaj.append(x_nov)
                        ypolozaj.append(y_nov)
                        zpolozaj.append(z_nov)
                        break
                else:
                    # razdalja do novega sipanja: pot_dodatna
                    # tocka absorpcije:
                    x_nov = x_nov + pot_dodatna * np.cos(a) * np.sin(b)
                    y_nov = y_nov + pot_dodatna * np.sin(a) * np.sin(b)
                    z_nov = z_nov + pot_dodatna * np.cos(b)

    z= np.ones(n)
    y = np.random.rand(n)
    x = np.random.rand(n)

    print('\t 5/6')

    r = -1 * prosta_pot * np.log(1 - np.random.rand(n))
    fi = np.random.rand(n) * 2 * np.pi
    t = np.arccos(2 * np.random.rand(n) - 1)

    rs = -1 * prosta_pot_sipanje * np.log(1 - np.random.rand(n))

    for i in range(n):
        if rs[i] > r[i]:
            x_nov = x[i] + r[i] * np.cos(fi[i]) * np.sin(t[i])
            y_nov = y[i] + r[i] * np.sin(fi[i]) * np.sin(t[i])
            z_nov = z[i] + r[i] * np.cos(t[i])

            if 0 < x_nov < 1 and 0 < y_nov < 1 and 0 < z_nov < 1:
                xpolozaj.append(x_nov)
                ypolozaj.append(y_nov)
                zpolozaj.append(z_nov)

        else:
            a = fi[i]
            b = t[i]
            pot = rs[i]
            radijsipanje = rs[i]

            # tocka sipanja
            x_nov = x[i] + radijsipanje * np.cos(a) * np.sin(b)
            y_nov = y[i] + radijsipanje * np.sin(a) * np.sin(b)
            z_nov = z[i] + radijsipanje * np.cos(b)

            while (0 < x_nov < 1 and 0 < y_nov < 1 and 0 < z_nov < 1):

                pot_dodatna = -1 * prosta_pot_sipanje * np.log(1 - np.random.rand())
                pot += pot_dodatna

                # nova smer nevtrona, a,b sta kota phi in theta
                a, b = sipanje(a, b)

                x_nov = x_nov + pot_dodatna * np.cos(a) * np.sin(b)
                y_nov = y_nov + pot_dodatna * np.sin(a) * np.sin(b)
                z_nov = z_nov + pot_dodatna * np.cos(b)

                if pot > r[i]:
                    # razdalja od sipanja do absorpcije:
                    r_do_sipanja = pot_dodatna - (pot - r[i])
                    # tocka absorpcije:
                    x_nov = x_nov + r_do_sipanja * np.cos(a) * np.sin(b)
                    y_nov = y_nov + r_do_sipanja * np.sin(a) * np.sin(b)
                    z_nov = z_nov + r_do_sipanja * np.cos(b)

                    if 0 < x_nov < 1 and 0 < y_nov < 1 and 0 < z_nov < 1:
                        xpolozaj.append(x_nov)
                        ypolozaj.append(y_nov)
                        zpolozaj.append(z_nov)
                        break
                else:
                    # razdalja do novega sipanja: pot_dodatna
                    # tocka absorpcije:
                    x_nov = x_nov + pot_dodatna * np.cos(a) * np.sin(b)
                    y_nov = y_nov + pot_dodatna * np.sin(a) * np.sin(b)
                    z_nov = z_nov + pot_dodatna * np.cos(b)

    return xpolozaj,ypolozaj,zpolozaj


def delez_absorbiranih(razdalja_sipanje):
    n=10**5
    delez_abs=[]
    k=0

    absorpciija=[0.01,0.05,0.1,0.25,0.5,0.75,1,2,5,10,50,100]
    for i in absorpciija:
        a,b,c=polozaj_abs_nevtronov(i,razdalja_sipanje,n)
        delez_abs.append(len(a)/(3*n))
        print(k,'/',len(absorpciija))
        k+=1
    return absorpciija,delez_abs






print('zakljucil streljanje nevtronov')

# ###plot 2d histograma porazdelitev absorpcije nevtrona v plasti
# prosta_pot=1
# pot_sipanje=0.1
# n=10**6
# x,y,z=polozaj_abs_nevtronov(prosta_pot,pot_sipanje,n)
# a,b=rezina(0.5,0.1,x,y,z)
#
# print('zakljucil rezino')
# naslov='porazdelitev_lambda_s_'+str(pot_sipanje).replace('.','_')+'lamda_'+str(prosta_pot).replace('.','_')+'n_'+str(n)+'.png'
# # ,norm = mpl.colors.LogNorm()
# plt.hist2d(a,b, bins=50)
# plt.title('porazdelitev absorpcije nevtronov v preseku kocke\n'+r'$\lambda =$ '+str(prosta_pot)+ r' $\lambda_S=$ '+str(pot_sipanje))
# cb=plt.colorbar(format='%d')
# tick_locator = ticker.MaxNLocator(nbins=5)
# cb.locator = tick_locator
# cb.update_ticks()
# cb.set_label('število absorbiranih nevtronov')
# plt.savefig(naslov)
# plt.show()

a,b=delez_absorbiranih(99999)
c,d=delez_absorbiranih(0.1)
e,f=delez_absorbiranih(0.5)
g,h=delez_absorbiranih(2)

plt.plot(a,b,'o-',label='brez sipanja')
plt.plot(c,d,'o-',label=r'$\lambda_S=0.1$')
plt.plot(e,f,'o-',label=r'$\lambda_S=0.5$')
plt.plot(g,h,'o-',label=r'$\lambda_S=2$')
plt.xscale('log')
plt.xlabel('povprečna prosta pot (v enotah velikosti kocke)')
plt.ylabel('delež absorbiranih nevtronov')
plt.legend()
plt.grid()
plt.savefig('delez_absorbiranih_nevtronov.png')
plt.show()







###3d narisana kocka
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(x0,y0,z0)
# plt.show()