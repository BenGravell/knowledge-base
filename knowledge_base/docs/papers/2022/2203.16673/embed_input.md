System Identification via Nuclear Norm Regularization

This paper studies the problem of identifying low-order linear systems via Hankel nuclear norm regularization. Hankel regularization encourages the low-rankness of the Hankel matrix, which maps to the low-orderness of the system. We provide novel statistical analysis for this regularization and carefully contrast it with the unregularized ordinary least-squares (OLS) estimator. Our analysis leads to new bounds on estimating the impulse response and the Hankel matrix associated with the linear system. We first design an input excitation and show that Hankel regularization enables one to recover the system using optimal number of observations in the true system order and achieve strong statistical estimation rates. Surprisingly, we demonstrate that the input design indeed matters, by showing that intuitive choices such as i.i.d. Gaussian input leads to provably sub-optimal sample complexity. To better understand the benefits of regularization, we also revisit the OLS estimator....

## Introduction

System identification is an important topic in control theory. Accurate estimation of system dynamics is the basis of control or policy decision problems in tasks varying from linear-quadratic control to deep reinforcement learning. Consider a linear time-invariant system of order $R$ with the *minimal* state-space representation

where $x_{t} \in {\mathbb{R}}^{R}$ is the state, $u_{t} \in {\mathbb{R}}^{p}$ is the input, $y_{t} \in {\mathbb{R}}^{m}$ is the output, $z_{t} \in {\mathbb{R}}^{m}$ is the output noise, $A \in {\mathbb{R}}^{R \times R}$, $B \in {\mathbb{R}}^{R \times p}$, $C \in {\mathbb{R}}^{m \times R}$, $D \in {\mathbb{R}}^{m \times p}$ are the system parameters, and $x_{0}$ is the initial state (in this paper, we assume $x_{0} = 0$). Generally with the same input and output, the dimension of the hidden state $x$ can be any number no less than $R$, and we are interested in the minimum dimensional representation (i.e., minimal realization) in this paper.

## Future directions

This paper established new sample complexity and estimation error bounds for system identification. We showed that nuclear norm penalization works well with small sample size regardless of the misspecification of the problem (i.e. fitting impulse response with a much larger length rather than the true order). For least-squares, we provided the first guarantee that is optimal in sample complexity and the Hankel spectral norm error. These results can be refined in several directions. In the proof of Theorem 1, we used a weighted Hankel operator....

The theorem below shows that Hankel-regularization achieves near-optimal sample complexity with similarly strong estimation error rates that decay as $1/\sqrt{T}$.

There are several interesting generalizations of least squares with non-asymptotic guarantees for different goals. Refs. and introduce filtering strategies on top of least squares. The filters in is the top eigenvectors of a special deterministic matrix, used for output prediction in stable systems. Ref. uses filters in frequency domain to recover the system parameters of a stable system, gives a non-asymptotic analysis for learning a Kalman filter system, which can also be applied to an auto-regressive setting....

This theorem improves the spectral norm bound compared to, which naively bounds the spectral norm in terms of IR error using the...
