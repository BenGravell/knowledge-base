<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

BOWConnect: Parallel Bayesian Optimization over Windows with Learned Local Cost Maps for Sample-Efficient Kinodynamic Motion Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents BOWConnect, a bidirectional parallel kinodynamic motion planner that addresses three fundamental limitations of existing sampling-based methods: sample inefficiency in high-dimensional state spaces, unreliable cost heuristics under dynamic constraints, and poor performance in narrow passage environments. Unlike classical planners that rely on random control sampling and geometric distance heuristics, BOWConnect integrates Bayesian Optimization over Windows (BOW) as a learning-based steering function within a parallel tree-based exploration framework, enabling each worker to learn local cost maps and constraints to guide sampling toward dynamically feasible and collision-free controls. A bidirectional architecture simultaneously grows forward and backward trees from the start and goal regions in parallel threads, with a spatial hashing mechanism enabling fast connection queries and a boundary value problem solver generating kinodynamically consistent bridge trajectories. Extensive evaluations across ten benchmark environments demonstrate that BOWConnect achieves 100\% success while delivering the fastest or near-fastest planning time in complex scenarios, including narrow passages and non-convex spaces where state-of-the-art planners fail or degrade substantially.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Real-world deployment on a ground vehicle and a quadrotor confirms real-time planning with no collisions. Videos of real-world and simulated experiments, high-resolution versions of the figures, and the open-source code are available at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Kinodynamic motion planning remains a fundamental challenge in robotics because the relevant search space is the system *state space*, which is typically higher-dimensional than configuration space due to the inclusion of configuration variables and their derivatives (e.g., velocities and higher-order derivatives). This dimensionality makes sampling-based exploration susceptible to the curse of dimensionality and slow convergence.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Beyond dimensionality, kinodynamic planning must satisfy differential constraints throughout the trajectory, meaning geometrically collision-free paths may still be dynamically infeasible. For many systems, an exact steering function is difficult or impractical to derive, so planners typically generate motion by sampling controls and forward-propagating the dynamics rather than by simple interpolation. Guiding this search is equally difficult: existing methods often rely on Euclidean distance heuristics for candidate selection because estimating transition costs under dynamics is non-trivial, though learning-based approaches have recently been proposed to address this limitation. These challenges compound further in highly constrained environments such as narrow passages, where generating dynamically feasible connections through constrained regions is particularly demanding.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Parallelism has improved performance for geometric planners such as RRT-Connect through GPU-parallel expansion and collision checking, but kinodynamic planners have historically been harder to parallelize due to propagation-dominated, serial computation patterns. This has motivated recent work that explicitly restructures kinodynamic tree growth for massively parallel devices, yet scalable bidirectional kinodynamic planning with efficient connection discovery remains an open problem.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we present BOWConnect, a bidirectional and parallel kinodynamic motion planner designed to improve sample efficiency and accelerate connection discovery in continuous state spaces. BOWConnect grows two trees simultaneously from the start and goal, using an online learning-based trajectory generator to produce collision-free, kinodynamically feasible motions directly in continuous state and control spaces. A spatial hashing mechanism embedded in the MotionTree data structure enables efficient multi-stage feasibility verification, reducing redundant propagation and accelerating connection queries between the two trees. Together, these components improve computational efficiency while maintaining trajectory feasibility across diverse robotic platforms, as demonstrated through experiments on ground and aerial vehicles.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main contributions of this work are: An online learning-based method for generating collision-free, kinodynamically feasible trajectories directly in continuous state and control spaces.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

A bidirectional parallel planning architecture that enhances global connectivity while preserving local trajectory quality.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A spatial hashing mechanism within the MotionTree data structure that enables efficient multi-stage feasibility verification.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Extensive experimental validation on ground vehicles with unicycle and bicycle models, and aerial vehicles with quadrotor dynamics.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Let $\mathcal{C}$ be the robot configuration space, modeled as an $n$-dimensional smooth manifold. Let $\mathcal{C}_{\text{free}}\subset\mathcal{C}$ denote the open subset of configurations in which the robot does not intersect any obstacle. The kinodynamic planning problem extends beyond geometric path planning by incorporating the robot's dynamics. Let $\mathbf{x}=(q,\dot{q})\in\mathcal{X}$ be the $2n$-dimensional state vector, where $\mathcal{X}=T\mathcal{C}$ is the tangent bundle of $\mathcal{C}$. The feasible state space is defined as: The system dynamics are governed by the ordinary differential equation $\dot{\mathbf{x}}=f(\mathbf{x},\mathbf{u})$, where $\mathbf{u}\in\mathcal{U}\subset\mathbb{R}^{m}$ is a control input drawn from a compact action set.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

For a candidate control $\mathbf{u}$, the system dynamics are integrated, e.g.,

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem 1 (Kinodynamic Planning)", "weight": 1.0} -->

Given initial and goal states $\mathbf{x}_{I},\mathbf{x}_{G}\in\mathcal{X}_{\text{free}}$, find a control sequence $\mathbf{u}:[0,t_{F}]\rightarrow\mathcal{U}$ such that the resulting trajectory $\tau(\mathbf{u})=\Phi(\mathbf{x}_{I},\mathbf{u})$ satisfies: When time-optimality is required, $t_{F}$ is minimized over all feasible solutions.

<!-- chunk {"id": "body-0015", "role": "body", "section": "BOWConnect Algorithm", "weight": 1.0} -->

0: Initial state xstart, goal position pgoal, sampling radius rgoal, number of workers N, time budget Tmax 0: Kinodynamic trajectory τ or failure 1: 𝒮← SampleStates(xstart, rgoal, N) 2: 𝒢← SampleStates(pgoal, rgoal, N) 4: Launch forward worker Wf[i]: 𝒮[i] → 𝒢[i] 5: Launch backward worker Wb[i + 1]: 𝒢[i + 1] → 𝒮[i + 1] 7: while time elapsed < Tmax do 8: for each forward state xf and backward state xb do 9: if xb nearby xf via spatial hash and IsKinematicallyFeasible(xf, xb) then 12: return (true, MergeTrees(wf, τbridge, wb)) 16: if any worker reached pgoal then 17: return unidirectional solution Algorithm 1 BOWConnect Algorithm The algorithmic steps of BOWConnect are outlined in Alg. 1. The core idea is to leverage multiple independent BOW planner instances within a tree-based exploration framework.

<!-- chunk {"id": "body-0016", "role": "body", "section": "BOWConnect Algorithm", "weight": 1.0} -->

Unlike traditional bidirectional planners that grow a single forward and backward tree, BOWConnect spawns $N/2$ forward workers and $N/2$ backward workers, each maintaining its own search tree and BOW instance. This high-level parallelism enables diverse exploration patterns while preserving the kinodynamic feasibility guarantees of the underlying BOW planner.

<!-- chunk {"id": "body-0017", "role": "body", "section": "BOWConnect Algorithm", "weight": 1.0} -->

Given an initial state $\mathbf{x}_{\text{start}}\in\mathbb{R}^{n}$ and goal position $\mathbf{p}_{\text{goal}}\in\mathbb{R}^{d}$, BOWConnect first samples multiple initial configurations around both regions. Specifically, it generates collision-free start states $\mathcal{S}=\{\mathbf{x}_{1},\ldots,\mathbf{x}_{N}\}$ and goal states $\mathcal{G}=\{\mathbf{x}^{\prime}_{1},\ldots,\mathbf{x}^{\prime}_{N}\}$ by sampling uniformly within radius $r_{\text{goal}}$ of the respective centers. Each sampled state includes a random heading $\theta\in[-\pi,\pi]$, enabling workers to explore from different initial orientations. This sampling strategy addresses heading ambiguity at the goal and provides diversified exploration directions, significantly improving connection probability between trees.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-A Tree Growth with Constrained Bayesian Optimization", "weight": 1.0} -->

Fig. 1: Parallel motion tree growth of BOW-Connect in a cluttered planar environment. Trees are initialized from the start (green) and goal (red) regions and extended in separate threads using the BOW planner. Grey trajectories depict sampled short-horizon trajectories and the bold blue curve indicates the final connected path. A successful bidirectional connection via boundary value problem solution is highlighted in cyan.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Tree Growth with Constrained Bayesian Optimization", "weight": 1.0} -->

The BOW planner formulates local planning as a constrained Bayesian Optimization problem over the control space $\mathcal{U}\subset\mathbb{R}^{m}$, where the dimension $m$ depends on the robot type. For each candidate control $\mathbf{u}$, BOW uses a robot-specific motion model to simulate forward trajectory through numerical integration. The motion model captures the system dynamics via ordinary differential equations $\dot{\mathbf{x}}=f(\mathbf{x},\mathbf{u})$, which are integrated using fourth-order Runge-Kutta to obtain the predicted trajectory $\tau(\mathbf{u})$ over a finite time horizon $T$. For each simulated trajectory, BOW evaluates two functions: a reward and a constraint satisfaction indicator. The reward is defined as the negative distance to the local target for collision-free trajectories: where $\mathbf{p}(T)$ represents the position component of the predicted state after time horizon $T$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A Tree Growth with Constrained Bayesian Optimization", "weight": 1.0} -->

The constraint function returns 1 if the entire trajectory avoids obstacles and 0 otherwise: BOW learns two separate Gaussian Process models: one for the reward $\mathcal{GP}_{r}$ and one for the constraint $\mathcal{GP}_{c}$. These models provide mean predictions $\mu_{r}(\mathbf{u})$, $\mu_{c}(\mathbf{u})$ and uncertainties $\sigma_{r}^{2}(\mathbf{u})$, $\sigma_{c}^{2}(\mathbf{u})$ respectively. The acquisition function balances exploration and exploitation while respecting collision constraints through the probability of feasibility: where $\Phi$ is the standard normal cumulative distribution function.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-A Tree Growth with Constrained Bayesian Optimization", "weight": 1.0} -->

The next control to evaluate is selected by optimizing the constrained acquisition function $\alpha(\mathbf{u})=[\mu_{r}(\mathbf{u})-\kappa\sigma_{r}(\mathbf{u})]\times P_{\text{feas}}(\mathbf{u})$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A Tree Growth with Constrained Bayesian Optimization", "weight": 1.0} -->

A key property of this formulation is its learning behavior in narrow passages. When the reward function in Eqn. drives the robot toward a region that is largely infeasible, constraint violations inflate $P_{\text{feas}}$ penalties, causing the feasibility term to dominate $\alpha(\mathbf{u})$ and redirecting the search toward collision-free controls in free space. This mechanism prevents BOW from becoming trapped in local minima induced by inadmissible costs within the planning horizon $T$. When BOW successfully produces a collision-free trajectory $\tau=[\mathbf{x}_{\text{near}},\mathbf{x}_{1},\ldots,\mathbf{x}_{m}]$, all states are appended sequentially to the tree. Kinodynamic feasibility is guaranteed by construction, as the motion model integration inherently respects velocity, acceleration, and curvature limits. Combined with parallel tree growth across multiple workers, this property gives BOW-Connect space exploration characteristics akin to those of global planners.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B Connection Detection and BVP Solving", "weight": 1.0} -->

While workers grow their trees independently, the main thread periodically checks for potential connections between forward and backward trees. To enable efficient connection queries, BOWConnect employs spatial hashing through the MotionTree structure. Each state $\mathbf{x}$ is mapped to a discrete grid cell via the hash function: where $\Delta$ is the grid resolution and $\oplus$ denotes bit-packing operations. This allows $\mathcal{O}$ average-case lookup to determine if a forward tree state has nearby backward tree states.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Connection Detection and BVP Solving", "weight": 1.0} -->

When a potential connection is detected, BOWConnect performs a multi-stage verification. First, it checks kinematic feasibility by ensuring the required heading change and travel distance are within vehicle constraints. Specifically, given two states $\mathbf{x}_{f}$ and $\mathbf{x}_{b}$ belonging to the forward tree $\mathcal{T}_{I}$ and backward tree $\mathcal{T}_{G}$ respectively, the connection is kinematically feasible if: where $\theta_{\text{req}}=\arctan 2(y_{b}-y_{f},x_{b}-x_{f})$ is the required heading and $\mathbf{p}(t)$ denotes the position component of $\mathbf{x}(t)$ at time $t$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B Connection Detection and BVP Solving", "weight": 1.0} -->

If kinematically feasible, BOWConnect solves a Boundary Value Problem (BVP) to generate the connecting trajectory. The BVP seeks a control $\mathbf{u}_{c}:[0,t_{c}]\rightarrow\mathcal{U}$ such that the connecting trajectory $\tau(\mathbf{u}_{c})=\Phi(\mathbf{x}_{f},\mathbf{u}_{c})$ satisfies: The BVP solver employs proportional control to smoothly transition between states while respecting kinodynamic constraints.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B Connection Detection and BVP Solving", "weight": 1.0} -->

Starting from $\mathbf{x}_{f}$, it iteratively computes the heading error $\Delta\theta=\theta_{\text{desired}}-\theta_{\text{current}}$ and applies yaw rate $\omega=\text{clamp}(k_{p}\Delta\theta/\Delta t,-\omega_{\max},\omega_{\max})$ while moving toward $\mathbf{x}_{b}$ with speed proportional to remaining distance. The resulting trajectory undergoes collision checking before acceptance. If multiple connections are found, BOWConnect selects the one with minimum Euclidean distance, as shorter connections are more reliable and easier to verify.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-C Solution Extraction and Fallback Mechanisms", "weight": 1.0} -->

BOWConnect terminates when trees successfully connect or when any worker reaches the goal region. Upon connection, the algorithm extracts trajectories from both trees up to the connection points, generates the BVP bridge trajectory, and concatenates them. If the backward trajectory does not fully reach the goal, an additional BVP call extends it from the last state to the goal configuration.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-C Solution Extraction and Fallback Mechanisms", "weight": 1.0} -->

The algorithm implements graceful degradation through fallback solutions. If no connection is found within the time budget but a forward worker reached the goal, that unidirectional solution is returned. Similarly, backward solutions serve as fallbacks. The parallel architecture provides theoretical speedup proportional to the number of workers, though practical speedup is limited by connection checking overhead and sequential BVP solving. With $N_{f}$ forward and $N_{b}$ backward workers, the probability of finding at least one successful path is: where $p_{\text{single}}$ is the success probability of a single worker pair. This portfolio effect, combined with BOW's efficient local planning, enables BOWConnect to solve complex kinodynamic planning problems in real-time.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments and Results", "weight": 1.0} -->

All experiments were performed on a desktop computer running Ubuntu 22.04 LTS with an AMD Ryzen^TM^ 9 7950X processor with 32 GB of RAM. Robot localization was achieved using a VICON motion capture system sampling at 120 Hz. The BOWConnect Planner was parameterized with the following constraints: maximum and minimum speeds of 1.0 m/s and 0.0 m/s respectively, maximum acceleration of 0.5 m/s^2^, maximum yaw rate of 0.6981 rad/s, and maximum yaw acceleration of 2.0472 rad/s^2^. The planner employed a time discretization of 0.1 s and a local planning horizon of 3.0 - 5.0 s. We evaluate BOWConnect against state-of-the-art kinodynamic planners with OMPL implementation including RRT, SST, EST, KPIECE, and BOW.

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-A UGV Benchmark Results", "weight": 1.0} -->

All planners are evaluated across six complex environments: Bugtrap, Narrow Passage-1, Narrow Passage-2, Forest, Nonconvex, and Intel as shown in Table. I. For each environment--planner pair, five independent trials were conducted, and the mean and standard deviation of all key metrics (except success rate) were computed. All planners were evaluated under both Unicycle and Bicycle motion models. The evaluation metrics include total planning time, trajectory length, success rate, average velocity, and average jerk.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-A UGV Benchmark Results", "weight": 1.0} -->

We set the solver timeout to $5$--$30$ s depending on environment complexity. Across all environments, BOWConnect achieves 100% success under both Unicycle and Bicycle motion models. Baseline planners degrade significantly under the Bicycle model, which imposes stricter nonholonomic constraints. EST and KPIECE fail entirely (0%) under the Bicycle model in every environment. RRT and SST also degrade, dropping to 40% and 20% in Narrow Passage-2 and to 40% and 20% in Nonconvex, respectively. Even under the Unicycle model, KPIECE fails in Nonconvex and Intel, while SST and EST drop below 100% in several environments. BOWConnect also achieves the fastest or near-fastest computation time across all environments under both motion models. In Bugtrap, it computes solutions in $0.035$ s (Unicycle) and $0.021$ s (Bicycle), outperforming all baselines except BOW under the Bicycle model ($0.019$ s).

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-A UGV Benchmark Results", "weight": 1.0} -->

In Narrow Passage-1 and Narrow Passage-2, where classical planners approach the $30$ s time limit or fail, BOWConnect solves both in under $0.06$ s. In Forest and Nonconvex, it computes solutions in under $0.03$ s under both models. Even in the most complex environment (Intel), BOWConnect remains the fastest planner at $0.397$ s (Unicycle) and $2.133$ s (Bicycle), while baselines require $6.886$ to $30$ s.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-A UGV Benchmark Results", "weight": 1.0} -->

BOWConnect also produces shorter trajectories in several environments. In Nonconvex, forward-only planners tend to explore suboptimal paths, whereas BOWConnect's backward tree guides expansion toward the goal more directly, achieving the shortest average trajectory ($15.814$ m Unicycle, $17.816$ m Bicycle) among all planners. The benefit is particularly evident under the Bicycle model, where BOW produces $28.626$ m compared to BOWConnect's $17.816$ m. Similarly, in Forest, BOWConnect achieves the shortest trajectory under both models ($20.176$ m and $21.464$ m).

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-A UGV Benchmark Results", "weight": 1.0} -->

The average velocity of BOWConnect remains competitive across all environments and achieves the highest value in Nonconvex for both motion models. BOW-based planners further exhibit significantly lower jerk values than classical sampling-based methods, indicating smoother control profiles. For example, in Bugtrap (Bicycle), BOWConnect achieves an average jerk of 0.0279, substantially lower than RRT and EST.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-B UAV Benchmark Results", "weight": 1.0} -->

We evaluate BOWConnect across four quadrotor environments (Quad-1 through Quad-4) using the same baselines and evaluation metrics (Table II). All planners achieve 100% success in every environment. However, significant differences arise in computation time and trajectory quality.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-B UAV Benchmark Results", "weight": 1.0} -->

BOWConnect and BOW both compute solutions in under $0.12$ s, while SST, EST, and KPIECE consistently require $30$--$42$ s. In Quad-1, BOWConnect requires $0.117$ s compared to $7.815$ s for RRT and over $29$ s for SST and KPIECE. BOWConnect achieves the fastest time in Quad-2 ($0.086$ s), while BOW is slightly faster in Quad-1 ($0.094$ s), Quad-3 ($0.074$ s), and Quad-4 ($0.058$ s).

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-B UAV Benchmark Results", "weight": 1.0} -->

BOWConnect produces the shortest trajectories in Quad-1 ($6.562$ m) and Quad-4 ($6.231$ m), with consistently lower variance than BOW. In Quad-2 and Quad-3, SST yields the shortest trajectories ($16.715$ m and $16.615$ m), but requires over $30$ s to compute them. BOWConnect also achieves the lowest jerk in Quad-1 ($0.0279$) and Quad-4 ($0.0246$), indicating smoother control profiles than classical planners while maintaining computation times two orders of magnitude lower.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-C Unmanned Ground Vehicle Real-World Experiments", "weight": 1.0} -->

Fig. 2: Experimental validation of the proposed kinodynamic motion planner in a cluttered indoor laboratory environment under two representative start–goal configurations. Fig. 2a and Fig. 2b illustrate the first and second configurations, respectively. In each case, the left panel shows the planned trajectory visualized in RViz, where the green-to-red color gradient indicates temporal progression, and the right panel shows the corresponding real-world UGV experiment conducted under similar obstacle layouts.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-C Unmanned Ground Vehicle Real-World Experiments", "weight": 1.0} -->

We implemented BOWConnect on a non-holonomic differential-drive Create 3 educational robot with a radius of 0.17 m, operating within a bounded 6.5 m × 5.5 m workspace populated with obstacle configurations designed to emulate the constrained geometry of the benchmark scenario. Collision checking was performed using a 2D occupancy grid map constructed from the laboratory layout, while localization was provided by a Vicon motion capture system to ensure high-precision state estimation during execution. The UGV is modeled using a five-dimensional state vector $\mathbf{x}=(x,y,\theta,v,\omega)$, where $(x,y)$ denote planar position, $\theta$ is the heading angle, $v$ the linear velocity, and $\omega$ the angular velocity, with control input $\mathbf{u}=(v_{c},\omega_{c})$ representing commanded linear and angular velocities with respect to the body frame. The Unicycle motion model was used for the physical experiments.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-C Unmanned Ground Vehicle Real-World Experiments", "weight": 1.0} -->

As illustrated in Fig. 2, the goal pose (marked as a purple disk) was specified interactively in RViz using a 2D goal command, after which BOWConnect generated a dynamically feasible trajectory that was executed by the robot. The primary objective was to validate kinodynamic feasibility and real-time performance, and multiple start--goal configurations were tested across the workspace, with BOWConnect consistently generating feasible trajectories in under 0.15 s. During execution, the maximum linear velocity was limited to 1.0 m/s and the maximum angular velocity to 1.5 rad/s, while the low-level controller operated with a control time step of $\Delta t=0.05$ s. Across five independent trials with varying start--goal configurations, no collisions or tracking instabilities were observed during execution. The average planning time was 0.12 s, with a maximum of 0.15 s across all runs, demonstrating real-time feasibility on the onboard compute platform.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-C Unmanned Ground Vehicle Real-World Experiments", "weight": 1.0} -->

Fig. 3: BOWConnect quadrotor experiments in a cluttered indoor environment with a fixed obstacle layout and two distinct start–goal configurations. Fig. 3a shows the first configuration, while Fig. 3b shows the second configuration. In each case, the left panel presents the simulated planning setup with the generated kinodynamic trajectory (green) visualized in RViz, and the right panel shows the corresponding real-world quadrotor experiment conducted under the identical obstacle arrangement, demonstrating sim-to-real consistency in trajectory execution.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-D Unmanned Aireal Vehicle Physical Experiments", "weight": 1.0} -->

We implemented BOWConnect on a 6-DOF quadrotor UAV in a three-dimensional environment with 3D obstacles to demonstrate the capability of the proposed planner in high-dimensional planning problems, as shown in Fig. 3. The experiments were conducted using a Parrot Bebop 2 UAV. The UAV state is modeled using an 8-dimensional vector $\mathbf{x}=(x,y,z,\theta,\dot{x},\dot{y},\dot{z},\dot{\theta})$, which includes position, yaw orientation, and linear and angular velocities. The control input is defined as a 4-dimensional vector $\mathbf{u}=(\dot{x}_{c},\dot{y}_{c},\dot{z}_{c},\dot{\theta}_{c})$, representing commanded body-frame linear velocities and yaw rate.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-D Unmanned Aireal Vehicle Physical Experiments", "weight": 1.0} -->

In Fig. 3, the left panels show the RViz visualization with the real UAV state and the planned trajectory generated by BOWConnect (green), while the cyan curve denotes the actual trajectory followed by the UAV during execution. The goal position is sent interactively from RViz using the Nav Goal tool. The experiments were conducted in a bounded workspace of $6.5~\text{m}\times 5.5~\text{m}\times 2.5~\text{m}$ with three box-shaped obstacles placed to replicate the RViz configuration: two identical obstacles of dimensions $0.4~\text{m}\times 0.8~\text{m}\times 0.92~\text{m}$ and one obstacle of dimensions $0.64~\text{m}\times 0.64~\text{m}\times 1.08~\text{m}$. The close alignment between the planned trajectory (green) and the executed trajectory (cyan) demonstrates accurate tracking and confirms the dynamic feasibility of the generated paths.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-D Unmanned Aireal Vehicle Physical Experiments", "weight": 1.0} -->

Multiple trials were conducted from different start and goal configurations, and in all cases BOWConnect consistently computed collision-free trajectories in under $0.1~\text{s}$, demonstrating computational efficiency and robustness in high-dimensional kinodynamic planning.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper presented BOWConnect, a bidirectional parallel kinodynamic motion planner that combines parallel Bayesian Optimization over Windows local planners with spatial hashing and boundary value solver to overcome the sample inefficiency, heuristic limitations, and narrow passage failures of existing kinodynamic planners. BOWConnect replaces random control sampling with GP-guided acquisition and grows trees from both start and goal regions in parallel. Across ten benchmark environments evaluated under both kinematic and dynamic motion models, BOWConnect consistently achieves 100% success and the fastest or near-fastest computation time, typically solving problems in under 0.019s to 2.133s while classical planners such as SST, EST, and KPIECE frequently require 7 to 42 s or fail entirely. Real-world experiments on a ground vehicle and a quadrotor confirm real-time performance under 0.15 s with no collisions, validating the practical applicability of the approach. Future work will explore adaptive worker allocation, planning under uncertainty, and extension to dynamic environments with moving obstacles.
