A Nonlinear Model Predictive Control Framework Using Reference Generic Terminal Ingredients - Extended Version

In this paper, we present a quasi infinite horizon nonlinear model predictive control (MPC) scheme for tracking of generic reference trajectories. This scheme is applicable to nonlinear systems, which are locally incrementally stabilizable. For such systems, we provide a reference generic offline procedure to compute an incrementally stabilizing feedback with a continuously parameterized quadratic quasi infinite horizon terminal cost. As a result we get a nonlinear reference tracking MPC scheme with a valid terminal cost for general reachable reference trajectories without increasing the online computational complexity. As a corollary, the terminal cost can also be used to design nonlinear MPC schemes that reliably operate under online changing conditions, including unreachable reference signals. The practicality of this approach is demonstrated with a benchmark example. This paper is an extended version of the accepted paper, and contains additional details regarding \textit{robust} trajectory tracking (App.~B), continuous-time dynamics (App.~C), output tracking stage costs (App.~D) and the connection to incremental system properties (App.~A).

## Introduction

Model Predictive Control (MPC) is a well established control method, that computes the control input by repeatedly solving an optimization problem online. The main advantages of MPC are the ability to cope with general nonlinear dynamics, hard state and input constraints, and the inclusion of performance criteria. In MPC (theory), recursive feasibility and closed-loop stability of a desirable setpoint are usually ensured by including suitable terminal ingredients (terminal set and terminal cost) in the optimization problem.

In many applications, the control goal goes beyond the stabilization of a pre-determined setpoint. These practical challenges include tracking of changing reference setpoints, stabilization of dynamic trajectories, output regulation and general economic optimal operation. There exist many promising ideas to tackle these issues in MPC, for example by simultaneously optimizing an artificial reference. However, most of these approaches are limited in some form to linear systems and/or setpoint stabilization.

## Contribution

In this work, we provide a reference generic offline procedure to compute a parameterized terminal cost. This procedure is applicable to both setpoint or trajectory stabilization. The feasibility of this approach requires local incremental stabilizability of the nonlinear dynamics. The existing design procedures use the linearization around the considered setpoint or trajectory to locally establish properties of the nonlinear systems.

## Conclusion

We have presented a procedure to compute terminal ingredients for nonlinear reference tracking MPC schemes offline. The main novelty in this approach is that the offline computation only needs to be done once, irrespective of the setpoint or trajectory to be stabilized. This is possible by computing parameterized terminal ingredients and approximating the nonlinear system locally as a quasi-LPV system, with the reference trajectory to be stabilized as the parameter.

The extension of the proposed procedure to large scale nonlinear distributed systems using a seperable formulation is part of future work.
