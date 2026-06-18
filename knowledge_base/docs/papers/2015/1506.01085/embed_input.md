A Convex Optimization Approach to Smooth Trajectories for Motion Planning with Car-Like Robots

Topics include Smooth trajectory, Car-like, Optimization, Heuristic, Optimal, Real-time, Smoothing, Path planning, Convex optimization, Self driving, Bicycle model, Bubble, Ground vehicles, Collision-free, Vehicle dynamics, Speed profile.

CES takes a reference trajectory as input, then re-plans both the path shape and speed profile within a sequence of obstacle-free "bubble" regions along the trajectory using convex programming. This makes it a powerful post-processor, reportedly outperforming traditional path shortcutting heuristics as well as elastic band approaches.

In the recent past, several sampling-based algorithms have been proposed to compute trajectories that are collision-free and dynamically-feasible. However, the outputs of such algorithms are notoriously jagged. In this paper, by focusing on robots with car-like dynamics, we present a fast and simple heuristic algorithm, named Convex Elastic Smoothing (CES) algorithm, for trajectory smoothing and speed optimization. The CES algorithm is inspired by earlier work on elastic band planning and iteratively performs shape and speed optimization. The key feature of the algorithm is that both optimization problems can be solved via convex programming, making CES particularly fast. A range of numerical experiments show that the CES algorithm returns high-quality solutions in a matter of a few hundreds of milliseconds and hence appears amenable to a real-time implementation.

## Introduction

The problem of planning a collision-free and dynamically-feasible trajectory is fundamental in robotics, with application to systems as diverse as ground, aerial, and space vehicles, surgical robots, and robotic manipulators. A common strategy is to decompose the problem in steps of computing a collision-free, but possibly highly-suboptimal or not even dynamically-feasible trajectory, smoothing it, and finally reparameterizing the trajectory so that the robot can execute it....

The first step is often accomplished by running a sampling-based motion planning algorithm, such as PRM or RRT. While these algorithms are very effective for quickly finding collision-free trajectories in obstacle-cluttered environments, they often return jerky, unnatural paths. Furthermore, sampling-based algorithms can only handle rather simplified dynamic models, due to the complexity of exploring the state space while retaining dynamic feasibility of the trajectories....

In this paper we presented a novel algorithm, Convex Elastic Smoothing, for trajectory smoothing which alternates between shape and speed optimization. We showed that both optimization problems can be solved via convex programming, which makes CES particularly fast and amenable to a real-time implementation.

This paper leaves numerous important extensions open for further research. First, it is of interest to extend the CES algorithm to other dynamic systems, such as aerial vehicles or spacecraft. Second, we plan to investigate more thoroughly the robustness of the algorithm when the reference trajectory is not collision-free or dynamically-feasible and the "typical" factor of suboptimality for a number of representative scenarios. Third, for shape optimization, this paper considered smoothness as the objective function....

Accordingly, the balancing force at point $Q_{k}$, $k = {1,\ldots,n}$ is

### III-A Bubble Generation

where the $Q_{k}^{\lbrack{i - 1}\rbrack}$'s are the waypoints computed at iteration $i - 1$. According to our discussion in Section III-B ‣ III The CES Algorithm ‣ A Convex Optimization Approach to Smooth Trajectories for Motion Planning with Car-Like Robots"), at iteration $i = 1$ one should set $Q_{k}^{\lbrack 0\rbrack} = P_{k}$, for $k = {1,\ldots,n}$.
