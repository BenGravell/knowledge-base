Recent Advances in Path Integral Control for Trajectory Optimization: An Overview in Theoretical and Algorithmic Perspectives

Topics include Model predictive path integral control, Path integral control, Survey, Trajectory optimization, Stochastic optimal control, Variational inference.

Survey paper reviewing the theoretical foundations and algorithmic advances in path integral control methods for trajectory optimization, covering MPPI variants, variational inference approaches, and connections to stochastic optimal control theory.

This paper presents a tutorial overview of path integral (PI) approaches for stochastic optimal control and trajectory optimization. We concisely summarize the theoretical development of path integral control to compute a solution for stochastic optimal control and provide algorithmic descriptions of the cross-entropy (CE) method, an open-loop controller using the receding horizon scheme known as the model predictive path integral (MPPI), and a parameterized state feedback controller based on the path integral control theory. We discuss policy search methods based on path integral control, efficient and stable sampling strategies, extensions to multi-agent decision-making, and MPPI for the trajectory optimization on manifolds. For tutorial demonstrations, some PI-based controllers are implemented in Python, MATLAB and ROS2/Gazebo simulations for trajectory optimization. The simulation frameworks and source codes are publicly available at

## Introduction

Trajectory optimization for motion or path planning is a fundamental problem in autonomous systems. Several requirements must be simultaneously considered for autonomous robot motion, path planning, navigation, and control. Examples include the specifications of mission objectives, examining the certifiable dynamical feasibility of a robot, ensuring collision avoidance, and considering the internal physical and communication constraints of autonomous robots.

In particular, generating an energy-efficient and collision-free safe trajectory is of the utmost importance during the process of autonomous vehicle driving, autonomous racing drone, unmanned aerial vehicles, electric vertical take-off and landing (eVTOL) urban air mobility (UAM), missile guidance, space vehicle control, and satellite attitude trajectory optimization

## Conclusions

In this paper, we present an overview of the fundamental theoretical developments and recent advances in path integral control with a focus on sampling-based stochastic trajectory optimization. The theoretical and algorithmic frameworks of several optimal control methods employing the path integral control framework are provided, and their similarities and differences are reviewed. Python, MATLAB and ROS2/Gazebo simulation results are provided to demonstrate the effectiveness of various path integral control methods....

Importance sampling The goal of importance sampling in MC techniques is to minimize the variance in the MC estimation of integration, ${{\mathbb{E}}_{\mathcal{Q}}{\lbrack{\ell{({\mathbf{X}})}}\rbrack}} = {{\mathbb{E}}_{\mathcal{P}}{\lbrack{\ell{({\mathbf{X}})}\frac{d\mathcal{Q}}{d\mathcal{P}}}\rbrack}}$. To reduce the variance, we want to find a probability measure $\mathcal{P}$ on $(\Omega,\mathcal{F})$ with which an unbiased MC estimate for $\rho$ is given by

The goal of stochastic optimal control for the dynamics and the cost-to-go is to determine an optimal policy that minimizes the expected cost-to-go with respect to the policy.

Simulations are performed in Python environments. Fig. 4 illustrates the controlled trajectories of the cart-pole system under various control strategies. Fig. 4 depicts the force inputs derived from the application of each control method....
