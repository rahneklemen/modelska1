import random
import matplotlib.pyplot as plt


def lcg(n,seed=random.randint(0,100)):
    '''

    generator random stevik na podlagi linear congruential generator:
    x_i+1 = (a*x_i + c )mod_m

    a = 1140671485
    c = 128201163
    m = 2**24


    Returns
    -------
    seznam - array n random stevilk med 0 in 1
    Parameters
    ----------
    n - stevilo generiranih random stevk
    seed - seme-default value:random.randint(0,100)

    Returns
    -------
    seznam - array n random stevilk med 0 in 1

    '''
    a = 1103515245
    c = 123454
    m = 2**32

    x0=seed
    seznam=[]

    for i in range(n):
        x0=(a*x0+c) % m
        seznam.append(x0/m)
    return seznam
#
#
#
# list=lcg(100)
# print(max(list))
# print(min(list))
#
# plt.hist(list,bins=10)
# plt.show()
