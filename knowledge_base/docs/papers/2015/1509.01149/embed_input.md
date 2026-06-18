Model Predictive Path Integral Control Using Covariance Variable Importance Sampling

Folds importance sampling into the cost function in order to address the practical issue of infrequent selection of low-cost trajectories under naive sampling of actions on the uncontrolled system, which is a known drawback of MPPI. Also discusses implementation of MPPI on a GPU for massively parallel sampling. Includes a clear description of MPPI in Algorithm 1.

In this paper we develop a Model Predictive Path Integral (MPPI) control algorithm based on a generalized importance sampling scheme and perform parallel optimization via sampling using a Graphics Processing Unit (GPU). The proposed generalized importance sampling scheme allows for changes in the drift and diffusion terms of stochastic diffusion processes and plays a significant role in the performance of the model predictive control algorithm. We compare the proposed algorithm in simulation with a model predictive control version of differential dynamic programming.

## INTRODUCTION

The path integral optimal control framework provides a mathematically sound methodology for developing optimal control algorithms based on stochastic sampling of trajectories. The key idea in this framework is that the value function for the optimal control problem is transformed using the Feynman-Kac lemma into an expectation over all possible trajectories, which is known as a path integral. This transformation allows stochastic optimal control problems to be solved with a Monte-Carlo approximation using forward sampling of stochastic diffusion processes.

There have been a variety of algorithms developed in the path integral control setting. The most straight-forward application of path integral control is when the iterative feedback control law suggested in is implemented in its open loop formulation. This requires that sampling takes place only from the initial state of the optimal control problem. A more effective approach is to use the path integral control framework to find the parameters of a feedback control policy. This can be done by sampling in policy parameter space, these methods are known as Policy Improvement with Path Integrals....

The derivation of the likelihood ratio enables the designer of the algorithm to tune the exploration variance in the path integral control framework, whereas previous methods have only allowed for the mean of the distribution to be changed. Tuning the exploration variance is critical in achieving a high level of performance since the natural variance of the system is typically too low to achieve good performance.

The experiments considered in this work only consider changing the variance by a constant multiple times the natural variance of the system. In this special case the introduction of the likelihood ratio corresponds to adding in a control cost when evaluating the cost-to-go of a trajectory. A direction for future research is to investigate how to automatically adjust the variance online. Doing so could enable the algorithm to switch from aggressively exploring the state space when performing aggressive maneuvers to exploring more conservatively for performing very precise maneuvers.

Now we expand out the first quadratic term to get:

And we can then write this as an expectation with respect to $\mathsf{q}$:

## MODEL PREDICTIVE CONTROL ALGORITHM
