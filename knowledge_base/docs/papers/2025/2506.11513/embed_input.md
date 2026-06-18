Automatic Generation of Explicit Quadratic Programming Solvers

Topics include Quadratic programming, CVX, CVXPY, CVXPYgen.

Generates C++ code that solves explicit MPC problems. Super fast runtime for moderate size problems. Alternative to (implicit) quadratic program solvers.

We consider a family of convex quadratic programs in which the coefficients of the linear objective term and the righthand side of the constraints are affine functions of a parameter. It is well known that the solution of such a parametrized quadratic program is a piecewise affine function of the parameter. The number of (polyhedral) regions in the solution map can grow exponentially in problem size, but when the number of regions is moderate, a so-called explicit solver is practical. Such a solver computes the coefficients of the affine functions and the linear inequalities defining the polyhedral regions offline; to solve a problem instance online it simply evaluates this explicit solution map. Potential advantages of an explicit solver over a more general purpose iterative solver can include transparency, interpretability, reliability, and speed. In this paper we describe how code generation can be used to automatically generate an explicit solver from a high level description of a parametrized quadratic program. Our method has been implemented in the open-source software CVXPYgen, which is part of CVXPY, a domain specific language for general convex optimization.

## Introduction

### Parametric convex optimization

A parametric convex optimization problem can be written as

## Conclusions

We have added new functionality to the code generator CVXPYgen that generates an explicit solver (in C) for a parametrized convex optimization problem, when that is tractable. The user can prototype a problem in CVXPY, with code close to the math and convenient names for multiple variables and parameters, using a generic iterative solver; a change of one option in code generation will generate an explicit solver for the parametrized problem....

We extend the open-source code generator CVXPYgen \[SBD^+^22\] to generate code for explicitly solving QPs. The QP is modeled with CVXPY before CVXPYgen generates library-, allocation-, and division-free code for translating between the user-defined problem and a canonical form (that of PDAQP in this case) for explicitly solving QPs. Open source code and full documentation for CVXPYgen and its explicit solve feature is available at

Since compositions of affine functions are affine, it follows that the primal and dual solutions of the QP are (locally) affine functions of $\theta$. Since the inverse image of a polyhedron under an affine mapping is a polyhedron, the values of $\theta$ over which this affine function gives the solution is also a polyhedron. Thus the solution map is a piecewise affine function of $\theta$, with the polyhedral regions determined by the active set. By the uniqueness of the solution, it is not difficult to prove that such a map is also continuous across region boundaries \[\]....

Figure shows the comparison, demonstrating how the explicit solver can be used via its auto-generated CVXPY interface. Starting in line 15, we show that the primal and dual solutions and the objective values are all close, respectively.

where $x \in \text{R}^{n}$ is the variable and $\theta \in \Theta \subseteq \text{R}^{p}$ is the parameter, i.e., data that is given and known whenever is solved. The objective function $f_{0}$ and the inequality constraint functions $f_{i}$, $i = {1,\ldots,m}$, are convex in $x$ and the equality constraint functions $h_{i}$, $i = {1,\ldots,q}$, are affine in $x$, for any given value of $\theta \in \Theta$ \[\]. We refer to a solution of as $x^{\star}{(\theta)}$ to emphasize its dependence on the parameter $\theta$....
