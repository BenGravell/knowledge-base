Learning One-hidden-layer Neural Networks with Landscape Design

We consider the problem of learning a one-hidden-layer neural network: we assume the input xin R^(d) is from Gaussian distribution and the label y = a^(top) sigma(Bx) + xi, where a is a nonnegative vector in R^(m) with m <= d, Bin R^(mx) d is a full-rank weight matrix, and xi is a noise vector. We first give an analytic formula for the population risk of the standard squared loss and demonstrate that it implicitly attempts to decompose a sequence of low-rank tensors simultaneously. Inspired by the formula, we design a non-convex objective function G(*) whose landscape is guaranteed to have the following properties: 1. All local minima of G are also global minima. 2. All global minima of G correspond to the ground truth parameters. 3. The value and gradient of G can be estimated using samples. With these properties, stochastic gradient descent on G provably converges to the global minimum and learn the ground-truth parameters. We also prove finite sample complexity result and validate the results by simulations.

## Introduction

Scalable optimization has been playing crucial roles in the success of deep learning, which has immense applications in artificial intelligence. Remarkably, optimization issues are often addressed through designing new models that make the resulting training objective functions easier to be optimized. For example, over-parameterization \[\], batch-normalization \[\], and residual networks are often considered as ways to improve the optimization landscape of the resulting objective functions.

How do we design models and objective functions that allow efficient optimization with guarantees? Towards understanding this question in a principled way, this paper studies learning neural networks with one hidden layer. Roughly speaking, we will show that when the input is from Gaussian distribution and under certain simplifying assumptions on the weights, we can design an objective function $G{( \cdot )}$, such that\

We conjecture that the objective ${\alphaf_{2}} + {\betaf_{4}}$ has no spurious local minimum when $\alpha,\beta$ are reasonable constants and the ground-truth parameters are in general position^1313^13See equation (2.4) for the definition of $f_{k}$ and Theorem 2.2 for how to access ${\alphaf_{2}} + {\betaf_{4}}$ in the setting of one-hidden-layer neural nets.. We provided empirical evidence to support the conjecture.

Our results assume that the input distribution is Gaussian. Extending them to other input distributions is a very interesting open problem.

### Analytic Formula for population risk $f$ and $f^{\prime}$

Here ${\hat{\sigma}}_{k}$ and ${\hat{\gamma}}_{k}$ are the $k$-th Hermite coefficient of the function $\sigma$ and $\gamma$. That is, letting $h_{k}$ the $k$-th normalized probabilists' Hermite polynomials \[\] and $\langle \cdot, \cdot \rangle$ be the standard inner product between functions, we have ${\hat{\sigma}}_{k} = {\langle h_{k},\sigma\rangle}$.

Note that our variable $B$ is a matrix of dimension $d \times d$ and we use $b_{i}$ to denote the rows of $B$, that is, $B = \begin{bmatrix}
\end{bmatrix}$. Naturally, towards analyzing the properties of a local minimum $B$, the first step is that we pick a row $b_{s}$ of $B$ and treat only $b_{s}$ as variables and others rows as fixed....
