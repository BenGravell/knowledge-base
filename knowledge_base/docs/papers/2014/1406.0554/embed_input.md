Universal Convexification via Risk-Aversion

We develop a framework for convexifying a fairly general class of optimization problems. Under additional assumptions, we analyze the suboptimality of the solution to the convexified problem relative to the original nonconvex problem and prove additive approximation guarantees. We then develop algorithms based on stochastic gradient methods to solve the resulting optimization problems and show bounds on convergence rates. %We show a simple application of this framework to supervised learning, where one can perform integration explicitly and can use standard (non-stochastic) optimization algorithms with better convergence guarantees. We then extend this framework to apply to a general class of discrete-time dynamical systems. In this context, our convexification approach falls under the well-studied paradigm of risk-sensitive Markov Decision Processes. We derive the first known model-based and model-free policy gradient optimization algorithms with guaranteed convergence to the optimal solution. Finally, we present numerical results validating our formulation in different applications.

## INTRODUCTION

It has been said that the "the great watershed in optimization isn't between linearity and nonlinearity, but convexity and nonconvexity". In this paper, we describe a framework for convexifying a fairly general class of optimization problems (section 3), turning them into problems that can be solved with efficient convergence guarantees. The convexification approach may change the problem drastically in some cases, which is not surprising since most nonconvex optimization problems are NP-hard and cannot be reduced to solving convex optimization problems.

## GENERAL OPTIMIZATION PROBLEMS

We

where $g$ is an arbitrary function and $\mathcal{C} \subset \mathbf{R}^{k}$ is a convex set. We do not assume that $g$ is convex so the above problem could be a nonconvex optimization problem. In this work, we convexify this problem by decomposing $g(\theta)$ as follows: ${g{(\theta)}} = {{f{(\theta)}} + {\frac{1}{2}\theta^{T}R\theta}}$ and perturbing $f$ with Gaussian noise. Optimization problems of this form are very common in machine learning (where $R$ corresponds to a regularizer) and control (where $R$ corresponds to a control cost).

This kind of objective is common in risk-averse optimization. To a first order Taylor expansion in $\alpha$, the above objective is equal to ${E\left\lbrack {f\left( {\theta + \omega} \right)} \right\rbrack} + {\alpha{\operatorname{Var}\left( {f\left( {\theta + \omega} \right)} \right)}}$, indicating that increasing $\alpha$ will make the solution more robust to Gaussian perturbations. $\alpha$ is called the risk-factor and is a measure of the risk-aversion of the decision maker. Larger values of $\alpha$ will reject solutions that are not robust to Gaussian perturbations.

## CONCLUSION AND FUTURE WORK

We have developed a general framework for convexifying a broad class of optimization problems, analysis that relates the solution of the convexified problem to the original one and given algorithms with convergence rate guarantees to solve the convexified problems. Extending the framework to dynamical systems, we derive the first approach to policy optimization with optimality and convergence rate guarantees. We validated our approach numerically on problems of binary classification and training neural networks. In future work, we will refine the suboptimality analysis for our convexification approach.
