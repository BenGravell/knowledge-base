<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

CusADi: A GPU Parallelization Framework for Symbolic Expressions and Optimal Control

Topics include Reinforcement learning, Optimal control, Optimization, Control, Learning, CusADi, Compute unified device architecture.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The parallelism afforded by GPUs presents significant advantages in training controllers through reinforcement learning (RL). However, integrating model-based optimization into this process remains challenging due to the complexity of formulating and solving optimization problems across thousands of instances. In this work, we present CusADi, an extension of the CasADi symbolic framework to support the parallelization of arbitrary closed-form expressions on GPUs with CUDA. We also formulate a closed-form approximation for solving general optimal control problems, enabling large-scale parallelization and evaluation of MPC controllers. Our results show a ten-fold speedup relative to similar MPC implementation on the CPU, and we demonstrate the use of CusADi for various applications, including parallel simulation, parameter sweeps, and policy training.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Using GPUs for robotics is attractive due to their powerful computing and parallelization capabilities compared to CPUs. These advantages are particularly beneficial in training controllers through parallelized simulations and reinforcement learning (RL), evidenced by the success of learned policies in handling complex, high-dimensional tasks \[Miki2022_LearningLocomotion, Cheng2024_ExtremeParkourLegged, Zhuang2023_RobotParkour, Hoeller2020_DeepValueMPC\]. With cheaper compute, it is appealing to begin incorporating model-based techniques and optimization into training, where the sample efficiency, exploration, and interpretability of the policy could all be improved by embedding model-based domain knowledge as part of the learning pipeline \[Jenelten2024_DTC, Grandesso2023_CACTO, Lee2024_RLHumanoidLIPPlanning\].

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Moreover, the barrier to creating model-based controllers has been substantially lowered. There exists an ecosystem of software tools that simplify developing, designing, and tuning controllers, such as OCS2, Crocoddyl, rockit, and casadi\[OCS2, Mastalli2020_crocoddyl, Gillis2020_rockit, Andersson2019_casadi\]. casadi's symbolic framework in particular greatly simplifies the process of formulating the costs, constraints, and dynamics of an optimal control problem (OCP).

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

However, it is difficult to embed these controllers directly into learning environments because these tools are confined to CPU evaluation. Solving optimization problems across thousands of RL agents is complex to implement on the GPU, and computing their solutions efficiently is more challenging still. Generally, GPU parallelization has been used to speedup a single "large" numerical problem by exploiting repeated structures within it (e.g., long-horizon model predictive control (MPC) or a system with high-dimensional states). These can often be decomposed into independent, parallelizable subproblems, such as computing gradients of constraints in trajectory optimization \[Hyatt2017_GPUevolutionaryMPC, Plancher2021_DynamicsGPU, Plancher2019_DDPGPU, Plancher2020_ParallelDDPGPU\] or the matrix factorizations for solving linear systems \[Adabag2023_MPCGPU, Schubiger2020_cuOSQP, Kang2024_FastCertifiableTO\]. These works are specialized to parallelize specific aspects of their numerical problem.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

For RL applications however, the parallelization needed for computational efficiency is not within a single instance or controller, but rather across the thousands of environments in simulation. There are relatively few works that extend computational tools for batch evaluation on the GPU. \\textciteAmos2017_OptNet developed a custom solver for batches of small QPs on the GPU, but does not exploit sparsity patterns present in MPC, and is specialized for solving small dense linear systems in batches. Frameworks like PyTorch and JAX similarly lack mature libraries for sparse matrix algebra \[Bradbury2018_JAX, Paszke2019_Pytorch\]. Although these computations could also be offloaded to the CPU, the limited number of threads and the overhead incurred by CPU-GPU data transfer make this inefficient. For example, solving MPC on the CPU in RL training loops can take weeks for full policy convergence \[Jenelten2024_DTC\].

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In this work, we present CusADi, an extension of the casadi symbolic framework with CUDA for parallel evaluation on the GPU^11^1Repository and videos: CusADi code-generates and compiles symbolic functions from casadi, enabling parallel evaluation for any specified batch size. Algorithms and optimizations formulated symbolically for a single instance can then be evaluated simultaneously for thousands on the GPU. CusADi serves as a bridge for embedding model-based techniques and expressions from casadi into RL environments, offering speedups of up to 10-100x compared to parallel CPU evaluation, depending on data transfer overhead.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We show several examples highlighting robotics applications with CusADi. First, we formulate a closed-form approximation to the OCP that is amenable for parallelization and deploy MPC across thousands of environments in IsaacGym \[Makoviychuk2021_isaacgym\], as shown in Fig. 1, with training iterations roughly 11x faster than in \[Jenelten2024_DTC\]. Second, we demonstrate how dynamic quantities, such as the centroidal momentum or composite rigid-body inertia, can be symbolically expressed in casadi, computed in parallel with CusADi, and used to augment the observations and rewards in a training environment. Lastly, we run custom parallel simulations for a planar quadcopter system to efficiently evaluate parameter sensitivity and the region of attraction.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We summarize our main contributions as follows: We present CusADi, our open-source tool to parallelize arbitrary symbolic functions on the GPU.

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We formulate a closed-form approximation to the optimal control problem for GPU parallelization.

<!-- chunk {"id": "body-0011", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We demonstrate how CusADi can be used for various robotics applications, including parallelized simulation, parameter sweeps, and reinforcement learning.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A casadi", "weight": 1.0} -->

casadi is a software stack designed for gradient-based numerical optimization and is widely used for optimal control \[Andersson2019_casadi\]. Symbolic expressions in casadi are one of two data types: SX or MX. SX expressions in casadi are represented as directed graphs where each node represents an atomic operation, as shown in Fig. 2 (left). These atomic operations are either unary (${\mathbb{R}}\rightarrow{\mathbb{R}}$) or binary (${{\mathbb{R}} \times {\mathbb{R}}}\rightarrow{\mathbb{R}}$), and arbitrary closed-form expressions can be expressed as a finite sequence of these scalar operations. Examples of unary operations are log, cos, and sqrt, and examples of binary operations are addition, multiplication, and atan2. Note that this does not limit SX expressions to scalar inputs or outputs; operations such as matrix multiplication are simply expanded into unary and binary ones between scalar elements of the function.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A casadi", "weight": 1.0} -->

The MX type generalizes the SX type and consists of sequences of operations that are not limited to be scalar unary or binary operations. Matrix expressions can also be transformed into a series of atomic operations on scalar values with the expand functionality in casadi.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A casadi", "weight": 1.0} -->

We chose the casadi stack for parallelization for several reasons. Firstly, casadi fully supports sparse matrix algebra and algorithmic differentiation (AD), ensuring expressions are both efficient and differentiable. This makes it convenient to take Jacobians and Hessians symbolically. While other frameworks such as Pytorch and JAX also support symbolic and differentiable functions, sparse operations are not yet fully mature in either \[Paszke2019_Pytorch, Bradbury2018_JAX\]. Exploiting sparsity is crucial given the structure present in optimal control problems, where typically only a small fraction of the Karush-Kuhn-Tucker (KKT) system has non-zero elements \[Betts1999_SparsityInOCP\]. With casadi, the expression graphs compute only the non-zero outputs for symbolic functions.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A casadi", "weight": 1.0} -->

Secondly, the Opti stack in casadi streamlines the process of defining the variables and parameters of an optimal control problem, providing convenient interfaces to a breadth of solvers, including IPOPT, KNITRO, and OSQP \[Wachter2002_IPOPT, Byrd2006_Knitro, Stellato2020_OSQP\].

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A casadi", "weight": 1.0} -->

Lastly, several robotic toolboxes available are already compatible with casadi, such as spatial_v2 \[Featherstone2007_RBDA\], Pinocchio \[Carpentier2019_Pinocchio\], and GRBDA \[Chignoli2023_GRBDA\]. Rewriting these dynamic libraries and algorithms in a different symbolic framework would require significant and largely unnecessary effort. Expressions computed from these libraries can be exported as a casadi expression graph directly callable from MATLAB, Python, or C++.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B GPU Parallelization", "weight": 1.0} -->

While CPUs have dozens of cores intended for high-speed sequential processing and computation, GPUs consist of thousands of smaller cores with simpler control logic. Consequently, GPUs excel at performing identical operations on large volumes of data. This so-called "single instruction multiple data" (SIMD) parallelism allows GPUs to process many data elements simultaneously, dramatically increasing throughput for parallelizable tasks. Naturally, this architecture has been particularly advantageous in applications large-scale, repetitive computations such as reinforcement learning, graphics processing, and numerical simulation \[Patterson_ComputerArchitecture\]. With interfaces such as NVIDIA's CUDA library, users can directly write programs (kernels) to be evaluated in parallel across the threads of a GPU \[NVIDIA_CUDA\].

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B GPU Parallelization", "weight": 1.0} -->

In Section III, we detail how CusADi code-generates CUDA kernels from symbolic casadi expressions. These kernels are compiled as an externally callable C library with an interface to PyTorch.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-D Sequential Quadratic Programming", "weight": 1.0} -->

After solving the KKT equations of the QP problem in to obtain step direction ${\delta\mathbf{v}_{k}} = {({\delta\mathbf{z}_{k}},{\delta{\mathbf{λ}}_{k}},{\delta{\mathbf{σ}}_{k}})}$, the solution is updated as $\mathbf{v}_{k + 1} = {\mathbf{v}_{k} + {\alpha\delta\mathbf{v}_{k}}}$, where $\alpha$ is a scalar that determines the acceptable step length via backtracking line search methods, such as the Armijo method \[Armijo1966_LineSearch\]. The matrices of the QP subproblem are recomputed with the updated solution and is resolved. This process is repeated until the solution and/or cost converges.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-D Sequential Quadratic Programming", "weight": 1.0} -->

In Section V-A, we present an approximate SQP algorithm that can be expressed in closed-form for GPU parallelization.

<!-- chunk {"id": "body-0021", "role": "body", "section": "CusADi", "weight": 1.0} -->

Our work, which we call CusADi, leverages CUDA kernels and the graph structure of casadi functions to compute any symbolic expression from casadi in parallel with CUDA. The key insight is that the sequence of atomic operations that define a function can be vectorized to operate on tensors of data instead of individual scalar values, as shown in Fig. 2 (right). By writing each vectorized atomic operation sequentially as a CUDA kernel, thousands of function instances can be computed in parallel, limited only by the memory capacity of the GPU and compilation time. Unlike prior works, we also assume all incoming and outgoing data are stored only on the GPU so that no additional time is spent checking or transferring data between devices \[Schubiger2020_cuOSQP, Jenelten2024_DTC\].

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Code Generation", "weight": 1.0} -->

A symbolic casadi function consists of a work vector to store intermediate values, and n_instructions, where each instruction contains three elements: instruction_id (the operation type) instruction_input (the operation input index) instruction_output (the operation output index) The function is evaluated by traversing across the instructions sequentially and performing each operation on the specified indices.^22^2Python example available: Instead of traversing the instructions for evaluation, we programmatically generate strings of CUDA code at each iteration. To do so, we create a map between the casadi operation IDs and their equivalent, vectorized counterparts written in CUDA with the appropriate indices, as shown in 1.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Code Generation", "weight": 1.0} -->

OP_ASSIGN: "work[env_idx + %d] = work[env_idx + %d];", OP_ADD: "work[env_idx + %d] = work[env_idx + %d] + work[env_idx + %d];", OP_SUB: "work[env_idx + %d] = work[env_idx + %d] - work[env_idx + %d];", OP_MUL: "work[env_idx + %d] = work[env_idx + %d] * work[env_idx + %d];", OP_DIV: "work[env_idx + %d] = work[env_idx + %d] / work[env_idx + %d];", OP_NEG: "work[env_idx + %d] = -work[env_idx + %d];", OP_EXP: "work[env_idx +

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Code Generation", "weight": 1.0} -->

%d] = exp(work[env_idx + %d]);", OP_LOG: "work[env_idx + %d] = log(work[env_idx + %d]);", OP_POW: "work[env_idx + %d] = pow(work[env_idx + %d], work[env_idx + %d]);", Listing 1: Subset of the mappings from CasADi instructions keys (instruction_id) to strings of CUDA kernels that vectorize the corresponding operation. env_idx corresponds to the thread index of the kernel, added to the appropriate input/output (%d) index of the work vector.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Code Generation", "weight": 1.0} -->

__global__ void evaluate_kernel (const double *inputs, const int batch_size) { int idx = blockIdx.x * blockDim.x + threadIdx.x; int env_idx = idx * n_w; if (idx < batch_size) { work[env_idx + 0] = inputs[idx * nnz_in + 0]; work[env_idx + 1] = sin(work[env_idx + 0]); work[env_idx + 1] = work[env_idx + 1] + work[env_idx + 0]; work[env_idx + 1] = work[env_idx + 1] * work[env_idx + 1]; outputs[idx * nnz_out + 0] = work[env_idx + 1]; Listing 2: Automatically generated CUDA code for the example CasADi function in Fig. 2. A unique thread idx is assigned for processing data in parallel, calculated from a local thread index and global block index coordinates.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A Code Generation", "weight": 1.0} -->

The if statement ensures that the instructions do not operate on data outside of the allocated batch_size.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Code Generation", "weight": 1.0} -->

After iterating through and vectorizing each instruction, the code is output to a file and compiled with the CUDA Toolkit in C \[NVIDIA_CUDA\]. The programmatically generated code file is shown in 2. This process only needs to be done once, offline, and the compiled library can be called for evaluation in any CUDA compatible environment. By including all the operations in a single kernel, the overhead of starting threads is minimized.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-A Code Generation", "weight": 1.0} -->

This vectorized unrolling of the operations could be written in higher-level languages, but directly compiling low-level CUDA kernels offers the fastest evaluation without any interpreter overhead.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B PyTorch Interface", "weight": 1.0} -->

To access the generated CUDA kernels conveniently, we use PyTorch to call the compiled libraries and store the input/output of vectorized expressions. The software has a mature library of tensor operations that make it convenient to allocate tensors and interface with data on the GPU. Furthermore, this allows CusADi to easily be integrated into RL environments such as \[Makoviychuk2021_isaacgym\], as demonstrated in Section V. Usage examples and tutorials are available in the CusADi repository.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Benchmarking", "weight": 1.0} -->

To evaluate the speedups offered by our GPU parallelization framework, we benchmark the wall clock time of CusADi against serial CPU evaluation, parallel CPU evaluation with the multiprocessing library OpenMP, and with PyTorch. In the same manner as 2, we code generate the casadi function in PyTorch for a single instance and evaluate it as a batch with PyTorch's vmap vectorization method.^33^3We also test with the new torch.compile functionality introduced in PyTorch 2.0. While the speedups are comparable with those of CusADi, the initial JIT compilation of the function can require hours to process, and system recursion limits were hit for functions with more than 1,000 operations. All benchmarks and applications in Section V are conducted on a desktop computer with an Intel i7 10850K processor and NVIDIA 3090 GPU.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Benchmarking", "weight": 1.0} -->

We compare five functions, each with an order of magnitude more operations than the previous one, across a range of batch sizes. Each function evaluates the LDL^T^ decomposition solution to a positive definite linear system \[Boyd2004_ConvexOptimization\]. The speedup of CusADi with respect to serial CPU evaluation (with and without data transfer overhead) is shown in Fig. 3.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Benchmarking", "weight": 1.0} -->

The speedups depend on the complexity of the function (i.e., the total number of operations required) and the batch size. As the batch size increases, the GPU can take advantage of its threads, and parallelization enables speedups that are 1000x faster than serial CPU evaluations. However, the CPU can process operations significantly faster than the GPU, and as the number of sequential computations increases, the advantage of having more parallel threads is reduced.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Benchmarking", "weight": 1.0} -->

At the scale of parallelization typical for RL applications (2,000 - 8,000 environments), the overhead from transferring data between host and device memory is the largest bottleneck. By keeping data entirely on the GPU, CusADi enables speedups from 100-1000x in this regime. For the applications in Section V, the estimated speedups are shown in Table I.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Benchmarking", "weight": 1.0} -->

Speedup [w/o data transfer] TABLE I: Estimated speedups compared to parallel CPU evaluation for the applications in Section V, based on the batch size used and function complexity.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Applications", "weight": 1.0} -->

We present several examples demonstrating how CusADi can be used for robotics. However, any application with repeated functional substructures at large scales (value iteration, fluid/weather simulation, image processing, finite element analysis, etc.) could leverage this framework for efficient GPU parallelization.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Applications", "weight": 1.0} -->

We consider two systems: the MIT Humanoid \[Saloutos2023_MITHumanoid\] (Section V-A, Section V-B) and a planar, thrust-limited quadcopter (Section V-C).

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-A MPC Parallelization for the MIT Humanoid", "weight": 1.0} -->

A limitation of the SIMD parallelization approach described in Section III is handling complex branching logic during function evaluation. The vectorization is only valid when every function instance has the same set of instructions that can be performed in lock step, and branching evaluation paths can break this synchronized parallelization. While simple ternary statements can be parallelized (e.g., min and max operators), functions with diverging evaluation paths are challenging to evaluate synchronously. Consequently, CusADi-parallelizable functions must have a finite set of synchronous instructions, limiting them to be closed-form and relatively free of branching logic.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-A MPC Parallelization for the MIT Humanoid", "weight": 1.0} -->

Unfortunately, the algorithms to solve OCPs typically involve conditional divergence at each solver iteration, such as checking for solution convergence, line search criteria, and/or constraint violations. However, prior work has shown that approximations of an OCP are typically "good enough" to achieve stable closed-loop performance for robotic systems. The accuracy and convergence criteria of the OCP can be relaxed significantly without sacrificing controller quality, as in \[Diehl2005_realtimeIteration, Grandia2023_perceptiveLocomotion, Numerow2024_RobustSuboptimalMPC, Khazoom2024_TailoredMPC\].

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-A MPC Parallelization for the MIT Humanoid", "weight": 1.0} -->

Consequently, we approximate the solution to an OCP with a strictly fixed number of operations. Suppose a single solver iteration can be expressed in closed-form as where $\mathbf{z}_{k} \in {\mathbb{R}}^{N}$ is the current solution iterate of an OCP and $h:{{\mathbb{R}}^{N}\rightarrow{\mathbb{R}}^{N}}$ is a single iteration of some arbitrary solver. Then we can express an approximate solution $\hat{\mathbf{z}}$ to the optimization by recursively applying $M$ times, so that $\hat{\mathbf{z}} = {H{(\mathbf{z}_{0})}}:={h^{M}{(\mathbf{z}_{0})}}$. This eliminates branching logic within the solver, allowing us to express $H$ as a CusADi expression. One advantage of this approach is that the accuracy of the solver can be tailored for computational demands as necessary.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-A MPC Parallelization for the MIT Humanoid", "weight": 1.0} -->

With this approximation, we seek to solve the OCP in Section II-C symbolically for parallelization. Using the previous solution as an initial guess, a single QP iteration is often sufficient to approximate the solution (a "real-time iteration", as in \[Diehl2005_realtimeIteration\]). This reduces to a QP problem.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-A MPC Parallelization for the MIT Humanoid", "weight": 1.0} -->

To solve the QP, we adopt a penalty-based method to approximate the original QP problem in by incorporating inequality constraints into the cost function, penalizing solution deviations from feasibility. The approximated QP problem can be represented as follows: where $\mu$ is a penalty parameter, and ${p{(\cdot)}}:{{\mathbb{R}}^{M_{ineq}}\rightarrow{\mathbb{R}}}$ is a penalty function, such as a quadratic function or an $l_{1}$ penalty function. It can be shown that for sufficiently large $\mu$, the solutions of the approximated problem also solve the original problem \[Boyd2004_ConvexOptimization\]. By iteratively increasing the penalty parameter to a sufficiently large value (e.g., ${\mu_{k + 1} = {\alpha\mu_{k}}},{\alpha > 0}$), the solution gradually converges to the original problem.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-A MPC Parallelization for the MIT Humanoid", "weight": 1.0} -->

The equality-constrained problem in (V-A) can be solved by applying the LDL^T^ factorization approach \[Boyd2004_ConvexOptimization\] to the KKT equations. Therefore, we chose the formulation in (V-A), as it allows us to obtain accurate equality-constrained solutions with minimal computational overhead.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-A MPC Parallelization for the MIT Humanoid", "weight": 1.0} -->

For the MIT Humanoid, we implement the single rigid-body model (SRBM) nonlinear MPC controller detailed in \[Hong_MPCSO3\] entirely in casadi, and demonstrate its subsequent CusADi parallelization across 4,096 environments in IsaacGym, as shown in Fig. 1. For the penalty function, we use ${p{(\mathbf{x})}} = {\sum_{i = 1}^{M_{ineq}}{({\max{(0,x_{i})}})}^{2}}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-A MPC Parallelization for the MIT Humanoid", "weight": 1.0} -->

There is a direct trade-off between the convergence accuracy of the approximated MPC and the evaluation time of the function. With too few, the controller fails to be stable in closed-loop simulation, but past a certain number of iterations, the marginal benefit of each solve diminishes rapidly while incurring significant computational cost, as visualized in Fig. 4. The fidelity of the controller can be tuned to accommodate the computational demands of the application, such as sampling high-quality rollouts offline or embedding MPC in RL training.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-A MPC Parallelization for the MIT Humanoid", "weight": 1.0} -->

Jenelten et al.\[Jenelten2024_DTC\] requires roughly 14 seconds per PPO iterations when trained with 4,096 environments at a 200 Hz simulation frequency, 50 Hz policy frequency, and 2.2 Hz MPC frequency. While we leave learning a policy alongside the parallelized MPC to future work, initial tests in IsaacGym showed an iteration time of roughly 1.24 seconds per PPO iteration with the same frequencies, corresponding to a speedup of roughly 11x. While the MPC controller in \[Jenelten2024_DTC\] is more complex than our SRBM MPC, leveraging the GPU and eliminating the overhead of data transfer significantly improves the efficiency of learning with optimization in the loop.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-B RL Training with Centroidal Momentum", "weight": 1.0} -->

We demonstrate how CusADi can act as a bridge to incorporate in model-based quantities relevant for legged locomotion (centroidal momentum \[Orin2013_centroidal\], center of pressure \[Sentis2009_COP\], the divergent component of motion \[Englsberger2015_DCM\], composite rigid-body inertia, etc.) to RL settings. While these could be computed directly in the RL environments, it can be challenging to efficiently implement the necessary algorithms across tensors of state data, especially if sparsity can be exploited. These quantities only need to be expressed symbolically for a single instance (made straightforward with the dynamics libraries mentioned in Section II-A) to be computed in parallel across any number of environments.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-B RL Training with Centroidal Momentum", "weight": 1.0} -->

Taking inspiration from \\textciteWensing2016_centroidal, we parallelize computing the centroidal momentum matrix (CMM) for the MIT Humanoid (using the casadi-compatible dynamics algorithms in spatial_v2) to augment RL training, as shown in Fig. 5. Typically, tracking some desired angular velocity for the base is rewarded in RL settings. For this simple example, we instead reward tracking a desired centroidal angular momentum. By doing so, we observe emergent arm swing during locomotion, corroborating the relationship between minimizing the CAM and arm motion from the original work, as well as \[Khazoom2022_armSwing\].

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-C Parallelized Rollouts", "weight": 1.0} -->

The system we consider is a planar quadcopter subject to thrust limits. We consider two scenarios to showcase the parallelization of CusADi. First, given a controller, from what initial states can the system be stabilized? What is the region of attraction of that controller? Second, given an initial and desired state, how is the optimal trajectory affected by the system and controller parameters? Can they be adjusted to meet design or state constraints for the system?

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-C Parallelized Rollouts", "weight": 1.0} -->

With CusADi, we parallelize a closed-loop simulation step of the quadcopter with a linear quadratic regulator (LQR) controller. If the LQR horizon $T$ is finite, the problem can be rewritten as an equality-constrained quadratic program, and its KKT system can be solved with symbolic LDL^T^ decomposition as in Section V-A. For the infinite-horizon case, the structured doubling algorithm from \\textciteWang2008_fastApproxMPC can be implemented to solve the discrete algebraic Riccati equation (DARE), which has quadratic convergence to the solution $S_{\infty}$. While the algorithm should be repeated until convergence, we can again fix the number of iterations to approximate the solution. For the drone, we found that 10-15 iterations of this algorithm was suitable.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-C Parallelized Rollouts", "weight": 1.0} -->

The symbolic LQR solution is used as the input for the drone dynamics, and integrated with the semi-implicit Euler scheme in casadi. In addition to the current state, we specify the thrust limits, inertial parameters, and LQR weights as additional parameters for the function. Overall, our casadi function computing the closed-loop dynamics with the LQR controller takes the form with quadcopter state $\mathbf{z} \in {\mathbb{R}}^{6}$ and parameters $\theta$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-C Parallelized Rollouts", "weight": 1.0} -->

With CusADi, we parallelize this closed-loop simulation step for the quadcopter and rollout 10,000 environments in parallel. For the first scenario, we fix the controller and initialize each environment with different angular and linear momenta with zero position and rotation offset, and determine which rollouts were stable. The resultant region of attraction for each thrust limit is visualized in Fig. 6.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-C Parallelized Rollouts", "weight": 1.0} -->

The MPC described in Section V-A could likewise be rolled out across large batches to estimate regions of stability in state space for the humanoid, a high-dimensional problem that would be extremely inefficient to compute without GPU parallelization.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-C Parallelized Rollouts", "weight": 1.0} -->

For the second scenario, the quadcopter is initialized from rest at some non-zero position, and the parameters of the system are varied to study their effects on the optimal trajectory, as shown in Fig. 7. The resultant rollouts directly visualize the effect of the parameters on closed-loop simulation, making them much easier to tune. A potential use case for CusADi is performing these kinds of sweeps online. Similar to \[Sacks2022_LearningMPPI\], Monte Carlo rollouts can be evaluated on the GPU to better estimate uncertain parameters of the system or adjust its trajectory in real time.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-C Parallelized Rollouts", "weight": 1.0} -->

While these low-dimensional examples do not require GPU scaling for evaluation, they serve to illustrate how CusADi can be used to tackle high-dimensional problems that require substantial data.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we extend the symbolic framework of casadi so that arbitrary closed-form expressions can be parallelized on the GPU with CUDA and formulate a closed-form approximation to the OCP to evaluate MPC in parallel at a large-scale.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusion", "weight": 1.5} -->

As a tool, CusADi can be extended in several ways. Parallelism within individual expressions could also be exploited, especially for larger problems as studied in \[Plancher2019_DDPGPU\]. Results from graph theory could be used to identify parallelization opportunities from casadi expression graphs. However, this would have to be balanced against the overhead of starting and synchronizing additional threads.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion", "weight": 1.5} -->

For future work, the parallelization offered by CusADi opens up several promising directions. To improve the locomotion capabilities of the MIT Humanoid, we plan to learn a residual policy alongside the parallelized MPC with reinforcement learning \[Silver2018_ResidualPolicy\]. Another potential direction is to learn the value function for MPC with parallelized rollouts. The function could then be used to bootstrap value estimates in RL pipelines, similar to \[Grandesso2023_CACTO\], or as a terminal cost for more complex MPC controllers.
