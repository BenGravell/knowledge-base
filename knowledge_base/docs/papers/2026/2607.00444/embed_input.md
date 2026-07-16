<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Spatiotemporal motion planning, especially in multi-robot settings, requires robots to reason about collision-free regions that change over time, which is challenging in continuous spaces when feasible regions are transient and geometrically constrained. We present an algorithmic framework based on graphs of space-time convex sets (ST-GCSs), where collision-free regions are represented as convex sets in space-time and trajectories correspond to paths on the graph together with continuous motions within the selected sets. We formulate time-optimal planning on ST-GCSs as a graph-search problem over path-indexed states and develop a best-first search solver that evaluates partial paths via continuous trajectory optimization, guided by admissible heuristics and dominance checks. We further present an Exact Convex Decomposition (ECD) scheme to reserve trajectory occupancies in space-time, enabling unified handling of dynamic obstacles and multi-robot interactions. For multi-robot motion planning, we integrate ST-GCS planning and ECD into prioritized planning methods and introduce a windowed coordination scheme to improve efficiency.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Extensive experiments on single-robot and multi-robot problems demonstrate substantial speedups over various planners while maintaining high solution quality, particularly in environments with narrow and transient feasible regions. Large-scale demonstrations further show that the proposed multi-robot motion planner can solve instances with up to 100 robots within only a few minutes.
