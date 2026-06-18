PANTHER: Perception-Aware Trajectory Planner in Dynamic Environments

This paper presents PANTHER, a real-time perception-aware (PA) trajectory planner for multirotor-UAVs (Unmanned Aerial Vehicles) in dynamic environments. PANTHER plans trajectories that avoid dynamic obstacles while also keeping them in the sensor field of view (FOV) and minimizing the blur to aid in object tracking. The rotation and translation of the UAV are jointly optimized, which allows PANTHER to fully exploit the differential flatness of multirotors to maximize the PA objective. Real-time performance is achieved by implicitly imposing the underactuated dynamics of the UAV through the Hopf fibration. PANTHER is able to keep the obstacles inside the FOV 7.9 and 1.5 times more than non-PA approaches and PA approaches that decouple translation and yaw, respectively. The projected velocity (and hence the blur) is reduced by 18% and 34%, respectively. This leads to average success rates three times larger than state-of-the-art approaches in multi-obstacle avoidance scenarios. The MINVO basis is used to impose low-conservative collision avoidance constraints in position and velocity space....

## Introduction and Related Work

Table I: Classification of the related work, together with a (nonexhaustive) list of references.

While the last decade has seen an increase on the number of successful deployments of multirotor-UAVs in different real-world scenarios, their applicability is often limited by two common assumptions, namely the fact that the environment is static, and/or the omnidirectional coverage of the sensor(s) of the UAV. Indeed, many UAVs have a limited FOV, and many applications (delivery, aerial videography, emergency response, etc.) have non-static environments due to the presence of cars, people, and/or other UAVs....

Another possible direction of future work is to solve the trade-off between visibility and time optimality. This would entail adding the time minimization in the optimization problem of section II-D4, and would also allow to highlight the advantages of the Hopf fibration when flying aggressive trajectories that pass close to the singularity produced by the commonly-used maps presented in (first two definitions of Table III).

Finally, another interesting research direction is how to incorporate disturbances in the planning problem, while still guaranteeing that the tracking error of the UAV remains bounded. The incorporation of such disturbance information is especially important when flying outdoors under windy conditions, since a large deviation between the planned trajectory and the actual trajectory can provoke a collision with the obstacles.

We use the Octopus Search Algorithm (OSA), which is a search-based algorithm that operates directly on the control points of the position spline. It ensures collision-free constraints between the agent and the dynamic obstacles by finding the planes that separate the inflated MINVO polyhedral representation of each interval $j$ of the trajectory of the obstacle $i$ (denoted as $\mathcal{C}_{ij}^{\text{MV}}$) and the MINVO polyhedral representation of that interval $j$ of the trajectory of the agent, denoted as $\left( \mathcal{Q}_{j}^{\text{MV}} \right)_{\text{agent}}$ (see Fig. 2)....

is the trajectory the UAV is currently optimizing, t ∈ [tin,tf]

For the obstacle avoidance of dynamic obstacles, we first create a polyhedral outer representation of both the trajectory of the agent and of the obstacle (see Fig....
