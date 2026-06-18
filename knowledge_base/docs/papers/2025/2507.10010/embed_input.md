Probabilistic Robustness in the Gap Metric

Topics include Stability analysis, Robustness, Uncertainty, Probabilistic models, Control, Robust control, Random variable.

Uncertainties influencing the dynamical systems pose a significant challenge in estimating the achievable performance of a controller aiming to control such uncertain systems. When the uncertainties are of stochastic nature, obtaining hard guarantees for the robustness of a controller aiming to hedge against the uncertainty is not possible. This issue set the platform for the development of probabilistic robust control approaches. In this work, we utilise the gap metric between the known nominal model and the unknown perturbed model of the uncertain system as a tool to gauge the robustness of a controller and formulate the gap as a random variable in the setting with stochastic uncertainties. The main results of this paper include giving a probabilistic bound on the gap exceeding a known threshold, followed by bounds on the expected gap value and probabilistic robust stability and performance guarantees in terms of the gap metric. We also provide a probabilistic controller performance certification under gap uncertainty and probabilistic guarantee on the achievable H_infinity robustness. Numerical simulations are provided to demonstrate the proposed approach.

## Introduction

Robust control stands to be one of the most mature control methodologies to be ever developed mainly due to the strong guarantees that comes with it (interested readers are referred to and the references therein). Vinnicombe in \[\] describes robust control approaches as the ones where we try to come up with a control input for a system using what we know about the system so that the control input renders the system insensitive to what we do not know about the system....

where, $\mathbf{\Delta}$ denotes the set of possible uncertainties and it is allowed to be structured, unstructured, parametric, static, dynamic, time invariant and even time-varying in nature.

Another important research direction will be to extend the problem setting to both linear time varying systems and to nonlinear systems by formulating the quantity of interest namely the gap between the nominal and the corresponding perturbed system models as random.

Another interesting direction is to first develop gap metric based robust tube model predictive control (MPC). The uncertainty around the system trajectories from the true but unknown perturbed model different from the nominal model is characterised along the prediction horizon using the assumed gap between the nominal $(\overline{P})$ and the perturbed system $(P)$ (by formulating linear matrix inequality (LMI) \[\] constraints for the condition ${\delta_{g}{(P,\overline{P})}} \leq \alpha$ for a given $\alpha \in {}$)....

Note that $\theta^{\prime} = \mu_{\theta}$ is a valid assumption to make as ${{\mathbb{E}}{\lbrack\theta\rbrack}} = \mu_{\theta}$. On the other hand, we see that ${{\mathbb{E}}\left\lbrack {{Gap}{(\mu_{\theta})}} \right\rbrack} = {{Gap}{(\mu_{\theta})}}$ becomes a deterministic quantity. Then, using (35a ‣ 3 Solution Methodology ‣ Probabilistic Robustness in the Gap Metric")) in ), we get ). ∎

Coprime factor uncertainty can be understood as a combination of multiplicative and inverse multiplicative type uncertainties and the trade off between them is determined by the nominal plant. As a precursor to the gap metric, we will first demonstrate how the randomness in the co-prime factor uncertainty affects the robust stability associated with the nominal controller stabilising the nominal plant....
