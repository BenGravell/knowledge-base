Wasserstein Distributionally Robust Stochastic Control: A Data-Driven Approach

Standard stochastic control methods assume that the probability distribution of uncertain variables is available. Unfortunately, in practice, obtaining accurate distribution information is a challenging task. To resolve this issue, we investigate the problem of designing a control policy that is robust against errors in the empirical distribution obtained from data. This problem can be formulated as a two-player zero-sum dynamic game problem, where the action space of the adversarial player is a Wasserstein ball centered at the empirical distribution. We propose computationally tractable value and policy iteration algorithms with explicit estimates of the number of iterations required for constructing an epsilon-optimal policy. We show that the contraction property of associated Bellman operators extends a single-stage out-of-sample performance guarantee, obtained using a measure concentration inequality, to the corresponding multi-stage guarantee without any degradation in the confidence level....

## Introduction

The theory of stochastic optimal control is based on the assumption that the probability distribution of uncertain variables (e.g., disturbances) is fully known. However, this assumption is often restrictive in practice, because estimating an accurate distribution requires large-scale high-resolution sensor measurements over a long training period or multiple periods....

To overcome this issue of limited distribution information in stochastic control, we investigate a *distributionally robust control* approach. This emerging minimax stochastic control method minimizes a cost function of interest, assuming that the distribution of uncertain variables is not completely known, but is contained in a pre-specified *ambiguity set* of probability distributions. In this paper, we model the ambiguity set as a statistical ball centered at an empirical distribution with a radius measured by the *Wasserstein metric*....

## Conclusions

In this paper, we considered distributionally robust stochastic control problems with Wasserstein ambiguity sets by directly using the data samples of uncertain variables. We showed that the proposed framework has several salient features, including $(i)$ computational tractability with error bounds, $({ii})$ an out-of-sample performance guarantee, and $({iii})$ an explicit solution in the LQ setting. It is worth emphasizing that the Kantorovich duality principle plays a critical role in our DP solution and analysis....

Note that the modified PI algorithm approximately evaluates the performance of a policy $\pi_{k}$ as ${\overset{\sim}{v}}_{k}$ instead of finding the exact fixed point of $T^{\pi_{k}}$. Concrete choices of the *order sequence* $\{ M_{k}\}$ are discussed in. However, for any choice of $\{ M_{k}\}$, the modified PI algorithm converges under Assumption 1:

To interpret this reformulation, we consider the following equivalent integral form:

where $\overline{\theta}$ satisfies $\frac{\overline{\theta}}{\log{({2 + {1/\overline{\theta}}})}} = {\lbrack{\frac{1}{Nc_{2}}{\log{(\frac{c_{1}}{\beta})}}}\rbrack}^{1/2}$, and $c_{1},c_{2}$ are the positive constants in Theorem 2. ‣ 4 Out-of-Sample Performance Guarantee ‣ Wasserstein Distributionally Robust Stochastic Control: A Data-Driven Approach").^66^6The constants $c_{1}$ and $c_{2}$ in Theorem 2....
