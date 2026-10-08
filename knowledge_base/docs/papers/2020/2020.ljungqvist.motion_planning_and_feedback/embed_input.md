<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Motion Planning and Feedback Control Techniques with Applications to Long Tractor-Trailer Vehicles

Topics include Motion planning, Tractor-trailer systems, Path following, Model predictive control, State estimation, Nonholonomic systems.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Develops motion planning, path-following feedback, and tractor-mounted state estimation for long tractor-trailer vehicles. Combines lattice and closed-loop RRT planning with optimal control and validates the resulting frameworks in laboratory and full-scale vehicle experiments.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

During the last decades, improved sensor and hardware technologies as well as new methods and algorithms have made self-driving vehicles a realistic possibility in the near future. At the same time, there has been a growing demand within the transportation sector to increase efficiency and to reduce the environmental impact related to transportation of people and goods. Therefore, many leading automotive and technology companies have turned their attention towards developing advanced driver assistance systems and self-driving vehicles. Autonomous vehicles are expected to have their first big impact in closed environments, such as mines, harbors, loading and offloading sites. In such areas, the legal requirements are less restrictive and the surrounding environment is more controlled and predictable compared to urban areas. Expected positive outcomes include increased productivity and safety, reduced emissions and the possibility to relieve the human from performing complex or dangerous tasks. Within these sites, tractor-trailer vehicles are frequently used for transportation. These vehicles are composed of several interconnected vehicle segments, and are therefore large, complex and unstable while reversing. This thesis addresses the problem of designing efficient motion planning and feedback control techniques for such systems. The contributions of this thesis are within the area of motion planning and feedback control for long tractor-trailer combinations operating at low-speeds in closed and unstructured environments.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

It includes development of motion planning and feedback control frameworks, structured design tools for guaranteeing closed-loop stability and experimental validation of the proposed solutions through simulations, lab and field experiments. Even though the primary application in this work is tractor-trailer vehicles, many of the proposed approaches can with some adjustments also be used for other systems, such as drones and ships. The developed sampling-based motion planning algorithms are based upon the probabilistic closed-loop rapidly exploring random tree (CL-RRT) algorithm and the deterministic lattice-based motion planning algorithm. It is also proposed to use numerical optimal control offline for precomputing libraries of optimized maneuvers as well as during online planning in the form of a warm-started optimization step. To follow the motion plan, several predictive path-following control approaches are proposed with different computational complexity and performance. Common for these approaches are that they use a path-following error model of the vehicle for future predictions and are tailored to operate in series with a motion planner that computes feasible paths. The design strategies for the path-following approaches include linear quadratic (LQ) control and several advanced model predictive control (MPC) techniques to account for physical and sensing limitations.

<!-- chunk {"id": "abstract-0005", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

To strengthen the practical value of the developed techniques, several of the proposed approaches have been implemented and successfully demonstrated in field experiments on a full-scale test platform. To estimate the vehicle states needed for control, a novel nonlinear observer is evaluated on the full-scale test vehicle. It is designed to only utilize information from sensors that are mounted on the tractor, making the system independent of any sensor mounted on the trailer.
