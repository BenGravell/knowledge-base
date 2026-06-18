Code Generation for Solving and Differentiating through Convex Optimization Problems

We introduce custom code generation for parametrized convex optimization problems that supports evaluating the derivative of the solution with respect to the parameters, i.e., differentiating through the optimization problem. We extend the open source code generator CVXPYgen, which itself extends CVXPY, a Python-embedded domain-specific language with a natural syntax for specifying convex optimization problems, following their mathematical description. Our extension of CVXPYgen adds a custom C implementation to differentiate the solution of a convex optimization problem with respect to its parameters, together with a Python wrapper for prototyping and desktop (non-embedded) applications. We give three representative application examples: Tuning hyper-parameters in machine learning; choosing the parameters in an approximate dynamic programming (ADP) controller; and adjusting the parameters in an optimization based financial trading engine via back-testing, i.e., simulation on historical data.

## Introduction

A convex optimization problem, parametrized by $\theta \in \Theta \subseteq \text{R}^{d}$, can be written as

where $x \in \text{R}^{n}$ is the optimization variable, $f_{0}$ is the objective function to be minimized, which is convex in $x$, and $f_{1},\ldots,f_{m}$ are inequality constraint functions that are convex in $x$. The parameter $\theta$ specifies data that can change, but is constant and given (or chosen) when we solve an instance of the problem. We refer to the parametrized problem as a *problem family*; when we specify a fixed value of $\theta \in \Theta$, we refer to it as a *problem instance*. We let $x^{\star}$ denote an optimal point for problem, assuming it exists.

Convex optimization is used in many domains, including signal and image processing \[, \], machine learning \[ \], control systems \[RMD^+^17 \], quantitative finance \[, BJK^+^24, BBD^+^17 \], and operations research \[ \].

## Differentiating through convex optimization problems

In many applications we are interested in the sensitivity of the solution $x^{\star}$ with respect to the parameter $\theta$. We will assume there is a unique solution for parameters near $\theta$, and that the mapping from $\theta$ to $x^{\star}$ is differentiable with Jacobian ${\partial{x^{\star}/{\partial\theta}}} \in \text{R}^{n \times d}$, evaluated at $\theta$. We then have
