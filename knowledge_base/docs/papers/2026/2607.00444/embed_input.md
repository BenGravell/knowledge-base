<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Spatiotemporal motion planning, especially in multi-robot settings, requires robots to reason about collision-free regions that change over time, which is challenging in continuous spaces when feasible regions are transient and geometrically constrained. We present an algorithmic framework based on graphs of space-time convex sets (ST-GCSs), where collision-free regions are represented as convex sets in space-time and trajectories correspond to paths on the graph together with continuous motions within the selected sets. We formulate time-optimal planning on ST-GCSs as a graph-search problem over path-indexed states and develop a best-first search solver that evaluates partial paths via continuous trajectory optimization, guided by admissible heuristics and dominance checks. We further present an Exact Convex Decomposition (ECD) scheme to reserve trajectory occupancies in space-time, enabling unified handling of dynamic obstacles and multi-robot interactions. For multi-robot motion planning, we integrate ST-GCS planning and ECD into prioritized planning methods and introduce a windowed coordination scheme to improve efficiency.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Extensive experiments on single-robot and multi-robot problems demonstrate substantial speedups over various planners while maintaining high solution quality, particularly in environments with narrow and transient feasible regions. Large-scale demonstrations further show that the proposed multi-robot motion planner can solve instances with up to 100 robots within only a few minutes.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Spatiotemporal motion planning is a core problem in robotics. A robot must move from a start state to a goal while avoiding both static obstacles and time-varying constraints induced by dynamic environments or other robots. This problem becomes particularly challenging in continuous domains when feasible regions are transient, geometrically constrained, and tightly coupled with time. Such conditions arise naturally in Multi-Robot Motion Planning (MRMP), where each robot must treat the trajectories of others as dynamic obstacles, as well as in single-robot planning tasks with moving obstacles or temporal constraints.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite extensive progress, existing approaches still struggle to provide efficient and reliable solutions in these settings. Sampling-based planners, such as PRM and RRT, and their spatiotemporal variants, offer modeling flexibility but rely on random exploration, which can be ineffective in capturing narrow or short-lived feasible regions in space-time. Their performance further degrades due to repeated collision checking in a time-augmented state space. Optimization-based approaches based on the Graph of Convex Sets (GCS) replace random exploration with deterministic reasoning over convex decompositions, but extending them to dynamic environments requires a unified treatment of time, velocity constraints, and dynamic obstacle avoidance. When formulated as a single large optimization, this leads to significant computational challenges.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we present a general framework for time-optimal spatiotemporal motion planning in continuous spaces with dynamic obstacles based on a novel graph representation, namely a Graph of Space-Time Convex Sets (ST-GCS), where vertices correspond to collision-free convex sets in space-time and edges encode nonempty intersections between sets. An ST-GCS extends a spatial GCS into the time dimension, allowing both geometric and temporal constraints to be captured within a single graph structure. A feasible trajectory then corresponds to a path on an ST-GCS together with a continuous trajectory constructed within the selected convex sets. This representation also provides a natural basis for spatiotemporal planning in dynamic environments and for multi-robot coordination, where planned robot trajectories can be incorporated back into the graph as reserved occupancies.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A key challenge in solving time-optimal planning on an ST-GCS by graph search is that the cost and feasibility of reaching a vertex cannot be determined solely by the vertex itself. Instead, they depend on the entire prefix path used to reach that vertex, since different paths induce different feasible arrival states and different continuation costs. As a result, standard shortest-path formulations that identify search states only by vertices are generally insufficient. To address this, we formulate planning on an ST-GCS as a graph search over path-indexed states, where each search node represents a partial path together with the corresponding optimal trajectory and its cost.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Building on this formulation, we develop a best-first search solver for planning on ST-GCSs and introduce several algorithmic components that together make it practical and scalable. The search repeatedly evaluates partial paths by solving the corresponding continuous trajectory optimization over the convex sets along that path. To improve efficiency, we design admissible heuristics over partial paths and develop reachability-based dominance checks, including a safe set-containment check that preserves optimality and two lightweight heuristic checks that are substantially faster while maintaining high solution quality in practice. In addition, we present the Exact Convex Decomposition (ECD) scheme to reserve the spatiotemporal occupancy of trajectories by updating an ST-GCS, thereby enabling a unified treatment of dynamic obstacles and inter-robot interactions. On top of this, we integrate ECD into prioritized planning methods for MRMP, and further introduce a windowed coordination scheme to improve efficiency in multi-robot coordination by focusing planning effort on the relevant time intervals.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate the proposed Windowed-PBS + BFS planner on large-scale and highly congested MRMP instances, solving a bottlenecked $50$-robot instance in $1.64$m and a dense $100$-robot instance in $1.60$m, which shows its scalability beyond the main benchmark range.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We summarize our contributions as follows: We formulate time-optimal spatiotemporal motion planning as a graph-search problem on ST-GCSs.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop a search-based solver that operates on path-indexed states, together with admissible heuristics and dominance checks tailored to searching ST-GCSs.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present the ECD scheme to reserve trajectory occupancies in arbitrary-dimensional space-time, enabling unified handling of dynamic obstacles and multi-robot interactions.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We integrate ST-GCS planning and ECD into prioritized planning methods for MRMP, and further introduce a windowed coordination scheme to improve efficiency in multi-robot coordination.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide extensive empirical evaluation demonstrating substantial speedups over optimization-based approaches and strong performance in challenging spatiotemporal scenarios.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

This work substantially extends our prior conference version as follows: The prior version formulates time-optimal motion planning on an ST-GCS as a unified optimization problem, whereas this work develops a search-based formulation on ST-GCSs with path-indexed states, pruning strategies, and heuristic guidance, resulting in orders of magnitude faster in practice.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

The prior version presents ECD in the original 3D setting arising from 2D spatial motion plus time, whereas this work generalizes ECD to arbitrary-dimensional space-time.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

The prior version integrates ST-GCS within prioritized multi-robot planning, whereas this work additionally introduces windowed coordination to improve efficiency in multi-robot coordination.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

This work also provides substantially more extensive empirical evaluation, including additional search ablations and real-robot experiments.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Spatiotemporal Motion Planning", "weight": 1.0} -->

Spatiotemporal motion planning treats time as part of the planning domain to handle moving obstacles with known trajectories. Grid-based methods reserve discrete space-time states; SIPP reasons over safe time intervals for discrete spatial occupancies; any-angle variants such as Zeta^∗^-SIPP combine safe intervals with any-angle search for time-optimal planning in dynamic environments; and state-lattice methods plan over spatiotemporal lattices built from continuous space and fixed motion primitives. Sampling-based planners lift RRT-, PRM-, and RRT^∗^-style methods into configuration--time space, validating sampled time-parameterized states or edges against moving obstacles over their execution intervals; they are flexible, but can struggle when feasible regions are narrow, short-lived, or repeatedly changing, and their runtime can be dominated by collision checking in the time-augmented state space. Recent work mitigates this issue by bringing safe-interval ideas from MAPF into sampling-based planning.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Spatiotemporal Motion Planning", "weight": 1.0} -->

In contrast, we plan on ST-GCSs: collision-free space-time is represented by convex sets connected through nonempty intersections, so reserved occupancies can be removed from an updatable free-space decomposition while continuous trajectory optimization remains available over remaining regions.

<!-- chunk {"id": "body-0021", "role": "body", "section": "MRMP", "weight": 1.0} -->

MRMP methods differ mainly in how they represent and resolve inter-robot conflicts. Coupled methods reason in composite configuration spaces. Coordinated PRMs explicitly construct products of individual roadmaps, dRRT-style methods explore implicit tensor-product roadmaps without materializing the full joint graph, and partially coupled methods such as M^∗^ plan independently when possible while expanding into higher-dimensional coupled search near conflicts. Decoupled and conflict-based methods improve scalability by using priorities, reservations, or constraints. Prioritized planning treats planned robots as moving obstacles in configuration--time space, cooperative pathfinding uses discrete space-time reservations, CBS separates high-level conflict resolution from low-level planning, and PBS searches over priority constraints rather than a fixed ordering. These ideas underlie MAPF variants including continuous-time MAPF, safe-interval planning on continuous-time roadmaps, and representation-optimal MRMP for heterogeneous robots in continuous spaces.

<!-- chunk {"id": "body-0022", "role": "body", "section": "MRMP", "weight": 1.0} -->

Recent MRMP work connects conflict-based coordination with sampling-based, kinodynamic, optimization, and control-based planning. Kinodynamic CBS incorporates motion primitives into CBS, while adaptive methods vary coupling online through adaptive robot coordination, kinodynamic adaptive coordination, or guidance-informed grouping. Other approaches use decentralized trajectory optimization, path retiming, CBS-guided MPC, or mixed-integer continuous formulations. Our MRMP planner is closest to prioritized planning, but each low-level query plans on an ST-GCS; after a robot is planned, ECD updates the ST-GCS to reserve its swept occupancy, so later robots plan in the remaining collision-free space-time and jointly reason about route choice, timing, and dynamic collision avoidance.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Planning on GCSs", "weight": 1.0} -->

GCSs combine graph structure with convex optimization for mixed discrete--continuous planning. They have been applied beyond cluttered Euclidean motion planning to non-Euclidean configuration spaces, temporal-logic and precedence-constrained planning, contact-rich manipulation, and guidance for downstream nonconvex trajectory optimization. These works demonstrate the breadth of GCS modeling, but mainly consider static, task-augmented, or contact-mode domains rather than a free-space representation repeatedly updated by moving obstacles and planned robot trajectories.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Planning on GCSs", "weight": 1.0} -->

GCS performance depends strongly on the convex decomposition of free space. IRIS grows large obstacle-free convex regions; visibility-graph clique covers and certified polyhedral decompositions improve coverage, certification, and scalability; and GPU-accelerated methods compute collision-free configuration-space convex sets online in changing environments. Our ECD scheme is complementary. It updates an ST-GCS by removing swept occupancies while maintaining a convex decomposition of the remaining collision-free space-time.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Planning on GCSs", "weight": 1.0} -->

Efficient GCS solving has also received substantial attention. Large safe-box planners exploit offline preprocessing with fast runtime shortest-path and convex-control subproblems, while search-based solvers such as GCS^∗^, implicit graph search, and A^∗^-GCS reduce reliance on one monolithic mixed-integer convex program over the full graph. Other variants address multi-query planning, shortest walks with repeated vertices, nonconvex-cost or parametrized-space objectives, fixed-sequence minimum-time motion through convex sets, and routing problems that couple discrete visitation order with continuous trajectories. Closest to our setting, Osburn et al. studies ST-GCS planning in dynamic environments and constructs GCS-compatible constraints, while Zhao et al. combines CBS with time-augmented GCS under a fixed time-step representation. Recent GCS work has expanded modeling scope and solver efficiency, but has not jointly addressed path-indexed search on ST-GCSs, occupancy reservation by convex-decomposition updates, and windowed multi-robot coordination.

<!-- chunk {"id": "body-0026", "role": "body", "section": "GCS Definition", "weight": 1.0} -->

We consider a robot with an $m$-dimensional state space, whose collision-free region is decomposed into a collection of convex sets. These spatial convex sets need not be disjoint. A GCS, denoted as $G=(V,E,\mathcal{X})$, is a connected graph representing such a convex decomposition, where $V$ is the vertex set, $E$ is the edge set, and $\mathcal{X}=\{X_{v}\}_{v\in V}$ is the collection of convex sets. Each vertex $v\in V$ corresponds to a convex set $X_{v}=\{\mathbf{x}\,|\,\mathbf{A}_{v}\mathbf{x}\preceq\mathbf{b}_{v}\}\subseteq\mathbb{R}^{m}$ of states. Each edge $e=(u,v)\in E$ indicates that $X_{u}\cap X_{v}\neq\emptyset$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "GCS Definition", "weight": 1.0} -->

Our use of GCS is slightly more restrictive than the original formulation of Marcucci et al., where constraints may be attached more generally to vertices and edges.

<!-- chunk {"id": "body-0028", "role": "body", "section": "GCS Definition", "weight": 1.0} -->

A path on $G$ is an ordered sequence of vertices $\pi=\langle v_{1},v_{2},\ldots,v_{l}\rangle$ where $(v_{i-1},v_{i})\in E$ for all $i=2,\ldots,l$. Unless otherwise stated, we consider simple paths, i.e., paths without repeated vertices. A trajectory associated with $\pi$ is a continuous curve obtained by concatenating local trajectory segments inside the convex sets along $\pi$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Motion Planning on GCSs", "weight": 1.0} -->

Given a start state $\mathbf{x}_{s}$ and a goal state $\mathbf{x}_{g}$, motion planning on a GCS $G=(V,E,\mathcal{X})$ asks for a trajectory from $\mathbf{x}_{s}$ to $\mathbf{x}_{g}$. Since the start and goal states may lie in multiple convex sets, we introduce auxiliary source and target vertices $v_{s}$ and $v_{g}$, with $X_{v_{s}}=\{\mathbf{x}_{s}\}$ and $X_{v_{g}}=\{\mathbf{x}_{g}\}$, connected to all start- and goal-containing vertices, respectively, and use these auxiliary vertices as the unique endpoints of the graph path. We introduce two sets of variables.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Motion Planning on GCSs", "weight": 1.0} -->

The binary edge-selection variables $\Phi=\{\phi_{e}\}_{e\in E}$ parameterize a path $\pi_{\Phi}$, where $\phi_{e}=1$ if and only if edge $e$ is selected by the path $\pi_{\Phi}$. The continuous variables $\mathbf{x}_{v},\mathbf{y}_{v}\in X_{v}$ represent the entry and exit states of the local trajectory segment inside $X_{v}$. For each vertex $v\in V$, let $\ell_{v}(\mathbf{x}_{v},\mathbf{y}_{v})$ denote a given local cost associated with vertex $v$. The motion planning problem on GCS can be written as: where $\mathcal{P}(v_{s},v_{g};G)$ denotes the set of simple paths in $G$ that start from $v_{s}$ and end at $v_{g}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Motion Planning on GCSs", "weight": 1.0} -->

The objective in Eqn. (1a) sums the local costs of the trajectory segments $\mathbf{x}_{v}\rightarrow\mathbf{y}_{v}$ along the selected path. Eqn. (1b) enforces that the selected edges form a valid simple path from the auxiliary source vertex to the auxiliary target vertex. This path constraint can be encoded using standard flow-conservation and degree constraints for routing problems, yielding a Mixed-Integer Convex Program (MICP). Eqn. (1c) enforces that each local segment lies inside the corresponding convex set. Since $X_{v}$ is convex, the straight-line segment $(\mathbf{x}_{v},\mathbf{y}_{v})$ is collision-free. Eqn. (1d) enforces continuity between consecutive local segments for every selected edge. Eqn. (1e) enforces the trajectory starts from and ends at the given start state and goal state, respectively.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Motion Planning on GCSs", "weight": 1.0} -->

As illustrated in Fig. 2, a feasible solution reconstructs a continuous, collision-free, piecewise-linear trajectory from $\mathbf{x}_{s}$ to $\mathbf{x}_{g}$ by chaining the local segments $\mathbf{x}_{v}\rightarrow\mathbf{y}_{v}$ along $v\in\pi_{\Phi}$. The above formulation focuses on kinematic feasibility, which aligns with the standard convention in the literature. Differential or kinodynamic constraints can be incorporated by augmenting the state space and adding suitable constraints, such as in Marcucci et al.. The formulation can also be adapted to a convex start set $X_{s}$ or a convex goal set $X_{g}$ by replacing the point constraints in Eqn. (1e) with set-membership constraints.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Path-Conditioned Optimization", "weight": 1.0} -->

Solving Eqns. (1a--1e) directly as an MICP can be computationally expensive. A useful subproblem is obtained by fixing the graph path and optimizing only the continuous variables along that path. This operation is commonly referred to as convex restriction and is used as a subroutine in several search-based solvers for graph optimization problems on GCSs.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Path-Conditioned Optimization", "weight": 1.0} -->

Given a path $\pi=\langle v_{1},v_{2},\ldots,v_{l}\rangle$ on $G$, we say that a trajectory $\tau$ is *conditioned on* $\pi$ if it is represented by an ordered sequence $\tau=\langle(\mathbf{x}_{v_{i}},\mathbf{y}_{v_{i}})\rangle_{i=1}^{l}$ of entry and exit states, where $\mathbf{x}_{v_{i}},\mathbf{y}_{v_{i}}\in X_{v_{i}}$ with continuity enforced between consecutive sets. Conditioning on a path $\pi$ fixes the binary variables $\Phi$ so that $\pi_{\Phi}=\pi$. The remaining optimization is the convex program over the continuous entry and exit states, given as follows: This is a convex program that off-the-shelf optimizers can efficiently solve whenever the local costs and set constraints are convex.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Path-Conditioned Optimization", "weight": 1.0} -->

If feasible, its solution defines the optimal trajectory conditioned on the fixed path $\pi$. For example, in Fig. 2, fixing $\pi=\langle v_{1},v_{2},v_{3},v_{4},v_{5}\rangle$ removes the discrete path-selection variables and optimizes only the entry and exit state variables along that path.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Spatiotemporal Planning on ST-GCSs", "weight": 1.0} -->

This section extends the GCS formulation in Sec. 3 to spatiotemporal motion planning. The key concept is a Graph of Space-Time Convex Sets (ST-GCS), where each convex set lies in the joint space of position and time. Planning on an ST-GCS allows dynamic-obstacle avoidance, variable arrival times, velocity limits, and time optimality to be handled within a unified graph-optimization problem.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Let $G=(V,E,\mathcal{X})$ denote an input ST-GCS, where $\mathcal{X}=\{X_{v}\}_{v\in V}$ is a collection of space-time convex sets. Each vertex $v\in V$ corresponds to a space-time convex set $X_{v}\subset\mathbb{R}^{m+1}$ that is collision-free from both static and dynamic obstacles. Each edge $(u,v)\in E$ indicates that $X_{u}\cap X_{v}\neq\emptyset$. As shown in Fig. 3, an ST-GCS can be initialized by extruding each given spatial collision-free convex set from time $0$ to an arbitrarily large but finite time limit $t_{\text{max}}$. In addition, the ECD scheme introduced in Sec. 6 can further remove the space-time occupancies of dynamic obstacles or previously planned robots, potentially subdividing the extruded sets.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Let $\mathbf{x}=(\mathbf{p},t)\in\mathbb{R}^{m+1}$ denote a space-time state, where $\mathbf{x}.\mathbf{p}\in\mathbb{R}^{m}$ is the spatial position and $\mathbf{x}.t\in\mathbb{R}$ is the time. Within each space-time convex set $X_{v}$, the local trajectory segment $\mathbf{x}_{v}\rightarrow\mathbf{y}_{v}$ is linear in space-time, that is, traversed at a uniform speed but may vary across different sets.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

For each query, we consider a start space-time state $\mathbf{x}_{s}$ and a goal spatial position $\mathbf{p}_{g}$, with an unconstrained arrival time. To avoid treating multiple start- or goal-containing vertices specially, we augment $G$ with a single auxiliary start vertex $v_{s}$ and a single auxiliary goal vertex $v_{g}$. In this work, we consider a single start state point $\mathbf{x}_{s}$ and define: More generally, $X_{v_{s}}$ can be any convex set of admissible start states. The auxiliary goal set contains all admissible goal states induced by $\mathbf{p}_{g}$. In this work, by convention, a solution must also allow the robot to remain at $\mathbf{p}_{g}$ after arrival until the time limit $t_{\text{max}}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We therefore define the auxiliary goal set by Thus, membership in $X_{v_{g}}$ certifies that the robot reaches $\mathbf{p}_{g}$ at a time from which it can safely remain there until $t_{\max}$ through the space-time collision-free region $\bigcup_{v\in V}X_{v}$ represented by $G$. If the query instead specifies a full goal state, or only requires reaching $\mathbf{p}_{g}$ without remaining there, the definition of $X_{v_{g}}$ can be modified directly while the rest of the formulation remains unchanged.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Given a component-wise velocity bound $\mathbf{v}_{\mathrm{lim}}\in\mathbb{R}^{m}_{>0}$, the time-optimal spatiotemporal planning problem on the query-augmented ST-GCS $G^{\sharp}$ is written as: Eqn. (3a) minimizes the time cost $c(\tau)$, defined as the total elapsed time of trajectory $\tau$ reconstructed from the selected path $\pi_{\Phi}$ and continuous variables. Eqns. (3b--3d) folllow the graph topology, set membership, and continuity constraints from Eqns. (1b--1d), specialized to the query-augmented ST-GCS $G^{\sharp}$. Eqn. (3e) enforces time monotonicity within each selected convex set. Eqn. (3f) imposes component-wise velocity limits by bounding spatial displacement over elapsed time within each selected convex set. The auxiliary start and goal vertices encode the query through set membership and graph connectivity.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Since $X_{v_{s}}=\{\mathbf{x}_{s}\}$, the trajectory starts at $\mathbf{x}_{s}$. Since $X_{v_{g}}$ contains only states with spatial position $\mathbf{p}_{g}$, any feasible path ending at $v_{g}$ reaches the goal position. Under the goal-staying convention, membership in $X_{v_{g}}$ further guarantees that the robot can remain at $\mathbf{p}_{g}$ until $t_{\max}$. As illustrated in Fig. 3, a feasible solution reconstructs a continuous, space-time collision-free, piecewise-linear trajectory $\tau$ from $\mathbf{x}_{s}$ to some goal state $\mathbf{x}_{g}=(\mathbf{p}_{g},\cdot)$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Optimization-Based Solving", "weight": 1.0} -->

The formulation above can be solved as an MICP. The binary variables select a sequence of space-time convex sets, while the continuous variables optimize the entry and exit states within the selected sets. Time monotonicity, velocity limits, and continuity between consecutive local trajectory segments constrain these continuous states.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Optimization-Based Solving", "weight": 1.0} -->

Following Tang et al., we use two optimization-based variants as baselines in our experiments. The first, denoted by MICP, solves the mixed-integer program directly. The second, denoted by MICP(g), solves the continuous relaxation and then applies stochastic path rounding multiple times. Once a graph path is fixed, the remaining trajectory optimization is path-conditioned, as described in Sec. 3.3.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Graph Search on ST-GCSs", "weight": 1.0} -->

This section presents the search-based solver for spatiotemporal planning on ST-GCSs. We first define the path-indexed search space and explain why vertex-indexed shortest-path search is insufficient. We then justify excluding set revisitation under the piecewise-linear trajectory representation. Finally, we describe the best-first search solver, which repeatedly solves path-conditioned convex programs, uses admissible heuristics for guidance, and applies upper-bound pruning and dominance checks for pruning the search tree.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Search Space", "weight": 1.0} -->

In standard cost-minimal-path search on a discrete graph, such as A^∗^ search ), a search state is typically identified by the current vertex. This is valid because the graph has a vertex-level optimal substructure. Once the minimum cost-to-come to a vertex $v$ is known, any more expensive prefix ending at $v$ can be discarded, since all future costs depend only on $v$ and the remaining path.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Search Space", "weight": 1.0} -->

This vertex-level optimal substructure does not generally hold for motion planning on GCSs or ST-GCSs. The cost of a path is not the sum of fixed edge costs. Instead, once a vertex sequence is chosen, the continuous trajectory variables along the entire sequence are optimized jointly. Consequently, when a prefix path $\pi=\langle v_{s},\ldots,v\rangle$ is extended to $\pi^{\prime}=\langle v_{s},\ldots,v,w\rangle$, the optimal continuous states along the earlier part of the path, including the state at $v$, may change. Thus, the optimal trajectory conditioned on $\pi^{\prime}$ is not obtained by simply appending a locally optimal transition from $v$ to $w$ to the optimal trajectory conditioned on $\pi$. A prefix that is more expensive when considered only up to $v$ may still result in a lower-cost full trajectory after extension.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Search Space", "weight": 1.0} -->

Thus, search nodes for planning on ST-GCSs must be indexed by the full prefix path, rather than only by the arrival vertex. Let $\Pi$ denote the set of partial vertex paths on the query-augmented $G^{\sharp}$ that start from the auxiliary start vertex $v_{s}$. As justified in Sec. 5.2, we restrict $\Pi$ to paths that do not revisit a vertex.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Set Transition and Revisitation Exclusion", "weight": 1.0} -->

The candidate graph transition follows the topology of the query-augmented ST-GCS $G^{\sharp}$. For a vertex $v$, let denote its adjacent vertices. By construction of $G^{\sharp}$, $w\in\operatorname{Adj}(v)$ implies $X_{v}\cap X_{w}\neq\emptyset$. The temporal direction and velocity feasibility of an extended path are not imposed at the graph-transition level, but are instead enforced by the path-conditioned convex program.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Set Transition and Revisitation Exclusion", "weight": 1.0} -->

Unlike a monolithic GCS optimization, which needs additional machinery to explicitly allow repeated visits to the same convex set, graph search can naturally represent such paths by allowing the same vertex to appear multiple times in a prefix path. However, for the piecewise-linear trajectory representation and time-cost objective as described in Sec. 4.1, such set revisitation is unnecessary. Intuitively, if a trajectory enters the same convex set more than once, then the portion between the first entry and the later exit can be replaced by a single line segment inside that set with no higher cost.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Best-First Search (BFS) Solver", "weight": 1.0} -->

We now present the BFS solver for spatiotemporal planning on ST-GCSs. Given an input ST-GCS $G=(V,E,\mathcal{X})$ and a query $(\mathbf{x}_{s},\mathbf{p}_{g})$, the solver first applies QueryAugment to construct the query-augmented ST-GCS $G^{\sharp}=(V^{\sharp},E^{\sharp},\mathcal{X}^{\sharp})$ from Sec. 4.1. It then searches over path-indexed nodes and returns a solution trajectory if one is found. Optionally, it can take a feasible incumbent trajectory $\tau_{\text{ub}}$ with cost $c_{\text{ub}}$; if the search exhausts OPEN without finding a better trajectory, this incumbent is returned. The optimality guarantee depends on the heuristic inflation factor, the validity of the incumbent upper bound, and whether the selected dominance check is safe.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Best-First Search (BFS) Solver", "weight": 1.0} -->

Input: ST-GCS G = (V, E, 𝒳), query (xs, pg) Param: admissible heuristic h, inflation factor ϵ ≥ 1, valid incumbent pair (cub, τub) ← (+∞, ∅), dominance check δ ← δ∅ Output: solution trajectory if one exists 1 $(G^{\sharp},v_{s},v_{g})\leftarrow\textsc{QueryAugment}(G,\mathbf{x}_{s},\mathbf{p}_{g})$ 2 τr← zero length trajectory at xs 4 OPEN ← [Nr] ⊳ min-heap prioritized by N.f 5 initialize S(v) ← ∅ for each vertex v ∈ V♯ 12 foreach w ∈ Adj (N.v) with w ∉ N.π do 14 $(\tau,g)\leftarrow\textsc{PathOptimize}(G^{\sharp},\pi)$ 17 if Nchild.f < cub and not δ(Nchild, S(w)) then 18 Update

<!-- chunk {"id": "body-0053", "role": "body", "section": "Best-First Search (BFS) Solver", "weight": 1.0} -->

S(w) with Nchild 19 OPEN.add(Nchild) 22 return τub and “no better solution found” 25 return “no solution found”; 28 construct the path-conditioned convex program by fixing πΦ = π in Eqns.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Best-First Search (BFS) Solver", "weight": 1.0} -->

(3a–3f) 29 solve the resulting convex program 30 return the optimal trajectory τ conditioned on π and its cost g = c(τ), or report infeasibility Algorithm 1 Best-First Search on an ST-GCS Alg. 1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets") summarizes the procedure. The solver creates the root node $N_{r}$ corresponding to the trivial path $\langle v_{s}\rangle$, inserts into OPEN, and stores it in $S(v_{s})$ (Lines 1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")--1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Best-First Search (BFS) Solver", "weight": 1.0} -->

The map $S$ defined by $S(v)=\{N\,|\,N.v=v\}$ records the accepted search nodes that arrive at each vertex $v$. These stored nodes are used by dominance checks. At each iteration, the solver expands the node $N$ with the smallest $f$-value in OPEN (Lines 1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")--1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Best-First Search (BFS) Solver", "weight": 1.0} -->

If $N.v=v_{g}$, the stored trajectory $N.\tau$ is returned as a solution (Lines 1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")--1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")). Otherwise, the solver expands $N$ by considering each adjacent vertex $w$ of $N.v$ that does not already appear in $N.\pi$ (Lines 1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")--1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Best-First Search (BFS) Solver", "weight": 1.0} -->

For each extended path $\pi=N.\pi\oplus\langle w\rangle$, the solver calls PathOptimize to solve the corresponding path-conditioned convex program. If the program is feasible, a child node is created (Lines 1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")--1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")). The child node is discarded if its key is no smaller than the input cost upper bound $c_{\text{ub}}$, or if the dominance check $\delta$ certifies that it is dominated by accepted nodes in $S(w)$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Best-First Search (BFS) Solver", "weight": 1.0} -->

Otherwise, the child node is inserted into both $S(w)$ and OPEN, and previously accepted nodes in $S(w)$ that are dominated by the child node are removed (Lines 1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")--1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")). If OPEN becomes empty, the solver returns the incumbent trajectory $\tau_{\text{ub}}$ if one was provided; otherwise, it reports failure (Lines 1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")--1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Upper-Bound Pruning with $c_{\\text{ub}}$", "weight": 1.0} -->

Alg. 1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets") uses an optional input cost upper bound $c_{\text{ub}}$ to avoid exploring nodes that cannot improve the current incumbent, inspired by the spatial GCS search. If no incumbent is available, it uses $c_{\text{ub}}=+\infty$ and $\tau_{\text{ub}}=\emptyset$. If $c_{\text{ub}}<+\infty$, it must be paired with a corresponding feasible incumbent trajectory $\tau_{\text{ub}}$ for the same query, with $c(\tau_{\text{ub}})=c_{\text{ub}}$. This ensures that, if all remaining nodes are pruned by the upper-bound test, the solver can still return a valid trajectory.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Upper-Bound Pruning with $c_{\\text{ub}}$", "weight": 1.0} -->

We obtain $\tau_{\text{ub}}$ using a fast vertex-indexed best-first search on the same query-augmented ST-GCS $G^{\sharp}$. This auxiliary search still generates graph paths and calls PathOptimize to validate each path and compute its trajectory, but it applies the standard duplicate-pruning rule from graph search. For each arrival vertex, it keeps only the lowest-cost node found so far and discards later nodes arriving at the same vertex with no smaller cost. As discussed in Sec. 5.1, this vertex-indexed pruning is not sound for optimal planning on ST-GCSs, as future costs depend on the entire prefix path. We therefore use this auxiliary search only to obtain a feasible incumbent. If it reaches $v_{g}$, the returned trajectory is feasible because it is produced by PathOptimize, and its cost provides a valid $c_{\text{ub}}$ for Alg. 1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets").

<!-- chunk {"id": "body-0061", "role": "body", "section": "Pruning with Dominance Checks $\\delta$", "weight": 1.0} -->

We now define the dominance relation used by the optional check $\delta$ on Line 1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets") of Alg. 1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets"). Since search nodes are path-indexed, dominance is defined through the path-conditioned optimal solution cost $J^{*}(\cdot)$ (Definition 2. ‣ 5.1 Search Space ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")). Consider two search nodes $N$ and $N^{\prime}$ with the same arrival vertex $v$. We say that $N^{\prime}$ dominates $N$ if $J^{*}(N^{\prime}.\pi)\leq J^{*}(N.\pi)$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Pruning with Dominance Checks $\\delta$", "weight": 1.0} -->

A dominance check $\delta(N,S(N.v))$ is *safe* if it returns true only when there exists a retained node $N^{\prime}\in S(N.v)$ that dominates $N$. Safe checks are sufficient but may be conservative. They need not detect all dominated nodes, and they only compare nodes pairwise rather than detecting whether a set of nodes jointly dominate another node. In contrast, *heuristic* dominance checks may prune without certifying this relation and therefore do not by themselves preserve the theoretical guarantee.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Optimality with Safe Pruning", "weight": 1.0} -->

The following theorem states the optimality guarantee for Alg. 1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets") when the pruning operations used on Line 1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets") are safe.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Pairwise Dominance Checks", "weight": 1.0} -->

We now present three pairwise dominance checks as the optional check $\delta$ used in Alg. 1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets"). Throughout this subsection, let $N$ be a newly generated node and $N^{\prime}\in S(N.v)$ be a retained node with the same arrival vertex $v=N.v=N^{\prime}.v$. The trivial case is $v=v_{g}$, where both nodes already represent solution trajectories, and exact dominance reduces to directly comparing their trajectory costs. The checks below are therefore described for non-goal vertices $v\neq v_{g}$. Each check compares $N$ only with each retained node $N^{\prime}$, rather than testing whether several retained nodes jointly dominate $N$. This pairwise restriction affects pruning power but not correctness when the check is safe.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Pairwise Dominance Checks", "weight": 1.0} -->

Recall from Sec. 5.3.2 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets") that $N^{\prime}$ dominates $N$ if $J^{*}(N^{\prime}.\pi)\leq J^{*}(N.\pi)$. A dominance check is safe if it returns true only when this dominance relation is guaranteed to hold for some $N^{\prime}\in S(N.v)$. Among the three checks below, $\delta_{\text{set}}$ is safe, while $\delta_{\text{state}}$ and $\delta_{\text{pos}}$ are heuristic checks that trade optimality guarantees for stronger empirical pruning.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Safe Set-Containment Check $\\delta_{\\text{set}}$", "weight": 1.0} -->

The set-containment check $\delta_{\text{set}}$ certifies dominance by showing that $N^{\prime}$ can reach every state that an $N.\pi$-consistent trajectory may reach after entering the shared vertex $v$. Let $N.\pi=\langle v_{s},\ldots,u,v\rangle$ and define the arrival set The set $R_{N}$ contains all states that any $N.\pi$-consistent solution trajectory may use to enter $v$. Continuity (Eqn. (1d)) requires membership in the predecessor interface $X_{u}\cap X_{v}$, and $N.\mathbf{x}.t$ is the earliest arrival time achieved by the path-conditioned optimum for $N.\pi$. For a space-time state $\mathbf{x}$, define its forward reachable generalized cone under the velocity limits by Thus, $C(\mathbf{x})$ contains all states reachable from $\mathbf{x}$ by a single time-forward segment satisfying the velocity bounds.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Safe Set-Containment Check $\\delta_{\\text{set}}$", "weight": 1.0} -->

Then $\delta_{\text{set}}$ is defined by | | $\displaystyle\delta_{\text{set}}(N,S)\equiv{}$ | $\displaystyle\exists\,N^{\prime}\in S(N.v),$ | | \(5\) | | | | $\displaystyle\textbf{s.t. }\forall\,\mathbf{x}\in R_{N},\;C(\mathbf{x})\subseteq C(N^{\prime}.\mathbf{x}).$ | | | In implementation, since $R_{N}$ is convex, it is sufficient to check whether every corner of $R_{N}$ lies in $C(N^{\prime}.\mathbf{x})$ by transitivity of the cone reachability relation under the same velocity limits.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Heuristic Arrival-State-Containment Check $\\delta_{\\text{state}}$", "weight": 1.0} -->

The arrival-state-containment check $\delta_{\text{state}}$ approximates $\delta_{\text{set}}$ by testing only the stored witness state $N.\mathbf{x}$, rather than all states in $R_{N}$. Then $\delta_{\text{state}}$ is defined by This check is cheaper than $\delta_{\text{set}}$ because it only compares two cones. It is heuristic since $N.\mathbf{x}$ is only the stored witness state of the prefix-optimal trajectory for $N.\pi$, while an optimal $N.\pi$-consistent solution trajectory may use a different state to enter $X_{N.v}$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Heuristic Position-Based Dominance Check $\\delta_{\\text{pos}}$", "weight": 1.0} -->

The set-containment check $\delta_{\text{set}}$ can be expensive because it reasons over all states in $R_{N}$. A cheaper alternative is to compare two prefixes only at a sampled spatial position $\mathbf{p}\in\{\mathbf{x}.\mathbf{p}\,|\,\mathbf{x}\in X_{N.v}\}$. For a generated search node $N$, let $J_{\mathbf{p}}(N.\pi)$ denote the cost of the optimal trajectory conditioned on $N.\pi$ whose terminal state in $X_{v}$ has spatial position $\mathbf{p}$, with $J_{\mathbf{p}}(\pi)=+\infty$ if no such trajectory exists. Then $\delta_{\text{pos}}$ is defined by This check can be strengthened by using multiple sampled positions.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Heuristic Position-Based Dominance Check $\\delta_{\\text{pos}}$", "weight": 1.0} -->

In the limiting case of covering all relevant positions in $X_{N.v}$, it can certify a safe pairwise dominance relation between $N$ and a retained node $N^{\prime}$. One can further extend the idea to certify joint dominance by allowing different retained nodes in $S(N.v)$ to dominate $N$ at different positions. These extensions are more expensive. Experimentally, we use only one sampled position, so $\delta_{\text{pos}}$ remains heuristic.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Comparison and Use with Upper-Bound Pruning", "weight": 1.0} -->

Fig. 5 illustrates the difference between the three pairwise dominance checks. The $\delta=\delta_{\text{set}}$ check reasons over all relevant states in $R_{N}$, $\delta_{\text{state}}$ only compares the stored witness states, and $\delta_{\text{pos}}$ compares the prefixes at sampled spatial positions. In our implementation, upper-bound pruning is applied before one of these dominance checks. When the input $\delta=\delta_{\emptyset}$ or $\delta=\delta_{\text{set}}$, the guarantee in Theorem 2. ‣ 5.3.3 Optimality with Safe Pruning ‣ 5.3 Best-First Search (BFS) Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets") applies.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Comparison and Use with Upper-Bound Pruning", "weight": 1.0} -->

When $\delta_{\text{state}}$ or $\delta_{\text{pos}}$ is used, the solver becomes heuristic and can run substantially faster, but the pruning no longer preserves the optimality guarantee. Combining upper-bound pruning with heuristic dominance checks is empirically effective but can make the search more likely to return the incumbent trajectory. The heuristic checks may remove nodes that would otherwise lead to a feasible solution, while the upper-bound test further restricts the search to trajectories with cost strictly below $c_{\text{ub}}$. Thus, a solution that the heuristic search might find without upper-bound pruning can be discarded if it is no better than the incumbent. In that case, Alg. 1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets") falls back to the stored incumbent trajectory $\tau_{\text{ub}}$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Comparison and Use with Upper-Bound Pruning", "weight": 1.0} -->

Among the two heuristic checks, $\delta_{\text{pos}}$ is usually more aggressive because it compares prefixes only through sampled spatial positions and may miss useful unsampled states. The check $\delta_{\text{state}}$ is also heuristic, but remains tied to the actual stored witness states through cone containment. This makes $\delta_{\text{pos}}$ generally more sensitive to upper-bound pruning, while $\delta_{\text{state}}$ tends to be more conservative in practice.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Admissible Heuristics", "weight": 1.0} -->

We now describe admissible heuristics for Alg. 1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets"). All heuristics below are defined to be zero when $N.v=v_{g}$, since $N.\tau$ is already a solution trajectory. Thus, the definitions in this subsection focus on non-goal nodes $N.v\neq v_{g}$. By Definition 3. ‣ 5.1 Search Space ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets"), an admissible heuristic must lower-bound the optimal remaining solution cost from a prefix path $N.\pi$, rather than the cost-to-go from the stored witness state $N.\mathbf{x}$ alone.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Admissible Heuristics", "weight": 1.0} -->

This distinction is important because $N.\mathbf{x}$ is only the stored witness state of the trajectory optimized for $N.\pi$; after extending the path, the optimal trajectory may pass through a different state in $X_{N.v}$. Thus, a heuristic evaluated from $N.\mathbf{x}$ can overestimate the optimal remaining solution cost for the path-indexed node, as illustrated in Fig. 6.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Admissible Heuristics", "weight": 1.0} -->

For a non-goal node $N$, we define the prefix interface which is a useful source set for computing heuristics, as any $N.\pi$-consistent trajectory must pass through some state in $I_{N}$ before continuing beyond the prefix.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Admissible Heuristics", "weight": 1.0} -->

A general way to construct admissible heuristics is to relax different subsets of constraints in the path-conditioned ST-GCS problem. The original problem enforces graph topology, set membership, continuity between adjacent sets, motion constraints, and the query-specific goal-position constraint. The three heuristics below represent different choices. The $h_{\text{mot}}$ heuristic keeps only the motion constraints, $h_{\text{tri}}$ keeps local set-membership and motion constraints but relaxes continuity across local transitions, and $h_{\text{tab}}$ uses precomputed true interface-to-set costs with an online correction to the query goal position.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Admissible Heuristics", "weight": 1.0} -->

Offline precomputation can use the static environment and any dynamic obstacles known before the query. Query-specific information, such as $\mathbf{x}_{s}$, $\mathbf{p}_{g}$, and $v_{g}$, is incorporated online after query augmentation. In MRMP, trajectories of previously planned robots are not known during offline preprocessing; the resulting ECD-updated ST-GCSs only remove feasible space, so lower bounds computed on the initial ST-GCS remain admissible relaxations, as discussed later in Sec. 7.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Admissible Heuristics", "weight": 1.0} -->

For the ST-GCS trajectory representation in Sec. 4.1, we define the following useful quantity for query-specific online computation. For a set $Y$ of space-time states, define the velocity-only travel-time lower bound to the query goal position by with value of $+\infty$ if $Y=\emptyset$, where $\oslash$ denotes element-wise division. Since the query specifies a goal position with free arrival time, all our heuristics estimate the cost to $\mathbf{p}_{g}$ rather than to a fixed goal state.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Motion-Only Heuristic $h_{\\mathrm{mot}}$", "weight": 1.0} -->

This heuristic relaxes all the graph-topology and set-membership constraints after the prefix and keeps only the motion constraints needed to reach goal $\mathbf{p}_{g}$. In a more general setting, $h_{\mathrm{mot}}$ is the minimum travel cost from some state in $I_{N}$ to any state with spatial position $\mathbf{p}_{g}$, subject only to the chosen motion constraints. For our ST-GCS trajectory representation, the retained motion constraints are time monotonicity and component-wise velocity limits. Therefore, $h_{\mathrm{mot}}$ is defined by This is a lightweight online heuristic. Compared with estimating from any state in $X_{N.v}$, using $I_{N}$ is stronger because it respects the predecessor--current-set interface induced by the prefix path.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Triplet-Relaxation Heuristic $h_{\\mathrm{tri}}$", "weight": 1.0} -->

This heuristic keeps the graph topology and local constraints within each convex set, but relaxes continuity between consecutive local transitions. A similar idea has been used by spatial GCS solvers. For each input-graph triplet $(u,v,w)$ with $u,v,w\in V$ and $u,w$ adjacent to $v$ in $G$, a local lower-bound cost is precomputed for moving through $X_{v}$ from the interface $X_{u}\cap X_{v}$ to the interface $X_{v}\cap X_{w}$, subject to the same local set-membership and motion constraints. In our piecewise-linear instantiation, this cost is computed offline by a local convex program over one segment inside $X_{v}$ with time monotonicity and velocity limits, denoted by $q(u,v,w)$. If no such segment exists, $q(u,v,w)=+\infty$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Triplet-Relaxation Heuristic $h_{\\mathrm{tri}}$", "weight": 1.0} -->

At query time, costs of query-specific triplets induced by the auxiliary goal vertex $v_{g}$ of the form $q(u,v,v_{g})$ are computed online by a local convex program similarly. For $N.\pi=\langle\ldots,u,v\rangle$, let $\Pi^{\text{suf}}_{N}$ denote the set of all the suffixes with its predecessor $u$, where each $\pi\in\Pi^{\text{suf}}_{N}$ is in the form of $\pi=\langle u,v=w_{0},\ldots,w_{l}=v_{g}\rangle$ ending at $v_{g}$. We define $h_{\mathrm{tri}}$ as the minimum accumulated relaxed triplet cost over $\Pi^{\text{suf}}_{N}$ by where the first term is omitted if $u=v_{s}$, and the summation is omitted if $l=1$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Triplet-Relaxation Heuristic $h_{\\mathrm{tri}}$", "weight": 1.0} -->

For the root node $N.\pi=\langle v_{s}\rangle$, it omits the first two triplets and minimizes over the first input-graph vertex $w_{1}$ after $v_{s}$. The minimization is computed online as a shortest-path problem on the induced triplet graph, e.g., by Dijkstra's algorithm.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Interface-to-Set Cost Table Heuristic $h_{\\text{tab}}$", "weight": 1.0} -->

This heuristic precomputes stronger lower bounds by solving interface-to-set problems offline and storing their solution costs in a table. For any input-graph interface $I=X_{u}\cap X_{v}$ with $u,v\in V$ and any input-graph vertex $w\in V$, let $d(I,w)$ denote the minimum trajectory cost of reaching any state in $X_{w}$ from any state in $I$, over all graph paths, subject to the same graph, set-membership, continuity, and motion constraints. These values can be precomputed offline for all interfaces and all vertices by running Alg. 1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets") to solve the corresponding interface-to-set problems. They are query independent because they start from input-graph interfaces and end at input-graph sets.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Interface-to-Set Cost Table Heuristic $h_{\\text{tab}}$", "weight": 1.0} -->

For a non-goal search node $N$, define the relaxed table-start value by The first two cases handle query-specific start interfaces by omitting the nonnegative cost from $\mathbf{x}_{s}$ to the first input-graph interface used by the cost table. For a non-goal $N$ with $N.v\notin\operatorname{Adj}(v_{g})$, we define the heuristic by If $N.v\in\operatorname{Adj}(v_{g})$, we instead set $h_{\mathrm{tab}}(N.\pi)=\rho(I_{N},\mathbf{p}_{g})$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Comparison and Maximum Heuristic $h_{\\text{max}}$", "weight": 1.0} -->

Fig. 7 illustrates the three heuristics above on an example query. They capture complementary relaxations of the optimal remaining solution cost from a prefix path. The maximum heuristic $h_{\text{max}}$ combines them by taking their pointwise maximum: This preserves the strongest available lower bound at each search node.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Trajectory Occupancy Reservation", "weight": 1.0} -->

This section presents the Exact Convex Decomposition (ECD) scheme for reserving piecewise-linear trajectory occupancies in an ST-GCS. Given the spatiotemporal occupancy of a moving object, such as a robot or a dynamic obstacle, ECD removes the occupied region from the relevant space-time convex sets and decomposes the remaining free space into convex subsets. The resulting ST-GCS can then be used for subsequent planning queries that must avoid the reserved trajectory in space-time.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Spatiotemporal Trajectory Occupancy", "weight": 1.0} -->

We assume that each moving object, including a robot or a dynamic obstacle, is represented by a piecewise-linear center trajectory $\tau=\langle\mathbf{x}_{1},\ldots,\mathbf{x}_{l}\rangle$ in $(m+1)$-dimensional space-time with radius $r>0$. At each time, the object is centered at the position $\mathbf{x}.\mathbf{p}$ of state $\mathbf{x}$ along $\tau$ and occupies a spatial collision body of hypercube Let $\Psi(\mathbf{x}_{i},\mathbf{x}_{i+1},r)$ be the parallelotope obtained by sweeping the spatial $\boxdot(\mathbf{x}.\mathbf{p},r)$ along each segment $\mathbf{x}_{i}\rightarrow\mathbf{x}_{i+1}$ of $\tau$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Spatiotemporal Trajectory Occupancy", "weight": 1.0} -->

A piecewise-convex spatiotemporal occupancy for trajectory $\tau$ with object radius $r$ can be defined by Consider a robot with radius $r$ and another moving object with trajectory $\tau$ and radius $r^{\prime}$. An ST-GCS without any intersections with $\Omega(\tau,r+r^{\prime})$ naturally represents the collection of the space-time collision-free space for the robot. In the next section, we introduce the ECD scheme, which aims to reserve (i.e., remove) any occupancy represented as in Eqn. from an ST-GCS. Fig. 8 ‣ 6 Trajectory Occupancy Reservation ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets") illustrates two piecewise-linear trajectories and their reserved occupancies in 1D and 2D spaces.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Exact Convex Decomposition (ECD)", "weight": 1.0} -->

ECD reserves trajectory occupancy on an arbitrary ST-GCS $G=(V,E,\mathcal{X})$ using a piecewise-linear trajectory $\tau=\langle\mathbf{x}_{1},\ldots,\mathbf{x}_{l}\rangle$ and a safe clearance parameter $R$ as input. As aforementioned, $R$ is typically the sum of the radii of two objects, with a positive offset if needed. For each parallelotope piece $\Psi(\mathbf{x}_{i},\mathbf{x}_{i+1},R)\in\Omega(\tau,R)$ of $\tau$, it may intersects multiple convex sets of $G$. On the other hand, a convex set of $G$ might also contain multiple parallelotope occupancy pieces.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Exact Convex Decomposition (ECD)", "weight": 1.0} -->

To account for above cases, ECD subdivides $\tau$ and constructs an ordered sequence of vertex--segments tuples $L_{v}=\langle(\mathbf{x}_{j},\mathbf{y}_{j})\rangle_{j=1}^{\eta_{v}}$ for each $v\in V$, such that for every $j=1,\ldots,\eta_{v}$, it satisfies that $\Psi(\mathbf{x}_{j},\mathbf{y}_{j},R)\cap X_{v}\neq\emptyset$ and that $\mathbf{y}_{j}.t\leq\mathbf{x}_{j+1}.t$ if $j\neq\eta_{v}$. Intuitively speaking, each sequence $L_{v}$ collects the time-sorted subdivided segments of $\tau$ whose occupancies intersect with $X_{v}\in\mathcal{X}$.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Exact Convex Decomposition (ECD)", "weight": 1.0} -->

Writing $\mathcal{L}$ for all collected vertex--segment tuples, we have Input: ST-GCS G = (V, E, 𝒳), piecewise-linear trajectory τ, safe clearance R Output: updated ST-GCS with Ω(τ, R) removed 3 Lv← vertex–segments tuple sequence of τ for v 9 foreach (A, b) ∈ the facets of Ψ(xj, yj, R) do 12 add vertex v′ to V′ and set Xv′ = X to 𝒳′ 14 add the Xv residuals defined in Eqn. to G′ 15 remove v and Xv from G′ 18 return updated ST-GCS G′ = (V′, E′, 𝒳′) Algorithm 2 Exact Convex Decomposition Figure 8: Reserved trajectory occupancy Ω(τ, r) in Eqn. and the ECD scheme. (a) A piecewise-linear trajectory τ = ⟨x1, x2, x3, x4⟩ in 2D space-time and its occupancy Ω(τ, r), represented as a union of parallelotopes.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Exact Convex Decomposition (ECD)", "weight": 1.0} -->

(b) The input 2D ST-GCS, together with the first separating hyperplanes induced by the occupancy parallelotopes. (c)–(d) Progressive ECD slicing of Xv. Previously used separating hyperplanes are shown in light dashed lines, and newly introduced hyperplanes are shown in black dashed lines. (e) The updated ST-GCS after ECD, whose convex sets partition Xv \ Ω(τ, r), overlaid with the trajectory and the outline of Ω(τ, r). (f) A 3D ST-GCS after ECD reservation, with a trajectory in red and its reserved occupancy overlaid.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Exact Convex Decomposition (ECD)", "weight": 1.0} -->

Alg. 2 ‣ 6 Trajectory Occupancy Reservation ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets") summarizes the ECD scheme. It starts by iterating each vertex $v\in V$ and collects the corresponding vertex--segments tuple sequence $L_{v}$ from $\tau$ (Lines 2 ‣ 6 Trajectory Occupancy Reservation ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")-2 ‣ 6 Trajectory Occupancy Reservation ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")).

<!-- chunk {"id": "body-0095", "role": "body", "section": "Exact Convex Decomposition (ECD)", "weight": 1.0} -->

If $L_{v}$ is not empty, ECD replaces $X_{v}$ by a convex decomposition of $X_{v}\setminus\Omega(\tau,R)$ (Lines 2 ‣ 6 Trajectory Occupancy Reservation ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")--2 ‣ 6 Trajectory Occupancy Reservation ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")) and removes the original $v$ and $X_{v}$ from $G^{\prime}$ (Line 2 ‣ 6 Trajectory Occupancy Reservation ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")).

<!-- chunk {"id": "body-0096", "role": "body", "section": "Exact Convex Decomposition (ECD)", "weight": 1.0} -->

For each segment $\mathbf{x}_{j}\rightarrow\mathbf{y}_{j}$ from $L_{v}$, it slices only the time-bounded subset $Y\subseteq X_{v}$ (Line 2 ‣ 6 Trajectory Occupancy Reservation ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")).

<!-- chunk {"id": "body-0097", "role": "body", "section": "Exact Convex Decomposition (ECD)", "weight": 1.0} -->

Using each facet of the parallelotope occupancy $\Psi(\mathbf{x}_{j},\mathbf{y}_{j},R)$ as the separating hyperplane (Line 2 ‣ 6 Trajectory Occupancy Reservation ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")), ECD creates outside convex pieces disjoint from the parallelotope (Line 2 ‣ 6 Trajectory Occupancy Reservation ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")) and updates the residual on the occupancy side (Line 2 ‣ 6 Trajectory Occupancy Reservation ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")).

<!-- chunk {"id": "body-0098", "role": "body", "section": "Exact Convex Decomposition (ECD)", "weight": 1.0} -->

By convention, each facet $(\mathbf{A},\mathbf{b})$ is formed such that the convex set $\{\mathbf{x}\mid\mathbf{A}\mathbf{x}\preceq\mathbf{b}\}$ contains parallelotope $\Psi(\mathbf{x}_{j},\mathbf{y}_{j},R)$. After the subdivision by each time-bounded $Y$, there remain three types of $X_{v}$ residuals that are outside the interiors of the time-bounded subsets $Y$ and thus need to be added back to $G^{\prime}$ if nonempty (Line 2 ‣ 6 Trajectory Occupancy Reservation ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")).

<!-- chunk {"id": "body-0099", "role": "body", "section": "Exact Convex Decomposition (ECD)", "weight": 1.0} -->

We define the three types of $X_{v}$ residuals as follows: Finally, ECD rebuilds the adjacency of $G^{\prime}$ by checking set intersections (Line 2 ‣ 6 Trajectory Occupancy Reservation ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")), and returns the updated ST-GCS $G^{\prime}$ (Line 2 ‣ 6 Trajectory Occupancy Reservation ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")). The ECD scheme is quite general and applies to various other motions that can be represented by a piecewise-linear space-time trajectory. For example, waiting or in-place turning can be encoded as a segment $(\mathbf{p},t)\to(\mathbf{p},t^{\prime})$ along $\tau$ and being reserved in the input ST-GCS.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Exact Convex Decomposition (ECD)", "weight": 1.0} -->

More importantly, as we will see in Sec. 7, pre-start and post-arrival waiting segments should be inserted into the beginning and end of every single-robot trajectory $\tau$, respectively. As a result, when planning on the ST-GCS with $\tau$ reserved by ECD, the other robots must avoid the robot that stays at the start and goal positions before and after executing $\tau$.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Multi-Robot Motion Planning", "weight": 1.0} -->

This section integrates spatiotemporal planning on ST-GCSs and ECD reservation for Multi-Robot Motion Planning (MRMP). The low-level solver solves single-robot queries one at a time with the BFS solver in Sec. 5, while the high-level coordinator resolves inter-robot conflicts by deciding which robot trajectories are reserved in each low-level call.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

We consider $n$ robots with the same radius $r$ sharing a given base ST-GCS $G_{0}=(V_{0},E_{0},\mathcal{X}_{0})$, which represents the collision-free space-time region before inter-robot reservations and may be constructed, for example, by extruding a spatial GCS through time and then applying the ECD scheme to remove occupancies of known dynamic obstacles. Each robot $i=1,2,\ldots,n$ has a query $(\mathbf{x}_{s,i},\mathbf{p}_{g,i})$ with $\mathbf{x}_{s,i}=(\mathbf{p}_{s,i},t_{s,i})\in\mathbb{R}^{m+1}$, where the arrival time at $\mathbf{p}_{g,i}$ is unconstrained.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

Therefore, we let $\tilde{\tau}_{i}$ denote its endpoint-augmented variant, defined as follows: A trajectory set $\mathcal{T}=\{\tau_{i}\}_{i=1}^{n}$ is feasible if and only if each $\tau_{i}$ is a feasible single-robot trajectory for query $(\mathbf{x}_{s,i},\mathbf{p}_{g,i})$ on $G_{0}$, and every robot pair is collision-free under the robot occupancy model defined in Eqn.: The MRMP problem seeks to find such a feasible trajectory set described above. We evaluate the MRMP solution quality by two common aggregate metrics, namely the sum-of-costs (SOC) and the makespan: where makespan is the maximum individual trajectory duration, excluding the pre-start waiting time.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

For notation, let $\operatorname{ECD}(G,\tau,R)$ denote the ST-GCS returned by Alg. 2 ‣ 6 Trajectory Occupancy Reservation ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets"). For an ordered list of trajectories, $\operatorname{ECD}(G,\langle\tau_{1},\ldots,\tau_{l}\rangle,2r)$ denotes the ST-GCS obtained by applying Alg. 2 ‣ 6 Trajectory Occupancy Reservation ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets") successively to $\tau_{1},\ldots,\tau_{l}$ in that order, with $\operatorname{ECD}(G,\langle\rangle,2r)=G$.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

It is worth noting that, for MRMP where the robots have different radii, we only need to construct an individual base $G_{0}$ for each robot and change the ECD clearance parameter accordingly, while the low-level single-robot solver and the following high-level coordination algorithms remain unchanged.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Prioritized Planning with ST-GCS and ECD", "weight": 1.0} -->

We instantiate Prioritized Planning (PP) in the ST-GCS setting using the BFS solver in Alg. 1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets") for low-level single-robot planning and ECD for trajectory reservation. We consider a total priority order $\boldsymbol{\sigma}=\langle\sigma_{1},\dots,\sigma_{n}\rangle$, where $\boldsymbol{\sigma}$ is a permutation of the robot indices $1,2,\ldots,n$. Robot $\sigma_{i}$ has higher priority than robot $\sigma_{j}$ if $i<j$. PP plans robots sequentially on progressively updated ST-GCSs. When planning for robot $\sigma_{k}$, the trajectories of robots $\sigma_{1},\sigma_{2},\dots,\sigma_{k-1}$ have already been planned and reserved.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Prioritized Planning with ST-GCS and ECD", "weight": 1.0} -->

Set $G^{}=G_{0}$. At iteration $k$, robot $\sigma_{k}$ is planned on $G^{(k)}$. The low-level solver solves the query $(\mathbf{x}_{s,\sigma_{k}},\mathbf{p}_{g,\sigma_{k}})$ on $G^{(k)}$, so the returned trajectory avoids all higher-priority trajectories, including their endpoint-staying portions. If this call fails, PP reports failure for the priority order $\boldsymbol{\sigma}$. Otherwise, after obtaining $\tau_{\sigma_{k}}$, PP updates the graph for the next iteration by After all robots have been processed, PP returns the solution set of trajectories.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Prioritized Planning with ST-GCS and ECD", "weight": 1.0} -->

We consider the base ST-GCS $G_{0}$ constructed by extruding a spatial GCS along the time dimension from $0$ to $t_{\text{max}}$. Without loss of generality, we assume no dynamic obstacles are present to analyze the MRMP solvability on ST-GCS. Let $t_{0}=\max_{i=1,\ldots,n}t_{s,i}$ defines the time when all robots are ready to move. In case there are dynamic obstacles, we shift $t_{0}$ to the time when all dynamic obstacles have reached their terminal positions and all robots are ready to go, and the rest analysis remains identical.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Prioritized Planning with ST-GCS and ECD", "weight": 1.0} -->

Let $\tau_{\text{stay}}(\mathbf{p},t)=\langle(\mathbf{p},t),(\mathbf{p},t_{\text{max}})\rangle$ denote the trajectory segment staying at position $\mathbf{p}$ from some time $t\leq t_{\text{max}}$ to $t_{\text{max}}$. We further define a sequence collecting the start and goal staying trajectories for all robots $j=j_{1},\ldots,j_{n-1}$ and $j\neq i$. We now define well-formedness conditions for MRMP instances that are sufficient for the completeness of PP on ST-GCS.

<!-- chunk {"id": "body-0110", "role": "body", "section": "PBS with ST-GCS and ECD", "weight": 1.0} -->

We instantiate Priority-Based Search (PBS) in the ST-GCS setting by using the BFS solver in Alg. 1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets") for low-level single-robot planning and ECD for reserving spatiotemporal occupancies. PBS searches over partial priority orders instead of committing to one total priority order. A PBS node $N$ stores a set $\bm{\boldsymbol{\prec}}_{N}$ of ordered robot pairs and a trajectory set $N.\mathcal{T}$. Let ${\prec}_{N}^{+}$ denotes the transitive closure of ${\boldsymbol{\prec}}_{N}$ such that if $i\prec^{+}_{N}j$, then robot $j$ must avoid robot $i$.

<!-- chunk {"id": "body-0111", "role": "body", "section": "PBS with ST-GCS and ECD", "weight": 1.0} -->

Namely, its trajectory $N.\tau_{j}$ can be obtained by planning on where $\langle i_{1},\ldots,i_{l}\rangle$ is any fixed topological ordering of the set $\{i\mid i\prec_{N}^{+}j\}$ of all high-priority robots. Here, $N.\tilde{\tau}_{i}$ denotes the endpoint-augmented reservation trajectory corresponding to the stored trajectory $N.\tau_{i}$. Unlike PP, PBS reserves only endpoint-augmented trajectories that are constrained to have higher priority than $j$. If two robots have no priority relation, neither is forced to avoid the other's endpoint-augmented trajectory until a collision introduces such a constraint.

<!-- chunk {"id": "body-0112", "role": "body", "section": "PBS with ST-GCS and ECD", "weight": 1.0} -->

Alg. 3 summarizes the procedure of PBS. It starts with an empty partial priority set and independently planned trajectories (Lines 3-3). PBS performs a depth-first search on a priority tree using STACK. When PBS selects a node $N$ from STACK, if the endpoint-augmented trajectories corresponding to $N.\mathcal{T}$ are pairwise collision-free, PBS returns it (Line 3). Otherwise, it identifies a colliding robot pair $i_{1},i_{2}$ whose endpoint-augmented trajectories $N.\tilde{\tau}_{i_{1}}$ and $N.\tilde{\tau}_{i_{2}}$ collide (Line 3). PBS then creates two child nodes by orienting this collision in both directions. One child adds $i_{1}\prec i_{2}$, and the other adds $i_{2}\prec i_{1}$ (Lines 3-3).

<!-- chunk {"id": "body-0113", "role": "body", "section": "PBS with ST-GCS and ECD", "weight": 1.0} -->

For any branch $(i,j)$, the child node $N^{\prime}$ adds $i\prec j$ and calls UpdateNode$(N^{\prime},j)$, where $j$ is the newly lower-priority robot. UpdateNode builds the replanning set $K$, containing $j$ and all robots whose higher-priority constraints may change after adding $i\prec j$ (Line 3). It then processes each robot $k\in K$ in a topological ordering of $\bm{\boldsymbol{\prec}}_{N^{\prime}}$.

<!-- chunk {"id": "body-0114", "role": "body", "section": "PBS with ST-GCS and ECD", "weight": 1.0} -->

If $N^{\prime}.\tilde{\tau}_{k}$ collides with $N^{\prime}.\tilde{\tau}_{i^{\prime}}$ of some higher-priority robot $i^{\prime}\prec_{N^{\prime}}^{+}k$, UpdateNode replans $\tau_{k}$ to respect all of higher-priority reservations of robot $k$ (Lines 3--3). If UpdateNode succeeds, PBS adds the child node $N^{\prime}$ to STACK (Lines 3--3). PBS returns failure if no valid solution can be found after exploring all nodes (Line 3).

<!-- chunk {"id": "body-0115", "role": "body", "section": "Node Evaluation and Ordering Rules (Lines 3-3 of Alg. 3)", "weight": 1.0} -->

PBS can vary how child nodes are generated and expanded. A child node is *generated* once its new priority relation is added, and it is *expanded* once UpdateNode has replanned the affected robots under that relation. With lazy evaluation, both child nodes are generated before calling UpdateNode; expansion is delayed until a generated child is selected for evaluation. This avoids spending low-level planning effort on generated nodes that may never be expanded. Alternatively, PBS can expand both child nodes immediately and order the expanded children by a metric. A metric of sum-of-costs or makespan favors branches with better current solution quality, while a metric of the number of pairwise conflicts favors less congested branches. These metric-based rules require immediate node expansion via UpdateNode and therefore are not compatible with lazy evaluation. Since Alg. 3 uses a stack, the favored expanded child is pushed after the other child so that it is selected first.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Reuse of Base ST-GCS Heuristic Values", "weight": 1.0} -->

In PP or PBS, the low-level solver is repeatedly called on ECD-updated ST-GCSs. The motion-only heuristic $h_{\text{mot}}$ is evaluated directly on the current query-augmented graph using the actual prefix interface $I_{N}$. In contrast, $h_{\text{tri}}$ and $h_{\text{tab}}$ rely on heuristic values computed on the base ST-GCS $G_{0}$, and we reuse these values on ECD-updated graphs through the corresponding base vertices and interfaces. Let $G=(V,E,\mathcal{X})$ be any ST-GCS obtained from $G_{0}$ by a finite sequence of ECD reservations, and consider any query-updated $(G^{\sharp},v_{s},v_{g})=\textsc{QueryAugment}(G,\mathbf{x}_{s},\mathbf{p}_{g})$.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Reuse of Base ST-GCS Heuristic Values", "weight": 1.0} -->

For every non-query vertex $v\in V$, let $\beta(v)\in V_{0}$ denote the base vertex of $G_{0}$ from which $v$ descends, so that $X_{v}\subseteq X_{\beta(v)}$. This map is inherited through ECD subdivisions. Initially $\beta(v)=v$ for $v\in V_{0}$, and when ECD subdivides a vertex $v$ into new vertices, each new vertex $w$ is assigned $\beta(w)=\beta(v)$. Specifically, we define $\beta(v_{s})=v_{s}$ and $\beta(v_{g})=v_{g}$ for the auxiliary query vertices.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Reuse of Base ST-GCS Heuristic Values", "weight": 1.0} -->

Consider a non-goal search node $N$ generated on $G^{\sharp}$, and write its prefix as $N.\pi=\langle v_{0},\ldots,v_{l}\rangle$, where $v_{0}=v_{s}$ and $v_{l}=N.v$. Similar to the prefix interface in Eqn., we define a projected base interface $\tilde{I}_{N}$. If $l=0$, then $\tilde{I}_{N}=\{\mathbf{x}_{s}\}$. Otherwise, let $u_{N}$ be the latest vertex $v_{k}$ in the prefix such that $k<l$ and $\beta(v_{k})\neq\beta(v_{l})$, and define In short, $\tilde{I}_{N}$ is the interface in $G_{0}$ where the base-projected prefix last enters the current base vertex.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Reuse of Base ST-GCS Heuristic Values", "weight": 1.0} -->

Thus, consecutive ECD-subdivision vertices with the same base vertex are collapsed before evaluating the reusable heuristics. The reused $h_{\text{tri}}$ and $h_{\text{tab}}$ are then evaluated on $G_{0}^{\sharp}$ from $\tilde{I}_{N}$ using the precomputed values from $G_{0}$ and the same query goal, where $(G_{0}^{\sharp},v_{s},v_{g})=\textsc{QueryAugment}(G_{0},\mathbf{x}_{s},\mathbf{p}_{g})$. Same as in Sec. 5.5, all heuristic values are defined to be zero when $N.v=v_{g}$.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Windowed Coordination", "weight": 1.0} -->

Full-horizon robot coordination can be computationally intensive, as low-level solver calls may reserve long trajectory occupancies, including portions that have no near-term spatiotemporal correlation with the current coordination step, causing ECD-updated ST-GCSs to grow rapidly. Windowed coordination reduces this computation by applying either PP or PBS over a finite planning window, so high-level ECD reservations and PBS conflict detection use only trajectory portions inside that window.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Windowed Coordination", "weight": 1.0} -->

Let $W=[t,t+\Delta t_{\mathrm{plan}}]$ be the planning window, where $\Delta t_{\mathrm{plan}}>0$ is the window span. Let $\Delta t_{\mathrm{exec}}\leq\Delta t_{\mathrm{plan}}$ be the execution horizon. At coordination time $t$, each robot $i$ starts from a window-start state $\mathbf{x}_{s,i}^{W}$, equal to its original start at the first call and otherwise the endpoint of its last executed prefix. After each successful call, the coordinator commits the returned trajectory only over $[t,\,t+\Delta t_{\mathrm{exec}}]$, appends this prefix to the global trajectory, discards the remaining suffix, and uses its endpoint as the next $\mathbf{x}_{s,i}^{W}$.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Windowed Coordination", "weight": 1.0} -->

The selected high-level coordinator, either PP or PBS, solves the current query $(\mathbf{x}_{s,i}^{W},\mathbf{p}_{g,i})$ for every robot, including robots that have already reached their goals. For a goal-reached robot, this query starts at its current goal position and can still be replanned if priority constraints require it to move away temporarily and then return.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Windowed Coordination", "weight": 1.0} -->

For a trajectory $\tau$, let $\tau|_{W}$ denote the trajectory clipped to window $W$, with segment endpoints clipped to the window boundaries when necessary. For both windowed-PP and windowed-PBS, ECD reservations use $\tilde{\tau}|_{W}$, so they reserve the same trajectory occupancy as in Eqn. but only within $W$. Under the same window restriction, a robot pair $i\neq j$ is in conflict within $W$ if Since windowed ECD only subdivides the base ST-GCS to exclude reserved trajectory occupancy within $W$, any trajectory feasible on the windowed ECD-reserved ST-GCS remains feasible on the base ST-GCS $G_{0}$ when the reservations are ignored. Therefore, the admissible heuristics remain valid by Lemma 10.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Windowed Coordination", "weight": 1.0} -->

Windowed-PP constructs the reserved graph sequence along a fixed priority order $\boldsymbol{\sigma}$, starting from $G_{W}^{}=G_{0}$. For each $k$, robot $\sigma_{k}$ is planned on $G_{W}^{(k)}$; after this plan is found, the next reserved graph is updated as $G_{W}^{(k+1)}=\operatorname{ECD}(G_{W}^{(k)},\tilde{\tau}_{\sigma_{k}}|_{W},2r)$.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Windowed Coordination", "weight": 1.0} -->

For windowed-PBS, replanning at a node uses the same window-restricted ECD reservations. When robot $i$ is replanned at node $N$, let $\langle j_{1},\ldots,j_{l}\rangle$ be any fixed topological ordering of the set $\{j\mid j\prec_{N}^{+}i\}$ under $\prec_{N}^{+}$. The query $(\mathbf{x}_{s,i}^{W},\mathbf{p}_{g,i})$ is then solved on The child node expansion ordering is also adjusted to prefer progress by unreached robots. When a detected conflict involves one robot that has reached its goal and one that has not, PBS first considers the child node that prioritizes the unreached robot.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Windowed Coordination", "weight": 1.0} -->

Otherwise, it follows the node expansion rules as described in Sec. 7.3.1 ‣ 7.3 PBS with ST-GCS and ECD ‣ 7 Multi-Robot Motion Planning ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets").

<!-- chunk {"id": "body-0127", "role": "body", "section": "Windowed Coordination", "weight": 1.0} -->

This commit-and-replan cycle naturally matches a closed-loop execution with receding-horizon. After each execution horizon, the planner replans from the updated window-start states and incorporates updated reservations or dynamic obstacles. The special case $\Delta t_{\mathrm{exec}}=\Delta t_{\mathrm{plan}}$ commits the entire planned window before replanning; choosing $\Delta t_{\mathrm{exec}}<\Delta t_{\mathrm{plan}}$ retains a lookahead suffix that guides the current solve but is not committed. A smaller lookahead gap $\Delta t_{\mathrm{plan}}-\Delta t_{\mathrm{exec}}$ potentially leaves the robots in better states for subsequent calls, but increases total planning effort because replanning is invoked more often depending on the gap. On the other hand, as $\Delta t_{\mathrm{plan}}$ approaches the remaining horizon, windowed-PP or PBS recovers its full-horizon counterpart.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Windowed Coordination", "weight": 1.0} -->

For finite $\Delta t_{\mathrm{plan}}$, windowed coordination is incomplete in general because conflicts outside the current window are ignored until later. However, in practice, it greatly reduces the computation cost, since each low-level call reserves fewer trajectory segments and thus the ECD-updated ST-GCSs remain smaller.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Dynamic Window Adjustment", "weight": 1.0} -->

A short fixed window can defer conflicts that should be exposed before the robots commit another prefix. To reduce this failure mode, we use a dynamic adjustment rule that enlarges the planning window only when the current horizon appears insufficient. For windowed-PP, this retry is triggered when the fixed-priority solve fails in the current window. For windowed-PBS, it is triggered either by current-window failure or by repeatedly returning the same topological priority order among the same unreached robots without meaningful progress. In either case, the coordinator retries the same coordination step with doubled $\Delta t_{\mathrm{plan}}$ and commits no new trajectory prefixes. The larger window exposes more future interactions and reserves longer portions of higher-priority occupancies. After a successful step, $\Delta t_{\mathrm{plan}}$ is reset to its nominal value, keeping easy windows small while giving congested windows additional horizon.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

This section presents our numerical results for spatiotemporal planning and MRMP on ST-GCS. We implement the proposed planners and algorithmic components in Python and evaluate on an Apple^®^ M4 CPU machine with 16GB RAM. The GCS-related trajectory optimization uses Drake library and the Mosek solver. The source code and numerical results are publicly available on More detailed visualizations and simulation videos of the proposed planners can be found at Figure 9: Example instances of the generated spatial GCS. Colors indicate convex regions in the spatial decomposition. Black regions indicate environment static obstacles.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

We consider three two-dimensional base domains, rand, maze, and iris, to define the problem domains for benchmarking the spatiotemporal and MRMP planners. Each ST-GCS instance initializes a seeded spatial GCS as described in Sec. 8.1.1, and then extrudes the spatial sets through time $t\in[0,t_{\mathrm{max}}]$ with $t_{\mathrm{max}}=1000$. We precompute the heuristics $h_{\text{tri}}$ and $h_{\text{tab}}$ on only these base ST-GCSs, although Sec. 8.1.2 additionally adds dynamic obstacles into each base ST-GCS instance.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Spatial GCS Generation", "weight": 1.0} -->

For rand, we generate an $n\times n$ grid, sample a random convex polygon around each grid cell, connect intersecting convex sets, and retain the largest connected component. For maze, we first generate a random $10\times 10$ maze via recursive division and then merge adjacent free cells into larger axis-aligned rectangles whenever possible using a bipartite matching procedure similar to that of Lu et al.. For iris, we sample $10$ polygonal static obstacles in a square workspace and grow a connected cover of collision-free convex sets with the IRIS algorithm. This presents a set of more realistic GCS commonly seen in practice. The robot radius is $0.1$ in rand, and $0.25$ in maze and iris. Fig. 9 shows examples of the generated spatial GCS.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Spatiotemporal Planning Instances", "weight": 1.0} -->

We generate $60$ single-robot spatiotemporal planning instances, with $20$ instances from each of rand, maze, and iris. Each query is a feasible query on one seeded base ST-GCS and starts at time $0$ with a velocity bound $\mathbf{v}_{\mathrm{lim}}=[1.0,\ldots,1.0]$. We then add moving obstacles with piecewise-linear trajectories and the same object occupancy model as defined in Eqn. while preserving query feasibility. The resulting ST-GCS instances have a median of $33$ vertices and $184$ edges.

<!-- chunk {"id": "body-0134", "role": "body", "section": "MRMP Instances", "weight": 1.0} -->

We generate $60$ MRMP instances, with $20$ instances from each of rand, maze, and iris. Each instance contains $n$-robot queries on a seeded base ST-GCS, where each robot query starts at time $0$ with a velocity bound $\mathbf{v}_{\mathrm{lim}}=[1.0,\ldots,1.0]$. The query generation for the start positions $\mathbf{p}_{s,1},\ldots,\mathbf{p}_{s,n}$ and goal positions $\mathbf{p}_{g,1},\ldots,\mathbf{p}_{g,n}$ follow the assumption as in condition (i. ‣ 7.2 Prioritized Planning with ST-GCS and ECD ‣ 7 Multi-Robot Motion Planning ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")), while keeping their independent trajectories still intersects to make the MRMP instances emphasize coordination rather than isolated planning.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

This subsection follows our algorithmic stack for MRMP. We first ablate the low-level single-robot spatiotemporal planning BFS solver (Alg. 1 Solver ‣ 5 Graph Search on ST-GCSs ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets")), and then the child node expansion rules used by full-horizon PBS (Alg. 3), and at last the planning horizons in windowed coordination in Sec. 7.5. All ablation planners have a $10$-minute runtime budget. Unless otherwise stated, we set all their inflation factors to $\epsilon=1$ for the heuristics used in the low-level BFS solvers.

<!-- chunk {"id": "body-0136", "role": "body", "section": "BFS Heuristics", "weight": 1.0} -->

This ablation isolates the BFS heuristic (Sec. 5.5) with upper-bound pruning enabled and no optional pairwise dominance check (Sec. 5.4). Fig. 10 shows that $h_{\text{max}}$ is the most robust choice. The $h_{\text{max}}$ and $h_{\text{tab}}$ heuristics solve all $60$ instances in Sec. 8.1.2, while $h_{\text{mot}}$, $h_{\text{tri}}$, and $h_{\text{zero}}$ solve $58$, $56$, and $53$, respectively. On common-success instances, $h_{\text{max}}$ has the smallest median runtime and expanded-node count in every domain. Relative to $h_{\text{zero}}$, it reduces the median runtime by $5.3$--$56.2\times$ and the median number of expanded nodes by $11.5$--$56.5\times$ across the three domains.

<!-- chunk {"id": "body-0137", "role": "body", "section": "BFS Heuristics", "weight": 1.0} -->

Among the single-component heuristics, $h_{\text{mot}}$ is competitive on rand and strongest on the most open iris, while $h_{\text{tab}}$ solves all instances and is strongest on maze, where detours make the motion-only bound less informative; $h_{\text{tri}}$ is weaker without inflation. Fig. 11 shows that increasing $\epsilon$ substantially reduces runtime, especially for $h_{\text{tri}}$ and $h_{\text{tab}}$, but larger inflation factors produce wider optimality-gap tails. At $\epsilon=5$, the median runtime reductions are about $65\%$ for $h_{\text{mot}}$, $91\%$ for $h_{\text{tri}}$, $88\%$ for $h_{\text{tab}}$, and $56\%$ for $h_{\text{max}}$. The precomputation panel reports median preprocessing runtime.

<!-- chunk {"id": "body-0138", "role": "body", "section": "BFS Heuristics", "weight": 1.0} -->

The $h_{\text{tri}}$ heuristic stays in the seconds range, whereas $h_{\text{tab}}$ requires substantially more precomputation and peaks over $2.5$ hours. We therefore use $h_{\text{max}}$ as the default BFS heuristic and inflate it when bounded suboptimality is allowed. It inherits the strongest available component lower bound at each prefix path, and its offline cost is amortized in MRMP because many low-level calls reuse the precomputation for the same base ST-GCSs.

<!-- chunk {"id": "body-0139", "role": "body", "section": "BFS Dominance Checks", "weight": 1.0} -->

This ablation isolates the effect of the pairwise dominance check (Sec. 5.4) with the heuristic fixed to $h_{\text{max}}$. All variants use the same upper-bound pruning, and differ only in the optional pairwise dominance check. The alternatives are the safe set-containment check $\delta_{\text{set}}$, the heuristic position-based check $\delta_{\text{pos}}$, and the heuristic arrival-state-containment check $\delta_{\text{state}}$. The auxiliary vertex-indexed search used to obtain the incumbent contributes only the scalar upper-bound cost $c_{\text{ub}}$, so differences in success, runtime, and solution cost come from the selected pairwise dominance check. Fig. 12 compares the upper-bound-only variant (UB) and the three pairwise dominance checks in runtime, expanded nodes, and solution-cost increase.

<!-- chunk {"id": "body-0140", "role": "body", "section": "BFS Dominance Checks", "weight": 1.0} -->

UB, $\delta_{\text{set}}$, and $\delta_{\text{state}}$ solve all $60$ instances in Sec. 8.1.2, while $\delta_{\text{pos}}$ solves $59$ instances. Relative to $\delta_{\text{set}}$ on common-success instances, $\delta_{\text{pos}}$ and $\delta_{\text{state}}$ reduce the median expanded-node count by $65.4\%$ and $42.7\%$, and reduce the median runtime by $41.1\%$ and $42.1\%$, respectively. Both heuristic checks have zero median solution-cost increase over all common-success instances. $\delta_{\text{state}}$ has three positive solution-cost increases, with a $1.68\%$ median positive increase and a $4.8\%$ worst-case increase.

<!-- chunk {"id": "body-0141", "role": "body", "section": "BFS Dominance Checks", "weight": 1.0} -->

In contrast, $\delta_{\text{pos}}$ trades more aggressive pruning for fourteen positive solution-cost increases, with a $4.14\%$ median positive increase and a $15.1\%$ worst-case increase. Overall, these results suggest using $\delta_{\text{pos}}$ as the default scalable pairwise dominance check when small heuristic losses are acceptable, and using $\delta_{\text{state}}$ when low-level success and solution quality should stay closer to the $\delta_{\text{set}}$ reference.

<!-- chunk {"id": "body-0142", "role": "body", "section": "PBS Node Expansion Rules", "weight": 1.0} -->

This ablation isolates the node expansion rule of full-horizon PBS in Alg. 3. As introduced in Sec. 7.3.1 ‣ 7.3 PBS with ST-GCS and ECD ‣ 7 Multi-Robot Motion Planning ‣ Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets"), we compare the four rules of lazy evaluation (Lazy), the sum-of-costs (SoC) metric, the makespan (MS) metric, and the number of conflicts (NC) metric. All variants share the same low-level BFS solver with $h_{\text{max}}$ heuristic, upper-bound pruning, and $\delta_{\text{pos}}$ dominance check. Recall that a PBS node is said to be generated once created by adding a new partial priority order, while it is expanded once the robots are replanned via UpdateNode.

<!-- chunk {"id": "body-0143", "role": "body", "section": "PBS Node Expansion Rules", "weight": 1.0} -->

As shown in the first row of Fig. 13, the NC rule gives the strongest PBS scalability on $60$ $10$-robot MRMP instances generated in Sec. 8.1.3. It solves $58$ instances within the $600$s budget, compared with $55$, $52$, and $46$ for the MS, SoC, and Lazy rules, respectively. It also exhibits the best anytime behavior, solving $42$ instances by $120$s and $52$ instances by $200$s, which is consistent with the two node-count curves. We now look at the second row containing $45$ instances solved by all four rules. The generated/expanded ratio subplot shows that the Lazy rule does postpone node expansions, with the largest ratio reaching $1.93$ as PBS moves closest to a binary search tree. The two solution-quality subplots show that median solution-quality differences among expansion rules are modest. The NC and SoC rules have nearly tied median SoC ($78.1$ and $78.2$), while Lazy and MS have higher median SoC ($82.6$ and $81.2$).

<!-- chunk {"id": "body-0144", "role": "body", "section": "PBS Node Expansion Rules", "weight": 1.0} -->

The MS rule gives the lowest median MS of $10.9$, compared with at least $11.1$ for the other rules. In general, the NC rule is suggested as the default node expansion rule because it gives the strongest scalability while remaining competitive in median SoC and MS.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Windowed Coordination", "weight": 1.0} -->

This ablation isolates the planning window $t_{\text{plan}}$ and the execution window $t_{\text{exec}}$ for windowed-PBS as described in Sec. 7.5. We compare $\Delta t_{\mathrm{plan}}=\alpha r/\|\mathbf{v}_{\mathrm{lim}}\|_{\infty}$ with a planning span factor $\alpha\in\{2.5,5,10\}$, and $\Delta t_{\mathrm{exec}}=\beta\Delta t_{\mathrm{plan}}$ with an execution span factor $\beta\in\{0.5,1\}$.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Windowed Coordination", "weight": 1.0} -->

In addition, we compare the variants with static windows and dynamically adjusted windows as introduced in Sec. 7.5.1. All variants use $h_{\text{max}}$ heuristic with inflation factor $\epsilon=10$, upper-bound pruning, $\delta_{\text{pos}}$ dominance check, and the NC child-node expansion rule on $60$ $20$-robot MRMP instances generated in Sec. 8.1.3, with a $600$s per-instance runtime budget. Fig. 14 shows that dynamic window adjustment improves the $\beta=1$ success count for all spans, from $36$ to $50$ instances at $\alpha=2.5$, from $50$ to $55$ at $\alpha=5$, and from $49$ to $50$ at $\alpha=10$. Larger windows are not monotonically beneficial because they trade fewer coordination calls for harder local subproblems.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Windowed Coordination", "weight": 1.0} -->

Increasing $\alpha$ from $5$ to $10$ raises the $\beta=1$ median runtime from $40.1$s to $65.1$s and reduces success from $55$ to $50$ instances. For fixed $\alpha$, dynamic $\beta=0.5$ shifts the corresponding $\beta=1$ curve toward larger runtimes. It recovers some instances missed by $\beta=1$, but is not a strict improvement. For $\alpha=2.5,5,10$, it gains $5$, $4$, and $6$ instances while losing $12$, $5$, and $2$ instances solved by the corresponding $\beta=1$ variant. The solution-quality panels show the complementary tradeoff. Shorter windows can yield shorter successful trajectories, with fixed $\alpha=2.5$ giving the lowest median SoC/makespan ($250.0/12.5$), but only $36$ successes.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Windowed Coordination", "weight": 1.0} -->

Among the more reliable variants, dynamic $\alpha=5,\beta=1$ achieves the highest success count ($55$) with median SoC/makespan $325.0/16.2$. Using $\beta=0.5$ improves median SoC/makespan for the same dynamic $\alpha$ values, but at the cost of longer runtimes. Overall, dynamic $\alpha=5,\beta=1$ gives the best scalability--quality tradeoff in this ablation.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Performance Comparison", "weight": 1.0} -->

This subsection presents the performance comparison results on spatiotemporal planning and MRMP.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Spatiotemporal Planning Benchmark", "weight": 1.0} -->

We evaluate the spatiotemporal planners under $60$s runtime budget on the $60$ instances from Sec. 8.1.2. The first two are BFS variants shortlisted from previous ablations. Both use $h_{\text{max}}$, upper-bound pruning, and $\epsilon=10$, and differ only in whether they use $\delta_{\text{pos}}$ or $\delta_{\text{set}}$. The $\delta_{\text{pos}}$ variant tests the more aggressive point-based dominance check, whereas the $\delta_{\text{set}}$ variant tests set-containment pruning with the same inflated max heuristic. The optimization-based baselines are MICP and MICP(g), which solve Eqns.. MICP directly solves the program to optimality, while MICP(g) solves its linear relaxation and then applies stochastic path rounding (see Sec. 4.2) with $\lceil 1000\log|E|\rceil$ rounded paths.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Spatiotemporal Planning Benchmark", "weight": 1.0} -->

We also compare against the sampling-based baseline ST-RRT^∗^ from OMPL, reporting both the first feasible trajectory and the final incumbent solutions. Given the robot radius $r$, we also compare against the discrete search-based Zeta^∗^-SIPP with cell sizes of $r$ and $2r$.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Spatiotemporal Planning Scalability", "weight": 1.0} -->

Fig. 15 shows that the proposed BFS solvers on ST-GCS are the only planning variants that solve all $60$ instances while remaining consistently subsecond. The bounded-suboptimal $\delta_{\text{set}}$ variant has a $0.10$s median runtime, while the $\delta_{\text{pos}}$ variant has a $0.12$s median runtime. Running the same $\delta_{\text{set}}$ solver with $\epsilon=1$ increases the median runtime to $0.23$s. The two optimization baselines on ST-GCS are substantially less scalable. MICP solves $31$ instances with a $6.03$s median runtime on successful runs, whereas MICP(g) solves $59$ instances with a $1.30$s median runtime. The non-ST-GCS baselines expose representation-dependent scalability and success behavior.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Spatiotemporal Planning Scalability", "weight": 1.0} -->

For ST-RRT^∗^, the first feasible trajectory appears on $57$ instances with a $0.06$s median time-to-first-solution, but the planner reaches its final incumbent only after the full anytime budget. The domain split still shows geometry dependence, since ST-RRT^∗^ solves all $20$ rand and iris instances but only $17$ maze instances. This dependence is visible in the success-rate curves. The iris instances reach $20/20$ successes by $0.005$s, rand reaches $16/20$ by $0.47$s and $20/20$ only after the last successful first solution at $8.84$s, and maze reaches $17/20$ by $3.82$s and remains below full success through $60$s. ST-RRT^∗^ samples and connects directly in continuous collision-free space rather than using the GCS adjacency, so the maze domains make it harder to discover a temporally feasible connection within the budget.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Spatiotemporal Planning Scalability", "weight": 1.0} -->

Zeta^∗^-SIPP with cell size $r$ solves $46$ instances with a $0.34$s median runtime, while the coarser $2r$ grid solves $41$ instances with a $0.13$s median runtime. Its success depends on the spatial discretization. The finer grid improves success on rand instances ($9/20$ versus $4/20$), while both grids solve $17/20$ maze instances and all $20$ iris instances. Zeta^∗^-SIPP searches safe intervals only on fixed spatial grids; when the grid cells and line-of-sight edges do not represent the relevant passage, a feasible trajectory may be absent from the discretized search space.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Spatiotemporal Planning Solution Quality", "weight": 1.0} -->

The middle and bottom rows of Fig. 15 show that the search-based ST-GCS solvers preserve solution quality while improving scalability. The bounded-suboptimal $\delta_{\text{set}}$ variant has a $9.08$ median cost, while the $\delta_{\text{pos}}$ variant has a $9.18$ median cost. Running the $\delta_{\text{set}}$ solver with $\epsilon=1$ reduces the median cost to $8.53$, compared with a $9.70$ median cost for MICP(g). On the $30$ instances solved by MICP, the two inflated BFS variants, and MICP(g), the median cost increase relative to MICP is $0.0\%$ for all three non-MICP planners.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Spatiotemporal Planning Solution Quality", "weight": 1.0} -->

Nonzero increases occur on $12$, $6$, and $2$ instances for $\delta_{\text{pos}}$, $\delta_{\text{set}}$, and MICP(g), respectively, with median positive increases of $4.79\%$, $5.95\%$, and $3.23\%$. For the anytime ST-RRT^∗^ baseline, the final incumbent substantially improves solution quality after the first feasible trajectory is found. Across its $57$ successful instances, the final incumbent reduces the median successful cost from $9.29$ to $6.49$. The single ST-RRT^∗^ legend entry uses first-feasibility time for success and final-incumbent cost for quality. The solution-cost comparisons should be interpreted relative to the solution space represented by each planner. For rand and maze, the ST-GCS-based planners produce costs close to the ST-GCS optimum, with small increases for the inflated BFS variants and MICP(g) on common-success instances.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Spatiotemporal Planning Solution Quality", "weight": 1.0} -->

For iris, however, the ST-GCS-based planners generally have higher costs than the non-ST-GCS baselines. This is expected since IRIS-generated convex sets provide only partial coverage of the full collision-free space, so ST-GCS optimality is with respect to the ST-GCSs rather than the entire continuous free space.

<!-- chunk {"id": "body-0158", "role": "body", "section": "MRMP Benchmark", "weight": 1.0} -->

We evaluate various MRMP planners under $180$s runtime budget on $n$-robots MRMP instances, where each $n=2,4,\ldots,20$ corresponds to $60$ instances generated as in Sec. 8.1.3. The proposed Windowed-PBS + BFS applies windowed-PBS with NC node expansion rule and $\Delta_{\text{plan}}=\Delta_{\text{exec}}=5r/||\mathbf{v}_{\text{lim}}||_{\infty}$ as the high-level coordinator, and the BFS solver with $h_{\text{max}}$, $\epsilon=10$, upper-bound pruning, and $\delta_{\text{pos}}$ as the low-level solver, which empirically is most scalable under limited runtime.

<!-- chunk {"id": "body-0159", "role": "body", "section": "MRMP Benchmark", "weight": 1.0} -->

With the same low-level BFS solver, we also compare several composed baselines with different high-level coordinators, namely, windowed-PP with $\Delta_{\text{plan}}=\Delta_{\text{exec}}=5r/||\mathbf{v}_{\text{lim}}||_{\infty}$, PBS with NC node expansion rule, and PP. To test the alternative low-level planners in Sec. 8.3.1, we evaluate PBS + Zeta^∗^-SIPP with discretization of $r$, and PP + ST-RRT^∗^. PP + ST-RRT^∗^ is adopted as an anytime prioritized planning baseline. After the first priority-ordered pass produces a feasible joint solution, the remaining budget is used for improvement rounds that revisit the robots in the same order and replace an incumbent trajectory only when ST-RRT^∗^ finds a shorter collision-free trajectory against the current reservations. We report its first feasible solution for runtime and its final incumbent solution for solution quality. In addition, we compare with two standalone MRMP baselines.

<!-- chunk {"id": "body-0160", "role": "body", "section": "MRMP Benchmark", "weight": 1.0} -->

K-CBS is a fast feasibility-oriented and sampling-based MRMP planner from OMPL. CB-GCS similarly solves MRMP on GCSs under a fixed time-step representation.

<!-- chunk {"id": "body-0161", "role": "body", "section": "MRMP Scalability", "weight": 1.0} -->

Fig. 16 shows that the proposed Windowed-PBS + BFS has the highest success rate. Over the $n\geq 10$ instances, it solves $338$ out of $360$ instances. All baselines solve fewer cases in the same regime. Among the other composed baselines, PP + BFS solves $159$, PP + ST-RRT^∗^ solves $151$, PBS + BFS solves $135$, Windowed-PP + BFS solves $108$, and PBS + Zeta^∗^-SIPP solves $9$. The two standalone baselines also degrade at high robot counts. K-CBS solves $242$ instances for $n\geq 10$, while CB-GCS solves only $6$. At $n=20$, Windowed-PBS + BFS solves $19/20$ rand, $16/20$ maze, and $16/20$ iris instances, giving $51/60$ successes overall. The next-best baseline at this scale is K-CBS with $20/60$ successes.

<!-- chunk {"id": "body-0162", "role": "body", "section": "MRMP Scalability", "weight": 1.0} -->

The remaining baselines solve $13/60$ cases for PP + ST-RRT^∗^, $7/60$ for Windowed-PP + BFS, $6/60$ for PP + BFS, $2/60$ for PBS + BFS, and $0/60$ for PBS + Zeta^∗^-SIPP and CB-GCS. These comparisons separate the two ingredients needed for scalability. Windowing alone is not sufficient. Windowed-PP + BFS uses the same low-level solver and horizon schedule as Windowed-PBS + BFS, but solves only $108/360$ high-count cases and $7/60$ cases at $n=20$. PBS alone is also not sufficient. Full-horizon PBS + BFS solves $135/360$ high-count cases and only $2/60$ cases at $n=20$. The proposed combination avoids these two failure modes by resolving local priority conflicts inside each window while committing only the next execution interval. The comparison against PP + ST-RRT^∗^ and K-CBS is clearest on the most challenging $n\geq 16$ instances.

<!-- chunk {"id": "body-0163", "role": "body", "section": "MRMP Scalability", "weight": 1.0} -->

Windowed-PBS + BFS solves $55/60$, $51/60$, and $55/60$ cases on rand, maze, and iris, respectively. PP + ST-RRT^∗^ solves $15/60$, $2/60$, and $39/60$, while K-CBS solves $12/60$, $27/60$, and $49/60$. On successful runs in this regime, the median runtimes of Windowed-PBS + BFS are $37.1$s, $20.8$s, and $51.9$s across the three domains. PP + ST-RRT^∗^ has successful-run median runtimes of $15.1$s, $88.5$s, and $1.07$s, while K-CBS has $105$s, $82.3$s, and $37.1$s.

<!-- chunk {"id": "body-0164", "role": "body", "section": "MRMP Scalability", "weight": 1.0} -->

Thus, although PP + ST-RRT^∗^ and K-CBS are very strong baselines on smaller instances with fewer robots, the proposed Windowed-PBS + BFS remains the only scalable choice for the most challenging MRMP instances across all three domains. Tab. 1 shows search and optimization dominate the runtime, while ECD becomes substantial at larger $n$ and other costs remain small. The query density reports the area fraction of the entire spatial GCSs covered by the union of the start and goal hypercube occupancies as in Eqn..

<!-- chunk {"id": "body-0165", "role": "body", "section": "MRMP Solution Quality", "weight": 1.0} -->

The SoC and makespan rows of Fig. 16 show that the proposed Windowed-PBS + BFS retains competitive solution quality while achieving the scalability reported above. We report the median SoC and makespan on the $n\leq 10$ instances where most planners succeed on substantial subsets. On the corresponding common-success subsets, the median SoC/makespan Windowed-PBS + BFS is $40.0/10.0$. Full-horizon PBS + BFS and PP + BFS have lower median SoC/makespan $26.7/8.71$ and $27.3/8.79$, respectively. Windowed-PP + BFS gives a similar limited-horizon tradeoff, with median SoC/makespan $40.0/10.0$. Thus, windowed coordination sacrifices some SoC since it plans and commits only within a finite horizon, while keeping the makespan close to the full-horizon BFS planners. In contrast, the feasibility-oriented K-CBS has substantially worse solution quality with median SoC/makespan $66.0/21.7$.

<!-- chunk {"id": "body-0166", "role": "body", "section": "MRMP Solution Quality", "weight": 1.0} -->

PP + ST-RRT^∗^ is a stronger solution-quality baseline in favorable domains after using the full $180$s runtime budget. On iris, it achieves median SoC/makespan $33.6/8.33$, below the median $60.0/10.0$ of Windowed-PBS + BFS. As in Sec. 8.3.3, this gap is expected since IRIS-generated convex sets only partially cover the full collision-free space. However, its quality advantage is domain-dependent. On maze, PP + ST-RRT^∗^ has median SoC/makespan $42.6/15.0$, while Windowed-PBS + BFS has median SoC/makespan $60.0/14.4$. Fig. 17 illustrates these domain-dependent quality differences on representative $10$-robot examples with a 30s runtime budget. Overall, K-CBS emphasizes feasibility at the cost of longer joint plans. PP + ST-RRT^∗^ can produce high-quality solutions in favorable domains but is less consistent. Windowed-PBS + BFS provides the most consistent quality-scalability tradeoff across domains.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Applications and Demonstrations", "weight": 1.0} -->

This section complements the quantitative comparisons above with several demonstration scenarios. We first describe a trajectory-optimization postprocessing step for smoothing the piecewise-linear trajectories produced by our planner, then demonstrate the solutions on large-scale simulated problems and real-robot deployments.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Global Trajectory Optimization", "weight": 1.0} -->

The proposed MRMP planner produces piecewise-linear trajectories with fixed vertex paths on ST-GCS. As a postprocessing step, we can smooth these trajectories by solving a Quadratic Program (QP) over sampled spatial positions along the trajectories at fixed time samples. Given $n$ robot trajectories $\mathcal{T}^{0}=\{\tau_{i}^{0}\}_{i=1}^{n}$, we choose a shared ordered sample sequence $\mathcal{K}=\langle t_{1},\ldots,t_{l}\rangle$, with $t_{1}<\cdots<t_{l}$, formed from a uniform time grid together with the original trajectory knot times. We will use $k$ to denote the index of the fixed time sample $t_{k}$.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Global Trajectory Optimization", "weight": 1.0} -->

Let $\bar{\mathbf{p}}_{i,k}=\tau_{i}^{0}(t_{k}).\mathbf{p}$ be the reference position of robot $i$ at time $t_{k}$. The program keeps the times fixed and optimizes only the sampled spatial positions $\mathbf{p}_{i,k}\in\mathbb{R}^{m}$. Similarly to Sec. 7.1, we assume a common radius $r$ for the robots. For compactness, we define the sampled velocity and velocity-variation term as follows: Let $\mathcal{F}_{i}$ denote the samples at which robot $i$ is fixed at its initial or terminal state. For each interval $[t_{k},t_{k+1}]$, let $v_{i,k}$ be the ST-GCS vertex traversed by the input piecewise-linear trajectory at the interval midpoint. We formulate the trajectory optimization as: where Eqns.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Global Trajectory Optimization", "weight": 1.0} -->

(12a)--(12c) are enforced for every robot and all valid sample indices, with Eqn. (12a) restricted to $k\in\mathcal{F}_{i}$. Eqn. (12d) is enforced for every robot pair $1\leq i<j\leq n$ and every sample $k$. The objectives regularize velocity variation and penalize deviations from the input reference trajectories. The two nonnegative weights $\lambda_{c}$ and $\lambda_{d}$ tune the relative emphasis of these two objective terms, respectively. Eqn. (12a) preserves the prescribed start and goal positions. Eqn. (12b) enforces the same component-wise velocity limits constraint as Eqn. (3f) in the original formulation. Eqn. (12c) constrains both endpoints of each optimized segment to lie in the same set $X_{v_{i,k}}$ of the original trajectory segment.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Global Trajectory Optimization", "weight": 1.0} -->

Since each optimized segment is a linear interpolation in space-time between the two endpoints, the convexity of $X_{v_{i,k}}$ keeps the entire optimized segment inside this collision-free set. Eqn. (12d) is a sampled linearization of pairwise robot separation, where $\mathbf{n}_{ij,k}=(\bar{\mathbf{p}}_{i,k}-\bar{\mathbf{p}}_{j,k})/\|\bar{\mathbf{p}}_{i,k}-\bar{\mathbf{p}}_{j,k}\|_{2}$ is the unit normal precomputed from the original sampled positions $\bar{\mathbf{p}}_{i,k}$ and $\bar{\mathbf{p}}_{j,k}$ at time $t_{k}$.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Global Trajectory Optimization", "weight": 1.0} -->

When explicit obstacle representations are available, we can further replace Eqn. (12c) with direct sampled collision-avoidance constraints. At each sample time $t_{k}$, a static obstacle uses its fixed spatial geometry, while a space-time obstacle uses its spatial slice at $t_{k}$. For each robot $i$, obstacle $o$, and time sample $t_{k}$, let $\mathbf{a}_{i,k,o}\in\mathbb{R}^{m}$ and $b_{i,k,o}\in\mathbb{R}$ jointly define a precomputed separating halfspace that contains the original trajectory sample $\bar{\mathbf{p}}_{i,k}$ and excludes the obstacle geometry inflated by the robot radius $r$.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Global Trajectory Optimization", "weight": 1.0} -->

We enforce the corresponding sampled collision-avoidance constraint $\mathbf{a}_{i,k,o}^{\top}\mathbf{p}_{i,k}\geq b_{i,k,o}$, which keeps the optimized sample on the same collision-free side of this halfspace.

<!-- chunk {"id": "body-0174", "role": "body", "section": "Global Trajectory Optimization", "weight": 1.0} -->

The resulting smoothed trajectories are certified to be space-time collision-free only at the sampled states $(\mathbf{p}_{i,k},t_{k})$ where the QP constraints are imposed. For larger instances, we improve scalability with a sequential rolling-horizon variant that optimizes a short block of consecutive time samples, fixes the accepted prefix, advances the block, and repeats until all samples have been processed. This decomposition keeps each local trajectory-optimization QP small and makes the full problem easier to solve, while retaining the same smoothing objective and sampled-state collision-free.

<!-- chunk {"id": "body-0175", "role": "body", "section": "Large-Scale Coordination", "weight": 1.0} -->

We demonstrate in large-scale MRMP instances that the proposed Windowed-PBS + BFS planner scales to confined and highly congested workspaces, with trajectory optimization applied afterward as a smoothing post-processing step. Fig. 18 shows two planar coordination settings with complementary sources of difficulty. Using the same query-density metric as Tab. 1, the $50$-robot and $100$-robot instances have query densities of $95.7\%$ and $77.1\%$, respectively. In the $50$-robot four-room instance, the workspace funnels traffic through narrow inter-room passages, so difficulty comes from geometric bottlenecks and the need to sequence many robots through shared doorways. In the $100$-robot empty-workspace instance, the independent trajectories of $97$ robots are involved in collisions initially in one connected conflict component, so difficulty comes from dense pairwise interaction rather than static obstacles. These results show that the planner remains practical both when difficulty comes from geometric bottlenecks and when it comes from dense pairwise robot interactions.

<!-- chunk {"id": "body-0176", "role": "body", "section": "Large-Scale Coordination", "weight": 1.0} -->

Fig. 19 further stresses coordination with a $32$-UAV position-exchange problem on a 3D sphere, where every robot conflicts with any other robots at the sphere center. This fully coupled exchange forces the coordinator to resolve simultaneous conflicts in 3D before trajectory optimization smooths the resulting paths. Fig. 20 further tests a $48$-UAV instance in a fastpathplanning-style 3D village with dense buildings and trees. The generated village occupies an $8\times 8\times 3$ workspace, includes building footprints together with randomly placed tree and bush obstacles, and decomposes the remaining free space into $119$ convex boxes. The start--goal pairs are sampled as long-distance trips across this fragmented free space, so many UAVs must simultaneously route around vertical clutter while avoiding one another in narrow local passages.

<!-- chunk {"id": "body-0177", "role": "body", "section": "Mobile Robots Deployment", "weight": 1.0} -->

We validate our MRMP planner in an open indoor environment with a system of $9$ differential drive mobile robots. The system is centrally controlled by an Intel Core Ultra 5 125U laptop with 16GB RAM, ROS2 Humble, and Vicon for robot localization. Each robot has a bounding radius of 7cm and is exposed to a velocity command $(v,\omega)$, with linear velocity $v\in[0,0.6]$ m/s and angular velocity $\omega\in[-2.5,2.5]$ rad/s. Note that this velocity limit is set conservatively smaller than the physical robot limits for system robustness.

<!-- chunk {"id": "body-0178", "role": "body", "section": "Mobile Robots Deployment", "weight": 1.0} -->

We construct a rearrange task consisting of a sequence of MRMP queries within a 3m$\times$`<!-- -->`{=html}3m bounding square. The goal positions in each query consecutively form a configuration of five letters: S, T, G, C, and S. All the robots start simultaneously from their previous goal configurations; specifically, they initialize and terminate in a $3\times 3$ grid configuration. We first compute piecewise-linear solution trajectories via Windowed-PBS+BFS, and then smooth them via the trajectory optimization described in Sec. 9.1. The safe clearance between the robots is set to $20$cm during planning, which is $6$cm larger than twice the robot radius. The offline planning for the entire task took 16.28s.

<!-- chunk {"id": "body-0179", "role": "body", "section": "Mobile Robots Deployment", "weight": 1.0} -->

During online execution, the smoothed trajectories are discretized with a $0.05$s time step into time-indexed waypoints, and the tracker precomputes segment-wise reference linear and angular velocities from consecutive samples. All robots receive a common start time and evaluate their own trajectory at a system-wide shared elapsed time, preserving the simultaneity encoded by the offline solution. We use a simple trajectory tracking controller for the robots with a 60-Hz frequency. In each control cycle, the tracker first identifies the active trajectory segment whose time interval contains the system time. The final published velocity command combines the active segment's reference velocities as feedforward terms with body-frame feedback corrections computed from the interpolated desired pose error. In our deployments, the conservative velocity limits and additional planned inter-robot clearance provided enough margin for the observed tracking errors, and the robots completed the rearrangement without inter-robot collisions. Fig. 21 demonstrates the actual robot trajectories during the rearrange task.

<!-- chunk {"id": "body-0180", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We presented ST-GCS as a continuous-space framework for time-optimal spatiotemporal motion planning with dynamic obstacles and multi-robot interactions. By searching over path-indexed states on space-time convex sets, the proposed solver avoids a single large mixed-integer formulation while still optimizing continuous trajectories along candidate paths. The ECD scheme further allows planned occupancies to be reserved directly in the graph, enabling prioritized and windowed coordination for MRMP. Experiments show that the resulting planners substantially improve scalability while maintaining competitive solution quality. Large-scale demonstrations further show practical coordination of up to $100$ robots within a few minutes.

<!-- chunk {"id": "body-0181", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Several scope limitations suggest natural directions for future work. First, the current ST-GCS formulation uses piecewise-linear trajectory representations with time monotonicity and component-wise velocity bounds, motivating richer trajectory representations for nonholonomic systems, kinodynamic constraints, and manipulation tasks. Second, this work targets offline MRMP with known environments, motivating online MRMP with frequent replanning under changing environments or lifelong task assignments, together with adaptive or approximate convex decompositions that keep such replanning more efficient. Third, finite-window coordination is incomplete in general because conflicts outside the current window are deferred, motivating stronger window-selection rules with completeness guarantees.
