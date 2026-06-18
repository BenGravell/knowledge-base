## Introduction

We consider convex optimisation problems in the form

where we assume that both the objective function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ and the inequality constraint functions $g_{i}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ are convex, and that the equality constraints ${h_{i}{(x)}}:={{a_{i}^{\top}x} - b_{i}}$ are affine. We will denote an optimal solution to this problem (if it exists) as $x^{\ast}$. Convex optimisation problems feature heavily in a wide range of research areas and industries, including problems in machine learning \[\], finance \[BBD^+^17\], optimal control \[\], and operations research \[\]. Concrete examples of problems fitting the general form include linear programming (LP), convex quadratic programming (QP), second-order cone programming (SOCP), and semidefinite programming (SDP) problems. Methods to solve each of these standard problem classes are well known and a number of open- and closed-source solvers are widely available. However, the trend for data and training sets of increasing size in decision making problems and machine learning poses a challenge for state-of-the-art software.

Algorithms for LPs were first used to solve military planning and allocation problems in the 1940s \[\]. In 1947 Danzig developed the simplex method that solves LPs by searching for the optimal solution along the vertices of the inequality polytope. Extensions to the method led to the general field of *active-set methods* \[\] that are able to solve both LPs and QPs, and which search for an optimal point by iteratively constructing a set of active constraints. Although often efficient in practice, a major theoretical drawback is that the worst-case complexity increases exponentially with the problem size \[\].

The most common approach taken by modern convex solvers is the *interior-point method* \[\], which stems from Karmarkar's original projective algorithm \[\], and is able to solve both LPs and QPs in polynomial time. Interior point methods have since been extended to problems with positive semidefinite (PSD) constraints in \[\] and \[\]. The primal-dual interior point methods apply variants of Newton's method to iteratively find a solution to a set of optimality KKT conditions. At each iteration the algorithm alternates between a Newton step that involves factoring a Jacobian matrix and a line search to determine the magnitude of the step to ensure a feasible iterate. Most notably, the Mehrotra predictor-corrector method in \[\] forms the basis of several implementations because of its strong practical performance \[\]. However, interior-point methods typically do not scale well for very large problems since the Jacobian matrix has to be calculated and factored at each step.

Two main approaches to overcome this limitation are active research areas. Firstly, a renewed focus on first-order methods with computationally cheaper per-iteration-cost, and secondly the exploitation of sparsity in the problem data. First-order methods are known to handle larger problems well at the expense of reduced accuracy compared to interior-point methods. In the 1960s Everett \[\] proposed a dual decomposition method that allows one to decompose a separable objective function, making each iteration cheaper to compute. Augmented Lagrangian methods by Miele (\[ \]), Hestenes \[\], and Powell \[\] are more robust and helped to remove the strict convexity conditions on problems, while losing the decomposition property. By splitting the objective function, the alternating direction method of multipliers (ADMM), first described in \[\], allowed the advantages of dual decomposition to be combined with the superior convergence and robustness of augmented Lagrangian methods. Subsequently, it was shown that ADMM can be analysed from the perspective of monotone operators and that it is a special case of Douglas-Rachford splitting \[\] as well as of the proximal point algorithm in \[\], which allowed further insight into the method.

ADMM methods are simple to implement and computationally cheap, even for large problems. However, they tend to converge slowly to a high accuracy solution and the detection of infeasibility is more involved compared to interior-point methods. They are therefore most often used in applications where a modestly accurate solution is sufficient \[PB^+^14\]. Most of the early advances in first-order methods such as ADMM happened in the 1970s/80s long before the demand for large scale optimisation, which may explain why they stayed less well-known and have only recently resurfaced.

A method of exploiting the sparsity pattern of PSD constraints in an interior-point algorithm was developed in \[\]. This work showed that if the coefficient matrices of an SDP exhibit an aggregate sparsity pattern represented by a chordal graph, then both primal and dual problems can be decomposed into a problem with many smaller PSD constraints on the nonzero blocks of the original matrix variable. These blocks are associated with subsets, called *cliques*, of graph vertices. Moreover, it can be advantageous to merge some of these blocks, for example if they overlap significantly. The optimal way to merge the blocks, or equivalently the corresponding graph cliques, after the initial decomposition depends on the solver algorithm and is still an open question. Sparsity in SDPs has also been studied for problems with underlying graph structure, e.g. optimal power-flow problems in \[\] and graph optimisation problems in \[\].

### Related Work

Widely used solvers for conic problems, especially SDPs, include SeDuMi \[\], SDPT3 \[\] (both open source, MATLAB), and MOSEK \[\] (commercial, C) among others. All of these solvers implement primal-dual interior-point methods.

Both Fukuda \[\] and Sun \[\] developed interior-point solvers that exploit chordal sparsity patterns in PSD constraints. Some heuristic methods to merge cliques have been proposed for interior-point methods in \[\] and been implemented in the SparseCoLO package \[FKK^+^09\] and the CHOMPACK package \[\].

Several solvers based on the ADMM method have been released recently. The solver OSQP \[SBG^+^18\] is implemented in C and detects infeasibility based on the differences of the iterates \[\], but only solves LPs and QPs. The C-based SCS \[\] implements an operator splitting method that solves the primal-dual pair of conic programs in order to provide infeasibility certificates. The underlying homogeneous self-dual embedding method has been extended by \[ZFP^+^19\] to exploit sparsity and implemented in the MATLAB solver CDCS. The conic solvers SCS and CDCS are unable to handle quadratic cost functions directly. Instead they are forced to reformulate problem with quadratic objective functions by adding a second-order cone constraint, which increases the problem size. Moreover, they rely on primal-dual formulations to detect infeasibility.

### Outline

In Section 2 we define the general conic problem format, its dual problem, as well as optimality and infeasibility conditions. Section 3 describes the ADMM algorithm that is used by COSMO. Section 4 explains how to decompose SDPs in a preprocessing step provided the problem data has an aggregated sparsity pattern. In Section 5 we describe a new clique merging strategy and compare it to existing approaches. Implementation details and code related design choices are discussed in Section 6. Section 7 shows benchmark results of COSMO vs. other state-of-the art solvers on a number of test problems. Section 8 concludes the paper.

### Contributions

With the solver package described in this paper we make the following contributions:

We implement a first-order method for large conic problems that is able to detect infeasibility without the need of a homogeneous self-dual embedding.

COSMO directly supports quadratic objective functions, thus reducing overheads for applications with both quadratic objective function and PSD constraints. This also avoids a major disadvantage of conic solvers compared to native QP solvers, i.e no additional matrix factorisation for the conversion is needed and favourable sparsity in the objective can be maintained.

Large structured positive semidefinite programs are analysed and, if possible, chordally decomposed. This typically allows one to solve very large sparse and structured problems orders of magnitudes faster than competing solvers. For complex sparsity patterns, further performance improvements are achieved by recombining some of the sub-blocks of the initial decomposition in an optimal way. For this purpose, we propose a new clique graph based merging strategy and compare it to existing heuristic approaches.

The open-source solver is written in a modular way in the fast and flexible programming language Julia. The design allows users to extend the solver by specifying a specific linear system solver and by defining their own convex cones or custom projection methods.

### Notation

The following notation and definitions will be used throughout this paper. Denote the space of real numbers $\mathbb{R}$, the n-dimensional real space ${\mathbb{R}}^{n}$, the n-dimensional zero cone ${\{ 0\}}^{n}$, the nonnegative orthant ${\mathbb{R}}_{+}^{n}$, the space of symmetric matrices ${\mathbb{S}}^{n}$, and the set of positive semidefinite matrices ${\mathbb{S}}_{+}^{n}$.

In some of the following sections matrix data is considered in vectorized form. Denote the vectorization of a matrix $X$ by stacking it columns as $x ≔ {\text{vec}{(X)}}$ and the inverse operation as ${\text{vec}^{- 1}{(X)}} = {\text{mat}{(x)}}$. For symmetric matrices it is often computationally beneficial to work only with the upper-triangular elements of the matrix. Denote the transformation of a symmetric matrix $V \in {\mathbb{S}}^{n}$ with i,j-th element $V_{ij}$ into a vector of upper-triangular elements as

Here the scaling factor of $\sqrt{2}$ preserves the matrix inner product, i.e. ${{tr}{({AB})}} = {{svec}{(A)}^{\top}{svec}{(B)}}$ for symmetric matrices ${A,B} \in {\mathbb{S}}^{n}$. The inverse operation is denoted by ${{svec}^{- 1}{(s)}} ≕ {{smat}{(s)}}$. Denote the Kronecker product of two matrices $A$ and $B$ as $A \otimes B$. The Frobenius norm of a matrix $A$ is given by $\left. ||A||_{F} = \left( \sum_{ij}|a_{ij}|^{2}) \right. \right)^{1/2}$.

Sometimes we consider positive semidefinite constraints in vector form, so we define the space of vectorized symmetric positive semidefinite matrices as

For a convex cone $\mathcal{K}$ denote the *polar cone* by

the *normal cone* of $\mathcal{K}$ by

and, following \[\], the *recession cone* of $\mathcal{K}$ by

The *proximal operator* of a convex, closed and proper function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is given by

We denote the *indicator function* of a nonempty, closed convex set $\mathcal{C} \subseteq {\mathbb{R}}^{n}$ by

and the *projection* of $x \in {\mathbb{R}}^{n}$ onto $\mathcal{C}$ by:

We further denote the *support function* of $\mathcal{C}$ by:

## Conic Problems

We will address convex optimisation problems with a quadratic objective function and a number of conic constraints in the form:

where $x \in {\mathbb{R}}^{n}$ is the primal *decision variable* and $s \in {\mathbb{R}}^{m}$ is the primal *slack variable*. The objective function is defined by positive semidefinite matrix $P \in {\mathbb{S}}_{+}^{n}$ and vector $q \in {\mathbb{R}}^{n}$. The constraints are defined by matrix $A \in {\mathbb{R}}^{m \times n}$, vector $b \in {\mathbb{R}}^{m}$ and a non-empty, closed, convex cone $\mathcal{K}$ which itself can be a Cartesian product of cones in the form

with cone dimensions ${\sum_{i = 1}^{N}m_{i}} = m$. Note that any LP, QP, SOCP, or SDP can be written in the form using an appropriate choice of cones, as well as problems involving the power or exponential cones and their duals.

The dual problem associated with is given by:

with dual variable $y \in {\mathbb{R}}^{m}$.

The conditions for optimality (assuming linear independence constraint qualification) follow from the Karush-Kuhn-Tucker (KKT) conditions:

${s \in \mathcal{K}},$ ${y \in {(\mathcal{K}^{\infty})}^{\circ}}.$ (6c)

Assuming strong duality, if there exists a $x^{\ast} \in {\mathbb{R}}^{n}$, $s^{\ast} \in {\mathbb{R}}^{m}$, and $y^{\ast} \in {\mathbb{R}}^{m}$ that fulfil (6a)--(6c) then the pair $(x^{\ast},s^{\ast})$ is called the primal solution and $y^{\ast}$ is called the dual solution of problem.

### Infeasibility certificates

Primal and dual infeasibility conditions were developed for ADMM in \[\]. These conditions are directly applicable to problems of the form. To simplify the notation of the conditions, define the cone $\overline{\mathcal{K}} ≔ {{- \mathcal{K}} + {\{ b\}}}$. Then, the following sets provide certificates for primal and dual infeasibility:

The existence of some $y \in \mathcal{D}$ certifies that problem is primal infeasible, while the existence of some $x \in \mathcal{P}$ certifies dual infeasibility.

## ADMM Algorithm

We use the same splitting as in \[SBG^+^18\] to transform problem into standard ADMM format. The problem is rewritten by introducing the dummy variables $\overset{\sim}{x} = x$ and $\overset{\sim}{s} = s$:

where the indicator functions of the sets $\{{{(x,s)} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}}\mid{{{Ax} + s} = b}\}$ and $\mathcal{K}$ were used to move the constraints of into the objective function. The augmented Lagrangian of is given by

with step size parameters $\rho > 0$ and $\sigma > 0$ and dual variables $\lambda \in {\mathbb{R}}^{n}$ and $y \in {\mathbb{R}}^{m}$. The corresponding ADMM iteration is given by:

$({\overset{\sim}{x}}^{k + 1},$ ${\overset{\sim}{s}}^{k + 1}) = \operatorname{argmin}_{\overset{\sim}{x},\overset{\sim}{s}}L\left( \overset{\sim}{x},\overset{\sim}{s},x^{k},s^{k},\lambda^{k},y^{k} \right),$ (11a)
$x^{k + 1}$ ${= {{\alpha{\overset{\sim}{x}}^{k + 1}} + {{({1 - \alpha})}x^{k}} + {\frac{1}{\sigma}\lambda^{k}}}},$ (11b)
$s^{k + 1}$ ${= {{{\operatorname{argmin}\limits_{s}\frac{\rho}{2}}\left. \parallel{{{{\alpha{\overset{\sim}{s}}^{k + 1}} + {{({1 - \alpha})}s^{k}}} - s} + {\frac{1}{\rho}y^{k}}}\parallel \right._{2}^{2}} + {I_{\mathcal{K}}{(s)}}}},$ (11c)
$\lambda^{k + 1}$ ${= {\lambda^{k} + {\sigma\left( {{{\alpha{\overset{\sim}{x}}^{k + 1}} + {{({1 - \alpha})}x^{k}}} - x^{k + 1}} \right)}}},$ (11d)

where we relaxed the $z$-update and the dual variable update with relaxation parameter $\alpha \in {}$ according to \[\]. Notice from (11b) and (11d) that the dual variable corresponding to the constraint $x = \overset{\sim}{x}$ satisfies $\lambda^{k} = {0\text{~for all~}k}$.

### Solution of the equality constrained QP

The minimization problem in (11a) has the form of an equality-constrained quadratic program:

The solution of can be obtained by solving a single linear system. The corresponding Lagrangian is given by:

where the Lagrangian multiplier $\nu \in {\mathbb{R}}^{m}$ accounts for the equality-constraint ${{Ax} + s} = b$. Thus, the KKT optimality conditions for this equality constrained QP are given by:

Elimination of ${\overset{\sim}{s}}^{k + 1}$ from these equations leads to the linear system:

Note that the introduction of the dummy variable $\overset{\sim}{x}$ led to the term $\sigmaI$ in the upper-left corner of the coefficient matrix in. Consequently, the coefficient matrix in is always quasi-definite \[\], i.e. it always has a positive definite upper-left block and a negative definite lower-right block, and is therefore full rank even when $P = 0$ or $A$ is rank deficient. Following \[\] the left hand side of always has a well-defined $LDL^{\top}$ factorization with a diagonal $D$.

### Projection step

As shown in \[PB^+^14\] the minimization problem in (11c) can be interpreted as the $\rho$-weighted proximal operator of the indicator function $I_{\mathcal{K}}$. It is therefore equivalent to the Euclidean projection $\Pi_{\mathcal{K}}$ onto the cone $\mathcal{K}$, i.e.

If $\mathcal{K}$ is a Cartesian product of cones as in this projection is equivalent to the projection of the relevant components of the argument of $\Pi_{\mathcal{K}}{( \cdot )}$ onto each cone $\mathcal{K}_{i}$. A problem with $N$ SDP constraints therefore requires $N$ projections, but, since each of these operates on an independent segment of the input vector, they can be performed in parallel.

### Algorithm steps

The calculations performed at each iteration are summarized in Algorithm 1.

Input: initial values x0, s0, y0, problem data P, q, A, b, and parameters σ &gt; 0, ρ &gt; 0, α ∈
3 ${({\overset{\sim}{x}}^{k + 1},\nu^{k + 1})}\leftarrow$ solve linear system;
4 ${\overset{\sim}{s}}^{k + 1}\leftarrow{s^{k} - {\frac{1}{\rho}{({\nu^{k + 1} + y^{k}})}}}$;
5 $x^{k + 1}\leftarrow{{\alpha{\overset{\sim}{x}}^{k + 1}} + {{({1 - \alpha})}x^{k}}}$;
6 $s^{k + 1}\leftarrow{\Pi_{\mathcal{K}}\left( {{\alpha{\overset{\sim}{s}}^{k + 1}} + {{({1 - \alpha})}s^{k}} + {\frac{1}{\rho}y^{k}}} \right)}$;
9while termination criteria not satisfied;
Algorithm 1 ADMM iteration

Observe that the coefficient matrix of the linear system in is constant, so that one can precompute and cache the $LDL^{\top}$ factorization and efficiently evaluate line 2 with changing right hand sides. A refactorisation is only necessary if the step size parameters $\rho$ and $\sigma$ are updated.

Lines 3, 4, and 6 are computationally inexpensive since they involve only vector addition and scalar-vector multiplication. The projection in line 5 is crucial to the performance of the algorithm depending on the particular cones employed in the model: projections onto the zero-cone or the nonnegative orthant are inexpensive, while a projection onto the positive-semidefinite cone of dimension $N$ involves an eigenvalue decomposition. Since direct methods for eigen-decompositions have a complexity of approximately $\mathcal{O}{(N^{3})}$, this turns line 5 into the most computationally expensive operation of the algorithm for large SDPs, and improving the efficiency of this step will be the objective of much of Sections 4 and 5.

### Algorithm convergence

For feasible problems, Algorithm 1 produces a sequence of iterates $(x^{k},s^{k},y^{k})$ that converges to a limit satisfying the optimality conditions in as $k\rightarrow\infty$. The authors in \[SBG^+^18\] show convergence of Algorithm 1 by applying the Douglas-Rachford splitting to a problem reformulation.

In the Douglas-Rachford formulation, lines 5 and 6 become projections onto $\mathcal{K}$ and $\mathcal{K}^{\circ}$ respectively, so that the conic constraints in (6c) always hold. Furthermore, convergence of the residual iterates in (6a)--(6b) can be concluded from the convergence of the splitting variables

which generally holds for Douglas-Rachford splitting \[\].

For infeasible problems, \[\] showed that Algorithm 1 leads to convergence of the successive differences between iterates

For primal infeasible problems ${\deltay} = {\lim_{k\rightarrow\infty}{\deltay^{k}}}$ will satisfy condition, whereas for dual infeasible problems ${\deltax} = {\lim_{k\rightarrow\infty}{\deltax^{k}}}$ is a certificate of.

### Scaling the problem data

The rate of convergence of ADMM and other first-order methods depends in practice on the scaling of the problem data; see \[\]. Particularly for badly conditioned problems, this suggests a preprocessing step where the problem data is scaled in order to improve convergence. For certain problem classes an optimal scaling has been found, see \[ \]. However, the computation of the optimal scaling is often more complicated than solving the original problem. Consequently, most algorithms rely on heuristic methods such as matrix equilibration.

We scale the equality constraints by diagonal positive definite matrices $D$ and $U$. The scaled form of is given by:

with scaled problem data

and the scaled convex cone ${U\mathcal{K}} ≔ {\{{{Uv} \in {\mathbb{R}}^{m}}\mid{v \in \mathcal{K}}\}}$. After solving the original solution is obtained by reversing the scaling:

One heuristic strategy that has been shown to work well in practice is to choose the scaling matrices $D$ and $U$ to equilibrate, i.e. reduce the condition number of, the problem data. The Ruiz equilibration technique described in \[\] iteratively scales the rows and columns of a matrix to have an infinity-norm of $1$ and converges linearly. We apply the modified Ruiz algorithm shown in Algorithm 2 to reduce the condition number of the symmetric matrix $R$

which represents the problem data.

6 $c_{i}\leftarrow\left. \parallel R_{c,i}\parallel \right._{\infty}^{- \frac{1}{2}}$;
Algorithm 2 Modified Ruiz equilibration

Since $R$ is symmetric it suffices to consider the columns $R_{c,i}$ of $R$. At each iteration the scaling routine calculates the norm of each column. For the columns with norms higher than the tolerance $\tau$ scaling vector $c$ is updated with the inverse square root of the norm^11^1For the presented results a value of $\tau = 10^{- 6}$ was chosen.. If the norm is below the tolerance, the corresponding column will be scaled by 1.

Since the matrix $U$ scales the (possibly composite) cone constraint, the scaling must ensure that if $s \in \mathcal{K}$ then ${U^{- 1}s} \in \mathcal{K}$. Let $\mathcal{K}$ be a Cartesian product of $N$ cones as in and partition $U$ into blocks

with block $U_{i} \in {\mathbb{R}}^{m_{i} \times m_{i}}$ which scales the constraint corresponding to $\mathcal{K}_{i}$. For each cone $\mathcal{K}_{i} \in {\mathbb{R}}^{m_{i}}$ that requires a scalar or symmetric scaling, e.g. a second-order cone or positive semidefinite cone, the corresponding block $U_{i}$ is replaced with

where the mean value of the diagonal entries of the original block in $U$, $u_{i} = {{\text{tr}{(U_{i})}}/m_{i}}$, was chosen as a heuristic scaling factor.

### Termination criteria

The termination criteria discussed in this section are based on the unscaled problem data and iterates. Thus, before checking for termination the solver first reverses the scaling according to equations --. To measure the progress of the algorithm, we define the primal and dual residuals of the problem as:

According to Section 3.3 of \[BPC^+^11\] a valid termination criterion is that the size of the norms of the residual iterates in are small. Our algorithm terminates if the residual norms are below the sum of an absolute and a relative tolerance term:

$\left. \parallel r_{p}^{k}\parallel \right._{\infty}$ ${\leq {\epsilon_{abs} + {\epsilon_{rel}\text{max}\left\{ \left. \parallel{Ax^{k}}\parallel \right._{\infty},\left. \parallel s^{k}\parallel \right._{\infty},\left. \parallel b\parallel \right._{\infty} \right\}}}},$ (29a)
$\left. \parallel r_{d}^{k}\parallel \right._{\infty}$ ${\leq {\epsilon_{abs} + {\epsilon_{rel}\text{max}\left\{ \left. \parallel{Px^{k}}\parallel \right._{\infty},\left. \parallel q\parallel \right._{\infty},\left. \parallel{A^{\top}y^{k}}\parallel \right._{\infty} \right\}}}},$ (29b)

where $\epsilon_{abs}$ and $\epsilon_{rel}$ are user defined tolerances.

Following \[\], the algorithm determines if the one-step differences $\deltax^{k}$ and $\deltay^{k}$ of the primal and dual variable fulfil the normalized infeasibility conditions -- up to certain tolerances $\epsilon_{\text{p,inf}}$ and $\epsilon_{d,\inf}$. The solver returns a primal infeasibility certificate if

$\left. \parallel{A^{\top}\deltay^{k}}\parallel \right._{\infty}/\left. \parallel{\deltay^{k}}\parallel \right._{\infty}$ ${\leq \epsilon_{p,\inf}},$ (30a)
$\sigma_{\overline{\mathcal{K}}}\left( {\deltay^{k}} \right)$ ${\leq \epsilon_{p,\inf}},$ (30b)

holds and a dual infeasibility certificate if

$\left. \parallel{P\deltax^{k}}\parallel \right._{\infty}/\left. \parallel{\deltax^{k}}\parallel \right._{\infty}$ ${\leq \epsilon_{d,\inf}},$ (31a)
${q^{\top}\deltax^{k}}/\left. \parallel{\deltax^{k}}\parallel \right._{\infty}$ ${\leq \epsilon_{d,\inf}},$ (31b)
${A\deltax^{k}} + v$ ${\in {\overline{\mathcal{K}}}^{\infty}},$ (31c)
$\text{with~}\left. \parallel v\parallel \right._{\infty}$ ${\leq {\epsilon_{d,\inf}\left. \parallel{\deltax^{k}}\parallel \right._{\infty}}},$

## Chordal Decomposition

As noted in Section 3.3, for large SDPs the eigen-decomposition in the projection step is the principal performance bottleneck for the algorithm. However, since large-scale SDPs often exhibit a certain structure or sparsity pattern, a sensible strategy is to exploit any such structure to alleviate this bottleneck. If the aggregated sparsity pattern is *chordal*, Agler's \[\] and Grone's \[\] theorems can be used to decompose a large PSD constraint into a collection of smaller PSD constraints and additional coupling constraints. The projection step applied to the set of smaller PSD constraints is usually significantly faster than when applied to the original constraint. Since the projections are independent of each other, further performance improvement can be achieved by carrying them out in parallel. Our approach is to apply chordal decomposition to a standard form SDP in the form to produce a decomposed problem, and then transform the resulting decomposed problem back to a problem in the form but with more variables and a collection of smaller PSD cone constraints. This process allows us to apply chordal decomposition as a preprocessing step before the problem is handed to the solver. As discussed in Section 4.2, a chordal sparsity pattern can be imposed on any PSD constraint.

### Graph preliminaries

In the following we define graph-related concepts that are useful to describe the sparsity structure of a problem. A good overview of this topic is given in the survey paper \[VA^+^15\]. Consider the *undirected graph* $G{(V,E)}$ with vertex set $V = {\{ 1,\ldots,n\}}$ and edge set $E \subseteq {V \times V}$. If all vertices are pairwise adjacent, i.e. $E = \left\{ {\{ v,u\}}\mid{{{v,u} \in V},{v \neq u}} \right\}$, the graph is called *complete*. We follow the convention of \[VA^+^15\] by defining a *clique* as a subset of vertices $\mathcal{C} \subseteq V$ that induces a *maximal* complete subgraph of $G$. The number of vertices in a *clique* is given by the cardinality $|\mathcal{C}|$. A *cycle* is a path of edges (i.e. a sequence of distinct edges) joining a sequence of vertices in which only the first and last vertices are repeated.

The following decomposition theory relies on a subset of graphs that exhibit the important property of *chordality*. A graph $G$ is *chordal* (or *triangulated*) if every cycle of length greater than three has a *chord*, which is an edge between nonconsecutive vertices of the cycle. A non-chordal graph can always be made chordal by adding extra edges.

An undirected graph with $n$ vertices can be used to represent the sparsity pattern of a symmetric matrix $S \in {\mathbb{S}}^{n}$. Every nonzero entry $S_{ij} \neq 0$ in the lower triangular part of the matrix introduces an edge ${(i,j)} \in E$. An example of a sparsity pattern and the associated graph is shown in Figure 1(a--b).

Figure 1: (a) Aggregate sparsity pattern, (b) sparsity graph G (V,E), and (c) clique tree 𝒯 (ℬ,ℰ).

For a given sparsity pattern $G{(V,E)}$, we define the following symmetric sparse matrix cones:

Given the definition in and a matrix $S \in {{\mathbb{S}}^{n}(E,0)}$, note that the diagonal entries $S_{ii}$ and the off-diagonal entries $S_{ij}$ with ${(i,j)} \in E$ may be zero or nonzero. Moreover, we define the cone of positive semidefinite completable matrices as

For a matrix $Y \in {{\mathbb{S}}_{+}^{n}{(E,?)}}$ we can find a positive semidefinite completion by choosing appropriate values for all entries ${(i,j)} \notin E$. An algorithm to find this completion is described in \[VA^+^15\]. An important structure that conveys a lot of information about the nonzero blocks of a matrix, or equivalently the cliques of a chordal graph, is the *clique tree* (or *junction tree*). For a chordal graph $G$ let $\mathcal{B} = {\{\mathcal{C}_{1},\ldots,\mathcal{C}_{p}\}}$ be the set of cliques. The clique tree $\mathcal{T}{(\mathcal{B},\mathcal{E})}$ is formed by taking the cliques as vertices and by choosing edges from $\mathcal{E} \subseteq {\mathcal{B} \times \mathcal{B}}$ such that the tree satisfies the *running-intersection property*:

### Definition 4.1 (Running intersection property)

For each pair of cliques $\mathcal{C}_{i}$, $\mathcal{C}_{j} \in \mathcal{B}$, the intersection $\mathcal{C}_{i} \cap \mathcal{C}_{j}$ is contained in all the cliques on the path in the clique tree connecting $\mathcal{C}_{i}$ and $\mathcal{C}_{j}$.

This property is also referred to as the clique-intersection property in \[NFF^+^03\] and the induced subtree property in \[VA^+^15\]. For a given chordal graph, a clique tree can be computed using the algorithm described in \[\]. The clique tree for an example sparsity pattern is shown in Figure 1(c).

In a *post-ordered* clique tree the descendants of a node are given consecutive numbers, and a suitable post-ordering can be found via depth-first search. For a clique $\mathcal{C}_{\ell}$ we refer to the first clique encountered on the path to the root as its parent clique $\mathcal{C}_{par}$. Conversely $\mathcal{C}_{\ell}$ is called the child of $\mathcal{C}_{par}$. If two cliques have the same parent clique we refer to them as siblings.

We define the function ${par}:{2^{V}\rightarrow 2^{V}}$ and the multivalued function ${ch}:{2^{V}\rightrightarrows 2^{V}}$ such that ${par}{(\mathcal{C}_{\ell})}$ and ${ch}{(\mathcal{C}_{\ell})}$ return the parent clique and set of child cliques of $\mathcal{C}_{\ell}$, respectively, where $2^{V}$ is the power set (set of all subsets) of $V$.

Note that each clique in Figure 1(c) has been partitioned into two sets. The upper row represents the separators $\eta_{\ell} = {\mathcal{C}_{\ell} \cap {{par}{(\mathcal{C}_{\ell})}}}$, i.e. all clique elements that are also contained in the parent clique. We call the sets of the remaining vertices shown in the lower rows the clique residuals or supernodes $\nu_{\ell} = {\mathcal{C}_{\ell} \smallsetminus \eta_{\ell}}$. Keeping track of which vertices in a clique belong to the supernode and the separator is useful as the information is needed to perform a positive semidefinite completion. Following the authors in \[\], we say that two cliques $\mathcal{C}_{i}$, $\mathcal{C}_{j}$ form a separating pair $\mathcal{P}_{ij} = {\{\mathcal{C}_{i},\mathcal{C}_{j}\}}$ if their intersection is non-empty and if every path in the underlying graph $G$ from a vertex $\mathcal{C}_{i} \smallsetminus \mathcal{C}_{j}$ to a vertex $\mathcal{C}_{j} \smallsetminus \mathcal{C}_{i}$ contains a vertex of the intersection $\mathcal{C}_{i} \cap \mathcal{C}_{j}$.

### Agler's and Grone's theorems

To explain how the concepts in the previous section can be used to decompose a positive semidefinite constraint, we first consider an SDP in standard primal form:

with variable $X$ and coefficient matrices ${A_{k},C} \in {\mathbb{S}}^{n}$. The corresponding dual problem is

with dual variable $y \in {\mathbb{R}}^{m}$ and slack variable $S$. Let us assume that the problem matrices in and each have their own sparsity pattern

The *aggregate sparsity* of the problem is given by the graph $G{(V,E)}$ with edge set

In general $G{(V,E)}$ will not be chordal, but a *chordal extension* can be found by adding edges to the graph. We denote the extended graph as $G{(V,\overline{E})}$, where $E \subseteq \overline{E}$. Finding the minimum number of additional edges required to make the graph chordal is an NP-complete problem \[\]. Consider a $0$--$1$ matrix $M$ with edge set $E$. A commonly used heuristic method to compute the chordal extension is to perform a symbolic Cholesky factorisation of $M$ \[\], with the edge set of the Cholesky factor then providing the chordal extension $\overline{E}$. To simplify the notation in the remainder of the article, we henceforward assume that $E$ represents a chordal graph or has been appropriately extended.

Using the aggregate sparsity of the problem we can modify the constraints on the matrix variables in and to be in the respective sparse positive semidefinite matrix spaces:

We further define the entry-selector matrices $T_{\ell} \in {\mathbb{R}}^{{|\mathcal{C}_{\ell}|} \times n}$ for a clique $\mathcal{C}_{\ell}$ as

where $\mathcal{C}_{\ell}{(i)}$ is the $i$th vertex of $\mathcal{C}_{\ell}$. We can express the constraints in in terms of multiple smaller coupled constraints using Grone's and Agler's theorems.

### Theorem 1 (Grone's theorem \[GJSW84\])

Let $G{(V,E)}$ be a chordal graph with a set of maximal cliques $\{\mathcal{C}_{1},\ldots,\mathcal{C}_{p}\}$. Then $X \in {{\mathbb{S}}_{+}^{n}{(E,?)}}$ if and only if

for all $\ell = {1,\ldots,p}$.

Applying this theorem to while restricting $X$ to the positive semidefinite completable matrix cone as in yields the decomposed problem:

For the dual problem we utilise Agler's theorem, which is the dual to Theorem 1. ‣ 4.2 Agler’s and Grone’s theorems ‣ 4 Chordal Decomposition ‣ COSMO: A conic operator splitting method for convex conic problems"):

### Theorem 2 (Agler's theorem \[AHMR88\])

Let $G{(V,E)}$ be a chordal graph with a set of maximal cliques $\{\mathcal{C}_{1},\ldots,\mathcal{C}_{p}\}$. Then $S \in {{\mathbb{S}}_{+}^{n}{(E,0)}}$ if and only if there exist matrices $S_{\ell} \in {\mathbb{S}}_{+}^{|\mathcal{C}_{\ell}|}$ for $\ell = {1,\ldots,p}$ such that

Note that the matrices $T_{\ell}$ serve to extract the submatrix $S_{\ell}$ such that $S_{\ell} = {T_{\ell}ST_{\ell}^{\top}}$ has rows and columns corresponding to the vertices of the clique $C_{\ell}$. With this theorem, we transform the dual form SDP in with the restriction on $S$ in to arrive at:

### Returning a decomposed problem into standard SDP form

After the decomposition results of Section 4.2 have been applied, the SDP problem has to be transformed back into standard form. For the undecomposed problem in, this is achieved by first relabeling $y$ as $x$. We then choose $P = 0_{n \times n}$, $q = {- b}$, define $A = {\lbrack{{svec}{(A_{1})}},\ldots,{{svec}{(A_{m})}}\rbrack}$, $b = {{svec}{(C)}}$ and $s = {{svec}{(S)}}$.

To transform the decomposed dual problem, we will make use of the fact that the decision variable $S \in {\mathbb{S}}^{n}$ and all the submatrices $S_{\ell}$ are symmetric and consider instead $s_{\ell} = {{svec}{(S_{\ell})}}$. The main challenge is to keep track of the overlapping entries in the individual blocks and ensure they sum to the original entry in $S$. Different possible transformations achieving this are described in \[\].

All the necessary information about the overlapping entries is stored in the clique tree $\mathcal{T}{(\mathcal{B},\mathcal{E})}$ that represents the sparsity pattern of $S$. We assume that the clique tree is post-ordered with cliques $\mathcal{C}_{1},\ldots,\mathcal{C}_{p}$. Define a vector to represent slack variables for overlapping entries $\theta ≔ {\lbrack\theta_{1},\ldots,\theta_{n_{o}}\rbrack}^{\top}$, where $n_{o} ≔ {\sum_{\ell = 1}^{p}\frac{\left| \eta_{\ell} \right|{({\left| \eta_{\ell} \right| + 1})}}{2}}$ is the total number of overlapping entries in the upper triangle of the sparsity pattern. The $s$ vector of the decomposed problem is created by stacking the vectorized subblocks $s_{\ell}$ according to the postordering of the clique tree. Define $\omega{(i,j,\ell)}$ as the index of $s$ corresponding to the $(i,j)$th element of block $S_{\ell}$. The equality constraint in problem can be represented in the equivalent standard form as:

The matrices ${\overset{\sim}{A}}_{k}^{\ell}$ and ${\overset{\sim}{B}}^{\ell}$ take on the values of $A_{k}$ and $B$ in the locations corresponding to the elements in the submatrix $S_{\ell}$. If a matrix entry of clique $\mathcal{C}_{l}$ in $A_{k,{ij}}^{\ell}$ and $B_{ij}^{\ell}$ is overlapped by an entry of the parent clique, i.e. both $(i,j)$ are included in ${sep}{(\mathcal{C}_{l})}$, it is set to zero. Each column of the linking matrix $L \in {\mathbb{R}}^{m_{d} \times n_{o}}$ links one overlapping entry in the clique tree. $L$ is generated by first collecting all the matrix indices ${(i,j)}_{\ell}$ of the separators ${sep}{(\mathcal{C}_{\ell})}$ in the clique tree:

Then $L$ is constructed column-by-column, each representing one overlapping entry. The column vector $l_{c}$ is equal to $1$ in the row $r$ corresponding to the ${(i,j)}_{\ell}$-th entry of $S_{\ell}$ and $- 1$ in the row corresponding to the same entry of the parent block $S_{k}$, where $\mathcal{C}_{\ell} = {{ch}{(\mathcal{C}_{k})}}$. Thus, each element in $l_{c}$ is defined by:

As an example consider a problem with $m = 1$ and $p = 3$ and the simple sparsity pattern and clique tree given by:

Using the transformation in this constraint can be represented by three constraints on the submatrices $S_{1}$, $S_{2}$ and $S_{3}$ and six overlap variables $\theta_{1},\ldots,\theta_{6}$:

Notice how the overlap variables drop out if the original matrix $S$ is reassembled according to Theorem 2. ‣ 4.2 Agler’s and Grone’s theorems ‣ 4 Chordal Decomposition ‣ COSMO: A conic operator splitting method for convex conic problems") by adding the entries of each subblock.

## Clique Merging

Given an initial decomposition with (chordally completed) edge set $E$ and a set of cliques $\{\mathcal{C}_{1},\ldots,\mathcal{C}_{p}\}$, we are free to re-merge any number of cliques back into larger blocks. This is equivalent to treating *structural* zeros in the problem as *numerical* zeros, leading to additional edges in the graph. Looking at the decomposed problem in and, the effects of merging two cliques $\mathcal{C}_{i}$ and $\mathcal{C}_{j}$ are twofold:

We replace two positive semidefinite matrix constraints of dimensions $\left| \mathcal{C}_{i} \right|$ and $\left| \mathcal{C}_{j} \right|$ with one constraint on a larger clique with dimension $\left| {\mathcal{C}_{i} \cup \mathcal{C}_{j}} \right|$, where the increase in dimension depends on the size of the overlap.

We remove consistency constraints for the overlapping entries between $\mathcal{C}_{i}$ and $\mathcal{C}_{j}$, thus reducing the size of the linear system of equality constraints.

When merging cliques these two factors have to be balanced, and the optimal merging strategy depends on the particular SDP solution algorithm employed. In \[NFF^+^03\] and \[\] a clique tree is used to search for favourable merge candidates; We will refer to their two approaches as SparseCoLO and the *parent-child* strategy, respectively, in the following sections. We will then propose a new merging method in Section 5.2 whose performance is superior to both methods when used in ADMM. Given a merging strategy, Algorithm 3 describes how to merge a set of cliques within the set $\mathcal{B}$ and update the edge set $\mathcal{E}$ accordingly.

Input: A set of cliques ℬ with edge set ℰ, a subset of cliques ℬm = {𝒞m, 1, 𝒞m, 2, …, 𝒞m, r} ⊆ ℬ to be merged.
Output: A reduced set of cliques $\hat{\mathcal{B}}$ with edge set $\hat{\mathcal{E}}$ and the merged clique 𝒞m.
1 $\hat{\mathcal{E}}\leftarrow\mathcal{E}$;
3 $\hat{\mathcal{B}}\leftarrow{{({\mathcal{B} \smallsetminus \mathcal{B}_{m}})} \cup {\{\mathcal{C}_{m}\}}}$;
4 Remove edges {(𝒞i,𝒞j) ∣ i ≠ j, 𝒞i, 𝒞j ∈ ℬm} in $\hat{\mathcal{E}}$;
5 Replace edges {(𝒞i,𝒞j) ∣ 𝒞i ∈ ℬm, 𝒞j ∉ ℬm} with (𝒞m,𝒞j) in $\hat{\mathcal{E}}$;
Algorithm 3 Function mergeCliques (ℬ,ℰ,ℬm).

### Existing clique tree-based strategies

The parent-child strategy described in \[\] traverses the clique tree in a depth-first order and merges a clique $\mathcal{C}_{\ell}$ with its parent clique $\mathcal{C}_{{par}{(\ell)}} ≔ {{par}{(\mathcal{C}_{\ell})}}$ if at least one of the two following conditions are met:

with heuristic parameters $t_{fill}$ and $t_{size}$. These conditions keep the amount of extra fill-in and the supernode cardinalities below the specified thresholds. The SparseCoLO strategy described in \[NFF^+^03\] and \[\] considers parent-child as well as sibling relationships. Given a parameter $\sigma > 0$, two cliques $\mathcal{C}_{i},\mathcal{C}_{j}$ are merged if the following merge criterion holds

This approach traverses the clique tree depth-first, performing the following steps for each clique $\mathcal{C}_{\ell}$:

For each clique pair $\left\{ {(\mathcal{C}_{i},\mathcal{C}_{j})}\mid{{\mathcal{C}_{i},\mathcal{C}_{j}} \in {{ch}\left( \mathcal{C}_{\ell} \right)}} \right\}$, check if holds, then:

$\mathcal{C}_{i}$ and $\mathcal{C}_{j}$ are merged, or

if ${({\mathcal{C}_{i} \cup \mathcal{C}_{j}})} \supseteq \mathcal{C}_{\ell}$, then $\mathcal{C}_{i}$, $\mathcal{C}_{j}$, and $\mathcal{C}_{\ell}$ are merged.

For each clique pair $\left\{ \left( \mathcal{C}_{i},\mathcal{C}_{\ell} \right)\mid{\mathcal{C}_{i} \in {{ch}\left( \mathcal{C}_{\ell} \right)}} \right\}$, merge $\mathcal{C}_{i}$ and $\mathcal{C}_{\ell}$ if is satisfied.

We note that the open-source implementation of the SparseCoLO algorithm described in \[NFF^+^03\] follows the algorithm outlined here, but also employs a few additional heuristics.

An advantage of these two approaches is that the clique tree can be computed easily and the conditions are inexpensive to evaluate. However, a disadvantage is that choosing parameters that work well on a variety of problems and solver algorithms is difficult. Secondly, clique trees are not unique and in some cases it is beneficial to merge cliques that are not directly related on the particular clique tree that was computed. To see this, consider a chordal graph $G{(V,E)}$ consisting of three connected subgraphs:

and some additional vertices $\{ 1,2,{m_{a} + 1}\}$. The graph is connected as shown in Figure 2(a), where the complete subgraphs are represented as nodes $V_{a},V_{b},V_{c}$. A corresponding clique tree is shown in Figure 2(b).

Figure 2: Sparsity graph (a) that can lead to clique tree (b) with an advantageous “nephew-uncle” merge between 𝒞1 and 𝒞3.

By choosing the cardinality $\left| V_{c} \right|$, the overlap between cliques $\mathcal{C}_{1} = {{\{ 1,2\}} \cup V_{c}}$ and $\mathcal{C}_{3} = {{\{{m_{a} + 1}\}} \cup V_{c}}$ can be made arbitrarily large while $\left| V_{a} \right|$, $\left| V_{b} \right|$ can be chosen so that any other merge is disadvantageous. However, neither the parent-child strategy nor SparseCoLO would consider merging $\mathcal{C}_{1}$ and $\mathcal{C}_{3}$ since they are in a "nephew-uncle" relationship. In fact for the particular sparsity graph in Figure 2(a) eight different clique trees can be computed. Only in half of them do the cliques $\mathcal{C}_{1}$ and $\mathcal{C}_{3}$ appear in a parent-child relationship. Therefore, a merge strategy that only considers parent-child relationships would miss this favorable merge in half the cases.

### A new clique graph-based strategy

To overcome the limitations of existing strategies we propose a merging strategy based on the *reduced clique graph* $\mathcal{G}{(\mathcal{B},\xi)}$, which is defined as the union of all possible clique trees of $G$; see \[\] for a detailed discussion. The set of vertices of this graph is given by the maximal cliques of the sparsity pattern. We then create the edge set $\xi$ by introducing edges between pairs of cliques $(\mathcal{C}_{i},\mathcal{C}_{j})$ if they form a separating pair $\mathcal{P}_{ij}$. We remark that $\xi$ is a subset of the edges present in the *clique intersection graph* which is obtained by introducing edges for every two cliques that intersect. However, the reduced clique graph has the property that it remains a valid reduced clique graph of the altered sparsity pattern after performing a permissible merge between two cliques. This is not always the case for the clique intersection graph. For convenience, we will refer to the reduced clique graph simply as the clique graph in the following sections. Based on the permissibility condition for edge reduction in \[\] we define a permissibility condition for clique merges:

### Definition 5.1 (Permissible merge)

Given a reduced clique graph $\mathcal{G}{(\mathcal{B},\xi)}$, a merge between two cliques ${(\mathcal{C}_{i},\mathcal{C}_{j})} \in \xi$ is permissible if for every common neighbour $\mathcal{C}_{k}$ it holds that ${\mathcal{C}_{i} \cap \mathcal{C}_{k}} = {\mathcal{C}_{j} \cap \mathcal{C}_{k}}$.

We further define a monotone *edge weighting function* $e:{{2^{V} \times 2^{V}}\rightarrow{\mathbb{R}}}$ that assigns a weight $w_{ij}$ to each edge ${(\mathcal{C}_{i},\mathcal{C}_{j})} \in \xi$:

This function is used to estimate the per-iteration computational savings of merging a pair of cliques depending on the targeted algorithm and hardware. It evaluates to a positive number if a merge reduces the per-iteration time and to a negative number otherwise. For a first-order method, whose per-iteration cost is dominated by an eigenvalue factorisation with complexity $\mathcal{O}\left( |\mathcal{C}|^{3} \right)$, a simple choice would be:

More sophisticated weighting functions can be determined empirically; see Section 7.5. After a weight has been computed for each edge $(\mathcal{C}_{i},\mathcal{C}_{j})$ in the clique graph, we merge cliques as outlined in Algorithm 4.

Input: A weighted clique graph 𝒢 (ℬ,ξ).
Output: A merged clique graph $\mathcal{G}{(\hat{\mathcal{B}},\hat{\xi})}$.
1 $\hat{\mathcal{B}}\leftarrow\mathcal{B}$ and ξ̂ ← ξ;
4 choose permissible edge (𝒞i,𝒞j) with maximum wi j;
7 ${\hat{\mathcal{B}},\hat{\xi},\mathcal{C}_{m}}\leftarrow{{mergeCliques}\left( \hat{\mathcal{B}},\hat{\xi},\mathcal{B}_{m} \right)}$;
8 for each edge (𝒞m,𝒞ℓ) ∈ ξ̂ do
Algorithm 4 Clique graph-based merging strategy.

This strategy considers the edges in terms of their weights, starting with the permissible clique pair $(\mathcal{C}_{i},\mathcal{C}_{j})$ with the highest weight $w_{ij}$. If the weight is positive, the two cliques are merged and the edge weights for all edges connected to the merged clique $\mathcal{C}_{m} = {\mathcal{C}_{i} \cup \mathcal{C}_{j}}$ are updated. This process continues until no edges with positive weights remain.

The clique graph for the clique tree in Figure 1(c) is shown in Figure 3(a) with the edge weighting function in. Following Algorithm 4 the edge with the largest weight is considered first and the corresponding cliques are merged, i.e. $\{ 3,6,7,8\}$ and $\{ 6,7,8,9\}$. Note that the merge is permissible because both cliques intersect with the only common neighbour $\{ 4,5,8\}$ in the same way. The revised clique graph $\mathcal{G}{(\hat{\mathcal{B}},\hat{\xi})}$ is shown in Figure 3(b). Since no edges with positive weights remain, the algorithm stops.

Figure 3: (a) Clique graph 𝒢 (ℬ,ξ) of the clique tree in Figure 1(c) with edge weighting function e (𝒞i,𝒞j) = |𝒞i|3 + |𝒞j|3 − |𝒞i∪𝒞j|3 and (b) clique graph $\mathcal{G}{(\hat{\mathcal{B}},\hat{\xi})}$ after merging the cliques {3, 6, 7, 8} and {6, 7, 8, 9} and updating edge weights.

After Algorithm 4 has terminated, it is possible to recompute a valid clique tree from the revised clique graph. This can be done in two steps. First, the edge weights in $\mathcal{G}{(\hat{\mathcal{B}},\hat{\xi})}$ are replaced with the cardinality of their intersection:

Second, a clique tree is then given by any *maximum weight spanning tree* of the newly weighted clique graph, e.g. using Kruskal's algorithm described in \[\].

Our merging strategy has some clear advantages over competing approaches. Since the clique graph covers a wider range of merge candidates, it will consider edges that do not appear in clique tree-based approaches such as the "nephew-uncle" example in Figure 2. Moreover, the edge weighting function allows one to make a merge decision based on the particular solver algorithm and hardware used. One downside is that this approach is more computationally expensive than the other methods. However, our numerical experiments show that the time spent on finding the clique graph, merging the cliques, and recomputing the clique tree represent only a very small fraction of the total computational savings relative to other merging methods when solving SDPs.

## Open-Source Implementation

We have implemented our algorithm in the Conic Operator Splitting Method (COSMO), an open-source package written in Julia \[\]. Julia allows the solver to be written in a flexible, modular and extensible way, while still maintaining the benefits of a fast compiled language. The source code and documentation are available at

[https://github.com/oxfordcontrol/COSMO.jl](https://github.com/oxfordcontrol/COSMO.jl).

COSMO offers the user two interfaces to describe the constraints of the optimisation problem: a direct interface, and an interface to the modelling languages JuMP \[\] and Convex.jl \[UMZ^+^14\]. These interfaces connect the solver to the Julia optimisation ecosystem which provide flexible problem description and automatic problem reformulation.

As shown in Algorithm 1 the two main steps of the algorithm are solving a linear system and projecting onto a Cartesian product of cones. The implementation of these two parts allows customisation by the user. For the solution of the linear system in the user can either use the QDLDL \[SBG^+^18\] solver provided with COSMO, the standard sparse solver from SuiteSparse \[D^+^15\], or choose one of the provided interfaces to direct and indirect solvers, e.g. Pardiso \[SGK^+^10, KAA^+^15\], conjugate gradient, minimal residual method, or link their own implementation.

The second important part of the algorithm is the projection step onto a Cartesian product of convex sets. By default COSMO supports the zero cone, the nonnegative orthant, the hyperbox, the second-order cone, the PSD cone, the exponential cone and its dual, and the power cone and its dual. Our Julia implementation also allows the user to define their own convex cones^22^2To allow infeasibility detection the user has to either define a convex cone, a convex compact set or a composition of the two. and custom projection functions. To implement a custom cone $\mathcal{K}_{c}$ the user has to provide:

a projection function that projects an input vector onto the cone

a function that determines if a vector is inside the dual cone $\mathcal{K}_{c}^{\ast}$

a function that determines if a vector is inside the recession cone of $- \mathcal{K}_{c}$

The latter two functions are required for our solver to implement checks for infeasibility as described in Sections 2.1 and 3.4. An example that shows the advantages of defining a custom cone is provided in Section 7.2.

The authors in \[\] used COSMO's algorithm with a specialized implementation of the projection function for positive semidefinite constraints. The projection method used approximate matrix eigendecompositions to significantly reduce the projection time, while maintaining all the features of COSMO such as scaling, infeasibility detection and interfaces to linear system solvers. It was demonstrated that this can provide a significant, up to 20x, reduction in solve time.\

Given a problem with multiple constraints, the projection step can be carried out in parallel. This is particularly advantageous when used in combination with chordal decomposition, which typically yields a large number of smaller PSD constraints. For the eigendecomposition involved in the projection step of a PSD constraint, the LAPACK \[ABB^+^99\] function sveyr is used, which can also utilise multiple threads. Consequently, this leads to two-level parallelism in the computation, i.e on the higher level the projection functions are carried out in parallel and each projection function independently calls sveyr. Determining the optimal allocation of the CPU cores to each of these tasks depends on the number of PSD constraints and their dimensions and is a difficult problem. For the problem sets considered in section 7 we achieved the best performance by running sveyr single-threaded and using all physical CPUs to carry out the projection functions in parallel.

Moreover, Julia's type abstraction features are used to enable the solver to solve problems of arbitrary floating-point precision. This allows for example to reduce the memory usage of the solver for very large problems by switching to 32-bit single-precision floating-point format.

## Numerical Results

This section presents benchmark results of COSMO against the interior-point solver MOSEK v$9.0$ and the accelerated first-order ADMM solver SCS v$2.1.1$. When applied to a quadratic program, COSMO's main algorithm becomes very similar to the first-order QP solver OSQP. To test the performance penalty of using a pure Julia implementation against a similar C implementation we also compare our solver against OSQP v$0.6.0$ on QP problems.

We selected a number of problem sets to test different aspects of COSMO. The advantage of supporting a quadratic cost function in a conic solver is shown by solving QPs from the Maros and Mészáros QP repository \[\] in Section 7.1 and SDPs with quadratic objectives in the form of nearest correlation matrix problems in Section 7.3.

To highlight the advantages of implementing custom constraints, we consider a problem set with doubly-stochastic matrices in Section 7.2. We then show how chordal decomposition can speed up the solver for SDPs that exhibit a block-arrow sparsity pattern in Section 7.4.

The performance of chordal decomposition is further explored in Section 7.5 by solving large structured problems from the SDPLib benchmark set \[\] as well as some non-chordal SDPs generated with sparsity patterns from the SuiteSparse Matrix Collections \[\]. Using the same problems we additionally evaluate the performance of different clique merging strategies.

All the experiments were carried out on a computing node of the University of Oxford ARC-HTC cluster with 16 logical Intel Xeon E5-2560 cores and $64\ {GB}$ of DDR3 RAM. All the problems were run using Julia v$1.3$ and the problems were passed to the solvers via MathOptInterface \[\].

To evaluate the accuracy of the returned solution we compute three errors adapted from the DIMACS error measures for SDPs \[\]:

where $A_{a}$, $b_{a}$ and $y_{a}$ correspond to the rows of $A$, $b$ and $y$ that represent active constraints. This is to ensure meaningful values even if the problem contains inactive constraints with very large, or possibly infinite, values $b_{i}$. The maximum of the three errors for each problem and solver is reported in the results below.

We configured COSMO, MOSEK, SCS and OSQP to achieve an accuracy of $\epsilon = {10^{- 3}}$. We set the maximum allowable solve time for the Maros and Mészáros problems to $5\ \min$ and to $30\ \min$ for the other problem sets. All other solver parameters were set to the solvers' standard configurations. COSMO uses a Julia implementation of the QDLDL solver to factor the quasi-definite linear system. Similarly, we configured SCS to use a direct solver for the linear system.

### Maros and Mészáros QP test set

The Maros and Mészáros test problem set \[\] is a repository of challenging convex QP problems that is widely used to compare the performance of QP solvers. For comparison metrics we compute the failure rate, the number of fastest solve time and the normalized shifted geometric mean for each solver. The shifted geometric mean is more robust against large outliers (compared to the arithmetic mean) and against small outliers (compared to the geometric mean) and is commonly used in optimisation benchmarks; see \[SBG^+^18, Mit\]. The shifted geometric mean $\mu_{g,s}$ is defined as:

with total solver time $t_{p,s}$ of solver $s$ and problem $p$, shifting factor $sh$ and size of the problem set $n$. In the reported results a shifting factor of ${sh} = 10$ was chosen and the maximum allowable time $t_{p,s} = {300\ s}$ was used if solver $s$ failed on problem $p$. Lastly, we normalize the shifted geometric mean for solver $s$ by dividing by the geometric mean of the fastest solver. The failure rate $f_{r,s}$ is given by the number of unsolved problems compared to the total number of problems in the problem set. As unsolved problems we count instances where the algorithm does not converge within the allowable time or fails during the setup or solve phase. Table 7.1 shows the normalized shifted geometric mean and the failure rate for each solver. Additionally, the number of cases where solver $s$ was the fastest solver is shown.

Normalized shifted geometric mean

Number of fastest solve time

OSQP shows the best performance in terms of lowest failure rates, number of fastest solves and in the shifted geometric mean of solve times. COSMO follows very closely. The shifted geometric mean of MOSEK seems to suffer from a higher failure rate compared to OSQP/COSMO, and SCS fails on a large number of problems. The higher failure rate could be due to the necessary transformation into a second-order-cone problem.
For this problem set of QPs COSMO’s algorithm reduces, with some minor differences, to the algorithm of OSQP. Consequently, this benchmark is useful to evaluate the performance penalty that COSMO pays due to its implementation in the higher-order language Julia. The results in Table 7.1 show that the performance difference is very small. This can also be seen by looking at the solve times of each solver for increasing problem dimension, as shown in Figure 4.

Figure 4: Solve time of benchmarked solvers for problems of the Maros and Mészáros QP problem set. Only problem results classified as solved are shown. The problems are ordered by increasing number of non-zeros in the constraint matrix.

COSMO and OSQP have very similar solve times, aside from very small problems that are solved in under 1×10−5 s to 1×10−4 s. This difference is primarily due to overheads incurred from features in our Julia implementation that support more than one constraint type during problem setup. The marginally better resulting performance of OSQP for the smallest problems in the test set is the reason that OSQP is the faster solver in a larger number of cases in Table 7.1.
7.2 Custom convex cones
In many cases writing a custom solver algorithm for a particular problem can be faster than using available solver packages if a particular aspect of the problem structure can be exploited to speed up parts of the computations. As mentioned earlier, COSMO supports user customisation by allowing the definition of new convex cones. This is useful if constraints of the problem can be expressed using this new convex cone and a fast projection method onto the cone exists. A fast specialized projection method in an ADMM framework has for example been used by the authors in [] to solve the error-correcting code decoding problem.
To demonstrate the advantage of custom convex cones, consider the problem of finding the doubly stochastic matrix that is nearest, in the Frobenius norm, to a given symmetric matrix C ∈ 𝕊n. Doubly stochastic matrices are used for instance in spectral clustering [] and matrix balancing [RHD+14]. A specialized algorithm for this problem type has been recently discussed by the authors in []. Doubly stochastic matrices have the property that all rows and columns each sum to one and all entries are nonnegative. The nearest doubly stochastic matrix X can be found by solving the following optimisation problem:

\text{minimize} &amp; {\frac{1}{2}\left. \parallel{X - C}\parallel \right._{F}^{2}} \\
\text{subject to} &amp; {X_{ij} \geq 0} \\
&amp; {{X\mathbf{1}} = \mathbf{1}} \\
&amp; {{{X^{\top}\mathbf{1}} = \mathbf{1}},}

with symmetric real matrix C ∈ 𝕊n and decision variable X ∈ ℝn × n. This problem can be solved as a QP in the following form using equality and inequality constraints:

\text{minimize} &amp; {\frac{1}{2}{({{{x^{\top}x} - {2c^{\top}x}} + {c^{\top}c}})}} \\
\text{subject to} &amp; {{{\begin{bmatrix}
{\mathbf{1}_{n}^{\top} \otimes I_{n}} \\
{I_{n} \otimes \mathbf{1}_{n}^{\top}} \\
\end{bmatrix}x} + s} = \begin{bmatrix}
&amp; {{s \in {{\{ 0\}}^{4n} \times {\mathbb{R}}_{+}^{n^{2}}}},}

with x = vec (X) and c = vec (C) However, the problem can be written in a more compact form by using a custom projection function to project the matrix iterate onto the affine set of matrices 𝒞∑, whose rows and columns each sum to one. In general the projection of vector s ∈ ℝn onto the affine set 𝒞a = {s ∈ ℝn ∣ A s = b} is given by:

where A is assumed to have full rank. In the case of 𝒞a = 𝒞∑ we can exploit the fact that the inverse of A A⊤ can be efficiently computed. The projection can be carried out as described in Algorithm 5; see Appendix B.1 for a derivation.

{I_{n - 1} \otimes \mathbf{1}_{n}^{\top}} &amp; \mathbf{0}_{n - {1 \times n}}
\end{bmatrix}^{\top}$;
4 $\eta_{2} = {{\frac{1}{n}\left( {I_{n - 1} + {\mathbf{1}_{n - 1}\mathbf{1}_{n - 1}^{\top}}} \right)} \cdot \left( {r_{2} - {\frac{1}{n}\mathbf{1}_{n - 1}\mathbf{1}_{n}^{\top}r_{1}}} \right)}$;
5 $\eta_{1} = {\frac{1}{n}\left( {r_{1} - {\mathbf{1}_{n}\mathbf{1}_{n - 1}^{\top}\eta_{2}}} \right)}$;
Algorithm 5 Projection of s ∈ ℝn onto C∑

Notice that Algorithm 5 can be implemented efficiently without ever assembling and storing A and 11⊤. By using the custom convex set 𝒞∑ and the corresponding projection function, can now be rewritten as:

\text{minimize} &amp; {{({1/2})}{({{{x^{\top}x} - {2c^{\top}x}} + {c^{\top}c}})}} \\
\text{subject to} &amp; {{{\begin{bmatrix}
\end{bmatrix}x} + s} = \mathbf{0}_{2n^{2}}} \\
&amp; {{s \in {\mathcal{C}_{\sum} \times {\mathbb{R}}_{+}^{n^{2}}}}.}

The sparsity pattern of the new constraint matrix A only consists of two diagonals and the number of non-zeros reduces from 3 n2 to 2 n2. We expect this to reduce the initial factorisation time of the linear system in as well as the forward- and back-substitution steps.
Figure 5 shows the total solve time of all the solvers for problem with randomly generated dense matrix C with Ci j ∼ 𝒰 and increasing matrix dimension. Additionally, we show the solve time for COSMO in the problem form and with a specialized custom set and projection function as in.

Figure 5: Solve time of benchmarked solvers for increasing problem size of doubly stochastic matrix problems. The orange line shows the solve time of COSMO(CS) with a custom convex set and projection function.

It is not surprising that COSMO and OSQP scale in the same way for this problem type. MOSEK is slightly slower for smaller problem dimension and overtakes COSMO/OSQP for problems of dimensions n ≥ 500. This might be due to fact that MOSEK uses a faster multi-threaded linear system solver while OSQP/COSMO rely on the single-threaded solver QDLDL. The longer solve time of SCS is due to slow convergence of the algorithm for this problem type. Furthermore, when the problem is solved with a custom convex set as in COSMO(CS) is able to outperform all other solvers. Table LABEL:tb:doubly_stochastic shows the total solve time and the factorisation time of the two versions of COSMO for small, medium and large problems. As predicted the lower solve time can be mainly attributed to the faster factorisation time.

solving with a custom convex set 𝒞∑ and projection function

7.3 Nearest correlation matrix
Consider the problem of projecting a matrix C onto the set of correlation matrices, i.e. real symmetric positive semidefinite matrices with diagonal elements equal to 1. This problem is for example relevant in portfolio optimisation []. The correlation matrix of a stock portfolio might lose its positive semidefiniteness due to noise and rounding errors of previous data manipulations. Consequently, it is of interest to find the nearest correlation matrix X to a given data matrix C ∈ ℝn × n. The problem is given by:

\text{minimize} &amp; {\frac{1}{2}\left. \parallel{X - C}\parallel \right._{F}^{2}} \\
\text{subject to} &amp; {{X_{ii} = 1},{i = {1,\ldots,n}}} \\

In order to transform the problem into the standard form used by COSMO, C and X are vectorized and the objective function is expanded:

\text{minimize} &amp; {{({1/2})}{({{{x^{\top}x} - {2c^{\top}x}} + {c^{\top}c}})}} \\
\text{subject to} &amp; {{{\begin{bmatrix}
\end{bmatrix}x} + s} = \begin{bmatrix}
&amp; {{s \in {{\{ 0\}}^{n} \times \mathcal{S}_{+}^{n}}},}

with c = vec (C) ∈ ℝn2 and x = vec (X) ∈ ℝn2. Here E ∈ ℝn × n2 is a matrix that extracts the n diagonal entries Xi i from its vectorized form x.
For the benchmark problems we randomly sample the data matrix C with entries Ci, j ∼ 𝒰 (−1,1) from a uniform distribution. Figure 6 shows the benchmark results for increasing matrix dimension n.

Figure 6: Solve time of benchmarked solvers for increasing problem size of nearest correlation matrix problems. The results for MOSEK are shown until they exceeded the time limit of 30 min.

Unsurprisingly, the first-order methods SCS and COSMO outperform the interior-point solver MOSEK for these large SDPs. Furthermore, for larger problems the solve times of COSMO and SCS scale in a similar way. COSMO seems to benefit from directly supporting the quadratic objective term in the problem while SCS has to transform it into an additional second-order-cone constraint. This increases the factorisation time and the projection time; see Table A.1.
7.4 Block-arrow sparse SDPs
To demonstrate the benefits of the chordal decomposition discussed in Section 4, we consider randomly generated SDPs of the form with a block-arrow aggregate sparsity pattern similar to test problems in [ZFP+19, ]. Figure 7 shows the sparsity pattern of the PSD constraint. The sparsity pattern is generated based on the following parameters: block size d, number of blocks Nb and width of the arrow head w. Note that the graph corresponding to the sparsity pattern is always chordal and that, for this sparsity pattern, clique merging yields no benefit.

Figure 7: Parameters of block-arrow sparsity pattern. The shaded area represents the non-zeros of the sparsity pattern.

In the following we study the effects of independently increasing the block size d and the number of blocks Nb. The parameters for the two test cases are:

Varying the number of blocks: Nb = 50, 60, …, 140, d = 10, w = 20, and m = 100.
Varying the block size: d = 10, 12, …, 28, Nb = 50, w = 10, and m = 100.

The solve times for all solvers are shown in Figure 8, Figure 9 and in Table A.1. The line COSMO(CD) corresponds to the solver with chordal decomposition enabled.

Figure 8: Solve time for increasing number of blocks Nb of block-arrow sparsity pattern.

Figure 9: Solve time for increasing block size d of block-arrow sparsity pattern.

The figures show that both COSMO with and without chordal decomposition solve this problem type consistently faster than MOSEK and SCS. The reason why COSMO performs better than the other first order solver SCS can be explained by the significantly lower number of iterations (Table A.1). Furthermore, one can see that in both cases the solver time for each solver rises when the number of blocks and the block sizes are increased. The increase is smaller for COSMO(CD) which is more affected by the number of iterations than the problem dimension.
7.5 Non-chordal problems with clique merging
To compare our proposed clique graph-based merge approach with the clique tree-based strategies of [NFF+03] and [], all three methods discussed in Section 5 were used to preprocess large sparse SDPs from SDPLib, a collection of SDP benchmark problems []. This problem set contains maximum cut problems, SDP relaxations of quadratic programs and Lovász theta problems. Moreover, we consider a set of test SDPs generated from (non-chordal) sparsity patterns of matrices from the SuiteSparse Matrix Collections []. The sparsity patterns for these problems are shown in Figure 10.

Figure 10: Aggregate sparsity pattern of non-chordal SDPs created from matrices of the SuiteSparse Matrix Collection. The patterns are labeled with their ID number.

Both problem sets were used in the past to benchmark structured SDPs [ZFP+19, ]. This section discusses how the different decompositions affect the per-iteration computation times of the solver. In a second step we compare the solver time of COSMO with our clique graph merging strategy to those of MOSEK and SCS.
For the strategy described in [NFF+03] we used the SparseCoLO package to decompose the problem. The parent-child method discussed in [] and the clique graph based method described in Section 5.2 are available as options in COSMO. We further investigate the effect of using different edge weighting functions. The major operation affecting the per-iteration time is the projection step. This step involves an eigenvalue decomposition of the matrices corresponding to the cliques. Since the eigenvalue decomposition of a symmetric matrix of dimension N has a complexity of 𝒪 (N3), we define a nominal edge weighting function as in. However, the exact relationship will be different because the projection function involves copying of data and is affected by hardware properties such as cache size. We therefore also consider an empirically estimated edge weighting function. To determine the relationship between matrix size and projection time, the execution time of the relevant function inside COSMO was measured for different matrix sizes. We then approximated the relationship between projection time, tproj, and matrix size, N, as a polynomial:

where a, b were estimated using least squares (Figure 11). The estimated weighting function is then defined as

e (𝒞i,𝒞j) = tproj (|𝒞i|) + tproj (|𝒞j|) − tproj (|𝒞i∪𝒞j|).

Figure 11: Measured and estimated relationship between matrix size and execution time of the projection function in COSMO.

Six different cases were considered: no decomposition (NoDe), no clique merging (NoMer), decomposition using SparseCoLO (SpCo), parent-child merging (ParCh), and the clique graph-based method with nominal edge weighting (CG1) and estimated edge weighting (CG2). SparseCoLO was used with default parameters. All cases were run single-threaded. Since the per-iteration projection times for some problems lie in the millisecond range every problem was benchmarked ten times and the median values are reported. Table LABEL:tb:benchmark_results shows the solve time, the mean projection time, the number of iterations, the number of cliques after merging, and the maximum clique size of the sparsity pattern for each problem and strategy. The solve time includes the time spent on decomposition and clique merging. We do not report the total solver time when SparseCoLO was used for the decomposition because this has to be done in a separate preprocessing step in MATLAB which was orders of magnitude slower than the other methods.

parent-child merging; 5 clique graph with nominal edge weighting; 6 clique graph with estimated edge weighting;
Our clique graph-based methods lead to a reduction in overall solver time. The method with estimated edge weighting function CG2 achieves the lowest average projection times for the majority of problems. In four cases ParCh has a narrow advantage. The geometric mean of the ratios of projection time of CG2 compared to the best non-graph method is 0.701, with a minimum ratio of 0.407 for problem mcp500-2. There does not seem to be a clear pattern that relates the projection time to the number of cliques or the maximum clique size of the decomposition. This is expected as the optimal merging strategy depends on the properties of the initial decomposition such as the overlap between the cliques. The merging strategies ParCh, CG1 and CG2 generally result in similar maximum clique sizes compared to SparseCoLO, with CG1 being the most conservative in the number of merges.
Table LABEL:tb:sdplib_solver_comparison shows the benchmark results of COSMO with merging strategy CG2, MOSEK, and SCS. The decomposition helps COSMO to solve most problems faster than MOSEK and SCS. This is even more significant for the larger problems that were generated from the SuiteSparse Matrix Collection. The decomposition does not seem to provide a major benefit for the slightly denser problems mcp500-3 and mcp500-4. Furthermore, COSMO seems to converge slowly for qpG51 and thetaG51. Similar observations for mcp500-3, mcp500-4 and thetaG51 have been made by the authors in []. Finally, many of the larger problems were not solvable within the time limit or caused out-of-memory problems if no decomposition was used in MOSEK and SCS.

out of memory error;
This paper describes the first-order solver COSMO and the ADMM algorithm on which it is based. The solver combines direct support of quadratic objectives, infeasibility detection, custom constraints, chordal decomposition of PSD constraints and automatic clique merging. The performance of the solver is illustrated on a number of benchmark problems that challenge different aspects of modern solvers.
The implementation in the Julia language facilitates rapid development and testing of ideas and allows users to customize the solver for their applications. It further allows the abstraction of precision and array types which we are planning to use to allow COSMO to run on GPUs. Further performance gains are likely to be achieved by exploring acceleration methods to speed up convergence to higher accuracies and reduce the dependency on problem scaling.
