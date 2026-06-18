<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

RRT-Connect: An Efficient Approach to Single-Query Path Planning

Topics include Motion planning, Kinodynamic planning, Trajectory planning, Sampling-based, Rapidly-exploring random tree.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends RRT with bidirectional search (two trees, one from start and one from goal).

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A simple and efficient randomized algorithm is presented for solving single-query path planning problems in high-dimensional configuration spaces. The method works by incrementally building two rapidly-exploring random trees (RRTs) rooted at the start and the goal configurations. The trees each explore space around them and also advance towards each other through, the use of a simple greedy heuristic. Although originally designed to plan motions for a human arm (modeled as a 7-DOF kinematic chain) for the automatic graphic animation of collision-free grasping and manipulation tasks, the algorithm has been successfully applied to a variety of path planning problems. Computed examples include generating collision-free motions for rigid objects in 2D and 3D, and collision-free manipulation motions for a 6-DOF PUMA arm in a 3D workspace. Some basic theoretical analysis is also presented.
