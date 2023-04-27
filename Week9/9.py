from scipy.stats import norm

mu = 0     # 均值
sigma = 1  # 标准差
p = 0.995  # 概率

x = norm.ppf(p, mu, sigma)
print(x)
