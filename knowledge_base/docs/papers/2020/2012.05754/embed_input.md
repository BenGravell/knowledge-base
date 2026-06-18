Optimal Thompson Sampling Strategies for Support-aware CVaR Bandits

Topics include Bandits, Regret bounds, Sampling, Conditional value at risk, Thompson sampling.

In this paper we study a multi-arm bandit problem in which the quality of each arm is measured by the Conditional Value at Risk (CVaR) at some level alpha of the reward distribution. While existing works in this setting mainly focus on Upper Confidence Bound algorithms, we introduce a new Thompson Sampling approach for CVaR bandits on bounded rewards that is flexible enough to solve a variety of problems grounded on physical resources. Building on a recent work by Riou & Honda, we introduce B-CVTS for continuous bounded rewards and M-CVTS for multinomial distributions. On the theoretical side, we provide a non-trivial extension of their analysis that enables to theoretically bound their CVaR regret minimization performance. Strikingly, our results show that these strategies are the first to provably achieve asymptotic optimality in CVaR bandits, matching the corresponding asymptotic lower bounds for this setting. Further, we illustrate empirically the benefit of Thompson Sampling approaches both in a realistic environment simulating a use-case in agriculture and on various synthetic examples.

## Introduction

Over the past few years, a number of works have focused on adapting multi-armed bandit strategies (see e.g. Lattimore and Szepesvari ) to optimize an other criterion than the expected cumulative reward. Sani et al., Vakili and Zhao, Vakili and Zhao, Zimin et al. consider a mean-variance criterion, studies a quantile (Value-at-Risk) criterion, focuses on Entropic-value-at-risk. The Conditional Value at Risk (CVaR) as well as more generic coherent spectral risk measures have received specific attention from the bandit community (Galichet et al.; Galichet; Cassel et al.; Zhu and Tan; Tamkin et al.; Prashanth et al. to cite a few)....

The Conditional Value at Risk (CVaR) at level $\alpha \in {\lbrack 0,1\rbrack}$ (see Mandelbrot, Artzner et al. ) is easily interpretable as the expected reward in the worst $\alpha$-fraction of the outcomes, and hence captures different preferences, from being neutral to the shape of the distribution ($\alpha = 1$, mean criterion) to trying to maximize the reward in the worst-case scenarios ($\alpha$ close to 0, typically in finance or insurance). It is further a coherent spectral measure in the sense of Rockafellar et al., see Acerbi and Tasche )....

### Perspectives

This first set of experiments using a challenging realistic crop simulator is promising, and motivates to further investigate the use of B-CVTS algorithm for crop-management support and other problems that can be modeled as CVaR bandits. B-CVTS enjoys appealing theoretical guarantees, and thanks to its simplicity and competitive empirical performances may be a good candidate for practitioners. In order to address real-world crop-management challenges, many questions remain to be considered, e.g....

The proofs of, and follow the outline of Riou and Honda, respectively for Multinomial Thompson Sampling and Non Parametric Thompson Sampling. However, replacing the linear expectation by the CVaR that is non-linear, causes several technical challenges that make the adaptation non-trivial. This is particularly true for the boundary crossing probabilities for Dirichlet random variables, that we define and analyze in this section. Our results aim at replacing the Lemma 13, 14, 15 and 17 of Riou and Honda in the proofs of Theorem 2....

Using, this result directly yields an asymptotic lower bound on the regret. The proof of Theorem 1....
