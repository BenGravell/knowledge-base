Picasso: A Sparse Learning Library for High Dimensional Data Analysis in R and Python

We describe a new library named picasso, which implements a unified framework of pathwise coordinate optimization for a variety of sparse learning problems (e.g., sparse linear regression, sparse logistic regression, sparse Poisson regression and scaled sparse linear regression) combined with efficient active set selection strategies. Besides, the library allows users to choose different sparsity-inducing regularizers, including the convex l_1, nonconvex MCP and SCAD regularizers. The library is coded in C++ and has user-friendly R and Python wrappers. Numerical experiments demonstrate that picasso can scale up to large problems efficiently.

## Abstract

We describe a new library named picasso ^11^1More details can be found in our Github page: which implements a unified framework of pathwise coordinate optimization for a variety of sparse learning problems (e.g., sparse linear regression, sparse logistic regression, sparse Poisson regression and scaled sparse linear regression) combined with efficient active set selection strategies. Besides, the library allows users to choose different sparsity-inducing regularizers, including the convex $\ell_{1}$, nonvoncex MCP and SCAD regularizers. The library is coded in C++ and has user-friendly R and Python wrappers.

## Overview

Sparse Learning arises due to the demand of analyzing high-dimensional data such as high-throughput genomic data and functional Magnetic Resonance Imaging. The pathwise coordinate optimization is undoubtedly one the of the most popular solvers for a large variety of sparse learning problems. By leveraging the solution sparsity through a simple but elegant algorithmic structure, it significantly boosts the computational performance in practice.

We recently developed a new library named picasso, which implements a unified toolkit of pathwise coordinate optimization for solving a large class of convex and nonconvex regularized sparse learning problems. Efficient active set selection strategies are provided to guarantee superior statistical and computational preference. Specifically, we implement sparse linear regression, sparse logistic regression, sparse Poisson regression and scaled sparse linear regression. The options of regularizers include the $\ell_{1}$, MCP, and SCAD regularizers.

## Conclusion

The picasso library demonstrates significantly improved computational and statistical performance over existing libraries for nonconvex regularized sparse learning such as ncvreg. Besides, picasso also shows improvement over the popular libraries for convex regularized sparse learning such as glmnet. Overall, the picasso library has the potential to serve as a powerful toolbox for high dimensional sparse learning. We will continue to maintain and support this library.
