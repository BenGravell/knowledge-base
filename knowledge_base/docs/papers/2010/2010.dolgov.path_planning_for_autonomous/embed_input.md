<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Path Planning for Autonomous Vehicles in Unknown Semi-structured Environments

Topics include Autonomous vehicles, Hybrid A*, Path planning, Trajectory optimization, Urban challenge, Parking lots.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Describes the two-stage planner used for autonomous driving in unknown semi-structured environments: a kinematically feasible Hybrid A* search followed by numerical trajectory improvement. The paper is a key practical reference for vehicle planning in parking lots and unstructured road spaces.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We describe a practical path-planning algorithm for an autonomous vehicle operating in an unknown semi-structured (or unstructured) environment, where obstacles are detected online by the robot's sensors. This work was motivated by and experimentally validated in the 2007 DARPA Urban challenge, where robotic vehicles had to autonomously navigate parking lots. The core of our approach to path planning consists of two phases. The first phase uses a variant of A* search (applied to the 3D kinematic state space of the vehicle) to obtain a kinematically feasible trajectory. The second phase then improves the quality of the solution via numeric non-linear optimization, leading to a local (and frequently global) optimum. Further, we extend our algorithm to use prior topological knowledge of the environment to guide path planning, leading to faster search and final trajectories better suited to the structure of the environment. We present experimental results from the DARPA Urban challenge, where our robot demonstrated near-flawless performance in complex general path-planning tasks such as navigating parking lots and executing U-turns on blocked roads. We also present results on autonomous navigation of real parking lots.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In those latter tasks, which are significantly more complex than the ones in the DARPA Urban challenge, the time of a full replanning cycle of our planner is in the range of 50—300 ms.
