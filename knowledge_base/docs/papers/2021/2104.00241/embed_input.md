Variational Inference MPC Using Tsallis Divergence

Topics include Model predictive path integral control, Variational inference, Tsallis divergence, Stochastic optimal control, Model predictive control.

Extends variational inference MPC by replacing KL divergence with Tsallis divergence, yielding a broader family of sampling-based controllers that recovers MPPI as a special case and can better handle multimodal cost landscapes.

In this paper, we provide a generalized framework for Variational Inference-Stochastic Optimal Control by using thenon-extensive Tsallis divergence. By incorporating the deformed exponential function into the optimality likelihood function, a novel Tsallis Variational Inference-Model Predictive Control algorithm is derived, which includes prior works such as Variational Inference-Model Predictive Control, Model Predictive Path Integral Control, Cross Entropy Method, and Stein Variational Inference Model Predictive Control as special cases. The proposed algorithm allows for effective control of the cost/reward transform and is characterized by superior performance in terms of mean and variance reduction of the associated cost. The aforementioned features are supported by a theoretical and numerical analysis on the level of risk sensitivity of the proposed algorithm as well as simulation experiments on 5 different robotic systems with 3 different policy parameterizations.

## Introduction

Variational Inference (VI) is a powerful tool for approximating the posterior distribution of the unobserved random variables. VI recasts the approximation problem as an optimization problem. Instead of directly approximating the target distribution $p{(\left. z \middle| x \right.)}$ of the latent variable $z$, VI minimizes the Kullback-Leibler (KL) divergence between a tractable variational distribution $q{(z)}$ and the target distribution. Due to its faster convergence and comparable performance to Markov Chain Monte Carlo sampling methods, VI has received increasing attention in machine learning and robotics.

In existing VI-SOC works, the KL divergence is used as the distributional distance metric due to its simplicity. On the other hand, recent advances in VI research involve extending the framework to other statistical divergences, such as the $\alpha$-divergence and $\chi$-divergence. In Wang et al., Regli and Silva, the authors proposed variants of the $\alpha$-divergence to improve the performance and robustness of the inference algorithm. Wan et al. further extended the VI framework to $f$-divergence, which is a broad statistical divergence family that recovers the KL, $\alpha$ and $\chi$-divergence as special cases.

In this paper, we provide a generalized formulation of the VI-SOC framework using the Tsallis divergence and introduce a novel Model Predictive Control (MPC) algorithm.

We propose the Tsallis VI-MPC algorithm, which allows for additional control of the shape of the cost transform compared to previous VI-MPC algorithms using KL divergence.

## Conclusion

We present a generalized Variational Inference-Stochastic Optimal Control framework using Tsallis divergence, which allows for additional control of the cost/reward transform and results in lower cost/reward variance. We provide a unifying study of the connections between Tsallis VI-SOC, MPPI, CEM, and SS methods. The performance and variance reduction benefits of the proposed Tsallis VI-SOC framework is verified analytically and numerically. We further showcase advantages of the Tsallis VI-MPC algorithm against MPPI and CEM on 5 different systems with 3 different policy distributions.
