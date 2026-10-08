<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

GLASS: Architecture-Tuned, Composable, Device-Side Linear Algebra for Edge Robotics and Beyond

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

GPU robotics lacks the reusable numerical infrastructure of mature CPU stacks, instead relying on compiler frameworks that introduce overhead or repeatedly reimplementing numerical libraries. To address this, we introduce GLASS (GPU Linear Algebra Simple Subroutines), a header-only CUDA C++ library that provides thread-, warp-, block-, and NVIDIA-backed implementations of robotics-scale linear algebra and geometric computations under one composable device API. GLASS treats implementation choice, execution scope, and launch packing as architecture-specific placement decisions determined by offline measurement and resolved statically at compile time. This is critical as the best and worst placements differ by a median of 4.9x (max 81x), with 145 of 396 recommended placements changing between a Jetson AGX Orin and an RTX 5090, and 162 of 396 versus an AGX Xavier. These stakes are highest at the edge as GLASS's advantage over the best of PyTorch and JAX is as much as 73x on the Orin versus 12x on the RTX 5090. GLASS is released open source with independent numerical oracles and source-bound local-GPU test attestation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finally, integrating GLASS with published robotics systems both exposed a pre-existing numerical bug and improved embedded runtimes by up to 1.5x.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robotics computation is rapidly moving to the GPU, from perception, mapping, localization, and learning to simulation, dynamics, planning, and control. Unfortunately, unlike on the CPU, where robotics applications achieve high performance through the use of libraries that concentrate software optimization, validation, and maintenance into reusable shared infrastructure (e.g., Eigen and BLASFEO for linear algebra, Pinocchio and GTSAM for geometric, kinematic, dynamic, and factor-graph kernels ), GPU edge robotics lacks such a comparable layer.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This persists because the small, structured operations embedded inside larger robotics kernels still require choosing how computation should map onto GPU threads, warps, and blocks, and whether vendor-backed routines are applicable. As such, it is unclear whether to leverage high-level compiler frameworks like JAX and PyTorch, use NVIDIA host libraries such as cuBLAS and cuSOLVER, integrate device-callable functionality through CUB, CUTLASS, cuBLASDx, and cuSOLVERDx, or repeatedly build and tune bespoke low-level code. As shown in prior work, and confirmed in this work, no one of these choices is universally best. As such, robotics systems still rely on a mix of all of these methods, incurring overheads and creating duplicate low-level code.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unfortunately, the cost of this duplication is growing as AI coding tools make new implementations much cheaper to produce but not cheaper to validate or maintain. This is particularly problematic for GPU code, which is prone to subtle errors, and for which continuous testing is often too expensive. Thus, a shared GPU numerical software layer could help amortize optimization, validation, and maintenance across human- and agent-written software.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

As such, we introduce GLASS (GPU Linear Algebra Simple Subroutines), an open source, header-only CUDA C++ library of composable device-side primitives for robotics-scale linear algebra and geometric computation. GLASS unifies, under one API, thread-, warp-, and block-scoped implementations alongside NVIDIA device library wrappers. GLASS uses offline measurement to determine architecture-specific dispatch and launch placements, resolved statically at compile time. This is critical as the best and worst placements differ by a median of 4.9$\times$ (max 81$\times$), with 145 of 396 recommended placements changing between a Jetson AGX Orin and an RTX 5090, and 162 of 396 versus an AGX Xavier. These stakes are highest at the edge as GLASS's advantage over the best of PyTorch and JAX is as much as 73$\times$ on the Orin versus 12$\times$ on the RTX 5090.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In short, GLASS transforms the numerical layer edge GPU robotics repeatedly rebuilds, or incurs overheads, into tuned and tested infrastructure. Our contributions are: Composable GPU numerical infrastructure. GLASS provides one device-side API spanning thread-, warp-, block-, and NVIDIA-backed implementations of dense and structured linear algebra and robotics geometry.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Measured execution placement. GLASS treats implementation choice, execution scope, and launch packing as offline-measured, architecture-specific optimization decisions, leading to both speedups and changing recommendations between hardware targets.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robotics-aware composition. Composable primitives keep intermediates on device and enable domain-specific fusion, itself a measured placement choice, providing as much as 1.75--2.9$\times$ speedups.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Validated reuse in robotic systems. GLASS provides independent oracles and source-bound GPU test attestation. Integrating GLASS with published robotics systems exposed a pre-existing numerical bug and improved embedded runtimes by up to 1.5$\times$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We release GLASS open source to benefit the wider community: github.com/A2R-Lab/GLASS

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A CPU and GPU Numerical Libraries", "weight": 1.0} -->

Robotics has long benefited from shared numerical infrastructure on the CPU. Eigen and BLASFEO provide general and small-problem linear algebra, while Pinocchio and GTSAM provide reusable geometric, dynamic, and estimation machinery. BLASFEO is particularly relevant because it treats the small-to-medium matrices of embedded optimization as a distinct performance regime. LIBXSMM similarly demonstrates substantial specialization headroom for small matrix multiplication. GLASS targets an analogous reusable numerical layer for *GPU-resident* robotics computation.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A CPU and GPU Numerical Libraries", "weight": 1.0} -->

The GPU ecosystem already provides strong numerical libraries at several abstraction levels (Table I). Host-dispatched cuBLAS/cuSOLVER, MAGMA, and KBLAS provide optimized dense and batched linear algebra. Ginkgo similarly fuses complete batched iterative and structured solvers into GPU kernels. At a higher level, JAX and PyTorch expose compiled, differentiable batched linear algebra, but their operations remain host-dispatched behind framework and kernel-launch boundaries and so cannot be embedded inside application kernels. More recent NVIDIA libraries move more of this computation inside user kernels. MathDx provides device-callable numerical routines, CUB provides warp- and block-level collectives, and CUTLASS provides hierarchical matrix kernels with profiler-supported tuning. Kokkos Kernels provides composable serial, team, and team-vector batched routines across architectures, while Eigen can execute a subset of its operations serially in CUDA threads.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A CPU and GPU Numerical Libraries", "weight": 1.0} -->

GLASS does not seek to replace such device libraries, but rather integrates them as candidate backends alongside native implementations under a single API that can be automatically tuned per target architecture to jointly optimize execution scope and launch packing, saving the optimal setup as a reusable configuration.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Performance Portability and Validation", "weight": 1.0} -->

Numerical software has long used measurement to adapt implementations to a target machine. ATLAS benchmarks alternative kernels at installation time, FFTW measures candidate execution plans, and OSKI selects sparse-kernel implementations from offline measurements. A different approach is to generate or search for specialized code, as in Halide, TVM/Ansor, Triton, and Exo. GLASS follows the measurement-based approach, applying it to execution placement inside GPU kernels.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Performance Portability and Validation", "weight": 1.0} -->

Reusable numerical infrastructure must also preserve correctness across these implementations. GPUVerify targets synchronization and race errors, while recent work on generated GPU kernels shows that apparent performance can depend strongly on the correctness oracle used for validation. GLASS therefore pairs its implementations with independent numerical oracles. Its engineering workflow can also carry source-bound, low-cost, local-GPU test results into CPU-only Continuous Integration (CI). thread/warp/block thread/warp/block TABLE I: Representative GPU numerical libraries and the capabilities. Parentheses denote partial support (e.g., a subset of functions, profiler- or heuristic-guided choices).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Design", "weight": 1.0} -->

GLASS (Fig. 1) is a header-only CUDA C++ library of composable device-side primitives for robotics-scale linear algebra and geometric computation designed for the small- to medium-sized batched computations common in robotics. Application kernels call these primitives directly, allowing numerical operations to remain inside the surrounding GPU computation and avoiding additional host calls, kernel launches, or data marshalling. measure once, dispatch statically, independently verified target GPU → implementation and launch placement tables in-kernel calls;on-chip intermediatesimplementation +launch placements Fig. 1: GLASS at a glance. Application kernels call one device-side API spanning thread-, warp-, block-, and NVIDIA-backed implementations. Offline measurement produces architecture-specific compile-time dispatch and launch placements. Independent numerical tests validate every implementation separately from performance measurement.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Programming Model and Execution Interfaces", "weight": 1.0} -->

In the canonical interface, one CUDA block owns one independent numerical problem and its threads cooperate over that problem, with alternative interfaces also available. In particular, glass::block:: uses dependency-free cooperative SIMT, glass::warp:: assigns one problem to a warp, and glass::thread:: assigns one problem to a thread. GLASS also exposes optional NVIDIA-backed implementations through glass::nvidia::\*::, where \* is block, warp, or thread. These interfaces wrap CUB collectives, cuBLASDx matrix operations, and cuSOLVERDx factorizations and solves where available. Importantly, all of these interfaces share the same mathematical conventions and data layouts while making execution scope and optional dependencies explicit.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Programming Model and Execution Interfaces", "weight": 1.0} -->

Choosing among these implementations is architecture and application dependent and would quickly become a challenge for users. GLASS therefore ships with autotuning tools that benchmark the library's performance offline on a target GPU and store the resulting choices in architecture-specific tables. The selected implementation body is then folded through an architecture-specific constexpr table at compile time, avoiding host dispatch and runtime overheads.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Programming Model and Execution Interfaces", "weight": 1.0} -->

GLASS provides two ways to use these measurements. A bare call such as glass::posv keeps the standard block-level calling contract but automatically selects the best compatible implementation body from the measured table. Changing from one problem per block to one per warp or thread also changes application launch geometry and indexing, so GLASS cannot make that transformation implicitly. Thus, we also provide a compile-time advisor that reports the recommended execution scope and launch packing, allowing the application to adopt the measured mapping when desired. For example, on the Orin, for fp32 POSV, the glass::recommend API places glass::thread:: at $N{=}8$ but glass::nvidia::block:: at $N{=}32$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Programming Model and Execution Interfaces", "weight": 1.0} -->

Finally, GLASS deliberately targets numerical problems small enough to be owned by one CUDA block. Such problems are common in edge robotic applications, and this is the regime in which embedding a routine inside an application kernel avoids costly overheads. Larger cross-block dense problems are generally better served by conventional host-dispatched libraries. Within the targeted regime, each implementation is instantiated only where its compile-time size and resource requirements are feasible.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Numerical and Robotics Primitives", "weight": 1.0} -->

GLASS's linear algebra surface covers much of the BLAS and LAPACK functionality needed by robotics applications, including reductions, BLAS L1--L3 operations, triangular and symmetric updates, factorizations, and linear solves. GLASS also includes structured routines such as block-tridiagonal matrix-vector products and direct and iterative solvers commonly used in trajectory optimization. On top of this general numerical layer, GLASS adds operations that recur throughout robotics software. These include spatial algebra, SO, SE, and quaternion maps and Jacobians, pose errors and retractions, projections, and related geometric and optimization primitives. Sharing these implementations is useful for correctness as well as performance because robotics libraries often differ in twist ordering, quaternion layout, perturbation conventions, and small-angle behavior. GLASS fixes these conventions as part of each operation's interface and tests them against independent references or defining identities.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Numerical and Robotics Primitives", "weight": 1.0} -->

Because these primitives share an in-kernel interface, they can also be composed without introducing new kernel boundaries. Higher-level operations can therefore reuse the same library calls while retaining intermediate data on chip, providing performance gains. For example, the LQR feedback gain, $K=(R+B^{\top}PB)^{-1}B^{\top}PA$, can be assembled from general matrix and solve primitives or optimized with a fused riccati_gain implementation (Sec. IV-E). As such, we include a number of fused operations in GLASS.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Validation and Continuous Testing", "weight": 1.0} -->

Because GLASS may select different implementations across execution scopes and GPU architectures, numerical correctness must hold independently of the chosen implementation. We therefore validate conventional linear algebra against independent NumPy and SciPy references, and robotics operations against Pinocchio where applicable. Operations without a direct reference are checked using defining identities, factorization residuals, algebraic equivalences, or finite-difference derivatives. Tests also cover numerical scale, conditioning, layouts, and execution scopes where these form part of the documented contract.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C Validation and Continuous Testing", "weight": 1.0} -->

Continuous testing of this library presents a practical problem because GPU runners in hosted CI are comparatively expensive. We therefore developed a lightweight pytest plugin that runs GPU tests on available local hardware, records the exact source tree and test outcomes, and signs this evidence for later verification in CPU-only CI. Subsequent CI runs can reject stale or source-mismatched results without rerunning the GPU test suite. We note that these receipts are engineering attestations by their signers, not proof that a claimed GPU executed the tests. However, we include mechanisms to reduce the viable signer list to a trusted subset of developers, e.g., for major releases, to provide higher levels of confidence in the testing regime. We release this testing tool open source alongside GLASS:\github.com/A2R-Lab/pytest-gpu-proof\and via: pip install pytest-gpu-proof.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Fig. 2: Measured fp32 kernel timings on the Jetson AGX Orin at B = 8192. Each panel reports per-problem time as problem size varies. Native GLASS Thread, Warp, and Block implementations are measured alongside NVIDIA device paths where supported. Sampled problem sizes are spaced uniformly to expose the small-N regime. Crossings show why no single execution scope provides the best implementation and why placement matters.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Five key questions anchor our evaluation. First, what does GLASS provide beyond existing device-side numerical libraries? Second, how strongly do placements depend on GPU architecture? Third, how does this execution model compare with conventional host-batched libraries and compiler frameworks? Fourth, do the same choices benefit robotics-specific operations and compositions? Finally, does replacing bespoke code with GLASS improve real robotics software?

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A Methodology", "weight": 1.0} -->

Our evaluation spans the regimes exposed by GPU robotics. GPU simulation and sampling-based methods can evaluate batches containing hundreds to thousands of numerical problems, trajectory optimization commonly exposes batch sizes in the tens to hundreds, and high-rate control also makes the batch-one latency regime important. We thus evaluate batch sizes from $B=1$ to $B=8192$ and problem sizes from $N=4$ to $N=128$, ensuring that we span robotics-scale, low-latency single-problem execution, through heavily batched GPU workloads.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A Methodology", "weight": 1.0} -->

We use the embedded Jetson AGX Orin (sm_87, CUDA 13.2) as our primary test platform. A Jetson AGX Xavier (sm_72, CUDA 11.4) provides an older-generation edge comparison, and a desktop RTX 5090 (sm_120, CUDA 13.2) provides a high-performance ablation that tests whether the same measured-placement design scales up. Benchmarks preheat the GPU, use repeated measurements, and validate implementations independently from timing.^11^ 1 Placement benchmarks measure wall-clock time around back-to-back asynchronous launches followed by one synchronization, while case-study A/B experiments use CUDA events. Throughput comparisons exclude host API overhead, favoring the host-dispatched baselines, while synchronized batch-one measurements separately capture call latency.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Methodology", "weight": 1.0} -->

Placement sweeps cover six operations, eleven problem sizes, three batch regimes, and two scalar types (fp32, fp64), for 396 cells per architecture. Host comparisons cover GEMM, POTRF, and POSV over nine sizes, seven batch sizes, and both scalar types, for 378 cells, and use only GLASS's dependency-free native tiers as candidates.^22^ 2 Destructive POTRF, TRSV, and POSV benchmarks give every supported native and NVIDIA execution plan a fresh valid input per launch, randomize plan order within paired rounds, and retain all raw samples. We note that due to structural limitations, the NVIDIA backend supports only 357 of 396 (195 of 198 fp32) cells on the Orin, 354 (192 fp32) on the RTX 5090, and 0 on the Xavier.^33^ 3 Its CUDA 11.4 toolchain predates the device-callable MathDx libraries, requiring it to always fall back to native GLASS implementations. We call these the *comparable* cells.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A Methodology", "weight": 1.0} -->

Finally, NVIDIA placements are chosen when they are $>5$% faster, the *dispatch margin*, to account for measurement noise.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-B Performance Against Device-Side Libraries", "weight": 1.0} -->

As GLASS is designed to execute inside application GPU kernels, its closest comparisons are other device-side numerical implementations. Figure 2 shows the placement measurement sweep for $B=8192$ for fp32 operations on the Jetson AGX Orin. The crossing curves expose the value of retaining several execution scopes rather than standardizing on one implementation family, with the best and worst placements differing by a median of 4.9$\times$ and up to 81$\times$. In particular, native GLASS wins 99 of the 195 comparable fp32 cells (51%), most often for dot, GEMV, GEMM, and triangular solves. These wins have a geometric mean of $2.1\times$, with 39 exceeding $2\times$, and reaching $22.1\times$ in the extreme case where thread-packed execution replaces a block-wide reduction at tiny $N$. NVIDIA implementations are selected or lie within the dispatch margin in 96 of 195 comparable cells (49%), dominated by factorization operations.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B Performance Against Device-Side Libraries", "weight": 1.0} -->

On the workstation RTX 5090 the NVIDIA-backed share rises to 64% with a maximum native win of $3.9\times$ on its 192 comparable cells.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B Performance Against Device-Side Libraries", "weight": 1.0} -->

Fig. 3: Other device-side comparisons over limited matched supported operations on the Jetson AGX Orin, confirming GLASS’s advantage due to its broader set of execution placements and numerical primitives.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B Performance Against Device-Side Libraries", "weight": 1.0} -->

Other device-side library baselines reinforce this result (Figure 3). As Eigen can only be embedded into individual threads, we compare it to glass::thread:: and find that GLASS wins 36 of 126 cells, Eigen wins 26, the remaining 64 tie, and the median runtime ratio is 1.00$\times$. Kokkos Kernels provides a broader composable comparison spanning serial and cooperative execution. Here, GLASS wins 119 of 162 cells, Kokkos wins 7, and the other 36 tie.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B Performance Against Device-Side Libraries", "weight": 1.0} -->

Taken together, these benchmarks show that GLASS's advantage comes from its broader set of placements and primitives, and this advantage is most important for deployable robotics-scale edge devices.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B Performance Against Device-Side Libraries", "weight": 1.0} -->

Fig. 4: Recommended fp32 placements across operation, problem size, and batch size on the RTX 5090, Jetson AGX Orin, and Jetson AGX Xavier. Colors denote native Thread, Warp, and Block execution and NVIDIA-backed implementations. Black outlines mark recommendations that differ from the Orin’s (center row, shaded). For the Xavier much of this divergence is structural as it cannot support the evaluated NVIDIA device libraries.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Performance Against Device-Side Libraries", "weight": 1.0} -->

Finally, we note that the NVIDIA warp tier is omitted from Figure 2, and the remaining experiments, as the NVIDIA warp backend is only exposed via CUB reductions, and those fall within the dispatch margin in 121 of 126 cells (96%).

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-C Architecture Adaptation", "weight": 1.0} -->

The preceding results show that execution placement matters on one GPU. We next ask whether the same choices transfer across architectures and whether architectural changes impact placement decisions. Figure 4 shows that the qualitative trends presented in Section IV-B persist, but their boundaries move substantially. Threads remain particularly effective for many small factorizations and solves, while warp, block, and NVIDIA-backed implementations take over in different regions as problem size and batch size change, reinforcing the importance of a flexible, portable, and architecture-tuned numerical library.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-C Architecture Adaptation", "weight": 1.0} -->

In particular, we find that the Orin's placements differ from the RTX 5090 in 145/396 cells and from the older-generation Xavier in 162/396. As the Xavier cannot support the NVIDIA backend, we also restricted all three GPUs to their common native GLASS backend candidates and find that 107/396 RTX--Orin, 94/396 RTX--Xavier, and 66/396 Orin--Xavier placements still change.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-C Architecture Adaptation", "weight": 1.0} -->

These differences are important for performance. Figure 5 transfers native GLASS placements between architectures. We find that cross-architecture reuse adds 4--20% geometric-mean runtime depending on direction, with 95th-percentile penalties reaching 2.59$\times$. This is particularly costly when transferring between hardware classes as transfers between the two Jetsons cost only 4--5%, while carrying a Jetson policy onto the RTX 5090 costs 20% on average. We note that here, portability means retaining the same numerical interface while retuning placement across NVIDIA GPUs. Cross-vendor source portability is left for future work.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-C Architecture Adaptation", "weight": 1.0} -->

Fig. 5: Penalty from transferring native placements and launch configurations between GPU architectures across the 396 measured cells. Rows are source hardware and columns are target hardware. Each off-diagonal entry reports geometric-mean and 95th-percentile slowdown relative to the locally tuned target plan. One Orin placement (16 warp-packed fp64 GEMM problems per block) exceeds the RTX 5090’s per-block shared memory and cannot be transferred.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C Architecture Adaptation", "weight": 1.0} -->

Fig. 6: Host-batched baseline time divided by the best measured valid native GLASS time for fp32 GEMM, POTRF, and POSV on the Jetson AGX Orin against cuBLAS/cuSOLVER (top) and the per-cell best of PyTorch and JAX batched linear algebra with device-resident inputs and outputs and pre-compiled and jitted code (bottom). Values above one favor GLASS and are clipped to 16× for visual clarity (true maximum value is 113.9×), exposing both the small-matrix region where device-side execution wins and the larger regimes where host batching can regain some advantage, and exposing the benefit of a flexible, portable, and adaptable placement framework.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-C Architecture Adaptation", "weight": 1.0} -->

For edge deployments, the power mode is also a key consideration. Reducing the Jetson Orin from 50 W to 30 W and 15 W increases geometric-mean runtime by 29% and 91%, respectively, yet changes only 9 of 396 placement decisions in each mode (with 5--6 of those sitting inside the dispatch margin). Power limits therefore primarily scale the candidates together, whereas switching architectures changes their relative ordering. The same placement table can consequently be reused across power modes without retuning, even though reducing the power ceiling substantially reduces absolute throughput.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-C Architecture Adaptation", "weight": 1.0} -->

Finally, generating a placement table is a one-time, offline operation for each architecture and toolchain configuration. Our complete tuning sweeps required 5.5 hours on the Orin, 9 hours on the Xavier, and 2 hours on the RTX 5090.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-D Performance Against Host-Batched Libraries and Compiler Frameworks", "weight": 1.0} -->

We next compare device-side GLASS execution with conventional host-dispatched numerical libraries and compiler frameworks to demonstrate the overheads associated with such popular approaches. Figure 6 compares the best measured fp32 native GLASS implementation with the best cuBLAS/cuSOLVER or PyTorch/JAX implementation while varying problem size and batch size.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-D Performance Against Host-Batched Libraries and Compiler Frameworks", "weight": 1.0} -->

Both baseline families pay per-call dispatch overhead that device-side execution eliminates, and both pay it most heavily in the small-matrix regime GLASS targets. On the Orin, GLASS beats host-dispatched cuBLAS/cuSOLVER at every measured batch size for POSV through $N=64$ (up to 113.9$\times$), GEMM through $N=48$ (up to 12.1$\times$), and POTRF through $N=24$ (up to 12.8$\times$). Compared to the per-cell best of PyTorch and JAX, optimized with both device-resident inputs and outputs and pre-compiled and jitted code, GLASS is faster in 359 of 378 cells with per-operation geometric means of 4.3--9.5$\times$ and individual dispatch-bound cells reaching 73$\times$. That being said, the wins are not uniform, and host cuSOLVER retakes portions of standalone Cholesky at larger $N$, while PyTorch/JAX wins for the largest combination of $N$ and $B$ for GEMM.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-D Performance Against Host-Batched Libraries and Compiler Frameworks", "weight": 1.0} -->

As with the device-side results, ablations show large wins for GLASS on the older Xavier (up to 89.3$\times$ against cuBLAS/cuSOLVER) and smaller wins on the RTX 5090 workstation (GLASS leads the frameworks in 320 of 378 cells at geometric means of 1.5--2.6$\times$, up to 12$\times$). And, unsurprisingly, workstation-only baselines like MAGMA perform best on the workstation, but remain out of reach for embedded deployments, reinforcing our core thesis that flexible dispatch wins.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-E Robotics Operations and Composition", "weight": 1.0} -->

This placement effect extends to robotics-specific operations and compositions. Table II evaluates representative pose, spatial-algebra, small-spectral, and reduction primitives from the robotics-specific portion of GLASS. On the Orin, the best fine-grained placement improves throughput by 3.5--9.7$\times$ over whole-block execution across these operations, and the same protocol on the RTX 5090 spans 1.7--5.0$\times$. Thread execution wins most cases, while the reduction-heavy fp32 softmax instead favors a warp. motion_cross_mul TABLE II: Execution placement for representative robotics operations. ns/problem for fp32 on the Jetson AGX Orin at B = 4, 096.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-E Robotics Operations and Composition", "weight": 1.0} -->

Composability also makes composition granularity itself a measurable placement choice. Figure 7 evaluates an LQR feedback gain $K=(R+B^{\top}PB)^{-1}B^{\top}PA$ expressed two ways from the same GLASS primitives: a fused riccati_gain kernel that retains every intermediate on chip, and an unfused composition that launches each primitive as its own kernel. Both dominate the equivalent seven-call host-dispatched vendor chain, consistent with Sec. IV-D, but, as with our prior placement evaluations, the measured winner between them flips with the deployment regime. Through $B=64$ the fused kernel is up to 1.75$\times$ faster, while at larger batches, and for the register-heavier fp64 shapes almost everywhere, the unfused composition wins by up to 2.9$\times$. While possibly surprising at first, this is because independent per-primitive kernels can occupy the GPU more fully than the fused kernel's shared-memory footprint allows. Composition granularity is thus another architecture- and regime-specific placement decision GLASS can optimize.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-F Case Studies in Published Robotics Systems", "weight": 1.0} -->

We finally integrate GLASS into two existing open-source robotics systems. Across both, replacing bespoke numerical code preserves or improves performance while reducing application-specific implementation burden, and in one case it also exposes a pre-existing numerical bug.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-F Case Studies in Published Robotics Systems", "weight": 1.0} -->

In a CUDA implementation of sampling-based MPC, we replace application-specific reductions with GLASS, while preserving the surrounding algorithm and public interface. This change makes a pre-existing failing host-versus-device normalization test pass. An independent double-precision reference shows that the original reduction can return a non-minimal baseline. Our repair for this error has since been accepted upstream. Relative to the corrected baseline, using GLASS provides 1.21--1.50$\times$ speedups across 128--8192 rollouts on the Orin (1.21--1.46$\times$ on the RTX 5090). Thus, reuse replaces an assumption-sensitive reduction with independently tested primitives while also improving performance.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-F Case Studies in Published Robotics Systems", "weight": 1.0} -->

In a batched inverse-kinematics solver, integrating GLASS reduces approximately 355 lines of specialized device numerics to 29 lines of application code, a 92% reduction. For example, a 201-line warp Cholesky implementation becomes glass::warp::posv, while custom reductions, argmin logic, and geometric operations become library calls. In an interleaved A/B comparison at batch size 2,000, GLASS adoption reduces Orin runtime from 9.94 ms to 7.92 ms, a 1.26$\times$ speedup, while the corresponding RTX 5090 improvement is only 1.02$\times$. This is yet another example of why GLASS is useful for edge robotics.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

GPU robotics repeatedly embeds small, structured numerical operations inside larger kernels, where the best execution strategy depends on the operation, problem size, batch size, and GPU architecture. We introduced GLASS, an open source, header-only CUDA C++ library that unifies, under one composable API, thread-, warp-, and block-scoped implementations with NVIDIA device routines, using offline measurement to select among them. Our evaluation shows that across three GPU architectures, no implementation family dominates, and transferring placements between architectures adds 4--20% geometric-mean runtime. Downstream integrations further show that shared implementations can resolve latent correctness errors while improving embedded runtimes by up to 1.5x. These results suggest that execution placement should be treated as part of the reusable numerical interface for GPU robotics, rather than repeatedly chosen inside each application. We release GLASS open source together with its tests, tuning and continuous integration tools, documentation, and coding-agent guidance.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

Future work includes provably correct reduced- and mixed-precision numerical support, building on recent tooling infrastructure, broader factorization support, community-contributed architecture tables, and support for non-NVIDIA accelerators. Finally, although motivated by edge robotics, the same design applies wherever small, structured numerical operations are embedded inside larger GPU kernels, and we look forward to supporting other domains.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

Fig. 7: Runtime ratio of the unfused GLASS Riccati composition (one kernel per primitive, intermediates in global memory) to the fused riccati_gain kernel (intermediates in shared memory) on the Jetson AGX Orin. Above one favors fusion. Color identifies the problem size, (nx, nu). Solid curves are fp32, and dashed fp64.
