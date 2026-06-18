Finite Sample Analysis of Stochastic System Identification

Topics include Robustness, Kalman filtering, System identification, Sample complexity, Learning, Kalman filter.

In this paper, we analyze the finite sample complexity of stochastic system identification using modern tools from machine learning and statistics. An unknown discrete-time linear system evolves over time under Gaussian noise without external inputs. The objective is to recover the system parameters as well as the Kalman filter gain, given a single trajectory of output measurements over a finite horizon of length N. Based on a subspace identification algorithm and a finite number of N output samples, we provide non-asymptotic high-probability upper bounds for the system parameter estimation errors. Our analysis uses recent results from random matrix theory, self-normalized martingales and SVD robustness, in order to show that with high probability the estimation errors decrease with a rate of 1/sqrt(N). Our non-asymptotic bounds not only agree with classical asymptotic results, but are also valid even when the system is marginally stable.

## Introduction

Identifying predictive models from data has been a fundamental problem across several fields, from classical control theory to economics and modern machine learning. System identification, in particular, has a long history of studying this problem from a control theoretic perspective.

from input-output data has been the focus of time-domain identification. In fact, some identification algorithms can not only learn the system matrices in but also the Kalman filter required for state estimation.

Most identification methods for linear systems either follow the prediction error approach or the subspace method. The prediction error approach is usually non-convex and directly searches over the system parameters $A,B,C,D$ by minimizing a prediction error cost. The subspace approach is a convex one; first, Hankel matrices of the system are estimated, then, the parameters are realized via steps involving singular value decomposition (SVD). Methods inspired by machine learning have also also been employed. In this paper, we focus on the subspace identification approach--see for an overview.

In this paper, we perform the first finite sample analysis of system in the case ${B,D} = 0$, when we have no inputs, also known as stochastic system identification (SSI). This problem is more challenging than the case ${B,D} \neq 0$, since the system can only be driven through noise and establishing persistence of excitation is harder. We provide the first non-asymptotic guarantees for the estimation of matrices $A,C$ as well as the Kalman filter gain of. Similar to, the analysis is based on new tools from machine learning and statistics.

## Discussion and Future Work

One of the main differences between the subspace algorithm considered in this paper and other stochastic subspace identification algorithms is the SVD step. The other algorithms perform SVD on $W_{1}GW_{2}$ instead of $G$, where $W_{1},W_{2}$ are full rank weighting matrices, possibly data dependent. From this point of view, the results of Section 4 (upper bound for $\|{G - \hat{G}}\|$ in Theorem 1. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification") and persistence of excitation in Theorem 2.
