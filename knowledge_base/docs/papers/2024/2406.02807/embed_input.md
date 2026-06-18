Collision-Affording Point Trees: SIMD-Amenable Nearest Neighbors for Fast Collision Checking

Topics include Motion planning, Robotics, Nearest neighbors, Real-time systems, Sampling-based methods, Planning, Control, Sampling, Collision-affording point tree, CAPT, Single-instruction multiple-data.

Motion planning against sensor data is often a critical bottleneck in real-time robot control. For sampling-based motion planners, which are effective for high-dimensional systems such as manipulators, the most time-intensive component is collision checking. We present a novel spatial data structure, the collision-affording point tree (CAPT): an exact representation of point clouds that accelerates collision-checking queries between robots and point clouds by an order of magnitude, with an average query time of less than 10 nanoseconds on 3D scenes comprising thousands of points. With the CAPT, sampling-based planners can generate valid, high-quality paths in under a millisecond, with total end-to-end computation time faster than 60 FPS, on a single thread of a consumer-grade CPU. We also present a point cloud filtering algorithm, based on space-filling curves, which reduces the number of points in a point cloud while preserving structure. Our approach enables robots to plan at real-time speeds in sensed environments, opening up potential uses of planning for high-dimensional systems in dynamic, changing, and unmodeled environments.

## Introduction

Motion planning underpins many applications of high-degree-of-freedom robots, allowing them to efficiently find collision-free trajectories between arbitrary poses. Modern motion planning methods capably solve problems with many obstacles for these high-dimensional robots, typically by either building and searching a graph or tree approximating the collision-free subset of the robot's state space (*i.e.*, sampling-based motion planning (sbmp) \[orthey2023sampling, LaValle2001, Kavraki1996\]) or by solving a numerical optimization problem (*i.e.*, trajectory optimization \[Schulman2014, Zucker2013, bhardwaj_storm_integrated_2021\]).

In this work, we propose a data structure and associated construction and search algorithms for *exact* point cloud distance computation and collision checking. Our proposed data structure, the *collision-affording point tree* (capt), adapts and refines concepts from the classical $k$-d tree to support efficient parallel evaluation.

the collision-affording point tree (capt), a novel data structure for storing sensed point clouds for collision checking.

## Conclusion

Planning from sensor data is a crucial component of autonomous robotics. In this paper, we present a novel data structure for motion planning with observed point clouds, demonstrating an order-of-magnitude speedup compared to state-of-the-art techniques. We also present a unique filtering algorithm to reduce the density of a point cloud while still providing safety guarantees on collision detection. Combined, these two contributions enable a robot to plan from sensor data in milliseconds on a single CPU core, allowing the robot to plan faster than standard 60FPS camera refresh rates.

The primary limitation of a capt is that it is an immutable data structure. After construction, no points in the tree can be inserted or deleted. Since depth-camera images are streamed on a frame-by-frame basis, this is not a problem for collision-checking in dynamic environments, since we can reconstruct the capt from scratch for each frame. However, the capt's immutability precludes use of a capt for the state-space nearest-neighbor search required by most sampling-based planning algorithms.
