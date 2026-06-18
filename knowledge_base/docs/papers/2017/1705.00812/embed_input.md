Semidefinite Approximations of the Matrix Logarithm

Topics include Convex optimization, Semidefinite programming, Optimization, Matrix function.

The matrix logarithm, when applied to Hermitian positive definite matrices, is concave with respect to the positive semidefinite order. This operator concavity property leads to numerous concavity and convexity results for other matrix functions, many of which are of importance in quantum information theory. In this paper we show how to approximate the matrix logarithm with functions that preserve operator concavity and can be described using the feasible regions of semidefinite optimization problems of fairly small size. Such approximations allow us to use off-the-shelf semidefinite optimization solvers for convex optimization problems involving the matrix logarithm and related functions, such as the quantum relative entropy. The basic ingredients of our approach apply, beyond the matrix logarithm, to functions that are operator concave and operator monotone. As such, we introduce strategies for constructing semidefinite approximations that we expect will be useful, more generally, for studying the approximation power of functions with small semidefinite representations.

## Introduction

Semidefinite optimization problems are convex optimization problems that take the form

where $\mathbf{H}_{+}^{d}$ is the cone of $d \times d$ Hermitian positive semidefinite matrices, and $L \subseteq \mathbf{H}^{d}$ is an affine subspace of $d \times d$ Hermitian matrices (thought of as a real vector space). A convex function $f$ is said to have a *semidefinite representation* of size $d$ if its epigraph $\{{(x,t)}:{{f{(x)}} \leq t}\}$ can be expressed in the form $\pi{({L \cap \mathbf{H}_{+}^{d}})}$ where $\pi$ is a linear map. The existence of such representations for many convex functions \[\] explains the importance of semidefinite programming as a class of convex optimization problems....

### Free semidefinite representation

The semidefinite representation given in this paper of the hypograph of $f_{t}$ (see ) is a "free linear matrix inequality" representation in the sense of \[\]. This is one reason why our representations also work for the noncommutative perspective of $f_{t}$. In fact one can show that if an operator concave function $f$ admits a free linear matrix inequality representation, then the noncommutative perspective of $f$ also has a free linear matrix inequality representation. An interesting question would be to understand the class of operator concave functions that admit a free LMI representation.

$P_{r_{m}}$ is monotone in its first argument. This easily follows from the monotonicity of $r_{m}$.

The following theorem gives an approximation error for the cone $K_{m,k}$.

### Theorem 6 (Approximation error for $K_{g}^{n}$)

One fundamental limitation is that the feasible regions of semidefinite optimization problems are necessarily semialgebraic sets, i.e., they can be expressed as finite unions of sets defined by polynomial inequalities. As such, we cannot hope to *exactly* model non-semialgebraic convex sets and functions, such as the logarithm, using semidefinite programming. This leads us to consider the problem of understanding which general convex sets and functions can be *approximated* with high accuracy by sets with small semidefinite representations.

### Semidefinite approximations

One starting point is to consider the approximation of univariate convex or concave functions from the point of view of semidefinite optimization....
