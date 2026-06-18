Concentration Bounds for CVaR Estimation: The Cases of Light-tailed and Heavy-tailed Distributions

Topics include Bandits, Optimization, Concentration bounds, Conditional value at risk, Random variable.

Conditional Value-at-Risk (CVaR) is a widely used risk metric in applications such as finance. We derive concentration bounds for CVaR estimates, considering separately the cases of light-tailed and heavy-tailed distributions. In the light-tailed case, we use a classical CVaR estimator based on the empirical distribution constructed from the samples. For heavy-tailed random variables, we assume a mild `bounded moment' condition, and derive a concentration bound for a truncation-based estimator. Notably, our concentration bounds enjoy an exponential decay in the sample size, for heavy-tailed as well as light-tailed distributions. To demonstrate the applicability of our concentration results, we consider a CVaR optimization problem in a multi-armed bandit setting. Specifically, we address the best CVaR-arm identification problem under a fixed budget. We modify the well-known successive rejects algorithm to incorporate a CVaR-based criterion. Using the CVaR concentration result, we derive an upper-bound on the probability of incorrect identification by the proposed algorithm.

## Introduction

In applications such as portfolio optimization in finance, the quality of a portfolio is not satisfactorily captured by the expected value of return. Indeed, in such applications, a more risk-sensitive metric is desirable, so as to capture typical losses in the case of adverse events. Value-at-Risk (VaR) and Conditional-Value-at-Risk (CVaR) are two risk-aware metrics, which are widely used in applications such as portfolio optimization and insurance....

In this paper, we derive concentration bounds for CVaR estimators, for both light-tailed and heavy-tailed random variables. For light-tailed distributions, our concentration bound uses a classical CVaR estimator based on the empirical distribution. For the heavy-tailed case, we employ a truncation-based CVaR estimator, and derive a concentration result under a mild assumption: the $p$th moment of the distribution is assumed to exist, for some ${p > 1}.$ Notably, our concentration bounds enjoy an exponential decay in the sample size, for heavy-tailed as well as light-tailed distributions....

## Concluding Remarks

We derived concentration bounds for CVaR estimation, separately considering light-tailed and heavy-tailed distributions. For light-tailed distributions, our concentration bound uses a classical CVaR estimator based on the empirical distribution. For the heavy-tailed case, we employ a truncation based CVaR estimator, and derive a concentration result under a mild bounded-moment assumption. Our concentration bound enjoys exponential decay in the sample size even for heavy-tailed random variables. We highlighted the applicability of the CVaR concentration result by considering a risk-aware best bandit arm selection problem....

In, $B_{i}$ represents a truncation level of $X_{i}$, and the choice for $B_{i}$ given above is under the assumption that ${{\mathbb{E}}\left\lbrack |X|^{p} \right\rbrack} < u < \infty$ for some $p \in (1,2\rbrack$. Such a truncation based estimator has been employed in the context of expected regret minimization with heavy-tailed random variables in. Intuitively, the truncation level serves to discard very large samples values early on, as $B_{i}$ is set to grow slowly with $i.$

The bound in the theorem above is significantly better than the two-sided bound obtained in for the light-tailed case....
