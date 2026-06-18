<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps

Topics include Robotics, Safety, Robustness, Pose estimation, Real-time systems, Online algorithms, Planning, Splat-Nav.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present Splat-Nav, a real-time robot navigation pipeline for Gaussian Splatting (GSplat) scenes, a powerful new 3D scene representation. Splat-Nav consists of two components: 1) Splat-Plan, a safe planning module, and 2) Splat-Loc, a robust vision-based pose estimation module. Splat-Plan builds a safe-by-construction polytope corridor through the map based on mathematically rigorous collision constraints and then constructs a Bézier curve trajectory through this corridor. Splat-Loc provides real-time recursive state estimates given only an RGB feed from an on-board camera, leveraging the point-cloud representation inherent in GSplat scenes. Working together, these modules give robots the ability to recursively re-plan smooth and safe trajectories to goal locations. Goals can be specified with position coordinates, or with language commands by using a semantic GSplat. We demonstrate improved safety compared to point cloud-based methods in extensive simulation experiments. In a total of 126 hardware flights, we demonstrate equivalent safety and speed compared to motion capture and visual odometry, but without a manual frame alignment required by those methods.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We show online re-planning at more than 2 Hz and pose estimation at about 25 Hz, an order of magnitude faster than Neural Radiance Field (NeRF)-based navigation methods, thereby enabling real-time navigation. We provide experiment videos on our project page at Our codebase and ROS nodes can be found at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous robotic operation requires robots to localize themselves within an envrionment, plan safe paths to reach a desired goal location, and have closed-loop trajectory-tracking. Traditionally, the fundamental problems of planning and localization have been performed in maps represented as occupancy grids, triangular meshes, point clouds, and Signed Distance Fields (SDFs), all of which provide well-defined geometry.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, these explicit scene representations are generally constructed at limited resolutions (to enable real-time operation), leaving out potentially-important scene details that could be valuable in planning and localization problems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Neural Radiance Fields (NeRFs) have recently been used to implicitly represent $3$D scenes. NeRFs consist of a volumetric density field and a view-dependent color field parameterized by multilayer perceptrons (MLPs). NeRFs generate photo-realistic scene reconstructions, addressing the fundamental limitations of explicit representations; however, NeRFs require running inference on a deep neural network to render the scene, making them impractical for real-time use in robotic path planning. More recently, Gaussian Splatting (GSplat) has emerged as a viable scene representation compared to NeRFs, representing the environment with Gaussian (ellipsoidal) primitives. Compared to NeRFs, GSplats generate higher-fidelity maps at faster rendering rates, with shorter or comparable training times. More importantly for robotics, GSplats, unlike NeRFs, offer a geometrically consistent collision geometry, enabling us to use level sets of these Gaussians to generate an ellipsoidal representation of the scene. These interpretable geometric primitives facilitate the development of rigorous motion planning algorithms that are safe, robust, and real-time.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we introduce *Splat-Nav*, a pipeline for drone navigation in GSplat maps with a *monocular* camera. Splat-Nav comprises a lightweight pose estimation module, Splat-Loc, coupled with a planning module, Splat-Plan, to enable safe navigation from RGB-only (monocular) camera observations, as illustrated in Figure 1. Given an incoming RGB frame, Splat-Loc performs Perspective-n-Point (PnP)-based localization, leveraging the GSplat map to estimate the RGB and depth values rendered at candidate poses, which are then used to estimate the drone's pose. Next, Splat-Plan ingests the estimated pose computed by Splat-Loc to generate an initial trajectory, which is subsequently optimized to lie within safe flight corridors constructed from the ellipses that make up the GSplat map. The trajectory is parametrized by smooth, continuously safe Bézier splines that route the robot to a specified position or to a open-vocabulary language-conditioned goal location (i.e., "go to the microwave").

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

This feature enables the execution of Splat-Nav in a wide array of deployment conditions, such as in search missions where the precise location of targets is not known.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Additionally, the proposed system enables both open-loop trajectory generation and closed-loop re-planning. The latter is important in long trajectories, where existing onboard localization may drift or be subject to noise, impacting the overall safety of the executed trajectory of the robot. In these scenarios, Splat-Loc estimates can either be fused with that of the existing localization module or used as a correction mechanism to steer the current motion toward a safer one. Finally, closed-loop re-planning additionally enables changes in goal locations during execution, leading to more dynamic plans.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In extensive simulations we compare Splat-Plan and Splat-Loc with baseline alternatives for planning and localization, respectively. We show Splat-Plan is always safe with respect to the full collision geometry, while four variants of a point-cloud based planner sometimes lead to collisions, or fail to find trajectories. Splat plan achieves similar or better solutions in terms of path length compared to point cloud-based planner in all cases, with similar computation time. Splat-Plan runs at no less than 2 Hz; comparable to point cloud-based solutions for the same scenes, but faster than gradient-based NeRF planners and sampling-based planners (greater than 1 Hz) for similar solution quality. Similarly, we find that Splat-Loc is more accurate, faster, and fails less often compared to baselines. We demonstrate online pose estimation at about 25 Hz on a desktop computer, enabling real-time navigation.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, in an experimental campaign with 124 hardware flights, we show that Splat-Nav (Splat-Plan and Splat-Loc running together) perform as well as motion capture or on board VIO, without the manual frame alignment required for those methods to align the MoCap or VIO frame with the GSplat (since both Splat-Plan and Splat-Loc operate natively in the same GSplat map).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop a fast polytope corridor generation algorithm to enable provably safe planning for drone navigation in GSplat maps.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop a fast camera localization module based on GSplat maps that does not require manual alignment of the pose estimation frame to the planning frame, improving the synergy between planning and pose estimation.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate safe closed-loop re-planning with open-vocabulary goal specification, across a series of $124$ hardware experimental trials.

<!-- chunk {"id": "body-0015", "role": "body", "section": "3D Gaussian Splatting", "weight": 1.0} -->

Background. We present a brief introduction to $3$D Gaussian Splatting, a radiance field method for deriving volumetric scene representations from a set of monocular images. Gaussian Splatting represents non-empty space in a scene using $3$D Gaussian primitives, each of which is parameterized by a mean $\mu \in {\mathbb{R}}^{3}$ (defining its position), covariance matrix $\Sigma \in {\mathbb{S}}_{+ +}$ (related to its spatial extent and orientation), opacity $\alpha \in {\lbrack 0,1\rbrack}$, and spherical harmonics (SH) coefficients (defining view-dependent colors). The scene is typically initialized using a sparse point cloud computed via structure-from-motion.

<!-- chunk {"id": "body-0016", "role": "body", "section": "3D Gaussian Splatting", "weight": 1.0} -->

To render an image from a given camera pose, the $3D$ Gaussians are projected onto the image plane using an affine approximation of the projective transformation, given by $\Sigma_{2D} = {JW\Sigma W^{T}J^{T}}$, with Jacobian $J$ and viewing transformation $W$. The number of primitives, along with the coefficients for each primitive, is then learned via stochastic gradient descent with a loss function comprising of the photometric loss between the rendered and ground-truth images and the structural similarity (SSIM) index loss (the same as NeRF methods).

<!-- chunk {"id": "body-0017", "role": "body", "section": "3D Gaussian Splatting", "weight": 1.0} -->

For better numerical optimization, the anisotropic $3$D covariance of each Gaussian is written as: $\Sigma = {RSS^{T}R^{T}}$, where $R \in {{SO}{}}$ is a rotation matrix (parameterized by a quaternion) and $S$ is a diagonal scaling matrix (parameterized by a $3$D vector). This anisotropic covariance along with adaptive density control (i.e., splitting and merging Gaussians) enable the computation of compact high-quality representations, even in complex scenes, unlike many state-of-the-art point-based rendering methods. Further, $3$D Gaussian Splatting obviates the need for volumetric ray-marching required in NeRF methods, enabling high-quality real-time rendering, even from novel views.

<!-- chunk {"id": "body-0018", "role": "body", "section": "3D Gaussian Splatting", "weight": 1.0} -->

GSplats versus NeRFs. Gaussian Splatting typically requires less training time than state-of-the-art NeRF methods, while achieving about the same or better photometric quality. The biggest difference is in the rendering speed, where Gaussian Splatting achieves real-time performance. Moreover, $3$D Gaussian Splatting enables relatively fast extraction of a mesh representation (Remark 1) of the scene from the Gaussian primitives, and instantaneous extraction of the primitives themselves. In contrast, slower meshing techniques are needed for NeRFs, and the extraction of a point cloud requires slow volumetric rendering of many training viewpoints. In Fig. 2, we visualize the ground-truth mesh, the GSplat mesh, and the associated point cloud extracted from a NeRF of a simulated Stonehenge scene to showcase the collision geometry quality of GSplats over NeRFs. Quantitatively, the GSplat mesh has a smaller Chamfer distance (0.031 with 3M vertices) compared to the NeRF point cloud (0.081 with 4M points) despite having fewer points.

<!-- chunk {"id": "body-0019", "role": "body", "section": "3D Gaussian Splatting", "weight": 1.0} -->

We note that the NeRF does not necessarily yield a view-consistent geometry due to volumetric rendering, especially when the point cloud is not post-processed to remove outliers, leading to relatively poor collision geometry despite having good photometric quality.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The original work only projects $3D$ Gaussians whose $99\%$ confidence interval intersects the view frustum of a camera, effectively restricting the scene representation to the $99\%$ confidence ellipsoid associated with each Gaussian. Consequently, the union of the $99\%$ confidence ellipsoids represents the entirety of the geometry of the scene learned during the training procedure. We find that this cutoff is too conservative, due to the fact that the color of the Gaussians toward the tails of the distribution are close to transparent. Instead, we find that renderings of the $1\sigma$ collision geometry closely matches that of the GSplat depth channel, so we elect to use $1\sigma$-ellipsoid as the collision geometry for the remainder of this work. Future work will seek to explore the calibration of this cutoff.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Semantic Gaussian Splatting. To enable goal specifications for the navigation task in natural-language, we leverage semantic Gaussian Splatting, which distills $2$D language semantics from vision-language models, e.g., CLIP, into $3$D GSplat models. In general, these methods assign learnable semantic codes to each Gaussian, supervised by the robust semantic features extracted by $2$D foundation models. The semantic GSplats are trained in the same way as non-semantic GSplat via gradient descent. Semantic Gaussian Splatting has been utilized in prior work to enable open-vocabulary robotics tasks, e.g., robotic manipulation.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 1", "weight": 1.0} -->

In the subsequent sections, we present the core contributions of our work in deriving an efficient navigation pipeline for robots, describing how we leverage $3$D Gaussian Splatting as the underlying scene representation. Specifically, the quick extraction of simple convex primitives (whose union closely approximates the ground-truth scene geometry) promotes the development of guarantees on safety and solution quality of Splat-Plan and facilitates real-time deployment with low sim-to-real gap while navigating in Gaussian Splatting environments. Similarly, the fast and high-quality color and depth rendering from arbitrary viewpoints of the GSplat enables robust, fast camera localization in Splat-Loc.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Planning with Safe Polytopes", "weight": 1.0} -->

Now, we present Splat-Plan, our planner for GSplat maps. Splat-Plan generates safe polytopic corridors that represent the free space of a GSplat map between an initial configuration to a goal configuration. These corridors, and the resulting trajectories through them, are rigorously built on theory derived from tests for intersection between ellipsoids. The method is fast enough to provide real-time operation, provides safety guarantees extending to any scene with a pre-trained GSplat representation, and is not overly-conservative.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Planning with Safe Polytopes", "weight": 1.0} -->

We stress that, as with any safety guarantee on a map, our ultimate safety rests on the completeness of the map. If the map does not reflect the presence of an obstacle, our method may collide with the obstacle---we cannot avoid what we cannot see. In practice, we observe that GSplat maps provide fast and efficient representations of the underlying ground-truth geometry, as validated in our hardware experiments.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Planning with Safe Polytopes", "weight": 1.0} -->

We would also like to motivate the use of the full collision geometry of GSplats for planning compared to conventional representations like point clouds in an RGB setting. It is common to extract the means of the GSplat to form a point cloud. However, in feature-less regions, we observe that the point cloud can be quite sparse. Meanwhile, the full collision geometry spanned by the ellipsoids covers the full surface. This phenomenon can be observed in Fig. 1, where the render of the ellipsoidal representation of the collision geometry closely mimics the RGB render from the GSplat. However, the point cloud extracted from the means is very sparse. While usable for localization, such a sparse representation leaves a large sim-to-real gap when planning safe trajectories close to those areas. Another option is to sample the surface of these primitives for a point cloud, but even with this modification, point cloud-based planners are not as robust as Splat-Plan (Section VI).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Planning with Safe Polytopes", "weight": 1.0} -->

Before presenting the planning problem, we make the following assumptions on the representations of the robot $\mathcal{R}$ and the map $\mathcal{G}$ considered in this work. We assume that the robot is represented by a union of the ellipsoids in the non-empty set ${\{\mathcal{E}_{\mathcal{R},i}\}}_{i = 1}^{d}$, where $d$ denotes the cardinality of the set, i.e., $\mathcal{R} \subseteq {\cup_{i = 1}^{d}\mathcal{E}_{\mathcal{R},i}}$. For simplicity, we consider a singleton set $\mathcal{E}_{\mathcal{R}}$, noting that the subsequent discussion applies directly to the non-singleton case by running the collision check for all robot ellipsoids. One can also convert a mesh or point cloud of a robot to an ellipsoid by finding the minimal bounding ellipsoid (or sphere).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 2 (Online Gaussian Splatting)", "weight": 1.0} -->

Our planning algorithm requires a GSplat map. While this map can be trained online using real-time SLAM methods for radiance fields, which is a very new and active area of research, we limit the scope of this work to only plan in pre-trained maps.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 3 (Handling Uncertainty of the Scene Representation)", "weight": 1.0} -->

We can vary the value of $\gamma$ (from that used during the training procedure) based on the quality of the GSplat map and uncertainty in different regions of the GSplat map. In general, larger values of $\gamma$ inflate the volume of the confidence ellipsoids associated with each Gaussian, resulting in greater safety margins and more conservative planning. The converse holds if smaller values of $\gamma$ are selected. Moreover, for simplicity, we utilized a uniform value of $\gamma$. However, the value of $\gamma$ can vary among the ellipsoids, allowing the planner to account for varying levels of uncertainty in different regions of the GSplat map. Likewise, the volume of the ellipsoid representing the robot can be increased/decreased to account for uncertainty in the pose of the robot.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 4 (Dynamic Scenes)", "weight": 1.0} -->

We limit our discussion to planning in static scenes. However, we note that our method readily applies to planning in dynamic scenes, under the assumption that a dynamic Gaussian Splatting scene representation can be constructed. We discuss more about planning in dynamic scenes in Section VIII.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 4 (Dynamic Scenes)", "weight": 1.0} -->

Problem Statement. Given a bounding ellipsoid $\mathcal{E}_{\mathcal{R}}$ for the robot and a GSplat map $\mathcal{G}$, we seek to find a smooth, feasible path $x{(t)}$ for a robot to navigate from an initial configuration ${x{}} = x_{0}$ to a specified goal configuration ${x{(T)}} = x_{f}$, such that there are no collisions in the continuum, i.e., ${{{\mathcal{E}_{\mathcal{R}}{({x{(t)}})}} \cap \mathcal{E}_{j}} = \varnothing},{{\forall\mathcal{E}_{j}} \in \mathcal{G}}$, ${\forall t} \in {\lbrack 0,T\rbrack}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 4 (Dynamic Scenes)", "weight": 1.0} -->

Collision Detection. We leverage the ellipsoidal representations of the robot and the environment to derive an efficient collision-checking algorithm, based, where we take advantage of GPU parallelization for faster computation. We build upon rather than on other existing ellipsoid-to-ellipsoid intersection tests, because of its amenability to significant GPU parallelization. We do not utilize the GJK algorithm, since we do not require knowledge of the distance between the two ellipsoids. For completeness, we restate the collision-checking method from \[, Proposition 2\].

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-1 Seed Path", "weight": 1.0} -->

There are two primary flavors of graph-based paths that are popular in the literature: those that use random trees (e.g. RRT) and those on uniform grids. We will detail how both can be used as an initialization.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-1 Seed Path", "weight": 1.0} -->

Methods like RRT primarily rely on a module for collision detection at test points as well as a module to test for collision along a line. The use of Corollary 2 serves both functions. Unfortunately, the probabilistic completeness of these algorithms make them undesirable for real-time execution.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-1 Seed Path", "weight": 1.0} -->

The use of a uniform grid to run algorithms like Dijkstra Search are optimal and typically faster than those of random trees if there exists a cheap subroutine that converts the scene representation into a uniform grid. Specifically, we would like to avoid expensive collision checking between each disjoint sub-region of $3D$ space with the environment. Conversion from point clouds to binary voxel grids circumvents this issue by binning every point and assigning it an $(i,j,k)$ index.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-1 Seed Path", "weight": 1.0} -->

While there are many ways one could convert the ellipsoidal representation into a conservative occupancy grid, we propose the following method that is parallelizable and efficient, and show in Section VI that it is not too conservative. Without loss of generality, we assume that the robot is a sphere, which can be done by applying the necessary rotation and stretching for all ellipsoids such that the robot ellipsoid is a sphere. For every ellipsoid, we calculate its axis-aligned bounding box.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-1 Seed Path", "weight": 1.0} -->

The Minkowski sum of the ellipsoid with a sphere does not present an ellipsoid. However, at the extremal points which represent intersections of the bounding box with the ellipsoid, the normal of the ellipsoid is in the principal directions. The bounding box is defined as the following

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-1 Seed Path", "weight": 1.0} -->

where $\mu_{j}^{i}$ is the $i -$th element in the mean for ellipsoid $j$, and $\Sigma_{ii}$ represents the $i$-th diagonal term of the associated covariance.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-1 Seed Path", "weight": 1.0} -->

For those $\mathcal{B}_{j}$ whose side lengths are not within the resolution of each grid cell $v_{x,y,z}$, we subdivide them by their largest side length relative to $v_{x,y,z}$. We iterate on this process until all subdivisions of $\mathcal{B}_{j}$ are smaller than $v_{x,y,z}$. At this point, we can calculate all 8 vertices for every subdivision of $\mathcal{B}_{j}$ and bin them similar to the point cloud case. This procedure can leverage batch operations on GPU and ensures that we construct an over-approximation of the collision geometry.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-1 Seed Path", "weight": 1.0} -->

To account for the extent of the robot body, we convert the robot sphere into a kernel and perform a MaxPool3D operation. The resultant grid represents where the robot can be centered and be safe or unsafe. More sophisticated subdivision routines may be used to reduce the conservativism of the grid. Once the final grid is constructed, we run Dijkstra to find the seed path represented as an ordered set of connected line segments $\mathcal{L} = {\{\ell_{i}\}}_{i = 1}^{L}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-2 Collision Set", "weight": 1.0} -->

Along the seed path, rather than checking collisions between the robot and *every* ellipsoid in the scene, we would like to quickly find a subset of these primitives in the local vicinity of the robot to check against for efficiency reasons. In fact, Proposition 1 or Corollary 1 can directly be used to define a ball or ellipsoid collision set centered around the seed path, but may contain unnecessary information at the cost of additional compute.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-2 Collision Set", "weight": 1.0} -->

Instead, following the paradigm of, we can rapidly define a bounding box oriented along $\ell_{i}$ and pinpoint ellipsoids that live within it without incurring the additional cost of reasoning about the linear motion of the robot body. We define a radius $r_{s} = \frac{v_{\max}^{2}}{2a_{\max}}$, which is the maximum stopping distance (dependent on the maximum velocity and acceleration), such that the facets of the box are no less than $r_{s} + \kappa$ away from $\ell_{i}$. This bounding box will be denoted as ${A_{i}^{bb}x} \leq B_{i}^{bb}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-2 Collision Set", "weight": 1.0} -->

To check all ellipsoids that are at least partially contained within the box, we check for the minimum signed distance between each hyperplane ${\min_{x \in \mathcal{E}_{j}}{a_{i}^{bb}x}} \leq b_{i}^{bb}$ with every ellipsoid $\mathcal{E}_{j}$ in the scene. Ellipsoids that have negative signed distance for every hyperplane in the box will be at least partially contained. To perform this check, the plane and ellipsoid undergo an affine transformation to produce a new plane and an origin-centered sphere. The signed distance of the new plane from the origin must be less than 1, namely

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-3 Polytope Generation", "weight": 1.0} -->

The creation of polytopes around the line segment $\ell_{i}$ can be done through Corollary 5 and appending these constraints to the bounding box constraints ${a_{i}^{bb}x} \leq {b_{i}^{bb} - {\kappa{\| a_{i}^{bb}\|}_{2}}}$. Note that if we were to create a halfspace for every ellipsoid in the constraint set, we would overly constrain the free space, leading to a smaller-than-necessary polytope. This phenomenon arises from the fact that, given an existing set of halfspaces, ellipsoids that are outside of the set can still contribute non-redundant halfspaces to the existing set. Moreover, having more halfspaces than necessary in the polytope representation can significantly slow down the proceeding spline optimization.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-3 Polytope Generation", "weight": 1.0} -->

Therefore, we adopt a greedy algorithm like. Every time we form a new halfspace, we use Eq. 6 to eliminate from our collision set all ellipsoids that violate this halfspace. Of the remaining ellipsoids, we create a new halfspace for the one that had the smallest $K{(s^{\ast})}$. We iterate this process until no ellipsoids remain in the collision set.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-3 Polytope Generation", "weight": 1.0} -->

Due to manageability, we can further reduce the complexity of our corridor representation by retrieving a smaller number $P$ of polytopes than line segments $L$. For the current part of the seed path, we construct the minimal collision set and the polytope $(A_{p},b_{p})$. Then, we check subsequent line segments, represented as the endpoints, with the current polytope. The first instance where the line segment is not fully contained in $(A_{p},b_{p})$, we construct a new minimal collision set and polytope and repeat the process until the end of the seed path. Keeping more polytopes enables smoother paths (e.g. less opportunity for pinch points) at the expense of higher computation in the spline optimization phase.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-4 Spline Optimization", "weight": 1.0} -->

Given the safe flight corridor represented as $P$ polytopes and initial and final configurations $(x_{0},x_{f})$, we compute a set of $P$ Bézier curves (parametrized by $M + 1$ control points $c_{p}^{m}$ and Bernstein basis $\beta^{m}{(t)}$^22^2For notational simplicitiy, we refer to the variable as both the conventional basis and its time derivatives up to some specified order $D$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-4 Spline Optimization", "weight": 1.0} -->

Without the dynamics constraints (7f), the optimization problem reduces to a quadratic program that can be solved in real-time, producing a trajectory that can be tracked by differentially-flat robots. The quadratic program is solved natively using Clarabel.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-4 Spline Optimization", "weight": 1.0} -->

Due to the convex hull property of Bézier curves, constraining the control points to lie in the polytopes ensures that all points along the curves will lie in the corridor and hence guarantees safety in the continuum. Additionally, Splat-Plan is sound and complete, summarized in the following corollary.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Monocular Pose Estimation", "weight": 1.0} -->

In this section, we present our pose estimation module, Splat-Loc, for localizing a robot in a GSplat representation of its environment. This is essential to the overall functionality of the SplatNav pipeline as the safety guarantees of Splat-Plan only hold if the robot is able to consistently and accurately estimate its pose in the GSplat map. Splat-Loc only requires a monocular RGB camera, which enables it to work on a broad range of hardware platforms, including those beyond robots (such as mobile phones). Furthermore, Splat-Loc can be used either as a stand-alone pose estimation system or in conjunction with an independent pose estimation system (onboard VIO, external motion capture, etc).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Monocular Pose Estimation", "weight": 1.0} -->

Problem Formulation. Formally, we wish to estimate the pose of a robot at a particular time ${\hat{T}}_{t} \in {{SE}{}}$ given a color image $I_{t} \in {\mathbb{R}}^{H \times W \times 3}$. The true camera pose $T_{t}$ is unknown. A pose in $SE$$$ is parameterized by a rotation matrix $R \in {{SO}{}}$ and a translation vector $\tau \in {\mathbb{R}}^{3}$

<!-- chunk {"id": "body-0051", "role": "body", "section": "Monocular Pose Estimation", "weight": 1.0} -->

In the case that the navigating robot has an independent pose estimation system, we would like to use those pose estimates as initializations for Splat-Loc's optimization procedures, and also correct these poses using the estimates from Splat-Loc. We assume knowledge of the camera's calibration including the intrinsic matrix and distortion coefficients for projective geometry. These are easily computable, and are often available from the camera manufacturer.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Monocular Pose Estimation", "weight": 1.0} -->

Lightweight Monocular Pose Estimator. At its core, Splat-Loc uses the fast rendering capabilities of GSplats and standard tools from camera tracking to formulate Perspective-n-Point (PnP) problems, which can be reliably solved using off-the-shelf optimizers, and produces accurate estimates of the robot pose. As input for the pose estimation procedure, we have the color image and a coarse initial guess for the pose estimate, ${\hat{T}}_{t,0}$. This guess can either come from an independent localization module (e.g. VIO) or can simply be the previous time step's estimate. We begin by rendering an RGB image using the GSplat map with the camera pose set to the initial guess and simultaneously generate a local point-cloud within the camera's view, effectively using the GSplat as a monocular depth estimator.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Monocular Pose Estimation", "weight": 1.0} -->

Next, a local feature extractor is used to compute visual features (keypoints and descriptors) in both the camera image and the rendered image. Each keypoint has an associated pixel coordinate ${(u,v)} \in {\mathbb{R}}^{2}$, and let $m$ and $n$ respectively be the number of keypoints in the camera and rendered images. A feature matcher is used to determine correspondences between the visual features in the camera image and the rendered image. Let $\ell \leq {\min{\{ m,n\}}}$ be the number of successfully matched features. In our experiments we found that the feature extractor SuperPoint used in conjunction with the transformer-based LightGlue feature matcher had the best performance (see Section VI for more details).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Monocular Pose Estimation", "weight": 1.0} -->

Using the rendered depth image and the camera intrinsics matrix, the keypoints from the rendered color image can be projected into the 3D to produce a point cloud. Let ${\hat{p}}_{j} \in {\mathbb{R}}^{3}$ be the position of the $j$th projected keypoint where $j \in {1,\ldots,n}$. Finally, we seek to minimize the following reprojection error in order to find the relative pose transform that transforms ${\hat{T}}_{t,0}$ to ${\hat{T}}_{t}$

<!-- chunk {"id": "body-0055", "role": "body", "section": "Monocular Pose Estimation", "weight": 1.0} -->

where $\rho_{k} = {\lbrack u_{k},v_{k},1\rbrack}^{\top}$ and subsequently recover our estimated pose ${\hat{T}}_{t} = {{\overline{T}}_{t}{\hat{T}}_{t,0}}$. Eq. 9 is the Perspective-n-Point problem, and is a nonlinear least-squares optimization problem that we solve using the Levenberg-Marquardt algorithm. In practice, we use Random Sample Consensus (RANSAC) to remove outliers from the set of matched features which results in more robust solutions of Eq. 9. We illustrate this procedure in Figure 1. In Section VI, we highlight the accuracy of incremental estimation in real-world experiments while a drone navigates a cluttered environment.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Monocular Pose Estimation", "weight": 1.0} -->

Global Initialization. The above pose estimation procedure requires common overlap between $I_{t}$ and ${\hat{I}}_{t}$, necessitating a reasonably accurate initial estimate of the robot's pose ${\hat{T}}_{t,0}$, which may not be available in many practical settings. When a good initial guess of the robot's pose is unavailable, we execute a global pose estimation procedure. Note that this only needs to be performed once, and then subsequent pose estimate steps can be performed using the solution from the previous iteration.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Monocular Pose Estimation", "weight": 1.0} -->

One approach requires a monocular depth estimator, e.g. to augment the RGB image obtained by the robot with depth information, which is used to generate a point cloud (in the camera frame). Another is to randomly sample ${SE}{}$ for pose initializations and return the pose estimate from the P$n$P run that has the lowest reprojection error.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Monocular Pose Estimation", "weight": 1.0} -->

where $C$ denotes the set of correspondences, associating the point $p$ in the map cloud to a point $q$ in the point cloud from the camera. If we are given a known set of correspondences, we can compute the optimal solution of using Umeyama's method.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Monocular Pose Estimation", "weight": 1.0} -->

In practice, we do not have prior knowledge of the set of correspondences $\mathcal{C}$ between the two point clouds. To address this challenge, we apply standard techniques in feature-based global point-cloud registration. We begin by computing $33$-dimensional Fast Point Feature Histograms (FPFH) descriptors for each point in the point-cloud, encoding the local geometric properties of each point. Prior work has shown that visual attributes can play an important role in improving the convergence speed of point-cloud registration algorithms, something that FPFH does not do. To solve this, we augment the FPFH feature descriptor of a given point with its RGB color. We then identify putative sets of correspondences using a nearest-neighbor query based on the augmented FPFH descriptors, before running RANSAC to iteratively identify and remove outliers in $\mathcal{C}$. The RANSAC convergence criterion is based on the distance between the aligned point clouds and the length of a pair of edges defined by the set of correspondences.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Monocular Pose Estimation", "weight": 1.0} -->

Non-invasive Pose Correction. While fusing Splat-Loc poses with existing pose estimates like VIO is beyond the scope of this work, we will address challenges that arises when using Splat-Plan to plan high-level plans in a GSplat while using existing pose estimates to stabilize (i.e., for control). Fundamentally, discrepancies between the one in which the GSplat is trained in $\mathcal{T}_{\text{gs}}$ and the running coordinate frame of the existing localization module $\mathcal{T}_{(\text{control},t)}$ can vary with time, either due to noise or drift. Yet, poses from Splat-Loc are inherently tied to the GSplat coordinate frame, leading to potentially more informative state estimates of whether the robot is in collision or not. In turn, these estimates can be passed into Splat-Plan to create safer trajectories if necessary, as depicted in Fig. 1.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Monocular Pose Estimation", "weight": 1.0} -->

However, the trajectory that Splat-Plan returns again lives in $\mathcal{T}_{\text{gs}}$ and not necessarily the running coordinate frame of the existing localization, which is crucially used for control. To overcome this mismatch, we necessarily need to transform the outputs of Splat-Plan into the control localization frame. Namely, there exists a transform ${{}_{}^{\text{control},t}{}_{}^{}}:{\mathcal{T}_{\text{gs}}\rightarrow\mathcal{T}_{(\text{control},t)}}$ that maps poses in the GSplat frame to ones in the control localization frame. Therefore, the waypoints that we send to the robot are ${{}_{}^{(\text{control},t)}{}_{}^{}}{({X{(T)}})}$, which is depicted in Fig. 1 as the input to the robot.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Experiments", "weight": 1.0} -->

We demonstrate the effectiveness of our navigation pipeline for GSplat maps, examining its performance in real-world scenes on hardware and in simulation. In addition, we perform ablative studies comparing our algorithms against existing methods.

<!-- chunk {"id": "body-0063", "role": "body", "section": "VI-A1 Test Environments", "weight": 1.0} -->

We benchmark Splat-Plan and Splat-Loc independently on four different environments: Stonehenge, a fully-synthetic scene, and three real-world scenes Statues, Flightroom, and Old Union. For Stonehenge, we captured image-pose pairs by rendering the Stonehenge mesh in Blender. For the other scenes, we recorded a video from a mobile phone and processed the image frames through structure-from-motion to retrieve corresponding camera poses and intrinsics.

<!-- chunk {"id": "body-0064", "role": "body", "section": "VI-A2 Splat-Loc Evaluations", "weight": 1.0} -->

We compare Splat-Loc to existing pose estimation methods, including a baseline GS-Loc, based on the localization component of existing GSplat SLAM methods. We leverage finite differences to estimate the gradient of the photometric loss function utilized in the pose estimator, which might not be particularly fast or robust, especially for larger errors in the initial pose estimate. While these methods optimize over the re-rendering loss composed of the photometric loss, and in some cases, depth and semantic-related loss terms, in our baseline, we optimize only over the photometric loss, since we assume the robot in these evaluations does not have an RGB-D camera for depth measurements. As a result, our baseline essentially matches the GSplat SLAM method. In addition, we compare our pose estimator to the Point-to-plane Iterative Closest Point (ICP) and Colored-ICP algorithms, assuming these point-cloud methods have privileged $3$D information that the incremental estimation of Splat-Loc does not have.

<!-- chunk {"id": "body-0065", "role": "body", "section": "VI-A2 Splat-Loc Evaluations", "weight": 1.0} -->

Furthermore, we examine two variants of our pose estimator: Splat-Loc-Glue, which utilizes LightGlue for feature matching; and Splat-Loc-SIFT, which utilizes SIFT for feature matching.

<!-- chunk {"id": "body-0066", "role": "body", "section": "VI-A2 Splat-Loc Evaluations", "weight": 1.0} -->

In each scene, we run 10 trials (of $100$ frames each) of each pose estimation algorithm. We evaluate the rotation error (R.E.) and translation error (T.E.) with respect to the ground-truth pose, the computation time (C.T.) per frame, and the overall success rate (S.R.). Here, success indicates the generation of a solution regardless of its quality. The performance of pose estimation algorithms often depends on the error associated with the initial estimate of the pose. As such, we test our system across a range of different errors in the initial estimate of the pose. In this study, we assume an initial estimate of the pose is available. We generate the initial estimate by taking the ground truth pose then applying a rotation $\delta_{R}$ about a random axis and the translation $\delta_{t}$ in a random direction.

<!-- chunk {"id": "body-0067", "role": "body", "section": "VI-A2 Splat-Loc Evaluations", "weight": 1.0} -->

We provide the summary statistics of the error in the pose estimates computed by each algorithm, in addition to the computation time on a trial with $100$ frames in the Statues scene in Table I. We note that all methods had a perfect success rate in this problem. The GS-Loc algorithm achieves the lowest accuracy and requires the greatest computation time, unlike Colored-ICP, Splat-Loc-SIFT, and Splat-Loc-Glue, which achieve much-higher accuracy with a rotation error less than a degree and a translation error less than $15$cm. GS-Loc requires a computation time of about 36.15 s per frame, which is about two orders of magnitude slower than the next-slowest method ICP, which requires a computation time of about 110 ms. Colored-ICP, Splat-Loc-SIFT, and Splat-Loc-Glue require less than 100 ms of computation time. Compared to all methods, Splat-Loc-Glue yields pose estimates with the lowest mean rotation and translation error, less than $0.06^{\circ}$ and 4 mm, respectively, and achieves the fastest mean computation time, less than 42 ms.

<!-- chunk {"id": "body-0068", "role": "body", "section": "VI-A2 Splat-Loc Evaluations", "weight": 1.0} -->

The computation time of Splat-Loc may be about a standard deviation greater during the first call, which may be due to the time spent loading the models and initializing the GPU kernels.

<!-- chunk {"id": "body-0069", "role": "body", "section": "VI-A2 Splat-Loc Evaluations", "weight": 1.0} -->

Lastly, we examine the performance of the pose estimation algorithms in problems with a larger error in the initial estimate of the pose, with $\delta_{R} = 30^{\circ}$ and $\delta_{t} = {0.5m}$ in the synthetic Stonehenge scene. We present the performance of each algorithm on each metric in Table II, where we note that ICP and Colored-ICP do not provide accurate estimates of the robot's pose. Moreover, the pose estimation errors achieved by ICP and Colored-ICP have a significant variance. In contrast, Splat-Loc-SIFT and Splat-Loc-Glue yield pose estimates of high accuracy with average rotation and translation errors less than $0.5$ deg. and $5$mm, respectively. However, Splat-Loc-SIFT achieves a lower success rate, compared to Splat-Loc-Glue, which achieves a perfect success rate.

<!-- chunk {"id": "body-0070", "role": "body", "section": "VI-A3 Splat-Plan Evaluations", "weight": 1.0} -->

Splat-Plan is benchmarked against three different methods: a point-cloud planner, a sampling-based planner (RRT\* using Proposition 1), and a NeRF-based planner. Furthermore, we perform ablations against variations of the point-cloud planner in order to expose flaws when planning against point clouds compared to the full scene geometry. For each simulation scene, we train a dense and sparse GSplat, totaling 8 scenes. In every scene, we run 100 start and goal locations distributed in a circle around the boundary of the scene.

<!-- chunk {"id": "body-0071", "role": "body", "section": "VI-A3 Splat-Plan Evaluations", "weight": 1.0} -->

In the simulated tests, we represent the robot using balls of various sizes in order to generate interesting trajectories due to the fact that the simulated scenes are not trained in metric scale.^33^3Nerfstudio adopts the NeRF conventions in scaling the scene to fit within the confines of a two-unit-length cube centered at the origin, with the poses of the camera residing within a ${\lbrack{- 1},1\rbrack}^{3}$-bounding box. We disable this feature for the hardware Maze scene.. Additional parameters, such as the number of Gaussians, can be found in Table III.

<!-- chunk {"id": "body-0072", "role": "body", "section": "VI-A3 Splat-Plan Evaluations", "weight": 1.0} -->

While point cloud-based planners are ubiquitously used, they can sometimes fall short when the scene geometry is not dense or if the scene is very cluttered. To this end, we developed four variants of the Safe Flight Corridor (SFC). SFC-1 ingests the GSplat means as a point cloud, runs Dijkstra to retrieve a feasible initial path seed, creates collision sets with respect to the point cloud, synthesizes a polytope corridor that marginally intersects with the point cloud, and finally deflates the polytopes by the robot radius. These polytopes are fed to the same spline optimizer that Splat-Plan uses. SFC-2 executes the same pipeline as SFC-1, but the point cloud representation is sampled from the surface of the ellipsoids. We sample 20 points from each ellipsoid in the scene to simulate a typical amount of points a Lidar or depth image would produce (approximately 2-5 million points). SFC-3 uses the Splat-Plan occupancy grid to retrieve a feasible path seed, while the means are still used to create polytopes.

<!-- chunk {"id": "body-0073", "role": "body", "section": "VI-A3 Splat-Plan Evaluations", "weight": 1.0} -->

Finally, SFC-4 uses the Splat-Plan occupancy grid, synthesizes polytopes using the means, but deflates the polytope by the robot radius and the maximum eigenvalue of the ellipsoid whose mean was used to create a particular halfspace in the polytope. These variants are all potential solutions to apply SFC to GSplat environments. We summarize the tradeoffs of all methods in Table IV.

<!-- chunk {"id": "body-0074", "role": "body", "section": "VI-A3 Splat-Plan Evaluations", "weight": 1.0} -->

Visually, the paths generated by Splat-Plan are smooth, safe, and non-conservative. This fact is validated in Fig., where Splat-Plan's trajectories in blue are safe (minimum distances greater than 0 with respect to the GSplat collision geometry). Unfortunately, because many of these scenes were captured in the real-world, no ground-truth mesh exists. Moreover, we inspect the point cloud and mesh created by COLMAP and notice poor overall reconstruction of the collision geometry. Therefore, we elected to use the GSplat ellipsoidal geometry in place of the ground-truth geometry due to its high-quality approximation.

<!-- chunk {"id": "body-0075", "role": "body", "section": "VI-A3 Splat-Plan Evaluations", "weight": 1.0} -->

Notice that these trajectories are non-conservative compared to the SFC methods. More importantly, we see that Splat-Plan never fails to return a trajectory, highlighted by the 0 failure rate. All other methods have failures, other than NeRF-Nav by virtue of it being an end-to-end optimization method. Finally, Splat-Plan has comparable execution times to SFC. Note that as SFC does not use GPU, we rewrote the codebase in Pytorch to yield comparable times to Splat-Plan.

<!-- chunk {"id": "body-0076", "role": "body", "section": "VI-A3 Splat-Plan Evaluations", "weight": 1.0} -->

Finally, in terms of memory, we observe that in the scene with the most Gaussians (Old Union), GPU memory usage hovered around 3.1 GB, with the GSplat itself requiring 1.6 GB and the binary occupancy grid, 1.5GB.

<!-- chunk {"id": "body-0077", "role": "body", "section": "VI-B1 Test Environment", "weight": 1.0} -->

We test Splat-Nav in the Maze scene using a drone. Images to train Maze were captured using the RGB camera onboard the drone. We utilize Nerfstudio to train the Semantic GSplat, using its default parameters. In Figure, we show the true training images captured by the drone, the rendered RGB image from the GSplat at the same camera pose, and the semantic relevancy for the associated language query. First, we note that the rendered image is photorealistic, highlighting the remarkable visual quality of the trained Gaussian Splat. Second, the semantic relevancy spatially agrees with the expected location of the queried object, making the semantic field suitable for open-vocabulary goal querying.

<!-- chunk {"id": "body-0078", "role": "body", "section": "VI-B2 Hardware", "weight": 1.0} -->

We test our pipeline on the Modal AI development drone platform measuring $29$ cm x $20$ cm x $10$ cm (diagonal length of $36.6$ cm). In the hardware tests, we approximate the robot using a sphere with diameter $0.5m$. Readers can find our test parameters in Table III. An OptiTrack motion capture system is solely used for evaluation purposes. Any other markers, such as ArUco tags, in the scene are purely cosmetic.

<!-- chunk {"id": "body-0079", "role": "body", "section": "VI-B3 Implementation", "weight": 1.0} -->

We run the pose estimator and the planner ROS2 nodes on a desktop computer with an Nvidia RTX 4090 GPU and an Intel i9 13900K CPU, which communicates with the drone via WiFi. We emphasize that both modules are running asynchronously. At a frequency of about 3 Hz, the drone transmits images from its cameras and associated VIO poses to the desktop computer. Splat-Loc ingests the VIO pose ${\hat{T}}_{t,0}$ and the image $I_{t}$ to compute the pose estimate ${\hat{T}}_{t}$ of the drone body after applying rigid body transforms to transform the camera pose to the body frame. We run the estimator continuously, synchronized with the stream of images published from the drone via ROS2.

<!-- chunk {"id": "body-0080", "role": "body", "section": "VI-B3 Implementation", "weight": 1.0} -->

The planning module ingests ${\hat{T}}_{t}$ as $x_{0}$ and computes a safe trajectory for the drone to follow toward the language-conditioned goal $x_{f}$. The re-plan node, which runs Splat-Plan based on $x_{0}$, updates the spline(s) $X{(T)}$ as frequently as possible. The waypoint node, which operates asynchronously from the re-plan node, measures the running time since the $X{(T)}$ was last updated and returns positions, velocities, acceleration, and jerk at this running time. The waypoint node runs at 10 Hz. This architecture allows the drone to continue following a smooth spline even when Splat-Plan is still computing the next plan. However, we find that simply sending position waypoints can cause the drone to jerk when $X{(T)}$ is updated, as successive splines need not be close to one another. To rectify this issue, we forward integrate the waypoint velocities to get positions.

<!-- chunk {"id": "body-0081", "role": "body", "section": "VI-B3 Implementation", "weight": 1.0} -->

Finally, these positions undergo ${{}_{}^{(\text{control},t)}{}_{}^{}}{({X{(T)}})}$ before being sent to the drone. Additionally, we run a Kalman Filter to smooth ${}_{}^{(\text{control},t)}{}_{}^{}$, as both the Splat-Loc and VIO pose estimates can be somewhat noisy.

<!-- chunk {"id": "body-0082", "role": "body", "section": "VI-B4 Goal Specification", "weight": 1.0} -->

In the Maze, we specify the goal locations for the drone via natural language, comprising of the following objects: a keyboard, beachball, phonebook, and microwave. We query the semantic Gaussian Splat for the location of these objects using the following text prompts: "keyboard," "beachball," "phonebook" and "microwave," corresponding to these objects, without negative prompts. These objects are placed in locations that require dynamic motions, such as hard turns and elevation maneuvers, to reach. Moreover, all tests begin at the same position at hover, and the objects are positioned relative to this position so that they are not immediately visible when the drone first begins flight.

<!-- chunk {"id": "body-0083", "role": "body", "section": "VI-B5 Control Schemes", "weight": 1.0} -->

Our hardware tests consist of three different control schemes, coined Open-loop, Closed-loop VIO, and Splat-Loc. Open-loop tests do not not re-plan, and therefore does not use Splat-Loc estimates. One trajectory is created at the start $T = 0$, and the control node returns the corresponding waypoint at that point in time. No forward integration of the velocities is necessary since only one trajectory is ever created. Closed-loop VIO and Splat-Loc are re-planning control schemes where the re-plan node updates the trajectory $X{(T)}$ as frequently as possible. Closed-loop VIO uses the VIO estimate as $x_{0}$ and no additional transform is applied to the waypoint. Conversely, Splat-Loc uses the Splat-Loc pose estimate as $x_{0}$, and the smoothed ${}_{}^{(\text{control},t)}{}_{}^{}$ is applied to the Splat-Plan trajectories to transform them into the VIO control frame.

<!-- chunk {"id": "body-0084", "role": "body", "section": "VI-B5 Control Schemes", "weight": 1.0} -->

Our hardware tests consist of all combinations of goal locations and control schemes. In addition, we run these combinations 10 times for statistical significance, yielding a total of 120 flights.

<!-- chunk {"id": "body-0085", "role": "body", "section": "VI-B6 Splat-Loc Evaluations", "weight": 1.0} -->

We validate the performance of Splat-Loc in hardware experiments in the Maze scene, showing that Splat-Loc achieves relatively the same level of accuracy as the onboard VIO in estimating the drone's pose, without requiring any special calibration or re-initialization procedures for frame alignment, which the onboard VIO requires. In Table V, we provide the rotation and translation errors of the Splat-Loc estimates, with the MOCAP poses as the ground-truth estimates. We note that Splat-Loc achieves rotation errors of about 3 deg and translation errors of about 4 cm, which is comparable to the accuracy of the VIO estimates, shown in Table VI. However, Splat-Loc failed in one of the closed-loop trials with the "keyboard" goal location. As a result, the rotation and translation errors for this goal location is higher compared to the those of the other goal locations. The failure case is visualized in Figure 9, where the drone goes past the keyboard. We note that the failure likely occurred because the drone's camera was pointing towards an area of the scene which was not really covered in the video used in training the GSplat.

<!-- chunk {"id": "body-0086", "role": "body", "section": "VI-B6 Splat-Loc Evaluations", "weight": 1.0} -->

We discuss strategies for addressing such failure cases in Section VIII. In Figure 8, we show the estimated trajectories of the drone using MOCAP, the onboard VIO, and Splat-Loc, demonstrating the effectiveness of Splat-Loc. Essentially, all the pose estimators achieve comparable estimation accuracy. However, unlike the MOCAP system, Splat-Loc does not require a specialized hardware system and is amenable to any monocular camera. Moreover, Splat-Loc runs at about $25$ Hz on average, which is fast-enough for real-time operation. The bulk of the computation time is utilized in computing the feature matches and in solving the PnP problem, which requires about $10$ milliseconds.

<!-- chunk {"id": "body-0087", "role": "body", "section": "VI-B7 Splat-Plan Evaluations", "weight": 1.0} -->

Visualizations of 120 trajectories across four goal locations and three control schemes can be found in Fig. 9. Note that all flights were collision-free with respect to the true scene except for one flight using Splat-Loc to navigate to the keyboard. The drone was oriented toward the edge of the scene, where features were few and the GSplat quality was poor. The poor quality can be attributed to the lack of training images pointing toward the edges of the scene, as we wanted to reconstruct the foreground in the highest quality. These qualitative results indicate that, within the confines of our controlled setting, all control schemes work equally well. These results are promising for Splat-Loc from a convenience point of view. We noticed that the VIO of the drone would drift in subsequent runs, necessitating the reinitialization of the VIO at the start of every run. In addition, as the VIO is not calibrated to be in the GSplat frame, we manually aligned the frames by zero-ing the VIO of the drone at the same position for all flights and for collection of training data.

<!-- chunk {"id": "body-0088", "role": "body", "section": "VI-B7 Splat-Plan Evaluations", "weight": 1.0} -->

Meanwhile, Splat-Loc needed no such alignment, and was kept running continuously throughout all experiments without zero-ing (even in control schemes that do not use Splat-Loc).

<!-- chunk {"id": "body-0089", "role": "body", "section": "VI-B7 Splat-Plan Evaluations", "weight": 1.0} -->

Qualitatively, we see similar trends in Fig. 10. All control schemes are unsafe at different times, but in similar amounts. Note that some curves dip below 0, yet are verifiably safe in real-life. This is due to a variety of reasons, the most of prominent of which are: the difference in the set robot radius ($0.25$ cm) versus the true radius ($0.18$ cm), errors in aligning the motion capture frame into the frame of the GSplat (because the GSplat was not trained using motion capture), and the tracking capabilities of the drone. Note that the safety violation of all control schemes is relatively small compared to the size of the drone, which allows error in low-level tracking to obfuscate advantages of one method over another, especially in cluttered environments.

<!-- chunk {"id": "body-0090", "role": "body", "section": "VI-B8 Fast Control", "weight": 1.0} -->

We stress test Splat-Plan by increasing $v_{\max}$ until the onboard VIO could no longer track the desired waypoint with enough accuracy to avoid collision, which was ${1.5m}/s$. These speeds, coupled with the clutter in the environment, allowed for dynamic flight, which is visualized in the right column of Fig. 9. We point readers toward the associated videos hosted on our website to better visualize the trajectories.

<!-- chunk {"id": "body-0091", "role": "body", "section": "VI-B9 Closed-loop Endurance", "weight": 1.0} -->

Finally, we stress test the Splat-Loc re-planning pipeline through endurance flights. The pipeline is left to continually execute. Once the drone reaches a goal location, another goal location is set. We demonstrate collision-free flight over the order of minutes, which can again be visualized on our website.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduce an efficient navigation pipeline termed *Splat-Nav* for robots operating in GSplat environments. Splat-Nav consists of a guaranteed-safe planning module *Splat-Plan*, which allows for real-time planning ($>$ 2 Hz) by leveraging the ellipsoidal representation inherent in GSplats for efficient collision-checking and safe corridor generation, facilitating real-time online replanning. Splat-Plan demonstrates superior performance in terms of conservativeness, safety, success rate and comparable computation times compared to point-cloud and NeRF methods on the same scene. Moreover, our proposed pose estimation module *Splat-Loc* computes high-accuracy pose estimates faster (25 Hz) and more reliably compared to existing pose estimation algorithms for radiance fields, such as NeRFs. We present extensive hardware and simulation results, highlighting the effectiveness of Splat-Nav.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Limitations and Future Work", "weight": 1.5} -->

We only tested Splat-Nav in pre-constructed scenes. Existing GSplat SLAM algorithms do not run in real-time, limiting the application of our method in online mapping. In future work, we seek to examine the derivation of real-time GSplat mapping methods, integrated with the planning and pose estimation algorithms proposed in this work. Additionally, the results from Section VI-A2 suggest that we can incorporate Splat-Loc as a localization module within online GSplat SLAM algorithms to improve localization accuracy and the resulting map quality.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Limitations and Future Work", "weight": 1.5} -->

We assumed that the pre-constructed scenes were correct. Safety of the planned trajectories depends on the quality of the underlying GSplat map. As noted in Remark 3. ‣ IV Planning with Safe Polytopes ‣ Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps"), we can use different confidence levels of the ellipsoids to account for uncertainty in an object in the GSplat map. Splat-Plan cannot do anything if an obstacle is completely missing from the scene, which is a fundamental limitation of the GSplat map representation. Likewise, Splat-Plan could fail if the initialization graph-search procedure which utilizes Dijkstra fails to find a path to the goal, which could occur in maps with a coarse resolution. Future work will examine uncertainty quantification of different regions within a GSplat scene to aid the design of active-planning algorithms that enable a robot to collect additional observations in low-quality regions, such as areas with missing/non-existent geometry, while updating the GSplat scene representation via online mapping.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Limitations and Future Work", "weight": 1.5} -->

We only tested Splat-Nav in a static scene. This could be a limitation in many practical problems. Using NeRFs and GSplat for dynamic environments remains an open area of research, especially in scenes without prerecorded motion. Splat-Plan is fast enough to be extended easily to problems with dynamic scenes so long as the underlying dynamic GSplat representation is available.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Limitations and Future Work", "weight": 1.5} -->

The performance of Splat-Loc depends on the presence of informative features in the scene. We can address this in two ways: through planning and by incorporating additional sensor data. Future work will explore the design of planning algorithms that bias the path towards feature-rich regions, improving localization accuracy during path execution. Future work will also incorporate IMU data to improve the robustness of the pose estimator, particularly in featureless regions of the scene where the PnP-RANSAC procedure might fail.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Limitations and Future Work", "weight": 1.5} -->

Splat-Plan and Splat-Nav require loading the GSplat model onto the GPU, which takes up about 10 GB of GPU memory. Many drone platforms do not have the onboard compute resources to load the GSplat model, hindering onboard computation. Future work will seek to reduce the memory-usage demands of GSplat models, e.g., using sparse GSplat models.
