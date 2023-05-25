import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['Hiragino Sans GB'] 
# mpl.rcParams['font.size'] = 15  
mpl.rcParams['axes.unicode_minus'] = False 

def exp(exp_epoches=1000):
    pos = random.randint(0, 2)
    # 每一次状态转移有2个可能的去处，分别对应第1/2种可能
    path = [[0, 0, 1], [1, 2, 2]]
    for i in range(exp_epoches):
        rand = random.randint(0, 1)
        pos = path[rand][pos]
    
    return pos

cnt = np.array([0, 0, 0])
N = 1000
for i in range(N):
    cnt[exp()] += 1
    
# 输出平稳分布
print(cnt / N)

categories = ['状态0', '状态1', '状态2']
values = cnt / N

# 创建柱状图
plt.bar(categories, values)

# 添加标题和标签
plt.title('平稳分布')
plt.xlabel('Category')
plt.ylabel('Value')

# 显示图形
plt.savefig('9.png')
plt.show()
