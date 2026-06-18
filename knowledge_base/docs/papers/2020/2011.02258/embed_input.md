Concentration Inequalities for Statistical Inference

Topics include Regression, Statistical inference, Poisson regression.

This paper gives a review of concentration inequalities which are widely employed in non-asymptotical analyses of mathematical statistics in a wide range of settings, from distribution-free to distribution-dependent, from sub-Gaussian to sub-exponential, sub-Gamma, and sub-Weibull random variables, and from the mean to the maximum concentration. This review provides results in these settings with some fresh new results. Given the increasing popularity of high-dimensional data and inference, results in the context of high-dimensional linear and Poisson regressions are also provided. We aim to illustrate the concentration inequalities with known constants and to improve existing bounds with sharper constants.

## Introduction

In probability theory and statistical inference, researchers often need to bound the probability of a difference between a random quantity from its target, usually the error bound of estimation. Concentration inequalities (CIs) are tools for attaining such bounds, and play important roles in deriving theoretical results for various inferential situations in statistics and probability. The recent developments in high-dimensional (HD) statistical inference, and statistical and machine learning have generated renewed interests in the CIs, as reflected in Koltchinskii, Vershynin, Wainwright and Fan et al..

CIs enable us to obtain non-asymptotic results for estimating, constructing confidence intervals, and doing hypothesis testing with a high-probability guarantee. For example, the first-order optimized condition for HD linear regressions should be held with a high probability to guarantee the well-behavior of the estimator. The concentration inequality for error distributions is to ensure the concentration from first-order optimized conditions to the estimator.

where $Z_{n}:={f{(X_{1},\cdots,X_{n})}}$ and $X_{1},\cdots,X_{n}$ are random variables. We present two types of CIs: distribution-free and distribution-dependent. Distribution free CIs are free of distribution assumptions, while the distribution-dependent CIs are based on exponential moment conditions reflecting the tail property for the particular class of distributions.

The review is organized as follows. Section 2 outlines distribution-free CIs. CIs for Sub-Gaussian, Sub-exponential, sub-Gamma, and sub-Weibull random variables are given in Section 3, 4, 5, and 6 respectively. Section 7 reports concentration for the maximal of random variables and suprema of empirical processes. Applications for high dimensional linear and Poisson regression are outlined in Section 8. Section 9 discusses extensions to other settings.
