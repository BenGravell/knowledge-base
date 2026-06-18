Learning One-hidden-layer Neural Networks with Landscape Design

We consider the problem of learning a one-hidden-layer neural network: we assume the input xin R^(d) is from Gaussian distribution and the label y = a^(top) sigma(Bx) + xi, where a is a nonnegative vector in R^(m) with m <= d, Bin R^(mx) d is a full-rank weight matrix, and xi is a noise vector. We first give an analytic formula for the population risk of the standard squared loss and demonstrate that it implicitly attempts to decompose a sequence of low-rank tensors simultaneously. Inspired by the formula, we design a non-convex objective function G(*) whose landscape is guaranteed to have the following properties: 1. All local minima of G are also global minima. 2. All global minima of G correspond to the ground truth parameters. 3. The value and gradient of G can be estimated using samples. With these properties, stochastic gradient descent on G provably converges to the global minimum and learn the ground-truth parameters. We also prove finite sample complexity result and validate the results by simulations.

## Introduction

Scalable optimization has been playing crucial roles in the success of deep learning, which has immense applications in artificial intelligence. Remarkably, optimization issues are often addressed through designing new models that make the resulting training objective functions easier to be optimized. For example, over-parameterization, batch-normalization, and residual networks are often considered as ways to improve the optimization landscape of the resulting objective functions.

How do we design models and objective functions that allow efficient optimization with guarantees? Towards understanding this question in a principled way, this paper studies learning neural networks with one hidden layer. Roughly speaking, we will show that when the input is from Gaussian distribution and under certain simplifying assumptions on the weights, we can design an objective function $G{( \cdot )}$, such that\

\[a\] all local minima of $G{( \cdot )}$ are global minima\

\[b\] all the global minima are the desired solutions, namely, the ground-truth parameters (up to permutation and some fixed transformation).

## Conclusion

In this paper we first give an analytic formula for the population risk of the standard $\ell_{2}$ loss, which empirically may converge to a spurious local minimum. We then design a novel population loss that is guaranteed to have no spurious local minimum.

Designing objective functions with well-behaved landscape is an intriguing and fruitful direction. We hope that our techniques can be useful for characterizing and designing the optimization landscape for other settings.
