Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization

Topics include Convex optimization, Gradient descent, Optimization, II.

We provide a concise, self-contained proof that the Silver Stepsize Schedule proposed in Part I directly applies to smooth (non-strongly) convex optimization. Specifically, we show that with these stepsizes, gradient descent computes an epsilon-minimizer in O(epsilon^-log_rho 2) = O(epsilon^(-0).7864) iterations, where rho = 1+sqrt is the silver ratio. This is intermediate between the textbook unaccelerated rate O(epsilon^(-1)) and the accelerated rate O(1/sqrt(epsilon)) due to Nesterov in 1983. The Silver Stepsize Schedule is a simple explicit fractal: the i-th stepsize is 1+rho^(v)(i)-1 where v(i) is the 2-adic valuation of i. The design and analysis are conceptually identical to the strongly convex setting in Part I, but simplify remarkably in this specific setting.

## Introduction

We revisit the classical problem of smooth convex optimization: solve ${\min_{x \in {\mathbb{R}}^{d}}f}{(x)}$ where $f$ is convex and $M$-smooth (i.e., its gradient is $M$-Lipschitz). A celebrated result is that with a prudent choice of stepsizes $\{\alpha_{t}\}$, the gradient descent algorithm (GD)

solves such a convex optimization problem to arbitrary accuracy from any initialization $x_{0}$. How quickly does GD converge? The mainstream approach (see e.g., the textbooks among many others) is to use a constant stepsize schedule $\alpha_{t} \equiv \overline{\alpha} \in {}$ since this ensures

### Rate certificate

The identity (3.5. ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization")) has two components: a linear form in the function values and a quadratic form in the iterates and gradients. For the linear form, it suffices to verify ${e - s - \ell} = 0$ by Lemma 3.6. ‣ 3.1 Helper lemmas ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"), where ${e,s,\ell} \in {\mathbb{R}}^{3}$ are the vectors defined in Appendix A.1 ‣ Appendix A Deferred proof details ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule...

## Recursive gluing

### Rescaling

The "gluing component" $\Theta$ is defined as

The main question posed in Part I was: can we accelerate the convergence of GD without changing the algorithm---just by judiciously choosing the stepsizes? Here we continue to investigate this question, now in the setting of smooth convex optimization. Note that this is markedly different from classical approaches to acceleration---starting from Nesterov's seminal result of 1983, those approaches modify the basic GD algorithm by adding momentum, internal dynamics, or other additional building blocks beyond just changing the stepsizes....

### Contribution

Figure 1: Silver Stepsize schedule {α0, α1, α2, …}. See (2.1) for the definition. Only the first n = 63 values are shown (i.e., k = 8). The fractal-like stepsizes are non-monotonic and have increasingly large “spikes” α2k − 1 = 1 + ρk − 1.

This paper provides a concise, self-contained proof that the Silver Stepsize Schedule proposed in Part I directly applies to smooth (non-strongly) convex optimization....
