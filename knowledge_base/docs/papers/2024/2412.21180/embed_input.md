<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

STITCHER: Real-Time Trajectory Planning with Motion Primitive Search

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Autonomous high-speed navigation through large, complex environments requires real-time generation of agile trajectories that are dynamically feasible, collision-free, and satisfy constraints. Most modern trajectory planning techniques rely on numerical optimization because high-quality, expressive trajectories that satisfy constraints can be systematically computed. However, strict requirements on computation time and the risk of numerical instability can limit the use of optimization-based planners in safety-critical situations. This work presents an optimization-free planning framework called STITCHER that leverages graph search to generate long-range trajectories by stitching short trajectory segments together in real time. STITCHER is shown to outperform modern optimization-based planners through its innovative planning architecture and several algorithmic developments that make real-time planning possible. Simulation results show safe trajectories through complex environments can be generated in milliseconds that cover tens of meters.
