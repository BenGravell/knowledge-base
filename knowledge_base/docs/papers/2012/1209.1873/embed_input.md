Stochastic Dual Coordinate Ascent Methods for Regularized Loss Minimization

Topics include Stochastic dual coordinate ascent, Variance reduction, Empirical risk minimization, Convex optimization, Coordinate ascent, Support vector machine, Regularized loss minimization.

Reanalyzes stochastic dual coordinate ascent for regularized empirical-risk objectives and establishes strong convergence guarantees comparable to or better than stochastic gradient descent. The paper helped make SDCA a canonical variance-reduced finite-sum method, especially for linear supervised-learning problems with convex losses and explicit regularization.

Stochastic Gradient Descent (SGD) has become popular for solving large scale supervised machine learning optimization problems such as SVM, due to their strong theoretical guarantees. While the closely related Dual Coordinate Ascent (DCA) method has been implemented in various software packages, it has so far lacked good convergence analysis. This paper presents a new analysis of Stochastic Dual Coordinate Ascent (SDCA) showing that this class of methods enjoy strong theoretical guarantees that are comparable or better than SGD. This analysis justifies the effectiveness of SDCA for practical applications.

## Introduction

We consider the following generic optimization problem associated with regularized loss minimization of linear predictors: Let $x_{1},\ldots,x_{n}$ be vectors in ${\mathbb{R}}^{d}$, let $\phi_{1},\ldots,\phi_{n}$ be a sequence of scalar convex functions, and let $\lambda > 0$ be a regularization parameter. Our goal is to solve ${\min_{w \in {\mathbb{R}}^{d}}P}{(w)}$ where^11^1Throughout this paper, we only consider the $\ell_{2}$-norm.

Let $w^{\ast}$ be the optimum of. We say that a solution $w$ is $\epsilon_{P}$-sub-optimal if ${{P{(w)}} - {P{(w^{\ast})}}} \leq \epsilon_{P}$. We analyze the runtime of optimization procedures as a function of the time required to find an $\epsilon_{P}$-sub-optimal solution.

A simple approach for solving SVM is stochastic gradient descent (SGD). SGD finds an $\epsilon_{P}$-sub-optimal solution in time $\overset{\sim}{O}{({1/{({\lambda\epsilon_{P}})}})}$. This runtime does not depend on $n$ and therefore is favorable when $n$ is very large. However, the SGD approach has several disadvantages. It does not have a clear stopping criterion; it tends to be too aggressive at the beginning of the optimization process, especially when $\lambda$ is very small; while SGD reaches a moderate accuracy quite fast, its convergence becomes rather slow when we are interested in more accurate solutions.

The dual objective in has a different dual variable associated with each example in the training set. At each iteration of DCA, the dual objective is optimized with respect to a single dual variable, while the rest of the dual variables are kept in tact.

We focus on a *stochastic* version of DCA, abbreviated by SDCA, in which at each round we choose which dual coordinate to optimize uniformly at random. The purpose of this paper is to develop theoretical understanding of the convergence of the duality gap for SDCA.
