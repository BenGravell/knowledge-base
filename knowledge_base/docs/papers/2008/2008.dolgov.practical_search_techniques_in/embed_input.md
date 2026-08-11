<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Practical Search Techniques in Path Planning for Autonomous Driving

Topics include Autonomous driving, Path planning, Hybrid A*, Heuristic search, Nonholonomic vehicles, Path smoothing, Nonlinear optimization, DARPA urban challenge.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces the practical Hybrid A* planning pipeline used by Stanford's Junior in the DARPA Urban Challenge. Continuous vehicle states attached to discrete search cells preserve kinematic feasibility, while a nonlinear optimization pass smooths and improves the resulting path for fast online replanning.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We describe a practical path-planning algorithm that generates smooth paths for an autonomous vehicle operating in an unknown environment, where obstacles are detected online by the robot's sensors. This work was motivated by and experimentally validated in the 2007 DARPA Urban Challenge, where robotic vehicles had to autonomously navigate parking lots. Our approach has two main steps. The first step uses a variant of the well-known A* search algorithm, applied to the 3D kinematic state space of the vehicle, but with a modified state-update rule that captures the continuous state of the vehicle in the discrete nodes of A* (thus guaranteeing kinematic feasibility of the path). The second step then improves the quality of the solution via numeric non-linear optimization, leading to a local (and frequently global) optimum. The path-planning algorithm described in this paper was used by the Stanford Racing Teams robot, Junior, in the Urban Challenge. Junior demonstrated flawless performance in complex general path-planning tasks such as navigating parking lots and executing U-turns on blocked roads, with typical full-cycle replaning times of 50-300ms.
