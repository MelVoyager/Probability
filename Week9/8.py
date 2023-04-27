from scipy.stats import binom

n = 10000
p = 0.001
x = 15

prob = binom.cdf(x, n, p)

print(prob)
