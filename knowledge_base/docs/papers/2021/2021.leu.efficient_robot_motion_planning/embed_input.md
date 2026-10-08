<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Efficient Robot Motion Planning via Sampling and Optimization

Topics include Robot motion planning, Sampling-based planning, Trajectory optimization, Sequential convex optimization, Convex feasible sets, Narrow passages, Motion planning benchmarks.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

RRT*-CFS combines RRT* initialization with convex feasible set trajectory optimization to improve the robustness and cost of robot motion planning. The paper supplies feasibility and convergence analysis and benchmarks the hybrid planner against sampling and optimization methods, including difficult narrow-passage scenarios.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Robot motion planning is one of the important elements in robotics. In environments full of obstacles, it is always challenging to find a collision-free and dynamically-feasible path between the robot's initial configuration and goal configuration. While many motion planning algorithms have been proposed in the past, each of them has its pros and cons. This work presents a benchmark which implements and compares existing planning algorithms on a variety of problems with extensive simulation. Based on that, we also propose a hybrid planning algorithm, RRT*-CFS, that combines the merits of sampling-based planning methods and optimization-based planning methods. The first layer, RRT*, quickly samples a semi-optimal path. The second layer, CFS, performs sequential convex optimization given the reference path from RRT*. The proposed RRT*-CFS has feasibility and convergence guarantees. Simulation results show that RRT*-CFS benefits from the hybrid structure and performs robustly in various scenarios including the narrow passage problems.
