Multi-Query Shortest-Path Problem in Graphs of Convex Sets

Topics include Semidefinite programming, Motion planning, Robotics, Graphs, Online algorithms, Offline algorithms, Optimization, Planning, Shortest path problem.

The Shortest-Path Problem in Graph of Convex Sets (SPP in GCS) is a recently developed optimization framework that blends discrete and continuous decision making. Many relevant problems in robotics, such as collision-free motion planning, can be cast and solved as an SPP in GCS, yielding lower-cost solutions and faster runtimes than state-of-the-art algorithms. In this paper, we are motivated by motion planning of robot arms that must operate swiftly in static environments. We consider a multi-query extension of the SPP in GCS, where the goal is to efficiently precompute optimal paths between given sets of initial and target conditions. Our solution consists of two stages. Offline, we use semidefinite programming to compute a coarse lower bound on the problem's cost-to-go function. Then, online, this lower bound is used to incrementally generate feasible paths by solving short-horizon convex programs. For a robot arm with seven joints, our method designs higher quality trajectories up to two orders of magnitude faster than existing motion planners.

## Introduction

A Graph of Convex Sets (GCS) is a graph where each vertex is paired with a convex set and an optimization variable inside this set, while each edge couples adjacent vertex variables through additional convex costs and constraints. In the Shortest-Path Problem (SPP) in GCS, we simultaneously seek a discrete path through this graph and optimize the continuous variables associated with the vertices along the path, while minimizing the cumulative edge costs.

Though the SPP in GCS is NP-hard \[, Section 9.2\], effective solution methods have been proposed . This technique has shown remarkable success in various robotics applications, such as optimal control, planning through contact, and other robotics problems. In real-world hardware deployment, it has been especially effective in collision-free motion planning, addressing the challenges of non-convex obstacle avoidance constraints.

(b) Online: at each iteration, we evaluate all n-step paths from the current vertex (n = 1 shown) and greedily select the decision that minimizes the n-step lookahead cost-to-go. The first three iterations are shown, as the path is built incrementally.

## Conclusion and future work

In this work, we generalized the classical All-Pairs Shortest-Paths problem to the Graphs of Convex Sets, and developed practical approximate numerical methods for solving this problem. We demonstrated that a coarse lower bound on the cost-to-go with a greedy multi-step lookahead policy produce near-optimal paths, while significantly reducing solve times. Our methodology effectively scales to high-dimensional set scenarios and large graph instances, enabling practical robotics applications in multi-query settings. We plan to provide an efficient implementation of our approach within the Drake library.

For hardware applications in non-static environments, we are interested in ways to tackle changes to the robot's configuration space, like those arising in object manipulation, as well as addition and removal of obstacles. Assuming the changes are minor, the online search via the multi-step lookahead policy provides natural local adaptation. Changes to the environment can be incorporated into the online policy rollout program via non-convex constraints, similar to.
