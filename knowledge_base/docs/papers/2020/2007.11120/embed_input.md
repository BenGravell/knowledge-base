On Linear Convergence of Policy Gradient Methods for Finite MDPs

Topics include Policy iteration, Optimization, Policy gradients.

We revisit the finite time analysis of policy gradient methods in the one of the simplest settings: finite state and action MDPs with a policy class consisting of all stochastic policies and with exact gradient evaluations. There has been some recent work viewing this setting as an instance of smooth non-linear optimization problems and showing sub-linear convergence rates with small step-sizes. Here, we take a different perspective based on connections with policy iteration and show that many variants of policy gradient methods succeed with large step-sizes and attain a linear rate of convergence.

## Introduction

Policy gradient methods, dating back to the works of, along with their modern variants, have emerged as one of the most effective classes of algorithms for solving challenging reinforcement learning problems with impressive empirical success. Despite this, little was known about their global convergence properties, as these methods search over a parameterized class of policies by performing (stochastic) gradient descent on a scalar loss function that is typically non-convex.

This has changed recently with several recent papers analysing the global convergence properties of policy gradient methods. Our earlier work identifies properties for general MDPs which guarantee that (despite non-convexity) the optimization landscape does not suffer from spurious local optima, thereby implying convergence of policy gradient methods to globally optimal solutions. Though that work does not consider specific algorithms, some convergence rates for follow easily from the framework (e.g. a sub-linear convergence rate for tabular MDPs using projected gradient descent with natural parameterization).

For finite MDPs, we show that this leads to an extremely simple analysis covering many different first-order methods applied to the policy gradient objective, including projected gradient descent, Frank-Wolfe, mirror descent, and natural gradient descent. In an idealized setting where step-sizes are set by line search, a one paragraph proof applies to all algorithms. For natural gradient algorithms, a slightly longer calculation studies a specific step-size sequence. In the final section of this paper, we also discuss a setting of approximate line search as well as natural gradient methods with entropy regularization.

## Discussion of results

The following discussion is based primarily on feedback of the reviewers. We thank them for their valuable inputs.

Dependence on $\rho_{\min}$ for exact line search result:\
Readers will note that proof of our result in part (a) of Theorem 1. ‣ 6 Main result: geometric convergence") also shows that,
