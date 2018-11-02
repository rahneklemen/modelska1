from scipy.optimize import linprog
import numpy as np

c=np.array([-20,-10,-15])
A=np.array([[3,2,5],[2,1,1],[1,1,3],[5,2,4]])
b=np.array([55, 26, 30, 57])

x0_bounds=(0,None)
x1_bounds=(0,None)
x2_bounds=(0,None)
res = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds,x1_bounds,x2_bounds),             options={"disp": True})
print('Testni del:',res)

print('sedaj zares:\n')

f = open('tabela-zivil.txt', 'r',encoding='utf-8')

vrstice=f.readlines()


i=0
matrika=[]
for vrstica in vrstice:
    if i>1:
        razdeljena=vrstica.split('\t')
        del razdeljena[0]
        #print(razdeljena)
        nova_vrsta=[]
        element=0
        for j in razdeljena:
            j.strip('\n')
            element=float(j)
            nova_vrsta.append(element)
            
        #print(nova_vrsta)
        matrika.append(nova_vrsta)    
    i=i+1

#print(matrika)

np_matrika=np.array(matrika)
#np_matrika=np.negative(np_matrika)


matrika=np.ndarray.tolist(np_matrika.T)
#print(matrika)


funkcija=np.array(matrika[0])
funkcija_negativna=np.negative(funkcija)
funkcija=np.ndarray.tolist(funkcija_negativna)




#print('funkcija f:\n',f)
del matrika[0]
#print('mattrikaA:\n',matrika)
b=[-70,-310,-50,-1,-0.018]


print(matrika,'\nfunkcija:\n',funkcija,'\nvektor b:\n',b)


#print(matrika[4][5])
#[70;310;50;1;0.018];
pogoj=(None,0)

resitev=linprog(funkcija, A_ub=matrika, b_ub=b, bounds=(pogoj),method='simplex',options={"disp": True})
print(resitev)



