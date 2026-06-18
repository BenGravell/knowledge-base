Complexity of Finding Stationary Points of Nonsmooth Nonconvex Functions

We provide the first non-asymptotic analysis for finding stationary points of nonsmooth, nonconvex functions. In particular, we study the class of Hadamard semi-differentiable functions, perhaps the largest class of nonsmooth functions for which the chain rule of calculus holds. This class contains examples such as ReLU neural networks and others with non-differentiable activation functions. We first show that finding an epsilon-stationary point with first-order methods is impossible in finite time. We then introduce the notion of (delta, epsilon)-stationarity, which allows for an epsilon-approximate gradient to be the convex combination of generalized gradients evaluated at points within distance delta to the solution. We propose a series of randomized first-order methods and analyze their complexity of finding a (delta, epsilon)-stationary point. Furthermore, we provide a lower bound and show that our stochastic algorithm has min-max optimal dependence on delta. Empirically, our methods perform well for training ReLU neural networks.

## Introduction

Gradient based optimization underlies most of machine learning and it has attracted tremendous research attention over the years. While non-asymptotic complexity analysis of gradient based methods is well-established for convex and *smooth* nonconvex problems, little is known for nonsmooth nonconvex problems. We summarize the known rates (black) in Table 1 based on the references.

Table 1: When the problem is nonconvex and nonsmooth, finding a ϵ-stationary point is intractable, see Theorem 11. Thus we introduce a refined notion, (δ,ϵ)-stationarity, and provide non-asymptotic convergence rates for finding (δ,ϵ)-stationary point.

Our results provide the first non-asymptotic analysis of nonconvex optimization algorithms in the general Lipschitz continuous setting. Yet, they also open further questions. The first question is whether the current dependence on $\epsilon$ in our complexity bound is optimal. A future research direction is to try to find provably faster algorithms or construct adversarial examples that close the gap between upper and lower bounds on $\epsilon$. Second, the rate we obtain in the deterministic case requires function evaluations and is randomized, leading to high probability bounds....

In addition to the open problems listed above, our work uncovers another very interesting observation. In the standard stochastic, nonconvex, and smooth setting, stochastic gradient descent is known to be theoretically optimal, while widely used practical techniques such as momentum-based and adaptive step size methods usually lead to worse theoretical convergence rates. In our proposed setting, momentum and adaptivity naturally show up in algorithm design, and become necessary for the convergence analysis....

Consequently, the two notions of stationarity are equivalent for differentiable functions. It is then natural to ask: *does $(\delta,\epsilon)$-stationarity permit a finite time analysis?*

### Lemma 4

To update the descent direction, we incorporate a randomized strategy. We randomly sample an interpolation point $y_{t,{k + 1}}$ on the segment $\lbrack x_{t},x_{t,k}\rbrack$ and evaluate the generalized gradient $g_{t,{k + 1}}$ at this random point $y_{t,{k + 1}}$. Then, we update the descent direction as a convex combination of $g_{t,{k + 1}}$ and the previous direction $m_{t,k}$....
