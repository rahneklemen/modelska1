import matplotlib.pyplot as plt
import numpy as np

def fft_noise(vrsta):
    frekvenca=np.fft.fft(vrsta)
    N=len(frekvenca)
    moc=abs(frekvenca)**2

    ##šum:
    mejna=100
    vsota=0
    for i in range(mejna,N):
        vsota+=moc[i]
    povprecje = vsota/(N-mejna)
    print(povprecje)
    noise = np.ones(N)*povprecje

    ##prenosna funkcija:
    fi=[]
    tau=30
    r=[]

    for i in range(N):
        fi.append(moc[i]/(moc[i]+noise[i]))
        r.append(np.exp(-i/tau)/(tau))
    for i in range(int(N/2)):
        r[-i]=r[i]
    # print(fi)

    R=np.fft.fft(r)
    okej=np.real(np.fft.ifft(frekvenca/R*fi))

    return okej

#----------------------------------------------------
def nonoise(matrika):
    slika=[]
    for i in matrika:
        slika.append(fft_noise(i))
    return slika

#-----------------------------------------------------

naslov='lincoln_L30 _N00.txt'
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

matrika2=[]

for i in range(len(matrika[0])):
    vrsta=[]
    for j in range(len(matrika)):
        print(i,j)
        vrsta.append(matrika[i][j])
    matrika2.append(vrsta)


plt.matshow(matrika2,  cmap=plt.cm.gray)
plt.show()

ociscena_slika=nonoise(matrika1)
print(type(ociscena_slika),type(ociscena_slika[0]))

tapravo=[]
for i in ociscena_slika:
    tapravo.append(np.array(i))

plt.matshow(ociscena_slika,  cmap=plt.cm.gray)
plt.show()


