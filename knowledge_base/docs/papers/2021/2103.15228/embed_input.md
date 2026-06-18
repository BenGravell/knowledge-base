Anomaly Detection under Multiplicative Noise Model Uncertainty

Topics include Cyber-physical systems, Anomaly detection, Attack detection, Robust state estimation, Linear quadratic Gaussian control, Multiplicative noise, Model uncertainty, Stochastic systems, State-space models, Kalman filtering, Robust filtering, Sensor attacks, False data injection, Detection performance, Uncertainty-aware estimation, Resilient control systems, Secure control, Numerical simulation.

Uses the multiplicative-noise control design framework in order to control an uncertain system using output measurement feedback and monitor for excessive output residuals (anomaly detection).

State estimators are crucial components of anomaly detectors that are used to monitor cyber-physical systems. Many frequently-used state estimators are susceptible to model risk as they rely critically on the availability of an accurate state-space model. Modeling errors make it more difficult to distinguish whether deviations from expected behavior are due to anomalies or simply a lack of knowledge about the system dynamics. In this research, we account for model uncertainty through a multiplicative noise framework. Specifically, we propose to use the multiplicative noise LQG based compensator in this setting to hedge against the model uncertainty risk. The size of the residual from the estimator can then be compared against a threshold to detect anomalies. Finally, the proposed detector is validated using numerical simulations. Extension of state-of-the-art anomaly detection in cyber-physical systems to handle model uncertainty represents the main novel contribution of the present work.

## Introduction

Cyber-Physical Systems (CPS) are physical processes that are tightly integrated with computation and communication systems for monitoring and control. Though advances in CPS design has equipped them with adaptability, resiliency, safety, and security features that exceed the simple embedded systems of the past, it often leaves open several points for attackers to strike. CPS security problems have attracted the attention of researchers worldwide recently; some state-of-the-art anomaly detection algorithms can be found in.

A common practice is to model a CPS as either a deterministic system or a stochastic system with additive Gaussian uncertainties. Motivated by the recent developments in distributionally robust optimization (DRO) techniques, authors in have developed DRO anomaly detectors that remove assumptions on specific functional forms of the uncertainties in the stochastic CPS model. On the other hand, it is a common practice to assume that the true CPS dynamics are known exactly....

## Conclusion

An extension of the state-of-the-art anomaly detection algorithms for CPS with modeling errors via the multiplicative noise framework was discussed in this paper. The multiplicative noise-driven LQG being a robust state estimator was used to hedge against the model risk to construct the state estimate. The proposed method was demonstrated using a numerical simulation....

It is necessary to account for the multiplicative noise to achieve the minimum quadratic cost; furthermore, it is straightforward to find systems in and which are *mean-square unstable* when controlled by (multiplicative-noise-ignorant) LQG, meaning that it is necessary to account for multiplicative noise to achieve mean-square stability.

The optimal state estimator at any time $k$ given and is an affine^22^2It is possible to design a nonlinear state estimator to outperform a given affine estimator in this setting. However, it is out of the scope of this paper. function of the output $y_{k}$.

Finally, using the matrix reshaping operator $\text{mat}{( \cdot )}$, we retrieve the steady state $\Sigma_{r}$ as follows

State estimation is a crucial component in any model-based anomaly detector design, which depends on a state-space model for the system dynamics....
