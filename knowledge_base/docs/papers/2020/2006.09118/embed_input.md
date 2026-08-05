<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Q-learning with Logarithmic Regret

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents the first non-asymptotic result showing that a model-free algorithm can achieve a logarithmic cumulative regret for episodic tabular reinforcement learning if there exists a strictly positive sub-optimality gap in the optimal Q-function. We prove that the optimistic Q-learning studied in [Jin et al. 2018] enjoys a O(fracSA* poly(H){Delta_min}log(SAT)) cumulative regret bound, where S is the number of states, A is the number of actions, H is the planning horizon, T is the total number of steps, and Delta_min is the minimum sub-optimality gap. This bound matches the information theoretical lower bound in terms of S,A,T up to a log(SA) factor. We further extend our analysis to the discounted setting and obtain a similar logarithmic cumulative regret bound.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

$Q$-learning[watkins1992q] is one of the most popular classes of methods for solving reinforcement learning (RL) problems. $Q$-learning tries to estimate the optimal state-action value function ($Q$-function). With a $Q$-function, at every state, one can just greedily choose the action with the largest $Q$ value to interact with the RL environment. Compared to another popular class of methods, model-based learning, $Q$-learning algorithms (or more generally, model-free algorithms) often enjoy better memory and time efficiency See Sectionsec:pre for the precise definitions of model-free and model-based algorithms in the tabular setting.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

These are the main reasons why $Q$-learning is applied in solving a wide range of RL problems[mnih2015human].

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

While model-free methods are widely applied in practice, most theoretical works study model-based RL. In one of the most fundamental RL frameworks, tabular RL, which is the focus of this paper, the majority of works study model-based algorithms[kearns1999finite, kakade2003sample, singh1994upper, azar2013minimax,azar2017minimax,dann2015sample,dann2017unifying,agarwal2019optimality,max2019nonasymptotic] with a few exceptions [strehl2006pac,jin2018qlearning,dong2019qlearning,zhang2020optimal]. From a regret minimization point of view, the state-of-the-art analysis demonstrates that one can achieve a $\sqrt{T}$-type regret bound where $T$is the number of episodes. Although these bounds are sharp in the worst-case scenario, they do not reveal the favorable structures of the environment, which can significantly decrease the regret.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

One such structure is the existence of a strictly positive sub-optimality gap, i.e., for every state, there is a strictly positive value gap between the optimal action(s) and the rest (cf. Definition[defn:gap]). In practice, arguably, nearly all environments with finite action sets satisfy some sub-optimality gap conditions. In Atari-games, e.g., Freeway, the optimal action has a value that is usually very distinctive from the rest of actions. In many other environments with finite number of actions, e.g. those control environments in OpenAI gym [1606.01540], the gap condition usually holds. Similar gap conditions can be observed in other environments (see e.g. [kakade2003sample]).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Theoretically, the sub-optimality gap is extensively investigated in the bandit problems, which can be viewed as RL problems with the planning horizon being $1$. With this structure, one can drastically decrease the $\sqrt{T}$-type regret to $\log T$-type regret[bubeck2012regret,lattimore2018bandit,slivkins2019introduction]. For RL, most existing works that can leverage this structure require additional assumptions about the environment, such as finite hitting time and ergodicity[jaksch2010near,tewari2007reinforcement,ok2018exploration] or access to a generator[zanette2019almost].

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The simulator allows the user to query any state-action pair.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, [max2019nonasymptotic] presented a systematic study of episodic tabular RL with the gap structure. They presented a novel algorithm which achieves the near-optimal $\sqrt{T}$-type regret in the worst scenario and $\log T$-type regret if there exists a strictly positive sub-optimality gap. Furthermore, they also provided instance-dependent lower bounds for a class of reasonable algorithms. See Section[sec:rel]for more detailed discussions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, to our knowledge, all existing works that obtain $\log T$-type regret bounds are about model-based algorithms. It remains open whether model-free algorithms such as $Q$-learning can achieve $\log T$-type regret bounds. Indeed, this is a challenging task. As discussed in [max2019nonasymptotic], their analysis framework cannot be applied to model-free algorithms directly. Later in this section, we also provide some technical explanations on why their approach is difficult to adopt.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We answer the aforementioned open problem by proving that the optimistic $Q$-learning algorithm studied in [jin2018qlearning] enjoys $\cO\!\left(\frac{SA H^6}{\Delta_{\min}}\log \left(SAT\right)\right)$ cumulative regret where $S$ is the number states, $A$ is the number of actions, $H$ is the planning horizon and $\Delta_{\min}$ is the minimum sub-optimality gap. To our knowledge, this is the first result showing model-free algorithms can achieve $\log T$-type regret. Furthermore, our bound matches the lower bound by[max2019nonasymptotic] in terms of $S$, $A$ and $T$ up to a $\log\left(SA\right)$ factor. Importantly, the algorithm does not need to know $\Delta_{\min}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, we extend our analysis to the infinite-horizon discounted setting with the regret defined in [liu2020regret], for which we show the optimistic $Q$-learning achieves $\cO\!\left(\frac{SA}{\Delta_{\min}\left(1-\gamma\right)^6}\log\left(\frac{SAT}{\Delta_{\min} \left(1-\gamma\right)}\right)\right)$ regret where $0 \!<\! \gamma\! <\! 1$is the discount factor.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Here we explain the main challenges of using existing analyses and give an overview of our main techniques at a high level. The existing proof in [jin2018qlearning] bounds the regret in terms of a weighted sum of the estimation error of $Q$-function. Note the estimation error scales $1/\sqrt{T}$ which in turn gives a $\sqrt{T}$-type regret, but cannot give a $\log T$-type regret bound.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

For model-based algorithms, [max2019nonasymptotic] introduced a novel notion, optimistic surplus (cf. Equation[eqn:opt\_surplus]), which can be bounded by the estimation error of the transition probability. The logarithmic regret bound can be proved via a clipping trick on top of the optimistic surplus. [max2019nonasymptotic], their analysis is highly tailored to model-based algorithms. First, model-free algorithms do not estimate the probability transition, so we cannot bound the optimistic surplus via this approach. Secondly, although we can also obtain a formula for the optimistic surplus in each episode using the update rules of the $Q$-learning algorithm, the formula depends on the estimation error of $Q$-function in previous episodes. This dependency makes it difficult to bound the optimistic surplus. See Section[sec:opt\_surplus]for more technical details.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we adopt an entirely different counting approach. We first write the total regret as expected sum over sub-optimality gaps appearing in the whole learning process, then use the estimation error of $Q$-function and the definition of sub-optimality gap to upper bound the number of times the algorithm takes suboptimal actions.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

To obtain a sharp dependency on $\Delta_{\min}$, we divide the interval $[\Delta_{\min},H]$ (the range of all gaps) into multiple subintervals. We then bound the sum of learning error in each subinterval by its maximum value times the number of steps falling into this subinterval. The number of steps in each layer is bounded through computing the weighted sum of learning error across all the episodes $k\in[K]$. See detailed discussion in Lemma[lemma:weighed-sum-learning-error] and Lemma[lemma:count-in-each-layer].

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper is organized as follows. In Section[sec:rel] we discuss related works. In Section[sec:pre], we introduce necessary definitions and backgrounds. In Section[sec:main\_results], we present our main results and discussions. In Section[sec:proof\_sketch], we give the proof of our theorem on the episodic setting. We conclude in Section[sec:conclusion]and leave remaining proofs to the appendix.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Main Theoretical Results", "weight": 1.0} -->

Now we present our main results.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Main Theoretical Results", "weight": 1.0} -->

Main Result for Episodic MDP The following theorem characterizes the performance of Algorithm[algo:ucb-q] for episodic MDP. To our knowledge, this is the first theoretical result showing a model-free algorithm can achieve logarithmic regret of tabular RL.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Main Theoretical Results", "weight": 1.0} -->

The expected regret of Algorithm[algo:ucb-q] for episodic tabular MDP is upper bounded by $\expect{\mathrm{Regret}(K)}\le\cO\left(\frac{H^6SA}{\Delta_{\min}} \log\left({SAT}\right)\right)$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Main Theoretical Results", "weight": 1.0} -->

An interesting advantage of our theorem is adaptivity. Note the algorithm we analyze is exactly the same algorithm studied in [jin2019provably], which has been shown to achieve the worst-case $\sqrt{T}$-type regret bound. Theorem[thm:episodic] suggests that one does not need to modify the algorithm to exploit the strictly positive minimum sub-optimality gap structure, Algorithm[algo:ucb-q] automatically adapts to this benign structure. Importantly, Algorithm[algo:ucb-q] does not need to know $\Delta_{\min}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Main Theoretical Results", "weight": 1.0} -->

Proposition 2.2 in [max2019nonasymptotic] suggested that any algorithm with sub-linear regret in the worst case, suffer an $\Omega\left(\sum_{(x,a), \Delta_1(x,a) > 0}\frac{H^2}{\Delta_1\left(x,a\right)} \log T\right)$ expected regret. Therefore, the dependencies on $S$, $A$ and $T$ are nearly tight in Theorem[thm:episodic].

<!-- chunk {"id": "body-0023", "role": "body", "section": "Main Theoretical Results", "weight": 1.0} -->

One may wonder whether it is possible to obtain a regret bound that only depends the sum of positive gaps, e.g., $O\left(\sum_{(x,a), \Delta_1(x,a) > 0}\frac{H^2}{\Delta_1\left(x,a\right)} \log T\right)$, unlike ours, which is a multiple of $1/\Delta_{\min}$. Unfortunately, [max2019nonasymptotic] showed, all existing algorithms, including Algorithm[algo:ucb-q] and their algorithm, suffer an $\Omega\left(\frac{S}{\Delta_{\min}}\right)$regret, and new algorithmic ideas are needed in order to circumvent this lower bound.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Main Theoretical Results", "weight": 1.0} -->

We compare Theorem[thm:episodic] with the regret bound for model-based algorithm in [max2019nonasymptotic] (in big-$\cO$ form): \Bigg(\!&\!\sum_{\substack{(x,a): \\\exists h \in [H], \Delta_{h}\!(x,a) >0 }}\!\frac{H^3}{\min_h \Delta_h\left(x,a\right)} + \frac{SH^3}{\Delta_{\min}} \\&+ H^4SA\max\left(S,H\right) \log\!\left(\!\frac{SAH}{\Delta_{\min}}\!\right)\Bigg)\log\left(SAHT\right) First recall our bound is for a model-free algorithm which is more space-efficient and time-efficient than the model-based algorithm in In terms of the regret bound, Theorem[thm:episodic]'s dependency on

<!-- chunk {"id": "body-0025", "role": "body", "section": "Main Theoretical Results", "weight": 1.0} -->

$H$ is worse than that in their bound. We remark that simple model-free algorithms may have a worse dependency on $H$ compared to model-based algorithms (e.g., see [jin2018qlearning]).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Main Theoretical Results", "weight": 1.0} -->

Now let us consider an environment where there are $\sim SA$ state-action pairs whose gap is $\Delta_{\min}$. Then the bound in [max2019nonasymptotic] becomes $$\left(\!\frac{H^3SA}{\Delta_{\min}} \!+\! H^4SA \max\!\left\{S,\!H\right\}\!\log\!\left(\!\frac{SAH}{\Delta_{\min}}\!\right)\!\right)\! \log\!\left(\!SAHT\!\right).$$ In this regime, both Theorem[thm:episodic] and their bound have an $\frac{SA}{\Delta_{\min}}$ term. Their bound also has an additional $H^4 SA\max\left(H,S\right) \log\left(\frac{SAH}{\Delta_{\min}}\right)$ burn-in term which our bound does not have.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Main Theoretical Results", "weight": 1.0} -->

When $S$ is large compared to $H$ and $\Delta_{\min}$, this term scales $S^2$ and can dominate other terms, so our bound is better. The technical reason behind this phenomenon is that Algorithm[algo:ucb-q] uses the Hoeffding bound for constructing bonus on $Q$-value, which does not need burn-.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Main Theoretical Results", "weight": 1.0} -->

Main Result for Infinite-horizon Discounted MDP Algorithm[algo:ucb-q] can be easily generalized to the discounted MDP. See Algorithm[algo:infinite ucb-q]in the appendix. We also obtain a logarithmic regret bound for infinite-horizon discounted MDP.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Main Theoretical Results", "weight": 1.0} -->

The expected regret of Algorithm[algo:infinite ucb-q] for infinite-horizon discounted MDP is upper bounded by $\expect{\mathrm{Regret}(T)}\le\cO\left(\frac{SA}{\Delta_{\min}\left(1-\gamma\right)^6} \log\frac{SAT}{\Delta_{\min}\left(1-\gamma\right)}\right)$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Main Theoretical Results", "weight": 1.0} -->

Theorem[thm:discounted] suggests that model-free algorithms can achieve logarithmic regret even in the infinite-horizon discounted MDP setting. The main difference from Theorem[thm:episodic] is that $H$ is replaced by $\frac{1}{1-\gamma}$. By analogy, we believe the dependencies on $S,A,T$ and $\Delta_{\min}$ are nearly tight and the dependency $\frac{1}{1-\gamma}$ can be improved. The proof of Theorem[thm:discounted]is deferred to Appendix.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Conclusion and Future Directions", "weight": 1.5} -->

This paper gives the first logarithmic regret bounds for $Q$-learning in both finite-horizon and discounted tabular MDPs. Below we list some future directions that we believe are worth exploring.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Conclusion and Future Directions", "weight": 1.5} -->

The dependency on $H$ in our regret bound for episodic RL is $H^6$, which we believe is suboptimal. As discussed in [max2019nonasymptotic], improving the $H$ dependence is often a challenging task. Recently, [zhang2020optimal] showed a model-free algorithm can achieve near-optimal regret in the worst case using the idea of reference value function. It would be interesting to apply this idea to improve the $H$ dependence in our logarithmic regret bound.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Conclusion and Future Directions", "weight": 1.5} -->

Lastly, we note that recently researchers found the sub-optimality gap assumption is crucial for dealing with large state-space RL problems where function approximation is needed. [du2019q] presented an algorithm that enjoys polynomial sample complexity if there is a sub-optimality gap and the environment satisfies a low-variance assumption. [du2019good,du2020agnostic] further showed this assumption is necessary in certain settings. There is another line of works putting certain low-rank assumptions on MDPs[krishnamurthy2016pac,jiang2017contextual,dann2018oracle,du2019provably,sun2018model,misra2019kinematic]. It would be interesting to extend our analysis to these settings and obtain logarithmic regret bounds.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Algorithm for Discounted MDP", "weight": 1.0} -->

The pseudocode is listed in Algorithm[algo:infinite ucb-q]. We acknowledge that Algorithm[algo:infinite ucb-q] relies on knowing a lower bound on $\Delta_{\min}$, and we leave it an open problem to develop a parameter-free algorithm.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Proofs for Discounted MDP", "weight": 1.0} -->

Let $Q^t(s,a),\widehat{Q}^t(s,a),V^t(s), \widehat{V}^t(s),N^t(s,a)$ denote the value of $Q(s,a),\widehat{Q}(s,a),V(s), \widehat{V}(s),N(s,a)$ right before the $t$-th step, respectively. Let $\tau(s,a,i):=\max\left\{t:N^t(s,a)=i-1\right\}$ be the step $t$ at which $\xahk{}{t}=(x,a)$ for the $i$-th time. We will abbreviate $\Nxahk{}{t}$ for $n^t$ when no confusion can arise. $\alpha_{t}^i$ is defined same as that in the finite-horizon episodic setting.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Proofs for Discounted MDP", "weight": 1.0} -->

Proof of Theoremthm:discounted We shall decompose the regret of each step as the expected sum of discounted gaps using the exact same argument as Eq([eq:episodic-regret-decomp]), where the expect runs over all the possible infinite-length trajectories For the convenience of analysis, when proving the upper bound we remove the constraint $t\in[T]$ in the for-loop of linealgo:for-loop. Instead, we allow the algorithm to take as many steps as we need, even yielding infinite-length trajectories.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Proofs for Discounted MDP", "weight": 1.0} -->

\gamma^{h'-t}\Delta\!\xah{h'}}$$ Our next lemma is borrowed from [dong2019qlearning], which shows that Algorithm[algo:infinite ucb-q] satisfies optimism and bounded learning error with high probability.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Proofs for Discounted MDP", "weight": 1.0} -->

By abuse of notation, we still use $\cE_{\mathrm{conc}}$ to denote the successful concentration event in this setting. Recall that Algorithm[algo:infinite ucb-q] specifies $\iota(t)=\log\left(SAT(t+1)(t+2)\right)$ and $\beta_t=\frac{c_3}{1-\gamma}\sqrt{\frac{H\iota(t)}{ t}}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Proofs for Discounted MDP", "weight": 1.0} -->

For the first term of we claim that $\left\{\widetilde{w}_t\right\}_{\!t\ge2}$ is a $\left(\!C,(1+1\!/\!H)w\!\right)$-sequence. This can be verified by a similar argument to Ineq([ineq:w\_h+1]). We also have \left(\hV^{t}-V^*\right)\!(x_t)&=\hV^t(x_t)-V^*(x_t)=\hQ^t(x_t,a_t)-V^*(x_t)\le\hQ^t(x_t,a_t)-Q^*(x_t,a_t)=\left(\hQ^t-Q^*\right)(x_t,a_t).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Proofs for Discounted MDP", "weight": 1.0} -->

+\frac{2c_3\!}{1-\gamma}\sqrt{SAHCw{\iota(C)}} +\frac{\gamma (1+1\!/\!H)wS}{1-\gamma} +\gamma\sum_{t\ge2}\widetilde{w}_t\left(\hQ^{t}-Q^*\right)\!\xah{t}& Note that the last term in Ineq ([ineq:inf-recursion]) is another weighted sum of learning errors starting from step 2, where the weights form a $\left(\!C,(1+1\!/\!H)w\!\right)$-sequence.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Proofs for Discounted MDP", "weight": 1.0} -->

We can therefore repeat this unrolling argument for $H$ times. Our choice of $H$ in Algorithm[algo:infinite ucb-q] guarantees not only the bounded blow-up factor of weights, but also sufficiently small contribution of learning error after step $H$. In particular, we define a family of weights: when $h=0$, $\left\{w_t^{(h)}\right\}_{t\ge h+1}=\{w_t\}_{t\ge1}$ is a $(C,w)$ sequence; $\forall h\in[H]$ $\left\{w_t^{(h)}\right\}_{t\ge h+1}$ is a $\left(\!C,(1+1\!/\!H)^hw\!\le\! ew\!\right)$ sequence. Note that our previous definition of $\widetilde{w}$ is exactly $w_t^{}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Proofs for Discounted MDP", "weight": 1.0} -->

Note that we have clarified in Ineq ([ineq:gap-bounded-by-learning-error]) that on $\cE_{\mathrm{conc}}$ where optimism holds, sub-optimality gaps can be bounded by clipped learning error of $Q$-function. Again we divide its range $\left[\Delta_{\min},\frac{1}{1-\gamma}\right]$ into disjoint subintervals and bound the sum inside each subinterval independently.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Difficulty in Applying Optimistic Surplus", "weight": 1.0} -->

The closest related work is by [max2019nonasymptotic] who proved the logarithmic regret bound for a model-based algorithm. introduced a novel property characterizing optimistic algorithms, which is called optimistic surplus and defined as E_{k,h}(x,a):=Q_h^k(x,a)-\left[r_h(x,a)+P_h(x,a)^{\!\mathsf{T}}V_{h+1}^k\right].

<!-- chunk {"id": "body-0044", "role": "body", "section": "Difficulty in Applying Optimistic Surplus", "weight": 1.0} -->

The analysis of model-based algorithms is to first bound the regret $\left(\!V^*-V^{\pi_k}\!\right)$ by a sum over surpluses that are clipped to zero whenever being smaller than some $\Delta$-related quantities, then combine the concentration argument and properties of specially-designed bonus terms $b_h^k$ to provide high probability bound for surpluses. However, for model-free algorithms, estimates of transition probabilities are no longer maintained, so $\widehat{P}_h$ is a one-hot vector reflecting only the current step's empirical sample drawn from the real next-state distribution. In this scenario, concentration argument of $\left(\widehat{P}-P\right)$ cannot give us $\log T$regret.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Difficulty in Applying Optimistic Surplus", "weight": 1.0} -->

This indicates that the surplus of an episode is closely correlated with estimates of value functions during previous episodes. The correlation makes the analysis more difficult. Therefore, we use a very different approach to analyze $Q$-learning in this paper.
