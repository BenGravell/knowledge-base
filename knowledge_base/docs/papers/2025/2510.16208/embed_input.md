<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Explore-then-Commit for Nonstationary Linear Bandits with Latent Dynamics

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study a nonstationary bandit problem where rewards depend on both actions and latent states, the latter governed by unknown linear dynamics. Crucially, the state dynamics also depend on the actions, resulting in tension between short-term and long-term rewards. We propose an explore-then-commit algorithm for a finite horizon T. During the exploration phase, random Rademacher actions enable estimation of the Markov parameters of the linear dynamics, which characterize the action-reward relationship. In the commit phase, the algorithm uses the estimated parameters to design an optimized action sequence for long-term reward. Our proposed algorithm achieves tildeO(T^(2/3)) regret. Our analysis handles two key challenges: learning from temporally correlated rewards, and designing action sequences with optimal long-term reward. We address the first challenge by providing near-optimal sample complexity and error bounds for system identification using bilinear rewards. We address the second challenge by proving an equivalence with indefinite quadratic optimization over a hypercube, a known NP-hard problem. We provide a sub-optimality guarantee for this problem, enabling our regret upper bound.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Lastly, we propose a semidefinite relaxation with Goemans-Williamson rounding as a practical approach.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many application domains, like personalized recommendations or online advertising, require sequential decision-making under uncertainty. Classical bandit algorithms address the trade-off between reducing uncertainty and optimizing performance in environments where rewards do not depend on the algorithm's past decisions. Many real world systems exhibit temporal dependencies -- actions influence not only immediate reward, but also the future state of the environment Schedl et al.,. This paper studies such a setting where decisions propagate through latent dynamics, leading to correlations that fundamentally change both how to learn and how to act optimally.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We study a nonstationary bandit problem in which reward depends *bilinearly* on the *current action* and an *unobserved latent state* that evolves according to a stable linear dynamical system. Formally,

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

where ${\mathbf{A}},{\mathbf{B}},{\mathbf{C}}$ are unknown matrices, ${\mathbf{u}}_{t}$ is a bounded action chosen by the learner, ${\mathbf{w}}_{t},z_{t}$ are random noise processes, and ${\mathbf{x}}_{t}$ is the latent state, at time $t \geq 0$. Unlike classical multi-armed bandits with i.i.d. rewards, here actions not only determine immediate payoffs but also propagate through the state dynamics, creating temporal correlations in rewards, and making parameter estimation and optimal action sequence search significantly more challenging.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We observe that the problem can be resolved in the following ways. The issue of temporal correlation to estimate unknown parameters is addressed by improving upon recent results from system identification Sattar et al., 2025b. While the state-space parameters may not be identifiable from the observed rewards (without additional assumptions on ${\mathbf{A}},{\mathbf{B}},{\mathbf{C}}$), it is possible to obtain high-probability bounds on the estimation error for the *Markov parameters*, which characterize the action-reward relationship. In order to obtain an optimal long-term reward, we show that it is sufficient to use only this action-reward representation. In particular, selecting an optimal action sequence is equivalent to solving an indefinite quadratic problem over a hypercube, where the quadratic function is defined in terms of the Markov parameters.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Combining these two insights, we propose an *explore--then--commit* (ETC) algorithm. In the exploration phase, the learner applies random Rademacher actions to estimate the system's Markov parameter. In the commit phase, it commits to an action sequence which is a solution to an indefinite quadratic optimization problem. We show that, with high probability, this algorithm achieves sublinear regret, scaling as $\overset{\sim}{\mathcal{O}}{(T^{2/3})}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our setting bears relation to several other nonstationary bandits, including restless bandits Whittle rebounding bandits Leqi et al. and bandits with underlying state Khosravi et al. to name a few (see §7 for further discussion). Key novelties of our setting include that states can be of arbitrary dimension, the evolution can depend on interactions between dimensions (i.e., the matrix $\mathbf{A}$ need not be diagonal), and actions directly affect states in a potentially correlated manner (through the matrix $\mathbf{B}$). Furthermore, unlike many multi-armed bandit settings, we consider a continuous action space. Our problem also bears relation to model-based reinforcement learning for linear dynamics Dean et al. Simchowitz Mania et al. Lale et al., 2020b; Lale et al., 2020a, but the reward differs and provides only partial information about the underlying state.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Framework: We propose a novel nonstationary bandit problem in which the action affects both the current reward (through a bilinear interaction) as well as the future rewards (through a latent state).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Algorithm: We propose an explore-then-commit algorithm for our bandit problem. After exploration with random Rademacher actions, we estimate the Markov parameters which characterize the action-reward relationship. We then commit to an optimized action sequence obtained by solving a semidefinite relaxation of indefinite quadratic optimization over a hypercube --- a known NP-hard problem.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Estimation: We provide near-optimal sample complexity and estimation error bounds for learning Markov parameters. Specifically, in terms of the exploration length $H$, our error rate scales as $\overset{\sim}{\mathcal{O}}{({1/\sqrt{H}})}$, and we require $H \gtrsim {\overset{\sim}{\mathcal{O}}{(d_{M})}}$, where $d_{M}$ is the dimension of unknown Markov parameters.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Regret: We prove an upper bound on regret scaling as $\overset{\sim}{\mathcal{O}}{(T^{2/3})}$, and additionally provide a sub-optimality guarantee for the semidefinite relaxation with the Goemans-Williamson rounding approach.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Organization", "weight": 1.0} -->

§2 formalizes the model and the regret benchmark, defines the action set, and discuss the computational difficulty of the problem. §3 introduces the ETC algorithm and its regret guarantee. §4 presents our parameter estimation results with sample complexity and error bounds. §5 discuss our regret analysis. §6 presents numerical experiments. §7 shows related work to this paper, and §8 concludes the paper.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Organization", "weight": 1.0} -->

Notations: We use boldface lowercase/uppercase letters to denote vectors/matrices. The $\ell_{2}$-norm and $\ell_{\infty}$-norm of a vector $\mathbf{x}$ are denoted by $\left\| {\mathbf{x}} \right\|_{2}$ and $\left\| {\mathbf{x}} \right\|_{\infty}$, respectively. The spectral radius, the spectral norm, and the Frobenius norm of a matrix $\mathbf{X}$ are denoted by ${\rho{({\mathbf{X}})}},\left\| {\mathbf{X}} \right\|$, and $\left\| {\mathbf{X}} \right\|_{F}$, respectively.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Organization", "weight": 1.0} -->

The largest and smallest eigenvalue of a square matrix $\mathbf{X}$ are denoted by $\lambda_{\max}{({\mathbf{X}})}$ and $\lambda_{\min}{({\mathbf{X}})}$. The operation $\otimes$ denotes the Kronecker product. We use $\gtrsim$ and $\lesssim$ for inequalities that hold up to an absolute constant factor. The notation $\overset{\sim}{\mathcal{O}}$ hides constants and logarithmic terms. Lastly, we use $\mathbf{0}_{d}$ and $\mathbf{0}_{m \times n}$ to denote the zero vector in ${\mathbb{R}}^{d}$ and the zero matrix in ${\mathbb{R}}^{m \times n}$, respectively.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We consider a nonstationary stochastic bandit problem with controlled^11^1i.e., the state is nontrivially influenced by the actions latent dynamics and a bilinear reward model. At each round $t = {0,1,\ldots,T}$, the learner selects an action ${\mathbf{u}}_{t}$ from a bounded action set $\mathcal{U} \subseteq {\mathbb{R}}^{p}$, and receives a reward $r_{t} \in {\mathbb{R}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

More specifically, the reward is bilinear in the latent state ${\mathbf{x}}_{t} \in {\mathbb{R}}^{n}$ and the action ${\mathbf{u}}_{t} \in \mathcal{U}$, whereas the latent state evolves according to a linear dynamical system, as defined, where ${\mathbf{A}},{\mathbf{B}},{\mathbf{C}}$ are unknown matrices of appropriate dimensions, and ${\mathbf{w}}_{t}$, $z_{t}$ are random zero-mean noise processes. Without loss of generality, we assume ${\mathbf{x}}_{0} = \mathbf{0}_{n}$. Throughout, we assume $\mathbf{A}$ is Schur-stable, that is, ${\rho{({\mathbf{A}})}} < 1$, and the noise processes are i.i.d.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Objective, Action Set, and Regret", "weight": 1.0} -->

Our objective is to maximize the expected cumulative reward ${\mathbb{E}}\left\lbrack {\sum_{t = 0}^{T}r_{t}} \right\rbrack$ over the horizon $T$, by choosing actions from a bounded set. For simplicity, we consider the action set to be a centered hypercube in ${\mathbb{R}}^{p}$. In other words, we choose

<!-- chunk {"id": "body-0020", "role": "body", "section": "Optimal Open-Loop Actions", "weight": 1.0} -->

In this section, we suppose that ${\mathbf{A}},{\mathbf{B}},{\mathbf{C}}$ are known, and show that the optimal action sequence is the solution to an indefinite quadratic optimization problem with $\ell_{\infty}$-norm constraint. By unrolling the latent state through, we have $r_{0} = z_{0}$, and for $t \geq 1$,

<!-- chunk {"id": "body-0021", "role": "body", "section": "Optimal Open-Loop Actions", "weight": 1.0} -->

Since ${\mathbf{w}}_{t}$ and $z_{t}$ have zero-mean, the expected cumulative reward is given by

<!-- chunk {"id": "body-0022", "role": "body", "section": "Optimal Open-Loop Actions", "weight": 1.0} -->

With these definitions, the optimal action sequence and the corresponding cumulative reward are given as follows. This cumulative reward is our regret baseline.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Combinatorial Actions", "weight": 1.0} -->

The problem is the maximization of an indefinite quadratic function over the hypercube. We show that it suffices to consider a discrete set of actions corresponding to the vertices of the hypercube,

<!-- chunk {"id": "body-0024", "role": "body", "section": "Combinatorial Actions", "weight": 1.0} -->

so that each coordinate of every action is restricted to $\pm 1$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Main Result: Explore-then-Commit", "weight": 1.0} -->

We propose an explore--then--commit (ETC) algorithm for minimizing regret tailored to bandits with latent linear dynamics and bilinear rewards. The ETC algorithm runs in two phases, *an exploration phase* and *a commit phase*. In §3.1, we describe the *exploration phase*, which consists in estimating the so-called *Markov parameters*^22^2The Markov parameters corresponding to the system are typically defined, for example in Sattar et al., 2025b, as the sequence of matrices ${\{{{\mathbf{C}}{\mathbf{A}}^{k}{\mathbf{B}}}\}}_{k \geq 0}$. of the system. In §3.2, we describe the *commit phase*, where the learner uses the estimated Markov parameters to formulate an open-loop optimization problem and design a sequence of actions for the remaining horizon.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Main Result: Explore-then-Commit", "weight": 1.0} -->

Finally, in §3.3, we state our main theoretical result: with appropriate choices of exploration and truncation lengths, the ETC algorithm achieves a regret of order $\overset{\sim}{\mathcal{O}}{(T^{2/3})}$. We summarize the overall procedure in Algorithm 1.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Main Result: Explore-then-Commit", "weight": 1.0} -->

1:Horizon T, exploration length H, truncation length L
3:For t = 0, …, H, play ut ∼ Unif ({−1, +1}p) and observe reward rt.
4:Find an estimate $\hat{\mathbf{G}}$ of the first L Markov parameters via least squares using {(ut,rt)}t = 0H as.
5:Construct ${\hat{\mathbf{S}}}_{T - H - 1} = {\frac{1}{2}{({{\hat{\mathbf{M}}}_{T - H - 1} + {\hat{\mathbf{M}}}_{T - H - 1}^{\top}})}}$ where MT − H − 1 is defined via $\hat{\mathbf{G}}$ as.
7:Find a sequence (uH + 1π,…,uTπ) that solves,

<!-- chunk {"id": "body-0028", "role": "body", "section": "Main Result: Explore-then-Commit", "weight": 1.0} -->

by (a) SDP relaxation with Goemans-Williamson rounding, or (b) sign-iteration method.
8:For t = H + 1, …, T, play utπ and observe reward rt.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Exploration Phase", "weight": 1.0} -->

In the exploration phase, the learner selects actions independently from the Rademacher distribution ${Unif}{\{{- 1},{+ 1}\}}^{p}$. This distribution satisfies the action constraint (see §2.3) and provides sufficient excitation of the system, ensuring that the Markov parameters can be consistently estimated Sattar et al., 2025b. Further discussion of persistence of excitation is deferred to the appendix.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Exploration Phase", "weight": 1.0} -->

The trajectory ${\{{({\mathbf{u}}_{t},r_{t})}\}}_{t = 0}^{H}$ collected in this phase is used to estimate the system's Markov parameters. Concretely, we form nonlinear regressors/features using the previous $L$ actions $({\mathbf{u}}_{t - 1},\ldots,{\mathbf{u}}_{t - L})$ together with the current action ${\mathbf{u}}_{t}$, and use linear regression to predict the current reward $r_{t}$. The least-squares solution gives an estimate of the first $L$ Markov parameters ${\{{{\mathbf{C}}{\mathbf{A}}^{k}{\mathbf{B}}}\}}_{k = 0}^{L - 1}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Exploration Phase", "weight": 1.0} -->

Since the matrix $\mathbf{A}$ is Schur-stable, the influence of terms beyond lag $L$ decays geometrically. Hence, it suffices to estimate only the first $L$ parameters. The details of the regression procedure and error analysis are deferred to §4.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Commit Phase", "weight": 1.0} -->

After exploration, the learner uses the estimated Markov parameters to construct an open-loop optimization problem aimed at maximizing the expected cumulative reward from $t = {H + 1}$ to $T$. Because the Rademacher actions and the noise processes are zero-mean, the theoretical objective will be

<!-- chunk {"id": "body-0033", "role": "body", "section": "Commit Phase", "weight": 1.0} -->

with ${\mathbf{S}}_{T - H - 1} = {{\mathbf{M}}_{T - H - 1} + {\mathbf{M}}_{T - H - 1}^{\top}}$ where ${\mathbf{M}}_{T - H - 1}$ is a block Toeplitz matrix with similar structure to Equation (see the appendix for derivation).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Commit Phase", "weight": 1.0} -->

Since the true parameters are unknown, we replace them with estimates from the exploration phase. Specifically, we form ${\hat{\mathbf{S}}}_{T - H - 1}$ by substituting the estimated blocks for ${\mathbf{C}}{\mathbf{A}}^{k}{\mathbf{B}}$ whenever $k < L$ and setting the blocks to $\mathbf{0}_{p \times p}$ for $k \geq L$, consistent with the Schur-stability of $\mathbf{A}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Commit Phase", "weight": 1.0} -->

The structure of this problem is identical to, but with estimated rather than true parameters. As noted in §2.3, the problem is NP-hard. We therefore rely on practical approaches to obtain tractable approximations, which will be discussed in §6.1 and §6.2.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Regret Guarantee", "weight": 1.0} -->

Our main result establishes that the ETC algorithm achieves sublinear regret with high probability.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Main Result: Parameter Estimation", "weight": 1.0} -->

In this section, we use the action-reward samples ${\{{({\mathbf{u}}_{t},r_{t})}\}}_{t = 0}^{H}$ from the exploration phase to estimate a map between the actions and rewards. Similar to Sattar et al., 2025b, we can estimate Markov parameters by regressing the rewards $r_{t}$ to an expression defined by the history of inputs ${\{{\mathbf{u}}_{\tau}\}}_{\tau \leq t}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Main Result: Parameter Estimation", "weight": 1.0} -->

In this paper, we provide improved sample complexity and error bounds, under the following assumption.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Regret Analysis", "weight": 1.0} -->

In this section we prove Theorem 3. Additional details and proofs of intermediate results are deferred to the appendix. Recall the definition of regret. From Proposition 1 and Equation, we obtain

<!-- chunk {"id": "body-0040", "role": "body", "section": "Regret Analysis", "weight": 1.0} -->

Intuitively, $R_{1,T}$ captures the sub-optimality between the full-time horizon and the commit-phase horizon, $R_{2,T}$ captures the sub-optimality between the true and estimated dynamics, and finally $R_{3,T}$ captures the error from parameter estimation. We analyze these three terms in detail in §5.1 and §5.2.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Upper Bounding $R_{1,T}$", "weight": 1.0} -->

The term $R_{1,T}$ quantifies the loss from truncating the horizon at $H$, capturing both short-term dependencies within the exploration phase and long-term dependencies between exploration and commit phases through the dynamics.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Upper Bounding $R_{2,T}$ and $R_{3,T}$", "weight": 1.0} -->

The terms $R_{2,T}$ and $R_{3,T}$ both depend on the estimation error $\epsilon$ and the truncation error $\rho^{L}$, and their bounds are given in the following proposition.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Final Regret Analysis", "weight": 1.0} -->

From Theorem 4, we can take $\epsilon \lesssim \sqrt{\frac{\log{({1/\delta})}}{H - L}}$ with probability at least $1 - \delta$. Optimizing over $H$ gives $H = {\overset{\sim}{\mathcal{O}}{(T^{2/3})}}$, and with $L = {\Theta{({\log T})}}$ we obtain the high-probability regret bound ${R_{T}{(\pi)}} = {\overset{\sim}{\mathcal{O}}{(T^{2/3})}}$. Note that we define regret to be the expected cumulative rewards, where expectation is taken both over actions (in the exploration phase) and noise processes. However, we still have a high-probability bound on the regret because the estimation error bound holds with high probability.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In this section, we present numerical experiments with synthetic data. To obtain tractable solutions to and and analyze sub-optimality, we investigate two methods: (i) a semidefinite relaxation combined with Goemans-Williamson random hyperplane rounding, and (ii) a heuristic sign-iteration method. The code for experiments can be found in

<!-- chunk {"id": "body-0045", "role": "body", "section": "SDP Relaxation and Rounding", "weight": 1.0} -->

Dropping the rank constraint yields the semidefinite relaxation, which we solve using the Mosek solver ApS,.

<!-- chunk {"id": "body-0046", "role": "body", "section": "SDP Relaxation and Rounding", "weight": 1.0} -->

To obtain a feasible binary matrix from a solution $\mathbf{X}$ to the relaxed problem, we apply Goemans-Williamson (GW) random hyperplane rounding algorithm Goemans and Williamson,: factor ${\mathbf{X}} = {{\mathbf{V}}^{\top}{\mathbf{V}}}$, sample ${\mathbf{r}} \sim {\mathcal{N}{(0,{\mathbf{I}}_{n})}}$, and set a vector

<!-- chunk {"id": "body-0047", "role": "body", "section": "SDP Relaxation and Rounding", "weight": 1.0} -->

where ${\mathbf{v}}_{i}$ is the $i$th column vector of $\mathbf{V}$. Then the matrix ${\mathbf{x}}{\mathbf{x}}^{\top}$ is rank-one and feasible. In practice, we repeat the rounding multiple times and keep the best value of ${\mathbf{x}}^{\top}{\mathbf{W}}{\mathbf{x}}$. We will hereafter refer to this method as SDP+GW.

<!-- chunk {"id": "body-0048", "role": "body", "section": "SDP Relaxation and Rounding", "weight": 1.0} -->

For MaxCut problems, SDP+GW achieves an $\alpha$-approximation algorithm with $\alpha \approx 0.87856$. While our objective is not exactly MaxCut, we derive a similar lower bound which depend on $\mathbf{W}$ (see the appendix).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Sign-Iteration Method", "weight": 1.0} -->

As an alternative to relaxation and rounding, we also consider a heuristic method called *sign-iteration* (henceforth SignIter) to maximize ${\mathbf{x}}^{\top}{\mathbf{W}}{\mathbf{x}}$ over ${\mathbf{x}} \in {\{{- 1},{+ 1}\}}^{n}$. Starting from a random ${\mathbf{x}}^{}$, the update is

<!-- chunk {"id": "body-0050", "role": "body", "section": "Sign-Iteration Method", "weight": 1.0} -->

and the procedure repeats until convergence or a maximum number of iterations. To mitigate dependence on initialization, the method is run multiple times and the best objective value is returned.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Experimental Evaluation of Regret", "weight": 1.0} -->

We consider a simple latent dynamics and reward function specified by

<!-- chunk {"id": "body-0052", "role": "body", "section": "Experimental Evaluation of Regret", "weight": 1.0} -->

We set the noise processes to be Gaussian with variances $\mathbf{\Sigma}_{w} = {{(0.01)}^{2}{\mathbf{I}}_{3}}$ and $\sigma_{z} = 0.01$. To select the exploration and truncation lengths, we perform a grid search to determine constants $c_{1},c_{2}$ in $H = {c_{1}T^{2/3}}$ and $L = {c_{2}{\log T}}$, calibrated at $T = 1500$. These constants were then fixed and applied across all regret experiments.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Experimental Evaluation of Regret", "weight": 1.0} -->

We ran the ETC algorithm under this setup, repeating each experiment $20$ times with different noise seeds. Regret was computed using the two benchmarks described in §6.1 and §6.2. As shown in Figure 2(a), SDP+GW consistently attains higher benchmark values than SignIter, indicating that the latter rarely approaches the true optimum. We therefore adopt the SDP+GW benchmark as the reference for regret.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Parameter Estimation", "weight": 1.0} -->

In this section, we show that the parameters are estimated effectively. We generate random instances with $n = 5$, $p = 3$, and Schur-stable $\mathbf{A}$ (scaled from i.i.d. $\mathcal{N}{(0,{1/n})}$ entries), with ${\mathbf{B}},{\mathbf{C}}$ similarly and noise levels $\mathbf{\Sigma}_{w} = {{(0.05)}^{2}{\mathbf{I}}_{n}}$, $\sigma_{z} = 0.05$. We study the estimation error of Markov parameters for two spectral radii, ${\rho{({\mathbf{A}})}} = 0.1$ and ${\rho{({\mathbf{A}})}} = 0.9$, by repeating each experiment 20 times with different noise seeds.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Parameter Estimation", "weight": 1.0} -->

Figures 2(c) and 2(d) show that the relative estimation error decreases with exploration length $H$. For small $\rho{({\mathbf{A}})}$, shorter truncation lengths $L$ yield smaller errors, while for large $\rho{({\mathbf{A}})}$ the trend reverses, reflecting a trade-off between memory of states and number of Markov parameters. We also observe a characteristic double-descent effect Nakkiran et al., as the regression problem transitions from under- to over-determined. For further discussion and derivations, see Sattar et al., 2025b and the appendix.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Comparison of Practical Methods", "weight": 1.0} -->

To evaluate the performance of the two approaches, we compare them against the true optimum of the regret-benchmark problem. Since this optimization is NP-hard in general, we restrict to small instances ($n = 3$, $p = 2$, $T = {5,\ldots,16}$) where brute force is feasible. Both SDP+GW and SignIter are randomized, we vary the number of rounding trials ($r = {1,10,30}$) and repeat each experiment 20 times with different seeds.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We study a nonstationary bandit problem where rewards depend bilinearly on actions and latent states evolving under unknown linear dynamics. We propose an explore-then-commit algorithm that combines the system parameter estimation and an open-loop action optimization. Our analysis shows that the algorithm achieves $\overset{\sim}{\mathcal{O}}{(T^{2/3})}$ regret with high probability. To address the NP-hard commit-phase optimization, we employed semidefinite relaxation and a rounding scheme, demonstrating its effectiveness empirically.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion", "weight": 1.5} -->

A natural direction for future work is to move beyond open-loop policies toward adaptive strategies. The recent work Sattar et al., 2025a considers a related structure in control theory, studying an optimal control problem of minimizing quadratic cost under linear dynamics with bilinear observations. It shows that the optimal feedback policy is nonlinear in the estimated state, suggesting that extending open-loop analysis to feedback or closed-loop designs is both challenging and an important direction for future research.
