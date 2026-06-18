Multi-Modal Model Predictive Path Integral Control for Collision Avoidance

Topics include Model predictive path integral control, Trajectory optimization, Collision avoidance, Multimodal, Sampling-based control.

Extends MPPI to handle multimodal trajectory distributions for collision avoidance, enabling the controller to simultaneously explore multiple qualitatively different trajectory groups (homotopy classes) rather than collapsing to a single mode.

This paper proposes a novel approach to motion planning and decision-making for automated vehicles, using a multi-modal Model Predictive Path Integral control algorithm. The method samples with Sobol sequences around the prior input and incorporates analytical solutions for collision avoidance. By leveraging multiple modes, the multi-modal control algorithm explores diverse trajectories, such as manoeuvring around obstacles or stopping safely before them, mitigating the risk of sub-optimal solutions. A non-linear single-track vehicle model with a Fiala tyre serves as the prediction model, and tyre force constraints within the friction circle are enforced to ensure vehicle stability during evasive manoeuvres. The optimised steering angle and longitudinal acceleration are computed to generate a collision-free trajectory and to control the vehicle.

## Introduction

The ability to design and select a safe trajectory during an evasive manoeuvre at high and low-friction conditions is a critical factor for the success of automated vehicles. Tyre nonlinearities, combined with the complexity of dynamic environments and the uncertainty of the road friction coefficient, make this problem particularly challenging. The complexity of motion planning also arises from the two interconnected tasks which must be addressed.

## Multi-Modal Model Predictive Path Integral Control

This section explains how the Multi-Modal MPPI is formulated and proposed.

## Model Predictive Path Integral Control

MPPI control is a sampling-based stochastic optimal control algorithm to solve a non-linear optimisation problem subject to non-linear dynamics and non-convex constraints. The MPPI utilises Monte Carlo sampling to explore a large number of control sequences, which are propagated through the discrete-time model $(f)$ over a finite time horizon, and the obtained state trajectories' performance is evaluated using a cost function $(J)$. The computed cost for state trajectories is used to weight each sampled control sequence (or rollout), forming a path integral estimate of the optimal control input.

where $\omega$ is the weight for each rollout $k \in {\lbrack 1,K\rbrack}$, $K$ is the total number of rollouts, $\eta$ is the normalization constant to ensure ${\sum_{k = 1}^{K}\omega_{k}} = 1$, $S_{k}$ is the trajectory cost for each rollout, and $\rho$ is the minimum cost $S_{k}$ which is used to avoids large exponents that could cause underflow. Regarding $\lambda$, it is the temperature parameter which regulates the selectivity of the weighting, a small $\lambda$ prioritises the lowest-cost trajectories, so it favours exploitation, vice versa, a large $\lambda$ favours exploration, flattening the cost rollouts.
