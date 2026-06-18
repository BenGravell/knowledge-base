<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

EXACT-MPPI: Exact Signed-Distance Navigation for Arbitrary-Footprint Robots from Point Clouds via Path Integral Control

Topics include Model predictive path integral control, Point cloud, Signed distance, Robot navigation, Arbitrary footprints, Collision avoidance.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces an MPPI-based local navigation method that uses exact signed-distance reasoning over point clouds for robots with non-convex or payload-dependent footprints. The paper removes common occupancy-grid and convex-footprint approximations, preserving feasible motions in tight cluttered spaces.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Ground robots often carry payloads, implements, or other attachments that turn their effective footprint into complex, non-convex shapes. Navigating safely through clutter then requires reasoning about this true geometry, yet most local planners simplify it with convex or inflated proxies and rasterize sensor data into occupancy grids or distance fields. Both choices eliminate feasible motions when clearance is comparable to the footprint geometry. We present EXACT-MPPI, a training-free local navigation framework that maps local point-cloud observations and sparse guidance directly to motion commands, without any intermediate map representation. The framework embeds an analytic, exact signed-distance evaluator into a Model Predictive Path Integral (MPPI) controller. The footprint is represented as a simple polygon for general convex or concave planar shapes, with a rectangle-cover specialization for faster evaluation of rectilinear footprints, enabling footprint-aware collision costs without convex decomposition, inflation, or learned encoders. During each MPPI rollout, observed obstacle points are transformed into the predicted body frame and evaluated against the footprint. All operations are batched in JAX, leveraging GPU parallelism for real-time receding-horizon control.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Experiments show that EXACT-MPPI accelerates batched distance evaluation over a learned point-to-robot baseline, preserves feasible motion where convex-footprint planners fail, and remains robust under dense static and moving obstacles. The same framework deploys on differential-drive, Ackermann, omnidirectional, and hybrid-mode platforms by changing only the footprint description and motion model without per-platform training. Pairing exact footprint geometry with sampling-based predictive control thus offers a practical, training-free path to footprint-aware local navigation across diverse robots.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Ground robots are increasingly deployed in cluttered environments, where safe and efficient local navigation requires careful reasoning about the robot's geometry. Many such robots have intricate planar footprints; for example, forklifts carrying palletized loads in warehouse aisles, agricultural platforms towing implements through orchard rows, and mobile manipulators transporting objects through constrained workspaces. The resulting footprint is often non-convex and irregular. In cluttered environments, the available clearance is frequently comparable to the geometric detail of the robot footprint, and accurately accounting for this geometry becomes essential for finding feasible motions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Navigating such robots in cluttered scenes presents several technical challenges. First, accurately evaluating collision geometry against a complex footprint is computationally expensive. To meet real-time requirements, many planners approximate the robot footprint by circles, rectangles, or convex hulls. These approximations can be effective in open environments, but in narrow passages they inflate the collision boundary and eliminate maneuvers that the true footprint would have allowed. Second, most navigation pipelines construct an intermediate environment representation (e.g., an occupancy grid or costmap) before planning can proceed, adding latency and introducing sensitivity to design choices such as grid resolution and inflation radius. Third, navigation commands must respect the kinematic constraints of the robot (e.g., differential-drive or Ackermann), and the planning framework must accommodate different motion models without redesign of its core machinery. Fourth, learning-based approaches that aim to circumvent these issues are typically tied to a specific robot platform and environment, and transferring them to new settings requires extensive retraining in simulation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address these challenges, we propose EXACT-MPPI -- a training-free, perception-to-control local navigation framework for ground robots with complex 2D footprints operating in cluttered environments. The framework computes the exact minimum signed distance analytically between observed obstacle points and the robot footprint, which is modeled as a simple polygon that can be convex or concave, without convex decomposition or inflation. Motion commands are generated directly from point clouds perceived by onboard LiDAR, without constructing any intermediate environment representation such as an occupancy grid, signed-distance field, or local costmap. Collision-aware and smooth local navigation is achieved through Model Predictive Path Integral (MPPI) control, a sampling-based predictive controller that does not require gradient information or differentiable cost functions and supports a wide range of robot kinematics. MPPI is driven by a weak guidance path, and the signed-distance evaluation is incorporated into the cost function as a safety penalty. The signed-distance evaluator and the MPPI trajectory rollouts are implemented as batched JAX computations with GPU acceleration, enabling real-time planning over a receding horizon while preserving the exact polygonal footprint.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main contributions of this work, illustrated in Fig.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose EXACT-MPPI, a perception-to-control local navigation framework that maps local LiDAR point-cloud observations and weak waypoint guidance directly to motion commands, without constructing occupancy grids, signed-distance fields, or local costmaps.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop an analytic point-to-footprint signed-distance evaluator for explicit 2D footprint representations. The simple-polygon formulation handles convex and concave planar footprints in a unified manner, while a rectangle-cover specialization accelerates evaluation for rectilinear footprints.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We integrate this signed-distance evaluator into MPPI as a footprint-aware safety cost and validation mechanism. The evaluator and rollout computations are implemented as JAX-compiled batched operations, parallelized across rollout samples, horizon steps, and obstacle points.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate that the same collision-evaluation and MPPI control structure transfers across multiple ground-robot platforms with different footprints and motion models (differential-drive, Ackermann-steering, omnidirectional, and hybrid). Deploying EXACT-MPPI on a new platform requires only specifying its footprint polygon and motion model. Experiments span indoor environments (office, hallway) and outdoor environments (garden-like) with both static and low-speed dynnamic obstacles, in simulation and on real hardware.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows. Section II reviews related work, and Section III introduces preliminary concepts and notation. Section IV describes the exact minimum signed-distance evaluation and the MPPI cost formulation. Section V presents the experimental design and results. Section VI concludes the paper.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Modular Map-Based Navigation", "weight": 1.0} -->

Most robot navigation systems follow a modular pipeline of perception, mapping, planning, and control. Sensor data is first converted into a structured environment representation such as an occupancy grid, costmap, or Euclidean Signed Distance Field (ESDF), in which obstacle observations are rasterized into occupied cells or pre-computed distance values, and the robot footprint is approximated for collision checking. A local planner then generates kinematically feasible, collision-free trajectories on this representation in response to nearby and possibly dynamic obstacles, and a low-level controller tracks the resulting motion.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Modular Map-Based Navigation", "weight": 1.0} -->

Local planners operating on map representations generally fall into four families. *Reactive methods*, including artificial potential fields, vector field histograms, the nearness diagram method, and the dynamic window approach, compute steering commands from local sensor data while reducing the robot to a point or a disc. *Sampling-based methods*, including lattice planners and Falco, sample candidate motions and score them against a cost function. *Search-based methods*, including Hybrid $A^{\ast}$, discretize the configuration space and apply heuristic search over a costmap. *Optimization-based methods*, including the Timed Elastic Band, EGO-Planner, corridor-based planners that decompose free space into convex regions, and recent swept-volume extensions, generate trajectories by optimizing a cost function over a parameterized trajectory representation.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Modular Map-Based Navigation", "weight": 1.0} -->

A closely related body of work embeds collision avoidance within a model predictive control (MPC) framework, solving a finite-horizon optimal control problem at each control step. Representative examples include model predictive contouring control, CIAO, and optimization-based collision avoidance (OBCA), which handles full-shape robot-obstacle distance through a convex-duality reformulation. Control barrier functions provide a complementary, control-level safety mechanism by enforcing forward invariance of a safe set defined by a smooth distance-like function.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Modular Map-Based Navigation", "weight": 1.0} -->

These methods share three limitations when applied to robots with complex footprints in cluttered environments. First, they rely on an intermediate map representation whose discrete structure introduces sensitivity to grid resolution and inflation radius and a loss of geometric detail relative to the raw sensor data. Second, obstacle and robot geometry are typically simplified into convex, smooth, or inflated proxies, inflating the collision boundary and eliminating maneuvers that the true footprint would have permitted. Methods that retain exact geometry, such as OBCA and swept-volume extensions, can incur a computational cost that limits real-time use on densely cluttered problems. Third, when the footprint is geometrically detailed, the modular separation between perception, planning, and control compounds the first two limitations: small geometric details available in the raw sensor data are abstracted away at the mapping stage and are no longer accessible to the planner. EXACT-MPPI addresses these limitations by evaluating analytic point-to-footprint signed distances directly between observed obstacle points and an explicit planar footprint representation in the robot body frame. It avoids map rasterization in the local collision-evaluation loop and generates control commands through a perception-to-control sampling-based predictive controller.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Learning-Based Navigation", "weight": 1.0} -->

A second body of work replaces parts or all of the navigation pipeline with learned components. We distinguish two groups: end-to-end policies that map sensor observations directly to control, and model-based learning approaches that retain a model-based planner or controller but learn one or more of its subroutines.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Learning-Based Navigation", "weight": 1.0} -->

End-to-end policies. Pioneered by ALVINN and revived for highway driving by Bojarski et al., end-to-end methods have demonstrated strong performance in automotive domains through large-scale imitation learning. Recent work has also explored LiDAR-based reinforcement learning policies for navigation in dynamic environments. To improve sample efficiency and generalization, subsequent work has introduced inductive biases for planning, including value iteration networks and motion-planning networks such as MPNet. Recent foundation-model-style navigation policies such as ViNT further target cross-embodiment generalization across heterogeneous robots and environments. Despite this progress, end-to-end methods face a structural data requirement. Unlike autonomous driving, where fleet-scale data is abundant, applications such as warehousing and orchard operations are characterized by data scarcity, distributional shifts, and platform-specific footprint geometries. Policies that perform well on benchmark distributions frequently exhibit out-of-distribution degradation when environment topology, obstacle density, or robot dimensions differ from the training set, often necessitating site-specific retraining or parameter tuning.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Learning-Based Navigation", "weight": 1.0} -->

Model-based learning approaches. A second group retains a model-based formulation but replaces specific subroutines with learned components, aiming to preserve interpretability and constraint handling while accelerating expensive computations. Hybrid architectures such as iPlanner combine a learned perception front-end with classical trajectory optimization. The most closely related example, and the most direct point of comparison for our work, is NeuPAN. NeuPAN formulates navigation as an end-to-end model-based learning problem in which point-cloud observations, robot geometry, and predictive control are coupled within a unified perception-to-control pipeline. A deep unfoldered neural encoder (DUNE) maps raw obstacle points to latent distance features, which are then consumed by a neural regularized motion planner (NRMP). The encoder amortizes the cost of solving a per-point convex distance subproblem derived from a duality-based formulation of point-to-body distance, enabling real-time evaluation across thousands of points. NeuPAN demonstrates strong performance in cluttered environments on differential-drive, wheel-legged, and passenger-vehicle platforms.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Learning-Based Navigation", "weight": 1.0} -->

EXACT-MPPI shares NeuPAN's robot-centric, perception-to-control viewpoint and its goal of avoiding intermediate map representations, but differs in three design choices. First, NeuPAN's DUNE encodes the robot footprint into network weights through training, so the encoder must be retrained whenever the footprint changes. In contrast, we compute the point-to-footprint signed distance analytically, so adapting to a new footprint requires only updating the polygon description. Second, NeuPAN's distance formulation models the robot as a convex set, with non-convex bodies represented as the union of convex sets; our analytic evaluator handles simple polygons, including concave ones, as a single object. Third, NeuPAN's NRMP solves a biconvex motion-planning problem via proximal alternating minimization, a gradient-based scheme whose regularizer parameters are tuned in simulation. Because the analytic distance function we use is non-smooth, we instead adopt sampling-based MPPI control, which is gradient-free, batches naturally on GPU, and accommodates a wide range of robot kinematics without retraining.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-C Sampling-Based Predictive Control", "weight": 1.0} -->

EXACT-MPPI adopts Model Predictive Path Integral (MPPI) control, the most widely used formulation of sampling-based predictive control. In this family, trajectory candidates are drawn from a stochastic distribution and weighted by their costs. This formulation accommodates non-smooth, non-convex cost functions and a broad class of rollout dynamics, and its sampling structure maps naturally onto GPU parallelism. MPPI has been deployed for aggressive off-road driving, autonomous racing, and agile flight. Subsequent work has targeted robustness and sample efficiency: Log-MPPI uses a heavy-tailed sampling distribution for broader trajectory-space exploration, and smooth variants reduce control chatter.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-C Sampling-Based Predictive Control", "weight": 1.0} -->

Despite these advances, MPPI's treatment of collision avoidance has received comparatively less attention. Many implementations delegate collision evaluation to map-based primitives such as costmap lookups or grid-based signed-distance fields. These primitives inherit the footprint-simplification and resolution-sensitivity issues discussed in Sec. II-A, particularly when the footprint is non-convex or obstacle density is high.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-C Sampling-Based Predictive Control", "weight": 1.0} -->

To address this gap, EXACT-MPPI integrates MPPI with an analytic body-frame signed-distance evaluator that operates directly on observed obstacle points and the robot's polygonal footprint. The evaluator and rollout computations are implemented as JAX-compiled batched operations. This combines MPPI's sampling parallelism with exact-shape collision evaluation, without any costmap or ESDF queries.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Problem Setting", "weight": 1.0} -->

At each replanning instant, the controller receives a local point cloud from onboard LiDAR and the current robot state from onboard state estimation. We denote the current planar pose of the robot by $\mathbf{q}_{0} = {\lbrack x_{0},y_{0},\theta_{0}\rbrack}^{\top}$, expressed in the local planning frame. Collision costs are evaluated with respect to the observed local obstacle points after preprocessing, rather than against a continuous obstacle surface or a rasterized map. The collision-relevant geometry of the robot is captured by a two-dimensional projected footprint that includes the chassis together with any rigidly attached or carried geometry. The detailed model is given in Sec. III-B.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A Problem Setting", "weight": 1.0} -->

We assume that weak guidance is available from an upstream module. Examples include a target pose, waypoint sequence, reference path, or learned navigation prior. This assumption matches the applications that motivate this work: warehouse forklifts receive target pallet poses from fleet- or task-level planners, agricultural platforms follow between-row reference paths generated from prior maps or row-detection modules, and mobile manipulators receive target object poses from task planners. In all these cases, the local controller is responsible for following the high-level intent safely through clutter, not for generating the intent itself.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Problem Setting", "weight": 1.0} -->

To handle dynamic obstacles, the controller treats them as quasi-static within a single short MPPI horizon. Collisions are then re-evaluated at each replanning step through receding-horizon updates. The core formulation does not include an explicit motion-prediction model, but one can be added separately if required.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Robot Effective Footprint", "weight": 1.0} -->

We represent the collision-relevant geometry of the robot by an *effective footprint*: a compact planar set in the robot body frame,

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B Robot Effective Footprint", "weight": 1.0} -->

used for collision checking and clearance evaluation during local navigation. Depending on the platform, $\mathcal{B}_{eff}$ may correspond to the chassis alone or include any rigidly attached or carried geometry. We write

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B Robot Effective Footprint", "weight": 1.0} -->

where $\mathcal{B}_{chassis}$ denotes the nominal chassis and $\mathcal{B}_{add}$ denotes any added geometry, such as a palletized load on a forklift, a trailing implement on an agricultural platform, or an object grasped by a mobile manipulator.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B Robot Effective Footprint", "weight": 1.0} -->

The effective footprint is assumed fixed in the body frame during a navigation episode. Different platform configurations are accommodated by updating $\mathcal{B}_{eff}$, with no per-platform training required. In practice, $\mathcal{B}_{eff}$ is represented either by a rectangle cover or by a (possibly non-convex) simple polygon, depending on the platform geometry. The computational details are given in Sec. IV-B.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-C Robot--Obstacle Signed Distance", "weight": 1.0} -->

At each replanning instant, the controller uses a preprocessed local obstacle set

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-C Robot--Obstacle Signed Distance", "weight": 1.0} -->

expressed in the current planning frame. Here $N$ denotes the number of obstacle points supplied to the controller after height filtering and downsampling, rather than the number of original LiDAR returns.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-C Robot--Obstacle Signed Distance", "weight": 1.0} -->

The signed distance from a body-frame query point $\mathbf{p}$ to the effective footprint, denoted

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-C Robot--Obstacle Signed Distance", "weight": 1.0} -->

is negative inside $\mathcal{B}_{eff}$, zero on its boundary, and positive outside. Throughout this paper, the query is taken against observed obstacle points rather than a continuous obstacle surface. Explicit formulas for $d^{\pm}$ are derived in Sec. IV-C.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-C Robot--Obstacle Signed Distance", "weight": 1.0} -->

The minimum signed distance from $\mathcal{O}$ to the robot footprint at the current pose is

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-C Robot--Obstacle Signed Distance", "weight": 1.0} -->

A negative value $d^{\min} < 0$ indicates that at least one obstacle point lies inside the effective footprint. A positive value is the minimum point-wise clearance to the local obstacle set.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-D Robot Kinematic Models", "weight": 1.0} -->

Let $m \in \mathcal{M}$ index the motion model used for state propagation. The planar pose $\mathbf{q}_{h} = {\lbrack x_{h},y_{h},\theta_{h}\rbrack}^{\top}$ is propagated with a forward-Euler discretization,

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-D Robot Kinematic Models", "weight": 1.0} -->

where $\mathbf{u}_{h} \in {\mathbb{R}}^{n_{u}}$ is the control input, $\Deltat$ is the sampling interval, and $\mathcal{F}_{m}{( \cdot )}$ denotes the model-specific continuous-time kinematics.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-D Robot Kinematic Models", "weight": 1.0} -->

We consider the following motion models in our experiments. The differential-drive (or unicycle) model takes control input $\mathbf{u} = {\lbrack v,\omega\rbrack}^{\top}$, where $v$ is the linear velocity and $\omega$ is the angular velocity, with kinematics

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-D Robot Kinematic Models", "weight": 1.0} -->

The Ackermann (or bicycle) model takes $\mathbf{u} = {\lbrack v,\delta\rbrack}^{\top}$, where $\delta$ is the steering angle, with kinematics

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-D Robot Kinematic Models", "weight": 1.0} -->

For platforms that accept planar body-frame velocity commands, the omni-motion model is

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-D Robot Kinematic Models", "weight": 1.0} -->

where $v_{x}$ and $v_{y}$ are the body-frame longitudinal and lateral velocities. The spin-in-place mode is represented by

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-D Robot Kinematic Models", "weight": 1.0} -->

For hybrid platforms that additionally support lateral translation (e.g., the AgileX Ranger Mini ), a parallel-motion mode is modeled as

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-D Robot Kinematic Models", "weight": 1.0} -->

where $v_{para}$ is the signed lateral body-frame velocity, that is, translation along the body-frame $y$-axis with the heading preserved.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-E MPPI Formulation", "weight": 1.0} -->

Model Predictive Path Integral (MPPI) control is used as the receding-horizon local controller. At each replanning instant, the controller maintains a nominal control sequence

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-E MPPI Formulation", "weight": 1.0} -->

where $T$ is the planning horizon length. MPPI generates $K$ sampled rollout sequences by perturbing this nominal sequence,

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-E MPPI Formulation", "weight": 1.0} -->

where $\mathbf{\epsilon}_{h}^{(r)}$ is the sampled control perturbation for rollout $r$ at horizon step $h$. The corresponding perturbed control sequence is denoted by

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-E MPPI Formulation", "weight": 1.0} -->

Using the Euler discretization in Sec. III-D, each rollout starts from $\mathbf{q}_{0}$ and follows

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-E MPPI Formulation", "weight": 1.0} -->

under the selected motion model $m$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-E MPPI Formulation", "weight": 1.0} -->

At a high level, MPPI evaluates sampled control sequences using a finite-horizon cost that combines task, control-regularization, and safety terms. In EXACT-MPPI, the safety term is defined by the minimum signed distance between the predicted robot footprint and the local obstacle observation. For rollout $r$, we write

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-E MPPI Formulation", "weight": 1.0} -->

where $\phi_{task}$ represents navigation objectives such as goal seeking, path following, or progress along a reference path, $\phi_{ctrl}$ regularizes the sampled control command, and $\phi_{obs}$ penalizes collision or insufficient clearance. The scalar $d_{h}^{\min,{(r)}}$ denotes the minimum signed distance evaluated at the rollout state $\mathbf{q}_{h}^{(r)}$ over the local obstacle points; its rollout-frame definition is given in Sec. IV-C.

<!-- chunk {"id": "body-0053", "role": "body", "section": "III-E MPPI Formulation", "weight": 1.0} -->

After all rollouts are evaluated, MPPI assigns an importance weight to each rollout according to its relative cost. Let

<!-- chunk {"id": "body-0054", "role": "body", "section": "III-E MPPI Formulation", "weight": 1.0} -->

where $\lambda > 0$ is the temperature parameter. The nominal control sequence is then updated by the weighted average of the sampled perturbations,

<!-- chunk {"id": "body-0055", "role": "body", "section": "III-E MPPI Formulation", "weight": 1.0} -->

This update is a stochastic receding-horizon improvement step rather than an exact solution of the nonlinear finite-horizon optimal control problem. After the update, only the first control command is executed. The horizon is then shifted forward, the local obstacle observation is refreshed, and the procedure is repeated at the next replanning instant. The specific signed-distance computation, safety cost, feasibility screening, trajectory validation, and batched implementation used in EXACT-MPPI are described in Sec. IV.

<!-- chunk {"id": "body-0056", "role": "body", "section": "III-E MPPI Formulation", "weight": 1.0} -->

The main MPPI parameters that determine the sampling budget are the rollout count $K$, horizon length $T$, integration step $\Deltat$, control-perturbation distribution, and temperature $\lambda$. The physical prediction horizon is $T\Deltat$. Each control cycle samples $K$ candidate control sequences, corresponding to $KT$ perturbed control inputs and $K{({T + 1})}$ rollout states before the first command is executed. In the footprint-aware setting, the obstacle point budget $N$, safety margin $d_{safe}$, and cost weights further determine the number and influence of collision checks performed per cycle.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Methodology", "weight": 1.0} -->

We describe the computational realization of EXACT-MPPI, building on the formulation introduced in Sec. III. As shown in Fig. 2, local point-cloud observations are reduced to a fixed-budget obstacle set. MPPI rollouts are propagated under the selected kinematics, obstacle points are transformed into each predicted body frame, and signed-distance values are used for rollout scoring, control-sequence update, and safety validation.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-A Overview of EXACT-MPPI", "weight": 1.0} -->

At each replanning instant, EXACT-MPPI receives three inputs: weak guidance from an upstream module, the current robot velocity, and a compact local obstacle set. The weak guidance is provided as a target pose or short waypoint sequence in the current robot frame, which defines the local navigation intent without requiring a dense reference trajectory. The current chassis velocity, obtained from odometry, is used to warm-start the nominal control sequence. The obstacle set is obtained from the local point cloud by retaining points within a task-relevant height range and downsampling them to a fixed budget $N$. The downsampling procedure is applied before rollout evaluation and determines the point-wise obstacle set against which clearance is measured.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-A Overview of EXACT-MPPI", "weight": 1.0} -->

Given these inputs, MPPI samples $K$ control rollouts over $T$ horizon steps, and propagates the corresponding state trajectories under the selected motion model. For each predicted state, the $N$ obstacle points are transformed into the predicted robot body frame, where signed distance is evaluated against the explicit 2D effective footprint. The resulting minimum signed-distance values are used with task and control costs to score the rollouts, screen unsafe candidates, update the nominal control sequence, and validate the selected trajectory before executing only the first command.

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-B Computational Footprint Representations", "weight": 1.0} -->

Starting from the effective-footprint model in Sec. III-B, we use two representations for signed-distance evaluation. The choice between them reflects a deliberate trade-off between geometric generality and computational efficiency. The general simple-polygon representation handles arbitrary boundary shapes, including non-convex footprints, but requires per-edge projection and a point-in-polygon test. The rectangle-cover representation is restricted to orthogonal footprints, but admits a closed-form point-to-box distance that is substantially cheaper to batch on the GPU. EXACT-MPPI retains both routes so that rectilinear platforms benefit from the faster evaluator without sacrificing the ability to handle more general footprints. We use $R$ for the number of rectangles in a rectangle cover and $B$ for the number of boundary edges (equivalently, vertices) in a polygonal footprint.

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-B1 Orthogonal Footprints via Rectangle Covering", "weight": 1.0} -->

A footprint is termed *rectilinear* when its boundary edges are axis-aligned and meet at right angles. Many vehicle chassis and attached implements fall in this class. For such footprints, the effective footprint is represented as a union of axis-aligned rectangles in the body frame,

<!-- chunk {"id": "body-0062", "role": "body", "section": "IV-B1 Orthogonal Footprints via Rectangle Covering", "weight": 1.0} -->

Each rectangle $\mathcal{R}_{j}$ is parameterized by its center $\mathbf{c}_{j} \in {\mathbb{R}}^{2}$ and half-extent $\mathbf{s}_{j} \in {\mathbb{R}}_{+}^{2}$. We retain this representation alongside the general polygon route purely for computational efficiency. The closed-form point-to-box distance derived in Sec. IV-C requires only elementwise arithmetic and a single vector norm per rectangle, with no branching, sorting, or topology test, which makes it well suited to batched rollout evaluation on the GPU.

<!-- chunk {"id": "body-0063", "role": "body", "section": "IV-B2 General Simple Polygonal Footprints", "weight": 1.0} -->

For footprints whose boundary is not rectilinear, including concave shapes such as those resulting from attached implements or grasped objects, the effective footprint is described by an ordered cyclic sequence of $B$ vertices in the body frame,

<!-- chunk {"id": "body-0064", "role": "body", "section": "IV-B2 General Simple Polygonal Footprints", "weight": 1.0} -->

with the wrap-around convention $\mathbf{v}_{B + 1} \equiv \mathbf{v}_{1}$. The polygon is *simple* in the sense that its boundary is a non-self-intersecting closed curve. The boundary consists of $B$ directed edges, each represented as a vector,

<!-- chunk {"id": "body-0065", "role": "body", "section": "IV-B2 General Simple Polygonal Footprints", "weight": 1.0} -->

This vector form is used as the basic primitive in the point-to-segment distance derived in Sec. IV-C.

<!-- chunk {"id": "body-0066", "role": "body", "section": "IV-C Signed Distance Evaluation", "weight": 1.0} -->

We now instantiate the signed-distance evaluation in Eq.. For both footprint representations in Sec. IV-B, distance queries are evaluated in the predicted robot body frame. Thus, the effective footprint remains fixed during rollout evaluation, while the preprocessed obstacle points are transformed according to each predicted rollout pose.

<!-- chunk {"id": "body-0067", "role": "body", "section": "IV-C1 Rollout-Frame Transformation", "weight": 1.0} -->

Let $\mathcal{O} = {\{\mathbf{o}_{i}\}}_{i = 1}^{N}$ denote the preprocessed local obstacle set supplied to the controller, expressed in the current planning frame. During rollout evaluation, this same obstacle set is copied across sampled trajectories and horizon steps. For rollout $r$ and horizon step $h$, let

<!-- chunk {"id": "body-0068", "role": "body", "section": "IV-C1 Rollout-Frame Transformation", "weight": 1.0} -->

denote the predicted robot pose relative to the current planning frame, with $\mathbf{t}_{h}^{(r)} = {\lbrack x_{h}^{(r)},y_{h}^{(r)}\rbrack}^{\top}$. Each obstacle point is re-expressed in the predicted body frame as

<!-- chunk {"id": "body-0069", "role": "body", "section": "IV-C1 Rollout-Frame Transformation", "weight": 1.0} -->

The resulting points are then evaluated against the effective footprint in the predicted body frame. In this way, EXACT-MPPI keeps the footprint representation static and instead transforms the local obstacle observation into the body frame of each rollout pose for signed-distance evaluation.

<!-- chunk {"id": "body-0070", "role": "body", "section": "IV-C2 Distance to Orthogonal Footprints", "weight": 1.0} -->

For a body-frame query point $\mathbf{p}$ and a rectangle $\mathcal{R}_{j}$ with center $\mathbf{c}_{j}$ and half-extent $\mathbf{s}_{j}$, define

<!-- chunk {"id": "body-0071", "role": "body", "section": "IV-C2 Distance to Orthogonal Footprints", "weight": 1.0} -->

where the absolute value is applied elementwise. The point-to-box signed distance is

<!-- chunk {"id": "body-0072", "role": "body", "section": "IV-C2 Distance to Orthogonal Footprints", "weight": 1.0} -->

where $\max{( \cdot,0)}$ inside the norm is taken elementwise and $a_{j,x},a_{j,y}$ are the components of $\mathbf{a}_{j}{(\mathbf{p})}$. For a rectangle-cover footprint, the signed distance is obtained by reduction over the $R$ rectangles,

<!-- chunk {"id": "body-0073", "role": "body", "section": "IV-C3 Distance to General Simple Polygonal Footprint", "weight": 1.0} -->

For a simple polygonal footprint, the unsigned distance to the boundary is the minimum distance to its polygon edges. For an edge $\mathbf{e}_{b} = {\mathbf{v}_{b + 1} - \mathbf{v}_{b}}$, define the clipped projection parameter

<!-- chunk {"id": "body-0074", "role": "body", "section": "IV-C3 Distance to General Simple Polygonal Footprint", "weight": 1.0} -->

and the corresponding point-to-segment distance

<!-- chunk {"id": "body-0075", "role": "body", "section": "IV-C3 Distance to General Simple Polygonal Footprint", "weight": 1.0} -->

The sign is assigned using a point-in-polygon test (implemented via ray casting),

<!-- chunk {"id": "body-0076", "role": "body", "section": "IV-C3 Distance to General Simple Polygonal Footprint", "weight": 1.0} -->

The signed distance to the simple polygonal footprint is then

<!-- chunk {"id": "body-0077", "role": "body", "section": "IV-C3 Distance to General Simple Polygonal Footprint", "weight": 1.0} -->

This quantity is the exact signed distance for the represented simple polygon, whether convex or non-convex.

<!-- chunk {"id": "body-0078", "role": "body", "section": "IV-C3 Distance to General Simple Polygonal Footprint", "weight": 1.0} -->

Exactness and sign correctness. For a simple polygonal footprint, the method computes the exact Euclidean distance to the polygon boundary and assigns the sign through the inside--outside test. For a rectangle-union footprint, the min-reduced box signed distance is sign-correct: it is negative if and only if the query point lies inside at least one rectangle, zero on the exterior boundary of the union, and positive outside. For points outside the rectangle union, the exterior distance is exact. For points inside regions where multiple rectangles overlap, the interior penetration magnitude may differ from the true signed-distance magnitude, but the collision classification remains correct. In EXACT-MPPI, this signed-distance quantity is used primarily for collision screening and clearance penalization near the footprint boundary.

<!-- chunk {"id": "body-0079", "role": "body", "section": "IV-D Batched Rollout and Distance Computation", "weight": 1.0} -->

The dominant computation at each control cycle is the joint evaluation of $K$ sampled rollouts, $T$ horizon steps per rollout, and $N$ obstacle points. Together these produce $K \times T \times N$ signed-distance queries. The preprocessed obstacle set is stored as a fixed-size array of $N$ points with an accompanying validity mask. Padding is used when the number of observed obstacle points is smaller than $N$, and the mask prevents padded entries from contributing to the distance reduction. The obstacle array is then broadcast over the rollout and horizon dimensions, producing $K \times T \times N$ body-frame query points $\mathbf{p}_{h,i}^{b,{(r)}}$ for signed-distance evaluation.

<!-- chunk {"id": "body-0080", "role": "body", "section": "IV-D Batched Rollout and Distance Computation", "weight": 1.0} -->

The rollout and distance computations are implemented in batched form. For rollout propagation, the selected motion model is evaluated over the $K$ sampled control sequences. For collision evaluation, the rollout-frame transformation of Sec. IV-C is applied over the rollout, horizon, and obstacle-point dimensions. The transformed query points are then evaluated using either the rectangle-cover signed-distance function $d_{rect}^{\pm}$ or the polygonal signed-distance function $d_{poly}^{\pm}$. The validity mask is applied during the reduction over obstacle points so that padded entries do not affect the result. This produces the minimum signed-distance matrix

<!-- chunk {"id": "body-0081", "role": "body", "section": "IV-D Batched Rollout and Distance Computation", "weight": 1.0} -->

of size $K \times T$. These values are used for rollout scoring, feasibility screening, and trajectory validation (Sec. IV-E).

<!-- chunk {"id": "body-0082", "role": "body", "section": "IV-D Batched Rollout and Distance Computation", "weight": 1.0} -->

The signed-distance stage evaluates a batched set of $K \times T \times N$ body-frame query points. For a rectangle-cover footprint, each query point is reduced over $R$ point-to-box distances, giving computational cost $O{({KTNR})}$. For a polygonal footprint, each query point requires a reduction over $B$ point-to-segment distances and an inside--outside test that also scales with $B$, giving computational cost $O{({KTNB})}$. The arithmetic operations inside each point-to-box or point-to-segment evaluation are constant-size vector operations and therefore affect the constant factor rather than the asymptotic scaling.

<!-- chunk {"id": "body-0083", "role": "body", "section": "IV-D Batched Rollout and Distance Computation", "weight": 1.0} -->

Although these computations are executed efficiently in batched form on the GPU, the total number of point-to-primitive evaluations still scales with the rollout count, horizon length, obstacle-point budget, and footprint primitive count. We implement the computation in JAX. Just-in-time compilation and automatic vectorization allow the per-rollout, per-horizon-step, per-point, and per-footprint-primitive operations to be written in NumPy-like syntax and compiled into optimized computations for CPU or GPU execution. Compilation occurs at the first control cycle for a fixed input shape, and subsequent cycles reuse the compiled computation.

<!-- chunk {"id": "body-0084", "role": "body", "section": "IV-E Safety Penalties and Trajectory Validation", "weight": 1.0} -->

The signed-distance quantities computed during rollout evaluation are incorporated into MPPI through both a soft obstacle penalty and a hard post-update validation step. For a rollout state with minimum signed distance $d$, we use the obstacle penalty

<!-- chunk {"id": "body-0085", "role": "body", "section": "IV-E Safety Penalties and Trajectory Validation", "weight": 1.0} -->

where $w_{coll}$ is a large collision penalty, $w_{rep}$ weights the clearance penalty, $d_{safe}$ is the desired safety margin, and ${\mathbb{I}}{( \cdot )}$ denotes the indicator function ($1$ when its argument is true and $0$ otherwise). The first term penalizes penetration of the effective footprint, while the second term discourages trajectories that pass closer than the safety margin.

<!-- chunk {"id": "body-0086", "role": "body", "section": "IV-E Safety Penalties and Trajectory Validation", "weight": 1.0} -->

In addition to this soft penalty, rollout scoring records an unsafe flag $\chi^{(r)}$ whenever any horizon step violates the safety margin,

<!-- chunk {"id": "body-0087", "role": "body", "section": "IV-E Safety Penalties and Trajectory Validation", "weight": 1.0} -->

The rollout cost used for MPPI weighting is then augmented as

<!-- chunk {"id": "body-0088", "role": "body", "section": "IV-E Safety Penalties and Trajectory Validation", "weight": 1.0} -->

where $w_{\inf}$ is chosen large enough that unsafe rollouts receive negligible importance weight.

<!-- chunk {"id": "body-0089", "role": "body", "section": "IV-E Safety Penalties and Trajectory Validation", "weight": 1.0} -->

After the nominal control sequence is updated by the MPPI weighted-average rule, the corresponding nominal trajectory is rolled out once and validated using the same clearance condition,

<!-- chunk {"id": "body-0090", "role": "body", "section": "IV-E Safety Penalties and Trajectory Validation", "weight": 1.0} -->

where $d_{h}^{\min,{nom}}$ denotes the minimum signed distance evaluated along the updated nominal trajectory (the rollout superscript is dropped because there is a single nominal trajectory). If this validation fails, the controller executes a zero-velocity hold for the current cycle and reinitializes the nominal control sequence to zero for the next replanning step. If validation succeeds, the first command of the updated sequence is executed, and the remaining sequence is shifted forward in standard receding-horizon fashion. Algorithm 1 summarizes one control cycle of EXACT-MPPI.

<!-- chunk {"id": "body-0091", "role": "body", "section": "IV-E Safety Penalties and Trajectory Validation", "weight": 1.0} -->

1Input: pose q0, nominal 𝕌, obstacles 𝒪, footprint ℬeff, motion model m 2 Params: K, T, Δ t, λ, dsafe, wcoll, wrep, winf /* 1. Batched rollout propagation */ 4 Sample ϵh(r); form uh(r) ← uh + ϵh(r); propagate qh + 1(r) ← qh(r) + ℱm (qh(r),uh(r)) Δ t from q0(r) = q0; /* 2. Signed-distance evaluation and scoring */ 8 Transform 𝒪 into the body frame at qh(r) to obtain ph, ib, (r); 9 dhmin, (r) ← minid± (ph, ib, (r),ℬeff); 10 J(r) ← J(r) + ϕtask (qh(r),uh(r)) + ϕctrl (uh(r)) + ϕobs (dhmin, (r)); /* 3. Feasibility flag and path-integral update */ 15

<!-- chunk {"id": "body-0092", "role": "body", "section": "IV-F Extension to Hybrid-Mode Platforms", "weight": 1.0} -->

Some mobile platforms achieve near-holonomic maneuverability through a finite set of non-skidding motion modes (e.g., dual-Ackermann steering, lateral parallel motion, spin-in-place). Treating the command space as fully continuous can produce motions that require wheel slip to execute. Selecting among discrete modes avoids this but introduces mode-switching decisions. We therefore extend MPPI to a hybrid-mode formulation that evaluates each mode as a separate rollout family and selects among them at each control cycle.

<!-- chunk {"id": "body-0093", "role": "body", "section": "IV-F Extension to Hybrid-Mode Platforms", "weight": 1.0} -->

Let $\mathcal{M}_{hyb}$ denote the set of active motion modes. For each $m \in \mathcal{M}_{hyb}$, EXACT-MPPI runs the Algorithm 1 cycle under dynamics $\mathcal{F}_{m}$, producing a validated candidate sequence ${\mathbb{U}}_{m}$ with cost $J_{m}$. The signed-distance evaluator and effective footprint are shared across modes; only the rollout dynamics and admissible command structure differ.

<!-- chunk {"id": "body-0094", "role": "body", "section": "IV-F Extension to Hybrid-Mode Platforms", "weight": 1.0} -->

To discourage unnecessary switching, each candidate cost is augmented with a switching penalty relative to the previously active mode $m_{prev}$,

<!-- chunk {"id": "body-0095", "role": "body", "section": "IV-F Extension to Hybrid-Mode Platforms", "weight": 1.0} -->

Candidates that fail trajectory validation are assigned ${\overline{J}}_{m} = {+ \infty}$ and excluded. A cooldown variable further blocks mode changes for a fixed number of replanning steps after a switch. The selected mode is $m^{\star} = {\arg{\min_{m}{\overline{J}}_{m}}}$.

<!-- chunk {"id": "body-0096", "role": "body", "section": "IV-F Extension to Hybrid-Mode Platforms", "weight": 1.0} -->

For physical deployment, the chosen command is projected onto the command structure of mode $m^{\star}$ and passed through a deadzone correction. If its magnitude falls below a mode-dependent threshold, it is scaled to the minimum executable value. The direction is preserved for translational modes and the sign is preserved for pure rotation. This post-processing affects only hardware execution, not the rollout-time signed-distance evaluation. Algorithm 2 summarizes the full procedure.

<!-- chunk {"id": "body-0097", "role": "body", "section": "IV-F Extension to Hybrid-Mode Platforms", "weight": 1.0} -->

1Input: pose q0, sequences {𝕌m}m ∈ ℳhyb, obstacles 𝒪, footprint ℬeff, mprev, τcool 2 Params: λswitch, τcoolmax, vmin, ωmin, δnoisev, δnoiseω (plus Algorithm 1 parameters) 3 Output: command u*, mode m* /* 1. Per-mode rollout evaluation */ 5 Run Algorithm 1 with dynamics ℱm to obtain 𝕌m, Jm, νm; 6 ${\overline{J}}_{m}\leftarrow{J_{m} + {\lambda_{switch}{\mathbb{I}}{({m \neq m_{prev}})}}}$ if νm, else + ∞; /* 2. Mode selection with cooldown */ if ${\overline{J}}_{m} = {+ {\infty{\forall m}}}$ then return 0, mprev; 11

<!-- chunk {"id": "body-0098", "role": "body", "section": "IV-F Extension to Hybrid-Mode Platforms", "weight": 1.0} -->

$m^{\ast}\leftarrow{\arg{\min_{m}{\overline{J}}_{m}}}$; 12 if τcool &gt; 0 and m* ≠ mprev then m* ← mprev; 13 τcool ← τcoolmax if m* ≠ mprev, else max (τcool − 1,0); 14 uraw← first command of 𝕌m*; // drop components inadmissible for m* 16 Let ulin*, ω* denote the linear and angular parts of u*; 18 vmag ← ∥ulin*∥2; if δnoisev &lt; vmag &lt; vmin then ulin* ← (vmin/vmag) ulin*; 21 if δnoiseω &lt; |ω*| &lt; ωmin then ω* ← sgn(ω*) ωmin; Algorithm 2 Hybrid-Mode EXACT-MPPI with Actuator Post-Processing

<!-- chunk {"id": "body-0099", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

We evaluate EXACT-MPPI in simulation and real-world settings across multiple robot platforms with distinct footprint geometries and kinematic characteristics.

<!-- chunk {"id": "body-0100", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

Computational efficiency: Can the JAX-based batched signed-distance evaluator support real-time MPPI rollout evaluation under a fixed sampling budget?

<!-- chunk {"id": "body-0101", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

Footprint-modeling fidelity: Does explicit footprint-aware signed-distance evaluation preserve feasible motion in clearance-limited environments where convex-hull or simplified footprint approximations become overly conservative?

<!-- chunk {"id": "body-0102", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

Cross-platform deployment: Can the same collision-evaluation and MPPI update structure be reused across platforms by changing only the explicit footprint representation and the platform-specific rollout model, including cases with carried objects, payloads, or implements?

<!-- chunk {"id": "body-0103", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

Hybrid-motion adaptability: Can the same footprint-aware MPPI formulation be extended to platforms with multiple kinematic modes, enabling mode selection through rollout-cost evaluation rather than manually designed mode-specific navigation rules?

<!-- chunk {"id": "body-0104", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

Dynamic-obstacle experiments are included as a supporting evaluation. Since EXACT-MPPI does not explicitly predict obstacle motion, moving obstacles are treated as quasi-static within each MPPI horizon. Reactivity is obtained through receding-horizon replanning from updated point-cloud observations. Therefore, the dynamic-obstacle results should be interpreted within the low-speed settings considered in this work.

<!-- chunk {"id": "body-0105", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

Experimental Platforms and Environments. We conduct experiments in simulation and on real robot platforms to evaluate EXACT-MPPI under different footprint geometries, motion models, sensing conditions, and obstacle configurations. In simulation, controlled narrow-passage scenarios are used to evaluate footprint-modeling fidelity under different degrees of narrowness, while dynamic-obstacle scenarios are used to evaluate reactive replanning from updated point-cloud observations. IR-SIM is used as the main lightweight simulator, and Gazebo is used for the higher-fidelity dynamic-obstacle comparison. To support the omni-directional body-velocity cases considered in this work, we adapt IR-SIM with a control interface that accepts longitudinal, lateral, and yaw-rate commands.

<!-- chunk {"id": "body-0106", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

Feature Dual-arm robot AgileX Ranger mini Unitree Go2 Ack.

<!-- chunk {"id": "body-0107", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

Parallel Spin Motion model(s) Differential mode Dual-Ackermann mode Parallel mode Spin mode Omni-motion mode Control input(s) (vx,ω) (vx,ω) (vx,vy) (ω) (vx,vy,ω) Longitudinal velocity limit (m/s) vx ∈ [−1.5, 1.5] vx ∈ [−1.5, 1.5] vx ∈ [−1.0, 1.0] vx = 0 vx ∈ [−1.0, 1.0] Lateral velocity limit (m/s) Not used Not used vy ∈ [−0.6, 0.6] Not used vy ∈ [−0.4, 0.4] Yaw-rate limit (rad/s) ω ∈ [−1.0, 1.0] ω ∈ [−1.0, 1.0] ω = 0 ω ∈ [−1.0, 1.0] ω ∈ [−1.0, 1.0] Linear acceleration limit (m/s2) ax ∈ [−1.0, 1.0] ax ∈

<!-- chunk {"id": "body-0108", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

[−1.0, 1.0] ax, ay ∈ [−1.0, 1.0] Not used ax, ay ∈ [−1.0, 1.0] Angular acceleration limit (rad/s2) aω ∈ [−1.0, 1.0] aω ∈ [−1.0, 1.0] Not used aω ∈ [−2.0, 2.0] aω ∈ [−1.0, 1.0] TABLE I: Cross-platform motion models and kinematic limits used in the hardware deployment experiments.

<!-- chunk {"id": "body-0109", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

The hardware experiments use three platforms with distinct motion interfaces and effective footprints, as shown in Fig. 5. The differential-drive dual-arm robot represents a conventional indoor service platform. AgileX Ranger mini is a hybrid 4WS/4WD platform with dual-Ackermann, parallel, and spin-in-place modes, and is used to evaluate the hybrid-mode extension of EXACT-MPPI. The Unitree Go2 quadruped carries a rigid bar that extends its projected footprint, providing a body-velocity deployment case with a task-dependent footprint. Across these platforms, the same collision-evaluation principle is used: observed obstacle points are transformed into the predicted robot body frame and evaluated against an explicit planar effective footprint represented by either a rectangle cover or a simple polygon.

<!-- chunk {"id": "body-0110", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

Shared MPPI Sampling Budget. Unless otherwise stated, the navigation experiments use $K = 1000$ sampled trajectories, $T = 50$ horizon steps, and ${\Deltat} = 0.1$ s, corresponding to a 5 s prediction horizon. The local point cloud is preprocessed and downsampled to $N = 100$ obstacle points before rollout evaluation. Thus, each control cycle evaluates ${KTN} = {5.0 \times 10^{6}}$ point-to-footprint signed-distance queries. In our implementation, this setting occupies approximately 500 MB of GPU memory.

<!-- chunk {"id": "body-0111", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

All platforms are equipped with onboard 2D or 3D LiDAR sensors for local point-cloud acquisition. The weak guidance path is provided to the local planner and transformed into the robot coordinate frame using the available state-estimation or SLAM system, such as Cartographer or FAST-LIO2. The guidance provides high-level directional information, while local collision avoidance and maneuver generation are handled by EXACT-MPPI.

<!-- chunk {"id": "body-0112", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

Evaluation Metrics. We report four task-performance metrics and one clearance-difficulty metric. Task-specific measures, such as path length, are reported only when they are needed to interpret a particular experiment.

<!-- chunk {"id": "body-0113", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

Success rate is the ratio of successful trials to the total number of trials. A trial is counted as successful if the robot reaches the target pose within the prescribed position and heading tolerances, remains collision-free with respect to the observed obstacle set, and completes the task within the predefined time limit. Collision, timeout, or failure to make progress is counted as failure.

<!-- chunk {"id": "body-0114", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

Navigation time is the elapsed time required to complete the navigation task successfully. In simulation, it is measured from the control-loop steps; in real-world experiments, it is recorded from system timestamps.

<!-- chunk {"id": "body-0115", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

Mean speed is the average speed along the executed trajectory, computed over successful trials.

<!-- chunk {"id": "body-0116", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

Path length is the total executed trajectory length. It is reported for experiments where route efficiency is compared in addition to completion time.

<!-- chunk {"id": "body-0117", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

Degree of Narrowness (DoN) quantifies the difficulty of clearance-limited navigation. Following, we define

<!-- chunk {"id": "body-0118", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

where $W_{r}$ is the effective robot width and $W_{p}$ is the minimum passable width of the environment. Larger DoN values indicate tighter passages; as ${DoN}\rightarrow 1$, the available clearance becomes small and footprint modeling becomes more important.

<!-- chunk {"id": "body-0119", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

The effective width depends on the motion model because it is measured relative to the direction of translation. Let $\mathbf{d}$ denote the translation direction and $\mathbf{n}$ an orthogonal unit vector. For a footprint $S \subset {\mathbb{R}}^{2}$, the directional width is

<!-- chunk {"id": "body-0120", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

and $W_{p}$ is measured along the same cross-sectional direction. For Ackermann-steered and differential-drive robots, $\mathbf{d}$ is the forward direction, so $W_{r}$ is the lateral body width. For parallel motion, $\mathbf{d}$ is the sideways direction, so $W_{r}$ is the longitudinal span. For omni-directional motion, we report the minimum directional width over all planar translation directions.

<!-- chunk {"id": "body-0121", "role": "body", "section": "V-A Experimental Design", "weight": 1.0} -->

For concave footprints, this directional width is a coarse scalar measure rather than a complete description of passability. In particular, $W_{r}{(\mathbf{n})}$ is unchanged if $S$ is replaced by its convex hull, since both have the same extrema along direction $\mathbf{n}$. Therefore, DoN is used only to quantify passage tightness; it does not capture the extra feasible configurations that may be available when the planner reasons about the exact concave footprint instead of its convex hull.

<!-- chunk {"id": "body-0122", "role": "body", "section": "V-B Experiment 1: Benchmark the Signed-Distance Evaluator", "weight": 1.0} -->

This experiment evaluates the signed-distance evaluator, which is the dominant geometric operation in the proposed MPPI rollout computation. The goal is to assess runtime, scaling behavior, and deployment overhead rather than distance accuracy, since the analytic distance formulation is described in Sec. IV-C.

<!-- chunk {"id": "body-0123", "role": "body", "section": "V-B Experiment 1: Benchmark the Signed-Distance Evaluator", "weight": 1.0} -->

We compare EXACT-MPPI with the deep unfolded neural encoder (DUNE) from NeuPAN, a recent learning-based method for point-to-robot distance computation. Both methods take obstacle points and robot geometry as inputs and return point-to-robot distance values without constructing an occupancy grid or ESDF. The comparison therefore isolates two different design choices for the distance module: analytic evaluation from an explicit footprint representation versus learned distance approximation.

<!-- chunk {"id": "body-0124", "role": "body", "section": "V-B Experiment 1: Benchmark the Signed-Distance Evaluator", "weight": 1.0} -->

How does analytic signed-distance evaluation compare with DUNE in runtime and scaling behavior?

<!-- chunk {"id": "body-0125", "role": "body", "section": "V-B Experiment 1: Benchmark the Signed-Distance Evaluator", "weight": 1.0} -->

How much does the rectangle-cover specialization accelerate evaluation on rectilinear footprints compared with direct polygon-edge evaluation?

<!-- chunk {"id": "body-0126", "role": "body", "section": "V-B Experiment 1: Benchmark the Signed-Distance Evaluator", "weight": 1.0} -->

What deployment overhead is required when switching footprints or robot platforms?

<!-- chunk {"id": "body-0127", "role": "body", "section": "V-B Experiment 1: Benchmark the Signed-Distance Evaluator", "weight": 1.0} -->

Benchmark setup. All measurements are collected on an Ubuntu workstation with an Intel Core i7-13700F CPU and an NVIDIA GeForce RTX 4060 Ti GPU. For each benchmarked footprint, query points are uniformly sampled from a $50 \times 50$ m region. Unless otherwise stated, per-call inference time is averaged over 50 randomly sampled batches, and EXACT-MPPI and DUNE use identical query batches for fairness. The DUNE models are trained using the default training settings reported for NeuPAN. For Q1, we use four representative footprints: a rectangle, a trapezoid, a sprayer footprint, and a double-sided pruner footprint. For Q2, we use three rectilinear multi-component footprints: L-, T-, and F-shaped bodies.

<!-- chunk {"id": "body-0128", "role": "body", "section": "V-B1 Analytic versus Learned Distance Evaluation (Q1)", "weight": 1.0} -->

Property comparison. Table II ‣ V-B Experiment 1: Benchmark the Signed-Distance Evaluator ‣ V Experiments and Results ‣ EXACT-MPPI: Exact Signed-Distance Navigation for Arbitrary-Footprint Robots from Point Clouds via Path Integral Control") summarizes the structural differences between the two evaluators. DUNE uses a learned surrogate for distance evaluation and requires footprint-specific training or adaptation. In contrast, EXACT-MPPI evaluates distances analytically from an explicit footprint representation. For simple-polygon footprints, the signed distance is computed from point-to-edge distances and an inside--outside test. For rectangle-cover footprints, the exterior distance is exact with respect to the rectangle union, while the interior value is used primarily for collision classification and penalty assignment.

<!-- chunk {"id": "body-0129", "role": "body", "section": "V-B1 Analytic versus Learned Distance Evaluation (Q1)", "weight": 1.0} -->

Runtime comparison. At the representative benchmark size of 100,000 query points, the JAX-batched analytic evaluator is consistently faster than DUNE on the GPU. The measured speedups are $14.0 \times$ for the rectangle, $12.6 \times$ for the trapezoid, $18.9 \times$ for the sprayer footprint, and $16.0 \times$ for the double-sided pruner footprint.

<!-- chunk {"id": "body-0130", "role": "body", "section": "V-B1 Analytic versus Learned Distance Evaluation (Q1)", "weight": 1.0} -->

Scaling with obstacle point count. Figure 6 ‣ V-B Experiment 1: Benchmark the Signed-Distance Evaluator ‣ V Experiments and Results ‣ EXACT-MPPI: Exact Signed-Distance Navigation for Arbitrary-Footprint Robots from Point Clouds via Path Integral Control") reports per-call inference time as the number of query points grows from $10^{2}$ to $10^{6}$. The curves show the mean over 100 trials, with shaded bands denoting one standard deviation. Across the tested range, EXACT-MPPI scales more favorably than DUNE for both simple and multi-part footprints. This behavior is expected because the proposed evaluator uses explicit analytic geometry implemented as tensorized arithmetic and reduction operations, whereas DUNE performs inference through a neural encoder. As the query batch size increases, the neural inference overhead becomes more pronounced, while the analytic evaluator remains well matched to GPU-parallel batched distance computation.

<!-- chunk {"id": "body-0131", "role": "body", "section": "V-B2 Rectangle-Cover versus Polygon Evaluation", "weight": 1.0} -->

For rectilinear footprints, EXACT-MPPI provides a rectangle-cover specialization in addition to the general simple-polygon evaluator. Table III reports per-call GPU runtime on the tested L-, T-, and F-shaped footprints. Under the same benchmark setup, the rectangle-cover path is faster than direct polygon-edge evaluation by $3.25 \times$, $3.34 \times$, and $2.03 \times$, respectively. These results justify using rectangle covers as a computational specialization for rectilinear bodies, while retaining the polygon-edge route for general planar polygonal footprints.

<!-- chunk {"id": "body-0132", "role": "body", "section": "V-B3 Deployment Overhead", "weight": 1.0} -->

The proposed evaluator requires no neural-network training and no precomputed distance field. A new platform requires specifying the footprint representation and motion model, followed by JAX just-in-time compilation at the first execution for the fixed input shape. In our setup, this compilation takes less than 1 s, and subsequent calls reuse the compiled computation. By contrast, DUNE requires a trained distance encoder for the target footprint representation. Under the default settings reported, training takes approximately one hour per footprint. Therefore, when the robot footprint changes substantially, EXACT-MPPI requires only updating the explicit footprint description, whereas the learned distance module requires retraining or adaptation.

<!-- chunk {"id": "body-0133", "role": "body", "section": "V-B3 Deployment Overhead", "weight": 1.0} -->

Experiment 1 shows that the analytic evaluator provides order-of-magnitude GPU speedups over DUNE on the tested footprints, scales consistently with the number of query points, and supports fast deployment by avoiding footprint-specific training. The rectangle-cover specialization further accelerates evaluation on rectilinear footprints by $2.03$--$3.34 \times$ compared with direct polygon-edge evaluation. These results support the use of analytic signed-distance evaluation as a lightweight, training-free distance module for MPPI-based local navigation.

<!-- chunk {"id": "body-0134", "role": "body", "section": "V-C Experiment 2: Clearance-Limited Navigation with Exact versus Convex Footprints", "weight": 1.0} -->

This experiment evaluates the footprint-modeling claim in clearance-limited navigation. The first two test cases isolate the effect of explicit footprint modeling in narrow passages, while the last two test cases evaluate the same principle under mixed static-dynamic obstacle settings. The full setup includes four simulation studies: a differential-drive corridor DoN sweep, an omni-directional narrow-gap benchmark, an IR-SIM dynamic-obstacle corridor benchmark, and a Gazebo dynamic-obstacle comparison.

<!-- chunk {"id": "body-0135", "role": "body", "section": "V-C1 Test Case 1: Differential-Drive Corridor with DoN Sweeps", "weight": 1.0} -->

A differential-drive robot with a T-shaped footprint navigates through a cluttered corridor with varying degrees of narrowness. We create synthetic environments with gap widths tuned to achieve DoN values from 0.6 to 1.0, while keeping the start pose, goal pose, kinematic limits, and overall layout fixed. We compare three methods: (i) EXACT-MPPI with the T-shaped footprint represented explicitly, (ii) Convex-MPPI with the convex hull of the T-shaped footprint, and (iii) NeuPAN with the same convex-hull footprint representation.

<!-- chunk {"id": "body-0136", "role": "body", "section": "V-C1 Test Case 1: Differential-Drive Corridor with DoN Sweeps", "weight": 1.0} -->

For NeuPAN, the DUNE distance encoder is trained for the convex-hull T-shaped footprint. The Learnable Optimization Network (LON) is used to tune the NRMP planner parameters on a representative base case, DoN = 0.9. The tuned NRMP parameters are then kept fixed when evaluating the remaining DoN values. This protocol reflects a deployment-transfer setting in which the footprint-specific distance encoder and planner parameters are prepared once and applied across related environment variations without per-case planner retuning. NeuPAN uses a reference speed of $1.5$ m/s, chosen to be compatible with its typical update frequency of approximately 15 Hz in our setup. For the MPPI-based methods, we use the same linear-velocity limit of $\pm 2$ m/s, but do not include a fixed reference-speed critic; their executed speed is determined by rollout costs and local clearance.

<!-- chunk {"id": "body-0137", "role": "body", "section": "V-C1 Test Case 1: Differential-Drive Corridor with DoN Sweeps", "weight": 1.0} -->

For DoN = 0.6--0.9, all three methods use the same straight-line weak guidance path, and the passage remains feasible under both the explicit T-shaped footprint and its convex hull. For DoN = 1.0, the convex-hull representation removes the remaining feasible passage. We therefore also test this case using an $A^{\ast}$ waypoint path as weak guidance. The $A^{\ast}$ path does not account for the detailed T-shaped footprint geometry. With this guidance, EXACT-MPPI completes the task by exploiting the non-convex free space of the T-shaped footprint, while Convex-MPPI and NeuPAN still fail under their convex-hull footprint representation.

<!-- chunk {"id": "body-0138", "role": "body", "section": "V-C2 Test Case 2: Omni-Directional Gap Scenario", "weight": 1.0} -->

An omni-directional robot with an L-shaped footprint navigates through a narrow-gap environment. The L-shaped footprint has an overall height of 2.0 m, an overall width of 2.0 m, and a uniform leg thickness of 0.4 m. The gap width varies over $\lbrack 1.9,2.0,2.2,2.4\rbrack$ m, producing different DoN values while keeping the start pose, goal pose, and environment layout fixed. Omni-directional motion allows the robot to rotate and translate laterally, so it can align favorable cross-sectional dimensions with the passage constraint.

<!-- chunk {"id": "body-0139", "role": "body", "section": "V-C2 Test Case 2: Omni-Directional Gap Scenario", "weight": 1.0} -->

We compare two methods under the same omni-motion dynamics and MPPI settings: (i) EXACT-MPPI with the L-shaped footprint represented explicitly and (ii) Convex-MPPI with the convex hull of the L-shaped footprint. NeuPAN is not included in this test because the purpose is to isolate footprint modeling under identical omni-directional MPPI dynamics.

<!-- chunk {"id": "body-0140", "role": "body", "section": "V-C2 Test Case 2: Omni-Directional Gap Scenario", "weight": 1.0} -->

Table V summarizes the omni-directional gap scenario across DoN levels. When both methods are feasible, EXACT-MPPI completes the task slightly faster, reducing navigation time by about $5\%$ across the shared feasible cases. At the hardest setting, DoN = 1.05, EXACT-MPPI still succeeds with an average speed of $0.98$ m/s and a navigation time of $20.04$ s, whereas Convex-MPPI fails. These results show that explicit footprint modeling can improve efficiency in moderately tight gaps and extend the feasible operating range when the convex-hull approximation becomes too conservative.

<!-- chunk {"id": "body-0141", "role": "body", "section": "V-C2 Test Case 2: Omni-Directional Gap Scenario", "weight": 1.0} -->

The first two test cases support the core footprint-modeling claim. In the differential-drive corridor sweep, EXACT-MPPI is not uniformly fastest over the shared feasible DoN range: Convex-MPPI is slightly faster at several easier or moderately narrow settings, while EXACT-MPPI gives the shortest time at DoN = 0.7 and is the only method that completes the DoN = 1.0 case. In the omni-directional gap scenario, EXACT-MPPI reduces navigation time in the shared feasible cases and succeeds at the hardest setting where Convex-MPPI fails. The advantage is therefore most pronounced near the feasibility boundary, where convex-hull approximations can remove narrow but valid configurations.

<!-- chunk {"id": "body-0142", "role": "body", "section": "V-C3 Test Case 3: Dynamic-Obstacle Corridor Benchmark", "weight": 1.0} -->

Dynamic testing is included as a supporting study. We evaluate four navigation setups in an 8 m-wide corridor containing mixed static and dynamic obstacles: EXACT-MPPI with the explicit T-shaped footprint, Convex-MPPI with the convex hull of the T-shaped footprint, Rectangle-MPPI with a rectangle-cover approximation of the T-shaped footprint, and NeuPAN with the convex-hull T-shaped footprint. Each method is tested for 50 trials under the same environment configuration, with 2 dynamic obstacles, 8 static obstacles, and concave polygonal obstacle geometry. For guidance, we use a straight-line reference from start to goal. A run is counted as successful only if the robot reaches the goal within a 60 s time limit. Mean navigation time, path length, and speed are reported over successful runs.

<!-- chunk {"id": "body-0143", "role": "body", "section": "V-C3 Test Case 3: Dynamic-Obstacle Corridor Benchmark", "weight": 1.0} -->

For NeuPAN, the DUNE encoder uses the same convex-hull T-shaped footprint as in Test Case 1, and the NRMP parameters are kept from the LON-tuned DoN = 0.9 corridor setting. We do not retune the NRMP parameters for each random obstacle realization. This follows the same deployment-transfer protocol as Test Case 1: the baseline planner is configured on a representative case and then evaluated under related environment variations.

<!-- chunk {"id": "body-0144", "role": "body", "section": "V-C3 Test Case 3: Dynamic-Obstacle Corridor Benchmark", "weight": 1.0} -->

Method Success rate Mean Time (s) Mean Path (m) Mean Speed (m/s) EXACT-MPPI 0.92 44.25 63.62 1.482 Convex-MPPI 0.86 41.79 63.57 1.556 Rectangle-MPPI 0.78 39.66 63.00 1.609 NeuPAN (convex hull) 0.76 42.95 64.05 1.491
TABLE VI: Corridor dynamic-random benchmark (50 trials per method): success rate and mean metrics over successful runs for EXACT-MPPI, Convex-MPPI, Rectangle-MPPI, and NeuPAN with a convex-hull T-shaped footprint.

<!-- chunk {"id": "body-0145", "role": "body", "section": "V-C4 Test Case 4: Gazebo Dynamic-Obstacle Comparison", "weight": 1.0} -->

Following the Gazebo-style dynamic-obstacle setting used in the NeuPAN repository, we construct a corridor benchmark with a differential-drive AgileX Limo carrying a 0.7 m extra load. The effective footprint used by the planner is T-shaped. The environment contains eight static obstacles randomly placed in the corridor and two moving obstacles, as shown in Fig. 10. The moving obstacles follow fixed cross-corridor trails at random speeds below 0.2 m/s. For fairness, EXACT-MPPI and NeuPAN receive the same point-cloud observations and share the same vehicle-kinematics setting. NeuPAN is evaluated using the public implementation from its repository.

<!-- chunk {"id": "body-0146", "role": "body", "section": "V-C4 Test Case 4: Gazebo Dynamic-Obstacle Comparison", "weight": 1.0} -->

For the loaded-Limo footprint, NeuPAN's DUNE distance encoder is trained using the convex hull of the effective T-shaped footprint. The NRMP planner parameters are initialized from the repository's tuned no-load dynamic-obstacle setting and then kept fixed for the added-load evaluation. This setup evaluates a practical add-on deployment scenario: after the robot footprint is changed by an extra load, the footprint-specific distance representation is updated, while the downstream planner configuration is transferred from the existing tuned setting.

<!-- chunk {"id": "body-0147", "role": "body", "section": "V-C4 Test Case 4: Gazebo Dynamic-Obstacle Comparison", "weight": 1.0} -->

We complete 50 Gazebo trials for each method. Table VII summarizes the quantitative comparison between EXACT-MPPI and NeuPAN with a convex-hull T-shaped footprint. In this benchmark, EXACT-MPPI achieves a success rate of $0.96$, compared with $0.65$ for NeuPAN. Over successful runs, EXACT-MPPI also yields lower mean navigation time ($62.47$ s versus $64.47$ s) and shorter mean path length ($25.05$ m versus $26.49$ m), while NeuPAN has a slightly higher mean speed ($0.41$ m/s versus $0.40$ m/s). These results indicate that explicit footprint-aware signed-distance evaluation improves robustness in the setting with the added load while maintaining comparable efficiency on successful trials.

<!-- chunk {"id": "body-0148", "role": "body", "section": "V-C4 Test Case 4: Gazebo Dynamic-Obstacle Comparison", "weight": 1.0} -->

Method Success rate Mean Time (s) Mean Path (m) Mean Speed (m/s) EXACT-MPPI 0.96 62.47 25.05 0.40 NeuPAN (convex hull) 0.65 64.47 26.49 0.41
TABLE VII: Gazebo dynamic-obstacle benchmark (50 trials per method): success rate and mean metrics over successful runs for EXACT-MPPI and NeuPAN with a convex-hull T-shaped footprint.

<!-- chunk {"id": "body-0149", "role": "body", "section": "V-D Experiment 3: Cross-Platform Deployment on Multiple Robot Platforms", "weight": 1.0} -->

This experiment evaluates whether EXACT-MPPI can be deployed across heterogeneous robot platforms with limited platform-specific changes. The study is organized as three real-robot deployment case studies: an indoor differential-drive dual-arm transportation robot, the AgileX Ranger mini hybrid-motion platform, and a Unitree Go2 quadrupedal robot carrying an elongated object. In each case, the same collision-evaluation and MPPI update structure is retained, while the platform-specific motion model, effective-footprint representation, and sensor interface are updated. The goal of this experiment is to assess practical transferability of the framework, rather than to provide a statistically exhaustive benchmark for each platform.

<!-- chunk {"id": "body-0150", "role": "body", "section": "V-D Experiment 3: Cross-Platform Deployment on Multiple Robot Platforms", "weight": 1.0} -->

The cross-platform motion-model and kinematic summary is given in Table I. The AgileX Ranger mini's dual-Ackermann, parallel, and spin modes are listed separately to make the hybrid-motion deployment explicit.

<!-- chunk {"id": "body-0151", "role": "body", "section": "V-D1 Dual-Arm, Differential-Drive Transportation in Indoor Narrow Spaces", "weight": 1.0} -->

We first deploy EXACT-MPPI on a dual-arm, differential-drive robot in an indoor transportation task. This case represents a conventional indoor service platform operating in a clearance-limited office environment. Front and rear 2D laser scanners provide local obstacle observations, and a 2D SLAM system is used to transform the nominal guidance path into the robot coordinate frame.

<!-- chunk {"id": "body-0152", "role": "body", "section": "V-D1 Dual-Arm, Differential-Drive Transportation in Indoor Narrow Spaces", "weight": 1.0} -->

As shown in Fig. 11, the robot passes through a narrow gate, interacts with a pedestrian in a narrow corridor, and enters a tight workspace for bottle placement. The task is completed using the same point-cloud-based collision-evaluation and MPPI control structure as in simulation, with the rollout model adapted to differential-drive kinematics and the footprint specified for this platform. This deployment shows that the proposed collision-evaluation module can be reused on a conventional indoor service robot by updating the platform model and footprint description.

<!-- chunk {"id": "body-0153", "role": "body", "section": "V-D2 AgileX Ranger mini Deployment in a Trap-Like Narrow-Space Scenario", "weight": 1.0} -->

We next deploy EXACT-MPPI on the AgileX Ranger mini platform, which provides a complementary transfer case because it has a different footprint and supports multiple non-skidding motion modes. In this deployment, the footprint representation is replaced by the Ranger mini body geometry, and rollout propagation is matched to the available motion modes. The signed-distance evaluation and MPPI update structure remain unchanged. For the dual-Ackermann rollout model, we use half the axle-axis length as the effective wheelbase parameter.

<!-- chunk {"id": "body-0154", "role": "body", "section": "V-D3 Unitree Go2 with a Carried Bar", "weight": 1.0} -->

Finally, we deploy EXACT-MPPI on a Unitree Go2 quadrupedal robot carrying a rigid bar that extends the projected footprint beyond the nominal body width. This case tests transfer beyond wheeled robots to a legged platform that accepts body-velocity commands from the local planner. EXACT-MPPI uses the Go2 body-velocity interface together with a bar-augmented effective footprint, so the collision-evaluation module reasons about the carried object instead of only the nominal quadruped body.

<!-- chunk {"id": "body-0155", "role": "body", "section": "V-D3 Unitree Go2 with a Carried Bar", "weight": 1.0} -->

We first test the full system in an outdoor garden-like environment with scattered tables, chairs, planters, and other irregular obstacles, as shown in Fig. 14. The robot follows a rectangular guidance path through the unstructured scene while carrying the extra bar. During execution, the local planner corrects the motion by evaluating the bar-augmented footprint against the observed point cloud. This case study evaluates end-to-end transportability of the perception-to-control loop on a legged body-velocity platform operating for the structured indoor layouts.

<!-- chunk {"id": "body-0156", "role": "body", "section": "V-D3 Unitree Go2 with a Carried Bar", "weight": 1.0} -->

We also compare EXACT-MPPI with Falco in the same garden scenario. Falco uses its standard rectangular robot abstraction, while EXACT-MPPI uses the bar-augmented footprint. EXACT-MPPI completes the traversal in $108.96$ s with a traveled distance of $45.72$ m, compared with $114.78$ s and $50.90$ m for Falco. During this comparison, EXACT-MPPI updates at approximately $30$ Hz, while Falco runs at approximately $50$ Hz. This comparison is intended to evaluate the effect of task-dependent footprint reasoning in this deployment case, rather than to isolate update frequency alone.

<!-- chunk {"id": "body-0157", "role": "body", "section": "V-D3 Unitree Go2 with a Carried Bar", "weight": 1.0} -->

We further construct an extreme narrow-passage case to isolate the effect of footprint modeling with the carried bar. As shown in Fig. 17, EXACT-MPPI traverses the passage with the bar-augmented footprint, and the corresponding planning visualization shows a feasible path through the cluttered gap while maintaining explicit bar-aware clearance. Under the same scene, Falco with the rectangular robot abstraction does not complete the passage. This result is consistent with the broader observation that, in clearance-limited real-world navigation, explicit task-dependent footprint reasoning can preserve maneuvers that are lost under simplified footprint abstractions.

<!-- chunk {"id": "body-0158", "role": "body", "section": "V-E Experiment 4: Hybrid-Motion Navigation on AgileX Ranger mini", "weight": 1.0} -->

This experiment evaluates the hybrid-mode extension of EXACT-MPPI on the Ranger mini platform. While Experiment 3 demonstrated cross-platform deployment, this experiment isolates the contribution of multi-mode rollout selection by comparing the full hybrid-mode controller with a dual-Ackermann-only ablation under the same footprint model and environment.

<!-- chunk {"id": "body-0159", "role": "body", "section": "V-E Experiment 4: Hybrid-Motion Navigation on AgileX Ranger mini", "weight": 1.0} -->

Experimental Setup. The test environment contains tight turns, narrow passages, and local recovery regions that require heterogeneous maneuvers. The representative narrow-space scenario has a maximum degree of narrowness of ${DoN} = 0.90$, so the task remains clearance-limited but is traversable with appropriate mode selection. The signed-distance evaluator, footprint representation, obstacle processing, and MPPI cost structure are kept the same for both methods. The only difference is the admissible motion set: the hybrid controller can select among dual-Ackermann, parallel, and spin-in-place modes, whereas the ablation is restricted to dual-Ackermann steering.

<!-- chunk {"id": "body-0160", "role": "body", "section": "V-E Experiment 4: Hybrid-Motion Navigation on AgileX Ranger mini", "weight": 1.0} -->

Ablation Result. In the representative scenario, the dual-Ackermann-only configuration requires $140$ s to complete the task, while the hybrid-mode configuration completes it in $106$ s. This corresponds to an approximately $24\%$ reduction in completion time. The result indicates that access to multiple non-skidding motion modes can enlarge the local maneuver set and reduce unnecessary steering corrections in constrained regions.

<!-- chunk {"id": "body-0161", "role": "body", "section": "V-F Discussion of Experimental Findings and Limitations", "weight": 1.0} -->

The experiments support the central claim that explicit footprint-aware signed-distance evaluation can improve feasibility and robustness in clearance-limited settings. The narrow-passage studies show that convex-hull or simplified footprint models may remove feasible configurations when clearance is tight, even though they can be faster in some less restrictive successful trials. The dynamic-obstacle and hardware case studies indicate that the same collision-evaluation structure can be deployed across different platforms and sensing conditions. At the same time, the results should be interpreted within the scope of the assumptions used in this work.

<!-- chunk {"id": "body-0162", "role": "body", "section": "V-F Discussion of Experimental Findings and Limitations", "weight": 1.0} -->

First, EXACT-MPPI is a local planner that assumes obstacle observations and weak guidance are available from upstream modules. The planner does not address global route generation, semantic scene interpretation, or task-level decision making. In the experiments, the guidance signal is provided as a target pose or simple reference path, and the local planner is responsible for footprint-aware collision avoidance and short-horizon maneuver generation. Integrating the framework with richer perception modules, global planners, or learned navigation priors may improve behavior in more ambiguous scenes, but this system-level integration is outside the scope of the present study.

<!-- chunk {"id": "body-0163", "role": "body", "section": "V-F Discussion of Experimental Findings and Limitations", "weight": 1.0} -->

Second, rollout propagation is based on kinematic models. This choice is appropriate for the low-speed ground-navigation scenarios evaluated here, where the main challenge is local geometric clearance. However, the current validation does not establish dynamic feasibility for high-speed motion, aggressive maneuvers, rough-terrain locomotion, contact-rich legged locomotion, or articulated trailer-like systems. Extending the method to those settings would require replacing the kinematic rollout model with an appropriate dynamic or articulated model and adding stability, actuation, or articulation constraints while preserving the same footprint-aware collision-evaluation principle.

<!-- chunk {"id": "body-0164", "role": "body", "section": "V-F Discussion of Experimental Findings and Limitations", "weight": 1.0} -->

Third, collision evaluation is performed with respect to a planar projected footprint and a preprocessed local point-cloud observation. This is sufficient for the flat-ground scenarios considered in this paper, but it does not model full 3D body geometry, height-dependent clearance, overhanging obstacles, or posture-dependent robot shape. For robots operating in environments where vertical clearance or whole-body configuration matters, the current 2D footprint representation would need to be extended to 3D occupied-volume or configuration-dependent collision reasoning. Whether the same computational advantages carry over to such 3D formulations remains an open direction.

<!-- chunk {"id": "body-0165", "role": "body", "section": "V-F Discussion of Experimental Findings and Limitations", "weight": 1.0} -->

Finally, dynamic obstacles are handled through receding-horizon replanning from updated point-cloud observations, without explicit obstacle-motion prediction. This strategy is effective in the low-speed dynamic-obstacle scenarios tested in this work, but it may be insufficient in dense crowds or fast-changing environments where future obstacle motion must be anticipated. A natural extension is to incorporate time-indexed obstacle predictions into the rollout evaluation, so that the signed-distance cost is evaluated against predicted obstacle positions along the MPPI horizon rather than only the current observation.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper presented EXACT-MPPI, a perception-to-control local navigation framework that evaluates exact signed distances between observed point clouds and arbitrary 2D robot footprints, with motion commands generated directly by a sampling-based MPPI controller. The geometric evaluator handles both convex and concave footprints in a unified manner: orthogonal bodies are evaluated efficiently through a rectangle-cover point-to-box specialization, while general simple polygons are evaluated through analytic point-to-edge signed distance with an inside--outside test. The evaluator and the MPPI rollouts are fused into a single JAX-compiled GPU kernel, batched across rollout samples, horizon steps, obstacle points, and footprint edges, yielding a training-free and map-free local planning pipeline that supports real-time control.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The experiments support three conclusions within the scope considered in this work. First, the analytic signed-distance evaluator is well-matched to batched rollout evaluation on GPU and achieves an order-of-magnitude speedup over a learned point-to-robot distance baseline (Experiment 1). Second, explicit footprint-aware evaluation preserves feasible motion near clearance limits where convex approximations become overly conservative, while not necessarily producing the shortest completion time in every shared feasible setting. Third, the same evaluator transfers across multiple ground-robot platforms -- differential-drive, Ackermann-steering, omnidirectional, and hybrid -- without modification to the core geometric reasoning module. At the same time, the present results validate local navigation in planar settings with static or moderately dynamic obstacles, using kinematic rollout models and projected 2D footprints.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The contribution of this work is therefore best understood as a practical local-navigation framework rather than a complete solution covering perception, motion prediction, and whole-body planning. Future work will pursue tighter integration with higher-level perception and guidance modules, dynamic or articulated rollout models for more complex platforms (e.g., legged systems on rough terrain or articulated trailer-like vehicles), extension from planar footprints to 3D body-clearance reasoning, and explicit obstacle-motion prediction for more dynamic environments.
