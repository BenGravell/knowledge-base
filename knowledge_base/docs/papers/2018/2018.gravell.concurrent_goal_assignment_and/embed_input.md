Concurrent Goal Assignment and Collision-Free Trajectory Generation for Multiple Aerial Robots

Topics include Goal assignment, Collision avoidance, Motion planning, Multi-robot planning, Centralized planning, Trajectory planning, Trajectory generation, UAVs, Aerial robots.

Presents heuristics for planning motions and goal assignments for large-scale fleets of cylinder-shaped flying robots. Uses several simplifying assumptions and design choices, such as constant-velocity straight-line trajectories, and the ability to instantaneously "teleport" between altitudes in a 2.5D spatial arrangement.

We develop computationally tractable methods for concurrent goal assignment and planning of collision-free trajectories for multiple aerial robot systems. Our method first assigns robots to goals to minimize total time-in-motion, assuming straight-line maximum-speed trajectories. By coupling the assignment and trajectory generation, the initial motion plans tend to require only limited collision resolution. We then refine the plans by checking for potential collisions and resolving them using either start time delays or altitude assignment. Numerical experiments using both methods show significant reductions in the total time required for agents to arrive at goals with only modest additional computational effort in comparison to state-of-the-art prior work.
