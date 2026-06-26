<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Bubble Planner: Planning High-speed Smooth Quadrotor Trajectories Using Receding Corridors

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Quadrotors are agile platforms. With human experts, they can perform extremely high-speed flights in cluttered environments. However, fully autonomous flight at high speed remains a significant challenge. In this work, we propose a motion planning algorithm based on the corridor-constrained minimum control effort trajectory optimization (MINCO) framework. Specifically, we use a series of overlapping spheres to represent the free space of the environment and propose two novel designs that enable the algorithm to plan high-speed quadrotor trajectories in real-time. One is a sampling-based corridor generation method that generates spheres with large overlapped areas (hence overall corridor size) between two neighboring spheres. The second is a Receding Horizon Corridors (RHC) strategy, where part of the previously generated corridor is reused in each replan. Together, these two designs enlarge the corridor spaces in accordance with the quadrotor's current state and hence allow the quadrotor to maneuver at high speeds. We benchmark our algorithm against other state-of-the-art planning methods to show its superiority in simulation. Comprehensive ablation studies are also conducted to show the necessity of the two designs.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The proposed method is finally evaluated on an autonomous LiDAR-navigated quadrotor UAV in woods environments, achieving flight speeds over 13.7 m/s without any prior map of the environment or external localization facility.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Quadrotors are proved to be one of the most agile platforms which perform increasingly complex missions in different scenarios. However, high-speed flight in unknown environments is still an open problem. The limits on payload and onboard sensing make this task especially challenging for aerial robots. To achieve high-speed flights, trajectory planning is of vital importance to ensure the safety (i.e., collision avoidance ), smoothness, and fast maneuvers facing unknown obstacles.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

High-speed trajectory planning in unknown environments is a great challenge, especially in the replanning phase where the high quadrotor speeds require extremely agile maneuvers to avoid newly-sensed obstacles. Existing (re-)planning methods typically consist of a frontend that aims to find a guiding path (or flight corridor) and a backend that smooths the trajectory around the guiding path (or optimizes a smooth trajectory within the corridor). The main difficulty in this framework is how to design the frontend such that the replanned guiding path (or flight corridor) is feasible: at least one dynamically-feasible and obstacle-free solution can be found in the backend optimization. A poorly-designed frontend may leave too little space for the quadrotor to avoid obstacles (e.g., decelerate or make turns), hence leaving no dynamically feasible solution in the subsequent trajectory optimization. Another difficulty is the backend optimization, which needs to perform both temporal and spatial deformation in an efficient manner such that the maximal speed can be attained.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose a robust and efficient motion planning algorithm to address the above issues systematically. The overall algorithm is based on a corridor approach. In the backend, we adopt a state-of-the-art minimum control effort optimization (MINCO) framework to deform the trajectory temporal and spatial parameters efficiently. Our contribution in this paper mainly lies in the frontend, including: A novel sampling-based corridor generation method that preserves large corridor volume by considering the size of each sphere and their overlapped spaces. The increased corridor volume allows more space for the quadrotor to maneuver (hence succeed) at high speeds.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A Receding Horizon Corridors (RHC) scheme that reuses corridors in the previous planning cycle. Specifically, in each replan, the first part of the flight corridor is directly from the previous planning cycle, and the second part is generated according to newly-sensed obstacles. This receding scheme ensures the corridor in each replan always contains sufficient space for the quadrotor to maneuver from its current state, significantly improving the replan process's success rate and convergence speed under high-speed flight.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A real-time planning system that integrates these two designs of frontend with the MINCO backend. A comprehensive benchmark comparison and an ablation study are conducted in simulation to show the superiority of our system and the effectiveness of the two designs.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Implementation and validation the proposed method on a fully autonomous quadrotor system. Multiple real-world tests show that our methods achieve flight speeds over ${13.7m}/s$ (see Fig. 1).

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A High-Speed Navigation in the Wild", "weight": 1.0} -->

Various approaches have been proposed to enable autonomous quadrotor flights in unknown environments. Florence et al. propose a reactive planner, which takes depth image as input and selects the best trajectory from a pre-built motion primitives library. The work in proposes an uncertainty-aware lazy search map called NanoMap on the reactive controller and achieves a maximum flight speed of ${10m}/s$. Although it has a low computation complexity, the pre-built set of motion primitives is relatively small, making it difficult to cover fine maneuvering skills that are necessary when the quadrotor is facing new, unexpected obstacles during high-speed flights. Similar motion primitive-based method is used (as a frontend) by Zhou et al., Liu et al., Zhang et al. and Kong et al., which therefore suffer from similar drawbacks. Ye et al. utilizes a frontend based on RRT\* kinodynamic sampling. Similar to the motion primitive methods, the sampled states are usually in low dimensions (e.g., position and velocity) and few in numbers in order to ensure sufficient computation efficiency, making it very difficult to produce fine quadrotor maneuvers in high-speed flights.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A High-Speed Navigation in the Wild", "weight": 1.0} -->

Unlike the previous methods, which typically have a frontend planning a rough path from the quadrotor's current position to the target one and a backend which further refines the trajectory by optimization, Zhou et al. proposed to plan a whole trajectory without considering any obstacle in the first stage and then locally modify the trajectory to fly around the detected obstacles. The local trajectory modification is achieved efficiently by directly incorporating a repulsive force from obstacles in the trajectory optimization cost function. The repulsive force is similar to a coarse-level distance field and hence suffers from the local minimum problem, hence unsuitable for high-speed trajectory planning. Another interesting method is proposed by Loquercio et al., they use imitation learning to generate a trajectory directly from the depth image and current state. Limited by the sensing range and noise, the success rate of their methods decreases when forward speed is over 10 $m/s$. Compared with the methods mentioned above, our method achieves much higher flight speed in both simulation and experiments (see Fig. 2).

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Corridor-based Trajectory Planning", "weight": 1.0} -->

Corridor-based trajectory planning methods, which use geometrical shapes to represent free space, have been popular in recent years. Chen et al. build a discrete graph from an OctoMap structure and directly use free cubes in OctoMap as the corridor constraints. Liu et al. use polyhedrons to represent the free space, also called convex decomposition. Each cube or polyhedron on the flight corridor then imposes multiple linear hyperplane constraints in the subsequent trajectory optimization. Sphere-shaped corridors are also very commonly used. Compared with polyhedrons, a sphere imposes only one constraint in the trajectory optimization. It can often be quickly obtained by Nearest Neighbor Search (NN-Search) using a KD-Tree structure. Gao et al. propose a sphere-shaped corridor generation scheme under the RRT\* framework. Ji et al. propose a forward-spanning-tree-based spherical corridor generation scheme. These two methods can generate corridors in a relatively short time. However, their corridor generation process only considers the connectivity of adjacent spheres. The found spheres often have small overlaps between adjacent ones, which over constrains the subsequent trajectory optimization and leaves tiny space for the quadrotor to maneuver at high speeds.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-B Corridor-based Trajectory Planning", "weight": 1.0} -->

Another problem is the lack of explicit consideration of the quadrotor's current speed, the resultant flight corridor often does not contain sufficient space for the quadrotor to maneuver from its current speed. The two problems will considerably reduce the feasible solution space and cause the backend optimization to fail. In contrast, our frontend attempts to find large individual spheres and their overlaps, while the receding scheme automatically incorporates the quadrotor current speed in each replan. These two designs greatly improve the success rate and convergence speed of the subsequent trajectory optimization.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Corridor-based Trajectory Planning", "weight": 1.0} -->

Trajectory optimization with the corridor constraint is also well studied by some recent works. Ji et al. use an alternating minimization method and iteratively insert waypoints to ensure that the trajectory completely falls in the corridor. However, the waypoints are selected heuristically, which leads to sub-optimal solutions. Mellinger et al. use piece-wise polynomial to represent the trajectory and generate a minimum-snap trajectory by solving a quadratic programming (QP) problem. The corridor constraints are used as inequality constraints in the QP. Gao et al. use B-spline to represent trajectories and formulate the corridor constraints and trajectory optimization into a second-order cone programming (SOCP) problem. Both methods solve the optimization problem with hard constraints and have quite significant computation time. Our approach is most similar to. The corridor constraints are first eliminated by a $C^{2}$-continuous barrier function. Then, a spatial-temporal deformation is performed. The optimization problem is finally turned into an unconstrained one that can be solved by Quasi-Newton methods efficiently and robustly.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Planner", "weight": 1.0} -->

In this section, we present the frontend design that enables high-speed trajectory optimization, which is the main contribution of this paper.

<!-- chunk {"id": "body-0016", "role": "body", "section": "IV-A Sphere-Shaped Corridor", "weight": 1.0} -->

As shown in Fig. 4, a sphere is defined by its center $o \in {\mathbb{R}}^{3}$, the nearest obstacle point $n \in {\mathbb{R}}^{3}$, and the radius: where $r_{d}$ is the radius of the drone. During the trajectory optimization process, each piece of trajectory is constrained in the corresponding sphere to satisfy safety constraints.

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-A Sphere-Shaped Corridor", "weight": 1.0} -->

To generate a new sphere, we first build a KD-Tree with the obstacle point cloud. Then, for a given center of the sphere $o$, a nearest neighbor search (NN-Search) is performed on that KD-Tree to find the nearest obstacle point $n$, which then determines the radius as. We call this process GenerateOneSphere$(o)$, which will be used in the sequel.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-B Flight Corridor Generation", "weight": 1.0} -->

The main workflow of the flight corridor generation is described in Alg. 1, where a complete flight corridor $\mathcal{B}$ is generated from the given initial position $p_{0}$, goal position $p_{g}$, and a global guide path $\mathcal{T}$ generated by A\*. The algorithm initializes with a largest possible sphere $\mathcal{B}_{cur}$ around the initial position $p_{0}$ (Line 2-3). Then, in Line 1, a local guide point $p_{h}$ is selected from the guide path $\mathcal{T}$, which is the nearest point out of the current sphere $\mathcal{B}_{cur}$, and a new sphere is generated by BatchSample($p_{h},\mathcal{B}_{cur}$) (Sec. IV-B1) and added to $\mathcal{B}$. This process repeats until the goal position $p_{g}$ is included in the new generated sphere (Line 8-10).

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-B Flight Corridor Generation", "weight": 1.0} -->

With the found flight corridor $\mathcal{B}$, the initial waypoint position $\mathbf{q}$ and time allocation $\mathbf{T}$ are initialized by the function WaypointAndTimeInitialization ($\mathcal{B}$)(Sec. IV-B2) and then optimized in the backend (Sec. III).

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-B Flight Corridor Generation", "weight": 1.0} -->

1 Notation: The flight corridor ℬ; global guide path 𝒯; Initial and goal position: p0, pg; local guide point ph

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B1 Batch sample", "weight": 1.0} -->

The problem of trajectory optimization under flight corridor constraints is highly non-convex, which means overly conservative constraints may lead to local-minimum or even infeasible solution when the quadrotor initial speed is high. Existing methods only considered the connectivity between two adjacent spheres. To preserve larger space for the quadrotor to maneuver hence improve the feasibility of the trajectory optimization at high-speeds, we propose a novel batch sample method to generate a high-quality corridor. We consider this problem in the following aspects: (a) the volume of each sphere: a sphere with larger size can better approximate the real free space with fewer number of spheres, making the optimization problem less constrained, (b) the volume of the overlapped spaces between two adjacent spheres: as discussed in Sec. III, all waypoints of the trajectory are constrained in the intersecting space, a larger intersecting space means more freedom for the optimization process.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B1 Batch sample", "weight": 1.0} -->

1 Notation: Last sphere ℬf; Guide point ph; Best sphere in this round ℬb e s t; Random sampler 𝒮; Maximum sample num K; Safe distance rd; Priority queue sorted by sphere’s score: 𝒬; The sampling process is shown in Alg.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B1 Batch sample", "weight": 1.0} -->

2. We first initialize the sampler $\mathcal{S}$ in Line 2. As shown in the orange area of Fig. 5, the sampler generates a random candidate point $p_{cand} \in {\mathbb{R}}^{3}$ under a 3D Gaussian distribution $N{(\mu,\Sigma)}$, where the mean is set at the guide point $\mu = p_{h}$ and the covariance is set as $\Sigma = {\text{diag}\left(\sigma_{x},\sigma_{y},\sigma_{z} \right)}$, ${\sigma_{x} = {\frac{1}{3}\left\| {o_{f} - p_{h}} \right\|_{2}}},{\sigma_{z} = \sigma_{y} = {2\sigma_{x}}}$, where $o_{f}$ is the center of last sphere and the $\sigma_{x}$ direction is aligned with the direction of

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B1 Batch sample", "weight": 1.0} -->

Then in Line 2-2, a total number of $K$ points (called a batch) are randomly sampled with $\mathcal{S}$, each has its score computed by the function ComputeScore($\mathcal{B}_{cand}$) defined below: where ${\rho_{r},\rho_{v}} \in {\mathbb{R}}_{+}$ are positive weights, $V_{\text{cand}}$ is the volume of the candidate sphere $\mathcal{B}_{cand}$ and $V_{\text{inter}}$ is the overlapped volume between $\mathcal{B}_{cand}$ and $\mathcal{B}_{f}$. Finally, the best sphere with the highest score is selected in Line 13.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B1 Batch sample", "weight": 1.0} -->

As shown in Fig. 6, compared with Gao, the proposed method can better approximate the real free space with fewer spheres and larger sphere sizes. Furthermore, our algorithm has lower computational complexity than Gao's approach, which uses an RRT-like method and takes samples from the whole space. Our process follows a coarse-to-fine manner, where we first use A\* to find the shortest path and then take batch samples only around this path. In this way, the sample space, hence computation time, is significantly reduced. We test 100 times in the same environment shown in Fig. 6. The proposed method only takes an average $0.74ms$ to generate the corridor, while Gao's method takes an average $100ms$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B2 Waypiont and Time Initialization", "weight": 1.0} -->

For a given flight corridor $\mathcal{B}$, we adopt a Default Initialization strategy, where the waypoint are initialized as the center of the overlap space between two adjacent spheres (pink points in Fig. 7(b)), and the time allocation is initialized as $T_{i} = \frac{\left\| {q_{i} - q_{i - 1}} \right\|_{2}}{v_{max}}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-C Receding Horizon Corridors in Replan", "weight": 1.0} -->

During a high-speed flight in an unknown environment, the quadrotor needs to replan frequently to avoid newly sensed obstacles. We use a distance-triggering replaning strategy. Specifically, the trajectory is planned (both frontend corridor generation and backend optimization) in a fixed distance $D$ (i.e. planning horizon) depending on the sensing range. Denote the position of last replan as $p_{last}$ and current quadrotor position as $p_{curr}$. The replan process is triggered if $\left\| {p_{last} - p_{curr}} \right\|_{2} > {\gamma \cdot D}$, where $\gamma \in {\lbrack 0,1\rbrack}$ is a constant ratio. In this way, as the drone moves forward, the newly sensed obstacle can be actively handled by the replan process. A replan is also triggered when the current trajectory under execution is found to collide with any obstacles.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-C Receding Horizon Corridors in Replan", "weight": 1.0} -->

A major challenge in the replan occurs when the quadrotor speed is high, which requires sufficient space for the quadrotor to maneuver such that the newly sensed obstacles can be avoided successfully. Corridor generation without considering the quadrotor's current state often causes too small feasible region in the trajectory optimization, which is difficult (or even impossible) to solve (e.g., by optimizing ). Another problem is that with the increase of the current speed, the objective function becomes highly non-convex. As described in Sec. III, our optimization problem is turned into an unconstrained one. The non-convexity of the objective function may cause the optimization with the Default Initialization to easily stuck at a bad local minimum which violates the collision-free or kinodynamic constraints.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-C Receding Horizon Corridors in Replan", "weight": 1.0} -->

We solve these problems by a Receding Horizon Corridors (RHC) strategy shown in Fig. 7. The key is to reuse a few spheres from the previous planning cycle in current replan. Concretely, when a new replan is triggered, the nearest future waypoint $\mathbf{d}_{rp}$ in $\mathbf{q}$ is selected as the initial state. A few spheres after $\mathbf{d}_{rp}$ will be reused to constitute the first part of the new corridor, followed by newly generated spheres reaching the current planning horizon $D$. This receding scheme ensures the corridor in each replan always contains sufficient space for the quadrotor to maneuver from its current state (since the current quadrotor state is on the previous trajectory, which is contained in the previous corridor), hence significantly enlarging the feasible region in the backend trajectory optimization. In experiments, we reuse spheres that fall within a certain distance (e.g., $3m$) of the current quadrotor position $p_{curr}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-C Receding Horizon Corridors in Replan", "weight": 1.0} -->

Furthermore, to speed up the trajectory optimization and mitigate the local minimum issue, the waypoints $\mathbf{q}$ and time allocation $\mathbf{T}$ contained in the reused corridor, which were optimized in the previous planning cycle, are used to initialize the current trajectory optimization (i.e. Hot Initialization). The waypoints and time allocation in the newly generated spheres are still initialized by the default scheme (Sec. IV-B2).

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-A Benchmark Comparison", "weight": 1.0} -->

In this section, we compare the proposed method with a most recent planning work based on imitation learning (Learning), and two model-based planning methods evaluated by it, including a frontend-backend type optimization-based method from Zhou et al. (FastPlanner) and a reactive planner designed for the high-speed flight from Florence et al. (Reactive). We evaluate the performance of our method in a simulated forest environment used by the learning method. Due to the unavailability of the simulation environment used by the original work, we reproduce the environment according to their description. Specifically, the forest has trees distributed in a rectangular region $R{(l,w)}$ of width $w$ and length $l$, the origin lies in the center of $R$. Trees are randomly placed according to a homogeneous Poisson point process $P$ with the intensity ${\deltatree}/{(m^{2})}$. The sensor input in the simulation includes a simulated LiDAR point cloud, with the sensing range of $8m$ at $30Hz$ (see green points in Fig. 8(b)).

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-A Benchmark Comparison", "weight": 1.0} -->

The quadrotor full state is assumed to be known to eliminate the influence of state estimation.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-A Benchmark Comparison", "weight": 1.0} -->

We use exactly the same configuration in to make a fair comparison: $w = {30m}$ and $l = {60m}$, and the start zone of the drone is at $({- {l/2}},0)$, the goal position $({l/2},0)$. Three different tree densities with $\delta = {1/49}$ (low), $\delta = {1/36}$ (medium), and $\delta = {1/25}$ (high) are tested. In each experiment, we use different random seed to generate different simulated maps. One flight is considered to be successful only if the drone reaches the goal without violating the velocity, acceleration, or collision-free constraints. The results are shown in Fig. 9. Similar to, we test our method 10 times in each different density or speed and compute the success rate of each, and the results of other baseline are directly obtained.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-A Benchmark Comparison", "weight": 1.0} -->

Noting that, the maximum mass-normalized thrust of the simulated drone is limited to ${35.3m}/s^{2}$, while we limit our simulated drone to ${15m}/s^{2}$. As can be seen, our approach outperforms others in all cases, even with a lower thrust limit. Moreover, compared with Loquercio et al., the proposed method generates much smoother trajectories, which is usually easier to track (see Fig. 8).

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-B Ablation Study", "weight": 1.0} -->

To further validate each module of the proposed method, we compare our method in detail with Gao et al., which generates sphere-shaped corridors in an RRT\* style and optimizes a minimal snap trajectory with fixed time allocation. We use the same simulated map configuration mentioned in Sec.V-A, but further add tests with $\delta = {1/12}$ (super high). The key three elements of our approach includes the trajectory optimization in Sec. III (MINCO), the frontend corridor generation in Sec. IV-B (Front), and the receding horizon corridors strategy (RHC) in Sec. IV-C. A series of ablation studies are performed, and the results are shown in Fig. 10. Gao is the original version. This method fails to generate trajectory with speed over ${2m}/s$ due to the inability to optimize time allocation in the backend. To fix this issue, we replace the backend of Gao by MINCO (Gao+MINCO) and compare it with our method without RHC strategy (Ours (Front+MINCO)).

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-B Ablation Study", "weight": 1.0} -->

The performances of the two are very close, showing that MINCO can generate more aggressive trajectories and that our frontend alone does not improve the success rate much. Furthermore, we incorporate the RHC strategy to the method Gao (Gao + MINCO + RHC) and compare it with our full algorithm (with both frontend and RHC). As can be seen, each method with RHC has a significantly higher success rate at high speeds on all map densities, verifying the effectiveness of the RHC strategy. Moreover, our full algorithm with our frontend (Ours(Front + MINCO + RHC)) achieves a higher success rate than Gao with the same MINCO and RHC strategy (Gao+MINCO+RHC), showing the effectiveness of our frontend in the overall planning system.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-C Run Time Analysis", "weight": 1.0} -->

In this section, we compare the run time of the proposed method with the baseline. We test our method both on the desktop computer, with a 2.90 GHz Intel i7-10700 CPU, and an onboard computer with a 1.1 GHz Intel i7-10710U CPU. The baseline FastPlanner and Gao are tested on the same desktop computer. The test environment is a simulated forest with $\delta = \frac{1}{25}$ shown in Fig. 8(b). The computation time is divided into two parts: mapping and planning. For FastPlanner, the mapping process includes building a Euclidean signed distance field (ESDF), and planning includes frontend path-search and backend trajectory optimization. For Gao's method, the mapping process includes a static KD-Tree update, and the planning includes corridor generation and SOCP optimization. For the proposed method, the mapping includes the update of an OctoMap (no ray-casting) and an incremental KD-Tree (i.e., ikd-tree ). The planning includes frontend A\* search, corridor generation, and trajectory optimization.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-C Run Time Analysis", "weight": 1.0} -->

As shown in Table I, the proposed method enjoys much lower computational complexity, which can replan at over $50Hz$ even on the onboard platform.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In this paper, we propose a novel motion planning algorithm that generates smooth, collision-free, and high-speed trajectories in real-time. The whole planning system can work with fully onboard sensing, and computation at a replan frequency over $50Hz$. To enable high-speed flight in the wild, we proposed two novel designs. One is a sampling-based sphere-shaped corridor generation method, which can generate high-quality corridors (i.e. larger size and bigger overlaps) in a relatively short time. Another is a Receding Horizon Corridors strategy, which fully utilizes previously generated corridors and the optimized trajectory. With these designs, the proposed method significantly increases the replan success rate in high-speed cases.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

One limitation of our algorithm is that the reused corridors from last planning cycle are not guaranteed to be obstacle-free due to newly sensed obstacles that may be occluded in previous LiDAR measurements. This will cause the reused corridor to be discarded and hence occasionally lower the success rate when the environment is extremely cluttered. This limitation can be overcome by placing the first few corridors of a (re-)plan in known free spaces (instead of free and unknown spaces), so that these free corridors can be safely reused in the next planning cycle. Restraining the first few spheres in free spaces also enables the planning of a safe backup trajectory like which guarantees a safe flight. In the future, we will explore these designs and extend the method to more different missions and environments.
