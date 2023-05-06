import numpy as np
import matplotlib.pyplot as plt

lambdas = [1, 2, 5]
sequences = [[] for _ in range(len(lambdas))]

fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axes = axs.flatten()


for i in range(len(lambdas)):
    t = 0
    scale = 1 / lambdas[i]
    while(True):
        random_number = np.random.exponential(scale)
        t += random_number
        if(t > 10):
            break
        sequences[i].append(t)
    sequences[i] = np.array(sequences[i])
    height = np.arange(1, len(sequences[i]) + 1)
    axes[i].scatter(sequences[i], height, marker='o', s=5)
    axes[i].set_title(f'λ={lambdas[i]}')
    axes[i].set_xlabel("time")
    axes[i].set_ylabel("arrivals")
    
plt.savefig('4.png')
plt.show()