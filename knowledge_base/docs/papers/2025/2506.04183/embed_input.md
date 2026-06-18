Learning Parametric Convex Functions

Topics include Convex optimization, Optimization, Learning, Convex function.

A parametrized convex function depends on a variable and a parameter, and is convex in the variable for any valid value of the parameter. Such functions can be used to specify parametrized convex optimization problems, i.e., a convex optimization family, in domain specific languages for convex optimization. In this paper we address the problem of fitting a parametrized convex function that is compatible with disciplined programming, to some given data. This allows us to fit a function arising in a convex optimization formulation directly to observed or simulated data. We demonstrate our open-source implementation on several examples, ranging from illustrative to practical.

## Introduction

### Parametrized convex functions

A *parametrized convex function* (PCF) $f$ has the form

## Conclusions

We have shown how to fit a PCF to data, in a simple yet customizable way, with our open-source Python tool LPCF. Our method allows (parametrized) convex optimization to be (in part) data driven: while the modeling stage may heavily rely on learning functions from data, the first-principles structure of convex optimization is retained when solving a given problem instance. Our experiments exhibit good modeling accuracy (also compared to alternative convex function approximations), and the use of learned PCFs in convex optimization problems.

A further variation is a low rank plus diagonal quadratic $Q = {{F^{T}F} + {\operatorname{\mathbf{d}\mathbf{i}\mathbf{a}\mathbf{g}}{(d_{1}^{2},\ldots,d_{n}^{2})}}}$, where $F \in \text{R}^{m \times n}$ is a wide matrix with $m \ll n$ and $d \in \text{R}^{n}$ is a vector of diagonal entries before they are squared to make $Q$ positive semidefinite. Such a form can be used to capture the dominant directions of curvature when $n$ is large.

### Convexity

Nonconvex (relative to best affine fit)

where $\Theta \subseteq \text{R}^{p}$. To be a PCF, $f$ must be continuous in $\theta$, and for each $i = {1,\ldots,d}$, $f_{i}{(x,\theta)}$ is convex in $x$ for any $\theta \in \Theta$. We refer to the first argument $x$ of the PCF $f$ as the *variable*, and the second argument $\theta$ as the *parameter*. When $d = 1$, we refer to $f$ as a scalar PCF.

### Disciplined convex programming

The terms variable and parameter in a PCF are taken from disciplined convex programming (DCP), a method for expressing a PCF as an expression in a domain specific language (DSL) constructed from variables, constants, parameters, and a small library of functions called atoms \[, []\]. In DCP, the expression must be constructed in a specific way that corresponds to a composition rule that establishes convexity of the function with respect to the variable, for any valid parameter.

Functions expressed in DCP form can be used to form a parametrized convex optimization problem or convex optimization family. When the parameters are given specific numerical values, we obtain a problem instance, which can be solved by automatically transforming the problem instance to a canonical form, solving the canonical form, and then...
