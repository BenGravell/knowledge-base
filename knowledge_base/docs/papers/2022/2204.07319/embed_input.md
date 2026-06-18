A Review of Path Following Control Strategies for Autonomous Robotic Vehicles: Theory, Simulations, and Experiments

Topics include Robotics, Vehicles, Control, Frenet-serret, F-S, Parallel transport, P-T, Reference frame, MATLAB.

This article presents an in-depth review of the topic of path following for autonomous robotic vehicles, with a specific focus on vehicle motion in two dimensional space (2D). From a control system standpoint, path following can be formulated as the problem of stabilizing a path following error system that describes the dynamics of position and possibly orientation errors of a vehicle with respect to a path, with the errors defined in an appropriate reference frame. In spite of the large variety of path following methods described in the literature we show that, in principle, most of them can be categorized in two groups: stabilization of the path following error system expressed either in the vehicle's body frame or in a frame attached to a "reference point" moving along the path, such as a Frenet-Serret (F-S) frame or a Parallel Transport (P-T) frame. With this observation, we provide a unified formulation that is simple but general enough to cover many methods available in the literature. We then discuss the advantages and disadvantages of each method, comparing them from the design and implementation standpoint....

## Introduction

Path-following (PF) is one of the most fundamental tasks to be executed by autonomous vehicles. It consists of driving a vehicle to and maintaining it on a pre-defined path while tracking a path-dependent speed profile. Unlike trajectory tracking, the path is not parameterized by time but rather by any other useful parameter that in some cases may be the path length. Thus, there is more flexibility in making the vehicle first converge to the path smoothly then move along it while tracking a given speed assignment....

An in-depth review of standard path-following methods in two dimensional space (2D) explaining in detail the theoretical principles of the different methods.

Furthermore, from the dynamics of the orientation error are given by

At this point, it should be clear that the geometric task in the path following problem, stated in Section 2.3, is equivalent to the problem of stabilizing the position error system, i.e. making ${\mathbf{e}_{\mathcal{P}}{(t)}}\rightarrow\mathbf{0}$ as $t\rightarrow\infty$. In what follows we will describe a number of path following methods available in the literature that solve this problem. These methods are categorized in Table 2. In *Methods 1* and *3*, the "*reference point*" is chosen as the orthogonal projection of the center of mass of the vehicle on the path, thus the *along-track* error ${s_{1}{(t)}} = 0$ for all $t$....

This frame was introduced in \[\] and used for the first time in the path following method of \[KPX^+^10\]. The P-T frame is based on the observation that, while the tangent vector for a given curve is unique, we may choose any convenient arbitrary normal vector so as to make it perpendicular to the tangent and vary smoothly throughout the path regardless of the curvature \[\].\
In 2D, a simple way to define the P-T frame is as follows. First, specify the tangent basic vector t as in. The second basic vector, called normal vector $\mathbf{n}_{1}$, is obtained by rotating the tangent vector $90$ degree clockwise....

### Scenario 3: fully or over-actuated vehicle

Should the vehicle achieve precise path following, both the vehicle and the point $P$ will move with the desired speed profile $U_{d}$, i.e. $u = u_{\mathcal{P}} = U_{d}$. In this case the dynamics task in is equivalent to requiring
