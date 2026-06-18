A Regularized Newton Method for Nonconvex Optimization with Global and Local Complexity Guarantees

Topics include Convex optimization, Nonconvex optimization, Neural networks, Optimization.

Finding an epsilon-stationary point of a nonconvex function with a Lipschitz continuous Hessian is a central problem in optimization. Regularized Newton methods are a classical tool and have been studied extensively, yet they still face a trade-off between global and local convergence. Whether a parameter-free algorithm of this type can simultaneously achieve optimal global complexity and quadratic local convergence remains an open question. To bridge this long-standing gap, we propose a new class of regularizers constructed from the current and previous gradients, and leverage the conjugate gradient approach with a negative curvature monitor to solve the regularized Newton equation. The proposed algorithm is adaptive, requiring no prior knowledge of the Hessian Lipschitz constant, and achieves a global complexity of O(epsilon^(-3/2)) in terms of the second-order oracle calls, and tildeO(epsilon^(-7/4)) for Hessian-vector products, respectively. When the iterates converge to a point where the Hessian is positive definite, the method exhibits quadratic local convergence.

## Introduction

We focus on the nonconvex optimization problem

where $\varphi:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is twice differentiable function with globally Lipschitz continuous Hessian. Since finding a global minimum is generally difficult, the typical goal is to instead find an $\epsilon$-stationary point $x^{\ast}$ such that ${\|{{\nabla\varphi}{(x^{\ast})}}\|} \leq \epsilon$ for arbitrary $\epsilon > 0$.

The Newton-type method is one of the most powerful tools for solving such problems, known for its quadratic local convergence near a solution with positive definite Hessian.

Although this method enjoys a quadratic local rate, it is well-known that it may fail to converge globally (i.e., converge from any initial point) even for a strongly convex function. Various globalization techniques have been developed to ensure global convergence by introducing regularization or constraints in (1.2) to adjust the direction $d_{k}$, including Levenberg-Marquardt regularization, trust-region methods, and damped Newton methods with a linesearch procedure.

However, the original versions of these approaches exhibit a slow $O{(\epsilon^{- 2})}$ worst-case performance, leading to extensive efforts to improve the global complexity of second-order methods. Among these, the cubic regularization method overcomes this issue and achieves an iteration complexity of $O{(\epsilon^{- \frac{3}{2}})}$, which has been shown to be optimal, while retaining the quadratic local rate.

The remaining parts of this article are organized as follows: We list the notations used throughout the paper below. Some background, our main results and related works are provided in Section 2. The ideas and techniques underlying our method are presented in Section 3, and the detailed proofs are deferred to the appendix. Finally, we present some preliminary numerical results to illustrate the performance of our algorithm in Section 4, and discuss potential directions in Section 5.
