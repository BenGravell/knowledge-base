Contraction L1-Adaptive Control Using Gaussian Processes

Topics include Aerial robotics, Safety, Gaussian processes, Bayesian methods, Regression, Control, Learning, GP.

We present CL_1-GP, a control framework that enables safe simultaneous learning and control for systems subject to uncertainties. The two main constituents are contraction theory-based L_1 (CL_1) control and Bayesian learning in the form of Gaussian process (GP) regression. The CL_1 controller ensures that control objectives are met while providing safety certificates. Furthermore, CL_1-GP incorporates any available data into a GP model of uncertainties, which improves performance and enables the motion planner to achieve optimality safely. This way, the safe operation of the system is always guaranteed, even during the learning transients. We provide a few illustrative examples for the safe learning and control of planar quadrotor systems in a variety of environments.

## Introduction

A majority of planning algorithms based on model predictive control (MPC) and model-based reinforcement learning (MBRL) compute optimal control sequences using a nominal or learned system model. However, models have inaccuracies and the robot may behave sub-optimally. In the worst cases, the system will become unstable or collide with obstacles. These model inaccuracies have especially serious consequences for safety-critical systems. Machine learning (ML) algorithms have been proven to be potent tools for learning complex and accurate models in robotics, improving performance....

Control-theoretic approaches that offer safety certificates based on Lyapunov functions and robust control invariant sets are gaining popularity in the context of safe robot learning. Many recent safe-learning examples establish the notion of asymptotic stability with control-theoretic tools \[16, Chapter 3\]. Although critically important, asymptotic stability by itself is not sufficient for the safe operation of robots. Safety must be guaranteed during the learning process with transient bounds. Techniques like uncertainty propagation have been proposed to characterize transient performance using learned statistical models....

## Conclusion

In this work, we have presented the $\mathcal{C}\mathcal{L}_{1}$-$\mathcal{G}\mathcal{P}$ framework, which enables safe simultaneous learning and control. The safety of the method is certified by the tracking error bounds produced by the ancillary $\mathcal{C}\mathcal{L}_{1}$ controller. The learning is performed using Gaussian process regression. The learned Gaussian process model can be used to generate high probability uniform error bounds, which are incorporated into the controller to improve the tracking error bounds. Future work will extend the architecture to leverage the tracking error bounds in the path planning phase....

Furthermore, the state $x{(t)}$ is uniformly ultimately bounded as

Using the linearity of the differential operator, we can also compute the posterior distributions of the partial derivatives of $h{(\xi,x)}$ using the previously defined data in. The posterior distributions of the partial derivatives are given by

where $k_{c,\hat{F}}$ is defined via the analytic solution of the following QP:

### Our Contributions
