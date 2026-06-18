<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Trajectory Generation for Car-Like Robots Using Cubic Curvature Polynomials

Topics include Path planning, Trajectory generation, Continuous curvature, Nonholonomic systems.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes a steering method for connecting boundary conditions in (x, y, yaw, curvature) state space with a curve having curvature which is a cubic polynomial of arc length, generalizing simple clothoids. The method for computing the curvature polynomial coefficients is based on an iterative procedure (essentially equivalent to Newton's method) with an informative heuristic initial guess and a residual based on the deviation from the target end state.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Curvature polynomials of cubic order are ideal primitive trajectories for car-like robots. Unlike the clothoids, which are linear curvature polynomials, cubic curves can be used to determine a unique trajectory to an arbitrary target posture using a single continuous primitive. Such curves are also the lowest order curves which are continuous in the torque applied to steering mechanisms, so they generate trajectories which are relatively easily tracked by a real vehicle. Like the clothoids, cubic curvature polynomials are relatively difficult to compute but are easy to execute. A real-time numerical method to compute them is described.
