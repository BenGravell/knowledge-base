Super-Universal Regularized Newton Method

Topics include Universal regularized Newton method.

We analyze the performance of a variant of Newton method with quadratic regularization for solving composite convex minimization problems. At each step of our method, we choose regularization parameter proportional to a certain power of the gradient norm at the current point. We introduce a family of problem classes characterized by Hölder continuity of either the second or third derivative. Then we present the method with a simple adaptive search procedure allowing an automatic adjustment to the problem class with the best global complexity bounds, without knowing specific parameters of the problem. In particular, for the class of functions with Lipschitz continuous third derivative, we get the global O(1/k^) rate, which was previously attributed to third-order tensor methods. When the objective function is uniformly convex, we justify an automatic acceleration of our scheme, resulting in a faster global rate and local superlinear convergence. The switching between the different rates (sublinear, linear, and superlinear) is automatic. Again, for that, no a priori knowledge of parameters is needed.

## Introduction

### Motivation

Newton's method is one of the most important tools in Numerical Analysis and Continuous Optimization. It has a reputation for being a powerful algorithm, especially due to its ability to solve ill-conditioned problems. The method has a local quadratic convergence, thus converging extremely fast in a neighbourhood of the solution. However, the global behaviour of Newton's method has been remaining an active area of research for several decades.

Another important direction is the creation of methods that are suitable for non-Euclidean geometry. In our method we fix the Euclidean norm as a regularizer, while it is also possible to use for that a contraction of the feasible domain, leading to affine-invariant contracting-point methods, or an appropriate Bregman divergence (see also for the framework of relative smoothness).

For solving large-scale problems, our method can be equipped with modern stochastic techniques which are able to keep versatile convergence guarantees. Another potential way to make the methods more applicable to high-dimensional objectives is to consider quasi-Newton updates, which at the moment seems to be very challenging due to the lack of theoretical results on their global behavior.

## Super-Universal Method

For any ${\gamma,\nu} \in {\lbrack 0,1\rbrack}$, it holds:

iterations of Algorithm 2 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003).").

It is widely known that the classical Newton method with a unit stepsize may not converge globally, even if the problem is strongly convex (see, e.g., Example 1.4.3 in ). Consequently, there were many techniques developed for the method to improve its global behaviour, including damped Newton steps combined with line search strategies, Levenberg-Marquardt regularization, and trust-region approach....
