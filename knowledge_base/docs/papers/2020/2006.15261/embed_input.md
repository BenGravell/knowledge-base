Picasso: A Sparse Learning Library for High Dimensional Data Analysis in R and Python

We describe a new library named picasso, which implements a unified framework of pathwise coordinate optimization for a variety of sparse learning problems (e.g., sparse linear regression, sparse logistic regression, sparse Poisson regression and scaled sparse linear regression) combined with efficient active set selection strategies. Besides, the library allows users to choose different sparsity-inducing regularizers, including the convex l_1, nonconvex MCP and SCAD regularizers. The library is coded in C++ and has user-friendly R and Python wrappers. Numerical experiments demonstrate that picasso can scale up to large problems efficiently.

## Abstract

We describe a new library named picasso ^11^1More details can be found in our Github page: which implements a unified framework of pathwise coordinate optimization for a variety of sparse learning problems (e.g., sparse linear regression, sparse logistic regression, sparse Poisson regression and scaled sparse linear regression) combined with efficient active set selection strategies. Besides, the library allows users to choose different sparsity-inducing regularizers, including the convex $\ell_{1}$, nonvoncex MCP and SCAD regularizers. The library is coded in C++ and has user-friendly R and Python wrappers....

## Overview

## Conclusion

The picasso library demonstrates significantly improved computational and statistical performance over existing libraries for nonconvex regularized sparse learning such as ncvreg. Besides, picasso also shows improvement over the popular libraries for convex regularized sparse learning such as glmnet. Overall, the picasso library has the potential to serve as a powerful toolbox for high dimensional sparse learning. We will continue to maintain and support this library.

## Example of R User Interface

\(3\) Inner loop: The algorithm conducts coordinate optimization (for sparse linear regression) or proximal Newton optimization combined with coordinate optimization (for sparse logistic regression, Possion regression, scaled sparse linear regression, sparse undirected graph estimation) only over active coordinates until convergence, with all inactive coordinates staying zero values. The active coordinates are updated efficiently using an efficient "naive update" rule that only operates on the non-zero coefficients. Better efficiency is achieved by the "covariance update" rule. See more details in....

To demonstrate the superior efficiency of our library, we compare picasso with a popular R library ncvreg (version 3.9.1) for nonconvex regularized sparse regression, the most popular R library glmnet (version 2.0-13) for convex regularized sparse regression, and two R libraries scalreg-v1.0 and flare-v1.5.0 for scaled sparse linear regression. All experiments are evaluated on an Intel Core CPU i7-7700k 4.20GHz and under R version 3.4.3. Timings of the CPU execution are recored in seconds and averaged over 10 replications on a sequence of 100 regularization parameters....
