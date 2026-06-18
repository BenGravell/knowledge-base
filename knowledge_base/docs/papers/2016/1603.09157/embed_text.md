## Introduction

Linear time invariant (LTI) state-space models provide a useful approximation of dynamical system behavior in a multitude of applications. In situations where models cannot be derived from first principles, some form of data-driven modeling, i.e. system identification, is appropriate. This paper is concerned with identification of discrete-time LTI models of the form

where $x_{t} \in {\mathbb{R}}^{n_{x}}$ denotes the system state, and $u_{t} \in {\mathbb{R}}^{n_{u}}$, $y_{t} \in {\mathbb{R}}^{n_{y}}$ denote the observed input and output, respectively. The disturbances (a.k.a. process noise), $w_{t} \in^{n_{w}}$ and measurement noise, $v_{t}$, are modeled as zero mean Gaussian white noise processes, while the uncertainty in the initial condition $x_{1}$ is modeled by a normal distribution, i.e.

For convenience, all unknown model parameters are denoted by the variable $\theta = {\{\mu,\Sigma_{1},\Sigma_{w},\Sigma_{v},}$\

Despite the simplicity of LTI models, identification of such systems is complicated by the presence of *latent* variables. Specifically, in applications the observed data typically consists of inputs and (noisy) outputs, but not internal states or exogenous disturbances.

Various strategies have been developed to deal with this 'missing data'. *Marginalization*, for instance, involves integrating out (i.e. marginalizing over) the latent variables, leaving $\theta$ as the only quantity to be estimated. This is the approach adopted by prediction error methods and the Metropolis-Hastings algorithm.

Alternatively, one may treat the latent variables as additional quantities to be estimated together with the model parameters. Such a strategy is termed *data augmentation*, and examples include subspace methods, the Gibbs sampler, and the Expectation Maximization (EM) algorithm.

Recently, a new family of methods have been developed in which one *supremizes over* the latent variables to obtain convex upper bounds for quality-of-fit cost functions, such as simulation error (a.k.a. output error). An important technique employed in this approach is Lagrangian relaxation, which replaces difficult constrained optimization problems with tractable, unconstrained, convex approximations.

This work draws on the underlying similarities between EM and Lagrangian relaxation to develop a new algorithm that seeks the maximum likelihood estimate of the model parameters $\theta$, given measurements $u_{1:T}$ and $y_{1:T}$, i.e.

The EM algorithm is an iterative approach to ML estimation, in which estimates of the latent variables are used to construct tractable lower bounds to the likelihood. In the application of EM to the latent variables are typically taken to be the system *states*, $x_{1:T}$, as this simplifies the ensuing optimization problem(s). Specifically, optimization of the bound at each iteration reduces to linear least squares.

In this work, we formulate the EM algorithm, for the approximate solution of, over latent *disturbances*, $w_{1:T}$. In contrast to the latent states formulation, the optimization of bounds based on disturbances is nonconvex. By applying Lagrangian relaxation, we obtain new bounds that can be optimized by semidefinite programming (SDP). The resulting algorithm can be considered an example of the more general *minorization maximization* principle.

The rewards for this additional complexity are threefold. First, the proposed method elegantly handles identification of *singular* state-space models (i.e. $n_{w} < n_{x}$), a case to which the standard formulation of EM over latent states is not applicable, without modification. Secondly, this approach naturally ensures stability of the model at each iteration. Finally, when the *magnitude* of the disturbances (i.e. $\Sigma_{w}$) is small, we show that use of latent disturbances produces better approximations to the likelihood, leading to convergence in fewer iterations.

We first introduced the basic idea of combining Lagrangian relaxation with a formulation of EM over latent disturbances in our conference paper. This paper extends this recent work in several significant ways. In Section 4 we apply Lagrangian relaxation without resorting to Monte Carlo approximations, unlike the approach outlined in. Furthermore, the Lagrangian relaxation detailed in this paper makes use of a more sophisticated multiplier, introduced in Section 4.4. A new study of the behavior of the EM algorithm for large and small disturbances is presented in Sections 5.2 and 6.1, offering insights into the results of numerical experiments on convergence rates in Section 6.2.

## Preliminaries

### Notation

The cone of real, symmetric nonnegative (positive) definite matrices is denoted by ${\mathbb{S}}_{+}^{n}$ (${\mathbb{S}}_{+ +}^{n}$). The $n \times n$ identity matrix is denoted $I_{n}$. Let $\text{vec}:{{\mathbb{R}}^{m \times n}\mapsto{\mathbb{R}}^{mn}}$ denote the function that stacks the columns of a matrix to produce a column vector. The Kronecker product is denoted $\otimes$. The transpose of a matrix $A$ is denoted $A^{\prime}$, and ${|A|}_{Q}^{2}$ is shorthand for $A^{\prime}QA$. Time series data ${\{ x_{t}\}}_{t = a}^{b}$ is denoted $x_{a:b}$ where ${a,b} \in {\mathbb{N}}$. A random variable $x$ distributed according to the multivariate normal distribution, with mean $\mu$ and covariance $\Sigma$, is denoted $x \sim {\mathcal{N}{(x;\mu,\Sigma)}}$. We use ${a{(\theta)}} \propto {b{(\theta)}}$ to mean ${b{(\theta)}} = {{c_{1}a{(\theta)}} + c_{2}}$ where $c_{1},c_{2}$ are constants that do not effect optimization of $a{(\theta)}$ w.r.t. $\theta$. For invertible $A$, $A\backslash B$ is shorthand for $A^{- 1}B$. The log likelihood function is denoted ${L_{\theta}{(y_{1:T})}} \triangleq {{\log p_{\theta}}{(u_{1:T},y_{1:T})}}$.

### The minorization-maximization principle

The minorization-maximization (MM) principle is an iterative approach to optimization problems of the form ${\max_{\theta}f}{(\theta)}$. Given an objective function $f{(\theta)}$ (not necessarily a likelihood), at each iteration of an MM algorithm we first build a *tight* lower bound $b{(\theta,\theta_{k})}$ satisfying

i.e. we *minorize* $f$ by $b$. Then we optimize $b{(\theta,\theta_{k})}$ w.r.t. $\theta$ to obtain $\theta_{k + 1}$ such that ${f{(\theta_{k + 1})}} \geq {f{(\theta_{k})}}$. The principle is useful when direct optimization of $f$ is challenging, but optimization of $b$ is tractable (e.g. concave). In the following two subsections, we present EM and Lagrangian relaxation as special cases of the MM principle, for problems involving missing data. Each of these algorithms is predicated on the assumption that there exists latent variables, $z$, such that optimization of $f{(\theta)}$ would be more straightforward if $z$ were known.

### The Expectation Maximization algorithm

The EM algorithm applies the MM principle to ML estimation, i.e. ${f{(\theta)}} = {L_{\theta}{(y_{1:T})}}$. Each iteration of the algorithm consists of two steps: the expectation (E) step computes the *auxiliary* function

which is then maximized in lieu of the likelihood function during the maximization (M) step. The auxiliary function can be shown to satisfy the following inequality

and so the new parameter estimate $\theta_{k + 1}$ obtained by maximization of $Q{(\theta,\theta_{k})}$ is guaranteed to be of equal or greater likelihood than $\theta_{k}$. In this sense, EM may be thought of as a specific MM recipe for building lower bounds $Q{(\theta,\theta_{k})}$ to the objective $L_{\theta}{(y_{1:T})}$, in ML estimation problems involving latent variables.

### Remark 1

Strictly speaking $Q{(\theta,\theta_{k})}$ does not minorize $L_{\theta}{(y_{1:T})}$. Rather, the *change* in $Q{(\theta,\theta_{k})}$ lower bounds the *change* in $L_{\theta}{(y_{1:T})}$; c.f.. Nevertheless, with some abuse of terminology, we will refer to $Q{(\theta,\theta_{k})}$ as a lower bound, as shorthand for the relationship in.

### Lagrangian relaxation

The technique of Lagrangian relaxation applies the MM principle to *constrained* optimization problems of the form

i.e. ${f{(\theta)}} = {J{(\theta,z^{\ast})}}$ where $z^{\ast}$ is such that ${F{(\theta,z^{\ast})}} = 0$. Here $J{(\theta,z)}$ is a cost function assumed to be convex in $\theta$, and $F{(\theta,z)}$, assumed affine in $\theta$, encodes the constraints. Notice that we present the problem as cost minimization, rather than objective maximization, and consequently develop upper bounds; however, this difference in superficial.

Unlike EM, in which we estimate $z$, Lagrangian relaxation *supremizes* over the latent variables to generate the bound. Specifically, the relaxation of takes the form

where $\lambda$ may be interpreted as a Lagrange multiplier. For arbitrary $\lambda$, the function ${\overline{J}}_{\lambda}{(\theta)}$ has two key properties:

It is convex in $\theta$. Recall that $J$ and $F$ are convex and affine in $\theta$, respectively. As such, ${\overline{J}}_{\lambda}{(\theta)}$ is the supremum of an infinite family of convex functions, and is, therefore, itself convex in $\theta$; see Section 3.2.3 of.

It is an upper bound for the original problem. Given $\theta$, let $z^{\ast}$ be such that ${F{(\theta,z^{\ast})}} = 0$. Then

which implies that the supremum over all $z$ can be no smaller; i.e. ${\overline{J}}_{\lambda}{(\theta)}$ is an upper bound for $f{(\theta)}$.

The original optimization problem may then be approximated by the convex program ${\min_{\theta}{\overline{J}}_{\lambda}}{(\theta)}$.

### Latent variables for dynamical systems

In the application of EM to the identification of dynamical systems, there are two possible choices of latent variables: systems states, $x_{1:T}$, and initial conditions and disturbances $\{ x_{1},w_{1:T}\}$. Choosing latent states yields a joint likelihood function of the form

whereas latent disturbances leads to

where $x_{t + 1} = {{Ax_{t}} + {Bu_{t}} + {Gw_{t}}}$ for $t = {1,\ldots,T}$. We denote this *simulated* state sequence by

which, for given $\theta$, is a *deterministic* mapping from initial conditions and disturbances to system states.

One can begin to understand the relationship between the choice of latent variables and difficulty of the ensuing optimization problems by examining the joint log likelihood. For latent states, ${\log p_{\theta}}{(y_{1:T},x_{1:T})}$ decomposes as

Given $\{ u_{1:T},x_{1:T},y_{1:T}\}$, optimization of this function (w.r.t. $\theta$) amounts to simple linear least squares. Conversely, for latent disturbances, ${\log p_{\theta}}{(y_{1:T},x_{1},w_{1:T})}$, is given by

Here $\mathcal{E}{(\theta,u_{1:T},y_{1:T},x_{1},w_{1:T})}$ denotes the *simulation error*, defined

where $x_{1:T} = {\mathcal{X}_{T}{(\theta,u_{1:T},x_{1},w_{1:T})}}$. This dependence on the simulated state sequence renders optimization of a challenging nonlinear, nonconvex problem.

## EM with latent disturbances

In this section we detail the application of EM to the identification of LGSS models, when formulated with latent disturbances; refer to for the formulation over latent states. Each iteration of the algorithm involves optimization of the *auxiliary function*

which serves as a lower bound to the likelihood, given our current best estimate of the model parameters, $\theta_{k}$. With the joint log likelihood ${\log p_{\theta}}{(y_{1:T},x_{1},w_{1:T})}$ given by, to evaluate $Q{(\theta,\theta_{k})}$ we must compute $p_{\theta_{k}}{(x_{1},{w_{1:T} \mid y_{1:T}})}$, i.e., the joint smoothing distribution (JSD) of the initial state and disturbances. The E step then amounts to solving a *disturbance smoothing*, rather than *state smoothing*, problem, which reflects the use of disturbances, rather than states, as latent variables.

As demonstrated in Section 2.5, $L_{\theta}{(y_{1:T},x_{1},w_{1:T})}$ involves the simulated state sequence $\mathcal{X}_{T}{(\theta,}$\
$u_{1:T},x_{1},w_{1:T})$. As a consequence, we shall show that the M step is equivalent to a nonconvex simulation error minimization problem (c.f. ). This is in contrast to the latent states formulation, in which ${\max_{\theta}Q}{(\theta,\theta_{k})}$ reduces to linear least squares.

### Expectation step

To compute $Q{(\theta,\theta_{k})}$ it is convenient to use the following decomposition

which was obtained by inserting into.

### Remark 2

Each term in is a function of different parameters: $\mu$ and $\Sigma_{1}$ appear only in $Q_{1}{(\theta,\theta_{k})}$; $\Sigma_{w}$ in $Q_{2}{(\theta,\theta_{k})}$; and $\Sigma_{v},A,B,G,C,D$ in $Q_{3}{(\theta,\theta_{k})}$. To emphasize this we introduce the following decomposition of $\theta$

The following lemma details the computation of $Q{(\theta,\theta_{k})}$. For clarity of expression, we introduce the following *lifted* form of the dynamics in,

where $Y = {\text{vec}{(y_{1:T})}}$, $U = {\text{vec}{(u_{1:T})}}$, $V = {\text{vec}{(v_{1:T})}}$, $Z = {\text{vec}{({\lbrack x_{1},w_{1:{T - 1}}\rbrack})}}$,

$\overline{C} = {I_{T} \otimes C}$ and $\overline{D} = {I_{T} \otimes D}$.

### Lemma 1

The auxiliary function $Q{(\theta,\theta_{k})}$ defined in is given by

${\hat{x}}_{1 \mid T}$ ${= {E_{\theta_{k}}\left\lbrack x_{1} \middle| y_{1:T} \right\rbrack}},$ (14a)
${\hat{\Sigma}}_{1 \mid T}$ ${= {{Var}_{\theta_{k}}\left\lbrack x_{1} \middle| y_{1:T} \right\rbrack}},$ (14b)

$\hat{Z}$ ${= {\text{E}_{\theta_{k}}\left\lbrack {Z \mid y_{1:T}} \right\rbrack}},$ (15a)
$\Omega$ ${= {\text{Var}_{\theta_{k}}\left\lbrack {Z \mid y_{1:T}} \right\rbrack}},$ (15b)

$\mu_{Y}$ ${\triangleq {E_{\theta}\left\lbrack Y \middle| Z \right\rbrack} = {{\overline{C}\overline{F}Z} + {{({{\overline{C}\overline{G}} + \overline{D}})}U}}},$ (16a)
$\Sigma_{Y}$ ${\triangleq {{Var}_{\theta}\left\lbrack Y \middle| Z \right\rbrack} = {I_{T} \otimes \Sigma_{v}}},$ (16b)

### Proof

The first term in is given by

Ignoring constant terms and scaling factors yields

where ${\hat{x}}_{1|T}$ and ${\hat{\Sigma}}_{1|T}$ are given in.

As the disturbances are i.i.d., $Q_{2}{(\beta,\theta_{k})}$ is given by

Once more ignoring constants, this reduces to

Finally, we turn our attention to $Q_{3}{(\gamma,\theta_{k})}$. The p.d.f. $p_{\theta}{({y_{1:T} \mid {x_{1},w_{1:T}}})}$ is given by ${p_{\theta}{({Y \mid Z})}} = {\mathcal{N}{(Y;\mu_{Y},\Sigma_{Y})}}$, where $\mu_{Y}$ and $\Sigma_{Y}$ are given in. $Q_{3}{(\gamma,\theta_{k})}$ may then be expressed as

Letting $\hat{Z}$ and $\Omega$, defined in, denote the mean and covariance (respectively) of $p_{\theta_{k}}{(x_{1},}$\

where $\Delta = {E_{\theta_{k}}\left\lbrack {Y - \mu_{Y}} \middle| y_{1:T} \right\rbrack}$ is defined in. ∎

Calculating the quantities in amounts to a state smoothing problem, the solution for which is given in closed form by, e.g., the RTS smoother (see also, \[23, Section 4.4\]). Similarly, for the LGSS models considered in this work, $E_{\theta_{k}}\left\lbrack {w_{t}w_{t}^{\prime}} \middle| Y_{T} \right\rbrack$, $\hat{Z}$ and $\Omega$ can be computed in closed form by standard disturbance smoothers; see, e.g., \[23, Section 4.5\].

### Maximization step

To perform the M step, i.e. maximize $Q{(\theta,\theta_{k})}$, we will utilize the same decomposition as in, and optimize each of the conditional expectations separately; the validity of this approach is established by Remark 2.

We begin with maximization of $Q_{1}{(\alpha,\theta_{k})}$:

### Lemma 2

The solution to $\alpha_{k + 1} = {{\arg{\max_{\alpha}Q_{1}}}{(\alpha,\theta_{k})}}$ is given by $\alpha_{k + 1} = {\{{\hat{x}}_{1|T},{\hat{\Sigma}}_{1|T}\}}$.

### Proof

To maximize $Q_{1}{(\alpha,\theta_{k})}$, notice that is concave w.r.t. $\mu$ and $\Sigma_{1}^{- 1}$. Therefore, setting the gradient to zero gives the global maximizers $\mu = {\hat{x}}_{1|T}$ and $\Sigma_{1} = {\hat{\Sigma}}_{1|T}$. ∎

Maximization of $Q_{2}{(\beta,\theta_{k})}$ can be handled in a similar way:

### Lemma 3

The solution to $\beta_{k + 1} = {{\arg{\max_{\beta}Q_{2}}}{(\beta,\theta_{k})}}$ is given by $\beta_{k + 1} = {\hat{\Sigma}}_{w}$ where

### Proof

Substituting into yields

This function is concave w.r.t. $\Sigma_{w}$ and so setting the gradient to zero gives the global maximizer $\Sigma_{w} = {\hat{\Sigma}}_{w}$. ∎

Finally, we consider maximization of $Q_{3}{(\gamma,\theta_{k})}$. This is a challenging problem, due to its dependence on *simulated* state sequences; c.f. Section 2.5. Indeed, from, it is clear that the quantities $\overline{F}$ and $\overline{G}$ render $Q_{3}{(\gamma,\theta_{k})}$ a nonconvex function of the model parameters.

To maximize $Q_{3}{(\gamma,\theta_{k})}$ it is convenient to conceptualize as the summation of $T + 1$ simultaneous simulation error minimization problems.

### Lemma 4

Recalling the definition of simulation error in, $Q_{3}{(\gamma,\theta_{k})}$ in is equivalent to:

where $x_{1}^{j},w_{1:T}^{j}$ are such that $\Omega = {\sum_{j = 1}^{T}{\omega_{j}\omega_{j}^{\prime}}}$ for $\omega_{j} = {\text{vec}{({\lbrack x_{1}^{j},w_{1:{T - 1}}^{j}\rbrack})}}$.

### Proof

First consider the $\text{tr}{({\Sigma_{Y}\Delta\Delta^{\prime}})}$ term in. From, $\Delta$ is clearly the difference between the measured output $y_{1:T}$ and the simulated output of the model with the expected value of the latent disturbances, i.e.

Next, consider the $\text{tr}{({\Sigma_{Y}^{- 1}\overline{C}\overline{F}\Omega{\overline{F}}^{\prime}{\overline{C}}^{\prime}})}$ term. Decomposing $\Omega$ as the sum of $T$ rank one matrices, i.e. $\Omega = {\sum_{j = 1}^{T}{\omega_{j}\omega_{j}^{\prime}}}$, leads to

where $x_{t + 1}^{j} = {{Ax_{t}^{j}} + {Gw_{t}^{j}}}$. One can interpret this as the sum of $T$ simulation error problems with $y_{1:T} \equiv 0$, $u_{1:T} \equiv 0$, ${\{ x_{1},w_{1:T}\}} = \omega_{j}$. ∎

To summarize, the computations involved in each iteration of the EM algorithm (formulated with latent disturbances) are straightforward, with the exception of maximization of $Q_{3}{(\gamma,\theta_{k})}$. From, this maximization is equivalent to $T + 1$ simultaneous nonconvex simulation error minimization problems.

## Lagrangian relaxation of maximization step

In this section we describe how Lagrangian relaxation (c.f. Section 2.4) can be applied to the optimization of $Q_{3}{(\gamma,\theta_{k})}$ in. Specifically, we shall develop a bound for $Q_{3}{(\gamma,\theta_{k})}$ that can be efficiently optimized as a convex program. Furthermore, we shall show how this approach naturally enforces model stability at each iteration, by searching over a convex parametrization of all stable linear models.

### Lagrangian relaxation of simulation error

Optimization of $Q_{3}{(\gamma,\theta_{k})}$ in is difficult because it requires minimization of *simulation error*, as defined in. In this subsection, we detail the application of Lagrangian relaxation, introduced in Section 2.4, to minimization of simulation error, which can be formulated as

$J^{\ast} \triangleq \min\limits_{\gamma,x_{1:T}}$ ${J{(\gamma,x_{1:T})}} \triangleq {\sum\limits_{t = 1}^{T}{|{y_{t} - {Cx_{t}} - {Du_{t}}}|}_{\Sigma_{v}^{- 1}}^{2}}$ (23a)

Here $\xi_{1}$ denotes the initial state, assumed to be known, and $\mathcal{F}{(\gamma,u_{1:T},\xi_{1},x_{1:T},w_{1:T})}$ encodes the dynamic constraints on $x_{1:T}$, such that

As in, the Lagrangian relaxation of takes the form

and, for arbitrary multiplier $\lambda$, represents a convex upper bound on the simulation error $\mathcal{E}{(\gamma,u_{1:T},}$\

### Implicit dynamics

It remains to choose the Lagrange multiplier $\lambda$ such that ${\overline{J}}_{\lambda}{(\gamma)}$ is a useful upper bound, i.e., such that ${\overline{J}}_{\lambda}^{\ast} \approx J^{\ast}$. Unfortunately, the simultaneous search for $\lambda$ and $\gamma$ is not jointly convex, due to the coupling between $\lambda$ and $\mathcal{F}$, and so $\lambda$ must be specified in advance. However, we can alleviate this restriction by searching over an implicit representation of the dynamics in (1a)

where $E$ is invertible such that $A = {E^{- 1}F}$, $B = {E^{- 1}K}$ and $G = {E^{- 1}L}$. With the implicit dynamics of, the dynamics constraint can be expressed

where $\overline{F} \in {\mathbb{R}}^{{{Tn_{x}} \times T}n_{x}}$ and $\epsilon \in {\mathbb{R}}^{Tn_{x}}$ denote

respectively. One may interpret the convex bound resulting from this implicit formulation as that of, but with the multiplier ${({I \otimes E^{\prime}})}\lambda$, thereby allowing a simultaneous (partial) search for multipliers and model parameters.

### Remark 3

We introduce $\eta = {\{ E,F,K,L,C,D,\Sigma_{v},P\}}$ to group the implicit model parameters, $\Sigma_{v}$ and $P \in {\mathbb{S}}_{+ +}^{n_{x}}$, into a single variable. Here $P$ represents a model stability certificate, the role of which is made precise in Lemma 6. Henceforth, ${\overline{J}}_{\lambda}{(\eta)}$ denotes Lagrangian relaxation with the implicit dynamics constraint. For convenience, we define the mapping $\mathcal{M}:{\eta\mapsto\gamma}$ from an implicit to explicit parametrization: ${\mathcal{M}{(\eta)}} \triangleq {\{\Sigma_{v},{E\backslash F},{E\backslash K},{E\backslash L},C,D\}}$.

### Convex upper bound for $- {Q_{3}\hspace{0pt}{(\gamma,\theta_{k})}}$

The representation of $Q_{3}{(\gamma,\theta_{k})}$ in makes the application of Lagrangian relaxation straightforward. To obtain a convex upper bound for $- {Q_{3}{(\gamma,\theta_{k})}}$ we can simply replace each simulation error term $\mathcal{E}{(\gamma)}$ with the appropriate corresponding convex bound ${\overline{J}}_{\lambda}{(\eta)}$.

### Lemma 5

Consider the following function

where $x_{1}^{j},w_{1:T}^{j}$ are defined in Lemma 4. ${\overline{Q}}_{3}{(\eta)}$ is a convex upper bound for $- {Q_{3}{(\gamma,\theta_{k})}}$, where $\gamma = {\mathcal{M}{(\eta)}}$.

### Proof

As ${\overline{Q}}_{3}{(\eta)}$ is defined by a summation of convex functions, it is itself a convex function. Summation of the following inequalities

gives ${{\overline{Q}}_{3}{(\eta)}} \geq {- {Q_{3}{(\gamma,\theta_{k})}}}$. Notice that $n_{y} + {\log{\det\Sigma_{v_{k}}}} + {\text{tr}{({\Sigma_{v_{k}}^{- 1}\Sigma_{v}})}}$ is an affine upper bound on the concave term $\log{\det\Sigma_{v}}$, which is tight at our current best estimate of the covariance, $\Sigma_{v_{k}}$. ∎

Notice that ${\overline{Q}}_{3}{(\eta)}$ is a function of an implicit representation of the dynamical model, denoted $\eta$, reflecting the fact that we formulate the Lagrangian relaxation using the implicit dynamics of (25a).

### Lagrange multipliers

To utilize the convex bound ${\overline{Q}}_{3}{(\eta)}$ we must supply suitable Lagrange multipliers, ${\{\lambda^{j}\}}_{j = 0}^{T}$. While convexity of the upper bound ${\overline{J}}_{\lambda}$ defined in is guaranteed for any multiplier $\lambda$ that is independent of $\eta$, in this work we consider multipliers of the form $\lambda = {\text{vec}\left( {\{\lambda_{t}\}}_{t = 1}^{T} \right)}$ for $\lambda_{t} = {2\left( {{Hx_{t}} + h_{t}} \right)}$, i.e.

where $\Lambda = {I_{T} \otimes H}$ for $H \in {\mathbb{R}}^{n_{x} \times n_{x}}$ and $h \in {\mathbb{R}}^{Tn_{x}}$. Recall from Section 4.2 that the use of the implicit model class allows a convex (partial) search over model parameters and multipliers. Furthermore, this implicit representation permits the following definition of a convex parametrization of all stable LTI models.

### Lemma 6

Let $\Theta{(H)}$ denote the set of all models $\eta$ of the form and $P \in {\mathbb{S}}_{+ +}^{n_{x}}$ that satisfy the LMI

i.e. ${{\Theta{(H)}} \triangleq {\{\eta:{{M{(\eta,H)}} > 0}\}}}.$

Then a model $\theta$ of the form is stable iff there exists $E$ such that $\eta = {\{ E,{EA},{EB},{EG},C,D,P\}} \in {\Theta{(H)}}$ for some full-rank $H \in^{n_{x} \times n_{x}}$.

### Proof

This result is a straightforward extension of Lemma 4 and Corollary 5 in \[24, Section 3.2\]. ∎

### Remark 4

The LMI ${M{(\eta,H)}} > 0$ implies ${{H^{\prime}E} + {E^{\prime}H}} > 0$ which ensures that $E$ is invertible, i.e., the implicit dynamics in are well-posed.

The model stability condition and multiplier also guarantee finiteness of the supremum in:

### Lemma 7

Given arbitrary $u_{1:T}$, $y_{1:T}$, $\xi_{1}$, $w_{1:T}$, $h$ and full-rank $H$ the supremum in the definition of ${\overline{J}}_{\lambda}{(\eta)}$ given by is finite, for $\lambda$ given by and $\eta \in {\Theta{(H)}}$.

### Proof

For ease of exposition, we define

where $u_{1:T}$, $w_{1:T}$, $\xi_{1}$ are dropped from the notation for brevity. The bound in may then be equivalently expressed as ${{\overline{J}}_{\lambda}{(\eta)}} = {\sup_{x_{1:T}}{J_{\lambda}{(\eta,x_{1:T})}}}$. We can write

where $\text{aff}{(x_{1:T})}$ denotes additional terms that are affine in $x_{1:T}$. We make use of the inequality

(see, e.g., \[12, Section IV\]) to obtain an upper bound for $J_{\lambda}{(\eta,x_{1:T})}$. Specifically, by setting $a = x_{t + 1}$ and $b = {H^{\prime}Fx_{t}}$ we obtain the inequality

which holds for all $x_{t},x_{t + 1}$. Applying to to yields the following upper bound:

The supremum w.r.t. $x_{1:T}$ of the upper bound on the LHS of is finite when the quadratic component is concave, i.e., ${{{{|{H^{\prime}F}|}_{P^{- 1}}^{2} + P} - {H^{\prime}E} - {E^{\prime}H}} + {|C|}_{\Sigma_{v}^{- 1}}^{2}} < 0$. By the Schur complement this condition is equivalent to the LMI in. As finiteness of the bound implies finiteness of $J_{\lambda}{(\eta,x_{1:T})}$ this completes the proof. ∎

The key to the EM algorithm is, i.e., increasing $Q{(\theta,\theta_{k})}$ guarantees an improvement in $L_{\theta}{(y_{1:T})}$. Consequently, we must ensure that optimization of ${\overline{Q}}_{3}{(\eta)}$ does not decrease $Q_{3}{(\gamma,\theta_{k})}$. This property holds if there exist multipliers ${\{\lambda^{j}\}}_{j = 0}^{T}$ such that the bound ${\overline{Q}}_{3}{(\eta)}$ is 'tight' to $- {Q_{3}{(\gamma,\theta_{k})}}$ at $\gamma = {\mathcal{M}{(\eta)}} = \gamma_{k}$, and may be understood as an application of the MM principle of Section 2.3.

To obtain such a set of multipliers, we can minimize the bound ${\overline{Q}}_{3}{(\eta_{k})}$ w.r.t. the multipliers ${\{\lambda^{j}\}}_{j = 1}^{T}$ for a fixed $\eta_{k}$. Here $\eta_{k}$ is such that $\gamma_{k} = {\mathcal{M}{(\eta_{k})}}$. We propose a two-stage approach:

For each of the $T + 1$ bounds ${\overline{J}}_{\lambda^{j}}{(\eta)}$ that comprise ${\overline{Q}}_{3}{(\eta)}$, solve the convex optimization problem

where $\phi_{j} = {{I_{T} \otimes \Phi_{j}}\text{vec}{(x_{1:T})}}$.

Set $\lambda^{j} = {2\left( {{{I_{T} \otimes H_{j}}\text{vec}{(x_{1:T})}} + h_{j}} \right)}$ such that ${{\overline{J}}_{\lambda^{j}}{(\eta_{k})}} = {\mathcal{E}{(\gamma_{k})}}$, where $h_{j}$ is computed as in Lemma 8.

### Lemma 8

Given a model $\eta_{k} \in {\Theta{(H)}}$ of the form, and arbitrary $u_{1:T}$, $y_{1:T}$, $x_{1}$, $w_{1:T}$ and full-rank $H$, let $\lambda$ denote a multiplier of the form with $h$ defined as

Furthermore, let $\theta_{k}$ be such that $A = {E\backslash F}$, $B = {E\backslash K}$ and $G = {E\backslash L}$. With this multiplier ${{\overline{J}}_{\lambda}{(\eta_{k})}} = {\mathcal{E}{(\theta_{k})}}$, i.e. the convex bound ${\overline{J}}_{\lambda}{(\eta)}$ is tight to the simulation error $\mathcal{E}{(\gamma)}$ at $\eta = \eta_{k}$. The notation is as follows: $\overline{F}$ and $\epsilon$ are defined in; $\overline{C}$, $\overline{D}$, $\Sigma_{Y}$, $U$, $Y$ are defined in Section 3.1; $X^{\ast} = {\text{vec}{({\mathcal{X}_{T}{(\eta_{k},u_{1:T},x_{1},w_{1:T})}})}}$ and

### Proof

As $\eta_{k} \in \Theta$, by Lemma 7, we know that $J_{\lambda}{(\eta,x_{1:T})}$, defined in, is a concave quadratic function in $x_{1:T}$. By the first order optimality condition, it can be shown that the state sequence $x_{1:T}^{\ast}$ that maximizes this function must satisfy

Setting $x_{1:T}^{\ast} = X^{\ast}$ and solving for $h$ yields the expression in. Note that invertibility of $E$ ensures that ${\overline{F}}^{- 1}$ is well-defined; c.f. Remark 4. As $x_{1:T}^{\ast} = X^{\ast}$ we have

In summary, to update $\gamma$ at the $k^{\text{th}}$ iteration of the EM algorithm, we solve the convex optimization problem

where $\lambda^{j}$ is given by with $H_{j}$ from and $h_{j}$ from, for $j = {0,\ldots,T}$, and then set $\gamma_{k + 1} = {\mathcal{M}{(\eta_{k + 1})}}$. For a complete summary of EM with latent disturbances, refer to Algorithm 1.

### Remark 5

A common heuristic for terminating the EM algorithm is to cease iterations once the change in likelihood falls below a certain tolerance $\delta$, i.e.

Alternatively, one can simply run the algorithm for a finite number of iterations, chosen so as to attain a model of quality sufficient for its intended application; this is the approach taken, e.g., in.

Set k = 0 and initialize θk such that Lθk (y1: T) is finite.

Assemble {λi}j = 0T of the form by computing {Hj}j = 0T with and {hj}j = 0T with.
Compute ηk + 1 by solving and set γk + 1 = ℳ (ηk + 1).

Terminate if, otherwise k ← k + 1 and return to step 2.

Algorithm 1 EM with latent disturbances

## Theoretical properties of identification via EM

### Singular state space models

In applications, it may arise that the dimension of the disturbance is less than that of the state variable, i.e. $n_{w} < n_{x}$. For example, consider a simple mass-spring-damper system governed by ${{m\overset{¨}{s}} + {c\overset{˙}{s}} + {ks}} = {u + w}$ for displacement $s$. When discretized, these dynamics can be represented by the second order state space model

with state variable $x_{t} = \left\lbrack {s{(t)}\overset{˙}{s}{(t)}} \right\rbrack^{\prime}$.

In such cases, the process noise covariance $G\Sigma_{v}G^{\prime}$ is singular, and standard EM algorithms based on latent states are no longer applicable. To see why, observe that the transition density of such a model is given by

As $G\Sigma_{w}G^{\prime}$ is rank deficient, the transition $p_{\theta}{({x_{t + 1} \mid x_{t}})}$ does not admit a density, and so we cannot evaluate, much less optimize, the joint log likelihood ${\log p_{\theta}}{(y_{1:T},x_{1:T})}$ given in. Modifications to the standard latent states EM algorithm have been proposed to circumvent this difficulty e.g. the work of introduces a perturbation model with full-rank process noise covariance. However, by choosing latent disturbances we can elegantly handle identification of both singular and full-rank state space models, with the same algorithm.

In particular, when formulating the EM algorithm over latent disturbances we work with the joint likelihood function $p_{\theta}{(y_{1:T},x_{1},w_{1:T})}$, given in. Comparing to, we observe that the problematic transition density is replaced by the joint distribution of disturbances

This distribution is independent of $n_{x}$, and so $p_{\theta}{(y_{1:T},x_{1},w_{1:T})}$ and, therefore, $Q{(\theta,\theta_{k})}$ remains well-defined, even in the singular case, $n_{w} < n_{x}$.

### Absence of disturbances or output noise

In this section, we study the auxiliary function $Q{(\theta,\theta_{k})}$ in the limit cases of $\Sigma_{w} = 0$ and $\Sigma_{v} = 0$, for different choices of latent variables. These results will offer insight into the behavior of the EM algorithm as a function of disturbance magnitude, as explored in the numerical experiments of Section 6.1. For convenience, we denote the bounds based on latent states and disturbances by $Q_{\text{ls}}{(\theta,\theta_{k})}$ and $Q_{\text{ld}}{(\theta,\theta_{k})}$, respectively.

### Proposition 9

Consider a model of the form, and let $\theta$ be such that $\Sigma_{w} = 0$, i.e. disturbances are omitted from the model. The auxiliary function built on latent states, $Q_{\text{ls}}{(\theta,\theta_{k})}$, is undefined when $A \neq A_{k}$ or $B \neq B_{k}$.

### Proof

When $\Sigma_{w} = 0$, given any $x_{1} \in^{n_{x}}$ the p.d.f. $p_{\theta_{k}}{({x_{1:T} \mid y_{1:T}})}$ is nonzero on the set $\mathcal{S}{(\theta_{k})} = {\{ x_{1:T}:x_{1:T} = \mathcal{X}{(\theta_{k},u_{1:T},x_{1},0)}\forall x_{1} \in^{n_{x}}\}}$. The auxiliary function may be expressed as

As $\Sigma_{w} = 0$, $p_{\theta}{({x_{2:T} \mid x_{1}})}$ is deterministic, evaluating to unity when $x_{1:T} = {\mathcal{X}{(\theta,u_{1:T},x_{1},0)}}$, and zero otherwise. When $A \neq A_{k}$ or $B \neq B_{k}$, ${{\log p_{\theta}}{({x_{2:T} \mid x_{1}})}} = 0$ for all $x_{1:T} \in {\mathcal{S}{(\theta_{k})}}$, and so ${\log p_{\theta}}{(x_{1:T},y_{1:T})}$ is undefined. As a consequence, $Q_{\text{ls}}{(\theta,\theta_{k})}$ is undefined.

When $A = A_{k}$ and $B = B_{k}$, ${p_{\theta}{({x_{2:T} \mid x_{1}})}} = 1$ for all $x \in {\mathcal{S}{(\theta_{k})}}$ and so $Q_{\text{ls}}{(\theta,\theta_{k})}$ can be evaluated as usual. ∎

### Proposition 10

Consider a model of the form, and let $\theta$ be such that $\Sigma_{w} = 0$, i.e. disturbances are omitted from the model. Furthermore, suppose $\Sigma_{1} = 0$; i.e. the initial conditions $x_{1} = \mu$ are modeled without uncertainty. Then ${L_{\theta}{(y_{1:T},x_{1})}} = {Q_{\text{ld}}{(\theta,\theta_{k})}}$ for all $\theta,\theta_{k}$; i.e., the auxiliary function built on latent disturbances, $Q_{\text{ld}}{(\theta,\theta_{k})}$, reduces to the log likelihood.

### Proof

As ${\Sigma_{w} = 0},{\Sigma_{1} = 0}$ the p.d.f. $p_{\theta_{k}}{(x_{1},{w_{1:T} \mid y_{1:T}})}$ is trivially deterministic, evaluating to unity when $x_{1} = \mu$ and $w_{1:T} \equiv 0$, and evaluating to zero otherwise. Therefore

The log likelihood can be decomposed as

where the final equality follows from the fact that $p_{\theta}{(x_{1})}$ is a $\delta$-function, at $x_{1} = \mu$. ∎

### Proposition 11

Consider a first order model of the form, and let $\theta$ be such that $\Sigma_{v} = 0$, i.e. output noise is omitted from the model. The auxiliary function built on latent disturbances, $Q_{\text{ld}}{(\theta,\theta_{k})}$, is undefined for $\theta \neq \theta_{k}$, i.e. $Q{(\theta,\theta_{k})}$ collapses to a single point at $\theta = \theta_{k}$.

### Proof

For a given $\theta$, let $x_{1:T}^{\theta}$ denote the unique state sequence that is 'consistent' with the data, i.e. $x_{1:T}^{\theta} \triangleq {\{ x_{1:T}:{{y_{t} = {{Cx_{t}} + {Du_{t}}}},{t = {1,\ldots,T}}}\}}$. There is also a corresponding unique disturbance sequence, denoted $w_{1:T}^{\theta} = {\{ w_{1:T}:{x_{1:T}^{\theta} = {\mathcal{X}{(\theta,u_{1:T},x_{1}^{\theta},w_{1:T})}}}\}}$.

As $\Sigma_{v} = 0$, the p.d.f. $p_{\theta_{k}}{(x_{1},{w_{1:T} \mid y_{1:T}})}$ is a $\delta$-function at $x_{1} = x_{1}^{\theta_{k}}$ and $w_{1:T} = w_{1:T}^{\theta_{k}}$. The auxiliary function is then given by

We can decompose $p_{\theta}{(y_{1:T},x_{1}^{\theta_{k}},w_{1:T}^{\theta_{k}})}$ as in. As $\Sigma_{v} = 0$, the p.d.f. $p_{\theta}{({y_{1:T} \mid {x_{1},w_{1:T}}})}$ is also a $\delta$-function at $x_{1} = x_{1}^{\theta}$ and $w_{1:T} = w_{1:T}^{\theta}$. If $C \neq C_{k}$ or $D \neq D_{k}$ then $x_{1}^{\theta} \neq x_{1}^{\theta_{k}}$. Furthermore, if $A \neq A_{k}$, $B \neq B_{k}$ or $G \neq G_{k}$, then ${\mathcal{X}{(\theta,u_{1:T},x_{1}^{\theta},w_{1:T}^{\theta})}} \neq {\mathcal{X}{(\theta_{k},u_{1:T},x_{1}^{\theta_{k}},w_{1:T}^{\theta_{k}})}}$. In both cases ${p_{\theta}{({y_{1:T} \mid {x_{1}^{\theta_{k}},w_{1:T}^{\theta_{k}}}})}} = 0$ and so $Q_{\text{ld}}{(\theta,\theta_{k})}$ is undefined.

When $\theta = \theta_{k}$, ${p_{\theta}{({y_{1:T} \mid {x_{1}^{\theta_{k}},w_{1:T}^{\theta_{k}}}})}} = 1$ and $Q_{\text{ld}}{(\theta,\theta_{k})}$ can be evaluated as usual. ∎

### Proposition 12

Consider a first order model of the form, and let $\theta$ be such that $\Sigma_{v} = 0$, i.e. output noise is omitted from the model. Let $Q_{\text{ls}}{(\theta,\theta_{k})}$ denote the auxiliary function built on latent states, then:

$Q_{\text{ls}}{(\theta,\theta_{k})}$ is undefined for all $\theta$ such that $C \neq C_{k}$ or $D \neq D_{k}$.

${Q_{\text{ls}}{(\theta,\theta_{k})}} = {L_{\theta}{(y_{1:T})}}$ for all $\theta$ such that $C = C_{k}$ and $D = D_{k}$.

### Proof

For a given $\theta$, let $x_{1:T}^{\theta}$ denote the unique state sequence that is 'consistent' with the data, i.e. $x_{1:T}^{\theta} \triangleq {\{ x_{1:T}:{{y_{t} = {{Cx_{t}} + {Du_{t}}}},{t = {1,\ldots,T}}}\}}$. As $\Sigma_{v} = 0$, given $y_{1:T}$ both $p_{\theta_{k}}{({x_{1:T} \mid y_{1:T}})}$ and $p_{\theta}{({y_{1:T} \mid x_{1:T}})}$ are $\delta$-functions at $x_{1:T} = x_{1:T}^{\theta}$. The auxiliary function is then given by

Let us now consider the two cases:

When $C \neq C_{k}$ or $D \neq D_{k}$, $x_{1:T}^{\theta} \neq x_{1:T}^{\theta_{k}}$ and so ${p_{\theta}{({y_{1:T} \mid x_{1:T}^{\theta_{k}}})}} = 0$. Therefore, $Q_{\text{ls}}{(\theta,\theta_{k})}$ is undefined.

When $C = C_{k}$ and $D = D_{k}$, $x_{1:T}^{\theta} = x_{1:T}^{\theta_{k}}$ and so

The likelihood can be expressed as

where the second inequality comes from the fact that $p_{\theta}{({y_{1:T} \mid x_{1:T}})}$ is a $\delta$-function. Therefore, ${L_{\theta}{(y_{1:T})}} = {Q_{\text{ls}}{(\theta,\theta_{k})}}$.

## Numerical experiments

### Influence of disturbance magnitude on bound fidelity

In the following experiment, we investigate the fidelity of $Q{(\theta,\theta_{k})}$ as a bound on $L_{\theta}{(y_{1:T})}$, as a function of the magnitude of the disturbances, $w_{1:T}$, and the choice of latent variables. As in Section 5.2, we denote the bounds based on latent states and disturbances by $Q_{\text{ls}}{(\theta,\theta_{k})}$ and $Q_{\text{ld}}{(\theta,\theta_{k})}$, respectively. The results are presented in Figure 1, which depicts $Q_{\text{ls}}$, $Q_{\text{ld}}$ and $L_{\theta}{(y_{1:T})}$ for a first order ($n_{x} = 1$) LGSS model, each plotted as a function of the single unknown scalar parameter $\theta = A$.

We begin with the case of 'small' disturbances (i.e. $\Sigma_{w} \ll \Sigma_{v}$) as depicted in Figure 1(a), and observe the following: $Q_{\text{ld}}{(\theta,\theta_{k})}$ represents $L_{\theta}{(y_{1:T})}$ with high fidelity, whereas $Q_{\text{ls}}{(\theta,\theta_{k})}$ is localized about $\theta_{k}$. Such an observation is not without precedent. For instance, in the latent states formulation of \[9, Section 10\] it was noted that an initial disturbance covariance estimate $\Sigma_{w} = 0$ results in $\theta_{k} = \theta_{0}$ for all $k$; i.e. the model parameters are not improved. This suggests that $Q_{\text{ls}}{(\theta,\theta_{k})}$ fails to accurately represent $L_{\theta}{(y_{1:T})}$, except at $\theta = \theta_{0}$.

Proposition 9 makes this observation more precise: in the 1D case of Figure 1(a), when $\Sigma_{w} = 0$, $Q_{\text{ls}}{(\theta,\theta_{k})}$ is undefined for $A \neq A_{k}$. Taken together, Figure 1(a) and Proposition 9 suggest that as $\Sigma_{w}$ becomes smaller (relative to $\Sigma_{v}$) the bound $Q_{\text{ls}}{(\theta,\theta_{k})}$ becomes more localized about $\theta_{k}$, eventually collapsing to a single point when $\Sigma_{w} = 0$. Conversely, as $\Sigma_{w}$ (and $\Sigma_{1}$) decrease, $Q_{\text{ld}}{(\theta,\theta_{k})}$ becomes an increasingly accurate representation of the log likelihood, eventually reproducing $L_{\theta}{(y_{1:T})}$ *exactly*, when $\Sigma_{w}$ (and $\Sigma_{1}$) are identically zero, as in Proposition 10.

Turning our attention to the case of 'large' disturbances (i.e. $\Sigma_{w} \gg \Sigma_{v}$) as depicted in Figure 1(b), we observe the opposite behavior: $Q_{\text{ls}}{(\theta,\theta_{k})}$ faithfully represents the log likelihood, whereas $Q_{\text{ld}}{(\theta,\theta_{k})}$ appears to be localized about $\theta_{k}$. Once more, studying the limiting case $\Sigma_{v} = 0$ offers insight into this behavior: Proposition 11 states that when $\Sigma_{v} = 0$, $Q_{\text{ld}}{(\theta,\theta_{k})}$ is undefined for $A \neq A_{k}$.

Taken together, Figure 1(b) and Proposition 11 suggest that as $\Sigma_{v}$ decreases (i.e. as $\Sigma_{w}$ increases relative to $\Sigma_{v}$), the bound $Q_{\text{ld}}{(\theta,\theta_{k})}$ becomes more localized about $\theta_{k}$, eventually collapsing to a single point when $\Sigma_{v} = 0$. Conversely, for this 1D experiment with $\theta = A$, Proposition 12 states that $Q_{\text{ls}}{(\theta,\theta_{k})}$ will reproduce $L_{\theta}{(y_{1:T})}$ *exactly*, when $\Sigma_{v}$ is identically zero. Indeed, in Figure 1(b) with $\Sigma_{v} \ll \Sigma_{w}$, we observe $Q_{\text{ls}}{(\theta,\theta_{k})}$ representing the likelihood faithfully.

To summarize: in the case of 'large disturbances' (i.e. $\Sigma_{w} \gg \Sigma_{v}$), $Q_{\text{ld}}{(\theta,\theta_{k})}$ will tend to bound $L_{\theta}{(y_{1:T})}$ with greater fidelity, compared to $Q_{\text{ls}}{(\theta,\theta_{k})}$. In the case of 'small disturbances' (i.e. $\Sigma_{w} \ll \Sigma_{v}$) the converse is true.

(a) ‘Small’ disturbances: Σv = 1 × 10−3 and Σv = 1 × 10−2.

(b) ‘Large’ disturbances: Σw = 10 and Σv = 1 × 10−2.

Figure 1: Lower bounds to the log likelihood Lθ (y1: T) of a first order system with a single unknown scalar parameter, A. Qld (θ,θk) and Qls (θ,θk) denote the bounds based on latent disturbances and states respectively, while ${\overline{Q}{(\eta)}} = {{Q_{1}{(\alpha,\theta_{k})}} + {Q_{2}{(\beta,\theta_{k})}} + {{\overline{Q}}_{3}{(\eta)}}}$, where ${\overline{Q}}_{3}{(\eta)}$ is the bound based on Lagrangian relaxation defined in.

### Convergence rate

It is clear from Figure 1(a), that both $Q_{\text{ld}}{(\theta,\theta_{k})}$ and ${\overline{Q}}_{3}{(\eta)}$ better represent $L_{\theta}{(y_{1:T})}$ compared to $Q_{\text{ls}}{(\theta,\theta_{k})}$. In fact, one would expect that optimization of ${\overline{Q}}_{3}{(\eta)}$, as in Algorithm 1, would converge to $\theta^{\text{ML}}$ in fewer iterations than optimization of $Q_{\text{ls}}{(\theta,\theta_{k})}$, as in a 'standard' EM algorithm.

This principle, which is clearly understood in the first order example of Figure 1, is further illustrated in Figure 3 for three different $4^{\text{th}}$ order SISO systems; Bode plots for each system are given in Figure 2. The results in Figure 3 clearly show Algorithm 1, based on latent disturbances, converging in fewer iterations than the latent states formulation of. These results are consistent with the analysis in Section 6.1. Specifically, in each trial disturbances were 'small' in magnitude ($\Sigma_{w} = {1 \times 10^{- 5}}$) and so we expect ${\overline{Q}}_{3}{(\eta)}$ to better represent the likelihood, allowing Algorithm 1 to converge in fewer iterations.

It should be stressed that although Algorithm 1 converges in fewer iterations than the latent states formulation, each iteration is considerably more computationally expensive, and thus the total computation times for each algorithm are comparable. Nevertheless, this faster convergence rate is advantageous as it renders Algorithm 1 less sensitive to the choice of $\delta$ when termination conditions of the form are employed. Furthermore, as methods for SDP mature, one may expect Algorithm 1 to gain the upper hand in regards to computation time.

Figure 2: Bode plots of 4th order systems used for the experiments presented in Figure 3.

(a) System 1, sharp resonant peaks.

(b) System 2, smooth resonant peaks.

Figure 3: Difference between Lθk (y1: T) and Lθtrue (y1: T) (where θtrue denotes the true model parameters) as a function of iterations for Algorithm 1 (EM with latent disturbances, red) and the method of (EM with latent states, blue dashed). The difference is averaged over 10 trials, each with SNR of 100, Σv = 1 × 10−5 and T = 250. Also plotted are the best and worst trial results (in terms of final likelihood) for each system. Bode plots for systems 1, 2 and 4 are depicted in Figure 2.

### Stability of the identified model

A desirable property of Algorithm 1 is that stability of the identified model is enforced at every iteration; recall from Lemma 6 that we confine our search to an implicit parametrization of all stable models, which, by Lemma 7, is necessary to ensure that ${\overline{J}}_{\lambda}{(\eta)}$ is well-defined. Conversely, in a standard latent states implementation of the EM algorithm, the M step is accomplished by the solution of an unconstrained linear least squares problem. Consequently, it is possible that at any iteration (or indeed the conclusion) of the algorithm, the parameters $\theta_{k}$ could constitute an unstable model.

Such a scenario is illustrated in the numerical experiment of Figure 4, which depicts the identification of a $4^{\text{th}}$ order model, similar to System 2 in Figure 2. From Figure 4(b) it is apparent that, for the first one thousand iterations, the parameters maintained by the latent states EM algorithm represent an *unstable* model (i.e. ${|{\lambda_{\text{max}}{(A_{k})}}|} > 1$). This instability can be particularly problematic, given the slow convergence rate; e.g. in this instance, if a heuristic such as was used employed, for $\delta > {4.7 \times 10^{- 3}}$ the algorithm would terminate before the thousandth iteration, and an unstable model would be returned. Conversely, the parameters maintained by Algorithm 1 constitute a stable model at each iteration.

(a) Difference between Lθk (y1: T) and Lθtrue (y1: T), where θtrue denotes the true model parameters, at each iteration.

(b) Magnitude of the largest eigenvalue of Ak, at each iteration. When the spectral radius of Ak is greater than unity, i.e. |λmax (Ak)| &gt; 1, the model θk is unstable.

Figure 4: Log likelihood and spectral radius of Ak at each iteration for two different EM algorithms: i. EM with latent states as in (Lat. states, blue dash); ii. Algorithm 1 (Lat. dist. (LR), red). The spectral radius of A for the true system was 0.90.

## Conclusion

In this paper, we have formulated the EM algorithm over latent disturbances, rather than states, for the identification of linear dynamical systems. Our main contribution is the use of Lagrangian relaxation to obtain a convex approximation of the challenging maximization step, guaranteed not to decrease the likelihood at each iteration. Though more computationally complex, this formulation with latent disturbances allows EM to be applied to singular state-space models, where latent states based methods break down.

Extension of this approach to the identification of nonlinear models shall be the subject of future research. In the nonlinear case, two major challenges arise during the formulation of EM with latent disturbances. First, the E step (c.f. Section 3.1) now involves a nonlinear disturbance smoothing problem, for which no closed form solution is known to exist. In recent decades, *sequential Monte Carlo* (SMC) methods have emerged as effective tools for overcoming similar difficulties, having already proved useful in nonlinear, non-Gaussian *state smoothing* and *disturbance filtering* problems.

Second, nonlinearity of the model complicates the Lagrangian relaxation of the M step; e.g. the bound ${\hat{J}}_{\lambda}{(\eta)}$ cannot be evaluated analytically, as the supremum (in ) requires optimization of a function that is no longer quadratic in $x$. To proceed, one might approximate the simulation error terms in $Q_{3}{(\gamma,\theta_{k})}$ with the *linearized simulation error*, introduced in, to which the Lagrangian relaxation presented in this work can be applied with little modification. Alternatively, when the system nonlinearity is modeled as a polynomial, *sum-of-squares* (SOS) programing may be used to generate, and optimize, convex approximations to the Lagrangian relaxation.
