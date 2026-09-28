<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Structure of the Time-Optimal Path Parameterization Problem with Third-Order Constraints

Topics include Time-optimal, Speed planning, Path parameterization, Jerk constraints, Numerical integration, Multiple shooting, Singularities.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces TOPP3 for time-optimal traversal of a fixed path under third-order constraints, combining multiple shooting to connect extremal jerk profiles with a method for passing through singularities that otherwise halt integration. The analysis focuses on pure third-order constraints and identifies remaining challenges in handling more general switching structures and combined velocity, acceleration, and jerk limits.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finding the Time-Optimal Parameterization of a Path (TOPP) subject to second-order constraints (e.g. acceleration, torque, contact stability, etc.) is an important and well-studied problem in robotics. In comparison, TOPP subject to third-order constraints (e.g. jerk, torque rate, etc.) has received far less attention and remains largely open. In this paper, we investigate the structure of the TOPP problem with third-order constraints. In particular, we identify two major difficulties: (i) how to smoothly connect optimal profiles, and (ii) how to address singularities, which stop profile integration prematurely. We propose a new algorithm, TOPP3, which addresses these two difficulties and thereby constitutes an important milestone towards an efficient computational solution to TOPP with third-order constraints.
