Guaranteed Minimum-Rank Solutions of Linear Matrix Equations via Nuclear Norm Minimization

Topics include Rank minimization, Nuclear norm, Compressed sensing, Convex relaxation, Restricted isometry, Matrix recovery.

Shows that nuclear-norm minimization can recover minimum-rank matrices from linear measurements under restricted-isometry conditions. The paper establishes low-rank recovery as the matrix analogue of sparse compressed sensing and ties it to system identification, embedding, and recommendation problems.

The affine rank minimization problem consists of finding a matrix of minimum rank that satisfies a given system of linear equality constraints. Such problems have appeared in the literature of a diverse set of fields including system identification and control, Euclidean embedding, and collaborative filtering. Although specific instances can often be solved with specialized algorithms, the general affine rank minimization problem is NP-hard. In this paper, we show that if a certain restricted isometry property holds for the linear transformation defining the constraints, the minimum rank solution can be recovered by solving a convex optimization problem, namely the minimization of the nuclear norm over the given affine space. We present several random ensembles of equations where the restricted isometry property holds with overwhelming probability. The techniques used in our analysis have strong parallels in the compressed sensing framework. We discuss how affine rank minimization generalizes this pre-existing concept and outline a dictionary relating concepts from cardinality minimization to those of rank minimization.

## Introduction

Notions such as order, complexity, or dimensionality can often be expressed by means of the rank of an appropriate matrix. For example, a low-rank matrix could correspond to a low-degree statistical model for a random process (e.g., factor analysis), a low-order realization of a linear system, a low-order controller for a plant, or a low-dimensional embedding of data in Euclidean space. If the set of feasible models or designs is affine in the matrix variable, choosing the simplest model can be cast as an *affine rank minimization problem*,

where $X \in {\mathbb{R}}^{m \times n}$ is the decision variable, and the linear map $\mathcal{A}:{{\mathbb{R}}^{m \times n}\rightarrow{\mathbb{R}}^{p}}$ and vector $b \in {\mathbb{R}}^{p}$ are given. In certain instances with very special structure, the rank minimization problem can be solved by using the singular value decomposition, or can be exactly reduced to the solution of linear systems. In general, however, problem (1.1) is a challenging nonconvex optimization problem for which all known finite time algorithms have at least doubly exponential running times in both theory and practice....

### Parsimonious models and optimization

Sparsity and low-rank are two specific classes of parsimonious (or low-complexity) descriptions. Are there other kinds of easy-to-describe parametric models that are amenable to exact solutions via convex optimizations techniques? Given the intimate connections between linear and semidefinite programming and the Jordan algebraic approaches described earlier, it is likely that this will require alternative tractable convex optimization formulations.

Let $\mathcal{A}$ be a random variable that takes values in linear maps from ${\mathbb{R}}^{m \times n}$ to ${\mathbb{R}}^{p}$. We say that $\mathcal{A}$ is *nearly isometrically distributed* if for all $X \in {\mathbb{R}}^{m \times n}$

### Optimality conditions

A variety of methods can be developed for the effective minimization of the nuclear norm over an affine subspace of matrices, and we do not have room for a comprehensive treatment here. Instead, we focus on three methods highlighting the trade-offs between computational speed and guarantees on accuracy of the resulting solution....
