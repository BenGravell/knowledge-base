Clarabel: An Interior-point Solver for Conic Programs with Quadratic Objectives

Topics include Convex optimization, Semidefinite programming, Robustness, Benchmarks, Distributed systems, Optimization, Clarabel, Interior-point methods.

We present a general-purpose interior-point solver for convex optimization problems with conic constraints. Our method is based on a homogeneous embedding method originally developed for general monotone complementarity problems and more recently applied to operator splitting methods, and here specialized to an interior-point method for problems with quadratic objectives. We allow for a variety of standard symmetric and non-symmetric cones, and provide support for chordal decomposition methods in the case of semidefinite cones. We describe the implementation of this method in the open-source solver Clarabel, and provide a detailed numerical evaluation of its performance versus several state-of-the-art solvers on a wide range of standard benchmarks problems. Clarabel is faster and more robust than competing commercial and open-source solvers across a range of test sets, with a particularly large performance advantage for problems with quadratic objectives. Clarabel is currently distributed as a standard solver for the Python CVXPY optimization suite.

## Introduction

We consider throughout the following convex conic optimization problem:

with decision variables $x \in {\mathbb{R}}^{n}$ and $s \in {\mathbb{R}}^{m}$, and problem data $A \in {\mathbb{R}}^{m \times n}$, $b \in {\mathbb{R}}^{m}$, $q \in {\mathbb{R}}^{n}$ and $P \in {\mathbb{R}}^{n \times n}$. We assume that $P$ is symmetric and positive semidefinite (possibly zero) and that the set $\mathcal{K}$ is a closed and convex cone. We will denote the optimal value of this problem as $p^{\ast}$ and an optimizer (when it exists) as $(x^{\ast},s^{\ast})$.

We have presented a novel interior-point solver for conic optimization problems with quadratic objectives. Our method uses a homogeneous embedding inspired by previous work on monotone complementarity problems, but not previously applied to interior-point conic optimization in any widely available solver. We have shown that our method is competitive with state-of-the-art solvers for a wide range of problem classes, and in particular outperforms state-of-the-art solvers in problems with quadratic objectives (QPs), large-scale SOCPs, and SDPs with significant sparsity structure.

Our implementation of Clarabel is available as open-source software in both Rust and Julia, with several other language interfaces, and is available as a standard solver in the CVXPY modelling package. Clarabel already has growing base of both academic and industrial users and has been downloaded several million times since its initial release.

For symmetric cones we linearize the central path equation (21c). The NT scaling method exploits the self-scaled property of symmetric cone $\mathcal{K}$ to define, for ${(s,z)} \in \mathcal{K}$, a unique scaling point $w \in \mathcal{K}$ satisfying

Before solving we perform an equilibration step on all matrix-valued data using the Ruiz equilibration technique described in \[Ruiz:2001\]. We refer the reader to \[COSMO, §3.5\] and \[OSQP, §5.1\] for implementation details.

so that the solver with the lowest shifted geometric mean solve time has a normalized score of 1. For those problems for which a given solver fails, we assign a solve time $t_{p,s}$ equal to the maximum allowable solve time for the relevant benchmark.

It can be shown that the problem dual to $\mathcal{P}$ is
