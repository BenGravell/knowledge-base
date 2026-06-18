Policy Gradient for LQR with Domain Randomization

Topics include Robustness, Control, Policy gradients, DR, Linear quadratic regulator.

Domain randomization (DR) enables sim-to-real transfer by training controllers on a distribution of simulated environments, with the goal of achieving robust performance in the real world. Although DR is widely used in practice and is often solved using simple policy gradient (PG) methods, understanding of its theoretical guarantees remains limited. Toward addressing this gap, we provide the first convergence analysis of PG methods for domain-randomized linear quadratic regulation (LQR). We show that PG converges globally to the minimizer of a finite-sample approximation of the DR objective under suitable bounds on the heterogeneity of the sampled systems. We also quantify the sample-complexity associated with achieving a small performance gap between the sample-average and population-level objectives. Additionally, we propose and analyze a discount-factor annealing algorithm that obviates the need for an initial jointly stabilizing controller, which may be challenging to find. Empirical results support our theoretical findings and highlight promising directions for future work, including risk-sensitive DR formulations and stochastic PG algorithms.

## Introduction

Domain randomization (DR) has emerged as a dominant paradigm to enable transfer of policies optimized in simulation to the real world by randomizing simulator parameters during training. In doing so, just as with robust control, DR accounts for discrepancies between the model used in simulation to synthesize a policy and the system that it is deployed . However, unlike conventional robust control approaches, DR minimizes an average control objective over the uncertainty in the system rather than a worst case objective.

Despite the ease with which DR can be implemented using first order methods, ensuring convergence of these methods remains a critical challenge, with practitioners relying upon complex scheduling of various hyperparameters in the optimization procedure. Motivated by this challenge, we rigorously study the convergence of policy gradient methods for DR in the setting of the linear quadratic regulator.

## Discussion

There are several exciting possibilities for theoretical and empirical extensions of the results presented in this paper.

Relaxed heterogeneity assumptions: Our theory required strong requirements on the distance between systems. These requirements can almost certainly be made weaker; however, it is unclear the extent to which they are fundamental. Our numerical experiments failed to discover any instances where policy gradient did not converge due to a large distance between systems, unless it was impossible to simultaneously stabilize these systems.

Practical implications: The study conducted in this paper provides a better understanding of the application of gradient-based approaches for reinforcement learning with domain randomization. It may be possible to use this perspective to design alternative hyperparameter schedules for domain randomization as applied in practice.
