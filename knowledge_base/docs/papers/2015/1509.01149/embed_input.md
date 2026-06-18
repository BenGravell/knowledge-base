Model Predictive Path Integral Control Using Covariance Variable Importance Sampling

Folds importance sampling into the cost function in order to address the practical issue of infrequent selection of low-cost trajectories under naive sampling of actions on the uncontrolled system, which is a known drawback of MPPI. Also discusses implementation of MPPI on a GPU for massively parallel sampling. Includes a clear description of MPPI in Algorithm 1.

In this paper we develop a Model Predictive Path Integral (MPPI) control algorithm based on a generalized importance sampling scheme and perform parallel optimization via sampling using a Graphics Processing Unit (GPU). The proposed generalized importance sampling scheme allows for changes in the drift and diffusion terms of stochastic diffusion processes and plays a significant role in the performance of the model predictive control algorithm. We compare the proposed algorithm in simulation with a model predictive control version of differential dynamic programming.

## INTRODUCTION

The path integral optimal control framework provides a mathematically sound methodology for developing optimal control algorithms based on stochastic sampling of trajectories. The key idea in this framework is that the value function for the optimal control problem is transformed using the Feynman-Kac lemma into an expectation over all possible trajectories, which is known as a path integral. This transformation allows stochastic optimal control problems to be solved with a Monte-Carlo approximation using forward sampling of stochastic diffusion processes.

There have been a variety of algorithms developed in the path integral control setting. The most straight-forward application of path integral control is when the iterative feedback control law suggested in is implemented in its open loop formulation. This requires that sampling takes place only from the initial state of the optimal control problem. A more effective approach is to use the path integral control framework to find the parameters of a feedback control policy. This can be done by sampling in policy parameter space, these methods are known as Policy Improvement with Path Integrals.

The approach we take here generalizes these approaches in that it enables for both the mean and variance of the sampling distribution to be changed by the control designer, without violating the underlying assumptions made in the path integral derivation. This enables the algorithm to converge fast enough that it can be applied in a model predictive control setting. After deriving the model predictive path integral control (MPPI) algorithm, we compare it with an existing model predictive control formulation based on differential dynamic programming (DDP).

## CONCLUSION

In this paper we have developed a model predictive path integral control algorithm which is able to outperform a state-of-the-art DDP method on two difficult control tasks. The algorithm is based on stochastic sampling of system trajectories and requires no derivatives of either the dynamics or costs of the system. This enables the algorithm to naturally take into account non-linear dynamics, such as a non-linear tire model.

The derivation of the generalized likelihood ratio between discrete time diffusion processes.
