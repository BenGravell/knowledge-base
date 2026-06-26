<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Wasserstein Distributionally Robust Stochastic Control: A Data-Driven Approach

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Standard stochastic control methods assume that the probability distribution of uncertain variables is available. Unfortunately, in practice, obtaining accurate distribution information is a challenging task. To resolve this issue, we investigate the problem of designing a control policy that is robust against errors in the empirical distribution obtained from data. This problem can be formulated as a two-player zero-sum dynamic game problem, where the action space of the adversarial player is a Wasserstein ball centered at the empirical distribution. We propose computationally tractable value and policy iteration algorithms with explicit estimates of the number of iterations required for constructing an epsilon-optimal policy. We show that the contraction property of associated Bellman operators extends a single-stage out-of-sample performance guarantee, obtained using a measure concentration inequality, to the corresponding multi-stage guarantee without any degradation in the confidence level. In addition, we characterize an explicit form of the optimal distributionally robust control policy and the worst-case distribution policy for linear-quadratic problems with Wasserstein penalty. Our study indicates that dynamic programming and Kantorovich duality play a critical role in solving and analyzing the Wasserstein distributionally robust stochastic control problems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The theory of stochastic optimal control is based on the assumption that the probability distribution of uncertain variables (e.g., disturbances) is fully known. However, this assumption is often restrictive in practice, because estimating an accurate distribution requires large-scale high-resolution sensor measurements over a long training period or multiple periods. Situations in which uncertain variables are not directly observed are much more challenging; computational methods, such as filtering or statistical learning techniques, are often used to obtain the (posterior) distribution of the uncertain variables given limited observations. The accuracy of the obtained distribution is often unsatisfactory, as it is subject to the quality of the collected data, computational methods, and prior knowledge regarding the variables. If poor distributional information is employed in constructing a stochastic optimal controller, it does not guarantee optimality and can even cause catastrophic system behaviors (e.g., ).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

To overcome this issue of limited distribution information in stochastic control, we investigate a *distributionally robust control* approach. This emerging minimax stochastic control method minimizes a cost function of interest, assuming that the distribution of uncertain variables is not completely known, but is contained in a pre-specified *ambiguity set* of probability distributions. In this paper, we model the ambiguity set as a statistical ball centered at an empirical distribution with a radius measured by the *Wasserstein metric*. This modeling approach provides a straightforward means to incorporate data samples into distributionally robust control problems. Our focus is to show that the resulting stochastic control problems have several salient features in terms of computational tractability and out-of-sample performance guarantee.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Due to its superior statistical properties, the Wasserstein ambiguity set has recently received a great deal of attention in distributionally robust optimization (e.g., ), learning (e.g., ) and filtering. Specifically, the Wasserstein ball contains both continuous and discrete distributions while statistical balls with the $\phi$-divergence such as the Kullback-Leibler divergence centered at a discrete empirical distribution is not sufficiently rich to contain relevant continuous distributions. Furthermore, the Wasserstein metric addresses the closeness between two points in the support, unlike the $\phi$-divergence. Due to the incapability of the $\phi$-divergence in terms of taking into account the distance between two support elements, the associated ambiguity set may contain irrelevant distributions. For these reasons, we chose the Wasserstein metric to handle distribution ambiguity, although several other types of ambiguity sets have been proposed in the context of single-stage optimization by using moment constraints (e.g., ), confidence sets (e.g., ), and the $\phi$-divergences (e.g., ).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Contributions", "weight": 1.0} -->

Departing from the aforementioned control approaches that indirectly use data samples, we consider *continuous-state* distributionally robust control problems with Wasserstein ambiguity sets and develop a dynamic programming method to solve and analyze problems by directly using the data. The following is a summary of the main contributions of this work. First, we propose computationally tractable value and policy iteration algorithms with explicit estimates of the number of iterations necessary for obtaining an $\epsilon$-optimal policy. The original Bellman equation involves an infinite-dimensional minimax optimization problem, where the inner maximization problem is over probability measures in the Wasserstein ball. To alleviate the computational issue without sacrificing optimality, we reformulate Bellman operators by using modern DRO based on Kantorovich duality. Second, we show that the resulting distributionally robust policy $\pi^{\star}$ has a probabilistic *out-of-sample performance guarantee* by using the contraction property of associated Bellman operators and a measure concentration inequality.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contributions", "weight": 1.0} -->

In other words, when $\pi^{\star}$ is used, a probabilistic bound holds on the closed-loop performance evaluated under a new set of samples that are selected independently of the training data. We observe that the contraction property of the Bellman operator seamlessly connects a single-stage performance guarantee to its multi-stage counterpart in a manner that is independent of the number of stages. Third, we consider a Wasserstein penalty problem and derive an explicit expression of the optimal control policy and the worst-case distribution policy, along with a Riccati-type equation in the linear-quadratic setting. We also show that the resulting control policy converges to the optimal policy of the corresponding linear-quadratic-Gaussian (LQG) problem as the penalty parameter tends to $+ \infty$. The performance and utility of the proposed method are demonstrated through an investment-consumption problem and a power system frequency control problem.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

This paper is significantly extended from its preliminary version, which models distribution ambiguity by using confidence sets. Specifically, we consider Wasserstein ambiguity sets and investigate new salient features of the corresponding distributionally robust control framework such as $(i)$ a characterization of the worst-case distribution policy, $({ii})$ an out-of-sample performance guarantee, and $({iii})$ an explicit expression of the solution to linear-quadratic problems.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Organization", "weight": 1.0} -->

In Section 2, we define optimal distributionally robust policies under ambiguous uncertainty and formulate the corresponding distributionally robust stochastic control problem as a dynamic game. In Section 3, we develop a tractable semi-infinite program formulation of the Bellman equation and characterize one of the worst-case distribution policies by using Kantorovich duality. In Section 4, we examine a probabilistic out-of-sample performance guarantee of the distributionally robust policy. In Section 5, we present the Wasserstein penalty problem and its explicit solution obtained from a Riccati-type solution. Finally, in Section 6, we provide the results of our numerical experiments.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Ambiguity in Stochastic Systems", "weight": 1.0} -->

Consider a discrete-time stochastic system of the form where $x_{t} \in \mathcal{X} \subseteq {\mathbb{R}}^{n}$ and $u_{t} \in \mathcal{U} \subseteq {\mathbb{R}}^{m}$ denote the system state and control input, respectively. Here, $w_{t} \in \mathcal{W} \subseteq {\mathbb{R}}^{l}$ is a random disturbance. The probability distribution of $w_{t}$ is denoted by $\mu_{t}$. However, in practice, the probability distribution is not fully known and is difficult to estimate accurately. We assume that $\mathcal{X}$, $\mathcal{U}$ and $\mathcal{W}$ are Borel subsets of ${\mathbb{R}}^{n}$, ${\mathbb{R}}^{m}$ and ${\mathbb{R}}^{l}$, respectively.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Ambiguity in Stochastic Systems", "weight": 1.0} -->

Suppose that $w_{t}$'s are i.i.d. and that we have access to the sample $\{{\hat{w}}^{},\ldots,{\hat{w}}^{(N)}\}$ of $w_{t}$. One of the most straightforward approaches is to use the sample average approximation (SAA) method and solve the corresponding optimal control problem with the empirical distribution. This SAA-control problem can be formulated as where $\nu_{N}$ denotes the empirical distribution constructed from the $N$-samples: with the Dirac delta measure $\delta_{{\hat{w}}^{(i)}}$ concentrated at ${\hat{w}}^{(i)}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Ambiguity in Stochastic Systems", "weight": 1.0} -->

Here, $\alpha \in {}$ is a discount factor, $c:{{\mathcal{X} \times \mathcal{U}}\rightarrow{\mathbb{R}}}$ is a stage-wise cost function of interest, and ${\mathbb{E}}_{w_{t} \sim \nu_{N}}^{\pi}$ denotes the expected value taken with respect to the probability measure induced by the control policy $\pi$ and the empirical distribution $\nu$. As the number of samples, $N$, tends to infinity, the empirical distribution $\nu$ well approximates the true distribution $\mu$; thus, an optimal policy of the SAA-control problem presents a near-optimal performance.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Ambiguity in Stochastic Systems", "weight": 1.0} -->

Unfortunately, it takes a long simulation period or multiple episodes to obtain a large number of samples. Furthermore, in practice, it is likely that the sample data do not reflect the true distribution due to inaccurate sensor measurements or data corruption by malicious attackers (e.g., hackers). To resolve these issues in data-driven stochastic control, we propose an optimization method to construct a policy that is robust against errors in the empirical distribution (2.3). More specifically, our policy minimizes the *worst-case* total cost that is calculated under a probability distribution contained in a given set $\mathcal{D} \subset {\mathcal{P}{(\mathcal{W})}}$, which is called the *ambiguity set* of probability distributions. The ambiguity set can be designed to adequately characterize errors in the empirical distribution.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Distributionally Robust Policy", "weight": 1.0} -->

To formulate a concrete distributionally robust control problem, we consider a *Markov (or stochastic) game with complete information* (e.g., ), which is a class of two-player zero-sum dynamic games: Player I (controller) determines a policy to minimize the total cost while Player II (adversary) selects the disturbance distribution $\mu_{t}$ of $w_{t}$ from the ambiguity set $\mathcal{D}$ to maximize the same cost value.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Distributionally Robust Policy", "weight": 1.0} -->

Let $H_{t}$ be the set of *histories* up to stage $t$, whose element is of the form $h_{t}:={(x_{0},u_{0},\cdots,x_{t - 1},u_{t - 1},x_{t})}$.^11^1All the results in this paper are valid with histories of the form ${\overset{\sim}{h}}_{t}:={(x_{0},u_{0},w_{0},\mu_{0},\cdots,x_{t - 1},u_{t - 1},w_{t - 1},\mu_{t - 1},x_{t})}$ that also contains Player II's actions $(\mu_{0},\cdots,\mu_{t - 1})$; that is because under Assumption 1, without loss of optimality, it suffices to focus on stationary policies that depend only on current state information.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Distributionally Robust Policy", "weight": 1.0} -->

We intentionally use the reduced version of histories, as the realized distributions may not be observable in practice. The set of admissible control strategies (for Player I) is given by $\Pi:=\left. \{{\pi:={(\pi_{0},\pi_{1},\ldots)}} \middle| {{\pi_{t}{(\left. {\mathcal{U}{(x_{t})}} \middle| h_{t} \right.)}} = {1{\forall h_{t}}} \in H_{t}}\} \right.$, where $\pi_{t}$ is a stochastic kernel from $H_{t}$ to ${\mathbb{R}}^{m}$ and ${\mathcal{U}{(x_{t})}} \subseteq \mathcal{U}$ is the set of admissible control actions (given that the system state is $x_{t}$ at stage $t$).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Distributionally Robust Policy", "weight": 1.0} -->

Similarly, the set of Player II's admissible strategies is defined by $\Gamma:=\left. \{{\gamma:={(\gamma_{0},\gamma_{1},\ldots)}} \middle| {{\gamma_{t}{(\left.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Distributionally Robust Policy", "weight": 1.0} -->

Here, we allow Player II can change the distribution of $w_{t}$ over time. Thus, the strategy space for Player II is larger than necessary, and this gives an advantage to the adversary. However, later we will show that an optimal policy of Player II is stationary under some assumption (see Proposition 5. ‣ 3.4 The Worst-Case Distribution Policy ‣ 3 Dynamic Programming Solution and Analysis ‣ Wasserstein Distributionally Robust Stochastic Control: A Data-Driven Approach")).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Distributionally Robust Policy", "weight": 1.0} -->

We consider the following infinite-horizon discounted cost function: where ${\mathbb{E}}^{\pi,\gamma}$ denotes expectation with respect to the probability measure induced by the strategy pair ${(\pi,\gamma)} \in {\Pi \times \Gamma}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The first condition trivially holds when $c$ is bounded. In fact, $\xi$ is a weight function introduced to relax the boundedness assumption. Assumption 1 ensures the existence of an optimal policy $\pi^{\star}$, which is deterministic and stationary, of a minimax control problem with the cost function (2.6) \[19, Theorem 4.1\]. Furthermore, the corresponding optimal value function lies in ${\mathbb{B}}_{lsc}{(\mathcal{X})}$ as discussed later.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Wasserstein Ambiguity Set", "weight": 1.0} -->

To complete the formulation of the DR-control problem, we consider a specific class of ambiguity sets using the Wasserstein metric. Let $\mathcal{D}$ be a statistical ball centered at the empirical distribution $\nu_{N}$ defined by (2.3) with radius $\theta > 0$: Here, the distance between the two probability distributions is measured by the Wasserstein metric of order $p \in {\lbrack 1,\infty)}$, where $d$ is a metric on $\mathcal{W}$, and $\Pi^{i}\kappa$ denotes the $i$th marginal of $\kappa$ for $i = {1,2}$. The Wasserstein distance between two probability distributions represents the minimum cost of transporting or redistributing mass from one to another via non-uniform perturbation, and the optimization variable $\kappa$ can be interpreted as a transport plan.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Wasserstein Ambiguity Set", "weight": 1.0} -->

The minimization problem to identify an optimal transport plan $\kappa$ in (2.8) is called the *Monge-Kantorovich problem*. The minimum of this problem can be found by solving the following dual problem: where $\Phi:={\{{{(\varphi,\psi)} \in {{{L^{1}{({d\mu})}} \times L^{1}}{({d\nu_{N}})}}}\mid{{{{\varphi{(w)}} + {\psi{(w')}}} \leq {d{(w,w')}^{p}{\forall w}}},{w' \in \mathcal{W}}}\}}$. This equivalence is known as the *Kantorovich duality principle*. Then, the Wasserstein ball (2.8)

<!-- chunk {"id": "body-0023", "role": "body", "section": "Dynamic Programming Solution and Analysis", "weight": 1.0} -->

Our first goal is to develop a computationally tractable dynamic programming (DP) solution for the DR-control problem (2.6). We begin by characterizing an optimality condition using the Bellman's principle.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Bellman's Principle of Optimality", "weight": 1.0} -->

For any $v \in {{\mathbb{B}}_{\xi}{(\mathcal{X})}}$, let $T$ be the Bellman operator of the DR-control problem (2.6), defined by for every ${\mathbf{x}} \in \mathcal{X}$. Assumption 1 enables us to conduct the contraction analysis with respect to the weighted sup-norm $\parallel \cdot \parallel_{\xi}$ defined by The second and third conditions in Assumption 1 play a critical role in preserving the lower semicontinuity of the value function when applying the Bellman operator as well as in the existence and optimality of deterministic stationary policies.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Value Iteration", "weight": 1.0} -->

To compute the optimal value function $v^{\star}$, we first consider a *value iteration* (VI) approach, $v_{k + 1}:={Tv_{k}}$, where $v_{k}$ denotes the value function evaluated at the $k$th iteration and $v_{0}$ is initialized as an arbitrary function in ${\mathbb{B}}_{lsc}{(\mathcal{X})}$. By the contraction property of $T$ (Lemma 2. ‣ 3.1 Bellman’s Principle of Optimality ‣ 3 Dynamic Programming Solution and Analysis ‣ Wasserstein Distributionally Robust Stochastic Control: A Data-Driven Approach")), the Banach fixed-point theorem implies that $v_{k}$ converges to $v^{\star}$ pointwise as $k$ tends to $\infty$ under Assumption 1. However, this approach requires us to solve the infinite-dimensional minimax optimization problem in the Bellman operator for each ${\mathbf{x}} \in \mathcal{X}$ in each iteration.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Value Iteration", "weight": 1.0} -->

To alleviate this issue, we reformulate the problem into a computationally tractable form by using modern Wasserstein DRO.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Policy Iteration", "weight": 1.0} -->

*Policy iteration* (PI) is an alternative way to construct an $\epsilon$-optimal policy. The PI algorithm can be described as follows: Initialize $\pi_{0}$ as an arbitrary policy in $\Pi^{DS}$, and set $k:=0$; (Policy evaluation) Find the fixed point $v^{\pi_{k}}$ of $T^{\pi_{k}}$; (Policy improvement) For each ${\mathbf{x}} \in \mathcal{X}$, set where $\overset{\sim}{\mathbf{u}}$ is an optimal $\mathbf{u}$ of the semi-infinite program (3.2) that computes ${({Tv^{\pi_{k}}})}{({\mathbf{x}})}$; If the stopping criterion is met, then stop and set $\overset{\sim}{\pi}:=\pi_{k + 1}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Policy Iteration", "weight": 1.0} -->

Otherwise, set $k\leftarrow{k + 1}$ and go to Step 2); Here, the stopping criterion can be chosen as ${\|{v^{\pi_{k}} - v^{\pi_{k - 1}}}\|}_{\xi} < \delta$ for a positive constant $\delta$. To perform the policy evaluation step (Step 2) in a computationally tractable manner, we reformulate the infinite-dimensional maximization problem in the definition of $T^{\pi}$ as finite dimensional by using Wasserstein DRO.

<!-- chunk {"id": "body-0029", "role": "body", "section": "The Worst-Case Distribution Policy", "weight": 1.0} -->

Given a policy $\pi \in \Pi^{DS}$ (for Player I), the worst-case distribution policy (for Player II) can be found by solving which is an optimal control problem. By the dynamic programming principle, the worst-case value function $v^{\pi}$, defined by (3.3), is the unique solution to the following Bellman equation: under Assumption 1. The worst-case value function $v^{\pi}$ can be computed, for example, via value iteration. *Given $v^{\pi}$, how can we characterize the worst-case distribution policy?* The following proposition indicates that, if the optimization problem involved in ${({T^{\pi}v^{\pi}})}{({\mathbf{x}})}$ admits an optimal solution for all ${\mathbf{x}} \in \mathcal{X}$, then there exists an optimal policy for Player II, which is deterministic and stationary, and it generates a finitely-supported worst-case distribution.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Out-of-Sample Performance Guarantee", "weight": 1.0} -->

A potential defect of the SAA-control formulation (2.2) is that its optimal policy may not perform well if a testing dataset of $w_{t}$ is different from the training dataset $\{{\hat{w}}^{},\ldots,{\hat{w}}^{(N)}\}$. This issue occurs even when the testing and training datasets are sampled from the same distribution. Such a degradation of the optimal decisions in out-of-sample tests is often called the *optimizer's curse* in the literature of decision analysis. We show that an optimal distributionally robust policy can alleviate this issue and provide a guaranteed *out-of-sample performance* if the radius $\theta$ of Wasserstein ambiguity set is carefully determined.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Out-of-Sample Performance Guarantee", "weight": 1.0} -->

Let $\pi_{\hat{w}}^{\star} \in \Pi$ denote an optimal distributionally robust policy obtained by using the training dataset $\hat{w}:={\{{\hat{w}}^{},\ldots,{\hat{w}}^{(N)}\}}$ of $N$ samples. The out-of-sample performance of $\pi^{\star}$ is measured as which represents the expected total cost under a new sample that is generated (according to $\mu$) independent of the training dataset. Unfortunately, the out-of-sample performance cannot be precisely computed because the true distribution $\mu$ is unknown.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Out-of-Sample Performance Guarantee", "weight": 1.0} -->

Thus, instead, we aim at establishing a *probabilistic out-of-sample performance guarantee* of the form: where $v_{\hat{w}}^{\star}$ denotes the optimal value function of the DR-control problem with the training dataset $\hat{w}:={\{{\hat{w}}^{},\ldots,{\hat{w}}^{(N)}\}}$, and $\beta \in {}$.^44^4Here, $\hat{w}$, $\pi_{\hat{w}}^{\star}$ and $v_{\hat{w}}^{\star}$ are viewed as random objects. The inequality represents a bound $({1 - \beta})$ on the probability that the expected cost incurred by $\pi^{\star}$ is no greater than the optimal value function. Note that the probability and the expected cost are evaluated with respect to the true distribution $\mu$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Out-of-Sample Performance Guarantee", "weight": 1.0} -->

Thus, this inequality provides a probabilistic bound on the performance of $\pi^{\star}$ evaluated with unseen test samples drawn from $\mu$. Here, $v_{\hat{w}}^{\star}$, which depends on $\theta$, plays the role of a certificate for the out-of-sample performance.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Out-of-Sample Performance Guarantee", "weight": 1.0} -->

Our goal is to identify conditions on the radius $\theta$ under which an optimal distributionally robust policy provides the probabilistic performance guarantee.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Assumption 2 (Light tail)", "weight": 1.0} -->

There exists a positive constant $q > p$ such that This assumption implies that the tail of $\mu$ decays exponentially.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Note that the contraction property of $T$ and $T^{\star}$ plays a critical role in connecting the single-stage performance guarantee (4.4) to the multi-stage guarantee (4.2) in a way that is independent of the number of stages. This is a quite powerful result, because if we have a radius $\theta$ that provides a desirable confidence level $({1 - \beta})$ in the single-stage guarantee, we can use the same radius to achieve the same level of confidence in the multi-stage guarantee with no additional requirement.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Wasserstein Penalty Problem", "weight": 1.0} -->

We now consider a slightly different version of the DR-control problem, which can be considered as a relaxation of (2.6) with a fixed penalty parameter $\lambda > 0$: where the strategy space $\Gamma':={\{\gamma:={(\gamma_{0},\gamma_{1},\ldots)}|}$ $\gamma_{t}{(\mathcal{P}{(\mathcal{W})}|h_{t}^{e})} = 1\forall h_{t}^{e} \in H_{t}^{e}\}$ of Player II no longer depends on a Wasserstein ambiguity set. Instead of using an explicit ambiguity set $\mathcal{D}$, Player II is penalized by $\lambdaW_{p}{(\mu_{t},\nu_{N})}^{p}$, which can be interpreted as the cost of perturbing the empirical distribution $\nu_{N}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Linear-Quadratic Problem", "weight": 1.0} -->

We now develop a solution approach, using a Riccati-type equation, to linear-quadratic (LQ) problems with the Wasserstein penalty when where $\parallel \cdot \parallel$ denotes the Euclidean norm on ${\mathbb{R}}^{l}$. Consider a linear system of the form where $A \in {\mathbb{R}}^{n \times n}$, $B \in {\mathbb{R}}^{n \times m}$, and $\Xi \in {\mathbb{R}}^{n \times l}$. We also choose the following quadratic stage-wise cost function: where $Q = Q^{\top} \in {\mathbb{R}}^{n \times n}$ is positive semidefinite, and $R = R^{\top} \in {\mathbb{R}}^{m \times m}$ is positive definite.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Linear-Quadratic Problem", "weight": 1.0} -->

In the LQ setting, we also set $\mathcal{X}:={\mathbb{R}}^{n}$, ${\mathcal{U}{({\mathbf{x}})}} \equiv \mathcal{U}:={\mathbb{R}}^{m}$, and $\mathcal{W}:={\mathbb{R}}^{l}$. Note that, unlike the standard LQG, the LQ problems with Wasserstein penalty do not assume that the probability distribution of random disturbances is Gaussian. In fact, the main motivation of this distributionally robust LQ formulation is to relax the assumption of Gaussian disturbance distributions in LQG, and to obtain a useful control policy when the true distribution deviates from a Gaussian distribution.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Investment-Consumption Problem", "weight": 1.0} -->

We first demonstrate the performance and utility of DR-control through an investment-consumption problem (e.g.,). Let $x_{t}$ be the wealth of an investor at stage $t$. The investor wishes to decide the amount $u_{1,t}$ to be invested in a risky asset (with an i.i.d. random rate of return, $w_{t}$) and the amount $u_{2,t}$ to be consumed at stage $t$. The remaining amount $({x_{t} - u_{1,t} - u_{2,t}})$ is automatically re-invested into a riskless asset with a deterministic rate of return, $\eta$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Investment-Consumption Problem", "weight": 1.0} -->

The cost function is given by the following negative expected utility from consumption: where the utility function $U:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ is selected as ${U{(c)}} = {c - {\zetac^{2}}}$. The following parameters are used in the numerical simulations: $\zeta = 0.25$, $\alpha = 0.9$, $\eta = 1.02$, and $p = 1$. The data samples $\{{\hat{w}}^{},\ldots,{\hat{w}}^{(N)}\}$ of $w_{t}$ are generated according to the normal distribution $\mathcal{N}{(1.08,0.1^{2})}$. We numerically approximate the optimal value function $v_{\hat{w}}^{\star}$ and the corresponding optimal policy $\pi_{\hat{w}}^{\star}$ on a computational grid by using the convex optimization approach.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Investment-Consumption Problem", "weight": 1.0} -->

This method approximates the Bellman operator by the optimal value of a convex program with a uniform convergence property. Furthermore, it does not require any explicit interpolation in evaluating the value function and control policies at some state other than the grid points, by using an auxiliary optimization variable to assign the contribution of each grid point to the next state.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Investment-Consumption Problem", "weight": 1.0} -->

The numerical experiments were conducted on a Mac with 4.2 GHz Intel Core i7 and 64GB RAM. The amount of time required for simulations with different grid sizes and $N = 10$ are reported in TABLE 1. For the rest of the simulations, we used 71 states (with grid spacing 0.02).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Out-of-sample performance guarantee", "weight": 1.0} -->

To demonstrate the out-of-sample performance guarantee of an optimal distributionally robust policy, we compute the following *reliability* of $\pi_{\hat{w}}^{\star}$: which represents the probability that the expected cost incurred by $\pi_{\hat{w}}^{\star}$ under the true distribution $\mu$ is no greater than $v_{\hat{w}}^{\star}{({\mathbf{x}})}$. As shown in Fig. 1 (a), the reliability increases with the Wasserstein ball radius $\theta$ and the number $N$ of samples. This result is consistent with Theorem 3. ‣ 4 Out-of-Sample Performance Guarantee ‣ Wasserstein Distributionally Robust Stochastic Control: A Data-Driven Approach"). Our numerical experiments also confirm that the same radius $\theta$ can be used to achieve the same level of reliability in both single-stage and multi-stage settings as indicated in the theorem.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Out-of-sample performance guarantee", "weight": 1.0} -->

Fig. 1 (b) illustrates the out-of-sample cost (4.1) of $\pi_{\hat{w}}^{\star}$ with respect to $\theta$ and $N$. Interestingly, the out-of-sample cost does not monotonically decrease with $\theta$.^88^8This observation is consistent with the single-stage case in Section 7.2 of. For a too-small radius, the resulting DR-policy is not sufficiently robust to obtain the best out-of-sample performance (i.e., the least out-of-sample cost). On the other hand, if a too-large Wasserstein ambiguity set is selected, the resulting DR-policy is overly conservative and thus sacrifices the closed-loop performance. Thus, there exists an optimal radius (e.g., $0.02$ in the case of $N = 20$) that provides the best out-of-sample performance.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Comparison to SAA", "weight": 1.0} -->

To compare DR-control (2.6) with SAA-control (2.2), we first compute the out-of-sample performance of $\pi_{\hat{w}}^{\star}$ and that of the corresponding optimal SAA policy $\pi_{\hat{w}}^{\text{SAA}}$ obtained by using the same training dataset $\hat{w}$. The radius is selected as the one that provides the best out-of-sample performance. As shown in Fig. 2, the proposed DR-policy achieves 8% lower out-of-sample cost than the SAA-policy when $N = 10$. As expected, the gap between the two decreases with the number of samples. Note that the proposed DR-policy designed even with a small number of samples ($N = 10$) maintains its performance under the test dataset that is generated independent of the training dataset, unlike the corresponding SAA-policy.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Power System Frequency Control Problem", "weight": 1.0} -->

Consider an electric power transmission system with $N$ buses (and $\overline{n}$ generator buses). This system may be subject to ambiguous uncertainty generated from variable renewable energy sources such as wind and solar. For the frequency regulation of this system, we use the proposed Wasserstein penalty method to control the mechanical power input of generator. Let ${\mathbf{θ}}_{i}$ and $P_{e,i}$ be the voltage angle (in radian) and the mechanical power input (in per unit), respectively, at generator bus $i$. The swing equation of this system is then given by where $M_{i}$ and $D_{i}$ denote the inertia coefficient (in pu$\cdot$sec^2^/rad) and the damping coefficient (in pu$\cdot$sec/rad) of the generator at bus $i$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Power System Frequency Control Problem", "weight": 1.0} -->

Assuming that all the voltage magnitudes are $1$ per unit, the angle differences $|{{\mathbf{θ}}_{i} - {\mathbf{θ}}_{j}}|$'s are small, and all the transmission lines are (almost) lossless, the AC power flow equation can be approximated by the following linearized DC power flow equation: where $P_{e}:={(P_{e,1},\ldots,P_{e,\overline{n}})}$, ${\mathbf{θ}}:={({\mathbf{θ}}_{1},\ldots,{\mathbf{θ}}_{\overline{n}})}$, and $L \in {\mathbb{R}}^{\overline{n} \times \overline{n}}$ is the Kron-reduced Laplacian matrix of this power network.^99^9The Kron reduction is used to express the system in the reduced dimension $\overline{n}$ by focusing on the interactions of the generator

<!-- chunk {"id": "body-0049", "role": "body", "section": "Power System Frequency Control Problem", "weight": 1.0} -->

We discretize this system using zero-order hold on the input and a sampling time of $0.1$ seconds to obtain the matrices $A$ and $B$ of the following discrete-time system model (5.1): where $w_{i,t}$ is the random disturbance (in per unit) at bus $i$ at stage $t$. It can model uncertain power injections generated by solar or wind energy sources.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Power System Frequency Control Problem", "weight": 1.0} -->

The state-dependent portion of the quadratic cost function (5.2) is chosen as where $\mathbb{1}$ denotes the $\overline{n}$-dimensional vector of all ones, the first term measures the deviation of rotor angles from their average $\overline{\mathbf{θ}}:={{\mathbb{1}^{\top}{\mathbf{θ}}}/\overline{n}}$, and the second term corresponds to the kinetic energy stored in the electro-mechanical generators. The matrix $R$ is chosen to be the $\overline{n}$ by $\overline{n}$ identity matrix.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Power System Frequency Control Problem", "weight": 1.0} -->

The IEEE 39-bus New England test case (with 10 generator buses, 29 load buses, and 40 transmission lines) is used to demonstrate the performance of the proposed LQ control $\pi_{\hat{w}}'$ with Wasserstein penalty. The initial values of voltage angles ${\mathbf{θ}}{}$ are determined by solving the (steady-state) power flow problem using MATPOWER. The initial frequency is set to be zero for all buses except bus 1 at which ${{\overset{˙}{\mathbf{θ}}}_{1}{}}:=0.1$ per unit. We use $\alpha = 0.9$ in all simulations.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Worst-case distribution policy", "weight": 1.0} -->

We first compare the standard LQG control policy $\pi_{\hat{w}}^{LQG}$ and the proposed DR-control policy $\pi_{\hat{w}}'$ with the Wasserstein penalty under the worst-case distribution policy $\gamma_{\hat{w}}'$ obtained by using the proof of Theorem 4. We set $N = 10$ and $\lambda = 0.03$. The i.i.d. samples ${\{{\hat{w}}^{(i)}\}}_{i = 1}^{N}$ are generated according to the normal distribution $\mathcal{N}{(0,{0.1^{2}I})}$. As depicted in Fig. 3,^1010^10The central bar on each box indicates the median; the bottom and top edges of the box indicate the 25th and 75th percentiles, respectively; and the '+' symbol represents the outliers.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Worst-case distribution policy", "weight": 1.0} -->

$\pi_{\hat{w}}'$ is less sensitive than $\pi_{\hat{w}}^{LQG}$ against the worst-case distribution policy.^1111^11The frequency deviation at other buses displays a similar behavior. In the $\lbrack 0,24\rbrack$ (seconds) interval, the frequency controlled by $\pi_{\hat{w}}^{LQG}$ fluctuates around non-zero values while $\pi_{\hat{w}}'$ maintains the frequency fluctuation centered approximately around zero. This is because the proposed DR-method takes into account the possibility of nonzero-mean disturbances, while the standard LQG method assumes zero-mean disturbances. Furthermore, the proposed DR-method suppress the frequency fluctuation much faster than the standard LQG method: Under $\pi_{\hat{w}}'$, the mean frequency deviation averaging across the buses is less than 1% for any time after 16.7 seconds.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Worst-case distribution policy", "weight": 1.0} -->

On the other hand, if the standard LQG control is used, it takes 41.8 seconds to take the mean frequency deviation (averaging across the buses) below 1%. The detailed results for each bus are reported in Table 2.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Out-of-sample performance guarantee", "weight": 1.0} -->

We now examine the out-of-sample performance of $\pi_{\hat{w}}'$ and how it depends on the penalty parameter $\lambda$ and the number $N$ of samples. The i.i.d. samples ${\{{\hat{w}}^{(i)}\}}_{i = 1}^{N}$ are generated according to the normal distribution $\mathcal{N}{(0,I)}$. Given $\lambda$ and $N$, we define the *reliability* of $\pi_{\hat{w}}'$ as As shown in Fig. 4, the reliability decreases with $\lambda$. This is because when using larger $\lambda$, the control policy $\pi_{\hat{w}}'$ becomes less robust against the deviation of the empirical distribution from the true distribution. Increasing $\lambda$ has the effect of decreasing the radius $\theta$ in DR-control. In addition, the reliability tends to increase as the number $N$ of samples used to design $\pi_{\hat{w}}'$ increases.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Out-of-sample performance guarantee", "weight": 1.0} -->

This result is consistent with the dependency of the DR-control reliability on the number of samples. By using this result, we can determine the penalty parameter to attain a desired out-of-sample performance guarantee (or reliability), given the number of samples.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this paper, we considered distributionally robust stochastic control problems with Wasserstein ambiguity sets by directly using the data samples of uncertain variables. We showed that the proposed framework has several salient features, including $(i)$ computational tractability with error bounds, $({ii})$ an out-of-sample performance guarantee, and $({iii})$ an explicit solution in the LQ setting. It is worth emphasizing that the Kantorovich duality principle plays a critical role in our DP solution and analysis. Furthermore, with regard to the out-of-sample performance guarantee, our analysis provides the unique insight that the contraction property of the Bellman operators extends a single-stage guarantee---obtained using a measure concentration inequality---to the corresponding multi-stage guarantee without any degradation in the confidence level.
