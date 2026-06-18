<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Policy Iteration for Multiplicative Noise Output Feedback Control

Topics include Policy iteration, Multiplicative noise, Output feedback, Linear quadratic control, Stochastic optimal control, POMDPs, Riccati equation, Dynamic output feedback.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends policy iteration to the partially observed multiplicative-noise linear quadratic setting, where the controller is a linear dynamic output-feedback policy rather than a static state-feedback gain. The main contribution is a coupled estimator-controller Riccati iteration that delivers results much more quickly/with less computation effort than the prior value-iteration approach, in some cases. This points toward scalable policy optimization methods for more general POMDPs.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a policy iteration algorithm for solving the multiplicative noise linear quadratic output feedback design problem. The algorithm solves a set of coupled Riccati equations for estimation and control arising from a partially observable Markov decision process (POMDP) under a class of linear dynamic control policies. We show in numerical experiments far faster convergence than a value iteration algorithm, formerly the only known algorithm for solving this class of problem. The results suggest promising future research directions for policy optimization algorithms in more general POMDPs, including the potential to develop novel approximate data-driven approaches when model parameters are not available.
