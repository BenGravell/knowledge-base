<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

AirSplan: Risk-Aware Motion Planning for Quadrotors in Cluttered 3D Gaussian Splats

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Quadrotors are increasingly deployed in applications such as agriculture, infrastructure inspection, and maintenance. In each of these applications, the robot must navigate complex scene geometry while remaining strictly collision-free. Unlike in ground domains, even minor collisions for aerial vehicles can result in the loss of the robot. This safety requirement induces a pair of technical challenges. First, the environment must be represented with sufficient fidelity to encode complex structure, even when no ground-truth obstacle data is available. Second, a motion planner must leverage this representation to determine a collision-free path to the goal. This paper proposes a system that addresses these complementary challenges. The proposed method, AirSplan, adopts a normalized variant of 3D Gaussian Splatting that encodes high-fidelity scene geometry. It then applies a novel reachability-based motion planner that leverages the differential flatness of quadrotors to compute continuous-time collision constraints that tightly overapproximate the robot's occupancy. Experiments demonstrate that AirSplan successfully finds a path in 81.2% of challenging test cases, a significant improvement over the nearest baseline method's 51.2%.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Quadrotors enable robotic operation in environments inaccessible to ground-restricted platforms, enabling applications such as crop monitoring, infrastructure inspection, and navigation in confined or elevated spaces. However, ensuring safe operation in cluttered environments remains a significant challenge. Unlike ground robots, even minor collisions can result in catastrophic failure for aerial vehicles. Achieving safety and reliable operation therefore requires accurately modeling the robot's occupied volume, representing complex scene geometry, and planning motions that guarantee separation between the two.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Existing collision avoidance methods for aerial vehicles typically approximate the robot as spherical or convex. This conservative approximation simplifies computation, but impedes the ability of the robot to operate in cluttered environments. Another category of planners enforce collision avoidance only at discrete time points using sampling-based planners, inducing a trade-off between safety and computational cost. This work addresses these limitations by exploiting quadrotors' differential flatness to construct a continuous-time safety representation that tightly overapproximates a robot's swept volume.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Accurate scene representation presents an additional challenge. Many planning methods assume access to ground-truth scene geometry, which is unavailable in many real-world deployments. To solve this problem, robotics researchers have increasingly turned their attention to radiance field models such as NeRFs and 3D Gaussian Splats due to their ability to accurately reconstruct complex scene geometry directly from camera data. However, existing radiance field planners for quadrotors rely on spherical robot approximations. As illustrated in this paper, this spherical overapproximation limits quadrotors' ability to navigate highly cluttered scenes. This work addresses these challenges by introducing an optimized continuous-time collision-checking method for quadrotors and scenes represented as normalized 3D Gaussian Splats.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, the contributions of this work are as follows: A differential flatness-based reachability formulation that constructs a continuous-time forward reachable set for quadrotors, accounting for the full geometry of the robot.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

An optimized collision checking method between the forward reachable set and scenes represented as Normalized 3D Gaussian Splats.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The two contributions above are implemented in AirSplan, a receding-horizon trajectory optimization framework that integrates them to synthesize safe motions in complex environments. Experiments demonstrate state-of-the-art collision avoidance performance for quadrotors across diverse cluttered environments.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fig. 1: AirSplan generates safe quadrotor trajectories in cluttered environments. The robot occupancy is tightly overapproximated using a reachable set (shown in pink) based on differential flatness. The scene is modeled as a Normalized 3D Gaussian Splat. A sampling-based planner jointly reasons over both representations to compute safe paths between waypoints (yellow) to the goal (red).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fig. 2: AirSplan plans safe quadrotor trajectories through cluttered environments represented as normalized Gaussian Splats. It combines three key components. First, differential flatness is used to construct a tight sphere-based overapproximation of the robot volume along a trajectory. Second, the collision probability between each sphere and the normalized 3D Gaussian Splat is efficiently computed using a Bounding Volume Hierarchy (visualized with gray wireframe boxes). Third, a GPU-parallel sampling-based optimizer evaluates many candidate trajectories to efficiently find safe paths through dense environments.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Related Works", "weight": 1.0} -->

This paper describes a method that combines collision avoidance for quadrotors, planning in radiance field representations, and reachability-based motion planning. The relevant literatures are summarized below.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Quadrotor Collision Avoidance", "weight": 1.0} -->

Quadrotors and other aerial vehicles must remain strictly collision-free during operation; yet generating safe plans through cluttered environments remains challenging. A prominent category of works constructs a global map of geometric primitives and optimizes collision-free plans within it. These methods require explicit representations of scene occupancy, such as voxel grids or octrees, zonotopes, or polytopes. Polytopes and zonotopes admit efficient constraint formulations but are difficult to construct from sensor data. Voxel grids and octrees avoid this difficulty but carry high memory overhead in dense, cluttered scenes. A second category operates reactively to local obstacles without maintaining a global map. While effective with local sensing data, reactive planning makes safety guarantees difficult to establish. This paper addresses both limitations by performing risk-aware planning directly in high-fidelity radiance fields, which can be reconstructed from sensor data while supporting rigorous safety guarantees.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Quadrotor Collision Avoidance", "weight": 1.0} -->

A recurring pattern in existing methods is overapproximating the robot with a simple primitive such as a sphere, superellipsoid, or zonotope. While computationally efficient, this simplification limits safe planning for vehicles with complex geometry in tight spaces. A common workaround is to employ sampling: either checking for collisions at poses sampled along the path, or sampling points on the robot's surface. Sampling, however, makes collision-avoidance guarantees difficult to establish. In contrast, this paper leverages the differential flatness of quadrotors to compute forward reachable sets, yielding tight, continuous-time overapproximations of the robot's swept volume.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Planning in Radiance Fields", "weight": 1.0} -->

While many safe motion planners assume ground-truth knowledge of obstacle locations, such information is often not available. Several works have proposed planning methods that operate directly on NeRF reconstructions. NeRF-Nav plans dynamically-feasible trajectories for quadrotors by sampling a finite set of points from the robot body, and applying a penalty to the density integrated along those points' paths. While NeRF-Nav demonstrates the promise of radiance field planning, this approach relies on a discrete approximation of robot geometry and does not provide probabilistic safety guarantees. CATNIPS overcomes these limitations by relating NeRFs to a Poisson Point Process, and using this relation to convert the NeRF into an occupancy grid.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Planning in Radiance Fields", "weight": 1.0} -->

While NeRFs use neural networks to approximate radiance fields, 3D Gaussian Splatting represents the same information using a set of unnormalized 3D Gaussians. Splat-Nav plans in 3D Gaussian Splats by building safe flight corridors that avoid the $1\sigma$ level sets of these Gaussians. Other planning methods avoid collisions with the splats by sampling trajectory points or applying a soft collision penalty. These offer useful heuristics but assume a spherical robot and provide no continuous-time collision-avoidance guarantees. Further, it remains unclear how to extend existing methods to robots that are not tightly approximated as spheres.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Planning in Radiance Fields", "weight": 1.0} -->

In contrast to these approaches, Splanning uses a normalized formulation of 3D Gaussian Splatting and applies reachability analysis to overapproximate the continuous-time swept volume of a robot manipulator. It then solves a trajectory optimization that bounds the probability of intersection between the robot and the scene. Still, Splanning relies on a manipulator fixed to a workspace. To address these limitations, this paper develops improved reachability, collision-checking, and trajectory optimization methods that enable quadrotors to navigate highly cluttered environments.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-C Reachability-Based Motion Planning", "weight": 1.0} -->

Reachability-based Trajectory Design (RTD) generates safe, receding-horizon trajectories by constructing a continuous-time representation of the robot's swept volume along candidate trajectories. This swept volume, called a Forward Reachable Set (FRS), is checked for collisions with obstacles to provably guarantee safety. RTD has been applied to ground vehicles, quadrotors, and manipulators. It has also been extended to risk-aware planning with uncertain obstacles, and to planning in radiance fields represented by 3D Gaussian Splatting. Finally, Kwon et al. replace explicit FRS construction with a neural network approximation and use conformal prediction to guarantee conservativeness. This work extends the literature on reachability-based motion planning by leveraging quadrotor differential flatness to construct a tight safety representation for aerial vehicles, which can be efficiently integrated over a Normalized Gaussian Splat to compute the probability of collision.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Differential Flatness of Quadrotors", "weight": 1.0} -->

Although quadrotors are underactuated in their full $SE$ state, they are differentially flat: the state and control inputs are algebraic functions of four flat outputs and their derivatives, namely the position $\mathbf{p}(t)\in\mathbb{R}^{3}$ and yaw $\psi(t)\in SO$. Any sufficiently smooth curve in $\mathbb{R}^{3}\times SO$ with bounded derivatives therefore corresponds to a dynamically feasible trajectory, reducing trajectory planning to constructing smooth functions $\mathbf{p}$ and $\psi$. The attitude is recovered as follows. Let $\mathbf{g}=[0,0,g]^{\top}$ be the gravity vector in the world frame. The body-frame $z$-axis aligns with the total thrust direction: Given $\psi$, the remaining body axes are where $C$ denotes a frame coincident with the center-of-mass frame $B$ but with zero roll and pitch.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Differential Flatness of Quadrotors", "weight": 1.0} -->

These relations uniquely determine the body rotation $R^{B}=[\mathbf{x}^{B}\;\;\mathbf{y}^{B}\;\;\mathbf{z}^{B}]$: roll and pitch follow entirely from $\ddot{\mathbf{p}}$ and $\psi$. Planning can thus occur in $\mathbb{R}^{3}\times SO$, where the quadrotor is fully actuated, while uniquely recovering the full $SE$ trajectory.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Polynomial Zonotopes for Reachability Analysis", "weight": 1.0} -->

Reachability analysis computes an overapproximation of the states a system may attain over a time interval. In configuration space, this yields a joint reachable set (JRS), which forward kinematics propagates into the FRS, a conservative overapproximation of the robot's swept volume. Assuming precise trajectory tracking, this yields a guaranteed bound on swept occupancy for collision checking.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Polynomial Zonotopes for Reachability Analysis", "weight": 1.0} -->

Polynomial zonotopes (PZs) are a set representation that captures nonlinear dependence between variables. They support exact propagation through addition and multiplication, corresponding to Minkowski sums and set products. General nonlinear functions acting on a polynomial zonotope can be efficiently overapproximated, producing a new polynomial zonotope that contains the true image. In particular, for an analytical function $f:\mathbb{R}^{N}\to\mathbb{R}^{M}$, it is possible to evaluate $f$ on a PZ $\mathbf{S}\subset\mathbb{R}^{N}$ to obtain a PZ $\mathbf{Q}\subset\mathbb{R}^{M}$ such that $\{f(\mathbf{x})\mid\mathbf{x}\in\mathbf{S}\}\subseteq\mathbf{Q}$, where we write $f(\mathbf{S})=\mathbf{Q}$ by an abuse of notation.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Polynomial Zonotopes for Reachability Analysis", "weight": 1.0} -->

For brevity, the mathematical formulation of PZs is omitted; we refer readers instead to for a comprehensive treatment.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-C Scene Representation", "weight": 1.0} -->

Following, AirSplan represents scenes using a normalized 3D Gaussian Splat, a form of radiance field representation that allows probabilistic interpretation of rigid body collisions. The properties of this representation are summarized below.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-C1 Normalized 3D Gaussian Splatting", "weight": 1.0} -->

A radiance field is a function $\mathcal{L}:(\mathbf{x},\mathbf{d})\mapsto(r,g,b,\sigma)$ mapping position $\mathbf{x}\in\mathbb{R}^{3}$ and direction $\mathbf{d}\in\mathbb{S}^{2}$ to color and density $\sigma\in\mathbb{R}^{+}$. Radiance fields can be learned from images via differentiable rendering. For collision avoidance, color is irrelevant; only $\sigma$ is needed. Because it is independent of $\mathbf{d}$, we write $\sigma(\mathbf{x})$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Method", "weight": 1.0} -->

This section introduces AirSplan, a method for risk-aware trajectory generation in scenes reconstructed from camera data.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-A System Overview", "weight": 1.0} -->

AirSplan synthesizes motion plans by solving the following optimization problem in a receding-horizon manner: | | | $\displaystyle\underset{k\in K}{\min}$ | | $\displaystyle\texttt{cost}(k)$ | | \(7\) | | | | $\displaystyle\mathrm{P}\left(\text{FRS}(q(t;k,x_{0}))\cap\mathscr{E}\neq\emptyset\right)\leq\beta$ | $\displaystyle\forall t\in T$ | | \(8\) | A trajectory parameter $k$ is chosen from a parameter space $K$, the cost in encourages the robot to reach a specified goal configuration, and encodes a risk-aware obstacle avoidance constraint, enforcing that the probability of the robot's FRS intersecting the environment $\mathscr{E}$ may not exceed a risk threshold $\beta$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-A System Overview", "weight": 1.0} -->

Here $x_{0}$ denotes the robot's initial state (e.g., position, velocity, and acceleration), which is fixed at planning time and not optimized over. Section IV-B describes the trajectory parameterization and construction of an FRS for an aerial vehicle, while Section IV-C describes an optimized form of the collision check in Theorem 1, and Section IV-D describes a GPU-parallelized trajectory optimization.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-B Trajectory Parameterization and Reachability Analysis", "weight": 1.0} -->

We compute an FRS for the quadrotor as a union of spheres in three steps: constructing reachable sets of the flat outputs, propagating them to the full system state using differential flatness, and approximating the resulting FRS with a neural network for efficient online evaluation.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B1 Trajectory Parameterization and JRS Construction", "weight": 1.0} -->

Each flat output is parameterized as a degree-5 Bernstein polynomial in time, whose coefficients depend on both the initial state $x_{0}$ and trajectory parameter $k_{d}$: where $b_{l}$ are the Bernstein Basis Functions \[30, Example 15\].

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B1 Trajectory Parameterization and JRS Construction", "weight": 1.0} -->

To ensure safe receding-horizon planning, the planning horizon $T$ is divided into two intervals: the first corresponds to the planned motion, and the second to a braking maneuver that brings the system to zero velocity and acceleration. During execution of the first interval, the system plans the next horizon; if successful, the braking maneuver is discarded and planning continues in a receding-horizon manner. For convenience, we set $T=1$ second and divide it equally between the two intervals.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B1 Trajectory Parameterization and JRS Construction", "weight": 1.0} -->

Because the robot executes the previously planned trajectory while replanning, $x_{0}$ is known at planning time. Furthermore, since every trajectory must end in a braking maneuver, the terminal velocity and acceleration are fully determined. Together, these boundary conditions fix five of the six Bernstein coefficients. We parameterize the remaining coefficient, which we choose without loss of generality to be the last coefficient, as where $\eta_{d,1},\eta_{d,2}\in\mathbb{R}$ are user-specified constants. As a result, $q_{d}(t;\,x_{0},k_{d})$ is polynomial in $k_{d}$ and $t$. By representing $[0,T]$ as a PZ and evaluating, we obtain a PZ $\mathbf{Q}_{d}$ that bounds all reachable configurations of DOF $d$ over the planning horizon as a function of $k_{d}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B1 Trajectory Parameterization and JRS Construction", "weight": 1.0} -->

We refer to $\mathbf{Q}_{d}$ as the $JRS$ of the $d^{th}$ DOF of the system. In practice, the JRS of the quadrotor system is built by assembling four of the individual $\mathbf{Q}_{d}$ objects. Each position dimension is represented by a single JRS axis. Yaw is represented using separate JRSs for $\sin(\psi)$ and $\cos(\psi)$ to reduce nonlinear overapproximation error, as is common in reachability-based methods. We refer to the 5-DOF JRS of the quadrotor's position and yaw as $\mathbf{Q}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-B2 Computing the SE FRS", "weight": 1.0} -->

While $\mathbf{Q}$ bounds the set of states that the robot's position and yaw will occupy during a trajectory, there remains ambiguity in the roll and pitch angles. While prior works commonly avoid this ambiguity by overapproximating the robot with a sphere or zonotope, we instead propagate the JRS through differential flatness relations --, yielding a reachable rigid-body transform PZ $\mathbf{T}^{WB}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B2 Computing the SE FRS", "weight": 1.0} -->

To obtain an FRS that bounds the quadrotor conservatively, we pack the robot body with body-fixed spheres with centers $\{\mathbf{c}_{m}\}$ and radii $\{r_{m}\}$ generated using the method of. Each center is propagated through the set of reachable rigid body transformations: This produces a reachable set for each sphere center. Each set $\mathbf{C}_{m}$ is then overapproximated by a bounding sphere with center $\mathbf{c}_{m}$ and radius $\delta_{m}$. The corresponding robot volume is obtained by inflating this radius by the body-fixed sphere radius, yielding a final radius Finally, the robot FRS over the time interval is given by the union of the spheres $B(\mathbf{c}_{m},R_{m})$ over all $m$. In practice, the planning horizon is split into several sub-intervals, and the spheres from all sub-intervals are accumulated to form the full FRS. The resulting spheres bound the swept volume of the aerial base.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B2 Computing the SE FRS", "weight": 1.0} -->

The overapproximativeness of this bound follows closely from \[24, Theorem 10\], where we apply the differential flatness relations instead of the forward kinematics of arms.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B3 Neural Network Approximation", "weight": 1.0} -->

The computation above yields an overapproximation of the robot's occupancy. In practice, however, PZs come with a trade-off between the tightness of the overapproximation and computational complexity. The compute requirements of highly-accurate PZs limit applicability to the sampling-based planner we describe in Section IV-D. To reduce online computation, we adopt the method of and train a neural network to approximate the spherical FRS. With these values, the corresponding spherical FRS is computed using the exact reachability pipeline. The network predicts sphere centers and radii as functions of these inputs, and conformal prediction is applied to conservatively inflate the outputs and preserve safety guarantees.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-C Parallel Collision Detection", "weight": 1.0} -->

In practice, each FRS contains hundreds to thousands of spheres per planning horizon. The sampling-based planner described in Section IV-D may consider up to 100 candidate trajectories, requiring collision checking on up to hundreds of thousands of spheres per iteration. Further, the environment representation may contain millions of Gaussians. Naively evaluating the collision constraint in across all sphere-Gaussian pairs is therefore computationally prohibitive. To overcome this problem, Splanning ignores Gaussians outside the reachable workspace of the fixed manipulator. Yet, this solution does not handle a mobile vehicle and conservatively assumes that all spheres interact with the same set of Gaussians. Instead, we use a Bounding Volume Hierarchy (BVH) to accelerate collision queries by restricting evaluation to nearby Gaussians.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-C1 BVH construction", "weight": 1.0} -->

For each Gaussian, an axis-aligned bounding box (AABB) is computed corresponding to the Gaussian's $n_{\sigma}$ confidence region. A linear BVH is then constructed over these AABBs using an open-source implementation^11^ 1 of the method. This pre-processing happens once per scene.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-C2 Query procedure", "weight": 1.0} -->

Each sphere is processed by a GPU thread. During a query, the sphere's AABB is computed, then the BVH traversed to identify overlapping Gaussians. Each thread stores candidate Gaussians in a per-thread buffer of size $n_{B}$, capping the number of Gaussians considered for that sphere. Let $n_{K,i}\leq n_{B}$ denote the number of Gaussians retrieved for sphere $i$. The collision risk is computed by evaluating the closed-form integral from Theorem 1 over this candidate set. If the buffer capacity is exceeded during traversal (i.e., more than $n_{B}$ Gaussians overlap the sphere), the trajectory candidate is immediately flagged as unsafe.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-C3 Parallelization and Complexity", "weight": 1.0} -->

The BVH reduces the number of Gaussian evaluations per sphere from $n_{G}$ to $n_{K,i}\ll n_{G}$, yielding $\mathcal{O}(\log n_{G}+n_{K,i})$ time complexity and $\mathcal{O}(n_{B})$ memory complexity for each sphere query.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-C3 Parallelization and Complexity", "weight": 1.0} -->

1: Mean μ0, covariance Σ, temperature λ, samples nS, iterations nI, max time Tmax, collision weight wcol, tolerance β 2: Trajectory parameter k*, or ⌀ if none is safe 5: if elapsed time > Tmax then break 9: costj ← cost(kj) + wcol ccol(kj) 15: wj ← exp (−costj/λ)/∑ℓexp (−costℓ/λ) Algorithm 1 Sampling-Based Trajectory Optimization

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-D Trajectory Optimization", "weight": 1.0} -->

Most reachability-based motion planners leverage interior point methods to optimize trajectories subject to collision avoidance constraints. In practice, this style of optimization fails to converge on the differentially flat quadrotor system. We suspect this is because there are spurious local minima in the optimization problem. Hence, we instead use a sampling-based trajectory optimizer based on a soft cross-entropy method. As described in Algorithm 1, trajectories are iteratively refined using importance-weighted averaging of Gaussian samples. The user-specified cost is augmented with a collision penalty computed as described in Section IV-C. Trajectories are rejected if the final collision probability exceeds the risk threshold.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experiments", "weight": 1.0} -->

Two experiments were run to evaluate the proposed methodology. First, the optimized collision checker was evaluated for speed and accuracy. Second, the proposed planner was evaluated end-to-end against relevant baselines. All experiments were run on a machine with an AMD 5950x CPU and NVIDIA RTX Pro 6000 GPU.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-A Collision Constraint", "weight": 1.0} -->

The collision constraint was evaluated according to the procedure described. The collision comparison operates on the randomized scenes with cube obstacles. Individual spheres were randomly sampled that were either in collision, near collision, or collision-free with an equal distribution of each. Each method then evaluates whether each sphere is in collision with the environment.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-A1 Collision Baselines", "weight": 1.0} -->

Three baseline methods were evaluated. First, the collision constraint from CATNIPS between a sphere and a NeRF was run using the reference implementation and the default settings. Second, collision comparisons between a standard, un-normalized 3DGS and a sphere was evaluated using the constraint in Splat-Nav. For Splat-Nav, the constraint was evaluated by checking for collisions between the sphere and multiple $n\sigma$ ellipsoids of the un-normalized Gaussians using the reference implementation. Next, the Splanning constraint between spheres and a normalized 3D Gaussian Splat was evaluated at multiple risk thresholds $\beta$ (See Thm 1 for a definition of $\beta$). Finally, the optimized Splanning constraint proposed in this method was evaluated. Note that while the constraint in and that proposed in this paper are theoretically identical, differences in the logic for ignoring far-away Gaussians and numerical implementation may cause slight discrepancies.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-A2 Metrics", "weight": 1.0} -->

Each collision checker was treated as a classifier of free space vs collision, and both precision and recall were evaluated at a range of parameters. Furthermore, for the Splanning constraint and our method, the time required to evaluate the constraint was measured. For Splat-Nav and CATNIPS, the compute time was not measured because the methodology required to isolate the collision constraint from the rest of the planner significantly affected their runtime performance.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-B Motion Planning", "weight": 1.0} -->

To create realistic, challenging obstacle-avoidance environments, we procedurally generate three-dimensional trees using L-systems, representing each segment as a ten-sided zonotope. Scenes are rendered in PyRender with cameras arranged spherically around each tree, emulating images captured by an aerial vehicle at a safe distance (Figure 3). These images are used to train a normalized 3D Gaussian Splat for AirSplan, a standard 3D Gaussian Splat for Splat-Nav, and a NeRF for CATNIPS. Only our method and CATNIPS used depth supervision, as Splat-Nav's Nerfstudio pipeline does not support it for 3D Gaussian Splatting. We generate 100 unique tree scenes, each with five pairs of collision-free start and goal configurations for a simulated quadrotor, though a collision-free path between them is not guaranteed to exist.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-B Motion Planning", "weight": 1.0} -->

Fig. 3: Examples of images used to reconstruct the tree environments used in planning experiments. Trees were procedurally generated using L-Systems. 3DGS models were reconstructed from these simulated observations.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-B Motion Planning", "weight": 1.0} -->

The simulator verifies successfully generated trajectories of each method by checking for intersections between the robot and the ground truth obstacle meshes. In the case of AirSplan, the simulator checks for collisions after each time horizon, while for and, collision comparisons are performed post-hoc using the optimized trajectories. In these experiments, AirSplan is run with high-level waypoints computed with a Bidirectional RRT where constraint evaluation is implemented using the same constraint as defined in Theorem 1. The optimizer defined in Algorithm 1 is run in a receding-horizon fashion and the optimizer is constrained to 0.45s to compute each second of motion; if this optimizer fails, the safe braking maneuver is executed, and the planner continues. If after ten planning horizons the vehicle has not moved more than 10cm, the RRT is re-run from the current state. Each trial is run for a maximum of 150 planning horizons.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-B Motion Planning", "weight": 1.0} -->

A success indicates that the quadrotor reached the goal with zero collisions. Failures are counted if the robot fails to reach the goal or if the planned path results in a collision. The parameters used in the motion planning experiments are listed in Table I.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-B Motion Planning", "weight": 1.0} -->

Gaussian culling level BVH buffer size Number of trajectory samples Max optimizer iterations Collision penalty weight Num. spheres in spherepacking TABLE I: Key planning, reachability, and collision-checking parameters used in the motion planning experiments

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-C Ablation Study", "weight": 1.0} -->

Two key features of the system were individually assessed for their contribution to the overall system. First, the flatness-based FRS was replaced with a simple single-sphere overapproximation, mirroring a common approach in the literature. Second, the PZ reachability pipeline proposed in this paper was replaced with that of. However, unlike which over-approximates the robot with a single zonotope, we instead use a sphere to maintain compatibility with the 3DGS collision check.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Results", "weight": 1.0} -->

This section summarizes the results of our experimental evaluations.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Results", "weight": 1.0} -->

Fig. 4: The precision and recall of various collision-checking methods between spheres and radiance fields are evaluated with multiple risk parameters; outlined entries indicate the values used by each method during planning. The proposed collision check yields results that are equivalent to or better than the baselines, with significantly lower computational complexity.

<!-- chunk {"id": "body-0055", "role": "body", "section": "VI-A Collision Constraint", "weight": 1.0} -->

Benchmarking results are found in Table II. The BVH-accelerated collision check is, on average, nearly three times faster than the naive PyTorch implementation, with significantly lower standard deviation. We believe that most of this improvement comes from avoiding the materialization of large intermediate matrices required by the PyTorch implementation.

<!-- chunk {"id": "body-0056", "role": "body", "section": "VI-B Planning", "weight": 1.0} -->

Table III summarizes the end-to-end planning results across 100 procedurally generated tree scenes with 5 start and goal configurations per scene. In addition to success, stuck, and collision rates, we further report the success weighted by path length (SPL). Splat-Nav achieves a success rate of 51.2%, and becomes stuck on the remaining 48.8% of trials. The 'stuck' trials resulted from Splat-Nav classifying the start or goal positions as infeasible, indicating the spherical overapproximation of the robot was too conservative for the highly cluttered test scenes. CATNIPS similarly becomes stuck in 70.4% of the scenes, which is consistent with the finding in Figure 4 that the CATNIPS constraint has high recall but comparatively low precision. In contrast, AirSplan succeeds in 81.2% of scenes without collisions, demonstrating its ability to safely navigate cluttered scenes.

<!-- chunk {"id": "body-0057", "role": "body", "section": "VI-C Ablation Study", "weight": 1.0} -->

Results of the ablation study are presented in Table IV. In the first row, we replace our proposed PZ reachability pipeline with the zonotope reachability method of. This produces a significantly more conservative planner, with success dropping to 16.2% and the robot becoming stuck in 83.8% of trials.

<!-- chunk {"id": "body-0058", "role": "body", "section": "VI-C Ablation Study", "weight": 1.0} -->

Enabling PZ reachability and the sampling-based optimizer raises the success rate to 49.8%. This indicates that polynomial zonotopes provide a less conservative safety representation, even without the flatness-based FRS, but still do not overcome the conservativeness of a single-sphere robot approximation. Enabling flatness-based reachability with a tight sphere packing of the robot but disabling the sampling optimizer reduces the success rate to 25.2%. This reinforces the importance of the sampling-based optimizer. Finally, enabling all proposed features increases the success rate to 81.2%, outperforming all ablations and baselines.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

This paper introduced AirSplan, a novel method that synthesizes risk-aware trajectories for quadrotors in scenes represented using radiance fields. Three key contributions were presented. First, this paper introduced a novel reachability method that leverages differential flatness to tightly overapproximate the robot's forward reach set. Second, a highly parallelizable method was developed for collision checking between spheres and a normalized 3D Gaussian Splat. Finally, a sampling-based optimizer was presented that leveraged the parallel collision check and tight reachability analysis to synthesize risk-aware plans for quadrotors.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

Experiments demonstrate that, unlike state-of-the-art methods, the proposed system plans effectively in cluttered environments. Across 500 planning problems in procedurally generated tree structures, AirSplan successfully found a path in 81.2% of cases, a substantial improvement over the strongest baseline, which achieved a 51.2% success rate. A key takeaway from both the planning experiments and the ablation study is that overapproximating an aerial vehicle with a single sphere limits its ability to generate plans in highly cluttered environments. These results suggest that coupling high-fidelity scene representations with continuous-time reachability analysis enables aerial robots to identify safe paths that would otherwise be rejected by conservative geometric approximations.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

Despite the promising results, the current work has limitations that should be addressed in future work. First, as with other safe motion planners operating in radiance fields, AirSplan assumes that the robot has access to an accurate radiance field representing the scene. While these can be constructed from sensor data, future work will focus on synthesizing plans in incomplete maps generated by radiance-field-based SLAM algorithms. Similarly, current evaluations are limited to simulation. While prior works demonstrate that 3DGS as a representation transfers well between simulation and the real world, future work will validate AirSplan on hardware.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

Furthermore, the current method assumes that the robot can accurately track the planned motion. Methods for incorporating tracking error should be considered in the future to increase robustness in real-world deployments. Finally, the method's computational cost currently requires offboard planning; mitigating this remains future work.
