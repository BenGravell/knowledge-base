<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

PROXDDP: Proximal Constrained Trajectory Optimization

Topics include Trajectory optimization, Differential dynamic programming, Constrained optimization, Proximal methods, ProxDDP.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces ProxDDP, using proximal point iterations within a DDP framework to overcome convergence issues often encountered in Augmented Lagrangian DDP methods (e.g., ALTRO), with provable convergence guarantees for constrained trajectory optimization.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Trajectory optimization has been a popular choice for motion generation and control in robotics for at least a decade. Several numerical approaches have exhibited the required speed to enable online computation of trajectories for real-time of various systems, including complex robots. Many of these said are based on the differential dynamic programming (DDP) algorithm—initially designed for unconstrained trajectory optimization problems—and its variants, which are relatively easy to implement and provide good runtime performance. However, several problems in robot control call for using constrained formulations (e.g., torque limits, obstacle avoidance), from which several difficulties arise when trying to adapt DDP-type methods: numerical stability, computational efficiency, and constraint satisfaction. In this article, we leverage proximal methods for constrained optimization and introduce a DDP-type method for fast, constrained trajectory optimization suited for model-predictive control (MPC) applications with easy warm-starting. Compared to earlier solvers, our approach effectively manages hard constraints without warm-start limitations and exhibits good convergence behavior. We provide a complete implementation as part of an open-source and flexible C++ trajectory optimization library called aligator.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

These algorithmic contributions are validated through several trajectory planning scenarios from the robotics literature and the real-time whole-body MPC of a quadruped robot.
