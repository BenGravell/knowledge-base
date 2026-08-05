<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Fast Asymptotically Optimal Kinodynamic Planning via Vectorization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sampling-based motion planners have been shown to be effective for systems with complex kinodynamic constraints and high dimensionality. However, these algorithms struggle to achieve real-time performance, leading to recent efforts to parallelize planning. While GPU-accelerated planners have achieved significant speedups, existing approaches require specialized CUDA programming that limits accessibility and portability. We present Parallel Asymptotically Optimal Kinodynamic RRT (PAKR), a massively parallel kinodynamic planner leveraging JAX and the XLA compiler to achieve GPU acceleration through standard Python tooling. By combining our parallel planner with the AO-x meta-algorithm, we achieve asymptotic optimality through fast iterative replanning. We provide a theoretical analysis of probabilistic completeness, analyze the effects of batch size and branching factor on convergence, and demonstrate scalability to complex dynamics using the MuJoCo-XLA simulator. Experiments show competitive runtimes with state-of-the-art GPU planners and superior solution quality.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robotic systems deployed in dynamic environments require fast, reactive motion planning that accounts for the robot's dynamics. One approach is kinodynamic motion planning, which is concerned with finding trajectories that satisfy both kinematic constraints and equations governing the robot's dynamics, and can be quite challenging for even low-dimensional problems \[lavalle2006planning, kavraki2016motion\]. Sampling-based motion planners (SBMPs) have proven effective due to their ability to handle high-dimensional state spaces and complex nonlinear dynamics \[rrt, sst, orthey2023sampling\]. Still, finding solutions can take hundreds of milliseconds for simple systems and tens of seconds for complex nonlinear dynamics, which is insufficient for real-time reactivity in changing environments.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent advances in parallel computing offer a solution. GPU and CPU parallelization have demonstrated significant speedups by batching operations such as collision checking \[vamp, 6095053\], parallelizing entire expansion iterations \[prrtc, kinopax\], or running multiple independent planner instances \[caselli99, cforest\]. For kinodynamic systems specifically, Kino-PAX \[kinopax\] achieves real-time performance through GPU-accelerated tree expansion, finding solutions in tens of milliseconds.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, parallel motion planning algorithms often compromise on solution quality. Many asymptotically optimal (AO) planners achieve high-quality solutions through mechanisms like rewiring \[rrtstar, kinorrtstar\] or maintaining best-cost nodes within witness regions \[sst\]. These techniques rely on ordering; each node's insertion depends on the current global state of the tree. In a batched parallel context, samples within the same batch lack mutual visibility: a node may attach to a sub-optimal parent because the optimal parent is still being processed. This staleness problem leads to redundant exploration and sub-optimal decisions, making it difficult to maintain theoretical convergence guarantees without introducing significant synchronization overhead.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present PAKR, a massively parallel kinodynamic motion planner that achieves both speed and solution quality. Our key insight is that the AO-x meta-algorithm \[aox\], which transforms any probabilistically complete planner into an asymptotically optimal one through iterative cost-bounded replanning, is naturally suited to parallelization; rather than fighting stale information, we embrace fast, sub-optimal planning and use rapid replanning to converge toward optimal solutions. Our implementation uses JAX \[jax2018github\] to fuse the entire planning loop into a single GPU kernel, eliminating CPU-GPU overhead without requiring CUDA programming. Our approach makes GPU-accelerated kinodynamic planning accessible through standard Python tooling.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, our contributions are: a massively parallel kinodynamic SBMP that leverages XLA compilation via JAX for efficient GPU execution, an implementation of the AO-x algorithm to achieve asymptotic optimality in a parallel setting, demonstration of scalability to complex domains including MuJoCo-XLA (MJX) \[mujoco\], and experimental validation showing competitive or superior performance compared to state-of-the-art planners, with solutions found in milliseconds. Our code is available open source at

<!-- chunk {"id": "body-0008", "role": "body", "section": "II-A Kinodynamic Planning", "weight": 1.0} -->

In kinodynamic planning, interpolating between $x_{rand}$ and $x_{near}$ requires solving a Two-Point Boundary Value Problem (BVP): finding a control trajectory $u(t)$ such that the system state $x(t)$ exactly satisfies $x=x_{near}$ and $x(T)=x_{rand}$ while obeying the dynamics $\dot{x}=f(x,u)$. For high-dimensional or non-linear systems, such as those with underactuated dynamics or non-holonomic constraints, the BVP is often computationally intractable or has no closed-form solution. To avoid the BVP in bidirectional search, Nayak and Otte \[gbrrt\] use the reverse tree as a heuristic to guide the forward expansion, but do not directly connect the forward and reverse trees.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-A Kinodynamic Planning", "weight": 1.0} -->

Sampling-based kinodynamic planners \[rrt, sst, gbrrt\] avoid this by adding new states through forward propagation from $x_{near}$, ensuring dynamic feasibility while still guiding expansion towards unexplored regions by selecting $x_{near}$ to be close to $x_{rand}$. Forward propagation can either be guided by a steering function to ensure the new state is close to $x_{rand}$, or it can be random, sampling a control from a uniform distribution \[rrt\]. By bypassing the need for a "steering" mechanism, kinodynamic planners excel in planning for systems with complex physics, such as agile drones, soft robots \[vine\], and non-prehensile manipulation tasks where the contact dynamics are non-linear and discontinuous.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-B Asymptotically Optimal Motion Planners", "weight": 1.0} -->

While some motion planners emphasize fast initial solutions, others prioritize the quality of solutions as they converge toward an optimal path. A motion planner is defined as asymptotically optimal (AO) if, provided an optimal solution exists, the probability that the cost of the returned solution approaches the theoretical optimum equals 1 as the number of samples approaches infinity \[gammell2021asymptotically\].

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-B Asymptotically Optimal Motion Planners", "weight": 1.0} -->

Many AO and near-optimal variants of the RRT algorithm achieve this property by maintaining a tree structure that is dynamically reorganized as better paths are discovered. RRT\* \[rrtstar\] introduced the concept of "rewiring," where new samples look within a local radius to see if they can provide a lower-cost path to existing nodes. This was also extended to the kinodynamic domain, though the requirement to solve the two-point BVP for every rewiring attempt limits its practical use to systems with linear dynamics \[kinorrtstar\].

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Asymptotically Optimal Motion Planners", "weight": 1.0} -->

As an AO kinodynamic planner for general non-linear systems without a BVP solver, Stable-Sparse RRT\* \[sst\] maintains witness regions that only consider best-cost nodes within each region for expansion, maintaining a sparse set of nodes that improve in cost with each iteration.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-B Asymptotically Optimal Motion Planners", "weight": 1.0} -->

Search-based planners typically construct a graph through a lattice decomposition \[lattice-search\] and leverage heuristics to find an optimal path. For certain classes of dynamics, solutions found on the lattice are provably within a tolerance $\epsilon$ of the continuous optimum \[donald1993, donald1995provably\]. Meanwhile, Iterative Discontinuity Bounded A\* (iDb-A\*) grows a set of locally optimal trajectories which asymptotically cover the state space and allow for "discontinuity-bounded" connections between states that are sufficiently close. This allows the planner to treat a sequence of dynamically feasible trajectories as a continuous path, which is further refined through trajectory optimization.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Asymptotically Optimal Motion Planners", "weight": 1.0} -->

Finally, optimality can be achieved through meta-algorithmic wrappers like AO-x \[aox\]. This approach allows any feasible (but sub-optimal) kinodynamic planner to be transformed into an AO planner. By iteratively decreasing a cost threshold based on the best solution found so far and rejecting any future samples that exceed this threshold, the algorithm forces the underlying planner to produce increasingly efficient trajectories over time.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-C Parallel Motion Planning", "weight": 1.0} -->

Parallel motion planners are generally categorized into coarse-grained and fine-grained methods. Coarse-grained parallelization typically involves running multiple independent planner instances; the simplest approach runs separate planners simultaneously and returns the first solution found \[caselli99\]. More sophisticated frameworks, such as C-FOREST \[cforest\], use a higher-level manager to periodically share the promising paths found.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-C Parallel Motion Planning", "weight": 1.0} -->

Fine-grained parallelization targets specific, computationally expensive sub-processes. VAMP \[vamp\] uses Single Instruction, Multiple Data (SIMD) batching to parallelize collision checking and forward kinematics solving, achieving sub-millisecond runtimes. Similarly, Kino-PAX \[kinopax\] and pRRTC \[prrtc\] parallelize the expansion iteration itself, considering multiple states for tree insertion simultaneously.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-C Parallel Motion Planning", "weight": 1.0} -->

Parallelization often conflicts with the mechanisms required for asymptotic optimality. Algorithms like RRT\* \[rrtstar\] and SST\* \[sst\] rely on a strict sequential ordering; each node's insertion is conditioned on the current "global" state of the tree to determine optimal connection or pruning. We also note Kino-PAX^+^ \[perrault2026kino\], a recent extension to Kino-PAX that provides asymptotic near-optimality guarantees by only expanding from the best-cost nodes in witness regions, similar to \[sst\]. In contrast, the AO-x meta-algorithm \[aox\] builds off of parallelism directly: the faster a feasible solution can be found, the more the solution can be improved.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Consider a robot with state space $\mathcal{X}\subseteq\mathbb{R}^{n}$ and control space $\mathcal{U}\subseteq\mathbb{R}^{m}$. The system dynamics are governed: where $x(t)\in\mathcal{X}$ and $u(t)\in\mathcal{U}$ are the state and control at time $t$. We assume $f$ is Lipschitz continuous in both arguments. A trajectory $\sigma:[0,T]\to\mathcal{X}$ is *feasible* if there exists controls $u:[0,T]\to\mathcal{U}$ such that $\dot{\sigma}(t)=f(\sigma(t),u(t))$ and $\sigma(t)\in\mathcal{X}_{free}$ for all $t\in[0,T]$, where $\mathcal{X}_{free}$ is the collision-free subset of $\mathcal{X}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Let $\Sigma$ denote the set of all feasible trajectories. We define a cost function $J:\Sigma\to\mathbb{R}_{\geq 0}$ that assigns a non-negative cost to each trajectory. We assume $J$ satisfies the standard properties for optimal planning \[aox\]: Lipschitz continuity, additivity, and monotonicity. Common examples include path length $J(\sigma)=\int_{0}^{T}\|\dot{\sigma}(t)\|dt$ and time optimality $J(\sigma)=T$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We are concerned with the problem of optimal kinodynamic planning. That is, given dynamics $f$, initial state $x_{init}\in\mathcal{X}_{free}$, goal region $\mathcal{X}_{goal}\subseteq\mathcal{X}_{free}$, and cost function $J$, find a control trajectory $u:[0,T]\to\mathcal{U}$ that minimizes $J(\sigma)$ over all feasible trajectories $\sigma$ satisfying: Let $J^{*}=\inf_{\sigma\in\Sigma_{sol}}J(\sigma)$ denote the optimal cost, where $\Sigma_{sol}\subseteq\Sigma$ is the set of goal-reaching feasible trajectories. An algorithm is *asymptotically optimal* if the cost of its returned solution converges to $J^{*}$ almost surely as computation time increases \[gammell2021asymptotically\].

<!-- chunk {"id": "body-0021", "role": "body", "section": "Methodology", "weight": 1.0} -->

Our key insight is that the AO-x meta-algorithm \[aox\] is naturally suited to massively parallel execution. While AO-x transforms any probabilistically complete planner into an asymptotically optimal one through iterative cost-bounded replanning, its practical utility depends on the speed of the inner planner. Typical planners require seconds per iteration, limiting the number of refinement cycles achievable. Rather than fighting synchronization issues within a single tree, we embrace fast sub-optimal planning and use rapid replanning to converge toward optimality. By using our parallel kinodynamic RRT (Sec. IV-A), each inner planning iteration completes in milliseconds, enabling many cycles of improvement.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Methodology", "weight": 1.0} -->

Input: Initial state xinit, Goal region 𝒳goal, Control space 𝒰, Batch size B, Branching factor A Output: Best trajectory σ* found within time budget 5 while time budget not exceeded do // Initialize new tree for this planning iteration // Tree stores (state, action, cost-to-come) tuples 7 while goal not reached do // Parallel batch expansion // Select B/A parents via nearest neighbor 9 Xnear ← NearestNeighbor(𝒯, Xrand); // Sample A controls per parent // Parallel rollout of all B expansions 11 Xnew, Cnew ← Propagate(Xnear, U, Δt); 12 foreach (xnew, cnew) ∈ (Xnew, Cnew) in parallel do 13 if cnew + h(xnew) < cbest then 14 if CollisionFree(xnear ⇝ xnew) then 16 if xnew ∈ 𝒳goal then // Exit inner loop to refine with tighter bound Algorithm 1 Parallel AO Kinodynamic RRT (PAKR) Alg. 1 presents the parallel AO kinodynamic-RRT (PAKR) algorithm.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Methodology", "weight": 1.0} -->

The outer loop (Line 1) iteratively refines solutions by restarting the planner with progressively tighter cost bounds. The inner loop (Line 1) implements parallel kinodynamic RRT expansion: each iteration samples $B/A$ target states (Line 1), finds their nearest neighbors in the tree, samples $A$ random controls per parent, and propagates all $B$ state-action pairs in parallel (Line 1). Nodes are only inserted if their f-cost $f(n)=g(n)+h(n)$ is below the current best solution cost, where $g(n)$ is the cost-to-come and $h(n)=\|x_{n}-x_{goal}\|_{2}$ is the Euclidean heuristic (Line 1). This focuses computation on regions that can potentially improve the solution. When a goal is reached (Line 1), the algorithm records the solution, updates $c_{best}$, and restarts with the tighter bound.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-A Implementation", "weight": 1.0} -->

To maximize performance, our implementation employs a static-graph architecture optimized for GPU execution. Unlike CUDA-based planners that rely on dynamic branching and host-side management, a statically compiled planner runs entirely within a single GPU kernel, eliminating CPU-GPU device transfer overhead.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-A Implementation", "weight": 1.0} -->

To enable the compiler to generate a high-efficiency monolithic kernel, the algorithm imposes a static shape constraint: the maximum tree size ($N$) and the parallel batch size ($B$) must be defined at compile-time for fixed memory offsets. The search tree is represented as a structure of arrays, where four contiguous buffers store the tree data: $\textbf{states}\in\mathbb{R}^{N\times d}$ for state vectors, $\textbf{actions}\in\mathbb{R}^{N\times m}$ for control inputs, $\textbf{parents}\in\mathbb{Z}^{N}$ for parent indices enabling path reconstruction, and $\textbf{costs}\in\mathbb{R}^{N}$ for cost-to-come values. Node insertion uses indexed slice updates that write batches of new nodes at the current tree frontier. A scalar counter tracks the number of valid nodes, enabling masked operations over padded arrays.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-A Implementation", "weight": 1.0} -->

The computational cost of nearest neighbor (NN) search is often the bottleneck for planners that construct large trees \[nnbottleneck\]. Fortunately, the distance calculations of the NN search are easily vectorizable, allowing it to scale efficiently with GPU core counts. To further reduce the NN bottleneck, we introduce a Branching Factor ($A$). Rather than performing a costly NN search for every candidate expansion, we select $K=B/A$ parent nodes and sample $A$ random controls per parent. Our experiments show that moderate branching factors ($A\in$) effectively balance exploration efficiency with NN overhead. To minimize the performance penalty of padding in a growing tree, we employ a tiered nearest neighbor strategy. We define memory tiers at tree sizes in the range $4^{}$, with specialized kernels for each tier that process only the active portion of the tree.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-A Implementation", "weight": 1.0} -->

Our framework supports arbitrary dynamics through modular propagator functions. For example, we can interface directly with MuJoCo-XLA \[mujoco\], enabling planning directly on the differentiable simulator's state representation. Forward propagation integrates the system dynamics using fourth-order Runge-Kutta integration. The entire rollout is vectorized, which compiles efficiently. Each propagation applies the same control for $T$ timesteps, with validity checked at each step via batched collision queries.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-B Theoretical Analysis", "weight": 1.0} -->

We establish that our approach is probabilistically complete and, through the AO-x meta-algorithm, achieves asymptotic optimality under the condition that the cost function and robot dynamics are Lipschitz continuous. We use a forward-propagation scheme to satisfy differential constraints. Our parallel kinodynamic RRT inherits probabilistic completeness from sequential kinodynamic RRT \[pcrrt\]. Our parallelization affects only the *rate* of sampling by introducing a bounded delay on the discoverability of nodes, not the *distribution* of samples.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Theoretical Analysis", "weight": 1.0} -->

Consider a batched planner with a branching factor $A=1$. Unlike sequential kinodynamic RRT, where newly inserted nodes are immediately available for future nearest-neighbor queries, all nearest-neighbor queries within a batch are evaluated against a frozen snapshot of the tree. Consequently, the discovery of descendants of newly inserted nodes may be delayed by at most one batch. Probabilistic completeness of forward-propagation RRT relies on the existence of a finite sequence of successful extensions connecting the start state to the goal region, each occurring with non-zero probability \[pcrrt\]. Batching only requires successive extensions along such a sequence to occur in different batches, rather than different iterations, introducing a finite delay in node availability without changing the probability that each extension is eventually realized. Since the number of batches approaches infinity as the number of samples approaches infinity, this bounded delay does not affect asymptotic probabilistic completeness.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B Theoretical Analysis", "weight": 1.0} -->

For a branching factor $A>1$, the planner performs $K=B/A$ nearest-neighbor queries and samples $A$ controls for each selected parent. Relative to a planner with batch size $K$ and a single control sample per parent, the branching planner evaluates the same set of parent nodes while augmenting each parent with an additional $A-1$ independently sampled controls. Thus, every candidate propagation considered by the $A=1$ planner is also considered by the branching planner, together with additional control samples. Since branching preserves all opportunities for successful expansion while introducing additional candidate propagations, it does not compromise probabilistic completeness.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B Theoretical Analysis", "weight": 1.0} -->

Our use of a fixed-step propagator ($\Delta t$) for XLA-optimization purposes is consistent with the assumptions of completeness for discrete-time kinodynamic planners, provided $\Delta t$ is sufficiently small.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B Theoretical Analysis", "weight": 1.0} -->

Since the inner planner is probabilistically complete and the cost threshold $c_{\mathrm{best}}$ is monotonically decreasing across AO-x iterations, the assumptions of AO-x \[aox\] remain satisfied. Under Lipschitz continuous dynamics and cost functions, the sequence of solutions produced by PAKR therefore converges almost surely to the optimal cost $c^{\ast}$, establishing asymptotic optimality.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

We benchmark PAKR against Kino-PAX \[kinopax\], another parallelized kinodynamic motion planner implemented in CUDA C, as well as the sequential CPU-based kinodynamic planners iDb-A\* \[idbastar\], and SST\* \[sst\] from the Open Motion Planning Library (OMPL) \[ompl\]. We also show convergence results for PAKR, and explore the effects of batch size and branching factor on the performance of PAKR. Both PAKR and Kino-PAX are run on an NVIDIA GeForce RTX 4090 with 16,384 CUDA cores and 24 GB of VRAM, while iDb-A\* and SST are executed on a 24-core AMD Ryzen Threadripper PRO 5965WX with a base clock speed of 3.8GHz and 32 GB of RAM. In all experiments, we report the median performance of each planner across 100 trials.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-A Comparison With Kino-PAX", "weight": 1.0} -->

We evaluate the performance of PAKR and Kino-PAX on the same environments and dynamics in the original Kino-PAX paper: Double Integrator (DI) has a 6-dimensional state space $[x,y,z,\dot{x},\dot{y},\dot{z}]$ consisting of the 3D position and velocity, and a 3-dimensional control space $[\ddot{x},\ddot{y},\ddot{z}]$ consisting of the linear acceleration applied to each axis.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-A Comparison With Kino-PAX", "weight": 1.0} -->

Dubins Airplane (DA) has a 6-dimensional state space $[x,y,z,\phi,\theta,v]$ consisting of the 3D position, yaw, pitch, and forward speed, and a 3-dimensional control space $[\dot{\phi},\dot{\theta},\dot{v}]$ consisting of the yaw rate, pitch rate, and forward acceleration.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-A Comparison With Kino-PAX", "weight": 1.0} -->

Quadcopter (QC) has a 12-dimensional state space $[x,y,z,\phi,\theta,\psi,u,v,w,p,q,r]$ consisting of the 3D position, yaw, pitch, and roll angles, linear velocities in body frame, and angular velocities in body frame, and a 4-dimensional control space $[T,\tau_{x},\tau_{y},\tau_{z}]$ consisting of the thrust and torques in body frame.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-A Comparison With Kino-PAX", "weight": 1.0} -->

A depiction of the Tree (A), Narrow (B), and House (C) environments can be seen in Fig. 1. As Kino-PAX is not asymptotically optimal, we use a variant of PAKR without the AO-x meta-algorithm, where a single parallel RRT iteration is run, for a fair comparison. Experimental results are shown in Table I. While there is an asymptotically near-optimal extension of Kino-PAX \[perrault2026kino\], we do not evaluate against it due to the lack of an open-source implementation. In all environments and dynamics, PAKR consistently has a smaller tree size than Kino-PAX upon finding a solution, showing that it is more efficient at exploring the state space while achieving comparable runtime.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-B AO Convergence", "weight": 1.0} -->

We show the fast convergence of PAKR towards an optimal solution for the dynamics and environments described in Sec. V-A. A visualization of the initial and final trajectories can be found in Fig. 1. While it is standard for kinodynamic planners to find time-optimal trajectories using time duration as the cost criterion, we chose to measure distance traveled to make it easier to visualize the solution convergence. Numerical results are reported in Table II, and Fig. 2 displays the convergence of the 6d double integrator in environment A relative to the number of iterations and time. We find that PAKR is able to significantly reduce the cost of solution trajectories in only tens of milliseconds.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-C Comparison With iDb-A\\* and SST\\*", "weight": 1.0} -->

To evaluate the quality of solutions produced, we compare the performance of PAKR with that of the asymptotically optimal iDb-A\* and SST\* planners on four dynamical systems from DynoBench, a benchmark for kinodynamic planning problems \[idbastar\]: Unicycle 1 has a 3-dimensional state space $[x,y,\theta]$ consisting of the 2D position and heading, and a 2-dimensional control space $[v,\omega]$ consisting of the linear velocity in the direction of the heading and angular velocity.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-C Comparison With iDb-A\\* and SST\\*", "weight": 1.0} -->

Unicycle 2 has a 5-dimensional state space $[x,y,\theta,v,\omega]$ including the linear and angular velocities in the state, and a 2-dimensional control space $[a,\alpha]$ consisting of the linear and angular accelerations.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-C Comparison With iDb-A\\* and SST\\*", "weight": 1.0} -->

Acrobot has a 4-dimensional state space $[\theta_{1},\theta_{2},\dot{\theta}_{1},\dot{\theta}_{2}]$ consisting of the angles and angular velocities of the two links of double pendulum that is actuated at the second (elbow) joint, and has a 1-dimensional control space consisting of the torque applied at the second joint.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-C Comparison With iDb-A\\* and SST\\*", "weight": 1.0} -->

Quadcopter has the same dynamics as the 12D Quadcopter described in Sec. V-A, and is referred to as "Quadrotor v1" in DynoBench.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-C Comparison With iDb-A\\* and SST\\*", "weight": 1.0} -->

For Unicycle 1 and Unicycle 2, the planners are evaluated on a custom problem with randomly distributed square obstacles, as illustrated in Fig. 3, while for Acrobot and Quadcopter the swing-up and window problems from DynoBench are used, respectively, for evaluation. More information about these systems and problems can be found in \[idbastar\].

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-C Comparison With iDb-A\\* and SST\\*", "weight": 1.0} -->

Note: Unicycle 1 uses velocity control while Unicycle 2 uses force control.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-C Comparison With iDb-A\\* and SST\\*", "weight": 1.0} -->

Both iDb-A\* and SST\* are given a planning budget of 300 seconds to fairly evaluate their convergence towards the optimal solution. The hyperparameters of SST\* (goal bias, selection radius, pruning radius) are also fine-tuned for each problem to achieve more competitive performance; additionally, for Acrobot and Quadcopter the goal region of SST\* is expanded to increase likelihood of finding a solution, with an additional trajectory optimization step to find an exact solution. In line with DynoBench, the duration of the solution trajectory is used as the cost. Results are shown in Table III. We find PAKR achieves orders of magnitude speed-up of initial solution time, as well as better initial solution cost in 3 out of 4 problems compared to iDb-A\* and SST\*, while also having better or competitive final solution cost. We believe that the particularly low success rate of iDb-A\* on Unicycle 2 is due to its reliance on a trajectory optimization step to compute a feasible trajectory, which fails under the complex dynamics and cluttered environment.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-D Effects of Batch Size and Branching Factor", "weight": 1.0} -->

We experiment with varying batch sizes and branching factors on the performance of PAKR with the 12D quadcopter in Environment A. Results are displayed in Table IV.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-D Effects of Batch Size and Branching Factor", "weight": 1.0} -->

Due to the high dimensionality of the quadcopter system, a large branching factor is detrimental to exploration, causing success rates and runtime performance to worsen. However, a branching factor of 2 is tested to show its effect on reducing the nearest neighbor search overhead, especially for large batch sizes that approach the limits of GPU capacity. Both batch size and branching factor affect the exploration efficiency, which can be seen in the increasing tree size.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-E Scalability to Heavy Simulation", "weight": 1.0} -->

To show PAKR's ability to scale to complex physical simulation, we demonstrate our approach on Cartpole and Block Push problems using Mujoco XLA \[mujoco\], as well as a soft growing vine robot planning problem using the soft robot simulator from Gao et al. \[vine\]: Cartpole has a 4-dimensional state space $[x,\theta,v,\omega]$ and a 1-dimensional control space $[a]$ for the cart's linear acceleration.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-E Scalability to Heavy Simulation", "weight": 1.0} -->

Block Push is defined by a 10-dimensional state space $\mathbf{s}\in\mathbb{R}^{10}$, which can be decomposed into the configuration vector $\mathbf{q}$ and the velocity vector $\dot{\mathbf{q}}$: We simplify the standard robot manipulator problem by reducing the state space, only accounting for the end effector position and velocity instead of the $q$ and $\dot{q}$ of the entire arm. We also restrict the end effector and block positions to the 2d plane. The controls $[\ddot{x}_{ee},\ddot{y}_{ee}]$ are forces acting upon the end effector.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-E Scalability to Heavy Simulation", "weight": 1.0} -->

Vine \[vine\] decomposes a soft growing vine robot into a multi-body link, calculating the joint angles and the length of the distal tip as the vine grows and actuation is applied to the body. While it keeps track of all joints, the planner only considers the tip position $[x,y,\theta]$ for its distance calculations. Its action space $[p,l_{0}]$ are two pneumatic actuator inputs that determine the bending moment at each joint.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-E Scalability to Heavy Simulation", "weight": 1.0} -->

Fig. 4 shows a trajectory produced by PAKR for the block push problem, while Fig. 5 displays the resultant tree for the vine planner. The median times to find a solution for Cartpole, Block Push, and Vine were 22.82, 283.65, and 360.25 ms, respectively. This increase in runtime can be attributed to heavier computation during propagation when using a physics simulator instead of analytical functions.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

We present PAKR, a high-performance kinodynamic motion planner that balances rapid execution with high solution quality. By parallelizing the AO-x meta-algorithm with a fast internal RRT-based approach, we transform fast, sub-optimal sampling into an asymptotically optimal process through iterative, cost-bounded replanning. Our implementation uses JAX to fuse the entire planning loop into a single GPU kernel, eliminating CPU-GPU overhead and making high-speed kinodynamic planning accessible through standard Python tooling.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In summary, our contributions include: a massively parallel sampling-based motion planner utilizing XLA compilation for efficient GPU execution, an adaptation of the AO-x algorithm that achieves asymptotic optimality in a parallelized setting, demonstrated scalability across complex environments, including high-dimensional MuJoCo-XLA domains, and experimental validation showing that PAKR achieves competitive or superior performance compared to state-of-the-art planners, frequently finding solutions in milliseconds.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

Future work includes extending this planner to more difficult, higher-dimensional problems such as non-prehensile manipulation with a 7-DoF arm, integrating learned action proposals rather than random sampling, and evaluating against Kino-PAX^+^ \[perrault2026kino\] when available.
