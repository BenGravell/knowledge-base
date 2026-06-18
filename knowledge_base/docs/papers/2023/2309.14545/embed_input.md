<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Motions in Microseconds via Vectorized Sampling-Based Planning

Topics include Motion planning, Robotics, Sampling-based methods, Planning, Control, Sampling.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Modern sampling-based motion planning algorithms typically take between hundreds of milliseconds to dozens of seconds to find collision-free motions for high degree-of-freedom problems. This paper presents performance improvements of more than 500x over the state-of-the-art, bringing planning times into the range of microseconds and solution rates into the range of kilohertz, without specialized hardware. Our key insight is how to exploit fine-grained parallelism within sampling-based planners, providing generality-preserving algorithmic improvements to any such planner and significantly accelerating critical subroutines, such as forward kinematics and collision checking. We demonstrate our approach over a diverse set of challenging, realistic problems for complex robots ranging from 7 to 14 degrees-of-freedom. Moreover, we show that our approach does not require high-power hardware by also evaluating on a low-power single-board computer. The planning speeds demonstrated are fast enough to reside in the range of control frequencies and open up new avenues of motion planning research.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

High degree-of-freedom (d o f) robots rely on *motion planning* to move in complex workspaces, either using sampling-based approximations or numerical optimization. These planners are general and can solve realistic, challenging problems in hundreds of milliseconds to dozens of seconds on consumer cpus. However, this level of performance falls short---it is too slow for reactive operation in evolving environments and hampers algorithms for higher-level autonomy such as integrated task and motion planning.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A large literature accelerates motion planning with *coarse-grained* (*e.g.*, thread or process-level) parallelism, but these methods have seen relatively little uptake in practice, as their performance gains do not justify the added complexity. More recent work uses gpu-based parallelism to improve performance, but at the cost of communication overhead, algorithmic limitations, and the additional expense and power consumption of gpu hardware. In general, the field has come to believe that sampling-based motion planner (sbmp) primitives (*e.g.*, checking if motion between two states is valid) are either inherently serial, cannot be accelerated without specialized hardware, or cannot be parallelized without paying a greater cost than the parallelism saves.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We refute this belief and show several orders of magnitude performance improvement over the state-of-the-art (more than 500x faster) by contributing insights into *fine-grained* parallelism and work-ordering in sbmps. Our core insight is the use of *vector-oriented* state representations and planning primitives (*e.g.*, forward kinematics and collision checking), which enable fine interleaving of parallel and serial operation. Crucially, we use "Single Instruction/Multiple Data" (simd) instructions to execute these primitives with high throughput and low latency on ubiquitous consumer cpus, accelerating *almost any* sbmp for ?free?. These insights let us plan high-quality paths at reactive speeds (*e.g.*, a median time of $40\ {µs}$ for the 7 d o f Panda over the MotionBenchMaker dataset, *i.e.*, $25\ {kHz}$---see Table I) on a single cpu core.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our method significantly outperforms standard implementations of state-of-the-art sbmps on both desktop and low-power single board computers. Moreover, this work will enhance any work that uses motion planning, and our perspective on vector-oriented planning primitives extends beyond cpu simd instructions to other, similar parallelism models, *e.g.*, gpus. The planning speeds demonstrated blur the line between planning and control, and give cause to re-evaluate assumptions about robot motion.

<!-- chunk {"id": "body-0007", "role": "body", "section": "II-A Parallelism in Motion Planning", "weight": 1.0} -->

Parallelized planners have been sought since the advent of motion planning (*e.g.*, ). We broadly categorize parallelism in motion planning as either *coarse-grained* or *fine-grained*. In our use, coarse-grained refers to parallelism at the level of subroutines or planner components, such as running many planners in parallel, or running cc in a separate thread. Fine-grained refers to parallelism at the level of primitive operations, such as checking several states for collisions simultaneously in the same thread, without architectural changes.

<!-- chunk {"id": "body-0008", "role": "body", "section": "II-A Parallelism in Motion Planning", "weight": 1.0} -->

Parallelism in sbmp is typically coarse-grained, *e.g.*, simply running independent planners in parallel. This improves average-case performance; the set of solutions can also be hybridized together to improve plan quality. Early work (*e.g.*, ) observed that roadmap-based planners (*e.g.*, prm ) are amenable to coarse-grained parallelism. Parallel sbmp has also been achieved by constructing a forest of planning trees, potentially in distinct regions of the search space, and by parallelizing components of the rrt$^{*}$ asao planner. These methods typically offer sub-linear (in the degree of parallelism) performance improvement (with some exceptions ) due to the synchronization overhead and architectural complexity required. Still other work uses coarse-grained parallelism in graph search used in roadmap- or search-based planning, both on cpus and gpus. In contrast to the work discussed above, this work investigates a novel approach to *fine-grained* parallelism in sbmps, which is understudied in the field.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-A Parallelism in Motion Planning", "weight": 1.0} -->

Recently, there has been significant interest in applying gpus more broadly to motion planning. The most successful approaches include parallelized sampling-based mpc, parallel particle-based optimization seeded by a partially parallelized rrt-like planner, and end-to-end learning of a neural local control policy from a dataset of motion plans. Earlier work also investigated gpu-parallelized cc. Although these methods show promising performance, they require powerful gpus for efficiency and impose the overhead of moving data between the gpu and cpu.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-B Hardware-Accelerated Motion Planning", "weight": 1.0} -->

Hardware acceleration is crucial for our proposed vector-based approach to sbmp. We use simd instructions, a feature ubiquitous on consumer cpus ^11^1Our primary implementation uses avx$2$, which has been broadly available on Intel and AMD cpus since 2013. Lower-width simd instruction sets such as sse have been available since 1999.. Hardware acceleration has long been used for motion planning, with particular focus on accelerating cc. Some work (*e.g.*, 's compile-time specialized sbmp, or 's statically dispatched, precompiled dynamics algorithms) implicitly exploits hardware acceleration by creating ?machine sympathetic? implementations---code that enables compilers, etc. to better exploit hardware capabilities.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-B Hardware-Accelerated Motion Planning", "weight": 1.0} -->

Many modern robotics algorithms are accelerated by gpus, *e.g.*, using cuda. gpu acceleration has been applied to sbmps, mpc and trajectory optimization. Recently, asic- or fpga-based accelerators have been proposed, *e.g.*, to validate an entire roadmap at once with an fpga or as an external cc accelerator. investigated "robomorphic" computing with specialized accelerators for common robotics algorithms.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Hardware-Accelerated Motion Planning", "weight": 1.0} -->

However, gpus and other accelerators come at a cost: there is latency in communicating with the device, there are restrictions on the types of algorithms that can be applied on specialized hardware, and often there is a relatively high cost to send data back and forth. Our approach uses native simd instructions on the cpu, inflicting at worst a slight overhead penalty^22^2cpus may downclock when using simd instructions---there is also a cost to move data in and out of vector registers. to achieve large performance gains.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Method", "weight": 1.0} -->

Most sbmps can be decomposed into a handful of ?primitive? operations (see Ch. 7 in ). Algorithms typically use (approximate) nearest-neighbors (nn) to find nearby states, a state validity function (*e.g.*, checking for collisions), a local planner or steering function to grow edges between states, and an edge validity function to check these edges. Validity functions usually require forward kinematics (fk) to compute the poses of the robot's links in its workspace from a configuration.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Method", "weight": 1.0} -->

We lift a selection of these primitives---fk and state/edge validity checking---to operate over *vectors* of states in parallel. This lifting immediately accelerates the primitive operations by multiplying their throughput. More importantly, shifting perspective to vector primitives admits low-overhead parallelism that cooperates with sequential code, and reveals beneficial algorithmic changes to the primitives based on insights about their specific uses in sbmp. This perspective allows us to exploit ubiquitous hardware parallelism via simd instructions, resulting in highly efficient implementations of our vector primitives. Finally, by focusing on primitives common across sbmps, we improve the performance of *almost any* sbmp without requiring significant algorithmic changes.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Vectorized Motion Planning", "weight": 1.0} -->

?Vectorized? is an overloaded term; we use it in the simd sense, where a ?vector? is a fixed-length set of values with the same scalar datatype (*e.g.*, floating-point numbers) and a ?vectorized operation? is an operation that transforms all values in a vector independently, in parallel.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Vectorized Motion Planning", "weight": 1.0} -->

This parallelism model is similar to gpu computing (and our lifted vector operations may benefit gpu-based planners), but with a few key differences. We focus on cpu-based simd parallelism---our algorithms run on any modern computer, even those without a gpu. This increases applicability and decreases both the barrier to entry and the power consumption of our technique. cpu-based simd parallelism is also better-suited to the opportunities for parallelism in sbmp: it has significantly lower overhead than gpu-, thread-, or process-based parallelism^33^3While modern hardware is quite parallelism-performant, there is still non-negligible overhead (*e.g.*, gpu-cpu communication latency) in the tens of microseconds, which can easily add up into the milliseconds. and is amenable both to fine-grained interleaving of parallel and sequential code and to efficient computation for relatively small workloads.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Vectorized Motion Planning", "weight": 1.0} -->

Exploiting simd instructions requires careful consideration of data structure and algorithm design, often involving unconventional memory layouts to ensure adequate *data parallelism*. Our approach addresses this challenge through a novel Struct-of-Arrays (s o a) memory layout for fk and cc. This choice enables seamless exploitation of data parallelism, allowing us to pose and check multiple configurations for collision in parallel. The s o a layout stands in contrast to the more common Array-of-Structs (a o s) layout (illustrated in Fig. 1), which is less favorable for simd approaches as it causes memory access patterns that slow access to values.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Vectorized Motion Planning", "weight": 1.0} -->

Many sbmp algorithms and subroutines make heavy use of conditional branching, inimical to parallel code. However, as cpu-based simd parallelism allows easy interleaving of parallel and sequential code, and as our subroutines have reduced branching, we are able to sidestep this problem more easily compared to other forms of parallelism^44^4We also benefit from advances in modern hardware, which have produced branch predictors and fused ?test-and-branch? instructions that are highly performant on the limited set of branches we retain.. These properties mean that our algorithm implementations, despite being parallelized, are close to ?standard? algorithms---there is no explicit synchronization or communication code, etc.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Vectorized Motion Planning", "weight": 1.0} -->

[width=0.75]svg-inkscape/aos_soa_svg-tex.pdf_tex
Figure 1: Struct-of-Arrays (s o a) and Array-of-Structs (a o s) memory layout. Here, there are three configurations a, b, and c, each with four dimensions. a o s is the more “natural” layout of memory, but hard to exploit with simd.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Vectorized Motion Planning", "weight": 1.0} -->

The overhead of conventional mechanisms (*e.g.*, threads) limits naive parallelization of sbmp---reducing this overhead is especially challenging as most sbmp algorithms rapidly alternate between expensive, parallelization-friendly subroutines (*e.g.*, cc) and code that relies on these subroutines but is not itself easily parallelized (*e.g.*, graph search). Fortunately, the relatively low overhead of cpu simd-based parallelism---and the specific nature of this overhead, which modern compilers excel at reducing---means that our vector-oriented primitives (the expensive subroutines) can be efficiently interleaved within a sbmp. This property may suffice to accelerate sbmp, *e.g.*, reducing the cost of a single collision check. However, by using s o a memory layouts for our vector-oriented operations, we can not only perform the computation required for sbmp in parallel, but also exploit motion-planning-specific independence patterns in this computation to *intelligently order* the requisite operations to improve overall performance.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Vectorized Forward Kinematics", "weight": 1.0} -->

Vectorized fk is necessary to pose batches of states in parallel for subsequent parallel cc; sequentially posing each element in a batch introduces a bottleneck that reduces overall throughput. Naive vectorization of fk attempts to compute the poses for a *single* configuration faster---we instead choose a less conventional use of vectorization: carrying out each operation in sequence, but on *multiple configurations* simultaneously.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Vectorized Forward Kinematics", "weight": 1.0} -->

fk implementations commonly use dynamic branching and joint-type polymorphism to compute transforms between links (*e.g.* kdl ). This structure is difficult for compilers to optimize and has spurious data dependencies between link transforms, which decreases throughput and causes slower operations across the entire vector of configurations. These dependencies arise as the compiler cannot determine if poses later in the kinematic tree depend on earlier poses (or, better still, on components of these poses). Even naively vectorizing fk for multiple configurations requires vector configuration and pose data structures, and use of vector operations, which are tedious to manually implement.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Vectorized Forward Kinematics", "weight": 1.0} -->

We overcome these challenges with a novel *tracing compiler* for robot kinematics. This compiler takes in standard Universal Robot Description Format (urdf) files and *traces* the operations of arbitrary functions of the robot's kinematics (*e.g.*, fk). It uses this trace to automatically generate a vector configuration structure representing a batch of configurations and the minimal set of operations required to compute the traced function. This latter output constitutes an ?unrolled? fk loop that avoids branching and spurious data dependencies, allowing an optimizing compiler to generate faster machine code. Further, our tracing compiler applies optimizations to reduce the operations required, *e.g.*, constant folding, algebraic simplification, removing redundant negations, etc. This use of automatic code generation creates hyper-specialized vector-lifted fk without loss of generality, as the tracing compiler itself is general. We note other techniques for efficient fk, *e.g.* which uses static polymorphism and the Curiously Recurring Template Pattern (crtp) for compile-time optimized fk routines.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Vectorized Forward Kinematics", "weight": 1.0} -->

In contrast, our tracing compiler, by merit of tracking the precise operations (*e.g.*, the multiplies, sines, etc. from input configuration to output pose), outputs "straightline" code that removes operations that are not necessarily detectable at compile-time with crtp.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Vectorized Collision Checking", "weight": 1.0} -->

Existing approaches to cc (*e.g.*, broadphases, narrowphase triangle mesh collision algorithms ) are optimized for checking a single configuration. Fully vectorizing these approaches is challenging. We instead draw inspiration from classical work on simplified representations of robots and obstacles to automatically generate collision geometry from meshes using primitives (*i.e.*, spheres, cylinders, and cuboids). Sphere-based representations are common in the trajectory optimization literature.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C Vectorized Collision Checking", "weight": 1.0} -->

By representing the robot and environment as geometric primitives we can vectorize intersection tests between pairs of such primitives. We check batches of robot poses for self-collision and environment collision in parallel and reject the whole batch if any collide. Surprisingly, we see that this narrowphase-only approach (due to its reduced branching) can be highly efficient even in complex environments. Further, using spheres to represent the robot's geometry synergizes with our tracing compiler for fk---as we only compute the position of each sphere (rather than a full $SE{}$ pose), the compiler skips a large number of irrelevant operations.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-D Vectorized Motion Validation", "weight": 1.0} -->

[width=0.8]svg-inkscape/rake_svg-tex.pdf_tex
Figure 2: Illustration of the “raked” motion validator for a two-link mechanism. a) The rake consists of evenly spaced configurations (here, n = 4), which are “raked” backwards to achieve sufficient resolution. b) These configurations are computed in s o a form from an initial a o s layout, then checked in parallel. c) Spherical approximations of collision geometry are checked in parallel. A hierarchy of spheres is used to avoid unnecessary checks. d) When any collision is discovered at the lowest refinement level (in red), the entire check terminates (the last sphere in grey is skipped).

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-D Vectorized Motion Validation", "weight": 1.0} -->

sbmps validate not only individual states, but also the motions between them. Typically, motion validation requires discretizing a continuous motion and validating each state in the discretization. Thus, this is where sbmps spend most of their time, and a significant body of work has gone into reducing the number of edges validated during planning. However, here is where our perspective on vector-lifted primitives shines: by combining our previously developed insights into vectorized fk and individual state cc, we unearth further algorithmic insights to improve the performance of motion validation via vectorization.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-D Vectorized Motion Validation", "weight": 1.0} -->

For efficient motion validation, we want to stop checking invalid motions as quickly as possible. Assuming uniform probability of collision along a motion^55^5In reality *e.g.*, motion toward objects, this distribution is not uniform., $\frac{n}{2}$ cc attempts are wasted (in expectation) for an invalid motion discretized into $n$ states. Due to our perspective on vector-lifted fk and cc, we can reduce the amount of wasted computation by testing a *spatially distributed* set of states in parallel. Without loss of generality, consider a vector of eight states, and a motion discretized into $n$ states.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-D Vectorized Motion Validation", "weight": 1.0} -->

We can *simultaneously* check states $\lbrack 0,\frac{n}{8},\ldots,\frac{7n}{8}\rbrack$ for the cost of a single check^66^6This is a slight simplification; vector operations have low but nonzero overhead, and using them as we do may prevent auto-vectorization., and---if no collisions are found---comb through the remaining states by incrementing each index, for at most $\frac{n}{8}$ iterations. We refer to this spatially distributed collision check as the ?rake? (Fig. 2). Beyond improving cc throughput by decreasing the total number of checks required by a factor of the width of the vector, by spatially distributing the states checked, we increase the probability of exiting cc early for invalid motions---the validity of close states is correlated, so we have a higher chance of finding an invalid state by testing along the entire motion at once, compared to, *e.g.*, the first eight states at once.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-D Vectorized Motion Validation", "weight": 1.0} -->

Other work has investigated spatially distributed collision check scheduling in both hardware and non-parallel software.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-D Vectorized Motion Validation", "weight": 1.0} -->

Although the pure narrowphase approach is highly effective, we augment it with a ?mid-phase? check. Specifically: we employ a hierarchy of increasingly refined sphere collision models of the robot, and use coarse levels of this hierarchy to avoid expensive checks at the finer levels. We generate a sphere model for the robot with a single sphere per link, conservatively over-approximating the actual collision geometries. If this sphere does not collide with a given obstacle, we know that the actual collision geometry cannot collide with that obstacle, and can skip checking the spheres of the higher-fidelity model. Notably, this does not require the typical branching-heavy approaches to broadphase collision detection, *e.g.*, bounding volume hierarchies---our approach does not require or use the typical recursive tree structure or any update operations beyond fk.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-D Vectorized Motion Validation", "weight": 1.0} -->

For efficiency, it is preferable to not compute poses for any of a robot's links that come *after* a link in collision. We exploit a property of our tracing compiler, which can re-order instructions topologically, to *interleave* each sphere's collision check (environment and self-collision) within the generated fk code, placing checks immediately after the position of the sphere has been computed, wasting almost no effort on irrelevant fk computation and achieving a significant performance gain. This interleaving is compatible with the previously-described hierarchical sphere tree.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-E Bringing it Together: Design of the Planner", "weight": 1.0} -->

We also leverage simd instructions elsewhere to improve planner performance. Although not required in general, we assume the configuration space of the robot is Euclidean and thus linear interpolation between two a o s configurations becomes simply adding and multiplying their vectors together. Similarly, the $\ell_{2}$-norm is computed efficiently as a horizontal summation. We use these improvements to quickly compute the intermediate configurations used in the rake as well as distances in our nn data-structure.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-E Bringing it Together: Design of the Planner", "weight": 1.0} -->

We have implemented two sbmps: rrt-Connect and prm, without algorithmic changes or additional complexity due to our focus on planner primitives.We have also implemented simplification algorithms: randomized shortcutting and B-spline smoothing.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

[width=]svg-inkscape/panda_svg-tex.pdf_tex
Figure 3: Results for the 7 d o f Panda. a) Planning times for each problem class. b) Planning time vs. initial path length and c) planning and simplification time vs. simplified path length for entire dataset. d) Cumulative distribution of planning time and e) cumulative distribution of simplified path length for entire dataset. All times are on a logarithmic scale.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

[width=]svg-inkscape/fetch_svg-tex.pdf_tex
Figure 4: Results for the 8 d o f Fetch. a) Planning times for each problem class. b) Planning time vs. initial path length and c) planning and simplification time vs. simplified path length for entire dataset. d) Cumulative distribution of planning time and e) cumulative distribution of simplified path length for entire dataset. All times are on a logarithmic scale.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments", "weight": 1.0} -->

[width=]svg-inkscape/baxter_svg-tex.pdf_tex
Figure 5: Results for the 14 d o f Baxter over entire dataset. a) Planning time vs. initial path length. b) Planning time plus simplification time vs. simplified path length. d) Cumulative distribution of planning time and e) cumulative distribution of simplified path length. All times are on a logarithmic scale.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate our approach against two baselines which use the Open Motion Planning Library (ompl): MoveIt through Robowflex (MoveIt/ompl) and ompl's Python bindings with PyBullet (PyBullet/ompl). These represent two common interfaces of motion planning in practice: the standard motion planner for ros, and a Python implementation using a popular simulation framework. We evaluate our implementation, ?Vector Accelerated Motion Planning? on an x86-based desktop computer (VAMP) as well as a small arm-based single-board computer (VAMP (arm))^77^7For VAMP, avx$2$ was used. The authors attempted using avx-$512$, but found lower throughput than avx$2$, possibly due to downclocking, lack of 512-bit registers, or other issues that will be investigated in future work. For VAMP (arm), arm's Neon simd instructions were used.. All hyperparameters are shared between each implementation: all planners use equivalent implementations of algorithms with identical validity checking resolution. Moreover, we determinize all planners by sampling from a multi-dimensional Halton sequence.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiments", "weight": 1.0} -->

The same sequence is used between all systems. Thus, performance differences can be attributed to vector-acceleration^88^8MoveIt/ompl uses the $\ell_{1}$ metric for nearest neighbors rather than $\ell_{2}$..

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experiments", "weight": 1.0} -->

All benchmarks for MoveIt/ompl, PyBullet/ompl, and VAMP were performed with a amd Ryzen™ 9 7950X cpu clocked at 4.5GHz. For VAMP (arm), benchmarks were run on an Orange Pi 5B with an arm Cortex-A76 cpu clocked at 2.4GHz. Our approach is implemented in C++17 with Python bindings through nanobind. All code (including ompl and MoveIt) was compiled using clang 15.0.7 with the -Ofast optimization level^99^9Note that some of the issues with -ffast-math, *e.g.*, handling non-finite values, subnormals, etc., are not particularly relevant for the motion planning case, where configurations are from a compact, closed, and bounded space with relatively similar range in each dimension. However, we warn practitioners to still be wary of issues arising from reciprocal approximation. and with all architecture optimizations (-march=native, *i.e.*, znver4).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate on seven different environments from the MotionBenchMaker dataset, a collection of realistic, difficult motion planning problems: 1. *table pick*and *table under pick* environments to evaluate tabletop manipulation, 2. *bookshelf small*, *tall*, and *thin* to demonstrate reaching, and 3. *box*and *cage* to demonstrate highly constrained reaching. We use the publicly available pre-generated 100 problems for each of the environments. We evaluate on the following systems: 1. the 7 d o f Franka Emika Panda^1010^10We use the approximation of the Panda, 2. the 8 d o f Fetch Robotics Fetch, including the prismatic torso joint, and 3. the 14 d o f bimanual Rethink Robotics Baxter. For the Baxter, we use the *bookshelf tall {easy, medium, hard}* datasets for bimanual manipulation. For Fetch and Baxter, we use the algorithm of to automatically generate a spherized model (after ensuring manifold meshes )---these approximations were also manually tuned. We evaluate each planner on each problem 5 times.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experiments", "weight": 1.0} -->

For MoveIt/ompl and PyBullet/ompl, we give a timeout of 5 minutes. For VAMP and VAMP (arm), we give a limit of 1 million planner iterations.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experiments", "weight": 1.0} -->

Results for rrt-Connect on the Panda, Fetch, and Baxter are respectively shown in Figs. 3, 4 and 5 and summarized in Table I. We note the following general features of these plots: 1. times are all reported on a logarithmic scale, 2. the distribution of planning time for VAMP is almost completely separated from both PyBullet/ompl and MoveIt/ompl, and 3. the distribution shapes of planning time versus path length are qualitatively similar and simplified path length distributions are equivalent for each planner, indicating planner similarity at the algorithmic level. Over all robots, VAMP is roughly 500x faster than PyBullet/ompl and 100 to 200x faster than MoveIt/ompl, while achieving similar path quality. VAMP provides high-quality plans at control frequencies, *e.g.*, $10\ {kHz}$ mean, $25\ {kHz}$ median, and $2.3\ {kHz}$ 95% planning rates for the Panda arm for the entire dataset, which includes trivial problems such as tabletop manipulation and complex problems such as reaching into shelves.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Experiments", "weight": 1.0} -->

Note that even the slowest number in Table I, $25\ {ms}$ for the Fetch's 95% quantile, achieves a $40\ {Hz}$ planning rate. Morever, VAMP (arm) also achieves similar speed-ups on a low-power single-board computer (the Orange Pi 5B uses up to $7\ W$), still 20--50x faster than baselines on a desktop cpu. We also report times for prm for the Panda and Fetch over the *table pick*, *table under pick*, and *box* environments (Table II), and show the same caliber of performance improvements, indicating our approach generalizes across sbmps.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Discussion", "weight": 1.5} -->

Efficient motion planning is critical for many applications of robotics. In this paper, we demonstrate a novel approach to accelerating motion planning, based on a new perspective on *vector-oriented* operations for simple, high-frequency interleaving of high-performance parallelized and serial sections of code present in most sampling-based motion planning algorithms. By applying this perspective to the most expensive and ubiquitous motion planning subroutines (*i.e.*, collision checking, forward kinematics, and distance computation), we achieve algorithmic improvements and create proof-of-concept planners that achieve more than 500x speedup over the state of the art on realistic, challenging planning problems for three different robots. Our approach solves planning problems at kilohertz rates on ordinary consumer CPUs and low-power single-board computers.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Discussion", "weight": 1.5} -->

We also believe that our ideas will extend naturally to harder motion planning problems, such as kinodynamic and manifold-constrained planning. Further, because we can produce so many motion plans so fast, we may be able to efficiently provide empirical proofs of *solution nonexistence*, a feat that has long been challenging for sbmp. There may also be potential for using our vector-oriented planners as *local planners* inside higher-level motion planning algorithms.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Discussion", "weight": 1.5} -->

The planning performance demonstrated in this work pushes sbmp for high-DoF manipulators to frequencies required for control---providing a complete, global, high-quality plan at each update. We believe that this is cause to re-examine old assumptions in robotics about the roles of planning and control, as well as about the ?best? way to solve problems such as planning under uncertainty or integrated task and motion planning. In particular, we are excited to explore extensions of this work around, *e.g.*, rapid replanning, integrated task and motion planning, etc. In general, there is a rich discussion to be had about implications for algorithms that use motion planning as a subroutine, and that have traditionally needed to be designed around motion planning as an *expensive* subroutine, now that we can consistently provide high-quality motion plans at high frequencies.
