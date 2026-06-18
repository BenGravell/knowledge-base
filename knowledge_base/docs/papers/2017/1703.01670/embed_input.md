Control Interpretations for First-Order Optimization Methods

Topics include Optimization, Control, Learning.

First-order iterative optimization methods play a fundamental role in large scale optimization and machine learning. This paper presents control interpretations for such optimization methods. First, we give loop-shaping interpretations for several existing optimization methods and show that they are composed of basic control elements such as PID and lag compensators. Next, we apply the small gain theorem to draw a connection between the convergence rate analysis of optimization methods and the input-output gain computations of certain complementary sensitivity functions. These connections suggest that standard classical control synthesis tools may be brought to bear on the design of optimization algorithms.

## Introduction

First-order iterative optimization methods have been widely applied in data science and machine learning. These methods only require access to first-order derivative information, and iterate on the data until satisfactory convergence is achieved. For example, the gradient method is

Such simple methods are often favored over higher order methods such as Newton's method when the dimension of the underlying space is large and computing Hessians is prohibitively expensive.

This slight modification can yield a dramatic improvement in worst-case convergence rate if $f$ is quadratic. A similar acceleration scheme, *Nesterov's accelerated method*, can improve the convergence rate for strongly convex $f$ with smooth gradients. These convergence results are derived on a case-by-case basis, and the intuition behind the acceleration is still not fully understood.

Recent efforts have adopted a dynamical system (or differential equation) perspective in analyzing acceleration for convex objectives, though a more general understanding of acceleration is still lacking (non-convex objectives, inexact computations, etc). This paper aims to bring new insights on how to accelerate first-order optimization methods for objective functions which are not convex in general.

## Conclusion

This paper discussed connections between the analysis of optimization algorithms and classical control-theoretic concepts. Specifically, the gradient method, the Heavy-ball method, and Nesterov's accelerated method were interpreted as combinations of PID and lag compensators. A loop-shaping interpretation was also used to explain several well-known robustness properties of these algorithms.

We invoked the small gain theorem to show that finding worst-case convergence rates for algorithms amounts to computing the gain of a complementary sensitivity function. In addition, we demonstrated a connection between $\mathcal{H}_{\infty}$ state feedback synthesis and stepsize selections of the gradient method. These observations are an encouraging first step toward leveraging tools from control theory for the analysis and eventual synthesis of robust optimization algorithms.
