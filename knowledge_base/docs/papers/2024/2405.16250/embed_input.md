Conformal Robust Control of Linear Systems

Topics include Policy gradients, Regret bounds, Optimal control, Robustness, Uncertainty, Probabilistic models, Control, Linear systems.

End-to-end engineering design pipelines, in which designs are evaluated using concurrently defined optimal controllers, are becoming increasingly common in practice. To discover designs that perform well even under the misspecification of system dynamics, such end-to-end pipelines have now begun evaluating designs with a robust control objective in place of the nominal optimal control setup. Current approaches of specifying such robust control subproblems, however, rely on hand specification of perturbations anticipated to be present upon deployment or margin methods that ignore problem structure, resulting in a lack of theoretical guarantees and overly conservative empirical performance. We, instead, propose a novel methodology for LQR systems that leverages conformal prediction to specify such uncertainty regions in a data-driven fashion. Such regions have distribution-free coverage guarantees on the true system dynamics, in turn allowing for a probabilistic characterization of the regret of the resulting robust controller. We then demonstrate that such a controller can be efficiently produced via a novel policy gradient method that has convergence guarantees....

## Introduction

Seeking control over a family of dynamical systems is a problem often encountered in engineering. One prevalent application of this is in cases where engineering designs and their respective controllers are being concurrently developed, known as control co-design (CCD) \[\]. Traditional engineering design loops operated sequentially, first proposing a design and then developing a controller. Such workflows, however, sacrificed the improved optimality possible in their coupling, hence the increasing interest in leveraging end-to-end co-control design pipelines.

Initial works in CCD studied optimal design assuming perfectly specified, deterministic system dynamics. Such assumptions have, however, become overly restrictive, resulting in interest in robust extensions of the CCD formulation, referred to as uncertain CCD (UCCD). Such uncertainty can arise from many sources in the design process, such as noise in the controllers, uncertainties in the design parameters, or unmodeled dynamics. The UCCD specification also differs depending on the risk tolerance in the downstream application....

## Discussion

We have presented CPC, a principled framework for specifying the LQR robust control subproblem in a UCCD setting, suggesting many directions for extension. The most immediate would involve integrating this framework fully into a UCCD pipeline: we focused herein on the robust control subproblem but characterizing the end-to-end workflow is of great interest. In addition, nonlinear extension by leveraging Koopman operator theory or nonparametric neural operator models would be interesting as would the extension to MDPs \[\].

### Theorem 3.5 (Stochastic, continuous-time)

where $J$ is the objective function particular to the setting of interest, differing between infinite and finite time horizons and continuous and discrete time dynamics, and $\mathcal{U}{(\theta)}$ is an uncertainty set over dynamics. Notably, the notion of stabilizing controllers must be generalized in this robust formulation, since the nominal formulation is for a specific $C$....

The full proof is deferred to Appendix I and parallels the proof strategy presented in \[\]; the main technical challenges are in demonstrating that bounds on expressions related to $J{(K,C)}$ and ${\nabla_{K}J}{(K,C)}$ are retained in our robust setting and that the non-uniqueness of the...
