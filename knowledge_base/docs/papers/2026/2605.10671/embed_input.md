<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Natural Policy Gradient as Doubly Smoothed Policy Iteration: A Bellman-Operator Framework

Topics include Policy gradients, Reinforcement learning, Bellman equations, Policy iteration, Learning, DSPI.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this work, we show that natural policy gradient, a core algorithm in reinforcement learning, admits an exact formulation as a smoothed and averaged form of policy iteration. Specifically, we introduce doubly smoothed policy iteration (DSPI), a Bellman-operator framework in which each policy is obtained by applying a regularized greedy step to a weighted average of past Q-functions. DSPI includes policy iteration, dual-averaged policy iteration, natural policy gradient, and more general policy dual averaging methods as special cases. Using only monotonicity and contraction of smoothed Bellman operators, we prove distribution-free global geometric convergence of DSPI. Consequently, standard natural policy gradient and policy dual averaging achieve an iteration complexity of O((1-gamma)^(-1)log((1-gamma)^(-1)epsilon^(-1))) for computing an epsilon-optimal policy, without modifying the MDP, adding regularization beyond the mirror map inherent in the update, or using adaptive, trajectory-dependent stepsizes. For the unregularized greedy case, corresponding to dual-averaged policy iteration, we also prove finite termination.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The same Bellman-operator framework further extends to discounted MDPs with linear function approximation and stochastic shortest path problems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the last decade, reinforcement learning (RL) has emerged as a principled framework for large-scale sequential decision making, with applications ranging from autonomous vehicles and robotics to large language models. Mathematically, RL problems are typically modeled as Markov decision processes (MDPs). The seminal work of showed that solving an MDP reduces to finding a fixed point of the Bellman equation. By leveraging key properties of the Bellman operator, most notably contraction and monotonicity, a range of principled algorithms have been developed, including value iteration (VI), policy iteration (PI), and their variants.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the modern era of sequential decision making, it was recognized that an MDP can be formulated as a continuous optimization problem over the policy space. From this perspective, the policy gradient (PG) method was introduced. Building on this viewpoint and further exploiting the geometry of the policy space, the natural policy gradient (NPG) method, along with more general approaches such as policy mirror ascent (PMA) and policy dual averaging (PDA), was developed. Over time, practical variants of these gradient-based methods, such as trust region policy optimization and proximal policy optimization, have become dominant approaches in large-scale applications.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The empirical success of NPG and its variants has motivated extensive theoretical work on their convergence properties. Existing approaches for studying NPG can be broadly categorized into two groups. One prominent line of work adopts a gradient-based optimization viewpoint, leveraging tools such as the policy gradient theorem, the performance difference lemma, the Polyak Łojasiewicz condition, and techniques from continuous optimization. A second line of work views NPG as an approximation of PI. Indeed, the original NPG paper \[24, Theorem 2\] observed that, as the stepsize approaches infinity, NPG recovers PI. Following this perspective, NPG has been analyzed as an approximation of PI by leveraging properties of the Bellman operator and separately bounding the approximation error.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite substantial progress, existing analyses still leave open a conceptual gap. The defining structural property of discounted MDPs is the $\ell_{\infty}$-norm contraction of the Bellman operator, which underlies the design and analysis of classical methods such as VI and PI. This property is not naturally visible when NPG is analyzed as a continuous optimization method over the policy space. Consequently, many optimization-based analyses either do not establish global geometric convergence or achieve it by introducing additional regularization into the MDP or the algorithm to induce curvature. In contrast, approaches that view NPG as an approximation of PI exploit Bellman operator properties and obtain distribution-free geometric convergence without additional regularization, but require stepsizes chosen adaptively based on the algorithm trajectory to control the approximation error. See Section 1.1 for further details.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

More fundamentally, a unified perspective connecting classical dynamic programming methods based on Bellman iteration, such as PI, with modern gradient-based methods, such as NPG and PDA, remains lacking at both the algorithmic and analytical levels. In this paper, we address this gap by introducing doubly smoothed policy iteration (DSPI), a unified framework that includes PI, dual-averaged PI, NPG, and PDA as special cases. This perspective enables a unified analysis that yields strong guarantees for a broad class of algorithms. We summarize our contributions below.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Doubly Smoothed Policy Iteration. We introduce DSPI, in which the policy is updated via a regularized greedy step with respect to a weighted average of past $Q$-functions. This structure admits a compact Bellman operator formulation (cf. Algorithm 2, Line 4). We show that DSPI captures a broad class of existing algorithms, including PI, dual-averaged PI, and, most notably, NPG and PDA. Crucially, for NPG and PDA, interpreting these gradient-based methods as smoothed and averaged variants of PI allows the updates to be expressed via the smoothed Bellman operator, thereby enabling a principled analysis based on its properties.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A Unified Convergence Analysis. We show that DSPI converges asymptotically whenever the stepsizes are non-summable. Moreover, under a constant stepsize, DSPI achieves distribution-free global geometric convergence. In particular,

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $V^{\pi_{0}}$, $V^{\pi_{k}}$, and $V^{\ast}$ denote the value functions of the initial policy, the $k$-th iterate, and an optimal policy, respectively, $\gamma$ is the discount factor, and $\beta$ is the constant stepsize. See Theorem 4.1 for details. As byproducts,

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

this result implies an iteration complexity of $\mathcal{O}{({{({1 - \gamma})}^{- 1}{\log{({{({1 - \gamma})}^{- 1}\epsilon^{- 1}})}}})}$ for NPG and PDA to achieve ${\|{V^{\pi_{k}} - V^{\ast}}\|}_{\infty} \leq \epsilon$ (cf. Theorem 4.3), matching the state of the art without requiring additional regularization of the MDP or the algorithm, or the use of adaptive stepsizes;

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

it also enables us to establish finite termination of dual-averaged PI; in particular, an iteration complexity of $\mathcal{O}{({mn{({1 - \gamma})}^{- 1}{\log{({({1 - \gamma})}^{- 1})}}})}$ for finding an optimal policy (cf. Theorem 4.6), where $n$ and $m$ denote the sizes of the state and action spaces, respectively.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, the algorithm and analysis extend to settings such as discounted MDPs with linear function approximation, where we obtain the same convergence rate up to a function approximation error (cf. Appendix C), and stochastic shortest path problems, where we establish analogous geometric convergence (cf. Appendix D).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Related Literature", "weight": 1.0} -->

Since we focus on the MDP setting rather than the model-free RL setting, we restrict our discussion below to PI and NPG, rather than results that broadly analyze actor--critic algorithms.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Related Literature", "weight": 1.0} -->

Policy Iteration. The PI method was first proposed. The global geometric convergence of PI was shown. The proof has two main steps: showing that the performance of the policies is monotonically improving, and leveraging the contraction property of the Bellman operator to establish a contractive recursion. This approach also inspires our analysis of DSPI. Beyond global geometric convergence, it was shown that PI can terminate in a finite number of iterations. The key property that enabled such strong results is that PI gradually eliminates sub-optimal actions. Such a property also plays a key role in showing the finite termination of dual-averaged PI in this work. Other variants of PI, including simplex PI, modified PI, and incremental PI, are analyzed.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Related Literature", "weight": 1.0} -->

Policy Gradient. The PG method was first proposed, which treats a weighted sum of the value function as a scalar objective and performs projected gradient ascent in the policy space. A comprehensive analysis of PG was carried out in and subsequent works. Beyond the setting of finite state-action space MDPs, PG methods for more general MDPs (e.g., continuous state-action spaces with potentially unbounded costs) have also been studied. Since the focus of this work is on NPG and more general PDA methods, we do not delve further into the literature on the convergence-rate analysis of vanilla PG.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Related Literature", "weight": 1.0} -->

Natural Policy Gradient. NPG, proposed, can be viewed as PG with a preconditioner. Alternatively, it can be interpreted as PMA or PDA, with the divergence-generating function chosen as the Shannon entropy. The majority of existing analyses of NPG suffer from at least one of the following limitations: lack of global geometric convergence; dependence on the initial distribution or a concentrability coefficient; additional regularization of the MDP or the algorithm; or reliance on adaptive stepsizes that depend on the policy trajectory. See Table 1 from Appendix A for more details. The only exception is, which provides the state-of-the-art analysis of NPG from a continuous optimization perspective^11^1The results in were developed for general PMA, which covers NPG as a special case., but their choice of stepsize depends on the Bellman error (also called the advantage gap) of the initial policy, which is not required in our result.

<!-- chunk {"id": "body-0019", "role": "body", "section": "The Bellman Equation and Policy Iteration", "weight": 1.0} -->

The key to solving an MDP lies in the Bellman equation. We next present the Bellman equations for policy evaluation and policy optimization. To facilitate the connection between PI and NPG developed later in this paper, we express these equations in terms of $Q$-functions.

<!-- chunk {"id": "body-0020", "role": "body", "section": "The Bellman Equation and Policy Iteration", "weight": 1.0} -->

Similarly, the optimal $Q$-function $Q^{\ast}$ is the unique solution to the Bellman optimality equation $Q = {\mathcal{H}{(Q)}}$, where $\mathcal{H}:{{\mathbb{R}}^{mn}\rightarrow{\mathbb{R}}^{mn}}$ is the Bellman optimality operator defined as

<!-- chunk {"id": "body-0021", "role": "body", "section": "The Bellman Equation and Policy Iteration", "weight": 1.0} -->

Moreover, once $Q^{\ast}$ is obtained, an optimal policy $\pi^{\ast}$ can be computed by choosing actions greedily with respect to $Q^{\ast}$. The operators $\mathcal{H}^{\pi}$ and $\mathcal{H}$ enjoy several useful properties. In particular, both are contraction mappings with respect to the $\ell_{\infty}$ norm with contraction factor $\gamma$, and are monotone in the sense that ${F{(Q_{1})}} \leq {F{(Q_{2})}}$ whenever $Q_{1} \leq Q_{2}$, where $F$ denotes either $\mathcal{H}^{\pi}$ or $\mathcal{H}$. One should not confuse the definition of monotonicity here with the notion of monotonicity in variational inequalities. These two properties enable the design and analysis of several classical algorithms, such as VI and PI.

<!-- chunk {"id": "body-0022", "role": "body", "section": "The Bellman Equation and Policy Iteration", "weight": 1.0} -->

When expressed in terms of $Q$-functions, the PI algorithm can be compactly written as

<!-- chunk {"id": "body-0023", "role": "body", "section": "The Bellman Equation and Policy Iteration", "weight": 1.0} -->

Note that (2.1) does not define a unique update. In particular, $\pi_{k + 1}$ can be any policy such that, when its associated Bellman operator $\mathcal{H}^{\pi_{k + 1}}$ is applied to the previous $Q$-function $Q^{\pi_{k}}$, the result coincides with applying the Bellman optimality operator to $Q^{\pi_{k}}$. In view of the definition of the Bellman operators, one concrete way to implement the PI update in (2.1) is

<!-- chunk {"id": "body-0024", "role": "body", "section": "The Bellman Equation and Policy Iteration", "weight": 1.0} -->

The global geometric convergence of PI is well established in the literature. The analysis proceeds in two main steps: using the monotonicity of the Bellman operators to show that the policies are monotonically improving, i.e., $Q^{\pi_{k}} \leq Q^{\pi_{k + 1}}$; using the contraction property of the Bellman operators to show that the convergence error ${\|{Q^{\ast} - Q^{\pi_{k}}}\|}_{\infty}$ admits a contractive recursion. For completeness, we provide an analysis of PI in Appendix B.1.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Natural Policy Gradient and Policy Dual Averaging", "weight": 1.0} -->

Since an optimal policy maximizes the value function $V^{\pi}{(s)}$ uniformly over all states $s$, solving an MDP is equivalent to solving an optimization problem over the policy space with the scalar objective ${V^{\pi}{(\rho)}}:={\sum_{s \in \mathcal{S}}{\rho{(s)}V^{\pi}{(s)}}}$, where $\rho \in {\Delta{(\mathcal{S})}}$ can be interpreted as the initial state distribution. This viewpoint naturally motivates gradient-based algorithms. In particular, the vanilla PG method performs projected gradient ascent over the policy space, while the NPG method performs gradient ascent under a geometry induced by the Fisher information matrix.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Natural Policy Gradient and Policy Dual Averaging", "weight": 1.0} -->

1: Input: Initialize π0 as the uniform policy and θ0 = 0 ∈ ℝm n.
4: πk + 1 (s) = arg max μ ∈ Δ (𝒜){μ⊤ θk + 1 (s)+h (μ)} for any s ∈ 𝒮.
Algorithm 1 Natural Policy Gradient

<!-- chunk {"id": "body-0027", "role": "body", "section": "Natural Policy Gradient and Policy Dual Averaging", "weight": 1.0} -->

There are many equivalent formulations of the NPG update. In this paper, to facilitate its connection with PI, we adopt the NPG update rule from ^22^2It corresponds to Q-NPG in \[1, Page 25\] when using a tabular representation., presented in Algorithm 1, where $h:{{\Delta{(\mathcal{A})}}\rightarrow{\mathbb{R}}}$ is the entropy function defined by ${h{(\mu)}} = {- {\sum_{a \in \mathcal{A}}{\mu{(a)}{\log\mu}{(a)}}}}$. Note that NPG is a special case of PDA. Specifically, replacing $h{( \cdot )}$ in Algorithm 1, Line 4, with the negative of any valid divergence-generating function yields PDA.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Doubly Smoothed Policy Iteration", "weight": 1.0} -->

To present DSPI, we begin by introducing the concept of smoothed Bellman operators. Let $\nu:{{\Delta{(\mathcal{A})}}\rightarrow{\mathbb{R}}}$ be a bounded, non-negative, and concave function; examples include the Shannon entropy, the Tsallis entropy, the shifted negative squared norm, and the zero function. Given a scalar $\eta \geq 0$, let the smoothed Bellman optimality operator $\mathcal{H}_{\eta}:{{\mathbb{R}}^{mn}\rightarrow{\mathbb{R}}^{mn}}$ be defined as

<!-- chunk {"id": "body-0029", "role": "body", "section": "Doubly Smoothed Policy Iteration", "weight": 1.0} -->

Note that $\mathcal{H}_{\eta}$ (respectively, $\mathcal{H}_{\eta}^{\pi}$) reduces to $\mathcal{H}$ (respectively, $\mathcal{H}^{\pi}$) when $\eta = 0$. Moreover, the smoothed Bellman operators are also contraction mappings and are monotonic (cf. Appendix B.2).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Doubly Smoothed Policy Iteration", "weight": 1.0} -->

With the smoothed Bellman operators in place, DSPI is presented in Algorithm 2.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Doubly Smoothed Policy Iteration", "weight": 1.0} -->

1: Input: Initialize π0 (s) ∈ arg max μ ∈ Δ (𝒜)ν (μ) for all s ∈ 𝒮 and ${\overline{Q}}_{0} = \mathbf{0}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Doubly Smoothed Policy Iteration", "weight": 1.0} -->

where βk ∈ is the stepsize.
4: Choose πk + 1 such that

<!-- chunk {"id": "body-0033", "role": "body", "section": "Doubly Smoothed Policy Iteration", "weight": 1.0} -->

where $\eta_{k} = {\tau{\prod_{j = 1}^{k}{({1 - \beta_{j}})}}}$ with τ ≥ 0 being a tunable parameter.
Algorithm 2 Doubly Smoothed Policy Iteration

<!-- chunk {"id": "body-0034", "role": "body", "section": "Doubly Smoothed Policy Iteration", "weight": 1.0} -->

Similar to PI, Line 4 of Algorithm 2 in general does not define a unique update. As long as $\pi_{k + 1}$ is chosen such that, when its associated smoothed Bellman operator $\mathcal{H}_{\eta_{k}}^{\pi_{k + 1}}$ is applied to the running average ${\overline{Q}}_{k + 1}$, the result coincides with that of applying the smoothed Bellman optimality operator $\mathcal{H}_{\eta_{k}}$ to ${\overline{Q}}_{k + 1}$, it is a valid update. A concrete way to implement this step is given by

<!-- chunk {"id": "body-0035", "role": "body", "section": "Doubly Smoothed Policy Iteration", "weight": 1.0} -->

While (3.1) is more explicit, the Bellman operator viewpoint in Line 4 of Algorithm 2 more naturally captures the fundamental nature of the update.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Doubly Smoothed Policy Iteration", "weight": 1.0} -->

Compared with PI presented in (2.1) (or more explicitly, (2.2)), DSPI introduces two levels of smoothing. First, it updates the policy using a weighted average of all past $Q$-functions rather than relying solely on the most recent one. Second, it replaces the greedy policy update with a softmax-based update, where $\nu{( \cdot )}$ acts as a regularization term. These two smoothing mechanisms motivate the name *doubly smoothed policy iteration*. Note that the stepsize $\beta_{k}$ simultaneously controls the weights in computing ${\overline{Q}}_{k + 1}$ and the degree of smoothing through the scaling $\eta_{k}$. As $\beta_{k}$ increases from zero to one, ${\overline{Q}}_{k + 1}$ places more weight on the last iterate $Q^{\pi_{k}}$ and the effect of smoothing fades away. In the extreme case where $\beta_{k} \equiv 1$, DSPI reduces to PI.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Doubly Smoothed Policy Iteration", "weight": 1.0} -->

Natural Policy Gradient. In addition to capturing PI, we next show that DSPI serves as a unified algorithmic framework encompassing a broad class of algorithms, starting with NPG.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Analysis", "weight": 1.0} -->

This section presents our main theoretical results. We begin with the convergence rates of DSPI in Section 4.1. Due to its unified nature, this result immediately implies the distribution-free global geometric convergence of NPG and PDA in Section 4.2, and enables us to establish the finite termination of dual-averaged PI in Section 4.3.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Convergence Rates of Doubly Smoothed Policy Iteration", "weight": 1.0} -->

The following theorem presents the asymptotic convergence and convergence rates of the DSPI algorithm. The proof of Theorem 4.1 is presented in Section 5.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Convergence Rates of Natural Policy Gradient and Policy Dual Averaging", "weight": 1.0} -->

As Proposition 3.1 shows NPG as a special case of the DSPI algorithm, Theorem 4.1 allows us to establish the geometric convergence of NPG below.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 4.4", "weight": 1.0} -->

The geometrically increasing stepsize sequence $\{\alpha_{k}\}$ has also been used in prior works to establish geometric convergence of NPG. Notably, Proposition 3.1 shows that the same policy sequence can be implemented via Algorithm 2 using the normalized recursion ${\overline{Q}}_{k + 1} = {{{({1 - \beta})}{\overline{Q}}_{k}} + {\betaQ^{\pi_{k}}}}$, together with the decaying smoothing parameter $\eta_{k} = {\tau{({1 - \beta})}^{k}}$. Thus, the prescribed schedule does not require storing exponentially large variables.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 4.4", "weight": 1.0} -->

The proof of Theorem 4.3 follows by combining Proposition 3.1 and Theorem 4.1, and is given in Appendix B.3. As a consequence, we obtain the following iteration complexity for NPG.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Finite Termination of Dual-Averaged Policy Iteration", "weight": 1.0} -->

When setting ${\nu{( \cdot )}} \equiv 0$ in Algorithm 2, the DSPI algorithm reduces to the dual-averaged PI, which updates the policies greedily with respect to the averaged $Q$-functions. As a special case of DSPI, the dual-averaged PI also enjoys geometric convergence (cf. Theorem 4.1 with $\nu_{\max} \equiv 0$). Moreover, we show that the algorithm terminates in a finite number of iterations with an optimal policy. This is presented in our next result.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 4.7", "weight": 1.0} -->

When $\gamma$ is treated as fixed, this yields a strongly polynomial bound in the numbers of states and actions, in the standard sense used for discounted MDP policy-iteration analyses. More generally, the bound is polynomial in $n$, $m$, and the effective horizon ${({1 - \gamma})}^{- 1}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 4.7", "weight": 1.0} -->

The proof of Theorem 4.6 is given in Appendix B.5. Following, the key idea is to show that dual-averaged PI eliminates at least one suboptimal action at some state every $k^{\ast}$ iterations, where $k^{\ast} = {\lceil{\beta^{- 1}{({1 - \gamma})}^{- 1}{\log{({2{({1 - \gamma})}^{- 1}})}}}\rceil}$. Since there are at most $n{({m - 1})}$ suboptimal actions, dual-averaged PI finds an optimal policy in at most $n{({m - 1})}k^{\ast}$ iterations.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Extensions", "weight": 1.0} -->

Although we have focused on discounted MDPs with a tabular representation, the generality of our framework allows both the algorithm and its analysis to extend naturally to other settings. We discuss these extensions below.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Extensions", "weight": 1.0} -->

Natural Policy Gradient with Linear Function Approximation. To overcome the curse of dimensionality, algorithms often incorporate function approximation (e.g., approximate dynamic programming). In Appendix C, we show that NPG with linear function approximation also admits a DSPI formulation, and we establish distribution-free global geometric convergence up to a function approximation error.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Extensions", "weight": 1.0} -->

Natural Policy Gradient for Stochastic Shortest Path Problems. Beyond the discounted setting, our framework also extends to stochastic shortest path problems, a special case of undiscounted MDPs. Classical results show that, under mild assumptions, the Bellman operator is monotone and contractive with respect to a weighted $\ell_{\infty}$ norm. Leveraging the DSPI formulation, we show that NPG for stochastic shortest path problems enjoys distribution-free global geometric convergence. See Appendix D for more details.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 5.2", "weight": 1.0} -->

By our convention, $Q^{\pi_{k}} \leq Q^{\pi_{k + 1}}$ means that ${Q^{\pi_{k}}{(s,a)}} \leq {Q^{\pi_{k + 1}}{(s,a)}}$ for all $(s,a)$. This vector-version monotonic improvement lemma is stronger than those in the literature on NPG, where monotonicity is established only for the scalar objective $V^{\pi_{k}}{(\rho)}$. This stronger form is important for leveraging the contraction property of the Bellman operator in the next step to derive a contractive recursion for the convergence error.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 5.4", "weight": 1.0} -->

In view of the proof of Theorem 4.1, although DSPI captures gradient-based policy optimization algorithms (e.g., NPG and PDA), its analysis differs fundamentally from approaches based on optimization techniques. It relies directly on Bellman's core principles: the monotonicity of the Bellman operator yields monotonic improvement of the policies (cf. Lemma 5.1), and its contraction property induces a contractive recursion for the convergence error (cf. Lemma 5.3).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduce DSPI, an algorithmic framework that bridges classical dynamic programming algorithms, such as PI and dual-averaged PI, with modern policy optimization methods, such as NPG and PDA. This perspective enables a unified analysis based on monotonicity and contraction properties of the Bellman operator, yielding distribution-free global geometric convergence for NPG and PDA, and establishing finite termination for dual-averaged PI. The framework also extends to discounted MDPs with linear function approximation and to stochastic shortest path problems.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Looking ahead, our current analysis assumes access to the exact $Q$-function $Q^{\pi}$ for each policy iterate, which isolates the policy-improvement dynamics. Extending DSPI to the model-free RL setting, where $Q^{\pi}$ must be estimated from sampled trajectories (e.g., via temporal-difference learning or Monte Carlo rollouts ), is therefore a natural next step. While finite-time guarantees for such policy evaluation methods are well understood, combining them with our framework to obtain sharp sample complexity results for model-free RL remains nontrivial. In particular, determining whether these variants can achieve minimax-optimal dependence on all problem parameters, namely $\mathcal{O}{({\epsilon^{- 2}{({1 - \gamma})}^{- 3}mn})}$, is, to the best of our knowledge, still broadly open in the existing analysis of actor-critic methods, and is an important direction for future work.
