<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

TinyMPC: Model-Predictive Control on Resource-Constrained Microcontrollers

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Model-predictive control (MPC) is a powerful tool for controlling highly dynamic robotic systems subject to complex constraints. However, MPC is computationally demanding, and is often impractical to implement on small, resource-constrained robotic platforms. We present TinyMPC, a high-speed MPC solver with a low memory footprint targeting the microcontrollers common on small robots. Our approach is based on the alternating direction method of multipliers (ADMM) and leverages the structure of the MPC problem for efficiency. We demonstrate TinyMPC's effectiveness by benchmarking against the state-of-the-art solver OSQP, achieving nearly an order of magnitude speed increase, as well as through hardware experiments on a 27 gram quadrotor, demonstrating high-speed trajectory tracking and dynamic obstacle avoidance. TinyMPC is publicly available at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model-predictive control (MPC) enables reactive and dynamic online control for robots while respecting complex control and state constraints such as those encountered during dynamic obstacle avoidance and contact events. However, despite MPC's many successes, its practical application is often hindered by computational limitations, which can necessitate algorithmic simplifications. This challenge is amplified when dealing with systems that have fast or unstable open-loop dynamics, where high control rates are needed for safe and effective operation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

At the same time, there has been an explosion of interest in tiny, low-cost robots that can operate in confined spaces, making them a promising solution for applications ranging from emergency search and rescue to routine monitoring and maintenance of infrastructure and equipment. These robots are limited to low-power, resource-constrained microcontrollers (MCUs) for their computation. As shown in Figure 2, these microcontrollers feature orders of magnitude less processor speed, RAM,and flash memory compared to the CPUs and GPUs available on larger robots and, historically, were not able to support the real-time execution of computationally or memory-intensive algorithms. Consequently, many of the examples in the literature of intelligent robot behaviors being executed on these tiny platforms rely on off-board computers.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Several efficient optimization solvers suitable for embedded MPC have emerged in recent years, most notably OSQP and CVXGEN. Both of these solvers have code-generation tools that enable users to create dependency-free C code to solve quadratic programs (QPs) on embedded computers. However, they do not take full advantage of the unique structure of the MPC problem and still have relatively large memory footprints, making them unable to run within the resource constraints of many microcontrollers.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inspired by the recent success of "TinyML," which has enabled the deployment of neural networks on microcontrollers, we introduce TinyMPC, an MCU-optimized implementation of convex MPC using the alternating direction method of multipliers (ADMM) algorithm. Our approach leverages the structure of the MPC problem by precomputing and caching as much as possible and completely avoiding divisions and matrix inversions online. This approach facilitates rapid computation and has a very small memory footprint, enabling deployment onto resource-constrained MCUs. To the best of the authors' knowledge, TinyMPC is the first MPC solver tailored for execution on MCUs that has been demonstrated onboard a highly dynamic, compute-limited robotic system.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A novel quadratic programming algorithm that: is optimized for MPC, is matrix-inversion free, and achieves high efficiency and a very low memory footprint. This combination makes it suitable for deployment on resource-constrained microcontrollers.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

An open-source solver implementation of TinyMPC in C++ that delivers state-of-the-art real-time performance for convex MPC problems on microcontrollers.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Experimental demonstration on a small, resource-constrained agile quadrotor platform.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper proceeds as follows: Section II reviews linear-quadratic optimal control, convex optimization, and ADMM. Section III then derives the core TinyMPC solver algorithm. Benchmarking results and hardware experiments on a Crazyflie quadrotor are presented in Section IV. Finally, we summarize our results and conclusions in Section V.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A The Linear-Quadratic Regulator", "weight": 1.0} -->

The linear-quadratic regulator (LQR) is a widely used approach for solving robotic control problems.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A The Linear-Quadratic Regulator", "weight": 1.0} -->

where $x_{k} \in {\mathbb{R}}^{n}$ $u_{k} \in {\mathbb{R}}^{m}$ are the state and control input at time step $k$, $N$ is the number of time steps (also referred to as the horizon), $A \in {\mathbb{R}}^{n \times n}$ and $B \in {\mathbb{R}}^{n \times m}$ define the system dynamics, $Q \succeq 0$, $R \succ 0$, and $Q_{f} \succeq 0$ are symmetric cost weight matrices and $q$ and $r$ are the linear cost vectors.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-B Convex Model-Predictive Control", "weight": 1.0} -->

where $\mathcal{X}$ and $\mathcal{U}$ are convex sets. The convexity of this problem means that it can be solved efficiently and reliably, enabling real-time deployment in a variety of control applications including the landing of rockets, legged locomotion, and autonomous driving.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-C The Alternating Direction Method of Multipliers", "weight": 1.0} -->

The alternating direction method of multipliers (ADMM) is a popular and efficient approach for solving convex optimization problems, including QPs like. We provide a very brief summary here and refer readers to for more details.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-C The Alternating Direction Method of Multipliers", "weight": 1.0} -->

If we alternate minimization over $x$ and $z$, rather than simultaneously minimizing over both, we arrive at the three-step ADMM iteration,

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-C The Alternating Direction Method of Multipliers", "weight": 1.0} -->

the last step of which is a dual-ascent update on the Lagrange multiplier. These steps can be iterated until a desired convergence tolerance is achieved.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-C The Alternating Direction Method of Multipliers", "weight": 1.0} -->

In the special case of a QP, each step of the ADMM algorithm becomes very simple to compute: the primal update is the solution to a linear system, and the dual update is a linear projection. ADMM-based QP solvers, like OSQP, have demonstrated state-of-the-art results.

<!-- chunk {"id": "body-0018", "role": "body", "section": "The TinyMPC Solver", "weight": 1.0} -->

TinyMPC trades generality for speed by exploiting the special structure of the MPC problem. Specifically, we leverage the closed-form Riccati solution to the LQR problem in the primal update of. Pre-computing and caching this solution allows us to avoid online matrix factorizations and enables very fast performance and a small memory footprint.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Combining LQR and ADMM for MPC", "weight": 1.0} -->

where $z$, $w$, $\lambda$, $\mu$ are the state slack, input slack, state dual, and input dual variables over the entire horizon.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Combining LQR and ADMM for MPC", "weight": 1.0} -->

We observe that because exhibits the same LQR problem structure as, can be solved.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Combining LQR and ADMM for MPC", "weight": 1.0} -->

Finally, the dual update for simply becomes

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Pre-Computation and Penalty Scaling", "weight": 1.0} -->

Solving the linear system in each primal update is the most expensive step in each ADMM iteration. In our case, this is the solution to the Riccati equation, which has properties we can leverage to significantly reduce computation and memory usage. Given a long enough horizon, the Riccati recursion converges to the solution of the infinite-horizon LQR problem. As such, we can pre-compute a single LQR gain matrix $K_{\text{inf}}$ and cost-to-go Hessian $P_{\text{inf}}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Pre-Computation and Penalty Scaling", "weight": 1.0} -->

As a result, we can completely avoid matrix factorizations online and only compute matrix-vector products using the pre-computed matrices.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Pre-Computation and Penalty Scaling", "weight": 1.0} -->

ADMM is also sensitive to the value of the penalty term $\rho$. Adaptively scaling $\rho$ is standard in solvers like OSQP. However, this requires additional matrix factorizations that we are trying to avoid. Therefore, we pre-compute and cache a set of matrices corresponding to several values of $\rho$. Online, we switch between these cached matrices according to the primal and dual residual values, in a scheme adapted from OSQP. The resulting TinyMPC algorithm is summarized in Algorithm 1.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Pre-Computation and Penalty Scaling", "weight": 1.0} -->

1:function TinyMPC(input)
2: while not converged do
4: p1: N − 1, d1: N − 1 ← Backward pass via
5: x1: N, u1: N − 1 ← Forward pass via
7: z1: N, w1: N − 1 ← Projected to feasible set
10: q1: N, r1: N − 1, pN ← Update linear cost terms return x1: N, u1: N − 1

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate TinyMPC through two sets of experiments: First, we benchmark our solver against the state-of-the-art OSQP solver on a representative microcontroller, demonstrating improved computational speed and reduced memory footprint. We then test the efficacy of our solver on a resource-constrained nano-quadrotor platform, the Crazyflie 2.1. We show that TinyMPC enables the Crazyflie to track aggressive reference trajectories while satisfying control limits and time-varying state constraints.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-A Microcontroller Benchmarks", "weight": 1.0} -->

We compare TinyMPC and OSQP on random linear MPC problems while varying the state and input dimensions as well as the horizon length.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-A1 Methodology", "weight": 1.0} -->

Experiments are performed on a Teensy 4.1 development board, which has an ARM Cortex-M7 microcontroller operating at 600MHz, 7.75MB of flash memory, and 512kB of RAM. TinyMPC is implemented in C++ using the Eigen matrix library. We leverage OSQP's code-generation feature to generate a C implementation of our problem to run on the microcontroller. Wherever possible, solver parameters were set to equivalent values. Objective tolerances were set to $10^{- 3}$ and constraint tolerances to $10^{- 4}$. The maximum number of iterations for both solvers was set to 4000, and both utilized warm starting. OSQP's solution polishing was disabled to make it faster. Dynamics models, $A$ and $B$, were randomly generated and checked to ensure controllability for all values of state dimension $n$, input dimension $m$, and time horizon $N$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A2 Evaluation", "weight": 1.0} -->

Fig. 3 shows the average execution times for both solvers, in which TinyMPC exhibits a maximum speed-up of 8.85x over OSQP. This speed-up allows TinyMPC to perform real-time trajectory tracking while handling input and state constraints. OSQP also quickly exceeded the memory limitations of the MCU, while TinyMPC was able to scale to much larger problem sizes. For example for a fixed input dimension of $m = 4$ and time horizon of $N = 10$, OSQP exceeds 512kB at only a state dimension of $n = 16$, while TinyMPC only used around 400kB at a state dimension of $n = 32$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B Hardware Experiments", "weight": 1.0} -->

We demonstrate the efficacy of our solver for real-time execution of dynamic control tasks on a resource-constrained Crazyflie 2.1 quadrotor. We present three experiments: 1) figure-eight trajectory tracking at slow and fast speeds, 2) recovery from extreme initial attitudes, and 3) dynamic obstacle avoidance through online updating of state constraints.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B1 Methodology", "weight": 1.0} -->

The Crazyflie 2.1 is a 27 g quadrotor. Its main MCU is an ARM Cortex-M4 (STM32F405) clocked at 168MHz with 192kB of SRAM and 1MB of flash. OSQP could not fit within the memory available on this MCU. Instead, we compare against the four controllers shipped with the Crazyflie firmware: Cascaded PID, Mellinger, INDI, and Brescianini. These are reactive controllers that often clip the control input to meet hardware constraints.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B1 Methodology", "weight": 1.0} -->

All experiments shown were performed in an OptiTrack motion capture environment sending pose data to the Crazyflie at 100 Hz. We ran TinyMPC at 500Hz with the horizon length $N = 15$ for the figure-eight tracking task and the attitude-recovery task. For the obstacle-avoidance task, we sent the location of the end of a stick to the Crazyflie using the onboard radio. Additionally, we reduced the MPC frequency to 100 Hz and increased $N$ to 20. In all experiments, we linearize the quadrotor's dynamics about a hover and represent its attitude with a quaternion using the formulation. We solve a problem with state dimension $n = 12$ and $m = 4$ for the Crazyflie's full state pose and four PWM motor control commands.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-B2 Evaluation----Figure-Eight Trajectory Tracking", "weight": 1.0} -->

We compare the tracking performance of TinyMPC and other controllers with a figure-eight trajectory, as shown in Fig. 5. For the fast trajectory, the maximum velocity and attitude deviation reach 1.5 m/s and 20^∘^, respectively. Only TinyMPC could track the entire reference, while the Mellinger and Brescianini controllers crashed almost immediately.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B3 Evaluation----Extreme Initial Poses", "weight": 1.0} -->

Fig. 1 (bottom) shows the performance of the Crazyflie when initialized with a 90^∘^ attitude error. TinyMPC displayed the best recovery performance with a maximum position error of 23 cm while respecting the input limits. The PID and Brescianini achieved maximum errors of 40 cm and 65 cm, respectively, while violating input limits (Fig. 4). The other controllers, INDI and Mellinger, failed to stabilize the quadrotor, causing it to crash.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B4 Evaluation----Dynamic Obstacle Avoidance", "weight": 1.0} -->

We demonstrate TinyMPC's ability to handle time-varying state constraints by avoiding a moving stick (Fig. 1 top). The obstacle constraint was re-linearized about its updated position at each MPC step, thereby allowing the drone to avoid the unplanned movements of the swinging stick. To make it more challenging, we add an additional constraint of the quadrotor's moving within a vertical plane. While avoiding the dynamic obstacle, the Crazyflie only makes a maximum deviation of approximately 5 cm from the vertical plane.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We introduce TinyMPC, a model-predictive control solver for resource-constrained embedded systems. TinyMPC uses ADMM to handle state and input constraints while leveraging the structure of the MPC problem and insights from LQR to reduce memory footprint and speed up online execution compared to existing state-of-the-art solvers like OSQP. We demonstrated TinyMPC's practical performance on a Crazyflie nano-quadrotor performing highly dynamic tasks with input and obstacle constraints.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Several directions for future work remain: It should be straight-forward to extend TinyMPC to handle second-order cone constraints, which are useful in many MPC applications for modeling thrust and friction cone constraints. We also plan to further reduce TinyMPC's hardware requirements by developing a fixed-point version, since many small microcontrollers lack hardware floating-point support. Finally, to ease deployment, we plan to develop a code-generation wrapper for TinyMPC in a high-level language like Julia or Python, similar to OSQP and CVXGEN.
