import numpy as np

def random_walk(N=100, p=0.5):
    pos = N / 2
    cnt = 0
    while(1):
        cnt = cnt + 1
        rand = np.random.uniform(0, 1)
        if rand < p:
            pos = pos + 1
        else:
            pos = pos - 1
        if pos == 0 or pos == N:
            return (cnt, pos)

print(random_walk(p=0.25))
print(random_walk(p=0.5))
print(random_walk(p=0.75))

result = [[], [], []]
for i in range(1000):
    result[0].append(random_walk(p=0.25))
    result[1].append(random_walk(p=0.5))
    result[2].append(random_walk(p=0.75))

time_avg = [0, 0, 0]
zeros = [0, 0, 0]
for i in range(3):
    time_avg[i] = sum(a for a, _ in result[i]) / len(result[i])
    zeros[i] = sum(1 for _, b in result[i] if b == 0) / 1000
    
print(f'time_avg={time_avg}')
print(f'zeros={zeros}')