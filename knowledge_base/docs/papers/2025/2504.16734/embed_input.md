<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

DYNUS: Uncertainty-aware Trajectory Planner in Dynamic Unknown Environments

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper introduces DYNUS, an uncertainty-aware trajectory planner designed for dynamic unknown environments. Operating in such settings presents many challenges - most notably, because the agent cannot predict the ground-truth future paths of obstacles, a previously planned trajectory can become unsafe at any moment, requiring rapid replanning to avoid collisions. Recently developed planners have used soft-constraint approaches to achieve the necessary fast computation times; however, these methods do not guarantee collision-free paths even with static obstacles. In contrast, hard-constraint methods ensure collision-free safety, but typically have longer computation times. To address these issues, we propose three key contributions. First, the DYNUS Global Planner (DGP) and Temporal Safe Corridor Generation operate in spatio-temporal space and handle both static and dynamic obstacles in the 3D environment. Second, the Safe Planning Framework leverages a combination of exploratory, safe, and contingency trajectories to flexibly re-route when potential future collisions with dynamic obstacles are detected. Finally, the Fast Hard-Constraint Local Trajectory Formulation uses a variable elimination approach to reduce the problem size and enable faster computation by pre-computing dependencies between free and dependent variables while still ensuring collision-free trajectories.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We evaluated DYNUS in a variety of simulations, including dense forests, confined office spaces, cave systems, and dynamic environments. Our experiments show that DYNUS achieves a success rate of 100% and travel times that are approximately 25.0% faster than state-of-the-art methods. We also evaluated DYNUS on multiple platforms - a quadrotor, a wheeled robot, and a quadruped - in both simulation and hardware experiments.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Path and trajectory planning for autonomous navigation has been extensively studied. In practical implementations of trajectory planning methods, it is crucial to avoid making overly strict prior assumptions about the environment, as these can limit the generalizability of an approach. This work aims to develop a trajectory planner that utilizes a highly relaxed set of assumptions, which enables it to operate on a wide range of vehicles in a diverse set of environments. The assumptions made by DYNUS are listed in Section II-E. In Section I-A, we demonstrate that DYNUS is capable of operating in a wide range of environments. Sections I-B to I-E review related work on global planning, local trajectory optimization, dynamic obstacle tracking, and exploration. We then summarize our key contributions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "I-A Classification of Environments", "weight": 1.0} -->

Environments are classified by three criteria: known vs. unknown, static vs. dynamic, and open vs. confined. Known environments provide agents with prior information, while unknown environments do not. Static environments have fixed obstacles, whereas dynamic environments could include moving ones. The primary difference is predictability: static obstacles do not change position once observed, while dynamic obstacles continuously move, making it a challenging planning environment. Finally, open environments are characterized by relatively sparse obstacle distributions, such as outdoor settings, whereas confined environments involve occlusions and narrow spaces, such as indoor settings.

<!-- chunk {"id": "body-0006", "role": "body", "section": "I-A Classification of Environments", "weight": 1.0} -->

Table I compares the capabilities of numerous UAV trajectory planners under these environmental assumptions. State-of-the-art methods such as FASTER, EGO-Planner, RAPTOR, HDSM, and SUPER are designed for unknown static environments. MADER handles dynamic environments but requires the future trajectories of dynamic obstacles. PANTHER can operate in dynamic unknown environments, but it generates convex hulls around each obstacle, and this approach is computationally expensive and less effective in environments with many static obstacles. FHD and STS are the most recent works addressing dynamic unknown environments. FHD constructs a temporal Euclidean Signed Distance Field (ESDF) and plans around dynamic obstacles, while STS employs an end-to-end learning approach to navigate highly dynamic environments. However, both approaches assume a 2D environment and do not handle the challenge of planning in 3D dynamic unknown environments.

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-B Global Planning and Safe Corridor Generation", "weight": 1.0} -->

Many existing works implement a two-stage planning approach: global planning followed by local trajectory optimization. Global planning generates a path that connects the start and goal positions, while local planning produces a dynamically feasible trajectory. Hard-constraint safe corridor-based methods, such as FASTER, use a global path to generate a safe corridor through convex decomposition techniques. In contrast, soft-constrained methods often use a global path as an initial guess for trajectory optimization.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-B Global Planning and Safe Corridor Generation", "weight": 1.0} -->

FASTER uses Jump Point Search (JPS) to generate a global path; however, it does not account for dynamic obstacles. Several works have extended JPS, such as, which proposed JPS-based approaches for handling dynamic obstacles. In addition, D\* has been developed as an extension of A\* designed to improve its ability to handle dynamic obstacles. Although these methods address dynamic obstacles, they focus on obstacles that appear randomly during planning execution, which differs from the problem discussed in this paper. In our case, obstacles are detected and their future trajectories are predicted, and therefore the planner must generate a path that avoids these predicted obstacle trajectories in a spatio-temporal manner.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-C1 Position Trajectory Optimization", "weight": 1.0} -->

Local trajectory optimization generates a dynamically feasible trajectory that is either constrained within a safe corridor (if hard-constrained) or loosely follows the global path (if soft-constrained). Many existing works employ spline-based trajectory optimization methods to produce smooth trajectories. One key challenge in trajectory optimization is the trade-off between safety and computational efficiency. Many works use soft-constrained methods. While these methods are computationally efficient, they do not guarantee safety---collision avoidance is encouraged by the soft constraints, but not enforced. On the other hand, hard-constrained methods, such as, guarantee collision-free safety, but can be computationally expensive.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-C2 Yaw Optimization and Uncertainty-awareness in the Direction of Motion", "weight": 1.0} -->

When exploring dynamic environments, tracking dynamic obstacles is crucial to avoid collisions. There are two main approaches for yaw optimization: coupled and decoupled with position optimization. Coupled approaches optimize position and yaw trajectory simultaneously, allowing position optimization to be influenced by perception quality, which improves tracking of dynamic obstacles. However, this approach is known to be computationally expensive. Decoupled approaches optimize position and yaw separately, reducing computation cost. Operating in dynamic unknown environments requires agents account for the possibility of encountering dynamic obstacles in unobservable areas. Thus, whether coupled or decoupled, one of the primary goals of yaw optimization must be to balance dynamic obstacle tracking with maintaining visibility in the direction of motion. Focusing solely on tracking dynamic obstacles, as in PANTHER, may result in unexpected collisions with obstacles in the direction of motion, whereas prioritizing the direction of motion may lead to collisions with dynamic obstacles. PUMA balances the tracking of dynamic obstacles with looking in the direction of motion; however, its implicit tracking approach with its position-yaw coupled optimization results in a computationally expensive optimization.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-D Dynamic Obstacle Estimation and Prediction", "weight": 1.0} -->

There are various approaches to estimating dynamic obstacles' location and predicting their future trajectories. Many works employ a Kalman filter-based approach combined with either a constant velocity or constant acceleration prediction model, while others adopt learning-based methods. When using a Kalman filter-based approach, the prediction model noise and measurement noise are often assumed to be known and fixed. In contrast, learning-based approaches can learn the noise model from the data but may require a large amount of training data to achieve accurate predictions. It is also important to note that prediction models cannot perfectly predict the future states of dynamic obstacles. To address this, uncertainty-aware prediction methods can be used to account for errors in the prediction and estimation models of dynamic obstacles.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-E Frontier-based Exploration", "weight": 1.0} -->

Frontiers represent the boundary between known and unknown space, and frontier-based exploration is a method used to explore unknown areas. The approach selects frontiers to maximize the speed of exploration, while introduces a trajectory optimization approach that leverages a frontier information structure. Similarly to, the work employs an Octomap -based frontier detection method. In recent years, several works have proposed frontier-based exploration techniques to tackle exploration in complex unknown environments.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-F DYNUS Contributions", "weight": 1.0} -->

DYNUS Global Planner (DGP) and Temporal Safe Corridor Generation: A fast and safe global planner operating in spatio-temporal space and generating temporal safe corridors.

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-F DYNUS Contributions", "weight": 1.0} -->

A safe local planning framework that leverages an exploratory trajectory, safe trajectories, and a contingency plan to handle dynamic unknown environments.

<!-- chunk {"id": "body-0015", "role": "body", "section": "I-F DYNUS Contributions", "weight": 1.0} -->

Variable Elimination-Based Hard-Constraint Optimization Formulation: An optimization technique that pre-computes dependencies between the free and dependent variables to reduce problem complexity while ensuring collision-free trajectories.

<!-- chunk {"id": "body-0016", "role": "body", "section": "I-F DYNUS Contributions", "weight": 1.0} -->

A yaw optimization method that considers potential encounters with obstacles and balances between tracking dynamic obstacles and maintaining visibility in the direction of motion.

<!-- chunk {"id": "body-0017", "role": "body", "section": "I-F DYNUS Contributions", "weight": 1.0} -->

Numerous simulations demonstrating the effectiveness of DYNUS in various complex domains, including unknown, open, confined, static, and dynamic environments in both 2D and 3D.

<!-- chunk {"id": "body-0018", "role": "body", "section": "I-F DYNUS Contributions", "weight": 1.0} -->

Hardware experiments on three different platforms: a quadrotor, a wheeled robot, and a quadruped robot.

<!-- chunk {"id": "body-0019", "role": "body", "section": "DYNUS", "weight": 1.0} -->

This section provides an overview of DYNUS, as illustrated in Fig.. Each component of DYNUS is designed to handle not only static but dynamic unknown obstacles, which requires: planning in spatio-temporal space, adapting trajectories flexibly as dynamic obstacles move unpredictably, and computing safe trajectories quickly.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A DYNUS Global Planner (DGP)", "weight": 1.0} -->

Traditional global planning algorithms such as JPS, A\*, and RRT\* can find paths in 3D static space but do not consider dynamic obstacles. To address this limitation, we first introduce Dynamic A\*, a time-aware graph search algorithm that estimates both velocity and the time needed to reach each node during node expansion in graph search. These time estimates allow us to check for potential conflicts with dynamic obstacles. However, this time-aware approach can be computationally expensive, as it requires estimating velocity and travel time at every node expansion. Thus, to plan efficiently, while remaining robust to dynamic obstacles, our global planner, DGP, combines two components: JPS, which is computationally efficient but cannot handle dynamic obstacles, and Dynamic A\*, which accounts for dynamic obstacles, but is computationally slow. DGP uses Dynamic A\* only when necessary, reducing computation time without compromising safety. See Section III for further details on DGP.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Trajectory Planning Framework", "weight": 1.0} -->

When planning a trajectory, an agent must consider three categories of space within its environment: unknown space, known-free space, and known-occupied space. Some approaches assume that an unknown space is free space and plan trajectories within it; however, this assumption could lead to collisions. FASTER and SUPER instead plan a trajectory into unknown space but commit to a trajectory that is known to be safe to avoid the conservatism of planning only in safe known space. Although this approach is efficient and ensures safety in a static world, it assumes that the known-free space remains free. That assumption can be violated in dynamic unknown environments because the obstacles can move unpredictably, causing known-free space to suddenly become occupied. To address this limitation, DYNUS introduces a novel planning framework that leverages three types of trajectories: exploratory, safe, and contingency.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B Trajectory Planning Framework", "weight": 1.0} -->

Fig. illustrates the trajectory planning framework. The exploratory trajectory is generated from point $A$ using the MIQP-based method described in Section IV-A. We then identify the point where the exploratory trajectory enters the unknown space (point $H$). From $A$ to $H$, we sample points along the exploratory trajectory and generate safe trajectories that starts at these sampled points using a fast closed-form solution, which is described in Section IV-A. We parallelize the computation of safe trajectories to reduce the computation time, which leads to fast computation times, as reported in Section VII. We then commit to the trajectory that is the combination of the exploratory and safe trajectories that ends closest to $H$, denoted as Point $S$ in Fig.. If we fail to find more than a certain number of safe trajectories, we discard the exploratory trajectory, since this means the environment does not allow the agent to have safe backup plans. As the agent moves, we continuously check if the committed trajectory is still safe, and if not, we switch to the closest safe trajectory from the current position.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B Trajectory Planning Framework", "weight": 1.0} -->

However, if a future potential collision is detected and there is no safe trajectory available (e.g., even the safe trajectory is now in collision), we immediately generate and commit to a contingency trajectory using the closed-form solution that avoids the collision.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B Trajectory Planning Framework", "weight": 1.0} -->

As discussed in detail in Section IV-A2, each of these safe and contingency trajectories can be generated in microseconds using our closed-form solution, making the framework suitable for real-time operation. Note that DGP generates a global path that avoids both dynamic and static obstacles. Safe corridors (polyhedra) are then generated around this path, and the local trajectory planner generates trajectories that remain within these corridors, accounting for both types of obstacles. However, because dynamic obstacles are unpredictable and may change their motion at any moment, we designed our replanning framework, which enables DYNUS to flexibly adapt its trajectories.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-C Local Trajectory Optimization", "weight": 1.0} -->

Since dynamic obstacles can change their motion unpredictably, fast trajectory optimization is needed. As discussed in Section I-C1, soft constraint-based approaches, while computationally efficient, do not guarantee safety even with static obstacles. On the other hand, hard constraint-based approaches can guarantee safety with static obstacles but are typically slower. To address this trade-off, we introduce a variable elimination technique that reduces the number of decision variables and constraints in the optimization problem, significantly accelerating hard-constraint-based optimization. Section IV provides a detailed explanation of this method.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-D Yaw Optimization", "weight": 1.0} -->

The yaw optimization module consists of two components: yaw graph search and yaw fitting. First, we perform a graph search using utility values that consider factors such as collision probability and the time since each obstacle was last observed. This search produces a sequence of discrete yaw angles. Then, a B-spline fitting process is applied to generate a smooth yaw trajectory from these discrete values. The full algorithm is described in Section IV-C.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-E System Overview Summary", "weight": 1.0} -->

DYNUS processes point cloud data from both a LiDAR and a depth camera. The point cloud is processed using an Octomap-based Map Manager, which generates a voxel map in a sliding window as detailed in Section IV-B. Point cloud data is also used by the Dynamic Obstacle Tracker, where dynamic obstacles are detected, clustered, and associated with previously observed obstacles. As described in Section V, the Adaptive Extended Kalman Filter (AEKF) is applied within this module to estimate the current positions of dynamic obstacles, and a constant acceleration model is used to predict their future trajectories.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-E System Overview Summary", "weight": 1.0} -->

The voxel map and predicted obstacle trajectories ($\mathbf{p}_{\text{obst}}{(t)}$) are provided as inputs to the DYNUS Global Planner (DGP) and the Safe Corridor Generation module. The DGP computes a global path from the agent's start position to a subgoal, while the Safe Corridor Generation module generates a sequence of overlapping polyhedra. These polyhedra serve as constraints in the trajectory optimization process, ensuring collision-free paths. The resulting position trajectory ($\mathbf{p}{(t)}$) is passed to the Yaw Optimization module. Initially, the Graph Search module generates a sequence of discrete yaw angles, which are then smoothed using B-spline fitting in the Yaw Fitting module, where yaw rate constraints are enforced. The position trajectory ($\mathbf{p}{(t)}$) and yaw trajectory ($\psi{(t)}$) are then transmitted to the low-level controller for execution. Note that point cloud processing, dynamic obstacle tracking, map management, and DYNUS's planning modules are all parallelized.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-E System Overview Summary", "weight": 1.0} -->

Trajectories generated by DYNUS, which satisfy dynamic constraints, can be tracked by the low-level controller.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-E System Overview Summary", "weight": 1.0} -->

Static and dynamic obstacles can be detected by onboard sensors.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-E System Overview Summary", "weight": 1.0} -->

The depth of any bug trap (dead end) is within the maximum range of the local map. Specifically, if a bug trap exceeds the local map's maximum sensing range, the agent may fail to recover, even if the global map captures the entire trap.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-E System Overview Summary", "weight": 1.0} -->

Dynamic obstacles have relatively consistent motion patterns. As described in Section V, the process and sensor noise covariances for newly detected obstacles are initialized using the average covariance from previously observed obstacles. This implicitly assumes that new obstacles behave similarly to those encountered before. However, since these covariances evolve over time, the effect of this initialization diminishes. Alternatively, one could use predefined covariance values; however, this approach does not incorporate any information about the environment. Therefore, we choose to use the average of the covariances from previously encountered obstacles.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A Global Planner", "weight": 1.0} -->

To handle static obstacles and predicted trajectories of dynamic obstacles in a computationally efficient manner, we propose the DYNUS Global Planner (DGP). DGP combines two global planning algorithms: Dynamic A\* and JPS. We first introduce Dynamic A\* and then discuss how DGP integrates these two methods.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-A1 Dynamic A\\*", "weight": 1.0} -->

The main challenge in global planning for *dynamic* environments is to efficiently deconflict with the *predicted* future positions of moving obstacles. We use a graph-search approach where each node is defined as

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-A1 Dynamic A\\*", "weight": 1.0} -->

encoding a 3D position, velocity, travel time $t_{i}$, A\* cost $f_{i}$, and occupancy status $o_{i}$. Since each node specifies a unique position at a specific time, occupancy $o_{i}$ can be directly queried in the spatio-temporal space. Velocities $(v_{x,i},v_{y,i},v_{z,i})$ are included because different routes require different velocities, directly influencing travel times. The cost $f_{i}$, computed via the standard A\* formulation (sum of travel and heuristic costs), determines node expansion priority.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Why travel-time matters", "weight": 1.0} -->

Because dynamic obstacles are timestamped, the occupancy of a location depends on *when* the agent gets there. Hence, during expansion we must estimate the *travel time* to a child node so that its timestamp $t_{i + 1}$ is known before the collision check.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Axis-wise time estimate", "weight": 1.0} -->

Note that all computations below are performed *independently on each axis*, and for clarity, we omit the axis subscript (e.g. $v_{k,i}$ is now denoted as $v_{i}$).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Axis-wise time estimate", "weight": 1.0} -->

To estimate travel time, we introduce a kinematics-based time estimation approach, which is incorporated into node expansion during the graph search. When a node is expanded, we estimate the time required to reach it from its parent. We first show the simple example case. If the initial velocity $v_{i}$ at node $i$ is positive ($v_{i}$ \> 0), and also the node expansion is positive ($\delta$ \> 0). Then the agent's velocity at node $i + 1$ is computed by $v_{i + 1} = \sqrt{v_{i}^{2} + {2a_{\text{max}}d}}$ and the travel time from node $i$ to node $i + 1$ is given by ${\Delta t} = {{({v_{i + 1} - v_{i}})}/a_{\text{max}}}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Axis-wise time estimate", "weight": 1.0} -->

If the agent is initially moving opposite to the desired direction (i.e., if the current velocity $v_{i}$ and the displacement have opposite signs), the algorithm first computes the time required to decelerate to zero before accelerating in the intended direction.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Axis-wise time estimate", "weight": 1.0} -->

We also consider *cruising phase*. When the agent reaches the maximum velocity $v_{\text{max}}$ we need to maintain this maximum velocity and compute travel time accordingly. To this end, we first calculate the candidate velocity, $v_{\text{cand}} = \sqrt{v_{i}^{2} + {2a_{\text{max}}d}}$, and we check if $v_{\text{cand}}$ exceeds $v_{\text{max}}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Axis-wise time estimate", "weight": 1.0} -->

Thus, the total travel time is given by ${\Delta t} = {t_{\text{accel}} + t_{\text{cruise}}}$ with the final velocity at the node updated to $v_{i + 1}\leftarrow v_{\text{max}}$. A similar approach is applied for negative displacements ($\delta \leq 0$) with appropriate sign adjustments.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Axis-wise time estimate", "weight": 1.0} -->

This ensures that the estimated arrival times consider both the agent's kinematic capabilities and the imposed velocity limits. Algorithm provides the pseudocode for time estimation in Dynamic A\* ---to simplify the presentation, only the positive displacement case is presented. For negative displacements, similar logic applies with appropriate deceleration and reversal operations.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Axis-wise time estimate", "weight": 1.0} -->

1:Input: Positions pi and pi + 1, velocity at node i (vi), maximum acceleration amax, maximum velocity vmax, and tolerance ϵ. 2:Output: Travel time Δt and updated velocity vi + 1. 4:if δ &gt; 0 then // Positive displacement. 5: if vi ≥ 0 then // Moving in the right direction. 6: if vi ≥ (vmax−ϵ) then // Already cruising near vmax. 7: vi + 1 ← vmax // Set final velocity to the maximum. 10: // Compute candidate velocity. 11: $v_{\text{cand}}\leftarrow\sqrt{v_{i}^{2} + {2a_{\text{max}}d}}$
12: if vcand ≤ vmax then // No cruising phase needed. 15: else// Candidate velocity exceeds maximum
16: // Distance required to accelerate to vmax. 17: daccel ← (vmax2−vi2)/(2amax)
18: // Time to accelerate up to vmax.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Axis-wise time estimate", "weight": 1.0} -->

19: taccel ← (vmax−vi)/amax
20: // If a cruise phase is allowed. 22: // Remaining distance at cruising speed. 24: tcruise ← dcruise/vmax
25: Δt ← taccel + tcruise // Total travel time. 27: vi + 1 ← vmax // Final velocity set to vmax. 31: // vi &lt; 0 case is omitted for brevity. Algorithm 1 Time Estimation in Dynamic A*

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-A2 DYNUS Global Planner (DGP)", "weight": 1.0} -->

Although Dynamic A\* can handle dynamic obstacles, it requires computing the travel time whenever a node is expanded. Since this can increase computation time significantly, we propose DGP. The planner first considers only static obstacles and finds a path using JPS. Next, it checks whether the JPS-generated path intersects with the predicted trajectory of dynamic obstacles. If no collision is detected, the JPS path is returned since it is guaranteed to be collision-free. However, if the path intersects with a predicted dynamic obstacle trajectory, the planner identifies the colliding node (node A) and the nearest subsequent collision-free node (node B). Dynamic A\* is then used to generate a subpath between node A and node B that avoids dynamic obstacles. This new subpath is merged with the original JPS path, and the planner re-evaluates the entire path to check for potential collisions with dynamic obstacles. This re-evaluation is necessary since the updated path may be longer than the original path, and new collisions could arise. This process is repeated until a fully collision-free path is obtained, after which the planner returns the final path.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-A2 DYNUS Global Planner (DGP)", "weight": 1.0} -->

Unlike Dynamic A\*, DGP does not need to consider dynamic obstacles at every search step, as dynamic obstacles are only accounted for when the JPS-generated path intersects with their predicted trajectories.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-A3 Path Adjustment", "weight": 1.0} -->

To account for uncertainty in the prediction of dynamic obstacles and potential encounters with obstacles from behind occlusions, we propose a path adjustment algorithm that improves the visibility of unknown areas by pushing the global path away from both static obstacles and the predicted trajectories of dynamic obstacles. First, Algorithm summarizes the process of adjusting paths to account for dynamic obstacles, and Fig. illustrates the path adjustment process. The algorithm begins by initializing an adjusted path, copying the initial point of the global path. For each subsequent point in the global path, the algorithm evaluates the repulsion force based on the predicted uncertainty of obstacles, which is represented by the estimated covariance from the AEKF estimation module (Section V). Fig. shows that as the uncertainty increases, the repulsion force becomes stronger, enforcing a larger safety distance from the obstacle.

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-A3 Path Adjustment", "weight": 1.0} -->

1:Input: 𝒫 (global path) 2: 𝒯obs (set of predicted obstacle trajectories) 3:Output: 𝒫new (adjusted new path) 5:for i ← 1 to size(𝒫) − 1 do // Skip the first point 6: p ← 𝒫[i] // Current global path point 7: pnew ← 𝒫[i] // Initialize adjusted point 8: for τ ∈ 𝒯obs do // Iterate through each obstacle trajectory 9: // Compute push force 10: // k: const., αP: scaling factor, τ.P: estimate covariance 12: o ← τ.pos(ti) // Obstacle position at t = ti 13: d ← p − o // Direction vector to obstacle 15: if r &lt; C then // Check if within collision clearance 16: // Compute repulsion force 17: $\mathbf{f}_{rep}\leftarrow{F_{push} \cdot \left( {1 - \frac{r}{C}} \right) \cdot \frac{\mathbf{d}}{r}}$ 18: pnew ←

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-A3 Path Adjustment", "weight": 1.0} -->

pnew + frep // Update adjusted point 21: // Append adjusted point to adjusted new path 22: 𝒫new.append(pnew) Algorithm 2 Dynamic Obstacle Path Adjustment

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-A3 Path Adjustment", "weight": 1.0} -->

We now describe the path adjustment process for static obstacles. Although the path generated by DGP is collision-free, it may pass close to static obstacles, limiting the visibility of unknown areas. To address this issue, we propose a path adjustment algorithm that pushes the global path away from static obstacles, improving the visibility of previously unknown areas. Fig. illustrates the static obstacle path adjustment algorithm. As shown in Fig. LABEL:fig:static_push_1, the adjustment process begins by finding a straight line that connects the start and $N_{\text{LAD}}$-th points of the global path, where $N_{\text{LAD}}$ denotes the number of look-ahead discretization points. The algorithm then discretizes this path and checks for occupied points in the static map, and if occupied points are detected, the mean position of these points is computed. Lastly, the points on the original global path are pushed away from this mean position by a fixed distance (Fig. LABEL:fig:static_push_2).

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-A3 Path Adjustment", "weight": 1.0} -->

After adjusting the path, DGP verifies that the updated trajectory remains within known-free space, and if not, the push distance is decreased until a collision-free path is obtained. This mean position of the occupied points is stored and used to push the path at the next iteration as well.

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-A3 Path Adjustment", "weight": 1.0} -->

1:Input: 𝒫 (global path)
2: ddisc. (discretization distance)
3:Output: 𝒫new (adjusted new path)
4:// Find the path connecting the start and NLAD-th points
5:pstart ← 𝒫, pLAD ← 𝒫[NLAD], d ← pLAD − pstart
6:// Discretize the path and check for occupied points
7:nsteps ← ⌈∥d∥/ddisc.⌉, s ← d/nsteps
13:end for// Compute the mean position of occupied points
14:${\overline{\mathbf{p}}}_{mean}\leftarrow{\frac{1}{|\mathcal{O}|}\left.

<!-- chunk {"id": "body-0053", "role": "body", "section": "III-A3 Path Adjustment", "weight": 1.0} -->

\sum{}_{\mathbf{o} \in \mathcal{O}}\mathbf{o} \right.}$ // Compute push vectors
16: $\mathcal{V}_{push}.{{append}\left( {{\mathcal{P}\lbrack i\rbrack} - {\overline{\mathbf{p}}}_{mean}} \right)}$
18:// Push the path points away from ${\overline{\mathbf{p}}}_{mean}$
20: 𝒫new[i] ← 𝒫[i] + αpush ⋅ 𝒱push[i]
Algorithm 3 Static Obstacle Path Adjustment

<!-- chunk {"id": "body-0054", "role": "body", "section": "III-B Temporal Safe Corridor Generation", "weight": 1.0} -->

The safe corridor generation module constructs a series of overlapping convex hulls, or polyhedra, that allow the agent to navigate safely through the environment. The inputs for this module consist of the path generated by the global planner, the static occupancy map, and the predicted trajectories of dynamic obstacles. A polyhedron is generated around each segment of the piecewise linear path by first inflating an ellipsoid aligned with the segment, followed by computing tangent planes at the contact points of the ellipsoid with obstacles. See for a detailed explanation of this method.

<!-- chunk {"id": "body-0055", "role": "body", "section": "III-B Temporal Safe Corridor Generation", "weight": 1.0} -->

To account for timestamped dynamic obstacles, we estimate travel times along the global path using the double integrator model. Note that the path found by DGP is adjusted by Algorithms and, and therefore we use the double integrator to re-estimate travel times along the global path. We then update the occupancy of the map and generate a snapshot of the environment for each segment. The safe corridor generation module uses this snapshot to construct a safe corridor, accouting for dynamic obstacles.

<!-- chunk {"id": "body-0056", "role": "body", "section": "III-C Starting Point Selection", "weight": 1.0} -->

This section describes how DYNUS selects the starting point. DYNUS continuously replans its trajectory as it moves and adjusts the starting point based on the computation time of the global planner. If the starting point is too close to the current position, the global planner may not have enough time to compute the trajectory before the agent reaches that point. Conversely, if the starting point is too far, the agent will have to execute a trajectory based on outdated information, making it suboptimal. DYNUS uses an exponential moving average (EMA) of the computation time to adjust the starting point.

<!-- chunk {"id": "body-0057", "role": "body", "section": "III-C Starting Point Selection", "weight": 1.0} -->

where $\delta t_{A}$ is the estimated computation time for the global planner to compute the trajectory from the starting point A, $\delta t_{A}^{\text{new}}$ is the new computation time, and $\alpha_{\delta t_{A}}$ is the EMA coefficient.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Trajectory Optimization", "weight": 1.0} -->

This section describes the trajectory optimization process for both the position and yaw of the agent. For position trajectory optimization, we utilize hard constraint with Mixed-Integer Quadratic Programming (MIQP). Although a MIQP-based hard constraint approach introduces additional variables (binary variables for interval-polyhedron assignment) and increases computational cost, it guarantees safety against static obstacles and improves the likelihood of finding a feasible solution. To reduce computational complexity, we introduce a variable elimination technique that pre-computes the dependencies of variables and eliminates dependent variables from the optimization problem. Additionally, to balance efficiency and feasibility, we change the number of intervals based on the replanning results. A lower number of intervals mean fewer variables and constraints, which reduces computational cost but may lead to infeasible solutions. In contrast, more intervals increase the likelihood of finding feasible solutions but also increase computational cost. We therefore starts with smaller number of intervals and increase the number of intervals if the solution is infeasible.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-A Position Trajectory Optimization", "weight": 1.0} -->

This section first describes DYNUS's MIQP formulation for position trajectory optimization. We use triple integrator dynamics with the state vector: $\mathbf{x}^{T} = \left\lbrack {{\mathbf{x}}^{T}{\mathbf{v}}^{T}{\mathbf{a}}^{T}} \right\rbrack$, where $\mathbf{x}$, $\mathbf{v}$, and $\mathbf{a}$ represent the position, velocity, and acceleration, respectively.

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-A Position Trajectory Optimization", "weight": 1.0} -->

We formulate trajectory optimization using an $N$-interval composite Bézier curve with $P$ polyhedra. Let $n \in {\{ 0:{N - 1}\}}$ denote a specific interval of the trajectory, $p \in {\{ 0:{P - 1}\}}$ represent a specific polyhedron, and $dt$ denote the time allocated for each interval---the same for all intervals. To clarify the notation, ${\mathbf{j}}_{n}{(\tau)}$ denotes the jerk vector at the $n$-th interval at time $\tau$ within that interval.

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-A Position Trajectory Optimization", "weight": 1.0} -->

We now discuss constraints for the optimization formulation.

<!-- chunk {"id": "body-0062", "role": "body", "section": "IV-A Position Trajectory Optimization", "weight": 1.0} -->

and, to assign intervals to polyhedra and ensure the control points for each interval are within the corresponding polyhedron, we introduce binary variables $b_{np}$, where $b_{np} = 1$ if interval $n$ is assigned to polyhedron $p$, and $b_{np} = 0$ otherwise.

<!-- chunk {"id": "body-0063", "role": "body", "section": "IV-A Position Trajectory Optimization", "weight": 1.0} -->

where $\mathbf{x}_{\text{init}}$ is the initial state, and $\mathbf{x}_{\text{final}}$ is the final state. Note that the final state is chosen to be the mean of the last polyhedron's vertices.

<!-- chunk {"id": "body-0064", "role": "body", "section": "IV-A Position Trajectory Optimization", "weight": 1.0} -->

For dynamic constraints, we require the velocity, acceleration, and jerk control points to satisfy the following constraints for all intervals $n$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "IV-A Position Trajectory Optimization", "weight": 1.0} -->

where $v_{\text{max}}$, $a_{\text{max}}$, and $j_{\text{max}}$ denote the maximum allowable velocity, acceleration, and jerk, respectively.

<!-- chunk {"id": "body-0066", "role": "body", "section": "IV-A Position Trajectory Optimization", "weight": 1.0} -->

The objective function consists of two components: control input cost and reference tracking cost.

<!-- chunk {"id": "body-0067", "role": "body", "section": "IV-A Position Trajectory Optimization", "weight": 1.0} -->

Reference Tracking Cost: We penalize deviation from reference points $\mathbf{x}_{\text{ref},i}$, which are computed as the mean of each polyhedron's vertices.

<!-- chunk {"id": "body-0068", "role": "body", "section": "IV-A Position Trajectory Optimization", "weight": 1.0} -->

where $t_{i} = {\frac{i}{P - 1}T}$ is the time associated with reference point $\mathbf{x}_{\text{ref},i}$, and $\mathbf{x}{(t_{i})}$ is the position evaluated at time $t_{i}$. The reason for excluding the first and last polyhedra is that they are already constrained by Eq., and there is no need to have reference points for them.

<!-- chunk {"id": "body-0069", "role": "body", "section": "IV-A1 Variable Elimination", "weight": 1.0} -->

In our MIQP formulation (see Eq. ), four sets of coefficients, $\mathbf{a}_{n}$, $\mathbf{b}_{n}$, $\mathbf{c}_{n}$, and $\mathbf{d}_{n}$, are introduced per segment $n$. Since the total number of decision variables grows linearly with the number of segments, the computational burden increases accordingly.

<!-- chunk {"id": "body-0070", "role": "body", "section": "IV-A1 Variable Elimination", "weight": 1.0} -->

To address this challenge, we employ a variable elimination technique that leverages the structure of cubic splines. Specifically, by symbolically solving the equality constraints imposed by the initial/final conditions and the continuity conditions between segments, we can express most of the spline coefficients in terms of a small set of free variables.

<!-- chunk {"id": "body-0071", "role": "body", "section": "IV-A1 Variable Elimination", "weight": 1.0} -->

It significantly reduces the number of decision variables.

<!-- chunk {"id": "body-0072", "role": "body", "section": "IV-A1 Variable Elimination", "weight": 1.0} -->

It eliminates the need to include equality constraints explicitly in the optimization.

<!-- chunk {"id": "body-0073", "role": "body", "section": "IV-A1 Variable Elimination", "weight": 1.0} -->

Problem Setup: Each segment is a cubic polynomial, as shown in Eq.,

<!-- chunk {"id": "body-0074", "role": "body", "section": "IV-A1 Variable Elimination", "weight": 1.0} -->

Continuity Constraints (Eq. ): These ensure continuity of position, velocity, and acceleration at the junctions between consecutive segments, resulting in $3{({N - 1})}$ constraints per axis.

<!-- chunk {"id": "body-0075", "role": "body", "section": "IV-A1 Variable Elimination", "weight": 1.0} -->

Boundary Conditions (Eq. ): These impose the initial and final values for position, velocity, and acceleration (a total of 6 constraints per axis).

<!-- chunk {"id": "body-0076", "role": "body", "section": "IV-A1 Variable Elimination", "weight": 1.0} -->

Thus, for $N$ segments, there are $4N$ decision variables and ${3N} + 3$ equality constraints per axis.

<!-- chunk {"id": "body-0077", "role": "body", "section": "IV-A1 Variable Elimination", "weight": 1.0} -->

*Decision Variables:* ${4N} = 12$ per axis (i.e., 36 total for $x$, $y$, and $z$).

<!-- chunk {"id": "body-0078", "role": "body", "section": "IV-A1 Variable Elimination", "weight": 1.0} -->

*Equality Constraints:* ${{3N} + 3} = 12$ per axis (i.e., 36 total).

<!-- chunk {"id": "body-0079", "role": "body", "section": "IV-A1 Variable Elimination", "weight": 1.0} -->

This implies that the system is fully determined, resulting in a unique closed-form solution for all spline coefficients as functions of the boundary conditions. While this formulation enables very fast computation, it does not guarantee the satisfaction of inequality constraints (e.g., Eqs. and ). These constraints can be verified in a post-optimization step, making the $N = 3$ formulation appropriate for safe and contingency trajectory generation (see Section II-B).

<!-- chunk {"id": "body-0080", "role": "body", "section": "IV-A1 Variable Elimination", "weight": 1.0} -->

*Decision Variables:* ${4N} = 16$ per axis (i.e., 48 total for all axes).

<!-- chunk {"id": "body-0081", "role": "body", "section": "IV-A1 Variable Elimination", "weight": 1.0} -->

*Equality Constraints:* ${{3N} + 3} = 15$ per axis (i.e., 45 total).

<!-- chunk {"id": "body-0082", "role": "body", "section": "IV-A1 Variable Elimination", "weight": 1.0} -->

which indicates the existence of one free parameter per axis. Symbolic elimination reveals that this free variable is $\mathbf{d}_{3}$ (the first control point of the final segment, where $n \in {\{ 0,1,2,3\}}$). Consequently, all other spline coefficients can be expressed as explicit affine functions of $\mathbf{d}_{3}$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "IV-A1 Variable Elimination", "weight": 1.0} -->

The equality constraints are implicitly satisfied, enabling their removal from the optimization problem.

<!-- chunk {"id": "body-0084", "role": "body", "section": "IV-A1 Variable Elimination", "weight": 1.0} -->

Only a single decision variable per axis, $\mathbf{d}_{3}$, remains explicitly.

<!-- chunk {"id": "body-0085", "role": "body", "section": "IV-A1 Variable Elimination", "weight": 1.0} -->

All other control points are formulated as affine functions of $\mathbf{d}_{3}$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "IV-A2 Contingency Trajectory Generation", "weight": 1.0} -->

This section discusses how we generate the contingency trajectory (See Section II-B for details), using the closed-form solution ($N = 3$).

<!-- chunk {"id": "body-0087", "role": "body", "section": "IV-A2 Contingency Trajectory Generation", "weight": 1.0} -->

To explore alternative directions, we build a plane orthogonal to ${\hat{\mathbf{v}}}_{\text{curr}}$ and define evenly spaced lateral directions (at $45^{\circ}$ increments), generating eight additional candidate goals around $\mathbf{x}_{\text{center}}$. Each candidate's goal is scored based on its distance from the predicted collision point, and the planner iteratively attempts to connect to the farthest candidate using the closed-form solution. As soon as a feasible plan is found, it is committed and replaces the previous trajectory. If none of the contingency goals result in a feasible trajectory, the agent executes an emergency stop. In this case, the planner replaces the committed trajectory with a static hover command at the current position and zero velocity, acceleration, and jerk.

<!-- chunk {"id": "body-0088", "role": "body", "section": "IV-A3 Time Allocation and Parallelization", "weight": 1.0} -->

where $f$ is a factor that we vary in parallel to efficiently explore different time allocations. Fig. shows how we initialize the time allocation with different factors and solve the optimization problems in parallel to find the optimal trajectory. As soon as any of the optimization problems running in parallel find a feasible solution, the other optimization problems are stopped, and that solution is used. The factors for the next iteration are chosen so that the previously successful factor is the median of the new ones. If none of the parallelized optimization problems find a feasible solution, we initialize the minimum factor to be the largest factor in the previous iteration.

<!-- chunk {"id": "body-0089", "role": "body", "section": "IV-A4 Adaptive Number of Intervals", "weight": 1.0} -->

QP-based methods use an equal number of intervals and polyhedra ($P = N$) while using non-uniform time allocation. This approach is computationally efficient but may lead to infeasible solutions. In contrast, MIQP-based methods use $P < N$ with uniform time allocation. This approach improves feasibility, but it also increases computational cost. DYNUS adaptively changes the number of intervals based on the replanning results---when the solution is infeasible, the number of intervals is increased.

<!-- chunk {"id": "body-0090", "role": "body", "section": "IV-B Map Representation", "weight": 1.0} -->

To achieve efficient map storage, we use an octomap. Additionally, as illustrated in Fig., we use a sliding window with varying size. We first project the terminal goal onto DYNUS's planning horizon and adjust the sliding window's size based on the projected goal's location. Specifically, we increase the window's size in the direction of the projected goal. The octomap stores the entire map (global map), while the sliding window maintains a local map for planning. Note that, as discussed in Section VI, when DYNUS is assigned exploration tasks, we do not perform projection and use the best frontier as the sub-goal.

<!-- chunk {"id": "body-0091", "role": "body", "section": "IV-B Map Representation", "weight": 1.0} -->

We also implemented the removal of residual obstacle traces or "smears" in the octomap. When sensors detect dynamic obstacles, residual data may persist even after the obstacles have moved away, creating false obstacles on the map. To address this, we introduce a smear-removal mechanism that periodically checks the last detection timestamp of obstacles and removes occupied space if the obstacle has not been detected for a certain period.

<!-- chunk {"id": "body-0092", "role": "body", "section": "IV-C Yaw Optimization", "weight": 1.0} -->

As discussed in Section I-C2, coupled approaches are computationally expensive and may not be suitable for real-time applications. Thus, DYNUS adopts a decoupled approach, where the position and yaw trajectories are optimized separately. First, we run a graph search to find the optimal sequence of discrete yaw angles along the position trajectory. Next, we perform B-spline fitting to smooth the discrete yaw angles, ensuring a continuous and feasible yaw trajectory.

<!-- chunk {"id": "body-0093", "role": "body", "section": "IV-C1 Graph Search for Discrete Yaw Angles", "weight": 1.0} -->

To find a sequence of yaw angles that optimally balance tracking obstacles and looking in the direction of motion, we employ a graph search algorithm that balances multiple objectives: collision likelihood, velocity of dynamic obstacles, proximity to obstacles, time since last observed, and minimization of yaw changes. The algorithm operates over a discretized time horizon and incrementally explores potential yaw states by evaluating their utility.

<!-- chunk {"id": "body-0094", "role": "body", "section": "IV-C1 Graph Search for Discrete Yaw Angles", "weight": 1.0} -->

The graph search begins by initializing an open set containing the root node, which corresponds to the initial position, yaw, and time. At each iteration, the algorithm selects the node with the lowest cost from the open set and expands it by generating potential next yaw angeles. For each new state, the utility is computed as a weighted sum of the following components.

<!-- chunk {"id": "body-0095", "role": "body", "section": "IV-C1 Graph Search for Discrete Yaw Angles", "weight": 1.0} -->

Collision Likelihood: Using the Mahalanobis distance, the collision likelihood evaluates the probability of a collision between the agent and obstacles by considering position uncertainty. This uncertainty is represented by the covariance matrix obtained from the Adaptive Extended Kalman Filter (AEKF) obstacle tracker, which is discussed in detail in Section V.

<!-- chunk {"id": "body-0096", "role": "body", "section": "IV-C1 Graph Search for Discrete Yaw Angles", "weight": 1.0} -->

where $T_{\text{total}} = {t_{\text{end}} - t_{\text{cur}}}$ is the total duration of the trajectory, with $t_{\text{end}}$ representing the final time and $t_{\text{cur}}$ the current time, and $\Sigma_{\text{EKF}}$ is the AEKF estimate covariance, and $\Sigma_{\text{poly}}$ has the dynamic obstacles' predicted future trajectory (polynomial)'s fitting residuals as the diagonal elements. We blended the covariances since, at $t = t_{\text{cur}}$, the estimation uncertainty primarily arises from the AEKF estimate covariance, while as time progresses, the uncertainty from the trajectory prediction becomes more significant.

<!-- chunk {"id": "body-0097", "role": "body", "section": "IV-C1 Graph Search for Discrete Yaw Angles", "weight": 1.0} -->

Velocity: The velocity cost encourages an agent to track dynamic obstacles that are moving faster.

<!-- chunk {"id": "body-0098", "role": "body", "section": "IV-C1 Graph Search for Discrete Yaw Angles", "weight": 1.0} -->

where ${\mathbf{v}}_{o}{(t)}$ is the velocity of the obstacle at time $t$, and $M$ is the number of sampled time points.

<!-- chunk {"id": "body-0099", "role": "body", "section": "IV-C1 Graph Search for Discrete Yaw Angles", "weight": 1.0} -->

where $\mathcal{O}$ represents the set of obstacles within the cutoff distance, and $t_{\text{slo},o}$ denotes the time elapsed since the last observation of obstacle $o$. For clarity, a smaller value of this term for a particular yaw angle indicates that all obstacles, as well as the direction of motion, have been observed recently, indicating a good yaw angle. Note that in DYNUS, the direction of motion is computed using a point that is $t_{lookup}$ seconds ahead along the planned trajectory.

<!-- chunk {"id": "body-0100", "role": "body", "section": "IV-C1 Graph Search for Discrete Yaw Angles", "weight": 1.0} -->

where $\mathcal{U} = {\{\text{collision},\text{velocity},\text{observed},\text{proximity},\text{yaw}\}}$ represents the set of utility components.

<!-- chunk {"id": "body-0101", "role": "body", "section": "IV-C1 Graph Search for Discrete Yaw Angles", "weight": 1.0} -->

To reconstruct the optimal yaw sequence, the algorithm tracks the parent node for each explored state, enabling backtracking once the terminal node is reached. The resulting yaw sequence is then smoothed using a B-spline fitting process, which is detailed in the following.

<!-- chunk {"id": "body-0102", "role": "body", "section": "IV-C2 Yaw B-Spline Fitting", "weight": 1.0} -->

To achieve a smooth yaw trajectory, we employ a clamped uniform cubic B-spline fitting. This approach minimizes the squared error between the optimized discrete yaw sequence and the fitted B-spline trajectory while enforcing constraints on the yaw rate.

<!-- chunk {"id": "body-0103", "role": "body", "section": "IV-C2 Yaw B-Spline Fitting", "weight": 1.0} -->

Problem Formulation: The yaw trajectory is represented as a cubic B-spline defined by a set of control points $\mathbf{q} = {\{ q_{0},q_{1},\ldots,q_{n}\}}$. The objective is to determine the optimal control points that minimize the squared error between the B-spline values and the yaw sequence $\{\psi_{\text{opt},i}\}$ for $i \in {\{ 0:{S - 1}\}}$, where $S$ is the number of yaw angles in the sequence.

<!-- chunk {"id": "body-0104", "role": "body", "section": "IV-C2 Yaw B-Spline Fitting", "weight": 1.0} -->

where $\psi_{\text{B-spline}}{(t)}$ represents the B-spline value at time $t$, and the time increment between two consecutive points, $t_{i + 1} - t_{i}$, is given by $T_{\text{total}}/S$, with $T_{\text{total}}$ denoting the total trajectory duration. Since the B-spline is defined over a clamped uniform knot vector, the initial and final yaw values are inherently satisfied.

<!-- chunk {"id": "body-0105", "role": "body", "section": "IV-C2 Yaw B-Spline Fitting", "weight": 1.0} -->

where $\overset{˙}{\psi}{(t)}$ represents the yaw rate control point, $p$ is the degree of the B-spline (here $p = 3$), and $t_{i}$ denotes the time at point $i$ in knots. For all control points $q_{i}$, the yaw rate constraints are enforced as ${|{\overset{˙}{\psi}}_{i}|} \leq \omega_{\text{max}}$, where $\omega_{\text{max}}$ is the maximum allowable yaw rate. The optimization is solved using Gurobi.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Dynamic Obstacle Tracking and Prediction", "weight": 1.0} -->

Dynamic Obstacle Tracking: Many methods assume predefined noise models for both process and measurement noise, and they typically use fixed noise covariances, which could represent inaccurate noise models. To overcome this challenge, we employ an Adaptive Extended Kalman Filter (AEKF), which dynamically adjusts the process noise and measurement noise covariances. By continuously updating these covariance values, the AEKF accounts for uncertainty in estimation. Below, we briefly describe the covariance update steps of the AEKF algorithm for both process noise and sensor noise covariances.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Dynamic Obstacle Tracking and Prediction", "weight": 1.0} -->

where $\epsilon_{k}$ is the residual, $z_{k}$ is the actual measurement, ${\hat{x}}_{k}^{+}$ is the updated state estimate, $h{( \cdot )}$ is the measurement model, $u_{k}$ is the control input, which is not used in our case, and $\alpha$ is a forgetting factor (with $0 < \alpha \leq 1$) that controls the influence of past values on the new covariance estimate.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Dynamic Obstacle Tracking and Prediction", "weight": 1.0} -->

where $d_{k}$ is the innovation, ${\hat{x}}_{k}^{-}$ is the predicted state, and $K_{k}$ is the Kalman gain. We implement this AEKF-based filtering approach to estimate and smooth the history of dynamic obstacles' positions, velocities, and accelerations. Additionally, when DYNUS detects a new dynamic obstacle, it initializes $Q_{0}$ and $R_{0}$ by averaging the process noise and sensor noise covariances of previously detected dynamic obstacles. This approach enables DYNUS to capture the uncertainty in both the prediction and sensor noise of the dynamic obstacles.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Dynamic Obstacle Tracking and Prediction", "weight": 1.0} -->

Dynamic Obstacle Prediction: To predict the future positions of dynamic obstacles, we use a constant acceleration model. After predicting the future positions, we fit it into a polynomial to smooth the prediction. Additionally, we compute residual values to capture prediction inaccuracies, which are used in the yaw optimization step detailed in Section IV-C.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Frontier-based exploration", "weight": 1.0} -->

In some missions, target goals are predefined, while in others, the agent must explore the environment autonomously. To enable autonomous exploration, we designed a frontier-based exploration approach.

<!-- chunk {"id": "body-0111", "role": "body", "section": "VI-A Frontier-based Exploration Algorithm", "weight": 1.0} -->

DYNUS selects the optimal frontier based on a multi-objective cost function. The algorithm evaluates a set of candidate frontiers and selects the one with the lowest cost. The algorithm includes Frontier Filtering, Cost Function Evaluation, and Frontier Selection.

<!-- chunk {"id": "body-0112", "role": "body", "section": "VI-A1 Frontier Filtering", "weight": 1.0} -->

Frontiers $\mathcal{F} = {\{{\mathbf{f}}_{1},{\mathbf{f}}_{2},\ldots,{\mathbf{f}}_{n}\}}$ are identified by detecting voxels in the octomap that lie between known-free and unknown voxels and are within the agent's sliding window map.

<!-- chunk {"id": "body-0113", "role": "body", "section": "VI-A2 Cost Function Evaluation", "weight": 1.0} -->

where ${\mathbf{x}}_{\text{agent}}$ is the agent's current position, $d_{\text{max}}$ is the maximum distance to the frontier, $v_{\text{max}}$ is the maximum velocity, and $\epsilon$ is a small positive constant.

<!-- chunk {"id": "body-0114", "role": "body", "section": "VI-A2 Cost Function Evaluation", "weight": 1.0} -->

where $| \cdot |$ denotes the cardinality of the set, and $d_{\text{thresh}}$ is a threshold distance. This term encourages selecting frontiers that are clustered together, which indicates more information gain.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

We performed all the simulations on an AlienWare Aurora R8 desktop computer with an Intel^®^ Core ^TM^ i99900K CPU @ 3.60GHz$\times$`<!-- -->`{=html}16, 64 GB of RAM. The operating system is Ubuntu 22.04 LTS, and we used ROS2 Humble.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

To simulate LiDAR data, we used the livox_ros_driver2 package, which provides a ROS 2 interface for the Livox MID-360 LiDAR sensor. For depth camera data, we utilized the ROS 2 interface provided by the realsense-ros package for the Intel^®^ RealSense^TM^ D435 depth camera.

<!-- chunk {"id": "body-0117", "role": "body", "section": "VII-A Benchmarking against State-of-the-Art Methods in Static Environments", "weight": 1.0} -->

We performed benchmarking experiments to compare DYNUS against state-of-the-art methods: FASTER, SUPER, and EGO-Swarm. FASTER and EGO-Swarm use a depth camera, while SUPER uses a LiDAR sensor. As illustrated in Fig., DYNUS uses both the LiDAR sensor and the depth camera for mapping. Since all of them assume a static environment, we evaluated them in a static forest setting, as shown in Fig.. The simulation environment was generated with randomly generated static cylinder obstacles with a radius ranging from $0.2\ m$ to $1.0\ m$ and a height ranging from $1.0\ m$ to $5.0\ m$. The obstacles are spawned within $100\ m$ $\times$ $20\ m$, and the agent starts at position $(0.0,0.0,3.0)$ $\ m$, and the goal position is $(105.0,0.0,3.0)$ $\ m$.

<!-- chunk {"id": "body-0118", "role": "body", "section": "VII-A Benchmarking against State-of-the-Art Methods in Static Environments", "weight": 1.0} -->

Each planner was executed in its preferred operating system: FASTER on Ubuntu 18.04 with ROS1 Melodic, and SUPER and EGO-Swarm on Ubuntu 20.04 with ROS1 Noetic. To ensure a fair comparison, all algorithms were containerized using Docker and executed on the same machine. The reason why we used EGO-Swarm (multiagent planner) over EGO-Planner (single-agent planner) is that EGO-Planner's GitHub code specifically states that EGO-Swarm is more robust and safe than EGO-Planner.

<!-- chunk {"id": "body-0119", "role": "body", "section": "VII-A Benchmarking against State-of-the-Art Methods in Static Environments", "weight": 1.0} -->

Success: The number of successful runs without hitting obstacles and getting stuck.

<!-- chunk {"id": "body-0120", "role": "body", "section": "VII-A Benchmarking against State-of-the-Art Methods in Static Environments", "weight": 1.0} -->

Travel Time \[s\]: Travel time taken by the agent to reach the goal position.

<!-- chunk {"id": "body-0121", "role": "body", "section": "VII-A Benchmarking against State-of-the-Art Methods in Static Environments", "weight": 1.0} -->

Path Length \[m\]: Total length of the path traveled.

<!-- chunk {"id": "body-0122", "role": "body", "section": "VII-A Benchmarking against State-of-the-Art Methods in Static Environments", "weight": 1.0} -->

Global Path Planning Computation Time \[ms\]: Average computation time for global path planning.

<!-- chunk {"id": "body-0123", "role": "body", "section": "VII-A Benchmarking against State-of-the-Art Methods in Static Environments", "weight": 1.0} -->

Exploratory Trajectory Optimization Computation Time \[ms\]: Average computation time for exploratory trajectory optimization.

<!-- chunk {"id": "body-0124", "role": "body", "section": "VII-A Benchmarking against State-of-the-Art Methods in Static Environments", "weight": 1.0} -->

Safe Trajectory Optimization Computation Time \[ms\]: Average computation time for safe trajectory optimization.

<!-- chunk {"id": "body-0125", "role": "body", "section": "VII-A Benchmarking against State-of-the-Art Methods in Static Environments", "weight": 1.0} -->

Total Planning Computation Time \[ms\]: Total computation time for planning of the three components.

<!-- chunk {"id": "body-0126", "role": "body", "section": "VII-A Benchmarking against State-of-the-Art Methods in Static Environments", "weight": 1.0} -->

Replanning Total Computation Time \[ms\]: Total computation time for replanning ---for instance, DYNUS includes safe corridor generation, sub-goal computation, yaw planning, etc.

<!-- chunk {"id": "body-0127", "role": "body", "section": "VII-A Benchmarking against State-of-the-Art Methods in Static Environments", "weight": 1.0} -->

Table II summarizes the benchmarking results, and Fig. shows one of DYNUS's velocity profiles in Case 2. Note that SUPER and EGO-Swarm are soft constraint methods, while FASTER and DYNUS are hard constraint methods. The data reported in Table II is based on the average of 10 simulations, excluding failed runs. Note that SUPER performs global path planning for both exploratory and safe trajectories, so we report both values as Exploratory \| Safe under the Global Path Planning Computation Time column.

<!-- chunk {"id": "body-0128", "role": "body", "section": "VII-A Benchmarking against State-of-the-Art Methods in Static Environments", "weight": 1.0} -->

In Case 1, SUPER and FASTER suffer from a low success rate. A common failure mode for SUPER is that the LiDAR does not provide sufficient point cloud coverage below the drone (the downward angle of Livox Mid-360 is -7.22 degrees), causing the drone to crash into the lower parts of obstacles. EGO-Swarm and DYNUS achieved a 100% success rate; however, DYNUS outperformed EGO-Swarm in terms of travel time and path length. In terms of planning computation time, EGO-Swarm achieves the fastest computation time, followed by DYNUS. Note that compared to FASTER, which also uses a hard constraint MIQP-based trajectory optimization method, DYNUS achieves a shorter total planning time due to its variable elimination technique. Also note that FASTER and SUPER generate only a single safe trajectory, while DYNUS parallelizes safe trajectory optimization and generates up to 15 safe trajectories.

<!-- chunk {"id": "body-0129", "role": "body", "section": "VII-A Benchmarking against State-of-the-Art Methods in Static Environments", "weight": 1.0} -->

In Case 2, FASTER and DYNUS achieved a 100% success rate, while SUPER and EGO-Swarm suffered from a low success rate. This is consistent with the observation in HDSM that the performance of EGO-Swarm degrades in high-speed scenarios. Further note that DYNUS achieved the fastest travel time and a shorter computation time compared to FASTER.

<!-- chunk {"id": "body-0130", "role": "body", "section": "VII-A Benchmarking against State-of-the-Art Methods in Static Environments", "weight": 1.0} -->

Global Path Plan
Exp. Traj. Opt.
Safe Traj. Opt

<!-- chunk {"id": "body-0131", "role": "body", "section": "VII-B DYNUS in Dynamic Environments", "weight": 1.0} -->

This section showcases the ability of DYNUS to navigate in dynamic unknown environments and compares DGP to Dynamic A\*. Fig. shows the simulation environment in which we generated dynamic obstacles following a trefoil knot trajectory, with randomized parameters including initial position, scale, time offset, and speed. A total of 20 obstacles (modeled as $1m$ cubes) were spawned at evenly spaced intervals along the $x$-axis, with their $y$ and $z$ positions uniformly sampled from a predefined range. Each obstacle follows a parametric trefoil trajectory with different spatial and time scaling. The dynamic constraints are ${\mathbf{v}}_{\text{max}} = 10.0$ $\ {m/s}$, ${\mathbf{a}}_{\text{max}} = 20.0$ $\ {m/s^{2}}$, and ${\mathbf{j}}_{\text{max}} = 30.0$ $\ {m/s^{3}}$.

<!-- chunk {"id": "body-0132", "role": "body", "section": "VII-B DYNUS in Dynamic Environments", "weight": 1.0} -->

Table III summarizes the benchmarking results, and Fig. shows the detailed time sequence of DYNUS's navigation, where the agent optimally balances tracking obstacles and visibility in the direction of motion. Both DGP and Dynamic A\* achieved a 100% success rate, and DGP outperformed Dynamic A\* in terms of travel time and computation time. Table III also shows DYNUS's fast yaw computation time ---its decoupled yaw optimization approach achieves faster computation than coupled yaw optimization methods such as PUMA.

<!-- chunk {"id": "body-0133", "role": "body", "section": "VII-C DYNUS's Performance in Various Environments on UAV, Wheeled Robot, and Quadruped Robot Platforms", "weight": 1.0} -->

This section tests DYNUS's ability to navigate in various environments, including photorealistic forests, office, and cave environments, using the UAV, wheeled robot, and quadruped robot platforms. For each environment, the agent's trajectory, point cloud, and camera view are presented. The trajectory is color-coded according to the velocity profile.

<!-- chunk {"id": "body-0134", "role": "body", "section": "VII-C DYNUS's Performance in Various Environments on UAV, Wheeled Robot, and Quadruped Robot Platforms", "weight": 1.0} -->

First, we test DYNUS in a photo-realistic forest environment. Unlike the previous simulation environments, this setting includes trees with branches and smaller obstacles. This test evaluates the ability of DYNUS to navigate highly cluttered, unknown, static environments. Fig. shows DYNUS navigating through a dense forest populated with realistic high-resolution trees.

<!-- chunk {"id": "body-0135", "role": "body", "section": "VII-C DYNUS's Performance in Various Environments on UAV, Wheeled Robot, and Quadruped Robot Platforms", "weight": 1.0} -->

We then tested DYNUS in an office environment that contains many dead ends and walls. We gave the agent three different goals to test its ability to navigate the office environment from the same starting position. This environment evaluates DYNUS's ability to fly in unknown, confined spaces and its ability to escape and recover from dead-end situations. Fig. and 1(b) ‣ DYNUS: Uncertainty-aware Trajectory Planner in Dynamic Unknown Environments") showcases the office simulation environment and results. DYNUS encounters numerous dead-ends but successfully recovers and reroutes to reach the goal.

<!-- chunk {"id": "body-0136", "role": "body", "section": "VII-C DYNUS's Performance in Various Environments on UAV, Wheeled Robot, and Quadruped Robot Platforms", "weight": 1.0} -->

We also test DYNUS's exploration capabilities in a cave environment, as shown in Fig.. The cave is extremely confined, and DYNUS is tasked with exploring the space and locating a person inside. Person detection is performed in real-time using. This test evaluates DYNUS's ability to explore unknown, confined environments and detect target objects. For the cave simulation, the exploration algorithm described in Section VI is utilized to guide the agent through the environment. The figures in Fig. display the point cloud data generated by the agent and the corresponding exploration trajectory. The top-right figure shows the detection of a person by the model, and the bottom-left figure in the top figure shows the drone's onboard light illuminating the cave. DYNUS successfully explores the space while avoiding collisions with walls and safely ascending the vertical shaft.

<!-- chunk {"id": "body-0137", "role": "body", "section": "VII-D 2D Performance ---Wheeled Robot and Quadruped Robot", "weight": 1.0} -->

To evaluate DYNUS's collision-avoidance ability on different platforms, we tested it on both a wheeled ground robot and a quadruped robot. DYNUS's trajectory for the robots is tracked using a geometric controller. The simulations are performed in a cluttered static forest environment. The quadruped robot is simulated using the Unitree Go2 ROS2 simulator. The dynamic constraints for the wheeled robot are set to ${\mathbf{v}}_{\text{max}} = 1.0$ $\ {m/s}$, ${\mathbf{a}}_{\text{max}} = 5.0$ $\ {m/s^{2}}$, and ${\mathbf{j}}_{\text{max}} = 10.0$ $\ {m/s^{3}}$.

<!-- chunk {"id": "body-0138", "role": "body", "section": "VII-D 2D Performance ---Wheeled Robot and Quadruped Robot", "weight": 1.0} -->

For the quadruped robot, the constraints are set to ${\mathbf{v}}_{\text{max}} = 0.5$ $\ {m/s}$, ${\mathbf{a}}_{\text{max}} = 5.0$ $\ {m/s^{2}}$, and ${\mathbf{j}}_{\text{max}} = 10.0$ $\ {m/s^{3}}$. These constraints are lower than those used for the quadrotor to mitigate tracking errors introduced by the lower-level controller. For the Unitree Go2, we used a Velodyne LiDAR sensor. Fig. shows that DYNUS successfully enables both ground robots to navigate the environment.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Hardware Experiments", "weight": 1.0} -->

To evaluate the performance of DYNUS, we conduct hardware experiments on three platforms: a UAV, a wheeled robot, and a quadruped robot. For perception, we use a Livox Mid-360 LiDAR sensor, and for localization, we use onboard DLIO. DYNUS runs on an Intel^™^ NUC 13 across all platforms. For low-level UAV control, we use PX4 on a Pixhawk flight controller. All perception, planning, control, and localization modules run onboard in real time, enabling fully autonomous operations.

<!-- chunk {"id": "body-0140", "role": "body", "section": "VIII-A UAV in Static Environments", "weight": 1.0} -->

We first evaluate DYNUS on a UAV operating in static indoor environments. Fig. shows the UAV platform used in our experiments. We custom-designed and 3D-printed a protective frame for the propellers, a shelf for the Intel NUC, and a mounting stage for the Livox Mid-360 with additional housing for protection.

<!-- chunk {"id": "body-0141", "role": "body", "section": "VIII-A UAV in Static Environments", "weight": 1.0} -->

Static obstacles are placed in an ${{8\text{m}} \times 20}\text{m}$ area, and the UAV is tasked with flying from the start position at ${(0,0,1.5)}\text{m}$ to the goal at ${(18,0,1.5)}\text{m}$. Experiment 1 has more static obstacles, making the space cluttered, while Experiment 2 has fewer obstacles. In Experiment 1, the dynamic constraints are set to $v_{\max} = {2.0\text{m/s}}$, $a_{\max} = {5.0\text{m/s}^{2}}$, and $j_{\max} = {10.0\text{m/s}^{3}}$.

<!-- chunk {"id": "body-0142", "role": "body", "section": "VIII-A UAV in Static Environments", "weight": 1.0} -->

In Experiment 2, the dynamic constraints are set to $v_{\max} = {8.0\text{m/s}}$, $a_{\max} = {15.0\text{m/s}^{2}}$, and $j_{\max} = {30.0\text{m/s}^{3}}$ for faster flight. Fig. shows the resulting trajectory visualized in RViz, along with the occupancy map, point cloud, and safe corridors used for planning in Experiment 1. The UAV successfully completes the mission by navigating through narrow passages and avoiding all static obstacles.

<!-- chunk {"id": "body-0143", "role": "body", "section": "VIII-A UAV in Static Environments", "weight": 1.0} -->

Fig. shows the trajectory of Experiment 2, where DYNUS achieved a maximum of $4.9\ {m/s}$ and successfully reached the goal.

<!-- chunk {"id": "body-0144", "role": "body", "section": "VIII-B UAV in Dynamic Environments", "weight": 1.0} -->

To evaluate DYNUS in dynamic environments, we conducted hardware experiments involving one and two dynamic obstacles that were created by attaching approximately $2.0\ m$-tall foam rectangular boxes to a wheeled robot. In Experiments 3 and 4, a single obstacle moved at a constant speed of $0.4\ {m/s}$ within an ${{8\text{m}} \times 10}\text{m}$ area, periodically blocking the UAV's path. Experiments 5 and 6 have one dynamic obstacle and several static obstacles randomly placed in an ${{8\text{m}} \times 20}\text{m}$ area. In Experiments 7 to 10, two dynamic obstacles and multiple static obstacles were placed in the same ${{8\text{m}} \times 20}\text{m}$ environment.

<!-- chunk {"id": "body-0145", "role": "body", "section": "VIII-B UAV in Dynamic Environments", "weight": 1.0} -->

Unlike simulations that utilize both LiDAR and depth cameras, the hardware experiments relied solely on a LiDAR sensor for perception to reduce computational load. Figs. to illustrate the results of Experiments 3 through 11. Each figure presents time-lapse snapshots of the UAV's trajectory as it navigates around dynamic obstacles. In all cases, DYNUS successfully plans and executes safe trajectories in dynamic environments.

<!-- chunk {"id": "body-0146", "role": "body", "section": "VIII-B UAV in Dynamic Environments", "weight": 1.0} -->

For the faster flights in Experiments 9 and 10, the UAV reached maximum speeds of $5.6\ {m/s}$ and $4.6\ {m/s}$, respectively. In Experiment 9, although DYNUS commanded a maximum velocity of $4.6\ {m/s}$ to respect the dynamic constraint of $5.0\ {m/s}$, the lower-level controller commanded a peak velocity of $5.6\ {m/s}$ to maintain tracking performance.

<!-- chunk {"id": "body-0147", "role": "body", "section": "VIII-C Ground Robots in Static Environments", "weight": 1.0} -->

We also evaluate DYNUS on ground robots ---a wheeled robot and a quadruped robot ---operating in a static environment. Figs. and show both robots successfully navigating while avoiding static obstacles. Each robot is equipped with a Livox Mid-360 LiDAR and an Intel^™^ NUC 13. As with the UAV experiments, all modules ---including perception, planning, control, and localization ---run onboard in real time, enabling fully autonomous operation.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this paper, we present DYNUS, an uncertainty-aware trajectory planning framework for dynamic, unknown environments. DYNUS navigates across diverse settings, including unknown, confined, cluttered, static, and dynamic spaces. It integrates a spatio-temporal global planner (DGP), a framework for handling dynamic obstacle unpredictability, and a variable elimination-based local optimizer for fast, safe trajectory generation. We validate DYNUS in simulation across forests, office spaces, and caves, and on hardware with UAV, wheeled, and legged robots. Future work will implement larger-scale deployments and further computational improvements.
