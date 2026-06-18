<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

High-Speed Motion Planning for Aerial Swarms in Unknown and Cluttered Environments

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Coordinated flight of multiple drones allows to achieve tasks faster such as search and rescue and infrastructure inspection. Thus, pushing the state-of-the-art of aerial swarms in navigation speed and robustness is of tremendous benefit. In particular, being able to account for unexplored/unknown environments when planning trajectories allows for safer flight. In this work, we propose the first high-speed, decentralized, and synchronous motion planning framework (HDSM) for an aerial swarm that explicitly takes into account the unknown/undiscovered parts of the environment. The proposed approach generates an optimized trajectory for each planning agent that avoids obstacles and other planning agents while moving and exploring the environment. The only global information that each agent has is the target location. The generated trajectory is high-speed, safe from unexplored spaces, and brings the agent closer to its goal. The proposed method outperforms four recent state-of-the-art methods in success rate (100% success in reaching the target location), flight speed (97% faster), and flight time (50% lower).

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finally, the method is validated on a set of Crazyflie nano-drones as a proof of concept.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The ability of aerial swarms to rapidly fly through cluttered environments while avoiding each other and any other obstacles could result in faster mission accomplishment and increase area coverage in inspection tasks, aerial logistics, or search for rescue missions. However, current approaches to coordinated flight of multiple drones cannot leverage the maximum possible speed of the drones and do not meet the speed conditions for the longest flight distance. Although recent work on drone racing achieved human-competitive flight speed through gates, those trajectory planning algorithms apply to a single drone, assume knowledge of the environment, and do not generalize well to flight in environments with unknown obstacle layouts.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

While early methods of trajectory planning of aerial swarm in cluttered environments were centralized, more recent work focused on decentralized approaches where each drone can compute its trajectory based on local information, and thus better scale up in computation time and communication range. Consequently, here we discuss the state-of-the-art in decentralized approaches that produce coordinated flight trajectories in cluttered environments (Tab. I). These methods fall into two categories depending on inter-drone communication mode: asynchronous or synchronous.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Asynchronous approaches do not require periodic communication between agents. EGO-Swarm, an extension of a gradient-based planner for a single agent, is a recent example of an asynchronous multi-drone planner. However, it cannot handle communication delay between the agents and assumes perfect knowledge of occluded obstacles. EGO-Swarm2 uses the MINCO trajectory parametrization instead of B-Splines of EGO-Swarm to produce smoother trajectories and a lower optimization time. However, it cannot handle communication delay and it flies slower in unknown environments. EDG-Team improves over EGO-Swarm2 by dealing with deadlocks between multiple agents that pass through narrow gaps. This is achieved by switching the method to a centralized and synchronous planner in dense environments. The method was proven to be more robust to communication delay but could not guarantee collision-free navigation. MADER and its delay-robust version RMADER are another family of asynchronous planners. They both use the MINVO basis to generate trajectories that can pass through narrow gaps.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Both approaches assume perfect knowledge of the obstacle positions and shapes within a bounding box around each agent and do not account for the unknown part of the environment, which could lead to collisions. DREAM is another asynchronous planning method for aerial swarms that minimizes collision probabilities, but cannot guarantee safety in unknown environments. MRNAV was built on top of DREAM to provide collision-free and deadlock-free flight using a centralized, long-horizon planning module. MRNAV retains communication delay robustness of DREAM but still does not guarantee safety in unknown environments.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In dense environments, EDG-Team switches to a centralized and synchronous planner that executes joint optimization.
The long horizon module runs on a centralized system that communicates with the planning robots periodically.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast to asynchronous methods, synchronous approaches require periodic communication of the trajectories between all agents, which can result in faster trajectories. AMSwarmX is a synchronous method that uses Bernstein polynomials as trajectory parametrization. However, it assumes no communication delays between the agents as well as prior knowledge of the environment. The same assumptions are made by DPDS, which uses a discretized trajectory and MPC optimization for obstacle avoidance where obstacles are represented by mathematical functions (e.g. cylinders, paraboloids). Some synchronous planning methods are based on linear safe corridors, which use separating hyperplanes to guarantee collision avoidance with static obstacles and the other planning agents, such as LSC and its extension to dynamic obstacles DLSC. However, these methods do not account for communication delay and assume prior knowledge of the environment.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Here we propose a high-speed decentralized and synchronous motion (HDSM) planning method for aerial swarms that can operate in cluttered and unknown environments with a guarantee of collision-free navigation (Fig. 1). The method builds on our previous work for aerial swarm motion planning and its extension to arbitrary communication delays. However, those methods were unable to deal with unknown environments, unlike the proposed approach. Furthermore, the method described here introduces novelties that reduce trajectory lengths, allow drones to fly through narrow gaps, and adapt flight speed to environment density. Taken together, all these improvements substantially increase flight speed while producing collision-free trajectories. When compared to four recent and open-source methods that outperform all other state-of-the-art approaches (Sect. III-B), the method described here results in 67% higher flight speed and 42% lower flight time with 100% mission success rate. Finally, while all state-of-the-art approaches (Tab. I) are implemented in ROS1 or Matlab, the method described here takes advantage of ROS2 peer-to-peer communication and other real-time and security features.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Overview", "weight": 1.0} -->

The HDSM method consists of two modules that run in parallel on each of the $M$ drones that make the aerial swarm: the mapping module and the planning module (Fig. 2). The mapping module takes in a depth point cloud from sensors and generates a voxel grid representation of the environment. The voxel grid is partitioned into free, occupied, and unknown voxels. The module is updated at a period $T_{\text{map}}$. The voxel grid is given to the planning module which consists of two sub-modules that run in parallel (Fig. 3). The first sub-module takes the voxel grid as input and generates a global path between the current position and the target position at a period $T_{\text{path}}$. The second sub-module takes as inputs the voxel grid, the global path, and the trajectories of the other drones, and generates a collision-free and dynamically feasible trajectory at a period $T_{\text{traj}}$. Running the path generation and trajectory generation in parallel allows each agent more time to share its trajectory with other drones before the next planning iteration begins (Fig. 3).

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Overview", "weight": 1.0} -->

The periods $T_{\text{map}}$ and $T_{\text{path}}$ are usually chosen equal to the sensor measurement period, whereas the period $T_{\text{traj}}$ is chosen to be smaller than $T_{\text{path}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-B The Mapping Module", "weight": 1.0} -->

The objective of the mapping module is to provide the most up-to-date representation of the local environment in the form of a voxel grid given all the previous sensory measurements. It relies on a depth point cloud from 360-degree sensors, which can be produced by several commercial drones (Skydio, DJI, e.g.). Fig. 4 illustrates the mapping module steps. It takes as input the most recent point cloud and transforms it into a voxel grid $G_{\text{meas}}$, which can be generated by GPU accelerators for lower latency, which is then merged with the latest computed voxel grid $G_{\text{last}}$. Each grid is a cuboid of fixed dimensions and of fixed voxel size $l_{\text{vox}}$ where each voxel is a cube. The user selects the dimensions and voxel size to balance between the time it takes to compute the voxel grid and the extent of the area mapped.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B The Mapping Module", "weight": 1.0} -->

The voxel grid's origin coordinates ($x,y,z$) are chosen according to the following rules: each coordinate of the origin is a multiple of $l_{\text{vox}}$ and the voxel at the center of the grid contains the current position of the agent. This makes sure that as the grid moves with the agent, individual voxels can be compared and merged in a one-to-one fashion between $G_{\text{meas}}$ and $G_{\text{last}}$. Every time a new point cloud is produced by the sensors, a grid full of unknown voxels $G_{\text{meas}}$ is generated (measurement grid). First, all the voxels that contain at least a point of the point cloud are set to occupied. Raycasting is then performed from the center of the grid to every voxel on the borders of the grid, freeing all the voxels on the raycasted line until an occupied voxel is encountered.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B The Mapping Module", "weight": 1.0} -->

Finally, the unknown voxels of $G_{\text{meas}}$ are replaced with their value from $G_{\text{last}}$, and $G_{\text{last}}$ is set to $G_{\text{meas}}$. This step can utilize a probabilistic approach (log odds ) without requiring any modifications to the planning module.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-C The global path generation module", "weight": 1.0} -->

The global path generation module (Fig. 2) takes as input the last voxel grid $G_{\text{last}}$ and the goal position ${\mathbf{p}}_{\text{goal}}$ to generate a path in the free space of the voxel grid. If the goal ${\mathbf{p}}_{\text{goal}}$ is outside the voxel grid, an intermediate goal ${\mathbf{p}}_{\text{goal,inter}}$ is set where the line connecting the agent position and the goal position ${\mathbf{p}}_{\text{goal}}$ intersects the voxel grid border (all border voxels are always left free for positioning of ${\mathbf{p}}_{\text{goal,inter}}$).

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-C The global path generation module", "weight": 1.0} -->

The module starts from $G_{\text{last}}$ and frees up all unknown voxels to generate $G_{\text{last,free}}$ because if the unknown voxels are assumed to be occupied, the goal may not be reachable when doing the path search. At this point, the module inflates the dimensions of the voxels by taking into account the agent radius (agent modeled as a sphere with radius $r_{\text{agent}}$) and finds a path from the current agent position ${\mathbf{p}}_{\text{curr}}$ to ${\mathbf{p}}_{\text{goal,inter}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-C The global path generation module", "weight": 1.0} -->

The objective is to find a short path that is also pushed away from obstacles so that there is a safety margin between the drone and the obstacles (the drone will try to follow that path in the trajectory generation module). For this reason, a potential field is created around obstacles to increase the cost of paths passing too close to these obstacles, discouraging their selection during any subsequent path search (see Appendix VI-A1 for more details). Doing an A\* search with a potential field (denoted as Distance Map Planner (DMP) ) over the whole voxel grid would be computationally expensive. For this reason, the shortest path is first found while ignoring the potential field. Then, that shortest path is used to create a small region around it (search corridor). The DMP is then restricted to that region, reducing the number of voxels the DMP search has to consider and thus reducing the computational time. The path generated by DMP is finally shortened for better optimality (Fig. 5(b) - see Appendix VI-A2) to get the final global path that the drone will try to follow in the trajectory generation module.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-C The global path generation module", "weight": 1.0} -->

Jump Point Search (JPS) is used to first find the shortest path while ignoring the potential field because it offers path optimality guarantees with reduced computation time compared to A\*. The search corridor is the union of all the voxels that are within a distance $d_{\text{search}}$ of the JPS path.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-C The global path generation module", "weight": 1.0} -->

DMP or JPS can generate diagonal paths between 2 occupied voxels (Fig. 5(a)). However, since a real drone would not be able to follow that path because there is no empty space between the obstacles, we do not enable such paths.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-D The trajectory generation module", "weight": 1.0} -->

This module takes as input the last generated global path, voxel grid, and trajectories of other drones, and generates the trajectory executed by the drone (Fig. 2). It runs synchronously on all agents, i.e. all the agents start generating their own trajectory at the same time in a periodic fashion. This requires the clocks of all agents to be synchronized. It is run at a constant period $T_{\text{traj}}$. The objective of this module is to make the drone follow the last generated global path as fast as possible while guaranteeing no collisions with the static obstacles and other agents. This is achieved through 3 sub-modules that run sequentially (Fig. 3): TASC (Time-Aware Safe Corridor) generation, which generates constraints to avoid collisions with obstacles and other drones; reference generation, which samples the global path to generate a reference trajectory for the Model Predictive Controller (MPC) to follow; and Mixed-Integer Quadratic Program/Model Predictive Control (MIQP/MPC) solver, which generates a dynamically feasible trajectory that is constrained in the TASC and that follows the reference trajectory while optimizing for smoothness.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-D1 TASC generation", "weight": 1.0} -->

In this module, a safe corridor is generated around the global path that covers the free space and avoids static obstacles (blue polyhedra in Fig. 2). Then, hyperplanes are added between the agents (in the middle) to split the space into 2 volumes and constrain each agent to one volume to ensure no collisions occur between the agents. The combination of the safe corridor and the added hyperplanes is called the Time-Aware Safe Corridor (TASC). The time awareness comes from the fact that the hyperplanes are generated from the trajectories of the other agents at the previous iteration, and are used to constrain future positions of agents at the current planning iteration. The generation of the TASC is detailed in Appendix VI-B1.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-D2 Reference trajectory generation", "weight": 1.0} -->

This module's goal is to create a reference trajectory for the MPC/MIQP that has $N$ discretization steps. It samples the most recent global path to produce a reference trajectory for the MPC to follow. Each planning iteration involves sampling $N$ points starting from a reference point ${\mathbf{p}}_{0,\text{ref}}$, which is the agent's location at the very first iteration of the planning algorithm. The sampling progresses along the global path at a speed $v_{\text{samp}}$ to end at ${\mathbf{p}}_{N,\text{ref}}$ (Fig. 2). To ensure efficient navigation, the module employs an algorithm to dynamically modulate $v_{\text{samp}}$, allowing the agent to move faster in open areas and slow down in cluttered spaces.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-D2 Reference trajectory generation", "weight": 1.0} -->

As the agent moves and progresses along the path, the reference trajectory is updated to reflect this movement, ensuring that it is always pushing the drone along the path and towards the final goal. This update mechanism involves sampling the trajectory at each iteration and adjusting the starting point of the sampling based on the agent's proximity to the points sampled at the previous planning iteration. The full description of the reference trajectory generation process is in Appendix VI-B2.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-D3 MIQP/MPC solver", "weight": 1.0} -->

This module takes the reference trajectory and the TASC and generates a dynamically feasible and collision-free trajectory that brings the agent closer to its goal position. The generated trajectory is the result of an MPC/MIQP optimization that constrains the trajectory inside the TASC for collision-free navigation. The cost function of this optimization makes the generated trajectory follow closely the reference trajectory while ensuring a level of smoothness through a jerk cost. The full optimization formulation is derived in Appendix VI-B3.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-D4 Communication between agents", "weight": 1.0} -->

During each planning iteration, every agent requires the previously generated trajectories of other agents to generate the TASC (Sect. II-D1) and plan safely. This necessitates broadcasting the current trajectory to all other agents immediately after the last step in the trajectory planning module. The trajectory must reach all other agents within $T_{\text{traj}}$ time from the current iteration's start. If the computation time for the current trajectory is $t_{\text{comp}}$, this leaves $t_{\text{lim}} = {T_{\text{traj}} - t_{\text{comp}}}$ time for the trajectory to reach all other agents before the next planning iteration begins for all agents. Minimizing computation time is essential to accommodate communication latency, hence why the path planning module is done on a different thread (Fig. 3). If the delay exceeds $t_{\text{lim}}$, we can deal with it actively by adapting the planning period.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-D4 Communication between agents", "weight": 1.0} -->

Furthermore, if an agent does not receive the trajectory of another nearby agent due to packet loss, it continues executing its previously generated trajectory, ensuring collision-free navigation for all agents in the swarm (see Appendix VI-C for more details).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

Mean flight time (s)
Mean flight velocity (m/s)
Mean flight distance (m)

<!-- chunk {"id": "body-0029", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

The simulations are run on Intel i9-13900K CPU with a base frequency of 3.0GHz and a turbo boost of 5.8GHz. ROS2 is used for communication between the mapping module and the planning module as well as for communication between the different agents. All methods have access to ground truth states and perfect control.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

The planner is tested in 3 different environments. One free environment and 2 environments with obstacles. The comparison in the free environment is done with AMSwarmX, EGO-Swarm2 (ES2), MADER and RMADER. In the environments with obstacles, the comparison is done only with EGO-Swarm2 since it performs considerably better than the other methods. The comparison is done with 2 versions of our planner. The first version is HDSM where the planner has privileged information about the obstacles i.e. it knows the position and shape of the obstacles within a bounded box around it. Privileged information is required by all the planners used in the comparison. The other version is HDSM\* where the planner only sees the obstacles that are in the agent's field of view i.e. the planner is not aware of all the occluded obstacles. This is where our mapping framework comes into play i.e. to determine the unexplored/unseen areas that are unsafe to navigate.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

For comparison between the different methods, the following performance metrics are used: collision \[%\] (percentage of simulations that resulted in a collision); flight distance; flight velocity; flight time; acceleration cost ($\int{{\|{{\mathbf{a}}{(t)}}\|}^{2}{dt}}$); jerk cost ($\int{{\|{{\mathbf{j}}{(t)}}\|}^{2}{dt}}$); success (number of simulation runs where all agents successfully reached their goal position without any collision); deadlock rate \[%\] (percentage of generated trajectories that resulted in a deadlock).

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A Planner parameters", "weight": 1.0} -->

The local voxel grid around each agent is of size $20 \times 20 \times 6$ m and has a voxel size of $0.3$ m. The following parameters are chosen: $N = 9$, $h = 100$ ms, $v_{\text{samp,min}} = 4.5$ m/s, $v_{\text{samp,max}} = 6$ m/s, $s_{d} = 0.001$, $s_{o} = 0.01$, $d_{\text{pot,max}} = 0.6$ m, $d_{\text{search}} = 1.5$ m. The vertical offset is set equal to the agent radius $z_{\text{offset}} = r_{\text{agent}}$ (the radius will be different for each environment).

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A Planner parameters", "weight": 1.0} -->

The period of the mapping module is $T_{\text{map}} = 200$ ms, of the path generation submodule $T_{\text{path}} = 200$ ms, and of the trajectory generation submodule $T_{\text{traj}} = 100$ ms. The starting index for the path planning algorithm is $i_{\text{path,start}} = 9$. The jerk and acceleration limits are set differently for each experiment and will be specified in the corresponding section.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B Empty environment", "weight": 1.0} -->

The testing consists of 10 agents in a circular configuration exchanging positions. The circle is of radius 10 m and the agents are positioned in an equidistant way on the circle (Fig. 6(a)). Each agent exchanges its position with the agent that is diametrically opposite. The comparison is done over 10 simulated runs.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B Empty environment", "weight": 1.0} -->

The proposed method is compared with AMSwarmX, MADER, RMADER and EGO-Swarm2 (ES2). The maximum acceleration is set to $a_{\text{max}} = {20{\text{m/s}}}$ and the maximum jerk $j_{\text{max}} = {30{\text{m/s}}}$ for all the planners. For MADER and RMADER, each agent is represented as a bounding box of size $0.25 \times 0.25 \times 0.25$ m. For EGO-Swarm2, AMSwarmX, and our planner, each agent is represented as a sphere of diameter $0.25$. The MADER/RMADER values are taken from the results reported by their authors since they have been fine-tuned for this experiment where the maximum speed is set to $v_{\text{max}} = 10$ m/s (the values were computed from 100 simulation runs ).

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-B Empty environment", "weight": 1.0} -->

We fine-tuned to the best of our ability the parameters of AMSwarmX, mainly relying on the parameters set by the authors. AMSwarmX results in collisions as soon as the speed limit exceeds 2 m/s. For EGO-Swarm2, we fine-tuned its parameters with a large sensing horizon (10 m) and planning horizon (15 m). Different speed limits are tested: 4, 5, 6, and 7 m/s all shown in Tab. II. Note that the average speed performance of the planner improves from 4 m/s until 6 m/s is reached. After that, the average navigation speed decreases while the jerk cost goes up (which is why we stopped at 7 m/s).

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-B Empty environment", "weight": 1.0} -->

Our method outperforms the other methods in mean speed and flight time as shown in Tab. II. It is 28.8% faster than the second-best performer (ES2 - 6 m/s). In terms of flight distance, the difference is negligible between all the methods: the best performer (ES2 - 4 m/s) is only 3.3% better than the worst performer (AMSwarmX).

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-C Environment with obstacles", "weight": 1.0} -->

Our planner is also tested in 2 environments with obstacles. The first one is a circular exchange: the agents are set up in a circular configuration on a circle of radius 22 m and each agent exchanges its position with the agent that is diametrically opposite. A forest of 90 cylindrical obstacles is generated inside a box of size $30 \times 30 \times 20$ m that is centered at the circle's center (density 0.1 obst/m^2^). The positions of the obstacles are generated following a uniform distribution (Fig. 8).

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-C Environment with obstacles", "weight": 1.0} -->

The second environment is linear navigation: the agents start on a line next to each other and then navigate through a cluttered environment to reach their goal. The goal of each agent is its initial position translated 96 m in the positive $x$ direction (Fig. 7(a)). The cluttered environment consists of 2 cylindrical forests of size $30 \times 30 \times 20$ m separated by a wall with rectangular openings in it (Fig. 7(b)). The first forest is centered at $$ and contains 90 cylinders (density 0.1 obst/m^2^). The second forest is centered at $$ and contains 180 cylinders (density 0.2 obst/m^2^). The separating wall is 0.6 m thick and contains 11 openings. Its width is 30 m and its height is 15 m.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-C Environment with obstacles", "weight": 1.0} -->

The cylinders are all of radius 0.15 m and length 20 m. Their center of gravity is sampled uniformly inside the forest volume. additional environments with obstacles. The radius of each agent is set to 0.3 m (in contrast to 0.125 m in the empty environment) for experimental diversity.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-C Environment with obstacles", "weight": 1.0} -->

The dynamical limits are set to $a_{\text{max}} = 40$ m/s^2^ and $j_{\text{max}} = 80$ m/s^3^ for EGO-Swarm2 and our planners HDSM/HSDM^\*^. The performance of the planner in the considered environments as well as in other environments is shown in the supplementary video. The results of 10 simulation runs where the forests of cylinders have been randomized are shown in Tab. III.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-C Environment with obstacles", "weight": 1.0} -->

HDSM and HDSM^\*^ are compared with 3 versions of EGO-Swarm2 where the maximum velocity $v_{\text{max}}$ is set to 4, 5, and 6 m/s. Note that this limit is on the $x$, $y$, and $z$ components of the velocity, and thus the norm of the velocity can get up to $\sqrt{3} \cdot v_{\text{max}}$. In the circle environment, EGO-Swarm2 loses robustness when the maximum speed is set to 6 m/s (5/10 runs where successful): the trajectories start going through the static obstacles. This phenomenon happens when the speed is set to 5 m/s in the linear environment and the collisions happen when agents are trying to traverse the wall. This is because EGO-Swarm2 relies on discretization of the trajectory which can result in a point being on one side of the wall and its subsequent point being on the other side.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-C Environment with obstacles", "weight": 1.0} -->

In both the circle and linear environments, HDSM and HDSM^\*^ largely outperform EGO-Swarm2 in flight velocity and flight time. Note that even though EGO-Swarm2 has privileged information about occluded obstacles in comparison with HDSM^\*^, HDSM^\*^ is still 67% faster in terms of mean flight velocity and has a 42% lower mean flight time than the best version of EGO-Swarm2 (ES2 - 6 m/s in the circle experiment). In terms of smoothness (acceleration and jerk costs), EGO-Swarm2 outperforms our planner due to its low-speed navigation.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-D Computation time and communication latency", "weight": 1.0} -->

The computation time of each step of the planning algorithm over all simulations (with and without obstacles) is shown in Fig. 6(c) using a boxplot showing the median (line inside the box), 25^th^ and 75^th^ percentile (bottom and upper limits of the box), and the min and max (bottom and upper whiskers). The communication latency percentile is shown in Fig. 6(b). The computation time for the local reference generation step is negligible compared to the other steps, and thus not shown separately in Fig. 6(c). Since 100% of all communication delay is less than 15 ms, and our total computation time (without the path planning step which is run in parallel) never exceeds 40 ms, safety is guaranteed because ${40 + 15} < T_{\text{traj}} = 100$ ms. The mean computation time of our planner is 9.3 ms and the mean for EGO-Swarm2 is 1.6 ms.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-D Computation time and communication latency", "weight": 1.0} -->

The computation time of the mapping framework over all simulations that require raycasting (HDSM^\*^) has a mean of 10.6 ms, a standard deviation of 2.7 ms, and a max of 21.3 ms.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Hardware experiments", "weight": 1.0} -->

The dynamic feasibility of our planner is tested using 7 nano-drones: the Crazyflies. The drones start in the formation shown in Fig. 9(a), with a 0.9 m distance between them. They then proceed to traverse the environment to the goal position which is their current position translated 6 m forward. After reaching their goal, the drones traverse the environment again in the opposite direction and go back to their initial positions. Due to the computational limitations of the Crazyflie, the planner is run on a separate PC and sends the commands to the drones to execute using CrazySwarm2. The positions of the obstacles in the test environment (Fig. 9(a)) are assumed to be known beforehand since the sensing capabilities of the Crazyflie are limited. They are placed in the real world for symbolic purposes (Fig. 9(b)).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Hardware experiments", "weight": 1.0} -->

The dynamics are limited to the following to adhere to the drone's dynamical limitations and the built-in controller performance: $v_{\text{max}} = 1.5$ m/s, $a_{\text{max}} = 3$ m/s^2^, $j_{\text{max}} = 4$ m/s^3^, $v_{\text{samp,min}} = 1.5$ m/s, $v_{\text{samp,max}} = 1.5$ m/s. The other planner parameters are the same as the ones presented in Sect. III-A. The Crazyflie has a radius of $7$ cm radius, but the collision radius is set to $r_{\text{agent}} = 0.3$ m, and the vertical offset to avoid the downwash of other drones is set to $z_{\text{offset}} = 0.6$ m. The large safety radius is to avoid interactions between the airflow/downwash of the drones, which can make the drones unstable. The Mellinger controller is used.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Hardware experiments", "weight": 1.0} -->

However, one could reduce the safety radius as well as the vertical offset by employing recent advances in control for swarms such as Neural-Swarm2.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Hardware experiments", "weight": 1.0} -->

The voxel size is set to $0.2$ m and the obstacles are inflated by one voxel. The potential distance is set to $d_{\text{pot,max}} = 0.4$ m, and $d_{\text{search}} = 0.6$ m. The drones were able to execute the trajectories without any crashes (going to the goal area and back to the initial position 2 times). The mean tracking error was 6.8 cm, the standard deviation 2.5 cm, and the maximum tracking error was 10.4 cm. Since the distance between the center of gravity of the drone and the obstacles will always be bigger than 20 cm (because the obstacles are inflated by one voxel), safety is guaranteed. This is because the sum of the radius (7 cm) and the maximum tracking error (10.4 cm) is smaller than 20 cm. This demonstrates to a certain extent that the trajectories generated by our planner are dynamically feasible enough for real-world operations. The performance of the drones is shown in the video.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Limitations", "weight": 1.5} -->

Dynamic obstacles are not considered in the framework. They can be added by creating a larger potential field around them in the direction of their motion or their reachable space. Limitations of the proposed framework also include the lack of a mechanism to deal with deadlocks that happen when multiple agents are passing through an extremely narrow gap (especially when the agents are coming from opposing sides of the gap). Another notable limitation is dealing with CPU clock drift, which can lead to unsynchronized trajectories and thus, collisions. Modern CPU clocks have a drift of 100 parts per million (ppm). This means if the clocks are synchronized at the start of a mission, they will deviate by 180 ms after 30 minutes of operation (which is much larger than the planning period of 100 ms). This would require periodic synchronization of the clocks, or using clocks with lower drift (0.1 ppm) which makes a single synchronization at the start of the mission sufficient for safe operations.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, a new framework for high-speed aerial swarm planning in unknown and cluttered environments is presented. To the best of our knowledge, it is the only framework that explicitly takes into account the unknown space of the environment and can guarantee safety in unknown environments. The method is compared to 4 state-of-the-art methods in simulation and is shown to outperform them in multiple metrics such as speed (67% faster) and flight time (42% lower). Finally, it is tested in the real world on hardware to show the feasibility of the generated trajectories.
