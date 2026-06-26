<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

NanoMap: Fast, Uncertainty-Aware Proximity Queries with Lazy Search over Local 3D Data

Topics include Motion planning, Robotics, Aerial robotics, Safety, Robustness, Uncertainty, State estimation, Planning, NanoMap.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We would like robots to be able to safely navigate at high speed, efficiently use local 3D information, and robustly plan motions that consider pose uncertainty of measurements in a local map structure. This is hard to do with previously existing mapping approaches, like occupancy grids, that are focused on incrementally fusing 3D data into a common world frame. In particular, both their fragile sensitivity to state estimation errors and computational cost can be limiting. We develop an alternative framework, NanoMap, which alleviates the need for global map fusion and enables a motion planner to efficiently query pose-uncertainty-aware local 3D geometric information. The key idea of NanoMap is to store a history of noisy relative pose transforms and search over a corresponding set of depth sensor measurements for the minimum-uncertainty view of a queried point in space. This approach affords a variety of capabilities not offered by traditional mapping techniques: (a) the pose uncertainty associated with 3D data can be incorporated in motion planning, (b) poses can be updated (i.e., from loop closures) with minimal computational effort, and (c) 3D data can be fused lazily for the purpose of planning.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We provide an open-source implementation of NanoMap, and analyze its capabilities and computational efficiency in simulation experiments. Finally, we demonstrate in hardware its effectiveness for fast 3D obstacle avoidance onboard a quadrotor flying up to 10 m/s.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Robust, fast motion near obstacles is an open problem that is central in robotics, with applications spanning across manipulation, autonomous cars, and UAV navigation in unknown environments. Although many approaches exist for planning obstacle-free motions, mapping errors due to significant state estimation uncertainty can degrade their performance. Accordingly, a notable trend in the state of the art has been to develop memoryless approaches to obstacle avoidance that use only the current depth sensor measurement. These approaches are less prone to state estimation errors, but fail to capture all available information.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Towards this goal, a primary motivation of this work was to be able to use pose uncertainty to reason about a local history of depth information. NanoMap is an algorithm and data structure that enables uncertainty-aware proximity queries for planning. While traditional mapping approaches rely on fusing a history of depth information into a discretized world frame, we propose an alternative: perform no discretization, and no fusing. Instead, the process for querying local 3D data is a search over views. When a query point (i.e. a sample along a motion plan) is provided, the history of depth information is searched for the most-recent and therefore minimum-uncertainty relative to current body frame view of that query point.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In practice, this approach offers a variety of unique capabilities not present in traditional fusion-based mapping algorithms. For one, the pose uncertainty associated with depth sensor measurements can be incorporated into planning, by treating each pose with frame-specific uncertainty relative to the current body frame (Figure 1, c). Second, since fusion between measurements is not performed, it is trivial to incorporate updated information about previous poses. Third, the build time of the data structure is low, which leads to an improvement in computational efficiency for small amounts of motion planning queries ($< {10,000}$).

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

This paper presents the design of NanoMap and our experiments in quantifying the benefits of its novel properties. We believe this work strongly demonstrates that more deeply integrating motion planning and perception can improve a system's robustness and computational efficiency. To briefly clarify our scope of work: (a) we focus on a method of incorporating pose uncertainty, but modeling the noise of the depth sensor itself is outside of scope, (b) NanoMap requires nonzero volume depth sensors, i.e. depth cameras or 3D lidars, but not 2D or 1D sensors, (c) adding more sensors to increase the FOV is a hardware route to alleviate the problem but does not address occlusions, and (d) we are concerned with local obstacle avoidance, rather than global planning, and so short histories of information are sufficient.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The contributions of this work are as follows: A novel use of frame-specific uncertainty for planning with depth sensors An approach to searching a history of depth frustums to enable motion plans to satisfy field of view constraints An efficient use of independently spatially partitioned depth measurements for motion planning queries Simulation experiments demonstrating the magnitudes of state estimation uncertainty at which frame-specific uncertainty becomes significant (approximately $1\%$ drift, or 1 $m$ pose corrections) Hardware validation demonstrating this approach onboard a quadrotor, including flight at up to $8 - 10$ $m/s$ in unknown warehouse and forest environments

<!-- chunk {"id": "body-0009", "role": "body", "section": "MOTIVATION", "weight": 1.0} -->

This work seeks a method to reason about local 3D obstacles in the presence of significant state estimation uncertainty. Our approach is guided by our experience with high-speed UAVs, the use of depth sensors for obstacle avoidance, and the planning challenges introduced by imperfect state estimation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "MOTIVATION", "weight": 1.0} -->

One key observation is that in practice, depth sensor data (Figure 1, b) is often clean enough that fusing many recent observations is not required in order to plan obstacle-free motions. Rather than averaging many measurements to create intricate 3D reconstructions, mapping for obstacle avoidance only needs to robustly determine collision-free space. Furthermore, the current or very recent depth measurements frequently contain a view of planned directions of motion (Figure 1, b). In the case that the planned trajectory does not fall within the current field of view, it is still possible to perform robust trajectory planning by using the history of depth measurements.

<!-- chunk {"id": "body-0011", "role": "body", "section": "MOTIVATION", "weight": 1.0} -->

Additionally, as shown in Figure 2, the incorporation of pose uncertainty (the acknowledgement that the robot does not perfectly know its previous positions relative to its current body frame) is a fundamentally different model of uncertainty than, for example, what is modeled in an occupancy grid. Although the Bayesian update in occupancy grids may well model 0-mean Gaussian noise of both poses and depth sensing, it does not handle the case of pose drift.

<!-- chunk {"id": "body-0012", "role": "body", "section": "FORMULATION", "weight": 1.0} -->

NanoMap is a framework composed of both a local 3D data structure and an algorithm for searching that data structure. Briefly, the algorithm works by reverse searching over time through sensor measurement views until finding a satisfactory view of a subset of space (Figure 3), and then returning the $k$-nearest-neighbors from that view's sensor measurement. Important components of the framework include: the determination of in-frame views (the IsInFOV function), the propagation of uncertainty, and efficient data structure design for handling asynchronous data inputs of point clouds, poses, and pose updates. We first describe the query algorithm, which gives insight into efficient data structure design. We then discuss details of handling asynchronous data.

<!-- chunk {"id": "body-0013", "role": "body", "section": "IV-A Querying Algorithm", "weight": 1.0} -->

The query algorithm (Algorithm 1) iteratively transforms an uncertain query point into the coordinate frames of previous sensor measurements until it finds a view which contains the query. An uncertain query point is a sampled point along a stochastic motion plan, and is provided in body frame, $\mathbf{x}_{query}^{\mathcal{B}} = {\mathcal{N}{(\mu^{\mathcal{B}},\Sigma^{\mathcal{B}})}} \in {\mathbb{R}}^{3}$. The query point in the original body frame and each of the relative transforms are each modeled with Gaussian translational uncertainty.

<!-- chunk {"id": "body-0014", "role": "body", "section": "IV-A Querying Algorithm", "weight": 1.0} -->

In each frame associated with a given sensor measurement $\mathcal{S}_{i}$, the query point $\mathbf{x}_{query}^{\mathcal{S}_{i}} = {\mathcal{N}{(\mu^{\mathcal{S}_{i}},\Sigma^{\mathcal{S}_{i}})}} \in {\mathbb{R}}^{3}$ has uncertainty specific to that frame. As noted in Algorithm 1, NanoMap is unconventional in that it also returns the uncertain query point itself transformed into a different frame. While NanoMap has been implemented to only address query points in ${\mathbb{R}}^{3}$, downstream the query return points may be inflated for spherical approximations of collision geometry.

<!-- chunk {"id": "body-0015", "role": "body", "section": "IV-A Querying Algorithm", "weight": 1.0} -->

Input: body frame query point xq u e r yℬ = 𝒩 (μℬ, Σℬ) Output: i, index of frame containing view 3 Transform query point from body frame into most recent sensor frame: xq u e r y𝒮0 ← 𝒩 (Tℬ𝒮0 μℬ, Σℬ𝒮0 + Rℬ𝒮0 Σℬ) 8 Transform query point into previous frame: xq u e r y𝒮i ← 𝒩 (T𝒮i − 1𝒮i μ𝒮i − 1, Σ𝒮i − 1𝒮i + R𝒮i − 1𝒮i Σ𝒮i − 1) return “out of known space”, xq u e r y𝒮0, Knn(μ𝒮0); Algorithm 1 NanoMap query algorithm. Subroutine IsInFOV is described in Section IV-A2; Knn is provided by a single-frame k-d-tree query. N is the number of measurements stored in memory.

<!-- chunk {"id": "body-0016", "role": "body", "section": "IV-A1 Uncertainty propagation", "weight": 1.0} -->

Accounting for uncertainty is performed as follows. The query is provided as the mean and covariance of a point in the current body frame $\mathcal{B}$ of the robot $\mathbf{x}_{query}^{\mathcal{B}} = {\mathcal{N}{(\mu^{\mathcal{B}},\Sigma^{\mathcal{B}})}}$. The query is first transformed into the frame $\mathcal{S}_{0}$ of the most recent sensor measurement, $\mu^{\mathcal{S}_{0}} = {T_{\mathcal{B}}^{\mathcal{S}_{0}}\mu^{\mathcal{B}}}$, where $T_{\mathcal{B}}^{\mathcal{S}_{0}}$ represents the local, relative transform between the current body frame and the recent sensor frame.

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-A1 Uncertainty propagation", "weight": 1.0} -->

$T_{\mathcal{B}}^{\mathcal{S}_{0}}$ is modeled with a noisy translation $\mathcal{T}_{\mathcal{B}}^{\mathcal{S}_{0}}$ with covariance $\Sigma_{\mathcal{B}}^{\mathcal{S}_{0}}$, and known rotation $R_{\mathcal{B}}^{\mathcal{S}_{0}}$. In addition to computational simplification, our choice to model translational uncertainty and not rotational is guided by the practical observation that due to gravity, IMUs provide good observability of roll and pitch, and yaw is only a single integration of a noisy gyrometer (covariance grows $\propto N$ for $N$ measurements), whereas positions are double integration of the accelerometer (covariance grows $\propto N^{3}$).

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-A1 Uncertainty propagation", "weight": 1.0} -->

Under the assumption of independence between body-frame query point uncertainty and each transform covariance, the variance of the query point in frame $\mathcal{S}_{0}$ is simply the sum $\Sigma^{\mathcal{S}_{0}} = {\Sigma_{\mathcal{B}}^{\mathcal{S}_{0}} + {R_{\mathcal{B}}^{\mathcal{S}_{0}}\Sigma^{\mathcal{B}}}}$. Extending this process to the $i$th sensor coordinate frame, we have and concatenating transforms for the mean we have which defines $\mathbf{x}_{query}^{\mathcal{S}_{i}} = {\mathcal{N}{(\mu^{\mathcal{S}_{i}},\Sigma^{\mathcal{S}_{i}})}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A2 IsInFOV: determining in-frame views", "weight": 1.0} -->

A key challenge is in determining which view contains the uncertain point, referred to as the IsInFOV function. Projecting the mean of the uncertain point into the depth image, as described in Figure 4: determining in-frame views ‣ IV-A Querying Algorithm ‣ IV FORMULATION ‣ NanoMap: Fast, Uncertainty-Aware Proximity Queries with Lazy Search over Local 3D Data"), can be used to efficiently check a series of inequalities (inside each of lateral and vertical FOV, occluded, not beyond sensor horizon) to determine if the point is in free space. A challenge, however is represented by Figure 5: determining in-frame views ‣ IV-A Querying Algorithm ‣ IV FORMULATION ‣ NanoMap: Fast, Uncertainty-Aware Proximity Queries with Lazy Search over Local 3D Data"). If only the mean of the distribution is used to check whether or not a view contains the point, then a large portion of that distribution may lie outside the FOV. With infinite-tail Gaussian distributions, no view fully contains them. NanoMap approximates this problem by using an axis-aligned bounding box (AABB), a familiar concept for fast approximations in the graphics community.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A2 IsInFOV: determining in-frame views", "weight": 1.0} -->

The AABB for the 1-$\sigma$ (1 standard deviation) of the distribution is used. Checking whether or not the AABB is contained can be done efficiently with the same number of inequality evaluations as the single point. To check for occlusions, NanoMap performs a simple occlusion check of the mean point.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B Data Structure for Asynchronous Data", "weight": 1.0} -->

The data structure (Figure 6) matches the form of the query algorithm and is performant given the requirements of asynchronous data and continuous addition and removal of data. The core data structure is a chain of edge-vertex pairs, where the edge is the transform $T_{\mathcal{S}_{i - 1}}^{\mathcal{S}_{i}}$ and the vertex contains both the raw point cloud data and the previously-processed $k$-d-tree. The raw point cloud data (row-column-organized) is used to evaluate the IsInFOV function, whereas the $k$-d-tree is used to evaluate $k$-nearest-neighbors if IsInFOV=true.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B Data Structure for Asynchronous Data", "weight": 1.0} -->

We briefly highlight some data structure design considerations. By nature NanoMap is never defined in one coordinate frame, and rather has components in many coordinate frames. One implication of this is that NanoMap must constantly be updating $T_{\mathcal{B}}^{\mathcal{S}_{0}}$ with each new pose. Further, we desired both fast insertion of a new edge-vertex pair, and fast removal of the oldest edge-vertex pair. Since search through the data structure is also always performed linearly, a doubly-linked list of edge-vertex pairs is a good fit for these requirements, efficiently supporting $O{}$ addition/removal at ends, and $O{}$ for each step of IsInFOV. An additional feature given the separate-frame nature of the framework and asynchronous data is that the $k$-d-tree of a point cloud can be built even before the pose of the point cloud can be determined, allowing the $k$-d-tree building to begin before a world-frame map would be capable of starting insertion.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B Data Structure for Asynchronous Data", "weight": 1.0} -->

Lastly, a key feature of NanoMap is to be able to efficiently handle asynchronous updated recent pose information, which may only cover a subset of its history. Upon receiving a series of updated world-frame poses, NanoMap only updates a transform edge $T_{\mathcal{S}_{i - 1}}^{\mathcal{S}_{i}}$ if it can fully interpolate the updated world frame pose of both vertices. This can be done efficiently by searching through the edge-vertex chain with a time-sequenced list of pose updates.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Data Structure for Asynchronous Data", "weight": 1.0} -->

6-DOF pose corrections sequence of timestamped poses organized (row,column) from depth camera Max sensor range Depth camera resolution, FOV 320x240, 60 deg V, 90 deg H FOV N, history length (# point clouds) between sensor poses TABLE I: NanoMap Data Inputs and Parameters

<!-- chunk {"id": "body-0025", "role": "body", "section": "RESULTS", "weight": 1.0} -->

We start by (A) analyzing in simulation how NanoMap is able to provide robust obstacle avoidance depsite significant state estimation uncertainty, and quantify the scale of drift and correction jumps (i.e., from a loop closure) at which this is significant. We then (B) analyze the computational efficiency of NanoMap compared to other available packages for evaluating local 3D data in motion planning. Finally, (C) we demonstrate NanoMap used effectively on a real hardware system.

<!-- chunk {"id": "body-0026", "role": "body", "section": "V-A Robustness of NanoMap to State Estimation Uncertainty", "weight": 1.0} -->

A central goal of NanoMap was to increase obstacle avoidance robustness in regimes of significant state estimation uncertainty. There are two separate features we evaluate: the ability to separately model pose uncertainty of each depth measurement, and the ability to efficiently correct recent pose information from a sliding-window state estimator. Our hypothesis was that at some threshold of pose uncertainty, these features become relevant. Here we present our findings.

<!-- chunk {"id": "body-0027", "role": "body", "section": "V-A1 Experimental: Motion Planner and Simulation", "weight": 1.0} -->

In these experiments, NanoMap is used by a stochastic motion planner. This motion planner was as described previously, with the following modifications: (a) a full 3D motion primitive library of 125 primitives, (b) a collision-chance-constrained (maximum allowed collision probability of $0.001$) rather than mixed-objective described previously, and (c) "early-exit" for subsequent sampling of a primitive that already evaluates below the chance constraint. Our simulation system was also as described, here used with a professional-grade urban environment created in the Unity game engine. The simulated depth camera was 30 Hz, 20 $m$ range, and 46 $deg$ $FOV_{vertical}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "V-A2 Scenario", "weight": 1.0} -->

The ability of NanoMap to provide pose-uncertainty-aware queries is most relevant when a motion planner is forced to search deeper into its history of poses. As discussed later with Figure 12, this is most apparent during extreme dodging maneuvers. Accordingly the experiments use the following scenario which is desirable due to its ease of interpretability: a quadrotor, initially at 5 $m$ altitude, is given a desired goal 200 $m$ away, with a desired top speed of $15$ $m/s$, and 100 $m$ along its path there is a large wall of a building with a 3D overhang near its altitude. The vehicle must aggressively decelerate, such that its velocity is outside of its current FOV. Significant pose uncertainty during this aggressive deceleration period would be difficult for other mapping and planning systems to handle.

<!-- chunk {"id": "body-0029", "role": "body", "section": "V-A3 Using Pose-Uncertainty-Aware Queries", "weight": 1.0} -->

To evaluate the magnitude of pose drift at which NanoMap's frame-specific uncertainty capability measurably increases robustness, we experimented with the following controlled experiment. As we increased state estimation noise, we either had NanoMap model the local, relative transforms with no translation covariance, $\Sigma_{\mathcal{S}_{i - 1}}^{\mathcal{S}_{i}} = \mathbf{0}$, or with a covariance corresponding to the noise level, $\Sigma_{\mathcal{S}_{i - 1}}^{\mathcal{S}_{i}} = f{(\Sigma_{actual}}$).

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-A3 Using Pose-Uncertainty-Aware Queries", "weight": 1.0} -->

Our noise model was to add noise to each of the $x$ and $y$ acceleration measurements, $\overset{\sim}{a} = {{({a + \eta})} \times \xi}$, where $\eta \sim {\mathcal{N}{(0,\Sigma_{actual})}}$ and $\xi \sim {\mathcal{N}{(1,\Sigma_{actual})}}$. Acceleration noise was integrated into the corrupted velocities and positions. Since quadrotors can measure altitude directly with downward-facing lidars and barometers, we did not model noise in $z$. An intuitive grasp of the scale of the noise model is best described as the standard deviation of drift over the depth measurement history (5 seconds = 150 measurements at 30 Hz) during the final portion of the flight. We term this $\sigma_{\text{drift, 5 seconds}}$, and accordingly used ${f{(\Sigma_{actual})}} = \frac{\Sigma_{\text{drift, 5 seconds}}}{150}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-A3 Using Pose-Uncertainty-Aware Queries", "weight": 1.0} -->

The singular difference between the two groups of the data (Figure 8) was the value of the $\Sigma_{\mathcal{S}_{i - 1}}^{\mathcal{S}_{i}}$ parameter in NanoMap.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-A3 Using Pose-Uncertainty-Aware Queries", "weight": 1.0} -->

These experiments show (Figure 8) that incorporating pose uncertainty can have a substantial effect, in particular when the drift is on the order of 10 $cm$ per second. At speeds above 10 $m/s$, this is approximately 1% position drift, which is comparable to expected performance from our VIO state estimator. At very small drift ($\sigma_{\text{drift, 5 seconds}} = {0.4m}$), there is little noticeable difference, but at $\sigma_{\text{drift, 5 seconds}} = {0.7,1.5,{3.8m}}$, incorporating the uncertainty enables the vehicle to still stay safe 97-98$\%$ of the time, whereas the drift deteriorates the safety of the group that doesn't incorporate pose uncertainty. The ability to stay safe diminishes at massive levels of drift (7.3 $m$ in 5 seconds), where the pose-uncertainty-modeled group only stays safe 90$\%$ of the time, but still more than the unmodeled group.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-A3 Using Pose-Uncertainty-Aware Queries", "weight": 1.0} -->

The pose-uncertainty-modeled group on average stays much farther away from obstacles, ($\gamma$ = distance to closest obstacle), playing it conservative during the aggressive maneuver.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-A4 Incorporating Updated Pose Information", "weight": 1.0} -->

NanoMap has a unique ability to efficiently update recent pose information, which as shown later in Figure 11, is not possible at realtime rates for the other benchmarked packages. This is meaningless, however, without getting a sense of when this capability is useful. Rather than provide a drifting state estimate, as in the previous experiment, we instead provide a deterministic backwards "pose correction" during the deceleration event (triggered at 12 $m/s$ during the deceleration). This is representative of a loop closure occurring in the global state estimator. NanoMap is configured to either use the pose corrections to update and maintain a smooth history of poses, or only add new poses as they come, and accordingly have a large "jump" in its history.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-A4 Incorporating Updated Pose Information", "weight": 1.0} -->

We find that even at the scale of 0.5 $m$ pose corrections, this size of a pose jump in its history can measurably cause crashes during the aggressive maneuver scenario, causing 18$\%$ crashes. With pose corrections of 2 $m$ or more, these jumps cause crashes more than 50$\%$. By using NanoMap's capability to trivially update its entire pose history upon receiving a sliding-window correction (orange), there is expectedly little effect for any level of pose jump tested, with crashes occurring less than 5$\%$ at all levels.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-B Computational Efficiency Benchmarking", "weight": 1.0} -->

We compare NanoMap to three other packages: OctoMap, Voxblox, and Ewok. OctoMap implements an octree occupancy grid, Voxblox builds ESDFs (euclidean signed distance functions) out of projective TSDFs, and Ewok builds its ESDF by iterating over a 3D circular buffer occupancy grid. Each of these can provide nearest-obstacle queries, which makes them efficient for stochastic motion planning, where there is uncertainty in configuration. There are of course many parameters for each of these packages, but we have made best efforts to provide a useful comparison given reasonable parameter choices. For both benchmarking experiments, we used a data log of a quadrotor with a simulated 320 $\times$ 240 depth image with 20 $m$ range traversing an approximately $200$ $m \times 200$ $m$ urban environment. This dataset, and the scripts for using each of these packages to generate the benchmarking data, are available^11^1 We use two metrics to measure the packages.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-B Computational Efficiency Benchmarking", "weight": 1.0} -->

The first metric (Figure 10) measures total time to incorporate a new sensor measurement and then perform $n_{queries}$ nearest-obstacle queries. The second metric (Figure 11) measures total time to adjust or rebuild a data structure after $n_{poses}$ poses are corrected, i.e. after a loop closure.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-B Computational Efficiency Benchmarking", "weight": 1.0} -->

There are a number of conclusions to draw from the plots. There is a tradeoff inherent from Figure 10 between the fusion-based packages (OctoMap, Voxblox, Ewok) which spend more time building their data structure, and NanoMap which spends less time building the data structure but has more expensive queries. For small amounts of queries, this tips the computational advantage to NanoMap, whereas for large amounts of queries, the fusion-based packages have an advantage. Figure 10 also demonstrates that unlike the discretized, fused packages, NanoMap has variable query time, based on how deep in history the query searches. We plot both the worst-case (each query searches the full history) and best-case (each query is in current FOV). In practice, our planner on average has approximately 75% best-case queries, but it is important to specify the system to worst-case timing, since as shown in Figure 12, more memory is used during critical dodging maneuvers. In the range of queries of our motion planner (2,500 queries), NanoMap is the fastest, even in the worst-case.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-B Computational Efficiency Benchmarking", "weight": 1.0} -->

From Figure 11, we see a unique capability of NanoMap -- its ability to incorporate updated pose information at realtime rates. NanoMap is two to four orders of magnitude faster than the others -- this is not a capability that is feasible at realtime rates for the other packages for more than a handful of $n_{poses}$. Whereas the only way to incorporate new pose information for the other packages is to rebuild the data structure with new world-frame-registered measurements, NanoMap can adjust by simply updating the relevant sequential transforms ($T_{\mathcal{S}_{i - 1}}^{\mathcal{S}_{i}}$) in its data structure.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-B Computational Efficiency Benchmarking", "weight": 1.0} -->

We also have been able to empirically validate that for obstacle avoidance motion planning in our flight regimes, a large percentage of NanoMap queries fall within the current or very recent FOV of the depth sensor. For a representative flight, we measure a very strong sufficiency of recent measurements, with 74.4% of queries falling within the current FOV, and a cumulative 92.3% of queries satisfied with the last 40 measurements. Figure 12 shows a histogram plotted over time during the course of the flight. During aggressive obstacle avoidance maneuvers (between $\sim$ 9 to 11 seconds into flight), there is expectedly more of a need to use memory. Yet even during this period, the last few seconds of flight mostly suffice for satisfying motion planning queries.\Figure 12: Histogram over time for depth of history is searched in a representative flight. This data is from a 13 second flight traveling approximately 50 m in low clutter with a 30 Hz depth sensor, 10 m range, and 45 d e g F O Vv e r t i c a l. Phases of flight are labeled above the time axis.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-C Hardware Experimentation", "weight": 1.0} -->

NanoMap has been extensively used in our hardware system on our MIT-Draper DARPA FLA^22^2DARPA Fast Lightweight Autonomy program: team. Figure 1, a, shows images from onboard video of a flight. Over the course of a week of experimental testing at the May 2017 FLA event, NanoMap was the local mapping representation used for the majority of flights, with both an Intel RealSense r200 (for outdoor environments) and an ASUS Xtion (for indoor environments) used as the depth camera sensor. A Hokuyo 2D lidar sensor also aided obstacle perception for many of these flights, but it was used in a memoryless fashion, and due to its 0-$deg$ vertical FOV was not useful during aggressive high-attitude maneuvers. We also (see video) demonstrate flight using only the RealSense, with no Hokuyo lidar. A sliding-window visual inertial (VIO) state estimator with 100 Hz low-latency poses and lower-rate, higher-latency pose corrections over a 5-second sliding window. NanoMap incorporated these sliding window pose corrections.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-C Hardware Experimentation", "weight": 1.0} -->

The mapping, planning, and hardware systems have been described in the author's Master's Thesis. Notable other vehicle hardware includes: a dual-core Intel NUC i7, a 450 mm Flamewheel DJI frame, and monocular Point Grey Flea3 camera and ADIS 16448 IMU for visual-inertial state estimation.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-C Hardware Experimentation", "weight": 1.0} -->

Our hardware experimentation with NanoMap demonstrates its robustness and applicability to high-speed obstacle avoidance. We have flown at up to 10 $m/s$ in forested canopy environments with the Intel r200 (empirically, we observe 20+ $m$ range in high-texture environments), and 8 $m/s$ in indoor warehouse environments with the ASUS Xtion (empirically, we observe $\sim$ 8-10 $m$ range). Flights in these types of settings can be seen in our video.

<!-- chunk {"id": "body-0044", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

We have described, implemented, analyzed, and validated NanoMap. NanoMap provides novel features for using local 3D data with pose uncertainty. Specifically, it (a) models relative positional uncertainty into its response to local 3D data queries, (b) uses the minimum-uncertainty view to respond to these queries, and (c) can trivially incorporate updated pose information two to four orders of magnitude faster than the benchmarked alternatives.

<!-- chunk {"id": "body-0045", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

We have shown that for state estimation drift on the order of tens of ${cm}/s$ (about 1% position drift at speeds above 10 $m/s$), or state estimate position corrections on the order of 1 $m$, using NanoMap's uncertainty-aware features can substantially increase robustness. Given these results, we believe NanoMap is a compelling, novel route forward when compared to the traditional, fusion-first paradigm of mapping for planning. We would encourage future work that may draw inspiration from NanoMap and supplement traditional mapping approaches. NanoMap is open source and available at github.com/peteflorence/nanomap_ros.
