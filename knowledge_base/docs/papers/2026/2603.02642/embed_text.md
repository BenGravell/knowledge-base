<!-- arxiv-full-text:v1 {"arxiv_id": "2603.02642", "source": "arxiv-html"} -->

## Introduction

Trajectory optimization has become a foundational tool for motion planning and control of robotic systems, enabling robots to compute dynamically feasible paths that minimize objective cost while satisfying constraints. Applications span from manipulation and legged locomotion to aerial vehicles and autonomous driving. However, real-world robotic systems inevitably face uncertainty. When constraints encode safety-critical requirements---such as obstacle avoidance or actuator limits---failing to account for these uncertainties can lead to catastrophic consequences.

Handling uncertainty is critical for real-world deployment. One common approach is to model uncertainty as a stochastic disturbance characterized by a probability distribution. Existing methods, ranging from chance-constrained optimization to covariance steering, provide probabilistic guarantees on constraint satisfaction. However, stochastic models may not capture all uncertainty types; modeling inaccuracies or exogenous disturbances are often better represented as deterministic uncertainty, referring to disturbances assumed to lie within a bounded set. In many safety-critical applications, a guarantee is required for all possible realizations of such uncertainty. This work addresses trajectory optimization in the presence of these deterministic disturbances.

Figure 1: cuNRTO on a 7-DoF Franka manipulator: cuNRTO involves an outer successive linearization (SL) loop run on the host CPU, with an inner loop executed on the GPU. Compared to NRTO, cuNRTO achieves a 25.9× wall-clock speedup on this setting with 100% constraint satisfaction. The three small boxes show the final state under Monte Carlo rollouts.

Standard approaches to address deterministic uncertainty involve providing worst-case guarantees over bounded uncertainty sets, a concept originating from the field of robust control. This idea has been adapted for trajectory optimization in several forms, ranging from Tube-based and Robust Model Predictive Control (MPC) to min-max methods. Tube-based MPC computes a nominal trajectory and feedback gains to maintain the system within a safe tube; but can be overly conservative due to the decoupling between the nominal control and the feedback gains. Robust MPC typically considers linear systems, and Min-Max DDP frame the problem as a game against an adversarial disturbance to optimize a robust policy, failing to address nonlinear state constraints. While DIRTREL studies robust nonlinear direct transcription under ellipsoidal disturbances with an LQR tracking controller, it assumes uncorrelated uncertainty across the time-steps. To effectively handle both nonlinear dynamics and state constraints, recent research has shifted toward Robust Optimization (RO). Some frameworks in this category address nonlinear constraints but are limited to linear dynamical systems. Conversely, recent work introduced the Nonlinear Robust Trajectory Optimization (NRTO) framework, a trajectory optimization framework that accounts for nonlinearity in both the dynamics and the constraints.

The NRTO framework comprises three core elements: successive linearization, robust constraint reformulation, and the resolution of linearized subproblem infeasibility via operator-splitting techniques. Since the framework enforces robust constraints that must be satisfied for every possible realization of uncertainty within a bounded set, the problem is intractable in its original form due to the infinite number of constraints. To overcome this, the NRTO framework employs robust constraint reformulation, converting the problem into a tractable form that yields Second-Order Conic Programming (SOCP) constraints. Despite the effectiveness of this framework, the computational cost of the existing implementation based on Interior Point (IP) methods for solving the SOCP subproblems remains a primary barrier to its widespread adoption for high-dimensional systems with numerous constraints.

Leveraging GPU acceleration offers a powerful solution to overcome these computational barriers. As single-core CPU performance has largely plateaued, the robotics community has increasingly turned to massively parallel architectures to accelerate complex motion planning tasks. Early research in this domain focused primarily on parallelizing rigid body dynamics and their corresponding gradients. More recently, GPU acceleration has been pushed into the optimization loop itself. For example, MPCGPU achieves real-time nonlinear MPC by accelerating the dominant sparse Newton solve (PCG) on the GPU. Similar GPU-parallelism has also been explored in constrained sampling-based planning.

Beyond nonlinear MPC, GPU implementations of first-order splitting methods for convex programs, particularly ADMM-based QP solvers such as OSQP, achieve high throughput by mapping the repeated linear algebra and projection steps to GPU kernels while keeping iterates on-device. However, the NRTO framework in its current form is not inherently amenable to parallelization.

This paper presents cuNRTO: a GPU-accelerated nonlinear robust optimization framework by introducing two novel extensions to the original NRTO formulation. This enables efficient parallel execution. Fig. 1 provides a high-level overview of the cuNRTO execution flow. Specifically, the contributions of this paper are three-fold: First, we introduce NRTO-DR, a minimal-change methodology to solve the computationally expensive sub-problems of the NRTO framework using Douglas-Rachford splitting (DR). The proposed methodology improves the performance over Interior Point (IP) Methods through parallel SOC projections and sparse direct solves that reduce matrix operations.

Second, we propose NRTO-FullADMM, a novel variant of the NRTO framework that could fully leverage GPU acceleration. By restructuring the inner ADMM update blocks, this framework integrates SOCP projections directly into the inner loop eliminating extra DR layer and host-device communication overhead.

Third, we develop cuNRTO, which constitutes GPU implementation of the NRTO-DR and NRTO-FullADMM. Our approach utilizes cuBLAS GEMM chains for the feedback gain update and custom CUDA kernels for SOC projections. We validate our approach on unicycle, quadcopter, and Franka manipulator trajectory optimization, demonstrating a speedup of up to 139.60$\times$.

### I-A Notations

The space of symmetric positive definite (semi-definite) matrices with dimension $n$ is denoted as $\mathbb{S}^{++}_{n}$ ($\mathbb{S}^{+}_{n}$). The 2-norm of a vector ${\bm{x}}$ is denoted with $\|{\bm{x}}\|_{2}$, while the Frobenius norm of a matrix ${\bf X}$ is given by $\|{\bf X}\|_{F}$. The indicator function of a set $X$, $\pazocal{I}_{X}$ is defined as $\pazocal{I}({\bf x})=\{0$ if ${\bm{x}}\in X$ or $+\infty$ if ${\bm{x}}\notin X\}$. With $\llbracket a,b\rrbracket$, we denote the integer set $\{[a,b]\cap\mathbb{Z}\}$.

### I-B Organization of the paper

The remainder of this paper is organized as follows. Section II presents the problem statement and a detailed overview of the Nonlinear Robust Trajectory Optimization (NRTO) framework. In Sections III and IV, we introduce our core architectural contributions: NRTO-DR and NRTO-FullADMM, respectively. Section V demonstrates the computational performance of these proposed frameworks through a series of simulation experiments involving unicycle, quadcopter, and Franka Emika manipulator models. Finally, Section VI provides concluding remarks and discusses future work.

## Nonlinear Robust Trajectory Optimization Framework

In this section, we outline the nonlinear robust trajectory optimization framework (NRTO) considered in this work. We start by presenting the problem statement followed by framework details.

### II-A Problem Statement

Consider the following discrete-time nonlinear dynamics where ${\bm{x}}_{k}\in\mathbb{R}^{n_{x}}$ is the state, ${\bm{u}}_{k}\in\mathbb{R}^{n_{u}}$ is the control input, $f:\mathbb{R}^{n_{x}}\times\mathbb{R}^{n_{u}}\rightarrow\mathbb{R}^{n_{x}}$ is the known dynamics function and $T$ is the time horizon. The initial state ${\bm{x}}_{0}$ consists of a known part $\bar{{\bm{x}}}_{0}$, as well as an uncertain part $\bar{{\bm{d}}}_{0}$. The terms $\bar{{\bm{d}}}_{0},{\bm{d}}_{k}\in\mathbb{R}^{n_{x}}$ represent unknown disturbances. Considering ${\bm{\zeta}}=[\bar{{\bm{d}}}_{0};{\bm{d}}_{0};\dots;{\bm{d}}_{T-1}]\in\mathbb{R}^{(T+1)n_{x}}$, the uncertainty vector ${\bm{\zeta}}$ is characterized to lie inside a bounded ellipsoidal set defined as follows | | $\displaystyle\pazocal{U}[\tau]=\{{\bm{\zeta}}|~\exists({\bm{z}}\in\mathbb{R}^{n_{z}},$ | $\displaystyle\tau\in\mathbb{R}^{+}):$ | | \(3\) | | | | $\displaystyle~{\bm{\zeta}}={\mathbf{\Gamma}}{\bm{z}},~{\bm{z}}^{\mathrm{T}}{\bf S}{\bm{z}}\leq\tau\},$ | | | where ${\mathbf{\Gamma}}\in\mathbb{R}^{(T+1)n_{x}\times n_{z}}$, and ${\bf S}\in\mathbb{S}^{++}_{n_{z}}$. Further, the proposed methodology can be extended for other common types of uncertainty sets such as ellitopes, polytopes, etc..

Consider affine control policies of the following form where $\bar{{\bm{u}}}_{k}\in\mathbb{R}^{n_{u}}$ is feed-forward control and ${\bf K}_{k}\in\mathbb{R}^{n_{u}\times n_{x}}$ are feedback gain. By convention, we set ${\bm{d}}_{-1}=\bar{{\bm{d}}}_{0}$.

The system is subject to robust state and control constraints that should be satisfied for all possible disturbance realizations ${\bm{\zeta}}$ within the uncertainty set $\pazocal{U}[\tau]$, which are defined as where ${\bm{x}}=[{\bm{x}}_{0};{\bm{x}}_{1};\dots;{\bm{x}}_{T}]$, ${\bm{u}}=[{\bm{u}}_{0};{\bm{u}}_{1};\dots;{\bm{u}}_{T-1}]$, ${\bm{g}}:\mathbb{R}^{(T+1)n_{x}}\rightarrow\mathbb{R}^{n_{g}}$, ${\bm{h}}:\mathbb{R}^{Tn_{u}}\rightarrow\mathbb{R}^{n_{h}}$. Further, $g_{i}$ is concave or linear, and $h_{i}$ is linear.

Subsequently, the nonlinear robust trajectory optimization problem addressed in this work is presented.

### Problem 1 (Robust Trajectory Optimization Problem)

Find the optimal control policy $\{\bar{{\bm{u}}}_{k},{\bf K}_{k}\}_{k=0}^{T-1}$ such that

### II-B NRTO Algorithm

In this section, we provide an outline of the NRTO framework, which integrates successive linearization, robust constraint reformulation, and Alternating Direction Method of Multipliers (ADMM). For the simplicity of analysis, we present the problem in terms of the variable ${\bm{k}}_{v}\in\mathbb{R}^{Tn_{u}n_{x}}$ defined as ${\bm{k}}_{v}=[{\bm{k}}_{v,0};{\bm{k}}_{v,1};\dots;{\bm{k}}_{v,T-1}]$ with ${\bm{k}}_{v,k}=\text{vec}({\bf K}_{k})$.

NRTO is a bi-level algorithm as shown in Fig. 2. In the outer loop of the algorithm, the problem is linearized around a nominal trajectory $\hat{{\bm{u}}},\hat{{\bm{x}}}$ and converted into a tractable form. This results in Second Order Conic Programming (SOCP) constraints as shown below.

### Problem 2 (Tractable Linearized Problem)

Find the optimal decision variables $\delta\hat{{\bm{u}}},{\bm{k}}_{v},{\bm{p}}$ such that where the functions $\pazocal{Q}_{\hat{u}}(\delta\hat{{\bm{u}}})$, $\tilde{\pazocal{Q}}({\bm{k}}_{v})$, ${\bm{g}}^{\text{lin},1}(\delta\hat{{\bm{u}}},{\bm{p}})$, the matrices $\hat{{\bf A}}_{j}\in\mathbb{R}^{n_{z}\times Tn_{u}n_{x}}$, $\hat{{\bm{b}}}_{j}\in\mathbb{R}^{n_{z}}$, ${\bf F}_{u}\in\mathbb{R}^{(T+1)n_{x}\times Tn_{u}}$ are defined in Section I of Supplementary Material (SM). Further, $r_{\text{trust}}\in\mathbb{R}^{+}$ is the trust region radius.

This linearized problem can be infeasible due to linearization, especially during the initial iterations of the algorithm. Thus, the problem is solved indirectly using ADMM in the inner loop (refer to Algorithm 1 of for details). For which, Problem 2. ‣ II-B NRTO Algorithm ‣ II Nonlinear Robust Trajectory Optimization Framework ‣ cuNRTO: GPU-Accelerated Nonlinear Robust Trajectory Optimization") is converted to the following form solvable using ADMM, by introducing a slack variable $\tilde{p}$, Figure 2: Overview of NRTO Framework: A bi-level structure involving an outer successive linearization (SL) loop to generate tractable linearized problem, and an inner ADMM loop to solve the resulting linearized problem.

### Problem 3 (Tractable Linearized Problem - ADMM form)

Find the optimal decision variables $\delta\hat{{\bm{u}}},{\bm{k}}_{v},{\bm{p}},\tilde{{\bm{p}}}$ such that where $\pazocal{H}_{p}(\delta\hat{{\bm{u}}},{\bm{p}})$, $\pazocal{H}_{\tilde{p}}({\bm{k}}_{v},\tilde{{\bm{p}}})$ can be referred.

The above problem is solved using ADMM by considering the variables $\{{\bm{k}}_{v},\tilde{{\bm{p}}}\}$ as the first block, and $\{\delta\hat{{\bm{u}}},{\bm{p}}\}$ as the second block of ADMM. Each iteration of the ADMM (indexed by $l_{\text{in}}$) involves sequential minimization of the Augmented Lagrangian (AL) of the problem with respect to each block variables, followed by a dual update, given as follows where the AL of the problem $\pazocal{L}_{\rho}(\delta\hat{{\bm{u}}},{\bm{p}},{\bm{k}}_{v},\tilde{{\bm{p}}};{\bm{\lambda}})=\pazocal{H}_{p}(\delta\hat{{\bm{u}}},{\bm{p}})+\pazocal{H}_{\tilde{p}}({\bm{k}}_{v},\tilde{{\bm{p}}})+{\bm{\lambda}}^{\mathrm{T}}({\bm{p}}-\tilde{{\bm{p}}})+\frac{\rho}{2}\|{\bm{p}}-\tilde{{\bm{p}}}\|_{2}^{2}$, with ${\bm{\lambda}}\in\mathbb{R}^{n_{g}}$ being the dual variable for the constraint ${\bm{p}}=\tilde{{\bm{p}}}$ and $\rho>0$ as the penalty parameter. For the complete details of the NRTO algorithm, the reader is referred to.

### II-C NRTO-LE Algorithm

This section outlines NRTO-LE, an extension of the NRTO framework developed to address linearization error. While the standard NRTO algorithm ensures that a linearized trajectory satisfies all the constraints, it may not guarantee the safety of the actual trajectory when the linearization error is significant. To address this, NRTO-LE models the linearization error at each time step as a bounded uncertainty lying inside an ellipsoidal set. For the comprehensive derivation of the modification, the reader is referred to.

## NRTO-DR Framework

In this section, we introduce a framework for accelerating the solving of the sub-problem (7a) which is the most computationally expensive update in the inner loop of the NRTO. Subsequently, we provide a GPU version of the framework that could further enhance the computational speed. The design goal of NRTO-DR is to make the smallest algorithmic change to NRTO while replacing the expensive interior-point SOCP subsolve in (7a). By rewriting this block with Douglas-Rachford splitting, the update decomposes into reusable sparse linear solves and independent SOC projections, exposing the parallelism needed for GPU acceleration. We begin by explicitly writing the ADMM update step (7a) as follows | | $\displaystyle\min_{{\bm{k}}_{v},\tilde{{\bm{p}}}}$ | $\displaystyle\tilde{\pazocal{Q}}({\bm{k}}_{v})+\tfrac{\rho}{2}\big\|\tilde{{\bm{p}}}-{\bm{p}}^{l_{\text{in}}-1}-{\bm{\lambda}}^{l_{\text{in}}-1}/\rho\big\|_{2}^{2}$ | | \(8\) | | | s.t. | $\displaystyle\|\hat{{\bf A}}_{j}{\bm{k}}_{v}+\hat{{\bm{b}}}_{j}\|_{2}\leq\tilde{p}_{j},\qquad j\in\llbracket 1,n_{g}\rrbracket$ | | |

### III-A Framework

We introduce a framework leveraging Douglas-Rachford Splitting (DR) to reduce the computational complexity of solving the above problem. To achieve this, the problem needs to be transformed to a form solvable by DR method. Let us define ${\bm{\chi}}=[{\bm{k}}_{v};\tilde{{\bm{p}}}]$ and a slack variable ${\bm{s}}$ such that can be equivalently given as follows - | | $\displaystyle\min_{{\bm{\chi}},{\bm{s}}}$ | $\displaystyle\tfrac{1}{2}{\bm{\chi}}^{\mathrm{T}}{\bf P}{\bm{\chi}}+{\bm{q}}^{\mathrm{T}}{\bm{\chi}}$ | | \(9\) | | | s.t. | $\displaystyle{\bf A}{\bm{\chi}}+{\bm{s}}=\mathbf{b},\qquad{\bm{s}}\in\pazocal{K},$ | | | with ${\bf P}=\mathrm{blkdiag}({\bf Q}_{v},\rho{\bf I})$ and a product of SOCs $\pazocal{K}=\pazocal{K}_{1}\times\cdots\times\pazocal{K}_{n_{g}}$. We provide the explicit construction of ${\bf A},\mathbf{b}$ and $\pazocal{K}_{i}$ in Section II of SM. The above problem can be rewritten in a form solvable by the DR method as follows where $\pazocal{J}({\bm{\chi}},{\bm{s}})=(1/2){\bm{\chi}}^{\mathrm{T}}{\bf P}{\bm{\chi}}+{\bm{q}}^{\mathrm{T}}{\bm{\chi}}+\pazocal{I}_{{\bf A}{\bm{\chi}}+{\bm{s}}=\mathbf{b}}({\bm{\chi}},{\bm{s}})$ and $\hat{\pazocal{J}}({\bm{s}})=\pazocal{I}_{\pazocal{K}}({\bm{s}})$.

For simplicity, let us also define ${\bm{\xi}}=[{\bm{\chi}};{\bm{s}}]$. The update steps in each iteration of relaxed DR method (indexed as $l_{\text{dr}}$) to solve the above problem can be given as follows where $\alpha\in$ is the relaxation parameter. We will now simplify the above update steps. The update (11a) is a quadratic programming (QP) problem, which can be solved by solving the KKT conditions. This involves solving the following where ${\bf R}_{\chi},{\bf R}_{s}\succ 0$ are fixed proximal scalings, ${\bf L}$ is obtained from the Cholesky decomposition of ${\bf K}_{\mathrm{KKT}}$. The matrix ${\bf K}_{\mathrm{KKT}}$ and the derivation of above update are provided in Section II of the SM. Since ${\bf K}_{\mathrm{KKT}}$ is constant within each iteration of the inner ADMM loop, we factor it once and reuse triangular solves throughout DR.

Now, the update (11c) involves where the projection step $\Pi_{\pazocal{K}_{j}}({\bm{s}}_{\text{ref},j}^{l_{\text{dr}}})$ is defined in Section II of SM, a visual interpretation is provided in Fig. 3.

Figure 3: Three cases of projecting a point $(\hat{t},\hat{{\bm{y}}})$ (red) onto a SOC, illustrated in the (t, ‖y‖2) plane. Left: if $\lVert\hat{{\bm{y}}}\rVert_{2}\leq\hat{t}$, the point is already feasible and remains unchanged after projection (green). Middle: if $\lVert\hat{{\bm{y}}}\rVert_{2}>|\hat{t}|$, the point lies outside the cone and is projected onto the cone boundary, preserving the direction of $\hat{{\bm{y}}}$. Right: if $\lVert\hat{{\bm{y}}}\rVert_{2}\leq-\hat{t}$, the point lies in the opposite cone and the projection collapses to the origin.

The DR iterations are terminated when the fixed-point residual $(r_{\text{dr}})$, defined as $r_{\text{dr}}^{l_{\text{dr}}}:=\|\tilde{{\bm{s}}}^{l_{\text{dr}}}-\tilde{{\bm{s}}}^{l_{\text{dr}}-1}\|_{2},$ is below a specified threshold $\varepsilon_{\text{dr}}$ or when the maximum iteration count $L_{\max}$ is reached.

Figure 4: GPU execution of one relaxed DR iteration: Each iteration involves an affine-set projection (11a), a reflection step (11b), and massively parallel second-order cone projections (11c) that are separable across constraints. The right panel illustrates the GPU mapping: each SOCP constraint block is handled by one warp, the warp scheduler dispatches these warps across streaming multiprocessors, and the grey blocks depict the execution lanes (CUDA cores) that run the warp instructions, with shared memory cache supporting fast projection and vector updates.

### III-B GPU implementation

The GPU implementation of NRTO-DR (Fig. 4) follows the relaxed DR updates (11a)-(11c). The affine set proximal step (11a) reduces to solving a fixed sparse KKT system with coefficient matrix ${\bf K}_{\mathrm{KKT}}$, which is factored once across DR iterations. The details are as follows: The one-time sparse factorization of ${\bf K}_{\mathrm{KKT}}$ and per-iteration triangular solves are performed by cuDSS.

SOC projections are computed by a CUDA kernel. The cone-projection case logic is adapted from the open-source SCS implementation.

All vector operations, such as reflection, updates, and residuals, are handled via cuBLAS and kept on-device.

## NRTO-FullADMM Framework

In this section, we present a framework that accelerates the solving of Problem 2. ‣ II-B NRTO Algorithm ‣ II Nonlinear Robust Trajectory Optimization Framework ‣ cuNRTO: GPU-Accelerated Nonlinear Robust Trajectory Optimization"). Specifically, we propose a novel architecture by modifying the inner ADMM loop of the NRTO framework. We start by rewriting Problem 2. ‣ II-B NRTO Algorithm ‣ II Nonlinear Robust Trajectory Optimization Framework ‣ cuNRTO: GPU-Accelerated Nonlinear Robust Trajectory Optimization") by introducing a slack variable ${\bm{\nu}}$, as follows

### IV-A Framework

We propose a framework to solve the above problem using a scaled form of ADMM. The variables $({\bm{\nu}},\tilde{{\bm{p}}})$ are considered as the first block, and $(\delta\hat{{\bm{u}}},{\bm{p}},{\bm{k}}_{v})$ are as the second block of the inner ADMM loop, with (14c) being the coupling constraints. The AL of the above problem is disclosed in Section III of SM, with the penalty parameter as $\rho$, and $\rho{\bm{\lambda}}_{p},\rho{\bm{\lambda}}_{\nu}$ as the dual variables. Subsequently, we present the update steps in the $(l_{\text{in}}^{th})$ iteration, with the detailed derivation disclosed in Section III of SM.

### Block-1 update

This update can be decoupled with respect to the variables $\{{\bm{\nu}}_{j},\tilde{p}_{j}\}_{j=1}^{n_{g}}$, and is given as follows | | | $\displaystyle({\bm{\nu}}^{l_{\text{in}}}_{j},\tilde{p}_{j}^{l_{\text{in}}})$ | | \(15\) | | | | $\displaystyle~~~~~=\Pi_{\text{SOC}}(\hat{{\bf A}}_{j}{\bm{k}}_{v}^{l_{\text{in}}-1}+\hat{{\bm{b}}}_{j}+{\bm{\lambda}}_{\nu,j}^{l_{\text{in}}-1},p_{j}^{l_{\text{in}}-1}+\lambda_{p,j}^{l_{\text{in}}-1})$ | | | where $\Pi_{\text{SOC}}(\hat{{\bm{y}}},\hat{t})$ represents projection of $(\hat{{\bm{y}}},\hat{t})$ onto the cone $\|{\bm{y}}\|_{2}\leq t$ (shown in Fig. 3). This projection step is similar to the projection involved in (13b) of NRTO-DR framework.

### Block-2 update

The variables $(\delta\hat{{\bm{u}}},{\bm{p}})$ and ${\bm{k}}_{v}$ are decoupled, with the ADMM update steps given as where ${\bm{q}},\pazocal{M},\bar{\pazocal{M}}$, disclosed in Section III of SM, remain constant throughout the inner ADMM loop. The update (16a) is similar to the update step (7b) of NRTO.

### Dual update

The update of the regularized dual variables is given as The inner ADMM loop is terminated when the primal residual $r_{p}:=\|\mathbf{p}^{l_{\text{in}}}-\tilde{\mathbf{p}}^{l_{\text{in}}}\|_{2}$ and the dual residual $r_{d}:=\rho\|\tilde{\mathbf{p}}^{l_{\text{in}}}-\tilde{\mathbf{p}}^{l_{\text{in}}-1}\|_{2}$ fall below their respective thresholds, $\varepsilon_{p}$ and $\varepsilon_{d}$, or when max iterations $L_{\max}$ are reached.

0: $\{\hat{{\bf A}}_{j},\hat{{\bm{b}}}_{j}\}_{j=1}^{n_{g}}$, tol ε, max iters Lmax 1: Form ${\bm{q}},\pazocal{M},\{\bar{\pazocal{M}}_{j}\}_{j=1}^{n_{g}}$ 3: for lin = 0 to Lmax do 5: if (rp ≤ εp and rd ≤ εd) then break 8: return $(\delta\hat{{\bm{u}}},{\bm{k}}_{v},{\bm{\nu}},{\bm{p}},\tilde{{\bm{p}}})$ Algorithm 1 Inner ADMM Loop - NRTO-FullADMM Figure 5: cuNRTO pipeline for NRTO-FullADMM: Each outer SL iteration on the host CPU linearizes the problem, packs the SOCP and QP data, and uploads constants to the GPU once. The FullADMM inner loop runs entirely on-device: (i) batched affine evaluation forms per-constraint inputs, (ii) SOC projections are computed in parallel over j, (iii) Block-2 updates solve the QP and update kv using prepacked operators, and (iv) dual updates and residual checks determine termination.

### IV-B GPU Implementation

An overview of the end-to-end on-device inner ADMM loop pipeline for NRTO-FullADMM is shown in Fig. 5.

The details are as follows

### IV-B1 On-device data layout

We store ${\bm{\nu}}\in\mathbb{R}^{n_{g}\times n_{z}}$ and ${\bm{\lambda}}_{\nu}\in\mathbb{R}^{n_{g}\times n_{z}}$ as contiguous row-major blocks with each row corresponding to one constraint $j$, and ${\bm{p}},\tilde{{\bm{p}}},{\bm{\lambda}}_{p}\in\mathbb{R}^{n_{g}}$ as contiguous vectors. All constant matrices $\{\hat{{\bf A}}_{j},\hat{{\bm{b}}}_{j}\}_{j=1}^{n_{g}}$ as well as ${\bm{q}},\pazocal{M},\bar{\pazocal{M}}$ are uploaded once per outer iteration.

### IV-B2 Block-1

The Block-1 update requires projecting We implement this in two GPU steps. First, affine evaluation. We compute all $\hat{{\bm{y}}}_{j}$ via a sequence of cuBLAS GEMM calls that exploit the structured factorization of $\hat{{\bf A}}_{j}$ through ${\bf M}$, ${\bf U}_{k}$, and ${\bf B}_{k}$, avoiding explicit dense matrix formation. Second, SOC projection. We launch a CUDA kernel that performs the SOC projection for each constraint block in parallel. The projection routine follows the standard SOC projection cases and is adapted from the SCS reference implementation, with modifications for warp-level execution and our batched memory layout. This step is bandwidth-bound and scales linearly with $n_{g}$, it achieves near-ideal parallel efficiency.

### IV-B3 Block-2

The update (16a) is a convex QP with fixed quadratic term and fixed constraints (14a). We solve it using preconditioned conjugate gradient (PCG) with a Jacobi preconditioner. Crucially, its linear algebra is reusable across inner iterations, so any preconditioner is computed once per outer iteration and reused thereafter. The ${\bm{k}}_{v}$ update (16b) is solved via PCG with matrix-free Hessian-vector products, avoiding explicit formation of the dense Hessian matrix.

### IV-B4 Dual updates

Dual updates are vector axpy-style operations. We compute the primal residual $r_{p}$ and dual residual $r_{d}$ on the GPU and terminate when both fall below the tolerance.

### Remark 1

NRTO-FullADMM scales effectively over NRTO and NRTO-DR through two key innovations. First, it replaces the nested structure of NRTO-DR by directly integrating the parallel SOCP block projections into the inner ADMM updates. Second, it eliminates CPU-GPU data transfer bottlenecks by executing the entire inner ADMM loop on the GPU.

Figure 6: Performance comparison on Unicycle model with five obstacles: We compare (a) the baseline NRTO solver, (b) NRTO-DR, and (c) NRTO-FullADMM. All produce collision-free trajectories that satisfy the robust constraints for 2,000 disturbance realizations. The right insets represent the distribution of terminal state realizations for random, edge, and combined rollouts, demonstrating robustness.

Figure 7: Performance comparison on Quadcopter model with five obstacles: We compare (a) NRTO-DR and (b) NRTO-FullADMM; both produce collision-free trajectories for 2,000 disturbance realizations. Insets report the distribution of terminal state realizations under random Monte Carlo, boundary edge-case, and combined disturbances.

TABLE I: Unicycle and quadcopter dynamics. Three independent sweeps vary one factor while holding the others fixed at (T0, τ0, O0). Bold: best; Underline: second-best.

## Simulation

We evaluate cuNRTO, a suite comprising the GPU-accelerated versions of NRTO-DR and NRTO-FullADMM, on unicycle, quadcopter, and Franka manipulator tasks. We provide a comprehensive analysis of the impact of key system parameters, such as time horizon ($T$), uncertainty level ($\tau$), and the number of obstacles, on both constraint satisfaction and wall-clock time in comparison to the baseline NRTO. Furthermore, we highlight the effectiveness of the proposed architectures in addressing complex dynamical systems through a high-dimensional Franka manipulator task.

### V-A Methodology

Results were collected on a high-performance workstation with a 3.06 GHz 60-core Intel Xeon W-3500 CPU and an NVIDIA A100 80GB GPU, running Ubuntu 22.04 and CUDA 12.9. Code was compiled with g++ 11.4.0. We use the same outer-loop parameters for all methods. The baseline NRTO solves subproblems using MOSEK interior-point optimizer with multi-threading enabled. Solver-specific hyperparameters were tuned independently for best performance, and its complete list is provided in Section IV of SM.

The performance is evaluated based on the following: Constraint satisfaction: Constraint satisfaction was verified using Monte Carlo sampling with 1,000 i.i.d. disturbance drawn uniformly from the interior of the uncertainty set, combined with 1,000 reproducible edge cases that probe the boundary of the uncertainty set via convex combinations of worst-case constraint directions. We set fixed seed to ensure the consistency of the sampling across all experiments. The reported satisfaction probability is the fraction of successful rollouts.

Wall-clock time: We report the wall-clock time required for each solver to converge to a feasible solution. Runtimes were measured using C++ std::chrono::high_resolution_clock.

### V-B Performance Evaluation

Trajectory comparisons between the proposed frameworks and the baseline NRTO for the unicycle and quadcopter models are presented in Fig. 6 and Fig. 7, respectively. Further, the computational efficiency is demonstrated in Table I. We report three sweep studies over horizon length $T$, uncertainty level $\tau$, and the number of obstacles for both unicycle and quadcopter. We denote the nominal setting as $(T_{0},\tau_{0},O_{0})=(30,0.05,0)$ and vary one parameter at a time. All experiments use time-step $\Delta k=$ 25 ms for both optimization and rollout.

### V-B1 Horizon Sweep ($T$)

At the nominal horizon $T_{0}=30$, NRTO-FullADMM reduces solve time from 32.137 s to 6.231 s for the unicycle, which is 5.16$\times$ faster, and from 1327.390 s to 98.585 s for the quadcopter, which is 13.46$\times$ faster. At $T=45$, NRTO-FullADMM reaches 6.387 s for the unicycle and 132.484 s for the quadcopter, corresponding to 6.94$\times$ and 13.21$\times$ speedups over NRTO, respectively.

### V-B2 Obstacle Sweep ($Obs$)

As the number of obstacles increases, the number of robust constraints and associated SOC projections grow, and the GPU implementations benefit from the resulting parallelism. At $Obs=5$, NRTO-FullADMM reduces solve time from 30423.523 s to 217.932 s for the unicycle, which is 139.60$\times$ faster, and from 13374.375 s to 199.935 s for the quadcopter, which is 66.89$\times$ faster.

### V-B3 Uncertainty sweep ($\tau$)

As $\tau$ increases, the NRTO success rate decreases, reflecting the increased conservativeness and difficulty of the robust constraints. In contrast, when accounting for linearization error using NRTO-LE, we observe 100% constraint satisfaction across all reported $\tau$ values for both dynamics. Across the sweep, NRTO-FullADMM consistently yields the lowest wall-clock times among the compared methods.

### V-C Source of speedup

For the unicycle task with five obstacles in Fig. 6, NRTO-DR spends most of its runtime on host--device synchronization and linear solves ($43.5\%$ and $32.6\%$), while SOC projections account for only $11.0\%$. A detailed runtime breakdown is provided in Section IV of the SM. By keeping the inner ADMM loop on-device, NRTO-FullADMM reduces synchronization overhead and increases average GPU utilization from $34.9\%$ to $86.5\%$.

### V-D Solution quality

The proposed reformulations achieve significant speedup without compromising solution quality. The visual variations in terminal-state distributions in Fig. 6-7 and the linearization error differences in Table I are due to convergence toward distinct local minima. These variations arise from the sensitivity of successive linearization towards initialization, hyperparameters, and solver tolerances, rather than a degradation of robust feasibility. Consequently, Table I reveals no distinct pattern in linearization errors across the solvers. Furthermore, for the unicycle task (Fig. 6), the objective components $(J_{u},J_{kv})$ for NRTO, NRTO-DR, and NRTO-FullADMM are $(14.624,204.914)$, $(14.932,204.912)$, and $(13.117,207.425)$, respectively (refer to Table II), with less than $0.5\%$ difference across solvers.

Figure 8: Real-world Robotarium rollout with NRTO disturbance-feedback. Four snapshots over time show the executed trajectory using the affine disturbance-feedback policy. The feedback gain significantly reduces accumulated tracking error and steers the robot into the target region despite real-world disturbances and actuation imperfections.

Figure 9: Real-world Robotarium rollout with nominal control only. Using only the nominal sequence leads to substantial drift from the planned path. The resulting tracking error accumulates over time, and the robot fails to reliably satisfy constraints.

TABLE II: Solution quality comparison for unicycle case (Fig. 6). Bold: best; Underline: second-best.

### V-E Real-World Robotarium Experiment

To further demonstrate that the policy can compensate for real-world model mismatch, we deploy NRTO on a Robotarium unicycle robot. The disturbance set is estimated from open-loop rollout residuals, and the resulting NRTO policy applies the affine feedback $u_{k}=\bar{u}_{k}+K_{k}d_{k}$, where $d_{k}$ is estimated online from consecutive state-transition residuals. As shown in Fig. 8--9, the policy substantially reduces accumulated tracking error and steers the robot into the target region, whereas executing the nominal control sequence alone leads to visible drift. Additional details on disturbance estimation are provided in Section V of SM.

### V-F Franka Manipulator Experiment

We evaluate our framework on a 7-DOF Franka Emika Panda manipulator, a high-dimensional system with $n_{x}=14$ joint positions and velocities and $n_{u}=7$ joint torques, as shown in Fig. 10. The task is to drive the end-effector from a nominal configuration to a goal region while satisfying joint position limits, joint velocity limits, torque bounds, and collision avoidance constraints with respect to spherical obstacles in the workspace. Collision constraints are evaluated using Isaac Sim collision spheres. The feedback gain variables scale as $\mathscr{O}\left(Tn_{u}n_{x}\right)$, yielding $\mathbf{K}_{k}\in\mathbb{R}^{7\times 14}$ per timestep, and obstacle avoidance constraints are enforced at every knot point via the end-effector position obtained from forward kinematics. We report experiments across fixed horizon length $T=30$, number of obstacles $n_{\mathrm{obs}}=1$, and robustness level $\tau=0.01$. As shown in Table III, NRTO-FullADMM achieves a 25.9$\times$ wall-clock speedup over NRTO on this Franka setting, indicating the scalability of NRTO-FullADMM.

Figure 10: NRTO-FullADMM on Franka Manipulator Task: Left: end-effector trajectory with disturbance rollouts (green) toward the goal region (cyan) while avoiding obstacles (gray). Right: qualitative visualization of the motion in Isaac Sim.

TABLE III: Franka manipulator dynamics with fixed setting (T, τ, Obs) = (30, 0.01, 1). best; second-best.

## Conclusion

We introduced cuNRTO, a GPU-accelerated implementation of nonlinear robust trajectory optimization (NRTO). By exposing fine-grained parallelism in second-order cone (SOC) projections and reusing constant linear operators across inner iterations, cuNRTO enables two accelerated inner solvers, NRTO-DR and NRTO-FullADMM. Across unicycle, quadcopter, and Franka manipulator tasks, the proposed methods achieve substantial wall-clock speedups up to 139.6$\times$ over the baseline while maintaining robust constraint satisfaction.

In future work, we will extend cuNRTO to contact-rich manipulation and locomotion settings involving larger conic programs. We aim to further enhance computational speed by leveraging learning-to-optimize frameworks, ranging from learning-to-warmstart architectures to deep-unfolding techniques. Another direction is to extend the framework's applicability to multi-agent swarms and to address heterogeneous forms of uncertainty.
