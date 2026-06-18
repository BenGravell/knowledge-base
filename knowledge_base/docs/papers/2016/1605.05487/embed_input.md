Chebyshev Inequalities for Products of Random Variables

We derive sharp probability bounds on the tails of a product of symmetric non-negative random variables using only information about their first two moments. If the covariance matrix of the random variables is known exactly, these bounds can be computed numerically using semidefinite programming. If only an upper bound on the covariance matrix is available, the probability bounds on the right tails can be evaluated analytically. The bounds under precise and imprecise covariance information coincide for all left tails as well as for all right tails corresponding to quantiles that are either sufficiently small or sufficiently large. We also prove that all left probability bounds reduce to the trivial bound 1 if the number of random variables in the product exceeds an explicit threshold. Thus, in the worst case, the weak-sense geometric random walk defined through the running product of the random variables is absorbed at 0 with certainty as soon as time exceeds the given threshold. The techniques devised for constructing Chebyshev bounds for products can also be used to derive Chebyshev bounds for sums, maxima and minima of non-negative random variables.

## Introduction

The classical one-sided Chebyshev inequality for a random variable $\overset{\sim}{\xi}$ with mean $\mu$ and variance $\sigma^{2}$ can be represented as

This inequality is sharp. Indeed, for $\gamma \neq \mu$ it is binding under the two-point distribution

In the degenerate case $\gamma = \mu$, the inequality is still sharp because the distributions

If we have the extra information that the random variable $\overset{\sim}{\xi}$ is non-negative (and without much loss of generality that $\mu > 0$), then one can strengthen the Chebyshev inequality to

In this paper we aim to derive Chebyshev inequalities for products of non-negative random variables. Specifically, we will derive sharp upper bounds on the left and right tail probabilities ${\mathbb{P}}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \leq \gamma} \right)$ and ${\mathbb{P}}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \geq \gamma} \right)$, respectively. Products of random variables frequently arise in physics, statistics, finance, number theory and many other branches of science. Indeed, they are at the heart of stochastic models of many complex phenomena.
