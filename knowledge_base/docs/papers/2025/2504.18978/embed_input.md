A Biconvex Method for Minimum-Time Motion Planning through Sequences of Convex Sets

Topics include Motion planning, Trajectory optimization, Convex optimization, Minimum-time planning, Graphs of convex sets, Bezier curves.

Addresses minimum-time trajectory design through a fixed sequence of convex sets subject to velocity and acceleration constraints - a problem that is natively nonconvex due to the coupling between time scaling and path shape. The proposed biconvex method alternates between two convex subproblems, quickly generating a feasible initial trajectory and iteratively refining it without line-search parameters.

We consider the problem of designing a smooth trajectory that traverses a sequence of convex sets in minimum time, while satisfying given velocity and acceleration constraints. This problem is naturally formulated as a nonconvex program. To solve it, we propose a biconvex method that quickly produces an initial trajectory and iteratively refines it by solving two convex subproblems in alternation. This method is guaranteed to converge, returns a feasible trajectory even if stopped early, and does not require the selection of any line-search or trust-region parameter. Exhaustive experiments show that our method finds high-quality trajectories in a fraction of the time of state-of-the-art solvers for nonconvex optimization. In addition, it achieves runtimes comparable to industry-standard waypoint-based motion planners, while consistently designing lower-duration trajectories than existing optimization-based planners.

## Introduction

Selecting the most effective motion-planning algorithm for a robotic system often requires balancing three competing objectives: reliability, computational efficiency, and trajectory quality. Consider Sparrow, the robot arm in Fig. that sorts individual products into bins before they get packaged in the Amazon warehouses. The algorithms that move Sparrow must be extremely reliable, as these robots handle millions of diverse products every day, and each failure requires expensive interventions....

Sampling-based methods like PRM \[\], RRT \[\], and their asymptotically optimal versions \[\] can be fast enough for real-time applications. They are highly parallelizable \[\] and can run on a GPU. They are also reliable in low-dimensional spaces, where dense sampling is computationally feasible. However, they become significantly less effective as the space dimension grows. Additionally, although their kinodynamic variants support differential constraints, sampling-based methods remain considerably less practical for designing smooth continuous trajectories than producing polygonal paths.

The three methods use the same constraints and trajectory parameterization. The first two share also the same initialization strategy and termination tolerance. Tab. I shows the statistics for the task-completion time and the runtime of each motion planner. SCS generates the best trajectories: in fact, the average completion time for the overall package-transfer task is about $10$ s for SCS, $13$ s for the trust-region method, and $15$ s for the waypoint-based planner. In other words, SCS allows us to transfer $28\%$ and $50\%$ more packages per unit of time than the trust-region and the waypoint-based planners, respectively....

We conclude by emphasizing that the trust-region and the waypoint-based planners are natural baselines for the task considered in this section. The first provides the same completeness guarantees as SCS, designs smooth trajectories, and has relatively low runtimes. The second is widespread in warehouse automation thanks to its good performance and high reliability....

The shape of our polygonal trajectory is computed through the following convex program:

### IV-B Nonconvex formulation

### VIII-A Convergence and completeness
