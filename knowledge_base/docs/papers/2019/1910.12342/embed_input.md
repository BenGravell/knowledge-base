Minimizing a Sum of Clipped Convex Functions

We consider the problem of minimizing a sum of clipped convex functions; applications include clipped empirical risk minimization and clipped control. While the problem of minimizing the sum of clipped convex functions is NP-hard, we present some heuristics for approximately solving instances of these problems. These heuristics can be used to find good, if not global, solutions and appear to work well in practice. We also describe an alternative formulation, based on the perspective transformation, which makes the problem amenable to mixed-integer convex programming and yields computationally tractable lower bounds. We illustrate one of our heuristic methods by applying it to various examples and use the perspective transformation to certify that the solutions are relatively close to the global optimum. This paper is accompanied by an open-source implementation.

## Introduction

Suppose $f:{\text{R}^{n}\rightarrow\text{R}}$ is a convex function, and $\alpha \in \text{R}$. We refer to the function $\min{\{{f{(x)}},\alpha\}}$ as a *clipped convex function*. In this paper we consider the problem of minimizing a sum of clipped convex functions,

with variable $x \in \text{R}^{n}$, where $f_{0}:{\text{R}^{n}\rightarrow{\text{R} \cup {\{{+ \infty}\}}}}$ and $f_{i}:{\text{R}^{n}\rightarrow\text{R}}$ for $i = {1,\ldots,m}$ are closed proper convex functions, and $\alpha_{i} \in \text{R}$ for $i = {1,\ldots,m}$. We use infinite values of $f_{0}$ to encode constraints on $x$, i.e., to constrain $x \in \mathcal{X}$ for a closed convex set $\mathcal{X}$ we let ${f_{0}{(x)}} = {+ \infty}$ for all $x \notin \mathcal{X}$. When ${f_{i}{(x)}} > \alpha_{i}$, the value of the $i$th term in the sum is *clipped* to $\alpha_{i}$, which limits how large each term in the objective can be....

### Lower bound

Using the relaxed version of the perspective formulation, we can compute a lower bound on the objective value of the clipped control problem. We found a lower bound value of around 103.55, while the approximate solution we found had an objective value of 119.07, indicating that our approximate solution is no more than 15% suboptimal.

### Conic representation of the perspective

with variables $\lambda \in \text{R}^{m}$ and $x \in \text{R}^{n}$. (We note that this reformulation was also pointed out in \[23, §3\].) The equivalence follows immediately from the fact that

Our Python package `sccf` approximately solves generic problems of the form provided all $f_{i}$ can be represented as valid `cvxpy` expressions and constraints. It is available at:

### NP-hardness

In general, problem is nonconvex and as a result can be very difficult to solve. Indeed, is NP-hard. We show this by giving a reduction of the subset sum problem to an instance of.

The subset sum problem involves determining whether or not there exists a subset of a given set of integers $a_{1},\ldots,a_{n}$ that sum to zero. The optimal value of the problem

which has the form, is zero if and only if $x_{i} \in {\{ 0,1\}}$, at least one of $x_{i} = 1$, and ${a^{T}x} = 0$; in other words, the set $\{ a_{i}\mid{x_{i} = 1}\}$ sums to zero....
