Sampling-based Model Predictive Control Leveraging Parallelizable Physics Simulations

Topics include Model predictive path integral control, Motion planning, Trajectory optimization, Graphics processing unit, Parallelized, Isaac, Gym, IsaacGym, Robotics, Simulation.

Uses IsaacGym as a simulator for forward dynamics propagation within an MPPI framework.

We present a method for sampling-based model predictive control that makes use of a generic physics simulator as the dynamical model. In particular, we propose a Model Predictive Path Integral controller (MPPI), that uses the GPU-parallelizable IsaacGym simulator to compute the forward dynamics of a problem. By doing so, we eliminate the need for explicit encoding of robot dynamics and contacts with objects for MPPI. Since no explicit dynamic modeling is required, our method is easily extendable to different objects and robots and allows one to solve complex navigation and contact-rich tasks. We demonstrate the effectiveness of this method in several simulated and real-world settings, among which mobile navigation with collision avoidance, non-prehensile manipulation, and whole-body control for high-dimensional configuration spaces. This method is a powerful and accessible open-source tool to solve a large variety of contact-rich motion planning tasks.

## Introduction

As robots become increasingly integrated into our daily lives, their ability to navigate and interact with the environment is becoming more important than ever. From collision avoidance to moving obstacles out of the way to pick up some objects, robots must be able to plan their motions while accounting for contact with their surroundings. At the same time, robotic platforms require many Degrees Of Freedom (DOF) to achieve agile and dexterous movements.

On the other hand, model-based approaches like Model Predictive Control (MPC) can solve challenging tasks. However, MPC often relies on constrained optimization, requiring constraint simplifications, precise modeling, and ad-hoc solutions to handle discontinuous dynamics in contact-rich tasks. While utilizing motion memory for warm-starting optimization can enhance performance, the above limitations still persist.

In this paper, we propose a training-free model-based framework for real-time control of complex systems, where one designs only a cost function, not the problem's dynamics and contact models. We introduce the idea of using a general GPU-parallelizable physics simulator, IsaacGym, as the dynamic model for MPPI. This creates a robust framework that generalizes to various tasks. An overview is given in Fig. 1.

## I-A Related work

This section provides an overview of selected works focusing on motion planning and contact-rich tasks in robotics. Motion planning pipelines are categorized as global and local motion planning. Local motion planning encompasses approaches like operational space control, geometric methods such as Riemannian Motion Policies and Optimization Fabrics, and receding-horizon optimization formulations like Model Predictive Control (MPC) that may incorporate learned components. Most MPC algorithms rely on constrained optimization and assume smooth dynamics.

## Discussion

In this section, we discuss key aspects and potential future work related to our solution. First, the computational demands of planning and control with our method can be high when extending the time horizon to several seconds. To keep the time horizon limited for real-time control while preventing being trapped in local minima, future work should incorporate global planning techniques such as A\*, RRT, and Probabilistic Roadmaps (PRM) to guide the local planner.
