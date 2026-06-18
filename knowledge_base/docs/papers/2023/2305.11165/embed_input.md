The Noise Level in Linear Regression with Dependent Data

We derive upper bounds for random design linear regression with dependent (beta-mixing) data absent any realizability assumptions. In contrast to the strictly realizable martingale noise regime, no sharp instance-optimal non-asymptotics are available in the literature. Up to constant factors, our analysis correctly recovers the variance term predicted by the Central Limit Theorem - the noise level of the problem - and thus exhibits graceful degradation as we introduce misspecification. Past a burn-in, our result is sharp in the moderate deviations regime, and in particular does not inflate the leading order term by mixing time factors.

## Introduction

Ordinary least squares (OLS) regression from a finite sample is one of the most ubiquitous and widely used technique in machine learning. When faced with independent data, there are now sharp tools available to analyze its success optimally under relatively general assumptions. Indeed, a non-asymptotic theory matching the classical asymptotically optimal understanding from statistics has been developed over the last decade. However, once we relax the independence assumption and move toward data that exhibits correlations, the situation is much less well-understood---even for a problem as seemingly simple as linear regression....

In this paper, we study the instance-specific performance of ordinary least squares in a setting with dependent data---and in contrast to much contemporary work on the theme---without imposing realizability.^11^1A distribution $\mathsf{P}_{X,Y}$ is (linearly) realizable if the regression function $x\mapsto{\mathbf{E}{\lbrack{{Y \mid X} = x}\rbrack}}$ is linear. If in addition to a realizability assumption the noise forms a martingale difference sequence, it is now well-known that martingale methods can be used to demonstrate that dependent linear regression is no harder than its independent counterpart....

The lower tail of the empirical covariance matrix (2.9) is well-behaved under mild assumptions. In an excess risk bound, the contribution of the lower uniform law to the overall error is not of leading order. Hence, incurring a sample size deflation for this purpose is not critical.

By combining blocking with a version of Bernstein's inequality, we are able to push the effect of blocking to only affect the large deviations regime. In the moderate and small deviations regimes, control of the leading order of the random walk in (2.7) is not directly impacted by slow mixing.

as long as the following burn-in conditions hold:

### The Noise Term

we incur an additional burn-in penalizing slow mixing---the last part of (3.7) asks that the block-length is not \"too small\".

However, barring any such strong realizability assumption, martingale methods are no longer directly available, and neither are there any sharp non-asymptotics in the learning theory literature....
