<!-- arxiv-full-text:v1 {"arxiv_id": "2606.00842", "source": "arxiv-html"} -->

## Introduction

Motion planning is a fundamental problem in robotics and autonomous systems involving the computation of feasible, optimized trajectories for agents navigating through complex environments. Beyond obstacle avoidance, many real-world tasks impose rich logical and sequential constraints on how an agent must interact with its environment. A warehouse robot must pick and verify an item at one station before proceeding to delivery locations. An autonomous underwater robot must make a surface communications handshake before descending into a deep zone. A surgical robot must exchange the correct tool at a swap station before entering the next anatomical tissue layer. An inspection robot must confirm sensor access before traversing a restricted zone. In general, these are *precedence constraints*: conditions under which parts of an environment become accessible only after prior actions have been completed, such as task execution, confirmation, clearance, or manipulation.

Encoding and solving motion planning problems with such constraints efficiently and optimally is a major challenge, due to the inherent coupling between combinatorial sequencing (determining the order of actions) and continuous geometric optimization (computing a smooth trajectory through the environment). These problems are coupled tightly: the optimal action sequence depends on the geometry, and the feasibility of a continuous path depends on the action sequence. Existing approaches, discussed in detail in the related work section below, tend to handle one problem well, but rarely both.

The *graphs of convex sets* (GCS) framework, introduced by Marcucci et al., provides a powerful framework to address this discrete-continuous coupling. By associating convex programs with the nodes and edges of a graph, GCS elegantly unifies combinatorial graph search with continuous convex optimization into a single optimization problem. For shortest path problems, solving the relaxation of a tight mixed-integer convex reformulation yields certifiably near-optimal or globally optimal solutions for many practical motion planning problems, essentially using only convex optimization.

The goal of the present paper is to extend the GCS framework to a much richer class of *mission* planning problems with precedence constraints, expressed as a fragment of signal temporal logic (STL). An overview of the proposed approach is shown in Fig. 1. Prior work of You et al. introduced *augmented graphs of convex sets* that encode key-door precedence constraints within the GCS framework. The main insight was that by constructing carefully layered and modified copies of the base GCS -- one subgraph per reachable subset of collected keys -- and linking layers via zero-cost directed edges at key nodes, the combinatorial precedence structure is exactly encoded in the graph topology. A shortest path in the augmented GCS simultaneously selects an optimal key-collection sequence and computes an optimal continuous trajectory, solving the discrete-continuous problems jointly. On benchmark instances, our approach runs several orders of magnitude faster and scales to far larger environments than general-purpose temporal logic motion planning tools.

Figure 1: Overview of the proposed approach. The environment is first partitioned and represented as a Graph of Convex Sets (GCS). An augmented GCS is then constructed to encode precedence specifications, and a shortest path problem is solved for the augmented GCS.

The present paper substantially extends You et al.. We provide formal proofs of optimality, establish a precise connection to a landmark classical combinatorial algorithm, develop a library of specification variations, and present an expanded computational study.

### I-A Contributions

Prior work made the following contributions: an exact convex partitioning algorithm (Algorithm 1) that constructs a labeled GCS encoding connectivity among free space, key, and door regions; an algorithm (Algorithm 2) for constructing an augmented GCS with an informal argument that a shortest path in the augmented GCS exactly solves the original motion planning problem; and a key-door benchmark generator and numerical experiments demonstrating orders-of-magnitude speedup over general-purpose temporal logic tools.

The present paper contributes the following beyond: Formal proofs of correctness and optimality (Theorem 1). We present proofs of soundness and completeness, establishing a bijection between augmented GCS paths and feasible trajectories, and of cost equivalence.

Bellman-Held-Karp (BHK) correspondence (Theorem 2). We demonstrate that the layer structure and inter-layer edges of the augmented GCS correspond exactly to the BHK dynamic programming recurrence for the Traveling Salesman Problem (TSP), generalized from discrete city-to-city costs to shortest paths through continuous geometry. The augmented GCS matches the combinatorial complexity class of BHK while additionally solving the continuous geometry problem that BHK takes as preprocessed input.

The BHK correspondence is not just an elegant aesthetic observation, it also opens the door to connect with more than 70 years of research on the TSP, one of the most widely studied combinatorial optimization problems. It strongly motivates translating a wide variety of heuristics into the augmented GCS framework; these heuristics can enable scaling to extremely large instances despite worst-case (exponential) computational complexity.

Extended Specification Library (Section VII). We develop eight specification variations extending the key-door precedence logic: mandatory key collection, pure wayset collection (without precedence constraints), ordered key collection, disjunctive keys, conjunctive doors (multi-key doors), items/tools (multi-door keys), timed keys and doors, and conditional (if-then) constraints. For each variation, we provide the modified STL formula, the corresponding modification for augmented GCS construction in Algorithm 2, and a proof of correctness. This extensible library of STL specifications enables moving from vanilla motion planning to increasingly complex *mission* planning and design problems.

Expanded experimental evaluation and refactored codebase. We present substantially expanded numerical experiments including more varied and larger key-door maze instances, a new benchmark suite for the pure wayset collection (TSP) variation, a hand-designed environment from a classic video game, and a relaxation tightness analysis. For the final version, we will provide a clean refactoring of the codebase to facilitate reproducibility and follow-up research.

Improved Exact Convex Partitioning. Finally, we provide a significant improvement over the convex partitioning algorithm . In contrast to obstacles and doors, key regions do not constrain traversability: an agent may pass through a key region freely, and key regions are permitted to overlap with free-space cells. Therefore, only obstacles and doors must contribute hyperplanes to the arrangement that partitions the environment. Key regions are incorporated as labeled nodes after the partition is constructed, by identifying which cells each key region intersects. Excluding key region boundaries from the hyperplane arrangement avoids introducing cuts into the free-space partition that serve no geometric purpose, directly reducing the size of every subgraph in the augmented GCS.

### I-B Related Work

Motion Planning. Motion planning comprises sampling-based, combinatorial, and optimization-based paradigms. Sampling-based methods such as RRT(^∗^) and PRM(^∗^) handle high-dimensional configuration spaces but provide only probabilistic guarantees and non-smooth trajectories. Combinatorial methods give exact solutions in low dimensions but face exponential complexity in higher dimensions. Trajectory optimization approaches compute high-quality locally optimal solutions but may become trapped in local minima. Our approach inherits the ability of optimization-based methods to compute certifiably near-optimal smooth trajectories while extending their reach to problems with complex combinatorial logical structure.

Graphs of Convex Sets. The GCS framework was introduced by Marcucci et al., who developed a tight mixed-integer convex formulation of the shortest path problem in graphs of convex sets and showed that the convex relaxation is often exact in practice. The framework was applied to robot motion planning around obstacles , establishing GCS as a highly effective tool for motion planning that produces certifiably near-optimal trajectories on challenging environments. Subsequent work has extended the GCS framework towards multi-query settings, contact-rich manipulation, non-Euclidean configuration spaces, a unified graph optimization framework, and other directions.

Temporal Logic Motion Planning. Using formal specification languages such as linear temporal logic (LTL) to express complex robot tasks has been widely studied. The standard approach constructs a product automaton between a finite abstraction and discrete finite or Büchi automaton for the LTL formula, facing doubly exponential complexity. For continuous environments, combining formal specifications with continuous trajectory optimization has been pursued through mixed-integer programming, satisfiability modulo theories, and control barrier functions. Signal temporal logic (STL) extends temporal logic to continuous-time signals, and has been used with robust and risk-based optimization formulations.

Temporal Logic with GCS. Combining temporal logic specifications with the GCS framework was first studied by Kurtz and Lin, who represent the product of an LTL automaton with a GCS structure as a graph of convex sets. This top-down approach handles arbitrary LTL specifications but inherits doubly exponential automaton construction cost. Our approach is complementary: rather than applying a general pipeline to arbitrary formulas, we identify classes of specifications whose structure can be directly encoded in the GCS topology, achieving singly exponential construction in the number of key-door pairs. The fragment library in Section VII explores the boundary between these two approaches.

Task and Motion Planning. Our problem can also be framed within the task and motion planning (TAMP) paradigm, which jointly reasons about discrete task-level decisions and continuous motion-level execution. TAMP methods generally rely on interleaving symbolic planning with geometric feasibility checking. The augmented GCS approach differs from classical TAMP in that the discrete sequencing problem and the continuous geometric optimization are solved simultaneously rather than iteratively, and the solution is certifiably near-optimal rather than satisficing.

Traveling Salesman, Vehicle Routing, and Waypoint Collection. The Traveling Salesman Problem (TSP) and its variants formalize the combinatorial structure underlying waypoint collection tasks. The BHK dynamic programming algorithm is the foundational exact method, running in $O(2^{n}n^{2})$ time. Several works have studied TSP variants in continuous geometric spaces, including TSP with neighborhoods, the Dubins TSP for vehicles with turning constraints and coverage path planning. Our BHK correspondence result in Section VI precisely characterizes the relationship between the augmented GCS and BHK, showing that the augmented GCS solves a continuous-geometry generalization of both the shortest Hamiltonian path problem and Traveling Salesman Problem within the same combinatorial complexity class.

Convex Partitioning. Computing a convex partition of the free space is a classical problem in computational geometry. The cell enumeration approach based on hyperplane arrangements used in Algorithm 1 follows the classic reverse search method of Avis and Fukuda. The optimal complexity reduction problem for minimizing the size of a decomposition was studied by Geyer et al..

## Problem Formulation

Consider a robot operating in a bounded environment $\mathcal{X}\subset\mathbf{R}^{d}$. The environment contains a set of obstacles $\mathcal{O}=\{\mathcal{O}_{i}\}_{i=1,...,n_{O}}$ with $\mathcal{O}_{i}\subset\mathcal{X}$. The obstacle-free space is $\mathcal{C}=\mathcal{X}\setminus\mathcal{O}$. The environment also contains a set of *door* regions $\mathcal{D}=\{\mathcal{D}_{i}\}_{i=1,...,n_{\mathcal{K}}}$, which are obstacles that can be "unlocked" and removed by visiting a corresponding set of *key* regions $\mathcal{K}=\{\mathcal{K}_{i}\}_{i=1,...,n_{\mathcal{K}}}$. All sets are assumed to be polytopes with given half-space representations: We assume $n_{\mathcal{K}}$ keys and $n_{\mathcal{K}}$ doors with a bijective pairing: key $i$ unlocks door $i$ for $i=1,...,n_{\mathcal{K}}$. The *key-door mapping* $\mathbf{D}:2^{\mathcal{K}}\rightarrow 2^{\mathcal{D}}$ specifies which doors are unlocked by a given key subset. In the base setting, this is the identity mapping $\mathbf{D}(S)=\{D_{i}:K_{i}\in S\}$.

Our goal is to find a trajectory $q$ over a time horizon $T$ that solves the following optimization problem: | | | $\displaystyle\underset{q}{\text{minimize}}\quad$ | | $\displaystyle\alpha\int_{0}^{T}\|\dot{q}(t)\|_{2}dt+\beta T$ | | \(1\) | | | | subject to | | $\displaystyle q(t)\in\mathcal{C}\cup\mathcal{K}\cup\mathcal{D}\quad\forall t\in[0,T]$ | | | | | | $\displaystyle q(t)\models\phi(\mathcal{K},\mathcal{D})$ | | | | | | $\displaystyle\dot{q}(t)\in\mathcal{Q}\quad\forall t\in[0,T]$ | | | | | | $\displaystyle\dot{q}=\dot{q}_{0},\ \dot{q}(T)=\dot{q}_{T}.$ | | | The objective is a weighted sum of the trajectory length and the time horizon with weights $\alpha$ and $\beta$, respectively. The first constraint requires the trajectory to be in the union of free space sets, key sets, and door sets for all time. The second constraint is a temporal logic specification that enforces the key-door precedence logic to be satisfied. The third constraint requires the velocity to be in the convex set $\mathcal{Q}$ for all time. The remaining constraints specify initial and terminal conditions for the position and velocity.

The optimization problem is infinite-dimensional. Candidate trajectories are parameterized with piecewise Bézier curves defined by a finite set of control points, making the problem finite-dimensional and admitting additional convex constraints or objective terms on higher-order derivatives for dynamic feasibility. This facilitates trajectory design for fully actuated and differentially flat systems.

### II-A Precedence Constraints via Signal Temporal Logic

We use signal temporal logic (STL) to encode the key-door precedence specifications. STL is a variation of temporal logic that offers a general and expressive framework to specify complex spatiotemporal tasks and constraints. A STL formula can be composed from the following grammar by starting from a set of atomic propositions $AP$ with $p\in AP$ and recursively applying boolean operators: $\neg$ (not), $\wedge$ (and), and $\vee$ (or), and temporal operators: $\mathcal{U}$ (until), and $\mathcal{R}$ (release). The until operator $\phi\mathcal{U}\psi$ is satisfied if $\phi$ remains true until $\psi$ becomes true. The release operator $\phi\mathcal{R}\psi$ is satisfied if $\psi$ remains true until and including when $\phi$ becomes true, and if $\phi$ never becomes true, then $\psi$ always remains true; in other words, $\phi$ releases $\psi$. Additional temporal operators include eventually ($\mathcal{F}\varphi:=\top\mathcal{U}\varphi$) and always ($G\varphi:=\neg\mathcal{F}\neg\varphi$).

The base key-door precedence specification uses the release operator: which requires $\lnot D_{i}$ to hold until $K_{i}$ is visited (and visiting $K_{i}$ releases the constraint), while making key collection *optional* unless geometrically required to reach the goal. The term $\mathcal{F}(\mathcal{T})$ requires the trajectory to eventually reach the target set, which is guaranteed by the terminal condition.

Alternatively, key collection can be made *mandatory* using the until operator: which prevents passage through $D_{i}$ until $K_{i}$ has been collected and additionally guarantees $K_{i}$ is eventually collected. When the geometry requires all keys to reach the target, $\varphi_{\mathrm{base}}$ and $\varphi_{\mathcal{U}}$ are equivalent.

### II-B Graphs of Convex Sets

The GCS framework consists of a graph $\mathcal{G}(\mathcal{V},\mathcal{E})$ where each vertex $v\in\mathcal{V}$ is associated with a variable $x_{v}\in\mathbf{R}^{n_{v}}$, a convex set $\mathcal{X}_{v}\subseteq\mathbf{R}^{n_{v}}$, and a convex function $f_{v}:\mathbf{R}^{n_{v}}\rightarrow\mathbf{R}$. Each edge $e=(u,v)\in\mathcal{E}$ couples the vertex variables through a convex function $f_{e}:\mathbf{R}^{n_{u}+n_{v}}\rightarrow\mathbf{R}$ and a convex constraint set $\mathcal{X}_{e}\subseteq\mathbf{R}^{n_{u}+n_{v}}$.

A general GCS optimization problem is | | | $\displaystyle\underset{H,\ \{x_{v}\}_{v\in\mathcal{W}}}{\text{minimize}}\quad$ | | $\displaystyle\sum_{v\in\mathcal{W}}f_{v}(x_{v})+\sum_{e=(u,v)\in\mathcal{F}}f_{e}(x_{u},x_{v})$ | | \(5\) | | | | subject to | | $\displaystyle H=(\mathcal{W},\mathcal{F})\in\mathcal{H},$ | | | | | | $\displaystyle x_{v}\in\mathcal{X}_{v},\quad\forall v\in\mathcal{W},$ | | | | | | $\displaystyle(x_{u},x_{v})\in\mathcal{X}_{e},\quad\forall e=(u,v)\in\mathcal{F},$ | | | where the variables are the (discrete) subgraph $H$ with vertex set $\mathcal{W}\subseteq\mathcal{V}$ and edge set $\mathcal{F}\subseteq\mathcal{W}^{2}\cap\mathcal{E}$ within an admissible subset of graphs $\mathcal{H}$ and the (continuous) variables $x_{v}$ for each vertex $v\in\mathcal{W}$.

Shortest Path Problem in GCS. For a given start vertex $s\in\mathcal{V}$ and target vertex $t\in\mathcal{V}$, a path $p$ is a sequence of distinct vertices that connects $s$ to $t$ via an edge subset $\mathcal{F}\subset\mathcal{E}$. The general problem can be specialized to the Shortest Path Problem (SPP) by taking $\mathcal{H}$ as the set of all paths, $\mathcal{P}$, from $s$ to $t$ in the graph $\mathcal{G}$. The shortest path problem is: | | | $\displaystyle\underset{p,\ x_{v}}{\text{minimize}}\quad$ | | $\displaystyle\sum_{e=(u,v)\in\mathcal{E}_{p}}\ell_{e}(x_{u},x_{v})$ | | \(6\) | | | | subject to | | $\displaystyle p\in\mathcal{P},$ | | | | | | $\displaystyle x_{v}\in\mathcal{X}_{v},\quad\forall v\in p,$ | | | | | | $\displaystyle(x_{u},x_{v})\in\mathcal{X}_{e},\quad\forall e\in\mathcal{E}_{p}$ | | | Although computationally hard in general, a tight mixed-integer formulation using network flow and perspective cone duality enables practically efficient solutions. A convex relaxation obtained by dropping binary constraints, combined with an inexpensive rounding scheme, yields certifiably near-optimal or even optimal solutions for many practical motion planning problems.

## Exact Convex Partitioning and Labeled GCS Construction

This section presents an exact convex partitioning algorithm that represents the traversable space as a union of convex sets and constructs a labeled graph $\mathcal{G}(\mathcal{V},\mathcal{E})$ encoding connectivity among free-space, key, and door regions. Key regions do not constrain traversability: an agent may pass through a key region freely, so key regions are permitted to overlap with free-space cells. Accordingly, only obstacles and doors contribute hyperplanes to the arrangement that partitions the environment. Key regions are incorporated as additional labeled nodes after the partition is constructed, by identifying which cells each key region intersects.

### III-A Cell Enumeration for Hyperplane Arrangements

We collect all distinct hyperplanes bounding $\mathcal{X}$ $\mathcal{O}$, and $\mathcal{D}$ into a *hyperplane arrangement* $\mathcal{H}=\{(h_{i},g_{i})\}_{i=1}^{n_{h}}$. Define the sign function $\mathcal{S}:\mathcal{X}\rightarrow\{+,-\}^{n_{h}}$ by This function assigns to each point in $\mathcal{X}$ a sign pattern, called a *marking*, that encodes which side of each hyperplane that point lies. Each *marking* $m\in\{+,-\}^{n_{h}}$ defines a (convex) polytopic *cell* These sets form an exact convex partition of the environment $\mathcal{X}$. Cells and their associated markings can be enumerated using the reverse search algorithm, which does a depth-first search to construct a spanning tree of the cells. For $n_{h}$ hyperplanes in $d$-dimensionals, the cell count is bounded by with the bound attained when the hyperplanes are in *general position* (no pair of hyperplanes is parallel and no point lies on more than $d$ hyperplanes). This exponential dimension dependence is an inherent computational bottleneck, which is mitigated in structured environments.

### III-B Labeled Graph Construction

Associating a vertex with each cell defines the vertex set $\mathcal{V}$. Two cells share a facet if and only if their markings differ in exactly one entry, so the edge set is $\mathcal{E}=\{(u,v)\mid d_{H}(m_{u},m_{v})=1\}$, where $d_{H}$ denotes Hamming distance. Door cells can be identified by their markings: for the subset $H\subset\mathcal{H}$ of hyperplanes defining any door, cells with $m_{i}=-$ for all $i\in H$ correspond to that door and are merged and labeled accordingly, forming the door vertices $\mathcal{V}_{\mathcal{D}}$. Obstacle cells and their associated vertices are similarly identified but then removed. The remaining vertices correspond to free space, forming free-space vertices $\mathcal{V}_{\mathcal{C}}$ and corresponding polytopes $\mathcal{C}_{v}$. Free-space nodes can be further merged to reduce graph size using an optimal complexity reduction algorithm based on branch and bound, or a greedy variant.

Key region labeling. Unlike obstacles and doors, key regions do not contribute hyperplanes to the arrangement and therefore do not influence the cell structure. After the partition is constructed and free-space cells are merged, each key region $K_{i}$ is associated with a key vertex $i\in\mathcal{V}_{\mathcal{K}}$ and connected to the graph by identifying all vertices $v\in\mathcal{V}_{\mathcal{C}}$ whose associated convex set $\mathcal{C}_{v}$ satisfies $\mathcal{C}_{v}\cap K_{i}\neq\emptyset$. These vertices are connected with an edge to the corresponding key vertex. In the common case where $K_{i}$ is fully contained within a single merged free-space cell, the key vertex is connected to exactly one free space vertex. When $K_{i}$ spans multiple cells (for instance, when a key region straddles a cell boundary introduced by a door or obstacle hyperplane), its vertex is connected to multiple free space vertices. The intersection test $\mathcal{C}_{v}\cap K_{i}\neq\emptyset$ reduces to a linear feasibility check since both sets are polytopes.

Our algorithm for exact convex partitioning and labeled GCS construction is summarized in Algorithm 1. The output is a labeled graph of convex sets $\mathcal{G}(\mathcal{V},\mathcal{E})$ with vertex partition $\mathcal{V}=\{\mathcal{V}_{\mathcal{C}},\mathcal{V}_{\mathcal{K}},\mathcal{V}_{\mathcal{D}}\}$. The polytopes corresponding to $\mathcal{V}_{\mathcal{C}}$ form an exact convex partition of the free space, and the edge set encodes connectivity among free-space, key, and door regions.

0: Environment 𝒳, obstacles 𝒪, keys 𝒦, doors 𝒟 (all in half-space representation) 0: Labeled graph of convex sets 𝒢(𝒱, ℰ) with 𝒱 = {𝒱𝒞, 𝒱𝒦, 𝒱𝒟} and exact convex partition 𝒳 \ (𝒪 ∪ 𝒟) = {𝒞i}i = 1nC 1: Form hyperplane arrangement ℋ from all boundaries of 𝒳, 𝒪, 𝒟 (key boundaries are excluded) 2: Enumerate non-empty cells and generate markings M(𝒳) (via reverse search) 3: Define vertex for each cell to form initial vertex set 𝒱 4: Set edge set ℰ between vertices whose markings differ in exactly one entry 6: Merge cells whose markings place them inside Di; label merged vertex as Di in 𝒱𝒟 9: Merge and discard corresponding cells and vertices 12: Create vertex Ki in 𝒱𝒦. Identify all vertices v ∈ 𝒱𝒞 = 𝒱 \ (𝒱𝒪 ∪ 𝒱𝒟) whose corresponding convex sets intersect Ki and connect them; 14: Merge free space nodes that preserve convexity (via optimal complexity reduction or greedy algorithm) Algorithm 1 Exact Convex Partition & Labeled GCS Construction

### Remark 1 (Partition quality and augmented GCS size)

The number of free-space nodes $|\mathcal{V}_{\mathcal{C}}|$ produced by Algorithm 1 directly affects the size of every subgraph in the augmented GCS and thus total solve time. Investing in better free-space merging (e.g., the branch-and-bound method of ) yields downstream computational savings that compound with the number of subgraph copies. Excluding key region boundaries from the hyperplane arrangement avoids introducing cuts into the free-space partition that serve no geometric purpose, directly reducing $|\mathcal{V}_{\mathcal{C}}|$ and thus the size of every subgraph in the augmented GCS.

## Augmented GCS Construction

In this section, we describe how to construct an augmented graph of convex sets that exactly encodes the key-door precedence constraints based on the labeled GCS $\mathcal{G}(\mathcal{V},\mathcal{E})$ from Section III. The augmented GCS is built as a layered collection of subgraphs, one per reachable key subset. Each subgraph is a copy of the base graph $\mathcal{G}$, with different edge sets according to the current set of collected keys. The augmented GCS consists of $n_{\mathcal{K}}+1$ layers, where each layer represents reachable key subsets of a certain cardinality. Augmented GCS construction begins with a start node connected to a free space vertex whose corresponding set contains the initial condition. By construction, every path connecting the starting node and a target node copy in the augmented GCS satisfies the key-door precedence constraints.

A simple 2-key environment is shown in Fig. 2, and the associated augmented GCS is shown in Fig. 3. We will refer to this as a running example throughout our description.

Figure 2: A key-door environment with 2 keys and 2 doors. The dashed blue line shows the optimal linear-piecewise solution, and the solid blue line shows the optimal 4th-order Bézier spline solution with a small penalty on curvature.

Figure 3: The augmented GCS for a simple 2-key environment. The start point is located in free space node 𝒞1 and the target set is adjacent to 𝒟2.

### IV-A Constructing the Augmented GCS

The Base Layer ($\ell=0)$. The base layer of the augmented GCS corresponds to the empty key set $\emptyset\in 2^{\mathcal{K}}$. The base subgraph $\mathcal{G}_{\emptyset}(\mathcal{V}_{\emptyset},\mathcal{E}_{\emptyset})$ has vertex set $\mathcal{V}_{\emptyset}=\mathcal{V}$ and edge set removing all edges incident to door nodes. The base layer for the 2-key environment is shown at the bottom of Fig. 3.

Layer $\ell$ ($1\leq\ell<n_{\mathcal{K}}$). Layer $\ell$ consists of subgraphs $\mathcal{G}_{S}$ for each reachable $\ell$-element key subset $S\in S_{\ell}\subset 2^{\mathcal{K}}$. The reachable key subsets are found with breadth- or depth-first search from each subgraph at the previous layer. The *width* of layer $\ell$ is $|S_{\ell}|$. Each subgraph $\mathcal{G}_{S}(\mathcal{V}_{S},\mathcal{E}_{S})$ has vertex set $\mathcal{V}_{S}=\mathcal{V}$ and edge set reinserting edges incident to doors unlocked by keys in $S$. For each key node $K_{v}\in S$, a directed edge of zero cost is added from the copy of key $K_{v}$ in $\mathcal{G}_{S-\{v\}}$ to its copy in $\mathcal{G}_{S}$, encoding the key collection event.

In our running 2-key example, both keys are reachable from the start node, so $S_{1}=\{\{1\},\{2\}\}$ and layer 1 has width 2. The subgraphs $G_{\{1\}}$ and $G_{\{2\}}$ are shown in the middle of Fig. 3, along with the directed edges from key nodes in $G_{\emptyset}$.

Layer $n_{\mathcal{K}}$. The final layer corresponds to the full key set $\mathcal{K}\in 2^{\mathcal{K}}$ and consists of a single subgraph $\mathcal{G}_{\mathcal{K}}(\mathcal{V}_{\mathcal{K}},\mathcal{E}_{\mathcal{K}})$ with vertex set $\mathcal{V}_{\mathcal{K}}=\mathcal{V}$ and edge set $\mathcal{E}_{\mathcal{K}}=\mathcal{E}$, the same edge set as $\mathcal{G}$. For each key node $v\in\mathcal{V}_{\mathcal{K}}$, a directed edge of zero cost is added from the key node copy in $\mathcal{G}_{\mathcal{K}-\{v\}}$.

In our 2-key example, the subgraph $G_{\{1,2\}}$ associated with the full key set is shown at the top of Fig. 3.

Target Merging. Finally, given a target node $t\in\mathcal{V}_{\mathcal{C}}$ whose corresponding set contains the terminal condition, we merge all its copies node throughout all layers and subgraphs into a single node that serves as the target node in the augmented GCS. The algorithm for constructing the augmented graph is summarized in Algorithm 2.

For each subgraph in the augmented graph, we associate the free space, key, and door regions with the corresponding node copies to obtain the augmented GCS. The machinery of the GCS motion planning framework can be applied to compute a shortest path from the start node to the (merged) target node in the augmented GCS.

0: Labeled graph 𝒢(𝒱, ℰ), with 𝒱 = {𝒱𝒞, 𝒱𝒟, 𝒱𝒦}, start node s connected to v ∈ 𝒱𝒞, target node t ∈ 𝒱𝒞 0: Augmented graph $\hat{\mathcal{G}}(\hat{\mathcal{V}},\hat{\mathcal{E}})$ 1: Create subgraph 𝒢∅(𝒱∅, ℰ∅), where 𝒱∅:= 𝒱, ℰ∅:= ℰ − {(u, v) ∈ ℰ ∣ u ∈ 𝒱𝒟 or v ∈ 𝒱𝒟} 3: Find all reachable ℓ-element key sets Sℓ ⊂ 2𝒦 from start node copy in all subgraphs with (ℓ − 1)-element key sets 5: Create subgraph 𝒢S(𝒱S, ℰS), where 𝒱S:= 𝒱, ℰS:= ℰ∅ ∪ {(u, v) ∈ ℰ ∣ u ∈ D(S) or v ∈ D(S)} 7: Add directed edge ℰS ← ℰS ∪ {(u, v)}, where u is the copy of v in 𝒱S − {v} 11: Merge copies of target node in all layers & subgraphs 12: return $\hat{\mathcal{G}}(\hat{\mathcal{V}},\hat{\mathcal{E}})$, where $\hat{\mathcal{V}}=\cup_{S\in\{S_{\ell}\}_{\ell=0}^{n_{\mathcal{K}}}}\mathcal{V}_{S}$, $\hat{\mathcal{E}}=\cup_{S\in\{S_{\ell}\}_{\ell=0}^{n_{\mathcal{K}}}}\mathcal{E}_{S}$ Algorithm 2 Augmented GCS Construction Size of the augmented GCS. The total number of subgraphs in the augmented GCS satisfies with equality when all keys are reachable from the start node $s$. This exponential dependence on the number of keys represents an important computational challenge. However, the subgraph lattice structure has a close correspondence with the landmark Bellman-Held-Karp algorithm, which will be made precise in Section VI. Fig. 4 shows subgraph lattices for up to 4 keys when all key subsets are reachable.

At another extreme, when the environment geometry requires keys to be collected in a fixed sequence, the augmented GCS reduces to a chain of $n_{\mathcal{K}}+1$ subgraphs. There are degenerate cases where some keys are not reachable at all, which reduces the count further. In intermediate problems, the geometry constrains the reachable key subsets and limits the size of the augmented GCS. The *maximum width* $\max_{\ell}|S_{\ell}|$ of the augmented graph is the key computational bottleneck.

Figure 4: Augmented GCS layer structure for base graphs with up to n𝒦 = 4 keys.

## Optimality of an Augmented GCS Shortest Path

In this section, we formally prove that a shortest path in the augmented GCS corresponds to an optimal solution of the original problem. Thus, the mixed-integer convex reformulation of applied to the augmented GCS exactly solves, up to the finite Bézier parameterization of the trajectory $q$. We will study the tightness of the convex relaxation in our numerical experiments. In the absence of a bound on the horizon $T$, an optimal solution is found if one exists. Otherwise, infeasibility is certified when the merged target node is disconnected from the start node $s$ in the augmented graph.

We now state the main optimality result.

### Theorem 1 (Optimality of Augmented GCS Shortest Path)

A shortest path from start node $s$ to the merged target node $t$ in $\hat{\mathcal{G}}(\hat{\mathcal{V}},\hat{\mathcal{E}})$ corresponds to an optimal solution of problem, up to a finite parameterization of the trajectory $q$ by Bézier curves.

The proof proceeds via three lemmas establishing soundness, completeness, and cost equivalence. The proofs for these lemmas are given in Appendix A.

### Lemma 1 (Soundness)

Every path in $\hat{\mathcal{G}}$ from start node $s$ to merged target node $t$ corresponds to a trajectory that satisfies the key-door precedence specification $\phi$.

### Lemma 2 (Completeness)

Every feasible trajectory $q^{*}$ of problem corresponds to some path in $\hat{\mathcal{G}}$.

### Lemma 3 (Cost Equivalence)

The cost of a path $\hat{p}$ in $\hat{\mathcal{G}}$ equals the cost of the corresponding trajectory in problem.

### Proof of Theorem 1. ‣ V Optimality of an Augmented GCS Shortest Path ‣ A Framework for Motion Planning with Temporal Logic Precedence Specifications via Augmented Graphs of Convex Sets")

By Lemmas 1. ‣ V Optimality of an Augmented GCS Shortest Path ‣ A Framework for Motion Planning with Temporal Logic Precedence Specifications via Augmented Graphs of Convex Sets") and 2. ‣ V Optimality of an Augmented GCS Shortest Path ‣ A Framework for Motion Planning with Temporal Logic Precedence Specifications via Augmented Graphs of Convex Sets") together establish a bijection between paths in $\hat{\mathcal{G}}$ and feasible trajectories of. By Lemma 3. ‣ V Optimality of an Augmented GCS Shortest Path ‣ A Framework for Motion Planning with Temporal Logic Precedence Specifications via Augmented Graphs of Convex Sets"), both objectives coincide over this bijection. Therefore: where $\hat{\mathcal{P}}$ denotes the set of all paths from $s$ to $t$ in $\hat{\mathcal{G}}$. A shortest path in $\hat{\mathcal{G}}$ thus recovers an optimal solution to, up to the finite Bézier curve parameterization of $q$. ∎

### Remark 2 (Trajectory Continuity at Layer Transitions)

When $\hat{p}$ crosses a directed inter-layer edge at a key node, the corresponding trajectory transitions between two copies of the same convex key set. Since both copies share identical geometry and the transition incurs zero positional displacement, the trajectory $q$ remains $C^{k}$-continuous for any finite order $k$ supported by the Bézier parameterization. This continuity condition must be explicitly included in the Bézier curve boundary constraints.

### Remark 3 (Repeated Key Visits)

If a trajectory visits the same key region $K_{i}$ multiple times, subsequent visits do not alter the accumulated key set $S_{j}$. The path $\hat{p}$ remains in the current subgraph without triggering additional layer transitions, which is consistent with the construction. A unique subgraph assignment is obtained by using the first visit to each key as the layer-transition trigger.

### Remark 4 (Finite Parameterization)

It is worth emphasizing that optimality holds up to the Bézier curve parameterization of $q$. Strictly, Theorem 1. ‣ V Optimality of an Augmented GCS Shortest Path ‣ A Framework for Motion Planning with Temporal Logic Precedence Specifications via Augmented Graphs of Convex Sets") recovers a finitely parameterized optimal trajectory, not a global optimum over all smooth curves. The gap introduced by finite-order Bézier parameterization is a separate approximation not addressed by the augmented GCS construction. However, the gap is small in practice for moderate Bézier order.

## Correspondence with the Bellman--Held--Karp Algorithm

The Bellman--Held--Karp (BHK) algorithm solves the Traveling Salesman Problem (TSP), finding a minimum cost tour amongst $n$ cities in $O(2^{n}n^{2})$ time via dynamic programming. Let $g(S,v)$ denote the minimum cost of a path that starts at a fixed origin $0$, visits exactly the cities in $S\subseteq\{1,\ldots,n\}$, and ends at city $v\in S$. The recurrence is: and the optimal tour cost is $\min_{v\neq 0}\left[g(\{1,\ldots,n\},v)+c_{v0}\right]$.

To demonstrate the cleanest correspondence between BHK and the augmented GCS structure, we consider the until-based specification for mandatory key collection, and further assume there are no doors, so that the door constraints are trivially satisfied. The specification then becomes requiring all keys to eventually be collected but not specifying a collection order.

### VI-A Structural Correspondence and Correspondence Theorem

### Definition 1 (BHK--GCS Dictionary)

Table I. ‣ VI-A Structural Correspondence and Correspondence Theorem ‣ VI Correspondence with the Bellman–Held–Karp Algorithm ‣ A Framework for Motion Planning with Temporal Logic Precedence Specifications via Augmented Graphs of Convex Sets") summarizes the correspondence between BHK and the augmented GCS: Subgraph 𝒢S, active vertex v Transition cost cuv GCS edge cost ℓe(xu, xv) Discrete pairwise distances Shortest path through continuous geometry Shortest path cost to Kv(S) in $\hat{\mathcal{G}}$ TABLE I: BHK–GCS Correspondence Dictionary

### Theorem 2 (BHK--Augmented GCS Correspondence)

Let the environment contain $n_{\mathcal{K}}$ keys and no doors, with all keys reachable from the start node. Then: The layer structure of $\hat{\mathcal{G}}$ implements exactly the BHK subset enumeration over $2^{n_{\mathcal{K}}}$ key subsets.

The inter-layer directed edges of $\hat{\mathcal{G}}$ implement exactly the BHK recurrence relation.

A shortest path in $\hat{\mathcal{G}}$ solves the same optimal subset-sequencing problem as BHK, generalized from discrete transition costs to shortest paths through continuous geometry.

### Proof of 1: Layer Structure = BHK Subset Enumeration

In BHK, the dynamic programming table is indexed by all subsets $S\subseteq\{1,\ldots,n\}$, processed in order of increasing cardinality $|S|=0,1,2,\ldots,n$.

In the augmented GCS, layer $\ell$ consists of subgraphs $\{\mathcal{G}_{S}:S\in\mathcal{S}_{\ell}\}$, one per reachable $\ell$-element key subset. The total number of subgraphs satisfies: with equality when all keys are reachable from the start node. The subgraphs at layer $\ell$ are in bijection with the BHK subproblems of cardinality $\ell$, and the construction processes them in order of increasing $\ell$. The enumeration structures are identical. ∎

### Proof of 2: Directed Inter-Layer Edges = BHK Recurrence

The BHK recurrence encodes the optimal cost to reach state $(S,v)$ is achieved by choosing the best predecessor $u$, taking the optimal path to state $(S\setminus\{v\},u)$, then paying transition cost $c_{uv}$.

In Algorithm 2 (lines 6--8), for each $S\in\mathcal{S}_{\ell}$ and each $K_{v}\in S$, a directed edge is added from $K_{v}^{(S\setminus\{v\})}$ in $\mathcal{G}_{S\setminus\{v\}}$ to $K_{v}^{(S)}$ in $\mathcal{G}_{S}$. The augmented GCS shortest path cost to $K_{v}^{(S)}$ satisfies: where $\hat{g}(S,K_{v})$ is the shortest path cost to $K_{v}^{(S)}$ in $\hat{\mathcal{G}}$ and $d_{\hat{\mathcal{G}}}(\cdot,\cdot)$ denotes intra-subgraph shortest path distance through the convex free space. Equation is the BHK recurrence with discrete transition costs $c_{uv}$ replaced by continuous geodesic distances $d_{\hat{\mathcal{G}}}(K_{u}^{(S\setminus\{v\})},K_{v}^{(S\setminus\{v\})})$ through the obstacle-laden convex geometry. ∎

### Proof of Part 3: Optimal Path = Generalized BHK Solution

Consider the restriction of the augmented GCS shortest path problem to key-node-to-key-node transitions. Collapse each subgraph $\mathcal{G}_{S}$ to a complete graph on its key nodes, with edge weights given by intra-subgraph shortest path distances. The resulting combinatorial problem is: where $v_{0}=s$, $v_{m+1}=t$, and $d_{\mathcal{G}}$ denotes free-space shortest path distance. This is a Shortest Hamiltonian Path problem on a subset of key sets with geodesic distances through convex obstacle-laden geometry replacing Euclidean city-to-city distances. A pure TSP tour can be obtained by setting the boundary constraints in with $q=q(T)=q_{0}\in\mathcal{K}_{1}$.

The augmented GCS shortest path problem therefore subsumes BHK: it solves the combinatorial key-sequencing problem (as BHK does for city ordering) and simultaneously optimizes the continuous trajectory within each sequencing decision. The two problems coincide precisely when the intra-subgraph geodesics are replaced by precomputed pairwise distances for singleton key regions, recovering the standard BHK setting. ∎

### VI-B Key Generalizations Beyond BHK

The augmented GCS framework strictly generalizes BHK along three axes.

### Specification

Classical TSP requires visiting all cities, which is analogous to the until-based specification with no doors. The augmented GCS framework allows much richer specifications via alternative temporal logic fragments, several of which will be discussed further in the next section. Including door regions incorporates precedence structure, and the release operator $K_{i}\,\mathcal{R}\,\neg D_{i}$ makes key collection optional unless geometrically necessary to reach the goal. This corresponds to a *generalized TSP on a subset*: the algorithm self-selects which keys to collect based on whether doing so shortens the path to the terminal condition.

### Geometry

BHK operates on a complete graph with precomputed pairwise distances. The augmented GCS operates directly on the continuous free space, computing geodesic distances through convex obstacle-free regions as part of the same optimization. Crucially, when door regions are present, the effective "distance" between two keys depends on which doors have been unlocked --- a state-dependent geometric coupling that BHK, which takes fixed distances as input, cannot express.

### Continuous-Combinatorial Coupling

In BHK, the combinatorial sequencing problem and the metric distances are decoupled; distances are fixed inputs. In the augmented GCS, the two are solved jointly: the convex optimization over Bézier curve control points within each subgraph is coupled to the shortest path search across subgraphs through shared vertex variables at subgraph boundaries. This coupling enables certifiably near-optimal solutions via convex relaxation, a guarantee that BHK does not provide in non-metric settings.

### VI-C Complexity Alignment

The augmented GCS operates within the same combinatorial complexity class as BHK. The worst-case number of subgraphs in the augmented GCS is $2^{n_{\mathcal{K}}}$, matching the $O(2^{n})$ BHK table size. The additional $O(n^{2})$ factor in BHK's $O(2^{n}n^{2})$ complexity corresponds to the $n_{\mathcal{K}}$ inter-layer edge additions per subgraph and the intra-subgraph shortest path solves, both of which are polynomial in $n_{\mathcal{K}}$ for fixed graph structure. By incorporating continuous geometry, the shortest path problem on the augmented GCS, via exact mixed-integer convex reformulation, inherits the same additional computational complexity challenges (NP-hardness) as the base GCS framework. However, in instances where the optimality gap is small between convex relaxation and rounding schemes, the continuous geometry optimization is carried out at no additional exponential cost.

## Specification Variations

We develop eight variations of the base key-door precedence specification, each obtained by modifying the STL formula and the corresponding augmented GCS construction. For each variation we state the specification, describe the modification to Algorithm 2, summarize the correctness result, and note the worst-case subgraph count. Full proofs of all correctness theorems appear in Appendix B.

### VII-A Variation 1: Mandatory Key Collection (Until Operator)

### Specification

Replace the release operator with the until operator: This is strictly stronger than when keys are not geometrically required: it both prevents passage through $D_{i}$ before $K_{i}$ is collected and guarantees $K_{i}$ is eventually collected.

### Augmented graph modification

### Construction 1

The layer structure and inter-layer directed edges are identical to Algorithm 2. The sole modification is to line 11: instead of merging all copies of $t$ across all layers, instantiate the target node only in the top-layer subgraph $\mathcal{G}_{\mathcal{K}}$: All other copies $t^{(S)}$ for $S\subsetneq\mathcal{K}$ are removed from $\hat{\mathcal{G}}$.

### Theorem 3

A shortest path from start node $s$ to target node $t^{*}$ in the augmented GCS of Construction 1 ‣ VII Specification Variations ‣ A Framework for Motion Planning with Temporal Logic Precedence Specifications via Augmented Graphs of Convex Sets") corresponds to an optimal solution of with specification $\varphi_{\mathcal{U}}$.

### Proof

Worst-case subgraph count: $O(2^{n_{\mathcal{K}}})$, unchanged from the base construction.

### Remark 5

When the geometry forces all keys to be collected, $\varphi_{\mathrm{base}}$ and $\varphi_{\mathcal{U}}$ are equivalent and both augmented graphs yield the same optimal solution.

### VII-B Variation 2: Pure Wayset Collection (TSP Variation)

As described in the previous section, this variation removes all door regions and requires the agent to visit every key region (wayset) before reaching the goal. It is the cleanest instantiation of the BHK correspondence: the augmented GCS implements BHK exactly, without the state-dependent geometry effect of door unlocking.

### Specification

Equivalently, $\varphi_{\mathrm{TSP}}=\bigwedge_{i}(\top\,\mathcal{U}\,K_{i})\land\mathcal{F}(\mathcal{T})$. No door regions are present in the environment.

### Augmented graph modification

### Construction 2

Remove all door nodes and edges from $\mathcal{G}$; the remaining graph has $\mathcal{V}=\{\mathcal{V}_{\mathcal{C}},\mathcal{V}_{\mathcal{K}}\}$. Apply Construction 1 ‣ VII Specification Variations ‣ A Framework for Motion Planning with Temporal Logic Precedence Specifications via Augmented Graphs of Convex Sets") (target restricted to the top layer), with the door-reinsertion step (Algorithm 2, line 5) vacuous since no doors exist. The result is $\mathcal{G}_{\mathcal{K}}$ at the top layer being identical to the original graph, and all inter-layer edges being zero-cost transitions at key nodes.

### Theorem 4

A shortest path from $s$ to $t^{*}$ in Construction 2 ‣ VII Specification Variations ‣ A Framework for Motion Planning with Temporal Logic Precedence Specifications via Augmented Graphs of Convex Sets") corresponds to an optimal solution of the continuous-geometry shortest Hamiltonian path problem: visiting all $n_{\mathcal{K}}$ waysets in obstacle-free convex space with minimum total cost.

### Proof

Worst-case subgraph count: $O(2^{n_{\mathcal{K}}})$.

### Remark 6

The Hamiltonian path begins at $q_{0}$, visits each wayset, and ends at $q_{T}$. To produce a pure TSP tour among waysets, the boundary constraints in can be replaced with $q=q(T)=q_{0}\in\mathcal{K}_{1}$. In this case, where a wayset is the source, the number of subgraphs reduces from $2^{n_{\mathcal{K}}}$ to $2^{n_{\mathcal{K}}-1}$.

### Remark 7 ($k$-of-$n$ wayset collection and connections to combinatorial optimization)

A natural generalization of Variation 2 requires the robot to visit *any* $k$ out of the $n_{\mathcal{K}}$ key regions before reaching the target. The augmented graph modification is simply to truncate the subgraph lattice after layer $k$ and merge target nodes across all subgraphs at that layer. The shortest path selects the optimal $k$-element key subset to collect. The worst-case subgraph count reduces from $O(2^{n_{\mathcal{K}}})$ to $O(\sum_{\ell=0}^{k}\binom{n_{\mathcal{K}}}{\ell})=O(n_{\mathcal{K}}^{k})$ for fixed $k$, a substantial reduction when $k\ll n_{\mathcal{K}}$.

In combinatorial optimization, the discrete counterpart of this variation is the *$k$-TSP* (selective TSP), which seeks the minimum-cost Hamiltonian path visiting exactly $k$ out of $n$ cities. The augmented GCS provides a continuous-geometry generalization of $k$-TSP.

### VII-C Variation 3: Ordered Key Collection

### Specification

Keys must be collected in the fixed sequence $K_{1},K_{2},\ldots,K_{n_{\mathcal{K}}}$:

### Augmented graph modification

### Construction 3

The augmented graph is a *linear chain* of $n_{\mathcal{K}}+1$ subgraphs: $\mathcal{G}_{\emptyset}\to\mathcal{G}_{\{1\}}\to\mathcal{G}_{\{1,2\}}\to\cdots\to\mathcal{G}_{\{1,\ldots,n_{\mathcal{K}}\}}$. At layer $\ell$, create only the single subgraph $\mathcal{G}_{\{1,\ldots,\ell\}}$ and add a directed edge only at $K_{\ell}$. The target $t^{*}$ is instantiated only in $\mathcal{G}_{\{1,\ldots,n_{\mathcal{K}}\}}$.

### Theorem 5

A shortest path from $s$ to $t^{*}$ in Construction 3 corresponds to an optimal solution of with $\varphi_{\mathrm{ord}}$.

### Proof

### Remark 8

The ordered construction requires exactly $n_{\mathcal{K}}+1$ subgraphs, reducing the worst-case augmented GCS size from $O(2^{n_{\mathcal{K}}})$ to $O(n_{\mathcal{K}})$ subgraphs. When key order is only partially specified, the augmented graph is a partial-order directed acyclic graph (DAG) on key subsets with complexity intermediate between $O(n_{\mathcal{K}})$ and $O(2^{n_{\mathcal{K}}})$.

### VII-D Variation 4: Disjunctive Keys

### Specification

Either key $K_{i}^{A}$ or key $K_{i}^{B}$ suffices to unlock door $D_{i}$:

### Augmented graph modification

### Construction 4

Introduce abstract keys $\tilde{\mathcal{K}}=\{\tilde{K}_{1},\ldots,\tilde{K}_{n_{D}}\}$. Assign both $K_{i}^{A}$ and $K_{i}^{B}$ the abstract label $\tilde{K}_{i}$. Build the subset lattice over $\tilde{\mathcal{K}}$ rather than individual keys. For each $\tilde{K}_{i}\in S$, add directed inter-layer edges at both physical key nodes: $K_{i}^{A,(S\setminus\{\tilde{K}_{i}\})}\to K_{i}^{A,(S)}$ and $K_{i}^{B,(S\setminus\{\tilde{K}_{i}\})}\to K_{i}^{B,(S)}$.

### Theorem 6

A shortest path from $s$ to $t$ in Construction 4 corresponds to an optimal solution of with $\varphi_{\mathrm{disj}}$.

### Proof

Worst-case subgraph count: $O(2^{n_{D}})$ over abstract keys. The only overhead relative to the base construction is a doubling of inter-layer edges per abstract key.

### Remark 9

This construction easily generalizes to more than two disjunctive keys. This variation also enables the framework to incorporate non-convex key regions that can be decomposed into a union of polytopes; the components then correspond to a set of disjunctive keys.

### VII-E Variation 5: Multi-Key Doors (Conjunctive Keys)

### Specification

Door $D_{i}$ requires a specified subset $\mathcal{K}_{i}\subseteq\mathcal{K}$ of keys:

### Augmented graph modification

The sole modification to Algorithm 2 is the door-unlocking mapping: Edges incident to $D_{i}$ are reinserted only when $S$ contains the *entire* required key set $\mathcal{K}_{i}$.

### Theorem 7

A shortest path from $s$ to $t$ in the augmented GCS with mapping (17 ‣ VII Specification Variations ‣ A Framework for Motion Planning with Temporal Logic Precedence Specifications via Augmented Graphs of Convex Sets")) corresponds to an optimal solution of with $\varphi_{\mathrm{multi}}$.

### Proof

Worst-case subgraph count: $O(2^{n_{\mathcal{K}}})$, unchanged. This variation composes naturally with Variation 4 to express arbitrary Boolean combinations of key requirements per door.

### VII-F Variation 6: Tools/Items (Multi-Door Keys)

### Specification

Key $K_{i}$ unlocks a set $D(K_{i})=\{D_{i_{1}},D_{i_{2}},\ldots\}$ of doors, so $n_{\mathcal{K}}<n_{D}$ in general, with assignment $\sigma:\{1,\ldots,n_{D}\}\to\{1,\ldots,n_{\mathcal{K}}\}$:

### Augmented graph modification

The subset lattice is built over keys $\mathcal{K}$ (not doors). The door-unlocking mapping becomes non-injective: When $K_{i}$ is added to $S$, all doors in $\mathbf{D}(K_{i})$ are simultaneously unlocked.

### Theorem 8

A shortest path from $s$ to $t$ in this augmented GCS corresponds to an optimal solution of with $\varphi_{\mathrm{tool}}$.

### Proof

### Remark 10

When $n_{\mathcal{K}}<n_{\mathcal{D}}$, the augmented GCS has at most $2^{n_{\mathcal{K}}}$ subgraphs rather than $2^{n_{\mathcal{D}}}$, yielding an exponential reduction relative to a naive door-indexed construction.

### Remark 11 (Reusable manipulation capabilities)

This variation admits a natural and rich interpretation beyond the literal key-door metaphor: a single "key" $K_{i}$ may represent a tool or item: a *reusable manipulation capability* that reconfigures the environment at multiple locations. A robot carrying a powered screwdriver can remove fasteners at any number of access panels; one equipped with a glass-breaking tool can breach multiple glazed barriers; a decontamination sprayer can neutralize hazardous zones at several points along a route. Similarly, a wire-cutting attachment can sever restraining cables at multiple junctions, a lubricant dispenser can free seized valves or hinges throughout a facility, and an RFID programmer can re-credential any number of electronically controlled gates sharing a common lock standard. In each case, acquiring the capability once (visiting $K_{i}$) simultaneously unlocks all corresponding "doors" $\mathbf{D}(K_{i})$, exactly as encoded by the non-injective mapping $\mathbf{D}(S)=\bigcup_{K_{i}\in S}\mathbf{D}(K_{i})$. The exponential reduction in subgraph count noted above (from $O(2^{n_{D}})$ to $O(2^{n_{\mathcal{K}}})$ when $n_{\mathcal{K}}<n_{D}$) reflects the practical observation that a small number of distinct tool types may unlock a much larger number of individual obstacles throughout the environment. This variation therefore provides a formal basis for manipulation planning problems in which the robot must reason jointly about which capabilities to acquire and in what order to deploy them across spatially distributed obstacles.

### VII-G Variation 7: Timed and Bounded-Horizon Constraints

### Specification

Key $K_{i}$ must be collected and door $D_{i}$ passed within specified time intervals:

### Augmented graph modification

Timed constraints are encoded in convex sets rather than graph topology; the layer structure is unchanged.

### Construction 5

\(i\) Extend each vertex variable to include a time component: $x_{v}=(q_{v},\tau_{v})$ with $\tau_{v}\geq 0$. (ii) For key node $K_{i}^{(S)}$, add convex constraint $\tau_{K_{i}}\in[a^{K}_{i},b^{K}_{i}]$; for door node $D_{i}^{(S)}$, add $\tau_{D_{i}}\in[a^{D}_{i},b^{D}_{i}]$. (iii) For each edge $(u,v)\in\hat{E}$, add monotonicity constraint $\tau_{v}\geq\tau_{u}$.

### Theorem 9

A shortest path from $s$ to $t$ in Construction 5 corresponds to an optimal solution of with $\varphi_{\mathrm{time}}$.

### Proof

Worst-case subgraph count: $O(2^{n_{\mathcal{K}}})$. All added constraints (time windows, monotonicity) are linear and preserve the GCS convex optimization structure.

### VII-H Variation 8: Conditional (If-Then) Specification

### Specification

If the agent visits *trigger region* $A_{i}$, then key-door precedence $K_{i}\,\mathcal{R}\,\neg D_{i}$ becomes active. Prior to visiting $A_{i}$, door $D_{i}$ is freely passable: This can be rewritten in pure STL as $\mathcal{G}(\neg A_{i}\vee(K_{i}\,\mathcal{R}\,\neg D_{i}))$, which enforces the precedence globally once the trigger is encountered.

### Augmented graph modification

### Construction 6

Index subgraphs by a joint state $(\mathbf{a},S)$ where $\mathbf{a}\in\{0,1\}^{n}$ is a binary trigger vector and $S\subseteq\mathcal{K}$ is the collected key set. The total subgraph lattice has at most $2^{n}\cdot 2^{n_{\mathcal{K}}}=2^{n+n_{\mathcal{K}}}$ subgraphs.

The first term captures doors whose precedence has not yet been triggered and are therefore freely passable. The second captures doors whose triggered precedence has been satisfied by collecting the corresponding key.

Trigger transition edges: For each trigger region $A_{i}$, add a directed edge at the trigger node from subgraph $\mathcal{G}_{(\mathbf{a},S)}$ to $\mathcal{G}_{(\mathbf{a}\cup\{i\},\,S)}$ upon visiting $A_{i}$: This transition removes the freely-passable status of $D_{i}$ (setting $a_{i}=1$), activating the precedence.

Key transition edges: Identical to the base construction, now additionally indexed by $\mathbf{a}$: Edge sets: For subgraph $\mathcal{G}_{(\mathbf{a},S)}$, the edge set is: All other aspects of Algorithm 2 are unchanged.

### Theorem 10

A shortest path from $s$ to $t$ in the augmented GCS of Construction 6 Specification ‣ VII Specification Variations ‣ A Framework for Motion Planning with Temporal Logic Precedence Specifications via Augmented Graphs of Convex Sets") corresponds to an optimal solution of problem with specification $\varphi_{\mathrm{cond}}$.

### Proof

### Remark 12

The conditional specification subsumes the base release specification as the special case $A_{i}\equiv\top$ (trigger always active from the start), recovering $a_{i}=1$ for all $i$ at $t=0$.

### Remark 13

Chained conditionals of the form $A_{i}\Rightarrow(B_{i}\Rightarrow(K_{i}\,\mathcal{R}\,\neg D_{i}))$ are encodable by composing trigger vectors: the state becomes $(\mathbf{a}^{},\mathbf{a}^{},S)$ with $|\mathbf{a}^{}|=|\mathbf{a}^{}|=n$, yielding subgraph count $O(4^{n}\cdot 2^{n_{\mathcal{K}}})$. Each level of nesting multiplies the trigger component of the state space by a factor of 2, remaining singly exponential in total atom count.

### Remark 14

Two sub-variations replace the release consequent with stronger obligations. The first uses an until consequent, where the trigger incurs an *obligation* to collect the key before the door may be passed. The second omits the door entirely, requiring only that $K_{i}$ be visited before mission completion. Both sub-variations are naturally interpreted as a sensor-based event when the expected measurement is known at planning time: the trigger fires when a measurement at the current position exceeds a threshold, incurring an obligation to perform a subsequent action $K_{i}$. For example, a decontamination robot detecting radiation above a threshold at location $A_{i}$ incurs an obligation to visit a decontamination station $K_{i}$ before returning to base; or an inspection drone detecting a blade anomaly at turbine $A_{i}$ incurs an obligation to acquire a confirmatory close-range observation at $K_{i}$. When the trigger condition is unknown until execution, the obligation $\mathcal{F}(K_{i})$ can be injected dynamically via event-triggered replanning.

### Remark 15 (Combining and Composing Variations)

The variations are largely orthogonal and can be combined for form highly expressive mission specifications. Timed constraints compose cleanly with all other variations because they modify only convex sets, not graph topology. For example, combining with Variation 2 (ordered keys) requires only appending time windows to the linear chain node sets.

### VII-I Fragment Admissibility and the Double-Exponential Barrier

The computational advantage of the augmented GCS over general-purpose temporal logic motion planning tools stems from a structural property of the specification fragments it targets. The classical pipeline for arbitrary STL or LTL motion planning faces two sequential exponential blowups: constructing a finite automaton from the formula costs $2^{O(|\varphi|)}$ in formula length, and forming the product of that automaton with the planning state space multiplies the exponential again, yielding double-exponential complexity in the worst case. The augmented GCS avoids the double blowup by building the subgraph structure directly from the semantics of the formula, exploiting the fact that each specification variation in Section VII admits a *progress monitor* (a deterministic finite-state tracker of which actions have been completed and which regions are currently accessible) whose state space is at most singly exponential in the number of logical atoms. The augmented GCS subgraph lattice is precisely this progress monitor embedded in the continuous geometry, giving a construction that is singly exponential in $n_{\mathcal{K}}$ by design.

This *bottom-up* philosophy --- identifying specific fragments whose structure can be exploited directly, rather than applying a top-down pipeline to arbitrary formulas --- is the organizing principle behind the specification library developed here. Each variation in Section VII represents a fragment for which the progress monitor is known, the modification to the augmented GCS construction is explicit and tractable, and the correctness proof is tractable. The natural question is how far this library can be extended: which additional STL fragments admit singly exponential progress monitors and therefore tractable augmented GCS encodings, and where does the double-exponential barrier become unavoidable? Precisely characterizing this *admissibility boundary*, including a formal definition of admissible fragments, a hierarchy organizing them by the algebraic structure of their progress states, and syntactic sufficient conditions for admissibility, is the subject of ongoing work and will be developed in a companion paper expanding the specification library.

## Numerical Experiments

In this section, we demonstrate and evaluate the augmented GCS framework for solving two key-door benchmarks, procedurally generated key-door mazes, and a hand-designed key-door environment from a classic video game. Experiments were performed on a laptop with an Apple M2 CPU and 8GB RAM, unless otherwise noted. The underlying convex optimization solver was MOSEK, accessed via the GCS components from the Drake Python bindings. The relaxed optimality gap is reported as where $C_{\mathrm{relax}}$ lower-bounds the optimal value and $C_{\mathrm{round}}$ is the rounded solution cost. We use the rounding implementation from with 100 trials and 10 max paths. All experiments minimize path length only, with $\alpha=1$ and $\beta=0$ in problem. The source code is publicly available at

### VIII-A Key-Door Environments from

2-Key Environment. We first consider the simple key-door environment with two keys and two doors shown in Fig. 2. The robot must pick up two keys to open two doors in order to reach the target set, which can be written as the STL formula $\varphi=\mathcal{K}_{1}\mathcal{R}\neg\mathcal{D}_{1}\wedge\mathcal{K}_{2}\mathcal{R}\neg\mathcal{D}_{2}\wedge\mathcal{F}\,\mathcal{T}$.

We created an exact convex partition and labeled GCS by inspection and used Algorithm 2 to construct the augmented GCS, shown in Fig. 3. The augmented GCS construction time is 0.0108 seconds and the solving time is 0.249 seconds, certified globally optimal with $\delta_{\mathrm{relax}}=0$. Compared with an approach that uses general-purpose temporal logic tools, our augmented GCS construction is about 80$\times$ faster.

5-Key Environment. We also solved a 5 key-door environment. The STL formula can be written as We extracted an exact convex partition by inspection, which produces a graph with 7 free space cells, 5 key cells, 5 door cells. The augmented GCS constructed by Algorithm 2 contains six layers with nine subgraphs. The augmented GCS construction time is 0.0423 seconds and the solving time is 1.573 seconds, certified globally optimal with $\delta_{\mathrm{relax}}=0$. Compared with an approach that uses general-purpose temporal logic tools, our augmented GCS construction is more than 50000$\times$ faster, and our solve time is about 3.5$\times$ faster.

More generally, compared with the top-down, full-grammar pipeline targeted , our bottom-up approach is *exponentially* faster by exploiting the structure in the specification fragment, which will compound further with problem size. This is due to the fundamental doubly exponential complexity of converting an arbitrary temporal logic specification into a finite automaton versus the singly exponential complexity of our fragments, matching BHK.

## of keys

Form GCS (sec) TABLE II: Numerical Experiments with Key-Door Mazes Figure 5: (a) key-door maze, (b) graph of maze.

### VIII-B Numerical Experiments on Key-Door Mazes

To further evaluate the augmented GCS framework, we developed a maze benchmark generator (described in Appendix C) that produces key-door maze environments of controllable size and width. Fig. 5 shows a partitioned and merged maze and its associated graph.

We evaluate the performance of the proposed approach on a set of key-door mazes created by the our generator. The convex free space partition and labeled GCS are constructed from the maze generation process without requiring Algorithm 1. From the labeled GCS for each maze, we used Algorithm 2 to construct the augmented GCS and then solved a shortest path problem on the augmented GCS based on using Drake and Mosek. Table II shows the results of 29 experiments. For each experiment, we report the maze size; number of vertices in the base GCS $|\mathcal{V}|$; number of edges in the base GCS $|\mathcal{E}|$; number of keys $n_{\mathcal{K}}$; maximum width of the augmented GCS; number of vertices in the augmented GCS $|\hat{\mathcal{V}}|$; number of edges in the augmented GCS $|\hat{\mathcal{E}}|$; the augmented GCS construction time; the augmented GCS solving time; and an upper bound on the optimality gap $\delta_{\mathrm{relax}}$. Fig. 6 shows a 3-key, 3-door, 99$\times$`<!-- -->`{=html}99 maze, which we solve we solve to global optimality within $1.5s$.

Figure 6: A 99×99 maze with 3 keys and 3 doors.

Discussion. We make several observations based on the results in Table II. First, our approach scales to far larger problems than reported , obtaining optimal or near-optimal solutions for up to $6$k-node base graphs, up to 10 keys, and up to an augmented GCS max width of 35. The augmented GCS construction times are within a few seconds across all instances, and the solve times scale mainly with the number of augmented GCS nodes and edges, which strongly depend on the maximum width and reflect the complexity of mission logic; this is illustrated graphically in Fig. 7. The optimality gap is certified to within 2% of the global optimum across all instances, with many cases globally optimal.

Figure 7: Log-log plot showing singly exponential growth of solve time vs. augmented GCS node count, which depends strongly on max width.

### VIII-C Pure Wayset Collection (TSP) Experiments

We now illustrate Variation 2 (pure wayset collection (TSP)) from the specification library in Section VII. Here, the augmented GCS produces the full $2^{n_{\mathcal{K}}}$ BHK subgraph lattice with maximum width, which allows us to push Algorithm 2 to its limit. These experiments were performed on a laptop with an Intel Core Ultra 7 258V and 32 GB of RAM.

We generated random instances of region-TSP with $n_{\mathcal{K}}\in\{3,5,7,9,11\}$ waysets and no obstacles. Each instance uniformly places $n_{\mathcal{K}}$ center points in $^{2}$ and then creates polytopic waysets from a convex hull of random points around the center. Since there are no obstacles, each subgraph is a complete graph on key nodes with $n_{\mathcal{K}}(n_{\mathcal{K}}-1)$ edges. For each instance the shortest path problem on the augmented GCS is solved using Drake and Mosek, using the first key vertex in $\mathcal{V}$ as both the start and target. Table III Experiments ‣ VIII Numerical Experiments ‣ A Framework for Motion Planning with Temporal Logic Precedence Specifications via Augmented Graphs of Convex Sets") shows the results from the 500 experiments, 100 per $n_{\mathcal{K}}\in\{3,5,7,9,11\}$. For each $n_{\mathcal{K}}$ we report the number of vertices and edges in the augmented graph, the augmented GCS construction time, and the mean and medium solve time and optimality gap. Figure 8 Experiments ‣ VIII Numerical Experiments ‣ A Framework for Motion Planning with Temporal Logic Precedence Specifications via Augmented Graphs of Convex Sets") shows one instance of $n_{\mathcal{K}}=11$, with certified globally optimal trajectory.

TABLE III: Pure Waypoint Collection (TSP) Experiments Figure 8: Optimal wayset solution for n𝒦 = 11.

Discussion. Table III Experiments ‣ VIII Numerical Experiments ‣ A Framework for Motion Planning with Temporal Logic Precedence Specifications via Augmented Graphs of Convex Sets") shows singly exponential scaling with $n_{\mathcal{K}}$ for both augmented GCS size and solve times, matching the BHK algorithm. The optimality gaps show that most instances are certified globally optimal. Further analysis reveals that non-zero optimality gap is typically due to the relaxation, not the rounding.

Although the singly exponential scaling of our approach is far better than the doubly exponential scaling of top-down approaches for arbitrary STL formulas, these results strongly motivate the use of heuristics and pruning strategies that trade solution quality for speed. The BHK correspondence suggests that 70 years of research on TSP approximation algorithms may provide inspiration for scalable approximation schemes with suboptimality bounds. An exploration of how such heuristics could be translated to the augmented GCS framework was initiated , where high quality solutions can be obtained for up to $n_{\mathcal{K}}=100$ waysets within one minute solve times.

### VIII-D Hand-Designed Maze: Legend of Zelda Eagle Dungeon

Procedurally generated mazes provide statistical coverage of the augmented GCS parameter space, but their key-door dependencies are placed algorithmically rather than designed by a human expert. To complement the maze benchmark, we consider the Eagle Dungeon (Level 1) from *The Legend of Zelda*, a canonical example of a human-designed environment in which sequential access constraints arise intentionally from the designer's puzzle logic. Video game dungeons are a particularly apt benchmark class for key-door planning frameworks, since game designers invest substantial effort calibrating precedence structures to be non-trivial but tractable, a regime where algorithmic methods should demonstrate clear value.

### Environment description

The Eagle Dungeon, shown in Fig. 9, consists of a grid of interconnected rooms arranged on a $16\times 16$ tile map. Each room contains obstacles made of one or more axis-aligned tiles. We manually extracted the half-space representations of all obstacles and obtained a polytopic partition of the free space using Algorithm 1 with greedy merging. The dungeon contains $n_{\mathcal{K}}=6$ small keys, $n_{D}=6$ locked doors; the terminal goal is the Triforce room at the dungeon's end (top right). The start position is the dungeon entrance at the bottom. The resulting labeled graph, shown in Fig. 10, has $|\mathcal{V}|=153$ vertices and $|\mathcal{E}|=440$ edges. The dungeon's room-graph and obstacle structure produces a labeled GCS with a substantial number of free-space vertices relative to the number of logical constraints, placing it in a qualitatively different regime from the mazes of Table II.

Figure 9: The Legend of Zelda Eagle Dungeon.

Figure 10: Base GCS of the Eagle Dungeon.

Figure 11: Augmented GCS of the Eagle Dungeon.

Figure 12: The solid blue line shows the global optimal solution. The dashed red line shows a feasible solution obtained from 100 rounded trials, with relaxation gap 17.9% and true optimality gap 9.53%.

TABLE IV: Zelda Dungeon Experiments

### Specification

The small keys in the Eagle Dungeon are *fungible* and *consumable*: any small key opens any locked small-key door within the dungeon, and a single small key is consumed upon passage through any locked door and cannot be reused. For the purposes of this experiment we adopt a simplified specification that assigns each small key a fixed identity (key $K_{i}$ unlocks door $D_{i}$)^11^1We also omit the dungeon's key item (in this case, the bow) and move one locked door from the top left towards the item room to the top right towards the triforce room. In the original game, the Eagle Dungeon can be completed without acquiring the bow., which is an instance of the base release specification $\varphi_{\mathrm{base}}$: The full Zelda mechanic is a richer specification than and lies outside the variation library of the current paper. The simplified specification therefore represents a relaxation of the true game logic in which key identities are fixed rather than fungible. We discuss the implications of this gap and the path toward closing it below. The augmented GCS associated with this specification is obtained from Algorithm 2, has max width 3, and is shown in Fig. 11. Solving a convex relaxation of the shortest path problem on the augmented GCS with 100 rounding trials in about 10 seconds yields the feasible trajectory in Fig. 12 with relaxation gap $\delta_{\mathrm{relax}}=$ 17.9%. Also shown is a globally optimal path, obtained by solving the exact mixed-integer convex reformulation of the shortest path problem on the augmented GCS, requiring about 6 hours.

### Discussion

The convex relaxation exhibits a relatively large relaxation gap on the Eagle Dungeon compared to procedurally generated maze instances. We attribute this mainly to the environment geometry. In particular, certain rooms contain numerous small obstacles, resulting in a fine partition of the free space into many small interconnected convex cells. This induces many distinct paths between room entrances and exits. In the GCS relaxation, flow is distributed fractionally across these alternative routes, and the rounding procedure recovers a discrete path by sampling edges according to their fractional weights. With a limited number of trials, the algorithm explores only a small portion of this combinatorial path space, often yielding suboptimal or duplicated paths. Increasing the number of rounding trials (e.g., from 100 to 1000) improves coverage of candidate paths and reduces the optimality gap to $11.9\%$, at the cost of substantially increased computation time; see Table IV.

Furthermore, we observe that the relaxation itself is relatively loose in this instance. Solving the mixed-integer program yields a globally optimal cost of $192.8$, while the relaxation cost is $178.6$. Thus, it is worth emphasizing that the relaxation gap may be attributed to either suboptimality or poor quality of the lower bound (or both). This highlights that the observed optimality gap is influenced not only by the effectiveness of the rounding procedure, but also by the tightness of the convex relaxation, both of which are adversely affected by the highly fragmented structure of the environment.

Investigating relaxation tightness on human-designed environments with irregular geometry (as opposed to procedurally generated mazes) is an interesting direction for future work, and motivates developing tighter mixed-integer formulations or problem-specific rounding strategies for this instance class.

### Specification gap and future directions

The Eagle Dungeon highlights a natural limit of the current specification library: the fungible-consumable-key mechanic, in which a single key is expended upon door passage and cannot be reused, is not captured by any of the eight variations in Section VII. Extending the augmented GCS framework to fungible and consumable keys, and more generally developing the full specification library needed to handle the rich precedence structures found in human-designed environments, is a natural direction for future work.

More broadly, human-designed environments (game dungeons, building floor plans with access-controlled zones, multi-stage inspection routes) represent a benchmark class qualitatively distinct from procedurally generated instances. Their key-door structures are crafted to be challenging yet solvable, their geometry is irregular and purposeful, and their optimal solutions carry semantic meaning that procedural benchmarks lack. We view the Eagle Dungeon as an initial representative of this class and anticipate that a systematic benchmark library drawn from hand-designed environments will be a productive avenue for evaluating and extending the augmented GCS framework.

## Conclusion

We presented a framework for motion planning with logical precedence specifications based on augmented graphs of convex sets. The augmented GCS encodes key-door precedence constraints exactly in the graph topology, enabling the GCS shortest-path machinery to simultaneously optimize key-collection sequencing and continuous trajectory geometry. We provided formal proofs of optimality, established a precise correspondence with the Bellman--Held--Karp dynamic programming algorithm that reveals the augmented GCS as a continuous-geometry generalization of the shortest Hamiltonian path and TSP problems, and developed a library of eight systematic variations based on STL fragments that admit tractable augmented GCS encodings. Extensive numerical experiments confirmed exponential speedup over general-purpose temporal logic tools and solution quality within 2% of globally optimal across almost all tested instances.

Several limitations of the current framework motivate future work. Scaling to environments with large numbers of keys and high augmented GCS width will likely require heuristics or approximations that trade off computation time with solution quality; the BHK correspondence suggests that TSP approximation algorithms may provide inspiration for systematic approximation schemes with suboptimality bounds. The convex partition quality (number of free-space nodes) significantly affects solve time, and adaptive or online partition refinement strategies would be valuable. Extending the framework to dynamic environments, stochastic settings, and multi-agent problems, where the key-door precedence structure and GCS convexity can still be exploited, are natural directions. Finally, integrating the offline augmented GCS planning with real-time feedback control and online replanning for environments with uncertainty and disturbances remains an important open challenge.
