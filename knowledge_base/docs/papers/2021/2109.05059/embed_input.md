The Speed-Robustness Trade-Off for First-Order Methods with Additive Gradient Noise

Topics include Gradient descent, Robustness, Optimization, GD, S heavy Ball, HB, S Fast gradient, FG, Convex function.

We study the trade-off between convergence rate and sensitivity to stochastic additive gradient noise for first-order optimization methods. Ordinary Gradient Descent (GD) can be made fast-and-sensitive or slow-and-robust by increasing or decreasing the stepsize, respectively. However, it is not clear how such a trade-off can be navigated when working with accelerated methods such as Polyak's Heavy Ball (HB) or Nesterov's Fast Gradient (FG) methods. We consider two classes of functions: strongly convex quadratics and smooth strongly convex functions. For each function class, we present a tractable way to compute the convergence rate and sensitivity to additive gradient noise for a broad family of first-order methods, and we present algorithm designs that trade off these competing performance metrics. Each design consists of a simple analytic update rule with two states of memory, similar to HB and FG. Moreover, each design has a scalar tuning parameter that explicitly trades off convergence rate and sensitivity to additive gradient noise.

## Introduction

We consider the problem of designing robust first-order methods for unconstrained minimization. Given a continuously differentiable function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$, consider solving the optimization problem

where the algorithm only has access to gradient measurements corrupted by additive stochastic noise.^11^1Preliminary versions of portions of this work appeared in the conference proceedings. Specifically, the algorithm can sample the oracle ${g{(x)}}{: =}{{{\nabla f}{(x)}} + w}$, where $w$ is zero-mean and independent across queries. This form of additive noise arises in various applications.

Many iterative algorithms have been proposed to solve this problem, and most have tunable parameters. For example, Gradient Descent (GD) uses the update

where $t$ is the iteration index and the stepsize $\alpha$ is a tunable parameter. Fig. 1 illustrates how the error $\parallel{x^{t} - x^{\star}}\parallel$ evolves under GD applied to strongly convex quadratic functions for different fixed $\alpha$. The convergence of the error is characterized by an initial transient phase followed by a stationary phase. In the transient phase, the gradient dominates the noise, and the error converges at a linear rate. When the gradient is small enough that the noise becomes significant, the average error of the iterates converges to a constant value.

Gradient Descent is easy to interpret and tune: the stepsize directly mediates the trade-off between convergence rate and sensitivity. Unfortunately, GD is generally slow to converge, and alternative methods can provide faster convergence rates. Two such methods are Polyak's Heavy Ball and Nesterov's Fast Gradient, which use the updates
