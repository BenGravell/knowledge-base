## Introduction

In the last decade, reinforcement learning (RL) has emerged as a principled framework for large-scale sequential decision making, with applications ranging from autonomous vehicles and robotics to large language models. Mathematically, RL problems are typically modeled as Markov decision processes (MDPs). The seminal work of showed that solving an MDP reduces to finding a fixed point of the Bellman equation. By leveraging key properties of the Bellman operator, most notably contraction and monotonicity, a range of principled algorithms have been developed, including value iteration (VI), policy iteration (PI), and their variants.

In the modern era of sequential decision making, it was recognized that an MDP can be formulated as a continuous optimization problem over the policy space. From this perspective, the policy gradient (PG) method was introduced. Building on this viewpoint and further exploiting the geometry of the policy space, the natural policy gradient (NPG) method, along with more general approaches such as policy mirror ascent (PMA) and policy dual averaging (PDA), was developed. Over time, practical variants of these gradient-based methods, such as trust region policy optimization and proximal policy optimization, have become dominant approaches in large-scale applications.

The empirical success of NPG and its variants has motivated extensive theoretical work on their convergence properties. Existing approaches for studying NPG can be broadly categorized into two groups. One prominent line of work adopts a gradient-based optimization viewpoint, leveraging tools such as the policy gradient theorem, the performance difference lemma, the Polyak Łojasiewicz condition, and techniques from continuous optimization. A second line of work views NPG as an approximation of PI. Indeed, the original NPG paper \[24, Theorem 2\] observed that, as the stepsize approaches infinity, NPG recovers PI. Following this perspective, NPG has been analyzed as an approximation of PI by leveraging properties of the Bellman operator and separately bounding the approximation error.

Despite substantial progress, existing analyses still leave open a conceptual gap. The defining structural property of discounted MDPs is the $\ell_{\infty}$-norm contraction of the Bellman operator, which underlies the design and analysis of classical methods such as VI and PI. This property is not naturally visible when NPG is analyzed as a continuous optimization method over the policy space. Consequently, many optimization-based analyses either do not establish global geometric convergence or achieve it by introducing additional regularization into the MDP or the algorithm to induce curvature. In contrast, approaches that view NPG as an approximation of PI exploit Bellman operator properties and obtain distribution-free geometric convergence without additional regularization, but require stepsizes chosen adaptively based on the algorithm trajectory to control the approximation error. See Section 1.1 for further details.

More fundamentally, a unified perspective connecting classical dynamic programming methods based on Bellman iteration, such as PI, with modern gradient-based methods, such as NPG and PDA, remains lacking at both the algorithmic and analytical levels. In this paper, we address this gap by introducing doubly smoothed policy iteration (DSPI), a unified framework that includes PI, dual-averaged PI, NPG, and PDA as special cases. This perspective enables a unified analysis that yields strong guarantees for a broad class of algorithms. We summarize our contributions below.

Doubly Smoothed Policy Iteration. We introduce DSPI, in which the policy is updated via a regularized greedy step with respect to a weighted average of past $Q$-functions. This structure admits a compact Bellman operator formulation (cf. Algorithm 2, Line 4). We show that DSPI captures a broad class of existing algorithms, including PI, dual-averaged PI, and, most notably, NPG and PDA. Crucially, for NPG and PDA, interpreting these gradient-based methods as smoothed and averaged variants of PI allows the updates to be expressed via the smoothed Bellman operator, thereby enabling a principled analysis based on its properties.

A Unified Convergence Analysis. We show that DSPI converges asymptotically whenever the stepsizes are non-summable. Moreover, under a constant stepsize, DSPI achieves distribution-free global geometric convergence. In particular,

where $V^{\pi_{0}}$, $V^{\pi_{k}}$, and $V^{\ast}$ denote the value functions of the initial policy, the $k$-th iterate, and an optimal policy, respectively, $\gamma$ is the discount factor, and $\beta$ is the constant stepsize. See Theorem 4.1 for details. As byproducts,

this result implies an iteration complexity of $\mathcal{O}{({{({1 - \gamma})}^{- 1}{\log{({{({1 - \gamma})}^{- 1}\epsilon^{- 1}})}}})}$ for NPG and PDA to achieve ${\|{V^{\pi_{k}} - V^{\ast}}\|}_{\infty} \leq \epsilon$ (cf. Theorem 4.3), matching the state of the art without requiring additional regularization of the MDP or the algorithm, or the use of adaptive stepsizes;

it also enables us to establish finite termination of dual-averaged PI; in particular, an iteration complexity of $\mathcal{O}{({mn{({1 - \gamma})}^{- 1}{\log{({({1 - \gamma})}^{- 1})}}})}$ for finding an optimal policy (cf. Theorem 4.6), where $n$ and $m$ denote the sizes of the state and action spaces, respectively.

Moreover, the algorithm and analysis extend to settings such as discounted MDPs with linear function approximation, where we obtain the same convergence rate up to a function approximation error (cf. Appendix C), and stochastic shortest path problems, where we establish analogous geometric convergence (cf. Appendix D).

### Related Literature

Since we focus on the MDP setting rather than the model-free RL setting, we restrict our discussion below to PI and NPG, rather than results that broadly analyze actor--critic algorithms.

Policy Iteration. The PI method was first proposed . The global geometric convergence of PI was shown . The proof has two main steps: showing that the performance of the policies is monotonically improving, and leveraging the contraction property of the Bellman operator to establish a contractive recursion. This approach also inspires our analysis of DSPI. Beyond global geometric convergence, it was shown that PI can terminate in a finite number of iterations. The key property that enabled such strong results is that PI gradually eliminates sub-optimal actions. Such a property also plays a key role in showing the finite termination of dual-averaged PI in this work. Other variants of PI, including simplex PI, modified PI, and incremental PI, are analyzed .

Policy Gradient. The PG method was first proposed , which treats a weighted sum of the value function as a scalar objective and performs projected gradient ascent in the policy space. A comprehensive analysis of PG was carried out in and subsequent works. Beyond the setting of finite state-action space MDPs, PG methods for more general MDPs (e.g., continuous state-action spaces with potentially unbounded costs) have also been studied . Since the focus of this work is on NPG and more general PDA methods, we do not delve further into the literature on the convergence-rate analysis of vanilla PG.

Natural Policy Gradient. NPG, proposed , can be viewed as PG with a preconditioner. Alternatively, it can be interpreted as PMA or PDA, with the divergence-generating function chosen as the Shannon entropy. The majority of existing analyses of NPG suffer from at least one of the following limitations: lack of global geometric convergence; dependence on the initial distribution or a concentrability coefficient; additional regularization of the MDP or the algorithm; or reliance on adaptive stepsizes that depend on the policy trajectory. See Table 1 from Appendix A for more details. The only exception is, which provides the state-of-the-art analysis of NPG from a continuous optimization perspective^11^1The results in were developed for general PMA, which covers NPG as a special case., but their choice of stepsize depends on the Bellman error (also called the advantage gap) of the initial policy, which is not required in our result.

## Background

Consider an infinite horizon discounted MDP defined by the tuple $\mathcal{M} = {(\mathcal{S},\mathcal{A},p,\mathcal{R},\gamma)}$, where $\mathcal{S}$ and $\mathcal{A}$ denote the finite state and action spaces, respectively, ${\{ p{( \cdot \mid s,a)}\}}_{{(s,a)} \in {\mathcal{S} \times \mathcal{A}}}$ denotes the transition kernel, $\mathcal{R}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\lbrack 0,1\rbrack}}$ is the reward function, and $\gamma \in {}$ is the discount factor. Throughout, we denote $n = {|\mathcal{S}|}$ and $m = {|\mathcal{A}|}$.

Given a policy $\pi:{\mathcal{S}\rightarrow{\Delta{(\mathcal{A})}}}$, where $\Delta{(\mathcal{A})}$ denotes the set of probability distributions supported on $\mathcal{A}$, the $Q$-function $Q^{\pi}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ is defined as

where the expectation ${\mathbb{E}}_{\pi}{\lbrack \cdot \rbrack}$ is taken with respect to the randomness in both the action selection $A_{k} \sim \pi{( \cdot \mid S_{k})}$ and the state transitions $S_{k + 1} \sim p{( \cdot \mid S_{k},A_{k})}$. With $Q^{\pi}$ defined above, the value function $V^{\pi}:{\mathcal{S}\rightarrow{\mathbb{R}}}$ is defined as ${V^{\pi}{(s)}} = {\sum_{a \in \mathcal{A}}{\pi{(\left. a \middle| s \right.)}Q^{\pi}{(s,a)}}}$ for all $s \in \mathcal{S}$. Since the MDP has finitely many states and actions, $Q^{\pi}$ and $V^{\pi}$ can be equivalently viewed as vectors in ${\mathbb{R}}^{mn}$ and ${\mathbb{R}}^{n}$, respectively.

A policy $\pi^{\ast}$ is *optimal* if $V^{\ast}:=V^{\pi^{\ast}} \geq V^{\pi}$ for all $\pi$, or equivalently, $Q^{\ast}:=Q^{\pi^{\ast}} \geq Q^{\pi}$ for all $\pi$. Throughout this paper, inequalities between vectors are understood componentwise. For notational simplicity, for any vector $x \in {\mathbb{R}}^{mn}$ (e.g., representing a policy or a $Q$-function), we denote by ${x{(s)}} \in {\mathbb{R}}^{m}$ the vector whose $a$-th entry is $x{(s,a)}$.

### The Bellman Equation and Policy Iteration

The key to solving an MDP lies in the Bellman equation. We next present the Bellman equations for policy evaluation and policy optimization. To facilitate the connection between PI and NPG developed later in this paper, we express these equations in terms of $Q$-functions.

Given a policy $\pi$, its $Q$-function $Q^{\pi}$ is the unique solution to the Bellman equation $Q = {\mathcal{H}^{\pi}{(Q)}}$, where $\mathcal{H}^{\pi}:{{\mathbb{R}}^{mn}\rightarrow{\mathbb{R}}^{mn}}$ is the Bellman operator associated with policy $\pi$, defined as

Similarly, the optimal $Q$-function $Q^{\ast}$ is the unique solution to the Bellman optimality equation $Q = {\mathcal{H}{(Q)}}$, where $\mathcal{H}:{{\mathbb{R}}^{mn}\rightarrow{\mathbb{R}}^{mn}}$ is the Bellman optimality operator defined as

Moreover, once $Q^{\ast}$ is obtained, an optimal policy $\pi^{\ast}$ can be computed by choosing actions greedily with respect to $Q^{\ast}$. The operators $\mathcal{H}^{\pi}$ and $\mathcal{H}$ enjoy several useful properties. In particular, both are contraction mappings with respect to the $\ell_{\infty}$ norm with contraction factor $\gamma$, and are monotone in the sense that ${F{(Q_{1})}} \leq {F{(Q_{2})}}$ whenever $Q_{1} \leq Q_{2}$, where $F$ denotes either $\mathcal{H}^{\pi}$ or $\mathcal{H}$. One should not confuse the definition of monotonicity here with the notion of monotonicity in variational inequalities. These two properties enable the design and analysis of several classical algorithms, such as VI and PI.

When expressed in terms of $Q$-functions, the PI algorithm can be compactly written as

Note that (2.1) does not define a unique update. In particular, $\pi_{k + 1}$ can be any policy such that, when its associated Bellman operator $\mathcal{H}^{\pi_{k + 1}}$ is applied to the previous $Q$-function $Q^{\pi_{k}}$, the result coincides with applying the Bellman optimality operator to $Q^{\pi_{k}}$. In view of the definition of the Bellman operators, one concrete way to implement the PI update in (2.1) is

where, according to our notation, $\pi_{k + 1}{(s)}$ (respectively, $Q^{\pi_{k}}{(s)}$) denotes the $m$-dimensional vector whose $a$-th entry is $\pi_{k + 1}{({a \mid s})}$ (respectively, $Q^{\pi_{k}}{(s,a)}$).

The global geometric convergence of PI is well established in the literature. The analysis proceeds in two main steps: using the monotonicity of the Bellman operators to show that the policies are monotonically improving, i.e., $Q^{\pi_{k}} \leq Q^{\pi_{k + 1}}$; using the contraction property of the Bellman operators to show that the convergence error ${\|{Q^{\ast} - Q^{\pi_{k}}}\|}_{\infty}$ admits a contractive recursion. For completeness, we provide an analysis of PI in Appendix B.1.

### Natural Policy Gradient and Policy Dual Averaging

Since an optimal policy maximizes the value function $V^{\pi}{(s)}$ uniformly over all states $s$, solving an MDP is equivalent to solving an optimization problem over the policy space with the scalar objective ${V^{\pi}{(\rho)}}:={\sum_{s \in \mathcal{S}}{\rho{(s)}V^{\pi}{(s)}}}$, where $\rho \in {\Delta{(\mathcal{S})}}$ can be interpreted as the initial state distribution. This viewpoint naturally motivates gradient-based algorithms. In particular, the vanilla PG method performs projected gradient ascent over the policy space, while the NPG method performs gradient ascent under a geometry induced by the Fisher information matrix.

1: Input: Initialize π0 as the uniform policy and θ0 = 0 ∈ ℝm n.
4: πk + 1 (s) = arg max μ ∈ Δ (𝒜){μ⊤ θk + 1 (s)+h (μ)} for any s ∈ 𝒮.
Algorithm 1 Natural Policy Gradient

There are many equivalent formulations of the NPG update. In this paper, to facilitate its connection with PI, we adopt the NPG update rule from ^22^2It corresponds to Q-NPG in \[1, Page 25\] when using a tabular representation., presented in Algorithm 1, where $h:{{\Delta{(\mathcal{A})}}\rightarrow{\mathbb{R}}}$ is the entropy function defined by ${h{(\mu)}} = {- {\sum_{a \in \mathcal{A}}{\mu{(a)}{\log\mu}{(a)}}}}$. Note that NPG is a special case of PDA. Specifically, replacing $h{( \cdot )}$ in Algorithm 1, Line 4, with the negative of any valid divergence-generating function yields PDA.

## Doubly Smoothed Policy Iteration

To present DSPI, we begin by introducing the concept of smoothed Bellman operators. Let $\nu:{{\Delta{(\mathcal{A})}}\rightarrow{\mathbb{R}}}$ be a bounded, non-negative, and concave function; examples include the Shannon entropy, the Tsallis entropy, the shifted negative squared norm, and the zero function. Given a scalar $\eta \geq 0$, let the smoothed Bellman optimality operator $\mathcal{H}_{\eta}:{{\mathbb{R}}^{mn}\rightarrow{\mathbb{R}}^{mn}}$ be defined as

Given a policy $\pi$ and a scalar $\eta \geq 0$, let $\mathcal{H}_{\eta}^{\pi}:{{\mathbb{R}}^{mn}\rightarrow{\mathbb{R}}^{mn}}$ be defined as

Note that $\mathcal{H}_{\eta}$ (respectively, $\mathcal{H}_{\eta}^{\pi}$) reduces to $\mathcal{H}$ (respectively, $\mathcal{H}^{\pi}$) when $\eta = 0$. Moreover, the smoothed Bellman operators are also contraction mappings and are monotonic (cf. Appendix B.2).

With the smoothed Bellman operators in place, DSPI is presented in Algorithm 2.

1: Input: Initialize π0 (s) ∈ arg max μ ∈ Δ (𝒜)ν (μ) for all s ∈ 𝒮 and ${\overline{Q}}_{0} = \mathbf{0}$.
3: Maintain a running average of past Q-functions:

${{\overline{Q}}_{k + 1} = {{{({1 - \beta_{k}})}{\overline{Q}}_{k}} + {\beta_{k}Q^{\pi_{k}}}}},$

where βk ∈ is the stepsize.
4: Choose πk + 1 such that

${{\mathcal{H}_{\eta_{k}}^{\pi_{k + 1}}{({\overline{Q}}_{k + 1})}} = {\mathcal{H}_{\eta_{k}}{({\overline{Q}}_{k + 1})}}},$

where $\eta_{k} = {\tau{\prod_{j = 1}^{k}{({1 - \beta_{j}})}}}$ with τ ≥ 0 being a tunable parameter.
Algorithm 2 Doubly Smoothed Policy Iteration

Similar to PI, Line 4 of Algorithm 2 in general does not define a unique update. As long as $\pi_{k + 1}$ is chosen such that, when its associated smoothed Bellman operator $\mathcal{H}_{\eta_{k}}^{\pi_{k + 1}}$ is applied to the running average ${\overline{Q}}_{k + 1}$, the result coincides with that of applying the smoothed Bellman optimality operator $\mathcal{H}_{\eta_{k}}$ to ${\overline{Q}}_{k + 1}$, it is a valid update. A concrete way to implement this step is given by

While (3.1) is more explicit, the Bellman operator viewpoint in Line 4 of Algorithm 2 more naturally captures the fundamental nature of the update.

Compared with PI presented in (2.1) (or more explicitly, (2.2)), DSPI introduces two levels of smoothing. First, it updates the policy using a weighted average of all past $Q$-functions rather than relying solely on the most recent one. Second, it replaces the greedy policy update with a softmax-based update, where $\nu{( \cdot )}$ acts as a regularization term. These two smoothing mechanisms motivate the name *doubly smoothed policy iteration*. Note that the stepsize $\beta_{k}$ simultaneously controls the weights in computing ${\overline{Q}}_{k + 1}$ and the degree of smoothing through the scaling $\eta_{k}$. As $\beta_{k}$ increases from zero to one, ${\overline{Q}}_{k + 1}$ places more weight on the last iterate $Q^{\pi_{k}}$ and the effect of smoothing fades away. In the extreme case where $\beta_{k} \equiv 1$, DSPI reduces to PI.

Natural Policy Gradient. In addition to capturing PI, we next show that DSPI serves as a unified algorithmic framework encompassing a broad class of algorithms, starting with NPG.

### Proposition 3.1

In Algorithm 2, when choosing $\beta_{k} = {\alpha_{k}/{\sum_{i = 0}^{k}\alpha_{i}}}$, $\tau = {1/\alpha_{0}}$, and ${\nu{( \cdot )}} = {h{( \cdot )}}$, the sequence of policies generated by Algorithm 2 with Line 4 implemented via (3.1) is identical to that generated by Algorithm 1.

### Proof of Proposition 3.1

Since both algorithms initialize at the uniform policy, it suffices to show that their update equations generate identical policies thereafter. By Line 3 of Algorithm 1, we have $\theta_{k + 1} = {\sum_{i = 0}^{k}{\alpha_{i}Q^{\pi_{i}}}}$ for all $k \geq 0$. As a result, Line 4 of Algorithm 1 becomes

where the last equality follows from (i) the $\arg\max$ operator being indifferent to constant scaling and (ii) $\tau = {1/\alpha_{0}}$. In view of the above equality and Line 4 of Algorithm 2 (which is equivalent to (3.1) since the Shannon entropy $h{( \cdot )}$ is strongly concave), it remains to show that ${\overline{Q}}_{k + 1} = {\sum_{i = 0}^{k}{{\alpha_{i}Q^{\pi_{i}}}/{\sum_{i = 0}^{k}\alpha_{i}}}}$ and ${\prod_{j = 1}^{k}{({1 - \beta_{j}})}} = {\alpha_{0}/{\sum_{i = 0}^{k}\alpha_{i}}}$ for all $k \geq 0$, which we prove by induction.

For $k = 0$, since $\beta_{0} = 1$, the base case clearly holds. Suppose that the desired equalities hold for some $k \geq 0$. Then, by the update equation in Line 3 of Algorithm 2, we have

where the last equality follows from the induction hypothesis. Similarly, we have

The induction is complete. ∎

Proposition 3.1 is conceptually important, as it reveals that the widely used NPG algorithm, although originally developed from a gradient-based continuous optimization viewpoint, can be interpreted as a smoothed and averaged variant of classical PI. This perspective allows us to build on Bellman's foundational insights, such as the contraction and monotonicity of the Bellman operator, to establish strong convergence guarantees for NPG via the analysis of DSPI.

Policy Dual Averaging. Since NPG is a special case of PDA when the divergence-generating function is chosen as the negative entropy, by setting $\nu{( \cdot )}$ to a shifted negative divergence-generating function, i.e., ${\nu{(\mu)}} = {C - {\omega{(\mu)}}}$ for a bounded convex divergence-generating function $\omega$, where $C:={{\max_{\mu}\omega}{(\mu)}}$ ensures that ${\nu{(\mu)}} \geq 0$, DSPI also captures PDA. The proof follows identically to that of Proposition 3.1 and is therefore omitted.

Dual-Averaged Policy Iteration. DSPI is more general than PDA, as it allows choosing ${\nu{( \cdot )}} \equiv 0$. In this case, Algorithm 2 updates the policy greedily based on a weighted average of historical $Q$-functions. We refer to this update as dual-averaged PI. One should not confuse dual-averaged PI with incremental PI, where the averaging is performed in the policy space, whereas in dual-averaged PI the averaging is performed in the $Q$-function space.

## Analysis

This section presents our main theoretical results. We begin with the convergence rates of DSPI in Section 4.1. Due to its unified nature, this result immediately implies the distribution-free global geometric convergence of NPG and PDA in Section 4.2, and enables us to establish the finite termination of dual-averaged PI in Section 4.3.

### Convergence Rates of Doubly Smoothed Policy Iteration

The following theorem presents the asymptotic convergence and convergence rates of the DSPI algorithm. The proof of Theorem 4.1 is presented in Section 5.

### Theorem 4.1

Consider $\{\pi_{k}\}$ generated by Algorithm 2.

When $\beta_{k} \in {(0,1\rbrack}$ and ${\sum_{k = 0}^{\infty}\beta_{k}} = \infty$, we have ${\lim_{k\rightarrow\infty}{\|{V^{\ast} - V^{\pi_{k}}}\|}_{\infty}} = 0$.

When choosing $\beta_{0} = 1$, $\beta_{k} \equiv \beta \in {(0,1\rbrack}$ for all $k \geq 1$, we have

where $\nu_{\max}:={{\max_{\mu \in {\Delta{(\mathcal{A})}}}\nu}{(\mu)}}$.

Theorem 4.1 states that $V^{\pi_{k}}$ asymptotically converges to the optimal value function as long as the stepsizes are non-summable. Theorem 4.1 characterizes global geometric convergence, which implies the iteration complexity presented below.

### Corollary 4.2

For any $\epsilon > 0$, choose $\beta_{0} = 1$, $\beta_{k} = {1/2}$ for $k \geq 1$, and choose $\tau$ such that ${\tau\nu_{\max}} \leq 1$ in Algorithm 2. Then, we have ${\|{V^{\ast} - V^{\pi_{k}}}\|}_{\infty} \leq \epsilon$ provided that $k \geq {2{({1 - \gamma})}^{- 1}{\log{({\epsilon^{- 1}{({1 - \gamma})}^{- 1}})}}}$.

### Convergence Rates of Natural Policy Gradient and Policy Dual Averaging

As Proposition 3.1 shows NPG as a special case of the DSPI algorithm, Theorem 4.1 allows us to establish the geometric convergence of NPG below.

### Theorem 4.3

Consider $\{\pi_{k}\}$ generated by Algorithm 1. When choosing $\alpha_{0} = {\log{(m)}}$ and $\alpha_{k} = {{\beta\alpha_{0}}/{({1 - \beta})}^{k}}$ for all $k \geq 1$, where $\beta \in {}$ can be arbitrary, we have

### Remark 4.4

The geometrically increasing stepsize sequence $\{\alpha_{k}\}$ has also been used in prior works to establish geometric convergence of NPG. Notably, Proposition 3.1 shows that the same policy sequence can be implemented via Algorithm 2 using the normalized recursion ${\overline{Q}}_{k + 1} = {{{({1 - \beta})}{\overline{Q}}_{k}} + {\betaQ^{\pi_{k}}}}$, together with the decaying smoothing parameter $\eta_{k} = {\tau{({1 - \beta})}^{k}}$. Thus, the prescribed schedule does not require storing exponentially large variables.

The proof of Theorem 4.3 follows by combining Proposition 3.1 and Theorem 4.1, and is given in Appendix B.3. As a consequence, we obtain the following iteration complexity for NPG.

### Corollary 4.5

For any $\epsilon > 0$, by choosing $\alpha_{0} = {\log{(m)}}$ and $\alpha_{k} = {{\log{(m)}} \cdot 2^{k - 1}}$ for all $k \geq 1$ in Algorithm 1, we have ${\|{V^{\ast} - V^{\pi_{k}}}\|}_{\infty} \leq \epsilon$ provided that $k \geq {2{({1 - \gamma})}^{- 1}{\log{({\epsilon^{- 1}{({1 - \gamma})}^{- 1}})}}}$.

Theorem 4.3 and Corollary 4.5 show that NPG enjoys global geometric convergence, measured by the optimality gap of the last iterate $\pi_{k}$. Moreover, the convergence bounds have several important features, which we discuss below.

Distribution-Free Convergence Rates. In the existing literature on NPG, convergence rates typically depend on the initial distribution $\rho$, either explicitly or implicitly through a distribution mismatch coefficient. In contrast, our convergence bound is expressed in terms of the $\ell_{\infty}$ norm of the value-function gap and is free of such dependencies.

No Additional Regularization. While our iteration complexity matches the state of the art, our result is obtained without modifying the MDP or the algorithm. Several existing analyses establishing geometric convergence for NPG either regularize the MDP or introduce an additional strongly convex regularizer into the algorithm. In contrast, we do not rely on any such modifications; the only regularization arises from the entropy term inherent in the standard NPG formulation. Our DSPI viewpoint, together with its Bellman-operator formulation (cf. Line 4 of Algorithm 2), allows us to directly exploit the contraction property of the Bellman operator, thereby eliminating the need for additional curvature-inducing regularization.

A Simple Prespecified Stepsize Schedule. Our results show that NPG converges at a geometric rate with a simple stepsize schedule $\alpha_{k} = {{\beta\alpha_{0}}/{({1 - \beta})}^{k}}$, where $\beta \in {}$ is arbitrary. In contrast, existing results that view NPG as an approximation of PI require adaptive stepsizes that depend on the value of $\pi_{k}{({a_{k}^{\ast} \mid s})}$, where $a_{k}^{\ast} \in {{{\arg\max}_{a \in \mathcal{A}}Q^{\pi_{k}}}{(s,a)}}$. Similarly, analyses that study NPG from an optimization viewpoint require stepsizes that depend on the Bellman error (also known as the advantage gap) of the initial policy \[23, Theorems 3.4 and 3.5\].

Policy Dual Averaging. Similarly, by choosing ${\nu{(\mu)}} = {C - {\omega{(\mu)}}}$, where $\omega$ is a bounded divergence-generating function and $C:={{\max_{\mu \in {\Delta{(\mathcal{A})}}}\omega}{(\mu)}}$, Algorithm 2 captures PDA. Theorem 4.1 therefore implies global geometric convergence for PDA. The results and proofs are identical to those of Theorem 4.3 and are therefore omitted.

### Finite Termination of Dual-Averaged Policy Iteration

When setting ${\nu{( \cdot )}} \equiv 0$ in Algorithm 2, the DSPI algorithm reduces to the dual-averaged PI, which updates the policies greedily with respect to the averaged $Q$-functions. As a special case of DSPI, the dual-averaged PI also enjoys geometric convergence (cf. Theorem 4.1 with $\nu_{\max} \equiv 0$). Moreover, we show that the algorithm terminates in a finite number of iterations with an optimal policy. This is presented in our next result.

### Theorem 4.6

Let $\{\pi_{k}\}$ be generated by Algorithm 2 with ${\nu{( \cdot )}} \equiv 0$ and a deterministic $\pi_{0}$, where Line 4 selects a deterministic greedy policy according to a fixed tie-breaking rule. When $\beta_{0} = 1$ and $\beta_{k} \equiv \beta \in {}$ for all $k \geq 1$, the algorithm terminates after at most $n{({m - 1})}\left\lceil {\beta^{- 1}{({1 - \gamma})}^{- 1}{\log\left( {2{({1 - \gamma})}^{- 1}} \right)}} \right\rceil$ iterations with an optimal policy, where $\lceil x\rceil$ denotes the smallest integer greater than or equal to $x$.

### Remark 4.7

When $\gamma$ is treated as fixed, this yields a strongly polynomial bound in the numbers of states and actions, in the standard sense used for discounted MDP policy-iteration analyses. More generally, the bound is polynomial in $n$, $m$, and the effective horizon ${({1 - \gamma})}^{- 1}$.

The proof of Theorem 4.6 is given in Appendix B.5. Following, the key idea is to show that dual-averaged PI eliminates at least one suboptimal action at some state every $k^{\ast}$ iterations, where $k^{\ast} = {\lceil{\beta^{- 1}{({1 - \gamma})}^{- 1}{\log{({2{({1 - \gamma})}^{- 1}})}}}\rceil}$. Since there are at most $n{({m - 1})}$ suboptimal actions, dual-averaged PI finds an optimal policy in at most $n{({m - 1})}k^{\ast}$ iterations.

### Extensions

Although we have focused on discounted MDPs with a tabular representation, the generality of our framework allows both the algorithm and its analysis to extend naturally to other settings. We discuss these extensions below.

Natural Policy Gradient with Linear Function Approximation. To overcome the curse of dimensionality, algorithms often incorporate function approximation (e.g., approximate dynamic programming). In Appendix C, we show that NPG with linear function approximation also admits a DSPI formulation, and we establish distribution-free global geometric convergence up to a function approximation error.

Natural Policy Gradient for Stochastic Shortest Path Problems. Beyond the discounted setting, our framework also extends to stochastic shortest path problems, a special case of undiscounted MDPs. Classical results show that, under mild assumptions, the Bellman operator is monotone and contractive with respect to a weighted $\ell_{\infty}$ norm. Leveraging the DSPI formulation, we show that NPG for stochastic shortest path problems enjoys distribution-free global geometric convergence. See Appendix D for more details.

## Proof of Theorem 4.1

Our proof proceeds in two steps: we first establish monotonic improvement of the $Q$-functions, and then derive and solve a contractive recursion for the convergence error.

### Lemma 5.1

Algorithm 2 satisfies $Q^{\pi_{k}} \leq Q^{\pi_{k + 1}}$ for all $k \geq 0$.

### Remark 5.2

By our convention, $Q^{\pi_{k}} \leq Q^{\pi_{k + 1}}$ means that ${Q^{\pi_{k}}{(s,a)}} \leq {Q^{\pi_{k + 1}}{(s,a)}}$ for all $(s,a)$. This vector-version monotonic improvement lemma is stronger than those in the literature on NPG, where monotonicity is established only for the scalar objective $V^{\pi_{k}}{(\rho)}$. This stronger form is important for leveraging the contraction property of the Bellman operator in the next step to derive a contractive recursion for the convergence error.

### Proof of Lemma 5.1

It suffices to show that $Q^{\pi_{k}} \leq {\mathcal{H}^{\pi_{k + 1}}{(Q^{\pi_{k}})}}$ for all $k \geq 0$. Once this is established, repeatedly applying $\mathcal{H}^{\pi_{k + 1}}$ to both sides and using its monotonicity yields $Q^{\pi_{k}} \leq {{\lbrack\mathcal{H}^{\pi_{k + 1}}\rbrack}^{n}{(Q^{\pi_{k}})}}$ for all $n \geq 0$. Taking $n\rightarrow\infty$ gives $Q^{\pi_{k}} \leq Q^{\pi_{k + 1}}$.

For simplicity of notation, define $f:{{\mathbb{R}}^{mn}\rightarrow{\mathbb{R}}^{mn}}$ by ${{\lbrack{f{(\pi)}}\rbrack}{(s,a)}} = {\gamma{\sum_{s^{\prime} \in \mathcal{S}}{p{({s^{\prime} \mid {s,a}})}\nu{({\pi{(s^{\prime})}})}}}}$ for all $(s,a)$. Then, for any policy $\pi$ and $Q \in {\mathbb{R}}^{mn}$, we have ${\mathcal{H}_{\eta}^{\pi}{(Q)}} = {{\mathcal{H}^{\pi}{(Q)}} + {\etaf{(\pi)}}}$. We now show that $Q^{\pi_{k}} \leq {\mathcal{H}^{\pi_{k + 1}}{(Q^{\pi_{k}})}}$ for the two cases $k = 0$ and $k \geq 1$.

For $k = 0$, since $\beta_{0} = 1$, we have ${\overline{Q}}_{1} = Q^{\pi_{0}}$. It follows that $Q^{\pi_{0}} = {\mathcal{H}^{\pi_{0}}{({\overline{Q}}_{1})}} = {{\mathcal{H}_{\eta_{0}}^{\pi_{0}}{({\overline{Q}}_{1})}} - {\eta_{0}f{(\pi_{0})}}}$. Since ${\mathcal{H}_{\eta_{0}}^{\pi_{0}}{({\overline{Q}}_{1})}} \leq {\mathcal{H}_{\eta_{0}}{({\overline{Q}}_{1})}} = {\mathcal{H}_{\eta_{0}}^{\pi_{1}}{({\overline{Q}}_{1})}}$ and ${f{(\pi_{1})}} \leq {f{(\pi_{0})}}$, where the latter follows from initializing ${\pi_{0}{(s)}} \in {{{\arg\max}_{\mu \in {\Delta{(\mathcal{A})}}}\nu}{(\mu)}}$ for all $s \in \mathcal{S}$, we further obtain

For $k \geq 1$, since $Q^{\pi_{k}} = {\mathcal{H}^{\pi_{k}}{(Q^{\pi_{k}})}}$ and $Q^{\pi_{k}} = {{({{\overline{Q}}_{k + 1} - {{({1 - \beta_{k}})}{\overline{Q}}_{k}}})}/\beta_{k}}$ (cf. Line 3 of Algorithm 2), we have

where the second equality follows from $\mathcal{H}_{\eta_{k - 1}}^{\pi_{k}}$ being an affine operator, and the last equality follows from $\eta_{k} = {{({1 - \beta_{k}})}\eta_{k - 1}}$.

To proceed, observe that by Line 4 of Algorithm 2, we have ${\mathcal{H}_{\eta_{k}}^{\pi_{k}}{({\overline{Q}}_{k + 1})}} \leq {\mathcal{H}_{\eta_{k}}^{\pi_{k + 1}}{({\overline{Q}}_{k + 1})}}$ and ${\mathcal{H}_{\eta_{k - 1}}^{\pi_{k}}{({\overline{Q}}_{k})}} \geq {\mathcal{H}_{\eta_{k - 1}}^{\pi_{k + 1}}{({\overline{Q}}_{k})}}$. Therefore,

where the last equality follows from Algorithm 2, Line 3, and $\eta_{k} = {{({1 - \beta_{k}})}\eta_{k - 1}}$.

With Lemma 5.1 in hand, we next derive a contractive recursion for ${\overline{Q}}_{k}$.

### Lemma 5.3

### Proof of Lemma 5.3

An immediate implication of Lemma 5.1 is that ${\overline{Q}}_{k} \leq Q^{\pi_{k}}$ for all $k \geq 0$, since ${\overline{Q}}_{k}$ is a weighted average of a monotonically increasing sequence.

Let $\mathbf{1}$ denote the all-ones vector. Using Algorithm 2, Line 3, we obtain for all $k \geq 1$ that

$\leq$ ${{({1 - \beta_{k}})}{({Q^{\ast} - {\overline{Q}}_{k}})}} + {\beta_{k}{({{\mathcal{H}{(Q^{\ast})}} - {\mathcal{H}^{\pi_{k}}{({\overline{Q}}_{k})}}})}}$ (5.1b)
$=$ ${{({1 - \beta_{k}})}{({Q^{\ast} - {\overline{Q}}_{k}})}} + {\beta_{k}{({{\mathcal{H}{(Q^{\ast})}} - {\mathcal{H}_{\eta_{k - 1}}^{\pi_{k}}{({\overline{Q}}_{k})}}})}} + {\beta_{k}\eta_{k - 1}f{(\pi_{k})}}$
$\leq$ ${{({1 - \beta_{k}})}{({Q^{\ast} - {\overline{Q}}_{k}})}} + {\beta_{k}{({{\mathcal{H}{(Q^{\ast})}} - {\mathcal{H}{({\overline{Q}}_{k})}}})}} + {\beta_{k}\eta_{k - 1}f{(\pi_{k})}}$ (5.1c)
$\leq$ ${{({1 - \beta_{k}})}{\|{Q^{\ast} - {\overline{Q}}_{k}}\|}_{\infty}\mathbf{1}} + {\beta_{k}{\|{{\mathcal{H}{(Q^{\ast})}} - {\mathcal{H}{({\overline{Q}}_{k})}}}\|}_{\infty}\mathbf{1}} + {\gamma\beta_{k}\eta_{k - 1}\nu_{\max}\mathbf{1}}$
$\leq$ ${{\left( {1 - {{({1 - \gamma})}\beta_{k}}} \right){\|{Q^{\ast} - {\overline{Q}}_{k}}\|}_{\infty}\mathbf{1}} + {\gamma\beta_{k}\eta_{k - 1}\nu_{\max}\mathbf{1}}},$ (5.1d)

where (5.1a) follows from the Bellman equations, (5.1b) follows from ${\overline{Q}}_{k} \leq Q^{\pi_{k}}$ and $\mathcal{H}^{\pi_{k}}$ being a monotonic operator, (5.1c) follows from ${\mathcal{H}{({\overline{Q}}_{k})}} \leq {\mathcal{H}_{\eta_{k - 1}}{({\overline{Q}}_{k})}} = {\mathcal{H}_{\eta_{k - 1}}^{\pi_{k}}{({\overline{Q}}_{k})}}$, and (5.1d) follows from $\mathcal{H}$ being a contraction mapping with respect to $\parallel \cdot \parallel_{\infty}$. Since the vector $Q^{\ast} - {\overline{Q}}_{k + 1}$ has non-negative entries, the desired inequality follows. ∎

### Proof of Theorem 4.1

Repeatedly applying Lemma 5.3, we obtain a bound on ${\|{Q^{\ast} - {\overline{Q}}_{k}}\|}_{\infty}$. The final step of the proof is to translate this bound into one on ${\|{V^{\ast} - V^{\pi_{k}}}\|}_{\infty}$, and then solve the resulting recursion. This step involves only algebraic manipulations, and we defer the details to Appendix B.4. The proof is complete after this step. ∎

### Remark 5.4

In view of the proof of Theorem 4.1, although DSPI captures gradient-based policy optimization algorithms (e.g., NPG and PDA), its analysis differs fundamentally from approaches based on optimization techniques. It relies directly on Bellman's core principles: the monotonicity of the Bellman operator yields monotonic improvement of the policies (cf. Lemma 5.1), and its contraction property induces a contractive recursion for the convergence error (cf. Lemma 5.3).

## Conclusion

We introduce DSPI, an algorithmic framework that bridges classical dynamic programming algorithms, such as PI and dual-averaged PI, with modern policy optimization methods, such as NPG and PDA. This perspective enables a unified analysis based on monotonicity and contraction properties of the Bellman operator, yielding distribution-free global geometric convergence for NPG and PDA, and establishing finite termination for dual-averaged PI. The framework also extends to discounted MDPs with linear function approximation and to stochastic shortest path problems.

Looking ahead, our current analysis assumes access to the exact $Q$-function $Q^{\pi}$ for each policy iterate, which isolates the policy-improvement dynamics. Extending DSPI to the model-free RL setting, where $Q^{\pi}$ must be estimated from sampled trajectories (e.g., via temporal-difference learning or Monte Carlo rollouts ), is therefore a natural next step. While finite-time guarantees for such policy evaluation methods are well understood, combining them with our framework to obtain sharp sample complexity results for model-free RL remains nontrivial. In particular, determining whether these variants can achieve minimax-optimal dependence on all problem parameters, namely $\mathcal{O}{({\epsilon^{- 2}{({1 - \gamma})}^{- 3}mn})}$, is, to the best of our knowledge, still broadly open in the existing analysis of actor-critic methods, and is an important direction for future work.
