import matplotlib.pyplot as plt
import numpy as np


def vrstaDesumiraj(x):
    frekvencno=np.fft.fft(x)
    f=abs(frekvencno)**2

    N=len(x)
    
    ##šum:
    mejna=50
    vsota=0
    for i in range(mejna,N):
        vsota+=f[i]
    povprecje=vsota/(N-mejna)
    # print(povprecje)
    
    sum_1=np.ones(N)*povprecje
    
    
    # plt.plot(f)
    # plt.axhline(y=povprecje,color='r')
    # plt.show()
    
    ##prenosna funkcija+fi:
    fi=[]
    tau=30
    r=[]
    
    for i in range(len(frekvencno)):
        fi.append(f[i]/(f[i]+sum_1[i]))
        r.append(np.exp(-i/tau)/(tau))
    for i in range(int(len(frekvencno)/2)):
        r[-i]=r[i]
    # print(fi)
    
    R=np.fft.fft(r)
    
    ##inverzna fft:

    invert=np.fft.ifft(frekvencno/R*fi)

    return invert
    
def slika_sum(tabela):
    nova_tabela=[]
    for i in tabela:
        nova_tabela.append(vrstaDesumiraj(i))
    # print(nova_tabela)
    tabela2=np.sqrt(np.array(nova_tabela)**2)
    naslov1=naslov[:-4]+'desum.png'
    # print(len(tabela2),len(tabela2[0]))
    

    return tabela2

###iz datoteke, da dobimo sliko:

def slika(naslov):
    x=[]
    f = open(naslov, 'r',encoding='utf-8')
    data_file=f.readlines()
    
    i=0
    for vrsta in data_file:
        # print(i)
        # print(type(vrsta))
        # print(vrsta)
        # print(len(vrsta))
        x.extend(vrsta)
        i=i+1
    
    matrika=[]
    for i in x:
        if i!='\n':
            matrika.append(i)


    str1 = ''.join(matrika)

    matrika=str1.split('}, {')
    matrika1=[]
    
    for vrsta in matrika:
        vrsta.strip('\n')
        vrsta.strip('{{')
        vrsta.strip('}}')
        vrsta=vrsta.split(', ')
        prava_vrsta=[]
        for i in vrsta:
            if '{{' in i:
                element=i[2:]
            elif '}}' in i:
                element=i[:-2]
            else:
                element=i
            prava_vrsta.append(float(element))
        matrika1.append(prava_vrsta)
    
    naslov_slike=naslov[:-4]+'.png'
    plt.matshow(matrika1,  cmap=plt.cm.gray)
    plt.savefig(naslov_slike)
    plt.show()
    return matrika1



##prikaz slike in returna matriko s podatki slike:

for i in range(3,5):
    naslov='lincoln_L30 _N'+str(i)+'0.txt'
    matrika=slika(naslov)
    matrika2=slika_sum(matrika)
    print(matrika2)
    print(len(matrika),len(matrika[0]))
    plt.matshow(matrika2)
    
    # plt.title('desumirana')
    # # plt.savefig(naslov1)
    # plt.show()
    


