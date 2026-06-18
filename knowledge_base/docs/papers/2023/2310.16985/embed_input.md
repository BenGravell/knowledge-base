TinyMPC: Model-Predictive Control on Resource-Constrained Microcontrollers

Model-predictive control (MPC) is a powerful tool for controlling highly dynamic robotic systems subject to complex constraints. However, MPC is computationally demanding, and is often impractical to implement on small, resource-constrained robotic platforms. We present TinyMPC, a high-speed MPC solver with a low memory footprint targeting the microcontrollers common on small robots. Our approach is based on the alternating direction method of multipliers (ADMM) and leverages the structure of the MPC problem for efficiency. We demonstrate TinyMPC's effectiveness by benchmarking against the state-of-the-art solver OSQP, achieving nearly an order of magnitude speed increase, as well as through hardware experiments on a 27 gram quadrotor, demonstrating high-speed trajectory tracking and dynamic obstacle avoidance. TinyMPC is publicly available at

## Introduction

Model-predictive control (MPC) enables reactive and dynamic online control for robots while respecting complex control and state constraints such as those encountered during dynamic obstacle avoidance and contact events. However, despite MPC's many successes, its practical application is often hindered by computational limitations, which can necessitate algorithmic simplifications. This challenge is amplified when dealing with systems that have fast or unstable open-loop dynamics, where high control rates are needed for safe and effective operation.

At the same time, there has been an explosion of interest in tiny, low-cost robots that can operate in confined spaces, making them a promising solution for applications ranging from emergency search and rescue to routine monitoring and maintenance of infrastructure and equipment. These robots are limited to low-power, resource-constrained microcontrollers (MCUs) for their computation....

We introduce TinyMPC, a model-predictive control solver for resource-constrained embedded systems. TinyMPC uses ADMM to handle state and input constraints while leveraging the structure of the MPC problem and insights from LQR to reduce memory footprint and speed up online execution compared to existing state-of-the-art solvers like OSQP. We demonstrated TinyMPC's practical performance on a Crazyflie nano-quadrotor performing highly dynamic tasks with input and obstacle constraints.

Several directions for future work remain: It should be straight-forward to extend TinyMPC to handle second-order cone constraints, which are useful in many MPC applications for modeling thrust and friction cone constraints. We also plan to further reduce TinyMPC's hardware requirements by developing a fixed-point version, since many small microcontrollers lack hardware floating-point support. Finally, to ease deployment, we plan to develop a code-generation wrapper for TinyMPC in a high-level language like Julia or Python, similar to OSQP and CVXGEN.

We leverage a scaled form of by introducing the scaled dual variables $y$ and $g$:

The alternating direction method of multipliers (ADMM) is a popular and efficient approach for solving convex optimization problems, including QPs like. We provide a very brief summary here and refer readers to for more details.
