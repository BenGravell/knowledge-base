## Introduction

$Q$-learning is one of the most popular classes of methods for solving reinforcement learning (RL) problems. $Q$-learning tries to estimate the optimal state-action value function ($Q$-function). With a $Q$-function, at every state, one can just greedily choose the action with the largest $Q$ value to interact with the RL environment. Compared to another popular class of methods, model-based learning, $Q$-learning algorithms (or more generally, model-free algorithms) often enjoy better memory and time efficiency^11^1See Section 2 for the precise definitions of model-free and model-based algorithms in the tabular setting.. These are the main reasons why $Q$-learning is applied in solving a wide range of RL problems.

While model-free methods are widely applied in practice, most theoretical works study model-based RL. In one of the most fundamental RL frameworks, tabular RL, which is the focus of this paper, the majority of works study model-based algorithms with a few exceptions. From a regret minimization point of view, the state-of-the-art analysis demonstrates that one can achieve a $\sqrt{T}$-type regret bound where $T$ is the number of episodes. Although these bounds are sharp in the worst-case scenario, they do not reveal the favorable structures of the environment, which can significantly decrease the regret.

One such structure is the existence of a strictly positive sub-optimality gap, i.e., for every state, there is a strictly positive value gap between the optimal action(s) and the rest (cf. Definition 2.1. ‣ Sub-optimality Gap ‣ 2 Preliminaries")). In practice, arguably, nearly all environments with finite action sets satisfy some sub-optimality gap conditions. In Atari-games, e.g., Freeway, the optimal action has a value that is usually very distinctive from the rest of actions. In many other environments with finite number of actions, e.g. those control environments in OpenAI gym, the gap condition usually holds. Similar gap conditions can be observed in other environments (see e.g. Kakade ).

Theoretically, the sub-optimality gap is extensively investigated in the bandit problems, which can be viewed as RL problems with the planning horizon being $1$. With this structure, one can drastically decrease the $\sqrt{T}$-type regret to $\log T$-type regret. For RL, most existing works that can leverage this structure require additional assumptions about the environment, such as finite hitting time and ergodicity or access to a generator.^22^2The simulator allows the user to query any state-action pair. Recently, Simchowitz and Jamieson presented a systematic study of episodic tabular RL with the gap structure. They presented a novel algorithm which achieves the near-optimal $\sqrt{T}$-type regret in the worst scenario and $\log T$-type regret if there exists a strictly positive sub-optimality gap. Furthermore, they also provided instance-dependent lower bounds for a class of reasonable algorithms. See Section 1.1 for more detailed discussions.

However, to our knowledge, all existing works that obtain $\log T$-type regret bounds are about model-based algorithms. It remains open whether model-free algorithms such as $Q$-learning can achieve $\log T$-type regret bounds. Indeed, this is a challenging task. As discussed in Simchowitz and Jamieson, their analysis framework cannot be applied to model-free algorithms directly. Later in this section, we also provide some technical explanations on why their approach is difficult to adopt.

### Our Contributions

We answer the aforementioned open problem by proving that the optimistic $Q$-learning algorithm studied in Jin et al. enjoys $\mathcal{O}\left( {\frac{SAH^{6}}{\Delta_{\min}}{\log\left( {SAT} \right)}} \right)$ cumulative regret where $S$ is the number states, $A$ is the number of actions, $H$ is the planning horizon and $\Delta_{\min}$ is the minimum sub-optimality gap. To our knowledge, this is the first result showing model-free algorithms can achieve $\log T$-type regret. Furthermore, our bound matches the lower bound by Simchowitz and Jamieson in terms of $S$, $A$ and $T$ up to a $\log\left( {SA} \right)$ factor. Importantly, the algorithm does not need to know $\Delta_{\min}$.

Second, we extend our analysis to the infinite-horizon discounted setting with the regret defined in Liu and Su, for which we show the optimistic $Q$-learning achieves $\mathcal{O}\left( {\frac{SA}{\Delta_{\min}\left( {1 - \gamma} \right)^{6}}{\log\left( \frac{SAT}{\Delta_{\min}\left( {1 - \gamma} \right)} \right)}} \right)$ regret where $0 < \gamma < 1$ is the discount factor.

### Main Challenges

Here we explain the main challenges of using existing analyses and give an overview of our main techniques at a high level. The existing proof in Jin et al. bounds the regret in terms of a weighted sum of the estimation error of $Q$-function. Note the estimation error scales $1/\sqrt{T}$ which in turn gives a $\sqrt{T}$-type regret, but cannot give a $\log T$-type regret bound.

For model-based algorithms, Simchowitz and Jamieson introduced a novel notion, *optimistic surplus* (cf. Equation ), which can be bounded by the estimation error of the transition probability. The logarithmic regret bound can be proved via a clipping trick on top of the optimistic surplus.

Unfortunately, as acknowledged by Simchowitz and Jamieson, their analysis is highly tailored to model-based algorithms. First, model-free algorithms do not estimate the probability transition, so we cannot bound the optimistic surplus via this approach. Secondly, although we can also obtain a formula for the optimistic surplus in each episode using the update rules of the $Q$-learning algorithm, the formula depends on the estimation error of $Q$-function in previous episodes. This dependency makes it difficult to bound the optimistic surplus. See Section 8 for more technical details.

### Technique Overview

In this paper, we adopt an entirely different *counting* approach. We first write the total regret as expected sum over sub-optimality gaps appearing in the whole learning process, then use the estimation error of $Q$-function and the definition of sub-optimality gap to upper bound the number of times the algorithm takes suboptimal actions.

To obtain a sharp dependency on $\Delta_{\min}$, we divide the interval $\lbrack\Delta_{\min},H\rbrack$ (the range of all gaps) into multiple subintervals. We then bound the sum of learning error in each subinterval by its maximum value times the number of steps falling into this subinterval. The number of steps in each layer is bounded through computing the weighted sum of learning error across all the episodes $k \in {\lbrack K\rbrack}$. See detailed discussion in Lemma 4.3. ‣ Proof of Lemma 4.2 ‣ 4 Proof of Theorem 3.1") and Lemma 4.2. ‣ Proof of Theorem 3.1 ‣ 4 Proof of Theorem 3.1").

### Organization

This paper is organized as follows. In Section 1.1 we discuss related works. In Section 2, we introduce necessary definitions and backgrounds. In Section 3, we present our main results and discussions. In Section 4, we give the proof of our theorem on the episodic setting. We conclude in Section 5 and leave remaining proofs to the appendix.

### Related Work

### Gap-independent Finite-horizon and Infinite-horizon Discounted RL

^33^3There is another line of works on gap-independent infinite-horizon average-reward setting. This setting is beyond the scope of this paper.

There is a long list of results about regret or sample complexity of tabular RL, dating back to Singh and Yee. One line of works require access to a simulator where the agent can query samples freely from any state-action pair of the environment and therefore the agent does not need to design a strategy to explore the environment..

Another line of works drop the simulator assumption and thus the agent needs to use advanced techniques, such as upper confidence bound (UCB) to explore the state space. In terms of the regret, the state-of-art result shows one can achieve $\overset{\sim}{\mathcal{O}}\left( {\sqrt{SAH^{2}T} + {{poly}(S,A,H)}} \right)$ regret for which the first term nearly match the $\Omega\left( \sqrt{SAH^{2}T} \right)$up to logarithmic factors.^44^4 In this paper, we study the same setting as in Jin et al. where the reward at each level is in $\lbrack 0,1\rbrack$, and the transition probabilities at each level can be different. In another setting, the total reward is bounded by $1$ and the transition probabilities at each level are the same. The latter setting is more challenging to analyze and the worst-case sample complexity is still open. Among these results, only a few are for model-free algorithms and only very recently, Jin et al.; Zhang et al. showed $Q$-learning can achieve $\sqrt{T}$-type regret bounds.

### Sub-optimality Gap

The results about gap-dependent regret bounds for MDP algorithms can be categorized into asymptotic bounds and non-asymptotic bounds. Asymptotic bounds are only valid when the total number of steps $T$ is large enough. These bounds often suffer from the worst-case dependency on some problem-specific quantities, such as diameter and worst-case hitting time. Under the infinite-horizon average-reward setting, Auer and Ortner provided a logarithmic regret algorithm for irreducible MDPs. Besides dependency on hitting times, their regret also depends inversely on $\Delta_{\ast}^{2}$, the squared distance between optimal and second-optimal policy. Along this direction and improving over previous algorithm of Burnetas and Katehakis, Tewari and Bartlett proposed an algorithm called Optimistic Linear Programming (OLP). OLP is proved to have $C{(P)}{\log T}$ regret asymptotically in $T$, where $C{(P)}$ depends on some diameter-related quantity as well as the sum over reciprocals of gaps for $(x,a)$ inside a critical set.

For non-asymptotic bounds, Jaksch et al. introduced UCRL2 algorithm, which enjoys $\overset{\sim}{\mathcal{O}}\left( {\frac{D^{2}S^{2}A}{\Delta_{\ast}}{\log T}} \right)$ regret where $D$ is the diameter. More recently, Ok et al. derived problem-specific lower bounds for both structured and unstructured MDPs. Their lower bound scales $SA{\log T}$ for unstructured MDP and $c{\log T}$ for structured MDP, where this $c$ depends on both the minimal action sub-optimality gap and the span of bias function, which can be bounded by diameter $D$. For non-asymptotic bounds, Simchowitz and Jamieson proved that model-based optimistic algorithm StrongEuler has gap-dependent regret bound that holds uniformly over $T$. Moreover, their bounds depend only on $H$ and not on any term such as hitting time or diameter. In Section 3, we compare our result with the one in Simchowitz and Jamieson in more detail.

## Preliminaries

### Episodic MDP

An episodic Markov decision process (MDP) is a tuple $\mathcal{M}:=(\mathcal{S},\mathcal{A},H,P,r)$, where $\mathcal{S}$ is the finite state space with $|\mathcal{S}| = S$, $\mathcal{A}$ is the finite action space with $|\mathcal{A}| = A$, $H \in {\mathbb{Z}}_{+}$ is the planning horizon, $P_{h}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\Delta{(\mathcal{S})}}}$ is the transition operator at step $h$ that takes a state-action pair and returns a distribution over states, and $r_{h}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\lbrack 0,1\rbrack}}$ is the deterministic reward function at step $h$. Each episode starts at an initial state $x_{1} \in \mathcal{S}$ picked by an adversary.

In this paper, we focus on deterministic policies. A deterministic policy $\pi$ is a sequence of mappings $\pi_{h}:{\mathcal{S}\rightarrow\mathcal{A}}$ for $h = {1,\ldots,H}$. Given a policy $\pi$, for a state $x \in \mathcal{S}$, the value function of state $x \in \mathcal{S}$ at the $h$-step is defined as

and the associated $Q$-function of a state-action pair ${(x,a)} \in {\mathcal{S} \times \mathcal{A}}$ at the $h$-step is

We let $\pi^{\ast}$ be the optimal policy such that ${V^{\pi^{\ast}}{(x)}} = {V^{\ast}{(x)}} = {{argmax}_{\pi}V^{\pi}{(x)}}$ and ${Q^{\pi^{\ast}}{(x,a)}} = {Q^{\ast}{(x,a)}} = {{argmax}_{\pi}Q^{\pi}{(x,a)}}$ for every $(x,a)$. For episodic MDP, the agent interacts with the MDP for $K \in {\mathbb{Z}}^{+}$ episodes. For each episode $k = {1,\ldots,K}$, the learning algorithm $\mathsf{A}\mathsf{l}\mathsf{g}$ specifies a policy $\pi^{k}$, plays $\pi^{k}$ for $H$ steps and observes trajectory ${(x_{1},a_{1})},\cdots,{(x_{H},a_{H})}$. The total number of steps is $T = {KH}$, and the total regret of an execution instance of $\mathsf{A}\mathsf{l}\mathsf{g}$ is then

In this paper we focus on bounding the expected regret ${\mathbb{E}}\left\lbrack {{Regret}{(K)}} \right\rbrack$ where the expectation is over the randomness from the environment.

### Model-free Algorithm V.S. Model-based Algorithm

In this paper we focus on *model-free* $Q$-learning algorithms. Formally, by model-free algorithms, we mean the space complexity of the algorithm scales at most *linearly* in $S$ in contrast to the model-based algorithms whose space complexity often scales *quadratically* with $S$. For episodic MDP, we will analyze the $Q$-learning with UCB-Hoeffding algorithm studied in Jin et al. (cf. Algorithm 1). At a high level, this algorithm maintains an upper bound of $Q^{\ast}$ for every $(s,a)$ pair and choose the action greedily at every episode. The algorithm uses a carefully designed step size sequence $\{\alpha_{k}\}$ to update the upper bound based on the observed data. Jin et al. proved that Algorithm 1 enjoys $\left( \sqrt{H^{4}SAT{\log\left( {SAT} \right)}} \right)$ regret, which is the first $\sqrt{T}$-type bound for model-free algorithms.

1:Initialize: Qh (x,a) ← H and Nh (x,a) ← 0 for all (x,a,h) ∈ 𝒮 × 𝒜 × [H].
2:Define $\alpha_{t} = \frac{H + 1}{H + t}$, ι ← log (S A T2).
6: Take action ah ← argmaxa′ ∈ 𝒜 Qh (xh,a′), observe xh + 1.
8: $b_{t}\leftarrow{c\sqrt{{H^{3}\iota}/t}}$, ⊳ c is a constant that can be set to 4.
Algorithm 1 Q-learning with UCB-Hoeffding

### Sub-optimality Gap

Our paper investigates what structures of the MDP enable us to improve the $\sqrt{T}$-type bound. In this paper we focus on the positive sub-optimality gap condition.

### Definition 2.1 (Sub-optimality Gap)

Given $h \in {\lbrack H\rbrack}$, ${(x,a)} \in {\mathcal{S} \times \mathcal{A}}$, the suboptimality gap of $(x,a)$ at level $h$ is defined as ${{\Delta_{h}{(x,a)}}:={{V_{h}^{\ast}{(x)}} - {Q_{h}^{\ast}{(x,a)}}}}.$

### Definition 2.2

Minimum Sub-optimality Gap\] Denote by $\Delta_{\min}$ the minimum non-zero gap: $\Delta_{\min}:={\min_{h,x,a}\left\{ {{\Delta_{h}{(x,a)}}:{{\Delta_{h}{(x,a)}} \neq 0}} \right\}}$.

Note that if $\left\{ {\Delta_{h}{(x,a)}}:{{\Delta_{h}{(x,a)}} \neq 0} \right\} = \varnothing$, then all the states are the same, and the MDP degenerates. Otherwise we always have $\Delta_{\min} > 0$. For the rest of the paper, we focus on the case when $\Delta_{\min} > 0$. In Section 1 we have discussed why many MDPs admit this structure. Our main result is a logarithmic regret bound of Algorithm 1.

### Infinite-horizon Discounted MDP

In this paper we also study infinite-horizon discounted MDP, which is a tuple $\mathcal{M}:=(\mathcal{S},\mathcal{A},\gamma,P,r)$, where every step shares the same transition operator $P$ and reward function $r$. Here $\gamma$ denotes the discount factor, and there is no restart during the entire process. Let $\mathcal{C} = {\left\{ {\mathcal{S} \times \mathcal{A} \times {\lbrack 0,1\rbrack}} \right\}^{\ast} \times \mathcal{S}}$ be the set of all possible trajectories of any length. A non-stationary deterministic policy $\pi:{\mathcal{C}\rightarrow\mathcal{A}}$ is a mapping from paths to actions. The $V$ function and $Q$ function are defined as below ($c_{i}:=\left( x_{1},a_{1},r_{1},\cdots,x_{i} \right)$).

Let $V^{\ast}{(s)}$ and $Q^{\ast}{(s,a)}$ denote respectively the value function and $Q$ function of the optimal policy $\pi^{\ast}$.

### Definition 2.3 (Sub-optimality Gap)

Given ${(x,a)} \in {\mathcal{S} \times \mathcal{A}}$, the suboptimality gap of $(x,a)$ is defined as ${{\Delta{(x,a)}}:={{V^{\ast}{(x)}} - {Q^{\ast}{(x,a)}}}}.$

### Definition 2.4 (Minimum Sub-optimality Gap)

Denote by $\Delta_{\min}$ the minimum non-zero gap: $\Delta_{\min}:={\min_{x,a}\left\{ {{\Delta{(x,a)}}:{{\Delta{(x,a)}} \neq 0}} \right\}}$.

Again, if $\left\{ {\Delta{(x,a)}}:{{\Delta{(x,a)}} \neq 0} \right\} = \varnothing$, all the states are the same, and the MDP degenerates. Otherwise, we have $\Delta_{\min} > 0$.

Consider a game that starts at state $x_{1}$. A learning algorithm $\mathsf{A}\mathsf{l}\mathsf{g}$ specifies an initial non-stationary policy $\pi_{1}$. At each time step $t$, the player takes action $\pi_{t}{(x_{t})}$, observes $r_{t}$ and $x_{t + 1}$, and updates $\pi_{t}$ to $\pi_{t + 1}$. The total regret of $\mathsf{A}\mathsf{l}\mathsf{g}$ for the first $T$ steps is thus defined as ${{{Regret}{(T)}} = {\sum_{t = 1}^{T}{\left( {V^{\ast} - V^{\pi_{t}}}) \right.{(x_{t})}}}}.$ This definition was studied in Liu and Su, which follows the sample complexity definition in Kakade. For this setting, we study Algorithm 2. This is a simple adaptation of Algorithm 1 that takes $\gamma$ into account, so we defer it to the appendix. We prove Algorithm 2 also enjoys a logarithmic regret bound.

## Main Theoretical Results

Now we present our main results.

### Main Result for Episodic MDP

The following theorem characterizes the performance of Algorithm 1 for episodic MDP. To our knowledge, this is the first theoretical result showing a model-free algorithm can achieve logarithmic regret of tabular RL.

### Theorem 3.1 (Logarithmic Regret Bound of $Q$-learning for Episodic MDP)

The expected regret of Algorithm 1 for episodic tabular MDP is upper bounded by ${{\mathbb{E}}\left\lbrack {{Regret}{(K)}} \right\rbrack} \leq {\mathcal{O}\left( {\frac{H^{6}SA}{\Delta_{\min}}{\log\left( {SAT} \right)}} \right)}$.

An interesting advantage of our theorem is adaptivity. Note the algorithm we analyze is exactly the same algorithm studied in Jin et al., which has been shown to achieve the worst-case $\sqrt{T}$-type regret bound. Theorem 3.1. ‣ Main Result for Episodic MDP ‣ 3 Main Theoretical Results") suggests that one does not need to modify the algorithm to exploit the strictly positive minimum sub-optimality gap structure, Algorithm 1 *automatically adapts* to this benign structure. Importantly, Algorithm 1 does not need to know $\Delta_{\min}$.

Proposition 2.2 in Simchowitz and Jamieson suggested that any algorithm with sub-linear regret in the worst case, suffer an $\Omega\left( {\sum_{{{(x,a)},{\Delta_{1}{(x,a)}}} > 0}{\frac{H^{2}}{\Delta_{1}(x,a)}{\log T}}} \right)$ expected regret. Therefore, the dependencies on $S$, $A$ and $T$ are nearly tight in Theorem 3.1. ‣ Main Result for Episodic MDP ‣ 3 Main Theoretical Results").

One may wonder whether it is possible to obtain a regret bound that only depends the sum of positive gaps, e.g., $O\left( {\sum_{{{(x,a)},{\Delta_{1}{(x,a)}}} > 0}{\frac{H^{2}}{\Delta_{1}(x,a)}{\log T}}} \right)$, unlike ours, which is a multiple of $1/\Delta_{\min}$. Unfortunately, Simchowitz and Jamieson showed, all existing algorithms, including Algorithm 1 and their algorithm, suffer an $\Omega\left( \frac{S}{\Delta_{\min}} \right)$ regret, and new algorithmic ideas are needed in order to circumvent this lower bound.

We compare Theorem 3.1. ‣ Main Result for Episodic MDP ‣ 3 Main Theoretical Results") with the regret bound for model-based algorithm in Simchowitz and Jamieson (in big-$\mathcal{O}$ form):

First recall our bound is for a model-free algorithm which is more space-efficient and time-efficient than the model-based algorithm in Simchowitz and Jamieson. In terms of the regret bound, Theorem 3.1. ‣ Main Result for Episodic MDP ‣ 3 Main Theoretical Results")'s dependency on $H$ is worse than that in their bound. We remark that simple model-free algorithms may have a worse dependency on $H$ compared to model-based algorithms (e.g., see Jin et al. ).

Now let us consider an environment where there are $\sim {SA}$ state-action pairs whose gap is $\Delta_{\min}$. Then the bound in Simchowitz and Jamieson becomes

In this regime, both Theorem 3.1. ‣ Main Result for Episodic MDP ‣ 3 Main Theoretical Results") and their bound have an $\frac{SA}{\Delta_{\min}}$ term. Their bound also has an additional $H^{4}SA{\max(H,S)}{\log\left( \frac{SAH}{\Delta_{\min}} \right)}$ burn-in term which our bound does not have. When $S$ is large compared to $H$ and $\Delta_{\min}$, this term scales $S^{2}$ and can dominate other terms, so our bound is better. The technical reason behind this phenomenon is that Algorithm 1 uses the Hoeffding bound for constructing bonus on $Q$-value, which does not need burn-in.

### Main Result for Infinite-horizon Discounted MDP

Algorithm 1 can be easily generalized to the discounted MDP. See Algorithm 2 in the appendix. We also obtain a logarithmic regret bound for infinite-horizon discounted MDP.

### Theorem 3.2 (Logarithmic Regret Bound of $Q$-learning for Infinite-horizon Discounted MDP)

The expected regret of Algorithm 2 for infinite-horizon discounted MDP is upper bounded by ${{\mathbb{E}}\left\lbrack {{Regret}{(T)}} \right\rbrack} \leq {\mathcal{O}\left( {\frac{SA}{\Delta_{\min}\left( {1 - \gamma} \right)^{6}}{\log\frac{SAT}{\Delta_{\min}\left( {1 - \gamma} \right)}}} \right)}$.

Theorem 3.2. ‣ Main Result for Infinite-horizon Discounted MDP ‣ 3 Main Theoretical Results") suggests that model-free algorithms can achieve logarithmic regret even in the infinite-horizon discounted MDP setting. The main difference from Theorem 3.1. ‣ Main Result for Episodic MDP ‣ 3 Main Theoretical Results") is that $H$ is replaced by $\frac{1}{1 - \gamma}$. By analogy, we believe the dependencies on $S,A,T$ and $\Delta_{\min}$ are nearly tight and the dependency $\frac{1}{1 - \gamma}$ can be improved. The proof of Theorem 3.2. ‣ Main Result for Infinite-horizon Discounted MDP ‣ 3 Main Theoretical Results") is deferred to Appendix.

## Proof of Theorem 3.1. ‣ Main Result for Episodic MDP ‣ 3 Main Theoretical Results")

In this section, we prove Theorem 3.1. ‣ Main Result for Episodic MDP ‣ 3 Main Theoretical Results").

### Notations

Let ${Q_{h}^{k}{(x,a)}},{V_{h}^{k}{(x)}},{N_{h}^{k}{(x,a)}}$ denote the value of ${Q_{h}{(x,a)}},{V_{h}{(x)}}$,and $N_{h}{(x,a)}$ right before the $k$-th episode, respectively. Let ${\mathbb{I}}\lbrack \cdot \rbrack$ denote the indicator function. Let ${\tau_{h}{(x,a,i)}}:={\max\left\{ {k:{{N_{h}^{k}{(x,a)}} = {i - 1}}} \right\}}$ be the episode $k$ at which ${(x_{h}^{k},a_{h}^{k})} = {(x,a)}$ for the $i$-th time. We will abbreviate $N_{h}^{k}{(x_{h}^{k},a_{h}^{k})}$ for $n_{h}^{k}$ when no confusion can arise. $\alpha_{t}^{i}$ is defined by the following: $\alpha_{t} = \frac{H + 1}{H + t}$, $\alpha_{t}^{0} = {\prod_{j = 1}^{t}\left( {1 - \alpha_{j}} \right)}$ and $\alpha_{t}^{i} = {\alpha_{i}{\prod_{j = {i + 1}}^{t}{\left( {1 - \alpha_{j}} \right){({i > 0})}}}}$. Let $\beta_{0} = 0$ and $\beta_{t} = {4c\sqrt{\frac{H^{3}\iota}{t}}}$ for $t \geq 1$.

### Proof of Theorem 3.1. ‣ Main Result for Episodic MDP ‣ 3 Main Theoretical Results")

Our proof starts with the observation that the regret of each episode can be rewritten as the expected sum of sub-optimality gaps for each action:

In order to bound $\Delta_{h}{(x_{h}^{k},a_{h}^{k})}$ by learning error ${({Q_{h}^{k} - Q_{h}^{\ast}})}{(x_{h}^{k},a_{h}^{k})}$, we define the following concentration event.

### Definition 4.1 (Concentration of Learning Errors)

Intuitively, $\mathcal{E}_{conc}$ is the event in which all the learning errors of the value function is both bounded below (by zero) and bounded above.

We now refer to Jin et al. for the following lemma that shows $\mathcal{E}_{conc}$ happens with high probability via a concentration argument.

### Lemma 4.1 (Concentration)

Event $\mathcal{E}_{conc}$ occurs w.p. at least $1 - {1/T}$.

Lemma 4.1. ‣ Proof of Theorem 3.1 ‣ 4 Proof of Theorem 3.1") suggests that Algorithm 1 is optimistic on $\mathcal{E}_{conc}$. Combining with the greedy choice of actions yields

To bound $\Delta_{h}{(x_{h}^{k},a_{h}^{k})}$, the following notion introduced in Simchowitz and Jamieson is convenient. If we define ${{clip}\left\lbrack x \middle| \delta \right\rbrack}:={{x \cdot {\mathbb{I}}}\left\lbrack {x \geq \delta} \right\rbrack}$, then Ineq suggests that $\Delta_{h}{(x_{h}^{k},a_{h}^{k})}$ can be bounded by clipped estimation error:

Our main technique to get $1/\Delta_{\min}$ instead of $1/\Delta_{\min}^{2}$ regret bound is to classify gaps of state-action pairs into different intervals and count them separately. Note the gap can range from $\Delta_{\min}$ to $H$. Thus, we divide the interval $\left\lbrack \Delta_{\min},H \right\rbrack$ into $N$ disjoint intervals: $\left\lbrack \Delta_{\min},{2\Delta_{\min}} \right),\cdots,\left\lbrack {2^{N - 1}\Delta_{\min}},{2^{N}\Delta_{\min}} \right\rbrack$, where $N = \left\lceil {\log_{2}\left( {H/\Delta_{\min}} \right)} \right\rceil$.

Lemma 4.2. ‣ Proof of Theorem 3.1 ‣ 4 Proof of Theorem 3.1") below is our main technical lemma which upper bounds the number of steps Algorithm 1 chooses a sub-optimal action whose suboptimality is in a certain interval.

### Lemma 4.2 (Bounded Number of Steps in Each Interval)

Under $\mathcal{E}_{conc}$, we have for every $n \in \lbrack N\rbrack$,

Before we give the proof for Lemma 4.2. ‣ Proof of Theorem 3.1 ‣ 4 Proof of Theorem 3.1"), we first show how to use Lemma 4.2. ‣ Proof of Theorem 3.1 ‣ 4 Proof of Theorem 3.1") to prove Theorem 3.1. ‣ Main Result for Episodic MDP ‣ 3 Main Theoretical Results").

### Proof of Theorem 3.1. ‣ Main Result for Episodic MDP ‣ 3 Main Theoretical Results")

Since the trajectories inside $\mathcal{E}_{conc}$ have bounded empirical regret, and complementary event $\overline{\mathcal{E}_{conc}}$ happens with sufficiently low probability,

Above, follows from the definition of expectation, is because Ineq suggests that for trajectories inside $\mathcal{E}_{conc}$, gaps can be bounded by clipped learning errors; whereas for trajectories outside of $\mathcal{E}_{conc}$, sub-optimality gaps never exceed $H$. follows from adding an outer summation for state-action pairs over the $N$ disjoint subintervals, then bounding the estimation error in each subinterval by its maximum value times the number of steps it contains. comes from a sum of numbers in a geometric progression generated by Lemma 4.2. ‣ Proof of Theorem 3.1 ‣ 4 Proof of Theorem 3.1"), and the fact that ${{\mathbb{P}}\left( \overline{\mathcal{E}_{conc}} \right)} \leq {1/T}$ from concentration Lemma 4.1. ‣ Proof of Theorem 3.1 ‣ 4 Proof of Theorem 3.1"). In the final step, we notice that $\iota = {\log{({SAT^{2}})}} = {\mathcal{O}\left( {\log{({SAT})}} \right)}$. ∎

### Proof of Lemma 4.2. ‣ Proof of Theorem 3.1 ‣ 4 Proof of Theorem 3.1")

The proof of Lemma 4.2. ‣ Proof of Theorem 3.1 ‣ 4 Proof of Theorem 3.1") relies on a general lemma (Lemma 4.3. ‣ Proof of Lemma 4.2 ‣ 4 Proof of Theorem 3.1")) characterizing a weighted sum of the estimation errors of $Q$-function.Then we choose a particular sequence of weights to prove Lemma 4.2. ‣ Proof of Theorem 3.1 ‣ 4 Proof of Theorem 3.1"). We remark that this general idea has appeared in Jin et al.; Wang et al.; Zhang et al..

Formally, we use the following definition.

### Definition 4.2 ($(C,w)$-Sequence (Definition 3 in Wang et al. (2019)))

A sequence $\left\{ w_{k} \right\}_{k \geq 1}$ is called a $(C,w)$-sequence if $0 \leq w_{k} \leq w$ for all $k$ and ${\sum_{k}w_{k}} \leq C$.

### Lemma 4.3 (Weighted Sum of Learning Errors)

On event $\mathcal{E}_{conc}$, for every $h \in {\lbrack H\rbrack}$, if $\left\{ w_{k} \right\}_{k \in {\lbrack K\rbrack}}$ is a $(C,w)$-sequence, then:

Before presenting the proof of Lemma 4.3. ‣ Proof of Lemma 4.2 ‣ 4 Proof of Theorem 3.1"), we refer the readers to Jin et al. for Lemma 4.4. ‣ Proof of Lemma 4.2 ‣ 4 Proof of Theorem 3.1") below, which summarizes the properties of $\alpha_{t}^{i}$ that will be useful in our proof.

### Lemma 4.4 (Properties of $\alpha_{t}^{i}$)

Let $\alpha_{t} = \frac{H + 1}{H + t}$, $\alpha_{t}^{0} = {\prod_{j = 1}^{t}\left( {1 - \alpha_{j}} \right)}$ and $\alpha_{t}^{i} = {\alpha_{i}{\prod_{j = {i + 1}}^{t}\left( {1 - \alpha_{j}} \right)}}$ for $0 < i \leq t$.

${\sum_{i = 1}^{t}\alpha_{t}^{i}} = 1$ and $\alpha_{t}^{0} = 0$ for every $t \geq 1$, ${\sum_{i = 1}^{t}\alpha_{t}^{i}} = 0$ and $\alpha_{t}^{0} = 1$ for $t = 0$.

${\sum_{t = i}^{\infty}\alpha_{t}^{i}} = {1 + \frac{1}{H}}$ for every $i \geq 1$.

### Proof of Lemma 4.3. ‣ Proof of Lemma 4.2 ‣ 4 Proof of Theorem 3.1")

We will recursively bound the weighted sum of step $h$ by its next step $({h + 1})$, and unroll $({{H - h} + 1})$ times for the desired bound. As suggested by Lemma 4.1. ‣ Proof of Theorem 3.1 ‣ 4 Proof of Theorem 3.1"), upper bounds of learning error holds under $\mathcal{E}_{conc}$. Thus we have

For the first term of, $n_{h}^{k} = 0$ at most once for every state-action pair, and we always have $w_{k} \leq w$. Thus,

The second term of can be bounded by the following inequalities with respective reasons listed below:

Above, comes from prior definition $\beta_{t} = {4c\sqrt{\frac{H^{3}\iota}{t}}}$ when $t \geq 1$ and $\beta_{0} = 0$. Note that $\tau_{h}{(x,a,i)}$ is the episode where $(x,a)$ is visited for the $i$-th time, so we always have $n_{h}^{\tau_{h}{(x,a,i)}} = {i - 1}$. follows from a rearrangement inequality with $C_{s,a}$ defined as $C_{s,a}:={\sum_{i = 1}^{n_{h}^{K}{(s,a)}}w_{\tau{(s,a,i)}}}$, where we always keep in mind that $0 < w_{\tau{(s,a,i)}} \leq w$. follows from the integral conversion of $\sum_{i}{1/\sqrt{i}}$, and is true because of Cauchy-Schwartz inequality where ${\sum_{s,a}C_{s,a}} = {\sum_{k = 1}^{K}w_{k}} \leq C$.

For the third term in Ineq, we notice that ${V_{h}^{k}{(x_{h}^{k})}} = {Q_{h}^{k}{(x_{h}^{k},a_{h}^{k})}}$ due to greedy choice of actions and ${V_{h}^{\ast}{(x_{h}^{k})}} \geq {Q_{h + 1}^{\ast}{(x_{h + 1}^{k},a_{h + 1}^{k})}}$ by definition. Therefore ${\left( {V_{h}^{k} - V_{h}^{\ast}}) \right.{(x_{h}^{k})}} \leq {\left( {Q_{h}^{k} - Q_{h}^{\ast}}) \right.{(x_{h}^{k},a_{h}^{k})}}$. Note that ${\forall k} \in {\lbrack K\rbrack}$, the third term takes into account all the prior episodes $l < k$ where ${(x_{h}^{k},a_{h}^{k})} = {(x_{h}^{l},a_{h}^{l})}$, indicating that the learning error at step $l$ is only counted by subsequent episodes $k > l$ when the same $(s,a)$ is visited. Thus, we exchange the order of summation and obtain

Then for $l \in {\lbrack K\rbrack}$ we let ${\overset{\sim}{w}}_{l} = {\sum\limits_{j = {n_{h}^{l} + 1}}^{N_{h}^{K}{(x_{h}^{l},a_{h}^{l})}}{w_{\tau_{h}{(x_{h}^{l},a_{h}^{l},j)}}\alpha_{j}^{n_{h}^{l} + 1}}}$ and further simplify the above equation to be

Next, we use Lemma 4.4. ‣ Proof of Lemma 4.2 ‣ 4 Proof of Theorem 3.1") to verify that $\left\{ {\overset{\sim}{w}}_{l} \right\}_{l \in {\lbrack K\rbrack}}$ is a $\left( C,{{({1 + \frac{1}{H}})}w} \right)$-sequence:

Plugging the upper bounds of three separate terms in, and back into Ineq gives us

where the third term is a weighted sum of learning errors of the same format, but taken at level $h + 1$. In addition, it has weights $\left\{ {\overset{\sim}{w}}_{l} \right\}_{l \in {\lbrack K\rbrack}}$ being a $\left. (C,{{({1 + {1/H}})}w} \right)$-sequence. Therefore, the above analysis will also yield

Recursing this argument for ${h + 1},{h + 2},\cdots,H$ gives us

which is the desired conclusion.

With Lemma 4.3. ‣ Proof of Lemma 4.2 ‣ 4 Proof of Theorem 3.1"), we can easily prove Lemma 4.2. ‣ Proof of Theorem 3.1 ‣ 4 Proof of Theorem 3.1") by choosing a particular $(C,w)$-sequence.

### Proof of Lemma 4.2. ‣ Proof of Theorem 3.1 ‣ 4 Proof of Theorem 3.1")

For every $n \in {\lbrack N\rbrack}$, $h \in {\lbrack H\rbrack}$, let

By definition, ${\forall h} \in {\lbrack H\rbrack}$ and $n \in {\lbrack N\rbrack}$, $\left. \{ w_{k}^{(n,h)} \right\}_{k \in {\lbrack K\rbrack}}$ is a $(C^{(n,h)},1)$-sequence. Now we consider bounding $\sum_{k = 1}^{K}{w_{k}^{(n,h)}{({Q_{h}^{k} - Q_{h}^{\ast}})}{(x_{h}^{k},a_{h}^{k})}}$ from both sides. On the one hand, by Lemma 4.3. ‣ Proof of Lemma 4.2 ‣ 4 Proof of Theorem 3.1"),

On the other hand, according to the definition of $w_{k}^{(n,h)}$,

Combining these two sides, we obtain the following inequality of $C^{(n,h)}$:

Finally, we observe that

which is exactly the statement of Lemma 4.2. ‣ Proof of Theorem 3.1 ‣ 4 Proof of Theorem 3.1"). ∎

## Conclusion and Future Directions

This paper gives the first logarithmic regret bounds for $Q$-learning in both finite-horizon and discounted tabular MDPs. Below we list some future directions that we believe are worth exploring.

### $H$ dependence

The dependency on $H$ in our regret bound for episodic RL is $H^{6}$, which we believe is suboptimal. As discussed in Simchowitz and Jamieson, improving the $H$ dependence is often a challenging task. Recently, Zhang et al. showed a model-free algorithm can achieve near-optimal regret in the worst case using the idea of reference value function. It would be interesting to apply this idea to improve the $H$ dependence in our logarithmic regret bound.

### Function Approximation

Lastly, we note that recently researchers found the sub-optimality gap assumption is crucial for dealing with large state-space RL problems where function approximation is needed. Du et al. presented an algorithm that enjoys polynomial sample complexity if there is a sub-optimality gap and the environment satisfies a low-variance assumption. Du et al. further showed this assumption is necessary in certain settings. There is another line of works putting certain low-rank assumptions on MDPs. It would be interesting to extend our analysis to these settings and obtain logarithmic regret bounds.
