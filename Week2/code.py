import numpy as np
import matplotlib.pyplot as plt

def experiment(n, probablity, ifprint, figname):
    tot = 0
    pos = 0
    freq = []
    frame = np.linspace(0, n, n)
    for i in range(n):
        x = np.random.rand()
        if(x <= probablity):
            pos += 1
        tot += 1
        freq.append(pos/tot)
    if(ifprint):
        plt.scatter(frame, freq, marker='o')
        plt.xlabel("Experiments")
        plt.ylabel("Frequency")
        plt.savefig(figname)
    return pos

# experiment(2000, 0.5, True, "3.png")
# exit()
num = []
for i in range(100):
    num.append(experiment(2000, 0.5, False, ""))
plt.bar(range(0, 100), num)
plt.title("Histogram of 100 experiments")
plt.xlabel("Experiments")
plt.ylabel("Frequency")
print(np.mean(num))
plt.savefig("4.png")