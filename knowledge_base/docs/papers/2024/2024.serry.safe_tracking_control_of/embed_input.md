<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Safe Tracking Control of Discrete-Time Nonlinear Systems Using Backward Reachable Sets

Topics include Safety control, Safety guarantees, Reachable sets, Discrete-time systems, Nonlinear systems, Reachability analysis, Control synthesis.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Designs a tracking controller for discrete-time nonlinear systems by computing backward reachable sets that certify when reference tracking remains safe. The contribution is a synthesis workflow that connects reachability guarantees with a practical tracking-control objective.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Tracking controllers are often integrated into control systems to ensure robustness against uncertainties and disturbances during trajectory following maneuvers, where the design methods in the literature lack formal guarantees, can be applied only to limited classes of systems, and/or suffer from conservatism. In this paper, we propose a new tracking control approach for discrete-time nonlinear uncertain systems using set-based computations. In particular, we compute zonotopic backward reachable sets along prescribed nominal trajectories, and utilize such sets to synthesize tracking controllers that ensure safety and reachability in the presence of input/state constraints and disturbances. We illustrate our approach through two numerical examples (Dubin's car and planar quadrotor).
