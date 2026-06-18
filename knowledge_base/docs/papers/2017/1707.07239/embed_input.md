A New Approach to Time-Optimal Path Parameterization Based on Reachability Analysis

Topics include Time-optimal, Speed planning, Reachability.

Reframes TOPP as a reachability problem, propagating feasible velocity sets via small LPs, so you get the speed of numerical integration and the robustness of convex optimization in one easy-to-implement algorithm. Claims to (at least partially) generalize AVP (1411.4045).

Time-optimal path parameterization (TOPP) is a well-studied problem in robotics and has a wide range of applications. There are two main families of methods to address TOPP: numerical integration (NI) and convex optimization (CO). The NI-based methods are fast but difficult to implement and suffer from robustness issues, while CO-based approaches are more robust but, at the same time, significantly slower. Here, we propose a new approach to TOPP based on reachability analysis. The key insight is to recursively compute reachable and controllable sets at discretized positions on the path by solving small linear programs. The resulting algorithm is faster than NI-based methods and as robust as CO-based ones (100% success rate), as confirmed by extensive numerical evaluations. Moreover, the proposed approach offers unique additional benefits: admissible velocity propagation and robustness to parametric uncertainty can be derived from it in a simple and natural way.

## Introduction

Time-Optimal Path Parameterization (TOPP) is the problem of finding the fastest way to traverse a path in the configuration space of a robot system while respecting the system constraints. This classical problem has a wide range of applications in robotics. In many industrial processes (cutting, welding, machining, 3D printing, etc.) or mobile robotics applications (driverless cars, warehouse UGVs, aircraft taxiing, etc.), the robot paths may be predefined, and optimal productivity implies tracking those paths at the highest possible speed while respecting the process and robot constraints....

### Existing approaches to TOPP

A recognized disadvantage of the classical TOPP formulation is that the time-optimal trajectory contains hard acceleration switches, corresponding to infinite jerks. Solving TOPP subject to jerk bounds, however, is not possible using the CO-based approach as the problem becomes non-convex. Some prior works proposed to either extend the NI-based approach or to represent the parameterization as a spline and optimize directly over the parameter space. Exploring how Reachability Analysis can be extended to handle jerk bounds is another direction of our future research.

Similar to the CO-based approach, Reachability Analysis can only be applied to instances with convex constraints. Yet in practice, it is often desirable to consider in addition non-convex constraints, such as joint torque bounds with viscous friction effect. Extending Reachability Analysis to handle non-convex constraints is another important research question.

We show the following result: as the discretization step size goes to zero, the cost, i.e. traversal time, of the parameterization returned by TOPP-RA converges to the optimal value.

### Implementation remark 4

Fig. 3 shows the computation time for TOPP-RA and TOPP-NI, excluding the "setup" and "extract trajectory" steps (which takes much longer in TOPP-NI than in TOPP-RA). The experimental results confirm our theoretical analysis in that the complexity of TOPP-RA is in linear in $m$ while that of TOPP-NI is quadratic in $m$. In terms of actual computation time, TOPP-RA becomes faster than TOPP-NI as soon as $m \geq 22$. Table I reports the different components of the computation time.
