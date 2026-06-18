KPC: Learning-Based Model Predictive Control with Deterministic Guarantees

Topics include Model predictive control, Predictive control, Safety, Robustness, Regression, Optimization, Control, Learning, KPC.

We propose Kernel Predictive Control (KPC), a learning-based predictive control strategy that enjoys deterministic guarantees of safety. Noise-corrupted samples of the unknown system dynamics are used to learn several models through the formalism of non-parametric kernel regression. By treating each prediction step individually, we dispense with the need of propagating sets through highly non-linear maps, a procedure that often involves multiple conservative approximation steps. Finite-sample error bounds are then used to enforce state-feasibility by employing an efficient robust formulation. We then present a relaxation strategy that exploits on-line data to weaken the optimization problem constraints while preserving safety. Two numerical examples are provided to illustrate the applicability of the proposed control method.

## Introduction

Safety is the number one requirement for any system that operates under physical constraints. For decades, this has been a major concern when control systems incorporate forms of adaptation or learning. A considerable body of literature exists establishing stability and performance guarantees in scenarios of parametric plant-model mismatch (see Lorenzen et al.; Tanaskovic et al.; Bujarbaruah and Vallon for some recent works in this direction)....

A compelling alternative to the paradigm described above is the use of non-parametric models. These form a flexible class of surrogate functions whose number of parameters grows with the cardinality of the dataset. Relevant examples for the control community include the Nonlinear Set Memebership (NSM) and the Kinky Inference (KI) techniques....

KPC was proposed as a predictive control methodology based on non-parametric kernel models and their associated uncertainty estimates. Its key feature is deterministic constraint satisfaction when a solution to the optimization problem is found. From an approximation theory perspective, future works could study the advantages of employing SVR surrogate models over KRR ones, as well as refining the existing error-bounds, which we believe to be possible....

This work received support from the Swiss National Science Foundation under the Risk Aware Data-Driven Demand Response project (grant number 200021 175627) and CSEM's Data Program.

When compared to the GP bounds presented in Srinivas et al., the result given in Theorem 3.1). ‣ 3 Non-Parametric Kernel Learning ‣ KPC: Learning-Based Model Predictive Control with Deterministic Guarantees") does not involve information-theoretic measures such as the maximal information gain. The need of estimating such constant hampers the applicability of the former bounds in practical scenarios (see the discussion in Lederer et al. ). When compared to the results in, the inequality....

Note that the map described by has the same form as a Gaussian process posterior distribution conditioned on the data, that is, its predictive mean. Indeed, if $\sigma$ is the noise variance in the GP scenario and $\lambda$ is selected as $\sigma^{2}/D$, the two models are exactly the same. The reader is referred to for a discussion on the existing connections.
