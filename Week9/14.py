import numpy as np
from scipy.stats import cauchy
import matplotlib.pyplot as plt

def Gen(type='normal', N=1000):
    X1 = []
    X25 = []
    X100 = []
    X1000 = []
    for i in range(N):
        if type=='normal':
            X = np.random.normal(0, 1, N)
        elif type=='uniform':
            X = np.random.uniform(0, 1, N)
        elif type=='cauchy':
            X = cauchy.rvs(loc=0, scale=1, size=N)
        else:
            raise TypeError('Invalid distribution type')
        X1.append(X[0])
        X25.append(np.mean(X[0:25]))
        X100.append(np.mean(X[0:100]))
        X1000.append(np.mean(X[0:1000]))
        
    X1 = np.array(X1)
    X25 = np.array(X25)
    X100 = np.array(X100)
    X1000 = np.array(X1000)
    
    q1 = [0 for _ in range(4)]
    q3 = [0 for _ in range(4)]
    iqr = [0 for _ in range(4)]
    
    q1[0], q3[0] = np.percentile(X1, [25, 75])
    iqr[0] = q3[0] - q1[0]
    
    q1[1], q3[1] = np.percentile(X25, [25, 75])
    iqr[1] = q3[1] - q1[1]
    
    q1[2], q3[2] = np.percentile(X100, [25, 75])
    iqr[2] = q3[2] - q1[2]
    
    q1[3], q3[3] = np.percentile(X1000, [25, 75])
    iqr[3] = q3[3] - q1[3]
    
    q1 = np.array(q1)
    q3 = np.array(q3)
    iqr = np.array(iqr)
    
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    fig, axs = plt.subplots(2, 2, figsize=(8, 8))
    axes = axs.flatten()
    
    axs[0, 0].hist(X1, bins=100, density=True, range=(lower_bound[0], upper_bound[0]))
    axs[0, 0].set_title(f'{type},n=1')
    
    axs[0, 1].hist(X25, bins=100, density=True, range=(lower_bound[1], upper_bound[1]))
    axs[0, 1].set_title(f'{type},n=25')

    axs[1, 0].hist(X100, bins=100, density=True, range=(lower_bound[2], upper_bound[2]))
    axs[1, 0].set_title(f'{type},n=100')

    axs[1, 1].hist(X1000, bins=100, density=True, range=(lower_bound[3], upper_bound[3]))
    axs[1, 1].set_title(f'{type},n=1000')
    
    for i in range(4):
        axes[i].ticklabel_format(style='sci', axis='x', scilimits=(0, 0))

    plt.savefig(f'{type}.png')
    plt.clf()
        
Gen('normal')
Gen('uniform')
Gen('cauchy')