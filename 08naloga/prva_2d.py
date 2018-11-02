import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import time
from mpl_toolkits.mplot3d import Axes3D


def chi(podatki,n):
    vsota=0
    pricakovana=n/(len(podatki)*len(podatki[0]))
    print(pricakovana)
    for i in range(len(podatki)):
        for j in range(len(podatki[i])):
            vsota+=(podatki[i][j]-pricakovana)**2/pricakovana
    return vsota


n=100000
n_bins=10

# [d,h]=porazdelitev_kolmogor_hi(n,n_bins,iteracij)
x=np.random.random(n)
y=np.random.random(n)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

hist, xedges, yedges = np.histogram2d(x, y, bins=n_bins)

elements = (len(xedges) - 1) * (len(yedges) - 1)
xpos, ypos = np.meshgrid(xedges[:-1], yedges[:-1])

xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros(elements)
dx = 1/n_bins * np.ones_like(zpos)
dy = dx.copy()
dz = hist.flatten()



ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')
# blue_proxy = plt.Rectangle((0, 0), 1, 1, fc="b")
# ax.bar3d(xpos[8:], ypos[8:], zpos[8:], dx, dy, dz, color='r', zsort='average')
# red_proxy = plt.Rectangle((0, 0), 1, 1, fc="r")
# ax.legend([blue_proxy,red_proxy],['cars','bikes'])

plt.show()

print(chi(hist,n))
