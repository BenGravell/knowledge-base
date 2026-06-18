<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

OmniPlanner: Universal Exploration and Inspection Path Planning across Robot Morphologies

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Autonomous robotic systems are increasingly deployed for mapping, monitoring, and inspection in complex and unstructured environments. However, most existing path planning approaches remain domain-specific (i.e., either on air, land, or sea), limiting their scalability and cross-platform applicability. This article presents OmniPlanner, a unified planning framework for autonomous exploration and inspection across aerial, ground, and underwater robots. The method integrates volumetric exploration and viewpoint-based inspection, alongside target reach behaviors within a single modular architecture, complemented by a platform abstraction layer that captures morphology-specific sensing, traversability and motion constraints. This enables the same planning strategy to generalize across distinct mobility domains with minimal retuning. The framework is validated through extensive simulation studies and field deployments in underground mines, industrial facilities, forests, submarine bunkers, and structured outdoor environments. Across these diverse scenarios, OmniPlanner demonstrates robust performance, consistent cross-domain generalization, and improved exploration and inspection efficiency compared to representative state-of-the-art baselines.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Autonomous robotic operation in complex and unstructured environments requires the ability to actively acquire spatial information and systematically observe structures of interest. From underground mines and industrial plants to subsea infrastructures and disaster zones, robots of diverse morphologies are increasingly deployed to perceive, map, and assess their surroundings, potentially without external supervision. These capabilities underpin applications such as search and rescue, infrastructure monitoring, and environmental surveying, where human access is unsafe, impractical, or impossible.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

A large body of prior work has addressed autonomous planning for these tasks, typically by tailoring solutions to specific domains or robot classes. Representative examples include volumetric exploration strategies for aerial robots, traversability-aware planning for ground systems, and coverage-oriented approaches for underwater inspection. While such methods achieve strong performance within their target domains, they are often tightly coupled to assumptions about the robot morphology, including the associated vehicle dynamics, sensing modalities, and environmental structure. Consequently, adapting these planners to new robot types or tasks typically requires substantial redesign, reparameterization, or parallel development of separate planning pipelines. Moreover, exploration and inspection are commonly treated as distinct problems, with limited support for transitioning between them within a unified planning architecture. This fragmentation restricts scalability and limits the transfer of autonomy across diverse robotic platforms.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Despite the apparent diversity of robotic morphologies and domains, many of the underlying planning requirements remain shared. Aerial and underwater robots are both floating-base platforms operating in 3D space. Ground platforms, despite other morphological differences, must simultaneously reason both for obstacle avoidance and traversability over uneven terrain and complex geometries. Across morphologies, robots must repeatedly solve a common set of problems: selecting collision-free motions, reasoning over partially observed environments, and choosing viewpoints that maximize task-relevant information. These shared objectives suggest that autonomy across domains need not rely on fundamentally different planners, but rather on a unified planning core that can be specialized through modular interfaces.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Motivated by these observations, this paper introduces OmniPlanner, a unified planning framework centered around a domain-agnostic planning kernel. The proposed framework decouples the core planning logic from robot-specific constraints, map representations, and task objectives. The planning kernel serves as a shared backbone for global and local planning, while behaviors such as volumetric exploration, visual inspection, and target reach are realized through modular objective functions. Robot-specific characteristics --including aerial, ground, and underwater embodiments-- are incorporated through lightweight adaptation layers, enabling the same planning kernel to be reused across platforms with minimal domain-specific tuning.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Planning Kernel architecture: A unified, domain-agnostic planning kernel that serves as a shared core for global and local planning behaviors across heterogeneous robotic platforms.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Modular behavior integration: A behavior abstraction that unifies volumetric exploration, visual inspection, and target reach within a unified planning framework, enabling a multitude of tasks and the autonomous switching between behaviors without external intervention.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Cross-domain validation: Extensive simulation studies benchmark OmniPlanner against state-of-the-art methods, while experimental field deployments on aerial, ground, and underwater robots demonstrate its effectiveness across diverse environments, including underground mines, forests, submarine bunkers, industrial facilities, and structured outdoor settings.

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The above position OmniPlanner in a distinct category compared to other methods that are limited in their ability to generalize regarding the robot morphologies they can guide and the operational domains (air, land, sea) they can successfully operate. The implementation of the method, alongside the environments used for evaluations in simulation and the datasets from field testing shall be openly released and associated with the paper when it otherwise does not conflict with the rules of double-blind review.

<!-- chunk {"id": "body-0011", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The remainder of this paper is organized as follows. Section 2 reviews related work on exploration, inspection, and unified planning approaches. Section 3 formulates the planning problem and introduces the abstraction used to represent heterogeneous robots and environments. Section 4 details the proposed planning kernel and its associated adaptation layers. Section 5 presents simulation-based evaluations, while Section 6 reports the results of extensive field experiments conducted with aerial, ground, and underwater robots. Finally, Section 7 concludes the paper and discusses directions for future research.

<!-- chunk {"id": "body-0012", "role": "body", "section": "2.A Exploration Planning", "weight": 1.0} -->

Autonomous exploration has been extensively studied under two dominant approaches, the frontier-based exploration and Next-Best-View (NBV) planning. Frontier-based methods select goals on the boundary between known free space and unknown space, originating from the seminal work in and later extended to multi-robot exploration. More recent frontier formulations have focused on enabling rapid exploration for agile aerial robots, e.g., by designing frontier selection strategies that support high-speed flight. Several studies have also compared frontier-based variants to highlight their trade-offs across representative environments and deployment conditions. Exploiting implicit grouping of frontier voxels, the work in improves computational performance.

<!-- chunk {"id": "body-0013", "role": "body", "section": "2.A Exploration Planning", "weight": 1.0} -->

NBV planning instead chooses sensing configurations by optimizing an information objective, and has roots in early work on determining the next best view. NBV principles are broadly applicable across domains, including underwater perception, where view selection must respect sensing and visibility constraints. Modern NBV systems often adopt receding-horizon formulations, such as NBVP, and have been accelerated through sampling-based improvements tailored to Micro Aerial Vehicles (MAV) platforms. A well-known limitation of purely local NBV selection is susceptibility to local minima, where a planner exhausts locally informative viewpoints and fails to relocate to distant informative regions. This limitation is explicitly discussed and addressed in large-scale 3D exploration settings. Simultaneously, approaches such as that rely on sampling-based methods but build a single tree face computational challenges as the scale of the environment increases. Complementary approaches have explored motion-primitive libraries to enable fast, dynamically feasible exploration behaviors. Since many exploration pipelines rely on sampling-based planning, improving sampling efficiency remains an active area, including methods that reduce computational overhead for online informative planning in unknown environments.

<!-- chunk {"id": "body-0014", "role": "body", "section": "2.A Exploration Planning", "weight": 1.0} -->

Recent work has also proposed the ERRT framework, a tree-based next-best-trajectory formulation for 3-D UAV exploration, which explicitly optimizes informative motion over a branching trajectory tree while maintaining real-time feasibility.

<!-- chunk {"id": "body-0015", "role": "body", "section": "2.A Exploration Planning", "weight": 1.0} -->

To mitigate local-minima behavior and improve scalability, hierarchical and integrated exploration planners combine local planning with global reasoning. Representative local--global frameworks include GBPlanner 2.0, TARE, DSVP, and FUEL, which typically maintain global structures (e.g., graphs or frontier sets) to support long-horizon repositioning while using local planners for collision-free execution. More recent works have further targeted global optimality and robustness, e.g., by incorporating frontier-omission awareness and altitude-stratified planning, or by exploiting submap structures to maintain exploration progress under severe odometry drift. In parallel, information-theoretic exploration has advanced through objectives based on mutual information and its tractable approximations, including Bayesian optimization for informative view selection, state-lattice planning with information measures for subterranean environments, and real-time information-theoretic exploration using Gaussian mixture model maps. Exploration in dynamic environments has also been studied, e.g., by leveraging roadmap-style representations that enable efficient re-querying as the environment changes.

<!-- chunk {"id": "body-0016", "role": "body", "section": "2.A Exploration Planning", "weight": 1.0} -->

Finally, learning-based exploration has gained traction, including imitation learning approaches derived from expert behavior in subterranean settings and broader learning-based formulations for adaptive informative path planning. At the systems level, MAexp provides a generic high-efficiency platform for RL-based multi-agent exploration, combining continuous point-cloud environments, multiple MARL algorithms, and faster sampling to support more reproducible cross-scenario evaluation and improved sim-to-real fidelity.

<!-- chunk {"id": "body-0017", "role": "body", "section": "2.A Exploration Planning", "weight": 1.0} -->

A related thread is uncertainty-aware exploration and active Simultaneous Localization and Mapping (SLAM), where the objective is not only map coverage but also improved localization and state estimation. Early active SLAM work framed viewpoint selection through model predictive control and attractor-based exploration, while later approaches incorporated information measures such as Kullback--Leibler divergence to guide exploration under particle-filter SLAM. Active vision has also been used to improve localization quality via controllable sensing, for example through an active stereo head. Uncertainty-aware planners such as RHEMPlanner explicitly consider estimation uncertainty during exploration and mapping, and recent surveys summarize the broader active SLAM landscape and open challenges.

<!-- chunk {"id": "body-0018", "role": "body", "section": "2.B Inspection and Coverage Planning", "weight": 1.0} -->

Inspection and coverage planning differ from exploration in that the objective is typically to observe a known or partially known target surface under sensing constraints, rather than only to expand the free-space map. Classical 3D coverage path planning methods usually assume a prior model and decompose the problem into viewpoint generation and route optimization. An early sampling-based formulation proposed in addresses full-surface inspection in cluttered, occluded environments and provides probabilistic completeness guarantees for coverage planning. A representative online extension is the receding-horizon framework, which offers volumetric exploration and surface inspection, albeit not integrated within a single autonomous mission. Analogous to, the method faces computational challenges in spatially extended missions as it samples a single random tree. In a more inspection-specific setting, ASSCPP uses an existing 3D reference model and sensor noise models to adaptively sample viewpoints toward low-coverage and low-accuracy regions, thereby improving both path efficiency and expected model quality.

<!-- chunk {"id": "body-0019", "role": "body", "section": "2.B Inspection and Coverage Planning", "weight": 1.0} -->

A major challenge in aerial inspection is scalability in large and cluttered 3D scenes. HCPP addresses this through a hierarchical decomposition that partitions the environment into subspaces, computes a global traversal order, and then solves local coverage paths within each subspace. More recently, FC-Planner improves this idea through skeleton-guided space decomposition and specialized viewpoint generation, reducing redundant sampling and yielding faster coverage planning in complex scenes. Beyond geometric coverage alone, recent work has also emphasized visibility and reconstruction quality. Star-convex visibility planning constrains the trajectory to remain within safe-and-visible regions during inspection, while GS-Planner uses 3D Gaussian Splatting to evaluate reconstruction completeness together with geometric and textural quality online, enabling quality-aware active reconstruction.

<!-- chunk {"id": "body-0020", "role": "body", "section": "2.B Inspection and Coverage Planning", "weight": 1.0} -->

Another recent trend is to unify coverage and exploration for online modeling of unknown structures. SEAC departs from the conventional explore-then-exploit pipeline by jointly optimizing local coverage of low-quality surfaces and global exploration of unseen regions within a hierarchical framework, improving both reconstruction quality and efficiency. Practical deployment has also motivated model-informed and cooperative variants, including BIM-supported path planning for building exterior inspection and multi-robot systems for 3-D surface reconstruction. At the evaluation level, CARIC highlights the growing importance of realistic benchmarking for inspection planners, especially in multi-UAV settings, by emphasizing not only completeness and efficiency but also inspection quality under practical constraints such as heterogeneous sensing and communication limits. Overall, the literature shows a clear shift from offline model-based coverage toward scalable, visibility-aware, and quality-driven online inspection planning.

<!-- chunk {"id": "body-0021", "role": "body", "section": "2.C Target Reach Planning", "weight": 1.0} -->

Target-reach planning considers the problem of navigating a robot to a specified goal as quickly and safely as possible, typically in partially known or unknown environments. Recent work has increasingly adopted integrated global--local formulations to balance long-horizon route selection with fast local replanning. FAR Planner is representative of this direction, which incrementally builds a polygonal map and dynamically updates a visibility graph, enabling low-latency "attemptable" routing toward a goal while adapting to newly observed obstacles and dead ends. For aerial robots, FASTER combines global guidance with local trajectory optimization and explicitly maintains a safe backup trajectory in known free space while planning a faster exploratory trajectory toward the goal, improving speed without sacrificing safety.

<!-- chunk {"id": "body-0022", "role": "body", "section": "2.C Target Reach Planning", "weight": 1.0} -->

A closely related line of work targets aggressive goal-reaching in cluttered unknown environments. Bubble Planner improves high-speed local replanning through overlapping sphere corridors and a receding-horizon corridor reuse strategy, increasing replanning success and enabling smooth, dynamically feasible flight. More recently, SUPER extends this safety-assured paradigm by planning directly on LiDAR point clouds and using differentiable trajectory optimization, achieving high-speed and robust waypoint navigation in complex unknown environments. In parallel, perception-driven local planners reduce reliance on explicit mapping by reasoning directly from onboard sensing. For example, depth-conditioned N-MPC embeds a learned collision model into receding-horizon control for real-time obstacle avoidance during waypoint reaching, while reinforcement learning with deep collision encoding maps compressed depth observations, robot state, and goal information directly to low-latency control commands. Overall, recent target-reach methods have shifted toward integrated global--local and perception-aware formulations that better trade off speed, safety, and online adaptability.\

<!-- chunk {"id": "body-0023", "role": "body", "section": "2.C Target Reach Planning", "weight": 1.0} -->

Despite the strong performance of recent exploration, inspection, and target-reach planners, most remain specialized either to a single task or to a specific robot embodiment, sensing stack, and map representation. Exploration methods primarily optimize information gain, inspection methods emphasize surface visibility and coverage quality, and target-reach methods often focus on fast local navigation under behavior-specific assumptions. As a result, transferring these approaches across tasks or platforms typically requires separate implementations, substantial redesign, or extensive retuning. In contrast, our work departs from this fragmented view by introducing a unified, domain-agnostic planning kernel in which volumetric exploration, visual inspection, and target reach are instantiated as modular objectives within the same bifurcated local--global architecture. Coupled with lightweight embodiment adaptation layers, this enables a single planning framework to operate across heterogeneous aerial, ground, and underwater robots.

<!-- chunk {"id": "body-0024", "role": "body", "section": "PROBLEM STATEMENT", "weight": 1.0} -->

This work considers autonomous path planning under partial observability, where information about the environment is acquired through motion while respecting embodiment-specific motion and sensing constraints. The problem is formulated in a domain-agnostic manner to support a unified planning kernel that can be instantiated across heterogeneous robotic platforms and task objectives.

<!-- chunk {"id": "body-0025", "role": "body", "section": "PROBLEM STATEMENT", "weight": 1.0} -->

Let $V \subset {\mathbb{R}}^{3}$ denote a bounded environment volume. The robotic platform is characterized by its embodiment morphology $R_{\mu}$ and associated motion constraints $C_{\mu}$, which define the set of collision-free configurations $\Xi$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "PROBLEM STATEMENT", "weight": 1.0} -->

A configuration ${\mathbf{ξ}} \in \Xi$ is defined as the robot position $\lbrack p^{x},p^{y},p^{z}\rbrack$ and yaw angle $\psi$, and when available, further includes a single rotational degree of freedom corresponding to the pitch angle $\vartheta_{a}$ of an actuated onboard sensor (${\mathbf{ξ}} = {\lbrack p^{x},p^{y},p^{z},\psi\rbrack}$ or ${\mathbf{ξ}} = {\lbrack p^{x},p^{y},p^{z},\psi,\vartheta_{a}\rbrack}$). In this work, a set of onboard sensing modalities $S = {\{ D,C\}}$, corresponding to a depth and a camera sensor (possibly but not necessarily realized on the same device), respectively, are characterized by bounded Field of Views, finite sensing range, and configuration-dependent visibility constraints.

<!-- chunk {"id": "body-0027", "role": "body", "section": "PROBLEM STATEMENT", "weight": 1.0} -->

These properties induce geometric observability relations between robot configurations and environment regions.

<!-- chunk {"id": "body-0028", "role": "body", "section": "PROBLEM STATEMENT", "weight": 1.0} -->

The environment is represented by a spatial map that combines a voxelized Signed Distance Field (SDF) grid $\mathcal{M}$ (also referred to as volumetric map) with fixed resolution $r_{V}$ and (optionally) a $2.5$D grid-based elevation map $\mathcal{H}$ (for ground robots) with fixed resolution $r_{H}$. Each voxel $m \in \mathcal{M}$ encodes the belief state of the corresponding spatial region as free, occupied, or unknown, as well as the distance to the closest surface (referred to as SDF distance). The function $\text{SDF}{(\mathbf{x})}$ returns the SDF distance of the voxel in which $\mathbf{x} \in {\mathbb{R}}^{3}$ lies. This representation supports collision checking, visibility reasoning, and information-theoretic evaluation within the planning process.

<!-- chunk {"id": "body-0029", "role": "body", "section": "PROBLEM STATEMENT", "weight": 1.0} -->

The elevation map $H$ is implemented as a $2.5$D sliding-window map of dimensions $\lbrack d_{h}^{x},d_{h}^{y}\rbrack$, centered at the current robot location. Each grid cell $h \in H$ stores the estimated ground elevation at the corresponding $\lbrack x,y\rbrack$ coordinate. This representation enables traversability-aware planning for ground robots.

<!-- chunk {"id": "body-0030", "role": "body", "section": "PROBLEM STATEMENT", "weight": 1.0} -->

Due to the inherent limitations of range-based and view-constrained sensing, which primarily observe surface boundaries and are subject to occlusions, certain regions of the environment may remain fundamentally unobservable. Let $\Xi_{m}^{\mathcal{D}} \subset \Xi$ denote the set of collision-free configurations from which a voxel $m$ is observable by the depth sensor $\mathcal{D}$. Similarly, let $\Xi_{m}^{\mathcal{C}} \subset \Xi$ denote the set of configurations from which an occupied voxel $m$ is observable by the camera sensor $\mathcal{C}$. Definitions 1 ‣ 3 PROBLEM STATEMENT ‣: Universal Exploration and Inspection Path Planning across Robot Morphologies") and 2 ‣ 3 PROBLEM STATEMENT ‣: Universal Exploration and Inspection Path Planning across Robot Morphologies") capture intrinsic limits of environment observability imposed by the robot's embodiment and sensing modalities.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Problem 1 (Overarching Planning Problem)", "weight": 1.0} -->

Given a bounded environment volume $V$, a robot with configuration space $\Xi$ and motion constraints $C_{\mu}$, and sensing modalities $\mathcal{S}$, determine a collision-free trajectory $\sigma$ that respects all motion and sensing constraints and optimizes an extrinsic objective $\mathcal{J}$ over the environment. As objective we consider target reach or information tasks and specifically exploration and inspection. For the latter two cases, the objective evaluates how effectively the robot's trajectory acquires task-relevant information through sensing, based on a volumetric map representation $\mathcal{M}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Objective 1 (Exploration)", "weight": 1.0} -->

As the exploration objective, the method considers the planning of a path and viewpoints to unveil all possible volume within a defined bounded box, given no prior information and subject to the considered sensing and motion model.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Objective 2 (Inspection)", "weight": 1.0} -->

As the inspection objective, the method considers the planning of a path and viewpoints to enable the coverage of all possible surfaces within a defined bounded box, given a representation of the underlying map (possibly through the exploration step).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Objective 3 (Target Reach)", "weight": 1.0} -->

As the target reach objective, the method considers the planning of a path to reach a user-defined target destination, with or without any prior map information and subject to the considered sensing and motion model.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Objective 3 (Target Reach)", "weight": 1.0} -->

Subsequently, we present how OmniPlanner addresses the considered problem and accordingly gives rise to task-specific autonomous behaviors realized by instantiating different objective functions, constraints, and termination conditions on top of this shared planning kernel, without modifying its underlying structure. Formal definitions for each of OmniPlanner behaviors are also provided.

<!-- chunk {"id": "body-0036", "role": "body", "section": "PROPOSED APPROACH", "weight": 1.0} -->

This section presents OmniPlanner, a unified planning framework, which is structured around a domain- and morphology-agnostic planning kernel. The kernel provides a shared backbone for path planning across heterogeneous robotic platforms, while autonomous behaviors are realized through modular objective functions and feature extensions layered on top of this core, as shown in Fig. 2.

<!-- chunk {"id": "body-0037", "role": "body", "section": "4.A Planning Kernel", "weight": 1.0} -->

The planning kernel operates on the robot configuration space $\Xi$ and an incrementally constructed volumetric map $\mathcal{M}$ and elevation map $H$, independent of task specification and robot embodiment. It adopts a bifurcated planning structure, inspired, composed of tightly coupled local and global planning modules that enable scalable planning in large-scale three-dimensional environments.

<!-- chunk {"id": "body-0038", "role": "body", "section": "4.A.1 Local Planning Module", "weight": 1.0} -->

The local planning module constructs a bounded, sampling-based dense graph ${\mathbb{G}}_{L}$ in a box of dimensions $\mathbf{B}_{L} = {\lbrack b_{L}^{x},b_{L}^{y},b_{L}^{z}\rbrack}$ around the robot's current configuration ${\mathbf{ξ}}_{0}$. The purpose of this graph is to represent the locally reachable subset of the configuration space $\Xi$ under embodiment-specific motion and sensing constraints, while maintaining bounded computational complexity.

<!-- chunk {"id": "body-0039", "role": "body", "section": "4.A.1 Local Planning Module", "weight": 1.0} -->

Given the volumetric map $M$, elevation map $H$, and a bounding box $\mathbf{B}_{R} = {\lbrack b_{R}^{x},b_{R}^{y},b_{R}^{z}\rbrack}$ encoding the robot's physical extent, a set $\Xi_{\mathbf{B}_{L}}$ of collision-free configurations within $\mathbf{B}_{L}$ are randomly sampled.

<!-- chunk {"id": "body-0040", "role": "body", "section": "4.A.1 Local Planning Module", "weight": 1.0} -->

Uniform: Uniform distribution along each axis within $\mathbf{B}_{L}$. This is the most generic distribution that can be used to enable efficient planning in a wide variety of environments.

<!-- chunk {"id": "body-0041", "role": "body", "section": "4.A.1 Local Planning Module", "weight": 1.0} -->

Gaussian: Gaussian distribution centered at ${\mathbf{ξ}}_{0}$ with a user-defined covariance $\mathbf{\Lambda}$. This distribution can enable improved reachability when operating in narrow environments, as the planner samples densely around the robot, at the cost of worse reach in the volume further away.

<!-- chunk {"id": "body-0042", "role": "body", "section": "4.A.1 Local Planning Module", "weight": 1.0} -->

Hybrid: Combination of Uniform and Gaussian. In this distribution, $\eta\%$ samples are sampled using the Gaussian distribution and the rest using Uniform. This creates a balance between operating in narrow environments while maintaining the coverage of the uniform distribution.

<!-- chunk {"id": "body-0043", "role": "body", "section": "4.A.1 Local Planning Module", "weight": 1.0} -->

The samples in $\Xi_{\mathbf{B}_{L}}$ are connected by admissible edges to form the local graph ${\mathbb{G}}_{L}$ along with its vertex and edge sets $V_{L}$, $E_{L}$ respectively. An edge is admissible if it lies entirely in the collision-free part of the volumetric map $M_{free} \subset M$ and respects the robot motion constraints $C_{\mu}$ (further details presented in Section 4.B).

<!-- chunk {"id": "body-0044", "role": "body", "section": "4.A.1 Local Planning Module", "weight": 1.0} -->

Basic: Analogous to, in this method, one robot configuration is sampled and added to ${\mathbb{G}}_{L}$ at a time. Specifically, a random sample ${\mathbf{ξ}}_{r}$ is sampled inside $\mathbf{B}_{L}$ using the selected sampling distribution. The closest vertex $\nu_{c} \in V_{L}$ to ${\mathbf{ξ}}_{r}$ is selected, and if ${\mathbf{ξ}}_{r}$ is further than the maximum allowed edge length $e_{\max}$, ${\mathbf{ξ}}_{r}$ is moved closer to $\nu_{c}$ along the line joining them to create the new vertex $\nu_{r}$. Next, the vertices ${\{\nu_{nb}\}} \in V_{L}$ within a radius $e_{\max}$ of $\nu_{r}$ are connected if the straight line edges are admissible.

<!-- chunk {"id": "body-0045", "role": "body", "section": "4.A.1 Local Planning Module", "weight": 1.0} -->

The process is then repeated until the number of vertices or edges in ${\mathbb{G}}_{L}$ reaches the user-defined limits $n_{\max}^{V},n_{\max}^{E}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "4.A.1 Local Planning Module", "weight": 1.0} -->

Batch: The Batch approach is the newly implemented approach in which the planner samples a batch of $n_{\max}^{V}$ samples at a time. The vertices within a radius of $e_{\max}$ of each other are connected if admissible straight line edges exist. The parts of ${\mathbb{G}}_{L}$ disconnected from the vertex $\nu_{0}$ corresponding to ${\mathbf{ξ}}_{0}$ are pruned. This process is then repeated until the number of vertices or edges in ${\mathbb{G}}_{L}$ reaches the user-defined limits $n_{\max}^{V},n_{\max}^{E}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "4.A.2 Global Planning Module", "weight": 1.0} -->

The global planning module maintains a sparse, incrementally constructed graph ${\mathbb{G}}_{G} = {\{\mathcal{V}_{G},\mathcal{E}_{G}\}}$ that captures the connectivity of the mapped configuration space over time. In contrast to the local planning graph, which is transient and restricted to a bounded planning volume, the global graph persists across planning iterations and grows as the robot moves through previously unmapped regions of the environment.

<!-- chunk {"id": "body-0048", "role": "body", "section": "4.A.2 Global Planning Module", "weight": 1.0} -->

Through this incremental aggregation of locally validated motion structure, the resulting graph remains lightweight while providing a meaningful approximation of the traversable configuration space. It enables efficient long-horizon path queries between arbitrary previously visited configurations, while maintaining bounded memory usage and computational complexity without requiring dense sampling of the entire configuration space. Furthermore, the Global Planning Module keeps track of the robot's endurance to provide safe return to home functionality. In each local planning iteration, the global planner calculates a path $\sigma_{home}$ from the current robot location to the start location $\nu_{home} \in V_{G}$, along ${\mathbb{G}}_{G}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "4.A.2 Global Planning Module", "weight": 1.0} -->

If ${{{len}{(\sigma_{home})}}/v_{nom}} \geq {T_{thr} - t}$, where ${len}{(\sigma)}$ is the length of the path $\sigma$, $v_{nom}$ the nominal commanded speed, $T_{thr}$ the robot's endurance (or mission time limit), $t$ the current time, then the robot is commanded to execute the homing path $\sigma_{home}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "4.A.2 Global Planning Module", "weight": 1.0} -->

To handle potential unseen obstacles or inadmissible segments of the global path $\sigma_{G}$, the Local Planning Module is used to track $\sigma_{G}$. A point $\mathbf{p}_{g}$ at a distance $d_{g}$ from the current robot location ${\mathbf{ξ}}_{0}$ along $\sigma_{G}$ is selected as the goal point. The local graph ${\mathbb{G}}_{L}$ is built, and the set of shortest paths $\Sigma_{L}$ from ${\mathbf{ξ}}_{0}$ is calculated. The path $\sigma_{L} \in \Sigma_{L}$ that takes the robot closest to $\mathbf{p}_{g}$ is selected and commanded to the robot. Upon execution, $\mathbf{p}_{g}$ is updated and the process is repeated until the robot reaches the end of $\sigma_{G}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "4.B Embodiment Adaptation Layer", "weight": 1.0} -->

The embodiment adaptation layer specializes the domain-agnostic planning kernel for different robotic platforms by instantiating primitives and criteria for vertex sampling, collision checking, and edge validation during graph construction, parameterized by the robot morphology $R_{\mu}$, motion constraints $C_{\mu}$, and sensing-limited observability constraints. This design preserves a unified planning kernel while enabling consistent operation across heterogeneous robotic systems. It thus allows one to depart from platform-specific approaches and associated non-generic implementations as. Specifically, OmniPlanner supports multi-rotors, legged robots, differential drive robots, and holonomic underwater robots. Embodiments such as airplanes and non-holonomic ground or underwater robots are not beyond the scope of this work and will be considered for future extensions of the method.

<!-- chunk {"id": "body-0052", "role": "body", "section": "4.B.1 Aerial Robot Adaptation", "weight": 1.0} -->

For aerial robots such as multirotors and other rotorcrafts, graph construction is performed directly in the three-dimensional free space encoded by the volumetric map $\mathcal{M}$. In this embodiment, $C_{\mu}$ does not introduce additional constraints beyond those implied by the platform dynamics at the planning-kernel level. Vertices are sampled from the local planning domain as collision-free configurations ${\mathbf{ξ}} \in \Xi$. A configuration $\mathbf{ξ}$ is accepted if the robot's bounding box $\mathbf{B}_{R}$ is fully contained within the free space $M_{free} \subset M$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "4.B.2 Ground Robot Adaptation", "weight": 1.0} -->

For ground robots such as legged systems, graph construction leverages the elevation map $H$ (built following ) to enforce terrain support and inclination limits in addition to collision avoidance. These requirements define the ground-specific motion constraints $C_{\mu}$. We refer to the elevation-derived portion as $C_{H} \subset C_{\mu}$, which requires valid elevation at the footprint query locations and enforces a maximum slope $\theta_{\max}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "4.B.2 Ground Robot Adaptation", "weight": 1.0} -->

Each candidate sample ${\mathbf{ξ}} \in \Xi$ is projected onto $\mathcal{H}$ by querying the elevation at the footprint center and at a set of offsets corresponding to the footprint corners. If elevation data is unavailable or invalid at any queried location, the sample is rejected. For valid projections, the configuration height is set to $z = {{\mathcal{H}{(x,y)}} + h_{0}}$, where $h_{0}$ is a nominal clearance representing the robot's height. The sample is accepted only if the inclination between the center and corner elevation values does not exceed a maximum allowable slope $\theta_{\max}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "4.B.2 Ground Robot Adaptation", "weight": 1.0} -->

Given two vertices ${{\nu_{i},\nu_{j}} \in V_{k}},{k \in {\{ L,G\}}}$, the candidate edge $e_{ij}$ is evaluated by discretizing the straight-line path between them and projecting each intermediate point onto $\mathcal{H}$. The resulting sequence of projected points defines a ground-consistent polyline ${\hat{\mathbf{γ}}}_{ij}$. The edge is rejected if any projected point lacks valid elevation data or if the incremental slope between successive points exceeds $\theta_{\max}$. If ${\hat{\mathbf{γ}}}_{ij}$ lies in $M_{free}$ (evaluation similar to that for aerial robot), $e_{ij}$ is considered admissible, else rejected.

<!-- chunk {"id": "body-0056", "role": "body", "section": "4.B.3 Underwater Robot Adaptation", "weight": 1.0} -->

For underwater robots such as thruster-based Remote Operated Vehicles, graph construction follows the same kernel mechanism of sampling vertices within a local planning volume and connecting them via feasible edges as that for aerial robots. However, admissibility criteria are adapted to underwater sensing and operational constraints, while $C_{\mu}$ continues to denote motion constraints only.

<!-- chunk {"id": "body-0057", "role": "body", "section": "4.B.3 Underwater Robot Adaptation", "weight": 1.0} -->

A sampled configuration ${\mathbf{ξ}} \in \Xi$ is accepted only if lies in $M_{free}$ and its Euclidean distance to the nearest occupied voxel in $\mathcal{M}_{occ}$ is below a predefined proximity threshold $d_{\max}$. This constraint restricts graph expansion to regions sufficiently close to observed structure, thereby prohibiting the robot from entering open-water volumes.

<!-- chunk {"id": "body-0058", "role": "body", "section": "4.B.3 Underwater Robot Adaptation", "weight": 1.0} -->

Given two vertices ${{\nu_{i},\nu_{j}} \in V_{k}},{k \in {\{ L,G\}}}$, a candidate edge $e_{ij}$ is evaluated by discretizing the straight-line path between them and performing collision checking against $\mathcal{M}$ using the robot bounding volume $\mathbf{B}_{R}$, analogous to the aerial robot.

<!-- chunk {"id": "body-0059", "role": "body", "section": "4.C Behavior Objectives", "weight": 1.0} -->

The planning kernel described in the previous section is task-agnostic and operates solely on the configuration space $\Xi$ and the environment representations $M$ and $H$. Task-specific behaviors are realized by instantiating different objective functions, path evaluation criteria, and termination conditions on top of this shared kernel. Unlike most current planning methods, such as, that present a monolithic architecture for a single behavior, OmniPlanner operates on the common planning kernel which can facilitate multiple behaviors without modifying its underlying planning structure. In this work, three behavior objectives are considered: (i) Volumetric Exploration (VE), (ii) Visual Inspection (VI), and (iii) Target Reach (TR).

<!-- chunk {"id": "body-0060", "role": "body", "section": "4.C.1 Volumetric Exploration (VE) Behavior", "weight": 1.0} -->

1:ξ0 ← GetCurrentConfiguration ⊳ Local Planner
8:else⊳ Global Planner
10: ΣG, home ← GetShortestPaths (ℱ,νhome,𝔾G)
Algorithm 1 Volumetric Exploration (VE) Behavior

<!-- chunk {"id": "body-0061", "role": "body", "section": "4.C.1 Volumetric Exploration (VE) Behavior", "weight": 1.0} -->

The VE behavior instantiates the planning kernel with the objective of incrementally classifying the environment volume using depth sensing $\mathcal{D}$, under the robot's motion and sensing constraints.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Behavior 1 (Volumetric Exploration)", "weight": 1.0} -->

Given a bounded environment volume $V$ and an initial robot configuration ${\mathbf{ξ}}_{init} \in \Xi$, determine a collision-free path $\sigma_{E}$ that enables the classification of the environment into free space $V_{free} \subset V$ and occupied space $V_{occ} \subset V$, based on observations acquired by the depth sensor $\mathcal{D}$. Exploration is considered complete when no further reachable, collision-free configuration exists from which any remaining unclassified portion of the environment can be observed, i.e., ${V_{free} \cup V_{occ}} = {V \smallsetminus V_{res}}$. The generated paths must satisfy the robot's motion constraints $C_{\mu}$ at all times.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Behavior 1 (Volumetric Exploration)", "weight": 1.0} -->

Let ${\mathbb{G}}_{L} = {\{\mathcal{V}_{L},\mathcal{E}_{L}\}}$ denote the local planning graph constructed by the planning kernel, rooted at the current robot configuration ${\mathbf{ξ}}_{0}$. At each planning iteration, the shortest paths $\Sigma_{L}$ are calculated using Dijkstra's algorithm from the root vertex $\nu_{0}$, corresponding to the configuration ${\mathbf{ξ}}_{0}$, to all vertices in the graph.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Behavior 1 (Volumetric Exploration)", "weight": 1.0} -->

For a configuration ${\mathbf{ξ}} \in \Xi$, let $\Gamma_{VE}{({\mathbf{ξ}})}$ denote the volumetric information gain, defined as the number of previously unknown voxels in $\mathcal{M}$ that would become observable by the depth sensor $\mathcal{D}$ if the robot were to be in the configuration $\mathbf{ξ}$, accounting for sensor FoV $\lbrack F_{H}^{\mathcal{D}},F_{V}^{\mathcal{D}}\rbrack$, maximum range $d_{\max}^{\mathcal{D}}$, and visibility constraints.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Behavior 1 (Volumetric Exploration)", "weight": 1.0} -->

where $\lambda_{l}{(\nu_{0},\nu_{k})}$ denotes the path length from the root $\nu_{0}$ to vertex $\nu_{k}$ along ${\mathbb{G}}_{L}$ and $\mu_{l} > 0$ is a distance-based penalty factor. $\lambda_{d}{(\sigma_{L})}$, with the direction-based penalty factor $\mu_{d} > 0$, is a function that penalizes deviation from the current exploration direction similar to. Among all feasible paths $\sigma_{L} \in \Sigma_{L}$ extracted from the local planning graph, the VE behavior selects

<!-- chunk {"id": "body-0066", "role": "body", "section": "Behavior 1 (Volumetric Exploration)", "weight": 1.0} -->

The VE behavior terminates locally when all candidate paths in the local planning graph ${\mathbb{G}}_{L}$ yield negligible cumulative information gain, i.e., when $\sum_{k = 1}^{N}{\Gamma_{VE}{({\mathbf{ξ}}_{k})}}$ is negligible for all $\sigma_{L} \in \Sigma_{L}$, indicating that no further reduction of environmental uncertainty is achievable within the local planning volume (effectiveExploration = False in line 6 of Alg. 1 Behavior ‣ 4.C Behavior Objectives ‣ 4 PROPOSED APPROACH ‣: Universal Exploration and Inspection Path Planning across Robot Morphologies")). In this case, the global planning graph ${\mathbb{G}}_{G}$ is queried to compute a collision-free repositioning path to another previously explored region. This maneuver is called "Global Repositioning".

<!-- chunk {"id": "body-0067", "role": "body", "section": "Behavior 1 (Volumetric Exploration)", "weight": 1.0} -->

In the VE behavior, the global graph maintains a set of vertices $F$ called "frontier" vertices that have $\Gamma_{VE} > \Gamma_{{thr},F}$, where $\Gamma_{{thr},F}$ is the threshold on the volumetric information gain for a vertex to qualify as frontier. When the local exploration is exhausted, the planner repositions the robot to one of the vertices in $F$. To select the best frontier, first, the set $\Sigma_{G,F}$ of the shortest paths from the vertex $\nu_{0,G} \in V_{G}$ corresponding to ${\mathbf{ξ}}_{0}$ to all vertices in $F$ is calculated. Next, the shortest paths $\Sigma_{G,{home}}$ from each vertex in $F$ to the home vertex $\nu_{home}$ are calculated.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Behavior 1 (Volumetric Exploration)", "weight": 1.0} -->

If no frontiers exist in ${\mathbb{G}}_{G}$ the planner concludes that the exploration is completed, a safe path $\sigma_{home}$ from $\nu_{0,G}$ to $\nu_{home}$ is calculated and commanded to the robot.

<!-- chunk {"id": "body-0069", "role": "body", "section": "4.C.2 Visual Inspection (VI) Behavior", "weight": 1.0} -->

5: if dmin𝒞 ≤ SDF (pv) ≤ dmax𝒞 then
8: ξv ← [pvx, pvy, pvz, ψ, ϑa]
Algorithm 2 Visual Inspection (VI) Behavior

<!-- chunk {"id": "body-0070", "role": "body", "section": "4.C.2 Visual Inspection (VI) Behavior", "weight": 1.0} -->

The VI behavior addresses the problem of systematically observing a specified subset of visible surface regions in the environment while respecting camera sensing constraints. The inspection task is formally defined as follows.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Behavior 2 (Visual Inspection)", "weight": 1.0} -->

Given a target surface set $S_{I}$ related to the associated target volumetric map $M_{I} \subset \mathcal{M}_{occ}$ to be inspected, determine a collision-free path $\sigma_{I}$ such that the camera sensor $\mathcal{C}$ observes all elements of $S_{I}$ within its FoV $\lbrack F_{H}^{C},F_{V}^{C}\rbrack$ and effective sensing range $\lbrack d_{\min}^{\mathcal{C}},d_{\max}^{\mathcal{C}}\rbrack$. The inspection process terminates when no collision-free configuration exists from which any remaining unobserved surface region $S_{I} \smallsetminus S_{res}$ can be perceived.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Behavior 2 (Visual Inspection)", "weight": 1.0} -->

To reduce redundancy, the initial viewpoint set $\Xi_{I}$ is reduced to a coverage-optimal subset $\Xi_{I}^{\star}$ using a greedy gain-driven strategy. At each iteration, the viewpoint providing the largest incremental coverage of previously unobserved surface elements is selected. Formally,

<!-- chunk {"id": "body-0073", "role": "body", "section": "Behavior 2 (Visual Inspection)", "weight": 1.0} -->

where ${Vis}{({\mathbf{ξ}})}$ denotes the subset $S_{I}$ visible from configuration $\mathbf{ξ}$ under the sensor constraints.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Behavior 2 (Visual Inspection)", "weight": 1.0} -->

To enable path planning between selected viewpoints, a local planning graph ${\mathbb{G}}_{L}$ is constructed by sampling collision-free configurations within $\mathbf{B}_{VI}$ using the Local Planning Module with $\mathbf{B}_{L} = \mathbf{B}_{VI}$. For each viewpoint ${\mathbf{ξ}}_{v} \in \Xi_{I}^{\star}$, a vertex $\nu_{v}$ is explicitly inserted and connected to nearby vertices of ${\mathbb{G}}_{L}$ via admissible edges forming the set of viewpoint vertices $V_{I}^{\star}$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Behavior 2 (Visual Inspection)", "weight": 1.0} -->

The inspection trajectory is obtained by solving a shortest path problem over ${\mathbb{G}}_{L}$ that visits all viewpoints in $\Xi_{I}^{\star}$. The optimal inspection path

<!-- chunk {"id": "body-0076", "role": "body", "section": "Behavior 2 (Visual Inspection)", "weight": 1.0} -->

where $|\sigma|$ is the number of configurations in $\sigma$ and $d_{l}{({\mathbf{ξ}}_{k},{\mathbf{ξ}}_{k + 1})}$ denotes the path length between successive configurations. The solution is required to satisfy the coverage constraint

<!-- chunk {"id": "body-0077", "role": "body", "section": "Behavior 2 (Visual Inspection)", "weight": 1.0} -->

where ${Vis}{({\mathbf{ξ}}_{k})}$ denotes the surface region visible from ${\mathbf{ξ}}_{k}$ and $S_{res}$ is the residual surface defined in Section 3. The planner calculates $\sigma_{I}^{\star}$ by solving the Traveling Salesman Problem (TSP) to find the ordering between the viewpoints ${\mathbf{ξ}}_{v} \in \Xi_{I}^{\star}$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Behavior 2 (Visual Inspection)", "weight": 1.0} -->

The cost of traveling $d{({\mathbf{ξ}}_{i},{\mathbf{ξ}}_{j})}$ between ${{\mathbf{ξ}}_{i},{\mathbf{ξ}}_{j}} \in \Xi_{I}^{\star}$ is the length of the shortest path between the corresponding vertices ${\nu_{i},\nu_{j}} \in V_{I}^{\star}$ in ${\mathbb{G}}_{L}$. We utilize the Lin-Kernighan-Helsgaun (LKH) heuristic to solve the TSP. The final inspection trajectory is obtained by concatenating the shortest collision-free paths between successive viewpoints along $\sigma_{I}^{\star}$. The inspection behavior terminates when no additional collision-free viewpoints yield positive visual gain, indicating that all observable surface regions have been inspected.

<!-- chunk {"id": "body-0079", "role": "body", "section": "4.C.3 Target Reach (TR) Behavior", "weight": 1.0} -->

2:if ∥pos (ξ0) − pt∥2 ≤ ρreach then
3: return ⌀ ⊳ Target reached
10: return ⌀ ⊳ No frontier to progress
12:σguide ← GetShortestPath (𝔾G,ν0,νbest)
13:plh ← SelectLookaheadPoint (σguide,ρlh)
Algorithm 3 Target Reach (TR) Behavior

<!-- chunk {"id": "body-0080", "role": "body", "section": "4.C.3 Target Reach (TR) Behavior", "weight": 1.0} -->

The TR behavior instantiates the planning kernel with the objective of guiding the robot toward a user-defined target position $\mathbf{p}_{t} \in {\mathbb{R}}^{3}$ (potentially in unknown space), while respecting the robot's motion and sensing constraints. Unlike conventional methods, OmniPlanner is able to reach targets in unknown space in complex, $3$D environments (e.g., Figure 7) due to the bifurcated local-global architecture of the planning kernel.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Behavior 3 (Target Reach)", "weight": 1.0} -->

Given a bounded environment volume $V$, an initial robot configuration ${\mathbf{ξ}}_{init} \in \Xi$, and a predefined target position $\mathbf{p}_{t} \in {\mathbb{R}}^{3}$, determine a collision-free path $\sigma_{T}$ that guides the robot toward the target. The selected path must satisfy the robot's motion constraints $C_{\mu}$ at all times and is chosen such that its terminal configuration minimizes the Euclidean distance to the target. The target reach behavior is considered complete when the robot reaches the target within a predefined tolerance $\rho_{reach}$ or when no further reachable, collision-free configuration exists that reduces the distance to the target.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Behavior 3 (Target Reach)", "weight": 1.0} -->

In the TR behavior, the planner iteratively calculates paths to take the robot closer to the target $\mathbf{p}_{t}$. Let ${\mathbb{G}}_{G} = {\{ V_{G},E_{G}\}}$ be the graph built by the Global Planning Module, and ${\mathbb{G}}_{L} = {\{ V_{L},E_{L}\}}$ be the graph built by the Local Planning Module of the planning kernel in each planning iteration. Similar to the VE behavior, the planner keeps track of the set $F$ of frontier vertices in ${\mathbb{G}}_{G}$ that have the volumetric gain $\Gamma_{VE} > \Gamma_{{thr},F}$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Behavior 3 (Target Reach)", "weight": 1.0} -->

In each planning iteration, the planner selects the best vertex $\nu_{best}$ in ${\mathbb{G}}_{G}$ to advance toward $\mathbf{p}_{t}$, calculates a guiding path $\sigma_{guide}$ towards it, and then computes a collision-free path, using the Local Planning Module, to advance along the guiding path.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Behavior 3 (Target Reach)", "weight": 1.0} -->

More specifically, the planner first checks if $\mathbf{p}_{t}$ is close to the explored space by searching for the closest vertex $\nu_{c}$ to $\mathbf{p}_{t}$ within a distance $\rho_{t}$ in ${\mathbb{G}}_{G}$. If found, $\nu_{best} = \nu_{c}$ and the shortest path from the vertex $\nu_{0}$, corresponding to the current robot configuration ${\mathbf{ξ}}_{0}$, to $\nu_{best}$ along ${\mathbb{G}}_{G}$ is calculated and used as the guiding path $\sigma_{guide}$ to reach $\mathbf{p}_{t}$. If $\nu_{c}$ is not found, then $\mathbf{p}_{t}$ is sufficiently far away from the explored space.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Behavior 3 (Target Reach)", "weight": 1.0} -->

In this case, the planner finds the best frontier vertex in ${\mathbb{G}}_{G}$ to visit to make progress towards the target. For a frontier vertex $\nu_{f}$, let $d_{f}^{l}$ be the shortest path length from $\nu_{0}$ to $\nu_{f}$ along ${\mathbb{G}}_{G}$ and $d_{f}^{u}$ be the Euclidean distance between the position of $\nu_{f}$ and $\mathbf{p}_{t}$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Behavior 3 (Target Reach)", "weight": 1.0} -->

Once the guiding path is calculated, the Local Planning Module is used to calculate a local, collision-free path to reach $\nu_{best}$. First, a lookahead point $\mathbf{p}_{lh}$ on $\sigma_{guide}$ is selected at a distance $\rho_{lh}$ along the path (note that this is the distance along the path, not Euclidean distance between the current robot location and the point on the path). If the target position $\mathbf{p}_{t}$ is within the local planning volume $\mathbf{B}_{L}$, then $\mathbf{p}_{lh} = \mathbf{p}_{t}$. Dijkstra's algorithm is applied to the local planning graph ${\mathbb{G}}_{L}$ to compute the shortest paths $\Sigma_{L}$ from the root configuration ${\mathbf{ξ}}_{0}$ to all vertices in the graph.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Behavior 3 (Target Reach)", "weight": 1.0} -->

where ${\mathbf{ξ}}_{N}$ denotes the final configuration along the path $\sigma_{L}$. Among all feasible paths $\sigma_{L} \in \Sigma_{L}$ extracted from ${\mathbb{G}}_{L}$, the TR behavior selects

<!-- chunk {"id": "body-0088", "role": "body", "section": "Behavior 3 (Target Reach)", "weight": 1.0} -->

The TR behavior terminates when either a) the robot reaches within a user-defined distance $\rho_{reach}$ of $\mathbf{p}_{t}$, b) no frontier exists ($F = \varnothing$), or c) no terminal vertex in $\Sigma_{L}$ takes the robot closer to $\mathbf{p}_{t}$ for $n$ consecutive planning iterations.

<!-- chunk {"id": "body-0089", "role": "body", "section": "SIMULATION STUDIES", "weight": 1.0} -->

This section presents simulation-based validation of the proposed planning framework. We first perform a feature-specific evaluation to qualitatively assess the impact of key design choices in the planning kernel. We then demonstrate the behavior of the complete system in representative simulation scenarios. Finally, we quantitatively compare the proposed framework against state-of-the-art planning methods.

<!-- chunk {"id": "body-0090", "role": "body", "section": "5.A Planning Feature Evaluation", "weight": 1.0} -->

This subsection provides evaluations of individual planning features. The objective of this study is to demonstrate how specific design choices influence the planner's behavior and performance under representative conditions.

<!-- chunk {"id": "body-0091", "role": "body", "section": "5.A.1 Sampling Strategies", "weight": 1.0} -->

The Local Planning Module supports three sampling strategies within the bounded planning volume $\mathbf{B}_{L}$: (i) Uniform, (ii) Gaussian, and (iii) Hybrid. All methods operate within the same $\mathbf{B}_{L}$ and differ only in how candidate configurations are distributed prior to collision checking and graph construction. To analyze their impact on reachable-space representation, we consider a representative T-shaped corridor environment, shown in Fig. 3. This geometry contains narrow passages and branching connectivity. For each strategy, identical sample counts are used, and we record the spatial distribution of valid and rejected samples.

<!-- chunk {"id": "body-0092", "role": "body", "section": "5.A.1 Sampling Strategies", "weight": 1.0} -->

As illustrated in Fig. 3a, Uniform sampling distributes candidate configurations evenly throughout $\mathbf{B}_{L}$. In this environment, many samples fall inside unreachable regions and are rejected during collision checking, while only a sparse subset of valid samples lie within the narrow corridors. This behavior promotes broad coverage in open spaces but reduces efficiency in constrained geometries. Fig. 3b shows that Gaussian sampling concentrates samples around the current robot configuration ${\mathbf{ξ}}_{0}$, resulting in dense clusters of valid samples along nearby corridor segments. This improves local connectivity and increases the probability of discovering feasible motions in narrow passages, but reduces sampling density near distant corridor branches, limiting outward exploration. Hybrid sampling, shown in Fig. 3c, combines both effects by allocating a portion of samples near the robot while preserving uniform coverage across the planning volume.

<!-- chunk {"id": "body-0093", "role": "body", "section": "5.A.2 Graph Construction Strategies", "weight": 1.0} -->

This subsection evaluates the two local graph construction strategies introduced in Section 4.A, namely the Basic incremental construction and the Batch construction methods. Both strategies operate on the same bounded planning volume $\mathbf{B}_{L}$, and differ only in how the collision-free vertices are added and connected during graph generation. To study their effect on reachable-space representation, we consider two representative environments: (i) a multi-room building layout consisting of six interconnected rooms arranged around a central corridor, and (ii) a multi-branch mine topology containing six tunnel branches connected at a junction. For each strategy, experiments are performed with eight different sample counts ranging from $100$ to $800$, each repeated over 20 trials. For every trial, we record the computation time required to build the local graph and the number of distinct reachable regions discovered by the graph (rooms or branches).

<!-- chunk {"id": "body-0094", "role": "body", "section": "5.A.2 Graph Construction Strategies", "weight": 1.0} -->

The curves in Fig. 4 and Fig. 5 report the computation time and the mean number of reachable regions covered by each strategy. The Batch method identifies multiple reachable regions more quickly, particularly at lower computation times, owing to its broader sampling of the planning volume prior to edge pruning. In contrast, the Basic strategy expands incrementally from the current robot configuration, requiring more time to reach distant regions but producing structured graph growth that closely follows feasible corridors. As the number of samples increases, both strategies converge to similar coverage once all reachable regions are discovered. The bottom visualizations in Figs. 4 and 5 show representative local graph instances generated by the two strategies within the same planning volume. These examples illustrate the qualitative difference between the methods: Basic construction produces corridor-following branches that reflect reachable paths, while Batch construction yields denser connectivity and faster region discovery in both multi-room and multi-branch environments.

<!-- chunk {"id": "body-0095", "role": "body", "section": "5.A.3 Camera Sensing Strategies", "weight": 1.0} -->

To assess the impact of camera actuation on the VI behavior, we compare two sensing strategies in a cargo tank inspection scenario (Fig. 6a): (i) a Passive (body-fixed) Camera and (ii) an Active Camera with controllable pitch. Both strategies follow the inspection pipeline described in Section 4.C.2 Behavior ‣ 4.C Behavior Objectives ‣ 4 PROPOSED APPROACH ‣: Universal Exploration and Inspection Path Planning across Robot Morphologies") and differ only in the camera model used to instantiate ${Vis}{( \cdot )}$ and the associated viewpoint orientation set $O_{v}$.

<!-- chunk {"id": "body-0096", "role": "body", "section": "5.A.3 Camera Sensing Strategies", "weight": 1.0} -->

With a passive camera, the sensor is rigidly mounted with a fixed pitch. Consequently, each sampled position $\mathbf{p}_{v}$ admits an orientation set $O_{v}$ that varies only in yaw. This limits the visible surface per viewpoint and typically requires additional viewpoints to mitigate occlusions and unfavorable viewing angles (Fig. 6b). In contrast, the active camera allows pitch actuation, and $O_{v}$ includes feasible yaw--pitch pairs $\psi,\vartheta_{a}$ that satisfy the camera FoV and range constraints. This expands the achievable visibility from the same spatial samples, allowing the greedy selection to cover larger portions of $S_{I}$ with fewer redundant viewpoints and yielding more effective inspection routes (Fig. 6c).

<!-- chunk {"id": "body-0097", "role": "body", "section": "5.A.3 Camera Sensing Strategies", "weight": 1.0} -->

We performed $5$ independent trials per strategy using identical planning budgets and inspection settings. Coverage is reported as the fraction of the target surface observed along the executed inspection trajectory. The passive camera achieves $62.16 \pm {9.01\%}$ coverage, whereas the active camera improves coverage to $88.01 \pm {5.36\%}$. Fig. 6b-6c shows representative trial instances for both strategies.

<!-- chunk {"id": "body-0098", "role": "body", "section": "5.B Simulation Scenarios", "weight": 1.0} -->

We conduct a set of evaluations on aerial, ground, and underwater robots demonstrating the performance of OmniPlanner across morphologies, environments and tasks.

<!-- chunk {"id": "body-0099", "role": "body", "section": "5.B.1 Aerial Robot: Target Reach Behavior", "weight": 1.0} -->

We demonstrate the proposed TR behavior in a cave-like environment using three representative missions (Fig. 7). In all cases, a user-defined target position $\mathbf{p}_{t}$ is specified in initially unknown space. The planner first reasons on the global graph ${\mathbb{G}}_{G}$ to select a guiding point, either a vertex near $\mathbf{p}_{t}$ when it becomes reachable from the explored space, or an intermediate frontier vertex that best advances toward $\mathbf{p}_{t}$ when the target is still far from any explored region. A guiding path $\sigma_{guide}$ is then computed on ${\mathbb{G}}_{G}$, and the local planning module generates collision-free motions by tracking a lookahead point $\mathbf{p}_{lh}$ along $\sigma_{guide}$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "5.B.1 Aerial Robot: Target Reach Behavior", "weight": 1.0} -->

Fig. 7a illustrates Mission 1, where the user-defined target lies outside the currently explored volume but is directly reachable in the sense that progress toward $\mathbf{p}_{t}$ does not require intermediate global repositioning (e.g., detours to alternative branches). The planner expands exploration along the guiding direction until the target becomes reachable and terminates once the robot arrives within the user-defined tolerance $\rho_{reach}$. Fig. 7b shows Mission 2, where the target is indirectly reachable. Although the target lies in free space, continuing along the most direct exploratory route leads into a dead-end branch. The planner therefore navigates to a different frontier to resume progress toward $\mathbf{p}_{t}$, ultimately enabling target reachability. Fig. 7c shows Mission 3, where the target is unreachable from the robot's connected free space.

<!-- chunk {"id": "body-0101", "role": "body", "section": "5.B.1 Aerial Robot: Target Reach Behavior", "weight": 1.0} -->

In this case, the planner advances toward the closest attainable region and terminates when no further collision-free path can reduce the distance to $\mathbf{p}_{t}$, reporting completion once the robot reaches the closest achievable configuration within $\rho_{reach}$ of the target.

<!-- chunk {"id": "body-0102", "role": "body", "section": "5.B.2 Ground Robot: Exploration Behavior", "weight": 1.0} -->

We demonstrate ground robot exploration using OmniPlanner in a large-scale mine tunnel network environment (Fig. 8). The robot operates in initially unknown terrain while incrementally constructing both a volumetric map $\mathcal{M}$ and an elevation map $\mathcal{H}$ used to enforce terrain feasibility constraints. At each planning iteration, the local planning module generates collision-free motions that satisfy terrain inclination and embodiment constraints. In this mission, the robot traverses a total path length of $1260.9$ m over $736.8$ s.

<!-- chunk {"id": "body-0103", "role": "body", "section": "5.B.2 Ground Robot: Exploration Behavior", "weight": 1.0} -->

Fig. 8a shows the full exploration trajectory in a mine environment spanning approximately $220 \times 200$ m. The robot incrementally maps the tunnel network while avoiding untraversable regions identified from elevation data. Representative planning events are highlighted to illustrate how the planner selects feasible frontier directions in branching tunnel structures. The resulting trajectory demonstrates sustained exploration across multiple tunnel segments without entering terrain that violates slope or support constraints.

<!-- chunk {"id": "body-0104", "role": "body", "section": "5.B.2 Ground Robot: Exploration Behavior", "weight": 1.0} -->

Fig. 8b presents selected local planning instances illustrating terrain-aware sampling. Candidate configurations are projected onto the elevation map $\mathcal{H}$, and samples whose projected footprint violates the maximum allowable slope $\theta_{\max}$ or lacks terrain support are rejected. This mechanism prevents the planner from proposing motions across excessively steep or unsupported terrain while maintaining connectivity along feasible corridors.

<!-- chunk {"id": "body-0105", "role": "body", "section": "5.B.2 Ground Robot: Exploration Behavior", "weight": 1.0} -->

Finally, Fig. 8c demonstrates global repositioning and return-to-home behavior. When the time budget runs out, the planner computes a safe homing path along ${\mathbb{G}}_{G}$, allowing the robot to reliably return to the start location through previously validated terrain.

<!-- chunk {"id": "body-0106", "role": "body", "section": "5.B.3 Underwater Robot: Exploration-Inspection Behavior", "weight": 1.0} -->

We demonstrate underwater exploration and inspection using OmniPlanner in a simulated submarine crash-site environment (Fig. 9). The robot operates in initially unknown space while incrementally constructing a volumetric map $\mathcal{M}$ used for collision avoidance and inspection planning. At each planning iteration, the local planning module generates collision-free motions subject to embodiment constraints, while the inspection objective selects informative viewpoints to maximize surface coverage. In this mission, the robot traveled a total path length of $973.9$ m over $1401.9$ s.

<!-- chunk {"id": "body-0107", "role": "body", "section": "5.B.3 Underwater Robot: Exploration-Inspection Behavior", "weight": 1.0} -->

Fig. 9a shows the reconstructed point-cloud map of the crash site from top and side views, along with the executed trajectory. The planner incrementally explores the environment while maintaining proximity to observed structure to satisfy underwater sensing constraints. The resulting trajectory demonstrates sustained exploration across complex geometry without entering large open-water regions.

<!-- chunk {"id": "body-0108", "role": "body", "section": "5.B.3 Underwater Robot: Exploration-Inspection Behavior", "weight": 1.0} -->

Fig. 9b presents representative planning instances. It first illustrates local graph construction within the bounded planning volume, where collision-free configurations are sampled near observed structure and connected through admissible edges to enable safe expansion in cluttered geometry. The same subfigure also shows example instances of the two behaviors considered in this scenario: (i) volumetric exploration, in which the planner selects informative paths to reduce the unseen regions, and (ii) visual inspection, in which the planner selects viewpoints along the structure to maximize surface coverage while respecting sensing range and safety constraints.

<!-- chunk {"id": "body-0109", "role": "body", "section": "5.C Comparison with State-of-the-Art Planning Methods", "weight": 1.0} -->

This subsection compares the proposed planner with state-of-the-art exploration methods for aerial, ground, and underwater robots in simulation, using explored volume over time and aggregate efficiency metrics. Comparison with exploration planning is prioritized due to the prevalence of exploration planning, while in OmniPlanner the inspection behavior has the distinct feature of being able to immediately utilize the online result of exploration.

<!-- chunk {"id": "body-0110", "role": "body", "section": "5.C.1 Simulation Setup", "weight": 1.0} -->

We quantitatively compare the proposed framework against representative state-of-the-art exploration planners. The aerial and ground robot simulations are conducted in the Gazebo Classic simulator, whereas the underwater robot simulations were done in the HoloOcean simulator. For each environment, all methods are initialized from the same robot configuration. A run terminates when the corresponding planner declares mission completion, which may occur due to (i) full environment exploration, (ii) planner failure or deadlock (e.g., getting stuck), or (iii) premature termination despite incomplete exploration.

<!-- chunk {"id": "body-0111", "role": "body", "section": "5.C.1 Simulation Setup", "weight": 1.0} -->

We evaluate performance across multiple simulated environments with increasing structural complexity. For aerial robots, we consider two representative settings: (i) cave environments with single-branch and multi-branch topologies (Fig. 10), and (ii) a ballast water tank environment (Fig. 11). For ground robots, we evaluate in a mine environment consisting of multiple traversable corridors and junctions (Fig. 12). For the underwater robot, we conduct the simulations in a submarine crash site. The parameters used by OmniPlanner are listed in Table 1.

<!-- chunk {"id": "body-0112", "role": "body", "section": "5.C.2 Baselines", "weight": 1.0} -->

We include the following baselines to cover complementary exploration paradigms and to enable comparison against established methods for each embodiment.

<!-- chunk {"id": "body-0113", "role": "body", "section": "5.C.2 Baselines", "weight": 1.0} -->

ERRT: A purely local exploration planner for aerial robots that expands a rapidly-exploring random tree in the robot's reachable space and selects motions based on local information gain. We include ERRT as a representative local-only baseline to assess performance in the absence of explicit global memory or repositioning.

<!-- chunk {"id": "body-0114", "role": "body", "section": "5.C.2 Baselines", "weight": 1.0} -->

GBPlanner 2.0: A hierarchical graph-based exploration planner that couples a local volumetric exploration layer with a global graph used for frontier-based repositioning. We include GBPlanner 2.0 because it is a widely adopted local--global baseline for exploration in complex environments and is closely related in spirit to our graph-based formulation.

<!-- chunk {"id": "body-0115", "role": "body", "section": "5.C.2 Baselines", "weight": 1.0} -->

FUEL: A viewpoint-based aerial robot exploration method that samples candidate viewpoints, evaluates them using a gain--cost utility (expected newly observed volume versus travel cost), and replans online as the map is updated. We include FUEL to compare against a representative utility-driven viewpoint selection strategy that directly balances information gain and motion cost.

<!-- chunk {"id": "body-0116", "role": "body", "section": "5.C.2 Baselines", "weight": 1.0} -->

TARE: A ground-robot exploration framework that integrates local planning with global reasoning and revisit mechanisms to improve long-range progress in large environments. We include TARE as a strong ground-specific baseline that is widely used for autonomous exploration in mine-like settings.

<!-- chunk {"id": "body-0117", "role": "body", "section": "5.C.2 Baselines", "weight": 1.0} -->

DSVP: A ground-robot exploration planner based on decision-space/viewpoint reasoning, designed to improve coverage and navigation efficiency in cluttered environments. We include DSVP to represent an alternative ground exploration formulation that differs from TARE in its planning abstraction and decision-making strategy.

<!-- chunk {"id": "body-0118", "role": "body", "section": "5.C.2 Baselines", "weight": 1.0} -->

NBVP: A receding horizon next-best-view exploration planner. Although the original authors of this method showed results on aerial robots, prominent works have utilized this method for underwater robot exploration as well. Hence, this method is chosen as the baseline among the small set of underwater exploration planning literature.

<!-- chunk {"id": "body-0119", "role": "body", "section": "5.C.3 Aerial Robot Evaluation", "weight": 1.0} -->

Large-scale Environment. We compare OmniPlanner against GBPlanner 2.0 and ERRT to evaluate aerial exploration performance in large-scale cave environments. Experiments are conducted in two settings: (i) a multi-branch cave spanning approximately $520 \times 460$ m and (ii) a single-branch cave spanning approximately $450 \times 290$ m, as shown in Fig. 10. For each environment, all methods are evaluated over $10$ independent trials with identical initial conditions and planning budgets. In this study, a $3$D LiDAR sensor model with ${\lbrack F_{H}^{D},F_{V}^{D}\rbrack} = {\lbrack 360^{\circ},90^{\circ}\rbrack}$ and $d_{\max}^{D} = {20\text{m}}$ was used as the depth sensor.

<!-- chunk {"id": "body-0120", "role": "body", "section": "5.C.3 Aerial Robot Evaluation", "weight": 1.0} -->

To enable a fair comparison with ERRT, which is purely local and does not perform global repositioning, we additionally evaluate the single-branch cave (Fig. 10b), where repositioning is not needed. We summarize exploration efficiency using the area under the explored-volume curve (AUC) and the total exploration time. Relative to ERRT, OmniPlanner increases AUC by $46.90\%$ and reduces the exploration time to $66.25\%$ of ERRT (i.e., $33.75\%$ faster). GBPlanner 2.0 increases AUC by $11.55\%$ and reduces the exploration time to $89.53\%$ of ERRT (i.e., $10.47\%$ faster) as shown in Table 2.

<!-- chunk {"id": "body-0121", "role": "body", "section": "5.C.3 Aerial Robot Evaluation", "weight": 1.0} -->

Confined Environment.We compare OmniPlanner with FUEL, a representative exploration planner for aerial robots, to evaluate performance in confined environments. Experiments are conducted in a custom-designed ballast water tank comprising eight compartments connected via narrow manholes (openings). FUEL is selected as the baseline method due to its high efficiency demonstrated in small-scale environments such as the ballast tank, as opposed to the other baselines (ERRT, GBPlanner2.0), which are geared more towards large-scale settings. The environment spans approximately $80 \times 10$ m and represents a constrained setting with limited maneuvering space and narrow inter-compartment passages. Both planners were deployed from the same starting points with identical planning budgets over five independent trials. In this study, a depth camera sensor model with ${\lbrack F_{H}^{D},F_{V}^{D}\rbrack} = {\lbrack 100^{\circ},70^{\circ}\rbrack}$ and $d_{\max}^{D} = {7.5\text{m}}$ was used as the depth sensor.

<!-- chunk {"id": "body-0122", "role": "body", "section": "5.C.4 Ground Robot Evaluation", "weight": 1.0} -->

We compare OmniPlanner against DSVP and TARE to evaluate ground robot exploration performance in a large-scale mine environment. The environment spans approximately $500 \times 250$ m, as shown in Fig. 12. All methods are evaluated over $5$ independent trials using identical initial conditions and planning budgets. In this study, a $3$D LiDAR sensor model with ${\lbrack F_{H}^{D},F_{V}^{D}\rbrack} = {\lbrack 360^{\circ},90^{\circ}\rbrack}$ and $d_{\max}^{D} = {20\text{m}}$ was used as the depth sensor. To enable fair comparison, the Gazebo Classic-based Autonomous Exploration Development Environment was used for this evaluation.

<!-- chunk {"id": "body-0123", "role": "body", "section": "5.C.5 Underwater Robot Evaluation", "weight": 1.0} -->

We compare Universal exploration and inspection path planner (OmniPlanner) against NBVP, evaluating the underwater exploration performance in a simulation model of an underwater submarine crash site. The environment contains vegetation and a crashed submarine providing additional structures. The environment spans approximately $50 \times 50 \times 25$ m, as shown in Fig. 13. All methods are evaluated over 3 runs, starting at the same location. In this study, a depth camera with ${\lbrack F_{H}^{D},F_{V}^{D}\rbrack} = {\lbrack 90^{\circ},90^{\circ}\rbrack}$ and $d_{\max}^{D} = {10\text{m}}$ was used as the depth sensor.

<!-- chunk {"id": "body-0124", "role": "body", "section": "FIELD EXPERIMENTS", "weight": 1.0} -->

To validate OmniPlanner's ability to autonomously execute the proposed behaviors across heterogeneous robotic morphologies and operating domains, extensive field deployments were conducted on three types of robotic platforms: two aerial robots as described below, one ground robot, and one underwater ROV. Each platform performed fully autonomous missions in its respective environment using the same planning pipeline described in Section 4.

<!-- chunk {"id": "body-0125", "role": "body", "section": "6.A.1 Aerial Robots", "weight": 1.0} -->

The aerial experiments were conducted using two flying robots, called i) Aerial Robot 1 (AR-1) and ii) Aerial Robot 2 (AR-2).

<!-- chunk {"id": "body-0126", "role": "body", "section": "6.A.1 Aerial Robots", "weight": 1.0} -->

AR-1 is a resilient aerial robot designed for autonomous missions in confined and structurally complex environments. The platform is equipped with a collision-tolerant frame measuring $0.38 \times 0.38 \times 0.24$ m (L $\times$ W $\times$ H) and has a total mass of $1.45$ kg, providing an average flight endurance of approximately $10$ minutes. The onboard sensing and compute payload -- hereafter referred to as Autonomy Module 1 (AM-1) -- consists of a Khadas VIM4 single-board computer (SBC) featuring $4 \times 2.2$ GHz Cortex-A73 cores and $4 \times 2.0$ GHz Cortex-A53 cores as the compute unit.

<!-- chunk {"id": "body-0127", "role": "body", "section": "6.A.1 Aerial Robots", "weight": 1.0} -->

The sensing suite of AM-1 includes a VectorNav VN-100 IMU, an Ouster OS0-64 LiDAR (FoV: $\lbrack{360^{\circ} \times 90^{\circ}}\rbrack$, maximum range: $100\ m$), and a Blackfly S RGB camera (FoV: $\lbrack{85^{\circ} \times 64^{\circ}}\rbrack$, resolution: $720 \times 540$ px). The robot runs CompSLAM, a multi-modal simultaneous localization and mapping (SLAM) framework that provides accurate odometry and dense mapping in real time. In addition, the proposed unified path planning pipeline is executed onboard to generate collision-free trajectories, which are subsequently tracked using the model predictive controller (MPC) proposed.

<!-- chunk {"id": "body-0128", "role": "body", "section": "6.A.1 Aerial Robots", "weight": 1.0} -->

AR-2 is a collision-tolerant aerial robot designed for autonomous operation in GPS-denied and confined environments. The platform features a lightweight protective frame measuring approximately $0.52 \times 0.52 \times 0.24$ m (L $\times$ W $\times$ H) and a total mass of $1.47$ kg excluding payload. AR-2's autonomy payload Autonomy Module 2 (AM-2) is equipped with an NVIDIA Jetson Orin NX as the compute module and a multi-modal sensing suite including a RoboSense Airy dome LiDAR (FoV: $\lbrack{360^{\circ} \times 90^{\circ}}\rbrack$, max range: $60\ m$), multiple MIPI cameras, a pmd flexx2 time-of-flight (ToF) camera, a D3 Embedded FMCW radar, and a VectorNav VN-100 IMU. The robot interfaces with a Pixracer flight controller running PX4 firmware, which tracks position and velocity setpoints generated by the onboard autonomy stack.

<!-- chunk {"id": "body-0129", "role": "body", "section": "6.A.1 Aerial Robots", "weight": 1.0} -->

All state estimation, mapping, planning, and control processes are executed fully onboard, enabling robust autonomous flight in perceptually degraded environments.

<!-- chunk {"id": "body-0130", "role": "body", "section": "6.A.2 Ground Robot", "weight": 1.0} -->

The ground experiments were conducted using ANYmal, hereby called Ground Robot 1 (GR-1), a quadruped mobile robot with dimensions of $0.93 \times 0.53 \times 0.80$ m (L $\times$ W $\times$ H), a mass of $50$ kg, and a payload capacity of up to $10$ kg. The platform provides a continuous operational endurance of approximately $1$ hour.

<!-- chunk {"id": "body-0131", "role": "body", "section": "6.A.2 Ground Robot", "weight": 1.0} -->

To demonstrate the generality of the proposed approach across heterogeneous autonomy payloads, three different sensing and computation configurations were evaluated. The first configuration employs the AM-2 as in AR-2, running a LiDAR--radar--inertial odometry pipeline based, which provides accurate and robust state estimation throughout the experiment. The second configuration uses Autonomy Module 3 (AM-3) payload, equipped with an NVIDIA Jetson Orin AGX. Its sensing suite includes an Intel RealSense D455 RGB-D camera, an Ouster OS0-64 LiDAR, and a VectorNav VN-100 IMU. For this configuration, a LiDAR--inertial odometry pipeline based on was employed, similarly providing reliable odometry during deployment. Finally, the third configuration, Autonomy Module 4 (AM-4), consists of the base sensing and compute suite of the ANYmal robot. In AM-4, the onboard computation is handled by two 8th-generation Intel Core i7 CPUs (6 cores each).

<!-- chunk {"id": "body-0132", "role": "body", "section": "6.A.2 Ground Robot", "weight": 1.0} -->

The sensing suite of AM-4 includes a Velodyne VLP-16 LiDAR (FoV: $\lbrack{360^{\circ} \times 30^{\circ}}\rbrack$, maximum range: $100\ m$) and six Intel RealSense depth cameras distributed around the body and primarily used for perception.

<!-- chunk {"id": "body-0133", "role": "body", "section": "6.A.2 Ground Robot", "weight": 1.0} -->

In all configurations, the proposed planning method was executed entirely onboard the payload computer. The generated paths were transmitted to the robot and tracked using GR-1's internal path-tracking controller.

<!-- chunk {"id": "body-0134", "role": "body", "section": "6.A.3 Marsupial Ground-Aerial Robot Team", "weight": 1.0} -->

The marsupial system comprises a heterogeneous ground--aerial robot team consisting of the GR-1 quadruped ground robot carrying the AM-4 payload and the AR-1 aerial robot carrying AM-1 payload operating in a marsupial configuration. The aerial robot is mechanically integrated with the ground platform via a dedicated deployment mechanism that enables secure transport during autonomous ground operation and reliable, controlled detachment. AR-1 is mounted on a rigid, custom-designed interface engineered to withstand ground robot motion while supporting autonomous deployment. Both robots maintain independent onboard computation, sensing, and state estimation pipelines, and communicate over a wireless network to enable bidirectional data exchange when connectivity is available. This design supports coordinated operation while allowing each robot to function autonomously after deployment, with all sensing, computation, and control processes executed fully onboard their respective autonomy modules.

<!-- chunk {"id": "body-0135", "role": "body", "section": "6.A.4 Underwater Robot", "weight": 1.0} -->

The underwater experiments were conducted using an Underwater Robot 1 (UR-1) that is a custom modification of the BlueROV2 Heavy Configuration platform. UR-1 integrates the autonomy payload Autonomy Module 5 (AM-5) consisting of an Alphasense Core Research Development Kit comprising five monochrome Sony IMX-287 global-shutter cameras ($0.4$ MP) rigidly mounted on a common frame (FoV: $\lbrack{126^{\circ} \times 92.4^{\circ}}\rbrack$). The cameras are tightly synchronized with a Bosch BMI085 IMU using a mid-frame, exposure-compensated scheme, achieving sub-100 $\mu$s synchronization accuracy. An NVIDIA Orin AGX compute board is utilized to perform all the computations onboard the robot as part of AM-5, while the high-level commands and telemetry are supported by a tether cable.

<!-- chunk {"id": "body-0136", "role": "body", "section": "6.A.4 Underwater Robot", "weight": 1.0} -->

The robot state estimation is based on ReAqROVIO, a refraction-aware multi-camera visual-inertial odometry (VIO) system, providing real-time state estimation, alongside velocity aiding by proprioceptive method DeepVL, to enable robustness to lack of visual features in the underwater environment. Among the five cameras, two are used as the front-facing stereo camera pair, with stereo matching performed using for geometric 3D perception.\

<!-- chunk {"id": "body-0137", "role": "body", "section": "6.A.4 Underwater Robot", "weight": 1.0} -->

In all robot cases, the proposed unified path-planning framework is also executed onboard the respective autonomy modules to generate motion plans for autonomous operation.

<!-- chunk {"id": "body-0138", "role": "body", "section": "6.B Field Results", "weight": 1.0} -->

Values are reported as 𝔞|𝔟, where 𝔞 corresponds to the aerial robot and 𝔟 corresponds to the ground robot.

<!-- chunk {"id": "body-0139", "role": "body", "section": "6.B Field Results", "weight": 1.0} -->

To provide a structured overview of the conducted field deployments, Table 6 summarizes all field experiments performed across three robotic platforms and operating domains. The table reports, for each field environment, the deployed robot platform, key environment characteristics, executed mission behaviors, and associated mission statistics. The table serves as a reference for the detailed qualitative and quantitative results presented in the following subsections.

<!-- chunk {"id": "body-0140", "role": "body", "section": "6.B.1 Underground Mine", "weight": 1.0} -->

The (abandoned) underground mine environment consists of a narrow, tunnel-like structure characterized by constrained cross-sections, uneven surfaces, and multiple branching corridors. The geometry includes long, winding passages with occasional junctions that lead to side branches of varying lengths and visibility. The environment presents limited line-of-sight, visually-degraded conditions, and restricted maneuvering space.

<!-- chunk {"id": "body-0141", "role": "body", "section": "6.B.1 Underground Mine", "weight": 1.0} -->

Aerial Robot Mission. For the first mission conducted in the underground mine, we deployed the AR-2 aerial robot to explore the environment starting from a designated location inside the mine. The mission was initialized at the starting point indicated in Fig. 14(a), from which the robot began volumetric exploration using the proposed planning framework. At each planning iteration, the planner selected informative exploration paths while accounting for collision constraints imposed by the narrow tunnel geometry. As the exploration progressed, the aerial robot encountered multiple branching corridors. When local exploration within a branch was completed, the global planner triggered repositioning maneuvers to guide the robot toward unexplored branches, as illustrated in Fig. 14(b.1)-(b.2). These repositioning actions enabled systematic coverage of the environment while avoiding previously explored regions. Upon completion of the exploration task, the return-to-home was triggered, and the planner generated a homing path directing the robot back to the starting location, as shown in Fig. 14(b.3). The full three-dimensional map generated during the mission, along with the executed aerial trajectory, is shown in Fig. 14(a).

<!-- chunk {"id": "body-0142", "role": "body", "section": "6.B.1 Underground Mine", "weight": 1.0} -->

The robot traversed a total path length of $168.5$ m over a mission duration of $4.3$ min.

<!-- chunk {"id": "body-0143", "role": "body", "section": "6.B.1 Underground Mine", "weight": 1.0} -->

Ground Robot Mission. For the second mission conducted in the underground mine, we deployed GR-1 with the AM-2 payload. The mission was initiated at the mine entrance, where the robot engaged its volumetric exploration mode. At each planning iteration, the planner selected the most informative path (pink) while accounting for constraints derived from the elevation map and predefined no-go zones. Consequently, the local planning graph did not expand into these restricted areas, as illustrated in Fig. 15(b.1)-(b.2). Upon completion of the exploration task, the return-to-home functionality was triggered, and the global planner generated a homing path (green) for the robot, as shown in Fig. 15(b.3). The complete map generated by the ground platform, alongside its executed trajectory (cyan), is presented in Fig. 15(a). The robot traversed a total path length of $357.7$ m over a mission duration of $19.5$ min.

<!-- chunk {"id": "body-0144", "role": "body", "section": "6.B.2 University Campus", "weight": 1.0} -->

This field experiment was conducted in a large-scale outdoor academic environment including long corridors formed by buildings, narrow pedestrian pathways between structures, and tree-dense regions.

<!-- chunk {"id": "body-0145", "role": "body", "section": "6.B.2 University Campus", "weight": 1.0} -->

Ground Robot Mission. To showcase the realistic and challenging setting for a long-range autonomous exploration, the GR-1 robot was deployed with the sensing and compute payload AM-3. The platform initiated exploration from a designated starting location and incrementally explored the environment by executing the planned paths generated by the proposed planner. Fig. 16(b) highlights three representative planning instances encountered during the mission. Fig. 16(b.1)-(b.2) demonstrate the planner's ability to operate in environments with limited clearance and dense obstacle distributions, successfully generating collision-free paths in both tree-dense regions and narrow passages. Fig. 16(b.3) illustrates a planner's repositioning path that enables the robot to escape a local deadlock and reach unexplored regions. The complete point cloud map produced during the experiment, alongside the executed ground robot trajectory (cyan), is shown in Fig. 16(a). The robot traversed a total path length of $1228.6$ m over a mission duration of $49.5$ min.

<!-- chunk {"id": "body-0146", "role": "body", "section": "6.B.3 Forest", "weight": 1.0} -->

Two field experiments were conducted in forest environments to evaluate the proposed planning framework under different operational settings. Although both experiments were performed in outdoor forested areas, they were carried out at distinct locations with different terrain and vegetation characteristics.

<!-- chunk {"id": "body-0147", "role": "body", "section": "6.B.3 Forest", "weight": 1.0} -->

Marsupial Ground--Aerial Robot Team Mission. The first experiment was conducted in a forest environment featuring uneven terrain and dense vegetation. To address these challenges, a marsupial ground--aerial robot team was deployed, with the aerial robot initially carried by the ground platform. The mission was initiated from a predefined starting location, after which the aerial robot was deployed to assist exploration when the ground robot encountered untraversable terrain. While the ground robot continued exploration along accessible trails, the aerial robot explored regions beyond the reach of the ground platform. Fig. 17(a) illustrates the resulting collaborative exploration outcome, showing the trajectories executed by the ground robot (cyan) and the aerial robot (red), along with the fused point cloud map generated during the mission. Regrouping events were initiated when the remaining time budget became limited, allowing the robots to reestablish coordination. The aerial robot deployment process is shown in Fig. 17(b), while representative planning instances for both robots are presented in Fig. 17(c.1)-(c.2), highlighting the planners' ability to generate collision-free and terrain-aware paths in cluttered forest conditions.

<!-- chunk {"id": "body-0148", "role": "body", "section": "6.B.3 Forest", "weight": 1.0} -->

The GR-1 and AR-1 robots traversed total path lengths of $310.8$ m and $91.3$ m, respectively, over mission durations of $13.9$ min and $2.5$ min.

<!-- chunk {"id": "body-0149", "role": "body", "section": "6.B.3 Forest", "weight": 1.0} -->

Aerial Robot Mission. The second experiment was conducted in a different forest environment characterized by tall trees, dense canopy coverage, and cluttered three-dimensional vegetation structures. This setting emphasizes aerial navigation challenges such as limited free space, reduced visibility, and complex obstacle distributions. In this experiment, the AR-1 aerial robot was deployed, and the TR behavior was tested. The mission was initialized at a predefined starting location, from which a sequence of spatial target goals was specified within the forested area. At each planning iteration, the planner generated collision-free trajectories toward the current target goal while accounting for surrounding vegetation and previously mapped obstacles. Upon reaching a target, the planner transitioned to the next goal in the sequence, enabling structured coverage of the environment, as shown in Fig. 18(a). Key planning instances are illustrated in Fig. 18(b.1)-(b.2), demonstrating the planner's ability to adaptively generate feasible paths in densely cluttered environments. After completing the target sequence, the return-to-home behavior was triggered, and the planner generated a homing trajectory guiding the aerial robot back to the starting location, as depicted in Fig. 18(b.3).

<!-- chunk {"id": "body-0150", "role": "body", "section": "6.B.3 Forest", "weight": 1.0} -->

The robot traversed a total path length of $129.8$ m over a mission duration of $5.1$ min.

<!-- chunk {"id": "body-0151", "role": "body", "section": "6.B.4 Ballast Water Tank", "weight": 1.0} -->

This field experiment was conducted in a confined industrial environment consisting of interconnected ballast water tank compartments with narrow passages and complex internal geometry.

<!-- chunk {"id": "body-0152", "role": "body", "section": "6.B.4 Ballast Water Tank", "weight": 1.0} -->

Aerial Robot Mission. To evaluate both the proposed exploration and inspection behaviors under these conditions, the AR-1 aerial robot was deployed to perform a fully autonomous mission inside the tank structure. The mission began from a designated entry point, after which the robot autonomously explored the interior volume while incrementally building a three-dimensional map of the environment, followed by visual inspection of the mapped surfaces. Fig. 19(a) presents the final point cloud map generated during the mission together with the executed aerial robot trajectory. The robot navigated through multiple compartments and traversed a narrow opening to access adjacent sections of the tank before reaching the designated end point. Fig. 19(b) illustrates representative planning instances corresponding to different autonomous behaviors executed during the mission. These include volumetric exploration for map coverage, visual inspection for close-range sensing of structural elements, and opening traversal for navigating through constrained passages. The robot traversed a total path length of $45.1$ m over a mission duration of $4.2$ min.

<!-- chunk {"id": "body-0153", "role": "body", "section": "6.B.5 Submarine Bunker", "weight": 1.0} -->

The experiments were conducted in a submarine bunker environment. The water exhibited low visibility, resulting in perceptually degraded conditions that challenge both state estimation and collision-aware planning.

<!-- chunk {"id": "body-0154", "role": "body", "section": "6.B.5 Submarine Bunker", "weight": 1.0} -->

Underwater Robot Mission. Two missions were conducted using the UR-1 underwater robot to evaluate the proposed framework under different operational objectives: an exploration-only mission and an exploration--inspection mission. In both cases, the robot was deployed from a predefined starting location and initialized in VE mode. At each planning iteration, the local planning graph was constructed by sampling vertices in close proximity to the surrounding structure, biasing exploration toward the infrastructure of interest and preventing expansion into open-water regions, while still enforcing collision constraints.

<!-- chunk {"id": "body-0155", "role": "body", "section": "6.B.5 Submarine Bunker", "weight": 1.0} -->

In the exploration-only mission, the robot autonomously explored the environment and generated a three-dimensional point cloud map, as shown in Fig. 20(a). After completing the exploration task, the return-to-home was triggered, and the planner generated a homing path guiding the robot back to the deployment location. Representative planning instances for this mission are shown in Fig. 20(c.1)-(c.2). The robot traversed a total path length of $238.9$ m over a mission duration of $13.9$ min.

<!-- chunk {"id": "body-0156", "role": "body", "section": "6.B.5 Submarine Bunker", "weight": 1.0} -->

In the exploration--inspection mission, volumetric exploration was followed by visual inspection of the mapped surface. The planner generated an inspection path to obtain detailed observations of structural elements, as shown in Fig. 20(b). Since the VE behavior in this mission was similar to that of the exploration-only mission, only the VI behavior is illustrated. After completing the inspection task, the robot autonomously returned to the starting location. Representative planning instances for this mission are shown in Fig. 20(c.3)-(c.4). The robot traversed a total path length of $156.3$ m over a mission duration of $8.2$ min.

<!-- chunk {"id": "body-0157", "role": "body", "section": "6.C Summary", "weight": 1.0} -->

We conducted eight field deployments in diverse and challenging environments to evaluate the robustness and generality of the proposed unified planning framework across robot morphologies. In all deployments, the method was executed fully onboard and operated autonomously without human intervention throughout mission execution. Across these scenarios, the planner consistently demonstrated robust performance in environments characterized by limited clearance, dense obstacles, uneven terrain, and confined spaces. The results indicate effective long-range exploration, coordinated multi-robot operation with regrouping events, and reliable execution of volumetric exploration, visual inspection, and target reach behaviors. Collectively, these deployments confirm the field readiness and broad applicability of the proposed framework across heterogeneous platforms and operational domains.

<!-- chunk {"id": "body-0158", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

This paper presented OmniPlanner, a unified planning framework built around a domain-agnostic planning kernel for autonomous exploration, inspection, and target reach across heterogeneous robotic platforms. By decoupling core planning from embodiment-specific constraints through adaptation layers, the same planning structure can be applied across aerial, ground, and underwater robots.

<!-- chunk {"id": "body-0159", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

Simulation and field results showed that the proposed framework achieves strong performance across diverse environments and tasks, while maintaining fully onboard autonomous operation in challenging real-world deployments. The results support the effectiveness and practical generality of the proposed unified planning approach across diverse robot morphologies.

<!-- chunk {"id": "body-0160", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

Future work will focus on extending OmniPlanner to an increased diversity of morphologies, including non-holonomic platforms (e.g., fixed-wing aerial vehicles, car-like robots, and autonomous underwater vehicles), broadening the applicability of the framework to a wider range of systems. Similarly, future work will also focus on correlating perception uncertainty with the sampling of informative viewpoints.
