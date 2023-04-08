import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import expon
# define the normal distribution arguments
mu = 0
sigma = 1

# generate random numbers
n = 100
x1 = np.random.normal(mu, sigma, n)
x2 = np.random.exponential(1 / 2, size=n)
x1.sort()
x2.sort()

# Calculate the quantile of the normal distribution at the p-th quantile
quantile1 = []
quantile2 = []
for i in range(100):
    quantile1.append(norm.ppf((i - 0.5)/100, loc=mu, scale=sigma))
    quantile2.append(expon.ppf((i - 0.5)/100, scale=1 / 2))
quantile1 = np.array(quantile1)
quantile2 = np.array(quantile2)

plt.plot(x1, quantile2, label='normal')
plt.plot(x2, quantile2, label='exponential')

plt.title("x-quantile Plot")
plt.xlabel("x")
plt.ylabel("quantile")
plt.legend()
plt.savefig('x-quantile.png')
plt.show()