import scipy.stats as stats
import scipy.special as special

# 方法一：使用概率密度函数
P1 = 1 - (stats.norm.cdf(2) - stats.norm.cdf(-3))
print("方法一计算结果：", P1)

# 方法二：使用累积分布函数和误差函数
# P2 = special.erf(2/2**0.5)/2 + (1 - special.erf(3/2**0.5))/2
# print("方法二计算结果：", P2)
