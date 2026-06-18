Certainty Equivalent Quadratic Control for Markov Jump Systems

Topics include Markov jump systems, Certainty equivalence, Linear quadratic control, Riccati equation, Robustness, Perturbation bounds.

Develops perturbation bounds for certainty-equivalent quadratic control of Markov jump linear systems with errors in dynamics and transition probabilities. The paper isolates how uncertainty propagates through coupled Riccati equations and the optimal cost, supporting model-based control under estimated jump dynamics.

Real-world control applications often involve complex dynamics subject to abrupt changes or variations. Markov jump linear systems (MJS) provide a rich framework for modeling such dynamics. Despite an extensive history, theoretical understanding of parameter sensitivities of MJS control is somewhat lacking. Motivated by this, we investigate robustness aspects of certainty equivalent model-based optimal control for MJS with quadratic cost function. Given the uncertainty in the system matrices and in the Markov transition matrix is bounded by epsilon and eta respectively, robustness results are established for (i) the solution to coupled Riccati equations and (ii) the optimal cost, by providing explicit perturbation bounds which decay as O(epsilon+ eta) and O((epsilon+ eta)^) respectively.

## Introduction

The Linear Quadratic Regulator (LQR) is both theoretically well understood and commonly used in practice when the system dynamics are known. It also provides an interesting benchmark, when system dynamics are unknown, for reinforcement learning with continuous state and action spaces and for adaptive control.

A natural generalization of linear dynamical systems is Markov jump linear systems (MJS) that allow the dynamics of the underlying system to switch between multiple linear systems according to an underlying finite Markov chain. Similarly, a natural generalization of LQR problem to MJS is to use mode-dependent cost matrices, which allows to have different control goals under different modes. While the optimal control for MJS-LQR is well understood when one has perfect knowledge of the system dynamics, in practice it may not be optimal due to the imperfect knowledge of the system dynamics and the transition matrix....

## Conclusions

In this work, we provide a perturbation analysis for cDARE, which arise in the solution of MJS-LQR, and an end-to-end suboptimality guarantee for certainty equivalence control for MJS-LQR. Our results show the robustness of the optimal policy to perturbations in system dynamics and establish the validity of the certainty equivalent control in a neighborhood of the original system. This work opens up multiple future directions. First, with proper system identification algorithms, we can analyze model-based online/adaptive algorithms where control policy is updated continuously over a single trajectory....

for all $i \in {\lbrack s\rbrack}$ and $\mathbf{X}_{i} \succeq 0$, where the operator $\hat{\varphi}$ is defined as

Here, we consider the long-term average quadratic cost

In the following, we will show that despite being coupled, cDARE for MJS-LQR satisfies nice properties. To be more precise, we show that if the approximate MJS is accurate enough, i.e., $\epsilon$ and $\eta$ are sufficiently small, we can guarantee that not only the positive definite solution ${\hat{\mathbf{P}}}_{1:s}$ to the perturbed cDARE uniquely exists, but also ${\hat{\mathbf{P}}}_{1:s}$ does not not deviate much from $\mathbf{P}_{1:s}^{\star}$.

The solution of infinite horizon MJS-LQR involves coupled algebraic Riccati equations. Our goal is to understand how sensitive the solution of these equations and the corresponding...
