<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

FRENETIX: A High-Performance and Modular Motion Planning Framework for Autonomous Driving

Topics include Motion planning, Frenet frame, Autonomous driving, Modular, High performance, CommonRoad.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces FRENETIX, a high-performance and modular motion planning framework for autonomous driving built around Frenet-frame trajectory sampling. Features a Python/C++ implementation with CommonRoad compatibility, achieving real-time performance through parallelized sampling and efficient trajectory evaluation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our research introduces a modular motion planning framework for autonomous vehicles using a sampling-based trajectory planning algorithm. This approach effectively tackles the challenges of solution space construction and optimization in path planning. The algorithm is applicable to both real vehicles and simulations, offering a robust solution for complex autonomous navigation. Our method employs a multi-objective optimization strategy for efficient navigation in static and highly dynamic environments, focusing on optimizing trajectory comfort, safety, and path precision. The algorithm is used to analyze the algorithm performance and success rate in 1750 virtual complex urban and highway scenarios. Our results demonstrate fast calculation times (8ms for 800 trajectories), a high success rate in complex scenarios (88%), and easy adaptability with different modules presented. The most noticeable difference exhibited was the fast trajectory sampling, feasibility check, and cost evaluation step across various trajectory counts. We demonstrate the integration and execution of the framework on real vehicles by evaluating deviations from the controller using a test track. This evaluation highlights the algorithm's robustness and reliability, ensuring it meets the stringent requirements of real-world autonomous driving scenarios.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

With its promise of revolutionizing transportation, autonomous driving technology faces significant real-world challenges brought to light through various collision reports and practical experiences. Among these challenges are the complexities of urban navigation, the unpredictability of traffic and pedestrian behavior, and the necessity for rapid, informed decision-making in ever-changing environments. These factors underscore the importance of high-performance and adaptable trajectory planning algorithms in autonomous vehicles (AVs) (Fig. 1). Unfortunately, foundational, traditional trajectory planning methods often struggle to cope with the dynamic and intricate nature of real-world driving scenarios, especially in diverse and unpredictable conditions encountered in urban settings. This highlights the need for trajectory planning algorithms with low calculation times, robustness, and high adaptability to various situations to ensure safety and efficiency in autonomous driving. Our work introduces an advanced analytical sampling-based trajectory planning algorithm to address these challenges. This algorithm is designed to efficiently handle the complexities and uncertainties inherent in urban driving environments.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present a publicly available sampling-based trajectory planner for AVs called FRENETIX, employing a multi-objective optimization strategy for efficient navigation in complex environments, focusing on optimizing trajectory comfort, safety, and path precision. Unlike anything available before, we offer an out-of-the-box method integrated into the simulation environment with a wide variety of scenarios.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide a modular approach to improve adaptability and scalability, allowing for easy integration and optimal functionality of each component within the system, catering to a wide range of scenarios.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide a Python and C++ implementation to demonstrate the algorithm's real-time capability and success rate in complex scenarios, showcasing its potential effectiveness and efficiency for real-world applications.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Methodology", "weight": 1.0} -->

This section introduces the FRENETIX algorithm, a motion planning algorithm for AVs. FRENETIX enables efficient, safe, and reliable navigation (e.g., overtaking), especially in dynamic and complex environments. The modular structure of FRENETIX is a key feature, simplifying the planning process while enhancing adaptability and scalability for different scenarios. Developed using Python for its flexibility and prototyping capabilities, FRENETIX also incorporates C++ components to enhance computational efficiency. This combination results in a system that optimizes performance and is practical for deployment. At its heart is an iterative motion planning cycle, including cost functions, risk assessments, validity checks, and safety features for continuously refining the vehicle's trajectory in response to environmental changes, as depicted in Fig. 2.

<!-- chunk {"id": "body-0009", "role": "body", "section": "III-A Preprocessing", "weight": 1.0} -->

The motion planning algorithm obtains the environment data from the simulation environment, in our case, from the CommonRoad scenario database (Fig. 3). The environment, modeled as a semantic lanelet network with static and dynamic obstacles and traffic signs, contains traffic participant data, regulatory elements, and the specific planning problem. Each obstacle is characterized by its type, dimensions, location, and orientation. The planning problem is defined by the initial state of the ego vehicle and the conditions required to reach a specific goal. An optimal global route through the lanelet network is needed to form a reference path $\Gamma$ for subsequent trajectory generation in the Frenet coordinate system. To select the optimal sequence of lanelets, a graph optimization algorithm, such as Dijkstra or A\*, is employed. The selected lanelets are interconnected through their centroids, forming a navigable route.

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-A Preprocessing", "weight": 1.0} -->

Risk assessment and harm estimation

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

Vehicle state update: The motion planning cycle starts by updating the ego vehicle's state in our trajectory planning algorithm. This involves refreshing the state vector with the latest position and motion data and merging past states with current planner-directed controls.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

Trajectory sampling: Our planner is implemented as a semi-reactive approach to generate vehicle trajectories by continuously optimizing local paths and performing cyclic replanning steps (Fig. 3b). Samples are generated in the Frenet coordinate system to simplify trajectory planning by separating longitudinal and lateral vehicle motion. The vehicle's position in the Frenet frame is quantified using two key parameters: the lateral displacement, denoted as $d$, and the longitudinal displacement, represented by $s$, as illustrated in Fig. 4. Unlike the traditional Cartesian coordinate system, the Frenet coordinate system adopts a path-focused methodology. Within this system, a vehicle's position and movement are characterized by their relationship to a predetermined reference path, providing a distinct, path-oriented viewpoint.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

The trajectory planning algorithm generates potential final states for lateral and longitudinal trajectories within a predetermined discretization scheme shown in Table I.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

The density and number of trajectories can be defined. $t_{\text{max}}$ corresponds to the maximum sampled time horizon $\tau$ and the index $curr$ represents a clipping to the current ego vehicle state. All trajectories are extended to a fixed planning horizon $T$ to ensure comparability between all samples for later cost evaluations. $v_{\text{min}}$ and $v_{\text{max}}$ are dependent on the current vehicle state and the acceleration limits. Due to the dependencies, the s-sampling method is only used if velocity-sampling is deactivated. This is because the longitudinal end state can only be defined by the velocity or position range to avoid overdetermination. The sampling scheme in Table I contains the possible variants and the number of trajectories to be generated. There are extensions to the systematic sampling procedure, e.g., limiting sampling to the width of the roadway or the reachable set of the ego vehicle.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

For lateral trajectories, the sampling process involves considering different lateral distances $d_{\tau}$ from the reference path $\Gamma$ and distinct time horizons $\tau$. Similarly, for longitudinal trajectories, the algorithm samples endpoints at various velocities $v_{\tau}$ and again distinct time horizons. Alternatively, the endpoint $s_{\tau}$ can be defined directly over all sampled time horizons $\tau$. In this case, the velocity profile is adapted to the endpoint constraint. This method ensures that the longitudinal trajectory samples represent different speeds and acceleration profiles. These sampled final states serve as targets for the vehicle to conclude its trajectory. To effectively connect an initial state ${\zeta{}} = \zeta_{0}$ with a final state ${\zeta{(\tau)}} = \zeta_{\tau}$ and form a coherent path, suitable polynomial functions are employed (Fig. 3c). In lateral motion planning, quintic polynomial functions are utilized to guarantee a trajectory that is both smooth and minimal in jerk.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

This matrix equation establishes the relationship between the polynomial coefficients $c_{0},\ldots,c_{5}$ and the vehicle's state.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

The final lateral state velocity ${\overset{˙}{d}}_{\tau}$ and acceleration ${\overset{¨}{d}}_{\tau}$ are set to zero, as the planning algorithm aims for a movement parallel to the reference path. For trajectory generation in the longitudinal direction, quartic polynomials are employed, providing an adequate description of vehicle motions in the longitudinal direction while ensuring minimal jerk. When s-sampling is enabled, quintic polynomials are used because the endpoint manifold is omitted. The quartic polynomials in the longitudinal direction enable a manifold of the end positions since the velocity at the endpoint is not zero, while the acceleration is. The coefficients can analogously be calculated by solving an adapted version of Eq. 3 and applying the appropriate boundary conditions presented. By sampling $m$ trajectories in the longitudinal direction and $n$ in the lateral direction, a set comprising $m \times n$ trajectories is constructed through a systematic crosswise superposition of these two sets. The number of trajectories generated depends on the sampling scheme and density.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

With the completion of the sampling process, the trajectory samples are transformed back into global cartesian coordinates for further evaluation steps. The sampling process is visualized in Fig. 5, where the resulting samples are shown in curvilinear and cartesian coordinate systems.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

Trajectory evaluation: The trajectory evaluation stage is required to assess the trajectory samples w.r.t. feasibility and optimality. Illustrated in Fig. 6, this stage adopts a systematic funnel approach, processing all trajectory samples generated in the preceding step through a sequence of evaluations. These assessments are designed to identify the optimal trajectory that the vehicle should adhere to for the subsequent timestep.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

1.) Kinematic check: The first step in the evaluation process is a kinematic check. This involves assessing each trajectory sample to ensure it satisfies the kinematic constraints of the vehicle based on a kinematic single-track model. This step ensures that the trajectories are within the physical movement capabilities of the ego vehicle, considering the acceleration, curvature, curvature rate, and yaw rate.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

Let $v{(t)}$ denote the vehicle's velocity at any point along the trajectory, and $a{(t)}$ represent the corresponding acceleration. Given a predefined maximum acceleration $a_{\text{max}}$ and a threshold velocity $v_{\text{switch}}$, which delineates the transition from constant to variable acceleration limits.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

Here, $t_{0}$ and $t_{f}$ represent the start and end of the considered time interval, respectively.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

Thus, the curvature constraint can be stated according to Eq. 7.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

quantifies the total squared acceleration a, penalizing large accelerations

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

quantifies the total squared jerk $\overset{˙}{a}$, penalizing abrupt changes

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

JVO = ∫tstf|v (t)−vref (t)| dt + (v (tf)−vref (t))2
calculates the absolute velocity offset compared to a reference velocity vref (t) over a given period from ts to tf, with an additional emphasis on the squared difference in velocity at the final time tf

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

Dist. to ref. path
measures the total squared distance from the reference path, penalizing deviations from the desired path

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

$J_{CP} = {\sum_{1}^{n}{\int_{t_{0}}^{t_{f}}{\int{f{(x,0,\Sigma_{rot})}{dx}{dt}}}}}$
calculates the total collision probability over time for n obstacles by integrating the probability density function with a rotated covariance matrix Σrot across a spatial domain x

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

Collision prob. mahalanobis
calculates the collision probability for n obstacles by integrating the inverse Mahalanobis distance dM between the trajectory point u (t) and each obstacle’s predicted position v (t), with a linearly decreasing weight over T

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

The rate of change of the curvature $\overset{˙}{\kappa}{(t)}$ should also be bounded to ensure smooth transitions in steering. Therefore, we assume a maximum acceptable curvature rate ${\overset{˙}{\kappa}}_{max}$ to determine the trajectory's feasibility, where

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

Should any trajectory sample violate these constraints, it is deemed infeasible, signifying a deviation from the vehicle's kinematic capabilities.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

2.) Cost calculation: After the kinematic validation, each trajectory is assigned a cost based on a cost function. The cost computation for the trajectory planning algorithm is formulated as a weighted sum of various partial cost components, each quantifying distinct aspects of the trajectory's quality. The total cost $J_{sum}{(\left. \xi \middle| f_{\xi} \right.)}$

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

where $J_{i}{(\xi)}$ represents the $i^{th}$ cost function from the implemented set of cost functions. The weighting factor $\omega_{i}$ indicates the relative importance of the corresponding cost component in the overall cost calculation. The cost functions encompass criteria such as comfort, efficiency, and particularly safety. Safety is quantified primarily through collision probability costs, derived from predictive models of other traffic participants' movements. By estimating the likelihood of a collision based on these predicted trajectories, the algorithm assigns a cost that reflects the potential collision probability. Each cost function is designed to provide a robust indicator of the trajectory's viability. An overview of all implemented cost functions is given in Table II. After the cost computation for each trajectory, they are sorted in ascending order of their respective costs, placing the most cost-effective trajectory at the forefront for further evaluation.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

3.) Collision check: The sorted trajectories then undergo a collision check using the drivability checker. This step analyzes the trajectories for collisions with static and dynamic objects. As trajectories are required to be free of collisions for all continuous times $t$, it is crucial to ensure collision avoidance not just at discrete steps but also between any two subsequent states $x_{1} = {x{(t_{1})}}$ and $x_{2} = {x{(t_{2})}}$, where $t_{1} \leq t_{2}$. Therefore, the collision checker uses an oriented bounding box (OBB) around the occupied spaces for two consecutive time steps. This approach makes it possible to ensure a continuous collision-free path within these intervals. Initially, the first trajectory in the list is checked for collisions. If it is collision-free, the process stops. As the trajectories are already sorted according to their cost, we only need to find the first collision-free trajectory, significantly reducing the computation time for collision checking.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

4.) Road boundary check: The final step involves a road boundary check, where only the first collision-free trajectory is initially evaluated for adherence to road boundaries. If it keeps the vehicle on the road, it is accepted; otherwise, the next trajectory is checked until one meets both non-collision and road adherence criteria.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

Optimal trajectory: The output of this evaluation funnel is the optimal trajectory, which has successfully passed through all the assessment layers with the lowest associated costs while ensuring safety. This trajectory is deemed the most suitable for execution by the vehicle, balancing efficiency, safety, and comfort.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

Emergency risk trajectory: If the evaluation does not result in an optimal trajectory, FRENETIX calculates an additional emergency trajectory. This is done by assessing the risk $R{(\xi)}$ of an unavoidable collision trajectory for the ego vehicle and the potential collision partner. The risk is defined by the maximum harm and the collision probability.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-B Motion Planning Cycle", "weight": 1.0} -->

Emergency stopping trajectory: In scenarios where calculating the minimum risk trajectory proves infeasible, for instance, when no prediction information is available, the system defaults to a stopping trajectory. To optimize the braking process and minimize braking distance, the vehicle maintains its current lateral distance ($\text{argmin}_{i}{|{d_{\text{curr}} - d_{\text{samp}_{d}{\lbrack i\rbrack}}}|}$) from the reference path. This approach is specifically designed to maximize the absorption of longitudinal negative acceleration during braking. Furthermore, only dynamically feasible trajectories $\mathcal{T}_{f}$ are considered in this process, ensuring both effectiveness and safety in vehicle maneuvering.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-A Environment & Evaluation", "weight": 1.0} -->

We evaluate our new FRENETIX motion planner in the CommonRoad simulation environment. The AV has to find a trajectory in given scenarios to reach the goal region in a limited amount of time without a collision and in a kinematically feasible way. The algorithm's success rate depends on many factors and the difficulty of the scenarios. We use $1750\ $ CommonRoad scenarios^11^1 to evaluate the performance of the algorithm. In this evaluation, we maintain consistent settings and cost weightings for the algorithm, intentionally avoiding adjustments or fine-tuning. The results created are, therefore, from an untuned model lacking specialized behavior features, especially in edge-case scenarios. This ensures that the evaluation of performance is independent and unbiased. Fig. 7 shows the simulation results of the $1750\ $ scenarios.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-A Environment & Evaluation", "weight": 1.0} -->

Our FRENETIX planner finds in $1539\ $ scenarios a safe and valid solution and can solve the scenario. In $143\ $ scenarios, FRENETIX is causing a collision. It should be noted that incorrect predictions of vehicle movements and collisions, where the responsibility does not lie with the ego vehicle, cause around $40\ \%$ of the accidents. In $29\ $ scenarios, FRENETIX could not reach the goal within a given time limit.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B Vehicle Dynamic Interaction Scenario", "weight": 1.0} -->

We evaluate FRENETIX in two detailed scenarios: an overtaking maneuver in Fig. 8 and an overtaking maneuver with an oncoming vehicle in Fig. 9. We use different cost weight settings displayed in Table III to investigate the trajectory selection process while overtaking.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-B Vehicle Dynamic Interaction Scenario", "weight": 1.0} -->

The weightings depend on the respective cost function, meaning they can only be considered relative to their changes between different runs. In the following investigations, a distinction is made between the different weighting levels to demonstrate the performance and functionality of the algorithm. A detailed parameter analysis is not carried out, as this can be obtained from the literature. In the first study without oncoming traffic, the costs of the collision probability are varied to investigate the change in driving behavior.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-B Vehicle Dynamic Interaction Scenario", "weight": 1.0} -->

In our study, the overtaken vehicle maintains a constant speed of $13\ {m\ s^{- 1}}$. As illustrated in Fig. 8, we observe that augmenting the costs associated with collision probability leads to an increased lateral distance from overtaking vehicle. If the distance is sufficient, the cost of the collision probability decreases so much that it hardly influences the distance so that the vehicle does not move unnecessarily far from the other vehicle. This ensures that the vehicle does not deviate excessively from its reference path. Under these conditions, the overtaking velocity is influenced by the target speed. Conversely, when the costs for increased distance to an obstacle are factored, the ego vehicle stays behind the preceding vehicle instead of overtaking. This is due to the increased distance to obstacle costs to the leading vehicle, which exceeds the velocity. The trajectory planner can also manage critical situations with conflicting objectives. Fig. 9 shows the same scenario with an oncoming vehicle. The study examines the variation in velocity costs and how to handle the oncoming traffic. The velocity costs are dependent on the target speed. With high velocity costs, the vehicle accelerates significantly faster and can turn in again sooner after overtaking.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-B Vehicle Dynamic Interaction Scenario", "weight": 1.0} -->

With low velocity costs, the vehicle in front cannot be overtaken in time. The ego vehicle has to pull in again and overtake at a later timestep after $5\ s$. Nevertheless, none of the different setups results in a collision with the other vehicles. However, if we deactivate one of the two important cost functions, the vehicle fails. Collision probability costs and velocity costs are necessary to achieve the goal region.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-C Calculation time", "weight": 1.0} -->

To analyze computation times for trajectory planning, the study utilized a Dell Alienware computer equipped with an AMD 7950X processor, 128 GB RAM, and an NVIDIA GeForce RTX 4090 graphics card. We benchmark our FRENETIX C++ implementation against a FRENETIX Python implementation. We distinguish between single-core (SC) and multiprocessing (MP) since sampling-based planners are easy to parallelize. Since we are using a sampling scheme, we cannot raise the number of trajectories linearly. We investigate how much time the algorithm needs to create the trajectory samples, check the feasibility of each trajectory, and calculate their costs. We depict the results of this evaluation in Table IV.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-C Calculation time", "weight": 1.0} -->

The results reveal significant differences in calculation times between different implementations. The percentage differences between SC and MP modes were remarkably high, indicating a substantial efficiency gain in multi-processing. For instance, for $90\, 000\ $ trajectories, the time was reduced from $5.52\ s$ in SC to $0.717\ s$ in MP. In the comparative analysis of Python implementations, MP exhibits a threshold-dependent efficacy. Specifically, Python-MP demonstrates a net advantage beyond a critical number of trajectories. This is attributable to the inherent overhead associated with MP under Python, which can outweigh the computational gains when dealing with a limited set of trajectories. Conversely, the C++ implementation showcases a more efficient resource utilization.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Discussion", "weight": 1.5} -->

The results from our study indicate that the FRENETIX algorithm presented is effective in rapidly finding a safe and reliable trajectory in dynamic environments. The algorithm's modular structure allows for quickly adapting and integrating new features and modules. However, it is essential to note that specific settings and parameters influence the algorithm's performance, which is consistent with expectations for an analytical algorithm. During our research, collisions and other issues were mainly attributed to the lack of features for specific scenarios or inadequate parameter tuning. Nonetheless, the potential for optimizing vehicle behavior in various situations is achievable through further extensions. The cost functions demonstrate a variable influence on the target variables, facilitating the successful simulation of complex maneuvers, such as overtaking in the presence of oncoming traffic.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion & Outlook", "weight": 1.5} -->

In this paper, we introduced FRENETIX, a high-performance and modular sampling-based trajectory planner algorithm for autonomous driving applications We propose a composition of multiple steps and methods to create a trajectory planner that runs computationally efficiently. Therefore, FRENETIX is characterized by its robustness, adaptability, and ability to effectively handle complex scenarios. The modular approach and presented cost functions allow different prioritizations of the driving behavior by adapting the cost weights. Our results demonstrate dynamic vehicle behavior, e.g., overtaking maneuvers, especially in highly dynamic situations, including oncoming traffic. Since we open-source FRENETIX, it can provide a valuable motion planner baseline for the community, encouraging collaborative development and innovation. For further research, FRENETIX offers a solid basis for further studies, e.g. on behavior planning, reinforcement learning, or other extensions, with great potential for comprehensive benchmark analyses.
