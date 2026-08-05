<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

STITCHER: Real-Time Trajectory Planning with Motion Primitive Search

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Autonomous high-speed navigation through large, complex environments requires real-time generation of agile trajectories that are dynamically feasible, collision-free, and satisfy constraints. Most modern trajectory planning techniques rely on numerical optimization because high-quality, expressive trajectories that satisfy constraints can be systematically computed. However, strict requirements on computation time and the risk of numerical instability can limit the use of optimization-based planners in safety-critical situations. This work presents an optimization-free planning framework called STITCHER that leverages graph search to generate long-range trajectories by stitching short trajectory segments together in real time. STITCHER is shown to outperform modern optimization-based planners through its innovative planning architecture and several algorithmic developments that make real-time planning possible. Simulation results show safe trajectories through complex environments can be generated in milliseconds that cover tens of meters.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Planning collision-free and dynamically feasible trajectories through complex environments in real-time is a necessary capability for many autonomous systems. As a result, trajectory planning has received considerable attention from the research community, but achieving the reliability and computational efficiency required for real-world, safety-critical applications remains a challenge. In particular, few methods have guarantees in terms of trajectory optimality and time/memory complexity without sacrificing trajectory expressiveness, length, or computation time. Our proposed approach addresses this gap by combining optimal control theory with graph search to generate near-optimal trajectories over long distances in real-time without online optimization.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Numerical optimization has emerged as the principal approach for trajectory design in autonomous systems. This is because it allows for natural expression of performance index and constraints, and high-quality solutions for complex problems. Continuous variable methods employ gradient descent to jointly optimize the coefficients of basis functions and waypoint arrival times, while mixed-integer variable methods utilize integer variables to impose collision constraints along a discretized trajectory. Despite their popularity, optimization methods lack time complexity bounds that can be known a priori, and can scale poorly with trajectory length, especially if integer variables are used. Numerical stability can also be a problem with these methods.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

A computationally efficient alternative is to continuously replan with a library of short-duration trajectories, i.e., motion primitives, that can be efficiently evaluated. However, this framework can introduce myopic or suboptimal behavior that is exacerbated in large or complex environments. Subsequent work has attempted to pose the problem as a graph search with nodes and edges being desired states and motion primitives. Although this enables long-range trajectories, search times can be extremely high, and it is non-trivial to design an admissible heuristic that expedites the search.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In this work, we introduce a new trajectory planning algorithm called STITCHER, which enables real-time motion primitive search over long distances in complex environments. STITCHER utilizes a novel three-stage planning architecture to generate expressive trajectories by *stitching* motion primitives together. Specifically, given a set of waypoints computed in the first stage, we create a velocity graph by sampling velocities at each waypoint, and employ dynamic programming to compute the cost-to-go for each node in the graph. The cost-to-go is then used as a heuristic to efficiently guide the motion primitive search in the third stage. We also propose a greedy graph pre-processing step to form a compact motion primitive search graph. We prove all graphs are finite, and that the proposed search heuristic is admissible. These properties guarantee i) *a priori* time and memory complexity bounds and ii) trajectory optimality with respect to the graph discretization set. To further reduce computation time, we improve the collision checking procedure from by leveraging the known free space from previous trajectory evaluations, bypassing the rigidity and computational complexity of free space decomposition.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Additionally, we show that employing a simple sampling procedure in the final search stage is effective at pruning trajectory candidates that violate complex state or actuator constraints. STITCHER was extensively tested in two simulation environments, and compared with two state-of-the-art real-time optimization-based planners. Results show that STITCHER consistently generates trajectories faster with comparable trajectory execution times.

<!-- chunk {"id": "body-0008", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

Optimization-based trajectory planners can be categorized using several criteria, but the clearest delineation is whether the method uses continuous or integer variables. For methods that use only continuous variables, the work by reformulated to jointly optimize over polynomial endpoint derivatives and arrival times for a trajectory passing through waypoints. Collisions were handled by re-optimizing the trajectory with added waypoints. Oleynikova et al. represented obstacles using an Euclidean Signed Distance Field (ESDF) which was incorporated into a nonconvex solver as a soft constraint. Zhou et al. used a similar penalty-based method but introduced a topological path search to escape local minima. An alternative approach is to decompose the occupied or free space into convex polyhedra which can be easily incorporated as constraints in an optimization. The methods in treat these constraints as soft while efficiently optimizing over polynomial trajectory segments that must pass near waypoints. One can also use the free-space polyhedra to formulate a mixed-integer program to bypass the nonconvexity introduced by having unknown waypoint arrival times, but at the expense of poor scalability with trajectory length and number of polyhedra.

<!-- chunk {"id": "body-0009", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

Motion primitive planners have been proposed as an alternative to optimization-based planners to address computation and numerical instability concerns. Initial work on motion primitives for quadrotors leveraged differential flatness and known optimal control solutions to efficiently compute point-to-point trajectories. Later work employed motion primitives for receding horizon collision avoidance where motion primitives were generated online by sampling desired end states, and selected based on safety and trajectory cost. While computationally efficient, the behavior of these planners can be myopic, leading to suboptimal behavior in complex environments. One way to address this behavior is to extend standard search-based algorithms, which typically use discrete action sets, to a lattice of motion primitives. The main issue with search-based motion primitive planners is the search space can become untractable, and with the non-triviality of constructing an admissible search heuristic, search times are not suited for real-time use. Recently, proposed an efficient waypoint-constrained minimum-time motion primitive search in velocity space using a double integrator model. The search is real-time but the resulting bang-bang acceleration profile is dynamically infeasible for aerial vehicles.

<!-- chunk {"id": "body-0010", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

A final smoothing step, e.g., model predictive contouring control, is required to achieve sufficient trajectory smoothness.

<!-- chunk {"id": "body-0011", "role": "body", "section": "PROBLEM FORMULATION", "weight": 1.0} -->

In this work, we are concerned with solving the following trajectory planning problem where $\mathbf{x}\in\mathbb{R}^{n}$ is the state that must satisfy state $\mathcal{X}_{s}$ and obstacle (collision) $\mathcal{X}_{obst}$ constraints, $\mathbold{u}\in\mathbb{R}^{m}$ is the control input that must satisfy actuator constraints $\mathcal{U}$, $A\in\mathbb{R}^{n\times n}$ and $B\in\mathbb{R}^{n\times m}$ govern the system's dynamics, and $r:\mathbb{R}_{+}\rightarrow\mathbb{R}_{+}$ and $q:\mathbb{R}^{n}\times\mathbb{R}^{m}\rightarrow\mathbb{R}_{+}$ are the terminal and stage cost, respectively.

<!-- chunk {"id": "body-0012", "role": "body", "section": "PROBLEM FORMULATION", "weight": 1.0} -->

The goal is to find an optimal final time $T^{*}$ and feasible optimal state trajectory $\mathbf{x}^{*}(t)$ with a corresponding control input $\mathbold{u}^{*}(t)$ for $t\in[0,\,T^{*}]$ that steers the system from an initial state $\mathbf{x}_{0}$ to a desired final state $\mathbf{x}_{f}$ that minimizes the cost functional $J$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "PROBLEM FORMULATION", "weight": 1.0} -->

While the dynamics are linear in Equation 1, differentially flat nonlinear systems, e.g., quadrotors, can be represented as a linear system with a state vector $\mathbf{x}=[\mathbold{r},\,{\mathbold{v}},\,{\mathbold{a}},\,\dots,\,\mathbold{r}^{(p\!-\!1)}]^{\top}$ and control input $\mathbold{u}=\mathbold{r}^{(p)}$ where $\mathbold{r}=(x,\,y,\,z)^{\top}$ is the vehicle's position in some reference frame.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Background: Motion Primitives", "weight": 1.0} -->

We define motion primitives to be closed-form solutions to certain optimal control problems. In this work, we will restrict our attention to the following two optimal control problems. The formulations will be presented for a single axis, but can be repeated for all three position coordinates.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Background: Motion Primitives", "weight": 1.0} -->

Minimum-Time Double Integrator: Given an initial state $({s}_{0},\,{{v}}_{0})\in\mathbb{R}^{2}$ and desired final state $({s}_{f},\,{{v}}_{f})\in\mathbb{R}^{2}$, the minimum-time double integrator optimal control problem is where the final time $T$ is free. The problem is known to have a bang-bang control profile detailed. The control input switching times, which fully characterizes the solution, can be efficiently computed by solving a quadratic equation.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Background: Motion Primitives", "weight": 1.0} -->

Linear Quadratic Minimum-Time $p$-th Order Integrator: Smooth trajectories can be generated by solving the linear quadratic minimum-time (LQMT) optimal control problem, where $\rho>1$ penalizes the final time. The final time $T$ and all terminal states except position and velocity are free. The final time can be found with a root-finding method such as QR algorithm because the cost functional can be expressed as a polynomial in terms of $T$ and the known boundary conditions, detailed. State constraints are omitted from Equation 3 as it is more efficient to prune many candidate trajectories once the final time is known, as discussed in Section IV-D.

<!-- chunk {"id": "body-0017", "role": "body", "section": "METHODOLOGY", "weight": 1.0} -->

STITCHER generates a full-state trajectory by stitching collision-free, dynamically feasible trajectory segments together through graph search. At its core, STITCHER searches over closed-form solutions, i.e., motion primitives, to optimal control problems like those discussed above. These solutions serve as a basis for the solution space to Equation 1. To achieve real-time performance, STITCHER utilizes a three stage planning process where the final motion primitive search is guided by two other planners run sequentially (see Fig. 2). In Stage 1 (left), A\* algorithm is used to produce a sparse geometric path, i.e., waypoints, in the free space of the environment. In Stage 2 (middle), nodes representing sampled velocities at the waypoints are formed into a velocity graph where dynamic programming is used to compute the minimum time path between nodes using a control-constrained double integrator model. This step is critical for constructing an admissible heuristic to guide the full motion primitive search, and is one of the key innovations that enables real-time performance.

<!-- chunk {"id": "body-0018", "role": "body", "section": "METHODOLOGY", "weight": 1.0} -->

It is important to note that the optimal "path" in velocity space is never used; computing the cost-to-go is the primary objective as it serves as an admissible heuristic for motion primitive search as shown in Section V-B. In Stage 3 (right), an A\* search is performed over motion primitives using a higher-order dynamical model and the heuristic from Stage 2. At this stage, position and all higher-order derivatives are considered, yielding a full state trajectory that can be tracked by the system. Collisions and other state and control input constraints are also checked in this stage. The remainder of this section expands upon each component of STITCHER.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Stage 1: Forward Geometric Path Search", "weight": 1.0} -->

STITCHER requires a sequence of waypoints that guides the motion primitive search by limiting the size of the search space. This can be done by generating a collision-free geometric path (see Fig. 2 left) through the environment with A\* search or any other discrete graph search algorithm where the environment is represented as a 3D voxel occupancy grid. Let the collision-free, geometric path generated by a discrete graph search algorithm be composed of points $\mathcal{O}=\{\mathbold{o}_{1},\mathbold{o}_{2},...,\mathbold{o}_{H}\}$ where $\mathbold{o}_{i}\in\mathbb{R}^{3}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A Stage 1: Forward Geometric Path Search", "weight": 1.0} -->

The set of points $\mathcal{O}$ is further pruned to create a sparse set of waypoints $\mathcal{W}=\{\mathbold{w}_{1},\mathbold{w}_{2},...,\mathbold{w}_{N}\}$ where $N\leq H$ and $\mathbold{w}_{i}\in\mathbb{R}^{3}$. Sparsification is done by finding the minimal set of points in $\mathcal{O}$ that can be connected with collision-free line segments.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B Stage 2: Backward Velocity Search", "weight": 1.0} -->

The ordered waypoint set $\mathcal{W}$ found in Stage 1 only provides a collision-free geometric path through the environment. In other words, the velocity, acceleration, and higher-order states necessary for tracking control are not specified. We propose creating a velocity graph (see Fig. 2 middle) where each node in the graph is defined by a position and velocity. The positions are restricted to waypoint locations and $M$ velocities are sampled at each waypoint. More explicitly, for each waypoint $\mathbold{w}_{i}\in\mathcal{W}$, we sample a set of velocities $\mathcal{V}=\{\mathbold{v}_{1},...,\mathbold{v}_{M}\}$, where $\mathcal{V}$ is composed of candidate velocity magnitudes $\mathcal{V}_{m}$ and directions $\mathcal{V}_{d}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B Stage 2: Backward Velocity Search", "weight": 1.0} -->

With the ordered waypoint $\mathcal{W}$ and sampled velocity $\mathcal{V}$ sets, we create a velocity graph $\mathcal{G}=(\mathcal{N},\mathcal{E})$, where node $n\in\mathcal{N}$ is a given position and sampled velocity, i.e., $n=(\mathbold{w}_{i},\,\mathbold{v}_{j})$ with $\mathbold{w}_{i}\in\mathcal{W}$ and $\mathbold{v}_{j}\in\mathcal{V}$, and edge $e\in\mathcal{E}$ is the *double integrator control-constrained minimum-time* motion primitive $\mathbold{r}(t)$ from Equation 2 that connects neighboring nodes. At this stage, collision and state constraints are not enforced to prevent candidate trajectories from being eliminated prematurely.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B Stage 2: Backward Velocity Search", "weight": 1.0} -->

We recursively compute and store the ranked list of cost-to-go's $V_{d}:\mathcal{N}\times\mathcal{E}\rightarrow\mathbb{R}_{+}$ for each node $n\in\mathcal{N}$ and all connecting edges $e\in\mathcal{E}_{n}$ of $n$ where with the optimal cost-to-go $V_{d}^{*}(n)=\min_{e\in\mathcal{E}_{n}}V_{d}(n,e)$, the cost of taking edge $e$ from node $n$ being $\ell(n,e)$, and the node reached by taking edge $e$ being $\phi(n,e)$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Stage 2: Backward Velocity Search", "weight": 1.0} -->

The cost of taking an edge is given by $\ell(n,e)=T^{*}_{d}(n,e)$, where $T^{*}_{d}(n,e)$ is the minimum time of trajectory $\mathbold{r}(t)$ connecting the states of node $n$ to the states of $\phi(n,e)$. Minimizing Equation 4 is the well-known Bellman equation, which is guaranteed to return the optimal cost-to-go. In Section V-B we prove that $V_{d}^{*}(n)$ for each node in graph $\mathcal{G}$ is an admissible heuristic for an A\* search over a broad class of motion primitives.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-C Stage 3: Forward Motion Primitive Search", "weight": 1.0} -->

The cost-to-go's computed in Stage 2 for the sampled velocities at each waypoint serve as an admissible heuristic (see Definition 1. ‣ V-B Admissible Heuristic for Motion Primitive Search ‣ V THEORETICAL ANALYSIS ‣ STITCHER: Real-Time Trajectory Planning with Motion Primitive Search")) that guides an efficient A\* search over motion primitives.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-C Stage 3: Forward Motion Primitive Search", "weight": 1.0} -->

The motion primitives can be generated using any chain of integrators model of order at least two so long as i) the initial and final position and velocities match those used to construct the velocity graph $\mathcal{G}$ and ii) the allowable acceleration is maximally bounded by $u_{max}$ given in Equation 2. The motion primitive search graph is denoted as $\mathcal{G}_{mp}=(\mathcal{N}_{mp},\,\mathcal{E}_{mp})$ where $\mathcal{N}_{mp}$ is the set of nodes, each corresponding to a state vector, and $\mathcal{E}_{mp}$ is the set of edges, each corresponding to a motion primitive that connects neighboring nodes.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-C Stage 3: Forward Motion Primitive Search", "weight": 1.0} -->

A\* search is used to meet real-time constraints where the search minimizes the cost $f(n)=g(n)+h(n)$ where $n\in\mathcal{N}_{mp}$ is the current node, $g:\mathcal{N}_{mp}\rightarrow\mathbb{R}_{+}$ is the cost from the start node $n_{s}$ to node $n$, and $h:\mathcal{N}_{mp}\rightarrow\mathbb{R}_{+}$ is the estimated cost from the current node $n$ to the goal node $n_{g}$. In the context of optimal control, $g$ is the cost accrued, i.e., the running cost, for a path from $n_{s}$ to $n$ whereas $h$ is the estimated cost-to-go, i.e., the estimated value function $V^{*}$, from $n$ to $n_{g}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-C Stage 3: Forward Motion Primitive Search", "weight": 1.0} -->

In this stage, collision and state constraints are checked for each candidate motion primitive to ensure safety; the methodology for both is discussed in Section IV-D.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-D Pruning Infeasible & In-Collision Motion Primitives", "weight": 1.0} -->

STITCHER guarantees safety by pruning motion primitives from the final search that violate constraints or are in collision. For state and actuator constraints, many optimization-based planning approaches approximate the true physical constraints of the system with simple convex constraints, e.g., $\|\mathbold{{v}}\|_{\infty}\leq v_{max},~\|\mathbold{{a}}\|_{\infty}\leq a_{max},$ etc., to reduce computational complexity. When polynomials are used to represent the optimal trajectory, imposing a convex hull constraint on the polynomial is one method to enforce such constraints. However, many of these approximations are made only to simplify the resulting optimization problem and might not accurately reflect the actual physical constraint, which can lead to conservatism. STITCHER has the freedom to use different methods to enforce state and actuator constraints, but we uniformly sample candidate trajectories in time to check for constraint violations as it was found to be effective and efficient. Sampling avoids mistakenly eliminating safe trajectories, and the observed computation time was comparable to or better than using convex hulls.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-D Pruning Infeasible & In-Collision Motion Primitives", "weight": 1.0} -->

Critically, sampling allows for the inclusion of more complex constraints, such as those that couple multiple axes. Examples are | | Thrust Magnitude: | $\displaystyle~~0\leq f_{min}\leq\|\boldsymbol{f}\|_{2}\leq f_{max}$ | | \(5\) | | | Thrust Tilt Angle: | $\displaystyle~~\|\boldsymbol{f}\|_{2}\cos(\theta_{max})\leq f_{z}$ | | | | | Linear Velocity: | $\displaystyle~~\|\boldsymbol{v}\|_{2}\leq v_{max}$ | | | | | Angular Velocity: | $\displaystyle~~\|\boldsymbol{\omega}\|_{2}\leq\omega_{max},$ | | | where we note differential flatness can be leveraged to express the angular velocity constraint in terms of derivatives of position.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-D Pruning Infeasible & In-Collision Motion Primitives", "weight": 1.0} -->

Figure 3 depicts the achievable mass-normalized thrust of a VTOL vehicle given thrust and tilt constraints. The constraints are nonconvex making it difficult to include in real-time optimization-based planners without some form of relaxation, e.g., as in for a double integrator, which is tight, or a more conservative relaxation.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-D Pruning Infeasible & In-Collision Motion Primitives", "weight": 1.0} -->

An efficient collision checking strategy was devised by constructing a safe set of spheres resulting from a sampling-based collision checking approach proposed. The core idea from is that a trajectory can be intelligently sampled for collisions by estimating the next possible "time-of-collision" along the trajectory by combining obstacle proximity and the vehicle's maximum speed. Leveraging this idea, further computation time savings can be achieved by storing and reusing nearest neighbor queries. Figure 4a depicts that for the first candidate motion primitive connecting two successive waypoints, we use the strategy from while also storing the resulting set of safe, obstacle-free spheres $\mathcal{S}$. For subsequent motion primitives between the same waypoint pair (see Fig. 4b), a nearest neighbor query is only done if the primitive is expected to leave the set $\mathcal{S}$. For a point found to be within a certain sphere, the next possible "time-of-collision" is when the trajectory intersects the edge of the sphere, which can be estimated by assuming the trajectory emanates radially from the center of the sphere at maximum velocity. The process is repeated until the final time horizon $T$ is reached.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-D Pruning Infeasible & In-Collision Motion Primitives", "weight": 1.0} -->

Unlike spherical safety corridors, our safe set is only used to avoid repeated calculation, and allows for on-the-fly addition of collision-free spheres. STITCHER thus has the flexibility to create and check candidate trajectories without being restricted to pre-defined safety spheres.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-E Motion Primitive Search Graph with Triple Integrator", "weight": 1.0} -->

In many applications, a triple integrator model for generating motion primitives is sufficient because discontinuities in jerk typically do not severely degrade tracking for most aerial vehicles. Motion primitives in our formulation are derived imposing a free terminal acceleration in Equation 3. If the acceleration at each node, i.e., the final acceleration, ${\mathbold{a}}_{f}$, is free and graph nodes are represented by a waypoint-velocity-acceleration tuple, the number of edges grows exponentially with respect to the number of waypoints. Our formulation employs a greedy pre-processing step in which the motion primitive search graph $\mathcal{G}_{mp}$ is identical in size to the velocity graph $\mathcal{G}$ (graph size detailed in Section V-A). This formulation offers an advantage in terms of computational efficiency, as a full-state trajectory is generated while the graph size is restricted by only the number of sampled velocities. Excluding acceleration information when creating the graph assumes that the optimal stitched trajectory is only weakly dependent on acceleration at each waypoint.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-E Motion Primitive Search Graph with Triple Integrator", "weight": 1.0} -->

Figure 5 shows the greedy graph pre-processing step (right) maintains more edges than a traditional greedy algorithm (left).

<!-- chunk {"id": "body-0036", "role": "body", "section": "THEORETICAL ANALYSIS", "weight": 1.0} -->

In this section we prove STITCHER has bounded time and memory complexity by showing the velocity and motion primitive graphs are finite. We also show STITCHER is complete and optimal by proving the heuristic used in the motion primitive search is admissible.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-A Velocity Graph Complexity", "weight": 1.0} -->

The following proposition proves the size of the velocity graph $\mathcal{G}$ is finite and solely depends on the number of waypoints and sampled velocities; a property that also holds for the motion primitive graph $\mathcal{G}_{mp}$ by extension. This result is critical as a finite graph yields *known time complexity* for the motion primitive search. In other words, an upper bound can be placed on the computation time of the planner given known quantities. This is in contrast to optimization-based methods where the time complexity depends on the number of iterations required to converge---which cannot be known a priori---so the time to compute a trajectory via optimization does not have an a priori bound.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-B Admissible Heuristic for Motion Primitive Search", "weight": 1.0} -->

Heuristics are critical for speeding up graph search by incentivizing the search to prioritize exploring promising nodes. For example, in A\* search, the next node explored is selected based on minimizing the cost $f(n)=g(n)+h(n)$, where $g$ is the stage cost to get from the start node $n_{s}$ to node $n$, and $h$ is a heuristic estimate of the remaining cost to reach the goal node $n_{g}$. A\* search is guaranteed to find an optimal solution so long as the heuristic function $h$ is admissible (see Definition 1. ‣ V-B Admissible Heuristic for Motion Primitive Search ‣ V THEORETICAL ANALYSIS ‣ STITCHER: Real-Time Trajectory Planning with Motion Primitive Search")). Below, we prove the cost-to-go $V^{*}$ for each node in the velocity graph $\mathcal{G}$ calculated in Stage 2 is an admissible heuristic for an A\* search over motion primitives of any higher-order chain of integrators.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Proposition 2 also holds when inequality state or actuator constraints in Equation 8 are present, and when the terminal desired states are specified rather than free.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The main result of this section can now be stated.

<!-- chunk {"id": "body-0041", "role": "body", "section": "SIMULATION RESULTS", "weight": 1.0} -->

Simulation experiments were completed in a Perlin Noise and the Willow Garage environment, both with a volume of approximately $50\times 50\times 5$ m (see Fig. 6). Geometric paths with $N=4,\,6,\,8$ waypoints were found for different start and end locations in each environment. For all experiments, we imposed $f_{min}=0.85\text{ m/s}^{2}$, $f_{max}=18.75\text{ m/s}^{2}$, $\theta_{max}=60^{\circ}$, $\omega_{max}=6\text{ rad/s}$, $v_{max}=10\text{ m/s}$, and a time penalty $\rho=1000$. STITCHER requires a discrete velocity set $\mathcal{V}$ which is composed of a set of magnitudes and directions.

<!-- chunk {"id": "body-0042", "role": "body", "section": "SIMULATION RESULTS", "weight": 1.0} -->

At each waypoint $\mathbold{w}_{i}$, the velocity direction set $\mathcal{V}_{d}$ is defined by the center and boundaries of a $20^{\circ}$ cone. We define the center of the cone as the vector that points from the previous waypoint $\mathbold{w}_{i-1}$ to the next waypoint $\mathbold{w}_{i+1}$. For magnitudes, we use the set $\mathcal{V}_{m}=\left\{0,~0.25\,v_{max},~0.5\,v_{max},~0.75\,v_{max},~v_{max}\right\}$ for our analysis unless otherwise indicated. All reported times are from tests run on an 11^th^ generation Intel i7 laptop.

<!-- chunk {"id": "body-0043", "role": "body", "section": "VI-A Heuristic Benchmarking", "weight": 1.0} -->

The quality of the heuristic used to guide STITCHER can be quantified by comparing the number of edges (number of motion primitives), generated by STITCHER to an offline version of STITCHER that runs Dijkstra's algorithm rather than A\*. The number of edges created is a better evaluation metric than nodes explored because motion primitive generation and evaluation is the main source of computation time. Table I shows the number of edges created for STITCHER and Dijkstra's algorithm using execution time as the edge cost. The velocity magnitude and direction sets were kept constant across both planners with $|\mathcal{V}_{m}|=11$ containing speeds in the interval $[0,\,v_{max}]$ and $|\mathcal{V}_{d}|=3$. STITCHER generates an average of 20% fewer edges in the Perlin Noise environment and 13% fewer in the Willow Garage environment. The reduced effectiveness of the heuristic in the latter test case is attributed to narrower corridors, resulting in a greater number of motion primitives being in collision (see Fig. 7).

<!-- chunk {"id": "body-0044", "role": "body", "section": "VI-A Heuristic Benchmarking", "weight": 1.0} -->

The reduction in explored nodes shows that the heuristic is effective, but its performance depends on the environment. Note that Dijkstra's algorithm does not generate the maximum possible number of edges because nodes become disconnected if motion primitives are found to be in collision or exceed state constraints.

<!-- chunk {"id": "body-0045", "role": "body", "section": "VI-C Comparison with State-of-the-Art", "weight": 1.0} -->

We compared STITCHER to two state-of-the-art algorithms: GCOPTER and FASTER. GCOPTER performs an online optimization by incorporating state constraints into the cost functional and running a quasi-newton method, while FASTER solves a mixed integer quadratic program online. Both algorithms rely on a sparse geometric path for safe corridor formation, but do not enforce final trajectories to pass through waypoints. We evaluate each planner by time (planning time versus execution time) and failure (constraint violation or incomplete/no path found). For the Perlin Noise environment, the path lengths were 12.5 m, 30 m, and 55 m, and the path lengths for Willow Garage were 20 m, 25 m, and 30 m with $N=$ 4, 6, 8 waypoints for both environments.

<!-- chunk {"id": "body-0046", "role": "body", "section": "VI-C1 Time Analysis", "weight": 1.0} -->

Table II compares the planning times and the trajectory execution times of each planner. STITCHER's planning times are faster than those measured for GCOPTER and FASTER in each test, with an average of 6x and 200x speed up, respectively. In some cases GCOPTER and FASTER achieved lower execution times, but this was found to be a result of waypoints being treated as soft constraints, i.e., the trajectory is only required to pass nearby a waypoint rather than through it, as well as the chosen resolution of state samples in STITCHER.

<!-- chunk {"id": "body-0047", "role": "body", "section": "VI-C2 Failure Analysis", "weight": 1.0} -->

A Monte Carlo simulation composed of 50 test cases was performed to evaluate the different modes of failure experienced by each planner. Table III compares the rate at which each planner does not find a path, generates a trajectory violating constraints or generates a trajectory in collision. The "No Path Found" metric includes a numerical solver not returning a solution, or if the solution does not reach the goal. Across all test cases, STITCHER's motion primitive graph disconnects only once, achieving the lowest rate of failure among the tested planners. In the Willow Garage environment, where narrow corridors make collisions more likely, the number of failed solutions by FASTER and collisions by GCOPTER significantly increases. In contrast, STITCHER never violates constraints (state, control, or obstacles) because all constraints are strictly enforced. As an example, Fig. 9 is a representative mass-normalized thrust profile generated by STITCHER, which remains within the valid limits.

<!-- chunk {"id": "body-0048", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

In this work, we presented STITCHER, a motion primitive search planning algorithm that utilizes a novel three-stage planning architecture to design trajectories in real-time over long distances. We proved the search graph is finite, and the proposed search heuristic is admissible, so STITCHER is guaranteed to i) have a priori bounded time and memory complexity and ii) generate optimal trajectories with respect to the sampled set of states. Real-time search speeds were achieved through our novel heuristic crafting technique, greedy graph pre-processing method, and non-conservative constraint and collision checking procedure. Our simulation study showed the effectiveness of the proposed heuristic, the average computation of the components that make up STITCHER, and the satisfaction of complex actuator constraints. Critically, STITCHER was shown to consistently generate trajectories faster than two state-of-the-art optimization-based planners, with improvements of up to two orders of magnitude for computation time. Future work includes developing a receding horizon planning framework, using learning for motion primitive generation and heuristic construction, and hardware/field experiments.

<!-- chunk {"id": "body-0049", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

Acknowledgments The authors would like to thank Grace Kwak and Ryu Adams for implementation support.
