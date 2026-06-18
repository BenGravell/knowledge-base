Complexity of Finding Stationary Points of Nonsmooth Nonconvex Functions

We provide the first non-asymptotic analysis for finding stationary points of nonsmooth, nonconvex functions. In particular, we study the class of Hadamard semi-differentiable functions, perhaps the largest class of nonsmooth functions for which the chain rule of calculus holds. This class contains examples such as ReLU neural networks and others with non-differentiable activation functions. We first show that finding an epsilon-stationary point with first-order methods is impossible in finite time. We then introduce the notion of (delta, epsilon)-stationarity, which allows for an epsilon-approximate gradient to be the convex combination of generalized gradients evaluated at points within distance delta to the solution. We propose a series of randomized first-order methods and analyze their complexity of finding a (delta, epsilon)-stationary point. Furthermore, we provide a lower bound and show that our stochastic algorithm has min-max optimal dependence on delta. Empirically, our methods perform well for training ReLU neural networks.

## Introduction

Gradient based optimization underlies most of machine learning and it has attracted tremendous research attention over the years. While non-asymptotic complexity analysis of gradient based methods is well-established for convex and *smooth* nonconvex problems, little is known for nonsmooth nonconvex problems. We summarize the known rates (black) in Table 1 based on the references.

Within the nonsmooth nonconvex setting, recent research results have focused on asymptotic convergence analysis. Despite their advances, these results fail to address finite-time, non-asymptotic convergence rates. Given the widespread use of nonsmooth nonconvex problems in machine learning, a canonical example being deep ReLU neural networks, obtaining a *non-asymptotic* convergence analysis is an important open problem of fundamental interest.

We tackle this problem for nonsmooth functions that are Lipschitz and directionally differentiable. This class is rich enough to cover common machine learning problems, including ReLU neural networks. Surprisingly, even for this seemingly restricted class, finding an $\epsilon$-stationary point, i.e., a point $\overline{x}$ for which ${d{(0,{\partial{f{(\overline{x})}}})}} \leq \epsilon$, is intractable. In other words, no algorithm can guarantee to find an $\epsilon$-stationary point within a *finite* number of iterations.

This intractability suggests that, to obtain meaningful non-asymptotic results, we need to refine the notion of stationarity.

We show that a traditional $\epsilon$-stationary point cannot be obtained in finite time (Theorem 5).

We propose a normalized "gradient descent" style algorithm that achieves $\overset{\sim}{\mathcal{O}}{({\epsilon^{- 3}\delta^{- 1}})}$ complexity in finding a $(\delta,\epsilon)$-stationary point in the deterministic setting.

We propose a momentum based algorithm that achieves $\overset{\sim}{\mathcal{O}}{({\epsilon^{- 4}\delta^{- 1}})}$ complexity in finding a $(\delta,\epsilon)$-stationary point in the stochastic finite variance setting.
