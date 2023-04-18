import numpy as np
import matplotlib.pyplot as plt

x = [[] for _ in range(4)]

for j in range(4):
    for i in range(10000):
        r = np.random.rand()
        if r < 0.5:
            if i == 0:
                x[j].append(1)
            else:
                x[j].append(x[j][i - 1] + 1)
        else:
            if i == 0:
                x[j].append(-1)
            else:
                x[j].append(x[j][i - 1] - 1)
    

# 创建一个2x2的子图
fig, axes = plt.subplots(nrows=2, ncols=2)

# 创建示例数据
x_frame = np.linspace(0, 10000, 10000)

axes[0, 0].plot(x_frame, x[0])
axes[0, 0].set_title("1")

axes[0, 1].plot(x_frame, x[1])
axes[0, 1].set_title("2")

axes[1, 0].plot(x_frame, x[2])
axes[1, 0].set_title("3")

axes[1, 1].plot(x_frame, x[3])
axes[1, 1].set_title("4")

# 调整子图之间的间距
plt.subplots_adjust(wspace=0.5, hspace=0.5)

# 显示图形
plt.savefig('16.png')
plt.show()