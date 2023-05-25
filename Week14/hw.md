### 第14周作业

#### 1、
$$
\vec{\pi^{\prime}}=\vec{\pi}\underbar{P}
\\\pi^{\prime}_i=\sum_{k=1}^{M}\frac{P_{ki}}{M}=\frac{1}{M}
\\\pi^{\prime}=\pi
\\因此\vec{\pi}=\frac{1}{M}(1, \cdots, 1)为平稳分布
$$

#### 2、
$$
状态转移矩阵为\underbar{P}=
\left[\begin{array}{ll}
\frac{2}{9} & \frac{7}{9} \\
\frac{1}{2} & \frac{1}{2}
\end{array}\right]
$$

$$
\vec{\beta}=\vec{\beta}\underbar{P}
\\\vec{\beta}=[\frac{9}{23}\ \ \frac{14}{23}]
\\长期来看滞销概率为\frac{9}{23}，畅销概率为\frac{14}{23}
$$

#### 3、
(1)
$$
X_{n+1}-X_n=Y-Z
\\Y\sim P(\lambda),Z\sim B(X_n, p)
\\Y、Z与X_{n-1}时刻及以前的时刻无关，符合无后效性
$$

(2)
$$
设其平稳为\vec{\beta},\vec{\beta}=\vec{\beta}\underbar{P}
\\
\begin{aligned}
    \\X_0为平稳分布，E(X_0)&=\sum_{i=0}^{+\infty}i\beta_i
    \\X_1与X_0同分布，E(X_1)&=E(X_0)
    \\&=E(X_0)+E(Y)-E(Z)
    \\E(Y)&=E(Z)
    \\E(Z)&=\lambda,其中Z\sim B(X_0,p),X_0\sim P(\alpha)
    \\由随机过程的复合，Z&sim P(p\alpha)
    \\E(Z)=p\alpha=\lambda,\alpha&=\frac{\lambda}{p}
\end{aligned}
$$

(3)
$$
\begin{aligned}
平稳分布&\iff X_{n+1}与X_{n}在状态集上同分布
\Rightarrow E(X_{n+1})=E(X_n)
\\&\iff E(Y)=E(Z)\iff E(Z)=\lambda,Z\sim B(X_n, p)
\\E(Z)&=E(E(Z|X_n=k))=\sum_{k=0}^{+\infty}kpP_k=p\sum_{k=0}^{+\infty}kP_k=pE(X_n)
\\E(X_n)&=\frac{\lambda}{p}是平稳分布的必要条件
\end{aligned}
$$