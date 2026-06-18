Fast Non-Episodic Adaptive Tuning of Robot Controllers with Online Policy Optimization

Topics include Reinforcement learning, Robotics, Aerial robotics, Online algorithms, Optimization, Control, Learning.

We study online algorithms to tune the parameters of a robot controller in a setting where the dynamics, policy class, and optimality objective are all time-varying. The system follows a single trajectory without episodes or state resets, and the time-varying information is not known in advance. Focusing on nonlinear geometric quadrotor controllers as a test case, we propose a practical implementation of a single-trajectory model-based online policy optimization algorithm, M-GAPS,along with reparameterizations of the quadrotor state space and policy class to improve the optimization landscape. In hardware experiments,we compare to model-based and model-free baselines that impose artificial episodes. We show that M-GAPS finds near-optimal parameters more quickly, especially when the episode length is not favorable. We also show that M-GAPS rapidly adapts to heavy unmodeled wind and payload disturbances, and achieves similar strong improvement on a 1:6-scale Ackermann-steered car....

## Introduction

We study the problem of optimizing a parameterized non-linear robot control policy in an online setting. A deployed robot may face unpredictable changes in both environment and task, and must adapt to them immediately. Therefore, we consider a protocol where the dynamics, policy class, and cost functions are all time-varying and revealed online: the optimization algorithm has no knowledge of how they will vary in the future. The algorithm is evaluated on a single trajectory without episodes or state resets. As a case study, we focus on nonlinear trajectory tracking control for quadrotors.

Policy optimization has been widely studied in the control and machine learning communities from varying perspectives. We are interested in methods that:

The requirement of a differentiable dynamics may limit the applicability of M-GAPS and DiffTune to systems with discontinuities, such as walking robots. Unstable behavior near discontinuities can degrade gradient-based optimization, even when the discontinuities form a set of measure zero \[\]. Further testing and development is needed on such systems.

The contractiveness required for the local regret guarantee of M-GAPS can be difficult to verify, and does not rule out the possibility of bad local minima. Similar to other applications of gradient-based nonconvex optimization, one must do empirical validation (like this work) before deploying M-GAPS in complex real-world robotic systems.

### IV-A Dynamics and Representation

Therefore, the ideal of OGD on the surrogate costs $F_{t}$ is not a practical algorithm. Instead, M-GAPS forms a computationally efficient approximation of ${\nabla F_{t}}{(\theta_{t})}$ with error small enough to yield optimal regret. M-GAPS computes the recursion as in ) *without* re-simulation, essentially "ignoring" the fact that $\theta_{t}$ is changing online. Specifically, it maintains an internal state $y_{t} \in {\mathbb{R}}^{n \times d}$ that approximates the sensitivity $\partial{x^{\theta_{t}}/{\partial\theta_{t}}}$, with the dynamics

## Quadrotor Experiments

Can be applied to general nonlinear dynamics and costs.

Optimize a given policy class (vs. prescribe their own).

Are adaptive -- do not rely on stationarity assumptions on the dynamics or costs.

Are efficient enough to run onboard a microcontroller.
