<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

CuClarabel: GPU Acceleration for a Conic Optimization Solver

Topics include Convex optimization, Semidefinite programming, Accuracy, Parallel computing, Optimization, CuClarabel.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present the GPU implementation of the general-purpose interior-point solver Clarabel for convex optimization problems with conic constraints. We introduce a mixed parallel computing strategy that processes linear constraints first, then handles other conic constraints in parallel. The GPU solver currently supports linear equality and inequality constraints, second-order cones, exponential cones, power cones and positive semidefinite cones of the same dimensionality. We demonstrate that integrating a mixed parallel computing strategy with GPU-based direct linear system solvers enhances the performance of GPU-based conic solvers, surpassing their CPU-based counterparts across a wide range of conic optimization problems. We also show that employing mixed-precision linear system solvers can potentially achieve additional acceleration without compromising solution accuracy.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

with respect to $x,s$ and with parameters $A \in \text{R}^{m \times n}$, $b \in \text{R}^{m}$, $q \in \text{R}^{n}$ and $P \in {SS}_{+}^{n}$ and variables ${x \in \text{R}^{n}},{s \in \text{R}^{m}}$. For the rest of the paper, ${SS}_{+}^{n}$ represents the cone of positive semi-definite matrices. The cone $\mathcal{K}$ is a closed convex cone. The formulation ($\mathcal{P}$) is very general and can model most conic convex optimization problems in practice. Examples include the optimal power flow problem in power systems, model predictive control in control, limit analysis of engineering structures in mechanics, support vector machines and lasso problems in machine learning, statistics, and signal processing, and portfolio optimization in finance.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Linear equality (zero cones) and inequality (nonnegative cones), second-order cone, and semidefinite cone constraints have been long supported in standard conic optimization solvers, and support for exponential and power cone constraints was recently included in several state-of-the-art conic optimization solvers. The combination of these cones can represent many more elaborate convex constraints through the lens of disciplined convex programming.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

with respect to $x,z$ and where $\mathcal{K}^{\ast}$ is the dual cone of $\mathcal{K}$. Solving $\mathcal{P}$ and $\mathcal{D}$ is equivalent to solving the Karush-Kuhn-Tucker (KKT) conditions when strong duality holds. On the other hand, the set of strongly primal infeasibility certificates for ($\mathcal{P}$) is

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

and the set of strongly dual infeasibility certificates is

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

with respect to $x,s,z,\tau,\kappa$. It is well-known that when $P = 0$, ($\mathcal{H}$) is the *homogenous self-dual embedding* of ($\mathcal{P}$), and the extension for $P \neq 0$ can be regarded as a *homogeneous embedding* for linear complementarity problems. Precisely, in our case ($\mathcal{H}$) is homogeneous but not self-dual.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The optimal solution $\tau^{\star},\kappa^{\star}$ satisfy the complementarity slackness condition, *i.e.*, at most one of $\tau^{\star},\kappa^{\star}$ is nonzero. The pathological case $\tau^{\star} = \kappa^{\star} = 0$ has been discussed.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The *interior-point method* is a popular choice for solving ($\mathcal{H}$). However, it usually requires to factorize linear systems that are increasingly ill-conditioned. The time complexity of matrix factorization scales with respect to the fill-in that is closely related to nonzeros of the matrix and permutation strategies during factorization. It is thus time-consuming to solve large-scale conic optimization problems with interior-point methods.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Our contribution", "weight": 1.0} -->

We contribute a GPU-accelerated implementation of the general-purpose interior-point solver Clarabel, in Julia. This implementation supports cases where $\mathcal{K}$ is a product of *atomic* cones: zero cones, nonnegative cones, second-order cones, exponential cones, power cones and positive semidefinite cones. We propose a *mixed parallel computing strategy* that parallelizes computing for each type of cone, integrates the cuDSS library for linear system solving, and supports *mixed-precision* linear system solves for moderate speed improvements. Furthermore, we evaluate our solver against others across a variety of conic optimization problems. Our implementation of CuClarabel is open-sourced on GitHub^11^1 and can be easily accessed through CVXPY.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Interior-point methods and solver development", "weight": 1.0} -->

The interior-point method was first discovered by Dikin, and became more mainstream after the conception of Karmarkar's method, a polynomial-time algorithm for linear programming, and Renegar's path following method. Interior-point methods are known for their ability to solve conic optimization problems to high precision, and is chosen as the default algorithm for many conic optimization solvers. Common variations of the interior-point method include potential reduction methods and path-following methods.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Interior-point methods and solver development", "weight": 1.0} -->

Interior-point methods employ a Newton-like strategy to compute a search direction at every iteration. Unfortunately, the matrix factorization required to compute this direction which scales with the dimension of an optimization problem, rendering very large problems difficult to solve. Developing efficient interior-point methods on exotic cones directly is a promising research direction to alleviate this computational burden. Using exotic cones, we can represent equivalent problems with significantly fewer variables and exploit sparse structure within these exotic cones for efficient implementation of interior-point methods. However, operations within an exotic cone can hardly be parallelized, while parallelism across heterogeneous cones of different dimensionalities will introduce significant synchronization delay.

<!-- chunk {"id": "body-0013", "role": "body", "section": "GPU acceleration in optimization algorithms", "weight": 1.0} -->

GPUs are playing an increasingly significant role in scientific computing. In optimization, GPUs are used to run solvers based on first-order methods. For example, CuPDLP is based on the popular PDHG algorithm, which requires only matrix multiplication and addition without the use of direct methods (*i.e.*, it is *factorization-free*). Solvers that require the solution to linear systems, like SCS and CuOSQP, have relied on indirect iterative methods---such as the conjugate gradient (CG), the minimal residual (MINRES), and the generalized minimum residual (GMRES) methods---to solve these systems on GPUs. However, the linear systems solved in first-order methods are generally much better conditioned than those encountered in interior-point methods, where the linear systems become increasingly ill-conditioned as the iterations progress. As an interior-point method approaches higher precision, the number of iterations for each inner indirect linear solves increases significantly, which will eventually offset benefits of GPU parallelism and make GPU-based interior-point methods less preferable compared to CPU-based solvers with direct methods in overall computational time.

<!-- chunk {"id": "body-0014", "role": "body", "section": "GPU acceleration in optimization algorithms", "weight": 1.0} -->

Recently, NVIDIA released the cuDSS package, which provides fast direct methods on GPUs for sparse linear systems. Previous work has integrated cuDSS in a nonlinear optimization solver, MADNLP, resulting in significant speed-up on large-scale problems compared to its CPU-based counterpart.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Mixed-precision methods", "weight": 1.0} -->

Mixed-precision, or multiprecision, methods have become progressively more popular due to their synergies with modern GPU architectures. For example, in lower-precision configuration one enjoys significant speedup in algorithms, as modern architectures have 32-bit implementations that are around twice as fast as their 64-bit counterparts. Mixed precision methods aim to capitalize on the computational benefits of performing expensive operations in lower precision, while maintaining (or reducing the negative impact to) the superior numerical accuracy from higher precision. Classically, mixed-precision methods for direct (linear system solving) methods involve factorizing a matrix in lower precision, and then applying iterative refinement. In this approach, only the more expensive steps, such as the matrix factorizations and backsolves, are done in lower precision. Mixed-precision methods are used throughout scientific computing, with applications including BLAS operations, different linear system solvers such as Krylov methods (CG, GMRES), solving partial differential equations, and training deep neural networks.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Paper outline", "weight": 1.0} -->

In §, we review supported cones and discuss the interior point method used by Clarabel for solving conic optimization problems. In §, we outline how to implement parallel computation for cone operations and solve linear systems within our GPU solver. § details our numerical experiments. We detail the scaling matrices for each cone in §A.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Backgrounds", "weight": 1.0} -->

We first review supported cones in CuClarabel with the corresponding barrier functions, along with their dual cones. We then briefly sketch the main operations used by the Clarabel solver to compute a solution to ($\mathcal{P}$).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Supported cones", "weight": 1.0} -->

The *second-order cone* $\mathcal{K}_{\text{soc~}}^{n}$ (also called the *quadratic* or *Lorentz cone*), defined as

<!-- chunk {"id": "body-0019", "role": "body", "section": "Supported cones", "weight": 1.0} -->

The *positive semidefinite cone* $\mathcal{K}_{psd}^{n}$ is defined as

<!-- chunk {"id": "body-0020", "role": "body", "section": "Supported cones", "weight": 1.0} -->

where ${\mathbb{S}}^{n}$ denotes the space of $n \times n$ symmetric matrices, and $X \succeq 0$ indicates that $X$ is positive semidefinite. The positive semidefinite cone is self-dual, *i.e.*, $\mathcal{K}_{psd}^{n} = \left( \mathcal{K}_{psd}^{n} \right)^{\ast}$.^22^2In the current solver implementation, all positive semidefinite (PSD) cones are restricted to have dimension at most $32$, and all PSD cones within a given problem must share the same dimension.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Supported cones", "weight": 1.0} -->

The *exponential cone*, a $3$-dimensional cone defined as

<!-- chunk {"id": "body-0022", "role": "body", "section": "Supported cones", "weight": 1.0} -->

with its dual cone given by

<!-- chunk {"id": "body-0023", "role": "body", "section": "Supported cones", "weight": 1.0} -->

The $3$-dimensional *power cone* with exponent $\alpha \in {}$, defined as

<!-- chunk {"id": "body-0024", "role": "body", "section": "Supported cones", "weight": 1.0} -->

with its dual cone given by

<!-- chunk {"id": "body-0025", "role": "body", "section": "Interior point method", "weight": 1.0} -->

Solving the problem ($\mathcal{H}$) amounts to finding a root of the following nonlinear equations

<!-- chunk {"id": "body-0026", "role": "body", "section": "Interior point method", "weight": 1.0} -->

where $\mathcal{F}:={\text{R}^{n} \times \mathcal{K}^{\ast} \times \mathcal{K} \times \text{R}_{+} \times \text{R}_{+}}$ defines the region of cone constraints. Besides the zero cone that is a linear constraint, other supported conic constraints are smoothed by nonlinear equations in pairs within an interior-point method,

<!-- chunk {"id": "body-0027", "role": "body", "section": "Interior point method", "weight": 1.0} -->

where $\mu$ is the smoothing parameter and $f{( \cdot )}$ is the logarithmically homogeneous self-concordant barrier (LHSCB) function for cone $\mathcal{K}^{\ast}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Interior point method", "weight": 1.0} -->

The trajectory (also called the central path)

<!-- chunk {"id": "body-0029", "role": "body", "section": "Interior point method", "weight": 1.0} -->

where $v = {(x,z,s,\tau,\kappa)}$, characterizes the solution of in the right limit $\mu\rightarrow 0^{+}$, given an initial point $v^{0}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Update residuals and check the termination condition", "weight": 1.0} -->

We update several key metrics at the start of each iteration. Defining the normalized variables ${\overline{x} = {x/\tau}},{{\overline{s} = {s/\tau}},{\overline{z} = {z/\tau}}}$, the primal and dual residuals are then

<!-- chunk {"id": "body-0031", "role": "body", "section": "Update residuals and check the termination condition", "weight": 1.0} -->

and complementarity slackness $\mu = \frac{{s^{T}z} + {\kappa\tau}}{\nu + 1}$, where $\nu$ is the degree of cone $\mathcal{K}$. The solver returns an approximate optimal point if

<!-- chunk {"id": "body-0032", "role": "body", "section": "Update residuals and check the termination condition", "weight": 1.0} -->

Otherwise, it returns a certificate of primal infeasibility if

<!-- chunk {"id": "body-0033", "role": "body", "section": "Update residuals and check the termination condition", "weight": 1.0} -->

Note that $\epsilon_{\text{feas}},\epsilon_{\text{inf}}$ are predefined parameters within the Clarabel solver.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Find search directions", "weight": 1.0} -->

We then compute Newton-like search directions using a linearization of the central path. In other words, we solve the following linear system given some right-hand side residual $d = {(d_{x},d_{z},d_{\tau},}$ $d_{s},d_{\kappa})$,

<!-- chunk {"id": "body-0035", "role": "body", "section": "Find search directions", "weight": 1.0} -->

where $\xi = {x\tau^{- 1}}$, and $H$ is the same positive-definite scaling matrix as in the CPU version of Clarabel, also described in §A. We have shown that solving reduces to solve the next linear system with two different right-hand sides,

<!-- chunk {"id": "body-0036", "role": "body", "section": "Find search directions", "weight": 1.0} -->

Since both $P,H$ are positive semidefinite, adding a positive regularization to them makes $K$ symmetric quasi-definite and thus strongly factorizable via the $LDL^{T}$ decomposition. After solving, we recover the search direction $\Delta = {({\Deltax},{\Deltaz},{\Delta\tau},{\Deltas},{\Delta\kappa})}$ using

<!-- chunk {"id": "body-0037", "role": "body", "section": "Find search directions", "weight": 1.0} -->

In an interior-point method with a predictor-corrector scheme, we need to solve with two different values for $d$. The first is for the affine step (predictor) with

<!-- chunk {"id": "body-0038", "role": "body", "section": "Find search directions", "weight": 1.0} -->

in the combined step (predictor+corrector), where $\lambda = {W^{- T}s} = {Wz}$ and $\mathbf{e}$ is the idempotent for a symmetric cone with the product operator '$\circ$' and its inverse operator '$\backslash$'. Here $\eta$ denotes a higher-order correction term, which is a heuristic technique that can significantly accelerate the convergence of interior-point methods. We set it to the Mehrotra correction

<!-- chunk {"id": "body-0039", "role": "body", "section": "Find search directions", "weight": 1.0} -->

for nonsymmetric cones. The centering parameter $\sigma$ controls the rate at which both the residual $G{(x,z,s,\tau,\kappa)}$ and the complementarity measure $\mu$ decrease. It is determined heuristically based on the value of the affine step size $\alpha_{a}$, defined as the maximal step size ensuring that ${v + {\alpha_{a}\Delta_{a}}} \in \mathcal{F}$. Computing $\alpha_{a}$ is non-trivial in the presence of exponential and power cones. As a practical alternative, we perform a backtracking line search with a shrinking ratio of $0.8$ to determine a feasible $\alpha_{a}$ for power and exponential cones.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Update iterates", "weight": 1.0} -->

At the end of each iteration $k$, we move the current iterate $v$ along the combined direction $\Delta_{c}:={(x,z,s,\tau,\kappa)}$ and obtain the new iterate $v + {\alpha_{c}\Delta_{c}}$. As discussed, the combined step size $\alpha_{c}$ should satisfy ${v + {\alpha_{c}\Delta_{c}}} \in \mathcal{F}$. Furthermore, we must ensure that the new iterate $v + {\alpha_{c}\Delta_{c}}$ stays in the neighborhood $\mathcal{N}{(\beta)}$ of the central path,

<!-- chunk {"id": "body-0041", "role": "body", "section": "A primer on GPU programming", "weight": 1.0} -->

Originally developed for computationally demanding gaming applications, graphics processing units (GPUs) are *massively parallel*, *multithreaded*, *manycore processors*, with massive computational power and memory bandwidth. As a result, GPUs are used throughout scientific computing. In this section, we outline some core properties of GPU computing devices to highlight why a GPU implementation is a natural extension to Clarabel. We then discuss our specific implementation details.

<!-- chunk {"id": "body-0042", "role": "body", "section": "A primer on GPU programming", "weight": 1.0} -->

Due to their natural parallelism, GPUs differ dramatically from CPUs in the way their transistors are configured. GPUs have a smaller number of caches (blocks where memory access is fast) and instruction processing blocks, and far more, albeit simpler, computational blocks (*i.e.*, arithmetic logic and floating point units). This suggests that CPUs utilize their larger caches to minimize instruction and memory latency within each thread, while GPUs switch between their significantly larger number of threads to hide said latency.

<!-- chunk {"id": "body-0043", "role": "body", "section": "A primer on GPU programming", "weight": 1.0} -->

GPUs use a *single instruction, many threads* (SIMT) approach. In practice, the GPU receives a stream of instructions -- each instruction is sent to groups of GPU cores (also known as a *warp*) and acts on multiple data in parallel. Each group of GPU cores, as a result, has *single instruction, many data* (SIMD) structure. This contrasts the traditional CPU vector lane approach of *single instruction, single data*. Note that modern CPUs also support SIMD, but at a much smaller scale than GPUs, as implied by the transistor layout. Furthermore, the SIMD structure requires data parallelism for parallel execution on a GPU.

<!-- chunk {"id": "body-0044", "role": "body", "section": "GPU implementation for interior point method", "weight": 1.0} -->

We detail our GPU implementation of the primal-dual interior point method in Algorithm, which is divided into two phases: setup and solve. The setup phase involves data equilibration and solver initialization, while the solve phase implements the classical primal-dual interior point method. Synchronization is required at the end of each step in Algorithm.

<!-- chunk {"id": "body-0045", "role": "body", "section": "GPU implementation for interior point method", "weight": 1.0} -->

0: Parameter inputs P, A, q, b and cone information 𝒦. //Setup phase
2: Initialize solver structure s, including matrix K and cuDSS solver.//Solve phase
3: while termination check or is not satisfied do
4: Update the scaling matrix H as in Appendix A.
5: Factorize the matrix K.
6: Compute the right-hand residual d for the affine step and solve to obtain Δa via.
7: Compute the affine step αa satisfying v + αa Δa ∈ ℱ.
8: Compute the centering parameter σ = (1−αa)3.
9: Compute the right-hand residual d for the combined step and solve to obtain Δc via.
10: Compute the combined step αc satisfying v + αc Δc ∈ ℱ with the neighborhood check.
11: Update the variable v ← v + 0.99 αc Δc.
12: Update residuals and objective values.
Algorithm 1 Primal-dual interior-point method

<!-- chunk {"id": "body-0046", "role": "body", "section": "GPU implementation for interior point method", "weight": 1.0} -->

The matrix factorization (step 5) and the back-solve (steps 6 and 9) are the most time-consuming parts in each iteration of an interior point method, and can be computed using the cuDSS package. Variable and information update (steps 11 and 12) contain matrix addition and multiplication operations that have already been supported in CUDA. Steps 4, 6, 7, 9, and 10 include cone operations that should be tailored for each cone, but we can abstract them into the same framework for parallelism. We will detail how to parallelize each of these steps under a unified framework in the next subsection.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Mixed parallel computing strategy", "weight": 1.0} -->

The cone operations related to steps 4, 6, 7, 9, and 10 above require only information local to each constituent cone, and hence can be executed concurrently with respect to individual cones. We propose the *mixed parallel computing strategy* for a cone operation across different types of cones. Each family of cones is handled in parallel, and families of cones can be addressed by separate streams.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Mixed parallel computing strategy", "weight": 1.0} -->

As stated earlier, the cone operations related to zero cones and nonnegative cones are simply vector additions and multiplications, which have already been parallelized in CUDA. In our implementation we aggregate all zero cones into a single zero cone in our preprocessing step. The same holds for nonnegative cones. For the remaining cones, we parallelize within each *family* of cones (*i.e.*, second-order cone, exponential cone, etc.). For each family of cones, we allocate a thread to each cone belonging to that family, and execute in parallel. This adheres to the SIMD computing paradigm, as each type of cone has its own set of instructions for updating its scaling matrix.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Mixed parallel computing strategy", "weight": 1.0} -->

We employ our mixed parallel computing strategy in step 4, the scaling matrix update. Recall that the conic constraint $\mathcal{K}$ can be decomposed as a Cartesian product of $p$ constituent atomic cones $\mathcal{K}_{1} \times \cdots \times \mathcal{K}_{p}$ that are ordered by cone types. We assume $\mathcal{K}_{1}$ is a zero cone, $\mathcal{K}_{2}$ is a nonnegative cone, $\mathcal{K}_{3}$ to $\mathcal{K}_{i}$ are second-order cones, $\mathcal{K}_{i + 1}$ to $\mathcal{K}_{j}$ are exponential cones, $\mathcal{K}_{j + 1}$ to $\mathcal{K}_{l}$ are power cones and $\mathcal{K}_{l + 1}$ to $\mathcal{K}_{p}$ are positive semidefinite cones.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Mixed parallel computing strategy", "weight": 1.0} -->

Due to our decomposition into constituent atomic cones, $H$ is a block-diagonal matrix,

<!-- chunk {"id": "body-0051", "role": "body", "section": "Mixed parallel computing strategy", "weight": 1.0} -->

where $H_{1}$ and $H_{2}$ are diagonal matrices and each block ${H_{t},t} \geq 3$ is the scaling matrix corresponding to cone $\mathcal{K}_{t}$ of small dimensionality.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Mixed parallel computing strategy", "weight": 1.0} -->

0: Current iterate vk, streams s ts o c, s te x p, s tp o w, s ts d p.
2: Update Hzerok // Zero cone (t = 1)
3: Update Hnnk // Nonnegative cone (t = 2)
6: Hsock= _kernel_soc_update_H&lt;s ts o c&gt; // t = 3 to i
9: Hexpk= _kernel_exp_update_H&lt;s te x p&gt; // t = i + 1 to j
12: Hpowk= _kernel_pow_update_H&lt;s tp o w&gt; // t = j + 1 to l
14: // Positive semidefinite cones
15: Hsdpk= _kernel_sdp_update_H&lt;s ts d p&gt; // t = l + 1 to p
17: // Synchronize scaling update
20: return Hk // Output the scaling matrix Hk
Algorithm 2 Algorithmic sketch for the scaling matrix Hk update in Algorithm 1

<!-- chunk {"id": "body-0053", "role": "body", "section": "Mixed parallel computing strategy", "weight": 1.0} -->

Algorithm illustrates the update of scaling matrix $H^{k}$ in function \_update_H($v^{k}$). For the update of $H$ at iteration $k$, we first set diagonal terms of the scaling matrix $H_{1}^{k}$ for the zero cone to all $0$s, and then update the diagonals of the scaling matrix $H_{2}^{k}$ for the nonnegative cone by element-wise vector division, as in the Nesterov-Todd (NT) scaling. These computations are already parallelized by CUDA. For conic constraints other than the zero cone and the nonnegative cone, the corresponding parts in the scaling matrix $H$ are no longer diagonal, but we observe $H_{t}$ only requires local information within each constituent cone, and thus we can solve for each $H_{t}$ concurrently, independent to the other cones.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Mixed parallel computing strategy", "weight": 1.0} -->

We implement kernel functions \_kernel_soc_update_H, \_kernel_exp_update_H, \_kernel_pow_update_H and \_kernel_sdp_update_H for second-order cones, exponential cones, power cones and positive semidefinite cones respectively. Details regarding the update functions for each type of cone can be found in §A. Each kernel function will process one cone per thread, and updating scaling matrices of the same class of cones is executed in parallel. Kernel functions for different cone classes are launched independently in separate streams. Synchronization is required at the end of the scaling matrix update.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Mixed parallel computing strategy", "weight": 1.0} -->

Since the mixed parallel computing strategy is independent of choices of optimization algorithms, it is also applicable for GPU implementations for cone operations in first-order operator-splitting conic solvers, like SCS and COSMO.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Mixed parallel computing strategy", "weight": 1.0} -->

Note that the SIMD GPU computing structure naturally favors *balanced workloads*, *i.e.*, the workloads in each thread should be similar so that the synchronization will not take too much time. The exponential and power cones are 3-dimensional nonsymmetric cones that all cone operations have balanced workload among the same class of cones, thus we can parallelize the computation for each cone. On the other hand, the second-order cones may vary in dimensionality, which may not mesh well with the SIMD computing paradigm. In most use cases for large-scale second-order cone problems, *e.g.*, optimal power flow problems and finite-element problems, the second-order cones are of small (less than 5) dimensionality; thus the effect of this workload imbalance is negligible. Regardless, we support second-order cones of all sizes. In the next section, we outline how to process second-order cones of high dimensionality.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Dynamic parallelism for second-order cones", "weight": 1.0} -->

Due to the definition of the barrier function over a second-order cone ${(t,x)} \in \mathcal{K}_{q}^{n}$, the computation of residuals involving $t^{2} - {\| x\|}^{2}$ requires substantial reduction operations within each cone. This introduces an additional level of parallelism, particularly relevant when the dimension of a second-order cone reaches thousands or more, as seen in applications like multistage portfolio optimization.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Dynamic parallelism for second-order cones", "weight": 1.0} -->

In such high-dimensional cases, processing second-order cones in a purely thread-wise fashion above becomes inefficient, as the residual computation becomes effectively single-threaded. A straightforward workaround is to use the dot product operations provided by cuBLAS for computing residuals. However, this approach processes each high-dimensional cone sequentially and fails to exploit cone-level parallelism when multiple second-order cones are present. To address this, we implement custom reduction operations and leverage *dynamic parallelism* in CUDA, which enables additional cone-level parallelism and better utilization of GPU resources.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Dynamic parallelism for second-order cones", "weight": 1.0} -->

We then launch $q$ child kernel functions, \_child_kernel_soc_residual ($x_{i},r$), for each thread $i$ ($1 \leq i \leq q$) within the parent kernel function, processing the residual of cone $i$. The $2$-norm of $u_{i}$ can be realized by the standard parallel reduction utilizing shared memory efficiently, see Algorithm. Finally, we obtain the residual for each cone $i$ and store it back to $r$ in the child function.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Dynamic parallelism for second-order cones", "weight": 1.0} -->

0: x = [x1; x2; …; xq] and r ∈ Rq, where xi = [ti; ui] ∈ Rni + 1
3: function _parent_kernel_soc_residual(x, r)
4: i← (blockIdx.x -1)* blockDim.x + threadIdx.x //Julia is 1-indexed
6: xi← extract cone block i from x
8: //compute residual of each cone i
9: _child_kernel_soc_residual(xi, r)
14: function _child_kernel_soc_residual(xi, r)
15: ti ← xi // Julia: 1-based indexing
Algorithm 3 Dynamic parallelism for the residual computation of q second-order cones

<!-- chunk {"id": "body-0061", "role": "body", "section": "Batched support for positive semidefinite cones", "weight": 1.0} -->

The positive semidefinite (PSD) cone is a matrix cone that can vary in dimensionality. Computing scaling matrices and step sizes involves several matrix factorizations, such as Cholesky factorization, singular value decomposition and eigenvalue decomposition. In CuClarabel, we address this by using batched matrix factorizations provided by the cuSOLVER library. Hence, we only support a restricted class of SDPs in which all PSD cones have the same dimensionality that is less than or equal to $32$. This includes examples from finite element analysis problems, where each SDP constraint encodes localized, element-wise or point-wise conditions ---such as stress admissibility or yield criteria---that can be uniformly applied across the mesh.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Data structures", "weight": 1.0} -->

Since data parallelism is required for parallel execution on GPUs, we manage data for each cone as a structure of arrays (SoA) in our GPU implementation, in contrast to the existing CPU counterpart which uses an array of structures (AoS). In other words, instead of creating structs for ${{\mathcal{K}_{i},i} = 1},{\ldots,p}$ and storing pointers to each struct in an array, we concatenate the same type of local variable from different cones into a global variable and then store it in a global struct for $\mathcal{K}$, which is illustrated in Figure.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Data structures", "weight": 1.0} -->

In addition, indexing cones in order in the setup phase can simplify the implementation of mixed parallel computing strategy. We reorder the input cones such that memory is coalescing for the same class of cones, which can accelerate computation on GPUs. Matrices are stored in the compressed sparse row (CSR) format. Instead of storing only the triangular part of a square matrix as in the CPU-based Clarabel, we store the full matrix for more efficient multiplication on the GPU.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Solving linear systems", "weight": 1.0} -->

Most of the computation time for our interior point method is spent in factorizing the matrix $K$ and in the three backsolve operations. Our GPU implementation also leverages the power of the newly released sparse linear system solver cuDSS for the $LDL^{T}$ factorization and backsolve operations. We implement a self-contained iterative refinement originated to increase the numerical stability of the backsolve operation.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Solving linear systems", "weight": 1.0} -->

Currently, a GPU has more computing cores for than and hence better performance for parallel algorithms. Also, requires less memory and takes less time for the same computation than. However, lowering the precision will introduce numerical instability for solving linear systems. Thus, we employ a *mixed precision* solve in our matrix solves.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Solving linear systems", "weight": 1.0} -->

Solve for the residual at step $i$: $r_{i} = {b - {Kx_{i - 1}}}$, where $x_{i - 1}$ is our guess for iteration $i - 1$. (Full precision)

<!-- chunk {"id": "body-0067", "role": "body", "section": "Solving linear systems", "weight": 1.0} -->

Solve the linear system under a regularization parameter ${{({K + {\deltaI}})}\Delta_{i}} = r_{i}$. (Lower precision)

<!-- chunk {"id": "body-0068", "role": "body", "section": "Solving linear systems", "weight": 1.0} -->

In all our matrix solves, given matrix $K$ and right-hand side $b$, we factorize the lower precision copy of $K$, and then solve the linear system in this lower precision. To enhance numerical stability during matrix factorization, a regularization term $\deltaI$ with

<!-- chunk {"id": "body-0069", "role": "body", "section": "Solving linear systems", "weight": 1.0} -->

is added to $K$, where $\delta_{s}$ is a static regularization and $\delta_{d}{\max_{i}{|D_{ii}|}}$ provides dynamic scaling based on the magnitude of the diagonal entries of $D$. To offset the regularization effect and rounding errors from the lower precision in backsolves, we solve in full precision for the other steps, *i.e.*, we compute the residual $r_{i}$ and save the update $\{ x_{i}\}$ in full precision. When we change the factorization data type from to, it reduces down to the standard iterative refinement as employed in standard conic optimization solvers.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Solving linear systems", "weight": 1.0} -->

We apply iterative refinement until either we reach a pre-specified number of max steps $T_{\max}$ for iterative refinement, or the $\ell_{\infty}$ norm of $b - {Kx_{i}}$ reaches a certain threshold, specifically $\left\| {b - {Kx_{i}}} \right\|_{\infty} \leq {t_{\text{abs}} + {t_{\text{rel}}\left\| b \right\|_{\infty}}}$. We set both $t_{\text{abs}}$ (absolute tolerance) and $t_{\text{rel}}$ (relative tolerance) to $10^{- 12}$, and the maximum number of steps $T_{\max} = 10$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Solving linear systems", "weight": 1.0} -->

We set $\delta_{s}$ to the square root of machine precision, *i.e.*, $\sqrt{\epsilon} \approx {3.45e^{- 4}}$, for mixed precision and $\delta_{s} = {1e^{- 8}}$ for full precision, and we set $\delta_{d}$ to the square of machine precision, *i.e.*, $\epsilon^{2}$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Solving linear systems", "weight": 1.0} -->

Although the mixed precision for the iterative refinement can improve the numerical stability for solving linear system in lower precision, it is to be expected that the mixed precision may take longer time to converge or fail in cases where the matrix $K$ is extremely ill-conditioned. Caution is required when using mixed precision for numerically hard problems, *e.g.*, conic programs with exponential cones. Hence, we provide the mixed precision as an optional choice and use by default.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

We have benchmarked our Julia GPU implementation of the Clarabel solver, denoted as *ClarabelGPU*, against the state-of-the-art commercial interior-point solvers MOSEK and Gurobi. We also include our Rust CPU implementation of Clarabel solver with the 3rd-party multithreaded supernodal LDL factorization method in the *faer-rs* package, denoted as *ClarabelRs*. Note that MOSEK and Gurobi already utilize multithreaded linear system solvers. We include benchmark results for several classes of problems including quadratic programming (QP), second-order cone programming (SOCP) and exponential cone programming. All benchmarks are performed using the default settings for each solver, with pre-solve disabled where applicable to ensure equivalent problem-solving conditions. No additional iteration limits are imposed beyond each solver's internal defaults. We set $\epsilon_{\text{feas}} = {1e^{- 6}}$ for all solvers in termination check.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

All experiments were carried out on a workstation with Intel(R) Xeon(R) w9-3475X CPU @ 4.8 GHz with 256 GB RAM and NVIDIA GeForce RTX 4090 24GB GPU. All benchmarks tests are scripted in Julia and access solver interfaces via JuMP. We use Rust compiler version 1.76.0 and Julia version 1.10.2. Before recording benchmark tests, we run a few example solves; this offsets the just-in-time (JIT) precompilation overhead in Julia.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Benchmarking metrics", "weight": 1.0} -->

We choose the same benchmarking tests as used in the Clarabel solver, and compare our results using metrics that are commonly used when comparing computational time across different solvers. For a set of $N$ test problems, we define the *shifted geometric mean* $g_{s}$ as

<!-- chunk {"id": "body-0076", "role": "body", "section": "Benchmarking metrics", "weight": 1.0} -->

where $t_{p,s}$ is the time in seconds for solver $s$ to solve problem $p$, and $k = 1$ is the shift. The normalized shifted geometric mean is then defined as

<!-- chunk {"id": "body-0077", "role": "body", "section": "Benchmarking metrics", "weight": 1.0} -->

Note that the solver with the lowest shifted geometric mean solve time has a normalized score of 1. We assign a solve time $t_{p,s}$ equal to the maximum allowable solve time if solver $s$ fails to solve the problem $p$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Benchmarking metrics", "weight": 1.0} -->

The *relative performance ratio* for a solver $s$ and a problem $p$ is defined as

<!-- chunk {"id": "body-0079", "role": "body", "section": "Benchmarking metrics", "weight": 1.0} -->

The *relative performance profile* denotes the fraction of problems solved by solver $s$ within a factor $\tau$ of the solve time of the best solver, which is defined as $f_{s}^{r}:{\text{R}_{+}\mapsto{\lbrack 0,1\rbrack}}$

<!-- chunk {"id": "body-0080", "role": "body", "section": "Benchmarking metrics", "weight": 1.0} -->

where ${\mathcal{I}_{\leq \tau}{(u)}} = 1$ if $\tau \leq u$ and ${\mathcal{I}_{\leq \tau}{(u)}} = 0$ otherwise. For $\tau = 1$, $f_{s}^{r}{}$ denotes the ratio of problems where the solver $s$ performs the best, and $\sum_{s}{f_{s}^{r}{}}$ should be equal to 1 if every problem is solvable for at least one solver. We also compute the *absolute performance profile* $f_{s}^{a}:{\text{R}_{+}\mapsto{\lbrack 0,1\rbrack}}$, which denotes the fraction of problems solved by solver $s$ within $\tau$ seconds and is defined as

<!-- chunk {"id": "body-0081", "role": "body", "section": "Benchmarking metrics", "weight": 1.0} -->

Our numerical experiments highlight the performance gains achieved by the GPU implementation of Clarabel on a diverse set of conic optimization problems. We record *total time* by default, the sum of the *setup time*, including data equilibration and solver initialization, and the *solve time*, which is the running time for the algorithm underlying a solver.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Quadratic programming", "weight": 1.0} -->

We first present benchmark results for QPs. Note that in this setting, the set $\mathcal{K}$ in ($\mathcal{P}$) is restricted to the composition of zero cones, *i.e.*, linear equality constraints, and nonnegative cones, *i.e.*, linear inequality constraints. We consider two classes of problems, the portfolio optimization problem and the Huber fitting problem.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Quadratic programming", "weight": 1.0} -->

Portfolio optimization, a problem arising in quantitative finance, aims to allocate assets in a manner that maximizes expected return while keeping risk under control. We can formulate it as

<!-- chunk {"id": "body-0084", "role": "body", "section": "Quadratic programming", "weight": 1.0} -->

where $x \in \text{R}^{n}$ (the variable) represents the ratio of allocated assets, $\mu \in \text{R}^{n}$ is the vector of expected returns, $\gamma > 0$ is the risk-aversion parameter, and $\Sigma \in \mathbf{S}_{+}^{n}$ the risk covariance matrix which is of the form $\Sigma = {{FF^{T}} + D}$ with $F \in \text{R}^{p \times n}$ and $D \in \text{R}^{p \times p}$ diagonal. We set the rank $p$ to the integer closest to $0.1n$, and vary $n$ from $5000$ to $25000$.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Quadratic programming", "weight": 1.0} -->

Huber fitting is a version of robust least squares. For a given matrix $A \in \text{R}^{m \times n}$ and vector $b \in \text{R}^{m}$, we replace the least squares loss function with the Huber loss. The Huber loss makes the penalty incurred by larger points linear instead of quadratic, thus outliers have a smaller effect on the resulting estimator.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Quadratic programming", "weight": 1.0} -->

We set $m$ to the nearest integer of $1.5n$ and vary value of $n$ from $5000$ to $25000$.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Quadratic programming", "weight": 1.0} -->

Results for large QP tests are shown in Table LABEL:table:qp. We benchmark ten different examples from two classes above and set the time limit to $1$h. We compare our GPU implementation ClarabelGPU with ClarabelRs and two commercial solvers, Gurobi and MOSEK. ClarabelGPU is the fastest solver on these problems, and it has the lowest per-iteration time for almost all examples. Since most of time of an interior point solver is spent on factorizing and solving a linear system in QPs, we can say that ClarabelGPU benefits from the use of the cuDSS linear system solver and it is more than 2 times faster than Gurobi, about 4 times faster than MOSEK and 10x times faster than the existing Rust implementation with the multithreaded *faer-rs* linear system solver.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Second-order cone programming", "weight": 1.0} -->

We next consider the second-order cone relaxations of optimal power flow problems from the IEEE PLS PGLib-OPF benchmark library, using the *PowerModels.jl* package for modeling convenience. Note that only second-order cones of dimensionality $3$ or $4$ are used in these second-order cone relaxations, which satisfies our assumption in §3.3: that the dimensionality of each cone is very small.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Second-order cone programming", "weight": 1.0} -->

We compare our GPU implementation with the CPU-based Clarabel solver and MOSEK solver. We also include results of the MOSEK solver with pre-solve for comparison, which is denoted as Mosek\* in the plots. The maximum termination time is again set to $1$h. We benchmark the second-order cone relaxations of 120 problems from the PGLib-OPF library, where the number of second-order cones exceed $2000$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Second-order cone programming", "weight": 1.0} -->

Results for these problems are shown in Figure. Both ClarabelGPU and ClarabelRs are faster and more numerically stable than MOSEK even with the presolve step. Moreover, the GPU implementation can solve 118 out of 120 examples within an hour, while the Rust version of Clarabel can solve 104 out of 120 examples within the same time limit. In contrast, MOSEK with presolve fails on about 40% of the optimal flow problems, and the one without presolve fails on over 90% of the problems.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Second-order cone programming", "weight": 1.0} -->

Overall, the GPU solver is several times faster than Rust-based CPU solver. This speedup causes ClarabelGPU to achieve a lower failure rate than ClarabelRs as it could solve more problems in under $10^{4}$ seconds each. However, note that ClarabelGPU fails on two examples that ClarabelRs successfully solves. This highlights the different numerical performance of the linear system solvers between cuDSS and *faer-rs*.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Second-order cone programming", "weight": 1.0} -->

(c) Benchmark timings as shifted geometric mean and failure rates

<!-- chunk {"id": "body-0093", "role": "body", "section": "Second-order cone programming", "weight": 1.0} -->

with respect to $x$, $y$, $z$, and $r$. This problem is formulated over $T$ time periods, allocating wealth across $n$ assets while managing exposure to $k$ underlying factors. Here, $x_{t}$ represents asset allocations, $y_{t}$ represents factor exposures, $z_{t}$ represents trade volumes, and $r_{t}$ is a risk proxy. We impose additional constraints $x_{t} \in {\lbrack 0,0.1\rbrack}^{n}$, $y_{t} \in {\lbrack 0,0.1\rbrack}^{k}$, $z_{t} \in {\mathbb{R}}^{n}$, and $r_{t} \geq 0$. Our objective is a minimization over the trade-off between negative expected returns, linear transaction costs, and a second-order cone-based risk penalty scaled by risk aversion $\gamma$.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Second-order cone programming", "weight": 1.0} -->

The transaction constraints ensure that trade volumes $z_{t}$ correctly reflect changes in portfolio weights. Budget constraints enforce capital conservation: initial capital changes by a known inflow $d$, and total capital remains constant thereafter. Factor exposure is modeled via linear mappings $y_{t} = {F_{t}x_{t}}$. Risk $r_{t}$ is quantified through a second-order cone (SOC) constraint that captures both systematic risk $Uy_{t}$ and idiosyncratic risk $D_{\text{sqrt}} \odot x_{t}$ across each time period.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Second-order cone programming", "weight": 1.0} -->

We benchmark multistage portfolio optimization problems with ${n = 5000},{k = 50}$ and varying horizon $T$ in Table LABEL:table:parametric_programming_large_socp; ClarabelGPU achieved up to a $3$x speedup over MOSEK and $40$x over ClarabelRs.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Exponential cone programming", "weight": 1.0} -->

For exponential programming, we benchmark the entropy maximization problems with varying dimensionality. The entropy maximization problem aims to maximize entropy over a probability distribution given a set of $m$ linear inequality constraints, which can be interpreted as bounds on the expectations of arbitrary functions. The problem is formulated as

<!-- chunk {"id": "body-0097", "role": "body", "section": "Exponential cone programming", "weight": 1.0} -->

Each element of $A$ is generated from the distribution $A_{ij} \sim {\mathcal{N}{(0,n)}}$. Then, we set $b = {{{Av}/1^{T}}v}$ where $v \in \text{R}^{n}$ is generated randomly from $v_{i} \sim {U{\lbrack 0,1\rbrack}}$, which ensures the problem is always feasible. We set $m$ to the nearest integer of $0.5n$ and vary value of $n$ from $2000$ to $10000$.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Exponential cone programming", "weight": 1.0} -->

The benchmark results for these two problems with varying dimensionality are shown in Table LABEL:table:exponential_cone. Though the GPU acceleration of Clarabel is offset by nearly doubled number of iterations compared to MOSEK, we can still achieve more than 2 times of acceleration for the overall time. That is to say we can possibly achieve more acceleration in ClarabelGPU if we can improve the numerical stability to the same level of MOSEK on exponential cone programs. We find ClarabelGPU can benefit from GPU computation up to 10x times faster compared to ClarabelRs.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Semidefinite programming", "weight": 1.0} -->

Our results in Table LABEL:table:FEM_SDP show that ClarabelGPU achieves a speedup of $1.5 \times$ to $4 \times$ over MOSEK, both with and without presolve, and up to $10 \times$ speedup compared to ClarabelRs. ClarabelGPU can only solve FELA_SDP_9263 to $1e^{- 5}$ precision and is less numerical stable than Mosek\* under the default setting, but increasing the static regularization $\delta_{s}$ to $1e^{- 7}$ can fix the numerical issue.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Parametric programming", "weight": 1.0} -->

Clarabel supports updating the coefficients $P,A,q,b$ without reinitializing the solver object. This feature is particularly advantageous for parametric programming, where the solver setup is required only once, and the symbolic factorization structure can be reused efficiently in subsequent solves. Such capability is especially useful in applications like model predictive control and portfolio optimization.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Parametric programming", "weight": 1.0} -->

For the multistage portfolio optimization problem, we also split the total time into two parts, the setup time and the solve time, and report the ratio of them respectively in Table LABEL:table:time_ratio. Notably, the setup time for ClarabelGPU constitutes a larger proportion of the total time compared to its CPU counterpart. This suggests that, when the setup time dominates the total computational time, higher acceleration ratios can be achieved on a GPU when we need to solve multistage portfolio optimization multiple times with different parameters.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Mixed precision", "weight": 1.0} -->

In the implementation of the mixed precision setting, as described we only set the data type of the cuDSS linear system solver to. Since the use of mixed precision accelerates the numerical factorization rather than the symbolic factorization within a factorization method, we only record the computational time for an interior point method without the setup time.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Mixed precision", "weight": 1.0} -->

We test the mixed precision setting on QPs, including portfolio optimization and Huber fitting problems from §4.2, for high accuracy level $\epsilon_{\text{feas}} = {1e^{- 8}}$. We compare it with the standard GPU implementation of data type. The results in Table LABEL:table:mixed_large_qp demonstrate that employing a mixed-precision strategy can reduce solve time by up to a factor of 2 when the matrix $A$ becomes dense. However, we note that mixed precision is less numerically stable when solving an ill-conditioned KKT system. This can lead to an increased number of iterative refinement steps and longer solve times compared to full precision, or even failure to converge to the desired tolerance.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have developed a GPU interior point solver for conic optimization.^33^3 In our implementation, we propose a mixed parallel computing strategy to process linear constraints with second-order cone, exponential cone, power cone and semidefinite cone constraints. Our GPU solver shows several times acceleration compared to state-of-the-art CPU conic solvers on many problems to high precision, such as QPs, SOCPs, exponential cone programs and SDPs.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Future research directions include extending support to general SDPs with PSD cones of varying dimensionalities. The proposed mixed parallel computing strategy for GPU implementation is also applicable to conic solvers based on first-order operator-splitting methods. This approach could improve GPU utilization, especially when sufficient computational resources are available to handle different cone classes in parallel. Additional performance gains may be achieved through kernel fusion, the use of CUDA graphs to reduce kernel launch overhead and overlapping more independent computation within interior-point methods.
