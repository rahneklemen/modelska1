def v(t,v_0):
    l=1
    t_0=1
    lamda=6/(t_0**3)*(l-v_0*t_0)
    
    return -lamda/4*t**2+lamda/2*t_0*t+v_0

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 1, 0.01);



nicla,=plt.plot(t,v(t,0))
prva,= plt.plot(t, v(t,0.1))
prva_druga,= plt.plot(t,v(t,0.5))
druga,= plt.plot(t, v(t,1))
tretja, = plt.plot(t, v(t,2))
cetrta, = plt.plot(t, v(t,5))


plt.legend([nicla,prva,prva_druga, druga,tretja,cetrta], ['v$_{0}=0$','v$_{0}=0.1$','v$_{0}=0.5$', 'v$_{0}=1$','v$_{0}=2$','v$_{0}=5$'],title='začetna hitrost')
plt.grid()

plt.xlabel('čas')
plt.ylabel('hitrost')

#plt.savefig('prva.png')
plt.show()