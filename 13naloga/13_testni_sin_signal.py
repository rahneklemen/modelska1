import numpy as np
import matplotlib.pyplot as plt
from nitime import algorithms as alg

def aproksimacija(podatki,seznam_koeficientov,iteracij):
    for i in range(iteracij):
        vsota=0
        for j in range(len(seznam_koeficientov)):
            vsota+=podatki[-j-1]*seznam_koeficientov[j]
        # print(vsota)
        # print(type(vsota))
        podatki.append(vsota)
    return podatki


N=512

x=np.arange(0,2*np.pi,2*np.pi/(N))
y=np.sin(110*x)+np.sin(150*x)+np.sin(180*x)

#
# print(len(x))
#
# st_polov=30
#
#
# y32=y[:32]
# y64=y[:64]
# y128=y[:128]
# y256=y[:256]
#
#
# plt.plot(y)
# plt.plot(y256)
# plt.show()
#
# ##gostota:y
# a, b = alg.AR_est_YW(np.array(y), st_polov)
# spekter512 = alg.autoregressive.AR_psd(a, b)
#
# ##gostota:y32
# a, b = alg.AR_est_YW(np.array(y32), st_polov)
# spekter32 = alg.autoregressive.AR_psd(a, b)
#
# ##gostota:y64
# a, b = alg.AR_est_YW(np.array(y64), st_polov)
# spekter64 = alg.autoregressive.AR_psd(a, b)
#
# ##gostota:y128
# a, b = alg.AR_est_YW(np.array(y128), st_polov)
# spekter128 = alg.autoregressive.AR_psd(a, b)
#
# ##gostota:y256
# a, b = alg.AR_est_YW(np.array(y256), st_polov)
# spekter256 = alg.autoregressive.AR_psd(a, b)
#
#
# x_os=[i/len(spekter32)/2 for i in range(len(spekter32))]
#
# plt.plot(spekter32[0],spekter32[1],label='32')
# plt.plot(spekter64[0],spekter64[1],label='64')
# plt.plot(spekter128[0],spekter128[1],label='128')
# plt.plot(spekter256[0],spekter256[1],label='256')
# plt.plot(spekter512[0],spekter512[1],label='512')
# plt.xlabel('frekvenca')
# plt.ylabel('spektralna gostota')
# plt.yscale('log')
# plt.legend(title='število točk')
# plt.grid()
# plt.savefig('sinusni_frekvenca_osnovna.png')
# plt.show()
#
#

# plt.plot(spekter32[0],spekter32[1],label='32')
# plt.plot(spekter64[0],spekter64[1],label='64')
# plt.plot(spekter128[0],spekter128[1],label='128')
# plt.plot(spekter256[0],spekter256[1],label='256')
# plt.plot(spekter512[0],spekter512[1],label='512')
# plt.legend(title='število točk')
# plt.grid()
# plt.show()

polovica=int(len(y)/2)

podatki=y[:polovica].tolist()
st_koef=20


a,b=alg.AR_est_YW(np.array(podatki),st_koef)


# y2=aproksimacija(x,a,ii)
y3=aproksimacija(podatki,a,polovica)


plt.plot(y,label='meritev')
plt.plot(y3,label='napoved N='+str(st_koef))
plt.legend(title='testni signal')
plt.grid()
plt.axvline(x=polovica,color='r')
plt.xlim(xmax=len(y3))
plt.savefig('napoved_testni_sin.png')
plt.show()

