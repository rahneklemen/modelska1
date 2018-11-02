#v poročilo: ne gre za negativne C, in tudi za c=0, za primer C=0.1, zelo podobno prvi nalogi

import numpy as np
import matplotlib.pyplot as plt

def v(t,C,v0):
    l0=1
    t0=1
    korC=np.sqrt(C)
    alfa=korC*t0
    
    lamda=(l0-v0/korC*np.tanh(alfa))/(t0/2/C-np.tanh(alfa)/2/C/korC)
    C2=v0-lamda/2/C
    C1=-C2*np.tanh(alfa)
    return C1*np.sinh(korC*t)+C2*np.cosh(korC*t)+lamda/2/C


p=1000  #vbistvu C
t = np.arange(0, 1, 0.01);



nicla,=plt.plot(t,v(t,p,0))
prva,= plt.plot(t, v(t,p,0.5))
prva_druga,= plt.plot(t,v(t,p,1))
druga,= plt.plot(t, v(t,p,2))
tretja, = plt.plot(t, v(t,p,3))
cetrta, = plt.plot(t, v(t,p,5))


plt.legend([nicla,prva,prva_druga, druga,tretja,cetrta], ['v$_{0}=0$','v$_{0}=0.5$','v$_{0}=1$', 'v$_{0}=2$','v$_{0}=3$','v$_{0}=5$'],title='začetna hitrost')
plt.grid()
naslov='konstanta A='+str(p)
plt.title(naslov)
naslov='konstanta'+str(p)+'.png'
plt.xlabel('čas')
plt.ylabel('hitrost')
plt.savefig(naslov)
plt.show()