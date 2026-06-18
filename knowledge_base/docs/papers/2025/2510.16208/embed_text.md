## Introduction

Many application domains, like personalized recommendations or online advertising, require sequential decision-making under uncertainty. Classical bandit algorithms address the trade-off between reducing uncertainty and optimizing performance in environments where rewards do not depend on the algorithm's past decisions. Many real world systems exhibit temporal dependencies -- actions influence not only immediate reward, but also the future state of the environment Schedl et al.,. This paper studies such a setting where decisions propagate through latent dynamics, leading to correlations that fundamentally change both how to learn and how to act optimally.

We study a nonstationary bandit problem in which reward depends *bilinearly* on the *current action* and an *unobserved latent state* that evolves according to a stable linear dynamical system. Formally,

where ${\mathbf{A}},{\mathbf{B}},{\mathbf{C}}$ are unknown matrices, ${\mathbf{u}}_{t}$ is a bounded action chosen by the learner, ${\mathbf{w}}_{t},z_{t}$ are random noise processes, and ${\mathbf{x}}_{t}$ is the latent state, at time $t \geq 0$. Unlike classical multi-armed bandits with i.i.d. rewards, here actions not only determine immediate payoffs but also propagate through the state dynamics, creating temporal correlations in rewards, and making parameter estimation and optimal action sequence search significantly more challenging.

We observe that the problem can be resolved in the following ways. The issue of temporal correlation to estimate unknown parameters is addressed by improving upon recent results from system identification Sattar et al., 2025b. While the state-space parameters may not be identifiable from the observed rewards (without additional assumptions on ${\mathbf{A}},{\mathbf{B}},{\mathbf{C}}$), it is possible to obtain high-probability bounds on the estimation error for the *Markov parameters*, which characterize the action-reward relationship. In order to obtain an optimal long-term reward, we show that it is sufficient to use only this action-reward representation. In particular, selecting an optimal action sequence is equivalent to solving an indefinite quadratic problem over a hypercube, where the quadratic function is defined in terms of the Markov parameters.

Combining these two insights, we propose an *explore--then--commit* (ETC) algorithm. In the exploration phase, the learner applies random Rademacher actions to estimate the system's Markov parameter. In the commit phase, it commits to an action sequence which is a solution to an indefinite quadratic optimization problem. We show that, with high probability, this algorithm achieves sublinear regret, scaling as $\overset{\sim}{\mathcal{O}}{(T^{2/3})}$.

Our setting bears relation to several other nonstationary bandits, including restless bandits Whittle rebounding bandits Leqi et al. and bandits with underlying state Khosravi et al. to name a few (see §7 for further discussion). Key novelties of our setting include that states can be of arbitrary dimension, the evolution can depend on interactions between dimensions (i.e., the matrix $\mathbf{A}$ need not be diagonal), and actions directly affect states in a potentially correlated manner (through the matrix $\mathbf{B}$). Furthermore, unlike many multi-armed bandit settings, we consider a continuous action space. Our problem also bears relation to model-based reinforcement learning for linear dynamics Dean et al. Simchowitz Mania et al. Lale et al., 2020b; Lale et al., 2020a, but the reward differs and provides only partial information about the underlying state.

In this paper, we make following contributions:

Framework: We propose a novel nonstationary bandit problem in which the action affects both the current reward (through a bilinear interaction) as well as the future rewards (through a latent state).

Algorithm: We propose an explore-then-commit algorithm for our bandit problem. After exploration with random Rademacher actions, we estimate the Markov parameters which characterize the action-reward relationship. We then commit to an optimized action sequence obtained by solving a semidefinite relaxation of indefinite quadratic optimization over a hypercube --- a known NP-hard problem.

Estimation: We provide near-optimal sample complexity and estimation error bounds for learning Markov parameters. Specifically, in terms of the exploration length $H$, our error rate scales as $\overset{\sim}{\mathcal{O}}{({1/\sqrt{H}})}$, and we require $H \gtrsim {\overset{\sim}{\mathcal{O}}{(d_{M})}}$, where $d_{M}$ is the dimension of unknown Markov parameters.

Regret: We prove an upper bound on regret scaling as $\overset{\sim}{\mathcal{O}}{(T^{2/3})}$, and additionally provide a sub-optimality guarantee for the semidefinite relaxation with the Goemans-Williamson rounding approach.

### Organization

§2 formalizes the model and the regret benchmark, defines the action set, and discuss the computational difficulty of the problem. §3 introduces the ETC algorithm and its regret guarantee. §4 presents our parameter estimation results with sample complexity and error bounds. §5 discuss our regret analysis. §6 presents numerical experiments. §7 shows related work to this paper, and §8 concludes the paper.

Notations: We use boldface lowercase/uppercase letters to denote vectors/matrices. The $\ell_{2}$-norm and $\ell_{\infty}$-norm of a vector $\mathbf{x}$ are denoted by $\left\| {\mathbf{x}} \right\|_{2}$ and $\left\| {\mathbf{x}} \right\|_{\infty}$, respectively. The spectral radius, the spectral norm, and the Frobenius norm of a matrix $\mathbf{X}$ are denoted by ${\rho{({\mathbf{X}})}},\left\| {\mathbf{X}} \right\|$, and $\left\| {\mathbf{X}} \right\|_{F}$, respectively. The largest and smallest eigenvalue of a square matrix $\mathbf{X}$ are denoted by $\lambda_{\max}{({\mathbf{X}})}$ and $\lambda_{\min}{({\mathbf{X}})}$. The operation $\otimes$ denotes the Kronecker product. We use $\gtrsim$ and $\lesssim$ for inequalities that hold up to an absolute constant factor. The notation $\overset{\sim}{\mathcal{O}}$ hides constants and logarithmic terms. Lastly, we use $\mathbf{0}_{d}$ and $\mathbf{0}_{m \times n}$ to denote the zero vector in ${\mathbb{R}}^{d}$ and the zero matrix in ${\mathbb{R}}^{m \times n}$, respectively.

## Problem Formulation

Figure 1: Graphical Model for Non-Stationary Bandits with controlled Latent Dynamics.

We consider a nonstationary stochastic bandit problem with controlled^11^1i.e., the state is nontrivially influenced by the actions latent dynamics and a bilinear reward model. At each round $t = {0,1,\ldots,T}$, the learner selects an action ${\mathbf{u}}_{t}$ from a bounded action set $\mathcal{U} \subseteq {\mathbb{R}}^{p}$, and receives a reward $r_{t} \in {\mathbb{R}}$. More specifically, the reward is bilinear in the latent state ${\mathbf{x}}_{t} \in {\mathbb{R}}^{n}$ and the action ${\mathbf{u}}_{t} \in \mathcal{U}$, whereas the latent state evolves according to a linear dynamical system, as defined , where ${\mathbf{A}},{\mathbf{B}},{\mathbf{C}}$ are unknown matrices of appropriate dimensions, and ${\mathbf{w}}_{t}$, $z_{t}$ are random zero-mean noise processes. Without loss of generality, we assume ${\mathbf{x}}_{0} = \mathbf{0}_{n}$. Throughout, we assume $\mathbf{A}$ is Schur-stable, that is, ${\rho{({\mathbf{A}})}} < 1$, and the noise processes are i.i.d. zero-mean sub-Gaussian, with ${\mathbf{w}}_{t}$ having variance proxy $\mathbf{\Sigma}_{w}$ and $z_{t}$ having variance proxy $\sigma_{z}^{2}$.

### Objective, Action Set, and Regret

Our objective is to maximize the expected cumulative reward ${\mathbb{E}}\left\lbrack {\sum_{t = 0}^{T}r_{t}} \right\rbrack$ over the horizon $T$, by choosing actions from a bounded set. For simplicity, we consider the action set to be a centered hypercube in ${\mathbb{R}}^{p}$. In other words, we choose

Let ${\{ r_{t}^{\star}\}}_{t = 0}^{T}$ denote the rewards collected under the *optimal open-loop action sequence*, and ${\{ r_{t}^{\pi}\}}_{t = 0}^{T}$ denote the rewards collected by policy $\pi$. Then, the regret up to round $T$ of a policy $\pi$ is defined as:

### Optimal Open-Loop Actions

In this section, we suppose that ${\mathbf{A}},{\mathbf{B}},{\mathbf{C}}$ are known, and show that the optimal action sequence is the solution to an indefinite quadratic optimization problem with $\ell_{\infty}$-norm constraint. By unrolling the latent state through, we have $r_{0} = z_{0}$, and for $t \geq 1$,

Since ${\mathbf{w}}_{t}$ and $z_{t}$ have zero-mean, the expected cumulative reward is given by

where ${\mathbf{u}}_{0:T}:=\left\lbrack {{\mathbf{u}}_{T}^{\top}{\mathbf{u}}_{T - 1}^{\top}\cdots{\mathbf{u}}_{0}^{\top}} \right\rbrack^{\top} \in {\mathbb{R}}^{p{({T + 1})}}$, and ${\mathbf{M}}_{T} \in {\mathbb{R}}^{{{p{({T + 1})}} \times p}{({T + 1})}}$ is a block Toeplitz matrix with $(i,j)$-th $p \times p$ block given by

With these definitions, the optimal action sequence and the corresponding cumulative reward are given as follows. This cumulative reward is our regret baseline.

### Proposition 1

Let $\mathbf{S}_{T}:={\mathbf{M}_{T} + \mathbf{M}_{T}^{\top}}$. Then, the optimal open-loop action sequence $\mathbf{u}_{0:T}^{\star}$ is the solution to the problem:

Note that the maximum value of (i.e. the optimal expected cumulative reward) is at least $\frac{1}{2}\lambda_{\max}\left( {\mathbf{S}}_{T} \right)$ because $\left\| {\mathbf{u}}_{0:T} \right\|_{2} \leq 1$ implies $\left\| {\mathbf{u}}_{0:T} \right\|_{\infty} \leq 1$.

This optimal action sequence represents the optimal *open-loop* strategy for accruing reward, in contrast to a *feedback* or *closed-loop* policy Bar-Shalom and Tse,. It captures the problem of selecting optimal *sequences* of actions to maximize the long-term reward, a consideration which is not present in the classical bandit settings.

### Combinatorial Actions

The problem is the maximization of an indefinite quadratic function over the hypercube. We show that it suffices to consider a discrete set of actions corresponding to the vertices of the hypercube,

so that each coordinate of every action is restricted to $\pm 1$.

### Proposition 2

If $\mathbf{A} \in {\mathbb{R}}^{n \times n}$ is symmetric with nonnegative diagonal entries, a maximizer of $\mathbf{z}^{\top}\mathbf{A}\mathbf{z}$ over ${\lbrack{- 1},1\rbrack}^{n}$ exists at a vertex $\mathbf{s} \in {\{{- 1},{+ 1}\}}^{n}$, that is,

The proof of Proposition 2 is deferred to the appendix. We therefore take the action set to be $\mathcal{U} = {\{{- 1},{+ 1}\}}^{p}$ instead of the hypercube ${\lbrack{- 1},1\rbrack}^{p}$ in the remainder of this paper. Under this choice of action set, the optimization reduces to an instance of *quadratic unconstrained binary optimization* (QUBO), which is known to be NP-hard, as it generalizes classical problems such as MaxCut. Consequently, solving for the optimal actions exactly is computationally intractable. This motivates the use of semidefinite relaxations and randomized rounding schemes in §6.

## Main Result: Explore-then-Commit

We propose an explore--then--commit (ETC) algorithm for minimizing regret tailored to bandits with latent linear dynamics and bilinear rewards. The ETC algorithm runs in two phases, *an exploration phase* and *a commit phase*. In §3.1, we describe the *exploration phase*, which consists in estimating the so-called *Markov parameters*^22^2The Markov parameters corresponding to the system are typically defined, for example in Sattar et al., 2025b, as the sequence of matrices ${\{{{\mathbf{C}}{\mathbf{A}}^{k}{\mathbf{B}}}\}}_{k \geq 0}$. of the system. In §3.2, we describe the *commit phase*, where the learner uses the estimated Markov parameters to formulate an open-loop optimization problem and design a sequence of actions for the remaining horizon. Finally, in §3.3, we state our main theoretical result: with appropriate choices of exploration and truncation lengths, the ETC algorithm achieves a regret of order $\overset{\sim}{\mathcal{O}}{(T^{2/3})}$. We summarize the overall procedure in Algorithm 1.

1:Horizon T, exploration length H, truncation length L
3:For t = 0, …, H, play ut ∼ Unif ({−1, +1}p) and observe reward rt.
4:Find an estimate $\hat{\mathbf{G}}$ of the first L Markov parameters via least squares using {(ut,rt)}t = 0H as .
5:Construct ${\hat{\mathbf{S}}}_{T - H - 1} = {\frac{1}{2}{({{\hat{\mathbf{M}}}_{T - H - 1} + {\hat{\mathbf{M}}}_{T - H - 1}^{\top}})}}$ where MT − H − 1 is defined via $\hat{\mathbf{G}}$ as .
7:Find a sequence (uH + 1π,…,uTπ) that solves,

$\max\limits_{{\mathbf{u}}_{{H + 1}:T}}$
$\frac{1}{2}{\mathbf{u}}_{{H + 1}:T}^{\top}{\hat{\mathbf{S}}}_{T - H - 1}{\mathbf{u}}_{{H + 1}:T}$

by (a) SDP relaxation with Goemans-Williamson rounding, or (b) sign-iteration method.
8:For t = H + 1, …, T, play utπ and observe reward rt.

### Exploration Phase

In the exploration phase, the learner selects actions independently from the Rademacher distribution ${Unif}{\{{- 1},{+ 1}\}}^{p}$. This distribution satisfies the action constraint (see §2.3) and provides sufficient excitation of the system, ensuring that the Markov parameters can be consistently estimated Sattar et al., 2025b. Further discussion of persistence of excitation is deferred to the appendix.

The trajectory ${\{{({\mathbf{u}}_{t},r_{t})}\}}_{t = 0}^{H}$ collected in this phase is used to estimate the system's Markov parameters. Concretely, we form nonlinear regressors/features using the previous $L$ actions $({\mathbf{u}}_{t - 1},\ldots,{\mathbf{u}}_{t - L})$ together with the current action ${\mathbf{u}}_{t}$, and use linear regression to predict the current reward $r_{t}$. The least-squares solution gives an estimate of the first $L$ Markov parameters ${\{{{\mathbf{C}}{\mathbf{A}}^{k}{\mathbf{B}}}\}}_{k = 0}^{L - 1}$.

Since the matrix $\mathbf{A}$ is Schur-stable, the influence of terms beyond lag $L$ decays geometrically. Hence, it suffices to estimate only the first $L$ parameters. The details of the regression procedure and error analysis are deferred to §4.

### Commit Phase

After exploration, the learner uses the estimated Markov parameters to construct an open-loop optimization problem aimed at maximizing the expected cumulative reward from $t = {H + 1}$ to $T$. Because the Rademacher actions and the noise processes are zero-mean, the theoretical objective will be

with ${\mathbf{S}}_{T - H - 1} = {{\mathbf{M}}_{T - H - 1} + {\mathbf{M}}_{T - H - 1}^{\top}}$ where ${\mathbf{M}}_{T - H - 1}$ is a block Toeplitz matrix with similar structure to Equation (see the appendix for derivation).

Since the true parameters are unknown, we replace them with estimates from the exploration phase. Specifically, we form ${\hat{\mathbf{S}}}_{T - H - 1}$ by substituting the estimated blocks for ${\mathbf{C}}{\mathbf{A}}^{k}{\mathbf{B}}$ whenever $k < L$ and setting the blocks to $\mathbf{0}_{p \times p}$ for $k \geq L$, consistent with the Schur-stability of $\mathbf{A}$. This yields the commit-phase optimization problem:

The structure of this problem is identical to, but with estimated rather than true parameters. As noted in §2.3, the problem is NP-hard. We therefore rely on practical approaches to obtain tractable approximations, which will be discussed in §6.1 and §6.2.

### Regret Guarantee

Our main result establishes that the ETC algorithm achieves sublinear regret with high probability.

### Theorem 3

With exploration length $H = {\overset{\sim}{\mathcal{O}}{(T^{2/3})}}$ and truncation length $L = {\Theta{({\log T})}}$, the explore-then-commit algorithm $\pi$ (Alg. 1) achieves regret

with high probability.

The proof of Theorem 3 is discussed in §5. Note that the regret inevitably has a high-probability bound because the Markov parameter estimation error, which affects the regret, has a high-probability bound.

This rate arises from a simple trade-off. The algorithm incurs linear loss during exploration ($\sim H$) and suffers estimation error of order $\overset{\sim}{\mathcal{O}}{(\sqrt{1/H})}$ across the remaining horizon ($\sim T$). Optimizing the bound over $H$ yields the $\overset{\sim}{\mathcal{O}}{(T^{2/3})}$ rate with $H = {\overset{\sim}{\mathcal{O}}{(T^{2/3})}}$. Lastly, taking $L = {\Theta{({\log T})}}$ makes the truncation error negligible, as already noted in §3.1 where Schur stability implies geometric decay of higher-order terms.

## Main Result: Parameter Estimation

In this section, we use the action-reward samples ${\{{({\mathbf{u}}_{t},r_{t})}\}}_{t = 0}^{H}$ from the exploration phase to estimate a map between the actions and rewards. Similar to Sattar et al., 2025b, we can estimate Markov parameters by regressing the rewards $r_{t}$ to an expression defined by the history of inputs ${\{{\mathbf{u}}_{\tau}\}}_{\tau \leq t}$. For $t \geq L$, the reward $r_{t}$ depends on the past $L$ actions as follows:

To ease notation, for any sequence of vectors ${\{{\mathbf{q}}_{t}\}}_{t = 0}^{T}$, letc${\overline{\mathbf{q}}}_{t}:=\left\lbrack {{\mathbf{q}}_{t}^{\top}{\mathbf{q}}_{t - 1}^{\top}\cdots{\mathbf{q}}_{{t - L} + 1}^{\top}} \right\rbrack^{\top}$ denote a concatenation of past $L$ vectors starting from $t \geq L$. If we let

then can be compactly written as

where we define the covariates ${\overset{\sim}{\mathbf{u}}}_{t}:={{\overline{\mathbf{u}}}_{t - 1} \otimes {\mathbf{u}}_{t}} \in {\mathbb{R}}^{p^{2}L}$, the effective noise $\zeta_{t}:={{{\mathbf{u}}_{t}^{\top}{\mathbf{C}}{\mathbf{A}}^{L}{\mathbf{x}}_{t - L}} + {{\mathbf{u}}_{t}^{\top}{\mathbf{F}}{\overline{\mathbf{w}}}_{t - 1}} + z_{t}}$, and ${\mathbf{F}}:={\lbrack{{\mathbf{C}}{\mathbf{C}}{\mathbf{A}}\cdots{\mathbf{C}}{\mathbf{A}}^{L - 1}}\rbrack}$. Hence, we can formulate the following least-squares problem to estimate the unknown parameter $\mathbf{G}$ from ${\{{({\mathbf{u}}_{t},r_{t})}\}}_{t = 0}^{H}$:

Let $\overset{\sim}{\mathbf{U}}:={\sum_{t = {L + 1}}^{H}{{\overset{\sim}{\mathbf{u}}}_{t}{\overset{\sim}{\mathbf{u}}}_{t}^{\top}}}$ for brevity. When $\overset{\sim}{\mathbf{U}}$ is full rank, the solution to the least-squares problem above is ${{\mathbf{v}\mathbf{e}\mathbf{c}}{(\hat{\mathbf{G}})}} = {{\overset{\sim}{\mathbf{U}}}^{- 1}{\sum_{t = {L + 1}}^{H}{{\overset{\sim}{\mathbf{u}}}_{t}r_{t}}}}$, and the corresponding estimation error is given by

In this paper, we provide improved sample complexity and error bounds, under the following assumption.

### Assumption 1

\(a\) $\mathbf{A}$ is Schur-stable; (b) $\mathbf{w}_{t}$ and $z_{t}$ are i.i.d. centered sub-Gaussian with variance proxy $\mathbf{\Sigma}_{w}$ and $\sigma_{z}$, respectively; (c) $\mathbf{u}_{t}\overset{\text{i.i.d.}}{\sim}{Unif}\left( {\{{- 1},{+ 1}\}}^{p} \right)$.

Under Assumption 1, we derive a bound on sample complexity and an estimation error of in Theorem 4. We note the following fact regarding the stability condition. According to Gelfand's formula, for all $\rho > {\rho{({\mathbf{A}})}}$, the quantity ${\phi{({\mathbf{A}},\rho)}}:={\sup_{k \in {\mathbb{Z}}_{+}}{({{\|{\mathbf{A}}^{k}\|}/\rho^{k}})}}$ is finite. Hence, if ${\rho{({\mathbf{A}})}} < 1$, for all $\rho \in {({\rho{({\mathbf{A}})}},1)}$, we have ${\|{\mathbf{A}}^{k}\|} \leq {\phi{({\mathbf{A}},\rho)}\rho^{k}}$ for all $k \in {\mathbb{Z}}_{+}$. A proof is shown in the appendix.

### Theorem 4

Under Assumption 1, let ${\{{(\mathbf{u}_{t},r_{t})}\}}_{t = 0}^{H}$ be a single trajectory of action-reward pairs collected from the system. For given $\delta \in {}$, suppose

With probability at least $1 - \delta$, we have ${\|{\hat{\mathbf{G}} - \mathbf{G}}\|}_{F} \lesssim$

for $\Lambda_{w}^{(L)}:={\sum_{k = 0}^{L - 1}\sqrt{\lambda_{\max}{({\mathbf{C}\mathbf{A}^{k}\mathbf{\Sigma}_{w}{(\mathbf{A}^{k})}^{\top}\mathbf{C}^{\top}})}}}$.

The proof of Theorem 4 is presented in the appendix. The recent work Sattar et al., 2025b shows that such a randomized design yields an estimation error bound of order $\overset{\sim}{\mathcal{O}}{({1/\sqrt{\deltaH}})}$ with probability at least $1 - \delta$. In this work, we sharpen this guarantee by exploiting the sub-Gaussian structure of the noise processes, obtaining an improved bound of order $\overset{\sim}{\mathcal{O}}{(\sqrt{{\log{({1/\delta})}}/H})}$ with probability at least $1 - \delta$.

The first term in our error bound corresponds to the approximation error because we use only $L$ Markov parameters to reconstruct the reward function. It decays exponentially with $L$ when the latent dynamics is strictly stable because the norm of Markov parameters decreases exponentially. The second term corresponds to the error due to noisy reward model and noisy latent dynamics update. This term depends linearly on the noise variance proxies.

The sample complexity in Theorem 4 scales as $\overset{\sim}{\mathcal{O}}{({p^{2}L^{2}})}$, which is optimal in the dimension of Markov parameters $p^{2}$. In contrast, the sample complexity in Sattar et al., 2025b scales as $\overset{\sim}{\mathcal{O}}{({p^{4}L^{3}})}$. The reason for this improvement is the choice of inputs ${\mathbf{u}}_{t}\overset{\text{i.i.d.}}{\sim}{Unif}\left( {\{{- 1},{+ 1}\}}^{p} \right)$ which leads to better persistence of excitation. Secondly, the error bound in Theorem 4 depends on the failure probability $\delta$ through $\log{({1/\delta})}$. This is significantly better than the $1/\delta$ dependence in Sattar et al., 2025b which considers a setting where noise processes can be heavy-tailed. The sub-Gaussian noise assumption in this paper allows using better concentration arguments, such as self-normalized bounds for martingales and Freedman's inequality, to obtain optimal dependence on the failure probability.

## Regret Analysis

In this section we prove Theorem 3. Additional details and proofs of intermediate results are deferred to the appendix. Recall the definition of regret . From Proposition 1 and Equation, we obtain

where ${\mathbf{u}}_{{H + 1}:T}^{\pi}$ is the optimized action sequence which maximizes. For the purpose of analysis, let ${\overset{\sim}{\mathbf{u}}}_{{H + 1}:T}$ be an action sequence that maximizes Equation with true parameters under the constraint ${\overset{\sim}{\mathbf{u}}}_{t} \in {\{{- 1},{+ 1}\}}^{p}$ for $t = {{H + 1},\ldots,T}$. Then, we decompose the regret as follows:

Intuitively, $R_{1,T}$ captures the sub-optimality between the full-time horizon and the commit-phase horizon, $R_{2,T}$ captures the sub-optimality between the true and estimated dynamics, and finally $R_{3,T}$ captures the error from parameter estimation. We analyze these three terms in detail in §5.1 and §5.2.

### Upper Bounding $R_{1,T}$

The term $R_{1,T}$ quantifies the loss from truncating the horizon at $H$, capturing both short-term dependencies within the exploration phase and long-term dependencies between exploration and commit phases through the dynamics.

### Proposition 5

Let $\rho \in {({\rho{(\mathbf{A})}},1)}$ be given. Then

for $\alpha = {1 + \frac{\phi{(\mathbf{A},\rho)}\rho}{1 - \rho}}$, $\beta = {\frac{\phi{(\mathbf{A},\rho)}\rho}{{({1 - \rho})}^{2}} + 1}$, and $\kappa = {\max{\{{\|\mathbf{B}\|},{\|\mathbf{C}\|}\}}}$.

The proof of Proposition 5 is deferred to the appendix. Note that the upper bound in 5 depends linearly on $H$, implying that the available reward grows linearly in time horizon. There is also a second term, a constant term independent of $H$. The coefficients $\alpha$ and $\beta$ depending on the stability of the state dynamics $\mathbf{A}$, and can be understood as effective memory capacity Kumar et al.,. The first term arises from to short-term dependencies within the exploration-phase. The second term is related to long-term dependencies which, due to stability, do not depend on the horizon.

### Upper Bounding $R_{2,T}$ and $R_{3,T}$

The terms $R_{2,T}$ and $R_{3,T}$ both depend on the estimation error $\epsilon$ and the truncation error $\rho^{L}$, and their bounds are given in the following proposition.

### Proposition 6

Let $\rho \in {({\rho{(\mathbf{A})}},1)}$ be given and $\epsilon > 0$ be the high-probability parameter estimation error, i.e., ${\|{\mathbf{G} - \hat{\mathbf{G}}}\|}_{F} \leq \epsilon$. Then, with high probability,

where $\kappa = {\max{\{{\|\mathbf{B}\|},{\|\mathbf{C}\|}\}}}$ and $\gamma_{L} = \frac{\phi{(\mathbf{A},\rho)}\rho^{L}}{1 - \rho}$.

The proof of Proposition 6 is deferred to the appendix. We can observe that the bound depends on the length of commit-phase $T - H$, the estimation error $\epsilon$, and the truncation error $\rho^{L}$.

### Final Regret Analysis

Finally, combining Propositions 5 and 6 yields the following high-probability bound:

From Theorem 4, we can take $\epsilon \lesssim \sqrt{\frac{\log{({1/\delta})}}{H - L}}$ with probability at least $1 - \delta$. Optimizing over $H$ gives $H = {\overset{\sim}{\mathcal{O}}{(T^{2/3})}}$, and with $L = {\Theta{({\log T})}}$ we obtain the high-probability regret bound ${R_{T}{(\pi)}} = {\overset{\sim}{\mathcal{O}}{(T^{2/3})}}$. Note that we define regret to be the expected cumulative rewards, where expectation is taken both over actions (in the exploration phase) and noise processes. However, we still have a high-probability bound on the regret because the estimation error bound holds with high probability.

## Numerical Experiments

Figure 2: Each curve shows a mean over 20 experiments, with shaded regions indicating ± 1 standard deviation. (a) Expected cumulative reward under the oracle benchmark, approximated by semidefinite relaxation with Goemans-Williamson rounding (SDP+GW) and by the sign-iteration method (SignIter). (b) The regret of the explore-then-commit algorithm measured against the SDP+GW oracle benchmark, compared with the theoretical $\overset{\sim}{\mathcal{O}}{(T^{2/3})}$ rate. (c)–(d) Relative error of Markov parameter estimation for different truncation lengths L, under systems with spectral radii ρ (A) = 0.1 and ρ (A) = 0.9.

In this section, we present numerical experiments with synthetic data. To obtain tractable solutions to and and analyze sub-optimality, we investigate two methods: (i) a semidefinite relaxation combined with Goemans-Williamson random hyperplane rounding, and (ii) a heuristic sign-iteration method. The code for experiments can be found in

### SDP Relaxation and Rounding

Our problem is to maximize a quadratic form ${\mathbf{x}}^{\top}{\mathbf{W}}{\mathbf{x}}$ for some symmetric ${\mathbf{W}} \in {\mathbb{R}}^{n \times n}$ over ${\mathbf{x}} \in {\{{- 1},1\}}^{n}$, which is equivalent to

Dropping the rank constraint yields the semidefinite relaxation, which we solve using the Mosek solver ApS,.

To obtain a feasible binary matrix from a solution $\mathbf{X}$ to the relaxed problem, we apply Goemans-Williamson (GW) random hyperplane rounding algorithm Goemans and Williamson,: factor ${\mathbf{X}} = {{\mathbf{V}}^{\top}{\mathbf{V}}}$, sample ${\mathbf{r}} \sim {\mathcal{N}{(0,{\mathbf{I}}_{n})}}$, and set a vector

where ${\mathbf{v}}_{i}$ is the $i$th column vector of $\mathbf{V}$. Then the matrix ${\mathbf{x}}{\mathbf{x}}^{\top}$ is rank-one and feasible . In practice, we repeat the rounding multiple times and keep the best value of ${\mathbf{x}}^{\top}{\mathbf{W}}{\mathbf{x}}$. We will hereafter refer to this method as SDP+GW.

For MaxCut problems, SDP+GW achieves an $\alpha$-approximation algorithm with $\alpha \approx 0.87856$. While our objective is not exactly MaxCut, we derive a similar lower bound which depend on $\mathbf{W}$ (see the appendix).

### Sign-Iteration Method

As an alternative to relaxation and rounding, we also consider a heuristic method called *sign-iteration* (henceforth SignIter) to maximize ${\mathbf{x}}^{\top}{\mathbf{W}}{\mathbf{x}}$ over ${\mathbf{x}} \in {\{{- 1},{+ 1}\}}^{n}$. Starting from a random ${\mathbf{x}}^{}$, the update is

and the procedure repeats until convergence or a maximum number of iterations. To mitigate dependence on initialization, the method is run multiple times and the best objective value is returned.

### Experimental Evaluation of Regret

We consider a simple latent dynamics and reward function specified by

We set the noise processes to be Gaussian with variances $\mathbf{\Sigma}_{w} = {{(0.01)}^{2}{\mathbf{I}}_{3}}$ and $\sigma_{z} = 0.01$. To select the exploration and truncation lengths, we perform a grid search to determine constants $c_{1},c_{2}$ in $H = {c_{1}T^{2/3}}$ and $L = {c_{2}{\log T}}$, calibrated at $T = 1500$. These constants were then fixed and applied across all regret experiments.

We ran the ETC algorithm under this setup, repeating each experiment $20$ times with different noise seeds. Regret was computed using the two benchmarks described in §6.1 and §6.2. As shown in Figure 2(a), SDP+GW consistently attains higher benchmark values than SignIter, indicating that the latter rarely approaches the true optimum. We therefore adopt the SDP+GW benchmark as the reference for regret.

Figure 2(b) reports regrets measured against this benchmark. The SDP+GW regret grows slowly and closely follows the $\overset{\sim}{\mathcal{O}}{(T^{2/3})}$ rate, consistent with our theoretical analysis. In contrast, the SignIter regret increases much more rapidly, nearly linearly in $T$, demonstrating that the heuristic commit phase is substantially suboptimal relative to the SDP+GW benchmark.

### Parameter Estimation

In this section, we show that the parameters are estimated effectively. We generate random instances with $n = 5$, $p = 3$, and Schur-stable $\mathbf{A}$ (scaled from i.i.d. $\mathcal{N}{(0,{1/n})}$ entries), with ${\mathbf{B}},{\mathbf{C}}$ similarly and noise levels $\mathbf{\Sigma}_{w} = {{(0.05)}^{2}{\mathbf{I}}_{n}}$, $\sigma_{z} = 0.05$. We study the estimation error of Markov parameters for two spectral radii, ${\rho{({\mathbf{A}})}} = 0.1$ and ${\rho{({\mathbf{A}})}} = 0.9$, by repeating each experiment 20 times with different noise seeds.

Figures 2(c) and 2(d) show that the relative estimation error decreases with exploration length $H$. For small $\rho{({\mathbf{A}})}$, shorter truncation lengths $L$ yield smaller errors, while for large $\rho{({\mathbf{A}})}$ the trend reverses, reflecting a trade-off between memory of states and number of Markov parameters. We also observe a characteristic double-descent effect Nakkiran et al., as the regression problem transitions from under- to over-determined. For further discussion and derivations, see Sattar et al., 2025b and the appendix.

### Comparison of Practical Methods

To evaluate the performance of the two approaches, we compare them against the true optimum of the regret-benchmark problem. Since this optimization is NP-hard in general, we restrict to small instances ($n = 3$, $p = 2$, $T = {5,\ldots,16}$) where brute force is feasible. Both SDP+GW and SignIter are randomized, we vary the number of rounding trials ($r = {1,10,30}$) and repeat each experiment 20 times with different seeds.

Figure 3: Comparison between SDP+GW and SignIter to the true optimum from the brute force method.

Figure 3 shows SignIter becomes increasingly suboptimal as $T$ grows, even with more rounding trials. In contrast, SDP+GW consistently returns values very close to the brute-force optimum; even a single trial ($r = 1$) mostly outperforms all SignIter cases. These results indicate that SDP+GW is an effective and reliable method for the commit-phase optimization.

## Related Work

Our formulation is connected to, but fundamentally different , several classical bandit settings. Unlike classic multi-armed bandits (MAB), we consider continuous (or combinatorially many) actions and temporally correlated rewards. Many settings which generalize MAB to nonstationary rewards have been investigated, including restless bandits Whittle rotting bandits Levine et al. Seznec et al. recharging bandits Kleinberg and Immorlica blocking bandits Basu et al. decaying/rebounding bandits Heidari et al. Leqi et al. delay-dependent rewards Cella and Cesa-Bianchi and bandits with underlying state Khosravi et al.,. Most of these works consider finitely many discrete actions which affect rewards in a simple and uncorrelated manner, e.g. repeatedly playing the same action results in decayed or improved reward.

The linear bandit setting Abbasi-Yadkori et al., naturally models correlations between actions, but classically considers a static parameter, equivalent in our setting to a fixed but unknown state. The nonstationary linear bandit setting Russac et al., allows for drift, but requires bounded variation to provide meaningful regret guarantees. Recently, Trella et al., consider a nonstationary linear bandit with auto-regressive structure, but do not model any impact of past actions on the rewards. Closely related to our work in motivation, Clerici et al., study linear bandits with memory. Our setting differs in two regards: the state depends on all past actions, not just finitely many, and the actions affect the state linearly, leading to a quadratic dependence in the reward, rather than through sublinear powers of a covariance-like "memory matrix".

The structure of our reward function bears resemblance to both linear contextual bandits Lattimore and Szepesvári, and bilinear bandits Jun et al.,. Unlike these settings, our latent state is unobserved. Furthermore, unlike the contexutal setting, the state is affected by past actions; unlike for bilinear bandits, the state is influenced through to dynamics and cannot be chosen directly.

Our setting is also related to model-based reinforcement learning for linear dynamical systems Dean et al. Simchowitz Mania et al. Lale et al., 2020b; Lale et al., 2020a, with two key differences. First, classical models assume action-independent observations, whereas our rewards depend bilinearly on actions. Second, quadratic costs in prior work yield linear optimal policies, whereas our selection is NP-hard.

## Conclusion

We study a nonstationary bandit problem where rewards depend bilinearly on actions and latent states evolving under unknown linear dynamics. We propose an explore-then-commit algorithm that combines the system parameter estimation and an open-loop action optimization. Our analysis shows that the algorithm achieves $\overset{\sim}{\mathcal{O}}{(T^{2/3})}$ regret with high probability. To address the NP-hard commit-phase optimization, we employed semidefinite relaxation and a rounding scheme, demonstrating its effectiveness empirically.

A natural direction for future work is to move beyond open-loop policies toward adaptive strategies. The recent work Sattar et al., 2025a considers a related structure in control theory, studying an optimal control problem of minimizing quadratic cost under linear dynamics with bilinear observations. It shows that the optimal feedback policy is nonlinear in the estimated state, suggesting that extending open-loop analysis to feedback or closed-loop designs is both challenging and an important direction for future research.
