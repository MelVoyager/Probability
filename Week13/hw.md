#### 第13周作业

##### 1、
$
该链上任意2点均可互达，因此其常返性相同
$
$
考虑0时刻目标在位置0的状态(左边有-1，-2，\cdots，右边有1，2，\cdots)
$
$
当p=\frac{1}{2}时：
$
$$
P_{ii}^{(2)}=C_2^1p(1-p)
\\P_{ii}^{(4)}=C_4^2p^2(1-p)^2
\\\cdots
\\P_{ii}^{(2n)}=C_{2n}^np^n(1-p)^n
\\
\\\begin{aligned}
    \\lnP_{ii}^{(2n)}&=ln(2n!)-2ln(n!)+2nln(\frac{1}{2})
    \\由斯特林公式，ln(n!)&=\frac{1}{2}ln(2\pi n)+n(ln(n)-1)
    \\LHS&=\frac{1}{2}[ln(4\pi n)-ln((2\pi n)^2)]+2nln2+2nln(\frac{1}{2})
    \\&=\frac{1}{2}ln(\frac{1}{\pi n})
    \\P_{ii}^{(2n)}&\sim \sqrt{\frac{1}{\pi n}}
    \\\sum_{n=1}^{+\infty}P_{ii}^{(2n)}&=\sum_{n=1}^{+\infty}\sqrt{\frac{1}{\pi n}}=+\infty
\end{aligned}
$$
$
因此0状态是常返的，当p\neq\frac{1}{2}时
$
$$
\begin{aligned}
    LHS&=\frac{1}{2}ln(\frac{1}{\pi n})+2nln2+nln(p(1-p))
    \\&=\frac{1}{2}ln(\frac{1}{\pi n})+nln(4p(1-p))
    \\4p(1-p)<1,&ln(4p(1-p))<0,lim_{n\rightarrow+\infty}nln(4p(1-p))=-\infty
    \\LHS&\rightarrow-\infty
    \\\iff P_{ii}^{(2n)}&\rightarrow0,\sum_{n=1}^{+\infty}P_{ii}^{(2n)}<+\infty
\end{aligned}
$$
$
说明当p\neq\frac{1}{2}时，0状态是非常返的
$

##### 2、
(1)
$从状态0出发经过k步未回到状态0的概率P(X>k)=0.5^k$
$P(X\le k)=1-0.5^k$
$在第k步首次返回的概率为f_{ii}^{(k)}=P(X\le k)-P(X\le k-1)=0.5^k$
$平均步数=k0.5^k=2$
$$
f_{ii}=\sum_{k=1}^{+\infty}f_{ii}^{(k)}=0.5+0.5^2+\cdots=1
$$
$由定义知状态0是正常返的$

(2)
$对\forall k\in N^*，P_{ii}^{(k)}>0$
$状态0是周期为1的$

(3)
$该链上任意2状态是互达的，因此都是正常返的$
$互达状态的周期相同，因此周期均为1$

##### 3、
(1)
$$
若i非常返，则从i出发，以概率1-f_{ii}>0回不到i
\\成功逃离的概率为\sum_{k=1}^{+\infty}f_{ii}^{k-1}(1-f_{ii})=1(几何分布)
\\若有限链均为非常返态，则所有状态都将被逃离(无法到达),这与状态总属于有限状态集矛盾
$$

(2)
$Markov链不可约\iff所有状态均可互达\iff所有状态的常返性相同，均为正常返$

##### 5、
(1)
$1、2为常返态，3、4为非常返态$
$1、2可互达，且这2个状态的次态也为1、2，状态4无法到达，状态3有\frac{1}{2}的概率逃离$

(2)
$状态1可以自返，周期为1，状态2与1互达，也为正常返且周期为1$

##### 6、
(1)
$假设对于状态有限的Markov链，存在零常返态i$
$考虑零常返态i的可达状态集A(i)={j:i\rightarrow j}，则A(i)中所有态均与i互达$
$且A(i)所有态均为零常返的$
$由零常返的性质，若j为非常返或零常返，则\forall i\in S，都有lim_{n\rightarrow\infty}P_{ij}^{(n)}=0$
$$固定i,取j遍历有限状态集中每一个状态，则\sum_{j\in A(i)}P_{ij}^{(n)}=0，这与A(i)是i的所有可达状态矛盾$$

(2)
$$
不可约\iff所有状态可达\iff所有状态常返性相同，且至少有一个常返态
$$
$且状态有限的Markov链不存在零常返态，所以所有状态均为正常返$

8、
$$
\vec{\beta} \underline{P}=\vec{\beta}
\\\underline{P}^{T} \vec{\beta}^{T}=\vec{\beta}^{T}
\\求解P^T的特征向量和特征值，其中特征值为1对应的特征向量为(\frac{1}{3}\ \  \frac{1}{3}\ \  \frac{1}{3})
\\平稳分布即为(\frac{1}{3}\ \  \frac{1}{3}\ \  \frac{1}{3})
$$

9、
$考虑题8中的Markov链$
!['9.png'](9.png)