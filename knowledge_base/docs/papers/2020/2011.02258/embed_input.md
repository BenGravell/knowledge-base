Concentration Inequalities for Statistical Inference

Topics include Regression, Statistical inference, Poisson regression.

This paper gives a review of concentration inequalities which are widely employed in non-asymptotical analyses of mathematical statistics in a wide range of settings, from distribution-free to distribution-dependent, from sub-Gaussian to sub-exponential, sub-Gamma, and sub-Weibull random variables, and from the mean to the maximum concentration. This review provides results in these settings with some fresh new results. Given the increasing popularity of high-dimensional data and inference, results in the context of high-dimensional linear and Poisson regressions are also provided. We aim to illustrate the concentration inequalities with known constants and to improve existing bounds with sharper constants.

## Introduction

In probability theory and statistical inference, researchers often need to bound the probability of a difference between a random quantity from its target, usually the error bound of estimation. Concentration inequalities (CIs) are tools for attaining such bounds, and play important roles in deriving theoretical results for various inferential situations in statistics and probability. The recent developments in high-dimensional (HD) statistical inference, and statistical and machine learning have generated renewed interests in the CIs, as reflected in Koltchinskii, Vershynin, Wainwright and Fan et al.....

CIs enable us to obtain non-asymptotic results for estimating, constructing confidence intervals, and doing hypothesis testing with a high-probability guarantee. For example, the first-order optimized condition for HD linear regressions should be held with a high probability to guarantee the well-behavior of the estimator. The concentration inequality for error distributions is to ensure the concentration from first-order optimized conditions to the estimator. Our review focuses on four types of CIs:

Testing hypotheses on the regression coefficients are a necessity in measuring the effects of covariates on the certain response variables. Scientists are interested in testing the significance of a large number of covariates simultaneously. From this backgrounds, Zhong and Chen proposed simultaneous tests for coefficients in HD linear models under the "large $p$, small $n$" situations by U-statistics motivated by Chen and Qin. However, their HD tests are asymptotical without a non-asymptotic guarantee....

In future, it would be essential and practical to study the estimator for the sub-exponential, sub-Gaussian, sub-Weibull and GBO norms as the unknown parameters when constructing non-asymptotical and data-driven confidence intervals; see Zhang et al.; Wang et al.; Zhou et al..

### Lemma 5.14 (Analytic property of MGF in the exponential family)

### Proof 4.14

The Corollary 7.2 (b) implies a tail bound for maximum of sub-Gaussian random variables for $t > 0$

where $Z_{n}:={f{(X_{1},\cdots,X_{n})}}$ and $X_{1},\cdots,X_{n}$ are random variables. We present two types of CIs: distribution-free and distribution-dependent....
