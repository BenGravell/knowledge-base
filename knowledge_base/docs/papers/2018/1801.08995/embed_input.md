Trajectory Generation Using Sharpness Continuous Dubins-like Paths with Applications in Control of Heavy Duty Vehicles

Topics include Path generation, Dubins, Curvature continuity, Sharpness, Trajectory generation, Heavy vehicles, Autonomous driving, Steering constraints.

Proposes sharpness-continuous (G3) path primitives composed of cubic curvature curves, circular arcs, and straight lines. Closely related to and builds upon ”Trajectory generation for car-like robots using cubic curvature polynomials” by Nagy and Kelly and ”From Reeds and Shepp's to continuous-curvature paths” by Fraichard and Scheuer.

We present a trajectory generation framework for control of wheeled vehicles under steering actuator constraints. The motivation is smooth autonomous driving of heavy vehicles. The key idea is to take into account rate, and additionally, torque limitations of the steering actuator directly. Previous methods only take into account curvature rate limitations, which deal indirectly with steering rate limitations. We propose the new concept of Sharpness Continuous curves, which uses cubic and sigmoid curvature trajectories together with circular arcs to steer the vehicle. The obtained trajectories are characterized by a smooth and continuously differentiable steering angle profile. These trajectories provide low-level controllers with reference signals which are easier to track, resulting in improved performance. The smoothness of the obtained steering profiles also results in increased passenger comfort. The method is characterized by a fast computation time, which can be further speeded up through the use of simple pre-computations. We detail possible path planning applications of the method, and conduct simulations that show its advantages and real time capabilities.

## Main Contributions

The

Directly take into account steering actuator magnitude, rate, and acceleration limitations, generating $\mathbf{G}^{3}$ paths;

Ease the controller task and improve passenger comfort;

Can connect arbitrary vehicle configurations;

## Introduction

Cubic curvature paths are defined as paths with a cubic curvature profile ${\kappa{(s)}} = {{a_{3}s^{3}} + {a_{2}s^{2}} + {a_{1}s} + a_{0}}$, where $s$ is the length along the path. A cubic curvature profile is the minimum degree polynomial that allows to define arbitrary initial and final curvatures, $\kappa_{i}$ and $\kappa_{f}$, and sharpnesses $\alpha_{i}$ and $\alpha_{f}$.

In

where $s_{f}$ is the path length, and is itself an unknown.
