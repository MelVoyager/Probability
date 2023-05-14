import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['Hiragino Sans GB'] 
mpl.rcParams['font.size'] = 15  
mpl.rcParams['axes.unicode_minus'] = False  

def poisson_arrival_time(t, lamda):
    N = np.random.poisson(t * lamda)
    arrival_time = np.random.uniform(0, t, size=N)
    arrival_time = np.sort(arrival_time)
    return arrival_time

fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axes = axs.flatten()

lambdas = [1, 2, 5]

def highlight_points(p, len):
    highlights = []
    for i in range(len):
        rand = np.random.uniform(0, 1)
        if rand < p:
            highlights.append(True)
        else:
            highlights.append(False)
    return highlights
        
for i in range(len(lambdas)):
    arrival_time = poisson_arrival_time(10, lambdas[i])
    height = np.arange(1, len(arrival_time) + 1)
    axes[i].scatter(arrival_time, height, marker='o', s=5)
    axes[i].set_title(f'λ={lambdas[i]}')
    axes[i].set_xlabel("time")
    axes[i].set_ylabel("arrivals")

plt.savefig('3.png')
for ax in axes:
    ax.clear()

for i in range(len(lambdas)):
    arrival_time = poisson_arrival_time(10, lambdas[i])
    highlights = highlight_points(0.3, len(arrival_time))
    colors = ['red' if h else 'blue' for h in highlights]
    height = np.arange(1, len(arrival_time) + 1)
    axes[i].scatter(arrival_time, height, marker='o', s=5, c=colors)
    
    axes[i].scatter([], [], color='red', label='I型')
    axes[i].scatter([], [], color='blue', label='II型')
    
    axes[i].legend()
    axes[i].set_title(f'λ={lambdas[i]}')
    axes[i].set_xlabel("time")
    axes[i].set_ylabel("arrivals")
    
plt.savefig('4.png')