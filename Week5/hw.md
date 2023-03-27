### 第5周作业

##### 1、
(1)
$$
取出红球的概率P_1=\frac{3}{3+4+5}=\frac{3}{12}
\\取出白球的概率P_2=\frac{4}{3+4+5}=\frac{4}{12}
\\取出黑球的概率P_3=\frac{5}{3+4+5}=\frac{5}{12}
$$
$P(2红3白1黑)=\big(^{\ \ \ 6}_{2\ 3\ 1}\big)P_1^2P_2^3P_3=\frac{25}{432}$

(2)
$X+Y=3，分别有(X,Y)=(0,3),(1,2),(2,1),(3,0)$
$$
P(X=0,Y=3)=\frac{C_4^3}{C_{12}^3}=\frac{1}{55}
\\P(X=1,Y=2)=\frac{C_3^1C_4^2}{C_{12}^3}=\frac{9}{110}
\\(把所有无序3元组看成基本事件)
\\P(X=2,Y=1)=\frac{C_3^2C_4^1}{C_{12}^3}=\frac{3}{55}
\\P(X=3,Y=0)=\frac{C_3^3}{C_{12}^3}=\frac{1}{220}
$$
事件|$X=0,Y=3$|$X=1,Y=2$|$X=2,Y=1$|$X=3,Y=0$
:-:|:-:|:-:|:-:|:-:
$P$|$\frac{1}{55}$|$\frac{9}{110}$|$\frac{3}{55}$|$\frac{1}{220}$

(3)
$$
P(X=1)=\frac{C_3^1C_9^2}{C_{12}^3}=\frac{27}{55}
$$

##### 2、
$$
F(x,y)=\int_{-\infty}^x \int_{-\infty}^yf(s,t)dtds
$$
$$
\begin{aligned}
    LHS
    &=F(b,d) − F(a,d) − F(b,c) + F(a,c)
    \\&=( F(b,d)-F(b,c) )-(F(a,d)-F(a,c))
    \\&=(\int_{-\infty}^b \int_{-\infty}^df(s,t)dtds-\int_{-\infty}^b \int_{-\infty}^cf(s,t)dtds)-(\int_{-\infty}^a \int_{-\infty}^df(s,t)dtds- \int_{-\infty}^a \int_{-\infty}^cf(s,t)dtds)
    \\&=\int_{-\infty}^b \int_{c}^df(s,t)dtds-\int_{-\infty}^a \int_{c}^df(s,t)dtds
    \\&=\int_{a}^b \int_{c}^df(s,t)dtds
    \\&=P(a < X \le b,c < Y \le d)
\end{aligned}
$$

##### 3、
(1)
$$
S=\pi
\\ \iint_Sp(x,y)=1
\\p=\frac{1}{\pi}
$$
$$f(X,Y)=
\left\{
    \begin{aligned}
        \frac{1}{\pi},x^2+y^2\le1
        \\0,x^2+y^2>1
    \end{aligned}
\right.
$$

(2)
$$
X的pdf:f_x(X)=\int_{-\infty}^{\infty}f(X,Y)dY=\frac{2}{\pi}\sqrt{4-X^2}
\\由对称性，Y的pdf:f_y(Y)=\frac{2}{\pi}\sqrt{4-Y^2}
$$

(3)
$记以r为半径的圆为s$
$$
P(R\le r)=\iint_Sf(x,y)dxdy=\frac{\pi r^2}{\pi}=r^2
$$

(4)
$R的cdf为F(r)=r^2,pdf为f(r)=\frac{d}{dr}F(r)=2r$
$$
\begin{aligned}
    E(R)&=\int_{0}^1rf(r)dr
    \\ &=\int_{0}^1r\times2rdr
    \\ &= \frac{2}{3}
\end{aligned}
$$

##### 4、
$f(x, y) = \frac{1}{2 \pi \sigma_x \sigma_y \sqrt{1 - \rho^2}} \exp \left( -\frac{1}{2(1 - \rho^2)} \left[ \frac{(x - \mu_x)^2}{\sigma_x^2} + \frac{(y - \mu_y)^2}{\sigma_y^2} - \frac{2 \rho (x - \mu_x)(y - \mu_y)}{\sigma_x \sigma_y} \right] \right)$

$$
\begin{aligned}
    f_x(x)&=\int_{-\infty}^{+\infty}\frac{1}{2 \pi \sigma_x \sigma_y \sqrt{1 - \rho^2}} \exp \left( -\frac{1}{2(1 - \rho^2)} \left[ \frac{(x - \mu_x)^2}{\sigma_x^2} + \frac{(y - \mu_y)^2}{\sigma_y^2} - \frac{2 \rho (x - \mu_x)(y - \mu_y)}{\sigma_x \sigma_y} \right] \right)dy
    \\&=\int_{-\infty}^{+\infty}\frac{1}{2 \pi \sigma_x \sigma_y \sqrt{1 - \rho^2}} \exp \left( -\frac{1}{2(1 - \rho^2)} \left[ (\frac{y - \mu_y}{\sigma_y} - \frac{x - \mu_x}{\sigma_x})^2 +(1- \rho^2) \frac{(x - \mu_x)^2}{\sigma_x^2} \right] \right)dy
    \\&= \int_{-\infty}^{+\infty}\frac{1}{2 \pi \sigma_x \sigma_y \sqrt{1 - \rho^2}} \exp \left( -\frac{1}{2(1 - \rho^2)} \left[ (\frac{y - \mu_y}{\sigma_y} - \frac{x - \mu_x}{\sigma_x})^2 \right]-\frac{1}{2} \frac{(x - \mu_x)^2}{\sigma_x^2}  \right)dy
    \\&= \int_{-\infty}^{+\infty}\frac{1}{\sqrt{2} \pi \sigma_x } \exp \left( -\frac{1}{2(1 - \rho^2)} \left[ (\frac{y - \mu_y}{\sigma_y} - \frac{x - \mu_x}{\sigma_x})^2 \right]-\frac{1}{2} \frac{(x - \mu_x)^2}{\sigma_x^2}  \right)d(\frac{y-\mu_y}{\sqrt{2(1-\rho^2)}\sigma_y})
    \\&=\frac{1}{\sqrt{2} \pi \sigma_x } \sqrt{\pi}exp(-\frac{1}{2} \frac{(x - \mu_x)^2}{\sigma_x^2})
    \\&=\frac{1}{\sqrt{2\pi}  \sigma_x }e^{-\frac{(x - \mu_x)^2}{2\sigma_x^2}}
\end{aligned}
$$

##### 5、
$$
\begin{aligned}
    f(x|y)&=\frac{f(x,y)}{f_Y(y)}
    \\&=\frac{\frac{1}{2 \pi \sigma_x \sigma_y \sqrt{1 - \rho^2}} \exp \left( -\frac{1}{2(1 - \rho^2)} \left[ \frac{(x - \mu_x)^2}{\sigma_x^2} + \frac{(y - \mu_y)^2}{\sigma_y^2} - \frac{2 \rho (x - \mu_x)(y - \mu_y)}{\sigma_x \sigma_y} \right] \right)}{\frac{1}{\sqrt{2\pi}  \sigma_y }e^{-\frac{(y - \mu_y)^2}{2\sigma_y^2}}}
    \\ &=\frac{1}{\sqrt{2\pi} \sigma_x  \sqrt{1 - \rho^2}}\exp \left( -\frac{1}{2(1 - \rho^2)} \left[ -(1-\rho^2)\frac{(y - \mu_y)^2}{\sigma_y^2}+\frac{(x - \mu_x)^2}{\sigma_x^2} + \frac{(y - \mu_y)^2}{\sigma_y^2} - \frac{2 \rho (x - \mu_x)(y - \mu_y)}{\sigma_x \sigma_y} \right] \right)
    \\ &=\frac{1}{\sqrt{2\pi} \sigma_x  \sqrt{1 - \rho^2}}\exp \left( -\frac{1}{2(1 - \rho^2)} \left[ \rho^2\frac{(y - \mu_y)^2}{\sigma_y^2}+\frac{(x - \mu_x)^2}{\sigma_x^2} - \frac{2 \rho (x - \mu_x)(y - \mu_y)}{\sigma_x \sigma_y} \right] \right)
    \\ &=\frac{1}{\sqrt{2\pi} \sigma_x  \sqrt{1 - \rho^2}}\exp \left( -\frac{1}{2(1 - \rho^2)} \left[ (\frac{x - \mu_x}{\sigma_x}-
        \rho\frac{y - \mu_y}{\sigma_y})^2 \right] \right)
    \\ &=\frac{1}{\sqrt{2\pi} \sigma_x  \sqrt{1 - \rho^2}}\exp \left( -\frac{1}{2(1 - \rho^2 \sigma_x^2)}  (x - \mu_x-\rho\frac{\sigma_x}{\sigma_y}(y - \mu_y))^2  \right)
\end{aligned}
$$

##### 6、
(1)
$$
S=\frac{1}{2}
$$
$$P(X,Y)=
\left\{
    \begin{aligned}
        2,X\ge0且Y\ge0且X+Y\le1
        \\0,其他\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 
    \end{aligned}
\right.
$$
(2)
$当Y<0或Y>1，P(X,Y)=0,f_Y(y)=0$
$当0\le Y\le1,P(X,Y)=2,X\in[0,1-y],f_Y(y)=\int_0^{1-y}2dx=2(1-y)$

(3)
$当Y<0或Y>1，f_Y(y)=0,无条件密度函数$
$当0\le Y\le1,f_Y(y)=2(1-y)$
$$f(x|y)=\frac{f(x,y)}{f_Y(y)}=
\left\{
    \begin{aligned}
        \frac{1}{1-y},y\le1
        \\0,y>1
    \end{aligned}
\right.
$$

##### 7、
(1)
$$
\begin{aligned}
    P(X_1=k|X_1+X_2=n)&=\frac{P(X_1=k,X_1+X_2=n)}{P(X_1+X_2=n)}
    \\&= \frac{P(X_1=k,X_2=n-k)}{P(X_1+X_2=n)}
    \\由独立性&=\frac{P(X_1=k)P(X_2=k)}{P(X_1+X_2=n)}
    \\ &=\frac{\frac{\lambda_1^k}{k!}e^{-\lambda_1}\frac{\lambda_2^{n-k}}{(n-k)!}e^{-\lambda_2}}{\frac{(\lambda_1+\lambda_2)^n}{n!}e^{-(\lambda_1+\lambda_2)}}
    \\ &=C_n^k(\frac{\lambda_1}{\lambda_1+\lambda_2})^k(\frac{\lambda_2}{\lambda_1+\lambda_2})^{n-k}
\end{aligned}
$$

(2)
$泊松分布可近似理解为二项分布，分别做k次实验一和n-k次实验二，得到的就是类似的二项分布$

##### 8、
(1)
$考虑0-60分钟,P(X=k)=P(Y=k)=\frac{1}{60},k\in[0,60]$
$因为X,Y独立，P(X=k,Y=m)=(\frac{1}{60})^2=\frac{1}{3600}$

(2)
$如果甲先到,P=\int_0^{50}\int_{x+10}^{60}\frac{1}{3600}dydx=\frac{25}{72}$
$对称可得乙先到等甲超过十分钟的概率为\frac{25}{72}$
$P_{tot}=\frac{25}{36}$

##### 9、
(1)
$$
H(x,y)=\int_{-\infty}^{x} \int_{-\infty}^y f(s,t)dtds
\\ \frac{\partial}{\partial x}H(x,y)=\int_{-\infty}^y f(x,t)dt
\\ lim_{y\rightarrow +\infty}\frac{\partial}{\partial x}H(x,y)=\int_{-\infty}^{+\infty} f(x,t)dt=f_x(x)
$$
$$
\begin{aligned}
    lim_{y\rightarrow +\infty}\frac{\partial}{\partial x}H(x,y)&=G(y)(F'(x)[1+\alpha(1-F(x))(1-G(y))]+F(x)[-\alpha F'(x)(1-G(y))])
    \\代入G(y)=1,LHS&=F'(x)
\end{aligned}
$$
$由对称性，Y的边际分布函数f_y(y)=G'(y)$

(2)
$令F(x)=x,x\in[0,1]，则X的边际分布函数F'(x)=x'=1，类似定义G(y)=y,取\alpha=-1和1$

##### 10、
$令U=F(x),V=G(y),则有$
$$
\begin{aligned}
    C(u, v)&=P(U\le u,V\le v)
    \\&=P(F_x(X)\le F_x(x),F_y(Y)\le F_y(y))
    \\由累计分布函数单调性&=P(X\le x, Y\le y)
\end{aligned}
$$

##### 11、
(1)$X连续，Y连续$
$$
全概率公式：\int_{-\infty}^{+\infty}f_{X|Y}(x|y)f_Y(y)dy
\\Bayes公式:
\begin{aligned}
    f_{Y|X}(y|x)&=\frac{f(x,y)}{f_X(x)}=\frac{f_{X|Y}(x|y)f_Y(y)}{\int_{-\infty}^{+\infty}f_{X|Y}(x|y)f_Y(y)dy}
\end{aligned}
$$

(2)$X连续，Y离散$
$$
全概率公式：\sum_{i}f_{X|Y}(x|y)P_{Yi}(y)
\\Bayes公式:
\begin{aligned}
    P_{Y|X}(y|x)&=\frac{P(x,y)}{f_X(x)}=\frac{f_{X|Y}(x|y)P_Y(y)}{\sum_{i}f_{X|Y}(x|y)P_{Yi}(y)}
\end{aligned}
$$

(3)$X离散，Y连续$
$$
全概率公式：\int_{-\infty}^{+\infty}P(x|y)f_Y(y)dy
\\Bayes公式:
\begin{aligned}
    f_{Y|X}(y|x)&=\frac{P(x,y)}{f_X(x)}=\frac{P_{X|Y}(x|y)f_Y(y)}{\int_{-\infty}^{+\infty}P_{X|Y}(x|y)f_{Y}(y)}
\end{aligned}
$$

(4)$X离散，Y离散$
$$
全概率公式：\sum_iP(x|y_i)P(y_i)
\\Bayes公式：
\begin{aligned}
    P(y|x)=\frac{P(x|y)P(y)}{\sum_iP(x|y_i)P(y_i)}
\end{aligned}
$$

##### 12、
(1)
$$
f(x,y)=\frac{c}{1+x^2+y^2},x^2+y^2\le1
\\
\begin{aligned}
    \\ \iint_{x^2+y^2\le1}\frac{c}{1+x^2+y^2}dxdy&=\iint_{0\le r\le 1,0 \le \theta \le 2\pi}\frac{c}{1+r^2}rdrd\theta
    \\&=\int_{0\le r\le 1}\frac{2\pi rc}{1+r^2}dr
    \\ &=\int_{0\le r\le 1} \frac{\pi c}{1+r^2}dr^2
    \\ &=\pi cln(1+r^2)\big|_{r=0}^1
    \\ &= \pi c(ln(2)-ln(1))
    \\ &=\pi c ln2
\end{aligned}
\\ \pi cln2=1
\\ c=\frac{1}{\pi ln2}
$$

(2)
$$
\begin{aligned}
    f_X(x)&=\int_{-\infty}^{+\infty}f(x,y)dy
    \\ &=\int_{-\infty}^{+\infty}\frac{c}{1+x^2+y^2}dy
    \\ 令\alpha^2=1+x^2,&=\int_{-\infty}^{+\infty}\frac{c}{\alpha^2+y^2}dy
    \\ &=\int_{-\infty}^{+\infty}\frac{c}{\alpha(1+(\frac{y}{\alpha})^2)}d\frac{y}{\alpha}
    \\ &= arctan(\frac{y}{\alpha})|_{-\sqrt{1-x^2}}^{\sqrt{1-x^2}}\frac{c}{\alpha}
\end{aligned}
$$
$$
类似可定义\beta^2=1+y^2,f_Y(y)=arctan(\frac{x}{\beta})|_{-\sqrt{1-y^2}}^{\sqrt{1-y^2}}\frac{c}{\beta}
\\显然f(x)\neq f_X(x)f_Y(y)
$$

13、
(1)
$$
\begin{aligned}
    f(x, y) &= \frac{1}{2 \pi \sigma_x \sigma_y \sqrt{1 - \rho^2}} \exp \left( -\frac{1}{2(1 - \rho^2)} \left[ \frac{(x - \mu_x)^2}{\sigma_x^2} + \frac{(y - \mu_y)^2}{\sigma_y^2} - \frac{2 \rho (x - \mu_x)(y - \mu_y)}{\sigma_x \sigma_y} \right] \right)
    \\ &= \frac{1}{2\pi \sqrt{1-\rho^2}}\exp(-\frac{x^2+y^2-2\rho xy}{2(1-\rho^2)})
    \\由X，Y独立，\rho=0 &=\frac{1}{2\pi }\exp(-\frac{x^2+y^2}{2})
    \\ &\ge\frac{1}{2\pi}e^{-1}\approx0.059
\end{aligned}
$$
$在x^2+y^2\le 1时，f(x, y)+\frac{xy}{100}\ge0，且\iint_{x^2+y^2\le 1}\frac{xy}{100}dxdy=0满足\iint_{\Omega}f(x,y)=1，所以g(x,y)是二维密度函数$
(2)
$$
f(x, y) =\frac{1}{2\pi }\exp(-\frac{x^2+y^2}{2})
\\g(x,y)=\frac{1}{2\pi }\exp(-\frac{x^2+y^2}{2})+\frac{xy}{100}
\\ g_X(x)=\int g(x,y)dy=\frac{1}{2\pi}e^{-\frac{x^2}{2}}
\\类似得g_Y(y)=\frac{1}{2\pi}e^{-\frac{y^2}{2}}
\\且(U,V)显然不符合二元正态分布
$$

##### 14、
![6f901052647a1658daa68e59192cab7f.png](https://s1.imagehub.cc/images/2023/03/27/6f901052647a1658daa68e59192cab7f.png)

```python
import random
import math
import matplotlib.pyplot as plt
import numpy as np

# exp = np.random.exponential(scale=1, size=10000)
y = []
x = []
for i in range(10000):
    y.append(random.uniform(0, 1))
    x.append(-math.log(1 - y[i]))
plt.hist(x, bins=20, range=(0,1))

x_func = np.linspace(0, 1, 1000)
y_func = np.exp(-x_func) * 500
plt.title('Histogram and function plot')
plt.plot(x_func, y_func, 'r', label='500 * pdf function')
plt.savefig('2.png')
plt.show()
```