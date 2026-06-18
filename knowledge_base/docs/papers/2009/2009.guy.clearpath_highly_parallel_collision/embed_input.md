ClearPath: Highly Parallel Collision Avoidance for Multi-agent Simulation

Topics include Collision avoidance, Multi-agent simulation, Parallel algorithms, Crowd simulation, Velocity obstacles, Real-time planning.

Introduces ClearPath, a highly parallel collision-avoidance method for large multi-agent simulations. By formulating avoidance as simple local optimization that maps well to parallel hardware, it enables real-time simulation of dense crowds.

We present a new local collision avoidance algorithm between multiple agents for real-time simulations. Our approach extends the notion of velocity obstacles from robotics and formulates the conditions for collision free navigation as a quadratic optimization problem. We use a discrete optimization method to efficiently compute the motion of each agent. This resulting algorithm can be parallelized by exploiting data-parallelism and thread-level parallelism. The overall approach, ClearPath, is general and can robustly handle dense scenarios with tens or hundreds of thousands of heterogeneous agents in a few milli-seconds. As compared to prior collision avoidance algorithms, we observe more than an order of magnitude performance improvement.
