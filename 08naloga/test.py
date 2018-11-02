import numpy as np
f=open('test.txt','w')

a=np.arange(1,5,0.01)

for i in range(len(a)):
    f.write(str(a[i])+'\n')
    print(i,'\n')
f.close()
