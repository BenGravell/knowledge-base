<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Explore-then-Commit for Nonstationary Linear Bandits with Latent Dynamics

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study a nonstationary bandit problem where rewards depend on both actions and latent states, the latter governed by unknown linear dynamics. Crucially, the state dynamics also depend on the actions, resulting in tension between short-term and long-term rewards. We propose an explore-then-commit algorithm for a finite horizon T. During the exploration phase, random Rademacher actions enable estimation of the Markov parameters of the linear dynamics, which characterize the action-reward relationship. In the commit phase, the algorithm uses the estimated parameters to design an optimized action sequence for long-term reward. Our proposed algorithm achieves tildeO(T^(2/3)) regret. Our analysis handles two key challenges: learning from temporally correlated rewards, and designing action sequences with optimal long-term reward. We address the first challenge by providing near-optimal sample complexity and error bounds for system identification using bilinear rewards. We address the second challenge by proving an equivalence with indefinite quadratic optimization over a hypercube, a known NP-hard problem. We provide a sub-optimality guarantee for this problem, enabling our regret upper bound.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Lastly, we propose a semidefinite relaxation with Goemans-Williamson rounding as a practical approach.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many application domains, like personalized recommendations or online advertising, require sequential decision-making under uncertainty. Classical bandit algorithms address the trade-off between reducing uncertainty and optimizing performance in environments where rewards do not depend on the algorithm's past decisions. Many real world systems exhibit temporal dependencies actions influence not only immediate reward, but also the future state of the environment. This paper studies such a setting where decisions propagate through latent dynamics, leading to correlations that fundamentally change both how to learn and how to act optimally.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We study a nonstationary bandit problem in which reward depends bilinearly on the current action and an unobserved latent state that evolves according to a stable linear dynamical system. where $\bv{A},\bv{B},\bv{C}$ are unknown matrices, $\bv{u}_t$ is a bounded action chosen by the learner, $\bv{w}_t,z_t$ are random noise processes, and $\bv{x}_t$ is the latent state, at time $t{\geq}0$. Unlike classical multi-armed bandits with i.i.d. rewards, here actions not only determine immediate payoffs but also propagate through the state dynamics, creating temporal correlations in rewards, and making parameter estimation and optimal action sequence search significantly more challenging.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We observe that the problem can be resolved in the following ways. The issue of temporal correlation to estimate unknown parameters is addressed by improving upon recent results from system identification While the state-space parameters may not be identifiable from the observed rewards(without additional assumptions on $\bv{A},\bv{B},\bv{C}$), it is possible to obtain high-probability bounds on the estimation error for the Markov parameters, which characterize the action-reward relationship. In order to obtain an optimal long-term reward, we show that it is sufficient to use only this action-reward representation. In particular, selecting an optimal action sequence is equivalent to solving an indefinite quadratic problem over a hypercube, where the quadratic function is defined in terms of the Markov parameters.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Combining these two insights, we propose an explorethencommit (ETC) algorithm. In the exploration phase, the learner applies random Rademacher actions to estimate the system’s Markov parameter. In the commit phase, it commits to an action sequence which is a solution to an indefinite quadratic optimization problem. We show that, with high probability, this algorithm achieves sublinear regret, scaling as $\tilde{\mathcal{O}}(T^{2/3})$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our setting bears relation to several other nonstationary bandits, including restless bandits rebounding bandits, and bandits with underlying state, to name a few (see [sec:related-work] for further discussion). Key novelties of our setting include that states can be of arbitrary dimension, the evolution can depend on interactions between dimensions (i.e., the matrix $\bv{A}$ need not be diagonal), and actions directly affect states in a potentially correlated manner (through the matrix $\bv{B}$). Furthermore, unlike many multi-armed bandit settings, we consider a continuous action space. Our problem also bears relation to model-based reinforcement learning for linear dynamics, but the reward differs and provides only partial information about the underlying state.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

- Framework: We propose a novel nonstationary bandit problem in which the action affects both the current reward (through a bilinear interaction) as well as the future rewards (through a latent state). - Algorithm: We propose an explore-then-commit algorithm for our bandit problem. After exploration with random Rademacher actions, we estimate the Markov parameters which characterize the action-reward relationship. We then commit to an optimized action sequence obtained by solving a semidefinite relaxation of indefinite quadratic optimization over a hypercube a known NP-hard problem. - Estimation: We provide near-optimal sample complexity and estimation error bounds for learning Markov parameters. Specifically, in terms of the exploration length $H$, our error rate scales as $\tilde{\mathcal{O}}(1/\sqrt{H})$, and we require $H \gtrsim \tilde{\mathcal{O}}(d_M)$, where $d_M$ is the dimension of unknown Markov parameters.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

- Regret: We prove an upper bound on regret scaling as $\tilde{\mathcal{O}}(T^{2/3})$, and additionally provide a sub-optimality guarantee for the semidefinite relaxation with the Goemans-Williamson rounding approach. [sec:problem-formulation] formalizes the model and the regret benchmark, defines the action set, and discuss the computational difficulty of the problem. [sec:main-results] introduces the ETC algorithm and its regret guarantee. [sec:sys-id] presents our parameter estimation results with sample complexity and error bounds. [sec:regret-analysis] discuss our regret analysis. [sec:exp] presents numerical experiments. [sec:related-work] shows related work to this paper, and [sec:conclusion]concludes the paper.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notations: We use boldface lowercase/uppercase letters to denote vectors/matrices. The $\ell_2$-norm and $\ell_\infty$-norm of a vector $\bv{x}$ are denoted by $\twonorm{\bv{x}}$ and $\infnorm{\bv{x}}$, respectively. The spectral radius, the spectral norm, and the Frobenius norm of a matrix $\bv{X}$ are denoted by $\rho(\bv{X}), \norm{\bv{X}}$, and $\fronorm{\bv{X}}$, respectively. The largest and smallest eigenvalue of a square matrix $\bv{X}$ are denoted by $\lambda_{\max}(\bv{X})$ and $\lambda_{\min}(\bv{X})$. The operation $\otimes$ denotes the Kronecker product.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We use $\gtrsim$ and $\lesssim$ for inequalities that hold up to an absolute constant factor. The notation $\tilde{\mathcal{O}}$ hides constants and logarithmic terms. Lastly, we use $\bv{0}_d$ and $\bv{0}_{m\times n}$ to denote the zero vector in $\mathbb{R}^d$ and the zero matrix in $\mathbb{R}^{m\times n}$, respectively.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

confidence=None created_by=None text='\\begin{tikzpicture}[\n node distance=1.2cm and 1.5cm,\n latent/.style={circle, draw, minimum size=0.8cm},\n obs/.style={circle, draw, fill=gray!30, minimum size=0.8cm},\n action/.style={circle, draw, minimum size=0.8cm}\n]\n% Nodes for t=1\n\\node[latent] (z1) {$\\vx_1$};\n\\node[obs, below of=z1] (r1) {$r_1$};\n\\node[action, below of=r1] (a1) {$\\vu_1$};\n% Nodes for t=2\n\\node[latent, right=of z1] (ztk) {$\\vx_{2}$};\n\\node[obs, below of=ztk]

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

(z1) -- (ztk);\n\\draw[->] (ztk) -- (zt1);\n\\draw[->, densely dotted, line width=0.8pt] (zt1) -- (zt);\n% Arrows from latent to observed\n\\draw[->] (z1) -- (r1);\n\\draw[->] (ztk) -- (rtk);\n\\draw[->] (zt1) -- (rt1);\n\\draw[->] (zt) -- (rt);\n% Arrows from action to observed\n\\draw[->] (a1) -- (r1);\n\\draw[->] (atk) -- (rtk);\n\\draw[->] (at1) -- (rt1);\n\\draw[->] (at) -- (rt);\n% Arrows from action to next latent

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

state\n\\draw[->] (a1) -- (ztk);\n\\draw[->] (atk) -- (zt1);\n\\draw[->, densely dotted, line width=0.8pt] (at1) -- (zt);\n\n\\path (at1) -- (at) node[midway] {$\\cdots$};\n\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> Graphical Model for Non-Stationary Bandits with controlled Latent Dynamics.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We consider a nonstationary stochastic bandit problem with controlled i.e., the state is nontrivially influenced by the actions latent dynamics and a bilinear reward model. At each round $t{=}0,1, \dots, T$, the learner selects an action $\bv{u}_t$ from a bounded action set $\mathcal{U} {\subseteq} \mathbb{R}^p$, and receives a reward $r_t {\in} \mathbb{R}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

More specifically, the reward is bilinear in the latent state $\bv{x}_t {\in} \mathbb{R}^n$ and the action $\bv{u}_t {\in} \mathcal{U}$, whereas the latent state evolves according to a linear dynamical system, as defined in[eqn:sys], where $\bv{A}, \bv{B}, \bv{C}$ are unknown matrices of appropriate dimensions, and $\bv{w}_t$, $z_t$ are random zero-mean noise processes. Without loss of generality, we assume $\bv{x}_0{=}\bv{0}_n$. Throughout, we assume $\bv{A}$ is Schur-stable, that is, $\rho(\bv{A}){<}1$, and the noise processes are i.i.d.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

zero-mean sub-Gaussian, with $\bv{w}_t$ having variance proxy $\bvgrk{\Sigma}_w$ and $z_t$ having variance proxy $\sigma_z^2$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Objective, Action Set, and Regret", "weight": 1.0} -->

Our objective is to maximize the expected cumulative reward $\mathbb{E}\left[\sum_{t=0}^T r_t\right]$ over the horizon $T$, by choosing actions from a bounded set. For simplicity, we consider the action set to be a centered hypercube in $\mathbb{R}^p$. In other words, we choose \mathcal{U} =\{\bv{u} \in \mathbb{R}^p \colon \infnorm{\bv{u}}\le 1 \} = ^p.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Objective, Action Set, and Regret", "weight": 1.0} -->

Let $\{r_t^\star\}_{t=0}^T$ denote the rewards collected under the optimal open-loop action sequence, and $\{r_t^\pi\}_{t=0}^T$ denote the rewards collected by policy $\pi$. Then, the regret up to round $T$ of a policy $\pi$ is defined as: R_T(\pi):= \mathbb{E} \left[\sum_{t=0}^T r_t^\star - \sum_{t=0}^T r_t^\pi\right].

<!-- chunk {"id": "body-0021", "role": "body", "section": "Optimal Open-Loop Actions", "weight": 1.0} -->

In this section, we suppose that $\bv{A}, \bv{B}, \bv{C}$ are known, and show that the optimal action sequence is the solution to an indefinite quadratic optimization problem with $\ell_{\infty}$-norm constraint. By unrolling the latent state through[eqn:sys], we have $r_0 = z_0$, and for $t \ge 1$, r_t = \bv{u}_t^\top \bv{C} \sum_{i=0}^{t-1} \bv{A}^{t-i-1} (\bv{B}\bv{u}_i + \bv{w}_i) + z_t.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Optimal Open-Loop Actions", "weight": 1.0} -->

sequence and the corresponding cumulative reward are given as follows. This cumulative reward is our regret baseline.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Optimal Open-Loop Actions", "weight": 1.0} -->

This optimal action sequence represents the optimal open-loop strategy for accruing reward, in contrast to a feedback or closed-loop policy. It captures the problem of selecting optimal sequencesof actions to maximize the long-term reward, a consideration which is not present in the classical bandit settings.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Combinatorial Actions", "weight": 1.0} -->

[eqn:baseline-regret-form] is the maximization of an indefinite quadratic function over the hypercube. We show that it suffices to consider a discrete set of actions corresponding to the vertices of the hypercube, so that each coordinate of every action is restricted to $\pm 1$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Combinatorial Actions", "weight": 1.0} -->

The proof of Proposition [prop:max-vertex] is deferred to the appendix. We therefore take the action set to be $\mathcal{U}=\{-1,+1\}^p$ instead of the hypercube $^p$ in the remainder of this paper. Under this choice of action set, the optimization[eqn:baseline-regret-form] reduces to an instance of quadratic unconstrained binary optimization (QUBO), which is known to be NP-hard, as it generalizes classical problems such as MaxCut. Consequently, solving for the optimal actions exactly is computationally intractable. This motivates the use of semidefinite relaxations and randomized rounding schemes in [sec:exp].

<!-- chunk {"id": "body-0026", "role": "body", "section": "Main Result: Explore-then-Commit", "weight": 1.0} -->

We propose an explore–then–commit (ETC) algorithm for minimizing regret tailored to bandits with latent linear dynamics and bilinear rewards. The ETC algorithm runs in two phases, an exploration phase and a commit phase. In [subsec:exploration-phase], we describe the exploration phase, which consists in estimating the so-called Markov parameters The Markov parameters corresponding to the system eqn:sys are typically defined, for example, as the sequence of matrices $\lbrace \bv{C} \bv{A}^k \bv{B}\rbrace_{k \ge 0}$. of the system. In [subsec:commit-phase], we describe the commit phase, where the learner uses the estimated Markov parameters to formulate an open-loop optimization problem and design a sequence of actions for the remaining horizon. Finally, in [subsec:regret-guarantee], we state our main theoretical result: with appropriate choices of exploration and truncation lengths, the ETC algorithm achieves a regret of order $\tilde{\mathcal{O}}(T^{2/3})$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Main Result: Explore-then-Commit", "weight": 1.0} -->

We summarize the overall procedure in Algorithm[alg:EtC].

<!-- chunk {"id": "body-0028", "role": "body", "section": "Main Result: Explore-then-Commit", "weight": 1.0} -->

Horizon $T$, exploration length $H$, truncation length $L$ For $t {=} 0, \dots, H $, play $\bv{u}_t {\sim} {\rm Unif}(\{-1,+1\}^p)$ and observe reward $r_t$. an estimate $\hat{\bv{G}}$ of the first $L$ Markov parameters via least squares using $ \{(\bv{u}_t, r_t)\}_{t=0}^H$ as in [eqn:least\_squares].

<!-- chunk {"id": "body-0029", "role": "body", "section": "Exploration Phase", "weight": 1.0} -->

In the exploration phase, the learner selects actions independently from the Rademacher distribution ${\rm Unif}\{-1,+1\}^p$. This distribution satisfies the action constraint (see [subsec:action-set-NP-hard]) and provides sufficient excitation of the system, ensuring that the Markov parameters can be consistently estimated. Further discussion of persistence of excitation is deferred to the appendix.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Exploration Phase", "weight": 1.0} -->

\(\{(\bv{u}\_t,r\_t)\}\_{t=0}^H\) collected in this phase is used to estimate the system’s Markov parameters. Concretely, we form nonlinear regressors/features using the previous $L$ actions $(\bv{u}_{t-1},\dots,\bv{u}_{t-L})$ together with the current action $\bv{u}_t$, and use linear regression to predict the current reward $r_t$. The least-squares solution gives an estimate of the first $L$ Markov parameters $\{\bv{C}\bv{A}^k\bv{B}\}_{k=0}^{L-1}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Exploration Phase", "weight": 1.0} -->

Since the matrix $\bv{A}$ is Schur-stable, the influence of terms beyond lag $L$ decays geometrically. Hence, it suffices to estimate only the first $L$ parameters. The details of the regression procedure and error analysis are deferred to [sec:sys-id].

<!-- chunk {"id": "body-0032", "role": "body", "section": "Commit Phase", "weight": 1.0} -->

After exploration, the learner uses the estimated Markov parameters to construct an open-loop optimization problem aimed at maximizing the expected cumulative reward from Because the Rademacher actions and the noise processes are zero-mean, the theoretical objective will be \mathbb{E}\left[\sum_{t=H+1}^T r_t \right] = \frac{1}{2}\bv{u}_{H+1:T}^\top \bv{S}_{T\!-\!H\!-\!1} \bv{u}_{H+1:T} with $\bv{S}_{T\!-\!H\!-\!1} = \bv{M}_{T\!-\!H\!-\!1} + \bv{M}_{T\!-\!H\!-\!1}^\top$ where $\bv{M}_{T\!-\!H\!-\!1}$ is a block Toeplitz matrix with similar structure to Equation

<!-- chunk {"id": "body-0033", "role": "body", "section": "Commit Phase", "weight": 1.0} -->

[eqn:block-toeplitz-M](see the appendix for derivation).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Commit Phase", "weight": 1.0} -->

Since the true parameters are unknown, we replace them with estimates from the exploration phase. $\hat{\bv{S}}_{T-H-1}$ by substituting the estimated blocks for $\bv{C} \bv{A}^k \bv{B}$ whenever $k < L$ and setting the blocks to $\bv{0}_{p\times p}$ for $k \ge L$, consistent with the Schur-stability of $\bv{A}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Commit Phase", "weight": 1.0} -->

This yields the commit-phase optimization problem: \max_{\bv{u}_{H+1:T}}& \quad \frac{1}{2}\bv{u}_{H+1:T}^\top \hat{\bv{S}}_{T-H-1} \bv{u}_{H+1:T} \\\text{subject to}& \quad \bv{u}_{H+1:T} \in \{-1,+1\}^{p(T-H)} The structure of this problem is identical to [eqn:baseline-regret-form], but with estimated rather than true parameters. As noted in [subsec:action-set-NP-hard], the problem [eqn:commit-obj] is NP-hard. We therefore rely on practical approaches to obtain tractable approximations, which will be discussed in [subsec:SDP-GW] and [subsec:sign-iter].

<!-- chunk {"id": "body-0036", "role": "body", "section": "Regret Guarantee", "weight": 1.0} -->

Our main result establishes that the ETC algorithm achieves sublinear regret with high probability.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Regret Guarantee", "weight": 1.0} -->

With exploration length $H=\tilde{\mathcal{O}}(T^{2/3})$ and truncation length $L=\Theta(\log T)$, the explore-then-commit algorithm $\pi$(Alg.[alg:EtC]) achieves regret with high probability.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Regret Guarantee", "weight": 1.0} -->

The proof of Theorem [thm:regret-bound] is discussed in [sec:regret-analysis]. Note that the regret inevitably has a high-probability bound because the Markov parameter estimation error, which affects the regret, has a high-probability bound.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Regret Guarantee", "weight": 1.0} -->

This rate arises from a simple trade-off. The algorithm incurs linear loss during exploration ($\sim H$) and suffers estimation error of order $\tilde{\mathcal{O}}(\sqrt{1/H})$ across the remaining horizon ($\sim T$). Optimizing the bound over $H$ yields the $\tilde{\mathcal{O}}(T^{2/3})$ rate with $H=\tilde{\mathcal{O}}(T^{2/3})$. Lastly, taking $L=\Theta(\log T)$ makes the truncation error negligible, as already noted in [subsec:exploration-phase]where Schur stability implies geometric decay of higher-order terms.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Main Result: Parameter Estimation", "weight": 1.0} -->

In this section, we use the action-reward samples $\{(\bv{u}_t, r_t)\}_{t=0}^{H}$ from the exploration phase to estimate a map between the actions and rewards. Similar to [sattar2025learning], we can estimate Markov parameters by regressing the rewards $r_t$ to an expression defined by the history of inputs $\{\bv{u}_\tau\}_{\tau \leq t}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Main Result: Parameter Estimation", "weight": 1.0} -->

In this paper, we provide improved sample complexity and error bounds (compared with [sattar2025learning]), under the following assumption.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Main Result: Parameter Estimation", "weight": 1.0} -->

(b) $\bv{w}_t$ and $z_t$ are i.i.d. centered sub-Gaussian with variance proxy $\bvgrk{\Sigma}_w$ and $\sigma_z$, respectively; (c) $\bv{u}_t \overset{\text{i.i.d.}}{\sim} {\rm Unif}\left(\{-1,+1\}^p\right)$. [assump:sysID], we derive a bound on sample complexity and an estimation error of [eqn:estimation\_error\_form] in Theorem[thm:sysID]. We note the following fact regarding the stability condition.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Main Result: Parameter Estimation", "weight": 1.0} -->

Under Assumption[assump:sysID], let $\{(\bv{u}_t,r_t)\}_{t=0}^H$ be a single trajectory of action-reward pairs collected from the system [eqn:sys]. For given $\delta \in $, suppose H-L \gtrsim (L+1) \left(p^2L \log(p^2L) + \log \left(\frac{L+1}{\delta} \right)\right).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Main Result: Parameter Estimation", "weight": 1.0} -->

The proof of Theorem [thm:sysID] is presented in the appendix. The recent work shows that such a randomized design yields an estimation error bound of order $\tilde{\mathcal{O}}(1/\sqrt{\delta H})$ with probability at least $1-\delta$. In this work, we sharpen this guarantee by exploiting the sub-Gaussian structure of the noise processes, obtaining an improved bound of order $\tilde{\mathcal{O}}(\sqrt{\log(1/\delta)/H})$ with probability at least $1-\delta$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Main Result: Parameter Estimation", "weight": 1.0} -->

The first term in our error bound corresponds to the approximation error because we use only $L$ Markov parameters to reconstruct the reward function. It decays exponentially with $L$when the latent dynamics is strictly stable because the norm of Markov parameters decreases exponentially. The second term corresponds to the error due to noisy reward model and noisy latent dynamics update. This term depends linearly on the noise variance proxies.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Main Result: Parameter Estimation", "weight": 1.0} -->

The sample complexity in Theorem [thm:sysID] scales as $\tilde{\mathcal{O}}(p^2L^2)$, which is optimal in the dimension of Markov parameters $p^2$. In contrast, the sample complexity in [sattar2025learning] scales as $\tilde{\mathcal{O}}(p^4L^3)$. The reason for this improvement is the choice of inputs $\bv{u}_t \overset{\text{i.i.d.}}{\sim} {\rm Unif}\left(\{-1,+1\}^p\right)$ which leads to better persistence of excitation. Secondly, the error bound in Theorem[thm:sysID] depends on the failure probability $\delta$ through $\log(1/\delta)$. This is significantly better than the $1/\delta$ dependence in [sattar2025learning]which considers a setting where noise processes can be heavy-tailed.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Main Result: Parameter Estimation", "weight": 1.0} -->

The sub-Gaussian noise assumption in this paper allows using better concentration arguments, such as self-normalized bounds for martingales and Freedman’s inequality, to obtain optimal dependence on the failure probability.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Regret Analysis", "weight": 1.0} -->

In this section we prove Theorem [thm:regret-bound]. Additional details and proofs of intermediate results are deferred to the appendix. Recall the definition of regret from [eqn:regret\_def]. From Proposition[prop:regret-benchmark] and Equation[eqn:commit-theoretical-objective], we obtain R_T(\pi) {=} \frac{1}{2} (\bv{u}_{0:T}^\star)^{\!\top} \bv{S}_T \bv{u}_{0:T}^\star where $\bv{u}_{H+1:T}^\pi$ is the optimized action sequence which maximizes ([eqn:commit-obj]).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Regret Analysis", "weight": 1.0} -->

For the purpose of analysis, let $\tilde{\vu}_{H+1:T}$ be an action sequence that maximizes Equation[eqn:commit-theoretical-objective] with true parameters under the constraint $\tilde{\vu}_t \in \{-1,+1\}^p$ for $t=H+1,\dots,T$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Regret Analysis", "weight": 1.0} -->

(\bv{u}_{H+1:T}^\pi)^\top \hat{\bv{S}}_{T-H-1} \bv{u}_{H+1:T}^\pi \\Intuitively, $R_{1,T}$ captures the sub-optimality between the full-time horizon and the commit-phase horizon, $R_{2,T}$ captures the sub-optimality between the true and estimated dynamics, and finally $R_{3,T}$ captures the error from parameter estimation. We analyze these three terms in detail in [subsec:analysis-a] and [subsec:analysis-b-c].

<!-- chunk {"id": "body-0051", "role": "body", "section": "Upper Bounding $R_{1,T}$", "weight": 1.0} -->

$R_{1,T}$ quantifies the loss from truncating the horizon at $H$, capturing both short-term dependencies within the exploration phase and long-term dependencies between exploration and commit phases through the dynamics.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Upper Bounding $R_{1,T}$", "weight": 1.0} -->

The proof of Proposition [prop:regret-a] is deferred to the appendix. Note that the upper bound in [prop:regret-a] depends linearly on $H$, implying that the available reward grows linearly in time horizon. There is also a second term, a constant term independent of $H$. The coefficients $\alpha$ and $\beta$ depending on the stability of the state dynamics $\bv{A}$, and can be understood as effective memory capacity. The first term arises from to short-term dependencies within the exploration-phase. The second term is related to long-term dependencies which, due to stability, do not depend on the horizon.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Upper Bounding $R_{2,T}$ and $R_{3,T}$", "weight": 1.0} -->

$R_{2,T}$ and $R_{3,T}$ both depend on the estimation error $\epsilon$ and the truncation error $\rho^L$, and their bounds are given in the following proposition.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Upper Bounding $R_{2,T}$ and $R_{3,T}$", "weight": 1.0} -->

The proof of Proposition [prop:regret-b-c] is deferred to the appendix. We can observe that the bound depends on the length of commit-phase $T-H$, the estimation error $\epsilon$, and the truncation error $\rho^L$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Final Regret Analysis", "weight": 1.0} -->

Finally, combining Propositions [prop:regret-a] and [prop:regret-b-c] yields the following high-probability bound: R_T(\pi) \le 2p\kappa^2(\alpha H + \beta) + 4pT(\epsilon + \kappa^2\gamma_L).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Final Regret Analysis", "weight": 1.0} -->

From Theorem[thm:sysID], we can take $\epsilon \lesssim \sqrt{\tfrac{\log(1/\delta)}{H-L}}$ with probability at least $1-\delta$. Optimizing over $H$ gives $H=\tilde{\mathcal{O}}(T^{2/3})$, and with $L=\Theta(\log T)$ we obtain the high-probability regret bound $R_T(\pi)=\tilde{\mathcal{O}}(T^{2/3})$. Note that we define regret to be the expected cumulative rewards, where expectation is taken both over actions (in the exploration phase) and noise processes. However, we still have a high-probability bound on the regret because the estimation error bound holds with high probability.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Each curve shows a mean over 20 experiments, with shaded regions indicating $\pm1$ standard deviation. (a) Expected cumulative reward under the oracle benchmark, approximated by semidefinite relaxation with Goemans-Williamson rounding (SDP+GW) and by the sign-iteration method (SignIter). (b) The regret of the explore-then-commit algorithm measured against the SDP+GW oracle benchmark, compared with the theoretical $\tilde{\mathcal{O}}(T^{2/3})$ rate. (c)(d) Relative error of Markov parameter estimation for different truncation lengths $L$, under systems with spectral radii $\rho(\bv{A})=0.1$ and $\rho(\bv{A})=0.9$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In this section, we present numerical experiments with synthetic data. To obtain tractable solutions to [eqn:baseline-regret-form] and [eqn:commit-obj] and analyze sub-optimality, we investigate two methods: (i) a semidefinite relaxation combined with Goemans-Williamson random hyperplane rounding, and (ii) a heuristic sign-iteration method. The code for experiments can be found in

<!-- chunk {"id": "body-0059", "role": "body", "section": "SDP Relaxation and Rounding", "weight": 1.0} -->

Our problem is to maximize a quadratic form $\bv{x}^\top \bv{W} \bv{x}$ for some symmetric $\bv{W} \in \mathbb{R}^{n\times n}$ over $\bv{x}\in \{-1,1\}^n$, which is equivalent to \text{maximize } \; & \text{tr}(\bv{W}\bv{X}) \\\text{subject to } \; & \bv{X} \succeq 0, \; \text{rank} (\bv{X}) =1 \\Dropping the rank constraint yields the semidefinite relaxation, which we solve using the Mosek solver.

<!-- chunk {"id": "body-0060", "role": "body", "section": "SDP Relaxation and Rounding", "weight": 1.0} -->

To obtain a feasible binary matrix from a solution $\bv{X}$ to the relaxed problem, we apply Goemans-Williamson (GW) random hyperplane rounding algorithm: factor $\bv{X} = \bv{V}^\top \bv{V}$, sample $\bv{r} \sim \mathcal{N}(0,\bv{I}_n)$, and set a vector \text{sign}(\bv{r}^\top \bv{v}_1) & \cdots & \text{sign}(\bv{r}^\top \bv{v}_n) \end{bmatrix}^\top where $\bv{v}_i$ is the $i$th column vector of $\bv{V}$. Then the matrix $\bv{x}\bv{x}^\top$ is rank-one and feasible for [eqn:simple-form-matrix].

<!-- chunk {"id": "body-0061", "role": "body", "section": "SDP Relaxation and Rounding", "weight": 1.0} -->

In practice, we repeat the rounding multiple times and keep the best value of $\bv{x}^\top \bv{W} \bv{x}$. We will hereafter refer to this method as SDP+GW.

<!-- chunk {"id": "body-0062", "role": "body", "section": "SDP Relaxation and Rounding", "weight": 1.0} -->

For MaxCut problems, SDP+GW achieves an $\alpha$-approximation algorithm with $\alpha\approx0.87856$. While our objective is not exactly MaxCut, we derive a similar lower bound which depend on $\bv{W}$(see the appendix).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Sign-Iteration Method", "weight": 1.0} -->

As an alternative to relaxation and rounding, we also consider a heuristic method called sign-iteration (henceforth SignIter) to maximize $\bv{x}^\top \bv{W} \bv{x}$ over $\bv{x} \in \{-1,+1\}^n$. Starting from a random $\bv{x}^{}$, the update is \mathrm{sign}\big((\bv{W} \bv{x}^{(k)})_i\big), & (\bv{W} \bv{x}^{(k)})_i \neq 0, \\and the procedure repeats until convergence or a maximum number of iterations. To mitigate dependence on initialization, the method is run multiple times and the best objective value is returned.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Experimental Evaluation of Regret", "weight": 1.0} -->

We consider a simple latent dynamics and reward function specified by \bv{A}{=} \textup{\textbf{diag}}([0.3~0.15~0.12]), ~ \bv{B} {=} \begin{bmatrix} \end{bmatrix}, ~ \bv{C} {=} \begin{bmatrix} \end{bmatrix}^\top We set the noise processes to be Gaussian with variances $\bvgrk{\Sigma}_w = (0.01)^2 \bv{I}_3$ and $\sigma_z=0.01$. To select the exploration and truncation lengths, we perform a grid search to determine constants $c_1,c_2$ in $H=c_1T^{2/3}$ and $L=c_2\log T$, calibrated at $T=1500$. These constants were then fixed and applied across all regret experiments.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Experimental Evaluation of Regret", "weight": 1.0} -->

We ran the ETC algorithm under this setup, repeating each experiment $20$ times with different noise seeds. Regret was computed using the two benchmarks described in [subsec:SDP-GW] and [subsec:sign-iter]. As shown in Figure[fig:regret-benchmark], SDP+GW consistently attains higher benchmark values than SignIter, indicating that the latter rarely approaches the true optimum. We therefore adopt the SDP+GWbenchmark as the reference for regret. [fig:regret] reports regrets measured against this benchmark. The SDP+GW regret grows slowly and closely follows the $\tilde{\mathcal{O}}(T^{2/3})$ rate, consistent with our theoretical analysis. In contrast, the SignIter regret increases much more rapidly, nearly linearly in $T$, demonstrating that the heuristic commit phase is substantially suboptimal relative to the SDP+GWbenchmark.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Parameter Estimation", "weight": 1.0} -->

In this section, we show that the parameters are estimated effectively. We generate random instances with $n=5$, $p=3$, and Schur-stable $\bv{A}$ (scaled from i.i.d. $\mathcal N(0,1/n)$ entries), with $\bv{B},\bv{C}$ similarly and noise levels $\bvgrk{\Sigma}_w=(0.05)^2 \bv{I}_n$, $\sigma_z=0.05$. We study the estimation error of Markov parameters for two spectral radii, $\rho(\bv{A})=0.1$ and $\rho(\bv{A})=0.9$, by repeating each experiment 20 times with different noise seeds. [fig:param-est-rho-p1] and [fig:param-est-rho-p9] show that the relative estimation error decreases with exploration length $H$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Parameter Estimation", "weight": 1.0} -->

For small $\rho(\bv{A})$, shorter truncation lengths $L$ yield smaller errors, while for large $\rho(\bv{A})$ the trend reverses, reflecting a trade-off between memory of states and number of Markov parameters. We also observe a characteristic double-descent effect as the regression problem transitions from under- to over-determined. For further discussion and derivations, see[sattar2025learning]and the appendix.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Comparison of Practical Methods", "weight": 1.0} -->

To evaluate the performance of the two approaches, we compare them against the true optimum of the regret-benchmark problem [eqn:baseline-regret-form]. Since this optimization is NP-hard in general, we restrict to small instances ($n{=}3$, $p{=}2$, $T{=}5{,\dots,}16$) where brute force is feasible. Both SDP+GW and SignIter are randomized, we vary the number of rounding trials ($r{=}1,10,30$) and repeat each experiment 20 times with different seeds.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Comparison of Practical Methods", "weight": 1.0} -->

Comparison between SDP+GW and SignIter to the true optimum from the brute force method. [fig:brute-force-comparison] shows SignIter becomes increasingly suboptimal as $T$ grows, even with more rounding trials. In contrast, SDP+GW consistently returns values very close to the brute-force optimum; even a single trial ($r{=}1$) mostly outperforms all SignIter cases. These results indicate that SDP+GWis an effective and reliable method for the commit-phase optimization.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We study a nonstationary bandit problem where rewards depend bilinearly on actions and latent states evolving under unknown linear dynamics. We propose an explore-then-commit algorithm that combines the system parameter estimation and an open-loop action optimization. Our analysis shows that the algorithm achieves $\tilde{\mathcal{O}}(T^{2/3})$regret with high probability. To address the NP-hard commit-phase optimization, we employed semidefinite relaxation and a rounding scheme, demonstrating its effectiveness empirically.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Conclusion", "weight": 1.5} -->

A natural direction for future work is to move beyond open-loop policies toward adaptive strategies. The recent work a related structure in control theory, studying an optimal control problem of minimizing quadratic cost under linear dynamics with bilinear observations. It shows that the optimal feedback policy is nonlinear in the estimated state, suggesting that extending open-loop analysis to feedback or closed-loop designs is both challenging and an important direction for future research.
