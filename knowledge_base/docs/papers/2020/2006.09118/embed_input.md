<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Q-learning with Logarithmic Regret

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents the first non-asymptotic result showing that a model-free algorithm can achieve a logarithmic cumulative regret for episodic tabular reinforcement learning if there exists a strictly positive sub-optimality gap in the optimal Q-function. We prove that the optimistic Q-learning studied in [Jin et al. 2018] enjoys a O(fracSA* poly(H){Delta_min}log(SAT)) cumulative regret bound, where S is the number of states, A is the number of actions, H is the planning horizon, T is the total number of steps, and Delta_min is the minimum sub-optimality gap. This bound matches the information theoretical lower bound in terms of S,A,T up to a log(SA) factor. We further extend our analysis to the discounted setting and obtain a similar logarithmic cumulative regret bound.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

$Q$-learning is one of the most popular classes of methods for solving reinforcement learning (RL) problems. $Q$-learning tries to estimate the optimal state-action value function ($Q$-function). With a $Q$-function, at every state, one can just greedily choose the action with the largest $Q$ value to interact with the RL environment. Compared to another popular class of methods, model-based learning, $Q$-learning algorithms (or more generally, model-free algorithms) often enjoy better memory and time efficiency^11^1See Section 2 for the precise definitions of model-free and model-based algorithms in the tabular setting.. These are the main reasons why $Q$-learning is applied in solving a wide range of RL problems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

While model-free methods are widely applied in practice, most theoretical works study model-based RL. In one of the most fundamental RL frameworks, tabular RL, which is the focus of this paper, the majority of works study model-based algorithms with a few exceptions. From a regret minimization point of view, the state-of-the-art analysis demonstrates that one can achieve a $\sqrt{T}$-type regret bound where $T$ is the number of episodes. Although these bounds are sharp in the worst-case scenario, they do not reveal the favorable structures of the environment, which can significantly decrease the regret.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

One such structure is the existence of a strictly positive sub-optimality gap, i.e., for every state, there is a strictly positive value gap between the optimal action(s) and the rest (cf. Definition 2.1. ‣ Sub-optimality Gap ‣ 2 Preliminaries")). In practice, arguably, nearly all environments with finite action sets satisfy some sub-optimality gap conditions. In Atari-games, e.g., Freeway, the optimal action has a value that is usually very distinctive from the rest of actions. In many other environments with finite number of actions, e.g. those control environments in OpenAI gym, the gap condition usually holds. Similar gap conditions can be observed in other environments (see e.g. Kakade ).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Theoretically, the sub-optimality gap is extensively investigated in the bandit problems, which can be viewed as RL problems with the planning horizon being $1$. With this structure, one can drastically decrease the $\sqrt{T}$-type regret to $\log T$-type regret. For RL, most existing works that can leverage this structure require additional assumptions about the environment, such as finite hitting time and ergodicity or access to a generator.^22^2The simulator allows the user to query any state-action pair. Recently, Simchowitz and Jamieson presented a systematic study of episodic tabular RL with the gap structure. They presented a novel algorithm which achieves the near-optimal $\sqrt{T}$-type regret in the worst scenario and $\log T$-type regret if there exists a strictly positive sub-optimality gap. Furthermore, they also provided instance-dependent lower bounds for a class of reasonable algorithms. See Section 1.1 for more detailed discussions.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, to our knowledge, all existing works that obtain $\log T$-type regret bounds are about model-based algorithms. It remains open whether model-free algorithms such as $Q$-learning can achieve $\log T$-type regret bounds. Indeed, this is a challenging task. As discussed in Simchowitz and Jamieson, their analysis framework cannot be applied to model-free algorithms directly. Later in this section, we also provide some technical explanations on why their approach is difficult to adopt.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

We answer the aforementioned open problem by proving that the optimistic $Q$-learning algorithm studied in Jin et al. enjoys $\mathcal{O}\left( {\frac{SAH^{6}}{\Delta_{\min}}{\log\left( {SAT} \right)}} \right)$ cumulative regret where $S$ is the number states, $A$ is the number of actions, $H$ is the planning horizon and $\Delta_{\min}$ is the minimum sub-optimality gap. To our knowledge, this is the first result showing model-free algorithms can achieve $\log T$-type regret. Furthermore, our bound matches the lower bound by Simchowitz and Jamieson in terms of $S$, $A$ and $T$ up to a $\log\left( {SA} \right)$ factor. Importantly, the algorithm does not need to know $\Delta_{\min}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Second, we extend our analysis to the infinite-horizon discounted setting with the regret defined in Liu and Su, for which we show the optimistic $Q$-learning achieves $\mathcal{O}\left( {\frac{SA}{\Delta_{\min}\left( {1 - \gamma} \right)^{6}}{\log\left( \frac{SAT}{\Delta_{\min}\left( {1 - \gamma} \right)} \right)}} \right)$ regret where $0 < \gamma < 1$ is the discount factor.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Main Challenges", "weight": 1.0} -->

Here we explain the main challenges of using existing analyses and give an overview of our main techniques at a high level. The existing proof in Jin et al. bounds the regret in terms of a weighted sum of the estimation error of $Q$-function. Note the estimation error scales $1/\sqrt{T}$ which in turn gives a $\sqrt{T}$-type regret, but cannot give a $\log T$-type regret bound.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Main Challenges", "weight": 1.0} -->

For model-based algorithms, Simchowitz and Jamieson introduced a novel notion, *optimistic surplus* (cf. Equation ), which can be bounded by the estimation error of the transition probability. The logarithmic regret bound can be proved via a clipping trick on top of the optimistic surplus.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Main Challenges", "weight": 1.0} -->

Unfortunately, as acknowledged by Simchowitz and Jamieson, their analysis is highly tailored to model-based algorithms. First, model-free algorithms do not estimate the probability transition, so we cannot bound the optimistic surplus via this approach. Secondly, although we can also obtain a formula for the optimistic surplus in each episode using the update rules of the $Q$-learning algorithm, the formula depends on the estimation error of $Q$-function in previous episodes. This dependency makes it difficult to bound the optimistic surplus. See Section 8 for more technical details.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Technique Overview", "weight": 1.0} -->

In this paper, we adopt an entirely different *counting* approach. We first write the total regret as expected sum over sub-optimality gaps appearing in the whole learning process, then use the estimation error of $Q$-function and the definition of sub-optimality gap to upper bound the number of times the algorithm takes suboptimal actions.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Technique Overview", "weight": 1.0} -->

To obtain a sharp dependency on $\Delta_{\min}$, we divide the interval $\lbrack\Delta_{\min},H\rbrack$ (the range of all gaps) into multiple subintervals. We then bound the sum of learning error in each subinterval by its maximum value times the number of steps falling into this subinterval. The number of steps in each layer is bounded through computing the weighted sum of learning error across all the episodes $k \in {\lbrack K\rbrack}$. See detailed discussion in Lemma 4.3. ‣ Proof of Lemma 4.2 ‣ 4 Proof of Theorem 3.1") and Lemma 4.2. ‣ Proof of Theorem 3.1 ‣ 4 Proof of Theorem 3.1").

<!-- chunk {"id": "body-0015", "role": "body", "section": "Organization", "weight": 1.0} -->

This paper is organized as follows. In Section 1.1 we discuss related works. In Section 2, we introduce necessary definitions and backgrounds. In Section 3, we present our main results and discussions. In Section 4, we give the proof of our theorem on the episodic setting. We conclude in Section 5 and leave remaining proofs to the appendix.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Gap-independent Finite-horizon and Infinite-horizon Discounted RL", "weight": 1.0} -->

^33^3There is another line of works on gap-independent infinite-horizon average-reward setting. This setting is beyond the scope of this paper.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Gap-independent Finite-horizon and Infinite-horizon Discounted RL", "weight": 1.0} -->

There is a long list of results about regret or sample complexity of tabular RL, dating back to Singh and Yee. One line of works require access to a simulator where the agent can query samples freely from any state-action pair of the environment and therefore the agent does not need to design a strategy to explore the environment..

<!-- chunk {"id": "body-0018", "role": "body", "section": "Gap-independent Finite-horizon and Infinite-horizon Discounted RL", "weight": 1.0} -->

Another line of works drop the simulator assumption and thus the agent needs to use advanced techniques, such as upper confidence bound (UCB) to explore the state space. In terms of the regret, the state-of-art result shows one can achieve $\overset{\sim}{\mathcal{O}}\left( {\sqrt{SAH^{2}T} + {{poly}(S,A,H)}} \right)$ regret for which the first term nearly match the $\Omega\left( \sqrt{SAH^{2}T} \right)$up to logarithmic factors.^44^4 In this paper, we study the same setting as in Jin et al. where the reward at each level is in $\lbrack 0,1\rbrack$, and the transition probabilities at each level can be different. In another setting, the total reward is bounded by $1$ and the transition probabilities at each level are the same. The latter setting is more challenging to analyze and the worst-case sample complexity is still open.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Gap-independent Finite-horizon and Infinite-horizon Discounted RL", "weight": 1.0} -->

Among these results, only a few are for model-free algorithms and only very recently, Jin et al.; Zhang et al. showed $Q$-learning can achieve $\sqrt{T}$-type regret bounds.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Sub-optimality Gap", "weight": 1.0} -->

The results about gap-dependent regret bounds for MDP algorithms can be categorized into asymptotic bounds and non-asymptotic bounds. Asymptotic bounds are only valid when the total number of steps $T$ is large enough. These bounds often suffer from the worst-case dependency on some problem-specific quantities, such as diameter and worst-case hitting time. Under the infinite-horizon average-reward setting, Auer and Ortner provided a logarithmic regret algorithm for irreducible MDPs. Besides dependency on hitting times, their regret also depends inversely on $\Delta_{\ast}^{2}$, the squared distance between optimal and second-optimal policy. Along this direction and improving over previous algorithm of Burnetas and Katehakis, Tewari and Bartlett proposed an algorithm called Optimistic Linear Programming (OLP). OLP is proved to have $C{(P)}{\log T}$ regret asymptotically in $T$, where $C{(P)}$ depends on some diameter-related quantity as well as the sum over reciprocals of gaps for $(x,a)$ inside a critical set.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Sub-optimality Gap", "weight": 1.0} -->

For non-asymptotic bounds, Jaksch et al. introduced UCRL2 algorithm, which enjoys $\overset{\sim}{\mathcal{O}}\left( {\frac{D^{2}S^{2}A}{\Delta_{\ast}}{\log T}} \right)$ regret where $D$ is the diameter. More recently, Ok et al. derived problem-specific lower bounds for both structured and unstructured MDPs. Their lower bound scales $SA{\log T}$ for unstructured MDP and $c{\log T}$ for structured MDP, where this $c$ depends on both the minimal action sub-optimality gap and the span of bias function, which can be bounded by diameter $D$. For non-asymptotic bounds, Simchowitz and Jamieson proved that model-based optimistic algorithm StrongEuler has gap-dependent regret bound that holds uniformly over $T$. Moreover, their bounds depend only on $H$ and not on any term such as hitting time or diameter.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Sub-optimality Gap", "weight": 1.0} -->

In Section 3, we compare our result with the one in Simchowitz and Jamieson in more detail.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Episodic MDP", "weight": 1.0} -->

An episodic Markov decision process (MDP) is a tuple $\mathcal{M}:=(\mathcal{S},\mathcal{A},H,P,r)$, where $\mathcal{S}$ is the finite state space with $|\mathcal{S}| = S$, $\mathcal{A}$ is the finite action space with $|\mathcal{A}| = A$, $H \in {\mathbb{Z}}_{+}$ is the planning horizon, $P_{h}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\Delta{(\mathcal{S})}}}$ is the transition operator at step $h$ that takes a state-action pair and returns a distribution over states, and $r_{h}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\lbrack 0,1\rbrack}}$ is the deterministic reward function at step $h$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Episodic MDP", "weight": 1.0} -->

Each episode starts at an initial state $x_{1} \in \mathcal{S}$ picked by an adversary.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Episodic MDP", "weight": 1.0} -->

In this paper, we focus on deterministic policies. A deterministic policy $\pi$ is a sequence of mappings $\pi_{h}:{\mathcal{S}\rightarrow\mathcal{A}}$ for $h = {1,\ldots,H}$. Given a policy $\pi$, for a state $x \in \mathcal{S}$, the value function of state $x \in \mathcal{S}$ at the $h$-step is defined as

<!-- chunk {"id": "body-0026", "role": "body", "section": "Episodic MDP", "weight": 1.0} -->

and the associated $Q$-function of a state-action pair ${(x,a)} \in {\mathcal{S} \times \mathcal{A}}$ at the $h$-step is

<!-- chunk {"id": "body-0027", "role": "body", "section": "Episodic MDP", "weight": 1.0} -->

In this paper we focus on bounding the expected regret ${\mathbb{E}}\left\lbrack {{Regret}{(K)}} \right\rbrack$ where the expectation is over the randomness from the environment.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Model-free Algorithm V.S. Model-based Algorithm", "weight": 1.0} -->

In this paper we focus on *model-free* $Q$-learning algorithms. Formally, by model-free algorithms, we mean the space complexity of the algorithm scales at most *linearly* in $S$ in contrast to the model-based algorithms whose space complexity often scales *quadratically* with $S$. For episodic MDP, we will analyze the $Q$-learning with UCB-Hoeffding algorithm studied in Jin et al. (cf. Algorithm 1). At a high level, this algorithm maintains an upper bound of $Q^{\ast}$ for every $(s,a)$ pair and choose the action greedily at every episode. The algorithm uses a carefully designed step size sequence $\{\alpha_{k}\}$ to update the upper bound based on the observed data. Jin et al. proved that Algorithm 1 enjoys $\left( \sqrt{H^{4}SAT{\log\left( {SAT} \right)}} \right)$ regret, which is the first $\sqrt{T}$-type bound for model-free algorithms.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Model-free Algorithm V.S. Model-based Algorithm", "weight": 1.0} -->

1:Initialize: Qh (x,a) ← H and Nh (x,a) ← 0 for all (x,a,h) ∈ 𝒮 × 𝒜 × [H].
2:Define $\alpha_{t} = \frac{H + 1}{H + t}$, ι ← log (S A T2).
6: Take action ah ← argmaxa′ ∈ 𝒜 Qh (xh,a′), observe xh + 1.
8: $b_{t}\leftarrow{c\sqrt{{H^{3}\iota}/t}}$, ⊳ c is a constant that can be set to 4.
Algorithm 1 Q-learning with UCB-Hoeffding

<!-- chunk {"id": "body-0030", "role": "body", "section": "Sub-optimality Gap", "weight": 1.0} -->

Our paper investigates what structures of the MDP enable us to improve the $\sqrt{T}$-type bound. In this paper we focus on the positive sub-optimality gap condition.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Infinite-horizon Discounted MDP", "weight": 1.0} -->

In this paper we also study infinite-horizon discounted MDP, which is a tuple $\mathcal{M}:=(\mathcal{S},\mathcal{A},\gamma,P,r)$, where every step shares the same transition operator $P$ and reward function $r$. Here $\gamma$ denotes the discount factor, and there is no restart during the entire process. Let $\mathcal{C} = {\left\{ {\mathcal{S} \times \mathcal{A} \times {\lbrack 0,1\rbrack}} \right\}^{\ast} \times \mathcal{S}}$ be the set of all possible trajectories of any length. A non-stationary deterministic policy $\pi:{\mathcal{C}\rightarrow\mathcal{A}}$ is a mapping from paths to actions.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Infinite-horizon Discounted MDP", "weight": 1.0} -->

Let $V^{\ast}{(s)}$ and $Q^{\ast}{(s,a)}$ denote respectively the value function and $Q$ function of the optimal policy $\pi^{\ast}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Main Theoretical Results", "weight": 1.0} -->

Now we present our main results.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Main Result for Episodic MDP", "weight": 1.0} -->

The following theorem characterizes the performance of Algorithm 1 for episodic MDP. To our knowledge, this is the first theoretical result showing a model-free algorithm can achieve logarithmic regret of tabular RL.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Main Result for Infinite-horizon Discounted MDP", "weight": 1.0} -->

Algorithm 1 can be easily generalized to the discounted MDP. See Algorithm 2 in the appendix. We also obtain a logarithmic regret bound for infinite-horizon discounted MDP.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusion and Future Directions", "weight": 1.5} -->

This paper gives the first logarithmic regret bounds for $Q$-learning in both finite-horizon and discounted tabular MDPs. Below we list some future directions that we believe are worth exploring.

<!-- chunk {"id": "body-0037", "role": "body", "section": "$H$ dependence", "weight": 1.0} -->

The dependency on $H$ in our regret bound for episodic RL is $H^{6}$, which we believe is suboptimal. As discussed in Simchowitz and Jamieson, improving the $H$ dependence is often a challenging task. Recently, Zhang et al. showed a model-free algorithm can achieve near-optimal regret in the worst case using the idea of reference value function. It would be interesting to apply this idea to improve the $H$ dependence in our logarithmic regret bound.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Function Approximation", "weight": 1.0} -->

Lastly, we note that recently researchers found the sub-optimality gap assumption is crucial for dealing with large state-space RL problems where function approximation is needed. Du et al. presented an algorithm that enjoys polynomial sample complexity if there is a sub-optimality gap and the environment satisfies a low-variance assumption. Du et al. further showed this assumption is necessary in certain settings. There is another line of works putting certain low-rank assumptions on MDPs. It would be interesting to extend our analysis to these settings and obtain logarithmic regret bounds.
