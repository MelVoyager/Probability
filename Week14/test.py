import matplotlib.pyplot as plt

# 创建一个列表
data = list(range(1, 11))

# 创建直方图
plt.hist(data, bins=len(data), edgecolor='black')

# 添加标题和坐标轴标签
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 显示直方图
plt.show()
