Admissible Velocity Propagation: Beyond Quasi-Static Path Planning for High-Dimensional Robots

Topics include Kinodynamic planning, Path-velocity decomposition, Quasi-static planning, Velocity propagation, Dynamic motions.

Starting point is quasi-static (velocity ~= 0) path planning. Then augments state space with velocity and uses propagation of velocity using kinodynamics to determine the reachable set (admissible interval) of velocity, and includes that in the connection check for new nodes. Builds on the foundational TOPP velocity planner. AVP is modularly (re)usable in many sampling-based planners; the authors give a concrete instantiation and numerical experiments with AVP-RRT.

Path-velocity decomposition is an intuitive yet powerful approach to address the complexity of kinodynamic motion planning. The difficult trajectory planning problem is solved in two separate, simpler, steps: first, find a path in the configuration space that satisfies the geometric constraints (path planning), and second, find a time-parameterization of that path satisfying the kinodynamic constraints. A fundamental requirement is that the path found in the first step should be time-parameterizable. Most existing works fulfill this requirement by enforcing quasi-static constraints in the path planning step, resulting in an important loss in completeness. We propose a method that enables path-velocity decomposition to discover truly dynamic motions, i.e. motions that are not quasi-statically executable. At the heart of the proposed method is a new algorithm — Admissible Velocity Propagation — which, given a path and an interval of reachable velocities at the beginning of that path, computes the interval of all reachable and time-parameterizable velocities at the end of that path.

## Introduction

Planning motions for robots with many degrees of freedom and subject to kinodynamic constraints (i.e. constraints that involve higher-order time-derivatives of the robot configuration ) is one of the most important and challenging problems in robotics. Path-velocity decomposition is an intuitive yet powerful approach to address the complexity of kinodynamic motion planning: first, find a *path* in the configuration space that satisfies the geometric constraints, such as obstacle avoidance, joint limits, kinematic closure, etc.

## Advantages of path-velocity decomposition

This approach was suggested as early as 1986 -- only a few years after the birth of motion planning itself as a research field -- by Kant and Zucker, in the context of motion planning amongst movable obstacles. Since then, it has become an important tool to address many kinodynamic planning problems, from manipulators subject to torque limits, to coordination of teams of mobile robots, to legged robots subject to balance constraints, etc.

Path-velocity decomposition is appealing in that it *exploits the natural decomposition* of the constraints, in most systems, into two categories: those depending uniquely on the robot configuration, and those depending in particular on the velocity, which in turn is related to the energy of the system. Consider for instance a humanoid robot in a multi-contact task. Such a robot must avoid collision with the environment, avoid self-collisions, respect kinematic closure for the parts in contact with the environment (e.g. the stance foot must be fixed with respect to the ground), maintain balance.

## Discussion

We have presented a new algorithm, Admissible Velocity Propagation (AVP) which, given a path and an interval of reachable velocities at the beginning of that path, computes exactly and efficiently the interval of valid final velocities. We have shown how to combine AVP with well-known sampling-based geometric planners to give rise to a family of new efficient kinodynamic planners, which we have evaluated on two difficult kinodynamic problems.
