Wasserstein Distributionally Robust Kalman Filtering

Topics include Nonconvex optimization, Robustness, Kalman filtering, Wasserstein distances, Kalman filter.

We study a distributionally robust mean square error estimation problem over a nonconvex Wasserstein ambiguity set containing only normal distributions. We show that the optimal estimator and the least favorable distribution form a Nash equilibrium. Despite the non-convex nature of the ambiguity set, we prove that the estimation problem is equivalent to a tractable convex program. We further devise a Frank-Wolfe algorithm for this convex program whose direction-searching subproblem can be solved in a quasi-closed form. Using these ingredients, we introduce a distributionally robust Kalman filter that hedges against model risk.

## Introduction

The Kalman filter is the workhorse for the online tracking and estimation of a dynamical system's internal state based on indirect observations. It has been applied with remarkable success in areas as diverse as automatic control, brain-computer interaction, macroeconomics, robotics, signal processing, weather forecasting and many more. The classical Kalman filter critically relies on the availability of an accurate state-space model and is therefore susceptible to model risk. This observation has led to several attempts to robustify the Kalman filter against modeling errors.

The $\mathcal{H}_{\infty}$-filter targets situations in which the statistics of the noise process is uncertain and where one aims to minimize the worst case instead of the variance of the estimation error. This filter bounds the $\mathcal{H}_{\infty}$-norm of the transfer function that maps the disturbances to the estimation errors. However, in transient operation, the desired $\mathcal{H}_{\infty}$-performance is lost, and the filter may diverge unless some (typically restrictive) positivity condition holds in each iteration. In set-valued estimation the disturbance vectors are modeled through bounded sets such as ellipsoids....

Under small time-invariant uncertainty (Figure 5(a)), the Wasserstein and KL distributionally robust filters display a similar steady-state performance but outperform the classical Kalman filter. Note that the KL distributionally robust filter starts from a different initial point as we use the delayed implementation from. Under small time-varying uncertainty (Figure 5(b)), both distributionally robust filters display a similar performance as the classical Kalman filter. Figures 5(c) and (d) corresponding to the case of large uncertainty are similar to Figures 5(a) and (b), respectively....

Figure 5: Empirical means square estimation error of different filters

The finite convex optimization problem (5. ‣ 2 Robust Estimation with Wasserstein Ambiguity Sets ‣ Wasserstein Distributionally Robust Kalman Filtering")) is numerically challenging as it constitutes a nonlinear semi-definite program (SDP). In principle, it would be possible to eliminate all nonlinearities by using Schur complements and to reformulate (5....
