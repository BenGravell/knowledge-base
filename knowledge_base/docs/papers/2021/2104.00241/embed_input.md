Variational Inference MPC Using Tsallis Divergence

Topics include Model predictive path integral control, Variational inference, Tsallis divergence, Stochastic optimal control, Model predictive control.

Extends variational inference MPC by replacing KL divergence with Tsallis divergence, yielding a broader family of sampling-based controllers that recovers MPPI as a special case and can better handle multimodal cost landscapes.

In this paper, we provide a generalized framework for Variational Inference-Stochastic Optimal Control by using thenon-extensive Tsallis divergence. By incorporating the deformed exponential function into the optimality likelihood function, a novel Tsallis Variational Inference-Model Predictive Control algorithm is derived, which includes prior works such as Variational Inference-Model Predictive Control, Model Predictive Path Integral Control, Cross Entropy Method, and Stein Variational Inference Model Predictive Control as special cases. The proposed algorithm allows for effective control of the cost/reward transform and is characterized by superior performance in terms of mean and variance reduction of the associated cost. The aforementioned features are supported by a theoretical and numerical analysis on the level of risk sensitivity of the proposed algorithm as well as simulation experiments on 5 different robotic systems with 3 different policy parameterizations.

## Introduction

Variational Inference (VI) is a powerful tool for approximating the posterior distribution of the unobserved random variables. VI recasts the approximation problem as an optimization problem. Instead of directly approximating the target distribution $p{(\left. z \middle| x \right.)}$ of the latent variable $z$, VI minimizes the Kullback-Leibler (KL) divergence between a tractable variational distribution $q{(z)}$ and the target distribution. Due to its faster convergence and comparable performance to Markov Chain Monte Carlo sampling methods, VI has received increasing attention in machine learning and robotics.

VI has been applied to Stochastic Optimal Control (SOC) problems recently. In Okada and Taniguchi, the authors formulated the SOC problem as a VI problem by setting the desired policy distribution as the target distribution. The VI-SOC framework works directly in the space of policy distributions instead of specific policy parameterizations in most SOC and Reinforcement Learning (RL) frameworks. This gives rise to a unified derivation for a variety of parametric policy distributions, such as unimodal Gaussian and Gaussian mixture in Okada and Taniguchi. Lambert et al....

## Conclusion

We present a generalized Variational Inference-Stochastic Optimal Control framework using Tsallis divergence, which allows for additional control of the cost/reward transform and results in lower cost/reward variance. We provide a unifying study of the connections between Tsallis VI-SOC, MPPI, CEM, and SS methods. The performance and variance reduction benefits of the proposed Tsallis VI-SOC framework is verified analytically and numerically. We further showcase advantages of the Tsallis VI-MPC algorithm against MPPI and CEM on 5 different systems with 3 different policy distributions....

## Analysis

Stein Variational Policy: The policy can also be a non-parametric distribution approximated by a set of particles $\Theta ≔ {\{\theta_{l}\}}_{l = 1}^{L}$ for some parametrized policy $\hat{\pi}{(U;\theta)}$. In, $\hat{\pi}$ is taken to be a unimodal Gaussian with fixed variance, where $\theta \in {\mathbb{R}}^{n_{x} \times {({T - 1})}}$ corresponds to the mean. The update law of each Stein particle for the $k + 1$th iteration has the form

Cost (Std Dev)
Mean Control Error
