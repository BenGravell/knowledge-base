<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Unifying PAC and Regret: Uniform PAC Bounds for Episodic Reinforcement Learning

Topics include Reinforcement learning, Regret bounds, Learning, Probably approximately correct.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Statistical performance bounds for reinforcement learning (RL) algorithms can be critical for high-stakes applications like healthcare. This paper introduces a new framework for theoretically measuring the performance of such algorithms called Uniform-PAC, which is a strengthening of the classical Probably Approximately Correct (PAC) framework. In contrast to the PAC framework, the uniform version may be used to derive high probability regret guarantees and so forms a bridge between the two setups that has been missing in the literature. We demonstrate the benefits of the new framework for finite-state episodic MDPs with a new algorithm that is Uniform-PAC and simultaneously achieves optimal regret and PAC guarantees except for a factor of the horizon.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The recent empirical successes of deep reinforcement learning (RL) are tremendously exciting, but the performance of these approaches still varies significantly across domains, each of which requires the user to solve a new tuning problem. Ultimately we would like reinforcement learning algorithms that simultaneously perform well empirically and have strong theoretical guarantees. Such algorithms are especially important for high stakes domains like health care, education and customer service, where non-expert users demand excellent outcomes.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a new framework for measuring the performance of reinforcement learning algorithms called Uniform-PAC. Briefly, an algorithm is Uniform-PAC if with high probability it simultaneously for all $\varepsilon > 0$ selects an $\varepsilon$-optimal policy on all episodes except for a number that scales polynomially with $1/\varepsilon$. Algorithms that are Uniform-PAC converge to an optimal policy with high probability and immediately yield both PAC and high probability regret bounds, which makes them superior to algorithms that come with only PAC or regret guarantees. Indeed,

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Neither PAC nor regret guarantees imply convergence to optimal policies with high probability;

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

$(\varepsilon,\delta)$-PAC algorithms may be $\varepsilon/2$-suboptimal in every episode;

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Algorithms with small regret may be maximally suboptimal infinitely often.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Uniform-PAC algorithms suffer none of these drawbacks. One could hope that existing algorithms with PAC or regret guarantees might be Uniform-PAC already, with only the analysis missing. Unfortunately this is not the case and modification is required to adapt these approaches to satisfy the new performance metric. The key insight for obtaining Uniform-PAC guarantees is to leverage time-uniform concentration bounds such as the finite-time versions of the law of iterated logarithm, which obviates the need for horizon-dependent confidence levels.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide a new optimistic algorithm for episodic RL called UBEV that is Uniform PAC. Unlike its predecessors, UBEV uses confidence intervals based on the law of iterated logarithm (LIL) which hold uniformly over time. They allow us to more tightly control the probability of failure events in which the algorithm behaves poorly. Our analysis is nearly optimal according to the traditional metrics, with a linear dependence on the state space for the PAC setting and square root dependence for the regret. Therefore UBEV is a Uniform PAC algorithm with PAC bounds and high probability regret bounds that are near optimal in the dependence on the length of the episodes (horizon) and optimal in the state and action spaces cardinality as well as the number of episodes. To our knowledge UBEV is the first algorithm with both near-optimal PAC and regret guarantees.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Uniform PAC and Existing Learning Frameworks", "weight": 1.0} -->

We briefly summarize the most common performance measures used in the literature.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Uniform PAC and Existing Learning Frameworks", "weight": 1.0} -->

$(\varepsilon,\delta)$-PAC: There exists a polynomial function $F_{\text{PAC}}{(S,A,H,{1/\varepsilon},{\log{({1/\delta})}})}$ such that

<!-- chunk {"id": "body-0012", "role": "body", "section": "Uniform PAC and Existing Learning Frameworks", "weight": 1.0} -->

High Probability Regret: There exists a function $F_{\text{HPR}}{(S,A,H,T,{\log{({1/\delta})}})}$ such that

<!-- chunk {"id": "body-0013", "role": "body", "section": "Uniform PAC and Existing Learning Frameworks", "weight": 1.0} -->

Uniform High Probability Regret: There exists a function $F_{\text{UHPR}}{(S,A,H,T,{\log{({1/\delta})}})}$ such that

<!-- chunk {"id": "body-0014", "role": "body", "section": "Uniform PAC and Existing Learning Frameworks", "weight": 1.0} -->

In all definitions the function $F$ should be polynomial in all arguments. For notational conciseness we often omit some of the parameters of $F$ where the context is clear. The different performance guarantees are widely used (e.g. PAC:, (uniform) high-probability regret:; expected regret: ). Due to space constraints, we will not discuss Bayesian-style performance guarantees that only hold in expectation with respect to a distribution over problem instances. We will shortly discuss the limitations of the frameworks listed above, but first formally define the Uniform-PAC criteria

<!-- chunk {"id": "body-0015", "role": "body", "section": "Limitations of regret", "weight": 1.5} -->

Since regret guarantees only bound the integral of $\Delta_{k}$ over $k$, it does not distinguish between making a few severe mistakes and many small mistakes. In fact, since regret bounds provably grow with the number of episodes $T$, an algorithm that achieves optimal regret may still make infinitely many mistakes (of arbitrary quality, see proof of Theorem 2 below). This is highly undesirable in high-stakes scenarios. For example in drug treatment optimization in healthcare, we would like to distinguish between infrequent severe complications (few large $\Delta_{k}$) and frequent minor side effects (many small $\Delta_{k}$). In fact, even with an optimal regret bound, we could still serve infinitely patients with the worst possible treatment.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Limitations of PAC", "weight": 1.5} -->

PAC bounds limit the number of mistakes for a given accuracy level $\varepsilon$, but is otherwise non-restrictive. That means an algorithm with $\Delta_{k} > {\varepsilon/2}$ for all $k$ almost surely might still be $(\varepsilon,\delta)$-PAC. Worse, many algorithms designed to be $(\varepsilon,\delta)$-PAC actually exhibit this behavior because they explicitly halt learning once an $\varepsilon$-optimal policy has been found. The less widely used TCE (total cost of exploration) bounds and KWIK guarantees suffer from the same issueand for conciseness are not discussed in detail.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Advantages of Uniform-PAC", "weight": 1.0} -->

The new criterion overcomes the limitations of PAC and regret guarantees by measuring the number of $\varepsilon$-errors at every level simultaneously. By definition, algorithms that are Uniform-PAC for a $\delta$ are $(\varepsilon,\delta)$-PAC for all $\varepsilon > 0$. We will soon see that an algorithm with a non-trivial Uniform-PAC guarantee also has small regret with high probability. Furthermore, there is no loss in the reduction so that an algorithm with optimal Uniform-PAC guarantees also has optimal regret, at least in the episodic RL setting. In this sense Uniform-PAC is the missing bridge between regret and PAC. Finally, for algorithms based on confidence bounds, Uniform-PAC guarantees are usually obtained without much additional work by replacing standard concentration bounds with versions that hold uniformly over episodes (e.g. using the law of the iterated logarithms). In this sense we think Uniform-PAC is the new 'gold-standard' of theoretical guarantees for RL algorithms.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Relationships between Performance Guarantees", "weight": 1.0} -->

Existing theoretical analyses usually focus exclusively on either the regret or PAC framework. Besides occasional heuristic translations, Proposition 4 in and Corollary 3 in are the only results relating a notion of PAC and regret, we are aware of. Yet the guarantees there are not widely used^22^2The average per-step regret in is superficially a PAC bound, but does not hold over infinitely many time-steps and exhibits the limitations of a conventional regret bound. The translation to average loss in comes at additional costs due to the discounted infinite horizon setting. unlike the definitions given above which we now formally relate to each other. A simplified overview of the relations discussed below is shown in Figure 1.

<!-- chunk {"id": "body-0019", "role": "body", "section": "The UBEV Algorithm", "weight": 1.0} -->

The pseudo-code for the proposed UBEV algorithm is given in Algorithm 1. In each episode it follows an optimistic policy $\pi_{k}$ that is computed by backwards induction using a carefully chosen confidence interval on the transition probabilities in each state. In line 1 an optimistic estimate of the Q-function for the current state-action-time triple is computed using the empirical estimates of the expected next state value ${\hat{V}}_{\text{next}} \in {\mathbb{R}}$ (given that the values at the next time are ${\overset{\sim}{V}}_{t + 1}$) and expected immediate reward $\hat{r}$ plus confidence bounds ${({H - t})}\phi$ and $\phi$. We show in Lemma D.1.

<!-- chunk {"id": "body-0020", "role": "body", "section": "The UBEV Algorithm", "weight": 1.0} -->

‣ Appendix D Planning Problem of UBEV ‣ Unifying PAC and Regret: Uniform PAC Bounds for Episodic Reinforcement Learning") in the appendix that the policy update in Lines 1--1 finds an optimal solution to ${\max_{P^{\prime},r^{\prime},V^{\prime},\pi^{\prime}}{\mathbb{E}}_{s \sim p_{0}}}{\lbrack{V_{1}^{\prime}{(s)}}\rbrack}$ subject to the constraints that for all ${s \in \mathcal{S}},{{a \in \mathcal{A}},{t \in {\lbrack H\rbrack}}}$,

<!-- chunk {"id": "body-0021", "role": "body", "section": "The UBEV Algorithm", "weight": 1.0} -->

Instead of using confidence intervals over the transition kernel by itself, we incorporate the value function directly into the concentration analysis. Ultimately this saves a factor of $S$ in the sample complexity, but the price is a more difficult analysis. Previously MoRMax also used the idea of directly bounding the transition and value function, but in a very different algorithm that required discarding data and had a less tight bound. A similar technique has been used by Azar et al..

<!-- chunk {"id": "body-0022", "role": "body", "section": "The UBEV Algorithm", "weight": 1.0} -->

Many algorithms update their policy less and less frequently (usually when the number of samples doubles), and only finitely often in total. Instead, we update the policy after every episode, which means that UBEV immediately leverages new observations.

<!-- chunk {"id": "body-0023", "role": "body", "section": "The UBEV Algorithm", "weight": 1.0} -->

Confidence bounds in existing algorithms that keep improving the policy (e.g. Jaksch et al., Azar et al. ) scale at a rate $\sqrt{{\log{(k)}}/n}$ where $k$ is the number of episodes played so far and $n$ is the number of times the specific ($s,a,t$) has been observed. As the results of a brief empirical comparison in Figure 2 indicate, this leads to slow learning (compare UCBVI_1 and UBEV's performance which differ essentially only by their use of different rate bounds). Instead the width of UBEV's confidence bounds $\phi$ scales at rate $\sqrt{\ln{{\ln{({\max{\{ e,n\}}})}}/n}} \approx \sqrt{{({\log{\log n}})}/n}$ which is the best achievable rate and results in significantly faster learning.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Uniform PAC Analysis", "weight": 1.0} -->

We now discuss the Uniform-PAC analysis of UBEV which results in the following Uniform-PAC and regret guarantee.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Enabling Uniform PAC With Law-of-Iterated-Logarithm Confidence Bounds", "weight": 1.0} -->

To have a PAC bound for all $\varepsilon$ jointly, it is critical that UBEV continually make use of new experience. If UBEV stopped leveraging new observations after some fixed number, it would not be able to distinguish with high probability among which of the remaining possible MDPs do or do not have optimal policies that are sufficiently optimal in the other MDPs. The algorithm therefore could potentially follow a policy that is not at least $\varepsilon$-optimal for infinitely many episodes for a sufficiently small $\varepsilon$. To enable UBEV to incorporate all new observations, the confidence bounds in UBEV must hold for an infinite number of updates. We therefore require a proof that the total probability of all possible failure events (of the high confidence bounds not holding) is bounded by $\delta$, in order to obtain high probability guarantees. In contrast to prior $(\varepsilon,\delta)$-PAC proofs that only consider a finite number of failure events (which is enabled by requiring an RL algorithm to stop using additional data), we must bound the probability of an infinite set of possible failure events.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Enabling Uniform PAC With Law-of-Iterated-Logarithm Confidence Bounds", "weight": 1.0} -->

Some choices of confidence bounds will hold uniformly across all sample sizes but are not sufficiently tight for uniform PAC results. For example, the recent work by Azar et al. uses confidence intervals that shrink at a rate of $\sqrt{\frac{\ln T}{n}}$, where $T$ is the number of episodes, and $n$ is the number of samples of a $(s,a)$ pair at a particular time step. This confidence interval will hold for all episodes, but these intervals do not shrink sufficiently quickly and can even increase. One simple approach for constructing confidence intervals that is sufficient for uniform PAC guarantees is to combine bounds for fixed number of samples with a union bound allocating failure probability $\delta/n^{2}$ to the failure case with $n$ samples. This results in confidence intervals that shrink at rate $\sqrt{{1/n}{\ln n}}$. Interestingly we know of no algorithms that do such in our setting.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Enabling Uniform PAC With Law-of-Iterated-Logarithm Confidence Bounds", "weight": 1.0} -->

We follow a similarly simple but much stronger approach of using law-of-iterated logarithm (LIL) bounds that shrink at the better rate of $\sqrt{{1/n}{\ln{\ln n}}}$. Such bounds have sparked recent interest in sequential decision making but to the best of our knowledge we are the first to leverage them for RL. We prove several general LIL bounds in Appendix F and explain how we use these results in our analysis in Appendix E.2. These LIL bounds are both sufficient to ensure uniform PAC bounds, and much tighter (and therefore will lead to much better performance) than $\sqrt{{1/n}{\ln T}}$ bounds. Indeed, LIL have the tightest possible rate dependence on the number of samples $n$ for a bound that holds for all timesteps (though they are not tight with respect to constants).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Discussion of UBEV Bound", "weight": 1.5} -->

The (Uniform-)PAC bound for UBEV in Theorem 4 is never worse than $\overset{\sim}{O}{({{S^{2}AH^{4}}/\varepsilon^{2}})}$, which improves on the similar MBIE algorithm by a factor of $H^{2}$ (after adapting the discounted setting for which MBIE was analysed to our setting). For $\varepsilon < {1/{({S^{2}A})}}$ our bound has a linear dependence on the size of the state-space and depends on $H^{4}$, which is a tighter dependence on the horizon than MoRMax's $\overset{\sim}{O}{({{SAH^{6}}/\varepsilon^{2}})}$, the best sample-complexity bound with linear dependency $S$ so far.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Discussion of UBEV Bound", "weight": 1.5} -->

Comparing UBEV's regret bound to the ones of UCRL2 and REGAL requires care because (a) we measure the regret over entire episodes and (b) our transition dynamics are time-dependent within each episode, which effectively increases the state-space by a factor of $H$. Converting the bounds for UCRL2/REGAL to our setting yields a regret bound of order $SH^{2}\sqrt{AHT}$. Here, the diameter is $H$, the state space increases by $H$ due to time-dependent transition dynamics and an additional $\sqrt{H}$ is gained by stating the regret in terms of episodes $T$ instead of time steps. Hence, UBEV's bounds are better by a factor of $\sqrt{SH}$. Our bound matches the recent regret bound for episodic RL by Azar et al. in the $S$, $A$ and $T$ terms but not in $H$. Azar et al. has regret bounds that are optimal in $H$ but their algorithm is not uniform PAC, due to the characteristics we outlined in Section 2.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The Uniform-PAC framework strengthens and unifies the PAC and high-probability regret performance criteria for reinforcement learning in episodic MDPs. The newly proposed algorithm is Uniform-PAC, which as a side-effect means it is the first algorithm that is both PAC and has sub-linear (and nearly optimal) regret. Besides this, the use of law-of-the-iterated-logarithm confidence bounds in RL algorithms for MDPs provides a practical and theoretical boost at no cost in terms of computation or implementation complexity.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This work opens up several immediate research questions for future work. The definition of Uniform-PAC and the relations to other PAC and regret notions directly apply to multi-armed bandits and contextual bandits as special cases of episodic RL, but not to infinite horizon reinforcement learning. An extension to these non-episodic RL settings is highly desirable. Similarly, a version of the UBEV algorithm for infinite-horizon RL with linear state-space sample complexity would be of interest. More broadly, if theory is ever to say something useful about practical algorithms for large-scale reinforcement learning, then it will have to deal with the unrealizable function approximation setup (unlike the tabular function representation setting considered here), which is a major long-standing open challenge.\
