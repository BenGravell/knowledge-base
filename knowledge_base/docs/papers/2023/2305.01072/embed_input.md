Fast Path Planning through Large Collections of Safe Boxes

Topics include Motion planning, Convex optimization, Path planning, Trajectory optimization, Free-space decomposition, Graph search, Graphs of convex sets.

Presents a fast two-phase path planner for environments where the free space is pre-decomposed into a large collection of axis-aligned safe boxes. An offline phase constructs a graph over box intersections. At runtime, a graph shortest-path search finds a polygonal waypoint sequence, then a convex optimal-control problem smooths it into a continuous Bézier trajectory guaranteed collision-free at all times. The decomposition into a cheap graph search followed by small convex programs gives near-real-time performance even with tens of thousands of boxes.

We present a fast algorithm for the design of smooth paths (or trajectories) that are constrained to lie in a collection of axis-aligned boxes. We consider the case where the number of these safe boxes is large, and basic preprocessing of them (such as finding their intersections) can be done offline. At runtime we quickly generate a smooth path between given initial and terminal positions. Our algorithm designs trajectories that are guaranteed to be safe at all times, and detects infeasibility whenever such a trajectory does not exist. Our algorithm is based on two subproblems that we can solve very efficiently: finding a shortest path in a weighted graph, and solving (multiple) convex optimal-control problems. We demonstrate the proposed path planner on large-scale numerical examples, and we provide an efficient open-source software implementation, fastpathplanning.

## Introduction

Path planning is a problem at the core of almost any autonomous system. Driverless cars, drones, autonomous aircraft, robot manipulators, and legged robots are just a few examples of systems that rely on a path-planning algorithm to navigate in their environment. Path-planning problems can be challenging on many fronts. The environment can be dynamic, i.e., change over time, or uncertain because of noisy sensor measurements. Computation might be subject to strict real-time requirements. Interactions between multiple robots without central coordination can lead to game-theoretic problems....

Figure 1: Path planning for a quadrotor flying through a simulated village. Top. The village, composed of buildings, trees, and bushes. The free space is decomposed using more than ten thousand safe boxes. Bottom. A snapshot of the quadrotor flight. The smooth path connects two opposite corners of the village and is guaranteed to be collision free at all times. The online planning time is only a few seconds.

### Multiple waypoints

In some path-planning problems we need to design a single smooth path that interpolates or passes through a given sequence of intermediate waypoints in order. To extend our approach to these problems, the steps in the polygonal phase are repeated to connect each pair of consecutive waypoints, yielding a single polygonal curve that satisfies all the interpolation constraints. Similarly, in the smooth phase, we concatenate multiple problems of the form into a single program, where each piecewise Bézier curve has fixed endpoints and is constrained to connect smoothly with its neighbors....

are the second group of variables in our control problem.

### Improvement of the box sequence

The resulting problem is an SOCP that approximates the nonconvex program locally, and tries to improve the current solution by taking a step in the tangent space of the nonlinear equation. Like the projection problem, it can be solved in a time that increases only linearly with $N$. From its solution we only retain the optimal traversal times $T_{1}^{\star},\ldots,T_{N}^{\star}$, and then we solve a new projection problem to obtain a new feasible path. If the optimal objective value decreases, compared to the previous projection problem, we accept the new times and update our path. Otherwise we keep the previous times and path.
