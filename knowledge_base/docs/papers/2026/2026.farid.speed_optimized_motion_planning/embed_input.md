<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Speed-Optimized Motion Planning for Robotic Object Handling via Constrained Linear Convex Optimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a framework for speed-optimized motion planning in robotic object handling, including dynamic throwing and pick-and-place with obstacle avoidance tasks. An S-curve-based optimization algorithm first computes optimal throwing configurations to ensure accurate object landing. A two-stage trajectory generation strategy is adopted: speed-optimized trajectory planning to compute time-efficient velocity profiles under physical constraints, and B-spline-based trajectory smoothing to produce smooth joint trajectories. Velocity, acceleration, torque, and jerk constraints are reformulated as convex problems, with cubic B-splines representing the squared pseudo-velocity and a convex relaxation addressing non-convex jerk limits. For obstacle-aware motions, a discrete LP framework parameterizes the path with cubic polynomials and enforces convex polyhedral constraints on the end-effector to maintain safety. The LP maximizes traversal speed while satisfying joint and dynamic limits. Simulation and real-world tests on a Franka Emika Panda robot with a qb SoftHand as a gripper show precise, fast object handling, including throwing and PnP operations.
