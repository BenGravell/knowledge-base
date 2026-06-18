Funnel Libraries for Real-Time Robust Feedback Motion Planning

Topics include Convex optimization, Motion planning, Robotics, Aerial robotics, Vehicles, Safety, Robustness, Uncertainty, Real-time systems, Online algorithms, Optimization, Planning, Control.

We consider the problem of generating motion plans for a robot that are guaranteed to succeed despite uncertainty in the environment, parametric model uncertainty, and disturbances. Furthermore, we consider scenarios where these plans must be generated in real-time, because constraints such as obstacles in the environment may not be known until they are perceived (with a noisy sensor) at runtime. Our approach is to pre-compute a library of "funnels" along different maneuvers of the system that the state is guaranteed to remain within (despite bounded disturbances) when the feedback controller corresponding to the maneuver is executed. We leverage powerful computational machinery from convex optimization (sums-of-squares programming in particular) to compute these funnels. The resulting funnel library is then used to sequentially compose motion plans at runtime while ensuring the safety of the robot. A major advantage of the work presented here is that by explicitly taking into account the effect of uncertainty, the robot can evaluate motion plans based on how vulnerable they are to disturbances....

## Introduction

Imagine an unmanned aerial vehicle (UAV) flying at high speed through a cluttered environment in the presence of wind gusts, a legged robot traversing rough terrain, or a mobile robot grasping and manipulating previously unlocalized objects in the environment. These applications demand that the robot move through (and in certain cases interact with) its environment with a very high degree of agility while still being in close proximity to obstacles. Such systems today lack guarantees on their safety and can fail dramatically in the face of uncertainty in their environment and dynamics.

The tasks mentioned above are characterized by three main challenges. First, the dynamics of the system are nonlinear, underactuated, and subject to constraints on the input (e.g. torque limits). Second, there is a significant amount of uncertainty in the dynamics of the system due to disturbances and modeling error. Finally, the geometry of the environment that the robot is operating in is unknown until runtime, thus forcing the robot to plan in *real-time*.

Due to the computation time associated with funnels, the approach presented in this work had two phases: an offline phase for computing funnels and an online stage for real-time planning with funnels. Recently, more scalable alternatives to SOS programming have been introduced \[Ahmadi and Majumdar, 2016, Ahmadi and Majumdar, 2014\]. These alternatives rely on *linear* and *second-order cone programming* instead of semidefinite programming. This makes it possible to obtain large computational gains in terms of scalability and running time using DSOS and SDSOS programming as compared to SOS programming....

We believe that the work presented in this paper has the potential to be deployed on real robots to make them operate safely in real-world environments. Our hope is that by building upon this work and pursuing the directions for future research presented above we can make this a reality.

Sequential composability of $(F_{1},F_{2})$ is equivalent to the following condition:

Recall that the ability to minimize the volume of the ellipsoid $\mathcal{E}$ using SDP relied on being able to maximize the determinant of $S_{k}$. In order to minimize the volume of $\mathcal{E}_{p}$, we would have to maximize det$(S_{k}^{(p)})$, which is a complicated (i.e. nonlinear) function of $S_{k}$....
