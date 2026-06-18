Learning with Little Mixing

We study square loss in a realizable time-series framework with martingale difference noise. Our main result is a fast rate excess risk bound which shows that whenever a trajectory hypercontractivity condition holds, the risk of the least-squares estimator on dependent data matches the iid rate order-wise after a burn-in time. In comparison, many existing results in learning from dependent data have rates where the effective sample size is deflated by a factor of the mixing-time of the underlying process, even after the burn-in time. Furthermore, our results allow the covariate process to exhibit long range correlations which are substantially weaker than geometric ergodicity. We call this phenomenon learning with little mixing, and present several examples for when it occurs: bounded function classes for which the L^ and L^+epsilon norms are equivalent, ergodic finite state Markov chains, various parametric models, and a broad family of infinite dimensional ell^(N) ellipsoids....

## Introduction

Consider regression in the context of the time-series model:

Such models are ubiquitous in applications of machine learning, signal processing, econometrics, and control theory. In our setup, the learner is given access to $T \in {\mathbb{N}}_{+}$ pairs ${\{{(X_{t},Y_{t})}\}}_{t = 0}^{T - 1}$ drawn from the model (1.1), and is asked to output a hypothesis $\hat{f}$ from a hypothesis class $\mathcal{F}$ which best approximates the (realizable) regression function $f_{\star} \in \mathcal{F}$ in terms of square loss.

We developed a framework for showing when the mixing-time of the covariates plays a relatively small role in the rate of convergence of the least-squares estimator. In many situations, after a finite burn-in time, this learning procedure exhibits an excess risk that scales as if all the samples were independent (Theorem 4.1). As a byproduct of our framework, by instantiating our results to system identification for dynamics with generalized linear model transitions (Section 7.2), we derived the sharpest known excess risk rate for this problem; our rates are nearly minimax optimal after only a polynomial burn-in time.

To arrive at Theorem 4.1, we leveraged insights from Mendelson via a one-sided concentration inequality (Theorem 5.2). As mentioned in Section 4.1, hypercontractivity is closely related to the small-ball condition. Such conditions can be understood as quantitative identifiability conditions by providing control of the "version space" (cf. Mendelson )....

### Theorem 5.2

In particular, this bound only depends on $\mathcal{F}_{\star}$ and is *independent* of ${\|{\Gamma_{\mathsf{d}\mathsf{e}\mathsf{p}}{(\mathsf{P}_{X})}}\|}_{\mathsf{o}\mathsf{p}}^{2}$. Furthermore, (4.5) coincides with the corresponding risk bound for the LSE with iid covariates.

## System identification in parametric classes

In this work, we study the least-squares estimator (LSE). This procedure minimizes the empirical risk associated to the square loss over the class $\mathcal{F}$. When each pair of observations $(X_{t},Y_{t})$ is drawn iid from some fixed distribution, this procedure is minimax optimal over a broad set of hypothesis classes (Tsybakov Lecué and Mendelson Mendelson Wainwright, )....
