import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['Hiragino Sans GB'] 
mpl.rcParams['font.size'] = 10  
mpl.rcParams['axes.unicode_minus'] = False 

def Zipf(a=1, iter_epoch=100):
    state = 1
    for i in range(iter_epoch):
        a_add1 = math.pow(min(i / (i + 1), 1), a)
        if i > 1:
            a_sub1 = math.pow(min(i / (i - 1), 1), a)
        if state == 1:
            rand = np.random.uniform(0, 1)
            if rand < a_add1 * 0.5:
                state += 1
        
        else:
            rand = np.random.uniform(0, 1)
            if rand < a_add1 * 0.5:
                state += 1
            elif rand > 1 - a_sub1 * 0.5:
                state -= 1
    
    return state

samples = []

for i in range(10000):
    samples.append(Zipf(1, iter_epoch=100))
plt.hist(samples, bins=len(set(samples)), edgecolor='black', density=True)

plt.title('Zipf分布')
plt.xlabel('取值')
plt.ylabel('出现频率')
plt.savefig("6.png")
plt.show()