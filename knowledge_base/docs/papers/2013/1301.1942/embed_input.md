Bayesian Optimization in a Billion Dimensions via Random Embeddings

Topics include REMBO, Bayesian optimization, Random embeddings, High-dimensional optimization, Black-box optimization, Gaussian processes, Algorithm configuration.

Introduces REMBO, a Bayesian optimization method that searches a random low-dimensional embedding of a very high-dimensional input space. The key contribution is showing that Gaussian-process Bayesian optimization can remain effective in billion-dimensional spaces when the objective has low intrinsic dimensionality, with both theory and solver-configuration experiments supporting the claim.

Bayesian optimization techniques have been successfully applied to robotics, planning, sensor placement, recommendation, advertising, intelligent user interfaces and automatic algorithm configuration. Despite these successes, the approach is restricted to problems of moderate dimension, and several workshops on Bayesian optimization have identified its scaling to high-dimensions as one of the holy grails of the field. In this paper, we introduce a novel random embedding idea to attack this problem. The resulting Random EMbedding Bayesian Optimization (REMBO) algorithm is very simple, has important invariance properties, and applies to domains with both categorical and continuous variables. We present a thorough theoretical analysis of REMBO. Empirical results confirm that REMBO can effectively solve problems with billions of dimensions, provided the intrinsic dimensionality is low. They also show that REMBO achieves state-of-the-art performance in optimizing the 47 discrete parameters of a popular mixed integer linear programming solver.

## Introduction

Let $f:{\mathcal{X}\rightarrow{\mathbb{R}}}$ be a function on a compact subset $\mathcal{X} \subseteq {\mathbb{R}}^{D}$. We address the following global optimization problem

Bayesian optimization has been demonstrated to outperform other state-of-the-art blackbox optimization techniques when function evaluations are expensive and the number of allowed function evaluations is therefore low (?). In recent years, it has found increasing use in the machine learning community (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?). Despite many success stories, the approach is restricted to problems of moderate dimension, typically up to about 10. Of course, for a great many problems this is all that is needed.

In this journal version of our work, we expand the presentation to provide more details throughout. In particular, we expand our description of the strategy for selecting the boundaries of the low-dimensional space and for setting the kernel length scale parameter; we show by means of an additional application (automatic configuration of random forest body-part classifiers) that the performance of our technique does not collapse when the problem does not have an obvious low effective dimensionality.

## Conclusion

We have demonstrated that it is possible to use random embeddings in Bayesian optimization to optimize functions of extremely high extrinsic dimensionality $D$ provided that they have low intrinsic dimensionality $d_{e}$. Moreover, our resulting REMBO algorithm is coordinate independent and it only requires a simple modification of the original Bayesian optimization algorithm; namely multiplication by a random matrix. We proved REMBO's independence of $D$ theoretically and empirically validated it by optimizing low-dimensional functions embedded in previously untenable extrinsic dimensionalities of up to $1$ billion.

We note that the central idea of our work -- using an otherwise unmodified optimization procedure in a randomly embedded space -- in principle could be applied to arbitrary optimization procedures. Evaluating the effciency of this technique for other procedures is an interesting topic for future work.
