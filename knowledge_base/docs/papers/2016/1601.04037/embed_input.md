Funnel Libraries for Real-Time Robust Feedback Motion Planning

Topics include Convex optimization, Motion planning, Robotics, Aerial robotics, Vehicles, Safety, Robustness, Uncertainty, Real-time systems, Online algorithms, Optimization, Planning, Control.

We consider the problem of generating motion plans for a robot that are guaranteed to succeed despite uncertainty in the environment, parametric model uncertainty, and disturbances. Furthermore, we consider scenarios where these plans must be generated in real-time, because constraints such as obstacles in the environment may not be known until they are perceived (with a noisy sensor) at runtime. Our approach is to pre-compute a library of "funnels" along different maneuvers of the system that the state is guaranteed to remain within (despite bounded disturbances) when the feedback controller corresponding to the maneuver is executed. We leverage powerful computational machinery from convex optimization (sums-of-squares programming in particular) to compute these funnels. The resulting funnel library is then used to sequentially compose motion plans at runtime while ensuring the safety of the robot. A major advantage of the work presented here is that by explicitly taking into account the effect of uncertainty, the robot can evaluate motion plans based on how vulnerable they are to disturbances.

## Introduction

Imagine an unmanned aerial vehicle (UAV) flying at high speed through a cluttered environment in the presence of wind gusts, a legged robot traversing rough terrain, or a mobile robot grasping and manipulating previously unlocalized objects in the environment. These applications demand that the robot move through (and in certain cases interact with) its environment with a very high degree of agility while still being in close proximity to obstacles. Such systems today lack guarantees on their safety and can fail dramatically in the face of uncertainty in their environment and dynamics.

The tasks mentioned above are characterized by three main challenges. First, the dynamics of the system are nonlinear, underactuated, and subject to constraints on the input (e.g. torque limits). Second, there is a significant amount of uncertainty in the dynamics of the system due to disturbances and modeling error. Finally, the geometry of the environment that the robot is operating in is unknown until runtime, thus forcing the robot to plan in *real-time*.

## Contributions

(a) A plane deviating from its nominal planned trajectory due to a heavy cross-wind.

## Discussion and Conclusion

In this paper we have presented an approach for real-time motion planning in a priori unknown environments with dynamic uncertainty in the form of bounded parametric model uncertainty and external disturbances. The method augments the traditional trajectory library approach by constructing stabilizing controllers around the nominal trajectories in a library and computing outer approximations of reachable sets ( funnels ) for the resulting closed-loop controllers via sums-of-squares (SOS) programming.

We have demonstrated our approach using extensive simulation experiments on a ground vehicle model. These experiments demonstrate that our approach can afford significant advantages over a trajectory-based approach. We also applied our approach to a quadrotor model and demonstrated how for certain classes of environments we can guarantee that the system will fly forever in a collision-free manner. We have also validated our approach using thorough hardware experiments on a small fixed-wing airplane flying through previously unseen cluttered environments at high speeds.
