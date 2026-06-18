Model-Predictive Control via Cross-Entropy and Gradient-Based Optimization

Topics include Trajectory optimization, Model predictive control, Cross-entropy method, Gradient-based optimization, Sampling-based control.

Combines CEM-style action sampling with gradient descent refinement. Quite similar in spirit to Sampled DDP (SaDDP), but uses first-order (gradient) refinement instead of second-order (Hessian), and stays closer to vanilla CEM.

Recent works in high-dimensional model-predictive control and model-based reinforcement learning with learned dynamics and reward models have resorted to population-based optimization methods, such as the Cross-Entropy Method (CEM), for planning a sequence of actions. To decide on an action to take, CEM conducts a search for the action sequence with the highest return according to the dynamics model and reward. Action sequences are typically randomly sampled from an unconditional Gaussian distribution and evaluated on the environment. This distribution is iteratively updated towards action sequences with higher returns. However, this planning method can be very inefficient, especially for high-dimensional action spaces. An alternative line of approaches optimize action sequences directly via gradient descent, but are prone to local optima. We propose a method to solve this planning problem by interleaving CEM and gradient descent steps in optimizing the action sequence. Our experiments show faster convergence of the proposed hybrid approach, even for high-dimensional action spaces, avoidance of local minima, and better or equal performance to CEM....

## Introduction

High-dimensional, nonlinear Model-Predictive Control (MPC) and Model-Based Reinforcement Learning (MBRL) have seen significant progress over the last years, the task being to first learn a dynamics and a reward model of the environment and then plan using the learned models. While a number of recent approaches \[Hafner et al.Hafner, Lillicrap, Fischer, Villegas, Ha, Lee, and Davidson, Sharma et al.Sharma, Gu, Levine, Kumar, and Hausman, Chua et al.Chua, Calandra, McAllister, and Levine, Wang and Ba\] have developed efficient techniques for learning these models in MBRL, fewer papers \[Amos and Yarats, Srinivas et al.Srinivas, Jabri,...

Many current MBRL approaches do not leverage gradients through the model, which are cheaply available, and resort to inefficient optimization, particularly in high dimensions, whereas gradient-based planning converges faster.

## Conclusion

In this paper we investigate the problem of planning and optimization in model predictive control and in the context of model-based reinforcement learning. We address the scaling problems of the widely-used, but gradient-free, Cross-Entropy Method, which struggles as the dimensionality of the environment increases. This is an important issue as we scale these methods to real world control problems. On the other hand, gradient-descent-based planning is conveniently applicable to high-dimensional continuous control problems, especially since the learned dynamics models are typically parameterized by differentiable functions....

To consider the planning problem in isolation, we created a toy environment in which we have access to ground truth gradients through the dynamics model. The agent controls a mass in an N dimensional space by applying forces at each time step. Fig. 2 shows a 2D projection of the environment. The task is to move towards high reward regions of the state-space (red region) from the blue region. The black lines and dots show 2D projections of multiple rolled out trajectories starting from the origin. The fluorescent green region denotes an obstacle with soft contact....

Here, $t$ indexes the CEM iterations. Now, treating these initial sampled plans as initialization of the gradient-descent procedure, we perform $J$ steps of gradient descent on all of the sequences. In all of our experiments to ensure fair comparison to CEM, we set $J = 1$.
