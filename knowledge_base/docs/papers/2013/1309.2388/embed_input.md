Minimizing Finite Sums with the Stochastic Average Gradient

Topics include Stochastic average gradient, Finite-sum optimization, Variance reduction, Linear convergence, Convex optimization, Non-uniform sampling, Empirical risk minimization.

Gives the extended analysis of SAG for smooth finite-sum convex objectives, proving faster rates than black-box stochastic gradient methods and linear convergence under strong convexity. Compared with the shorter NeurIPS paper, this version clarifies the Lyapunov-style proof, step-size behavior, storage tradeoffs, and non-uniform sampling ideas that made SAG a canonical variance-reduction method.

We propose the stochastic average gradient (SAG) method for optimizing the sum of a finite number of smooth convex functions. Like stochastic gradient (SG) methods, the SAG method's iteration cost is independent of the number of terms in the sum. However, by incorporating a memory of previous gradient values the SAG method achieves a faster convergence rate than black-box SG methods. The convergence rate is improved from O(1/k^{1/2}) to O(1/k) in general, and when the sum is strongly-convex the convergence rate is improved from the sub-linear O(1/k) to a linear convergence rate of the form O(p^k) for p \textless{} 1. Further, in many cases the convergence rate of the new method is also faster than black-box deterministic gradient methods, in terms of the number of gradient evaluations. Numerical experiments indicate that the new algorithm often dramatically outperforms existing SG and deterministic gradient methods, and that the performance may be further improved through the use of non-uniform sampling strategies.

## Introduction

A plethora of the optimization problems arising in practice involve computing a minimizer of a finite sum of functions measuring misfit over a large number of data points. A classical example is least-squares regression,

where the $a_{i} \in {\mathbb{R}}^{p}$ and $b_{i} \in {\mathbb{R}}$ are the data samples associated with a regression problem. Another important example is logistic regression,

where the $a_{i} \in {\mathbb{R}}^{p}$ and $b_{i} \in {\{{- 1},1\}}$ are the data samples associated with a binary classification problem. A key challenge arising in modern applications is that the number of data points $n$ (also known as *training examples*) can be extremely large, while there is often a large amount of redundancy between examples. The most wildly successful class of algorithms for taking advantage of the *sum* structure for problems where $n$ is very large are *stochastic gradient* (SG) methods \Robbins and Monro, [1951, Bottou and LeCun, 2003\].

In this work, we focus on such *finite data* problems where each $f_{i}$ is *smooth* and *convex*.

That is, like the FG method, the step incorporates a gradient with respect to each function. But, like the SG method, each iteration only computes the gradient with respect to a single example and the cost of the iterations is independent of $n$. Despite the low cost of the SAG iterations, we show in this paper that with a constant step-size *the SAG iterations have an $O{({1/k})}$ convergence rate for convex objectives and a linear convergence rate for strongly-convex objectives*, like the FG method.

## Discussion

Since the first version of this work was published \Le Roux et al. there has been an explosion of interest in stochastic methods with improved convergence rates. In this section we first review other algorithms that have been discovered to have this property, and then we discuss the many possible variants on these basic algorithms that have been explored. As this is a very quickly-evolving area there are likely to be many new developments in the near future, but we note that this literature review is up to date as of January, 2015.
