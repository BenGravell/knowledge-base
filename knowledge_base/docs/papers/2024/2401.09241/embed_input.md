Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers

Topics include Model predictive path integral control, Trajectory optimization, Sampling-based control, Informed sampling, Ancillary controller.

Biased-MPPI augments the MPPI sampling distribution by biasing it toward trajectories suggested by one or more ancillary controllers (e.g., path-following or optimization-based), improving sample efficiency and trajectory quality while preserving the exploration benefits of random sampling.

Motion planning for autonomous robots in dynamic environments poses numerous challenges due to uncertainties in the robot's dynamics and interaction with other agents. Sampling-based MPC approaches, such as Model Predictive Path Integral (MPPI) control, have shown promise in addressing these complex motion planning problems. However, the performance of MPPI relies heavily on the choice of sampling distribution. Existing literature often uses the previously computed input sequence as the mean of a Gaussian distribution for sampling, leading to potential failures and local minima. In this paper, we propose a novel derivation of MPPI that allows for arbitrary sampling distributions to enhance efficiency, robustness, and convergence while alleviating the problem of local minima. We present an efficient importance sampling scheme that combines classical and learning-based ancillary controllers simultaneously, resulting in more informative sampling and control fusion. Several simulated and real-world demonstrate the validity of our approach.

## Introduction

Navigating autonomous robots through dense and dynamic environments poses a formidable challenge due to significant uncertainties, including the robot's state, model, environmental conditions, and interactions with other agents. Achieving desired behaviors under such conditions often necessitates using intricate cost functions and constraints, resulting in complex, nonlinear, non-convex, and occasionally discontinuous problem formulations. The dynamic nature of the environment introduces potential unexpected changes, demanding rapid adaptability in the robot's actions.

To address these challenges, one approach is to cast the problem in a stochastic optimal control setting, where they can be mathematically represented as stochastic Hamilton-Jacobi-Bellman (HJB) equations. However, solving these equations numerically can be challenging due to the curse of dimensionality. Pioneering work demonstrated that the stochastic HJB equations can be linearized for control-affine systems, and their solution can be approximated through sampling using the path integral formulation \[\]....

## Conclusions

In this paper, we have derived a sampling scheme for Model Predictive Path Integral (MPPI) control that removes computationally problematic terms and allows for the design of arbitrary sampling distributions as long as a bias in the solution is allowed. We proposed using classical and learning-based ancillary controllers for several control and motion planning experiments to bias the sampling distribution and achieve more efficient sampling and better performances. We demonstrated how the proposed algorithm can act as a control fusion scheme, taking suggestions from an arbitrary number of controllers and improving upon them....

### Linear Quadratic Integral (LQI)

There are several ways one could design an arbitrary sampling distribution. This paper focuses on taking most samples around a previously computed input distribution and some samples from hand-crafted policies.

### V-A1 Ancillary Controllers

Figure 1: Top: Usually, MPPI only takes samples around a previous plan. Here, the environment changes unexpectedly, and all the sampled trajectories are in collision, which leads to computing a new plan that also collides....
