Optimality of Linear Policies in Distributionally Robust Linear Quadratic Control

We study a generalization of the classical discrete-time, Linear-Quadratic-Gaussian (LQG) control problem where the noise distributions affecting the states and observations are unknown and chosen adversarially from divergence-based ambiguity sets centered around a known nominal distribution. For a finite horizon model with Gaussian nominal noise and a structural assumption on the divergence that is satisfied by many examples - including 2-Wasserstein distance, Kullback-Leibler divergence, moment-based divergences, entropy-regularized optimal transport, or Fisher (score-matching) divergence - we prove that a control policy that is affine in the observations is optimal and the adversary's corresponding worst-case optimal distribution is Gaussian. When the nominal means are zero (as in the classical LQG model), we show that the adversary should optimally set the distribution's mean to zero and the optimal control policy becomes linear. Moreover, the adversary should optimally ``inflate" the noise by choosing covariance matrices that dominate the nominal covariance in Loewner order.

## Introduction

The Linear Quadratic Gaussian (LQG) control problem has served as a fundamental building block for a wide range of applications in management \[Bensoussan et al. Holt et al., \], economics \[Hansen and Sargent, \], finance \[Abeille et al., \], engineering \[Auger et al. Chen, \], or medicine \[Patek et al. Chakravarty et al. Kazemian et al. Todorov and Jordan, \].

The discrete-time, finite-horizon formulation considers the problem of minimizing the expected costs incurred when controlling a linear dynamical system over a finite number of periods $t \in \left\{ 0,1,\ldots,{T - 1} \right\}$. The system evolves according to the equations

where $x_{t} \in {\mathbb{R}}^{n}$ denotes the system states, $u_{t} \in {\mathbb{R}}^{m}$ denotes the control inputs, $w_{t} \in {\mathbb{R}}^{n}$ denotes an exogenous noise process, and the system matrices $A_{t} \in {\mathbb{R}}^{n \times n}$ and $B_{t} \in {\mathbb{R}}^{n \times m}$ are known. The decision maker only has access to imperfect state measurements

corrupted by exogenous observation noise $v_{t} \in {\mathbb{R}}^{p}$, where $C_{t} \in {\mathbb{R}}^{p \times n}$ and usually $p \leq n$ (so that observing $y_{t}$ does not allow perfectly reconstructing $x_{t}$ even without observation noise).
