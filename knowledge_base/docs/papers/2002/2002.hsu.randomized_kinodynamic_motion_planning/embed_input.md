<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Randomized Kinodynamic Motion Planning with Moving Obstacles

Topics include Motion planning, Kinodynamic planning, Moving obstacles, Probabilistic roadmap, Randomized planning, State-time space.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents a randomized kinodynamic planner that samples state-time space by drawing random controls and integrating equations of motion, building a probabilistic roadmap of milestones connected by short admissible trajectories. Extended PRM-style randomized planning into dynamic environments and helped establish the now-standard idea that avoiding dynamic obstacles is fundamentally a spacetime planning problem.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a novel randomized motion planner for robots that must achieve a specified goal under kinematic and/or dynamic motion constraints while avoiding collision with moving obstacles with known trajectories. The planner encodes the motion constraints on the robot with a control system and samples the robot's state × time space by picking control inputs at random and integrating its equations of motion. The result is a probabilistic roadmap of sampled state ×time points, called milestones, connected by short admissible trajectories. The planner does not precompute the roadmap; instead, for each planning query, it generates a new roadmap to connect an initial and a goal state×time point. The paper presents a detailed analysis of the planner's convergence rate. It shows that, if the state×time space satisfies a geometric property called expansiveness, then a slightly idealized version of our implemented planner is guaranteed to find a trajectory when one exists, with probability quickly converging to 1, as the number of milestones increases. Our planner was tested extensively not only in simulated environments, but also on a real robot. In the latter case, a vision module estimates obstacle motions just before planning starts.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The planner is then allocated a small, fixed amount of time to compute a trajectory. If a change in the expected motion of the obstacles is detected while the robot executes the planned trajectory, the planner recomputes a trajectory on the fly. Experiments on the real robot led to several extensions of the planner in order to deal with time delays and uncertainties that are inherent to an integrated robotic system interacting with the physical world.
