Certainty Equivalent Quadratic Control for Markov Jump Systems

Topics include Markov jump systems, Certainty equivalence, Linear quadratic control, Riccati equation, Robustness, Perturbation bounds.

Develops perturbation bounds for certainty-equivalent quadratic control of Markov jump linear systems with errors in dynamics and transition probabilities. The paper isolates how uncertainty propagates through coupled Riccati equations and the optimal cost, supporting model-based control under estimated jump dynamics.

Real-world control applications often involve complex dynamics subject to abrupt changes or variations. Markov jump linear systems (MJS) provide a rich framework for modeling such dynamics. Despite an extensive history, theoretical understanding of parameter sensitivities of MJS control is somewhat lacking. Motivated by this, we investigate robustness aspects of certainty equivalent model-based optimal control for MJS with quadratic cost function. Given the uncertainty in the system matrices and in the Markov transition matrix is bounded by epsilon and eta respectively, robustness results are established for (i) the solution to coupled Riccati equations and (ii) the optimal cost, by providing explicit perturbation bounds which decay as O(epsilon+ eta) and O((epsilon+ eta)^) respectively.

## Introduction

The Linear Quadratic Regulator (LQR) is both theoretically well understood and commonly used in practice when the system dynamics are known. It also provides an interesting benchmark, when system dynamics are unknown, for reinforcement learning with continuous state and action spaces and for adaptive control.

A natural generalization of linear dynamical systems is Markov jump linear systems (MJS) that allow the dynamics of the underlying system to switch between multiple linear systems according to an underlying finite Markov chain. Similarly, a natural generalization of LQR problem to MJS is to use mode-dependent cost matrices, which allows to have different control goals under different modes. While the optimal control for MJS-LQR is well understood when one has perfect knowledge of the system dynamics, in practice it may not be optimal due to the imperfect knowledge of the system dynamics and the transition matrix.

The solution of infinite horizon MJS-LQR involves coupled algebraic Riccati equations. Our goal is to understand how sensitive the solution of these equations and the corresponding optimal cost are to the perturbations in system model. To this aim, we first develop explicit $\mathcal{O}{({\epsilon + \eta})}$ perturbation bound for the solution to coupled algebraic Riccati equations that arise in the context of MJS-LQR. This in turn is used to establish explicit $\mathcal{O}{({({\epsilon + \eta})}^{2})}$ suboptimality bound. Finally, numerical experiments are provided to support our theoretical claims.

## III-A Markov Jump Systems

We consider the problem of optimally controlling MJS, which are governed by the state equation,
