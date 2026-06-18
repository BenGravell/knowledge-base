<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Randomized Kinodynamic Planning

Topics include Motion planning, Kinodynamic planning, Trajectory planning, Sampling-based, Rapidly-exploring random tree.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces RRTs for sampling-based trajectory planning in high-dimensional configuration spaces.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The paper presents a state-space perspective on the kinodynamic planning problem, and introduces a randomized path planning technique that computes collision-free kinodynamic trajectories for high degree-of-freedom problems. By using a state space formulation, the kinodynamic planning problem is treated as a 2n-dimensional nonholonomic planning problem, derived from an n-dimensional configuration space. The state space serves the same role as the configuration space for basic path planning. The bases for the approach is the construction of a tree that attempts to rapidly and uniformly explore the state space, offering benefits that are similar to those obtained by successful randomized planning methods, but applies to a much broader class of problems. Some preliminary results are discussed for an implementation that determines the kinodynamic trajectories for hovercrafts and satellites in cluttered environments resulting in state spaces of up to twelve dimensions.
