A Regularized Newton Method for Nonconvex Optimization with Global and Local Complexity Guarantees

Topics include Convex optimization, Nonconvex optimization, Neural networks, Optimization.

Finding an epsilon-stationary point of a nonconvex function with a Lipschitz continuous Hessian is a central problem in optimization. Regularized Newton methods are a classical tool and have been studied extensively, yet they still face a trade-off between global and local convergence. Whether a parameter-free algorithm of this type can simultaneously achieve optimal global complexity and quadratic local convergence remains an open question. To bridge this long-standing gap, we propose a new class of regularizers constructed from the current and previous gradients, and leverage the conjugate gradient approach with a negative curvature monitor to solve the regularized Newton equation. The proposed algorithm is adaptive, requiring no prior knowledge of the Hessian Lipschitz constant, and achieves a global complexity of O(epsilon^(-3/2)) in terms of the second-order oracle calls, and tildeO(epsilon^(-7/4)) for Hessian-vector products, respectively. When the iterates converge to a point where the Hessian is positive definite, the method exhibits quadratic local convergence....

## Introduction

We focus on the nonconvex optimization problem

where $\varphi:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is twice differentiable function with globally Lipschitz continuous Hessian. Since finding a global minimum is generally difficult, the typical goal is to instead find an $\epsilon$-stationary point $x^{\ast}$ such that ${\|{{\nabla\varphi}{(x^{\ast})}}\|} \leq \epsilon$ for arbitrary $\epsilon > 0$.

It would also be interesting to investigate whether these regularizers are suitable for the convex settings studied in Doikov and Nesterov; Doikov et al. and whether they can be extended to inexact methods such as Yao et al. and stochastic optimization.

Y. Zhou and J. Zhu are supported by the National Natural Science Foundation of China (Nos. 92270001, 62350080, 62106120), Tsinghua Institute for Guo Qiang, and the High Performance Computing Center, Tsinghua University; J. Zhu was also supported by the XPlorer Prize. C. Bao is supported by the National Key R&D Program of China (No. 2021YFA1001300) and the National Natural Science Foundation of China (No. 12271291). J. Xu is supported in part by PolyU postdoc matching fund scheme of the Hong Kong Polytechnic University (No....

It is worth noting that, previous to Royer et al., a linesearch method with negative detection was proposed by Royer and Wright. For convex problems, damped Newton methods achieving fast rates have also been developed, and the method of Jiang et al. can also be applied.

thm:newton-local-rate-boosted,thm:newton-local-rate-boosted-oracle-complexity summarize our main results, and \\tablereftab:rate-comparision-for-rmn compares them with other regularized Newton methods for nonconvex optimization. All parameters aside from the regularizers can be chosen arbitrarily, provided they satisfy the requirements in Table 2.1.

The following lemma characterizes the overall decrease of the function within a subsequence. It roughly states that there are at most $O\left( {\log{\log\frac{g_{\ell_{j}}}{g_{k}}}} \right)$ iterations with insufficient descent in the subsequence $I_{\ell_{j},\ell_{j + 1}}$, since otherwise the gradient decreases superlinearly below $g_{k}$.

The Newton-type method is one of the most powerful tools for solving such problems, known for its quadratic local convergence near a solution with positive definite Hessian....
