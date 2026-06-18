Dojo: A Differentiable Physics Engine for Robotics

Topics include Physics engines, Robot simulation, Differentiable optimization, Robotics, Trajectory optimization, System identification, Implicit differentiation.

Presents a differentiable rigid-body physics engine designed around stable contact simulation and analytic gradients. Dojo combines variational integration, cone-constrained contact modeling, and implicit differentiation so simulation can directly support planning, policy learning, and system identification.

We present Dojo, a differentiable physics engine for robotics that prioritizes stable simulation, accurate contact physics, and differentiability with respect to states, actions, and system parameters. Dojo models hard contact and friction with a nonlinear complementarity problem with second-order cone constraints. We introduce a custom primal-dual interior-point method to solve the second order cone program for stable forward simulation over a broad range of sample rates. We obtain smooth gradient approximations with this solver through the implicit function theorem, giving gradients that are useful for downstream trajectory optimization, policy optimization, and system identification applications. Specifically, we propose to use the central path parameter threshold in the interior point solver as a user-tunable design parameter. A high value gives a smooth approximation to contact dynamics with smooth gradients for optimization and learning, while a low value gives precise simulation rollouts with hard contact. We demonstrate Dojo's differentiability in trajectory optimization, policy learning, and system identification examples....

## Introduction

The last decade has seen immense advances in learning-based methods for policy optimization and trajectory optimization in robotics, e.g., for dexterous manipulation, quadrupedal locomotion, and pixels-to-torques control \[\]. These advances have largely hinged on innovations in learning architectures, large scale optimization algorithms, and large datasets. In contrast, there has been comparatively little work on the lowest level of the robotics reinforcement learning stack: the physics engine....

Physics engines that simulate rigid-body dynamics with contact are utilized for trajectory optimization, reinforcement learning, system identification, and dataset generation for domains ranging from locomotion to manipulation. To overcome the sim-to-real gap \[\] and to be of practical value in real-world applications, an engine should provide stable simulation, accurately reproduce a robot's dynamics, and ideally, be differentiable to enable the use of efficient gradient-based optimization methods.

Perhaps the most important remaining question is whether the physics and optimization improvements from this work translate into better transfer of simulation results to successes on real-world robotic hardware. In this thrust, future work will explore the transfer of control policies trained in Dojo to hardware and deployment of the engine in model predictive control frameworks.

In conclusion, we have presented a new physics engine, Dojo, specifically designed for robotics. This tool is the culmination of a number of improvements to the contact dynamics model and underlying optimization routines, aiming to advance state-of-the-art physics engines for robotics by improving physical accuracy and differentiability.

TABLE II: Contact violation for Atlas drop (Fig. 1). Comparison between Dojo and MuJoCo for foot contact penetration (millimeters) with the floor for different time steps (seconds). Dojo strictly enforces no penetration. When Atlas lands, its feet remains above the ground by an infinitesimal amount. In contrast, MuJoCo exhibits significant penetration through the floor (i.e., negative values).

where $F:{{\mathbf{Z} \times \mathbf{Z} \times \mathbf{Z} \times \mathbf{J}}\rightarrow\mathbf{R}^{6N}}$. In order to simulate the system we find $z_{+}$ and $j$ that satisfy for a provided $z_{-}$ and $z$ using Newton's method.
