<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimization-Based Autonomous Racing of 1: 43 Scale RC Cars

Topics include Model predictive control, Contouring control, Autonomous racing, Path planning, Real-time optimization, RC cars, Model predictive contouring control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Foundational paper for Model Predictive Contouring Control (MPCC) in vehicle racing, introducing the idea of maximizing progress along a reference path as an MPC objective. Demonstrates real-time performance on 1:43 scale RC cars at drifting speeds, and coined the contouring-control formulation widely adopted in subsequent autonomous racing and AV trajectory planning work.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper describes autonomous racing of RC race cars based on mathematical optimization. Using a dynamical model of the vehicle, control inputs are computed by receding horizon based controllers, where the objective is to maximize progress on the track subject to the requirement of staying on the track and avoiding opponents. Two different control formulations are presented. The first controller employs a two-level structure, consisting of a path planner and a nonlinear model predictive controller (NMPC) for tracking. The second controller combines both tasks in one nonlinear optimization problem (NLP) following the ideas of contouring control. Linear time varying models obtained by linearization are used to build local approximations of the control NLPs in the form of convex quadratic programs (QPs) at each sampling time. The resulting QPs have a typical MPC structure and can be solved in the range of milliseconds by recent structure exploiting solvers, which is key to the real-time feasibility of the overall control scheme. Obstacle avoidance is incorporated by means of a high-level corridor planner based on dynamic programming, which generates convex constraints for the controllers according to the current position of opponents and the track layout.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The control performance is investigated experimentally using 1:43 scale RC race cars, driven at speeds of more than 3 m/s and in operating regions with saturated rear tire forces (drifting). The algorithms run at 50 Hz sampling rate on embedded computing platforms, demonstrating the real-time feasibility and high performance of optimization-based approaches for autonomous racing.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous car racing is a challenging task for automatic control systems due to the need for handling the vehicle close to its stability limits and in highly nonlinear operating regimes. In addition, dynamically changing racing situations require advanced path planning mechanisms with obstacle avoidance executed in real-time. Fast dynamics constrain the sampling time to be in the range of a few tens of milliseconds at most, which severely limits the admissible computational complexity of the algorithms. This situation is even more challenging if the autonomous algorithms shall be executed on simple, low-power embedded computing platforms.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we investigate optimization-based control strategies for the task of racing an autonomous vehicle around a given track. We focus on methods that can be implemented to run in real-time on embedded control platforms, and present experimental results using 1:43 scale Kyosho *dnano* RC race cars that achieve top speeds of more than 3 m/s, which corresponds to an upscaled speed of about 465 km/h. For high performance, the proposed controllers operate the car at its friction limits, far beyond the linear region of what is typically used in other autonomous driving systems. This challenging task is generally mastered only by expert drivers with lots of training. In contrast, our approach requires merely a map of the track and a dynamical model of the car; in particular, we use a bicycle model with nonlinear tire forces, neglecting load transfer and coupling of lateral and longitudinal slip.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Two model-based control schemes are presented in this paper. First, we describe a hierarchical two-level control scheme consisting of a model-based path planner generating feasible trajectories for an underlying nonlinear model predictive control (NMPC) trajectory tracking controller. Our second approach combines both path planning and path following into one formulation, resulting in one NMPC controller that is based on a particular formulation known from contouring control. The objective of both approaches is to maximize the progress on the track, measured by a projection of the vehicle's position onto the center line of the track. Linear time varying (LTV) models obtained by linearization are employed to construct a tractable convex optimization problem to be solved at each sampling time. Efficient interior point solvers for embedded systems, generated by FORCES, are employed to solve the resulting optimization problems, which makes the approaches presented in this paper amenable for use on embedded systems.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We furthermore demonstrate that both schemes can easily be extended to incorporate obstacle avoidance by adjusting the constraints of the resulting optimization problems according to the racing situation. With this mechanism in place, the avoidance trajectory is optimized to yield maximal overall progress, which translates into highly effective overtaking maneuvers that are automatically planned and executed.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-A Related work", "weight": 1.0} -->

Safe autonomous driving at moderate speeds has been demonstrated for example in the context of Autonomous Highway Systems (AHS) in 1997 within the Californian PATH programme, or in contests such as the DARPA Grand Challenge in 2005 and the Urban Challenge in 2007 by numerous research groups. In these projects, the main goal was do develop autonomous driving systems for public traffic situations. Autonomous racing has received less attention, but impressive advances have been made recently also in this discipline. For instance, a fully autonomous Audi TTS has been reported to race at high speeds in using a trajectory tracking controller, which follows a pre-computed trajectory. However, to the best knowledge of the authors, fully automatic racing including obstacle avoidance in dynamic racing situations has not been demonstrated yet in practice.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-A Related work", "weight": 1.0} -->

From a control perspective, the fundamental building blocks for automatic racing can be grouped into three categories: drift control, reference tracking, and path planning. Research associated with the first group focuses on gaining a better understanding of the behavior of the car near the friction limit for designing safety control systems that try to prevent loss-of-control accidents. By analyzing the nonlinear car model, it can be shown that steady state motions corresponding to drifting can be generated, see e.g. and. As these approaches are not designed for trajectory tracking, the controlled car drifts in a circle, which represents a steady state drift equilibrium.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-A Related work", "weight": 1.0} -->

Reference tracking controllers usually are designed to operate the vehicle within the linear tire force region for maximum safety and robustness. Approaches based on NMPC, which allows one to incorporate the latter constraint in a systematic manner, deal with the nonlinearities of the model either directly by a nonlinear programming (NLP) solver, or use LTV or piece-wise affine (PWA) approximations, resulting in a convex quadratic program (QP) or a mixed-integer QP, respectively. Approaches without optimization in real-time include nonlinear robust control and flatness-based control, which however lack the ability to incorporate constraints. One approach that is explicitly designed for operating with saturated tire forces is, where the center of percussion (CoP) is used to design a state feedback steering controller for reference tracking. At the CoP, the rear tire forces do not influence the dynamics by definition, which allows for a simple linear steering controller.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-A Related work", "weight": 1.0} -->

In order to avoid obstacles, reference tracking schemes rely on a higher-level path planner. A simple point mass model in the high-level path planner is used in to limit the computational complexity. This can be problematic if the generated trajectories are infeasible with respect to the car's physical dynamics, which can lead to preventable collisions. The latter reference suggests to use a library of steady-state movements (trims) with parametrizable length, which are generated from a more complex dynamical model, and to connect them by maneuvers which allow the transition from one trim to another, similar to the idea of. This path planning has the advantage that it generates feasible reference trajectories for the low level tracking controller, and that drifting trims can be included to increase the agility of the car. However, the resulting optimization problem is a mixed-integer program that is too complex to be solved within the typical sampling times on embedded platforms. Consequently, the approach is not well suited for real-time autonomous racing.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-A Related work", "weight": 1.0} -->

In order to avoid relying on the feasibility of the path planner, one-level approaches have been investigated e.g., where optimal trajectories and the associated open-loop control inputs for rally racing maneuvers are calculated numerically in simulation. In, obstacle avoidance is incorporated into the tracking controller by using an additional cost term that penalizes coming too close to the obstacle. However, the controller is reported to perform worse than its two-level counterpart, especially if the car has to diverge from the reference trajectory. A one-level approach similar to is studied in in simulation, where obstacle avoidance is incorporated into the problem formulation by using a spatial reformulation and imposing constraints on the transformed variables. While in the solution to the NLP is obtained by a standard nonlinear solver with prohibitively long solve times, uses real-time iterations to achieve the low computation times needed for a real-time implementation. However, it is assumed that there is only one side where the obstacle can be overtaken, which may not be the case in practical racing situations.

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-A Related work", "weight": 1.0} -->

An interesting alternative to optimization-based methods are sampling-based methods. For example, rapidly exploring random trees (RRTs) have been investigated in and to generate time optimal trajectories through a 180^∘^ curve. The advantage is that such algorithms tend to quickly find feasible trajectories. In, the differential flatness of the system is exploited to speed up the convergence of the algorithm, generating obstacle-free trajectories even in complex situations. However, the reported computation times are not yet low enough to allow for a real-time implementation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

In this paper, we describe two novel autonomous, optimization-based racing controllers that incorporate obstacle avoidance, track constraints, actuator limitation and the ability for controlled drift in a systematic and straightforward way. Real-time feasibility at 50 Hz sampling rate is demonstrated in experimental results with fast RC cars. To the best knowledge of the authors, this is the first implementation of autonomous racing controllers with obstacle avoidance on an experimental testbed.

<!-- chunk {"id": "body-0016", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

The fundamental idea of both approaches is to use a receding horizon controller, which maximizes progress on the track within the horizon as a performance measure. This is closely related to a time optimality criterion and allows for a systematic incorporation of obstacles and other constraints. It is particularly effective for overtaking opponents, as our controllers seek for a progress-optimal solution around the obstacles. In order to deal with track constraints and obstacle avoidance situations, we represent the feasible set for the position of the car at any time instance by a slab defined by two parallel linear inequalities. This ensures tractability of the subproblems by convex programming on one hand, and incorporation of track and obstacle constraints in a systematic manner on the other hand. To deal with non-convex situations such as overtaking an obstacle on the left or right, a high-level corridor planning algorithm supplies a set of appropriate convex constraints to the controllers. This constraint set is the result of a shortest path problem solved by dynamic programming.

<!-- chunk {"id": "body-0017", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

The first, hierarchical control approach presented in this paper is in principle similar to, but its complexity is low enough to be fully implemented in real-time. Our path planner also uses trims, but only *one* is selected for the whole prediction horizon from a set of trajectories, which represent steady-state cornering conditions of the nonlinear model, gridded for velocity and steering angle. The path planner selects the trajectory with the largest progress that does not leave the track or hits any obstacle. Moving obstacles can inherently be dealt, as new trims are generated every sampling time. A low level nonlinear reference tracking MPC controller tracks the selected trim, as, but we additionally use obstacle avoidance constraints as described above, which turns out to be very effective in practice.

<!-- chunk {"id": "body-0018", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

The second controller is based on a model predictive contouring control (MPCC) formulation, combining path generation and path tracking into one problem. The MPCC essentially plans a progress-optimal path by taking into account the (nonlinear) projection of the vehicle's position onto the center line. The resulting controller is able to plan and to follow a path which is similar to the time-optimal path in when the horizon is chosen long enough.

<!-- chunk {"id": "body-0019", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

Both NMPC problems are approximated locally by linearizing the continuous nonlinear system dynamics around a state trajectory to obtain an LTV model. In the hierarchical approach, we linearize around the trajectory obtained from the path planner, while in the one-level approach the linearization points are given by the shifted trajectory from the previous sampling time. We then discretize by the matrix exponential, and solve the resulting quadratic program (QP) by a tailored interior point solver, generated by FORCES. The computation time of the solvers scale linearly with the horizon length, hence we make use of long horizons of up to 40 time steps in the MPCC, for example. After the QP has been solved, the first control input is applied to the system, and the process is repeated at the next sampling time. This approach for solving the NMPC problems corresponds to the basic version of the real-time iterations.

<!-- chunk {"id": "body-0020", "role": "body", "section": "I-C Outline", "weight": 1.0} -->

The paper is organized as follows. In Section II, the dynamical model of the car and some of its basic properties are described. In Section III-A, we present the hierarchical control approach with separate path planner and path tracking, while the combined approach is presented in Section III-B. In Section III-C, we briefly discuss our method for selecting convex constraints for the two controllers, enabling obstacle avoidance in dynamic racing situations. Section IV presents the testbed setup and experimental results for both controllers.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-A Bicycle Model", "weight": 1.0} -->

The RC cars are modeled using a bicycle model as done, where the car is modeled as one rigid body with a mass $m$ and an inertia $I_{z}$, and the symmetry of the car is used to reduce it to a bicycle. Only the in-plane motions are considered, i.e. the pitch and roll dynamics as well as load changes are neglected. As the used cars are rear wheel driven and do not have active brakes, the longitudinal force on the front wheel is neglected.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-A Bicycle Model", "weight": 1.0} -->

The equation of motion is derived around the center of gravity (CoG), where the states are the position $X$, $Y$ of the CoG in the inertial frame and the angle of the car relative to the inertial frame, $\varphi$. This is the kinematic part of the model. The kinetic part of the model is derived around a body-fixed frame centered at the CoG, where the states are the longitudinal and lateral velocity of the car, $v_{x}$ and $v_{y}$, and finally the yaw rate $\omega$. The control inputs are the PWM duty cycle $d$ of the electric drive train motor and the steering angle $\delta$. The subscripts $x$ and $y$ indicate longitudinal and lateral forces or velocities, while $r$ and $f$ refer to the front and rear tires, respectively. Finally, $l_{f}$ and $l_{r}$ are the distance from the CoG to the front and the rear wheel.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A Bicycle Model", "weight": 1.0} -->

The tire forces $F$ model the interaction between the car and the road and are the most important part of the dynamics. As the goal is for the cars to race, the model of the tire forces has to be realistic enough to represent the car at high speeds and its handling limits.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-A Bicycle Model", "weight": 1.0} -->

The parameters $B$, $C$ and $D$ define the exact shape of the semi-empirical curve. The longitudinal force of the rear wheel $F_{r,x}$ is modeled using a motor model for the DC electric motor as well as a friction model for the rolling resistance and the drag, cf. (2c). Due to the size of the cars, it is currently not feasible to measure the wheel speed, which makes it impossible to use combined slip models such as.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-A Bicycle Model", "weight": 1.0} -->

The model is identified using a combination of stationary and dynamic identification experiments, as reported. This allows for identifying the rear wheel combined slip effects into the lateral tire friction model (2b). Thus the identified model is suitable to represent the car also at its handling limits, when the tire forces are saturated or close to saturation.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-B Stationary Velocity Analysis", "weight": 1.0} -->

For a better understanding of the model, the stationary velocities of the model are investigated. A similar, more elaborate analysis is presented.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-B Stationary Velocity Analysis", "weight": 1.0} -->

The objective is to find points in the model where all accelerations are zero. This is done for different constant forward velocities ${\overline{v}}_{x}$ and constant steering angles $\overline{\delta}$, thus the problem becomes a nonlinear algebraic system of equations, with two equations (${{\overset{˙}{v}}_{y} = 0},$ $\overset{˙}{\omega} = 0$) and two unknowns (${\overline{v}}_{y},$ $\overline{\omega}$). By finding a solution to the algebraic equations for different steering angles $\overline{\delta}$ and different initial conditions, the stationary velocities for one forward velocity (${\overline{v}}_{y},$ $\overline{\omega}$) can be calculated.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-B Stationary Velocity Analysis", "weight": 1.0} -->

The resulting stationary velocities are shown for ${\overline{v}}_{x} = 1.5$ m/s and ${\overline{v}}_{x} = 2$ m/s in Figure 2. The resulting stationary velocities can be categorized into three different regions. The blue line is the normal driving region, which is characterized by the linear dependency of the yaw rate and the steering angle, as well as small lateral velocities. The other two regions in red and green correspond to over- and understeering points in the model. In the understeering region (green curves), the saturated front tire force law prevents the car from achieving larger yaw rates, and thus the car can not take a sharper turn. In the oversteering region (red curves), the rear tire force law is fully saturated and the car drives with a high lateral velocity, which is usually called drift.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-B Stationary Velocity Analysis", "weight": 1.0} -->

The dynamics of the model in the different regions are different, for example in the oversteering region where the car is drifting, the steering angle can be of opposite sign than the curvature the car is driving, known as counter steering, which does not occur in the case of the normal and the understeering mode. A stability analysis of the lateral velocity model around the different stationary velocity points also shows the difference in the dynamics: While the normal driving region and the understeering region are stable, the drifting region is unstable.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-B Stationary Velocity Analysis", "weight": 1.0} -->

From Figure 2 it is visible that the normal steering region is getting smaller when the car is driving faster. Thus the maximal and minimal steering angle for which the tire forces are not saturated is reduced with increasing velocities, and at the same time the maximal yaw rate decreases.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-B Stationary Velocity Analysis", "weight": 1.0} -->

Because all velocities are constant, the movement of the car is a uniform circular movement, for which the relationship between the yaw rate, the radius $R$ and the curvature $\kappa$ is known,

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-B Stationary Velocity Analysis", "weight": 1.0} -->

Consequently, all stationary velocity points correspond to the car driving in a circle with a constant radius, i.e. the model can predict drifting along a circle.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Autonomous Racing Control", "weight": 1.0} -->

In this main part of the paper, we present two optimization-based formulations for the task of autonomous racing for RC cars which are based on the model described in Section II. First, the hierarchical two-level approach is presented in Section III-A, followed by the one-level scheme in Section III-B. We then briefly discuss a high-level method for obstacle avoidance that is the same for both controllers in Section III-C. A summary of the algorithms is given in Section III-D.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-A Hierarchical Receding Horizon Controller", "weight": 1.0} -->

In our hierarchical control approach, a high-level path planner finds a progress-optimal, feasible trajectory within a finite number of possibilities and for a horizon of $N$ sampling times. This trajectory is then tracked by an MPC controller employing soft-constraints to ensure feasibility of the low-level optimization at all times. This process is repeated in a receding-horizon fashion, hence we call the controller Hierarchical Receding Horizon Controller (HRHC) in what follows. Details on the individual components are given in the following.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-A1 Path Planning", "weight": 1.0} -->

The purpose of the path planner is to generate a trajectory with maximal progress which is feasible for the car's dynamics. It is based on gridding the stationary velocities of the nonlinear system described in Section II-B. By solving for the stationary lateral velocity points given a set of different longitudinal velocities ${\overline{v}}_{x}$ and steering angles $\overline{\delta}$, a library of zero acceleration points is generated. This includes stationary velocities from the normal as well as from the drifting region. Table I shows an excerpt of such a library. The library used in our experiments consists of $N_{\overline{v}} = 95$ stationary points, out of which 26 correspond to drifting equilibria. The stationary points are selected by uniformly gridding the longitudinal velocity $v_{x}$ between 0.5 and 3.5 m/s, with steps of 0.25 m/s.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-A1 Path Planning", "weight": 1.0} -->

For each ${\overline{v}}_{x}$, about five to nine points are selected in the normal driving region, and up to four drifting points are selected for forward velocities between 1.5 and 2.25 m/s. Note that the library does not change during run-time, hence it can be generated offline.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-A1 Path Planning", "weight": 1.0} -->

To generate trajectories for the whole horizon, the stationary points are integrated. This is computationally cheap under the assumption that the stationary velocity can be reached within one time step, since in this case all accelerations are zero. This procedure allows us to generate reference trajectories also for unstable drifting points. The integration of the reasonable stationary velocity points leads to a countable set of possible trajectories with a constant turning radius over the horizon. A visualization of such a set of candidate trajectories is shown in Figure 3.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-A1 Path Planning", "weight": 1.0} -->

where $x_{k} \triangleq {(X_{k},Y_{k},\varphi_{k})}$ is the position and orientation at time step $k$ generated by integrating the kinematic part of the bicycle model using the stationary velocity ${\overline{v}}^{j} \triangleq {({\overline{v}}_{x}^{j},{\overline{v}}_{y}^{j},{\overline{\omega}}^{j})}$ from the library of stationary points. The integration is denoted by the discrete time version of the model, $f_{km}$ in (4c).

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-A1 Path Planning", "weight": 1.0} -->

The objective (4a) is to find the trajectory with the largest progress on the track, which is measured by the projection operator $\mathcal{P}:{{\mathbb{R}}^{2}\rightarrow{\lbrack 0,L\rbrack}}$ that calculates the scalar projection of the position $X_{k}^{j},Y_{k}^{j}$ onto the piecewise linear center line parameterized by the arc length $\theta \in {\lbrack 0,L\rbrack}$, where $L$ is the length of the center line. All positions of the trajectory ${{{x_{k}^{j},k} = 0},{\ldots,N}},$ need to lie in the set $\mathcal{X}_{track} \subset {\mathbb{R}}^{2}$ (4d) which is the set of all admissible positions inside the track boundaries.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-A1 Path Planning", "weight": 1.0} -->

where the two cases correspond to selecting non-drift or drift trajectories, respectively, based on the lateral steady state velocity ${\overline{v}}_{y}$. The tuning parameters $\nu,\rho,\sigma_{x},\sigma_{y},\sigma_{\omega}$ are used to determine the behavior of the path planner in terms of selecting candidate trajectories. Choosing parameters that lead to too loose constraints in result typically in physically impossible trajectories, which can result in crashes. Conversely, constraints that are too tight limit the performance of the controller, as the planned trajectories are too conservative.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-A1 Path Planning", "weight": 1.0} -->

Problem is an integer program with the decision variable $j$ and solved by enumeration in practice by checking the discrete positions against local convex inner approximations of the track set, which is reasonable due to the relatively small number of trajectories (about one hundred in our case). The result of the optimization problem is visualized in Figure 3. The path planning allows to efficiently handle drift, as a drifting trajectory is selected if it yields the largest progress.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-A1 Path Planning", "weight": 1.0} -->

The path planner has some limitations. Firstly, on one hand, the horizon length has to be quite short, otherwise the planned trajectories become circles and always yield infeasibilities with respect to the track constraints, even if the selected velocity would be well suited for the current state. A horizon which is too short, on the other hand, leads to poor performance as the path planner recognizes a forthcoming curve too late. The second problem is that the whole horizon has the same velocity, which can lead to problems in complicated curve combinations such as chicanes.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-A2 Model Predictive Reference Tracking", "weight": 1.0} -->

The reference trajectory from the path planner is generated under simplifying assumptions, thus it is not possible to directly apply the controls which correspond to the stationary velocity point.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-A2 Model Predictive Reference Tracking", "weight": 1.0} -->

where $Q \in {\mathbb{S}}_{+ +}^{6}$, $R \in {\mathbb{S}}_{+ +}^{2}$, $P \in {\mathbb{S}}_{+ +}^{6}$ are tuning matrices and ${p,q} \in {\mathbb{R}}_{+ +}$ are penalties for the soft constraints (6d), which are discussed below. To capture as much of the nonlinear model as possible while maintaining computational tractability, the model is linearized around the reference trajectory, cf. (6c). It is necessary to linearize around a trajectory rather than a single operating point, since both position and orientation can vary significantly over the horizon. The reference trajectory is by construction feasible with respect to the track. In order to also guarantee that the trajectory of the optimal MPC solution satisfies track constraints, the $X$ and $Y$ states are limited to stay inside the track if possible.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-A2 Model Predictive Reference Tracking", "weight": 1.0} -->

This is achieved by limiting each point in the horizon to lie within two parallel half spaces (6d), which leads to two affine inequality constraints per time step (one for the right and one for the left border), resulting in a convex feasible set. Figure 4 depicts these border constraints (6d), which we formulate as soft constraints in order to avoid infeasibility problems in practice. By using an exact penalty function (an infinity norm in our case), we ensure that the resulting optimization problem is always feasible, and that the original solution of the hard constrained problem is recovered in case it would admit a solution. Finally, the control inputs are limited within their physical constraints, and all other states are limited within reasonable bounds to avoid convergence problems of the solver due to free variables (6f), (6g).

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-A2 Model Predictive Reference Tracking", "weight": 1.0} -->

Problem can be reformulated as a convex QP and thus efficiently solved. In this work FORCES, is employed to generate tailored C-code that solves instances of where parameters are the initial state $x$, the matrices defining the dynamics along the reference trajectory ($A_{k},B_{k},g_{k}$) as well as the changing halfspace constraints $F_{k},f_{k}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-B Model Predictive Contouring Control", "weight": 1.0} -->

Contouring control is used in various industrial applications such as machine tools for milling and turning or laser profiling. In these applications, the challenge is to compute inputs that control the movement of the tool along a reference path. The latter is given only in spatial coordinates; the associated velocities, angles, etc. are calculated and imposed by the control algorithm. This is different from tracking controllers in that the controller has more freedom to determine the state trajectories to follow the given path, for example to schedule the velocity, which in tracking is defined by the reference trajectory.

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-B Model Predictive Contouring Control", "weight": 1.0} -->

The contour following problem can be formulated in a predictive control framework to incorporate constraints, see e.g.. In this work, we adapt the particular formulation of the model predictive contouring control (MPCC) framework from to obtain a high-performance controller for autonomous racing, which maximizes the travelled distance on the reference path within the prediction horizon. In our experiments, we use the center line as a reference path, but employ it merely as a measure of progress by selecting low weights on the tracking (contouring) error. As a result, the driven trajectory is very similar to those driven by expert drivers. The advantage of this approach is that path planning and path tracking can be combined into one nonlinear optimization problem, which can be solved in real-time by approximating the NLP using local convex QP approximations at each sampling time. The resulting QPs can be formulated with multistage structure, which is exploited by FORCES to obtain solution times in the range of a few milliseconds.

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-B Model Predictive Contouring Control", "weight": 1.0} -->

Before posing the MPCC problem, a few preliminaries are introduced such as the parameterization of the reference path and the definition of useful error measures.

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-B1 Parameterization of Reference Trajectory", "weight": 1.0} -->

The reference path is parameterized by its arc length $\theta \in {\lbrack 0,L\rbrack}$ using third order spline polynomials, where $L$ is the total length. The splines are obtained by an offline fitting of the center line. Using this parameterization, we can obtain any point ${X^{\text{ref}}{(\theta)}},{Y^{\text{ref}}{(\theta)}}$ on the center line by evaluating a third order polynomial for its argument $\theta$. The angle of the tangent to the path at the reference point with respect to the $X$-axis,

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-B1 Parameterization of Reference Trajectory", "weight": 1.0} -->

is also readily available. This parameterization leads to an accurate interpolation within the known points of the reference path, and it is more accurate than the piece-wise linear parameterization employed for the HRHC in Section III-A, which only uses a linear interpolation between the points.

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-B2 Error measures", "weight": 1.0} -->

In order to formulate the MPCC problem, error measures are needed that define the deviation of the car's current position $X,Y$ from the desired reference point ${X^{\text{ref}}{(\theta)}},{Y^{\text{ref}}{(\theta)}}$. We use the same definitions as, but give another derivation here. Let $\mathcal{P}:{{\mathbb{R}}^{2}\rightarrow{\lbrack 0,L\rbrack}}$ be a projection operator on the reference trajectory defined by

<!-- chunk {"id": "body-0053", "role": "body", "section": "III-B2 Error measures", "weight": 1.0} -->

For brevity, we define $\theta_{\mathcal{P}} \triangleq {\mathcal{P}{(X,Y)}}$. The orthogonal distance of the car from the reference path is then given by the *contouring error*

<!-- chunk {"id": "body-0054", "role": "body", "section": "III-B2 Error measures", "weight": 1.0} -->

where $\Phi{( \cdot )}$ is defined. The contouring error is depicted in the left picture in Figure 5.

<!-- chunk {"id": "body-0055", "role": "body", "section": "III-B2 Error measures", "weight": 1.0} -->

The projection operator is not well suited for use within online optimization algorithms, as it resembles an optimization problem itself. Thus an approximation $\theta_{\mathcal{A}}$ of $\theta_{\mathcal{P}}$ is introduced, which is an independent variable determined by the controller. For this approximation to be useful, it is necessary to link $\theta_{\mathcal{A}}$ to $\theta_{\mathcal{P}}$ via the *lag error*

<!-- chunk {"id": "body-0056", "role": "body", "section": "III-B2 Error measures", "weight": 1.0} -->

which measures the quality of the approximation. The lag error is depicted in the right picture in Figure 5 (red segment on reference path).

<!-- chunk {"id": "body-0057", "role": "body", "section": "III-B2 Error measures", "weight": 1.0} -->

The approximate contouring error ${\hat{e}}^{c}$ (11a) and the approximate lag error ${\hat{e}}^{l}$ (11b) are defined as the orthogonal and tangential component of the error between ${X^{\text{ref}}{(\theta_{\mathcal{A}})}},{Y^{\text{ref}}{(\theta_{\mathcal{A}})}}$ and the position ${X,Y},$ see the right picture in Figure 5.

<!-- chunk {"id": "body-0058", "role": "body", "section": "III-B3 MPCC problem", "weight": 1.0} -->

With these error measures in place, we now formulate the model predictive contouring control problem for autonomous racing.

<!-- chunk {"id": "body-0059", "role": "body", "section": "III-B3 MPCC problem", "weight": 1.0} -->

where $X_{k},Y_{k}$ is the position of the car at time step $k$ determined by the nonlinear model $f$ in (12c), which is the discrete-time version of with piece-wise constant control inputs. The contouring error $e_{k}^{c}{(X_{k},Y_{k},\theta_{\mathcal{P}})}$ in the objective (12a) is defined, and $\theta_{\mathcal{P},k}$ is the associated path parameter such that ${X^{\text{ref}}{(\theta_{\mathcal{P},k})}},{Y^{\text{ref}}{(\theta_{\mathcal{P},k})}}$ is the orthogonal projection of $X_{k},Y_{k}$ onto the reference path.

<!-- chunk {"id": "body-0060", "role": "body", "section": "III-B3 MPCC problem", "weight": 1.0} -->

The two objectives (maximum progress and tight path following) are traded off by the weights $\gamma \in {\mathbb{R}}_{+ +}$ and $q_{c} \in {\mathbb{R}}_{+ +}$, respectively. Constraints (12d) are the parallel half space constraints for containing the position in the allowed corridor as described in Section III-A2, while (12e), (12f) corresponds to (6f), (6g), limiting states and inputs to physically admissible values.

<!-- chunk {"id": "body-0061", "role": "body", "section": "III-B3 MPCC problem", "weight": 1.0} -->

Due to the implicit dependency of the objective (12a) on the projection operator, optimization problem is a bi-level NLP, which is too complex to solve in real-time. Thus the idea is to use the approximate projection $\theta_{\mathcal{A},k}$ instead of $\theta_{\mathcal{P},k}$ as introduced in Section III-B2, and to control the approximation quality by adding a cost on the lag error to the objective. In order to allow for forming the lag error at each time step in the prediction horizon, it is necessary to introduce an integrator state with dynamics $\theta_{\mathcal{A},{k + 1}} = {\theta_{\mathcal{A},k} + {v_{k}/T_{s}}}$, where $v_{k}$ can be interpreted as the *projected velocity*, and $\theta_{\mathcal{A},k}$ as the *state of progress* at time $k$, respectively.

<!-- chunk {"id": "body-0062", "role": "body", "section": "III-B3 MPCC problem", "weight": 1.0} -->

where ${\Deltau_{k}} \triangleq {u_{k} - u_{k - 1}}$ and ${\Deltav_{k}} \triangleq {v_{k} - v_{k - 1}}$. Note that the approximate contouring error ${\hat{e}}_{k}^{c}{(X_{k},Y_{k},\theta_{\mathcal{A},k})}$ (11a) is used in the objective (13a). Furthermore, we have replaced the maximization of the final progress measure, $\theta_{\mathcal{P},N}$, by $\sum_{k = 0}^{N - 1}{v_{k}T_{s}}$, which is equivalent if the approximation is accurate. Sensible lower and upper bounds on $\theta_{k}$ and $v_{k}$ are imposed to avoid spurious solutions of the NLP, with $\overline{v}$ denoting the largest possible progress per sampling time.

<!-- chunk {"id": "body-0063", "role": "body", "section": "III-B3 MPCC problem", "weight": 1.0} -->

The cost on the lag error ${\hat{e}}_{k}^{l}{(X_{k},Y_{k},\theta_{\mathcal{A},k})}$ in (13a) links the state of progress to the dynamics of the car. To ensure an accurate progress approximation and thus a strong coupling between the cost function and the car model, the weight on the lag error $q_{l} \in {\mathbb{R}}_{+ +}$ is chosen high as suggested. Furthermore, a cost term on the rate of change of the inputs is added to the objective (13a) in order to penalize fast changing controls, which helps to obtain smooth control inputs in order to prevent amplifying unmodeled dynamics.

<!-- chunk {"id": "body-0064", "role": "body", "section": "III-B4 Solving the MPCC problem", "weight": 1.0} -->

where $\Gamma_{k} \in {\mathbb{S}}_{+}^{7}$ is formed by the quadratic part of the linearized contouring and lag error cost function from (13a) and $c_{k} \in {\mathbb{R}}^{7}$ stems from the linear part, respectively. In order to keep the linearization error small, we use an LTV approximation of the dynamics as well as of the contouring and lag errors. Each nonlinear function is linearized around the output of the last QP iteration shifted by one stage. The measurement $x = x_{0}$ is used as the first linearization point, and the last input of the previous iteration is kept constant to generate a new last input. The linearization point for the terminal state $x_{N}$ is calculated by simulating the nonlinear model for one time step.

<!-- chunk {"id": "body-0065", "role": "body", "section": "III-B4 Solving the MPCC problem", "weight": 1.0} -->

The track or corridor constraints (14e) are formulated by two half space constraints tangential to the track per time step, as described in Section III-A. These constraints are formulated as soft constraints, with slack variables $s_{k} \in {\mathbb{R}}^{2}$ and a corresponding infinity-norm penalty in the objective (14a) weighted by $q \in {\mathbb{R}}_{+ +}$, which is chosen quite high to recover the behavior of the hard constrained problem whenever possible.

<!-- chunk {"id": "body-0066", "role": "body", "section": "III-B4 Solving the MPCC problem", "weight": 1.0} -->

Note that the described re-linearization scheme is essentially the basic real-time iteration, where a nonlinear continuous-time optimal control problem is solved using a multiple shooting technique, with an exponential map as integrator, and in every time step only one step of a sequential QP (SQP) scheme is performed. Hence the convergence properties that are known for the real-time iteration hold also for the MPCC problem.

<!-- chunk {"id": "body-0067", "role": "body", "section": "III-B4 Solving the MPCC problem", "weight": 1.0} -->

The local QP is solved using FORCES. Due to the rate costs, the problem has to be lifted to obtain the multistage structure, for which FORCES has been designed, by introducing a copy of the previous control input at each stage.

<!-- chunk {"id": "body-0068", "role": "body", "section": "III-C Obstacle Avoidance", "weight": 1.0} -->

The two controllers presented in this section plan a path within the track, or a corridor, by taking into account constraints (4d), (6f) or (14e) on the position of the car. Thus it is possible to include obstacle avoidance by adapting this corridor online depending on the current constellation of opponents. Generating the optimal corridor based on the position of the obstacles is in general hard, because of the fundamental problem that the decision on which side to overtake is non-convex and of combinatorial nature if more than one opponent is involved. This situation is depicted in Figure 6 in the left picture.

<!-- chunk {"id": "body-0069", "role": "body", "section": "III-C Obstacle Avoidance", "weight": 1.0} -->

In this work, we employ a high level path planner based on dynamic programming (DP) to decide on which side to overtake the obstacles. Based on the result of the DP, the adapted corridor is given to the controllers of Section III-A or Section III-B. The high level path planner solves a shortest path problem on a spatial-temporal grid, cf. Figure 6. To incorporate the planned path of the lower level controller into the DP, the grid is built up based on the last output of the path planner in the case of the HRHC or the last QP solution in the case of the MPCC. The DP minimizes the travelled distance, and additionally the deviation from the last plan of the lower level controller, such that the DP path is close to the state prediction of the lower level controller. This ensures that the linearizations stay approximately valid most of the time. Based on the optimal trajectory from the DP, the corridor constraints can easily be identified, see the right picture in Figure 6.

<!-- chunk {"id": "body-0070", "role": "body", "section": "III-C Obstacle Avoidance", "weight": 1.0} -->

Due to space restrictions, we do not go further into detail, but many references exist that solve the corridor problem with different approaches. For example, a similar problem had to be solved during the DARPA Urban challenge where the goal was autonomous driving in city traffic. In several approaches to this problem are presented, for example based on model predictive trajectory generation algorithms, modified $A^{\star}$-algorithms or RRTs.

<!-- chunk {"id": "body-0071", "role": "body", "section": "III-D Summary", "weight": 1.0} -->

In this main part of the paper, we have presented two approaches for automatic racing. Both approaches are model-based and maximize progress within a given time horizon. They directly incorporate track and obstacle constraints by using two parallel affine inequalities (slabs) representing the feasible set of positions at each time. The major difference between the approaches is that the first (cf. Section III-A and Algorithm 1) is a two-level approach with a separate path planning mechanism combined with a reference tracking MPC controller, while the second approach (cf. Section III-B and Algorithm 2) formulates both tasks (path planning and path tracking) into one nonlinear optimal control problem based on model predictive contouring control.

<!-- chunk {"id": "body-0072", "role": "body", "section": "III-D Summary", "weight": 1.0} -->

1:get current position and velocities
2:compute delay compensation
4: shift old planned path by one stage
5: get position of opposing cars
6: run DP and get new borders (Sec. III-C)
8:run path planner
9:linearize and discretize the model, i.e. build problem
10:solve QP using FORCES
11:send first control at the end of time slot

<!-- chunk {"id": "body-0073", "role": "body", "section": "III-D Summary", "weight": 1.0} -->

1:get current position and velocities
2:compute delay compensation
3:augment old QP output (Section III-B4)
5: get position of opposing cars
6: run DP and get new borders (Sec. III-C)
8:linearize and discretize the model and the cost function, i.e. build problem
9:solve QP using FORCES
10:send first control at the end of time slot
Algorithm 3 HRHC and MPCC algorithm

<!-- chunk {"id": "body-0074", "role": "body", "section": "III-D Summary", "weight": 1.0} -->

Both controllers send the new control input at the end of the sampling period. In order to compensate for this fixed delay, the nonlinear model is simulated forward for this time interval at the beginning of the algorithm, see line 2 of Algorithm 1 and 2. The nonlinear model is integrated using a second-order Runge-Kutta method with the current state estimate from the Kalman filter as the initial condition.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Results", "weight": 1.0} -->

In this section the performance of both controllers is evaluated on an experimental testbed using 1:43 scale RC race cars. Details on the experimental setup, the particular implementation and closed-loop performance are given in the following.

<!-- chunk {"id": "body-0076", "role": "body", "section": "IV-A Experimental Setup", "weight": 1.0} -->

For our experiments, we use the Kyosho *dnano* cars, which are quite sophisticated with a front and rear suspension and a rear axle differential. The cars are able to reach speeds of over 3 m/s on straights, which corresponds to an upscaled speed of about 465 km/h. The wide speed range, the high maximal forward velocity and the small scale introduce further complexity which is not present in full size testbeds.

<!-- chunk {"id": "body-0077", "role": "body", "section": "IV-A Experimental Setup", "weight": 1.0} -->

The testbed further consists of an infrared camera tracking system, a control board and a custom built race track of length $L = 18.43$ m (measured at the center line), see Figure 7. A PointGrey Flea3 camera captures 100 frames per second with an accuracy of below 4 mm. A wide angle lens with an infrared filter is used to capture the 4 by 4 meter track. Reflecting markers are arranged on the cars in different unique patterns and used to identify the car and to measure the position and angle of the cars. An Extended Kalman Filter (EKF) is used for state estimation, filtering the vision data and estimating the longitudinal and lateral velocity as well as the yaw rate. The vision data of all cars is passed over an Ethernet connection to a control PC, which runs one of the two control algorithms described in Section III together with the corridor planner solving the DP problem. The calculated inputs are then sent via Bluetooth to the car.

<!-- chunk {"id": "body-0078", "role": "body", "section": "IV-A Experimental Setup", "weight": 1.0} -->

As the original electronics of the *dnano* cars does not feature an open digital communication link, we have replaced it by a custom made PCB, featuring a Bluetooth chip, current and voltage sensors, H-bridges for DC motor actuation, and an ARM Cortex M4 microcontroller for the low level control loops such as steering servo and traction motor control.

<!-- chunk {"id": "body-0079", "role": "body", "section": "IV-B Implementation", "weight": 1.0} -->

The HRHC is implemented in ANSI C on an embedded platform using an ARM A9 chip (Exynos 4412) at 1.7 GHz. The chip is identical to the one used in Samsung Galaxy S3 smartphones. The runtime environment was Ubuntu Linux version 12.11, and the code was compiled with the GCC compiler 4.6.3 with option -O2. The sampling time of the controller is $T_{s} = 20$ ms, while the discretization time of the path planner and the tracking MPC controller is 25 ms. The horizon length is $N = 14$ time steps, which gives an ahead prediction of $0.35$ s. The tracking MPC controller results in a multistage QP with $9$ variables per stage, i.e. $132$ variables in total. We use a library of $95$ candidate trajectories, out of which $26$ are drifting stationary velocity points.

<!-- chunk {"id": "body-0080", "role": "body", "section": "IV-B Implementation", "weight": 1.0} -->

The MPCC does not have the limitation of the HRHC path planner, or in other words, the acceleration is not zero over the whole horizon, thus it is possible to use longer horizons which should increase the performance. Hence the controller runs with a horizon length of $N = 40$ with a sampling time of $T_{s} = 20$ ms, which corresponds to a $0.8$ s ahead prediction. With the re-linearization method presented in Section III-B4, the discretization and sampling time have to be the same, as the re-linearization is based on the last QP solution. The resulting QP has 14 variables per stage and 570 in total.

<!-- chunk {"id": "body-0081", "role": "body", "section": "IV-B Implementation", "weight": 1.0} -->

The MPCC is implemented on a newer gereration embedded platform using an Exynos 5410 chip based on the ARM Cortex A15 architecture and running at 1.6 GHz. The chip is identical to the one used in the Korean version of the Samsung Galaxy S4 smartphone. The embedded board runs Ubuntu Linux version 12.04. The ANSI C code of the MPCC controller has been compiled with GCC 4.6.3 with option -O3. To improve the convergence of the QP, the problem data is scaled to lie between $- 1$ and $+ 1$, and the objective (Hessian and linear term) is scaled by a factor of $0.1$ to reduce large entries occurring due to the lag error term. Note that these scalings do not change the minimizer. The optimality criteria of the FORCES solver are adjusted such as to terminate once a sufficiently good solution has been found, with the residuals of the equality and inequality constraints set to $10^{- 5}$, and with the duality gap set to $10^{- 4}$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "IV-C Single Car Racing", "weight": 1.0} -->

The driven trajectories for a single car are depicted in Figure 8, with the velocity profile encoded in colors. Depicted are three laps, for which the HRHC achieves a lap time between 9.5 to 9.8 s while the MPCC yields lap times between 8.9 and 9.2 s.

<!-- chunk {"id": "body-0083", "role": "body", "section": "IV-C Single Car Racing", "weight": 1.0} -->

To better understand the driven trajectory of the HRHC, the path planner of the HRHC has to be analyzed. The path planner has a comparably short prediction horizon, and all velocities over the whole horizon are constant, which leads to turns of constant radius. Such a path planner works fine for 90^∘^ and even up to 180^∘^ curves. However, the car tends to drive to the outer border after the curve, as this allows driving a wider radius at a faster longitudinal velocity and thus maximizes the progress. However, this is a limitation if the car should drive a combination of curves, where the position of the car at the end of the first curve is essential for a low overall time. This problem can be seen in Figure 8, for example in the chicane in the lower left corner. Furthermore, due to the short lookahead, the HRHC path planner is not able to prevent such an ill positioning relative to a curve ahead.

<!-- chunk {"id": "body-0084", "role": "body", "section": "IV-C Single Car Racing", "weight": 1.0} -->

Due to the suboptimal position relative to the curve, the controller has to brake more compared to a car on the ideal line and it is even possible that the car touches the borders, see the narrow 180^∘^ curve in the center of the track in Figure 9.

<!-- chunk {"id": "body-0085", "role": "body", "section": "IV-C Single Car Racing", "weight": 1.0} -->

These limitations are not present in the MPCC approach, where a comparably long horizon is employed. Unlike the HRHC, the velocity is not fixed over the horizon but computed for each time step as the result of the NLP. As a consequence of these features, the MPCC is able to plan a path even through a complicated combination of curves. This results in a trajectory which is closer to an ideal line in a least curvature sense, especially through complicated curves like the chicane in the lower left corner of Figure 8. In this curve combination, the MPCC achieves velocities not smaller than $1$ m/s, while the HRHC has to reduce the velocity to nearly $0.5$ m/s to drive through the chicane, and additionally causes the car to drive an overall longer distance.

<!-- chunk {"id": "body-0086", "role": "body", "section": "IV-C Single Car Racing", "weight": 1.0} -->

However, the MPCC has some disadvantages compared to the HRHC. In our current implementation, the MPCC still tracks the center line, which can be seen on the first straight, after the top left corner where a movement to the center line is clearly visible in Figure 8. This is clearly due to the objective function of the MPCC, and cannot be completely avoided, even if the contouring cost is small. The HRHC on the other hand does not have any cost related to the center line and only uses it as a measure of progress, thus the car drives straight in the aforementioned segment of the track. The second disadvantage can be seen in the S-curve at lower end of the track, where the MPCC has a small S shape in the driven trajectory. The HRHC on the other hand shows that the section can be driven completely straight, which gives a speed benefit. This can be most probably also attributed to the contouring error penalty, for which it would be beneficial to drive an S-shape in order to follow the center line.

<!-- chunk {"id": "body-0087", "role": "body", "section": "IV-C Single Car Racing", "weight": 1.0} -->

In summary, our results indicate that the HRHC is limited by the path planner, and the fact that the whole horizon has the same velocity. Allowing multiple velocities within one prediction horizon would most probably increase the performance of the controller. However, the complexity in the path planner grows exponentially with the number of different velocity triples in the horizon. The MPCC, which does not have this limitation, is able to plan better trajectories which also improve the closed loop performance. However, the MPCC comes at a price, first in terms of computational cost (it is about a factor of five more expensive than the HRHC when comparing computation times on the same platform, see Section IV-E for more details on computation times) and, second, in terms of robustness. During our experiments, the re-linearization scheme turned out to be sensitive to measurement errors and model drift. In particular, sudden unexpected skidding of the car can cause problems in the re-linearization scheme. Such drifts are also responsible for the high variations between different trajectories in certain areas of the track.

<!-- chunk {"id": "body-0088", "role": "body", "section": "IV-C Single Car Racing", "weight": 1.0} -->

Furthermore, since the MPCC relies on the results from the previous iteration to compute the linearizations, sudden jumps in the high-level corridor path planner might make the previous trajectory infeasible. In such a situation, several time steps might be needed to recover feasibility of the planned trajectory, although by using the soft constrained formulation sensible inputs are still provided to the car. The HRHC on the other hand does not need any information from the last iteration as only the current position and velocity is needed. This helps to deal efficiently with unexpected behavior and fast changing measurements or corridors from the high-level obstacle avoidance mechanism.

<!-- chunk {"id": "body-0089", "role": "body", "section": "IV-C Single Car Racing", "weight": 1.0} -->

HRHC controller (Section III-A) MPCC controller (Section III-B)

<!-- chunk {"id": "body-0090", "role": "body", "section": "IV-D Racing with multiple cars", "weight": 1.0} -->

Since both controllers plan a path around opponents while maximizing the progress, fast and safe overtaking maneuvers are enabled. In the current work, we focus on static obstacles, which seems sufficient to outperform non-expert human drivers. To robustly overtake dynamically moving obstacles (other automatic controllers or expert drivers), it would be necessary to have a prediction of their behavior, which is currently not available. These predictions could however be systematically incorporated into the high-level corridor planner outlined in Section III-C, and would merely change the corridor issued to the controllers presented in Section III-A and Section III-B.

<!-- chunk {"id": "body-0091", "role": "body", "section": "IV-D Racing with multiple cars", "weight": 1.0} -->

An obstacle avoidance situation is shown in Figure 9, with a detailed zoom taken at three different time points in Figure 10. These zooms show the prediction horizon and the corresponding planned trajectories. Due to the limited path planner, the HRHC is not able to directly plan a path around all obstacles from the beginning. Thus it avoids the first three cars, without predicting how to overtake the next two cars. Only after the car has made enough progress and overtaken the first group of obstacles, can the controller find a way between of the other two cars. The MPCC on the other hand plans the path around all obstacles before it even reaches the first car due to its long horizon. This is an advantage, but if the model mismatch is significant it can lead to problems, as the planned path is too optimistic.

<!-- chunk {"id": "body-0092", "role": "body", "section": "IV-D Racing with multiple cars", "weight": 1.0} -->

HRHC controller (Section III-A) MPCC controller (Section III-B)

<!-- chunk {"id": "body-0093", "role": "body", "section": "IV-D Racing with multiple cars", "weight": 1.0} -->

HRHC controller (Section III-A) MPCC controller (Section III-B)

<!-- chunk {"id": "body-0094", "role": "body", "section": "IV-E Computation Times", "weight": 1.0} -->

The computation times of the most time-consuming components of the two controllers are given in Tables II and III for the laps depicted in Figure 8 (single car racing) and Figure 9 (avoidance of opponents). Note that the computation times of the individual blocks of the two controllers cannot be compared directly. To directly compare the computation times of the two controllers, the horizon length should be identical. However, due to the constant velocity limitation in the HRHC path planner, a horizon length identical to the MPCC is impossible without using multiple segments of constant velocity, which would make the path planning combinatorial in complexity and thus currently prohibitive for a real-time implementation. Vice versa, the MPCC cannot work robustly with the short horizon length used by the HRHC. The multiple car case does not have a significant impact on the execution times of the lower level controller; only the path planning in the HRHC gets slightly more complicated. However, the computation time of the high-level corridor planner (the DP approach from Section III-C) varies significantly, depending on the complexity of the racing situation. For the MPCC, the limiting factor with respect to the sampling time is the computation time for solving the QP.

<!-- chunk {"id": "body-0095", "role": "body", "section": "IV-E Computation Times", "weight": 1.0} -->

The main bottleneck in the HRHC is the path planner, which has a very high maximal computation time caused by back up rules in the case no feasible trajectory can be found. The QP on the other hand is the most expensive step in the average, but does not have a large variation in computation time, which makes it less critical.

<!-- chunk {"id": "body-0096", "role": "body", "section": "IV-E Computation Times", "weight": 1.0} -->

The $20$ ms sampling time was missed by the HRHC controller in only $0.07$ % (one sampling instant in three laps) and by the MPCC controller in $4.4$ % (60 sampling instants in three laps) of the time. Overall, our experiments demonstrate that both schemes can be implemented in (soft) real-time at sampling rates of $50$ Hz.
