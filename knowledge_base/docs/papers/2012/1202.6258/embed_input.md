A Stochastic Gradient Method with an Exponential Convergence Rate for Finite Training Sets

Topics include Stochastic average gradient, Variance reduction, Finite-sum optimization, Linear convergence, Convex optimization, Empirical risk minimization, Incremental gradient methods.

Introduces the stochastic average gradient method, which stores the most recent gradient for each finite-sum component and averages those stored gradients to obtain a low-cost update with linear convergence on strongly convex objectives. It is one of the first modern variance-reduction methods showing that finite training sets permit faster rates than black-box stochastic gradient assumptions allow.

We propose a new stochastic gradient method for optimizing the sum of a finite set of smooth functions, where the sum is strongly convex. While standard stochastic gradient methods converge at sublinear rates for this problem, the proposed method incorporates a memory of previous gradient values in order to achieve a linear convergence rate. In a machine learning context, numerical experiments indicate that the new algorithm can dramatically outperform standard algorithms, both in terms of optimizing the training error and reducing the test error quickly.

## Introduction

A plethora of the problems arising in machine learning involve computing an approximate minimizer of the sum of a loss function over a large number of training examples, where there is a large amount of redundancy between examples. The most wildly successful class of algorithms for taking advantage of this type of problem structure are *stochastic gradient* (SG) methods Robbins and Monro; Bottou and LeCun. Although the theory behind SG methods allows them to be applied more generally, in the context of machine learning SG methods are typically used to solve the problem of optimizing a sample average over a finite training set, i.e.,

In this work, we focus on such *finite training data* problems where each $f_{i}$ is *smooth* and the average function $g$ is *strongly-convex*.

Training cost vs. testing cost: The theoretical contribution of this work is limited to the convergence rate of the training cost. Though there are several settings where this is the metric of interest (e.g., variational inference in graphical models), in many cases one will be interested in the convergence speed of the testing cost....

Step-size selection and termination criteria: The three major disadvantages of SG methods are: (i) the slow convergence rate, (ii) deciding when to terminate the algorithm, and (iii) choosing the step size while running the algorithm. This paper showed that the SAG iterations achieve a much faster convergence rate, but the SAG iterations may also be advantageous in terms of tuning step sizes and designing termination criteria....

While we have stated Proposition 1 in terms of the iterates and Proposition 2 in terms of the function values, the rates obtained on iterates and function values are equivalent because, by the Lipschitz and strong-convexity assumptions, we have ${\frac{\mu}{2}{\|{x^{k} - x^{\ast}}\|}^{2}} \leqslant {{g{(x^{k})}} - {g{(x^{\ast})}}} \leqslant {\frac{L}{2}{\|{x^{k} - x^{\ast}}\|}^{2}}$.

## Convergence Analysis

L-BFGS: A publicly-available limited-memory quasi-Newton method that has been tuned for log-linear models.^33^3 This method is by far the most complicated method we considered.

As an example, in the case of $\ell_{2}$-regularized logistic regression we have $f_{i}{(x)}: = \frac{\lambda}{2} \parallel x \parallel^{2} + \log{(1 + \exp{( - b_{i}a_{i}^{T}x)})}$, where $a_{i} \in {\mathbb{R}}^{p}$ and...
