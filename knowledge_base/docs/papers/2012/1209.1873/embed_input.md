Stochastic Dual Coordinate Ascent Methods for Regularized Loss Minimization

Topics include Stochastic dual coordinate ascent, Variance reduction, Empirical risk minimization, Convex optimization, Coordinate ascent, Support vector machine, Regularized loss minimization.

Reanalyzes stochastic dual coordinate ascent for regularized empirical-risk objectives and establishes strong convergence guarantees comparable to or better than stochastic gradient descent. The paper helped make SDCA a canonical variance-reduced finite-sum method, especially for linear supervised-learning problems with convex losses and explicit regularization.

Stochastic Gradient Descent (SGD) has become popular for solving large scale supervised machine learning optimization problems such as SVM, due to their strong theoretical guarantees. While the closely related Dual Coordinate Ascent (DCA) method has been implemented in various software packages, it has so far lacked good convergence analysis. This paper presents a new analysis of Stochastic Dual Coordinate Ascent (SDCA) showing that this class of methods enjoy strong theoretical guarantees that are comparable or better than SGD. This analysis justifies the effectiveness of SDCA for practical applications.

## Introduction

We consider the following generic optimization problem associated with regularized loss minimization of linear predictors: Let $x_{1},\ldots,x_{n}$ be vectors in ${\mathbb{R}}^{d}$, let $\phi_{1},\ldots,\phi_{n}$ be a sequence of scalar convex functions, and let $\lambda > 0$ be a regularization parameter. Our goal is to solve ${\min_{w \in {\mathbb{R}}^{d}}P}{(w)}$ where^11^1Throughout this paper, we only consider the $\ell_{2}$-norm.

Let $w^{\ast}$ be the optimum of. We say that a solution $w$ is $\epsilon_{P}$-sub-optimal if ${{P{(w)}} - {P{(w^{\ast})}}} \leq \epsilon_{P}$. We analyze the runtime of optimization procedures as a function of the time required to find an $\epsilon_{P}$-sub-optimal solution.

In Figure 8 we compare the zero-one test error of SDCA, when working with the smooth hinge-loss ($\gamma = 1$) to the zero-one test error of SGD, when working with the non-smooth hinge-loss. As can be seen, SDCA with the smooth hinge-loss achieves the smallest zero-one test error faster than SGD.

Figure 8: Comparing the test error of SDCA with the smoothed hinge-loss (γ = 1) to the test error of SGD with the non-smoothed hinge-loss. In all plots the vertical axis is the zero-one error on the test set and the horizontal axis is the number of iterations divided by training set size (corresponding to the number of epochs through the data). We terminated SDCA when the duality gap was smaller than 10−5.

For the smoothed hinge loss, step (\*) in Procedure SDCA-Perm has a closed form solution as

### Remark 8

Similar argument holds for $\alpha < {- L}$. \

A simple approach for solving SVM is stochastic gradient descent (SGD). SGD finds an $\epsilon_{P}$-sub-optimal solution in time $\overset{\sim}{O}{({1/{({\lambda\epsilon_{P}})}})}$. This runtime does not depend on $n$ and therefore is favorable when $n$ is very large. However, the SGD approach has several disadvantages. It does not have a clear stopping criterion; it tends to be too aggressive at the beginning of the optimization process, especially when $\lambda$ is very small; while SGD reaches a moderate accuracy quite fast, its convergence becomes rather slow when we are interested in more accurate solutions.

The dual objective in has a different dual variable associated with each example in the training set....
