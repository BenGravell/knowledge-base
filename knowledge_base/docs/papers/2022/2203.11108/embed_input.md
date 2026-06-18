db-A*: Discontinuity-bounded Search for Kinodynamic Mobile Robot Motion Planning

Topics include Trajectory optimization, Motion planning, Robotics, Graphs, Benchmarks, Sampling-based methods, Generalization, Optimization, Planning, Sampling, Mobile robots.

We consider time-optimal motion planning for dynamical systems that are translation-invariant, a property that holds for many mobile robots, such as differential-drives, cars, airplanes, and multirotors. Our key insight is that we can extend graph-search algorithms to the continuous case when used symbiotically with optimization. For the graph search, we introduce discontinuity-bounded A* (db-A*), a generalization of the A* algorithm that uses concepts and data structures from sampling-based planners. Db-A* reuses short trajectories, so-called motion primitives, as edges and allows a maximum user-specified discontinuity at the vertices. These trajectories are locally repaired with trajectory optimization, which also provides new improved motion primitives. Our novel kinodynamic motion planner, kMP-db-A*, has almost surely asymptotic optimal behavior and computes near-optimal solutions quickly. For our empirical validation, we provide the first benchmark that compares search-, sampling-, and optimization-based time-optimal motion planning on multiple dynamical systems in different settings....

## Introduction

Motion planning for robots with known kinodynamics remains challenging, especially when a time-optimal motion is desired. Consider the example in Fig. 1 of a simple dynamical model in 2D (unicycle, 3-dimensional state space and 2-dimensional control space). Finding the time-optimal solution is surprisingly challenging for state-of-the-art methods when constraining the control space to model a plane with a malfunctioning rudder, i.e., with a positive minimum speed and asymmetric angular velocity limits.

Current planning approaches are sampling-based, search-based, optimization-based, or hybrid. Each of these methods has their strengths and weaknesses. Sampling-based planners can find initial solutions quickly and have strong guarantees for convergence to an optimal solution. However, in practice the initial solutions are far from the optimum, the convergence rate is low, and the solutions typically require some post-processing. Search-based approaches can remedy those shortcomings by connecting precomputed trajectories, so-called *motion primitives*, using A\* or related graph search algorithms....

We present a new kinodynamic motion planning technique, kMP-db-A\*, that uses a novel graph-search method with trajectory optimization in an iterative fashion. For the graph search, we introduce db-A\*, a generalization of A\* that reuses motion primitives to compute trajectories with a bounded discontinuity. Then, we warm-start trajectory optimization using the output of the graph search and compute new motion primitives online....

The major limitation of kMP-db-A\* is that it sometimes requires a long time to compute an initial solution. We believe that this is not a fundamental issue and that it can be improved using the following techniques in the future. First, we are interested in using stronger heuristics and bounded suboptimal and incremental graph search techniques to reuse information between iterations. Second, we plan to investigate the use of optimizers that do not operate over the full trajectory time horizon. Finally, we believe that our work also lays the foundation for novel kinodynamic multi-robot motion planners.

Db-A\* is incomplete and suboptimal if $\delta > 0$.

### IV-A db-A\*: Discontinuity-bounded A\*
