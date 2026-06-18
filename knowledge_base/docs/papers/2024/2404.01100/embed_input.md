Finite Sample Frequency Domain Identification

We study non-parametric frequency-domain system identification from a finite-sample perspective. We assume an open loop scenario where the excitation input is periodic and consider the Empirical Transfer Function Estimate (ETFE), where the goal is to estimate the frequency response at certain desired (evenly-spaced) frequencies, given input-output samples. We show that under sub-Gaussian colored noise (in time-domain) and stability assumptions, the ETFE estimates are concentrated around the true values. The error rate is of the order of O((d_u+sqrt{d_ud_y})sqrt{M/N_tot}), where N_tot is the total number of samples, M is the number of desired frequencies, and d_u, d_y are the dimensions of the input and output signals respectively. This rate remains valid for general irrational transfer functions and does not require a finite order state-space representation. By tuning M, we obtain a N_tot^(-1/3) finite-sample rate for learning the frequency response over all frequencies in the H_infinity norm. Our result draws upon an extension of the Hanson-Wright inequality to semi-infinite matrices. We study the finite-sample behavior of ETFE in simulations.

## Introduction

We consider the identification of *unknown* linear, discrete-time, time-invariant systems of the form

Frequency domain identification has been extensively studied. The estimation error guarantees (on its distribution) are typically asymptotic, e.g. see Central Limit Theorem in \[, Ch. 16\], and, thus, are valid when the number of samples grows to infinity. Here, we adopt a finite-sample point of view, motivated by advances in modern statistics and statistical learning theory. Asymptotic methods are sharp asymptotically but are often heuristically applied for finite samples. Finite-sample bounds, on the other hand, are valid for any number of samples, but suffer from looser bounding constants.

Our

Finite-sample guarantees for the ETFE. We provide finite sample guarantees for the well-established Empirical Transfer Function Estimate (ETFE), a non-parametric method for frequency domain identification, under open-loop periodic excitation. While the mean and variance of the ETFE have been characterized before, we provide guarantees on the distribution of the estimation error, the tail probabilities in particular. Under certain stability conditions, we prove that the estimation error decays with a rate of $\sqrt{M/N_{tot}}$, where $N_{tot}$ is the total number of samples.

## Conclusion and Future Work

We provide finite-sample guarantees for the ETFE over a selected frequency grid, in the case of open-loop periodic excitation and under strict stability assumptions. By tuning the frequency resolution and exploiting Lipschitz continuity, we also obtain estimation guarantees in the $\mathcal{H}_{\infty}$ norm. An interesting direction for future work is studying finite-sample non-parametric least squares in the frequency domain. This approach could lead to interesting connections between function class complexity and experiment design. Moreover, adding more structure, beyond Lipschitz continuity, will lead to faster rates.
