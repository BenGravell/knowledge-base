<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Simple and Efficient Algorithms for Computing Smooth, Collision-free Feedback Laws over Given Cell Decompositions

Topics include Feedback planning, Cell decompositions, Collision avoidance, Navigation functions, Motion planning, Smooth control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Constructs smooth collision-free feedback laws over given cell decompositions, turning discrete decompositions into continuous controllers. The work is useful where a planner must provide not just a path but a stabilizing vector field over regions of free space.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a novel approach to computing feedback laws in the presence of obstacles. Instead of computing a trajectory between a pair of initial and goal states, our algorithms compute a vector field over the entire state space; all trajectories obtained from following this vector field are guaranteed to asymptotically reach the goal state. As a result, the vector field globally solves the navigation problem and provides robustness to disturbances in sensing and control. The vector field's integral curves (system trajectories) are guaranteed to avoid obstacles and are C ∞ smooth. We construct a vector field with these properties by partitioning the space into simple cells, defining local vector fields for each cell, and smoothly interpolating between them to obtain a global vector field. We present an algorithm that computes these feedback controls for a kinematic point robot in an arbitrary dimensional space with piecewise linear boundary; the algorithm requires minimal preprocessing of the environment and is extremely fast during execution. For many practical applications in two-dimensional environments, full computation can be done in milliseconds. We also present an algorithm for computing feedback laws over cylindrical algebraic decompositions, thereby solving a smooth feedback version of the generalized piano movers' problem.
