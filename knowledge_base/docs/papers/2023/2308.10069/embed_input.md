Real-time Mixed-Integer Quadratic Programming for Vehicle Decision Making and Motion Planning

Topics include Integer programming, Motion planning, Vehicles, Real-time systems, Planning, Sampling, MIP-DM, Mixed-integer quadratic program, MIQP, Quadratic programming.

We develop a real-time feasible mixed-integer programming-based decision making (MIP-DM) system for automated driving. Using a linear vehicle model in a road-aligned coordinate frame, the lane change constraints, collision avoidance and traffic rules can be formulated as mixed-integer inequalities, resulting in a mixed-integer quadratic program (MIQP). The proposed MIP-DM simultaneously performs maneuver selection and trajectory generation by solving the MIQP at each sampling time instant. While solving MIQPs in real time has been considered intractable in the past, we show that our recently developed solver BB-ASIPM is capable of solving MIP-DM problems on embedded hardware in real time. The performance of this approach is illustrated in simulations in various scenarios including merging points and traffic intersections, and hardware-in-the-loop simulations on dSPACE Scalexio and MicroAutoBox-III. Finally, we present results from hardware experiments on small-scale automated vehicles.

## Introduction

Automated transportation systems, even in the case of partial automation, may lead to reduced road accidents and more efficient usage of the road network. However, the complexity of automated driving (AD) and advanced driver-assistance systems (ADAS) and their real-time requirements in resource-limited automotive platforms requires the implementation of a multi-layer guidance and control architecture....

A typical guidance and control architecture is illustrated in Figure 1(a), e.g., similar to. Based on a route given by a navigation system, a decision making module decides when to perform maneuvers such as lane changing, stopping, waiting, and intersection crossing. Given these decisions, a motion planning system generates a state trajectory to execute the maneuvers, and a vehicle control system computes the input signals to track the trajectory.

We designed a mixed-integer programming-based decision making for automated driving. The mixed-integer quadratic programming formulation uses a linear vehicle model in a road-aligned coordinate frame, it includes lane selection and lane change timing constraints, polyhedral collision avoidance and intersection crossing constraints, and zone-dependent traffic rule changes....

Future works will focus on using more advanced behavior prediction models for other vehicles and explicit handling of uncertainty in the modeling and perception of the environment, as well as deployment on full scale vehicles.

The sixth term in minimizes a tracking error of the current lane with respect to a given preferred lane value ${\overline{p}}_{n}^{ref}{(i)}$, e.g., the right lane in right-hand traffic or the left most lane when a vehicle desires to make a left turn at a next traffic intersection. To handle the absolute value in, we minimize an auxiliary control variable $\Deltap_{n}^{ref}$, satisfying

### Remark 7

## Numerical Simulation Results

Optimization-based motion planning and control techniques, such as model predictive control (MPC), directly account for dynamics, constraints and objectives in a model-based design framework. This has been extended to hybrid systems, including both discrete and continuous decision variables....
