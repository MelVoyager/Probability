import scipy.stats as stats

# 计算概率质量函数
mu = 2  # 泊松分布的参数
k = 0   # 想要求解概率质量函数的点
sum = 0
# pmf = stats.poisson.pmf(k, mu)
# print(pmf)

# # 计算累积分布函数
# cdf = stats.poisson.cdf(k, mu)
# print(cdf)

# # 生成随机变量
# rvs = stats.poisson.rvs(mu, size=10)
# print(rvs)

for i in range(2):
    sum += stats.poisson.pmf(i, mu)
    print(f"stats.poisson.pmf({i}, {mu})={stats.poisson.pmf(i, mu)}")
print(sum)