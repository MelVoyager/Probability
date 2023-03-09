from scipy.stats import binom

n = 25  # n为试验次数
p = 0.6  # p为成功的概率
k = 15  # k为成功的次数

p_x_k = binom.pmf(k, n, p)  # 计算p(X=k)
s = 0
for i in range(0, 10):
    s += binom.pmf(i, n, p)
print("p(X={}) = {}".format(k, p_x_k))
print(s)
