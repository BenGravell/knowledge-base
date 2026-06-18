Small Errors in Random Zeroth-order Optimization Are Imaginary

Topics include Optimization.

Most zeroth-order optimization algorithms mimic a first-order algorithm but replace the gradient of the objective function with some gradient estimator that can be computed from a small number of function evaluations. This estimator is constructed randomly, and its expectation matches the gradient of a smooth approximation of the objective function whose quality improves as the underlying smoothing parameter delta is reduced. Gradient estimators requiring a smaller number of function evaluations are preferable from a computational point of view. While estimators based on a single function evaluation can be obtained by use of the divergence theorem from vector calculus, their variance explodes as delta tends to 0. Estimators based on multiple function evaluations, on the other hand, suffer from numerical cancellation when delta tends to 0. To combat both effects simultaneously, we extend the objective function to the complex domain and construct a gradient estimator that evaluates the objective at a complex point whose coordinates have small imaginary parts of the order delta. As this estimator requires only one function evaluation, it is immune to cancellation.

## Introduction

We study optimization problems of the form

where $f:{\mathcal{D}\rightarrow{\mathbb{R}}}$ is a real analytic and thus smooth objective function defined on an open set $\mathcal{D} \subseteq {\mathbb{R}}^{n}$, and $\mathcal{X} \subseteq \mathcal{D}$ is a non-empty closed feasible set. Throughout the paper we assume that problem (1.1) admits a global minimizer $x^{\star}$ and that the objective function $f$ can only be accessed through a deterministic zeroth-order oracle, which outputs function evaluations at prescribed test points.

Zeroth-order optimization algorithms are needed when problem (1.1) cannot be addressed with first- or higher-order methods. This is the case when there is no simple closed-form expression for $f$ and its partial derivatives or when evaluating the gradient of $f$ is expensive. In simulation-based optimization, for example, the function $f$ can be evaluated via offline or online simulation methods, but its gradient is commonly inaccessible. Zeroth-order optimization algorithms can also be used for addressing minimax, bandit or reinforcement learning problems, and they lend themselves for hyperparameter tuning in supervised learning \[ \].

Zeroth-order optimization algorithms can be categorized into direct search methods, model-based methods and random search methods. Direct search methods evaluate the objective function at a set of trial points without the goal of approximating the gradient. A representative example of a direct search method is the popular Nelder--Mead algorithm.

Inspired by techniques for numerically differentiating analytic functions, we propose here a new smoothed approximation $f_{\delta}$ as well as a corresponding stochastic gradient estimator $g_{\delta}$ that can be evaluated rapidly and faithfully for arbitrarily small values of $\delta$ without suffering from cancellation effects. Integrating the new estimator into the gradient-descent-type algorithm
