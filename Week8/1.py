import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# 设置参数
n = 10
p1 = 0.9
p2 = 0.1
shift = 8

# 计算概率质量函数
x = np.arange(0, n+1)
pmf1 = binom.pmf(x, n, p1)
pmf2 = binom.pmf(x, n, p2)

# 创建子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 绘制X的PMF
ax1.vlines(x, 0, pmf1, colors='b', lw=5)
ax1.plot(x, pmf1, 'bo', ms=8)
ax1.set_xlabel('X')
ax1.set_ylabel('Probability')
ax1.set_title('X: Binomial PMF with n=10, p=0.9')

# 绘制Y-8的PMF
ax2.vlines(x + shift, 0, pmf2, colors='r', lw=5)
ax2.plot(x + shift, pmf2, 'ro', ms=8)
ax2.set_xlabel('Y')
ax2.set_ylabel('Probability')
ax2.set_title('Y-8: Shifted Binomial PMF with n=10, p=0.1')

# 显示图形
plt.savefig('1.png')
plt.show()
