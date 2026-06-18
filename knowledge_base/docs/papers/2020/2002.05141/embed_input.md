Online Learning of the Kalman Filter with Logarithmic Regret

In this paper, we consider the problem of predicting observations generated online by an unknown, partially observed linear system, which is driven by stochastic noise. For such systems the optimal predictor in the mean square sense is the celebrated Kalman filter, which can be explicitly computed when the system model is known. When the system model is unknown, we have to learn how to predict observations online based on finite data, suffering possibly a non-zero regret with respect to the Kalman filter's prediction. We show that it is possible to achieve a regret of the order of polylog(N) with high probability, where N is the number of observations collected. Our work is the first to provide logarithmic regret guarantees for the widely used Kalman filter. This is achieved using an online least-squares algorithm, which exploits the approximately linear relation between future observations and past observations. The regret analysis is based on the stability properties of the Kalman filter, recent statistical tools for finite sample analysis of system identification, and classical results for the analysis of least-squares algorithms for time series....

## Introduction

The celebrated Kalman filter has been a fundamental approach for estimation and prediction of time-series data, with diverse applications ranging from control systems and robotics to computer vision and economics. Given a known system model with known noise statistics, the Kalman filter predicts future observations of a *partially observable* dynamical process by filtering past observations. When the underlying process is linear and the noise is Gaussian, the Kalman filter is optimal in the sense that it minimizes the mean square prediction error....

Learning to predict unknown partially observed systems is a significantly more challenging problem. Even in the case of linear systems, learning directly the model parameters of the system results in nonlinear, non-convex problems. Adaptive filtering algorithms address the problem of making observation predictions when the system model or the noise statistics are unknown or changing. These adaptive filtering approaches are usually based on variations of extended least squares....

In this paper, we provided the first logarithmic regret upper bounds for learning the classical Kalman filter of an unknown system with unknown stochastic noise. Our regret analysis holds for non-explosive systems and our bounds do not degrade with the system stability gap.

Going forward, our paper opens up several research directions. An open question that is whether we can define an appropriate regret notion in the case of state prediction, when matrices $A,C$ are unknown, and prove logarithmic bounds. Another interesting direction is to study how the learning performance is affected by system theoretic properties, such as the exponential quantity $d^{\kappa}$ in the case of systems with long chain structure, e.g. $\kappa$-order integrators. Analyzing the regret of other online algorithms, e.g. extended least squares, is also an open problem....

## Regret Analysis

We assume that the initial state covariance is $\Sigma_{0} = P$, where $P$ is defined in (7. ‣ 2.1 Kalman Filter Background ‣ 2 Problem Formulation ‣ Online Learning of the Kalman Filter with Logarithmic Regret")).

The key ingredients to analyze the cumulative error $\mathcal{L}_{N}$ are i) the stability properties of the closed-loop matrix $A - {KC}$; ii) self-normalization properties of predictor; and iii) persistency of excitation for the past...
