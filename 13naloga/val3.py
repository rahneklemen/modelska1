import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from nitime import algorithms as alg



def aproksimacija(podatki, seznam_koeficientov, iteracij):
    for i in range(iteracij):
        vsota = 0
        for j in range(len(seznam_koeficientov)):
            vsota += podatki[-j - 1] * seznam_koeficientov[j]
        podatki.append(vsota)
    return podatki


x = []

f = open('val3.dat', 'r', encoding='utf-8')
data_file = f.readlines()

for vrsta in data_file:
    x.append(float(vrsta))

f.close()

#
# x32=[]
# x64=[]
# x128=[]
# x256=[]
# for i in range(len(x)):
#     if i%16==0:
#         x32.append(x[i])
#     if i%8==0:
#         x64.append(x[i])
#     if i%4==0:
#         x128.append(x[i])
#     if i%2==0:
#         x256.append(x[i])
#
#
#
# print(len(x),len(x32),len(x64),len(x128),len(x256))
#
#
# dolzina = 20
# ii = 100
#
# a, b = alg.AR_est_YW(np.array(x), dolzina)
#
#
#
#
#
#
#
#
# y3 = aproksimacija(x[:250], a, ii)
#
# plt.plot(x, label='meritev')
#
# plt.plot(y3, label='napoved N=' + str(dolzina))
# plt.legend()
# plt.grid()
# plt.show()


#odvisnost od stevila polov
#
# dolzina=10
# a,b=alg.AR_est_YW(np.array(x),dolzina)
# f10=alg.autoregressive.AR_psd(a,b)
#
# dolzina=20
# a,b=alg.AR_est_YW(np.array(x),dolzina)
# f20=alg.autoregressive.AR_psd(a,b)
#
# dolzina=50
# a,b=alg.AR_est_YW(np.array(x),dolzina)
# f50=alg.autoregressive.AR_psd(a,b)
#
# dolzina=100
# a,b=alg.AR_est_YW(np.array(x),dolzina)
# f100=alg.autoregressive.AR_psd(a,b)
#
# dolzina=200
# a,b=alg.AR_est_YW(np.array(x),dolzina)
# f200=alg.autoregressive.AR_psd(a,b)
#
# #fft:
# fft_koncentracija=abs(np.fft.fft(x))**2
# fft_koncentracija=fft_koncentracija/sum(fft_koncentracija)
# f_cas=np.arange(len(fft_koncentracija))/len(fft_koncentracija)

# plt.plot(f_cas,fft_koncentracija,label='FFT')
# plt.plot(f10[0]/2/np.pi,f10[1]/sum(f10[1]),label='10')
# plt.plot(f20[0]/2/np.pi,f20[1]/sum(f20[1]),label='20')
# plt.plot(f50[0]/2/np.pi,f50[1]/sum(f50[1]),label='50')
# plt.plot(f100[0]/2/np.pi,f100[1]/sum(f100[1]),label='100')
# plt.plot(f200[0]/2/np.pi,f200[1]/sum(f200[1]),label='200')
# plt.legend(title='# koeficientov')
# plt.yscale('log')
# plt.xlabel('frekvenca')
# plt.ylabel('gostota moči')
# plt.xlim(xmax=1/2)
# plt.grid()
# plt.savefig('val3_primerjava_fft.png')
# plt.show()


# plt.plot(f_cas,fft_koncentracija,label='FFT')
# # plt.plot(f10[0]/2/np.pi,f10[1]/sum(f10[1]),label='10')
# plt.plot(f20[0]/2/np.pi,f20[1]/sum(f20[1]),label='20')
# plt.plot(f50[0]/2/np.pi,f50[1]/sum(f50[1]),label='50')
# # plt.plot(f100[0]/2/np.pi,f100[1]/sum(f100[1]),label='100')
# plt.plot(f200[0]/2/np.pi,f200[1]/sum(f200[1]),label='200')
# plt.legend(title='# koeficientov')
# plt.yscale('log')
# plt.xlabel('frekvenca')
# plt.ylabel('gostota moči')
# plt.xlim(xmax=1/2)
# plt.grid()
# plt.savefig('val3_primerjava_koef.png')
# plt.show()

#napoved
polovica=int(len(x)/2)

podatki=x[:polovica]
st_koef=20


a,b=alg.AR_est_YW(np.array(podatki),st_koef)


# y2=aproksimacija(x,a,ii)
y3=aproksimacija(podatki,a,polovica)


plt.plot(x,label='meritev')
plt.plot(y3,label='napoved N='+str(st_koef))
plt.legend(title='val3.dat')
plt.grid()
plt.axvline(x=polovica,color='r')
plt.xlim(xmax=len(y3))
plt.savefig('napoved_val3.png')
plt.show()

