<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Quartic Bézier Curve Based Trajectory Generation for Autonomous Vehicles with Curvature and Velocity Constraints

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

To generate local trajectory between initial states and target states for autonomous vehicles, a feasible trajectory generation algorithm based on quartic Bézier curve is proposed. The problem of trajectory generation is firstly separated into generating continuous and bounded curvature profile to shape the trajectory and generating linear velocity profile to execute the trajectory. The curvature profile generation is further converted to an optimization problem with only 3 parameters owing to the specific properties of quartic Bézier curve. Sequential quadratic programming is employed to find optimal solution with respect to specific objective function. To avoid sideslip and ensure velocity-continuity and acceleration limits, the framework of linear velocity profile generation is also proposed. A simple profile with constant acceleration is also provided as an example. Simulation results on lane keeping and changing and path following demonstrate the capability and the real-time performance of the proposed algorithm.
