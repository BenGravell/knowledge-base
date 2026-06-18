Model-Predictive Control via Cross-Entropy and Gradient-Based Optimization

Topics include Trajectory optimization, Model predictive control, Cross-entropy method, Gradient-based optimization, Sampling-based control.

Combines CEM-style action sampling with gradient descent refinement. Quite similar in spirit to Sampled DDP (SaDDP), but uses first-order (gradient) refinement instead of second-order (Hessian), and stays closer to vanilla CEM.

Recent works in high-dimensional model-predictive control and model-based reinforcement learning with learned dynamics and reward models have resorted to population-based optimization methods, such as the Cross-Entropy Method (CEM), for planning a sequence of actions. To decide on an action to take, CEM conducts a search for the action sequence with the highest return according to the dynamics model and reward. Action sequences are typically randomly sampled from an unconditional Gaussian distribution and evaluated on the environment. This distribution is iteratively updated towards action sequences with higher returns. However, this planning method can be very inefficient, especially for high-dimensional action spaces. An alternative line of approaches optimize action sequences directly via gradient descent, but are prone to local optima. We propose a method to solve this planning problem by interleaving CEM and gradient descent steps in optimizing the action sequence. Our experiments show faster convergence of the proposed hybrid approach, even for high-dimensional action spaces, avoidance of local minima, and better or equal performance to CEM.

## Introduction

High-dimensional, nonlinear Model-Predictive Control (MPC) and Model-Based Reinforcement Learning (MBRL) have seen significant progress over the last years, the task being to first learn a dynamics and a reward model of the environment and then plan using the learned models.

Many current MBRL approaches do not leverage gradients through the model, which are cheaply available, and resort to inefficient optimization, particularly in high dimensions, whereas gradient-based planning converges faster.

In this paper we combine the two methods, to take advantage of the convergence speed of gradient-based planning and the broader search, multi-extremum optimization performed by CEM. Gradient based optimization is one of the main approaches for a number of high-dimensional non-convex optimization problems in machine learning, yet it has not been widely adopted in planning problems due to the issue of vanishing or exploding gradients.

## Limitations and Future Works

One of the main directions for future works is to investigate the implications of model-bias in the planning scheme. In MBRL, one of the primary issues leading to a suboptimal plan is that the planner exploits model bias of an imperfectly learned model \[Wang et al.Wang, Bao, Clavera, Hoang, Wen, Langlois, Zhang, Zhang, Abbeel, and Ba\]. So, for better planning, we also need to develop better strategies for learning the dynamics model itself.

Another effective direction for tackling model-bias is by learning dynamics models conditioned on some latent variables, instead of trying to learn a global dynamics model. A recent paper, DADS \[Sharma et al.Sharma, Gu, Levine, Kumar, and Hausman\] does this by conditioning the dynamics model on latent 'skills' and the main idea is to learn smaller behavior-specific dynamics models instead of trying to learn a global dynamics model. The latent 'skills' are basically an abstraction for the low-level action sequences that get executed in the environment.
