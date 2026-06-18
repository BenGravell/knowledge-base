Clarabel: An Interior-point Solver for Conic Programs with Quadratic Objectives

Topics include Convex optimization, Semidefinite programming, Robustness, Benchmarks, Distributed systems, Optimization, Clarabel, Interior-point methods.

We present a general-purpose interior-point solver for convex optimization problems with conic constraints. Our method is based on a homogeneous embedding method originally developed for general monotone complementarity problems and more recently applied to operator splitting methods, and here specialized to an interior-point method for problems with quadratic objectives. We allow for a variety of standard symmetric and non-symmetric cones, and provide support for chordal decomposition methods in the case of semidefinite cones. We describe the implementation of this method in the open-source solver Clarabel, and provide a detailed numerical evaluation of its performance versus several state-of-the-art solvers on a wide range of standard benchmarks problems. Clarabel is faster and more robust than competing commercial and open-source solvers across a range of test sets, with a particularly large performance advantage for problems with quadratic objectives. Clarabel is currently distributed as a standard solver for the Python CVXPY optimization suite.

## Introduction

We

with decision variables $x \in {\mathbb{R}}^{n}$ and $s \in {\mathbb{R}}^{m}$, and problem data $A \in {\mathbb{R}}^{m \times n}$, $b \in {\mathbb{R}}^{m}$, $q \in {\mathbb{R}}^{n}$ and $P \in {\mathbb{R}}^{n \times n}$. We assume that $P$ is symmetric and positive semidefinite (possibly zero) and that the set $\mathcal{K}$ is a closed and convex cone. We will denote the optimal value of this problem as $p^{\ast}$ and an optimizer (when it exists) as $(x^{\ast},s^{\ast})$.

It can be shown that the problem dual to $\mathcal{P}$ is

where $\mathcal{K}^{\ast}$ is the dual cone of $\mathcal{K}$. We will denote its optimal value as $d^{\ast}$ and an optimizer (when it exists) as $(x^{\ast},z^{\ast})$. We will assume throughout that strong duality holds between $\mathcal{P}$ and $\mathcal{D}$, i.e. that $p^{\ast} = d^{\ast}$.
