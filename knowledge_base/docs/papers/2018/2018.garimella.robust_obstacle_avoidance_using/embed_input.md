<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robust Obstacle Avoidance Using Tube NMPC

Topics include Tube model predictive control, Nonlinear model predictive control, Robust obstacle avoidance, Disturbance invariant sets, Bi-level optimization, Nonlinear dynamics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Alternates nominal-trajectory optimization with finite-dimensional approximations of disturbance-invariant tubes for nonlinear systems. The resulting NMPC avoids obstacles under disturbances in ground and aerial vehicle simulations, with approximate rather than exact invariance guarantees.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This work considers the problem of avoiding obstacles for general nonlinear systems subject to disturbances. Obstacle avoidance is achieved by computing disturbance invariant sets along a nominal trajectory and ensuring these invariant sets do not intersect with obstacles. We develop a novel technique to compute approximate disturbance invariant sets for general nonlinear systems using a set of finite dimensional optimizations. A bi-level NMPC optimization strategy alternates between optimizing over the nominal trajectory and finding the disturbance invariant sets. Simulation results show that the proposed algorithm is able to generate disturbance invariant sets for standard 3D aerial and planar ground vehicles models, and the NMPC algorithm successfully computes obstacle avoidance trajectories using the disturbance invariant sets.
