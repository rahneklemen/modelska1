

import numpy as np

import matplotlib.pyplot as plt



def v(t,p,v0):
    a=v0+(4*p-1)/(2*p)*(1-v0)*(1-np.power(1-t,(2*p/(2*p-1))))
    return a


p=10
t = np.arange(0, 1, 0.01);



nicla,=plt.plot(t,v(t,p,0))
prva,= plt.plot(t, v(t,p,0.5))
prva_druga,= plt.plot(t,v(t,p,1))
druga,= plt.plot(t, v(t,p,2))
tretja, = plt.plot(t, v(t,p,3))
cetrta, = plt.plot(t, v(t,p,5))

naslov='p='+str(p)
plt.legend([nicla,prva,prva_druga, druga,tretja,cetrta], ['v$_{0}=0$','v$_{0}=0.5$','v$_{0}=1$', 'v$_{0}=2$','v$_{0}=3$','v$_{0}=5$'],title='začetna hitrost')
plt.grid()
plt.title(naslov)



plt.xlabel('čas')
plt.ylabel('hitrost')
naslov='druga'+naslov+'.png'
plt.savefig(naslov)
plt.show()