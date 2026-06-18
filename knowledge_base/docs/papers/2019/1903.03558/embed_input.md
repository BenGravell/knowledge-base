<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

FASTER: Fast and Safe Trajectory Planner for Flights in Unknown Environments

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

High-speed trajectory planning through unknown environments requires algorithmic techniques that enable fast reaction times while maintaining safety as new information about the operating environment is obtained. The requirement of computational tractability typically leads to optimization problems that do not include the obstacle constraints (collision checks are done on the solutions) or use a convex decomposition of the free space and then impose an ad-hoc time allocation scheme for each interval of the trajectory. Moreover, safety guarantees are usually obtained by having a local planner that plans a trajectory with a final "stop" condition in the free-known space. However, these two decisions typically lead to slow and conservative trajectories. We propose FASTER (Fast and Safe Trajectory Planner) to overcome these issues. FASTER obtains high-speed trajectories by enabling the local planner to optimize in both the free-known and unknown spaces. Safety guarantees are ensured by always having a feasible, safe back-up trajectory in the free-known space at the start of each replanning step. Furthermore, we present a Mixed Integer Quadratic Program formulation in which the solver can choose the trajectory interval allocation, and where a time allocation heuristic is computed efficiently using the result of the previous replanning iteration.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This proposed algorithm is tested extensively both in simulation and in real hardware, showing agile flights in unknown cluttered environments with velocities up to 3.6 m/s.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Navigating through unknown environments entails repeatedly generating collision-free, dynamically feasible trajectories that are executed over a finite horizon. Similar to that in the Model Predictive Control (MPC) literature, safety is guaranteed by ensuring a feasible solution exists indefinitely. If we consider ${\mathbb{R}}^{3} = {\mathcal{O} \cup \mathcal{F} \cup \mathcal{U}}$ where $\mathcal{F}$, $\mathcal{O}$, $\mathcal{U}$ are disjoint sets denoting free-known, occupied-known, and unknown space respectively, safety is guaranteed by constructing trajectories that are entirely contained in $\mathcal{F}$ with a final stop condition. This can be achieved by generating motion primitives that do not intersect $\mathcal{O} \cup \mathcal{U}$, or by constructing a convex representation of $\mathcal{F}$ to be used in an optimization.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

However, both approaches lead to slow trajectories in scenarios where $\mathcal{F}$ is small compared to $\mathcal{U} \cup \mathcal{O}$. This paper presents an optimization-based approach that reduces the aforementioned limitations by solving for two optimal trajectories at every planning step (see Fig. 1): one in $\mathcal{U} \cup \mathcal{F}$, and another one in $\mathcal{F}$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Decomposing the free space into $P$ overlapping polyhedra along a path connecting a start $A$ to goal $E$ location (see Fig. 1), the usual approach is to divide the total trajectory into $N = P$ intervals. On one hand, this simplifies the problem because no integer variables are needed, as each interval is forced to be in one specific polyhedron. On the other hand, the time allocation problem becomes much harder, as there are $N$ different $dt_{n}$ (time allocated for each interval $n$). The trajectory is also more conservative since the optimizer is only allowed to move the end points of each interval of the trajectory in the overlapping areas. To overcome these two problems, we propose the use of the same $dt$ for all the intervals, and use $N > P$ intervals, encoding the optimization problem as a Mixed Integer Quadratic Program (MIQP).

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Moreover, and as the minimum feasible $dt$ depends depends on the state of the UAV and on the specific shape of $\mathcal{F}$ and $\mathcal{U}$ at a specific replanning step, we also propose an efficient way to compute a heuristic of this $dt$ using the result obtained in the previous replanning iteration.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

A framework that ensures feasibility of the entire collision avoidance algorithm and guarantees safety without reducing the nominal flight speed by allowing the local planner to plan in $\mathcal{F} \cup \mathcal{U}$ while always having a safe trajectory in $\mathcal{F}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Reduced conservatism of the MIQP formulation for the interval and time allocation problem of the flight trajectories compared to prior work.

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Extension of our previous work, (where we considered the interaction between the global and local planners) by proposing a way to compute very cheaply a heuristic of the cost-to-go needed by the local planner to decide which direction is the best one to optimize towards.

<!-- chunk {"id": "body-0011", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Simulation and hardware experiments showing agile flights in completely unknown cluttered environments, with velocities up to $3.6$ m/s.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A Planning", "weight": 1.0} -->

The Fast and Safe Trajectory Planner (FASTER) uses hierarchical architecture where a long-horizon global planner guides a short-horizon local planner to a desired goal location. The global planner used in this work is Jump Point Search (JPS). JPS finds the shortest piecewise linear path between two points in a 3D uniformly-weighted voxel grid, guaranteeing optimality and completeness but running an order of magnitude faster than A\*,.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A Planning", "weight": 1.0} -->

For the local planner, we distinguish these three different jerk-controlled trajectories (some of the points will be precisely defined later, see Fig.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Planning", "weight": 1.0} -->

Whole Trajectory: This trajectory goes from a start location $A$ to goal location $E$, and it is contained in $\mathcal{F} \cup \mathcal{U}$. It has a final stop condition.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Planning", "weight": 1.0} -->

Safe Trajectory: It goes from $R$ to $F$, where $R$ is a point in the Whole Trajectory, and $F$ is any point inside the polyhedra obtained by doing a convex decomposition of $\mathcal{F}$. It is completely contained in $\mathcal{F}$ (free-known space), and it has also a final stop condition to guarantee safety.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Planning", "weight": 1.0} -->

Committed Trajectory: This trajectory consists of two pieces: The first part is the interval $A\rightarrow R$ of the Whole Trajectory. The second part is the Safe Trajectory. It is also guaranteed to be inside $\mathcal{F}$ (see explanation below). This trajectory is the one that the UAV will execute in case no feasible solutions are found in the next replanning steps.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Planning", "weight": 1.0} -->

Let ${n = 0}:{N - 1}$ denote the specific interval of the trajectory and ${p = 0}:{P - 1}$ the specific polyhedron. If ${\mathbf{j}}{(t)}$ is constrained to be constant in each interval ${n = 0}:{N - 1}$, then the whole trajectory will be a spline consisting of third degree polynomials. Matching the cubic form of the position for each interval

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Planning", "weight": 1.0} -->

with the expression of a cubic Bézier curve

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Planning", "weight": 1.0} -->

Let us denote the sequence of $P$ overlapping polyhedra as ${{{\{{({\mathbf{A}}_{p},{\mathbf{c}}_{p})}\}},p} = 0}:{P - 1}$, and introduce binary variables $b_{np}$ ($P$ variables for each interval ${n = 0}:{N - 1}$). As a Bézier curve is contained in the convex hull of its control points, we can ensure that the whole trajectory will be inside this convex corridor by forcing that all the control points are in the same polyhedron with the constraint $\lbrack{b_{np} = 1\Longrightarrow{\mathbf{r}}_{nj} \in {{\text{polyhedron~}p}{\forall j}}}\rbrack$, and at least in one polyhedron with the constraint ${\sum_{p = 0}^{P - 1}b_{np}} \geq 1$. The optimizer is free to choose in which polyhedron exactly.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Planning", "weight": 1.0} -->

In the optimization problem above, $dt$ (same for every interval $n$) is computed as

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Planning", "weight": 1.0} -->

where $T_{v_{i}}$, $T_{a_{i}}$, $T_{j_{i}}$ are solution of the constant-input motions in each axis $i = {x,y,z}$ by applying $v_{max}$, $a_{max}$ and $j_{max}$ respectively. $f \geq 1$ is a factor that is obtained according to the solution of the previous replanning step (see Fig. 2): The optimizer will try values of $f$ (in increasing order) in the interval $\lbrack{f_{{worked},{k - 1}} - \gamma},{f_{{worked},{k - 1}} + \gamma^{\prime}}\rbrack$ until the problem converges. Here, $f_{{worked},{k - 1}}$ is the factor that made the problem feasible in the previous replanning step.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Planning", "weight": 1.0} -->

Note that, if $f = 1$, then $dt$ is a lower bound on the minimum time per interval required for the problem to be feasible.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Planning", "weight": 1.0} -->

Data: Current Position of the UAV L, C o m m i t t e dk − 1, J P Sk − 1, Gt e r m, 𝒪, ℱ, 𝒰, r 6 Choose point A in C o m m i t t e dk − 1 with offset δ t from L 7 G← Projection of Gt e r m into map ℳ 11 J P Sb← Modified J P Sk − 1 such that J P Sk − 1 ∩ 𝒪 = ⌀ 15 $J_{a} = {{{N \cdot d}t_{a}} + \frac{\left\| {JPS_{a}\left( {C\rightarrow G} \right)} \right\|}{v_{max}}}$ 16 $J_{b} = {{{N \cdot d}t_{b}} + \frac{\left\| {JPS_{b}\left( {D\rightarrow G} \right)} \right\|}{v_{max}}}$ 17

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Planning", "weight": 1.0} -->

${JPS_{k}}\leftarrow{\underset{\{{JPS_{a,}JPS_{b}}\}}{\text{argmin}}\left\{ J_{a},J_{b} \right\}}$ 21 P o l yw h o l e← Convex Decomposition in 𝒰 ∪ ℱ using J P Si n 23 W h o l e← MIQP in P o l yw h o l e from A to G using fw h o l e 25 P o l ys a f e←Convex Decomposition in ℱ using J P Si n, k n o w n 27 S a f e ← MIQP in P o l ys a f e from R to F using fs a f e 30 fw h o l e, k← Factor that worked for W h o l e 31 fs a f e, k← Factor that worked for S a f e 32 Δ tk← Total replanning time

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Planning", "weight": 1.0} -->

Algorithm 1 summarizes the full approach (see also Fig. 3). Let $L$ be the current position of the UAV. The point $A$ is chosen in the Committed Trajectory of the previous replanning step with an offset $\deltat$ from $L$. This offset $\deltat$ is computed by multiplying the total time of the previous replanning step by $\alpha \geq 1$ (typically $\alpha \approx 1.25$). The idea here is to dynamically change this offset to ensure that most of the times the solver is able to find the next solution in less than $\deltat$. Then, the final goal $G_{term}$ is projected into the sliding map $\mathcal{M}$ (centered on the UAV) in the direction $\overset{\rightarrow}{G_{term}A}$ to obtain the point $G$ (line 1). Next, we run JPS from $A$ to $G$ (line 1) to obtain $JPS_{a}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A Planning", "weight": 1.0} -->

The local planner then must decide if the current JPS solution should be used to guide the optimization (lines 1-1). Instead of blindly trusting the last JPS solution ($JPS_{a}$) as the best direction for the local planner to optimize (note that JPS is a zero-order model, without dynamics encoded), we take into account the dynamics of the UAV in the following way: First of all, we modify the $JPS_{k - 1}$ so that it does not collide with the new obstacles seen (Fig. 4): we find the points $I_{1}$ and $I_{2}$ (first and last intersections of $JPS_{k - 1}$ with $\mathcal{O}$) and run JPS three times, so $A\rightarrow I_{1}$, $I_{1}\rightarrow I_{2}$ and $I_{2}\rightarrow I_{G}$. Hence, the modified version, denoted by $JPS_{b}$, will be the concatenation of these three paths.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Planning", "weight": 1.0} -->

Then, we compute a lower bound on $dt$ using Eq. 7 for both $A\rightarrow C$ and $A\rightarrow D$, where $C$ and $D$ are the intersections of the previous JPS paths with a sphere $\mathcal{S}$ of radius $r$ centered on $A$. Next, we find the cost-to-go associated with each direction by adding this $dt_{a}$ (or $dt_{b}$) and the time it would take the UAV to go from $C$ (or $D$) to $G$ following the JPS solution and flying at $v_{max}$. Finally, the one with lowest cost is chosen, and therefore ${JPS_{k}}\leftarrow{\underset{\{{JPS_{a,}JPS_{b}}\}}{\text{argmin}}{\{ J_{a},J_{b}\}}}$. This will be the direction towards which the local planner will optimize.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-A Planning", "weight": 1.0} -->

The Whole Trajectory (lines 1-1) is obtained as follows. We do the convex decomposition of $\mathcal{U} \cup \mathcal{F}$ around $JPS_{in}$, which is the part of $JPS_{k}$ that is inside the sphere $\mathcal{S}$. This gives a series of overlapping polyhedra that we denote as $Poly_{whole}$. Then, the MIQP in is solved using these polyhedral constraints to obtain the Whole Trajectory.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A Planning", "weight": 1.0} -->

The Safe Trajectory is computed as in lines 1-1. First we choose the point $R$ along the Whole Trajectory with an offset $\deltat^{\prime}$ from $A$ (this $\deltat^{\prime}$ is computed by multiplying the previous replanning time by $\beta \geq 1$), and run convex decomposition in $\mathcal{F}$ using the part of $JPS_{in}$ that is in $\mathcal{F}$, obtaining the polyhedra $Poly_{safe}$. Then, we solve the MIQP from $R$ to any point $F$ inside $Poly_{safe}$ (this point $F$ is chosen by the optimizer).

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A Planning", "weight": 1.0} -->

In both of the convex decompositions presented above, one polyhedron is created for each segment of the piecewise linear paths. To obtain a less conservative solution (i.e. bigger polyhedra), we first check the length of segments of the JPS path, creating more vertexes if this length exceeds certain threshold $l_{max}$. Moreover, we truncate the number of segments in the path to ensure that the number of polyhedra found does not exceed a threshold $P_{max}$. This helps reduce the computation times (see Sec. IV).

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A Planning", "weight": 1.0} -->

Finally (line 1), we compute the Committed Trajectory by concatenating the piece $A\rightarrow R$ of the Whole Trajectory, and the Safe Trajectory. Note that in this algorithm we have run two decoupled optimization problems per replanning step: one for the Whole Trajectory, and one for the Safe Trajectory. This ensures that the piece $A\rightarrow R$ is not influenced by the braking maneuver $R\rightarrow F$, and therefore guarantees a higher nominal speed on this first piece. The intervals $L\rightarrow A$ and $A\rightarrow R$ have been designed so that, with high probability, at least one replanning step can be solved within that interval. Moreover, to prevent the (very rare) cases where both $A$ and $R$ are in $\mathcal{F}$, but the piece $A - R$ is not, we check that piece $A - R$ against collision with $\mathcal{U}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A Planning", "weight": 1.0} -->

If any of the two optimizations in this algorithm fails, or the piece $A - R$ intersects $\mathcal{U}$, or the replanning step takes longer than $\deltat$, the UAV does not commit to a new trajectory in that replanning step, and continues executing the Committed Trajectory of the previous replanning step. Thus safety is guaranteed by construction: the UAV will only fly Committed Trajectories, which are always guaranteed to be in $\mathcal{F}$ with a terminal stopping condition.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B Mapping", "weight": 1.0} -->

For the mapping, we use a sliding map centered on the UAV that moves as the UAV flies. We fuse a depth map into the occupancy grid using the 3D Bresenham's line algorithm for ray-tracing, and $\mathcal{O}$ and $\mathcal{U}$ are inflated by the radius of the UAV to ensure safety.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Simulation", "weight": 1.0} -->

We first test FASTER in 10 random forest environments with an obstacle density of $0.1$ obstacles/m^2^ (see Fig. 5) and compare the flight distances achieved against the following seven approaches: Incremental approach (no goal selection), random goal selection, optimistic RRT^⋆^ (unknown space = free), conservative RRT^⋆^ (unknown space = occupied), "next-best-view" planner (NBVP), Safe Local Exploration, (see for details of all these approaches), and Multi-Fidelity.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Simulation", "weight": 1.0} -->

The results are shown in Table III, which highlights that FASTER achieves a $8 - {51\%}$ improvement in the distance. Completion times are compared in Table III to our previous proposed algorithm (time values are not available for all other algorithms in Table III). FASTER achieves an improvement of $52\%$ in the completion time. The dynamic constraints imposed for the results of this table are (per axis) $v_{max} = 5$ m/s, $a_{max} = 5$ m/s^2^, and $j_{max} = 8$ m/s^3^.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-A Simulation", "weight": 1.0} -->

We also test FASTER using the bugtrap environment shown in Fig. 5, and obtain the results that appear on Table III. Both algorithms have a similar total distance, but FASTER achieves an improvement of $63\%$ on the total flight time. For both cases the dynamic constraints imposed are $v_{max} = 10$ m/s, $a_{max} = 10$ m/s^2^, and $j_{max} = 40$ m/s^3^.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-A Simulation", "weight": 1.0} -->

The timing breakdown of Alg. 1 as a function of the maximum number of polyhedra $P_{max}$ is shown in Fig. 6. The number of intervals $N$ was 10 for the Whole Trajectory and 7 for the Safe Trajectory. Note that the runtime for the MIQP of the Safe Trajectory is approximately constant as a function of $P_{max}$. This is due to the fact that the Safe Trajectory is planned only in $\mathcal{F}$, and therefore most of the times $P < P_{max}$. For the simulations and hardware experiments presented in this paper, $P_{max} = {2 - 3}$ was used. The runtimes for JPS as a function of the voxel size of the map for the forest simulation are available in Fig. 7 of. All these timing breakdowns were measured using an Intel Core i7-7700HQ 2.8GHz Processor.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B Hardware", "weight": 1.0} -->

The UAV used in the hardware experiments is shown in Fig. 7. The perception runs on the Intel^®^ RealSense, the mapper and planner run on the Intel^®^ NUC, and the control runs on the Qualcomm^®^ SnapDragon Flight. The attitude, IMU biases, position and velocity are estimated by fusing (via a Kalman filter) propagated IMU measurements with an external motion capture system.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Hardware", "weight": 1.0} -->

The first and second experiments (Fig. 11 and 11) were done in similar obstacle environments with the same starting point, but with different goal locations. In the first experiment (Fig. 11), the UAV performs a 3D agile maneuver to avoid the obstacles on the table. In the second experiment (Fig. 11) the UAV flies through the narrow gap of the cardboard boxes structure, and then flies below the triangle-shaped obstacle. In these two experiments, the maximum speed was $2.1$ m/s.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B Hardware", "weight": 1.0} -->

In the third and fourth experiments (Fig 11 and 11), the UAV must fly through a space with poles of different heights, and finally below the cardboard boxes structure to reach the goal, achieving a maximum speed of $3.6$ m/s.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B Hardware", "weight": 1.0} -->

For $P_{max} = 2$, the boxplots of the runtimes achieved on the forest simulation (measured on an Intel Core i7-7700HQ) and on the hardware experiments (measured on the onboard Intel NUC with the mapper and the RealSense also running on it) are shown in Fig. 12. For the runtimes of the MIQP for the Whole and the Safe Trajectories, the 75^th^ percentile is always below $32$ ms.

<!-- chunk {"id": "body-0042", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

This work presented FASTER, a fast and safe planner for agile flights in unknown environments. The key properties of this planner is that it leads to a higher nominal speed than other works by planning both in $\mathcal{U}$ and $\mathcal{F}$, and ensures safety by having always a Safe Trajectory planned in $\mathcal{F}$ at the beginning of every replanning step. FASTER was tested successfully both in simulated and in hardware flights, achieving velocities up to $3.6$ m/s.
