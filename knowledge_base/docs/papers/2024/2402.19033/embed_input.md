High-Speed Motion Planning for Aerial Swarms in Unknown and Cluttered Environments

Coordinated flight of multiple drones allows to achieve tasks faster such as search and rescue and infrastructure inspection. Thus, pushing the state-of-the-art of aerial swarms in navigation speed and robustness is of tremendous benefit. In particular, being able to account for unexplored/unknown environments when planning trajectories allows for safer flight. In this work, we propose the first high-speed, decentralized, and synchronous motion planning framework (HDSM) for an aerial swarm that explicitly takes into account the unknown/undiscovered parts of the environment. The proposed approach generates an optimized trajectory for each planning agent that avoids obstacles and other planning agents while moving and exploring the environment. The only global information that each agent has is the target location. The generated trajectory is high-speed, safe from unexplored spaces, and brings the agent closer to its goal. The proposed method outperforms four recent state-of-the-art methods in success rate (100% success in reaching the target location), flight speed (97% faster), and flight time (50% lower)....

## Introduction

The ability of aerial swarms to rapidly fly through cluttered environments while avoiding each other and any other obstacles could result in faster mission accomplishment and increase area coverage in inspection tasks, aerial logistics, or search for rescue missions. However, current approaches to coordinated flight of multiple drones cannot leverage the maximum possible speed of the drones and do not meet the speed conditions for the longest flight distance....

Figure 1: Multiple agents (green spheres) moving towards each other in a simulation environment where the obstacles are occupied voxels in orange. The Safe Corridor of each agent is shown in red, the previous positions as a green line, and the predicted future positions (MIQP/MPC solution) as the yellow line.

## Conclusion

In this work, a new framework for high-speed aerial swarm planning in unknown and cluttered environments is presented. To the best of our knowledge, it is the only framework that explicitly takes into account the unknown space of the environment and can guarantee safety in unknown environments. The method is compared to 4 state-of-the-art methods in simulation and is shown to outperform them in multiple metrics such as speed (67% faster) and flight time (42% lower). Finally, it is tested in the real world on hardware to show the feasibility of the generated trajectories.

During each planning iteration, every agent requires the previously generated trajectories of other agents to generate the TASC (Sect. II-D1) and plan safely. This necessitates broadcasting the current trajectory to all other agents immediately after the last step in the trajectory planning module. The trajectory must reach all other agents within $T_{\text{traj}}$ time from the current iteration's start....

DMP or JPS can generate diagonal paths between 2 occupied voxels (Fig. 5(a)). However, since a real drone would not be able to follow that path because there is no empty space between the obstacles, we do not enable such paths.

The proposed method is compared with AMSwarmX, MADER, RMADER and EGO-Swarm2 (ES2). The maximum acceleration is set to $a_{\text{max}} = {20{\text{m/s}}}$ and the maximum jerk $j_{\text{max}} = {30{\text{m/s}}}$ for all the planners. For MADER and RMADER, each agent is represented as a bounding box of size $0.25 \times 0.25 \times 0.25$ m....
