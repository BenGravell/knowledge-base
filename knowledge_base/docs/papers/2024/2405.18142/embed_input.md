Data-Driven Distributionally Robust System Level Synthesis

We present a novel approach for the control of uncertain, linear time-invariant systems, which are perturbed by potentially unbounded, additive disturbances. We propose a doubly robust data-driven state-feedback controller to ensure reliable performance against both model mismatch and disturbance distribution uncertainty. Our controller, which leverages the System Level Synthesis parameterization, is designed as the solution to a distributionally robust finite-horizon optimal control problem. The goal is to minimize a cost function while satisfying constraints against the worst-case realization of the uncertainty, which is quantified using distributional ambiguity sets. The latter are defined as balls in the Wasserstein metric centered on the predictive empirical distribution computed from a set of collected trajectory data. By harnessing techniques from robust control and distributionally robust optimization, we characterize the distributional shift between the predictive and the actual closed-loop distributions, and highlight its dependency on the model mismatch and the uncertainty about the disturbance distribution....

## Introduction

Dealing with uncertainty is a fundamental challenge in many control applications. Oftentimes, the dynamics of the system and the distribution of the disturbance acting on it are unknown and should be accounted for. Robust and stochastic approaches have been developed in the last two decades to specifically address both types of uncertainty. Robust methods assume bounded uncertainties and solve a worst-case optimization problem to provide guarantees against any possible realization of the uncertainty. Formulations have been developed to account for uncertainties in both the model and the realization of the disturbance....

Stochastic methods can reduce this conservatism by imposing constraints that must be satisfied with a certain probability. However, analytical solutions in the stochastic setting can be obtained only under specific assumptions about the distribution of the uncertainty. Alternatively, randomized methods such as the sample average approximation and the scenario approach can be used to reformulate the stochastic problem into large, but finite-dimensional, deterministic optimization problems....

## Conclusions

We presented a novel distributionally robust state-feedback data-driven controller for uncertain discrete-time linear time-invariant systems affected by unknown additive disturbances. We formulated the problem as a stochastic optimization problem with respect to the worst-case probability distribution within an ambiguity set centered on the empirical nominal predictive distribution....

The distance between the predictive empirical distribution and the closed-loop distribution is upper-bounded by:

The superscript $\hat{\mathcal{M}}$ denotes that we are relying on the nominal model to construct the empirical distribution of the disturbances in and for the system forward simulation in, while the subscript $\pi$ denotes the state-feedback policy induced by the feedback matrix $\mathcal{K}$.

On the flip side, the term $\kappa{(\eta,N)}$ decays slowly, that is, the rate $O{(N^{- {{1/n}T}})}$ is exponentially slow with the system dimension $n$ and horizon $T$. In the literature, this limitation is commonly referred to as the curse of dimensionality. In practice, we could use a $\kappa$ different from the one proscribed by Lemma 3. In this case, we can treat $\kappa$ as a hyperparameter and tune it via cross-validation.
