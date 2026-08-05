<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

cuNRTO: GPU-Accelerated Nonlinear Robust Trajectory Optimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Robust trajectory optimization enables autonomous systems to operate safely under uncertainty by computing control policies that satisfy the constraints for all bounded disturbances. However, these problems often lead to large Second Order Conic Programming (SOCP) constraints, which are computationally expensive. In this work, we propose the CUDA Nonlinear Robust Trajectory Optimization (cuNRTO) framework by introducing two dynamic optimization architectures that have direct application to robust decision-making and are implemented on CUDA. The first architecture, NRTO-DR, leverages the Douglas-Rachford (DR) splitting method to solve the SOCP inner subproblems of NRTO, thereby significantly reducing the computational burden through parallel SOCP projections and sparse direct solves. The second architecture, NRTO-FullADMM, is a novel variant that further exploits the problem structure to improve scalability using the Alternating Direction Method of Multipliers (ADMM). Finally, we provide GPU implementations of the proposed methodologies using custom CUDA kernels for SOC projection steps and cuBLAS GEMM chains for feedback gain updates.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We validate the performance of cuNRTO through simulated experiments on unicycle, quadcopter, and Franka manipulator models, demonstrating speedups of up to 139.6x. More details are available at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Trajectory optimization has become a foundational tool for motion planning and control of robotic systems, enabling robots to compute dynamically feasible paths that minimize objective cost while satisfying constraints. Applications span from manipulation and legged locomotion to aerial vehicles and autonomous driving. However, real-world robotic systems inevitably face uncertainty. When constraints encode safety-critical requirements---such as obstacle avoidance or actuator limits---failing to account for these uncertainties can lead to catastrophic consequences.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Handling uncertainty is critical for real-world deployment. One common approach is to model uncertainty as a stochastic disturbance characterized by a probability distribution. Existing methods, ranging from chance-constrained optimization to covariance steering, provide probabilistic guarantees on constraint satisfaction. However, stochastic models may not capture all uncertainty types; modeling inaccuracies or exogenous disturbances are often better represented as deterministic uncertainty, referring to disturbances assumed to lie within a bounded set. In many safety-critical applications, a guarantee is required for all possible realizations of such uncertainty. This work addresses trajectory optimization in the presence of these deterministic disturbances.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Standard approaches to address deterministic uncertainty involve providing worst-case guarantees over bounded uncertainty sets, a concept originating from the field of robust control. This idea has been adapted for trajectory optimization in several forms, ranging from Tube-based and Robust Model Predictive Control (MPC) to min-max methods. Tube-based MPC computes a nominal trajectory and feedback gains to maintain the system within a safe tube; but can be overly conservative due to the decoupling between the nominal control and the feedback gains. Robust MPC typically considers linear systems, and Min-Max DDP frame the problem as a game against an adversarial disturbance to optimize a robust policy, failing to address nonlinear state constraints. While DIRTREL studies robust nonlinear direct transcription under ellipsoidal disturbances with an LQR tracking controller, it assumes uncorrelated uncertainty across the time-steps. To effectively handle both nonlinear dynamics and state constraints, recent research has shifted toward Robust Optimization (RO). Some frameworks in this category address nonlinear constraints but are limited to linear dynamical systems. Conversely, recent work introduced the Nonlinear Robust Trajectory Optimization (NRTO) framework, a trajectory optimization framework that accounts for nonlinearity in both the dynamics and the constraints.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The NRTO framework comprises three core elements: successive linearization, robust constraint reformulation, and the resolution of linearized subproblem infeasibility via operator-splitting techniques. Since the framework enforces robust constraints that must be satisfied for every possible realization of uncertainty within a bounded set, the problem is intractable in its original form due to the infinite number of constraints. To overcome this, the NRTO framework employs robust constraint reformulation, converting the problem into a tractable form that yields Second-Order Conic Programming (SOCP) constraints. Despite the effectiveness of this framework, the computational cost of the existing implementation based on Interior Point (IP) methods for solving the SOCP subproblems remains a primary barrier to its widespread adoption for high-dimensional systems with numerous constraints.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Leveraging GPU acceleration offers a powerful solution to overcome these computational barriers. As single-core CPU performance has largely plateaued, the robotics community has increasingly turned to massively parallel architectures to accelerate complex motion planning tasks. Early research in this domain focused primarily on parallelizing rigid body dynamics and their corresponding gradients. More recently, GPU acceleration has been pushed into the optimization loop itself. For example, MPCGPU achieves real-time nonlinear MPC by accelerating the dominant sparse Newton solve (PCG) on the GPU. Similar GPU-parallelism has also been explored in constrained sampling-based planning.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Beyond nonlinear MPC, GPU implementations of first-order splitting methods for convex programs, particularly ADMM-based QP solvers such as OSQP, achieve high throughput by mapping the repeated linear algebra and projection steps to GPU kernels while keeping iterates on-device. However, the NRTO framework in its current form is not inherently amenable to parallelization.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper presents cuNRTO: a GPU-accelerated nonlinear robust optimization framework by introducing two novel extensions to the original NRTO formulation. This enables efficient parallel execution. Fig. 1 provides a high-level overview of the cuNRTO execution flow. Specifically, the contributions of this paper are three-fold: First, we introduce NRTO-DR, a minimal-change methodology to solve the computationally expensive sub-problems of the NRTO framework using Douglas-Rachford splitting (DR). The proposed methodology improves the performance over Interior Point (IP) Methods through parallel SOC projections and sparse direct solves that reduce matrix operations.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, we propose NRTO-FullADMM, a novel variant of the NRTO framework that could fully leverage GPU acceleration. By restructuring the inner ADMM update blocks, this framework integrates SOCP projections directly into the inner loop eliminating extra DR layer and host-device communication overhead.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Third, we develop cuNRTO, which constitutes GPU implementation of the NRTO-DR and NRTO-FullADMM. Our approach utilizes cuBLAS GEMM chains for the feedback gain update and custom CUDA kernels for SOC projections. We validate our approach on unicycle, quadcopter, and Franka manipulator trajectory optimization, demonstrating a speedup of up to 139.60$\times$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-B Organization of the paper", "weight": 1.0} -->

The remainder of this paper is organized as follows. Section II presents the problem statement and a detailed overview of the Nonlinear Robust Trajectory Optimization (NRTO) framework. In Sections III and IV, we introduce our core architectural contributions: NRTO-DR and NRTO-FullADMM, respectively. Section V demonstrates the computational performance of these proposed frameworks through a series of simulation experiments involving unicycle, quadcopter, and Franka Emika manipulator models. Finally, Section VI provides concluding remarks and discusses future work.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Nonlinear Robust Trajectory Optimization Framework", "weight": 1.0} -->

In this section, we outline the nonlinear robust trajectory optimization framework (NRTO) considered in this work. We start by presenting the problem statement followed by framework details.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Problem Statement", "weight": 1.0} -->

Subsequently, the nonlinear robust trajectory optimization problem addressed in this work is presented.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B NRTO Algorithm", "weight": 1.0} -->

In this section, we provide an outline of the NRTO framework, which integrates successive linearization, robust constraint reformulation, and Alternating Direction Method of Multipliers (ADMM). For the simplicity of analysis, we present the problem in terms of the variable ${\bm{k}}_{v}\in\mathbb{R}^{Tn_{u}n_{x}}$ defined as ${\bm{k}}_{v}=[{\bm{k}}_{v,0};{\bm{k}}_{v,1};\dots;{\bm{k}}_{v,T-1}]$ with ${\bm{k}}_{v,k}=\text{vec}({\bf K}_{k})$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B NRTO Algorithm", "weight": 1.0} -->

NRTO is a bi-level algorithm as shown in Fig. 2. In the outer loop of the algorithm, the problem is linearized around a nominal trajectory $\hat{{\bm{u}}},\hat{{\bm{x}}}$ and converted into a tractable form. This results in Second Order Conic Programming (SOCP) constraints as shown below.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem 2 (Tractable Linearized Problem)", "weight": 1.0} -->

This linearized problem can be infeasible due to linearization, especially during the initial iterations of the algorithm. Thus, the problem is solved indirectly using ADMM in the inner loop (refer to Algorithm 1 of for details). For which, Problem 2. ‣ II-B NRTO Algorithm ‣ II Nonlinear Robust Trajectory Optimization Framework ‣ cuNRTO: GPU-Accelerated Nonlinear Robust Trajectory Optimization") is converted to the following form solvable using ADMM, by introducing a slack variable $\tilde{p}$, Figure 2: Overview of NRTO Framework: A bi-level structure involving an outer successive linearization (SL) loop to generate tractable linearized problem, and an inner ADMM loop to solve the resulting linearized problem.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-C NRTO-LE Algorithm", "weight": 1.0} -->

This section outlines NRTO-LE, an extension of the NRTO framework developed to address linearization error. While the standard NRTO algorithm ensures that a linearized trajectory satisfies all the constraints, it may not guarantee the safety of the actual trajectory when the linearization error is significant. To address this, NRTO-LE models the linearization error at each time step as a bounded uncertainty lying inside an ellipsoidal set. For the comprehensive derivation of the modification, the reader is referred to.

<!-- chunk {"id": "body-0020", "role": "body", "section": "NRTO-DR Framework", "weight": 1.0} -->

In this section, we introduce a framework for accelerating the solving of the sub-problem (7a) which is the most computationally expensive update in the inner loop of the NRTO. Subsequently, we provide a GPU version of the framework that could further enhance the computational speed. The design goal of NRTO-DR is to make the smallest algorithmic change to NRTO while replacing the expensive interior-point SOCP subsolve in (7a). By rewriting this block with Douglas-Rachford splitting, the update decomposes into reusable sparse linear solves and independent SOC projections, exposing the parallelism needed for GPU acceleration.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Framework", "weight": 1.0} -->

Now, the update (11c) involves where the projection step $\Pi_{\pazocal{K}_{j}}({\bm{s}}_{\text{ref},j}^{l_{\text{dr}}})$ is defined in Section II of SM, a visual interpretation is provided in Fig. 3.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B GPU implementation", "weight": 1.0} -->

The GPU implementation of NRTO-DR (Fig. 4) follows the relaxed DR updates (11a)-(11c). The affine set proximal step (11a) reduces to solving a fixed sparse KKT system with coefficient matrix ${\bf K}_{\mathrm{KKT}}$, which is factored once across DR iterations. The details are as follows: The one-time sparse factorization of ${\bf K}_{\mathrm{KKT}}$ and per-iteration triangular solves are performed by cuDSS.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B GPU implementation", "weight": 1.0} -->

SOC projections are computed by a CUDA kernel. The cone-projection case logic is adapted from the open-source SCS implementation.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B GPU implementation", "weight": 1.0} -->

All vector operations, such as reflection, updates, and residuals, are handled via cuBLAS and kept on-device.

<!-- chunk {"id": "body-0025", "role": "body", "section": "NRTO-FullADMM Framework", "weight": 1.0} -->

In this section, we present a framework that accelerates the solving of Problem 2. ‣ II-B NRTO Algorithm ‣ II Nonlinear Robust Trajectory Optimization Framework ‣ cuNRTO: GPU-Accelerated Nonlinear Robust Trajectory Optimization"). Specifically, we propose a novel architecture by modifying the inner ADMM loop of the NRTO framework. We start by rewriting Problem 2. ‣ II-B NRTO Algorithm ‣ II Nonlinear Robust Trajectory Optimization Framework ‣ cuNRTO: GPU-Accelerated Nonlinear Robust Trajectory Optimization") by introducing a slack variable ${\bm{\nu}}$, as follows

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-A Framework", "weight": 1.0} -->

We propose a framework to solve the above problem using a scaled form of ADMM. The variables $({\bm{\nu}},\tilde{{\bm{p}}})$ are considered as the first block, and $(\delta\hat{{\bm{u}}},{\bm{p}},{\bm{k}}_{v})$ are as the second block of the inner ADMM loop, with (14c) being the coupling constraints. The AL of the above problem is disclosed in Section III of SM, with the penalty parameter as $\rho$, and $\rho{\bm{\lambda}}_{p},\rho{\bm{\lambda}}_{\nu}$ as the dual variables. Subsequently, we present the update steps in the $(l_{\text{in}}^{th})$ iteration, with the detailed derivation disclosed in Section III of SM.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Block-2 update", "weight": 1.0} -->

The variables $(\delta\hat{{\bm{u}}},{\bm{p}})$ and ${\bm{k}}_{v}$ are decoupled, with the ADMM update steps given as where ${\bm{q}},\pazocal{M},\bar{\pazocal{M}}$, disclosed in Section III of SM, remain constant throughout the inner ADMM loop. The update (16a) is similar to the update step (7b) of NRTO.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Dual update", "weight": 1.0} -->

SOCP and QP data, and uploads constants to the GPU once.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Dual update", "weight": 1.0} -->

The FullADMM inner loop runs entirely on-device: (i) batched affine evaluation forms per-constraint inputs, (ii) SOC projections are computed in parallel over j, (iii) Block-2 updates solve the QP and update kv using prepacked operators, and (iv) dual updates and residual checks determine termination.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B GPU Implementation", "weight": 1.0} -->

An overview of the end-to-end on-device inner ADMM loop pipeline for NRTO-FullADMM is shown in Fig. 5.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B2 Block-1", "weight": 1.0} -->

The Block-1 update requires projecting We implement this in two GPU steps. First, affine evaluation. We compute all $\hat{{\bm{y}}}_{j}$ via a sequence of cuBLAS GEMM calls that exploit the structured factorization of $\hat{{\bf A}}_{j}$ through ${\bf M}$, ${\bf U}_{k}$, and ${\bf B}_{k}$, avoiding explicit dense matrix formation. Second, SOC projection. We launch a CUDA kernel that performs the SOC projection for each constraint block in parallel. The projection routine follows the standard SOC projection cases and is adapted from the SCS reference implementation, with modifications for warp-level execution and our batched memory layout. This step is bandwidth-bound and scales linearly with $n_{g}$, it achieves near-ideal parallel efficiency.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B3 Block-2", "weight": 1.0} -->

The update (16a) is a convex QP with fixed quadratic term and fixed constraints (14a). We solve it using preconditioned conjugate gradient (PCG) with a Jacobi preconditioner. Crucially, its linear algebra is reusable across inner iterations, so any preconditioner is computed once per outer iteration and reused thereafter. The ${\bm{k}}_{v}$ update (16b) is solved via PCG with matrix-free Hessian-vector products, avoiding explicit formation of the dense Hessian matrix.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-B4 Dual updates", "weight": 1.0} -->

Dual updates are vector axpy-style operations. We compute the primal residual $r_{p}$ and dual residual $r_{d}$ on the GPU and terminate when both fall below the tolerance.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 1", "weight": 1.0} -->

NRTO-FullADMM scales effectively over NRTO and NRTO-DR through two key innovations. First, it replaces the nested structure of NRTO-DR by directly integrating the parallel SOCP block projections into the inner ADMM updates. Second, it eliminates CPU-GPU data transfer bottlenecks by executing the entire inner ADMM loop on the GPU.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Simulation", "weight": 1.0} -->

We evaluate cuNRTO, a suite comprising the GPU-accelerated versions of NRTO-DR and NRTO-FullADMM, on unicycle, quadcopter, and Franka manipulator tasks. We provide a comprehensive analysis of the impact of key system parameters, such as time horizon ($T$), uncertainty level ($\tau$), and the number of obstacles, on both constraint satisfaction and wall-clock time in comparison to the baseline NRTO. Furthermore, we highlight the effectiveness of the proposed architectures in addressing complex dynamical systems through a high-dimensional Franka manipulator task.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-A Methodology", "weight": 1.0} -->

Results were collected on a high-performance workstation with a 3.06 GHz 60-core Intel Xeon W-3500 CPU and an NVIDIA A100 80GB GPU, running Ubuntu 22.04 and CUDA 12.9. Code was compiled with g++ 11.4.0. We use the same outer-loop parameters for all methods. The baseline NRTO solves subproblems using MOSEK interior-point optimizer with multi-threading enabled. Solver-specific hyperparameters were tuned independently for best performance, and its complete list is provided in Section IV of SM.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-A Methodology", "weight": 1.0} -->

The performance is evaluated based on the following: Constraint satisfaction: Constraint satisfaction was verified using Monte Carlo sampling with 1,000 i.i.d. disturbance drawn uniformly from the interior of the uncertainty set, combined with 1,000 reproducible edge cases that probe the boundary of the uncertainty set via convex combinations of worst-case constraint directions. We set fixed seed to ensure the consistency of the sampling across all experiments. The reported satisfaction probability is the fraction of successful rollouts.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-A Methodology", "weight": 1.0} -->

Wall-clock time: We report the wall-clock time required for each solver to converge to a feasible solution. Runtimes were measured using C++ std::chrono::high_resolution_clock.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-B Performance Evaluation", "weight": 1.0} -->

Trajectory comparisons between the proposed frameworks and the baseline NRTO for the unicycle and quadcopter models are presented in Fig. 6 and Fig. 7, respectively. Further, the computational efficiency is demonstrated in Table I. We report three sweep studies over horizon length $T$, uncertainty level $\tau$, and the number of obstacles for both unicycle and quadcopter. We denote the nominal setting as $(T_{0},\tau_{0},O_{0})=(30,0.05,0)$ and vary one parameter at a time. All experiments use time-step $\Delta k=$ 25 ms for both optimization and rollout.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-B1 Horizon Sweep ($T$)", "weight": 1.0} -->

At the nominal horizon $T_{0}=30$, NRTO-FullADMM reduces solve time from 32.137 s to 6.231 s for the unicycle, which is 5.16$\times$ faster, and from 1327.390 s to 98.585 s for the quadcopter, which is 13.46$\times$ faster. At $T=45$, NRTO-FullADMM reaches 6.387 s for the unicycle and 132.484 s for the quadcopter, corresponding to 6.94$\times$ and 13.21$\times$ speedups over NRTO, respectively.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-B2 Obstacle Sweep ($Obs$)", "weight": 1.0} -->

As the number of obstacles increases, the number of robust constraints and associated SOC projections grow, and the GPU implementations benefit from the resulting parallelism. At $Obs=5$, NRTO-FullADMM reduces solve time from 30423.523 s to 217.932 s for the unicycle, which is 139.60$\times$ faster, and from 13374.375 s to 199.935 s for the quadcopter, which is 66.89$\times$ faster.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-B3 Uncertainty sweep ($\\tau$)", "weight": 1.0} -->

As $\tau$ increases, the NRTO success rate decreases, reflecting the increased conservativeness and difficulty of the robust constraints. In contrast, when accounting for linearization error using NRTO-LE, we observe 100% constraint satisfaction across all reported $\tau$ values for both dynamics. Across the sweep, NRTO-FullADMM consistently yields the lowest wall-clock times among the compared methods.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-C Source of speedup", "weight": 1.0} -->

For the unicycle task with five obstacles in Fig. 6, NRTO-DR spends most of its runtime on host--device synchronization and linear solves ($43.5\%$ and $32.6\%$), while SOC projections account for only $11.0\%$. A detailed runtime breakdown is provided in Section IV of the SM. By keeping the inner ADMM loop on-device, NRTO-FullADMM reduces synchronization overhead and increases average GPU utilization from $34.9\%$ to $86.5\%$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-D Solution quality", "weight": 1.0} -->

The proposed reformulations achieve significant speedup without compromising solution quality. The visual variations in terminal-state distributions in Fig. 6-7 and the linearization error differences in Table I are due to convergence toward distinct local minima. These variations arise from the sensitivity of successive linearization towards initialization, hyperparameters, and solver tolerances, rather than a degradation of robust feasibility. Consequently, Table I reveals no distinct pattern in linearization errors across the solvers. Furthermore, for the unicycle task (Fig. 6), the objective components $(J_{u},J_{kv})$ for NRTO, NRTO-DR, and NRTO-FullADMM are $(14.624,204.914)$, $(14.932,204.912)$, and $(13.117,207.425)$, respectively (refer to Table II), with less than $0.5\%$ difference across solvers.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-E Real-World Robotarium Experiment", "weight": 1.0} -->

To further demonstrate that the policy can compensate for real-world model mismatch, we deploy NRTO on a Robotarium unicycle robot. The disturbance set is estimated from open-loop rollout residuals, and the resulting NRTO policy applies the affine feedback $u_{k}=\bar{u}_{k}+K_{k}d_{k}$, where $d_{k}$ is estimated online from consecutive state-transition residuals. As shown in Fig. 8--9, the policy substantially reduces accumulated tracking error and steers the robot into the target region, whereas executing the nominal control sequence alone leads to visible drift. Additional details on disturbance estimation are provided in Section V of SM.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-F Franka Manipulator Experiment", "weight": 1.0} -->

We evaluate our framework on a 7-DOF Franka Emika Panda manipulator, a high-dimensional system with $n_{x}=14$ joint positions and velocities and $n_{u}=7$ joint torques, as shown in Fig. 10. The task is to drive the end-effector from a nominal configuration to a goal region while satisfying joint position limits, joint velocity limits, torque bounds, and collision avoidance constraints with respect to spherical obstacles in the workspace. Collision constraints are evaluated using Isaac Sim collision spheres. The feedback gain variables scale as $\mathscr{O}\left(Tn_{u}n_{x}\right)$, yielding $\mathbf{K}_{k}\in\mathbb{R}^{7\times 14}$ per timestep, and obstacle avoidance constraints are enforced at every knot point via the end-effector position obtained from forward kinematics. We report experiments across fixed horizon length $T=30$, number of obstacles $n_{\mathrm{obs}}=1$, and robustness level $\tau=0.01$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-F Franka Manipulator Experiment", "weight": 1.0} -->

As shown in Table III, NRTO-FullADMM achieves a 25.9$\times$ wall-clock speedup over NRTO on this Franka setting, indicating the scalability of NRTO-FullADMM.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced cuNRTO, a GPU-accelerated implementation of nonlinear robust trajectory optimization (NRTO). By exposing fine-grained parallelism in second-order cone (SOC) projections and reusing constant linear operators across inner iterations, cuNRTO enables two accelerated inner solvers, NRTO-DR and NRTO-FullADMM. Across unicycle, quadcopter, and Franka manipulator tasks, the proposed methods achieve substantial wall-clock speedups up to 139.6$\times$ over the baseline while maintaining robust constraint satisfaction.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In future work, we will extend cuNRTO to contact-rich manipulation and locomotion settings involving larger conic programs. We aim to further enhance computational speed by leveraging learning-to-optimize frameworks, ranging from learning-to-warmstart architectures to deep-unfolding techniques. Another direction is to extend the framework's applicability to multi-agent swarms and to address heterogeneous forms of uncertainty.
