PANTHER: Perception-Aware Trajectory Planner in Dynamic Environments

This paper presents PANTHER, a real-time perception-aware (PA) trajectory planner for multirotor-UAVs (Unmanned Aerial Vehicles) in dynamic environments. PANTHER plans trajectories that avoid dynamic obstacles while also keeping them in the sensor field of view (FOV) and minimizing the blur to aid in object tracking. The rotation and translation of the UAV are jointly optimized, which allows PANTHER to fully exploit the differential flatness of multirotors to maximize the PA objective. Real-time performance is achieved by implicitly imposing the underactuated dynamics of the UAV through the Hopf fibration. PANTHER is able to keep the obstacles inside the FOV 7.9 and 1.5 times more than non-PA approaches and PA approaches that decouple translation and yaw, respectively. The projected velocity (and hence the blur) is reduced by 18% and 34%, respectively. This leads to average success rates three times larger than state-of-the-art approaches in multi-obstacle avoidance scenarios. The MINVO basis is used to impose low-conservative collision avoidance constraints in position and velocity space.

## Introduction and Related Work

While the last decade has seen an increase on the number of successful deployments of multirotor-UAVs in different real-world scenarios, their applicability is often limited by two common assumptions, namely the fact that the environment is static, and/or the omnidirectional coverage of the sensor(s) of the UAV. Indeed, many UAVs have a limited FOV, and many applications (delivery, aerial videography, emergency response, etc.) have non-static environments due to the presence of cars, people, and/or other UAVs.

We show how the Hopf fibration can be embedded in the planning optimization to jointly optimize translation and yaw while implicitly imposing the underactuated dynamics that couples acceleration and orientation. This avoids the need to explicitly impose the dynamics of the UAV as differential constraints, while automatically guaranteeing the largest possible great-circle distance between the hovering condition and the differential flatness singularity. Dynamic obstacle avoidance constraints are imposed by leveraging the MINVO basis to reduce conservatism.

This paper uses the notation shown in Table II.

## Conclusion

This work derived PANTHER, a perception-aware (PA) trajectory planner in dynamic environments. PANTHER is able to couple together the translation and the full rotation in the optimization, leading to PA trajectories computed in real time that maximize the presence of the obstacles in the FOV while minimizing their projected velocity. Extensive hardware experiments in unknown dynamic environments, with all the computation running onboard, and with relative velocities of up to 6.3 m/s have shown its effectiveness.

Our approach has also some limitations. Specifically, in the hardware experiments we observed the importance of the choice of the obstacle to include in the optimization (i.e., the choice of $i^{\ast}$, see Table II and section II-B): when should the UAV include a specific (already tracked) obstacle in the PA term of the optimization, in order to predict its trajectory more accurately to be able to avoid it, and when should the UAV turn around to explore unknown space?
