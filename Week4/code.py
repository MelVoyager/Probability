import numpy as np
import matplotlib.pyplot as plt

mean = 100
std_dev = np.sqrt(100)  # 标准差为方差的平方根，此处方差为100
num_samples = 1000

random_samples = np.random.normal(mean, std_dev, num_samples)
# print(random_samples)

plt.bar(range(0, 1000), random_samples)
plt.title("1000 random samples")
plt.xlabel("1000 samples")
plt.ylabel("Value")
plt.savefig("1.png")
plt.clf()

mean1 = np.mean(random_samples)
var1 = np.var(random_samples)

second_samples = []
for i in range(1000):
    select_sample = np.random.randint(0, 1000)
    second_samples.append(random_samples[select_sample])
mean2 = np.mean(second_samples)
var2 = np.var(second_samples)

plt.bar(range(0, 1000), second_samples)
plt.title("1000 second random samples")
plt.xlabel("1000 samples")
plt.ylabel("Value")
plt.savefig("2.png")

print(f"mean1={mean1}, var1={var1}")
print(f"mean2={mean2}, var2={var2}")