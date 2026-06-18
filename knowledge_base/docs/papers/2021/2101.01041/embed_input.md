Derivative-Free Policy Optimization for Linear Risk-Sensitive and Robust Control Design: Implicit Regularization and Sample Complexity

Topics include Nonconvex optimization, Policy gradients, Reinforcement learning, Multi-agent systems, Safety, Robustness, Attention mechanisms, Sample complexity, Optimization, Control, Learning, Sampling, Design, Multi-agent reinforcement learning, Optimization problem.

Direct policy search serves as one of the workhorses in modern reinforcement learning (RL), and its applications in continuous control tasks have recently attracted increasing attention. In this work, we investigate the convergence theory of policy gradient (PG) methods for learning the linear risk-sensitive and robust controller. In particular, we develop PG methods that can be implemented in a derivative-free fashion by sampling system trajectories, and establish both global convergence and sample complexity results in the solutions of two fundamental settings in risk-sensitive and robust control: the finite-horizon linear exponential quadratic Gaussian, and the finite-horizon linear-quadratic disturbance attenuation problems. As a by-product, our results also provide the first sample complexity for the global convergence of PG methods on solving zero-sum linear-quadratic dynamic games, a nonconvex-nonconcave minimax optimization problem that serves as a baseline setting in multi-agent reinforcement learning (MARL) with continuous spaces....

## Introduction

Recent years have witnessed the rapid development of reinforcement learning (RL) methods in handling continuous control tasks. Central to the success of RL are policy optimization (PO) methods, including policy gradient (PG), actor-critic, and other variants. Progress reported in the literature has clearly shown an increasing interest in understanding theoretical properties of PO methods for relatively simple baseline problems such as various linear control problems. However, the theory of model-free PO methods on *risk-sensitive/robust* control remains underdeveloped in the literature....

Our work in this paper is motivated by the above concern, and studies the sample complexity of model-free PG methods on two important baseline problems in risk-sensitive/robust control, namely the linear exponential quadratic Gaussian (LEQG), and the linear quadratic (LQ) disturbance attenuation problems. The former covers a fundamental setting in risk-sensitive control, and the latter is an important baseline for robust control. Based on the well-known equivalence between these problems and LQ dynamic games, we develop a *unified* PO perspective for both....

## Concluding Remarks

In this paper, we have investigated derivative-free policy optimization methods for solving a class of risk-sensitive and robust control problems, covering three fundamental settings: LEQG, LQ disturbance attenuation, and zero-sum LQ dynamic games. This work aims towards combining two lines of research, robust control theory, and policy-based model-free RL methods....

Subsequently, we analyze the optimization landscape of the outer loop in the following lemma (proved in §A.9), subject to the feasible set $\mathcal{K}$ defined by (3.9). Note that the set $\mathcal{K}$ is critical, as by Lemma 3.3, it is a sufficient and almost necessary condition to ensure that the solution to the associated inner-loop subproblem is well defined. More importantly, from a robust control perspective, such a set $\mathcal{K}$ represents the set of control gains that enjoy a certain level of *robustness*, which share the same vein as the $\mathcal{H}_{\infty}$-norm constraint for the infinite-horizon LTI setting....

## Policy Gradient Methods

We present the sample complexity of our double-loop algorithm, when the exact PG is not accessible, and can only be estimated through samples of...
