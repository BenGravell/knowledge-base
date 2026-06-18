Finite Sample Frequency Domain Identification

We study non-parametric frequency-domain system identification from a finite-sample perspective. We assume an open loop scenario where the excitation input is periodic and consider the Empirical Transfer Function Estimate (ETFE), where the goal is to estimate the frequency response at certain desired (evenly-spaced) frequencies, given input-output samples. We show that under sub-Gaussian colored noise (in time-domain) and stability assumptions, the ETFE estimates are concentrated around the true values. The error rate is of the order of O((d_u+sqrt{d_ud_y})sqrt{M/N_tot}), where N_tot is the total number of samples, M is the number of desired frequencies, and d_u, d_y are the dimensions of the input and output signals respectively. This rate remains valid for general irrational transfer functions and does not require a finite order state-space representation. By tuning M, we obtain a N_tot^(-1/3) finite-sample rate for learning the frequency response over all frequencies in the H_infinity norm. Our result draws upon an extension of the Hanson-Wright inequality to semi-infinite matrices. We study the finite-sample behavior of ETFE in simulations.

## Introduction

We consider the identification of *unknown* linear, discrete-time, time-invariant systems of the form

Frequency domain identification has been extensively studied. The estimation error guarantees (on its distribution) are typically asymptotic, e.g. see Central Limit Theorem in \[, Ch. 16\], and, thus, are valid when the number of samples grows to infinity. Here, we adopt a finite-sample point of view, motivated by advances in modern statistics and statistical learning theory. Asymptotic methods are sharp asymptotically but are often heuristically applied for finite samples. Finite-sample bounds, on the other hand, are valid for any number of samples, but suffer from looser bounding constants....

## Conclusion and Future Work

We provide finite-sample guarantees for the ETFE over a selected frequency grid, in the case of open-loop periodic excitation and under strict stability assumptions. By tuning the frequency resolution and exploiting Lipschitz continuity, we also obtain estimation guarantees in the $\mathcal{H}_{\infty}$ norm. An interesting direction for future work is studying finite-sample non-parametric least squares in the frequency domain. This approach could lead to interesting connections between function class complexity and experiment design. Moreover, adding more structure, beyond Lipschitz continuity, will lead to faster rates....

### Theorem 1 (ETFE Finite-Sample)

We can now state our objective, which is providing finite-sample guarantees for estimating the frequency responses. We focus on $\epsilon - \delta$ probabilistic guarantees, where $\epsilon$ controls the estimation accuracy and $\delta$ controls the confidence. {mdframed}\[roundcorner=3pt, backgroundcolor=blue!6,innertopmargin=-2pt\]

Let Assumption. ‣ 2.2 Excitation Method ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification") be in effect. Then, for all $k = {N_{p}\ell}$, $\ell \in {\lbrack M\rbrack}$

While finite-sample system identification has been studied before, most results are focused on time domain identification. Detailed related work and a tutorial on the subject can be found in. Frequency domain and time domain identification have many similarities--ignoring initial conditions, transients, or leakage effects, the two domains are equivalent from a prediction error framework perspective \[\]....
