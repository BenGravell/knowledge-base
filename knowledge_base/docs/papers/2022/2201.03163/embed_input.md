<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Continuous-Curvature Target Tree Algorithm for Path Planning in Complex Parking Environments

Topics include Path planning, Parking, Clothoid, Curvature continuity, Rapidly-exploring random tree, Target tree, Autonomous vehicles.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends the target tree algorithm - “Model-based decision making with imagination for autonomous parking” by Feng, Chen, Chen, and Zheng - for autonomous parking by replacing circular/straight path segments with clothoid curves to achieve continuous curvature (G2). Introduces an obstacle-aware cost function for target tree construction to reduce planning time in complex environments. Combined with RRT* and shortest-path selection, yields near-optimal continuous-curvature parking solutions.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Rapidly-exploring random tree (RRT) has been applied for autonomous parking due to quickly solving high-dimensional motion planning and easily reflecting constraints. However, planning time increases by the low probability of extending toward narrow parking spots without collisions. To reduce the planning time, the target tree algorithm was proposed, substituting a parking goal in RRT with a set (target tree) of backward parking paths. However, it consists of circular and straight paths, and an autonomous vehicle cannot park accurately because of curvature-discontinuity. Moreover, the planning time increases in complex environments; backward paths can be blocked by obstacles. Therefore, this paper introduces the continuous-curvature target tree algorithm for complex parking environments. First, a target tree includes clothoid paths to address such curvature-discontinuity. Second, to reduce the planning time further, a cost function is defined to construct a target tree that considers obstacles. Integrated with optimal-variant RRT and searching for the shortest path among the reached backward paths, the proposed algorithm obtains a near-optimal path as the sampling time increases.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Experiment results in real environments show that the vehicle more accurately parks, and continuous-curvature paths are obtained more quickly and with higher success rates than those acquired with other sampling-based algorithms.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Path planning is a key component in autonomous parking tasks. Path planning methods for parking need to satisfy the following conditions. First, a collision-free path should be planned considering various obstacles around the parking spot. Second, the parking path should be obtained within a short planning time, even in complex parking situations. Third, the path needs to be a continuous-curvature path for the autonomous vehicle to track and park accurately. In other words, the method needs to consider the vehicle's kinematic constraints, such as minimum turning radius and maximum steering velocity.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Various path planning methods take the abovementioned conditions into account, such as geometric, optimization-based, grid search-based, and sampling-based methods. A geometric method plans the parking path in a short planning time by a combination of simple geometric curves that considers the vehicle's constraints. However, this approach may fail to find the path in complex parking environments where the road is narrow due to obstacles near the parking spot. Optimization-based methods have been applied in various parking situations; they formulate the path planning problem as an optimization problem. This optimization problem needs to be convexified to find the path within a short planning time. A grid search-based method searches the parking path in a grid unit while considering the vehicle's constraints. This technique can certainly find the path and needs a short planning time in simple parking situations. However, the path quality depends on the grid resolution. The planning time can increase with a higher grid resolution.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Rapidly-exploring random tree (RRT), a typical sampling-based method, was studied for parking. RRT is guaranteed to find a collision-free path, if one exists, and the path does not depend on the discretization. Compared with the optimization- and grid search-based methods, RRT can plan the path within a shorter planning time when the road is narrow and obstacles surround the parking spot. Nevertheless, the planned path may vary in accordance with random samples. Furthermore, the planning time can be further increased by the low probability that the random sample is connected to the tree without collisions at a narrow parking spot and in a narrow road.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The target tree algorithm was proposed to find the parking path in a shorter planning time than RRT path planning algorithm. The target tree algorithm substitutes a parking goal in RRT with a set (target tree) of backward parking paths, and each backward path consists of candidate goals. If one of the candidate goals is reached by RRT, then the parking path is found. The target tree algorithm can reduce the planning time by building the backward parking paths in advance such that narrow regions need not be searched by RRT. However, the autonomous vehicle cannot easily track the path and park accurately due to the curvature-discontinuity between the circular and straight paths in the target tree. A parking path with such curvature-discontinuity does not take into account the vehicle's steering velocity. Moreover, the target tree should be constructed considering the obstacles in complex parking environments to reduce the planning time. This is because the planning time can be further increased or decreased according to the narrow regions covered by the target tree.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address these limitations, this paper presents the continuous-curvature target tree algorithm for complex autonomous parking situations. First, the proposed target tree algorithm builds a continuous-curvature target tree, which considers the vehicle's maximum steering velocity. This target tree allows the vehicle to track the path and park more accurately than it can with using the original target tree algorithm. Second, a cost function is proposed to construct a target tree that considers obstacles in complex parking situations. The target tree that can minimize the area to be searched by RRT is identified by using this cost function, and the planning time is reduced. The proposed algorithm is integrated with optimal-variant RRT (RRT\*) and searches for the minimum-length path among the randomly reached candidate goals, thereby obtaining a shorter parking path within the given sampling time.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Related Works", "weight": 1.0} -->

The path planning methods for autonomous parking can be categorized into four groups: geometric, optimization-based, grid search-based, and sampling-based methods.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Related Works", "weight": 1.0} -->

Geometric methods are presented. These methods plan a path on which the vehicle drives out of the parking spot with a set of geometric curves, such as a circular arc or a straight line, and find a path connecting this path to the vehicle's initial pose using other geometric curves. Geometric methods are simple and can plan the parking path with a shorter planning time than can optimization-, grid search-, and sampling-based methods. However, geometric approaches may fail to find the path in complex parking situations where the road is narrow due to obstacles near the parking spot. Moreover, their use can be limited due to the assumption that the path contains one forward/backward direction switch.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Related Works", "weight": 1.0} -->

Optimization-based methods formulate parking path planning as an optimal control problem (OCP), and solve it by numerical optimization. These methods can consider desired parking behaviors as the objective function, such as minimization of the number of forward/backward direction switches, minimization of path length, or maximization of the obstacle clearance of the path. Any vehicle's kinematic constraints can be considered by the equality/inequality constraints. However, the optimization problem needs to be convexified to find the path within a relatively short time. Approximating complex parking situations to be convexified can be difficult, and an inaccurate path can be obtained.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Related Works", "weight": 1.0} -->

Grid search-based methods were applied for parking path planning. A grid search-based path planning approach, such as Hybrid-A\*, discretizes the configuration space as a set of grids and incrementally searches these grids to find the path. This method is guaranteed to find a collision-free path if the path exists, and this parking path can be obtained within a short planning time in simple parking situations. However, high-resolution grids can be required for parking paths when parking needs several forward/backward direction switches. These high-resolution grids can exponentially increase the planning time.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Related Works", "weight": 1.0} -->

A sampling-based method, typically RRT, finds the path by incrementally searching the configuration space through random samples. It does not depend on the discretization of the grids, and the path can be obtained within a shorter planning time in complex parking situations than can optimization- and grid search-based methods. However, as mentioned in Section I, the parking path may vary, and the planning time can be increased by narrow regions. RRT\* can keep the parking path from varying through a tree-rewiring step, but this step requires further planning time. There are bidirectional approaches that reduce the planning time by growing another tree from the parking spot and connecting the two trees. These approaches can search for a narrow parking spot in advance. However, the planning time can increase if the two trees grow toward directions that are difficult to connect.

<!-- chunk {"id": "body-0015", "role": "body", "section": "IV-A Continuous-Curvature Target Tree", "weight": 1.0} -->

The proposed continuous-curvature target tree addresses the curvature-discontinuity of the original target tree by using a clothoid path. A clothoid path was used to find a continuous-curvature path by addressing the curvature-discontinuity between straight lines and circular arcs. Motivated by these works, the continuous-curvature target tree in the present work is defined as a set of backward parking paths with continuous curvature by including a clothoid path between the straight and circular paths. In contrast to the original target tree, the continuous-curvature target tree considers not only the vehicle's minimum turning radius but also its steering velocity.

<!-- chunk {"id": "body-0016", "role": "body", "section": "IV-A Continuous-Curvature Target Tree", "weight": 1.0} -->

The vehicle model for the continuous-curvature target tree is defined as a kinematic bicycle model, and additionally considers the curvature derivative of the path. The vehicle model is defined as

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-A Continuous-Curvature Target Tree", "weight": 1.0} -->

where $(x,y)$ is the position of the center of the rear axle. $\theta$ means the orientation of the vehicle. $L$ is the wheelbase of the vehicle, and $\delta$ is the vehicle's steering angle. $d$ is the forward or backward direction of the vehicle. $( \bullet^{\prime})$ means the derivative with respect to the path length. $\kappa$ ($= \theta^{\prime}$) is the curvature of the path. $\sigma$ means the sharpness, the curvature derivative. The sharpness is related to $\delta^{\prime}$, the vehicle's steering velocity of the front wheels ($\kappa^{\prime} = \frac{\delta^{\prime}}{Lcos^{2}{(\delta)}}$). The curvature of the path $\kappa$ and its derivative $\sigma$ are constrained by ${|\kappa|} \leq \kappa_{\text{max}}$ and ${|\sigma|} \leq \sigma_{\text{max}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-A Continuous-Curvature Target Tree", "weight": 1.0} -->

The continuous-curvature target tree is divided into perpendicular and parallel parking cases (see Fig. 2). For perpendicular parking, the continuous-curvature target tree consists of straight, clothoid, and circular paths (left part of Fig. 2(a)). For parallel parking, the continuous-curvature target tree is designed by adding a set of backward and forward circular paths, and a clothoid path (right part of Fig. 2(a)). The vehicle can be parked by aligning it to the parking spot by moving forward and backward via these additional paths.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Continuous-Curvature Target Tree", "weight": 1.0} -->

The clothoid path is a path of which curvature is changed linearly by the path length. The curvature, $\kappa$, is described as

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A Continuous-Curvature Target Tree", "weight": 1.0} -->

where $s$ is the path length. In Fig. 2(b), the curvature of the clothoid path (cyan line) is initially zero. It is changed linearly from zero to the maximum curvature, $\kappa_{\text{max}}$, by the sharpness, $\sigma$, as the slope in the path length and curvature plot. After the clothoid path, the vehicle's configuration, $q_{cl}$, can be derived with respect to the $xy$-axis in Fig. 2(a), given as

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-A Continuous-Curvature Target Tree", "weight": 1.0} -->

The sharpness, $\sigma$, is changed within $\{{- \sigma_{\text{max}}},\ldots,\sigma_{\text{max}}\}$ to build the branches of the continuous-curvature target tree. For example, the branch of the target tree in the left part of Fig. 2(a) (the green, cyan and red lines) is constructed by setting the sharpness as $\sigma_{\text{max}}$. As the sharpness, $\sigma$, decreases from $\sigma_{\text{max}}$ to $- \sigma_{\text{max}}$, the other branches are formed. At each branch, when the clothoid path's curvature becomes the maximum curvature, $\kappa_{\text{max}}$, the circular path whose radius is $\kappa_{\text{max}}^{- 1}$ (red line) is added to the end of the clothoid path (see Fig. 2(b)).

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A Continuous-Curvature Target Tree", "weight": 1.0} -->

If the curvature does not reach the maximum curvature due to collisions, the branch will consist of straight and clothoid paths.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-A Continuous-Curvature Target Tree", "weight": 1.0} -->

For parallel parking, a set of circular paths, and a clothoid path are added to the straight and turning paths. This set of circular paths was proposed in as a method by which a vehicle drives out of a parking spot in parallel parking. The continuous-curvature target tree for parallel parking is described in Fig. 2(c). The backward circular path is built by the vehicle driving backward from the parking spot, $q_{goal}$, to approach the rear obstacle without collisions. The vehicle's direction is switched to forward, and the forward circular path is added. If the vehicle can drive out of the parking spot with these circular paths, the clothoid path whose curvature is changed from $\kappa_{\text{max}}$ to zero is added to the end of this forward circular path. Otherwise, another set of backward and forward circular paths is added, and the above steps is repeated. For example, in the right part of Fig. 2(a), two sets of backward and forward circular paths, and the clothoid path are built. The number of sets of circular paths is increased as the dimensions of the parking spot are decreased.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Cost Function for Reducing Planning Time in Complex Parking Environments", "weight": 1.0} -->

The cost function is proposed to determine the target tree that can reduce the planning time. The target tree that covers a larger area of the road for a parking situation is identified, by calculating the cost of the target tree. This is because the area to be searched by RRT can be reduced if the road could be covered widely by the target tree. In this regard, the planning time can be reduced further if the target tree covers a larger area of the road. The larger the area that the target tree covers, the lower the cost of the target tree.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B Cost Function for Reducing Planning Time in Complex Parking Environments", "weight": 1.0} -->

Examples for calculating the cost of the target tree are shown in Fig. 3. The cost function uses the area covered by the turning path of the target tree. The area is divided into two portions with respect to the straight path of the target tree. It is represented as the red rectangles. Each portion is calculated by the length and width of each rectangle. The length (width) is defined as the maximum distance of the turning path along the $x$-axis ($y$-axis). The cost function is defined as

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B Cost Function for Reducing Planning Time in Complex Parking Environments", "weight": 1.0} -->

where $x_{b}$ and $y_{b}$ are the coordinates at the end of each branch $b$ in the target tree. $B_{k}$ means the set of the branches at {Left, Right} in the target tree in Fig. 3. $\max_{{\forall b} \in B_{k}}{|x_{b}|}$ and $\max_{{\forall b} \in B_{k}}{|y_{b}|}$ are the length and width, respectively. Thus, $A_{k}$ means the area of each red rectangle, and $\Sigma_{k}A_{k}$ means the area covered by the turning paths of the target tree (see Fig. 3). $l_{\text{max}}$ and $w_{\text{max}}$ are the length and width, respectively, when there are no obstacles blocking the turning paths of the target tree.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-B Cost Function for Reducing Planning Time in Complex Parking Environments", "weight": 1.0} -->

In the case of Fig. 3 (top-left), $l_{\text{max}}$ becomes the length of the turning path. $w_{\text{max}}$ is calculated by the distance of the turning path along the $y$-axis, in the leftmost branch. Hence, $2l_{\text{max}}w_{\text{max}}$ in denotes the area covered by the target tree when there are no obstacles, and it is depicted as the green rectangles. ${({\Sigma_{k}A_{k}})}/{({2l_{\text{max}}w_{\text{max}}})}$ in becomes the ratio of the area covered by the target tree in the parking situation to the area covered by the target tree when there are no obstacles around the turning paths.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-B Cost Function for Reducing Planning Time in Complex Parking Environments", "weight": 1.0} -->

The proposed target tree algorithm initializes the target tree using, as detailed in Algorithm 2.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Cost Function for Reducing Planning Time in Complex Parking Environments", "weight": 1.0} -->

For determining the target tree that considers obstacles, continuous-curvature target trees are built by changing the length of the straight path, $l$, from zero to the length of the parking spot, $l_{parking}$, by intervals of $\alpha$ (lines 2-6 in Algorithm 2). The $cost$ of each target tree is calculated by the proposed cost function in (line 4 in Algorithm 2). For example, in parking situation #1 in Fig. 3, the $cost$ of the target tree is calculated with different lengths of the straight path, $l$. The continuous-curvature target tree, $T_{target}$, with minimum $cost$ is selected among those target trees (line 7 in Algorithm 2).

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-C Minimum-Length Path Selection for Finding Shorter Parking Path", "weight": 1.0} -->

The proposed target tree algorithm finds a shorter parking path by integrating with RRT\* and executing the minimum-length path selection step. RRT\* rewires a tree (denoted as $T$ in Algorithm 1) to reduce the length of the RRT\* path that connects $q_{init}$ to a reached candidate goal, $q_{new}$. The proposed path selection step searches for a shorter parking path among the randomly reached candidate goals of the target tree within the sampling time ($t_{max}$ in Algorithm 1).

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-C Minimum-Length Path Selection for Finding Shorter Parking Path", "weight": 1.0} -->

The minimum-length path selection step replaces lines 10 and 11 in Algorithm 1. First, several candidate goals of the target tree reached by the RRT\* tree, $T$, are stored within the sampling time. This is because, even after the first parking path is obtained, RRT\* paths that reach other candidate goals may be found during the additional time for a tree-rewiring step. Lines 10 and 11 in Algorithm 1 are replaced,

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-C Minimum-Length Path Selection for Finding Shorter Parking Path", "weight": 1.0} -->

where $q_{new}$ is the candidate goal in the target tree reached by the RRT\* tree, $T$. $Q_{soln}$ is a set of these goals. Next, the minimum-length path selection step is added as follows,

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-C Minimum-Length Path Selection for Finding Shorter Parking Path", "weight": 1.0} -->

In the GetMinimumLenPath function, the shortest parking path is returned among a set of the reached candidate goals, $Q_{soln}$. This function is executed when one of the candidate goals is reached or when the RRT\* tree, $T$, is rewired. This minimum-length path selection step allows the target tree algorithm to find a shorter parking path as the sampling time increases. It is similar to the RRT\* path planning algorithm, which finds a shorter path by adding a tree-rewiring step to RRT. The path selection step can also be used when the cost function for tree rewiring considers not only the path length but also other costs such as the number of forward/backward direction switches, and obstacle clearance.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

The proposed algorithm was tested with an autonomous vehicle in real parking environments. The hardware configuration of the autonomous vehicle is shown in Fig. 4. The proposed target tree algorithm was implemented with Open Motion Planning Library (OMPL). The vehicle's dimensions and path planning parameters are described in Table I.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

The hybrid curvature (HC) tree-extension function was used when the proposed target tree algorithm was integrated with RRT\* for planning the continuous-curvature parking path. A kanayama controller was used for tracking the parking path. The controller received the vehicle's position and orientation relative to the path and curvature of the path as inputs, and the vehicle's input steering angle was calculated. The vehicle's maximum velocity was set to 4 km/h and 2 km/h when tracking the RRT path and the backward parking path of the target tree, respectively. The vehicle's velocity was decreased in an inversely proportional manner to the path's curvature. At the forward/backward direction switch, the vehicle stops for 3 s to change the steering angle. The LeGO-LOAM algorithm was used to obtain the vehicle's position and orientation relative to the path.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-A1 Experiments for continuous-curvature target tree", "weight": 1.0} -->

In the first experiment, the effectiveness of the continuous-curvature target tree was evaluated. The continuous-curvature target tree algorithm with RRT\* and HC tree-extension function was compared with i) the original target tree algorithm with RRT and ii) the original target tree algorithm with RRT\* and HC tree-extension function. The parking path was planned by each algorithm, and the autonomous vehicle tracked the path and parked in perpendicular and parallel parking situations. The first experiment was repeated five times for each algorithm, and the path tracking and parking alignment errors were measured.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-A2 Experiments for cost function", "weight": 1.0} -->

In the second experiment, the effectiveness of the proposed cost function was evaluated. The path planning time was measured when the parking path was planned with the target tree determined by the proposed cost function. The parking situations included a parallel-parked vehicle near the parking spot, in which parking required considering a narrow region (the road width was reduced to about 3.5 m), i.e., a complex parking environment. Continuous-curvature target trees with different $cost$s were built in each parking situation. Each target tree was built by discretely changing the length of the straight path by the interval, $\alpha$ (Algorithm 2). The interval, $\alpha$ was set to 0.2 m considering the road width and the dimensions of the parallel-parked vehicle. The proposed algorithm (using the minimum-$cost$ target tree) was compared with the target tree algorithm with higher-$cost$s target tree. Also, it was compared with other sampling-based algorithms for parking, which uses informed-RRT\* and bidirectional-RRT\*, respectively. In, the RRT\* tree was built from the parking spot, and informed sampling was applied to reduce the planing time.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-A2 Experiments for cost function", "weight": 1.0} -->

In, bidirectional tree growth was combined with RRT\* to deal with a narrow parking spot. The path was planned 100 times for each algorithm. The path length, planning time, and planning success rate were measured. The maximum sampling time in RRT\* ($t_{max}$ in Algorithm 1) was set to 3 s for considering the tree-rewiring step. The path planning was deemed to have failed when the path was not found within the sampling time. The cost function for tree rewiring considered the path length.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-B1 Analysis of results and discussion of continuous-curvature target tree experiments (Section V-A1)", "weight": 1.0} -->

The results of the first experiment where the vehicle tracks the path and parks are shown in Fig. 5. The parking result of the proposed algorithm is shown in a video^11^1 The cross-track error, which is the shortest distance between the vehicle's position and the closest point on the path while tracking the path, was calculated when the vehicle tracked the target tree path. The lateral/orientation parking alignment errors were calculated by comparing the vehicle's pose and the parking goal when the vehicle was parked. These parking alignment errors are criteria for determining whether a vehicle is parked properly.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-B1 Analysis of results and discussion of continuous-curvature target tree experiments (Section V-A1)", "weight": 1.0} -->

As seen in Fig. 5, the proposed target tree algorithm planned parking paths, where the vehicle tracked and parked with fewer tracking and parking errors. The input steering angle was calculated considering the steering velocity, and the vehicle's steering angle (red solid line) was controlled with the input steering angle (red dashed line) without error. When the vehicle was parked, in the proposed algorithm, all four wheels of the vehicle did not invade the parking line in contrast to the original algorithm. In the perpendicular parking case, the lateral and orientation alignment errors were reduced by more than half compared with the case of the original target tree. In the parallel parking case, the lateral alignment error was not significantly reduced because the vehicle moved forward and backward several times near the parking spot. Nevertheless, these direction switches reduced the orientation alignment error by one-third compared with the tracking with the original target tree.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-B2 Analysis of results and discussion of cost function experiments (Section V-A2)", "weight": 1.0} -->

The results of the path planning experiments in parking environments with narrow regions are shown in Table II ‣ V-B Experimental Results ‣ V Experiments and Discussions ‣ Continuous-Curvature Target Tree Algorithm for Path Planning in Complex Parking Environments"). '#number-a, b, c, d ($cost$)' represent the target tree algorithms with different $cost$ target tree, integrated with RRT\*. The time for search, $t_{\text{tfs}}$, is the time for determining the minimum-$cost$ target tree by Algorithm 2. The time to the first path, $t_{\text{ttfp}}$, means the time for finding the first parking path within the sampling time. Continuous-curvature target trees (#number-a, b, c) are shown in Fig. 6 ‣ V-B Experimental Results ‣ V Experiments and Discussions ‣ Continuous-Curvature Target Tree Algorithm for Path Planning in Complex Parking Environments"). Each target tree had a different $cost$ with respect to the length of the straight path. In the case of #number-a, the minimum-$cost$ target tree was obtained by Algorithm 2.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-B2 Analysis of results and discussion of cost function experiments (Section V-A2)", "weight": 1.0} -->

For comparison with the original target tree algorithm, in #number-d, the original target tree was used with RRT\* to plan the parking paths.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-B2 Analysis of results and discussion of cost function experiments (Section V-A2)", "weight": 1.0} -->

#1-a (0.572, min-c o s t)

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-B2 Analysis of results and discussion of cost function experiments (Section V-A2)", "weight": 1.0} -->

#1-b (0.770)

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-B2 Analysis of results and discussion of cost function experiments (Section V-A2)", "weight": 1.0} -->

#1-c (0.878)

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-B2 Analysis of results and discussion of cost function experiments (Section V-A2)", "weight": 1.0} -->

#1-d (0.743)

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-B2 Analysis of results and discussion of cost function experiments (Section V-A2)", "weight": 1.0} -->

#2-a (0.891, min-c o s t)

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-B2 Analysis of results and discussion of cost function experiments (Section V-A2)", "weight": 1.0} -->

#2-b (0.966)

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-B2 Analysis of results and discussion of cost function experiments (Section V-A2)", "weight": 1.0} -->

#2-c (0.983)

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-B2 Analysis of results and discussion of cost function experiments (Section V-A2)", "weight": 1.0} -->

#2-d (0.952)

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-B2 Analysis of results and discussion of cost function experiments (Section V-A2)", "weight": 1.0} -->

The results show that the target tree which reduces the planning time could be determined by the proposed cost function. As shown in Table II ‣ V-B Experimental Results ‣ V Experiments and Discussions ‣ Continuous-Curvature Target Tree Algorithm for Path Planning in Complex Parking Environments"), path planning with the minimum-$cost$ target tree (-a, proposed) obtained parking paths with a shorter planning time than did the target trees with higher $costs$ (-b, -c, -d). In situation #1-a, in Fig 6 ‣ V-B Experimental Results ‣ V Experiments and Discussions ‣ Continuous-Curvature Target Tree Algorithm for Path Planning in Complex Parking Environments"), the parking path was obtained by the RRT\* tree reaching the candidate goal of the target tree without searching the narrow region near the parallel-parked vehicle. Moreover, even though additional planning time was required for determining this minimum-$cost$ target tree by Algorithm 2, the total planning time, $t_{\text{total}}$, was reduced.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-B2 Analysis of results and discussion of cost function experiments (Section V-A2)", "weight": 1.0} -->

About the target trees with higher $cost$s, the path planning time was increased, and path planning could fail. As for #1-b and #1-c, in Fig. 6 ‣ V-B Experimental Results ‣ V Experiments and Discussions ‣ Continuous-Curvature Target Tree Algorithm for Path Planning in Complex Parking Environments"), the RRT tree should be extended toward the target tree without collisions in the narrow region. This could cause path planning failure within the sampling time, and the path length was increased despite that the parking path was obtained. Consequently, further sampling time may be required. In #1-d, in Fig. 6 ‣ V-B Experimental Results ‣ V Experiments and Discussions ‣ Continuous-Curvature Target Tree Algorithm for Path Planning in Complex Parking Environments"), even if the parking path was obtained successfully within the sampling time, the planned path is curvature-discontinuous, so the vehicle could not easily track and park accurately (see Fig. 5).

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-B2 Analysis of results and discussion of cost function experiments (Section V-A2)", "weight": 1.0} -->

Compared with other sampling-based algorithms for parking, the proposed algorithm planned a path within a shorter planning time. In particular, it reduced the path length and its deviation within the given sampling time by building backward parking paths (target tree) in advance, unlike the bidirectional-RRT\* planning algorithm, which kept searching for a backward path using the tree built from the goal.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-C Completeness and Optimality Analysis for continuous-curvature target tree algorithm", "weight": 1.0} -->

This section presents an analysis of whether the probabilistic completeness of RRT or RRT\* is maintained after the integration of the proposed target tree algorithm. Additional experiments show that the proposed algorithm can find a path close to the optimal path planned by RRT\*, within a shorter sampling time than can the original target tree algorithm and other sampling-based planning algorithms for parking.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-C Completeness and Optimality Analysis for continuous-curvature target tree algorithm", "weight": 1.0} -->

In the path planning problem, $\mathcal{P}{(q_{init},q_{goal},Q_{free})}$, the probabilistic completeness of the sampling-based planning algorithm means that if a collision-free path exists, the probability of finding the path will converge to one when the number of random samples approaches to infinity. The proposed target tree algorithm does not change the completeness of RRT\*. The target tree is a set of poses constituting collision-free paths, and any pose can reach the original goal ($q_{goal}$); i.e., the target tree algorithm is complete with respect to these poses. In this regard, the target tree, $T_{target}$, can be an extended goal region ($Q_{target}$) that includes not only the original goal ($q_{goal} \in Q_{target}$) but also candidate goals that can reach this original goal.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-C Completeness and Optimality Analysis for continuous-curvature target tree algorithm", "weight": 1.0} -->

Accordingly, the proposed algorithm can be deemed to solve the path planning problem to reach this extended goal region with the RRT\* path planning algorithm, $\mathcal{P}{(q_{init},Q_{target},Q_{free})}$. Integration of the target tree algorithm and RRT\*, which are both complete, maintains the probabilistic completeness.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-C Completeness and Optimality Analysis for continuous-curvature target tree algorithm", "weight": 1.0} -->

Additional experiments were executed to discuss the optimality of the proposed algorithm, as shown in Fig. 7. The proposed target tree algorithm was compared with the original target tree algorithm with RRT\* and minimum-length path selection, and other sampling-based planning algorithms for parking. Each algorithm was run 100 times for 60 s. The dashed horizontal line in Fig. 7 is regarded as the minimum length (i.e., optimal cost) in the original RRT\* after 7200 s. The results show that the proposed target tree algorithm can obtain a parking path close to the optimal-length path (i.e., near-optimal). There are two reasons for these results. First, integrating RRT\* and the proposed minimum-length path selection step (Section IV-C) allows to find a shorter parking path (near-optimal path) as the sampling time increases (see Fig. 7). Second, the proposed minimum-$cost$ target tree (Section IV-B) contains backward parking paths similar to the backward path of the optimal path. For example, as shown in situation #1-a of Figs.

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-C Completeness and Optimality Analysis for continuous-curvature target tree algorithm", "weight": 1.0} -->

6 ‣ V-B Experimental Results ‣ V Experiments and Discussions ‣ Continuous-Curvature Target Tree Algorithm for Path Planning in Complex Parking Environments") and 7(a), a shorter parking path was found when planning a path with the proposed target tree considering obstacles.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper introduces the continuous-curvature target tree algorithm for complex parking, which addresses the limitations of the original target tree algorithm. The proposed algorithm uses a continuous-curvature target tree that additionally considers the vehicle's steering velocity. The algorithm then searches the target tree, thereby possibly reducing the planning time further in complex parking environments. Integrated with RRT\* and minimum-length path selection, the proposed algorithm finds a shorter parking path within a given sampling time. Experiment results show the practical advantages of the proposed algorithm in real parking environments. The autonomous vehicle accurately parked, with the cross-track error and lateral/orientation parking alignment error reduced by more than half compared with those of the original target tree algorithm. In addition, the continuous-curvature path was obtained within relatively short planning times of less than 127 ms for perpendicular parking and 33 ms for parallel parking, and the success rate was 100%. In particular, even in complex parking environments, the proposed algorithm found the near-optimal path more rapidly compared with not only the original target tree algorithm but also the informed-RRT\* and bidirectional-RRT\* path planning algorithms for parking. In future work, a target tree that considers the steering acceleration of the vehicle will be studied.
