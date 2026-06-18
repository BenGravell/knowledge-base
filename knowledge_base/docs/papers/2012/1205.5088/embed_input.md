Kinodynamic RRT*: Optimal Motion Planning for Systems with Linear Differential Constraints

Topics include Kinodynamic planning, Rapidly-exploring random tree star, Linear systems, Optimal control, Double integrator.

Uses a fixed-final-state-free-final-time controller that exactly and optimally connects any pair of states in RRT*, where cost trades off trajectory duration against control effort. Dynamics are restricted to linear (or linearized) systems.

We present Kinodynamic RRT*, an incremental sampling-based approach for asymptotically optimal motion planning for robots with linear differential constraints. Our approach extends RRT*, which was introduced for holonomic robots, by using a fixed-final-state-free-final-time controller that exactly and optimally connects any pair of states, where the cost function is expressed as a trade-off between the duration of a trajectory and the expended control effort. Our approach generalizes earlier work on extending RRT* to kinodynamic systems, as it guarantees asymptotic optimality for any system with controllable linear dynamics, in state spaces of any dimension. Our approach can be applied to non-linear dynamics as well by using their first-order Taylor approximations. In addition, we show that for the rich subclass of systems with a nilpotent dynamics matrix, closed-form solutions for optimal trajectories can be derived, which keeps the computational overhead of our algorithm compared to traditional RRT* at a minimum.

## Introduction

Much progress has been made in the area of motion planning in robotics over the past decades, where the basic problem is defined as finding a trajectory for a robot between a start state and a goal state without collisions with obstacles in the environment. The introduction of incremental sampling-based planners, such as probabilistic roadmaps (PRM) and rapidly-exploring random trees (RRT) enabled solving motion planning problems in high-dimensional state spaces in reasonable computation time, even though the problem is known to be PSPACE-hard.

In this paper, we present Kinodynamic RRT\*, an extension of RRT\* that overcomes the above limitations by introducing into the algorithm a fixed-final-state-free-final-time controller that exactly and optimally connects any pair of states for any system with controllable linear dynamics in state spaces of arbitrary dimension. Our approach finds asymptotically optimal trajectories in environments with obstacles and bounds on the state and control input, with respect to a cost function that is expressed as a tunable trade-off between the duration of the trajectory and the expended control effort.

We note that while we focus our presentation on extending RRT\* to kinodynamic systems, also the application of PRM and path *smoothing* by iterative shortcutting have thus far been limited to holonomic systems, for these methods too require connecting pairs of states by feasible trajectories. Our approach is equally suited for making PRM and smoothing applicable to robots with differential constraints, and may particularly align well with recent interest in constructing roadmaps containing near-optimal trajectories.

## Discussion, Conclusion, and Future Work

We have presented Kinodynamic RRT\*, an incremental sampling-based approach that extends RRT\* for asymptotically optimal motion planning for robots with differential constraints. Our approach achieves asymptotically optimality by using a fixed-final-state-free-final-time optimal control formulation that connects any pair of states exactly and optimally for systems with controllable linear dynamics.
