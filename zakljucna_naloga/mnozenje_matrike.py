# from sympy import *
#
# x = symbols('x')
# y = symbols('y')
#
#
# Rx = Matrix([[1, 0,0], [0,cos(x),-sin(x)],[0,sin(x),cos(x)]])
# Ry = Matrix([[cos(y),-sin(y),0],[sin(y),cos(y),0],[0,0,1]])
#
# R=Rx*Ry
#
#
#
# print(simplify(R))




import numpy as np

def kota_sipanje(fi,theta):


    #vektor vpadnega nevtrona
    vpadni_vektor=np.array([np.cos(fi)*np.sin(theta),np.sin(fi)*np.sin(theta),np.cos(theta)])

    #kota x in y kolikot je potrebno zasukati:
    y=fi+np.pi
    x=-np.pi/2+theta

    #rotacijska matrika:
    matrika=np.array([[np.cos(y),-np.sin(y),0],[np.cos(x)*np.sin(y),np.cos(x)*np.cos(y),-np.sin(x)],[np.sin(x)*np.sin(y),np.sin(x)*np.cos(y),np.cos(x)]])

    #random tocka na preseku jedra:
    alfa = np.random.rand() * np.pi * 2
    radij = np.random.rand() ** (0.5)
    #transformacija tocke iz preseka na povrsino sfere:
    fi1 = np.arctan((radij * np.sin(alfa)) / np.sqrt(1 - radij ** 2))
    theta1 = np.arccos(radij * np.cos(alfa))

    #smer trka:
    vector_zacetni=np.array([np.cos(fi1)*np.sin(theta1),np.sin(fi1)*np.sin(theta1),np.cos(theta1)])

    #tocka trka na sferi jedra:

    tocka_trka=np.dot(matrika,vector_zacetni)

    #projekcij na vektor trka:

    proj=tocka_trka[0]*vpadni_vektor[0]+tocka_trka[1]*vpadni_vektor[1]+tocka_trka[1]*vpadni_vektor[2]
    print(proj)

    #smer odbitega:

    odbiti=vpadni_vektor+2*proj*vector_zacetni

    razdalja=np.sqrt(odbiti[0]**2+odbiti[1]**2+odbiti[2]**2)

    #return: np.arctan(y/x) , np.arccos(z/(normalizacija))
    return np.arctan(odbiti[1]/odbiti[0]) , np.arccos(odbiti[2]/razdalja)
