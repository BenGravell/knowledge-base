<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Minimum Jerk Trajectory Generation for Differential Wheeled Mobile Robots

Topics include Trajectory generation, Minimum jerk, Differential drive, Mobile robots, Smooth trajectory.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes a minimum jerk trajectory generation method for differential wheeled mobile robots, based on solving a finite-dimensional unconstrained nonlinear optimization problem.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper we present a trajectory generation scheme for approximate way point tracking for a nonholonomic differential wheeled mobile robot. The generated trajectories are guaranteed to satisfy the nonholonomic dynamics and minimizes the jerk of the center of mass motion of the robot. Minimizing jerk is desirable to ensure the smoothness of the trajectories and is often necessary to ensure physical hardware limitations of the electromagnetic actuators, prevent undesirable induced vibrations, and ensure comfort of the passengers. The problem is naturally formulated in the setting of a constrained optimal control problem. The paper presents a way of reducing the computationally intensive infinite dimensional optimal control solution to that of a finite dimensional nonlinear programming problem that can be easily solved using any of the existing fast numerical algorithms and thus making the scheme realtime implementable.
