from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

n = 25  # n为试验次数
p = 0.6  # p为成功的概率
ps = []
u = 0
var = 0

for i in range(0, 26):
    ps.append(binom.pmf(i, n, p))
    u += ps[i] * i
plt.bar(range(0, 26), ps)
plt.title("Probability distribution of targets in 25 samples")
plt.xlabel("k targets in 25 samples")
plt.ylabel("Probability")
plt.savefig("1.png")

for i in range(0, 26):
    var += ps[i] * ((i - u) ** 2)
sd = np.sqrt(var)
sum_p = 0

# print(u - 2 * sd, u + 2 * sd)
for i in range(0, 26):
    if(u - 2 * sd <= i and i <= u + 2 * sd):
        # print(i)
        sum_p += ps[i]

print(f"E(X)={u}")
print(f"Var(X)={var}")
print(f"Probability in (u-2{chr(963)}, u+2{chr(963)})={sum_p}")