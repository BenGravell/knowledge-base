Learning Robust Control for LQR Systems with Multiplicative Noise via Policy Gradient

Topics include Gradient method, Gradient descent, Natural gradients, Reinforcement learning, Policy gradients, Linear systems, Uncertain systems, Optimal control, Stochastic systems, Multiplicative noise, Non-convex, Dynamics, Global convergence, Linear quadratic regulator.

Provides non-asymptotic finite-sample convergence results for policy gradient algorithms applied to the problem of optimal control of linear systems with multiplicative noise when the dynamics and noise covariances are unknown.

The linear quadratic regulator (LQR) problem has reemerged as an important theoretical benchmark for reinforcement learning-based control of complex dynamical systems with continuous state and action spaces. In contrast with nearly all recent work in this area, we consider multiplicative noise models, which are increasingly relevant because they explicitly incorporate inherent uncertainty and variation in the system dynamics and thereby improve robustness properties of the controller. Robustness is a critical and poorly understood issue in reinforcement learning; existing methods which do not account for uncertainty can converge to fragile policies or fail to converge at all. Additionally, intentional injection of multiplicative noise into learning algorithms can enhance robustness of policies, as observed in ad hoc work on domain randomization.

## Introduction

Reinforcement learning-based control has recently achieved impressive successes in games and simulators. But these successes are significantly more challenging to translate to complex physical systems with continuous state and action spaces, safety constraints, and non-negligible operation and failure costs that demand data efficiency. An intense and growing research effort is creating a large array of models, algorithms, and heuristics for approaching the myriad of challenges arising from these systems.

Almost all recent work on learning in LQR problems has utilized either deterministic or additive noise models, but here we consider *multiplicative noise models*. In control theory, multiplicative noise models have been studied almost as long as their deterministic and additive noise counterparts, although this area is somewhat less developed and far less widely known. We believe the study of learning in LQR problems with multiplicative noise is important for three reasons.

## Related literature

Multiplicative noise LQR problems have been studied in control theory since the 1960s. Since then a line of research parallel to deterministic and additive noise has developed, including basic stability and stabilizability results, semidefinite programming formulations, robustness properties, and numerical algorithms. This line of research is less widely known perhaps because much of it studies continuous time systems, where the heavy machinery required to formalize stochastic differential equations is a barrier to entry for a broad audience.

In contrast to classical work on system identification and adaptive control, which has a strong focus on asymptotic results, more recent work has focused on non-asymptotic analysis using newly developed mathematical tools from statistics and machine learning. There remain fundamental open problems for learning in LQR problems, with several addressed only recently, including non-asymptotic sample complexity, regret bounds, and algorithmic convergence. Alternatives to reinforcement learning include other data-driven model-free optimal control schemes and those leveraging the behavioral framework.
