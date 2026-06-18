Sample Complexity of Kalman Filtering for Unknown Systems

In this paper, we consider the task of designing a Kalman Filter (KF) for an unknown and partially observed autonomous linear time invariant system driven by process and sensor noise. To do so, we propose studying the following two step process: first, using system identification tools rooted in subspace methods, we obtain coarse finite-data estimates of the state-space parameters and Kalman gain describing the autonomous system; and second, we use these approximate parameters to design a filter which produces estimates of the system state. We show that when the system identification step produces sufficiently accurate estimates, or when the underlying true KF is sufficiently robust, that a Certainty Equivalent (CE) KF, i.e., one designed using the estimated parameters directly, enjoys provable sub-optimality guarantees. We further show that when these conditions fail, and in particular, when the CE KF is marginally stable (i.e., has eigenvalues very close to the unit circle), that imposing additional robustness constraints on the filter leads to similar sub-optimality guarantees....

## Introduction

Time series prediction is a fundamental problem across control theory, economics and machine learning. In the case of autonomous linear time invariant (LTI) systems driven by Gaussian process and sensor noise:

the celebrated Kalman Filter (KF) has been the standard method for prediction. When model is known, the KF minimizes the mean square prediction error. However, in many practical cases of interest (e.g., tracking moving objects, stock price forecasting), the state-space parameters are not known and must be learned from time-series data. This system identification step, based on a finite amount of data, inevitably introduces parametric errors in model, which leads to a KF with suboptimal prediction performance.

## Conclusions & Future work

In this paper, we proposed and analyzed a system identification and filter synthesis pipeline. Leveraging contemporary finite data guarantees from system identification, as well as novel parameterizations of robust Kalman filters, we provided, to the best of our knowledge, the first end-to-end sample complexity bounds for the Kalman filtering of an unknown autonomous LTI system. Our analysis revealed that, depending on the spectral properties of the CE Kalman filter, a robust Kalman filter approach may lead to improved performance....

### Theorem 3.1 (Near Optimal Certainty Equivalent Kalman Filtering)

Fix a failure probability $\delta > 0$. Given a single trajectory $y_{0},\ldots,y_{N}$ of system, compute system parameter estimates $\hat{A},\hat{C},\hat{K},\hat{R}$, and design a Kalman filter in class, defined by gains $\left\{ L_{t} \right\}_{t = 1}^{\infty}$, such that with probability at least $1 - \delta$, we have that $\overset{\sim}{J} \leq \epsilon_{J}$, so long as $N \geq {{poly}{({1/\epsilon_{J}},{\log{({1/\delta})}})}}$.

where the constant $\mathcal{C}$ is a regularization parameter, and the affine constraint ${{{\mathbf{\Phi}_{w}{({{zI} - \hat{A}})}} - {\mathbf{\Phi}_{v}\hat{C}}} = {I,\mathbf{\Phi}_{w}}},{\mathbf{\Phi}_{v} \in {\frac{1}{z}\mathcal{R}\mathcal{H}_{\infty}}}$ parameterizes all filters of the form that have bounded mean squared prediction error (see Wang et al. for more details)....
