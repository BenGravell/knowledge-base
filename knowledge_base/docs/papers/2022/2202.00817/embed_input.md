Do Differentiable Simulators Give Better Policy Gradients?

Topics include Policy gradients, Reinforcement learning, Robustness, Planning, Control, Learning.

Differentiable simulators promise faster computation time for reinforcement learning by replacing zeroth-order gradient estimates of a stochastic objective with an estimate based on first-order gradients. However, it is yet unclear what factors decide the performance of the two estimators on complex landscapes that involve long-horizon planning and control on physical systems, despite the crucial relevance of this question for the utility of differentiable simulators. We show that characteristics of certain physical systems, such as stiffness or discontinuities, may compromise the efficacy of the first-order estimator, and analyze this phenomenon through the lens of bias and variance. We additionally propose an alpha-order gradient estimator, with alpha , which correctly utilizes exact gradients to combine the efficiency of first-order estimates with the robustness of zero-order methods. We demonstrate the pitfalls of traditional estimators and the advantages of the alpha-order estimator on some numerical examples.

## Introduction

Consider the problem of minimizing a *stochastic objective*,

At the heart of many algorithms for reinforcement learning (RL) lies *zeroth-order* estimation of the gradient $\nabla F$. Yet, in domains that deal with structured systems, such as linear control, physical simulation, or robotics, it is possible to obtain *exact* gradients of $f$, which can also be used to construct a *first-order* estimate of $\nabla F$. The availability of both options begs the question: given access to exact gradients of $f$, which estimator should we prefer?

However, the landscape of RL objectives that involve long-horizon sequential decision making (e.g. policy optimization) is challenging to analyze, and convergence properties in these landscapes are relatively poorly understood, except for structured settings such as finite-state MDPs or linear control. In particular, physical systems with contact, as we show in Figure 1, can display complex characteristics including nonlinearities, non-smoothness, and discontinuities.

When $f$ is continuous, these quantities both converge to the same quantity ($\nabla F$) in expectation. We first show that even with continuous $f$, the first-order gradient estimate *can* result in more variance than the zeroth-order one due to the *stiffness* of dynamics or due to compounding of gradients in chaotic systems.

## Discussion

In this section, we elaborate and discuss on some of the ramifications of our work.

Impact on Computation Time. The convergence rate of gradient descent in stochastic optimization scales directly with the variance of the estimator. For smooth and well-behaved landscapes, FoBG often converges faster since ${\text{Var}{\lbrack{{\overline{\nabla}}^{\lbrack 1\rbrack}F}\rbrack}} < {\text{Var}{\lbrack{{\overline{\nabla}}^{\lbrack 0\rbrack}F}\rbrack}}$. However, when there are discontinuities or near-discontinuities in the landscape, this promise no longer holds since gradient descent using FoBG might not converge due to bias. Indeed, Example 3.6.
