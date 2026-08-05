<!-- arxiv-full-text:v1 {"arxiv_id": "2304.00290", "source": "ar5iv"} -->

## Introduction

Convex quadratic programs are fundamental in many areas of applied mathematics and engineering. They are utilized in various applications, including portfolio optimization, optimal control, state estimation, and geometry processing. Furthermore, QPs are a crucial building block of powerful optimization techniques, such as sequential quadratic programming for nonlinear programming and branch-and-bound methods for mixed integer quadratic programming. Due to their widespread use, the demand for efficient QP solvers that are both fast and reliable has increased, driven by emerging applications in areas such as optimal control, embedded systems, and signal processing.

In recent decades, significant research efforts have focused on developing efficient QP solvers. Numerous algorithms have been proposed, such as the classical active-set and interior-point methods, first-order and second-order Newton-type methods, to design QP solvers that achieve high computational efficiency and scalability. As one of the most classical QP approaches, active-set based solvers, such as qpOASES, are known for their speed in solving small to medium-sized problems and the ability to warm-start using an estimate of the active constraint set. However, they have limited scalability, struggle to exploit sparsity, and are not robust to early termination. Compared to the active-set method, interior-point based solvers, such as ECOS and QPSWIFT, can be fast for large-scale problems and robust to early termination. They can solve sparse large-scale problems efficiently using advanced linear algebra routines but are difficult to warm-start.

In contrast to classical approaches, specifically, interior-point methods, first-order solvers - including operator-splitting-based solvers like OSQP and PROXQP - can easily be warm-started, offer simplicity and tight complexity bounds. However, their convergence rates are slower than other methods. In contrast to this, the Newton-type solvers, such as the dual-Newton solver qpDUNES, can exploit sparsity and warm-start, but require restrictive assumptions, such as the QP being strongly convex and satisfying the linear independence constraint qualification (LICQ). These assumptions reduce their applicability and may cause robustness issues. Although the primal-dual Newton-type methods, such as FBRS, can relax the strong convexity requirement to the second-order sufficient condition (SOSC). However, they still require the LICQ.

Recently, hybrid methods that combine first-order and active set/interior-point methods have been the focus of increasing research attention. An example of such a method is QPNNLS. Using the proximal point algorithm, a sequence of regularized QP problems is solved which converges to the solution of the original problem. The regularized QP problems are strictly convex and are solved using a non-negative least-square based active set method. Since solving QP subproblems is computationally expensive, QPNNLS relies heavily on warm-starting to reduce computational cost. Another related method is QPALM, which is based on the Augmented Lagrangian Method. Additionally, FBstab, a proximally stabilized Fischer-Burmeister method-based solver, employs a primal-dual version of the proximal point algorithm, in which the proximal subproblems are solved by using a Newton-type method.

In this paper, we present a software contribution, a hybrid approach based QP solver, called PIQP. The underlying algorithm implemented in PIQP follows the framework proposed , which combines the interior-point method and the proximal method of multipliers (PMM). In particular, it uses one-iteration of Mohetra's predictor-corrector method to deal with the proximal subproblem combining the dual gradient update.

Section II introduces some preliminaries, including the problem formulation and the main idea of PMM. The practical algorithm implemented in PIQP is presented in Section III. Section IV elaborates the numerical implementation details of PIQP. We demonstrate the effectiveness of our solver in Section V, in which it is compared against five existing state-of-art approaches, including two commercial solvers Gurobi and Mosek, three open-source solvers OSQP, SCS, and PROXQP. All solvers are evaluated on the Maros-Mészáros benchmark problems.

Notations: we denote the set of real numbers by $\mathbb{R}$, the set of $n$-dimensional real-valued vectors by ${\mathbb{R}}^{n}$, and the set of $n \times m$-dimensional real-valued matrices by ${\mathbb{R}}^{n \times m}$. Moreover, we denote the subspace of symmetric matrices in ${\mathbb{R}}^{n \times n}$ by ${\mathbb{S}}^{n}$ and the cone of positive semi-definite matrices by ${\mathbb{S}}_{+}^{n}$. We denote the identity matrix as $I_{n} \in {\mathbb{R}}^{n \times n}$ and a vector filled with ones as $\mathbf{1}_{n} \in {\mathbb{R}}^{n}$. The $\circ$ operator indicates the element-wise multiplication of two vectors.

## Preliminaries

This section defines the problem formulation considered in PIQP and briefly reviews the proximal method of multipliers, which will be used later to design the underlying algorithm in PIQP.

### II-A Problem Formulation

PIQP considers quadratic programs in the form with primal decision variables $x \in {\mathbb{R}}^{n}$, matrices $P \in {\mathbb{S}}_{+}^{n}$, $A \in {\mathbb{R}}^{p \times n}$, $G \in {\mathbb{R}}^{m \times n}$, and vectors $c \in {\mathbb{R}}^{n}$, $b \in {\mathbb{R}}^{p}$, and $h \in {\mathbb{R}}^{m}$. To design a practical numerical solver, it is convenient to rewrite as the equivalent standard form problem where slack variables $s \in {\mathbb{R}}^{m}$ are introduced to lift the affine inequality (1c) into the equality (2c). Although introducing slack variables $s$ may compromise strong convexity when $P \succ 0$, it has distinct computational benefits. For example, it makes it particularly easy to project onto the feasible set in the context of operator splitting-based approaches, this reformulation results in an easily computable projection operator; another example is the well-known interior-point method to be discussed in the next section. In the following, we mainly work with formulation.

### II-B Proximal method of multipliers

The augmented Lagrangian of problem is defined as where variables $\lambda$ and $\nu$ are the Lagrangian multipliers of equality constraints (2b) and (2c), respectively, and $\delta > 0$ is a penalty parameter. We then introduce the iterations of the proximal method of multipliers originally proposed in as follows: where superscript ^+^ denotes the iteration update. Note that compared to the standard form for the original problem, does not add a penalty term for the slack variable as it does not contribute to the cost of the primal problem.

## Practical Algorithm

The method implemented in PIQP, following the framework proposed, deals with (4a) by applying one iteration of the interior-point method, and uses the Mehrotra predictor-corrector method to update the primal-dual iterates. To detail the algorithm, we define the log-barrier function where ${\lbrack s\rbrack}_{i}$ denotes the $i$-th element of $s$, and $\mu > 0$ is usually referred to as the barrier parameter. Replacing the constraint $s \geq 0$ in problem (4a) with the penalty term ${\sigma \cdot \Phi_{\mu}}{(s)}$ in the objective function yields at iteration $k$, where $(\xi_{k},\lambda_{k},\nu_{k})$ defines the primal-dual iterates, and $\sigma_{k} \in {(0,1\rbrack}$ is the centering parameter in the predictor-corrector method discussed below. The first-order optimality conditions of the resulting unconstrained problem can then be represented as with auxiliary variables $y \in {\mathbb{R}}^{p}$ and $z \in {\mathbb{R}}^{m}$. Introducing auxiliary variables yields a sparser linear system of equations allowing highly efficient numerical routines.

Applying Newton's method to solve results in the following linear equations with initialization $(x_{k},y_{k},z_{k},s_{k})$ and

### Remark 1

In the implementation, we can eliminate $\Deltas_{k}$. To this end, we compute the Nesterov-Todd scaling $W_{k} = {Z_{k}^{- 1}S_{k}}$ such that can be rewritten as with ${\overline{r}}_{k}^{z} = {r_{k}^{z} - {Z_{k}^{- 1}r_{k}^{s}}}$. Here, $Z_{k} \in {\mathbb{R}}^{m \times m}$ is a diagonal matrix with $z_{k}$ on its diagonal. Note that the slack direction $\Deltas_{k}$ can be reconstructed with ${\Deltas_{k}} = {Z_{k}^{- 1}{({r_{k}^{s} - {S_{k}\Deltaz_{k}}})}}$. This also ensures that $\overset{\sim}{J}{(s_{k},z_{k})}$ is symmetric.

Next, we present the three main steps of the Mehrotra predictor-corrector method:

### III-1 Prediction

solve with $\mu_{k} = 0$ and solution ${\Delta\omega_{k}^{a}} = {({\Deltax_{k}^{a}},{\Deltay_{k}^{\text{a}}},{\Deltaz_{k}^{a}},{\Deltas_{k}^{\text{a}}})}$

### III-2 Step Size and Centering Parameter

compute the primal and dual step sizes with the scaling parameter $\tau = 0.995$ chosen heuristically that ensures the iterates do not get too close to the boundary of the feasible set, and evaluate the centering parameter following with $\eta_{k} = {\left({\left({s_{k} + {\alpha_{p}^{a}\Deltas_{k}^{a}}} \right)^{\top}\left({z_{k} + {\alpha_{d}^{a}\Deltaz_{k}^{a}}} \right)} \right)/\left({\left({s_{k}^{\top}z_{k}} \right)/m} \right)}$.

### III-3 Combined Correction and Centering

compute $\mu_{k} = {\left({s_{k}^{\top}z_{k}} \right)/m}$ and solving with replacing $r_{k}^{s}$ by yields solution ${\Delta\omega_{k}^{c}} = {({\Deltax_{k}^{\text{c}}},{\Deltay_{k}^{\text{c}}},{\Deltaz_{k}^{a}},{\Deltas_{k}^{\text{c}}})}$. Then, update ${(x_{k + 1},s_{k + 1},y_{k + 1},z_{k + 1})}:=$ with step sizes Based on the aforementioned discussion, the primal-dual iterate $(\xi_{k},\lambda_{k},\nu_{k})$ is optionally updated as outlined in Algorithm 2 proposed by \[24, Section 5.1.4\]. Here, we introduce the primal-dual residual with respect to the $k$-th iteration Moreover, $\delta$ and $\rho$ are limited by $\underset{¯}{\delta}$ and $\underset{¯}{\rho}$ for numerical stability.

Now, we can summarize a predictor-corrector-based practical computational framework for the interior-point proximal method of multipliers to solve in Algorithm 1.

### Remark 2

Algorithm 1 is a practical variant of the standard interior-point proximal method of multipliers as presented in \[24, Algorithm 1\], which substitutes the correction step and regularization update in \[24, Algorithm 1\] by the Mehrotra's predictor-corrector method and Algorithm 2, respectively. Note that Algorithm 2 is a numerical heuristic to update the primal-dual iterates $(\xi_{k},\lambda_{k},\nu_{k})$ such that the convergence analysis proposed in \[24, Section 3\] cannot be rigorously established step by step. However, this heuristic leads to a more reliable and effective numerical convergence, although compared to the update in \[24, Algorithm 1\] without theoretical guarantees. Analyzing the theoretical convergence guarantee of practical Algorithm 1 is beyond the scope of this paper and will be investigated in our future work.

Initialization: choose (ξ0, s0, λ0, ν0), set δ0, ρ0 > 0. 3: Solve with rks = −Sk zk for Δ ωka; 6: Solve with rks by for Δ ωkc; 7: Compute (αpc, αdc) by and update (xk, sk, yk, zk) + (αpc Δ ξkc, αpc Δ skc, αdc Δ ykc, αdc Δ zkc); 8: Run Alg. 2 to get (ξk + 1, λk + 1, νk + 1), (δk + 1, ρk + 1). Algorithm 1 Interior-Point Proximal Method of Multipliers for Convex Quadratic Programming 11:$\delta_{k + 1}\leftarrow{\max\left\{ \delta_{k + 1},\underset{¯}{\delta} \right\}}$, $\rho_{k + 1}\leftarrow{\max\left\{ \rho_{k + 1},\underset{¯}{\rho} \right\}}$ Algorithm 2 Penalty and Estimate Updates

## Numerical Implementation

### IV-A Initialization

We initialize the primal and dual variables using the standard method proposed in by minimizing the unconstrained optimization problem which can be posed as the solution to the linear system of equations with potentially negative slack variable ${\overset{\sim}{s}}_{0} = {- {\overset{\sim}{\nu}}_{0}}$. Note that the structure is the same as for $\overset{\sim}{J}{({\overset{\sim}{s}}_{0},{\overset{\sim}{\nu}}_{0})}$; hence, we can reuse the symbolic factorization, resulting in lower computational cost.

To guarantee that $s_{0}$ and $\nu_{0}$ are in the non-negative orthant with sufficient magnitude, we calculate the conservative step sizes as and similar to, we shift initial solutions further away from the barrier based on the normalized complementarity violation resulting in the initial values for slack and inequality Lagrange multipliers $s_{0} = {{\overset{\sim}{s}}_{0} + {\Deltas_{0}}}$, $\nu_{0} = {{\overset{\sim}{\nu}}_{0} + {\Delta\nu_{0}}}$

### IV-B Termination Criteria

We adopt the same terminal criteria for convergence as in SCS v3.0. More specifically, PIQP terminates when it finds primal variables $x \in {\mathbb{R}}^{n}$, $s \in {\mathbb{R}}^{m}$, and dual variables $y \in {\mathbb{R}}^{p}$, $z \in {\mathbb{R}}^{m}$ which satisfy the conditions where $\epsilon_{abs} > 0$ and $\epsilon_{rel} \geq 0$ are the user defined absolute and relative accuracies. Condition (13a) corresponds to the primal feasibility, and (13b) to the dual feasibility, which is common in most solvers like OSQP or qpSWIFT. The condition on the duality gab (13c) is less commonly checked, but if neglected, it can result in poor solution quality. The Maros-Mészáros problem set, for example, includes problems that are solved inaccurately without the criteria on the duality gap as discussed in \[30, Section 7.2\].

### IV-C Sparse Pivot-Free LDL Factorization

The solution of the KKT system constitutes the most computationally expensive step in any interior-point method. In our work, we have chosen to employ a direct method that is particularly well-suited for use in embedded applications. Specifically, we have opted for a modified version of Tim Davis' sparse pivot-free LDL factorization with approximate minimum degree (AMD) ordering, resulting in the factorization where $\Gamma$ is the permutation matrix of the AMD ordering reducing fill-in of the lower triangular matrix $L$, and $D$ is a diagonal matrix.

To ensure that the LDL factorization of any symmetric permutation of the KKT matrix exists, it is sufficient if $K$ is quasi-definite. Although adding terms to the diagonal of through the proximal method of multipliers typically ensures that $K$ is almost certainly quasi-definite, there may be rare instances when it is not. In such cases, we slightly perturb the regularization parameters and retry the factorization. Thanks to this approach, there is no need to resort to techniques such as dynamic regularization with subsequent iterative refinement, which are employed in ECOS, resulting in less computational overhead.

The LDL factorization process consists of two phases: symbolic and numeric. During the symbolic phase, the elimination tree and the fill-in pattern of the lower triangular matrix $L$ are determined, which provides the necessary information regarding the required memory. In the numeric phase, the factorization of $K$ is performed using the previously calculated elimination tree, which fills in both $L$ and $D$. Since the structure of $\overset{\sim}{J}{(s_{k},z_{k})}$ remains constant, we can reuse the elimination tree and fill-in pattern for every subsequent solve. As a result, symbolic computation can be avoided, and all previously allocated memory can be reused. This provides a significant advantage in terms of computational efficiency, particularly in the context of optimal control, where the structure of the sequence of solved problems stays constant.

### IV-D Preconditioning

Preconditioning is a well-established technique for reducing the number of iterations for first-order methods by decreasing the condition number of the KKT system \[28, Chapter 5\]. Although commonly used for first-order methods, preconditioners can also be beneficial for interior-point methods by improving numerical stability and convergence. In our implementation, we adopt the Ruiz equilibration as our default preconditioner. This technique scales the problem data diagonally to reduce the conditioning number of the unregularized KKT conditions while being relatively cheap to compute.

### Remark 3

With the implementation of the Ruiz equilibration technique, we observed a notable improvement, achieving an average speedup of $22\%$ on the Maros-Mészáros problem set. Before preconditioning, one less problem could be solved.

### IV-E Interface and Memory Allocation

In addition to the QP formulation discussed in the paper, our implementation includes an interface for incorporating box constraints of the form $l \leq x \leq u$ with ${l,u} \in {\mathbb{R}}^{n}$. By exploiting this underlying structure, we are able to achieve computational speedups when factoring the corresponding KKT matrix.

Our QP solver, PIQP, leverages the high performance of C/C++ and the efficient vectorized matrix/vector operations provided by the popular Eigen3 library. In addition to the C/C++ interface, we provide a Python, Matlab, and an R interface, making it easy to integrate PIQP into a wide range of computational pipelines. The code structure and Python interface have been adopted from ProxSuite.

The interface of PIQP is comprised of three main routines: setup, update, and solve. During the setup routine, all necessary memory structures are set up, the problem data is preconditioned, and the symbolic factorization, including the AMD ordering, is computed. The update routine is designed for updating problem data in subsequent solves, reusing the existing memory and factorization, assuming the sparsity structure remains unchanged. Similar to the setup, the updated problem data gets preconditioned. Upon executing the algorithm, the solve routine returns the solution, as well as the status of the optimization.

In predictive optimal control applications, it is common to solve the same problem repeatedly without any changes in structure. By utilizing the update routine, the problem data can be updated while reusing the symbolic factorization and already allocated memory. This significantly speeds up subsequent solutions.

Similar to solvers like OSQP, ECOS, and PROXQP, dynamic memory is only allocated during the setup routine, ensuring that the update and solve functions remain malloc-free. This feature is particularly important for embedded systems, where memory should be allocated statically or at least only once, without any subsequent dynamic allocations.

## Numerical Examples

To demonstrate the performance of PIQP, we benchmark it against the open-source toolkits OSQP, SCS, and PROXQP, as well as commercial solvers Gurobi and Mosek. Note that we did not compare our solver with the dense solver qpOASES or conic programming solvers such as ECOS, as they do not support quadratic objectives natively.

To make the comparison fair, we enforced the same termination criteria across all solvers. Specifically, all solvers verify the primal feasibility (13a) and dual feasibility (13b). However, the duality gap (13c) is only checked by PIQP, SCS, and PROXQP. As a result, other solvers may report an optimal solution that fails to satisfy the duality gap condition and may require more time or even fail to find a solution that meets our termination criteria. Thus, it is important to note that the reported results for these solvers may be overly optimistic. For example, Mosek would fail on $75\%$ of problems if we check the termination criteria of the solution.

All benchmarks are run on a workstation with an AMD Ryzen Threadripper 3990X 4.3 GHz CPU. Gurobi and Mosek were limited to a single thread, and all solvers were subject to a $1000$ second time limit. We use an adapted benchmark framework from OSQP.

### V-A Maros-Mészáros problems

We consider the standard Maros-Mészáros problem set, comprised out of $138$ hard QP problems. Most problems are very sparse, and a certain subset is numerically extremely ill-conditioned.

Our implementation is based on the Python interface of all solvers. Moreover, we only use the internally measured times reported by the solver. This includes setup and solution time.

We conduct two sets of experiments to evaluate the performance of our QP solver. In the first scenario, we aim to find solutions with low accuracy, setting $\epsilon_{abs} = 10^{- 3}$ and $\epsilon_{rel} = 10^{- 4}$. In the second scenario, we target highly accurate solutions, setting $\epsilon_{abs} = 10^{- 8}$ and $\epsilon_{rel} = 10^{- 9}$.

Table I summarizes the failure rates of the solvers for the different accuracy settings. Compared to the other solvers, our solver, PIQP, demonstrates remarkable robustness, successfully solving all problems with low accuracy settings and failing to solve only a single problem with high accuracy settings.

TABLE I: Failure rates on the Maros-Mészáros problem set We provide the individual solve times for each problem in the Maros-Meszaros problem set for high accuracy settings in Figure 1. The problems are sorted by PIQP solve time, highlighting the speed of our solver relative to the others. Notably, our solver is almost always the fastest for most problems. These results highlight the advantages of interior-point methods in high-accuracy settings, where they outperform most first-order methods.

Figure 1: Solve times for high accuracy settings for individual problems in the Maros-Mészáros problem set, ordered by PIQP solve time. The lowest point in each column corresponds to the fastest solver.

We include the Dolan-Moré performance profiles for the high accuracy settings in Figure 2. The x-axis of the graphs shows the solve time normalized by the fastest solver, with a performance ratio of one indicating that the solver was the fastest and a performance ratio of ten indicating that the solver was ten times slower than the fastest solver for a particular problem. The y-axis of the graphs shows the ratio of problems solved. For instance, PIQP was the fastest solver for 65% of the problems and took at most five times longer for 96% of the problems.

Figure 2: Performance profiles on the Maros-Mészáros problem set for high accuracy settings.
