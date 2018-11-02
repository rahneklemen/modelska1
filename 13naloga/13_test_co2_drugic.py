import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from nitime import algorithms as alg


def aproksimacija(podatki,seznam_koeficientov,iteracij):
    for i in range(iteracij):
        vsota=0
        for j in range(len(seznam_koeficientov)):
            vsota+=podatki[-j-1]*seznam_koeficientov[j]
        podatki.append(vsota)
    return podatki

def nicle(seznam_koeficientov):
    koeficienti=[]
    for i in range(len(seznam_koeficientov)):
        koeficienti.append(-1*seznam_koeficientov[-i-1])
    koeficienti.append(1)
    nicle=np.roots(koeficienti)

    print(nicle)
    realno=[]
    compleks=[]
    for i in nicle:
        realno.append(i.real)
        compleks.append(i.imag)
    return realno,compleks

def transform_nicle(seznam_x,seznam_y):
    x_koo=seznam_x
    y_koo=seznam_y

    j=0

    for i in range(len(seznam_x)):
        dolzina=(seznam_x[i]**2+seznam_y[i]**2)**0.5
        kot=np.arctan(seznam_y[i]/seznam_x[i])
        # print('kot1',kot)
        if dolzina>1:
            if seznam_x[i]<0 and seznam_y[i]>=0:
                kot=kot+np.pi
            if seznam_x[i]<0 and seznam_y[i]<0:
                kot=kot-np.pi
            j+=1
            if int(dolzina)%2==1:
                razdalja=1-dolzina%1
            else:
                razdalja = dolzina % 1
            print(razdalja,dolzina)
            x_koo[i]=razdalja*np.cos(kot)
            y_koo[i]=razdalja*np.sin(kot)
        else:
            x_koo[i]=seznam_x[i]
            y_koo[i]=seznam_y[i]
    print(len(seznam_y),j)
    return x_koo,y_koo



cas=[]
y=[]

f = open('co2.dat', 'r',encoding='utf-8')
data_file=f.readlines()
i=0
for vrsta in data_file:
    if i>18:
        for j in range(len(vrsta)):
            if vrsta[j]==' ':
                break
        meritev=float(vrsta[j+1:])
        if meritev!=-99.99:
            cas.append(float(vrsta[:j]))
            y.append(float(vrsta[j+1:]))
    i+=1


# plt.plot(cas,y)
# plt.grid()
#
# plt.xlabel('leto')
# plt.ylabel(r'koncentracija $CO_2$ [ppm]')
# plt.savefig('co2_koncentracija.png')
# plt.show()




## odstet linearen fit
naklon,zacetna_vrednost,ena,dva,tri=stats.linregress(cas,y)
print(naklon,zacetna_vrednost)

koncentracija=[]
for i in range(len(y)):
    koncentracija.append(y[i]-naklon*cas[i]-zacetna_vrednost)
prava=koncentracija




dolzina=16
ii=400

#
# a,b=alg.AR_est_YW(np.array(koncentracija),dolzina)
# print('"prava:"',a)
#
#
#
#
# a1,a2=nicle(a)
#
# y2=aproksimacija(koncentracija[:250],a1,ii)
# y3=aproksimacija(koncentracija[:250],a,ii)
#
# plt.plot(koncentracija,label='meritev')
# plt.plot(y3,label='napoved N='+str(dolzina))
# plt.grid()
# plt.xlim(xmax=600)
# plt.show()
#
# f_konc=alg.autoregressive.AR_psd(a,b)
#
# fft_koncentracija=abs(np.fft.fft(koncentracija))**2
# fft_koncentracija=fft_koncentracija/sum(fft_koncentracija)
# f_cas=np.arange(len(fft_koncentracija))/len(fft_koncentracija)







# plt.plot(f_cas,fft_koncentracija,label='FFT')
# plt.plot(f_konc[0]/2/np.pi,f_konc[1]/sum(f_konc[1]),label='MEM-N='+str(dolzina))
# plt.legend()
# # plt.yscale('log')
# plt.ylim(ymin=10e-10)
# plt.xlim(xmax=0.5)
# plt.grid()
# plt.savefig('co2_mem_frekvence.png')
# plt.show()
#
# plt.plot(f_cas,fft_koncentracija,label='FFT')
# plt.plot(f_konc[0]/2/np.pi,f_konc[1]/sum(f_konc[1]),label='MEM-N='+str(dolzina))
# plt.legend()
# plt.yscale('log')
# plt.ylim(ymin=10e-10)
# plt.xlim(xmax=0.5)
# plt.grid()
# plt.savefig('co2_mem_frekvence_log.png')
# plt.show()
#
#
# transform_nicle(a1,a2)
#
# plt.plot(a1,a2,'or')
# #plt.plot(a3,a4,'r')
# plt.grid()
# plt.title('položaji polov')
# plt.xlabel('Re{z}')
# plt.ylabel('Im{z}')
#
# x = np.linspace(-1.0, 1.0, 100)
# y = np.linspace(-1.0, 1.0, 100)
# X, Y = np.meshgrid(x,y)
# F = X**2 + Y**2 - 1
# plt.contour(X,Y,F,[0])
# plt.show()



#odvisnost od stevila polov

# dolzina=10
# a,b=alg.AR_est_YW(np.array(prava),dolzina)
# f10=alg.autoregressive.AR_psd(a,b)
#
# dolzina=20
# a,b=alg.AR_est_YW(np.array(prava),dolzina)
# f20=alg.autoregressive.AR_psd(a,b)
# a1,a2=nicle(a)
#
#
# dolzina=50
# a,b=alg.AR_est_YW(np.array(prava),dolzina)
# f50=alg.autoregressive.AR_psd(a,b)
#
# dolzina=100
# a,b=alg.AR_est_YW(np.array(prava),dolzina)
# f100=alg.autoregressive.AR_psd(a,b)
#
# dolzina=200
# a,b=alg.AR_est_YW(np.array(prava),dolzina)
# f200=alg.autoregressive.AR_psd(a,b)
#
# #fft:
# fft_koncentracija=abs(np.fft.fft(prava))**2
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
# plt.savefig('co2_primerjava_fft.png')
# plt.show()



# # plt.plot(f10[0]/2/np.pi,f10[1]/sum(f10[1]),label='10')
# plt.plot(f20[0]/2/np.pi,f20[1]/sum(f20[1]),label='20')
# plt.plot(f50[0]/2/np.pi,f50[1]/sum(f50[1]),label='50')
# # plt.plot(f100[0]/2/np.pi,f100[1]/sum(f100[1]),label='100')
# plt.plot(f200[0]/2/np.pi,f200[1]/sum(f200[1]),label='200')
# plt.plot(f_cas,fft_koncentracija,label='FFT')
# plt.legend(title='# koeficientov')
# plt.yscale('log')
# plt.xlabel('frekvenca')
# plt.ylabel('gostota moči')
# plt.xlim(xmax=1/2)
# plt.ylim(ymin=10**-8)
# plt.grid()
# plt.savefig('co2_primerjava_koef.png')
# plt.show()



#polozaj polov
# transform_nicle(a1,a2)
#
# plt.plot(a1,a2,'or')
# plt.grid()
# plt.title('položaji polov, #polov=20')
# plt.xlabel('Re{z}')
# plt.ylabel('Im{z}')
# x = np.linspace(-1.0, 1.0, 100)
# y = np.linspace(-1.0, 1.0, 100)
# X, Y = np.meshgrid(x,y)
# F = X**2 + Y**2 - 1
# plt.contour(X,Y,F,[0])
# plt.savefig('polozaji_polov.png')
# plt.show()


polovica=int(len(koncentracija)/2)

podatki=koncentracija[:polovica]
st_koef=20


a,b=alg.AR_est_YW(np.array(podatki),st_koef)


# y2=aproksimacija(x,a,ii)
y3=aproksimacija(podatki,a,polovica)


plt.plot(koncentracija,label='meritev')
plt.plot(y3,label='napoved N='+str(st_koef))
plt.legend(title=r'$C0_2$')
plt.grid()
plt.savefig('napoved_co2.png')
plt.show()
