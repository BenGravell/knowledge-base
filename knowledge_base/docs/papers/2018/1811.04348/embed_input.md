Model Predictive Trajectory Optimization and Tracking for On-Road Autonomous Vehicles

Topics include Autonomous driving, Model predictive control, Trajectory optimization, Trajectory tracking.

Combines trajectory optimization with a feedback-feedforward tracking controller for on-road autonomous vehicles. The main contribution is the coupling of model-predictive feedforward planning with a stability-oriented tracking design for dynamic-obstacle scenarios.

Motion planning for autonomous vehicles requires spatio-temporal motion plans (i.e. state trajectories) to account for dynamic obstacles. This requires a trajectory tracking control process which faithfully tracks planned trajectories. In this paper, a control scheme is presented which first optimizes a planned trajectory and then tracks the optimized trajectory using a feedback-feedforward controller. The feedforward element is calculated in a model predictive manner with a cost function focusing on driving performance. Stability of the error dynamic is then guaranteed by the design of the feedback-feedforward controller. The tracking performance of the control system is tested in a realistic simulated scenario where the control system must track an evasive lateral maneuver. The proposed controller performs well in simulation and can be easily adapted to different dynamic vehicle models. The uniqueness of the solution to the control synthesis eliminates any nondeterminism that could arise with switching between numerical solvers for the underlying mathematical program.

## INTRODUCTION

Autonomous vehicles often decompose the selection of steering, throttle, and braking control signals into a planning process which generates a feasible motion through the perceived scene. This is followed by a control process which executes a local trajectory tracking control policy robust to process noise and load disturbances. Motion planning algorithms for autonomous driving usually simplify the planning task by first planning a geometric path followed by planning a longitudinal velocity profile along the geometric path....

The downside to this decomposition is that it implicitly discards effective options available to the planner. For example, if a dynamic obstacle suddenly crosses the vehicle's path, a geometric planner will not reason about the motion of that object and will have to assume a fixed location, or neglect the dynamic obstacle completely; the subsequent longitudinal planner must find a safe option restricted to the selected geometric path. This motivates spatio-temporal motion planning that accounts for predicted states of dynamic obstacles....

## CONCLUSIONS

This paper proposes a trajectory tracking control approach for autonomous vehicles based on a model predictive trajectory optimization to generate a feedforward control and a time varying linear quadratic regulator for feedback. Optimization of a reference trajectory is formulated as a strictly convex quadratic program by leveraging a linearization about the reference trajectory, polyhedral constraints, and a family of strictly convex quadratic cost functions. Additionally, the quadratic cost function is developed taking into account the rate of change of the feedforward input....

The dynamics of the LTV system over an $N$-step planning horizon is written compactly as

### II-C Convexity of Quadratic Functions

Justification of this observation can be found in Appendix A.

To address such issue, one approach attracting increasing attention is Model Predictive Control (MPC) which incorporates a sophisticated dynamic model to recursively optimize tracking errors over the reference trajectory. MPC approaches for trajectory tracking have been widely investigated for both autonomous driving and semi-autonomous driving cases. Furthermore, if the cost function can be proved as a Lyapunov function, stability of the nominal closed-loop system is guaranteed....
