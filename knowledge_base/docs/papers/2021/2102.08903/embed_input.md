<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Provably Efficient Policy Optimization for Two-Player Zero-Sum Markov Games

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Policy-based methods with function approximation are widely used for solving two-player zero-sum games with large state and/or action spaces. However, it remains elusive how to obtain optimization and statistical guarantees for such algorithms. We present a new policy optimization algorithm with function approximation and prove that under standard regularity conditions on the Markov game and the function approximation class, our algorithm finds a near-optimal policy within a polynomial number of samples and iterations. To our knowledge, this is the first provably efficient policy optimization algorithm with function approximation that solves two-player zero-sum Markov games.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Two-player zero-sum Markov game is a popular setting with many applications, such as Go, StarCraft II, and poker. In this setting, the goal of player one is to find a policy that achieves the maximum reward against player two who plays optimally to minimize the reward in response to player one's policy.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy optimization methods are widely used for solving zero-sum games. These algorithms often constrain the policy in a parametric form, and compute the gradient of the cumulative reward with respect to the parameters using the policy gradient theorem or its variants to update the parameters iteratively. Due to its flexibility, a wide range of successful results are attained by policy optimization methods. For example, Lockhart et al. performed direct policy optimization against worst-case opponents and empirically demonstrate their effectiveness in Kuhn Poker and Goofspiel card game. Foerster et al. invented LOLA where each agent shapes the learning of other agents. It gave the highest average returns on the iterated prisoners' dilemma (IPD).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the large body of empirical work using policy optimization methods for two-player zero-sum Markov games, theoretical studies are very limited.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Can we design a provably efficient policy optimization algorithm with function approximation for two-player zero-sum Markov games with a large state-action space?*

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We answer the above question affirmatively. We summarize our contributions below.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Our contributions", "weight": 1.0} -->

We design a new, provably efficient policy optimization algorithm for two-player zero-sum Markov games based on the natural policy gradient (NPG) method. On a high level, our algorithm has the two-step style as in previous work on value-based algorithms for two-player zero-sum Markov games. In the Greedy step, we aim to find *a pair of policies* that approximately solves matrix games for a given value function, and in the Iteration step, we aim to update the value function upon the current policy. In contrast to their value-based algorithm where function approximation is used for value functions, our results are entirely policy-based. We only have *function approximation for policies*. Therefore, we need to tackle additional challenges which are absent in value-based algorithms.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Our contributions", "weight": 1.0} -->

First, in the Greedy step, the algorithms in requires solving two-player zero-sum matrix games *for every state* in a value-based manner. The computational complexity scales with the size of the state-action space, which can be infeasible. For finding the equilibria for state-wise matrix games, we employ policy-based methods whose sample complexity only scales with the complexity of the function class (e.g., feature dimension for linear function approximation) instead of the size of state-action space. Specifically, we design a subroutine that combines two-player policy gradients with the optimistic mirror descent (OMD) updates to solve the zero-sum matrix game in a computational and statistical efficient way.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Second, in the Iteration step, Perolat et al. used *Generalized Policy Iteration* to evaluate the value function while we only have function approximation for policies. We leverage recent developments on NPG in single-agent RL to update *policies* in this step and represent the value function using *policies* instead of explicitly storing the value function.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Third, technically, we incorporates policy-based methods into value-based schemes, and develop new perturbation analyses for policy-based methods, both of which may be of independent interest.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Theoretically, first, to illustrate the main idea of our algorithm, in Section 4, we study an idealized "population\" tabular Markov game setting where we can access the population quantities, including the true policy gradients and the Fisher information. We prove an $\overset{\sim}{O}\left( \frac{1}{T} \right)$ rate,^11^1$\overset{\sim}{O}( \cdot )$ hides logarithmic factors. where $T$ is the number of iterations. This result is interesting in its own right because this matches the rate in the single-agent RL setting. We further obtain an improved rate in the entropy-regularized setting.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Our contributions", "weight": 1.0} -->

We present our main algorithm and theoretical results in Section 5 where we study Markov games with a large state-action space, and log-linear policy parameterization is used for generalization. Instead of the idealized "population\" setting, we study the realistic online setting, where we can only access the model through interactions. We prove an $\overset{\sim}{O}\left( {\frac{1}{\sqrt{T}} + \frac{1}{N^{1/4}}} \right)$ rate where $T$ is the number of iterations and $N$ is the number of samples (interaction with the model). To our knowledge, this is the first quantitative analysis of online policy optimization methods with function approximation for two-player zero-sum Markov games.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Two-Player zero-sum Markov Games", "weight": 1.0} -->

In this paper, we consider the centralized setting where we can control both players in the training phase to learn good policies. we focus on infinite-horizon discounted two-player zero-sum Markov games, which can be described by a tuple $\mathcal{M} = {(\mathcal{S},\mathcal{A},\mathcal{P},r,\gamma)}$: a set of states $\mathcal{S}$, a set of actions $\mathcal{A}$, a transition probability $\mathcal{P}:{{\mathcal{S} \times \mathcal{A} \times \mathcal{A}}\rightarrow{\Delta{(\mathcal{S})}}}$, a reward function $r:{{\mathcal{S} \times \mathcal{A} \times \mathcal{A}}\rightarrow{\lbrack 0,1\rbrack}}$, and a discount factor $\gamma \in {\lbrack 0,1)}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Two-Player zero-sum Markov Games", "weight": 1.0} -->

We let $\sigma$ to be the initial state distribution and define policies as probability distributions over the action space: ${x,f} \in \mathcal{S}\rightarrow{\Delta{(\mathcal{A})}}$. ^22^2 For clarity we assume two players share the same set of actions, it is straight forward to generalize to the setting where two action sets are different. See Section 5.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Two-Player zero-sum Markov Games", "weight": 1.0} -->

we use distribution $\sigma$ as the optimization measure we use to train the policy and use distribution $\rho$ as the performance measure of our interest. We remark that these two separate measures are widely used in analyzing approximate dynamic programming and policy gradient. We overload notations and define $V^{x,f}{(\rho)}$ as the expected value function of interest, i.e. ${{V^{x,f}{(\rho)}} ≔ {{\mathbb{E}}_{s \sim \rho}V^{x,f}{(s)}}}.$

<!-- chunk {"id": "body-0017", "role": "body", "section": "Two-Player zero-sum Markov Games", "weight": 1.0} -->

In a two-player zero-sum Markov game, player one ($x$) wants to maximize the value function and the other player ($f$) wants to minimize it. We define the Markov game's state-action value function $Q^{x,f}:{{\mathcal{S} \times \mathcal{A} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$, the advantage function $A^{x,f}:{{\mathcal{S} \times \mathcal{A} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$, and the state visitation function $d_{s_{0}}^{x,f}:{\mathcal{S}\rightarrow{\lbrack 0,1\rbrack}}$ as

<!-- chunk {"id": "body-0018", "role": "body", "section": "Two-Player zero-sum Markov Games", "weight": 1.0} -->

where $s_{0} \in \mathcal{S}$ is an initial state, respectively. With the state visitation function at hand, we are prepared to introduce NPG for two-player zero-sum games which relies on the Fisher information matrix.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Two-Player zero-sum Markov Games", "weight": 1.0} -->

One important concept in RL is the Bellman operator. For two-player zero-sum Markov games and two behavior policies $x$ and $f$, we define ${\mathcal{P}_{x,f}{(\left. s^{\prime} \middle| s \right.)}} = {{\mathbb{E}}_{a \sim x{( \cdot |s)},b \sim f{( \cdot |s)}}\mathcal{P}{(\left.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Two-Player zero-sum Markov Games", "weight": 1.0} -->

${\mathcal{T}_{x}v} ≔ {\inf_{f}{\mathcal{T}_{x,f}v}}$, which is an asymmetric operator by letting $f$ to be optimal. ^33^3Here we focus on max player $x$ (see Eq. 3). If we replace $x$ by $f$, we will have an analogous notation for min player.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Two-Player zero-sum Markov Games", "weight": 1.0} -->

Perolat et al. introduced these operators as generalized counterparts of single agent RL. We are able to adopt the dynamic programming scheme only once the Bellman operators are introduced.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Two-Player zero-sum Markov Games", "weight": 1.0} -->

Since we are considering a learning problem, we need to collect samples from the environment. We assume we can stop and restart at any time. With this, we can have the following sampling oracle.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Episodic Sampling Oracle", "weight": 1.0} -->

For a fixed state-action distribution $\nu_{0}$, we can start from ${s_{0},a_{0},b_{0}} \sim \nu_{0}$, act according to any policy pair $(x,f)$, and terminate when desired. We obtain unbiased estimates of the *on policy* state-action distribution

<!-- chunk {"id": "body-0024", "role": "body", "section": "Episodic Sampling Oracle", "weight": 1.0} -->

which can be used for acquiring an unbiased $Q^{x,f}{(s,a,b)}$ where ${s,a,b} \sim \nu_{\nu_{0}}^{x,f}$. See for a sampler.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Episodic Sampling Oracle", "weight": 1.0} -->

This oracle essentially requires that we can terminate at any time and restart, therefore many real-world applications including games and physics simulation (e.g., OpenFOAM ) admit this oracle. This oracle is also used in the analysis (see Algorithm 1,3 and Assumption 6.3 therein).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Episodic Sampling Oracle", "weight": 1.0} -->

The oracle is essential in analysis, technically because policy gradient methods need to estimate the values. This is the same reason as in the single-agent setting. Moreover, we believe this sampling oracle is not a strong assumption: it only requires that we can terminate at any time and restart. This is much weaker than the generative model assumption. The generative model assumes that one can query *any* state-action pair where we only require we can restart from a fixed initial distribution.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Episodic Sampling Oracle", "weight": 1.0} -->

NE always exists for discounted two-player zero-sum Markov Games. In practice, we seek to find an approximate pair of NE instead of an exact solution. The goal of this paper is to output a policy $x$ that makes the metric

<!-- chunk {"id": "body-0028", "role": "body", "section": "Episodic Sampling Oracle", "weight": 1.0} -->

small where $\rho$ is some state distribution of interest. This metric measures the performance of $x$ against the worst-case $f$. If it is less than $\epsilon$, we call $x$ an one-sided $\epsilon$-approximate NE, ^44^4From an optimization perspective, the sampling complexity of finding a solution so that both the min and max player are approximate NE scales only twice as large as that in one-sided case, since we may apply algorithms with the roles switched. it has been used.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Function Approximation", "weight": 1.0} -->

This paper studies function approximation to generalize across a large state space in Section 5. To represent both behavior policies $x$ and $f$, we adopt a log-linear parameterization: for a coefficient vector $\theta \in {\mathbb{R}}^{d}$, the associated probability of choosing action $a$ under state $s$, $\pi_{\theta}{(\left. a \middle| s \right.)}$, is given by $\frac{\exp{({\theta^{\top}\phi_{s,a}})}}{\sum_{a^{\prime} \in \mathcal{A}}{\exp{({\theta^{\top}\phi_{s,a^{\prime}}})}}}$ where $\phi_{s,a}$ is a feature vector representation of $s$ and $a$. This parameterization has been used.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Problem-Dependent Quantities", "weight": 1.0} -->

The first problem-dependent quantity is used to measure the inherent dynamics of Markov games.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Warm-up: Population Algorithm for Tabular Case", "weight": 1.0} -->

We first introduce the population version algorithm for the tabular case with the exact Fisher information matrix and policy gradients. The algorithm is spiritually similar to fictitious play. We enforce $x,f$ to be tabular softmax parameterized by ${\xi,\theta} \in {\mathbb{R}}^{{|\mathcal{S}|} \times {|\mathcal{A}|}}$

<!-- chunk {"id": "body-0032", "role": "body", "section": "Parameterization", "weight": 1.0} -->

This algorithm can be viewed as a prototypical algorithm and in the subsequent section, we will generalize to the online setting. The pseudo-code is listed in Algorithm 1.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Parameterization", "weight": 1.0} -->

0: Approximate policy xK at Nash equilibrium
Run Algorithm 2 with As defined in Eq. 4 and returns xk(⋅|s) for every state s.
Algorithm 1 Population Two-Player NPG.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Parameterization", "weight": 1.0} -->

0: f0, g0′, x0, y0′ ∈ Unif (𝒜), $\beta = \frac{1}{{}_{}^{}}$, and As for s ∈ 𝒮.
0: Approximate optimal $\overline{x_{T^{\prime}}}$ for max player
play ft(⋅|s), observe As⊤xt(⋅|s).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Parameterization", "weight": 1.0} -->

Algorithm 2 Subroutine: OMD for tabular case

<!-- chunk {"id": "body-0036", "role": "body", "section": "Parameterization", "weight": 1.0} -->

In Algorithm 1, we perform $K$ outer loops and obtain a near-optimal $x$ and value function $V_{K}$. We note that this algorithm is asymmetric since our metric (Eq. 3) is only considering max player $x$ while taking the best response of min player $f$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Parameterization", "weight": 1.0} -->

Each outer iteration begins with a Greedy Step. For current $V_{k - 1}$, we aim to find approximate equilibrium ($x,f$) with which ${\mathcal{T}_{x,f}V} \approx {\mathcal{T}V_{k - 1}}$. This step is spiritually equivalent to finding minimax equilibrium of a matrix game for *every state $s$*. In intuition, this step helps to update $V_{k - 1}$ towards $V^{\ast}$ (cf. contraction Lemma).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Parameterization", "weight": 1.0} -->

Let us take a closer look at Greedy Step. Consider an approximate two-player zero-sum matrix game: for every state $s \in \mathcal{S}$, we try to solve

<!-- chunk {"id": "body-0039", "role": "body", "section": "Parameterization", "weight": 1.0} -->

Here $A_{s}$ represents a set of matrices related to current value function $V_{k - 1}$. Instead of value-based approaches (PI, VI ) which are often inefficient, we solve these matrix games by policy-based methods for efficiency and sub-optimality guarantee. We adopt the *Optimistic Mirror Descent* for two players by assuming access to population quantities, e.g., $A_{s}\pi$ in Eq. 4. Note that each ${A_{s}{(a,b)}} \in {\lbrack 0,\frac{1}{1 - \gamma}\rbrack}$ because $V_{k - 1} \in {\lbrack 0,\frac{1}{1 - \gamma})}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Parameterization", "weight": 1.0} -->

We perform simultaneous updates for $T^{\prime}$ iterations in Algorithm 2 to minimize the following terms,

<!-- chunk {"id": "body-0041", "role": "body", "section": "Parameterization", "weight": 1.0} -->

Suppose two infs are achieved at $f^{\ast}$ and $x^{\ast}$ respectively.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Parameterization", "weight": 1.0} -->

After obtaining $x^{k}$ from Greedy Step, the Iteration Step aims to evaluate the value function while fixing $x = x^{k}$. We run $T$ updates to find $f^{\ast} = {\arg{\min_{f}V^{x,f}}}$. In the competitive multi-agent RL literature, this step is equivalent to finding the *best response* of min player (namely, $f^{\ast}$) when fixing $x = x^{k}$. The intuition is that when the max player's policy is very close to its optimal policy at NE and $f$ takes $f^{\ast}$, their accumulative value function is also close to $V^{\ast}$ at NE. This step can be viewed as running NPG for a single-agent RL problem.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Parameterization", "weight": 1.0} -->

The following theorem gives the performance guarantee for Algorithm 1.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Extension: Entropy regularization", "weight": 1.0} -->

Following, we give an extension of entropy-regularized NPG in the Iteration Step for Algorithm 1. Denote $\tau$ as the regularization term, the entropy regularized value function is formulated as

<!-- chunk {"id": "body-0045", "role": "body", "section": "Extension: Entropy regularization", "weight": 1.0} -->

Therefore, the regularized problem and the original problem are close when $\tau$ is small.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Extension: Entropy regularization", "weight": 1.0} -->

NPG methods with entropy regularization. Let ${\eta = \frac{1 - \gamma}{\tau}},$ we have the NPG update rule

<!-- chunk {"id": "body-0047", "role": "body", "section": "Extension: Entropy regularization", "weight": 1.0} -->

The following theorem shows the performance improvement over Theorem 1.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Online Algorithm with Function Approximation", "weight": 1.0} -->

In this section, we extend Algorithm 1 to the realistic online setting with function approximation, in which the parameterization we adopt is defined in Section 3.2. In this setting, we only observe samples (instead of the population quantities in Section 4). The pseudo-code is listed in Algorithm 3.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Online Algorithm with Function Approximation", "weight": 1.0} -->

To obtain estimates of quantities, we adopt the episodic sampling oracle (cf. Section 3) to provide transition tuples for estimating $A_{s}{(a,b)}$ in Greedy Step (cf. Eq. 4). This sampling oracle is also used in the Iteration Step to estimate value functions and gradients. See Appendix C for more details about how we use the sampling oracle.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Online Algorithm with Function Approximation", "weight": 1.0} -->

In Section 2, we have pointed out that our algorithm has a smaller sample complexity of $O\left( \epsilon^{- 6} \right)$ comparing to $O\left( \epsilon^{- 12.5} \right)$. As for the computational complexity, we remark that we only need projecting onto an $L_{2}$-norm ball in Algorithm 3, 4, which has the same time complexity as computing the gradient (linear in the dimension of $\theta$), so our algorithms are computationally efficient.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Online Algorithm with Function Approximation", "weight": 1.0} -->

Now we describe our algorithm. Specifically, we let $\xi$ and $\theta$ be parameters of $x$ and $f$, respectively. ^66^6We assume that the two players share the same parameter set only for clarity. We only need some minor modifications in the analysis to extend our results to the setting where two opposing players have different capabilities. Specifically, we only need to treat $W$ (norm-bound of updates), $D$ (regularity condition on features), and $\eta$ separately for each agent. The output and motivation of the Greedy Step and the Iteration Step are analogous to those in Algorithm 1. In both steps, we need to take sample-based NPG updates which are forced to be constrained in a convex set $\mathcal{W} = {\{ w:{{\| w\|}_{2} \leq W}\}}$ for analysis. From now, we denote $W$ as the bound of this norm-constrained convex set where each NPG update lies.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Online Algorithm with Function Approximation", "weight": 1.0} -->

Again, we first discuss the Greedy Step whose pseudo-code is listed in Algorithm 4. Our goal is still to obtain a near-optimal $x^{k}$ with respect to $\mathcal{T}V_{k - 1}$. Algorithm 4 is similar to Algorithm 2 in spirit. The main difference is that we use a sample-based NPG update rule for both $x$ and $f$. Ideally, we wish to find simultaneous updates $w_{f}^{\ast}$ and $w_{x}^{\ast}$ for the players. Both are minimizers of quadratic loss

<!-- chunk {"id": "body-0053", "role": "body", "section": "Online Algorithm with Function Approximation", "weight": 1.0} -->

After obtaining $x^{k}$ from the Greedy Step, we adapt NPG updates (Eq. 7) in Algorithm 1 to the online setting.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Online Algorithm with Function Approximation", "weight": 1.0} -->

Denote $\nu^{t} = \nu_{\nu_{0}}^{x,f^{t}}$ for simplicity. Ideally, NPG update in the Iteration Step takes the form

<!-- chunk {"id": "body-0055", "role": "body", "section": "Online Algorithm with Function Approximation", "weight": 1.0} -->

We perform sample-based quadratic loss minimization, which shares similarity with the former step: it takes $N$ steps of *projected gradient descent* to return an approximate update.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Online Algorithm with Function Approximation", "weight": 1.0} -->

Now we state our main theorem.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Online Algorithm with Function Approximation", "weight": 1.0} -->

Run Algorithm 4 returns xk with T′ iterations.
Sample s, a, b ∼ νt, then obtain Q̂ (s,a,b) using the sampling oracle.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Online Algorithm with Function Approximation", "weight": 1.0} -->

0: $\overline{x_{T^{\prime}}}$ as average of {xt}, t ∈ [T′]
min player: Initialize w0 = 0. Sample s ∼ σ(s), a ∼ xt(⋅|s), b ∼ ft(⋅|s), s′ ∼ 𝒫(⋅|s,a,b), b′ ∼ ft(⋅|s), observe:gn = [r (s,a,b) + γ Vk − 1 (s′)] ⋅ (∇θlog ft (b|s)−∇θlog ft (b′|s)). Update: wn + 1 = Proj𝒲 [wn − 2 α′ ⋅ (wn⊤ ∇θlog ft (b|s) ∇θlog ft (b|s)−gn)]. ${\hat{w}}^{t} = {\frac{1}{N^{\prime}}{\sum_{n = 1}^{N^{\prime}}w_{n}}}$. max player: Initialize w0 = 0.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Online Algorithm with Function Approximation", "weight": 1.0} -->

Sample s ∼ σ(s), a ∼ xt(⋅|s), b ∼ ft(⋅|s), s′ ∼ 𝒫(⋅|s,a,b), a′ ∼ xt(⋅|s), observe:gn = [r (s,a,b) + γ Vk − 1 (s′)] ⋅ (∇ξlog xt (a|s)−∇ξlog xt (a′|s)). Update: wn + 1 = Proj𝒲 [wn−2 α′ ⋅ (wn⊤ ∇ξlog xt (a|s) ∇ξlog xt (a|s)−gn)]. ${\hat{w}}^{t} = {\frac{1}{N^{\prime}}{\sum_{n = 1}^{N^{\prime}}w_{n}}}$. Algorithm 4 Online Greedy Step with Function-Approx

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper gave the first quantitative analysis of policy gradient methods for general two-player zero-sum Markov games with function approximation. We quantified the performance gap of the output policy in terms of the number of iterations, number of samples, concentrability coefficients, and approximation error. An interesting direction is to extend our results to more advanced PG methods such as PPO.
