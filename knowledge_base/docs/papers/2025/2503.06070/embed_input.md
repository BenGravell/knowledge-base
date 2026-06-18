Natural Gradient Descent for Control

This paper bridges optimization and control, and presents a novel closed-loop control framework based on natural gradient descent, offering a trajectory-oriented alternative to traditional cost-function tuning. By leveraging the Fisher Information Matrix, we formulate a preconditioned gradient descent update that explicitly shapes system trajectories. We show that, in sharp contrast to traditional controllers, our approach provides flexibility to shape the system's low-level behavior. To this end, the proposed method parameterizes closed-loop dynamics in terms of stationary covariance and an unknown cost function, providing a geometric interpretation of control adjustments. We establish theoretical stability conditions. The simulation results on a rotary inverted pendulum benchmark highlight the advantages of natural gradient descent in trajectory shaping.

## Introduction

Optimization techniques, particularly gradient descent (GD) and its numerous variants (Ruder Laborde and Oberman Rattray et al. Martens, ), have become fundamental in modern control and machine learning. These methods are broadly classified into two categories when applied to control systems: GD-based control, where gradient methods optimize controller parameters, and controlled GD, where control-theoretic tools improve the convergence properties of a gradient-based optimizer (Lessard et al. Padmanabhan and Seiler Nayyer et al., ).

In our previous work, we proposed a fundamentally different perspective by directly shaping system trajectories through a gradient-descent-like closed-loop approach. We introduced a novel parameterization of the stable closed-loop dynamics

This trajectory-oriented perspective offers several advantages. Firstly, it provides explicit trajectory control. The gradient formulation provides direct control over the trajectory shape, eliminating the need for trial-and-error cost function tuning. Secondly, it quantifies robustness by the step size. For a small step size, closed-loop eigenvalues have small variations. Lastly, it unifies with a Linear Quadratic Regulator (LQR). We established theoretical connections between our approach and classical optimal control, showing that LQR solutions can be naturally represented in this setting.

## Discussion

Stability conditions ensure the existence of a Lyapunov function that decreases along system trajectories, guaranteeing stability. However, these conditions do not necessarily provide an explicit mechanism for *shaping* the trajectories themselves. In contrast, our framework leverages a GD-like formulation to directly influence how the state evolves at each step, thereby offering more transparency over closed-loop behavior.

Classical LQR designs the gain matrix by minimizing a quadratic cost function, but there is no straightforward, systematic way to target specific *transient* behaviors beyond fine-tuning the weighting matrices $Q$ and $R$. The proposed natural GD approach, on the other hand, utilizes a step-size parameter $\alpha$ and a preconditioning (covariance) matrix $\Sigma$ to shape the trajectory explicitly.
