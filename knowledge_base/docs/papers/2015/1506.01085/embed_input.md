A Convex Optimization Approach to Smooth Trajectories for Motion Planning with Car-Like Robots

Topics include Smooth trajectory, Car-like, Optimization, Heuristic, Optimal, Real-time, Smoothing, Path planning, Convex optimization, Self driving, Bicycle model, Bubble, Ground vehicles, Collision-free, Vehicle dynamics, Speed profile.

CES takes a reference trajectory as input, then re-plans both the path shape and speed profile within a sequence of obstacle-free "bubble" regions along the trajectory using convex programming. This makes it a powerful post-processor, reportedly outperforming traditional path shortcutting heuristics as well as elastic band approaches.

In the recent past, several sampling-based algorithms have been proposed to compute trajectories that are collision-free and dynamically-feasible. However, the outputs of such algorithms are notoriously jagged. In this paper, by focusing on robots with car-like dynamics, we present a fast and simple heuristic algorithm, named Convex Elastic Smoothing (CES) algorithm, for trajectory smoothing and speed optimization. The CES algorithm is inspired by earlier work on elastic band planning and iteratively performs shape and speed optimization. The key feature of the algorithm is that both optimization problems can be solved via convex programming, making CES particularly fast. A range of numerical experiments show that the CES algorithm returns high-quality solutions in a matter of a few hundreds of milliseconds and hence appears amenable to a real-time implementation.

## Introduction

The problem of planning a collision-free and dynamically-feasible trajectory is fundamental in robotics, with application to systems as diverse as ground, aerial, and space vehicles, surgical robots, and robotic manipulators. A common strategy is to decompose the problem in steps of computing a collision-free, but possibly highly-suboptimal or not even dynamically-feasible trajectory, smoothing it, and finally reparameterizing the trajectory so that the robot can execute it.

The first step is often accomplished by running a sampling-based motion planning algorithm, such as PRM or RRT. While these algorithms are very effective for quickly finding collision-free trajectories in obstacle-cluttered environments, they often return jerky, unnatural paths. Furthermore, sampling-based algorithms can only handle rather simplified dynamic models, due to the complexity of exploring the state space while retaining dynamic feasibility of the trajectories.

Accordingly, the objective of this paper is to design a fast and simple *heuristic* algorithm for trajectory smoothing and reparametrization that is amenable to a real-time implementation, with a focus on mobile robots, in particular robotic cars. Specifically, we seek an algorithm that within a few hundreds of milliseconds can turn a jerky trajectory returned by a sampling-based motion planner into a smooth, speed-optimized trajectory that fulfills strict dynamical constraints such as friction, bounded acceleration, or turning radius limitations.

## I-A Literature Review

The problem of smoothing a trajectory returned by a sampling-based planner is not new and has been studied since the introduction of sampling-based algorithms. For planning problems that do not involve the fulfillment of dynamic constraints (e.g., limited turning radius), efficient smoothing algorithms are already available. In this case, the most widely applied method is the Shortcut heuristic, because of its effectiveness and simple implementation. In a typical implementation, this algorithm considers two random configurations along the trajectory.
