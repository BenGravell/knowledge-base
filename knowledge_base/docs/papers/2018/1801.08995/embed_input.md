Trajectory Generation Using Sharpness Continuous Dubins-like Paths with Applications in Control of Heavy Duty Vehicles

Topics include Path generation, Dubins, Curvature continuity, Sharpness, Trajectory generation, Heavy vehicles, Autonomous driving, Steering constraints.

Proposes sharpness-continuous (G3) path primitives composed of cubic curvature curves, circular arcs, and straight lines. Closely related to and builds upon ”Trajectory generation for car-like robots using cubic curvature polynomials” by Nagy and Kelly and ”From Reeds and Shepp's to continuous-curvature paths” by Fraichard and Scheuer.

We present a trajectory generation framework for control of wheeled vehicles under steering actuator constraints. The motivation is smooth autonomous driving of heavy vehicles. The key idea is to take into account rate, and additionally, torque limitations of the steering actuator directly. Previous methods only take into account curvature rate limitations, which deal indirectly with steering rate limitations. We propose the new concept of Sharpness Continuous curves, which uses cubic and sigmoid curvature trajectories together with circular arcs to steer the vehicle. The obtained trajectories are characterized by a smooth and continuously differentiable steering angle profile. These trajectories provide low-level controllers with reference signals which are easier to track, resulting in improved performance. The smoothness of the obtained steering profiles also results in increased passenger comfort. The method is characterized by a fast computation time, which can be further speeded up through the use of simple pre-computations. We detail possible path planning applications of the method, and conduct simulations that show its advantages and real time capabilities.

## Introduction

### Background and Motivation

Path planning deals with the generation of paths or trajectories (paths with an associated time law) for a vehicle. The generated paths/trajectories are used as a reference signal for the controllers implemented in the vehicle. Planning methods for autonomous vehicles have come a long way from the initial problem of finding collision free paths, being now focused on properties such as kinodynamic constraints, optimality, and uncertainty,. Car-like vehicles must follow specific patterns of motion defined by their kinematic constraints....

Controllers could also be designed so that they take advantage of the smooth properties of the path, without requiring the computational burden of more complex control approaches that are design to withstand lower quality paths.

This work can also be extended into time optimal trajectory planning. The velocity profile could be optimized, such that the vehicle performs the path in minimum time and obeys steering constraints. Moreover, different curvature profiles could be optimized with respect to time, and abiding by the steering constraints.

As seen before, the possible set of departure configurations of an SC turn are located in a circle, and its orientations differ from the circle tangent by $\mu$. Thus, to connect two SC turns, we need a way to connect two circles $\Omega_{s}$ and $\Omega_{f}$ with arbitrary centers, radii, and $\mu$ values.

### Sharpness Continuous Turns

In order to have a feasible path, we need to ensure that a vehicle can follow it while complying with its steering constraints. If we make both $\kappa_{i}$ and $\kappa_{f}$ smaller in magnitude than $\kappa_{\max}$, we ensure that the path always has a steering angle magnitude smaller than $\phi_{\max}$.

Much research effort has been devoted to the field of $\mathbf{G}^{3}$ path planning. A $\mathbf{G}^{3}$ path is characterized by a continuously differentiable curvature profile. $\mathbf{G}^{3}$ paths are important as they avoid jerky motion and wheel slippage, simplifying the tracking task and improving controller performance. $\mathbf{G}^{3}$ path planning is analogous to the $\mathbf{G}^{3}$ interpolation problem with applications often related to Computer-Aided Design. Some authors have focused on its applications to autonomous mobile robots.
