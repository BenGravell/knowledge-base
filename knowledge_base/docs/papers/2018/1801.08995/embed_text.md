## Introduction

### Background and Motivation

Path planning deals with the generation of paths or trajectories (paths with an associated time law) for a vehicle. The generated paths/trajectories are used as a reference signal for the controllers implemented in the vehicle. Planning methods for autonomous vehicles have come a long way from the initial problem of finding collision free paths, being now focused on properties such as kinodynamic constraints, optimality, and uncertainty,. Car-like vehicles must follow specific patterns of motion defined by their kinematic constraints. These constraints introduce an additional difficulty, as they limit the maneuverability of the vehicle, resulting in limited types of paths that are admissible, i.e., can be feasibly followed. Heavy-duty vehicles introduce additional constraints due to their slow actuator dynamics. Thus planning methods for autonomous vehicles must be adapted, in order to deal with the additional control challenges imposed by heavy-duty vehicles.

Much research effort has been devoted to the field of $\mathbf{G}^{3}$ path planning. A $\mathbf{G}^{3}$ path is characterized by a continuously differentiable curvature profile. $\mathbf{G}^{3}$ paths are important as they avoid jerky motion and wheel slippage, simplifying the tracking task and improving controller performance. $\mathbf{G}^{3}$ path planning is analogous to the $\mathbf{G}^{3}$ interpolation problem with applications often related to Computer-Aided Design. Some authors have focused on its applications to autonomous mobile robots.

Path planning for autonomous vehicles introduces additional demands. Besides the $\mathbf{G}^{3}$ property, another important property of a path is its length. Shorter paths are desirable as they result in more efficient driving.

Steering methods are a class of path planners that are able to efficiently compute a path between vehicle states in an environment without obstacles. Even though the majority of autonomous vehicle applications considers obstacles, steering methods still prove to be useful, as they are often used as components of more complex path planners which can take obstacles into account --.

Dubins and Reeds-Shepp paths are steering methods that connect two arbitrary vehicle poses through a minimal length path. However, these paths have discontinuous curvatures, thus not being $\mathbf{G}^{3}$. makes use of clothoidal paths to generate near length optimal curvature continuous paths. Clothoids are an obvious choice, since they have long been used in road design, as they allow for smooth driving. However, the curvature derivative is discontinuous, resulting in paths that are not $\mathbf{G}^{3}$. extends, so that $\mathbf{G}^{3}$ paths with near optimal length are planned. This last method deals with limitations of the path curvature and curvature derivative, which are not directly related to the steering actuator limitations of the vehicle.

### Main Contributions

The contribution of this work comes from the generation of vehicle trajectories that: Directly take into account steering actuator magnitude, rate, and acceleration limitations, generating $\mathbf{G}^{3}$ paths; Ease the controller task and improve passenger comfort; Can connect arbitrary vehicle configurations; Have fast computation times.

We build upon the work of, replacing clothoids with cubic curvature paths. Additionally, we formulate the constraints so that we can limit the actual steering angle rate and steering angle acceleration of the vehicle, instead of the curvature derivative of the path, as done in previous approaches,. This is because the maximum steering angle rate and acceleration are more intuitive constraints that can be directly obtained from the vehicle actuator limitations. The proposed method is also computationally fast and can be used online, as part of a more complex motion planner.

### Outline

Section 2 funded by the Knut and Alice Wallenberg Foundation") introduces the vehicle model used and defines the problem we address. Section 3 funded by the Knut and Alice Wallenberg Foundation") presents Sharpness Continuous paths used to solve the stated problem. Section 4 funded by the Knut and Alice Wallenberg Foundation") presents Cubic Curvature paths, a building block of Sharpness Continuous paths. Section 5 funded by the Knut and Alice Wallenberg Foundation") illustrates our simulation results, showing the performance of the method. Conclusions and future work are presented in Section 6 funded by the Knut and Alice Wallenberg Foundation").

## Problem Statement

### Vehicle Model

We start by defining the vehicle model as: $(x,y)$ represents the location of the vehicle rear wheel axle center, $\theta$ its orientation and $v$ is the vehicle velocity. The curvature $\kappa$ of a vehicle with wheelbase length $L$ is related to its steering angle $\phi$ through A vehicle pose is defined by the three variables $(x,y,\theta)$. If an additional curvature is associated to a pose we obtain a configuration, defined as $(x,y,\theta,\kappa)$.

The steering angle of the vehicle is set by an actuator, which like any real system has physical limitations. The limitations with which we comply in this work are: Maximum steering angle amplitude $\phi_{\max}$, Maximum steering angle rate of change ${\overset{˙}{\phi}}_{\max}$, Maximum steering actuation acceleration ${\overset{¨}{\phi}}_{\max}$.

These limitations effectively affect the vehicle motion capabilities and should be dealt with when generating paths.

### Path Feasibility

Path feasibility depends on the capabilities of the vehicle that executes it and on the path itself. The limited steering angle amplitude $\phi_{\max}$ imposes a maximum allowed curvature on the path $\kappa_{\max}$. This limitation is addressed by generating paths which have a curvature profile ${|\kappa|} \leq \kappa_{\max}$. Limited steering angle rate of change ${\overset{˙}{\phi}}_{\max}$ can be tackled by limiting the curvature derivative of the generated paths.

In this paper, we deal with the third limitation, related to the limited steering angle acceleration ${\overset{¨}{\phi}}_{\max}$. Having a limited ${\overset{¨}{\phi}}_{\max}$ results in $\overset{˙}{\phi}$ being a continuous function, which in turn indicates that $\phi$ is a continuously differentiable, $\mathbf{C}^{\mathbf{1}}$ function. The paths generated by have corresponding $\overset{˙}{\phi}$ profiles with discontinuities, that require an infinite ${\overset{¨}{\phi}}_{\max}$. This is impossible to achieve by an actuator, and motivates the usage of paths with a $\mathbf{C}^{\mathbf{1}}$ steering profile.

The steering profile is related to the curvature profile through (1 funded by the Knut and Alice Wallenberg Foundation")). The sharpness $\alpha$ is defined as the change of curvature along the path length $s$: By ensuring sharpness continuity in a path, we guarantee that the curvature, and the steering profile of such a path is $\mathbf{C}^{\mathbf{1}}$, i.e., the path is $\mathbf{G}^{3}$. A vehicle is thus able to follow the path using a bounded steering acceleration ${\overset{¨}{\phi}}_{\max}$.

In the following section, we detail how to generate paths that respect all three limitations previously stated.

## Sharpness Continuous Paths

In this section we present the Sharpness Continuous (SC) paths. 3.1 funded by the Knut and Alice Wallenberg Foundation") introduces the principle behind SC paths. SC paths are composed of SC turns (detailed in 3.2 funded by the Knut and Alice Wallenberg Foundation")) connected over a line segment. The process of connecting SC turns over a line segment to form a continuous SC path is detailed in 3.3 funded by the Knut and Alice Wallenberg Foundation"). When generating an SC path there is a total of 16 possible combinations of different SC turns that can be used. 3.4 funded by the Knut and Alice Wallenberg Foundation") indicates how to choose the best combination.

### Principle

use a combination of arc circle turns and/or line segments to connect two arbitrary poses. In, this idea is extended with Curvature Continuous (CC) turns, which replace arc circles by a combination of clothoid and arc circles. We extend this further, replacing the clothoid segments by cubic curvature paths, achieving sharpness continuity and respecting the limited steering acceleration ${\overset{¨}{\phi}}_{\max}$.

### Sharpness Continuous Turns

Figure 1: Sharpness continuous turn general case.

We propose Sharpness Continuous (SC) turns, which consist of three segments, an initial cubic curvature path $\Gamma_{1,2}$, a circular arc $\Gamma_{2,3}$, and a final cubic curvature path $\Gamma_{3,4}$. Figure 1 funded by the Knut and Alice Wallenberg Foundation") shows an example of an SC turn. The initial segment $\Gamma_{1,2}$ starts at a configuration $\mathbf{q}_{1} = {(x_{1},y_{1},\theta_{1},\kappa_{1})}$ and ends with maximum curvature, $\pm \kappa_{\max}$, at a configuration $\mathbf{q}_{2} = {(x_{2},y_{2},\theta_{2},\kappa_{2})}$. The second segment is a circular arc $\Gamma_{2,3}$ with radius $\kappa_{\max}^{- 1}$ and arbitrary arc length, starting at $\mathbf{q}_{2}$ and ending at $\mathbf{q}_{3} = {(x_{3},y_{3},\theta_{3},\kappa_{3})}$. The SC turn is completed with a path $\Gamma_{3,4}$, with starting curvature $\pm \kappa_{\max}$ and ending at a configuration $\mathbf{q}_{4} = {(x_{4},y_{4},\theta_{4},\kappa_{4})}$.

We assume, without loss of generality, that the vehicle, and subsequently the path, starts at a configuration $\mathbf{q}_{1} = {}$. From $\mathbf{q}_{1}$, it then follows the path $\Gamma_{1,2}$ taking it to a configuration $\mathbf{q}_{2} = {(x_{2},y_{2},\theta_{2},\kappa_{\max})}$. The path $\Gamma_{1,2}$ has initial and final curvatures $0$ and $\kappa_{\max}$, respectively. The values $x_{2}$, $y_{2}$, and $\theta_{2}$ are those that result from following the curvature profile of $\Gamma_{1,2}$ with a starting vehicle state $\mathbf{q}_{1}$.

Once the vehicle has a curvature $\kappa_{\max}$, it then follows a circular arc path $\Gamma_{2,3}$ with radius $\kappa_{\max}^{- 1}$. The circular arc starts at $(x_{2},y_{2})$ and has its center at a distance $\kappa_{\max}^{- 1}$ perpendicular to the orientation $\theta_{2}$ at point $(x_{2},y_{2})$. Its center is given by The last path segment $\Gamma_{3,4}$ departs from the circular arc and it brings the vehicle to a configuration $\mathbf{q}_{4}$. Configuration $\mathbf{q}_{4}$ depends on the point of departure from the circular arc, $\mathbf{q}_{3}$. However, it always lies in a circle $\Omega$, which has the same center as the circular arc $(x_{\Omega},y_{\Omega})$ in (2 funded by the Knut and Alice Wallenberg Foundation")).

In order to find the radius of circle $\Omega$, we first assume an auxiliary circular arc to be centered at ${(x_{\Omega'},y_{\Omega'})} = {(0,\kappa_{\max}^{- 1})}$. We assume a departure configuration from the circle at $(0,0,0,\kappa_{\max})$. Then, by following the path given by a curvature profile with initial and final curvatures $\kappa_{\max}$ and $\kappa_{4}$, we will end at a configuration $\text{q}_{4} = {(x_{4},y_{4},\theta_{4},\kappa_{4})}$. $\text{q}_{4}$ is a configuration located at an auxiliary $\Omega'$ circle (the auxiliary equivalent of the $\Omega$ circle), that has the same center as the circular arc. Thus we compute the radius of $\Omega'$, which is equal to the radius of $\Omega$, as An additional angle $\mu$ is defined as the difference between $\theta_{4}$ and the tangential angle to $\Omega$ at configuration $\mathbf{q}_{4}$. It is computed using the previous auxiliary circular arc as Thus, given a certain initial configuration $\mathbf{q}_{1}$, the possible positions of the ending configuration $\mathbf{q}_{4}$, resulting from a combination of a cubic curvature path, a circular arc, and another cubic curvature path, i.e., an SC turn, lie on a circle $\Omega$. The possible $\theta_{4}$ orientations of these configurations are given by the tangential angle at the circle plus $\mu$.

### Connecting Sharpness Continuous Turns

An SC path between start and goal configurations $\mathbf{q}_{s}$ and $\mathbf{q}_{g}$ can be found by connecting two SC turns. An SC path consists of three elements: an SC turn starting at the start configuration $\mathbf{q}_{s}$ and ending at a configuration $\mathbf{q}_{a}$ with null curvature, a line segment starting at $\mathbf{q}_{a}$ and ending at $\mathbf{q}_{b}$, an SC turn starting at configuration $\mathbf{q}_{b}$ with null curvature, and ending at the goal configuration $\mathbf{q}_{g}$.

Figure 2 funded by the Knut and Alice Wallenberg Foundation") shows an example of an SC path, with the three elements described above.

Figure 2: Sharpness continuous path example. The path consists of an SC turn between qs and qa, a line segment from qa to qb, and an SC turn between qb and qg. The dashed circles correspond to the SC turns that can span from qa and qb.

In order to connect two SC turns, we need to find the configurations $\mathbf{q}_{a}$ and $\mathbf{q}_{b}$ that belong to the starting and ending SC turn possible departure configurations, and that can be connected with a line segment. That is, $\mathbf{q}_{a}$ and $\mathbf{q}_{b}$ must have the same orientation, i.e., $\theta_{a} = \theta_{b}$. Furthermore both must lie on a line segment with an inclination angle $\theta_{a}$.

As seen before, the possible set of departure configurations of an SC turn are located in a circle, and its orientations differ from the circle tangent by $\mu$. Thus, to connect two SC turns, we need a way to connect two circles $\Omega_{s}$ and $\Omega_{f}$ with arbitrary centers, radii, and $\mu$ values.

Figure 3: Computing the external (top) and internal (bottom) tangents between two circles.

We first assume two auxiliary circles $\Omega_{a}$ and $\Omega_{b}$, as depicted in Figure 3 funded by the Knut and Alice Wallenberg Foundation") (top). $\Omega_{a}$ and $\Omega_{b}$ have the same radii and $\mu$ values as the original circles $\Omega_{s}$ and $\Omega_{f}$. $\Omega_{a}$ is centered at $$ and $\Omega_{b}$ is located so that $\mathbf{q}_{a}$ and $\mathbf{q}_{b}$ are collinear. We are interested in finding the center of $\Omega_{b} = {(x_{\Omega_{b}},y_{\Omega_{b}})}$. From Figure 3 funded by the Knut and Alice Wallenberg Foundation") (top) it can be seen that We assume that the distance $r{(\Omega_{a},\Omega_{b})}$ between the circle centers is the same as the distance between the original circles $r{(\Omega_{s},\Omega_{f})}$. We then have We know that $\mathbf{q}_{a} = {({r_{a}{\sin\mu_{a}}},{- {r_{a}{\cos\mu_{a}}}},0,0)}$, and that $\mathbf{q}_{b} = {({x_{\Omega_{b}} - {r_{b}{\sin\mu_{b}}}},{y_{\Omega_{b}} - {r_{b}{\cos\mu_{b}}}},0,0)}$. To find these configurations in the original circles $\Omega_{s}$ and $\Omega_{f}$, we need to first apply a rotation $\Delta_{\theta} = {\arctan{({y_{\Omega_{f}} - y_{\Omega_{s}}},{x_{\Omega_{f}} - x_{\Omega_{s}}})}}$ to $\mathbf{q}_{a}$ and $\mathbf{q}_{b}$. We then translate these configurations by ${(\Delta_{x},\Delta_{y})} = {(x_{\Omega_{s}},y_{\Omega_{s}})}$. The resulting rotated and translated configurations correspond to the desired tangent configurations between the circles $\Omega_{s}$ and $\Omega_{f}$.

The above procedure finds the departure configurations between two counter clockwise (left steering) SC turns, shown in Figure 3 funded by the Knut and Alice Wallenberg Foundation") (top). An analogous procedure can be used to find the possible departure configurations between any combination of clockwise (right steering) and counter clockwise turns, as shown in Figure 3 funded by the Knut and Alice Wallenberg Foundation") (bottom). This procedures are valid if the found tangent configurations $\mathbf{q}_{a}$ and $\mathbf{q}_{b}$ do not lie inside the circles $\Omega_{b}$ and $\Omega_{a}$, respectively.

### Finding the Shortest SC Path

In order to find the shortest SC path between two configurations $\mathbf{q}_{s}$ and $\mathbf{q}_{g}$, we need to compute all the possible SC turns that can be spanned from these configurations. The SC turns are then connected, in order to generate possible SC paths. The process is detailed below.

Each of the configurations $\mathbf{q}_{s}$ and $\mathbf{q}_{g}$ can span a total of four SC turns, depending if the vehicle is moving forwards or backwards, or if it is turning left or right. The possible SC turns that span from $\mathbf{q}_{s}$ and $\mathbf{q}_{g}$ are shown in Figure 2 funded by the Knut and Alice Wallenberg Foundation") as dashed circles (forward and backward SC turns are equivalent, so they lie on top of each other). Figure 1 funded by the Knut and Alice Wallenberg Foundation") shows an SC turn which assumes a vehicle moving forward and turning left. The method explained in section 3.2 funded by the Knut and Alice Wallenberg Foundation") can be readily used to obtain SC turns moving forward, independent of the direction they are turning. The procedure to obtain an SC turn moving backwards is analogous.

There are a total of 16 possible SC paths between the two sets of 4 SC turns spanned from $\mathbf{q}_{s}$ and $\mathbf{q}_{g}$. Each path is found by computing the SC path, resulting from connecting two SC turns, as detailed in 3.3 funded by the Knut and Alice Wallenberg Foundation"). Each SC path length is evaluated, and the shortest is selected as the solution.

## Cubic Curvature Paths

Cubic curvature paths are a building block of an SC turn. They are used as transition paths connecting configurations to and from an arc circle (paths $\Gamma_{1,2}$ and $\Gamma_{3,4}$ in 3.2 funded by the Knut and Alice Wallenberg Foundation")), and they guarantee the sharpness continuity of the whole path.

### Introduction

Cubic curvature paths are defined as paths with a cubic curvature profile ${\kappa{(s)}} = {{a_{3}s^{3}} + {a_{2}s^{2}} + {a_{1}s} + a_{0}}$, where $s$ is the length along the path. A cubic curvature profile is the minimum degree polynomial that allows to define arbitrary initial and final curvatures, $\kappa_{i}$ and $\kappa_{f}$, and sharpnesses $\alpha_{i}$ and $\alpha_{f}$. The sharpness profile of these paths is given: In order to find the parameters of the cubic polynomial, we use the initial and final constraints: where $s_{f}$ is the path length, and is itself an unknown.

We want to ensure sharpness continuity, so we need to set the initial and final sharpness values, $\alpha_{i}$ and $\alpha_{f}$, to zero. This allows us to stitch together cubic curvature paths with line and arc segments, which have null sharpness, while ensuring sharpness continuity. It should be noted that (7 funded by the Knut and Alice Wallenberg Foundation")) does not take into account steering limitations, thus, infeasible paths can be generated. In the following we address this issue.

### Ensuring Steering Rate and Acceleration Constraints

In order to have a feasible path, we need to ensure that a vehicle can follow it while complying with its steering constraints. If we make both $\kappa_{i}$ and $\kappa_{f}$ smaller in magnitude than $\kappa_{\max}$, we ensure that the path always has a steering angle magnitude smaller than $\phi_{\max}$.

The steering angle profile corresponding to the cubic curvature path is first computed from the path curvature using (1 funded by the Knut and Alice Wallenberg Foundation")). Assuming then that the vehicle is following the path at a given fixed velocity $\mathbf{v}$, the steering angle rate and acceleration profiles are computed. Both profiles have a peak magnitude rate ${\overset{˙}{\phi}}_{peak}$ and acceleration ${\overset{¨}{\phi}}_{peak}$. In case ${\overset{˙}{\phi}}_{peak}$ is larger than the allowed maximum steering rate ${\overset{˙}{\phi}}_{\max}$ the length $s_{f}$ needs to be increased so that ${\overset{˙}{\phi}}_{peak} = {\overset{˙}{\phi}}_{\max}$. This can be achieved by simply scaling the path length by ${\overset{˙}{\phi}}_{peak}/{\overset{˙}{\phi}}_{\max}$. Similarly if ${\overset{¨}{\phi}}_{peak} > {\overset{¨}{\phi}}_{\max}$, we scale the path length by a scaling factor of $\sqrt{({{\overset{¨}{\phi}}_{peak}/{\overset{¨}{\phi}}_{\max}})}$. To guarantee that the path respects both steering rate and acceleration limitations, we need to scale its length by the greater of the scaling factors. Once the new path length $s_{f}$ is computed, the cubic curvature path is recomputed, by solving (7 funded by the Knut and Alice Wallenberg Foundation")).

## Results

### Convergence of SC Paths to Dubins Paths

As previously mentioned, Dubins paths are proven to be optimal in terms of length. SC paths are, however, longer than the Dubins path. This happens because SC turns have longer turning radii than a circular arc with radius $\kappa_{\max}^{- 1}$.

Figure 4 funded by the Knut and Alice Wallenberg Foundation") shows the Dubins path for a given start and goal configurations $\mathbf{q}_{s}$ and $\mathbf{q}_{g}$. Overlayed are SC paths with different maximum sharpness $\alpha_{\max}$ for the same configurations $\mathbf{q}_{s}$ and $\mathbf{q}_{g}$. It is seen that the greater the maximum sharpness $\alpha_{\max}$ of the SC paths is, i.e., the greater the achievable steering rate and accelerations of the vehicle, the closer it approaches the Dubins path. This is somewhat intuitive, as increasing $\alpha_{\max}$ results in increasing the rate of change of the curvature profile. If $\alpha_{\max}\rightarrow\infty$, then the curvature changes would be immediate, and the SC path would be equivalent to the Dubins path, and as such, length optimal.

Figure 4: SC paths with increasing sharpness α converge to the length optimal Dubins path.

### Notes on Computational Cost

As previously mentioned, given two configurations $\mathbf{q}_{s}$ and $\mathbf{q}_{g}$, the SC method computes all possible 16 SC turns and how they can be connected. The connection process, as detailed in section 3.3 funded by the Knut and Alice Wallenberg Foundation"), is computationally cheap. The bulk of processing comes from finding all 16 possible SC turns.

As seen in section 3.2 funded by the Knut and Alice Wallenberg Foundation"), an SC turn depends on the cubic curvature paths that are part of it. In order to evaluate these paths, one has to generate their curvature profiles from the given initial and final constraints. To comply with the steering constraints, a numerical evaluation of a steering profile must be done, in order to find the path length scaling factors, as detailed in section 4.2 funded by the Knut and Alice Wallenberg Foundation"). When one has the desired curvature profile, the orientations $\theta$ can be obtained analytically. The $x$ and $y$ positions of the path are found by solving the vehicle model equations, using an Euler method, which has a high computational cost. This cost can be greatly reduced using precomputations, as detailed in the following.

### Precomputation of Cubic Curvature Paths

As previously stated, the SC method computation speed is limited by the generation of the cubic curvature paths. Depending on the application, some assumptions can be made that greatly improve the computation speed, by allowing the precomputation of the cubic curvature paths to be used.

If one assumes that the start and end configurations $\mathbf{q}_{s}$ and $\mathbf{q}_{g}$ always have null curvatures, then one can compute, in an initialization procedure, all the possible cubic curvature paths starting and ending at curvatures $\kappa = {0,{\pm \kappa_{\max}}}$. Thus we skip the expensive generation of cubic curvature paths needed to find out the possible SC turns. In order to generate an SC turn, one just has to use the precomputed paths and apply rotations and translations on them.

The precomputation of paths can still be achieved, without limiting the start and goal configurations $\mathbf{q}_{s}$ and $\mathbf{q}_{g}$ to have null curvature. In fact, one can allow $\mathbf{q}_{s}$ and $\mathbf{q}_{g}$ to have curvature values belonging to finite discrete set.

### Timing Evaluation

We test the steering method, measuring its computational speed for several problem instances. The method is implemented in C++ and running on a Linux Mint distribution. The computer used is equipped with an Intel Core i7-6820HQ Processor running at 2.70 GHz, and with 16,0 GB of RAM.

We generate 1000 random pairs of start and goal configuration queries. Each query is repeated 100 times to get a better estimate of the average computational time. The start and goal configurations of each query are generated by sampling the $x$ and $y$ coordinates from a uniform random distribution between $- 50$ and $50$. The orientations sampled from the interval $\lbrack{- \pi},\pi\rbrack$, and the curvatures from a discrete equispaced set of 11 curvatures $\lbrack{- \kappa_{\max}},\ldots,0,\ldots,\kappa_{\max}\rbrack$.

When making use of precomputations, we get an average time for finding a solution path of $70{µs}$, while without precomputations we get an average time of $12{ms}$. The precomputations greatly decrease the computational time. These results indicate that the steering method is extremely inexpensive when using precomputations. Even without precomputations, the method runs in few milliseconds, making it suitable for real-time applications.

### Simulations

A simulation test is run in order to understand how the proposed paths affect the performance of a vehicle tracking them. A kinematic vehicle model coupled with a detailed steering actuator model are used to simulate a vehicle.

In the test, two paths consisting of a straight segment, a turn, and a straight segment are generated. The first path is a CC path, while the second is our proposed SC path. Both paths abide by the same maximum steering angle magnitude $\phi_{\max}$ and steering angle rate ${\overset{˙}{\phi}}_{\max}$ constraints. Additionally, the SC path respects also the steering angle acceleration ${\overset{¨}{\phi}}_{\max}$ constraint, unlike the CC paths.

The simulation assumes a steering actuator that is limited in terms of achievable steering angle magnitude, rate, and acceleration. The steering angle is controlled making use of a PID controller, which receives a steering angle reference, and actuates on the steering angle torque. The PID controller was tuned to achieve a step response with a relatively fast settling time and little overshoot. The steering angle reference is provided from a high-level path tracking controller. The high-level controller consists of a feedforward part and a feedback part. The feedforward part is obtained by finding the closest path point, and getting the corresponding steering angle reference at that point. The feedback part is a proportional controller regulating both lateral and heading errors. Such a controller is a simple implementation commonly used in path tracking applications.

Figure 5 funded by the Knut and Alice Wallenberg Foundation") shows the steering reference profiles of the paths to be tracked. The difference between them is in the shape of the increasing and decreasing sections of the steering angle. In the CC case, the steering angle change follows a linear profile while in the SC it follows a cubic profile.

Figure 5: Steering reference profiles used in simulation.

Figure 6 funded by the Knut and Alice Wallenberg Foundation") shows the lateral and heading errors when the vehicle tracks both paths. The vehicle is initially placed at the start of the path, and it follows the first straight segment perfectly. However, when the turning section starts, a deviation from the path begins to arise. The feedback part is then responsible for trying to regulate the errors to zero. Shortly after the turn begins, the CC case becomes unstable. On the other hand, the SC case is stable, and its error converges to zero. The error profiles show that the controller performance is worse when tracking CC paths.

Figure 6: Lateral error when tracking a CC and an SC path. When tracking the CC path, the controller becomes unstable, resulting in an error that grows indefinitely, and out of scope of the graph. The SC path tracking is seen to be stable.

The lateral acceleration and jerk (acceleration rate) experienced by the vehicle are related to passenger comfort. Figure 7 funded by the Knut and Alice Wallenberg Foundation") shows the lateral accelerations for a vehicle following the reference steering profiles without feedback actuation. It is seen that the CC path has large jerk values, which result from an aggressive steering actuation. The SC path steering profile achieves smoother lateral acceleration profiles.

Figure 7: Lateral acceleration when tracking a path without feedback, i.e., using only feedforward references.

## Conclusions

This paper presented the concept of SC paths. SC paths respect not only the maximum steering angle constraints, but also maximum steering rate and acceleration constraints. These properties ease the low-level controller task and introduce an higher degree of smoothness, improving the driving comfort and reducing actuator effort. This is of importance when dealing with heavy-duty vehicles, which are characterized by slow actuator dynamics.

As future work, one could extend this approach so that the SC paths handle more cases besides that of a combination of two SC turns connected by a line segment. This would allow to connect configurations that lie close together.

Controllers could also be designed so that they take advantage of the smooth properties of the path, without requiring the computational burden of more complex control approaches that are design to withstand lower quality paths.

This work can also be extended into time optimal trajectory planning. The velocity profile could be optimized, such that the vehicle performs the path in minimum time and obeys steering constraints. Moreover, different curvature profiles could be optimized with respect to time, and abiding by the steering constraints.
