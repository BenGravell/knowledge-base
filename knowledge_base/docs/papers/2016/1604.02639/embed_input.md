Disciplined Convex-Concave Programming

Topics include Convex optimization, Nonconvex optimization, Optimization, DCCP, DCP, With convex-concave programming, CCP, Concave function.

In this paper we introduce disciplined convex-concave programming (DCCP), which combines the ideas of disciplined convex programming (DCP) with convex-concave programming (CCP). Convex-concave programming is an organized heuristic for solving nonconvex problems that involve objective and constraint functions that are a sum of a convex and a concave term. DCP is a structured way to define convex optimization problems, based on a family of basic convex and concave functions and a few rules for combining them. Problems expressed using DCP can be automatically converted to standard form and solved by a generic solver; widely used implementations include YALMIP, CVX, CVXPY, and Convex.jl. In this paper we propose a framework that combines the two ideas, and includes two improvements over previously published work on convex-concave programming, specifically the handling of domains of the functions, and the issue of nondifferentiability on the boundary of the domains. We describe a Python implementation called DCCP, which extends CVXPY, and give examples.

## Abstract

In this paper we introduce *disciplined convex-concave programming* (DCCP), which combines the ideas of disciplined convex programming (DCP) with convex-concave programming (CCP). Convex-concave programming is an organized heuristic for solving nonconvex problems that involve objective and constraint functions that are a sum of a convex and a concave term. DCP is a structured way to define convex optimization problems, based on a family of basic convex and concave functions and a few rules for combining them....

## Disciplined convex-concave programming

Figure 9: Gaussian covariance matrix estimation.

An example with $n = 20$ and $N = 30$ is in figure 9. Not surprisingly, knowledge of the signs of the entries of $\Sigma$ allows us to obtain a much better estimate of the true covariance matrix.

Attribute `expression.domain` returns a list of constraints describing the domain of a DCP expression. (This attribute is also in the core CVXPY package.)

Recall that we defined DCCP problems to ensure that the linearized problem in algorithm 1.1 is a DCP problem. It is not obvious that if we replace the standard linearization with equation the linearized problem is still a DCP problem. In this section we prove that the linearized DCCP problem still satisfies the rules of DCP, or equivalently that each $\mathcal{I}_{i}{(x)}$ has a known graph implementation or satisfies the DCP composition rule.

An example with $d = 2$ and $n = 50$ is shown in figure 3.

### Difference of convex programming

Difference of convex (DC) programming problems have the form

where $x \in \text{R}^{n}$ is the optimization variable, and the functions $f_{i}:{\text{R}^{n}\rightarrow\text{R}}$ and $g_{i}:{\text{R}^{n}\rightarrow\text{R}}$ for $i = {0,\ldots,m}$ are convex. The DC problem can also include equality constraints of the form ${p_{i}{(x)}} = {q_{i}{(x)}}$, where $p_{i}$ and $q_{i}$ are convex; we simply express these as the pair of inequality constraints

which have the difference of convex form in. When the functions $g_{i}$ are all affine, the problem is a convex optimization problem, and easily solved \[\].

The broad class of DC functions includes all $C^{2}$ functions \[\], so the DC problem is very general. A special case is Boolean linear programs, which can represent many problems, such as the traveling salesman problem, that are widely believed to be...
