<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Linear System Identification under Multiplicative Noise from Multiple Trajectory Data

Topics include Linear systems, System identification, Trajectory data, Multiplicative noise, Multiple trajectories, Covariance matrix, Network system, Least squares, Optimal control, Convergence rate, Recursive, Algorithm.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Provides asymptotic results on convergence of identified system parameters (dynamics parameters and noise covariances) to true values using a trajectory-averaging least-squares estimation algorithm for linear systems with multiplicative noise. Later extended to non-asymptotic results in 2106.16078.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The study of multiplicative noise models has a long history in control theory but is re-emerging in the context of complex networked systems and systems with learning-based control. We consider linear system identification with multiplicative noise from multiple state-input trajectory data. We propose exploratory input signals along with a least-squares algorithm to simultaneously estimate nominal system parameters and multiplicative noise covariance matrices. Identifiability of the covariance structure and asymptotic consistency of the least-squares estimator are demonstrated by analyzing first and second moment dynamics of the system. The results are illustrated by numerical simulations.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The study of stochastic systems with noise which multiplies with the state and input i.e. multiplicative noise has a long history in control theory, but is re-emerging in the context of complex networked systems and systems with learning-based control. In contrast with the well-known additive noise setting, multiplicative noise has the ability to capture dependence of the noise on the state and/or control input. This situation occurs in modern control systems as diverse as robotics with distance-dependent sensor errors, networked systems with noisy communication channels, modern power networks with high penetration of intermittent renewables, turbulent fluid flow, and neuronal brain networks. Linear systems with multiplicative noise are particularly attractive as a stochastic modeling framework because they remain simple enough to admit closed-form expressions for stability and stabilization via generalized Lyapunov equations (e.g. ), optimal control via the solution of generalized Riccati equations and state estimation. Additionally, recent results show that the optimal control of this class of systems can be learned strictly from sample data without constructing a model via the reinforcement learning technique of policy gradient.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

As a complementary perspective, here we tackle the problem from a model-based perspective where the goal is to learn and construct a model from sample data, which can then be used e.g. for optimal control design.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The first issue that must be addressed is that a complete multiplicative noise system model requires accurate estimates not only of the nominal linear system matrices, but also the noise covariance structure. This stands in stark contrast to the additive noise case where the noise covariance structure has no bearing on the control design and can thus be ignored during system identification. For the identification of a nominal linear system, recursive algorithms have been developed in the control literature, such as the recursive least-squares algorithm. These can be utilized for linear systems with multiplicative noise provided that certain assumptions on the noise and on system stability hold. For the estimation of noise covariances, both recursive and batch estimation methods have been proposed over the last few decades (see for a review), but these focus nearly exclusively on additive noise. In order to estimate multiplicative noise covariances, the maximum-likelihood approach was introduced, and the Bayesian framework was utilized, for example assuming Gaussian or known distributions with unknown parameters. These methods, however, require prior assumptions on the noise distributions whose incorrectness may worsen the performance of the concerned algorithms for optimal control.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our paper concentrates on jointly estimating the nominal system parameters and the multiplicative noise covariances without imposing any prior assumptions on the distribution of the noises, other than being independent and identically distributed (i.i.d.) with finite first and second moments, which complicates the problem. Both state- and control-dependent noise in the system leads to coupling, which also makes the identification task more difficult.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The second issue we address is that of performing system identification based on multiple state-input trajectory data rather than a single trajectory. Multiple trajectory data arises in two broad situations: 1) episodic tasks where a single system is reset to an initial state after a finite run time, as encountered in iterative learning control and reinforcement learning problems and 2) collecting data from multiple identical systems in parallel, for example, physical experiments and snapshots of social interaction processes. For multiple trajectory data the duration of each trajectory sample may be small, but a large sample size can be obtained by virtue of repetition in the case of episodic tasks and parallel execution in the case of multiple identical systems. Thus, there is a growing interest in system identification based on multiple trajectory data, along with their applications in machine learning literature.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we consider linear system identification with multiplicative noise from multiple trajectory data. Our contributions are two-fold: We propose a least-squares estimation algorithm to jointly estimate the nominal system matrices and multiplicative noise covariances from sample averages of multiple finite-horizon trajectory rollouts (Algorithm 1). A two-stage algorithm based on first and second moment dynamics that separate the nominal parameters from the noise variances is utilized, where a stochastic input design, from Gaussian and Wishart distributions, is used for exciting the moment dynamics. The algorithm does not need prior knowledge for the multiplicative noise or stability conditions for the system, except that the noises are i.i.d. among different trajectories, with finite first and second moments so it may be applied to a wide range of scenarios.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Identifiability of the noise covariance matrices and asymptotic consistency of our proposed algorithm are demonstrated. First, it is shown that there exists an equivalent class of covariance structure that generates the same second moment dynamics. Then, it is verified that dynamics defined by the first and second moments of states can generate a well-defined closed-form expression of the parameters, provided sufficiently exciting input sequences and certain controllability conditions hold. Then by assuming the multiple trajectory data are i.i.d., the consistency of the estimator, i.e., convergence to the true value as the number of trajectory samples grows to infinity, is obtained by combining the former result and the law of large numbers.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of the paper is organized as follows: we formulate the problem in Section II, then in Section III the algorithm is introduced and theoretical results are given, numerical simulation results are presented in Section IV, and in Section V we conclude.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We consider linear systems with multiplicative noise where $x_{t} \in {\mathbb{R}}^{n}$ is the system state and $u_{t} \in {\mathbb{R}}^{m}$ is the control input to be designed. The dynamics are described by a nominal dynamics matrix $A \in {\mathbb{R}}^{n \times n}$ and nominal input matrix $B \in R^{n \times m}$ and incorporate multiplicative noise terms modeled by the i.i.d.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Note that if ${\overline{A}}_{t}$ has non-zero mean $\overline{A}$, then we can consider a system with nominal matrix $({A + \overline{A}},B)$, as well as noise terms ${\overline{A}}_{t} - \overline{A}$ and ${\overline{B}}_{t}$, which satisfies the above zero-mean assumption. This also holds for cases with ${\overline{B}}_{t}$ non-zero mean. The term multiplicative noise refers to the fact that noises ${\overline{A}}_{t}$ and ${\overline{B}}_{t}$ enter the system as multipliers of $x_{t}$ and $u_{t}$, rather than as additions. In the latter case, the noises are called additive ones, resulting in much simpler system dynamics.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Problem. Suppose that the system parameters ${A,B,\Sigma_{A}},$ and $\Sigma_{B}$ are unknown, but state-input trajectories are available for system identification.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Algorithm Design", "weight": 1.0} -->

In this section, we propose our exploratory input sequence design and least-squares algorithm to estimate the system parameters from multiple trajectory data. We assume that the sampled trajectory data are collected independently, and refer to each trajectory sample as a *rollout*. Because every rollout is affected by the multiplicative noise, we will use least-squares on the first and second moment dynamics averaged over multiple trajectories to solve the system identification problem. Also, we assume inputs of arbitrary magnitude may be executed perfectly.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Algorithm Design", "weight": 1.0} -->

We apply the following process to (III-A), to obtain a simplified version of it.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Algorithm Design", "weight": 1.0} -->

Now with the following fact, we can restate the above relation between $(\Sigma_{A}',\Sigma_{B}')$ and $({\overset{\sim}{\Sigma}}_{A}',{\overset{\sim}{\Sigma}}_{B}')$ from an entry-wise perspective in Theorem 1.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Example 1", "weight": 1.0} -->

Under this situation, According to the above simplification, from where $\sigma_{a,{ij},{kl}} = {{\mathbb{E}}{\{{{\overline{A}}_{t,{ij}}{\overline{A}}_{t,{kl}}}\}}}$, $\sigma_{b,{ij}} = {{\mathbb{E}}{\{{\overline{B}}_{t,i},{\overline{B}}_{t,j}\}}}$, and The first and second moment dynamics and (III-A) are linear in the dynamic model parameters to be estimated. It is natural to consider a two-stage least-squares procedure, where first the nominal system matrices ($A$,$B$) are estimated, and then these estimates are plugged in to obtain estimates for the variances ($\Sigma_{A}$, $\Sigma_{B}$) from (III-A).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Example 1", "weight": 1.0} -->

If we had access to the exact first and second moment dynamics, this procedure would produce exact estimates. However, we must estimate the first and second moment dynamics from rollout data, and we propose to take a sample average over multiple independent rollouts. To obtain persistently exciting inputs, we randomly generate the first and second moment of the input sequence from standard Gaussian and Wishart^11^1The Wishart distribution $W_{p}{(V,n)}$ is the probability distribution of the matrix $X = {GG^{\intercal}}$ where each column of the matrix $G$ is drawn from the $p$-variate Gaussian distribution $\mathcal{N}_{p}{(0,V)}$. Clearly Wishart distributions are supported on the set of positive semidefinite matrices. distributions, respectively. Likewise, the initial states are assumed to be randomly drawn from a distribution $\mathcal{X}$ with finite second moment (see Sec. III-B2). The overall algorithm is shown in Algorithm 1, where the superscript $(k)$ represents the $k$-th rollout.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Example 1", "weight": 1.0} -->

In Alg. 1 and in the sequel, to ease notation, we omit the "$\overset{\sim}{}$" above $X_{t}$, $U_{t}$, $\Sigma_{A}'$, and $\Sigma_{B}'$, but readers should keep in mind that they are the simplified version of their counterparts in (III-A).

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Theoretical Consistency Analysis", "weight": 1.0} -->

In this section we analyze the consistency of Algorithm 1 by investigating the moment dynamics and (III-A), which motivated the least-squares approach in Algorithm 1.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B1 Moment Dynamics", "weight": 1.0} -->

Then closed-form solutions of the least-squares problems are where $\mathbf{C}$, $\mathbf{D}$, $\mathbf{Y}$, and $\mathbf{Z}$ are defined in (LABEL:defLSMatrices) above, and the sign $\dagger$ represents the pseudoinverse. When the inverse matrices exist, the solutions are identical to true values, that is, ${(\hat{A},\hat{B})} = {(A,B)}$ and ${({\hat{\Sigma}}_{A}',{\hat{\Sigma}}_{B}')} = {(\Sigma_{A}',\Sigma_{B}')}$. Hence, the first question towards the consistency of the algorithm is whether the matrices ${\mathbf{Z}\mathbf{Z}}^{\intercal}$ and ${\mathbf{D}\mathbf{D}}^{\intercal}$ are invertible, which is necessary for the consistency of the algorithm.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B1 Moment Dynamics", "weight": 1.0} -->

As to be shown, this invertibility can be obtained by designing a proper input sequence, if systems $(A,B)$ and $({\overset{\sim}{A} + \Sigma_{A}'},{\overset{\sim}{B} + \Sigma_{B}'})$ are controllable, and the final time-step $\ell$ is large enough. In fact, in this paper we randomly generalized the first and second moments of inputs to ensure the invertibility. As a consequence, we need to demonstrate the following results in a probability sense, intuitively saying that random generation of input statistics results in the expected invertibility.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The above theorem shows that for large enough time step of each rollout, the full row rank condition of $\mathbf{Z}$ can be guaranteed with probability one if the mean of the input at each time step is generated randomly and independently. In the proof, the controllability of $(A,B)$ plays a key role. In addition, although the lower bound in the theorem is relatively small, one may conjecture that $\ell \geq {n + m}$ is a sharp lower bound for the invertibility of ${\mathbf{Z}\mathbf{Z}}^{\intercal}$, which will be a future work.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 3", "weight": 1.0} -->

The controllability condition in Theorem 3 reflects the nature of the multiplicative noise, i.e., coupling between ${\overline{A}}_{t}$ and $x_{t}$, and that between ${\overline{B}}_{t}$ and $u_{t}$. It also indicates that a controllability condition on (III-A), the dynamics of the second moments of states, is necessary to ensure the successful identification of $\Sigma_{A}'$ and $\Sigma_{B}'$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 4", "weight": 1.0} -->

From the proof of Theorems 2 and 3, we know that the existence of the inverses of ${\mathbf{Z}\mathbf{Z}}^{\intercal}$ and ${\mathbf{D}\mathbf{D}}^{\intercal}$ can in fact be guaranteed with probability one, as long as $\nu_{t}$ and ${\overline{U}}_{t}$, the mean and vectorized second moment matrix of the input at time $t$, are generated independently from a distribution that is absolutely continuous with respect to Lebesgue measure. Also note the random generation of the first and second moments of inputs leads to non-stationarity of the input sequence. Critically this provides sufficient excitation of both the first and second moments of the state and makes it possible to estimate all model parameters in the presence of multiplicative noise.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Under Assumption 1 the rollouts $x_{0}^{(k)},\ldots,x_{l}^{(k)}$, $1 \leq k \leq n_{r}$, are i.i.d., so consistency can be established from Kolmogorov's strong law of large numbers.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 5", "weight": 1.0} -->

This theorem indicates that despite the relatively small final time-step for each trajectory, an increasing number of rollouts compensates for this deficiency and guarantees asymptotic estimation performance.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Numerical Simulations", "weight": 1.0} -->

To empirically validate our theoretical consistency result, we simulated our least-squares estimator on two example systems. The first is a simple 2-state, 1-input system where we use a large amount of data to show asymptotic trends, while the second is an 8-state, 8-input system representing lossy diffusion dynamics on a network for a more practical application. Python code which implements the algorithms and performs the simulated experiments described here is available on GitHub at

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A Simple example", "weight": 1.0} -->

We consider a simple example system with $n = 2$, $m = 1$, ${{A = \begin{bmatrix} \end{bmatrix}},{B = \begin{bmatrix} \end{bmatrix}}},$ and noise covariances Figure 1: Consistency of Alg. 1.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Simple example", "weight": 1.0} -->

Model estimates were computed at 100 increasing logarithmically spaced numbers of rollouts between $1$ and $n_{r}$. The result is plotted in Fig. 1, indicating the consistency of the proposed algorithm.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B Network example", "weight": 1.0} -->

Many practical networked systems can be approximated by diffusion dynamics with loss; examples include heat flow through uninsulated pipes, hydraulic flow through leaky pipes, information flow between processors with packet loss, electrical power flow between generators with resistant electrical power lines, etc. These dynamics in continuous-time act on an undirected graph with no self-loops with symmetric weighted adjacency matrix $A_{c}$, degree matrix $D_{c} = {\text{diag}{({A_{c}\text{1}_{n \times 1}})}}$, graph Laplacian $L = {D_{c} - A_{c}}$, diagonal loss matrix $F_{c}$, and diagonal input matrix $B_{c}$: Discretizing these dynamics using the forward Euler method with a step size $T$ yields $x_{t + 1} = {{Ax_{t}} + {Bu_{t}}}$ where $A = {I - {T{({L_{c} + F_{c}})}}}$ and $B =

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-B Network example", "weight": 1.0} -->

Uncertainty on an edge weight of the graph i.e. on entry $(j,k)$ of $A_{c}$ manifests as a noise matrix with entries Uncertainty on an input strength i.e. entry $(k,k)$ of $B_{u}$ manifests as a noise matrix with entries For computational tractability we estimated only the noise variances while giving the estimator knowledge of the noise directions $A_{i}$ and $B_{j}$. To formulate this setting mathematically it is easier to work with the eigendecomposition of the noises as.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B Network example", "weight": 1.0} -->

We chose a network with $n = 8$ nodes and edges placed via the Erdős-Rényi random graph generation with random integer weights. The graph was selected to be connected so that the system would be controllable. We used rollout data of length $\ell = {{\frac{1}{2}m^{2}n^{4}} + {\frac{1}{2}m^{2}n^{2}} + m^{2} + 1} = 133185$ and collected 7 rollouts; more rollouts could be used, but empirically this amount of data was sufficient to give good estimates.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this paper we proposed a system identification scheme for linear systems with multiplicative noise based on multiple trajectory data. By designing appropriate persistently exciting input signals, a least-squares algorithm was proposed for the joint estimation of nominal system and multiplicative noise covariances. The asymptotic consistency of the algorithm was proved, and illustrated by numerical simulations. Ongoing and future research directions include studying the convergence rate and non-asymptotic behavior of the proposed algorithm, problems of optimal input design, identification from single-trajectory data, and sparsity-promoting regularization for identification of networked systems with prior knowledge of sparsity levels.
