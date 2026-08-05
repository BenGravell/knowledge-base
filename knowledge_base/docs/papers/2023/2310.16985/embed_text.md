<!-- arxiv-full-text:v1 {"arxiv_id": "2310.16985", "source": "ar5iv"} -->

## Introduction

Model-predictive control (MPC) enables reactive and dynamic online control for robots while respecting complex control and state constraints such as those encountered during dynamic obstacle avoidance and contact events. However, despite MPC's many successes, its practical application is often hindered by computational limitations, which can necessitate algorithmic simplifications. This challenge is amplified when dealing with systems that have fast or unstable open-loop dynamics, where high control rates are needed for safe and effective operation.

At the same time, there has been an explosion of interest in tiny, low-cost robots that can operate in confined spaces, making them a promising solution for applications ranging from emergency search and rescue to routine monitoring and maintenance of infrastructure and equipment. These robots are limited to low-power, resource-constrained microcontrollers (MCUs) for their computation. As shown in Figure 2, these microcontrollers feature orders of magnitude less processor speed, RAM,and flash memory compared to the CPUs and GPUs available on larger robots and, historically, were not able to support the real-time execution of computationally or memory-intensive algorithms. Consequently, many of the examples in the literature of intelligent robot behaviors being executed on these tiny platforms rely on off-board computers.

Figure 1: TinyMPC is a fast convex MPC solver that enables real-time optimal control on resource-constrained microcontrollers. We demonstrate its efficacy by performing dynamic obstacle avoidance (top) and recover from 90∘ attitude errors (bottom) on a 27 g Crazyflie 2.1 quadrotor.

Figure 2: A comparison of micro, tiny, and full-scale robot platforms and their associated computational hardware. At the smallest scale, microrobots like the Robobee and HAMR-F use highly constrained 8-bit microcontrollers to execute pre-planned open-loop cyclical gates and wing motions. At large scales, powerful embedded CPUs and GPUs, found onboard the Snapdragon Flight quadrotor or Unitree Go1edu quadruped, enable high performance at the cost of high power requirements. In this work we target tiny robots such as the Crazyflie2.1, DeepPiCarMicro, PIXHAWK PX4, and Petoi Bittle that leverage 32-bit microcontrollers for motion planning and control. These devices are capable of some onboard computation, but feature orders of magnitude less processor speed, as well as RAM and flash memory, than the powerful large-scale embedded CPUs and GPUs.

Several efficient optimization solvers suitable for embedded MPC have emerged in recent years, most notably OSQP and CVXGEN. Both of these solvers have code-generation tools that enable users to create dependency-free C code to solve quadratic programs (QPs) on embedded computers. However, they do not take full advantage of the unique structure of the MPC problem and still have relatively large memory footprints, making them unable to run within the resource constraints of many microcontrollers.

Inspired by the recent success of "TinyML," which has enabled the deployment of neural networks on microcontrollers, we introduce TinyMPC, an MCU-optimized implementation of convex MPC using the alternating direction method of multipliers (ADMM) algorithm. Our approach leverages the structure of the MPC problem by precomputing and caching as much as possible and completely avoiding divisions and matrix inversions online. This approach facilitates rapid computation and has a very small memory footprint, enabling deployment onto resource-constrained MCUs. To the best of the authors' knowledge, TinyMPC is the first MPC solver tailored for execution on MCUs that has been demonstrated onboard a highly dynamic, compute-limited robotic system.

Our contributions include: A novel quadratic programming algorithm that: is optimized for MPC, is matrix-inversion free, and achieves high efficiency and a very low memory footprint. This combination makes it suitable for deployment on resource-constrained microcontrollers.

An open-source solver implementation of TinyMPC in C++ that delivers state-of-the-art real-time performance for convex MPC problems on microcontrollers.

Experimental demonstration on a small, resource-constrained agile quadrotor platform.

This paper proceeds as follows: Section II reviews linear-quadratic optimal control, convex optimization, and ADMM. Section III then derives the core TinyMPC solver algorithm. Benchmarking results and hardware experiments on a Crazyflie quadrotor are presented in Section IV. Finally, we summarize our results and conclusions in Section V.

## Background

### II-A The Linear-Quadratic Regulator

The linear-quadratic regulator (LQR) is a widely used approach for solving robotic control problems. LQR optimizes a quadratic cost function subject to a set of linear dynamics constraints: where $x_{k} \in {\mathbb{R}}^{n}$ $u_{k} \in {\mathbb{R}}^{m}$ are the state and control input at time step $k$, $N$ is the number of time steps (also referred to as the horizon), $A \in {\mathbb{R}}^{n \times n}$ and $B \in {\mathbb{R}}^{n \times m}$ define the system dynamics, $Q \succeq 0$, $R \succ 0$, and $Q_{f} \succeq 0$ are symmetric cost weight matrices and $q$ and $r$ are the linear cost vectors.

Equation has a closed-form solution in the form of a linear feedback controller: $K_{k}$ and $d_{k}$ can be obtained by solving the discrete Riccati equation backwards in time, starting with $P_{N} = Q_{f}$ and $p_{N} = q_{f}$, where $P_{k}$ and $p_{k}$ are the Hessian and linear terms of the cost-to-go (or value) function:

### II-B Convex Model-Predictive Control

Convex MPC extends the LQR formulation to admit additional convex constraints on the system states and control inputs such as joint and torque limits, hyperplanes for obstacle avoidance, and contact constraints: where $\mathcal{X}$ and $\mathcal{U}$ are convex sets. The convexity of this problem means that it can be solved efficiently and reliably, enabling real-time deployment in a variety of control applications including the landing of rockets, legged locomotion, and autonomous driving.

When $\mathcal{X}$ and $\mathcal{U}$ can be expressed as linear equality or inequality constraints, is a QP, and can be put into the standard form: | | $\min\limits_{x \in {\mathbb{R}}^{n}}$ | ${\frac{1}{2}x^{\intercal}Px} + {q^{\intercal}x}$ | | \(5\) |

### II-C The Alternating Direction Method of Multipliers

The alternating direction method of multipliers (ADMM) is a popular and efficient approach for solving convex optimization problems, including QPs like. We provide a very brief summary here and refer readers to for more details.

Given a generic problem: with $f$ and $\mathcal{C}$ convex, we define the indicator function for the set $\mathcal{C}$: We can now form the following equivalent problem by introducing the slack variable $z$: | | $\min\limits_{x}$ | ${f{(x)}} + {I_{\mathcal{C}}{(z)}}$ | | \(8\) | The augmented Lagrangian of the transformed problem is as follows where $\lambda$ is a Lagrange multiplier and $\rho$ is a scalar penalty weight: If we alternate minimization over $x$ and $z$, rather than simultaneously minimizing over both, we arrive at the three-step ADMM iteration, the last step of which is a dual-ascent update on the Lagrange multiplier. These steps can be iterated until a desired convergence tolerance is achieved.

In the special case of a QP, each step of the ADMM algorithm becomes very simple to compute: the primal update is the solution to a linear system, and the dual update is a linear projection. ADMM-based QP solvers, like OSQP, have demonstrated state-of-the-art results.

## The TinyMPC Solver

TinyMPC trades generality for speed by exploiting the special structure of the MPC problem. Specifically, we leverage the closed-form Riccati solution to the LQR problem in the primal update of. Pre-computing and caching this solution allows us to avoid online matrix factorizations and enables very fast performance and a small memory footprint.

### III-A Combining LQR and ADMM for MPC

We solve the following problem, introducing slack variables as in and transforming into the following: | | | ${I_{\mathcal{X}}\left(z_{1:N} \right)} + {{I_{\mathcal{U}}\left(w_{1:{N - 1}} \right)} +}$ | | | | | | $\sum\limits_{k = 1}^{N}\left(\frac{\rho}{2}\left(x_{k} - z_{k} \right)^{\intercal}\left(x_{k} - z_{k} \right) + \right.$ | | | | | | $\left. \lambda_{k}^{\intercal}\left(x_{k} - z_{k} \right) \right) +$ | | | | | | $\sum\limits_{k = 1}^{N - 1}\left(\frac{\rho}{2}\left(u_{k} - w_{k} \right)^{\intercal}\left(x_{k} - w_{k} \right) + \right.$ | | | | | | $\left. \mu_{k}^{\intercal}\left(u_{k} - w_{k} \right) \right)$ | | | where $z$, $w$, $\lambda$, $\mu$ are the state slack, input slack, state dual, and input dual variables over the entire horizon. The primal update for becomes an equality-constrained QP: | | $\min\limits_{x_{1:N},u_{1:{N - 1}}}$ | ${\frac{1}{2}x_{N}^{\intercal}{\overset{\sim}{Q}}_{f}x_{N}} + {{{\overset{\sim}{q}}_{f}^{\intercal}x_{N}} +}$ | | \(14\) | | | $\sum\limits_{k = 1}^{N - 1}$ | ${\frac{1}{2}x_{k}^{\intercal}\overset{\sim}{Q}x_{k}} + {{\overset{\sim}{q}}_{k}^{\intercal}x_{k}} + {\frac{1}{2}u_{k}^{\intercal}\overset{\sim}{R}x_{k}} + {{\overset{\sim}{r}}^{\intercal}u_{k}}$ | | | We leverage a scaled form of by introducing the scaled dual variables $y$ and $g$: We observe that because exhibits the same LQR problem structure as, can be solved. The slack update for becomes a simple linear projection onto the feasible set: Finally, the dual update for simply becomes Figure 3: Comparison of average iteration times (top) and memory usage (bottom) for OSQP and TinyMPC on randomly generated trajectory tracking problems on a Teensy 4.1 development board (ARM Cortex-M7 running at 600MHz with 32-bit floating point support, 7.75Mb of flash, and 512kB of tightly coupled RAM). Error bars show the maximum and minimum time per iteration over all MPC steps executed for a given problem. In (a), the input dimension and time horizon are held constant at m = 4 and N = 10 while the state dimension n varies from 4 to 32. In (b), n = 10 and N = 10 while the m varies from 4 to 32. In (c), n = 10, m = 4 and N varies from 4 to 50. The dotted black line indicates the memory limit of the Teensy 4.1.

### III-B Pre-Computation and Penalty Scaling

Solving the linear system in each primal update is the most expensive step in each ADMM iteration. In our case, this is the solution to the Riccati equation, which has properties we can leverage to significantly reduce computation and memory usage. Given a long enough horizon, the Riccati recursion converges to the solution of the infinite-horizon LQR problem. As such, we can pre-compute a single LQR gain matrix $K_{\text{inf}}$ and cost-to-go Hessian $P_{\text{inf}}$. We then cache the following matrices: | | $C_{1}$ | $= {({R + {B^{\intercal}P_{\text{inf}}B}})}^{- 1}$ | | \(19\) | | | $C_{2}$ | $= {({A - {BK_{\text{inf}}}})}^{\intercal}$ | | | | | $C_{3}$ | $= {{K_{\text{inf}}^{\intercal}R} - {C_{2}P_{\text{inf}}B}}$ | | | A careful analysis of the Riccati equation then reveals that only the linear terms need to be updated as part of the ADMM iteration: As a result, we can completely avoid matrix factorizations online and only compute matrix-vector products using the pre-computed matrices.

ADMM is also sensitive to the value of the penalty term $\rho$ . Adaptively scaling $\rho$ is standard in solvers like OSQP. However, this requires additional matrix factorizations that we are trying to avoid. Therefore, we pre-compute and cache a set of matrices corresponding to several values of $\rho$. Online, we switch between these cached matrices according to the primal and dual residual values, in a scheme adapted from OSQP. The resulting TinyMPC algorithm is summarized in Algorithm 1.

1:function TinyMPC(input) 2: while not converged do 4: p1: N − 1, d1: N − 1 ← Backward pass via 5: x1: N, u1: N − 1 ← Forward pass via 7: z1: N, w1: N − 1 ← Projected to feasible set 10: q1: N, r1: N − 1, pN ← Update linear cost terms return x1: N, u1: N − 1

## Experiments

Figure 4: Control trajectories during the Extreme Initial Poses experiment. Four sets of pre-clipped PWM Motor commands, ranging from 0 to 65535, are shown for each controller. The black dotted line is the thrust limit. Among the three successful controllers, only TinyMPC can guarantee feasible controls.

Figure 5: Figure-eight tracking at low speed (top) and high speed (bottom) comparing TinyMPC with the two most performant available on the Crazyflie. For slower trajectories, all three controllers resulted in similar performance. For faster trajectories, only TinyMPC was capable of maintaining tracking without crashing. The maximum velocity and attitude deviation from hover with TinyMPC reached 1.5m/s and 20∘, respectively.

We evaluate TinyMPC through two sets of experiments: First, we benchmark our solver against the state-of-the-art OSQP solver on a representative microcontroller, demonstrating improved computational speed and reduced memory footprint. We then test the efficacy of our solver on a resource-constrained nano-quadrotor platform, the Crazyflie 2.1. We show that TinyMPC enables the Crazyflie to track aggressive reference trajectories while satisfying control limits and time-varying state constraints.

### IV-A Microcontroller Benchmarks

We compare TinyMPC and OSQP on random linear MPC problems while varying the state and input dimensions as well as the horizon length.

### IV-A1 Methodology

Experiments are performed on a Teensy 4.1 development board, which has an ARM Cortex-M7 microcontroller operating at 600MHz, 7.75MB of flash memory, and 512kB of RAM. TinyMPC is implemented in C++ using the Eigen matrix library. We leverage OSQP's code-generation feature to generate a C implementation of our problem to run on the microcontroller. Wherever possible, solver parameters were set to equivalent values. Objective tolerances were set to $10^{- 3}$ and constraint tolerances to $10^{- 4}$. The maximum number of iterations for both solvers was set to 4000, and both utilized warm starting. OSQP's solution polishing was disabled to make it faster. Dynamics models, $A$ and $B$, were randomly generated and checked to ensure controllability for all values of state dimension $n$, input dimension $m$, and time horizon $N$.

### IV-A2 Evaluation

Fig. 3 shows the average execution times for both solvers, in which TinyMPC exhibits a maximum speed-up of 8.85x over OSQP. This speed-up allows TinyMPC to perform real-time trajectory tracking while handling input and state constraints. OSQP also quickly exceeded the memory limitations of the MCU, while TinyMPC was able to scale to much larger problem sizes. For example for a fixed input dimension of $m = 4$ and time horizon of $N = 10$, OSQP exceeds 512kB at only a state dimension of $n = 16$, while TinyMPC only used around 400kB at a state dimension of $n = 32$.

### IV-B Hardware Experiments

We demonstrate the efficacy of our solver for real-time execution of dynamic control tasks on a resource-constrained Crazyflie 2.1 quadrotor. We present three experiments: 1) figure-eight trajectory tracking at slow and fast speeds, 2) recovery from extreme initial attitudes, and 3) dynamic obstacle avoidance through online updating of state constraints.

### IV-B1 Methodology

The Crazyflie 2.1 is a 27 g quadrotor. Its main MCU is an ARM Cortex-M4 (STM32F405) clocked at 168MHz with 192kB of SRAM and 1MB of flash. OSQP could not fit within the memory available on this MCU. Instead, we compare against the four controllers shipped with the Crazyflie firmware: Cascaded PID, Mellinger, INDI, and Brescianini. These are reactive controllers that often clip the control input to meet hardware constraints.

All experiments shown were performed in an OptiTrack motion capture environment sending pose data to the Crazyflie at 100 Hz. We ran TinyMPC at 500Hz with the horizon length $N = 15$ for the figure-eight tracking task and the attitude-recovery task. For the obstacle-avoidance task, we sent the location of the end of a stick to the Crazyflie using the onboard radio. Additionally, we reduced the MPC frequency to 100 Hz and increased $N$ to 20. In all experiments, we linearize the quadrotor's dynamics about a hover and represent its attitude with a quaternion using the formulation . We solve a problem with state dimension $n = 12$ and $m = 4$ for the Crazyflie's full state pose and four PWM motor control commands.

### IV-B2 Evaluation----Figure-Eight Trajectory Tracking

We compare the tracking performance of TinyMPC and other controllers with a figure-eight trajectory, as shown in Fig. 5. For the fast trajectory, the maximum velocity and attitude deviation reach 1.5 m/s and 20^∘^, respectively. Only TinyMPC could track the entire reference, while the Mellinger and Brescianini controllers crashed almost immediately.

### IV-B3 Evaluation----Extreme Initial Poses

Fig. 1 (bottom) shows the performance of the Crazyflie when initialized with a 90^∘^ attitude error. TinyMPC displayed the best recovery performance with a maximum position error of 23 cm while respecting the input limits. The PID and Brescianini achieved maximum errors of 40 cm and 65 cm, respectively, while violating input limits (Fig. 4). The other controllers, INDI and Mellinger, failed to stabilize the quadrotor, causing it to crash.

### IV-B4 Evaluation----Dynamic Obstacle Avoidance

We demonstrate TinyMPC's ability to handle time-varying state constraints by avoiding a moving stick (Fig. 1 top). The obstacle constraint was re-linearized about its updated position at each MPC step, thereby allowing the drone to avoid the unplanned movements of the swinging stick. To make it more challenging, we add an additional constraint of the quadrotor's moving within a vertical plane. While avoiding the dynamic obstacle, the Crazyflie only makes a maximum deviation of approximately 5 cm from the vertical plane.

## Conclusions

We introduce TinyMPC, a model-predictive control solver for resource-constrained embedded systems. TinyMPC uses ADMM to handle state and input constraints while leveraging the structure of the MPC problem and insights from LQR to reduce memory footprint and speed up online execution compared to existing state-of-the-art solvers like OSQP. We demonstrated TinyMPC's practical performance on a Crazyflie nano-quadrotor performing highly dynamic tasks with input and obstacle constraints.

Several directions for future work remain: It should be straight-forward to extend TinyMPC to handle second-order cone constraints, which are useful in many MPC applications for modeling thrust and friction cone constraints. We also plan to further reduce TinyMPC's hardware requirements by developing a fixed-point version, since many small microcontrollers lack hardware floating-point support. Finally, to ease deployment, we plan to develop a code-generation wrapper for TinyMPC in a high-level language like Julia or Python, similar to OSQP and CVXGEN.
