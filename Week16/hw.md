### 第15次作业

#### 1、
$$
分划0=t_0<t1<\cdots<t_n=t,\lambda_n=\max\{t_1-t_0,\cdots,t_k-t_{k-1}\}
\\
\begin{aligned}
    \int_0^tsdB(s)&=\sum t_{k-1}(B(t_k)-B(t_{k-1}))
    \\&=\sum [(t_{k}B(t_k)-t_{k-1}B(t_{k-1}))-B(t_k)(t_{k}-t_{k-1})]
    \\&=tB(t)-0\times B(0) -\sum B(t_k)(t_{k}-t_{k-1})
    \\&=tB(t)-\sum B(t_{k-1})(t_{k}-t_{k-1}) + (B(t_k)-B(t_{k-1}))(t_{k}-t_{k-1})
    \\&=tB(t)-\int_0^tB(s)ds+\sum (B(t_k)-B(t_{k-1}))(t_{k}-t_{k-1})
    \\&=tB(t)-\int_0^tB(s)ds+ E(\sum (B(t_k)-B(t_{k-1}))(t_{k}-t_{k-1}))
    \\&=tB(t)-\int_0^tB(s)ds+ E(\sum 0\times(t_{k}-t_{k-1}))
    \\&=tB(t)-\int_0^tB(s)ds
\end{aligned}
$$

#### 2、

$由It\hat{o}微分公式：$
$$
\begin{aligned}
    \\ dX(t)&=(\frac{\partial X}{\partial t}+\frac{1}{2}\frac{\partial^2 X}{\partial B(t)^2})dt+\frac{\partial X}{\partial B} dB(t)
    \\ &=(-\frac{1}{2}e^{B(t)}e^{-\frac{t}{2}}+\frac{1}{2}e^{B(t)}e^{-\frac{t}{2}})dt+e^{B(t)}e^{-\frac{t}{2}} dB(t)
    \\&=e^{B(t)}e^{-\frac{t}{2}}dB(t)
    \\&=X(t)dB(t)
\end{aligned}
$$

#### 3、
$$
\begin{aligned}
    d(\frac{1}{3}B^3)&=(0+\frac{1}{2}\times2 B)dt+B^2 dB
    \\B^2dB&=d(\frac{1}{3}B^3)-Bdt
    \\由It\hat{o}微分定义，\int_0^tB(s)^2dB(s)&=\frac{1}{3}B(s)^3-\int_0^tB(s)ds
\end{aligned}
$$

#### 4、
$$
\begin{aligned}
    考虑d(B(t)e^{at})&=(aB(t)e^{at}+\frac{1}{2}\times0)dt+e^{at}dB(t)
    \\&=aB(t)e^{at}dt+e^{at}dB(t)
    \\则有\int_0^te^{as}dB(s)&=B(t)e^{at}-\int_0^taB(s)e^{as}ds
    \\可得\frac{\partial}{\partial t}(\int_0^te^{as}dB(s))&=aB(t)e^{at}-aB(t)e^{at}=0
    \\\frac{\partial}{\partial B(t)}(\int_0^te^{as}dB(s))&=e^{at}
    \\\frac{\partial^2}{\partial B(t)^2}(\int_0^te^{as}dB(s))&=\frac{\partial}{\partial B(t)}(e^{at})=0
    \\Y(t)&=\sigma e^{-a t} \int_0^t e^{a s} d B(s)
    \\dY(t)&=(\frac{\partial Y}{\partial t}+\frac{\partial^2 Y}{\partial B^2})dt+\frac{\partial Y}{\partial B}dB
    \\&=((-aY(t)+\frac{\partial}{\partial t}(\int_0^te^{as}dB(s)))\sigma e^{-a t}+0)dt+\sigma e^{-at} e^{at}dB(t)
    \\&=-aY(t)dt+\sigma dB(t)
\end{aligned}
$$