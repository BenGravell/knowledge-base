<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Waypoint Kinodynamic Motion Planning for a Tractor with Two Trailers in an Orchard: Sampling-Based vs. Optimization- Based Approaches

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a novel sampling-based approach to waypoint-constrained kinodynamic planning for a custom apple-picking machine consisting of a tractor towing two trailers, operating autonomously in an orchard. The platform must follow sparse 2D waypoints through narrow headlands and rows. We adapt the Asymptotically Optimal A* (AOA*) planner to this setting and compare it against optimization-based methods (Fatrop and Ipopt) on representative benchmarks, a headland U-Turn, complex long path, and an environment with random obstacles. AOA* finds first feasible plans in seconds (often sub-second for U-turns), achieves 100% success at moderate temporal resolution, and reduces trajectory-time suboptimality to under 7% with a short anytime budget. Optimization-based planners (Fatrop and Ipopt) reach near-optimal trajectories when successful but typically require coarser time steps and longer runtime. At the same time, sampling-based algorithms support arbitrary obstacle geometries and are easier to set up. Overall, AOA* finds a feasible plan faster and scales better with the horizon and temporal resolution.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

At the same time, optimization-based solvers produce smoother, near-locally optimal trajectories when warm-started. The results of this work can enable a generalized approach for both intra-row maneuvers and inter-field logistics (e.g., orchard–warehouse transits) without changing environment representations.
