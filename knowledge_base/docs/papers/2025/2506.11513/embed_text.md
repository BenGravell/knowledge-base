## Introduction

### Parametric convex optimization

A parametric convex optimization problem can be written as

where $x \in \text{R}^{n}$ is the variable and $\theta \in \Theta \subseteq \text{R}^{p}$ is the parameter, i.e., data that is given and known whenever ((https://arxiv.org/html/2506.11513v2#S1.E1 "In 1.1 Parametric convex optimization ‣ 1 Introduction ‣ Automatic Generation of Explicit Quadratic Programming Solvers")) is solved. The objective function $f_{0}$ and the inequality constraint functions $f_{i}$, $i = {1,\ldots,m}$, are convex in $x$ and the equality constraint functions $h_{i}$, $i = {1,\ldots,q}$, are affine in $x$, for any given value of $\theta \in \Theta$ \[[](https://arxiv.org/html/2506.11513v2#bib.bibx22)\]. We refer to a solution of ((https://arxiv.org/html/2506.11513v2#S1.E1 "In 1.1 Parametric convex optimization ‣ 1 Introduction ‣ Automatic Generation of Explicit Quadratic Programming Solvers")) as $x^{\star}{(\theta)}$ to emphasize its dependence on the parameter $\theta$. Here we neglect that $x^{\star}$ might not be unique or might not exist, and refer to the mapping from $\theta$ to $x$ as the solution map of the parametrized problem.

Convex optimization is used in various domains, including control systems \[[](https://arxiv.org/html/2506.11513v2#bib.bibx9), [RMD^+^17](https://arxiv.org/html/2506.11513v2#bib.bibx61), [](https://arxiv.org/html/2506.11513v2#bib.bibx47), [](https://arxiv.org/html/2506.11513v2#bib.bibx46), [](https://arxiv.org/html/2506.11513v2#bib.bibx69), [](https://arxiv.org/html/2506.11513v2#bib.bibx17), [](https://arxiv.org/html/2506.11513v2#bib.bibx5), [](https://arxiv.org/html/2506.11513v2#bib.bibx40)\], signal and image processing \[[](https://arxiv.org/html/2506.11513v2#bib.bibx27), [](https://arxiv.org/html/2506.11513v2#bib.bibx26), [](https://arxiv.org/html/2506.11513v2#bib.bibx51), [](https://arxiv.org/html/2506.11513v2#bib.bibx70)\], and quantitative finance \[[](https://arxiv.org/html/2506.11513v2#bib.bibx59), [BJK^+^24](https://arxiv.org/html/2506.11513v2#bib.bibx15), [BBD^+^17](https://arxiv.org/html/2506.11513v2#bib.bibx6), [](https://arxiv.org/html/2506.11513v2#bib.bibx54), [](https://arxiv.org/html/2506.11513v2#bib.bibx37), [](https://arxiv.org/html/2506.11513v2#bib.bibx50)\], just to name a few that are particularly relevant for this work.

### Explicit solvers for multiparametric programming

Traditionally, $x^{\star}{(\theta)}$ is evaluated using an iterative numerical method that takes a given parameter value and computes an (almost) optimal point $x^{\star}{(\theta)}$ \[[](https://arxiv.org/html/2506.11513v2#bib.bibx36), [SBG^+^20](https://arxiv.org/html/2506.11513v2#bib.bibx64), [](https://arxiv.org/html/2506.11513v2#bib.bibx57), [](https://arxiv.org/html/2506.11513v2#bib.bibx29)\]. We focus here on a very special case when $x^{\star}{(\theta)}$ can be expressed in closed form, as an explicit function that maps a given value of $\theta$ directly to a solution $x^{\star}{(\theta)}$. Such explicit solvers are practical for only some problems, and generally only smaller instances, but when they are practical they can offer a number of advantages over generic iterative solvers. Developing such solvers for parametric programs is now known as multiparametric programming.

### Related work

### Multiparametric programming

Investigations of the theoretical properties of parametric convex optimization problems date back to the 60s \[[](https://arxiv.org/html/2506.11513v2#bib.bibx53)\] and were largely extended in the 80s \[[](https://arxiv.org/html/2506.11513v2#bib.bibx32)\]. After early work on explicitly solving parametric linear programs (LPs) in the context of economics \[[](https://arxiv.org/html/2506.11513v2#bib.bibx39)\] in the 70s, researchers started investigating the explicit solution of different convex optimization problems in the early 2000s. Some of the first papers developed explicit solutions to model predictive control problems based on quadratic programs (QPs) \[[](https://arxiv.org/html/2506.11513v2#bib.bibx18)\] and LPs \[[BBM^+^02](https://arxiv.org/html/2506.11513v2#bib.bibx7)\], and general algorithms were developed for explicitly solving QPs \[[](https://arxiv.org/html/2506.11513v2#bib.bibx18), [](https://arxiv.org/html/2506.11513v2#bib.bibx65), [](https://arxiv.org/html/2506.11513v2#bib.bibx60), [](https://arxiv.org/html/2506.11513v2#bib.bibx35)\] and LPs \[[](https://arxiv.org/html/2506.11513v2#bib.bibx8)\]. These are often cited as multiparametric linear or quadratic programming, respectively, where the latter is often abbreviated as MPQP. Further, people have worked on verifying the complexity of such methods \[[](https://arxiv.org/html/2506.11513v2#bib.bibx25)\], on approximate or suboptimal multiparametric programming \[[](https://arxiv.org/html/2506.11513v2#bib.bibx13), [](https://arxiv.org/html/2506.11513v2#bib.bibx43), [](https://arxiv.org/html/2506.11513v2#bib.bibx14)\], on multiparametric programming for linear complementary problems \[[](https://arxiv.org/html/2506.11513v2#bib.bibx45)\], and on synthesizing specialized hardware for multiparametric programming \[[](https://arxiv.org/html/2506.11513v2#bib.bibx44), [](https://arxiv.org/html/2506.11513v2#bib.bibx20), [ROL^+^23](https://arxiv.org/html/2506.11513v2#bib.bibx62)\].

Software implementations include the Hybrid Toolbox \[[](https://arxiv.org/html/2506.11513v2#bib.bibx10)\], the Multi-Parametric Toolbox \[[](https://arxiv.org/html/2506.11513v2#bib.bibx41)\], the Model Predictive Control Toolbox \[[](https://arxiv.org/html/2506.11513v2#bib.bibx11)\], and the POP Toolbox \[[ODP^+^16](https://arxiv.org/html/2506.11513v2#bib.bibx58)\] in Matlab, the MPQP solver in the proprietary FORCES PRO software \[[](https://arxiv.org/html/2506.11513v2#bib.bibx31)\], and the PDAQP solver \[[](https://arxiv.org/html/2506.11513v2#bib.bibx1)\] in Julia and Python, which we use in this work.

Potential advantages of an explicit solver over a more general purpose iterative solver can include transparency, interpretability, reliability, and speed. Since the solver is essentially a lookup table, with an explicit affine function associated with each region, there is no question of convergence. Indeed, we can explicitly determine the maximum number of floating-point operations (FLOPS) required to compute $x^{\star}{(\theta)}$ given $\theta$ \[[](https://arxiv.org/html/2506.11513v2#bib.bibx25), [](https://arxiv.org/html/2506.11513v2#bib.bibx3)\]. An explicit solver involves no division, so floating-point overflow or divide-by-zero exceptions cannot occur. For the same reason, it is possible to store the coefficients in a lower precision format such as 16-bit floating-point () to reduce storage, and possibly to carry out the computations in lower precision as well, to increase speed or use low-cost electronic boards (at the cost of a modest decrease in accuracy).

The disadvantages of using an explicit solver all relate to its worst-case exponential scaling with problem size. This limits its practical use to relatively small problems, which however do arise in many application areas. Even when it is practical to use an explicit solver, the solver data size can be large, since we must store the coefficients of the explicit solution map.

### Code generation for convex optimization

While typical convex optimization solvers are designed for general-purpose computers \[[](https://arxiv.org/html/2506.11513v2#bib.bibx28), [](https://arxiv.org/html/2506.11513v2#bib.bibx36)\], we are mostly interested in embedded applications with hard real-time constraints, and also non-embedded applications where extreme speeds are required.

A *code generator* heavily exploits the structure of the functions in ((https://arxiv.org/html/2506.11513v2#S1.E1 "In 1.1 Parametric convex optimization ‣ 1 Introduction ‣ Automatic Generation of Explicit Quadratic Programming Solvers")) and generates custom C code for solving the problem fast and reliably for changing values of $\theta$, while fulfilling rules for safety-critical code \[[](https://arxiv.org/html/2506.11513v2#bib.bibx42)\]. Examples of code generators for iterative solvers are CVXGEN \[[](https://arxiv.org/html/2506.11513v2#bib.bibx52)\] (for general QPs), CVXPYgen \[[SBD^+^22](https://arxiv.org/html/2506.11513v2#bib.bibx63)\], which interfaces with the OSQP code generator \[[BSM^+^17](https://arxiv.org/html/2506.11513v2#bib.bibx21)\] and QOCOGEN \[[](https://arxiv.org/html/2506.11513v2#bib.bibx24)\] (for QPs and second-order cone programs, respectively), and acados \[[VFK^+^21](https://arxiv.org/html/2506.11513v2#bib.bibx68)\] and the proprietary FORCES PRO \[[](https://arxiv.org/html/2506.11513v2#bib.bibx31)\], both specifically designed for QP-based and nonlinear control problems. These code generators are used for many applications. CVXGEN, for example, is used to guide and control all of the SpaceX first stage landings \[[](https://arxiv.org/html/2506.11513v2#bib.bibx16)\].

### Domain-specific languages for optimization

Code generators typically accept problem specifications given in a domain specific language (DSL) for convex optimization \[[L0̈4](https://arxiv.org/html/2506.11513v2#bib.bibx49), [](https://arxiv.org/html/2506.11513v2#bib.bibx34)\]. A DSL allows the user to describe the problem in a natural high level human readable way, eliminating the effort (and risk of error) in transforming the problem to the standard form required by a solver. For example there can be multiple variables or parameters, with names that make sense in the application; the code generator takes care of mapping these to our generic $x \in \text{R}^{n}$ and $\theta \in \Theta$. Well-known DSLs include YALMIP \[[L0̈4](https://arxiv.org/html/2506.11513v2#bib.bibx49)\] and CVX \[[](https://arxiv.org/html/2506.11513v2#bib.bibx34)\] in Matlab, CVXPY \[[](https://arxiv.org/html/2506.11513v2#bib.bibx28)\] in Python, Convex.jl \[[UMZ^+^14](https://arxiv.org/html/2506.11513v2#bib.bibx67)\] and JuMP \[[](https://arxiv.org/html/2506.11513v2#bib.bibx30)\] in Julia, and CVXR \[[](https://arxiv.org/html/2506.11513v2#bib.bibx33)\] in R. We focus on CVXPY.

### Contribution

In this paper, we adapt the code generator CVXPYgen with the multiparametric explicit QP solver PDAQP to generate explicit solvers for convex optimization problems, described in CVXPY, that can be reduced to QPs. Along with C and C++ code for the generated solver, we generate a Python interface for rapid prototyping and non-embedded applications.

We give four representative application examples, involving linear regression, power management in residential buildings, model predictive control, and financial portfolio optimization. Our code generator accelerates the solve time for these examples by up to three orders of magnitude compared to directly using CVXPY and its default QP solver, with solve times down to hundreds of nanoseconds (on a standard laptop).

### Outline

In §(https://arxiv.org/html/2506.11513v2#S2 "2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers") we give a quick derivation of the explicit solution map for a parametric QP. In §(https://arxiv.org/html/2506.11513v2#S3 "3 Code generation ‣ Automatic Generation of Explicit Quadratic Programming Solvers") we explain how we generate source code for an explicit solver that is described in the modeling language CVXPY, and how to interface with the generated code. We illustrate the explicit solver code generation process in §(https://arxiv.org/html/2506.11513v2#S4 "4 Hello world ‣ Automatic Generation of Explicit Quadratic Programming Solvers"). In §(https://arxiv.org/html/2506.11513v2#S5 "5 Applications ‣ Automatic Generation of Explicit Quadratic Programming Solvers") we assess the numerical performance of the explicit solvers for several practical examples. We report the time it takes to generate and compile the generated code, the size of the resulting binary files, and the solve times.

## Explicit solution of parametric QPs

### Parametric QP

where $x \in \text{R}^{n}$ is the variable, and the data are $P \in \text{S}_{+ +}^{n}$ (the set of symmetric positive definite $n \times n$ matrices), $q \in \text{R}^{n}$, $A \in \text{R}^{m \times n}$, and $b \in \text{R}^{m}$. The inequality in the constraints is elementwise.

Our focus is on the case when the data $P$ and $A$ are given, and $q$ and $b$ are affine functions of a parameter $\theta \in \text{R}^{p}$,

where $u \in \text{R}^{n}$, $U \in \text{R}^{n \times p}$, $v \in \text{R}^{m}$, and $V \in \text{R}^{m \times p}$ are given. We refer to the QP ((https://arxiv.org/html/2506.11513v2#S2.E2 "In 2.1 Parametric QP ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")) parametrized by $\theta$ in ((https://arxiv.org/html/2506.11513v2#S2.E3 "In 2.1 Parametric QP ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")) as a parametrized QP. Since the objective is strictly convex, there is at most one solution of the QP ((https://arxiv.org/html/2506.11513v2#S2.E2 "In 2.1 Parametric QP ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")) for each value of $\theta$. We refer to the mapping from $\theta$ to the optimal $x$ (when it exists) as the solution map of the parametrized QP ((https://arxiv.org/html/2506.11513v2#S2.E2 "In 2.1 Parametric QP ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")).

### Other QP forms

There are several other standard forms for a parametrized QP, both for analysis and as an interface to solvers \[[](https://arxiv.org/html/2506.11513v2#bib.bibx18), [](https://arxiv.org/html/2506.11513v2#bib.bibx65), [](https://arxiv.org/html/2506.11513v2#bib.bibx1)\], but it is easy to translate between them by introducing additional variables and constraints \[[](https://arxiv.org/html/2506.11513v2#bib.bibx22)\].

### Constraints on the parameters

In many applications we are also given a set $\Theta \subseteq \text{R}^{p}$ of possible parameter values. For simplicity we ignore this, but occasionally mention how this set of known possible values of $\theta$ can be handled. When we do address the parameter set, we assume it is a polyhedron.

### Optimality conditions

### Active constraints

We denote the $i$th row of $A$ as $a_{i}^{T}$, so the inequality constraints in ((https://arxiv.org/html/2506.11513v2#S2.E2 "In 2.1 Parametric QP ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")) can be expressed as ${a_{i}^{T}x} \leq b_{i}$, $i = {1,\ldots,m}$. We say that the $i$th inequality constraint is tight or active if ${a_{i}^{T}x} = b_{i}$. We let $\mathcal{A} = {\{ i\mid{{a_{i}^{T}x} = b_{i}}\}} \subseteq {\{ 1,\ldots,m\}}$ denote the set of active constraints \[[](https://arxiv.org/html/2506.11513v2#bib.bibx25), [](https://arxiv.org/html/2506.11513v2#bib.bibx38)\] (which depends on $x$, $A$, and $b$).

Let $\lambda \in \text{R}_{+}^{m}$ denote a dual variable associated with the linear inequality constraints in ((https://arxiv.org/html/2506.11513v2#S2.E2 "In 2.1 Parametric QP ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")). The optimality conditions for problem ((https://arxiv.org/html/2506.11513v2#S2.E2 "In 2.1 Parametric QP ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")) are

The first is primal feasibility; the second is nonnegativity of dual variables; the third is dual feasibility (stationarity of the Lagrangian); and the last one is complementary slackness \[[](https://arxiv.org/html/2506.11513v2#bib.bibx22), §5.5.3\].

Let $\overset{\sim}{A}$, $\overset{\sim}{b}$, and $\overset{\sim}{\lambda}$ denote the row slices of $A$, $b$, and $\lambda$, respectively, corresponding to the active constraints, i.e., $i \in \mathcal{A}$. Let $\hat{A}$, $\hat{b}$, and $\hat{\lambda}$ denote the row slices of $A$, $b$, and $\lambda$, respectively, corresponding to the inactive constraints, i.e., $i \notin \mathcal{A}$. By complementary slackness, we must have $\lambda_{i} = 0$ for $i \notin \mathcal{A}$, so $\hat{\lambda} = 0$. With $\hat{\lambda} = 0$, which we now assume, complementary slackness holds. Since $\hat{\lambda} = 0$, $A^{T}\lambda$ can be expressed as ${\overset{\sim}{A}}^{T}\overset{\sim}{\lambda}$, and dual feasibility can be expressed as

Since $\mathcal{A}$ is the active set corresponding to $x$, we have

These two sets of linear equations can be summarized as the Karush-Kuhn-Tucker (KKT) system

We assume that linear independence constraint qualification (LICQ) \[[](https://arxiv.org/html/2506.11513v2#bib.bibx12), [](https://arxiv.org/html/2506.11513v2#bib.bibx56), [](https://arxiv.org/html/2506.11513v2#bib.bibx22)\] holds, i.e., that the rows of $\overset{\sim}{A}$ are linearly independent. Then, it is well known that ((https://arxiv.org/html/2506.11513v2#S2.E4 "In Active constraints. ‣ 2.2 Optimality conditions ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")) can be uniquely solved for $(x,\overset{\sim}{\lambda})$ \[[](https://arxiv.org/html/2506.11513v2#bib.bibx22), §10.1.1\], \[[](https://arxiv.org/html/2506.11513v2#bib.bibx23), §12.3\] and we re-write ((https://arxiv.org/html/2506.11513v2#S2.E4 "In Active constraints. ‣ 2.2 Optimality conditions ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")) as

This shows that knowledge of the active set $\mathcal{A}$ determines the primal and dual solutions of the QP ((https://arxiv.org/html/2506.11513v2#S2.E2 "In 2.1 Parametric QP ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")). We note that $(x,\overset{\sim}{\lambda})$ are the solution of the problem of minimizing the objective of the QP subject to the linear equality constraints ${\overset{\sim}{A}x} = \overset{\sim}{b}$.

From ((https://arxiv.org/html/2506.11513v2#S2.E5 "In Active constraints. ‣ 2.2 Optimality conditions ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")) we see that the solution is a linear function of the data $q$ and $b$, provided the active set does not change. This implies that the solution is an affine function of the parameter $\theta$, provided the active set does not change.

When $(x,\overset{\sim}{\lambda})$ have the values ((https://arxiv.org/html/2506.11513v2#S2.E5 "In Active constraints. ‣ 2.2 Optimality conditions ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")) (with $\hat{\lambda} = 0$), they satisfy complementary slackness and dual feasibility. The remaining two optimality conditions, primal feasibility and dual nonnegativity, can be expressed as

since ${Ax} \leq b$ holds (as equality) for rows with $i \in \mathcal{A}$ and $\hat{\lambda} = 0$. The inequality ((https://arxiv.org/html/2506.11513v2#S2.E6 "In Active constraints. ‣ 2.2 Optimality conditions ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")) is a set of linear inequalities in the data $b$ and $q$, and therefore defines a polyhedron. When $(b,q)$ is in this polyhedron, called the critical region associated with the active set $\mathcal{A}$, $(x,\lambda)$ given by the linear function ((https://arxiv.org/html/2506.11513v2#S2.E5 "In Active constraints. ‣ 2.2 Optimality conditions ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")) are primal and dual optimal for the QP ((https://arxiv.org/html/2506.11513v2#S2.E2 "In 2.1 Parametric QP ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")).

Since compositions of affine functions are affine, it follows that the primal and dual solutions of the QP ((https://arxiv.org/html/2506.11513v2#S2.E2 "In 2.1 Parametric QP ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")) are (locally) affine functions of $\theta$. Since the inverse image of a polyhedron under an affine mapping is a polyhedron, the values of $\theta$ over which this affine function gives the solution is also a polyhedron. Thus the solution map is a piecewise affine function of $\theta$, with the polyhedral regions determined by the active set. By the uniqueness of the solution, it is not difficult to prove that such a map is also continuous across region boundaries \[[](https://arxiv.org/html/2506.11513v2#bib.bibx18)\]. This continuity property guarantees a certain degree of robustness to numerical errors when evaluating the map.

### Explicit parametric QP solver

The optimality conditions discussed above suggest a naive explicit solver, which can be practical when $m$ is small. We search over all $2^{m}$ potential active sets. For each one we compute $x$ and $\lambda$ via ((https://arxiv.org/html/2506.11513v2#S2.E5 "In Active constraints. ‣ 2.2 Optimality conditions ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")), and then check whether ((https://arxiv.org/html/2506.11513v2#S2.E6 "In Active constraints. ‣ 2.2 Optimality conditions ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")) holds. If this happens, we have found the solution; if not, the problem is infeasible.

Now we consider the parameter dependence. For each of the $2^{m}$ potential active sets, we can express ((https://arxiv.org/html/2506.11513v2#S2.E5 "In Active constraints. ‣ 2.2 Optimality conditions ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")) as

where $\overset{\sim}{V}$ and $\overset{\sim}{v}$ are the (row) slices of $V$ and $v$, respectively, corresponding to $\mathcal{A}$. We then express ((https://arxiv.org/html/2506.11513v2#S2.E6 "In Active constraints. ‣ 2.2 Optimality conditions ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")) in terms of $\theta$ as

For some choices of potential active sets, the inequalities ${H\theta} \leq j$ (together with $\theta \in \Theta$) are infeasible. We drop these, and consider only the remaining $K$ sets of potential active sets, and label them as $k = {1,\ldots,K}$. We can compute the coefficients of the piecewise affine solution map, denoted $F_{k}$ and $g_{k}$, and their associated region, defined by $H_{k}$ and $j_{k}$, before knowing the specific value of $\theta$. Thus we have the explicit solution map

Different existing MPQP solvers differ in how they avoid enumerating all $2^{m}$ active sets \[[](https://arxiv.org/html/2506.11513v2#bib.bibx1), §II-c\]. When $\theta \subseteq \Theta$ satisfies none of the inequalities above, the QP is infeasible. The collection of coefficient matrices and vectors $F_{k}$, $g_{k}$, $H_{k}$, $j_{k}$, $k = {1,\ldots,K}$ gives an explicit representation of the solution map of the parametrized QP ((https://arxiv.org/html/2506.11513v2#S2.E2 "In 2.1 Parametric QP ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")). Since we can compute these matrices and vectors (and determine the value of $K$) before we have specified $\theta$, we refer to computing these coefficients as the offline solve. Evaluating ((https://arxiv.org/html/2506.11513v2#S2.E7 "In 2.3 Explicit parametric QP solver ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")) for a given value of $\theta$ is called the online solve. Note that it involves no division.

The number of coefficients in the explicit solver is around $K{({n + m})}p$, up to a factor of $K$ larger than the number of coefficients in the original problem, $n^{2} + {nm} + {{({n + m})}p}$ (neglecting sparsity). Even though $K$ can grow exponentially with $m$, it is often practical for small problems \[[](https://arxiv.org/html/2506.11513v2#bib.bibx18), [](https://arxiv.org/html/2506.11513v2#bib.bibx65), [](https://arxiv.org/html/2506.11513v2#bib.bibx25)\].

### Implementation

When we explicitly solve a parametrized QP in practice, some of our initial assumptions can be relaxed. We can handle positive semidefinite $P$ (instead of just positive definite); we directly handle equality constraints; and we do not require LICQ. (When $P$ is not positive definite, the solver provides *a* solution, rather than *the* solution, since the solution need not be unique in this case.)

In the offline phase, implementations do not search all $2^{m}$ possible active sets, but instead find nonempty regions one by one. This allows us to handle problems where $2^{m}$ is very large, but $K$, the number of (nonempty) regions, is still moderate.

In the online solve, explicit solvers store the regions in a way that facilitates faster search than a simple linear search over $k = {1,\ldots,K}$, typically involving a pre-computed tree. Other methods are used to either reduce the storage or increase the speed of the online evaluations.

We use the specific solver PDAQP \[[](https://arxiv.org/html/2506.11513v2#bib.bibx1)\], which has several such accelerations implemented. The offline solve is made more efficient by systematic searching over neighboring regions. The online solve benefits from a binary search tree for the search over regions \[[](https://arxiv.org/html/2506.11513v2#bib.bibx66)\]. Complete details can be found in

[https://github.com/darnstrom/pdaqp](https://github.com/darnstrom/pdaqp).

## Code generation

### Domain-specific languages for optimization

When solving a problem instance, DSLs perform a sequence of three steps. First, the DSL transforms the user-defined problem into a form accepted by a standard or canonical solver. For example, a constraint like

for $x \in \text{R}$ is translated to

as it appears in a canonical form like ((https://arxiv.org/html/2506.11513v2#S2.E2 "In 2.1 Parametric QP ‣ 2 Explicit solution of parametric QPs ‣ Automatic Generation of Explicit Quadratic Programming Solvers")). In a second step, a canonical solver (like PDAQP) is called to solve the canonical problem. Ultimately, a solution for the user-defined problem is retrieved from the solution returned by the canonical solver.

Typically, these three steps are performed every time a problem instance is solved. We call such systems *parser-solvers*. When dealing with a parametric QP, whose structure does not change between solves, repeated parsing, i.e., discovering how to reduce the problem to canonical form, is unnecessary and usually inefficient.

### Code generation for explicitly solving QPs

Consider an application where we solve many instances of a specific parametric QP, possibly in an embedded system with hard real-time constraints. For such applications, a *code generator* makes more sense.

As illustrated in figure (https://arxiv.org/html/2506.11513v2#S3.F1 "Figure 1 ‣ 3.2 Code generation for explicitly solving QPs ‣ 3 Code generation ‣ Automatic Generation of Explicit Quadratic Programming Solvers"), a code generator for explicitly solving QPs takes as input the parametric QP, and generates source code that is tailored for (explicitly) solving instances of that parametric QP. The source code is then compiled into an efficient custom solver, which has a number of benefits compared to parser-solvers. First, by exploiting the parametric structure and caching canonicalization, the compiled solver becomes faster. Second, the compiled solver can be deployed in embedded systems, satisfying rules for safety-critical code \[[](https://arxiv.org/html/2506.11513v2#bib.bibx42)\].

Figure 1: Code generation for explicitly solving a parametric QP.

We extend the open-source code generator CVXPYgen \[[SBD^+^22](https://arxiv.org/html/2506.11513v2#bib.bibx63)\] to generate code for explicitly solving QPs. The QP is modeled with CVXPY before CVXPYgen generates library-, allocation-, and division-free code for translating between the user-defined problem and a canonical form (that of PDAQP in this case) for explicitly solving QPs. Open source code and full documentation for CVXPYgen and its explicit solve feature is available at

[https://github.com/cvxgrp/cvxpygen](https://github.com/cvxgrp/cvxpygen).

### Disciplined parametrized programming

We require the QP to be modeled in CVXPY using disciplined parametrized programming (DPP) \[[AAB^+^19](https://arxiv.org/html/2506.11513v2#bib.bibx2)\]. The DPP rules mildly restrict how parameters may enter the objective and constraints. Generally speaking, if parameters enter all expressions in an affine way, then the problem is DPP-compliant. Details on the DPP rules can be found at [https://www.cvxpy.org](https://www.cvxpy.org).

### Canonicalization

When a problem is modeled according to DPP, parameter canonicalization and solution retrieval are affine mappings,

where $\theta^{\text{user}}$ and $x^{\text{user}}$ are the user-defined parameter and variable, respectively. The matrices $C$ and $R$ are typically very sparse. The retrieval matrix $R$ is usually wide, i.e., there are more canonical variables than user-defined variables, since the canonicalization step introduces auxiliary variables \[[](https://arxiv.org/html/2506.11513v2#bib.bibx4)\]. CVXPYgen generates code for the respective sparse matrix-vector multiplications. In fact, the solution retrieval ${Rx} + r$ often reduces to simple pointing to memory in C.

### Parameter constraints

The user may specify constraints on parameters. Suppose that the values of the user-defined parameter $\theta^{\text{user}}$ lie in the set $\Theta^{\text{user}}$. Then, similarly to how the parameter $\theta^{\text{user}}$ itself is canonicalized, the parameter constraints are translated to the canonical set of possible parameters $\Theta$.

### Limitations

In PDAQP the number of inequality constraints $m$ is limited to 1024 so the regions can be efficiently represented as a bit string. If $K$, or the size of the data in the explicit solver, exceed a given limit, the offline phase is terminated with a warning.

## Hello world

Here we present a simple example to illustrate how explicit solver code generation works. Consider the parametric QP

where $\beta \in \text{R}^{d}$ and $v \in \text{R}$ are the variables, $\theta^{\text{user}} = y \in \text{R}^{p}$ is the parameter with $\Theta^{\text{user}} = {\{ y\mid{l \leq y \leq u}\}}$, and $\mathbf{1}$ denotes the vector with all entries one. The bounds $l \in \text{R}^{p}$ and $u \in \text{R}^{p}$ and the matrix $X \in \text{R}^{p \times d}$ are given data.

### Modeling and code generation

The problem can be formulated in CVXPY as shown in figure (https://arxiv.org/html/2506.11513v2#S4.F2 "Figure 2 ‣ 4.1 Modeling and code generation ‣ 4 Hello world ‣ Automatic Generation of Explicit Quadratic Programming Solvers"), up to line 11. Note that in line 10, we specify $\Theta^{\text{user}}$ with standard CVXPY constraints. We generate the explicit solver in line 13.

2from cvxpygen import cpg
5beta = cp.Variable(d, name=’beta’)
9obj = cp.Minimize(cp.sum_squares(X @ beta + v - y))
11prob = cp.Problem(obj, constr)
13cpg.generate_code(prob, solver=’explicit’)
Figure 2: Generating an explicit solver with CVXPYgen.

### C interface

Figure (https://arxiv.org/html/2506.11513v2#S4.F3 "Figure 3 ‣ 4.2 C interface ‣ 4 Hello world ‣ Automatic Generation of Explicit Quadratic Programming Solvers") shows how the generated explicit solver can be used in C. In line 7, the first entry of the parameter $y$ is updated to the value $1.2$. The function `cpg_update_y` ensures that the parameter values are within their pre-specified limits (otherwise, it maps the given value back onto $\Theta$). In line 8, the problem is solved explicitly with the `cpg_solve` function. In lines 9 and 10, respectively, the first entry of the optimal coefficients $\beta$ and the optimal $v$ is read and printed. In line 11, the resulting objective value is calculated and printed. Note that the calculation of the objective value is kept in a separate function from the solve function, for maximal efficiency.

2#include "cpg_workspace.h"
3#include "cpg_solve.h"
5int main(int argc, char *argv[]){
9 printf("%f\n", CPG_Result.prim-&gt;beta);
10 printf("%f\n", CPG_Result.prim-&gt;v);
11 printf("%f\n", cpg_obj());
Figure 3: Using the explicit solver.

Figure (https://arxiv.org/html/2506.11513v2#S4.F4 "Figure 4 ‣ 4.2 C interface ‣ 4 Hello world ‣ Automatic Generation of Explicit Quadratic Programming Solvers") shows the C structs that store the result. In the example above, we access the primal solution `beta` and `v` via the `prim` field of the result struct `CPG_Result`. The dual variables in `CPG_Dual_t` are named according to the index in the list of CVXPY constraints.

2 cpg_float *beta; // primal variable beta
3 cpg_float v; // primal variable v
7 cpg_float *d0; // dual variable d0
11 CPG_Prim_t *prim; // primal solution
12 CPG_Dual_t *dual; // dual solution
Figure 4: Data structure of explicit solver result.

### CVXPY interface

We consider a small instance of the parametric QP ((https://arxiv.org/html/2506.11513v2#S4.E8 "In 4 Hello world ‣ Automatic Generation of Explicit Quadratic Programming Solvers")) with $d = 2$, $p = 3$, the entries of $X$ generated IID from $\mathcal{N}{}$, $l = 0$, and $u = \mathbf{1}$. We assign the entries of $y$ randomly between $0$ and $1$ and solve the problem three times: with CVXPY using the iterative OSQP solver \[[SBG^+^20](https://arxiv.org/html/2506.11513v2#bib.bibx64)\], with CVXPYgen using OSQP, and with CVXPYgen using the explicit PDAQP solver.

Figure (https://arxiv.org/html/2506.11513v2#S4.F5 "Figure 5 ‣ 4.3 CVXPY interface ‣ 4 Hello world ‣ Automatic Generation of Explicit Quadratic Programming Solvers") shows the comparison, demonstrating how the explicit solver can be used via its auto-generated CVXPY interface. Starting in line 15, we show that the primal and dual solutions and the objective values are all close, respectively.

1from code_osqp.cpg_solver import cpg_solve
2prob.register_solve(’gen_OSQP’, cpg_solve)
4from code_explicit.cpg_solver import cpg_solve
5prob.register_solve(’gen_explicit’, cpg_solve)
7def print_result():
9 print(f’beta: {beta.value}’)
10 print(f’dual: {constr.dual_value}’)
11 print(f’obj: {obj.value}’)
15prob.solve(solver=’OSQP’)
23prob.solve(method=’gen_OSQP’)
31prob.solve(method=’gen_explicit’)

Figure 5: Using the explicit solver in CVXPY.

## Applications

In this section we report timing and code size details for some typical application examples. In each case we compare CVXPYgen using the explicit PDAQP solver to CVXPYgen using the iterative OSQP solver and standard CVXPY using OSQP. When using CVXPYgen with the OSQP solver, we use OSQP's code generation feature, which caches the factorization of the KKT system, for accelerated solving \[[BSM^+^17](https://arxiv.org/html/2506.11513v2#bib.bibx21)\]. When using OSQP in CVXPY or CVXPYgen, we set both the relative and absolute tolerances to $10^{- 4}$ (the default in CVXPY). We run the experiments on an Apple M1 Pro, compiling with Clang at optimization level 3. For iterative and explicit code generation, we report solve times in C, and the overall time when solving from Python via the auto-generated CVXPY interface. We also give the time it takes to generate and compile the code.

### Monotone regression

We consider the monotone regression problem

where $x \in \text{R}^{d}$ is the variable and $\theta^{\text{user}} = b \in \text{R}^{q}$ is the parameter, with $\Theta^{\text{user}} = {\lbrack{- 1},1\rbrack}^{q}$. The matrix $A \in \text{R}^{q \times d}$ is given. (This is called monotone regression since the components $x_{i}$ are constrained to be monotonically nondecreasing.)

### Problem instances

We consider $d = 5$ and $q = 10$. The entries of $A$ are generated IID from $\mathcal{N}{}$, and we generate 100 problem instances where $b$ is sampled uniformly from $\Theta^{\text{user}}$.

### Results

We obtain $n = 15$ variables, $m = {d - 1} = 4$ inequality constraints, and $p = q = 10$ parameters. (In this case, the canonicalization step introduced ${n - d} = 10$ auxiliary variables.) We find $K = 16$ regions (which equals $2^{m}$, the maximum possible number of active sets). Table (https://arxiv.org/html/2506.11513v2#S5.T1 "Table 1 ‣ Results. ‣ 5.1 Monotone regression ‣ 5 Applications ‣ Automatic Generation of Explicit Quadratic Programming Solvers") shows the average solve times and binary sizes.

Table 1: Timing and binary sizes for monotone regression problem.

### Power management

### Problem

A nonnegative electric power load $L$ is served by a PV (photovoltaic solar panel) system, a storage battery, and a grid connection \[[BNC^+^17](https://arxiv.org/html/2506.11513v2#bib.bibx19), [](https://arxiv.org/html/2506.11513v2#bib.bibx55)\]. We denote the solar power as $s$, the battery power as $b$, and the grid power as $g$. These three power sources supply the load, so we have

The PV power satisfies $0 \leq s \leq S$, where $S \geq 0$ is the available PV power. The battery power satisfies ${- C} \leq b \leq D$, where $D > 0$ is the maximum possible discharge power and $C > 0$ is the maximum possible charge power. The grid power satisfies $g \geq 0$, i.e., we cannot sell power back to the grid. The (positive) price of the grid power is $P$, so the grid cost is $Pgh$, where $h$ is the duration of one time period, over which we hold the power values constant.

The battery state of charge at the beginning of the time period is denoted $q$, and satisfies $0 \leq q \leq Q$, where $Q$ is the battery capacity. At the beginning of the next time period the battery charge is $q^{+} = {q - {hb}}$. We must have $0 \leq q^{+} \leq Q$.

We take the cost function

where $\alpha$ and $\beta$ are given and positive, and $q^{\text{tar}}$ is a given target battery charge value.

To choose the powers we solve the QP

where $s$, $b$, $g$, and $q^{+}$ are the variables, and $\theta^{\text{user}} = {(L,S,P,q)}$ are parameters. The remaining constants, $C$, $D$, $h$, $Q$, $q^{\text{tar}}$, $\alpha$, and $\beta$, are known. We take

### Problem instances

We set $C = D = 1$, $h = 0.05$, $Q = 1$, $q^{\text{tar}} = 0.5$, and $\alpha = \beta = 0.1$. We generate 100 problem instances where $(L,S,P,q)$ is sampled uniformly from $\Theta^{\text{user}}$.

### Results

After canonicalization, there are $n = 5$ variables (including one auxiliary variable), $m = 7$ inequality constraints, and $p = 4$ parameters. We find $K = 5$ regions. Table (https://arxiv.org/html/2506.11513v2#S5.T2 "Table 2 ‣ Results. ‣ 5.2 Power management ‣ 5 Applications ‣ Automatic Generation of Explicit Quadratic Programming Solvers") shows the average solve times and binary sizes.

Table 2: Timing and binary sizes for the power management problem.

### Model predictive control

We consider the linear dynamical system \[[](https://arxiv.org/html/2506.11513v2#bib.bibx5)\]

where $z_{t} \in \text{R}^{n_{z}}$ is the state and $u_{t} \in \text{R}^{n_{u}}$ is the input, which must satisfy ${\| u_{t}\|}_{\infty} \leq 1$. The matrices $A \in \text{R}^{n_{z} \times n_{z}}$ and $B \in \text{R}^{n_{z} \times n_{u}}$ are given. We solve the model predictive control problem \[[](https://arxiv.org/html/2506.11513v2#bib.bibx40), [](https://arxiv.org/html/2506.11513v2#bib.bibx47)\]

where $z_{0},\ldots,z_{H}$ and $u_{0},\ldots,u_{H - 1}$ are the variables and $\theta^{\text{user}} = z^{\text{init}}$ is the parameter. We take $\Theta^{\text{user}} = {\lbrack{- 1},1\rbrack}^{n_{z}}$. The objective matrices $P \in \text{S}_{+ +}^{n_{z}}$, $Q \in \text{S}_{+ +}^{n_{z}}$, and $R \in \text{S}_{+ +}^{n_{u}}$ (along with $A$ and $B$) are given.

### Problem instances

We consider $n_{z} = 6$ states, $n_{u} = 1$ input, and a horizon length of $H = 5$. We construct $A$ by sampling its diagonal entries from $\mathcal{N}{}$ and its off-diagonal entries IID from $\mathcal{N}{(0,0.01)}$, before scaling the whole matrix such that $A$ has spectral radius $1$. The entries of the input matrix $B$ are sampled IID from $\mathcal{N}{(0,0.001)}$. We set the controller weights to $Q = I$ and $R = {0.1I}$, and compute $P$ as the solution to the algebraic Riccati equation associated with the infinite-horizon problem \[[](https://arxiv.org/html/2506.11513v2#bib.bibx48)\]. We generate 100 problem instances where the entries of $z^{\text{init}}$ are generated uniformly from $\Theta^{\text{user}}$.

### Results

After canonicalization, we have $n = 77$ variables (of which $36$ are auxiliary variables), $m = 10$ inequality constraints, and $p = n_{z} = 6$ parameters. We find $K = 63$ regions. Table (https://arxiv.org/html/2506.11513v2#S5.T3 "Table 3 ‣ Results. ‣ 5.3 Model predictive control ‣ 5 Applications ‣ Automatic Generation of Explicit Quadratic Programming Solvers") shows the average solve times and binary sizes.

Table 3: Timing and binary sizes for the model predictive control problem.

### Portfolio optimization

We construct a financial portfolio consisting of holdings in $N$ assets \[[](https://arxiv.org/html/2506.11513v2#bib.bibx37), [](https://arxiv.org/html/2506.11513v2#bib.bibx54), [](https://arxiv.org/html/2506.11513v2#bib.bibx59)\]. We represent the holdings relative to the total (positive) portfolio value, in terms of nonnegative weights $w \in \text{R}_{+}^{N}$, where ${\mathbf{1}^{T}w} = 1$, with $w_{i}$ being the fraction of the (positive) total portfolio value invested in asset $i$. With estimated mean annualized asset returns $\mu \in \text{R}^{N}$ \[[](https://arxiv.org/html/2506.11513v2#bib.bibx37)\], the estimated mean annualized portfolio return is $\mu^{T}w$. The variance or risk of the portfolio return is $w^{T}\Sigma w$, where $\Sigma \in \text{S}_{+ +}^{N}$ is an estimate for the covariance matrix of the annualized asset returns. Our objective is to maximize the risk-adjusted expected annualized return

where $\gamma > 0$ is the risk-aversion factor. To find the portfolio we solve the Markowitz problem \[[](https://arxiv.org/html/2506.11513v2#bib.bibx50), [BJK^+^24](https://arxiv.org/html/2506.11513v2#bib.bibx15)\]

where the portfolio weights $w \in \text{R}^{N}$ are the variable and the parameter is $\theta^{\text{user}} = \mu$ with $\Theta^{\text{user}} = {\lbrack{- 1},1\rbrack}^{N}$. This means that we expect no annualized returns beyond $\pm {100\%}$. The covariance matrix $\Sigma \in \text{S}_{+ +}^{N}$ and the risk-aversion factor $\gamma > 0$ are given.

### Problem instances

We take $N = 7$ assets. To obtain data we choose the $7$ stocks with the largest market capitalization as of January 1, 2017, listed in table (https://arxiv.org/html/2506.11513v2#S5.T4 "Table 4 ‣ Problem instances. ‣ 5.4 Portfolio optimization ‣ 5 Applications ‣ Automatic Generation of Explicit Quadratic Programming Solvers").

Facebook (now Meta)

Table 4: Stocks used in the portfolio optimization problem.

We compute $\Sigma$ by first taking the sample covariance of the $7$ assets' daily returns in the years 2017 and 2018, and then annualizing the result. We choose $\gamma = 2$. We generate 250 problem instances where $\mu$ is taken as the one-year trailing average of returns for 250 trading days in the year 2019.

### Results

We have $n = N = 7$ variables, $m = N = 7$ inequality constraints, and $p = N = 7$ parameters. We find $K = 127$ regions, only one less than the maximum $2^{m}$ potential combinations of investing in an asset or not, since the constraint ${\mathbf{1}^{T}w} = 1$ prevents $w = 0$ (not investing in any asset). Table (https://arxiv.org/html/2506.11513v2#S5.T5 "Table 5 ‣ Results. ‣ 5.4 Portfolio optimization ‣ 5 Applications ‣ Automatic Generation of Explicit Quadratic Programming Solvers") shows the average solve times and binary sizes.

Table 5: Timing and binary sizes for the portfolio optimization problem.

## Conclusions

We have added new functionality to the code generator CVXPYgen that generates an explicit solver (in C) for a parametrized convex optimization problem, when that is tractable. The user can prototype a problem in CVXPY, with code close to the math and convenient names for multiple variables and parameters, using a generic iterative solver; a change of one option in code generation will generate an explicit solver for the parametrized problem. For typical (small) problems from various application domains, our numerical experiments show the generated explicit solvers exhibit solve times at (or below) one microsecond, giving up to three orders of magnitude speedup over an iterative solver.
