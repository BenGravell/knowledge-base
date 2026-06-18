RAKOMO: Reachability-Aware K-Order Markov Path Optimization for Quadrupedal Loco-Manipulation

Topics include Trajectory optimization, Motion planning, Robotics, Safety, Benchmarks, Optimization, Planning, RAKOMO, KOMO.

Legged manipulators, such as quadrupeds equipped with robotic arms, require motion planning techniques that account for their complex kinematic constraints in order to perform manipulation tasks both safely and effectively. However, trajectory optimization methods often face challenges due to the hybrid dynamics introduced by contact discontinuities, and tend to neglect leg limitations during planning for computational reasons. In this work, we propose RAKOMO, a path optimization technique that integrates the strengths of K-Order Markov Optimization (KOMO) with a kinematically-aware criterion based on the reachable region defined as reachability margin. We leverage a neural-network to predict the margin and optimize it by incorporating it in the standard KOMO formulation. This approach enables rapid convergence of gradient-based motion planning - commonly tailored for continuous systems - while adapting it effectively to legged manipulators, successfully executing loco-manipulation tasks. We benchmark RAKOMO against a baseline KOMO approach through a set of simulations for pick-and-place tasks with the HyQReal quadruped robot equipped with a Kinova Gen3 robotic arm.

## INTRODUCTION

Mobile manipulators are increasingly used in everyday activities due to their ability to perform tasks in industrial, domestic, and natural environments. Successful operations in the real world require the robot to reach and manipulate objects while avoiding collisions with both their own structure and the surrounding environment. The enhanced mobility provided by legs has motivated the robotics community to explore legged systems as mobile bases for manipulators....

In the literature, two powerful techniques for robot motion planning have been proposed: sampling-based and optimization-based planning, the latter often referred to as trajectory optimization (TO). Sampling-based methods, such as Rapidly Exploring Random Trees (RRT) and Probabilistic Roadmaps (PRM) \[\], can theoretically converge to an optimal solution if one exists, but tend to suffer from a slow convergence time. By contrast, optimization-based planning generally yields smoother trajectories that are compatible with real-time requirements....

## Conclusions

In this work, we presented a novel methodology for motion planning in legged manipulators that integrates a reachability margin within the K-Order Markov Optimization (KOMO) framework. By leveraging supervised learning to model the reachability margin (i.e. the shortest distance from the base's horizontal projection to the boundary of the leg's reachable region), we incorporated leg kinematic limitations directly into the motion planning process without explicitly modeling all the leg joints....

The final trajectory should be smooth and penalize overall joint displacement from the starting robot joint configuration. Hence, we introduce here two type of costs:

To incorporate the reachability margin in a gradient-based optimization problem, we need to be able to compute its gradient w.r.t. its inputs. Given the non-differentiable nature of the iterative algorithm used to obtain the region, this can only be achievable through the finite-difference of the numerical computation. This is considerably inefficient as the computation of one region can take, on average, 30 to 40 ms (with the gradient computation requiring over 1 sec). Instead, we proceed to approximate the reachability margin through training an MLP network.
