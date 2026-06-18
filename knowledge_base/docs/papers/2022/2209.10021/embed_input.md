DiffTune: Auto-Tuning through Auto-Differentiation

Topics include Robotics, Aerial robotics, Graphs, Online algorithms, Optimization, Control, DiffTune.

The performance of robots in high-level tasks depends on the quality of their lower-level controller, which requires fine-tuning. However, the intrinsically nonlinear dynamics and controllers make tuning a challenging task when it is done by hand. In this paper, we present DiffTune, a novel, gradient-based automatic tuning framework. We formulate the controller tuning as a parameter optimization problem. Our method unrolls the dynamical system and controller as a computational graph and updates the controller parameters through gradient-based optimization. The gradient is obtained using sensitivity propagation, which is the only method for gradient computation when tuning for a physical system instead of its simulated counterpart. Furthermore, we use L_1 adaptive control to compensate for the uncertainties (that unavoidably exist in a physical system) such that the gradient is not biased by the unmodelled uncertainties. We validate the DiffTune on a Dubin's car and a quadrotor in challenging simulation environments....

## Introduction

Robotic systems are at the forefront of executing intricate tasks, relying on the prowess of their low-level controllers to deliver precise and agile motions. An optimal controller design starts with a meticulous analysis to ensure stability, followed by parameter tuning to achieve the intended performance on real-world robotic platforms. Traditionally, controller tuning is done either by hand using trial-and-error or proven methods for specific controllers (e.g., Ziegler--Nichols method for proportional-integral-derivative (PID) controller tuning \[\])....

Figure 1: Illustration of an unrolled dynamical system as a computational graph.

In this paper, we propose DiffTune: an auto-tuning method using auto-differentiation, with the advantage of stability, compatibility with data from physical systems, and efficiency. Given a performance metric, DiffTune gradually improves the performance using gradient descent, where the gradient is computed using sensitivity propagation that is compatible with physical systems' data. We also show how to use $\mathcal{L}_{1}$AC to mitigate the discrepancy between the nominal model and the associated physical system when the latter suffers from uncertainties....

One limitation of the proposed approach is that it only applies to systems with differentiable dynamics and controllers. The requirement on differentiability is not met in contact-rich applications \[\] (e.g., legged robots \[\] and dexterous manipulation \[\]) and systems with actuation limits \[\] (e.g., saturations in magnitude or changing rate). Although subgradients \[\] generally exist at the points of discontinuity, the impact of surrogate gradient on the tuning efficiency is unknown, which will be investigated in the future....

### Remark 4

The sensitivity propagation and forward-mode AD share the same formula as in and. The difference lies in what type of data is applied. Two types of data are considered: The first type is from simulation, where $\mathbf{x}_{k}$ is obtained by the computation $\mathbf{x}_{k} = {f{(\mathbf{x}_{k - 1},\mathbf{u}_{k - 1})}}$; the second type is sampled from a physical system, where $\mathbf{x}_{k}$ is obtained by either sensor measurements or state estimation, which cannot be represented as the evaluation a mathematical expression....

### V-B Quadrotor
