## 第3周作业

#### 2、
######（1）
$(\Omega,\mathscr{F}, P)$为概率空间，对于随机变量$X$，设$S_n=\{t\in \Omega, X(t)<-n\}$,则有$S_1\supset S_2\supset S_3\cdots\supset S_n\cdots$
注意到$lim_{n\rightarrow \infty}S_n=\varnothing$，因为若其不为$\varnothing$，则$\exist t\in \Omega$，满足$X(t)<n,\forall n > 0$，矛盾
$$
\begin{aligned}
lim_{x\rightarrow -\infty}F(x)&=lim_{n\rightarrow\infty}P(x\in S_n)\\
&=P(x\in \varnothing)\\
&=0
\end{aligned}
$$

设$S_n^{'}=\{t \in \Omega, X(t)>n\}$，同样有$S_1\supset S_2\supset S_3\cdots\supset S_n\cdots$，且$lim_{n\rightarrow \infty}S_n=\varnothing$
$$
\begin{aligned}
lim_{x\rightarrow +\infty}F(x)&=lim_{n\rightarrow\infty}P(x\in {(S_n^{'})}^C)\\
&=P(x\in (\varnothing)^C)\\
&=P(\Omega)\\
&=1
\end{aligned}
$$

###### (2)
设$M_n=x+\frac{1}{n}$，