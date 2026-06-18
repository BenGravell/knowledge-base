Automatic Generation of Explicit Quadratic Programming Solvers

Topics include Quadratic programming, CVX, CVXPY, CVXPYgen.

Generates C++ code that solves explicit MPC problems. Super fast runtime for moderate size problems. Alternative to (implicit) quadratic program solvers.

We consider a family of convex quadratic programs in which the coefficients of the linear objective term and the righthand side of the constraints are affine functions of a parameter. It is well known that the solution of such a parametrized quadratic program is a piecewise affine function of the parameter. The number of (polyhedral) regions in the solution map can grow exponentially in problem size, but when the number of regions is moderate, a so-called explicit solver is practical. Such a solver computes the coefficients of the affine functions and the linear inequalities defining the polyhedral regions offline; to solve a problem instance online it simply evaluates this explicit solution map. Potential advantages of an explicit solver over a more general purpose iterative solver can include transparency, interpretability, reliability, and speed. In this paper we describe how code generation can be used to automatically generate an explicit solver from a high level description of a parametrized quadratic program. Our method has been implemented in the open-source software CVXPYgen, which is part of CVXPY, a domain specific language for general convex optimization.

## Parametric convex optimization

A parametric convex optimization problem can be written as

where $x \in \text{R}^{n}$ is the variable and $\theta \in \Theta \subseteq \text{R}^{p}$ is the parameter, i.e., data that is given and known whenever is solved. The objective function $f_{0}$ and the inequality constraint functions $f_{i}$, $i = {1,\ldots,m}$, are convex in $x$ and the equality constraint functions $h_{i}$, $i = {1,\ldots,q}$, are affine in $x$, for any given value of $\theta \in \Theta$. We refer to a solution of as $x^{\star}{(\theta)}$ to emphasize its dependence on the parameter $\theta$.

Convex optimization is used in various domains, including control systems \[, RMD^+^17 \], signal and image processing \[ \], and quantitative finance \[, BJK^+^24, BBD^+^17 \], just to name a few that are particularly relevant for this work.

## Explicit solvers for multiparametric programming

Traditionally, $x^{\star}{(\theta)}$ is evaluated using an iterative numerical method that takes a given parameter value and computes an (almost) optimal point $x^{\star}{(\theta)}$ \[, SBG^+^20 \]. We focus here on a very special case when $x^{\star}{(\theta)}$ can be expressed in closed form, as an explicit function that maps a given value of $\theta$ directly to a solution $x^{\star}{(\theta)}$. Such explicit solvers are practical for only some problems, and generally only smaller instances, but when they are practical they can offer a number of advantages over generic iterative solvers.

## Limitations

In PDAQP the number of inequality constraints $m$ is limited to 1024 so the regions can be efficiently represented as a bit string. If $K$, or the size of the data in the explicit solver, exceed a given limit, the offline phase is terminated with a warning.
