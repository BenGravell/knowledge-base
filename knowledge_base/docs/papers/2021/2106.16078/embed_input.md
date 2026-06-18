Identification of Linear Systems with Multiplicative Noise from Multiple Trajectory Data

Topics include System identification, Linear systems, Multiplicative noise, Stochastic systems, Multiple trajectory data, Least-squares estimation, Covariance estimation, Identifiability, Second-moment dynamics, Asymptotic consistency, Non-asymptotic, High-probability, Sample complexity, Excitation conditions, Controllability, Data-driven control.

Extends the asymptotic results of 2002.06613 to rigorous non-asymptotic finite-sample results, using basically the same system identification / parameter estimation algorithm.

The paper studies identification of linear systems with multiplicative noise from multiple-trajectory data. An algorithm based on the least-squares method and multiple-trajectory data is proposed for joint estimation of the nominal system matrices and the covariance matrix of the multiplicative noise. The algorithm does not need prior knowledge of the noise or stability of the system, but requires only independent inputs with pre-designed first and second moments and relatively small trajectory length. The study of identifiability of the noise covariance matrix shows that there exists an equivalent class of matrices that generate the same second-moment dynamic of system states. It is demonstrated how to obtain the equivalent class based on estimates of the noise covariance. Asymptotic consistency of the algorithm is verified under sufficiently exciting inputs and system controllability conditions. Non-asymptotic performance of the algorithm is also analyzed under the assumption that the system is bounded. The analysis provides high-probability bounds vanishing as the number of trajectories grows to infinity. The results are illustrated by numerical simulations.

## Introduction

The study of stochastic systems with multiplicative noise (i.e., system states and inputs multiplied by noise) has a long history in control theory, and is re-emerging in the context of complex networked systems and learning-based control. In contrast to the additive-noise setting, the multiplicative-noise modeling framework has the ability to capture the coupling between noise and system states....

It is important to study identification of linear systems with multiplicative noise, because, when solving problems such as control design of multiplicative-noise linear quadratic regulator (LQR), system parameters including the nominal system matrices and the noise covariance matrix, especially the latter, generally need be known. In contrast, for the design problem of additive-noise LQR, the covariance matrix of additive noise needs not be known....

## Conclusion and Future Work

In this paper an identification algorithm based on multiple-trajectory data was proposed for linear systems with multiplicative noise. With appropriately designed exciting inputs, the proposed algorithm is able to jointly estimate the nominal system and the multiplicative noise covariance. The asymptotic and non-asymptotic performance of the algorithm was analyzed theoretically, and illustrated by numerical experiments....

Under Assumption 1 the rollouts $\lbrack x_{0}^{(k)},\ldots,x_{l}^{(k)}\rbrack$, $k \in {\lbrack n_{r}\rbrack}$, are i.i.d., so the following consistency result can be obtained from strong law of large numbers.

1:Input: Rollout length ℓ and the number of rollouts nr.
2:Output: [Â B̂], $\lbrack{{\hat{\overset{\sim}{\Sigma}}}_{A}^{\prime}{\hat{\overset{\sim}{\Sigma}}}_{B}^{\prime}}\rbrack$.
5: Generate νt ∈ ℝm and ${\overline{U}}_{t} \in {\mathbb{R}}^{m \times m}$ with ${\overline{U}}_{t} \succeq 0$.
9: Generate x0(k) independently from the initial multivariate distribution 𝒳0.
11: Generate ut(k) independently from a multivariate distribution with first moment νt and second central

This proposition captures the deviations of random components of System from their expectations. Using the bounds in Assumption 2 one could upper-bound these deviations, for instance,

Another issue that must be addressed is how to perform system identification based on multiple-trajectory data, rather than on single-trajectory data....
