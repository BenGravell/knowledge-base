Learning Robust Control for LQR Systems with Multiplicative Noise via Policy Gradient

Topics include Gradient method, Gradient descent, Natural gradients, Reinforcement learning, Policy gradients, Linear systems, Uncertain systems, Optimal control, Stochastic systems, Multiplicative noise, Non-convex, Dynamics, Global convergence, Linear quadratic regulator.

Provides non-asymptotic finite-sample convergence results for policy gradient algorithms applied to the problem of optimal control of linear systems with multiplicative noise when the dynamics and noise covariances are unknown.

The linear quadratic regulator (LQR) problem has reemerged as an important theoretical benchmark for reinforcement learning-based control of complex dynamical systems with continuous state and action spaces. In contrast with nearly all recent work in this area, we consider multiplicative noise models, which are increasingly relevant because they explicitly incorporate inherent uncertainty and variation in the system dynamics and thereby improve robustness properties of the controller. Robustness is a critical and poorly understood issue in reinforcement learning; existing methods which do not account for uncertainty can converge to fragile policies or fail to converge at all. Additionally, intentional injection of multiplicative noise into learning algorithms can enhance robustness of policies, as observed in ad hoc work on domain randomization....

## Introduction

Reinforcement learning-based control has recently achieved impressive successes in games and simulators. But these successes are significantly more challenging to translate to complex physical systems with continuous state and action spaces, safety constraints, and non-negligible operation and failure costs that demand data efficiency. An intense and growing research effort is creating a large array of models, algorithms, and heuristics for approaching the myriad of challenges arising from these systems....

Almost all recent work on learning in LQR problems has utilized either deterministic or additive noise models, but here we consider *multiplicative noise models*. In control theory, multiplicative noise models have been studied almost as long as their deterministic and additive noise counterparts, although this area is somewhat less developed and far less widely known. We believe the study of learning in LQR problems with multiplicative noise is important for three reasons....

## Conclusions

We have shown that policy gradient methods in both model-based and model-free settings give global convergence to the globally optimal policy for LQR systems with multiplicative noise. These techniques are directly applicable for the design of robust controllers of uncertain systems and serve as a benchmark for data-driven control design. Our ongoing work is exploring ways of mitigating the relative sample inefficiency of model-free policy gradient methods by leveraging the special structure of LQR models and Nesterov-type acceleration, and exploring alternative system identification and adaptive control approaches....

where the last step used the definition and submultiplicativity of spectral norm. Using

In this section, we demonstrate that the multiplicative noise LQR cost function is *gradient dominated*, which facilitates optimization by gradient descent. Gradient dominated functions have been studied for many years in the optimization literature and have recently been discovered in deterministic LQR problems by.

confirming that the stationary point is indeed a global minimum.

### Related literature

Multiplicative noise LQR problems have been studied in control theory since the 1960s. Since then a line of research parallel to deterministic and additive noise has developed, including basic stability and stabilizability results,...
