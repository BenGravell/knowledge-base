<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Downwash-Aware Trajectory Planning for Large Quadrotor Teams

Topics include Robotics, Aerial robotics, Safety, Graphs, Planning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We describe a method for formation-change trajectory planning for large quadrotor teams in obstacle-rich environments. Our method decomposes the planning problem into two stages: a discrete planner operating on a graph representation of the workspace, and a continuous refinement that converts the non-smooth graph plan into a set of C^k-continuous trajectories, locally optimizing an integral-squared-derivative cost. We account for the downwash effect, allowing safe flight in dense formations. We demonstrate the computational efficiency in simulation with up to 200 robots and the physical plausibility with an experiment with 32 nano-quadrotors. Our approach can compute safe and smooth trajectories for hundreds of quadrotors in dense environments with obstacles in a few minutes.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Trajectory planning is a fundamental problem in multi-robot systems. Given a set of robots with known initial locations and a set of goal locations, the task is to find a one-to-one goal assignment and a set of continuous functions that move each robot from its start position to its goal, while avoiding collisions and respecting dynamic limits. Trajectory planning is a core subproblem of various applications including search-and-rescue, inspection, and delivery. In this work we address the *unlabeled* case; in the *labeled* case the goal assignment is given.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

A large body of work has addressed this problem with varied discrete and continuous formulations. However, no existing solution simultaneously satisfies the goals of completeness, physical plausibility, optimality in time or energy usage, and good computational performance. In this work, we present a method that attempts to balance these goals.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Our method uses a graph-based planner to compute a solution for a discretized version of the problem, and then refines this solution into smooth trajectories in a separate, decoupled optimization stage. We directly take the downwash effect of quadrotors into account, preserving safety during dense formation flights. Furthermore, our method is complete with respect to the resolution of the discretization, and locally optimal with respect to an energy-minimizing integral-squared-derivative objective function. We also present an anytime iterative refinement scheme that improves the trajectories within a given computational budget. We support user-specified smoothness constraints and provide simulations with up to 200 robots and a physical experiment with 32 quadrotors, see Fig. 1.

<!-- chunk {"id": "body-0006", "role": "body", "section": "APPROACH", "weight": 1.0} -->

We start by introducing the robot model, which is required to model the downwash effect. We then formalize the problem statement and outline our approach. In later sections, we will discuss each part of our approach in detail.

<!-- chunk {"id": "body-0007", "role": "body", "section": "III-A Robot Model", "weight": 1.0} -->

As aerial vehicles, quadrotors have a six-dimensional configuration space. However, as shown, quadrotors are *differentially flat* in the *flat outputs* $(x,y,z,\psi)$, where $x,y,z$ is the robot's position in space and $\psi$ its yaw angle (heading). Differential flatness implies that the control inputs needed to move the robot along a trajectory in the flat outputs are algebraic functions of the flat outputs and a finite number of their derivatives. Furthermore, in many applications, a quadrotor's yaw angle is unimportant and can be fixed at $\psi = 0$. We therefore focus our efforts on planning trajectories in three-dimensional Euclidean space.

<!-- chunk {"id": "body-0008", "role": "body", "section": "III-A Robot Model", "weight": 1.0} -->

While some multi-robot planning work has considered simplified dynamics models such as kinematic agents or double-integrators, our method produces trajectories with arbitrary smoothness up to a user-defined derivative. This goal is motivated, where it was shown that a continuous fourth derivative of position is necessary for physically plausible quadrotor trajectories, because it ensures that the quadrotor will not be asked to change its motor speeds instantaneously.

<!-- chunk {"id": "body-0009", "role": "body", "section": "III-A Robot Model", "weight": 1.0} -->

Rotorcraft generate a large, fast-moving volume of air underneath their rotors called *downwash*. The downwash force is large enough to cause a catastrophic loss of stability when one rotorcraft flies underneath another. We model downwash constraints by treating each robot as an axis-aligned ellipsoid of radii $0 < r_{x} = r_{y} \ll r_{z}$, illustrated in Fig. 2. Empirical data collected in support this model. The set of points representing a robot at position $q \in {\mathbb{R}}^{3}$ is given by where $E = {\operatorname{\mathbf{d}\mathbf{i}\mathbf{a}\mathbf{g}}{(r_{x},r_{y},r_{z})}}$. The collision-avoidance constraint between robots located at ${p,q} \in {\mathbb{R}}^{3}$ is given by Figure 2: Axis-aligned ellipsoid model of robot volume. Tall height prevents downwash interference between quadrotors.

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-B Problem Statement", "weight": 1.0} -->

Consider a team of $N$ robots in a bounded environment containing convex obstacles $\mathcal{O}_{1}\ldots\mathcal{O}_{N_{obs}}$. Boundaries of the environment are defined by a convex polytope $\mathcal{W}$. The free configuration space for a single robot is thus given by where $\circleddash$ denotes the Minkowski difference.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-B Problem Statement", "weight": 1.0} -->

We are given a start position for each robot $s^{i} \in \mathcal{F}$ and a set of goal positions ${G \subset \mathcal{F}},{{|G|} = N}$. The start and goal inputs must satisfy the collision constraint for all robot pairs.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-B Problem Statement", "weight": 1.0} -->

We seek the following: An assignment of each robot to a goal position $g^{\phi{(i)}} \in G$, where $\phi$ is a permutation of $1\ldotsN$ The total time duration $T \in {\mathbb{R}}_{> 0}$ until the last robot reaches its goal For each robot $r^{i}$, a trajectory $f^{i}:{{\lbrack 0,T\rbrack}\mapsto\mathcal{F}}$ where ${{f^{i}{}} = s^{i}},{{f^{i}{(T)}} = g^{\phi{(i)}}}$, and $f^{i}$ must be continuous up to a user-specified parameter $C$: Additionally, we require that the collision-avoidance constraint is satisfied at all times for all pairs of robots.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-B Problem Statement", "weight": 1.0} -->

In the following, we present an efficient solution to the subclass of problems where all $s^{i}$ and $g^{i}$ are positions in an orthogonal grid and obstacles are cubes within that grid.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-C Overview", "weight": 1.0} -->

Our approach decomposes the formation change problem into two steps: *Discrete Planning* and *Continuous Refinement*. Discrete planning solves the goal assignment problem (generating $\phi$) and computes a timed sequence of waypoints for each robot in a graph approximation of the environment. Continuous refinement uses the discrete plan as a starting point to compute a set of smooth trajectories satisfying user-supplied smoothness constraints.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-C Overview", "weight": 1.0} -->

We note that a major benefit of our method is its ability to use different discrete planners. For example, it would be possible to use a discrete planner for planning problems where the goal assignment is fixed a-priori, or where robots are split into smaller groups.

<!-- chunk {"id": "body-0016", "role": "body", "section": "DISCRETE PLANNING STAGE", "weight": 1.0} -->

The discrete planning stage works with a grid discretization of the environment. We assume that the robots' start and goal locations are vertices of the underlying graph.

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-A Overview", "weight": 1.0} -->

The discrete planning stage computes the goal assignment $\phi$ and a path $p^{i}$ for each robot composed of a sequence of $K + 1$ (time, position) pairs: where $0 = t_{0} < t_{1} < \cdots < t_{K} = T$, $x_{k}^{i} \in \mathcal{F}$, $x_{0}^{i} = s^{i}$, and $x_{K}^{i} = g^{\phi{(i)}}$. In between waypoints $(t_{k},x_{k}^{i})$ and $(t_{k + 1},x_{k + 1}^{i})$, we assume that robot $i$ travels on the line segment between $x_{k}^{i}$ and $x_{k + 1}^{i}$, but we do not make any assumptions about the velocity profile of the robot along that path.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-A Overview", "weight": 1.0} -->

We denote this line segment by $\ell_{k}^{i}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Overview", "weight": 1.0} -->

We require that the discrete planner supplies a plan that satisfies the ellipsoid collision-avoidance constraint for all possible identical velocity profiles. We also require all robots to share the same sequence of waypoint times $t_{0}\ldotst_{K}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A Overview", "weight": 1.0} -->

In the following, we discuss one specific discrete planner that simultaneously computes the goal assignment $\phi$ and produces waypoint sequences $p^{i}$ that minimize $K$. This planner operates in a grid environment and assumes fixed timesteps, i.e. $t_{k + 1} - t_{k}$ is equal for all $k$. Furthermore, we require the grid size to be greater than $2r_{x}$. A robot can either move to an adjacent grid cell or stay at its current location each step. At all timesteps, and during movements, the planner must ensure that the collision constraints are fulfilled. With fixed timesteps, the number of waypoints $K$ corresponds to the time duration of the trajectory. $K$ is known as the *makespan*. Our planner minimizes $K$ to produce short trajectories.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B Unlabeled Planner", "weight": 1.0} -->

We model unlabeled planning as a variant of the *unlabeled Multi-Agent Path-Finding* (MAPF) problem. We are given an undirected connected graph of the environment $\mathcal{G}_{E} = {(\mathcal{V}_{E},\mathcal{E}_{E})}$, where each vertex $v \in \mathcal{V}_{E}$ corresponds to a location in $\mathcal{F}$ and each edge ${(u,v)} \in \mathcal{E}_{E}$ denotes that there is a linear path in $\mathcal{F}$ connecting $u$ and $v$. Obstacles are implicitly modeled by not including a vertex in $\mathcal{V}_{E}$ for each cell that contains an obstacle.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B Unlabeled Planner", "weight": 1.0} -->

We assume that there exists a vertex $v_{s}^{i} \in \mathcal{V}_{E}$ corresponding to each start location $s^{i}$ and that there exists a vertex $v_{g}^{i} \in \mathcal{V}_{E}$ for each goal location $g^{i}$. At each discrete timestep, a robot can either wait at its current vertex or traverse an edge. For the following formulation, we assume that the locations corresponding to the vertices are in a grid world and that $z{(\cdot)}$ and $xy{(\cdot)}$ map a vector to its $z$ and $x,y$ components, respectively. Our goal is to find paths $p^{i}$, such that the following properties hold: Each robot starts at its start vertex: ${\forall i}:{x_{0}^{i} = s^{i}}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B Unlabeled Planner", "weight": 1.0} -->

No robots occupy the same location at the same time (*vertex collision*): ${{\forall k},{\forall i}} \neq j$: $x_{k}^{i} \neq x_{k}^{j}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Unlabeled Planner", "weight": 1.0} -->

We consider a solution optimal if the makespan $K$ is minimal. If only the first five properties are considered and $K$ is given, unlabeled MAPF can be solved in polynomial time by reduction to a maximum-flow problem in a larger graph, derived from $\mathcal{G}$, known as a *time-expanded flow-graph*. This graph, denoted by $\mathcal{G}_{F}$, contains $O{({K \cdot {|\mathcal{V}_{E}|}})}$ vertices and is constructed such that a flow in $\mathcal{G}_{F}$ represents a solution to the MAPF instance. This maximum-flow problem can also be expressed as an Integer Linear Program (ILP) where each edge is modeled as binary variable indicating its flow and the objective is to maximize the flow subject to flow conservation constraints. An ILP formulation allows us to add additional constraints for P6 and P7.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B Unlabeled Planner", "weight": 1.0} -->

We build the time-expanded flow-graph $\mathcal{G}_{F} = {(\mathcal{V}_{F},\mathcal{E}_{F})}$ as intermediate step to formulate the ILP. Compared to the existing detailed discussions, we add additional annotations ${con}:{\mathcal{E}_{F}\mapsto 2^{\mathcal{E}_{F}}}$ to some of the edges such that $con{(e)}$ is the set of edges with which $e$ is in conflict under the downwash model. For each timestep $k$ and vertex $v \in \mathcal{V}_{E}$ we add two vertices $u_{k}^{v}$ and $w_{k}^{v}$ to $\mathcal{V}_{F}$ and create an edge connecting them.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B Unlabeled Planner", "weight": 1.0} -->

For each timestep $k$ and edge ${(v_{1},v_{2})} \in \mathcal{E}_{E}$, we create a "gadget" connecting $u_{k}^{v_{1}},u_{k}^{v_{2}},w_{k}^{v_{1}}$, and $w_{k}^{v_{2}}$. As shown in Fig 3(b), the "gadget" disallows agents to swap their positions in one timestep, thus enforcing P5. Furthermore, we connect consecutive timesteps with additional edges $(w_{k}^{v},u_{k + 1}^{v})$ (green edges in Fig. 3(c)) to enforce P4.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-B Unlabeled Planner", "weight": 1.0} -->

Additionally we add vertices $source$ and $sink$, which are connected to vertices $\{ u_{0}^{v_{s}^{i}}:{\forall i}\}$ and $\{ w_{K}^{v_{g}^{i}}:{\forall i}\}$ respectively. If a maximum flow is computed on this graph, the flow describes a path for each robot, fulfilling P1--P5.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-B Unlabeled Planner", "weight": 1.0} -->

For each edge ${(u,v)} \in \mathcal{E}_{F}$, we introduce a binary variable $z_{(u,v)}$. The ILP can be formulated as follows: where $\mathcal{V}_{F}' = {\mathcal{V}_{F} \smallsetminus {\{{source},{sink}\}}}$. The first constraint enforces flow conservation, and thus P3--P5. The second constraint enforces P6--P7. P1 and P2 are implicitly enforced by construction of the flow graph. A solution to the ILP assigns a flow to each edge. We can then easily create the path $p^{i}$ for each robot by setting $t_{k} = {k\Deltat}$ for any ${\Deltat} > 0$, and $x_{k}^{i}$ based on the flow in $\mathcal{G}_{F}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Unlabeled Planner", "weight": 1.0} -->

In order to find an optimal solution for an unknown $K$, we use a two-step approach. First, we find a lower bound for $K$ by ignoring P6 and P7. We search the sequence $K = {1,2,4,8,\ldots}$ for a feasible $K$, and then perform a binary search to find the minimal feasible $K$, which we denote as $LB{(K)}$. Because we ignore the downwash constraints, we can check the feasibility in polynomial time using the Edmonds-Karp algorithm on the time-expanded flow-graph. Second, we execute a linear search starting from $LB{(K)}$, solving the fully constrained ILP. In practice, we have found that the lower bound $LB{(K)}$ is sufficiently close to the final $K$ such that a linear search is faster compared to another modified binary search using the ILP.

<!-- chunk {"id": "body-0030", "role": "body", "section": "CONTINUOUS REFINEMENT STAGE", "weight": 1.0} -->

In the continuous refinement stage, we convert the waypoint sequences $p^{i}$ generated by the discrete planner into smooth trajectories $f^{i}$. We use the discrete plan to partition the free space $\mathcal{F}$ such that each robot solves an independent smooth trajectory optimization problem in a region that is guaranteed to be collision-free.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-A Spatial Partition", "weight": 1.0} -->

The continuous refinement method begins by finding *safe corridors* within the free space $\mathcal{F}$ for each robot. The safe corridor for robot $r^{i}$ is a sequence of convex polyhedra ${\mathcal{P}_{k}^{i},k} \in {\{{1\ldotsK}\}}$, such that, if each $r^{i}$ travels within $\mathcal{P}_{k}^{i}$ during time interval $\lbrack t_{k - 1},t_{k}\rbrack$, both robot-robot and robot-obstacle collision avoidance are guaranteed.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-A Spatial Partition", "weight": 1.0} -->

We separate $r^{i}$ from $r^{j}$ by finding a separating hyperplane $(\alpha_{k}^{(i,j)},\beta_{k}^{(i,j)})$ such that: While this hyperplane separates $\ell_{k}^{i}$ and $\ell_{j}^{k}$, it does not account for the robot ellipsoids. Without loss of generality, suppose the hyperplanes are given in the normalized form where ${\|\alpha_{k}^{(i,j)}\|}_{2} = 1$. Then we accomodate the ellipsoids by shifting each hyperplane according to its normal vector: where $E = {\operatorname{\mathbf{d}\mathbf{i}\mathbf{a}\mathbf{g}}{(r_{x},r_{y},r_{z})}}$ is the ellipsoid matrix.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-A Spatial Partition", "weight": 1.0} -->

Robot-obstacle separating hyperplanes are computed similarly, except we use a different ellipsoid $E_{obs}$ for obstacles to model the fact that downwash is only important for robot-robot interactions, and we shift the hyperplanes such that they touch the obstacles.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-A Spatial Partition", "weight": 1.0} -->

In our implementation, we require that the obstacles $\mathcal{O}_{i}$ are bounded convex polytopes described by vertex lists. Line segments are also convex polytopes described by vertex lists. Computing a separating hyperplane between two disjoint convex polytopes $\Psi = {\operatorname{\mathbf{c}\mathbf{o}\mathbf{n}\mathbf{v}}{({\psi_{1}\ldots\psi_{m_{\Psi}}})}}$ and $\Omega = {\operatorname{\mathbf{c}\mathbf{o}\mathbf{n}\mathbf{v}}{({\omega_{1}\ldots\omega_{m_{\Omega}}})}}$, where $\operatorname{\mathbf{c}\mathbf{o}\mathbf{n}\mathbf{v}}$ denotes the convex hull, can be posed as an instance of the hard-margin support vector machine (SVM) problem.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-A Spatial Partition", "weight": 1.0} -->

However, the ellipsoid robot shape alters the problem: for a separating hyperplane with unit normal vector $\alpha$, the minimal safe margin is $2{\|{E\alpha}\|}_{2}$. Incorporating this constraint in the standard hard-margin SVM formulation yields a slightly modified version of the typical SVM quadratic program: We solve a problem of this form for each robot-robot and robot-obstacle half-space to yield the safe polyhedron $\mathcal{P}_{k}^{i}$ in the form of a set of linear inequalities. Note that the safe polyhedra need not be bounded and that ${\mathcal{P}_{k}^{i} \cap \mathcal{P}_{k + 1}^{i}} \neq \varnothing$ in general. In fact, the overlap between consecutive $\mathcal{P}_{k}^{i}$ allows the smooth trajectories to deviate significantly from the discrete plans, which is an advantage when the discrete plan is far from optimal.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-B Bézier Trajectory basis", "weight": 1.0} -->

After computing safe corridors, we plan a smooth trajectory $f^{i}{(t)}$ for each robot, contained within the robot's safe corridor. We represent these trajectories as piecewise polynomials with one piece per time interval $\lbrack t_{k},t_{k + 1}\rbrack$. Piecewise polynomials are widely used for trajectory planning: with an appropriate choice of degree and number of pieces, they can represent arbitrarily complex trajectories with an arbitrary number of continuous derivatives.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-B Bézier Trajectory basis", "weight": 1.0} -->

We denote the $k^{\text{th}}$ piece of robot $i$'s piecewise polynomial trajectory as $f_{k}^{i}$. We wish to constrain $f_{k}^{i}$ to lie within the safe polyhedron $\mathcal{P}_{k}^{i}$. However, when working in the standard monomial basis, i.e. when the decision variables are the $a_{i}$ in the expression bounding the polynomial inside a convex polyhedron is not a convex constraint. Instead, we formulate trajectories as Bézier curves.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-B Bézier Trajectory basis", "weight": 1.0} -->

A degree-$D$ Bézier curve is defined by a sequence of $D + 1$ *control points* $y_{i} \in {\mathbb{R}}^{3}$ and a fixed set of Bernstein polynomials, such that where each $b_{i,D}$ is a degree-$D$ Bernstein polynomial with coefficients^11^1 The canonical Bernstein polynomials are defined over the time interval $\lbrack 0,1\rbrack$, but they are easily modified to span our desired time interval. given. The curve begins at $y_{0}$ and ends at $y_{D}$. In between, it does not pass *through* the intervening control points, but rather is guaranteed to lie in the convex hull of all control points. Thus, when using Bézier control points as decision variables instead of monomial coefficients, constraining the control points to lie inside a safe polyhedron guarantees that the resulting polynomial will lie inside the polyhedron also.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-B Bézier Trajectory basis", "weight": 1.0} -->

We define $f^{i}$ as a $K$-piece, degree-$D$ Bézier curve and denote the $d^{\text{th}}$ control point of $f_{k}^{i}$ as $y_{k,d}^{i}$. The degree parameter $D$ must be sufficiently high to ensure continuity at the user-defined continuity level $C$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-C Optimization Problem", "weight": 1.0} -->

The set of Bézier curves that lie within a given safe corridor describes a family of feasible solutions to a single robot's planning problem. We select an optimal trajectory by minimizing a weighted combination of the integrated squared derivatives: where the $\gamma_{c} \geq 0$ are user-chosen weights on the derivatives. A typical choice in our experiments is to penalize acceleration and snap equally. As an input to the trajectory optimization stage, we require the user to supply an initial guess of the duration $\Deltat$ of each timestep, such that $T = {K\Deltat}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-C Optimization Problem", "weight": 1.0} -->

Our decision variable $\mathbf{y}$ consists of all control points for $f^{i}$ concatenated together: The objective function is a quadratic function of $\mathbf{y}$, which can be expressed in the form: where $B$ is a block-diagonal matrix transforming control points into polynomial coefficients, and the formula for $Q$ is given. The start and goal position constraints, as well as the continuity constraints between successive polynomial pieces, can be expressed as linear equalities. Thus, we solve the quadratic program: It is important to note that this quadratic program may not always have a solution due to our conservative assumptions regarding velocity profiles. In these cases, we fall back on a solution that follows the discrete plan exactly, coming to a complete stop at corners. Details of this solution are given.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-C Optimization Problem", "weight": 1.0} -->

The corridor-constrained Bézier formulation presents one notable shortcoming: for a given safe polyhedron $\mathcal{P}_{k}^{i}$, there exist degree-$D$ polynomials that lie inside the polyhedron but cannot be expressed as a Bézier curve with control points that are contained within $\mathcal{P}_{k}^{i}$. Empirical exploration of Bézier curves suggests that this problem is most significant when the desired trajectory is near the faces of the polyhedron rather than the center. Further research is needed to characterize this issue more precisely.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-D Iterative Refinement", "weight": 1.0} -->

Solving for each robot converts the discrete plan into a set of smooth trajectories that are locally optimal given the spatial decomposition. However, these trajectories are not globally optimal. In our experiments, we found that the smooth trajectories sometimes lie quite far away from the original discrete plan. Motivated by this observation, we implement an iterative refinement stage where we use the smooth trajectories to define a new spatial decomposition, and use the same optimization method to solve for a new set of smooth trajectories.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-D Iterative Refinement", "weight": 1.0} -->

For time interval $k$, we sample $f_{k}^{i}$ at $S$ evenly-spaced points in time to generate a set of points $\mathcal{S}_{k}^{i}$. The number of sample points $S$ is a user-specified parameter, set to $S = 32$ in our experiments. We then compute the separating hyperplanes as before, except we separate $\mathcal{S}_{k}^{i}$ from $\mathcal{S}_{k}^{j}$ instead of $\ell_{k}^{i}$ from $\ell_{k}^{j}$. This problem is also a (slightly larger) ellipsoid-weighted support vector machine instance.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-D Iterative Refinement", "weight": 1.0} -->

These new safe corridors are roughly "centered" on the smooth trajectories, rather than on the discrete plan. Intuitively, iterative refinement provides a chance for the smooth trajectories to move further towards a local optimum that was not feasible under the original spatial decomposition.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-D Iterative Refinement", "weight": 1.0} -->

Iterative refinement can be classified as an anytime algorithm. If a solution is needed quickly, the original set of $f^{i}$ can be obtained in a few seconds. If the budget of computational time is larger, iterative refinement can be repeated until the quadratic program cost converges.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-D Iterative Refinement", "weight": 1.0} -->

The user-supplied timestep duration $\Deltat$ directly affects the magnitudes of dynamic quantities such as acceleration and snap that are constrained by the robot's actuation limits. In the case that the final refined trajectories $f^{i}$ violate some constraint, we can apply a uniform temporal scaling to all trajectories. For quadrotors, as the temporal scaling goes to infinity, the actuator commands are guaranteed to approach a hover state, so kinodynamically feasible trajectories can always be found.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-E Discrete Postprocessing", "weight": 1.0} -->

Our grid-based MAPF discrete planner produces waypoints $p^{i}$ that require some postprocessing to ensure that they satisfy the collision constraints under arbitrary velocity profiles. In particular, we must deal with the case when one robot $r^{i}$ arrives at a vertex $v \in \mathcal{V}_{E}$ in the same timestep $k$ when another robot $r^{j}$ leaves $v$. This situation creates a conflict where neither robot's smooth trajectory can pass through $v$, as illustrated in Fig. 4. We ensure that this situation cannot happen by dividing each discrete line segment in half. In the subdivided discrete plan, odd timesteps exit a graph-vertex waypoint and arrive at a segment-midpoint waypoint, while even timesteps exit a segment-midpoint waypoint and arrive at a graph-vertex waypoint. Under this subdivision, the conflict cannot occur.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-E Discrete Postprocessing", "weight": 1.0} -->

In our experiments, we noticed that the continuous trajectories typically experience peak acceleration at $t = 0$ and $t = T$ due to the requirement of accelerating to/from a complete stop. We add an additional wait state at the beginning and end of the discrete plans to reduce the acceleration peak.

<!-- chunk {"id": "body-0050", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

We implement the discrete planner in C++ using the Boost Graph library for maximum flow computation and Gurobi 7.0 as the ILP solver. The continuous refinement stage is implemented in Matlab. We convert adjacent grid-cell obstacles into $N_{redObst}$ larger boxes using a greedy algorithm. To compute separating hyperplanes for the safe corridors, our method requires solving $O{({{KN^{2}} + {KN_{redObs}N}})}$ small ellipsoid-weighted SVM problems. For these problems, we use the CVXGEN package to generate C code optimized for the exact quadratic program specification. The per-robot trajectory optimization quadratic programs are solved using Matlab's quadprog solver. Since these problems are independent, this stage can take advantage of up to $N$ additional processor cores.

<!-- chunk {"id": "body-0051", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

In our experiments, we use a polynomial degree $D = 7$ and enforce continuity up to the fourth derivative ($C = 4$). We evaluate our method in simulation and on the Crazyswarm --- a swarm of nano-quadrotors.

<!-- chunk {"id": "body-0052", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

(a) Full 32-robot trajectory plan after six iterations of refinement. The start and end positions are marked by squares and filled circles, respectively. The obstacles are not shown for clarity.

<!-- chunk {"id": "body-0053", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

(b) Picture of the final configuration after the test flight. A video is available as supplemental material.

<!-- chunk {"id": "body-0054", "role": "body", "section": "VI-A Downwash Characterization", "weight": 1.0} -->

In order to determine the ellpsoid radii $E$, we executed several flight experiments. For $r_{z}$, we fly two quadrotors directly on top of each other and record the average position error of both quadrotors at $100\ {Hz}$ for varying distances between the quadrotors. We noticed that high controller gains lead to very low position errors even in this case, but can cause fatal crashes when the quadrotors are close. We determined $r_{z} = {0.3\ m}$ to be a safe vertical distance. For the horizontal direction, we use $r_{x} = r_{y} = {0.12\ m}$. We set $E_{obs}$ to a sphere of radius $0.15\ m$ based on the size of the Crazyflie quadrotor.

<!-- chunk {"id": "body-0055", "role": "body", "section": "VI-B Runtime Evaluation", "weight": 1.0} -->

We execute our implementation on a PC running Ubuntu 16.04, with a Xeon E5-2630 $2.2\ {GHz}$ CPU and $32\ {GB}$ RAM. This CPU has 10 physical cores, which improves the execution runtime for the continuous portion significantly. We compute plans for three example problems for 32 to 200 robots navigating in obstacle-rich environments. Table I summarizes the problems and breaks down the observed computation time into component parts. For the discrete step we report the runtime to find $LB{(K)}$ ($t_{LB}$), the runtime to solve the ILP with known $K$ ($t_{ILP}$), and the total time for the discrete solver to find paths for each robot ($t_{dis}$). For the continuous step we report $N_{redObst}$, the runtime for the first iteration ($t_{1}$), and the total time ($t_{con}$).

<!-- chunk {"id": "body-0056", "role": "body", "section": "VI-B Runtime Evaluation", "weight": 1.0} -->

For the first iteration, we report the time for finding the hyperplanes ($t_{1{({hp})}}$) and the time for solving the quadratic program ($t_{1{({qp})}}$).

<!-- chunk {"id": "body-0057", "role": "body", "section": "VI-B Runtime Evaluation", "weight": 1.0} -->

To investigate the effect of the robot ellipsoid size on computation time, we try each example with two ellipsoid heights: $r_{z} = {0.3\ m}$ corresponding to our experimental results, and $r_{z} = {0.9\ m}$ as an arbitrary larger safety distance. These necessitate safety margins of one and three empty grid cells, respectively, in the discrete planner. We notice that the choice of $r_{z}$ has little impact on the performance because there is enough slack in the examples to achieve a specific makespan even with higher safety distances. Furthermore, the estimated lower bound for $K$ is very close to the actual lowest possible $K$ in our examples, and the runtime for the discrete solver is dominated by solving the ILP.

<!-- chunk {"id": "body-0058", "role": "body", "section": "VI-B Runtime Evaluation", "weight": 1.0} -->

In the continuous portion, the balance between computing separating hyperplanes and solving the per-robot quadratic programs depends on the size of the problem. For all experiments, an initial solution is found in less than one minute. In these examples, we executed a total of six refinement iterations, which was enough for the quadratic program cost to converge in all of our experiments.

<!-- chunk {"id": "body-0059", "role": "body", "section": "VI-B Runtime Evaluation", "weight": 1.0} -->

One of the examples ("USC") is discussed in more detail in the next section. The supplemental material contains animated simulations for all examples.

<!-- chunk {"id": "body-0060", "role": "body", "section": "VI-C Flight Test", "weight": 1.0} -->

We discuss the different steps of our approach on a concrete task with 32 quadrotors. In this task, the quadrotors begin in a grid in the $x - y$ plane, fly through a wall with three holes, and form the letters "USC" in the air.

<!-- chunk {"id": "body-0061", "role": "body", "section": "VI-C Flight Test", "weight": 1.0} -->

The discrete planner plans on a grid of $0.5\ m$ side length and finds a solution of $K = 17$ timesteps in 40 seconds. The continuous planner needs three seconds to find the first set of smooth trajectories and finishes six iterations of refinement after 19 seconds. Fig. 7 shows the effect of iterative refinement on the dynamics properties of the trajectories $f^{i}$. For each iteration, we take the maximum acceleration and angular velocity over all robots for the duration of the trajectories. Iterative refinement results in trajectories with significantly smoother dynamics. This effect is also qualitatively visible when plotting a subset of the trajectories, as shown in Fig. 6. The final set of 32 trajectories is shown in Fig. 5(a).

<!-- chunk {"id": "body-0062", "role": "body", "section": "VI-C Flight Test", "weight": 1.0} -->

We use a swarm of Crazyflie 2.0 nano-quadrotors to execute the trajectories in a space with a physical barrier with windows. The space is ${{10\text{×}16}\text{×}2.5}\ m$ in size and equipped with a VICON motion capture system with 24 cameras. We upload the planned trajectories to the quadrotors before takeoff, and use the Crazyswarm infrastructure to execute the trajectories. State estimation and control run onboard the quadrotor, and the motion capture system information is broadcast to the UAVs for localization. Figure 5(b) shows a snapshot of the execution when the quadrotors reached their final state. The executed trajectories can be visualized with long-exposure photography, as shown in Fig. 1. The supplemental video shows the full trajectory execution.

<!-- chunk {"id": "body-0063", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

We presented a trajectory planning method for large quadrotor teams. Our approach is downwash-aware and thus creates plans where robots can safely fly in close proximity to each other. We plan trajectories using two independent stages, a discrete stage and a continuous stage. The presented discrete planner finds a goal assignment for each robot and a path such that the makespan is minimized while avoiding collisions and respecting downwash constraints. The continuous stage decouples each robot's trajectory planning, allowing easy parallelization and improving performance for large teams. The two-stage architecture supports the use of different discrete multi-agent planners, for example planners where each robot has an assigned goal or task-specific planners. Iterative refinement offers a user-controlled tradeoff between trajectory quality and computation time.

<!-- chunk {"id": "body-0064", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

Our approach can compute safe and arbitrarily smooth trajectories for hundreds of quadrotors in dense environments with obstacles in a few minutes. The trajectory plan outputs have been tested and executed safely in numerous trials on a team of 32 quadrotors.

<!-- chunk {"id": "body-0065", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

In future work, we plan to generalize our method to support arbitrary environments and start and goal locations that are not limited to an underlying grid, by exploring different discrete planning algorithms. We also plan to investigate performance improvements in both discrete and continuous stages.
