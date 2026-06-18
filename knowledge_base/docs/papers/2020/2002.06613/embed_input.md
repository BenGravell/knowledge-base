Linear System Identification under Multiplicative Noise from Multiple Trajectory Data

Topics include Linear systems, System identification, Trajectory data, Multiplicative noise, Multiple trajectories, Covariance matrix, Network system, Least squares, Optimal control, Convergence rate, Recursive, Algorithm.

Provides asymptotic results on convergence of identified system parameters (dynamics parameters and noise covariances) to true values using a trajectory-averaging least-squares estimation algorithm for linear systems with multiplicative noise. Later extended to non-asymptotic results in 2106.16078.

The study of multiplicative noise models has a long history in control theory but is re-emerging in the context of complex networked systems and systems with learning-based control. We consider linear system identification with multiplicative noise from multiple state-input trajectory data. We propose exploratory input signals along with a least-squares algorithm to simultaneously estimate nominal system parameters and multiplicative noise covariance matrices. Identifiability of the covariance structure and asymptotic consistency of the least-squares estimator are demonstrated by analyzing first and second moment dynamics of the system. The results are illustrated by numerical simulations.

## Introduction

The study of stochastic systems with noise which multiplies with the state and input i.e. multiplicative noise has a long history in control theory, but is re-emerging in the context of complex networked systems and systems with learning-based control. In contrast with the well-known additive noise setting, multiplicative noise has the ability to capture dependence of the noise on the state and/or control input.

The first issue that must be addressed is that a complete multiplicative noise system model requires accurate estimates not only of the nominal linear system matrices, but also the noise covariance structure. This stands in stark contrast to the additive noise case where the noise covariance structure has no bearing on the control design and can thus be ignored during system identification. For the identification of a nominal linear system, recursive algorithms have been developed in the control literature, such as the recursive least-squares algorithm.

The second issue we address is that of performing system identification based on multiple state-input trajectory data rather than a single trajectory. Multiple trajectory data arises in two broad situations: 1) episodic tasks where a single system is reset to an initial state after a finite run time, as encountered in iterative learning control and reinforcement learning problems and 2) collecting data from multiple identical systems in parallel, for example, physical experiments and snapshots of social interaction processes.

In this paper we consider linear system identification with multiplicative noise from multiple trajectory data.

We propose a least-squares estimation algorithm to jointly estimate the nominal system matrices and multiplicative noise covariances from sample averages of multiple finite-horizon trajectory rollouts (Algorithm 1). A two-stage algorithm based on first and second moment dynamics that separate the nominal parameters from the noise variances is utilized, where a stochastic input design, from Gaussian and Wishart distributions, is used for exciting the moment dynamics. The algorithm does not need prior knowledge for the multiplicative noise or stability conditions for the system, except that the noises are i.i.d.
