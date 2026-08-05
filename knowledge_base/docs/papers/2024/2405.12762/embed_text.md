<!-- arxiv-full-text:v1 {"arxiv_id": "2405.12762", "source": "arxiv-html"} -->

## Introduction

We consider throughout the following convex conic optimization problem: with decision variables $x \in {\mathbb{R}}^{n}$ and $s \in {\mathbb{R}}^{m}$, and problem data $A \in {\mathbb{R}}^{m \times n}$, $b \in {\mathbb{R}}^{m}$, $q \in {\mathbb{R}}^{n}$ and $P \in {\mathbb{R}}^{n \times n}$. We assume that $P$ is symmetric and positive semidefinite (possibly zero) and that the set $\mathcal{K}$ is a closed and convex cone. We will denote the optimal value of this problem as $p^{\ast}$ and an optimizer (when it exists) as $(x^{\ast},s^{\ast})$.

It can be shown that the problem dual to $\mathcal{P}$ is where $\mathcal{K}^{\ast}$ is the dual cone of $\mathcal{K}$. We will denote its optimal value as $d^{\ast}$ and an optimizer (when it exists) as $(x^{\ast},z^{\ast})$. We will assume throughout that strong duality holds between $\mathcal{P}$ and $\mathcal{D}$, i.e. that $p^{\ast} = d^{\ast}$.

The problem $\mathcal{P}$ is very general and can model most convex optimization problems of practical interest. Such problems appear in a huge range of applications including constrained optimal control \[Borrelli:MPCbook\] and moving horizon estimation \[Allan2019:MHE\], limit analysis of engineering structures \[Martin:LowerSOCP, Martin:UpperSOCP\] and fluid flows \[Goulart:FluidSOS\], image processing \[Combettes:ImageRecovery\], support vector machines \[Cortes:SVM:1995\], lasso problems \[Tibshirani:1996, Candes:2008\], circuit design \[Boyd:GeoProg\], portfolio optimization \[cornuejols2006, JOFI:JOFI1525\], and many others. The numerical solution of convex problems in the form $\mathcal{P}$ also underpins many nonconvex optimization methods, including those based on sequential quadratic programming \[, Ch. 18\]\[boggs:tolle:SQP:1995\] and branch-and-bound methods within mixed-integer methods \[Bertsimas:IntegerOpt, BandB:Survey\].

### Solution methods

Considerable research effort has focused on the development of solution techniques for $\mathcal{P}$ over many decades. If the cone $\mathcal{K}$ is the positive orthant, then $\mathcal{P}$ represents a linear program (LP) if $P = 0$ or a quadratic program (QP) otherwise. This case in particular has a long history, dating to the landmark work of Kantorovich \[Kantorovich:1939\] and Koopmans \[Koopmans:1942, Koopmans:1949\] in the LP case, and Frank and Wolfe in the QP case \[Frank:1956\]. Of particular significance was the development of numerical solution methods for such problems, and in particular *simplex* or active-set methods for the solution of LP \[Dantzig:1963\] and QP \[Wolfe:1959\] instances. Active set methods still form the basis of many modern LP and QP solvers, including commercial solvers such as Gurobi \[gurobi\] and open-source solvers such as qpOASES \[qpOASES\] and HiGHS \[HiGHS\].

However, since active set methods are based on the iterative updating of a basis of active constraints and rely heavily on the polyhedral structure of systems of linear equalities and inequalities, they do not generalize well to the case of non-polyhedral constraints. Recent advances for more general *conic programs*, i.e. optimization problems where the set $\mathcal{K}$ is a more general convex cone, have therefore focussed instead on either operator splitting methods such as the alternating direction method of multipliers (ADMM) \[boyd2011distributed\] or on interior-point methods. ADMM methods in particular are attractive in cases where only moderate accuracy is required, since ADMM is known to be prone to poor 'tail convergence' at high precision \[He:Yuan:2012\]. Nevertheless, ADMM based methods are widely used in practice for both their scalability and simplicity of implementation and form the basis of several open-source solvers for $\mathcal{P}$, including the open source solvers OSQP \[OSQP\], SCS \[SCS\] and COSMO \[COSMO\].

### Primal-dual interior-point methods

In this work we focus instead on primal-dual interior-point methods \[nemirovski:todd:2008\], since such methods are known to perform better than operator splitting methods at high precision and, unlike active set methods, can support general conic constraints. A significant milestone in the development of solution algorithms for $\mathcal{P}$ was Karmarkar's method \[Karmarkar:1984\], which provided the first practically useful polynomial-time solution method for linear programs, followed by the path following method of Renegar \[Renegar:1988\].

An advantage of interior-point methods is that they can be extended to the case of general conic constraints $\mathcal{K}$ in $\mathcal{P}$. Of particular importance in the development of efficient conic interior-point solvers was the development of solvers based on cones and associated barrier functions that have the *self-scaling* property \[, \]. The family of self-scaled cones include those that are generally considered the most important constraint types in practice, i.e. the nonnegative orthant, second-order cone and positive semidefinite (PSD) cone. Conic problems defined over self-scaled cones can be solved efficiently using primal-dual interior-point methods based on the *Nesterov-Todd (NT) scaling* strategy \[, \].

Nonsymmetric cones that do *not* have the self-scaling property have been the subject of increasing recent interest for interior-point methods \[, \]. The exponential cone and the power cone are the two most studied and are supported in commercial solvers such as Mosek. In certain cases it is also attractive to formulate problems in terms of more exotic nonsymmetric cones that can be solved more efficiently by exploiting their special structure \[, Hypatia, DDS\]. Since the NT scaling method does not apply to nonsymmetric cones, alternative strategies have been proposed based on either primal or dual iterates \[ Hypatia\] or both primal and dual iterates together \[, DDS\].

Alongside these developments, a further innovation was the development of the *homogeneous self-dual embedding* (HSDE). This method embeds a conic program with linear objectives into a slightly larger feasibility problem, which is *always* feasible regardless of the feasibility of the original problem. Once a feasible point is found, it can be used to construct either an optimizer for the original problem or a primal or dual certificate of infeasibility. The HSDE is at the heart of many modern interior-point solvers including CVXOPT \[cvxopt\], ECOS \[ecos\], SCS \[SCS\] and MOSEK \[MOSEK\]. A downside of this approach is that it does not naturally support problems with quadratic objectives, since the standard embedding method applied to such cases does not produce a self-dual problem.

### Monotone complementarity problems (MCPs)

Extensions of the HSDE method were quickly developed for the linear complementary problem (LCP), and later for the more general monotone complementary problem (MCP) \[Andersen1999\] with linear constraints. The homogeneous embedding for MCPs was also extended to problems defined over more general symmetric cone constraints \[, -a\].

The practical performance of the homogeneous embedding in the case of convex quadratically constrained quadratic programming (QCQP) problems was investigated. More recently, \[ODonoghue2021\] proposed a maximal monotone operator specialized for the LCP based on the monotone operator in \[Andersen1999\] to produce a first-order solver for problems with convex quadratic objectives and general conic constraints.

## Algorithmic approach

In this paper we adopt the approach of \[, ODonoghue2021\] by specializing the homogeneous embedding method of \[Andersen1999\] to convex problems with quadratic objectives. We will use this embedding as the basis for a general purpose primal-dual interior-point solver that handles both symmetric and nonsymmetric cone constraints.

The standard Karush-Kuhn-Tucker (KKT) conditions for problem $\mathcal{P}$ are | | $(s,z)$ | ${\in {\mathcal{K} \times \mathcal{K}^{\ast}}}.$ | | | We define the duality gap $\gamma$ as where the final equality follows from substitution in the KKT conditions. The duality gap $\gamma$ is nonnegative for any feasible point since $(s,z)$ are constrained to the dual pair of cones $(\mathcal{K},\mathcal{K}^{\ast})$, and is zero at an optimal point $(x^{\ast},s^{\ast},z^{\ast})$ when strong duality holds.

Taking problems $\mathcal{P}$ and $\mathcal{D}$ together with an objective minimizing the duality gap, we can rewrite our problem in the form This problem is of course infeasible whenever either $\mathcal{P}$ or $\mathcal{D}$ is infeasible or the pair is not strongly dual.

If we define nonnegative scalars $(\tau,\kappa)$ and apply a change of variables $x\rightarrow{x/\tau}$, $z\rightarrow{z/\tau}$ and $s\rightarrow{s/\tau}$, then we can rewrite the feasibility problem as The problem $\mathcal{H}$ is equivalent to the widely-used homogeneous self-dual embedding (HSDE) \[Nesterov1999\] in the special case $P = 0$. The most common approach to solving $\mathcal{P}$ is therefore to eliminate the quadratic term in the objective function, replacing it with an epigraphical upper bound and an additional second-order cone constraint in the objective \[Lobo:1998\]. This amounts to rewriting $\mathcal{P}$ as which is a conic optimization problem with a purely linear cost and an additional second-order cone constraint.

If we instead keep the quadratic term in the objective then $\mathcal{H}$ remains homogeneous but is no longer self-dual, in addition to featuring the seemingly awkward $\frac{1}{\tau}x^{\top}Px$ term in the first equality. Our approach will nevertheless amount to a direct solution of $\mathcal{H}$ using a primal-dual type interior-point method, and we will show that significant performance improvements are possible with this approach in many cases relative to standard HSDE-based interior-point methods.

### Existence of solutions and infeasibility detection

Before proceeding to the details of our algorithm, we address briefly the existence and interpretation of solutions to $\mathcal{H}$. As in the case of the HSDE, an advantage of our reformulation is that solutions will produce either a solution to the original problem $\mathcal{P}$ or $\mathcal{D}$, or (asymptotically) a certificate of either primal or dual infeasibility. We first define the following sets of infeasibility certificates for $\mathcal{P}$ and $\mathcal{D}$: The problem $\mathcal{P}$ is infeasible if and only if there exists some $\overline{x} \in {\mathbb{D}}$, while the problem $\mathcal{D}$ is infeasible if and only if there exists some $\overline{z} \in {\mathbb{P}}$. Similar conditions have appeared in \[COSMO, Banjac2019, ODonoghue2021\] in the context of conic optimization with quadratic objectives.

Solving the problem $\mathcal{H}$ amounts to finding a root of the nonlinear system of equations subject to the conic constraint These conditions are identical to those in \[ODonoghue2021, (4.1)\], where they were developed in terms of specialization of the homogeneous embedding of monotone complementary problems developed in \[Andersen1999\] to an LCP.

We can define a more compact notation $v:={(x,z,s,\tau,\kappa)}$ for convenience, so that $\mathcal{H}$ is equivalent to As in \[Andersen1999\], we say that the problem $\mathcal{H}$ (equivalently) is *asymptotically feasible* if there exists a bounded sequence ${\{ v^{k}\}} \subset \mathcal{C}$, ${k = {1,2,\ldots}},$ such that and call any limit point $\hat{v}:={(\hat{x},\hat{z},\hat{s},\hat{\tau},\hat{\kappa})}$ of such a sequence an *asymptotically feasible point*. We will call any such point with ${{{\hat{s}}^{\top}\hat{z}} + {\hat{\tau}\hat{\kappa}}} = 0$ an *(asymptotically) complementary* or optimal solution.

We can now develop some basic results about solutions to the problem $\mathcal{H}$ in the spirit of \[Andersen1999, Thm. 1\]:

### Lemma 2.1

The problem $\mathcal{H}$ is (asymptotically) feasible and every (asymptotically) feasible point is (asymptotically) complementary.

### Proof

We can construct an asymptotically feasible sequence by defining $x^{k} = {{(\frac{1}{2})}^{k}\mathbf{1}\frac{1}{\sqrt{n}}}$, $s^{k} = {{(\frac{1}{2})}^{k}e_{\mathcal{K}}}$, $z^{k} = {{(\frac{1}{2})}^{k}e_{\mathcal{K}^{\ast}}}$, $\tau^{k} = {(\frac{1}{2})}^{k}$ and $\kappa^{k} = {(\frac{1}{2})}^{k}$, where $(e_{\mathcal{K}},e_{\mathcal{K}^{\ast}})$ is any vector pair in $\mathcal{K} \times \mathcal{K}^{\ast}$. It is then straightforward to show that ${G{(v^{k})}}\rightarrow 0$, noting in particular that the sequence where $\overline{\sigma}{(P)}$ is the maximum singular value of $P$, and is lower bounded by zero since $P$ is positive semidefinite. To show the second part, observe that for any $v \in \mathcal{C}$, so ${{{(s^{k})}^{T}{(z^{k})}} + {\tau^{k}\kappa^{k}}}\rightarrow 0$ since ${G{(v^{k})}}\rightarrow 0$ and all sequences are bounded. ∎

### Lemma 2.2

Suppose that $v^{\ast}:={(x^{\ast},z^{\ast},s^{\ast},\tau^{\ast},\kappa^{\ast})}$ is an asymptotically complementary solution to $\mathcal{H}$. Then: If $\tau^{\ast} > 0$ then $({x^{\ast}/\tau^{\ast}},{s^{\ast}/\tau^{\ast}})$ is an optimal solution to $\mathcal{P}$ and $({x^{\ast}/\tau^{\ast}},{z^{\ast}/\tau^{\ast}})$ is an optimal solution to $\mathcal{D}$.

If $\kappa^{\ast} > 0$ then at least one of the following holds: $\mathcal{P}$ is infeasible and $z^{\ast} \in {\mathbb{D}}$. $\mathcal{D}$ is infeasible and $x^{\ast} \in {\mathbb{P}}$.

### Proof

For (i), note that $\kappa^{\ast}\rightarrow 0$ since the solution is assumed asymptotically complementary. Then any point satisfying ${G{(v^{\ast})}} = 0$ also satisfies the KKT conditions following rescaling of $(x^{\ast},s^{\ast},z^{\ast})$ by $\tau^{\ast}$.

For (ii), suppose that ${{{\{ v^{k}\}} \in \mathcal{C}},{k = {1,2,\ldots}}},$ is any bounded sequence with limit $v^{\ast}$. Since $\tau^{k}\rightarrow 0$ by assumption, it follows that ${{(x^{k})}^{\top}Px^{k}}\rightarrow 0$ since $\frac{1}{\tau^{k}}x^{k}Px^{k}$ must remain bounded. Hence ${Px^{\ast}} = 0$ since $P$ is assumed positive semidefinite, and both ${{Ax^{\ast}} - s^{\ast}} = 0$ and ${A^{\top}z^{\ast}} = 0$. Since ${\{ s^{k},z^{k}\}} \in {\mathcal{K} \times \mathcal{K}^{\ast}}$ by assumption and both cones are closed, $z^{\ast} \in \mathcal{K}^{\ast}$ and ${Ax^{\ast}} \in \mathcal{K}$. Since ${{q^{\top}x^{\ast}} + {b^{\top}z^{\ast}}} = {- \kappa^{\ast}}$ with $\kappa^{\ast} > 0$, then at least one of the inner product terms must be negative. Consequently, if ${q^{\top}x^{\ast}} < 0$ then $x^{\ast} \in {\mathbb{P}}$ and $\mathcal{D}$ is infeasible, and if ${b^{\top}z^{\ast}} < 0$ then $z^{\ast} \in {\mathbb{D}}$ and $\mathcal{P}$ is infeasible. ∎

### Supported constraint types and barrier functions

Our interior-point method supports a variety of cones of both symmetric (i.e. self dual) and nonsymmetric type, and we allow the cone $\mathcal{K}$ in problem $\mathcal{P}$ to be any arbitrary composition of the basic cone types we describe in this section. For the symmetric case, we support the following cones: The *nonnegative cone* ${\mathbb{R}}_{+}^{n}:=\left\{ {x \in {\mathbb{R}}^{n}} \middle| {x \geq 0} \right\}$.

The *second order cone* $\mathcal{Q}_{n}:=\left\{ {{(u,v)} \in {{\mathbb{R}} \times {\mathbb{R}}^{n - 1}}} \middle| {{\| v\|}_{2} \leq u} \right\}$.

The *positive semidefinite cone* $\mathcal{S}_{n}:=\left\{ {x \in {\mathbb{R}}^{{n{({n + 1})}}/2}} \middle| {{\text{mat}{(x)}} \succeq 0} \right\}$.

Our implementation for $\mathcal{S}_{n}$ uses the standard scaled and vectorized 'triangular' format. Given some symmetric matrix $M \in {\mathbb{R}}^{n \times n}$, we define an operator ${svec}{( \cdot )}$ that extracts the upper triangular part and scales off-diagonal terms by $\sqrt{2}$, i.e.

The inverse operation ${mat}{( \cdot )}$ then restores the original matrix, i.e. $M = {{mat}{({{svec}{(M)}})}}$. This scaling is necessary to preserve inner products, i.e. $\operatorname{tr}{(L^{\top}M)} = {svec}{(L)}^{\top}{svec}{(M)}$ for matrices of compatible dimension.

We also support two nonsymmetric cones, both defined as subsets of ${\mathbb{R}}^{3}$: The *exponential cone* $\mathcal{K}_{\text{exp}}:=\left\{ {{(s_{1},s_{2},s_{3})} \in {\mathbb{R}}^{3}} \middle| {{{s_{2} \cdot e^{s_{1}/s_{2}}} \leq s_{3}},{s_{2} > 0}} \right\}$.

The *power cone* $\mathcal{K}_{\text{pow}}:=\left\{ {{(s_{1},s_{2},s_{3})} \in {\mathbb{R}}^{3}} \middle| {{{s_{1}^{\alpha}s_{2}^{1 - \alpha}} \geq {|s_{3}|}},{{s_{1} \geq 0},{s_{2} \geq 0}}} \right\}$.

For these two nonsymmetric cones the corresponding dual cones are Finally, we support the zero cone $\mathcal{Z}_{n}:={\{ 0\}}^{n}$ to enable modelling of problems with equality constraints.

### Barrier functions

For each nonzero cone we define a strictly convex *barrier function* $f:{\mathcal{K}\rightarrow{\mathbb{R}}}$ and its associated *conjugate barrier* $f^{\ast}:{\mathcal{K}^{\ast}\rightarrow{\mathbb{R}}}$. In particular, we use barrier functions that meet the following definition:

### Definition 2.3 (\[Nesterov1994, \])

A function $f:{\mathcal{K}\rightarrow{\mathbb{R}}}$ is called a *logarithmically homogeneous self-concordant barrier* with degree $\nu \geq 1$ ($\nu$--LHSCB) for the cone $\mathcal{K}$ if it satisfies the following properties: The conjugate function $f^{\ast}:{\mathcal{K}^{\ast}\rightarrow{\mathbb{R}}}$ is defined as The function $f^{\ast}$ is also $\nu$--LHSCB for $\mathcal{K}^{\ast}$ if $f$ is. The primal gradient $\nabla f$ satisfies In cases where the conjugate barrier function is known only through the definition (i.e. rather than being representable in closed-form), we can compute its gradient as the solution to The relations -- then collectively ensure that

### The central path

We assume that $f:{\mathcal{K}\rightarrow{\mathbb{R}}}$ is a $\nu$--LHSCB function on $\mathcal{K}$ with conjugate barrier $f^{\ast}$ for some $\nu \geq 1$. Given any initial $v^{0} \in \mathcal{C}$, we define the *central path* $v^{\ast}{(\mu)}$ as the unique solution to where $\mathbf{e}$ is the standard idempotent for $\mathcal{K}$. The core of our interior-point algorithm amounts to a Newton-like method for computing a solution to the system of equations. We describe the calculation of step directions for this method in §3. Before doing so, we address solver initialization, termination and preprocessing steps in the remainder of this section.

### Solver initialization

Before solving we perform an equilibration step on all matrix-valued data using the Ruiz equilibration technique described in \[Ruiz:2001\]. We refer the reader to \[COSMO, §3.5\] and \[OSQP, §5.1\] for implementation details.

We have several strategies for choosing an initial iterate in the interior of our problem's conic constraints while being sufficiently near to the central path.

### Symmetric cones

In the symmetric case, i.e. when $\mathcal{K}$ is self-dual, our method follows the approach of \[cvxopt\] for initialization and we distinguish between the cases $P = 0$ and $P \neq 0$. Although the zero cone is not itself symmetric, we treat problems where $\mathcal{K}$ is a composition of symmetric and zero cones as symmetric for the purposes of initialization.

If $P \neq 0$, we first solve the linear system which is the solution to the problem where $\alpha_{p} = {\inf\left. \{\alpha \middle| {{{- z} + {\alpha\mathbf{e}}} \in \mathcal{K}}\} \right.}$. We introduce a threshold $\epsilon > 0$ to ensure that $s^{0}$ is in the strict interior of the cone $\mathcal{K}$. Likewise, $z^{0}$ is set to where $\alpha_{d} = {\inf\left. \{\alpha \middle| {{z + {\alpha\mathbf{e}}} \in \mathcal{K}}\} \right.}$.

If $P = 0$, we instead solve the linear system in an effort to minimize the linear residuals. We set $x^{0} = x$ and where $\alpha_{p} = {\inf\left. \{\alpha \middle| {{{- s} + {\alpha\mathbf{e}}} \in \mathcal{K}}\} \right.}$. We then solve the system where $\alpha_{d} = {\inf\left. \{\alpha \middle| {{z + {\alpha\mathbf{e}}} \in \mathcal{K}}\} \right.}$. In either case, we set the scalars $(\tau^{0},\kappa^{0})$ to $1$.

### Nonsymmetric cones

When $\mathcal{K}$ contains any nonsymmetric cone, we instead apply a unit initialization strategy as in \[, \]. In this case, we initialize both primal and dual variables at a point on the central path satisfying $z = s = {- {{\nabla f^{\ast}}{(z)}}}$ (corresponding to $\mu^{0} = 1$). This is equivalent to solving the unconstrained optimization which is strictly convex and has a unique solution. It yields $s_{sym}^{0} = z_{sym}^{0} = \mathbf{e}$ for symmetric cones, | for exponential cones, and | for power cones of parameter $\alpha$.

### Chordal Decomposition

For semidefinite programs (SDPs) we follow the chordal-decomposition and clique merging strategy developed as part of the COSMO solver \[COSMO\]. We implement both a 'parent-child' merge strategy based on the clique-tree analysis method of \[Sun:2014\] and the clique-graph merge strategy described in \[COSMO, §5\]. We reformulate problems decomposed using either of these methods using the so-called 'compact' or 'range-space' conversion method described in \[Kim:2011, §5\].

When implementing the clique-graph based merge strategy, we use the same edge-weight metric as in \[COSMO\] to determine when candidate clique merges are accepted. Given a clique graph with $V$ vertices and two cliques $\mathcal{C}_{i}$ and $\mathcal{C}_{j}$, we define an edge weight function $e:{{2^{V} \times 2^{V}}\rightarrow{\mathbb{R}}}$ as and merge candidate cliques when this metric is positive. We note that this metric was used in the ADMM-based solver \[COSMO, §5\] because it relates directly to the computational complexity of projections onto the positive semidefinite cone. In our case the size of a Hessian block generated by a conic variable in $\mathcal{S}_{n}$ has dimension ${\mathbb{R}}^{{({{n{({n + 1})}}/2})} \times {({{n{({n + 1})}}/2})}}$, with the resulting KKT factorization time further complicated by the linking variables generated between overlapping cliques. We note therefore that it is likely that more efficient merge metrics are possible.

### Termination Criteria

All termination criteria are based on unscaled problem data and iterates, i.e. after the Ruiz scaling described in §2.4 has been reverted. For checks of primal and dual feasibility, we first define normalized variables ${\overline{x} = {x/\tau}},{{\overline{s} = {s/\tau}},{\overline{z} = {z/\tau}}}$ and then define primal and dual residuals as | | $r_{d}$ | $:={{P\overline{x}} + {A^{\top}\overline{z}} + q}$ | | | | and primal and dual objectives as | | | $g_{p}$ | $:={{\frac{1}{2}{\overline{x}}^{\top}P\overline{x}} + {q^{\top}x}}$ | | | | | $g_{d}$ | ${:={{- {\frac{1}{2}{\overline{x}}^{\top}P\overline{x}}} - {b^{\top}\overline{z}}}}.$ | | | We then declare convergence if each of the following three conditions holds: We specify a default value of $\epsilon_{f} = 10^{- 8}$ in our implementation, and a weaker threshold of $\epsilon = 10^{- 5}$ when testing for 'near optimality' in cases of early termination (e.g. lack of progress, timeout, iterations limit).

When testing for infeasibility certificates, we do *not* normalize iterates, but rather work directly with the unscaled variables since infeasibility corresponds to the case where $\tau\rightarrow 0$. We declare primal infeasibility if and dual infeasibility if We again set $\epsilon_{i,r} = \epsilon_{i,a} = 10^{- 8}$ as default values, and allow for weaker thresholds to declare 'near infeasibility' certificates in cases of early termination.

## Computing step directions

Our interior-point method computes Newton-like search directions using a linearization of given some right-hand side residual $d:={(d_{x},d_{z},d_{\tau},d_{s},d_{\kappa})}$. This produces a linear system in the form where $\xi:={x\tau^{- 1}}$ and $H \in {\mathbb{R}}^{m \times m}$ is a positive definite matrix that we will refer to as the *scaling matrix*. The choice of both the scaling matrix and the right-hand side terms $d$ in depend on the search direction, the symmetry or asymmetry of the cone $\mathcal{K}$ and the particular choice of scaling strategy. We defer more precise definitions of these terms to later in this section.

Our approach to solving follows that of \[cvxopt, ecos\], but differs in the fact that some blocks in the coefficient matrix of (22a) include an additional term when $P \neq 0$. We first eliminate the variables $({\Delta s},{\Delta\kappa})$ to obtain the reduced system To solve we solve a pair of linear systems with a common left-hand side and then recover $({\Delta\tau},{\Delta x},{\Delta z})$ using Finally, we recover $({\Delta s},{\Delta\kappa})$ from (23b). After obtaining the search direction $({\Delta s},{\Delta z},{\Delta\tau},{\Delta\kappa})$, we compute the maximal step size $\alpha$ ensuring that the new update resides in the interior of conic constraints. In cases where any part of $\mathcal{K}$ is nonsymmetric, we also choose $\alpha$ sufficiently small so that the updated values $({s + {\alpha\Delta s}},{z + {\alpha\Delta z}})$ remain within a neighborhood of the central path using the proximity metric described.

### Scaling matrices

The choice of scaling matrix $H$ in depends on the way in which we linearize the central path equations as defined in Section 2.3. For symmetric cones the most common choice is the NT scaling \[, \], which we also employ. For nonsymmetric cones, the central path is defined by the set of point satisfying (21b), and both symmetric scaling or the nonsymmetric scaling strategies have been implemented in state-of-the-art solvers. We set $H = 0$ for the zero cone.

### Symmetric cones

For symmetric cones we linearize the central path equation (21c). The NT scaling method exploits the self-scaled property of symmetric cone $\mathcal{K}$ to define, for ${(s,z)} \in \mathcal{K}$, a unique scaling point $w \in \mathcal{K}$ satisfying The matrix $H{(w)}$ can be factorized as ${H^{- 1}{(w)}} = {W^{\top}W}$, and we set $H = {H^{- 1}{(w)}}$. The factors $w,W$ are then computed following \[cvxopt\] except in the case of second-order cones, where we instead apply a modified version of the sparse factorization strategy of \[ecos\] for second-order cones of dimension greater than $4$.

### Nonsymmetric cones

In the nonsymmetric case the self-scaled property does not hold and the central path can't be formulated as in (21c) due to the lack of a Jordan algebra, so we instead linearize (21b). A general primal-dual scaling strategy suitable for nonsymmetric cones was consequently proposed, and used later, which relies on the satisfaction of two secant equations Suppose we define *shadow iterates* as A scaling matrix $H$ can then be obtained from the rank-4 Broyden-Fletcher-Goldfarb-Shanno (BFGS) update, which is commonly used in quasi-Newton methods, where ${Z:={\lbrack z,\overset{\sim}{z}\rbrack}},{{S:={\lbrack s,\overset{\sim}{s}\rbrack}},{{\overset{\sim}{z}:={- {{\nabla f}{(s)}}}},{\overset{\sim}{s}:={- {{\nabla f^{\ast}}{(z)}}}}}}$ and $H_{a} \succ 0$ is an approximation of the Hessian. In our implementation, we choose $H_{a} = {\mu{\nabla^{2}f^{\ast}}{(z)}}$ following and the calculation of $H_{BFGS}$ reduces to a rank-3 update, More details about the primal-dual scaling of nonsymmetric cones can be found.

### The affine and centering directions

At every interior-point iteration, our method requires us to solve the linear system for each of two different right-hand side terms $(d_{x},d_{z},d_{\tau},d_{s},d_{\kappa})$. This amounts to a single factorization of the condensed system followed by three linear solves, noting the common right-hand-side term $({- q},b)$ .

The first of these two choices produces the affine step direction, where we compute the search direction $({\Delta x},{\Delta s},{\Delta z},{\Delta\kappa},{\Delta\tau})$ to eliminate the linear residuals , i.e. by computing a pure Newton step direction for with $\mu = 0$. The second is called the combined step, which is the affine step plus a centering correction toward the central path. In practice, the estimated direction $({\Delta x},{\Delta s},{\Delta z},{\Delta\kappa},{\Delta\tau})$ from the affine step is used to determine the right-hand side $(d_{x},d_{z},d_{\tau},d_{s},d_{\kappa})$ for the combined step to compute a higher-order correction for acceleration. In the language of predictor-corrector algorithms, the affine step is the *predictor* while the centering step as the *corrector*.

Computation of a higher-order correction term $\eta$ is a heuristic technique that is known to accelerate the convergence of IPMs significantly. The choice of this term varies depending on the choice of the scaling matrix $H$ and whether a given cone constraint is symmetric. For our method $(d_{x},d_{z},d_{\tau},d_{s},d_{\kappa})$ is defined as in the affine step, and in the combined step. For symmetric cones we use the Mehrotra correction $\eta = {{({W^{- 1}\Delta s})} \circ {({W\Delta z})}}$ \[cvxopt\], while for nonsymmetric cones we compute $\eta$ using the 3rd-order correction method, i.e.

We choose ${\sigma = {({1 - \alpha_{\text{aff}}})}^{3}},$ where $\alpha_{\text{aff}}$ is the step size from the affine step.

### Linear solve method

Nearly all of the cost of computing step directions in §3 typically comes when solving the symmetric linear system. To solve this system we add a small regularization term $\epsilon_{s}$ and then compute a direct factorization This *static regularization* ensures that the matrix $K$ is quasidefinite \[Vanderbei1995\] even if $P$ is rank deficient, and consequently that the factor $D$ is diagonal with $D_{ii} \neq 0$ when computing the Cholesky-like factorization $LDL^{T}$ \[Gill1996\]. This approach also ensures that the sparsity pattern of the factor $L$ depends only on the problem's sparsity pattern, so the method is allocation-free after the first factorization. When computing the $LDL$ factorization we also employ a *dynamic regularization* strategy by bounding pivots away from zero by an amount $\epsilon_{d}$ to ensure that the factorization is numerically stable. We have extended the open-source package QDLDL, original developed for OSQP and based on \[Davis2005\], to support this regularization strategy.

The improved numerical efficiency of our scheme relative to the standard HSDE method can be seen by consideration of the linear system. If we had started instead from the epigraphical reformulation, then the coefficient matrix in would have been with $H_{\mathcal{K}}$ a scaling matrix appropriate for the additional second order cone constraint introduced. Direct factorization of can produce significantly more fill-in than for coefficient matrix, particular when the matrix factor $P^{\frac{1}{2}}$ already has substantial fill-.

## Implementation: the Clarabel solver

We have implemented our approach in the Clarabel solver, an open-source and liberally licensed software package with separate implementations in both the Rust \[rust\] and Julia \[julia\] programming languages. Both implementations, along with extensive documentation, are available under the Apache v2.0 license and are publicly available via our main project site at Our Rust implementation is intended for most academic and industrial end users. This implementation can also be accessed via other common languages through standard foreign function interfaces (FFIs) and wrappers, and we currently provide such wrappers for Python, C, C++ and R. We also provide interfaces in Python to the standard modelling package CVXPY \[diamond2016cvxpy, agrawal2018rewriting\]. Clarabel is installed as part of the standard CVXPY distribution \[cvxpy:web\] and is the default solver in CVXPY for linear and second-order cone programs as of version 1.5.

The Rust version of Clarabel provides its own internal implementation of most linear algebra functionality, including a standalone Rust reimplementation of the quasidefinite linear solver QDLDL with regularization features as described in §3.3. We use Rust interfaces to user-selectable BLAS \[blackford2002updated\] implementations (e.g. \[intel_mkl, openblas\]) for solving conic programs on the semidefinite cone. We also allow for the use of alternative direct linear solvers, and provide optional support for a 3rd-party multithreaded supernodal LDL factorization method implemented in native Rust as part of the faer-rs package \[faer\].

The Julia implementation is intended for use both as a standalone solver for users of the Julia language and as a prototyping platform for future algorithmic development. The Julia implementation relies heavily on native Julia functions for most linear algebra functionality, aside from a Julia implementation of QDLDL which we provide as a standalone package. In Julia, we also provide the option of using alternative linear solve methods including CHOLMOD \[cholmod\], Pardiso \[pardiso\] and the HSL \[ma57\] solver.

Both implementations provide the same functionality and support the same set of conic constraints. We also provide support for different floating point data types in both languages, e.g. for standard 32- or 64-bit single or double precision floating point types \[kahan1996ieee\] or for extended precision types such as the Julia BigFloat type. Our implementation is inspired by the modular design pattern of the interior-point solver OOQP \[ooqp\], in the sense that all internal data types are defined as abstract types that can be extended or customized by end users to specific problem classes to exploit domain-specific structure. In the Rust implementation this functionality relies heavily on Rust's trait-based type system and generics, while in Julia we instead rely on Julia's dynamic dispatch and "duck typing" \[ducktyping\].

For more detail we refer the reader to the documentation available on the Clarabel project website.

## Numerical Experiments

We have benchmarked our implementation of Clarabel against a variety of open-source and commercial solvers: the open-source interior-point solver ECOS \[ecos\], the open-source dual-simplex base solver HiGHS \[HiGHS\], and the commercial interior-point solvers Mosek \[MOSEK\] and Gurobi \[gurobi\]. All benchmarks are executed with all default settings for all solvers enabled, but with pre-solve disabled where applicable to ensure that the solvers are solving equivalent problems. We do not impose any iteration limits other than those specified within each solver's internal defaults. We set the maximum solve time to 300 seconds unless otherwise stated.

Our two implementations of Clarabel use our native implementations of the direct LDL linear solver QDLDL for all tests unless otherwise stated. The QDLDL solver is relatively unsophisticated relative to the multithreaded methods used in commercial solvers, but is lightweight, open-source and does not rely on any external libraries.

All experiments were carried out on the Oxford University Advanced Research Computing (ARC) Facility \[OxfordArc\]. For each test problem in our benchmarks results, solver were run single threaded on an Intel Xeon Platinum 8268 CPU @ 2.90 GHz with 64 GB RAM. All benchmarks tests are scripted in Julia and access solver interfaces via JuMP \[Lubin2023\]. We use Rust compiler version 1.72.0 and Julia version 1.9.2. The code for all numerical examples is publicly available \[ClarabelBenchmarks\].

For each set of benchmark problems in our results we exclude problems for which *none* of the benchmarked solvers produced a valid solution. We provide a summary of the results for all benchmarked solvers appropriate to each problem class in the form of shifted geometric means and performance profiles in the remainder of this section.

For all benchmark tests sets, we provide more detailed numerical results for our Rust and Julia implementations as well as the solvers Mosek and ECOS (where applicable) in Appendix A, including solve times and iteration counts. We include only this subset of solvers in our detailed reporting since all are interior-point based methods and therefore have iteration counts that are directly comparable.

### Shifted geometric means

We follow the standard benchmarking convention of using a normalized shifted geometric mean for comparison of solve time across different solvers \[hansbench\]. For a set of $N$ test problems, we define the shifted geometric mean solve time $g_{s}$ for solver $s$ as where $t_{p,s}$ is the time in seconds for solver $s$ to solve problem $p$, and $k = 1$ is the shift. The normalized shifted geometric mean is then defined as so that the solver with the lowest shifted geometric mean solve time has a normalized score of 1. For those problems for which a given solver fails, we assign a solve time $t_{p,s}$ equal to the maximum allowable solve time for the relevant benchmark.

### Performance profiles

We also provide performance profiles \[Dolan2002\] to compare both the relative and absolute performance of different solvers. For a set of $N$ test problems, we define the *relative performance ratio* for solver $s$ and problem $p$ as The performance profile for the solver $s$ is then a plot of the function $f_{s}^{r}:{{\mathbb{R}}_{+}\mapsto{\lbrack 0,1\rbrack}}$ defined as where $\mathcal{I}_{\leq \tau} = 1$ if $\tau \leq t_{p,s}$ and $\mathcal{I}_{\leq \tau} = 0$ otherwise. The relative performance profile therefore shows, at each level $\tau$, the fraction of problems solved by solver $s$ in time within a factor $\tau$ of the solve time of the best solver.

Since the relative performance profile for a given solver can change depending on the overall collection of solvers being benchmarked, we further compute an *absolute performance profile* by plotting a function $f_{s}^{a}:{{\mathbb{R}}_{+}\mapsto{\lbrack 0,1\rbrack}}$ as The absolute performance profile then shows, at each level $\tau$, the fraction of problems solved by solver $s$ within $\tau$ seconds and is independent of the other solvers benchmarked.

### Benchmark problems with quadratic objectives

In this section we present benchmark results for quadratic programming (QP) problems in the standard form $\mathcal{P}$ with the set $\mathcal{K}$ restricted to the composition of the zero cone (i.e. modelling linear equality constraints) and the nonnegative orthant. We consider example problems taken or generated from standard open-source problem collections and covering a wide range of problem dimensions.

### The Maros-Meszaros test set

We consider first the standard benchmark collection of 138 quadratic programs from the Maros-Meszaros test set \[maros1999\]. This collection of QPs includes a wide range of problem sizes and contains a number of difficult test cases due to numerical ill-conditioning, rank deficiency or poor scaling.

Results Results for this benchmark set are shown in Figure 1 for all solvers. Clarabel is the fastest overall solver on this benchmark set, with the Rust implementation marginally faster as expected. We observe that the seemingly large gap in the relative performance profile of our Rust and Julia implementations is almost entirely attributable to faster solve times among the smallest examples in this test set. All solvers fail on at least some subset of these benchmarks, with Gurobi the lowest failure rate at full accuracy, and Clarabel the lowest failure rate at reduced accuracy.

Of particular note in this benchmark set is the high failure rate of the ECOS and Mosek solvers, since both are interior-point methods broadly similar to Clarabel. In the case of ECOS these failures are partly attributable to the solvers' requirement to reformulate QP problems in the conic form, since ECOS does not support quadratic objectives natively. This leads to immediate failures in a substantial number of cases due to ill-conditioning of the matrix $P$, resulting in a failed attempt to compute the Cholesky factor $P^{\frac{1}{2}}$ in when $P$ is either semidefinite or contains very small negative eigenvalues. Mosek handles this case more robustly, but is still not able to solve a substantial number of problems to full accuracy within the benchmark time limit.

(a) Relative performance profile (b) Absolute performance profile (c) Benchmark timings as shifted geometric mean and failure rates Figure 1: Performance profiles for the Maros-Meszaros problem set

### Least-squares problems with SuiteSparse matrices

We next consider a collection of 23 sparse least-squares problems ${Ax} \approx b$ derived from matrices taken from the SuiteSparse Matrix Collection \[SuiteSparseMatrices\], following the equivalent set of benchmark examples from \[OSQP\]. For each case we compute an approximate solution by solving a constrained QP using two standard methods:

### Huber Problem

The *Huber fitting* \[Huber:1964, Huber:1981\] or *robust least squares* problem for a given matrix $A$ and vector $b$ is defined as where $a_{i}^{\top}$ is the $i^{\text{th}}$ row of $A$ and the *Huber loss function* $\phi:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ is defined as We set $M = 1$ for all test cases. This problem is equivalent \[Mangasarian:2000\] to the following quadratic program:

### LASSO Problem

The *least absolute shrinkage and selection operator (LASSO)* problem \[Tibshirani:1996, Candes:2008\] for a given matrix $A$ and vector $b$ is defined as We set $\lambda = \left\| {A^{\top}b} \right\|_{\infty}$ for all test cases. This problem is equivalent \[Mangasarian:2000\] to the following quadratic program:

### Results

Results for this benchmark set of 46 problems are shown in Figure 2. Clarabel is again the fastest solver overall with the Rust implementation marginally faster. In this test set only the Clarabel and Gurobi solvers are able to solve all cases to full accuracy.

(a) Relative performance profile (b) Absolute performance profile (c) Benchmark timings as shifted geometric mean and failure rates Figure 2: Performance profiles for the SuiteSparse least-squares problem set

### Constrained optimal control

Finally, we consider finite-horizon constrained optimal control problems with quadratic objectives. Problems of this type are of particular interest in embedded control systems, since the repeated online solution of such problems is the basis of the model predictive control (MPC) method \[Borrelli:MPCbook\]. We consider a collection of 72 such problems taken from the benchmark collection of industrial and academic applications in \[Kouzoupis:2015\]. Problems in this collection are in the form where the constraint sets $\mathcal{U}_{k}$, $\mathcal{Y}_{k}$ and $\mathcal{T}$ are interval constraints. All problems have $Q_{k} \succeq 0$, $R_{k} \succeq 0$ and $P \succ 0$, which ensures that the problems are all convex QPs. As is typical of optimal control problems for embedded systems, the dimension of the states $x_{k}$ and inputs $u_{k}$ are relatively small (max 12 and 4, respectively), with horizons $N$ up to 100.

### Results

Results for this benchmark set are shown in Figure 3. Clarabel is the fastest solver overall, and is the only solver tested with a 100% success rate in solving problems to full accuracy.

(a) Relative performance profile (b) Absolute performance profile (c) Benchmark timings as shifted geometric mean and failure rates Figure 3: Performance profiles for the optimal control problem set

### Benchmark problems with linear objectives

In this section we present benchmark results for optimization problems *without* quadratic objective terms, i.e. with $P = 0$ in $\mathcal{P}$. We again consider example problems taken or generated from standard open-source problem collections and covering a wide range of problem dimensions. Our test set covers cases with constraints on the positive orthant (i.e. linear programs), as well as both second-order and exponential cone programs.

### NETLIB LP problems

We first consider linear programming (LP) problems taken from the NETLIB collection, a standard collection of benchmark LPs \[netlib:1987, netlib\]. Our benchmark test set includes 117 feasible and 29 infeasible test cases, representing all NETLIB LP problem instances with source files not exceeding 2.5 MB.

Results for the feasible and infeasible test sets are shown in Figures 4 and 5, respectively. For these cases Clarabel has performance broadly similar to both Mosek and Gurobi for the feasible set, and somewhat slower for the infeasible set. This result is to be expected since most of the potential performance advantage of our method arises from improved handling of quadratic objectives, but illustrates that our implementation is, in the LP case, still broadly comparable.

(a) Relative performance profile (b) Absolute performance profile (c) Benchmark timings as shifted geometric mean and failure rates Figure 4: Performance profiles for the NETLIB Feasible LP problem set (a) Relative performance profile (b) Absolute performance profile (c) Benchmark timings as shifted geometric mean and failure rates Figure 5: Performance profiles for the NETLIB Infeasible LP problem set

### CBLIB exponential cone problems

We consider a collection of 39 exponential cone programs from the CBLIB benchmark collection \[CBLIB\] in order to test performance on nonsymmetric cone programs. For these problems our implementation has broadly similar performance to Mosek, with slightly faster solve times in the Rust implementation despite a generally higher iteration count.

(a) Relative performance profile (b) Absolute performance profile (c) Benchmark timings as shifted geometric mean and failure rates Figure 6: Performance profiles for the CBLIB Exponential Cone problem set

### Optimal power flow

We next consider a collection of optimal power flow problems based on power networks from IEEE PLS PGLib-OPF benchmark library \[PGLIB:2019\] and constructed using the PowerModels.jl benchmark test framework \[PowerModels:2018\]. This framework allows for the generation of optimal power flow problems with various modelling assumptions and convex relaxations applied \[PowerModels:survey1, PowerModels:survey2\]. We consider in particular linear programming problems based on linearized (i.e. direct current (DC)) power flow models \[PowerModels:LPcase\], and SOCPs arising from second-order cone relaxations of AC models \[PowerModels:SOCcase\]. Results from these benchmarks are shown in Figures 7 and 8, respectively.

For both of these test sets Clarabel outperforms the other solvers tested, albeit with a slightly higher failure rate for the LP benchmark tests relative to Gurobi (i.e. 3.3% vs 0% at full accuracy). For the SOCP benchmark tests in particular our success rate is substantially better than the other solvers tested. All solvers in our benchmark group struggled to some extent in solve large scale SOCPs to full accuracy. Our Rust implementation is able to solve to at least its reduced accuracy level for more than 99% of test cases though, a success rate considerably higher than ECOS or Mosek, both of which failed even at reduced accuracy on more than 50% of cases.

We note also that our success rates differ slightly between our Julia and Rust implementations, even though the implementation of our algorithm is (nearly) identical between the cases. We believe that this difference is attributable to minor differences in compiled code vectorizations and optimizations, which in some very difficult problems lead to slight differences in behavior at high accuracy.

(a) Relative performance profile (b) Absolute performance profile (c) Benchmark timings as shifted geometric mean and failure rates Figure 7: Performance profiles for the LP Optimal Power Flow problem set (a) Relative performance profile (b) Absolute performance profile (c) Benchmark timings as shifted geometric mean and failure rates Figure 8: Performance profiles for the SOCP Optimal Power Flow problem set

### Semidefinite program benchmarks

(a) Relative performance profile (b) Absolute performance profile (c) Benchmark timings as shifted geometric mean and failure rates Figure 9: Performance profiles for the SDPLIB Semidefinite Programming problem set Finally, we test performance on large-scale SDPs using the SDPLIB benchmark collection \[SDPLIB\]. We consider a collection of 64 problems from this collection, where problems from the collection are included if they are known to be feasible and could be solved on our testing platform using the reference solver Mosek. Since some of these problems are large, we set a time limit of 30 minutes for each problem.

For this set of benchmarks we compare only our Rust implementation of Clarabel with Mosek and use the supernodal factorization method of \[faer\]. We provide results for Clarabel both with and without the chordal decomposition described in §2.5 enabled.

For this set of benchmarks we find that Clarabel outperforms Mosek overall, particularly when considering problems solved to full accuracy solutions. Clarabel also outperforms Mosek, sometimes very substantially, for those test cases with a considerable amount of sparsity that are amenable to chordal decomposition. We include in Appendix A a detailed breakdown of the results for this benchmark set, including performance both with and without chordal decomposition enabled. For problems in which no chordal structure could be identified, there is very little difference in performance between our two solver configurations. However, some problems (e.g. the series of problems 'ARCH0'--'ARCH8') show improvements in computation time of nearly 100x when chordal decomposition is enabled. We note that further improvements are likely possible in our implementation of chordal decomposition, particularly if more sophisticated clique-merging scoring methods are employed.

## Conclusions

We have presented a novel interior-point solver for conic optimization problems with quadratic objectives. Our method uses a homogeneous embedding inspired by previous work on monotone complementarity problems, but not previously applied to interior-point conic optimization in any widely available solver. We have shown that our method is competitive with state-of-the-art solvers for a wide range of problem classes, and in particular outperforms state-of-the-art solvers in problems with quadratic objectives (QPs), large-scale SOCPs, and SDPs with significant sparsity structure.

Our implementation of Clarabel is available as open-source software in both Rust and Julia, with several other language interfaces, and is available as a standard solver in the CVXPY modelling package. Clarabel already has growing base of both academic and industrial users and has been downloaded several million times since its initial release.
