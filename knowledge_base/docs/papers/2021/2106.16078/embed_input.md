Identification of Linear Systems with Multiplicative Noise from Multiple Trajectory Data

Topics include System identification, Linear systems, Multiplicative noise, Stochastic systems, Multiple trajectory data, Least-squares estimation, Covariance estimation, Identifiability, Second-moment dynamics, Asymptotic consistency, Non-asymptotic, High-probability, Sample complexity, Excitation conditions, Controllability, Data-driven control.

Extends the asymptotic results of 2002.06613 to rigorous non-asymptotic finite-sample results, using basically the same system identification / parameter estimation algorithm.

The paper studies identification of linear systems with multiplicative noise from multiple-trajectory data. An algorithm based on the least-squares method and multiple-trajectory data is proposed for joint estimation of the nominal system matrices and the covariance matrix of the multiplicative noise. The algorithm does not need prior knowledge of the noise or stability of the system, but requires only independent inputs with pre-designed first and second moments and relatively small trajectory length. The study of identifiability of the noise covariance matrix shows that there exists an equivalent class of matrices that generate the same second-moment dynamic of system states. It is demonstrated how to obtain the equivalent class based on estimates of the noise covariance. Asymptotic consistency of the algorithm is verified under sufficiently exciting inputs and system controllability conditions. Non-asymptotic performance of the algorithm is also analyzed under the assumption that the system is bounded. The analysis provides high-probability bounds vanishing as the number of trajectories grows to infinity. The results are illustrated by numerical simulations.

## Introduction

The study of stochastic systems with multiplicative noise (i.e., system states and inputs multiplied by noise) has a long history in control theory, and is re-emerging in the context of complex networked systems and learning-based control. In contrast to the additive-noise setting, the multiplicative-noise modeling framework has the ability to capture the coupling between noise and system states.

It is important to study identification of linear systems with multiplicative noise, because, when solving problems such as control design of multiplicative-noise linear quadratic regulator (LQR), system parameters including the nominal system matrices and the noise covariance matrix, especially the latter, generally need be known. In contrast, for the design problem of additive-noise LQR, the covariance matrix of additive noise needs not be known.

Another issue that must be addressed is how to perform system identification based on multiple-trajectory data, rather than on single-trajectory data. Multiple-trajectory data arises in two broad situations: episodic tasks where a system is reset to an initial state after a finite run time, as encountered in iterative learning control and reinforcement learning; and data collected from multiple identical systems in parallel, for example, robotic-grasping dataset collected by Google running several robot arms concurrently. For multiple-trajectory data, the length of each trajectory may be small, but the number of trajectories can be large.

## Contributions

This paper considers identification of linear systems with multiplicative noise from multiple-trajectory data.

## Conclusion and Future Work

In this paper an identification algorithm based on multiple-trajectory data was proposed for linear systems with multiplicative noise. With appropriately designed exciting inputs, the proposed algorithm is able to jointly estimate the nominal system and the multiplicative noise covariance. The asymptotic and non-asymptotic performance of the algorithm was analyzed theoretically, and illustrated by numerical experiments.
