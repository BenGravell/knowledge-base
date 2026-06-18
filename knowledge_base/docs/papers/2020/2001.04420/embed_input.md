<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

FASTER: Fast and Safe Trajectory Planner for Navigation in Unknown Environments

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Planning high-speed trajectories for UAVs in unknown environments requires algorithmic techniques that enable fast reaction times to guarantee safety as more information about the environment becomes available. The standard approaches that ensure safety by enforcing a "stop" condition in the free-known space can severely limit the speed of the vehicle, especially in situations where much of the world is unknown. Moreover, the ad-hoc time and interval allocation scheme usually imposed on the trajectory also leads to conservative and slower trajectories. This work proposes FASTER (Fast and Safe Trajectory Planner) to ensure safety without sacrificing speed. FASTER obtains high-speed trajectories by enabling the local planner to optimize in both the free-known and unknown spaces. Safety is ensured by always having a safe back-up trajectory in the free-known space. The MIQP formulation proposed also allows the solver to choose the trajectory interval allocation. FASTER is tested extensively in simulation and in real hardware, showing flights in unknown cluttered environments with velocities up to 7.8m/s, and experiments at the maximum speed of a skid-steer ground robot (2m/s).

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite its numerous applications, high-speed UAV navigation through unknown environments is still an open problem. The desired high speeds together with partial observability of the environment and limits on payload weight make this task especially challenging for aerial robots. Safe operation, in addition to flying fast, is also critical but difficult to guarantee since the vehicle must repeatedly generate collision-free, dynamically feasible trajectories in real-time with limited sensing. Similar to the model predictive control literature, safety is guaranteed by ensuring a feasible solution exists indefinitely.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

If we consider ${\mathbb{R}}^{3} = {\mathcal{F} \cup \mathcal{O} \cup \mathcal{U}}$ where $\mathcal{F}$, $\mathcal{O}$, $\mathcal{U}$ are disjoint sets denoting free-known, occupied-known, and unknown space respectively, the following hierarchical planning architecture is commonly used: a global planner first finds the shortest piece-wise linear path from the UAV to the goal, avoiding the known obstacles $\mathcal{O}$. Then, a local planner finds a dynamically feasible trajectory in the direction given by this global plan. This local planner should find a fast and Safe Trajectory that leads the UAV to the goal. These two requirements of safety and speed represent the following tradeoff: on one hand, safety argues for short trajectories completely contained in $\mathcal{F}$ and end points not necessarily near the global plan.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

As a final stop condition is needed to guarantee safety, short trajectories are generally much slower than long trajectories because the braking maneuver propagates backwards from the end to the initial state of the trajectory. On the other hand, speed argues for longer planned trajectories (usually extending farther than $\mathcal{F}$) and end points near the global plan.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The typical way to solve the speed versus safety tradeoff is to ensure safety by planning only in $\mathcal{F}$, and then impose a final stop condition near the global plan. This can be achieved by either generating motion primitives that do not intersect $\mathcal{O} \cup \mathcal{U}$, or by constructing a convex representation of $\mathcal{F}$ to be used in an optimization. The main limitation of these works is that safety is guaranteed at the expense of higher speeds, especially in scenarios where $\mathcal{F}$ is small compared to $\mathcal{O} \cup \mathcal{U}$. This article presents an optimization-based approach that solves this limitation by solving for two optimal trajectories at every planning step (see Fig. 1): The first trajectory is in $\mathcal{U} \cup \mathcal{F}$ and ensures a long planning horizon with an end point on the global plan. The second trajectory is in $\mathcal{F}$, starts from a point along the first trajectory, and it may deviate from the global plan.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Only a portion of the first trajectory is actually implemented by the UAV (therefore satisfying the speed requirement), while the second trajectory guarantees safety, since it is contained in $\mathcal{F}$ and available at the start of every replanning step. This second trajectory is only implemented if the optimization problem becomes infeasible in the next replanning steps.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A second limitation, specially for the optimization-based approaches that use convex decomposition, is the choice of the interval and time allocation method. The interval allocation decides in which polyhedron each interval of the trajectory will be located, whereas the time allocation deals with the time spent on each interval (see Fig. 2). In order to simplify the interval allocation, a common choice is to set the number of intervals to be the same as the number of polyhedra found, forcing each interval to be in one specific polyhedron. This forces the optimizer to select the end points of each trajectory segment within the overlapping area of two consecutive polyhedra, and therefore possibly leading to more conservative or longer trajectories. Moreover, since a different time for each interval has to be found, the time allocation calculation is harder, leading to higher replanning times when using optimization techniques to allocate this time, and to nonsmooth or infeasible trajectories when imposing an ad-hoc time allocation. To overcome this limitation, FASTER allows the solver to decide the interval allocation by using a number of intervals greater than the number of polyhedra found and by allocating the same time for all the intervals.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

This time allocation method is efficiently found through a line search algorithm initialized with the solution at the previous replanning iteration.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The planning framework proposed is called FASTER - FAst and Safe Trajectory PlannER, and is an extension of our two published conference papers.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

A framework that ensures feasibility of the entire collision avoidance algorithm and guarantees safety without reducing the nominal flight speed by allowing the local planner to plan in $\mathcal{F} \cup \mathcal{U}$ while always having a Safe Trajectory in $\mathcal{F}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reduced conservatism of the time and interval allocation compared to prior ad-hoc approaches by efficiently finding the time allocated from the result of the previous replanning iteration and then allowing the optimizer to choose the interval allocation.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Extension of our previous work by proposing a way to compute very cheaply a heuristic of the cost-to-go needed by the local planner to decide which direction is the best one to optimize toward.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Simulation and hardware experiments showing agile flights in completely unknown cluttered environments, with velocities up to $7.8$ m/s, two times faster than previous state-of-the-art methods. FASTER is also tested on a skid-steer robot, showing hardware experiments at the top speed of the robot ($2$ m/s).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Theoretical analysis: Feasibility theorem that guarantees safety for FASTER.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Simulation: Cluttered office simulation, which presents a major challenge in terms of both clutterness for obstacle avoidance and limited visibility.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

Hardware: Duplication of the flight volume, achieving velocities up to $7.8$ m/s.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, we also perform a deeper analysis of the role of the Safe Trajectory in terms of safety and speed, a comparison of the performance of the interval allocation vs. the time allocation, and a comparison between the flight corridors associated with the safe and whole trajectories.

<!-- chunk {"id": "body-0019", "role": "body", "section": "FASTER", "weight": 1.0} -->

The notation used throughout this article is shown in Fig. 4: $\mathcal{M}$ is a sliding map centered on $L$, the current position of the UAV. $\mathcal{F}$ and $\mathcal{O}$ will denote the free-known and occupied-known spaces respectively. Similarly, $\mathcal{F}_{\text{Unknown}}$ and $\mathcal{O}_{\text{Unknown}}$ will denote the free-unknown and occupied-unknown spaces, respectively.

<!-- chunk {"id": "body-0020", "role": "body", "section": "FASTER", "weight": 1.0} -->

The total unknown space, denoted as $\mathcal{U}$, is therefore $\mathcal{U} = {\mathcal{F}_{\text{Unknown}} \cup \mathcal{O}_{\text{Unknown}}}$, and $\mathcal{F}$ and $\mathcal{O}$ are completely contained inside the map (${\mathcal{F} \cup \mathcal{O}} \subseteq \mathcal{M}$), and all the space outside the map is inside $\mathcal{U}$ (${{\mathbb{R}}^{3} \smallsetminus \mathcal{M}} \subseteq \mathcal{U}$). Note also that FASTER is completely in 3-D, but some illustrations are in 2-D for visualization purposes.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Mapping", "weight": 1.0} -->

A body-centered sliding map $\mathcal{M}$ (in the form of an occupancy grid map) is used in this work. A rolling map is desirable since it reduces the influence of the drift in the estimation error. We fuse a depth map into the occupancy grid using the 3-D Bresenham's line algorithm for ray-tracing. Both $\mathcal{O}$ and $\mathcal{U}$ are inflated by the radius of the UAV to ensure safety.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Global Planner", "weight": 1.0} -->

In the proposed framework, Jump Point Search (JPS) is used as a global planner to find the shortest piece-wise linear path from the current position to the goal. JPS was chosen instead of A\* because it runs an order of magnitude faster, while still guaranteeing completeness and optimality. The only assumption of JPS is a uniform grid, which holds in our case.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-C Convex Decomposition", "weight": 1.0} -->

A convex decomposition is done around part of the piece-wise linear path obtained by JPS. To do this convex decomposition, we rely on the approach proposed: A polyhedron is found around each segment of the piece-wise linear path by first inflating an ellipsoid aligned with the segment, and then computing the tangent planes at the points of the ellipsoid that are in contact with the obstacles. The reader is referred to for a detailed explanation. Given a piece-wise linear path with $P$ segments, we will denote the sequence of $P$ overlapping polyhedra as ${{{\{{({\mathbf{A}}_{p},{\mathbf{c}}_{p})}\}},p} = 0}:{P - 1}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-D Local Planner", "weight": 1.0} -->

For the local planner, we distinguish these three different jerk-controlled trajectories (see Fig.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-D Local Planner", "weight": 1.0} -->

Whole Trajectory: This trajectory goes from $A$ to $E$, and it is contained in $\mathcal{F} \cup \mathcal{U}$. It has a final stop condition.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-D Local Planner", "weight": 1.0} -->

Safe Trajectory: It goes from $R$ to $F$, where $R$ is a point in the Whole Trajectory, and $F$ is any point inside the polyhedra obtained by doing a convex decomposition of $\mathcal{F}$. It is completely contained in $\mathcal{F}$, and it also has a final stop condition to guarantee safety.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-D Local Planner", "weight": 1.0} -->

Committed Trajectory: This trajectory consists of two pieces: The first part is the interval $A\rightarrow R$ of the Whole Trajectory. The second part is the Safe Trajectory. It will be shown later that this trajectory is also guaranteed to be inside $\mathcal{F}$. This trajectory is the one that the UAV will keep executing in case no feasible solutions are found in the next replanning steps.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-D Local Planner", "weight": 1.0} -->

In the optimization problem solved by the local planner, the trajectory is divided in $N$ intervals (see Fig. 6). Let ${n = 0}:{N - 1}$ denote the specific interval of the trajectory, ${p = 0}:{P - 1}$ the specific polyhedron and $dt$ the time allocated per interval (same for every interval $n$). If ${\mathbf{j}}{(t)}$ is constrained to be constant in each interval ${n = 0}:{N - 1}$, then the Whole Trajectory will be a spline consisting of third-degree polynomials. Matching the cubic form of the position for each interval

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-D Local Planner", "weight": 1.0} -->

with the expression of a cubic Bézier curve

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-D Local Planner", "weight": 1.0} -->

Let us introduce the binary variables $b_{np}$, with ${p = 0}:{P - 1}$ and ${n = 0}:{N - 1}$ ($P$ variables for each interval ${n = 0}:{N - 1}$). As a Bézier curve is contained in the convex hull of its control points, we can ensure that the trajectory will be completely contained in this convex corridor by forcing that all the control points of an interval $n$ are in the same polyhedron with the constraint $\lbrack{b_{np} = 1\Longrightarrow{\mathbf{r}}_{nj} \in {{\text{polyhedron~}p}{\forall j}}}\rbrack$, and at least in one polyhedron with the constraint ${\sum_{p = 0}^{P - 1}b_{np}} \geq 1$. With this formulation, the optimizer is free to choose the specific interval allocation (i.e., which interval is inside which polyhedron).

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-D Local Planner", "weight": 1.0} -->

This problem is solved using Gurobi. The decision variables of this optimization problem are the binary variables $b_{np}$ and the jerk along the trajectory ${\mathbf{j}}_{n}$. $\mathbf{x}_{\text{init}}$ and $\mathbf{x}_{\text{final}}$ denote the initial and final states of the trajectory, respectively.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-D Local Planner", "weight": 1.0} -->

$f \geq 1$ is a factor that is obtained according to the solution of the previous replanning step (see Fig. 7): Denoting $f_{\text{worked},{k - 1}}$ as the factor that made the optimization feasible in the replanning step $k - 1$, in the replanning step $k$ the optimizer will try values of $f$ (in increasing order) in the interval $\lbrack{f_{\text{worked},{k - 1}} - \gamma},{f_{\text{worked},{k - 1}} + \gamma^{\prime}}\rbrack$ until the problem converges. Here, $\gamma$ and $\gamma^{\prime}$ are constant values chosen by the user. Note that, if $f = 1$, then $dt$ is a lower bound on the minimum time per interval required for the problem to be feasible. Therefore, only factors $f \geq 1$ are tried.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-D Local Planner", "weight": 1.0} -->

This approach is essentially a line search for the time allocation, with the goal of trying to obtain the smallest $dt$ that makes the optimization feasible (leading therefore to faster trajectories), but at the same time trying to minimize the number of trials with different $dt$ needed until convergence.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-D Local Planner", "weight": 1.0} -->

$\text{JPS}_{k}\leftarrow{\underset{\{\text{JPS}_{a},\text{JPS}_{b}\}}{\text{argmin}}\left\{ J_{a},J_{b} \right\}}$ 23 JPSin← Part of JPSk inside 𝒮 24 PolyWhole← Convex Decomposition in 𝒰 ∪ ℱ using JPSin 25 fWhole ← [fWhole, k − 1 − γ,fWhole, k − 1 + γ′] 26 Whole← MIQP in PolyWhole from A to E using fWhole 28 R← Nearest state to H along Whole that is not in inevitable collision with 𝒰 29 JPSin,known← Part of JPSin in ℱ 30 PolySafe←Convex Decomposition in ℱ using JPSin,known 31 fSafe ← [fSafe, k − 1 − γ,fSafe, k − 1 + γ′] 32 Safe ← MIQP in PolySafe from R to F using fSafe 34 Committedk ← WholeA → R ∪ Safe 35 fWhole, k← Factor that

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-D Local Planner", "weight": 1.0} -->

worked for Whole 36 fSafe, k← Factor that worked for Safe 37 Δ tk← Total replanning time

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-E Complete Algorithm", "weight": 1.0} -->

Algorithm 1 gives the full approach (see also Figs. 8 and 9). Let $L$ be the current position of the UAV. The point $A$ is chosen in the Committed Trajectory of the previous replanning step with an offset $\deltat$ from $L$. This offset $\deltat$ is computed by multiplying the total time of the previous replanning step by $\alpha \geq 1$ (typically $\alpha \approx 1.25$). The idea here is to dynamically change this offset to ensure that most of the time the solver can find the next solution in less than $\deltat$. Then, the final goal $G_{\text{term}}$ is projected into the sliding map $\mathcal{M}$ (centered on the UAV) in the direction $\overset{\rightarrow}{G_{\text{term}}A}$ to obtain the point $G$ (line 1). Next, we run JPS from $A$ to $G$ (line 1) to obtain $\text{JPS}_{a}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-E Complete Algorithm", "weight": 1.0} -->

The local planner then has to decide which direction is the best one to optimize toward (lines 1-1). Instead of blindly trusting the last JPS solution ($\text{JPS}_{a}$) as the best direction for the local planner to optimize (note that JPS is a zero-order model, without dynamics encoded), we take into account the dynamics of the UAV in the following way: First of all, we modify the $\text{JPS}_{k - 1}$ so that it does not collide with the new obstacles seen (Fig. 10): we find the points $I_{1}$ and $I_{2}$ (first and last intersections of $\text{JPS}_{k - 1}$ with $\mathcal{O}$) and run JPS three times, so $A\rightarrow I_{1}$, $I_{1}\rightarrow I_{2}$ and $I_{2}\rightarrow G$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-E Complete Algorithm", "weight": 1.0} -->

Hence, the modified version, denoted by $\text{JPS}_{b}$, will be the concatenation of these three paths. Note that by using $A\rightarrow I_{1}$, $I_{1}\rightarrow I_{2}$, and $I_{2}\rightarrow G$, we are forcing the combined path to pass through the points $A$, $I_{1}$, $I_{2}$, and $G$ (all of which belonged to $\text{JPS}_{k - 1}$), and therefore this gives a close approximation to $\text{JPS}_{k - 1}$, while avoiding $\mathcal{O}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-E Complete Algorithm", "weight": 1.0} -->

Then, we compute a lower bound on $dt$ using Eq. 7 for both $A\rightarrow C$ and $A\rightarrow D$, where $C$ and $D$ are the intersections of the previous JPS paths with a sphere $\mathcal{S}$ of radius $r$ centered on $A$, where $r$ is specified by the user. Next, we find the cost-to-go associated with each direction by adding this $dt_{a}$ (or $dt_{b}$) and the time it would take the UAV to go from $C$ (or $D$) to $G$ following the JPS solution flying at $v_{\text{max}}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-E Complete Algorithm", "weight": 1.0} -->

Finally, the one with lowest cost is chosen, so $\text{JPS}_{k}\leftarrow{\underset{\{\text{JPS}_{a},\text{JPS}_{b}\}}{\text{argmin}}{\{ J_{a},J_{b}\}}}$, which is then the direction toward which the local planner optimizes. To save computation time, this decision between $\text{JPS}_{a}$ and $\text{JPS}_{b}$ is made only if the angle $\angleCAD$ exceeds a certain threshold $\alpha_{0}$ (typically $15^{\circ}$). Note that $\angleCAD$ gives a measure of how much the JPS solution has changed with respect to the iteration $k - 1$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-E Complete Algorithm", "weight": 1.0} -->

A small angle indicates that $\text{JPS}_{a}$ and $\text{JPS}_{k - 1}$ are very similar (at least within the sphere $\mathcal{S}$), and that therefore the direction of the local plan will not differ much from the iteration $k - 1$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-E Complete Algorithm", "weight": 1.0} -->

The Whole Trajectory (lines 1-1) is obtained as follows. We do the convex decomposition of $\mathcal{U} \cup \mathcal{F}$ around the part of $\text{JPS}_{k}$ that is inside the sphere $\mathcal{S}$, which we denote as $\text{JPS}_{\text{in}}$. This gives a series of overlapping polyhedra that we denote as $\text{Poly}_{\text{Whole}}$. Then, the MIQP in is solved using these polyhedral constraints to obtain the Whole Trajectory.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-E Complete Algorithm", "weight": 1.0} -->

The Safe Trajectory is computed as in lines 1-1. First, we compute the point $H$ as the intersection between the Whole Trajectory and $\mathcal{U}$. Then, we have to choose the point $R$ along the Whole Trajectory as the start of the Safe Trajectory. To do this, note that, on one hand, $R$ should be chosen as far as possible from $A$, so that $\deltat$ can be chosen larger in the next replanning step, which helps to guarantee that $A$ is not chosen on the Safe Trajectory (where the braking maneuver happens). On the other hand, however, a point $R$ too close to $H$ may lead to an infeasible problem for the Safe Trajectory optimizer. We propose two ways to compute $R$: The first one is to choose it with an offset $\deltat^{\prime}$ from $A$, where $\deltat^{\prime}$ is computed by multiplying the previous replanning time by $\beta \geq 1$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-E Complete Algorithm", "weight": 1.0} -->

The second (and better) way to solve this tradeoff is the following one: we can choose $R$ as the nearest state to $H$ (in the segment $A\rightarrow H$ of the Whole Trajectory) that is not in inevitable collision with $\mathcal{U}$. To compute an approximation of this state in a very efficient way, we choose $R$ as the last point (going from $A$ to $H$ along the Whole Trajectory) that satisfies

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-E Complete Algorithm", "weight": 1.0} -->

where ${\mathbf{v}}_{R,j}$, ${\mathbf{x}}_{R,j}$ and ${\mathbf{x}}_{H,j}$ are, respectively, the velocity of $R$, the position of $R$, and the position of $H$ in the axes $j = {\{ x,y\}}$. Here, we have approximated the system as a double integrator model in each axis and, hence, $\frac{{\mathbf{v}}_{R,j}^{2}}{2\left| a_{\text{max}} \right|}$ is the minimum stopping distance. Due to these two approximations (double integrator and decoupling in axes $x$ and $y$), this heuristic may be conservative. We ignore the axis $z$ in this computation to reduce the conservativeness of this heuristic.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-E Complete Algorithm", "weight": 1.0} -->

Note that even if this heuristic leads to a choice of $R$ for which no feasible collision-free (with $\mathcal{U} \cup \mathcal{O}$) trajectory exists, the optimizer will not find a solution in that replanning step and, therefore, will continue executing the solution of the previous replanning step.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-E Complete Algorithm", "weight": 1.0} -->

After choosing the point $R$, we do the convex decomposition of $\mathcal{F}$ using the part of $\text{JPS}_{\text{in}}$ that is in $\mathcal{F}$, obtaining the polyhedra $\text{Poly}_{\text{Safe}}$. Then, we solve the MIQP from $R$ to any point $F$ inside $\text{Poly}_{\text{Safe}}$ (this point $F$ is chosen by the optimizer).

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-E Complete Algorithm", "weight": 1.0} -->

In both of the convex decompositions presented earlier, one polyhedron is created for each segment of the piecewise linear paths. To obtain a less conservative solution (i.e. larger polyhedra), we first check the length of segments of the JPS path, creating more vertexes if this length exceeds a certain threshold $l_{\text{max}}$. Moreover, we truncate the number of segments in the path to ensure that the number of polyhedra found does not exceed a threshold $P_{\text{max}}$. This helps reduce the computation times (see Sec. IV).

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-E Complete Algorithm", "weight": 1.0} -->

Finally (line 1), we compute the Committed Trajectory by concatenating the piece $A\rightarrow R$ of the Whole Trajectory, and the Safe Trajectory. Note that in this algorithm we have run two decoupled optimization problems per replanning step: 1) one for the Whole Trajectory, and 2) one for the Safe Trajectory. This ensures that the piece $A\rightarrow R$ is not influenced by the braking maneuver $R\rightarrow F$, and therefore, it guarantees a higher nominal speed on this first piece. The intervals $L\rightarrow A$ and $A\rightarrow R$ have been designed so that at least one replanning step can be solved within that interval.

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-E Complete Algorithm", "weight": 1.0} -->

Scenario 1: Either of the two optimizations is infeasible.

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-E Complete Algorithm", "weight": 1.0} -->

Scenario 2: The piece $A - R$ intersects $\mathcal{U}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-E Complete Algorithm", "weight": 1.0} -->

Scenario 3: The replanning takes longer than $\deltat$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "III-E Complete Algorithm", "weight": 1.0} -->

4 V← First element of JPSk
5 N← Find nearest neighbour of V in 𝒰
9 𝒮← Sphere of radius r centered on V
12 Remove from JPSk the vertexes inside 𝒮
13 Insert M at the front of JPSk
Algorithm 2 FIND INTERSECTION

<!-- chunk {"id": "body-0054", "role": "body", "section": "III-E Complete Algorithm", "weight": 1.0} -->

In Alg. 1, it is required to compute the intersection between a piece-wise linear path (the solution of JPS) and a voxel grid ($\mathcal{U}$ or $\mathcal{O}$) to obtain the points $I_{1}$, $I_{2}$ or $M$. To do this in an efficient way, we use Alg. 2, depicted in Fig. 11. We first find the nearest neighbor $N$ from the beginning of the piece-wise linear path $A$ (line 2), and compute the intersection $M$ between the path and a sphere $\mathcal{S}$ centered on $A$ with radius equal to the distance between $A$ and $N$ (line 2). As it is guaranteed that all the points of the path that are inside $\mathcal{S}$ do not intersect with the voxel grid, we can repeat the same procedure again, but this time starting from $M$. This process continues until the distance to the nearest neighbor is below some threshold $\epsilon > 0$ (lines 2--2). Note that, instead of Alg.

<!-- chunk {"id": "body-0055", "role": "body", "section": "III-E Complete Algorithm", "weight": 1.0} -->

2, another option would be to represent $\mathcal{F}$ as a voxel grid, and then use standard ray-tracing (such as the 3-D Bresenham's line Algorithm ) for each of the segments of the piece-wise linear path. However, this might be very computationally expensive for grids $\mathcal{F}$ with small voxel sizes.

<!-- chunk {"id": "body-0056", "role": "body", "section": "III-F Feasibility Theorem", "weight": 1.0} -->

We can now state the following feasibility theorem for FASTER, which guarantees that all the Committed Trajectories are completely contained inside free space (known or unknown), and that, therefore, safety is guaranteed. Here, $k$ denotes the replanning step.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The theorem does not assume that $\mathcal{F}_{k} \subseteq \mathcal{F}_{k + 1}$. In other words, it does not assume that the size of the free-known space always increases: $\mathcal{F}_{k} \subseteq \mathcal{F}_{k + 1}$ is not necessarily true due to the sliding map. Note, however, that the proof does not depend on the shape of the map nor on the length of the history kept in this map.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Remark 1", "weight": 1.0} -->

a map $\mathcal{M} \equiv \text{FOV}$ (Field of View of the sensor), obtained uniquely by considering the instantaneous sensing data and, therefore, not keeping history in the map.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Remark 2", "weight": 1.0} -->

By allowing the algorithm to choose $\text{Committed}_{k + 1} = \text{Committed}_{k}$ (which occurs when one of the scenarios 1, 2, or 3 happen), in iteration $k + 1$ the UAV may commit to a trajectory that has some parts outside the map $\mathcal{M}_{k + 1}$. As proven above, it is still guaranteed that $\text{Committed}_{k + 1} \subseteq {\mathcal{F}_{k + 1} \cup \mathcal{F}_{\text{Unknown},{k + 1}}}$. This constitutes a form of data compression, where the information of a part of the world being free (which was obtained in iteration $k$ or before) is embedded in the trajectory itself and not directly in the map $\mathcal{M}_{k + 1}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "III-G Controller", "weight": 1.0} -->

To track the trajectory obtained by FASTER, we used the cascade controller presented. The yaw of the UAV is chosen such that the camera of the UAV points to $M$ (intersection between $\text{JPS}_{k}$ and $\mathcal{U}$, see Fig. 8). This controller is used in all the UAV simulation and hardware experiments of this article. In the real hardware experiments, position, velocity, attitude, and IMU biases are estimated by fusing propagated IMU measurements with an external motion capture system.

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-A Forest, bugtrap and office simulations", "weight": 1.0} -->

We evaluate the performance of the proposed algorithm in different simulated scenarios. The simulator uses C++ custom code for the dynamics engine, integrating the nonlinear differential equations of the UAV using the Runge-Kutta method. Gazebo is used to simulate perception data in the form of a depth map. In all these simulations, the depth camera has a horizontal FOV of $90^{\circ}$. The sensing range is $5$ m for the first simulation (corner environment), and $10$ m for the rest.

<!-- chunk {"id": "body-0062", "role": "body", "section": "IV-A Forest, bugtrap and office simulations", "weight": 1.0} -->

We now test FASTER in 10 random forest environments with an obstacle density of $0.1$ obstacles/m^2^ (see Fig.

<!-- chunk {"id": "body-0063", "role": "body", "section": "IV-A Forest, bugtrap and office simulations", "weight": 1.0} -->

Optimistic RRT^⋆^ (unknown space = free).

<!-- chunk {"id": "body-0064", "role": "body", "section": "IV-A Forest, bugtrap and office simulations", "weight": 1.0} -->

Conservative RRT^⋆^ (unknown space = occupied).

<!-- chunk {"id": "body-0065", "role": "body", "section": "IV-A Forest, bugtrap and office simulations", "weight": 1.0} -->

The first six methods are described in and is our previous algorithm. The results in Table II highlight that FASTER achieves a $8 - {51\%}$ improvement in the total distance flown. Completion times are compared in Table II to (time values are not available for all other algorithms in Table II). FASTER achieves an improvement of $52\%$ in the completion time. The dynamic constraints imposed for the results of this table are (per axis) $v_{\text{max}} = 5$ m/s, $a_{\text{max}} = 5$ m/s^2^, and $j_{\text{max}} = 8$ m/s^3^. The velocity profiles obtained for one random forest simulation are shown in Fig. 13.

<!-- chunk {"id": "body-0066", "role": "body", "section": "IV-A Forest, bugtrap and office simulations", "weight": 1.0} -->

We also test FASTER using the bugtrap environment shown in Fig. 12, and obtain the results that appear on Table III. Both algorithms have a similar total distance, but FASTER achieves an improvement of $63\%$ on the total flight time. For both cases, the dynamic constraints imposed are $v_{\text{max}} = 10$ m/s, $a_{\text{max}} = 10$ m/s^2^, and $j_{\text{max}} = 40$ m/s^3^. The velocity profile achieved along the trajectory can be seen in Fig. 14.

<!-- chunk {"id": "body-0067", "role": "body", "section": "IV-A Forest, bugtrap and office simulations", "weight": 1.0} -->

Finally, we test FASTER in an office environment, obtaining the velocity profile shown in Fig 15 and the distances and flight times shown in Table IV. In this case, the distance flown by FASTER was slightly longer than the one by (note that FASTER entered one of the last rooms, and then turned back), but even with this extra distance, it achieved a $29.6\%$ improvement on the flight time. The dynamic constraints used for the office simulation are $v_{\text{max}} = 3$ m/s, $a_{\text{max}} = 6$ m/s^2^ and $j_{\text{max}} = 35$ m/s^3^.

<!-- chunk {"id": "body-0068", "role": "body", "section": "IV-A Forest, bugtrap and office simulations", "weight": 1.0} -->

The timing breakdown of Alg. 1 as a function of the maximum number of polyhedra $P_{\text{max}}$ is shown in Fig. 17. The number of intervals $N$ was 10 for the Whole Trajectory and 7 for the Safe Trajectory. Note that the runtime for the MIQP of the Safe Trajectory is approximately constant as a function of $P_{\text{max}}$ because the Safe Trajectory is planned only in $\mathcal{F}$, and therefore, most of the time, $P < P_{\text{max}}$. For the simulation and hardware experiments presented here, $P_{\text{max}} = {2 - 4}$ was used. Fig. 17 shows the runtimes for JPS as a function of the voxel size of the map, which are always $< 10$ ms for voxel sizes $\geq 14$ cm. All these timing breakdowns were measured using an Intel Core i7-7700HQ 2.8GHz Processor.

<!-- chunk {"id": "body-0069", "role": "body", "section": "IV-B Time vs. Interval allocation", "weight": 1.0} -->

As explained in Sec. III, FASTER optimizes the interval allocation using binary variables, while fixing in each optimization the time allocated per interval. Another possible option would be to optimize the time allocation, while fixing the interval allocation.

<!-- chunk {"id": "body-0070", "role": "body", "section": "IV-B Time vs. Interval allocation", "weight": 1.0} -->

TA: Time Allocation is optimized and there are $N/P$ intervals per polyhedron. We test both the case when the total time of the trajectory $T$ is free and when it is fixed at $12.5$ s.

<!-- chunk {"id": "body-0071", "role": "body", "section": "IV-B Time vs. Interval allocation", "weight": 1.0} -->

IA (ours): Interval Allocation is optimized and all the intervals have the same fixed allocated time. IA uses binary variables to optimize the allocation of the $N$ intervals. $T$ is fixed at $12.5$ s and the time allocated per interval is $12.5/N$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "IV-B Time vs. Interval allocation", "weight": 1.0} -->

We use an environment whose free space is defined by 4 overlapping polyhedra (i.e., $P = 4$, see Fig. 18). The final state is a stop condition in the centroid of the last polyhedron, while the initial state is a stop condition in a random position of the first polyhedron, for a total of 50 runs. Both IA and TA methods use a weighted sum of the control effort and the total time as the total cost: ${\sum_{n = 0}^{N - 1}{\left\| \mathbf{j}_{n} \right\|^{2}dt}} + {\rhoT}$, where $\rho = 0.2$ m^2^/s^6^. Note that the second term of this cost is constant for the methods in which $T$ is not a decision variable. The dynamic constraints imposed are $v_{\text{max}} = 2$ m/s, $a_{\text{max}} = 20$ m/s^2^, and $j_{\text{max}} = 50$ m/s^3^.

<!-- chunk {"id": "body-0073", "role": "body", "section": "IV-B Time vs. Interval allocation", "weight": 1.0} -->

The solver used for the (nonconvex) problems of TA is *fmincon*, while *Gurobi* is used for the MIQP of IA (both interfaced through *YALMIP* ). The results in Fig. 18 show that IA is able to succeed in all of the runs, and it obtains smaller total costs and computation times. The TA methods achieve lower success rates, though these tend to increase when $T$ is not fixed and $N > P$. All these results support the choice of optimizing the interval allocation (instead of the time allocation) that FASTER makes. Note also that, as explained in Sec. III-D, FASTER runs on top of this a line search to choose the time allocated per interval, see Fig. 7.

<!-- chunk {"id": "body-0074", "role": "body", "section": "IV-C1 Speed achieved", "weight": 1.0} -->

We first test FASTER in a simple environment and, for the same replanning step, we compare the velocities of the trajectory found by FASTER (that plans in $\mathcal{U} \cup \mathcal{F}$) with the ones of the trajectory found by a planner that plans only in $\mathcal{F}$. The environment is shown in Fig. 19, and consists of a corner, with the goal on the other side of the wall, so that the UAV has to turn the corner. The initial velocity at $A$ is $4.8$ m/s, and the dynamic constraints imposed are $v_{\text{max}} = 6.5$ m/s, $a_{\text{max}} = 6$ m/s^2^, and $j_{\text{max}} = 20$ m/s^3^.

<!-- chunk {"id": "body-0075", "role": "body", "section": "IV-C1 Speed achieved", "weight": 1.0} -->

FASTER achieves a velocity of $6.02$ m/s in the segment $A\rightarrow R$ (segment that will actually be flown by the UAV), while planning only in $\mathcal{F}$ achieves a velocity of $5.06$ m/s. $R\rightarrow F$ is the Safe Trajectory, and $A\rightarrow R\rightarrow F$ is the Committed Trajectory. Safety is guaranteed by both planners.

<!-- chunk {"id": "body-0076", "role": "body", "section": "IV-C2 Safety", "weight": 1.0} -->

We now evaluate what happens if the UAV does not compute the Safe Trajectory, but instead commits directly to the Whole Trajectory. We test this in the environment shown in Fig. 20, which consists of a corner with one obstacle behind it. This environment is especially challenging due to the presence of obstacles just behind the corner, which are not fully visible to the UAV until it turns the corner. The results in Table V show that the Safe Trajectory is not strictly necessary when flying at low speeds ($\leq 4$ m/s), but it is crucial to guarantee safety when flying at high speeds ($\geq 6$ m/s). For high speeds, the planner without the Safe Trajectory collides due to the lack of time to replan when suddenly discovering an obstacle that was in the unknown space.

<!-- chunk {"id": "body-0077", "role": "body", "section": "IV-D Comparison between $\\text{Poly}_{\\text{Whole}}$ and $\\text{Poly}_{\\text{Safe}}$", "weight": 1.0} -->

For the corner environment explained in Sec. IV-C (which uses 4 polyhedra), the top view and the quantitative comparison of the volumes covered are shown in Fig. 21. $\text{Poly}_{\text{Whole}}$ covers $145.1 \cdot V_{\text{UAV}}$ of unknown space that extends beyond $\text{Poly}_{\text{Safe}}$. Here, $V_{\text{UAV}}$ is the volume of the drone (a sphere of radius 0.3 m).

<!-- chunk {"id": "body-0078", "role": "body", "section": "IV-D Comparison between $\\text{Poly}_{\\text{Whole}}$ and $\\text{Poly}_{\\text{Safe}}$", "weight": 1.0} -->

For the forest and office simulations (which use 2 polyhedra), the comparison of the volumes is shown in Fig. 22 and Table VI. Letting $V_{\text{UAV}}$ denote the volume of the sphere that models the UAV, these results show that, on average, $\text{Poly}_{\text{Whole}}$ is, respectively, $250.8 \cdot V_{\text{UAV}}$ and $21.9 \cdot V_{\text{UAV}}$ larger than $\text{Poly}_{\text{Safe}}$ in the office and forest simulations. Moreover, $\text{Poly}_{\text{Safe}}$ does not cover unknown space, while $\text{Poly}_{\text{Whole}}$ is able to cover, respectively, an unknown volume of $122.8 \cdot V_{\text{UAV}}$ and $5.5 \cdot V_{\text{UAV}}$ in the office and forest simulations.

<!-- chunk {"id": "body-0079", "role": "body", "section": "IV-D Comparison between $\\text{Poly}_{\\text{Whole}}$ and $\\text{Poly}_{\\text{Safe}}$", "weight": 1.0} -->

Note also that in the office simulation (which is more cluttered than the forest simulation), $\text{Poly}_{\text{Whole}}$ covers more unknown volume than in the forest simulation.

<!-- chunk {"id": "body-0080", "role": "body", "section": "IV-D Comparison between $\\text{Poly}_{\\text{Whole}}$ and $\\text{Poly}_{\\text{Safe}}$", "weight": 1.0} -->

The key conclusion of these results is that, even with a relatively small number of polyhedra (2-4), the volume of unknown space covered by $\text{Poly}_{\text{Whole}}$ can be hundreds of times the volume of the UAV, especially in cluttered environments. This makes $\text{Poly}_{\text{Whole}}$ extend much farther than $\text{Poly}_{\text{Safe}}$, which is restricted to stay in $\mathcal{F}$. Hence, the Whole Trajectory will benefit from a longer planning horizon, leading to a higher nominal speed in the segment $A\rightarrow R$ of the Whole Trajectory used in the Committed Trajectory.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Hardware results", "weight": 1.0} -->

The UAVs used in the hardware experiments are shown in Fig. 23. A quadrotor was used in the experiments 1-4, and a hexarotor was used in the experiments 5 and 6. In both UAVs, the perception runs on the Intel^®^ RealSense, the mapper and planner run on the Intel^®^ NUC, and the control runs on the Qualcomm^®^ SnapDragon Flight.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Hardware results", "weight": 1.0} -->

The six hardware experiments done are shown in Figs. 29-- 29. The corresponding velocity profiles are shown in Fig. 30. The maximum speed achieved was $7.8$ m/s, in Experiment 5 (Fig. 29). The first and second experiments (Fig. 29 and 29) were done in similar obstacle environments with the same starting point but with different goal locations. In the first experiment (Fig. 29), the UAV performs a 3-D agile maneuver to avoid the obstacles on the table. In the second experiment (Fig. 29) the UAV flies through the narrow gap of the cardboard boxes structure, and then flies below the triangle-shaped obstacle. In these two experiments, the maximum speed was $2.1$ m/s.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Hardware results", "weight": 1.0} -->

In the third and fourth experiments (Fig. 29 and 29), the UAV must fly through a space with poles of different heights, and finally below the cardboard boxes structure to reach the goal, achieving a maximum speed of $3.6$ m/s. Finally, in the fifth and sixth experiments (Fig. 29 and 29), the UAV is allowed to fly in a much bigger space, and has to avoid some poles and several cardboard boxes structures. In the fifth experiment (Fig. 29) the UAV achieved a top speed of $7.8$ m/s. In the sixth experiment (Fig. 29) the UAV was first commanded to go to a goal at the other side of the flight space, and then to come back to the starting position, achieving a top velocity of $4.6$ m/s.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Hardware results", "weight": 1.0} -->

Fig. 30 shows the estimated velocity of the UAV, obtained by applying finite differences to the ground truth position measurements of an external motion capture system. This leads to some noisy estimates, in particular for the high velocities of experiments 5 and 6. Moreover, these positions measurements are not available when the UAV is passing below an obstacle, which produces also noisy velocity estimates at those points. This happens in experiment 2 at $t = 4.0$ s and $t = 5.9$ s and in experiment 4 at $t = 5.0$ s.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Hardware results", "weight": 1.0} -->

For $P_{\text{max}} = 2$, the boxplots of the runtimes achieved on the forest simulation (measured on an Intel Core i7-7700HQ) and on the hardware experiments (measured on the onboard Intel NUC i7DNK with the mapper and the RealSense also running on it) are shown in Fig. 31. For the runtimes of the MIQP of the Whole and the Safe Trajectories, the 75^th^ percentile is always below $32$ ms.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Extension to a ground robot", "weight": 1.0} -->

We now show how, by generating 2-D trajectories instead of 3-D, and changing the controller, FASTER can also be extended for skid-steer robots. To track the trajectory obtained by MADER, we generate the linear and angular velocities using a PD controller based on the derivative of the tangential angle of the trajectory and the desired position and velocity. The commanded angular velocities of the wheels are then obtained from the desired angular velocities of the wheels using a PID.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Extension to a ground robot", "weight": 1.0} -->

Three different experiments were done with the ground robot (see Figs. 33, 33, and 34). An external motion capture system was used to estimate the position and orientation of the robot. Experiments 7 and 8 were done in obstacle environments similar to the random forest. The maximum speeds achieved for the experiments 7 and 8 were $1.95$ m/s and $2.22$ m/s respectively. Note that the maximum speed specified for this ground robot is $\approx 2$ m/s.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Extension to a ground robot", "weight": 1.0} -->

To test the ability of FASTER to reuse the map built, the setup for experiment 9 was a bugtrap environment, and only points in the depth image closer than 3 m were used to build the map. The robot first enters the bugtrap because it does not see the end of it. Once the robot detects that there is no exit at the end of the bugtrap, it turns back, exits the bugtrap, passes through its left and avoids some new obstacles to finally reach the goal. The maximum speed achieved in this experiment was $1.70$ m/s

<!-- chunk {"id": "body-0089", "role": "body", "section": "CONCLUSIONS AND FUTURE WORK", "weight": 1.0} -->

This work presented FASTER, a fast and safe planner for agile flights in unknown environments. The key properties of this planner is that it leads to a higher nominal speed than other works by planning both in $\mathcal{U}$ and $\mathcal{F}$ using a convex decomposition, and ensures safety by having always a Safe Trajectory planned in $\mathcal{F}$ at the beginning of every replanning step. FASTER was tested successfully both in simulated and in hardware flights, achieving velocities up to $7.8$ m/s. Finally, we showed how FASTER is also applicable to skid-steer robots, achieving hardware experiments at $2$ m/s.

<!-- chunk {"id": "body-0090", "role": "body", "section": "CONCLUSIONS AND FUTURE WORK", "weight": 1.0} -->

Our algorithm has also some limitations: In environments where the planning horizon is not very large (as in all the experiments shown in this article), $2 - 4$ polyhedra usually suffice, and our algorithm maintains computational tractability. However, for large known worlds (for example if a map of the environment already exists beforehand), a long planning horizon may require more than 4 polyhedra, which, as shown in Fig. 17, will increase the computation time. One possible way to address this is to solve the interval allocation only in the polyhedra that are close to the current position of the UAV, and force a predefined interval and time allocation for the polyhedra that are farther in the planning horizon. Moreover, we also noticed how important the choice of the point $R$ is: As discussed in Sec. III-E, if the point $R$ is chosen very close to the unknown space, it may lead to infeasibility of the optimization problem associated with the Safe Trajectory.

<!-- chunk {"id": "body-0091", "role": "body", "section": "CONCLUSIONS AND FUTURE WORK", "weight": 1.0} -->

However, if $R$ is chosen very close to $A$, then the UAV may not have enough time to replan in the next iteration, which will lead to keep executing the previous trajectory, and may eventually decrease the nominal speed of the flight. Nonheuristic ways to solve this tradeoff seems like a promising direction for future work. Further future work includes the relaxation of the assumption 1: we plan to include the uncertainty associated with the map (due to estimation error and/or sensor noise) in the replanning function, and to extend this planner to dynamic environments. We also plan to use onboard estimation algorithms like VIO instead of an external motion capture system for the real hardware experiments.

<!-- chunk {"id": "body-0092", "role": "body", "section": "CONCLUSIONS AND FUTURE WORK", "weight": 1.0} -->

Finally, another promising future work is the reduction of the computation times of the time allocation approaches. Experiments in Sec. IV-B use a generic nonconvex solver to optimize the time allocation, which may be inefficient in some situations. Exploitation of the structure of the time allocation problem and/or the use of hierarchical optimization could help to reduce the associated computation times. This could potentially avoid the use of binary variables needed for the interval allocation, or allow the optimization of *both* the interval and the time allocation in the trajectory planning problem.
