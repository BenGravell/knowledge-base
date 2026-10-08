<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Improved Path Planning by Tightly Combining Lattice-Based Path Planning and Optimal Control

Topics include Lattice planning, Optimal control, Bilevel optimization, Motion planning, Trajectory optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Formulates lattice planning as bilevel optimization and uses a dynamically consistent lattice solution to initialize numerical optimal control. The combination resolves discrete route choices before continuous refinement, improving reliability, cost, and computation time.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a unified optimization-based path planning approach to efficiently compute locally optimal solutions to advanced path planning problems. The approach is motivated by first showing that a lattice-based path planner can be cast and analyzed as a bilevel optimization problem. This information is then used to tightly integrate a lattice-based path planner and numerical optimal control in a novel way. The lattice-based path planner is applied to the problem in a first step using a discretized search space, where system dynamics and objective function are chosen to coincide with those used in a second numerical optimal control step. As a consequence, the lattice planner provides the numerical optimal control step with a resolution optimal solution to the problem, which is highly suitable as a warm-start to the second step. This novel tight combination of a sampling-based path planner and numerical optimal control makes, in a structured way, benefit of the former method's ability to solve combinatorial parts of the problem and the latter method's ability to obtain locally optimal solutions not constrained to a discretized search space.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Compared to previously presented combinations of sampling-based path planners and optimization, the proposed approach is shown in several path planning experiments to provide significant improvements in terms of computation time, numerical reliability, and objective function value.
