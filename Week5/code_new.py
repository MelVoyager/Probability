import random
import math
import matplotlib.pyplot as plt
import numpy as np

# exp = np.random.exponential(scale=1, size=10000)
y = []
x = []
for i in range(10000):
    y.append(random.uniform(0, 1))
    x.append(-math.log(1 - y[i]))
plt.hist(x, bins=20, range=(0,1))

x_func = np.linspace(0, 1, 1000)
y_func = np.exp(-x_func) * 500
plt.title('Histogram and function plot')
plt.plot(x_func, y_func, 'r', label='500 * pdf function')
plt.savefig('2.png')
plt.show()