<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Fast Iterative Alignment of Pose Graphs with Poor Initial Estimates

Topics include Simultaneous localization and mapping, Pose graph optimization, Stochastic gradient descent, Non-linear optimization, Robot trajectory estimation, Loop closure, Graph-based simultaneous localization and mapping, Mobile robotics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces a fast pose-graph SLAM solver using stochastic gradient descent on a relative-pose state-space representation, achieving robust convergence even from severely degraded odometric initial estimates. The approach is computationally efficient and scales to large environments, and became a foundational reference for graph-based SLAM optimization.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A robot exploring an environment can estimate its own motion and the relative positions of features in the environment. Simultaneous localization and mapping (SLAM) algorithms attempt to fuse these estimates to produce a map and a robot trajectory. The constraints are generally non-linear, thus SLAM can be viewed as a non-linear optimization problem. The optimization can be difficult, due to poor initial estimates arising from odometry data, and due to the size of the state space. We present a fast non-linear optimization algorithm that rapidly recovers the robot trajectory, even when given a poor initial estimate. Our approach uses a variant of stochastic gradient descent on an alternative state-space representation that has good stability and computational properties. We compare our algorithm to several others, using both real and synthetic data sets
