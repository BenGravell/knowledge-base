<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

FRENETIX: A High-Performance and Modular Motion Planning Framework for Autonomous Driving

Topics include Motion planning, Frenet frame, Autonomous driving, Modular, High performance, CommonRoad.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces FRENETIX, a high-performance and modular motion planning framework for autonomous driving built around Frenet-frame trajectory sampling. Features a Python/C++ implementation with CommonRoad compatibility, achieving real-time performance through parallelized sampling and efficient trajectory evaluation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our research introduces a modular motion planning framework for autonomous vehicles using a sampling-based trajectory planning algorithm. This approach effectively tackles the challenges of solution space construction and optimization in path planning. The algorithm is applicable to both real vehicles and simulations, offering a robust solution for complex autonomous navigation. Our method employs a multi-objective optimization strategy for efficient navigation in static and highly dynamic environments, focusing on optimizing trajectory comfort, safety, and path precision. The algorithm is used to analyze the algorithm performance and success rate in 1750 virtual complex urban and highway scenarios. Our results demonstrate fast calculation times (8ms for 800 trajectories), a high success rate in complex scenarios (88%), and easy adaptability with different modules presented. The most noticeable difference exhibited was the fast trajectory sampling, feasibility check, and cost evaluation step across various trajectory counts. We demonstrate the integration and execution of the framework on real vehicles by evaluating deviations from the controller using a test track. This evaluation highlights the algorithm's robustness and reliability, ensuring it meets the stringent requirements of real-world autonomous driving scenarios.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

With its promise of revolutionizing transportation, autonomous driving technology faces significant real-world challenges, as highlighted by various collision reports and practical experiences[Pokorny2022]. Among these challenges are the complexities of urban navigation, the unpredictability of traffic and pedestrian behavior, and the necessity for rapid, informed decision-making in constantly changing environments[Gu2013]. These factors underscore the importance of high-performance and adaptable trajectory planning algorithms in autonomous vehicles (AVs) (fig:introduction).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

confidence=None created_by=None text='\\begin{tikzpicture}[font=\\scriptsize]\n % Ego vehicle\n \\node[inner sep=0pt] at (0.7,0) {\\includegraphics[height=2.5mm]{figures/ego.png}};\n \\node[align=left, anchor=west] at (1.0,0) {ego \\\\ vehicle};\n \n % Obstacle\n \\node[inner sep=0pt] at (2.6,0) {\\includegraphics[height=2.5mm]{figures/dyn_obstacle.png}};\n \\node[align=left, anchor=west] at (2.9,0) {dynamic \\\\ obstacle};\n \n % Reference path\n \\draw[thick, GreenCR] (4.2,0) -- (4.6,0);\n \\node[align=left, anchor=west] at (4.6,0) {reference

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

\\\\ path $\\Gamma$};\n\n % Start Position\n \\node[inner sep=0pt] at (6.1,0) {\\optimaltrajectoryCR};\n \\node[align=left, anchor=west] at (6.3,0) {optimal \\\\ trajectory};\n\n % Goal Area\n \\node[inner sep=0pt] at (7.7,0) {\\trajectoriesCR};\n \\node[align=left, anchor=west] at (7.9,0) {trajectory \\\\ samples};\n \n \\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> Visualization of a trajectory planner for AVs, depicting potential trajectories while selecting an optimal trajectory for safe navigation in a dynamic and complex urban environment.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unfortunately, foundational, traditional trajectory planning methods often struggle to cope with the dynamic and intricate nature of real-world driving scenarios, especially in diverse and unpredictable conditions encountered in urban settings. This highlights the need for trajectory planning algorithms with low calculation times, robustness, and high adaptability to various situations to ensure safety and efficiency in autonomous driving. Our work introduces a modular framework for motion planning, including an analytical sampling-based trajectory planning algorithm, to address these challenges. This algorithm is designed to efficiently handle the complexities and uncertainties inherent in urban driving environments.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

- We introduce FRENETIX, a publicly available sampling-based trajectory planner for autonomous vehicles (AVs). This planner utilizes a multi-objective optimization strategy to enhance trajectory comfort, safety, and path precision in complex environments. We now offer a comprehensive toolbox that combines a planner and simulation environment, providing an all-in-one solution for diverse scenarios. - Our approach is modular, enhancing adaptability and scalability. This design allows for straightforward integration and optimal functionality of system components across various scenarios. - We offer Python and C++ implementations to demonstrate the algorithm's real-time capability and success rate in complex scenarios, including tests on actual vehicles to highlight its practical effectiveness and efficiency in real-world applications.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Methodology", "weight": 1.0} -->

This section introduces the FRENETIX algorithm, a motion planning algorithm for AVs. FRENETIX enables efficient, safe, and reliable navigation (e.g., overtaking), especially in dynamic and complex environments. The modular structure (fig:modules) of FRENETIX is a key feature, simplifying the planning process while enhancing adaptability and scalability for different scenarios. Developed using Python for its flexibility and prototyping capabilities, FRENETIX also incorporates C++ components to improve computational efficiency. This combination results in a system that optimizes performance and is practical for deployment. At its heart is an iterative motion planning cycle, including sampling, cost functions, risk assessments, validity checks, and safety features for continuously refining the vehicle's trajectory in response to environmental changes. A simplified overview of the trajectory planning procedure is shown in fig:planningprocedure. The module-based overview of the motion planning framework FRENETIX can be seen infig:modules.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Methodology", "weight": 1.0} -->

confidence=None created_by=None text='\\begin{tikzpicture}[font=\\scriptsize]\n % Ego vehicle\n \\node[inner sep=0pt] at (0.7,0) {\\includegraphics[height=2.5mm]{figures/ego.png}};\n \\node[align=left, anchor=west] at (1.0,0) {ego \\\\ vehicle};\n \n % Obstacle\n \\node[inner sep=0pt] at (2.6,0) {\\includegraphics[height=2.5mm]{figures/dyn_obstacle.png}};\n \\node[align=left, anchor=west] at (2.9,0) {dynamic \\\\ obstacle};\n \n % Reference path\n \\draw[thick, GreenCR] (4.2,0) -- (4.6,0);\n \\node[align=left, anchor=west] at (4.6,0) {reference

<!-- chunk {"id": "body-0011", "role": "body", "section": "Methodology", "weight": 1.0} -->

\\\\ path $\\Gamma$};\n\n % Start Position\n \\node[inner sep=0pt] at (6.3,0) {\\arrowCR};\n \\node[align=left, anchor=west] at (6.6,0) {start};\n\n % Goal Area\n \\node[inner sep=0pt] at (7.7,0) {\\boxCR};\n \\node[align=left, anchor=west] at (7.9,0) {Goal \\\\ Area};\n \n \\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> [Initial scenario at timestep 0, depicting the vehicle's starting position and potential trajectories within the lanelet network.] [Progression of the scenario at timestep 35, illustrating dynamic trajectory adjustments based on real-time environmental feedback.] [Final trajectory, demonstrating the optimized path and states the vehicle will follow within the lanelet network.]

<!-- chunk {"id": "body-0012", "role": "body", "section": "Methodology", "weight": 1.0} -->

Visualization of the sequential progression of the motion planning algorithm over time. The black trajectory shows the selected optimal trajectory. The gray trajectories are kinematically infeasible. The feasible trajectories are highlighted using a color scale corresponding to the cost, where green indicates a low cost and red indicates a high cost.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Preprocessing", "weight": 1.0} -->

The trajectory planning algorithm obtains the environment data from the map configuration, in our case, from the CommonRoad[commonroad,Wuersching2024] scenario database (fig:cont). The environment, modeled as a semantic lanelet network with static and dynamic obstacles and traffic signs, contains traffic participant data, regulatory elements, and the specific planning problem. Each obstacle is characterized by its type, dimensions, location, and orientation. The planning problem is defined by the initial state of the ego vehicle and the conditions required to reach a specific goal. An initial optimal global route through the lanelet network is needed to form a reference path $\Gamma$ for subsequent trajectory generation in the Frenet coordinate system to localize the ego vehicle. To select the optimal sequence of lanelets, a graph optimization algorithm, such as Dijkstra [Dijkstra.1959] or A* [Hart.1968], is employed. The selected lanelets are interconnected through their centroids, forming a navigable route.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

We differentiate between the trajectory planning cycle and the motion planning cycle. While trajectory planning (fig:planningprocedure) is limited to the core functionality of trajectory generation and evaluation, motion planning represents the entire FRENETIX module (fig:modules) with all modules and extensions.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

Vehicle state update:The trajectory planning cycle starts by updating the ego vehicle's state in our trajectory planning algorithm. This involves refreshing the state vector with the latest position and trajectory data and merging past states with current planner-directed controls.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

Trajectory sampling: Our planner is implemented as a semi-reactive approach[werling.2010] to generate vehicle trajectories by continuously optimizing local paths and performing cyclic replanning steps (fig:contb). Samples are generated in the Frenet coordinate system to simplify trajectory planning by separating longitudinal and lateral vehicle motion. The vehicle's position in the Frenet frame is quantified using two key parameters: the lateral displacement, denoted as $d$, and the longitudinal displacement, represented by $s$, as illustrated in fig:frenet[werling.2010]. Unlike the traditional Cartesian coordinate system, the Frenet coordinate system adopts a path-focused methodology. Within this system, a vehicle's position and movement are characterized by their relationship to a predetermined reference path, providing a distinct, path-oriented viewpoint.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

confidence=None created_by=None text='\\begin{tikzpicture}[font=\\scriptsize]\n % Ego vehicle\n \\node[inner sep=0pt] at {\\includegraphics[width=0.3\\textwidth, trim={0cm 1.5cm 2.5cm 1.5cm},clip]{figures/Curvilinear-2.pdf}};\n \\node[align=left, anchor=west] at (1.1,1.8) {trajectory};\n \\node[align=left, anchor=west] at (2.7,1.3) {reference \\\\ path $\\Gamma$};\n \\node[align=left, anchor=west] at (0.85,-0.85) {$s(t)$};\n \\node[align=left, anchor=west] at (-0.2,0.0) {$d(t)$};\n \\end{tikzpicture}'

<!-- chunk {"id": "body-0018", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

language=<CodeLanguageLabel.TIKZ: 'Tikz'> Frenet coordinate system for trajectory generation, adapted.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

The trajectory planning algorithm generates potential final states for lateral and longitudinal trajectories within a predetermined discretization scheme shown intab:sampling\_matrix.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

| Sampling category | Sampling scheme | The density and number of trajectories can be defined. $t_{\text{max}}$ corresponds to the maximum sampled time horizon $\tau$ and the index $curr$ represents a clipping to the current ego vehicle state. All trajectories are extended to a fixed planning horizon $T$ to ensure comparability between all samples for later cost evaluations. $v_{\text{min}}$ and $v_{\text{max}}$ are dependent on the current vehicle state and the acceleration limits. Due to the dependencies, the s-sampling method is only used if velocity-sampling is deactivated. This is because the longitudinal end state can only be defined by the velocity or position range to avoid overdetermination. The sampling scheme in tab:sampling\_matrix contains the possible variants and the number of trajectories to be generated. There are extensions to the systematic sampling procedure, e.g., limiting sampling to the width of the roadway or the reachable set of the ego vehicle[Manzinger2021].

<!-- chunk {"id": "body-0021", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

For lateral trajectories, the sampling process involves considering different lateral distances $d_\mathrm{\tau}$ from the reference path $\Gamma$ and distinct time horizons $\tau$. Similarly, for longitudinal trajectories, the algorithm samples endpoints at various velocities $v_\mathrm{\tau}$ and again distinct time horizons. Alternatively, the endpoint $s_\mathrm{\tau}$ can be defined directly over all sampled time horizons $\tau$. In this case, the velocity profile is adapted to the endpoint constraint. This method ensures that the longitudinal trajectory samples represent different speeds and acceleration profiles. These sampled final states serve as targets for the vehicle to conclude its trajectory. To effectively connect an initial state $\zeta = \zeta_\mathrm{0}$ with a final state $\zeta(\tau) = \zeta_\mathrm{\tau}$ and form a coherent path, suitable polynomial functions are employed (fig:contc). In lateral motion planning, quintic polynomial functions are utilized to guarantee a trajectory that is both smooth and minimal in jerk [Takahashi].

<!-- chunk {"id": "body-0022", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

Consequently, the trajectory along the lateral direction is represented by a polynomial function of the form: $$\zeta(t) = c_\mathrm{0} + c_\mathrm{1} \, t + c_\mathrm{2} \, t^{2} + c_\mathrm{3} \, t^{3} + c_\mathrm{4} \, t^{4} + c_\mathrm{5} \, t^{5}$$ Differentiating the polynomial function (eq:quinticpolynom) twice yields a system of equations as follows: This matrix equation establishes the relationship between the polynomial coefficients \(c\_0, \ldots, c\_5 \) and the vehicle's state.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

The final lateral state velocity $\dot{d}_\mathrm{\tau}$ and acceleration $\ddot{d}_\mathrm{\tau}$ are set to zero, as the planning algorithm aims for a movement parallel to the reference path. For trajectory generation in the longitudinal direction, quartic polynomials are employed, providing an adequate description of vehicle motions in the longitudinal direction while ensuring minimal jerk [werling.2012]. When s-sampling is enabled, quintic polynomials are used because the endpoint manifold is omitted. The quartic polynomials in the longitudinal direction enable a manifold of the end positions since the velocity at the endpoint is not zero, while the acceleration is. The coefficients can analogously be calculated by solving an adapted version of eq:quinticmatrix and applying the appropriate boundary conditions presented in [werling.2012]. By sampling $m$ trajectories in the longitudinal direction and $n$ in the lateral direction, a set comprising $m \times n$ trajectories is constructed through a systematic crosswise superposition of these two sets. The number of trajectories generated depends on the sampling scheme and density.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

With the completion of the sampling process, the trajectory samples are transformed back into global cartesian coordinates for further evaluation steps. The sampling process is visualized in fig:sampling, where the resulting samples are shown in curvilinear and cartesian coordinate systems. [Curvilinear coordinate system] [Cartesian coordinate system] Sampling process in different coordinate systems, as per: subfigure (a) illustrates trajectories in curvilinear coordinates, capturing the primary direction of movement within a curved reference frame. Subfigure (b) translates these trajectories into cartesian coordinates. The ego vehicle is blue (\node[inner sep=0pt] at {\includegraphics[height=2.1mm]{figures/ego.png}};), indicating its position following the sampled trajectories along the reference path (\draw[thick, GreenCR] -- (0.4,0); \node[inner sep=0pt] at (0,-0.05) {}; Trajectory evaluation:The trajectory evaluation stage is required to assess the trajectory samples w.r.t. feasibility and optimality.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

This stage adopts a systematic funnel approach, processing all trajectory samples generated in the preceding step through a sequence of evaluations. These assessments are designed to identify the optimal trajectory that the vehicle should adhere to for the subsequent timestep. 1.) Kinematic check: The first step in the evaluation process is a kinematic check. This involves assessing each trajectory sample to ensure it satisfies the kinematic constraints of the vehicle based on a kinematic single-track model. This step ensures that the trajectories are within the physical movement capabilities of the ego vehicle, considering the acceleration, curvature, curvature rate, and yaw rate.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

The permissible acceleration $ a_{\text{permissible}}(t) $ is expressed as[commonroad]: a_{\text{max}} \cdot \frac{v_{\text{switch}}}{v(t)} & \text{if } v(t) > v_{\text{switch}} \\a_{\text{max}} & \text{if } v(t) \leq v_{\text{switch}} $ v(t) $ denote the vehicle's velocity at any point along the trajectory, and $ a(t) $ represent the corresponding acceleration. Given a predefined maximum acceleration $ a_{\text{max}} $ and a threshold velocity $ v_{\text{switch}} $, which delineates the transition from constant to variable acceleration limits.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

The kinematic feasibility is thus determined by evaluating whether the actual acceleration $ a(t) $ for each trajectory point remains within the bounds of $ -a_{\text{max}} $ and $ a_{\text{permissible}}(t) $: $$-a_{\text{max}} \leq a(t) \leq a_{\text{permissible}}(t), \quad \forall t \in [t_0, t_f]$$ $ t_0 $ and $ t_f $ represent the start and end of the considered time interval, respectively. Furthermore, the curvature $\kappa(t)$ of the trajectory at any point in time must not exceed the maximum curvature $\kappa_{\text{max}}$, which is derived from the maximum allowable steering angle $\delta_{\text{max}}$ and the wheelbase $L$ of the vehicle: $$\kappa_{max} = \frac{\tan(\delta_{max})}{L}$$ Thus, the curvature constraint can be stated according to eq:curvatureconstraint.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

$$|\kappa(t)| \leq \kappa_{max}, \quad \forall t \in [t_0, t_f]$$ Implemented Cost Functions.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

Cost function Formula Explanation 2*Acceleration 2*$J_\mathrm{A} = \int_{t_\mathrm{0}}^{t_\mathrm{f}} a^{2} \mathrm{d}t$ quantifies the total squared acceleration $a$, penalizing large accelerations Jerk $J_\mathrm{J} = \int_{t_\mathrm{0}}^{t_\mathrm{f}} \dot{a}^{2} \mathrm{d}t$ quantifies the total squared jerk $\dot{a}$, penalizing abrupt changes 2*Lateral jerk 2*$J_\mathrm{J_\mathrm{lat}} = \int_{t_\mathrm{0}}^{t_\mathrm{f}} \dot{a}_\mathrm{lat}^{2} \mathrm{d}t$ quantifies the total squared lateral jerk $\dot{a}_\mathrm{lat}$, penalizing sudden changes in lateral acceleration -7*ComfortComfort

<!-- chunk {"id": "body-0030", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

2*Longitudinal jerk 2*$J_\mathrm{J_\mathrm{lon}} = \int_{t_\mathrm{0}}^{t_\mathrm{f}} \dot{a}_\mathrm{lon}^{2} \mathrm{d}t$ quantifies the total squared longitudinal jerk $\dot{a}_\mathrm{lat}$, penalizing sudden changes in longitudinal acceleration -3*.Efficiency.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

Efficiency 3*Velocity offset 34.8cm$J_\mathrm{VO} = \int_{t_\mathrm{s}}^{t_\mathrm{f}} \abs{v(t) - v_\mathrm{ref}(t)} \, \mathrm{d}t \newline \phantom{bbbbbbb} + (v(t_\mathrm{f}) - v_\mathrm{ref}(t))^{2}$ calculates the absolute velocity offset compared to a reference velocity $v_\mathrm{ref}(t)$ over a given period from $t_\mathrm{s}$ to $t_\mathrm{f}$, with an additional emphasis on the squared difference in velocity at the final time $t_\mathrm{f}$ 2*Dist. to ref.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

path 2*$J_\mathrm{RP} = \int_{t_\mathrm{0}}^{t_\mathrm{f}} {d}^{2}(t) \, \mathrm{d}t$ measures the total squared distance from the reference path, penalizing deviations from the desired path 2*Dist. to obstacle 2*$J_\mathrm{DO} = \sum_{1}^{n} \int_{t_\mathrm{0}}^{t_\mathrm{f}} \frac{1}{\Delta x_\mathrm{DO}^2} \mathrm{d}t$ computes the sum of the inverse squared distances to obstacles $\Delta x_\mathrm{DO}$ for $n$ different obstacles 32.0cmCollision prob.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

3*$J_\mathrm{CP} = \sum_{1}^{n} \int_{t_\mathrm{0}}^{t_\mathrm{f}} \int f(x, 0, \Sigma_\mathrm{rot}) \mathrm{d}x \, \mathrm{d}t$ calculates the total collision probability over time for $n$ obstacles by integrating the probability density function with a rotated covariance matrix $\Sigma_\mathrm{rot}$ across a spatial domain $x$ -8*SafetySafety 42.0cmCollision prob.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

mahalanobis 4*$J_{\mathrm{CM}} = \sum_{1}^{n} \int_{t_{0}}^{t_{f}} \frac{1 - \frac{t}{T}}{d_{\mathrm{M}}(u(t), v(t), \Sigma(t))} \, \mathrm{d}t $ calculates the collision probability for $n$ obstacles by integrating the inverse Mahalanobis distance $d_\mathrm{M}$ between the trajectory point $u(t)$ and each obstacle's predicted position $v(t)$, with a linearly decreasing weight over $T$ The rate of change of the curvature $\dot{\kappa}(t)$ should also be bounded to ensure smooth transitions in steering.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

Therefore, we assume a maximum acceptable curvature rate $\dot{\kappa}_{max}$ to determine the trajectory's feasibility, where $$|\dot{\kappa}(t)| \leq \dot{\kappa}_{max}, \quad \forall t \in [t_0, t_f]$$ Finally, the yaw rate $\dot{\psi}(t)$, which represents the rate of change of the vehicle's orientation $\psi$, should not exceed the maximum yaw rate $\dot{\psi}_{max}$ determined by $\kappa_{max}$ and the vehicle's velocity $v(t)$: $$\dot{\psi}_{max}(t) = \kappa_{max} \cdot v(t)$$ The yaw rate constraint is: $$|\dot{\psi}(t)| \leq \dot{\psi}_{max}(t), \quad \forall t \in [t_0, t_f]$$ Should any trajectory sample violate these constraints, it is deemed

<!-- chunk {"id": "body-0036", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

infeasible, signifying a deviation from the vehicle's kinematic capabilities.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

2.) Cost calculation: After the kinematic validation, each trajectory is assigned a cost based on a cost function. The cost computation for the trajectory planning algorithm is formulated as a weighted sum of various partial cost components, each quantifying distinct aspects of the trajectory's quality. The total cost $J_\mathrm{sum}(\xi|f_{\xi})$ for a given trajectory $\xi \in \mathcal{T}$ is expressed as: $$J_\mathrm{sum}(\xi|f_{\xi}) = \sum_{i=1}^{n} \omega_\mathrm{i} \cdot J_\mathrm{i}(\xi)$$ where $J_\mathrm{i}(\xi)$ represents the $i^{th}$ cost function from the implemented set of cost functions. The weighting factor $\omega_\mathrm{i}$ indicates the relative importance of the corresponding cost component in the overall cost calculation. The cost functions encompass criteria such as comfort, efficiency, and particularly safety [Naumann.2020].

<!-- chunk {"id": "body-0038", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

Safety is quantified primarily through collision probability costs, derived from predictive models of other traffic participants' movements [walenet]. By estimating the likelihood of a collision based on these predicted trajectories, the algorithm assigns a cost that reflects the potential collision probability. Each cost function is designed to provide a robust indicator of the trajectory's viability. An overview of all implemented cost functions is given in tab:costfunctions. After the cost computation for each trajectory, they are sorted in ascending order of their respective costs, placing the most cost-effective trajectory at the forefront for further evaluation. 3.) Collision check: The sorted trajectories then undergo a collision check using the drivability checker[DrivabilityChecker]. This step analyzes the trajectories for collisions with static and dynamic objects.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

As trajectories are required to be free of collisions for all continuous times $t$, it is crucial to ensure collision avoidance not just at discrete steps but also between any two subsequent states $x_1 = x(t_1)$ and $x_2 = x(t_2)$, where \(t\_1 \leq t\_2 \). Therefore, the collision checker uses an oriented bounding box (OBB) around the occupied spaces for two consecutive time steps. This approach makes it possible to ensure a continuous collision-free path within these intervals[DrivabilityChecker]. Initially, the first trajectory in the list is checked for collisions. If it is collision-free, the process stops. As the trajectories are already sorted according to their cost, we only need to find the first collision-free trajectory, significantly reducing the computation time for collision checking. 4.) Road boundary check: The final step involves a road boundary check, where only the first collision-free trajectory is initially evaluated for adherence to road boundaries.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

If it keeps the vehicle on the road, it is accepted; otherwise, the next trajectory is checked until one meets both non-collision and road adherence criteria[DrivabilityChecker].

<!-- chunk {"id": "body-0041", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

Optimal trajectory:The output of this evaluation funnel is the optimal trajectory, which has successfully passed through all the assessment layers with the lowest associated costs while ensuring safety. This trajectory is deemed the most suitable for execution by the vehicle, balancing efficiency, safety, and comfort.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

Emergency risk trajectory: If the evaluation does not result in an optimal trajectory, FRENETIX calculates an additional emergency trajectory. This is done by assessing the risk $R(\mathcal{\xi})$ of an unavoidable collision trajectory for the ego vehicle and the potential collision partner. The risk is defined by the maximum harm and the collision probability[geisslingerconcept].

<!-- chunk {"id": "body-0043", "role": "body", "section": "Trajectory Planning Cycle", "weight": 1.0} -->

R(\mathcal{\xi}) = \mathrm{max}(p(\mathcal{\xi}) \cdot H(\mathcal{\xi})) Emergency stopping trajectory: In scenarios where calculating the minimum risk trajectory proves infeasible, for instance, when no prediction information is available, the system defaults to a stopping trajectory. To optimize the braking process and minimize braking distance, the vehicle maintains its current lateral distance ($\text{argmin}_i \, |d_{\text{curr}} - d_{\text{samp}_d[i]}|$) from the reference path. This approach is specifically designed to maximize the absorption of longitudinal negative acceleration during braking. Furthermore, only dynamically feasible trajectories $\mathcal{T}_f$are considered in this process, ensuring both effectiveness and safety in vehicle maneuvering.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Modular Architecture", "weight": 1.0} -->

The modular software's main components and core functionalities are shown infig:modules.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Modular Architecture", "weight": 1.0} -->

Frenetix Motion Planner planning cycle iteration and module integration.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Modular Architecture", "weight": 1.0} -->

Since FRENETIX has a modular approach, one can initialize further FRENETIX modules to expand the planner's capabilities. The modules influence the motion planning process in each planning iteration. The modules can but do not have to be used. For example, the route may be reviewed and adjusted at each time step, or it may be possible to use only an initial route without further adjustment. The exchangeable integrated modules are labeled by M1-M8 in fig:modules.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Modular Architecture", "weight": 1.0} -->

M1: The global route planner generates an optimal route to the goal region in Cartesian coordinates [Hart.1968,Dijkstra.1959]. The route determines the sequence of lanelets to be traveled through. The sequence of Cartesian coordinates $[[x_1,y_1],...,[x_n,y_n]]$ is used as an interface from which a smoothed continuous path is calculated. We are calculating a smooth, approximating spline curve for a set of points in multi-dimensional space. By providing the coordinates of these points, the method generates a B-spline representation that best fits the given data[dierckx1982algorithms,dierckx1981algorithms,dierckx1993curve]. We then discretize the path again to use the trajectory calculation.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Modular Architecture", "weight": 1.0} -->

M2: The behavior & velocity planner can generate new potential routes, choose the optimal one, plan the target velocity, and facilitate high-level decision-making. The target speed $V_T$is calculated depending on the traffic rules, the vehicles in the surrounding area, the driving mode, and the goal features. The selected route, e.g., the route on the highway, can be adjusted to reach the destination according to the set requirements.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Modular Architecture", "weight": 1.0} -->

M3: Occlusion-aware trajectory planning addresses the risks posed by blind spots[Trauth2023]. Occluded areas introduce uncertainties that can result in significant personal harm if not accounted for in the planning process. These uncertainties can be effectively integrated into trajectory planning by incorporating phantom objects or risk assessments. This integration can occur either during cost calculation or during the trajectory validation stage, enhancing safety and reliability.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Modular Architecture", "weight": 1.0} -->

M4: Vehicle trajectory prediction with uncertainty integration[walenet]; The interface provides a time-based prediction of the position and speed of the surrounding objects. In addition, covariances can be added to calculate the costs more accurately when selecting the trajectory. We utilize the standardized ROS2 message format to establish the interface between the trajectory planning and prediction algorithm[Ros2].

<!-- chunk {"id": "body-0051", "role": "body", "section": "Modular Architecture", "weight": 1.0} -->

M5: Risk assessment and harm estimation of predicted traffic participants[geisslingerconcept]are crucial in ethical trajectory selection. The analysis distinguishes between vulnerable and non-vulnerable road users. Risk calculations are performed for both the ego vehicle and third-party road users. These risk assessments can inform cost calculations and serve as a trajectory validity check to ensure risk levels do not exceed acceptable thresholds.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Modular Architecture", "weight": 1.0} -->

M6: Optimizing the trajectory selection process through a reinforcement learning-based framework[Trauth-RL] addresses the challenge of setting appropriate weightings $[w_1, w_2, \ldots, w_n]$ in sampling-based approaches, particularly in dynamic situations. This hybrid approach enables continuous adaptation to various scenarios by reviewing and adjusting weightings at each time step. Consequently, it enhances the assessment of situations and the recognition of priorities, thereby improving safety. Module M8 can be used to train and validate the algorithm within an agent-based simulation framework[kaufeld2024investigating].

<!-- chunk {"id": "body-0053", "role": "body", "section": "Modular Architecture", "weight": 1.0} -->

M7: Validation & verification of the most cost-efficient trajectories through static and dynamic collision checks [DrivabilityChecker]. The module ensures that planned trajectories are both collision-free and road-compliant. It supports geometric shapes and hierarchical representations to enhance collision detection efficiency. With robust interfaces for Python and C++ implementations, it is ideal for real-time applications and simulations. The interface ensures that any CommonRoad trajectory can be processed[commonroad].

<!-- chunk {"id": "body-0054", "role": "body", "section": "Modular Architecture", "weight": 1.0} -->

M8: The Multi-agent simulation framework to investigate and test the motion planning framework before real-world application[kaufeld2024investigating]. The multiagent simulation module facilitates the use of simulations for various purposes, allowing for the execution of multiple simulations and managing numerous agents concurrently. Within this framework, the simulation class plays a pivotal role in organizing scenario-specific and planning-centric information, including prediction information of other road users. It generates batches of agents to accelerate the computation time, where each batch can comprise an arbitrary number of agents. Parallelization at the highest level is usually the most efficient. The batches enable such parallelization. This agent can be parallelized at the planner level when executing a single agent. These agent instances handle all relevant data and statuses relating to the ego vehicle, i.e., the vehicle directly controlled in the simulation. A designated planner interface governs the agents' motion planning process. This interface is designed to ensure compatibility with any planning algorithm, thus providing flexibility in assigning different planning algorithms to individual agents as required. At its heart, the framework's primary functions include transferring new individual information to the planning algorithm and the sequential execution of the planner at each time step.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Modular Architecture", "weight": 1.0} -->

Furthermore, it establishes universal interfaces, facilitating access to essential data such as trajectory information and global path details in the CommonRoad format[commonroad].

<!-- chunk {"id": "body-0056", "role": "body", "section": "Modular Architecture", "weight": 1.0} -->

- Idle: The system is inactive or has not yet been assigned a task. - Running: The system actively works towards the goal. - Goal Reached: The goal was successfully achieved within the expected time frame. - Goal Reached Outside Target Time: The goal was achieved later than the specified time frame. - Goal Reached Faster Than Target Time: The goal was achieved faster than the specified time frame. - Missed the Target: The intended goal was not achieved. - Time Limit Reached: The operation has hit its time cap without achieving the goal region. - Error: The system encountered a malfunction or unexpected issue. - Collision: The system experienced a physical collision during operation.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Modular Architecture", "weight": 1.0} -->

In our specific implementation, we use the Frenet interface to execute the planning phases of the FRENETIX Motion Planner; however, this work focuses on the execution of the single agent. The work of Kaufeld et al.[kaufeld2024investigating]provides more information on running multi-agent simulations. In addition, other modules, such as the global planner or the behavior planner, can be integrated into the agent's execution step independently of the used local planning algorithm by processing this information separately by the planning interface.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Results & Analysis", "weight": 1.0} -->

In this section, we will first examine the algorithm in simulation before demonstrating its applicability in a real vehicle. The aim is to examine the framework and the trajectory planner as standalone tools rather than comparing them to specific alternatives. This is because their performance can be continually enhanced through individual extensions.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Environment & Evaluation", "weight": 1.0} -->

We evaluate our new FRENETIX motion planner in the CommonRoad simulation environment[commonroad]. The AV has to find a trajectory in given scenarios to reach the goal region in a limited amount of time without a collision and in a kinematically feasible way. The algorithm's success rate depends on many factors and the difficulty of the scenarios. We use 1750 CommonRoad scenarios to evaluate the performance of the algorithm. In this evaluation, we maintain consistent settings and cost weightings for the algorithm, intentionally avoiding adjustments or fine-tuning. The results created are, therefore, from an untuned model lacking specialized behavior features, especially in edge-case scenarios. This ensures that the evaluation of performance is independent and unbiased. fig:success\_rate shows the simulation results of the 1750 scenarios.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Environment & Evaluation", "weight": 1.0} -->

Our FRENETIX planner finds in 1539 scenarios a safe and valid solution and can solve the scenario. In 143 scenarios, FRENETIX is causing a collision. It should be noted that incorrect predictions of vehicle movements and collisions, where the responsibility does not lie with the ego vehicle, cause around 40 of the accidents. In 29scenarios, FRENETIX could not reach the goal within a given time limit. However, this only means that the manually designed time limit of the scenario was not met.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Vehicle Dynamic Interaction Scenario", "weight": 1.0} -->

We evaluate FRENETIX in two detailed scenarios: an overtaking maneuver in fig:overtaking and an overtaking maneuver with an oncoming vehicle in fig:overtaking\_with\_oncoming\_traffic. We use different cost weight settings displayed in tab:cost\_weights to investigate the trajectory selection process while overtaking.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Vehicle Dynamic Interaction Scenario", "weight": 1.0} -->

Cost weight variations & planner setting for trajectory selection process.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Vehicle Dynamic Interaction Scenario", "weight": 1.0} -->

| Planner Settings | Values | The weightings depend on the respective cost function, meaning they can only be considered relative to their changes between different runs. In the following investigations, a distinction is made between the different weighting levels to demonstrate the performance and functionality of the algorithm. A detailed parameter analysis is not carried out, as this can be obtained from additional modules[Trauth-RL]. In the first study, without oncoming traffic, the costs of the collision probability varied to investigate the change in driving behavior.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Vehicle Dynamic Interaction Scenario", "weight": 1.0} -->

Overtaking scenario with four different cost-weight settings. The numbers next to the trajectories illustrate the progression of the runs.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Vehicle Dynamic Interaction Scenario", "weight": 1.0} -->

In our study, the overtaken vehicle maintains a constant speed of13. As illustrated in fig:overtaking, we observe that augmenting the costs associated with collision probability leads to an increased lateral distance from overtaking vehicle. If the distance is sufficient, the cost of the collision probability decreases so much that it hardly influences the distance so that the vehicle does not move unnecessarily far from the other vehicle. This ensures that the vehicle does not deviate excessively from its reference path. Under these conditions, the overtaking velocity is influenced by the target speed. Conversely, when the costs for increased distance to an obstacle are factored, the ego vehicle stays behind the preceding vehicle instead of overtaking. This is due to the increased distance to obstacle costs to the leading vehicle, which exceeds the velocity. The trajectory planner can also manage critical situations with conflicting objectives. fig:overtaking\_with\_oncoming\_traffic shows the same scenario with an oncoming vehicle. The study examines the variation in velocity costs and how to handle the oncoming traffic. The velocity costs are dependent on the target speed. With high-velocity costs, the vehicle accelerates significantly faster and can turn in again sooner after overtaking.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Vehicle Dynamic Interaction Scenario", "weight": 1.0} -->

With low-velocity costs, the vehicle in front cannot be overtaken in time. The ego vehicle has to pull in again and overtake at a later timestep after 5. Nevertheless, none of the different setups results in a collision with the other vehicles. However, the vehicle fails if we deactivate one of the two important cost functions. Collision probability costs, and velocity costs are necessary to achieve the goal region.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Vehicle Dynamic Interaction Scenario", "weight": 1.0} -->

Overtaking scenario with an oncoming vehicle with three different cost-weight settings. The numbers next to the trajectories illustrate the progression of the runs.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Calculation time", "weight": 1.0} -->

To analyze computation times for trajectory planning, the study utilized a Dell Alienware computer equipped with an AMD 7950X processor, 128 GB RAM, and an NVIDIA GeForce RTX 4090 graphics card. We benchmark our FRENETIX C++ implementation against a FRENETIX Python implementation. We distinguish between single-core (SC) and multi-processing (MP) since sampling-based planners are easy to parallelize. Since we are using a sampling scheme, we cannot linearly raise the number of trajectories. We investigate how much time the algorithm needs to create the trajectory samples, check the feasibility of each trajectory, and calculate their costs. We depict the results of this evaluation in tab:calculationtime.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Calculation time", "weight": 1.0} -->

Calculation times (in milliseconds) for trajectory sampling, feasibility check, and cost evaluation.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Calculation time", "weight": 1.0} -->

| Trajectories | C++ (SC) | C++ (MP) | % Difference (SC/MP) | Python (SC) | Python (MP) | % Difference (SC/MP) | The results reveal significant differences in calculation times between different implementations. The percentage differences between SC and MP modes were remarkably high, indicating a substantial efficiency gain in multi-processing. For instance, for 90000 trajectories, the time was reduced from 5.52 in SC to 0.717in MP. In the comparative analysis of Python implementations, MP exhibits a threshold-dependent efficacy. Specifically, Python-MP demonstrates a net advantage beyond a critical number of trajectories. This is attributable to the inherent overhead associated with MP under Python, which can outweigh the computational gains when dealing with a limited set of trajectories. Conversely, the C++ implementation showcases a more efficient resource utilization.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Real-World Vehicle Deployment", "weight": 1.0} -->

This section explores the algorithm's applicability to real-world vehicles. The tests are conducted using the EDGAR research vehicle shown in fig:edgar. This Volkswagen T7 bus is equipped with sensors and hardware necessary for fully autonomous test runs. Detailed specifications of the vehicle are available in[karle2024edgar].

<!-- chunk {"id": "body-0072", "role": "body", "section": "Real-World Vehicle Deployment", "weight": 1.0} -->

In addition to in-house implementations, the vehicle uses the basic Autoware Universe software stack[autoware]. We use ROS2 as the middleware communication interface[Ros2]. The planning algorithm is integrated into the vehicle using a CommonRoad interface toolbox[Wuersching2024]. In this way, the planning module of the Autoware software stack is completely replaced. The planning algorithm, therefore, plans on the vehicle in the same simulation environment format[Wuersching2024]. The trajectories generated by the presented algorithm are sent to the controller via ROS2[Ros2]. The control algorithm was not fine-tuned to the research vehicle and the trajectory planning algorithm to demonstrate adaptivity[autoware]. To analyze the algorithm, we initiate acceleration from a standstill, drive into a curve, and then apply braking while within the curve. fig:route\_edgar shows the driven route. The yellow area represents the destination region, and the blue vehicle shows the starting position.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Real-World Vehicle Deployment", "weight": 1.0} -->

EDGAR research vehicle testing scenario. fig:route\_edgar presents a combination of a real-world drone image and the CommonRoad lanelet street format. The algorithm utilizes the CommonRoad scenario format to plan the next trajectory[commonroad,Wuersching2024]. fig:route\_edgar illustrates the initial planning step of the vehicle along with the sampled trajectories. Gray represents dynamically infeasible trajectories, while the gradient from red to green indicates the varying costs of the feasible trajectories. The black path signifies the selected trajectory for this time step. fig:boxplots\_edgar illustrates the discrepancies between the planned trajectory, as proposed by our algorithms, and the actual output from the vehicle's controller in autonomous driving scenarios.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Real-World Vehicle Deployment", "weight": 1.0} -->

Deviations between the planned trajectory and the actual output of the controller. Velocity difference in (blue) and absolute position difference in (grey), divided into longitudinal (green) and lateral (orange) shown from left to right.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Real-World Vehicle Deployment", "weight": 1.0} -->

It can be seen that the velocity and position differences are small at moderate acceleration. The difference in velocity is usually less than 0.025. The position deviations in the lateral and longitudinal directions differ. There is a greater deviation from the controller in the longitudinal direction than in the lateral direction. The update frequency of the overall software and the driving direction can explain individual deviation measurements. The longitudinal positioning may exhibit deviations from the intended trajectory, attributable to the frequency at which the trajectory is replanned. Enhancing the frequency of trajectory planning enables more rapid integration of any deviations by the control system into the updated trajectory for the vehicle. Consequently, increasing the planning frequency can effectively diminish these deviations.

<!-- chunk {"id": "body-0076", "role": "body", "section": "FRENETIX Performance", "weight": 1.0} -->

The results from our study indicate that the FRENETIX framework presented is effective in rapidly finding a safe and reliable trajectory in dynamic environments. By outsourcing the computationally intensive functionalities to C++, the performance can be kept high even with many objects, so sufficient trajectories can always be generated at any time. However, it is essential to note that specific settings and parameters influence the algorithm's performance, which is consistent with expectations for an analytical algorithm. During our research, collisions and other issues were mainly attributed to the lack of features for specific scenarios or inadequate parameter tuning. Nonetheless, the potential for optimizing vehicle behavior in various situations is achievable through further extensions and modules. The cost functions demonstrate a variable influence on the target variables, facilitating the successful simulation of complex maneuvers, such as overtaking in the presence of oncoming traffic.

<!-- chunk {"id": "body-0077", "role": "body", "section": "FRENETIX Applicability", "weight": 1.0} -->

The presented open-source toolbox demonstrates its capability to effectively perform tests on research vehicles. Its modular structure facilitates the rapid adaptation and integration of new features and modules. This toolbox provides a convenient platform for testing and validation, addressing individual planning challenges. The accelerated research enabled by this work focuses on a modular software stack for real-world autonomous driving investigations between perception and control modules as well as for pure simulation purposes. Beyond simulation, the algorithm has been successfully implemented in a real research vehicle, with the sampling method efficiently identifying feasible trajectories. The results confirm that the controller can follow the planner's trajectory. However, it is noted that the resulting deviations can be minimized further, as the controller was not specifically tuned to the vehicle or the planning algorithm. It should also be noted that the system's overall behavior depends on many factors and is difficult to attribute to the planning algorithm. Furthermore, the presented work could also be used to investigate algorithms on other vehicles like small-scale RC cars or ground robots.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Conclusion & Outlook", "weight": 1.5} -->

This paper introduced FRENETIX, a high-performance and modular sampling-based trajectory planner algorithm designed for autonomous driving applications. We propose a novel integration of multiple steps and methods to develop a trajectory planner that operates with high computational efficiency. FRENETIX is characterized by its robustness, adaptability, and capacity to handle complex scenarios through individualized extensions. Its modular design and the presented cost functions facilitate varied prioritizations of driving behavior by adjusting the cost weights and validity checks. Our experimental results demonstrate the algorithm's ability to produce dynamic vehicle behaviors, such as overtaking maneuvers, particularly in highly dynamic environments, including scenarios with oncoming traffic. By using FRENETIX on a research vehicle, we demonstrate its suitability for use outside of simulation purposes. By open-sourcing FRENETIX, we aim to provide a valuable motion planning baseline for the community, fostering collaborative development and innovation. FRENETIX lays a strong foundation for future research in areas such as behavior planning, reinforcement learning, and other extensions, offering significant potential for comprehensive benchmark analyses.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Conclusion & Outlook", "weight": 1.5} -->

Further investigations could explore the algorithm's performance in diverse and more complex traffic situations, potentially leading to enhancements in autonomous driving systems.]Rainer Trauthreceived a B.Sc. degree in engineering science and an M.Sc. in mechanical engineering from the Technical University of Munich (TUM) in 2017 and 2020, respectively, where he is currently pursuing a Ph.D. degree in mechanical engineering at the Institute of Automotive Technology. His research interests include motion planning, situational awareness, and behavior planning approaches focusing on real-world applications in autonomous driving. received a B.Sc. degree in mechanical engineering from the Technical University of Munich (TUM) in 2021 and a M.Sc. in 2023 degree in mechanical engineering at the TUM School of Engineering and Design. He is currently pursuing a Ph.D. degree as part of the Autonomous Vehicle Systems (AVS) lab at TUM. His research interests include edge-case scenario simulation, the optimization of vehicle behavior, and motion planning in autonomous driving. received a B.Sc. degree and an M.Sc. degree in mechanical engineering from the Technical University of Munich (TUM), Munich, Germany, in 2018 and 2020, respectively.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Conclusion & Outlook", "weight": 1.5} -->

He is currently pursuing a Ph.D. degree at the professorship of cyber-physical systems (CPS) at TUM. His research interests include motion planning for autonomous driving, particularly developing robust and efficient planning algorithms for arbitrary traffic situations. is an assistant professor in the Department of Mobility Systems Engineering at the Technical University of Munich (TUM), leading the Autonomous Vehicle Systems (AVS) lab. He is one of the founders of the TUM Autonomous Motorsport team. His research focuses on developing adaptive dynamic path planning and control algorithms, decision-making algorithms that work under high uncertainty in multi-agent environments, and validating the algorithms on real-world robotic systems. Johannes earned a B.Eng. from the University of Applied Science Coburg, an M.Sc. from the University of Bayreuth, an MA in philosophy from TUM, and a Ph.D. from TUM.
