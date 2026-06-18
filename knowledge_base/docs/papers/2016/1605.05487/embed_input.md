Chebyshev Inequalities for Products of Random Variables

We derive sharp probability bounds on the tails of a product of symmetric non-negative random variables using only information about their first two moments. If the covariance matrix of the random variables is known exactly, these bounds can be computed numerically using semidefinite programming. If only an upper bound on the covariance matrix is available, the probability bounds on the right tails can be evaluated analytically. The bounds under precise and imprecise covariance information coincide for all left tails as well as for all right tails corresponding to quantiles that are either sufficiently small or sufficiently large. We also prove that all left probability bounds reduce to the trivial bound 1 if the number of random variables in the product exceeds an explicit threshold. Thus, in the worst case, the weak-sense geometric random walk defined through the running product of the random variables is absorbed at 0 with certainty as soon as time exceeds the given threshold. The techniques devised for constructing Chebyshev bounds for products can also be used to derive Chebyshev bounds for sums, maxima and minima of non-negative random variables.

## Introduction

The classical one-sided Chebyshev inequality for a random variable $\overset{\sim}{\xi}$ with mean $\mu$ and variance $\sigma^{2}$ can be represented as

This inequality is sharp. Indeed, for $\gamma \neq \mu$ it is binding under the two-point distribution

Figure 5 reports the worst-case value-at-risk of two portfolios over different time horizons $T$, where $\mathbf{μ}$ and $\mathbf{\Sigma}$ are calibrated to the 2003--2012 period of Fama and French's 10 Industry Portfolios data set.^22^2See library.html. The minimum-variance portfolio (left graph) corresponds to the weight vector ${\mathbf{w}} \in \mathcal{W}$ that minimizes ${\mathbf{w}}^{\intercal}\mathbf{\Sigma}{\mathbf{w}}$, whereas the maximum-expectation portfolio (right graph) invests all wealth into the asset $i$ with the highest expected return $\mu_{i}$....

In addition to *evaluating* the worst-case value-at-risk of a pre-selected portfolio $\mathbf{w}$, an investor often seeks to determine a portfolio ${\mathbf{w}}^{\star}$ that *optimizes* the worst-case value-at-risk. The search for optimal portfolios is greatly simplified by the observation that there is always a portfolio ${\mathbf{w}}^{\star}$ on the mean-variance efficient frontier that maximizes $\text{WVaR}_{\epsilon}({\mathbf{w}})$ over (subsets of) $\mathcal{W}$....

Keeping the scenario probabilities as well as the scenario-wise arithmetic and quadratic means constant, we first replace each ${\mathbf{ξ}}^{k}$ with a minimizer of the problem

As $s \in \left\lbrack 0,{T\gamma^{1/T}} \right\rbrack$ iff ${s\left( {{T\gamma^{1/T}} - s} \right)} \geq 0$, we can once again use the $\mathcal{S}$-lemma to show that (18a) holds iff there exists $\lambda_{3} \geq 0$ with

### Proposition 4.1

In the degenerate case $\gamma = \mu$, the inequality is still sharp because the distributions

If we have the extra information that the random variable $\overset{\sim}{\xi}$ is non-negative (and without much loss of generality that $\mu > 0$), then one can strengthen the Chebyshev inequality to

see, e.g.,. The extremal distributions are supported on the non-negative real line if either $\gamma \geq {\mu + \left. \sigma^{2}/\mu \right.} > \mu$ or if $\gamma < \mu$. Thus, they certify the sharpness of in the respective parameter domains. For $\mu \leq \gamma < {\mu + \left....
