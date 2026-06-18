<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

GRiD: GPU-Accelerated Rigid Body Dynamics with Analytical Gradients

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce GRiD: a GPU-accelerated library for computing rigid body dynamics with analytical gradients. GRiD was designed to accelerate the nonlinear trajectory optimization subproblem used in state-of-the-art robotic planning, control, and machine learning, which requires tens to hundreds of naturally parallel computations of rigid body dynamics and their gradients at each iteration. GRiD leverages URDF parsing and code generation to deliver optimized dynamics kernels that not only expose GPU-friendly computational patterns, but also take advantage of both fine-grained parallelism within each computation and coarse-grained parallelism between computations. Through this approach, when performing multiple computations of rigid body dynamics algorithms, GRiD provides as much as a 7.2x speedup over a state-of-the-art, multi-threaded CPU implementation, and maintains as much as a 2.5x speedup when accounting for I/O overhead. We release GRiD as an open-source library for use by the wider robotics community.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Efficient implementations of rigid body dynamics and their gradients have become key computational kernels for robotics applications. Originally required mostly for the nonlinear trajectory optimization sub-problems of model-based planning and control systems for high degrees-of-freedom robots, these computational kernels are also growing in importance for machine learning (ML) techniques.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite being highly accurate and optimized, existing implementations of spatial-algebra-based approaches to rigid body dynamics do not take advantage of opportunities for parallelism present in the algorithm, limiting their performance. This is critical because there is natural parallelism in many bottleneck computations involving rigid body dynamics in robotics. For example, the gradient of forward dynamics accounts for $30$% to $90$% of typical nonlinear model-predictive control (MPC) implementations, and is naturally parallel across the discrete points in the trajectory.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

While there is a growing need for parallel computation, the performance of multi-core CPUs has been limited by thermal dissipation, enforcing a utilization wall that restricts the performance a single chip can deliver. This has motivated increased use of GPUs, which can provide opportunities for higher performance by supporting larger-scale parallelism within a single chip.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we introduce *GRiD*, a GPU-accelerated library for spatial-algebra-based rigid body dynamics and their analytical gradients. GRiD is designed to accelerate the nonlinear trajectory optimization subproblem used in state-of-the-art robotic planning, control, and machine learning algorithms. GRiD is optimized to use blocks of GPU threads to compute the tens to hundreds of naturally parallel computations of rigid body dynamics and their gradients found in these algorithms, and implements the more accurate spatial-algebra-based formulation of rigid body dynamics used in state-of-the-art trajectory optimization. GRiD builds on recent work which designed a manually-optimized GPU implementation of rigid body dynamics gradients for a seven-link serial chain manipulator, providing further optimizations and generalizations to support multiple dynamics algorithms, URDF parsing of most common robot models, and optimized code generation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

GRiD not only unlocks the ability for nonlinear trajectory optimization to run entirely on the GPU, but when performing multiple computations of rigid body dynamics and their gradients, it also provides as much as a 7.2x speedup over a state-of-the-art, multi-threaded CPU implementation running on a high-performance workstation. GRiD also enables the use of a GPU as a rigid body physics accelerator for algorithms that are computed on a host CPU, maintaining as much as a 2.5x speedup when accounting for the I/O communication overhead between the CPU and GPU.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We release GRiD as an open-source library to enable robotics researchers to better explore and leverage the performance gains from large-scale parallelism on GPU platforms. Our library can be found at

<!-- chunk {"id": "body-0009", "role": "body", "section": "III-A Computing Hardware: CPUs vs. GPUs", "weight": 1.0} -->

Compared to a multi-core CPU, a GPU has a much larger set of simpler processors, optimized specifically for parallel computations with identical instructions operating over data accessed in regular patterns. Each GPU processor has many more arithmetic logic units (ALUs), but reduced control logic and a smaller cache memory (see Figure 1). GPUs are therefore best at computing highly regular and separable computations over large working sets of data (e.g., large matrix-matrix multiplication) where much of the cache, referred to as shared memory, can be manually manged by the programmer. We also note that data must be transferred between the CPU and GPU incurring I/O overhead.

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-A Computing Hardware: CPUs vs. GPUs", "weight": 1.0} -->

Our work uses NVIDIA's CUDA extensions to C++ which uses parallel blocks of threads to compute functions on the GPU. Each block's threads access a shared cache and are guaranteed to run on the same processor, but the ordering of the blocks is not guaranteed. For more information on CUDA and its programming model we suggest reading the NVIDIA CUDA programming guide.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-B Rigid Body Dynamics", "weight": 1.0} -->

Common algorithms include: Forward Dynamics, computing $\overset{¨}{q}$ when given $q,\overset{˙}{q},\tau$, and optionally $F$; Inverse Dynamics, computing $\tau$ when given $q,\overset{˙}{q},\overset{¨}{q}$ and optionally $F$; as well as the computations of the various terms present in Equation 1.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-B Rigid Body Dynamics", "weight": 1.0} -->

During computation, spatial algebra represents most quantities as operations over vectors in ${\mathbb{R}}^{6}$ and matrices in ${\mathbb{R}}^{6 \times 6}$, defined in the frame of each rigid body. These frames are numbered $i = {1\text{~to~}n}$ such that each body's parent $\lambda_{i}$ is a lower number. Most rigid body dynamics algorithms operate via outward and inward loops over these frames collecting and transforming forces, accelerations, velocities, and inertias. Transformation matrices from frame $\lambda_{i}$ to $i$ are denoted as ${}_{}^{}{}_{\lambda i}^{}$ and can be constructed from the rotation and translation between the two coordinate frames, which themselves are functions of the joint position $q_{i}$ between those frames and constants derived from the robot's topology.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-B Rigid Body Dynamics", "weight": 1.0} -->

The mass distribution of each link is denoted by its spatial inertia $I_{i}$, and $S_{i}$ is a joint-dependent term denoting in which directions a joint can move (and is often a constant). Finally, spatial algebra uses spatial cross product operators $\times$ and $\times^{\ast}$, in which a vector is re-ordered into a matrix, and then a standard matrix multiplication is performed.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-B Rigid Body Dynamics", "weight": 1.0} -->

For more information on spatial-algebra-based rigid body dynamics we suggest reading Featherstone's Rigid Body Dynamics Algorithms.

<!-- chunk {"id": "body-0015", "role": "body", "section": "The GRiD Library", "weight": 1.0} -->

The open-source GRiD library can be found at In this section we describe its design, features and code optimization approach.

<!-- chunk {"id": "body-0016", "role": "body", "section": "IV-A Design", "weight": 1.0} -->

Our overarching design methodology was to make GRiD easily adoptable and extensible by other robotics researchers. As such, the resulting optimized CUDA C++ code is designed to be header-only with only a single dependency, the standard cuda_runtime.h library.^11^1Even during URDF parsing and code generation, GRiD only requires the beautifulsoup4, lxml, numpy, and sympy Python libraries. We also provide APIs that allows users to automatically initialize and allocate all necessary memory on the CPU and GPU and integrate GRiD either directly into their existing CUDA code or through standard CPU C++ function calls.

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-A Design", "weight": 1.0} -->

Finally, the GRiD library is built using a set of modular open-source packages (shown in Figure 2) to enable easy extension, and re-use by other robotics researchers. Our GRiD package wraps and automates our GPU code generation engine (GRiDCodeGenerator), a self-contained URDF parser (URDFParser), and a set of reference implementations of rigid body dynamics algorithms (RBDReference) that can be used for code validation and testing. We also provide the benchmark experiments as described in Section V as a separate package (GRiDBenchmarks), as they require the support of additional external libraries.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-B Current Features", "weight": 1.0} -->

The Recursive Newton Euler Algorithm (RNEA) for inverse dynamics;

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-B Current Features", "weight": 1.0} -->

The direct inverse of mass matrix ($M^{- 1}$);

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-B Current Features", "weight": 1.0} -->

The analytical gradient of inverse dynamics with respect to the robot's position and velocity ($q,\overset{˙}{q}$);

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B Current Features", "weight": 1.0} -->

The analytical gradient of forward dynamics with respect to the robot's position, velocity, and input torque ($q,\overset{˙}{q},u$) via $\frac{\partial\overset{¨}{q}}{\partial u} = {- {M^{- 1}\frac{\partial{\text{RNEA}{(q,\overset{˙}{q},\overset{¨}{q})}}}{\partial u}}}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B Current Features", "weight": 1.0} -->

Directions for future work include extending this core with additional algorithms and joint types (see Section VI).

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-C Code Optimization Approach", "weight": 1.0} -->

GRiD builds on recent work which designed a manually-optimized GPU implementation of rigid body dynamics gradients for a seven-link serial chain manipulator. This section details how GRiD leverages the optimizations identified in that prior work, and how GRiD extends and generalizes those optimizations to enable acceleration of both a much larger class of robot models and additional rigid body dynamics algorithms through URDF driven code generation.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-C Code Optimization Approach", "weight": 1.0} -->

Previous work has shown that a robot's topology and joint types directly define structured sparsity patterns and opportunities for parallelism in the resulting spatial-algebra-based rigid body dynamics algorithms. GRiD leverages coarse-grained parallelism using multi-threading between independent computations, as well as *fine-grained parallelism within each computation*. For example, within each independent gradient computation, each column of that computation can be computed in parallel. Similarly, within those computations each entry in each matrix-matrix or matrix-vector multiplication can be computed in parallel. GRiD is able to achieve high performance by taking advantage of this fine-grained parallelism, through the use of blocks of parallel threads on a GPU.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-C Code Optimization Approach", "weight": 1.0} -->

In order for a GPU to effectively take advantage of such fine-grained parallelism, however, previous work also demonstrated that the target algorithm needs to be refactored to remove synchronization points, and to coalesce both memory accesses and computational operations. This is particularly important for the spatial cross product operations (Equation 2) which result in out-of-order memory accesses and an expansion of the dimension of the input vector into an output matrix. We adapt the refactoring approach used in prior work, moving computations out of serial loops by creating temporary variables that can be computed in parallel.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-C Code Optimization Approach", "weight": 1.0} -->

GRiD extends and generalizes these parallelism-generating optimizations, enabling it to target any robot with a branched tree topology (e.g., Figure 3). To do this, we inject additional optimizations to accommodate multiple branching points at different levels of the tree. For example, since dependencies in the serial passes of rigid body dynamics algorithms are between parent and child frames in the tree, we can compute "sibling" frames in parallel. For example, the forward pass of $\nabla$RNEA (Algorithm 1) computes the temporary variables ${\partial v_{i}},{\partial a_{i}}$ for frame $i$ as a function of ${\partial v_{\lambda_{i}}},{\partial a_{\lambda_{i}}}$ for its parent frame $\lambda_{i}$ (Lines 2 and 3). Therefore, we can compute each ${\partial v_{i}},{\partial a_{i}}$ by stepping serially through the levels of the tree, while computing all frames within each level in parallel.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-C Code Optimization Approach", "weight": 1.0} -->

For the robot shown in Figure 3, we would compute the values associated with frame 0, then 1 and 5 in parallel, then 2, 4, and 6 in parallel, and finally 3. GRiD also performs loop unrolling on these remaining serial loops to enable the compiler to easily optimize the resulting code. Then, once all ${\partial v},{\partial a}$ have been computed, all $\partial f$ can be computed fully in parallel.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-C Code Optimization Approach", "weight": 1.0} -->

When supporting arbitrarily large robots it is also important to ensure that the temporary variables fit into the GPU cache. At code generation time, GRiD determines if it is necessary to forgo any temporary memory computations in order to support robots with many degrees-of-freedom (dof). For example, for the 30 dof Atlas humanoid, GRiD does not compute each $v \times$ matrix in parallel and then use threaded matrix multiplication (as in previous work ), but instead computes $v_{1} \times v_{2}$ in a few parallel threads, trading off a slight latency penalty for a large savings in shared memory usage. This results in the refactored forward pass of the $\nabla$RNEA algorithm shown in Algorithm 2.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-C Code Optimization Approach", "weight": 1.0} -->

GRiD also leverages the robot's topology to determine sparsity patterns in the many temporary variables needed for the gradient computations. As such, columns of temporary memory variables that would be all zeros are skipped and shared memory is compressed to effectively remove those columns. For most robot models this leads to significant savings. For example, reducing shared memory usage for the the quadruped robot HyQ by more than 60%. ^22^2 Most required memory offsets are computed and cached at code generation time. GRiD employs non-branching *if/else* constructs (e.g., result = flag$\ast$val1 + !flag$\ast$val2) to avoid the branching performance penalty for any other pointer offsets or control flow switches.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-C Code Optimization Approach", "weight": 1.0} -->

Finally, GRiD employs further optimizations for certain classes of robot models. For example, for all single chain robots, the parent's frame number is always one less than the child's. For these robots, the code generated by GRiD will remove any indirect references to the parent (or child) frame number and instead simply subtract (or add) one.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-C Code Optimization Approach", "weight": 1.0} -->

GRiD applies similar patterns of refactorings, memory compressions, and computational optimizations across all of the algorithms described in Section IV-B.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Performance Benchmarks", "weight": 1.0} -->

We benchmark the GRiD library against the Pinocchio library,^33^3We used the pinocchio3-preview branch for the latest optimized code. a state-of-the-art CPU-implementation of rigid body dynamics that supports optimized CPU code generation of both rigid body dynamics and its analytical gradients. Source code accompanying this evaluation can be found at [

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-A Methodology", "weight": 1.0} -->

We used a high-performance workstation with a $3.8$GHz eight-core Intel Core i7-10700K CPU and a $1.44$GHz NVIDIA GeForce RTX 3080 GPU running Ubuntu 20.04 and CUDA 11.4.^44^4For clean timing measurements on the CPU, we disabled TurboBoost and fixed the clock frequency to the maximum. Code was compiled with Clang 12 and g++9.4, and time was measured with the Linux system call clock_gettime, using CLOCK_MONOTONIC as the source. We compare timing results across three robot models: the 7 degrees-of-freedom (dof) Kuka LBR IIWA-14 manipulator, the 12 dof HyQ quadruped, and the 30 dof Atlas humanoid. For single computation and multiple computation latency, we took the average of one million, and one hundred thousand trials, respectively.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-B Multiple Computation Latency", "weight": 1.0} -->

To characterize our performance in a typical nonlinear trajectory optimization scenario, which uses tens to hundreds of naturally parallel computations of dynamics algorithms, we evaluate the latency for $N = 16$, $32$, $64$, $128$, and $256$ computations of the gradient of forward dynamics using Pinocchio and GRiD across robot models in Figure 4. These times are broken down into computation time on the CPU or GPU and the GPU I/O overhead. The plot is overlayed with the speedup (or slowdown) of GRiD compared to Pinocchio in pure computation alone, and also the speedup including I/O overhead. We use the gradient of forward dynamics as our representative kernel because it uses many of the other kernels as sub-routines and is the most computationally intense kernel, clearly demonstrating scaling trends.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-B Multiple Computation Latency", "weight": 1.0} -->

The GPU outperforms the CPU on all but one of the multiple computation latency tests, even when accounting for I/O. In the one test where the CPU is faster---for the fewest computations, including I/O, for IIWA, the smallest robot with only a single limb---the GPU is still 0.9x as fast.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-B Multiple Computation Latency", "weight": 1.0} -->

Even on the CPU, this benchmark shows how important it is to take advantage of coarse-grained parallelism between computations. For example, the gradient of forward dynamics kernel ($\nabla{FD}$ in Table I) took 2.9, 4.3, and 20.9 $\mu$s for a single computation for IIWA, HyQ, and Atlas respectively. If we ran it 256 times serially it would therefore take over 742, 1091, and 5355 $\mu$s. As Figure 4 shows, computing it in parallel on 8-cores only takes 123, 172, 865 $\mu$s, saving 83-84% of the computation time.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-B Multiple Computation Latency", "weight": 1.0} -->

However, since the CPU only has 8 cores, it is unable to efficiently scale to take advantage of high numbers of naturally parallel computations, taking 5.4x, 6.2x, and 11.8x as long to compute N = 256 as compared to N = 16 for IIWA, HyQ, and Atlas respectively.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-B Multiple Computation Latency", "weight": 1.0} -->

The GPU, on the other hand, is designed to scale to higher numbers of computations without incurring a latency penalty by launching independent blocks of threads for each computation. In fact, for IIWA and HyQ, N = 256 takes only 1.3x and 1.5x as long as N = 16. This leads to the GPU outperforming the CPU by 5.3x and 7.2x for N = 256, and maintaining a 2.5x and 2.1x speedup when including I/O.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-B Multiple Computation Latency", "weight": 1.0} -->

For the much higher-dof Atlas robot, the GPU still outperforms the CPU for N = 256 by 5.0x, and 2.0x when including I/O. However, unlike with IIWA and HyQ, this performance increase is almost identical to the increase at N = 128 and N = 64. This stall in performance improvement is caused by the large amount of shared memory needed for Atlas's 30 dof which starts to limit the number of parallel blocks of threads that can fit concurrently on the GPU hardware.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-B Multiple Computation Latency", "weight": 1.0} -->

Finally, we note that for the GPU, I/O overhead accounts for 53-71% of the total time for N = 256. This indicates that GRiD can provide the highest performance if integrated directly into an entirely GPU-based algorithm, instead of being used to accelerate a step of a CPU-based algorithm. In either case, however, if there is sufficient parallel work to be done, GRiD can reduce the overall computational latency.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-C Single Computation Latency Scaling", "weight": 1.0} -->

For further analysis of the GPU performance benefits demonstrated in Section V-B, we plot the latency scaling, excluding I/O overheads, of a single computation of each rigid body dynamics algorithm, from IIWA to HyQ and IIWA to Atlas, on both the CPU and GPU in Figure 5, and list absolute timings in Table I. We also plot the scaling of the robots' dof as a measure of their computational complexity.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-C Single Computation Latency Scaling", "weight": 1.0} -->

We find that the GPU is able to scale to more complex robots and algorithms better than the CPU by taking advantage of fine-grained parallelism induced by independent robot limbs and the independent columns of gradient computations. As expected (and consistent with previous work ), the GPU is slower on a single computation than the CPU, but the GPU demonstrates better scalability across both algorithm and robot complexity. For example, as shown in Table I, for $\nabla{FD}$, the CPU is 4.4x faster than the GPU (2.9$\mu$s vs. 12.9$\mu$s), but only 2.0x faster for Atlas (20.9$\mu$s vs. 42.1$\mu$s). That said, the CPU is still faster than the GPU for all individual computations, showing that GPU acceleration only makes sense when there is sufficient parallel work to be done.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-C Single Computation Latency Scaling", "weight": 1.0} -->

On the CPU, the latency of each algorithm scales directly with its computational intensity, with the gradients requiring significantly more computation (see Table I). The most computationally intensive algorithm, the forward dynamics gradient ($\nabla{FD}$), takes 2.9, 4.3, and 20.9 $\mu$s for IIWA, HyQ, and Atlas, while the simplest algorithm, inverse dynamics ($ID$) takes 0.3, 0.3, and 1.1 $\mu$s---a 9.7x to 19.0x slowdown.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-C Single Computation Latency Scaling", "weight": 1.0} -->

CPU latency also scales with the dof of the robot (Figure 5). For example, as the robot's dof increases by a factor of 1.7x from IIWA to HyQ, the computation time also increase by 1.1x, for the $O{(N)}$ $ID$ algorithm, up to 1.5x, for the $O{(N^{2})}$ $\nabla{FD}$ algorithm. It appears that this strong performance is due to the code generation taking advantage of the the many shared computations in the gradients, as well as the sparsity induced by HyQ's independent limbs, which decrease the longest path through the rigid body tree from 7 on IIWA to 3 on HyQ. However, these optimizations are mitigated by the Atlas model, which has a much larger 30 dof, and a longest path through the rigid body tree of 8. Atlas has 4.3x the dof of IIWA, but has a 3.9x ($ID$) to 7.2x ($\nabla{FD}$) slowdown on the CPU.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-C Single Computation Latency Scaling", "weight": 1.0} -->

By contrast, the GPU is able improve its scalability by not only taking advantage of sparsity and shared computations, but *also the opportunities for fine-grained parallelism* caused by both independent limbs in complex robot models, and independent columns of the gradient computations. For example, Table I shows that by taking advantage of parallelism in the gradient computations, the GPU is not only able to compute $\nabla{ID}$ faster than $FD$, but also only takes 12.9, 11.0, and 42.1 $\mu$s (for IIWA, HyQ, Atlas) for $\nabla{FD}$ as compared to 3.0, 3.2, and 8.0 $\mu$s for $ID$---a slowdown of only 3.4x to 5.3x, and a significant reduction from the CPU's 9.7x to 19.0x slowdown for these algorithms.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-C Single Computation Latency Scaling", "weight": 1.0} -->

Similarly, Figure 5 shows that by leveraging limb-based parallelism, the GPU computes forward dynamics ($FD$) and both gradients (${\nabla{ID}},{\nabla{FD}}$) faster for HyQ than for IIWA, and only has a 2.7x to 3.3x slowdown from IIWA to Atlas, again a significant reduction from the CPU's 3.9x to 7.2x.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In this work, we introduce GRiD, a GPU-accelerated rigid body dynamics library with analytical gradients. We found that by leveraging large-scale parallelism when performing multiple computations of rigid body dynamics algorithms, GRiD can provide as much as a 7.2x speedup over a state-of-the-art, multi-threaded CPU implementation and maintains as much as a 2.5x speedup when including I/O overhead.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

There are many promising directions for future work to extend the functionality and versatility of the GRiD library. We have current work under development to expand GRiD to support the full breadth of rigid body dynamics algorithms and robot models supported by current state-of-the-art CPU spatial-algebra-based rigid body dynamics libraries. Additionally, we are developing wrappers to our C++ host functions in higher level languages to make it even easier to leverage GRiD.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

We would like to explore emerging rigid body dynamics algorithms and alternate formulations and implementations of rigid body dynamics, which may improve overall performance by exposing additional parallelism and computational efficiency.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

We would also like to add support for differentiating through model parameters, as well as for contact, and hope to integrate these accelerated dynamics implementations into existing robotics software frameworks. This would increase both GRiD's ease-of-use and applicability to more robotics researchers.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

Finally, building out increased support for more trajectory optimization, MPC, and ML algorithms running entirely on the GPU would further increase the performance benefits from integrating GRiD into these approaches.
