<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Reachability-guided Sampling for Planning under Differential Constraints

Topics include Kinodynamic planning, Reachability, Sampling-based planning, Differential constraints, Robot planning, Rapidly-exploring random tree.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Guides sampling-based planning using reachability information so expansion choices better respect differential constraints. The method improves over naive random sampling in kinodynamic systems where many sampled states are hard or impossible to reach from the existing tree.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Rapidly-exploring random trees (RRTs) are widely used to solve large planning problems where the scope prohibits the feasibility of deterministic solvers, but the efficiency of these algorithms can be severely compromised in the presence of certain kinodynamics constraints. Obstacle fields with tunnels, or tubes are notoriously difficult, as are systems with differential constraints, because the tree grows inefficiently at the boundaries. Here we present a new sampling strategy for the RRT algorithm, based on an estimated feasibility set, which affords a dramatic improvement in performance in these severely constrained systems. We demonstrate the algorithm with a detailed look at the expansion of an RRT in a swing up task, and on path planning for a nonholonomic car.
