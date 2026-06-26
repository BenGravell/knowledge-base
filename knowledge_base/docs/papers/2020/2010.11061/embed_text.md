## Introduction and related work

(a) Circle configuration: 32 agents, 25 static obstacles and 25 dynamic obstacles.

(b) Sphere configuration: 32 agents, 18 static obstacles and 52 dynamic obstacles.

Figure 1: 32 agents using MADER to plan trajectories in a decentralized and asynchronous way in an environment with dynamic obstacles (light brown boxes and horizontal poles), static obstacles (dark brown pillars) and other agents.

While efficient and fast UAV trajectory planners for static worlds have been extensively proposed in the literature, a 3D real-time planner able to handle environments with static obstacles, dynamic obstacles *and* other planning agents still remains an open problem (see Fig. 1).

To be able to guarantee safety, the trajectory of the planning agent and the ones of other obstacles/agents need to be encoded in the optimization (see Fig. 2). A common representation of this trajectory in the optimization is via points discretized along the trajectory. However, this does not usually guarantee safety between two consecutive discretization points and alleviating that problem by using a fine discretization of the trajectory can lead to a very high computational burden. To reduce this computational burden, polyhedral outer representations of each interval of the trajectory are extensively used in the literature, with the added benefit of ensuring safety at all times (i.e., not just at the discretization points). A common way to obtain this polyhedral outer representation is via the convex hull of the control points of the Bernstein basis (basis used by Bézier curves) or the B-Spline basis. However, these bases do not yield very tight (i.e., with minimum volume) tetrahedra that enclose the curve, leading to conservative results.

MADER addresses this conservatism at its source and leverages our recently developed MINVO basis to obtain control points that generate the $n$-simplex (a tetrahedron for $n = 3$) with the minimum volume that completely contains each interval of the curve. Global optimality (in terms of minimum volume) of this tetrahedron obtained by the MINVO basis is guaranteed both in position and velocity space.

When other agents are present, the deconfliction problem between the trajectories also needs to be solved. Most of the state-of-the-art approaches either rely on centralized algorithms and/or on imposing an ad-hoc priority such that an agent only avoids other agents with higher priority. Some decentralized solutions have also been proposed, but they require synchronization between the replans of different agents. The challenge then is how to create a decentralized and asynchronous planner that solves the deconfliction problem and guarantees safety and feasibility for all the agents.

MADER solves this deconfliction in a decentralized and asynchronous way by including the trajectories other agents have committed to as constraints in the optimization. After the optimization, a collision check-recheck scheme ensures that the trajectory found is still feasible with respect to the trajectories other agents have committed to while the optimization was happening.

To impose collision-free constraints in the presence of static obstacles, a common approach is to *first* find convex decompositions of free space and *then* force (in the optimization problem) the outer polyhedral representation of each interval to be inside these convex decompositions. However, this approach can be conservative, especially in cluttered environments in which the convex decomposition algorithm may not find a tight representation of the free space. In the presence of dynamic obstacles, these convex decompositions become harder, and likely intractable, due to the extra time dimension.

Figure 2: Contributions of MADER.

To be able to impose collision-free constraints with respect to dynamic obstacles/agents, MADER imposes the separation between the polyhedral representations of each trajectory via planes. Moreover, MADER overcomes the conservatism of a convex decomposition (imposed ad-hoc before the optimization) by including a parameterization of these separating planes as decision variables in the optimization problem. The solver can thus choose the optimal location of these planes to determine collision avoidance. Including this plane parameterization reduces conservatism, but it comes at the expense of creating a nonconvex problem, for which a good initial guess is imperative. For this initial guess, we present a search-based algorithm that handles dynamic environments and obtains both the control points of the trajectory and the planes that separate it from other obstacles/agents.

The contributions of this paper are therefore summarized as follows (see also Fig. 2): Decentralized and asynchronous planning framework that solves the deconfliction between the agents by imposing as constraints the trajectories other agents have committed to, and then doing a collision check-recheck scheme to guarantee safety with respect to trajectories other agents have committed to during the optimization time.

Collision-free constraints are imposed by using a novel polynomial basis in trajectory planning: the MINVO basis. In position space, the MINVO basis yields a volume 2.36 and 254.9 times smaller than the extensively-used Bernstein and B-Spline bases, respectively.

Formulation of the collision-free constraints with respect to other dynamic obstacles/agents by including the planes that separate the outer polyhedral representations of each interval of every pair of trajectories as decision variables.

Extensive simulations and comparisons with state-of-the-art baselines in cluttered environments. The results show up to a 33.9% reduction in the flight time, a 88.8% reduction in the number of stops (compared to Bernstein/B-Spline bases), shorter flight distances than centralized approaches, and shorter total times on average than synchronous decentralized approaches.

## Definitions

Position, Velocity, Acceleration and Jerk, ∈ ℝ3.

State vector: $\mathbf{x}:=\begin{bmatrix} \mathbf{p}^{T} & \mathbf{v}^{T} & \mathbf{a}^{T} \end{bmatrix}^{T} \in {\mathbb{R}}^{9}$ m + 1 is the number of knots of the B-Spline. n + 1 is the number of control points of the B-Spline.

Degree of the polynomial of each interval of the B-Spline. In this paper we will use p = 3.

Set that contains the indexes of all the intervals of a B-Spline J:= {0, 1, …, m − 2 p − 1}. ξ:= Number of agents + Number of obstacles Index of the planning agent.

Set that contains the indexes of all the obstacles/agents, except the agent s. I:= {0, 1, …, ξ} ∖ s.

Index of the control point. l ∈ L for position, l ∈ L ∖ {n} for velocity and l ∈ L ∖ {n − 1, n} for acceleration.

Index of the obstacle/agent, i ∈ I.

Index of the interval, j ∈ J.

Radius of the sphere that models the agents.

Bi is the 3D axis-aligned bounding box (AABB) of the shape of the agent/obstacle i. For simplicity, we assume that the obstacles do not rotate. Hence, Bi does not change for a given obstacle/agent i. The AABB of the planning agent is denoted as Bs.

Each entry of ηs is the length of each side of the AABB of the planning agent (agent whose index is s). I.e., ${\mathbf{η}}_{s}:={2\begin{bmatrix} \rho & \rho & \rho \end{bmatrix}^{T}} \in {\mathbb{R}}^{3}$ Set of vertexes of the polyhedron that completely encloses the trajectory of the obstacle/agent i during the initial and final times of the interval j of the agent s.

Position, velocity, and acceleration control points, ∈ ℝ3.

Notation for the basis used: MINVO (b = MV), Bernstein (b = Be), or B-Spline (b = BS).

Set that contains the 4 position control points of the interval j of the trajectory of the agent s using the basis b. 𝒬j − 1MV ∩ 𝒬jMV = ⌀ in general. If b = Be, the last control point of interval j − 1 is also the first control point of interval j. If b = BS, the last 3 control points of interval j − 1 are also the first 3 control points of interval j. Analogous definition for the set 𝒱jb, which contains the three velocity control points.

Matrix whose columns contain the 4 position control points of the interval j of the trajectory of the agent s using the basis b. Analogous definition for the matrix Vjb, whose columns are the three velocity control points.

Linear function (see Eq. 1) such that 𝒬jMV = fjBS → MV (𝒬jBS) Linear function (see Eq. 1) such that 𝒱jMV = hjBS → MV (𝒬jBS) Plane ni jT x + di j = 0 that separates 𝒞i j from 𝒬jb.

Column vector of ones, element-wise absolute value, element-wise inequality, Minkowski sum, and convex hull.

Unless otherwise noted, this colormap in the trajectories will represent the norm of the velocity (blue 0 m/s and red vmax).

Snapshot at t = t1 (current time): gterm is the terminal goal, and is the current position of the UAV. is the trajectory the UAV is currently executing. is the trajectory the UAV is currently optimizing, starts at t = tin and finishes at t = tf. d is a point, used as the initial position of.

𝒮 is a sphere of radius r around d. will be contained in 𝒮. g is the projection of gt e r m onto the sphere 𝒮.

Predicted trajectory of an obstacle i, and committed trajectory of agent i.

𝒯j is a uniform discretization of [tp + j, tp + j + 1] (timespan of interval j of the trajectory of agent s) with step size γj and such that tp + j, tp + j + 1 ∈ 𝒯j.

Table I: Notation used in this paper This paper will use the notation shown in Table I, together with the following two definitions: Agent: Element of the environment with the ability to exchange information and take decisions accordingly (i.e., an agent can change its trajectory given the information received from the environment).

Obstacle: Element of the environment that moves on its own without consideration of the trajectories of other elements in the environment. An obstacle can be static or dynamic.

Note that here we are calling dynamic obstacles what some works in the literature call *non-cooperative agents*.

This paper will also use clamped uniform B-Splines, which are B-Splines defined by $n + 1$ control points $\{{\mathbf{q}}_{0},\ldots,{\mathbf{q}}_{n}\}$ and $m + 1$ knots $\{ t_{0},t_{1},\ldots,t_{m}\}$ that satisfy: and where the internal knots are equally spaced by $\Deltat$ (i.e. ${\Deltat}:={t_{k + 1} - {t_{k}{\forall k}}} = {\{ p,\ldots,{m - p - 1}\}}$). The relationship $m = {n + p + 1}$ holds, and there are in total ${m - {2p}} = {{n - p} + 1}$ intervals. Each interval $j \in J$ is defined in $t \in \left\lbrack t_{p + j},t_{p + j + 1} \right\rbrack$. In this paper we will use $p = 3$ (i.e. cubic B-Splines). Hence, each interval will be a polynomial of degree $3$, and it is guaranteed to lie within the convex hull of its $4$ control points $\{{\mathbf{q}}_{j}$, ${\mathbf{q}}_{j + 1}$, ${\mathbf{q}}_{j + 2}$, ${\mathbf{q}}_{j + 3}\}$. Moreover, clamped B-Splines are guaranteed to pass through the first and last control points (${\mathbf{q}}_{0}$ and ${\mathbf{q}}_{n}$). The velocity and acceleration of a B-Spline are B-Splines of degrees $p - 1$ and $p - 2$ respectively, whose control points are given: Finally, and as shown in Table I, to obtain $\mathbf{g}$ we project the terminal goal ${\mathbf{g}}_{\text{term}}$ to a sphere $\mathcal{S}$ centered on $\mathbf{d}$. This is done only for simplicity, and other possible way would be to choose $\mathbf{g}$ as the intersection between $\mathcal{S}$ and a piecewise linear path that goes from $\mathbf{d}$ to ${\mathbf{g}}_{\text{term}}$, and that avoids the static obstacles (and potentially the dynamic obstacles or agents as well). If a voxel grid of the environment is available, this piecewise linear path could be obtained by running a search-based algorithm, as done.

## Assumptions

This paper relies on the following four assumptions: Let $\mathbf{p}_{i}^{\text{real}}{(t)}$ denote the real future trajectory of an obstacle $i$, and $\mathbf{p}_{i}{(t)}$ the one obtained by a given tracking and prediction algorithm. The smallest dimensions of the axis-aligned box $D_{ij}$ for which is satisfied will be denoted as ${2\left({{\mathbf{α}}_{ij} + {\mathbf{β}}_{ij}} \right)} \in {\mathbb{R}}^{3}$. Here, $\mathcal{T}_{j}$ is a uniform discretization of $\lbrack t_{p + j},t_{p + j + 1}\rbrack$ with step size $\gamma_{j}$ (see Table I), ${\mathbf{α}}_{ij}$ represents the error associated with the prediction and ${\mathbf{β}}_{ij}$ the one associated with the discretization of the trajectory of the obstacle. The values ${\mathbf{α}}_{ij},{\mathbf{β}}_{ij}$ and $\gamma_{j}$ are assumed known. This assumption is needed to be able to obtain an outer polyhedral approximation of the Minkowski sum of a bounding box and any continuous trajectory of an obstacle (Sec. IV-C).

Similar to other works in the literature (see for instance), we assume that an agent can communicate without delay with other agents. Specifically, we assume that the planning agent has access to the committed trajectory $\mathbf{p}_{i}{(t)}$ of agent $i$ when this condition holds: This condition ensures that the agent $s$ knows the trajectories of the agents whose committed trajectories, inflated with their AABBs, pass through the sphere $\mathcal{S}$ (inflated with $B_{s}$) during the interval $\lbrack t_{\text{in}},t_{\text{f}}\rbrack$. Note also that all the agents have the same reference time, but trigger the planning iterations asynchronously.

Two agents do not commit to a new trajectory at the very same time. Note that, as time is continuous, the probability of this assumption not being true is essentially zero. Letting $t_{4}$ denote the time when a UAV commits to a trajectory, the reason behind this assumption is to guarantee that it is safe for a UAV to commit to a trajectory at $t = t_{4}$ having checked all the committed trajectories of other agents at $t < t_{4}$ (this will be explained in detail in Sec. VI).

Finally, we assume for simplicity that the obstacles do not rotate (and hence $B_{i}$ is constant for an obstacle $i$). However, this is not a fundamental assumption in MADER: To take into account the rotation of the objects, one could still use MADER, but use for the inflation (Sec. IV) the largest AABB that contains all the rotations of the obstacle during a specific interval $j$.

## Polyhedral representations

To avoid the computational burden of imposing infinitely-many constrains to separate two trajectories, we need to compute a tight polyhedral outer representation of every interval of the optimized trajectory (trajectory that agent $s$ is trying to obtain), the trajectory of the other agents and the trajectory of other obstacles (see also Table II).

Table II: Polyhedral representations of interval j from the point of view of agent s. Here, ℛi jMV denotes the set of MINVO control points of every interval of the trajectory of agent i that falls in [tin + j Δ t, tin + (j + 1) Δ t] (timespan of the interval j of the trajectory of agent s).

### IV-A Polyhedral Representation of the trajectory of the agent $s$

When using B-Splines, one common way to obtain an outer polyhedral representation for each interval is to use the polyhedron defined by the control points of each interval. As the functions in the B-Spline basis are positive and form a partition of unity, this polyhedron is guaranteed to completely contain the interval. However, this approximation is far from being tight, leading therefore to great conservatism both in the position and in the velocity space. To mitigate this, used the Bernstein basis for the constraints in the velocity space. Although this basis generates a polyhedron smaller than the B-Spline basis, it is still conservative, as this basis does not minimize the volume of this polyhedron. We instead use both in position *and* velocity space our recently derived MINVO basis that, by construction, is a polynomial basis that attempts to obtain the simplex with minimum volume that encloses a given polynomial curve. As shown in Fig. 3, this basis achieves a volume that is 2.36 and 254.9 times smaller (in the position space) and $1.29$ and $5.19$ times smaller (in the velocity space) than the Bernstein and B-Spline bases respectively. For each interval $j$, the vertexes of the MINVO control points (${\mathbf{Q}}_{j}^{\text{MV}}$ and ${\mathbf{V}}_{j}^{\text{MV}}$ for position and velocity respectively) and the B-Spline control points (${\mathbf{Q}}_{j}^{\text{BS}}$, ${\mathbf{V}}_{j}^{\text{BS}}$) are related as follows: | | {\mathbf{Q}}_{j}^{\text{MV}} & {= {{\mathbf{Q}}_{j}^{\text{BS}}{\mathbf{A}}_{\text{pos}}^{\text{BS}}{(j)}\left({\mathbf{A}}_{\text{pos}}^{\text{MV}} \right)^{- 1}}} \\ | | | | | {\mathbf{V}}_{j}^{\text{MV}} & {= {{\mathbf{V}}_{j}^{\text{BS}}{\mathbf{A}}_{\text{vel}}^{\text{BS}}{(j)}\left({\mathbf{A}}_{\text{vel}}^{\text{MV}} \right)^{- 1}}} | | | where the matrices $\mathbf{A}$ are known, and are available in our recent work (for the MINVO basis) and in (for the Bernstein and B-Spline bases). For the B-Spline bases, and because we are using clamped uniform splines, the matrices ${\mathbf{A}}_{\text{pos}}^{\text{BS}}{(j)}$ and ${\mathbf{A}}_{\text{vel}}^{\text{BS}}{(j)}$ depend on the interval $j$. Eq. 1, together with the fact that ${\mathbf{V}}_{j}^{\text{BS}}$ is a linear combination of ${\mathbf{Q}}_{j}^{\text{BS}}$, allow us to write | | \mathcal{Q}_{j}^{\text{MV}} & {= {f_{j}^{\text{BS}\rightarrow\text{MV}}{(\mathcal{Q}_{j}^{\text{BS}})}}} \\ | | | | | \mathcal{V}_{j}^{\text{MV}} & {= {h_{j}^{\text{BS}\rightarrow\text{MV}}{(\mathcal{Q}_{j}^{\text{BS}})}}} | | | where $f_{j}^{\text{BS}\rightarrow\text{MV}}{(\cdot)}$ and $h_{j}^{\text{BS}\rightarrow\text{MV}}{(\cdot)}$ are known linear functions.

Figure 3: Comparison of the volumes, areas and lengths obtained by the MINVO basis (ours), Bernstein basis (used by the Bézier curves) and B-Spline basis for an interval of a given uniform B-Spline. In the acceleration space, the three bases generate the same control points.

Figure 4: To impose collision-free constraints, MADER uses polyhedral representations of each interval of the trajectories of other agents/obstacles. On the left a given scenario with dynamic obstacles and on the right the polyhedral representations obtained (in red).

Figure 5: Example of a trajectory avoiding a dynamic obstacle. The obstacle has a box-like shape and is moving following a trefoil knot trajectory. The trajectory of the obstacle is divided into as many segments as the optimized trajectory has. An outer polyhedral representation (whose edges are shown as black lines) is computed for each of theses segments, and each segment of the trajectory avoids these polyhedra.

Figure 6: Collision-free constraints between agent 2 and both the obstacle 0 and agent 1. This figure is from the view of agent 2. tin and tf are the initial and final times of the trajectory being optimized (dashed lines), and they are completely independent of the initial and final optimization times of agent 1. 𝒬0MV are the control points of the interval 0 of the optimized trajectory using the MINVO basis. 𝒞13 are the vertexes of the convex hull of the vertexes of the control points of all the intervals of the trajectory of agent 1 that fall in [tf − Δ t, tf]. Note that the trajectories and polyhedra are in 3D, but they are represented in 2D for visualization purposes.

### IV-B Polyhedral Representation of the trajectory of other agents

We first increase the sides of $B_{i}$ by ${\mathbf{η}}_{s}$ to obtain the inflated box $B_{i}'$. Now, note that the trajectory of the agent $i \neq s$ is also a B-Spline, but its initial and final times can be different from $t_{\text{in}}$ and $t_{\text{f}}$ (initial and final times of the trajectory that agent $s$ is optimizing). Therefore, to obtain the polyhedral representation of the trajectory of the agent $i$ in the intervals $\lbrack t_{\text{in}},{t_{\text{in}} + {\Deltat}}\rbrack$, $\lbrack{t_{\text{in}} + {\Deltat}},{t_{\text{in}} + {2\Deltat}}\rbrack$,..., $\lbrack{t_{\text{f}} - {\Deltat}},t_{\text{f}}\rbrack$ we first compute the MINVO control points of every interval of the trajectory of agent $i$ that falls in one of these intervals. The convex hull of the boxes $B_{i}'$ placed in every one of these control points will be the polyhedral representation of the interval $j$ of the trajectory of the agent $i$. We denote the vertexes of this outer polyhedral representation as $\mathcal{C}_{ij}$.

### IV-C Polyhedral Representation of the trajectory of the obstacles

For each interval $j$ we first increase the sides of $B_{i}$ by ${\mathbf{η}}_{s} + {2{({{\mathbf{β}}_{ij} + {\mathbf{α}}_{ij}})}}$, and denote this inflated box $B_{i}'$. Here ${\mathbf{β}}_{ij}$ and ${\mathbf{α}}_{ij}$ are the values defined in Sec. III. We then place $B_{i}'$ in $\mathbf{p}_{i}{(\mathcal{T}_{j})}$, where $\mathbf{p}_{i}{(\mathcal{T}_{j})}$ denotes the set of positions of the obstacle $i$ at the times $\mathcal{T}_{j}$ (see Table I) and compute the convex hull of all the vertexes of these boxes. Given the first assumption of Sec. III, this guarantees that the convex hull obtained is an outer approximation of all the 3D space occupied by the obstacle $i$ (inflated by the size of the agent $s$) during the interval $j$. The static obstacles are treated in the same way, with ${\mathbf{p}_{i}{(t)}} = \text{constant}$. An example of these polyhedral representations is shown in Fig. 4.

## Optimization And Initial Guess

### V-A Collision-free constraints

Once the polyhedral approximation of the trajectories of the other obstacles/agents have been obtained, we enforce the collision-free constraints between these polyhedra and the ones of the optimized trajectory as follows: we introduce the planes ${\mathbf{π}}_{ij}$ (characterized by ${\mathbf{n}}_{ij}$ and $d_{ij}$) that separate them as decision variables in the optimization problem and force this way the separation between the vertexes in $\mathcal{C}_{ij}$ and the MINVO control points $\mathcal{Q}_{j}^{\text{MV}}$ (see Figs. 5 and 6): | | ${{{{\mathbf{n}}_{ij}^{T}{\mathbf{c}}} + d_{ij}} > 0}\mspace{21mu}{{{\forall{\mathbf{c}}} \in \mathcal{C}_{ij}},{{{\forall i} \in I},{j \in J}}}$ | | \(3\) | | | ${{{{\mathbf{n}}_{ij}^{T}{\mathbf{q}}} + d_{ij}} < 0}\mspace{21mu}{{{\forall{\mathbf{q}}} \in \mathcal{Q}_{j}^{\text{MV}}},{{\forall j} \in J}}$ | | |

### V-B Other constraints

The initial condition (position, velocity and acceleration) is imposed by ${\mathbf{x}{(t_{\text{in}})}} = \mathbf{x}_{in}$. Note that ${\mathbf{p}}_{\text{in}}$, ${\mathbf{v}}_{\text{in}}$ and ${\mathbf{a}}_{\text{in}}$ completely determine ${\mathbf{q}}_{0}$, ${\mathbf{q}}_{1}$ and ${\mathbf{q}}_{2}$, so these control points are not included as decision variables.

For the final condition, we use a final stop condition imposing the constraints ${\mathbf{v}{(t_{\text{f}})}} = \mathbf{v}_{f} = \mathbf{0}$ and ${\mathbf{a}{(t_{\text{f}})}} = \mathbf{a}_{f} = \mathbf{0}$. These conditions require ${\mathbf{q}}_{n - 2} = {\mathbf{q}}_{n - 1} = {\mathbf{q}}_{n}$, so the control points ${\mathbf{q}}_{n - 1}$ and ${\mathbf{q}}_{n}$ can also be excluded from the set of decision variables. The final position is included as a penalty cost $\left\| {{\mathbf{q}}_{n - 2} - {\mathbf{g}}} \right\|_{2}^{2}$ in the objective function, weighted with a parameter $\omega \geq 0$. Here $\mathbf{g}$ is the goal (projection of the ${\mathbf{g}}_{\text{term}}$ onto a sphere $\mathcal{S}$ of radius $r$ around $\mathbf{d}$, see Table I). Note that, as we are using clamped uniform B-Splines with a final stop condition, ${\mathbf{q}}_{n - 2}$ coincides with the last position of the B-Spline. The reason of adding this penalty cost for the final position, instead of including ${\mathbf{q}}_{n - 2} = {\mathbf{g}}$ as a hard constraint, is that a hard constraint can easily lead to infeasibility if the heuristics used for the total time $({t_{\text{f}} - t_{\text{in}}})$ underestimates the time needed to reach $\mathbf{g}$.

To force the trajectory generated to be inside the sphere $\mathcal{S}$, we impose the constraint Moreover, we also add the constraints on the maximum velocity and acceleration: | | | ${{\text{abs}({\mathbf{v}})} \leq {\mathbf{v}}_{\text{max}}}\mspace{21mu}{{{\forall{\mathbf{v}}} \in \mathcal{V}_{j}^{\text{MV}}},{{\forall j} \in J}}$ | | \(5\) | | | | ${{\text{abs}\left({\mathbf{a}}_{l} \right)} \leq {\mathbf{a}}_{\text{max}}}\mspace{21mu}{{\forall l} \in {L\backslash{\{{n - 1},n\}}}}$ | | | where we are using the MINVO velocity control points for the velocity constraint. For the acceleration constraint, the B-Spline and MINVO control points are the same (see Fig. 3). Note that the velocity and acceleration are constrained independently on each one of the axes $\{ x,y,z\}$.

### V-C Control effort

The evaluation of a cubic clamped uniform B-Spline in an interval $j \in J$ can be done as follows: where $u_{j}:=\frac{t - t_{p + j}}{t_{p + j + 1} - t_{p + j}}$, $t \in {\lbrack t_{p + j},t_{p + j + 1}\rbrack}$ and ${\mathbf{A}}_{\text{pos}}^{\text{BS}}{(j)}$ is a known matrix that depends on each interval. Specifically, and with the knots chosen, we will have ${{\mathbf{A}}_{\text{pos}}^{\text{BS}}{}} \neq {{\mathbf{A}}_{\text{pos}}^{\text{BS}}{}} \neq {{\mathbf{A}}_{\text{pos}}^{\text{BS}}{}} = \ldots = {{\mathbf{A}}_{\text{pos}}^{\text{BS}}{({m - {2p} - 3})}} \neq {{\mathbf{A}}_{\text{pos}}^{\text{BS}}{({m - {2p} - 2})}} \neq {{\mathbf{A}}_{\text{pos}}^{\text{BS}}{({m - {2p} - 1})}}$. Now, note that Therefore, as the jerk is constant in each interval (since $p = 3$), the control effort is:

### V-D Optimization Problem

Given the constraints and the objective function explained above, the optimization problem solved is as follows^11^1In the optimization problem, $\forall i$ and $\forall j$ denote, respectively, ${\forall i} \in I$ and ${\forall j} \in J$.: This problem is clearly nonconvex since we are minimizing over the control points *and* the planes ${\mathbf{π}}_{ij}$ (characterized by ${\mathbf{n}}_{ij}$ and $d_{ij}$). Note also that the decision variables are the B-Spline control points $\mathcal{Q}_{j}^{\text{BS}}$. In the constraints, the MINVO control points $\mathcal{Q}_{j}^{\text{MV}}$ and $\mathcal{V}_{j}^{\text{MV}}$ are simply linear transformations of the decision variables (see Eq. 2). We solve this problem using the augmented Lagrangian method, and with the globally-convergent method-of-moving-asymptotes (MMA) as the subsidiary optimization algorithm. The interface used for these algorithms is NLopt. The time allocated per trajectory is chosen before the optimization as ${({t_{\text{f}} - t_{\text{in}}})} = \frac{\left\| {{\mathbf{g}} - {\mathbf{d}}} \right\|_{2}}{v_{max}}$.

### V-E Initial Guess

4 Compute q0, q1 and q2 from pin, vin and ain 6 while Q is not empty do 9 Remove first element of Q 10 ℳ←Uniformly sample vl satisfying vm a x and am a x 11 if any of the conditions 1-6 is true then 24 ${\mathbf{q}}_{l + 1}\leftarrow{{\mathbf{q}}_{l} + {\frac{t_{l + p + 1} - t_{l + 1}}{p}{\mathbf{v}}_{l}}}$ 30 return Closest Path found Algorithm 1 Octopus Search To obtain an initial guess (which consists of both the control points ${\{{\mathbf{q}}_{0},\ldots,{\mathbf{q}}_{n}\}}^{\text{BS}}$ and the planes ${\mathbf{π}}_{ij}$), we use the Octopus Search algorithm shown in Alg. 1. The Octopus Search takes inspiration from A^\*^, but it is designed to work with B-Splines, handle dynamic obstacles/agents, and use the MINVO basis for the collision check. Each control point will be a node in the search. All the open nodes are kept in a priority queue $Q$, in which the elements are ordered in increasing order of $f = {g + {\epsilonh}}$, where $g$ is the sum of the distances (between successive control points) from ${\mathbf{q}}_{0}$ to the current node (cost-to-come), $h$ is the distance from the current node to the goal (heuristics of the cost-to-go), and $\epsilon$ is the bias. Similar to A^\*^, this ordering of the priority queue makes nodes with lower $f$ be explored first.

The way the algorithm works is as follows: First, we compute the control points ${\mathbf{q}}_{0},{\mathbf{q}}_{1},{\mathbf{q}}_{2}$, which are determined from ${\mathbf{p}}_{\text{in}},{\mathbf{v}}_{\text{in}}$ and ${\mathbf{a}}_{\text{in}}$. After adding ${\mathbf{q}}_{2}$ to the queue $Q$ (line 1), we run the following loop until there are no elements in $Q$: First we store in ${\mathbf{q}}_{l}$ the first element of $Q$, and remove it from $Q$ (lines 1-1). Then, we store in a set $\mathcal{M}$ velocity samples for ${\mathbf{v}}_{l}$ that satisfy both $v_{\text{max}}$ and $a_{\text{max}}$^22^2In these velocity samples, we use the B-Spline velocity control points, to avoid the dependency with past velocity control points that appears when using the MINVO or Bernstein bases. But note that this is only for the initial guess, in the optimization problem the MINVO velocity control points are used.. After this, we discard the current ${\mathbf{q}}_{l}$ if any of these conditions are true (l.s. denotes linearly separable): $\mathcal{Q}_{l - 3}^{\text{MV}}$ is not l.s. from $\mathcal{C}_{i,{l - 3}}$ for some $i \in I$. $l = {({n - 2})}$ and $\mathcal{Q}_{n - 4}^{\text{MV}}$ is not l.s. from $\mathcal{C}_{i,{n - 4}}$ for some $i \in I$. $l = {({n - 2})}$ and $\mathcal{Q}_{n - 3}^{\text{MV}}$ is not l.s. from $\mathcal{C}_{i,{n - 3}}$ for some $i \in I$. $\left\| {{\mathbf{q}}_{l} - {\mathbf{d}}} \right\|_{2} > r$. $\left\| {{\mathbf{q}}_{l} - {\mathbf{q}}_{k}} \right\|_{\infty} \leq \epsilon'$ for some ${\mathbf{q}}_{k}$ already added to $Q$.

Cardinality of $\mathcal{M}$ is zero.

Condition 1 ensures that the convex hull of $\mathcal{Q}_{l - 3}^{\text{MV}}$ does not collide with any interval $l - 3$ of other obstacle/agent $i \in I$. The linear separability is checked by solving the following feasibility linear problem for the interval $j = {l - 3}$ of every obstacle/agent $i \in I$: where the decision variables are the planes ${\mathbf{π}}_{ij}$ (defined by ${\mathbf{n}}_{ij}$ and $d_{ij}$). We solve this problem using GLPK. Note that we also need to check the conditions 2 and 3 due to the fact that ${\mathbf{q}}_{n - 2} = {\mathbf{q}}_{n - 1} = {\mathbf{q}}_{n}$ and hence the choice of ${\mathbf{q}}_{n - 2}$ in the search forces the choice of ${\mathbf{q}}_{n - 1}$ and ${\mathbf{q}}_{n}$. In all these three previous conditions, the MINVO control points are used.

As in the optimization problem we are imposing the trajectory to be inside the sphere $\mathcal{S}$, we also discard ${\mathbf{q}}_{l}$ if condition 4 is not satisfied. Additionally, to keep the search computationally tractable, we discard ${\mathbf{q}}_{l}$ if it is very close to another ${\mathbf{q}}_{k}$ already added to $Q$ (condition 5): we create a voxel grid of voxel size $2\epsilon'$, and add a new control point to $Q$ only if no other point has been added before within the same voxel. Finally, we also discard ${\mathbf{q}}_{l}$ if there are not any feasible samples for ${\mathbf{v}}_{l}$ (condition 6).

Then, we check if we have found all the control points and if ${\mathbf{q}}_{n - 2}$ is sufficiently close to the goal $\mathbf{g}$ (distance less than $\epsilon^{\operatorname{\prime\prime}}$). If this is the case, the control points ${\mathbf{q}}_{n - 1}$ and ${\mathbf{q}}_{n}$ (which are the same as ${\mathbf{q}}_{n - 2}$ due to the final stop condition) are added to the list of the corresponding control points, and are returned together with all the separating planes ${{{\mathbf{π}}_{ij}{\forall i}} \in I},{{\forall j} \in J}$ (lines 1-1). If the goal has not been reached yet, we use the velocity samples $\mathcal{M}$ to generate ${\mathbf{q}}_{l + 1}$ and add them to $Q$ (lines 1-1). If the algorithm is not able to find a trajectory that reaches the goal, the one found that is closest to the goal is returned (line 1).

Figure 7: Example of the trajectories found by the Octopus Search in an environment with a dynamic obstacle following a trefoil knot trajectory. The best trajectory found is the thickest one in the figure.

Figure 8: Deconfliction between agents. Each agent includes the trajectories other agents have committed to as constraints in the optimization. After the optimization, a collision check-recheck scheme is performed to ensure feasibility with respect to trajectories other agents have committed to while the optimization was happening. In this example, agent B starts the optimization after agent A, but commits to a trajectory before agent A. Hence, when agent A finishes the optimization it needs to check whether the trajectory found collides or not with the trajectory agent B committed to at t = t4B, q. If it collides, agent A will simply keep executing the trajectory available at t = t1A, h. If it does not collide, agent A will do the Recheck step to ensure no agent has committed to any trajectory during the Check period, and if this Recheck step is satisfied, agent A will commit to the trajectory found.

Fig. 7 shows an example of the trajectories found by the Octopus Search algorithm in an environment with a dynamic obstacle following a trefoil knot trajectory.

### V-F Degree of the splines

In this paper, we focused on the case $p = 3$ (i.e., cubic splines). However, MADER could also be used with higher (or lower) order splines. For instance, one could use splines of fourth-degree polynomials (i.e., $p = 4$), minimize snap (instead of jerk), and then use the corresponding MINVO polyhedron that encloses each fourth-degree interval for the obstacle avoidance constraints. The reason behind the choice of cubic splines, instead of higher/lower order splines, is that cubic splines are a good trade-off between dynamic feasibility of a UAV and computational tractability.

## Deconfliction

Figure 9: At t = t1A, h, agent A chooses the point d along the current trajectory that it is executing, with an offset δ t from the current position. Then, it allocates κ δ t seconds to obtain an initial guess. The closest trajectory found to g is used as the initial guess if the search has not finished by that time. Then, the nonconvex optimization runs for μ δ t seconds, choosing the best feasible solution found if no local optimum has been found by then. κ and μ satisfy κ > 0, μ > 0, κ + μ < 1.

To guarantee that the agents plan trajectories asynchronously while not colliding with other agents that are also constantly replanning, we use a deconfliction scheme divided in these three periods (see Fig. 8): The Optimization period happens during $t \in {(t_{1},t_{2}\rbrack}$. The optimization problem will include the polyhedral outer representations of the trajectories ${{p_{i}{(t)}},i} \in I$ in the constraints. All the trajectories other agents commit to during the Optimization period are stored.

The Check happens during $t \in {(t_{2},t_{3}\rbrack}$. The goal of this period is to check whether the trajectory found in the optimization collides with the trajectories other agents have committed to during the optimization. This collision check is done by performing feasibility tests solving the Linear Program 7 $\forall j$ for every agent $i$ that has committed to a trajectory while the optimization was being performed (and whose new trajectory was not included in the constraints at $t_{1}$). A boolean flag is set to true if any other agent commits to a new trajectory during this Check period.

The Recheck period aims at checking whether agent A has received any trajectory during the Check period, by simply checking if the boolean flag is true or false. As this is a single Boolean comparison in the code, it allows us to assume that no trajectories have been published by other agents while this recheck is done, avoiding therefore an infinite loop of rechecks.

With $h$ denoting the replanning iteration of an agent A, the time allocation for each of these three periods described above is explained in Fig. 9: to choose the initial condition of the iteration $h$, Agent A first chooses a point $\mathbf{d}$ along the trajectory found in the iteration $h - 1$, with an offset of $\deltat$ seconds from the current position. Here, $\deltat$ should be an estimate of how long iteration $h$ will take. To obtain this estimate, and similar to our previous work, we use the time iteration $h - 1$ took multiplied by a factor $\alpha \geq 1$: ${\deltat} = {\alpha\left( {t_{4}^{A,{h - 1}} - t_{1}^{A,{h - 1}}} \right)}$. Agent A then should finish the replanning iteration $h$ in less than $\deltat$ seconds. To do this, we allocate a maximum runtime of $\kappa\deltat$ seconds to obtain an initial guess, and a maximum runtime of $\mu\deltat$ seconds for the nonconvex optimization. Here ${\kappa > 0},{\mu > 0}$ and ${\kappa + \mu} < 1$, to give time for the Check and Recheck. If the Octopus Search takes longer than $\kappa\deltat$, the trajectory found that is closest to the goal is used as the initial guess. Similarly, if the nonconvex optimization takes longer than $\mu\deltat$, the best feasible solution found is selected.

Fig. 8 shows an example scenario with only two agents A and B. Agent A starts its $h$-th replanning step at $t_{1}^{A,h}$, and finishes the optimization at $t_{2}^{A,h}$. Agent B starts its $q$-th replanning step at $t_{1}^{B,q}$. In the example shown, agent B starts the optimization later than agent A ($t_{1}^{B,q} > t_{1}^{A,h}$), but solves the optimization earlier than agent A ($t_{2}^{B,q} < t_{2}^{A,h}$). As no other agent has obtained a trajectory while agent B was optimizing, agent B does not have to check anything, and commits directly to the trajectory found. However, when agent A finishes the optimization at $t_{2}^{A,h} > t_{4}^{B,q}$, it needs to check if the trajectory found collides with the one agent B has committed to. If they do not collide, agent A will perform the Recheck by ensuring that no trajectory has been published while the Check was being performed.

An agent will keep executing the trajectory found in the previous iteration if any of these four scenarios happens: The trajectory obtained at the end of the optimization collides with any of the trajectories received during the Optimization.

The agent has received any trajectory from other agents during the Check period.

No feasible solution has been found in the Optimization.

The current iteration takes longer than $\deltat$ seconds.

Figure 10: Corridor environment of size 73 m × 4 m × 3 m used for the single-agent simulation. It contains 100 randomly-deployed dynamic obstacles that follow a trefoil knot trajectory. The corridor is along the x direction.

Figure 11: Boxplots and normalized histograms of the velocity profile of vx in the corridor environment shown in Fig. 10. The velocity constraint used was vm a x = 5 ⋅ 1 m/s. The histograms are for all the velocities obtained across 10 different simulations.

Under the third assumption explained in Sec. III (i.e., two agents do not commit to their trajectory at the very same time), this deconfliction scheme explained guarantees safety with respect to the other agents, which is proven as follows: If the planning agent commits to a new trajectory in the current replanning iteration, this new trajectory is guaranteed to be collision-free because it included all the trajectories of other agents as constraints, and it was checked for collisions with respect to the trajectories other agents have committed to during the planning agent's optimization time.

If the planning agent does not commit to a new trajectory in that iteration (because one of the scenarios 1--4 occur), it will keep executing the trajectory found in the previous iteration. This trajectory is still guaranteed to be collision-free because it was collision-free when it was obtained and other agents have included it as a constraint in any new plans that have been made recently. If the agent reaches the end of this trajectory (which has a final stop condition), the agent will wait there until it obtains a new feasible solution. In the meanwhile, all the other agents are including its position as a constraint for theirs trajectories, guaranteeing therefore safety between the agents.

## Results

We now test MADER in several single-agent and multi-agent simulation environments. The computers used for the simulations are an AlienWare Aurora r8 desktop (for the C++ simulations of VII-B), a ROG Strix GL502VM laptop (for the Matlab simulations of Sec. VII-B) and a general-purpose-N1 Google Cloud instance (for the simulations of Sec. VII-A and VII-C).

### VII-A Single-Agent simulations

To highlight the benefits of the MINVO basis with respect to the Bernstein or B-Spline bases, we first run the algorithm proposed in a corridor-like enviroment (${{{{73\text{m}} \times 4}\text{m}} \times 3}\text{m}$) depicted in Fig. 10. that contains 100 randomly-deployed dynamic obstacles of sizes ${{{{0.8\text{m}} \times 0.8}\text{m}} \times 0.8}\text{m}$. All the obstacles follow a trajectory whose parametric equations are those of a trefoil knot. The radius of the sphere $\mathcal{S}$ used is $r = 4.0$ m, and the velocity and acceleration constraints for the UAV are ${\mathbf{v}}_{max} = {{{5 \cdot \mathbf{1}}m}/s}$ and ${\mathbf{a}}_{max} = {{\begin{bmatrix} \end{bmatrix}^{T}m}/s^{2}}$. The velocity profile for $v_{x}$ is shown in Fig. 11. For the same given velocity constraint ($v_{\text{max}} = {{5m}/s}$), the mean velocity $v_{x}$ achieved by the MINVO basis is ${4.15m}/s$, higher than the ones achieved by the Bernstein and B-Spline basis (${3.23m}/s$ and ${2.79m}/s$ respectively).

Table III: Comparison of the number of stops and time to reach the goal in a corridor-like environment using different bases and with different number of obstacles.

Figure 12: Time to reach the goal and number of times the UAV had to stop for different number of obstacles. 5 simulations were performed for each combination of basis (MINVO, Bernstein and B-Spline) and number of obstacles. The shaded area is the 1σ interval, where σ is the standard deviation.

We now compare the time it takes for the UAV to reach the goal using each basis in the same corridor environment but varying the total number of obstacles (from 50 obstacles to 250 obstacles). Moreover, and as a stopping condition is not a safe condition in a world with dynamic obstacles, we also report the number of times the UAV had to stop. The results are shown in Table III and Fig. 12. In terms of number of stops, the use of the MINVO basis achieves reductions of 86.4% and 88.8% with respect to the Bernstein and B-Spline bases respectively. In terms of the time to reach the goal, the MINVO basis achieves reductions of 22.3% and 33.9% compared to the Bernstein and B-Spline bases respectively. The reason behind all these improvements is the tighter outer polyhedral approximation of each interval of the trajectory achieved by the MINVO basis in the velocity and position spaces.

### VII-B Multi-Agent simulations without obstacles

We now compare MADER with the following different state-of-the-art algorithms: Sequential convex programming.

Relative Bernstein Polynomial approach (RBP^††^footnotemark:, ).

Distributed model predictive control.

Decoupled incremental sequential convex programming (dec_iSCP^††^footnotemark:,).

Search-based motion planing, both in its sequential version (decS_Search) and in its non-sequential version (decNS_Search).

To classify these different algorithms, we use the following definitions: Decentralized: Each agent solves its own optimization problem.

Replanning: The agents have the ability to plan several times as they fly (instead of planning only once before starting to fly). The algorithms with replanning are also classified according to whether they satisfy the real-time constraint in the replanning: algorithms that satisfy this constraint are able to replan in less than $\deltat$ or at least have a trajectory they can keep executing in case no solution has found by then (see Fig. 9). Algorithms that do not satisfy this constraint allow replanning steps longer than $\deltat$ (which is not feasible in the real world), and simulations are performed by simply having a simulation time that runs completely independent of the real time.

Asynchronous: The planning is triggered independently by each agent without considering the planning status of other agents. Examples of synchronous algorithms include the ones that trigger the optimization of all the agents at the same time or that impose that one agent cannot plan until another agent has finished.

Discretization for inter-agent constraints: The collision-free constraints between the agents are imposed only on a finite set of points of the trajectories. The discretization step will be denoted as $h$ seconds.

In the test scenario, 8 agents are in a $8 \times 8$ m square, and they have to swap their positions. The velocity and acceleration constraints used are ${\mathbf{v}}_{max} = {{{1.7 \cdot \mathbf{1}}m}/s}$ and $a_{max} = {{{6.2 \cdot \mathbf{1}}m}/s^{2}}$, with a drone radius of 15 cm. Moreover, we define the safety ratio as ${\min_{i,i^{'}}d_{min}^{i,i'}}/{({\rho_{i} + \rho_{i'}})}$, where $d_{min}^{i,i'}$ is the minimum distance over all the pairs of agents $i$ and $i'$, and $\rho_{i}$, $\rho_{i'}$ denote their respective radii. Safety is ensured if safety ratio $> 1$. For the RBP and DMPC algorithms, the downwash coefficient $c$ was set to $c = 1$ (so that the drone is modeled as a sphere as in all the other algorithms).

Total Flight Distance (m) RBP, batch_size=1 RBP, batch_size=2 RBP, batch_size=4 dec_iSCP∗, hiSCP = 0.4 s dec_iSCP∗, hiSCP = 0.3 s dec_iSCP∗, hiSCP = 0.2 s dec_iSCP∗, hiSCP = 0.15 s Table IV: Comparison between MADER (ours), SCP, RBP, DMPC, dec_iSCP, decS_Search and decNS_Search. For SCP and MADER, the time and distance results are the mean of 5 runs, and the safety ratio is the minimum across all the runs. The test environment consists of 8 agents in a square that swap their positions without obstacles. For the algorithms that have replanning, the values in the columns of computation and execution times are t1s t start | tlast start | t1s t end (see Fig. 13). The superscript ∗ means the available implementation of the algorithm is in MATLAB (rest is in C++). Algorithms that have replanning but do not satisfy the real-time constraints in the replanning are denoted as Yes/No in the Replan? column of the table.

The results obtained, together with the classification of each algorithm, are shown in Table IV. For the algorithms that replan as they fly, we show the following times (see Fig. 13): $t_{1^{st}\text{start}}$ (earliest time a UAV starts flying), $t_{\text{last start}}$ (latest time a UAV starts flying), $t_{1^{st}\text{end}}$ (earliest time a UAV reaches the goal) and the total time $t_{\text{total}}$ (time when all the UAVs have reached their goals). Note that the algorithm decNS_Search is synchronous (link), and it does not satisfy the real-time constraints in the replanning iterations (link). Several conclusions can be drawn from Table IV: Algorithms that use discretization to impose inter-agent constraints are in general not safe due to the fact that the constraints may not be satisfied between two consecutive discretization points. A smaller discretization step may solve this, but at the expense of very high computation times.

Compared to the centralized solution that generates safe trajectories (RBP), MADER achieves a shorter overall flight distance. The total time of MADER is also shorter than the one of RBP.

Compared to decentralized algorithms (DMPC, dec_iSCP, decS_Search and decNS_Search), MADER is the one with the shortest total time, except for the case of decNS_Search with $u = {{5m}/s^{3}}$. However, for this case the flight distance achieved by MADER is $6.3$ m shorter. Moreover, MADER is asynchronous and satisfies the real-time constraints in the replanning, while decNS_Search does not.

From all the algorithms shown in Table IV, MADER is the only algorithm that is decentralized, has replanning, satisfies the real-time constraints in the replanning and is asynchronous.

Figure 13: Time notation for the algorithms that have replanning.

Figure 14: Results for the circle environment, that contains 25 static obstacles (pillars) and 25 dynamic obstacles (boxes). The case with 32 agents is shown in Fig. 1a.

Figure 15: Results for the sphere environment, that contains 18 static obstacles (pillars) and 52 dynamic obstacles (boxes and horizontal poles). The case with 32 agents is shown in Fig. 1b.

Flight Distance per agent (m) Safety ratio between agents Number of stops per agent Table V: Results for MADER in the circle and sphere environments.

For MADER, and measured on the simulation environment used in this Section, each UAV performs on average 12 successful replans before reaching the goal. On average, the check step takes $\approx 2.87$ ms, the recheck step takes $\approx 0.034$ $\mu$s, and the total replanning time is $\approx 199.6$ ms. Approximately half of this replanning time is allocated to find the initial guess (i.e., $\kappa = 0.5$).

### VII-C Multi-Agent simulations with static and dynamic obstacles

We now test MADER in multi-agent environments that have also static and dynamic obstacles. For this set of experiments, we use ${\mathbf{α}}_{j} = {\mathbf{β}}_{j} = {3 \cdot \mathbf{1}}$ cm, $\gamma_{j} = 0.1$ s $\forall j$, $r = 4.5$ m (radius of the sphere $\mathcal{S}$), and a drone radius of $5$ cm. We test MADER in the following two environments: Circle environment: the UAVs start in a circle formation and have to swap their positions while flying in a world with 25 static obstacles of size ${{{{0.4\text{m}} \times 8}\text{m}} \times 0.4}\text{m}$ and 25 dynamic obstacles of size ${{{{0.6\text{m}} \times 0.6}\text{m}} \times 0.6}\text{m}$ following a trefoil knot trajectory. The radius of the circle the UAVs start from is $10$ m.

Sphere environment: the UAVs start in a sphere formation and have to swap their positions while flying in a world with 18 static obstacles of size ${{{{0.4\text{m}} \times 8}\text{m}} \times 0.4}\text{m}$, 17 dynamic obstacles of size ${{{{0.4\text{m}} \times 4}\text{m}} \times 0.4}\text{m}$ (moving in $z$) and 35 dynamic obstacles of size ${{{{0.6\text{m}} \times 0.6}\text{m}} \times 0.6}\text{m}$ following a trefoil knot trajectory. The radius of the sphere the UAVs start from is $10$ m.

The results can be seen in Table V and in Figs. 1, 14 and 15. All the safety ratios between the agents are $> 1$, and the flight distances achieved (per agent) are approximately $21.5$ m. With respect to the number of stops, none of the UAVs had to stop in the circle environment with 4 and 8 agents and in the sphere environment with 4 agents. For the circle environment with 16 and 32 agents, each UAV stops (on average) 0.188 and 1.5 times respectively. For the sphere environment with 8, 16, and 32 agents, each UAV stops (on average) 0.125, 0.125, and 1.0 times respectively.\Note also that only the two agents that have been the closest are the ones that determine the actual value of the safety ratio, while the other agents do not contribute to this value. This means that, while the safety ratio is likely to decrease with the number of agents, a monotonic decrease of the safety ratio with respect to the number of agents is not strictly required.

## Conclusions

This work presented MADER, a decentralized and asynchronous planner that handles static obstacles, dynamic obstacles and other agents. By using the MINVO basis, MADER obtains outer polyhedral representations of the trajectories that are 2.36 and 254.9 times smaller than the volumes achieved using the Bernstein and B-Spline bases. To ensure non-conservative, collision-free constraints with respect to other obstacles and agents, MADER includes as decision variables the planes that separate each pair of outer polyhedral representations. Safety with respect to other agents is guaranteed in a decentralized and asynchronous way by including their committed trajectories as constraints in the optimization and then executing a collision check-recheck scheme. Extensive simulations in dynamic multi-agent environments have highlighted the improvements of MADER with respect to other state-of-the-art algorithms in terms of number of stops, computation/execution time and flight distance. Future work includes adding perception-aware and risk-aware terms in the objective function, as well as hardware experiments.
