<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Bounding on Rough Terrain with the LittleDog Robot

Topics include Motion planning, Kinodynamic planning, Sampling-based planning, RRTs, Legged locomotion, Quadruped robots, Rough terrain, Motion primitives, Feedback stabilization, Transverse linearization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Develops a practical kinodynamic planner for highly dynamic LittleDog bounding by combining motion primitives, reachability-guided sampling, and task-space Voronoi bias inside an RRT-style search. The paper is useful because it pairs the planner with transverse-linearization feedback, separating the problem of finding dynamic rough-terrain motions from the problem of stabilizing inherently unstable open-loop bounds on hardware.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A motion planning algorithm is described for bounding over rough terrain with the LittleDog robot. Unlike walking gaits, bounding is highly dynamic and cannot be planned with quasi-steady approximations. LittleDog is modeled as a planar five-link system, with a 16-dimensional state space; computing a plan over rough terrain in this high-dimensional state space that respects the kinodynamic constraints due to underactuation and motor limits is extremely challenging. Rapidly Exploring Random Trees (RRTs) are known for fast kinematic path planning in high-dimensional configuration spaces in the presence of obstacles, but search efficiency degrades rapidly with the addition of challenging dynamics. A computationally tractable planner for bounding was developed by modifying the RRT algorithm by using: motion primitives to reduce the dimensionality of the problem; Reachability Guidance, which dynamically changes the sampling distribution and distance metric to address differential constraints and discontinuous motion primitive dynamics; and sampling with a Voronoi bias in a lower-dimensional “task space” for bounding. Short trajectories were demonstrated to work on the robot, however open-loop bounding is inherently unstable.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A feedback controller based on transverse linearization was implemented, and shown in simulation to stabilize perturbations in the presence of noise and time delays.
