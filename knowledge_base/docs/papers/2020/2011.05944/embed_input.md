<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Asymptotically Optimal Information-Directed Sampling

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce a simple and efficient algorithm for stochastic linear bandits with finitely many actions that is asymptotically optimal and (nearly) worst-case optimal in finite time. The approach is based on the frequentist information-directed sampling (IDS) framework, with a surrogate for the information gain that is informed by the optimization problem that defines the asymptotic lower bound. Our analysis sheds light on how IDS balances the trade-off between regret and information and uncovers a surprising connection between the recently proposed primal-dual methods and the IDS algorithm. We demonstrate empirically that IDS is competitive with UCB in finite-time, and can be significantly better in the asymptotic regime.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The stochastic linear bandit problem is an iterative game between a learner and an environment played over $n$ rounds. In each round $t$, the learner chooses an action (or arm) $x_{t}$ from a finite set of actions $\mathcal{X} \subset {\mathbb{R}}^{d}$ and observes a noisy reward $y_{t} = {\left\langle x_{t},\theta^{\ast} \right\rangle + \epsilon_{t}}$ where $\theta^{\ast} \in {\mathbb{R}}^{d}$ is an unknown parameter vector and $\epsilon_{t}$ is zero-mean noise. The learner's goal is to maximize the expected cumulative reward or, equivalently, to minimize the expected regret, which is defined by

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $\pi$ is the policy mapping sequences of action/reward pairs to distributions over actions in $\mathcal{X}$ and the expectation is over the randomness in the policy and the rewards. Unlike in the multi-armed bandit setting, the linear structure allows the learner to estimate the reward of an action without directly observing it. In particular, the learner might play an action that it knows to be suboptimal in order to most efficiently identify the optimal action.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The *worst-case regret* ${R_{n}(\pi)} = {\sup_{\theta \in \mathcal{M}}{R_{n}(\pi,\theta)}}$ measures the performance of a policy on an adversarially chosen parameter $\theta$ in a class of models $\mathcal{M}$. On the other hand, for a fixed instance $\theta^{\ast}$, an algorithm can perform much better than the worst-case regret $R_{n}(\pi)$ suggests, and achieving the optimal instance-dependent regret $R_{n}\left( \pi,\theta^{\ast} \right)$ is therefore of significant interest. On a large horizon, the optimal instance-dependent regret, or *asymptotic regret*, is characterized by a convex program, that optimizes the allocated proportion of plays to each action to minimize the regret, subject to the constraint that the policy gathers enough information to infer the best action.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The optimal worst-case regret rate (up to logarithmic factors) is achieved by various algorithms, including adaptations of the upper confidence bound (UCB) algorithm and the information-directed sampling (IDS) approach. A conservative version of Thompson sampling is suboptimal by a factor of $\sqrt{d}$ and logarithmic factors. On the other hand, achieving optimal asymptotic regret has proven to be more challenging. Lattimore and Szepesvári showed that algorithms based on optimism or Thompson sampling are not asymptotically optimal in the linear setting. They propose an approach based on the explore-then-commit framework that computes an estimate of the optimal allocation and updates the allocation to match the predicted target. Combes et al. follow a similar plan for the structured bandit setting, which includes the linear setting as a special case. This idea was subsequently extended to the contextual setting by Hao et al.. Unfortunately these algorithms are not at all practical and do not enjoy reasonable minimax regret. More recently, Jun and Zhang refined this technique in the structured setting with a finite model class to avoid forced exploration and the knowledge of the horizon.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Similarly, Van Parys and Golrezaei use a dual formulation of the lower bound to devise an algorithm that achieves the optimal asymptotic regret up to a constant, and avoids re-solving for the predicted optimal allocation at every round. Degenne et al. take a different approach and translate the Lagrangian of the lower bound into a fictitious two-player game, where the saddle point corresponds to the asymptotic regret. Using tools from online convex optimization, this leads to a family of asymptotically optimal algorithms, which incrementally update the allocation in each round based on primal-dual updates on the Lagrangian of the lower bound. Another primal-dual method is by Tirinzoni et al., which unlike previous methods is both worst-case and asymptotically optimal and also applies to the contextual case. We explain how IDS relates to primal-dual methods in Section 2.3. Finally, Wagenmaker et al. combine optimal experimental design with a phased elimination-style algorithm to derive finite-time guarantees that scale with the Gaussian width of the action set.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

Our main contribution is new *conceptual insights* into information-directed sampling (IDS). We show that with an appropriate choice of the information gain, IDS performs *primal-dual updates* on the Lagrangian of the lower bound. The proposed version of IDS for the linear bandit setting is (nearly) *worst-case optimal* in finite time, satisfies an explicit *gap-dependent logarithmic regret* bound and is *asymptotically optimal*. All regret bounds are on *frequentist expected regret* and our analysis is relatively simple, avoiding all but one high-probability bound. The asymptotic analysis uncovers a connection between IDS and recently proposed primal-dual methods. Moreover, our choice of information gain function approximates the variance based information gain proposed by in the Bayesian setting.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Setting", "weight": 1.0} -->

Then $x_{t}$ is sampled from $\mu_{t}$ and the learner observes the reward $y_{t} = {\left\langle x_{t},\theta \right\rangle + \epsilon_{t}}$ where $\epsilon_{t}$ is sampled independently from a Gaussian with zero mean and unit variance. All our upper bounds hold without modification for conditionally $1$-subgaussian noise. The objective is to minimize the expected cumulative regret $R_{n} = {R_{n}\left( \pi,\theta^{\ast} \right)}$ defined in Eq., where $\pi = \left( \mu_{t} \right)_{t = 1}^{n}$ is the policy chosen by the learner. The dependency of the regret on $\theta^{\ast}$ and $\pi$ is mostly omitted when there is no ambiguity.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Setting", "weight": 1.0} -->

The expectation conditioned on previous observations is ${\mathbb{E}}_{s}\lbrack \cdot \rbrack = {\mathbb{E}}\left\lbrack \cdot \middle| \left( x_{l},y_{l} \right)_{l = 1}^{s - 1} \right\rbrack$. In line with all previous work focusing on the asymptotic setting, we assume that the optimal action $x^{\ast} = {x^{\ast}\left( \theta^{\ast} \right)} = {{\arg\max}_{x \in \mathcal{X}}\left\langle x,\theta^{\ast} \right\rangle}$ is unique. Eliminating this assumption is left as a delicate and possibly non-trivial challenge for the future.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Asymptotic Lower Bound", "weight": 1.0} -->

For an allocation $\alpha \in {\mathbb{R}}_{\geq 0}^{\mathcal{X}}$ over actions we define the associated covariance matrix ${V(\alpha)} = \left. \sum{}_{x \in \mathcal{X}}{\alpha(x)xx^{\top}} \right.$. Let $c^{\ast}$ be the solution to the following convex program,

<!-- chunk {"id": "body-0012", "role": "body", "section": "Asymptotic Lower Bound", "weight": 1.0} -->

The optimization minimizes the regret over (unbounded) allocations $\alpha$ that collect sufficient statistical evidence to reject all parameters $\nu \in \mathcal{C}^{\ast}$ for which an action $x \neq x^{\ast}$ is optimal. Note that for a fixed $\nu \in {\mathbb{R}}^{d}$, the constraints are linear in the allocation, $\left\| {\nu - \theta} \right\|_{V{(\alpha)}}^{2} = \left. \sum{}_{x \in \mathcal{X}}{\alpha(x)\left\langle {\nu - \theta},x \right\rangle^{2}} \right.$. The next lemma is a well-known result, which relates the asymptotic regret to the solution of.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Asymptotic Lower Bound", "weight": 1.0} -->

A policy $\pi$ is called *consistent* if for all $\theta \in \mathcal{M}$ and $p > 0$ it holds that ${R_{n}(\theta,\pi)} = {o\left( n^{p} \right)}$. Assuming consistency is required to rule out policies that are defined to always play a fixed action $x^{\ast}$, which incurs zero regret when $x^{\ast}$ is indeed optimal, but linear regret on other instances.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Asymptotically Optimal Information-Directed Sampling", "weight": 1.0} -->

The information-directed sampling (IDS) principle was introduced by Russo and Van Roy in the Bayesian setting. Our work is based on the frequentist version of this approach, developed by Kirschner and Krause.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Asymptotically Optimal Information-Directed Sampling", "weight": 1.0} -->

Intuitively, this objective requires to sample actions that have either small regret or large information gain. The *information ratio* $\Psi_{t}$ is a convex function of the distribution and can be minimized efficiently as we explain below. In *exploration rounds*, indexed by $s$, IDS samples the action $x_{s}$ from the IDS distribution $\mu_{s}$. Otherwise, in *exploitation rounds*, $x^{\ast}$ is identified with high probability, and the algorithm plays the action it believes to be optimal, denoted by ${\hat{x}}_{s}$ (where $s$ is the index of the last exploration round). The interaction with the environment, described in Algorithm 1.1; Combes et al. ). ‣ Asymptotic Lower Bound ‣ 1.1 Setting ‣ 1 Introduction ‣ Asymptotically Optimal Information-Directed Sampling"), is over rounds $t = {1,\ldots,n}$ on a *horizon* $n$, which is unknown a priori.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Asymptotically Optimal Information-Directed Sampling", "weight": 1.0} -->

Exploration rounds are counted separately by $s$, inducing an implicit mapping $s\mapsto t_{s} \leq t$. The number of exploration rounds up to time $t$ is $s_{t}$. We refer to $s$ and $t$ as *local* and *global time* respectively, and to $s_{n}$ as the *effective horizon*. The convention is that an $s$-index refers to the local time quantities, whereas a $t$-index refers to global time quantities. For example, the action chosen in exploration round $s$ at global time $t_{s}$ is $x_{s}$ and the observed reward is $y_{s}$. Similarly, an action $x_{s}$ at local time $s$ has a global time correspondence $x_{t} = x_{t_{s}}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Gap Estimates", "weight": 1.0} -->

All estimated quantities are defined using data collected in exploration rounds, whereas observation data from exploitation rounds is discarded. To justify this choice intuitively, note that with high probability, in exploration rounds the algorithm samples the optimal action $x^{\ast}$, thereby accumulating exponentially more data points on the optimal actions compared to suboptimal actions. Ignoring data from exploitation rounds leads to a much more balanced data set.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Gap Estimates", "weight": 1.0} -->

For concreteness, we use the choice derived by Abbasi-Yadkori et al., which is

<!-- chunk {"id": "body-0019", "role": "body", "section": "Gap Estimates", "weight": 1.0} -->

The reader might worry about the log determinant term, which is known to create an asymptotically suboptimal dependence on the dimension, and can be improved with a different choice of the confidence coefficient. Since $\beta_{s,{1/\delta}} = {{2{\log\frac{1}{\delta}}} + {\mathcal{O}\left( {d{\log(s)}} \right)}}$, we circumvent this shortcoming by limiting the amount of data the algorithm collects to $s_{n} = \mathcal{O}\left( \text{poly}\left( \log(n) \right) \right.$, which implies $\beta_{s_{n},{1/\delta}} = {{2{\log\frac{1}{\delta}}} + {\mathcal{O}\left( {d{\log{\log(n)}}} \right)}}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Gap Estimates", "weight": 1.0} -->

We also exploit this property for other steps in the analysis, but it is unclear whether or not it is essential.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Gap Estimates", "weight": 1.0} -->

which guarantees that with confidence level $\beta_{s,{t{\log{(t)}}}}$ there exists no plausible alternative parameter $\nu \neq {\hat{\theta}}_{s}$, such that an action $x \neq {\hat{x}}_{s}$ is optimal for $\nu$. At local time $s$, the *gap estimate* is

<!-- chunk {"id": "body-0022", "role": "body", "section": "Gap Estimates", "weight": 1.0} -->

Note that we use a different confidence level in the definition of the gap estimate, and in fact the only explicit dependence on the global time $t$ is in the exploitation condition. The gap estimate is an upper bound on the true gap, provided ${\hat{\theta}}_{s}$ is well concentrated, i.e. $\left\| {{\hat{\theta}}_{s} - \theta^{\ast}} \right\|_{V_{s}}^{2} \leq \beta_{s,s^{2}}$,

<!-- chunk {"id": "body-0023", "role": "body", "section": "Information Gain", "weight": 1.0} -->

where the mixing distribution $q_{s} \in {\mathcal{P}(\mathcal{X})}$ is defined so that

<!-- chunk {"id": "body-0024", "role": "body", "section": "Information Gain", "weight": 1.0} -->

The learning rate is $\eta_{s}{}{\min_{l \leq s}{m_{l}^{- {1/2}}{\log(k)}}}$, where $m_{s}{}\frac{1}{2}{\min_{z \neq {\hat{x}}_{s}}\left\| {{{\hat{\nu}}_{s}(z)} - {\hat{\theta}}_{s}} \right\|_{V_{s}}^{2}}$. The weights $q_{s}$ can be interpreted as a soft-min approximation of the minimum constraint value where the learning rate controls the lower order term (Lemma B.30. ‣ B.5 Technical Lemmas ‣ Appendix B Additional Proofs and Technical Lemmas ‣ Asymptotically Optimal Information-Directed Sampling")),

<!-- chunk {"id": "body-0025", "role": "body", "section": "Computational Complexity", "weight": 1.0} -->

There are three kinds of operations in the algorithm. First, using elementary matrix operations, we can update $V_{s}^{- 1}$, $\det\left( V_{s} \right)$ and ${\hat{\theta}}_{s}$ incrementally, and note that the $s$-index terms only need to be updated after exploration rounds. It can be checked that $\mathcal{O}\left( {kd^{2}s_{n}} \right)$ operations are needed over all $n$ rounds to compute this part. Second, the IDS distribution is defined as a minimizer of the convex objective $\Psi_{s}(\mu)$ and always admits a solution supported on two actions, see Lemma B.2. ‣ B.1 Properties of the IDS Distribution ‣ Appendix B Additional Proofs and Technical Lemmas ‣ Asymptotically Optimal Information-Directed Sampling").

<!-- chunk {"id": "body-0026", "role": "body", "section": "Computational Complexity", "weight": 1.0} -->

Hence, we can obtain the IDS distribution by computing the optimal trade-off between all $\mathcal{O}\left( k^{2} \right)$ pairs of actions (Lemma B.3). A closer inspection of the regret bounds reveals that it always suffices to optimize the trade-off between the greedy action ${\hat{x}}_{s}$ and some other (informative) action, which reduces the computational complexity to $\mathcal{O}(k)$. Third, the optimization problem that defines the alternative parameters ${\hat{\nu}}_{s}(z)$ is a quadratic program with $d$ variables and linear constraints $\left\langle {{\hat{\nu}}_{s}(z)},{z - {\hat{x}}_{s}} \right\rangle \geq 0$ and ${{\hat{\nu}}_{s}(z)} \in \mathcal{M}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Computational Complexity", "weight": 1.0} -->

Such optimization problems can be solved efficiently in practice and in $O\left( {ld^{3}} \right)$ time in the worst case for model sets $\mathcal{M}$ with $l$ constraints. Note, the analysis suggests that we can tolerate an additive numerical error on the information gain of order $\mathcal{O}\left( s^{- 2} \right)$. In practice, we can drop the constraints on $\mathcal{M}$, in which case

<!-- chunk {"id": "body-0028", "role": "body", "section": "Computational Complexity", "weight": 1.0} -->

With these improvements, the overall computation complexity is $\mathcal{O}\left( {n + {kd^{2}s_{n}}} \right)$ over $n$ rounds, where the linear term comes from checking whether to explore or exploit. This can be improved, by simply computing after each exploration round when the next exploration round will occur.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Regret Bounds", "weight": 1.0} -->

The regret bounds for Algorithm 1.1; Combes et al. ). ‣ Asymptotic Lower Bound ‣ 1.1 Setting ‣ 1 Introduction ‣ Asymptotically Optimal Information-Directed Sampling") come in three flavours. In Theorem 2.1. ‣ 2.1 Regret Bounds ‣ 2 Asymptotically Optimal Information-Directed Sampling ‣ Asymptotically Optimal Information-Directed Sampling"), we show a (nearly) optimal worst-case regret bound of $R_{n} \leq {\mathcal{O}\left( {d\sqrt{n}{\log(n)}} \right)}$. Second, using a gap-dependent bound on the information ratio, in Theorem 2.3. ‣ 2.1 Regret Bounds ‣ 2 Asymptotically Optimal Information-Directed Sampling ‣ Asymptotically Optimal Information-Directed Sampling") we show a gap-dependent regret bound of $R_{n} \leq \mathcal{O}\left( d^{3}\Delta_{\min}^{- 1}\log(n)^{2} \right)$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Regret Bounds", "weight": 1.0} -->

Besides universal constants, the $\mathcal{O}$-notation in the bound only depends on the norm of action features and the parameter. Last, in Theorem 2.6. ‣ 2.1 Regret Bounds ‣ 2 Asymptotically Optimal Information-Directed Sampling ‣ Asymptotically Optimal Information-Directed Sampling") we show that the proposed algorithm is asymptotically optimal, that is $R_{n} \leq {{c^{\ast}{\log(n)}} + {o\left( {\log(n)} \right)}}$. In contrast to the previous bound, here the lower order terms depend exponentially on problem-dependent quantities such as $\Delta_{\min}^{- 1}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Alternative Definitions of the Information Gain", "weight": 1.0} -->

Our definition of the information gain ensures that ${I_{s}(x)} \approx {\frac{1}{2}\left. \sum{}_{z \neq {\hat{x}}_{s}}{q_{s}(z)\left\langle {{{\hat{\nu}}_{s}(z)} - {\hat{\theta}}_{s}},x \right\rangle^{2}} \right.}$ asymptotically. In finite time, however, the mean estimates can be inaccurate. Therefore, we add an optimistic term in the definition of the information gain, which is an essential ingredient in the proof of Theorem 2.1. ‣ 2.1 Regret Bounds ‣ 2 Asymptotically Optimal Information-Directed Sampling ‣ Asymptotically Optimal Information-Directed Sampling"). At the same time, the optimistic term corresponds to an information gain which was analyzed in earlier work. Since this choice is motivated from a worst-case perspective, empirically it sometimes leads to over-exploration in the finite-time regime.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Alternative Definitions of the Information Gain", "weight": 1.0} -->

A closer inspection of the worst-case regret proof (in particular, Eq. 11) reveals that the optimistic term is only needed for the UCB action.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Alternative Definitions of the Information Gain", "weight": 1.0} -->

With a few additional steps in the proof of Lemma B.9. ‣ B.2 Bounds on the Information Ratio ‣ Appendix B Additional Proofs and Technical Lemmas ‣ Asymptotically Optimal Information-Directed Sampling") and Theorem 2.6. ‣ 2.1 Regret Bounds ‣ 2 Asymptotically Optimal Information-Directed Sampling ‣ Asymptotically Optimal Information-Directed Sampling"), the resulting algorithm is shown to satisfy the same regret bounds as presented in Theorems 2.1. ‣ 2.1 Regret Bounds ‣ 2 Asymptotically Optimal Information-Directed Sampling ‣ Asymptotically Optimal Information-Directed Sampling"), 2.3. ‣ 2.1 Regret Bounds ‣ 2 Asymptotically Optimal Information-Directed Sampling ‣ Asymptotically Optimal Information-Directed Sampling") and 2.6. ‣ 2.1 Regret Bounds ‣ 2 Asymptotically Optimal Information-Directed Sampling ‣ Asymptotically Optimal Information-Directed Sampling"). Since the proofs are very similar, we omit the details. We compare both information gain functions in our experiments. Another variant is to set the alternative parameters to

<!-- chunk {"id": "body-0034", "role": "body", "section": "Alternative Definitions of the Information Gain", "weight": 1.0} -->

Note that all bounds that we obtain hold true for IDS defined with $I_{s}^{\mathcal{C}}$ as well, by replacing $\mathcal{H}_{x}^{{\hat{x}}_{s}}$ with $\mathcal{C}_{x}$ in the proof. The key insight is that $\mathcal{C}^{\ast} = {\cup_{x \neq x^{\ast}}\mathcal{C}_{x}} = {\cup_{x \neq x^{\ast}}\mathcal{H}_{x}^{x^{\ast}}}$, hence the change is simply a different decomposition of the set of alternative parameters $\mathcal{C}^{\ast}$ into convex regions. One might expect faster convergence from the fact that ${\overset{\sim}{q}}_{s}$ is more concentrated, but empirically we find little difference compared to $I_{s}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Alternative Definitions of the Information Gain", "weight": 1.0} -->

On the other hand, for unconstrained parameter sets $\mathcal{M}$, we can compute ${\hat{\nu}}_{s}(z)$ in closed form (Eq. 10), whereas ${\overset{\sim}{\nu}}_{s}(z)$ can only be computed by solving a positive definite quadratic program with $k$ linear constraints for each action $z \neq {\hat{x}}_{s}$. Interestingly, however, the information gain relates to the Bayesian mutual information ${\mathbb{I}}_{s}\left( {{y_{s};\left. x^{\ast} \middle| x_{s} \right.} = x} \right)$. The argument uses concentration of measure to show that ${\overset{\sim}{q}}_{s}(x)$ approximates the posterior probability that an action $x \neq x^{\ast}$ is optimal in the Bayesian model. We refer to Appendix D for details.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Information-Directed Sampling as a Primal-Dual Approach", "weight": 1.0} -->

Lemma B.5. ‣ B.1 Properties of the IDS Distribution ‣ Appendix B Additional Proofs and Technical Lemmas ‣ Asymptotically Optimal Information-Directed Sampling") shows that the IDS distribution $\mu_{s}$ is supported on actions $x$ that minimize the function

<!-- chunk {"id": "body-0037", "role": "body", "section": "Information-Directed Sampling as a Primal-Dual Approach", "weight": 1.0} -->

The approximation holds because asymptotically, ${\Psi_{s}\left( \mu_{s} \right)} \approx {4c^{\ast}\delta_{s}}$ and ${{\hat{\Delta}}_{s}\left( \mu_{s} \right)} \approx {2\delta_{s}}$. The weight $c^{\ast}$ appears from normalizing the Lagrange multipliers as discussed in Appendix C. Therefore, the IDS distribution can be understood as a type of best-response on the primal-dual game defined by the Lagrangian of the lower bound, where the dual variables correspond to the $q$-weights of the information gain. Note that the best response on $g_{s}$ is not unique, and IDS chooses a particular, randomized trade-off, which is imposed by the IDS objective.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Information-Directed Sampling as a Primal-Dual Approach", "weight": 1.0} -->

The first work which exploits the primal-dual formulation for regret minimization is by Degenne et al.. In our notation, their algorithm corresponds to choosing the action with the best information-regret trade-off $z_{s} = {\left. {{{\arg\min}_{x \in \mathcal{X}}{\hat{\Delta}}_{s}}(x)}/I_{s} \right.(x)}$. IDS instead asymptotically randomizes between $x^{\ast}$ and $z_{s}$, which allows it to maintain the worst-case regret bound. Another more recent primal-dual approach is the solid algorithm by Tirinzoni et al.. This approach uses a different Lagrangian, which is defined by keeping the minimum over $\mathcal{C}^{\ast}$. Accordingly, the dual variable is one-dimensional, but the constraints appear non-smooth. solid is defined by alternating (optimistic) sub-gradient steps on the allocation and the dual variable.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Information-Directed Sampling as a Primal-Dual Approach", "weight": 1.0} -->

This leads to a randomized strategy over actions with exponential weights that are only updated when an exploration condition is satisfied.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiments", "weight": 1.0} -->

We compare IDS with LinUCB and solid, the latter being our closest competitor. Note that solid was shown to outperform OAM and LinTS in a variety of settings. To the best of our knowledge, solid is the current state-of-the-art for asymptotically optimal algorithms.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experiments", "weight": 1.0} -->

To enable a fair comparison, we use the same confidence coefficient $\beta_{t,{1/\delta}}$ for all algorithms. We also run the same experiment with the (tighter) confidence coefficient derived by Tirinzoni et al., but we found no significant difference in the results, see Appendix E. For solid, we use the default hyper-parameters suggested by Tirinzoni et al.. Finally, as recommended by the authors, we implement a variant of the solid algorithm, which is (heuristically) optimized for better performance in finite time and does not reset the sampling vector $\omega_{t}$ at the beginning of each phase. We display that improved version as solid++.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experiments", "weight": 1.0} -->

IDS is implemented as in Algorithm 1.1; Combes et al. ). ‣ Asymptotic Lower Bound ‣ 1.1 Setting ‣ 1 Introduction ‣ Asymptotically Optimal Information-Directed Sampling") with the computational improvements described at the end of Section 2. In particular, we use an unconstrained parameter set ($\mathcal{M} = {\mathbb{R}}^{d}$), which allows us to compute the parameter ${\hat{\nu}}_{s}(x)$ in closed form. We further compute the IDS distribution randomizing only between ${\hat{x}}_{t}$ and one other action (Lemma B.5. ‣ B.1 Properties of the IDS Distribution ‣ Appendix B Additional Proofs and Technical Lemmas ‣ Asymptotically Optimal Information-Directed Sampling")) to reduce the per-round computational complexity from $\mathcal{O}\left( k^{2} \right)$ to $\mathcal{O}(k)$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experiments", "weight": 1.0} -->

All variants of IDS used in the experiments satisfy the theoretical guarantees presented in this paper with minor proof modifications. We also compare to IDS-$I^{\mathcal{H}\text{-UCB}}$ defined with information gain. In Appendix E, we present further empirical evidence, including a benchmark with Thompson Sampling and Bayesian IDS, a comparison of information gain functions, and an evaluation of the tuning sensitivity of the $\beta_{s}$ and $\eta_{s}$ parameters.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Average performance on random problems", "weight": 1.0} -->

For each repetition, we sample an action set with 6 actions drawn uniformly from the unit sphere. We set $d = 2$ and the variance of the noise to $\sigma^{2} = 0.1$, which is chosen so that the asymptotic regime is observed after fewer rounds relative to $\sigma^{2} = 1$. The results are shown in the first row of Figure 1. We display the average over 100 runs and $95\%$ confidence intervals. All policies except for solid have comparable averaged performances, but the latter is not designed to optimize for worst-case regret in principle. IDS-$I^{\mathcal{H}\text{-UCB}}$ is similar to LinUCB, followed by IDS-$I^{\mathcal{H}}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "The End of Optimism?", "weight": 1.0} -->

This example of a 2-dimensional linear bandit dates back to Soare et al., and was used by Lattimore and Szepesvári to show that algorithms based on optimism and Thompson sampling are not asymptotically optimal in the linear setting. There are three arms $x_{1} = $, $x_{2} = \left( {1 - \epsilon},{2\epsilon} \right)$ and $x_{3} = $ with a tuning variable $\epsilon > 0$. The true parameter is $\theta = $ which makes action $x_{1}$ optimal. The situation is illustrated in Figure 2. The colored regions $\mathcal{C}_{1},\mathcal{C}_{2}$ and $\mathcal{C}_{3}$ are the corresponding *cells*, i.e. the subset of parameters in ${\mathbb{R}}^{2}$ for which $x_{1}$, $x_{2}$ or $x_{3}$ is optimal respectively.

<!-- chunk {"id": "body-0046", "role": "body", "section": "The End of Optimism?", "weight": 1.0} -->

Algorithms based on optimism and Thompson sampling quickly rule out the suboptimal arm $x_{3}$ and just play either $x_{1}$ or $x_{2}$. The twist is that the third arm is still informative for determining $a^{\ast}$, and in fact an asymptotically optimal algorithm plays only on $\left\{ x_{1},x_{3} \right\}$. To see why, note that any no-regret learner plays $x^{\ast} = x_{1}$ a lot, therefore the parameter is well-estimated along the direction $x_{1}$. It remains to shrink the confidence ellipsoid approximately along the direction $x_{3}$, which means increasing the $V_{t}$-norm of $x_{3}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "The End of Optimism?", "weight": 1.0} -->

Choosing arm $x_{2}$ incurs a small cost $\epsilon$, but the increase of the confidence ellipsoid in direction $x_{3}$ is only small, $\left\langle x_{3},{\left( {V_{t + 1} - V_{t}} \right)x_{3}} \right\rangle = \left\langle x_{3},x_{2} \right\rangle^{2} = \epsilon^{2}$. On the other hand, choosing $x_{3}$ implies a higher regret cost of $1$, but the confidence set is increased by $1$ along direction $x_{3}$, which allows to identify the optimal action at a much smaller cost. An optimistic algorithm has an asymptotic regret that scales with $R_{n} \approx \left. {\log(n)}/\epsilon \right.$, while for an optimal algorithm, $R_{n} \approx {1 \cdot {\log(n)}}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "The End of Optimism?", "weight": 1.0} -->

In fact, for some small $\epsilon$, the lower bound constant is $c^{\ast} = 64$ and does not depend on $\epsilon$, so optimistic algorithms cannot be asymptotically optimal.

<!-- chunk {"id": "body-0049", "role": "body", "section": "The End of Optimism?", "weight": 1.0} -->

For the experiments, we use noise variance $\sigma^{2} = 0.1$, and $\epsilon = 0.01$, which is sufficiently large to reach the asymptotic regime within $n = 10^{6}$ rounds, and small enough to highlight the difference between UCB and IDS. Results in this setting are shown in the bottom row of Figure 1. As expected, LinUCB's asymptotics show a suboptimal log-slope, but it is surprisingly followed by solid++. Despite our attempts, we are presently not able to provide a good explanation for this result and it might require a more involved analysis of the solid++ heuristic. However, both versions of IDS and the theoretical solid reach the optimal asymptotic around $t = 10^{5}$ ($10^{4}$ for solid) and significantly outperform LinUCB on that problem. An interesting observation is that IDS-$I_{s}^{\text{UCB}}$ performs better in finite time, whereas IDS-$I_{s}$ reaches the asymptotic regime earlier.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced a simple and efficient algorithm for linear bandits that is (nearly) worst-case optimal and matches the asymptotic lower bound exactly. Note that the algorithm is essentially hyper-parameter free with the usual boundedness assumptions. Nonetheless, the confidence parameter $\beta_{s,{1/\delta}}$ and the learning rate $\eta_{s}$ used in the definition of $I_{s}$ provide some tuning knobs to improve performance in practice.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our theoretical results still rely on some restrictive assumptions, such as the boundedness requirement for the parameter set, uniqueness of $x^{\ast}$ and $\left\| x^{\ast} \right\| > 0$ for the asymptotic regret, and the need to discard data in exploitation rounds. Also, the dependence on $d$ and $k$ is sub-optimal in some regimes, in particular for the worst-case regret bound and small $k$. On the upside, our analysis is relatively simple, and raises the hope that there exists a *really* simple proof. Finding an information gain which preserves the guarantees and telescopes more easily could be a first step towards this end.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Finally, it appears likely that our framework generalizes in several directions. The contextual case is already covered in previous work on asymptotic algorithms. We point out that IDS can be defined to optimize the marginals of the joint distribution between context and action. Decoupling the reward from the observation features leads to the linear partial monitoring framework, where IDS is known to achieve the optimal worst-case rate in all possible games. The structured bandit setting and information gain functions for a non-Gaussian likelihood are yet other promising directions.
