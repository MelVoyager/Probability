from scipy.stats import norm

x1 = -0.156
x2 = 0.156

fx2 = norm.cdf(x2)
fx1 = norm.cdf(x1)

result = fx2 - fx1

print(result)
