<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Parallel-in-Time Nonlinear Optimal Control via GPU-native Sequential Convex Programming

Topics include Optimal control, Model predictive control, Predictive control, Trajectory optimization, Aerial robotics, Safety, Robustness, Benchmarks, Real-time systems, Online algorithms, Parallel computing, Optimization, Planning, Control, Massively parallel.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Real-time trajectory optimization for nonlinear constrained autonomous systems is critical and typically performed by CPU-based sequential solvers. Specifically, reliance on global sparse linear algebra or the serial nature of dynamic programming algorithms restricts the utilization of massively parallel computing architectures like GPUs. To bridge this gap, we introduce a fully GPU-native trajectory optimization framework that combines sequential convex programming with a consensus-based alternating direction method of multipliers. By applying a temporal splitting strategy, our algorithm decouples the optimization horizon into independent, per-node subproblems that execute massively in parallel. The entire process runs fully on the GPU, eliminating costly memory transfers and large-scale sparse factorizations. This architecture naturally scales to multi-trajectory optimization. We validate the solver on a quadrotor agile flight task and a Mars powered descent problem using an on-board edge computing platform. Benchmarks reveal a sustained 4x throughput speedup and a 51% reduction in energy consumption over a heavily optimized 12-core CPU baseline. Crucially, the framework saturates the hardware, maintaining over 96% active GPU utilization to achieve planning rates exceeding 100 Hz.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Furthermore, we demonstrate the solver's extensibility to robust Model Predictive Control by jointly optimizing dynamically coupled scenarios under stochastic disturbances, enabling scalable and safe autonomy.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Real-time trajectory optimization plays a crucial role in modern autonomous systems, enabling agile quadrotors to execute aggressive maneuvers, reusable launch vehicles to perform pinpoint rocket-powered landings, and high-DOF manipulators to operate near their physical limits. As robotic missions become increasingly complex, the demand for solving large-scale, non-convex Optimal Control Problem in real-time has intensified. Despite significant progress has been made, existing solvers largely rely on CPU-based sequential algorithms. This results in a bottleneck that hinders the exploitation of modern massive parallel computing hardware, such as GPUs.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In continuous-time optimal control, trajectory optimization methods are typically classified into two paradigms: indirect methods and direct methods. Indirect methods derive necessary optimality conditions from Pontryagin's Maximum Principle and solve the resulting two-point boundary-value problem. Direct methods, conversely, discretize the dynamics and controls to solve a finite-dimensional optimization problem. In general, direct methods offer greater flexibility for complex constrained modeling and enhanced robustness, making them widely adopted in practical real-time engineering projects.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Direct methods can be broadly divided into two classes: those that primarily optimize the control sequence and those that optimize both state and control sequences. Algorithms such as Differential Dynamic Programming and its variants, including iLQR, typically belong to the former class. These methods are favored for their computational efficiency in unconstrained or soft-constrained settings. Traditionally, their recursive structure, which relies on forward rollouts and backward Riccati passes, is strictly sequential. Although linearized operations and Riccati recursions can be parallelized via reduction or associative scans on GPUs, the nonlinear forward rollouts remain fundamentally serial. Furthermore, handling hard constraints within the Differential Dynamic Programming framework often requires intricate approaches that can degrade numerical conditioning and slow down convergence.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

By contrast, transcription schemes such as multiple shooting, collocation, and pseudospectral methods treat both states and controls as optimization variables. These methods explicitly impose defect, path, and boundary constraints within the discretized problem. Consequently, many implementations rely on general-purpose Nonlinear Programming solvers (e.g., IPOPT ) to solve the resulting large-scale sparse problems. Similarly, Sequential Convex Programming operates on these discretized representations by repeatedly convexifying the dynamics and constraints to solve a sequence of subproblems. While iterative solvers can theoretically be parallelized on GPUs, their sensitivity to the ill-conditioning of Karush-Kuhn-Tucker matrices means robust implementations largely rely on direct sparse factorization. However, the factorization of irregular sparse matrices involves random memory access patterns and sequential pivoting dependencies that map poorly to Single Instruction Multiple Threads architectures. As a result, these solvers are severely bottlenecked by serial operations, restricting their ability to fully exploit massive GPU parallelism.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent advancements have increasingly leveraged GPU architectures to accelerate trajectory optimization and Model Predictive Control. For instance, Adabag et al. introduced MPCGPU, which achieves fast control rates for high-DOF manipulators by employing a custom GPU-accelerated preconditioned conjugate gradient solver to resolve the underlying sparse linear systems. In the aerospace domain, Chari et al. developed a library-free GPU framework for 6-DoF powered descent guidance, utilizing a proportional-integral projected gradient (PIPG) solver within a Sequential Convex Programming structure to efficiently conduct large-scale Monte Carlo simulations. Other notable contributions include the parallelization of forward rollouts and backward passes in Differential Dynamic Programming and massively parallel motion generation libraries like cuRobo, which evaluate thousands of sampled trajectories simultaneously for collision-free navigation. These pioneering works successfully demonstrate the immense potential of parallel hardware in scaling optimal control formulations to unprecedented execution rates and problem horizons.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

To bridge the gap between constraint-handling capability and real-time performance, this paper proposes ucenter, a massively parallel solver designed from the ground up for GPU architectures (see Fig. 1).The core insight is to exploit the temporal structure of the trajectory optimization problem through consensus-based operator splitting. Instead of viewing the trajectory as a rigid sequential chain of dependencies, we treat each discretization point (collocation node) as an independent entity that negotiates with its temporal neighbors to satisfy dynamic consistency. This formulation decouples the time steps, transforming the global problem into a set of localized subproblems that are suited for massive concurrent execution.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

While Sequential Convex Programming has matured into a comprehensively researched and widely utilized paradigm for advanced trajectory optimization, solving its inner convex subproblems traditionally relies on the centralized linear algebra required by typical CPU-based Nonlinear Programming solvers. To overcome this bottleneck, we utilize an Sequential Convex Programming framework combined with the Alternating Direction Method of Multipliers. This operator-splitting approach decouples the system dynamics, enabling the parallelization of the optimization iterations across the entire time horizon. By mapping the computations for each time node to dedicated GPU resources, we execute the Sequential Convex Programming linearizations and Alternating Direction Method of Multipliers consensus updates concurrently. This architecture effectively bypasses the need for large-scale serial factorizations, accelerating the solution process while rigorously maintaining the temporal coupling of the system.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The proposed solver is both massively parallel and amenable to hard constraints extend beyond standard point-to-point planning. Specifically, data-driven control policies (e.g., reinforcement learning) require massive datasets of expert demonstrations. Generating these datasets using CPU-based solvers can take days or weeks. Our GPU-native solver can batch-process distinct optimization problems simultaneously, reducing data generation time. Additionally, safe autonomy often requires accounting for model uncertainty and disturbances. Approaches like tube-based Model Predictive Control or scenario optimization require solving for a bundle of trajectories corresponding to different uncertainty realizations. Our framework naturally supports this "ensemble solving," allowing a robot to optimize a nominal plan while simultaneously ensuring feasibility under hundreds of perturbed scenarios significantly faster than traditional sequential methods.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present ucenter, a fully GPU-native Sequential Convex Programming trajectory optimization framework for nonlinear path-constrained optimal control. By executing the entire algorithmic loop strictly on the GPU, this design minimizes CPU-GPU synchronization overhead, delivers high GPU throughput (exceeding 96% active utilization), and reduces energy consumption.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We reformulate each Sequential Convex Programming subproblem via Alternating Direction Method of Multipliers-based time splitting so that each iteration consists of independent per-time-step dense solves, closed-form updates for dynamic consistency, and projection steps for state and control constraints, avoiding global sparse Karush-Kuhn-Tucker factorizations and Riccati-style recursions.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

The framework naturally supports parallel multi-trajectory optimal control, enabling simultaneous optimization across initial conditions, task goals, and uncertainty realizations. It thereby enables scalable robust and stochastic Model Predictive Control and large-scale dataset generation, demonstrating benchmark scaling that significantly outperforms a parallel CPU baseline.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide extensive empirical validation of the proposed solver on practical applications, including a quadrotor flight task and a Mars powered descent problem. Comprehensive benchmarking on an edge computing platform demonstrates the solver's capability to evaluate hundreds of perturbed scenarios simultaneously. This massive parallelization achieves execution times that bring computationally heavy paradigms, such as robust Model Predictive Control, toward real-time feasibility on embedded hardware.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

The proposed solver is packaged as a reusable Python library. The source code will be made publicly available to the community following the review process. Researchers may also contact the first author via email to request access to the code.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Here, $\phi{( \cdot )}$ and $\ell{( \cdot )}$ define the terminal and running costs. Eq. 1b represents the nonlinear system dynamics integrated over $\Deltat$ (e.g., via 4th-order Runge-Kutta). The boundary conditions Eq. 1c enforce the initial state $x_{\text{init}}$ and a partial terminal state $x_{\text{target}}$, mapped by a constant selection matrix $S$ to constrain only specific components (e.g., position for a rocket landing).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Finally, Eq. 1d restricts the states and controls to admissible closed convex sets $\mathcal{X}_{i}$ and $\mathcal{U}_{i}$. We assume these sets are "prox-friendly," meaning they admit computationally cheap analytical projections. Typical examples include box constraints (e.g., joint limits handled via element-wise clamping) and norm constraints (e.g., maximum thrust bounds handled via vector scaling). Because these projection operations require no iterative sub-routines, they are ideally suited for massive GPU parallelization.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Methodology", "weight": 1.0} -->

We propose a two-layer hierarchical framework, illustrated in Fig. 1, to solve the non-convex optimal control problem. The outer layer employs Sequential Convex Programming to handle nonlinearities by iteratively constructing local quadratic approximations. The inner layer utilizes a massively parallel, consensus-based Alternating Direction Method of Multipliers solver to resolve the resulting large-scale Quadratic Program subproblems.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Outer Loop: The Sequential Convex Programming Interface", "weight": 1.0} -->

The primary role of the Sequential Convex Programming layer is to convert the nonlinear dynamics and non-convex costs into a sequence of affine equality constraints and convex quadratic objectives. Let $({\overline{\mathbf{x}}}^{k},{\overline{\mathbf{u}}}^{k})$ denote the nominal trajectory at iteration $k$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Outer Loop: The Sequential Convex Programming Interface", "weight": 1.0} -->

Here, the matrices $A_{i}$ and $B_{i}$ are the Jacobians of the discretized dynamics $f$ evaluated at $({\overline{x}}_{i}^{k},{\overline{u}}_{i}^{k})$, and $d_{i}$ represents the linearization residual. The matrices $Q_{i},R_{i},M_{i}$ and vectors $q_{i},r_{i}$ form the local quadratic approximation of the running cost $\ell{( \cdot )}$, with $Q_{N}$ and $q_{N}$ specifically representing the Hessian and gradient of the terminal cost $\phi{( \cdot )}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Outer Loop: The Sequential Convex Programming Interface", "weight": 1.0} -->

The sets $\mathcal{X}_{i}^{k}$ and $\mathcal{U}_{i}^{k}$ denote the trust-region bounds (typically $\ell_{\infty}$-norm box constraints) imposed to ensure the validity of the local linearizations.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Outer Loop: The Sequential Convex Programming Interface", "weight": 1.0} -->

Crucially, the evaluation of the nonlinear dynamics, the cost function, and their respective derivatives at each time step $i$ are entirely independent operations. This structure allows the outer Sequential Convex Programming loop to compute the entire linear-quadratic approximation simultaneously by mapping each collocation node to a separate GPU thread block.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Outer Loop: The Sequential Convex Programming Interface", "weight": 1.0} -->

Since the focus of this work is the highly parallelized solution of the inner problem, we omit standard trust-region update logic and refer readers to literature such as for a comprehensive treatment.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Inner Loop: Parallel Consensus Alternating Direction Method of Multipliers", "weight": 1.0} -->

Solving the Quadratic Program subproblem using conventional solvers (e.g., Sequential Quadratic Programming or Interior Point Method) is computationally expensive due to the temporal coupling introduced by the dynamics constraints. To achieve standard-form parallelism, we reformulate the problem using the Alternating Direction Method of Multipliers framework with a specific variable splitting strategy.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B1 Variable Splitting and Reformulation", "weight": 1.0} -->

To decouple the optimization horizon, we introduce three distinct sets of variables (mapped to the layers shown in Fig.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B1 Variable Splitting and Reformulation", "weight": 1.0} -->

Physical Variables $(x,u)$: These are the primal variables responsible for minimizing the local quadratic cost and satisfying the linearized dynamics. In the split form, they constitute an unconstrained quadratic program.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B1 Variable Splitting and Reformulation", "weight": 1.0} -->

Dynamic Auxiliary Variables $(z)$: Defined such that $x_{i} = z_{i}$. These variables decouple the temporal dependency between time steps $i$ and $i + 1$, allowing the physical variables to be updated independently.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B1 Variable Splitting and Reformulation", "weight": 1.0} -->

Geometric Mirror Variables $(\hat{x},\hat{u})$: Defined such that $x_{i} = {\hat{x}}_{i}$ and $u_{i} = {\hat{u}}_{i}$. These variables handle all hard inequality constraints (such as trust regions and actuation limits) via indicator functions, mathematically manifesting as proximal projection operations.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B2 The Augmented Lagrangian", "weight": 1.0} -->

We formulate the problem as minimizing the Augmented Lagrangian $\mathcal{L}_{\rho}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B2 The Augmented Lagrangian", "weight": 1.0} -->

where $l_{i}{(x_{i},u_{i})}$ is the local quadratic cost defined in (2a), and $d_{\text{dyn},i} = {{A_{i}x_{i}} + {B_{i}u_{i}} + d_{i}}$ represents the linearized dynamic propagation. The vectors $\lambda,\mu,\nu$ are the dual multipliers, and $\rho_{\text{eq}},\rho_{\text{dyn}},\rho_{\text{geo}}$ are the scalar penalty parameters for state consistency, dynamic propagation, and geometric constraints, respectively.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B3 The Alternating Direction Method of Multipliers Iteration Steps", "weight": 1.0} -->

The algorithm alternates between minimizing $\mathcal{L}_{\rho}$ with respect to each variable block. Due to the temporal splitting, these steps can be executed in parallel or resolved via closed-form solutions across the trajectory nodes.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B3 The Alternating Direction Method of Multipliers Iteration Steps", "weight": 1.0} -->

Step 1: Physical Layer Update $(x,u)$. We minimize the terms in $\mathcal{L}_{\rho}$ involving $x_{i}$ and $u_{i}$, treating all other variables as constants. Ignoring indicator functions results in an unconstrained quadratic minimization. For each time step $i$, this requires solving the linear system ${H_{i}\xi_{i}} = g_{i}$, where $\xi_{i} = {\lbrack x_{i}^{T},u_{i}^{T}\rbrack}^{T}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B3 The Alternating Direction Method of Multipliers Iteration Steps", "weight": 1.0} -->

Crucially, $H_{i}$ is strictly positive definite due to the $\rho$ regularization terms. This guarantees the mathematical stability of standard, unpivoted Cholesky factorization. By avoiding numerical pivoting, this step completely circumvents branching and thread divergence, making it highly optimal for SIMT GPU execution. Furthermore, since $H_{i}$ is constant within an Sequential Convex Programming iteration, its factorization can be cached, leaving only highly efficient forward-backward substitutions for the inner Alternating Direction Method of Multipliers loop.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B3 The Alternating Direction Method of Multipliers Iteration Steps", "weight": 1.0} -->

Step 2: Dynamic Layer Update $(z)$. We minimize terms involving $z_{i}$ to reconcile the state $x_{i}$ with the dynamics propagated from the previous step.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-B3 The Alternating Direction Method of Multipliers Iteration Steps", "weight": 1.0} -->

Step 3: Geometric Layer Update $(\hat{x},\hat{u})$. This step handles the physical inequality constraints.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-B3 The Alternating Direction Method of Multipliers Iteration Steps", "weight": 1.0} -->

The update for the state proxy ${\hat{x}}_{i}$ is strictly analogous.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-B3 The Alternating Direction Method of Multipliers Iteration Steps", "weight": 1.0} -->

This four-step procedure repeats until the primal and dual residuals satisfy the chosen convergence criteria.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-B3 The Alternating Direction Method of Multipliers Iteration Steps", "weight": 1.0} -->

Remark on Alternating Direction Method of Multipliers Convergence: While standard Alternating Direction Method of Multipliers provides convergence guarantees strictly for two-block variable splitting, our proposed three-variable formulation preserves these theoretical guarantees through structural separability. Specifically, the variables can be grouped into exactly two blocks: the primal physical variables $(x,u)$ and the auxiliary variables $(z,\hat{x},\hat{u})$. Because the Augmented Lagrangian Eq. 3 contains no cross-penalty terms directly coupling the dynamic auxiliary variables $z$ with the geometric mirror variables $(\hat{x},\hat{u})$, their respective update steps are conditionally independent for a fixed $(x,u)$. Consequently, Steps 2 and 3 of our algorithm constitute a single, fully separable block update evaluated in parallel, reducing the framework to a standard two-block Alternating Direction Method of Multipliers sequence.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

To validate the proposed parallel-in-time solver, we deployed it on an Nvidia Jetson AGX Orin 64GB edge computing platform (see Fig. 2). This high-performance embedded architecture is increasingly being adopted across diverse and highly dynamic robotic domains. Recent applications demonstrate its capability to process complex 3D perception pipelines in real time for autonomous driving, provide low-latency monocular depth estimation for unmanned aerial vehicles, and operate reliably under ionizing radiation in challenging aerospace and low earth orbit missions.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The simulation environment and the proposed solver are implemented entirely in Python. To fully leverage the GPU architecture, the computational backend is built upon the JAX framework, utilizing its vmap and jit compilation features for highly efficient batched tensor operations.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-A1 Problem Setup", "weight": 1.0} -->

We evaluate the solver on a 6-DOF quadrotor model. Agile quadrotor flight serves as a standard and rigorous benchmark in modern robotics due to its highly nonlinear, underactuated dynamics and the strict requirement for high-frequency replanning in cluttered environments. Demonstrating real-time, massively parallel trajectory generation for such platforms addresses a critical demand for robust edge compute solutions in autonomous navigation.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-A1 Problem Setup", "weight": 1.0} -->

The state $x \in {\mathbb{R}}^{13}$ comprises position $r \in {\mathbb{R}}^{3}$, linear velocity $v \in {\mathbb{R}}^{3}$, unit quaternion $q \in {\mathbb{R}}^{4}$, and body-frame angular velocity $\omega \in {\mathbb{R}}^{3}$. The control $u \in {\mathbb{R}}^{4}$ consists of total thrust and body-frame torques. The continuous-time dynamics follow standard Newton-Euler equations with a mass of 1.0 kg and gravity of 9.81 m/s^2^. The dynamics are discretized via a 4th-order Runge-Kutta integration scheme and linearized using JAX's automatic differentiation.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-A2 Ablation Study", "weight": 1.0} -->

For this study, the quadrotor is tasked with a 6.0 s flight ($N = 50$) from an initial hover at $\lbrack{- 5.0},{- 5.0},2.0\rbrack$ m to a target position at $\lbrack 5.0,5.0,2.0\rbrack$ m. Terminal constraints strictly enforce the target position and zero linear velocity. The direct flight path is obstructed by three spherical obstacles with radii ranging from 1.2 to 1.5 m. Actuator limits constrain the total thrust to $\lbrack 0,20\rbrack$ N and body torques to $\lbrack{- 5},5\rbrack$ Nm.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-A2 Ablation Study", "weight": 1.0} -->

We evaluated the solver's sensitivity to the final penalty parameter $\rho_{f}$ and the number of inner Alternating Direction Method of Multipliers iterations under these tight conditions. For simplicity, the penalty parameters in Eq. 3 are set to an identical value ($\rho_{\text{eq}} = \rho_{\text{dyn}} = \rho_{\text{geo}} = \rho$) and scaled logarithmically over the Sequential Convex Programming iterations to a final value $\rho_{f}$. As shown in Fig. 3, testing $\rho_{f} \in {\{ 10^{3},10^{4},10^{5},10^{6}\}}$ reveals a tradeoff: higher values enforce constraint satisfaction more aggressively in early iterations but converge to higher final objective costs compared to $\rho_{f} = 10^{3}$. Furthermore, the solver demonstrates robust inexact Sequential Convex Programming behavior.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-A2 Ablation Study", "weight": 1.0} -->

It maintains stable convergence with as few as 100 inner Alternating Direction Method of Multipliers steps, though increasing the step count to 250 yields marginally lower final defects and objective costs.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-A3 Scalability Benchmark", "weight": 1.0} -->

To quantify the solver's robustness and scalability, we evaluated it on randomized, obstacle-cluttered environments. We reduced the temporal horizon to $N = 40$ to test a coarser resolution. We generated a batch of $B = 1000$ trajectories, each initialized with noise and tasked with navigating around three randomly placed spherical obstacles (radii $1.0$ to $2.0$ m). A trajectory is considered successfully solved if it meets three strict criteria: the mean dynamics violation is strictly below $10^{- 2}$, obstacle penetration is under $10^{- 3}$ m, and the combined boundary condition error is less than $0.1$. Under these rigorous thresholds, the solver achieved a 93.9% success rate, maintaining a low average dynamics defect of $0.007$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-A3 Scalability Benchmark", "weight": 1.0} -->

To assess computational efficiency, we benchmarked our GPU-native implementation against a highly optimized CPU baseline, which employs an iLQR algorithm distributed across 12 CPU cores via multiprocessing and numba JIT compilation. Evaluating batch sizes $B$ from 1 to 5000, Table I and Fig. 4 illustrate the scaling performance. The CPU baseline's throughput saturates at approximately 24.6 Hz for large batches. Conversely, the GPU solver efficiently leverages massive parallelization via JAX's vmap, reaching a peak throughput of 101.1 Hz at $B = 5000$. As detailed in the left panel of Fig. 5, the solver maintains an active GPU utilization of 96.93% during this highly dynamic agile flight task, effectively saturating the streaming multiprocessors. This yields a stable 4.1$\times$ speedup over the fully utilized 12-core CPU architecture.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-A3 Scalability Benchmark", "weight": 1.0} -->

Beyond pure computational speed, this hardware efficiency translates directly to power savings. Integrating the total module power consumption during the active computation phase reveals that the GPU solver requires only 119.03 J to process the batch of $B = 1000$ trajectories, whereas the multi-core CPU baseline consumes 243.58 J. This represents a 51% reduction in energy expenditure, offering a critical advantage for power-constrained mobile robots. Importantly, a replanning rate exceeding 100 Hz is highly suitable for real-time Model Predictive Control. While this benchmark intentionally evaluates peak capacity, practical edge deployments can explicitly partition hardware power profiles and software memory limits to reserve adequate compute and power budgets for concurrent sensor processing.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-A4 Robust Planning via Scenario Optimization", "weight": 1.0} -->

We evaluated the solver's utility for robust Model Predictive Control using scenario optimization. The quadrotor was tasked with navigating from $\lbrack{- 4.0},{- 5.0},2.0\rbrack$ m to a target at $\lbrack 5.0,5.0,2.0\rbrack$ m while bypassing a cylindrical obstacle with a 3.0 m radius. To ensure safety under uncertainty, we enforced an additional 0.5 m spatial buffer around the obstacle.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-A4 Robust Planning via Scenario Optimization", "weight": 1.0} -->

To simulate severe unmodeled disturbances, a stochastic crosswind was injected into the true dynamics whenever the quadrotor entered the middle flight corridor ($X \in {({- 2.5},2.5)}$). This wind applied a base acceleration of $\lbrack 0.0,2.5,{- 1.0}\rbrack$ m/s^2^ corrupted by Gaussian noise. At each Model Predictive Control step, a linear disturbance observer estimated the acceleration mismatch. To compute a safe policy, the solver jointly optimized $K = 15$ dynamically coupled scenarios over a horizon of $N = 30$, where each scenario was injected with scaled noise to synthesize a distribution-aware safety tube. Crucially, we applied a consensus-based approach to this formulation: a non-anticipativity constraint was enforced, strictly requiring the first control input to be identical across all $K$ scenarios. This ensures that the immediate control action is physically executable in reality, while allowing the predicted state trajectories to branch out over the horizon to accommodate the distinct disturbance profiles.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-A4 Robust Planning via Scenario Optimization", "weight": 1.0} -->

As depicted in Fig. 6, the robust Model Predictive Control successfully anticipates the bounded uncertainty. It generates a $2\sigma$ spatial prediction tube that smoothly deforms to respect the obstacle's safety margin despite the heavy crosswind. The quadrotor reaches and stabilizes at the target by step 40. Furthermore, the solver computes the full 15-scenario robust optimization in approximately 200 ms per step after stabilization, demonstrating its viability for handling complex, multi-trajectory constraints in realistic environments.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-B1 Problem Setup", "weight": 1.0} -->

We apply the proposed solver to the 6-DOF Mars powered descent landing problem adapted from Szmuk et al.. In planetary landing scenarios, state estimation is frequently degraded by severe observation errors and sensor noise. Evaluating the extensive uncertainty bounds required for active guidance is computationally demanding. Our massively parallel approach addresses this challenge by enabling the simultaneous computation of hundreds of dispersed trajectories, facilitating real-time safety verification and robust control under high uncertainty.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-B1 Problem Setup", "weight": 1.0} -->

The problem is formulated using non-dimensional unified units. The state vector $x \in {\mathbb{R}}^{14}$ consists of vehicle mass $m$, inertial position $r \in {\mathbb{R}}^{3}$, velocity $v \in {\mathbb{R}}^{3}$, body attitude quaternion $q \in {\mathbb{R}}^{4}$, and angular velocity $\omega \in {\mathbb{R}}^{3}$. The control input $u \in {\mathbb{R}}^{3}$ is the thrust vector $T_{B}$ in the body frame.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-B1 Problem Setup", "weight": 1.0} -->

The continuous-time dynamics account for mass depletion $\overset{˙}{m} = {- {\alpha{\| T_{B}\|}}}$ (where $\alpha = 0.1$), constant gravity, and full rotational kinematics governed by a diagonal inertia matrix. The flight horizon is fixed at 5.0 and discretized into $N = 30$ intervals.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-B1 Problem Setup", "weight": 1.0} -->

To ensure a safe and physically feasible descent, the vehicle must satisfy stringent state and control bounds. The spacecraft mass is restricted between a dry mass of 0.75 and a wet mass of 2.0. Actuator limits constrain the thrust magnitude within $\lbrack 0.5,3.0\rbrack$ and restrict the thrust gimbal angle to a $10^{\circ}$ cone relative to the body axis. Furthermore, spatial and attitude constraints are strictly enforced: the trajectory is confined within a $10^{\circ}$ glide slope cone to prevent surface collision, the vehicle tilt angle is limited to a maximum of $20^{\circ}$ from the vertical, and the angular velocity magnitude is bounded by $30^{\circ}$ per unit time.

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-B1 Problem Setup", "weight": 1.0} -->

The spacecraft initiates the descent around a nominal position of $\lbrack 2.0,1.0,0.0\rbrack$ in the Up-East-North frame with a velocity of $\lbrack{- 1.0},0.2,0.0\rbrack$. The solver is tasked strictly with minimizing fuel consumption to achieve a precise touchdown at the origin $\lbrack 0.0,0.0,0.0\rbrack$ with a soft terminal velocity of $\lbrack{- 0.1},0.0,0.0\rbrack$ while maintaining a strictly upright orientation.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-B2 Batch Trajectory Optimization and Scalability", "weight": 1.0} -->

To evaluate the solver's computational throughput and its ability to guarantee safety under uncertainty, we conducted a massively parallel batch optimization experiment. To account for state estimation and observation errors, we applied a 5% stochastic perturbation to the nominal initial state across all 14 state dimensions. By leveraging JAX's vmap transformation, the solver jointly optimizes a batch of $B = 1000$ independent descent scenarios simultaneously on the GPU. This large-scale Monte Carlo analysis serves to verify that, despite the initial dispersion, the solver can reliably ensure all trajectories remain within the feasible region and successfully reach the target.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-B2 Batch Trajectory Optimization and Scalability", "weight": 1.0} -->

As depicted in Fig. 7, the solver consistently discovers fuel-optimal trajectories that strictly respect the $10^{\circ}$ glide slope boundary across the randomized initial conditions. Furthermore, the optimized thrust profiles exhibit notable bang-bang control characteristics, rapidly switching between maximum and minimum bounds to optimize fuel, although the structure is not strictly rigid due to the discrete-time formulation and algorithmic smoothing.

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-B2 Batch Trajectory Optimization and Scalability", "weight": 1.0} -->

Under rigorous physical and algorithmic feasibility checks, including nonlinear dynamics rollouts, glide slope adherence, and boundary condition satisfaction, the solver achieved a strict success rate of 99.8%, sustaining an overall computational throughput of 268.63 Hz. As demonstrated in the right panel of Fig. 5, the solver achieved an active GPU utilization of 96.17%, proving its ability to consistently saturate parallel hardware across distinct dynamic models. This performance demonstrates the solver's exceptional capability for rapid, large-scale trajectory generation and safety verification in complex aerospace applications.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper presented a GPU-native trajectory optimization framework that combines Sequential Convex Programming with a consensus-based Alternating Direction Method of Multipliers decomposition to achieve massive parallelism across both time steps and problem instances. By splitting the nonlinear optimal control problem into independent per-node dense solves, closed-form dynamic consensus updates, and analytical constraint projections, the proposed method entirely avoids the global sparse factorizations that bottleneck conventional solvers on GPU architectures.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Numerical experiments on a 13-state quadrotor and a 14-state Mars powered descent problem validated the approach. The scalability benchmark demonstrated a sustained 4.1$\times$ throughput improvement and a 51% reduction in energy consumption over a 12-core CPU baseline, achieving over 100 Hz replanning rates suitable for real-time Model Predictive Control. Furthermore, the framework's natural support for multi-trajectory optimization was demonstrated through scenario-based robust Model Predictive Control, where 15 dynamically coupled scenarios were jointly optimized under stochastic disturbances while respecting safety constraints. The solver's ability to efficiently handle complex, multi-trajectory constraints in realistic environments highlights its potential for deployment in real-world robotic systems, particularly those requiring high-frequency replanning and robustness to uncertainty.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Despite these computational advantages, several avenues remain for future work. First, an in-depth theoretical analysis is required to establish rigorous convergence guarantees, particularly concerning the interaction between the partially converged inner Alternating Direction Method of Multipliers loop and the outer Sequential Convex Programming iterations. Second, future efforts will focus on deploying the GPU-native solver in physical hardware experiments to achieve real-world validations.
