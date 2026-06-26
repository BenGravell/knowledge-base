<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Settling the Sample Complexity of Online Reinforcement Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A central issue lying at the heart of online reinforcement learning (RL) is data efficiency. While a number of recent works achieved asymptotically minimal regret in online RL, the optimality of these results is only guaranteed in a ``large-sample'' regime, imposing enormous burn-in cost in order for their algorithms to operate optimally. How to achieve minimax-optimal regret without incurring any burn-in cost has been an open problem in RL theory. We settle this problem for the context of finite-horizon inhomogeneous Markov decision processes. Specifically, we prove that a modified version of Monotonic Value Propagation (MVP), a model-based algorithm proposed , achieves a regret on the order of (modulo log factors) \begin{equation*} \min\big\{ \sqrt{SAH^3K}, \,HK \big\}, \end{equation*} where S is the number of states, A is the number of actions, H is the planning horizon, and K is the total number of episodes. This regret matches the minimax lower bound for the entire range of sample size K >= 1, essentially eliminating any burn-in requirement.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

It also translates to a PAC sample complexity (i.e., the number of episodes needed to yield epsilon-accuracy) of SAH^/epsilon^ up to log factor, which is minimax-optimal for the full epsilon-range. Further, we extend our theory to unveil the influences of problem-dependent quantities like the optimal value/cost and certain variances. The key technical innovation lies in the development of a new regret decomposition strategy and a novel analysis paradigm to decouple complicated statistical dependency - a long-standing challenge facing the analysis of online RL in the sample-hungry regime.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In reinforcement learning (RL), an agent is often asked to learn optimal decisions (i.e., the ones that maximize cumulative reward) through real-time "trial-and-error" interactions with an unknown environment. This task is commonly dubbed as online RL, underscoring the critical role of adaptive online data collection and differentiating it from other RL settings that rely upon pre-collected data. A central challenge in achieving sample-efficient online RL boils down to how to optimally balance exploration and exploitation during data collection, namely, how to trade off the potential revenue of exploring unknown terrain/dynamics against the benefit of exploiting past experience. While decades-long effort has been invested towards unlocking the capability of online RL, how to fully characterize --- and more importantly, attain --- its fundamental performance limit remains largely unsettled.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we take an important step towards settling the sample complexity limit of online RL, focusing on tabular Markov Decision Processes (MDPs) with finite horizon and finite state-action space. More concretely, imagine that one seeks to learn a near-optimal policy of a time-inhomogeneous MDP with $S$ states, $A$ actions, and horizon length $H$, and is allowed to execute the MDP of interest $K$ times to collect $K$ sample episodes each of length $H$. This canonical problem is among the most extensively studied in the RL literature, with formal theoretical pursuit dating back to more than 25 years ago (e.g., kearns1998near).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Numerous works have since been devoted to improving the sample efficiency and/or refining the analysis framework (brafman2002r; kakade2003sample; jaksch2010near; azar2017minimax; jin2018q; dann2017unifying; zanette2019tighter; bai2019provably; zhang2020almost; zhang2020reinforcement; menard2021ucb; li2021breaking; domingues2021episodic). As we shall elucidate momentarily, however, information-theoretic optimality has only been achieved in the "large-sample" regime. When it comes to the most challenging sample-hungry regime, there remains a substantial gap between the state-of-the-art regret upper bound and the best-known minimax lower bound, which motivates the research of this paper.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Inadequacy of prior art: enormous burn-in cost", "weight": 1.0} -->

While past research has obtained asymptotically optimal (i.e., optimal when $K$ approaches infinity) regret bounds in the aforementioned setting, all of these results incur an enormous burn-in cost --- that is, the minimum sample size needed for an algorithm to operate sample-optimally --- which we explain in the sequel. For simplicity of presentation, we assume that each immediate reward lies within the normalized range $\lbrack 0,1\rbrack$ when discussing the prior art.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Minimax lower bound", "weight": 1.0} -->

To provide a theoretical benchmark, we first make note of the best-known minimax regret lower bound developed by jin2018q; domingues2021episodic:^11^1Let $\mathcal{X} = {\{ S,A,H,K,\frac{1}{\delta}\}}$, where $1 - \delta$ is the target success rate (to be seen shortly).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Minimax lower bound", "weight": 1.0} -->

Moreover, $\overset{\sim}{O}(\cdot)$, $\overset{\sim}{\Omega}(\cdot)$ and $\overset{\sim}{\Theta}(\cdot)$ are defined analogously, except that all logarithmic dependency on the quantities of $\mathcal{X}$ are hidden. assuming that the immediate reward at each step falls within $\lbrack 0,1\rbrack$ and imposing no restriction on $K$. Given that a regret of $O{({HK})}$ can be trivially achieved (as the sum of rewards in any $K$ episodes cannot exceed $HK$), we shall sometimes drop the $HK$ term and simply write

<!-- chunk {"id": "body-0010", "role": "body", "section": "Prior upper bounds and burn-in cost", "weight": 1.0} -->

We now turn to the upper bounds developed in prior literature. For ease of presentation, we shall assume in the rest of this subsection unless otherwise noted. Log factors are also ignored in the discussion below.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Prior upper bounds and burn-in cost", "weight": 1.0} -->

The first paper that achieves asymptotically optimal regret is azar2017minimax, which came up with a model-based algorithm called $\mathtt{U}\mathtt{C}\mathtt{B}\mathtt{V}\mathtt{I}$ that enjoys a regret bound $\overset{\sim}{O}\left({\sqrt{SAH^{3}K} + {H^{3}S^{2}A}} \right)$. A close inspection reveals that this regret matches the minimax lower bound if and only if due to the presence of the lower-order term $H^{3}S^{2}A$ in the regret bound. This burn-in cost is clearly undesirable, since the sample size available in many practical scenarios might be far below this requirement.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Prior upper bounds and burn-in cost", "weight": 1.0} -->

In light of its fundamental importance in contemporary RL applications (which often have very large dimensionality and relatively limited data collection capability), reducing the burn-in cost without compromising sample efficiency has emerged as a central problem in recent pursuit of RL theory (zanette2019tighter; dann2019policy; zhang2020reinforcement; zhou2023sharp; menard2021ucb; li2021breaking; li2021settling; li2022minimax; agarwal2020model; sidford2018variance). The state-of-the-art regret upper bounds for finite-horizon inhomogeneous MDPs can be summarized below (depending on the size of $K$): meaning that even the most advanced prior results fall short of sample optimality unless The interested reader is referred to Table 1 for more details about existing regret upper bounds and their associated sample complexities.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Prior upper bounds and burn-in cost", "weight": 1.0} -->

In summary, no prior theory was able to achieve optimal sample complexity in the data-hungry regime suffering from a significant barrier of either long horizon (as in the term $SAH^{5}$) or large state space (as in the term $S^{3}AH$). In fact, the information-theoretic limit is yet to be determined within this regime (i.e., neither the achievability results nor the lower bounds had been shown to be tight), although it has been conjectured by menard2021ucb that the lower bound reflects the correct scaling for any sample size $K$.^22^2Note that the original conjecture in menard2021ucb was $\overset{\sim}{\Theta}\left({\sqrt{SAH^{3}K} + {SAH^{2}}} \right)$. Combining it with the trivial upper bound $HK$ allows one to remove the term $SAH^{2}$ (with a little algebra).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Comparisons with other RL settings and key challenges", "weight": 1.0} -->

In truth, the incentives to minimize the burn-in cost and improve data efficiency arise in multiple other settings beyond online RL. For instance, in an idealistic setting that assumes access to a simulator (or a generative model) --- a model that allows the learner to query arbitrary state-action pairs to draw samples --- a recent work li2020breaking developed a perturbed model-based approach that is provably optimal without incurring any burn-in cost. Analogous results have been obtained in li2021settling for offline RL --- a setting that requires policy learning to be performed based on historical data --- unveiling the full-range optimality of a pessimistic model-based algorithm.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Comparisons with other RL settings and key challenges", "weight": 1.0} -->

Unfortunately, the algorithmic and analysis frameworks developed in the above two works fail to accommodate the online counterpart. The main hurdle stems from the complicated statistical dependency intrinsic to episodic online RL; for instance, in online RL, the empirical transition probabilities and the running estimates of the value function are oftentimes statistically dependent in an intertwined manner (unless we waste data). How to decouple the intricate statistical dependency without compromising data efficiency constitutes the key innovation of this work. More precise, in-depth technical discussions will be provided in Section 4.

<!-- chunk {"id": "body-0016", "role": "body", "section": "A peek at our main contributions", "weight": 1.0} -->

We are now positioned to summarize the main findings of this paper. Focusing on time-inhomogeneous finite-horizon MDPs, our main contributions can be divided into two parts: the first part fully settles the minimax-optimal regret and sample complexity of online RL, whereas the second part further extends and augments our theory to make apparent the impacts of certain problem-dependent quantities. Throughout this subsection, the regret metric ${\mathsf{R}\mathsf{e}\mathsf{g}\mathsf{r}\mathsf{e}\mathsf{t}}{(K)}$ captures the cumulative sub-optimality gap (i.e., the gap between the performance of the policy iterates and that of the optimal policy) over all $K$ episodes, to be formally defined.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Settling the optimal sample complexity with no burn-in cost", "weight": 1.0} -->

Our first result fully determines the sample complexity limit of online RL in a minimax sense, allowing one to attain the optimal regret regardless of the number $K$ of episodes that can be collected.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Extension: optimal problem-dependent regret bounds", "weight": 1.0} -->

In practice, RL algorithms often perform far more appealingly than what their worst-case performance guarantees would suggest. This motivates a recent line of works that investigate optimal performance in a more problem-dependent fashion (talebi2018variance; simchowitz2019non; zanette2019tighter; zhou2023sharp; fruit2018efficient; xu2021fine; yang2021q; jin2020reward; wagenmaker2022first; zhao2023variance; dann2021beyond; tirinzoni2021fully). Encouragingly, the proposed algorithm automatically achieves optimality on a more refined problem-dependent level, without requiring prior knowledge of additional problem-specific knowledge. This results in several extended theorems that take into account different problem-dependent quantities.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Extension: optimal problem-dependent regret bounds", "weight": 1.0} -->

The first extension below investigates how the optimal value influences the regret bound.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Related works", "weight": 1.0} -->

Let us take a moment to discuss several related theoretical works on tabular RL. Note that there has also been an active line of research that exploits low-dimensional function approximation to further reduce sample complexity, which is beyond the scope of this paper.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Related works", "weight": 1.0} -->

Our discussion below focuses on two mainstream approaches that have received widespread adoption: the model-based approach and the model-free approach. In a nutshell, model-based algorithms decouple model estimation and policy learning, and often use the learned transition kernel to compute the value function and find a desired policy. In stark contrast, the model-free approach attempts to estimate the optimal value function and optimal policy directly without explicit estimation of the model. In general, model-free algorithms only require $O{({SAH})}$ memory --- needed when storing the running estimates for Q-functions and value functions --- while the model-based counterpart might require $\Omega{({S^{2}AH})}$ space in order to store the estimated transition kernel.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Sample complexity for RL with a simulator", "weight": 1.0} -->

As an idealistic setting that separates the consideration of exploration from that of estimation, RL with a simulator (or generative model) has been studied by numerous works, allowing the learner to draw independent samples for any state-action pairs (kearns1998finite; pananjady2020instance; kakade2003sample; azar2013minimax; agarwal2020model; wainwright2019variance; wainwright2019stochastic; sidford2018near; sidford2018variance; chen2020finite; li2020breaking; li2023q; li2022minimax; even2003learning; shi2023curious; beck2012error; cui2021minimax). While both model-based and model-free approaches are capable of achieving asymptotic sample optimality (sidford2018variance; wainwright2019variance; azar2013minimax; agarwal2020model), all model-free algorithms that enjoy asymptotically optimal sample complexity suffer from dramatic burn-in cost.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Sample complexity for RL with a simulator", "weight": 1.0} -->

Thus far, only the model-based approach has been shown to fully eliminate the burn-in cost for both discounted infinite-horizon MDPs and inhomogeneous finite-horizon MDPs (li2020breaking). The full-range optimal sample complexity for time-homogeneous finite-horizon MDPs in the presence of a simulator remains open.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Sample complexity for offline RL", "weight": 1.0} -->

The subfield of offline RL is concerned with learning based purely on a pre-collected dataset (levine2020offline). A frequently used mathematical model assumes that historical data are collected (often independently) using some behavior policy, and the key challenges (compared with RL with a simulator) come from distribution shift and incomplete data coverage. The sample complexity of offline RL has been the focus of a large strand of recent works, with asymptotically optimal sample complexity achieved by multiple algorithms (jin2021pessimism; xie2021policy; yin2022near; ren2021nearly; shi2022pessimistic; qu2020finite; yan2022efficacy; rashidinejad2021bridging; li2022settling; li2021sample; wang2022gap). Akin to the simulator setting, the fully optimal sample complexity (without burn-in cost) has only been achieved via the model-based approach when it comes to discounted infinite-horizon and inhomogeneous finite-horizon settings (li2022settling).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Sample complexity for offline RL", "weight": 1.0} -->

All asymptotically optimal model-free methods incur substantial burn-in cost. The case with time-homogeneous finite-horizon MDPs also remains unsettled.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Sample complexity for online RL", "weight": 1.0} -->

Obtaining optimal sample complexity (or regret bound) in online RL without incurring any burn-in cost has been one of the most fundamental open problems in RL theory.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Sample complexity for online RL", "weight": 1.0} -->

In fact, the past decades have witnessed a flurry of activity towards improving the sample efficiency of online RL, partial examples including kearns1998near; brafman2002r; kakade2003sample; strehl2006pac; strehl2008analysis; kolter2009near; bartlett2009regal; jaksch2010near; szita2010model; lattimore2012pac; osband2013more; dann2015sample; agralwal2017optimistic; dann2017unifying; jin2018q; efroni2019tight; fruit2018efficient; zanette2019tighter; cai2019provably; dong2019q; russo2019worst; pacchiano2020optimism; neu2020unifying; zhang2020almost; zhang2020reinforcement; tarbouriech2021stochastic; xiong2021randomized; menard2021ucb; wang2020long; li2021settling; li2021breaking;

<!-- chunk {"id": "body-0028", "role": "body", "section": "Sample complexity for online RL", "weight": 1.0} -->

domingues2021episodic; zhang2022horizon; li2023minimax; li2024reward; ji2023regret.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Sample complexity for online RL", "weight": 1.0} -->

Unfortunately, no work has been able to conquer this problem completely: the state-of-the-art result for model-based algorithms still incurs a burn-in that scales at least quadratically in $S$ (zhang2020reinforcement), while the burn-in cost of the best model-free algorithms (particularly with the aid of variance reduction introduced in zhang2020almost) still suffers from highly sub-optimal horizon dependency (li2021breaking).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

In this section, we introduce the basics of tabular online RL, as well as some basic assumptions to be imposed throughout.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Basics of finite-horizon MDPs", "weight": 1.0} -->

This paper concentrates on time-inhomogeneous (or nonstationary) finite-horizon MDPs. Throughout the paper, we employ $\mathcal{S} = {\{ 1,\ldots,S\}}$ to denote the state space, $\mathcal{A} = {\{ 1,\ldots,A\}}$ the action space, and $H$ the planning horizon. The notation $P = \left\{ P_{h}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\Delta{(\mathcal{S})}}} \right\}_{1 \leq h \leq H}$ denotes the probability transition kernel of the MDP; for any current state $s$ at any step $h$, if action $a$ is taken, then the state at the next step $h + 1$ of the environment is randomly drawn from $P_{s,a,h} ≔ P_{h}{( \cdot |s,a)} \in \Delta{(\mathcal{S})}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Basics of finite-horizon MDPs", "weight": 1.0} -->

Also, the notation $R = \left\{ {R_{s,a,h} \in {\Delta{({\lbrack 0,H\rbrack})}}} \right\}_{{1 \leq h \leq H},{{s \in \mathcal{S}},{a \in \mathcal{A}}}}$ indicates the reward distribution; that is, while executing action $a$ in state $s$ at step $h$, the agent receives an immediate reward --- which is non-negative and possibly stochastic --- drawn from the distribution $R_{s,a,h}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Basics of finite-horizon MDPs", "weight": 1.0} -->

Additionally, a deterministic policy $\pi = {\{\pi_{h}:{\mathcal{S}\rightarrow\mathcal{A}}\}}_{1 \leq h \leq H}$ stands for an action selection rule, so that the action selected in state $s$ at step $h$ is given by $\pi_{h}{(s)}$. The readers can consult standard textbooks (e.g., bertsekas2019reinforcement) for more extensive descriptions.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Basics of finite-horizon MDPs", "weight": 1.0} -->

In each episode, a trajectory $(s_{1},a_{1},r_{1}',s_{2},\ldots,s_{H},a_{H},r_{H}')$ is rolled out as follows: the learner starts from an initial state $s_{1}$ independently drawn from some fixed (but unknown) distribution $\mu \in {\Delta{(\mathcal{S})}}$; for each step $1 \leq h \leq H$, the learner takes action $a_{h}$, gains an immediate reward $r_{h}' \sim R_{s_{h},a_{h},h}$, and the environment transits to the state $s_{h + 1}$ at step $h + 1$ according to $P_{s_{h},a_{h},h}$. Note that both the reward and the state transition are independently drawn from their respective distributions, depending solely on the current state-action-step triple but not any previous outcomes.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Basics of finite-horizon MDPs", "weight": 1.0} -->

All of our results in this paper operate under the following assumption on the total reward.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

As can be easily seen, Assumption 1 is less stringent than another common choice that assumes $r_{h}' \in {\lbrack 0,1\rbrack}$ for any $h$ in any episode. In particular, Assumption 1 allows for sparse and spiky rewards along an episode; more discussions can be found in (jiang2018open; wang2020long).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Value function and Q-function", "weight": 1.0} -->

$h < j \leq H$) is chosen in the definition of $V_{h}^{\pi}$ (resp. $Q_{h}^{\pi}$). Accordingly, we define the optimal value function and the optimal $Q$-function respectively as: Throughout this paper, we shall often abuse the notation by letting both $V_{h}^{\pi}$ and $V_{h}^{\star}$ (resp. $Q_{h}^{\pi}$ and $Q_{h}^{\star}$) represent $S$-dimensional (resp. $SA$-dimensional) vectors containing all elements of the corresponding value functions (resp. Q-functions). Two important properties are worth mentioning: (a) the optimal value and the optimal Q-function are linked by the Bellman equation: \(b\) there exists a deterministic policy, denoted by $\pi^{\star}$, that achieves optimal value functions and Q-functions for all state-action-step tuples simultaneously, that is,

<!-- chunk {"id": "body-0038", "role": "body", "section": "Data collection protocol and performance metrics", "weight": 1.0} -->

During the learning process, the learner is allowed to collect $K$ episodes of samples (using arbitrary policies it selects). More precisely, in the $k$-th episode, the learner is given an independently generated initial state $s_{1}^{k} \sim \mu$, and executes policy $\pi^{k}$ (chosen based on data collected in previous episodes) to obtain a sample trajectory $\left\{ {(s_{h}^{k},a_{h}^{k},r_{h}^{k})} \right\}_{1 \leq h \leq H}$, with $s_{h}^{k}$, $a_{h}^{k}$ and $r_{h}^{k}$ denoting the state, action and immediate reward at step $h$ of this episode.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Data collection protocol and performance metrics", "weight": 1.0} -->

To evaluate the learning performance, a widely used metric is the (cumulative) regret over all $K$ episodes: and our goal is to design an online RL algorithm that minimizes ${\mathsf{R}\mathsf{e}\mathsf{g}\mathsf{r}\mathsf{e}\mathsf{t}}{(K)}$ regardless of the allowable sample size $K$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Data collection protocol and performance metrics", "weight": 1.0} -->

It is also well-known (see, e.g., jin2018q) that a regret bound can often be readily translated into a PAC sample complexity result, the latter of which counts the number of episodes needed to find an $\varepsilon$-optimal policy $\hat{\pi}$ in the sense that ${{\mathbb{E}}_{s_{1} \sim \mu}\left\lbrack {{V_{1}^{\star}{(s_{1})}} - {V_{1}^{\hat{\pi}}{(s_{1})}}} \right\rbrack} \leq \varepsilon$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Data collection protocol and performance metrics", "weight": 1.0} -->

{f{(S,A,H)}K^{- \alpha}}$, thus resulting in a sample complexity bound of $\left(\frac{f{(S,A,H)}}{\varepsilon} \right)^{1/\alpha}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "A model-based algorithm: Monotonic Value Propagation", "weight": 1.0} -->

In this section, we formally describe our algorithm: a simple variation of the model-based algorithm called Monotonic Value Propagation proposed by zhang2020reinforcement. We present the full procedure in Algorithm 1, and point out several key ingredients.

<!-- chunk {"id": "body-0043", "role": "body", "section": "A model-based algorithm: Monotonic Value Propagation", "weight": 1.0} -->

Optimistic updates using upper confidence bounds (UCB). The algorithm implements the optimism principle in the face of uncertainty by adopting the frequently used UCB-based framework (see, e.g., $\mathtt{U}\mathtt{C}\mathtt{B}\mathtt{V}\mathtt{I}$ by azar2017minimax).

<!-- chunk {"id": "body-0044", "role": "body", "section": "A model-based algorithm: Monotonic Value Propagation", "weight": 1.0} -->

More specifically, the learner calculates the optimistic Bellman equation backward (from $h = {H,\ldots,1}$): it first computes an empirical estimate $\hat{P} = {\{{{\hat{P}}_{h} \in {\mathbb{R}}^{{SA} \times S}}\}}_{1 \leq h \leq H}$ of the transition probability kernel as well as an empirical estimate $\hat{r} = {\{{{\hat{r}}_{h} \in {\mathbb{R}}^{SA}}\}}_{1 \leq h \leq H}$ of the mean reward function, and then maintains upper estimates for the associated value function and Q-function using for all state-action pairs. Here, $Q_{h}$ (resp. $V_{h}$) indicates the running estimate for the Q-function (resp.

<!-- chunk {"id": "body-0045", "role": "body", "section": "A model-based algorithm: Monotonic Value Propagation", "weight": 1.0} -->

value function), whereas ${b_{h}{(s,a)}} \geq 0$ is some suitably chosen bonus term that compensates for the uncertainty. The above opportunistic Q-estimate in turn allows one to obtain a policy estimate (via a simple greedy rule), which will then be executed to collect new data. The fact that we first estimate the model (i.e., the transition kernel and mean rewards) makes it a model-based approach. Noteworthily, the empirical model $(\hat{P},\hat{r})$ shall be updated multiple times as new samples continue to arrive, and hence the updating rule will be invoked multiple times as well.

<!-- chunk {"id": "body-0046", "role": "body", "section": "A model-based algorithm: Monotonic Value Propagation", "weight": 1.0} -->

1 input: state space 𝒮, action space 𝒜, horizon H, total number of episodes K, confidence parameter δ, $c_{1} = \frac{460}{9}$, $c_{2} = {2\sqrt{2}}$, $c_{3} = \frac{544}{9}$. 2 initialization: set $\delta'\leftarrow\frac{\delta}{200SAH^{2}K^{2}}$, and for all (s, a, s′, h) ∈ 𝒮 × 𝒜 × 𝒮 × [H], set θh(s, a) ← 0, κh(s, a) ← 0, Nhall(s, a, s′) ← 0, Nh(s, a, s′) ← 0, Nh(s, a) ← 0, Qh(s, a) ← H, Vh(s) ← H. Set πk such that πhk(s) = arg maxaQh(s, a) for all s ∈ 𝒮 and h ∈ [H]. /* policy update.

<!-- chunk {"id": "body-0047", "role": "body", "section": "A model-based algorithm: Monotonic Value Propagation", "weight": 1.0} -->

*/Observe shk, take action ahk = arg maxaQh(shk, a), receive rhk, observe sh + 1k. /* sampling. */6 Update Nhall(s, a) ← Nhall(s, a) + 1, Nh(s, a, s′) ← Nh(s, a, s′) + 1, θh(s, a) ← θh(s, a) + rhk, κh(s, a) ← κh(s, a) + (rhk)2. /* perform updates using data of this epoch. */7 if Nhall(s, a) ∈ {1, 2, …, 2log2K} then ${N_{h}{(s,a)}}\leftarrow{\sum_{\overset{\sim}{s}}{N_{h}{(s,a,\overset{\sim}{s})}}}$. // number of visits to (s, a, h) in this epoch.

<!-- chunk {"id": "body-0048", "role": "body", "section": "A model-based algorithm: Monotonic Value Propagation", "weight": 1.0} -->

8 Set TRIGGERED = TRUE, and θh(s, a) ← 0, κh(s, a) ← 0, ${N_{h}{(s,a,\overset{\sim}{s})}}\leftarrow 0$ for all $\overset{\sim}{s} \in \mathcal{S}$. /* optimistic Q-estimation using empirical model of this epoch. */10 if TRIGGERED= TRUE then 11 Set TRIGGERED = FALSE, and VH + 1(s) ← 0 for all s ∈ 𝒮.

<!-- chunk {"id": "body-0049", "role": "body", "section": "A model-based algorithm: Monotonic Value Propagation", "weight": 1.0} -->

Compared to the original $\mathtt{U}\mathtt{C}\mathtt{B}\mathtt{V}\mathtt{I}$ (azar2017minimax), one distinguishing feature of $\mathtt{M}\mathtt{V}\mathtt{P}$ is to update the empirical transition kernel and empirical rewards in an epoch-based fashion, as motivated by a doubling update framework adopted in jaksch2010near. More concretely, the whole learning process is divided into consecutive epochs via a simple doubling rule; namely, whenever there exits a $(s,a,h)$-tuple whose visitation count reaches a power of 2, we end the current epoch, reconstruct the empirical model (cf. lines 1 and 1 of Algorithm 1), compute the Q-function and value function using the newly updated transition kernel and rewards (cf.), and then start a new epoch with an updated sampling policy.

<!-- chunk {"id": "body-0050", "role": "body", "section": "A model-based algorithm: Monotonic Value Propagation", "weight": 1.0} -->

This stands in stark contrast with the original $\mathtt{U}\mathtt{C}\mathtt{B}\mathtt{V}\mathtt{I}$, which computes new estimates for the transition model, Q-function and value function in every episode. With this doubling rule in place, the estimated transition probability vector for each $(s,a,h)$-tuple will be updated by no more than $\log_{2}K$ times, a feature that plays a pivotal role in significantly reducing some sort of covering number needed in our covering-based analysis (as we shall elaborate on shortly in Section 4). In each epoch, the learned policy is induced by the optimistic Q-function estimate --- computed based on the empirical transition kernel of the current epoch --- which will then be employed to collect samples in all episodes of the next epoch. More technical explanations of the doubling update rule will be provided in Section 4.2.

<!-- chunk {"id": "body-0051", "role": "body", "section": "A model-based algorithm: Monotonic Value Propagation", "weight": 1.0} -->

Monotonic bonus functions. Another crucial step in order to ensure near-optimal regret lies in careful designs of the data-driven bonus terms $\{{b_{h}{(s,a)}}\}$ in (18a). Here, we adopt the monotonic Bernstein-style bonus function for $\mathtt{M}\mathtt{V}\mathtt{P}$ originally proposed in zhang2020reinforcement, to be made precise. Compared to the bonus function in $\mathtt{E}\mathtt{u}\mathtt{l}\mathtt{e}\mathtt{r}$ (zanette2019tighter) and $\mathtt{U}\mathtt{C}\mathtt{B}\mathtt{V}\mathtt{I}$ (azar2017minimax), the monotonic bonus form has a cleaner structure that effectively avoids large lower-order terms. Note that in order to enable variance-aware regret, we also need to keep track of the empirical variance of the (stochastic) immediate rewards.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Remark 1", "weight": 1.0} -->

We note that a doubling update rule has also been used in the original $\mathtt{M}\mathtt{V}\mathtt{P}$ (zhang2020reinforcement). A subtle difference between our modified version and the original one lies in that: when the visitation count for some $(s,a,h)$ reaches $2^{i}$ for some integer $i \geq 1$, we only use the second half of the samples (i.e., the ${\{{2^{i - 1} + l}\}}_{l = 1}^{2^{i - 1}}$-th samples) to compute the empirical model, whereas the original $\mathtt{M}\mathtt{V}\mathtt{P}$ makes use of all the $2^{i}$ samples. This modified step turns out to be helpful in our analysis, while still preserving sample efficiency in an orderwise sense (since the latest batch always contains at least half of the samples).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Key technical innovations", "weight": 1.0} -->

In this section, we point out the key technical hurdles the previous approach encounters when mitigating the burn-in cost, and put forward a new strategy to overcome such hurdles. For ease of presentation, let us introduce a set of augmented notation to indicate several running iterates in Algorithm 1, which makes clear the dependency on the episode number $k$ and will be used throughout all of our analysis. ${\hat{P}}_{s,a,h}^{k} \in {\mathbb{R}}^{S}$: the latest update of the empirical transition probability vector ${\hat{P}}_{s,a,h}$ before the $k$-th episode. ${{\hat{r}}_{h}^{k}{(s,a)}} \in {\lbrack 0,H\rbrack}$: the latest update of the empirical reward ${\hat{r}}_{h}{(s,a)}$ before the $k$-th episode.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Key technical innovations", "weight": 1.0} -->

Another notation for the empirical transition probability vector is also introduced below: For any $j \geq 2$ (resp. $j = 1$), let ${\hat{P}}_{s,a,h}^{(j)}$ be the empirical transition probability vector for $(s,a,h)$ computed using the $j$-th batch of data, i.e., the ${\{{2^{j - 2} + i}\}}_{i = 1}^{2^{j - 2}}$-th samples (resp. the 1st sample) for $(s,a,h)$. For completeness, we take ${\hat{P}}_{s,a,h}^{} = {\frac{1}{S}1}$ for the $0$-th batch.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Key technical innovations", "weight": 1.0} -->

Similarly, let ${\hat{r}}_{h}^{(j)}{(s,a)}$ (resp. ${\hat{\sigma}}_{h}^{(j)}{(s,a)}$) denote the empirical reward (resp. empirical squared reward) w.r.t. $(s,a,h)$ based on the $j$-th batch of data.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Technical barriers in prior theory for $\\mathtt{U}\\mathtt{C}\\mathtt{B}\\mathtt{V}\\mathtt{I}$", "weight": 1.0} -->

Let us take a close inspection on prior regret analysis for UCB-based model-based algorithms, in order to illuminate the part that calls for novel analysis. To simplify presentation, this subsection assumes deterministic rewards so that each empirical reward is replaced by its mean.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Technical barriers in prior theory for $\\mathtt{U}\\mathtt{C}\\mathtt{B}\\mathtt{V}\\mathtt{I}$", "weight": 1.0} -->

Let us look at the original $\mathtt{U}\mathtt{C}\mathtt{B}\mathtt{V}\mathtt{I}$ algorithm proposed by azar2017minimax. Standard decomposition arguments employed in the literature (e.g., jaksch2010near; azar2017minimax; zhang2020reinforcement) decompose the regret as follows: see also the derivation in Section 5. Here, we abuse the notation by letting $V_{h + 1}^{k}$ (resp. $b_{h}^{k}$) be the value function estimate (resp.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Technical barriers in prior theory for $\\mathtt{U}\\mathtt{C}\\mathtt{B}\\mathtt{V}\\mathtt{I}$", "weight": 1.0} -->

bonus term) of $\mathtt{U}\mathtt{C}\mathtt{B}\mathtt{V}\mathtt{I}$ before the $k$-th episode, and in the meantime, we let ${\hat{P}}_{s,a,h}^{k,{\mathsf{a}\mathsf{l}\mathsf{l}}}$ represent the empirical transition probability for the ($s,a,h$)-tuple computed using all samples before the $k$-th episode (note that we add the superscript $\mathsf{a}\mathsf{l}\mathsf{l}$ to differentiate it from its counterpart in our algorithm). In order to achieve full-range optimal regret, one needs to bound the three terms on the right-hand side of carefully, among which two are easy to handle.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Technical barriers in prior theory for $\\mathtt{U}\\mathtt{C}\\mathtt{B}\\mathtt{V}\\mathtt{I}$", "weight": 1.0} -->

It is known that the second term (i.e., the aggregate bonus) on the right-hand side of can be controlled in a rate-optimal manner if we adopt suitably chosen Bernstein-style bonus; see, e.g., zhang2020reinforcement, which will also be made clear shortly in Section 5.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Technical barriers in prior theory for $\\mathtt{U}\\mathtt{C}\\mathtt{B}\\mathtt{V}\\mathtt{I}$", "weight": 1.0} -->

In the meantime, the third term on the right-hand side of can be easily coped with by means of standard martingale concentration bounds (e.g., the Freedman inequality).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Technical barriers in prior theory for $\\mathtt{U}\\mathtt{C}\\mathtt{B}\\mathtt{V}\\mathtt{I}$", "weight": 1.0} -->

It then comes down to controlling the first term on the right-hand side of. This turns out to be the most challenging part, owing to the complicated statistical dependency between ${\hat{P}}_{s_{h}^{k},a_{h}^{k},h}^{k,{\mathsf{a}\mathsf{l}\mathsf{l}}}$ and $V_{h + 1}^{k}$. To see this, note that ${\hat{P}}_{s,a,h}^{k,{\mathsf{a}\mathsf{l}\mathsf{l}}}$ is constructed based on all previous samples of $(s,a,h)$, which has non-negligible influences upon $V_{h + 1}^{k}$ as $V_{h + 1}^{k}$ is computed based on previous samples. At least two strategies have been proposed to circumvent this technical difficulty, which we take a moment to discuss.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Technical barriers in prior theory for $\\mathtt{U}\\mathtt{C}\\mathtt{B}\\mathtt{V}\\mathtt{I}$", "weight": 1.0} -->

Strategy 1: replacing $V_{h + 1}^{k}$ with $V_{h + 1}^{\star}$ for large $k$. Most prior analysis for model-based algorithms (azar2017minimax; dann2017unifying; zanette2019tighter; zhang2020reinforcement) decomposes The rationale behind this decomposition is as follows: given that $V_{h + 1}^{\star}$ is fixed and independent from the data, the first term on the right-hand side of can be bounded easily using Freedman's inequality; the second term on the right-hand side of would vanish as $V_{h + 1}^{k}$ and $V_{h + 1}^{\star}$ become exceedingly close (which would happen as $k$ becomes large enough).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Technical barriers in prior theory for $\\mathtt{U}\\mathtt{C}\\mathtt{B}\\mathtt{V}\\mathtt{I}$", "weight": 1.0} -->

Such arguments, however, fall short of tightness when analyzing the initial stage of the learning process: given that $V_{h + 1}^{k} - V_{h + 1}^{\star}$ cannot be sufficiently small at the beginning, this approach necessarily results in a huge burn-in cost.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Our approach", "weight": 1.0} -->

In light of the covering-based argument in Section 4.1, one can only hope this analysis strategy to work if substantial compression (i.e., a significantly reduced covering number) of the visitation counts is plausible. This motivates our introduction of the doubling batches as described in Section 3, so that for each $(s,a,h)$-tuple, the empirical model ${\hat{P}}_{s,a,h}$ and its associated visitation count $N_{h}{(s,a)}$ (for the associated batch) are updated at most $\log_{2}K$ times (see line 1 of Algorithm 1). Compared to the original $\mathtt{U}\mathtt{C}\mathtt{B}\mathtt{V}\mathtt{I}$ that recomputes the transition model in every episode, our algorithm allows for significant reduction of the covering number of the visitation counts, thanks to its much less frequent updates.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Our approach", "weight": 1.0} -->

Similar to, we are in need of bounding the following term when analyzing Algorithm 1: In what follows, we present our key ideas that enable tight analysis of this quantity, which constitute our main technical innovations. The complete regret analysis for Algorithm 1 is postponed to Section 5.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Key concept: profiles", "weight": 1.0} -->

One of the most important concepts underlying our analysis for Algorithm 1 is the so-called "profile", defined below.

<!-- chunk {"id": "body-0067", "role": "body", "section": "An expanded view of randomness w.r.t. state transitions", "weight": 1.0} -->

To facilitate analysis, we find it helpful to look at a different yet closely related way to generate independent samples from a generative model.

<!-- chunk {"id": "body-0068", "role": "body", "section": "A starting point: a basic decomposition", "weight": 1.0} -->

We now describe our approach to tackling the complicated statistical dependency between ${\hat{P}}_{s,a,h}^{k}$ and $V_{h + 1}^{k}$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "A starting point: a basic decomposition", "weight": 1.0} -->

the true visitation counts in the online learning process, $k_{l,j,s,a,h}$ denotes the episode index of the sample that visits $(s,a,h)$ for the $({2^{l - 1} + j})$-th time in the online learning process, and we take $V_{h + 1}^{k} = 0$ for any $k > K$. Here, the third line makes use of the fact that $0 \leq {V_{h + 1}^{k}{(s)}} \leq H$ for all $s \in \mathcal{S}$. The decomposition motivates us to first control the term $\sum_{s,a,h}\left\langle {{\hat{P}}_{s,a,h}^{(l)} - P_{s,a,h}},V_{h + 1}^{k_{l,j,s,a,h}} \right\rangle$, leading to the following 3-step analysis strategy.

<!-- chunk {"id": "body-0070", "role": "body", "section": "A starting point: a basic decomposition", "weight": 1.0} -->

For any given total profile $\mathcal{I} \in \mathcal{C}$ and any fixed $1 \leq l \leq {\log_{2}K}$, develop a high-probability bound on a weighted sum taking the following form where each vector $X_{{h + 1},s,a}$ is any deterministic function of $\mathcal{I}$ and the samples collected for steps $h' \geq {h + 1}$. Given the statistical independence between ${\hat{P}}_{s,a,h}^{(l)}$ and those samples for steps $h' \geq {h + 1}$ (in the view of $\mathcal{D}^{\mathsf{e}\mathsf{x}\mathsf{p}\mathsf{a}\mathsf{n}\mathsf{d}}$), we can bound (28 ‣ A starting point: a basic decomposition.

<!-- chunk {"id": "body-0071", "role": "body", "section": "A starting point: a basic decomposition", "weight": 1.0} -->

‣ 4.2.2 Decoupling the statistical dependency ‣ 4.2 Our approach ‣ 4 Key technical innovations ‣ Settling the Sample Complexity of Online Reinforcement Learning")) using standard martingale concentration inequalities.

<!-- chunk {"id": "body-0072", "role": "body", "section": "A starting point: a basic decomposition", "weight": 1.0} -->

Take the union bound over all possible $\mathcal{I} \in \mathcal{C}$ --- with the aid of Lemma 5 --- to obtain a uniform control of the term (28 ‣ A starting point: a basic decomposition. ‣ 4.2.2 Decoupling the statistical dependency ‣ 4.2 Our approach ‣ 4 Key technical innovations ‣ Settling the Sample Complexity of Online Reinforcement Learning")), simultaneously accounting for all $\mathcal{I} \in \mathcal{C}$ and all associated sequences $\{ X_{{h + 1},s,a}\}$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "A starting point: a basic decomposition", "weight": 1.0} -->

We then demonstrate that the above uniform bounds can be applied to the decomposition to obtain a desired bound.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Main steps", "weight": 1.0} -->

We now carry out the above three steps.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Main steps", "weight": 1.0} -->

Steps 1) and 2). Let us first specify the types of vectors $\{ X_{h,s,a}\}$ mentioned above in (28 ‣ A starting point: a basic decomposition. ‣ 4.2.2 Decoupling the statistical dependency ‣ 4.2 Our approach ‣ 4 Key technical innovations ‣ Settling the Sample Complexity of Online Reinforcement Learning")).

<!-- chunk {"id": "body-0076", "role": "body", "section": "Main steps", "weight": 1.0} -->

Given such a construction of $\left\{ \mathcal{X}_{h,\mathcal{I}} \right\}$, we can readily conduct Steps 1) and 2), with a uniform concentration bound stated below.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Step 1: the optimism principle", "weight": 1.0} -->

To begin, we justify that the running estimates of Q-function and value function in Algorithm 1 are always upper bounds on the optimal Q-function and the optimal value function, respectively, thereby guaranteeing optimism in the face of uncertainty.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Step 2: regret decomposition", "weight": 1.0} -->

In view of the optimism shown in Lemma 8. ‣ Step 1: the optimism principle. ‣ 5 Proof of Theorem 1 ‣ Settling the Sample Complexity of Online Reinforcement Learning"), the regret can be upper bounded by with probability at least $1 - {4SAHK\delta'}$. In order to control the right-hand side of, we first make note of the following upper bound on $V_{1}^{k}{(s_{1}^{k})}$.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Step 3.1: bounding the terms $T_{2},T_{3}$ and $T_{4}$", "weight": 1.0} -->

In this section, we seek to bound the terms $T_{2},T_{3}$ and $T_{4}$ defined in the regret decomposition. To do so, we find it helpful to first introduce the following quantities that capture some sort of aggregate variances: with $T_{5}$ denoting certain empirical variance and $T_{6}$ the true variance. With these quantities in place, we claim that the following bounds hold true.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Step 3.2: bounding the aggregate variances $T_{5}$ and $T_{6}$", "weight": 1.0} -->

The previous bounds on $T_{2}$ and $T_{3}$ stated in Lemma 10 depend respectively on the aggregate variance $T_{5}$ and $T_{6}$ (cf. (35a) and (35b)), which we would like to control now. By introducing the following quantities: we can upper bound $T_{5}$ and $T_{6}$ through the following lemma.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Step 3.3: bounding the terms $T_{1}$, $T_{7}$ and $T_{9}$", "weight": 1.0} -->

Taking a look at the above bounds on $T_{2},\ldots,T_{6}$, we see that one still needs to deal with the terms $T_{1}$, $T_{7}$ and $T_{9}$ (see, (37a) and (37c), respectively). As it turns out, these quantities have already been bounded in Section 4. Specifically, Lemma 7 tells us that: with probability at least $1 - \delta'$, where we recall that $B = {4000{({\log_{2}K})}^{3}{\log{({3SAH})}}{\log\frac{1}{\delta'}}}$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Step 4: putting all pieces together", "weight": 1.0} -->

To solve the inequalities, we resort to the elementary AM-GM inequality: if $a \leq {\sqrt{bc} + d}$ for some ${b,c} \geq 0$, then it follows that $a \leq {{\epsilon b} + {\frac{1}{2\epsilon}c} + d}$ for any $\epsilon > 0$. This basic inequality combined with gives which in turn result in By taking $\epsilon = {1/20}$, we arrive at where the last relation holds due to our assumption $K \geq {SAHB}$ (cf.). Substituting this into yields provided that $K \geq {SAHB}$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Step 4: putting all pieces together", "weight": 1.0} -->

These bounds taken collectively with readily give Combining the two scenarios (i.e., $K \geq {BSAH}$ and $K \leq {BSAH}$) reveals that with probability at least $1 - {100SAH^{2}K^{2}\delta'}$, The proof of Theorem 1 is thus completed by recalling that $\delta' = \frac{\delta}{200SAH^{2}K^{2}}$.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Extensions", "weight": 1.0} -->

In this section, we develop more refined regret bounds for Algorithm 1 in order to reflect the role of several problem-dependent quantities. Detailed proofs are postponed to Appendix D ‣ Settling the Sample Complexity of Online Reinforcement Learning") and Appendix F ‣ Settling the Sample Complexity of Online Reinforcement Learning").

<!-- chunk {"id": "body-0085", "role": "body", "section": "Value-based regret bounds", "weight": 1.0} -->

Thus far, we have not yet introduced the crucial quantity $v^{\star}$ in Theorem 2. ‣ 1.2.2 Extension: optimal problem-dependent regret bounds ‣ 1.2 A peek at our main contributions ‣ 1 Introduction ‣ Settling the Sample Complexity of Online Reinforcement Learning"), which we define now. When the initial states are drawn from $\mu$, we define $v^{\star}$ to be the weighted optimal value: Encouragingly, the value-dependent regret bound we develop in Theorem 2. ‣ 1.2.2 Extension: optimal problem-dependent regret bounds ‣ 1.2 A peek at our main contributions ‣ 1 Introduction ‣ Settling the Sample Complexity of Online Reinforcement Learning") is still minimax-optimal, as asserted by the following lower bound.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Cost-based regret bounds", "weight": 1.0} -->

Next, we turn to the cost-aware regret bound as in Theorem 3. ‣ 1.2.2 Extension: optimal problem-dependent regret bounds ‣ 1.2 A peek at our main contributions ‣ 1 Introduction ‣ Settling the Sample Complexity of Online Reinforcement Learning"). Note that all other results except for Theorem 3. ‣ 1.2.2 Extension: optimal problem-dependent regret bounds ‣ 1.2 A peek at our main contributions ‣ 1 Introduction ‣ Settling the Sample Complexity of Online Reinforcement Learning") (and a lower bound in this subsection) are about rewards as opposed to cost. In order to facilitate discussion, let us first formally formulate the cost-based scenarios.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Cost-based regret bounds", "weight": 1.0} -->

Suppose that the reward distributions ${\{ R_{h,s,a}\}}_{(s,a,h)}$ are replaced with the cost distributions ${\{ C_{h,s,a}\}}_{(s,a,h)}$, where each distribution $C_{h,s,a} \in {\Delta{({\lbrack 0,H\rbrack})}}$ has mean $c_{h}{(s,a)}$. In the $h$-th step of an episode, the learner pays an immediate cost $c_{h} \sim C_{h,s_{h},a_{h}}$ instead of receiving an immediate reward $r_{h}$, and the objective of the learner is instead to minimize the total cost $\sum_{h = 1}^{H}c_{h}$ (in an expected sense).

<!-- chunk {"id": "body-0088", "role": "body", "section": "Cost-based regret bounds", "weight": 1.0} -->

The optimal cost quantity $c^{\star}$ is then defined as In this cost-based setting, we find it convenient to re-define the $Q$-function and value function as follows: where we adopt different fonts to differentiate them from the original Q-function and value function. The optimal cost function is then define by Given the definitions above, we overload the notation ${\mathsf{R}\mathsf{e}\mathsf{g}\mathsf{r}\mathsf{e}\mathsf{t}}{(K)}$ to denote the regret for the cost-based scenario as One can also simply regard the cost minimization problem as reward maximization with negative rewards by choosing $r_{h} = {- c_{h}}$. This way allows us to apply Algorithm 1 directly, except that is replaced by Note that the proof of Theorem 3. ‣ 1.2.2 Extension: optimal problem-dependent regret bounds ‣ 1.2 A peek at our main contributions ‣ 1 Introduction ‣ Settling the Sample Complexity of Online Reinforcement Learning") closely resembles that of Theorem 2.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Cost-based regret bounds", "weight": 1.0} -->

‣ 1.2.2 Extension: optimal problem-dependent regret bounds ‣ 1.2 A peek at our main contributions ‣ 1 Introduction ‣ Settling the Sample Complexity of Online Reinforcement Learning"), which can be found in Appendix E ‣ Settling the Sample Complexity of Online Reinforcement Learning").

<!-- chunk {"id": "body-0090", "role": "body", "section": "Cost-based regret bounds", "weight": 1.0} -->

To confirm the tightness of Theorem 3. ‣ 1.2.2 Extension: optimal problem-dependent regret bounds ‣ 1.2 A peek at our main contributions ‣ 1 Introduction ‣ Settling the Sample Complexity of Online Reinforcement Learning"), we develop the following matching lower bound, which resorts to a similar hard instance as in the proof of Theorem 12.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Variance-dependent regret bound", "weight": 1.0} -->

The final regret bound presented in Theorem 4. ‣ 1.2.2 Extension: optimal problem-dependent regret bounds ‣ 1.2 A peek at our main contributions ‣ 1 Introduction ‣ Settling the Sample Complexity of Online Reinforcement Learning") depends on some sort of variance metrics. Towards this end, let us first make precise the variance metrics of interest: The first variance metric is defined as where ${\{{(s_{h},a_{h})}\}}_{1 \leq h \leq H}$ represents a sample trajectory under policy $\pi$. This captures the maximal possible expected sum of variance with respect to the optimal value function ${\{ V_{h}^{\star}\}}_{h = 1}^{H}$.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Variance-dependent regret bound", "weight": 1.0} -->

Another useful variance metric is defined as where ${\{ r_{h}\}}_{1 \leq h \leq H}$ denotes a sample sequence of immediate rewards under policy $\pi$. This indicates the maximal possible variance of the accumulative reward.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Variance-dependent regret bound", "weight": 1.0} -->

The interested reader is referred to zhou2023sharp for further discussion about these two metrics. Our final variance metric is then defined as With the above variance metrics in mind, we can then revisit Theorem 4. ‣ 1.2.2 Extension: optimal problem-dependent regret bounds ‣ 1.2 A peek at our main contributions ‣ 1 Introduction ‣ Settling the Sample Complexity of Online Reinforcement Learning"). As a special case, when the transition model is fully deterministic, the regret bound in Theorem 4. ‣ 1.2.2 Extension: optimal problem-dependent regret bounds ‣ 1.2 A peek at our main contributions ‣ 1 Introduction ‣ Settling the Sample Complexity of Online Reinforcement Learning") simplifies to for any $K \geq 1$, which is roughly the cost of visiting each state-action pair. The full proof of Theorem 4. ‣ 1.2.2 Extension: optimal problem-dependent regret bounds ‣ 1.2 A peek at our main contributions ‣ 1 Introduction ‣ Settling the Sample Complexity of Online Reinforcement Learning") is postponed to Appenndix F ‣ Settling the Sample Complexity of Online Reinforcement Learning").

<!-- chunk {"id": "body-0094", "role": "body", "section": "Variance-dependent regret bound", "weight": 1.0} -->

To finish up, let us develop a matching lower bound to corroborate the tightness and optimality of Theorem 4. ‣ 1.2.2 Extension: optimal problem-dependent regret bounds ‣ 1.2 A peek at our main contributions ‣ 1 Introduction ‣ Settling the Sample Complexity of Online Reinforcement Learning").

<!-- chunk {"id": "body-0095", "role": "body", "section": "Discussion", "weight": 1.5} -->

Focusing on tabular online RL in time-inhomogeneous finite-horizon MDPs, this paper has established the minimax-optimal regret (resp. sample complexity) --- up to log factors --- for the entire range of sample size $K \geq 1$ (resp. target accuracy level $\varepsilon \in {(0,H\rbrack}$), thereby fully settling an open problem at the core of recent RL theory. The $\mathtt{M}\mathtt{V}\mathtt{P}$ algorithm studied herein is model-based in nature. Remarkably, the model-based approach remains the only family of algorithms that is capable of obtaining minimax optimality without burn-ins, regardless of the data collection mechanism in use (e.g., online RL, offline RL, and the simulator setting). We have further unlocked the optimality of this algorithm in a more refined manner, making apparent the effect of several problem-dependent quantities (e.g., optimal value/cost, variance statistics) upon the fundamental performance limits.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Discussion", "weight": 1.5} -->

The new analysis and algorithmic techniques put forward herein might shed important light on how to conquer other RL settings as well.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Discussion", "weight": 1.5} -->

Moving forward, there are multiple directions that anticipate further theoretical pursuit. To begin, is it possible to develop a model-free algorithm --- which often exhibits more favorable memory complexity compared to the model-based counterpart --- that achieves full-range minimax optimality? As alluded to previously, existing paradigms that rely on reference-advantage decomposition (or variance reduction) seem to incur a high burn-in cost (zhang2020almost; li2021breaking), thus calling for new ideas to overcome this barrier. Additionally, multiple other tabular settings (e.g., time-homogeneous finite-horizon MDPs, discounted infinite-horizon MDPs) have also suffered from similar issues regarding the burn-in requirements (zhang2020reinforcement; ji2023regret). Take time-homogeneous finite-horizon MDPs for example: in order to achieve optimal sample efficiency, one needs to carefully deal with the statistical dependency incurred by aggregating data from across different time steps to estimate the same transition matrix (due to the homogeneous nature of $P$), which results in more intricate issues than the time-homogeneous counterpart.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Discussion", "weight": 1.5} -->

We believe that resolving these two open problems will greatly enhance our theoretical understanding about online RL and beyond.
