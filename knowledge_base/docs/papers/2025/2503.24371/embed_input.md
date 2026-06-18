Policy Gradient for LQR with Domain Randomization

Topics include Robustness, Control, Policy gradients, DR, Linear quadratic regulator.

Domain randomization (DR) enables sim-to-real transfer by training controllers on a distribution of simulated environments, with the goal of achieving robust performance in the real world. Although DR is widely used in practice and is often solved using simple policy gradient (PG) methods, understanding of its theoretical guarantees remains limited. Toward addressing this gap, we provide the first convergence analysis of PG methods for domain-randomized linear quadratic regulation (LQR). We show that PG converges globally to the minimizer of a finite-sample approximation of the DR objective under suitable bounds on the heterogeneity of the sampled systems. We also quantify the sample-complexity associated with achieving a small performance gap between the sample-average and population-level objectives. Additionally, we propose and analyze a discount-factor annealing algorithm that obviates the need for an initial jointly stabilizing controller, which may be challenging to find. Empirical results support our theoretical findings and highlight promising directions for future work, including risk-sensitive DR formulations and stochastic PG algorithms.

## Introduction

Domain randomization (DR) has emerged as a dominant paradigm to enable transfer of policies optimized in simulation to the real world by randomizing simulator parameters during training. In doing so, just as with robust control, DR accounts for discrepancies between the model used in simulation to synthesize a policy and the system that it is deployed on. However, unlike conventional robust control approaches, DR minimizes an average control objective over the uncertainty in the system rather than a worst case objective....

Despite the ease with which DR can be implemented using first order methods, ensuring convergence of these methods remains a critical challenge, with practitioners relying upon complex scheduling of various hyperparameters in the optimization procedure \[\]. Motivated by this challenge, we rigorously study the convergence of policy gradient methods for DR in the setting of the linear quadratic regulator.

## Conclusion

Our work proves the convergence of policy gradient methods applied to linear quadratic control with domain randomization. The analysis relies upon a generalization of the gradient domination condition from prior work. This generalization results in guarantees that are sensitive to the initialization; however, a curriculum learning approach with an appropriate schedule can bypass this sensitivity. We believe that this line of analysis has potential to demystify and improve heuristic approaches for taming the optimization landscape of DR from the robot learning literature \[\].

### Lemma III.6

A consequence of the above result is that the gradient descent procedure converges to a fixed point.

Subproblems and can be solved via bisection, while subproblem can be solved with algorithm starting from $K_{0}\leftarrow K$ by choosing an appropriate stepsize, and running sufficiently many iterations, as in Theorem III.1. ‣ III Policy Gradient Convergence ‣ Policy Gradient for LQR with Domain Randomization"). Extending the analysis of \[, Theorem 1\] to the setting of multiple systems leads to the following result.

### I-A Related Work

### Domain Randomization

Domain randomization, introduced by Tobin et al. \[\], is widely used for enabling *sim-to-real transfer*. By randomizing simulator parameters during training, it aims to produce policies robust to simulator variations, thereby enabling transfer to...
