Dojo: A Differentiable Physics Engine for Robotics

Topics include Physics engines, Robot simulation, Differentiable optimization, Robotics, Trajectory optimization, System identification, Implicit differentiation.

Presents a differentiable rigid-body physics engine designed around stable contact simulation and analytic gradients. Dojo combines variational integration, cone-constrained contact modeling, and implicit differentiation so simulation can directly support planning, policy learning, and system identification.

We present Dojo, a differentiable physics engine for robotics that prioritizes stable simulation, accurate contact physics, and differentiability with respect to states, actions, and system parameters. Dojo models hard contact and friction with a nonlinear complementarity problem with second-order cone constraints. We introduce a custom primal-dual interior-point method to solve the second order cone program for stable forward simulation over a broad range of sample rates. We obtain smooth gradient approximations with this solver through the implicit function theorem, giving gradients that are useful for downstream trajectory optimization, policy optimization, and system identification applications. Specifically, we propose to use the central path parameter threshold in the interior point solver as a user-tunable design parameter. A high value gives a smooth approximation to contact dynamics with smooth gradients for optimization and learning, while a low value gives precise simulation rollouts with hard contact. We demonstrate Dojo's differentiability in trajectory optimization, policy learning, and system identification examples.

## Introduction

The last decade has seen immense advances in learning-based methods for policy optimization and trajectory optimization in robotics, e.g., for dexterous manipulation, quadrupedal locomotion, and pixels-to-torques control. These advances have largely hinged on innovations in learning architectures, large scale optimization algorithms, and large datasets. In contrast, there has been comparatively little work on the lowest level of the robotics reinforcement learning stack: the physics engine.

Physics engines that simulate rigid-body dynamics with contact are utilized for trajectory optimization, reinforcement learning, system identification, and dataset generation for domains ranging from locomotion to manipulation. To overcome the sim-to-real gap and to be of practical value in real-world applications, an engine should provide stable simulation, accurately reproduce a robot's dynamics, and ideally, be differentiable to enable the use of efficient gradient-based optimization methods.

In this work, we propose to further advance the state of the art by focusing on the underlying numerics of the physics engine, introducing features that can be adopted throughout the existing simulation ecosystem to improve performance in a variety of ways. We package these numerical improvements in a new simulation engine, Dojo, to highlight their favorable properties over exiting numerical techniques commonly used in physics simulators.

Specifically, we introduce two new contributions specific to Dojo: (i) We propose a custom primal-dual interior point solver for stably solving the complementary problem for forward simulation. This solver allows for low sample rates while maintaining stable and accurate contact simulation, thereby alleviating the *vanishing/exploding* gradient problem that appears when differentiating through high sample rate rollouts common in other differentiable simulators.

## Conclusion

Dojo is designed from physics- and optimization-first principles to enable better gradient-based optimization for planning, control, policy optimization, and system identification.
