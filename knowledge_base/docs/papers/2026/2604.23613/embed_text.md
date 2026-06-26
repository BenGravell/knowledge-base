## Introduction

Zeroth-order (or derivative-free) optimization concerns the minimization of an objective function using only function evaluations, without access to explicit gradient information. Such methods are central in black-box optimization, hyperparameter tuning, bandit problems, and adversarial machine learning, where gradients are either unavailable or prohibitively expensive to compute.

In this paper, we try to solve the problem of minimizing an $L$-smooth, and $\mu$-strongly convex deterministic function using only zeroth-order information. Standard approaches estimate the gradient through randomized directional sampling or finite differences, and then perform (stochastic) gradient-descent steps based on these estimates.

Classical analyses of zeroth-order optimization typically provide convergence guarantees in expectation, bounding the average performance over algorithmic randomness or stochasticity in the objective. For example, existing results bound $\mathbb{E}[f(\bm{x}_{t})-f(\bm{x}^{*})]$ as a function of the number of queries with $\bm{x}^{*}$ being the optimal point. While useful, in-expectation guarantees do not provide explicit high-confidence assurances, which are critical in safety-sensitive or high-stakes applications. In contrast, high-probability guarantees provide stronger assurances about the algorithm's performance in practice.

High-probability convergence analysis of zeroth-order algorithms is substantially more challenging than expectation-based analysis. Zeroth-order gradient estimators, constructed via random directional sampling or finite differences, are inherently noisy, with variance scaling roughly linearly with the dimension $d$. The estimates are sequentially dependent: each iterate $\bm{x}_{t}$ affects the next estimate, creating a martingale-like structure that complicates standard concentration analysis. Moreover, smoothing techniques introduce bias, resulting in a delicate bias--variance tradeoff across iterations. Achieving a global confidence level $1-\delta$ over $T$ steps further requires sophisticated time-uniform concentration inequalities, as naive union bounds would be excessively loose. These factors collectively make high-probability analysis technically intricate and require careful probabilistic reasoning.

The challenge intensifies for stochastic objectives, as in Eq. (1.2), where each function evaluation adds randomness atop the estimator noise. Controlling both sources simultaneously demands balancing the estimator's smoothing bias against stochastic noise. The sequential dependence of iterates combined with stochastic function realizations produces a double-martingale structure, complicating concentration further. Ensuring a $1-\delta$ confidence level now often incurs extra logarithmic factors in query complexity and amplifies dimension-dependent variance. Consequently, establishing high-probability convergence for stochastic zeroth-order methods is far more complex than in the deterministic case, requiring advanced probabilistic tools and meticulous iteration-wise analysis.

In this work, we address this gap by establishing high-probability convergence guarantees for zeroth-order gradient descent in both deterministic and stochastic settings. Our main contributions are as follows: Deterministic objectives: For an $L$-smooth and $\mu$-strongly convex function, zeroth-order gradient descent converges to the global optimum with probability at least $1-\delta$, using function queries. Compared with the query complexity holding in expectation, our result shows that random zeroth-order algorithms only require only $\mathcal{O}(\log\frac{1}{\delta})$ extra queries to achieve a $1-\delta$ probability solution.

Stochastic objectives: For $f(\bm{x})=\mathbb{E}_{\xi}[f(\bm{x};\xi)]$, the random zeroth-order gradient descent converges to the global optimum with probability at least $1-\delta$, with query complexity Compared with the query complexity of zeroth-order stochastic gradient holding in expectation which is $\mathcal{O}\left(\frac{d}{\varepsilon}\right)$, our result shows that random zeroth-order stochastic gradient descent methods only take $\mathcal{O}\left(\log\frac{1}{\varepsilon}\left(\log\frac{1}{\varepsilon}+\log\frac{1}{\delta}\right)\right)$ times extra queries to find an $\varepsilon$-suboptimal solution with a probability at least $1-\delta$.

### Related Works

Zeroth-order optimization has received significant attention due to its ability to handle optimization problems when gradient information is unavailable. In this section, we review related works in three main directions which closely related to our work: random zeroth-order gradient descent, online convex optimization (OCO) with bandit feedback, and (zeroth-order) stochastic gradient descent.

### Random Zeroth-Order Gradient Descent

Random zeroth-order gradient descent method considers the minimization of a deterministic function when only function evaluations are available. A seminal contribution in this direction is by Nesterov & Spokoiny established convergence guarantees of random zeroth-order gradient descent with the Gaussian smoothing. Their method achieves convergence rates comparable to first-order methods up to a dimension-dependent factor and includes an accelerated variant for convex objectives.

Subsequent works have extended the analysis to various settings. For example, Ghadimi & Lan, studied deterministic and stochastic first- and zeroth-order methods for nonconvex optimization, highlighting the effectiveness of multi-point gradient approximations. Ye et al., 2025b proposed Hessian-aware zeroth-order optimization which exploits the second order information to achieve faster convergence rate. However, all these works focus on the convergence analysis holding in expectation.

Recently, Ye et al., 2025a showed that the random zeroth-order optimization with proper search direction and multi-point feedbacks can converge in high probability. Their work relied a large batch of feedbacks to guarantee a decay holding with a high probability for each iteration. Thus, Ye et al., 2025a can only achieve a query complexity $\mathcal{O}\left(\frac{(d+\log(1/\delta))L}{\mu}\log\frac{1}{\varepsilon}\log\log\frac{1}{\varepsilon}\right)$. The detailed comparison is listed in Table 1.

Queries per Iter $\mathcal{O}\Big(\frac{dL}{\mu}\log\frac{1}{\varepsilon}\Big)$ $\mathcal{O}(\log\frac{1}{\varepsilon\delta})$ $\mathcal{O}\left(\frac{(d+\log(1/\delta))L}{\mu}\log\frac{1}{\varepsilon}\log\log\frac{1}{\varepsilon}\right)$ $\mathcal{O}\Big(\frac{dL}{\mu}\log\frac{1}{\varepsilon}+\log\frac{1}{\delta}\Big)$ Table 1: Comparison of query complexities for zeroth-order gradient descent. The table juxtaposes the most related bounds with our high-probability guarantees.

### Online Convex Optimization (OCO) with Bandit Feedback

In the online setting, zeroth-order methods have been extensively applied to bandit convex optimization. Flaxman et al., introduced single-point gradient estimators, providing expected regret bounds for convex losses when only function evaluations are observed. Later works obtained sharper regret bounds for bandit convex optimization using two-point (multi-point) feedback. Recently, Yu et al., showed that OCO with two-point feedback can achieve the optimal regret holding in expectation, which is optimal in both the time zone and the dimension for the strongly convex function. Almost the same time, Ye, obtain the same result holding with a high probability. Through the online to batch conversion technique, the result of Ye, can directly derive that random zeroth-order stochastic gradient descent can achieve a $\mathcal{O}\left(d\log(1/\varepsilon)/\varepsilon\right)$ query complexity holding with high probability. However, in the OCO setting, a bounded stochastic gradient is necessary to achieve the optimal regret. In contrast, our analysis does *not* require the bounded stochastic gradient.

### (Zeroth-order) Stochastic Gradient Descent

Stochastic gradient descent (SGD) is another closely related line of work. The classical stochastic approximation framework dates back to Robbins & Monro who introduced an iterative method for solving stochastic root-finding problems. For strongly convex objectives with bounded stochastic gradient, SGD-type methods can achieve the optimal $O(1/T)$ convergence rate after $T$ stochastic gradient queries holding with high probability. When the function is additionally smooth and the noise has bounded variance, then SGD-type methods can achieve the optimal $O(1/T)$ rate holding in expectation. However, without a bounded-gradient assumption, it becomes substantially more challenging to achieve the optimal rate holding with high probability. More recently, Liu & Zhou, developed a general framework for high-probability convergence of stochastic gradient methods under subgaussian noise, achieving an $\mathcal{O}(\log T/T)$ convergence rate without the unbounded gradient assumption.

Stochastic zeroth-order optimization can be viewed as a derivative-free counterpart of stochastic gradient methods. Modern stochastic zeroth-order methods typically use randomized finite-difference or smoothing-based gradient estimators. Duchi et al., analyzed one- and two-point zeroth-order schemes and showed that two function evaluations can lead to nearly optimal rates up to dimension-dependent factors. Shamir, gave a simple optimal algorithm for bandit and zeroth-order convex optimization with two-point feedback. Ghadimi & Lan, studied stochastic first- and zeroth-order methods for nonconvex stochastic programming and derived complexity bounds for finding approximate stationary points, together with improved large-deviation guarantees through post-optimization procedures. More recently, when the objective function is smooth and strongly convex, several works showed that stochastic zeroth-order methods can achieve an expected query complexity $\mathcal{O}\left(d/\varepsilon\right)$.

We provide a detailed comparison of query complexities for zeroth-order SGD in Table 2 Stochastic Gradient Descent. ‣ 1.1 Related Works ‣ 1 Introduction ‣ High-Probability Guarantees for Random Zeroth-Order Gradient Descent"). $\mathcal{O}\Big(\frac{d}{\varepsilon}\Big)$ $\mathcal{O}\left(\frac{d}{\varepsilon}\right)$ $\mathcal{O}\left(\frac{d\log\frac{1}{\varepsilon}}{\varepsilon}\right)$ $\mathcal{O}\left(\frac{d(\log\frac{1}{\varepsilon}+\log\frac{1}{\delta})}{\varepsilon}\right)$ $\mathcal{O}\left(\frac{d}{\varepsilon}\right)$ $\mathcal{O}\left(\frac{d\cdot\left(\log\frac{1}{\varepsilon}\right)\left(\log\frac{1}{\varepsilon}+\log\frac{1}{\delta}\right)}{\varepsilon}\right)$ Table 2: Comparison of query complexities for zeroth-order gradient descent. We assume that the function is smooth and strongly convex except that Rakhlin et al., don’t require function be smooth. The works of Bottou et al. Rakhlin et al. Liu & Zhou, focus on convergence rates of the first-order SGD. We time d to their iteration complexities to obtain the query complexities.

## Assumptions and Preliminaries

### Assumptions

First, we introduce the first assumption that is widely used in the convergence analysis.

### Assumption 1

The function $f(\bm{x})$ is $L$-smooth and $\mu$-strongly convex. That is, for any $\bm{x},\bm{y}\in\mathbb{R}^{d}$, it holds that When the function $f(\bm{x})$ can be represented as Eq. (1.2), we will introduce the following two extra assumptions.

### Assumption 2

We assume that the stochastic gradient $\nabla f(\bm{x};\;\xi)$ is an unbiased estimation of $\nabla f(\bm{x})$, that is, $\mathbb{E}_{\xi}[\nabla f(\bm{x};\;\xi)]=\nabla f(\bm{x})$.

### Assumption 3 (Bounded Noise Assumption)

We also assume that with a probability $1$, it holds that Assumption 2 is the standard assumption in the analysis of stochastic gradient descent. Assumption 3. ‣ 2.1 Assumptions ‣ 2 Assumptions and Preliminaries ‣ High-Probability Guarantees for Random Zeroth-Order Gradient Descent") is also widely used. A more popular assumption is the bounded variance assumption. However, based on this assumption, we can only achieve the optimal convergence rate holding in expectation. Furthermore, if the objective function $f(\bm{x})=\frac{1}{n}\sum_{i=1}^{n}f_{i}(\bm{x})$, the bounded variance assumption, that is, $\mathbb{E}_{i}\left[\left\|\nabla f(\bm{x})-\nabla f_{i}(\bm{x})\right\|^{2}\right]\leq\sigma_{1}^{2}$, will directly imply that Assumption 3. ‣ 2.1 Assumptions ‣ 2 Assumptions and Preliminaries ‣ High-Probability Guarantees for Random Zeroth-Order Gradient Descent") hold. This can be obtained as Furthermore, if the noise only satisfies the bounded variance, without the extra assumption of the bounded gradient, one can *not* achieve a high probability convergence analysis to my best knowledge. In this work, we do *not* require the bounded gradient assumption, thus, we need a more strict assumption on the noise.

Liu & Zhou, assume that the noise is subgaussian and achieve a convergence rate $\mathcal{O}\left(\log T/T\right)$ when the iteration number $T$ is unknown. In this paper, we also consider the case that $T$ is unknown. Our bounded noise assumption is a little more strict than the subgaussian assumption. In fact, our convergence analysis can be easily extend to the case of subgaussian noise. A direct extension can be achieved using the fact that the subgaussian noise will imply Assumption 3. ‣ 2.1 Assumptions ‣ 2 Assumptions and Preliminaries ‣ High-Probability Guarantees for Random Zeroth-Order Gradient Descent") holds with a high probability at least $1-\delta$. This will only introduce an extra $\log(T/\delta)$ times queries. However, our work mainly focuses on the high probability convergence of *zeroth-order* SGD. The bounded noise assumption will help us to develop techniques to achieve high probability convergence analysis of zeroth-order SGD.

1: Input: Initial vector x0, number of total iteration T, and step size ηt. 4: Access to the value of f(xt + αut) and f(xt − αut) and construct the approximate gradient $$\bm{g}(\bm{x}_{t})=\frac{f(\bm{x}_{t}+\alpha\bm{u}_{t})-f(\bm{x}_{t}-\alpha\bm{u}_{t})}{2\alpha}\bm{u}_{t}.$$ Algorithm 1 Zeroth-order Gradient Descent

### Preliminaries

In this section, we will introduce how to construct the (stochastic) gradient by two-point function queries and list the detailed algorithm description of zeroth-order gradient descent and zeroth-order stochastic gradient descent.

In the construction of gradient estimation, we will first generate a random vector $\bm{u}$ of $d$-dimensional standard Gaussian distribution. Then, we access the function at point $\bm{x}+\alpha\bm{u}$ and $\bm{x}-\alpha\bm{u}$ where $\alpha>0$ is the smooth parameter. After obtaining two function values $f(\bm{x}+\alpha\bm{u})$ and $f(\bm{x}-\alpha\bm{u})$, we can construct the approximate gradient as follows: Similar for the stochastic function, we instead obtain the function value $f(\bm{x}+\alpha\bm{u},\;\xi)$ and $f(\bm{x}-\alpha\bm{u},\;\xi)$ and construct the approximate stochastic gradient at $\bm{x}$ as follows: Once we have the (stochastic) gradient estimation, we can conduct the (stochastic) gradient descent. The detailed algorithm descriptions are listed in Algorithm 1 and Algorithm 2.

1: Input: Initial vector x0, number of total iteration T, and step size ηt. 4: Access to the value of f(xt + αut; ξt) and f(xt − αut; ξt) and construct the approximate gradient $$\bm{g}(\bm{x}_{t};\;\xi_{t})=\frac{f(\bm{x}_{t}+\alpha\bm{u}_{t};\;\xi_{t})-f(\bm{x}_{t}-\alpha\bm{u}_{t};\;\xi_{t})}{2\alpha}\bm{u}_{t}.$$ Algorithm 2 Zeroth-Order Stochastic Gradient Descent

## Main Results

In this section, we will provide the convergence rates of Algorithm 1 and Algorithm 2 holding with high probabilities. Accordingly, we will also give their responding queries complexities. First, we will give the results of Algorithm 1 in the following theorem.

### Theorem 1

Let objective function $f(\bm{x})$ be $L$-smooth and $\mu$-strongly convex. Given $0<\delta<1$ and the total iteration number $0<T$, setting the step size $\eta_{t}=\frac{1}{4L\left\|\bm{u}_{t}\right\|^{2}}$ of of Algorithm 1, with $\bm{x}^{*}$ being the optimal point of objective function, then $\bm{x}_{T}$, the output of Algorithm 1, satisfies that | | $\displaystyle f(\bm{x}_{T})-f(\bm{x}^{*})\leq$ | $\displaystyle\exp\left(-\frac{\mu}{8L}\left(\frac{T}{2d}-\frac{4\log(3/\delta)}{d}\right)\right)\cdot\Big(f(\bm{x}_{0})-f(\bm{x}^{*})\Big)$ | | (3.1) | which holds with a probability at least $1-\delta$.

Based on the above theorem, we can easily obtain the query complexity of Algorithm 1.

### Corollary 2

Let $f(\bm{x})$ satisfies the properties in Theorem 1 and parameters of Algorithm 1 be set as Theorem 1. Given $0<\delta<1$ and the target precision $0<\varepsilon<1$, then if the total number $T$ satisfies and the smooth parameter $\alpha$ satisfies then with a probability at least $1-\delta$, the output $\bm{x}_{T}$ satisfies that

### Remark 1

To find an $\varepsilon$-suboptimal point, Nesterov & Spokoiny, requires that Comparing $T_{1}$ in above equation with our iteration $T$ in Eq. (3.2), to find an $\varepsilon$-suboptimal solution with a high probability $1-\delta$, Algorithm 1 only requires $\log\frac{1}{\delta}$ extra queries.

At the same time, comparing $\alpha_{1}$ in Eq (3.4) with $\alpha$ in Eq. (3.3), to find an $\varepsilon$-suboptimal solution with a high probability, the smooth parameter $\alpha$ of Algorithm 1 should be set almost the same to the case holding in expectation.

Above comparison shows that to find an $\varepsilon$-suboptimal solution with a probability at least $1-\delta$, the extra price of Algorithm 1 is only taking $\mathcal{O}(\log\frac{1}{\delta})$ extra queries.

Next, we will provide the convergence of zeroth-order stochastic gradient descent (Algorithm 2) in the following theorem.

### Theorem 3

Let objective functions $f(\bm{x};\;\xi)$ be $L$-smooth and $f(\bm{x})$ be $\mu$-strongly convex. Assume the stochastic gradient $\nabla f(\bm{x};\;\xi)$ satisfy Assumption 2 and Assumption 3. ‣ 2.1 Assumptions ‣ 2 Assumptions and Preliminaries ‣ High-Probability Guarantees for Random Zeroth-Order Gradient Descent"). Set step size $\eta_{t}=\frac{2d}{\mu(t+T_{0})\left\|\bm{u}_{t}\right\|^{2}}$ with $T_{0}=\frac{16dL}{\mu}$ and smooth parameter $\alpha=1/\sqrt{d(T+T_{0})}$ in Algorithm 2. Given any integer $0\leq K\leq T$ and $0<\delta<1$, define the event: With the notation $\Lambda=\log(T+T_{0})$, $c_{\rho}=2\exp\!\left(4\sqrt{\frac{\log(8T/\delta)}{T_{0}}}+\frac{2\log(T^{2}/\delta)}{T_{0}}\right)$ and $c_{\delta}=\frac{\log(8T/\delta)}{\log(T+T_{0})}$, the constant $\mathcal{C}$ is defined as | | $\displaystyle\mathcal{C}=\max$ | $\displaystyle\left\{\frac{\Delta_{0}dT_{0}}{\Lambda^{2}},\;\frac{8c_{\rho}T_{0}\Delta_{0}}{d\Lambda^{2}},\;\frac{4096\,c_{\rho}^{2}\,c_{\delta}}{\mu^{2}}\left(1+\frac{2c_{\delta}}{T_{0}}\right),\;\frac{256L\sigma^{2}}{\mu^{2}\Lambda}\left(1+\frac{2c_{\delta}}{T_{0}}\right),\;\right.$ | | (3.6) | | | | $\displaystyle\left.\frac{c_{\rho}}{4\Lambda}\left(\frac{L(9+2L)}{\mu}+\frac{c_{\delta}(36+L+4L^{2})}{4d}\right)\right\}.$ | | | Then, event $\mathcal{E}_{\Delta_{K}}$ holds with a probability at least $1-\delta_{K}^{(\Delta)}$ with $\delta_{K}^{(\Delta)}=K\delta/T$.

Based on the above theorem, we can obtain the query complexity of zeroth-order stochastic gradient descent.

### Corollary 4

Let $f(\bm{x})$ satisfies the properties in Theorem 3 and parameters of Algorithm 2 be set as Theorem 3. Given $0<\delta<1$ and the target precision $0<\varepsilon<1$, then if the total number $T$ satisfies and the smooth parameter $\alpha$ satisfies then with a probability at least $1-\delta$, the output $\bm{x}_{T}$ of Algorithm 2 satisfies that

### Remark 2

First, we compare our work with Liu & Zhou, which provides a high probability convergence analysis of stochastic gradient descent with the iteration number $T$ unknown. Liu & Zhou, achieve an iteration complexity Compared with our query complexity in Eq. (3.7), our complexity has an extra factor of $d$ which is natural for zeroth-order methods due to the fact that an exact gradient estimation can be achieved via $d$ times finite differences. The additional logarithmic term $\log(1/\varepsilon)$ stems from the requirement of event $\mathcal{E}_{\Delta_{K}}$ holding for each iteration. We conjecture that if we delicately lower bound $\sum_{t=k+1}^{K-1}\frac{1}{t+T_{0}}\frac{(\bm{u}_{t}^{\top}\nabla f(\bm{x}_{t}))^{2}}{\left\|\bm{u}_{t}\right\|^{2}\left\|\nabla f(\bm{x}_{t})\right\|^{2}},\forall\;k=0,\dots,T-1$, we can obtain a query complexity $\mathcal{O}\left(\frac{d\cdot\left(\log\frac{1}{\varepsilon}\right)\left(\log\log\frac{1}{\varepsilon\delta}\right)}{\varepsilon}\right)$.

Wang et al., provide a query complexity $\mathcal{O}\left(\frac{d}{\varepsilon}\right)$ holding in expectation. Our complexity has extra $\log(1/\varepsilon)$ terms which come from the requirement of event $\mathcal{E}_{\Delta_{K}}$ holding for each iteration. The extra price for a high probability rate is very small which is up to $\log\frac{1}{\varepsilon}$ times.

## Convergence Analysis of Random Zeroth-Order Gradient Descent

In this section, we will focus on the detailed convergence analysis of random zero-order gradient descent (Algorithm 1).

### Lemma 1

Letting the objective function $f(\bm{x})$ be $L$-smooth, and the sequence $\{\bm{x}_{t}\}$ be generated by Algorithm 1, then it holds that Based on the above lemma, we will choose a proper step size to achieve the sufficient decay after $T$-step updates.

### Lemma 2

Assume that the objective function $f(\bm{x})$ is $L$-smooth and $\mu$-strongly convex. We also assume that $\{\bm{x}_{t}\}$ generated by Algorithm 1 satisfies $\left\|\nabla f(\bm{x}_{t})\right\|\neq 0$. By setting step size $\eta_{t}=\frac{1}{4L\left\|\bm{u}_{t}\right\|^{2}}$ in Algorithm 1, we can obtain that | | $\displaystyle f(\bm{x}_{T})-f(\bm{x}^{*})\leq$ | $\displaystyle\exp\left(-\frac{\mu}{8L}\sum_{t=0}^{T-1}\left(\frac{\bm{u}_{t}^{\top}\nabla f(\bm{x}_{t})}{\left\|\bm{u}_{t}\right\|\cdot\left\|\nabla f(\bm{x}_{t})\right\|}\right)^{2}\right)\cdot\Big(f(\bm{x}_{0})-f(\bm{x}^{*})\Big)$ | | (4.3) | | | | $\displaystyle+\sum_{k=0}^{T-1}\exp\left(-\frac{\mu}{8L}\sum_{t=k+1}^{T-1}\left(\frac{\bm{u}_{t}^{\top}\nabla f(\bm{x}_{t})}{\left\|\bm{u}_{t}\right\|\cdot\left\|\nabla f(\bm{x}_{t})\right\|}\right)^{2}\right)\cdot\Delta_{\alpha,k}.$ | | |

### Remark 3

In Lemma 2, we assume that $\{\bm{x}_{t}\}$ generated by Algorithm 1 satisfies $\left\|\nabla f(\bm{x}_{t})\right\|\neq 0$. This is a reasonable assumption. When $f(\bm{x})$ is strongly convex, there is only one optimal point for $f(\bm{x})$. At the same time, $\left\|\nabla f(\bm{x}_{t})\right\|=0$ implies that $\bm{x}_{t}$ is the optimal point. For a random algorithm, the probability to find an optimal point of zero measurement is also zero.

### Remark 4

Lemma 2 is the key to our high-probability convergence of random zero-order gradient descent. Instead of analyzing how the function value will decay after one-step, we consider the function value decay after $T$-step updates. If we analyze the one-step update, with a proper step size, we can obtain that Furthermore, the value $(\bm{u}_{t}^{\top}\nabla f(\bm{x}_{t}))^{2}\sim\left\|\nabla f(\bm{x})\right\|^{2}\cdot\chi^{2}$ will dominate the convergence property. Unfortunately, for a one-step update, we can *not* lower bound the value of $(\bm{u}_{t}^{\top}\nabla f(\bm{x}_{t}))^{2}$ with a high probability since the lower bound of $\chi^{2}$ can not hold with a high probability. The common way to overcome this dilemma is taking expectation since $\mathbb{E}[\xi^{2}]=1$. This is the reason why the convergence analysis of random zeroth-order algorithms commonly holds in expectation. Instead, Lemma 2 analyze function value decay after $T$-step updates to overcome the problem that one can not lower bound $\chi^{2}$ with high probability.

### Remark 5

We take a step size $\eta_{t}=\Omega(\frac{1}{\left\|\bm{u}_{t}\right\|^{2}L})$ in Lemma 2 instead of $\Omega(\frac{1}{dL})$ in the popular convergence analysis of random zeroth-order gradient descent. This is also important in our convergence analysis. By this step size, we have $\left(\frac{\bm{u}_{t}^{\top}\nabla f(\bm{x}_{t})}{\left\|\bm{u}_{t}\right\|\cdot\left\|\nabla f(\bm{x}_{t})\right\|}\right)^{2}\sim\text{Beta}(\frac{1}{2},\;\frac{d-1}{2})$. By this nice property and well-known results of beta distribution, we can obtain our high probability convergence analysis.

### Lemma 3

Letting the function $f(\bm{x})$ be $L$-smooth and the step size be set as $\eta_{t}=\frac{1}{4L\left\|\bm{u}_{t}\right\|^{2}}$, then it holds that

### Proof

By the definition of $\Delta_{\alpha,t}$ and the step size $\eta_{t}$, we can obtain that Next, we will bound the two terms in the right-hand of Eq. (4.3) in the next lemmas. In the following lemma, we will prove that the function will achieve a sufficient function value decay after $T$-step updates which holds with a high probability.

### Lemma 4

Given $0<\delta_{1}^{(\rho)}<1$ and $0<\delta_{2}^{(\rho)}<1$, define two events: Then events $\mathcal{E}_{\rho,1}$ and $\mathcal{E}_{\rho,2}$ hold with probabilities at least $1-\delta_{1}^{(\rho)}$ and $1-\delta_{2}^{(\rho)}$ respectively.

### Proof

By Lemma 28 with $w_{t}=1$ for all $t=0,\dots,T-1$, we can obtain that which holds with a probability at least $1-\delta_{1}^{(\rho)}$.

By Lemma 30, we can obtain that the event $\mathcal{E}_{\rho,2}$ holds with a probability at least $1-\delta_{2}^{(\rho)}$.

The proof of Lemma 4 mainly based on the Freedman's inequality and the good properties of beta distribution. Eq. (4.6) guarantees that the function will achieve a sufficient function value decay which will bound the first term in the right hand of Eq. (4.3). Next, we will use Eq. (4.7) to bound the second term in the right hand of Eq. (4.3).

### Lemma 5

Given an integer $0\leq k\leq T-1$ and $0<\delta_{2}^{(\rho)}<1$, define $\rho_{k}$ as Letting the sequence $\{\bm{u}_{t}\}$ be generated by Algorithm 1 and given $0<\delta^{(\alpha)}<1$, define the event $\mathcal{E}_{\alpha}$ as follows: Then the event $\mathcal{E}_{\alpha}$ holds with a probability at least $1-\delta^{(\alpha)}$.

### Proof of Main Results

Based on the results of Lemma 2--Lemma 5, we will prove Theorem 1 and Corollary 2.

### Proof of Theorem 1

First, Eq. (4.3) of Lemma 2 holds. We will bound two terms of right hand of Eq. (4.3). Let events $\mathcal{E}_{\rho,1}$ (defined in Eq. (4.6)), $\mathcal{E}_{\rho,2}$ (defined in Eq. (4.7)), and $\mathcal{E}_{\alpha}$ (defined in Eq. (4.9)) all hold. Then, we have Furthermore, above equation holds with probability the same to $\Pr\{\mathcal{E}_{\rho,1}\cap\mathcal{E}_{\rho,2}\cap\mathcal{E}_{\alpha}\}$. By setting probability parameters $\delta_{1}^{(\rho)}=\delta_{2}^{(\rho)}=\delta^{(\alpha)}=\delta/3$ in above equation, we can obtain that which holds with a probability at least $1-\delta$. ∎

### Proof of Corollary 2

Setting the first term of the right hand of Eq. (3.1) to $\frac{\varepsilon}{2}$, that is, we can obtain that By setting the second term of the right hand of Eq. (3.1) to $\frac{\varepsilon}{2}$, that is, we can obtain that

## Convergence Analysis of Zeroth-Order Stochastic Gradient Descent

In this section, we will focus on the detailed convergence analysis of random zero-order stochastic gradient descent (Algorithm 2).

### Lemma 6

Letting $f(\bm{x};\;\xi)$ be $L$-smooth and $f(\bm{x})$ be $\mu$-strongly convex, by setting step size $\eta_{t}\leq\frac{1}{8L\left\|\bm{u}_{t}\right\|^{2}}$, then it holds that | | $\displaystyle\Delta_{t+1}\leq$ | $\displaystyle\left(1-\frac{\mu\eta_{t}}{2}\frac{(\bm{u}_{t}^{\top}\nabla f(\bm{x}_{t}))^{2}}{\left\|\nabla f(\bm{x}_{t})\right\|^{2}}\right)\cdot\Delta_{t}+\eta_{t}\left\langle\nabla f(\bm{x}_{t}),\bm{u}_{t}\bm{u}_{t}^{\top}\bm{e}_{t}\right\rangle$ | | (5.1) | | | | $\displaystyle+2L\eta_{t}^{2}\left\|\bm{u}_{t}\right\|^{2}\left\|\bm{u}_{t}^{\top}\bm{e}_{t}\right\|^{2}+\Delta_{\alpha,t}$ | | | where $\Delta_{t}$, $\bm{e}_{t}$, and $\Delta_{\alpha,t}$ are defined as Lemma 6 upper bounds the function value after one-step update of Algorithm 2. Similar to the convergence analysis of Algorithm 1, we will use Eq. (5.1) recursively to obtain the upper bound of the function value after $T$-step updates.

In the next three lemmas, we will describe the exact function value decay after $T$-step updates with properly chosen step size. Instead of an almost fixed step size, which does not depend on the iteration number, set in Algorithm 1, we will set the step size decaying as iteration goes.

### Lemma 7

Let $\{\bm{u}_{t}\}$ and $\{\bm{x}_{t}\}$ be sequences generated in Algorithm 2. Letting $T_{0}=\frac{16dL}{\mu}$, given $0<\delta_{K}^{(\rho)}<1$ and $0<\delta_{K,k}^{(\rho)}<1$, define the events where $\rho_{K}$ and $\rho_{K,k}$ are defined as Then events $\mathcal{E}_{\rho_{K}}$ and $\mathcal{E}_{\rho_{K,k}}$ hold with probabilities $1-\delta_{K}^{(\rho)}$ and $1-\delta_{K,k}^{(\rho)}$, respectively.

Lemma 7 is almost the same to Lemma 4 but Lemma 7 lower bounds the weighted sum of $\sum_{t=0}^{K-1}\frac{1}{t+T_{0}}\frac{(\bm{u}_{t}^{\top}\nabla f(\bm{x}_{t}))^{2}}{\left\|\bm{u}_{t}\right\|^{2}\left\|\nabla f(\bm{x}_{t})\right\|^{2}}$ with the weight $\frac{1}{t+T_{0}}$. This is because we choose a step size $\eta_{t}=\Omega(\frac{1}{t+T_{0}})$ which is almost standard in the analysis of stochastic gradient descent.

Based on above lemmas, we can exactly describe the function value decay after $T$-step updates.

### Lemma 8

Set step size $\eta_{t}=\frac{2d}{\mu(t+T_{0})\left\|\bm{u}_{t}\right\|^{2}}$ with $T_{0}=\frac{16dL}{\mu}$ in Algorithm 2. Assume that event $\mathcal{E}_{\rho,K}$ holds and events $\mathcal{E}_{\rho_{K,k}}$ hold for $k=0,\dots,K-1$. Then, it holds that | | $\displaystyle\Delta_{K}\leq$ | $\displaystyle\rho_{K}\cdot\Delta_{0}+\sum_{k=0}^{K-1}\rho_{K,k}\left(\frac{2d\cdot\left\langle\nabla f(\bm{x}_{k}),\bm{u}_{k}\bm{u}_{k}^{\top}\bm{e}_{k}\right\rangle}{\mu(k+T_{0})\left\|\bm{u}_{k}\right\|^{2}}\right)$ | | (5.7) | | | | $\displaystyle+\sum_{k=0}^{K-1}\rho_{K,k}\left(\frac{8Ld^{2}}{\mu^{2}(k+T_{0})^{2}}\cdot\frac{\left\|\bm{u}_{k}^{\top}\bm{e}_{k}\right\|^{2}}{\left\|\bm{u}_{k}\right\|^{2}}\right)$ | | | | | | $\displaystyle+\sum_{k=0}^{K-1}\rho_{K,k}\left(\frac{dL\alpha^{2}\left\|\bm{u}_{k}\right\|^{2}}{4\mu(k+T_{0})}+\frac{d^{2}L^{3}\alpha^{2}\left\|\bm{u}_{k}\right\|^{2}}{\mu^{2}(k+T_{0})^{2}}\right).$ | | | In the next subsections, we will upper bound the terms in the right hand of Eq. (5.7).

### Linear Martingale Bound

In this section, we will bound the second term of the right hand of Eq. (5.7). First, we will introduce two notations:

### Lemma 9

Let the stochastic gradient $\nabla f(\bm{x};\;\xi)$ satisfy Assumption 2 and Assumption 3. ‣ 2.1 Assumptions ‣ 2 Assumptions and Preliminaries ‣ High-Probability Guarantees for Random Zeroth-Order Gradient Descent"). Conditioning on the Gaussian directions $\{\bm{u}_{k}\}_{k=0}^{K-1}$, and let $\mathcal{G}_{k}:=\sigma(\xi_{0},\dots,\xi_{k})$ be the filtration generated by $\xi_{0},\dots,\xi_{k}$. Then $\{Y_{k}\}_{k=0}^{K-1}$ (defined in Eq. (5.8)) is a martingale difference sequence with respect to $\mathcal{G}_{k}$ conditional on $\{\bm{u}_{k}\}_{k=0}^{K-1}$. Moreover, given $\delta_{K}^{(Y)}\in$, define the event Then the event $\mathcal{E}_{Y_{K}}$ holds with a conditional probability at least $1-\delta_{K}^{(Y)}$.

Next, we will give an deterministic upper bound of $V_{K}$ defined in Eq. (5.10). We will upper bounding $1/\left\|\bm{u}_{k}\right\|^{2}$ and $\sum_{k=0}^{K-1}|\rho_{K,k}|\cdot|\nabla f(\bm{x}_{k})^{\top}\bm{u}_{k}|/T_{k}$ separately. Then, by the union bound, we can obtain the upper bound of $V_{K}$.

### Lemma 10

Let the sequence $\{\bm{u}_{t}\}$ with $t=0,\dots,T-1$ be generated by Algorithm 2. Define the event Given $0<\delta^{(u)}<1$ and the dimension satisfying $d\geq 16\log(T/\delta^{(u)})$, then the event $\mathcal{E}_{u}$ holds with a probability at least $1-\delta^{(u)}$.

### Proof

By Lemma 19, we can obtain that for a given $t$, with a probability at least $1-\delta^{(u)}/T$, it holds that $\left\|\bm{u}_{t}\right\|^{2}\geq d-2\sqrt{d\left(\log(T/\delta^{(u)})\right)}$. Combining with the condition that $d\geq 16\log(T/\delta^{(u)})$, we can obtain that $\left\|\bm{u}_{t}\right\|^{2}\geq d/2$. By the probability union for all $t=0,\dots,T-1$, we can obtain that the event $\mathcal{E}_{u}$ holds with a probability at least $1-\delta^{(u)}$. ∎

### Lemma 11

Assume that the objective function $f(\bm{x})$ is $L$-smooth, and for some deterministic constants $\bar{\Delta}_{k}$, Given $0<\delta_{K}^{(V)}<1$, define the event Then the event $\mathcal{E}_{V_{K}}$ holds that with a probability at least $1-\delta_{K}^{(V)}$.

Combining the results in Lemma 9--Lemma 11, we can upper bound $\sum_{k=0}^{K-1}Y_{k}$ explicitly.

### Lemma 12

Assume the conditions in Lemma 10 and Lemma 11 hold, then we have $V_{K}$ which holds with a probability at least $\Pr\{\mathcal{E}_{Y_{K}}\cap\mathcal{E}_{u}\cap\mathcal{E}_{V_{K}}\}$.

### Proof

Lemma 10 and Lemma 11 provides a deterministic upper bound of $V_{K}$ which holds a probability at least $\Pr\{\mathcal{E}_{u}\cap\mathcal{E}_{V_{K}}\}$. That is, Replacing above equation to Eq. (5.9), that is, event $\mathcal{E}_{Y_{K}}$ holds, we can obtain the result in Eq. (5.14) which holds with a probability at least $\Pr\{\mathcal{E}_{Y_{K}}\cap\mathcal{E}_{u}\cap\mathcal{E}_{V_{K}}\}$. ∎

### Quadratic Term Bound

In this section, we will bound the third term of the right hand of Eq. (5.7). Similar to upper bounding the second term, we will first provide an upper bound of $\sum_{k=0}^{K-1}\frac{\rho_{K,k}}{T_{k}^{2}}\cdot\left\|\bm{u}_{k}^{\top}\bm{e}_{k}\right\|^{2}$ holding with a high probability. Then, combining with Lemma 10, we obtain the final upper bound.

### Lemma 13

Given $0<\delta_{K}^{(Q)}<1$ and letting Assumption 3. ‣ 2.1 Assumptions ‣ 2 Assumptions and Preliminaries ‣ High-Probability Guarantees for Random Zeroth-Order Gradient Descent") hold, define the event: Then the event $\mathcal{E}_{Q_{K}}$ holds with a probability at least $1-\delta_{K}^{(Q)}$.

### Lemma 14

Assume the conditions in Lemma 10 and Lemma 13 hold, then we have which holds with a probability $\Pr\{\mathcal{E}_{u}\cap\mathcal{E}_{Q_{K}}\}$.

### Proof

Combining the results in Lemma 10 and Lemma 13, we can obtain the result. ∎

### Upper Bound Related to Parameter $\alpha$

Now we will bound the forth term of the right hand of Eq. (5.7) which is related to the smooth parameter $\alpha$.

### Lemma 15

Letting us denote $c_{1}=\frac{dL}{4\mu}$ and $c_{2}=d^{2}L^{3}/\mu^{2}$, given $0<\delta_{K}^{(\alpha)}<1$, define the event | | $\displaystyle\mathcal{E}_{\alpha_{K}}=$ | $\displaystyle\left\{\sum_{k=0}^{K-1}\rho_{K,k}\left(\frac{c_{1}}{T_{k}}+\frac{c_{2}}{T_{k}^{2}}\right)\left\|\bm{u}_{k}\right\|^{2}\leq d\sum_{k=0}^{K-1}\rho_{K,k}\left(\frac{c_{1}}{T_{k}}+\frac{c_{2}}{T_{k}^{2}}\right)\right.$ | | (5.15) | | | | $\displaystyle\left.+2d\sqrt{\log\frac{1}{\delta_{K}^{(\alpha)}}\cdot\sum_{k=0}^{K-1}\rho_{K,k}^{2}\left(\frac{c_{1}}{T_{k}}+\frac{c_{2}}{T_{k}^{2}}\right)^{2}}+2d\log\frac{1}{\delta_{K}^{(\alpha)}}\max_{0\leq k<K-1}\rho_{K,k}\left(\frac{c_{1}}{T_{k}}+\frac{c_{2}}{T_{k}^{2}}\right)\right\}.$ | | | Then the event $\mathcal{E}_{\alpha_{K}}$ holds with a probability at least $1-\delta_{K}^{(\alpha)}$.

### Induction Proof of Theorem 3

Before the detailed proof of Theorem 3, we first list two lemmas that upper bound $\rho_{K}$, $\rho_{K,k}$, and $\max\left\{\log\frac{1}{\delta_{K}^{(Y)}},\;\log\frac{1}{\delta_{K}^{(V)}},\;\log\frac{1}{\delta_{K}^{(Q)}},\;\log\frac{1}{\delta_{K}^{(\alpha)}}\right\}$.

### Lemma 16 (Upper bounds on $\rho_{K}$ and $\rho_{K,k}$)

Letting $\rho_{K}$ and $\rho_{K,k}$ be defined in Eq. (5.5) and Eq. (5.6) respectively, then for every $1\leq K\leq T-1$ and $0\leq k\leq K-1$, it holds that with $\delta_{K}^{(\rho)}=\mathcal{O}(\delta/(8T))$ and $\delta_{K,k}^{(\rho)}=\mathcal{O}\left(\delta/(8T^{2})\right)$, $c_{\rho}$ is defined as

### Lemma 17

There exists a constant $c_{\delta}$ such that the following inequalities hold: where the constant $c_{\delta}$ can be defined as Based on above lemmas, we will give the detailed proof of Theorem 3 by induction.

### Proof of Theorem 3

We prove Theorem 3 by induction on $K$.

### Base case

When $K=0$, since $T_{0}$ is deterministic, by the value of $\mathcal{C}$ in Eq. (3.6), we can directly obtain that Induction Hypothesis. Fixing any $K\in\{1,\dots,T-1\}$, we assume that event $\mathcal{E}_{\Delta_{K}}$ holds with a probability at least $1-\delta_{K}^{(\Delta)}$. That is, for every $k=0,\dots,K-1$, it holds that Assuming events $\mathcal{E}_{\rho_{K}}$ and $\mathcal{E}{\rho_{K,k}}$ (defined in Eq. (5.3) and (5.4)) hold, then Eq. (5.7) in Lemma 8 holds. Next, combining with induction hypothesis, we will bound the four terms on the right-hand side of Eq. (5.7) separately.

### The Initial Term

By Eq. (5.16. ‣ 5.4 Induction Proof of Theorem 3 ‣ 5 Convergence Analysis of Zeroth-Order Stochastic Gradient Descent ‣ High-Probability Guarantees for Random Zeroth-Order Gradient Descent")), we have $\rho_{K}\Delta_{0}\leq c_{\rho}\frac{T_{0}}{T_{K}}\Delta_{0}$. Hence, by the fact that $\mathcal{C}\geq 8c_{\rho}T_{0}\Delta_{0}/(d\Lambda^{2})$ in Eq. (3.6), we can obtain that Furthermore, above equation only depends on the event $\mathcal{E}_{\rho_{K}}$ defined in Eq. (5.3). Thus, it holds that

### Linear Martingale Bound

We may apply Lemma 12 with the deterministic upper bounds $\bar{\Delta}_{k}=\mathcal{C}d\Lambda^{2}/T_{k}$. Combining with Eq. (5.16. ‣ 5.4 Induction Proof of Theorem 3 ‣ 5 Convergence Analysis of Zeroth-Order Stochastic Gradient Descent ‣ High-Probability Guarantees for Random Zeroth-Order Gradient Descent")) and Eq. (5.13), we obtain Thus, we can obtain that Combining with Eq. (5.14), we can obtain that Moreover, to achieve above, it requires the events $\mathcal{E}_{\rho_{K,k}}$ with $k=0,\dots,K-1$, the induction hypothesis $\mathcal{E}_{\Delta_{K}}$ and Lemma 12 hold simultaneously. That is, by the union bound, we have

### Quadratic Term Bound

We will bound the terms in Lemma 14. By Eq. (5.16. ‣ 5.4 Induction Proof of Theorem 3 ‣ 5 Convergence Analysis of Zeroth-Order Stochastic Gradient Descent ‣ High-Probability Guarantees for Random Zeroth-Order Gradient Descent")), we get Thus, we can obtain that Combining with Lemma 14, we can obtain that | | | $\displaystyle\frac{8Ld^{2}}{\mu^{2}}\sum_{k=0}^{K-1}\frac{\rho_{K,k}}{T_{k}^{2}}\cdot\frac{\|\bm{u}_{k}^{\top}\bm{e}_{k}\|^{2}}{\|\bm{u}_{k}\|^{2}}\leq\frac{8Ld^{2}}{\mu^{2}}\cdot\frac{2\sigma^{2}}{d}\cdot\frac{c_{\rho}}{T_{K}}\left(\Lambda+\frac{2\sqrt{2}\sqrt{c_{\delta}\Lambda}}{T_{0}}+\frac{2c_{\delta}\Lambda}{T_{0}}\right)$ | | (5.25) | | | $\displaystyle\leq$ | $\displaystyle\frac{16Ld\sigma^{2}}{\mu^{2}T_{K}}\cdot\left(\Lambda+\frac{2\sqrt{2}\sqrt{c_{\delta}\Lambda}}{T_{0}}+\frac{2c_{\delta}\Lambda}{T_{0}}\right)\leq\frac{16Ld\sigma^{2}}{\mu^{2}T_{K}}\cdot\left(\Lambda+\frac{2+c_{\delta}\Lambda}{T_{0}}+\frac{2c_{\delta}\Lambda}{T_{0}}\right)$ | | | | | $\displaystyle\leq$ | $\displaystyle\frac{32Ld\sigma^{2}\Lambda}{\mu^{2}T_{K}}\cdot\left(1+\frac{2c_{\delta}}{T_{0}}\right)\stackrel{{\scriptstyleeq:cC}}{{\leq}}\frac{\mathcal{C}\cdot d\cdot\Lambda^{2}}{8T_{K}}.$ | | |

### Upper Bound Related to Parameter $\alpha$

Combining Lemma 15 and Lemma 31, we can obtain that where the last inequality is because of Furthermore, above equation holds only depending the event $\mathcal{E}_{\alpha_{K}}$, that is, Step 6: Conclusion of the induction step.

Combining Eq. (5.7), (5.21), (5.23), (5.25), and (5.27), we conclude that This proves the induction step.

By Eq. (5.22), (5.24), (5.26), and (5.28), we can obtain that where the last equality is because of $\delta_{K}^{(\Delta)}=K/T$ and we set

### Proof of Corollary 4

By Eq. (3.5), to achieve an $\varepsilon$-suboptimal solution, we only need that By the definition of $\mathcal{C}$ in Eq (3.6), we can obtain that if $T$ is large enough, then it holds that Combining above two equations, we can obtain that Combining with the value of $\alpha=1/\sqrt{d(T+T_{0})}$ in Theorem 3, we can obtain that

## Conclusion

In this paper, we studied high-probability convergence guarantees for zeroth-order gradient descent methods for smooth and strongly convex optimization. Unlike most classical analyses, which establish convergence only in expectation, our results provide explicit confidence guarantees for the performance of random zeroth-order algorithms.

For deterministic objectives, we proved that random zeroth-order gradient descent achieves an $\varepsilon$-suboptimal solution with probability at least $1-\delta$ using function queries. This matches the classical expectation-based query complexity up to only an additive logarithmic dependence on the confidence parameter. In particular, the result shows that the standard two-query random zeroth-order method can provide strong high-probability guarantees without requiring large batches of function evaluations at each iteration.

We further considered stochastic objectives, where both randomized directional sampling and stochastic function evaluations introduce additional uncertainty. Under a bounded-noise assumption, and without imposing a uniformly bounded stochastic-gradient condition, we established a high-probability query complexity of This result gives a high-confidence analogue of the standard expected convergence guarantees for stochastic zeroth-order methods, with only additional logarithmic factors in the accuracy and confidence parameters.

Overall, our analysis demonstrates that random zeroth-order gradient descent can achieve reliable high-probability performance guarantees in both deterministic and stochastic smooth strongly convex optimization. These results narrow the gap between expectation-based and high-probability theory for zeroth-order methods, and suggest several directions for future work, including improving the logarithmic factors in the stochastic setting, extending the analysis to weaker noise assumptions, and developing high-probability guarantees for broader classes of nonconvex or nonsmooth zeroth-order problems.
