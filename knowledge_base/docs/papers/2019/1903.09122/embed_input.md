Finite Sample Analysis of Stochastic System Identification

Topics include Robustness, Kalman filtering, System identification, Sample complexity, Learning, Kalman filter.

In this paper, we analyze the finite sample complexity of stochastic system identification using modern tools from machine learning and statistics. An unknown discrete-time linear system evolves over time under Gaussian noise without external inputs. The objective is to recover the system parameters as well as the Kalman filter gain, given a single trajectory of output measurements over a finite horizon of length N. Based on a subspace identification algorithm and a finite number of N output samples, we provide non-asymptotic high-probability upper bounds for the system parameter estimation errors. Our analysis uses recent results from random matrix theory, self-normalized martingales and SVD robustness, in order to show that with high probability the estimation errors decrease with a rate of 1/sqrt(N). Our non-asymptotic bounds not only agree with classical asymptotic results, but are also valid even when the system is marginally stable.

## Introduction

Identifying predictive models from data has been a fundamental problem across several fields, from classical control theory to economics and modern machine learning. System identification, in particular, has a long history of studying this problem from a control theoretic perspective. Identifying linear state-space models:

from input-output data has been the focus of time-domain identification. In fact, some identification algorithms can not only learn the system matrices in but also the Kalman filter required for state estimation.

We could also provide finite sample bounds for the estimation of the closed-loop matrix $A_{c} \triangleq {A - {KC}}$. This can be done in two ways. One option is to form matrix $\hat{A} - {\hat{K}\hat{C}}$ from the estimates $\hat{A},\hat{C},\hat{K}$. Alternatively, we could estimate $\hat{A_{c}}$ directly from ${\hat{\mathcal{K}}}_{p}$ in the same way that we estimated $\hat{A}$. However, we do not have finite sample guarantees for the stability of the closed-loop estimates $\hat{A} - {\hat{K}\hat{C}}$, $\hat{A_{c}}$. It would be interesting to address this in future work.

Another direction for future work is repeating the analysis when the Kalman filter has not reached steady-state, i.e. relax Assumption 2. Finally, in this work, we only considered upper bounds. It would be interesting to study lower bounds as well to evaluate the tightness of our upper bounds. In any case, from lower bounds for fully observed systems, the factor of $1/\sqrt{N}$ is tight.

The least singular value of the above matrix is denoted by:

Finally, for any $s \geq 2$, define block-Toeplitz matrix:

Establishing bounds for the the Kalman truncation error in (29. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification")).

Most identification methods for linear systems either follow the prediction error approach or the subspace method. The prediction error approach is usually non-convex and directly searches over the system parameters $A,B,C,D$ by minimizing a prediction error cost. The subspace approach is a convex one; first, Hankel matrices of the system are estimated, then, the parameters are realized via steps involving singular value decomposition (SVD). Methods inspired by machine learning have also also been employed....
