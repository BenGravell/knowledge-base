Gradient Descent Converges to Minimizers

Topics include Gradient descent.

We show that gradient descent converges to a local minimizer, almost surely with random initialization. This is proved by applying the Stable Manifold Theorem from dynamical systems theory.

## Introduction

Saddle points have long been regarded as a tremendous obstacle for continuous optimization. There are many well known examples when worst case initialization of gradient descent provably converge to saddle points \[20, Section 1.2.3\], and hardness results which show that finding even a *local* minimizer of non-convex functions is NP-Hard in the worst case. However, such worst-case analyses have not daunted practitioners, and high quality solutions of continuous optimization problems are readily found by a variety of simple algorithms....

More precisely, let $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ be twice continuously differentiable, and consider the classic gradient method with constant step size $\alpha$:

However, we note that there are very difficult unconstrained optimization problems where the strict saddle condition fails. Perhaps the simplest is optimization of quartic polynomials. Indeed, checking if $0$ is a local minimizer of the quartic

is equivalent to checking whether the matrix $Q = {\lbrack q_{ij}\rbrack}$ is co-positive, a co-NP complete problem. For this $f$, the Hessian at $x = 0$ is zero. Interestingly, the strict saddle property failing is analogous in dynamical systems to the existence of a *slow manifold* where complex dynamics may emerge. Slow manifolds give rise to metastability, bifurcation, and other chaotic dynamics, and it would be intriguing to see how the analysis of chaotic systems could be applied to understand the behavior of optimization algorithms around these difficult critical points.

When $\lim_{k}x_{k}$ does not exist, the above theorem is trivially true.

The gradient method is guaranteed to converge with a constant step size provided $0 < \alpha < \frac{2}{L}$. For this quadratic $f$, $L$ is equal to $\max{|\lambda_{i}|}$. Suppose $\alpha < {1/L}$, a slightly stronger condition. Then we will have ${({1 - {\alpha\lambda_{i}}})} < 1$ for $i \leq k$ and ${({1 - {\alpha\lambda_{i}}})} > 1$ for $i > k$. If $x_{0} \in E_{s}:={{span}{(e_{1},\ldots,e_{k})}}$, then $x_{k}$ converges to the saddle point at $0$ since ${({1 - {\alpha\lambda_{i}}})}^{k + 1}\rightarrow 0$. However, if $x_{0}$ has a component outside $E_{s}$ then gradient descent diverges to $\infty$....

### Further consequences of Theorem 4.1
