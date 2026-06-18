<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets

Topics include Partial observability, Optimal control, Robustness, Uncertainty, Control, Linear quadratic Gaussian.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The Linear Quadratic Gaussian (LQG) controller is known to be inherently fragile to model misspecifications common in real-world situations. We consider discrete-time partially observable stochastic linear systems and provide a robustification of the standard LQG against distributional uncertainties on the process and measurement noise. Our distributionally robust formulation specifies the admissible perturbations by defining a relative entropy based ambiguity set individually for each time step along a finite-horizon trajectory, and minimizes the worst-case cost across all admissible distributions. We prove that the optimal control policy is still linear, as in standard LQG, and derive a computational scheme grounded on iterative best response that provably converges to the set of saddle points. Finally, we consider the case of endogenous uncertainty captured via decision-dependent ambiguity sets and we propose an approximation scheme based on dynamic programming.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Linear Quadratic Regulator (LQG) is a cornerstone of control theory, and has been applied across several domains ranging from engineering, to economics, to computer science. It involves controlling a linear system subject to additive disturbances via the design of a control policy that minimizes a quadratic cost function. For linear systems, quadratic costs and additive Gaussian noise, it is well-known that the resulting optimal policy is linear in the observations. However, in practice, the system dynamics are often only approximately known, and the noise is not necessarily Gaussian. This leads to a mismatch between the nominal model and the true system, which can adversely affect performances.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider a generalization of the finite-horizon LQG framework for discrete-time linear stochastic systems subject to model mismatch. We interpret the problem as a zero-sum game between the controller and a distribution chosen from an ambiguity set that may change at each time step. Each ambiguity set is represented as a ball defined in the Kullback-Leibler (KL) divergence centered at a nominal Gaussian distribution. The goal of the control designer is then to synthesize a control policy that minimizes the worst-case expected cost. We refer to this problem as the Distributionally Robust LQG (DR-LQG) problem with KL ambiguity sets.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

For the DR-LGQ problem, we show that, even under distributional ambiguity, the optimal control policy is linear in the observations, as in the standard LQG. Following we re-parametrize the control policy in terms of purified observations and propose a novel \"sandwich\" argument to show that the DR-LQG is optimally solved by a linear policy and that the worst-case distribution is still Gaussian. We show that the resulting game admits a Nash equilibrium and provide a numerical scheme based on regularized best response that converges linearly to the set of saddle points of the DR-LQG. The best responses admits closed-form expression, making the algorithm computationally attractive. We further consider the case of endogenous uncertainty captured via decision-dependent ambiguity sets, well suited to capture perturbations in the system matrices. We derive an approximated closed-form recursion based on dynamic programming, and use it within a coordinate gradient descent scheme to solve the problem with linear convergence rate guarantees. Finally, we provide numerical simulations to illustrate the effectiveness of our approaches.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Literature review", "weight": 1.0} -->

Traditionally, the optimal control of systems subject to uncertainty has been studied through the LQR/LQG theory by synthesizing policies that either minimize a quadratic functional in the state and control action pair, or the $\mathcal{H}_{2}$ norm of the system's transfer function. Motivated by the fragility of the LQG against model mismatch, several robustification approaches were suggested in the literature. For example, if the perturbation is modeled as adversarial with known finite energy bound, the $\mathcal{H}_{\infty}$ synthesis approach can be used to minimize the infinity norm of the transfer function mapping disturbances to a measurable performance metric. While stability is guaranteed under any allowable process noise signal, the $\mathcal{H}_{\infty}$ controller might result in conservative behaviors as it plans for the worst uncertainty. This motivated the development of combined $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ strategies, trying to alleviate part of the conservatism.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Literature review", "weight": 1.0} -->

A different approach is represented by risk-sensitive control that incorporates risk sensitivity into the control design task by minimizing the entropic risk measure of the cost, rather than its expected value.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Literature review", "weight": 1.0} -->

Distributional robust control (DRC) is an alternative paradigm that is gaining momentum. The DRC problem seeks a control policy that minimizes the expected cost under the worst-case noise distribution in an ambiguity set, i.e., a set of probability distributions among which we can reasonably expect to find the true noise distribution. DRC robustifies against model misspecifications in the space of probabilities. Different types of ambiguity sets have been proposed in the literature based on moment constraints, total variation distance, Wasserstein distance (or, more broadly, optimal transport distances), and $\phi -$divergences.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Literature review", "weight": 1.0} -->

In a DR-LQG problem similar to the one considered here is solved by considering ambiguity sets defined on the basis of the Wasserstein distance. Compared to, (i) we motivate the choice of the KL distance by providing interesting connections with system identification and risk measure theory, (ii) we prove optimality of the linear policies for the DR-LQG problem with KL ambiguity sets, and (iii) we provide a novel best response algorithm that exploits the availability of closed-form expressions for the best responses, unlike the gradient-based method suggested that relies on automatic differentiation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Literature review", "weight": 1.0} -->

The dynamic-programming based recursion for decision-dependent ambiguity sets, is related to the approaches and. These works address a regularized relaxed problem with a fixed penalty value in the objective function; hence, there are no guarantees that the worst-case distribution, against which the controller is hedging, belongs to the specified ambiguity set. On the contrary, our formulation addresses the exact constrained formulation. Additionally, and distributed uncertainty modeling is not considered. Finally, and the problem is solved by neglecting a crucial non-linear dependence in the optimality equations; we tackle this problem by linearizing this dependence (instead of disregarding it) with obvious advantages in terms of performances, as demonstrated in the numerical section.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Outline", "weight": 1.0} -->

In Section II we present the necessary background, while in Section III we describe the problem statement. In Section IV the theoretical properties of the DR-LQG are analyzed and in Section V a computational framework is presented. Section VI considers the case with endogenous ambiguity sets, while in Section VII simulation results are reported. Finally, we draw our conclusions in Section VIII. We relegate all proofs to the appendix.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Relative entropy ambiguity sets", "weight": 1.0} -->

We do not differentiate between ${\mathbb{P}}_{i}$ and its density $p_{i}{(x)}$ in the following, when clear from the context.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Convex optimization", "weight": 1.0} -->

Finally, we recall some results from convex optimization.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem setup", "weight": 1.0} -->

Consider a discrete-time stochastic linear system

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem setup", "weight": 1.0} -->

where $\mathcal{B}$ is an ambiguity set is defined as

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem setup", "weight": 1.0} -->

for user-defined ${\rho_{x_{0}},\rho_{w_{t}},\rho_{v_{t}}} \geq 0$. Note that by construction all exogenous random variables $x_{0},w_{0},\ldots,w_{T - 1},v_{0},\ldots,v_{T - 1}$ are mutually independent under every distribution in $\mathcal{B}$. The restriction to zero-mean distributions, both in the nominal and in the perturbed distributions, is done to simplify the presentation; the results can be extended to the case of non-zero mean distributions with minor modifications. Note also that the DR-LQG problem constitutes a zero-sum game between the control policy and a fictitious adversary that selects $\mathcal{B}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A On the choice of the KL-divergence", "weight": 1.0} -->

We briefly review some benefits of the use of KL divergence to define ambiguity sets.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A On the choice of the KL-divergence", "weight": 1.0} -->

Connection with system identification. Consider the problem of estimating the parameters $\theta = {(A,B,C)}$ of a linear system of the form from noisy input-output data $\{{(u_{t},y_{t})}\}$. One of the most widely used paradigms to accomplish this task is maximum likelihood estimation (MLE), where the log-likelihood $\mathcal{L}{(\theta)}$ is maximized with respect to $\theta$. provides an attractive interpretation of the MLE problem as the search for a model that minimizes the KL-divergence to the true system. Building on this interpretation, we can directly employ $\mathcal{L}{(\theta^{\star})}$ to provide a meaningful estimate of the size of the KL ambiguity sets.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A On the choice of the KL-divergence", "weight": 1.0} -->

Connection with risk measures. For $p \in {\lbrack 1,\infty)}$, let $\mathcal{L}_{p}{(\Omega,\mathcal{F},{\mathbb{P}})}$ be the space of random variables $\xi:{\Omega\rightarrow{\mathbb{R}}}$ with finite $p -$th moment with respect to the measure $\mathbb{P}$. Then, a risk measure $\rho{(\xi)}$ with $\rho:{{\mathcal{L}_{p}{(\Omega,\mathcal{F},{\mathbb{P}})}}\rightarrow{{\mathbb{R}} \cup {\{\infty\}}}}$ is a mapping that maps $\xi$ to the extended real line, quantifying its \"riskiness\".

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A On the choice of the KL-divergence", "weight": 1.0} -->

Originating in economics, risk measures are now popular in the control community to allow for a systematic approach to risk assessment (e.g., for safety-critical systems). Among them, the class of coherent risk measures is the most widespread thanks to their appealing properties \[, Chapter 6, p.231\]. Exploiting the Fenchel-Moreau theorem, it is possible to show that any coherent risk measure can be written as

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A On the choice of the KL-divergence", "weight": 1.0} -->

where $\mathcal{A}$ is a set of probability density functions, and the measure $\mathbb{Q}$ is such that ${\mathbb{Q}}\operatorname{<<}{\mathbb{P}}$. This provides a clear connection with distributionally robust optimization with KL-based ambiguity sets.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Example 1 (Conditional Value at Risk)", "weight": 1.0} -->

The CVaR of level $\beta \in {}$ can be described as in

<!-- chunk {"id": "body-0023", "role": "body", "section": "Example 1 (Conditional Value at Risk)", "weight": 1.0} -->

since ${\int{q{(x)}{dx}}} = 1$. Consider now the LQG functional, and assume that instead of the expectation we want to consider the CVaR as we are interested in accounting for the tail-risk. Then, the cost functional becomes

<!-- chunk {"id": "body-0024", "role": "body", "section": "Example 1 (Conditional Value at Risk)", "weight": 1.0} -->

where for the second line we borrow the stacked notation from the upcoming Section IV, and the system evolves as. For $\xi = {{\mathbf{u}^{\top}{\mathbf{R}\mathbf{u}}} + {\mathbf{x}^{\top}{\mathbf{Q}\mathbf{x}}}}$, we then conclude that $\sup_{{\mathbb{Q}} \in \mathcal{B}_{\rho}}{{\mathbb{E}}_{\mathbb{Q}}{\lbrack\xi\rbrack}}$, with $\rho = {\log\left( \frac{1}{\beta} \right)}$, represents a conservative approximation of ). While solving ) is challenging, we will show that can be solved effectively, thus paving the way for novel risk-aware formulations as. $\bigtriangleup$

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-A Problem re-parametrization", "weight": 1.0} -->

As pointed out, in the LQG formulation the inputs are subject to a cyclic dependence, which makes the analysis of hard. To break this dependency, we proceed as and introduce a \"fictitious\" noise-free system

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-A Problem re-parametrization", "weight": 1.0} -->

In the remainder, we will then focus without loss of generality on the re-parametrized problem $(P)$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-B Analysis of the upper bound", "weight": 1.0} -->

where $\overset{\sim}{\mathcal{B}}$ is an ambiguity set (to be defined next) such that $\mathcal{B} \subseteq \overset{\sim}{\mathcal{B}}$, and $\mathcal{U}_{\mathbf{η}}^{\text{lin}}$ denotes the class of affine policies of the form $\mathbf{u} = {{\mathbf{U}{\mathbf{η}}} + \mathbf{q}}$ with $\mathbf{U} \in {\mathbb{R}}^{{{mT} \times p}T}$ being block lower triangular to enforce causality and $\mathbf{q} \in {\mathbb{R}}^{mT}$. Clearly, $(U)$ is an upper bound to $(P)$ since we are simultaneously restricting the feasible space of the controller, while enlarging the one of the adversary. We begin by defining $\overset{\sim}{\mathcal{B}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-C Analysis of the lower bound", "weight": 1.0} -->

Note that $\mathcal{G}$ only contains Gaussian distributions, hence $\mathcal{G} \subseteq \mathcal{B}$ and $(L)$ is a lower bound for $(P)$. Moreover, notice that for any ${\mathbb{P}} \in \mathcal{G}$, from classical LQG theory, the optimal policy is affine in the observations so we can rewrite $(L)$ as

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-C Analysis of the lower bound", "weight": 1.0} -->

Invoking, the lower bound $(L)$ becomes

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-D Optimality of linear policies", "weight": 1.0} -->

The analysis of the upper and lower bounds culminates with the following result, which represents our first contribution.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Computational framework for the DR-LQG", "weight": 1.0} -->

In search of methods for computing the optimal $u^{\star}$ and ${\mathbb{P}}^{\star}$, we start by showing that problem $(L)$ admits a Nash equilibrium. Then we devise a best response algorithm that provably converges to te set of saddle points of. Note that from the structure of (U) and (L), we directly infer that $\mathbf{q}^{\star} = \mathbf{0}$ when the nominal distribution is zero-mean. To simplify the results presentation, we will drop $\mathbf{q}$ in the remainder. All our results can be easily extended to the case of non-zero mean distributions, e.g., $\mathbf{q}^{\star} \neq \mathbf{0}$ with minor modifications.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-A Existence of a Nash equilibrium", "weight": 1.0} -->

Consider problem and its dual

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-A Existence of a Nash equilibrium", "weight": 1.0} -->

The next result shows that strong duality among the two problems holds.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-B Regularized best response scheme", "weight": 1.0} -->

Let us introduce the best response (BR) correspondences

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-B Regularized best response scheme", "weight": 1.0} -->

Before proceeding, we show that (18a) is equivalently obtained by restricting $\mathbf{U}$ to live in a compact set $\mathcal{S} \subseteq {\mathbb{R}}^{{{mT} \times p}T}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "DR-LQG with endogenous ambiguity sets", "weight": 1.0} -->

The problem formulation considered up to here assumes exogenous disturbances resulting in ambiguity sets that are defined a priori, i.e., before the control task, and are not influenced by the controller's actions. In this section, we extend the results to the case where the ambiguity sets are endogenously determined by the controller's actions.

<!-- chunk {"id": "body-0037", "role": "body", "section": "DR-LQG with endogenous ambiguity sets", "weight": 1.0} -->

Consider the standard Linear Fractional Transformation (LFT) model in Fig.: the source of uncertainty in the system dynamics, represented by the uncertainty operator $\Delta$ that is assumed to be unknown but of bounded magnitude, might depend on the system states and inputs. Consequently, to adequately represent the distributional ambiguity affecting the system, we shall resort to a state and decision-dependent ambiguity set of the form

<!-- chunk {"id": "body-0038", "role": "body", "section": "DR-LQG with endogenous ambiguity sets", "weight": 1.0} -->

While the theoretical analysis of Section IV carries over, the convergence of the best response dynamics in is no longer guaranteed, since the endogenous disturbance introduces a coupling among the feasible sets of the players. Thus, Theorem does no longer necessarily hold.

<!-- chunk {"id": "body-0039", "role": "body", "section": "DR-LQG with endogenous ambiguity sets", "weight": 1.0} -->

To overcome this issue, we devise a different approximated scheme that retain convergence guarantees despite the additional complexity introduced by the endogenous ambiguity sets. Differently from the previous sections, this approximated scheme is grounded on standard tools from dynamic programming. In this sense, the approach used here is therefore more closely related to.

<!-- chunk {"id": "body-0040", "role": "body", "section": "VI-A Relaxed problem", "weight": 1.0} -->

To simplify the derivation, in this section we only consider distributional ambiguity on the process noise $w_{t}$, while ${\mathbb{P}}_{x_{0}},{\mathbb{P}}_{v_{t}}$ are assumed to be known and equal to the their nominal distributions, i.e., we set ${\rho_{x_{0}} = \rho_{v_{t}} = 0},{\forall t}$. Let us denote the information collected up to time $t$ as

<!-- chunk {"id": "body-0041", "role": "body", "section": "VI-A Relaxed problem", "weight": 1.0} -->

with $I_{0} = y_{0}$, and we call it the information vector. When a new control action is computed, the information vector is updated as ${I_{t + 1} = {(I_{t},y_{t + 1},u_{t})}}.$ It is well-known in stochastic optimal control theory that $I_{t}$ serves as sufficient statistics.

<!-- chunk {"id": "body-0042", "role": "body", "section": "VI-A Relaxed problem", "weight": 1.0} -->

We begin by focusing on a relaxed version of Problem where, instead of constraining the adversary to select a distribution from the ambiguity sets ${\{{\mathcal{B}_{t}{(x_{t},u_{t})}}\}}_{t = 0}^{T - 1}$, we simply penalize the deviation of the distributions ${\mathbb{P}}_{w_{t}}$ from their nominal ones. In other words, we focus on the relaxed regularized problem. Let us use for brevity $R{({\mathbb{P}}||{\mathbb{Q}}_{t})} \equiv \mathcal{R}_{t}$. The relaxed problem reads

<!-- chunk {"id": "body-0043", "role": "body", "section": "VI-A Relaxed problem", "weight": 1.0} -->

for fixed ${\{\tau_{t}\}}_{t = 0}^{N}$ with $\tau_{t} \in {\mathbb{R}}_{+}$. We address by resorting to the dynamic programming technique. To this end, we derive the following instrumental result.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 1 (On approximating $r_{t}{(\\Sigma_{t})}$)", "weight": 1.0} -->

The non-linear dependence of $r_{t}$ on $\Sigma_{t}$ is also present in other distributionally robust control formulations, such as the data-driven Wasserstein-based approach discussed. In the search for closed-form recursions, disregard such dependence. Conversely, we account for it via a suitable approximation, while retaining tractability. For completeness, we show the benefits of our formulation compared to the one in in Appendix E on a simplified setting amenable to both algorithms. Finally, we notice that other linear approximation of $r_{t}{(\Sigma_{t})}$ are possible; for example, one can consider ${{\overline{\overline{r}}}_{t}{(X)}} = {\frac{1}{2}{{Tr}\left( {S_{t + 1}AXA^{\top}} \right)}}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "VI-B Constrained problem", "weight": 1.0} -->

Next, we extend the results of Subsection VI-A to the constrained minimax Problem resorting to the Lagrange duality theory. Let $\tau = {(\tau_{0},\ldots,\tau_{T - 1})}$ be the Lagrangian multipliers vector; the dual problem associated to is^44^4Contrary to Subsection VI-A, we will consider optimizing over $\tau$, hence we use the notation $\mathcal{V}_{t}{(I_{t},\tau)}$ to emphasize such dependence.

<!-- chunk {"id": "body-0046", "role": "body", "section": "VI-B Constrained problem", "weight": 1.0} -->

where the equivalence follows. We consider the linearized dual problem

<!-- chunk {"id": "body-0047", "role": "body", "section": "VI-B Constrained problem", "weight": 1.0} -->

Consider the coordinate gradient descent scheme, where at each iteration $t \in {\mathbb{N}}$ we update each $i$-th component of the vector $\tau$ sequentially^55^5One might also randomly select the order of the updates at each iteration $t$ rather than considering a cyclic pattern. Randomized updates might enhance numerical stability. for $i = {\{ 0,\ldots,{T - 1}\}}$ by solving the one-dimensional subproblem

<!-- chunk {"id": "body-0048", "role": "body", "section": "VI-B Constrained problem", "weight": 1.0} -->

The overall procedure to solve is summarized in Algorithm 1. We get the following result.

<!-- chunk {"id": "body-0049", "role": "body", "section": "VII-A Example 1", "weight": 1.0} -->

We set the radii to be $\rho_{x_{0}} = \rho_{w_{t}} = \rho_{v_{t}} = 1$ and the nominal covariances to ${\hat{W}}_{t} = {0.001I_{2}}$, ${\hat{V}}_{t} = 0.001$ for all times $t$, and $W_{- 1} = 0_{2}$. We set ${Q = I_{2}},{{Q_{t} = {10I_{2}}},{R = 0.1}}$, $T = 20$, and $\hat{x_{0}} = {\lbrack 0,0\rbrack}^{\top}$. We implement the iterative best response dynamics in in Python 3.8.6 using the Scipy package and the ODE solver. Fig. shows the empirical convergence behavior of the best response dynamics, confirming the exponential convergence rate from Theorem.

<!-- chunk {"id": "body-0050", "role": "body", "section": "VII-A Example 1", "weight": 1.0} -->

The DR-LQG controller was benchmarked against a standard LQG based on the nominal distributions. We carried out 5000 Montecarlo simulations with exogenous disturbances distributed according to the true distributions ${\mathbb{P}}_{x_{0}},{\mathbb{P}}_{w_{t}},{\mathbb{P}}_{v_{t}}$ selected randomly from the ambiguity sets. The DR-LQG controller led to an average cost across the Montecarlo run of 0.6287 and a standard deviation of 0.7125, while the standard LQG led to an average cost of 0.6587 and a standard deviation of 0.7588. The results confirm the effectiveness of the proposed approach to provide robustification against distributional ambiguity.

<!-- chunk {"id": "body-0051", "role": "body", "section": "VII-B Example 2", "weight": 1.0} -->

We show the benefits of our DR-LQG controller with endogenous ambiguity sets. Consider the linear model with

<!-- chunk {"id": "body-0052", "role": "body", "section": "VII-B Example 2", "weight": 1.0} -->

We assume that, for all $t$, $w_{t}$ follows a Gaussian distribution with zero-mean and nominal covariance

<!-- chunk {"id": "body-0053", "role": "body", "section": "VII-B Example 2", "weight": 1.0} -->

and ${R = {10^{- 3}I}}.$ We assume that the matrix $A$ contains some uncertainty and that the real underlying system evolves with a dynamics matrix $\overset{\sim}{A} = {A + {\DeltaA}}$ where

<!-- chunk {"id": "body-0054", "role": "body", "section": "VII-B Example 2", "weight": 1.0} -->

and ${\rho_{t} = 10^{- 5}}.$ We compare our controller, which we term D^2^O-LQG controller, with the standard LQG controller. Additionally, we consider the DRC controller with a single relative-entropy constraint (D-LQG), using ${\rho = {\sum_{t = 0}^{T - 1}\rho_{t}}}.$ We consider two scenarios: (i) Nominal scenario, with ${\DeltaA} = 0$; (ii) Perturbed scenario, with $a = 0.03$ and ${b = 0.02}.$ The results of the simulations are summarized in Figg. and. The standard LQG technique is not able to stabilize the system in the perturbed scenario, causing the cost index to increase dramatically. The D-LQG controller with a single constraint has not a satisfactory behaviour: this is due to the fact that the maximizing player is allowed to allocate most of the mismatch budget to few (or even one) time intervals.

<!-- chunk {"id": "body-0055", "role": "body", "section": "VII-B Example 2", "weight": 1.0} -->

On the other hands, D^2^O-LQG control in able to trade off optimality and robustness. In the nominal scenario the average closed-loop cost is slightly larger than the pure LQG optimum. This cost remains almost constant when ${{\DeltaA} \neq 0},$ giving evidence to the robustness properties of the control system.

<!-- chunk {"id": "body-0056", "role": "body", "section": "VII-C Example 3", "weight": 1.0} -->

In the last example, we aim to show that the scheme proposed in Section VI outperforms the one based on the Wasserstein distance. As does not directly handle decision-dependent ambiguity sets, we consider a simplified setting with exogenous uncertainty and adapt the recursions in Proposition accordingly by setting $E_{1} = E_{2} = 0$. We consider a building temperature control problem using a state-space model borrowed and affected by uncertainty in the ambient temperature $T_{t}^{a} \sim {\mathcal{N}{({{\overline{T}}_{t}^{a} + {\hat{\mu}}_{t}},{\hat{W}}_{t})}}$^66^6The recursions in this case are slightly different; but can be easilly derived using the same reasoning as in Proposition..

<!-- chunk {"id": "body-0057", "role": "body", "section": "VII-C Example 3", "weight": 1.0} -->

To fit the building temperature control problem into the presented framework, we define the error state $e_{t} = {x_{t} - r}$ and consider the error dynamics

<!-- chunk {"id": "body-0058", "role": "body", "section": "VII-C Example 3", "weight": 1.0} -->

For the sake of the simulation, we set the uncertainty budget $\rho_{t}$ a-posteriori based on the knowledge of the true process noise distribution, considering $d_{t} = {1.1\mathcal{R}_{t}}$ where $\mathcal{R}_{t}$ is the relative entropy between the nominal and the true distribution at time $t$. We compare the proposed D^2^O-LQG controller with the standard LQG controller and the DRC controller with a constant distributional ambiguity budget $\theta$ per each time step proposed ^77^7We use the public code from the authors accessible at (W-DRC). As before, we set $\theta = {\frac{1}{N}{\sum_{t = 0}^{N - 1}{({1.1d_{t}^{\text{W}}})}}}$, where $d_{t}^{\text{W}}$ is the a-posteriori Wasserstein distance between the true and the nominal distribution. Results are summarized in Fig..

<!-- chunk {"id": "body-0059", "role": "body", "section": "VII-C Example 3", "weight": 1.0} -->

Again, the standard LQG controller does not offer any robustness against model misspecification; thus, its performance rapidly deteriorates in the presence of distributional ambiguity. On the other hand, while the W-DRC controller offers a degree of robustness, its practical performance is hindered by the requirement for the same ambiguity set size (e.g., the same $\theta$) throughout the entire control task.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusions", "weight": 1.0} -->

For discrete-time stochastic linear systems, we propose an output feedback controller capable of robustifying the standard LQG approach against distributional ambiguity affecting both process and measurement noise by relying on KL ambiguity sets. Our analysis shows that linear policies are still optimal despite the added complexity; moreover, the worst-case distribution is still a Gaussian. These insights led us to design an iterated best response dyanmics scheme that provably convergences to the set of saddle points and admits closed-form expressions. Further, we consider the case of decision-dependent ambiguity sets to capture model perturbations. For this setting, we devise a tailored approximated recursive scheme based on dynamic programming and coordinate gradient descent.
