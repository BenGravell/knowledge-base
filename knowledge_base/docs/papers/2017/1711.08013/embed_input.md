<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

OSQP: An Operator Splitting Solver for Quadratic Programs

Topics include Quadratic programming, Convex optimization, Operator splitting, Alternating-direction method of multipliers, First-order optimization, Embedded optimization, Model predictive control, Warm-starting, Factorization caching, Infeasibility detection, Sparse linear algebra.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces OSQP, a general-purpose convex quadratic programming solver built around an ADMM-style operator splitting that repeatedly solves a quasi-definite linear system with reusable structure. The paper is especially useful for embedded and repeated-solve settings because it combines robustness to semidefinite objectives and dependent constraints with warm starts, factorization caching, optional division-free iterations, infeasibility detection, and a compact open-source C implementation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a general-purpose solver for convex quadratic programs based on the alternating direction method of multipliers, employing a novel operator splitting technique that requires the solution of a quasi-definite linear system with the same coefficient matrix at almost every iteration. Our algorithm is very robust, placing no requirements on the problem data such as positive definiteness of the objective function or linear independence of the constraint functions. It can be configured to be division-free once an initial matrix factorization is carried out, making it suitable for real-time applications in embedded systems. In addition, our technique is the first operator splitting method for quadratic programs able to reliably detect primal and dual infeasible problems from the algorithm iterates. The method also supports factorization caching and warm starting, making it particularly efficient when solving parametrized problems arising in finance, control, and machine learning. Our open-source C implementation OSQP has a small footprint, is library-free, and has been extensively tested on many problem instances from a wide variety of application areas. It is typically ten times faster than competing interior-point methods, and sometimes much more when factorization caching or warm start is used.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

OSQP has already shown a large impact with tens of thousands of users both in academia and in large corporations.

<!-- chunk {"id": "body-0005", "role": "body", "section": "The problem", "weight": 1.0} -->

Consider the following optimization problem \mbox{minimize} & (1/2) x^\tpose P x + q^\tpose x \\\mbox{subject to} & A x \in \mathcal{C}, where $x\in \reals^{n}$ is the decision variable. The objective function is defined by a positive semidefinite matrix $P \in \symm_{+}^{n}$ and a vector $q \in \reals^{n}$, and the constraints by a matrix $A\in \reals^{m \times n}$ and a nonempty, closed and convex set $\mathcal{C} \subseteq \reals^m$. We will refer to it as general (convex) QP.

<!-- chunk {"id": "body-0006", "role": "body", "section": "The problem", "weight": 1.0} -->

$\mathcal{C}$ takes the form $$\mathcal{C} = [l,u] \eqdef \left\{z \in \reals^{m} \mid l_i\le z_i \le u_i, \,\, i=1,\dots,m\right\},$$ with ${l_i \in \lbrace-\infty\rbrace\cup\reals}$ and ${u_i \in \reals\cup\lbrace+\infty\rbrace}$, we can write problem[pb:main] as \mbox{minimize} & (1/2) x^\tpose P x + q^\tpose x \\\mbox{subject to} & l \leq A x \leq u, which we will refer to as a QPquadratic program (QP). Linear equality constraints can be encoded in this way by setting $l_i = u_i$ for some or all of the elements in $(l,u)$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "The problem", "weight": 1.0} -->

Note that any LP can be written in this form by setting $P=0$. We will characterize the size of[pb:qp] with the tuple $(n, m, N)$ where $N$ is the sum of the number of nonzero entries in $P$ and $A$ $N \eqdef \nnz(P) + \nnz(A)$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "The problem", "weight": 1.0} -->

Applications. Optimization problems of the form[pb:main] arise in a huge variety of applications in engineering, finance, operations research and many other fields. Applications in machine learning include support vector machines (SVM)[Cortes:1995], Lasso[Tibshirani:1996,Candes:2008] and Huber fitting[Huber:1964,Huber:1981]. Financial applications of[pb:main] include portfolio optimization[cornuejols2006,JOFI:JOFI1525,OPT-001,OPT-023][boyd2004convex]. In the field of control engineering, MPC[Rawlings:2009,GARCIA1989335] and MHE[Allgower1999] techniques require the solution of a QP at each time instant. Several signal processing problems also fall into the same class[boyd2004convex]. In addition, the numerical solution of QP subproblems is an essential component in nonconvex optimization methods such as SQP and mixed-integer optimization using branch-and-bound algorithms[Belotti:2013dva,].

<!-- chunk {"id": "body-0009", "role": "body", "section": "Solution methods", "weight": 1.0} -->

Convex QP have been studied since the 1950s[MargueriteWolfe1956], following from the seminal work on LPs started by Kantorovich[Kantorovich:1939]. Several solution methods for both LP and QPhave been proposed and improved upon throughout the years.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Solution methods", "weight": 1.0} -->

Active-set methods were the first algorithms popularized as solution methods for QP [Wolfe1959], and were obtained from an extension of Dantzig's simplex method for solving LP[dantzig1963]. Active-set algorithms select an active-set (, a set of binding constraints) and then iteratively adapt it by adding and dropping constraints from the index of active ones. New active constraints are added based on the cost function gradient and the current dual variables. Active-set methods for QP differ from the simplex method for LP because the iterates are not necessarily vertices of the feasible region. These methods can easily be warm started to reduce the number of active-set recalculations required. However, the major drawback of active-set methods is that the worst-case complexity grows exponentially with the number of constraints, since it may be necessary to investigate all possible active-sets before reaching the optimal one[KleeMinty:1970].

<!-- chunk {"id": "body-0011", "role": "body", "section": "Solution methods", "weight": 1.0} -->

Modern implementations of active-set methods for the solution of QP can be found in many commercial solvers, such as MOSEK[mosek] and GUROBI[gurobi], and in the open-source solver qpOASES[Ferreau:2014].

<!-- chunk {"id": "body-0012", "role": "body", "section": "Solution methods", "weight": 1.0} -->

Interior-point algorithms gained popularity in the 1980s as a method for solving LP in polynomial time[Karmarkar1984,Gill1986]. In the 90s these techniques were extended to general convex optimization problems, including QP[doi:10.1137/1.9781611970791]. Interior-point methods model the problem constraints as parametrized penalty functions, also referred to as barrier functions. At each iteration an unconstrained optimization problem is solved for varying barrier function parameters until the optimum is achieved; see[boyd2004convex] and for details. Primal-dual interior-point methods, in particular the Mehrotra predictor-corrector[doi:10.1137/0802028] method, became the algorithms of choice for practical implementation[doi:10.1137/1.9781611971453] because of their good performance across a wide range of problems. However, interior-point methods are not easily warm started and do not scale well for very large problems.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Solution methods", "weight": 1.0} -->

Interior-point methods are currently the default algorithms in the commercial solvers MOSEK[mosek], GUROBI[gurobi] and CVXGEN[Mattingley:2012] and in the open-source solver OOQP[Gertz:2003:OSQ:641876.641880].

<!-- chunk {"id": "body-0014", "role": "body", "section": "Solution methods", "weight": 1.0} -->

First-order optimization methods for solving quadratic programs date to the 1950s[MargueriteWolfe1956]. These methods iteratively compute an optimal solution using only first-order information about the cost function. Operator splitting techniques such as the Douglas-Rachford splitting[doi:10.1137/0716071,10.2307/1993056]are a particular class of first-order methods which model the optimization problem as the problem of finding a zero of the sum of monotone operators.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Solution methods", "weight": 1.0} -->

In recent years, the operator splitting method known as the ADMM[GABAY197617,Glowinski1975] has received particular attention because of its very good practical convergence behavior; see[boyd2011distributed] for a survey. ADMM can be seen as a variant of the classical alternating projections algorithm[doi:10.1137/S0036144593251710] for finding a point in the intersection of two convex sets, and can also be shown to be equivalent to the Douglas-Rachford splitting[GABAY1983299]. ADMM has been shown to reliably provide modest accuracy solutions to QP in a relatively small number of computationally inexpensive iterations. It is therefore well suited to applications such as embedded optimization or large-scale optimization, wherein high accuracy solutions are typically not required due to noise in the data and arbitrariness of the cost function. ADMM steps are computationally very cheap and simple to implement, and thus ideal for embedded processors with limited computing resources such as those found in embedded control systems[6882832,6422363,SYS-008].

<!-- chunk {"id": "body-0016", "role": "body", "section": "Solution methods", "weight": 1.0} -->

ADMM is also compatible with distributed optimization architectures enabling the solution of very large-scale problems[boyd2011distributed].

<!-- chunk {"id": "body-0017", "role": "body", "section": "Solution methods", "weight": 1.0} -->

A drawback of first-order methods is that they are typically unable to detect primal and/or dual infeasibility.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Solution methods", "weight": 1.0} -->

In order to address this shortcoming, a homogeneous self-dual embedding has been proposed in conjunction with ADMM for solving conic optimization problems and implemented in the open-source solver SCS[ocpb:16]. Although every QP can be reformulated as a conic program, this reformulation is not efficient from a computational point of view. A further drawback of ADMM is that number of iterations required to converge is highly dependent on the problem data and on the user's choice of the algorithm's step-size parameters. Despite some recent theoretical results[7465685,BanjacLinearConvergence], it remains unclear how to select those parameters to optimize the algorithm convergence rate. For this reason, even though there are several benefits in using ADMM techniques for solving optimization problems, there exists no reliable general-purpose QPsolver based on operator splitting methods.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Our approach", "weight": 1.0} -->

In this work we present a new general-purpose QP solver based on ADMM that is able to provide high accuracy solutions. The proposed algorithm is based on a novel splitting requiring the solution of a quasi-definite linear system that is always solvable for any choice of problem data. We therefore impose no constraints such as strict convexity of the cost function or linear independence of the constraints. Since the linear system's matrix coefficients remain the same at every iteration when $\rho$ is fixed, our algorithm requires only a single factorization to solve the QP [pb:qp]. Once this initial factorization is computed, we can fix the linear system matrix coefficients to make the algorithm division-free. If we allow divisions, then we can make occasional updates to the term $\rho$ in this linear system to improve our algorithm's convergence. We find that our algorithm typically updates these coefficients very few times $1$ or $2$in our experiments. In contrast to other first-order methods, our approach is able to return primal and dual solutions when the problem is solvable or to provide certificates of primal and dual infeasibility without resorting to the homogeneous self-dual embedding.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Our approach", "weight": 1.0} -->

To obtain high accuracy solutions, we perform solution polishing on the iterates obtained from ADMM. By identifying the active constraints from the final dual variable iterates, we construct an ancillary equality-constrained QP whose solution is equivalent to that of the original QP[pb:main]. This ancillary problem is then solved by computing the solution of a single linear system of typically much lower dimensions than the one solved during the ADMMiterations. If we identify the active constraints correctly, then the resulting solution of our method has accuracy equal to or even better than interior-point methods.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Our approach", "weight": 1.0} -->

Our algorithm can be efficiently warm started to reduce the number of iterations. Moreover, if the problem matrices do not change then the quasi-definite system factorization can be reused across multiple solves greatly improving the computation time. This feature is particularly useful when solving multiple instances of parametric QP where only a few elements of the problem data change. Examples illustrating the effectiveness of the proposed algorithm in parametric programs arising in embedded applications appear in[embedded\_osqp:2017].

<!-- chunk {"id": "body-0022", "role": "body", "section": "Our approach", "weight": 1.0} -->

We implemented our method in the open-source Operator Splitting Quadratic Program (OSQP) solver. OSQP is written in C and can be compiled to be library free. OSQP is robust against noisy and unreliable problem data, has a very small code footprint, and is suitable for both embedded and large-scale applications. We have extensively tested our code and carefully tuned its parameters by solving millions of QP. We benchmarked our solver against state-of-the-art interior-point and active-set solvers over a benchmark library of 1400 problems from 7 different classes and over the hard QP Maros-Meszaros test set[maros1999]. Numerical results show that our algorithm is able to provide up to an order of magnitude computational time improvements over existing commercial and open-source solvers in a wide variety of applications. We also showed further time reductions from warm starting and factorization caching.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Optimality conditions", "weight": 1.0} -->

We will find it convenient to rewrite problem [pb:main] by introducing an additional decision variable $z\in\reals^m$, to obtain the equivalent problem \mbox{minimize} & (1/2) x^\tpose P x + q^\tpose x \\We can write the optimality conditions of problem[pb:equivalent] as[osqp-convergence][rockafellar1998variational] & z \in \mathcal{C}, \quad y\in N_{\mathcal{C}}(z), where $y\in \reals^{m}$ is the Lagrange multiplier associated with the constraint $Ax=z$ and $N_{\mathcal{C}}(z)$ denotes the normal cone of $\mathcal{C}$ at $z$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Optimality conditions", "weight": 1.0} -->

If there exist $x \in \reals^n$, $z \in \reals^{m}$ and $y \in \reals^{m}$ that satisfy the conditions above, then we say that $(x,z)$ is a primal and $y$ is a dual solution to problem[pb:equivalent]. We define the primal and dual residuals of problem[pb:main] as r_{\rm dual} &\eqdef Px + q + A^\tpose y.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Optimality conditions", "weight": 1.0} -->

In case of QP of the form[pb:qp], condition [eq:separating\_hyperplane] reduces to $$l \le z \le u, \qquad y_{+}^\tpose (z - u) = 0,\qquad y_{-}^\tpose (z - l) = 0,$$ where $y_{+} \eqdef \max(y, 0)$ and $y_{-} \eqdef \min(y, 0)$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Certificates of primal and dual infeasibility", "weight": 1.0} -->

theorem of strong alternatives[boyd2004convex],[osqp-convergence], exactly one of the following sets is nonempty \mathcal{P} &= \left\{x \in \reals^{n}\mid Ax\in\mathcal{C} \right\}, \\\mathcal{D} &= \left\{y \in \reals^{m} \mid A^\tpose y = 0, \quad S_\mathcal{C}(y)<0 \right\}, where $S_\mathcal{C}$ is the support function of $\mathcal{C}$, provided that some type of constraint qualification holds[boyd2004convex]. In other words, any variable $y \in \mathcal{D}$ serves as a certificate that problem[pb:main]is primal infeasible.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Certificates of primal and dual infeasibility", "weight": 1.0} -->

In case $\mathcal{C}=[l,u]$, certifying primal infeasibility of[pb:qp] amounts to finding a vector $y\in\reals^m$ such that $$A^\tpose y = 0, \quad u^\tpose y_{+} + l^\tpose y_{-} < 0.$$ Similarly, it can be shown that a vector $x\in\reals^n$ satisfying $$Px = 0, \quad q^\tpose x < 0, \quad (Ax)_i \begin{aligned} =0 &\quad l_i,u_i\in\reals \\\geq 0 &\quad u_i = +\infty, \,l_i \in \reals \\\leq 0 &\quad l_i = -\infty, \,u_i \in \reals is a certificate of dual infeasibility for problem[pb:qp]; see [osqp-convergence]for more details.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Solving the linear system", "weight": 1.0} -->

The optimality conditions for this equality constrained QP are P\tilde{x}^{k+1} + q + \sigma(\tilde{x}^{k+1} - x^k) + A^\tpose \nu^{k+1} &= 0, \\where $\nu^{k+1} \in \reals^m$ is the Lagrange multiplier associated with the constraint $Ax=z$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Solving the linear system", "weight": 1.0} -->

By eliminating the variable $\tilde{z}^{k+1}$ from[admm\_step1:eq2], the above linear system reduces to &\begin{bmatrix} P + \sigma I & A^\tpose \\ A & -\rho^{-1}I \end{bmatrix} \begin{bmatrix} \tilde{x}^{k+1} \\ \nu^{k+1} \end{bmatrix}= \begin{bmatrix}\sigma x^{k} - q \\ z^{k} - \rho^{-1} y^k \end{bmatrix}, with $\tilde{z}^{k+1}$ recoverable as We will refer to the coefficient matrix in[eq:kkt] as the KKT matrix.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Solving the linear system", "weight": 1.0} -->

This matrix always has full rank thanks to the positive parameters $\sigma$ and $\rho$ introduced in our splitting, so[eq:kkt] always has a unique solution for any matrices $P\in\symm_+^n$ and $A\in\reals^{m\times n}$. In other words, we do not impose any additional assumptions on the problem data such as strong convexity of the objective function or linear independence of the constraints as was done in[6892987,raghunathan2014cdc,raghunathan2014].

<!-- chunk {"id": "body-0031", "role": "body", "section": "Solving the linear system", "weight": 1.0} -->

A direct method for solving the linear system [eq:kkt] computes its solution by first factoring the KKT matrix and then performing forward and backward substitution. Since the KKT matrix remains the same for every iteration of ADMM, we only need to perform the factorization once prior to the first iteration and cache the factors so that we can reuse them in subsequent iterations. This approach is very efficient when the factorization cost is considerably higher than the cost of forward and backward substitutions, so that each iteration is computed quickly. Note that if $\rho$ or $\sigma$change, the KKT matrix needs to be factored again.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Solving the linear system", "weight": 1.0} -->

Our particular choice of splitting results in a KKT matrix that is quasi-definite it can be written as a 2-by-2 block-symmetric matrix where the $$-block is positive definite, and the $$-block is negative definite. It therefore always has a well defined $LDL^\tpose$ factorization, with$L$ being a lower triangular matrix with unit diagonal elements and$D$ a diagonal matrix with nonzero diagonal elements[vanderbei1995symmetric]. Note that once the factorization is carried out, computing the solution of[eq:kkt] can be made division-free by storing $D^{-1}$ instead of $D$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Solving the linear system", "weight": 1.0} -->

When the KKT matrix is sparse and quasi-definite, efficient algorithms can be used for computing a suitable permutation matrix $P$ for which the factorization of $PKP^\tpose$ results in a sparse factor$L$[Amestoy:2004,davis2006direct] without regard for the actual nonzero values appearing in the KKT matrix. The $LDL^\tpose$ factorization consists of two steps. In the first step we compute the sparsity pattern of the factor $L$. This step is referred to as the symbolic factorization and requires only the sparsity pattern of the KKT matrix. In the second step, referred to as the numerical factorization, we determine the values of nonzero elements in$L$ and$D$. Note that we do not need to update the symbolic factorization if the nonzero entries of the KKT matrix change but the sparsity pattern remains the same.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Solving the linear system", "weight": 1.0} -->

With large-scale QP, factoring linear system[eq:kkt] might be prohibitive. In these cases it might be more convenient to use an indirect method by solving instead the linear system $$\left(P + \sigma I + \rho A^\tpose A \right)\tilde{x}^{k+1} = \sigma x^{k} - q + A^\tpose (\rho z^{k} - y^{k})$$ obtained by eliminating$\nu^{k+1}$ from[eq:kkt]. We then compute $\tilde{z}^{k+1}$ as $\tilde{z}^{k+1} = A\tilde{x}^{k+1}$. Note that the coefficient matrix in the above linear system is always positive definite. The linear system can therefore be solved with an iterative scheme such as the conjugate gradient method[Golub:1996:MC:248979,]. When the linear system is solved up to some predefined accuracy, we terminate the method.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Solving the linear system", "weight": 1.0} -->

We can also warm start the method using the linear system solution at the previous iteration of ADMM to speed up its convergence. In contrast to direct methods, the complexity of indirect methods does not change if we update $\rho$ and $\sigma$since there is no factorization required. This allows for more updates to take place without any overhead.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Final algorithm", "weight": 1.0} -->

ADMM iterations according to the previous discussion, we obtain Algorithm[alg:osqp\_algorithm]. Steps[alg:update\_z\_tikde],[alg:update\_x],[alg:update\_z] and[alg:update\_y] of Algorithm[alg:osqp\_algorithm] are very easy to evaluate since they involve only vector addition and subtraction, scalar-vector multiplication and projection onto a box. Moreover, they are component-wise separable and can be easily parallelized. The most computationally expensive part is solving the linear system in Step[alg:solve\_lin\_sys], which can be performed as discussed in Section[sec:solving\_linear\_system].

<!-- chunk {"id": "body-0037", "role": "body", "section": "Convergence and infeasibility detection", "weight": 1.0} -->

We show in this section that the proposed algorithm generates a sequence of iterates $(x^{k},z^{k},y^{k})$ that in the limit satisfy the optimality conditions[eq:prim\_feas][eq:separating\_hyperplane] when problem[pb:main]is solvable, or provides a certificate of primal or dual infeasibility otherwise.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Convergence and infeasibility detection", "weight": 1.0} -->

If we denote the argument of the projection operator in step [alg:update\_z] of Algorithm[alg:osqp\_algorithm] by $v^{k+1}$, then we can express $z^k$ and $y^k$ as \quad\text{and}\quad y^{k} = \rho\left(v^{k} - \Pi(v^{k}) \right).$$ Observe from [zy-update] that iterates $z^{k}$ and $y^{k}$ satisfy optimality condition[eq:separating\_hyperplane] for all $k>0$ by construction[bauschke2011convex]. Therefore, it only remains to show that optimality conditions [eq:prim\_feas][eq:dual\_feas]are satisfied in the limit.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Convergence and infeasibility detection", "weight": 1.0} -->

[osqp-convergence], if problem[pb:qp] is solvable, then Algorithm[alg:osqp\_algorithm] produces a convergent sequence of iterates $(x^k,z^k,y^k)$ so that \lim_{k\to\infty} r_{\rm prim}^k = 0, \\\lim_{k\to\infty} r_{\rm dual}^k = 0, where $r_{\rm prim}^k$ and $r_{\rm dual}^k$ correspond to the residuals defined in[eq:res\_prim] and[eq:res\_dual]respectively.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Convergence and infeasibility detection", "weight": 1.0} -->

On the other hand, if problem [pb:qp] is primal and/or dual infeasible, then the sequence of iterates $(x^k,z^k,y^k)$ generated by Algorithm[alg:osqp\_algorithm] does not converge. However, the sequence $$(\delta x^{k}, \delta z^{k}, \delta y^{k}) \eqdef (x^{k} - x^{k-1}, z^{k} - z^{k-1}, y^{k} - y^{k-1})$$ always converges and can be used to certify infeasibility of the problem.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Convergence and infeasibility detection", "weight": 1.0} -->

According to [osqp-convergence], if the problem is primal infeasible, then $\delta y \eqdef \lim_{k\to\infty} \delta y^{k}$ satisfies conditions[eq:prim-infeas-linear], whereas $\delta x \eqdef \lim_{k\to\infty} \delta x^{k}$ satisfies conditions[eq:dual-infeas-linear]if it is dual infeasible.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Termination criteria", "weight": 1.0} -->

We can define termination criteria for Algorithm [alg:osqp\_algorithm]so that the iterations stop when either a primal-dual solution or a certificate of primal or dual infeasibility is found up to some predefined accuracy.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Solution polishing", "weight": 1.0} -->

Operator splitting methods are typically used for obtaining solution of an optimization problem with a low or medium accuracy. However, even if a solution is not very accurate we can often guess which constraints are active from an approximate primal-dual solution. When dealing with QP of the form[pb:qp], we can obtain high accuracy solutions from the final ADMMiterates by solving one additional system of equations.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Solution polishing", "weight": 1.0} -->

Given a dual solution $y$ of the problem, we define the sets of lower- and upper-active constraints \mathcal{L} &\eqdef \left\lbrace i \in \{ 1,\dots,m\} \mid y_i < 0 \right\rbrace, \\\mathcal{U} &\eqdef \left\lbrace i \in \{ 1,\dots,m\} \mid y_i > 0 \right\rbrace.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Solution polishing", "weight": 1.0} -->

According to[eq:compl\_slack] we have that $z_\mathcal{L}=l_\mathcal{L}$ and $z_\mathcal{U}=u_\mathcal{U}$, where $l_{\mathcal{L}}$ denotes the vector composed of elements of $l$ corresponding to the indices in $\mathcal{L}$. Similarly, we will denote by $A_{\mathcal{L}}$ the matrix composed of rows of $A$ corresponding to the indices in $\mathcal{L}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Solution polishing", "weight": 1.0} -->

If the sets of active constraints are known a priori, then a primal-dual solution $(x,y,z)$ can be found by solving the following linear system &\begin{bmatrix} P & A_{\mathcal{L}}^\tpose & A_{\mathcal{U}}^\tpose \\ A_{\mathcal{L}} & & \\ A_{\mathcal{U}} & & \end{bmatrix} \begin{bmatrix} x \\ y_{\mathcal{L}} \\ y_{\mathcal{U}} \end{bmatrix} = \begin{bmatrix} -q \\ l_{\mathcal{L}} \\ u_{\mathcal{U}}\end{bmatrix}, \\&y_i = 0, \quad i \notin(\mathcal{L}\cup\mathcal{U}), \\We can then apply the aforementioned procedure to obtain a candidate solution If $(x,y,z)$ satisfies the optimality

<!-- chunk {"id": "body-0047", "role": "body", "section": "Solution polishing", "weight": 1.0} -->

conditions[eq:prim\_feas][eq:separating\_hyperplane], then our guess is correct and $(x,y,z)$ is a primal-dual solution of problem[pb:equivalent].

<!-- chunk {"id": "body-0048", "role": "body", "section": "Solution polishing", "weight": 1.0} -->

This approach is referred to as solution polishing. Note that the dimension of the linear system[eq:kkt\_polish] is usually much smaller than the KKT system in Section[sec:solving\_linear\_system] because the number of active constraints at optimality is less than or equal to $n$ for non-degenerate QP.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Solution polishing", "weight": 1.0} -->

However, the linear system [eq:kkt\_polish] is not necessarily solvable even if the sets of active constraints $\mathcal{L}$ and $\mathcal{U}$ have been correctly identified. This can happen if the solution is degenerate if it has one or more redundant active constraints.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Solution polishing", "weight": 1.0} -->

Since the regularized matrix in[eq:kkt\_polish\_reg] is quasi-definite, the linear system[eq:kkt\_polish\_reg]is always solvable.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Solution polishing", "weight": 1.0} -->

By using regularization, we actually solve a perturbed linear system and thus introduce a small error to the polished solution. $K$ and $(K+\Delta K)$ the coefficient matrices in[eq:kkt\_polish] and[eq:kkt\_polish\_reg], respectively, then we can represent the two linear systems as $Kt = g$ and $(K+\Delta K)\hat{t} = g$. To compensate for this error, we apply an iterative refinement procedure[Wilkinson:1963] we iteratively solve $$(K+\Delta K) \Delta \hat{t}^k = g - K \hat{t}^k$$ and update $\hat{t}^{k+1} \eqdef \hat{t}^k + \Delta \hat{t}^k$. The sequence $\lbrace \hat{t}^k\rbrace$ converges to the true solution $t$, provided that it exists.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Solution polishing", "weight": 1.0} -->

Observe that, compared to solving the linear system[eq:kkt\_polish\_reg], iterative refinement requires only a backward- and a forward-solve, and does not require another matrix factorization. Since the iterative refinement iterations converge very quickly in practice, we just run them for a fixed number of passes without imposing any termination condition to satisfy. Note that this is the same strategy used in commercial linear system solvers using iterative refinement[intel2017].

<!-- chunk {"id": "body-0053", "role": "body", "section": "Preconditioning and parameter selection", "weight": 1.0} -->

A known weakness of first-order methods is their inability to deal effectively with ill-conditioned problems, and their convergence rate can vary significantly when data are badly scaled. In this section we describe how to precondition the data and choose the optimal parameters to speed up the convergence of our algorithm.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Preconditioning", "weight": 1.0} -->

Preconditioning is a common heuristic aiming to reduce the number of iterations in first-order methods The optimal choice of preconditioners has been studied for at least two decades and remains an active area of research[doi:10.1137/1.9781611970944],[doi:10.1137/1.9781611970937]. For example, the optimal diagonal preconditioner required to minimize the condition number of a matrix can be found exactly by solving a semidefinite program[doi:10.1137/1.9781611970777]. However, this computation is typically more complicated than solving the original QP, and is therefore unlikely to be worth the effort since preconditioning is only a heuristic to minimize the number of iterations.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Preconditioning", "weight": 1.0} -->

In order to keep the preconditioning procedure simple, we instead make use of a simple heuristic called matrix equilibration[bradley2010algorithms,TJ:14,fougnerboyd2017,diamond2017]. Our goal is to rescale the problem data to reduce the condition number of the symmetric matrix $M\in \symm^{n+m}$ representing the problem data, defined as $$M \eqdef \begin{bmatrix} P & A^\tpose\\ A & 0 In particular, we use symmetric matrix equilibration by computing the diagonal matrix $S \in \symm^{n+m}_{++}$ to decrease the condition number of $S M S$. We can write matrix$S$ as $$S = \begin{bmatrix} D & \\ & E \end{bmatrix},$$ where $D \in \symm^n_{++}$ and $E \in \symm^m_{++}$ are both diagonal.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Preconditioning", "weight": 1.0} -->

In addition, we would like to normalize the cost function to prevent the dual variables from being too large. We can achieve this by multiplying the cost function by the scalar $c > 0$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Preconditioning", "weight": 1.0} -->

Note that when $\mathcal{C}=[l,u]$ the Euclidean projection onto $\bar{\mathcal{C}}=[El,Eu]$ is as easy to evaluate as the projection onto$\mathcal{C}$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Preconditioning", "weight": 1.0} -->

The main idea of the equilibration procedure is to scale the rows of matrix $M$ so that they all have equal $\ell_p$ norm. It is possible to show that finding such a scaling matrix $S$ can be cast as a convex optimization problem. However, it is computationally more convenient to solve this problem with heuristic iterative methods, rather than continuous optimization algorithms such as interior-point methods. We refer the reader to[bradley2010algorithms]for more details on matrix equilibration.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Preconditioning", "weight": 1.0} -->

In this work we apply a variation of the Ruiz equilibration[ruiz2001]. This technique was originally proposed to equilibrate square matrices showing fast linear convergence superior to other methods such as the Sinkhorn-Knopp equilibration[sinkhorn1967concerning]. Ruiz equilibration converges in few tens of iterations even in cases when Sinkhorn-Knopp equilibration takes thousands of iterations[knightruizucar2014]. The steps are outlined in Algorithm[alg:ruiz\_equil] and differ from the original Ruiz algorithm by adding a cost scaling step that takes into account very large values of the cost.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Preconditioning", "weight": 1.0} -->

\|\bar{q}\|_{\infty}\rbrace$ Cost scaling $\bar{P} \gets \gamma \bar{P}, \bar{q} \gets \gamma \bar{q}$ $S \gets \diag(\delta) S, c \gets \gamma c$ The first part is the usual Ruiz equilibration step.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Preconditioning", "weight": 1.0} -->

Since $M$ is symmetric, we focus only on the columns $M_{i}$ and apply the scaling to both sides of $M$. At each iteration, we compute the $\infty$-norm of each column and normalize that column by the inverse of its square root. The second part is a cost scaling step. The scalar $\gamma$ is the current cost normalization coefficient taking into account the maximum between the average norm of the columns of $\bar{P}$ and the norm of $\bar{q}$. We normalize problem data $\bar{P}$, $\bar{q}$, $\bar{A}$, $\bar{l}$, $\bar{u}$ in place at each iteration using the current values of $\delta$ and $\gamma$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Parameter selection", "weight": 1.0} -->

The choice of parameters $(\rho,\sigma,\alpha)$ in Algorithm[alg:osqp\_algorithm] is a key factor in determining the number of iterations required to find an optimal solution. Unfortunately, it is still an open research question how to select the optimal ADMM parameters, see[6892987,Nishihara:2015,7465685]. After extensive numerical testing on millions of problem instances and a wide range of dimensions, we chose the algorithm parameters as follows for QP.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Parameter selection", "weight": 1.0} -->

Choosing $\sigma$ and $\alpha$. The parameter$\sigma$ is a regularization term which is used to ensure that a unique solution of[eq:ADMM\_iter1] will always exist, even when $P$ has one or more zero eigenvalues. After scaling $P$ in order to minimize its condition number, we choose $\sigma$ as small as possible to preserve numerical stability without slowing down the algorithm. We set the default value as $\sigma = 10^{-6}$. The relaxation parameter$\alpha$ in the range $[1.5, 1.8]$ has empirically shown to improve the convergence rate[Eckstein1994,doi:10.1287/ijoc.10.2.218]. In the proposed method, we set the default value of$\alpha=1.6$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Parameter selection", "weight": 1.0} -->

The most crucial parameter is the step-size Numerical testing showed that having different values of $\rho$ for different constraints, can greatly improve the performance. For this reason, without altering the algorithm steps, we chose $\rho\in\symm_{++}^{m}$ being a positive definite diagonal matrix with different elements $\rho_i$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Parameter selection", "weight": 1.0} -->

QP, if we know the active and inactive constraints, then we can rewrite it simply as an equality constrained QP. In this case the optimal $\rho$ is defined as $\rho_i=\infty$ for the active constraints and $\rho_i=0$ for the inactive constraints, therefore reducing the linear system[eq:kkt] to the optimality conditions of the equivalent equality constrained QP (after setting $\sigma = 0$). Unfortunately, it is impossible to know a priori whether any given constraint is active or inactive at optimality, so we must instead adopt some heuristics. We define $\rho$ as follows $$\rho = \diag(\rho_1, \dots,\rho_m),\qquad \rho_i = \begin{dcases}\bar{\rho} & l_i\neq u_i\\10^3\bar{\rho} & l_i = u_i,\end{dcases}$$ where $\bar{\rho} > 0$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Parameter selection", "weight": 1.0} -->

In this way we assign a high value to the step-size related to the equality constraints since they will be active at the optimum. Having a fixed value of $\bar{\rho}$ cannot provide fast convergence for different kind of problems since the optimal solution and the active constraints vary greatly. To compensate for this issue, we adopt an adaptive scheme which updates $\bar{\rho}$ during the iterations based on the ratio between primal and dual residuals. The idea of introducing feedback in the algorithm steps makes ADMM more robust to bad scaling in the data; see[he2000,boyd2011distributed,wohlberg2017].

<!-- chunk {"id": "body-0067", "role": "body", "section": "Parameter selection", "weight": 1.0} -->

\|_{\infty} \rbrace}}.$$ In other words we update $\bar{\rho}^{k}$ using the square root of the ratio between the scaled residuals normalized by the magnitudes of the relative part of the tolerances.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Parameter selection", "weight": 1.0} -->

We set the initial value as $\bar{\rho}^{0}=0.1$. In our benchmarks, if $\bar{\rho}^0$ does not already give a low number of ADMM iterations, it gets usually tuned with a maximum of 1 or 2 updates. The adaptation causes the KKT matrix in[eq:kkt] to change and, if the linear system solver solution method is direct, it requires a new numerical factorization. We do not require a new symbolic factorization because the sparsity pattern of the KKT matrix does not change. Since the numerical factorization can be costly, we perform the adaptation only when it is really necessary. In particular, we allow an update if the accumulated iterations time is greater than a certain percentage of the factorization time (nominally $40\:\%$) and if the new parameter is sufficiently different than the current one $5$ times larger or smaller. Note that in the case of an indirect method this rule allows for more frequent changes of $\rho$ since there is no need to factor the KKT matrix and the update is numerically much cheaper.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Parameter selection", "weight": 1.0} -->

Note that the convergence of the ADMM algorithm is hard to prove in general if the $\rho$ updates happen at each iteration. However, if we assume that the updates stop after a fixed number of iterations the convergence results hold[boyd2011distributed].

<!-- chunk {"id": "body-0070", "role": "body", "section": "Parametric programs", "weight": 1.0} -->

In application domains such as control, statistics, finance, and SQP, problem[pb:main] is solved repeatedly for varying data. For these problems, usually referred to as parametric programs, we can speed up the repeated OSQP calls by re-using the computations across multiple solves.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Parametric programs", "weight": 1.0} -->

We make the distinction between cases in which only the vectors or all data in [pb:main] change between subsequent problem instances. We assume that the problem dimensions $n$ and $m$ and the sparsity patterns of $P$ and $A$are fixed.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Parametric programs", "weight": 1.0} -->

If the vectors $q$, $l$, and $u$ are the only parameters that vary, then the KKT coefficient matrix in Algorithm[alg:osqp\_algorithm] does not change across different instances of the parametric program. Thus, if a direct method is used, we perform and store its factorization only once before the first solution and reuse it across all subsequent iterations. Since the matrix factorization is the computationally most expensive step of the algorithm, this approach reduces significantly the amount of time OSQP takes to solve subsequent problems. This class of problems arises very frequently in many applications including linear MPC and MHE[Rawlings:2009,Allgower1999], Lasso[Tibshirani:1996,Candes:2008], and portfolio optimization[OPT-001,JOFI:JOFI1525].

<!-- chunk {"id": "body-0073", "role": "body", "section": "Parametric programs", "weight": 1.0} -->

Matrices and vectors as parameters. We separately consider the case in which the values (but not the locations) of the nonzero entries of matrices $P$ and $A$ are updated. In this case, in a direct method, we need to refactor the matrix in Algorithm[alg:osqp\_algorithm]. However, since the sparsity pattern does not change we need only to recompute the numerical factorization while reusing the symbolic factorization from the previous solution. This results in a modest reduction in the computation time. This class of problems encompasses several applications such as nonlinear MPC and MHE[Diehl2009] and sequential quadratic programming.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Parametric programs", "weight": 1.0} -->

In contrast to interior-point methods, OSQP is easily initialized by providing an initial guess of both the primal and dual solutions to the QP. This approach is known as warm starting and is particularly effective when the subsequent QP solutions do not vary significantly, which is the case for most parametric programs applications. We can warm start theADMM iterates from the previous OSQP solution $(x^\star, y^\star)$ by setting $(x^{0}, z^{0}, y^{0})\gets (x^{\star}, Ax^{\star}, y^{\star})$. Note that we can warm-start the $\rho$ estimation described in Section[sec:osqp\_implementation]to exploit the ratio between the primal and dual residuals to speed up convergence in subsequent solves.

<!-- chunk {"id": "body-0075", "role": "body", "section": "OSQP", "weight": 1.0} -->

We have implemented our proposed approach in the Operator Splitting Quadratic Program (OSQP) solver, an open-source software package in the C language. OSQP can solve any QP of the form[pb:qp] and makes no assumptions about the problem data other than convexity. OSQP is available online at Users can call OSQP from C Fortran, Python, Matlab, R, Julia, Ruby and Rust, and via parsers such as CVXPY[cvxpy,agrawal2018], JuMP[DunningHuchetteLubin2017], and YALMIP[Lofberg2004].

<!-- chunk {"id": "body-0076", "role": "body", "section": "OSQP", "weight": 1.0} -->

To exploit the data sparsity pattern, OSQP accepts matrices in Compressed-Sparse-Column (CSC) format We implemented the linear system solution described in Section[sec:solving\_linear\_system] as an object-oriented interface to easily switch between efficient algorithms. At present, OSQP ships with the open-source QDLDL direct solver which is our independent implementation based on [Davis:2005], and also supports dynamic loading of more advanced algorithms such as the MKL Pardiso direct solver[intel2017]. We plan to add iterative indirect solvers and other direct solvers in future versions.

<!-- chunk {"id": "body-0077", "role": "body", "section": "OSQP", "weight": 1.0} -->

The default values for the OSQP termination tolerances described in Section [sec:termination criteria] are $$\eps_{\rm abs} = \eps_{\rm rel} = 10^{-3},\quad \eps_{\rm pinf} = \eps_{\rm dinf} = 10^{-4}.$$ The default step-size parameter $\sigma$ and the relaxation parameter $\alpha$ are set to $$\sigma = 10^{-6},\quad \alpha = 1.6,$$ while $\rho$ is automatically chosen by default as described in Section[sec:parameter\_selection], with optional user override. We set the default fixed number of iterative refinement steps to 3.

<!-- chunk {"id": "body-0078", "role": "body", "section": "OSQP", "weight": 1.0} -->

OSQP reports the total computation time divided by the time required to perform preprocessing operations such as scaling or matrix factorization and the time to carry out the If the solver is called multiple times reusing the same matrix factorization, it will report only the ADMMsolve time as total computation time. For more details we refer the reader to the solver documentation on the OSQP project website.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

We benchmarked OSQP against the open-source interior-point solver ECOS[domahidi2013ecos], the open-source active-set solver qpOASES[Ferreau:2014], and the commercial interior-point solvers GUROBI[gurobi] and MOSEK[mosek]. We executed every benchmark comparing different solvers with both low accuracy $\eps_{\rm abs} = \eps_{\rm rel} = 10^{-3}$, and high accuracy $\eps_{\rm abs} = \eps_{\rm rel} = 10^{-5}$. We set GUROBI, ECOS, MOSEK and OSQP primal and dual feasibility tolerances to our low and high accuracy tolerances. Since qpOASES is an active-set method and does not allow the user to tune primal nor dual feasibility tolerances, we set it to its default termination settings. In addition, the maximum time we allow each solver to run is $1000\; {\rm sec}$and no limit on the maximum number of iterations.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

Note that the use of maximum time limits with no bounds on the number of iterations is the default setting in commercial solvers such as MOSEK. For every solver we leave all the other settings to the internal defaults.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

In general it is hard to compare the solution accuracies because all the solvers, especially commercial ones, use an internal problem scaling and verify that the termination conditions are satisfied against their scaled version of the problem. In contrast, OSQP allows the option to check the termination conditions against the internally scaled or the original problem. Therefore, to make the benchmark fair, we say that the primal-dual solution $(x^\star, y^\star)$ returned by each solver is optimal if the following optimality conditions are satisfied with tolerances defined above with low and high accuracy modes, & \|(Ax^\star - u)_{+} + (Ax^\star - l)_{-}\|_\infty \leq \eps_{\rm prim}, &&\|Px^\star + q + A^\tpose y^\star\|_\infty \leq \eps_{\rm dual}, where $\eps_{\rm prim}$ and $\eps_{\rm dual}$ are defined in Section[sec:termination criteria].

<!-- chunk {"id": "body-0082", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

If the primal-dual solution returned by a solver does not satisfy the optimality conditions defined above, we consider it a failure. Note that we decided not to include checks on the complementary slackness satisfaction because interior-point solvers satisfied them with different metrics and scalings, therefore failing very often. In contrast OSQP always satisfies complementary slackness conditions with machine precision by construction.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

In addition, we used the direct single-threaded linear system solver QDLDL [qdldl] based on[Amestoy:2004,Davis:2005]and very simple linear algebra where other solvers such as GUROBI and MOSEK use advanced multi-threaded linear system solvers and custom linear algebra.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

All the experiments were carried out on the MIT SuperCloud facility in collaboration with the Lincoln Laboratory [supercloud] with 16 Intel Xeon E5-2650 cores. The code for all the numerical examples is available online at[OSQPBenchmarks].

<!-- chunk {"id": "body-0085", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

Shifted geometric mean. As in most common benchmarks[hansbench], we make use of the normalized shifted geometric mean to compare the timings of the various solvers. Given the time required by solver $s$ to solve problem $p$ $t_{p, s}$, we define the shifted geometric mean as $$g_{s} \eqdef \sqrt[n]{\prod_{p} (t_{p, s} + k) - k},$$ where $n$ is the number of problem instances considered and $k=1$ is the shift[hansbench]. The normalized shifted geometric mean is therefore This value shows the factor at which a specific solver is slower than the fastest one with scaled value of $1.00$. If solver $s$ fails at solving problem $p$, we set the time as the maximum allowed $t_{p, s} = 1000\; {\rm sec}$. Note that to avoid memory overflows in the product, we compute in practice the shifted geometric mean as $e^{\ln{g_s}}$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

We also make use of the performance profiles[Dolan2002] to compare the solver timings. We define the performance ratio The performance profile plots the function $f_s: \reals \mapsto $ defined as $$f_{s}(\tau) \eqdef \frac{1}{n} \sum_{p}\mathcal{I}_{\leq \tau}(u_{p, s}), %|\{p \mid r_{p, s} \leq \tau\}|,$$ where $\mathcal{I}_{\leq \tau}(u_{p, s}) = 1$ if $u_{p, s} \leq \tau$ or $0$ otherwise. The value $f_s(\tau)$ corresponds to the fraction of problems solved within $\tau$ times from the best solver. Note that while we cannot necessarily assess the performance of one solver relative to another with performance profiles, they still represent a viable choice to benchmark the performance of a solver with respect to the best one[gould2016].

<!-- chunk {"id": "body-0087", "role": "body", "section": "Benchmark problems", "weight": 1.0} -->

We considered QP in the form[pb:qp] from 7 problem classes ranging from standard random programs to applications in the areas of control, portfolio optimization and machine learning. For each problem class, we generated $10$ different instances for $20$ dimensions giving a total of $1400$ problem instances. All instances were obtained from either real data or from non-trivial random data. Note that the random QP and random equality constrained QP problem classes might not closely correspond to a real-world application. However, they have a typical number of nonzero elements appearing in practice. We described generation for each class in Appendix[app:problem\_classes]. Throughout all the problem classes, $n$ ranges between $10^1$ and $10^4$, $m$ between $10^2$ and $10^5$, and the number of nonzeros $N$ between $10^2$ and $10^8$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Benchmark problems", "weight": 1.0} -->

We show in Figures[fig:computation\_times\_low\_accuracy] and[fig:computation\_times\_high\_accuracy] the OSQP and GUROBI computation times across all the problem classes for low and high accuracy solutions respectively. OSQP is competitive or even faster than GUROBI for several problem classes. Results are shown in Table[tab:benchmark\_results] and Figure[fig:benchmarks\_performance\_profiles]. OSQP shows the best performance across these benchmarks with MOSEK performing better at lower accuracy and GUROBI at higher accuracy. ECOS is generally slower than the other interior-point solvers but faster than qpOASES that shows issues with many constraints. Table[tab:benchmark\_osqp\_stats] contains the OSQP statistics for this benchmark class. Because of the good convergence behavior of OSQP on these problems, the setup time is significant compared to the solve time, especially at low accuracy. Solution polishing increases the solution time by a median of $10$ to $20$ percent due to the additional factorization used.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Benchmark problems", "weight": 1.0} -->

The worst-case time increase is very high and happens for the problems that converge in very few iterations. Note that with high accuracy, polishing succeeds in 83% of test cases while on low accuracy it succeeds in only 42% of cases. The number of $\rho$ updates is in general very low, usually requiring just more matrix factorization to adjust, with up to 5 refactorisations used in the worst case when solving with high accuracy.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Benchmark problems", "weight": 1.0} -->

Benchmark problems comparison with timings as shifted geometric mean and failure rates. ${\rm OSQP}$ ${\rm GUROBI}$ ${\rm MOSEK}$ ${\rm ECOS}$ ${\rm qpOASES}$ [head to column names, late after line=]./data/results/benchmark\_problems/geom\_mean.csvOSQP=, means Low accuracy [head to column names, late after line=]./data/results/benchmark\_problems\_high\_accuracy/geom\_mean.csvOSQP\_high=, qpOASES=High accuracy [head to column names, late after line=]./data/results/benchmark\_problems/failure\_rates.csvOSQP=, 2*Failure rates [$\%$] Low accuracy [head to column names, late after line=]./data/results/benchmark\_problems\_high\_accuracy/failure\_rates.csvOSQP\_high=, qpOASES=High accuracy Benchmark problems OSQP statistics.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Benchmark problems", "weight": 1.0} -->

[head to column names, late after line=]./data/results/benchmark\_problems/ratio\_setup\_solve.csvmedian\_ratio=, 2*Setup/solve time [$\%$] Low accuracy [head to column names, late after line=]./data/results/benchmark\_problems\_high\_accuracy/ratio\_setup\_solve.csvmedian\_ratio=, max\_ratio=High accuracy [head to column names, late after line=]./data/results/benchmark\_problems/polish\_statistics.csvmedian\_time\_increase=, max\_time\_increase=, 2*Polish time increase [$\%$] Low accuracy [head to column names, late after line=]./data/results/benchmark\_problems\_high\_accuracy/polish\_statistics.csvmedian\_time\_increase=, max\_time\_increase= [head to column names, late after

<!-- chunk {"id": "body-0092", "role": "body", "section": "Benchmark problems", "weight": 1.0} -->

line=]./data/results/benchmark\_problems/rho\_updates.csvmedian\_rho\_updates=, max\_rho\_updates= 2*Number of $\rho$ updates Low accuracy 1r[zero-decimal-to-integer=true] 1r[zero-decimal-to-integer=true] [head to column names, late after line=]./data/results/benchmark\_problems\_high\_accuracy/rho\_updates.csvmedian\_rho\_updates=, max\_rho\_updates= High accuracy 1r[zero-decimal-to-integer=true] 1r[zero-decimal-to-integer=true] [head to column names, late after line=]./data/results/benchmark\_problems/polish\_statistics.csvpercentage\_of\_success= 2*Polish success [%] Low accuracy [head to column names, late after

<!-- chunk {"id": "body-0093", "role": "body", "section": "Benchmark problems", "weight": 1.0} -->

line=]./data/results/benchmark\_problems\_high\_accuracy/polish\_statistics.csvpercentage\_of\_success=

<!-- chunk {"id": "body-0094", "role": "body", "section": "SuiteSparse matrix collection least squares problems", "weight": 1.0} -->

We considered 30 least squares problem in the form $Ax \approx b$ from the SuiteSparse Matrix Collection library[davis2011]. Using the Lasso and Huber problem setups from Appendix[app:problem\_classes] we formulate 60 QPthat we solve with OSQP, GUROBI and MOSEK. We excluded ECOS because its interior-point algorithm showed numerical issues for several problems of the test set. We also excluded qpOASES because it is not designed for large linear systems.

<!-- chunk {"id": "body-0095", "role": "body", "section": "SuiteSparse matrix collection least squares problems", "weight": 1.0} -->

Results are shown in Table[tab:suitesparse\_results] and Figure[fig:suitesparse\_performance\_profiles]. OSQP shows the best performance with GUROBI slightly slower and MOSEK third. The failure rates for GUROBI and MOSEK are higher because the reported solution does not satisfy the optimality conditions of the original problem. We display the OSQP statistics in Table[tab:suitesparse\_osqp\_stats]. The setup phase takes a significant amount of time compared to the solve phase, especially when OSQP converges in a few iterations. This happens because the large problem dimensions result in a large initial factorization time. Polish time is in general $22$ to $32\%$ of the total solution time. However, the success is usually reliable, succeeding $78\%$ of the times with very high quality solutions. The number of matrix refactorizations required due to $\rho$ updates is very low in these examples, with a maximum of $2$ or $3$even for high accuracy.

<!-- chunk {"id": "body-0096", "role": "body", "section": "SuiteSparse matrix collection least squares problems", "weight": 1.0} -->

SuiteSparse matrix problems comparison with timings as shifted geometric mean and failure rates. ${\rm OSQP}$ ${\rm GUROBI}$ ${\rm MOSEK}$ [head to column names, late after line=]./data/results/suitesparse\_problems/geom\_mean.csvOSQP=, means Low accuracy [head to column names, late after line=]./data/results/suitesparse\_problems\_high\_accuracy/geom\_mean.csvOSQP\_high=, MOSEK\_high=High accuracy [head to column names, late after line=]./data/results/suitesparse\_problems/failure\_rates.csvOSQP=, 2*Failure rates [$\%$] Low accuracy [head to column names, late after line=]./data/results/suitesparse\_problems\_high\_accuracy/failure\_rates.csvOSQP\_high=, MOSEK\_high=High accuracy SuiteSparse problems OSQP statistics.

<!-- chunk {"id": "body-0097", "role": "body", "section": "SuiteSparse matrix collection least squares problems", "weight": 1.0} -->

[head to column names, late after line=]./data/results/suitesparse\_problems/ratio\_setup\_solve.csvmedian\_ratio=, 2*Setup/solve time [$\%$] Low accuracy [head to column names, late after line=]./data/results/suitesparse\_problems\_high\_accuracy/ratio\_setup\_solve.csvmedian\_ratio=, max\_ratio=High accuracy [head to column names, late after line=]./data/results/suitesparse\_problems/polish\_statistics.csvmedian\_time\_increase=, max\_time\_increase=, 2*Polish time increase [$\%$] Low accuracy [head to column names, late after line=]./data/results/suitesparse\_problems\_high\_accuracy/polish\_statistics.csvmedian\_time\_increase=, max\_time\_increase= [head to column names, late after

<!-- chunk {"id": "body-0098", "role": "body", "section": "SuiteSparse matrix collection least squares problems", "weight": 1.0} -->

line=]./data/results/suitesparse\_problems/rho\_updates.csvmedian\_rho\_updates=, max\_rho\_updates= 2*Number of $\rho$ updates Low accuracy 1r[zero-decimal-to-integer=true] 1r[zero-decimal-to-integer=true] [head to column names, late after line=]./data/results/suitesparse\_problems\_high\_accuracy/rho\_updates.csvmedian\_rho\_updates=, max\_rho\_updates= High accuracy 1r[zero-decimal-to-integer=true] 1r[zero-decimal-to-integer=true] [head to column names, late after line=]./data/results/suitesparse\_problems/polish\_statistics.csvpercentage\_of\_success= 2*Polish success [%] Low accuracy [head to column names, late after

<!-- chunk {"id": "body-0099", "role": "body", "section": "SuiteSparse matrix collection least squares problems", "weight": 1.0} -->

line=]./data/results/suitesparse\_problems\_high\_accuracy/polish\_statistics.csvpercentage\_of\_success=

<!-- chunk {"id": "body-0100", "role": "body", "section": "Maros-Meszaros problems", "weight": 1.0} -->

We considered the Maros-Meszaros test set[maros1999] of hard QP. We compared the OSQP solver against GUROBI and MOSEK against all the problems in the set. We decided to exclude ECOS because its interior-point algorithm showed numerical issues for several problems of the test set. We also excluded qpOASES because it could not solve most of the problems since it is not suited for large QP it is based on an active-set method with dense linear algebra.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Maros-Meszaros problems", "weight": 1.0} -->

Results are shown in Table[tab:maros\_results] and Figure[fig:maros\_performance\_profiles]. GUROBI shows the best performance and OSQP, while slower, is still competitive on both low and high accuracy tests. MOSEK remains the slowest in every case. Table[tab:maros\_osqp\_stats] shows the statistics relative to OSQP. Since these hard problems require a larger number of iterations to converge, the setup time overhead compared to the solution time is in general lower than the other benchmark sets. Moreover, since the problems are badly scaled and degenerate, the polishing strategy rarely succeeds. However, the median time increase from the polish step is less than $10\%$ of the total computation time for both low and high accuracy modes. Note that the number of $\rho$ updates is usually very low with a median of $1$ or $2$. However, there are some worst-case problems when it is very high because the bad scaling causes issues in our $\rho$ estimation.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Maros-Meszaros problems", "weight": 1.0} -->

However, from our data we have seen that in more than $95\%$ of the cases the number of $\rho$ updates is less than $5$.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Maros-Meszaros problems", "weight": 1.0} -->

Maros-Meszaros problems comparison with timings as shifted geometric mean and failure rates.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Maros-Meszaros problems", "weight": 1.0} -->

${\rm OSQP}$ ${\rm GUROBI}$ ${\rm MOSEK}$ [head to column names, late after line=]./data/results/maros\_meszaros\_problems/geom\_mean.csvOSQP=, means Low accuracy [head to column names, late after line=]./data/results/maros\_meszaros\_problems\_high\_accuracy/geom\_mean.csvOSQP\_high=, MOSEK\_high=High accuracy [head to column names, late after line=]./data/results/maros\_meszaros\_problems/failure\_rates.csvOSQP=, 2*Failure rates [$\%$] Low accuracy [head to column names, late after line=]./data/results/maros\_meszaros\_problems\_high\_accuracy/failure\_rates.csvOSQP\_high=, MOSEK\_high=High accuracy Maros-Meszaros problems OSQP statistics.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Maros-Meszaros problems", "weight": 1.0} -->

[head to column names, late after line=]./data/results/maros\_meszaros\_problems/ratio\_setup\_solve.csvmedian\_ratio=, 2*Setup/solve time [$\%$] Low accuracy [head to column names, late after line=]./data/results/maros\_meszaros\_problems\_high\_accuracy/ratio\_setup\_solve.csvmedian\_ratio=, max\_ratio=High accuracy [head to column names, late after line=]./data/results/maros\_meszaros\_problems/polish\_statistics.csvmedian\_time\_increase=, max\_time\_increase=, 2*Polish time increase [$\%$] Low accuracy [head to column names, late after line=]./data/results/maros\_meszaros\_problems\_high\_accuracy/polish\_statistics.csvmedian\_time\_increase=, max\_time\_increase= [head to column names, late

<!-- chunk {"id": "body-0106", "role": "body", "section": "Maros-Meszaros problems", "weight": 1.0} -->

after line=]./data/results/maros\_meszaros\_problems/rho\_updates.csvmedian\_rho\_updates=, max\_rho\_updates= 2*Number of $\rho$ updates Low accuracy 1r[zero-decimal-to-integer=true] 1r[zero-decimal-to-integer=true] [head to column names, late after line=]./data/results/maros\_meszaros\_problems\_high\_accuracy/rho\_updates.csvmedian\_rho\_updates=, max\_rho\_updates= High accuracy 1r[zero-decimal-to-integer=true] 1r[zero-decimal-to-integer=true] [head to column names, late after line=]./data/results/maros\_meszaros\_problems/polish\_statistics.csvpercentage\_of\_success= 2*Polish success [%] Low accuracy [head to column names, late after

<!-- chunk {"id": "body-0107", "role": "body", "section": "Maros-Meszaros problems", "weight": 1.0} -->

line=]./data/results/maros\_meszaros\_problems\_high\_accuracy/polish\_statistics.csvpercentage\_of\_success=

<!-- chunk {"id": "body-0108", "role": "body", "section": "Warm start and factorization caching", "weight": 1.0} -->

To show the benefits of warm starting and factorization caching, we solved a sequence of QP using OSQP with the data varying according to some parameters. Since we are not comparing OSQP with other high accuracy solvers in these benchmarks, we use its default settings with accuracy $10^{-3}$.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Warm start and factorization caching", "weight": 1.0} -->

Lasso regularization path. We solved a Lasso problem described in Appendix[app:lasso] with varying $\lambda$ in order to choose a regressor with good validation set performance. We solved one problem instance with $n=50, 100, 150, 200$ features, $m=100n$ data points, and $\lambda$ logarithmically spaced taking 100 values between $\lambda_{\rm max} = \|A^\tpose b\|_{\infty}$ and $0.01\lambda_{\rm max}$.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Warm start and factorization caching", "weight": 1.0} -->

Since the parameters only enter linearly in the cost, we can reuse the matrix factorization and enable warm starting to reduce the computation time as discussed in Section [sec:parametric\_programs].

<!-- chunk {"id": "body-0111", "role": "body", "section": "Warm start and factorization caching", "weight": 1.0} -->

Model predictive control. In MPC, we solve the optimal control problem described in Appendix[app:optimal\_control] at each time step to compute an optimal input sequence over the horizon. Then, we apply only the first input to the system and propagate the state to the next time step. The whole procedure is repeated with an updated initial state $x_{\rm init}$. We solved the control problem with $n_x = 20, 40, 60, 80$ states, $n_u=n_x/2$ inputs, horizon $T=10$ and $100$ simulation steps. The initial state of the simulation is uniformly distributed and constrained to be within the feasible region $x_{{\rm init}} \sim \mathcal{U}(-0.5\overline{x}, 0.5\overline{x})$.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Warm start and factorization caching", "weight": 1.0} -->

Since the parameters only enter linearly in the constraints bounds, we can reuse the matrix factorization and enable warm starting to reduce the computation time as discussed in Section [sec:parametric\_programs].

<!-- chunk {"id": "body-0113", "role": "body", "section": "Warm start and factorization caching", "weight": 1.0} -->

Portfolio back test. Consider the portfolio optimization problem in Appendix[app:portfolio] with $n=10k$ assets and $k=100, 200, 300, 400$factors.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Warm start and factorization caching", "weight": 1.0} -->

We run a 4 years back test to compute the optimal assets investment depending on varying expected returns and factor models We solved $240$ QP per year giving a total of 960 QP. Each month we solved $20$ QP corresponding to the trading days. Every day, we updated the expected returns $\mu$ by randomly generating another vector with $\mu_i \sim 0.9 \hat{\mu}_i + \mathcal{N}(0,0.1)$, where $\hat{\mu}_i$ comes from the previous expected returns.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Warm start and factorization caching", "weight": 1.0} -->

The risk model was updated every month by updating the nonzero elements of $D$ and $F$ according to $D_{ii} \sim 0.9 \hat{D}_{ii} + \mathcal{U}[0, 0.1\sqrt{k}]$ and $F_{ij} \sim 0.9\hat{F}_{ij} + \mathcal{N}(0,0.1)$ where $\hat{D}_{ii}$ and $\hat{F}_{ij}$come from the previous risk model. [sec:parametric\_programs], we exploited the following computations during the QP updates to reduce the computation times. Since $\mu$ only enters in the linear part of the objective, we can reuse the matrix factorization and enable warm starting. Since the sparsity patterns of $D$ and $F$do not change during the monthly updates, we can reuse the symbolic factorization and exploit warm starting to speed up the computations.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Warm start and factorization caching", "weight": 1.0} -->

We show the results in Table[tab:parametric]. For the Lasso problem we see more than $10$-fold improvement in time and between $8$ and $11$ times reduction in number of iterations depending on the dimension. For the MPC problem the number of iterations does not significantly decrease because the number of iterations is already low in cold-start. However we get from $2.6$ to $4$-fold time improvement from factorization caching. OSQP shows from $5.8$ to $7$ times reduction in time for the portfolio problem and from $2.9$ to $3.6$times reduction in number of iterations.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Warm start and factorization caching", "weight": 1.0} -->

OSQP parametric problem results with warm start (ws) and without warm start (no ws) in terms of time in seconds and number of iterations for different leading problem dimensions of Lasso, MPC and Portfolio classes.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We presented a novel general-purpose QP solver based on ADMM. Our method uses a new splitting requiring the solution of a quasi-definite linear system that is always solvable independently from the problem data. We impose no assumptions on the problem data other than convexity, resulting in a general-purpose and very robust algorithm.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Conclusions", "weight": 1.0} -->

For the first time, we propose a first-order QPsolution method able to provide primal and dual infeasibility certificates if the problem is unsolvable without resorting to homogeneous self-dual embedding or additional complexity in the iterations.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In contrast to other first-order methods, our solver can provide high-quality solutions by performing After guessing which constraints are active, we compute the solutions of an additional small equality constrained QPby solving a linear system. If the constraints are identified correctly, the returned solution has accuracy equal or higher than interior-point methods.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Conclusions", "weight": 1.0} -->

The proposed method is easily warm started to reduce the number of iterations. If the problem matrices do not change, the linear system matrix factorization can be cached and reused across multiple solves greatly improving the computation time. This technique can be extremely effective, especially when solving parametric QPwhere only part of the problem data change.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have implemented our algorithm in the open-source OSQP solver written in C and interfaced with multiple other languages and parsers. OSQP is based on sparse linear algebra and is able to exploit the structure of QParising in different application areas. OSQP is robust against noisy and unreliable data and, after the first factorization is computed, can be compiled to be library-free and division-free, making it suitable for embedded applications. Thanks to its simple and parallelizable iterations, OSQP can handle large-scale problems with millions of nonzeros.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We extensively benchmarked the OSQP solver with problems arising in several application domains including finance, control and machine learning. In addition, we benchmarked it against the hard problems from the Maros-M eszaros test set[maros1999] and Lasso and Huber fitting problems generated with sparse matrices from the SuiteSparse Matrix Collection[davis2011]. Timing and failure rate results showed great improvements over state-of-the-art academic and commercial QPsolvers.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Conclusions", "weight": 1.0} -->

OSQP has already a large userbase with tens of thousands of users both from top academic institutions and large corporations.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Conclusions", "weight": 1.0} -->

\def\paragraph{\@startsection{paragraph}{4}{\z@}% {-13pt plus-8pt minus-4pt}{\z@}{\small\itshape}} \renewcommand\thesection{\@Alph\c@section}

<!-- chunk {"id": "body-0126", "role": "body", "section": "Problem classes", "weight": 1.0} -->

In this section we describe the random problem classes used in the benchmarks and derive formulations with explicit linear equalities and inequalities that can be directly written in the form $Ax \in \mathcal{C}$ with $\mathcal{C} = [l, u]$.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Random QP", "weight": 1.0} -->

Consider the following QP \mbox{minimize} & (1/2) x^\tpose P x + q^\tpose x \\%[1ex] \mbox{subject to} & l \leq A x \leq u.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Random QP", "weight": 1.0} -->

The number of variables and constraints in our problem instances are $n$ and $m=10n$. We generated random matrix $P= M M^\tpose + \alpha I$ where $M\in \reals^{n \times n}$ and $15 \%$ nonzero elements $M_{ij}\sim \mathcal{N}$. We add the regularization $\alpha I$ with $\alpha = 10^{-2}$ to ensure that the problem is not unbounded. We set the elements of $A\in \reals^{m \times n}$ as $A_{ij} \sim \mathcal{N}$ with only $15 \%$ being nonzero. The linear part of the cost is normally distributed $q_i \sim \mathcal{N}$. We generated the constraint bounds as $u_i \sim \mathcal{U}$, $l_i \sim -\mathcal{U}$.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Equality constrained QP", "weight": 1.0} -->

Consider the following equality constrained QP \mbox{minimize} & (1/2) x^\tpose P x + q^\tpose x \\%[1ex] This problem can be rewritten as[pb:main] by setting $l = u = b$.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Equality constrained QP", "weight": 1.0} -->

The number of variables and constraints in our problem instances are $n$ and $m=\lfloor n/2\rfloor$.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Equality constrained QP", "weight": 1.0} -->

We generated random matrix $P= M M^\tpose + \alpha I$ where $M\in \reals^{n \times n}$ and $15 \%$ nonzero elements $M_{ij}\sim \mathcal{N}$. We add the regularization $\alpha I$ with $\alpha = 10^{-2}$ to ensure that the problem is not unbounded. We set the elements of $A\in \reals^{m \times n}$ as $A_{ij} \sim \mathcal{N}$ with only $15 \%$ being nonzero. The vectors are all normally distributed $q_i, b_i \sim \mathcal{N}$.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Equality constrained QP", "weight": 1.0} -->

Solution of the above problem can be found directly by solving the following linear system $$\begin{bmatrix} P & A^\tpose \\ A & 0\end{bmatrix} \begin{bmatrix}x \\ \nu \end{bmatrix} = \begin{bmatrix} -q \\ b \end{bmatrix}.$$ If we apply the ADMM iterations[eq:ADMM\_iter1][eq:ADMM\_iter5] for solving the above problem, and by setting $\alpha=1$ and $y^0=b$, the algorithm boils down to the following iteration $$\begin{bmatrix} x^{k+1} \\ \nu^{k+1} \end{bmatrix} = \begin{bmatrix} x^k \\ \nu^k \end{bmatrix} + \begin{bmatrix} P + \sigma I & A^\tpose \\ A & -\rho^{-1} I

<!-- chunk {"id": "body-0133", "role": "body", "section": "Equality constrained QP", "weight": 1.0} -->

This means that Algorithm[alg:osqp\_algorithm] applied to solve an equality constrained QP is equivalent to applying iterative refinement[Wilkinson:1963,duff1986direct] to solve the KKT system [eq:eq\_constr\_qp\_optimality]. Note that the perturbation matrix in this case is $$\Delta K = \begin{bmatrix} \sigma I \\ & -\rho^{-1} I \end{bmatrix},$$ which justifies using a low value of $\sigma$ and a high value of $\rho$for equality constraints.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Optimal control", "weight": 1.0} -->

We consider the problem of controlling a constrained linear time-invariant dynamical system. To achieve this, we formulate the following optimization problem \mbox{minimize} & x_T^\tpose Q_T x_T + \sum_{t=0}^{T-1} x_t^\tpose Q x_t + u_t^\tpose R u_t \\[.25em] The states $x_t\in\reals^{n_x}$ and the inputs $u_k\in\reals^{n_u}$ are subject to polyhedral constraints defined by the sets$\mathcal{X}$ and$\mathcal{U}$. The horizon length is$T$ and the initial state is $x_{\rm init}\in\reals^{n_x}$.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Optimal control", "weight": 1.0} -->

Matrices $Q\in\symm^{n_x}_+$ and $R\in\symm^{n_u}_{++}$ define the state and input costs at each stage of the horizon, and $Q_T\in\symm^{n_x}_+$defines the final stage cost.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Optimal control", "weight": 1.0} -->

By defining the new variable $z = (x_0, \dots, x_{T}, u_0, \dots, u_{T-1})$, problem[pb:mpc] can be written as a sparse QP of the form[pb:qp] with a total of $n_x(T+1) + n_u T$variables.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Optimal control", "weight": 1.0} -->

We defined the linear systems with $n = n_x$ states and $n_u = 0.5n_x$ inputs. We set the horizon length to $T=10$. We generated the dynamics as $A = I + \Delta$ with $\Delta_{ij} \sim \mathcal{N}(0, 0.01)$. We chose only stable dynamics by enforcing the norm of the eigenvalues of $A$ to be less than $1$. The input action is modeled as $B$ with $B_{ij} \sim \mathcal{N}$.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Optimal control", "weight": 1.0} -->

The state cost is defined as $Q = \diag(q)$ where $q_i \sim \mathcal{U}$ and $70\%$ nonzero elements in $q$. We chose the input cost as $R = 0.1I$. The terminal cost $Q_T$ is chosen as the optimal cost for the linear quadratic regulator (LQR) applied to $A, B, Q, R$ by solving a discrete algebraic Riccati equation (DARE)[borrelli2017predictive].

<!-- chunk {"id": "body-0139", "role": "body", "section": "Portfolio optimization", "weight": 1.0} -->

Portfolio optimization is a problem arising in finance that seeks to allocate assets in a way that maximizes the risk adjusted return [OPT-001,JOFI:JOFI1525,OPT-023],[boyd2004convex], \mbox{maximize} & \mu^\tpose x - \gamma (x^\tpose \Sigma x) \\\mbox{subject to} & \ones^\tpose x = 1 \\where the variable $x \in \reals^{n}$ represents the portfolio, $\mu \in \reals^{n}$ the vector of expected returns, $\gamma > 0$ the risk aversion parameter, and $\Sigma\in\symm_+^n$ the risk model covariance matrix. The risk model is usually assumed to be the sum of a diagonal and a rank $k < n$ matrix where $F\in \reals^{n\times k}$ is the factor loading matrix and $D\in \reals^{n\times n}$is a diagonal matrix describing the asset-specific risk.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Portfolio optimization", "weight": 1.0} -->

We introduce a new variable $y=F^\tpose x$ and solve the resulting problem in variables$x$ and$y$ \mbox{minimize} & x^\tpose D x + y^\tpose y - \gamma^{-1} \mu^\tpose x \\Note that the Hessian of the objective in [pb:portfolio\_sparse] is a diagonal matrix. Also, observe that $FF^\tpose$ does not appear in problem [pb:portfolio\_sparse].

<!-- chunk {"id": "body-0141", "role": "body", "section": "Portfolio optimization", "weight": 1.0} -->

Problem instances. We generated portfolio problems for increasing number of factors $k$ and number of assets $n=100k$. The elements of matrix $F$ were chosen as $F_{ij} \sim \mathcal{N}$ with $50 \%$ nonzero elements. The diagonal matrix $D$ is chosen as $D_{ii} \sim \mathcal{U}[0, \sqrt{k}]$. The mean return was generated as $\mu_i \sim \mathcal{N}$.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Lasso", "weight": 1.0} -->

The least absolute shrinkage and selection operator (Lasso) is a well known linear regression technique obtained by adding an$\ell_1$ regularization term in the objective[Tibshirani:1996,Candes:2008].

<!-- chunk {"id": "body-0143", "role": "body", "section": "Lasso", "weight": 1.0} -->

\mbox{minimize} & \|Ax - b\|_2^2 + \lambda\|x\|_1, where $x\in \reals^{n}$ is the vector of parameters and $A\in\reals^{m \times n}$ is the data matrix and $\lambda$is the weighting parameter.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Lasso", "weight": 1.0} -->

We convert this problem to the following \mbox{minimize} & y^\tpose y + \lambda \ones^\tpose t\\where $y\in\reals^{m}$ and $t\in\reals^{n}$are two newly introduced variables.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Lasso", "weight": 1.0} -->

The elements of matrix $A$ are generated as $A_{ij} \sim \mathcal{N}$ with $15 \%$ nonzero elements. To construct the vector $b$, we generated the true sparse vector $v\in \reals^{n}$ to be learned 0 & \mbox{with probability } p=0.5\\\mathcal{N}(0, 1/n) & \mbox{otherwise}.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Lasso", "weight": 1.0} -->

Then we let $b=Av + \varepsilon$ where $\varepsilon$ is the noise generated as $\varepsilon_i \sim \mathcal{N}$. We generated the instances with varying $n$ features and $m = 100n$ data points. The parameter $\lambda$ is chosen as $(1/5)\|A^\tpose b\|_{\infty}$ since $\|A^\tpose b\|_{\infty}$ is the critical value above which the solution of the problem is $x=0$.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Huber fitting", "weight": 1.0} -->

Huber fitting or the robust least-squares problem performs linear regression under the assumption that there are outliers in the data[Huber:1964,Huber:1981]. The fitting problem is written as \mbox{minimize} & \sum_{i=1}^m \phi_{\rm hub}(a_i^T x - b_i), with the Huber penalty function $\phi_{\rm hub}:\reals\to\reals$ defined as $$\phi_{\rm hub}(u) = \begin{cases} Problem[pb:huber\_fitting] is equivalent to the following QP[Mangasarian:2000] \mbox{minimize} & u^\tpose u + 2M \ones^\tpose (r + s) \\We generate the elements of $A$ as $A_{ij} \sim \mathcal{N}$ with $15 \%$ nonzero elements.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Huber fitting", "weight": 1.0} -->

To construct $b\in\reals^m$ we first generate a vector $v\in\reals^n$ as $v_i \sim \mathcal{N}(0,1/n)$ and a noise vector $\varepsilon\in\reals^m$ with elements $$\varepsilon_i \sim \begin{cases} \mathcal{N}(0,1/4) & \text{with probability $p=0.95$} \\\mathcal{U} & \text{otherwise}.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Huber fitting", "weight": 1.0} -->

We then set $b = Av + \varepsilon$. For each instance we choose $m=100n$ and $M=1$.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

Support vector machine problem seeks an affine function that approximately classifies the two sets of points[Cortes:1995]. The problem can be stated as \mbox{minimize} & x^\tpose x + \lambda \sum_{i=1}^m \max(0, b_i a_i^T x + 1), where $b_i \in \{ -1, +1 \}$ is a set label, and $a_i$ is a vector of features for the $i$-th point. The problem can be equivalently represented as the following QP \mbox{minimize} & x^\tpose x + \lambda \ones^\tpose t \\where$\diag(b)$ denotes the diagonal matrix with elements of$b$on its diagonal.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

We choose the vector$b$ so that and the elements of $A$ as $$A_{ij} \sim \begin{cases} \mathcal{N}(-1/n,1/n) & \text{otherwise}, with $15\%$nonzeros per case.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

confidence=None created_by=None text='\\begin{tikzpicture}\n \\begin{groupplot}[\n\twidth=.475\\textwidth,\n\theight=.2\\textheight,\n\tgroup style={\n\tgroup size= 2 by 3,\n\tvertical sep=3.5em,\n\thorizontal sep=3.5em},\n\tgrid=both, % Display a grid\n\t% grid style={line width=.1pt, draw=gray!30},\n\t% major grid style={line width=.2pt,draw=gray!60},\n\t% xlabel={Problem dimension $N$},\n\t% xticklabels = { },\n\t% ylabel={Computation time},\n\t% y unit=\\si{\\second},\n\tymin = 0.0001,\n\tymax =

<!-- chunk {"id": "body-0153", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

1000,\n\txmin = 100,\n\txmax = 100000000,\n\txmode=log,\n\tymode=log\n\t\t]\n\t\t% Random QP\n\t\t\\nextgroupplot[title=Random QP, ylabel={Computation time}, y unit=\\si{\\second}]\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{Random QP},\n\t\tscatter/classes={Random QP={mark=\\gurobimarker, gurobi}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma]

<!-- chunk {"id": "body-0154", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

{data/results/benchmark_problems/GUROBI/results.csv};\\label{plot:osqp:timing_gurobi_low}\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{Random QP},\n\t\tscatter/classes={Random QP={mark=\\osqpmarker, osqp}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma] {data/results/benchmark_problems/OSQP/results.csv};\\label{plot:osqp:timing_osqp_low}\n\t\t\\coordinate (top) at (rel axis cs:0,1);% coordinate at top of the first plot\n\t\t% Equality constrained QP\n\t\t\\nextgroupplot[title=Eq

<!-- chunk {"id": "body-0155", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

QP]\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{Eq QP},\n\t\tscatter/classes={Eq QP={mark=\\gurobimarker, gurobi}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma] {data/results/benchmark_problems/GUROBI/results.csv};\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{Eq QP},\n\t\tscatter/classes={Eq QP={mark=\\osqpmarker, osqp}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma]

<!-- chunk {"id": "body-0156", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

{data/results/benchmark_problems/OSQP/results.csv};\n\t\t% Portfolio\n\t\t\\nextgroupplot[title=Portfolio, ylabel={Computation time}, y unit=\\si{\\second}]\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{Portfolio},\n\t\tscatter/classes={Portfolio={mark=\\gurobimarker, gurobi}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma] {data/results/benchmark_problems/GUROBI/results.csv};\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if

<!-- chunk {"id": "body-0157", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

not={class}{Portfolio},\n\t\tscatter/classes={Portfolio={mark=\\osqpmarker, osqp}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma] {data/results/benchmark_problems/OSQP/results.csv};\n\t\t% Lasso\n\t\t\\nextgroupplot[title=Lasso]\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{Lasso},\n\t\tscatter/classes={Lasso={mark=\\gurobimarker, gurobi}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma]

<!-- chunk {"id": "body-0158", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

{data/results/benchmark_problems/GUROBI/results.csv};\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{Lasso},\n\t\tscatter/classes={Lasso={mark=\\osqpmarker, osqp}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma] {data/results/benchmark_problems/OSQP/results.csv};\n\t\t% SVM\n\t\t\\nextgroupplot[title=SVM, ylabel={Computation time}, y unit=\\si{\\second}, xlabel={Problem dimension $N$}]\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if

<!-- chunk {"id": "body-0159", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

not={class}{SVM},\n\t\tscatter/classes={SVM={mark=\\gurobimarker, gurobi}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma] {data/results/benchmark_problems/GUROBI/results.csv};\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{SVM},\n\t\tscatter/classes={SVM={mark=\\osqpmarker, osqp}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma] {data/results/benchmark_problems/OSQP/results.csv};\n\t\t% Huber\n\t\t\\nextgroupplot[title=Huber,

<!-- chunk {"id": "body-0160", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

xlabel={Problem dimension $N$}]\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{Huber},\n\t\tscatter/classes={Huber={mark=\\gurobimarker, gurobi}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma] {data/results/benchmark_problems/GUROBI/results.csv};\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{Huber},\n\t\tscatter/classes={Huber={mark=\\osqpmarker, osqp}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma]

<!-- chunk {"id": "body-0161", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

{data/results/benchmark_problems/OSQP/results.csv};\n\t \\coordinate (bot) at (rel axis cs:1,0);% coordinate at bottom of the last plot\n\\end{groupplot}\n\t% legend\n\t\\path (top|-current bounding box.north)--\n\t coordinate(legendpos)\n\t (bot|-current bounding box.north);\n\t\\matrix[\n\t matrix of nodes,\n\t anchor=south,\n\t draw,\n\t inner sep=0.2em,\n\t] at ([yshift=1ex]legendpos) {\n\t \plot:osqp:timing_gurobi_low& GUROBI &[5pt] \plot:osqp:timing_osqp_low& OSQP\\\\};\n\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ:

<!-- chunk {"id": "body-0162", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

'Tikz'> confidence=None created_by=None text='\\begin{tikzpicture}\n\t\t% Last plot\n\t\t\\begin{axis}[\n\t\twidth=.475\\textwidth,\n\t\theight=.2\\textheight,\n\t\tgrid=both, % Display a grid\n\t\tymin = 0.0001,\n\t\tymax = 1000,\n\t\txmin = 100,\n\t\txmax = 100000000,\n\t\ttitle = {Control},\n\t\txlabel={Problem dimension $N$},\n\t\tylabel={Computation time}, y unit=\\si{\\second},\n\t\txmode=log,\n\t\tymode=log]\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic,

<!-- chunk {"id": "body-0163", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

%%\n\t\tdiscard if not={class}{Control},\n\t\tscatter/classes={Control={mark=\\gurobimarker, gurobi}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma] {data/results/benchmark_problems/GUROBI/results.csv};\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{Control},\n\t\tscatter/classes={Control={mark=\\osqpmarker, osqp}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma]

<!-- chunk {"id": "body-0164", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

{data/results/benchmark_problems/OSQP/results.csv};\n\t\t\\end{axis}\n\t\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> Computation time vs problem dimension for OSQP and GUROBI for low accuracy mode.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

confidence=None created_by=None text='\\begin{tikzpicture}\n \\begin{groupplot}[\n\twidth=.475\\textwidth,\n\theight=.2\\textheight,\n\tgroup style={\n\tgroup size= 2 by 4,\n\tvertical sep=3.5em,\n\thorizontal sep=3.5em},\n\tgrid=both, % Display a grid\n\t% grid style={line width=.1pt, draw=gray!30},\n\t% major grid style={line width=.2pt,draw=gray!60},\n\t% xlabel={Problem dimension $N$},\n\t% xticklabels = { },\n\t% ylabel={Computation time},\n\t% y unit=\\si{\\second},\n\tymin = 0.0001,\n\tymax =

<!-- chunk {"id": "body-0166", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

1000,\n\txmin = 100,\n\txmax = 100000000,\n\txmode=log,\n\tymode=log\n\t\t]\n\t\t% Random QP\n\t\t\\nextgroupplot[title=Random QP, ylabel={Computation time}, y unit=\\si{\\second}]\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{Random QP},\n\t\tscatter/classes={Random QP={mark=\\gurobimarker, gurobi}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma]

<!-- chunk {"id": "body-0167", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

{data/results/benchmark_problems_high_accuracy/GUROBI_high/results.csv};\\label{plot:osqp:timing_gurobi_high}\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{Random QP},\n\t\tscatter/classes={Random QP={mark=\\osqpmarker, osqp}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma] {data/results/benchmark_problems_high_accuracy/OSQP_high/results.csv};\\label{plot:osqp:timing_osqp_high}\n\t\t\\coordinate (top) at (rel axis cs:0,1);% coordinate at top of the first plot\n\t\t% Equality constrained

<!-- chunk {"id": "body-0168", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

QP\n\t\t\\nextgroupplot[title=Eq QP]\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{Eq QP},\n\t\tscatter/classes={Eq QP={mark=\\gurobimarker, gurobi}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma] {data/results/benchmark_problems_high_accuracy/GUROBI_high/results.csv};\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{Eq QP},\n\t\tscatter/classes={Eq QP={mark=\\osqpmarker, osqp}}]

<!-- chunk {"id": "body-0169", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

%\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma] {data/results/benchmark_problems_high_accuracy/OSQP_high/results.csv};\n\t\t% Portfolio\n\t\t\\nextgroupplot[title=Portfolio, ylabel={Computation time}, y unit=\\si{\\second}]\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{Portfolio},\n\t\tscatter/classes={Portfolio={mark=\\gurobimarker, gurobi}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma] {data/results/benchmark_problems_high_accuracy/GUROBI_high/results.csv};\n\t\t\\addplot [scatter, only

<!-- chunk {"id": "body-0170", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{Portfolio},\n\t\tscatter/classes={Portfolio={mark=\\osqpmarker, osqp}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma] {data/results/benchmark_problems_high_accuracy/OSQP_high/results.csv};\n\t\t% Lasso\n\t\t\\nextgroupplot[title=Lasso]\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{Lasso},\n\t\tscatter/classes={Lasso={mark=\\gurobimarker, gurobi}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col

<!-- chunk {"id": "body-0171", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

sep=comma] {data/results/benchmark_problems_high_accuracy/GUROBI_high/results.csv};\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{Lasso},\n\t\tscatter/classes={Lasso={mark=\\osqpmarker, osqp}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma] {data/results/benchmark_problems_high_accuracy/OSQP_high/results.csv};\n\t\t% SVM\n\t\t\\nextgroupplot[title=SVM, ylabel={Computation time}, y unit=\\si{\\second}, xlabel={Problem dimension $N$}]\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic,

<!-- chunk {"id": "body-0172", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

%%\n\t\tdiscard if not={class}{SVM},\n\t\tscatter/classes={SVM={mark=\\gurobimarker, gurobi}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma] {data/results/benchmark_problems_high_accuracy/GUROBI_high/results.csv};\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{SVM},\n\t\tscatter/classes={SVM={mark=\\osqpmarker, osqp}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma] {data/results/benchmark_problems_high_accuracy/OSQP_high/results.csv};\n\t\t%

<!-- chunk {"id": "body-0173", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

Huber\n\t\t\\nextgroupplot[title=Huber, xlabel={Problem dimension $N$}]\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{Huber},\n\t\tscatter/classes={Huber={mark=\\gurobimarker, gurobi}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma] {data/results/benchmark_problems_high_accuracy/GUROBI_high/results.csv};\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{Huber},\n\t\tscatter/classes={Huber={mark=\\osqpmarker, osqp}}]

<!-- chunk {"id": "body-0174", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

%\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma] {data/results/benchmark_problems_high_accuracy/OSQP_high/results.csv};\n\t \\coordinate (bot) at (rel axis cs:1,0);% coordinate at bottom of the last plot\n\t % Control\n\t\t% \\nextgroupplot[title=Control, ylabel={Computation time}, y unit=\\si{\\second}, xlabel={Problem dimension $N$}]\n\t\t% \\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\t% discard if not={class}{Control},\n\t\t% scatter/classes={Control={mark=\\gurobimarker, gurobi}}] %\n\t\t% table[x=N, y=run_time, meta=class, col sep=comma]

<!-- chunk {"id": "body-0175", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

{data/results/benchmark_problems_high_accuracy/GUROBI_high/results.csv};\\label{plot:osqp:timing_gurobi_high}\n\t\t% \\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\t% discard if not={class}{Control},\n\t\t% scatter/classes={Control={mark=\\osqpmarker, osqp}}] %\n\t\t% table[x=N, y=run_time, meta=class, col sep=comma] {data/results/benchmark_problems_high_accuracy/OSQP_high/results.csv};\\label{plot:osqp:timing_osqp_high}\n\t\t% \\coordinate (top) at (rel axis cs:0,1);% coordinate at top of the first plot\n\\end{groupplot}\n\t% legend\n\t\\path

<!-- chunk {"id": "body-0176", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

(top|-current bounding box.north)--\n\t coordinate(legendpos)\n\t (bot|-current bounding box.north);\n\t\\matrix[\n\t matrix of nodes,\n\t anchor=south,\n\t draw,\n\t inner sep=0.2em,\n\t] at ([yshift=1ex]legendpos) {\n\t \plot:osqp:timing_gurobi_high& GUROBI &[5pt] \plot:osqp:timing_osqp_high& OSQP\\\\};\n\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> confidence=None created_by=None text='\\begin{tikzpicture}\n\t\t% Last

<!-- chunk {"id": "body-0177", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

plot\n\t\t\\begin{axis}[\n\t\twidth=.475\\textwidth,\n\t\theight=.2\\textheight,\n\t\tgrid=both, % Display a grid\n\t\tymin = 0.0001,\n\t\tymax = 1000,\n\t\txmin = 100,\n\t\txmax = 100000000,\n\t\ttitle = {Control},\n\t\txlabel={Problem dimension $N$},\n\t\tylabel={Computation time}, y unit=\\si{\\second},\n\t\txmode=log,\n\t\tymode=log]\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if

<!-- chunk {"id": "body-0178", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

not={class}{Control},\n\t\tscatter/classes={Control={mark=\\gurobimarker, gurobi}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma] {data/results/benchmark_problems_high_accuracy/GUROBI_high/results.csv};\n\t\t\\addplot [scatter, only marks, scatter src=explicit symbolic, %%\n\t\tdiscard if not={class}{Control},\n\t\tscatter/classes={Control={mark=\\osqpmarker, osqp}}] %\n\t\t\ttable[x=N, y=run_time, meta=class, col sep=comma]

<!-- chunk {"id": "body-0179", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

{data/results/benchmark_problems_high_accuracy/OSQP_high/results.csv};\n\t\t\\end{axis}\n\t\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> Computation time vs problem dimension for OSQP and GUROBI for high accuracy mode.

<!-- chunk {"id": "body-0180", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

10000,\n\t\txmode=log,\n\t\t\t\tlegend entries={OSQP, GUROBI, MOSEK, ECOS, qpOASES},\n\t\t\t\tlegend cell align=left,\n\t\tlegend style={at={(.95,.05)},anchor=south east, fill=white, fill opacity=1, draw opacity=1,text opacity=1},\n\t\tlog ticks with fixed point,\n\t\t\t\tevery axis plot/.append style={very thick}\n\t\t\t\t]\n\t\t\\addplot [osqp, \\osqplinestyle] table[x=tau, y=OSQP, col sep=comma] {data/results/benchmark_problems/performance_profiles.csv};\n\t\t\\addplot [gurobi, \\gurobilinestyle]

<!-- chunk {"id": "body-0181", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

table[x=tau, y=GUROBI, col sep=comma] {data/results/benchmark_problems/performance_profiles.csv};\n\t\t\\addplot [mosek, \\moseklinestyle] table[x=tau, y=MOSEK, col sep=comma] {data/results/benchmark_problems/performance_profiles.csv};\n\t\t\t\t\\addplot [ecos] table[x=tau, y=ECOS, col sep=comma] {data/results/benchmark_problems/performance_profiles.csv};\n\t\t\\addplot [qpoases, \\qpoaseslinestyle] table[x=tau, y=qpOASES, col sep=comma] {data/results/benchmark_problems/performance_profiles.csv};\n\t \\end{axis}\n\t\t\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ:

<!-- chunk {"id": "body-0182", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

10000,\n\t\txmode=log,\n\t\t\t\tlegend entries={OSQP, GUROBI, MOSEK, ECOS, qpOASES},\n\t\t\t\tlegend cell align=left,\n\t\tlegend style={at={(.95,.05)},anchor=south east, fill=white, fill opacity=1, draw opacity=1,text opacity=1},\n\t\tlog ticks with fixed point,\n\t\t\t\tevery axis plot/.append style={very thick}\n\t\t\t\t]\n\t\t\\addplot [osqp, \\osqplinestyle] table[x=tau, y=OSQP_high, col sep=comma] {data/results/benchmark_problems_high_accuracy/performance_profiles.csv};\n\t\t\\addplot [gurobi,

<!-- chunk {"id": "body-0183", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

\\gurobilinestyle] table[x=tau, y=GUROBI_high, col sep=comma] {data/results/benchmark_problems_high_accuracy/performance_profiles.csv};\n\t\t\\addplot [mosek, \\moseklinestyle] table[x=tau, y=MOSEK_high, col sep=comma] {data/results/benchmark_problems_high_accuracy/performance_profiles.csv};\n\t\t\t\t\\addplot [ecos] table[x=tau, y=ECOS_high, col sep=comma] {data/results/benchmark_problems_high_accuracy/performance_profiles.csv};\n\t\t\\addplot [qpoases, \\qpoaseslinestyle] table[x=tau, y=qpOASES, col sep=comma] {data/results/benchmark_problems_high_accuracy/performance_profiles.csv};\n\t

<!-- chunk {"id": "body-0184", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

\\end{axis}\n\t\t\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> Benchmark problems comparison with performance profiles.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

10000,\n\t\txmode=log,\n\t\t\t\tlegend entries={OSQP, GUROBI, MOSEK},\n\t\t\t\tlegend cell align=left,\n\t\tlegend style={at={(.95,.05)},anchor=south east, fill=white, fill opacity=1, draw opacity=1,text opacity=1},\n\t\tlog ticks with fixed point,\n\t\t\t\tevery axis plot/.append style={very thick}\n\t\t\t\t]\n\t\t\\addplot [osqp, \\osqplinestyle] table[x=tau, y=OSQP, col sep=comma] {data/results/suitesparse_problems/performance_profiles.csv};\n\t\t\\addplot [gurobi, \\gurobilinestyle] table[x=tau,

<!-- chunk {"id": "body-0186", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

y=GUROBI, col sep=comma] {data/results/suitesparse_problems/performance_profiles.csv};\n\t\t\\addplot [mosek, \\moseklinestyle] table[x=tau, y=MOSEK, col sep=comma] {data/results/suitesparse_problems/performance_profiles.csv};\n\t \\end{axis}\n\t\t\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> confidence=None created_by=None text='\\begin{tikzpicture}\n\t\t\\begin{axis}[\n\t\twidth=0.9\\textwidth,\n\t\theight=0.33\\textwidth,\n\t\tgrid=both, % Display a grid %\n\t\tgrid style={line width=.1pt,

<!-- chunk {"id": "body-0187", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

draw=gray!30},\n\t\tmajor grid style={line width=.2pt,draw=gray!60},\n\t\ttitle = {High accuracy},\n\t\txlabel={Performance ratio $\\tau$},\n\t\t\t\tylabel={Ratio of problems solved},\n\t\t\t\tymin = 0,\n\t\t\t\tymax = 1,\n\t\txmin = 1,\n\t\t\t\txmax = 10000,\n\t\txmode=log,\n\t\t\t\tlegend entries={OSQP, GUROBI, MOSEK},\n\t\t\t\tlegend cell align=left,\n\t\tlegend style={at={(.95,.05)},anchor=south east, fill=white, fill opacity=1, draw opacity=1,text

<!-- chunk {"id": "body-0188", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

opacity=1},\n\t\tlog ticks with fixed point,\n\t\t\t\tevery axis plot/.append style={very thick}\n\t\t\t\t]\n\t\t\\addplot [osqp, \\osqplinestyle] table[x=tau, y=OSQP_high, col sep=comma] {data/results/suitesparse_problems_high_accuracy/performance_profiles.csv};\n\t\t\\addplot [gurobi, \\gurobilinestyle] table[x=tau, y=GUROBI_high, col sep=comma] {data/results/suitesparse_problems_high_accuracy/performance_profiles.csv};\n\t\t\\addplot [mosek, \\moseklinestyle] table[x=tau, y=MOSEK_high, col sep=comma]

<!-- chunk {"id": "body-0189", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

{data/results/suitesparse_problems_high_accuracy/performance_profiles.csv};\n\t \\end{axis}\n\t\t\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> SuiteSparse matrix problems comparison with performance profiles.

<!-- chunk {"id": "body-0190", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

10000,\n\t\txmode=log,\n\t\t\t\tlegend entries={OSQP, GUROBI, MOSEK},\n\t\t\t\tlegend cell align=left,\n\t\tlegend style={at={(.95,.05)},anchor=south east, fill=white, fill opacity=1, draw opacity=1,text opacity=1},\n\t\tlog ticks with fixed point,\n\t\t\t\tevery axis plot/.append style={very thick}\n\t\t\t\t]\n\t\t\\addplot [osqp, \\osqplinestyle] table[x=tau, y=OSQP, col sep=comma] {data/results/maros_meszaros_problems/performance_profiles.csv};\n\t\t\\addplot [gurobi, \\gurobilinestyle]

<!-- chunk {"id": "body-0191", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

table[x=tau, y=GUROBI, col sep=comma] {data/results/maros_meszaros_problems/performance_profiles.csv};\n\t\t\\addplot [mosek, \\moseklinestyle] table[x=tau, y=MOSEK, col sep=comma] {data/results/maros_meszaros_problems/performance_profiles.csv};\n\t \\end{axis}\n\t\t\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> confidence=None created_by=None text='\\begin{tikzpicture}\n\t\t\\begin{axis}[\n\t\twidth=0.9\\textwidth,\n\t\theight=0.33\\textwidth,\n\t\tgrid=both, % Display a grid %\n\t\tgrid style={line

<!-- chunk {"id": "body-0192", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

width=.1pt, draw=gray!30},\n\t\tmajor grid style={line width=.2pt,draw=gray!60},\n\t\ttitle = {High accuracy},\n\t\txlabel={Performance ratio $\\tau$},\n\t\t\t\tylabel={Ratio of problems solved},\n\t\t\t\tymin = 0,\n\t\t\t\tymax = 1,\n\t\txmin = 1,\n\t\t\t\txmax = 10000,\n\t\txmode=log,\n\t\t\t\tlegend entries={OSQP, GUROBI, MOSEK},\n\t\t\t\tlegend cell align=left,\n\t\tlegend style={at={(.95,.05)},anchor=south east, fill=white, fill opacity=1, draw opacity=1,text

<!-- chunk {"id": "body-0193", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

opacity=1},\n\t\tlog ticks with fixed point,\n\t\t\t\tevery axis plot/.append style={very thick}\n\t\t\t\t]\n\t\t\\addplot [osqp, \\osqplinestyle] table[x=tau, y=OSQP_high, col sep=comma] {data/results/maros_meszaros_problems_high_accuracy/performance_profiles.csv};\n\t\t\\addplot [gurobi, \\gurobilinestyle] table[x=tau, y=GUROBI_high, col sep=comma] {data/results/maros_meszaros_problems_high_accuracy/performance_profiles.csv};\n\t\t\\addplot [mosek, \\moseklinestyle] table[x=tau, y=MOSEK_high, col sep=comma]

<!-- chunk {"id": "body-0194", "role": "body", "section": "Support vector machine", "weight": 1.0} -->

{data/results/maros_meszaros_problems_high_accuracy/performance_profiles.csv};\n\t \\end{axis}\n\t\t\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> Maros-Meszaros problems comparison with performance profiles.
