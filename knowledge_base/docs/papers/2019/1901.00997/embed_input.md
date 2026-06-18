Concentration Bounds for CVaR Estimation: The Cases of Light-tailed and Heavy-tailed Distributions

Topics include Bandits, Optimization, Concentration bounds, Conditional value at risk, Random variable.

Conditional Value-at-Risk (CVaR) is a widely used risk metric in applications such as finance. We derive concentration bounds for CVaR estimates, considering separately the cases of light-tailed and heavy-tailed distributions. In the light-tailed case, we use a classical CVaR estimator based on the empirical distribution constructed from the samples. For heavy-tailed random variables, we assume a mild `bounded moment' condition, and derive a concentration bound for a truncation-based estimator. Notably, our concentration bounds enjoy an exponential decay in the sample size, for heavy-tailed as well as light-tailed distributions. To demonstrate the applicability of our concentration results, we consider a CVaR optimization problem in a multi-armed bandit setting. Specifically, we address the best CVaR-arm identification problem under a fixed budget. We modify the well-known successive rejects algorithm to incorporate a CVaR-based criterion. Using the CVaR concentration result, we derive an upper-bound on the probability of incorrect identification by the proposed algorithm.

## Introduction

In applications such as portfolio optimization in finance, the quality of a portfolio is not satisfactorily captured by the expected value of return. Indeed, in such applications, a more risk-sensitive metric is desirable, so as to capture typical losses in the case of adverse events. Value-at-Risk (VaR) and Conditional-Value-at-Risk (CVaR) are two risk-aware metrics, which are widely used in applications such as portfolio optimization and insurance.

In this paper, we derive concentration bounds for CVaR estimators, for both light-tailed and heavy-tailed random variables. For light-tailed distributions, our concentration bound uses a classical CVaR estimator based on the empirical distribution. For the heavy-tailed case, we employ a truncation-based CVaR estimator, and derive a concentration result under a mild assumption: the $p$th moment of the distribution is assumed to exist, for some ${p > 1}.$ Notably, our concentration bounds enjoy an exponential decay in the sample size, for heavy-tailed as well as light-tailed distributions.

In order to highlight an important application for our CVaR concentration results, we consider a stochastic bandit set-up with a risk-sensitive metric for measuring the quality of an arm. In particular, we consider a $K$-armed stochastic bandit setting, and study the problem of finding the arm with the *lowest CVaR value* (at a fixed level $\alpha \in $) in a fixed budget setting. We propose an algorithm for the best CVaR arm identification that is inspired by successive-rejects. Using our CVaR concentration bound, we establish an upper bound on the probability of incorrect arm identification by our algorithm at the end of the given budget.

## CVaR estimation: Light-tailed case

In this section, we define empirical CVaR, provide a concentration result for CVaR estimation assuming that the underlying distribution is light-tailed, and subsequently present a multi-armed bandit application.
