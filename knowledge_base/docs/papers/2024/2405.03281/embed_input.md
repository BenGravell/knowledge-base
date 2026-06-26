<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

FDSPC: Fast and Direct Smooth Path Planning via Continuous Curvature Integration

Topics include Path planning, Smooth paths, Curvature continuity, Heuristic.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes FDSPC, a global path planner that directly produces G2 smooth paths via continuous curvature integration. It essentially uses a goal-directed heuristic for selecting (otherwise unspecified) yaw angles at sampled positions, rather than attempting to connect (x, y, yaw) boundary poses directly.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In recent decades, global path planning of robot has seen significant advancements. Both heuristic search-based methods and probability sampling-based methods have shown capabilities to find feasible solutions in complex scenarios. However, mainstream global path planning algorithms often produce paths with bends, requiring additional smoothing post-processing. In this work, we propose a fast and direct path planning method based on continuous curvature integration. This method ensures path feasibility while directly generating global smooth paths with constant velocity, thus eliminating the need for post-path-smoothing. Furthermore, we compare the proposed method with existing approaches in terms of solution time, path length, memory usage, and smoothness under multiple scenarios. The proposed method is vastly superior to the average performance of state-of-the-art (SOTA) methods, especially in terms of the self-defined S_2 smoothness (mean angle of steering). These results demonstrate the effectiveness and superiority of our approach in several representative environments.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robot motion planning has undergone significant development in recent years, and played crucial roles in various fields, such as autonomous vehicles, robot arms and unmanned aerial vehicles. However, existing commonly used path planning methods, such as search-based algorithms A\*, Dijkstra, sampling-based algorithms Rapidly-exploring Random Trees (RRT), RRT\*, extended-RRT, RRT-Connect and swarm intelligence-based algorithms Ant Colony Optimization (ACO), all yield non-continuous, zigzag global paths. Except for end-to-end approaches for robot navigation, the majority of these methods require additional smoothing or post-processing to be effectively applied to robot trajectory tracking. Moreover, during the smoothing or optimization process, the newly generated path will inevitably deviate from the original collision-free path in certain regions, resulting in additional collision re-detection and replanning. Gradient-based methods, convex optimization, and SQP-based approaches can generate smooth trajectories, but often struggle in complex environments due to high-dimensional gradient computations, reliance on convex decomposition, and sensitivity to non-convexity that demands costly iterative solving.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this letter, a fast and direct motion planning method based on continuous curvature integration (FDSPC) is proposed for mobile robot trajectory tracking on a given map, as shown in Fig. 1. The algorithm iteratively explores collision-free path segments satisfying $G^{2}$ smoothness (curvature continuity). If trapped in a local solution, it automatically backtracks to the previous optimal state to ensure feasibility. FDSPC demonstrates superior performances by comparing various indicators, including solution time, smoothness, in multiple scenarios. The contributions of this letter are as follows, A fast motion planning method based on continuous curvature integration is proposed, which can generate global paths that satisfies $G^{2}$ smoothness, avoiding the re-collision checking and smoothing.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A variant of the direct positioning binary tree combined with an ordered dictionary is introduced to facilitate heuristic search of the path rapidly and ensuring both the feasibility and efficiency of the algorithm.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A variety of evaluation indicators are compared across multiple scenarios, and successfully applied in our self-designed wheel-legged robot with four independent steering wheels in $2.5$-D terrain-based environments.

<!-- chunk {"id": "body-0008", "role": "body", "section": "II-A Classical motion planning", "weight": 1.0} -->

The motion planning problem has been around for decades, and the methods can be broadly divided into two categories, i.e., the search-based approaches and the sampling-based approaches. The former approaches discretize the environment and searches for the optimal path in the grid map. The latter methods sample in the configuration space and then find a feasible path through the sampling points. Besides, the paths generated by swarm intelligence optimization are more prone to fall into local optimum, and the optimization-based methods minimize a predefined cost function under various constraints but require a good initial value; otherwise, their efficiency and feasibility are difficult to guarantee.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-A Classical motion planning", "weight": 1.0} -->

The Greedy Best-First Search (GBFS) and $\theta^{*}$ family methods, including Lazy $\theta^{*}$, derive from classic A\*-based grid search and are well described in Planning Algorithms, where GBFS prioritizes heuristic cost leading to fast but possibly suboptimal paths, $\theta^{*}$ improves smoothness by allowing connections between non-adjacent nodes, and Lazy $\theta^{*}$ further enhances efficiency by delaying visibility checks. The $D^{*}$ algorithm, also covered, maintains a priority queue to enable efficient path replanning in dynamic environments. The Stable Sparse Rapidly-exploring Random Tree (SST) uses sparse sampling to reduce storage and computational complexity while ensuring asymptotic optimality.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-B Smooth path planning", "weight": 1.0} -->

Building upon the preceding path results, the curve planning method is crafted by amalgamating pathfinding and smoothness through the incorporation of Reed-Sheep (RS) curves, Bézier curves, or similar techniques. The hybrid A\* smooths the A\*-derived path using RS curves, ensuring that the kinematic constraints of the vehicle are followed and achieving $G^{1}$ continuity (tangency continuity). propose a hierarchical search spatial scales-based hybrid A\* (HHA\*) framework, which employs clothoids instead of RS curves, attaining $G^{2}$ continuity of the path and exhibiting commendable performance in parking scenario. Clothoids with continuous curvature expand the original motion primitive and enhance the granularity of the search space. However, clothoids are defined in terms of Fresnel integrals, making them challenging to be applied online. To address this, a lookup table is constructed to store the coordinates of basic clothoids, which accelerates calculations when dealing with other clothoids, yielding lower errors compared to approximations using Bézier or B-spline curves.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-B Smooth path planning", "weight": 1.0} -->

Nevertheless, achieving an exact approximation for the clothoid is not crucial in path planning, especially in iterative approaches, and none of the aforementioned algorithms can generate a smooth, and applicable trajectory directly and rapidly.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Smooth path planning", "weight": 1.0} -->

In this letter, a fast and direct motion planning method FDSPC, which can generate $G^{2}$ continuity trajectory without extra smoothing and take into account the obstacle-crossing ability of different robots is proposed. Unlike classical methods that plan directly in configuration or state space, FDSPC is built upon curvature-based and planning in the configuration space accordingly.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Curvature planning", "weight": 1.0} -->

The representation of a path in $n$-dimensional ($n$-D) space can be expressed as the set $\mathcal{C}$ of coordinates of discrete points $p\in\mathbb{R}^{n}$. For any curve in $n$-D space, it can be described by an $(n-1)$-D function, precisely. For example, on a $2$-D plane, the curve can be described by a $1$-D curvature $\kappa$, while in $3$-D space, the curve satisfies the continuity of curvature and torsion, and be twice differentiable in all directions by solving the $Frenet-Serret$ equations. In $n$ dimensional space, this requires solving $(n-1)$ coupled differential equations and integrating the tangent vector to obtain the path, making the process much more complex than $2$ or $2.5$-D spaces. Therefore, in this section, we focus solely on curvature planning in $2$-D plane and $2.5$-D terrain space.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Curvature planning on $2$-D plane", "weight": 1.0} -->

The relative positional relationship between path points on $2$-D plane and the obstacles is not directly discernible through the curvature. Thus, it is necessary to unfold the implicit expression, i.e., map the curvature function $\kappa$ to the path points by double integrating $\kappa$ on $2$-D plane, then evaluate the feasibility (whether the path generated collides with obstacles) and adjust the curvature accordingly. The relationship between curvature and the tangent at the path points can be expressed as, where $\theta$ is the tangent angle, $s$ is the arc length of the path, $dt$ is the integration step, $\kappa$ is the path curvature, and ${ds}/{dt}$ can be regarded as the pseudo velocity of the path (the rate of change of distance along the curve). The tangent angle $\theta(t)$ can be obtained by integrating the curvature function $\kappa(t)$ and the pseudo velocity ${ds}/{dt}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Curvature planning on $2$-D plane", "weight": 1.0} -->

The model of the curvature planning can be expressed as, | | | $\displaystyle\dot{\kappa}=\rho$ | | \(2\) | | | | $\displaystyle\dot{x}=\frac{ds}{dt}\cdot\cos\left(\theta\right)$ | | | | | | $\displaystyle\dot{y}=\frac{ds}{dt}\cdot\sin\left(\theta\right)$ | | | where $\rho$ represents the rate change of curvature, $a$ represents the pseudo acceleration along the curve.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Curvature planning on $2$-D plane", "weight": 1.0} -->

Consider $ds/dt$ to be the constant $1$, the waypoints can be strictly expressed as trigonometric functions with respect to the curvature, and the Eq. can be expressed as, In the process of path planning, collision avoidance can be achieved by adjusting the curvature $\kappa$ in Eq.. In this way, the collision-free path generated by the FDSPC algorithm can be guaranteed to have $G^{2}$-continuity. The path generated with the proposed curvature planning method under different conditions are demonstrated in Fig. 2.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-B Curvature planning in $2.5$-D terrain space", "weight": 1.0} -->

In complex $3$-D environment, the curve satisfies the continuity of curvature and torsion, must be twice differentiable in all directions. The Frenet-Serret equations are used to describe the $3$-D curve in the Frenet-Serret coordinate system. However, this method is relatively complex for pathfinding and is unnecessary for terrain-based mobile robots. In this work, we simplify the motion planning of $3$-D space to $2.5$-D path planning, which combines a continuous transformation scaling function $\tau$ in the $z$-direction and a $2$-D plane planning. The continuous variation of the curvature function $\kappa$ and the scaling function $\tau$ yields a $2.5$-D path that satisfies $G^{2}$ continuity.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-B Curvature planning in $2.5$-D terrain space", "weight": 1.0} -->

The curvature planning model in $2.5$-D space can be expressed as, where $\rho$ represents the rate of change of the curvature, $\rho_{z}$ and $\tau_{z}$ denote the rate of change and scaling function along the $z$-direction, respectively.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B Curvature planning in $2.5$-D terrain space", "weight": 1.0} -->

Once an obstacle is detected on the plane, FDSPC retreats a distance $back_{obs}$ and introduces a tilt along the $z$-axis. By comparing the $(x,y)$ coordinates of the new collision point with the original, it determines if the obstacle is crossable. If the $z$-tilt is below $\theta_{max}$, the algorithm continues $z$-axis expansion until a collision-free node is found; otherwise, it deems the obstacle uncrossable and backtracks. Two $z$-axis exploration cases are illustrated in Fig. 3.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Curvature planning in $2.5$-D terrain space", "weight": 1.0} -->

In practice, the mechanical structural and kinematics of a robot should be taken into consideration. For the path planning of the proposed wheel-legged robot, it might be favourable to keep the robot's torso height and posture stable, i.e., $\rho_{z}$ and $\tau_{z}$ in Eq. equal to $0$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-A Data structure", "weight": 1.0} -->

The path search process can be regarded as the construction of a binary tree from the root node (initial position) to the leaf nodes (target position). Each binary tree node stores path from the previous node to the current node. The node's search weight (the Euclidean distance from the current node position to the end point position) and the node's location (the node's position in the binary tree) is stored in an ordered dictionary. Whenever there arises a necessity to update and broaden potential path nodes, the location of the node with the lowest weight is popped out from the ordered dictionary, enabling a fast heuristic search of paths. The data structure of the FDSPC is illustrated in Fig. 4.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A Data structure", "weight": 1.0} -->

The path begins with the initialization of the root node in the binary tree, the destination is marked as the leaf node. Each node holds the $value$, representing the path from the preceding node to the current node. Additionally, the sequence stored in the $sequ$ attribute indicates the locating sequence in the binary tree from the root node to the current node. A corresponding node is created when a new branch point needs to be added. During expansion, the Euclidean distance from the current position to the end position is used as the $key$ (also regarded as the weight for node selection), and the locating sequence from the root node to the current node of the binary tree is viewed as the $value$. These are paired and added to the ordered dictionary. After adding a new node, prune the parent nodes in the ordered dictionary where both the left and right child nodes exist, indicating the infeasibility of further expansions.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B Smooth path planning on $2$-D plane", "weight": 1.0} -->

1 Initialize θg ← arctan 2(pstart, pgoal); 8 θg ← arctan 2(pnow, pgoal); Algorithm 1 Direct planning Dp(⋅) The direct planning part of the FDSPC is illustrated in Alg. 1. Firstly, the algorithm checks whether the current orientation can reach the target position directly (i.e., if there are no obstacles along a straight line from current position to the target). If not, it adjusts the current orientation $\theta$ iteratively by using the curvature integral until the direction $\theta_{g}$ of the line connecting the current position and the target aligns with the $\theta$. Then, the current position $P_{now}$ is updated with $\theta$ by Eq.. By assigning a curvature value of $0$ to the straight-line segment, the algorithm sequentially connects the current position to the target. Essentially, the FDSPC constructs the basic path structure by combining segments of indefinite radius arcs with straight lines. The exploration planning part of the FDSPC is illustrated in Alg. 2.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Smooth path planning on $2$-D plane", "weight": 1.0} -->

1 Initialize θt, θ0 ← arctan 2(pnow, pgoal); 3 Initialize oidx ← Od(ℱmap, κs); 4 while oidx is not empty and |θt − θ0| < π do 5 while oidx is not empty do 6 κold = κs, oidx, old = oidx; 7 lint = oidx + ladd; 22κa ← Pfimin(κold[oidx, old], κs); Algorithm 2 Explore planning Ep(⋅) Initially, $\boldsymbol{E}_{\boldsymbol{p}}(\cdot)$ establishes a connection between the current position and the endpoint along the orientation $\theta$ using a straight line, and calculates the position index of the collision. If the index is non-empty and the extension angle is less than $\pi$, it increases the extension angle $\theta_{t}$ on both sides of the obstacle progressively until the index of the collision become empty.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B Smooth path planning on $2$-D plane", "weight": 1.0} -->

The length of integration exploration $l_{int}$ is adjusted based on the position of collision index $o_{idx}$ and the linear extension length $l_{add}$ to avoid overly long exploration distances that might mistakenly identify boundaries as obstacles. In line 9 of Alg. 2, a sequence $\kappa_{s}$ of curvatures is obtained through inverse integration under specified integration length $l_{int}$, integral value $\theta_{t}$, and integration rate $\rho$. Upon the program runs into the inner while loop (line 5 to line 11, Alg. 2) for the second time, the extension angle begins increasing from the previous collision angle by increments $\theta_{a_{2}}$ ($\theta_{a_{2}}<\theta_{a_{1}}$) to refine the exploration of collision edges until the position index of the collision point is empty.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B Smooth path planning on $2$-D plane", "weight": 1.0} -->

Finally, the algorithm utilizes the ${P_{fimin}}(\cdot)$ function to locate a point $p$ on the current collision-free curvature path $\kappa_{s}$ that minimizes the distance to the previous collision position on the curvature path $\kappa_{old}$. Subsequently, the algorithm returns the collision-free curvature path $\kappa_{p}$ preceding point $p$ on $\kappa_{s}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-B Smooth path planning on $2$-D plane", "weight": 1.0} -->

In Alg. 2, if the extension angle to either side, i.e., $\left|\theta_{t}-\theta_{0}\right|$, exceeds $\pi$, the exploration node is closed. This process involves pruning the extra nodes, and then popping a new node from the binary tree $\mathcal{B}_{t}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-C Smooth path planning in $2.5$-D space", "weight": 1.0} -->

As shown in Fig. 5, if the obstacle on the plane is deemed crossable, the algorithm first identifies the point $s_{3}$ on the collision-free path that is closest to the previous point of collision $s_{2}$. It then generates a collision-free smooth path along the upward slope segment (the blue line). At point $s_{3}$, a negative $\rho_{z}$ is applied to transform the original path into a horizontal one (the green line). At point $s_{4}$, where the green path becomes horizontal, the algorithm searches for the point $s_{6}$ closest to the previous collision point $s_{5}$ on the first collision-free path from $\theta_{\textup{max}}$ to $0$. At point $s_{6}$, the algorithm searches for a ground collision point $s_{7}$ at a specified height, scanning from $0$ to $-\theta_{\textup{max}}$, and retreats $back_{obs}/2$ to $s_{8}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-C Smooth path planning in $2.5$-D space", "weight": 1.0} -->

At point $s_{8}$, a smooth path to the horizon is constructed (purple path), resulting in a smooth vertical path that crosses low obstacles.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-C Smooth path planning in $2.5$-D space", "weight": 1.0} -->

1 Initialize κd ← Dp(pstart, pgoal, θ0); 2 Initialize obsidx ← Od(ℱmap, κd); 3 update pnow, ℬt(pnow), 𝒪d(pnow); 5while obsidx ∧ ℬt is not empty do 6 κa ← Ep(ℱmap, pnow, pgoal); 7 update pnow, ℬt(pnow), 𝒪d(pnow); 10 update pnow, ℬt(pnow), 𝒪d(pnow); 14 // Find feasible path failed; Alg. 3 outlines the framework of the FDSPC. Initially, the algorithm generates an initial curvature path $\kappa_{d}$ via the direct planning function $\boldsymbol{D}_{p}(\cdot)$. Subsequently, the collision detection function $\boldsymbol{O}_{d}(\cdot)$ to assess the feasibility of the path. If a collision is detected, the algorithm retraces its steps along the collision point sequence $back_{obs}$ to determine a branch point $b$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-C Smooth path planning in $2.5$-D space", "weight": 1.0} -->

This branch point along with the collision-free branching path, is then incorporated into the binary tree $\mathcal{B}_{t}$ and the ordered dictionary $\mathcal{O}_{d}(\cdot)$. Using the exploration function $\boldsymbol{E}_{p}(\cdot)$, a short collision-free curvature path $\kappa_{a}$ is obtained. $\mathcal{B}_{t}$ and $\mathcal{O}_{d}(\cdot)$ are updated accordingly. The algorithm then iterates through the direct planning function $\boldsymbol{D}_{p}(\cdot)$ again to derive a new curvature path $\kappa_{d}$, repeating this cycle until a collision-free curvature path $\kappa_{d}$ is found. Finally, the algorithm traces back through the branches of the binary tree $\mathcal{B}_{t}$ from the endpoint leaf to obtain the final curvature path $\kappa$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-C Smooth path planning in $2.5$-D space", "weight": 1.0} -->

The algorithm selects the position of the node with the lowest weight in the popped binary tree based on the $key$ of the ordered dictionary for subsequent expansion. For the planning near obstacles, the newly added node often coincides with the position of the last expansion node after updating the collision point, as depicted in the subfigure of Fig. 7(b). This scenario poses a risk of generating pseudo-feasible paths, where all newly added paths are collision-free within the specified expansion length but do not reach the endpoint, potentially leading to premature termination of the algorithm. To mitigate this, for pseudo-feasible paths encountered in Alg. 2, we select a small segment and continue planning from the new node position. Essentially, FDSPC must begin and end with Direct planning $\boldsymbol{D}_{p}(\cdot)$, and with Explore planning $\boldsymbol{E}_{p}(\cdot)$ interspersed in between.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-D Velocity planning", "weight": 1.0} -->

Since the path obtained by FDSPC is of $G^{2}$ continuity, the corresponding velocity and acceleration functions can be generated based on the curvature $\kappa$ or $\rho_{z}$, which ultimately yields a smooth trajectory. The velocity planning function except for the beginning and ending part is as follows, where $a$ denotes the acceleration, $\kappa_{i}$ is the curvature at the $i$-th point, $\rho_{z}$ is the curvature along the $z$-axis, $v_{\max}$ and $v_{\min}$ are the maximum and minimum velocities, respectively.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-D Velocity planning", "weight": 1.0} -->

Compared with other velocity planning methods, such as those based on path coordinate positions, curvature-based velocity planning can anticipate changes in the path in advance, thereby adjusting the velocity in a timely manner to enhance the comfort of the vehicle and the stability of mobile robots. In contrast to optimization-based velocity planning methods, curvature-based velocity planning is simpler, faster, and does not require complex numerical optimization.

<!-- chunk {"id": "body-0035", "role": "body", "section": "SIMULATION AND ANALYSIS", "weight": 1.0} -->

In this section, the performance of FDSPC and some state-of-the-art methods are tested and compared five typical scenarios. Additionally, the proposed FDSPC method is also successfully applied on our self-designed wheel-legged robot to across a dike shaped obstacle.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-A Simulation results", "weight": 1.0} -->

In the validation, we constructed a randomly scattered polygonal map, as shown in Fig. 6. During the path generation, a total of 27 $\mathcal{B}_{t}$ nodes (blue points) are generated, including 3 discarded nodes (marked by red arrows). Ultimately, a path satisfying $G^{2}$ continuity is generated. Additionally, we designed five typical scenarios, including bypassing long obstacles, navigating through long corridors and semi-enclosed areas, traversing random complex and simple maze environments. The specific exploration process and the final smooth path with velocity are shown in Fig. 7.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-A Simulation results", "weight": 1.0} -->

In the bypassing-long-obstacle scenario, FDSPC successfully identifies a short and smooth path by navigating close to the obstacle edge. As shown in Fig. 7(a), 7(b), 7(d), and 7(e), aided by the heuristic function, FDSPC efficiently finds $G^{2}$-continuous paths in long corridor, random complex, and simple maze scenarios. In the semi-enclosed scenario (Fig. 7(c)), FDSPC explores both sides of the obstacle and determines that the shortest feasible path passes on the left, adding collision-free branch nodes to the binary tree (red circle). When a node is popped from the ordered dictionary, the branch in the red circle is farther from the goal and thus weighted higher. The algorithm prioritizes expansion from the unvisited (right) direction of the earlier node (red arrow). If the expansion angle exceeds $\pi$ and no valid node is found, the branch is pruned and planning continues from the next node. Across scenarios, pseudo-feasible paths are sometimes encountered.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-A Simulation results", "weight": 1.0} -->

By gradually extending these paths (e.g., two adjacent blue points in Fig. 7(b), 7(c)), FDSPC ultimately identifies smooth, feasible solutions.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-B Performance analysis", "weight": 1.0} -->

The performance of the FDSPC algorithm is compared with other algorithms in terms of path-solving time, memory usage, path length and smoothness (measured by $\mathcal{S}_{1}$ and $\mathcal{S}_{2}$). The results are presented in TableI and Fig. 8, with path smoothness calculated using Eq..

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-B Performance analysis", "weight": 1.0} -->

Mean: remove the maximum and minimum values and calculate the average of the remaining values. Time (s): seconds; Memory (MB): megabytes; Length (m): meters; 𝒮1 (deg/m): degrees per meter; 𝒮2 (deg): degrees. For all random sampling-based methods, we ran each scenario 500 times and took the average as the final result. Simulation environment: Windows 11 OS, python 3.10, AMD Ryzen 5600X CPU, 32GB RAM, RTX 4060Ti.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-B Performance analysis", "weight": 1.0} -->

However, $\mathcal{S}_{1}$ may not fully capture the smoothness of the entire path. In cases like Jump Point Search (JPS), the path consists of few discrete waypoints connected by straight lines, the resulting $\mathcal{S}_{1}$ may indicate high smoothness. Despite this, abrupt changes or sharp turns occur at these waypoints, compromising overall path smoothness. To address this, we introduced a new smoothness metric, $\mathcal{S}_{2}$, defined as the mean turning angle, which provides a more accurate representation of the path's smoothness.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-B Performance analysis", "weight": 1.0} -->

By exploring feasible trajectories through angle extensions, FDSPC outperforms traditional planners like $A^{*}$ in solving time on grid maps. Although not the most CPU-efficient, it ranks among the fastest. Unlike sampling-based methods such as RRT, FDSPC maintains stable solving times across different scenarios. In simulations, it requires many integrations to find collision-free paths, but in practice, sensors like LiDAR or depth cameras can provide distance information directly, reducing both memory usage and computation time.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-B Performance analysis", "weight": 1.0} -->

In terms of path length, FDSPC performs averagely in most scenarios but shows a significant increase in the semi-enclosed case due to the added $\theta$ dimension and large orientation deviation, leading to a nearly 180 degrees detour. For $\mathcal{S}_{1}$ smoothness, FDSPC consistently ranks among the best, slightly outperforming $\theta^{*}$ and lazy $\theta^{*}$, and matching JPS. In $\mathcal{S}_{2}$ smoothness, FDSPC excels significantly thanks to curvature-based planning, outperforming other algorithms by two orders of magnitude.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-B Performance analysis", "weight": 1.0} -->

To verify the feasibility of FDSPC, an obstacle avoidance scenario with uphill and downhill terrain is constructed in a $2.5$-D terrain-based environment, as shown in Fig. 9(a). Simulation results in Rviz and Webots are presented in Fig. 9(b) and Fig. 9(c), respectively. The hardware experiment replicates a 3.2m $\times$ 0.3m corridor with a 0.35m-high, 25 degrees ramp in the middle. The obstacle expansion radius is defined as $r_{exp}=\max\{r_{robot}+0.1,\ r_{robot}\times 1.1\}$, with $r_{robot}=0.3$m. The wheel-legged robot is equipped with an WSK i7, 16-line LiDAR, IMU, RGBD camera, 4 hub motors, 4 steering motors, and 8 joint motors, running ROS Noetic on Ubuntu 20.04. Trajectory tracking is controlled via MPC at 75 Hz and WBC at 200 Hz, as illustrated in Fig. 1(bottom).

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-B Performance analysis", "weight": 1.0} -->

The FDSPC algorithm is most sensitive to the integration step size $\Delta t$ and the linear extension length $l_{add}$, where inappropriate values may lead to planning failures. The angular increment $\theta_{a1}$ primarily affects path smoothness, with larger values significantly degrading curvature continuity. In contrast, the curvature variation rate $\rho$ has relatively minor impact on overall performance. Based on the sensitivity analysis results, the recommended parameter ranges are: $\Delta t=0.01$-$0.015$ s, $\rho=0.3$-$0.5$ m^-1^s^-1^, $\theta_{a1}=0.1$-$0.2$ rad, and $l_{add}=0.4$-$0.8$ m.

<!-- chunk {"id": "body-0046", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

In this letter, we introduced a novel motion planning algorithm FDSPC, based on continuous curvature integration. It explores feasible paths by continuous changes in curvature angles, offering high solution speed, efficient memory usage, shorter path lengths, and exceptional path smoothness. In five typical scenarios, FDSPC demonstrated superior performance, and successfully implemented in obstacle-crossing trajectories on our self-designed wheel-legged robot in a $2.5$-D terrain environment. However, FDSPC has some drawbacks: it's sensitive to parameter settings, may fail to find a path if parameters are unreasonable. In practice, using sensors like LiDAR or depth cameras can reduce integration needs, lowering memory usage and solution time.

<!-- chunk {"id": "body-0047", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

In the future, we will improve the FDSPC, reduce adjustable parameters and enhance its completeness, and aim to explore its potential as an effective initial value for mobile robot trajectory optimization.
