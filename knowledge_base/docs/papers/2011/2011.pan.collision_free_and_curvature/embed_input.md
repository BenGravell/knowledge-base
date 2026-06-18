<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Collision-Free and Curvature-Continuous Path Smoothing in Cluttered Environments

Topics include Path smoothing, Motion planning, B-splines, Collision checking, Curvature continuity, Trajectory constraints, Robotics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Turns jagged collision-free paths from sampling-based planners into curvature-continuous B-spline trajectories. The method locally refines splines to handle narrow passages, checks robot-environment collisions along curved paths efficiently, and enforces velocity and acceleration constraints, making post-processing more suitable for real robots.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a novel trajectory computation algorithm to smoothen jerky collision-free paths computed by samplebased motion planners. Our approach uses cubic B-splines to generate G2 or curvature continuous trajectories. The algorithm performs local spline refinement to compute collision-free trajectories in narrow passages and satisfies velocity and acceleration constraints. We also present a fast and reliable algorithm for collision checking between robot and the environment along the B-spline trajectories. We highlight the performance of our algorithm on complex benchmarks, including path computation for rigid and articulated models in tight spaces and narrow passages.
