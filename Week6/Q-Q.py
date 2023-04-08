import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

# 生成两个数据集
data1 = np.random.normal(loc=0, scale=1, size=100)
data2 = np.random.normal(loc=1, scale=1, size=100)

# 绘制两个数据集的Q-Q图
fig, ax = plt.subplots()
stats.probplot(data1, fit=True, plot=ax)
stats.probplot(data2, fit=True, plot=ax)

# 显示Q-Q图
plt.show()
