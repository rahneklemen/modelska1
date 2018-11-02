import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as optimization

def funkcija(parametri,matrika,meritve,error):
    return ((meritve - np.dot(matrika, parametri))/error)



##zacetek programa:

y=np.array([41.6 , 37.7875 , 36.4975 , 35.785 , 34.53 , 42.345 , 39.5375 , 37.3525 , 36.36 , 33.915])
temp=np.array([100 ,  161 , 227 , 270 , 362 , 90 , 149 , 206 , 247 , 352],dtype=float)
moc=np.array([545 , 602 , 538 , 550 , 522 , 276 , 275 , 274 , 274 , 272],dtype=float)
napaka=np.array([0.16 , 0.16 , 0.16 , 0.16 , 0.16 , 0.28 , 0.28 , 0.28 , 0.28 , 0.28])

n=len(y)





print(len(y),len(moc),len(temp),len(napaka))

A=np.vstack([np.ones(n),temp,temp**3,temp**4,moc,moc**2,moc**3]).T

print('matrika:\n')
print(A,'\n')

print('\n napaka:')
print(napaka)

x0=np.ones(7)/1
print(x0)

4
#napaka=np.ones(n)
resitev=optimization.leastsq(funkcija, x0, args=(A, y,napaka))
print('resitev',resitev)
koeficienti=resitev[0]
print('koeficienti',koeficienti)

y_fit=np.dot(A, koeficienti)
print(y_fit)
print(y)
plt.plot(y_fit,'o-')
plt.plot(y)
plt.show()
