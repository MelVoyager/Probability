### 第12周作业

#### 1、
##### 7.1
$$
设状态集S=\{0,1,2,3\},事件X_t=k表示t时刻距离此前(含t时刻)最近一次到达的距离
\\P_{00}=0.2
\\P_{01}=0.8
\\P_{12}=1
\\P_{20}=P(k=3|k\ge 3)=\frac{0.3}{0.3+0.5}=\frac{5}{8}
\\P_{23}=1-\frac{5}{8}=\frac{3}{8}
\\P_{30}=1
$$


##### 7.2
$不是，假设m>1,当老鼠在瓷砖1处时，X_N=L，P(X_{N+1}=L|X_N=L)=1；而当瓷砖在m处时，P(X_{N+1}=L|X_N=L)=0.5$

##### 7.3
$不是，当苍蝇处于状态2时，P(Y_{N+1}=2|Y_N=1)=0.3；当苍蝇处于状态1时，P(Y_{N+1}=2|Y_N=1)=0$

##### 7.4
(a)
$$
S=\{0,1,2,3,\cdots\}
\\X_t表示当时间为t时，蜘蛛与苍蝇间的距离
\\P_{00}=1,P_{10}=0.7,P_{11}=0.3
\\P_{ii}=0.3,P_{i(i-1)}=0.4,P_{i(i-2)}=0.3
$$

(b)
$$
P^{(n)}_{00}=1
\\P^{(n)}_{ii}=0.3^n
\\\sum_{n=0}^{+\infty}P^{(n)}_{00}=+\infty
\\\sum_{n=0}^{+\infty}P^{(n)}_{ii}=\frac{10}{7}有限
\\所以0状态是常返的，其他状态是非常返的
$$

#### 2、
$$
是Markov链
\\P_{01}=1
\\P_{10}=\frac{1}{9},P_{11}=\frac{4}{9},P_{12}=\frac{4}{9}
\\P_{21}=\frac{4}{9},P_{22}=\frac{4}{9},P_{23}=\frac{1}{9}
\\P_{32}=1
$$
$$
\begin{equation*}
\begin{bmatrix}
0 & 1 & 0 & 0 \\
\frac{1}{9} & \frac{4}{9} & \frac{4}{9} & 0 \\
0 & \frac{4}{9} & \frac{4}{9} & \frac{1}{9} \\
0 & 0 & 0 & 1
\end{bmatrix}
\end{equation*}
$$

#### 3、
$$
记r表示下雨，s表示晴天
\\S=\{rrr,rrs,rsr,rss,srr,srs,ssr,sss\}
\\P(rrr\rightarrow rrs)=0.2,P(rrr\rightarrow rrr)=0.8
\\P(rrs\rightarrow rsr)=0.4,P(rrs\rightarrow rss)=0.6
\\\cdots
\\P(sss\rightarrow sss)=0.8, P(sss,ssr)=0.2
$$

#### 4、

$$
X_2=\begin{equation*}
\begin{pmatrix}
0.25 & 0.25 & 0.5 \\
\end{pmatrix}
\cdot
\begin{pmatrix}
\frac{1}{2} & \frac{1}{3} & \frac{1}{6} \\
0 & \frac{1}{3} & \frac{2}{3} \\
\frac{1}{2} & 0 & \frac{1}{2} \\
\end{pmatrix}
\end{equation*}
\\X_2=(\frac{3}{8} \ \  \frac{1}{6} \ \ \frac{11}{24})
$$
$$
X_3=\begin{equation*}
\begin{pmatrix}
\frac{3}{8} &  \frac{1}{6} & \frac{11}{24} \\
\end{pmatrix}
\cdot
\begin{pmatrix}
\frac{1}{2} & \frac{1}{3} & \frac{1}{6} \\
0 & \frac{1}{3} & \frac{2}{3} \\
\frac{1}{2} & 0 & \frac{1}{2} \\
\end{pmatrix}
\end{equation*}
\\X_3=(0.417 \ \ 0.181 \ \ 0.402)
\\E(X_3)=X_3\cdot(0 \ \ 1 \ \ 2)=0.985
$$

#### 5、
$$
由状态i可达到状态j，可知存在中间状态a_1,a_2,\cdots,a_n(\forall a_n\neq i,j)
\\使得状态转移i\rightarrow a_1\rightarrow a_2\rightarrow\cdots\rightarrow a_n\rightarrow j
\\对1\le k < l \le n,若a_k=a_l,则删去a_{k+1},a_{k+2},\cdots,a_l不会对可达性产生影响
\\所以a_n各不相同，且不等于i,j，因此状态i可以在m步内到达状态 j.
$$

#### 6、
$$
反证：假设\exist k,P^{(k)}_{ij}=\varepsilon>0，
\\i常返\iff\sum_{i=0}^{+\infty}P_{ii}^{(n)}=+\infty
\\
\begin{aligned}
    \\&当1\le n \le k-1,P_{ii}\le 1
    \\&当k\le n \le 2k-1,P_{ii}\le 1-\varepsilon(因为经过k步有\varepsilon概率转移到j,但j无法回到i)
    \\&当2k\le n \le 3k-1,P_{ii}\le (1-\varepsilon)^2
    \\&\cdots
\end{aligned}
\\对由k个概率组成的每一组，\sum_{i=0}^{+\infty}P_{ii}^{(n)}\le k(1+(1-\varepsilon+(1-\varepsilon)^2)+\cdots)=\frac{k}{\varepsilon}
$$

#### 7、
(1)
$$
P_{00}=\frac{2}{9},P_{01}=\frac{7}{9}
\\P_{10}=\frac{1}{2},P_{11}=\frac{1}{2}
\\转移矩阵M=
\begin{equation*}
\begin{bmatrix}
\frac{2}{9} & \frac{7}{9}\\
\frac{1}{2} & \frac{1}{2}\\
\end{bmatrix}
\end{equation*}
$$

(2)
$$
当前状态X_0=[1\ \ 0]
\\X_1=X_0M=[\frac{2}{9} \ \ \frac{7}{9}]
\\X_2=X_1M,X3=X_2M\approx[0.378 \ \ 0.622]
$$

#### 8、
(1)
$$
p=0.25时，(位置，时间)=(0.0, 106)
\\p=0.5时，(位置，时间)=(0.0, 2658)
\\p=0.75时，(位置，时间)=(100.0, 100)
$$

(2)
|p|0.25|0.5|0.75|
|-|-|-|-|
|time_avg|99.834| 2473.896| 99.826|
|zero_proportion|1.0| 0.482| 0.0|

```python
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
```