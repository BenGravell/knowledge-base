Learning with Little Mixing

We study square loss in a realizable time-series framework with martingale difference noise. Our main result is a fast rate excess risk bound which shows that whenever a trajectory hypercontractivity condition holds, the risk of the least-squares estimator on dependent data matches the iid rate order-wise after a burn-in time. In comparison, many existing results in learning from dependent data have rates where the effective sample size is deflated by a factor of the mixing-time of the underlying process, even after the burn-in time. Furthermore, our results allow the covariate process to exhibit long range correlations which are substantially weaker than geometric ergodicity. We call this phenomenon learning with little mixing, and present several examples for when it occurs: bounded function classes for which the L^ and L^+epsilon norms are equivalent, ergodic finite state Markov chains, various parametric models, and a broad family of infinite dimensional ell^(N) ellipsoids.

## Introduction

Consider

Such models are ubiquitous in applications of machine learning, signal processing, econometrics, and control theory. In our setup, the learner is given access to $T \in {\mathbb{N}}_{+}$ pairs ${\{{(X_{t},Y_{t})}\}}_{t = 0}^{T - 1}$ drawn from the model (1.1), and is asked to output a hypothesis $\hat{f}$ from a hypothesis class $\mathcal{F}$ which best approximates the (realizable) regression function $f_{\star} \in \mathcal{F}$ in terms of square loss.

With this in mind, we seek to extend our understanding of the minimax optimality of the LSE for the time-series model (1.1). We show that for a broad class of function spaces and covariate processes, the effects of data dependency across time enter the LSE excess risk only as a higher order term, whereas the leading term in the excess risk remains order-wise identical to that in the iid setting. Hence, after a sufficiently long, but finite *burn-in time*, the LSE's excess risk scales as if all $T$ samples are independent. This behavior applies to processes that exhibit correlations which decay slower than geometrically.

## Conclusion

We developed a framework for showing when the mixing-time of the covariates plays a relatively small role in the rate of convergence of the least-squares estimator. In many situations, after a finite burn-in time, this learning procedure exhibits an excess risk that scales as if all the samples were independent (Theorem 4.1). As a byproduct of our framework, by instantiating our results to system identification for dynamics with generalized linear model transitions (Section 7.2), we derived the sharpest known excess risk rate for this problem; our rates are nearly minimax optimal after only a polynomial burn-in time.

To arrive at Theorem 4.1, we leveraged insights from Mendelson via a one-sided concentration inequality (Theorem 5.2). As mentioned in Section 4.1, hypercontractivity is closely related to the small-ball condition. Such conditions can be understood as quantitative identifiability conditions by providing control of the "version space" (cf. Mendelson ).
