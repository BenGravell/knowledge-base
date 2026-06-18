A Biconvex Method for Minimum-Time Motion Planning through Sequences of Convex Sets

Topics include Motion planning, Trajectory optimization, Convex optimization, Minimum-time planning, Graphs of convex sets, Bezier curves.

Addresses minimum-time trajectory design through a fixed sequence of convex sets subject to velocity and acceleration constraints - a problem that is natively nonconvex due to the coupling between time scaling and path shape. The proposed biconvex method alternates between two convex subproblems, quickly generating a feasible initial trajectory and iteratively refining it without line-search parameters.

We consider the problem of designing a smooth trajectory that traverses a sequence of convex sets in minimum time, while satisfying given velocity and acceleration constraints. This problem is naturally formulated as a nonconvex program. To solve it, we propose a biconvex method that quickly produces an initial trajectory and iteratively refines it by solving two convex subproblems in alternation. This method is guaranteed to converge, returns a feasible trajectory even if stopped early, and does not require the selection of any line-search or trust-region parameter. Exhaustive experiments show that our method finds high-quality trajectories in a fraction of the time of state-of-the-art solvers for nonconvex optimization. In addition, it achieves runtimes comparable to industry-standard waypoint-based motion planners, while consistently designing lower-duration trajectories than existing optimization-based planners.

## Introduction

Selecting the most effective motion-planning algorithm for a robotic system often requires balancing three competing objectives: reliability, computational efficiency, and trajectory quality. Consider Sparrow, the robot arm in Fig. that sorts individual products into bins before they get packaged in the Amazon warehouses. The algorithms that move Sparrow must be extremely reliable, as these robots handle millions of diverse products every day, and each failure requires expensive interventions.

This paper focuses on a problem similar to the one in the second phase of: we seek a trajectory that traverses a sequence of convex sets in minimum time, and satisfies convex velocity and acceleration constraints. This is a purely continuous problem, but is nonconvex due to the joint optimization of the trajectory shape and timing. Our contribution is a biconvex method, which we call Sequence of Convex Sets (SCS), that solves this problem effectively. SCS starts by quickly producing a feasible trajectory. Then, it alternates between two convex subproblems.

As most multi-convex methods, SCS is heuristic: it typically finds high-quality trajectories quickly, but might not converge to the problem optimum, or within a given distance of it. On the other hand, SCS is complete (i.e., guaranteed to find a feasible solution). Its main algorithmic advantage is that the two convex subproblems are conservative approximations of the original nonconvex problem. This allows us to take whole steps in the direction their optima without using a line search or a trust region, as done and other trajectory-optimization methods.

## Limitations

Our method has a few worth-noting limitations. First of all, SCS is restricted to minimum-time problems. However, a similar approach can be applied to problems with fixed final time and cost function that penalizes the magnitude of the trajectory velocity and acceleration.

SCS requires that the robot free space is described as a sequence of convex sets. This description can be challenging to compute for high-dimensional problems and cluttered environments. However, as mentioned in §I, many practical methods for decomposing complex spaces into convex sets are now available, and also GPU-based algorithms have been recently developed.
