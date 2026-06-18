Quintic G2-Splines for Trajectory Planning of Autonomous Vehicles

Topics include Path planning, Motion planning, Splines, G2 continuity, Autonomous vehicles, Nonholonomic systems, Flatness-based control, Differential flatness, Curvature continuity.

Proposes a steering method for connecting pairs of states in [x, y, yaw, curvature] state space using paths that are quintic polynomials in x, y position coordinates. This leaves four free tuning parameters eta1, eta2, eta3, eta4, which influence the shape of the paths and can be set according to heuristics or can be explicitly optimized, which is investigated in the companion work by the same authors "Optimal trajectory planning with quintic G2-splines".

Presents a motion planning primitive for car-like vehicles. It is a completely parametrized quintic spline, denoted as eta-spline, that allows interpolation of an arbitrary sequence of points with overall second order geometric G2-continuity. Issues such as minimality, regularity, symmetry, and flexibility of these G2-splines are addressed in the exposition. The development of the new primitive is tightly connected to the flatness based control of nonholonomic car-like vehicles.
