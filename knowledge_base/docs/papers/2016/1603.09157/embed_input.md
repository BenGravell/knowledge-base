<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Linear System Identification via EM with Latent Disturbances and Lagrangian Relaxation

Topics include Convex optimization, Semidefinite programming, Nonconvex optimization, System identification, Optimization, Lagrangian relaxation.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In the application of the Expectation Maximization algorithm to identification of dynamical systems, internal states are typically chosen as latent variables, for simplicity. In this work, we propose a different choice of latent variables, namely, system disturbances. Such a formulation elegantly handles the problematic case of singular state space models, and is shown, under certain circumstances, to improve the fidelity of bounds on the likelihood, leading to convergence in fewer iterations. To access these benefits we develop a Lagrangian relaxation of the nonconvex optimization problems that arise in the latent disturbances formulation, and proceed via semidefinite programming.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Linear time invariant (LTI) state-space models provide a useful approximation of dynamical system behavior in a multitude of applications. In situations where models cannot be derived from first principles, some form of data-driven modeling, i.e. system identification, is appropriate. This paper is concerned with identification of discrete-time LTI models of the form where $x_{t} \in {\mathbb{R}}^{n_{x}}$ denotes the system state, and $u_{t} \in {\mathbb{R}}^{n_{u}}$, $y_{t} \in {\mathbb{R}}^{n_{y}}$ denote the observed input and output, respectively. The disturbances (a.k.a. process noise), $w_{t} \in^{n_{w}}$ and measurement noise, $v_{t}$, are modeled as zero mean Gaussian white noise processes, while the uncertainty in the initial condition $x_{1}$ is modeled by a normal distribution, i.e.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

For convenience, all unknown model parameters are denoted by the variable $\theta = {\{\mu,\Sigma_{1},\Sigma_{w},\Sigma_{v},}$\Despite the simplicity of LTI models, identification of such systems is complicated by the presence of *latent* variables. Specifically, in applications the observed data typically consists of inputs and (noisy) outputs, but not internal states or exogenous disturbances.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Various strategies have been developed to deal with this 'missing data'. *Marginalization*, for instance, involves integrating out (i.e. marginalizing over) the latent variables, leaving $\theta$ as the only quantity to be estimated. This is the approach adopted by prediction error methods and the Metropolis-Hastings algorithm.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Alternatively, one may treat the latent variables as additional quantities to be estimated together with the model parameters. Such a strategy is termed *data augmentation*, and examples include subspace methods, the Gibbs sampler, and the Expectation Maximization (EM) algorithm.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, a new family of methods have been developed in which one *supremizes over* the latent variables to obtain convex upper bounds for quality-of-fit cost functions, such as simulation error (a.k.a. output error). An important technique employed in this approach is Lagrangian relaxation, which replaces difficult constrained optimization problems with tractable, unconstrained, convex approximations.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

This work draws on the underlying similarities between EM and Lagrangian relaxation to develop a new algorithm that seeks the maximum likelihood estimate of the model parameters $\theta$, given measurements $u_{1:T}$ and $y_{1:T}$, i.e.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The EM algorithm is an iterative approach to ML estimation, in which estimates of the latent variables are used to construct tractable lower bounds to the likelihood. In the application of EM to the latent variables are typically taken to be the system *states*, $x_{1:T}$, as this simplifies the ensuing optimization problem(s). Specifically, optimization of the bound at each iteration reduces to linear least squares.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we formulate the EM algorithm, for the approximate solution of, over latent *disturbances*, $w_{1:T}$. In contrast to the latent states formulation, the optimization of bounds based on disturbances is nonconvex. By applying Lagrangian relaxation, we obtain new bounds that can be optimized by semidefinite programming (SDP). The resulting algorithm can be considered an example of the more general *minorization maximization* principle.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rewards for this additional complexity are threefold. First, the proposed method elegantly handles identification of *singular* state-space models (i.e. $n_{w} < n_{x}$), a case to which the standard formulation of EM over latent states is not applicable, without modification. Secondly, this approach naturally ensures stability of the model at each iteration. Finally, when the *magnitude* of the disturbances (i.e. $\Sigma_{w}$) is small, we show that use of latent disturbances produces better approximations to the likelihood, leading to convergence in fewer iterations.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We first introduced the basic idea of combining Lagrangian relaxation with a formulation of EM over latent disturbances in our conference paper. This paper extends this recent work in several significant ways. In Section 4 we apply Lagrangian relaxation without resorting to Monte Carlo approximations, unlike the approach outlined. Furthermore, the Lagrangian relaxation detailed in this paper makes use of a more sophisticated multiplier, introduced in Section 4.4. A new study of the behavior of the EM algorithm for large and small disturbances is presented in Sections 5.2 and 6.1, offering insights into the results of numerical experiments on convergence rates in Section 6.2.

<!-- chunk {"id": "body-0013", "role": "body", "section": "The minorization-maximization principle", "weight": 1.0} -->

The minorization-maximization (MM) principle is an iterative approach to optimization problems of the form ${\max_{\theta}f}{(\theta)}$. Given an objective function $f{(\theta)}$ (not necessarily a likelihood), at each iteration of an MM algorithm we first build a *tight* lower bound $b{(\theta,\theta_{k})}$ satisfying i.e. we *minorize* $f$ by $b$. Then we optimize $b{(\theta,\theta_{k})}$ w.r.t. $\theta$ to obtain $\theta_{k + 1}$ such that ${f{(\theta_{k + 1})}} \geq {f{(\theta_{k})}}$. The principle is useful when direct optimization of $f$ is challenging, but optimization of $b$ is tractable (e.g. concave). In the following two subsections, we present EM and Lagrangian relaxation as special cases of the MM principle, for problems involving missing data.

<!-- chunk {"id": "body-0014", "role": "body", "section": "The minorization-maximization principle", "weight": 1.0} -->

Each of these algorithms is predicated on the assumption that there exists latent variables, $z$, such that optimization of $f{(\theta)}$ would be more straightforward if $z$ were known.

<!-- chunk {"id": "body-0015", "role": "body", "section": "The Expectation Maximization algorithm", "weight": 1.0} -->

The EM algorithm applies the MM principle to ML estimation, i.e. ${f{(\theta)}} = {L_{\theta}{(y_{1:T})}}$. Each iteration of the algorithm consists of two steps: the expectation (E) step computes the *auxiliary* function which is then maximized in lieu of the likelihood function during the maximization (M) step. The auxiliary function can be shown to satisfy the following inequality and so the new parameter estimate $\theta_{k + 1}$ obtained by maximization of $Q{(\theta,\theta_{k})}$ is guaranteed to be of equal or greater likelihood than $\theta_{k}$. In this sense, EM may be thought of as a specific MM recipe for building lower bounds $Q{(\theta,\theta_{k})}$ to the objective $L_{\theta}{(y_{1:T})}$, in ML estimation problems involving latent variables.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Strictly speaking $Q{(\theta,\theta_{k})}$ does not minorize $L_{\theta}{(y_{1:T})}$. Rather, the *change* in $Q{(\theta,\theta_{k})}$ lower bounds the *change* in $L_{\theta}{(y_{1:T})}$; c.f.. Nevertheless, with some abuse of terminology, we will refer to $Q{(\theta,\theta_{k})}$ as a lower bound, as shorthand for the relationship.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Lagrangian relaxation", "weight": 1.0} -->

The technique of Lagrangian relaxation applies the MM principle to *constrained* optimization problems of the form i.e. ${f{(\theta)}} = {J{(\theta,z^{\ast})}}$ where $z^{\ast}$ is such that ${F{(\theta,z^{\ast})}} = 0$. Here $J{(\theta,z)}$ is a cost function assumed to be convex in $\theta$, and $F{(\theta,z)}$, assumed affine in $\theta$, encodes the constraints. Notice that we present the problem as cost minimization, rather than objective maximization, and consequently develop upper bounds; however, this difference in superficial.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Lagrangian relaxation", "weight": 1.0} -->

Unlike EM, in which we estimate $z$, Lagrangian relaxation *supremizes* over the latent variables to generate the bound. Specifically, the relaxation of takes the form where $\lambda$ may be interpreted as a Lagrange multiplier. For arbitrary $\lambda$, the function ${\overline{J}}_{\lambda}{(\theta)}$ has two key properties: It is convex in $\theta$. Recall that $J$ and $F$ are convex and affine in $\theta$, respectively. As such, ${\overline{J}}_{\lambda}{(\theta)}$ is the supremum of an infinite family of convex functions, and is, therefore, itself convex in $\theta$; see Section 3.2.3 of.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Lagrangian relaxation", "weight": 1.0} -->

It is an upper bound for the original problem. Given $\theta$, let $z^{\ast}$ be such that ${F{(\theta,z^{\ast})}} = 0$. Then which implies that the supremum over all $z$ can be no smaller; i.e. ${\overline{J}}_{\lambda}{(\theta)}$ is an upper bound for $f{(\theta)}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Lagrangian relaxation", "weight": 1.0} -->

The original optimization problem may then be approximated by the convex program ${\min_{\theta}{\overline{J}}_{\lambda}}{(\theta)}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Latent variables for dynamical systems", "weight": 1.0} -->

In the application of EM to the identification of dynamical systems, there are two possible choices of latent variables: systems states, $x_{1:T}$, and initial conditions and disturbances $\{ x_{1},w_{1:T}\}$. Choosing latent states yields a joint likelihood function of the form whereas latent disturbances leads to where $x_{t + 1} = {{Ax_{t}} + {Bu_{t}} + {Gw_{t}}}$ for $t = {1,\ldots,T}$. We denote this *simulated* state sequence by which, for given $\theta$, is a *deterministic* mapping from initial conditions and disturbances to system states.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Latent variables for dynamical systems", "weight": 1.0} -->

One can begin to understand the relationship between the choice of latent variables and difficulty of the ensuing optimization problems by examining the joint log likelihood. For latent states, ${\log p_{\theta}}{(y_{1:T},x_{1:T})}$ decomposes as Given $\{ u_{1:T},x_{1:T},y_{1:T}\}$, optimization of this function (w.r.t. $\theta$) amounts to simple linear least squares.

<!-- chunk {"id": "body-0023", "role": "body", "section": "EM with latent disturbances", "weight": 1.0} -->

In this section we detail the application of EM to the identification of LGSS models, when formulated with latent disturbances; refer to for the formulation over latent states. Each iteration of the algorithm involves optimization of the *auxiliary function* | | $Q{(\theta,\theta_{k})}$ | $= {E_{\theta_{k}}\left\lbrack {{\log p_{\theta}}{(y_{1:T},x_{1},w_{1:T})}} \middle| y_{1:T} \right\rbrack}$ | | \(12\) | which serves as a lower bound to the likelihood, given our current best estimate of the model parameters, $\theta_{k}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "EM with latent disturbances", "weight": 1.0} -->

With the joint log likelihood ${\log p_{\theta}}{(y_{1:T},x_{1},w_{1:T})}$ given, to evaluate $Q{(\theta,\theta_{k})}$ we must compute $p_{\theta_{k}}{(x_{1},{w_{1:T} \mid y_{1:T}})}$, i.e., the joint smoothing distribution (JSD) of the initial state and disturbances. The E step then amounts to solving a *disturbance smoothing*, rather than *state smoothing*, problem, which reflects the use of disturbances, rather than states, as latent variables.

<!-- chunk {"id": "body-0025", "role": "body", "section": "EM with latent disturbances", "weight": 1.0} -->

As demonstrated in Section 2.5, $L_{\theta}{(y_{1:T},x_{1},w_{1:T})}$ involves the simulated state sequence $\mathcal{X}_{T}{(\theta,}$\$u_{1:T},x_{1},w_{1:T})$. As a consequence, we shall show that the M step is equivalent to a nonconvex simulation error minimization problem (c.f.). This is in contrast to the latent states formulation, in which ${\max_{\theta}Q}{(\theta,\theta_{k})}$ reduces to linear least squares.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Maximization step", "weight": 1.0} -->

To perform the M step, i.e. maximize $Q{(\theta,\theta_{k})}$, we will utilize the same decomposition as, and optimize each of the conditional expectations separately; the validity of this approach is established by Remark 2.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Lagrangian relaxation of maximization step", "weight": 1.0} -->

In this section we describe how Lagrangian relaxation (c.f. Section 2.4) can be applied to the optimization of $Q_{3}{(\gamma,\theta_{k})}$. Specifically, we shall develop a bound for $Q_{3}{(\gamma,\theta_{k})}$ that can be efficiently optimized as a convex program. Furthermore, we shall show how this approach naturally enforces model stability at each iteration, by searching over a convex parametrization of all stable linear models.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Lagrangian relaxation of simulation error", "weight": 1.0} -->

Optimization of $Q_{3}{(\gamma,\theta_{k})}$ in is difficult because it requires minimization of *simulation error*, as defined. In this subsection, we detail the application of Lagrangian relaxation, introduced in Section 2.4, to minimization of simulation error, which can be formulated as Here $\xi_{1}$ denotes the initial state, assumed to be known, and $\mathcal{F}{(\gamma,u_{1:T},\xi_{1},x_{1:T},w_{1:T})}$ encodes the dynamic constraints on $x_{1:T}$, such that As, the Lagrangian relaxation of takes the form and, for arbitrary multiplier $\lambda$, represents a convex upper bound on the simulation error $\mathcal{E}{(\gamma,u_{1:T},}$\

<!-- chunk {"id": "body-0029", "role": "body", "section": "Implicit dynamics", "weight": 1.0} -->

It remains to choose the Lagrange multiplier $\lambda$ such that ${\overline{J}}_{\lambda}{(\gamma)}$ is a useful upper bound, i.e., such that ${\overline{J}}_{\lambda}^{\ast} \approx J^{\ast}$. Unfortunately, the simultaneous search for $\lambda$ and $\gamma$ is not jointly convex, due to the coupling between $\lambda$ and $\mathcal{F}$, and so $\lambda$ must be specified in advance. However, we can alleviate this restriction by searching over an implicit representation of the dynamics in (1a) where $E$ is invertible such that $A = {E^{- 1}F}$, $B = {E^{- 1}K}$ and $G = {E^{- 1}L}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Implicit dynamics", "weight": 1.0} -->

With the implicit dynamics of, the dynamics constraint can be expressed where $\overline{F} \in {\mathbb{R}}^{{{Tn_{x}} \times T}n_{x}}$ and $\epsilon \in {\mathbb{R}}^{Tn_{x}}$ denote respectively. One may interpret the convex bound resulting from this implicit formulation as that of, but with the multiplier ${({I \otimes E'})}\lambda$, thereby allowing a simultaneous (partial) search for multipliers and model parameters.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 3", "weight": 1.0} -->

We introduce $\eta = {\{ E,F,K,L,C,D,\Sigma_{v},P\}}$ to group the implicit model parameters, $\Sigma_{v}$ and $P \in {\mathbb{S}}_{+ +}^{n_{x}}$, into a single variable. Here $P$ represents a model stability certificate, the role of which is made precise in Lemma 6. Henceforth, ${\overline{J}}_{\lambda}{(\eta)}$ denotes Lagrangian relaxation with the implicit dynamics constraint. For convenience, we define the mapping $\mathcal{M}:{\eta\mapsto\gamma}$ from an implicit to explicit parametrization: ${\mathcal{M}{(\eta)}} \triangleq {\{\Sigma_{v},{E\backslash F},{E\backslash K},{E\backslash L},C,D\}}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Convex upper bound for $- {Q_{3}{(\\gamma,\\theta_{k})}}$", "weight": 1.0} -->

The representation of $Q_{3}{(\gamma,\theta_{k})}$ in makes the application of Lagrangian relaxation straightforward. To obtain a convex upper bound for $- {Q_{3}{(\gamma,\theta_{k})}}$ we can simply replace each simulation error term $\mathcal{E}{(\gamma)}$ with the appropriate corresponding convex bound ${\overline{J}}_{\lambda}{(\eta)}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Lagrange multipliers", "weight": 1.0} -->

While convexity of the upper bound ${\overline{J}}_{\lambda}$ defined in is guaranteed for any multiplier $\lambda$ that is independent of $\eta$, in this work we consider multipliers of the form $\lambda = {\text{vec}\left({\{\lambda_{t}\}}_{t = 1}^{T} \right)}$ for $\lambda_{t} = {2\left({{Hx_{t}} + h_{t}} \right)}$, i.e. where $\Lambda = {I_{T} \otimes H}$ for $H \in {\mathbb{R}}^{n_{x} \times n_{x}}$ and $h \in {\mathbb{R}}^{Tn_{x}}$. Recall from Section 4.2 that the use of the implicit model class allows a convex (partial) search over model parameters and multipliers.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Lagrange multipliers", "weight": 1.0} -->

Furthermore, this implicit representation permits the following definition of a convex parametrization of all stable LTI models.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 4", "weight": 1.0} -->

The LMI ${M{(\eta,H)}} > 0$ implies ${{H'E} + {E'H}} > 0$ which ensures that $E$ is invertible, i.e., the implicit dynamics in are well-posed.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 5", "weight": 1.0} -->

A common heuristic for terminating the EM algorithm is to cease iterations once the change in likelihood falls below a certain tolerance $\delta$, i.e.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Alternatively, one can simply run the algorithm for a finite number of iterations, chosen so as to attain a model of quality sufficient for its intended application; this is the approach taken, e.g.,.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Set k = 0 and initialize θk such that Lθk (y1: T) is finite.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Assemble {λi}j = 0T of the form by computing {Hj}j = 0T with and {hj}j = 0T. Compute ηk + 1 by solving and set γk + 1 = ℳ (ηk + 1).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Terminate if, otherwise k ← k + 1 and return to step 2.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Singular state space models", "weight": 1.0} -->

In applications, it may arise that the dimension of the disturbance is less than that of the state variable, i.e. $n_{w} < n_{x}$. For example, consider a simple mass-spring-damper system governed by ${{m\overset{¨}{s}} + {c\overset{˙}{s}} + {ks}} = {u + w}$ for displacement $s$. When discretized, these dynamics can be represented by the second order state space model with state variable $x_{t} = \left\lbrack {s{(t)}\overset{˙}{s}{(t)}} \right\rbrack'$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Singular state space models", "weight": 1.0} -->

In such cases, the process noise covariance $G\Sigma_{v}G'$ is singular, and standard EM algorithms based on latent states are no longer applicable. To see why, observe that the transition density of such a model is given by As $G\Sigma_{w}G'$ is rank deficient, the transition $p_{\theta}{({x_{t + 1} \mid x_{t}})}$ does not admit a density, and so we cannot evaluate, much less optimize, the joint log likelihood ${\log p_{\theta}}{(y_{1:T},x_{1:T})}$ given. Modifications to the standard latent states EM algorithm have been proposed to circumvent this difficulty e.g. the work of introduces a perturbation model with full-rank process noise covariance. However, by choosing latent disturbances we can elegantly handle identification of both singular and full-rank state space models, with the same algorithm.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Singular state space models", "weight": 1.0} -->

In particular, when formulating the EM algorithm over latent disturbances we work with the joint likelihood function $p_{\theta}{(y_{1:T},x_{1},w_{1:T})}$, given. Comparing to, we observe that the problematic transition density is replaced by the joint distribution of disturbances This distribution is independent of $n_{x}$, and so $p_{\theta}{(y_{1:T},x_{1},w_{1:T})}$ and, therefore, $Q{(\theta,\theta_{k})}$ remains well-defined, even in the singular case, $n_{w} < n_{x}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Absence of disturbances or output noise", "weight": 1.0} -->

In this section, we study the auxiliary function $Q{(\theta,\theta_{k})}$ in the limit cases of $\Sigma_{w} = 0$ and $\Sigma_{v} = 0$, for different choices of latent variables. These results will offer insight into the behavior of the EM algorithm as a function of disturbance magnitude, as explored in the numerical experiments of Section 6.1. For convenience, we denote the bounds based on latent states and disturbances by $Q_{\text{ls}}{(\theta,\theta_{k})}$ and $Q_{\text{ld}}{(\theta,\theta_{k})}$, respectively.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Influence of disturbance magnitude on bound fidelity", "weight": 1.0} -->

In the following experiment, we investigate the fidelity of $Q{(\theta,\theta_{k})}$ as a bound on $L_{\theta}{(y_{1:T})}$, as a function of the magnitude of the disturbances, $w_{1:T}$, and the choice of latent variables. As in Section 5.2, we denote the bounds based on latent states and disturbances by $Q_{\text{ls}}{(\theta,\theta_{k})}$ and $Q_{\text{ld}}{(\theta,\theta_{k})}$, respectively. The results are presented in Figure 1, which depicts $Q_{\text{ls}}$, $Q_{\text{ld}}$ and $L_{\theta}{(y_{1:T})}$ for a first order ($n_{x} = 1$) LGSS model, each plotted as a function of the single unknown scalar parameter $\theta = A$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Influence of disturbance magnitude on bound fidelity", "weight": 1.0} -->

We begin with the case of 'small' disturbances (i.e. $\Sigma_{w} \ll \Sigma_{v}$) as depicted in Figure 1(a), and observe the following: $Q_{\text{ld}}{(\theta,\theta_{k})}$ represents $L_{\theta}{(y_{1:T})}$ with high fidelity, whereas $Q_{\text{ls}}{(\theta,\theta_{k})}$ is localized about $\theta_{k}$. Such an observation is not without precedent. For instance, in the latent states formulation of \[9, Section 10\] it was noted that an initial disturbance covariance estimate $\Sigma_{w} = 0$ results in $\theta_{k} = \theta_{0}$ for all $k$; i.e. the model parameters are not improved.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Influence of disturbance magnitude on bound fidelity", "weight": 1.0} -->

Proposition 9 makes this observation more precise: in the 1D case of Figure 1(a), when $\Sigma_{w} = 0$, $Q_{\text{ls}}{(\theta,\theta_{k})}$ is undefined for $A \neq A_{k}$. Taken together, Figure 1(a) and Proposition 9 suggest that as $\Sigma_{w}$ becomes smaller (relative to $\Sigma_{v}$) the bound $Q_{\text{ls}}{(\theta,\theta_{k})}$ becomes more localized about $\theta_{k}$, eventually collapsing to a single point when $\Sigma_{w} = 0$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Influence of disturbance magnitude on bound fidelity", "weight": 1.0} -->

Conversely, as $\Sigma_{w}$ (and $\Sigma_{1}$) decrease, $Q_{\text{ld}}{(\theta,\theta_{k})}$ becomes an increasingly accurate representation of the log likelihood, eventually reproducing $L_{\theta}{(y_{1:T})}$ *exactly*, when $\Sigma_{w}$ (and $\Sigma_{1}$) are identically zero, as in Proposition 10.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Influence of disturbance magnitude on bound fidelity", "weight": 1.0} -->

Turning our attention to the case of 'large' disturbances (i.e. $\Sigma_{w} \gg \Sigma_{v}$) as depicted in Figure 1(b), we observe the opposite behavior: $Q_{\text{ls}}{(\theta,\theta_{k})}$ faithfully represents the log likelihood, whereas $Q_{\text{ld}}{(\theta,\theta_{k})}$ appears to be localized about $\theta_{k}$. Once more, studying the limiting case $\Sigma_{v} = 0$ offers insight into this behavior: Proposition 11 states that when $\Sigma_{v} = 0$, $Q_{\text{ld}}{(\theta,\theta_{k})}$ is undefined for $A \neq A_{k}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Influence of disturbance magnitude on bound fidelity", "weight": 1.0} -->

Taken together, Figure 1(b) and Proposition 11 suggest that as $\Sigma_{v}$ decreases (i.e. as $\Sigma_{w}$ increases relative to $\Sigma_{v}$), the bound $Q_{\text{ld}}{(\theta,\theta_{k})}$ becomes more localized about $\theta_{k}$, eventually collapsing to a single point when $\Sigma_{v} = 0$. Conversely, for this 1D experiment with $\theta = A$, Proposition 12 states that $Q_{\text{ls}}{(\theta,\theta_{k})}$ will reproduce $L_{\theta}{(y_{1:T})}$ *exactly*, when $\Sigma_{v}$ is identically zero. Indeed, in Figure 1(b) with $\Sigma_{v} \ll \Sigma_{w}$, we observe $Q_{\text{ls}}{(\theta,\theta_{k})}$ representing the likelihood faithfully.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Influence of disturbance magnitude on bound fidelity", "weight": 1.0} -->

To summarize: in the case of 'large disturbances' (i.e. $\Sigma_{w} \gg \Sigma_{v}$), $Q_{\text{ld}}{(\theta,\theta_{k})}$ will tend to bound $L_{\theta}{(y_{1:T})}$ with greater fidelity, compared to $Q_{\text{ls}}{(\theta,\theta_{k})}$. In the case of 'small disturbances' (i.e. $\Sigma_{w} \ll \Sigma_{v}$) the converse is true.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Convergence rate", "weight": 1.0} -->

This principle, which is clearly understood in the first order example of Figure 1, is further illustrated in Figure 3 for three different $4^{\text{th}}$ order SISO systems; Bode plots for each system are given in Figure 2. The results in Figure 3 clearly show Algorithm 1, based on latent disturbances, converging in fewer iterations than the latent states formulation of. These results are consistent with the analysis in Section 6.1. Specifically, in each trial disturbances were 'small' in magnitude ($\Sigma_{w} = {1 \times 10^{- 5}}$) and so we expect ${\overline{Q}}_{3}{(\eta)}$ to better represent the likelihood, allowing Algorithm 1 to converge in fewer iterations.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Convergence rate", "weight": 1.0} -->

It should be stressed that although Algorithm 1 converges in fewer iterations than the latent states formulation, each iteration is considerably more computationally expensive, and thus the total computation times for each algorithm are comparable. Nevertheless, this faster convergence rate is advantageous as it renders Algorithm 1 less sensitive to the choice of $\delta$ when termination conditions of the form are employed. Furthermore, as methods for SDP mature, one may expect Algorithm 1 to gain the upper hand in regards to computation time.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Stability of the identified model", "weight": 1.0} -->

A desirable property of Algorithm 1 is that stability of the identified model is enforced at every iteration; recall from Lemma 6 that we confine our search to an implicit parametrization of all stable models, which, by Lemma 7, is necessary to ensure that ${\overline{J}}_{\lambda}{(\eta)}$ is well-defined. Conversely, in a standard latent states implementation of the EM algorithm, the M step is accomplished by the solution of an unconstrained linear least squares problem. Consequently, it is possible that at any iteration (or indeed the conclusion) of the algorithm, the parameters $\theta_{k}$ could constitute an unstable model.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Stability of the identified model", "weight": 1.0} -->

Such a scenario is illustrated in the numerical experiment of Figure 4, which depicts the identification of a $4^{\text{th}}$ order model, similar to System 2 in Figure 2. From Figure 4(b) it is apparent that, for the first one thousand iterations, the parameters maintained by the latent states EM algorithm represent an *unstable* model (i.e. ${|{\lambda_{\text{max}}{(A_{k})}}|} > 1$). This instability can be particularly problematic, given the slow convergence rate; e.g. in this instance, if a heuristic such as was used employed, for $\delta > {4.7 \times 10^{- 3}}$ the algorithm would terminate before the thousandth iteration, and an unstable model would be returned. Conversely, the parameters maintained by Algorithm 1 constitute a stable model at each iteration.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Stability of the identified model", "weight": 1.0} -->

(a) Difference between Lθk (y1: T) and Lθtrue (y1: T), where θtrue denotes the true model parameters, at each iteration.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Stability of the identified model", "weight": 1.0} -->

(b) Magnitude of the largest eigenvalue of Ak, at each iteration. When the spectral radius of Ak is greater than unity, i.e. |λmax (Ak)| > 1, the model θk is unstable.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we have formulated the EM algorithm over latent disturbances, rather than states, for the identification of linear dynamical systems. Our main contribution is the use of Lagrangian relaxation to obtain a convex approximation of the challenging maximization step, guaranteed not to decrease the likelihood at each iteration. Though more computationally complex, this formulation with latent disturbances allows EM to be applied to singular state-space models, where latent states based methods break down.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Extension of this approach to the identification of nonlinear models shall be the subject of future research. In the nonlinear case, two major challenges arise during the formulation of EM with latent disturbances. First, the E step (c.f. Section 3.1) now involves a nonlinear disturbance smoothing problem, for which no closed form solution is known to exist. In recent decades, *sequential Monte Carlo* (SMC) methods have emerged as effective tools for overcoming similar difficulties, having already proved useful in nonlinear, non-Gaussian *state smoothing* and *disturbance filtering* problems.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Second, nonlinearity of the model complicates the Lagrangian relaxation of the M step; e.g. the bound ${\hat{J}}_{\lambda}{(\eta)}$ cannot be evaluated analytically, as the supremum (in ) requires optimization of a function that is no longer quadratic in $x$. To proceed, one might approximate the simulation error terms in $Q_{3}{(\gamma,\theta_{k})}$ with the *linearized simulation error*, introduced, to which the Lagrangian relaxation presented in this work can be applied with little modification. Alternatively, when the system nonlinearity is modeled as a polynomial, *sum-of-squares* (SOS) programing may be used to generate, and optimize, convex approximations to the Lagrangian relaxation.
