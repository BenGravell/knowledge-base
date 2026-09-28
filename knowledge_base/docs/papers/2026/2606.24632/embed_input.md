<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Parallel Dynamic Programming for Conic Linear Quadratic Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Linear Quadratic (LQ) control problems are at the heart of linear control theory and Model Predictive Control (MPC). While performant, standard approaches to solving such problems are inherently serial, limiting real-time scalability despite the parallel computing power available on modern multi-core CPUs. Contributing to addressing this challenge and motivated by ``divide and conquer'' strategies, we present a parallel-in-time approach that solves computationally demanding conic optimal control problems through the use of the alternating direction method of multipliers (ADMM). In particular, we formulate the inner primal update of ADMM as an LQ problem and split the reformulated problem along the time horizon. This enables us to derive a variant of the Riccati recursion using dynamic programming to solve each subproblem in parallel. Numerical benchmarks on two real-world applications demonstrate as much as a 5x speedup compared to existing related approaches on multi-core CPU hardware.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model Predictive Control (MPC) has become increasingly popular in practice due to its ability to adapt to dynamic environments and systematically handle complex constraints, e.g., second-order conic constraints that commonly appear in robotics and aerospace control problems involving friction and thrust limits. These algorithms operate by repeatedly solving finite-horizon optimal control problems online. Fueled by advances in numerical optimization solvers, real-time conic nonlinear MPC is now practical for many robotics tasks and modalities.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In most efficient MPC implementations, the key computational primitive is the Linear-Quadratic (LQ) problem. This includes both historic and modern iterative schemes such as Sequential Quadratic Programming (SQP) and Differential Dynamic Programming (DDP). In most of these approaches, the resulting LQ (sub)problem can be interpreted as a quadratic optimization problem subject to linear dynamics constraints. Its corresponding KKT system exhibits a banded structure, which can be solved using a sparse $LDL^{\top}$ factorization, or an efficient Riccati recursion inspired by dynamic programming. We note that, as discussed in Jordana et al., the two approaches are closely related, and many variants, such as the square-root Riccati recursion, have been proposed for further efficiency.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, the complexity of the aforementioned methods scales linearly with the length of the prediction horizon and becomes a bottleneck in long-horizon problems. Moreover, while current solvers for (conic) trajectory optimization are serial, recent advances in parallel computing motivate the development of new parallel algorithms for such problems. One key class of such parallel algorithms is "divide and conquer" approaches, which decompose the problem into smaller subproblems that can be solved independently, followed by a consensus step that combines their partial solutions. In particular, Wright proposes two such methods, partitioned dynamic programming (PDP) and partitioned Riccati recursion (PRI), which differ in their treatment of the system of equations associated with the LQ problem, and in the way they parameterize the subproblems. There are multiple variants and extensions to these approaches; in particular, Jallet et al. consider general LQ problems with implicit dynamics and stage-wise equality constraints, and under explicit dynamics, apply a reduction phase that coincides with that of the PDP method. Table 1 summarizes the comparison among these various methods.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nielsen and Axehill,2015 Table 1: Comparison of parallel methods.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the advances achieved, with the exception of Jallet et al., the aforementioned methods do not account for constraints at all, let alone conic constraints. We build on this previous work and introduce a new LQ solver which is not only more computationally efficient through its parallel-in-time approach, but can also solve large-scale conic optimal control problems through the alternating direction method of multipliers (ADMM) for constraint handling. In particular, we decompose the ADMM primal problem into parallel fixed-end LQ subproblems, which we solve through our own variant of the Riccati recursion, achieving increased computational efficiency. Compared to related and common approaches for solving such problems, we demonstrate as much as a 5x speedup on multi-core CPU hardware.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Dense Linear Algebra", "weight": 1.0} -->

This work uses the following dense linear algebra operations: matrix-matrix/vector multiplication $(\texttt{gemm}/\texttt{gemv})$, triangular matrix-matrix/vector multiplication $(\texttt{trmm}/\texttt{trmv})$, symmetric rank-$k$ update $(\texttt{syrk})$, Cholesky factorization, triangular solve $(\texttt{trsv})$, as well as LU factorization and solve. More technical details can be found.

<!-- chunk {"id": "body-0009", "role": "body", "section": "The Conic LQ Problem", "weight": 1.0} -->

We solve via an ADMM-based approach, where the core idea is to separately handle the dynamics and conic constraints to simplify the optimization process, as described below.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Conic ADMM", "weight": 1.0} -->

Following Garstka et al., we reformulate as: where $\tilde{x}_{k}$ and $\tilde{u}_{k}$ are auxiliary variables achieving consensus with $x_{k}$ and $u_{k}$, respectively, through (2d) and (2f). The indicator function $I_{\mathcal{K}}$ of the set $\mathcal{K}$ in (2b) integrates the conic constraints into the objective. The ADMM algorithm solves problem through the following three-step iteration: where (3a) represents an unconstrained LQ problem that minimizes the augmented Lagrangian $\mathcal{L}_{\rho,\sigma}$ over $\tilde{\boldsymbol{x}}$ and $\tilde{\boldsymbol{u}}$, subject to linear dynamics.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Conic ADMM", "weight": 1.0} -->

The expression for the augmented Lagrangian is given: where the parameters $\rho>0$ and $\sigma>0$ act as regularization or step-size terms, and $\boldsymbol{y}$ is the vector of dual variables associated with the stage-wise constraints (2c). (3b) projects $\boldsymbol{s}$ into $\mathcal{K}$, and (3c) updates the dual variables. The $j$ superscript denotes the ADMM iteration index. An intermediate constraint relaxation step is often included between (3a) and (3b), which for the running variables takes the following form: where $\alpha\in$ is the relaxation parameter. If $\alpha>1$, imposes over-relaxation, with demonstrated improved convergence using $\alpha$ values in the range $1.5-1.8$. In our implementation, the relaxation parameter is set to $\alpha=1.6$, following Stellato et al..

<!-- chunk {"id": "body-0012", "role": "body", "section": "The LQ Problem", "weight": 1.0} -->

In (3a), we solve an LQ problem, which arises not only in ADMM-type methods but is also compatible with alternative constraint-handling approaches, including interior-point methods and proximal augmented Lagrangian methods. To match the quadratic form of the cost function, we reformulate the augmented Lagrangian in as a function of terms of the following cost matrices: We highlight the linear algebra routines and floating-point operation (flop) counts in blue for reference, with additional context provided in the following section.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Parallel LQ Solver", "weight": 1.0} -->

Our parallel algorithm to address (3a) comprises a backward pass and a forward pass. The backward pass includes two phases, namely the reduction and consensus phases, as illustrated in Figure 1. The forward pass involves a parallel rollout of the linear dynamics. This section focuses on the methods applied in the backward pass.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Parallel LQ Solver", "weight": 1.0} -->

We adopt a divide-and-conquer strategy to parallelize the computation of (3a). In particular, we break down the LQ problem along the prediction horizon into $J$ similar subproblems $\{\mathcal{P}_{i}\}_{i=0}^{J-1}$. Let $N_{i}$ and $k_{i}$ denote the horizon length and starting stage of the $i$-th subproblem. We then define the state and input sequences for subproblem $i$ as: Two consecutive subproblems, $\mathcal{P}_{i}$ and $\mathcal{P}_{i+1}$, are linked by the condition $x_{N_{i},i}=x_{0,i+1}$, ensuring continuity between the final state of $\mathcal{P}_{i}$ and the initial state of $\mathcal{P}_{i+1}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Parallel LQ Solver", "weight": 1.0} -->

Therefore, in addition to the initial state $x_{0,i}$, we also parameterize each subproblem by its terminal state $x_{N_{i},i}$, resulting in a fixed-end LQ problem $\mathcal{P}_{i}(x_{0,i},x_{N_{i},i})$: where $\boldsymbol{\hat{x}}_{i}=\left(x_{1,i},\dots,x_{N_{i}-1,i}\right)$ is the state sequence, excluding the initial and terminal states.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Parallel LQ Solver", "weight": 1.0} -->

In the remainder of this section, we describe the stages of our algorithm in detail and occasionally omit the subscript $i$ and the hat symbol for notational simplicity.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Reduction Phase", "weight": 1.0} -->

By dualizing the dynamics constraint coupling the terminal and second last stages, we reformulate as follows: where $x_{0}$ and $x_{N}$ are treated as parameters. The inner minimization problem in resembles a standard LQ problem with no terminal cost, but includes an additional term arising from the terminal state constraint.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Reduction Phase", "weight": 1.0} -->

We then apply dynamic programming to solve the inner optimization problem, starting from the minimization problem at stage $N-1$, where $g_{N-1,N}$ denotes the conditional dual value function from stage $N-1$ to $N$: | | | $\displaystyle+\lambda_{N}^{\top}\left(A_{N-1}x_{N-1}+B_{N-1}u_{N-1}-x_{N}\right).$ | | | By analytically solving the unconstrained problem above, we derive the mathematical expression for the conditional dual value function from stage $n$ to $N$ as follows: | | | $\displaystyle g_{n,N}(x_{n},x_{N},\lambda_{N})=\beta+\frac{1}{2}x_{n}^{\top}P_{n,N}x_{n}+p_{n,N}^{\top}x_{n}$ | | \(11\) | |

<!-- chunk {"id": "body-0019", "role": "body", "section": "Reduction Phase", "weight": 1.0} -->

$\displaystyle=A_{n+1,N}c_{n}+c_{n+1,N}.$ | | | Next, by setting the gradient of $Q_{n}$ to zero, we solve the minimization problem to obtain the optimal control input $u_{n}^{*}$ and the conditional dual value function $g_{n,N}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Reduction Phase", "weight": 1.0} -->

The optimal control input is then: Substituting $u_{n}^{*}$ into the action-value function, we obtain the key components of $g_{n,N}$: Solving the first-stage minimization problem, we obtain the conditional value function $V_{i}$ for subproblem $i$ by maximizing the conditional dual value function over the dual variable $\lambda_{N_{i}}$: which represents the optimal cost of the trajectory, conditioned on the initial and terminal states. If the terminal state is not reachable, the value function tends toward infinity. To simplify the notation, we introduce the following: For the last subproblem, we define $\mathcal{T}_{J-1}:=\left(P_{J-1},p_{J-1}\right)$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Reduction Phase", "weight": 1.0} -->

The full reduction phase is shown in Algorithm 1, with the linear algebra operation and the flop counts highlighted in blue, including only the cubic and quadratic terms. In Algorithm 1 (Lines 7-11), instead of directly implementing, we adopt the square-root Riccati recursion proposed, where the recursion is expressed in terms of the Cholesky factor $L_{nn,x}$ rather than $P_{n}$. This method reduces the flop counts and improves spatial locality in the cache by packing the matrices. The computational cost of the stage factorization is summarized in Table 2. We highlight in bold the additional floating-point operations required by the stage factorization in the fixed-end reduction. Moreover, during the reduction phase, we perform $J$ backward passes in parallel. If the whole LQ problem is evenly divided, the computational load differs between the first $J-1$ backward passes and the final one. Specifically, the last backward pass employs the standard Riccati recursion, by excluding Lines 17-25. To minimize unnecessary lag time, we balance the computational load by increasing the horizon length of the final subproblem.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Reduction Phase", "weight": 1.0} -->

Let $\psi$ denote the ratio between the computation time of the stage factorization in the fixed-end reduction (Lines 7-25) and that in the free-end reduction (Lines 7-16). Assuming that all CPUs have identical computing capabilities, we determine the horizon length $N^{\prime}$ of the first $J-1$ subproblems as follows, by equating the computation time of the first subproblem with that of the last one: which we denote as a load-balancing scheme.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Consensus Phase", "weight": 1.0} -->

Next, we aim to combine the subproblems by considering a minimization problem associated with all linkage states. Let the linkage state sequence be denoted as: $\boldsymbol{x}^{\text{lk}}=(x^{\text{lk}}_{1},\dots,x^{\text{lk}}_{J-1}):=(x_{k_{1}},\dots,x_{k_{J-1}}).$ The optimization problem is then formulated as: where $x^{\text{lk}}_{0}$ is defined as $x_{0}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Consensus Phase", "weight": 1.0} -->

By substituting into, we derive a min-max problem over the linkage states and corresponding dual variables: where $\boldsymbol{\lambda}^{\text{lk}}=(\lambda^{\text{lk}}_{1},\dots,\lambda^{\text{lk}}_{J-1}):=(\lambda_{N_{0}},\dots,\lambda_{N_{J-2}})$. The optimality conditions for are obtained by taking the gradient of the objective function with respect to $\boldsymbol{x}^{\text{lk}}$ and $\boldsymbol{\lambda}^{\text{lk}}$, yielding the following system of equations: Leveraging the special structure of the resulting banded KKT matrix, we perform a backward elimination to establish the relationship between $x_{i}$ and $\lambda_{i}$: where $P_{i}$ and $p_{i}$ are the parameters associated with the value function of an LQ problem.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Consensus Phase", "weight": 1.0} -->

During the backward pass, the connection between two consecutive states is: Once $\{P_{i}\}$ and $\{p_{i}\}$ are computed, we use and to obtain the linkage states and Lagrangian dual variables. The consensus phase is described in Algorithm 2. Unlike, our method only requires $P_{i,i+1}$ to be positive semi-definite rather than positive definite, at the cost of approximately $2n_{x}$ additional flop counts per stage.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Consensus Phase", "weight": 1.0} -->

(a) quadrotor hovering control (b) low-thrust orbital transfer planning Figure 2: Benchmarking results across various horizon lengths. Above-bar numbers indicate the speedups achieved by our PDPLQR solver over realted work. In the quadrotor hovering control experiment, load balancing is turned off.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

The objectives of this numerical study are threefold: to evaluate the computational performance of the proposed solver across a wide range of horizon lengths, to examine the effects of varying the number of subproblems and stage constraints, and to validate the effectiveness of the proposed load-balancing scheme via. In addition, we compare the performance of our parallel solver PDPLQR against several high-performance, state-of-the-art, LQ solvers: one based on the square-root Riccati recursion adopted in acados and identified as Riccati LQR, the proximal LQ solver (ProxLQR) integrated in Aligator, and the widely used sparse linear solver QDLDL.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

All simulations are conducted, using Google Benchmark, on a laptop with a $2.30\text{\,}\mathrm{GHz}$ Intel Core i7-11800H processor (8 physical cores) and $16\text{\,}\mathrm{GB}$ RAM. We implement our parallel method in C++ using Eigen for dense linear algebra. The OpenMP API is used to enable parallel execution. To minimize the overhead of online thread creation, all threads are created and bound to specific CPU cores during the problem setup. We disable Turbo Boost for stable thermal performance during benchmarking. Moreover, for a fair comparison, we use Aligator v0.16.0, which is optimized for explicit dynamics.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Benchmarking Results", "weight": 1.0} -->

For benchmarking, we focus on two real-world engineering problems: (a) quadrotor hovering control representing a short-horizon case and (b) low-thrust orbital transfer planning representing a long-horizon case. The quadrotor model is linearized around the hovering condition, with 12 states $(n_{x}=12)$ and 4 control inputs $(n_{u}=4)$. We enforce box constraints on the state and input variables, resulting in $n_{c,k}=16$ constraints per stage. The orbital dynamics model is adopted, consisting of 13 states and 2 control inputs. The imposed stage constraint requires that the $\ell$-2 norm of the control input vector $u_{k}$ remains below a specific bound, $\|u_{k}\|_{2}\leq u_{\max}$. This is a typical second-order cone constraint.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

We now delve into assessing the backward pass (Algorithm 1), which is the most computationally demanding component of the LQ-problem solution process. Table 2 shows that solving the fixed-end LQ problem is more computationally expensive than its free-end counterpart. By substituting $n_{x}=12,n_{u}=4,n_{c}=0$ into Table 2, we can estimate that the ratio between the flop counts of the fixed-end and free-end stage factorizations is $2.08$. This value implies that splitting the horizon evenly into two parts offers little computational advantage. To validate this finding, we measure the computation time of the backward pass for the Riccati LQR and our parallel solver, PDPLQR. The results for the problem with $N=20$ are shown in Figure 3. As expected, dividing the LQ problem into three subproblems reduces the computation time.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

However, we note that it is not beneficial to use an excessive number of threads for short-horizon problems $(N\leq 20)$ since the factorization in the consensus phase often incurs a higher computational cost than that in the reduction phase, as indicated in Table 2. Next, we turn to the constrained LQ problem. As illustrated on the right side of Figure 3, all parallel solvers outperform the Riccati LQR, since the flops associated with the stage constraints, $(n_{x}+n_{u})^{2}n_{c}$, offset the additional computational cost introduced by the fixed-end formulation. Overall, our method is effective for short-horizon problems with a large number of constraints and when properly choosing the number of segments.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Next, we investigate the effect of the load-balancing technique on the long-horizon problem introduced in Section 3.1. With the horizon length fixed at $2000$, we vary the number of subproblems. Without load balancing, the solve times (ms) were 11.26, 5.61, 3.88, and 3.01 for $J=2$, $4$, $6$, and $8$, respectively. Incorporating load balancing reduced these to 8.81, 4.95, 3.56, and $2.87\text{\,}\mathrm{m}\mathrm{s}$, corresponding to improvements of $21.7\%$, $11.7\%$, $8.1\%$, and $4.9\%$. The load-balancing effect becomes negligible, as the value of $N^{\prime}$ is close to the evenly divided horizon length.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we demonstrate that temporal parallelization on multi-core CPUs enables efficient solutions to LQ problems for optimal control problems with various horizon lengths. In the future, we plan to extend our open-source solver to support additional constraint-handling methods, including proximal augmented Lagrangian methods and interior-point methods, and to adapt it to other parallel computing architectures like GPUs.

<!-- chunk {"id": "body-0034", "role": "body", "section": "DECLARATION OF GENERATIVE AI AND AI-ASSISTED TECHNOLOGIES IN THE WRITING PROCESS", "weight": 1.0} -->

ChatGPT helped to enhance the writing quality of this work. Nonetheless, the authors reviewed and edited the manuscript throughout the full writing process, and assume full responsibility for the content of this publication.
