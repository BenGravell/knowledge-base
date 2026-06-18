<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Motion Planning around Obstacles with Convex Optimization

Topics include Motion planning, Trajectory optimization, Convex optimization, Mixed-integer programming, Collision avoidance, Bezier curves, Graphs of convex sets.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Applies the GCS framework to collision-free trajectory optimization by decomposing the free configuration space into convex regions and formulating motion planning as a shortest-path problem in a GCS. Trajectories are parameterized as Bézier curves, enabling compact mixed-integer optimization with constraints on shape, duration, and velocity. A convex relaxation with randomized rounding provides near-global solutions with certified optimality bounds, outperforming both sampling-based and prior trajectory optimization methods.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Trajectory optimization offers mature tools for motion planning in high-dimensional spaces under dynamic constraints. However, when facing complex configuration spaces, cluttered with obstacles, roboticists typically fall back to sampling-based planners that struggle in very high dimensions and with continuous differential constraints. Indeed, obstacles are the source of many textbook examples of problematic nonconvexities in the trajectory-optimization problem. Here we show that convex optimization can, in fact, be used to reliably plan trajectories around obstacles. Specifically, we consider planning problems with collision-avoidance constraints, as well as cost penalties and hard constraints on the shape, the duration, and the velocity of the trajectory. Combining the properties of Bézier curves with a recently-proposed framework for finding shortest paths in Graphs of Convex Sets (GCS), we formulate the planning problem as a compact mixed-integer optimization. In stark contrast with existing mixed-integer planners, the convex relaxation of our programs is very tight, and a cheap rounding of its solution is typically sufficient to design globally-optimal trajectories. This reduces the mixed-integer program back to a simple convex optimization, and automatically provides optimality bounds for the planned trajectories.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We name the proposed planner GCS, after its underlying optimization framework. We demonstrate GCS in simulation on a variety of robotic platforms, including a quadrotor flying through buildings and a dual-arm manipulator (with fourteen degrees of freedom) moving in a confined space. Using numerical experiments on a seven-degree-of-freedom manipulator, we show that GCS can outperform widely-used sampling-based planners by finding higher-quality trajectories in less time.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we consider the problem of designing continuous collision-free trajectories for robots moving in environments with obstacles. A wide array of techniques can be found in the literature to tackle this long-standing problem in robotics, and selecting the right one requires compromising between multiple features of the problem at hand: dimensionality and complexity of the environment, dynamic constraints, computation limits, completeness and optimality requirements.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Methods based on direct trajectory optimization can design trajectories in high-dimensional spaces while taking into account the robot kinematics and dynamics. However, by transcribing the planning problem as a nonconvex program, and by relying on local optimization, these techniques can fail in finding a collision-free trajectory, especially if the robot configuration space is cluttered. In these scenarios, roboticists typically fall back to sampling-based planners (see also the more recent review ). These algorithms are *probabilistically complete*, meaning that, if a feasible path exists, they will eventually find one, regardless of the complexity of the configuration space \[21, Chapter 5\]. This guarantee, however, comes at a cost. Although many sampling-based planners support "kinodynamic" constraints, continuous differential constraints are difficult to impose on discrete samples, making the kinodynamic versions of the classical sampling-based algorithms much less successful in practice. In addition, even using asymptotically-optimal sampling-based planners, the trajectories we design can be considerably suboptimal in practice, where only a finite number of samples can be taken.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

For certain classes of dynamical systems, hybrid approaches, where a trajectory-optimization planner is driven by a higher-level graph search, have been shown to overcome part of these difficulties. Still, these multi-layer architectures do not offer a unified formulation of the planning problem as a single optimization problem.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The promise of the planners based on Mixed-Integer Convex Programming (MICP) is to take the best of the two worlds above: the completeness of sampling-based algorithms, and the ease with which trajectory optimization handles the robot kinematics and dynamics; with the added bonus of global optimality and within a single optimization framework. The spread of MICP techniques, however, is strongly limited by their runtimes: even for small-scale problems, these methods can require several minutes to design a trajectory. Only recently, collision-free planners entirely based on convex optimization have been proposed, but their application is currently limited to purely-geometric path planning in low-dimensional spaces.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we focus on a limited but important class of motion-planning problems with differential constraints, and we present a planner that, although being based on MICP, reliably solves very high-dimensional problems in a few seconds, through a single convex program.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contribution", "weight": 1.0} -->

We consider a formulation of the collision-free planning problem similar to the one. In particular, we assume the robot configuration space to be partitioned into a collection of "safe" convex regions, i.e., regions that do not intersect with any of the obstacles. In the special case of polygonal obstacles, this partition can be constructed exactly. More generally, approximate decompositions can be efficiently obtained using existing algorithms, as well as newly-developed techniques tailored to the complex configuration spaces of multi-link kinematic trees. Our goal is then to design a continuous trajectory that is entirely contained in the union of the safe regions. The optimality criterion and the additional constraints are allowed to depend on the shape, the duration, and the velocity of the trajectory.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contribution", "weight": 1.0} -->

The main technical contribution of this work is showing that the trajectory-design problem just described can be formulated as a shortest-path problem in Graphs of Convex Sets (GCS): a recently-studied class of optimizations that lends itself to very efficient mixed-integer programming. Existing MICP planners parameterize a single trajectory and use binary variables to assign each of its segments to a safe region. Conversely, with the proposed planner, which we name GCS, the safe regions are connected through an adjacency graph and are each assigned a trajectory segment. The optimal probabilities of transitioning between the regions are then computed via an efficient blending of convex and graph optimization. We show that the MICPs constructed in this way have very tight convex relaxations and, in the great majority of practical cases, a single convex program, together with a cheap rounding step, is sufficient to identify a globally-optimal collision-free trajectory. Furthermore, by comparing the costs of the convex relaxation and the rounded trajectory, GCS automatically provides a tight bound on the optimality of the motion plan.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contribution", "weight": 1.0} -->

To parameterize trajectories we use Bézier curves: a relatively common tool in motion planning (see e.g. ) whose properties are very well suited for mixed-integer programming. This parameterization enables simple convex formulations of the collision-avoidance constraints and, when incorporated in our workflow, leads to very tractable convex optimizations; typically Second-Order-Cone Programs (SOCPs). This is in contrast with existing MICP planners, which require expensive semidefinite constraints to design trajectories that are differentiable more than three times. (Note that the requirement of smooth trajectories is of practical nature: to exploit the differential-flatness properties of quadrotors, for example, it is necessary to design trajectories that are differentiable at least four times.)

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contribution", "weight": 1.0} -->

We demonstrate GCS on a variety of planning problems, ranging from an intricate maze to a quadrotor flying through buildings and a fourteen-dimensional dual-arm manipulation task. The numerical results show that, besides significantly improving on state-of-the-art MICP planners, our relatively unoptimized implementation of GCS can also outperform widely-used sampling-based planners by finding higher-quality trajectories in lower, and consistent, runtimes.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

In this section we state the motion-planning problem addressed in this paper in abstract terms, as an optimization over the infinite-dimensional space of trajectories. It will be the goal of Section 5 to present our finite-dimensional transcription of this optimization, which will then be tackled using practical convex programming.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

As, we look at the problem of planning around obstacles as the problem of navigating within a collection of "safe" regions. More precisely, we assume the set $\mathcal{Q} \subset {\mathbb{R}}^{n}$ of collision-free robot configurations to be decomposed into a family of (possibly overlapping) bounded convex sets $\mathcal{Q}_{i} \subseteq \mathcal{Q}$, with $i$ in a finite index set $\mathcal{I}$. For polyhedral obstacles this decomposition can be exact, i.e. ${\bigcup_{i \in \mathcal{I}}\mathcal{Q}_{i}} = \mathcal{Q}$, while more complex configuration spaces can be decomposed approximately using efficient existing algorithms.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Given the regions $\mathcal{Q}_{i}$, our goal is to find a time $T \in {\mathbb{R}}_{> 0}$ and a trajectory $q:{{\lbrack 0,T\rbrack}\rightarrow\mathcal{Q}}$ that are a solution of the following optimization problem:^11^1 In Section 6 we show how penalties on the second and higher derivatives of $q$ can be approximately integrated in our problem formulation. Further costs and constraints are discussed in Section 8.1.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

The objective is a weighted sum, with user-specified weights ${a,b,c} \in {\mathbb{R}}_{\geq 0}$, of the trajectory duration $T$, the length $L{(q,T)}$ of the trajectory, and the energy $E{(\overset{˙}{q},T)}$ of the time derivative of the trajectory. Specifically, the latter two quantities are defined as

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Constraint (1b) asks the trajectory to be continuously differentiable $\eta$ times. Constraint (1c) ensures that $q$ is contained in the safe sets, and hence is collision free at all times. (Note that this is a stronger constraint than is usual in sampling-based motion planning, where trajectories are typically checked to be collision-free only at a finite number of points.) The set $\mathcal{D}$ in (1d) is required to be convex and can be used to enforce hard limits on the robot velocity. The bounds on the trajectory duration in (1e) are such that $T_{\max} \geq T_{\min} > 0$. Finally, the constraints (1f) and (1g) enforce the boundary conditions on $q$ and its time derivative.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

The coupling between the trajectory $q$ and its duration $T$ makes it hard to work with problem directly. Similarly to, we break this coupling by introducing the path coordinate $s \in {\lbrack 0,S\rbrack}$, where $S$ has fixed positive value. We relate the coordinate $s$ to the time variable $t$ via the scaling function $t = {h{(s)}}$: the map $h$ is required to be monotonically increasing, and such that ${h{}} = 0$ and ${h{(S)}} = T$. Expressing the trajectory $q$ as a function of $s$, we get the curve ${r{(s)}}:={q{({h{(s)}})}}$. Through a few simple manipulations, we restate problem in terms of the decision variables $r$ and $h$ as

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

In particular, we have used the chain rule to substitute $\overset{˙}{q}{(t)}$ with ${{\overset{˙}{r}{(s)}}/\overset{˙}{h}}{(s)}$, and we have changed integration variable in from $t$ to $s$. This makes ${\overset{˙}{r}/\sqrt{\overset{˙}{h}}}:{{\lbrack 0,S\rbrack}\rightarrow{\mathbb{R}}^{n}}$ the argument of the energy function in the objective. The symbol $\circ$ in (3b) denotes the composition operator: notice that the function $h$ is guaranteed to be invertible by the positivity of $\overset{˙}{h}$ from (3d). Finally, again by the chain rule, the right-hand sides of the velocity constraints in (3d) and (3g) are multiplied by the derivative $\overset{˙}{h}$ of the time scaling.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The Optimization Framework", "weight": 1.0} -->

Our strategy for solving problem is to first transcribe it as a Shortest-Path Problem (SPP) in GCS, and then use the techniques recently presented in to formulate this SPP as a compact MICP. As we will see in Section 7, the convex relaxation of this MICP is extremely tight in practice, up to the point that a cheap rounding of its solution is almost always sufficient to design a globally-optimal trajectory. In this section, we give a formal statement of the SPP in GCS and we propose a simple randomized rounding for the convex relaxation of our MICP. The latter will effectively reduce the computational cost of the MICP to that of a convex program.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Shortest Paths in Graphs of Convex Sets", "weight": 1.0} -->

The Shortest-Path Problem (SPP) in GCS generalizes the classical SPP with nonnegative edge lengths. We are given a directed graph $G:={(\mathcal{V},\mathcal{E})}$ with vertex set $\mathcal{V}$ and edge set $\mathcal{E} \subset \mathcal{V}^{2}$. Each vertex $v \in \mathcal{V}$ is paired with a bounded convex set $\mathcal{X}_{v}$, and a point $x_{v}$ contained in it. In contrast to the classical SPP, where edge lengths are fixed scalars, here the length of an edge $e = {(u,v)}$ is determined by the continuous values of $x_{u}$ and $x_{v}$ via the expression $\ell_{e}{(x_{u},x_{v})}$. The function $\ell_{e}$ is assumed to be convex and to take nonnegative values.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Shortest Paths in Graphs of Convex Sets", "weight": 1.0} -->

Convex constraints of the form ${(x_{u},x_{v})} \in \mathcal{X}_{e}$ are allowed to couple the endpoints of edge $e:={(u,v)}$. A path $p$ in the graph $G$ is defined as a sequence of distinct vertices that connects the source vertex $\sigma \in \mathcal{V}$ to the target vertex $\tau \in \mathcal{V}$. Denoting with $\mathcal{E}_{p}$ the set of edges traversed by the path $p$, and with $\mathcal{P}$ the family of all $\sigma$-$\tau$ paths in the graph $G$, the SPP in graphs of convex sets is stated as

<!-- chunk {"id": "body-0024", "role": "body", "section": "Shortest Paths in Graphs of Convex Sets", "weight": 1.0} -->

Here the decision variables are the discrete path $p$ and the continuous values $x_{v}$. The objective (5a) minimizes the length of the path $p$, defined as the sum of the lengths of its edges. Constraint (5b) asks $p$ to be a valid path connecting $\sigma$ to $\tau$. Importantly, the convex conditions (5c) and (5d) constrain only the continuous variables paired with the vertices visited by the path $p$, and do not apply to the remaining vertices in the graph. Unlike the classical SPP with nonnegative edge lengths, which is easily solvable in polynomial time, the SPP in GCS can be verified to be NP-hard \[26, Theorem 1\].

<!-- chunk {"id": "body-0025", "role": "body", "section": "Rounding the Convex Relaxation of the Shortest-Path Problem", "weight": 1.0} -->

Using recently-developed techniques, problem is formulated as a compact MICP with very tight convex relaxation \[26, Equation 21\]. In this paper, instead of tackling this MICP with an exact branch-and-bound algorithm, we solve its convex relaxation and we recover an approximate solution via a cheap randomized rounding, that is tailored to the graph structure beneath problem. Given the hardness of, this approach cannot be guaranteed to work for all instances. Nevertheless, for our planning problems, this strategy turns out to be extremely effective in practice. In addition, this workflow automatically provides us with a bound on the optimality of the approximate solution we identify. In fact, denoting with $C_{relax}$ the cost of the convex relaxation, with $C_{opt}$ the optimal value of, and with $C_{round}$ the cost of the rounded solution, we have $C_{relax} \leq C_{opt} \leq C_{round}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Rounding the Convex Relaxation of the Shortest-Path Problem", "weight": 1.0} -->

For the rounding step we propose a randomized strategy. The MICP from parameterizes a path $p$ by using a binary variable $\varphi_{e}$ per edge $e \in \mathcal{E}$, with $\varphi_{e} = 1$ if and only if $e \in \mathcal{E}_{p}$. In the convex relaxation, the binary requirement is relaxed to $\varphi_{e} \in {\lbrack 0,1\rbrack}$ and the optimal value of $\varphi_{e}$ is naturally interpreted as the probability of the edge $e$ being a part of the shortest path. To round these probabilities we then run a randomized depth-first search with backtracking. We initialize our candidate path as $p:={(\sigma)}$, and we denote with $\mathcal{E}_{u}$ the set of edges $e:={(u,v)}$ that connect $u$ to a vertex $v$ that the rounding algorithm has not visited yet.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Rounding the Convex Relaxation of the Shortest-Path Problem", "weight": 1.0} -->

At each iteration, calling $u$ the last vertex in the path $p$, we traverse the edge $e:={(u,v)} \in \mathcal{E}_{u}$ with probability $\varphi_{e}/{\sum_{e^{\prime} \in \mathcal{E}_{u}}\varphi_{e^{\prime}}}$, and we append a new vertex $v$ to the path $p$. If a dead end occurs, i.e. if $\varphi_{e} = 0$ for all $e \in \mathcal{E}_{u}$, we backtrack to the last vertex in $p$ that admits a way out. The algorithm terminates when $v = \tau$ and the target is reached.^33^3 Making this rounding strategy deterministic, e.g., selecting at each iteration the edge $e \in \mathcal{E}_{u}$ with larger probability $\varphi_{e}$ is, in general, a bad idea.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Rounding the Convex Relaxation of the Shortest-Path Problem", "weight": 1.0} -->

To see this, imagine a graph where multiple paths represent the same underlying decision (e.g. multiple symmetrical solutions). Since the convex relaxation will equally split the probability of this decision being optimal between the edges of these many paths, a greedy deterministic search might end up selecting an alternative path, corresponding to a decision that is overall less likely to be optimal. Conversely, in the same scenario, a randomized rounding correctly weights the two decisions (in expectation).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Rounding the Convex Relaxation of the Shortest-Path Problem", "weight": 1.0} -->

It is easily verified that this rounding strategy always finds a valid path (provided that the convex relaxation of the MICP is feasible). On the other hand, the cost of the path $p$ we find can in principle be infinite, since there might not be an assignment for the continuous variables ${\{ x_{v}\}}_{v \in p}$ that satisfies the constraints (5c) and (5d).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Rounding the Convex Relaxation of the Shortest-Path Problem", "weight": 1.0} -->

To increase our chances of finding a high-quality approximate solution, we apply the randomized rounding multiple times. First we run the depth-first search until $N$ distinct paths are identified, or a maximum number $M$ of trials is reached. Then we evaluate the cost of each distinct path by solving a convex program of the form, and we return the rounded solution of lowest cost $C_{round}$.^44^4 This sequence of convex optimizations is stopped early if the cost of a path coincides with the cost of the convex relaxation $C_{relax}$, since this proves the global optimality of the path at hand. We emphasize that this process is extremely cheap: the runtime of a depth-first search is practically zero (since it is a purely-discrete search in the graph $G$), while the convex programs are tiny, very sparse, and parallelizable. In this paper we set $N:=10$ and $M:=100$. These values lead to rounding times that are negligible with respect to the solution time of the convex relaxation and, in our experiments, they are typically sufficient to solve the planning problem to global optimality.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Rounding the Convex Relaxation of the Shortest-Path Problem", "weight": 1.0} -->

Many more details on the MICP formulation of and its convex relaxation can be found. For the scope of this paper, we will treat the framework from as a modeling language that allows us to formulate, and efficiently solve, an SPP in GCS just by providing the graph $G$, the edge lengths $\ell_{e}$, and the sets $\mathcal{X}_{v}$ and $\mathcal{X}_{e}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Collision-Free Motion Planning using Graphs of Convex Sets", "weight": 1.0} -->

We now illustrate how problem can be transcribed as an SPP in GCS. As seen in the previous section, to formulate an SPP in GCS we need to: define a graph $G:={(\mathcal{V},\mathcal{E})}$, assign a set $\mathcal{X}_{v}$ to each vertex $v \in \mathcal{V}$, and pair each edge $e \in \mathcal{E}$ with a constraint set $\mathcal{X}_{e}$ and a length function $\ell_{e}$. Below we describe how each of these components is constructed. At a high level, the plan is to pair each safe region $\mathcal{Q}_{i}$ with two Bézier curves: a trajectory segment $r_{i}$, and a time-scaling function $h_{i}$ that dictates the speed at which the curve $r_{i}$ is traveled.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Collision-Free Motion Planning using Graphs of Convex Sets", "weight": 1.0} -->

The functions $r$ and $h$ in problem will be then reconstructed by sequencing the Bézier curves $r_{i}$ and $h_{i}$ paired with the regions $\mathcal{Q}_{i}$ that are selected by the SPP. Figure 1 provides a visual support to the upcoming discussion.

<!-- chunk {"id": "body-0034", "role": "body", "section": "The Graph $G$", "weight": 1.0} -->

We let the vertex set $\mathcal{V}$ contain a vertex $i$ per safe set $\mathcal{Q}_{i}$ in the decomposition of the configuration space.^55^5As we will see in Section 5.2, the safe set $\mathcal{Q}_{i}$ does not coincide with the convex set $\mathcal{X}_{i}$ paired with vertex $i$ in the SPP. In addition, we introduce a source vertex $\sigma$ and a target vertex $\tau$: these will be used to enforce the boundary conditions (3e)--(3g). Overall, we then have $\mathcal{V}:={\mathcal{I} \cup {\{\sigma,\tau\}}}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "The Graph $G$", "weight": 1.0} -->

We include in the edge set $\mathcal{E}$ all the edges $(i,j)$ such that the intersection of $\mathcal{Q}_{i}$ and $\mathcal{Q}_{j}$ is nonempty. Note that, by the symmetry of this condition, ${(i,j)} \in \mathcal{E}$ implies ${(j,i)} \in \mathcal{E}$. Similarly, we let ${(\sigma,i)} \in \mathcal{E}$ and ${(i,\tau)} \in \mathcal{E}$ if the set $\mathcal{Q}_{i}$ contains the points $q_{0}$ and $q_{T}$, respectively. In symbols,

<!-- chunk {"id": "body-0036", "role": "body", "section": "The Convex Sets $\\mathcal{X}_{v}$", "weight": 1.0} -->

The source $\sigma$ and the target $\tau$ are auxiliary vertices used to enforce the boundary conditions (3e)--(3g); they require no decision variables and can be safely paired with the empty set $\mathcal{X}_{\sigma}:=\mathcal{X}_{\tau}:=\varnothing$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "The Convex Sets $\\mathcal{X}_{v}$", "weight": 1.0} -->

To each of the vertices $i \in \mathcal{I}$, we assign two Bézier curves: $r_{i}:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{Q}_{i}}$ (depicted in Figure 1(c)) and $h_{i}:{{\lbrack 0,1\rbrack}\rightarrow{\lbrack 0,T_{\max}\rbrack}}$. Both these curves have a user-defined degree $d \geq {\eta + 1}$, where $\eta$ is the required degree of differentiability of the overall trajectory $q$.^66^6 The assumption that the curves $r$ and $h$ have the same degree is without loss of generality.

<!-- chunk {"id": "body-0038", "role": "body", "section": "The Convex Sets $\\mathcal{X}_{v}$", "weight": 1.0} -->

The *degree elevation* property of Bézier curves allows us to describe a Bézier curve $\gamma$ of degree $d$ as a Bézier curve $\gamma^{\prime}$ of arbitrary degree $d^{\prime} \geq d$, with control points that are linear functions of the control points of $\gamma$. Any convex cost or constraint on the control points of $r$ and $h$, that takes advantage of the equal degree of these curves, can then be mapped to an equivalent convex cost or constraint on the control points of curves $r$ and $h$ of different degree. The convex set $\mathcal{X}_{i}$ contains the control points of the two curves, i.e.

<!-- chunk {"id": "body-0039", "role": "body", "section": "The Convex Sets $\\mathcal{X}_{v}$", "weight": 1.0} -->

The convex constraint (7a) requires all the control points of $r_{i}$ to lie in the collision-free set $\mathcal{Q}_{i}$. By the convex-hull property of the Bézier curves from Section 3, this implies that the whole trajectory segment $r_{i}$ is contained in $\mathcal{Q}_{i}$. Again by the properties of Bézier curves, the derivative ${\overset{˙}{h}}_{i}$ of the time scaling $h_{i}$ is itself a Bézier curve. Condition (7b) lower bounds each control point of this derivative with a small positive constant ${\overset{˙}{h}}_{\min}$ which, unless differently specified, is set to $10^{- 6}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "The Convex Sets $\\mathcal{X}_{v}$", "weight": 1.0} -->

By the convex-hull property, this implies that ${\overset{˙}{h}}_{i}{(s)}$ is positive for all $s \in {\lbrack 0,1\rbrack}$, and hence that $h_{i}$ is strictly increasing. Since the control points of ${\overset{˙}{h}}_{i}$ are linear functions of the ones of $h_{i}$, constraint (7b) is linear in $x_{i}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "The Convex Sets $\\mathcal{X}_{v}$", "weight": 1.0} -->

$({\overset{˙}{r}}_{i,k},{\overset{˙}{h}}_{i,k})$. Finally, the constraints in (7d) are conservative bounds that ensure the boundedness of $\mathcal{X}_{i}$, as assumed in Section 4.1.

<!-- chunk {"id": "body-0042", "role": "body", "section": "The Convex Sets $\\mathcal{X}_{v}$", "weight": 1.0} -->

We remark that asking the control points of a Bézier curve to be in a convex set is only a sufficient condition for the containment of the whole curve. Nonetheless, the conservativeness of the conditions in can be attenuated by increasing the degree of the curves $r_{i}$ and $h_{i}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "The Convex Sets $\\mathcal{X}_{e}$", "weight": 1.0} -->

The second role of the edge constraints is to enforce the differentiability of the overall curves $r$ and $h$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "The Edge Lengths $\\ell_{e}$", "weight": 1.0} -->

The edge lengths $\ell_{e}$ must reproduce the cost in (3a) by appropriately weighting the cost of each transition in the graph $G$. This is achieved by assigning to each edge $(\sigma,i)$ outgoing the source a length of zero, and to each edge $(i,j)$ or $(i,\tau)$ the length

<!-- chunk {"id": "body-0045", "role": "body", "section": "The Edge Lengths $\\ell_{e}$", "weight": 1.0} -->

While the first term in this sum is immediately restated as the linear cost $a{({h_{i,d} - h_{i,0}})}$, the other two terms require more work to be expressed as convex functions of $x_{i}$ that are amenable to efficient numerical optimization.

<!-- chunk {"id": "body-0046", "role": "body", "section": "The Edge Lengths $\\ell_{e}$", "weight": 1.0} -->

One option is to approximate to arbitrary precision the last two terms in using numerical integration. Since both $L$ and $E$ can be verified to be convex in the functions $r_{i}$ and $h_{i}$, the resulting expression would be convex in $x_{i}$, but its numerical implementation would require a large number of second-order-cone constraints, proportional to the density of the integration grid.

<!-- chunk {"id": "body-0047", "role": "body", "section": "The Edge Lengths $\\ell_{e}$", "weight": 1.0} -->

The first inequality overestimates the length of $r_{i}$ by summing the distances between its control points. The validity of this bound can be verified by applying inequality to the Bézier curve ${\overset{˙}{r}}_{i}$ and the convex function ${\|{\overset{˙}{r}}_{i}\|}_{2}$. The second inequality does a similar operation with the energy $E$, and can be checked by applying to the Bézier curve $({\overset{˙}{r}}_{i},{\overset{˙}{h}}_{i})$ and the function ${\|{\overset{˙}{r}}_{i}\|}_{2}^{2}/{\overset{˙}{h}}_{i}$, which is convex for ${\overset{˙}{h}}_{i} > 0$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Reconstruction of a Collision-Free Trajectory", "weight": 1.0} -->

Once the SPP is solved, the optimal path $p$ determines the sequence of safe regions $\mathcal{Q}_{i}$ that the robot must traverse. To reconstruct the trajectory $r$ and the time scaling $h$, we sequence the Bézier curves $r_{i}$ and $h_{i}$ associated with these regions, as shown in Figure 1(d) for $\eta:=0$. Precisely, if the optimal path is $p:={(\sigma,i_{0},\ldots,i_{S - 1},\tau)}$, for $\nu = {0,\ldots,{S - 1}}$, we define

<!-- chunk {"id": "body-0049", "role": "body", "section": "Reconstruction of a Collision-Free Trajectory", "weight": 1.0} -->

Let us verify that the functions $r$ and $h$ just defined form an optimal solution of problem, up to the conservativeness of the constraints and the cost bounds. The constraints in imply ${r,h} \in \mathcal{C}^{\eta}$. This, in turn, gives $h^{- 1} \in \mathcal{C}^{\eta}$ and (3b). That the collision-avoidance constraint (3c) is met, is implied by (7a). The velocity constraint in (3d) is verified thanks to (7c), while (7b) ensures that the function $h$ is monotonically increasing, as required by the second condition in (3d). The boundary conditions (3e)--(3g) are verified because of the constraints on the edges $(\sigma,i)$ and $(i,\tau)$ described in Section 5.3. Finally, summing the edge lengths for all the edges traversed by the path $p$ we get back (3a).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Class of Optimization Problems", "weight": 1.0} -->

Let us conclude this section by highlighting that, by feeding the SPP in GCS we just constructed to the machinery, we obtain very tractable optimization problems. The framework in relies on *perspective functions* \[13, Section IV.2.2\] to handle the interplay between the discrete and continuous components of problem. These are used to effectively "turn off" the edge costs $\ell_{e}$ and the convex constraints ${(x_{u},x_{v})} \in \mathcal{X}_{e}$ and $x_{v} \in \mathcal{X}_{v}$ corresponding to the edges $e$ and the vertices $v$ that do not lie along the path $p$, as required in problem.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Class of Optimization Problems", "weight": 1.0} -->

In case of polytopic safe sets $\mathcal{Q}_{i}$ and a purely-minimum-time objective ($a:=1$ and $b:=c:=0$), it can be verified that the perspective operations lead to a mixed-integer Linear Program (LP), which, as discussed in Section 4.2, we tackle as a simple LP followed by a rounding stage. More generally, when the safe sets $\mathcal{Q}_{i}$ are quadratics or the cost weights $b$ and $c$ are nonzero, we obtain a mixed-integer SOCP, which we solve as a single SOCP plus rounding. In both cases, we then have simple convex optimizations for which very efficient solvers are available (e.g. MOSEK and Gurobi). Conversely, in order to design trajectories that are differentiable more than three times, existing MICP planners formulate prohibitive mixed-integer semidefinite programs that cannot be tackled with common solvers.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Penalties on the Higher-Order Derivatives of the Trajectory", "weight": 1.0} -->

In many practical applications, we find the need to expand our problem formulation to include convex penalties on the second and higher time derivatives of the trajectory $q$. These can be used, for example, to indirectly limit the control efforts: for a robot manipulator, in fact, the joint torques needed to execute a trajectory $q$ are proportional to the acceleration $\overset{¨}{q}$ via the inertia matrix; while for a quadrotor the differential-flatness property makes the thrusts a function of the snap $q^{}$. Unfortunately, even though convex in $q$, these costs become nonconvex when in problem we optimize jointly over the shape $r$ and the time scaling $h$ of our trajectories. While we are currently working on the design of tight convex approximations of these costs, in this section we show how simple regularization terms can be added to our SPP in GCS to prevent the higher-order derivatives of $q$ from growing excessively in magnitude.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Penalties on the Higher-Order Derivatives of the Trajectory", "weight": 1.0} -->

where ${\overset{˙}{q}{(t)}} = {{{\overset{˙}{r}{(s)}}/\overset{˙}{h}}{(s)}}$ and $s = {h^{- 1}{(t)}}$. Using this expression, we see that a convex function of $\overset{¨}{q}$ does not, in general, translate into a convex function of $r$ and $h$, and hence it cannot be directly minimized in our programs. However, provided that we choose a bounded set $\mathcal{D}$ to constrain the velocity $\overset{˙}{q}$, the magnitude of $\overset{¨}{q}$ can be kept under control by increasing the minimum value ${\overset{˙}{h}}_{\min}$ of $\overset{˙}{h}{(s)}$ and by penalizing the magnitudes of $\overset{¨}{r}$ and $\overset{¨}{h}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Penalties on the Higher-Order Derivatives of the Trajectory", "weight": 1.0} -->

Letting $\varepsilon$ be a small positive scalar, a simple way to achieve the latter is the cost term

<!-- chunk {"id": "body-0055", "role": "body", "section": "Penalties on the Higher-Order Derivatives of the Trajectory", "weight": 1.0} -->

which can be enforced using the ideas from Section 5.4.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Penalties on the Higher-Order Derivatives of the Trajectory", "weight": 1.0} -->

The regularization of the higher-order derivatives of $q$ follows the same logic. Specifically, using Faà di Bruno's formula for differentiating composite functions, we see that the magnitude of $q^{(m)}$ can be regularized by increasing ${\overset{˙}{h}}_{\min}$ and by penalizing the magnitudes of $r^{(l)}$ and $h^{(l)}$, for $l = {2,\ldots,m}$. The numerical results in the next section show that, even though these regularization terms are not as tight as the velocity bounds, they can sensibly smooth the trajectories we design, while only minimally affecting their cost.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

We demonstrate the effectiveness of GCS on a variety of numerical examples. In Section 7.1 we analyze a simple two-dimensional problem, and we illustrate how the different components of problem affect the shape of the trajectories we design. In Section 7.2 we increase the environment complexity and we apply our algorithm to design paths across an intricate maze. In Section 7.3, we run a statistical analysis of the performance of GCS on the task of planning the flight of a quadrotor through randomly-generated buildings. In Section 7.4, we show that, with respect to widely-used sampling-based algorithms, our algorithm is capable of designing higher-quality trajectories in less runtime. Finally, in Section 7.5, we demonstrate the scalability of GCS with a bimanual manipulation problem in a fourteen-dimensional configuration space.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

The code necessary to reproduce all the results presented in this section can be found at It uses an implementation of the SPP in GCS provided by Drake. In addition to the techniques presented, the convex optimizations we solve in this paper feature additional tightening constraints, tailored to the structure of the graphs in our planning problems, and a pre-processing step that eliminates the redundancies in our graphs. These are described in detail in Appendix A. The optimization solver used for the numerical experiments is MOSEK 9.2. All experiments are run on a desktop computer with an Intel Core i7-6950X processor and 64 GB of memory.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Two-Dimensional Example", "weight": 1.0} -->

The goal of our first numerical example is to illustrate how the different parameters in problem affect the shape of the trajectories we design. To this end, we consider the simple two-dimensional environment depicted in Figure 2(a). The initial $q_{0}:={(0.2,0.2)}$ and final $q_{T}:={(4.8,4.8)}$ configurations are marked with a black cross; the obstacles are the red polygons. The convex decomposition ${\{\mathcal{Q}_{i}\}}_{i \in \mathcal{I}}$ of the free space $\mathcal{Q}$ is depicted in light blue in Figure 2(b).

<!-- chunk {"id": "body-0060", "role": "body", "section": "Two-Dimensional Example", "weight": 1.0} -->

The first planning problem we analyze asks to minimize the total Euclidean length of the trajectory. The weights in the objective (1a) are then $a:=c:=0$ and $b:=1$. The trajectory $q$ is only required to be continuous ($\eta:=0$), while velocity and time constraints are irrelevant for a minimum-length problem. We let the degree of the Bézier curves $r$ and $h$ be $d:=1$ (i.e. straight lines). Solving the convex relaxation of the SPP in GCS we obtain the cost $C_{relax} = 10.77$, while the rounding step from Section 4.2 gives us the feasible trajectory depicted in Figure 3(a) with cost $C_{round} = 10.96$. By comparing these two numbers, GCS automatically provides the optimality bound $\delta_{relax}:={{({C_{round} - C_{relax}})}/C_{relax}} = {1.7\%}$ for the rounded solution.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Two-Dimensional Example", "weight": 1.0} -->

However, by actually running a slightly more expensive mixed-integer solver, it is possible to verify that the rounded solution is indeed the global minimizer: $C_{round} = C_{opt}$ and $\delta_{opt}:={{({C_{round} - C_{opt}})}/C_{opt}} = {0\%}$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Two-Dimensional Example", "weight": 1.0} -->

For the second scenario, we consider a minimum-time problem with velocity limits. The weights in problem are set to $a:=1$ and $b:=c:=0$. We look for a continuous trajectory ($\eta:=0$), whose velocity $\overset{˙}{q}$ is contained in the box $\mathcal{D}:={\lbrack{- 1},1\rbrack}^{2}$ for all times $t$. The bounds on the trajectory duration are set to $T_{\min} \approx 0$ and $T_{\max} \gg 0$, so that they do not affect the optimization problem. For this problem we let the optimizer decide the initial $\overset{˙}{q}{}$ and final $\overset{˙}{q}{(T)}$ velocities by dropping the boundary conditions (1g). Once again, we use Bézier curves of degree $d:=1$. The trajectory generated by GCS is illustrated in Figure 3(b).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Two-Dimensional Example", "weight": 1.0} -->

The convex relaxation has cost $C_{relax} = 9.88$, while the rounded trajectory has duration $C_{round} = 10.60$ and, therefore, it is certified to be within $\delta_{relax} = {7.3\%}$ of the global minimum. As before, a mixed-integer solver can be used to verify that the trajectory generated by GCS is actually globally optimal ($\delta_{opt} = {0\%}$).

<!-- chunk {"id": "body-0064", "role": "body", "section": "Two-Dimensional Example", "weight": 1.0} -->

In juxtaposition to the minimum-length case, the minimum-time trajectory in Figure 3(b) passes below the central obstacle. This is because, although shorter, the trajectory in Figure 3(a) is everywhere almost horizontal or vertical, and in these directions the speed is limited by the constraint set $\mathcal{D}$ to ${\|\overset{˙}{q}\|}_{2} \leq 1$. The route below the obstacle is slightly longer, but it allows diagonal motion with speed ${\|\overset{˙}{q}\|}_{2} \leq \sqrt{2}$. In Figure 4(a) we report the velocity $\overset{˙}{q}$ corresponding to the minimum-time trajectory: as expected, the optimal velocity is discontinuous and, at all times $t$, either the horizontal or the vertical component of $\overset{˙}{q}$ reaches the upper bound of $1$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Two-Dimensional Example", "weight": 1.0} -->

Finally, we show the effects of the regularization strategy discussed in Section 6 on the smoothness of the minimum-time trajectory. We require the curve $q$ to be twice continuously differentiable ($\eta:=2$). The initial and final velocities are forced to be zero, ${\overset{˙}{q}}_{0}:={\overset{˙}{q}}_{T}:=0$, and we set the degree of the Bézier curves to $d:=6$. We increase ${\overset{˙}{h}}_{\min}$ from its default value of $10^{- 6}$ to $10^{- 1}$, and we add the penalty with weight $\varepsilon = 10^{- 1}$. The resulting trajectory is reported in Figures 3(c) and 4(b). As can be seen, the regularization smooths the optimal trajectory significantly and even changes its homotopy class.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Two-Dimensional Example", "weight": 1.0} -->

The costs of the convex relaxation and the rounded solution increase to $C_{relax} = 27.29$ and $C_{round} = 28.10$, respectively. The optimality gap certified by GCS is hence $\delta_{relax} = {3.0\%}$, but, once again, a mixed-integer solver can be used to verify that the rounded solution is actually globally optimal ($\delta_{opt} = {0\%}$). The duration of the smoothed trajectory is $T = 13.65$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Motion Planning in a Maze", "weight": 1.0} -->

In this example we consider a two-dimensional planning problem of higher complexity than the one just analyzed: we design trajectories through the maze depicted in Figure 5. The maze has ${50 \cdot 50} = {2,500}$ cells. The starting cell is the one at the bottom left, the goal cell is in the top right. The graph of convex sets is constructed by making each cell into a safe set $\mathcal{Q}_{i}$. Bidirectional edges are drawn between cells that are not separated by a wall. The maze is generated using random depth-first search. Since mazes constructed using this algorithm have all cells connected to the starting cell by a unique path, to make the planning problem more challenging, we create multiple paths to the goal by randomly selecting and removing $100$ walls from the maze.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Motion Planning in a Maze", "weight": 1.0} -->

As in the previous example, we consider a minimum-length problem and a minimum-time problem with regularized acceleration. We set the parameters $(a,b,c,\eta,\mathcal{D},T_{\min},T_{\max},{\overset{˙}{q}}_{0},{\overset{˙}{q}}_{T},d)$ to the same values we adopted in the corresponding problems in Section 7.1. The optimal trajectories across the maze corresponding to the two objective functions are reported in Figures 5(a) and 5(b). As it can be seen, the two curves visit different sequences of safe sets (cells). In particular, the sharp turn taken by the minimum-length trajectory, circled in red in Figure 5(a), would be expensive for the second problem, where we have a penalty on the magnitude of the acceleration. For the curve in Figure 5(b), GCS decides then to take a longer but smoother route to the goal.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Motion Planning in a Maze", "weight": 1.0} -->

For both the problems under analysis, the convex relaxation returns a solution with binary probabilities $\varphi_{e}$. Rounding is then unnecessary in this case, and the solution of the convex relaxation is automatically certified to be globally optimal ($\delta_{relax} = \delta_{opt} = {0\%}$).

<!-- chunk {"id": "body-0070", "role": "body", "section": "Motion Planning in a Maze", "weight": 1.0} -->

We find this example powerful because it highlights the transparency with which GCS blends discrete and continuous optimization. Finding a discrete sequence of cells to traverse the maze in Figure 5 is a trivial graph search. Also finding a path of minimum length, as in Figure 5(a), is a relatively simple problem: in fact, in two dimensions, the Euclidean SPP is solvable in polynomial time by constructing a discrete visibility graph. On the other hand, designing a trajectory like the minimum-time one in Figure 5(b) is a substantially more involved operation. GCS gives us a unified mathematical framework that can tackle all these problems very efficiently, while embracing both the higher-level combinatorial structure and the lower-level convexity of our planning problems.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Motion Planning in a Maze", "weight": 1.0} -->

In conclusion of this example let us illustrate another axis in which GCS significantly improves on existing MICP planners. The worst-case runtime of a mixed-integer solver is typically exponential in the number of binaries in the optimization problem. Previous MICP planners parameterize a single trajectory and subdivide it in a fixed number of segments, then they use a binary variable to assign each segment to each safe region $\mathcal{Q}_{i}$. Given that, in the worst case, the optimal trajectory might visit all the safe regions $\mathcal{Q}_{i}$, this approach requires a total of ${|\mathcal{I}|}^{2}$ binary variables. For the maze in Figure 5, we would then have ${{|\mathcal{I}|}^{2} = 2},{500^{2} = {6.25 \cdot 10^{6}}}$ binaries: a quantity well beyond the capability of today's solvers.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Motion Planning in a Maze", "weight": 1.0} -->

On the contrary, GCS uses only two binaries per pair of intersecting regions, and it yields an MICP with only $5198 \approx {2{|\mathcal{I}|}}$ binaries, which is solved exactly through a single SOCP.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Statistical Analysis: Quadrotor Flying through Buildings", "weight": 1.0} -->

In this section we present a statistical analysis of the performance of GCS. Taking inspiration, we test our algorithm on the task of planning the motion of a quadrotor through randomly-generated buildings. An example of such a task is illustrated in Figure 6: while moving from the brown to the green block, the quadrotor needs to fly around trees, and through doors and windows. A brief description of how the buildings are generated can be found in Appendix B.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Statistical Analysis: Quadrotor Flying through Buildings", "weight": 1.0} -->

Even though the configuration space of a quadrotor is six dimensional, the differential-flatness property of this system allows us to plan dynamically-feasible trajectories directly in the three-dimensional Cartesian space. In fact, given a four-times-differentiable trajectory of the position of the center of mass, the time evolution of the quadrotor's orientation, together with the necessary control signals, is uniquely defined and easily computed. The space in which we design trajectories is then $\mathcal{Q} \subset {\mathbb{R}}^{3}$ and, given that all the obstacles have polyhedral shape (as in Figure 6), the decomposition of this space into convex sets $\mathcal{Q}_{i}$ can be done exactly. Appendix B provides more details on this decomposition.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Statistical Analysis: Quadrotor Flying through Buildings", "weight": 1.0} -->

In the formulation of the planning problem, we penalize with equal weight the duration and the length of the trajectory ($a:=b:=1$ and $c:=0$). We parameterize the trajectories using Bézier curves of degree $d:=7$ and, to take advantage of the differential flatness, we require these curves to be continuously differentiable $\eta:=4$ times. The velocity is constrained to be in the box $\mathcal{D}:={\lbrack{- 10},10\rbrack}^{3}$ for all times.^77^7 To contextualize the velocity limits, consider that the random environments are squares with sides of length 25, and the collision geometry of the quadrotor is a sphere of radius 0.2 (see also Appendix B). The limits $T_{\min}$ and $T_{\max}$ on the duration of the trajectory have values that do not affect the optimal solution. As said, the initial $q_{0}$ and final $q_{T}$ positions are above the brown and green boxes, respectively.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Statistical Analysis: Quadrotor Flying through Buildings", "weight": 1.0} -->

The boundary values of the velocity are zero ${\overset{˙}{q}}_{0}:={\overset{˙}{q}}_{T}:=0$, as well as the boundary values of the second and the third derivatives of the trajectory.^88^8 For $l = {2,\ldots,L}$, the derivative constraints ${q^{(l)}{}} = {q^{(l)}{(T)}} = 0$ in problem map to the conditions ${r^{(l)}{}} = {h^{(l)}{}{\overset{˙}{q}}_{0}}$ and ${r^{(l)}{(S)}} = {h^{(l)}{(S)}{\overset{˙}{q}}_{T}}$ in problem. The latter are linear in the decision variables of our SPP in GCS, and can be easily incorporated among the edge constraints listed in Section 5.3.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Statistical Analysis: Quadrotor Flying through Buildings", "weight": 1.0} -->

Because of the differential flatness, the latter ensure that the quadrotor starts and ends the motion with horizontal orientation and zero angular velocity. Finally, to regularize the acceleration of the quadrotor, as discussed in Section 6, we set ${\overset{˙}{h}}_{\min}:=10^{- 3}$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Statistical Analysis: Quadrotor Flying through Buildings", "weight": 1.0} -->

We plan the motion of the quadrotor through 100 random buildings. To assess the quality of the trajectories generated by GCS, we look at the optimality gaps $\delta_{opt}$ and $\delta_{relax}$. As in the previous examples, the value of $\delta_{opt}$ is computed (just for analysis purposes) by solving the planning problem to global optimality using a mixed-integer algorithm, while $\delta_{relax}$ is the upper bound on $\delta_{opt}$ that is automatically provided to us by GCS. The histograms of these two quantities across the 100 experiments are reported in Figure 7. Figure 7(a) shows that on $95\%$ of the environments GCS designs a trajectory whose optimality gap $\delta_{opt}$ is smaller than $1\%$, and, even in the worst case, is only $2.9\%$.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Statistical Analysis: Quadrotor Flying through Buildings", "weight": 1.0} -->

From Figure 7(b), we see that on $68\%$ (respectively $84\%$) of the problems GCS certifies that the returned solution is within $4\%$ (respectively $7\%$) of the global optimum. The largest optimality gap $\delta_{relax}$ certified by GCS is $27.1\%$, and it corresponds to an environment where we have $\delta_{opt} = {2.3\%}$. Therefore, even for this problem instance, the moderately-large value of $\delta_{relax}$ is mostly due to the convex relaxation being slightly loose, rather than the rounded solution being suboptimal.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Statistical Analysis: Quadrotor Flying through Buildings", "weight": 1.0} -->

We report that, for the statistical analysis in this subsection, we set the MOSEK parameter MSK_IPAR_INTPNT_SOLVE_FORM = 1, which tells the interior-point solver to interpret our optimizations in standard primal form. Without this, MOSEK encountered numerical issues in the solution of the convex relaxations of the motion-planning problems. This parameter choice has the drawback of sensibly slowing down the planning times: the solve times for the convex relaxations of the 100 motion plans have median $3.7$ s, mean $6.4$ s, and maximum $31.2$ s. However, we are very confident that a deeper analysis of these numerical issues and a tailored pre-solve stage, can reduce these times by at least one order of magnitude.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Comparison with PRM: Motion Planning of a Robot Arm", "weight": 1.0} -->

In this subsection we consider the motion planning of a robot arm, and we compare GCS with commonly-used sampling-based planners. GCS is a multiple-query algorithm, meaning that the same data structure (the graph of convex sets) can be used to plan the motion of the robot for many initial and final conditions. Its natural sampling-based comparison is then the Probabilistic-RoadMap (PRM) algorithm. The robot arm we use in this benchmark is the KUKA LBR iiwa with $n = 7$ degrees of freedom: we have chosen a seven-dimensional configuration space $\mathcal{Q}$ since PRM methods can struggle in larger spaces, and both algorithms under analysis can easily design trajectories in lower dimensions.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Comparison with PRM: Motion Planning of a Robot Arm", "weight": 1.0} -->

The robot arm is depicted in Figure 8, and it is required to move within an environment composed of a rack (in front of the robot) and two bins (on the sides). As opposed to the examples considered so far, an exact decomposition of the free configuration space $\mathcal{Q}$ is not feasible in this application. We then adopt the approximate decomposition algorithm, IRIS more precisely, its extension to configuration spaces with nonconvex obstacles, IrisInConfigurationSpace, implemented in Drake. Given a "seed pose" of the robot, this algorithm inflates a polytope of robot configurations that are not in collision with the environment. While these polytopes could be rigorously certified to be collision free, for the experiments reported here we use a fast implementation based on nonconvex optimization that does not provide a rigorous certification, but that appears to be very reliable in practice.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Comparison with PRM: Motion Planning of a Robot Arm", "weight": 1.0} -->

Automatic seeding of the regions is certainly possible, but we have found that producing seeds manually via inverse kinematics, together with a simple visualization of the graph $G$ to check the connectivity between regions $\mathcal{Q}_{i}$, is straightforward and highly effective. We use IRIS to construct a total of eight safe polytopes $\mathcal{Q}_{i}$, whose corresponding seed poses $q_{i}$ are depicted in Figures 8. The seed poses ${\{ q_{i}\}}_{i = 1}^{5}$ in Figures 8(a) are chosen to create polytopes $\mathcal{Q}_{i}$ that cover the volume of configuration space for which the end effector is in the vicinity of the rack and the bins. The poses ${\{ q_{i}\}}_{i = 6}^{8}$ in Figures 8(b) are picked to approximately fill the rest of the free space. The construction of the safe regions is parallelized, and took us 53 seconds.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Comparison with PRM: Motion Planning of a Robot Arm", "weight": 1.0} -->

By processing the safe regions $\mathcal{Q}_{i}$ as described in Section 5.1, we obtain the graph $G$ depicted in Figure 8(c). The vertices $\mathcal{I} = {\{ 1,\ldots,8\}}$ are the subscripts of the poses that we use as seeds for the construction of each polytope, i.e., vertex $i \in \mathcal{I}$ is paired with the safe polytope $\mathcal{Q}_{i}$ obtained from the seed $q_{i}$. As can be seen from the connectivity of the graph, the polytopes $\mathcal{Q}_{i}$ are sufficiently inflated to connect all the seed poses $q_{i}$. At runtime, given the initial $q_{0}$ and final $q_{T}$ configuration, the source $\sigma$ and the target $\tau$ vertices are added to the graph and connected to other vertices as described in Section 5.1.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Comparison with PRM: Motion Planning of a Robot Arm", "weight": 1.0} -->

In practice, the plans generated by a PRM can be very suboptimal and are rarely commanded to the robot directly. While asymptotically-optimal versions of the PRM method exist, in our experience, in the relatively high-dimensional space we consider here, the increase in performance of these variants is not worth their computational cost. A solution commonly used in practice is then to post-process the plans generated by the PRM with a simple short-cutting algorithm. This algorithm samples pairs of points along the PRM trajectory and connects them via straight segments: if a segment is verified to be collision free the trajectory is successfully shortened. This step can dramatically shorten the PRM trajectories but it requires time-consuming collision checks: for this reason, here we compare GCS with both the regular PRM and the PRM with short-cutting. For both the PRM methods we use the implementation. More implementation details can be found in Appendix C; here we only mention that our roadmap is composed of $15 \cdot 10^{3}$ sample configurations and its construction took, with our (not fully optimized) setup, 16 minutes.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Comparison with PRM: Motion Planning of a Robot Arm", "weight": 1.0} -->

The tasks require moving the arm between five waypoint configurations $\rho_{i} \in \mathcal{Q}$, while avoiding collisions with the rack and the bins. Each waypoint $\rho_{i}$ is obtained from $q_{i}$ by perturbing the position of the robot end-effector as shown in Figure 9. We have a total of five tasks: for $i = {1,\ldots,4}$, task $i$ asks us to move the robot from $\rho_{i}$ to $\rho_{i + 1}$; task 5 requires moving the robot from $\rho_{5}$ back to $\rho_{1}$. The objective is to connect the start and the goal configurations with a continuous ($\eta:=0$) trajectory of minimum Euclidean length ($a:=c:=0$ and $b:=1$). Velocity and time constraints are irrelevant given our objective.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Comparison with PRM: Motion Planning of a Robot Arm", "weight": 1.0} -->

As a visual support to the analysis, Figure 9 illustrates the trajectories of the robot end-effector generated by each planner for each task. The blue curves correspond to GCS, the yellow to the regular PRM, and the red to the PRM with short-cutting. Let us emphasize, though, that shorter trajectories in configuration space do not necessarily map to shorter trajectories in task space. The actual configuration-space lengths of these trajectories are reported in Figure 10(a), with the same color scheme. The runtimes required by each planner can be found in Figure 10(b).^99^9 The runtimes of GCS are computed by summing the times necessary for the pre-processing described in Appendix A.2, the solution of the convex relaxation of the SPP in GCS, and the rounding step from Section 4.2. In all the tasks, GCS designs trajectories that are shorter than both PRM methods. Moreover, the runtimes of GCS are even smaller than the ones of the regular PRM.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Comparison with PRM: Motion Planning of a Robot Arm", "weight": 1.0} -->

The PRM with short-cutting designs higher-quality trajectories than the regular PRM, but its runtimes are significantly larger. The pre-processing described in Appendix A.2 is the reason why our method is extremely fast in solving task 2: in the graph $G$ in Figure 8(c) there is only one path that connects vertex $2$ to vertex $3$, and our pre-processing efficiently eliminates all the edges in the graph but $$ and $$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Comparison with PRM: Motion Planning of a Robot Arm", "weight": 1.0} -->

In conclusion, let us mention that in all the tasks the solution we identify via rounding is the global optimum of the SPP in GCS ($\delta_{opt} = {0\%}$). The certified optimality gap $\delta_{relax}$ is 4.1% on average, and achieves a maximum of 13.0% in the first task.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Coordinated Planning of Two Robot Arms", "weight": 1.0} -->

In the previous subsection we have compared GCS to widely-used PRM methods, choosing a robotic arm with $n = 7$ degrees of freedom because sampling-based algorithms perform poorly in higher dimensions. Here we demonstrate that GCS can tackle planning problems in much higher-dimensional spaces. To this end, we consider the dual-arm manipulator shown in Figure 11, composed of two KUKA LBR iiwa with seven degrees of freedom each, yielding an overall configuration space $\mathcal{Q}$ of $n = 14$ dimensions. The environment is the same as in the previous subsection, but this time, besides the collisions with the rack and the bins, GCS must also prevent collisions between the arms themselves.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Coordinated Planning of Two Robot Arms", "weight": 1.0} -->

To decompose the configuration space we proceed as in Section 7.4. This time we use a total of 22 seed poses, chosen to approximately cover the workspace around the rack and the bins, as well as the rest of the free space. Also in this case the seeds are produced manually, using inverse kinematics and with the visual support provided by the connectivity of the graph $G$. We analyze three tasks. In the first task, illustrated in Figure 11(a), the arms start in a neutral position and both reach into the top shelf. Task 2, in Figure 11(b), asks the arms to cross: the left arm reaches above the rack on the right, and the right arm moves to the left of the bottom shelf. Finally, in Figure 11(c), task 3 requires the two arms to reach inside the bins. To make the problem even more challenging, this time we do not limit ourselves to the design of purely-geometric shortest curves as in Section 7.4, but we plan continuously differentiable ($\eta:=1$) trajectories of degree $d:=3$.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Coordinated Planning of Two Robot Arms", "weight": 1.0} -->

The weights in the objective (1a) are set to $a:=b:=1$ and $c:=0$. The constraint set $\mathcal{D}$ in (1d) ensures that the joint velocities are no greater than 60% of the robot velocity limits. The duration bounds $T_{\min}$ and $T_{\max}$ are set so that they do not affect the optimal trajectory, while the boundary values of the velocity are zero (${\overset{˙}{q}}_{0}:={\overset{˙}{q}}_{T}:=0$). As described in Section 6, we penalize accelerations via a cost term of the form, with weight $\varepsilon = 10^{- 3}$. With the same goal, we set ${\overset{˙}{h}}_{\min}:=10^{- 3}$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Coordinated Planning of Two Robot Arms", "weight": 1.0} -->

The trajectories synthesized by GCS for each of the three tasks are represented in Figure 11, with the curves swept by the end-effectors depicted in blue. The optimality gaps $\delta_{relax}$ certified by GCS for the three tasks are $3.3\%$, $2.0\%$, and $0.6\%$. Running a mixed-integer solver, we verify that the first two trajectories are, in fact, globally optimal, while the last trajectory has an optimality gap of only $\delta_{opt} = {0.3\%}$. As in Section 7.3, to circumvent numerical issues, we set the MOSEK option MSK_IPAR_INTPNT_SOLVE_FORM = 1 in the solution of the convex relaxations. This leads to the following computation times for the three tasks at hand: $4.0$ s, $8.4$ s, and $12.9$ s. As already mentioned, we are confident that a tailored pre-solve stage can drastically decrease these runtimes.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Discussion", "weight": 1.5} -->

On the one hand, transcribing the motion-planning problem as an SPP in GCS allows us to use efficient convex optimization to design trajectories around obstacles. On the other hand, our convexity requirements restrict the class of planning problems we can tackle, and limit the families of trajectories we can parameterize. In this section we comment on the strengths and the limitations of our approach, and we illustrate the pros and the cons of GCS over existing planning algorithms.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Additional Costs and Constraints", "weight": 1.0} -->

Besides the derivative penalties discussed in Section 6, there are many additional costs and constraints that our problem statement does not feature but that are relevant in a variety of practical applications. Minimum-distance and minimum-time objectives might lead to unsafe robot trajectories, that do not avoid obstacles with sufficient clearance. A practical workaround in these cases is to discourage the control points of our trajectories to get too close to certain boundaries of the safe regions $\mathcal{Q}_{i}$. This can be achieved through convex barrier penalties, that are easily included among the edge costs in Section 5.4. Equality constraints that couple the trajectory $q$ to its time derivatives could be used to enforce continuous-time dynamics. However, our choice of optimizing over the shape $r$ and the timing $h$ of the trajectory jointly makes these constraints nonconvex, even for a linear control system. Similarly, the nonlinearity of the kinematics of a robot manipulator makes task-space constraints not directly suitable for our framework.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Additional Costs and Constraints", "weight": 1.0} -->

To cope with these nonconvexities, in some applications, it may be practical to post-process the output of GCS with a local nonconvex optimizer.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Comparison with Existing Mixed-Integer Planners", "weight": 1.0} -->

The tightness of the convex relaxation of our MICPs, demonstrated empirically in the numerical results in Section 7.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Comparison with Existing Mixed-Integer Planners", "weight": 1.0} -->

The reduced number of binary decision variables in our programs, illustrated in the maze example from Section 7.2.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Comparison with Existing Mixed-Integer Planners", "weight": 1.0} -->

The simplicity of the class of optimization problems that our method leads to, discussed in Section 5.6

<!-- chunk {"id": "body-0100", "role": "body", "section": "Comparison with Existing Mixed-Integer Planners", "weight": 1.0} -->

The first and the second are achieved by leveraging the optimization framework. The third is partly due to the first (since it is the tightness our MICP formulations that allows us to tackle the motion planning problem as a single convex program, plus rounding), but it is also due to the parameterization of trajectories as Bézier curves.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Comparison with Existing Mixed-Integer Planners", "weight": 1.0} -->

In Section 5.2, we have leveraged the properties of Bézier curves to enforce infinite families of constraints through a finite number of conditions. For example, in (7a), we have transcribed the safety requirement ${r_{i}{(s)}} \in \mathcal{Q}_{i}$ for all $s \in {\lbrack 0,1\rbrack}$ as a constraint $r_{i,k} \in \mathcal{Q}_{i}$ per control point $k = {0,\ldots,d}$. The MICP planner from achieves the same result by using Sums-Of-Squares (SOS) polynomials, and semidefinite programming.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Comparison with Existing Mixed-Integer Planners", "weight": 1.0} -->

These approaches are interchangeable and lead to a tradeoff: Bézier curves yield simpler constraints, SOS polynomials parameterize a richer class of trajectories.^1010^10 Asking a univariate polynomial to be nonnegative by parameterizing it as a Bézier curve with nonnegative control points is more stringent than asking it to be SOS (which, in the univariate case, is equivalent to nonnegativity). In the numerical examples analyzed in this paper, we have found this gap to be relatively narrow, and we have then prioritized simpler optimization problems.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Comparison with Existing Mixed-Integer Planners", "weight": 1.0} -->

Finally, it is worth mentioning that the problem formulation from features costs and constraints on time derivatives of the trajectory $q$ of any order. These, however, are handled by fixing the duration of each trajectory segment beforehand. A similar result could be achieved with GCS by fixing the time that can be spent in each safe set $\mathcal{Q}_{i}$.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Comparison with Sampling-Based Algorithms", "weight": 1.0} -->

As discussed in Section 7.4, among many sampling-based planners, PRM is the natural comparison for GCS. In fact, GCS can be thought of as a generalization of the PRM method, where each collision-free sample is expanded to a collision-free convex region, that is inflated as much as the obstacles allow; reducing in this way a dense roadmap to a compact GCS. In Sections 7.4 and 7.5, we have shown that GCS can outperform PRM in terms of: runtimes, quality of the designed trajectories, scalability with the dimensionality $n$ of the configuration space $\mathcal{Q}$, and variety of objective functions and trajectory constraints. In addition, because of the parallel above, it is reasonable to imagine that many of the techniques developed for PRM to handle, e.g., changes in the environments can be translated to GCS with relatively low effort.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Comparison with Sampling-Based Algorithms", "weight": 1.0} -->

One of the main reasons why sampling-based methods are widely used in academia and industry is their simplicity. Conversely, the implementation of GCS is very involved and requires familiarity with convex-optimization techniques. Nonetheless, we believe that the framework from lends itself to an intuitive mathematical abstraction, and that the programming interface of GCS can be made very easy to use. We have provided a mature implementation of the techniques from within the open-source software Drake, and we have developed a simple GCS interface at

<!-- chunk {"id": "body-0106", "role": "body", "section": "Comparison with Direct Trajectory Optimization", "weight": 1.0} -->

Direct-trajectory-optimization methods transcribe the motion-planning problem into a nonconvex optimization, and can virtually include any sort of cost terms and constraints, including dynamic and task-space constraints. In practice, however, these nonconvex programs can only be tackled with local-optimization algorithms that are slow and unreliable. GCS is different in spirit, as we prioritize low runtimes and the completeness of the planning algorithm over the modelling power.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Conclusions and Future Works", "weight": 1.0} -->

In this paper we have introduced GCS: an algorithm based on convex optimization for efficient collision-free motion planning. GCS leverages the framework presented in to design a very tight and lightweight convex relaxation of the planning problem. This convex optimization (typically an SOCP) is quickly solved using commonly-available software, and a cheap randomized rounding of its solution is almost always sufficient to identify a globally-optimal trajectory. We have demonstrated GCS on a variety of scenarios: an intricate maze, a quadrotor flying through buildings, and a manipulation task in a fourteen-dimensional configuration space. Furthermore, we have compared GCS to widely-used PRM methods, showing that our method can find higher-quality trajectories in less time.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Conclusions and Future Works", "weight": 1.0} -->

This paper presents the first version of a new algorithm, which already compares favorably with widely-used planners that have been optimized over decades. The runtimes of GCS can be drastically reduced (we are currently developing a customized solver for these convex optimizations). We are also highly optimistic that the class of cost functions and constraints that we can handle will expand considerably in the future. In particular, we imagine incorporating task-space constraints, tight penalties on the higher derivatives of the trajectory, as well as dynamic constraints arising from input limits. Furthermore, we wish to extend GCS to problems involving contacts between the robot and the environment. We believe that our planner demonstrates the value of formulating problems as SPPs in GCS, and it can already find multiple real-world applications.
