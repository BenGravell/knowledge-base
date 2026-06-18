## Introduction

Spacecraft trajectory design under uncertainty becomes particularly challenging when the orbit-determination process depends on the nominal trajectory. In such problems, maneuver design and navigation design cannot be treated independently, because the trajectory determines the measurement geometry and the achievable navigation accuracy. This coupling is especially important in scenarios with weak observability, such as angles-only navigation or missions with limited tracking opportunities. Although high-quality measurements are often available in conventional missions, for example, through radiometric tracking with Delta-DOR in deep-space missions \[CurkendallBorder2013DeltaDOR\] or GNSS measurements in LEO missions \[AllahvirdiZadehWangElMowafy2022ASCE\], increasing mission complexity and operational cadence can limit such tracking opportunities. These considerations motivate a unified framework for partially observable trajectory optimization problems, in which maneuver design, orbit determination, and correction maneuver planning are tightly coupled under uncertainty.

In spaceflight applications, covariance control approaches \[HotzSkelton1987CovarianceControl\] have been developed to design maneuver policies under uncertainty using a variety of optimization techniques, including differential dynamic programming (DDP), nonlinear programming (NLP), and sequential convex programming (SCP). Refs. \[Ozaki2018-rx, Ozaki2020-id\] derive tube stochastic DDP, in which DDP is applied to a stochastic dynamical system sampled by the unscented transform. As a higher-fidelity approach, Ref. \[Greco2022-at\] presents an NLP-based method for optimal impulsive control in belief space, incorporating the orbit-determination process into uncertainty propagation via polynomial chaos expansion. Ref. \[Varghese2026-sh\] improves convergence of NLP with covariance dynamics by exploiting the forward--backward structure and introducing a feedback-gain parameterization that reduces the search space. SCP-based methods have also been extensively studied due to their tractability and the availability of efficient convex optimization solvers. For example, Ref. \[ridderhof2020chance\] formulates convexified discrete-time dynamics, costs, and constraints that can be solved iteratively even for nonlinear trajectory optimization, and Ref. \[Oguri_undated-kc\] incorporates stochastic mass dynamics and the orbit-determination process into an SCP framework. Because the feedback gain is parameterized as a block lower-triangular matrix that depends on past states at the discretization nodes in many of these approaches, the computational effort increases quadratically with the number of nodes. To improve the efficiency of covariance control with chance constraints, sequential semidefinite programming methods have also been proposed \[rapakoulias2023discretetimeoptimalcovariancesteering, pilipovsky2024computationallyefficientchanceconstrained\] and applied to astrodynamics problems in Ref. \[Kumagai2025-bl\].

Planning under dynamical and observation uncertainties has also been studied extensively in the robotics community, where the problem is often formulated as a partially observable Markov decision process and addressed via belief-space planning \[KaelblingLittmanCassandra1998POMDP\]. Because belief-space planning is generally intractable due to its infinite-dimensional state space, practical methods often assume Gaussian beliefs and perform local approximations around a nominal trajectory. Ref. \[Platt2010-jq\] applies a linear quadratic regulator (LQR) to deterministic Gaussian belief-space dynamics under the assumption of maximum-likelihood observation (MLO). Refs. \[Van_Den_Berg2012-fn, Van_den_Berg2017-br\] remove the MLO assumption and propose iterative local optimization methods in belief space by expanding the cost function and dynamics around the nominal trajectory to obtain time-varying affine feedback policies. Ref. \[Indelman2015-jb\] further extends the framework by introducing random binary variables to model missed observations. Related active-sensing trajectory generation methods have also been developed to improve estimation performance by shaping the nominal trajectory according to information-related criteria. These approaches are closely related to belief-space planning in that they exploit the coupling between motion and estimation.

These two lines of research offer complementary strengths. Covariance control approaches provide powerful tools for robust control policy design under uncertainty, whereas belief-space planning methods are effective for information-aware decision-making. However, partially observable trajectory optimization problems in which trajectory design, orbit determination, and correction maneuver planning must be addressed in a unified manner remain insufficiently studied. Many covariance control formulations simplify the coupling by assuming that the orbit-determination process can be separated from the trajectory optimization problem. As a result, they are not primarily designed to generate navigation-aware solutions in which the nominal trajectory is deliberately shaped to pass through information-rich regions. In contrast, belief-space planning methods primarily emphasize information gathering through nominal-trajectory design and generally do not explicitly optimize feedback policies under general mission constraints. Thus, the joint optimization of informative nominal trajectories and feedback policies under general mission constraints remains a challenging problem in spacecraft mission design.

To address this gap, we develop a partially observable stochastic differential dynamic programming (PO-SDDP) framework for partially observable trajectory optimization problems. The proposed framework enables simultaneous optimization of the nominal control and feedback gains while explicitly accounting for state estimation and covariance propagation under general mission constraints. The main technical contributions are as follows. First, we formulate a generalized belief-space DDP framework by augmenting the belief-space transition model with the state-estimate covariance and by treating the feedback gain as an optimization variable. Second, we develop a practical formulation for spacecraft mission design by combining an augmented Lagrangian method with regularized or smooth approximations of representative cost functions and constraints, including thrust magnitude and guidance accuracy constraints. Third, we develop a semi-analytic method to efficiently compute the state transition matrices for covariance propagation, together with automatic differentiation for model-dependent derivatives and model-independent tensor operations for covariance propagation.

From an algorithmic perspective, the proposed method is rooted in stochastic differential dynamic programming \[Theodorou2010-xy\] and related DDP-based covariance control methods for nonlinear stochastic systems \[Yi2020-mz\]. The main distinction is that the proposed method formulates the local optimization problem in belief space, explicitly accounting for the dependence of navigation performance on the nominal trajectory. An observability-aware DDP approach \[fujiwara2024\] is also closely related to the present work. Compared with that approach, the proposed method can be interpreted as a stochastic extension that incorporates covariance propagation and feedback-gain optimization into the DDP recursion. An earlier version of this work appeared in Ref. \[fujiwara\]. This manuscript extends the conference paper by providing a more rigorous derivation of the dynamics, additional implementation details, and an expanded numerical analysis.

We demonstrate the proposed algorithm through three numerical examples: the light-dark domain problem, an Earth-to-Mars planar transfer, and a periodic-orbit transfer in the Earth--Moon circular restricted three-body problem (CR3BP). These examples show that the method can address a broad range of problems, from information-aware trajectory shaping to robust correction maneuver design.

The remainder of this paper is organized as follows. Section 2 derives a belief-space transition model defined by the dynamics, observation model, and uncertainty model. In Section 3, we introduce the partially observable stochastic DDP algorithm. Section 4 presents semi-analytic computations of the state transition matrices for covariance propagation, together with representative cost functions and constraints applicable to space mission design using smoothed approximations. Section 5 presents the numerical results, and Section 6 concludes the paper.

## Belief Propagation for Partially Observable Trajectory Optimization Problems

This section derives a tractable belief-space transition model for partially observable trajectory optimization. In belief-space planning, decisions are made based on a belief over the state rather than the unobserved true state. Our objective is to construct belief-space dynamics for mission design when future observations are unknown. To this end, we approximate the belief using up to second-order moments and derive propagation equations for two covariance matrices: the estimation-error covariance and the state-estimate covariance. These covariance dynamics, together with the nominal dynamics, constitute the belief-space transition model used in the subsequent DDP algorithm.

### Dynamics, observations, and time discretization

We consider a controlled stochastic system over the mission design interval $t \in {\lbrack t_{0},t_{f}\rbrack}$, with state ${{\mathbf{x}}{(t)}} \in {\mathbb{R}}^{n_{x}}$ and control ${{\mathbf{u}}{(t)}} \in {\mathbb{R}}^{n_{u}}$. The true state evolves according to the continuous-time stochastic dynamics

where ${\mathbf{f}}:{{{\mathbb{R}}^{n_{x}} \times {\mathbb{R}}^{n_{u}} \times {\mathbb{R}}}\rightarrow{\mathbb{R}}^{n_{x}}}$ represents the deterministic part of the dynamics, ${d{\mathbf{w}}_{x}} \in {\mathbb{R}}^{n_{w}}$ is a Brownian-motion increment, and ${G_{x}{({\mathbf{x}},{\mathbf{u}})}}:{{{\mathbb{R}}^{n_{x}} \times {\mathbb{R}}^{n_{u}}}\rightarrow{\mathbb{R}}^{n_{x} \times n_{w}}}$ is a weighting matrix that determines the process-noise intensity as a function of the state and control, for example, to model maneuver errors that depend on thrust magnitude and direction.

To discretize the stochastic dynamics in Eq., the optimization interval $\lbrack t_{0},t_{f}\rbrack$ is partitioned by maneuver and observation epochs. Let $N_{j}{(k)}$ denote the number of observation epochs between the $k$-th and $({k + 1})$-th maneuver epochs. When ${N_{j}{(k)}} > 0$, these observation epochs are ordered as

where epochs with a single subscript, except for the terminal epoch $t_{N} = t_{f}$, correspond to maneuver epochs, whereas epochs with double subscripts correspond to observation epochs. Without loss of generality, we define $t_{k,0}:=t_{k}$ and $t_{k,{{N_{j}{(k)}} + 1}}:=t_{k + 1}$. Thus, although $N_{j}{(k)}$ denotes the number of observation epochs, the interval between two consecutive maneuver epochs contains ${N_{j}{(k)}} + 1$ intermediate transitions. Here, the final observation epoch between two consecutive maneuver epochs is allowed to coincide with the latter maneuver epoch. In such a case, the observation is obtained just before performing the maneuver using the latest orbit-determination result, and therefore $t_{k,{N_{j}{(k)}}} = t_{k,{{N_{j}{(k)}} + 1}} = t_{k + 1}$. Moreover, different observation sources may be available at different observation epochs. This partitioning is applicable to general space mission design problems.

Observations at each epoch are modeled as

where ${\mathbf{h}}_{k,j}:{{\mathbb{R}}^{n_{x}}\rightarrow{\mathbb{R}}^{n_{y_{k,j}}}}$ is the observation model at epoch $t_{k,j}$, ${\mathbf{w}}_{y_{k,j}} \in {\mathbb{R}}^{n_{y_{k,j}}}$ is an independent Gaussian noise vector, and $G_{y_{k,j}}:{{\mathbb{R}}^{n_{x}}\rightarrow{\mathbb{R}}^{n_{y_{k,j}} \times n_{y_{k,j}}}}$ is a weighting matrix for state-dependent observation noise, with covariance

Here, $W_{k,j}{({\mathbf{x}}_{k,j})}$ is defined as the inverse matrix of the observation noise covariance. We assume that ${\mathbf{h}}_{k,j}$ and $G_{y_{k,j}}$ may vary with the epoch $t_{k,j}$ to enable handling different observation types and dimensions across epochs, and that ${\mathbf{w}}_{y_{k,j}}$ is mutually independent across epochs and independent of the process noise ${\mathbf{w}}_{x}$.

### Belief representation

Given the past nominal control sequence ${\overline{\mathbf{u}}}_{0:k} = {\{{\overline{\mathbf{u}}}_{0},\ldots,{\overline{\mathbf{u}}}_{k}\}}$ and the observation histories ${\mathbf{y}}_{{k,1}:j} = {\{{\mathbf{y}}_{k,1},\ldots,{\mathbf{y}}_{k,j}\}}$ and ${\mathbf{Y}}_{k - 1} = {\{{\mathbf{Y}}_{0},\ldots,{\mathbf{Y}}_{k - 1}\}}$, where ${\mathbf{Y}}_{j} = {\{{\mathbf{y}}_{j,1},\ldots,{\mathbf{y}}_{j,{N_{j}{(j)}}}\}}$, the belief is defined as the conditional distribution of the state:

Given a new observation ${\mathbf{y}}_{k,{j + 1}}$, the belief is propagated by Bayesian filtering:

where $\eta_{k,{j + 1}}$ is a normalizing constant independent of ${\mathbf{x}}_{k,{j + 1}}$. In general, Eq. yields an infinite-dimensional probability distribution that does not admit a closed-form representation. To address this issue, we first define the state estimate and the estimation-error covariance as

${\hat{\mathbf{x}}}_{k,j}$ $:={{\mathbb{E}}\left\lbrack {{\mathbf{x}}_{k,j} \mid {{\overline{\mathbf{u}}}_{0:k},{\mathbf{Y}}_{k - 1},{\mathbf{y}}_{{k,1}:j}}} \right\rbrack}$ (7a)
${\overset{\sim}{P}}_{k,j}$ $:={{\mathbb{E}}\left\lbrack {{{({{\mathbf{x}}_{k,j} - {\hat{\mathbf{x}}}_{k,j}})}{({{\mathbf{x}}_{k,j} - {\hat{\mathbf{x}}}_{k,j}})}^{\top}} \mid {{\overline{\mathbf{u}}}_{0:k},{\mathbf{Y}}_{k - 1},{\mathbf{y}}_{{k,1}:j}}} \right\rbrack}$ (7b)

and then approximate the belief ${\mathbf{b}}{({\mathbf{x}}_{k,j})}$ by a Gaussian density with mean ${\hat{\mathbf{x}}}_{k,j}$ and covariance ${\overset{\sim}{P}}_{k,j}$. Under this approximation, the estimation error ${\overset{\sim}{\mathbf{x}}}_{k,j}:={{\mathbf{x}}_{k,j} - {\hat{\mathbf{x}}}_{k,j}}$ is conditionally Gaussian with zero mean and covariance ${\overset{\sim}{P}}_{k,j}$.

In the mission design phase, future observations have not yet been realized. Therefore, ${\hat{\mathbf{x}}}_{k,j}$ is treated as a random variable induced by the process and observation noises, whereas ${\overset{\sim}{P}}_{k,j}$ may also depend on the realized trajectory and observations in the general nonlinear filtering problem. We further define the nominal state and the state-estimate covariance as

${\overline{\mathbf{x}}}_{k,j}$ $:={{\mathbb{E}}\left\lbrack {\hat{\mathbf{x}}}_{k,j} \right\rbrack}$ (8a)
${\hat{P}}_{k,j}$ $:={{\mathbb{E}}\left\lbrack {{({{\hat{\mathbf{x}}}_{k,j} - {\overline{\mathbf{x}}}_{k,j}})}{({{\hat{\mathbf{x}}}_{k,j} - {\overline{\mathbf{x}}}_{k,j}})}^{\top}} \right\rbrack}$ (8b)

and assume that ${\hat{\mathbf{x}}}_{k,j}$ also follows a Gaussian distribution, ${\hat{\mathbf{x}}}_{k,j} \sim {\mathcal{N}\left( {\overline{\mathbf{x}}}_{k,j},{\hat{P}}_{k,j} \right)}$. By the law of total expectation, the expectation of the true state coincides with that of the state estimate:

and the covariance of the true state is given by

where ${\overset{\sim}{P}}_{k,j}^{nom}$ is approximated as a deterministic function of the nominal state ${\overline{\mathbf{x}}}_{k,j}$, the nominal control ${\overline{\mathbf{u}}}_{k}$, and the assumed process- and observation-noise statistics. Eq. and Eq. are consistent with the derivation in Ref. \[Ridderhof2020-cm\]. Under the assumption that the true state lies in the vicinity of the nominal state, we approximate ${\overset{\sim}{P}}_{k,j} \approx {\overset{\sim}{P}}_{k,j}^{nom}$; that is, the estimation-error covariance obtained from the Bayesian filter is close to its nominal value. This approximation is justified when the deviation from the nominal trajectory remains sufficiently small. Therefore, the estimation-error covariance is evaluated along the nominal trajectory and treated deterministically under this approximation. Figure 1 illustrates the relationships among the true state ${\mathbf{x}}_{k,j}$, nominal state ${\overline{\mathbf{x}}}_{k,j}$, state estimate ${\hat{\mathbf{x}}}_{k,j}$, estimation error ${\overset{\sim}{\mathbf{x}}}_{k,j}$, estimation-error covariance ${\overset{\sim}{P}}_{k,j}$, and state-estimate covariance ${\hat{P}}_{k,j}$.

Figure 1: Schematic illustration of the nominal state, state estimate, true state, and associated covariances

To obtain a deterministic propagation of the first- and second-order moments that represent the approximate belief-state transition model, the prior distributions of the initial state estimate ${\hat{\mathbf{x}}}_{0}$ and the initial estimation error ${\overset{\sim}{\mathbf{x}}}_{0}$ are also assumed to be Gaussian, i.e., ${\hat{\mathbf{x}}}_{0} \sim {\mathcal{N}\left( {\overline{\mathbf{x}}}_{0},{\hat{P}}_{0} \right)}$ and ${\overset{\sim}{\mathbf{x}}}_{0} \sim {\mathcal{N}\left( \mathbf{0}_{n_{x}},{\overset{\sim}{P}}_{0} \right)}$, where ${\overline{\mathbf{x}}}_{0}$ is the initial nominal state, and ${\hat{P}}_{0}$ and ${\overset{\sim}{P}}_{0}$ denote the initial covariance matrices of the state estimate and the estimation error, respectively. The quantities ${\overline{\mathbf{x}}}_{0}$, ${\hat{P}}_{0}$, and ${\overset{\sim}{P}}_{0}$ are assumed to be fixed and known.

### Linearization of dynamics

Given a nominal trajectory $({\overline{\mathbf{x}}{(t)}},{\overline{\mathbf{u}}{(t)}})$, the linearized dynamics describing the evolution of the state deviation $\delta{\mathbf{x}}{(t)}$ are given by

where ${\overline{A}{(t)}} = \left. {\partial{{\mathbf{f}}/{\partial{\mathbf{x}}}}} \right|_{\overline{\mathbf{x}},\overline{\mathbf{u}}}$, ${\overline{B}{(t)}} = \left. {\partial{{\mathbf{f}}/{\partial{\mathbf{u}}}}} \right|_{\overline{\mathbf{x}},\overline{\mathbf{u}}}$, and ${{\overline{G}}_{x}{(t)}} = {G_{x}{({\overline{\mathbf{x}}{(t)}},{\overline{\mathbf{u}}{(t)}})}}$. Here, the bilinear terms $\left( {\partial{G_{x}/{\partial{{{\mathbf{x}} \cdot \delta}{\mathbf{x}}}}}} \right)d{\mathbf{w}}_{x}$ and $\left( {\partial{G_{x}/{\partial{{{\mathbf{u}} \cdot \delta}{\mathbf{u}}}}}} \right)d{\mathbf{w}}_{x}$ are neglected under a small-noise or locally small-deviation assumption.

The nominal control is parameterized as a zero-order-hold continuous thrust input:

Integrating Eq. from $t_{k,j}$ to the next epoch $t_{k,{j + 1}}$ yields the following discrete-time linearized dynamics:

where ${\mathbf{w}}_{x}$ denotes an independent Gaussian random vector with zero mean and identity covariance. The matrices ${\overline{A}}_{k,j}$ and ${\overline{B}}_{k,j}$ are given by

${\overline{A}}_{k,j}$ $:=\frac{\partial{\mathbf{x}}_{k,{j + 1}}}{\partial{\mathbf{x}}_{k,j}} = {\Phi_{A}{(t_{k,{j + 1}},t_{k,j})}}$ (14a)
${\overline{B}}_{k,j}$ $:=\frac{\partial{\mathbf{x}}_{k,{j + 1}}}{\partial{\mathbf{u}}_{k,j}} = {\int_{t_{k,j}}^{t_{k,{j + 1}}}{\Phi_{A}{(t_{k,{j + 1}},t)}\overline{B}{(t)}{dt}}}$ (14b)

where $\Phi_{A}{(t_{2},t_{1})}$ denotes the state transition matrix along the nominal trajectory from $t_{1}$ to $t_{2}$.

The matrix ${\overline{G}}_{x_{k,j}}$ is chosen such that the covariance of the discrete process noise ${\overline{G}}_{x_{k,j}}{\mathbf{w}}_{x}$ matches

where ${\overline{G}}_{x}{(t)}$ is the square-root process-noise matrix evaluated at $({\overline{\mathbf{x}}{(t)}},{\overline{\mathbf{u}}{(t)}})$, and ${\overline{Q}}_{k,j}:={{\overline{G}}_{x_{k,j}}{\overline{G}}_{x_{k,j}}^{\top}}$. The details of how to compute the matrices ${\overline{A}}_{k,j}$, ${\overline{B}}_{k,j}$ are described in the Appendix, and the computation of ${\overline{G}}_{x_{k,j}}$ is described in Section 4.2.

### Linearization of observations and statistical residuals

Since ${\mathbf{h}}_{k,j}$ is assumed to be known, the predicted observation is obtained by evaluating the observation model at the prior state estimate:

where ${\hat{\mathbf{x}}}_{k,j^{-}}$ is the prior state estimate at time $t_{k,j}$.

By substituting Eq. and Eq. into Eq. and linearizing the observation model about the nominal trajectory, the first-order approximation of the observation residual is obtained as

where ${\overset{\sim}{\mathbf{x}}}_{k,j^{-}}:={{\mathbf{x}}_{k,j} - {\hat{\mathbf{x}}}_{k,j^{-}}}$ is the prior estimation error, ${\overline{C}}_{k,j} = \left. {\partial{{\mathbf{h}}_{k,j}/{\partial{\mathbf{x}}}}} \right|_{{\overline{\mathbf{x}}}_{k,j}}$ is the observation sensitivity matrix, ${\overline{G}}_{y_{k,j}} = {G_{y_{k,j}}{({\overline{\mathbf{x}}}_{k,j})}}$, ${\overline{D}}_{k,j}:={\lbrack{\overline{C}}_{k,j}\quad{\overline{G}}_{y_{k,j}}\rbrack}$, and

collects random quantities affecting the observation residual. The first- and second-order moments of ${\mathbf{ξ}}_{k,j^{-}}$ are given by

${\mathbb{E}}\left\lbrack {\mathbf{ξ}}_{k,j^{-}} \right\rbrack$ $= \mathbf{0}_{n_{x} + n_{y_{k,j}}}$ (19a)
$P_{\xi_{k,j^{-}}}: = {\mathbb{E}}\left\lbrack {\mathbf{ξ}}_{k,j^{-}}{\mathbf{ξ}}_{k,j^{-}}^{\top} \right\rbrack$ $= \begin{bmatrix} (19b)
{\overset{\sim}{P}}_{k,j^{-}} & O_{n_{x} \times n_{y_{k,j}}} \\

and the covariance of the observation residual is defined as

The residual $\delta{\mathbf{y}}_{k,j^{-}}$, commonly referred to as the observed-minus-computed (O-C) term in spacecraft orbit determination, is evaluated from the actual observation data and the prior state estimate. In this study, $\delta{\mathbf{y}}_{k,j^{-}}$ is treated as a random variable characterized by ${\mathbf{ξ}}_{k,j^{-}}$.

### Filtered and nominal dynamics

Following Ref. \[Spinello2010-kl\], we adopt the extended Kalman filter (EKF) formulation for state-dependent observation noise derived from Bayes' theorem (cf. Eq. ). The posterior estimate ${\hat{\mathbf{x}}}_{k,{j + 1}}$ is given by the maximum a posteriori (MAP) estimate, i.e., the solution of

${\hat{\mathbf{x}}}_{k,{j + 1}}$ $= {\underset{{\mathbf{χ}}_{k,{j + 1}}}{\arg\min}{l{({\mathbf{χ}}_{k,{j + 1}})}}}$ (21a)

where ${\overset{\sim}{P}}_{k,{j + 1^{-}}}$ is the prior estimation-error covariance at $t_{k,{j + 1}}$, ${\mathbf{d}}_{k,{j + 1}} = {{\mathbf{χ}}_{k,{j + 1}} - {\hat{\mathbf{x}}}_{k,{j + 1^{-}}}}$, and ${\mathbf{e}}_{k,{j + 1}} = {{\mathbf{y}}_{k,{j + 1}} - {{\mathbf{h}}_{k,{j + 1}}{({\mathbf{χ}}_{k,{j + 1}})}}}$. The $\log{\det{W_{k,{j + 1}}^{- 1}{({\mathbf{χ}}_{k,{j + 1}})}}}$ term arises from the state dependence of the observation-noise covariance and is absent in the standard state-estimation problem. ${\mathbf{χ}}_{k,{j + 1}}$ denotes a candidate state in the minimization problem and is introduced to distinguish the optimization variable from the true state ${\mathbf{x}}_{k,{j + 1}}$.

Since the observation ${\mathbf{y}}_{k,{j + 1}}$ is uncertain and treated as a random variable in the mission design phase, we approximate the state-dependent noise covariance by fixing $W_{k,{j + 1}}^{- 1}$ at the nominal state ${\overline{\mathbf{x}}}_{k,{j + 1}}$. We define the fixed observation-noise covariance as

Consequently, the MAP estimate is approximated as

Here, $\Lambda_{k,{j + 1}}$ is the posterior information matrix defined as

and ${\mathbf{s}}_{k,{j + 1}}$ and ${\overline{S}}_{k,{j + 1}}$ are given by

${\mathbf{s}}_{k,{j + 1}}$ $= {{\overline{C}}_{k,{j + 1}}^{\top}{\overline{W}}_{k,{j + 1}}{\mathbf{e}}_{k,{j + 1}}}$ (25a)
${\overline{S}}_{k,{j + 1}}$ $= {{\overline{C}}_{k,{j + 1}}^{\top}{\overline{W}}_{k,{j + 1}}{\overline{C}}_{k,{j + 1}}}$ (25b)

The prior state estimate and estimation-error covariance at $t_{k,{j + 1}}$ are propagated from the posterior quantities at $t_{k,j}$ as

${\hat{\mathbf{x}}}_{k,{j + 1^{-}}}$ $= {{\mathbf{f}}_{k,j}{({\hat{\mathbf{x}}}_{k,j},{\mathbf{u}}_{k,j})}}$ (26a)
${\overset{\sim}{P}}_{k,{j + 1^{-}}}$ $= {{{\overline{A}}_{k,j}{\overset{\sim}{P}}_{k,j}{\overline{A}}_{k,j}^{\top}} + {{\overline{G}}_{x_{k,j}}{\overline{G}}_{x_{k,j}}^{\top}}}$ (26b)

where ${\mathbf{f}}_{k,j}{({\hat{\mathbf{x}}}_{k,j},{\mathbf{u}}_{k,j})}$ denotes the discrete-time nonlinear dynamics obtained by numerically integrating the deterministic part of Eq.. Under the Gaussian-belief assumption, the MAP estimate in Eq. coincides with the conditional expectation ${\mathbb{E}}\left\lbrack {{\mathbf{x}}_{k,{j + 1}} \mid {{\overline{\mathbf{u}}}_{0:k},{\mathbf{Y}}_{k - 1},{\mathbf{y}}_{{k,1}:{j + 1}}}} \right\rbrack$, because the posterior is Gaussian and its mean and mode are identical. Note that this equivalence does not hold in general for non-Gaussian posteriors. Since all terms in Eq., Eq., and Eq. are evaluated along the nominal trajectory, e.g., at ${\overline{\mathbf{x}}}_{k,j}$ and ${\overline{\mathbf{x}}}_{k,{j + 1}}$, the resulting propagation is more accurately described as a linearized Kalman filter than as the standard EKF, in which the matrices are evaluated at the latest state estimate ${\hat{\mathbf{x}}}_{k,j}$.

Under the first-order approximation ${\mathbf{e}}_{k,{j + 1}} \approx {\delta{\mathbf{y}}_{k,{j + 1}}^{-}}$, substituting Eq. into Eq. (25a) yields

Accordingly, the intermediate propagation with state estimation can be written as

and the propagation of the estimation-error covariance is then approximated by

By taking the expectation of both sides of Eq. and applying the first-order approximation, the nominal dynamics are approximated as

where ${\overline{\mathbf{x}}}_{k,{j + 1}}:={{\mathbb{E}}\left\lbrack {\hat{\mathbf{x}}}_{k,{j + 1}} \right\rbrack}$ and ${{\mathbb{E}}\left\lbrack {\mathbf{u}}_{k,j} \right\rbrack} = {\overline{\mathbf{u}}}_{k}$ because ${{\mathbb{E}}\left\lbrack {\delta{\hat{\mathbf{x}}}_{k,j}} \right\rbrack} = \mathbf{0}_{n_{x}}$.

### Belief-state transition model

Although the nominal control ${\overline{\mathbf{u}}}_{k}$ and feedback gain $K_{k}$ are held fixed within each stage, the feedback correction is recomputed at each intermediate epoch using the latest state estimate. Thus, for $t \in {\lbrack t_{k,j},t_{k,{j + 1}})}$, the applied control is modeled as

Because ${{\mathbb{E}}\left\lbrack {\delta{\hat{\mathbf{x}}}_{k,j}} \right\rbrack} = \mathbf{0}_{n_{x}}$, the expected applied control satisfies ${{\mathbb{E}}\left\lbrack {\mathbf{u}}_{k,j} \right\rbrack} = {\overline{\mathbf{u}}}_{k}$. The control deviation is defined as ${\delta{\mathbf{u}}_{k,j}}:={{\mathbf{u}}_{k,j} - {\overline{\mathbf{u}}}_{k}}$ and its covariance is given by

By substituting Eq. into Eq. and expanding to first order about the nominal trajectory, the propagation of the estimate deviation is approximated as

The propagation of the state-estimate covariance is then given by

$\mathcal{A}_{k,j}$ $= {{\overline{A}}_{k,j} + {{\overline{B}}_{k,j}K_{k}}}$ (35a)
$\mathcal{F}_{k,{j + 1}}$ $= {{\overset{\sim}{P}}_{k,{j + 1}}{\overline{C}}_{k,{j + 1}}^{\top}{\overline{W}}_{k,{j + 1}}{\overline{D}}_{k,{j + 1}}}$ (35b)

By vectorizing the belief state, we define the augmented state and control as

${\mathbf{X}}_{k,j}$ $= \begin{bmatrix} (36a)
{\overline{\mathbf{x}}}_{k,j}^{\top} & {{vec}{({\overset{\sim}{P}}_{k,j})}^{\top}} & {{vec}{({\hat{P}}_{k,j})}^{\top}}
\end{bmatrix}^{\top}$
${\mathbf{U}}_{k}$ $= \begin{bmatrix} (36b)
{\overline{\mathbf{u}}}_{k}^{\top} & {{vec}{(K_{k})}^{\top}}
\end{bmatrix}^{\top}$

where the feedback gain $K_{k}$ is included in the augmented control to explicitly consider ${\hat{P}}_{k}$ as controlled variables for the future distribution. Accordingly, the intermediate belief-state transition model can be written as

where ${\mathbf{F}}_{k,j}\left( {\mathbf{X}}_{k,j},{\mathbf{U}}_{k} \right)$ concatenates the transition model of the nominal state, the estimation-error covariance, and the state-estimate covariance, described in Eqs. and, respectively. If no observation is associated with an epoch $t_{k,{j + 1}}$, including the case ${N_{j}{(k)}} = 0$, the corresponding measurement-update terms are omitted by setting ${\overline{S}}_{k,{j + 1}} = O_{n_{x}}$ and removing the term $\mathcal{F}_{k,{j + 1}}P_{\xi_{k,{j + 1^{-}}}}\mathcal{F}_{k,{j + 1}}^{\top}$ from the propagations of ${\overset{\sim}{P}}_{k,{j + 1}}$ and ${\hat{P}}_{k,{j + 1}}$, respectively.

For use in trajectory optimization algorithms, the stage-to-stage belief-state transition must be written directly as a function of ${\mathbf{X}}_{k}$ and ${\mathbf{U}}_{k}$, because ${\mathbf{X}}_{k,j}$ is an intermediate variable determined by these quantities. Letting ${\mathbf{X}}_{k}:={\mathbf{X}}_{k,0}$, the belief-state transition model from $t_{k}$ to $t_{k + 1}$ is obtained by sequentially applying Eq. over the intermediate epochs:

Figure 2 illustrates the sequential state-propagation process described by Eq..

To obtain the posterior distribution $p{({{\mathbf{x}}_{k + 1} \mid {{\mathbf{Y}}_{k},{\mathbf{U}}_{k}}})}$, Bayes' rule may also be applied directly, as in Ref. \[Indelman2015-jb\]. In that case, only the distribution linking ${\mathbf{x}}_{k}$ and ${\mathbf{x}}_{k + 1}$ conditioned on the observation sequence ${\mathbf{Y}}_{k}$ is of interest, since all intermediate states ${\mathbf{x}}_{k,j}$ can be marginalized out. However, when the dynamical system contains process noise, filtering conditioned on ${\mathbf{Y}}_{k}$ induces strong correlations among observations, as shown in Ref. \[Carpenter2023-qo, Eq. \]. These correlations lead to cumbersome algorithmic implementation, particularly in the partial derivatives of the belief-state transition model. For this reason, sequential propagation with intermediate states is adopted in this study.

Figure 2: Block diagram of the sequential propagation of the belief-state dynamics

The dimensions of the augmented state and control are $n_{X} = {n_{x} + {2n_{x}^{2}}}$ and $n_{U} = {n_{u} + {n_{u}n_{x}}}$, respectively. Using square-root factors of the covariance matrices exploits symmetric structure and reduces the dimension of the augmented state to $n_{x} + {n_{x}{({n_{x} + 1})}}$. Although square-root representations may improve numerical stability and reduce dimensionality, we deliberately retain the full covariance matrices in this study because evaluating the state transition matrices for the belief-state transition model is simpler than with square-root factors, which require QR decompositions and second-order differentiation through them.

## Partially Observable Stochastic Differential Dynamic Programming

This section presents the PO-SDDP algorithm for solving partially observable trajectory optimization problems. The algorithm applies a DDP-based method with an augmented Lagrangian formulation to the deterministic belief-state transition model derived in the previous section.

For the nonlinear partially observable problem considered in this study, the separation principle does not generally decouple state estimation from trajectory optimization. The covariance dynamics are evaluated along the nominal trajectory being optimized; therefore, their coefficients vary with the nominal state and control inputs. This coupling appears through matrices such as ${\overline{A}}_{k,j}$, ${\overline{B}}_{k,j}$, ${\overline{G}}_{x_{k,j}}$, ${\overline{C}}_{k,{j + 1}}$, ${\overline{S}}_{k,{j + 1}}$, $\mathcal{A}_{k,j}$, and $\mathcal{F}_{k,{j + 1}}$, which depend on $({\overline{\mathbf{x}}}_{k,j},{\overline{\mathbf{u}}}_{k})$. Consequently, the augmented dynamics in Eq. must be differentiated with respect to the full augmented state and control. The DDP backward pass then uses the first- and second-order derivatives of this augmented transition map to construct local quadratic subproblems.

### Problem definition

Consider the following optimization problem:

$\min\limits_{{\mathbf{U}}_{0},{\mathbf{U}}_{1},\ldots,{\mathbf{U}}_{N - 1}}\mspace{21mu}$ ${\sum\limits_{k = 0}^{N - 1}{L_{k}{({\mathbf{X}}_{k},{\mathbf{U}}_{k})}}} + {\varphi{({\mathbf{X}}_{N})}}$ (39a)
${s.t}.\mspace{21mu}$ ${\mathbf{X}}_{k + 1} = {{\mathbf{F}}_{k}{({\mathbf{X}}_{k},{\mathbf{U}}_{k})}}$ (39b)
${{\mathbf{c}}_{k,\mathcal{I}}{({\mathbf{X}}_{k},{\mathbf{U}}_{k})}} \leq \mathbf{0}_{n_{c_{k,\mathcal{I}}}}$ (39c)
${{\mathbf{c}}_{k,\mathcal{E}}{({\mathbf{X}}_{k},{\mathbf{U}}_{k})}} = \mathbf{0}_{n_{c_{k,\mathcal{E}}}}$ (39d)
${\mathbf{\phi}{({\mathbf{X}}_{N})}} \leq \mathbf{0}_{n_{\phi}}$ (39e)
${{\mathbf{ψ}}{({\mathbf{X}}_{N})}} = \mathbf{0}_{n_{\psi}}$ (39f)

where ${L_{k}{({\mathbf{X}}_{k},{\mathbf{U}}_{k})}}:{{{\mathbb{R}}^{n_{X}} \times {\mathbb{R}}^{n_{U}}}\rightarrow{\mathbb{R}}}$ and ${\varphi{({\mathbf{X}}_{N})}}:{{\mathbb{R}}^{n_{X}}\rightarrow{\mathbb{R}}}$ denote the stage and terminal cost functions, respectively, and ${\mathbf{X}}_{k}$ and ${\mathbf{U}}_{k}$ denote the augmented state and augmented control at $t_{k}$. The functions ${{\mathbf{c}}_{k,\mathcal{I}}{({\mathbf{X}}_{k},{\mathbf{U}}_{k})}}:{{{\mathbb{R}}^{n_{X}} \times {\mathbb{R}}^{n_{U}}}\rightarrow{\mathbb{R}}^{n_{c_{k,\mathcal{I}}}}}$ and ${{\mathbf{c}}_{k,\mathcal{E}}{({\mathbf{X}}_{k},{\mathbf{U}}_{k})}}:{{{\mathbb{R}}^{n_{X}} \times {\mathbb{R}}^{n_{U}}}\rightarrow{\mathbb{R}}^{n_{c_{k,\mathcal{E}}}}}$ denote the stage inequality and equality constraints, and the functions ${\mathbf{\phi}{({\mathbf{X}}_{N})}}:{{\mathbb{R}}^{n_{X}}\rightarrow{\mathbb{R}}^{n_{\phi}}}$ and ${{\mathbf{ψ}}{({\mathbf{X}}_{N})}}:{{\mathbb{R}}^{n_{X}}\rightarrow{\mathbb{R}}^{n_{\psi}}}$ represent the terminal inequality and equality constraints, respectively.

### Augmented Lagrangian method

Although various approaches have been developed to handle constraints in DDP, including active-set methods \[Lantoine2012-ak, Xie2017-ma\] and interior-point DDP \[Pavlov2021-ll\], the proposed method adopts the augmented Lagrangian DDP (AL-DDP) framework \[howell2019altro, Pellegrini2020-ep\].

In AL-DDP, the stage and terminal constraints are incorporated into the cost function. The resulting augmented cost function is defined as

${\overset{\sim}{L}}_{k}$ $= {{L_{k}{({\mathbf{X}}_{k},{\mathbf{U}}_{k})}} + {\mathcal{P}_{\mathcal{I}}\left( {{\mathbf{c}}_{k,\mathcal{I}}{({\mathbf{X}}_{k},{\mathbf{U}}_{k})}},{\mathbf{λ}}_{k,\mathcal{I}},\sigma_{k,\mathcal{I}} \right)} + {\mathcal{P}_{\mathcal{E}}\left( {{\mathbf{c}}_{k,\mathcal{E}}{({\mathbf{X}}_{k},{\mathbf{U}}_{k})}},{\mathbf{λ}}_{k,\mathcal{E}},\sigma_{k,\mathcal{E}} \right)}}$ (41a)
$\overset{\sim}{\varphi}{({\mathbf{X}}_{N})}$ $= {{\varphi{({\mathbf{X}}_{N})}} + {\mathcal{P}_{\mathcal{I}}\left( {\mathbf{\phi}{({\mathbf{X}}_{N})}},{\mathbf{λ}}_{N,\mathcal{I}},\sigma_{N,\mathcal{I}} \right)} + {\mathcal{P}_{\mathcal{E}}\left( {{\mathbf{ψ}}{({\mathbf{X}}_{N})}},{\mathbf{λ}}_{N,\mathcal{E}},\sigma_{N,\mathcal{E}} \right)}}$ (41b)

where ${\mathbf{λ}}_{k,\mathcal{I}} \in {\mathbb{R}}^{n_{c_{k,\mathcal{I}}}}$ and ${\mathbf{λ}}_{k,\mathcal{E}} \in {\mathbb{R}}^{n_{c_{k,\mathcal{E}}}}$ denote the Lagrange multipliers for the stage constraints, and ${\mathbf{λ}}_{N,\mathcal{I}} \in {\mathbb{R}}^{n_{\phi}}$ and ${\mathbf{λ}}_{N,\mathcal{E}} \in {\mathbb{R}}^{n_{\psi}}$ denote the Lagrange multipliers for the terminal constraints. The positive scalars $\sigma_{k,\mathcal{I}}$, $\sigma_{k,\mathcal{E}}$, $\sigma_{N,\mathcal{I}}$, and $\sigma_{N,\mathcal{E}}$ denote the corresponding penalty parameters. The augmented Lagrangian penalty for equality constraints is defined as

For a generic inequality constraint vector ${\mathbf{c}} \in {\mathbb{R}}^{n_{c}}$, the penalty for inequality constraints is defined componentwise as

The AL-DDP algorithm consists of nested inner and outer loops. In the inner loop, DDP locally optimizes the control sequence by solving the unconstrained problem defined by the augmented cost function via backward and forward passes. After the inner loop has approximately converged, the outer loop updates the Lagrange multipliers and penalty parameters. The Lagrange multipliers and penalty parameters are updated as

${\mathbf{λ}}_{k,\mathcal{I}}^{+}$ ${= {\max\left( \mathbf{0}_{n_{c_{k,\mathcal{I}}}},{{\mathbf{λ}}_{k,\mathcal{I}} + {\sigma_{k,\mathcal{I}}{\mathbf{c}}_{k,\mathcal{I}}}} \right)}},$ ${\mathbf{λ}}_{k,\mathcal{E}}^{+}$ $= {{\mathbf{λ}}_{k,\mathcal{E}} + {\sigma_{k,\mathcal{E}}{\mathbf{c}}_{k,\mathcal{E}}}}$ (45a)
$\sigma_{k,\mathcal{I}}^{+}$ ${= {\gamma_{k,\mathcal{I}}\sigma_{k,\mathcal{I}}}},$ $\sigma_{k,\mathcal{E}}^{+}$ $= {\gamma_{k,\mathcal{E}}\sigma_{k,\mathcal{E}}}$ (45b)

where the maximum operation is applied componentwise, and $\gamma_{k,\mathcal{I}}$ and $\gamma_{k,\mathcal{E}}$ are penalty scaling constants.

### Backward pass

Given the augmented cost function in Eq., the value function satisfies the Bellman recursion

with the terminal condition ${J_{N}^{\ast}{({\mathbf{X}}_{N})}} = {\overset{\sim}{\varphi}{({\mathbf{X}}_{N})}}$, where $J_{k + 1}^{\ast}{({{\mathbf{F}}_{k}\left( {\mathbf{X}}_{k},{\mathbf{U}}_{k} \right)})}$ denotes the optimal cost-to-go, representing the future cost along the trajectory controlled by the optimal policy. In the backward pass, the control variations are obtained through minimizing the quadratic expansion of the cost-to-go function from the terminal stage to the initial one.

By introducing the state ${\mathbf{Z}}_{k} = {\lbrack{\mathbf{X}}_{k}^{\top}\quad{\mathbf{U}}_{k}^{\top}\rbrack}^{\top}$ that combines ${\mathbf{X}}_{k}$ with ${\mathbf{U}}_{k}$, the quadratic expansion of the combined belief-state transition model can be written as

where $\Phi_{k}^{1}$ and $\Phi_{k}^{2}$ denote the first- and second-order state transition matrices (STMs) from $t_{k}$ to $t_{k + 1}$, and $( \cdot )$ denotes a vector-tensor contraction. The STMs are associated with the combined dynamics defined as

since the controls are modeled as the zero-order-hold continuous thrust input. By expanding the cost-to-go function up to second order, the derivatives of the local quadratic expansion are written as

If $J_{{UU},k}$ is not positive definite, the resulting control update may fail to satisfy a descent condition. To address this issue, the algorithm incorporates a trust-region method that regularizes $J_{{UU},k}$ and restricts the control update $\delta{\mathbf{U}}_{k}$ to a region where the quadratic approximation remains valid. The trust-region subproblem is given by

$\min\limits_{\delta{\mathbf{U}}_{k}}\mspace{21mu}$ ${J_{U,k}^{\top}\delta{\mathbf{U}}_{k}} + {\frac{1}{2}\delta{\mathbf{U}}_{k}^{\top}J_{{UU},k}\delta{\mathbf{U}}_{k}}$ (51a)
${s.t}.\mspace{21mu}$ ${\parallel{D_{tr}\delta{\mathbf{U}}_{k}}\parallel} \leq \Delta$ (51b)

where $\parallel \cdot \parallel$ denotes the Euclidean norm, $D_{tr}$ is a positive definite scaling matrix and $\Delta$ is the trust-region radius. The matrix $D_{tr}$ defines a hyperellipsoid in the control space of ${\mathbf{U}}_{k}$. Using the regularized Hessian ${\overset{\sim}{J}}_{{UU},k} = {J_{{UU},k} + {\gammaD_{tr}^{\top}D_{tr}}}$ where $\gamma$ is the Lagrange multiplier associated with the trust-region constraint, the optimal local control update is obtained as

where ${\mathbf{α}}_{k}$ is the feedforward controller and $\beta_{k}$ is the feedback-gain matrix defined by ${\mathbf{α}}_{k} = {- {{\overset{\sim}{J}}_{{UU},k}^{- 1}J_{U,k}}}$ and $\beta_{k} = {- {{\overset{\sim}{J}}_{{UU},k}^{- 1}J_{{UX},k}}}$, respectively.

The expected cost reduction and value-function derivatives passed to the preceding stage are obtained by substituting the local policy into the quadratic expansion:

${ER}_{k}$ $= {{ER}_{k + 1} + {J_{U,k}^{\top}{\mathbf{α}}_{k}} + {\frac{1}{2}{\mathbf{α}}_{k}^{\top}J_{{UU},k}{\mathbf{α}}_{k}}}$ (53a)
$J_{X,k}^{\ast}$ $= {J_{X,k} + {J_{U,k}^{\top}\beta_{k}} + {{\mathbf{α}}_{k}^{\top}J_{{UX},k}} + {{\mathbf{α}}_{k}^{\top}J_{{UU},k}\beta_{k}}}$ (53b)
$J_{{XX},k}^{\ast}$ $= {J_{{XX},k} + {\beta_{k}^{\top}J_{{UX},k}} + {J_{{UX},k}^{\top}\beta_{k}} + {\beta_{k}^{\top}J_{{UU},k}\beta_{k}}}$ (53c)

with terminal conditions ${ER}_{N} = 0$, $J_{X,N}^{\ast} = {\overset{\sim}{\varphi}}_{X}$, and $J_{{XX},N}^{\ast} = {\overset{\sim}{\varphi}}_{XX}$.

### Forward pass

After the backward pass, a candidate reference trajectory is generated using the latest control policy. Given the reference state and control at the $i$th iteration, the candidate reference trajectory for the $({i + 1})$th iteration is computed by forward belief propagation:

${\mathbf{U}}_{k}^{({i + 1})}$ $= {{\mathbf{U}}_{k}^{(i)} + {\mathbf{α}}_{k} + {\beta_{k}\left( {{\mathbf{X}}_{k}^{({i + 1})} - {\mathbf{X}}_{k}^{(i)}} \right)}}$ (54b)

The total cost of the updated reference trajectory is then evaluated as

The ratio of the actual cost reduction $J_{0}^{({i + 1})} - J_{0}^{(i)}$ to the expected reduction ${ER}_{0}$ is then used to determine whether the candidate reference trajectory is accepted. If the candidate is accepted, the algorithm proceeds to the next iteration by reevaluating the quadratic expansions of the belief-state transition model ${\mathbf{F}}_{Z,k}$, stage cost ${\overset{\sim}{L}}_{k}$, and terminal cost $\overset{\sim}{\varphi}$ around the updated reference trajectory $\left( {\mathbf{X}}_{k}^{({i + 1})},{\mathbf{U}}_{k}^{({i + 1})} \right)$. Otherwise, the backward pass is repeated with a reduced trust-region radius $\Delta$ while reusing previously computed derivatives until the control update is accepted.

## Implementation Details

In this section, we describe implementation details that enhance the numerical stability and computational efficiency of the proposed framework. Specifically, we compute the first- and second-order derivatives of the covariance dynamics semi-analytically by reusing derivatives of the nominal dynamics, and introduce representative cost and constraint formulations for space mission design, smoothed by using Schatten-norm surrogates.

### Partial derivatives of covariance propagation

The most computationally expensive part of the framework is the computation of the first- and second-order STMs required for covariance propagation. Direct application of finite differences or automatic differentiation (AD) is computationally prohibitive because of the high dimensionality of the augmented dynamics. By exploiting the dependence of the covariance matrices on the nominal state and control, the STMs for covariance propagation can instead be computed from analytic derivatives expressed in terms of the STMs of the nominal-state dynamics. For example, the derivatives of the prior estimation-error covariance with respect to the nominal state can be written in terms of tensor multiplications as

where repeated superscripts follow the summation convention. On the right-hand side, the derivative of ${\overline{A}}_{k,j}$ with respect to $x_{k,j}$ corresponds to the second-order STMs of the nominal dynamics, whereas the derivative of ${\overline{G}}_{x_{k,j}}$ with respect to $x_{k,j}$ can be obtained through AD.

The procedure for computing the STMs of the nominal dynamics is summarized in the Appendix. Because these derivatives correspond to the belief-state transition over each intermediate interval from $t_{k,j}$ to $t_{k,{j + 1}}$, the Appendix also describes how the intermediate STMs are composed to obtain the stage-to-stage STMs.

In the second-order derivatives of covariance propagation, the third-order derivatives of the nominal-state dynamics emerge, for example,

The current implementation omits these terms to reduce computational burden. The effect of this approximation is mitigated in practice by the trust-region method in the backward pass, which limits the update when the quadratic expansion does not accurately predict the cost reduction.

Accordingly, the problem-dependent implementation effort is largely reduced to specifying the dynamics, observation models, and uncertainty models. The corresponding model-dependent derivatives can be evaluated using AD, whereas the tensor operations associated with covariance propagation are handled independently of the model.

### Approximation of discretized process noise

As described in Section 2.3, the discretized process-noise matrix ${\overline{G}}_{x_{k,j}}$ must be computed in the discretization procedure. This section introduces the approximation approach used in this study.

A direct approach is to integrate the continuous-time Lyapunov equation for $\overline{Q}{(t)}$:

from $t_{k,j}$ to $t_{k,{j + 1}}$ with the initial condition ${\overline{Q}{(t_{k,j})}} = O_{n_{x}}$. The matrix ${\overline{G}}_{x_{k,j}}$ can then be obtained from a Cholesky decomposition of ${\overline{Q}}_{k,j}$. Because the additional numerical integration of $\overline{Q}{(t)}$ increases the computational cost, the PO-SDDP algorithm instead uses the trapezoidal rule to approximate ${\overline{G}}_{x_{k,j}}$. Using the first-order STM ${\overline{A}}_{k,j}$, Eq. is approximated as

where ${\Deltat_{k,j}} = {t_{k,{j + 1}} - t_{k,j}}$, ${\overline{G}}_{k,j} = {G_{x}{({\overline{\mathbf{x}}}_{k,j},{\overline{\mathbf{u}}}_{k})}}$, and ${\overline{G}}_{k,{j + 1}} = {G_{x}{({\overline{\mathbf{x}}}_{k,{j + 1}},{\overline{\mathbf{u}}}_{k})}}$. Accordingly, ${\overline{G}}_{x_{k,j}}$ can be written as

so that ${\overline{Q}}_{k,j} = {{\overline{G}}_{x_{k,j}}{\overline{G}}_{x_{k,j}}^{\top}}$. This approximation is significantly faster than numerically integrating Eq. and more accurate than the Euler approximation used in Refs. \[Theodorou2010-xy, Yi2020-mz\].

### Representative cost functions and constraints

Since the covariance matrices ${\overset{\sim}{P}}_{k}$ and ${\hat{P}}_{k}$, together with the linear feedback gain $K_{k}$, are included in the state and control vectors, the costs and constraints can be formulated explicitly as functions of these quantities. In other words, the proposed method can handle stochastic costs and chance constraints expressed in terms of moments up to second order. Here, we introduce representative cost functions and constraints commonly used in spacecraft trajectory design, including minimum-fuel costs with covariance penalties, a stochastic thrust magnitude constraint, terminal covariance constraints, and linear state chance constraints. The cost functions and constraints introduced here are twice continuously differentiable with respect to the reference trajectory $\left( {\overline{\mathbf{X}}}_{k},{\overline{\mathbf{U}}}_{k} \right)$ and can therefore be incorporated into the proposed method. If different cost functions or constraints are introduced, their derivatives can also be evaluated using AD, although analytic implementations are significantly faster in practice.

### Cost functions

The stage and terminal cost functions are defined as the sum of the smoothed $\ell_{2}$-norm of the nominal control and quadratic penalties on the deviations of the state and control from the nominal trajectory. The cost functions are written as

$L_{k}{({\mathbf{X}}_{k},{\mathbf{U}}_{k})}$ $= {\Deltat_{k}\left( {\sqrt{{\parallel{\overline{\mathbf{u}}}_{k}\parallel}^{2} + \epsilon_{u}} + {{tr}\left\lbrack {{\hat{P}}_{k}Q_{k}} \right\rbrack} + {{tr}\left\lbrack {{\overset{\sim}{P}}_{k}Q_{k}} \right\rbrack} + {{tr}\left\lbrack {P_{u_{k}}R_{k}} \right\rbrack}} \right)}$ (61a)
$\varphi{({\mathbf{X}}_{N})}$ $= {{{tr}\left\lbrack {{\hat{P}}_{N}Q_{N}} \right\rbrack} + {{tr}\left\lbrack {{\overset{\sim}{P}}_{N}Q_{N}} \right\rbrack}}$ (61b)

where ${\Deltat_{k}}:={t_{k + 1} - t_{k}}$ is the discretization time step, $\epsilon_{u}$ is a small mass-leak parameter, $Q_{k} \succeq O_{n_{x}}$ and $R_{k} \succ O_{n_{u}}$ are weighting matrices, and $P_{u_{k}}:=P_{u_{k,0}} = {K_{k}{\hat{P}}_{k}K_{k}^{\top}}$; thus, the stochastic control penalty is evaluated only at the maneuver epochs.

The optimization results depend on the choice of the weighting matrices. With small weighting matrices, the solution is nearly fuel-optimal. In contrast, with large weighting matrices, the resulting solution becomes more observability-aware or uncertainty-robust: the optimized reference trajectory passes through a highly observable region, or the feedback gain keeps the spacecraft close to the reference trajectory, thereby reducing the covariances.

### Thrust magnitude constraint

The chance constraint on the thrust magnitude is given by

where ${\mathbf{u}}_{k}:={\mathbf{u}}_{k,0}$, $u_{\max}$ is the maximum thrust magnitude, and $\varepsilon_{u}$ is a risk bound. The sufficient condition derived in Ref. \[Oguri_undated-kc\] has the following convex form:

where $\parallel P_{u_{k}}\parallel$ is the spectral norm of $P_{u_{k}}$, ${n_{\sigma}{(\varepsilon_{u},n_{u})}} = \sqrt{\mathcal{Q}_{X \sim {\chi^{2}{(n_{u})}}}{({1 - \varepsilon_{u}})}}$, and $\mathcal{Q}_{X \sim {\chi^{2}{(n_{u})}}}{({1 - \varepsilon})}$ denotes the quantile function of the chi-squared distribution with $n_{u}$ degrees of freedom evaluated at probability $1 - \varepsilon$.

However, this convex formulation is not straightforward to handle in the PO-SDDP algorithm because the derivatives of the first term are singular when ${\parallel{\overline{\mathbf{u}}}_{k}\parallel} = 0$, and the derivatives of $\parallel P_{u_{k}}\parallel$ are also ill-conditioned when $P_{u_{k}}$ has repeated eigenvalues. We approximate Eq. using a smooth function based on the Schatten $p$-norm:

where the first term is regularized by the mass-leak parameter also used in Eq. (61a), and, in the second term, the spectral norm in Eq. is replaced by the Schatten $p$-norm. In this constraint, $P_{u_{k}}$ is also evaluated at the maneuver epoch, i.e., $P_{u_{k}} = P_{u_{k,0}}$. This Schatten surrogate overestimates $\sqrt{\parallel P_{u_{k}}\parallel}$ by a factor of $n_{u}^{{1/2}p}$ in the worst case.

### Terminal covariance constraint

The terminal covariance constraint is generally formulated as the matrix inequality

where $P_{f}$ represents the target state covariance.

The scalar inequality equivalent to Eq. can be written as

As mentioned in Section 4.3.2, the derivatives of the spectral norm are singular when the matrix $\mathcal{S}_{N}$ has repeated eigenvalues. For numerical stability, the logarithm of the normalized Schatten $p$-norm of $\mathcal{S}_{N}$ is introduced here:

This surrogate can underestimate $\parallel\mathcal{S}_{N}\parallel$ by a factor of $1/n_{x}^{1/p}$ in the worst case.

### Linear state chance constraint

A linear state chance constraint can be formulated as

where ${\mathbf{a}}_{s}$ and $b_{s}$ define a feasible half-space in which the spacecraft can move, and $\varepsilon_{x}$ is a risk bound. Under a Gaussian belief, the deterministic constraint that is necessary and sufficient for Eq. can be expressed as

where $\Psi^{- 1}{({1 - \varepsilon_{x}})}$ denotes the inverse cumulative distribution function at probability $1 - \varepsilon_{x}$. This constraint can be handled in the PO-SDDP algorithm without approximation.

## Numerical Examples

In this section, the PO-SDDP algorithm is demonstrated through three scenarios: the light-dark domain problem, the Earth-to-Mars transfer problem, and the halo orbit transfer in the Earth--Moon CR3BP. All computations are performed on a desktop computer (Intel Core i9-14900KF, 3.2 GHz).

In all scenarios, the stage and terminal cost functions are defined by Eq. (61a) and Eq. (61b), respectively. The initial augmented controls are set to zero, i.e., ${\mathbf{U}}_{k} = \mathbf{0}_{n_{U}}$ for all $k$, and the initial Lagrange multipliers for all constraints are also initialized with zero vectors. The Vern7 integrator from DifferentialEquations.jl \[rackauckas2017differentialequations\] is used to discretize the continuous dynamics, except for the light-dark domain problem, where the dynamics are linear.

To validate the optimization results, Monte Carlo analysis is conducted using 500 random initial states sampled from $\mathcal{N}{({\mathbf{x}}_{0},{{\overset{\sim}{P}}_{0} + {\hat{P}}_{0}})}$, with dynamical disturbances and random observations. For each sampled trajectory, the state is estimated using the standard EKF and controlled by the optimal policy given in Eq.. In the Monte Carlo analysis, the process-noise covariance is computed by numerically integrating the Lyapunov equation in Eq. to assess the accuracy of the trapezoidal approximation used in the optimization.

### Light-dark domain problem

Here, we consider the light-dark domain problem in which observation uncertainty varies with distance from a landmark. The state is defined by the two-dimensional position and velocity, ${\mathbf{x}} = {\lbrack r_{x}\quad r_{y}\quad v_{x}\quad v_{y}\rbrack}^{\top}$, and the dynamics are modeled as a double integrator described by the following discrete-time linear system:

with system matrices

where $\sigma_{p}$ and $\sigma_{v}$ are positive scalars representing the disturbance intensities of the position and velocity, respectively.

The observation is defined as the position with noise proportional to the distance from the landmark:

where $\sigma_{y,0}$ is a fixed observation-noise term and $\sigma_{y,1}$ is a coefficient for the noise proportional to the distance from the landmark position ${\lbrack l_{x}\quad l_{y}\rbrack}^{\top}$.

The key parameters in this scenario are summarized in Table 2. For the cost function, the weighting matrices are set to $Q_{k} = O_{n_{x}}$ and $R_{k} = I_{n_{u}}$, the scaling matrix in the trust-region subproblem is chosen as the identity matrix, i.e., $D_{tr} = I_{n_{U}}$, and the mass-leak parameter is set to $\epsilon_{u} = 10^{- 8}$. The stochastic thrust magnitude, terminal covariance, and linear state constraints are imposed, together with the terminal nominal-state constraint ${\overline{\mathbf{x}}}_{N} = {\mathbf{x}}_{f}$ where ${\mathbf{x}}_{f}$ denotes the target nominal state. The initial estimation-error and state-estimate covariances are both specified by the standard deviations ${\overset{\sim}{\sigma}}_{r_{0}} = {\hat{\sigma}}_{r_{0}} = {4 \times 10^{- 2}}$ and ${\overset{\sim}{\sigma}}_{v_{0}} = {\hat{\sigma}}_{v_{0}} = 10^{- 2}$, while the terminal target covariance is specified by $\sigma_{r_{f}} = {2 \times 10^{- 4}}$ and $\sigma_{v_{f}} = 10^{- 2}$. For the augmented Lagrangian method, the initial penalties are set to $1.0$ for all constraints, the penalty scaling factor is set to $2.0$, and the Schatten-norm parameters are chosen as $p = 1$ for the thrust magnitude constraint and $p = 8$ for the surrogate terminal covariance constraint.

Number of observations per stage

Initial nominal state

Target nominal state

Position noise coefficient

Velocity noise coefficient

Fixed observation noise

Distance-dependent noise coefficient

Risk bound of state

Risk bound of control

Half-space coefficient vector

Table 2: Parameters in the light-dark domain scenario

The nominal and sampled trajectories are shown in Fig. 3, where the nominal trajectory is plotted as a colored line, and the sampled trajectories are shown in gray. The nominal and sampled control profiles are also presented in Fig. 3. The region defined by $y > 3$ in the left panel of Fig. 3 is designated as a keep-out zone. Under the obtained control policy, the nominal trajectory approaches the landmark while proceeding toward the target state to obtain lower-noise position measurements. The trajectory then changes direction slightly below $y = 3$, leaving a margin to account for process noise and estimation error. The Monte Carlo sample trajectories also avoid entering the keep-out zone. For the thrust magnitude constraint, the nominal control sequence remains below the specified maximum acceleration, with a larger margin near the final stage. This increased margin helps reduce the terminal covariance because the system moves away from the landmark near the end of the trajectory, which increases the observation noise.

Figure 3: Nominal and sampled trajectories and control profiles in the light-dark domain problem

To clarify how the algorithmic formulation affects the solution, we compare PO-SDDP with belief-space iterative linear quadratic Gaussian (iLQG) \[Van_Den_Berg2012-fn\] and the SCP-based approach. Belief-space iLQG corresponds to a variant of the proposed method in which the state-estimate covariance is excluded from the state variables and the second-order STMs for the augmented dynamics are omitted. The SCP-based approach is implemented according to Ref. \[Kumagai2025-bl\] using JuMP.jl \[Lubin2023\] for general optimization modeling and Clarabel.jl \[Clarabel_2024\] as a semidefinite programming solver. The constraints and cost functions are selected to be consistent with the respective formulations of the methods being compared. In belief-space iLQG, the thrust magnitude, terminal covariance, and linear state constraints are imposed only for the nominal state and the estimation-error covariance. The cost function is defined without the state-estimate covariance term, since it is not included in the state variables. By contrast, the SCP-based approach can handle convex constraints expressed in terms of the spectral norm; therefore, Eqs. and are employed for the thrust magnitude and terminal covariance constraints, respectively. The cost function for the SCP-based approach follows the formulation in Ref. \[Kumagai2025-bl\]. However, with the same target covariance used for PO-SDDP and belief-space iLQG, the adopted SCP-based formulation does not yield a feasible converged solution satisfying the terminal covariance constraint. Therefore, the target covariance for the SCP-based approach is relaxed to $2.5P_{f}$.

Figure 4: Nominal and sampled trajectories and control profiles obtained by belief-space iLQG

Figure 5: Nominal and sampled trajectories and control profiles obtained by the SCP-based method

Figures 4 and 5 show the nominal and sampled trajectories obtained by belief-space iLQG and the SCP-based method, along with the corresponding control sequences. In the Monte Carlo analysis of belief-space iLQG, the feedback policy obtained in the backward pass is applied to the estimated state. The nominal trajectory generated by belief-space iLQG approaches the landmark in the same manner as that of the proposed method in order to reduce the estimation error. Because the state-estimate covariance and feedback gain are not included as optimization variables, the sampled trajectories and control sequences violate the keep-out zone and thrust magnitude constraints. As shown in Fig. 5, the SCP-based method yields a minimum-fuel solution with a robust feedback gain that guides the system directly to the target state while controlling the covariance to satisfy the terminal constraints.

Table 3 compares the fuel consumption, terminal covariance metric, and computational cost. The proposed method yields a navigation-aware trajectory while maintaining consistency between the predicted and Monte Carlo terminal covariance metrics. In contrast, belief-space iLQG underestimates the terminal uncertainty because the state-estimate covariance and optimized feedback gain are not included in its prediction. The SCP-based method obtains the lowest nominal fuel consumption under a relaxed covariance target, but it does not steer the trajectory toward the landmark because the EKF-related matrices are fixed during convexification. The lower runtime of belief-space iLQG mainly reflects its reduced state dimension.

Table 3: Comparison of the solutions for the light-dark domain scenario

### Earth-to-Mars transfer

Next, the PO-SDDP algorithm is applied to the design of a low-thrust Earth-to-Mars transfer with radiometric tracking. The state consists of the spacecraft position ${\mathbf{r}} \in {\mathbb{R}}^{2}$ and velocity ${\mathbf{v}} \in {\mathbb{R}}^{2}$ in the heliocentric inertial frame, i.e., ${\mathbf{x}} = {\lbrack{\mathbf{r}}^{\top}\quad{\mathbf{v}}^{\top}\rbrack}^{\top}$. The deterministic part of the continuous-time dynamics is given by

where $\mu_{s}$ is the gravitational parameter of the Sun.

The process noise is modeled using a two-dimensional reformulation of the Gates error model \[Gates1963-dv\]. In the original Gates model, the shutoff and resolution errors contribute to the uncertainty along the commanded thrust direction, whereas the pointing and autopilot errors contribute to the uncertainty orthogonal to that direction. The corresponding noise weighting matrix $G_{x}{({\mathbf{x}},{\mathbf{u}})}$ is defined as

The square-root factor of the covariance is written as

where the standard deviations orthogonal and parallel to the commanded thrust direction are defined by

Here, $\sigma_{ap}$, $\sigma_{pt}$, $\sigma_{res}$, and $\sigma_{sh}$ denote the autopilot, pointing, resolution, and shutoff errors, respectively. The commanded thrust direction is regularized as

For ${\parallel{\mathbf{u}}\parallel}^{2} \gg \epsilon_{u}$, this representation yields standard deviations approximately equal to $\sigma_{\parallel}$ along the commanded thrust direction and $\sigma_{\perp}$ in the orthogonal direction. The regularized direction vector preserves the directional structure of the original Gates model while keeping the noise model differentiable near zero thrust.

Range and range-rate observations between the spacecraft and Earth are modeled as

where ${\mathbf{ρ}}_{r} = {{\mathbf{r}} - {\mathbf{r}}_{e}}$, ${\mathbf{ρ}}_{v} = {{\mathbf{v}} - {\mathbf{v}}_{e}}$, ${\mathbf{r}}_{e}$ and ${\mathbf{v}}_{e}$ denote the Earth's position and velocity, respectively.

The initial and target states are listed in Table 4, and the key parameters for this scenario are summarized in Table 5. The transfer duration and the initial and target states are based on those used in the numerical examples of Refs. \[Ozaki2020-id, ridderhof2020chance\], except that the initial state is slightly modified to avoid a singularity in the observation model. In this scenario, the PO-SDDP algorithm is applied with three different shutoff-error values to compare the resulting solutions. To demonstrate that the proposed method can accommodate multiple observations, range and range-rate measurements are assumed to be available at three equally spaced epochs in each stage, including the subsequent maneuver epoch. Thus, the $N = 40$ maneuver sequence contains 120 intermediate belief-state transitions.

For the cost function, the weighting matrices are set to $Q_{k} = O_{n_{x}}$ and $R_{k} = I_{n_{u}}$, and the mass-leak parameter is set to $\epsilon_{u} = {10^{- 8}{({{mm}/s^{2}})}^{2}}$. The thrust magnitude constraint is imposed together with terminal constraints on the nominal state and terminal covariance. The initial estimation-error and state-estimate covariances are both specified by the standard deviations ${\overset{\sim}{\sigma}}_{r_{0}} = {\hat{\sigma}}_{r_{0}} = {10{km}}$ and ${\overset{\sim}{\sigma}}_{v_{0}} = {\hat{\sigma}}_{v_{0}} = {{0.1{km}}/s}$, while the terminal target covariance is specified by $\sigma_{r_{f}} = {{3.12 \times 10^{5}}{km}}$ and $\sigma_{v_{f}} = {{0.1{km}}/s}$. For the augmented Lagrangian method, the initial penalties are set to 1.0 for the thrust magnitude and terminal-state constraints and to $1 \times 10^{- 6}$ for the surrogate terminal covariance constraint, while the penalty scaling factor is set to 2.0 for all constraints. The Schatten-norm parameters are chosen as $p = 1$ for the thrust magnitude constraint and $p = 8$ for the surrogate terminal covariance constraint. In the trust-region subproblem, the scaling matrix is set to $D_{tr} = {{blkdiag}{(I_{n_{u}},{0.1I_{n_{u}n_{x}}})}}$, so that the terms corresponding to the feedback gain are one order of magnitude smaller than those corresponding to the nominal control. Using the identity scaling matrix fails to yield a solution that satisfies the surrogate terminal covariance constraints because the updates to the nominal control and feedback gain are treated as having comparable scales. The physical parameters are nondimensionalized using the length and time-scale factors listed in Table 5 to improve numerical stability during the optimization.

Table 4: Initial and target states for the Earth-to-Mars transfer scenario

Number of observations per stage

1.0 (low), 3.0 (medium), 4.0 (high)

Length scale factor

Time scale factor

Table 5: Parameters for the Earth-to-Mars transfer scenario

Figure 6 shows the nominal and sampled trajectories, with the deviations from the nominal trajectories exaggerated. The nominal control profiles and the sampled profiles from the Monte Carlo analysis are shown in Fig. 7, where the thrust azimuth is defined as ${atan2}{(u_{y},u_{x})}$. Figures 6 and 7 show that the nominal trajectories are nearly identical across the shutoff-error cases, whereas the thrusting durations, thrust margins, and correction maneuvers vary with the maneuver uncertainty. Thus, in this scenario, the proposed method primarily designs a feedback policy robust to maneuver errors rather than reshaping the nominal trajectory for improved observability.

Figure 6: Nominal and sampled trajectories for different shutoff errors, with deviations from the corresponding nominal trajectories exaggerated by a factor of 5

Figure 7: Nominal and sampled control profiles for different shutoff errors

Figure 8: Time histories of position and velocity errors relative to the nominal trajectory for the high-error case, together with the predicted 3 σ envelopes

Figure 8 shows that the sampled deviations remain mostly within the predicted $3\sigma$ envelopes for the high-error case. This result supports the accuracy of the trapezoidal approximation and the local covariance propagation used in the optimization. Table 6 shows that the required $\DeltaV$ increases with the shutoff-error level, reflecting the larger control margin required under stronger maneuver uncertainty.

Table 6: Comparison of Earth-to-Mars transfer solutions

### Halo orbit transfer in Earth--Moon CR3BP

As a third demonstration, the PO-SDDP algorithm is applied to an $L_{2}$-halo-to-$L_{1}$-halo transfer in the Earth--Moon CR3BP with radiometric tracking. The state consists of the three-dimensional position ${\mathbf{r}} \in {\mathbb{R}}^{3}$ and velocity ${\mathbf{v}} \in {\mathbb{R}}^{3}$ in the rotating frame with the origin at the barycenter of the system, i.e., ${\mathbf{x}} = {\lbrack{\mathbf{r}}^{\top}\quad{\mathbf{v}}^{\top}\rbrack}^{\top}$. The continuous-time dynamics are given by

where $\mu = {m_{2}/{({m_{1} + m_{2}})}}$ is the mass parameter of the CR3BP, and $m_{1}$ and $m_{2}$ denote the masses of the primary and secondary bodies, respectively. The relative position vectors to the two primaries are defined as ${\mathbf{ρ}}_{1} = {\lbrack{r_{x} + \mu}\quad r_{y}\quad r_{z}\rbrack}^{\top}$ and ${\mathbf{ρ}}_{2} = {\lbrack{r_{x} - {({1 - \mu})}}\quad r_{y}\quad r_{z}\rbrack}^{\top}$ with $\rho_{1} = {\|{\mathbf{ρ}}_{1}\|}$ and $\rho_{2} = {\|{\mathbf{ρ}}_{2}\|}$. The dynamical noise is modeled by a three-dimensional Gates error model obtained by extending the two-dimensional model described in Eq. and Eq.. The observations are modeled as range and range-rate measurements from the Earth in the rotating frame, as described in Eq., with ${\mathbf{r}}_{e} = {\lbrack{- {\mu0\ \ 0}}\rbrack}^{\top}$ and ${\mathbf{v}}_{e} = \mathbf{0}$.

The initial and target states are taken from Ref. \[Aziz2019-bw\], as listed in Table 7, and the key parameters are summarized in Table 8. In this scenario, two state-weighting matrices, $Q_{k} = {10I_{n_{x}}}$ and $Q_{k} = {500I_{n_{x}}}$ for all $k$, are considered in the cost function to compare the resulting solutions, while the control-weighting matrix is fixed at $R_{k} = I_{n_{u}}$ and the mass-leak parameter is set to $\epsilon_{u} = {{7.4 \times 10^{- 8}}{({{mm}/s^{2}})}^{2}}$. For the trust-region method, the scaling matrix in the trust-region subproblem is chosen as the identity matrix, i.e., $D_{tr} = I_{n_{U}}$. Here, the thrust magnitude constraint and the terminal constraint on the nominal state are imposed. For the augmented Lagrangian method, the initial penalties for the thrust magnitude and terminal-state constraints are both set to $1.0$, and the penalty scaling factor is set to $2.0$ for both constraints. The Schatten-norm parameter is chosen as $p = 1$ for the thrust magnitude constraint. The initial estimation-error covariance and state-estimate covariance are both defined from the standard deviations ${\overset{\sim}{\sigma}}_{r} = {\hat{\sigma}}_{r} = {10{km}}$ and ${\overset{\sim}{\sigma}}_{v} = {\hat{\sigma}}_{v} = {{0.1m}/s}$.

Table 7: Initial and target states for the halo orbit transfer scenario

Number of observations per stage

Time step for control

Table 8: Parameters for the halo-orbit transfer scenario

Figures 9 and 10 compare the nominal trajectories and control profiles. The thrust magnitude, azimuth (${atan2}{(u_{y},u_{x})}$), and elevation ($\arcsin{({u_{z}/{\parallel{\mathbf{u}}\parallel}})}$) histories in Fig. 10 show that the solution obtained with the large weighting matrix differs from the other solutions in the timing, magnitude, and three-dimensional directions of the thrust arcs. With the small weighting matrix, the PO-SDDP solution behaves as a robustified version of the deterministic DDP solution, producing a similar nominal trajectory with more conservative correction capability. With the large weighting matrix, the optimized trajectory follows a different manifold and requires shorter second and third thrusting arcs, indicating that the covariance-related terms can alter the nominal trajectory when they are weighted sufficiently.

Figures 11 and 12 show the corresponding Monte Carlo trajectories and control histories. The large-weighting solution exhibits smaller deviations from the nominal trajectory and requires less corrective maneuvering after the main thrust arcs.

Figure 9: Nominal trajectories projected onto the coordinate planes

Figure 10: Nominal control profiles for the halo-orbit transfer scenario

Figure 11: Nominal and sampled trajectories for the halo-orbit transfer scenario, with deviations from the corresponding nominal trajectories exaggerated by a factor of 3

Figure 12: Nominal and sampled control profiles for the halo-orbit transfer solutions with different weighting parameters

To clarify the differences between the solutions, nonlinearity and information analyses are conducted along the nominal trajectories. The results are shown in Fig. 13, where the nonlinearity index is defined using the finite-time Lyapunov exponent (FTLE) as

and the information index is defined from the cumulative information matrix with respect to the initial state:

where $C_{j}$ and $W_{j}$ denote the observation sensitivity matrix and the inverse observation-noise covariance matrix at each stage, respectively. The nonlinearity index reflects the local sensitivity of the dynamics, whereas the information index quantifies the cumulative information gain with respect to the initial state. As shown in Fig. 9 and Fig. 13, the large-weighting solution avoids the strongly nonlinear region near the Moon while maintaining comparable information gain. This behavior explains the reduced terminal dispersion reported in Table 9. The predicted and Monte Carlo terminal covariance traces are consistent in both PO-SDDP cases.

Figure 13: Nonlinearity and information indices along the nominal trajectories

Table 9: Comparison of the halo-orbit transfer solutions

## Conclusion

This paper presents a stochastic differential dynamic programming algorithm for partially observable trajectory optimization problems. In the algorithm, the control update is computed by explicitly considering the coupled evolution of the nominal trajectory, the state-estimation process, and the feedback policy, without relying on the separation principle. Constraints on thrust magnitude, terminal state, and covariance are handled using an augmented Lagrangian formulation. For computational efficiency, the method computes state transition matrices for covariance propagation semi-analytically and uses automatic differentiation to evaluate model-dependent derivatives.

The numerical results demonstrate three distinct capabilities of the proposed approach. In the light-dark domain problem, the method generates a navigation-aware solution that exploits an informative region while maintaining the path and thrust constraints and achieving terminal covariance performance close to the prescribed target. In the Earth-to-Mars transfer, it produces uncertainty-robust solutions under nonlinear dynamics, nonlinear observations, and maneuver execution errors. The periodic-orbit transfer in the Earth--Moon CR3BP shows that the method identifies solutions that exploit the coupling between trajectory design and orbit determination in a strongly nonlinear dynamical environment. The results indicate that the proposed framework provides a practical way to incorporate navigation performance and feedback robustness into mission design problems under partial observability.
