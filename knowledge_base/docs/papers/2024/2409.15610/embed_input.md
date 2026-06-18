Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing

Topics include Trajectory optimization, Model predictive path integral control, Diffusion, Locomotion, Model predictive control, Annealing.

Takes a perspective of treating MPPI as a single step of a denoising diffusion process, and generalizes this process to a multi-step diffusion-style annealing process. DIAL-MPC starts optimizing the control sequence with smooth but inaccurate objectives and gradually shifts to more accurate local objectives.

Due to high dimensionality and non-convexity, real-time optimal control using full-order dynamics models for legged robots is challenging. Therefore, Nonlinear Model Predictive Control (NMPC) approaches are often limited to reduced-order models. Sampling-based MPC has shown potential in nonconvex even discontinuous problems, but often yields suboptimal solutions with high variance, which limits its applications in high-dimensional locomotion. This work introduces DIAL-MPC (Diffusion-Inspired Annealing for Legged MPC), a sampling-based MPC framework with a novel diffusion-style annealing process. Such an annealing process is supported by the theoretical landscape analysis of Model Predictive Path Integral Control (MPPI) and the connection between MPPI and single-step diffusion. Algorithmically, DIAL-MPC iteratively refines solutions online and achieves both global coverage and local convergence. In quadrupedal torque-level control tasks, DIAL-MPC reduces the tracking error of standard MPPI by 13.4 times and outperforms reinforcement learning (RL) policies by 50% in challenging climbing tasks without any training.

## INTRODUCTION

Legged robots have demonstrated great potential in navigating through complex environments thanks to their agility and mobility \[parkHighspeedBoundingMIT2017, kimHighlyDynamicQuadruped2019, herdtOnlineWalkingMotion2010, khazoomTailoringSolutionAccuracy2024, koenemannWholebodyModelpredictiveControl2015, neunertWholeBodyNonlinearModel2018\]. However, the online control of articulated legged systems remains challenging because of their high-dimensional, underactuated and contact-rich nature, leads to non-convex and non-smooth optimization landscapes.

In this paper, we address these challenges by unveiling the intrinsic connection between sampling-based MPC and diffusion processes. Following the key iterative refinement idea of the diffusion model, we introduce a novel sampling-based MPC method, Diffusion-Inspired Annealing for Legged Model Predictive Control (DIAL-MPC). DIAL-MPC optimizes control sequences iteratively in a dual-loop manner. Specifically, DIAL-MPC starts optimizing the control sequence with smooth but inaccurate objectives and gradually shifts to more accurate local objectives.

Compared with MPPI, DIAL-MPC enables on-the-fly, full-order torque-level locomotion control by effectively balancing global coverage and local convergence. We evaluate DIAL-MPC on a quadrupedal robot with full-order dynamics and show that it can achieve real-time 50Hz control with both robustness and efficiency. As a training-free and purely online method, DIAL-MPC enables precise jumping with payload and outperforms RL methods.

Novel Diffusion-Inspired Annealing Framework: We propose a diffusion-inspired annealing framework for sampling-based MPC by revealing the connection between sampling-based MPC and diffusion processes.

## CONCLUSION

This work presents DIAL-MPC, a sampling-based MPC method with a diffusion-inspired annealing process to balance coverage and convergence in real-world legged locomotion. DIAL-MPC can solve the full-order control problem efficiently with the help of diffusion process and is generalizable to various tasks and dynamics in a training-free manner. One limitation is that DIAL-MPC requires fast simulation to generate samples, which limits the application of DIAL-MPC in longer planning horizon tasks.
