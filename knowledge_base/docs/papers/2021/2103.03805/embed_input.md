Topological Linear System Identification via Moderate Deviations Theory

Two dynamical systems are topologically equivalent when their phase-portraits can be morphed into each other by a homeomorphic coordinate transformation on the state space. The induced equivalence classes capture qualitative properties such as stability or the oscillatory nature of the state trajectories, for example. In this paper we develop a method to learn the topological class of an unknown stable system from a single trajectory of finitely many state observations. Using a moderate deviations principle for the least squares estimator of the unknown system matrix theta, we prove that the probability of misclassification decays exponentially with the number of observations at a rate that is proportional to the square of the smallest singular value of theta.

## Introduction

We consider the discrete-time linear time-invariant system

where $x_{t} \in {\mathbb{R}}^{n}$ and $w_{t} \in {\mathbb{R}}^{n}$ denote the state and the exogenous noise at time $t \in {\mathbb{N}}$, while $\theta$ represents the system matrix, and $\nu$ stands for the marginal distribution of the initial state $x_{0}$. Except for asymptotic stability we assume that nothing is known about $\theta$, and we aim to identify $\theta$ from a single trajectory of states ${\{{\hat{x}}_{t}\}}_{t = 0}^{T}$ generated . A simple estimator for $\theta$ is the least squares estimator

which may take any value in ${\mathbb{R}}^{n \times n}$. It is therefore possible that ${\hat{\theta}}_{T}$ is unstable even though $\theta$ is stable, in which case the estimator is of limited practical value. Alternative estimators with attractive statistical properties that are guaranteed to be stable have been proposed in \[undef, undefa, undefb, undefc\]. However, stability is not the only property of $\theta$ that impacts the qualitative behavior of a linear system; see Figure 1.

Related work. Linear system identification---especially by means of least squares techniques---has a rich history \[undefe, undeff\]. In this paper we are, however, not only interested in finding estimators that fall into the vicinity of the unknown true model $\theta$. In addition, the estimators should display a qualitatively similar behavior as $\theta$. This requirement relates to some extent to the work on qualitative identification pioneered by \[undefg\]. More recently, the focus in linear system identification shifted towards ensuring the efficient use of data.
