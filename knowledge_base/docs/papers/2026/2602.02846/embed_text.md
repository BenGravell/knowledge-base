## Introduction

Autonomous robotic systems deployed in dynamic environments require fast, reactive motion planning that accounts for complex kinematics and dynamics. However, feasibility alone is insufficient for high-performance operation; such systems demand *high-quality* trajectories that minimize costs such as path length, energy consumption, execution time, or control effort. Despite recent progress in accelerating fast kinodynamic motion planning via, e.g., parallelization, achieving *fast optimal* planning remains a significant challenge. In this work, we aim to enable real-time, near-optimal motion planning for complex and high-dimensional kinodynamical systems by exploiting the parallel architecture of GPU-like devices.

Sampling-based motion planners (SBMPs) have emerged as the dominant approach for these challenges, successfully handling complex dynamics, complex tasks, and stochastic environments. These methods have been extended to optimize for a cost function, achieving asympotic near-optimality. Nevertheless, traditional SBMPs are typically designed for serial computation, limiting their performance to the clock speed of a single CPU core. While recent methods can find solutions within seconds for simple systems and tens of seconds for complex ones, these latencies are insufficient for *real-time* reactivity. With the stagnation of single-thread performance improvements, parallel architectures like GPUs offer the only viable path to substantial speedups. Yet, standard asymptotically optimal algorithms are inherently sequential, making them inefficient when naively parallelized.

Figure 1: Three solutions found by Kino-PAX+ using 6D Double Integrator dynamics and minimizing path length cost.

On the other hand, parallel methodologies have been actively explored to overcome these serial limitations. CPU-based parallel approaches \[25, 28, 32, 10, 11, se, and euclidean spaces"), 33\] distribute the search workload across multiple cores to accelerate convergence. However, these methods are fundamentally constrained by the limited number of available CPU cores (typically tens) and the significant synchronization overhead required to maintain tree consistency, often yielding sub-linear speedups that are insufficient for high-rate replanning. Conversely, GPU-based algorithms such as Kino-PAX utilize massive concurrency (thousands of threads) to quickly find solutions. While this yields millisecond-level planning times, it only finds feasible solutions without optimizing for a cost function.

In this paper, we present Kino-PAX^+^, a massively parallel near-optimal kinodynamic SBMP designed for efficient execution on modern many-core (GPU) processors. Kino-PAX^+^ delivers *real-time*, *low-cost* first solutions and guarantees asymptotic *near-optimality* over extended planning durations (see Figure 1). Kino-PAX^+^ is an adaptation of existing GPU-based kinodynamic planner Kino-PAX. Unlike Kino-PAX, which focuses on rapidly finding a single solution, our proposed method quickly identifies low-cost initial solutions and iteratively refines these solutions over extended planning durations. Inspired by (serial) near-optimal planner SST, the main idea is that, in local neighborhoods, only promising nodes with low path costs should be considered for expansion. This enables pruning of nodes that do not contribute to good quality solutions, and thereby achieving asymptotic near-optimality. We present a formal analysis of Kino-PAX^+^, proving its asymptotic near-optimality and $\delta$-robust completeness. Finally, we demonstrate through several benchmarks that Kino-PAX^+^ is effective across a variety of motion planning problem domains.

In short, our main contributions are: (i) the *first* near-optimal, massively parallel kinodynamic SBMP algorithm designed for GPU-like devices to the best of knowledge, (ii) a thorough analysis and proof of probabilistic completeness and asymptotic near-optimality, and (iii) several benchmarks and comparisons showing the efficiency and efficacy of Kino-PAX^+^. Our results show that Kino-PAX^+^ achieves up to three orders-of-magnitude speedups over serial methods while attaining lower solution cost than both serial methods and Kino-PAX at comparable planning times. In 3D complex environments, Kino-PAX^+^ finds solutions in approximately $10$ ms for 6D systems and hundreds of milliseconds for 12D nonlinear systems, while continuously converging toward near-optimality with additional planning time.

### I-A Related Work

### Geometric Motion Planning

Sampling-based motion planners (SBMPs) such as PRM and RRT are foundational for geometric planning but are inherently serial. To improve planning rates, recent works have explored parallelization on both multi-core CPUs \[25, 28, 32, 10, 11, se, and euclidean spaces"), 33\] and many-core GPUs. While CPU-based methods achieve modest speedups via fine-grained lock-free data structures, they are constrained by low core counts and high inter-thread communication costs. Conversely, GPU-based methods like Ichter et al. achieve orders-of-magnitude speedups by adapting algorithms like FMT\*. However, these techniques rely on explicit boundary value problem solvers (steering functions) to connect states, restricting them strictly to geometric or simple linear problems and rendering them inapplicable to complex kinodynamic systems.

### Kinodynamic Motion Planning & Optimality

For systems with complex differential constraints, kinodynamic planners such as RRT and EST extend trees via forward propagation. To achieve *asymptotic near-optimality*, algorithms like SST and AO-RRT introduce cost-based pruning and selection criteria. However, these operations are computationally expensive and difficult to parallelize due to their sequential dependencies. Existing parallel kinodynamic approaches typically employ *coarse-grained* parallelism (running multiple independent trees), which improves average-case time-to-solution but does not accelerate the convergence rate of a single optimal plan.

Most relevant to our work is Kino-PAX, which demonstrates that massive GPU parallelism can solve the *feasibility* problem for kinodynamic systems in milliseconds. However, Kino-PAX lacks the mechanisms for cost refinement and asymptotic optimality. In this work, we build upon the parallel architecture of Kino-PAX, integrating cost-based selection and pruning mechanics to create the first GPU motion planner that is both fast and asymptotically near-optimal.

## Problem Formulation

Consider a robotic system in a bounded workspace $W \subset {\mathbb{R}}^{d}$, where $d \in {\{ 2,3\}}$, with a finite set of obstacles $\mathcal{O}$. The robot's motion is constrained to the dynamics

where ${x{(t)}} \in X \subset {\mathbb{R}}^{n}$ is the state, and ${u{(t)}} \in U \subset {\mathbb{R}}^{N}$ is the control at time $t$. The state space $X$ and control space $U$ are assumed to be compact. Function $f:{{X \times U}\rightarrow{\mathbb{R}}^{n}}$ is the vector field and assumed to be Lipschitz continuous with respect to both arguments, i.e, there exist constants ${K_{x},K_{u}} > 0$ such that for all ${x,x^{\prime}} \in X$ and ${u,u^{\prime}} \in U$, ${{\|{{f{(x,u)}} - {f{(x^{\prime},u^{\prime})}}}\|} \leq {{K_{x}{\|{x - x^{\prime}}\|}} + {K_{u}{\|{u - u^{\prime}}\|}}}}.$ In addition, we assume that the system dynamics satisfy Chow's condition, which implies that the system is small-time locally accessible.

Beyond the differential constraints in and obstacles in $\mathcal{O}$, the robot must satisfy state constraints (e.g., velocity limits). We define the valid state space $X_{\text{valid}} \subseteq X$ as the set of states that are collision-free and satisfy all state constraints.

Given an initial state $x_{\text{init}} \in X_{\text{valid}}$, a time horizon $t_{f} \geq 0$, and a control trajectory $\mathbf{u}:{{\lbrack 0,t_{f}\rbrack}\rightarrow U}$, a unique state trajectory $\mathbf{x}:{{\lbrack 0,t_{f}\rbrack}\rightarrow X}$ is obtained such that

Trajectory $\mathbf{x}$ is *valid* if, ${\forall t} \in {\lbrack 0,t_{f}\rbrack}$, ${\mathbf{x}{(t)}} \in X_{\text{valid}}$. The objective of kinodynamic motion planning is to find a valid trajectory $\mathbf{x}$ that reaches a given goal set $X_{\text{goal}} \subseteq X_{\text{valid}}$.

In addition to feasibility, we seek to optimize the cost of the trajectory. Let $\mathbf{X}$ denote the set of trajectories with finite durations. The cost of a trajectory is defined by a function ${cost}:{\mathbf{X}\rightarrow{\mathbb{R}}_{\geq 0}}$ that assigns to each trajectory $\mathbf{x} \in \mathbf{X}$ a non-negative value ${{cost}{(\mathbf{x})}} \in {\mathbb{R}}_{\geq 0}$. We assume that $cost$ is a smooth, continuous function satisfying the additivity, monotonicity, and non-degeneracy properties, as formally stated below.

### Assumption 1

The cost function $cost$ is Lipschitz continuous, i.e, there exists constant $K_{c} > 0$ such that

for all ${\mathbf{x},\mathbf{x}^{\prime}} \in \mathbf{X}$ with the same start state, i.e., ${\mathbf{x}{}} = {\mathbf{x}^{\prime}{}}$. Furthermore, consider a trajectory $\mathbf{x} \in \mathbf{X}$ with duration $t_{f} > 0$, and for $t \in {\lbrack 0,t_{f}\rbrack}$, define $\mathbf{x}^{t}$ and $\mathbf{x}_{t}$ as its *prefix* up to time $t$ and *suffix* from time $t$, respectively, so that their concatenation ${\mathbf{x}^{t} \bullet \mathbf{x}_{t}} = \mathbf{x}$. Then, it holds that, for all $t \in {\lbrack 0,t_{f}\rbrack}$:

Ideally, one seeks a valid trajectory $\mathbf{x}$ that reaches the goal set $X_{\text{goal}}$ while minimizing ${cost}{(\mathbf{x})}$. However, computing such an optimal trajectory is notoriously difficult. Instead, we aim to compute a near-optimal solution *very quickly*.

### Definition 1 (Near-optimal trajectory)

Let $\mathbf{X}_{\text{sol}} \subseteq \mathbf{X}$ be the set of solution trajectories to a given motion planning problem, i.e., ${\mathbf{X}_{\text{sol}} = {\{{\mathbf{x} \in \mathbf{X}}\mid{{{\mathbf{x}{(t)}} \in {X_{\text{valid}}{\forall t}} \in {\lbrack 0,t_{f}\rbrack}},{{\mathbf{x}{(t_{f})}} \in X_{\text{goal}}}}\}}},$ and denote by $c^{\ast}$ the minimum cost over all solution trajectories, i.e., ${c^{\ast} = {{\min_{\mathbf{x} \in \mathbf{X}_{\text{sol}}}{cost}}{(\mathbf{x})}}}.$ A trajectory $\mathbf{x}^{+} \in \mathbf{X}_{\text{sol}}$ is called a *near-optimal* solution if, for a $\beta > 0$,

### Problem 1 (Near-Optimal Kinodynamic Motion Planning)

Consider a robot with dynamics in operating in a workspace $W$ with obstacle set $\mathcal{O}$. Given an initial state $x_{\text{init}} \in X_{\text{valid}} \subseteq X$, a goal region $X_{\text{goal}} \subseteq X_{\text{valid}}$, and a trajectory cost function $cost$ satisfying Assumption 1. ‣ II Problem Formulation ‣ Kino-PAX+: Near-Optimal Massively Parallel Kinodynamic Sampling-based Motion Planner"), *efficiently* compute a control trajectory $\mathbf{u}:{{\lbrack 0,t_{f}\rbrack}\rightarrow U}$ whose induced state trajectory is a near-optimal solution as defined in Definition 1. ‣ II Problem Formulation ‣ Kino-PAX+: Near-Optimal Massively Parallel Kinodynamic Sampling-based Motion Planner").

While Problem 1. ‣ II Problem Formulation ‣ Kino-PAX+: Near-Optimal Massively Parallel Kinodynamic Sampling-based Motion Planner") is a standard near-optimal kinodynamic motion planning problem addressed by algorithms such as SST, it remains computationally challenging for real-time (millisecond-scale) applications. Recent GPU-based parallel solvers have enabled finding feasible kinodynamic trajectories tractable; however, the added complexity of optimizing for a cost function and ensuring near-optimality changes the algorithmic requirements. In this work, we focus on designing a highly efficient, GPU-based algorithm that provides asymptotic near-optimality guarantees.

## Kino-PAX^+^ Algorithm

To solve Problem 1. ‣ II Problem Formulation ‣ Kino-PAX+: Near-Optimal Massively Parallel Kinodynamic Sampling-based Motion Planner"), we propose *Near Optimal Kinodynamic Parallel Accelerated eXpansion* (Kino-PAX^+^), a highly parallel kinodynamic SBMP designed to utilize the throughput of many-core (GPU) architectures while providing asymptotic near-optimality properties. Kino-PAX^+^ builds a sparse trajectory tree by decomposing the SBMP iterative operations--node selection, node extension, and node pruning--into three massively parallelized subroutines. Each subroutine is optimized for efficient execution on highly parallel processors and reduce communication overhead such as CPU-GPU interactions.

Kino-PAX^+^ adapts the GPU-based planner Kino-PAX to achieve massive parallelizatoin and draws inspiration from SST to focuses on promising nodes with low path costs in local neighborhoods for expansion. This enables pruning of nodes that do not contribute to good quality paths, iteratively improving the cost of the solutions. During each iteration of Kino-PAX^+^, multiple nodes from the existing tree are extended concurrently via random control sampling. This extension is governed by a spatial decomposition $\mathcal{R}$ to guide the search process and systematically optimize for low cost solutions. Additionally, this decomposition promotes thread independence during node addition and selection phases. After extensions are completed, non-promising nodes are pruned in parallel, and a new set of promising nodes with low cost is selected concurrently for expansion in the subsequent iteration. By continuously tracking the lowest-cost node per region, Kino-PAX^+^ progressively refines cost estimates, selecting only promising nodes for further propagation, and converges towards near-optimal solutions.

### III-A Core Algorithm

Figure 2: Illustration of the Kino-PAX+ expansion process: (a) Current node sets VA and VT. Numbers within grid cells indicate the lowest-cost trajectories reaching each region ℛi. (b) Parallel expansion of nodes in VA with branching factor λ = 2. (c) Addition of selected nodes to the unexplored set VU and corresponding updates to region costs. (d) Pruning of nodes from VA based on newly acquired trajectory cost information. (e) Updated active set VA, ready for the next iteration of node expansion.

Here, we provide a detailed description of Kino-PAX^+^ with pseudocode in Algorithms 1-4 as well as an illustration of one cycle of Kino-PAX^+^ in Figure 2. Kino-PAX^+^ organizes tree nodes into four distinct sets: $V_{A}$, $V_{I}$, $V_{T}$, and $V_{U}$. Specifically, $V_{A}$ contains nodes selected for parallel expansion (Algorithm 2); $V_{I}$ includes temporarily inactive nodes that may be reactivated for expansion in future iterations (Algorithm 3); $V_{T}$ comprises terminal nodes permanently pruned from the tree, and thus not considered in subsequent iterations (Algorithm 3); and finally, $V_{U}$ consists of newly generated promising nodes produced during node propagation (Algorithm 2). Additionally, Kino-PAX^+^ partitions the state space into distinct hyper-cube regions with diagonal length $\delta$, denoted by $\mathcal{R}$, and maintains the lowest-cost node within each region to guide efficient exploration.

### III-A1 Initialization

In Algorithm 1, Kino-PAX^+^ takes as input an initial state $x_{\text{init}} \in X_{\text{valid}}$, a goal region $X_{\text{goal}} \subseteq X_{\text{valid}}$, a maximum execution time $t_{\text{max}}$, a branching factor $\lambda$, and a maximum inactive node count $I_{\text{max}}$. In Lines 1-2, the initial state $x_{\text{init}}$ is set as the root node of the tree $\mathcal{T}$ and placed into the active set $V_{A}$. The inactive set $V_{I}$, terminal set $V_{T}$, and unexplored set $V_{U}$ are initialized as empty. Lines 3-5 initialize each region in the spatial decomposition $\mathcal{R}$ with infinite cost, while the solution trajectory $\mathbf{x}$ is initialized as null with infinite cost.

Input: Initial state xinit, goal region Xgoal, planning time tm a x, parallel expansion λ, decomposition diagonal δ, inactivity threshold Im a x
Output: Near-optimal solution trajectory x
3𝒯← Initialize tree with root node xinit
5 Construct decomposition ℛ = {ℛi}i = 1N with diameter δ
7 Initialize x = n u l l with cost (x) = ∞

### III-A2 Node Extension

After initialization, the main loop of Kino-PAX^+^ begins (Algorithm 1, Lines 5-8). In each iteration, the Propagate subroutine (Algorithm 2, Figures 2(a) and 2(b)) propagates nodes in the active set $V_{A}$ using massive parallelism. The inputs to Propagate include $V_{A}$, $V_{U}$, $\mathcal{R}$, and parameter $\lambda \in {\mathbb{N}}^{+}$. Specifically, each node $x \in V_{A}$ undergoes $\lambda$ parallel expansions, resulting in a total of $\lambda \cdot {|V_{A}|}$ parallel threads, where $|V_{A}|$ denotes the cardinality of $V_{A}$. For each thread, a random control $u \in U$ and a duration ${dt} \in {(0,T_{\text{prop}}\rbrack}$ are sampled, with $T_{\text{prop}} > 0$ being a user-defined maximum propagation time. The node's state $x$ is then propagated using the system dynamics , generating a new candidate state $x^{\prime}$ (Algorithm 2, Lines 3-4, Figure 2(b)).

Subsequently, the validity of the trajectory segment between states $x$ and $x^{\prime}$, denoted $\overline{xx^{\prime}}$, is evaluated against $X_{\text{valid}}$. If the trajectory segment is valid, the spatial region $\mathcal{R}_{i}$ corresponding to the new state $x^{\prime}$ is identified (Algorithm 2, Line 6). The incremental cost from $x$ to $x^{\prime}$, i.e., ${cost}{(\overline{xx^{\prime}})}$, is computed, and the cumulative cost from the root $x_{\text{init}}$ to $x^{\prime}$ is updated accordingly (Algorithm 2, Line 7).

If the new state $x^{\prime}$ improves upon the previously recorded cost for region $\mathcal{R}_{i}$, the cost associated with that region is updated (Algorithm 2, Line 8). Furthermore, if $x^{\prime}$ remains the lowest recorded cost for region $\mathcal{R}_{i}$, it is added to the unexplored node set $V_{U}$ (Algorithm 2, Lines 9-10, Figure 2(c)). This selective admission criterion ensures that nodes added to $V_{U}$ consistently improve upon the best trajectories found, guiding the search toward near-optimal solutions while maintaining memory efficiency.

### Remark 1

To avoid data races when updating the region cost for $\mathcal{R}_{i}$, we perform the cost-update operation atomically. This ensures an ordering constraint on memory accesses, avoiding degenerate behavior.

### Remark 2

Since the Propagate subroutine executes as a parallel process, a thread may insert a node into the unexplored set $V_{U}$ even if another thread identifies a lower-cost trajectory to the same region. The higher-cost nodes introduced initially are removed during the UpdateTree subroutine, ensuring only the lowest-cost nodes remain in the tree $\mathcal{T}$.

3 Randomly sample u and d t
5 if the trajectory from x to x′ is valid then
7 ${{cost}{(\overline{x_{\text{init}}x^{\prime}})}}\leftarrow{{{cost}{(\overline{x_{\text{init}}x})}} + {{cost}{(\overline{xx^{\prime}})}}}$
8 ${cost{(R_{i})}}\leftarrow{\min{\{{cost{(R_{i})}},{{cost}{(\overline{x_{\text{init}}x^{\prime}})}}\}}}$
9 if ${{cost}{(\overline{x_{}x^{\prime}})}} = {cost{(R_{i})}}$ then

### III-A3 Node Selection

After propagating nodes in $V_{A}$, the algorithm executes the PruneNodes subroutine (Algorithm 1, Line 7; Algorithm 3), which classifies each node $x \in \mathcal{T}$ as active, inactive, or terminal based on newly acquired search information. This subroutine operates as a massively parallel procedure, assigning one thread per node.

4 if ${{cost}{(\overline{x_{}x})}} = {cost{(R_{i})}}$ and x ∈ VI then
10 if Ic o u n t (x) &gt; Im a x and ${{cost}{(\overline{x_{}x})}} = {cost{(R_{i})}}$ then
13 if ${{cost}{(\overline{x_{}x})}} &gt; {cost{(R_{i})}}$ then
17 if ∃ ancestor xp of x, ${{cost}{(\overline{x_{init}x_{p}})}} &gt; {cost{(R_{p})}}$ then

Each thread begins by mapping its node $x$ to its corresponding region $\mathcal{R}_{i}$ (Algorithm 3, Line 2). If a node $x \in V_{I}$ (currently inactive) no longer represents the lowest cost in its region, it is moved permanently to the terminal set $V_{T}$ (Algorithm 3, Lines 10-12). Conversely, if $x \in V_{I}$ remains the lowest-cost node in its region, its inactivity counter $I_{\text{count}}{(x)}$ is incremented (Algorithm 3, Lines 3-4). If this counter exceeds a user-defined threshold $I_{\text{max}}$, indicating prolonged inactivity without improvement in its region, node $x$ is reactivated and returned to the set $V_{A}$ for further expansion (Algorithm 3, Lines 5-7). This mechanism ensures essential nodes re-enter active exploration, maintaining completeness.

Nodes currently in $V_{A}$ are also evaluated for pruning. A node $x \in V_{A}$ is pruned and moved to $V_{T}$ if its trajectory cost exceeds the lowest recorded cost for its region (Algorithm 3, Lines 10-12). Alternatively, if node $x$ has the lowest cost within its region but any of its ancestor nodes exceeds the minimum recorded cost for their respective regions, node $x$ is moved to the set $V_{I}$ (Algorithm 3, Lines 13-15, Figure 2(d)). This selective pruning strategy enables Kino-PAX^+^ to concentrate computational resources on expanding a focused subset of promising nodes with a higher branching factor.

After pruning, the UpdateTree subroutine is invoked (Algorithm 1, Line 8; Algorithm 4). This subroutine concurrently removes nodes in $V_{U}$ that are not the minimum-cost nodes in their respective regions, adds the remaining nodes in $V_{U}$ to $\mathcal{T}$, and checks whether a better solution has been found. UpdateTree receives as input $\mathcal{T}$, $V_{A}$, $V_{U}$, and $\mathcal{R}$, with each thread responsible for processing a single node from $V_{U}$. Each thread retrieves the corresponding region $\mathcal{R}_{i}$ for its node $x$ (Algorithm 4, Line 2). If $x$ represents the lowest-cost node to reach region $\mathcal{R}_{i}$, it is added to both $V_{A}$ and $\mathcal{T}$ (Algorithm 4, Lines 3-4, Figure 2(e)). Subsequently, if node $x$ satisfies the goal criteria and its cost improves upon the current best-known solution, the solution trajectory $\mathbf{x}$ and its associated cost are updated accordingly (Algorithm 4, Lines 5-7).

Kino-PAX^+^ repeats the main loop of Propagate, PruneNodes, and UpdateTree until the user-defined time limit $t_{\text{max}}$ is exceeded, at which point the best-found solution trajectory $\mathbf{x}$ is returned. Figures 1 and 3 illustrate how Kino-PAX^+^ progressively improves the quality of its solution over time.

Figure 3: Three solutions found by Kino-PAX+ using 6D Double Integrator dynamics. Subfigure (a) is the first solution found, (b) is an intermediate solution, and (c) is the final solution found.

3 if ${{cost}{(\overline{x_{}x})}} = {cost{(R_{i})}}$ then
5 if x ∈ X and ${{cost}{(\overline{x_{}x})}} &lt; {{cost}{(\mathbf{x})}}$ then
6 x← $(\overline{x_{\text{init}}x})$
7 ${{cost}{(\mathbf{x})}}\leftarrow{{cost}{(\overline{x_{\text{init}}x^{\prime}})}}$

## Analysis

In this section, we establish that Kino-PAX^+^ achieves probabilistic $\delta$-robust completeness (Definition 2. ‣ IV Analysis ‣ Kino-PAX+: Near-Optimal Massively Parallel Kinodynamic Sampling-based Motion Planner")) and asymptotic $\delta$-robust near-optimality (Definition 3. ‣ IV Analysis ‣ Kino-PAX+: Near-Optimal Massively Parallel Kinodynamic Sampling-based Motion Planner")). We begin by defining required notions.

The *obstacle clearance* of a valid trajectory $\mathbf{x}$ is the minimum distance from $\mathbf{x}$ to the invalid set $X_{\text{invalid}} = {X \smallsetminus X_{\text{valid}}}$. The *dynamic clearance* of $\mathbf{x}$ is the maximum distance $\delta_{a}$ you can displace the start and end points of $\mathbf{x}$ such that a new, similar (within $\delta_{a}$ distance from $\mathbf{x}$) trajectory is feasible according to the dynamics in (see Definition 4 and Lemma 6 in for details). A trajectory is called $\delta$-robust if both of its obstacle and dynamic clearances are greater than $\delta$.

### Definition 2 (Probabilistic $\delta$-Robust Completeness)

Let $\mathbf{X}_{n}^{\text{alg}}$ denote the set of trajectories discovered by an algorithm alg at iteration $n$. Algorithm alg is probabilistically $\delta$-robustly complete, if for every motion planning problem where there exists at least one $\delta$-robust trajectory, the following holds for all independent runs:

### Definition 3 (Asymptotic $\delta$-robust Near-Optimality)

Consider the setting in Problem 1. ‣ II Problem Formulation ‣ Kino-PAX+: Near-Optimal Massively Parallel Kinodynamic Sampling-based Motion Planner") where there exists at least one $\delta$-robust trajectory. Let $c^{\ast}$ denote the minimum achievable cost over all $\delta$-robust solution trajectories. Let $Y_{n}^{\text{alg}}$ denote a random variable representing the minimum cost among all trajectories returned by algorithm alg after iteration $n$. The algorithm alg is asymptotically $\delta$-robust near-optimal if for all independent runs:

where $h:{{{\mathbb{R}}_{\geq 0} \times {\mathbb{R}}_{\geq 0}}\rightarrow{\mathbb{R}}_{\geq 0}}$ is a function of the optimum cost $c^{\ast}$ and the $\delta$ clearance such that ${h{(c^{\ast},\delta)}} \geq c^{\ast}$.

In what follows, we prove that Kino-PAX^+^ is both $\delta$-robust complete and asymptotic $\delta$-robust near-optimal. We leverage the concept of Covering Balls . That is, given a $\delta$, any valid trajectory $\mathbf{x}$ is covered by a sequence of balls of radius $\delta$. Let ${{\mathbb{B}}_{r}{(x)}} = {\{{x^{\prime} \in {\mathbb{R}}^{n}}\mid{{\|{x - x^{\prime}}\|} \leq \delta}\}}$ denote a ball of radius $r$ centered at point $x$.

### Definition 4 (Covering Balls)

For a $\delta$-robust trajectory $\mathbf{x}:{{\lbrack 0,T\rbrack}\rightarrow X_{\text{valid}}}$ and a given cost increment $C_{\Delta} > 0$, let $x_{0},x_{1},\ldots,x_{m}$ be a sequent of points on $\mathbf{x}$ such that ${{cost}{(\overline{x_{i}x_{i+1}})}} = C_{\Delta}$ for all $i \in {\{ 0,\ldots,{m - 1}\}}$. Then, the *covering ball sequence* ${{\mathbb{B}}{(\mathbf{x},\delta,C_{\Delta})}} = {\{{{\mathbb{B}}_{\delta}{(x_{0})}},\ldots,{{\mathbb{B}}_{\delta}{(x_{m})}}\}}$ is a set of $m + 1$ hyper-balls centered at those points with radius $\delta$.

Theorem 17 in guarantees that, using random control sampling, there exists a strictly positive probability $\rho_{\delta} > 0$ of generating a trajectory segment between consecutive balls that remains $\delta$-close to $\mathbf{x}$. To extend this result to Kino-PAX^+^, we align the sequence of covering balls with our spatial decomposition $\mathcal{R}$. We identify the sequence of regions corresponding to the optimal trajectory, formally defined as follows.

### Definition 5 (Optimal Trajectory Regions)

Consider a hyper-cube space decomposition $\mathcal{R}$ where each region $\mathcal{R}_{i} \in \mathcal{R}$ has diagonal length $\delta$. Let $\mathbf{x}^{\ast}$ be a $\delta$-robust optimal trajectory covered by the sequence ${{\mathbb{B}}{(\mathbf{x}^{\ast},\delta,C_{\Delta})}} = {\{{{\mathbb{B}}_{\delta}{(x_{0}^{\ast})}},\ldots,{{\mathbb{B}}_{\delta}{(x_{m}^{\ast})}}\}}$. The Optimal Trajectory Regions is a set of regions $\mathcal{R}^{\ast} = {\{{\mathcal{R}_{i}^{\ast} \in \mathcal{R}}\}}_{i = 0}^{m}$ such that $\mathcal{R}_{i}^{\ast}$ is the region that contains point $x_{i}^{\ast}$.

Figure 4: An illustration of a δ-robust optimal trajectory x* (yellow nodes), with nodes equally spaced in terms of cost increments of CΔ. Each node lies within a region ℛi, and the purple regions collectively form the Optimal Trajectory Regions set ℛ*.

Figure 4 depicts an example of Definition 5. ‣ IV Analysis ‣ Kino-PAX+: Near-Optimal Massively Parallel Kinodynamic Sampling-based Motion Planner"). We now show that Kino-PAX^+^ finds trajectory segments between consecutive regions in $\mathcal{R}^{\ast}$ with non-zero probability and bounded cost.

### Lemma 1

Given a $\delta$-robust optimal trajectory $\mathbf{x}^{\ast}$ with Optimal Trajectory Regions $\mathcal{R}^{\ast}$, the probability of Kino-PAX^+^ successfully propagating an arbitrary state $x \in \mathcal{R}_{i - 1}^{\ast}$ to a state $x^{\prime} \in \mathcal{R}_{i}^{\ast}$ such that the cost of the segment $\overline{xx^{\prime}}$ satisfies

is bounded below by a positive constant $\rho_{\mathcal{R}} > 0$.

### Proof

For the case where $R_{i - 1}^{\ast} = R_{i}^{\ast}$, we have that $x = x^{\prime}$, and the result trivially holds. We now consider the case when $R_{i - 1}^{\ast} \neq R_{i}^{\ast}$. From Theorem 17 , for any state in the covering ball ${\mathbb{B}}_{i - 1}$ and using random control sampling, there exists a strictly positive probability $\rho_{\delta}$ of successfully generating a trajectory segment to any state within ${\mathbb{B}}_{i}$ that is $\delta$-similar to the optimal segment. By definition, the diagonal length of region $\mathcal{R}_{i - 1}^{\ast}$ is $\delta$, implying $\mathcal{R}_{i - 1}^{\ast} \subseteq {\mathbb{B}}_{i - 1}$ (since ${\mathbb{B}}_{i - 1}$ has radius $\delta$). This implies that any valid node existing in $\mathcal{R}_{i - 1}^{\ast}$ is in the required covering ball ${\mathbb{B}}_{i - 1}$. Similarly, $\mathcal{R}_{j}^{\ast} \subseteq {\mathbb{B}}_{i}$. Thus, any state in $\mathcal{R}_{i - 1}^{\ast}$ can transition to states in $\mathcal{R}_{i}^{\ast}$ with probability $\rho_{\mathcal{R}} > 0$. Since this transition is $\delta$-similar to the optimal segment which has cost $C_{\Delta}$, the Lipschitz continuity of the cost function guarantees

Now, we present our main analytical result.

### Theorem 1

Kino-PAX^+^ is asymptotically $\delta$-robustly near-optimal.

### Proof

Consider $\delta$-robust optimal trajectory $\mathbf{x}^{\ast}$ with cost $c^{\ast} = {{cost}{(\mathbf{x}^{\ast})}}$ and its corresponding optimal trajectory regions $\mathcal{R}^{\ast} = {\{\mathcal{R}_{j}^{\ast}\}}_{j = 0}^{m}$ as defined in Definition 5. ‣ IV Analysis ‣ Kino-PAX+: Near-Optimal Massively Parallel Kinodynamic Sampling-based Motion Planner"). We proceed by induction to show that Kino-PAX^+^ generates a path along the Optimal Trajectory Regions $\mathcal{R}_{j}^{\ast}$ with accumulated cost $C_{j} \leq {{({C_{\Delta} + {K_{c}\delta}})} \cdot j}$. We first define the events:

$A_{j}^{(n)}$: On iteration $n$, Kino-PAX^+^ generates a trajectory $\mathbf{x}_{j}$ terminating in region $\mathcal{R}_{j}^{\ast}$ with cost satisfying ${{cost}{(\mathbf{x}_{j})}} \leq {{({C_{\Delta} + {K_{c}\delta}})} \cdot j}$.

$E_{j}^{(n)}$: By iteration $n$, Kino-PAX^+^ has generated at least one trajectory satisfying event $A_{j}^{(n)}$.

Base Case ($E_{0}^{(n)}$): The root node $x_{0} = x_{0}^{\ast} \in \mathcal{R}_{0}^{\ast}$ has cost 0, satisfying the bound for $j = 0$. Thus ${P{(E_{0}^{(n)})}} = 1$ for all $n \geq 1$.

Inductive Step (from $E_{j - 1}^{(n)}$ to $E_{j}^{(n)}$): Assume event $E_{j - 1}^{(n)}$ holds. Kino-PAX^+^ has a node in $\mathcal{R}_{j - 1}^{\ast}$ with cost $C_{j - 1} \leq {{({j - 1})}{({C_{\Delta} + {K_{c}\delta}})}}$. As $n\rightarrow\infty$, this node is selected for expansion infinitely often. By Lemma 1, there is a positive probability $\rho_{\mathcal{R}}$ of generating a trajectory segment from $\mathcal{R}_{j - 1}^{\ast}$ to $\mathcal{R}_{j}^{\ast}$ with cost bounded above by $C_{\Delta} + {K_{c}\delta}$. Then, two mutually exclusive scenarios arise:

Case 1 (Acceptance): Kino-PAX^+^ directly accepts trajectory $\mathbf{x}_{j}$ (or $\mathbf{x}_{j - 1} = \mathbf{x}_{j}$), as it achieves the lowest cost for its terminal region $\mathcal{R}_{j}^{\ast}$. This occurs with strictly positive probability $\gamma_{1} > 0$.

Case 2 (Rejection): Kino-PAX^+^ rejects trajectory $\mathbf{x}_{j}$ due to the existence of another trajectory $\mathbf{x}^{\prime}$ with a lower cost endpoint node already in region $\mathcal{R}_{j}^{\ast}$. Since the rejected trajectory $\mathbf{x}_{j}$ is $\delta$-optimal, the accepted trajectory $\mathbf{x}^{\prime}$ must also be $\delta$-optimal. Thus, even rejection results in having a $\delta$-optimal trajectory in region $\mathcal{R}_{j}^{\ast}$, and this case occurs with strictly positive probability $\gamma_{2} > 0$.

In either case, the region $\mathcal{R}_{j}^{\ast}$ is guaranteed to contain a node satisfying the $\delta$-bounded cost. Thus, ${\lim_{n\rightarrow\infty}{{\mathbb{P}}{(E_{j}^{(n)})}}} = {\gamma_{1} + \gamma_{2}} = 1$. By induction, the event $E_{j}^{(n)}$ holds for all segment indices $j$. We now derive the cost bound. From Lemma 1, each segment contributes an additive error of $K_{c}\delta$. Thus, for the $j$-th region, the accumulated cost of the trajectory $\mathbf{x}_{j}$ satisfies:

Let $m = {\lceil{c^{\ast}/C_{\Delta}}\rceil}$ be the index of the final region containing the goal state. We have that

Let $Y_{n}^{\text{alg}}$ denote the cost of the solution found by Kino-PAX^+^ at iteration $n$. The probability that the algorithm finds a solution satisfying this bound corresponds to the probability of the final event $E_{m}^{(n)}$:

As established in the inductive step, since the transition probability $\rho_{\mathcal{R}} > 0$, the event $E_{m}^{(n)}$ occurs almost surely as $n\rightarrow\infty$:

### Corollary 1

Kino-PAX^+^ solves Problem 1. ‣ II Problem Formulation ‣ Kino-PAX+: Near-Optimal Massively Parallel Kinodynamic Sampling-based Motion Planner") with a near-optimality parameter $\beta > 0$ (see Definition 1. ‣ II Problem Formulation ‣ Kino-PAX+: Near-Optimal Massively Parallel Kinodynamic Sampling-based Motion Planner")) if $\delta \leq {\frac{C_{\Delta}}{K_{c}}\beta}$.

### Remark 3

Explicitly computing the required (diagonal) $\delta$ for a specific $\beta$ is generally infeasible, as both the Lipschitz constant $K_{c}$ and the segmentation cost $C_{\Delta}$ of the optimal trajectory are unknown for general non-linear systems. This limitation is inherent to the analysis of asymptotically near-optimal planners such as SST. In practice, this theoretical result serves as a qualitative guideline rather than a quantitative rule: the term $\frac{\delta}{C_{\Delta}}$ represents the relative decomposition-based error of the algorithm. Since $\delta$ is a tunable parameter, the approximation error can be made arbitrarily small (${{\lim_{\delta\rightarrow 0}1} + \frac{K_{c}\delta}{C_{\Delta}}} = 1$), allowing Kino-PAX^+^ to approach optimality up to any arbitrary precision.

From Theorem 1, we establish that Kino-PAX^+^ is probabilistically $\delta$-robust complete.

### Theorem 2

Kino-PAX^+^ is probabilistically $\delta$-robust complete.

### Proof

This result follows directly from Theorem 1. ∎

## Experiments

We evaluate Kino-PAX^+^'s performance across four 3D environments using three dynamical systems. Three environments are taken from (Fig. 5a-c), while a fourth environment (Fig. 5d) is designed to test Kino-PAX^+^'s capability for planning in tight corridors over extended horizons. The robot dynamics considered are: (i) a 6D double integrator, (ii) a 6D Dubins airplane, and (iii) a 12D nonlinear quadcopter.

Figure 5: Considered Environments.

For each dynamical system and environment, we benchmark Kino-PAX^+^ against the GPU-based SBMP Kino-PAX and the serial SBMP algorithm SST. This comparison assesses Kino-PAX^+^'s time to first solution relative to Kino-PAX and evaluates its solution quality compared to SST. We additionally evaluated two tunable hyperparameters for Kino-PAX^+^: Kino-PAX^+^-large-$\delta$ and Kino-PAX^+^-small-$\delta$. These configurations vary the decomposition size $\delta$ and the pre-allocated expected tree size $t_{e}$^11^1$t_{e}$ is a parameter inherited from Kino-PAX defining the maximum number of nodes in GPU memory.. The Kino-PAX^+^-large-$\delta$ strategy uses a coarser decomposition and smaller expected tree sizes, emphasizing rapid first solutions and early termination. Specifically, for the 6D double integrator: $27,000$ regions; for the 6D Dubins airplane: 52,000 regions; and for the 12D nonlinear quadcopter: $10^{5}$ regions. Conversely, the Kino-PAX^+^-small-$\delta$ strategy uses $10^{7}$ regions for all systems.

We implemented Kino-PAX^+^ in CUDA C and performed benchmarks alongside Kino-PAX on an NVIDIA RTX 4090 GPU with 16,384 CUDA cores and 24 GB of RAM. The serial SBMP SST, implemented in C++ using OMPL, ran on an Intel i9-14900K CPU (base clock 4.4 GHz, 128 GB RAM).

### V-A Benchmark Results

Tables I-III III summarize results, presenting median first solution time, normalized median first solution cost, median final solution time, normalized median final solution cost, and the success rate across 100 queries.

Table I shows that, for the 6‑D double‑integrator, Kino-PAX^+^-large-$\delta$ reaches an first solution in under $11{ms}$ across all environments, comparable to Kino-PAX, which does so in under $8{ms}$. A comparison of their first solution times and solution quality over time is shown in Figure 6. Relative to SST, Kino-PAX^+^-large-$\delta$ finds the first solution $650 \times$, $1600 \times$, $1100 \times$, and $3300 \times$ faster in Environments a--d, respectively. On average, Kino-PAX^+^-large-$\delta$'s first solution cost is $65\%$ of SST's first‑solution cost. After $10{ms}$ of planning, Kino-PAX^+^-large-$\delta$ converges to a local optimum with an average cost that is $61\%$ of SST's first solution cost. In comparison, the fine-grained hyperparameter variant, Kino-PAX^+^-small-$\delta$, converges to a local optimum after an average of $160s$ of planning, achieving an average cost that is $55\%$ of SST's initial cost. Meanwhile, SST, after the full five‑minute duration, improves only to $84\%$ of its own initial cost. A visualization comparing SST with Kino-PAX^+^-large-$\delta$ and Kino-PAX^+^-small-$\delta$ is shown in Figure 7.

Table I: Benchmark results over 100 trials with a 300-second maximum planning time for the 6D double integrator system.

Figure 6: Planning performance of Kino-PAX and Kino-PAX+-large-δ on the 6D double integrator in Env. c over a 15 ms planning duration.

Figure 7: Performance of Kino-PAX+ (both variants) and SST on 6D double integrator in the Env. c. over a 300 s planning time.

Table II: Benchmark results over 100 trials with a 300-second maximum planning time for the Dubins Airplane system.

For the Dubins Airplane system in Table II, we see largely similar results, where Kino-PAX^+^-large-$\delta$ achieves first solutions on average $6000 \times$ faster than SST, with first solution costs that are $78\%$ of SST's first solution cost. Kino-PAX^+^-large-$\delta$ converges to solutions that are $72\%$ of SST's first solution cost, while Kino-PAX^+^-small-$\delta$ converges to solutions that are $65\%$ of the cost. Notably, in Env. d, only Kino-PAX^+^-small-$\delta$ is able to find a valid solution within the planning time. This environment posed a particularly challenging problem due to the Dubins Airplane system's large turning radius and the presence of long, narrow passages with tight turns. Due to its fine decomposition and large expected tree size, Kino-PAX^+^-small-$\delta$ is able to find an first solution in $4.3$ seconds and improve that solution by an additional $9\%$ over the five-minute planning period.

Table III: Benchmark results over 100 trials with a 300-second maximum planning time for the 12D Nonlinear Quadcopter system.

Figure 8: Planning performance of Kino-PAX+-small-δ, Kino-PAX+-large-δ, and Kino-PAX on the 12D nonlinear quadcopter system in the zig-zag environment d. over a 300 s planning duration.

Lastly, Table III and Figure 8 present the planning results for the 12D nonlinear quadcopter system. Both tuning variants of Kino-PAX^+^ consistently outperform SST across all evaluated metrics, including time to first solution, first solution cost, and final solution cost. In these experiments, SST successfully found solutions in only $84\%$, $53\%$, $42\%$, and $0\%$ of trials in environments a--d, respectively. In contrast, both Kino-PAX^+^-large-$\delta$ and Kino-PAX^+^-small-$\delta$ achieved a $100\%$ success rate across all environments. On average, Kino-PAX^+^-large-$\delta$ finds the first solution $750 \times$ faster than SST and with a cost that is $63\%$ of SST's first solution cost. It converges to a final solution that is $55\%$ of SST's first solution cost, while Kino-PAX^+^-small-$\delta$ converges to a final solution that is $51\%$ of SST's. In comparison, SST converges to a final solution that is $94\%$ of its own first solution cost.

Overall, Kino-PAX^+^ outperforms existing serial asymptotically near-optimal planners in *all* assessed metrics. Kino-PAX^+^-large-$\delta$ rapidly finds high-quality first solutions, achieving speeds thousands of times faster than SST and comparable to Kino-PAX. Additionally, Kino-PAX^+^-small-$\delta$ shows that the algorithm remains effective and reliable for extremely challenging problems. Finally, unlike Kino-PAX, Kino-PAX^+^ is consistently able to optimize towards the lowest final costs across all environments.

## Conclusion

We have introduced Kino-PAX^+^, a novel parallelized asymptotically near-optimal kinodynamic motion planner. Benchmark results show that initial solution times are orders of magnitude faster than those of existing asymptotically near-optimal kinodynamic SBMPs, with significantly lower initial solution costs. Furthermore, it consistently outperforms its predecessor, Kino-PAX, in solution costs. For future work, we plan to conduct deployments in real-world robotic systems.
