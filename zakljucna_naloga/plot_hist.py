import numpy as np
import matplotlib.pyplot as plt

n = 100000
x = np.random.standard_normal(n)
y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)



plt.hexbin(x,y)
plt.show()