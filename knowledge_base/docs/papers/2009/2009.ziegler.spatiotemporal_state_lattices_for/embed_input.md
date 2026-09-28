<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Spatiotemporal State Lattices for Fast Trajectory Planning in Dynamic on-road Driving Scenarios

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a method for motion planning in the presence of moving obstacles that is aimed at dynamic on-road driving scenarios. Planning is performed within a geometric graph that is established by sampling deterministically from a manifold that is obtained by combining configuration space and time. We show that these graphs are acyclic and shortest path algorithms with linear runtime can be employed. By reparametrising the configuration space to match the course of the road, it can be sampled very economically with few vertices, and this reduces absolute runtime further. The trajectories generated are quintic splines. They are second order continuous, obey nonholonomic constraints and are optimised for minimum square of jerk. Planning time remains below 20 ms on general purpose hardware.
