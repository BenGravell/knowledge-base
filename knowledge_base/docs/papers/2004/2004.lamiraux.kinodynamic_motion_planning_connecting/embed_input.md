<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Kinodynamic Motion Planning: Connecting Exploration Trees Using Trajectory Optimization Methods

Topics include Kinodynamic planning, Motion planning, Exploration trees, Trajectory optimization, Dynamic systems, Goal connection, Sampling-based planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Combines input-space exploration trees with local trajectory optimization to connect kinodynamic plans exactly to the goal. The method addresses a key weakness of pure exploration-tree planners: they can approach the goal neighborhood but may not satisfy the terminal state precisely without many samples.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Motion planning for complex dynamic systems as well as kinodynamic motion planning are still problems difficult to solve in their generic formulation. For systems for which no steering method is known, the only existing algorithms consist in building an exploration tree in the configuration space by exploring the input space of the system. The main drawback of this type of methods is that they never reach exactly the goal but stops the search when a small neighborhood of the goal has been reached. If the neighborhood is small, the exploration method needs to produce a lot of nodes. In this paper, we propose a solution to cope with this complexity issue. We run a tree exploration method with a big neighborhood and then we locally modify the trajectory in order to make it reach exactly the goal. Our solution is based on a trajectory optimization method we have developed earlier in a mobile robot context and that we have adapted for the problem raised here. The method is generic and can be applied to any dynamic system. A few experimental results are given at the end of the paper.
