Admissible Velocity Propagation: Beyond Quasi-Static Path Planning for High-Dimensional Robots

Topics include Kinodynamic planning, Path-velocity decomposition, Quasi-static planning, Velocity propagation, Dynamic motions.

Starting point is quasi-static (velocity ~= 0) path planning. Then augments state space with velocity and uses propagation of velocity using kinodynamics to determine the reachable set (admissible interval) of velocity, and includes that in the connection check for new nodes. Builds on the foundational TOPP velocity planner. AVP is modularly (re)usable in many sampling-based planners; the authors give a concrete instantiation and numerical experiments with AVP-RRT.

Path-velocity decomposition is an intuitive yet powerful approach to address the complexity of kinodynamic motion planning. The difficult trajectory planning problem is solved in two separate, simpler, steps: first, find a path in the configuration space that satisfies the geometric constraints (path planning), and second, find a time-parameterization of that path satisfying the kinodynamic constraints. A fundamental requirement is that the path found in the first step should be time-parameterizable. Most existing works fulfill this requirement by enforcing quasi-static constraints in the path planning step, resulting in an important loss in completeness. We propose a method that enables path-velocity decomposition to discover truly dynamic motions, i.e. motions that are not quasi-statically executable. At the heart of the proposed method is a new algorithm — Admissible Velocity Propagation — which, given a path and an interval of reachable velocities at the beginning of that path, computes the interval of all reachable and time-parameterizable velocities at the end of that path.

## Introduction

Planning motions for robots with many degrees of freedom and subject to kinodynamic constraints (i.e. constraints that involve higher-order time-derivatives of the robot configuration ) is one of the most important and challenging problems in robotics. Path-velocity decomposition is an intuitive yet powerful approach to address the complexity of kinodynamic motion planning: first, find a *path* in the configuration space that satisfies the geometric constraints, such as obstacle avoidance, joint limits, kinematic closure, etc....

### Advantages of path-velocity decomposition

### Future works

As just mentioned, we have recently extended TOPP to redundantly-actuated systems, including humanoid robots in multi-contact tasks. This enables AVP-based planners to be applied to multi-contact planning for humanoid robots. In this application, the existence of kinematic closure constraints (the parts of the robot in contact with the environment should remain fixed) makes path-velocity decomposition highly appealing since these constraints can be handled by a kinematic planner independently from dynamic constraints (torque limits, balance, etc.) In a preliminary experiment, we have planned a non-quasi-statically-feasible but...

If "sliding" along the ${MVC}_{D}$ does not violate the actuation bounds (1 ‣ 2 Propagating admissible velocities along a path ‣ Admissible Velocity Propagation: Beyond Quasi-Static Path Planning for High-Dimensional Robots")), then slide as far as possible along the $MVC$. The "slide" terminates either (a) when the maximum acceleration vector $\beta$ points downward from the ${MVC}_{D}$: in this case follow that vector out of ${MVC}_{D}$ or (b) when the minimum acceleration vector $\alpha$ points upward from the ${MVC}_{D}$: in this case, proceed as in 2;

Under the nomenclature introduced in Definition 1 ‣ 2 Propagating admissible velocities along a path ‣ Admissible Velocity Propagation: Beyond Quasi-Static Path Planning for High-Dimensional Robots"), we say that a velocity ${\overset{˙}{s}}_{end}$ is a *valid* final velocity if there exists a valid profile that starts at $(0,{\overset{˙}{s}}_{0})$ for some ${\overset{˙}{s}}_{0} \in {\lbrack{\overset{˙}{s}}_{beg}^{\min},{\overset{˙}{s}}_{beg}^{\max}\rbrack}$ and ends at $(s_{end},{\overset{˙}{s}}_{end})$.
