AcroMonk: A Minimalist Underactuated Brachiating Robot

Topics include Reinforcement learning, Trajectory optimization, Robotics, Robustness, Uncertainty, Optimization, Control, Learning, AcroMonk, TVLQR, Model-free proportional derivative, PD, Linear quadratic regulator.

Brachiation is a dynamic, coordinated swinging maneuver of body and arms used by monkeys and apes to move between branches. As a unique underactuated mode of locomotion, it is interesting to study from a robotics perspective since it can broaden the deployment scenarios for humanoids and animaloids. While several brachiating robots of varying complexity have been proposed in the past, this paper presents the simplest possible prototype of a brachiation robot, using only a single actuator and unactuated grippers. The novel passive gripper design allows it to snap on and release from monkey bars, while guaranteeing well defined start and end poses of the swing. The brachiation behavior is realized in three different ways, using trajectory optimization via direct collocation and stabilization by a model-based time-varying linear quadratic regulator (TVLQR) or model-free proportional derivative (PD) control, as well as by a reinforcement learning (RL) based control policy. The three control schemes are compared in terms of robustness to disturbances, mass uncertainty, and energy consumption. The system design and controllers have been open-sourced....

## Introduction

Brachiation is a complex dynamic maneuver involving a continuous swing motion and a discontinuity when switching the support arm. Apes brachiate with ease through unstructured environments with flexible or rigid handholds at variable distances, making this motion challenging and interesting to study for roboticists. Brachiating robots can be beneficial for inspection, agriculture, search and rescue applications, etc., since they can perform agile movements in hard to traverse terrains. Hence, there has been extensive research on brachiation robots in the past three decades.

Figure 1: Monkey inspired brachiation with AcroMonk

## Conclusion

With AcroMonk, we present a novel canonical underactuated system for studying brachiation. Due to the grooved gripper design, it is easily and reliably controllable, making it the first system of such a low complexity to achieve multiple consecutive brachiation motions. The readily available components and straightforward assembly make it a suitable reference system for underactuated robotics research. Our future work will focus on the following issues. Despite some success, we were not yet able to produce reliable backward brachiation....

where the final cost term includes minimization of total trajectory time $T$ with weight $W$, and the running costs include a state regularization cost $\mathbf{x}^{T}{\mathbf{Q}\mathbf{x}}$ with $\mathbf{Q} = \mathbf{Q}^{T} \succeq 0$ and an effort regularization cost $u^{T}Ru$ with $\mathbf{R} = \mathbf{R}^{T} \succ 0$. The set of constraints include first order ODE (2b) form of system dynamics given by, state and effort limits (2c), initial and final values of the state (2d), and collision avoidance constraints (2e) where $\mathbf{p}$ is the current position of the end-effector (EE) obtained via forward kinematics and...

Considering a system that comprises the robot and bars, we denote three fixed points as Z (single support, hanging), B (double support with swing arm on backward bar), and F (double support with swing arm on forward bar). The four atomic sub-behaviors are transitions between these fixed points, i.e. Zero-to-Back (ZB), Zero-to-Front (ZF), Front-to-Back (FB), and Back-to-Front (BF)....
