<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SBP-Guided MPC to Overcome Local Minima in Trajectory Planning

Topics include Trajectory planning, Trajectory optimization, Model predictive control, iLQR, Rapidly-exploring random tree, Sampling-based planning, Local minima, Hybrid planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Uses an RRT solution trajectory to warm-start iLQR, preventing the optimizer from getting stuck in local minima and simultaneously refining the crude RRT path into a smoother, more optimal trajectory.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Trajectory planning is often a difficult task for highdimensional systems, especially those with non-linear dynamics. Two common methods for trajectory planning in non-linear systems are Model Predictive Control (MPC) and kinodynamic Sampling-Based Planning (SBP). In this paper, we focus on a variant of MPC called the iterative Linear Quadratic Gaussian (iLQG) algorithm. iLQG has been shown to be fast and effective for generating trajectories to reach a goal. However, when optimizing for non-linear dynamics, it runs the risk of falling into local minima. Unlike iLQG, SBP methods such as Rapidly-exploring Random Trees (RRT) can be robust to local minima because they explore by taking random actions instead of following a gradient. However, for similar reasons, SBP often produces inefficient trajectories. We combine these two algorithms to take advantage of the specific strengths of each. We show that by using an RRT-produced trajectory as a warm start for iLQG, we can overcome local minima while still producing an efficient trajectory.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

On a specific system model (a robot snake), we show that the combination of these two algorithms allows the robot to reach a goal faster than the use of either algorithm alone in most cases.
