<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

PA-MPPI: Perception-Aware Model Predictive Path Integral Control for Quadrotor Navigation in Unknown Environments

Topics include Path planning, Aerial robotics, Safety, Robustness, Foundation models, Online algorithms, Sampling-based methods, Optimization, Planning, Control, Sampling, Model predictive path integral control, Model predictive path integral, Perception-aware, Predictive-action model predictive path integral control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Quadrotor navigation in unknown environments is critical for practical missions such as search-and-rescue. Solving this problem requires addressing three key challenges: path planning in non-convex free space due to obstacles, satisfying quadrotor-specific dynamics and objectives, and exploring unknown regions to expand the map. Recently, the Model Predictive Path Integral (MPPI) method has emerged as a promising solution to the first two challenges. By leveraging sampling-based optimization, it can effectively handle non-convex free space while directly optimizing over the full quadrotor dynamics, enabling the inclusion of quadrotor-specific costs such as energy consumption. However, MPPI has been limited to tracking control that optimizes trajectories only within a small neighborhood around a reference trajectory, as it lacks the ability to explore unknown regions and plan alternative paths when blocked by large obstacles. To address this limitation, we introduce Perception-Aware MPPI (PA-MPPI). In this approach, perception-awareness is characterized by planning and adapting the trajectory online based on perception objectives. Specifically, when the goal is occluded, PA-MPPI incorporates a perception cost that biases trajectories toward those that can observe unknown regions.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This expands the mapped traversable space and increases the likelihood of finding alternative paths to the goal. Through hardware experiments, we demonstrate that PA-MPPI, running at 50 Hz, performs on par with the state-of-the-art quadrotor navigation planner for unknown environments in challenging test scenarios. Furthermore, we show that PA-MPPI can serve as a safe and robust action policy for navigation foundation models, which often provide goal poses that are not directly reachable.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Enabling quadrotors to navigate to a goal in unknown environments autonomously is critical for practical missions such as search-and-rescue, infrastructure inspection, and exploration \[recalde2022system, xing2023autonomous, papachristos2019localization\]. It is also relevant for the safe deployment of navigation foundation models, which provide navigation waypoints or goals in previously unseen environments \[sridhar2023nomad, cheng2024navila\]. Achieving this capability requires addressing three key challenges: (i) non-convex constraints: cluttered environments create non-convex free space, which complicates gradient-based optimization; (ii) quadrotor-specific dynamics and costs: planned trajectories must satisfy dynamic feasibility while optimizing costs such as effort and energy; and (iii) mapping in unknown environments: since the environment must be mapped online using onboard perception, successful navigation must incorporate exploration and mapping of unknown regions to find a feasible path to the goal.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A common approach is a hierarchical planner--controller architecture \[cieslewski2017rapid, naazare2019application, liu2024integrated, achtelik2013path, super\], where a global planner computes trajectories subsequently tracked by a local controller. However, this separation often results in conservative, or dynamically infeasible plans, as quadrotor models and related costs and constraints need to be approximated \[hehn2015realtime\].

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model Predictive Path Integral (MPPI) control has recently emerged as a promising alternative. By employing sampling-based optimization, MPPI can navigate non-convex and nonsmooth free space in the presence of obstacles while directly optimizing control inputs on quadrotor-specific dynamics and costs \[saska2024MPPI, mohamed2020mppi\]. However, MPPI has been largely confined to following reference trajectories, demonstrating only limited local optimization near the reference, as it lacks both global map awareness and the capability to explore unknown areas and plan successful trajectories.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we introduce the Perception-Aware Model Predictive Path Integral (PA-MPPI) controller, tightly integrated with a perception and mapping module, to afford standard MPPI with the capability of navigating unknown environments without external references. This is achieved by extending standard MPPI with perception awareness, characterized by adapting control inputs and trajectory optimization based on both current and future perception of the environment \[xing2023autonomous, falanga2018pampc, Sarvaiya2024hpampc\]. Using the current map of the environment, PA-MPPI introduces a novel perception cost that evaluates sampled trajectories based on their potential to perceive unknown regions in the goal direction, thereby guiding the optimized trajectory to map unknown regions that lead to the goal.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We validate PA-MPPI in simulated and real-world experiments, demonstrating that perception-awareness enables MPPI to navigate through complex, unknown environments with performance comparable to SUPER \[super\], the current state-of-the-art planner for safety-assured quadrotor navigation in unknown environments.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Novel Perception-Aware MPPI Formulation: We propose a cost function that exploits the current environment map to guide trajectory optimization toward frontiers that help perceive unknown regions towards the goal, allowing MPPI to navigate without external references.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Integrated Framework: We present an integrated framework that tightly couples sensing, mapping, and a high-performance MPPI implementation, running at $50\ {Hz}$ for real-time quadrotor control.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Hardware-in-the-Loop Validation: Our experiments show that PA-MPPI performs comparably to the current SOTA planner, SUPER \[super\]. We further demonstrate that using PA-MPPI as the action policy enables robust deployment of navigation foundation models.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Derivative-based MPC", "weight": 1.0} -->

When objectives and constraints admit smooth approximations, derivative-based MPC offers strong local convergence and tight constraint handling. Progressive smoothing and continuation strategies have been proposed to navigate nonconvex obstacle costs \[reiter2024progressive\], conceptually paralleling equal to annealing in sampling-based MPC \[xue2024dialmpc\]. A recent approach proposed an algorithm with an external active set solver for cluttered point-cloud obstacles \[gao2025semiinfinite\], which achieves a feasible average but has an ample worst-case computation time. Still, in settings where, in addition to obstacles represented by raw depth maps, the cost functions are also highly nonsmooth, constructing reliable differentiable surrogates remains challenging. Sampling methods showed superior performance in these settings \[suh2022differentiable\].

<!-- chunk {"id": "body-0013", "role": "body", "section": "Sampling-based MPC", "weight": 1.0} -->

Sampling-based MPC methods, such as MPPI, optimize control sequences by Monte Carlo rollouts instead of using local gradients, making them attractive for nonconvex, nonsmooth objectives and dynamics. The most straightforward but largely inefficient random shooting method purely randomizes actions \[piovesan2009randomized\]. The Cross Entropy Method (CEM) \[rubinstein1997optimization\] iteratively refines a distribution toward high-performing controls via an elite-only update and has been widely adopted as a trajectory optimizer and within model-based RL pipelines \[chua2018deep\]. \\AcMPPI control \[kappen2005linear, theodorou2012relative, theodorou2015nonlinear\] uses all samples via weighting to iteratively refine an trajectory \[Williams2017MPPI\]. \\AcMPPI has recently been pushed to demanding robot platforms, including agile UAVs \[saska2024MPPI\] and whole-body locomotion \[alvarez2025realtime, xue2024dialmpc\].

<!-- chunk {"id": "body-0014", "role": "body", "section": "Sampling-based MPC", "weight": 1.0} -->

However, these works rely on external references, such as a reference quadrotor trajectory or quadruped walking gait joint position reference. PA-MPPI, on the other hand, enables reference-free navigation via the novel perception-aware cost.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Notation", "weight": 1.0} -->

We introduce two reference frames: $W$, the fixed world frame, whose $z$-axis is gravity-aligned, and $B$, the quadrotor body frame, whose $x$-axis aligns with the onboard camera's principal axis. In this paper, vectors and matrices are written in bold, with matrices indicated by capital letters. Each vector carries a subscript specifying the frame in which it is expressed and its endpoint. For instance, ${\mathbf{p}}_{WB} \in {\mathbb{R}}^{3}$ denotes the position of the body frame $B$ relative to the world frame $W$, and ${\mathbf{R}}_{WB}$ denotes the rotation from frame $B$ to $W$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-B Model Predictive Control", "weight": 1.0} -->

where constraints are approximated in the value and cost function. We denote the dependency of the cost function on external parameters, such as obstacle parameters or the goal by ${\mathbf{p}} \in {\mathbb{R}}^{n_{p}}$. Unlike gradient-based algorithms for solving the MPC problem, which typically rely on first or second-order derivatives, MPPI uses Monte Carlo sampling-based optimization. Despite the initial derivation of \\AcMPPI control for the stochastic system \[kappen2005linear, theodorou2012relative, theodorou2015nonlinear\], it is often used for the deterministic counterpart, where noise is added as part of the optimization algorithm \[homburger2025optimality\].

<!-- chunk {"id": "body-0017", "role": "body", "section": "Methodology", "weight": 1.0} -->

A graphical overview of the integrated control stack is shown in Fig. 2. As illustrated, PA-MPPI receives an occupancy grid from the perception module and optimizes a trajectory as control sequences, which are directly executed by the quadrotor. The proposed PA-MPPI algorithm utilizes a quadrotor dynamics model, as described in Sect. IV-A. A detailed description of the MPPI formulation is given in Sect. IV-B. The perception and mapping part, and the cost definition are detailed in Sect. IV-C and IV-D, respectively.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-A Quadrotor Dynamics", "weight": 1.0} -->

In addition to the quadrotor's position ${\mathbf{p}}_{WB}$, we define orientation, and linear velocity in the world frame by ${\mathbf{q}}_{WB} \in {\mathbb{H}}_{1}$, and ${\mathbf{v}}_{WB} \in {\mathbb{R}}^{3}$, respectively, and the quadrotor's angular velocity in the body frame by ${\mathbf{ω}}_{B} \in {\mathbb{R}}^{3}$. The collective thrust and the corresponding thrust vector in the body frame are defined as $c = {c_{1} + \ldots + c_{N_{rot}}}$ and ${\mathbf{c}}_{B} = \begin{bmatrix}
\end{bmatrix}^{\top}$, where $c_{i}$ is the thrust generated by the $i$-th of $N_{rot}$ motors.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Quadrotor Dynamics", "weight": 1.0} -->

The quadrotor mass is $m$ and ${\mathbf{g}}_{W}$ is the gravity vector in the world frame. Finally, the diagonal moment of inertia matrix is ${\mathbf{J}} \in {\mathbb{R}}^{3 \times 3}$, and the body torque is ${\mathbf{τ}}_{B} \in {\mathbb{R}}^{3}$. The quadrotor dynamics can then be expressed as

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A Quadrotor Dynamics", "weight": 1.0} -->

The lowest-level flight controller tracks the zero-order hold PA-MPPI control ${\mathbf{u}}_{t} = \begin{bmatrix}
\end{bmatrix}^{\top}$. To ensure a feasible total thrust and body rate at each timestep, we follow the single motor thrust clipping in \[saska2024MPPI\], using the motor thrust limits to acquire clipped control input $u_{t}^{\text{clip}}$, which is then used by PA-MPPI to simulate the dynamics via forward Euler integration.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B MPPI formulation", "weight": 1.0} -->

In the MPPI framework, at each timestep $k$, $N$ parallel trajectories of $H$ steps are sampled by adding multivariate Gaussian noise to the nominal control input ${\mathbf{u}}_{k:{k + H}}^{\text{nom}}$. The perturbed control sequences ${\mathbf{u}}_{k:{k + H}}^{j}$, $j = {1,\ldots,N}$, are then rolled out from the quadrotor state ${\mathbf{x}}_{k}$ using the model.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B MPPI formulation", "weight": 1.0} -->

where $\mathcal{L}^{\text{min}}$ is the lowest summed cost out of the $N$ rollouts, and $\lambda$ is the temperature parameter. A low $\lambda$ assigns higher weight to the best-performing rollout, while higher values assign more uniform weights to all rollouts \[Williams2017MPPI\]. The first action of the averaged sequence is then executed, and the optimization process repeats in the next time step.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B MPPI formulation", "weight": 1.0} -->

Recent works \[saska2024MPPI, xue2024dialmpc, howell2022\] have shown success in decoupling the prediction time step size $\Deltat_{\text{pred}}$, and the control step size $\Deltat_{\text{ctrl}}$. With ${\Deltat_{\text{pred}}} > {\Deltat_{\text{ctrl}}}$, the policy rollouts can predict over a longer real-time horizon for the same number of forward simulation steps, allowing optimization of actions further into the future. Since the optimization loop executes the first action at control frequency and the actions in the sequence are spaced by $\Deltat_{\text{pred}}$, to reuse the remaining actions as ${\mathbf{u}}^{\text{nom}}$ for the next iteration, the control sequence is linearly interpolated and shifted by $\Deltat_{\text{ctrl}}$, then down-sampled at $\Deltat_{\text{pred}}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B MPPI formulation", "weight": 1.0} -->

While the terminal value $\overline{V}$ function should in principle resemble the optimal value function and account for a recursive feasible safe set, cf. \[reiter2025synthesis\], we only consider a simple terminal hovering safe set with zero velocity and resort to a long enough planning horizon to diminish its influence on the open loop cost.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-C Perception & Environment Mapping", "weight": 1.0} -->

We use a depth sensor on the quadrotor to continuously build a 3D map of the environment during navigation. From each depth image, we reproject a point cloud into the world frame using the camera pose. The point clouds are then inserted into a ROG-Map \[ROG-Map\], which efficiently aggregates all past observations into a 3D occupancy grid representation, in which each voxel has one of three states: occupied, free, or unknown, with integer values $\{ 1,0,{- 1}\}$ respectively. Formally, the 3D occupancy grid is defined as ${\mathcal{G} \in {\{{- 1},0,1\}}^{X \times Y \times Z}}.$ We denote by $\mathcal{G}{({\mathbf{p}}_{WB})}$ the operation that looks up the voxel corresponding to position ${\mathbf{p}}_{WB}$ and returns its value.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-C Perception & Environment Mapping", "weight": 1.0} -->

The mapping pipeline is capable of processing depth images and updating the occupancy grid at $50\ {Hz}$ for a ${5 \times 5 \times 2}m$ grid with a voxel resolution of $0.1\ m$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-D Optimization Cost Definition", "weight": 1.0} -->

The stage costs have two distinct phases: when the goal is not within the direct line of sight of the quadrotor, as shown in Fig. 3, to encourage exploration, the cost is $\ell = {\ell_{\text{goal}} + \ell_{\text{goal},H} + \ell_{\text{act}} + \ell_{\text{collision}} + \ell_{\text{perception}}}$, with $c_{\text{goal}} = 0.125$ and $c_{\text{goal},{H - 1}} = 10$; when the goal is within the direct line of sight, as shown in Fig. 3, to quickly reach the goal and hover, the cost is $\ell = {\ell_{\text{goal}} + \ell_{\text{act}} + \ell_{\text{collision}} + \ell_{\text{progress}} + \ell_{\text{vel}}}$, with

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-D Optimization Cost Definition", "weight": 1.0} -->

The goal cost $\ell_{\text{goal}}$ encourages getting closer to the goal compared to the starting position of the current horizon. For the last step of the horizon $k = {H - 1}$, an additional cost $\ell_{\text{goal},{H - 1}}$ is given to weight the end position of the horizon more, similar to the intermediate point cost in \[yadav2023receding_horizon\]. This prevents greedy behavior and allows the policy to detour and go around obstacles if that brings the policy closer to the goal in the end. The action cost $\ell_{\text{act}}$ penalizes the magnitude and change in control inputs, similar to the implementation in \[saska2024MPPI\]. The velocity penalty $\ell_{\text{vel}}$ encourages the quadrotor to slow down near the goal, and the progress cost $\ell_{\text{progress}}$ encourages fast movement when a straight line path to the goal is available.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-D Optimization Cost Definition", "weight": 1.0} -->

The collision cost $\ell_{\text{collision}}$ is a binary value weighted by a large constant $c_{\text{collision}}$. The indicator function $\mathbb{1}_{\{{{\mathcal{G}{({\mathbf{p}}_{WB})}} \neq 0}\}}$ returns 1 if the quadrotor's current position lies outside the set of free voxels defined in Section IV-C. This large penalty enforces the quadrotor not only to avoid collisions with known obstacles but also to refrain from entering unknown regions, which is critical for ensuring safety when navigating in unknown environments.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-D Optimization Cost Definition", "weight": 1.0} -->

[Given only one depth observation, there is no position in known free space that has a direct line of sight to the goal. Trajectories receive a reward for exploring unknown regions (blue trajectories) or a penalty for facing obstacles (red trajectories).] [After moving to a new position while mapping the environment, there is a direct line of sight from the current position to the goal, and the second-phase cost is active, encouraging the quadrotor to directly reach the goal, and the perception cost is not assigned anymore.]
Figure 3: A top-down visualization of the ray-tracing in perception cost calculation, showing the occupied voxels (red), free voxels (green), and unknown voxels (blue), and sampled trajectories on which ray-tracing is performed.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-D Optimization Cost Definition", "weight": 1.0} -->

The perception cost, $\ell_{\text{perception}}$, consists of two components. The first, weighted by $c_{\text{PoI}}$, encourages alignment of the quadrotor's x-axis (coinciding with the depth camera's principal axis) with the direction of the goal position (point of interest), thereby maximizing the goal's visibility within the image frame \[falanga2018pampc, xing2023autonomous\]. As the quadrotor approaches the goal (distance below $c_{\text{thresh}}$), this term becomes inactive. The last two terms in $\ell_{\text{perception}}$ represent two mutually exclusive cases of the quadrotor position with respect to the mapped region of the environment.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-D Optimization Cost Definition", "weight": 1.0} -->

We define a ray that starts from the quadrotor position ${\mathbf{p}}_{WB}$ and ends at the goal position ${\mathbf{p}}_{\text{goal}}$ as: ${{{{\mathbf{r}}{(t)}} = {{\mathbf{p}}_{WB} + {t \cdot {\mathbf{d}}_{\text{goal}}}}},{\;0 \leq t \leq 1}}.$ Since ${\mathbf{p}}_{WB}$ is constrained to the known free space due to the collision cost, there exists a $t^{\ast}$ such that the ray either exits the free space at an obstacle or unknown space, as shown in Fig. 3. If ${\mathbf{r}}{(t^{\ast})}$ lies in an occupied voxel, a cost $c_{\text{occupied}}$ is assigned.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-D Optimization Cost Definition", "weight": 1.0} -->

If ${\mathbf{r}}{(t^{\ast})}$ falls in an unknown voxel, then it suggests an exploration frontier towards the goal is present, and a negative cost $c_{\text{unknown}}$ is given. When there is a direct line of sight from the current position to the goal, the second-phase cost is active, as there is no need for exploration, and no perception cost is assigned. As illustrated in Fig. 3, this ray-tracing term favors sampled trajectories that either explore unknown regions when the goal is blocked by obstacles (Fig. 3) or move directly toward the goal when possible, cf. Fig. 3. This design enables the PA-MPPI controller to exploit map information, allowing it to plan around obstacles and efficiently explore unknown space. For the implementation of ray tracing, we adopt the 3D Digital Differential Analyzer (DDA) algorithm \[amanatides1987DDA\], which does not require a signed distance field representation of the environment. Due to the high computational cost, ray tracing is performed at the last step, $k = {H - 1}$, of the open-loop trajectory.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

To evaluate the performance of PA-MPPI without considering the effect of other modules in the control loop, such as depth sensor noise or imperfect state estimation, we conduct simulated and hardware-in-the-loop (HIL) \[foehn2022agilicious\] experiments. In the HIL setting, we use a motion capture system to acquire the ground truth state of the quadrotor, and the Flightmare simulator \[song2020flightmare\] to render depth images in real time. The PA-MPPI controller is implemented in JAX and integrated into the Agilicious control framework \[foehn2022agilicious\], running on a laptop with an i7-13800H CPU with 64GB RAM and a NVIDIA A1000 laptop GPU with 6GB VRAM. The quadrotor used has a mass of $0.21\ {kg}$ and arm length $l = {19.4\ {cm}}$, with propeller radius of $3.81\ {cm}$ and a thrust to weight ratio of 6.8.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

Two sets of experiments are conducted. The first consists of navigating synthetic scenes of varying difficulty (Fig. 4) to quantitatively evaluate the performance of PA-MPPI. Robustness of PA-MPPI is also investigated by injecting wind disturbances during navigation. The second consists of indoor navigation scenes from the Habitat Matterport dataset \[ramakrishnan2021hm3d\], using goal poses proposed by a navigation foundation model \[sridhar2023nomad\] to demonstrate an example usage of PA-MPPI as the action policy for a Vision-Language-Action (VLA) model in unknown environments. A list of PA-MPPI parameters are provided in Table I. As in our experiments, the weight of the terminal safe set $c_{safe}$ barely had an influence, we set it to zero.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

[C-wall (w = 3.0 m)] [Hole (d = 0.5 m)] [4-Wall (w = 1.5 m)]
Figure 4: Synthetic scenes for navigation experiments. The goal pose for each task is always 3 m ahead of the initial pose, with three types of obstacles in between: a C-shaped wall (a), a wall with a hole (b), and four walls (c). The most challenging setting for each scene is illustrated here, with example successful trajectories depicted in blue.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

Synthetic Scene Experiment. To quantitatively evaluate the performance of PA-MPPI, we design three scenes for navigation. The first is a C-shaped wall of varying sizes, a challenging obstacle against greedy policies. The second is a hole in a wall, similar to manholes that quadrotors must navigate through during ship inspections \[Dharmadhikari2023autoassess\]. The third scene consists of four walls that the quadrotor must navigate past, which tests path-finding capabilities and precise control through narrow gaps of $0.5\ m$. The difficulty of each scene is parametrized by the size of the obstacles $w$ (each difficulty tested 5 times) or the diameter of the holes $r$ (5 random locations, each tested 2 times), as shown in Fig. 4. We validate the sufficient difficulty of the scenes by first showing that a gradient-based trajectory optimization algorithm, EGO-Planner \[EGO-Planner\], fails to solve the tasks at harder difficulties.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments", "weight": 1.0} -->

As shown in Fig. 5, while EGO-Planner is able to successfully navigate past a small obstacle, the optimization fails to converge when the A\* obstacle avoidance front-end deviates significantly from the initial trajectories, resulting in huge feasibility costs that prevent the optimization from converging.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments", "weight": 1.0} -->

As EGO-Planner \[EGO-Planner\] and trajectory tracking MPPI \[saska2024MPPI\] cannot navigate around obstacles beyond the easiest settings, we use SUPER\[super\], the state-of-the-art safety-assured MAV navigation planner in unknown environments, as the baseline. SUPER replans at $10\ {Hz}$, and a geometric controller is implemented to track the trajectories. We tune SUPER's parameter to be as fast as possible without collisions in our test scenes.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiments", "weight": 1.0} -->

The experiment results are summarized in Table II, III, IV. Guided by the perception cost, PA-MPPI moves to positions that help navigate around obstacles and map the environment towards the goal, successfully completing the tasks, as visualized in Fig. 6 and 7. While both SUPER and PA-MPPI are able to complete the tasks with 100% success rate, PA-MPPI consistently performs better in terms of total time and velocity of the trajectories, while having trajectory distances on par with SUPER. For a qualitative comparison, we visualize two trajectories from SUPER in Fig. 8. For the C-wall scene, although SUPER's A\* front-end proposed trajectories close to the obstacle wall, the subsequent trajectory optimization aggressively optimized for dynamic feasibility by penalizing jerk, body rate, and collective thrust, resulting in a smoother but longer trajectory, as shown in Fig. 8. In the 4-wall scene, the trajectory adheres to the shortest path in distance suggested by the A\* front end. However, compared to PA-MPPI's trajectory, the final trajectory requires significantly more rotational control effort, as A\* is unaware of the quadrotor dynamics.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experiments", "weight": 1.0} -->

On the other hand, PA-MPPI inherently samples dynamically feasible trajectories, allowing it to prioritize trajectory quality in the sampling-based optimization. As a result, PA-MPPI's trajectories are faster and significantly more energy-efficient.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experiments", "weight": 1.0} -->

[Duration 6.3 s, dist. 6.3 m] [Duration 7.6 s, dist. 5.5 m]
Figure 8: SUPER trajectory samples in the C-wall and the 4-wall scene

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experiments", "weight": 1.0} -->

Robustness Study. To investigate the robustness of PA-MPPI, we conduct simulated test in the most challenging setting of the three tasks while the quadrotor is subjected to external wind disturbances. The wind directions are randomly sampled in the $xy$-plane for each episode, with wind magnitudes of $\lbrack{1.0{m\ s^{- 1}}},{2.0{m\ s^{- 1}}},{3.0{m\ s^{- 1}}}\rbrack$ with 10 test episodes each. The results are shown in Fig. 9. With low external wind speed, PA-MPPI retains a high success rate, while at larger wind speeds, the controller cannot compensate for the disturbance, resulting in more episodes failing by colliding into the obstacles or being blown into unknown areas, resulting in early terminations.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experiments", "weight": 1.0} -->

PA-MPPI combined with Navigation Foundation Model. We validate the real-world applicability of the PA-MPPI controller by using it as the action policy for a navigation foundation model, NoMaD \[sridhar2023nomad\], which proposes trajectory waypoints. Since the inputs to NoMaD are only monocular RGB images, the proposed waypoints are not guaranteed to be feasible due to scale ambiguity. We use two scenes from the Habitat Matterport dataset \[ramakrishnan2021hm3d\]. In the first scene, visualized in Fig. 10, the NoMaD proposed trajectory attempts to enter the room but misses the door. PA-MPPI was able to explore and map unknown regions in this scene, navigate through the door, and ultimately reach the goal position, as shown in Fig. 10. In the second scene, visualized in Fig. 10, the NoMaD trajectory starts close to a ping-pong table and goes directly through it. PA-MPPI successfully avoids the obstacle. Both scenarios demonstrate successful reference-free navigation in cluttered environments using PA-MPPI, making it a suitable action policy for navigation foundation models.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Experiments", "weight": 1.0} -->

[NoMaD proposed traj.] [PA-MPPI trajectory]
[NoMaD proposed traj.] [PA-MPPI trajectory]
Figure 10: Two Habitat scenes, with obstacles (walls, furniture, etc) overlaid in red and NoMaD proposed trajectory in blue (a)(c), and visualization of the PA-MPPI trajectory in the occupancy map (b)(d).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Discussion & Future Work", "weight": 1.5} -->

Due to the limited FoV of the depth sensor, a good initial observation is crucial for successful navigation around large obstacles. For example, in the experiment shown in Fig. 6, the initial observation at $t = {0\ s}$ is initialized by turning the quadrotor $\pm 90^{\circ}$ to observe free space outside the convex hull of the C-shaped wall. However, this issue can be solved by replacing the depth camera with LIDAR, which only requires modification to the mapping module. Additonally, we only considered navigation tasks within a fixed 3D boundary. Future work may take advantage of the local map sliding feature of the ROG-Map to implement larger scale navigation. Finally, PA-MPPI's planning horizon is constrained by available computation, which fundamentally limits the complexity of navigation scenes it can handle. This may be mitigated by using an appropriate terminal value function on the last position of the horizon. We leave this for future work to investigate.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This work presents a perception-aware MPPI controller that integrates a novel perception-driven cost to enable reference-free quadrotor navigation in partially known, cluttered environments with MPPI. By exploiting the current map, the perception term steers trajectories toward informative frontiers to explore the unknown regions and advance towards the goal. Simulated and real-world experiments demonstrate that its performance is comparable to that of the state-of-the-art navigation planner. We further demonstrate its potential as an action policy for foundation models to navigate challenging environments. Future work will focus on extending PA-MPPI to longer-horizon navigation and conducting an in-depth study of its path-planning limits and methods to mitigate them.
