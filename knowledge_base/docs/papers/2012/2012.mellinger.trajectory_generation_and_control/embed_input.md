<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Trajectory Generation and Control for Precise Aggressive Maneuvers with Quadrotors

Topics include Quadrotor maneuvers, Trajectory generation, Learning control, Aggressive flight, Perching, Automated refinement, Experimental robotics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Builds a workflow for designing quadrotor trajectories and controllers for aggressive maneuvers, then iteratively refining controller parameters through repeated experiments. The contribution is the combination of dynamically feasible trajectory segments, model-based control, and automated learning from trials, enabling repeatable flights through narrow gaps and inverted-surface perching.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the problem of designing dynamically feasible trajectories and controllers that drive a quadrotor to a desired state in state space. We focus on the development of a family of trajectories defined as a sequence of segments, each with a controller parameterized by a goal state or region in state space. Each controller is developed from the dynamic model of the robot and then iteratively refined through successive experimental trials in an automated fashion to account for errors in the dynamic model and noise in the actuators and sensors. We show that this approach permits the development of trajectories and controllers enabling such aggressive maneuvers as flying through narrow, vertical gaps and perching on inverted surfaces with high precision and repeatability.
