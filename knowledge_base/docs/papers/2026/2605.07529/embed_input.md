<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Stochastic Differential Dynamic Programming for Trajectory Optimization under Partial Observability

Topics include Differential dynamic programming, Trajectory optimization, Partial observability, Spacecraft guidance, Covariance control, Belief-space planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends stochastic differential dynamic programming to partially observable trajectory optimization problems where guidance, estimation, and correction maneuvers are coupled. The paper is especially relevant for spacecraft trajectory design because it incorporates orbit-determination uncertainty and maneuver-execution noise into the optimization loop.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Designing spacecraft trajectories remains challenging in the presence of stochastic effects such as maneuver execution errors and observation uncertainties. Although covariance control and belief-space planning provide useful tools for designing robust control policies and information-aware trajectories under uncertainty, practical methods remain limited for partially observable trajectory optimization problems in which trajectory design, orbit determination, and correction maneuver planning are tightly coupled. This paper presents a stochastic differential dynamic programming algorithm for such coupled problems. The proposed method optimizes the nominal control sequence and feedback gains subject to belief dynamics and general mission constraints, explicitly accounting for the dependence of covariance propagation on the nominal trajectory without relying on the separation principle. Numerical examples demonstrate that the proposed algorithm produces navigation-aware and uncertainty-robust solutions across a range of dynamical systems, observation models, and uncertainty levels. In particular, the circular restricted three-body problem shows that the proposed method can exploit the coupling between trajectory design and orbit determination to obtain navigation-aware solutions with substantially lower fuel consumption than those from deterministic local optimization starting from the same initial guess.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Spacecraft trajectory design under uncertainty becomes particularly challenging when the orbit-determination process depends on the nominal trajectory. In such problems, maneuver design and navigation design cannot be treated independently, because the trajectory determines the measurement geometry and the achievable navigation accuracy. This coupling is especially important in scenarios with weak observability, such as angles-only navigation or missions with limited tracking opportunities. Although high-quality measurements are often available in conventional missions, for example, through radiometric tracking with Delta-DOR in deep-space missions \[CurkendallBorder2013DeltaDOR\] or GNSS measurements in LEO missions \[AllahvirdiZadehWangElMowafy2022ASCE\], increasing mission complexity and operational cadence can limit such tracking opportunities. These considerations motivate a unified framework for partially observable trajectory optimization problems, in which maneuver design, orbit determination, and correction maneuver planning are tightly coupled under uncertainty.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In spaceflight applications, covariance control approaches \[HotzSkelton1987CovarianceControl\] have been developed to design maneuver policies under uncertainty using a variety of optimization techniques, including differential dynamic programming (DDP), nonlinear programming (NLP), and sequential convex programming (SCP). Refs. \[Ozaki2018-rx, Ozaki2020-id\] derive tube stochastic DDP, in which DDP is applied to a stochastic dynamical system sampled by the unscented transform. As a higher-fidelity approach, Ref. \[Greco2022-at\] presents an NLP-based method for optimal impulsive control in belief space, incorporating the orbit-determination process into uncertainty propagation via polynomial chaos expansion. Ref. \[Varghese2026-sh\] improves convergence of NLP with covariance dynamics by exploiting the forward--backward structure and introducing a feedback-gain parameterization that reduces the search space. SCP-based methods have also been extensively studied due to their tractability and the availability of efficient convex optimization solvers. For example, Ref.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

\[ridderhof2020chance\] formulates convexified discrete-time dynamics, costs, and constraints that can be solved iteratively even for nonlinear trajectory optimization, and Ref. \[Oguri_undated-kc\] incorporates stochastic mass dynamics and the orbit-determination process into an SCP framework. Because the feedback gain is parameterized as a block lower-triangular matrix that depends on past states at the discretization nodes in many of these approaches, the computational effort increases quadratically with the number of nodes. To improve the efficiency of covariance control with chance constraints, sequential semidefinite programming methods have also been proposed \[rapakoulias2023discretetimeoptimalcovariancesteering, pilipovsky2024computationallyefficientchanceconstrained\] and applied to astrodynamics problems in Ref. \[Kumagai2025-bl\].

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Planning under dynamical and observation uncertainties has also been studied extensively in the robotics community, where the problem is often formulated as a partially observable Markov decision process and addressed via belief-space planning \[KaelblingLittmanCassandra1998POMDP\]. Because belief-space planning is generally intractable due to its infinite-dimensional state space, practical methods often assume Gaussian beliefs and perform local approximations around a nominal trajectory. Ref. \[Platt2010-jq\] applies a linear quadratic regulator (LQR) to deterministic Gaussian belief-space dynamics under the assumption of maximum-likelihood observation (MLO). Refs. \[Van_Den_Berg2012-fn, Van_den_Berg2017-br\] remove the MLO assumption and propose iterative local optimization methods in belief space by expanding the cost function and dynamics around the nominal trajectory to obtain time-varying affine feedback policies. Ref. \[Indelman2015-jb\] further extends the framework by introducing random binary variables to model missed observations.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Related active-sensing trajectory generation methods have also been developed to improve estimation performance by shaping the nominal trajectory according to information-related criteria. These approaches are closely related to belief-space planning in that they exploit the coupling between motion and estimation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

These two lines of research offer complementary strengths. Covariance control approaches provide powerful tools for robust control policy design under uncertainty, whereas belief-space planning methods are effective for information-aware decision-making. However, partially observable trajectory optimization problems in which trajectory design, orbit determination, and correction maneuver planning must be addressed in a unified manner remain insufficiently studied. Many covariance control formulations simplify the coupling by assuming that the orbit-determination process can be separated from the trajectory optimization problem. As a result, they are not primarily designed to generate navigation-aware solutions in which the nominal trajectory is deliberately shaped to pass through information-rich regions. In contrast, belief-space planning methods primarily emphasize information gathering through nominal-trajectory design and generally do not explicitly optimize feedback policies under general mission constraints. Thus, the joint optimization of informative nominal trajectories and feedback policies under general mission constraints remains a challenging problem in spacecraft mission design.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address this gap, we develop a partially observable stochastic differential dynamic programming (PO-SDDP) framework for partially observable trajectory optimization problems. The proposed framework enables simultaneous optimization of the nominal control and feedback gains while explicitly accounting for state estimation and covariance propagation under general mission constraints. The main technical contributions are as follows. First, we formulate a generalized belief-space DDP framework by augmenting the belief-space transition model with the state-estimate covariance and by treating the feedback gain as an optimization variable. Second, we develop a practical formulation for spacecraft mission design by combining an augmented Lagrangian method with regularized or smooth approximations of representative cost functions and constraints, including thrust magnitude and guidance accuracy constraints. Third, we develop a semi-analytic method to efficiently compute the state transition matrices for covariance propagation, together with automatic differentiation for model-dependent derivatives and model-independent tensor operations for covariance propagation.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

From an algorithmic perspective, the proposed method is rooted in stochastic differential dynamic programming \[Theodorou2010-xy\] and related DDP-based covariance control methods for nonlinear stochastic systems \[Yi2020-mz\]. The main distinction is that the proposed method formulates the local optimization problem in belief space, explicitly accounting for the dependence of navigation performance on the nominal trajectory. An observability-aware DDP approach \[fujiwara2024\] is also closely related to the present work. Compared with that approach, the proposed method can be interpreted as a stochastic extension that incorporates covariance propagation and feedback-gain optimization into the DDP recursion. An earlier version of this work appeared in Ref. \[fujiwara\]. This manuscript extends the conference paper by providing a more rigorous derivation of the dynamics, additional implementation details, and an expanded numerical analysis.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate the proposed algorithm through three numerical examples: the light-dark domain problem, an Earth-to-Mars planar transfer, and a periodic-orbit transfer in the Earth--Moon circular restricted three-body problem (CR3BP). These examples show that the method can address a broad range of problems, from information-aware trajectory shaping to robust correction maneuver design.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is organized as follows. Section 2 derives a belief-space transition model defined by the dynamics, observation model, and uncertainty model. In Section 3, we introduce the partially observable stochastic DDP algorithm. Section 4 presents semi-analytic computations of the state transition matrices for covariance propagation, together with representative cost functions and constraints applicable to space mission design using smoothed approximations. Section 5 presents the numerical results, and Section 6 concludes the paper.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Belief Propagation for Partially Observable Trajectory Optimization Problems", "weight": 1.0} -->

This section derives a tractable belief-space transition model for partially observable trajectory optimization. In belief-space planning, decisions are made based on a belief over the state rather than the unobserved true state. Our objective is to construct belief-space dynamics for mission design when future observations are unknown. To this end, we approximate the belief using up to second-order moments and derive propagation equations for two covariance matrices: the estimation-error covariance and the state-estimate covariance. These covariance dynamics, together with the nominal dynamics, constitute the belief-space transition model used in the subsequent DDP algorithm.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Dynamics, observations, and time discretization", "weight": 1.0} -->

We consider a controlled stochastic system over the mission design interval $t \in {\lbrack t_{0},t_{f}\rbrack}$, with state ${{\mathbf{x}}{(t)}} \in {\mathbb{R}}^{n_{x}}$ and control ${{\mathbf{u}}{(t)}} \in {\mathbb{R}}^{n_{u}}$. The true state evolves according to the continuous-time stochastic dynamics

<!-- chunk {"id": "body-0016", "role": "body", "section": "Dynamics, observations, and time discretization", "weight": 1.0} -->

To discretize the stochastic dynamics in Eq., the optimization interval $\lbrack t_{0},t_{f}\rbrack$ is partitioned by maneuver and observation epochs. Let $N_{j}{(k)}$ denote the number of observation epochs between the $k$-th and $({k + 1})$-th maneuver epochs. When ${N_{j}{(k)}} > 0$, these observation epochs are ordered as

<!-- chunk {"id": "body-0017", "role": "body", "section": "Dynamics, observations, and time discretization", "weight": 1.0} -->

where epochs with a single subscript, except for the terminal epoch $t_{N} = t_{f}$, correspond to maneuver epochs, whereas epochs with double subscripts correspond to observation epochs. Without loss of generality, we define $t_{k,0}:=t_{k}$ and $t_{k,{{N_{j}{(k)}} + 1}}:=t_{k + 1}$. Thus, although $N_{j}{(k)}$ denotes the number of observation epochs, the interval between two consecutive maneuver epochs contains ${N_{j}{(k)}} + 1$ intermediate transitions. Here, the final observation epoch between two consecutive maneuver epochs is allowed to coincide with the latter maneuver epoch.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Dynamics, observations, and time discretization", "weight": 1.0} -->

In such a case, the observation is obtained just before performing the maneuver using the latest orbit-determination result, and therefore $t_{k,{N_{j}{(k)}}} = t_{k,{{N_{j}{(k)}} + 1}} = t_{k + 1}$. Moreover, different observation sources may be available at different observation epochs. This partitioning is applicable to general space mission design problems.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Dynamics, observations, and time discretization", "weight": 1.0} -->

Observations at each epoch are modeled as

<!-- chunk {"id": "body-0020", "role": "body", "section": "Dynamics, observations, and time discretization", "weight": 1.0} -->

Here, $W_{k,j}{({\mathbf{x}}_{k,j})}$ is defined as the inverse matrix of the observation noise covariance. We assume that ${\mathbf{h}}_{k,j}$ and $G_{y_{k,j}}$ may vary with the epoch $t_{k,j}$ to enable handling different observation types and dimensions across epochs, and that ${\mathbf{w}}_{y_{k,j}}$ is mutually independent across epochs and independent of the process noise ${\mathbf{w}}_{x}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Belief representation", "weight": 1.0} -->

where $\eta_{k,{j + 1}}$ is a normalizing constant independent of ${\mathbf{x}}_{k,{j + 1}}$. In general, Eq. yields an infinite-dimensional probability distribution that does not admit a closed-form representation. To address this issue, we first define the state estimate and the estimation-error covariance as

<!-- chunk {"id": "body-0022", "role": "body", "section": "Belief representation", "weight": 1.0} -->

In the mission design phase, future observations have not yet been realized. Therefore, ${\hat{\mathbf{x}}}_{k,j}$ is treated as a random variable induced by the process and observation noises, whereas ${\overset{\sim}{P}}_{k,j}$ may also depend on the realized trajectory and observations in the general nonlinear filtering problem. We further define the nominal state and the state-estimate covariance as

<!-- chunk {"id": "body-0023", "role": "body", "section": "Belief representation", "weight": 1.0} -->

and the covariance of the true state is given by

<!-- chunk {"id": "body-0024", "role": "body", "section": "Belief representation", "weight": 1.0} -->

where ${\overset{\sim}{P}}_{k,j}^{nom}$ is approximated as a deterministic function of the nominal state ${\overline{\mathbf{x}}}_{k,j}$, the nominal control ${\overline{\mathbf{u}}}_{k}$, and the assumed process- and observation-noise statistics. Eq. and Eq. are consistent with the derivation in Ref. \[Ridderhof2020-cm\]. Under the assumption that the true state lies in the vicinity of the nominal state, we approximate ${\overset{\sim}{P}}_{k,j} \approx {\overset{\sim}{P}}_{k,j}^{nom}$; that is, the estimation-error covariance obtained from the Bayesian filter is close to its nominal value. This approximation is justified when the deviation from the nominal trajectory remains sufficiently small. Therefore, the estimation-error covariance is evaluated along the nominal trajectory and treated deterministically under this approximation.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Linearization of dynamics", "weight": 1.0} -->

Given a nominal trajectory $({\overline{\mathbf{x}}{(t)}},{\overline{\mathbf{u}}{(t)}})$, the linearized dynamics describing the evolution of the state deviation $\delta{\mathbf{x}}{(t)}$ are given by

<!-- chunk {"id": "body-0026", "role": "body", "section": "Linearization of dynamics", "weight": 1.0} -->

where ${\mathbf{w}}_{x}$ denotes an independent Gaussian random vector with zero mean and identity covariance. The matrices ${\overline{A}}_{k,j}$ and ${\overline{B}}_{k,j}$ are given by

<!-- chunk {"id": "body-0027", "role": "body", "section": "Linearization of dynamics", "weight": 1.0} -->

where $\Phi_{A}{(t_{2},t_{1})}$ denotes the state transition matrix along the nominal trajectory from $t_{1}$ to $t_{2}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Linearization of observations and statistical residuals", "weight": 1.0} -->

By substituting Eq. and Eq. into Eq. and linearizing the observation model about the nominal trajectory, the first-order approximation of the observation residual is obtained as

<!-- chunk {"id": "body-0029", "role": "body", "section": "Linearization of observations and statistical residuals", "weight": 1.0} -->

collects random quantities affecting the observation residual. The first- and second-order moments of ${\mathbf{ξ}}_{k,j^{-}}$ are given by

<!-- chunk {"id": "body-0030", "role": "body", "section": "Linearization of observations and statistical residuals", "weight": 1.0} -->

and the covariance of the observation residual is defined as

<!-- chunk {"id": "body-0031", "role": "body", "section": "Linearization of observations and statistical residuals", "weight": 1.0} -->

The residual $\delta{\mathbf{y}}_{k,j^{-}}$, commonly referred to as the observed-minus-computed (O-C) term in spacecraft orbit determination, is evaluated from the actual observation data and the prior state estimate. In this study, $\delta{\mathbf{y}}_{k,j^{-}}$ is treated as a random variable characterized by ${\mathbf{ξ}}_{k,j^{-}}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Filtered and nominal dynamics", "weight": 1.0} -->

Following Ref. \[Spinello2010-kl\], we adopt the extended Kalman filter (EKF) formulation for state-dependent observation noise derived from Bayes' theorem (cf. Eq. ). The posterior estimate ${\hat{\mathbf{x}}}_{k,{j + 1}}$ is given by the maximum a posteriori (MAP) estimate, i.e., the solution of

<!-- chunk {"id": "body-0033", "role": "body", "section": "Filtered and nominal dynamics", "weight": 1.0} -->

Since the observation ${\mathbf{y}}_{k,{j + 1}}$ is uncertain and treated as a random variable in the mission design phase, we approximate the state-dependent noise covariance by fixing $W_{k,{j + 1}}^{- 1}$ at the nominal state ${\overline{\mathbf{x}}}_{k,{j + 1}}$. We define the fixed observation-noise covariance as

<!-- chunk {"id": "body-0034", "role": "body", "section": "Filtered and nominal dynamics", "weight": 1.0} -->

Consequently, the MAP estimate is approximated as

<!-- chunk {"id": "body-0035", "role": "body", "section": "Filtered and nominal dynamics", "weight": 1.0} -->

Here, $\Lambda_{k,{j + 1}}$ is the posterior information matrix defined as

<!-- chunk {"id": "body-0036", "role": "body", "section": "Filtered and nominal dynamics", "weight": 1.0} -->

The prior state estimate and estimation-error covariance at $t_{k,{j + 1}}$ are propagated from the posterior quantities at $t_{k,j}$ as

<!-- chunk {"id": "body-0037", "role": "body", "section": "Filtered and nominal dynamics", "weight": 1.0} -->

where ${\mathbf{f}}_{k,j}{({\hat{\mathbf{x}}}_{k,j},{\mathbf{u}}_{k,j})}$ denotes the discrete-time nonlinear dynamics obtained by numerically integrating the deterministic part of Eq.. Under the Gaussian-belief assumption, the MAP estimate in Eq. coincides with the conditional expectation ${\mathbb{E}}\left\lbrack {{\mathbf{x}}_{k,{j + 1}} \mid {{\overline{\mathbf{u}}}_{0:k},{\mathbf{Y}}_{k - 1},{\mathbf{y}}_{{k,1}:{j + 1}}}} \right\rbrack$, because the posterior is Gaussian and its mean and mode are identical. Note that this equivalence does not hold in general for non-Gaussian posteriors.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Filtered and nominal dynamics", "weight": 1.0} -->

Since all terms in Eq., Eq., and Eq. are evaluated along the nominal trajectory, e.g., at ${\overline{\mathbf{x}}}_{k,j}$ and ${\overline{\mathbf{x}}}_{k,{j + 1}}$, the resulting propagation is more accurately described as a linearized Kalman filter than as the standard EKF, in which the matrices are evaluated at the latest state estimate ${\hat{\mathbf{x}}}_{k,j}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Filtered and nominal dynamics", "weight": 1.0} -->

Under the first-order approximation ${\mathbf{e}}_{k,{j + 1}} \approx {\delta{\mathbf{y}}_{k,{j + 1}}^{-}}$, substituting Eq. into Eq. (25a) yields

<!-- chunk {"id": "body-0040", "role": "body", "section": "Filtered and nominal dynamics", "weight": 1.0} -->

Accordingly, the intermediate propagation with state estimation can be written as

<!-- chunk {"id": "body-0041", "role": "body", "section": "Filtered and nominal dynamics", "weight": 1.0} -->

and the propagation of the estimation-error covariance is then approximated by

<!-- chunk {"id": "body-0042", "role": "body", "section": "Filtered and nominal dynamics", "weight": 1.0} -->

By taking the expectation of both sides of Eq. and applying the first-order approximation, the nominal dynamics are approximated as

<!-- chunk {"id": "body-0043", "role": "body", "section": "Belief-state transition model", "weight": 1.0} -->

Although the nominal control ${\overline{\mathbf{u}}}_{k}$ and feedback gain $K_{k}$ are held fixed within each stage, the feedback correction is recomputed at each intermediate epoch using the latest state estimate. Thus, for $t \in {\lbrack t_{k,j},t_{k,{j + 1}})}$, the applied control is modeled as

<!-- chunk {"id": "body-0044", "role": "body", "section": "Belief-state transition model", "weight": 1.0} -->

By substituting Eq. into Eq. and expanding to first order about the nominal trajectory, the propagation of the estimate deviation is approximated as

<!-- chunk {"id": "body-0045", "role": "body", "section": "Belief-state transition model", "weight": 1.0} -->

The propagation of the state-estimate covariance is then given by

<!-- chunk {"id": "body-0046", "role": "body", "section": "Belief-state transition model", "weight": 1.0} -->

By vectorizing the belief state, we define the augmented state and control as

<!-- chunk {"id": "body-0047", "role": "body", "section": "Belief-state transition model", "weight": 1.0} -->

where the feedback gain $K_{k}$ is included in the augmented control to explicitly consider ${\hat{P}}_{k}$ as controlled variables for the future distribution. Accordingly, the intermediate belief-state transition model can be written as

<!-- chunk {"id": "body-0048", "role": "body", "section": "Belief-state transition model", "weight": 1.0} -->

where ${\mathbf{F}}_{k,j}\left( {\mathbf{X}}_{k,j},{\mathbf{U}}_{k} \right)$ concatenates the transition model of the nominal state, the estimation-error covariance, and the state-estimate covariance, described in Eqs. and, respectively.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Belief-state transition model", "weight": 1.0} -->

For use in trajectory optimization algorithms, the stage-to-stage belief-state transition must be written directly as a function of ${\mathbf{X}}_{k}$ and ${\mathbf{U}}_{k}$, because ${\mathbf{X}}_{k,j}$ is an intermediate variable determined by these quantities. Letting ${\mathbf{X}}_{k}:={\mathbf{X}}_{k,0}$, the belief-state transition model from $t_{k}$ to $t_{k + 1}$ is obtained by sequentially applying Eq.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Belief-state transition model", "weight": 1.0} -->

To obtain the posterior distribution $p{({{\mathbf{x}}_{k + 1} \mid {{\mathbf{Y}}_{k},{\mathbf{U}}_{k}}})}$, Bayes' rule may also be applied directly, as in Ref. \[Indelman2015-jb\]. In that case, only the distribution linking ${\mathbf{x}}_{k}$ and ${\mathbf{x}}_{k + 1}$ conditioned on the observation sequence ${\mathbf{Y}}_{k}$ is of interest, since all intermediate states ${\mathbf{x}}_{k,j}$ can be marginalized out. However, when the dynamical system contains process noise, filtering conditioned on ${\mathbf{Y}}_{k}$ induces strong correlations among observations, as shown in Ref. \[Carpenter2023-qo, Eq. \]. These correlations lead to cumbersome algorithmic implementation, particularly in the partial derivatives of the belief-state transition model.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Belief-state transition model", "weight": 1.0} -->

For this reason, sequential propagation with intermediate states is adopted in this study.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Belief-state transition model", "weight": 1.0} -->

The dimensions of the augmented state and control are $n_{X} = {n_{x} + {2n_{x}^{2}}}$ and $n_{U} = {n_{u} + {n_{u}n_{x}}}$, respectively. Using square-root factors of the covariance matrices exploits symmetric structure and reduces the dimension of the augmented state to $n_{x} + {n_{x}{({n_{x} + 1})}}$. Although square-root representations may improve numerical stability and reduce dimensionality, we deliberately retain the full covariance matrices in this study because evaluating the state transition matrices for the belief-state transition model is simpler than with square-root factors, which require QR decompositions and second-order differentiation through them.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Partially Observable Stochastic Differential Dynamic Programming", "weight": 1.0} -->

This section presents the PO-SDDP algorithm for solving partially observable trajectory optimization problems. The algorithm applies a DDP-based method with an augmented Lagrangian formulation to the deterministic belief-state transition model derived in the previous section.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Partially Observable Stochastic Differential Dynamic Programming", "weight": 1.0} -->

For the nonlinear partially observable problem considered in this study, the separation principle does not generally decouple state estimation from trajectory optimization. The covariance dynamics are evaluated along the nominal trajectory being optimized; therefore, their coefficients vary with the nominal state and control inputs. This coupling appears through matrices such as ${\overline{A}}_{k,j}$, ${\overline{B}}_{k,j}$, ${\overline{G}}_{x_{k,j}}$, ${\overline{C}}_{k,{j + 1}}$, ${\overline{S}}_{k,{j + 1}}$, $\mathcal{A}_{k,j}$, and $\mathcal{F}_{k,{j + 1}}$, which depend on $({\overline{\mathbf{x}}}_{k,j},{\overline{\mathbf{u}}}_{k})$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Partially Observable Stochastic Differential Dynamic Programming", "weight": 1.0} -->

Consequently, the augmented dynamics in Eq. must be differentiated with respect to the full augmented state and control. The DDP backward pass then uses the first- and second-order derivatives of this augmented transition map to construct local quadratic subproblems.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Augmented Lagrangian method", "weight": 1.0} -->

Although various approaches have been developed to handle constraints in DDP, including active-set methods \[Lantoine2012-ak, Xie2017-ma\] and interior-point DDP \[Pavlov2021-ll\], the proposed method adopts the augmented Lagrangian DDP (AL-DDP) framework \[howell2019altro, Pellegrini2020-ep\].

<!-- chunk {"id": "body-0057", "role": "body", "section": "Augmented Lagrangian method", "weight": 1.0} -->

In AL-DDP, the stage and terminal constraints are incorporated into the cost function. The resulting augmented cost function is defined as

<!-- chunk {"id": "body-0058", "role": "body", "section": "Augmented Lagrangian method", "weight": 1.0} -->

For a generic inequality constraint vector ${\mathbf{c}} \in {\mathbb{R}}^{n_{c}}$, the penalty for inequality constraints is defined componentwise as

<!-- chunk {"id": "body-0059", "role": "body", "section": "Augmented Lagrangian method", "weight": 1.0} -->

The AL-DDP algorithm consists of nested inner and outer loops. In the inner loop, DDP locally optimizes the control sequence by solving the unconstrained problem defined by the augmented cost function via backward and forward passes. After the inner loop has approximately converged, the outer loop updates the Lagrange multipliers and penalty parameters. The Lagrange multipliers and penalty parameters are updated as

<!-- chunk {"id": "body-0060", "role": "body", "section": "Augmented Lagrangian method", "weight": 1.0} -->

where the maximum operation is applied componentwise, and $\gamma_{k,\mathcal{I}}$ and $\gamma_{k,\mathcal{E}}$ are penalty scaling constants.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Backward pass", "weight": 1.0} -->

Given the augmented cost function in Eq., the value function satisfies the Bellman recursion

<!-- chunk {"id": "body-0062", "role": "body", "section": "Backward pass", "weight": 1.0} -->

with the terminal condition ${J_{N}^{\ast}{({\mathbf{X}}_{N})}} = {\overset{\sim}{\varphi}{({\mathbf{X}}_{N})}}$, where $J_{k + 1}^{\ast}{({{\mathbf{F}}_{k}\left( {\mathbf{X}}_{k},{\mathbf{U}}_{k} \right)})}$ denotes the optimal cost-to-go, representing the future cost along the trajectory controlled by the optimal policy. In the backward pass, the control variations are obtained through minimizing the quadratic expansion of the cost-to-go function from the terminal stage to the initial one.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Backward pass", "weight": 1.0} -->

where $\Phi_{k}^{1}$ and $\Phi_{k}^{2}$ denote the first- and second-order state transition matrices (STMs) from $t_{k}$ to $t_{k + 1}$, and $( \cdot )$ denotes a vector-tensor contraction. The STMs are associated with the combined dynamics defined as

<!-- chunk {"id": "body-0064", "role": "body", "section": "Backward pass", "weight": 1.0} -->

since the controls are modeled as the zero-order-hold continuous thrust input. By expanding the cost-to-go function up to second order, the derivatives of the local quadratic expansion are written as

<!-- chunk {"id": "body-0065", "role": "body", "section": "Backward pass", "weight": 1.0} -->

If $J_{{UU},k}$ is not positive definite, the resulting control update may fail to satisfy a descent condition. To address this issue, the algorithm incorporates a trust-region method that regularizes $J_{{UU},k}$ and restricts the control update $\delta{\mathbf{U}}_{k}$ to a region where the quadratic approximation remains valid. The trust-region subproblem is given by

<!-- chunk {"id": "body-0066", "role": "body", "section": "Backward pass", "weight": 1.0} -->

where $\parallel \cdot \parallel$ denotes the Euclidean norm, $D_{tr}$ is a positive definite scaling matrix and $\Delta$ is the trust-region radius. The matrix $D_{tr}$ defines a hyperellipsoid in the control space of ${\mathbf{U}}_{k}$. Using the regularized Hessian ${\overset{\sim}{J}}_{{UU},k} = {J_{{UU},k} + {\gammaD_{tr}^{\top}D_{tr}}}$ where $\gamma$ is the Lagrange multiplier associated with the trust-region constraint, the optimal local control update is obtained as

<!-- chunk {"id": "body-0067", "role": "body", "section": "Forward pass", "weight": 1.0} -->

After the backward pass, a candidate reference trajectory is generated using the latest control policy.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Forward pass", "weight": 1.0} -->

The total cost of the updated reference trajectory is then evaluated as

<!-- chunk {"id": "body-0069", "role": "body", "section": "Forward pass", "weight": 1.0} -->

The ratio of the actual cost reduction $J_{0}^{({i + 1})} - J_{0}^{(i)}$ to the expected reduction ${ER}_{0}$ is then used to determine whether the candidate reference trajectory is accepted. If the candidate is accepted, the algorithm proceeds to the next iteration by reevaluating the quadratic expansions of the belief-state transition model ${\mathbf{F}}_{Z,k}$, stage cost ${\overset{\sim}{L}}_{k}$, and terminal cost $\overset{\sim}{\varphi}$ around the updated reference trajectory $\left( {\mathbf{X}}_{k}^{({i + 1})},{\mathbf{U}}_{k}^{({i + 1})} \right)$. Otherwise, the backward pass is repeated with a reduced trust-region radius $\Delta$ while reusing previously computed derivatives until the control update is accepted.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

In this section, we describe implementation details that enhance the numerical stability and computational efficiency of the proposed framework. Specifically, we compute the first- and second-order derivatives of the covariance dynamics semi-analytically by reusing derivatives of the nominal dynamics, and introduce representative cost and constraint formulations for space mission design, smoothed by using Schatten-norm surrogates.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Partial derivatives of covariance propagation", "weight": 1.0} -->

The most computationally expensive part of the framework is the computation of the first- and second-order STMs required for covariance propagation. Direct application of finite differences or automatic differentiation (AD) is computationally prohibitive because of the high dimensionality of the augmented dynamics. By exploiting the dependence of the covariance matrices on the nominal state and control, the STMs for covariance propagation can instead be computed from analytic derivatives expressed in terms of the STMs of the nominal-state dynamics. For example, the derivatives of the prior estimation-error covariance with respect to the nominal state can be written in terms of tensor multiplications as

<!-- chunk {"id": "body-0072", "role": "body", "section": "Partial derivatives of covariance propagation", "weight": 1.0} -->

where repeated superscripts follow the summation convention. On the right-hand side, the derivative of ${\overline{A}}_{k,j}$ with respect to $x_{k,j}$ corresponds to the second-order STMs of the nominal dynamics, whereas the derivative of ${\overline{G}}_{x_{k,j}}$ with respect to $x_{k,j}$ can be obtained through AD.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Partial derivatives of covariance propagation", "weight": 1.0} -->

The procedure for computing the STMs of the nominal dynamics is summarized in the Appendix. Because these derivatives correspond to the belief-state transition over each intermediate interval from $t_{k,j}$ to $t_{k,{j + 1}}$, the Appendix also describes how the intermediate STMs are composed to obtain the stage-to-stage STMs.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Partial derivatives of covariance propagation", "weight": 1.0} -->

In the second-order derivatives of covariance propagation, the third-order derivatives of the nominal-state dynamics emerge, for example,

<!-- chunk {"id": "body-0075", "role": "body", "section": "Partial derivatives of covariance propagation", "weight": 1.0} -->

The current implementation omits these terms to reduce computational burden. The effect of this approximation is mitigated in practice by the trust-region method in the backward pass, which limits the update when the quadratic expansion does not accurately predict the cost reduction.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Partial derivatives of covariance propagation", "weight": 1.0} -->

Accordingly, the problem-dependent implementation effort is largely reduced to specifying the dynamics, observation models, and uncertainty models. The corresponding model-dependent derivatives can be evaluated using AD, whereas the tensor operations associated with covariance propagation are handled independently of the model.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Approximation of discretized process noise", "weight": 1.0} -->

As described in Section 2.3, the discretized process-noise matrix ${\overline{G}}_{x_{k,j}}$ must be computed in the discretization procedure. This section introduces the approximation approach used in this study.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Approximation of discretized process noise", "weight": 1.0} -->

from $t_{k,j}$ to $t_{k,{j + 1}}$ with the initial condition ${\overline{Q}{(t_{k,j})}} = O_{n_{x}}$. The matrix ${\overline{G}}_{x_{k,j}}$ can then be obtained from a Cholesky decomposition of ${\overline{Q}}_{k,j}$. Because the additional numerical integration of $\overline{Q}{(t)}$ increases the computational cost, the PO-SDDP algorithm instead uses the trapezoidal rule to approximate ${\overline{G}}_{x_{k,j}}$. Using the first-order STM ${\overline{A}}_{k,j}$, Eq. is approximated as

<!-- chunk {"id": "body-0079", "role": "body", "section": "Approximation of discretized process noise", "weight": 1.0} -->

so that ${\overline{Q}}_{k,j} = {{\overline{G}}_{x_{k,j}}{\overline{G}}_{x_{k,j}}^{\top}}$. This approximation is significantly faster than numerically integrating Eq. and more accurate than the Euler approximation used in Refs. \[Theodorou2010-xy, Yi2020-mz\].

<!-- chunk {"id": "body-0080", "role": "body", "section": "Representative cost functions and constraints", "weight": 1.0} -->

Since the covariance matrices ${\overset{\sim}{P}}_{k}$ and ${\hat{P}}_{k}$, together with the linear feedback gain $K_{k}$, are included in the state and control vectors, the costs and constraints can be formulated explicitly as functions of these quantities. In other words, the proposed method can handle stochastic costs and chance constraints expressed in terms of moments up to second order. Here, we introduce representative cost functions and constraints commonly used in spacecraft trajectory design, including minimum-fuel costs with covariance penalties, a stochastic thrust magnitude constraint, terminal covariance constraints, and linear state chance constraints. The cost functions and constraints introduced here are twice continuously differentiable with respect to the reference trajectory $\left( {\overline{\mathbf{X}}}_{k},{\overline{\mathbf{U}}}_{k} \right)$ and can therefore be incorporated into the proposed method. If different cost functions or constraints are introduced, their derivatives can also be evaluated using AD, although analytic implementations are significantly faster in practice.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Cost functions", "weight": 1.0} -->

The stage and terminal cost functions are defined as the sum of the smoothed $\ell_{2}$-norm of the nominal control and quadratic penalties on the deviations of the state and control from the nominal trajectory. The cost functions are written as

<!-- chunk {"id": "body-0082", "role": "body", "section": "Cost functions", "weight": 1.0} -->

The optimization results depend on the choice of the weighting matrices. With small weighting matrices, the solution is nearly fuel-optimal. In contrast, with large weighting matrices, the resulting solution becomes more observability-aware or uncertainty-robust: the optimized reference trajectory passes through a highly observable region, or the feedback gain keeps the spacecraft close to the reference trajectory, thereby reducing the covariances.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Thrust magnitude constraint", "weight": 1.0} -->

The chance constraint on the thrust magnitude is given by

<!-- chunk {"id": "body-0084", "role": "body", "section": "Thrust magnitude constraint", "weight": 1.0} -->

where ${\mathbf{u}}_{k}:={\mathbf{u}}_{k,0}$, $u_{\max}$ is the maximum thrust magnitude, and $\varepsilon_{u}$ is a risk bound. The sufficient condition derived in Ref.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Thrust magnitude constraint", "weight": 1.0} -->

However, this convex formulation is not straightforward to handle in the PO-SDDP algorithm because the derivatives of the first term are singular when ${\parallel{\overline{\mathbf{u}}}_{k}\parallel} = 0$, and the derivatives of $\parallel P_{u_{k}}\parallel$ are also ill-conditioned when $P_{u_{k}}$ has repeated eigenvalues. We approximate Eq.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Thrust magnitude constraint", "weight": 1.0} -->

where the first term is regularized by the mass-leak parameter also used in Eq. (61a), and, in the second term, the spectral norm in Eq. is replaced by the Schatten $p$-norm. In this constraint, $P_{u_{k}}$ is also evaluated at the maneuver epoch, i.e., $P_{u_{k}} = P_{u_{k,0}}$. This Schatten surrogate overestimates $\sqrt{\parallel P_{u_{k}}\parallel}$ by a factor of $n_{u}^{{1/2}p}$ in the worst case.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Terminal covariance constraint", "weight": 1.0} -->

The terminal covariance constraint is generally formulated as the matrix inequality

<!-- chunk {"id": "body-0088", "role": "body", "section": "Terminal covariance constraint", "weight": 1.0} -->

where $P_{f}$ represents the target state covariance.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Terminal covariance constraint", "weight": 1.0} -->

The scalar inequality equivalent to Eq. can be written as

<!-- chunk {"id": "body-0090", "role": "body", "section": "Terminal covariance constraint", "weight": 1.0} -->

As mentioned in Section 4.3.2, the derivatives of the spectral norm are singular when the matrix $\mathcal{S}_{N}$ has repeated eigenvalues.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Terminal covariance constraint", "weight": 1.0} -->

This surrogate can underestimate $\parallel\mathcal{S}_{N}\parallel$ by a factor of $1/n_{x}^{1/p}$ in the worst case.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Linear state chance constraint", "weight": 1.0} -->

A linear state chance constraint can be formulated as

<!-- chunk {"id": "body-0093", "role": "body", "section": "Linear state chance constraint", "weight": 1.0} -->

where ${\mathbf{a}}_{s}$ and $b_{s}$ define a feasible half-space in which the spacecraft can move, and $\varepsilon_{x}$ is a risk bound. Under a Gaussian belief, the deterministic constraint that is necessary and sufficient for Eq. can be expressed as

<!-- chunk {"id": "body-0094", "role": "body", "section": "Linear state chance constraint", "weight": 1.0} -->

where $\Psi^{- 1}{({1 - \varepsilon_{x}})}$ denotes the inverse cumulative distribution function at probability $1 - \varepsilon_{x}$. This constraint can be handled in the PO-SDDP algorithm without approximation.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

In this section, the PO-SDDP algorithm is demonstrated through three scenarios: the light-dark domain problem, the Earth-to-Mars transfer problem, and the halo orbit transfer in the Earth--Moon CR3BP. All computations are performed on a desktop computer (Intel Core i9-14900KF, 3.2 GHz).

<!-- chunk {"id": "body-0096", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

In all scenarios, the stage and terminal cost functions are defined by Eq. (61a) and Eq. (61b), respectively. The initial augmented controls are set to zero, i.e., ${\mathbf{U}}_{k} = \mathbf{0}_{n_{U}}$ for all $k$, and the initial Lagrange multipliers for all constraints are also initialized with zero vectors. The Vern7 integrator from DifferentialEquations.jl \[rackauckas2017differentialequations\] is used to discretize the continuous dynamics, except for the light-dark domain problem, where the dynamics are linear.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

To validate the optimization results, Monte Carlo analysis is conducted using 500 random initial states sampled from $\mathcal{N}{({\mathbf{x}}_{0},{{\overset{\sim}{P}}_{0} + {\hat{P}}_{0}})}$, with dynamical disturbances and random observations. For each sampled trajectory, the state is estimated using the standard EKF and controlled by the optimal policy given in Eq.. In the Monte Carlo analysis, the process-noise covariance is computed by numerically integrating the Lyapunov equation in Eq. to assess the accuracy of the trapezoidal approximation used in the optimization.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Light-dark domain problem", "weight": 1.0} -->

Here, we consider the light-dark domain problem in which observation uncertainty varies with distance from a landmark.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Light-dark domain problem", "weight": 1.0} -->

where $\sigma_{p}$ and $\sigma_{v}$ are positive scalars representing the disturbance intensities of the position and velocity, respectively.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Light-dark domain problem", "weight": 1.0} -->

where $\sigma_{y,0}$ is a fixed observation-noise term and $\sigma_{y,1}$ is a coefficient for the noise proportional to the distance from the landmark position ${\lbrack l_{x}\quad l_{y}\rbrack}^{\top}$.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Light-dark domain problem", "weight": 1.0} -->

The key parameters in this scenario are summarized in Table 2. For the cost function, the weighting matrices are set to $Q_{k} = O_{n_{x}}$ and $R_{k} = I_{n_{u}}$, the scaling matrix in the trust-region subproblem is chosen as the identity matrix, i.e., $D_{tr} = I_{n_{U}}$, and the mass-leak parameter is set to $\epsilon_{u} = 10^{- 8}$. The stochastic thrust magnitude, terminal covariance, and linear state constraints are imposed, together with the terminal nominal-state constraint ${\overline{\mathbf{x}}}_{N} = {\mathbf{x}}_{f}$ where ${\mathbf{x}}_{f}$ denotes the target nominal state.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Light-dark domain problem", "weight": 1.0} -->

The initial estimation-error and state-estimate covariances are both specified by the standard deviations ${\overset{\sim}{\sigma}}_{r_{0}} = {\hat{\sigma}}_{r_{0}} = {4 \times 10^{- 2}}$ and ${\overset{\sim}{\sigma}}_{v_{0}} = {\hat{\sigma}}_{v_{0}} = 10^{- 2}$, while the terminal target covariance is specified by $\sigma_{r_{f}} = {2 \times 10^{- 4}}$ and $\sigma_{v_{f}} = 10^{- 2}$. For the augmented Lagrangian method, the initial penalties are set to $1.0$ for all constraints, the penalty scaling factor is set to $2.0$, and the Schatten-norm parameters are chosen as $p = 1$ for the thrust magnitude constraint and $p = 8$ for the surrogate terminal covariance constraint.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Light-dark domain problem", "weight": 1.0} -->

The nominal and sampled trajectories are shown in Fig. 3, where the nominal trajectory is plotted as a colored line, and the sampled trajectories are shown in gray. The nominal and sampled control profiles are also presented in Fig. 3. The region defined by $y > 3$ in the left panel of Fig. 3 is designated as a keep-out zone. Under the obtained control policy, the nominal trajectory approaches the landmark while proceeding toward the target state to obtain lower-noise position measurements. The trajectory then changes direction slightly below $y = 3$, leaving a margin to account for process noise and estimation error. The Monte Carlo sample trajectories also avoid entering the keep-out zone. For the thrust magnitude constraint, the nominal control sequence remains below the specified maximum acceleration, with a larger margin near the final stage. This increased margin helps reduce the terminal covariance because the system moves away from the landmark near the end of the trajectory, which increases the observation noise.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Light-dark domain problem", "weight": 1.0} -->

To clarify how the algorithmic formulation affects the solution, we compare PO-SDDP with belief-space iterative linear quadratic Gaussian (iLQG) \[Van_Den_Berg2012-fn\] and the SCP-based approach. Belief-space iLQG corresponds to a variant of the proposed method in which the state-estimate covariance is excluded from the state variables and the second-order STMs for the augmented dynamics are omitted. The SCP-based approach is implemented according to Ref. \[Kumagai2025-bl\] using JuMP.jl \[Lubin2023\] for general optimization modeling and Clarabel.jl \[Clarabel_2024\] as a semidefinite programming solver. The constraints and cost functions are selected to be consistent with the respective formulations of the methods being compared. In belief-space iLQG, the thrust magnitude, terminal covariance, and linear state constraints are imposed only for the nominal state and the estimation-error covariance. The cost function is defined without the state-estimate covariance term, since it is not included in the state variables.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Light-dark domain problem", "weight": 1.0} -->

By contrast, the SCP-based approach can handle convex constraints expressed in terms of the spectral norm; therefore, Eqs. and are employed for the thrust magnitude and terminal covariance constraints, respectively. The cost function for the SCP-based approach follows the formulation in Ref. \[Kumagai2025-bl\]. However, with the same target covariance used for PO-SDDP and belief-space iLQG, the adopted SCP-based formulation does not yield a feasible converged solution satisfying the terminal covariance constraint. Therefore, the target covariance for the SCP-based approach is relaxed to $2.5P_{f}$.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Light-dark domain problem", "weight": 1.0} -->

Figures 4 and 5 show the nominal and sampled trajectories obtained by belief-space iLQG and the SCP-based method, along with the corresponding control sequences. In the Monte Carlo analysis of belief-space iLQG, the feedback policy obtained in the backward pass is applied to the estimated state. The nominal trajectory generated by belief-space iLQG approaches the landmark in the same manner as that of the proposed method in order to reduce the estimation error. Because the state-estimate covariance and feedback gain are not included as optimization variables, the sampled trajectories and control sequences violate the keep-out zone and thrust magnitude constraints. As shown in Fig. 5, the SCP-based method yields a minimum-fuel solution with a robust feedback gain that guides the system directly to the target state while controlling the covariance to satisfy the terminal constraints.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Light-dark domain problem", "weight": 1.0} -->

Table 3 compares the fuel consumption, terminal covariance metric, and computational cost. The proposed method yields a navigation-aware trajectory while maintaining consistency between the predicted and Monte Carlo terminal covariance metrics. In contrast, belief-space iLQG underestimates the terminal uncertainty because the state-estimate covariance and optimized feedback gain are not included in its prediction. The SCP-based method obtains the lowest nominal fuel consumption under a relaxed covariance target, but it does not steer the trajectory toward the landmark because the EKF-related matrices are fixed during convexification. The lower runtime of belief-space iLQG mainly reflects its reduced state dimension.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Earth-to-Mars transfer", "weight": 1.0} -->

Next, the PO-SDDP algorithm is applied to the design of a low-thrust Earth-to-Mars transfer with radiometric tracking. The state consists of the spacecraft position ${\mathbf{r}} \in {\mathbb{R}}^{2}$ and velocity ${\mathbf{v}} \in {\mathbb{R}}^{2}$ in the heliocentric inertial frame, i.e., ${\mathbf{x}} = {\lbrack{\mathbf{r}}^{\top}\quad{\mathbf{v}}^{\top}\rbrack}^{\top}$. The deterministic part of the continuous-time dynamics is given by

<!-- chunk {"id": "body-0109", "role": "body", "section": "Earth-to-Mars transfer", "weight": 1.0} -->

where $\mu_{s}$ is the gravitational parameter of the Sun.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Earth-to-Mars transfer", "weight": 1.0} -->

The process noise is modeled using a two-dimensional reformulation of the Gates error model \[Gates1963-dv\]. In the original Gates model, the shutoff and resolution errors contribute to the uncertainty along the commanded thrust direction, whereas the pointing and autopilot errors contribute to the uncertainty orthogonal to that direction. The corresponding noise weighting matrix $G_{x}{({\mathbf{x}},{\mathbf{u}})}$ is defined as

<!-- chunk {"id": "body-0111", "role": "body", "section": "Earth-to-Mars transfer", "weight": 1.0} -->

The square-root factor of the covariance is written as

<!-- chunk {"id": "body-0112", "role": "body", "section": "Earth-to-Mars transfer", "weight": 1.0} -->

where the standard deviations orthogonal and parallel to the commanded thrust direction are defined by

<!-- chunk {"id": "body-0113", "role": "body", "section": "Earth-to-Mars transfer", "weight": 1.0} -->

Here, $\sigma_{ap}$, $\sigma_{pt}$, $\sigma_{res}$, and $\sigma_{sh}$ denote the autopilot, pointing, resolution, and shutoff errors, respectively. The commanded thrust direction is regularized as

<!-- chunk {"id": "body-0114", "role": "body", "section": "Earth-to-Mars transfer", "weight": 1.0} -->

For ${\parallel{\mathbf{u}}\parallel}^{2} \gg \epsilon_{u}$, this representation yields standard deviations approximately equal to $\sigma_{\parallel}$ along the commanded thrust direction and $\sigma_{\perp}$ in the orthogonal direction. The regularized direction vector preserves the directional structure of the original Gates model while keeping the noise model differentiable near zero thrust.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Earth-to-Mars transfer", "weight": 1.0} -->

Range and range-rate observations between the spacecraft and Earth are modeled as

<!-- chunk {"id": "body-0116", "role": "body", "section": "Earth-to-Mars transfer", "weight": 1.0} -->

The initial and target states are listed in Table 4, and the key parameters for this scenario are summarized in Table 5. The transfer duration and the initial and target states are based on those used in the numerical examples of Refs. \[Ozaki2020-id, ridderhof2020chance\], except that the initial state is slightly modified to avoid a singularity in the observation model. In this scenario, the PO-SDDP algorithm is applied with three different shutoff-error values to compare the resulting solutions. To demonstrate that the proposed method can accommodate multiple observations, range and range-rate measurements are assumed to be available at three equally spaced epochs in each stage, including the subsequent maneuver epoch. Thus, the $N = 40$ maneuver sequence contains 120 intermediate belief-state transitions.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Earth-to-Mars transfer", "weight": 1.0} -->

For the cost function, the weighting matrices are set to $Q_{k} = O_{n_{x}}$ and $R_{k} = I_{n_{u}}$, and the mass-leak parameter is set to $\epsilon_{u} = {10^{- 8}{({{mm}/s^{2}})}^{2}}$. The thrust magnitude constraint is imposed together with terminal constraints on the nominal state and terminal covariance.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Earth-to-Mars transfer", "weight": 1.0} -->

For the augmented Lagrangian method, the initial penalties are set to 1.0 for the thrust magnitude and terminal-state constraints and to $1 \times 10^{- 6}$ for the surrogate terminal covariance constraint, while the penalty scaling factor is set to 2.0 for all constraints. The Schatten-norm parameters are chosen as $p = 1$ for the thrust magnitude constraint and $p = 8$ for the surrogate terminal covariance constraint. In the trust-region subproblem, the scaling matrix is set to $D_{tr} = {{blkdiag}{(I_{n_{u}},{0.1I_{n_{u}n_{x}}})}}$, so that the terms corresponding to the feedback gain are one order of magnitude smaller than those corresponding to the nominal control. Using the identity scaling matrix fails to yield a solution that satisfies the surrogate terminal covariance constraints because the updates to the nominal control and feedback gain are treated as having comparable scales.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Earth-to-Mars transfer", "weight": 1.0} -->

The physical parameters are nondimensionalized using the length and time-scale factors listed in Table 5 to improve numerical stability during the optimization.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Halo orbit transfer in Earth--Moon CR3BP", "weight": 1.0} -->

As a third demonstration, the PO-SDDP algorithm is applied to an $L_{2}$-halo-to-$L_{1}$-halo transfer in the Earth--Moon CR3BP with radiometric tracking. The state consists of the three-dimensional position ${\mathbf{r}} \in {\mathbb{R}}^{3}$ and velocity ${\mathbf{v}} \in {\mathbb{R}}^{3}$ in the rotating frame with the origin at the barycenter of the system, i.e., ${\mathbf{x}} = {\lbrack{\mathbf{r}}^{\top}\quad{\mathbf{v}}^{\top}\rbrack}^{\top}$. The continuous-time dynamics are given by

<!-- chunk {"id": "body-0121", "role": "body", "section": "Halo orbit transfer in Earth--Moon CR3BP", "weight": 1.0} -->

The initial and target states are taken from Ref. \[Aziz2019-bw\], as listed in Table 7, and the key parameters are summarized in Table 8. In this scenario, two state-weighting matrices, $Q_{k} = {10I_{n_{x}}}$ and $Q_{k} = {500I_{n_{x}}}$ for all $k$, are considered in the cost function to compare the resulting solutions, while the control-weighting matrix is fixed at $R_{k} = I_{n_{u}}$ and the mass-leak parameter is set to $\epsilon_{u} = {{7.4 \times 10^{- 8}}{({{mm}/s^{2}})}^{2}}$. For the trust-region method, the scaling matrix in the trust-region subproblem is chosen as the identity matrix, i.e., $D_{tr} = I_{n_{U}}$. Here, the thrust magnitude constraint and the terminal constraint on the nominal state are imposed.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Halo orbit transfer in Earth--Moon CR3BP", "weight": 1.0} -->

For the augmented Lagrangian method, the initial penalties for the thrust magnitude and terminal-state constraints are both set to $1.0$, and the penalty scaling factor is set to $2.0$ for both constraints. The Schatten-norm parameter is chosen as $p = 1$ for the thrust magnitude constraint. The initial estimation-error covariance and state-estimate covariance are both defined from the standard deviations ${\overset{\sim}{\sigma}}_{r} = {\hat{\sigma}}_{r} = {10{km}}$ and ${\overset{\sim}{\sigma}}_{v} = {\hat{\sigma}}_{v} = {{0.1m}/s}$.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Halo orbit transfer in Earth--Moon CR3BP", "weight": 1.0} -->

Figures 9 and 10 compare the nominal trajectories and control profiles. The thrust magnitude, azimuth (${atan2}{(u_{y},u_{x})}$), and elevation ($\arcsin{({u_{z}/{\parallel{\mathbf{u}}\parallel}})}$) histories in Fig. 10 show that the solution obtained with the large weighting matrix differs from the other solutions in the timing, magnitude, and three-dimensional directions of the thrust arcs. With the small weighting matrix, the PO-SDDP solution behaves as a robustified version of the deterministic DDP solution, producing a similar nominal trajectory with more conservative correction capability. With the large weighting matrix, the optimized trajectory follows a different manifold and requires shorter second and third thrusting arcs, indicating that the covariance-related terms can alter the nominal trajectory when they are weighted sufficiently.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Halo orbit transfer in Earth--Moon CR3BP", "weight": 1.0} -->

Figures 11 and 12 show the corresponding Monte Carlo trajectories and control histories. The large-weighting solution exhibits smaller deviations from the nominal trajectory and requires less corrective maneuvering after the main thrust arcs.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Halo orbit transfer in Earth--Moon CR3BP", "weight": 1.0} -->

To clarify the differences between the solutions, nonlinearity and information analyses are conducted along the nominal trajectories. The results are shown in Fig. 13, where the nonlinearity index is defined using the finite-time Lyapunov exponent (FTLE) as

<!-- chunk {"id": "body-0126", "role": "body", "section": "Halo orbit transfer in Earth--Moon CR3BP", "weight": 1.0} -->

where $C_{j}$ and $W_{j}$ denote the observation sensitivity matrix and the inverse observation-noise covariance matrix at each stage, respectively. The nonlinearity index reflects the local sensitivity of the dynamics, whereas the information index quantifies the cumulative information gain with respect to the initial state. As shown in Fig. 9 and Fig. 13, the large-weighting solution avoids the strongly nonlinear region near the Moon while maintaining comparable information gain. This behavior explains the reduced terminal dispersion reported in Table 9. The predicted and Monte Carlo terminal covariance traces are consistent in both PO-SDDP cases.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper presents a stochastic differential dynamic programming algorithm for partially observable trajectory optimization problems. In the algorithm, the control update is computed by explicitly considering the coupled evolution of the nominal trajectory, the state-estimation process, and the feedback policy, without relying on the separation principle. Constraints on thrust magnitude, terminal state, and covariance are handled using an augmented Lagrangian formulation. For computational efficiency, the method computes state transition matrices for covariance propagation semi-analytically and uses automatic differentiation to evaluate model-dependent derivatives.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The numerical results demonstrate three distinct capabilities of the proposed approach. In the light-dark domain problem, the method generates a navigation-aware solution that exploits an informative region while maintaining the path and thrust constraints and achieving terminal covariance performance close to the prescribed target. In the Earth-to-Mars transfer, it produces uncertainty-robust solutions under nonlinear dynamics, nonlinear observations, and maneuver execution errors. The periodic-orbit transfer in the Earth--Moon CR3BP shows that the method identifies solutions that exploit the coupling between trajectory design and orbit determination in a strongly nonlinear dynamical environment. The results indicate that the proposed framework provides a practical way to incorporate navigation performance and feedback robustness into mission design problems under partial observability.
