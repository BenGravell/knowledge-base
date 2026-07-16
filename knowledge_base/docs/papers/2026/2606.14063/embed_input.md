<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Semidefinite Relaxations for Collision-Free Motion Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study semidefinite relaxations for collision-free motion planning. We focus on a point robot moving from start to goal through spherical obstacles in R^(n), subject to path continuity constraints and squared derivative costs; a setting that is conceptually simple yet captures the hardness of collision-free motion planning. We formulate this problem exactly as a nonconvex problem over polynomial curves, and present a natural semidefinite relaxation. We contribute two key theoretical insights; to our knowledge this is the first theoretical analysis of semidefinite relaxations for collision-free motion planning. First, we show that solving the convex relaxation is equivalent to solving, to global optimality, a related motion planning problem in a potentially higher-dimensional space. This geometric interpretation yields necessary and sufficient conditions for tightness, and a clear intuition for when the relaxation is loose. Second, we show that the relaxation admits a symmetry reduction that makes it significantly smaller than one might expect, with positive semidefinite cone sizes that scale linearly with the polynomial degree and are independent of the ambient dimension.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The resulting relaxation is 10 to 100 times faster than direct nonlinear programming transcriptions solved with SNOPT and IPOPT, exhibits significantly lower variance in solve times, and reliably finds a locally optimal path for the original problem. We demonstrate its effectiveness as a convex steering function in an RRT planner for minimum-snap quadrotor planning with C^ continuous trajectories.
