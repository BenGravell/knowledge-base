## Introduction

Automated transportation systems, even in the case of partial automation, may lead to reduced road accidents and more efficient usage of the road network. However, the complexity of automated driving (AD) and advanced driver-assistance systems (ADAS) and their real-time requirements in resource-limited automotive platforms requires the implementation of a multi-layer guidance and control architecture. Thus, the ADAS/AD system consists of multiple interconnected components, including communication and sensor interfaces connecting each block and potentially executing at different sampling rates, aiming for the integrated system to satisfy the driving specifications.

A typical guidance and control architecture is illustrated in Figure 1(a), e.g., similar to. Based on a route given by a navigation system, a decision making module decides when to perform maneuvers such as lane changing, stopping, waiting, and intersection crossing. Given these decisions, a motion planning system generates a state trajectory to execute the maneuvers, and a vehicle control system computes the input signals to track the trajectory.

Optimization-based motion planning and control techniques, such as model predictive control (MPC), directly account for dynamics, constraints and objectives in a model-based design framework. This has been extended to hybrid systems, including both discrete and continuous decision variables. The resulting hybrid MPC can tackle a large range of problems, including switched dynamical systems, motion planning with obstacle avoidance, logic rules and temporal logic specifications. However, the mixed-integer optimal control problem (MIOCP) to be solved at each step is non-convex due to integer variables, and $\mathcal{N}\mathcal{P}$-hard. For a linear-quadratic objective, linear or piecewise-linear dynamics and inequality constraints, the MIOCP results in a mixed-integer quadratic program (MIQP).

Recent work indicates that, by exploiting the particular structure of the MIOCPs, real-time solvers can achieve performance comparable to commercial tools, e.g., GUROBI and MOSEK, especially for small to medium-scale problems. Therefore, we use the tailored BB-ASIPM solver, using a branch-and-bound (B&B) method with reliability branching and warm starting, block-sparse presolve techniques, early termination and infeasibility detection within a fast convex quadratic programming (QP) solver based on an active-set interior point method (ASIPM).

In this paper, we design a mixed-integer programming decision making (MIP-DM) module for vehicles that simultaneously computes a sequence of discrete decisions and a continuous motion trajectory in a hybrid MPC framework. This approach eliminates the need for a separate motion planner in the ADAS/AD architecture as long as an advanced vehicle control algorithm is used, e.g., based on nonlinear MPC (NMPC), see Figure 1(b). We demonstrate the proposed MIP-DM approach in simulations in various scenarios including merging points and traffic intersections, and we confirm its real-time feasibility on dSPACE Scalexio and MicroAutoBox-III rapid prototyping units commonly used in automotive development. Finally, we present results from hardware experiments using MIP-DM in combination with NMPC-based reference tracking on a setup with small-scale automated vehicles.

### Relation with Existing Literature

In the DARPA Urban Challenge, most teams implemented rule-based decision making systems involving hand-tuned heuristics for different urban-driving scenarios. Some recent works on vehicle decision making are based on machine learning, e.g., supervised or reinforcement learning, which lacks guarantees. The work in proposes the use of automata combined with set reachability, however it does not account for performance, but only for maneuver feasibility. The work in proposes a method for simultaneous trajectory generation and maneuver selection, but the complexity of the approach grows rapidly with the number of obstacles.

Our prior work proposed to define traffic rules as signal temporal logic (STL) formulae that are converted into a set of mixed-integer inequalities for vehicle decision making based on the solution of MIQPs. This results in formal guarantees but using an excessively large optimization problem for real-time implementation, in part due to the automated STL formulae translation. Motivated by the latter results, the present paper proposes a real-time feasible MIQP formulation for vehicle decision making and motion planning. An overview on MIP-based decision making, motion planning and control problems may be found in. Specifically for ADAS/AD systems, the works in propose MIPs for vehicle lane changing and overtaking maneuvers. To the best of our knowledge, this paper presents the first MIP for decision making with an embedded solver that is demonstrated to be real-time feasible in automotive hardware-in-the-loop (HIL) simulations and in small-scale vehicle experiments.

### Contributions of Present Work

A first contribution of the present paper is a detailed description of an MIQP formulation for vehicle decision making that can handle a wide range of traffic scenarios, while operating in a dynamic environment with potentially changing traffic rules. Second, we present the tailored BB-ASIPM solver and illustrate its computational performance to implement the proposed MIP-DM method, comparing against state-of-the-art software tools based on simulation results in various scenarios including merging points and traffic intersections. Third, we illustrate real-time feasibility of the approach on dSPACE Scalexio and MicroAutoBox-III rapid prototyping units. A fourth contribution includes the results from hardware experiments based on MIP-DM in combination with NMPC-based reference tracking using small-scale automated vehicles.

### Outline and Notation

This paper is structured as follows. Section 2 introduces the objectives and problem formulation, followed by a detailed description of the MIP-DM method in Section 3. The embedded MIQP solver is described in Section 4, and the simulation results are shown in Section 5. Finally, Section 6 presents results from the hardware experiments and our conclusions are established in Section 7.

Notation: $\mathbb{R}$, ${\mathbb{R}}_{+}$, ${\mathbb{R}}_{0 +}$ ($\mathbb{Z}$, ${\mathbb{Z}}_{+}$, ${\mathbb{Z}}_{0 +}$) are the set of real, positive real and nonnegative real (integer) numbers, ${\mathbb{B}} = {\{ 0,1\}}$, and ${\mathbb{Z}}_{a}^{b} = {\{ a,{a + 1},\ldots,{b - 1},b\}}$. The logical operators and, or, xor, not are $\land$, $\vee$, $\veebar$, $\neg$, and the logical operators implies and equivalent (if and only if) are $\Longrightarrow$, $\Leftrightarrow$. Inequalities between vectors are intended componentwise.

## Problem Setup and Formulation

Figure 1: Multi-layer control architecture for ADAS/AD.

This section briefly describes common components in a multi-layer guidance and control architecture for ADAS/AD, and then introduces the MIOCP formulation for MIP-DM.

### Multi-layer Control Architecture for Automated Driving

A typical guidance and control architecture is illustrated in Figure 1(a). A perception, sensing and estimation module uses various on-board sensor information, such as radar, LIDAR, camera, and global positioning system (GPS) information, to estimate the vehicle states, parameters, and parts of the surroundings relevant to the driving scenario. Based on a route given by a navigation system, a decision making module determines what maneuvers to perform, e.g., lane changing, stopping, waiting, intersection crossing. Then, a motion planning system generates a collision-free and kinematically feasible trajectory to perform the maneuvers, see, e.g.,. A vehicle control system computes the input signals to execute the motion planning trajectory, see, e.g.,. Additional low-level controllers operate the vehicle actuators.

### Setup for MIP-based Decision Making (MIP-DM)

In this paper, an autonomous vehicle must reach a desired destination while obeying the traffic rules. This requires the vehicle to adjust its velocity to obey the speed limits, to avoid collisions, to follow and change lanes, and to cross intersections following right of way rules. We propose an alternative architecture to that in Fig. 1(a), using MIP-based vehicle decision making, see Fig. 1(b). The problem setup in this work requires the following simplifying assumptions.

### Assumption 1

There exists a prediction time window along which the following are known

the position and orientation for each of the obstacles in a sufficiently large neighborhood of the ego vehicle,

the map information, including center lines, road curvature and lane widths within the current road segment,

the current traffic rules and any changes to the rules, e.g., traffic light timings and/or speed zone changes. \\QEDopen

Assumption 1 ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning").1 requires the vehicle to be equipped with sensors to detect static and dynamic obstacles within a given range and to locate itself in the environment. Furthermore, the vehicle must be equipped with a module that provides conservative predictions for future trajectories of the dynamic obstacles, e.g., using techniques referenced in. Assumption 1 ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning").2 requires the availability of map information and/or the use of online updates and corrections to such map information. Assumption 1 ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning").3 requires a combination of map information, online perception, and/or vehicle-to-infrastructure (V2I) communication. Based on these assumptions, we define the problem statement and objectives.

### Definition 2 (MIP Decision Making (MIP-DM))

Under Assumption 1 ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning") and given navigation information, at each sampling instant, the MIP-DM module solves an MIOCP on embedded hardware and under strict timing requirements. The solution provides desired maneuvers that the vehicle should execute, and a coarse trajectory, i.e., a sequence of waypoints and target velocities, over a horizon of several seconds for the vehicle control module to execute the maneuver. \\QEDopen

Based on Def. 2) ‣ 2.2 Setup for MIP-based Decision Making (MIP-DM) ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning"), the trajectory computed by the MIP-DM is executed by a vehicle control module, e.g., the NMPC reference tracking controller in Fig. 1(b).

### Mixed-integer Optimal Control Problem (MIOCP)

At each sampling time instant, the proposed MIP-DM solves the following MIOCP

$\underset{X,U}{\text{min}}\quad$ ${\sum\limits_{i = 0}^{N}{\frac{1}{2}\begin{bmatrix} (1a)
\end{bmatrix}^{\top}H{(i)}\begin{bmatrix}
\end{bmatrix}}} + {\begin{bmatrix}
\end{bmatrix}^{\top}\begin{bmatrix}
s.t. ${{x{({i + 1})}} = {{\begin{bmatrix} ${{\forall i} \in {\mathbb{Z}}_{0}^{N - 1}},$ (1b)
\end{bmatrix}\begin{bmatrix}
${\begin{bmatrix} ${{\forall i} \in {\mathbb{Z}}_{0}^{N}},$ (1c)
\end{bmatrix} \leq \begin{bmatrix}
\end{bmatrix} \leq \begin{bmatrix}
${{\underset{¯}{c}{(i)}} \leq {\begin{bmatrix} ${{\forall i} \in {\mathbb{Z}}_{0}^{N}},$ (1d)
\end{bmatrix}\begin{bmatrix}
\end{bmatrix}} \leq {\overline{c}{(i)}}},$
${{{u_{j}{(i)}} \in {\mathbb{Z}}},{{\forall j} \in {\mathcal{I}{(i)}}}},$ ${{\forall i} \in {\mathbb{Z}}_{0}^{N}},$ (1e)

where $i \in {\{ 0,1,\ldots,N\}}$ is the time, $N$ is the horizon length, the state variables are ${x{(i)}} \in {\mathbb{R}}^{n_{x}^{i}}$, the control and auxiliary variables are ${u{(i)}} \in {\mathbb{R}}^{n_{u}^{i}}$ and $\mathcal{I}{(i)}$ denotes the index set of integer decision variables, i.e., the cardinality ${|{\mathcal{I}{(i)}}|} \leq n_{u}^{i}$ denotes the number of integer variables at each time step. The objective in (1a ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")) defines a linear-quadratic function with positive semi-definite Hessian matrix ${H{(i)}} \succeq 0$ and gradient vectors ${q{(i)}} \in {\mathbb{R}}^{n_{x}^{i}}$ and ${r{(i)}} \in {\mathbb{R}}^{n_{u}^{i}}$. The constraints include dynamic constraints in (1b ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")), simple bounds in (1c ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")), affine inequality constraints in (1d ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")) and integer feasibility constraints in (1e ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")). The initial state constraint ${x{}} = {\hat{x}}_{t}$, where ${\hat{x}}_{t}$ is a current state estimate at time $t$, can be enforced using the simple bounds in (1c ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")). The MIOCP (1 ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")) includes control variables on the terminal stage, ${u{(N)}} \in {\mathbb{R}}^{n_{u}^{N}}$, due to possibly needing auxiliary variables to formulate the mixed-integer inequality constraints. A binary optimization variable ${u_{j}{(i)}} \in {\{ 0,1\}}$ can be defined as an integer variable ${u_{j}{(i)}} \in {\mathbb{Z}}$ in (1e ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")), including the simple bounds $0 \leq {u_{j}{(i)}} \leq 1$ in (1c ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")). For compactness, we denote $X = {\lbrack{x{}^{\top}},\ldots,{x{(N)}^{\top}}\rbrack}^{\top}$ and $U = {\lbrack{u{}^{\top}},\ldots,{u{(N)}^{\top}}\rbrack}^{\top}$. The MIOCP (1 ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")) can be reformulated as a block-sparse structured MIQP, and solved with corresponding algorithms.

## Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning

Next, we describe the MIP-DM for achieving safe and real-time feasible automated driving in real-world scenarios.

### Linear Vehicle Model in Road-aligned Frame

The curvilinear coordinate system used in the prediction model of the MIOCP (1 ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")) is shown in Fig. 2. A similar coordinate system has been used for predictive control, e.g.,. The vehicle position is described by $(p_{s},p_{n})$, where $p_{s}$ denotes the progress along the center line of the lane in which the ego vehicle is driving, and $p_{n}$ denotes the normal distance of the vehicle position from the center line.

Figure 2: Road-aligned curvilinear coordinate system for a curved segment; ps is the arc length along the center line and pn is the lateral deviation.

### Assumption 3

The turning radius is much larger than the wheelbase of the vehicle, such that the steering and slip angles are relatively small and their difference for the outside and inside wheels is negligible. \\QEDopen

Based on Ass. 3, which is common in vehicle motion planning, we use a simplified linear vehicle model in the curvilinear coordinate system and with decoupled longitudinal and lateral kinematics

where the control inputs are the longitudinal acceleration $a_{s}{(i)}$ and the lateral velocity $v_{n}{(i)}$ at each time step $i \in {\mathbb{Z}}_{0}^{N - 1}$. To approximate the nonholonomic constraints of Ackerman steering for vehicles, we enforce the linear inequality constraint on the lateral and longitudinal velocity

where $\alpha > 0$, and we assume ${v_{s}{(i)}} \geq 0$ at all time steps.

### Proposition 4

The inequality constraint in is a linear approximation of a vehicle steering limit and, using a kinematic bicycle model,

where $l_{r}$ denotes the distance from center of gravity to the rear axle and $R^{\min}$ denotes the vehicle's minimum turning radius.

### Proof 3.1

Considering the kinematic bicycle model

${\overset{˙}{p}}_{X}$ ${= {v\text{cos}{({\psi + \beta})}}},$ ${\overset{˙}{p}}_{Y}$ ${= {v\text{sin}{({\psi + \beta})}}},$ (5a)
$\overset{˙}{\psi}$ ${= {v\frac{\text{cos}{(\beta)}}{L}\text{tan}{(\delta)}}},$ $\beta$ ${= {\text{tan}^{- 1}\left( \frac{l_{r}\text{tan}{(\delta)}}{L} \right)}},$ (5b)

where $(p_{X},p_{Y})$ is the position of the vehicle's center of gravity in an absolute frame, and $L = {l_{f} + l_{r}}$ is the wheelbase. For a constant radius $R$, or road curvature $\frac{1}{R}$, the yaw rate is $\overset{˙}{\psi} = \frac{v}{R}$ \[33, Sec. 2.2\], such that ${\text{tan}{(\delta)}} \approx \frac{L}{R}$ and $\beta = {\text{tan}^{- 1}\left( \frac{l_{r}}{R} \right)}$. We know that the lateral velocity is ${\overset{˙}{p}}_{y} = {v\text{sin}{(\beta)}}$ in the car body frame. Given a minimum turning radius $R^{\min} > 0$, the steady state lateral velocity is $v_{y}^{\max} = {v\text{sin}{({\text{tan}^{- 1}{(\frac{l_{r}}{R^{\min}})}})}}$, and therefore $\alpha_{R}^{\max} = {\text{sin}{({\text{tan}^{- 1}{(\frac{l_{r}}{R^{\min}})}})}} \approx \frac{l_{r}}{R^{\min}} > 0$ in.

The vehicle model is an approximation of more precise models, see, e.g. which are usually nonlinear. However, the MIOCP (1 ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")) provides a reference trajectory for the vehicle controller and operates in normal driving conditions when some of the vehicle nonlinearities, such as the road-tire friction curve, are not excited, while others can be neglected because the decision-making operates over long horizons with a fairly coarse sampling period. Modeling errors are compensated by the vehicle control layer as illustrated in Fig. 1.

### Remark 5

Given a time varying road radius $R{(i)}$, which may be positive or negative depending on the direction of the road curvature, the lateral velocity in is bounded as ${v_{n}{(i)}} \leq {v_{y}^{\max} - {v_{y}^{R}{(i)}}}$, where $v_{y}^{\max} = {v\alpha_{R}^{\max}}$, and ${v_{y}^{R}{(i)}} = {v\alpha_{R}{(i)}}$ denotes the steady state lateral velocity to follow the center of the road with radius $R{(i)}$. Eq. may be replaced by

where $\alpha_{R}^{\max} = \frac{l_{r}}{R^{\min}} > 0$ defines the maximum steering and ${\alpha_{R}{(i)}} = \frac{l_{r}}{R{(i)}}$ defines the steering needed to follow the center of the road with radius $R{(i)}$, following Proposition 4. \\QEDopen

### Remark 6

Proposition 4 uses a simple approximation of the steady-state cornering equations in \[33, Sec. 3.3\]. Alternatively, the cornering equations could be directly used to compute a time-varying value for $\alpha{(i)}$ that depends on the predicted velocity and the road curvature. \\QEDopen

### Lane Change and Timing Delay Constraints

We enforce lane bound constraints

where $w_{l}$ denotes a lane width given by the map and $p_{n}^{ref} \in {\mathbb{R}}$ is an auxiliary state variable that denotes the lateral position of the center line of the current lane of the vehicle. For equal lane width values $w_{l}$, the vehicle is in lane $j$ if $p_{n}^{ref} = {{({j - 1})}w_{l}}$ for $j \in {\{ 1,\ldots,n_{l}\}}$, where $n_{l}$ is the number of lanes in the current traffic scenario. Even though the reference lane value may jump from one time step $p_{n}^{ref}{(i)}$ to the next $p_{n}^{ref}{({i + 1})}$, it may take multiple time steps for the lateral position to transition from the center line of one lane to the next, i.e., ${p_{n}{({i - l})}} \approx {p_{n}^{ref}{(i)}}$ and ${p_{n}{({i + k})}} \approx {p_{n}^{ref}{({i + 1})}}$, where $l \geq 0$ and $k \geq 1$.

### Lane Change Decision Constraints

We use two binary variables ${{\delta_{c}^{u}{(i)}},{\delta_{c}^{d}{(i)}}} \in {\{ 0,1\}}$ that denote whether the vehicle performs a lane change left or right, respectively, at time step $i \in {\mathbb{Z}}_{0}^{N - 1}$. We also introduce an auxiliary variable $\Delta_{c} \in {\mathbb{R}}$ defined by $\delta_{c}^{u}{(i)}$, $\delta_{c}^{d}{(i)}$ through

For $i \in {\mathbb{Z}}_{0}^{N - 1}$, the implications in may be implemented as

Constraint (9b) ensures that ${{\delta_{c}^{u}{(i)}} + {\delta_{c}^{d}{(i)}}} \leq 1$. The auxiliary state dynamics are

$p_{n}^{ref}{({i + 1})}$ ${= {{p_{n}^{ref}{(i)}} + {\Delta_{c}{(i)}}}},$ (10a)

where $n_{LC}{(i)}$ counts the number of lane changes over the prediction horizon and is initialized to ${n_{LC}{}} = 0$.

### Remark 7

The state ${n_{LC}{(i)}} \in {\mathbb{Z}}$ is an integer variable, but it can be relaxed to be continuous because the sum in (10b) is guaranteed to be integer. Similarly, $p_{n}^{ref}$ and $\Delta_{c}$ could be reformulated as $p_{n}^{ref} = {w_{l}{\overset{\sim}{p}}_{n}^{ref}}$ and $\Delta_{c} = {w_{l}{\overset{\sim}{\Delta}}_{c}}$, where ${\overset{\sim}{p}}_{n}^{ref} \in {\{ 0,1,\ldots,{n_{l} - 1}\}}$ and ${\overset{\sim}{\Delta}}_{c} \in {\{{- 1},0,1\}}$. State of the art MIP solvers can possibly use these integer feasibility constraints to reduce the computational effort. For simplicity, we only use continuous and binary optimization variables. \\QEDopen

### Timing Delay Constraints for Lane Changes

We enforce a minimum time delay of $t_{\min}$ between two consecutive lane changes. The lane change variables ${{\delta_{c}^{u}{(i)}},{\delta_{c}^{d}{(i)}}} \in {\{ 0,1\}}$ reset a timer $t_{c}{(i)}$ as

which can be implemented by constraints

where ${\delta_{c}{(i)}} = {{\delta_{c}^{u}{(i)}} + {\delta_{c}^{d}{(i)}}}$ is a compact notation, and $M \gg 0$ is a large positive constant in a big-M formulation. Given $t_{c}{(i)}$, we impose a minimum time between lane changes

i.e., ${\delta_{c}^{u}{(i)}} = 1$ or ${\delta_{c}^{d}{(i)}} = 1$ only if ${t_{c}{(i)}} \geq t_{\min}$. In a receding horizon implementation of the MIP-DM, the timer $t_{c}{}$ is initialized to the value from the previous time step.

### Polyhedral Obstacle Avoidance Constraints

The MIP-DM enforces obstacle avoidance constraints to avoid a region of collision risk around other traffic participants, e.g., vehicles, bicycles or pedestrians. The position and dimensions of the safety region may be time varying and adapted to a prediction of the behavior for each of the traffic participants. In addition, obstacle avoidance constraints enforce stopping maneuvers, e.g., in case of a stop sign or a red traffic light at an intersection. Per Assumption 1 ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning"), the prediction of obstacle motions, the map information and the traffic rules are known. For simplicity, we use axis-aligned rectangular collision regions, as illustrated in Figure 3. Alternatively, any polyhedral representation of the collision regions could be used, see, e.g.,. The size of the collision region around the obstacle is increased with the geometric shape of the ego vehicle and includes an additional safety margin for robustness to discretization errors, model mismatch and/or disturbances.

As shown in Fig. 3, obstacle avoidance for an axis-aligned rectangular region results in four disjoint feasible sets. We introduce $4$ auxiliary binary variables ${\delta_{o}^{j}{(i)}} = {\lbrack{\delta_{o,k}^{j}{(i)}}\rbrack}_{k \in {\mathbb{Z}}_{1}^{4}}$ for $j \in {\mathbb{Z}}_{1}^{n_{obs}}$, to implement the logical implications

where we omit the index $i \in {\mathbb{Z}}_{0}^{N}$ for readability, and we use slack variables ${\nu_{s}^{c}{(i)}} \geq 0$, ${\nu_{n}^{c}{(i)}} \geq 0$ to ensure feasibility. We impose that the ego vehicle is in one of the feasible sets by ${\sum_{k = 1}^{4}{\delta_{o,k}^{j}{(i)}}} = 1$. Hard obstacle avoidance constraints can be defined by enforcing upper bounds on the slack variables $0 \leq {\nu_{s}^{c}{(i)}} \leq {\overline{\nu}}_{s}^{c}$ and $0 \leq {\nu_{n}^{c}{(i)}} \leq {\overline{\nu}}_{n}^{c}$, see Fig. 3. To reduce the number of variables in the MIP formulation, a single slack variable ${\nu_{s}^{c}{(i)}} = {a_{sn}\nu_{n}^{c}{(i)}}$ may be used, where $a_{sn} > 0$ is a constant. The implications in can be implemented as

where $M \gg 0$ denotes the big-M constant.

Figure 3: Obstacle avoidance constraints using binary variables and an axis-aligned rectangular collision region. The extent of the region is increased by the geometric shape of the ego vehicle and includes an additional safety margin. The light red shaded region is defined by soft constraints, while the dark region is defined by hard constraints.

### Remark 8

For each obstacle $j \in {\mathbb{Z}}_{1}^{n_{obs}}$ in, we predict its position based on a constant velocity profile in curvilinear coordinates. Future work may include the use of a more advanced prediction model, e.g., a switching dynamical model or a neural network classifier. \\QEDopen

### Traffic Intersection Crossing Constraints

The obstacle avoidance constraints in are also used to prevent the ego vehicle from crossing a traffic intersection, e.g., forcing the vehicle to stop during a particular time window. Similar to Fig. 3, the avoidance region is defined by the dimensions of the intersection, enlarged to account for the physical shape of the ego vehicle and with additional safety margins to account for modeling errors. If the intersection is controlled by traffic lights and if the traffic light changes are known, e.g., using V2I communication, the intersection crossing constraints are time-varying within the prediction horizon. For example, if it is known that a traffic light will turn red, the intersection crossing constraints cause the ego vehicle to slow down and plan a stopping maneuver. Similarly, the constraints are relaxed at future time steps within the prediction horizon when the traffic lights are predicted to become green. Alternatively, the intersection crossing constraints may be implemented based on map information and/or the perception system.

### Zone-dependent Traffic Rules

In real-world scenarios, traffic rules may change when the vehicle transitions into a particular zone. From one zone to the next, following traffic rule constraints may change

speed limit, e.g., the vehicle entering a low-speed zone,

allowed lane changes, e.g., when no lane changes are allowed inside a particular zone,

available lanes, e.g., when a three-lane road transitions into a two-lane road or when the vehicle must merge.

We introduce binary variables $\delta_{z} = {\lbrack\delta_{z}^{1},\ldots,\delta_{z}^{n_{z}}\rbrack}$, where $n_{z}$ denotes the number of position-dependent zones. Each zone is represented by a range $\lbrack{\underset{¯}{p}}_{j},{\overline{p}}_{j}\rbrack$ for $j \in {\mathbb{Z}}_{1}^{n_{z}}$ in the longitudinal $p_{s}$-direction. We detect whether the vehicle is in zone $j$ as

which can be implemented as

Because the position-dependent zones are disjoint, the vehicle needs to be inside exactly one zone, i.e., ${\sum_{j = 1}^{n_{z}}\delta_{z}^{j}} = 1$.

The auxiliary binary variables $\delta_{z}$ and constraints in enable implementing the zone-dependent traffic rules. For example, changing speed limits can be enforced by

where the speed limit ${\overline{v}}_{s}^{j}{(i)}$ corresponds to zone $j = {1,\ldots,n_{z}}$ and ${\sum_{j = 1}^{n_{z}}\delta_{z}^{j}} = 1$. Similarly, the allowed number of lane changes can be adjusted as

and the constraints on feasible lanes can be adjusted as

Figure 4 shows the transition from a three-lane road segment into a two-lane road segment using.

Figure 4: Zone-dependent traffic rule: transition from a zone with three lanes (δz1 = 1) to a zone with two lanes (δz2 = 1), using the proposed MIP inequality constraints in and.

### Extended Dynamic System with Auxiliary Variables

For the prediction model (1b ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")), the vehicle kinematics and the auxiliary dynamics result in the augmented system

The MIP-DM also enforces simple bounds on state variables at each time step $i \in {\mathbb{Z}}_{0}^{N}$

and simple bounds on control inputs for $i \in {\mathbb{Z}}_{0}^{N - 1}$

### Objective for Decision Making and Motion Planning

The objective function (1a ‣ 2 Problem Setup and Formulation ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning")) of the proposed MIP-DM is $\sum_{i = 0}^{N}{\ell_{i}{({x{(i)}},{u{(i)}})}}$, where the stage cost is

where ${\delta_{c}{(i)}} = {{\delta_{c}^{u}{(i)}} + {\delta_{c}^{d}{(i)}}}$, ${\nu^{c}{(i)}} = {{\nu_{s}^{c}{(i)}} + {\nu_{n}^{c}{(i)}}}$, and $w_{j} \geq 0$ for $j = {1,\ldots,7}$ are the weights. The first term in is the longitudinal tracking error with respect to a reference trajectory ${\overline{p}}_{s}^{ref}{(i)}$, e.g., computed based on a desired reference velocity. The second term minimizes the lateral tracking error with respect to the current center lane. The third and fourth terms penalize the control actions, i.e., the longitudinal acceleration and lateral velocities, respectively. The fifth term penalizes lane change decisions.

The sixth term in minimizes a tracking error of the current lane with respect to a given preferred lane value ${\overline{p}}_{n}^{ref}{(i)}$, e.g., the right lane in right-hand traffic or the left most lane when a vehicle desires to make a left turn at a next traffic intersection. To handle the absolute value in, we minimize an auxiliary control variable $\Deltap_{n}^{ref}$, satisfying

such that ${\Deltap_{n}^{ref}} \geq {|{p_{n}^{ref} - {\overline{p}}_{n}^{ref}}|}$ holds. The squared terms in may be replaced by absolute values which results in a mixed-integer linear program (MILP) instead of an MIQP. The last term in corresponds to a penalty on the slack variables for soft constraint violations. The weight $w_{7} \gg 0$ is chosen large enough to ensure that a feasible solution with ${\nu^{c}{(i)}} = 0$ is found if and when it exists.

The complete MIOCP of the proposed MIP-DM reads as

The state vector is $x = {\lbrack p_{s},p_{n},v_{s},p_{n}^{ref},n_{LC},t_{c}\rbrack}$, and the control and auxiliary input vector is $u = {\lbrack a_{s},v_{n},{\overset{\sim}{t}}_{c},\Delta_{c},\delta_{c},\delta_{o},\delta_{z}\rbrack}$. The binary optimization variables include the lane change variables $\delta_{c} = {\lbrack\delta_{c}^{u},\delta_{c}^{d}\rbrack}$, the obstacle avoidance variables $\delta_{o} = {\lbrack\delta_{o}^{1},\ldots,\delta_{o}^{n_{obs}}\rbrack}$, and the traffic zone variables $\delta_{z} = {\lbrack\delta_{z}^{1},\ldots,\delta_{z}^{n_{z}}\rbrack}$, while the remaining variables are continuous.

### Remark 9

By defining an upper bound on the number of other vehicles for obstacle avoidance in a realistic traffic environment, the MIOCP has fixed dimensions that allows for static memory allocation in an embedded implementation of the MIP-DM for microprocessors suitable to automotive applications, as discussed later. \\QEDopen

## Embedded MIQP Solver for Mixed-Integer Model Predictive Control

The MIOCP is converted into the MIQP

$\underset{\mathbf{z}}{\text{min}}\quad$ ${\frac{1}{2}{\mathbf{z}}^{\top}H{\mathbf{z}}} + {h^{\top}{\mathbf{z}}}$ (26a)
s.t. ${G{\mathbf{z}}} \leq {g,{F{\mathbf{z}}}}$ ${= f},$ (26b)
${{\mathbf{z}}_{j} \in {\mathbb{Z}}},$ ${j \in \mathcal{I}},$ (26c)

where $\mathbf{z}$ includes all optimization variables and the index set $\mathcal{I}$ denotes the integer variables. Next, we summarize the main ingredients of the BB-ASIPM solver that uses a B&B method with reliability branching and warm starting, block-sparse presolve techniques, early termination and infeasibility detection within a fast convex QP solver.

### Branch-and-bound Method and Search Heuristics

The B&B algorithm sequentially creates partitions of the original MIQP problem as shown in Figure 5. For each partition, a local lower bound on the optimal objective value is obtained by solving a convex relaxation of the MIQP subproblem. If the relaxation yields an integer-feasible solution, the B&B updates the global upper bound for the MIQP solution, which is used to *prune* tree partitions. The B&B method terminates when the difference between the upper and lower bound is below a user-defined threshold. A key decision of the B&B procedure is how to create partitions, i.e., which node to choose and which discrete variable to select for branching. BB-ASIPM uses *reliability branching* which combines strong branching and pseudo-costs.

Figure 5: Branch-and-bound (B&amp;B) method as a binary search tree. A selected node can be either branched, resulting in 2 partitions for each binary variable uj ∈ {0, 1}, or pruned based on feasibility or the current upper bound.

### Tailored Exact Presolve Reduction Techniques

We refer to the parametric MIQP from as $\mathcal{P}{(\theta)}$, in which the parameter vector $\theta$ includes the state estimate ${\hat{x}}_{t}$, and we denote the discrete variables in (26c) by $\delta \in {\mathbb{Z}}^{N_{\delta}}$. We use the compact notation $\mathcal{P}{({{\theta,\delta_{\mathcal{R}}} = \hat{\delta}})}$ to denote the MIQP after fixing ${\delta_{j} = {\hat{\delta}}_{j}},{j \in \mathcal{R}}$ where $\mathcal{R}$ is an index set.

### Definition 10 (Presolve Step)

Given problem $\mathcal{P}{(\theta)}$ and a set of integer values ${\{{\hat{\delta}}_{j}\}}_{j \in \mathcal{R}}$ for the index set $\mathcal{R} \subseteq {\{ 1,\ldots,N_{\delta}\}}$, the presolve step computes

resulting in updated integer values ${\{{\hat{\delta}}_{j}^{+}\}}_{j \in \mathcal{R}^{+}}$ for the index set $\mathcal{R}^{+} \subseteq {\{ 1,\ldots,N_{\delta}\}}$, such that:

The new index set includes the original set, $\mathcal{R} \subseteq \mathcal{R}^{+}$.

$\mathcal{P}{({{\theta,\delta_{\mathcal{R}^{+}}} = {\hat{\delta}}^{+}})}$ is infeasible / unbounded only if $\mathcal{P}{({{\theta,\delta_{\mathcal{R}}} = \hat{\delta}})}$ is infeasible / unbounded.

Any feasible / optimal solution of $\mathcal{P}{({{\theta,\delta_{\mathcal{R}^{+}}} = {\hat{\delta}}^{+}})}$ maps to a feasible / optimal solution of $\mathcal{P}{({{\theta,\delta_{\mathcal{R}}} = \hat{\delta}})}$, with identical objective value. \\QEDopen

A presolve routine applied to a root node in B&B corresponds to Definition 10 ‣ 4.2 Tailored Exact Presolve Reduction Techniques ‣ 4 Embedded MIQP Solver for Mixed-Integer Model Predictive Control ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning") with $\mathcal{R} = \varnothing$. In general, presolve cannot prune all of the binary or integer decision variables, but often it leads to a reduced problem that is significantly faster to solve.

We use the tailored block-sparse presolve procedure \[13, Section 4\] that abides by the rules in Def. 10 ‣ 4.2 Tailored Exact Presolve Reduction Techniques ‣ 4 Embedded MIQP Solver for Mixed-Integer Model Predictive Control ‣ Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning"), and includes:

*Domain propagation* to strengthen bounds based on constraints of the MIQP, which may lead to fixing multiple integer variables. A tailored implementation for MIOCPs based on an iterative forward-backward propagation is described in \[13, Alg. 2\].

*Redundant constraints* are detected and removed based on updated bound values, which may also benefit *dual fixing* of multiple variables, see \[13, Alg. 4\].

*Coefficient strengthening* to tighten the feasible space of the convex QP relaxation without removing any integer-feasible solution of the MIQP. A block-sparse implementation is described in \[13, Alg. 5\].

*Variable probing* to obtain tightened bound values for multiple optimization variables by temporarily fixing a binary variable to $0$ and $1$, see \[13, Alg. 6\].

The presolve procedure in terminates if the problem is detected to be infeasible or if insufficient progress is made from one iteration to the next. An upper limit on the number of presolve iterations and/or a timeout is typically needed to ensure computational efficiency, and it generally results in a considerable speedup of the B&B computations.

### Block-sparse QP solver for Convex Relaxations

A primal-dual interior point method (IPM) uses a Newton-type algorithm to solve a sequence of relaxed Karush-Kuhn-Tucker (KKT) conditions for the convex QP. We use the active-set based inexact Newton implementation of ASIPM, which exploits the block-sparse structure in the linear system, with improved numerical conditioning, reduced matrix factorization updates, warm starting, early termination and infeasibility detection. If the convex QP relaxation

has optimal value that exceeds the current global upper bound in the B&B method,

the node and corresponding subtree can be pruned from the B&B tree. A considerable computational effort can be avoided if the above scenarios are detected early, i.e., more quickly than solving the convex QPs. In, we describe an early termination method based on a tailored dual feasibility projection strategy applicable to BB-ASIPM to handle both cases and to reduce the computational effort of the B&B method without affecting the quality of the optimal solution.

### Embedded Software Implementation for Hybrid MPC

In hybrid MPC, warm starting can be used to reduce the computational effort in the B&B method from one time step to the next as discussed in. BB-ASIPM uses *tree propagation* to efficiently reuse the branching decisions and pseudo-costs from the previous MIQP solution. An upper bound can be imposed on the number of B&B iterations to ensure a maximum computation time below a threshold. If an integer-feasible solution is found, a B&B method automatically provides a bound on the suboptimality of this MIQP solution. The BB-ASIPM solver is implemented in self-contained C code, which allows for real-time implementations on embedded microprocessors as shown next.

## Numerical Simulation Results

We present numerical simulation results for the MIP-DM described in Section 3, in a variety of traffic scenarios. We also compare the BB-ASIPM solver from Section 4 against state-of-the-art software tools, and we demonstrate its real-time feasibility on dSPACE rapid prototyping units.

### Problem Formulation and Simulation Test Scenarios

\raisebox{-.9pt} {1}⃝ see Fig. 6(a)

\raisebox{-.9pt} {2}⃝ see Fig. 6(b)

\raisebox{-.9pt} {3}⃝ see Fig. 6(c)

\raisebox{-.9pt} {4}⃝ see Fig. 6(d)

\raisebox{-.9pt} {5}⃝ see Fig. 6(e)

\raisebox{-.9pt} {6}⃝ see Fig. 6(f)

\raisebox{-.9pt} {7}⃝ see Fig. 6(g)

\raisebox{-.9pt} {8}⃝ see Fig. 6(h)

Table 1: Problem dimensions and parameters in MIQP formulation of Section 3 for each of the test scenarios in Fig. 6. The number of binary variables per time step in the MIOCP prediction time horizon is nδ = 2 + 3 nobs + nz.

(a) Scenario 1: ego vehicle overtaking three obstacles on a road with one-way traffic.

(b) Scenario 2: ego vehicle swaying for two parked vehicles (only one visible), avoiding a third vehicle on other lane with one-way traffic.

(c) Scenario 3: ego vehicle overtaking before stopping at intersection, then ego continues after two vehicles finish crossing intersection.

(d) Scenario 4: ego vehicle overtaking obstacles on a curved road with one-way traffic, followed by stopping and crossing an intersection.

(e) Scenario 5: ego vehicle merging to lane 2 between three vehicles with one-way traffic.

(f) Scenario 6: ego vehicle merging at the end of lane onto a new lane while avoiding / overtaking three vehicles (only one visible).

(g) Scenario 7: ego vehicle performs right turn at a T-intersection, merging between two vehicles (only one visible) on same lane of the road segment.

(h) Scenario 8: ego vehicle turns left at T-intersection, following one vehicle while avoiding two other vehicles driving in the opposite direction.

Figure 6: Snapshot of the closed-loop Matlab simulations using the MIP-DM in 8 test scenarios. The ego vehicle is shown in blue, other vehicles in red. A video recording of the simulations is available at: https://youtu.be/FyaGRZvuqmA.

In this section, we perform closed-loop simulations of MIP-DM in Matlab using the vehicle model in, to show the variety of traffic scenarios that can be handled explicitly using the MIQP in Section 3. We use a simple model to assess the behavior and the stand-alone computational load of MIP-DM. Robustness to model approximations and uncertainty is validated in the experiments shown later.

Figure 6 shows a snapshot of the Matlab simulations for $8$ test scenarios. Table 1 shows the problem dimensions and parameter values in the MIQP formulation of Section 3 for the test scenarios in Fig. 6, where $N = 15$ is the horizon length, $n_{x}$ is the number of state variables, $n_{u}$ is the number of control variables, $n_{c}$ is the number of inequality constraints, each per time step, and $n_{\delta} = {2 + {3n_{obs}} + n_{z}}$ is the number of binary variables per time step, with $n_{obs}$ the maximum number of obstacles (see Section 3.3), and $n_{z}$ the number of zones (see Section 3.4). Using a sampling time of $T_{s} = 1$ s, the MIP-DM time horizon is $T = {NT_{s}} = 15$ s.

Scenario 1 in Fig. 6(a) shows the ego vehicle overtaking three obstacles, where two obstacles are on lane 1 and a third obstacle is on lane 2, on a road segment with one-way traffic. Lane 1 refers to the right most lane with respect to the ego vehicle's direction of motion. Scenario 2 in Fig. 6(b) shows the ego vehicle swaying around two parked vehicles (with zero velocity) on lane 1, while avoiding a third vehicle on lane 2. Scenario 3 in Fig. 6(c) shows the ego vehicle overtaking one vehicle on lane 1 before stopping at a traffic intersection, then crossing after two other vehicles. Scenario 4 in Fig. 6(d) shows the ego vehicle overtaking three obstacles (two vehicles on lane 1 and one vehicle on lane 2) on a curved road segment with one-way traffic, followed by stopping and crossing an intersection. In the test scenarios 1-4, lane 1 is the preferred lane ${\overline{p}}_{n}^{ref}$ in, so that the ego vehicle always returns to lane 1 after each overtaking or sway maneuver.

Scenario 5 in Fig. 6(e) shows the ego vehicle merging from lane 1 to lane 2 between three vehicles on lane 2, i.e., the preferred lane ${\overline{p}}_{n}^{ref}$ in is lane 2. Scenario 6 in Fig. 6(f) shows the ego vehicle merging at the end of a current lane onto a new lane while avoiding and/or overtaking three vehicles that are driving on the same lane. Scenario 7 in Fig. 6(g) shows the ego vehicle performing a right turn at a T-intersection, merging between two vehicles on the same lane of the new road segment. Scenario 8 in Fig. 6(h) shows the ego vehicle performing a left turn at a T-intersection, following one vehicle on the same lane while avoiding two other vehicles driving in the opposite direction. In the test scenarios 5-8, after a merging or turning maneuver, the ego vehicle overtakes any other vehicle that is driving below the speed limit.

### Computational Performance and Solver Comparisons

Table 2: Average and worst-case computation times for each of the 8 scenarios in Figure 6 for MIP-DM with the MIQP formulation in Section 3, using GUROBI, MOSEK and BB-ASIPM solver.

\raisebox{-.9pt} {1}⃝ see Fig. 6(a)

\raisebox{-.9pt} {2}⃝ see Fig. 6(b)

\raisebox{-.9pt} {3}⃝ see Fig. 6(c)

\raisebox{-.9pt} {4}⃝ see Fig. 6(d)

\raisebox{-.9pt} {5}⃝ see Fig. 6(e)

\raisebox{-.9pt} {6}⃝ see Fig. 6(f)

\raisebox{-.9pt} {7}⃝ see Fig. 6(g)

\raisebox{-.9pt} {8}⃝ see Fig. 6(h)

Table 2 shows the average and worst-case computation times of MIP-DM for each of the $8$ simulation scenarios that are illustrated in Figure 6, using the MIQP formulation as described in Section 3 and where the MIQPs at each control time step are solved using either GUROBI, MOSEK or BB-ASIPM. It can be observed that the average and worst-case computation times of BB-ASIPM are approximately $6$ and $5$ times faster than MOSEK, respectively. On the other hand, the average and worst-case computation times of GUROBI are approximately $1.5$ and $2.5$ times faster than BB-ASIPM, respectively. Note that all default presolve options are enabled in the GUROBI solver.

Given the relatively simple and compact algorithmic implementation in BB-ASIPM, e.g., compared to the extensive collection of advanced heuristics, presolve and cutting plane techniques in the commercial GUROBI solver, it is reassuring to see that the tailored BB-ASIPM solver can remain competitive with state-of-the-art software tools in Table 2. The software implementation of BB-ASIPM is relatively compact and self-contained such that it can execute on an embedded microprocessor for real-time vehicle decision making and motion planning. Instead, state-of-the-art optimization tools, such as GUROBI and MOSEK typically cannot be used on embedded control hardware with limited computational resources and available memory.

### Hardware-in-the-loop Simulation Results on dSPACE Scalexio and MicroAutoBox-III Rapid Prototyping Units

Next, we present detailed results of running hardware-in-the-loop simulations for each of the $8$ test scenarios shown in Figure 6 on both the dSPACE Scalexio^11^1dSPACE Scalexio DS6001 unit, with an Intel i7-6820EQ quad-core $2.8$ GHz processor with 64 kB L1 cache per core, 256 kB L2 cache per core, 8 MB shared L3 cache, 4 GB DDR4 RAM, and 8 GB flash memory. In the presented results, MIP-DM executes in a single core. and the dSPACE MicroAutoBox-III (MABX-III)^22^2dSPACE MicroAutoBox-III DS1403 unit, with four ARM Cortex-A15 processor cores with 32 kB L1 cache per core, 4 MB shared L2 cache, 2 GB DDR3L RAM, and 64 MB flash memory. In the presented results, MIP-DM executes in a single core. rapid prototyping units. Table 3 shows the average and worst-case computation times, the number of B&B iterations, total number of ASIPM iterations, and the memory usage of the BB-ASIPM solver on Scalexio and MABX-III. The memory usage is categorized into *text* that contains code and constant data, which is typically stored in ROM, and *data* that is stored in RAM.

From Table 3, MIP-DM is real-time feasible using the proposed BB-ASIPM solver for each of the $8$ simulation scenarios on both the dSPACE Scalexio and MABX-III units, as the worst-case computation time is below the sampling time of $T_{s} = 1$ s at each time step. More specifically, considering all test scenarios, the computation times on the dSPACE Scalexio are always below $200$ ms, below $100$ ms $99$% of the times, and the average is only $17.3$ ms. On MABX-III, the computation times are always below $800$ ms, below $400$ ms $99$% of the times, and the average is only $76.3$ ms. The total memory usage is approximately $18$ MB on Scalexio and $16.1$ MB on MABX-III, due to the different compilers. As expected, for each test scenario, Table 3 shows that the number of iterations on Scalexio and MABX-III is identical.

Table 3: Average and worst-case computation times, number of B&amp;B iterations, total number of ASIPM iterations, and memory footprint of the embedded BB-ASIPM solver on the dSPACE Scalexio and on the dSPACE MABX-III, for hardware-in-the-loop simulations of the MIP-DM method for the 8 scenarios in Figure 6.

BB-ASIPM on dSPACE Scalexio
BB-ASIPM on dSPACE MABX-III

\raisebox{-.9pt} {1}⃝ see Fig. 6(a)

\raisebox{-.9pt} {2}⃝ see Fig. 6(b)

\raisebox{-.9pt} {3}⃝ see Fig. 6(c)

\raisebox{-.9pt} {4}⃝ see Fig. 6(d)

\raisebox{-.9pt} {5}⃝ see Fig. 6(e)

\raisebox{-.9pt} {6}⃝ see Fig. 6(f)

\raisebox{-.9pt} {7}⃝ see Fig. 6(g)

\raisebox{-.9pt} {8}⃝ see Fig. 6(h)

## Experimental Results of MIP-DM and NMPC on Small-scale Automated Vehicles

Next, we validate the performance of MIP-DM on experiments with small-scale vehicles, using ROS and an Optitrack motion-capture system. First, we briefly present the hardware and software setup, then we describe the integration of MIP-DM with a nonlinear MPC (NMPC) for reference tracking, and finally we show the experiment results.

### Hardware Setup and Software Implementation

(a) Small-scale autonomous vehicle.

(b) OptiTrack motion capture camera.

(c) Experiments using three small-scale vehicles: the ego vehicle (blue flag) executing the MIP-DM and NMPC, and two obstacles (no flag).

Figure 7: Experimental testbench that consists of small-scale automated vehicles (a) with on-board sensors, and an OptiTrack motion capture system (b). Track and snapshot of the positions of the ego vehicle and of the two obstacle vehicles (c).

The hardware setup is illustrated in Figure 7. It includes a *Hamster* vehicle in Fig. 7(a), a $25 \times 20$ cm mobile robot with electric steering and electric motor speed control. The robot is equipped with sensors such as a rotating $360$ deg Lidar, an inertial measurement unit, GPS receiver, HD camera, and motor encoders. It has Ackermann steering and its kinematic behavior emulates that of a regular vehicle. To evaluate the performance of the automated driving system, we use an Optitrack motion-capture system, see Fig. 7(b), to obtain position and orientation measurements for each of the Hamster vehicles. Depending on the environment and quality of the calibration, the Optitrack system can track the position for each of the Hamster vehicles within $1$ cm and with an orientation error of less than $3$ deg.

Our experimental setup consists of three vehicles driving on a two-lane track shaped as a figure eight, resulting in a traffic intersection as shown in Fig. 7(c). Two Hamsters are designated as *obstacles*, executing a standard PID controller that tracks the center line of the current lane. A traffic intersection coordinator forces each of the obstacles to stop in front of the intersection for at least three seconds before continuing the execution of the PID lane keeping controller when the intersection is free. The third Hamster is the ego vehicle that is controlled by the multi-layer control architecture shown in Figure 8, i.e., the proposed MIP-DM method in combination with an NMPC for reference tracking as described in the next section. Each of the components in Fig. 8 is executed in a separate ROS node on a single dedicated desktop computer^33^3The desktop for vehicle experiments is equipped with an Intel i7-6900K CPU @ 3.20GHz $\times 8$ processor, 64 GB RAM, and Ubuntu 16.04 LTS..

Figure 8: Multi-layer control architecture with MIP-DM, NMPC controller, and EKF state estimator using measurements from the Optitrack system and on-board sensors of the Hamster.

### Integration of MIP-DM and NMPC Tracking Controller

We briefly introduce the NMPC that executes the motion plan of the MIP-DM, see Fig. 8. Based on the vehicle model in, the MIP-DM reference trajectory in curvilinear coordinates is $\begin{bmatrix}
\end{bmatrix}^{\top}$ for $i \in {\mathbb{Z}}_{0}^{N}$, which is transformed to an absolute coordinate frame $(p_{X},p_{Y})$ as in Fig. 2. Given an approximation of the heading angle ${\psi{(i)}} \approx {\arctan\left( \frac{{p_{Y}{({i + 1})}} - {p_{Y}{(i)}}}{{p_{X}{({i + 1})}} - {p_{X}{(i)}}} \right)}$, we obtain a reference trajectory $\begin{bmatrix}
\end{bmatrix}^{\top}$ for $i \in {\mathbb{Z}}_{0}^{N}$. Similar to, we use a $3^{\text{rd}}$ order polynomial approximation, resulting in ${{\mathbf{y}}^{ref}{(\tau)}} = \begin{bmatrix}
{{p_{X}^{ref}{(\tau)}},{p_{Y}^{ref}{(\tau)}},{\psi^{ref}{(\tau)}},{v^{ref}{(\tau)}}}
\end{bmatrix}^{\top}$ for $0 \leq \tau \leq T^{mpc}$, where $T^{mpc}$ is the NMPC horizon length.

For the NMPC prediction model, we use the nonlinear kinematic model with additional actuation dynamics as in, resulting in the continuous time dynamics

${\overset{˙}{p}}_{X}$ ${= {v\text{cos}{({\psi + \beta})}}},$ ${\overset{˙}{p}}_{Y}$ ${= {v\text{sin}{({\psi + \beta})}}},$ (28a)
$\overset{˙}{\psi}$ ${= {v\frac{\text{cos}{(\beta)}}{L}\text{tan}{(\delta_{f})}}},$ ${\overset{˙}{\delta}}_{f}$ $= {\frac{1}{t_{d}}{({{\delta + \delta_{o}} - \delta_{f}})}}$ (28b)
$\overset{˙}{v}$ ${= u_{1}},$ $\overset{˙}{\delta}$ ${= u_{2}},$ (28c)

where $p_{X},p_{Y}$ is the longitudinal and lateral position in the world frame, $\psi$ is the heading angle and $\overset{˙}{\psi}$ the heading rate, $v$ is the longitudinal velocity, $\delta$ and $\delta_{f}$ are the commanded and actual front wheel steering angle, respectively, and $L,\beta$ are defined as in. First order front steering dynamics are included in for the steering actuation response. In addition, we estimate the offset value $\delta_{o}$ for the steering angle online using an extended Kalman filter (EKF), which also compensates for unmodeled disturbances, see Fig. 8. The inputs $u_{1},u_{2}$ are the acceleration and steering rate, respectively.

At each control time step $t$, the NMPC solves

$\underset{X,U}{\text{min}}\quad$ ${\frac{1}{2}{\sum\limits_{i = 0}^{N^{mpc}}{\|{{{\mathbf{y}}{(k)}} - {{\mathbf{y}}^{ref}{(t_{k})}}}\|}_{Q}^{2}}} + {\|{e_{Y}{(k)}}\|}_{W}^{2}$ (29a)
${{\underset{¯}{c}}_{k} \leq {c_{k}\left( {x{(k)}},{u{(k)}} \right)} \leq {\overline{c}}_{k}},$ ${{\forall k} \in {\mathbb{Z}}_{0}^{N^{mpc}}},$ (29e)

where the $N^{mpc}$ control intervals are defined by an equidistant grid of time points $t_{k} = {k\frac{T^{mpc}}{N^{mpc}}}$ for $k \in {\mathbb{Z}}_{0}^{N^{mpc}}$ over the NMPC horizon, ${\hat{x}}_{t}$ is the current state estimate from the EKF at time $t$, and the constraints in (29d) are a discretization of the continuous time dynamics in using a $4^{\text{th}}$ order Runge-Kutta method. The NMPC tracking objective is formulated as a weighted least squares cost of the error between the output ${\mathbf{y}}{(k)}$ and the reference trajectory ${\mathbf{y}}^{ref}{(\tau)}$, the path error ${e_{Y}{(k)}} = {{\text{cos}{({\psi^{ref}{(t_{k})}})}\left( {{p_{Y}{(k)}} - {p_{Y}^{ref}{(t_{k})}}} \right)} - {\text{sin}{({\psi^{ref}{(t_{k})}})}\left( {{p_{X}{(k)}} - {p_{X}^{ref}{(t_{k})}}} \right)}}$, the squared inputs and an $L_{1}$ penalty on the slack variables $\nu{(k)}$. We introduce a nonnegative slack variable ${\nu{(k)}} \geq 0$ for implementing the $L_{1}$ penalty, and the weight $r_{\nu} \gg 0$ is chosen sufficiently large to ensure that ${\nu{(k)}} = 0$ when a feasible solution exists.

Constraints (29e) include hard bounds on the control inputs and soft constraints for limiting the distance to the reference trajectory, the velocity and the steering angle

$- {\overline{e}}_{Y}$ ${\leq {e_{Y} + s}},$ $- {\overline{\delta}}_{f}$ ${\leq {\delta_{f} + s}},$ $- \overline{v}$ ${\leq {v + s}},$ (30a)
$e_{Y}$ ${\leq {{\overline{e}}_{Y} + s}},$ $\delta_{f}$ ${\leq {{\overline{\delta}}_{f} + s}},$ $v$ ${\leq {\overline{v} + s}},$ (30b)
$- \overline{\overset{˙}{\delta}}$ ${\leq \overset{˙}{\delta} \leq \overline{\overset{˙}{\delta}}},$ $- \overline{\overset{˙}{v}}$ ${\leq \overset{˙}{v} \leq \overline{\overset{˙}{v}}}.$ (30c)

In NMPC, obstacle avoidance is enforced by ellipsoidal constraints that approximate the rectangular collision region for each obstacle in the MIP-DM, see Fig. 3,

where $\begin{bmatrix}
\end{bmatrix} = {R{(o_{\psi,j})}^{\top}\begin{bmatrix}
\end{bmatrix}}$ is the rotated distance, $(o_{X,j},o_{Y,j},o_{\psi,j})$ is the obstacle's pose, and $(a_{x,j},a_{y,j})$ are the lengths of the principal semi-axes of the ellipsoid that ensure a safety margin around each obstacle.

The nonlinear OCP includes $n_{x} = 6$ states, $n_{u} = 3$ control inputs and $N^{mpc} = 80$ control intervals with a sampling period of $T_{s}^{mpc} = 25$ ms over a $T^{mpc} = 2$ s horizon length. The NMPC controller is implemented with a sampling frequency of $40$ Hz, using the real-time iteration (RTI) algorithm in the ACADO code generation tool and the PRESAS QP solver. The sampling period of MIP-DM is reduced with respect to that of Section 5 due to the scaling of the vehicles. MIP-DM executes with a sampling period of $T_{s}^{mip} = 0.3$ s and horizon length $N^{mip} = 15$.

### Experimental Results using Small-scale Vehicles

Based on the MIP-DM in Section 3, the capabilities of the ego vehicle include lane selection, lane change execution, swaying maneuvers, queuing behavior and stopping / crossing at the traffic intersection. Based on the zone constraints in the MIP (see Section 3.4), we implement a traffic rule that the ego vehicle is only allowed to make lane changes in the bottom right loop of the figure eight track (see Fig. 7(c)).

Figure 9 shows four snapshots of the experiment. The left side of each subfigure shows the location of the ego (blue) and two obstacles (red) on the eight shaped track, the safety ellipsoid around each obstacle (dashed red line), the NMPC predicted trajectory (blue plus markers) and the MIP-DM reference trajectory (magenta circles). The bottom right side of each subfigure in Fig. 9 illustrates the proposed MIP-DM, i.e., it shows the two-lane road in curvilinear coordinates, the location of the ego (blue), two obstacles (red), the traffic intersection (purple), and the MIP solution trajectory (blue solid circles) over a $T^{mip} = 4.5$ s horizon length. For each obstacle, the dark red (or dark purple) region represents the physical shape of the obstacle, while the larger shaded area corresponds to the avoidance constraints in the MIP-DM. A sequence of larger shaded areas is shown for each obstacle based on a prediction of the obstacle behavior over the MIP-DM horizon. The top right side of each subfigure in Fig. 9 shows the steering angle and velocity command in the NMPC control input trajectory over a $T^{mpc} = 2$ s horizon.

Fig. 9(a) shows the trajectories for MIP-DM and NMPC at $26$ s in the experiment, demonstrating the ego vehicle stopping at the traffic intersection. After the obstacle (Hamster $3$) finishes crossing the intersection, the ego continues by crossing the intersection at $33$ s in the experiment. Fig. 9(b) shows the trajectories at $61$ s, demonstrating the ego changing lane and overtaking a slower obstacle to achieve the desired velocity of $0.4$ m/s. Fig. 9(c) shows the trajectories at $69$ s, demonstrating the ego changing lane back to the preferred lane after overtaking the slower obstacle. Finally, Fig. 9(d) shows the trajectories at $183$ s in the experiment, demonstrating the ego queuing behind a slower obstacle because overtaking is not allowed in the top left loop of the figure eight track.

(a) Trajectories for MIP-DM and NMPC at 26 s of experiment: ego vehicle stopping at traffic intersection.

(b) Trajectories for MIP-DM and NMPC at 61 s of experiment: ego vehicle overtaking slower obstacle to achieve desired velocity.

(c) Trajectories for MIP-DM and NMPC at 69 s of experiment: ego vehicle returning to preferred lane after overtaking slower obstacle.

(d) Trajectories for MIP-DM and NMPC at 183 s of experiment: ego vehicle slowing down behind slower obstacle because overtaking is not allowed.

Figure 9: Illustration of predicted trajectories of MIP-DM (Tsmip = 0.3 s), and NMPC (Tsmpc = 0.025 s) tracking the MIP-DM reference, at certain steps of small-scale vehicle experiments. The left side of each subfigure shows the eight shaped track, the ego (blue) and two obstacles (red), safety ellipsoid around each obstacle (dashed red line), NMPC predicted trajectory (blue plus markers) and MIP-DM reference (magenta circles). The bottom right side of each subfigure shows the ego (blue), two obstacles (red), traffic intersection (purple), and MIP-DM solution (blue solid circles) in curvilinear coordinates, and the top right side shows the NMPC control input trajectory. A video is available at: https://youtu.be/FyaGRZvuqmA.

Figure 10 shows the trace of ego positions (in blue) during the $200$ s experiment, and each of the locations where the ego vehicle came to a full stop are highlighted by red dots. The ego vehicle consistently stops at a desired safety distance from the intersection before crossing. The one red dot away from the intersection is due to the queuing behavior in Fig. 9(d), where the ego stops behind an obstacle at the intersection. In addition, Fig. 10 confirms that the ego vehicle only makes lane changes in the bottom right loop of the track, demonstrating the zone-dependent traffic rules in Section 3.4. Finally, Figure 11 shows the CPU times for the BB-ASIPM solver to implement the MIP-DM during the $200$ s experiment. The computation times are always below $120$ ms and therefore real-time feasible, due to the sampling period of $T_{s}^{mip} = 300$ ms.

Figure 10: Trace of ego vehicle positions during experiments in Fig. 9: red dots indicate positions at which the ego stopped, either at the intersection or queuing behind an obstacle.

Figure 11: CPU time of BB-ASIPM solver in MIP-DM (sampling period Tsmip = 0.3 s) during the experiments in Fig. 9.

## Conclusions and Outlook

We designed a mixed-integer programming-based decision making for automated driving. The mixed-integer quadratic programming formulation uses a linear vehicle model in a road-aligned coordinate frame, it includes lane selection and lane change timing constraints, polyhedral collision avoidance and intersection crossing constraints, and zone-dependent traffic rule changes. We leveraged the recently developed embedded BB-ASIPM solver, using a branch-and-bound method with reliability branching and warm starting, block-sparse tailored presolve techniques, early termination and infeasibility detection within an active-set interior point method. The performance of the MIP-DM method was demonstrated by simulations in various scenarios including merging points and traffic intersections, and real-time feasibility was demonstrated by hardware-in-the-loop simulations on dSPACE Scalexio and MicroAutoBox-III rapid prototyping units. Finally, we presented results from experiments on a setup with small-scale vehicles, integrating the MIP-DM with a nonlinear model predictive control for reference tracking.

Future works will focus on using more advanced behavior prediction models for other vehicles and explicit handling of uncertainty in the modeling and perception of the environment, as well as deployment on full scale vehicles.
