<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Quadratic Regulator-based Heuristic for Rapidly Exploring State Space

Topics include Kinodynamic planning, Rapidly-exploring random tree, Linear quadratic regulator heuristics, State space search, Robot planning, Differential constraints.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces AQR-RRT, using local quadratic-regulator approximations to define a dynamics-aware distance heuristic for tree expansion. The method targets the mismatch between Euclidean distance and actual reachability in kinodynamic planning.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Kinodynamic planning algorithms like Rapidly-Exploring Randomized Trees (RRTs) hold the promise of finding feasible trajectories for rich dynamical systems with complex, nonconvex constraints. In practice, these algorithms perform very well on configuration space planning, but struggle to grow efficiently in systems with dynamics or differential constraints. This is due in part to the fact that the conventional distance metric, Euclidean distance, does not take into account system dynamics and constraints when identifying which node in the existing tree is capable of producing children closest to a given point in state space. We show that an affine quadratic regulator (AQR) design can be used to approximate the exact minimum-time distance pseudometric at a reasonable computational cost. We demonstrate improved exploration of the state spaces of the double integrator and simple pendulum when using this pseudometric within the RRT framework, but this improvement drops off as systems' nonlinearity and complexity increase. Future work includes exploring methods for approximating the exact minimum-time distance pseudometric that can reason about dynamics with higher-order terms.
