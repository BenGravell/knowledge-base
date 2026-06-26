<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimistic Robust Linear Quadratic Dual Control

Topics include Convex optimization, Regret bounds, Robustness, Uncertainty, Optimization, Control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent work by Mania et al. has proved that certainty equivalent control achieves nearly optimal regret for linear systems with quadratic costs. However, when parameter uncertainty is large, certainty equivalence cannot be relied upon to stabilize the true, unknown system. In this paper, we present a dual control strategy that attempts to combine the performance of certainty equivalence, with the practical utility of robustness. The formulation preserves structure in the representation of parametric uncertainty, which allows the controller to target reduction of uncertainty in the parameters that `matter most' for the control task, while robustly stabilizing the uncertain system. Control synthesis proceeds via convex optimization, and the method is illustrated on a numerical example.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since the initial formulation of the `dual control' problem by [feldbaum1960dual] in the 1960s, learning to make decisions in uncertain and dynamic environments has remained a topic of sustained research activity. However, recent years have witnessed a resurgence of interest in such problems, inspired perhaps in part by the dramatic success of reinforcement learning, cf. [mnih2015human, silver2016mastering]. Specifically, linear systems with quadratic costs, a.k.a. `the linear quadratic regulator', have been the subject of intense recent study, cf. [matni2019self]. Such research typically focuses on two main aspects: i) performance, usually measured in terms of bounds on regret, and ii) robustness, i.e., stability of the closed-loop system, which is often important in practical applications. Concerning the former, the work of [mania2019certainty]has proved that `certainty equivalent' (CE) control (nearly) achieves the optimal regret bound; provided that this controller stabilizes the system, which is the case when parameter uncertainty is sufficiently small.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inspired by this result, the present paper attempts to combine the performance of certainty equivalence with the practical advantages of robustness. Specifically, we propose a dual control strategy, for linear systems with quadratic costs, that optimizes for performance of the nominal, i.e., most likely, system (as in CE control), while robustly stabilizing the system in the presence of parametric uncertainty. The dual controller performs `targeted exploration', attempting to reduce uncertainty in the parameters that `matter most' for control, while balancing the exploration-exploitation tradeoff.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The contributions of this paper are twofold.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

\S[sec:robust\_synthesis], we present a convex formulation of optimization of quadratic cost, for a nominal linear system, subject to robust stability guarantees under parametric uncertainty. This extends the existing system level synthesis (SLS) framework, by preserving structure in the representation of system uncertainty. In \S[sec:dual\_synthesis], we build upon this formulation to present an (approximate) dual control strategy, exploiting the preservation of structure to perform exploration that targets uncertainty reduction in the specific parameters that are `preventing' certainty equivalent control from stabilizing the uncertain true system.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Of greatest relevance to the present paper is the work of [mania2019certainty], which proves that certainty equivalence, i.e., estimating model parameters via online least squares and then applying LQR, achieves (nearly optimal) $\tilde{\mathcal{O}}(\sqrt{T})$ regret. This result holds when the parameter error is sufficiently small so as to ensure closed-loop stability of the true system, which does not always hold in practice, e.g., [dean2017sample]. Many recent works have addressed the issue of robustness in adaptive control, cf. [dean2017sample,dean2018regret,dean2018safely,cohen2018online]. The work of [umenberger2019robust], cf. also [ferizbegovic2019learning,iannelli2019structured], attempts to do `targeted-exploration' by prioritizing uncertainty reduction in the system parameters to which performance is most sensitive. These methods consider worst-case costs to bound performance on the true system, and as such, can be conservative in practice.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is the ambition of this paper the benefits of `targeted exploration' with a more `optimistic' CE strategy, that optimizes for performance of the nominal, rather than worst-case, system. Other recent work on adaptive linear quadratic control includes Thompson sampling (e.g. [ouyang2017learning,abeille2017thompson,abeille2018improved]), model-free (e.g. [fazel2018global,malik2018derivative]) and partially model-free (e.g. [agarwal2019online,agarwal2019logarithmic]) methods, as well as the `optimism in the face of uncertainty' heuristic (e.g. [abbasi2011regret,ibrahimi2012efficient,faradonbeh2017finite]).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem statement", "weight": 1.0} -->

In this section we describe in detail the problem addressed in this paper. Notation is largely standard. $\otimes$ denotes the Kronecker product. $\sym{n}$ denotes the space of $n\times n$ symmetric matrices. w.p. means `with probability'. $\chiSquare{n}{p}$ denotes the value of the Chi-squared distribution with $n$ degrees of freedom and probability $p$. The space of real, proper (strictly proper) transfer matrices is denoted $\mathcal{R}\mathcal{H}_{\infty}$ ($\frac{1}{z}\mathcal{R}\mathcal{H}_{\infty}$). With some abuse of notation, $[t_1,t_2]$ for $t_1,t_2\in\mathbb{N}$ denotes $\lbrace t_1,\dots,t_2\rbrace$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem statement", "weight": 1.0} -->

Dynamics and modeling We are concerned with control of linear time-invariant systems w_t \sim \normal{0}{\sigma_w^2I_{n_x}}, \quad x_0 = 0, where $x_t \in \mathbb{R}^{n_x}$, $u_t \in \mathbb{R}^{n_u}$ and $w_t \in \mathbb{R}^n$ denote the state (which is assumed to be directly measurable), input and process noise, respectively, at time $t$. We assume that the true parameters $\lbrace {A_\textup{tr}},{B_\textup{tr}}\rbrace$ are unknown; as such, all knowledge about the true system dynamics must be inferred from observed data, $\mathcal{D}_n:= \lbrace x_t,u_t\rbrace_{t=1}^n$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem statement", "weight": 1.0} -->

We assume that $\sigma_w$ is known, or has been estimated, and that we have access to initial data, denoted (with slight notational abuse) $\mathcal{D}_0$, obtained, e.g. during a preliminary experiment. Given data $\mathcal{D}_n$ we define a model $\mathcal{M}_{\delta}(\mathcal{D}_n) = \lbrace \hat{A},\hat{B},D\rbrace$, where $(\hat{A},\hat{B}):= \arg\min_{A,B} \sum_{t=1}^{n-1}|x_{t+1}-Ax_t-Bu_t|^2$ denote nominal parameters given by the ordinary least squares estimates of $({A_\textup{tr}},{B_\textup{tr}})$, and $D\in\sym{n_x+n_u}$ is a matrix that quantifies the uncertainty in our nominal parameter estimate.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem statement", "weight": 1.0} -->

$\lbrace{A_\textup{tr}}, \ {B_\textup{tr}}\rbrace\in {\Theta_m}(\mathcal{M}_{\delta})$ w.p. $1-\delta$. [lem:credibility\_region] is a consequence of the fact the posterior distribution of parameters $A,B$ (for a uniform prior) is Gaussian for models of the form [eq:lti], cf. e.g. [umenberger2018learning]. Similar credibility regions have been attained using results from high-dimensional statistics in recent works such as [dean2017sample].

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem statement", "weight": 1.0} -->

Our objective is to design a feedback control policy so as to minimize the cost function $\sum_{t=1}^T \ c(x_t,u_t)$, where $c(x_t,u_t) = x_t^\topQ x_t + u_t^\topR u_t $ for user-specified positive semidefinite matrices $Q$ and $R$. When the parameters of the true system, $\lbrace {A_\textup{tr}},{B_\textup{tr}}\rbrace$, are known this is the well-known LQR problem. As discussed, we do not assume knowledge of the true parameters; as such, the controller must regulate and learn the system simultaneously. To this end, we partition the total `control time' $[1,T]$ into two intervals: $[1,{T_e}]$ and $[{T_e}+1,T]$ for ${T_e}\in\mathbb{N}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem statement", "weight": 1.0} -->

At time $t=1$, given initial data $\mathcal{D}_0$, a policy $\phi_1$ is designed and applied to the system for $t\in[1,{T_e}]$. Then, at time $t={T_e}+1$, a new policy $\phi_2$ is designed, based on $\mathcal{D}_0$ and data $\mathcal{D}_{{T_e}}$ collected under $\phi_1$. Policy $\phi_2$ is then applied for $t\in[{T_e}+1,T]$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem statement", "weight": 1.0} -->

We can write this control task as: \min_{\phi_1,\phi_2} \quad \mathbb{E} {\sum}_{t=1}^T c(x_t,u_t), \quad \textup{s.t.} \ &\textup{ dynamics in } eq:lti \text{ with } A={A_\textup{tr}}, \ B={B_\textup{tr}}, \\& u_t = \phi_1(\cdot), \ t = 1,\dots,{T_e}, \u_t = \phi_2(\cdot), \ t = {T_e}+1,\dots,T. \nonumber One can think of the first interval, $[1,{T_e}]$, as an `exploration' or `learning' period where the data collected is used to design an improved controller, $\phi_2$, applied during the second interval $[{T_e}+1,T]$, which could be considered an `exploitation' period.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem statement", "weight": 1.0} -->

However, the task is to minimize the total cost therefore, it is important to balance exploration and exploitation. The decision to nominate a specific time, ${T_e}$, at which the control policy will be `updated' requires some justification. A more natural formulation might update the controller whenever new data becomes available. We shall discuss this aspect of the formulation in more detail in \S[sec:discussion], where alternative formulations are considered. For now, suffice to say that this formulation, i) simplifies the presentation of the technical developments to follow, and ii) still captures the importance of balancing `exploration' with `exploitation.'

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem statement", "weight": 1.0} -->

Observe that the control task in [eq:ideal\_control\_task] depends on the true, but unknown, system parameters ${A_\textup{tr}},{B_\textup{tr}}$, as we want to optimize for performance on the true system. In place of the true system parameters, we will optimize for our `best guess' of the parameters, i.e., the nominal parameters $\hat{A},\hat{B}$ from least squares corresponding to the mode of the posterior distribution. To ensure reasonable behavior of the true system in closed-loop, we also require the controllers to stabilize the true system with high probability. Let $\mathcal{S}_\textup{CL}(A,B,\phi)$ denote the closed loop system formed by combining [eq:lti] with the policy $\phi$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Controller synthesis", "weight": 1.0} -->

bold symbols denote the z-transform of time domain signals, e.g., the z-transform of $x$ is denoted $\textbf{x}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Preliminary results from System Level Synthesis", "weight": 1.0} -->

In this section we review some essential results from the System Level Synthesis (SLS) framework proposed by [wang2019system]; for a comprehensive tutorial, cf. [anderson2019system]. Consider the closed-loop behavior of [eq:lti] under the stabilizing controller $\textbf{u} = \textbf{K}\textbf{x}$; in particular, consider the transfer functions $\mathbf{\Phi_x}$ and $\mathbf{\Phi_u}$ from disturbance $\textbf{w}$ to state $\textbf{x}$ and control $\textbf{u}$, respectively.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Preliminary results from System Level Synthesis", "weight": 1.0} -->

This can be expressed as \left[\begin{array}{c} \end{array}\right] \left[\begin{array}{c} \mathbf{\Phi\_x} \\ \mathbf{\Phi\_u} \end{array}\right] Following in the spirit of the Youla parameterization, rather than designing the controller $\textbf{K}$ to obtain the closed-loop responses $\mathbf{\Phi_x} = (zI-A-B\textbf{K})^{-1}$ and $\mathbf{\Phi_u}=\textbf{K}\mathbf{\Phi_x}$, in SLS one designs the closed-loop responses directly, and then recovers the controller as $\textbf{K} = \mathbf{\Phi_u}\mathbf{\Phi_x}^{-1}$. The following theorem characterizes the space of all closed-loop responses achievable by a stabilizing controller.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Preliminary results from System Level Synthesis", "weight": 1.0} -->

The affine subspace defined by $$\left[\begin{array}{cc} \end{array}\right] \left[\begin{array}{c} \mathbf{\Phi_x} \\ \mathbf{\Phi_u} \end{array}\right] = I, \quad \mathbf{\Phi_x},\mathbf{\Phi_u}\in\frac{1}{z}\mathcal{R}\mathcal{H}_{\infty},$$ parametrizes all closed-loop responses achievable by a stabilizing controller. Further, the response is achieved by the controller $\textbf{K} = \mathbf{\Phi_u}\mathbf{\Phi_x}^{-1}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Preliminary results from System Level Synthesis", "weight": 1.0} -->

The following theorem considers a `perturbed' version of the constraints in [eq:sls\_affine], that is useful for synthesizing robust controllers, e.g., when the system parameters $A$,$B$ are uncertain.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Preliminary results from System Level Synthesis", "weight": 1.0} -->

While the preceding theorems define affine subspaces (i.e. [eq:sls\_affine] and [eq:sls\_robust]) that are convenient to optimize over, the decision variables $\mathbf{\Phi_x}$ and $\mathbf{\Phi_u}$ are infinite dimensional transfer matrices. As is common in the SLS framework, we will work with finite impulse response (FIR) approximations: $$\mathbf{\Phi_x}(z) = {\sum}_{k=0}^F \Phi_x^kz^{-k}, \quad \mathbf{\Phi_u}(z) = {\sum}_{k=0}^F \Phi_u^kz^{-k}.$$ Henceforth, we will restrict our attention to policies of the form $\phi(z) = \mathbf{\Phi_u}(z)\mathbf{\Phi_x}(z)^{-1}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Robust control formulation", "weight": 1.0} -->

In this section, we present a convex formulation of the following problem: (approximately) optimize the infinite-horizon quadratic cost, for a given nominal model $\lbrace\hat{A},\hat{B}\rbrace$, while robustly stabilizing all models $\lbrace A,B\rbrace$ in the model set ${\Theta_m}(\mathcal{M}_{\delta})$. This result extends existing SLS formulations, by preserving the structure in the representation of uncertainty captured by $D$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Robust control formulation", "weight": 1.0} -->

To ensure robustness of the policy on the true, unknown system (as, e.g., [eq:stability\_1]), we make use of Theorem [thm:sls\_robust]. Specifically, as $\mathbf{\Phi_x}$ and $\mathbf{\Phi_u}$ are constrained to satisfy [eq:affine\_nominal], we can express $\mathbf{\Delta}$ in [eq:sls\_robust] as $\mathbf{\Delta} = (\hat{A}-{A_\textup{tr}})\mathbf{\Phi_x} + (\hat{B}-{B_\textup{tr}})\mathbf{\Phi_u}$, by substituting [eq:affine\_nominal] into [eq:sls\_robust], with $A={A_\textup{tr}}$ and $B={B_\textup{tr}}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Robust control formulation", "weight": 1.0} -->

By Theorem [thm:sls\_robust], the controller $\mathbf{\Phi_u}\mathbf{\Phi_x}^{-1}$ will stabilize the true system, if and only if $(I+\mathbf{\Delta})^{-1}$ is stable. Of course, $\mathbf{\Delta}$ is defined in terms of ${A_\textup{tr}},{B_\textup{tr}}$, which are unknown; however, by Lemma [lem:credibility\_region], they are known to lie in ${\Theta_m}(\mathcal{M}_{\delta})$ with high-probability. A sufficient condition for stability of $(I+\mathbf{\Delta})^{-1}$ is given by the small gain theorem: $\norm{\mathbf{\Delta}}{\mathcal{H}_{\infty}}\leq1$ implies stability of $(I+\mathbf{\Delta})^{-1}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Robust control formulation", "weight": 1.0} -->

We can now present the main contribution of this section.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Robust control formulation", "weight": 1.0} -->

The convex program $\min_{\mathbf{\Phi_x},\mathbf{\Phi_u},P} \ J_{\mathcal{H}_{2}}(\mathbf{\Phi_x},\mathbf{\Phi_u})$ s.t. [eq:affine\_nominal] optimizes the infinite-horizon cost. All that remains is to ensure robust stability: a sufficient condition is $\norm{\mathbf{\Delta}}{\mathcal{H}_{\infty}}\leq 1$. This sufficient, but not necessary, condition is the source of the conservatism, i.e., the reason we only have an upper bound.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Robust control formulation", "weight": 1.0} -->

$\norm{\mathbf{\Delta}}{\mathcal{H}_{\infty}}\leq 1$ can be enforced by combining Lemma [lem:hinf] with the following lemma: The data matrices $(\mathcal{A},\mathcal{B},\mathcal{C},\mathcal{P},\mathcal{F},\mathcal{G},\mathcal{H})$ satisfy, for all $X$ with $I-X^\top\mathcal{P} X\succeq 0$, the robust fractional quadratic matrix inequality \left[\begin{array}{cc} \mathcal{H} & \mathcal{F}+\mathcal{G} X \\(\mathcal{F}+\mathcal{G} X)^\top & \mathcal{C}+X^\top \mathcal{B} + \mathcal{B} ^\top X +X^\top \mathcal{A} X \end{array}\right] \succeq

<!-- chunk {"id": "body-0030", "role": "body", "section": "Robust control formulation", "weight": 1.0} -->

Let $\textbf{H}(z)$ (from Lemma [lem:hinf]) denote $\mathbf{\Delta}^\top$, then the [eq:hinf\_lmi] can be put in the form of the MI on the left in [eq:robust\_LMI] by choosing $\mathcal{G}=\mathbf{\bar{\Phi}}$, and $\mathcal{A},\mathcal{B},\mathcal{F}$ all zero. Further, by choosing $\mathcal{P}=D$ in Lemma [thm:robustlmi], the condition $I\succeq X^\top\mathcal{P}X$ is equivalent to $\lbrace {A_\textup{tr}},{B_\textup{tr}}\rbrace\in{\Theta_m}(\mathcal{M}_{\delta})$, cf. [eq:spectral\_region].

<!-- chunk {"id": "body-0031", "role": "body", "section": "Robust control formulation", "weight": 1.0} -->

The final constraint (LMI) in [eq:robust\_synth] is then equivalent to the second LMI in [eq:robust\_LMI], which implies that $\norm{\mathbf{\Delta}^\top}{\mathcal{H}_{\infty}}\leq 1$ for the true model parameters w.p. $1-\delta$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Robust control formulation", "weight": 1.0} -->

Observe that this formulation preserves the structure in the uncertainty representation, as encoded in the matrix $D$. This is in contrast to other SLS methods, e.g., [dean2017sample,dean2018safely], that reduce model uncertainty to a single (or at most two) scalar quantities, e.g., $\Vert\hat{A}-{A_\textup{tr}}\Vert_2\leq \epsilon_A$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Robust dual control formulation", "weight": 1.0} -->

In this section we return to the dual control problem outlined in [eq:control\_task], namely: minimize cost over $[1,T]$, via an initial policy $\phi_1$, designed using data $\mathcal{D}_0$, and applied for $t\in[1,{T_e}]$, followed by a second policy $\phi_2$, designed using additional data $\mathcal{D}_{T_e}$, and applied for $t\in[{T_e}+1,T]$. The key idea is dual control: $\phi_1$ affects not only the cost, but also the data $\mathcal{D}_{T_e}$ available for the design of $\phi_2$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Robust dual control formulation", "weight": 1.0} -->

In what follows, we will approximate the cost $\sum_{t=1}^N \mathbb{E} c(x_t,u_t)$ by the infinite-horizon (i.e. stationary value) $N\times\lim_{\tau\rightarrow\infty}\frac{1}{\tau}\sum_{t=1}^\tau\mathbb{E} c(x_t,u_t)$. Such an approximation can be expected to be valid when the horizon $N$ is sufficiently long, so as to allow the system to reach the stationary distribution. Alternatives to this approximation are discussed in \S[sec:discussion].

<!-- chunk {"id": "body-0035", "role": "body", "section": "Robust dual control formulation", "weight": 1.0} -->

Problem [eq:compact\_dual] cannot be solved exactly, as it depends on $\mathcal{D}_{{T_e}}$ which is not available at time $t=1$. As such, we must predict the influence that $\phi_1$ will have on `future' data $\mathcal{D}_{{T_e}}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Robust dual control formulation", "weight": 1.0} -->

First, note that we approximate the predicted nominal parameters by the current estimates. Updating these estimates based on the expected value of future data involves difficult integrals that must be computed numerically, which would destroy convexity, cf. [lobo1999policies]. The predicted `uncertainty matrix' $\tilde{\uncert}$ is defined as follows. Given $\mathcal{D}_{T_e}$, $D$ at time ${T_e}$ can be computed as \frac{1}{\sigma\_w^2c\_{\delta}} \sum\_{t=1}^{{T\_e}}\left[\begin{array}{c} \end{array}\right] \left[\begin{array}{c} \end{array}\right]^\top$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Robust dual control formulation", "weight": 1.0} -->

Convex relaxation of dual control By substituting the approximate model $\tilde{\mathcal{M}}(\phi_1)$ for $\mathcal{M}_{\delta}(\mathcal{D}_0\cup\mathcal{D}_{{T_e}})$ in [eq:compact\_dual], we can remove the dependence of the cost on unknown future data. Furthermore, observe that (for fixed $\lambda$) the LMI constraint in [eq:robust\_synth] is linear in $D$. This implies that we can optimize over $D$ and $\phi$ jointly, as a convex program. Unfortunately, $\tilde{\uncert}$ in $\tilde{\mathcal{M}}(\phi_1)$ is a quadratic function of $\phi_1$, and so directly substituting $D\rightarrow\tilde{\uncert}$results in a non-convex matrix inequality.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this section, we discuss the partitioning of $[1,T]$ into two sub-intervals. A downside of this approach is that it requires the user to explicitly specify the `exploration' period, i.e., select ${T_e}$. The proposed approach could also be considered a `one-step-look-ahead' dual control, as there is only a single period of exploration ($[1,{T_e}]$), before a single period of exploitation ($[{T_e},T]$). Such a drawback can be partially mitigated by adopting a 'multistep-look-ahead' strategy, as in [umenberger2019robust]. In such a framework, the current period of exploration is followed by further exploration, rather than pure exploitation. This approach also requires the user to select `epoch times', at which the controller will be updated.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Discussion", "weight": 1.5} -->

To circumvent this, one could adopt a model predictive control (MPC) strategy, with SLS as in [wang2019robust], but exploiting the dual control effect, as in [lobo1999policies]. The major obstacle to extending the proposed approach to the multistep or MPC setting is the need to search over more than one multiplier, $\lambda_2$, cf. [eq:final\_lmi]. Such extensions represent interesting directions for future research. At any rate, the method proposed in this paper could be used (with fixed multipliers) as a convex means of providing sub-optimal initialization for local search methods.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Numerical illustration", "weight": 1.0} -->

In this section we illustrate the proposed method with a numerical example. Consider the linear control problem with parameters: $${A_\textup{tr}} = \left[\begin{array}{cc} \end{array} \right], \{B_\textup{tr}} = \left[\begin{array}{cc} \end{array} \right], \Q= \left[\begin{array}{cc} \end{array} \right], \Q= \left[\begin{array}{cc} \end{array} \right], \Initial data $\mathcal{D}_0$ is generated by simulating [eq:lti] open-loop with $u_t\sim\normal{0}{I}$ for $t=6$ timesteps; this is repeated 10 times. For control, $T=100$, ${T_e}$, and $F=12$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Numerical illustration", "weight": 1.0} -->

We compare three methods: i) nominal control: $\phi_1=\arg\min_\genpolicyJ_{\infty}(\phi,\mathcal{M}_{\delta}(\mathcal{D}_0))$ and $\phi_2=\arg\min_\genpolicyJ_{\infty}(\phi,\mathcal{M}_{\delta}(\mathcal{D}_0\cup\mathcal{D}_{{T_e}}))$, i.e., no explicit exploration; ii) dual control: as proposed in this paper; iii) greedy control: $\phi_1$ is given by $u=\textbf{K} x+e$ where $\textbf{K}$ is the nominal controller (i), and $e\sim\normal{0}{\sigma I}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Numerical illustration", "weight": 1.0} -->

$\sigma$ is tuned to give the same exploration cost as dual control on the true, and represents a `greedy strategy' of injecting as much `exploration signal' $e$ into the input as possible, as opposed to targeting uncertainty reduction in specific parameters. $\phi_2$ is given by the `nominal' control. This experiment is repeated 1000 times, with the results presented in Fig. [fig:main\_res]. The greedy strategy performs slightly better during exploitation, but this cannot offset the cost of exploration, leading to worse performance in terms of total cost. Dual control balances exploration and exploitation to achieve the lowest total cost.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Numerical illustration", "weight": 1.0} -->

Costs during exploration ($t\in[1,{T_e}]$), exploitation ($t\in[{T_e},T]$), and the total cost (exploration $+$ exploitation). Costs are normalized by the cost of the nominal control (i.e. unity implies the same cost as the nominal control). Dual control exhibits best performance.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Numerical illustration", "weight": 1.0} -->

This research was financially supported by the Swedish Foundation for Strategic Research (SSF) via the project ASSEMBLE (contract number: -0012) and by the project NewLEADS - New Directions in Learning Dynamical Systems, funded by the Swedish Research Council.
