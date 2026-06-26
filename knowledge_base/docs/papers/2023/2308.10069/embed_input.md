<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning

Topics include Integer programming, Motion planning, Vehicles, Real-time systems, Planning, Sampling, MIP-DM, Mixed-integer quadratic program, MIQP, Quadratic programming.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We develop a real-time feasible mixed-integer programming-based decision making (MIP-DM) system for automated driving. Using a linear vehicle model in a road-aligned coordinate frame, the lane change constraints, collision avoidance and traffic rules can be formulated as mixed-integer inequalities, resulting in a mixed-integer quadratic program (MIQP). The proposed MIP-DM simultaneously performs maneuver selection and trajectory generation by solving the MIQP at each sampling time instant. While solving MIQPs in real time has been considered intractable in the past, we show that our recently developed solver BB-ASIPM is capable of solving MIP-DM problems on embedded hardware in real time. The performance of this approach is illustrated in simulations in various scenarios including merging points and traffic intersections, and hardware-in-the-loop simulations on dSPACE Scalexio and MicroAutoBox-III. Finally, we present results from hardware experiments on small-scale automated vehicles.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Automated transportation systems, even in the case of partial automation, may lead to reduced road accidents and more efficient usage of the road network. However, the complexity of automated driving (AD) and advanced driver-assistance systems (ADAS) and their real-time requirements in resource-limited automotive platforms requires the implementation of a multi-layer guidance and control architecture. Thus, the ADAS/AD system consists of multiple interconnected components, including communication and sensor interfaces connecting each block and potentially executing at different sampling rates, aiming for the integrated system to satisfy the driving specifications.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A typical guidance and control architecture is illustrated in Figure 1(a), e.g., similar to. Based on a route given by a navigation system, a decision making module decides when to perform maneuvers such as lane changing, stopping, waiting, and intersection crossing. Given these decisions, a motion planning system generates a state trajectory to execute the maneuvers, and a vehicle control system computes the input signals to track the trajectory.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimization-based motion planning and control techniques, such as model predictive control (MPC), directly account for dynamics, constraints and objectives in a model-based design framework. This has been extended to hybrid systems, including both discrete and continuous decision variables. The resulting hybrid MPC can tackle a large range of problems, including switched dynamical systems, motion planning with obstacle avoidance, logic rules and temporal logic specifications. However, the mixed-integer optimal control problem (MIOCP) to be solved at each step is non-convex due to integer variables, and $\mathcal{N}\mathcal{P}$-hard. For a linear-quadratic objective, linear or piecewise-linear dynamics and inequality constraints, the MIOCP results in a mixed-integer quadratic program (MIQP).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent work indicates that, by exploiting the particular structure of the MIOCPs, real-time solvers can achieve performance comparable to commercial tools, e.g., GUROBI and MOSEK, especially for small to medium-scale problems. Therefore, we use the tailored BB-ASIPM solver, using a branch-and-bound (B&B) method with reliability branching and warm starting, block-sparse presolve techniques, early termination and infeasibility detection within a fast convex quadratic programming (QP) solver based on an active-set interior point method (ASIPM).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we design a mixed-integer programming decision making (MIP-DM) module for vehicles that simultaneously computes a sequence of discrete decisions and a continuous motion trajectory in a hybrid MPC framework. This approach eliminates the need for a separate motion planner in the ADAS/AD architecture as long as an advanced vehicle control algorithm is used, e.g., based on nonlinear MPC (NMPC), see Figure 1(b). We demonstrate the proposed MIP-DM approach in simulations in various scenarios including merging points and traffic intersections, and we confirm its real-time feasibility on dSPACE Scalexio and MicroAutoBox-III rapid prototyping units commonly used in automotive development. Finally, we present results from hardware experiments using MIP-DM in combination with NMPC-based reference tracking on a setup with small-scale automated vehicles.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Relation with Existing Literature", "weight": 1.0} -->

In the DARPA Urban Challenge, most teams implemented rule-based decision making systems involving hand-tuned heuristics for different urban-driving scenarios. Some recent works on vehicle decision making are based on machine learning, e.g., supervised or reinforcement learning, which lacks guarantees. The work in proposes the use of automata combined with set reachability, however it does not account for performance, but only for maneuver feasibility. The work in proposes a method for simultaneous trajectory generation and maneuver selection, but the complexity of the approach grows rapidly with the number of obstacles.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Relation with Existing Literature", "weight": 1.0} -->

Our prior work proposed to define traffic rules as signal temporal logic (STL) formulae that are converted into a set of mixed-integer inequalities for vehicle decision making based on the solution of MIQPs. This results in formal guarantees but using an excessively large optimization problem for real-time implementation, in part due to the automated STL formulae translation. Motivated by the latter results, the present paper proposes a real-time feasible MIQP formulation for vehicle decision making and motion planning. An overview on MIP-based decision making, motion planning and control problems may be found. Specifically for ADAS/AD systems, the works in propose MIPs for vehicle lane changing and overtaking maneuvers. To the best of our knowledge, this paper presents the first MIP for decision making with an embedded solver that is demonstrated to be real-time feasible in automotive hardware-in-the-loop (HIL) simulations and in small-scale vehicle experiments.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contributions of Present Work", "weight": 1.0} -->

A first contribution of the present paper is a detailed description of an MIQP formulation for vehicle decision making that can handle a wide range of traffic scenarios, while operating in a dynamic environment with potentially changing traffic rules. Second, we present the tailored BB-ASIPM solver and illustrate its computational performance to implement the proposed MIP-DM method, comparing against state-of-the-art software tools based on simulation results in various scenarios including merging points and traffic intersections. Third, we illustrate real-time feasibility of the approach on dSPACE Scalexio and MicroAutoBox-III rapid prototyping units. A fourth contribution includes the results from hardware experiments based on MIP-DM in combination with NMPC-based reference tracking using small-scale automated vehicles.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Outline and Notation", "weight": 1.0} -->

This paper is structured as follows. Section 2 introduces the objectives and problem formulation, followed by a detailed description of the MIP-DM method in Section 3. The embedded MIQP solver is described in Section 4, and the simulation results are shown in Section 5. Finally, Section 6 presents results from the hardware experiments and our conclusions are established in Section 7.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Setup and Formulation", "weight": 1.0} -->

This section briefly describes common components in a multi-layer guidance and control architecture for ADAS/AD, and then introduces the MIOCP formulation for MIP-DM.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Multi-layer Control Architecture for Automated Driving", "weight": 1.0} -->

A typical guidance and control architecture is illustrated in Figure 1(a). A perception, sensing and estimation module uses various on-board sensor information, such as radar, LIDAR, camera, and global positioning system (GPS) information, to estimate the vehicle states, parameters, and parts of the surroundings relevant to the driving scenario. Based on a route given by a navigation system, a decision making module determines what maneuvers to perform, e.g., lane changing, stopping, waiting, intersection crossing. Then, a motion planning system generates a collision-free and kinematically feasible trajectory to perform the maneuvers, see, e.g.,. A vehicle control system computes the input signals to execute the motion planning trajectory, see, e.g.,. Additional low-level controllers operate the vehicle actuators.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Setup for MIP-based Decision Making (MIP-DM)", "weight": 1.0} -->

In this paper, an autonomous vehicle must reach a desired destination while obeying the traffic rules. This requires the vehicle to adjust its velocity to obey the speed limits, to avoid collisions, to follow and change lanes, and to cross intersections following right of way rules. We propose an alternative architecture to that in Fig. 1(a), using MIP-based vehicle decision making, see Fig. 1(b). The problem setup in this work requires the following simplifying assumptions.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

There exists a prediction time window along which the following are known the position and orientation for each of the obstacles in a sufficiently large neighborhood of the ego vehicle, the map information, including center lines, road curvature and lane widths within the current road segment, the current traffic rules and any changes to the rules, e.g., traffic light timings and/or speed zone changes. \\QEDopen Assumption 1 ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning").1 requires the vehicle to be equipped with sensors to detect static and dynamic obstacles within a given range and to locate itself in the environment. Furthermore, the vehicle must be equipped with a module that provides conservative predictions for future trajectories of the dynamic obstacles, e.g., using techniques referenced. Assumption 1 ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning").2 requires the availability of map information and/or the use of online updates and corrections to such map information.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Assumption 1 ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning").3 requires a combination of map information, online perception, and/or vehicle-to-infrastructure (V2I) communication. Based on these assumptions, we define the problem statement and objectives.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Mixed-integer Optimal Control Problem (MIOCP)", "weight": 1.0} -->

At each sampling time instant, the proposed MIP-DM solves the following MIOCP where $i \in {\{ 0,1,\ldots,N\}}$ is the time, $N$ is the horizon length, the state variables are ${x{(i)}} \in {\mathbb{R}}^{n_{x}^{i}}$, the control and auxiliary variables are ${u{(i)}} \in {\mathbb{R}}^{n_{u}^{i}}$ and $\mathcal{I}{(i)}$ denotes the index set of integer decision variables, i.e., the cardinality ${|{\mathcal{I}{(i)}}|} \leq n_{u}^{i}$ denotes the number of integer variables at each time step.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Mixed-integer Optimal Control Problem (MIOCP)", "weight": 1.0} -->

The objective in (1a ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")) defines a linear-quadratic function with positive semi-definite Hessian matrix ${H{(i)}} \succeq 0$ and gradient vectors ${q{(i)}} \in {\mathbb{R}}^{n_{x}^{i}}$ and ${r{(i)}} \in {\mathbb{R}}^{n_{u}^{i}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Mixed-integer Optimal Control Problem (MIOCP)", "weight": 1.0} -->

The constraints include dynamic constraints in (1b ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")), simple bounds in (1c ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")), affine inequality constraints in (1d ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")) and integer feasibility constraints in (1e ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")). The initial state constraint ${x{}} = {\hat{x}}_{t}$, where ${\hat{x}}_{t}$ is a current state estimate at time $t$, can be enforced using the simple bounds in (1c ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Mixed-integer Optimal Control Problem (MIOCP)", "weight": 1.0} -->

The MIOCP (1 ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")) includes control variables on the terminal stage, ${u{(N)}} \in {\mathbb{R}}^{n_{u}^{N}}$, due to possibly needing auxiliary variables to formulate the mixed-integer inequality constraints. A binary optimization variable ${u_{j}{(i)}} \in {\{ 0,1\}}$ can be defined as an integer variable ${u_{j}{(i)}} \in {\mathbb{Z}}$ in (1e ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")), including the simple bounds $0 \leq {u_{j}{(i)}} \leq 1$ in (1c ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Mixed-integer Optimal Control Problem (MIOCP)", "weight": 1.0} -->

For compactness, we denote $X = {\lbrack{x{}^{\top}},\ldots,{x{(N)}^{\top}}\rbrack}^{\top}$ and $U = {\lbrack{u{}^{\top}},\ldots,{u{(N)}^{\top}}\rbrack}^{\top}$. The MIOCP (1 ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")) can be reformulated as a block-sparse structured MIQP, and solved with corresponding algorithms.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning", "weight": 1.0} -->

Next, we describe the MIP-DM for achieving safe and real-time feasible automated driving in real-world scenarios.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Linear Vehicle Model in Road-aligned Frame", "weight": 1.0} -->

The curvilinear coordinate system used in the prediction model of the MIOCP (1 ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")) is shown in Fig. 2. A similar coordinate system has been used for predictive control, e.g.,. The vehicle position is described by $(p_{s},p_{n})$, where $p_{s}$ denotes the progress along the center line of the lane in which the ego vehicle is driving, and $p_{n}$ denotes the normal distance of the vehicle position from the center line.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

The turning radius is much larger than the wheelbase of the vehicle, such that the steering and slip angles are relatively small and their difference for the outside and inside wheels is negligible. \\QEDopen Based on Ass. 3, which is common in vehicle motion planning, we use a simplified linear vehicle model in the curvilinear coordinate system and with decoupled longitudinal and lateral kinematics where the control inputs are the longitudinal acceleration $a_{s}{(i)}$ and the lateral velocity $v_{n}{(i)}$ at each time step $i \in {\mathbb{Z}}_{0}^{N - 1}$. To approximate the nonholonomic constraints of Ackerman steering for vehicles, we enforce the linear inequality constraint on the lateral and longitudinal velocity where $\alpha > 0$, and we assume ${v_{s}{(i)}} \geq 0$ at all time steps.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Given a time varying road radius $R{(i)}$, which may be positive or negative depending on the direction of the road curvature, the lateral velocity in is bounded as ${v_{n}{(i)}} \leq {v_{y}^{\max} - {v_{y}^{R}{(i)}}}$, where $v_{y}^{\max} = {v\alpha_{R}^{\max}}$, and ${v_{y}^{R}{(i)}} = {v\alpha_{R}{(i)}}$ denotes the steady state lateral velocity to follow the center of the road with radius $R{(i)}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Eq. may be replaced by where $\alpha_{R}^{\max} = \frac{l_{r}}{R^{\min}} > 0$ defines the maximum steering and ${\alpha_{R}{(i)}} = \frac{l_{r}}{R{(i)}}$ defines the steering needed to follow the center of the road with radius $R{(i)}$, following Proposition 4. \\QEDopen

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 6", "weight": 1.0} -->

Proposition 4 uses a simple approximation of the steady-state cornering equations in \[33, Sec. 3.3\]. Alternatively, the cornering equations could be directly used to compute a time-varying value for $\alpha{(i)}$ that depends on the predicted velocity and the road curvature. \\QEDopen

<!-- chunk {"id": "body-0028", "role": "body", "section": "Lane Change and Timing Delay Constraints", "weight": 1.0} -->

We enforce lane bound constraints where $w_{l}$ denotes a lane width given by the map and $p_{n}^{ref} \in {\mathbb{R}}$ is an auxiliary state variable that denotes the lateral position of the center line of the current lane of the vehicle. For equal lane width values $w_{l}$, the vehicle is in lane $j$ if $p_{n}^{ref} = {{({j - 1})}w_{l}}$ for $j \in {\{ 1,\ldots,n_{l}\}}$, where $n_{l}$ is the number of lanes in the current traffic scenario.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Lane Change and Timing Delay Constraints", "weight": 1.0} -->

Even though the reference lane value may jump from one time step $p_{n}^{ref}{(i)}$ to the next $p_{n}^{ref}{({i + 1})}$, it may take multiple time steps for the lateral position to transition from the center line of one lane to the next, i.e., ${p_{n}{({i - l})}} \approx {p_{n}^{ref}{(i)}}$ and ${p_{n}{({i + k})}} \approx {p_{n}^{ref}{({i + 1})}}$, where $l \geq 0$ and $k \geq 1$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Timing Delay Constraints for Lane Changes", "weight": 1.0} -->

Given $t_{c}{(i)}$, we impose a minimum time between lane changes i.e., ${\delta_{c}^{u}{(i)}} = 1$ or ${\delta_{c}^{d}{(i)}} = 1$ only if ${t_{c}{(i)}} \geq t_{\min}$. In a receding horizon implementation of the MIP-DM, the timer $t_{c}{}$ is initialized to the value from the previous time step.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Polyhedral Obstacle Avoidance Constraints", "weight": 1.0} -->

The MIP-DM enforces obstacle avoidance constraints to avoid a region of collision risk around other traffic participants, e.g., vehicles, bicycles or pedestrians. The position and dimensions of the safety region may be time varying and adapted to a prediction of the behavior for each of the traffic participants. In addition, obstacle avoidance constraints enforce stopping maneuvers, e.g., in case of a stop sign or a red traffic light at an intersection. Per Assumption 1 ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning"), the prediction of obstacle motions, the map information and the traffic rules are known. For simplicity, we use axis-aligned rectangular collision regions, as illustrated in Figure 3. Alternatively, any polyhedral representation of the collision regions could be used, see, e.g.,. The size of the collision region around the obstacle is increased with the geometric shape of the ego vehicle and includes an additional safety margin for robustness to discretization errors, model mismatch and/or disturbances.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 8", "weight": 1.0} -->

For each obstacle $j \in {\mathbb{Z}}_{1}^{n_{obs}}$, we predict its position based on a constant velocity profile in curvilinear coordinates. Future work may include the use of a more advanced prediction model, e.g., a switching dynamical model or a neural network classifier. \\QEDopen

<!-- chunk {"id": "body-0033", "role": "body", "section": "Traffic Intersection Crossing Constraints", "weight": 1.0} -->

The obstacle avoidance constraints in are also used to prevent the ego vehicle from crossing a traffic intersection, e.g., forcing the vehicle to stop during a particular time window. Similar to Fig. 3, the avoidance region is defined by the dimensions of the intersection, enlarged to account for the physical shape of the ego vehicle and with additional safety margins to account for modeling errors. If the intersection is controlled by traffic lights and if the traffic light changes are known, e.g., using V2I communication, the intersection crossing constraints are time-varying within the prediction horizon. For example, if it is known that a traffic light will turn red, the intersection crossing constraints cause the ego vehicle to slow down and plan a stopping maneuver. Similarly, the constraints are relaxed at future time steps within the prediction horizon when the traffic lights are predicted to become green. Alternatively, the intersection crossing constraints may be implemented based on map information and/or the perception system.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Zone-dependent Traffic Rules", "weight": 1.0} -->

In real-world scenarios, traffic rules may change when the vehicle transitions into a particular zone. From one zone to the next, following traffic rule constraints may change speed limit, e.g., the vehicle entering a low-speed zone, allowed lane changes, e.g., when no lane changes are allowed inside a particular zone, available lanes, e.g., when a three-lane road transitions into a two-lane road or when the vehicle must merge.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Zone-dependent Traffic Rules", "weight": 1.0} -->

We introduce binary variables $\delta_{z} = {\lbrack\delta_{z}^{1},\ldots,\delta_{z}^{n_{z}}\rbrack}$, where $n_{z}$ denotes the number of position-dependent zones. Each zone is represented by a range $\lbrack{\underset{¯}{p}}_{j},{\overline{p}}_{j}\rbrack$ for $j \in {\mathbb{Z}}_{1}^{n_{z}}$ in the longitudinal $p_{s}$-direction. We detect whether the vehicle is in zone $j$ as which can be implemented as Because the position-dependent zones are disjoint, the vehicle needs to be inside exactly one zone, i.e., ${\sum_{j = 1}^{n_{z}}\delta_{z}^{j}} = 1$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Zone-dependent Traffic Rules", "weight": 1.0} -->

The auxiliary binary variables $\delta_{z}$ and constraints in enable implementing the zone-dependent traffic rules. For example, changing speed limits can be enforced by where the speed limit ${\overline{v}}_{s}^{j}{(i)}$ corresponds to zone $j = {1,\ldots,n_{z}}$ and ${\sum_{j = 1}^{n_{z}}\delta_{z}^{j}} = 1$. Similarly, the allowed number of lane changes can be adjusted as and the constraints on feasible lanes can be adjusted as Figure 4 shows the transition from a three-lane road segment into a two-lane road segment using.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Extended Dynamic System with Auxiliary Variables", "weight": 1.0} -->

For the prediction model (1b ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")), the vehicle kinematics and the auxiliary dynamics result in the augmented system The MIP-DM also enforces simple bounds on state variables at each time step $i \in {\mathbb{Z}}_{0}^{N}$ and simple bounds on control inputs for $i \in {\mathbb{Z}}_{0}^{N - 1}$

<!-- chunk {"id": "body-0038", "role": "body", "section": "Objective for Decision Making and Motion Planning", "weight": 1.0} -->

The first term in is the longitudinal tracking error with respect to a reference trajectory ${\overline{p}}_{s}^{ref}{(i)}$, e.g., computed based on a desired reference velocity. The second term minimizes the lateral tracking error with respect to the current center lane. The third and fourth terms penalize the control actions, i.e., the longitudinal acceleration and lateral velocities, respectively. The fifth term penalizes lane change decisions.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Objective for Decision Making and Motion Planning", "weight": 1.0} -->

The sixth term in minimizes a tracking error of the current lane with respect to a given preferred lane value ${\overline{p}}_{n}^{ref}{(i)}$, e.g., the right lane in right-hand traffic or the left most lane when a vehicle desires to make a left turn at a next traffic intersection. To handle the absolute value, we minimize an auxiliary control variable $\Deltap_{n}^{ref}$, satisfying such that ${\Deltap_{n}^{ref}} \geq {|{p_{n}^{ref} - {\overline{p}}_{n}^{ref}}|}$ holds. The squared terms in may be replaced by absolute values which results in a mixed-integer linear program (MILP) instead of an MIQP. The last term in corresponds to a penalty on the slack variables for soft constraint violations.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Objective for Decision Making and Motion Planning", "weight": 1.0} -->

The weight $w_{7} \gg 0$ is chosen large enough to ensure that a feasible solution with ${\nu^{c}{(i)}} = 0$ is found if and when it exists.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 9", "weight": 1.0} -->

By defining an upper bound on the number of other vehicles for obstacle avoidance in a realistic traffic environment, the MIOCP has fixed dimensions that allows for static memory allocation in an embedded implementation of the MIP-DM for microprocessors suitable to automotive applications, as discussed later. \\QEDopen

<!-- chunk {"id": "body-0042", "role": "body", "section": "Embedded MIQP Solver for Mixed-Integer Model Predictive Control", "weight": 1.0} -->

The MIOCP is converted into the MIQP where $\mathbf{z}$ includes all optimization variables and the index set $\mathcal{I}$ denotes the integer variables. Next, we summarize the main ingredients of the BB-ASIPM solver that uses a B&B method with reliability branching and warm starting, block-sparse presolve techniques, early termination and infeasibility detection within a fast convex QP solver.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Branch-and-bound Method and Search Heuristics", "weight": 1.0} -->

The B&B algorithm sequentially creates partitions of the original MIQP problem as shown in Figure 5. For each partition, a local lower bound on the optimal objective value is obtained by solving a convex relaxation of the MIQP subproblem. If the relaxation yields an integer-feasible solution, the B&B updates the global upper bound for the MIQP solution, which is used to *prune* tree partitions. The B&B method terminates when the difference between the upper and lower bound is below a user-defined threshold. A key decision of the B&B procedure is how to create partitions, i.e., which node to choose and which discrete variable to select for branching. BB-ASIPM uses *reliability branching* which combines strong branching and pseudo-costs.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Tailored Exact Presolve Reduction Techniques", "weight": 1.0} -->

We refer to the parametric MIQP from as $\mathcal{P}{(\theta)}$, in which the parameter vector $\theta$ includes the state estimate ${\hat{x}}_{t}$, and we denote the discrete variables in (26c) by $\delta \in {\mathbb{Z}}^{N_{\delta}}$. We use the compact notation $\mathcal{P}{({{\theta,\delta_{\mathcal{R}}} = \hat{\delta}})}$ to denote the MIQP after fixing ${\delta_{j} = {\hat{\delta}}_{j}},{j \in \mathcal{R}}$ where $\mathcal{R}$ is an index set.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Block-sparse QP solver for Convex Relaxations", "weight": 1.0} -->

A primal-dual interior point method (IPM) uses a Newton-type algorithm to solve a sequence of relaxed Karush-Kuhn-Tucker (KKT) conditions for the convex QP. We use the active-set based inexact Newton implementation of ASIPM, which exploits the block-sparse structure in the linear system, with improved numerical conditioning, reduced matrix factorization updates, warm starting, early termination and infeasibility detection. If the convex QP relaxation has optimal value that exceeds the current global upper bound in the B&B method, the node and corresponding subtree can be pruned from the B&B tree. A considerable computational effort can be avoided if the above scenarios are detected early, i.e., more quickly than solving the convex QPs. In, we describe an early termination method based on a tailored dual feasibility projection strategy applicable to BB-ASIPM to handle both cases and to reduce the computational effort of the B&B method without affecting the quality of the optimal solution.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Embedded Software Implementation for Hybrid MPC", "weight": 1.0} -->

In hybrid MPC, warm starting can be used to reduce the computational effort in the B&B method from one time step to the next as discussed. BB-ASIPM uses *tree propagation* to efficiently reuse the branching decisions and pseudo-costs from the previous MIQP solution. An upper bound can be imposed on the number of B&B iterations to ensure a maximum computation time below a threshold. If an integer-feasible solution is found, a B&B method automatically provides a bound on the suboptimality of this MIQP solution. The BB-ASIPM solver is implemented in self-contained C code, which allows for real-time implementations on embedded microprocessors as shown next.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Numerical Simulation Results", "weight": 1.0} -->

We present numerical simulation results for the MIP-DM described in Section 3, in a variety of traffic scenarios. We also compare the BB-ASIPM solver from Section 4 against state-of-the-art software tools, and we demonstrate its real-time feasibility on dSPACE rapid prototyping units.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Problem Formulation and Simulation Test Scenarios", "weight": 1.0} -->

\raisebox{-.9pt} {1}⃝ see Fig. 6(a) \raisebox{-.9pt} {2}⃝ see Fig. 6(b) \raisebox{-.9pt} {3}⃝ see Fig. 6(c) \raisebox{-.9pt} {4}⃝ see Fig. 6(d) \raisebox{-.9pt} {5}⃝ see Fig. 6(e) \raisebox{-.9pt} {6}⃝ see Fig. 6(f) \raisebox{-.9pt} {7}⃝ see Fig. 6(g) \raisebox{-.9pt} {8}⃝ see Fig. 6(h) Table 1: Problem dimensions and parameters in MIQP formulation of Section 3 for each of the test scenarios in Fig. 6. The number of binary variables per time step in the MIOCP prediction time horizon is nδ = 2 + 3 nobs + nz.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Problem Formulation and Simulation Test Scenarios", "weight": 1.0} -->

(a) Scenario 1: ego vehicle overtaking three obstacles on a road with one-way traffic.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Problem Formulation and Simulation Test Scenarios", "weight": 1.0} -->

(b) Scenario 2: ego vehicle swaying for two parked vehicles (only one visible), avoiding a third vehicle on other lane with one-way traffic.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Problem Formulation and Simulation Test Scenarios", "weight": 1.0} -->

(c) Scenario 3: ego vehicle overtaking before stopping at intersection, then ego continues after two vehicles finish crossing intersection.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Problem Formulation and Simulation Test Scenarios", "weight": 1.0} -->

(d) Scenario 4: ego vehicle overtaking obstacles on a curved road with one-way traffic, followed by stopping and crossing an intersection.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Problem Formulation and Simulation Test Scenarios", "weight": 1.0} -->

(e) Scenario 5: ego vehicle merging to lane 2 between three vehicles with one-way traffic.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Problem Formulation and Simulation Test Scenarios", "weight": 1.0} -->

(f) Scenario 6: ego vehicle merging at the end of lane onto a new lane while avoiding / overtaking three vehicles (only one visible).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Problem Formulation and Simulation Test Scenarios", "weight": 1.0} -->

(g) Scenario 7: ego vehicle performs right turn at a T-intersection, merging between two vehicles (only one visible) on same lane of the road segment.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Problem Formulation and Simulation Test Scenarios", "weight": 1.0} -->

(h) Scenario 8: ego vehicle turns left at T-intersection, following one vehicle while avoiding two other vehicles driving in the opposite direction.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Problem Formulation and Simulation Test Scenarios", "weight": 1.0} -->

Scenario 1 in Fig. 6(a) shows the ego vehicle overtaking three obstacles, where two obstacles are on lane 1 and a third obstacle is on lane 2, on a road segment with one-way traffic. Lane 1 refers to the right most lane with respect to the ego vehicle's direction of motion. Scenario 2 in Fig. 6(b) shows the ego vehicle swaying around two parked vehicles (with zero velocity) on lane 1, while avoiding a third vehicle on lane 2. Scenario 3 in Fig. 6(c) shows the ego vehicle overtaking one vehicle on lane 1 before stopping at a traffic intersection, then crossing after two other vehicles. Scenario 4 in Fig. 6(d) shows the ego vehicle overtaking three obstacles (two vehicles on lane 1 and one vehicle on lane 2) on a curved road segment with one-way traffic, followed by stopping and crossing an intersection. In the test scenarios 1-4, lane 1 is the preferred lane ${\overline{p}}_{n}^{ref}$, so that the ego vehicle always returns to lane 1 after each overtaking or sway maneuver.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Problem Formulation and Simulation Test Scenarios", "weight": 1.0} -->

Scenario 5 in Fig. 6(e) shows the ego vehicle merging from lane 1 to lane 2 between three vehicles on lane 2, i.e., the preferred lane ${\overline{p}}_{n}^{ref}$ in is lane 2. Scenario 6 in Fig. 6(f) shows the ego vehicle merging at the end of a current lane onto a new lane while avoiding and/or overtaking three vehicles that are driving on the same lane. Scenario 7 in Fig. 6(g) shows the ego vehicle performing a right turn at a T-intersection, merging between two vehicles on the same lane of the new road segment. Scenario 8 in Fig. 6(h) shows the ego vehicle performing a left turn at a T-intersection, following one vehicle on the same lane while avoiding two other vehicles driving in the opposite direction. In the test scenarios 5-8, after a merging or turning maneuver, the ego vehicle overtakes any other vehicle that is driving below the speed limit.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Computational Performance and Solver Comparisons", "weight": 1.0} -->

\raisebox{-.9pt} {1}⃝ see Fig. 6(a) \raisebox{-.9pt} {2}⃝ see Fig. 6(b) \raisebox{-.9pt} {3}⃝ see Fig. 6(c) \raisebox{-.9pt} {4}⃝ see Fig. 6(d) \raisebox{-.9pt} {5}⃝ see Fig. 6(e) \raisebox{-.9pt} {6}⃝ see Fig. 6(f) \raisebox{-.9pt} {7}⃝ see Fig. 6(g) \raisebox{-.9pt} {8}⃝ see Fig. 6(h) Table 2 shows the average and worst-case computation times of MIP-DM for each of the $8$ simulation scenarios that are illustrated in Figure 6, using the MIQP formulation as described in Section 3 and where the MIQPs at each control time step are solved using either GUROBI, MOSEK or BB-ASIPM.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Computational Performance and Solver Comparisons", "weight": 1.0} -->

It can be observed that the average and worst-case computation times of BB-ASIPM are approximately $6$ and $5$ times faster than MOSEK, respectively. On the other hand, the average and worst-case computation times of GUROBI are approximately $1.5$ and $2.5$ times faster than BB-ASIPM, respectively. Note that all default presolve options are enabled in the GUROBI solver.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Computational Performance and Solver Comparisons", "weight": 1.0} -->

Given the relatively simple and compact algorithmic implementation in BB-ASIPM, e.g., compared to the extensive collection of advanced heuristics, presolve and cutting plane techniques in the commercial GUROBI solver, it is reassuring to see that the tailored BB-ASIPM solver can remain competitive with state-of-the-art software tools in Table 2. The software implementation of BB-ASIPM is relatively compact and self-contained such that it can execute on an embedded microprocessor for real-time vehicle decision making and motion planning. Instead, state-of-the-art optimization tools, such as GUROBI and MOSEK typically cannot be used on embedded control hardware with limited computational resources and available memory.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Hardware-in-the-loop Simulation Results on dSPACE Scalexio and MicroAutoBox-III Rapid Prototyping Units", "weight": 1.0} -->

Next, we present detailed results of running hardware-in-the-loop simulations for each of the $8$ test scenarios shown in Figure 6 on both the dSPACE Scalexio^11^1dSPACE Scalexio DS6001 unit, with an Intel i7-6820EQ quad-core $2.8$ GHz processor with 64 kB L1 cache per core, 256 kB L2 cache per core, 8 MB shared L3 cache, 4 GB DDR4 RAM, and 8 GB flash memory. In the presented results, MIP-DM executes in a single core. and the dSPACE MicroAutoBox-III (MABX-III)^22^2dSPACE MicroAutoBox-III DS1403 unit, with four ARM Cortex-A15 processor cores with 32 kB L1 cache per core, 4 MB shared L2 cache, 2 GB DDR3L RAM, and 64 MB flash memory. In the presented results, MIP-DM executes in a single core. rapid prototyping units.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Hardware-in-the-loop Simulation Results on dSPACE Scalexio and MicroAutoBox-III Rapid Prototyping Units", "weight": 1.0} -->

Table 3 shows the average and worst-case computation times, the number of B&B iterations, total number of ASIPM iterations, and the memory usage of the BB-ASIPM solver on Scalexio and MABX-III. The memory usage is categorized into *text* that contains code and constant data, which is typically stored in ROM, and *data* that is stored in RAM.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Hardware-in-the-loop Simulation Results on dSPACE Scalexio and MicroAutoBox-III Rapid Prototyping Units", "weight": 1.0} -->

From Table 3, MIP-DM is real-time feasible using the proposed BB-ASIPM solver for each of the $8$ simulation scenarios on both the dSPACE Scalexio and MABX-III units, as the worst-case computation time is below the sampling time of $T_{s} = 1$ s at each time step. More specifically, considering all test scenarios, the computation times on the dSPACE Scalexio are always below $200$ ms, below $100$ ms $99$% of the times, and the average is only $17.3$ ms. On MABX-III, the computation times are always below $800$ ms, below $400$ ms $99$% of the times, and the average is only $76.3$ ms. The total memory usage is approximately $18$ MB on Scalexio and $16.1$ MB on MABX-III, due to the different compilers. As expected, for each test scenario, Table 3 shows that the number of iterations on Scalexio and MABX-III is identical.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Hardware-in-the-loop Simulation Results on dSPACE Scalexio and MicroAutoBox-III Rapid Prototyping Units", "weight": 1.0} -->

BB-ASIPM on dSPACE Scalexio BB-ASIPM on dSPACE MABX-III \raisebox{-.9pt} {1}⃝ see Fig. 6(a) \raisebox{-.9pt} {2}⃝ see Fig. 6(b) \raisebox{-.9pt} {3}⃝ see Fig. 6(c) \raisebox{-.9pt} {4}⃝ see Fig. 6(d) \raisebox{-.9pt} {5}⃝ see Fig. 6(e) \raisebox{-.9pt} {6}⃝ see Fig. 6(f) \raisebox{-.9pt} {7}⃝ see Fig. 6(g) \raisebox{-.9pt} {8}⃝ see Fig. 6(h)

<!-- chunk {"id": "body-0066", "role": "body", "section": "Experimental Results of MIP-DM and NMPC on Small-scale Automated Vehicles", "weight": 1.0} -->

Next, we validate the performance of MIP-DM on experiments with small-scale vehicles, using ROS and an Optitrack motion-capture system. First, we briefly present the hardware and software setup, then we describe the integration of MIP-DM with a nonlinear MPC (NMPC) for reference tracking, and finally we show the experiment results.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Hardware Setup and Software Implementation", "weight": 1.0} -->

(c) Experiments using three small-scale vehicles: the ego vehicle (blue flag) executing the MIP-DM and NMPC, and two obstacles (no flag).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Hardware Setup and Software Implementation", "weight": 1.0} -->

The hardware setup is illustrated in Figure 7. It includes a *Hamster* vehicle in Fig. 7(a), a $25 \times 20$ cm mobile robot with electric steering and electric motor speed control. The robot is equipped with sensors such as a rotating $360$ deg Lidar, an inertial measurement unit, GPS receiver, HD camera, and motor encoders. It has Ackermann steering and its kinematic behavior emulates that of a regular vehicle. To evaluate the performance of the automated driving system, we use an Optitrack motion-capture system, see Fig. 7(b), to obtain position and orientation measurements for each of the Hamster vehicles. Depending on the environment and quality of the calibration, the Optitrack system can track the position for each of the Hamster vehicles within $1$ cm and with an orientation error of less than $3$ deg.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Hardware Setup and Software Implementation", "weight": 1.0} -->

Our experimental setup consists of three vehicles driving on a two-lane track shaped as a figure eight, resulting in a traffic intersection as shown in Fig. 7(c). Two Hamsters are designated as *obstacles*, executing a standard PID controller that tracks the center line of the current lane. A traffic intersection coordinator forces each of the obstacles to stop in front of the intersection for at least three seconds before continuing the execution of the PID lane keeping controller when the intersection is free. The third Hamster is the ego vehicle that is controlled by the multi-layer control architecture shown in Figure 8, i.e., the proposed MIP-DM method in combination with an NMPC for reference tracking as described in the next section. Each of the components in Fig. 8 is executed in a separate ROS node on a single dedicated desktop computer^33^3The desktop for vehicle experiments is equipped with an Intel i7-6900K CPU @ 3.20GHz $\times 8$ processor, 64 GB RAM, and Ubuntu 16.04 LTS..

<!-- chunk {"id": "body-0070", "role": "body", "section": "Integration of MIP-DM and NMPC Tracking Controller", "weight": 1.0} -->

For the NMPC prediction model, we use the nonlinear kinematic model with additional actuation dynamics as, resulting in the continuous time dynamics where $p_{X},p_{Y}$ is the longitudinal and lateral position in the world frame, $\psi$ is the heading angle and $\overset{˙}{\psi}$ the heading rate, $v$ is the longitudinal velocity, $\delta$ and $\delta_{f}$ are the commanded and actual front wheel steering angle, respectively, and $L,\beta$ are defined as. First order front steering dynamics are included in for the steering actuation response. In addition, we estimate the offset value $\delta_{o}$ for the steering angle online using an extended Kalman filter (EKF), which also compensates for unmodeled disturbances, see Fig. 8. The inputs $u_{1},u_{2}$ are the acceleration and steering rate, respectively.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Integration of MIP-DM and NMPC Tracking Controller", "weight": 1.0} -->

At each control time step $t$, the NMPC solves where the $N^{mpc}$ control intervals are defined by an equidistant grid of time points $t_{k} = {k\frac{T^{mpc}}{N^{mpc}}}$ for $k \in {\mathbb{Z}}_{0}^{N^{mpc}}$ over the NMPC horizon, ${\hat{x}}_{t}$ is the current state estimate from the EKF at time $t$, and the constraints in (29d) are a discretization of the continuous time dynamics in using a $4^{\text{th}}$ order Runge-Kutta method.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Integration of MIP-DM and NMPC Tracking Controller", "weight": 1.0} -->

We introduce a nonnegative slack variable ${\nu{(k)}} \geq 0$ for implementing the $L_{1}$ penalty, and the weight $r_{\nu} \gg 0$ is chosen sufficiently large to ensure that ${\nu{(k)}} = 0$ when a feasible solution exists.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Integration of MIP-DM and NMPC Tracking Controller", "weight": 1.0} -->

Constraints (29e) include hard bounds on the control inputs and soft constraints for limiting the distance to the reference trajectory, the velocity and the steering angle In NMPC, obstacle avoidance is enforced by ellipsoidal constraints that approximate the rectangular collision region for each obstacle in the MIP-DM, see Fig. 3, where $\begin{bmatrix} \end{bmatrix} = {R{(o_{\psi,j})}^{\top}\begin{bmatrix} \end{bmatrix}}$ is the rotated distance, $(o_{X,j},o_{Y,j},o_{\psi,j})$ is the obstacle's pose, and $(a_{x,j},a_{y,j})$ are the lengths of the principal semi-axes of the ellipsoid that ensure a safety margin around each obstacle.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Integration of MIP-DM and NMPC Tracking Controller", "weight": 1.0} -->

The nonlinear OCP includes $n_{x} = 6$ states, $n_{u} = 3$ control inputs and $N^{mpc} = 80$ control intervals with a sampling period of $T_{s}^{mpc} = 25$ ms over a $T^{mpc} = 2$ s horizon length. The NMPC controller is implemented with a sampling frequency of $40$ Hz, using the real-time iteration (RTI) algorithm in the ACADO code generation tool and the PRESAS QP solver. The sampling period of MIP-DM is reduced with respect to that of Section 5 due to the scaling of the vehicles. MIP-DM executes with a sampling period of $T_{s}^{mip} = 0.3$ s and horizon length $N^{mip} = 15$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Experimental Results using Small-scale Vehicles", "weight": 1.0} -->

Based on the MIP-DM in Section 3, the capabilities of the ego vehicle include lane selection, lane change execution, swaying maneuvers, queuing behavior and stopping / crossing at the traffic intersection. Based on the zone constraints in the MIP (see Section 3.4), we implement a traffic rule that the ego vehicle is only allowed to make lane changes in the bottom right loop of the figure eight track (see Fig. 7(c)).

<!-- chunk {"id": "body-0076", "role": "body", "section": "Experimental Results using Small-scale Vehicles", "weight": 1.0} -->

Fig. 9(a) shows the trajectories for MIP-DM and NMPC at $26$ s in the experiment, demonstrating the ego vehicle stopping at the traffic intersection. After the obstacle (Hamster $3$) finishes crossing the intersection, the ego continues by crossing the intersection at $33$ s in the experiment. Fig. 9(b) shows the trajectories at $61$ s, demonstrating the ego changing lane and overtaking a slower obstacle to achieve the desired velocity of $0.4$ m/s. Fig. 9(c) shows the trajectories at $69$ s, demonstrating the ego changing lane back to the preferred lane after overtaking the slower obstacle. Finally, Fig. 9(d) shows the trajectories at $183$ s in the experiment, demonstrating the ego queuing behind a slower obstacle because overtaking is not allowed in the top left loop of the figure eight track.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Experimental Results using Small-scale Vehicles", "weight": 1.0} -->

(a) Trajectories for MIP-DM and NMPC at 26 s of experiment: ego vehicle stopping at traffic intersection.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Experimental Results using Small-scale Vehicles", "weight": 1.0} -->

(b) Trajectories for MIP-DM and NMPC at 61 s of experiment: ego vehicle overtaking slower obstacle to achieve desired velocity.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Experimental Results using Small-scale Vehicles", "weight": 1.0} -->

(c) Trajectories for MIP-DM and NMPC at 69 s of experiment: ego vehicle returning to preferred lane after overtaking slower obstacle.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Experimental Results using Small-scale Vehicles", "weight": 1.0} -->

(d) Trajectories for MIP-DM and NMPC at 183 s of experiment: ego vehicle slowing down behind slower obstacle because overtaking is not allowed.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Conclusions and Outlook", "weight": 1.0} -->

We designed a mixed-integer programming-based decision making for automated driving. The mixed-integer quadratic programming formulation uses a linear vehicle model in a road-aligned coordinate frame, it includes lane selection and lane change timing constraints, polyhedral collision avoidance and intersection crossing constraints, and zone-dependent traffic rule changes. We leveraged the recently developed embedded BB-ASIPM solver, using a branch-and-bound method with reliability branching and warm starting, block-sparse tailored presolve techniques, early termination and infeasibility detection within an active-set interior point method. The performance of the MIP-DM method was demonstrated by simulations in various scenarios including merging points and traffic intersections, and real-time feasibility was demonstrated by hardware-in-the-loop simulations on dSPACE Scalexio and MicroAutoBox-III rapid prototyping units. Finally, we presented results from experiments on a setup with small-scale vehicles, integrating the MIP-DM with a nonlinear model predictive control for reference tracking.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Conclusions and Outlook", "weight": 1.0} -->

Future works will focus on using more advanced behavior prediction models for other vehicles and explicit handling of uncertainty in the modeling and perception of the environment, as well as deployment on full scale vehicles.
