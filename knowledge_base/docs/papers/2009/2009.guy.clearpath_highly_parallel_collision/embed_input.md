<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

ClearPath: Highly Parallel Collision Avoidance for Multi-agent Simulation

Topics include Collision avoidance, Multi-agent simulation, Parallel algorithms, Crowd simulation, Velocity obstacles, Real-time planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces ClearPath, a highly parallel collision-avoidance method for large multi-agent simulations. By formulating avoidance as simple local optimization that maps well to parallel hardware, it enables real-time simulation of dense crowds.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a new local collision avoidance algorithm between multiple agents for real-time simulations. Our approach extends the notion of velocity obstacles from robotics and formulates the conditions for collision free navigation as a quadratic optimization problem. We use a discrete optimization method to efficiently compute the motion of each agent. This resulting algorithm can be parallelized by exploiting data-parallelism and thread-level parallelism. The overall approach, ClearPath, is general and can robustly handle dense scenarios with tens or hundreds of thousands of heterogeneous agents in a few milli-seconds. As compared to prior collision avoidance algorithms, we observe more than an order of magnitude performance improvement.
