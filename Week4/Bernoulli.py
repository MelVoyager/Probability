from scipy.stats import binom

n = 1e6  # n为试验次数
p = 2 * 1e-6  # p为成功的概率
# k =   # k为成功的次数

# p_x_k = binom.pmf(k, n, p)  # 计算p(X=k)
s = 0
for i in range(0, 3):
    s += binom.pmf(i, n, p)
# print("p(X={}) = {}".format(k, p_x_k))
print(f"n={n},p={p},E={n*p}")
print(s)
print(1-s)