Universal Convexification via Risk-Aversion

We develop a framework for convexifying a fairly general class of optimization problems. Under additional assumptions, we analyze the suboptimality of the solution to the convexified problem relative to the original nonconvex problem and prove additive approximation guarantees. We then develop algorithms based on stochastic gradient methods to solve the resulting optimization problems and show bounds on convergence rates. %We show a simple application of this framework to supervised learning, where one can perform integration explicitly and can use standard (non-stochastic) optimization algorithms with better convergence guarantees. We then extend this framework to apply to a general class of discrete-time dynamical systems. In this context, our convexification approach falls under the well-studied paradigm of risk-sensitive Markov Decision Processes. We derive the first known model-based and model-free policy gradient optimization algorithms with guaranteed convergence to the optimal solution. Finally, we present numerical results validating our formulation in different applications.

## INTRODUCTION

It has been said that the "the great watershed in optimization isn't between linearity and nonlinearity, but convexity and nonconvexity". In this paper, we describe a framework for convexifying a fairly general class of optimization problems (section 3), turning them into problems that can be solved with efficient convergence guarantees. The convexification approach may change the problem drastically in some cases, which is not surprising since most nonconvex optimization problems are NP-hard and cannot be reduced to solving convex optimization problems....

### RELATED WORK

## CONCLUSION AND FUTURE WORK

We have developed a general framework for convexifying a broad class of optimization problems, analysis that relates the solution of the convexified problem to the original one and given algorithms with convergence rate guarantees to solve the convexified problems. Extending the framework to dynamical systems, we derive the first approach to policy optimization with optimality and convergence rate guarantees. We validated our approach numerically on problems of binary classification and training neural networks. In future work, we will refine the suboptimality analysis for our convexification approach....

### Stochastic Gradient Methods with Convergence Guarantees

### Theorem 3.2 (Suboptimality Analysis)

### Problem Setup

Smoothing with noise is a relatively common approach that has been used extensively in various applications to simplify difficult optimization problems. It has been used in computer vision heuristically and formalized in recent work where it is shown that under certain assumptions, adding sufficient noise eventually leads to a convex optimization problem. In this work, however, we show that for any noise level, one can choose the degree of risk-aversion in order to obtain a convex problem....

## NOTATION

Gaussian random variables are denoted by $\omega \sim {\mathcal{N}(\mu,\Sigma)}$, where $\mu$ is the mean and $\Sigma$ the covariance matrix. Given a random variable $\omega \in \Omega$ with distribution $P$ and a function $h:{\Omega\mapsto\mathbf{R}}$, the expected value of the random variable $h(\omega)$ is written as $\underset{\omega \sim P}{E}\left\lbrack {h(\omega)} \right\rbrack$....
