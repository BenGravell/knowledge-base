<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

GATO: GPU-Accelerated and Batched Trajectory Optimization for Scalable Edge Model Predictive Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

While Model Predictive Control (MPC) delivers strong performance across robotics applications, solving the underlying (batches of) nonlinear trajectory optimization (TO) problems online remains computationally demanding. Existing GPU-accelerated approaches either parallelize single solves, handle large batches at sub-real-time rates, or sacrifice model generality for speed. This leaves a large gap in solver performance for many state-of-the-art MPC applications that require real-time batches of tens to low-hundreds of solves. As such, we present GATO, an open source, GPU-accelerated, batched TO solver co-designed across algorithm, software, and computational hardware to deliver real-time throughput for these moderate batch size regimes. Our approach leverages a combination of block-, warp-, and thread-level parallelism within and across solves for ultra-high performance. We demonstrate the effectiveness of our approach through a combination of: simulated benchmarks showing speedups of 18-21x over CPU baselines and 1.4-16x over GPU baselines as batch size increases; case studies highlighting improved disturbance rejection and convergence behavior; and finally a validation on hardware using an industrial manipulator.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We open source GATO to support reproducibility and adoption.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model Predictive Control (MPC) is a feedback control strategy which has seen great success in a wide variety of robotic applications. Most implementations of (nonlinear) MPC leverage trajectory optimization (TO) to solve the underlying optimal control problems. Historically, these TO problems are solved through 1st- or 2nd-order optimization methods. Unfortunately, such problems are computationally expensive and only deliver locally optimal solutions. As such, several recent efforts have leveraged careful approximations and simplifications of the underlying optimal control problem, as well as hardware acceleration, most commonly on GPUs, to help overcome these computational limitations. These GPU-accelerated efforts include both the development of 0th order methods that construct sample-based approximate gradients as well as hybrid, 1st-, and 2nd-order methods targeting both the overall solvers, as well as the underlying numerical linear algebra and physics kernels. Importantly, this collection of works demonstrates robust, real-time, real-world usability though numerous deployments onto various modalities of physical robot hardware.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

At the same time, there have been a number of recent applications in which batches of tens to low-hundreds of trajectory optimization solves can be leveraged for state-of-the-art MPC performance. And while many of these results are demonstrated through GPU parallelism, in general, whether through 0th-, 1st-, 2nd-order, or hybrid approaches, existing GPU-accelerated solvers are designed to either parallelize a single solve across a GPU, implement large-scale (e.g., $>$`<!-- -->`{=html}1000) parallel batches of solves, or are special cased for a very limited setup. As such, to the best of the authors' knowledge, for batches of tens to low-hundreds of solves, prior solvers trade off latency, throughput, and generality: some hit kHz rates but only for a few parallel solves; others process large batches but miss real-time targets; still others attain speed by restricting the problem specification (e.g., point-mass models, a single linearization). This fundamentally limits their deployed use, despite their demonstrated real-world promise.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To overcome these challenges, we developed GATO (Figure 1), a GPU-accelerated, batched trajectory optimization solver designed to enable real-time batched solves of tens to low-hundreds of trajectory optimization problems. Our work is inspired by the MPCGPU solver, which demonstrated that GPU-acceleration through careful algorithm-hardware-software co-design can enable long-horizon, real-time performance. While MPCGPU is limited to a single solve per GPU, we designed GATO to solve tens to low-hundreds of problems simultaneously. This is done via block-, warp-, and thread-level parallelism both across and within underlying computations for efficient problem matrix formation, linear system solves, and line search iterate computations.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate the power of this GPU-first framework through a series of simulation benchmarks, case studies, and a hardware demonstration on an industrial manipulator. We find that GATO provides speedups of up to $18-21\times$ over CPU baselines and $1.4-16\times$ over GPU baselines as batch size increases. Our case studies highlight how such batched solves can improve disturbance rejection and convergence behavior of TO and MPC and can run in real-time on robot hardware.

<!-- chunk {"id": "body-0008", "role": "body", "section": "II-A Direct Trajectory Optimization", "weight": 1.0} -->

Trajectory optimization solves an (often) nonlinear optimization problem to compute a robot's path through an environment as a series of states $X\mkern 1.5mu{=}\mkern 1.5mu\{x_{0},\dotsi,x_{N}\}$ and controls $U\mkern 1.5mu{=}\mkern 1.5mu\{u_{0},\dotsi,u_{N-1}\}$ for $x$ $\in\mathbb{R}^{n}$ and $u$ $\in\mathbb{R}^{m}$. These problems model the robot as a discrete-time dynamical system, $x_{k+1}=f(x_{k},u_{k},h)$, with initial condition $x_{0}=x_{s}$ and timestep $h$, and minimize an additive cost function, $J(X,U)$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-A Direct Trajectory Optimization", "weight": 1.0} -->

Recent work has shown that direct methods, which explicitly represent the states, controls, dynamics, and any additional constraints, lead to moderately large nonlinear programs with structured sparsity patterns. These approaches can be greatly accelerated on the GPU, especially as the size of the problem increases.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Direct Trajectory Optimization", "weight": 1.0} -->

Direct methods follow a three-step process which is repeated until convergence: *Step 1:* Form the following quadratic program via a second-order Taylor expansion of the problem along a nominal trajectory, where $Q$, $R$ and $q$, $r$ are the Hessians and gradients of $J$, and $A$ and $B$ are the gradients of $f$, with respect to $x$ and $u$, and $e_{k}=f(x_{k},u_{k},h)-x_{k+1}$: *Step 2:* Compute $\delta X^{*},\delta U^{*}$ by solving the KKT system: where $\delta z_{k}=\begin{bmatrix}\delta x_{k}&\delta u_{k}\end{bmatrix}^{T}$, $\delta z_{N}=\delta x_{N}$, *Step 3:* Apply the update step, $\delta X^{*},\delta U^{*}$, while ensuring descent

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Direct Trajectory Optimization", "weight": 1.0} -->

on the original nonlinear problem through the use of a merit-function and a line-search.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Direct Trajectory Optimization", "weight": 1.0} -->

Within that framework, Adabag et al., leveraged a symmetric stair preconditioner to solve the KKT system through a Schur complement, preconditioned conjugate gradient, iterative linear system solve, and a parallel line search with the L1 merit function: This approach maximizes parallel performance on the GPU, but is customized for solving only a single problem while utilizing the entire GPU. In Section III we develop a computational approach that leverages similar underlying algorithmic approaches but enables high-performance for batches of tens to low hundreds of solves.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-B Schur Complement Iterative Methods", "weight": 1.0} -->

Iterative methods solve the problem $S\lambda^{*}=\gamma$ for a given $S$ and $\gamma$ by iteratively refining an estimate for $\lambda$ up to tolerance $\epsilon$. The most popular of these methods is the conjugate gradient (CG) method, which is used in the current state-of-the-art, GPU-accelerated TO solver, and also for general, large-scale optimization problems on the GPU. The convergence rate of CG is directly related to the spread of the eigenvalues of $S$. Thus, a preconditoning matrix $\Phi\approx S$ is often applied to instead solve the equivalent problem with better numerical properties: $\Phi^{-1}S\lambda^{*}=\Phi^{-1}\gamma$. To do so, the preconditioned conjugate gradient (PCG) algorithm leverages matrix-vector products with $S$ and $\Phi^{-1}$, as well as vector reductions, both parallel friendly operations.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Schur Complement Iterative Methods", "weight": 1.0} -->

The PCG algorithm also requires the linear system $S$ to be symmetric positive definite.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Design and Implementation", "weight": 1.0} -->

In this section, we describe the design of GATO as visualized in Figure 2 and described in the pseudocode in Algorithm 1. The solver architecture is optimized for GPU-parallel computations across tens to low-hundreds of trajectory optimization solves ($M$), each with tens to low-hundreds of timesteps ($N$). This paradigm, as noted in the introduction, is commonly found across robotics applications and is underserved by current solvers.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Design and Implementation", "weight": 1.0} -->

Our overall design is inspired by MPCGPU and leverages a similar GPU-first architecture and overall 3-step design flow. However, while MPCGPU is customized for single-solve performance, we designed a new underlying solver to enable high-performance parallelism across multiple solves without sacrificing solver accuracy. We also implemented a number of additional fine-grained parallelism optimizations both across and within solves. As shown in Section IV this improves performance across all batch sizes.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Design and Implementation", "weight": 1.0} -->

At a high level, our design leverages block-based parallelism to divide up discrete naturally parallel components of each step of our batched solve. Depending on the stage of the solver this either happens at the timestep level or problem level. Within each block we leverage warp- and thread-level intrinsics and parallelism to maximize performance and minimize overheads. Finally, by moving all of the computation onto the GPU we avoid costly I/O penalties. In the remainder of this section we detail our design.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Batched Problem Setup and Line Search", "weight": 1.0} -->

GATO is designed to maximize all possible parallelism arising from the computational structure of the underlying (batched) optimal control problems. This is most apparent in the problem setup and line search steps (shown as steps a and c in Figure 2). Here we must form $S$, $\gamma$, and $\Phi^{-1}$ per equation 6 and solve a line search for the final update to $Z$, namely $Z\leftarrow Z+\alpha^{*}\delta Z^{*}$, under a merit function, $\mathcal{M}$: where $\beta>1$ and $\mathcal{A}$ are positive integer values, with $\mathcal{A}$ representing the number of line search iterates.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Batched Problem Setup and Line Search", "weight": 1.0} -->

Throughout the steps, we compute gradients and Hessians of the costs and dynamics functions across all problems and timesteps ($N*M$ total timesteps), as well as compute the merit function values to support our line search, again requiring underlying cost and dynamics calculations across all problems, timesteps, and line search iterates ($N*M*\mathcal{A}$ total timesteps). As such, we exploit block-based parallelism for each timestep to maximize both the independent nature of these computations, as well as opportunities for within-computation thread-based parallelism for the underlying small-scale linear algebra. We use the GRiD library for efficient dynamics (gradient) computations, which follows a similar computational model.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Batched Problem Setup and Line Search", "weight": 1.0} -->

1:for b = 0…N * M do in parallel blocks 2: Sb, γb, Φb−1 via with parallel threads (III-A) 3:for b = 0…M do in parallel blocks 4: δZ* via with parallel warps of threads (III-B) 5:for b = 0…N * M * 𝒜 do in parallel blocks 6: ℳb via with parallel threads (III-A) 8: αb* via with parallel threads (III-A) Algorithm 1 GATO (Xinit, Uinit, N, M, 𝒜, → X*, U*) Importantly, because all computations to form $S$, $\gamma$, and each timestep's merit function are block-local, only cheap *intra*-block synchronizations are needed. Only a single *grid-wide* synchronization is required to finalize $\Phi^{-1}$, and a block-level reduction is used to compute the merit function for each line search iterate across all batches of solves.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Batched Problem Setup and Line Search", "weight": 1.0} -->

Throughout these computations, temporary variables are computed in fast shared memory and all final matrices and vectors are arranged densely and contiguously in global memory to maximize naturally coalesced loads and stores by the downstream PCG solver. We also reserve the device's persisting L2 cache to reduce global memory access during PCG. Most importantly, only the current system state(s) and goal(s), as well as the final optimized state and control trajectories, incur round-trip CPU-GPU data transfer overheads.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Batched PCG", "weight": 1.0} -->

A key factor of GATO's overall performance is our batched linear system solver which is built around per-block PCG solves with finer-grained warp-level^11^1We note that a "warp" represents 32 contiguous threads on the same GPU-core. These threads work in lock-step due to the design of NVIDIA GPU hardware. By exploiting their native implicit synchronization at the hardware level, further acceleration of software can be achieved. parallel linear algebra. This hardware-optimized design not only improves computational throughput, but also improves memory access patterns over MPCGPU, reduces synchronizations, and increases overall hardware resource utilization both for a single solve and, most importantly, for batches of solves.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Batched PCG", "weight": 1.0} -->

Each CUDA thread block is assigned to solve one linear system. Within a block, warps distribute work over knot points, and individual threads within a warp operate on rows/columns of the per-knot state/control blocks. This mapping eliminates inter-block coordination entirely: all vector updates, matrix-vector multiplications, and local reductions are resolved inside the block, avoiding the use of intra-block synchronization, e.g., the cooperative groups API used. This design improves both per-solve performance and portability across devices and launch contexts. This is because intra-block APIs require all blocks to be co-resident on the GPU, which constrains scalability and is particularly limiting on edge systems with restricted hardware resources.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Batched PCG", "weight": 1.0} -->

All matrices/vectors are packed contiguously in row-major order by batch and knot points, exploiting the block tridiagonal structure of the $S$ and $\Phi^{-1}$ matrices. This yields coalesced loads/stores for warp-strided accesses and makes warp shuffle intrinsics efficient for reductions. We also pad leading dimensions to multiples of the warp size to remove bounds checks and branch divergence. This enables us to implement a *warp-optimized* block tridiagonal matrix-vector multiplication routine that (i) uses shared memory tiles to stage the current and neighboring blocks, (ii) performs thread-parallel fused multiply--adds for the block-dense operations, (iii) pipelines loads to hide any memory latency (through the use of cudaMemcpyAsync), and (iv) avoids atomics or grid-wide barriers. The CUDA kernel's shared-memory footprint, block dimensions, and register usage are also tuned to maintain high occupancy while preventing register spilling for typical state/control sizes seen in MPC applications. As a result, each PCG solve proceeds efficiently and fully independently.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Batched PCG", "weight": 1.0} -->

Finally, we partially unroll all inner loops over small, compile-time dimensions to reduce loop overhead, and compile with aggressive optimization flags (e.g., -O3, -use_fast_math). As shown in Section IV, these choices result in superior performance across our target batch sizes.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Results", "weight": 1.0} -->

In this section, we present a two-part evaluation of GATO. We first test our solver on a number of software benchmarks aimed to evaluate our approach against relevant baselines and explore the scalability of our design. We then demonstrate the usefulness of our solver through case studies of batched trajectory optimization for MPC applications. Our case studies are first demonstrated via simulation ablations. The final case study is also deployed onto a physical KUKA iiwa manipulator. The source code accompanying this evaluation is released open source alongside our solver.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-A Methodology", "weight": 1.0} -->

Results were collected on a high-performance workstation with a $5.73$GHz 24-core AMD Ryzen 9 7900X i9-12900K and a $2.2$GHz NVIDIA GeForce RTX 4090 GPU running Ubuntu 22.04 and CUDA 12.6. Code was compiled with g++11.4, and time was measured using high-precision timeit package around Python wrappers for all CPU and GPU functions to provide realistic timing analysis for future users of our open source software.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-A Methodology", "weight": 1.0} -->

Throughout our experiments, we compare our solver to ablations of itself, the state-of-the-art CPU QP solver OSQP using the Pinocchio dynamics library, and the state-of-the-art GPU solver MPCGPU using the GRiD dynamics library. We note that we also leverage the GRiD library in GATO as mentioned in Section III. All hyperparameter values can be found in our open source code. All solvers used the same cost functions, and solver-specific hyperparameter values were independently optimized.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A Methodology", "weight": 1.0} -->

We exclude Jax-based GPU solvers (e.g., ) from our evaluations as both from their reported results in papers, and from our own evaluations on our computational hardware, they take tens of milliseconds to solve small batches of trajectory optimization problem: often an *order of magnitude slower* than our baselines. Similarly, OSQP's GPU backend is known to not be performant at our target problem sizes and is as such similarly excluded.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B Scalability Benchmarks", "weight": 1.0} -->

We begin with a scalability study on a 6-DoF Neuromeka Indy7 manipulator executing a figure-8 tracking task. At each control step, we solve a batch of $M$ trajectory-optimization problems with a fixed horizon of $N{=}64$, $h{=}0.01\,\text{s}$, warm-started with the previous control step's solution. Figure 3 (left) summarizes these results for $M=[1,2,4,\ldots,128]$ comparing GATO against the aforementioned OSQP CPU baseline and MPCGPU GPU baseline. OSQP never matches the single-problem latency of either GPU method and, while its runtime scales reasonably with problem size, it is consistently the slowest. On the other hand, while MPCGPU is just 1.4$\times$ slower than GATO for a single instance, since it is engineered to occupy the full GPU per solve, MPCGPU's latency grows nearly linearly with batch size, eventually falling behind GATO by a factor of 16$\times$ for batch size $M=128$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B Scalability Benchmarks", "weight": 1.0} -->

Overall, GATO achieves both lower single-solve latency and stronger scaling than baselines across our target range of batch-sizes. This yields an overall $18-21\times$ speedup over our CPU baseline and $1.4-16\times$ over our GPU baseline.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B Scalability Benchmarks", "weight": 1.0} -->

In the next sections, we present three case studies that demonstrate the practical value of GATO's ability to solve batches of tens--to-hundreds of TO problems in real-time.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-C Case Study 1: Online Hyperparameter Optimization", "weight": 1.0} -->

Our first case study addresses hyperparameter selection in MPC, traditionally a time-consuming and sensitive process. We consider motion planning for the 7-DoF KUKA iiwa with horizon $N=64$ and timestep $h=0.05\,\text{s}$, running the solver for 100 SQP iterations from zero-initialized states and controls on 100 randomly sampled points within the robot's workspace.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-C Case Study 1: Online Hyperparameter Optimization", "weight": 1.0} -->

Our batched solver is used to sample over $\rho$, a damping parameter often added to the diagonal of $Q_{k}$ in in deployed trajectory optimization solvers to improve numerical stability. We initialize the single-solve baseline with $\rho=10^{-1}$. For batch size $M$, we initialize $\rho$ by log‑spacing values between $10^{-8}$ and $10^{1}$. In both cases, $\rho$ is adjusted after each SQP iteration based on the status of the line search, similar to the scheme.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-D Case Study 2: Fixed Disturbance Rejection", "weight": 1.0} -->

Our second case study explores disturbance rejection, a common problem in robotic control tasks. Here, a 6-DoF manipulator tracks a figure-8 end-effector trajectory like in IV-B, but now faces an unmodeled constant external force applied at the end effector in the $-Z$ direction.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-D Case Study 2: Fixed Disturbance Rejection", "weight": 1.0} -->

Batched TO enables an "online hypothesize-and-test" strategy: evaluate multiple candidate disturbance models in parallel and apply the control from the most consistent one. At each control step, we solve a batch of $M$ TO problems differing only in the assumed external force, $f_{j}\;\text{for}\;j\in0,M)$. Candidate forces are generated by sampling directions uniformly on a sphere and adding them to the current estimated disturbance, exploring both direction and magnitude around the prior hypothesis. After solving this batch of problems, we use the optimized trajectory whose dynamics model best matches the measured evolution of the robot's state after one control step. We then update our disturbance estimate for our next solve by re-centering it around the selected $f_{j}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-D Case Study 2: Fixed Disturbance Rejection", "weight": 1.0} -->

As shown in Figure [5, this simple sampling approach proves effective, consistent with batched roll-outs as noted in and batched contact estimates as noted. In particular, Figure 5 (left) shows that tracking error and joint velocities decrease with increasing $M$ until reaching a sweet spot at around $M=32$. Beyond this point, increased solve times offset the benefit of finer hypothesis granularity and increase closed-loop error. Figure 5 (right) illustrates end-effector trajectories for a representative 50 N disturbance, where $M=32$ tracks the figure-8 substantially better than a single-solve baseline, while very large batches, e.g., the $M=128$ shown, lose effectiveness due to higher latency.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-E Case Study 3: Planning Under Uncertainty", "weight": 1.0} -->

In our final case study, we consider a 7-DoF KUKA iiwa executing a multi-point pick--and--place task with an *unmodeled* suspended load attached to the end effector (see Figure 6). The swinging payload induces time-varying, direction-dependent forces that degrade controller performance. To account for this, at each control step, and as done in Section IV-D, GATO warm-starts from the previous solution and solves a batch of trajectory-optimization problems in parallel, each conditioned on a different disturbance hypothesis. Controls are then selected or blended according to consistency with the observed motion, and the hypothesis set is re-centered for the next step. Throughout, the task enforces tight accuracy requirements with success requiring the end effector to reach within 5 cm of each goal in under 5 seconds. We also require the sum of joint-velocities to be under 1.0 rad/s. If time is exceeded, the target is considered a failure and we move onto the next target. This experiment demonstrates GATO's robustness and shows why our target batch sizes are practical: they offer sufficient disturbance coverage without sacrificing real-time performance.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-E1 Simulation Studies", "weight": 1.0} -->

In simulation the solver uses a horizon of $N{=}16$ with a timestep $h=0.01\,\text{s}$, and is limited to 5 SQP iterations with a PCG tolerance of $10^{-6}$. We simulate the plant at $1\,\text{kHz}$ (RK4 with $h{=}0.001\,\text{s}$). We use a constant 15kg mass and run 100 scenarios varying pendulum length $\ell\in[0.3,0.7]$ m, initial angle $\|\theta\|\in[0,0.6]$ rad, and damping constant $b\in[0.1,0.6]$ Nms/rad.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-E1 Simulation Studies", "weight": 1.0} -->

Table I summarizes the solver's performance and Figure 7 shows the distribution of solve times for GATO across different batch sizes. We can see that the success rate dramatically increases and the task-completion time falls significantly as $M$ grows from 1 to 8. Following that, performance continues to increase albeit at a slower rate. Ultimately, at our largest batch size of $M=128$ (shown in red), we are able to not only achieve a 99.2% success rate but also solve almost all problems faster than any other solver, with $M=64$ and $32$ (shown in light blue and green) not far behind. Figure 6 provides a visualization of the simulated experiments, with the red and green spheres denoting unreached and reached targets respectively for $M=1$ (left) and $M=32$ (right).

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-E2 Hardware Deployment", "weight": 1.0} -->

Finally, we run two variants of the simulation experiments from IV-E on a physical KUKA iiwa robot: (a) five-target goal reaching with no load at 100Hz, and (b) three-target goal reaching with an unmodeled 4kg load at 1000Hz. Both used horizon $N{=}32$, timestep $h=0.02\,\text{s}$, one SQP iteration, and PCG tolerance of $10^{-6}$. Our goal is to show real-world effectiveness of our GPU-accelerated approach, handling not only unmodeled forces but also control loop delays, system identification errors, and noisy sensor measurements. We compare results from a single solve against a batch size of $M=32$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-E2 Hardware Deployment", "weight": 1.0} -->

As shown in Figure 8, Table II, and our supplementary videos, the batched solver outperforms single solves, reaching targets in less time and successfully rejecting model errors, sensor noise, and the time-varying external disturbance.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In this work, we introduce GATO, an open source, GPU-accelerated, batched TO solver that is co-designed across algorithm, software, and computational hardware to deliver real-time throughput for batches of tens to low-hundreds of solves. GATO achieves its performance through co-designed parallelism at the block-, warp-, and thread-level, taking full advantage of the GPU computational model. Our experiments demonstrate not only superior performance, providing speedups of as much as $18–21\times$ over CPU and $1.4–16\times$ over GPU baselines as batch size increases, but also that such moderate batch sizes are useful for deployed applications, improving convergence, and rejecting disturbances both in simulation and on a physical manipulator.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

There are many promising directions for future work, including: integration with actor-critic reinforcement learning to guide agent exploration, use of branch-and-bound-based methods for contact-implicit trajectory optimization, and evaluation of our approach on mobile robots at the edge using low-power GPU platforms such as the NVIDIA Jetson.
