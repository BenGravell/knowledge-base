COSMO: A Conic Operator Splitting Method for Convex Conic Problems

Topics include Conic optimization, Operator splitting, Convex optimization, Semidefinite programming, Sparse linear algebra.

Presents COSMO, a first-order conic solver built around operator splitting, quasi-definite linear solves, cone projections, and chordal decomposition for large semidefinite structure. It matters as a practical convex optimization solver aimed at large sparse conic problems arising in areas such as robust control.

This paper describes the Conic Operator Splitting Method (COSMO) solver, an operator splitting algorithm for convex optimisation problems with quadratic objective function and conic constraints. At each step the algorithm alternates between solving a quasi-definite linear system with a constant coefficient matrix and a projection onto convex sets. The low per-iteration computational cost makes the method particularly efficient for large problems, e.g. semidefinite programs that arise in portfolio optimisation, graph theory, and robust control. Moreover, the solver uses chordal decomposition techniques and a new clique merging algorithm to effectively exploit sparsity in large, structured semidefinite programs. A number of benchmarks against other state-of-the-art solvers for a variety of problems show the effectiveness of our approach. Our Julia implementation is open-source, designed to be extended and customised by the user, and is integrated into the Julia optimisation ecosystem.

## Introduction

We consider convex optimisation problems in the form

where we assume that both the objective function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ and the inequality constraint functions $g_{i}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ are convex, and that the equality constraints ${h_{i}{(x)}}:={{a_{i}^{\top}x} - b_{i}}$ are affine. We will denote an optimal solution to this problem (if it exists) as $x^{\ast}$. Convex optimisation problems feature heavily in a wide range of research areas and industries, including problems in machine learning \[\], finance \[BBD^+^17\], optimal control \[\], and operations research \[\]....

parent-child merging; 5 clique graph with nominal edge weighting; 6 clique graph with estimated edge weighting;
Our clique graph-based methods lead to a reduction in overall solver time. The method with estimated edge weighting function CG2 achieves the lowest average projection times for the majority of problems. In four cases ParCh has a narrow advantage. The geometric mean of the ratios of projection time of CG2 compared to the best non-graph method is 0.701, with a minimum ratio of 0.407 for problem mcp500-2....

out of memory error;
This paper describes the first-order solver COSMO and the ADMM algorithm on which it is based. The solver combines direct support of quadratic objectives, infeasibility detection, custom constraints, chordal decomposition of PSD constraints and automatic clique merging. The performance of the solver is illustrated on a number of benchmark problems that challenge different aspects of modern solvers.
The implementation in the Julia language facilitates rapid development and testing of ideas and allows users to customize the solver for their applications....

The *aggregate sparsity* of the problem is given by the graph $G{(V,E)}$ with edge set

and the scaled convex cone ${U\mathcal{K}} ≔ {\{{{Uv} \in {\mathbb{R}}^{m}}\mid{v \in \mathcal{K}}\}}$. After solving the original solution is obtained by reversing the scaling:

By choosing the cardinality $\left| V_{c} \right|$, the overlap between cliques $\mathcal{C}_{1} = {{\{ 1,2\}} \cup V_{c}}$ and $\mathcal{C}_{3} = {{\{{m_{a} + 1}\}} \cup V_{c}}$ can be made arbitrarily large while $\left| V_{a} \right|$, $\left| V_{b} \right|$ can be chosen so that any other merge is disadvantageous....
