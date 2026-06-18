COSMO: A Conic Operator Splitting Method for Convex Conic Problems

Topics include Conic optimization, Operator splitting, Convex optimization, Semidefinite programming, Sparse linear algebra.

Presents COSMO, a first-order conic solver built around operator splitting, quasi-definite linear solves, cone projections, and chordal decomposition for large semidefinite structure. It matters as a practical convex optimization solver aimed at large sparse conic problems arising in areas such as robust control.

This paper describes the Conic Operator Splitting Method (COSMO) solver, an operator splitting algorithm for convex optimisation problems with quadratic objective function and conic constraints. At each step the algorithm alternates between solving a quasi-definite linear system with a constant coefficient matrix and a projection onto convex sets. The low per-iteration computational cost makes the method particularly efficient for large problems, e.g. semidefinite programs that arise in portfolio optimisation, graph theory, and robust control. Moreover, the solver uses chordal decomposition techniques and a new clique merging algorithm to effectively exploit sparsity in large, structured semidefinite programs. A number of benchmarks against other state-of-the-art solvers for a variety of problems show the effectiveness of our approach. Our Julia implementation is open-source, designed to be extended and customised by the user, and is integrated into the Julia optimisation ecosystem.

## Introduction

We consider convex optimisation problems in the form

where we assume that both the objective function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ and the inequality constraint functions $g_{i}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ are convex, and that the equality constraints ${h_{i}{(x)}}:={{a_{i}^{\top}x} - b_{i}}$ are affine. We will denote an optimal solution to this problem (if it exists) as $x^{\ast}$. Convex optimisation problems feature heavily in a wide range of research areas and industries, including problems in machine learning, finance \[BBD^+^17\], optimal control, and operations research.

Algorithms for LPs were first used to solve military planning and allocation problems in the 1940s. In 1947 Danzig developed the simplex method that solves LPs by searching for the optimal solution along the vertices of the inequality polytope. Extensions to the method led to the general field of *active-set methods* that are able to solve both LPs and QPs, and which search for an optimal point by iteratively constructing a set of active constraints. Although often efficient in practice, a major theoretical drawback is that the worst-case complexity increases exponentially with the problem size.

The most common approach taken by modern convex solvers is the *interior-point method*, which stems from Karmarkar's original projective algorithm, and is able to solve both LPs and QPs in polynomial time. Interior point methods have since been extended to problems with positive semidefinite (PSD) constraints and. The primal-dual interior point methods apply variants of Newton's method to iteratively find a solution to a set of optimality KKT conditions.

ADMM methods are simple to implement and computationally cheap, even for large problems. However, they tend to converge slowly to a high accuracy solution and the detection of infeasibility is more involved compared to interior-point methods. They are therefore most often used in applications where a modestly accurate solution is sufficient \[PB^+^14\]. Most of the early advances in first-order methods such as ADMM happened in the 1970s/80s long before the demand for large scale optimisation, which may explain why they stayed less well-known and have only recently resurfaced.
