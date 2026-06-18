Analyzing the Variance of Policy Gradient Estimators for the Linear-Quadratic Regulator

Topics include Policy gradients.

We study the variance of the REINFORCE policy gradient estimator in environments with continuous state and action spaces, linear dynamics, quadratic cost, and Gaussian noise. These simple environments allow us to derive bounds on the estimator variance in terms of the environment and noise parameters. We compare the predictions of our bounds to the empirical variance in simulation experiments.

## Introduction

Policy gradient (PG) algorithms are widely used for reinforcement learning (RL) in continuous spaces. PG methods construct an unbiased estimate of the gradient of the RL objective with respect to the policy parameters. They do so without the complication of intermediate steps of dynamics modeling or value function approximation. However, the gradient estimate is known to suffer from high variance. This makes PG methods sample-inefficient with respect to environment interaction, creating an obstacle for applications to real physical systems.

In this paper, we seek a more detailed understanding of how the PG gradient estimate variance relates to properties of the continuous-space Markov decision process (MDP) that defines the RL problem instance. Such characterization is well-developed for discrete state spaces, but in continuous spaces, a detailed breakdown is not possible without further restrictions on the set of MDPs and the policy class. We choose to examine systems with linear dynamics, linear policy, quadratic cost, and Gaussian noise, known as LQR systems in control theory.

In this work, we derived bounds on the variance of the REINFORCE policy gradient estimator in the stochastic linear-quadratic control setting. Our upper bound is fully general, while our lower bound applies to the scalar case at a stationary point. The bounds match with respect to all system parameters except the time horizon $H$ and stability $\rho{({A + {BK}})}$. We compared our bound prediction to the empirical variance in a variety of experimental settings, finding a close qualitative match in the parameters for which the bounds are tight.

Our experiments in Section 4.1 plotting the empirical convergence rate of REINFORCE suggest that the effect of action noise $\Sigma_{a}$ on the overall RL performance is not fully captured by its effect on the variance. An interesting direction for future work would be to investigate the role of $\Sigma_{a}$ more closely and attempt to disentangle its effect on gradient magnitude, variance, exploration, and regularization. Such an analysis could lead to improved variance reduction methods or algorithms that manipulate $\Sigma_{a}$ to speed up the RL optimization.

For a special case of scalar states and actions, we also show a lower bound on ${\mathbb{E}}{\lbrack{\hat{g}}^{2}\rbrack}$....
