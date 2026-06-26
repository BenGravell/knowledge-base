<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

SANDO is a safe trajectory planner for 3D dynamic unknown environments, where obstacle locations and motions are unknown a priori and a collision-free plan can become unsafe at any moment, requiring fast replanning. Existing soft-constraint planners are fast but cannot guarantee collision-free paths, while hard-constraint methods ensure safety at the cost of longer computation. SANDO addresses this trade-off through three contributions. First, a heat map-based A* global planner steers paths away from high-risk regions using soft costs, and a spatiotemporal safe flight corridor (STSFC) generator produces time-layered polytopes that inflate obstacles only by their worst-case reachable set at each time layer, rather than by the worst case over the entire horizon. Second, trajectory optimization is formulated as a Mixed-Integer Quadratic Program (MIQP) with hard collision-avoidance constraints, and a variable elimination technique reduces the number of decision variables, enabling fast computation. Third, a formal safety analysis establishes collision-free guarantees under explicit velocity-bound and estimation-error assumptions.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Ablation studies show that variable elimination yields up to 7.4x speedup in optimization time, and that STSFCs are critical for feasibility in dense dynamic environments. Benchmark simulations against state-of-the-art methods across standardized static benchmarks, obstacle-rich static forests, and dynamic environments show that SANDO consistently achieves the highest success rate with no constraint violations across all difficulty levels; perception-only experiments without ground truth obstacle information confirm robust performance under realistic sensing. Hardware experiments on a UAV with fully onboard planning, perception, and localization demonstrate six safe flights in static environments and ten safe flights among dynamic obstacles.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous unmanned aerial vehicle (UAV) navigation in dynamic unknown environments is challenging: the future trajectories of obstacles are unknown, so a collision-free path can become unsafe moments after it is computed. This requires planners that can quickly recompute safe trajectories while handling spatiotemporal collision avoidance. Existing approaches address parts of this challenge but fall into three categories with distinct limitations (see Table I).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

First, planners designed for unknown static environments (e.g., EGO-Planner, FASTER, HDSM, and SUPER ) achieve fast replanning but assume that once space is observed as free, it remains free, making them unsuitable for environments with moving obstacles. Second, planners that handle dynamic obstacles with soft constraints (e.g., HOPA, ViGO, FAPP, Risk-Aware, and FHD ) can react to moving obstacles but provide no formal safety guarantee, as collision avoidance is encouraged via penalty terms rather than enforced (see Fig. 1). Third, planners that enforce hard safety constraints in dynamic environments (e.g., CC-MPC, OA-MPC, Liu et al., Stamouli et al., STS, and IP-MPC ) guarantee safety only at discretized model predictive control (MPC) or sample points, leaving the trajectory potentially unsafe between time steps. While PANTHER provides continuous-time safety in dynamic environments, it has only been demonstrated in open settings and the computation scales poorly with the number of obstacles.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

As summarized in Table I, no existing method simultaneously handles spatiotemporal dynamic obstacle collision avoidance, guarantees continuous-time safety, and operates in dynamic unknown confined environments. To address these gaps, we introduce SANDO (Safe AutoNomous trajectory planning for Dynamic unknOwn environments), a trajectory planner that integrates a heat map-based A^∗^ global planner, a novel Spatiotemporal Safe Flight Corridor (STSFC) generation method, and a variable elimination-based hard-constrained optimization technique to provide continuous-time safety guarantees in dynamic unknown environments.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Chance hard constraint at discretized MPC steps Continuous guarantee; Assume static env.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Continuous guarantee; Probabilistic inflation for obstacle uncertainty Hard constraint at discretized MPC steps & Temporally conservative (See Fig. 1) Chance hard constraint at discretized MPC steps Continuous guarantee; Assume static env.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Probabilistic safety guarantee at discretized MPC steps Use ViGO as planner Safety only guaranteed at discretized sample points Hard constraint at discretized MPC steps Continuous guarantee; Bound dynamic obstacles’ maximum speed TABLE I: State-of-the-art UAV trajectory planners in unknown environments. Safety guarantee: ✓ = continuous, △ = discretized, ✗ = none.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Environment Taxonomy", "weight": 1.0} -->

We focus on unknown environments, where no prior map is available, and classify them into two categories: static vs. dynamic, and open vs. confined. Static environments have fixed obstacles, whereas dynamic environments include moving obstacles. Open environments have relatively sparse obstacle distributions, whereas confined environments involve occlusions and narrow passages.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Environment Taxonomy", "weight": 1.0} -->

We organize our review around the three criteria in Table I, namely, environment type (static vs. dynamic), environment structure (open vs. confined), and safety guarantee level (none, discretized, or continuous). We first discuss planners designed for static environments, and then review dynamic-environment planners grouped by their safety guarantee.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Planning in Unknown Static Environments", "weight": 1.0} -->

Several planners are designed for unknown static environments and achieve fast replanning by assuming that once space is observed as free, it remains free. EGO-Planner uses a gradient-based local optimizer with soft collision penalties, enabling fast replanning in both open and confined static settings but providing no safety guarantees. FASTER builds on the MIQP trajectory planning approaches by generating safe flight corridors via convex decomposition and solving a hard-constrained MIQP within them, providing continuous-time collision-free guarantees in static environments; however, it does not model dynamic obstacles. HDSM extends the corridor-based approach with a high-degree spline representation that improves trajectory smoothness and corridor utilization, also providing continuous safety guarantees but only under the static assumption. SUPER adopts FASTER's exploratory-safe trajectory framework and replaces the hard-constraint optimizer with a gradient-based solver for faster computation, but trades off safety guarantees by using soft constraints and is limited to static environments. While these methods work well in static settings, none of them handle dynamic obstacles.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-C Soft-Constrained Planning in Dynamic Environments", "weight": 1.0} -->

A number of planners handle dynamic obstacles but use soft constraints, meaning collision avoidance is encouraged via penalty terms but not strictly enforced. HOPA uses obstacle positions and potential fields to perform avoidance maneuvers, but operates only in open environments and provides no hard safety guarantee. ViGO fuses vision-based obstacle detection with a gradient-based planner to navigate dynamic clutter in both open and confined settings, but relies on soft collision penalties. FAPP tightly integrates perception and planning for dynamic cluttered environments, demonstrating fast replanning and good practical performance; however, its collision avoidance is soft-constrained using MINCO, so it does not guarantee safety. Xu et al. propose a heuristic-based incremental probabilistic roadmap (PRM) for efficient replanning in dynamic environments, using ViGO as the underlying local planner and thus inheriting its soft-constraint limitation. Risk-Aware incorporates risk metrics into the planning objective to improve safety awareness in dynamic environments, but the risk terms act as soft penalties rather than hard constraints. FHD uses a learning-based approach to navigate dynamic environments, achieving agile flight without explicit obstacle modeling; however, the learned policy provides no formal safety guarantee.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-C Soft-Constrained Planning in Dynamic Environments", "weight": 1.0} -->

While these methods demonstrate strong empirical performance, the absence of hard constraints means safety cannot be formally guaranteed, which is a critical limitation for safety-critical UAV deployments.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-D Safety-Guaranteed Planning in Dynamic Environments", "weight": 1.0} -->

Early approaches to dynamic collision avoidance include velocity obstacles. Formal safety frameworks such as control barrier functions and Hamilton-Jacobi reachability provide rigorous guarantees but can be computationally expensive in 3D cluttered environments. In the trajectory planning literature, a smaller set of planners enforce collision avoidance as hard constraints in dynamic environments. We distinguish between discretized guarantees (safety enforced only at sampled time steps or MPC knot points) and continuous guarantees (safety enforced continuously along the trajectory).

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-D1 Discretized Safety Guarantees", "weight": 1.0} -->

CC-MPC formulates chance constraints within an MPC framework to handle obstacle uncertainty, providing probabilistic safety guarantees at discretized MPC steps but not between them. OA-MPC provides hard-constraint guarantees at MPC steps via worst-case reachability analysis and accounts for occluded regions, but ignores the temporal motion history of obstacles, leading to excessive conservatism (see Fig. 1). Liu et al. compute tight collision probability bounds and enforce chance constraints at MPC steps, but safety is only guaranteed at discrete time points. Stamouli et al. combine conformal prediction with shrinking-horizon MPC to provide probabilistic safety guarantees at MPC steps without distributional assumptions; however, their approach has only been demonstrated in open environments. STS uses state-time space to handle dynamic environments; however, it is only demonstrated in 2D scenarios and only provides safety guarantees at discretized sample points but not continuously. IP-MPC incorporates intent prediction of dynamic obstacles into an MPC framework with hard constraints at MPC steps, improving avoidance quality but without continuous-time guarantees.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-D1 Discretized Safety Guarantees", "weight": 1.0} -->

All of these methods share a fundamental limitation: collisions can occur between the discrete time points at which constraints are enforced, particularly for fast-moving obstacles or long MPC intervals.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-D2 Continuous Safety Guarantees", "weight": 1.0} -->

PANTHER constructs per-obstacle convex hulls to enforce continuous-time collision avoidance in dynamic unknown environments using probabilistic reachable-set inflation for obstacle uncertainty. However, its per-obstacle convex hull representation becomes computationally expensive as the number of obstacles grows, and it has been demonstrated primarily in open environments without many static obstacles.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-E Contributions", "weight": 1.0} -->

To address the gaps identified above, SANDO makes the following contributions: STSFC Generation: A novel Spatiotemporal Safe Flight Corridor generation method that produces time-layered polytope sequences accounting for worst-case obstacle reachable sets at each time layer, addressing the lack of time-varying corridor generation framework for dynamic environments (Section IV Generation ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments")).

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-E Contributions", "weight": 1.0} -->

Heat Map-based Global Planner: A heat map-based A^∗^ planner that assigns soft costs around both static and dynamic obstacles, guiding the global path toward regions where larger STSFC corridors can be generated (Section V).

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-E Contributions", "weight": 1.0} -->

MIQP Trajectory Optimization with STSFCs: A hard-constraint MIQP formulation that assigns each trajectory piece to a time-layered STSFC polytope, whose continuous-time collision-free guarantee is established by the formal safety analysis below (Section VI).

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-E Contributions", "weight": 1.0} -->

Formal Safety Analysis: Safety guarantees through worst-case reachable set inflation with explicit assumptions, and a discussion of recursive feasibility limitations.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-E Contributions", "weight": 1.0} -->

Extensive Evaluation in simulation across diverse environments and hardware experiments on a fully automated UAV platform, demonstrating the practical effectiveness of SANDO in real-world scenarios.

<!-- chunk {"id": "body-0024", "role": "body", "section": "System Overview", "weight": 1.0} -->

SANDO consists of five modules (see Fig. 2): a dynamic obstacle tracker, a heat map generator, a global path planner, an STSFC generator, and a hard-constraint local trajectory optimizer. Each module is designed to handle dynamic unknown obstacles, which requires planning in spatiotemporal space, adapting trajectories as obstacles move unpredictably, and computing safe trajectories in real time.

<!-- chunk {"id": "body-0025", "role": "body", "section": "System Overview", "weight": 1.0} -->

SANDO processes point cloud data from a LiDAR sensor and/or a depth camera. The point cloud is processed by the map manager, which generates a voxel map with heat map costs for both static and dynamic obstacles. Point cloud data are also used by a dynamic obstacle tracker, where dynamic obstacles are detected, clustered, and tracked to estimate their current positions and predict their future trajectories, as detailed in Section VII.

<!-- chunk {"id": "body-0026", "role": "body", "section": "System Overview", "weight": 1.0} -->

The voxel map and predicted obstacle trajectories are provided as inputs to the heat map-based global planner and the STSFC Generation module. The global planner computes a global path from the agent's start position to a *subgoal* (a projection of the goal position on the local map around the agent) using heat map-based A^∗^ search with soft costs for both static and dynamic obstacles; see Section V for details. SANDO then constructs STSFCs, which account for spatial and temporal dimensions, by inflating dynamic obstacles based on their worst-case reachable sets at each time layer, as described in Section IV Generation ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments").

<!-- chunk {"id": "body-0027", "role": "body", "section": "System Overview", "weight": 1.0} -->

Since dynamic obstacles can change their motion unpredictably, fast trajectory optimization is needed. SANDO introduces a variable elimination approach that reduces the number of decision variables and constraints in the optimization problem, enabling fast hard-constraint optimization; see Section VI. The resulting trajectory is then sent to the low-level controller for execution. Replanning is triggered at 100 Hz; however, a new replanning cycle begins only after the previous one completes, so the effective replanning rate is bounded by the total replanning time (typically 20--35 ms in hardware, yielding an effective rate of approximately 30--50 Hz). If replanning fails to find a feasible trajectory, the agent continues executing the previously computed trajectory; if no valid trajectory remains, the agent hovers in place. Point cloud processing, dynamic obstacle tracking, map management, and SANDO's planning modules are all parallelized.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Spatiotemporal Safe Flight Corridor (STSFC) Generation", "weight": 1.0} -->

We first define the key terminology used throughout the paper. Let $t_{0}$ denote the *current planning time*. The trajectory is composed of $N$ *pieces* $\bm{x}_{0},\ldots,\bm{x}_{N-1}$, each a cubic Bézier polynomial indexed by $n\in\{0,\ldots,N{-}1\}$. Each piece $n$ executes during the *time interval* $[t_{0}+n\cdot dt,\;t_{0}+(n{+}1)\cdot dt]$, where $dt$ is the uniform duration per piece, so that the full trajectory spans $[t_{0},\;t_{0}+N\cdot dt]$. The global path consists of $P$ *path segments*, indexed by $p\in\{0,\ldots,P{-}1\}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Spatiotemporal Safe Flight Corridor (STSFC) Generation", "weight": 1.0} -->

Each of the $K$ tracked dynamic obstacles, indexed by $k\in\{1,\ldots,K\}$, occupies a region $\mathcal{O}_{k}(t)\subset\mathbb{R}^{3}$ at time $t$, with true centroid $\mathbf{c}_{k}(t)\in\mathbb{R}^{3}$. The obstacle region is contained in an axis-aligned bounding box (AABB) centered at $\mathbf{c}_{k}(t)$ with half-extents $\mathbf{h}_{k}=(h_{k}^{x},\,h_{k}^{y},\,h_{k}^{z})\in\mathbb{R}_{>0}^{3}$: In dynamic environments, safety corridors must account for both spatial constraints and how obstacles move over time.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Spatiotemporal Safe Flight Corridor (STSFC) Generation", "weight": 1.0} -->

Traditional corridor generation methods, such as, produce purely spatial polytopes along a path, which is sufficient for static environments but does not capture how free space changes as obstacles move. This requires corridors that account for both the spatial location and the time at which each region is safe. To this end, we introduce *STSFCs*, time-varying polytope sequences where each time layer represents the collision-free region at a given duration in the trajectory's time horizon. This section describes the structure of STSFCs, the time allocation strategy, and the obstacle inflation method used to ensure safety guarantees. The global path input used during corridor generation is described in Section V.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Temporal Corridor Structure", "weight": 1.0} -->

An STSFC is represented as a two-dimensional array $\mathcal{C}[n][p]$ where: $n\in\{0,\ldots,N-1\}$ indexes the *time layer*, representing discrete time intervals along the trajectory, $p\in\{0,\ldots,P-1\}$ indexes the *spatial polytope* within each time layer, representing free-space regions at that time.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A Temporal Corridor Structure", "weight": 1.0} -->

Each element $\mathcal{C}[n][p]$ is a convex polytope defined by linear constraints $\{\mathbf{F}_{np},\mathbf{g}_{np}\}$ such that a point $\mathbf{x}\in\mathbb{R}^{3}$ is inside the polytope if $\mathbf{F}_{np}\mathbf{x}\leq\mathbf{g}_{np}$. Each time layer $n$ corresponds to the time interval $[t_{0}+n\cdot dt,\;t_{0}+(n{+}1)\cdot dt]$, matching the time interval of trajectory piece $n$. This structure allows the trajectory optimizer to select different spatial corridors at different times, adapting to the evolving obstacle configuration.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A Temporal Corridor Structure", "weight": 1.0} -->

Note that we generate a polytope for every combination of time layer $n$ and path segment $p$, even though some assignments may seem unlikely (e.g., the last time layer in the first path segment, or the first time layer in the last path segment). This is necessary because the MIQP solver determines the piece-to-polytope assignment, and the assignment of pieces is not known a priori. Moreover, as reported in Tables IX and XI, the total STSFC generation time for 10--15 polytopes is only a few milliseconds, so generating polytopes for all combinations adds negligible computational cost.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B Obstacle Inflation by Reachable Radius", "weight": 1.0} -->

For each dynamic obstacle $k$ with estimated position $\hat{\mathbf{c}}_{k}(t_{0})\in\mathbb{R}^{3}$ and each time layer $n$, we compute the worst-case reachable position set by inflating the obstacle's AABB half-extents by the per-layer reachable radius: where $(n{+}1)\cdot dt$ is the end time of layer $n$ (we use the end time rather than the midpoint to ensure that the inflation covers the worst-case obstacle displacement over the *entire* layer), $v^{\mathrm{obs}}_{\max}$ is the maximum obstacle velocity, and $\epsilon\geq 0$ is a bound on the per-axis position estimation error from the obstacle tracker (Section VII). Because $r_{n}$ grows with $n$, obstacles are inflated more in later time layers, reflecting the increasing uncertainty in obstacle position over time.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B Obstacle Inflation by Reachable Radius", "weight": 1.0} -->

The inflated obstacle region for time layer $n$ is the Minkowski sum of the obstacle's estimated AABB with an axis-aligned cube of half-side $r_{n}$: yielding an enlarged AABB with half-extents $\mathbf{h}_{k}+r_{n}\mathbf{1}$ centered at $\hat{\mathbf{c}}_{k}(t_{0})$. In addition to $r_{n}$, a fixed safety margin $r_{\text{margin}}$ (see Table III) is added to the AABB half-extents $\mathbf{h}_{k}$ during obstacle detection (Section VII), providing an additional buffer that absorbs position estimation error and controller tracking error beyond the reachable-set inflation. In practice, this margin allows setting $\epsilon=0$ in $r_{n}$ while still maintaining robustness to estimation and tracking errors, since $r_{\text{margin}}$ serves the same role as a nonzero $\epsilon$ (see Section VIII).

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B Obstacle Inflation by Reachable Radius", "weight": 1.0} -->

The inflated AABB voxels are then used to generate STSFCs for time layer $n$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-C Unknown Space Inflation", "weight": 1.0} -->

SANDO maintains a voxel map that is built incrementally from sensor observations: each voxel is classified as free, occupied, or unknown, where unknown voxels are those that have not yet been observed by the sensor. In such environments, dynamic obstacles may emerge from unknown regions at any time. If these regions are treated as free during corridor generation, the resulting corridors may overlap with space that is actually occupied, violating safety. To address this, SANDO inflates the boundaries of unknown (unobserved) voxels, treating them as occupied during the ellipsoid-based corridor decomposition.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-C Unknown Space Inflation", "weight": 1.0} -->

Specifically, let $\mathcal{U}(t_{0})\subset\mathbb{R}^{3}$ denote the set of unknown voxels at planning time $t_{0}$, and let $\mathcal{B}_{\mathcal{U}}(t_{0})$ denote its boundary voxels. Each boundary voxel is inflated by the same per-layer radius $r_{n}$ used for dynamic obstacles. The inflated unknown region for time layer $n$ is: where $B_{\infty}(r_{n})$ is the $L_{\infty}$-ball of radius $r_{n}$ and $\oplus$ denotes the Minkowski sum. The inflated unknown voxels are included in the obstacle set used for corridor generation, ensuring that any dynamic obstacles that could emerge from these regions are accounted for in the resulting polytopes $\mathcal{C}[n][p]$ (see Fig. 3 Generation ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments")).

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-C Unknown Space Inflation", "weight": 1.0} -->

When the goal lies outside the unknown region (Scenario 1 in Fig. 3 Generation ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments")), the trajectory stays entirely in observed space and the inflated boundary provides a safety buffer against unobserved obstacles.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Safe subgoal selection", "weight": 1.0} -->

When the global path enters the unknown region, corridors cannot be generated beyond the unknown boundary. To handle this, SANDO finds the first point where the global path intersects the unknown boundary and walks back along the path until it reaches a point outside the worst-case inflated unknown region, yielding a new subgoal $G^{\prime}$ (Scenario 2 in Fig. 3 Generation ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments")). The worst-case inflation is computed from the planning horizon, the agent's dynamic constraints, and the maximum time allocation factor (see Section VI-A2) in a given replanning cycle. Since the trajectory to $G^{\prime}$ is shorter than to the original goal, each per-layer $r_{n}$ is smaller, producing less conservative inflation and larger corridors. Note that this is a heuristic: if the global path runs close to the unknown boundary, the walk-back may not find a subgoal fully outside the worst-case inflated region. In practice, however, the reduced trajectory duration sufficiently shrinks $r_{n}$ to yield feasible corridors.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Safe subgoal selection", "weight": 1.0} -->

The resulting STSFCs are used as constraints in the MIQP trajectory optimization described in Section VI. System-level parameters, including $r_{\text{drone}}$, $v^{\mathrm{obs}}_{\max}$, and the replanning rate, are configured per-environment and listed in Section IX.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Heat Map-Based Global Planner", "weight": 1.0} -->

As described in Section IV Generation ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments"), STSFC corridors shrink as dynamic obstacles are inflated by their worst-case reachable sets. If the global path passes close to dynamic obstacles, the resulting corridors may become too small for the trajectory optimizer to find a feasible solution. A naive approach would be to hard-block the entire worst-case reachable set as occupied in the planner's occupancy grid. However, this creates a critical replanning failure mode: at the next replanning step, the agent's current position may fall inside the previously blocked region, since the obstacle has moved and the reachable set has shifted, making the new planning query infeasible (see No Heat Map & No STSFC approach at $t=t_{1}$ in Fig. 4).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Heat Map-Based Global Planner", "weight": 1.0} -->

To avoid this, SANDO employs a heat map-based A^∗^ planner that uses soft costs rather than hard occupancy constraints for dynamic obstacles. The heat map proactively steers the global path away from regions where corridors will shrink, without blocking those regions entirely. This ensures that the global path search always has a feasible start configuration, while still biasing the path toward regions with larger corridors. Static and dynamic obstacles are both incorporated through heat maps, and only known static obstacles and the current location of dynamic obstacles enforce hard infeasibility. These occupied voxels are inflated by the drone radius $r_{\text{drone}}$ (the circumscribed radius of the vehicle) to account for the agent's physical extent. Unknown space is treated as free in the global planner to allow the agent to plan paths toward unexplored regions.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Heat Map-Based Global Planner", "weight": 1.0} -->

In contrast, during STSFC generation, unknown space is treated as occupied, and when unknown-space inflation is enabled, the boundaries of unknown regions are further inflated by the per-layer reachable radius $r_{n}$ so that the resulting corridors account for obstacles that may emerge from unobserved space (see Section IV-C Generation ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments")).

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-A Static Obstacle Heat Map", "weight": 1.0} -->

We define a static heat map $H^{s}:\mathbf{q}\in\mathbb{R}^{3}\to\mathbb{R}_{\geq 0}$ using a distance-based cost that decreases with distance from obstacle surfaces. Only boundary voxels (surface voxels of obstacles) serve as heat sources. For each boundary voxel $b$ with center $\mathbf{c}_{b}$ and halo radius $R^{s}$ (the maximum distance at which the voxel influences the cost), the heat contribution at a query point $\mathbf{q}\in\mathbb{R}^{3}$ is: where $\alpha^{s}$ is the intensity scale and $p^{s}$ controls the decay shape.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-A Static Obstacle Heat Map", "weight": 1.0} -->

The aggregate static heat is $H^{s}(\mathbf{q})=\min(\max_{b}H^{s}_{b}(\mathbf{q}),\,H_{\max})$, using max aggregation to avoid artificially inflating costs in dense obstacle regions, capped at $H_{\max}$ (the maximum allowable heat value). See Table II for the static heat parameters used in our experiments.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-B Dynamic Obstacle Heat Map", "weight": 1.0} -->

For each tracked dynamic obstacle $k$ with estimated position $\hat{\mathbf{c}}_{k}$, AABB half-extents $\mathbf{h}_{k}$, and predicted trajectory $\mu_{k}(t)$ from the obstacle tracker (Section VII) over a prediction time horizon $T_{h}$, we construct a per-obstacle heat $H_{k}(\mathbf{q})$ combining a penalty around the current position and a penalty around the predicted trajectory tube.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Base heat around the current position", "weight": 1.0} -->

We define the base obstacle radius as $R_{0,k}\coloneqq\max_{i}h_{k}^{i}+r_{\text{margin}}$, where $r_{\text{margin}}$ is a fixed safety margin (see Table III), and the horizon-limited reachable radius as $R^{d}_{k}\coloneqq R_{0,k}+v^{\mathrm{obs}}_{\max}T_{h}$. The base heat is: where $\alpha^{d}_{0}$ is the base cost scale and $p^{d}$ controls the decay shape.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Tube penalty from predicted motion", "weight": 1.0} -->

The tube penalty is: where $w(t)=\exp(-t/\tau^{d})$ with $\tau^{d}\coloneqq\tau^{d}_{\text{ratio}}\cdot T_{h}$ is an exponential time weight that discounts predictions further into the future (since they are less reliable), $\tau^{d}_{\text{ratio}}$ is a scaling factor that sets the decay time constant as a fraction of the horizon, $\alpha^{d}_{1}$ scales the tube penalty, and $q^{d}$ controls how sharply the cost increases near the predicted path. The tube radius $R_{k,j}$ grows with time while the time weight $w(t_{j})$ decays: near-future predictions receive high weight over a small region, whereas far-future predictions receive low weight over a larger region. This is a heuristic that balances spatial coverage against prediction reliability, and we found empirically that it produces effective obstacle avoidance paths across a wide range of environments.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Tube penalty from predicted motion", "weight": 1.0} -->

The total per-obstacle heat combines both components: $H_{k}(\mathbf{q})=H^{\mathrm{base}}_{k}(\mathbf{q})+H^{\mathrm{tube}}_{k}(\mathbf{q})$, where $H^{\mathrm{base}}_{k}$ penalizes proximity to the obstacle's current position and $H^{\mathrm{tube}}_{k}$ penalizes proximity to its predicted future path. The dynamic heat across all obstacles is $H^{d}(\mathbf{q})=\max_{k}H_{k}(\mathbf{q})$, using max aggregation so that the most dangerous obstacle dominates the cost.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-C Combined Heat Formulation", "weight": 1.0} -->

Fig. 5 illustrates the combined heat map in a hardware experiment. The combined heat map merges the static and dynamic components via max aggregation: where $H_{\max}$ caps the total heat. Max aggregation avoids double-penalization and ensures the highest risk dominates.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-D A^∗^ with Hard Occupancy and Soft Cost Penalties", "weight": 1.0} -->

Let $\mathcal{G}=(\mathcal{V},\mathcal{E})$ denote the 26-connected voxel graph (i.e., each voxel is connected to all $3^{3}-1=26$ neighbors in its $3\times 3\times 3$ neighborhood), where $\mathcal{V}$ is the set of free voxel centers and $\mathcal{E}$ contains edges between neighboring free voxels. For an edge $(\mathbf{q}_{i},\mathbf{q}_{i+1})\in\mathcal{E}$, the edge cost is: where $d(\mathbf{q}_{i},\mathbf{q}_{i+1})$ is the Euclidean distance between neighboring voxel centers and $w_{\text{heat}}>0$ is a tunable weight that balances the heat penalty against path length.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-D A^∗^ with Hard Occupancy and Soft Cost Penalties", "weight": 1.0} -->

A^∗^ searches for the minimum-cost path from start $\mathbf{q}_{s}$ to goal $\mathbf{q}_{g}$ using the goal-directed heuristic $h(\mathbf{q})=\|\mathbf{q}-\mathbf{q}_{g}\|$, yielding a global path in known-free space that avoids regions near both static and dynamic obstacles.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Heat map parameter selection", "weight": 1.0} -->

The heat map parameters (listed in Table II) influence only the global path quality, not the safety guarantee, which is enforced by the hard STSFC constraints in the trajectory optimizer. A path that passes too close to obstacles may result in small corridors and reduced optimization feasibility, while overly aggressive heat penalties can produce unnecessarily long detours. In practice, we found the same parameter set (Table II) to be effective across all simulation environments without per-scenario tuning. For the hardware experiments, we increased $w_{\text{heat}}$ from 5.0 to 20.0 in the five-obstacle configuration (Experiments 11--16) to account for the smaller physical environment ($8\times 20$ m vs. $100\times 40$ m in simulation), where obstacles occupy a proportionally larger fraction of the space and stronger steering is needed to maintain corridor feasibility.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Trajectory Optimization", "weight": 1.0} -->

Building on the MIQP framework for static environments, SANDO optimizes position trajectories using hard-constraint Mixed-Integer Quadratic Programming (MIQP) extended to dynamic settings with time-varying corridors. Although MIQP introduces binary variables for piece-polytope assignment and increases computational cost relative to soft-constraint methods, it guarantees collision-free trajectories. To reduce complexity, we leverage a variable elimination technique that reduces the number of decision variables by symbolically solving the linear equality constraints, similar to the closed-form reductions in but extended to the MIQP setting (see Section VI-A1 for details). SANDO also incorporates a parallelized time allocation strategy that launches multiple MIQP instances with different time allocations concurrently, selecting the best solution that satisfies all constraints (see Section VI-A2 for details).

<!-- chunk {"id": "body-0056", "role": "body", "section": "VI-A Trajectory Optimization", "weight": 1.0} -->

We formulate trajectory optimization using an $N$-piece composite Bézier curve with $P$ spatial polytopes per time layer. As described in Section IV Generation ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments"), STSFCs in dynamic environments are time-layered, with polytopes indexed by both time layer and spatial location. We reuse $n\in\{0:N-1\}$ and $p\in\{0{:}P-1\}$ from Section IV Generation ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments"): since each trajectory piece $n$ executes during time layer $n$ of the STSFC, the same index identifies both the piece and its corresponding time layer. Similarly, $p$ indexes the spatial polytope within that layer. The time interval $dt$ per piece is uniform and matches the STSFC layer duration.

<!-- chunk {"id": "body-0057", "role": "body", "section": "VI-A Trajectory Optimization", "weight": 1.0} -->

Fig. 4 illustrates this process: the MIQP assigns each trajectory piece to a spatial polytope within its time layer (e.g., $\bm{x}_{0}\subseteq\mathcal{C}$, $\bm{x}_{1}\subseteq\mathcal{C}$), ensuring the trajectory remains in free space both spatially and temporally.

<!-- chunk {"id": "body-0058", "role": "body", "section": "VI-A Trajectory Optimization", "weight": 1.0} -->

The control input, jerk, remains constant within each piece, allowing the position trajectory of each piece to be represented as a cubic polynomial. Note that this implies jerk is discontinuous at piece boundaries; however, cubic polynomial representations are widely adopted in real-time planning: where $\bm{a}_{n},\bm{b}_{n},\bm{c}_{n},\bm{d}_{n}\in\mathbb{R}^{3}$ are the coefficients of the cubic spline in piece $n$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "VI-A Trajectory Optimization", "weight": 1.0} -->

We now discuss the constraints for the optimization formulation. Continuity constraints are added between adjacent pieces to ensure the trajectory is continuous in position, velocity, and acceleration: The Bézier curve control points $\bm{p}_{nj}$ $(j\in\{0{:}3\})$ associated with each piece $n$ are: Since a Bézier curve lies within the convex hull of its control points, constraining all control points to lie inside a convex polytope guarantees that the entire piece remains inside that polytope. To assign pieces to polytopes, we introduce binary variables $z_{np}$, where $z_{np}=1$ if piece $n$ is assigned to polytope $p$, and $z_{np}=0$ otherwise.

<!-- chunk {"id": "body-0060", "role": "body", "section": "VI-A Trajectory Optimization", "weight": 1.0} -->

This condition is enforced through the following constraint: where polytopes are time-layered as described in Section IV Generation ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments"), with $(\mathbf{F}_{np},\mathbf{g}_{np})$ denoting the polytope at time layer corresponding to piece $n$ and spatial index $p$. In dynamic environments, the polytope constraints $\mathbf{F}_{np}$ and $\mathbf{g}_{np}$ vary with both the trajectory piece $n$ (time) and spatial polytope index $p$, reflecting the temporal evolution of free space as obstacles move. Each piece must be assigned to at least one polytope, which is ensured by the constraint: To ensure the trajectory starts at the initial state and ends at the final state, we impose the following constraints: where $\mathbf{x}_{\text{init}}$ is the initial state, and $\mathbf{x}_{\text{final}}$ is the final state.

<!-- chunk {"id": "body-0061", "role": "body", "section": "VI-A Trajectory Optimization", "weight": 1.0} -->

The final state is set to the $(P{+}1)$-th waypoint on the global path with zero velocity and zero acceleration, so that the trajectory spans exactly $P$ path segments and stops at the $(P{+}1)$-th waypoint. Since SANDO replans in a receding horizon manner, only the initial portion of the trajectory is typically executed before a new plan is computed; the agent does not necessarily reach the final stop state of each optimized trajectory.

<!-- chunk {"id": "body-0062", "role": "body", "section": "VI-A Trajectory Optimization", "weight": 1.0} -->

For dynamic constraints, we define the velocity control points $\bm{v}_{nj}$ ($j\in\{0{:}2\}$), acceleration control points $\bm{a}_{nj}$ ($j\in\{0{:}1\}$), and jerk $\bm{j}_{n}$ for each piece $n$. By the convex hull property of Bézier curves, bounding these control points guarantees that the continuous velocity, acceleration, and jerk remain within limits throughout each piece: where $v_{\text{max}}$, $a_{\text{max}}$, and $j_{\text{max}}$ denote the maximum allowable velocity, acceleration, and jerk, respectively.

<!-- chunk {"id": "body-0063", "role": "body", "section": "VI-A1 Variable Elimination", "weight": 1.0} -->

In the MIQP formulation of Eq., each piece $n$ introduces four coefficient vectors ($\bm{a}_{n}$, $\bm{b}_{n}$, $\bm{c}_{n}$, $\bm{d}_{n}$), giving $4N$ decision variables per axis ($x$, $y$, $z$), i.e., $12N$ in 3D. However, the continuity constraints (Eq. ) and boundary conditions (Eq. ) impose $3N+3$ equality constraints per axis: $3(N{-}1)$ from position, velocity, and acceleration continuity at the $N{-}1$ interior piece boundaries, plus $6$ from the initial and final boundary conditions (position, velocity, and acceleration at start and end). By symbolically solving these equality constraints, we can express most coefficients as affine functions of a small set of remaining variables, which reduces the number of decision variables to $N-3$ per axis and removes all equality constraints from the optimization.

<!-- chunk {"id": "body-0064", "role": "body", "section": "VI-A1 Variable Elimination", "weight": 1.0} -->

For instance, with $N=4$ pieces there are $4N=16$ variables and $3N+3=15$ equality constraints per axis, leaving only one decision variable per axis. Symbolic elimination reveals this remaining variable to be $\bm{d}_{3}$ (the first control point of the final piece); all other coefficients become affine functions of $\bm{d}_{3}$. In general, the number of remaining decision variables per axis is $4N-(3N+3)=N-3$; for example, $N=5$ yields 2 and $N=6$ yields 3 per axis, with the same elimination procedure applied. However, the symbolic expressions grow combinatorially with $N$: each remaining variable's affine coefficients depend on all boundary conditions and continuity relations, so the closed-form expressions become prohibitively large for $N>7$. In our implementation, we precompute the symbolic elimination offline for $N\in\{4,5,6,7\}$, which covers the operating range used in all experiments.

<!-- chunk {"id": "body-0065", "role": "body", "section": "VI-A1 Variable Elimination", "weight": 1.0} -->

This leads to a revised MIQP with many fewer decision variables and no equality constraints: This MIQP is solved using Gurobi. Section IX-B performs an ablation study to evaluate the computational benefits of this variable elimination technique, and it demonstrates up to $7.4\times$ reduction in optimization time.

<!-- chunk {"id": "body-0066", "role": "body", "section": "VI-A2 Time Allocation and Parallelization", "weight": 1.0} -->

The time allocated to each trajectory piece strongly affects feasibility and optimality: too short and the dynamical limits are violated, too long and the trajectory is overly slow. Following, SANDO computes a baseline time per piece $dt_{0}$ from the per-axis minimum-time solutions under velocity, acceleration, and jerk limits, and scales it by a factor $f\geq 1$ to obtain the actual time per piece $dt=f\cdot dt_{0}$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "VI-A2 Time Allocation and Parallelization", "weight": 1.0} -->

To search over time allocations efficiently, SANDO maintains a sliding window of $M$ candidate factors $\{f_{1},\ldots,f_{M}\}$ spanning a range of width $2\kappa$ centered on a mean value, with uniform step size $\Delta f$, where $M=\lfloor 2\kappa/\Delta f\rfloor+1$. At each replanning iteration, $M$ MIQP solver threads are launched in parallel, one per factor, each with $dt=f_{i}\cdot dt_{0}$. Since each factor yields a different $dt$, a separate STSFC is generated per thread to reflect the corresponding obstacle inflation radii; the per-thread STSFC computation cost is reported in Sections IX and X. As soon as any thread finds a feasible solution, the remaining threads are terminated and that solution is used.

<!-- chunk {"id": "body-0068", "role": "body", "section": "VI-A2 Time Allocation and Parallelization", "weight": 1.0} -->

The factor window adapts for the next replanning cycle based on the outcome: Success: The window is recentered so that the successful factor becomes the median, biasing the next iteration toward similar time allocations.

<!-- chunk {"id": "body-0069", "role": "body", "section": "VI-A2 Time Allocation and Parallelization", "weight": 1.0} -->

All fail: The window is shifted upward by one step $\Delta f$, increasing the time allocation to improve feasibility. If the window reaches a configurable upper bound $f_{\max}$ (see Table III), it resets to the initial position.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Dynamic Obstacle Detection and Tracking", "weight": 1.0} -->

SANDO detects and tracks dynamic obstacles from raw point cloud data through a multi-stage pipeline.

<!-- chunk {"id": "body-0071", "role": "body", "section": "VII-A Detection via Temporal Occupancy Grid", "weight": 1.0} -->

Inspired by Dynablox, SANDO constructs a temporal occupancy grid to classify voxels as static or dynamic. Voxels that remain occupied beyond a configurable duration are classified as static. When a voxel transitions from free to occupied and has fewer than a threshold number of static neighbors, it is classified as dynamic, indicating a newly appearing moving object rather than part of an existing static structure. Dynamic labels persist for a configurable duration to maintain temporal continuity during brief sensor occlusions. False positives are mitigated by the static-neighbor threshold: voxels adjacent to many static voxels are not classified as dynamic, preventing edges of static structures from being misidentified as moving objects.

<!-- chunk {"id": "body-0072", "role": "body", "section": "VII-B Clustering and Data Association", "weight": 1.0} -->

Dynamic voxels are grouped into clusters using Euclidean clustering. For each cluster, the centroid and AABB half-extents are computed. Since onboard sensors typically observe only one face of an obstacle, the AABB is inflated to a cubic shape using the largest observed dimension, providing a conservative size estimate for collision avoidance. Clusters are associated with existing tracks via nearest-neighbor matching within a distance threshold; unmatched clusters initialize new tracks. Nearest-neighbor association can produce incorrect matches when obstacle trajectories cross or obstacles are closely spaced; however, the tracker is a modular component and can be replaced with more sophisticated methods (e.g., the Hungarian algorithm) without changing the planning framework.

<!-- chunk {"id": "body-0073", "role": "body", "section": "VII-C Adaptive Extended Kalman Filter (AEKF)", "weight": 1.0} -->

Each tracked obstacle $k$ is modeled with a 9-state vector $\mathbf{x}_{k}=[\mathbf{p}_{k}^{\top},\,\mathbf{v}_{k}^{\top},\,\mathbf{a}_{k}^{\top}]^{\top}$, where $\mathbf{p}_{k}$, $\mathbf{v}_{k}$, and $\mathbf{a}_{k}$ denote the obstacle's position, velocity, and acceleration, using a constant-acceleration process model. The measurement is the cluster centroid (position only).

<!-- chunk {"id": "body-0074", "role": "body", "section": "VII-C Adaptive Extended Kalman Filter (AEKF)", "weight": 1.0} -->

To handle unknown and time-varying noise characteristics, we employ an AEKF that continuously updates both the measurement noise covariance $R_{i}$ and the process noise covariance $Q_{i}$ at each filter step $i$ using exponential forgetting with factor $\alpha$: where $\epsilon_{i}$ is the residual, $d_{i}$ is the innovation, and $K_{i}$ is the Kalman gain. When a new obstacle is detected, its initial $Q_{0}$ and $R_{0}$ are set to the average of the covariances from existing tracks, allowing the filter to use prior knowledge of the environment's noise characteristics.

<!-- chunk {"id": "body-0075", "role": "body", "section": "VII-D Prediction and Output", "weight": 1.0} -->

Future positions are predicted using a constant-velocity model with the AEKF-estimated velocity. Although the AEKF uses a constant-acceleration process model for state estimation, we use constant-velocity for prediction because acceleration estimates are noisy and change rapidly, making them unreliable over longer prediction horizons; constant-velocity extrapolation is more robust in practice. For each tracked obstacle, the system publishes the predicted trajectory and AABB half-extents. Tracks that are not updated for a configurable timeout are deleted, allowing the system to discard obstacles that have left the sensor's field of view or stopped moving. The predicted trajectories and reachable sets are then used by the heat map-based global planner (Section V) and STSFC generator (Section IV Generation ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments")).

<!-- chunk {"id": "body-0076", "role": "body", "section": "Safety Analysis", "weight": 1.0} -->

SANDO provides formal collision-free guarantees through its STSFC framework. Using the notation introduced in Section IV Generation ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments"), we recall that the per-layer inflation radius is: where the first term accounts for worst-case obstacle displacement from $t_{0}$ to $t_{0}+(n{+}1)\cdot dt$, and $\epsilon$ accounts for the position estimation error (see Assumption 2 ‣ VIII-A Assumptions ‣ VIII Safety Analysis ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments")).

<!-- chunk {"id": "body-0077", "role": "body", "section": "Assumption 2 (Bounded position estimation error)", "weight": 1.0} -->

The obstacle tracker provides an estimated position $\hat{\mathbf{c}}_{k}(t_{0})$ of each obstacle at the planning time $t_{0}$. There exists a known constant $\epsilon\geq 0$ such that: That is, the per-axis estimation error is bounded by $\epsilon$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Assumption 3 (Perfect trajectory tracking)", "weight": 1.0} -->

The low-level controller tracks the planned trajectory exactly, i.e., the executed position coincides with the planned position at all times.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Assumption 3 (Perfect trajectory tracking)", "weight": 1.0} -->

In practice, Assumptions 2 ‣ VIII-A Assumptions ‣ VIII Safety Analysis ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments") and 3 ‣ VIII-A Assumptions ‣ VIII Safety Analysis ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments") are not satisfied exactly. However, the safety margin $r_{\text{margin}}$ (see Table III), which is added to each obstacle's AABB half-extents during detection, provides an additional buffer beyond the reachable-set inflation $r_{n}$. This margin absorbs both position estimation errors and controller tracking errors: when $r_{\text{margin}}$ exceeds the combined worst-case estimation and tracking error, one can set $\epsilon=0$ in Eq. and still maintain the safety guarantee. In all experiments, we set $\epsilon=0$ and rely on $r_{\text{margin}}$ (0.1 m in simulation, 0.2 m in hardware) together with the drone radius $r_{\text{drone}}$ to absorb these errors. The larger hardware margin accounts for the greater tracking errors observed on the physical platform.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Assumption 4 (Untracked obstacles in unknown space)", "weight": 1.0} -->

Let $\mathcal{U}(t_{0})\subset\mathbb{R}^{3}$ denote the set of unobserved (unknown) voxels at the planning time $t_{0}$. Any dynamic obstacle that is not currently tracked by the obstacle tracker is located entirely within $\mathcal{U}(t_{0})$ at time $t_{0}$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "VIII-B Corridor Construction", "weight": 1.0} -->

As described in Section IV Generation ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments"), each dynamic obstacle $k$ is inflated by $r_{n}$ (Eq. ) to obtain $\hat{\mathcal{O}}_{k}^{n}$, and when unknown-space inflation is enabled, the unknown region boundary is inflated by the same radius to obtain $\hat{\mathcal{U}}^{n}$ (Section IV-C Generation ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments")).

<!-- chunk {"id": "body-0082", "role": "body", "section": "MIQP polytope assignment", "weight": 1.0} -->

As described in Section VI, the MIQP assigns each piece $n$ to a polytope $\mathcal{C}[n][p_{n}^{*}]$ such that all four control points lie inside (Eq. ). By the convex hull property of Bézier curves, the entire piece therefore remains inside $\mathcal{C}[n][p_{n}^{*}]$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Role of agent and obstacle velocities in the inflation radius", "weight": 1.0} -->

The inflation radius $r_{n}=v^{\mathrm{obs}}_{\max}\cdot(n{+}1)\cdot dt+\epsilon$ depends on both the obstacle velocity bound $v^{\mathrm{obs}}_{\max}$ and the per-piece duration $dt$. As described in Section VI-A2, $dt=f\cdot dt_{0}$, where $dt_{0}$ is the minimum feasible time per piece derived from the agent's dynamic constraints ($v_{\max}$, $a_{\max}$, $j_{\max}$) and $f\geq 1$ is the time allocation factor. Hence, tighter agent dynamic constraints reduce $dt_{0}$ and consequently $dt$, which shrinks $r_{n}$ and produces larger corridors. Conversely, a higher $v^{\mathrm{obs}}_{\max}$ increases $r_{n}$, requiring more conservative corridors and potentially reducing feasibility in dense environments.

<!-- chunk {"id": "body-0084", "role": "body", "section": "VIII-D When Assumptions Are Violated", "weight": 1.0} -->

The safety guarantee of Theorem 1 ‣ VIII-C Safety ‣ VIII Safety Analysis ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments") depends on both assumptions and the corridor construction properties.

<!-- chunk {"id": "body-0085", "role": "body", "section": "VIII-D When Assumptions Are Violated", "weight": 1.0} -->

Velocity bound violated: If an obstacle exceeds $v^{\mathrm{obs}}_{\max}$ along any axis, its true position at time $t$ can lie outside the inflated box $\hat{\mathcal{O}}_{k}^{n}$. The corridor remains obstacle-free with respect to the inflated region, but the true obstacle may have moved into the corridor. As $v^{\mathrm{obs}}_{\max}$ increases, the per-layer inflation radius $r_{n}$ grows linearly, shrinking the STSFC corridors and eventually making trajectory optimization infeasible. For very fast obstacles, the planner would need to rely more heavily on trajectory prediction to tighten the inflation (inflating around the predicted future position rather than the worst-case reachable set from the current position), which is an avenue for future work.

<!-- chunk {"id": "body-0086", "role": "body", "section": "VIII-D When Assumptions Are Violated", "weight": 1.0} -->

Estimation error exceeded: The total buffer available to absorb estimation error is $\epsilon+r_{\text{margin}}$. In our experiments, $\epsilon=0$ and $r_{\text{margin}}\in\{0.1,0.2\}$ m, so safety is maintained as long as the per-axis estimation error does not exceed $r_{\text{margin}}$. If the actual error exceeds this margin, the inflated region may not fully contain the true obstacle, and collisions become possible. Users can increase either $\epsilon$ or $r_{\text{margin}}$ to accommodate larger estimation errors at the cost of more conservative corridors.

<!-- chunk {"id": "body-0087", "role": "body", "section": "VIII-D When Assumptions Are Violated", "weight": 1.0} -->

Tracking error: If the low-level controller does not track the planned trajectory perfectly, the actual position may deviate from the planned position. Even though the planned trajectory lies inside the corridor, the actual trajectory may exit the corridor and potentially collide with obstacles. In practice, tracking errors are absorbed by the drone radius $r_{\text{drone}}$ and the safety margin $r_{\text{margin}}$, which together provide a spatial buffer between the corridor boundary and the obstacle surface.

<!-- chunk {"id": "body-0088", "role": "body", "section": "VIII-D When Assumptions Are Violated", "weight": 1.0} -->

Unknown-space inflation disabled: When unknown-space inflation is disabled, the safety guarantee of Theorem 1 ‣ VIII-C Safety ‣ VIII Safety Analysis ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments") covers only tracked dynamic obstacles. Untracked dynamic obstacles emerging from unobserved space are not represented in the corridor generation, and the trajectory may enter regions where such obstacles are present.

<!-- chunk {"id": "body-0089", "role": "body", "section": "VIII-D When Assumptions Are Violated", "weight": 1.0} -->

Note that safety is guaranteed only within the local planning horizon $N\cdot dt$; long-term safety requires continuous replanning, as discussed in Section VIII-E.

<!-- chunk {"id": "body-0090", "role": "body", "section": "VIII-E Recursive Feasibility", "weight": 1.0} -->

Recursive feasibility means that if a feasible trajectory exists at the current replanning step, one will also exist at the next step. OA-MPC and Stamouli et al. guarantee this for MPC in dynamic environments using a *shrinking horizon* tied to a fixed mission duration $T$, so the remaining planning time decreases at each step. Because the horizon shrinks toward the same end time $T$, the obstacle's reachable sets do not grow between replanning steps, and the previous plan remains feasible for the next step. However, this strategy is not suitable for long-duration navigation where the goal may be far from the agent and the mission duration is not fixed.

<!-- chunk {"id": "body-0091", "role": "body", "section": "VIII-E Recursive Feasibility", "weight": 1.0} -->

SANDO could adopt the same strategy if the goal were close enough to be reached within a single planning horizon, but this is not generally the case for long-range navigation. As described in Section III, SANDO replans in a receding horizon manner toward a subgoal that moves with the agent. Since the subgoal moves with the agent and the horizon does not shrink toward a fixed end time, the assumptions required for recursive feasibility do not hold. One alternative is to adopt the approach of Wu et al. when the agent reaches a subgoal but cannot find a new trajectory. Ref. guarantees infinite-horizon safety by allowing the agent to fly away from obstacles, but this requires the agent to be faster than all obstacles and the environment to be open, which is unrealistic in cluttered settings.

<!-- chunk {"id": "body-0092", "role": "body", "section": "VIII-E Recursive Feasibility", "weight": 1.0} -->

Theorem 1 ‣ VIII-C Safety ‣ VIII Safety Analysis ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments") guarantees collision-free execution within each individual planning horizon, but SANDO generally does not guarantee that a feasible plan will exist at every future replanning step due to the receding horizon nature where we use a different subgoal at each step. However, as shown in simulations in Section IX and hardware experiments in Section X, SANDO often finds new trajectories before reaching the end of the current plan, effectively maintaining safety through continuous replanning even without formal recursive feasibility guarantees.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

We performed all the simulations on an AlienWare Aurora R8 desktop computer with an Intel^®^ Core ^TM^ i9 CPU $\times$`<!-- -->`{=html}16, 64 GB of RAM. The operating system is Ubuntu 22.04 LTS, and we used ROS2 Humble for SANDO's implementation. Other methods were implemented in ROS1 Noetic/Melodic, so we dockerized them and ran them in ROS1 Noetic/Melodic on the same machine for benchmarking. Table II lists the SANDO system parameters that remain fixed across all simulations, and Table III summarizes the per-experiment configuration parameters for both simulation and hardware experiments (Section X). For all baseline methods, we used their default parameter values (planning horizon, number of trajectory pieces, etc.), with one exception: in the static forest benchmark, EGO-Swarm2's default planning horizon of 7.5 m caused frequent collisions even in the easy environment, so we increased it to 20.0 m to achieve a higher success rate (see Table VI).

<!-- chunk {"id": "body-0094", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

Static Heat Map Dynamic Heat Map Base cost scale Tube penalty scale Tube growth rate Time weight ratio Factor step size AEKF forgetting factor TABLE II: SANDO system parameters across all simulations.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

Standardized (Sec. IX-A, IX-B) Static Forest (Sec. IX-C) Dynamic w/ GT (Sec. IX-D, IX-E) Dynamic w/o GT (Sec. IX-F) Polytopes per layer P Drone radius rdrone [m] Max obs. velocity vmaxobs [m/s] A∗ heat weight wheat Safety margin rmargin [m] Max time factor fmax Unknown space inflation TABLE III: Per-experiment SANDO configuration. “N/A” indicates the parameter is not applicable.

<!-- chunk {"id": "body-0096", "role": "body", "section": "IX-A Benchmarking in Standardized Static Environments", "weight": 1.0} -->

To compare SANDO against state-of-the-art methods, we first performed benchmarking experiments in a standardized static environment, as shown in Fig. 6. We evaluated 61 cases by varying the goal position from $-3$ to $3$ m in $0.1$ m increments along the $y$-axis. For fair comparison, we used the same start and goal positions, dynamic constraints, and safe flight corridor constraints.

<!-- chunk {"id": "body-0097", "role": "body", "section": "IX-A Benchmarking in Standardized Static Environments", "weight": 1.0} -->

Since this benchmark has no dynamic obstacles, SANDO uses spatial safe flight corridors (SSFCs) rather than STSFCs; an SSFC is a single-time-layer STSFC (i.e., $\mathcal{C}[p]$ only), identical to FASTER's corridor generation, since obstacle positions do not change over time. FASTER uses MIQP-based hard constraints, while SUPER uses soft constraints. SANDO and FASTER use Gurobi as the MIQP solver, while SUPER uses LBFGS as the soft-constraint solver. For a fair comparison, we relaxed SUPER to use per-axis dynamic constraints ($L_{\infty}$ norm), since SANDO and FASTER enforce per-axis constraints. FASTER only applies dynamic constraints at the very first control points of each piece, so we also report the results of FASTER with additional dynamic constraints at all control points, denoted as FASTER (CP). The original FASTER is denoted as FASTER (orig.). For SANDO and FASTER, we set the number of pieces from 4 to 6.

<!-- chunk {"id": "body-0098", "role": "body", "section": "IX-A Benchmarking in Standardized Static Environments", "weight": 1.0} -->

The metrics used in the table are defined as follows.

<!-- chunk {"id": "body-0099", "role": "body", "section": "IX-A Benchmarking in Standardized Static Environments", "weight": 1.0} -->

$R^{\mathrm{opt}}_{\mathrm{succ}}$ \[%\] (optimization success rate; optimization completes without failure); $T^{\mathrm{per}}_{\mathrm{opt}}$ \[ms\] (per-optimization runtime; since SANDO and FASTER perform iterative time allocation and trajectory optimization, we report the average runtime of each individual optimization); $T^{\mathrm{total}}_{\mathrm{opt}}$ \[ms\] (total optimization runtime); $T_{\mathrm{trav}}$ \[s\] (trajectory travel time); $L_{\mathrm{path}}$ \[m\] (total path length); $S_{\mathrm{jerk}}=\!\int_{0}^{T_{\mathrm{trav}}}\!\lVert\mathbf{j}(t)\rVert\,dt$ \[m/s^2^\] (L1 jerk integral, where

<!-- chunk {"id": "body-0100", "role": "body", "section": "IX-A Benchmarking in Standardized Static Environments", "weight": 1.0} -->

$\mathbf{j}(t)=\dddot{\mathbf{p}}(t)$ is the trajectory jerk; smoothness); $\rho_{\mathrm{sfc}},\,\rho_{\mathrm{vel},}\,\rho_{\mathrm{acc}},\,\rho_{\mathrm{jerk}}$ \[%\] (SFC/velocity/acceleration/jerk constraint violation rates; the percentage of trajectory points that violate the respective constraints, with $\rho_{\mathrm{acc/jerk}}$ denoting the combined acceleration and jerk violation rate when reported jointly).

<!-- chunk {"id": "body-0101", "role": "body", "section": "IX-A Benchmarking in Standardized Static Environments", "weight": 1.0} -->

Unlike SANDO and FASTER, SUPER optimizes spatial trajectories combined with temporal allocation in a single optimization problem, so we report the per-optimization runtime as the total optimization runtime since it does not have iterative time allocation. FASTER and SUPER have two trajectory optimization approaches (exploratory and safe), but for this benchmarking we only report the exploratory trajectory optimization since it yields better performance. SUPER and SANDO use multi-threading for parallel optimization, while FASTER is single-threaded. We report both single-threaded and multi-threaded results for SANDO to show the benefit of multi-threading.

<!-- chunk {"id": "body-0102", "role": "body", "section": "IX-A Benchmarking in Standardized Static Environments", "weight": 1.0} -->

Table IV summarizes the benchmarking results. As $N$ increases, both SANDO and FASTER achieve better trajectory performance (shorter travel time) at the cost of increased computation time, since trajectories with more segments have larger degrees of freedom. Note that FASTER (orig.) achieves fastest travel time at $N=5$ but with a high velocity violation rate of $38.0\text{\,}\%$, while FASTER (CP) achieves zero velocity violation since it applies dynamic constraints at all control points.

<!-- chunk {"id": "body-0103", "role": "body", "section": "IX-A Benchmarking in Standardized Static Environments", "weight": 1.0} -->

Multi-threaded SANDO incurs a slightly higher per-optimization time $T^{\mathrm{per}}_{\mathrm{opt}}$ than single-threaded due to thread overhead (e.g., 6.8 vs. 6.1 ms at $N\!=\!5$, 17.2 vs. 16.1 ms at $N\!=\!6$), but achieves substantially faster total optimization time $T^{\mathrm{total}}_{\mathrm{opt}}$ due to parallel execution (e.g., 9.7 vs. 18.2 ms at $N\!=\!5$, 19.7 vs. 28.0 ms at $N\!=\!6$). No method exhibited acceleration or jerk constraint violations. SUPER reports SFC and velocity constraint violations because it uses soft constraints; however, it achieves fastest computation time while performing spatiotemporal optimization. Compared to FASTER, SANDO achieves consistently faster computation across all $N$ while maintaining the same trajectory performance and no constraint violations.

<!-- chunk {"id": "body-0104", "role": "body", "section": "IX-A Benchmarking in Standardized Static Environments", "weight": 1.0} -->

Overall, SUPER achieves the fastest computation time due to its MINCO-based spatiotemporal optimization, but at the cost of constraint violations. Among hard-constraint methods, SANDO and FASTER (CP) achieve the best trajectory performance with zero constraint violations, and SANDO is consistently computationally faster than FASTER across all $N$, especially with multi-threading. These results illustrate the fundamental trade-off between $N$ (and similarly $P$) and computational cost: larger $N$ and $P$ increase the MIQP's degrees of freedom and the number of binary assignment variables ($N\times P$), improving trajectory quality but increasing solve time. In dynamic environments where fast replanning is critical, we use $N=5$ and $P\in\{2,3\}$ as a practical operating point that balances trajectory quality against real-time computation (see Table III).

<!-- chunk {"id": "body-0105", "role": "body", "section": "IX-B Effectiveness of Variable Elimination", "weight": 1.0} -->

We also benchmarked SANDO with and without variable elimination (VE) (see Section VI-A1) to evaluate the effectiveness of the technique. The benchmark was performed in the same standardized static environment with $N=4,5,6$ with multi-threaded SANDO under the same dynamic constraints as in Section IX-A. Table V summarizes the results. The metrics used in the table are the same as those in Section IX-A except that we report all the constraint violation rates as a single value $\rho_{\mathrm{viol}}$ \[%\] (the maximum rate among SFC/velocity/acceleration/jerk constraint violations). VE achieves identical trajectory performance to the non-VE baseline across all $N$ while reducing per-optimization time by up to $7.4\times$, confirming that, as expected, variable elimination reduces computation time while producing the same optimal solution since the underlying optimization problem is equivalent. This is because VE reduces the number of decision variables and constraints in the MIQP while effectively solving the original problem, so the same optimal solution is obtained with much faster computation.

<!-- chunk {"id": "body-0106", "role": "body", "section": "IX-C Benchmarking against State-of-the-Art Methods in Static Environments", "weight": 1.0} -->

To evaluate SANDO's full planning pipeline in realistic settings, we benchmarked it against state-of-the-art methods in obstacle-rich static forest environments at three difficulty levels. Static cylindrical obstacles (radius 1.0--1.5 m, height 6 m) were placed randomly, occupying a $$100\text{\,}\mathrm{m}$\times$40\text{\,}\mathrm{m}$$ area (Fig. 7). Three difficulty levels are defined by the fraction of the area occupied by obstacles: Easy (5%), Medium (10%), and Hard (20%). The agent starts at \mathrm{m}$$ and the goal is \mathrm{m}$$.

<!-- chunk {"id": "body-0107", "role": "body", "section": "IX-C Benchmarking against State-of-the-Art Methods in Static Environments", "weight": 1.0} -->

We benchmarked SANDO against EGO-Swarm2, SUPER, and FASTER. To simulate LiDAR data, we used the livox_ros_driver2 package, which provides a ROS 2 interface for the Livox MID-360 LiDAR sensor; all methods receive the same sensor data for fair comparison. The dynamic constraints were set to $\bm{{v_{\text{max}}}}=5.0$ $\text{\,}\mathrm{m}\mathrm{/}\mathrm{s}$, $\bm{{a_{\text{max}}}}=20.0$ $\text{\,}\mathrm{m}\mathrm{/}\mathrm{s}\mathrm{{}^{2}}$, and $\bm{{j_{\text{max}}}}=100.0$ $\text{\,}\mathrm{m}\mathrm{/}\mathrm{s}\mathrm{{}^{3}}$.

<!-- chunk {"id": "body-0108", "role": "body", "section": "IX-C Benchmarking against State-of-the-Art Methods in Static Environments", "weight": 1.0} -->

SANDO and FASTER enforce hard $L_{\infty}$ dynamic constraints, while EGO-Swarm2 and SUPER use soft constraints. EGO-Swarm2 and SUPER originally use $L_{2}$ norms for dynamic constraints, but we relaxed them to $L_{\infty}$ norms for fair comparison since SANDO and FASTER enforce per-axis constraints. We performed 10 simulations per difficulty level with the same evaluation metrics in Section IX-A with the addition of $R_{\mathrm{succ}}$ \[%\] (overall success rate; the percentage of runs in which the agent reaches the goal without collision) and $T_{\mathrm{replan}}$ \[ms\] (total replanning computation time). Fig. 8 shows a visualization of one of SANDO's simulation runs in RViz.

<!-- chunk {"id": "body-0109", "role": "body", "section": "IX-C Benchmarking against State-of-the-Art Methods in Static Environments", "weight": 1.0} -->

Table VI summarizes the results. SANDO achieves a 100% success rate across all difficulty levels, whereas FASTER drops to 90% and 70% in the medium and hard cases, respectively, and EGO-Swarm2 drops to 50--60% in the hard case. SANDO also achieves the fastest travel time and the lowest total optimization computation time $T^{\mathrm{total}}_{\mathrm{opt}}$ across all cases. Since SUPER and FASTER use both safe and exploratory trajectory optimization, we report the computation time of both trajectories in $T^{\mathrm{total}}_{\mathrm{opt}}$. SANDO maintains no constraint violations in velocity, acceleration, and jerk owing to its hard-constraint formulation. Although FASTER also enforces hard constraints, it exhibits velocity violations of 7.9% in the hard case, likely due to the constraints only being applied at the first control point of each piece. SUPER shows high jerk violation rates (8--12.7%) because its soft-constraint solver does not strictly enforce dynamic limits.

<!-- chunk {"id": "body-0110", "role": "body", "section": "IX-C Benchmarking against State-of-the-Art Methods in Static Environments", "weight": 1.0} -->

Similarly, EGO-Swarm2 exhibits velocity violations (3--8.6%) due to its soft-constraint optimization. In terms of smoothness, SANDO's jerk integral $S_{\mathrm{jerk}}$ is lower than SUPER's and FASTER's, but higher than EGO-Swarm2's. Overall, SANDO achieves the best overall performance with the highest success rate, fastest travel time, and no constraint violations across all difficulty levels.

<!-- chunk {"id": "body-0111", "role": "body", "section": "IX-D SANDO in Dynamic Environments", "weight": 1.0} -->

We next evaluated SANDO in environments containing both static and dynamic obstacles to test its spatiotemporal collision avoidance capability. The environment spans a $$100\text{\,}\mathrm{m}$\times$40\text{\,}\mathrm{m}$$ forest area populated with static cylindrical obstacles and dynamic obstacles modeled as $0.8\text{\,}\mathrm{m}$ cubes following trefoil knot trajectories with randomized parameters (position, scale, speed, and time offset) (Fig. 9). Three difficulty levels are defined: Easy (50 obstacles, ${\sim}33$ dynamic), Medium (100 obstacles, ${\sim}65$ dynamic), and Hard (200 obstacles, ${\sim}130$ dynamic), with approximately 65% of obstacles being dynamic. The agent starts at \mathrm{m}$$ with a goal at \mathrm{m}$$.

<!-- chunk {"id": "body-0112", "role": "body", "section": "IX-D SANDO in Dynamic Environments", "weight": 1.0} -->

Constraint violations for all methods are evaluated against the shared limits $v_{\max}=5$ $\text{\,}\mathrm{m}\mathrm{/}\mathrm{s}$ and $a_{\max}=20$ $\text{\,}\mathrm{m}\mathrm{/}\mathrm{s}\mathrm{{}^{2}}$. Each method uses different inputs for dynamic obstacles. For instance, EGO-Swarm2 does not have a built-in dynamic obstacle estimator/predictor, but I-MPC and FAPP have built-in estimators/predictors. For a fair comparison, we feed the ground truth positions and future predictions of dynamic obstacles to EGO-Swarm2 since it only receives a quintic polynomial prediction of each dynamic obstacle with a clearance radius. For I-MPC, we feed the ground truth positions, velocities, and sizes of dynamic obstacles since that is what their built-in fake_detector provides. For FAPP, we also feed the ground truth positions and velocities.

<!-- chunk {"id": "body-0113", "role": "body", "section": "IX-D SANDO in Dynamic Environments", "weight": 1.0} -->

FAPP uses a fixed squared-distance threshold of $1.96\text{\,}{\mathrm{m}}^{2}$ in its obstacle avoidance cost, corresponding to an effective avoidance radius of $\sqrt{1.96}\approx 1.4\,\mathrm{m}$ from the obstacle center regardless of the actual obstacle size; i.e., it does not adapt per obstacle. In contrast, for this benchmarking, SANDO receives only the current position of dynamic obstacles, and hence SANDO receives the least information about dynamic obstacles compared to other methods.

<!-- chunk {"id": "body-0114", "role": "body", "section": "IX-D SANDO in Dynamic Environments", "weight": 1.0} -->

Table VII summarizes the results, and Fig. 10 shows a visualization of one of SANDO's simulation runs in RViz. SANDO achieves a 100% success rate across all difficulty levels, while all other methods exhibit failures in one or more cases. SANDO ($P$=3) also achieves the shortest path length in all cases and the fastest travel time in easy and hard. Most notably, SANDO maintains zero constraint violations in velocity, acceleration, and jerk across all cases, demonstrating that hard constraints in the MIQP formulation reliably enforce dynamic feasibility even in dense dynamic environments. EGO-Swarm2 achieves 100% success in easy and medium but drops to 80% in hard, with velocity violations of 5.1--11.8% across all cases. FAPP achieves 80% success in easy and medium and 50% in hard, with small velocity violations (3.1--8.1%) and no acceleration or jerk violations. Among I-MPC variants, lower velocity and acceleration limits reduce constraint violations, while higher limits lead to constraint violations without improved success rates. I-MPC's jerk violations are reported as "-" because it does not enforce jerk constraints.

<!-- chunk {"id": "body-0115", "role": "body", "section": "IX-D SANDO in Dynamic Environments", "weight": 1.0} -->

These results show that SANDO's STSFC approach with worst-case reachable set inflation maintains safety under the most conservative obstacle information assumption.

<!-- chunk {"id": "body-0116", "role": "body", "section": "IX-E STSFC Ablation", "weight": 1.0} -->

To evaluate the effectiveness of the STSFC approach, we compared it against a worst-case baseline that inflates all dynamic obstacles by the maximum time horizon. The STSFC approach inflates obstacles per layer using $r_{n}=v^{\mathrm{obs}}_{\max}\cdot(n{+}1)\cdot dt+\epsilon$, where $(n{+}1)\cdot dt$ is the end time of layer $n$ (Section IV Generation ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments")), whereas the worst-case baseline uses $r=v^{\mathrm{obs}}_{\max}\cdot T_{\text{traj}}+\epsilon$ for all layers, where $T_{\text{traj}}=N\cdot dt$ is the total trajectory duration.

<!-- chunk {"id": "body-0117", "role": "body", "section": "IX-E STSFC Ablation", "weight": 1.0} -->

We conducted the comparison in the Hard dynamic environment from Section IX-D at two maximum velocities ($v_{\max}=2.5$ and $5.0$ m/s) to examine how corridor inflation interacts with agent speed.

<!-- chunk {"id": "body-0118", "role": "body", "section": "IX-E STSFC Ablation", "weight": 1.0} -->

Table VIII summarizes the results. At $v_{\max}=2.5$ m/s, the worst-case baseline achieves only 80% success rate because the large uniform inflation radius results in replanning failures and stoppage when the agent gets hit by dynamic obstacles. The STSFC approach maintains a 100% success rate by inflating obstacles proportionally to each time layer, preserving more free space in earlier layers while still guaranteeing safety. STSFC also achieves substantially lower computation time (8.9 vs. 15.5 ms), faster travel time (43.8 vs. 58.8 s), and a much smoother trajectory (jerk integral 330.6 vs. 1392.2 m/s^2^). At $v_{\max}=5.0$ m/s, both approaches achieve 100% success, as the faster trajectory (and hence shorter traversal time) reduces the worst-case inflation radius and allows the worst-case approach to succeed without many replanning failures.

<!-- chunk {"id": "body-0119", "role": "body", "section": "IX-E STSFC Ablation", "weight": 1.0} -->

Nevertheless, STSFC still provides lower computation time (5.0 vs. 6.4 ms), faster travel time (22.7 vs. 23.5 s), and a smoother trajectory (jerk integral 669.6 vs. 753.3 m/s^2^) than the worst-case baseline.

<!-- chunk {"id": "body-0120", "role": "body", "section": "IX-F Dynamic Environments without Ground Truth Obstacle Knowledge", "weight": 1.0} -->

The dynamic benchmarks in Sections IX-D and IX-E provide all methods with ground truth obstacle information for fair comparison. In practice, however, this information is not available. This section evaluates SANDO in the same dynamic environments but without any ground truth obstacle knowledge, testing the full perception-to-planning pipeline.

<!-- chunk {"id": "body-0121", "role": "body", "section": "IX-F Dynamic Environments without Ground Truth Obstacle Knowledge", "weight": 1.0} -->

The environment, obstacle configuration, dynamic constraints, start/goal positions, and trial settings are identical to those in Section IX-D. For sensing, we used a simulated Intel RealSense D435 depth camera (via the realsense-ros package) rather than the Livox MID-360 LiDAR used in the static benchmarks, because the simulated LiDAR produces too few points on the small dynamic obstacles for reliable detection. This is a simulation artifact; in hardware experiments (Section X), the real LiDAR sensor provides sufficient point density for dynamic obstacle detection. Point clouds are processed by the temporal occupancy grid and AEKF-based dynamic obstacle tracker (Section VII); the planner receives only estimated obstacle positions, bounding boxes, and predicted trajectories rather than ground truth. We evaluated two spatial polytope configurations ($P=2$ and $P=3$).

<!-- chunk {"id": "body-0122", "role": "body", "section": "IX-F Dynamic Environments without Ground Truth Obstacle Knowledge", "weight": 1.0} -->

Table IX summarizes the results, where $T_{\mathrm{STSFC}}$ denotes the spatiotemporal safe flight corridor generation time. $P=2$ generally achieves faster per-optimization time (3.0--4.6 ms vs. 4.6--8.5 ms for $P=3$), while $P=3$ produces smoother trajectories with lower jerk integrals. In the easy case, both configurations achieve high success rates (93% for $P=2$, 95% for $P=3$). In the medium case, $P=2$ achieves 90% while $P=3$ drops to 86%. In the hard case, success rates are 64% ($P=2$) and 51% ($P=3$). This is likely because a shorter replanning horizon and faster computation time with $P=2$ allows more frequent replanning and quicker reactions to unexpected obstacles, which is beneficial in dense dynamic environments where perception uncertainty is high. Neither configuration produced any constraint violations across all difficulty levels.

<!-- chunk {"id": "body-0123", "role": "body", "section": "IX-F Dynamic Environments without Ground Truth Obstacle Knowledge", "weight": 1.0} -->

Compared to the ground-truth results in Section IX-D, where SANDO achieves 100% success across all difficulties, the perception-only gap is small in the easy case (93--95% vs. 100%) but becomes larger in medium (86--90% vs. 100%) and hard (51--64% vs. 100%) cases. The primary failure mode is late detection of dynamic obstacles: when obstacles are not detected until they are close to the agent, the planner has insufficient time to generate a collision-free trajectory, resulting in collisions. This highlights the challenge of perception uncertainty in dense dynamic environments. Nevertheless, these results confirm that SANDO can maintain a high success rate even without any ground truth obstacle information, showcasing the robustness of its full perception-to-planning pipeline in dynamic environments.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Hardware Experiments", "weight": 1.0} -->

To evaluate the performance of SANDO, we conducted hardware experiments in static and dynamic environments. Fig. 11 shows the UAV platform used in our experiments. For perception, we use a Livox Mid-360 LiDAR sensor, and for localization, we use onboard DLIO. SANDO runs on an Intel^™^ NUC 13 with an Intel^®^ Core ^TM^ i7 CPU $\times$`<!-- -->`{=html}16, 64 GB of RAM, and for low-level control, we use PX4 on a Pixhawk flight controller. All perception, planning, control, and localization modules run onboard in real time, enabling fully autonomous operations. As summarized in Table III, we use $w_{\text{heat}}=5.0$ for Experiments 7--10 (single obstacle) and increase it to $w_{\text{heat}}=20.0$ for Experiments 11--16 (five obstacles) to account for the higher collision risk in denser environments.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Hardware Experiments", "weight": 1.0} -->

We also disabled unknown space inflation for the hardware experiments because the MID-360's field of view has many blind spots, and inflating unknown space results in excessive conservatism close to the UAV and prevents it from finding any feasible trajectory. As noted in Section VIII, with unknown space inflation turned off, the formal safety guarantee of Theorem 1 ‣ VIII-C Safety ‣ VIII Safety Analysis ‣ SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments") covers only tracked dynamic obstacles; untracked obstacles emerging from unobserved space are not accounted for in the corridor generation. Nevertheless, SANDO maintains practical safety through the combined effect of conservative obstacle inflation ($r_{\text{margin}}=0.2$ m, $r_{\text{drone}}=0.45$ m), continuous replanning, and heat map-based steering away from occluded areas, as demonstrated by 16 collision-free hardware flights across all experiments.

<!-- chunk {"id": "body-0126", "role": "body", "section": "X-A Static Environments", "weight": 1.0} -->

We first evaluated SANDO in a static indoor environment where obstacles were placed in a $20\,\text{m}\times 8\,\text{m}$ area. The UAV was tasked with flying from $x=0.0$ m to $x=20.0$ m and returning to the start. To assess performance across a range of speeds, we conducted six flights with velocity limits $v_{\max}\in\{1.0,2.0,3.0,4.0,5.0,6.0\}$ m/s. The acceleration and jerk limits were set to $a_{\max}=5.0$ m/s^2^ and $j_{\max}=10.0$ m/s^3^ for the first four flights. For Experiments 5 and 6, $j_{\max}$ was reduced to $7.5$ m/s^3^ to mitigate the larger tracking errors observed at higher speeds. Fig. 12 shows the resulting trajectory overlaid on the LiDAR point cloud; the UAV successfully avoids all static obstacles across the entire speed range.

<!-- chunk {"id": "body-0127", "role": "body", "section": "X-A Static Environments", "weight": 1.0} -->

Table X reports the computation times for all six flights, where $T_{\mathrm{replan}}$, $T_{\mathrm{global}}$, $T_{\mathrm{SSFC}}$, and $T_{\mathrm{opt}}$ denote the average total replanning, global planning, spatial safe flight corridor (SSFC) generation, and trajectory optimization times, respectively. As in the static simulation benchmark (Section IX-A), SANDO uses SSFCs rather than STSFCs since there are no dynamic obstacles. Although the computation times are higher than in simulation due to the less powerful onboard computer, SANDO consistently maintains real-time performance, with average replanning times around $35\text{\,}\mathrm{ms}$ across all velocity limits. Fig. 13 shows the velocity profile for Experiment 3, confirming that the UAV satisfies the dynamic constraints while maintaining smooth velocity transitions throughout the flight.

<!-- chunk {"id": "body-0128", "role": "body", "section": "X-B UAV in Dynamic Environments", "weight": 1.0} -->

To evaluate SANDO in dynamic environments, we conducted hardware experiments involving one or five dynamic obstacles, each created by attaching an approximately $2.0\text{\,}\mathrm{m}$-tall foam rectangular box to a wheeled platform. In Experiments 7 to 10, the UAV flew back and forth ($x=0.0$ m to $x=8.0$ m, 5 rounds) in an $8\,\text{m}\times 8\,\text{m}$ area with a single dynamic obstacle moving at approximately $0.5\text{\,}\mathrm{m}\mathrm{/}\mathrm{s}$: Experiments 7--9 used linear, circular, and figure-eight obstacle trajectories, while Experiment 10 (Fig. 15) used a person walking randomly to test SANDO's ability to handle unpredictable human motion.

<!-- chunk {"id": "body-0129", "role": "body", "section": "X-B UAV in Dynamic Environments", "weight": 1.0} -->

Experiments 11 to 13 (Fig. 16) had five dynamic obstacles in an $8\,\text{m}\times 20\,\text{m}$ area, where each obstacle follows a linear trajectory at $0.5\text{\,}\mathrm{m}\mathrm{/}\mathrm{s}$ with random initial positions and directions. The agent was tasked with flying from $x=0.0$ m to $x=20.0$ m and returning to the start, similar to the static environment experiments. In Experiments 14 to 16 (Fig. 17), the same five dynamic obstacles were placed in an environment with additional static obstacles, and the UAV was tasked with flying at higher speeds ($v_{\max}\in\{2.0,3.0,4.0\}$ m/s) to further challenge SANDO's performance. The agent was tasked with flying from $x=0.0$ m to $x=20.0$ m, while avoiding both static and dynamic obstacles.

<!-- chunk {"id": "body-0130", "role": "body", "section": "X-B UAV in Dynamic Environments", "weight": 1.0} -->

The dynamic constraints were set to $v_{\max}=2.0\,\text{m/s}$, $a_{\max}=5.0\,\text{m/s}^{2}$, and $j_{\max}=10.0\,\text{m/s}^{3}$ for Experiments 7 to 13, and $v_{\max}\in\{2.0,3.0,4.0\}$ m/s, $a_{\max}=5.0\,\text{m/s}^{2}$, and $j_{\max}=10.0\,\text{m/s}^{3}$ for Experiments 14 to 16. Fig. 15 shows the velocity profile for Experiment 10, confirming that the UAV satisfies the dynamic constraints throughout the flight.

<!-- chunk {"id": "body-0131", "role": "body", "section": "X-B UAV in Dynamic Environments", "weight": 1.0} -->

Table XI summarizes the computation times for all ten dynamic environment experiments, where $T_{\mathrm{STSFC}}$ denotes the spatiotemporal safe flight corridor generation time. For the dynamic experiments, we used $P=2$ spatial polytopes per time layer, whereas the static experiments used $P=3$. This difference is because, as shown in Table IX, $P=2$ achieves higher success rates than $P=3$ in harder dynamic environments (64% vs. 51% in the hard case), since fewer polytopes per layer reduce the MIQP complexity and allow faster replanning, which is critical when the obstacles move. This also explains why the average replanning times in dynamic experiments (around $22\text{\,}\mathrm{ms}$) are lower than in static environments. Overall, SANDO successfully avoids all dynamic obstacles across all ten experiments while maintaining real-time performance.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Conclusions", "weight": 1.0} -->

This paper presented SANDO, a safe trajectory planner for 3D dynamic unknown environments. SANDO combines a heat map-based global planner with STSFC generation that inflates dynamic obstacles by worst-case reachable sets, a variable elimination technique that reduces hard-constraint MIQP optimization to as few as one free variable per axis (for $N=4$), and an AEKF-based dynamic obstacle tracker. Simulations across standardized static benchmarks, obstacle-rich forests, and dynamic environments showed that SANDO consistently achieves the highest success rate with no constraint violations across all difficulty levels, and perception-only experiments without ground truth obstacle information confirmed robust performance under realistic sensing conditions. Hardware experiments on a quadrotor validated the approach.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Conclusions", "weight": 1.0} -->

The current framework has two main limitations. First, as discussed in Section VIII-E, SANDO does not guarantee recursive feasibility due to its moving subgoal structure. Second, the worst-case reachable set inflation can become overly conservative in dense environments, as evidenced by the perception-only results in Section IX-F.
