Understanding the Acceleration Phenomenon via High-Resolution Differential Equations

Gradient-based optimization algorithms can be studied from the perspective of limiting ordinary differential equations (ODEs). Motivated by the fact that existing ODEs do not distinguish between two fundamentally different algorithms - Nesterov's accelerated gradient method for strongly convex functions (NAG-SC) and Polyak's heavy-ball method - we study an alternative limiting process that yields high-resolution ODEs. We show that these ODEs permit a general Lyapunov function framework for the analysis of convergence in both continuous and discrete time. We also show that these ODEs are more accurate surrogates for the underlying algorithms; in particular, they not only distinguish between NAG-SC and Polyak's heavy-ball method, but they allow the identification of a term that we refer to as "gradient correction" that is present in NAG-SC but not in the heavy-ball method and is responsible for the qualitative difference in convergence of the two methods....

## Introduction

Machine learning has become one of the major application areas for optimization algorithms during the past decade. While there have been many kinds of applications, to a wide variety of problems, the most prominent applications have involved large-scale problems in which the objective function is the sum over terms associated with individual data, such that stochastic gradients can be computed cheaply, while gradients are much more expensive and the computation (and/or storage) of Hessians is often infeasible....

We will be considering unconstrained minimization problems,

with $\beta = 0$ and $\beta = 1$, respectively. This ODE with a general $0 < \beta < 1$ corresponds to a new algorithm that can be thought of as an interpolation between the two methods. It is of interest to investigate the convergence properties of this class of algorithms. Second, we recognize that new optimization algorithms are obtained in by using different discretization schemes on low-resolution ODE. Hence, a direction of interest is to apply the techniques therein to our high-resolution ODEs and to explore possible appealing properties of the new methods....

More broadly, we wish to remark on possible extensions of the high-resolution ODE framework beyond smooth convex optimization in the Euclidean setting. In the non-Euclidean case, it would be interesting to derive a high-resolution ODE for mirror descent. This framework might also admit extensions to non-smooth optimization and stochastic optimization, where the ODEs are replaced, respectively, by differential inclusions \[ORX^+^16, \] and stochastic differential equations \[ HMC^+^18, \]....

### Theorem 4 (Convergence of heavy-ball method)

### Lemma 3.1 (Lyapunov function for NAG-SC ODE)

This bound reduces to the one claimed by Theorem 5 by only keeping the first term ${\sqrt{s}{({t^{3} - t_{0}^{3}})}}/3$ in the denominator.

where $f$ is a smooth convex function. Perhaps the simplest first-order method for solving this problem is gradient descent. Taking a fixed step size $s$, gradient descent is implemented as the recursive rule

As has been known at least since the advent of conjugate gradient algorithms, improvements to gradient descent can be obtained within a first-order framework by using the history of past gradients....
