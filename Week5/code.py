import random
import math
import matplotlib.pyplot as plt
import numpy as np

exp = np.random.exponential(scale=1, size=10000)
y = []
x = []
for i in range(10000):
    y.append(random.uniform(0, 1))
    x.append(-math.log(1 - y[i]))

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes[0].hist(x, bins=20, range=(0,1))
axes[0].set_title("Histogram of x")
axes[0].set_xlabel("x")
axes[0].set_ylabel("pdf")

axes[1].hist(exp, bins=20, range=(0,1))
axes[1].set_title("Histogram of exp(1)")
axes[1].set_xlabel("x")
axes[1].set_ylabel("pdf")
# plt.hist(x, bins=20, range=(0,1))
# plt.title("Histogram of Array")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
plt.savefig("1.png")
plt.show()

