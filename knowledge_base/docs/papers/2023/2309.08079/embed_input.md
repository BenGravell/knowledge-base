<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

MPCGPU: Real-Time Nonlinear Model Predictive Control through Preconditioned Conjugate Gradient on the GPU

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Nonlinear Model Predictive Control (NMPC) is a state-of-the-art approach for locomotion and manipulation which leverages trajectory optimization at each control step. While the performance of this approach is computationally bounded, implementations of direct trajectory optimization that use iterative methods to solve the underlying moderately-large and sparse linear systems, are a natural fit for parallel hardware acceleration. In this work, we introduce MPCGPU, a GPU-accelerated, real-time NMPC solver that leverages an accelerated preconditioned conjugate gradient (PCG) linear system solver at its core. We show that MPCGPU increases the scalability and real-time performance of NMPC, solving larger problems, at faster rates. In particular, for tracking tasks using the Kuka IIWA manipulator, MPCGPU is able to scale to kilohertz control rates with trajectories as long as 512 knot points. This is driven by a custom PCG solver which outperforms state-of-the-art, CPU-based, linear system solvers by at least 10x for a majority of solves and 3.6x on average.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nonlinear Model Predictive Control (NMPC) is a feedback control strategy which repeatedly solves finite horizon optimal control problems (OCP) in real time, enabling robots to adapt to changes in their environment. This approach has seen great recent success in applications to both locomotion and manipulation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most implementations of NMPC leverage trajectory optimization to solve the underlying optimal control problems. Two popular classes of these algorithms are shooting methods and direct methods. Shooting methods parameterize only the input trajectory and use Bellman's optimality principle to iteratively solve a sequence of smaller optimization problems. Direct methods explicitly represent the states, controls, dynamics, and any additional constraints, leading to moderately-large nonlinear programs with structured sparsity patterns.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

There has been historical interest in parallel strategies for solving trajectory optimization problems. This is growing increasingly important with the impending end of Moore's Law and the end of Dennard Scaling, which have led to a utilization wall that limits the performance a single CPU chip can deliver. Several more recent efforts have shown that significant computational benefits are possible by exploiting the natural parallelism in the computation of the (gradients of the) dynamics and cost functions on GPUs and FPGAs. However, multiple-shooting and consensus approaches to computing trajectory updates at each algorithmic iteration have only seen modest gains when implemented on alternative hardware platforms.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the other hand, direct methods naturally expose more parallelism that can be exploited through hardware acceleration. Importantly, these approaches are computationally dominated by the solutions of a moderately-large and sparse linear systems. Iterative methods, like the Preconditioned Conjugate Gradient (PCG) algorithm, are particularly well-suited for parallel solutions of linear systems, as they are computationally dominated by matrix-vector products and vector reductions, and have shown past success in outperforming state-of-the-art CPU implementations for solving very-large linear systems on GPUs.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we introduce MPCGPU, a GPU-accelerated, real-time NMPC solver that exploits the structured sparsity and the natural parallelism in direct trajectory optimization. At our solver's core is a custom, accelerated implementation of PCG tuned for the Schur complement of the KKT systems of trajectory optimization problems.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that MPCGPU increases the scalability and real-time performance of NMPC, solving larger problems, at faster rates. In particular, for tracking tasks using the Kuka IIWA manipulator, MPCGPU is able to scale to kilohertz rates with trajectories as long as 512 knot points. This is driven by a custom, GPU-accelerated, PCG solver which outperforms state-of-the-art, CPU-based, linear system solvers by at least 10x for a majority of solves and 3.6x on average.

<!-- chunk {"id": "body-0009", "role": "body", "section": "III-A Direct Trajectory Optimization", "weight": 1.0} -->

Trajectory optimization, also known as numerical optimal control, solves an (often) nonlinear optimization problem to compute a robot's path through an environment as a series of states $X = {\{ x_{0},\cdots,x_{N}\}}$ and controls $U = {\{ u_{0},\cdots,u_{N - 1}\}}$ for $x$ $\in {\mathbb{R}}^{n}$ and $u$ $\in {\mathbb{R}}^{m}$. These problems model the robot as a discrete-time dynamical system,

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-A Direct Trajectory Optimization", "weight": 1.0} -->

with a timestep $h$, and minimize an additive cost function,

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-A Direct Trajectory Optimization", "weight": 1.0} -->

Direct methods for trajectory optimization form a moderately-large and sparse nonlinear program. While there are a variety of algorithmic approaches used to solve these problems, most methods can be reduced to a three step process which is repeated until convergence.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A Direct Trajectory Optimization", "weight": 1.0} -->

*Step 3:* Apply the update step, ${\delta X^{\ast}},{\delta U^{\ast}}$, while ensuring descent on the original nonlinear problem through the use of a merit-function and a trust-region or line-search.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-B The Schur Complement Method", "weight": 1.0} -->

By defining the variables $\theta$, $\phi$, and $\zeta$,

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-C Iterative Methods", "weight": 1.0} -->

Iterative methods solve the problem ${S\lambda^{\ast}} = \gamma$ for a given $S$ and $\gamma$ by iteratively refining an estimate for $\lambda$ up to some tolerance $\epsilon$. The most popular of these methods is the conjugate gradient (CG) algorithm which has been used for state-of-the-art results on large-scale optimziation problems on the GPU. The convergence rate of CG is directly related to the spread of the eigenvalues of $S$. Thus, a preconditoning matrix $\Phi \approx S$ is often applied to instead solve the equivalent problem with better numerical properties: ${\Phi^{- 1}S\lambda^{\ast}} = {\Phi^{- 1}\gamma}$. To do so, the preconditioned conjugate gradient (PCG) algorithm leverages matrix-vector products with $S$ and $\Phi^{- 1}$, as well as vector reductions, both parallel friendly operations.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-D Graphics Processing Units (GPUs)", "weight": 1.0} -->

Compared to a multi-core CPU, a GPU is a larger set of simpler processors, optimized for parallel execution of identical instructions. GPUs are best at computing regular and separable computations, over large data sets, with limited synchronization (e.g., large matrix multiplication). Our work uses NVIDIA's CUDA extensions to C++.

<!-- chunk {"id": "body-0016", "role": "body", "section": "The MPCGPU Solver", "weight": 1.0} -->

In this section we describe the design of the MPCGPU solver which exploits the sparsity and natural parallelism found in direct trajectory optimization algorithms and iterative linear system solvers. To further promote efficient GPU acceleration, unlike generic approaches, which require a kernel launch and CPU-GPU synchronization for each matrix operation, MPCGPU uses only three kernels that are asynchronously queued, resulting in only a single CPU-GPU synchronization. We also only transfer the initial and final values between the CPU and GPU to reduce I/O overheads.

<!-- chunk {"id": "body-0017", "role": "body", "section": "The MPCGPU Solver", "weight": 1.0} -->

As shown in Figure, our approach can be broken down into a three step process. At each control step we first compute each block row of the Schur complement system, $S$ and $\gamma$, as well as our preconditioner, $\Phi^{- 1}$, in parallel by taking advantage of the structured sparsity of those matrices. Next, we use our custom GPU-optimized, warm-started, PCG solver, GBD-PCG, to compute the optimal Lagrange multipliers, $\lambda^{\ast}$, and reconstruct the optimal trajectory update, ${\delta X^{\ast}},{\delta U^{\ast}}$. Finally we leverage a parallel line search to compute the final trajectory $X,U$ which we send to the (simulated) robot for execution and simultaneously measure the current state of the (simulated) robot to begin our next control step. In the remainder of this section we provide further details on our approach.

<!-- chunk {"id": "body-0018", "role": "body", "section": "The MPCGPU Solver", "weight": 1.0} -->

Algorithm 1 Preconditioned Conjugate Gradient (PCG)

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Parallel Computation of $S,\\gamma$, and $\\Phi^{- 1}$", "weight": 1.0} -->

To efficiently compute $S,\gamma$, and $\Phi^{- 1}$ on the GPU, we need to find a naturally parallel approach to form the values as well as an efficient data storage format that minimizes overheads. We also need to find an effective preconditioner that is parallel-friendly in its computation.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A Parallel Computation of $S,\\gamma$, and $\\Phi^{- 1}$", "weight": 1.0} -->

We first leverage the block-tridiagonal structure of the Schur complement, $S$, as shown in Equation, which is for the most part independent across timesteps, $k$, for each block-row. This pattern also extends to each block-row of the $\gamma$ vector. To further remove the need for synchronizations, for each $k$, we also compute the only cross-timestep quantities, $Q_{k + 1}$ and $q_{k + 1}$. While this results in those terms being computed twice, it still proves to be more efficient than forcing a synchronization point between all block-rows. To ensure efficient computation of the underlying dynamics and kinematic quantities, we leverage the GRiD library, which was shown to outperform state-of-the-art CPU libraries even when taking into account I/O overheads.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-A Parallel Computation of $S,\\gamma$, and $\\Phi^{- 1}$", "weight": 1.0} -->

We further parallelize across and within the many small matrix inversions and matrix multiplications within each parallel block-row computation. Leveraging best practices, we also group together the various types of mathematical operations, storing intermediate values in shared memory, and re-ordering computations where needed.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A Parallel Computation of $S,\\gamma$, and $\\Phi^{- 1}$", "weight": 1.0} -->

The structure of $\Phi^{- 1}$ also permits mostly parallel computation as only the values of each $\theta_{k}^{- 1}$ need to be shared across timesteps. Our approach thus requires only a single global synchronization across blocks, and allows us to store the block-tridiagonal $S$ and $\Phi^{- 1}$ matrices in a custom, compressed, dense format for increased IO bandwidth and memory efficiency.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B GPU Parallel PCG for Block-Tridiagonal Systems", "weight": 1.0} -->

The core of our solver is a custom GPU Parallel PCG implementation specifically optimized for block-tridiagonal systems, GBD-PCG. That is, we leverage the sparsity structure of $S$ and $\Phi^{- 1}$ to maximize cache usage and natural parallelism resulting in a refactored, low-latency implementation with minimal synchronizations. These optimizations can be leveraged in the most computationally expensive part of the algorithm, the large matrix-vector products in lines 5, 6, and 8 of Algorithm, as each element of the product depends on at most $3n_{b}$ elements from the matrix and $3n_{b}$ elements from the vector, where $n_{b}$ is the block dimension. We exploit this by grouping threads that access similar elements into thread blocks and storing $S$, $\Phi^{- 1}$, and all PCG iterates concurrently in shared (cache) memory on the GPU.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B GPU Parallel PCG for Block-Tridiagonal Systems", "weight": 1.0} -->

We also operate as many steps of the algorithm fully in parallel as possible between the thread synchronizations needed for the parallel reductions of scalar values on lines 6, 12, and 21 of Algorithm. Similarly, we only use device memory (RAM) for those scalar reductions and for the values of $p$ and $r$ that need to be shared between blocks on lines 9 and 18 of Algorithm. This means that the choice of a sparse preconditioner not only enables its efficient computation and memory storage, but also reduces the number of synchronizations and amount of memory that needs to be shared through RAM during each PCG iterate. This holistic co-design across algorithm stages is part of the reason why MPCGPU is so performant. Finally, we warm-start the values for $\lambda$ based on the previous solve which we found greatly increased overall performance by reducing the number of PCG iterations needed for convergence.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B GPU Parallel PCG for Block-Tridiagonal Systems", "weight": 1.0} -->

Algorithm 2 GPU Parallel PCG for Block-Tridiagonal Systems (GBD-PCG) (S, Φ−1, γ, λ, ϵ) → λ*

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-C Parallel Line Search", "weight": 1.0} -->

We leverage a parallel line search, computing all possible iterates for $\alpha \in {\mathbb{A}}$ in parallel^11^1In this work we use ${\mathbb{A}} = \left\{ 1,\frac{1}{2},\cdots,\frac{1}{256} \right\}$, but any decaying set of fractional values can be used in practice. and selecting the iterate with the best value according to its L1 merit function. This allows MPCGPU to evaluate all possible line search iterates in the same amount of time as it would take to compute a single iterate under a standard backtracking approach. Importantly, this not only reduces latency of this step, but has also been shown to improve the convergence of NMPC on similar whole-body trajectory tracking problems.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Results", "weight": 1.0} -->

In this section we present a two-part evaluation of MPCGPU through a case study of online, dynamic, multi-goal, end-effector position tracking using whole-body NMPC for a simulated Kuka IIWA manipulator. First, we compare the performance of our underlying GBD-PCG iterative linear system solver with the state-of-the-art, CPU-based, QDLDL solver. Second, we show how the end-to-end performance enabled by MPCGPU allows us to scale to long time horizons and fast control rates. Source code accompanying this evaluation can be found at

<!-- chunk {"id": "body-0028", "role": "body", "section": "V-A Methodology", "weight": 1.0} -->

Results were collected on high-performance workstation with a $3.2$GHz 16-core Intel i9-12900K and a $2.2$GHz NVIDIA GeForce RTX 4090 GPU running Ubuntu 22.04 and CUDA 12.1. Code was compiled with g++11.4, and time was measured with the Linux system call clock_gettime, using CLOCK_MONOTONIC as the source. Our performance analysis is drawn from 100 NMPC trials of a 10 second, 5 goal, pick-and-place circuit for a simulated Kuka IIWA-14. Each NMPC trial consists of thousands of linear system solves which are needed for the many iterations of the underlying trajectory optimization problem for end-effector position tracking solved at each control step. All hyperparameter values can be found in our open-source source code and resulted in an average tracking error of $\sim$`<!-- -->`{=html}10cm, providing similar performance as previous experiments with GPU accelerated NMPC.

<!-- chunk {"id": "body-0029", "role": "body", "section": "V-A Methodology", "weight": 1.0} -->

In particular, we note that all solvers used the same quadratic cost functions for each amount of knot points, and solver-specific hyperparameter values were independently tuned for maximal performance.

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-B Linear System Solver Performance", "weight": 1.0} -->

We evaluate the performance of our underlying GBD-PCG linear system solver over its thousands of solves during each of our 100 NMPC trials running at a 500hz control rate and compare its performance to the state-of-the-art CPU-based QDLDL solver operating in the same context.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-B Linear System Solver Performance", "weight": 1.0} -->

Average Solve Time: Our results show that our GPU based solver outperforms QDLDL across most problem sizes and is only marginally slower at the smallest problem size, obtaining as much as a 3.6x average speedup. This is driven by the GPU's ability to leverage large scale parallelism to gracefully scale to larger problem sizes. We note that the speedup plateaus at 256 knot points as we begin to run out of hardware resources on our specific GPU. These results show that unlike generic approaches that become performant at tens to hundreds of thousands of variables, our domain-specific co-design approach enables the GPU to outperform the CPU even on moderately-sized linear systems (our experiments range from 448 to 7,168 variables).

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-B Linear System Solver Performance", "weight": 1.0} -->

Performance Distribution: Importantly, in most cases, the speedup is much larger than this. This is because iterative methods have a variable runtime as they can exit early depending upon the exit tolerance, $\epsilon$. We demonstrate this using the 128 knot point problem as a case study in Figure.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-B Linear System Solver Performance", "weight": 1.0} -->

We plot the distribution of solve times for QDLDL against GPU-PCG $\epsilon = {1e^{- 4}}$, resulting in our 1.9x average speedup in Figure, as well as $\epsilon = {5e^{- 5}}$ and $\epsilon = {1e^{- 5}}$. QDLDL presents a uni-modal timing distribution with almost all solves occurring between 280 and 305 $\mu$s. GBD-PCG, on the other hand, presents a bi-modal timing distribution clustered both much faster and a little slower than QDLDL. For example, for $\epsilon = {1e^{- 4}}$, 65% of GBD-PCG solves are $\geq$`<!-- -->`{=html}10x faster than the fastest QDLDL solve, and the slowest GBD-PCG solve is only 2.5x slower than the slowest QDLDL solve (with only 10% of solves $\geq$`<!-- -->`{=html}2x slower).

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-B Linear System Solver Performance", "weight": 1.0} -->

Furthermore, while all values of $\epsilon$ shown in the plot were able to successfully track the target trajectory, the lower the exit tolerance, the more of the distribution mass shifted to being $\geq$`<!-- -->`{=html}10x faster than QDLDL (65%, 52%, 20% for $\epsilon = {{1e^{- 4}},{5e^{- 5}},{1e^{- 5}}}$ respectively). However, when $\epsilon$ was reduced even farther, our entire NMPC controller was unable to accurately track our target trajectory. These results present interesting directions for future work to find ways to eliminate the second slower mode of the solve time distribution while ensuring robust NMPC convergence.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-C End-to-End NMPC Performance", "weight": 1.0} -->

To validate efficacy for use in NMPC for robotics applications, we also demonstrate the impact of our approach on the number of iterations of MPCGPU we could achieve at each control step for varying control rates and trajectory lengths. Figure shows the resulting number of average trajectory optimization solver iterations we can compute while meeting the specified control rates and trajectory lengths using both our GBD-PCG solver as well as QDLDL to solve the thousands of underlying linear systems.^22^2We note that in the QDLDL case, as the NMPC loop is running on the GPU, data needs to be copied onto the host before executing the solve and converted into the sparse CSR matrix format. To ensure fair comparisons and avoid overheads for unnecessary data transfers and transformations, we implemented a variant of our parallel Schur complement computation which directly stores data in the CSR format expected by QDLDL.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-C End-to-End NMPC Performance", "weight": 1.0} -->

Regardless of the linear system solver, our GPU-first approach, with both fast parallel construction of the Schur complement and fast parallel computation of the line search, enables trajectories as long as $128$ knot points to operate at a $1$kHz control rate, and achieve at least $4$ iterations at a $500$Hz control rate, for a per-iteration rate of $2$kHz. Furthermore, similar to what we witness in the case of average linear system solve times, as the problem gets larger and the control rate increases, our fully GPU-based approach is increasingly performant. Highlights include our approach's ability to scale to $512$ knot points at a $1$kHz control rate and execute $8$ iterations for 128 knot points at a $500$Hz control rate, for a per-iteration rate of $4$kHz. These results compare favorably to previously reported results in the literature of about $500$hz to $1$kHz per-iteration rates for trajectories of $30$ to $120$ knot points using state-of-the-art CPU-based and GPU-based solvers for similar NMPC tasks.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-C End-to-End NMPC Performance", "weight": 1.0} -->

As such, our GPU-first approach opens up the possibility for our NMPC solver to either leverage longer horizon trajectories, run at faster control rates, produce more optimal solutions for the same horizon and control rate, or include some combination of those highly beneficial traits.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In this work, we introduce MPCGPU, a GPU-accelerated, real-time NMPC solver built around a parallel PCG solver. MPCGPU exploits the structured sparsity and natural parallelism in both direct trajectory optimization algorithms and iterative linear system solvers. Our experiments show that our approach is able to scale NMPC to larger problems, and operate it at faster rates, than is possible with existing state-of-the-art solvers. In particular, for tracking tasks using the Kuka IIWA manipulator, MPCGPU is able to scale to kilohertz control rates with trajectories as long as 512 knot points. For this problem, our GPU-based PCG solver outperforms a state-of-the-art CPU-based linear system solver by as much as 10x for a majority of solves and 3.6x on average.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

There are many promising directions for future work to improve the functionality and usability of our approach. Most importantly, like all iterative methods, our GPU-based PCG solver exhibits variability in its solve times. Future work which learns when to leverage iterative methods vs. factorization-based methods, or which learns dynamic values for hyperparameters to reduce the worst-case runtimes, without sacrificing overall NMPC robustness, would greatly improve average-case performance. Furthermore, it would be interesting to explore the performance implications of adding additional constraints either through expanding the KKT system, or through augmented Lagrangian or operator splitting methods. Finally, we would like to evaluate our approach on physical robots at the edge using low-power GPU platforms such as the NVIDIA Jetson.
