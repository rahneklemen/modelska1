import numpy as np
import matplotlib.pyplot as plt


#np.random.random je na osnovi mersene twister

def funkcija_histogram(seznam, stevilo_binov):
    hist=np.zeros(stevilo_binov)
    normalizacija=len(seznam)
    for stevilka in seznam:
        indeks=int(stevilka*stevilo_binov)
        hist[indeks]+=1
    hist=hist/normalizacija
    return hist

def hi_kvadrat_stevka(moja_poraz,prava_poraz):
    vsota=0;
    normalizacija=sum(moja_poraz)*len(moja_poraz)

    for i in range(len(moja_poraz)):
        vsota+=(abs(moja_poraz[i]-prava_poraz[i])**2)/prava_poraz[i]

    vsota=vsota*normalizacija
    #print(vsota)
    return vsota


def kolmogor_d(moja_porazdelitev,prava_porazdelitev):
    d=0;

    for i in range(len(moja_porazdelitev)):
        trenutni_d=abs(moja_porazdelitev[i]-prava_porazdelitev[i])
        #print(d)
        if trenutni_d>d:
            d=trenutni_d
    return d

def porazdelitve(stevilo_porazdelitev,n,predalcki):
    hi=[]
    d=[]


    for i in range(stevilo_porazdelitev):
        stevilke=np.random.random(n)

        histogram_stevke=funkcija_histogram(stevilke,predalcki)
        histogram_stevke_pravi=np.ones(predalcki)/predalcki

        histogram_kolm_moj=np.cumsum(histogram_stevke)
        histogram_kolm_pravi=np.ones(predalcki)
        for j in range(predalcki):
            histogram_kolm_pravi[j]=(j)/(predalcki-1)

        # plt.plot(histogram_stevke_pravi,'o')
        # plt.plot(histogram_stevke)
        # plt.show()

        d.append(kolmogor_d(histogram_kolm_moj,histogram_kolm_pravi))
        hi.append(hi_kvadrat_stevka(histogram_stevke,histogram_stevke_pravi))
    return hi,d

def samo_ena_iter(n,predalcki):

    stevilke=np.random.random(n)
    histogram_stevke=funkcija_histogram(stevilke,predalcki)

    histogram_kolm_moj=np.cumsum(histogram_stevke)
    histogram_stevke_pravi=np.ones(predalcki)/predalcki

    histogram_kolm_pravi=np.ones(predalcki)


    print(histogram_kolm_moj)
    for j in range(predalcki):
        histogram_kolm_pravi[j]=histogram_kolm_pravi[j]*(j)/(predalcki-1)
    plt.plot(histogram_kolm_moj)
    plt.plot(histogram_kolm_pravi)
    plt.show()

    plt.plot(histogram_stevke_pravi)
    plt.plot(histogram_stevke)
    plt.show()

    D,HI = kolmogor_d(histogram_kolm_moj,histogram_kolm_pravi),hi_kvadrat_stevka(histogram_stevke,histogram_stevke_pravi)
    # plt.plot(histogram_kolm_moj)
    # plt.plot(histogram_kolm_pravi)
    # #plt.legend('moj')
    # plt.show()
    print('d in h',D,HI)
    return D,HI

samo_ena_iter(20,10)

hi_stevke, d_stevke =porazdelitve(100,1000,20)

print('povprecjen',np.average(hi_stevke))
print('povprecje D',np.average(d_stevke))
plt.hist(d_stevke,bins=10)
plt.show()


plt.hist(hi_stevke,bins=10)
plt.show()