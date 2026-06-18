<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Motion Planning for Hundreds of Floating Robots

Topics include Multi-robot motion planning, Fleet coordination, Collision avoidance, Trajectory optimization, Decomposition methods, Floating robots, Parallel planning, Real-world deployment.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents a scalable motion-planning pipeline for large fleets of omnidirectional floating robots, where dense collision constraints would otherwise couple hundreds of agents. The approach builds a collision graph, decomposes interactions into clusters, solves them in parallel, and includes robustness mechanisms validated in simulation and real water-based deployments.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Planning collision-free motion for large robot fleets is difficult because collision avoidance induces strong inter-agent coupling that grows rapidly with team size. We consider omnidirectional floating robots on water, where choreographies are specified by sparse keyframes and an interactive tool must generate trajectories within seconds, even when transitions span minutes and thousands of time steps. We propose a scalable pipeline that builds a collision graph from an initialization, decomposes the coupled problem into interaction clusters, and solves clusters independently (and in parallel) with robustness mechanisms for common decomposition pathologies. We validate the approach in simulations up to 500 robots. The synthesized trajectories have also been deployed in two real-world demonstrations, on Lake Zürich with a fleet of 24 Way of Water crafts and at the Time Space Existence 2025 Venice Biennale.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Planning collision-free motion for fleets of hundreds of robots remains challenging because collision avoidance introduces strong inter-agent coupling that grows rapidly (often quadratically) with fleet size. We study this problem in the context of floating robots operating on water (see LABEL:fig:planning-cover), where a show is specified by sparse *keyframes*, identified by a specific fleet configuration. The planning problem is to compute, for every robot, a collision-free trajectory that is dynamically feasible (i.e., trackable by a low-level controller to $cm$ accuracy) and that satisfies the boundary conditions at the beginning and end of the transition. For an interactive show-planning tool, a designer will iteratively adjust sparse keyframes and expect near-immediate feedback on the resulting fleet motion. Since consecutive keyframes can be separated by several minutes, a single transition may span thousands of planning steps. To render trajectories smoothly and to match the execution/preview rate, the planner must therefore produce dynamically feasible, collision-free trajectories over thousands of time steps within a few seconds per each transition between keyframes.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast to aerial drone choreography, where robots move in a largely unobstructed *three-dimensional* workspace and can use vertical maneuvers (e.g., temporary altitude offsets) to deconflict dense transitions, floating robots are constrained to the water surface and therefore evolve on a planar manifold. As a result, coordination and collision avoidance become intrinsically harder for surface fleets than for 3D aerial displays, where large multi-robot choreography has been demonstrated with integrated planning and collision-avoidance pipelines.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Sequential convex programming (SCP) is a widely used workhorse for generating smooth, dynamically feasible, collision-avoiding trajectories by iteratively solving convex subproblems that form local inner approximations of nonconvex dynamics and collision constraints (often coupled with trust regions and/or penalty continuation). Conceptually, SCP traces back to classical nonlinear-programming work on inner-approximation methods. In robotics, early demonstrations include time-optimal car trajectory planning and coordinated multi-vehicle 3D-trajectory generation for fleets of flying drones. Subsequent work further systematized and popularized SCP for motion planning among obstacles---notably through TrajOpt-style formulations that pair convexification with practical penalty continuation and efficient collision checking. In multi-robot and formation settings, related SCP formulations have been used to compute coordinated 3D trajectories and to navigate robot teams among static and dynamic obstacles.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Beyond SCP, several complementary paradigms address multi-agent collision avoidance, each with its own tradeoffs. Reciprocal-velocity-obstacle methods such as ORCA provide distributed and reactive avoidance with formal pairwise safety guarantees under modeling assumptions, but no guarantee that robots reach the target states in the given time period. On discrete domains (e.g., graphs), conflict-based search tackles combinatorial coordination explicitly. Within continuous trajectory optimization, planners such as CHOMP and STOMP handle obstacles primarily through smooth cost terms and stochastic or gradient-based updates rather than feasibility-focused convexification, and other methods have approached the problem with distributed feedback optimization. More recently, scalable interaction modeling has been pursued via learning-based decentralized policies and neural control-barrier-function approaches. However, because continuous-time motion planning pipelines often require strict enforcement of boundary conditions and safety constraints (e.g., collision avoidance), SCP remains a widely used workhorse.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A widely adopted optimization pipeline for multi-agent trajectory generation and execution is the one adopted, which plans collision-free 3D-trajectories for fleets of flying drones using a simplified translational model, to be tracked by a low-level controller; see Fig.˜2. However, this modeling simplification alone does not resolve the central scalability bottleneck: as the fleet size grows, collision avoidance induces rapidly increasing inter-agent coupling (and, in many formulations, a quadratic number of pairwise interactions), which can make SCP-based planning computationally demanding at scale. In fact, these SCP formulations rely on the solution of several quadratic programs (QP) with complexity depending on the sparsity of the matrices involved. The number of collision constraints scales as $\binom{N}{2}K$, with $N$ robots and $K$ discretized time steps. For ${N = 500},{K = 1000}$, the typical QP s in these settings have approximately hundreds of millions of non-zero entries--an intractable amount, in particular for surface robots that cannot perform 3D maneuvers.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. We engineer and validate a scalable planning pipeline for large surface-robot fleets specified by sparse keyframes which is orders of magnitude faster than the traditional SCP and more robust, producing collision-free trajectories within a few seconds on all the tested scenarios. Specifically, • we introduce a hierarchical planner that builds a collision graph from an initialization and decomposes the problem into interaction clusters, enabling independent (and parallel) subproblem solves; • we introduce robustness and efficiency mechanisms for the decomposition (fast graph/cluster updates and handling of common pathologies such as cyclic inter-cluster dependencies), with ablations isolating the effect of each design choice; and • we improve cluster-level trajectory optimization introducing a reformulation in terms of the objective variable to improve the sparsity of the linearized QP and a dynamic time-scale selection to improve the robustness of the solver. We validated the full system in simulations up to 500 robots and 1000 time steps, and the synthesized trajectories have been deployed in two real-world demonstrations, on Lake Zürich and at the Time Space Existence 2025 Venice Biennale.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The planning problem", "weight": 1.0} -->

Our planning problem considers $N$ robots moving in ${\mathbb{R}}^{2}$ from initial positions ${\{ p_{0}^{(i)}\}}_{i = 1}^{N}$ to a set of goal positions ${\{ p_{1}^{(i)}\}}_{i = 1}^{N}$ over a fixed horizon of $T$ seconds, while avoiding collisions. We discretize the horizon into $K$ steps of duration $h = {T/K}$ seconds and let $p^{(i)}{\lbrack k\rbrack}$ denote the position of robot $i$ at the discrete time index $k$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The planning problem", "weight": 1.0} -->

Collision avoidance is enforced via the constraint ${\|{{p^{(i)}{\lbrack k\rbrack}} - {p^{(j)}{\lbrack k\rbrack}}}\|}_{2} \geq R$ for all $i \neq j$ and all $k$, where $R$ is a safety radius derived from the robot geometry; in this work we set $R = {0.8m}$. In our setting, the floating robots are omnidirectional and rapidly reach the commanded speeds. Thus, we can plan directly in a single-integrator model without imposing higher-order smoothness (e.g., jerk) constraints.

<!-- chunk {"id": "body-0012", "role": "body", "section": "The planning problem", "weight": 1.0} -->

In a typical choreography, only a subset of the robots is *manually* matched to specific target locations. Let $\mathcal{L} \subseteq {\{ 1,\ldots,N\}}$ be the set of labelled robots, $\mathcal{U} = {{\{ 1,\ldots,N\}} \smallsetminus \mathcal{L}}$ the unlabelled robots, and let the manual matching be encoded by an injective map $\sigma:{\mathcal{L}\rightarrow{\{ 1,\ldots,N\}}}$. We compute a complete allocation by solving the minimum-cost assignment problem (equivalently, an optimal transport problem between uniform discrete measures )

<!-- chunk {"id": "body-0013", "role": "body", "section": "The planning problem", "weight": 1.0} -->

The $+ \infty$ costs enforce the prescribed matches for labelled robots; for unlabelled robots, the Euclidean cost yields assignments with small total displacement, which empirically reduces large swaps and simplifies subsequent collision-free trajectory generation; see Fig.˜4.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Increasing the fraction of labelled robots, i.e., enlarging $\mathcal{L}$, provides a simple knob that trades off designer intent against automatic regularization. At one extreme ($\mathcal{L} = \varnothing$), the Euclidean cost in yields a global assignment with small total displacement, which in practice avoids swaps between robots, minimizing collisions. At the other extreme ($\mathcal{L} = {\{ 1,\ldots,N\}}$), the assignment is fully prescribed by the user. The latter configuration can be arbitrarily challenging for solvers, and robustness to these scenarios is an important feature of our pipeline. In practice, we observed that allocating as little as $10\%$ of the robots randomly--while allocating the remainder via --already injects enough entropy to produce visually appealing trajectories.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Remark 1", "weight": 1.0} -->

For solving the linear program we use the Hungarian algorithm, which results in sub-$ms$ solve time for fleets of $500$ robots in the most challenging configuration ($0\%$ labelled robots). Given the resulting allocation, we construct an initial (generally not collision-free) trajectory $\tau_{0} = {({p^{(i)}{\lbrack k\rbrack}})}_{k = {0,\ldots,K}}^{i = {1,\ldots,N}}$ by linear interpolation between initial and final positions.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Hierarchical Solver", "weight": 1.0} -->

At every timestep robots are spread in space and collisions have high spatio-temporal locality. To exploit this structure, we (i) identify *collision clusters* (groups of interacting robots), (ii) convert each cluster into a smaller *subproblem* that can be solved independently. Given the initialization $\tau_{0}$ from Section˜II, the hierarchical solver thus produces a sequence of fleet trajectories $\tau_{1},\tau_{2},\ldots$ until it obtains one that is collision free; see Fig.˜3. In the remainder of this section, we describe the key components of the pipeline.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Collision Graph", "weight": 1.0} -->

Given a trajectory $\tau_{l} = {({p^{(i)}{\lbrack k\rbrack}})}_{k = {0,\ldots,K}}^{i = {1,\ldots,N}}$, we construct a spatio-temporal graph $\mathcal{G} = {(\mathcal{V},{\mathcal{E}_{s} \cup \mathcal{E}_{t}})}$; see Fig.˜5. A node ${(k,i)} \in \mathcal{V}$ is created for every robot $i$ at every timestep $k$. We connect vertices based on two conditions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Collision Graph", "weight": 1.0} -->

If ${\|{{p^{(i)}{\lbrack k\rbrack}} - {p^{(j)}{\lbrack k\rbrack}}}\|}_{2} < R$, then ${({(k,i)},{(k,j)})} \in \mathcal{E}_{s}$ (*spatial edges*). If robot $i$ collides with at least one other robot at time $k$ and $k + 1$, then ${({(k,i)},{({k + 1},i)})} \in \mathcal{E}_{t}$ (*temporal edges*). Spatial edges capture *which* robots are involved in a collision and temporal edges capture *for how long*.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Collision Graph", "weight": 1.0} -->

Each connected component of $\mathcal{G}$ defines a *collision cluster* ${\mathcal{G}_{m} = {(\mathcal{V}_{m},\mathcal{E}_{m})}},{m = {1,\ldots,M}}$, with $M$ the number of identified clusters. Building the graph requires detecting all pairwise violations across all time steps. We use a per-timestep KD-tree data structure to query all pairs within distance $R$, avoiding the $\mathcal{O}{({N^{2}K})}$ cost of exhaustive combinatorial checking.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Experiment 1", "weight": 1.0} -->

We build the collision graph for the linearly-interpolated initialization on $100$ randomized configurations with $N = 500$ vehicles, $K = 1000$ and $20\%$ allocated randomly (cf. Section˜IV-A). *Results.* In Fig.˜6, we report the cumulative time to compute the collision detection over all time steps using a KD-tree and compare it with the time it would take if we were naively checking all pair-wise collisions (with and without vectorization) or using a spatial hashing (i.e., discretizing the plane into uniform grid cells and hashing each robot into a cell so that collision checks are restricted to robots in the same or adjacent cells). This experiment clearly indicates the advantages of using a KD-tree with an average speedup of nearly $2000 \times$ with respect to the pairwise collision checking.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Clustering", "weight": 1.0} -->

Collision clusters span only the timesteps at which violations occur. For effective re-planning, we expand each robot's temporal window within a cluster to give the optimizer additional freedom to plan collision-free detours. Concretely, for each robot $i$ in a collision cluster $\mathcal{G}_{m} = {(\mathcal{V}_{m},\mathcal{E}_{m})}$, let $k_{\min}^{(i)} = {\min{\{{{k \mid {(k,i)}} \in \mathcal{V}_{m}}\}}}$ and $k_{\max}^{(i)} = {\max{\{{{k \mid {(k,i)}} \in \mathcal{V}_{m}}\}}}$ be the earliest and latest collision timesteps of robot $i$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Clustering", "weight": 1.0} -->

We define the *buffered timeframe* for robot $i$ as ${\lbrack{\hat{k}}_{\min}^{(i)},{\hat{k}}_{\max}^{(i)}\rbrack} = {({\max{(0,{k_{\min}^{(i)} - B})}},\ldots,{\min{(K,{k_{\max}^{(i)} + B})}})}$, where $B \in {\mathbb{N}}$ is a hyper-parameter; in our work, we fix it to the number of discrete time steps that correspond to $3$ seconds. Each robot in a cluster thus carries an individual time window, and the expanded cluster ${\hat{\mathcal{G}}}_{m}$ is defined over the union of these per-robot windows.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Clustering", "weight": 1.0} -->

This buffering step can create overlaps between expanded clusters: there may exist $m \neq m^{\prime}$ and a robot $i$ such that $i$ appears in both ${\hat{\mathcal{G}}}_{m}$ and ${\hat{\mathcal{G}}}_{m^{\prime}}$ with overlapping buffered timeframes, so that solving the two subproblems independently would produce conflicting trajectory updates. We detect all such overlaps and merge the corresponding clusters using a union-find procedure. However, naively merging all overlapping clusters can yield subproblems that are too large and negate the benefit of parallelization.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Clustering", "weight": 1.0} -->

We therefore estimate the resulting subproblem complexity as ${S{(\hat{\mathcal{G}})}} = {{{nnz}{(P)}} + {{nnz}{(A)}}}$, the number of nonzero entries in the objective and constraint matrices of the linearized QP; see Section III-C. If merging two clusters would produce a component with ${S{(\hat{\mathcal{G}})}} > S_{\max}$, we split the group. Let ${\hat{\mathcal{G}}}_{1},\ldots,{\hat{\mathcal{G}}}_{P}$ denote the buffered subproblems whose union exceeds the threshold.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Clustering", "weight": 1.0} -->

We then keep $p^{\ast} = {\arg{\min_{p}S_{p}^{\ast}}}$ as a singleton and proceed with clustering. We repeat this procedure until all components satisfy $S \leq S_{\max}$ or are singletons.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experiment 2", "weight": 1.0} -->

We run the entire pipeline on $100$ randomized configurations with $N = 500$ vehicles, $K = 1000$ and $20\%$ allocated randomly (cf. Section˜IV-A) without the buffering and without the cap on the subproblem complexity, and compare the performances in terms of success rate and computation time with the base configuration. *Results.* Without buffering, the pipeline does not converge. Without the cap, subproblems merge uncontrollably in congested situations, resulting in intractable subproblems. The pipeline's robustness and performance can drop up to 30%.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-C Subproblem solving", "weight": 1.0} -->

Next, we look at how to solve the resulting subproblems, each described by a cluster ${\hat{\mathcal{G}}}_{m}$. We adopt the SCP framework of for generating collision-free trajectories. The trajectory of robot $i$ is affine in its control inputs; velocities $v^{(i)}{\lbrack k\rbrack}$ for the single-integrator model.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-C Subproblem solving", "weight": 1.0} -->

with the constraint matrix $C = {\lbrack{C_{box}^{\top}C_{coll}^{\top}}\rbrack}^{\top}$. The box inequality rows $C_{box}$ encode dynamics, initial and final position constraints, and box limits on the state and control inputs. The collision rows $C_{coll}$ enforce the non-convex collision avoidance constraint via a first-order Taylor expansion

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-C Subproblem solving", "weight": 1.0} -->

where $\overline{p}$ denotes the previous iterate and linearization point, and $R$ is the collision distance. The QP is solved iteratively using OSQP at default (tolerances: $10^{- 4}$) accuracy with updated linearizations until the trajectory improvement satisfies the prescribed tolerances; in this work we consider modest SCP accuracies (tolerances: $10^{- 3}$).

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-C Subproblem solving", "weight": 1.0} -->

In large-scale scenarios, certain subproblems can become numerically ill-conditioned, for instance in symmetric configurations. We mitigate this by perturbing the SCP initialization and, if a solve is infeasible, re-solving the subproblem with an adaptively coarsened discretization rate. The resulting trajectory is then interpolated to the global discretization and refined via a lightweight SCP polishing step, significantly increasing robustness for difficult configurations with labelled fractions above $10\%$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-C Subproblem solving", "weight": 1.0} -->

In the *direct shooting* formulation employed by and described so far, positions are obtained by integrating the full control history, ${p^{(i)}{\lbrack k\rbrack}} = {p_{0}^{(i)} + {h{\sum_{m = 0}^{k - 1}{v^{(i)}{\lbrack m\rbrack}}}}}$. Thus, each collision constraint row at timestep $k$ couples *all* $k$ preceding control inputs of both robots involved. Consequently, $C_{coll}$ comprises lower-triangular blocks, with $\mathcal{O}{({N^{2}K^{2}})}$ non-zero entries.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-C Subproblem solving", "weight": 1.0} -->

However, it is possible to substantially reduce the number of non-zero entries (and, thus, increase the efficiency of the OSQP solver) by adopting a *direct transcription* formulation that augments the decision vector: $\chi = {\lbrack{p^{{(i)}\top}{\lbrack k\rbrack}},{v^{{(i)}\top}{\lbrack k\rbrack}}\rbrack}_{i,k}^{\top} \in {\mathbb{R}}^{4NK}$. The dynamics become local equality constraints $C_{dyn}$ between consecutive time steps, and each collision row can be directly encoded in the pairwise positions. The dynamics constraints are then locally banded; see Fig.˜7. The complexity reduces from $O{({N^{2}K^{2}})}$ to $O{({N^{2}K})}$ at the cost of a larger decision vector.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiment 3", "weight": 1.0} -->

We compare the *direct shooting* and the *direct transcription* formulations on randomized collision to assess the performance. For $N \in {\{ 2,4,6,8,10,12\}}$ and a time horizon of $T = {10\sqrt{N/2}}$, we sample the initial and final positions for each robot uniformly inside a ball of radius ${r{(N)}} = {5\sqrt{N/2}}$. We repeat the experiment with $50$ different seeds. The time steps are kept constant $K = 100$ and all robots are labelled. Cluster dimensions are scaled so that the congestion density is maintained across the experiments. We run the experiment for the modest SCP tolerance. *Results.* We report the statistics of the computation time for the two methods across varying numbers of robots in Fig.˜8. Overall, the direct transcription formulation improves over the direct shooting by up to two orders of magnitude for the larger problem instances and is the one that we adopt.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-D Merging", "weight": 1.0} -->

After solving all subproblems in parallel, the local solutions are merged back into the global trajectory by overwriting each robot's state variables in its time window. The pipeline loop then rebuilds the collision graph and repeats. However, this procedure can introduce collisions elsewhere and possibly result in the pipeline oscillating on identical collision patterns. We detect such cycles by recording the signature $(\mathcal{R}_{m},{\lbrack k_{s},k_{e}\rbrack})$ of every subproblem at each iteration $\ell$, where $\mathcal{R}_{m} \subseteq {\{ 1,\ldots,N\}}$ and $\{ k_{s},\ldots,k_{e}\}$ is the time range of the subproblem.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-D Merging", "weight": 1.0} -->

A subproblem at iteration $\ell$ is declared cyclic if there exists an earlier iteration $\ell^{\prime} < \ell$ containing a subproblem with the same robot set $\mathcal{R}_{m}$ and an overlapping time range ${{\{ k_{s},\ldots,k_{e}\}} \cap {\{ k_{s}^{\prime},\ldots,k_{e}^{\prime}\}}} \neq \varnothing$. Upon cycle detection, all subproblems with robot set $\mathcal{R}_{j}$ satisfying ${\mathcal{R}_{j} \cap \mathcal{R}_{m}} \neq \varnothing$ are locked into a single joint subproblem for all iterations $\ell^{\operatorname{\prime\prime}} \geq \ell$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Examples", "weight": 1.0} -->

In this section, we provide representative examples in simulation and real-world deployments to illustrate the qualitative and quantitative behavior of the proposed pipeline. All the data is collected on a MacBook Pro with an M3 Pro chip and 32GB of memory.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-A Case study: Motion planning for 500 crafts", "weight": 1.0} -->

We consider a large-scale case study with $N = 500$ vehicles, $K = 1000$ timesteps and labelled robots from $0\%$ to $100\%$. The partial "manual" allocation is uniform at random over the robots and their target locations. As keyframe configurations we use a star, a heart, and the words "Way", "Water" and "of". For each pattern, vehicle positions are sampled by placing $N$ points with uniform spacing of $4.5m$ along the corresponding curve; the perimeters of the shapes are thus calculated to ensure uniform spacing. As the shapes have varying sizes we scale time horizons accordingly; the discretization rate is evaluated based on $K$ and the maximum distance any robot has to travel.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A Case study: Motion planning for 500 crafts", "weight": 1.0} -->

The position box is sized with a $40\%$ margin around the larger of the two initial and final shapes. We report the statistics over 50 planning repetitions for each ratio of labelled robots and each of the initial-terminal configurations in Fig.˜9. For each repetition we consider a different random seed to sample the "manual" allocation. The solver appears to be robust, with $100\%$ convergence rate up to $30\%$ labelled robots. For larger amounts of labelled robots the solver converges to a collision-free trajectory in $99\%$ of the instances. Overall, the speed of our planner--which is able to successfully find collision-free trajectories within seconds--allows for a smooth user experience during choreography planning. We visualize representative trajectories in Fig.˜11, showing time snapshots of the fleet as well as the aggregate spatial footprint of the motion over the full horizon. In general, the trajectories span a few hundred meters and take several minutes to complete.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Case study: Deployment of 24 robots on Lake Zürich", "weight": 1.0} -->

For the demonstration on Lake Zürich, we deployed a fleet of $24$ robots and choreographed transitions for $16$ robots spanning one to two minutes. Using our planner within the choreography tool, designers could iteratively adjust keyframes and re-synthesize collision-free, dynamically feasible trajectories within seconds per design iteration, despite individual transitions discretizing into more than 400 time steps. A picture from the live demonstration is shown in LABEL:fig:planning-cover, and one of the performed trajectories in Example 3 in Fig.˜11.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-C Case study: Deployment at the Time Space Existence 2025 Venice Biennale", "weight": 1.0} -->

For the demonstration at the Time Space Existence 2025 Venice Biennale, we deployed a fleet of $8$ robots and designed several keyframe-to-keyframe transitions. Using our planner within the choreography tool, designers could iteratively adjust keyframes and regenerate collision-free, dynamically feasible trajectories within $1$ to $2$ seconds per design iteration, despite the transition discretizing into more than $2000$ time steps. The final, executed trajectory comprised $2491$ steps and was computed in $1.23s$ with the proposed planner. A picture from the live demonstration is shown in Fig.˜10, and one of the performed trajectories in Example 4 in Fig.˜11.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We summarize our main contributions and directions for future work.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusion", "weight": 1.5} -->

*Contributions.* We studied the motion planning problem for large fleets of omnidirectional surface robots, motivated by interactive show design where a user iteratively edits sparse keyframes and expects collision-free trajectories within seconds, even when transitions span minutes and thousands of discretization steps. To address the core scalability bottleneck induced by collision constraints, we proposed an engineering-focused pipeline that (i) builds a collision graph from a fast yet effective initialization, (ii) decomposes the globally coupled problem into interaction clusters, and (iii) solves these clusters independently (and in parallel), while incorporating robustness mechanisms. At the cluster level, we further improved solve efficiency and robustness through a reformulation that increases the sparsity of the linearized QP s and a dynamic time-scale selection strategy.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We validated the full system in simulations up to 500 robots and 1000 time steps, and the synthesized trajectories have been deployed in two real-world demonstrations, on Lake Zürich and in Venice. We systematically engineered the pipeline with the support of extensive ablations that isolate the effect of each design choice. Across the tested scenarios, the resulting planner substantially reduces runtime compared to traditional monolithic SCP pipelines and enables the fast turnaround required for iterative choreography design.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

*Outlook.* On the optimization side, our cluster-level solver can be strengthened by exploring alternative subproblem parameterizations and solution spaces---for instance, planning directly in a contact space, or leveraging learned priors while enforcing feasibility via *hard*-constrained neural architectures so that safety and boundary conditions remain guaranteed. Moreover, both collision detection and subproblem solve time can be improved by exploiting parallelization over GPUs. On the choreography side, the allocation step offers a powerful handle to shape artistic intent: replacing the current cost structure $c_{ij}$ with richer, designer-controllable (and potentially learning-based) costs could encode style and incorporate human preference feedback to extend the framework to match the subjective notion of "visually-appealing" motion.
