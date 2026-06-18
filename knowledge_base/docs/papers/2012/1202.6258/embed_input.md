A Stochastic Gradient Method with an Exponential Convergence Rate for Finite Training Sets

Topics include Stochastic average gradient, Variance reduction, Finite-sum optimization, Linear convergence, Convex optimization, Empirical risk minimization, Incremental gradient methods.

Introduces the stochastic average gradient method, which stores the most recent gradient for each finite-sum component and averages those stored gradients to obtain a low-cost update with linear convergence on strongly convex objectives. It is one of the first modern variance-reduction methods showing that finite training sets permit faster rates than black-box stochastic gradient assumptions allow.

We propose a new stochastic gradient method for optimizing the sum of a finite set of smooth functions, where the sum is strongly convex. While standard stochastic gradient methods converge at sublinear rates for this problem, the proposed method incorporates a memory of previous gradient values in order to achieve a linear convergence rate. In a machine learning context, numerical experiments indicate that the new algorithm can dramatically outperform standard algorithms, both in terms of optimizing the training error and reducing the test error quickly.

## Introduction

A plethora of the problems arising in machine learning involve computing an approximate minimizer of the sum of a loss function over a large number of training examples, where there is a large amount of redundancy between examples. The most wildly successful class of algorithms for taking advantage of this type of problem structure are *stochastic gradient* (SG) methods Robbins and Monro; Bottou and LeCun. Although the theory behind SG methods allows them to be applied more generally, in the context of machine learning SG methods are typically used to solve the problem of optimizing a sample average over a finite training set, i.e.,

In this work, we focus on such *finite training data* problems where each $f_{i}$ is *smooth* and the average function $g$ is *strongly-convex*.

That is, like the FG method, the step incorporates a gradient with respect to each training example. But, like the SG method, each iteration only computes the gradient with respect to a single training example and the cost of the iterations is independent of $n$. Despite the low cost of the SAG iterations, in this paper we show that *the SAG iterations have a linear convergence rate*, like the FG method. That is, by having access to $i_{k}$ and by keeping a *memory* of the most recent gradient value computed for each training example $i$, this iteration achieves a faster convergence rate than is possible for standard SG methods.

## Discussion

Optimal regularization strength: One might wonder if the additional hypothesis in Proposition 2 is satisfied in practice. In a learning context, where each function $f_{i}$ is the loss associated to a single data point, $L$ is equal to the largest value of the loss second derivative $\xi$ (1 for the square loss, 1/4 for the logistic loss) times $R^{2}$, where $R$ is a the uniform bound on the norm of each data point. Thus, the constraint $\frac{\mu}{L} \geqslant \frac{8}{n}$ is satisfied when $\lambda \geqslant \frac{8\xiR^{2}}{n}$.

Training cost vs. testing cost: The theoretical contribution of this work is limited to the convergence rate of the training cost. Though there are several settings where this is the metric of interest (e.g., variational inference in graphical models), in many cases one will be interested in the convergence speed of the testing cost.
