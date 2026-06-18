Fastest Convergence for Q-learning

The Zap Q-learning algorithm introduced in this paper is an improvement of Watkins' original algorithm and recent competitors in several respects. It is a matrix-gain algorithm designed so that its asymptotic variance is optimal. Moreover, an ODE analysis suggests that the transient behavior is a close match to a deterministic Newton-Raphson implementation. This is made possible by a two time-scale update equation for the matrix gain sequence. The analysis suggests that the approach will lead to stable and efficient computation even for non-ideal parameterized settings. Numerical experiments confirm the quick convergence, even in such non-ideal cases. A secondary goal of this paper is tutorial. The first half of the paper contains a survey on reinforcement learning algorithms, with a focus on minimum variance algorithms.

## Introduction

It is recognized that algorithms for reinforcement learning such as TD- and Q-learning can be slow to converge. The poor performance of Watkins' Q-learning algorithm was first quantified in, and since then many papers have appeared with proposed improvements, such as.

An emphasis in much of the literature is computation of finite-time PAC (probably almost correct) bounds as a metric for performance. Explicit bounds were obtained in for Watkins' algorithm, and in for the "speedy" Q-learning algorithm that was introduced by these authors. A general theory is presented in for stochastic approximation algorithms.

Reduce complexity and potential numerical instability of matrix inversion,

Maintain optimality of the asymptotic covariance

Conditions for convergence of the Zap-Q algorithm (53 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning"),54 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")) are summarized in Thm. 3.4. The following assumption is used to address the discontinuity in the recursion for $\{{\hat{A}}_{n}\}$ resulting from the dependence of $A_{n + 1}$ on $\phi_{n}$.

### Notation and assumptions

### Lemma 3.9

In each of the models considered in prior work, the update equation for the parameter estimates can be expressed

in which $\{\alpha_{n}\}$ is a positive gain sequence, and $\{\Delta_{n}\}$ is a martingale difference sequence. This representation is critical in analysis, but unfortunately is not typical in reinforcement learning applications outside of these versions of Q-learning. For Markovian models, the usual transformation used to obtain a representation similar to results in an error sequence $\{\Delta_{n}\}$ that is the sum of a martingale difference sequence and a telescoping sequence. It is the telescoping sequence that prevents easy analysis of Markovian models.

This gap in the research literature carries over to the general theory of Markov chains. Examples of concentration bounds for i.i.d. sequences or martingale-difference sequences include the finite-time bounds of Hoeffding and Bennett. Extensions to Markovian models either offer very crude bounds, or restrictive assumptions; this remains an active area of research.
