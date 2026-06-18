Sampling-based Model Predictive Control Leveraging Parallelizable Physics Simulations

Topics include Model predictive path integral control, Motion planning, Trajectory optimization, Graphics processing unit, Parallelized, Isaac, Gym, IsaacGym, Robotics, Simulation.

Uses IsaacGym as a simulator for forward dynamics propagation within an MPPI framework.

We present a method for sampling-based model predictive control that makes use of a generic physics simulator as the dynamical model. In particular, we propose a Model Predictive Path Integral controller (MPPI), that uses the GPU-parallelizable IsaacGym simulator to compute the forward dynamics of a problem. By doing so, we eliminate the need for explicit encoding of robot dynamics and contacts with objects for MPPI. Since no explicit dynamic modeling is required, our method is easily extendable to different objects and robots and allows one to solve complex navigation and contact-rich tasks. We demonstrate the effectiveness of this method in several simulated and real-world settings, among which mobile navigation with collision avoidance, non-prehensile manipulation, and whole-body control for high-dimensional configuration spaces. This method is a powerful and accessible open-source tool to solve a large variety of contact-rich motion planning tasks.

## Introduction

As robots become increasingly integrated into our daily lives, their ability to navigate and interact with the environment is becoming more important than ever. From collision avoidance to moving obstacles out of the way to pick up some objects, robots must be able to plan their motions while accounting for contact with their surroundings. At the same time, robotic platforms require many Degrees Of Freedom (DOF) to achieve agile and dexterous movements....

Figure 1: Scheme of the proposed method using IsaacGym as the dynamic model for MPPI. At each time step, IsaacGym is reset to the current world’s state x, and random input sequences V are applied for the horizon T, to every environment. MPPI uses the resulting rolled-out trajectories to approximate the optimal control u0* given a cost function C.

## Conclusions

We presented a way to perform Model Predictive Path Integral controller (MPPI) that uses a physics simulator as the dynamic model. By leveraging the GPU-parallelizable IsaacGym simulator for parallel sampling of forward trajectories, we have eliminated the need for explicit encoding of robot dynamics, contacts, and rigid-body interactions for MPPI. This makes our method easily adaptable to different objects and robots for a wide range of contact-rich motion-planning tasks....

### III-B Prehensile manipulation with whole-body control

### II-C1 Collision checking

We perform the same task as in \[\] and compare the final results of pushing a squared object on a table surface to two poses (Pose 1 and 2) with a robot arm equipped with a stick. In Table II, we report our findings, with our method showing double the accuracy. Our approach performs continuous pushes, unlike the baseline that stops for replanning after each short push. Thus, we complete either task in approximately 8 seconds, while the baseline takes approximately 4 minutes....

On the other hand, model-based approaches like Model Predictive Control (MPC) can solve challenging tasks \[\]. However, MPC often relies on constrained optimization, requiring constraint simplifications, precise modeling, and ad-hoc solutions to handle discontinuous dynamics in contact-rich tasks. While utilizing motion memory for warm-starting optimization can enhance performance, the above limitations still persist....
