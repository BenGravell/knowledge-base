Regret Analysis for Risk-aware Linear Quadratic Control

This paper investigates the regret associated with the Distributionally Robust Control (DRC) strategies used to address multistage optimization problems where the involved probability distributions are not known exactly, but rather are assumed to belong to specified ambiguity families. We quantify the price (distributional regret) that one ends up paying for not knowing the exact probability distribution of the stochastic system uncertainty while aiming to control it using the DRC strategies. The conservatism of the DRC strategies for being robust to worst-case uncertainty distribution in the considered ambiguity set comes at the price of lack of knowledge about the true distribution in the set. We use the worst case Conditional Value-at-Risk to define the distributional regret and the regret bound was found to be increasing with tighter risk level. The motive of this paper is to promote the design of new control algorithms aiming to minimize the distributional regret.

## Introduction

Stochastic optimization has been the backbone of success of several portfolio management systems in finance as they are equipped with necessary tools to handle risks of various kinds. Inspired by their application in finance, it is now being increasingly used in the control community as well. However, the success of stochastic optimization techniques depend on the knowledge of the true distribution of the random variable of interest as in \[Wozabal\].

To compute the regret associated with the problem formulation with moment based ambiguity sets, it is natural to consider the DRO objective function formulated using the expectation or the worst case $CVaR$ as the risk functional as described in \[Rockafellar et al.Rockafellar, Uryasev, et al., Wang and Chapman\]. However, we show that expectation is not the right risk functional to be considered in our problem setting as it does not effectively capture the tail probabilities from different distributions in the considered ambiguity set.

*Contributions:* To the best of our knowledge, this is one of the first articles in the literature to analyze the regret of a control policy that rather hedges against the worst case distributions of the stochastic system uncertainties and not knowing the exact true distribution of stochastic system uncertainties.

Following a short summary of notations and preliminaries, the rest of the paper is organized as follows: We propose a regret definition for distributionally robust control with moment based ambiguity sets in §2. Subsequently, a regret analysis is performed in §3. The simulation results demonstrating our proposed approach is explained in §4. Finally, the paper is closed in §5 along with a summary and directions for future research.

## Conclusion

The regret incurred by distributionally robust optimal controller while controlling systems with stochastic uncertainties modelled using moment based ambiguity set was presented in this paper. The worst-case ${CVaR}_{\alpha}{( \cdot )}$ with risk level $\alpha \in {}$ was selected to hedge against the distributional uncertainty and using it the regret incurred by the controller for not hedging against the true distribution of system uncertainties was analysed. The distributional regret bound was found to be increasing with tighter (that is smaller) risk levels.
