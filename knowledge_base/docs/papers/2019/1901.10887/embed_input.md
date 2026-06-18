<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

COSMO: A Conic Operator Splitting Method for Convex Conic Problems

Topics include Conic optimization, Operator splitting, Convex optimization, Semidefinite programming, Sparse linear algebra.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents COSMO, a first-order conic solver built around operator splitting, quasi-definite linear solves, cone projections, and chordal decomposition for large semidefinite structure. It matters as a practical convex optimization solver aimed at large sparse conic problems arising in areas such as robust control.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper describes the Conic Operator Splitting Method (COSMO) solver, an operator splitting algorithm for convex optimisation problems with quadratic objective function and conic constraints. At each step the algorithm alternates between solving a quasi-definite linear system with a constant coefficient matrix and a projection onto convex sets. The low per-iteration computational cost makes the method particularly efficient for large problems, e.g. semidefinite programs that arise in portfolio optimisation, graph theory, and robust control. Moreover, the solver uses chordal decomposition techniques and a new clique merging algorithm to effectively exploit sparsity in large, structured semidefinite programs. A number of benchmarks against other state-of-the-art solvers for a variety of problems show the effectiveness of our approach. Our Julia implementation is open-source, designed to be extended and customised by the user, and is integrated into the Julia optimisation ecosystem.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider convex optimisation problems in the form

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

where we assume that both the objective function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ and the inequality constraint functions $g_{i}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ are convex, and that the equality constraints ${h_{i}{(x)}}:={{a_{i}^{\top}x} - b_{i}}$ are affine. We will denote an optimal solution to this problem (if it exists) as $x^{\ast}$. Convex optimisation problems feature heavily in a wide range of research areas and industries, including problems in machine learning, finance \[BBD^+^17\], optimal control, and operations research. Concrete examples of problems fitting the general form include linear programming (LP), convex quadratic programming (QP), second-order cone programming (SOCP), and semidefinite programming (SDP) problems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Methods to solve each of these standard problem classes are well known and a number of open- and closed-source solvers are widely available. However, the trend for data and training sets of increasing size in decision making problems and machine learning poses a challenge for state-of-the-art software.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Algorithms for LPs were first used to solve military planning and allocation problems in the 1940s. In 1947 Danzig developed the simplex method that solves LPs by searching for the optimal solution along the vertices of the inequality polytope. Extensions to the method led to the general field of *active-set methods* that are able to solve both LPs and QPs, and which search for an optimal point by iteratively constructing a set of active constraints. Although often efficient in practice, a major theoretical drawback is that the worst-case complexity increases exponentially with the problem size.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The most common approach taken by modern convex solvers is the *interior-point method*, which stems from Karmarkar's original projective algorithm, and is able to solve both LPs and QPs in polynomial time. Interior point methods have since been extended to problems with positive semidefinite (PSD) constraints and. The primal-dual interior point methods apply variants of Newton's method to iteratively find a solution to a set of optimality KKT conditions. At each iteration the algorithm alternates between a Newton step that involves factoring a Jacobian matrix and a line search to determine the magnitude of the step to ensure a feasible iterate. Most notably, the Mehrotra predictor-corrector method forms the basis of several implementations because of its strong practical performance. However, interior-point methods typically do not scale well for very large problems since the Jacobian matrix has to be calculated and factored at each step.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Two main approaches to overcome this limitation are active research areas. Firstly, a renewed focus on first-order methods with computationally cheaper per-iteration-cost, and secondly the exploitation of sparsity in the problem data. First-order methods are known to handle larger problems well at the expense of reduced accuracy compared to interior-point methods. In the 1960s Everett proposed a dual decomposition method that allows one to decompose a separable objective function, making each iteration cheaper to compute. Augmented Lagrangian methods by Miele, Hestenes, and Powell are more robust and helped to remove the strict convexity conditions on problems, while losing the decomposition property. By splitting the objective function, the alternating direction method of multipliers (ADMM), first described, allowed the advantages of dual decomposition to be combined with the superior convergence and robustness of augmented Lagrangian methods. Subsequently, it was shown that ADMM can be analysed from the perspective of monotone operators and that it is a special case of Douglas-Rachford splitting as well as of the proximal point algorithm, which allowed further insight into the method.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

ADMM methods are simple to implement and computationally cheap, even for large problems. However, they tend to converge slowly to a high accuracy solution and the detection of infeasibility is more involved compared to interior-point methods. They are therefore most often used in applications where a modestly accurate solution is sufficient \[PB^+^14\]. Most of the early advances in first-order methods such as ADMM happened in the 1970s/80s long before the demand for large scale optimisation, which may explain why they stayed less well-known and have only recently resurfaced.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

A method of exploiting the sparsity pattern of PSD constraints in an interior-point algorithm was developed. This work showed that if the coefficient matrices of an SDP exhibit an aggregate sparsity pattern represented by a chordal graph, then both primal and dual problems can be decomposed into a problem with many smaller PSD constraints on the nonzero blocks of the original matrix variable. These blocks are associated with subsets, called *cliques*, of graph vertices. Moreover, it can be advantageous to merge some of these blocks, for example if they overlap significantly. The optimal way to merge the blocks, or equivalently the corresponding graph cliques, after the initial decomposition depends on the solver algorithm and is still an open question. Sparsity in SDPs has also been studied for problems with underlying graph structure, e.g. optimal power-flow problems and graph optimisation problems.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Outline", "weight": 1.0} -->

In Section 2 we define the general conic problem format, its dual problem, as well as optimality and infeasibility conditions. Section 3 describes the ADMM algorithm that is used by COSMO. Section 4 explains how to decompose SDPs in a preprocessing step provided the problem data has an aggregated sparsity pattern. In Section 5 we describe a new clique merging strategy and compare it to existing approaches. Implementation details and code related design choices are discussed in Section 6. Section 7 shows benchmark results of COSMO vs. other state-of-the art solvers on a number of test problems. Section 8 concludes the paper.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contributions", "weight": 1.0} -->

We implement a first-order method for large conic problems that is able to detect infeasibility without the need of a homogeneous self-dual embedding.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Contributions", "weight": 1.0} -->

COSMO directly supports quadratic objective functions, thus reducing overheads for applications with both quadratic objective function and PSD constraints. This also avoids a major disadvantage of conic solvers compared to native QP solvers, i.e no additional matrix factorisation for the conversion is needed and favourable sparsity in the objective can be maintained.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Contributions", "weight": 1.0} -->

Large structured positive semidefinite programs are analysed and, if possible, chordally decomposed. This typically allows one to solve very large sparse and structured problems orders of magnitudes faster than competing solvers. For complex sparsity patterns, further performance improvements are achieved by recombining some of the sub-blocks of the initial decomposition in an optimal way. For this purpose, we propose a new clique graph based merging strategy and compare it to existing heuristic approaches.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Contributions", "weight": 1.0} -->

The open-source solver is written in a modular way in the fast and flexible programming language Julia. The design allows users to extend the solver by specifying a specific linear system solver and by defining their own convex cones or custom projection methods.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Conic Problems", "weight": 1.0} -->

where $x \in {\mathbb{R}}^{n}$ is the primal *decision variable* and $s \in {\mathbb{R}}^{m}$ is the primal *slack variable*. The objective function is defined by positive semidefinite matrix $P \in {\mathbb{S}}_{+}^{n}$ and vector $q \in {\mathbb{R}}^{n}$. The constraints are defined by matrix $A \in {\mathbb{R}}^{m \times n}$, vector $b \in {\mathbb{R}}^{m}$ and a non-empty, closed, convex cone $\mathcal{K}$ which itself can be a Cartesian product of cones in the form

<!-- chunk {"id": "body-0018", "role": "body", "section": "Conic Problems", "weight": 1.0} -->

with cone dimensions ${\sum_{i = 1}^{N}m_{i}} = m$. Note that any LP, QP, SOCP, or SDP can be written in the form using an appropriate choice of cones, as well as problems involving the power or exponential cones and their duals.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Infeasibility certificates", "weight": 1.0} -->

Primal and dual infeasibility conditions were developed for ADMM. These conditions are directly applicable to problems of the form. To simplify the notation of the conditions, define the cone $\overline{\mathcal{K}} ≔ {{- \mathcal{K}} + {\{ b\}}}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Infeasibility certificates", "weight": 1.0} -->

The existence of some $y \in \mathcal{D}$ certifies that problem is primal infeasible, while the existence of some $x \in \mathcal{P}$ certifies dual infeasibility.

<!-- chunk {"id": "body-0021", "role": "body", "section": "ADMM Algorithm", "weight": 1.0} -->

We use the same splitting as in \[SBG^+^18\] to transform problem into standard ADMM format.

<!-- chunk {"id": "body-0022", "role": "body", "section": "ADMM Algorithm", "weight": 1.0} -->

where the indicator functions of the sets $\{{{(x,s)} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}}\mid{{{Ax} + s} = b}\}$ and $\mathcal{K}$ were used to move the constraints of into the objective function. The augmented Lagrangian of is given by

<!-- chunk {"id": "body-0023", "role": "body", "section": "ADMM Algorithm", "weight": 1.0} -->

where we relaxed the $z$-update and the dual variable update with relaxation parameter $\alpha \in {}$ according to. Notice from (11b) and (11d) that the dual variable corresponding to the constraint $x = \overset{\sim}{x}$ satisfies $\lambda^{k} = {0\text{~for all~}k}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Solution of the equality constrained QP", "weight": 1.0} -->

The solution of can be obtained by solving a single linear system.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Solution of the equality constrained QP", "weight": 1.0} -->

where the Lagrangian multiplier $\nu \in {\mathbb{R}}^{m}$ accounts for the equality-constraint ${{Ax} + s} = b$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Solution of the equality constrained QP", "weight": 1.0} -->

Note that the introduction of the dummy variable $\overset{\sim}{x}$ led to the term $\sigmaI$ in the upper-left corner of the coefficient matrix. Consequently, the coefficient matrix in is always quasi-definite, i.e. it always has a positive definite upper-left block and a negative definite lower-right block, and is therefore full rank even when $P = 0$ or $A$ is rank deficient. Following the left hand side of always has a well-defined $LDL^{\top}$ factorization with a diagonal $D$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Projection step", "weight": 1.0} -->

As shown in \[PB^+^14\] the minimization problem in (11c) can be interpreted as the $\rho$-weighted proximal operator of the indicator function $I_{\mathcal{K}}$. It is therefore equivalent to the Euclidean projection $\Pi_{\mathcal{K}}$ onto the cone $\mathcal{K}$, i.e.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Projection step", "weight": 1.0} -->

If $\mathcal{K}$ is a Cartesian product of cones as in this projection is equivalent to the projection of the relevant components of the argument of $\Pi_{\mathcal{K}}{( \cdot )}$ onto each cone $\mathcal{K}_{i}$. A problem with $N$ SDP constraints therefore requires $N$ projections, but, since each of these operates on an independent segment of the input vector, they can be performed in parallel.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Algorithm steps", "weight": 1.0} -->

The calculations performed at each iteration are summarized in Algorithm 1.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Algorithm steps", "weight": 1.0} -->

Observe that the coefficient matrix of the linear system in is constant, so that one can precompute and cache the $LDL^{\top}$ factorization and efficiently evaluate line 2 with changing right hand sides. A refactorisation is only necessary if the step size parameters $\rho$ and $\sigma$ are updated.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Algorithm steps", "weight": 1.0} -->

Lines 3, 4, and 6 are computationally inexpensive since they involve only vector addition and scalar-vector multiplication. The projection in line 5 is crucial to the performance of the algorithm depending on the particular cones employed in the model: projections onto the zero-cone or the nonnegative orthant are inexpensive, while a projection onto the positive-semidefinite cone of dimension $N$ involves an eigenvalue decomposition. Since direct methods for eigen-decompositions have a complexity of approximately $\mathcal{O}{(N^{3})}$, this turns line 5 into the most computationally expensive operation of the algorithm for large SDPs, and improving the efficiency of this step will be the objective of much of Sections 4 and 5.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Algorithm convergence", "weight": 1.0} -->

For feasible problems, Algorithm 1 produces a sequence of iterates $(x^{k},s^{k},y^{k})$ that converges to a limit satisfying the optimality conditions in as $k\rightarrow\infty$. The authors in \[SBG^+^18\] show convergence of Algorithm 1 by applying the Douglas-Rachford splitting to a problem reformulation.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Algorithm convergence", "weight": 1.0} -->

In the Douglas-Rachford formulation, lines 5 and 6 become projections onto $\mathcal{K}$ and $\mathcal{K}^{\circ}$ respectively, so that the conic constraints in (6c) always hold. Furthermore, convergence of the residual iterates in (6a)--(6b) can be concluded from the convergence of the splitting variables

<!-- chunk {"id": "body-0034", "role": "body", "section": "Algorithm convergence", "weight": 1.0} -->

which generally holds for Douglas-Rachford splitting.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Algorithm convergence", "weight": 1.0} -->

For infeasible problems, showed that Algorithm 1 leads to convergence of the successive differences between iterates

<!-- chunk {"id": "body-0036", "role": "body", "section": "Algorithm convergence", "weight": 1.0} -->

For primal infeasible problems ${\deltay} = {\lim_{k\rightarrow\infty}{\deltay^{k}}}$ will satisfy condition, whereas for dual infeasible problems ${\deltax} = {\lim_{k\rightarrow\infty}{\deltax^{k}}}$ is a certificate of.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Scaling the problem data", "weight": 1.0} -->

The rate of convergence of ADMM and other first-order methods depends in practice on the scaling of the problem data; see. Particularly for badly conditioned problems, this suggests a preprocessing step where the problem data is scaled in order to improve convergence. For certain problem classes an optimal scaling has been found, see. However, the computation of the optimal scaling is often more complicated than solving the original problem. Consequently, most algorithms rely on heuristic methods such as matrix equilibration.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Scaling the problem data", "weight": 1.0} -->

We scale the equality constraints by diagonal positive definite matrices $D$ and $U$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Scaling the problem data", "weight": 1.0} -->

One heuristic strategy that has been shown to work well in practice is to choose the scaling matrices $D$ and $U$ to equilibrate, i.e. reduce the condition number of, the problem data. The Ruiz equilibration technique described iteratively scales the rows and columns of a matrix to have an infinity-norm of $1$ and converges linearly. We apply the modified Ruiz algorithm shown in Algorithm 2 to reduce the condition number of the symmetric matrix $R$

<!-- chunk {"id": "body-0040", "role": "body", "section": "Scaling the problem data", "weight": 1.0} -->

which represents the problem data.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Scaling the problem data", "weight": 1.0} -->

6 $c_{i}\leftarrow\left. \parallel R_{c,i}\parallel \right._{\infty}^{- \frac{1}{2}}$;
Algorithm 2 Modified Ruiz equilibration

<!-- chunk {"id": "body-0042", "role": "body", "section": "Scaling the problem data", "weight": 1.0} -->

Since $R$ is symmetric it suffices to consider the columns $R_{c,i}$ of $R$. At each iteration the scaling routine calculates the norm of each column. For the columns with norms higher than the tolerance $\tau$ scaling vector $c$ is updated with the inverse square root of the norm^11^1For the presented results a value of $\tau = 10^{- 6}$ was chosen.. If the norm is below the tolerance, the corresponding column will be scaled by 1.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Scaling the problem data", "weight": 1.0} -->

Since the matrix $U$ scales the (possibly composite) cone constraint, the scaling must ensure that if $s \in \mathcal{K}$ then ${U^{- 1}s} \in \mathcal{K}$. Let $\mathcal{K}$ be a Cartesian product of $N$ cones as in and partition $U$ into blocks

<!-- chunk {"id": "body-0044", "role": "body", "section": "Scaling the problem data", "weight": 1.0} -->

with block $U_{i} \in {\mathbb{R}}^{m_{i} \times m_{i}}$ which scales the constraint corresponding to $\mathcal{K}_{i}$. For each cone $\mathcal{K}_{i} \in {\mathbb{R}}^{m_{i}}$ that requires a scalar or symmetric scaling, e.g. a second-order cone or positive semidefinite cone, the corresponding block $U_{i}$ is replaced with

<!-- chunk {"id": "body-0045", "role": "body", "section": "Scaling the problem data", "weight": 1.0} -->

where the mean value of the diagonal entries of the original block in $U$, $u_{i} = {{\text{tr}{(U_{i})}}/m_{i}}$, was chosen as a heuristic scaling factor.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Termination criteria", "weight": 1.0} -->

The termination criteria discussed in this section are based on the unscaled problem data and iterates. Thus, before checking for termination the solver first reverses the scaling according to equations --.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Termination criteria", "weight": 1.0} -->

According to Section 3.3 of \[BPC^+^11\] a valid termination criterion is that the size of the norms of the residual iterates in are small.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Termination criteria", "weight": 1.0} -->

where $\epsilon_{abs}$ and $\epsilon_{rel}$ are user defined tolerances.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Termination criteria", "weight": 1.0} -->

Following, the algorithm determines if the one-step differences $\deltax^{k}$ and $\deltay^{k}$ of the primal and dual variable fulfil the normalized infeasibility conditions -- up to certain tolerances $\epsilon_{\text{p,inf}}$ and $\epsilon_{d,\inf}$. The solver returns a primal infeasibility certificate if

<!-- chunk {"id": "body-0050", "role": "body", "section": "Termination criteria", "weight": 1.0} -->

holds and a dual infeasibility certificate if

<!-- chunk {"id": "body-0051", "role": "body", "section": "Chordal Decomposition", "weight": 1.0} -->

As noted in Section 3.3, for large SDPs the eigen-decomposition in the projection step is the principal performance bottleneck for the algorithm. However, since large-scale SDPs often exhibit a certain structure or sparsity pattern, a sensible strategy is to exploit any such structure to alleviate this bottleneck. If the aggregated sparsity pattern is *chordal*, Agler's and Grone's theorems can be used to decompose a large PSD constraint into a collection of smaller PSD constraints and additional coupling constraints. The projection step applied to the set of smaller PSD constraints is usually significantly faster than when applied to the original constraint. Since the projections are independent of each other, further performance improvement can be achieved by carrying them out in parallel. Our approach is to apply chordal decomposition to a standard form SDP in the form to produce a decomposed problem, and then transform the resulting decomposed problem back to a problem in the form but with more variables and a collection of smaller PSD cone constraints. This process allows us to apply chordal decomposition as a preprocessing step before the problem is handed to the solver.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Chordal Decomposition", "weight": 1.0} -->

As discussed in Section 4.2, a chordal sparsity pattern can be imposed on any PSD constraint.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Graph preliminaries", "weight": 1.0} -->

In the following we define graph-related concepts that are useful to describe the sparsity structure of a problem. A good overview of this topic is given in the survey paper \[VA^+^15\]. Consider the *undirected graph* $G{(V,E)}$ with vertex set $V = {\{ 1,\ldots,n\}}$ and edge set $E \subseteq {V \times V}$. If all vertices are pairwise adjacent, i.e. $E = \left\{ {\{ v,u\}}\mid{{{v,u} \in V},{v \neq u}} \right\}$, the graph is called *complete*. We follow the convention of \[VA^+^15\] by defining a *clique* as a subset of vertices $\mathcal{C} \subseteq V$ that induces a *maximal* complete subgraph of $G$. The number of vertices in a *clique* is given by the cardinality $|\mathcal{C}|$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Graph preliminaries", "weight": 1.0} -->

A *cycle* is a path of edges (i.e. a sequence of distinct edges) joining a sequence of vertices in which only the first and last vertices are repeated.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Graph preliminaries", "weight": 1.0} -->

The following decomposition theory relies on a subset of graphs that exhibit the important property of *chordality*. A graph $G$ is *chordal* (or *triangulated*) if every cycle of length greater than three has a *chord*, which is an edge between nonconsecutive vertices of the cycle. A non-chordal graph can always be made chordal by adding extra edges.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Graph preliminaries", "weight": 1.0} -->

An undirected graph with $n$ vertices can be used to represent the sparsity pattern of a symmetric matrix $S \in {\mathbb{S}}^{n}$. Every nonzero entry $S_{ij} \neq 0$ in the lower triangular part of the matrix introduces an edge ${(i,j)} \in E$. An example of a sparsity pattern and the associated graph is shown in Figure 1(a--b).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Graph preliminaries", "weight": 1.0} -->

Given the definition in and a matrix $S \in {{\mathbb{S}}^{n}(E,0)}$, note that the diagonal entries $S_{ii}$ and the off-diagonal entries $S_{ij}$ with ${(i,j)} \in E$ may be zero or nonzero. Moreover, we define the cone of positive semidefinite completable matrices as

<!-- chunk {"id": "body-0058", "role": "body", "section": "Graph preliminaries", "weight": 1.0} -->

For a matrix $Y \in {{\mathbb{S}}_{+}^{n}{(E,?)}}$ we can find a positive semidefinite completion by choosing appropriate values for all entries ${(i,j)} \notin E$. An algorithm to find this completion is described in \[VA^+^15\]. An important structure that conveys a lot of information about the nonzero blocks of a matrix, or equivalently the cliques of a chordal graph, is the *clique tree* (or *junction tree*). For a chordal graph $G$ let $\mathcal{B} = {\{\mathcal{C}_{1},\ldots,\mathcal{C}_{p}\}}$ be the set of cliques.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Agler's and Grone's theorems", "weight": 1.0} -->

with variable $X$ and coefficient matrices ${A_{k},C} \in {\mathbb{S}}^{n}$. The corresponding dual problem is

<!-- chunk {"id": "body-0060", "role": "body", "section": "Agler's and Grone's theorems", "weight": 1.0} -->

with dual variable $y \in {\mathbb{R}}^{m}$ and slack variable $S$. Let us assume that the problem matrices in and each have their own sparsity pattern

<!-- chunk {"id": "body-0061", "role": "body", "section": "Agler's and Grone's theorems", "weight": 1.0} -->

The *aggregate sparsity* of the problem is given by the graph $G{(V,E)}$ with edge set

<!-- chunk {"id": "body-0062", "role": "body", "section": "Agler's and Grone's theorems", "weight": 1.0} -->

In general $G{(V,E)}$ will not be chordal, but a *chordal extension* can be found by adding edges to the graph. We denote the extended graph as $G{(V,\overline{E})}$, where $E \subseteq \overline{E}$. Finding the minimum number of additional edges required to make the graph chordal is an NP-complete problem. Consider a $0$--$1$ matrix $M$ with edge set $E$. A commonly used heuristic method to compute the chordal extension is to perform a symbolic Cholesky factorisation of $M$, with the edge set of the Cholesky factor then providing the chordal extension $\overline{E}$. To simplify the notation in the remainder of the article, we henceforward assume that $E$ represents a chordal graph or has been appropriately extended.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Agler's and Grone's theorems", "weight": 1.0} -->

where $\mathcal{C}_{\ell}{(i)}$ is the $i$th vertex of $\mathcal{C}_{\ell}$. We can express the constraints in in terms of multiple smaller coupled constraints using Grone's and Agler's theorems.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Returning a decomposed problem into standard SDP form", "weight": 1.0} -->

After the decomposition results of Section 4.2 have been applied, the SDP problem has to be transformed back into standard form. For the undecomposed problem, this is achieved by first relabeling $y$ as $x$. We then choose $P = 0_{n \times n}$, $q = {- b}$, define $A = {\lbrack{{svec}{(A_{1})}},\ldots,{{svec}{(A_{m})}}\rbrack}$, $b = {{svec}{(C)}}$ and $s = {{svec}{(S)}}$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Returning a decomposed problem into standard SDP form", "weight": 1.0} -->

To transform the decomposed dual problem, we will make use of the fact that the decision variable $S \in {\mathbb{S}}^{n}$ and all the submatrices $S_{\ell}$ are symmetric and consider instead $s_{\ell} = {{svec}{(S_{\ell})}}$. The main challenge is to keep track of the overlapping entries in the individual blocks and ensure they sum to the original entry in $S$. Different possible transformations achieving this are described.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Returning a decomposed problem into standard SDP form", "weight": 1.0} -->

All the necessary information about the overlapping entries is stored in the clique tree $\mathcal{T}{(\mathcal{B},\mathcal{E})}$ that represents the sparsity pattern of $S$. We assume that the clique tree is post-ordered with cliques $\mathcal{C}_{1},\ldots,\mathcal{C}_{p}$. Define a vector to represent slack variables for overlapping entries $\theta ≔ {\lbrack\theta_{1},\ldots,\theta_{n_{o}}\rbrack}^{\top}$, where $n_{o} ≔ {\sum_{\ell = 1}^{p}\frac{\left| \eta_{\ell} \right|{({\left| \eta_{\ell} \right| + 1})}}{2}}$ is the total number of overlapping entries in the upper triangle of the sparsity pattern.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Returning a decomposed problem into standard SDP form", "weight": 1.0} -->

The $s$ vector of the decomposed problem is created by stacking the vectorized subblocks $s_{\ell}$ according to the postordering of the clique tree. Define $\omega{(i,j,\ell)}$ as the index of $s$ corresponding to the $(i,j)$th element of block $S_{\ell}$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Returning a decomposed problem into standard SDP form", "weight": 1.0} -->

The matrices ${\overset{\sim}{A}}_{k}^{\ell}$ and ${\overset{\sim}{B}}^{\ell}$ take on the values of $A_{k}$ and $B$ in the locations corresponding to the elements in the submatrix $S_{\ell}$. If a matrix entry of clique $\mathcal{C}_{l}$ in $A_{k,{ij}}^{\ell}$ and $B_{ij}^{\ell}$ is overlapped by an entry of the parent clique, i.e. both $(i,j)$ are included in ${sep}{(\mathcal{C}_{l})}$, it is set to zero. Each column of the linking matrix $L \in {\mathbb{R}}^{m_{d} \times n_{o}}$ links one overlapping entry in the clique tree.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Returning a decomposed problem into standard SDP form", "weight": 1.0} -->

Then $L$ is constructed column-by-column, each representing one overlapping entry. The column vector $l_{c}$ is equal to $1$ in the row $r$ corresponding to the ${(i,j)}_{\ell}$-th entry of $S_{\ell}$ and $- 1$ in the row corresponding to the same entry of the parent block $S_{k}$, where $\mathcal{C}_{\ell} = {{ch}{(\mathcal{C}_{k})}}$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Returning a decomposed problem into standard SDP form", "weight": 1.0} -->

Notice how the overlap variables drop out if the original matrix $S$ is reassembled according to Theorem 2. ‣ 4.2 Agler’s and Grone’s theorems ‣ 4 Chordal Decomposition ‣ COSMO: A conic operator splitting method for convex conic problems") by adding the entries of each subblock.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Clique Merging", "weight": 1.0} -->

Given an initial decomposition with (chordally completed) edge set $E$ and a set of cliques $\{\mathcal{C}_{1},\ldots,\mathcal{C}_{p}\}$, we are free to re-merge any number of cliques back into larger blocks. This is equivalent to treating *structural* zeros in the problem as *numerical* zeros, leading to additional edges in the graph.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Clique Merging", "weight": 1.0} -->

We replace two positive semidefinite matrix constraints of dimensions $\left| \mathcal{C}_{i} \right|$ and $\left| \mathcal{C}_{j} \right|$ with one constraint on a larger clique with dimension $\left| {\mathcal{C}_{i} \cup \mathcal{C}_{j}} \right|$, where the increase in dimension depends on the size of the overlap.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Clique Merging", "weight": 1.0} -->

We remove consistency constraints for the overlapping entries between $\mathcal{C}_{i}$ and $\mathcal{C}_{j}$, thus reducing the size of the linear system of equality constraints.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Clique Merging", "weight": 1.0} -->

When merging cliques these two factors have to be balanced, and the optimal merging strategy depends on the particular SDP solution algorithm employed. In \[NFF^+^03\] and a clique tree is used to search for favourable merge candidates; We will refer to their two approaches as SparseCoLO and the *parent-child* strategy, respectively, in the following sections. We will then propose a new merging method in Section 5.2 whose performance is superior to both methods when used in ADMM. Given a merging strategy, Algorithm 3 describes how to merge a set of cliques within the set $\mathcal{B}$ and update the edge set $\mathcal{E}$ accordingly.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Clique Merging", "weight": 1.0} -->

Input: A set of cliques ℬ with edge set ℰ, a subset of cliques ℬm = {𝒞m, 1, 𝒞m, 2, …, 𝒞m, r} ⊆ ℬ to be merged. Output: A reduced set of cliques $\hat{\mathcal{B}}$ with edge set $\hat{\mathcal{E}}$ and the merged clique 𝒞m.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Existing clique tree-based strategies", "weight": 1.0} -->

with heuristic parameters $t_{fill}$ and $t_{size}$. These conditions keep the amount of extra fill-in and the supernode cardinalities below the specified thresholds. The SparseCoLO strategy described in \[NFF^+^03\] and considers parent-child as well as sibling relationships. Given a parameter $\sigma > 0$, two cliques $\mathcal{C}_{i},\mathcal{C}_{j}$ are merged if the following merge criterion holds

<!-- chunk {"id": "body-0077", "role": "body", "section": "Existing clique tree-based strategies", "weight": 1.0} -->

We note that the open-source implementation of the SparseCoLO algorithm described in \[NFF^+^03\] follows the algorithm outlined here, but also employs a few additional heuristics.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Existing clique tree-based strategies", "weight": 1.0} -->

An advantage of these two approaches is that the clique tree can be computed easily and the conditions are inexpensive to evaluate. However, a disadvantage is that choosing parameters that work well on a variety of problems and solver algorithms is difficult. Secondly, clique trees are not unique and in some cases it is beneficial to merge cliques that are not directly related on the particular clique tree that was computed.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Existing clique tree-based strategies", "weight": 1.0} -->

and some additional vertices $\{ 1,2,{m_{a} + 1}\}$. The graph is connected as shown in Figure 2(a), where the complete subgraphs are represented as nodes $V_{a},V_{b},V_{c}$. A corresponding clique tree is shown in Figure 2(b).

<!-- chunk {"id": "body-0080", "role": "body", "section": "Existing clique tree-based strategies", "weight": 1.0} -->

By choosing the cardinality $\left| V_{c} \right|$, the overlap between cliques $\mathcal{C}_{1} = {{\{ 1,2\}} \cup V_{c}}$ and $\mathcal{C}_{3} = {{\{{m_{a} + 1}\}} \cup V_{c}}$ can be made arbitrarily large while $\left| V_{a} \right|$, $\left| V_{b} \right|$ can be chosen so that any other merge is disadvantageous. However, neither the parent-child strategy nor SparseCoLO would consider merging $\mathcal{C}_{1}$ and $\mathcal{C}_{3}$ since they are in a "nephew-uncle" relationship. In fact for the particular sparsity graph in Figure 2(a) eight different clique trees can be computed.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Existing clique tree-based strategies", "weight": 1.0} -->

Only in half of them do the cliques $\mathcal{C}_{1}$ and $\mathcal{C}_{3}$ appear in a parent-child relationship. Therefore, a merge strategy that only considers parent-child relationships would miss this favorable merge in half the cases.

<!-- chunk {"id": "body-0082", "role": "body", "section": "A new clique graph-based strategy", "weight": 1.0} -->

To overcome the limitations of existing strategies we propose a merging strategy based on the *reduced clique graph* $\mathcal{G}{(\mathcal{B},\xi)}$, which is defined as the union of all possible clique trees of $G$; see for a detailed discussion. The set of vertices of this graph is given by the maximal cliques of the sparsity pattern. We then create the edge set $\xi$ by introducing edges between pairs of cliques $(\mathcal{C}_{i},\mathcal{C}_{j})$ if they form a separating pair $\mathcal{P}_{ij}$. We remark that $\xi$ is a subset of the edges present in the *clique intersection graph* which is obtained by introducing edges for every two cliques that intersect. However, the reduced clique graph has the property that it remains a valid reduced clique graph of the altered sparsity pattern after performing a permissible merge between two cliques. This is not always the case for the clique intersection graph.

<!-- chunk {"id": "body-0083", "role": "body", "section": "A new clique graph-based strategy", "weight": 1.0} -->

For convenience, we will refer to the reduced clique graph simply as the clique graph in the following sections.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Open-Source Implementation", "weight": 1.0} -->

We have implemented our algorithm in the Conic Operator Splitting Method (COSMO), an open-source package written in Julia. Julia allows the solver to be written in a flexible, modular and extensible way, while still maintaining the benefits of a fast compiled language. The source code and documentation are available at

<!-- chunk {"id": "body-0085", "role": "body", "section": "Open-Source Implementation", "weight": 1.0} -->

COSMO offers the user two interfaces to describe the constraints of the optimisation problem: a direct interface, and an interface to the modelling languages JuMP and Convex.jl \[UMZ^+^14\]. These interfaces connect the solver to the Julia optimisation ecosystem which provide flexible problem description and automatic problem reformulation.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Open-Source Implementation", "weight": 1.0} -->

As shown in Algorithm 1 the two main steps of the algorithm are solving a linear system and projecting onto a Cartesian product of cones. The implementation of these two parts allows customisation by the user. For the solution of the linear system in the user can either use the QDLDL \[SBG^+^18\] solver provided with COSMO, the standard sparse solver from SuiteSparse \[D^+^15\], or choose one of the provided interfaces to direct and indirect solvers, e.g. Pardiso \[SGK^+^10, KAA^+^15\], conjugate gradient, minimal residual method, or link their own implementation.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Open-Source Implementation", "weight": 1.0} -->

The second important part of the algorithm is the projection step onto a Cartesian product of convex sets. By default COSMO supports the zero cone, the nonnegative orthant, the hyperbox, the second-order cone, the PSD cone, the exponential cone and its dual, and the power cone and its dual. Our Julia implementation also allows the user to define their own convex cones^22^2To allow infeasibility detection the user has to either define a convex cone, a convex compact set or a composition of the two. and custom projection functions.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Open-Source Implementation", "weight": 1.0} -->

a projection function that projects an input vector onto the cone

<!-- chunk {"id": "body-0089", "role": "body", "section": "Open-Source Implementation", "weight": 1.0} -->

a function that determines if a vector is inside the dual cone $\mathcal{K}_{c}^{\ast}$

<!-- chunk {"id": "body-0090", "role": "body", "section": "Open-Source Implementation", "weight": 1.0} -->

a function that determines if a vector is inside the recession cone of $- \mathcal{K}_{c}$

<!-- chunk {"id": "body-0091", "role": "body", "section": "Open-Source Implementation", "weight": 1.0} -->

The latter two functions are required for our solver to implement checks for infeasibility as described in Sections 2.1 and 3.4. An example that shows the advantages of defining a custom cone is provided in Section 7.2.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Open-Source Implementation", "weight": 1.0} -->

The authors used COSMO's algorithm with a specialized implementation of the projection function for positive semidefinite constraints. The projection method used approximate matrix eigendecompositions to significantly reduce the projection time, while maintaining all the features of COSMO such as scaling, infeasibility detection and interfaces to linear system solvers. It was demonstrated that this can provide a significant, up to 20x, reduction in solve time.\

<!-- chunk {"id": "body-0093", "role": "body", "section": "Open-Source Implementation", "weight": 1.0} -->

Given a problem with multiple constraints, the projection step can be carried out in parallel. This is particularly advantageous when used in combination with chordal decomposition, which typically yields a large number of smaller PSD constraints. For the eigendecomposition involved in the projection step of a PSD constraint, the LAPACK \[ABB^+^99\] function sveyr is used, which can also utilise multiple threads. Consequently, this leads to two-level parallelism in the computation, i.e on the higher level the projection functions are carried out in parallel and each projection function independently calls sveyr. Determining the optimal allocation of the CPU cores to each of these tasks depends on the number of PSD constraints and their dimensions and is a difficult problem. For the problem sets considered in section 7 we achieved the best performance by running sveyr single-threaded and using all physical CPUs to carry out the projection functions in parallel.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Open-Source Implementation", "weight": 1.0} -->

Moreover, Julia's type abstraction features are used to enable the solver to solve problems of arbitrary floating-point precision. This allows for example to reduce the memory usage of the solver for very large problems by switching to 32-bit single-precision floating-point format.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

This section presents benchmark results of COSMO against the interior-point solver MOSEK v$9.0$ and the accelerated first-order ADMM solver SCS v$2.1.1$. When applied to a quadratic program, COSMO's main algorithm becomes very similar to the first-order QP solver OSQP. To test the performance penalty of using a pure Julia implementation against a similar C implementation we also compare our solver against OSQP v$0.6.0$ on QP problems.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

We selected a number of problem sets to test different aspects of COSMO. The advantage of supporting a quadratic cost function in a conic solver is shown by solving QPs from the Maros and Mészáros QP repository in Section 7.1 and SDPs with quadratic objectives in the form of nearest correlation matrix problems in Section 7.3.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

To highlight the advantages of implementing custom constraints, we consider a problem set with doubly-stochastic matrices in Section 7.2. We then show how chordal decomposition can speed up the solver for SDPs that exhibit a block-arrow sparsity pattern in Section 7.4.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

The performance of chordal decomposition is further explored in Section 7.5 by solving large structured problems from the SDPLib benchmark set as well as some non-chordal SDPs generated with sparsity patterns from the SuiteSparse Matrix Collections. Using the same problems we additionally evaluate the performance of different clique merging strategies.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

All the experiments were carried out on a computing node of the University of Oxford ARC-HTC cluster with 16 logical Intel Xeon E5-2560 cores and $64\ {GB}$ of DDR3 RAM. All the problems were run using Julia v$1.3$ and the problems were passed to the solvers via MathOptInterface.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

where $A_{a}$, $b_{a}$ and $y_{a}$ correspond to the rows of $A$, $b$ and $y$ that represent active constraints. This is to ensure meaningful values even if the problem contains inactive constraints with very large, or possibly infinite, values $b_{i}$. The maximum of the three errors for each problem and solver is reported in the results below.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

We configured COSMO, MOSEK, SCS and OSQP to achieve an accuracy of $\epsilon = {10^{- 3}}$. We set the maximum allowable solve time for the Maros and Mészáros problems to $5\ \min$ and to $30\ \min$ for the other problem sets. All other solver parameters were set to the solvers' standard configurations. COSMO uses a Julia implementation of the QDLDL solver to factor the quasi-definite linear system. Similarly, we configured SCS to use a direct solver for the linear system.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

The Maros and Mészáros test problem set is a repository of challenging convex QP problems that is widely used to compare the performance of QP solvers. For comparison metrics we compute the failure rate, the number of fastest solve time and the normalized shifted geometric mean for each solver. The shifted geometric mean is more robust against large outliers (compared to the arithmetic mean) and against small outliers (compared to the geometric mean) and is commonly used in optimisation benchmarks; see \[SBG^+^18, Mit\].

<!-- chunk {"id": "body-0103", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

with total solver time $t_{p,s}$ of solver $s$ and problem $p$, shifting factor $sh$ and size of the problem set $n$. In the reported results a shifting factor of ${sh} = 10$ was chosen and the maximum allowable time $t_{p,s} = {300\ s}$ was used if solver $s$ failed on problem $p$. Lastly, we normalize the shifted geometric mean for solver $s$ by dividing by the geometric mean of the fastest solver. The failure rate $f_{r,s}$ is given by the number of unsolved problems compared to the total number of problems in the problem set. As unsolved problems we count instances where the algorithm does not converge within the allowable time or fails during the setup or solve phase. Table 7.1 shows the normalized shifted geometric mean and the failure rate for each solver. Additionally, the number of cases where solver $s$ was the fastest solver is shown.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

OSQP shows the best performance in terms of lowest failure rates, number of fastest solves and in the shifted geometric mean of solve times. COSMO follows very closely. The shifted geometric mean of MOSEK seems to suffer from a higher failure rate compared to OSQP/COSMO, and SCS fails on a large number of problems. The higher failure rate could be due to the necessary transformation into a second-order-cone problem.
For this problem set of QPs COSMO’s algorithm reduces, with some minor differences, to the algorithm of OSQP. Consequently, this benchmark is useful to evaluate the performance penalty that COSMO pays due to its implementation in the higher-order language Julia. The results in Table 7.1 show that the performance difference is very small. This can also be seen by looking at the solve times of each solver for increasing problem dimension, as shown in Figure 4.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

COSMO and OSQP have very similar solve times, aside from very small problems that are solved in under 1×10−5 s to 1×10−4 s. This difference is primarily due to overheads incurred from features in our Julia implementation that support more than one constraint type during problem setup. The marginally better resulting performance of OSQP for the smallest problems in the test set is the reason that OSQP is the faster solver in a larger number of cases in Table 7.1. 7.2 Custom convex cones
In many cases writing a custom solver algorithm for a particular problem can be faster than using available solver packages if a particular aspect of the problem structure can be exploited to speed up parts of the computations. As mentioned earlier, COSMO supports user customisation by allowing the definition of new convex cones. This is useful if constraints of the problem can be expressed using this new convex cone and a fast projection method onto the cone exists. A fast specialized projection method in an ADMM framework has for example been used by the authors to solve the error-correcting code decoding problem.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

To demonstrate the advantage of custom convex cones, consider the problem of finding the doubly stochastic matrix that is nearest, in the Frobenius norm, to a given symmetric matrix C ∈ 𝕊n. Doubly stochastic matrices are used for instance in spectral clustering and matrix balancing [RHD+14]. A specialized algorithm for this problem type has been recently discussed by the authors. Doubly stochastic matrices have the property that all rows and columns each sum to one and all entries are nonnegative.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

with symmetric real matrix C ∈ 𝕊n and decision variable X ∈ ℝn × n.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

with x = vec (X) and c = vec (C) However, the problem can be written in a more compact form by using a custom projection function to project the matrix iterate onto the affine set of matrices 𝒞∑, whose rows and columns each sum to one.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

where A is assumed to have full rank. In the case of 𝒞a = 𝒞∑ we can exploit the fact that the inverse of A A⊤ can be efficiently computed. The projection can be carried out as described in Algorithm 5; see Appendix B.1 for a derivation.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

Notice that Algorithm 5 can be implemented efficiently without ever assembling and storing A and 11⊤.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

The sparsity pattern of the new constraint matrix A only consists of two diagonals and the number of non-zeros reduces from 3 n2 to 2 n2. We expect this to reduce the initial factorisation time of the linear system in as well as the forward- and back-substitution steps.
Figure 5 shows the total solve time of all the solvers for problem with randomly generated dense matrix C with Ci j ∼ 𝒰 and increasing matrix dimension. Additionally, we show the solve time for COSMO in the problem form and with a specialized custom set and projection function as.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

It is not surprising that COSMO and OSQP scale in the same way for this problem type. MOSEK is slightly slower for smaller problem dimension and overtakes COSMO/OSQP for problems of dimensions n ≥ 500. This might be due to fact that MOSEK uses a faster multi-threaded linear system solver while OSQP/COSMO rely on the single-threaded solver QDLDL. The longer solve time of SCS is due to slow convergence of the algorithm for this problem type. Furthermore, when the problem is solved with a custom convex set as in COSMO(CS) is able to outperform all other solvers. Table LABEL:tb:doubly_stochastic shows the total solve time and the factorisation time of the two versions of COSMO for small, medium and large problems. As predicted the lower solve time can be mainly attributed to the faster factorisation time.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

solving with a custom convex set 𝒞∑ and projection function

<!-- chunk {"id": "body-0114", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

7.3 Nearest correlation matrix
Consider the problem of projecting a matrix C onto the set of correlation matrices, i.e. real symmetric positive semidefinite matrices with diagonal elements equal to 1. This problem is for example relevant in portfolio optimisation. The correlation matrix of a stock portfolio might lose its positive semidefiniteness due to noise and rounding errors of previous data manipulations. Consequently, it is of interest to find the nearest correlation matrix X to a given data matrix C ∈ ℝn × n.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

with c = vec (C) ∈ ℝn2 and x = vec (X) ∈ ℝn2. Here E ∈ ℝn × n2 is a matrix that extracts the n diagonal entries Xi i from its vectorized form x.
For the benchmark problems we randomly sample the data matrix C with entries Ci, j ∼ 𝒰 (−1,1) from a uniform distribution. Figure 6 shows the benchmark results for increasing matrix dimension n.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

Unsurprisingly, the first-order methods SCS and COSMO outperform the interior-point solver MOSEK for these large SDPs. Furthermore, for larger problems the solve times of COSMO and SCS scale in a similar way. COSMO seems to benefit from directly supporting the quadratic objective term in the problem while SCS has to transform it into an additional second-order-cone constraint. This increases the factorisation time and the projection time; see Table A.1.
7.4 Block-arrow sparse SDPs
To demonstrate the benefits of the chordal decomposition discussed in Section 4, we consider randomly generated SDPs of the form with a block-arrow aggregate sparsity pattern similar to test problems in [ZFP+19, ]. Figure 7 shows the sparsity pattern of the PSD constraint. The sparsity pattern is generated based on the following parameters: block size d, number of blocks Nb and width of the arrow head w. Note that the graph corresponding to the sparsity pattern is always chordal and that, for this sparsity pattern, clique merging yields no benefit.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

In the following we study the effects of independently increasing the block size d and the number of blocks Nb.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

The solve times for all solvers are shown in Figure 8, Figure 9 and in Table A.1. The line COSMO(CD) corresponds to the solver with chordal decomposition enabled.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

The figures show that both COSMO with and without chordal decomposition solve this problem type consistently faster than MOSEK and SCS. The reason why COSMO performs better than the other first order solver SCS can be explained by the significantly lower number of iterations (Table A.1). Furthermore, one can see that in both cases the solver time for each solver rises when the number of blocks and the block sizes are increased. The increase is smaller for COSMO(CD) which is more affected by the number of iterations than the problem dimension. 7.5 Non-chordal problems with clique merging
To compare our proposed clique graph-based merge approach with the clique tree-based strategies of [NFF+03] and, all three methods discussed in Section 5 were used to preprocess large sparse SDPs from SDPLib, a collection of SDP benchmark problems. This problem set contains maximum cut problems, SDP relaxations of quadratic programs and Lovász theta problems. Moreover, we consider a set of test SDPs generated from (non-chordal) sparsity patterns of matrices from the SuiteSparse Matrix Collections.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

The sparsity patterns for these problems are shown in Figure 10.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

Both problem sets were used in the past to benchmark structured SDPs [ZFP+19, ]. This section discusses how the different decompositions affect the per-iteration computation times of the solver. In a second step we compare the solver time of COSMO with our clique graph merging strategy to those of MOSEK and SCS. For the strategy described in [NFF+03] we used the SparseCoLO package to decompose the problem. The parent-child method discussed and the clique graph based method described in Section 5.2 are available as options in COSMO. We further investigate the effect of using different edge weighting functions. The major operation affecting the per-iteration time is the projection step. This step involves an eigenvalue decomposition of the matrices corresponding to the cliques. Since the eigenvalue decomposition of a symmetric matrix of dimension N has a complexity of 𝒪 (N3), we define a nominal edge weighting function as. However, the exact relationship will be different because the projection function involves copying of data and is affected by hardware properties such as cache size. We therefore also consider an empirically estimated edge weighting function.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

To determine the relationship between matrix size and projection time, the execution time of the relevant function inside COSMO was measured for different matrix sizes.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

where a, b were estimated using least squares (Figure 11). The estimated weighting function is then defined as

<!-- chunk {"id": "body-0124", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

Six different cases were considered: no decomposition (NoDe), no clique merging (NoMer), decomposition using SparseCoLO (SpCo), parent-child merging (ParCh), and the clique graph-based method with nominal edge weighting (CG1) and estimated edge weighting (CG2). SparseCoLO was used with default parameters. All cases were run single-threaded. Since the per-iteration projection times for some problems lie in the millisecond range every problem was benchmarked ten times and the median values are reported. Table LABEL:tb:benchmark_results shows the solve time, the mean projection time, the number of iterations, the number of cliques after merging, and the maximum clique size of the sparsity pattern for each problem and strategy. The solve time includes the time spent on decomposition and clique merging. We do not report the total solver time when SparseCoLO was used for the decomposition because this has to be done in a separate preprocessing step in MATLAB which was orders of magnitude slower than the other methods.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

parent-child merging; 5 clique graph with nominal edge weighting; 6 clique graph with estimated edge weighting;
Our clique graph-based methods lead to a reduction in overall solver time. The method with estimated edge weighting function CG2 achieves the lowest average projection times for the majority of problems. In four cases ParCh has a narrow advantage. The geometric mean of the ratios of projection time of CG2 compared to the best non-graph method is 0.701, with a minimum ratio of 0.407 for problem mcp500-2. There does not seem to be a clear pattern that relates the projection time to the number of cliques or the maximum clique size of the decomposition. This is expected as the optimal merging strategy depends on the properties of the initial decomposition such as the overlap between the cliques. The merging strategies ParCh, CG1 and CG2 generally result in similar maximum clique sizes compared to SparseCoLO, with CG1 being the most conservative in the number of merges. Table LABEL:tb:sdplib_solver_comparison shows the benchmark results of COSMO with merging strategy CG2, MOSEK, and SCS.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

The decomposition helps COSMO to solve most problems faster than MOSEK and SCS. This is even more significant for the larger problems that were generated from the SuiteSparse Matrix Collection. The decomposition does not seem to provide a major benefit for the slightly denser problems mcp500-3 and mcp500-4. Furthermore, COSMO seems to converge slowly for qpG51 and thetaG51. Similar observations for mcp500-3, mcp500-4 and thetaG51 have been made by the authors. Finally, many of the larger problems were not solvable within the time limit or caused out-of-memory problems if no decomposition was used in MOSEK and SCS.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Maros and Mészáros QP test set", "weight": 1.0} -->

out of memory error;
This paper describes the first-order solver COSMO and the ADMM algorithm on which it is based. The solver combines direct support of quadratic objectives, infeasibility detection, custom constraints, chordal decomposition of PSD constraints and automatic clique merging. The performance of the solver is illustrated on a number of benchmark problems that challenge different aspects of modern solvers.
The implementation in the Julia language facilitates rapid development and testing of ideas and allows users to customize the solver for their applications. It further allows the abstraction of precision and array types which we are planning to use to allow COSMO to run on GPUs. Further performance gains are likely to be achieved by exploring acceleration methods to speed up convergence to higher accuracies and reduce the dependency on problem scaling.
