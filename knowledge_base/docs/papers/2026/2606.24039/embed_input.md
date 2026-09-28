<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

TurboMPC: Fast, Scalable, and Differentiable Model Predictive Control on the GPU

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Robotics increasingly relies on GPUs for parallel simulation, large-scale learning, and neural-network inference. For model predictive control (MPC) to scale with this paradigm, solvers must run efficiently on this hardware while remaining fast, differentiable, and compatible with expressive MPC formulations used in robotics. We present TurboMPC, a differentiable MPC solver that runs entirely on the GPU and supports state and control inequality constraints, implicit integrators, cross-time-coupled costs, and slack variables. TurboMPC combines sequential quadratic programming (SQP), an alternating direction method of multipliers (ADMM) inner solver, implicit differentiation, and a co-designed JAX-CUDA implementation for efficiency and ease of use. In simulation, we validate TurboMPC on constrained planning, humanoid imitation learning, and reinforcement learning with neural-network cost function tasks, achieving up to 15x and 58x speedups over state-of-the-art CPU and GPU differentiable solvers, respectively.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We deploy TurboMPC on a full-scale car for minimum-time racing and find that batched, GPU-accelerated tuning of MPC parameters via Bayesian optimization yields significantly faster driving than a hand-tuned baseline. TurboMPC also scales to planning horizons of over 8000 knot points while maintaining control of the vehicle.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robotics is increasingly powered by scale: large datasets, parallel simulation, and neural networks trained on graphics processing units (GPUs). How can optimization-based model predictive control (MPC) scale with this new computational paradigm?

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

MPC remains one of the most reliable tools for controlling robotic systems, as it enables planning with a model, reasoning about constraints, and reacting to changing conditions. Yet, most high-performance MPC solvers are designed for central processing units (CPUs), where sequential algorithms such as Riccati recursions can exploit the temporal structure of optimal control problems. This CPU-centric design limits the integration of MPC into learning-based pipelines that rely on batching, parallel rollouts, and differentiable architectures at scale.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

While GPU-based differentiable solvers offer a path to scale MPC and bring its structured decision-making into modern learning-based robotics, *useful GPU acceleration is not only a matter of parallel execution*. The solver must also be fast enough for online control and expressive enough to model the dynamics and constraints that determine real-world performance. MPC formulations may require implicit integration for stiff dynamics, control-rate penalties for input smoothness and actuators protection, state inequalities for safety constraints, and slack variables to maintain feasibility. As shown in Table I, existing tools force a tradeoff: GPU-based solvers often restrict the problem class to expose parallelism, while CPU-based solvers support richer formulations and online deployment, with limited scalability.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Solvers on the CPU", "weight": 1.0} -->

MPC solvers have long exploited the time-induced sparsity of optimal control problems (OCPs) via sequential Riccati recursions and factorization approaches, achieving efficient resolution on CPUs, and outperforming general-purpose solvers that do not exploit the OCP structure. In particular, acados supports implicit integrators, inequality constraints, and differentiability. However, relying on a CPU-based implementation limits scalability to larger models and batch sizes.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Solvers on the GPU", "weight": 1.0} -->

GPU-based differentiable solvers for MPC offer a promising path toward scaling and combining optimization-based control and learning. However, existing methods restrict problem classes to leverage both the structure of OCPs and expose parallelism. For example, trajax, mpc.pytorch, and DiffMPC do not handle implicit integrators, cross-time costs, or state inequality constraints. Other GPU-accelerated solvers, whether gradient-based or sampling-based improve throughput or latency, but either lack differentiability or do not support the full set of features needed for many target MPC applications, see Table I.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Co-Design of Solvers and Learning Infrastructure", "weight": 1.0} -->

One barrier to GPU-native MPC is the mismatch between learning infrastructure and solver throughput. JAX provides automatic differentiation and batching that are used in learning pipelines, but incurs per-kernel launch overhead that is significant for iterative solver design. CUDA provides low-overhead kernels needed for efficient GPU execution, but is more difficult to interface. Moreover, the sparsity structure of the problems in the forward and backward passes of a differentiable MPC solver can be different. These requirements require a careful design to unlock an efficient yet practical GPU-accelerated solver (see Section III-E). Our approach addresses this gap through a JAX frontend and fused CUDA backend, using direct sparse factorization as a shared primitive for online control, batched learning, and differentiation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Autonomous Racing", "weight": 1.0} -->

Driving a vehicle at its limits via MPC remains a challenging problem, requiring long-horizon planning with track bound constraints, stiff dynamics, control-rate costs to protect actuators, and slack variables to ensure recursive feasibility despite model mismatch. Recent work has integrated learning and automated MPC tuning into racing pipelines through differentiable or gradient-free methods. However, existing approaches use CPU-only solvers or only partly support GPU acceleration, limiting batching and large-scale tuning.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Autonomous Racing", "weight": 1.0} -->

Other GPU Solvers Standard NLP Solvers TABLE I: Solver features: ✓supported, ✗not supported, ∼ partial.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

We propose TurboMPC, a differentiable GPU-accelerated MPC solver that addresses problems of the form with states $x_{t}\in\mathbb{R}^{n_{x}}$, controls $u_{t}\in\mathbb{R}^{n_{u}}$, optional equality constraints $u_{0}=u_{\rm init}$ and slack variables $\xi_{t}$, and horizon $N$. The binary $\delta_{\xi}\in\{0,1\}$ and the scalar $\gamma_{\xi}>0$ toggle and penalize $\xi_{t}$, respectively.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

The solver supports key features: Control rate costs to smooth inputs and protect actuators Implicit integrators to handle stiff dynamics Inequality constraints for obstacle avoidance, actuator limits, and additional constraints Slack variables to improve recursive feasibility Since the solver is differentiable and runs entirely on the GPU, it can efficiently: plan over long horizons, use expressive costs & constraints (e.g., neural networks), handle high-dimensional systems, and be used in imitation learning (IL), reinforcement learning (RL), and Bayesian optimization (BO) pipelines.

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-B1 Approach", "weight": 1.0} -->

The solver tackles OCP via sequential quadratic programming (SQP). It runs entirely on the GPU and leverages the time-induced sparse structure of OCP to exploit the GPU's parallel computation capabilities. The inner quadratic programs (QPs) in the SQP loop are solved by a custom alternating direction method of multipliers (ADMM) scheme using the Schur complement method. The ADMM scheme is inspired from OSQP, with the primal-update linear systems solved via cuDSS, and slack variables tackled using ideas from to simplify the implementation and avoid extending the size of the problem. Using implicit differentiation, custom vector-Jacobian products (VJP) give gradients of functions of the OCP solution by differentiating the active-set KKT conditions and solving a linear system.

<!-- chunk {"id": "body-0015", "role": "body", "section": "I-B2 Software", "weight": 1.0} -->

The solver is implemented in JAX and CUDA to simplify its use and ensure performance.

<!-- chunk {"id": "body-0016", "role": "body", "section": "I-B3 Results", "weight": 1.0} -->

We demonstrate the full feature set above across simulation results and deployment on a Lexus LC500 vehicle. The results show significant speedups over strong baselines such as the CPU solver acados and a hybrid GPU-CPU solver using OSQP. Some highlights of the on-vehicle results include the efficient and automatic tuning of the parameters of OCP via Bayesian optimization to race significantly faster, and real-time re-planning with horizon $N>8000$, an $8\times$ longer horizon than the largest horizon at which the baseline maintains control of the vehicle.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Differentiable Model Predictive Control", "weight": 1.0} -->

MPC is a planning and control strategy that recursively solves OCP from the current robot state $x_{\textrm{init}}$ and executes the first control input $u_{0}$ of the solution $x:=(x_{t},u_{t})_{t=0}^{N}$, before replanning again from the next robot state $x_{\textrm{init}}$. The OCP depends on parameters $\theta$ that encode the costs $\ell_{t}$ (e.g., weights penalizing the distance to the goal) and constraints $f_{t},g_{t},x_{\textrm{init}}$ (e.g., positions of obstacles or friction coefficients of the vehicle dynamics model).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Forward Pass", "weight": 1.0} -->

OCP is solved for a given parameter $\theta$ to obtain the solution $x$. The solver design is key to efficiently and reliably solve OCP, e.g., via an interior-point method or SQP.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Backward Pass", "weight": 1.0} -->

The sensitivity of the solution with respect to the parameters $\theta$ is computed. One approach is to differentiate through the solver iterations, but this approach can be slow and memory-intensive. Instead, we use implicit differentiation at the converged solution: The primal-dual variables $w=(x,y)$ satisfy the KKT conditions $F(w,\theta)=0$, and sensitivities are obtained by differentiating these conditions. The backward pass then amounts to solving a linear system, which avoids unrolling solver iterates.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Exploiting Time-Induced Sparse Structure", "weight": 1.0} -->

The finite-horizon structure of OCP induces sparse linear systems that MPC solvers exploit through Riccati recursions, structured factorizations, or iterative methods. For explicit dynamics and per-stage costs, the associated KKT systems are block tridiagonal across time. CPU solvers exploit this structure efficiently for single OCP solves, while GPU methods seek parallelism across time, batches, or sparse linear algebra operations. PCG-based solvers and parallel cyclic reduction efficiently solve these block-tridiagonal subclass on GPUs, but control-rate costs, implicit dynamics, and general inequalities, essential in robotics applications and autonomous racing, introduce cross-time couplings or active-set-dependent KKT structures that can break the aforementioned structure.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Exploiting Time-Induced Sparse Structure", "weight": 1.0} -->

Differentiable MPC adds a second structural challenge: the forward and backward passes do not necessarily share the same sparsity structure. For the forward pass, using our ADMM approach, the primal linear systems admit a Schur complement reduction to a block-tridiagonal linear system, whereas the linear systems in the backward pass do not admit this reduction. Thus, linear system solver primitives specialized only to the forward block-tridiagonal system OCP do not directly cover the full differentiable feature set in Table I. TurboMPC therefore uses cuDSS for GPU-friendly sparse direct factorization as a common linear system solver primitive for the forward and backward passes, supporting implicit dynamics, control-rate costs, inequalities, slack variables, and differentiability in one solver. Other supported (but potentially slower) linear system solvers are listed in Table III.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Solver Design and Implementation", "weight": 1.0} -->

The differentiable solver is described in Algorithms -. We solve OCP via SQP \[54, Chapter 18\]. At each SQP iteration, we form a convex approximation of OCP (Section III-A). We solve the resulting QP via an ADMM scheme inspired by OSQP and the slack variables handling of (Section III-B). Then, the next SQP iterate is selected using a backtracking linesearch (Section III-C). Finally, after convergence of the SQP scheme, gradients can be computed using an active-set VJP based on implicit differentiation (Section III-D). Each component has prior art, but the combined and co-designed implementation is what unlocks the performance of this GPU solver. We discuss design choices and implementation details in Section III-E. For compact presentation, we refer the reader to the Appendix for additional details.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A QP Approximation of OCP", "weight": 1.0} -->

At each SQP iterate, we quadratize the cost and linearize the constraints, giving the following approximation of OCP: where $x$ stacks the stage variables $x:=(x_{t},u_{t})_{t=0}^{N},$ and $(P,q,C,c,\underline{G},G,\overline{G})$ are defined in Appendix -B.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A QP Approximation of OCP", "weight": 1.0} -->

Leveraging the sparsity of QP enables an efficient solver for three reasons. First, as the cost of OCP couples only neighboring stages, the matrix $P$ is block-tridiagonal. Second, the matrix $C$ encodes the linearized dynamics and initial-state equality constraints and is block-bidiagonal. Third, the matrix $G$ encodes the linearized pointwise-in-time inequality constraints and is block diagonal.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Solving QP via ADMM", "weight": 1.0} -->

We solve QP via an ADMM scheme that combines OSQP's splitting scheme and the slack variables handling of. We introduce the slack variables $z$^11^ 1 The slack variables $\xi$ should not be confused with the slack variables $z$. The variables $\xi$ relax the inequality constraints. The variables $z$ come from the ADMM scheme and capture the right hand sides of the constraints. and rewrite QP as where $A={\footnotesize\begin{bmatrix}C\\G\end{bmatrix}}$, $l={\footnotesize\begin{bmatrix}c\\\underline{G}\end{bmatrix}}$, and $u={\footnotesize\begin{bmatrix}c\\\overline{G}\end{bmatrix}}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Solving QP via ADMM", "weight": 1.0} -->

Let $y$ be the multipliers associated to the constraints $Ax=z$. The KKT conditions of QP define the primal-dual residuals Our ADMM solver is derived as follows. We introduce the duplicated variables $(\tilde{x},\tilde{z})$ and rewrite QP as where $\mathcal{I}_{\mathcal{C}}$ is the indicator function of a set $\mathcal{C}$, with $\mathcal{I}_{[l,u]}(z):=0$ if $z\in\mathcal{C}$ and $\mathcal{I}_{\mathcal{C}}(z):=+\infty$ otherwise.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Solving QP via ADMM", "weight": 1.0} -->

Let $w$ and $y$ be the dual variables associated with the constraints $\tilde{x}-x=0$ and $\tilde{z}-z=0$, respectively. The augmented Lagrangian is then where $\sigma>0$ and $\rho\succ 0$ are step-size parameters (with $\rho$ diagonal).

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Solving QP via ADMM", "weight": 1.0} -->

ADMM scheme: Our QP solver consists of 1) minimizing $\mathcal{L}_{\sigma,\rho}$ over $(\tilde{x},\tilde{z})$, 2) minimizing $\mathcal{L}_{\sigma,\rho}$ over $(x,z,\xi)$, and 3) updating the multipliers $(w,y)$. By also including an over-relaxation strategy, we obtain the following three updates.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B2 Slack update", "weight": 1.0} -->

Given $\alpha\in$, we first form the over-relaxed variables The slack update then consists of minimizing $\mathcal{L}_{\sigma,\rho}$ over $(x,z,\xi)$, which gives the following updates.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B2 Slack update", "weight": 1.0} -->

First, minimizing $\mathcal{L}_{\sigma,\rho}$ over $x$ gives noting that $w\equiv 0$ (see Appendix -C for details).

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B2 Slack update", "weight": 1.0} -->

Second, we split the equality and inequality constraints into two blocks with the subscripts $f$ and $g$ denoting correspondence to the equality and inequality constraints, respectively.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B2 Slack update", "weight": 1.0} -->

For the equality block, minimizing $\mathcal{L}_{\sigma,\rho}$ over $z_{f}$ results in $z_{f}^{k+1}\leftarrow c,$ and as such we do not store it explicitly. For the inequality block, when minimizing $\mathcal{L}_{\sigma,\rho}$ over $(z_{g},\xi)$, we distinguish two cases: Without slack variables ($\delta_{\xi}=0$), we obtain where $\Pi$ is the standard projection With slack variables ($\delta_{\xi}=1$), by minimizing $\mathcal{L}_{\sigma,\rho}$ over $(z_{g},\xi)$, we get the smoothed projection: Note that $\gamma_{\xi}\to\infty$ recovers the hard projection.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B3 Dual update", "weight": 1.0} -->

It is as follows, where $w$ vanishes after the first iteration, so we only store the multipliers $y$: Step-size parameters selection. The performance of ADMM highly depends on the choice of the step-size parameters $(\sigma,\rho)$. We found the parameter selection rule in to work well in practice. Hence, we fix $\sigma=10^{-6}$ and use with initial $\bar{\rho}=0.1$. We adapt $\bar{\rho}$ every fixed number $k_{\rho}^{\textrm{iter}}\geq 1$ of ADMM iterations to balance the primal and dual residuals.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B3 Dual update", "weight": 1.0} -->

At each scheduled interval, we compute a candidate which we accept ($\bar{\rho}^{k+1}\leftarrow\bar{\rho}_{\textrm{new}}$) if the primal and dual residuals have not yet satisfied the convergence criteria, and if $\max\big(\frac{\bar{\rho}_{\textrm{new}}}{\bar{\rho}^{k}},\frac{\bar{\rho}^{k}}{\bar{\rho}_{\textrm{new}}}\big)$ is higher than a threshold value $k_{\rho}^{\textrm{ratio}}$. The last check measures how large the multiplicative change in $\bar{\rho}$ would be. The threshold values and the bounds in are user and problem dependent.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-C Linesearch and Convergence Check", "weight": 1.0} -->

We use a standard backtracking linesearch as described in \[54, Algorithm 18.3\] and Appendix -D. We terminate the SQP loop once the first-order optimality conditions are sufficiently satisfied, where $\|g(x)\|_{\infty,[\underline{g},\overline{g}]}$ denotes the maximum componentwise violation of the inequality bounds, and $\epsilon_{c}>0$ is a user-defined tolerance: This convergence criterion is standard in the optimization literature.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-D Backward Pass: Computing Sensitivities", "weight": 1.0} -->

We compute sensitivities of the solution $(x,\xi)$ of OCP with respect to parameters $\theta$ via implicit differentation, based on the function theorem (IFT). At convergence of SQP, the solution satisfies the OCP KKT conditions. We differentiate these KKT conditions while keeping the active set fixed, like.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-D Backward Pass: Computing Sensitivities", "weight": 1.0} -->

Active-set KKT system. Let $\mathcal{A}$ denote the set of active inequality constraints at the converged solution. From identifying the active inequality constraints $g_{\mathcal{A}}$, as described in Appendix -E, we rewrite these inequality constraints as equality constraints: where $\Sigma_{\mathcal{A}}$ is diagonal with entries $+1$ for lower-bound activations and $-1$ for upper-bound activations.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-D Backward Pass: Computing Sensitivities", "weight": 1.0} -->

The reduced active-set KKT conditions of OCP are where $L$ is the Lagrangian $L(x,y_{f},y_{\mathcal{A}})=\ell(x)+y_{f}^{\top}f(x)+y_{\mathcal{A}}^{\top}g_{\mathcal{A}}(x).$ We eliminate the slack stationarity condition $\gamma_{\xi}\xi_{\mathcal{A}}+\Sigma_{\mathcal{A}}y_{\mathcal{A}}=0$ in the presence of slack variables. We then write compactly as Gradients computation: We can now use standard techniques to obtain gradients, see e.g.. By the chain rule, differentiating $F(w(\theta),\theta)=0$ with respect to $\theta$ gives The above computation corresponds to a Jacobian-Vector Product (JVP), and requires solving a large linear system.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-D Backward Pass: Computing Sensitivities", "weight": 1.0} -->

Instead, the gradient of a loss $\nabla_{\theta}\mathcal{L}(x_{\theta},\xi_{\theta})$ can be more efficiently computed via a Vector-Jacobian Product (VJP): which also follows from the chain rule, and requires solving the following where $\eta_{y}=(\eta_{y_{f}},\eta_{y_{\mathcal{A}}})$, $H=\nabla_{xx}^{2}L(x,y_{f},y_{\mathcal{A}})$: Linear systems in the forward and backward passes. Note the difference in sparsity structure: Primal Linear System\Adjoint Linear System\For the forward pass, the block $\rho^{-1}I$ is amenable to a Schur reduction with a block-tridiagonal structure. Unfortunately, that block is zero for the backward pass. Eliminating the top left block instead generally destroys block-tridiagonality whenever $H$ contains cross-time coupling from implicit dynamics or control-rate costs.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-D Backward Pass: Computing Sensitivities", "weight": 1.0} -->

Thus, PCG primitives designed for the forward system do not directly apply to our backward pass, motivating the use of cuDSS.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-E Algorithm-Implementation-Learning Co-Design", "weight": 1.0} -->

The development of TurboMPC is a three-way co-design of the optimization algorithm, the GPU implementation, and the learning pipeline. Unlike hardware/control co-design, where mechanical and control tasks have clear physical boundaries, the boundary between solver and differentiable policy here is subtle: the same ADMM splitting that gives the forward pass its block-tridiagonal structure determines whether the backward pass is tractable, and the same cuDSS factorization that solves the primal update also solves the adjoint system. Designing these concurrently, rather than building a fast solver and then asking how to differentiate it, is what allows TurboMPC to simultaneously achieve GPU acceleration, constraint expressiveness, and differentiability.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-E Algorithm-Implementation-Learning Co-Design", "weight": 1.0} -->

The architecture of TurboMPC is summarized in Figure. The JAX layer hosts the outer SQP loop, problem-data linearization via autodiff of $(\ell,f,g,h)$, and vmap-based batching across problem instances. A C++ FFI (Foreign Function Interface) bridge passes JAX-managed device buffers to the CUDA implementation. The CUDA layer hosts the entire ADMM inner loop as a fused implementation, with custom parallel-over-time kernels for matrix-vector products with $P$, $C$, $G$, $A$, $A^{\top}$, $S$ that exploit the time-induced block sparsity established in Section III-A. The same compiled artifact supports online deployment (batch one, low latency) and batched offline evaluation (batch $B$, throughput proportional to GPU occupancy) from a single API.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-E Algorithm-Implementation-Learning Co-Design", "weight": 1.0} -->

Two important co-design choices of TurboMPC are: Linear-system primitive. The forward primal update and the backward linear system both require sparse linear-system solves, but as established in Section III-D the backward system has a structure that rules out the PCG-based primitives prior GPU MPC work relies. We use direct sparse factorization via cuDSS as a uniform primitive across both passes, called from within our fused CUDA ADMM loop through cuDSS's host API. This approach trades a constant-factor solve-time penalty for three benefits: generality across the explicit-vs-implicit and decoupled-vs-coupled-cost axes, robustness near constraint activation where iterative methods can exhibit long-tail convergence, and batched factorization across many problem instances. cuDSS's symbolic factorization is reused across ADMM iterations and refactorized only when $\rho$ adapts.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-E Algorithm-Implementation-Learning Co-Design", "weight": 1.0} -->

Fused CUDA ADMM Loop. An earlier version hosted ADMM in JAX, dispatching only the cuDSS solves to CUDA via FFI. Per-iteration kernel-launch overhead dominated solve time. We fused the entire ADMM loop into a single CUDA implementation that calls cuDSS through its host API and reuses the symbolic factorization across iterations, yielding a $4-8\times$ speedup at batch sizes $256-512$ relative to the JAX-FFI variant while preserving the user-facing JAX API.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-E Algorithm-Implementation-Learning Co-Design", "weight": 1.0} -->

Overall, we jointly select the ADMM splitting, the slack-variable smoothed projection of, and the implicit-differentiation-based backward pass to admit time-induced block sparsity, with a forward-pass linear system whose Schur reduction preserves block-tridiagonality even with implicit dynamics or cross-time costs, both with underlying CUDA for performance and a JAX frontend for easy integration with learning-based tools.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-F Reinforcement and Imitation Learning", "weight": 1.0} -->

TurboMPC can be used as a differentiable policy class for reinforcement learning (RL) and imitation learning (IL): where $R$ is the reward function, $\pi_{0:T}^{\theta}(x_{0})$ is the OCP control-input solution, Sim is a differentiable simulator, and $(\hat{u}_{0},\dots,\hat{u}_{T})$ is expert demonstration data. Compared to black-box neural networks, this MPC policy class leverages optimal-control structure for inductive bias and zero-shot generalization across problem instances. Our GPU-accelerated solver supports the larger batch sizes and expressive models these data-driven workflows might require.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Simulation Experiments", "weight": 1.0} -->

We first validate TurboMPC in simulation using a constrained drone task, a linear-system RL scaling benchmark, a humanoid imitation-learning task, and a neural-network (NN) training task. Timings are collected using an NVIDIA GeForce RTX 5090 GPU and a 12th Gen Intel(R) Core(TM) i9-12900K CPU with Ubuntu 22.04 and CUDA 13.0.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-A Constrained Drone Obstacle Avoidance", "weight": 1.0} -->

We validate that TurboMPC handles state inequalities, control constraints, and slack variables on a 6-DoF drone obstacle-avoidance task with three circular obstacles in $(x,y)$, initial and final state constraints, and control box constraints. Figure 2 shows representative trajectories from running closed-loop simulations from noisy initial states using a straight-line warm start and RK4 integration. Adding slack variables can increase the rate of solver convergence at the cost of increased constraint violation, as the relaxed constraints allow the trajectory to trade feasibility for convergence. We provide a Jupyter notebook that replicates this example and serves as an introductory tutorial.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-A Constrained Drone Obstacle Avoidance", "weight": 1.0} -->

Fig. 2: Drone obstacle avoidance: Closed-loop trajectories from random initial conditions (i.e., seeds).

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-B Linear-System RL Scaling", "weight": 1.0} -->

We next compare TurboMPC against state-of-the-art differentiable MPC baselines: the PyTorch-based iLQR solver mpc.pytorch ^22^ 2 mpc.pytorch excludes comparing on problems with state inequalities, implicit dynamics, or rate costs as it only supports control box constraints. and the C-based solver acados. To enable a comparison against these solvers within their supported problem class, we benchmark on an RL task (Section III-F) including linear-quadratic optimal control problems with control input box inequality constraints. We do not compare against trajax or DiffMPC since these differentiable solvers do not support inequality constraints. The linear quadratic setting represents the common subclass that all the baseline solvers support, enabling a direct comparison of raw solver scaling without confounding factors from nonlinear dynamics such as Hessian approximation quality and linesearch behaviour. While this task is more restrictive than the full feature set TurboMPC supports, this evaluation provides a fair comparison on this easy subclass, with more challenging problem instances in the next sections.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-B Linear-System RL Scaling", "weight": 1.0} -->

Fig. 3: Linear-system RL: mean solve time vs. batch size (left), planning horizon (center), state + control dimension (right) for TurboMPC (blue), acados (red), and mpc.pytorch (green) at umax ∈ {1, 10} with tol = 10−5.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-B Linear-System RL Scaling", "weight": 1.0} -->

Fig. 4: Humanoid SRB IL: (a) weight recovery and (b) imitation loss over gradient steps for TurboMPC across 20 initializations. Closed-loop balancing in MuJoCo with recovered weights: (c) initial perturbed state and (d) reached equilibrium state.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-B Linear-System RL Scaling", "weight": 1.0} -->

The evaluation tackles the RL problem in Section III-F. Timing results measure the evaluation of closed-loop rollouts and reward gradient evaluation through the closed-loop MPC rollouts. The nominal configuration uses: batch size $B=64$, planning horizon $N=40$, episode length $H=50$, and state-control dimensions $(n_{x},n_{u})=$. Then, we sweep $B\in\{1,8,16,32,64,128,256,512,1024\}$, $N\in\{10,20,40,80,160,320\}$, $(n_{x}{+}n_{u})\in\{6,12,24,48,96\}$ and the solver tolerance $\texttt{tol}\in\{10^{-3},10^{-5}\}$, with statistics computed over ten seeds per configuration.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-B Linear-System RL Scaling", "weight": 1.0} -->

The solver tolerance of TurboMPC corresponds to $\epsilon_{c}$ in and the maximum number of ADMM iterations is set to $10^{3}$. Figure 3 compiles the timing results for each solver with solver tolerance $\texttt{tol}=10^{-5}$. This threshold produces both accurate gradients (see cosine similarity plot in Appendix -F) and fast solve times across both TurboMPC and baselines. In contrast, lower tolerances like $\texttt{tol}=10^{-3}$ can be used for deployed applications of TurboMPC (e.g., Fig. 9), where higher speed is desired and accurate gradients are not required.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-B Linear-System RL Scaling", "weight": 1.0} -->

TurboMPC's advantage grows with planning horizon, problem size, and batch size. Compared to mpc.pytorch the gain reaches $14.6\times$ and $9.4\times$ speedups for the forward and backward passes for $(B,N,n_{x},n_{u})=$ with $u_{\max}=1.0$. On the other hand, acados, which exploits efficient CPU linear algebra and parallelization across cores, is the fastest for single-instance forward solves overall, although TurboMPC catches up as the batch size, horizon, and problem size increase. For the batch-size and horizon sweeps, for $u_{\max}\,{=}\,1.0$, TurboMPC is $2.0\times$ and $2.2\times$ faster for the backward pass at batch size $1024$ and horizon $320$, respectively. The speedup is even more significant for $u_{\max}\,{=}\,10.0$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-B Linear-System RL Scaling", "weight": 1.0} -->

On the largest configurations, the baselines fail: mpc.pytorch hits GPU memory limits, and acados cannot compile above $(n_{x}{+}n_{u})=48$. TurboMPC solves all sizes by leveraging GPU parallelism, time-induced sparsity, and cuDSS for the linear system solves. With a $10^{-3}$ tolerance, the results show similar trends, with TurboMPC further outperforming baselines, achieving up to $15\times$ and $58\times$ speedups over acados and mpc.pytorch, respectively, as detailed in Appendix -F.

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-C Differentiability on Constrained Nonlinear Systems", "weight": 1.0} -->

We demonstrate end-to-end differentiability on constrained nonlinear systems via a humanoid imitation-learning (IL) task and a neural-network (NN) training task.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-C Differentiability on Constrained Nonlinear Systems", "weight": 1.0} -->

Humanoid Imitation Learning: We recover expert cost weights $\theta^{\star}\in\mathbb{R}^{18}$ from demonstrations of a Unitree G1 humanoid performing standing balance. Both expert and student MPCs use Single Rigid Body (SRB) centroidal dynamics with state $x\in\mathbb{R}^{12}$, and control $u\in\mathbb{R}^{6}$ (see Appendix -G).

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-C Differentiability on Constrained Nonlinear Systems", "weight": 1.0} -->

Neural Network Training: We train a TurboMPC policy using a neural-network cost function for a 3D point-mass system tracking a periodic zig-zag reference under input bounds $\|u\|_{\infty}\!\leq\!5$. The parameters $\theta$ are the weights of a two-layer neural network that maps the state to the MPC's state-tracking and control-effort cost weights, trained by analytic policy gradient with closed-loop gradients flowing through TurboMPC to maximize a reference tracking reward. With $B=4$ rollouts per Adam step at horizon $N=8$, the policy reduces the two-cycle closed-loop tracking RMSE from $1.2\!\times\!10^{-1}$ m at initialization to $8.3\!\times\!10^{-2}$ m after $500$ gradient steps, with control inputs satisfying constraints throughout. Figure 5 shows the learning curve and the converged closed-loop trajectory. Appendix -H includes additional details.

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-C Differentiability on Constrained Nonlinear Systems", "weight": 1.0} -->

Fig. 5: RL with a trainable MPC policy using a neural-network cost function on a 3D point-mass system tracking a zig-zag reference. (Left) Two-cycle eval RMSE over 500 Adam steps. (Right) Closed-loop trajectory after training: learned policy (blue) vs. untrained initialisation (grey).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Hardware Deployment: Autonomous Racing", "weight": 1.0} -->

Finally, we evaluate TurboMPC on a 2019 Lexus LC 500 vehicle racing along the oval track in Figure 8. This problem involves the full feature set covered by OCP: state and control constraints, cross-time costs on control rates for smoothness, slack variables for recursive feasibility under disturbance, and implicit dynamics constraints to handle stiff dynamics. First, we use TurboMPC to automatically tune the racing controller for faster driving performance via Bayesian optimization. Then, we evaluate the solver's scalability for long horizons.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Hardware Deployment: Autonomous Racing", "weight": 1.0} -->

The vehicle is equipped with a GeForce RTX 4070 Ti Super GPU and an Intel Xeon E2278GE CPU \@3.30GHz with a computer running Ubuntu, with state estimates provided by an OXTS GPS system. The powertrain, drivetrain, and suspension are unchanged from their production configuration. Experiments are performed on a closed-course.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Hardware Deployment: Autonomous Racing", "weight": 1.0} -->

We use a standard single-track vehicle model in curvilinear coordinates. The state and control inputs are parameterized over the track length with a node $(x_{t},u_{t})$ every three meters, where $r$ is the yaw rate, $v$ is the total velocity, $\beta$ is the sideslip, $\omega_{r}$ is the rear wheelspeed, $\Delta F_{z}$ is the load transferred from the front to rear axle, $e$ and $\Delta\varphi$ are the lateral and angle deviations to the reference, $t$ is time, $\delta$ is the steering angle, $\tau_{\textrm{rear}}$ is the total rear axle torque combining engine and braking torques, and $\tau_{\textrm{front}}$ is the rear brake torque. We model tire forces using a Fiala tire model.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Hardware Deployment: Autonomous Racing", "weight": 1.0} -->

$(x_{\textrm{ref}},u_{\textrm{ref}})$ is a state-control reference, and $\alpha$ is a terminal-time penalty.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Hardware Deployment: Autonomous Racing", "weight": 1.0} -->

The racing OCP is solved recursively from the current $(x_{\text{init}},u_{\text{init}})$ and the plan $(u_{0},\dots,u_{N})$ is sent to the vehicle. A low-level controller executes the control $u$ at the current position along the track via linear interpolation of the latest MPC solution.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Hardware Deployment: Autonomous Racing", "weight": 1.0} -->

This racing problem pushes the vehicle to its handling limits. As such, closed-loop performance is highly sensitive to the parameters $\theta=($the tire friction coefficients $(\mu_{\textrm{front}},\mu_{\textrm{rear}})$, the terminal-time penalty $\alpha,$ and the diagonal entries of the state cost $Q$, control cost $R$), motivating the GPU-accelerated Bayesian optimization tuning of Section V-A. We then stress-test the solver for long planning horizons to demonstrate the scalability of TurboMPC in Section V-B.

<!-- chunk {"id": "body-0067", "role": "body", "section": "V-A Auto-tuning of the MPC parameters", "weight": 1.0} -->

To avoid the slow manual tuning of $\theta=(\mu,\alpha,Q,R)$, we apply Bayesian optimization over GPU-batched closed-loop simulations leveraging Optuna's Tree-structured Parzen Estimator (TPE) sampler. The control-rate (or smoothness) cost weights $W$ remain constant to smooth inputs.

<!-- chunk {"id": "body-0068", "role": "body", "section": "V-A Auto-tuning of the MPC parameters", "weight": 1.0} -->

All weights are optimized in log-space over their respective search intervals, with control weights for the torque channels tied together to reduce search dimensionality. At each iteration, a batch of $B=8$ candidate parameter vectors is evaluated in parallel, with each candidate assessed over $N_{\mathrm{seed}}=4$ closed-loop simulations with randomized tire friction coefficients $\mu_{\mathrm{sim}}\in[0.7,1.4]$, initial track positions $s_{0}\in$ m, and initial velocities $v_{0}\in$ m/s, yielding $B\times N_{\mathrm{seed}}=32$ parallel rollouts per batch. The simulation environments are sampled once at start and held fixed throughout, ensuring all candidates are evaluated under identical conditions.

<!-- chunk {"id": "body-0069", "role": "body", "section": "V-A Auto-tuning of the MPC parameters", "weight": 1.0} -->

The objective maximized by TPE is $\mathcal{R}(\theta)=\bar{R}(\theta)-k\cdot\sigma_{R}(\theta)$, where $\bar{R}(\theta)$ and $\sigma_{R}(\theta)$ are the mean and standard deviation of the per-seed rewards $\{R_{j}(\theta)\}_{j=1}^{N_{\mathrm{seed}}}$, and $k=0.5$ balances average performance against consistency across conditions.

<!-- chunk {"id": "body-0070", "role": "body", "section": "V-A Auto-tuning of the MPC parameters", "weight": 1.0} -->

Each per-seed reward is as follows, where $T_{j}\leq T_{\max}$ is the number of steps completed before a spin-out or off-track termination in seed $j$, $T_{\max}$ is the full rollout budget, and $\lambda=0.9$ penalizes each missed step uniformly: The per-step reward is as follows, where $e_{t}$ and $e_{\mathrm{ref}}$ are the actual and reference lateral deviations, respectively, $\delta_{e}=\min(e_{\mathrm{ref}}-e_{\min},\,e_{\max}-e_{\mathrm{ref}})$ is the half-width of the track boundary margin at the reference position, $\beta_{t}$ is the vehicle slip angle, and $v_{t}$ is the longitudinal velocity: The first two terms penalize leaving the track and reaching sideslip values above $\overline{\beta}=0.55~\rm{rad}$, while the third term rewards higher

<!-- chunk {"id": "body-0071", "role": "body", "section": "V-A Auto-tuning of the MPC parameters", "weight": 1.0} -->

The entire rollout pipeline runs on the GPU, with dynamics integration via Diffrax, and the MPC solve and reward accumulation batched together inside a single jax.lax.scan and jax.vmap call across $B\times N_{\mathrm{seed}}$ instances. This GPU parallelism makes Bayesian optimization tractable with more than $256$ trials.

<!-- chunk {"id": "body-0072", "role": "body", "section": "V-A Auto-tuning of the MPC parameters", "weight": 1.0} -->

GPU acceleration enables faster hyperparameter search. Using the default batch size $B=8$ on the GPU, the trial throughput is of ${\approx}150~\rm{trials/hour}$ or $24~\rm{secs./trial}$, while on the CPU the trial rate is of ${\approx}21~\rm{trials/hour}$ or $171~\rm{secs./trial}$. The GPU-over-CPU speedup is of ${\approx}7.12\times$, which represents a per-trial time reduction of ${\approx}86~\rm{secs.}$ The CPU runs used a PCG-based JAX solver backend (i.e., admm_jax_loop_pcg backend for both the forward and backward passes) that we make available with our implementation, see Table III.

<!-- chunk {"id": "body-0073", "role": "body", "section": "V-A Auto-tuning of the MPC parameters", "weight": 1.0} -->

In addition, we verified the GPU scalability by running the Optuna trainings with $B=1024$ batches at a rate of ${\approx}1,029~\rm{trials/hour}$ or $3.5~\rm{secs./trial}$, which represents trial-throughput speedups of ${\approx}6.9\times$ and ${\approx}50\times$ over the 8-batch trainings on the GPU and CPU, respectively.

<!-- chunk {"id": "body-0074", "role": "body", "section": "V-A Auto-tuning of the MPC parameters", "weight": 1.0} -->

Auto-tuned MPC parameters enable faster racing: We select the best BO weights and evaluate them on the vehicle, comparing against a baseline using hand-tuned weights. Figure 6 shows that the auto-tuned weights yield significantly faster racing. The vehicle's speed $v$ is $2.44~\rm{m/sec.}$ faster in average, and the vehicle turns with higher yaw rates $r$. The total torque $\tau_{\textrm{total}}$ is also larger in average, signaling more aggressive driving. This automatic tuning experiment exposes a weakness of the baseline MPC, which tracks the reference control trajectory too closely and brakes at each turn even when the car could drive faster, while TurboMPC's auto-tuned weights enable driving closer to the limits of handling.

<!-- chunk {"id": "body-0075", "role": "body", "section": "V-A Auto-tuning of the MPC parameters", "weight": 1.0} -->

Fig. 6: Auto-tuning enables faster racing. The baseline (blue) brakes conservatively at each turn. The tuned MPC (yellow) drives much faster.

<!-- chunk {"id": "body-0076", "role": "body", "section": "V-A Auto-tuning of the MPC parameters", "weight": 1.0} -->

The baseline and Optuna-tuned MPC parameters are in Table II. The higher terminal time cost weight $\alpha$ and lower control reference tracking weights $(R_{\tau_{\textrm{rear}}},R_{\tau_{\textrm{front}}})$ enable more aggressive driving and deviating from the reference control trajectory if it enables faster racing. Indeed, Figure 6 shows harder braking before each turn and earlier accelerations in the turns using tuned weights. Also, the higher sideslip and angle deviation weights $(Q_{\beta},Q_{\Delta\varphi})$ reduce sideslip and enable better acceleration in the turns. Finally, the tire friction parameters $(\mu_{\textrm{front}},\mu_{\textrm{rear}})$ change slightly, but this change is likely negligible compared to changes in the cost weights (e.g. compare with the larger changes in ).

<!-- chunk {"id": "body-0077", "role": "body", "section": "V-B Scalability to longer planning horizons", "weight": 1.0} -->

Next, we compare TurboMPC against an SQP solver using OSQP as the inner QP solver. This solver is a strong baseline, as its SQP outer loop forms the QP approximations on the GPU, and OSQP uses the multi-threaded Intel MKL PARDISO sparse linear system solver^33^ 3 OSQP-CUDA is known to be performant only for problems substantially larger than ours, so we use the CPU implementation of OSQP.. Both solvers use the same MPC problem formulation, auto-tuned weights from the previous section, and solver hyperparameters, isolating the effect of the inner QP solver on scalability.

<!-- chunk {"id": "body-0078", "role": "body", "section": "V-B Scalability to longer planning horizons", "weight": 1.0} -->

Fig. 7: Solve times across planning horizons N, demonstrating the scalability of TurboMPC to long horizons beyond what the OSQP baseline supports.

<!-- chunk {"id": "body-0079", "role": "body", "section": "V-B Scalability to longer planning horizons", "weight": 1.0} -->

Results in Figure 7 show that the OSQP-based baseline is slower than TurboMPC for longer planning horizons, with the gap widening at longer horizons. Thus, running the solver entirely on the GPU unlocks significant speedups. For example, at $N=1024$ the OSQP-based controller loses control of the vehicle (Fig. 8), while TurboMPC maintains control. On the other hand, TurboMPC scales to planning horizons of $N>8000$ discretization nodes, enabling the controller to anticipate multiple corners ahead within a single MPC solve. These results demonstrate new capabilities in online, very-long-horizon planning.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Discussion, Limitations, and Future Work", "weight": 1.5} -->

Differentiable GPU solvers help integrate MPC into learning pipelines and scale to higher-dimensional systems, longer planning horizons, larger batch sizes, and more expressive objectives, dynamics, and constraints models such as neural networks. However, TurboMPC comes with limitations.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Discussion, Limitations, and Future Work", "weight": 1.5} -->

First, direct sparse factorization methods for solving linear systems pay a constant-factor solve-time overhead relative to iterative methods such as PCG. A hybrid backend that selects PCG for the forward pass and direct factorization elsewhere could recover this advantage.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Discussion, Limitations, and Future Work", "weight": 1.5} -->

Second, TurboMPC supports pointwise inequality constraints, linearized as slab constraints $\underline{G}\leq Gx\leq\overline{G}$ inside the solver. Extending support to conic and complementary constraints would be useful to many problems in robotics (e.g., contact-rich humanoid locomotion without simplified friction-cone box constraints as in our IL experiments), aerospace (e.g., rocket engine thrust pointing constraints), and others.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Discussion, Limitations, and Future Work", "weight": 1.5} -->

Third, TurboMPC's backward pass inherits the advantages but also the limitations of implicit differentation: Gradient discontinuities at active-set transitions can destabilize training and require small learning rates that slow down learning. This is particularly a challenge for long-horizon problems like the racing case where such numerical instabilities can compound over time. The gradients' accuracy relies on the convergence of the forward pass that solves the MPC problem. However, gradient-based optimization may not always converge, motivating the development of robust warm-starting strategies. Implicit differentiation requires constraint Hessian information, which can be expensive to obtain. Better understanding where approximate second-order information is sufficient for successful application of differentiable MPC (our code supports this approximation to help further investigation), where it is necessary, and how second-order information can be efficiently computed, is of interest for future work.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Discussion, Limitations, and Future Work", "weight": 1.5} -->

Finally, TurboMPC currently relies on double precision for numerical robustness. This limits how much it can exploit modern GPUs, which increasingly devote more hardware resources to low-precision compute units for deep learning. We observed that lower precision yields higher numerical errors and degrades solver convergence and gradient accuracy. Future work should co-design problem scaling and mixed-precision linear algebra, so that the solver can better exploit low-precision throughput.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Discussion, Limitations, and Future Work", "weight": 1.5} -->

Fig. 8: At a planning horizon N = 1024, the OSQP baseline (yellow) loses control of the vehicle, while TurboMPC (blue) drives the vehicle successfully throughout the track.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Conclusion", "weight": 1.5} -->

TurboMPC is a differentiable and GPU-accelerated MPC framework that supports state and control inequalities, implicit integrators, cross-time-coupled costs, and slack variables. The solver combines an SQP outer loop with a custom ADMM inner solver, implicit differentiation, and a co-designed JAX-CUDA implementation. We validated TurboMPC in simulation across constrained planning, reinforcement learning, imitation learning, and neural network MPC tasks. We also deployed TurboMPC on a Lexus LC500 autonomous race car, where GPU-batched Bayesian optimization was used to tune controller parameters to drive closer to the vehicle's limits. The solver enabled planning over horizons with more than $8000$ discretization nodes. These results point toward differentiable MPC as a fast, GPU-native, constraint-aware primitive that exploits optimal control structure and can be trained at scale.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Conclusion", "weight": 1.5} -->

\[Mathematical Details of the Solver and Additional Experiment Information\] We describe the solver in further details as follows.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Conclusion", "weight": 1.5} -->

-A Optimal Control Problem ‣ VII Conclusion ‣ TurboMPC: Fast, Scalable, and DifferentiableModel Predictive Control on the GPU") -A ‣ VII Conclusion ‣ TurboMPC: Fast, Scalable, and DifferentiableModel Predictive Control on the GPU") We then provide additional details on our experiments.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Conclusion", "weight": 1.5} -->

-G Humanoid Balancing Imitation Learning -G -H 3D Point-Mass Tracking Training -H

<!-- chunk {"id": "body-0090", "role": "body", "section": "Optimal Control Problem (OCP)", "weight": 1.0} -->

We define the OCP in Sec. I-B and restate it below: where $x_{t}\in\mathbb{R}^{n_{x}}$ and $u_{t}\in\mathbb{R}^{n_{u}}$ are the state and control at node $t=0,\ldots,N$, and the binary $\delta_{\xi}\in\{0,1\}$ toggles the use of slack variables $\xi_{t}$, penalized by the scalar penalty $\gamma_{\xi}>0$.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Optimal Control Problem (OCP)", "weight": 1.0} -->

All the OCP functions are assumed twice continuously differentiable in $(x,u)$.

<!-- chunk {"id": "body-0092", "role": "body", "section": "B QP Approximation", "weight": 1.0} -->

At each SQP iterate $(\bar{x},\bar{u})$, we form a quadratic approximation of the objective and linear approximations of the constraints, yielding the quadratic program (QP) defined in Sec. III-A and restated below: where $x$ stacks the stage variables $x:=(x_{t},u_{t})_{t=0}^{N}$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "B QP Approximation", "weight": 1.0} -->

The $P$, $C$, and $G$ matrices derived from the cost and constraint approximations, are block-tridiagonal, -bidiagonal, and -diagonal, respectively, with dimensions denoted below. $P\succeq 0$ contains the Hessian of the cost quadratic approximation. $C$ encodes the linearized initial and dynamics constraints via $Cx=c$. $G$ encodes the linearized inequality constraints, with optional slack variables, via $\underline{G}\leq Gx+\delta_{\xi}\xi\leq\overline{G}$: Leveraging the sparse structure of $P$, $C$, and $G$ is key to an efficient implementation. The following sections describe other terms in further detail.

<!-- chunk {"id": "body-0094", "role": "body", "section": "B1 Cost", "weight": 1.0} -->

Collecting all terms, the block entries of $P$ are and the linear term $q=(q_{0},\dots,q_{N})\in\mathbb{R}^{(N+1)n}$, with

<!-- chunk {"id": "body-0095", "role": "body", "section": "B2 Equality constraints", "weight": 1.0} -->

The initial state and (optional) control constraints are already linear and define $A_{\mathrm{init}}$ in $C$. The dynamics constraints are linearized and take the form where $A^{-}_{t}$ and $A^{+}_{t}$ are Jacobian blocks of $f_{t}(x_{t},u_{t},x_{t+1},u_{t+1})$ at $(\bar{x}_{t},\bar{u}_{t},\bar{x}_{t+1},\bar{u}_{t+1})$, and The affine term of the equality constraints is then defined as $c=(b_{\mathrm{init}},b_{0},b_{1},\dots,b_{N-1})$.

<!-- chunk {"id": "body-0096", "role": "body", "section": "ADMM", "weight": 1.0} -->

We reformulate the QP as in OSQP. The main formulation is described in Sec. III-B. We further contrast the derivations with and without slack variables below.

<!-- chunk {"id": "body-0097", "role": "body", "section": "C1 ADMM without slack variables (OSQP, $\\delta_{\\xi}=0$)", "weight": 1.0} -->

First, we derive our ADMM scheme for the case without slack variables $(\delta_{\xi},\xi)=$. The scheme follows OSQP.

<!-- chunk {"id": "body-0098", "role": "body", "section": "C1 ADMM without slack variables (OSQP, $\\delta_{\\xi}=0$)", "weight": 1.0} -->

The corresponding augmented Lagrangian is given by Then, applying ADMM consists of minimizing $\mathcal{L}_{\sigma,\rho}$ over $(\tilde{x},\tilde{z})$ minimizing $\mathcal{L}_{\sigma,\rho}$ over $(x,z)$ updating the multipliers $(w,y)$ By also including an over-relaxation strategy, these steps produce the following updates.

<!-- chunk {"id": "body-0099", "role": "body", "section": "C1 ADMM without slack variables (OSQP, $\\delta_{\\xi}=0$)", "weight": 1.0} -->

Over-relaxation: Given $\alpha\in$, let Because $z_{f}^{k}\equiv c$ for all ADMM steps, our implementation does not store $z_{f}$ and substitutes it with $c$ throughout.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Eliminating $w$ and $\\hat{x}$", "weight": 1.0} -->

From (41a ‣ -C ADMM ‣ VII Conclusion ‣ TurboMPC: Fast, Scalable, and DifferentiableModel Predictive Control on the GPU")) and (43a ‣ -C ADMM ‣ VII Conclusion ‣ TurboMPC: Fast, Scalable, and DifferentiableModel Predictive Control on the GPU")), so $w^{k}=0$ and $x^{k}=\hat{x}^{k}$ for all $k\geq 1$. Substituting into the ADMM updates above and unrolling the over-relaxation step yields Algorithm.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Eliminating $w$ and $\\hat{x}$", "weight": 1.0} -->

Linear-system solve via the Schur complement method: The primal update (40 ‣ -C ADMM ‣ VII Conclusion ‣ TurboMPC: Fast, Scalable, and DifferentiableModel Predictive Control on the GPU")) is an equality-constrained QP. Its KKT conditions are where $\nu^{k+1}$ denotes the multipliers associated with the equality constraint $A\tilde{x}=\tilde{z}$.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Eliminating $w$ and $\\hat{x}$", "weight": 1.0} -->

Eliminating $\tilde{z}^{k+1}\mathop{=}\limits^{eq:admm:kkt_primal_z}z^{k}+\rho^{-1}(\nu^{k+1}-y^{k})$, and stacking (47a) and (47c) gives the linear system From the second block row, we obtain which once substituted into (47a) yields the Schur complement system $S\tilde{x}^{k+1}=\eta^{k}$ defined.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Eliminating $w$ and $\\hat{x}$", "weight": 1.0} -->

After solving the linear system, we recover Structure from OCP: We specialize to the OCP QP structure by partitioning to reflect the equality and inequality constraints.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Eliminating $w$ and $\\hat{x}$", "weight": 1.0} -->

Hence, the primal update (40 ‣ -C ADMM ‣ VII Conclusion ‣ TurboMPC: Fast, Scalable, and DifferentiableModel Predictive Control on the GPU")) consists of the steps $\tilde{x}^{k+1}\leftarrow\mathop{\text{Solve}}\limits_{x}\{Sx^{k+1}=\eta^{k}\}$, $(\tilde{z}_{f}^{k+1},\tilde{z}_{g}^{k+1})=(C\tilde{x}^{k+1},G\tilde{x}^{k+1})$, using the Schur complement components

<!-- chunk {"id": "body-0105", "role": "body", "section": "C2 ADMM with slack variables (ADMMSlack, $\\delta_{\\xi}=1$)", "weight": 1.0} -->

We tackle problems with slack variables as follows. While the QP with $\delta_{\xi}=1$ is a quadratic program that could be handled via the OSQP scheme presented previously, this approach is more complicated to implement: the structure of the primal linear system would change and one would need to keep track of the slack variables $\xi$.

<!-- chunk {"id": "body-0106", "role": "body", "section": "C2 ADMM with slack variables (ADMMSlack, $\\delta_{\\xi}=1$)", "weight": 1.0} -->

Instead, we adapt ideas from the ADMMSlack approach to tackle the QP previously defined: with augmented Lagrangian defined before: Then, our ADMM scheme consists of minimizing $\mathcal{L}_{\sigma,\rho}$ over $(\tilde{x},\tilde{z})$ minimizing $\mathcal{L}_{\sigma,\rho}$ over $(x,z,\xi)$ updating the multipliers $(w,y)$ These steps give the following updates, including an over-relaxation strategy similar to the case without slacks.

<!-- chunk {"id": "body-0107", "role": "body", "section": "C2 ADMM with slack variables (ADMMSlack, $\\delta_{\\xi}=1$)", "weight": 1.0} -->

Primal update: Same as in (40 ‣ -C ADMM ‣ VII Conclusion ‣ TurboMPC: Fast, Scalable, and DifferentiableModel Predictive Control on the GPU")) Slack update: Same as in (41 ‣ -C ADMM ‣ VII Conclusion ‣ TurboMPC: Fast, Scalable, and DifferentiableModel Predictive Control on the GPU")), but with where $\widetilde{\Pi}$ and $\Delta\widetilde{\Pi}$ are defined.

<!-- chunk {"id": "body-0108", "role": "body", "section": "C2 ADMM with slack variables (ADMMSlack, $\\delta_{\\xi}=1$)", "weight": 1.0} -->

Dual update: Same as (43 ‣ -C ADMM ‣ VII Conclusion ‣ TurboMPC: Fast, Scalable, and DifferentiableModel Predictive Control on the GPU")) The step in (52 ‣ -C ADMM ‣ VII Conclusion ‣ TurboMPC: Fast, Scalable, and DifferentiableModel Predictive Control on the GPU")) follows from \[50, Lemma 1\]. Specifically, denoting $Z=\hat{z}_{g}^{k+1}+\rho^{-1}_{g}y_{g}^{k}$, with appropriate substitutions, the last result of the proof of \[50, Lemma 1\] shows and (52b ‣ -C ADMM ‣ VII Conclusion ‣ TurboMPC: Fast, Scalable, and DifferentiableModel Predictive Control on the GPU")) then follows from the definitions of $(\widetilde{\Pi},\Delta\widetilde{\Pi})$.

<!-- chunk {"id": "body-0109", "role": "body", "section": "C2 ADMM with slack variables (ADMMSlack, $\\delta_{\\xi}=1$)", "weight": 1.0} -->

The remainder of the derivations to retrieve the steps in Algorithm follow those for the case without slack variables as described previously.\

<!-- chunk {"id": "body-0110", "role": "body", "section": "C3 Step-size parameters selection", "weight": 1.0} -->

The performance of ADMM highly depends on the choice of the step-size parameters $(\sigma,\rho)$. As, we fix $\sigma=10^{-6}$. We also partition $\rho=\operatorname{diag}(\rho_{f}I,\rho_{g}I)$ to reflect the always-active equality block and the inequality block and set with initial $\bar{\rho}=0.1$. We adapt $\bar{\rho}$ to balance primal and dual residuals following an adaptive schedule as described in Sec. III-B.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Line search", "weight": 1.0} -->

We use a standard backtracking linesearch \[54, Chapter 18\]. After each QP subproblem solve formulated at $\tilde{x}=(x,\xi)$ and with solution $\tilde{x}^{*}=(x^{*},\xi^{*})$, we search along the direction $\Delta\tilde{x}=\tilde{x}^{*}-\tilde{x}$. We use the merit function where $\ell(\tilde{x})$ is the total cost, $f(\tilde{x})$ corresponds to equality constraints, and $g(\tilde{x})$ to inequality constraints.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Line search", "weight": 1.0} -->

The penalty parameter is chosen as A candidate step size $\alpha$ is accepted if it satisfies the Armijo-type condition with the directional derivative $D_{\mu}=\nabla\ell(\tilde{x})^{\top}\Delta\tilde{x}-\mu\left(\|f(\tilde{x})\|_{1}+\|[g(\tilde{x})-\bar{g}]_{+}\|_{1}+\|[\underline{g}-g(\tilde{x})]_{+}\|_{1}\right)$ and $\eta=0.4$. Merit values are evaluated in parallel over a set of $\alpha$ values and the largest candidate satisfying the decrease condition is selected. If no finite candidate satisfies the Armijo condition, we take the finite candidate with the smallest merit value.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Backward Pass: Sensitivities Computation", "weight": 1.0} -->

The solution $(x_{\theta},\xi_{\theta})$ to OCP depends on parameters $\theta\in\mathbb{R}^{p}$ through the cost and constraints. To integrate the solver into learning pipelines, we compute gradients of functions of the solution where $\mathcal{L}$ denotes a downstream scalar loss. We use implicit differentiation, computing these gradients through differentiation of the KKT conditions at the converged primal-dual solution, while keeping the active set fixed.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Backward Pass: Sensitivities Computation", "weight": 1.0} -->

In the following, all quantities are evaluated at the converged primal-dual solution, and we suppress explicit dependence on $\theta$ whenever this does not create ambiguity.

<!-- chunk {"id": "body-0115", "role": "body", "section": "E1 Active constraints identification", "weight": 1.0} -->

Let $f(x)=0$ collect all initial and dynamics equality constraints. Let $\mathcal{A}=\underline{\mathcal{A}}\cup\overline{\mathcal{A}}$ denote the set of active inequality constraints. An inequality constraint belongs to $\underline{\mathcal{A}}$ (i.e., it is lower active) if and it belongs to $\overline{\mathcal{A}}$ (i.e., it is upper active) if where $\epsilon_{g}>0$ is a user-defined tolerance, with our code using a combination of $\epsilon_{\textrm{abs}}$ and $\epsilon_{\textrm{rel}}$. The dual check gives the KKT-consistent active side and takes priority, while the proximity to the bounds is used only when the dual side is ambiguous (i.e., $|y_{g_{i}}|<\epsilon_{g}$).

<!-- chunk {"id": "body-0116", "role": "body", "section": "E1 Active constraints identification", "weight": 1.0} -->

From this active-set check, we identify the active constraints as $g_{\mathcal{A}}$.

<!-- chunk {"id": "body-0117", "role": "body", "section": "E1 Active constraints identification", "weight": 1.0} -->

In the presence of slack variables ($\delta_{\xi}=1$), the active constraints are written compactly as so that $S_{i}=\operatorname{sign}(\xi_{i})$ for active softened constraints. Inactive softened constraints have $\xi_{i}=0$ and are not included in the backward KKT system.

<!-- chunk {"id": "body-0118", "role": "body", "section": "E2 Implicit differentiation", "weight": 1.0} -->

We compute the gradients by differentiating the KKT conditions. We denote the active-set Lagrangian by where $y_{f}$ are the multipliers of the equality constraints and $y_{g}$ are the multipliers of the active inequality constraints.

<!-- chunk {"id": "body-0119", "role": "body", "section": "E2 Implicit differentiation", "weight": 1.0} -->

The OCP KKT conditions are We write these conditions compactly as We can now use standard implicit differentiation techniques to obtain gradients. By the chain rule, differentiating $F(w(\theta),\theta)=0$ with respect to $\theta$ gives The above computation corresponds to a Jacobian-Vector Product (JVP), and requires solving a large linear system.

<!-- chunk {"id": "body-0120", "role": "body", "section": "E2 Implicit differentiation", "weight": 1.0} -->

Instead, the gradient of a loss $\nabla_{\theta}\mathcal{L}(x_{\theta},\xi_{\theta})$ can be more efficiently computed via a Vector-Jacobian Product (VJP): which also follows from the chain rule, and requires solving the linear system with $\eta_{y}=(\eta_{y_{f}},\eta_{y_{g}})$ and where $H:=\nabla^{2}_{xx}\left(\ell(x)+y_{f}^{\top}f(x)+y_{\mathcal{A}}^{\top}g_{\mathcal{A}}(x)\right).$ To solve this linear system, we distinguish two cases.

<!-- chunk {"id": "body-0121", "role": "body", "section": "No slack variables $(\\delta_{\\xi},\\xi)=$", "weight": 1.0} -->

When slack variables are disabled, the active inequality constraints are The KKT conditions reduce to with $F(w,\theta)=0$, $w=(x,y)$, and The gradient is then where ${\footnotesize\begin{bmatrix}\eta_{x}\\\eta_{y}\end{bmatrix}}$ solves the linear system $\frac{\partial F}{\partial w}{\footnotesize\begin{bmatrix}\eta_{x}\\\eta_{y}\end{bmatrix}}={\footnotesize\begin{bmatrix}\nabla_{x}\mathcal{L}\\

<!-- chunk {"id": "body-0122", "role": "body", "section": "Slack variables ($\\delta_{\\xi}=1$)", "weight": 1.0} -->

We first eliminate the slack adjoints $\eta_{\xi}$. From the last and second block rows of, By substituting (64 ‣ -E2 Implicit differentiation ‣ -E Backward Pass: Sensitivities Computation ‣ VII Conclusion ‣ TurboMPC: Fast, Scalable, and DifferentiableModel Predictive Control on the GPU")) into the first block row of, we obtain the reduced linear system After solving (65 ‣ -E2 Implicit differentiation ‣ -E Backward Pass: Sensitivities Computation ‣ VII Conclusion ‣ TurboMPC: Fast, Scalable, and DifferentiableModel Predictive Control on the GPU")), $(\eta_{\xi},\eta_{y_{g}})$ are recovered via (64 ‣ -E2 Implicit differentiation ‣ -E Backward Pass: Sensitivities Computation ‣ VII Conclusion ‣ TurboMPC: Fast, Scalable, and DifferentiableModel Predictive Control on the GPU")).

<!-- chunk {"id": "body-0123", "role": "body", "section": "Slack variables ($\\delta_{\\xi}=1$)", "weight": 1.0} -->

If the slack penalty $\gamma_{\xi}$ is also a parameter to differentiate, since the only explicit dependence of $F$ on $\gamma_{\xi}$ is through the stationarity condition $\gamma_{\xi}\xi_{\mathcal{A}}+Sy_{g}=0$,

<!-- chunk {"id": "body-0124", "role": "body", "section": "Solving the linear systems in the backward pass", "weight": 1.0} -->

The backward pass requires solving a linear system that shares the time-induced sparsity of the forward primal updates, including: a block-tridiagonal Hessian, a block-bidiagonal equality Jacobian $\nabla_{x}f$, and a block-diagonal active inequality Jacobian $\nabla_{x}g_{\mathcal{A}}$. However, the forward and backward linear-system solves diverge in the structure of the assembled KKT matrix.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Solving the linear systems in the backward pass", "weight": 1.0} -->

In the forward pass, the $-\rho^{-1}I$ block is derived from the ADMM augmented Lagrangian, while in the backward-pass matrix $\partial F/\partial w$, the bottom right block is zero. The backward pass differentiates the KKT stationarity conditions at the forward-pass converged solution, at which the penalty over the inequality constraints via $\rho$ has no role.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Solving the linear systems in the backward pass", "weight": 1.0} -->

Rather than attempting a Schur reduction on the backward-pass linear system, we assemble the full sparse linear system in CSR (Compressed Sparse Row) format and solve it directly using cuDSS in general-symmetric mode, which handles indefiniteness natively via $LDL^{\top}$ decomposition. This implementation entails our default and fastest GPU backward-solver backend, but we also provide a pure-JAX reference, (i.e., direct_jax_dense) useful for debugging and CPU-only testing. Table III identifies the backends that we make available through our implementation.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Solving the linear systems in the backward pass", "weight": 1.0} -->

We also explored solving the backward pass iteratively by formulating a reduced adjoint QP whose optimality conditions approximate the sensitivity system. This QP takes the form: where the active inequality constraints are absorbed into the Hessian via the penalty term $\gamma_{\xi}$, producing a convex equality-only QP that reuses the forward ADMM infrastructure directly. This approach recovers accurate gradients when the ADMM iterates are converged tightly, but introduces a small bias proportional to the convergence tolerance and the active-set approximation error. In contrast, the direct-backward solve via cuDSS yields the exact sensitivity in a single factorization. Our open-sourced code enables testing these different backward-solve strategies, by choosing between direct- and ADMM-based solver backends (Table III).

<!-- chunk {"id": "body-0128", "role": "body", "section": "Solving the linear systems in the backward pass", "weight": 1.0} -->

admm_jax_loop_pcg admm_jax_loop_pcg_ffi admm_jax_loop_cudss_ffi admm_jax_loop_jax_dense admm_fused_pcg admm_fused_cudss direct_jax_dense† Direct KKT (JAX) direct_cudss_ffi† Direct KKT (cuDSS) TABLE III: QP solver backends. All backends are available for both passes unless marked † (backward only).

<!-- chunk {"id": "body-0129", "role": "body", "section": "Solving the linear systems in the backward pass", "weight": 1.0} -->

Fig. 9: Linear-system RL (tol = 10−3): mean solve time vs. batch size (left), planning horizon (center), state + control dimension (right) for TurboMPC (blue), acados (red), and mpc.pytorch (green) at umax ∈ {1, 10}. TurboMPC’s GPU advantage grows with batch size, problem size, and horizon.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Solving the linear systems in the backward pass", "weight": 1.0} -->

Fig. 10: Linear-system RL: Cosine similarity between computed gradients and finite differencing across solver tolerances.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Linear-System RL Scaling", "weight": 1.0} -->

This section provides additional details regarding scalability and gradient accuracy.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Linear-System RL Scaling", "weight": 1.0} -->

First, concerning scalability, Fig. 9 shows scalability results with tolerance $\texttt{tol}=10^{-3}$. Compared to mpc.pytorch in this case, the gain reaches $24.0\times$ and $14.7\times$ speedups for the forward and backward passes with the nominal configuration and $u_{max}=1.0$. The highest gain achieved corresponds to a $58.1\times$ speedup with $u_{max}=10.0$ for the same nominal configuration. On the other hand, compared to acados, TurboMPC starts to consistently outperform acados at batch sizes $8$--$32$ on the backward pass, achieving $3.6\times$ and $13.3\times$ gains for the backward pass at batch size $1024$, with $u_{max}=1.0$ and $u_{max}=10.0$, respectively.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Linear-System RL Scaling", "weight": 1.0} -->

The highest gain compared to acados is a $15.1\times$ speedup for the backward pass for $(B,N,n_{x},n_{u})=$ with $u_{max}=10.0$. These results demonstrate the superior speedup performance that TurboMPC can achieve at deployment, when more computational effort lies on the forward than the backward pass.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Linear-System RL Scaling", "weight": 1.0} -->

Concerning the backward pass, we evaluate the accuracy of the gradients computed by TurboMPC against finite differences approximations depending on the solver tolerance. Fig. 10 reports the results for the nominal configuration with $u_{max}=1.0$ and statistics computed over 100 problem instances. The gradient accuracy increases with tighter tolerances. The outlier values can show low-primal feasibility solution due to the random seeds, or gradient discontinuities due to the solution landing on a constraint boundary that turns the active set ambiguous. Nonetheless, as noticed before, a tolerance below $10^{-5}$ produces accurate gradients. This analysis motivates future work to improve gradients computation at coarser tolerances.

<!-- chunk {"id": "body-0135", "role": "body", "section": "G1 State and control", "weight": 1.0} -->

The control $u_{t}=(f_{L,t},f_{R,t})\in\mathbb{R}^{6}$ includes the left, $f_{L,t}$, and right, $f_{R,t}$, foot contact forces in the world frame.

<!-- chunk {"id": "body-0136", "role": "body", "section": "G2 Single Rigid Body (SRB) dynamics", "weight": 1.0} -->

The SRB dynamics are governed: where $m=33.34$ kg is the total robot mass, $g=(0,0,-9.81)$ m/s^2^ is the gravity acceleration vector, $I\in\mathbb{R}^{3\times 3}$ is the body-frame inertia tensor, and $r_{L},r_{R}\in\mathbb{R}^{3}$ are contact position vectors from CoM to the corresponding feet.

<!-- chunk {"id": "body-0137", "role": "body", "section": "G2 Single Rigid Body (SRB) dynamics", "weight": 1.0} -->

The ZYX convention relates body-frame angular velocity $\omega_{t}$ to Euler angle rates via: This parameterization avoids 3D rotation matrix Lie group complexity, and has a singularity at $\theta_{t}=\pm\pi/2$ (gimbal lock) that does not occur during balance recovery. The parameterization is a deliberate simplification, acknowledging that unit quaternions (or another (SO)-consistent representation) would be the representation of choice for robust full locomotion with large rotations.

<!-- chunk {"id": "body-0138", "role": "body", "section": "G2 Single Rigid Body (SRB) dynamics", "weight": 1.0} -->

We use a 4th-order Runge-Kutta (RK4) scheme with $\Delta t=0.025~\rm{secs.}$: $x_{t+1}=\Phi(x_{t},u_{t}),$ where $\Phi(\cdot)$ is a function of the continuous-time SRB dynamics in (68 dynamics ‣ -G Humanoid Balancing Imitation Learning ‣ VII Conclusion ‣ TurboMPC: Fast, Scalable, and DifferentiableModel Predictive Control on the GPU")) via the RK4 coefficients.

<!-- chunk {"id": "body-0139", "role": "body", "section": "G3 Optimal Control Problem", "weight": 1.0} -->

We solve the OCP where $\delta x_{t}=x_{t}-x_{\text{ref}}$, $\delta u_{t}=u_{t}-u_{\text{ref}}$, and $\theta\in\mathbb{R}^{12}$ represents the learnable cost weights used to parameterize the state cost matrix $Q(\theta)$, $R=\mathrm{diag}(10^{-3},\ldots,10^{-3})\in\mathbb{R}^{6\times 6}$ is a control cost matrix, and $N=20$ is the horizon length.

<!-- chunk {"id": "body-0140", "role": "body", "section": "G4 Learnable cost weights", "weight": 1.0} -->

To ensure positive semi-definiteness, we parameterize the weights in log-space: The log-space parameterization ensures positivity by construction and allows the optimizer to work in an unconstrained search space.

<!-- chunk {"id": "body-0141", "role": "body", "section": "G5 Friction cone as box bounds", "weight": 1.0} -->

Friction cone constraints are approximated as independent box bounds: Horizontal forces: $|f_{x}|,|f_{y}|\leq 240$ N Vertical forces: $0\leq f_{z}\leq 400$ N The box structure avoids second-order cone constraints and is directly compatible with TurboMPC.

<!-- chunk {"id": "body-0142", "role": "body", "section": "G6 WBC approximation", "weight": 1.0} -->

We implement a SRB MPC that outputs desired ground reaction forces $f_{L,t},f_{R,t}$ mapped to joint torques using a static whole-body inverse-dynamics approximation on the full MuJoCo model: where $f_{\text{des},t}=(f_{L,t},f_{R,t})$, $h$ is the MuJoCo bias-force vector (gravity + Coriolis + centrifugal), and $J_{\text{feet}}$ is the stacked translational foot Jacobian. The operator $(\cdot)_{\text{ID}}$ selects actuated joints (29 DoF) from generalized coordinates (35 DoF). This setting corresponds to a quasi-static WBC assumption with $\dot{q}=0$ and $\ddot{q}=0$, and it is intentionally used as a bridge from centroidal MPC to full-body torque commands during balance-recovery experiments. A dynamic acceleration-level WBC is deferred to a walking-phase implementation as future work.

<!-- chunk {"id": "body-0143", "role": "body", "section": "G7 MuJoCo validation protocol", "weight": 1.0} -->

We validate the SRB-to-WBC pipeline in MuJoCo with three modes: Kinematic replay: set floating-base pose from SRB states, no physics stepping.

<!-- chunk {"id": "body-0144", "role": "body", "section": "G7 MuJoCo validation protocol", "weight": 1.0} -->

Open-loop physics: apply precomputed WBC torques and run forward dynamics.

<!-- chunk {"id": "body-0145", "role": "body", "section": "G7 MuJoCo validation protocol", "weight": 1.0} -->

Closed-loop physics: apply with $q_{\text{des}}=0$, $\dot{q}_{\text{des}}=0$ for nominal standing. $K_{p}$ and $K_{d}$ are diagonal, joint-group-dependent PD feedback gains: with units N$\cdot$m/rad and N$\cdot$m$\cdot$s/rad, respectively.

<!-- chunk {"id": "body-0146", "role": "body", "section": "G7 MuJoCo validation protocol", "weight": 1.0} -->

The open-loop mode validates short-horizon feasibility but drifts over longer horizons due to model mismatch and lack of feedback. The closed-loop mode reduces drift and is used as a practical validation mode. Future work includes using time-varying contact schedules and dynamic WBC for walking.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Neural Network Training", "weight": 1.0} -->

We use TurboMPC as a differentiable MPC policy with a neural-network cost function for a constrained 3D point-mass tracking task. The state is $x=(p,v)\in\mathbb{R}^{6}$, where $p\in\mathbb{R}^{3}$ is the position and $v\in\mathbb{R}^{3}$ is the velocity. The control is the thrust vector $u\in\mathbb{R}^{3}$. The dynamics are a unit-mass double integrator discretized with forward Euler at $\Delta t=0.1$, with thrust box constraints $\|u_{t}\|_{\infty}\leq 5$ N. The MPC planning horizon is $N=8$, and the closed-loop RL training rollout horizon is $H=8$.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Neural Network Training", "weight": 1.0} -->

The reference is a periodic zig-zag trajectory defined by six waypoints. Each waypoint is held for four control steps. After reaching the last waypoint, the reference reverses through the waypoint sequence. This gives the $40$-step cycle in Table IV. At each MPC call, the reference window contains the next $N+1$ waypoint targets from the current phase.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Neural Network Training", "weight": 1.0} -->

The learned parameters $\theta$ are the weights of a two-layer neural network with one hidden layer, $6\rightarrow 8\rightarrow 81.$ The hidden activation is $\tanh$. The first-layer weights are initialized i.i.d. from a zero-mean Gaussian with standard deviation $0.5$, all biases and the output layer weights are initialized to zero. Thus, at initialization the network outputs zero log-multipliers and the controller recovers the default MPC cost prior $(Q_{t}^{\theta},R_{t}^{\theta})=(I_{6},10^{-3}I_{3})$ for all stages $t$. The network output is reshaped as a $(N+1)\times 9$ matrix, providing time-varying cost weights.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Neural Network Training", "weight": 1.0} -->

The policy applies only the first control $\pi_{\theta}(x_{i})=u_{0}^{\star}$ before resolving the MPC problem at the next state. The exponential parameterization keeps all MPC cost weights positive while allowing unconstrained optimization over $\theta$.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Neural Network Training", "weight": 1.0} -->

Training minimizes the expected closed-loop tracking loss The phase $i_{0}$ is sampled uniformly over one reference cycle. Initial states $x_{0}$ are sampled near the reference: the initial position is the waypoint at phase $i_{0}$ plus uniform perturbation in $[-0.03,0.03]^{3}$, and the initial velocity is sampled uniformly in $[-0.05,0.05]^{3}$. We optimize with Adam using batch size $B=4$, learning rate $3\times 10^{-3}$, and $500$ gradient steps.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Neural Network Training", "weight": 1.0} -->

We use analytic policy gradients to train the neural network, which flow through the closed-loop rollout, with derivatives propagated through each MPC solution used by the policy.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Neural Network Training", "weight": 1.0} -->

For evaluation, the system starts on the first reference waypoint with zero velocity and is simulated for $80$ closed-loop steps. The reported metric is the position RMSE against the phase-aligned reference. Training takes $30.9$ minutes on an RTX 5090, with a median training step time of $3.2$ seconds. The tracking RMSE is reduced from $1.20\times 10^{-1}$ m at initialization to $8.33\times 10^{-2}$ m after $500$ gradient steps.
