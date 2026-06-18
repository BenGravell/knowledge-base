<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity

Topics include Reinforcement learning, Multi-agent systems, Sample complexity, Planning, Learning, Model-based reinforcement learning, Multi-agent reinforcement learning, Nash equilibrium, Neuroevolution, Generative model, State space.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Model-based reinforcement learning (RL), which finds an optimal policy using an empirical model, has long been recognized as one of the corner stones of RL. It is especially suitable for multi-agent RL (MARL), as it naturally decouples the learning and the planning phases, and avoids the non-stationarity problem when all agents are improving their policies simultaneously using samples. Though intuitive and widely-used, the sample complexity of model-based MARL algorithms has not been fully investigated. In this paper, our goal is to address the fundamental question about its sample complexity. We study arguably the most basic MARL setting: two-player discounted zero-sum Markov games, given only access to a generative model. We show that model-based MARL achieves a sample complexity of tilde O(|S||A||B|(1-gamma)^(-3)epsilon^(-2)) for finding the Nash equilibrium (NE) value up to some epsilon error, and the epsilon-NE policies with a smooth planning oracle, where gamma is the discount factor, and S,A,B denote the state space, and the action spaces for the two agents.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We further show that such a sample bound is minimax-optimal (up to logarithmic factors) if the algorithm is reward-agnostic, where the algorithm queries state transition samples without reward knowledge, by establishing a matching lower bound. This is in contrast to the usual reward-aware setting, with a tildeOmega(|S|(|A|+|B|)(1-gamma)^(-3)epsilon^(-2)) lower bound, where this model-based approach is near-optimal with only a gap on the |A|,|B| dependence. Our results not only demonstrate the sample-efficiency of this basic model-based approach in MARL, but also elaborate on the fundamental tradeoff between its power (easily handling the more challenging reward-agnostic case) and limitation (less adaptive and suboptimal in |A|,|B|), particularly arises in the multi-agent context.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent years have witnessed numerous successes of reinforcement learning (RL) in many applications, e.g., playing strategy games, playing the game of Go, autonomous driving, and security. Most of these successful applications involve more than one decision-maker, giving birth to the surging interests and efforts in studying multi-agent RL (MARL) recently, especially on the theoretical side. See also comprehensive surveys on MARL in Busoniu et al.; Zhang et al.; Nguyen et al..

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In general MARL, all agents affect both the state transition and the rewards of each other, while each agent may possess different, sometimes even totally conflicting objectives. Without knowledge of the model, the agents have to resort to data to either estimate the model, improve their own policy, and/or infer other agents' policies. One fundamental challenge in MARL is the emergence of *non-stationarity* during the learning process: when multiple agents improve their policies concurrently and directly using samples, the environment becomes non-stationary from each agent's perspective. This has posed great challenge to development of effective MARL algorithms based on single-agent ones, especially *model-free* ones, as the condition for guaranteeing convergence in the latter fails to hold in MARL. One tempting remedy for this non-stationarity issue is the simple while intuitive method --- model-based^11^1Note that we here follow the convention of model-based approach in the generative model setting, which separates these two stages explicitly. In general, model-based RL approaches do not have to separate the two stages, see e.g., Bayesian RL, and model-based RL in online exploration settings.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

MARL: one first estimates an empirical model using data, and then finds the optimal, more specifically, equilibrium policies in this empirical model, via planning. Model-based MARL naturally decouples the *learning* and *planning* phases, and can be incorporated with *any* black-box planning algorithm that is efficient, e.g., value iteration and (generalized) policy iteration. More importantly, after estimating the model, this approach can potentially handle *more than one* MARL tasks with different reward functions but a common transition model, without re-sampling the data. Being able to handle this *reward-agnostic* case greatly expands the power of such a model-based approach.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Though intuitive and widely-used, rigorous theoretical justifications for these model-based MARL methods are relatively rare. In this work, our goal is to answer the following standing question: how good is the performance of this naïve "plug-in" method in terms of non-asymptotic sample complexity? To this end, we focus on arguably the most basic MARL setting since Littman: two-player discounted zero-sum Markov games (MGs) with simultaneous-move agents, given only access to a generative model. This generative model allows agents to sample the MG, and query the next state from the transition process, given any state-action pair as input. The generative model setting has been a benchmark in RL when studying the sample efficiency of algorithms. Indeed, this model allows for the study of sample-based multi-agent planning over a long horizon, and helps develop better understanding of the statistical properties of the algorithms, decoupled from the exploration complexity.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by recent minimax optimal complexity results for single-agent model-based RL, we address the question above with a positive answer: the model-based MARL approach can achieve near-minimax optimal sample complexity --- in terms of dependencies on the size of the state space, the horizon, and the desired accuracy --- for finding both the Nash equilibrium (NE) value and the NE policies. We also provide a separation in the achievable sample complexity, unique to the multi-agent setting, where, with regards to the dependencies on the number of actions, the naïve model-based approach is sub-optimal. A detailed description is provided next.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contributions", "weight": 1.0} -->

We establish the sample complexities of model-based MARL in zero-sum discounted Markov games, when a generative model is available. First, observing that the sampling process in this setting is agnostic to the reward function, we distinguish between two algorithmic frameworks: *reward-aware* and *reward-agnostic* cases, depending on whether the reward is revealed *before* or *after* the sampling. The model-based approach can inherently handle both cases, especially the latter case with multiple reward functions, without re-sampling the data. Second, by establishing lower bounds for both cases, we show that there is indeed a separation in sample complexity, which is unique in the multi-agent setting. Third, we show that up to some logarithmic factors, the model-based approach is indeed minimax optimal in all parameters in the more challenging reward-agnostic case, and has only a gap on the ${|\mathcal{A}|},{|\mathcal{B}|}$ (both agents' action space size) dependence in the reward-aware case.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contributions", "weight": 1.0} -->

This separation and the (near-)minimax results have not only justified the sample efficiency of this simple approach, but also highlighted both its power (easily handling multiple reward functions known in hindsight) and its limitation (less adaptive and can hardly achieve optimal complexity with reward knowledge), particularly arising in the multi-agent RL context. These results are first-of-their-kind in model-based MARL, and among the first (near-)minimax results in general MARL, to the best of our knowledge. We also believe that this separation may shed some light on the choice of model-free and model-based approaches in various MARL scenarios in practice, and provide new understandings for algorithm-design in other MARL settings, e.g., with no generative model, and going beyond two-player zero-sum MGs.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Zero-Sum Markov Games", "weight": 1.0} -->

Consider a zero-sum MG^33^3We will hereafter refer to this model simply as a *MG*.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Zero-Sum Markov Games", "weight": 1.0} -->

$\mathcal{G}$ characterized by $(\mathcal{S},\mathcal{A},\mathcal{B},P,r,\gamma)$, where $\mathcal{S}$ is the state space; $\mathcal{A},\mathcal{B}$ are the action spaces of agents $1$ and $2$, respectively; $P:{{\mathcal{S} \times \mathcal{A} \times \mathcal{B}}\rightarrow{\Delta{(\mathcal{S})}}}$ denotes the transition probability of states; $r:{{\mathcal{S} \times \mathcal{A} \times \mathcal{B}}\rightarrow{\lbrack 0,1\rbrack}}$ denotes the reward function^44^4Our results can be generalized to other ranges of reward function by a standard reduction, see e.g., Sidford et al., and randomized reward functions.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Zero-Sum Markov Games", "weight": 1.0} -->

of agent $1$ (thus $- r$ is the bounded reward function of agent $2$); and $\gamma \in {\lbrack 0,1)}$ is the discount factor. The goal of agent $1$ (agent $2$) is to maximize (minimize) the long-term accumulative discounted reward. In MARL, the agents aim to achieve this goal using data samples collected from the model.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Zero-Sum Markov Games", "weight": 1.0} -->

As in the MDP model, one can define the *state-value function* under a pair of joint policies $(\mu,\nu)$ as

<!-- chunk {"id": "body-0015", "role": "body", "section": "Zero-Sum Markov Games", "weight": 1.0} -->

Note that ${V^{\mu,\nu}{(s)}} \in {\lbrack 0,{1/{({1 - \gamma})}}\rbrack}$ for any $s \in \mathcal{S}$ as $r \in {\lbrack 0,1\rbrack}$, and the expectation is taken over the random trajectory produced by the joint policy $(\mu,\nu)$. Also, the *state-action/Q-value function* under $(\mu,\nu)$ is defined by

<!-- chunk {"id": "body-0016", "role": "body", "section": "Zero-Sum Markov Games", "weight": 1.0} -->

The solution concept considered is the (approximate) *Nash equilibrium*, as defined below.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Reward-Aware v.s. Reward-Agnostic", "weight": 1.0} -->

We first differentiate between two algorithmic mechanisms in the generative-model setting. In the reward-aware case, the reward function is either known to the agents, or can at least be estimated from data. The reward knowledge can thus be used to potentially guide the sampling process, making the algorithm *adaptive*. In the reward-agnostic case, reward knowledge is not used to guide sampling, and is possibly only revealed after the sampling. This especially fits in the scenario when there is more than one reward function of interest, or when the reward function is engineered iteratively, since it can now handle a class of reward functions that are not pre-specified, without re-sampling the data for each of them. Existing works in single-agent settings have no such a separation, as the sample complexity of estimating the reward function is typically of lower order, and the reward function is thus assumed to be known. In particular, the model-based approaches in Azar et al.; Agarwal et al.; Li et al. are reward-agnostic, while the model-free approaches in Sidford et al. are reward-aware.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Reward-Aware v.s. Reward-Agnostic", "weight": 1.0} -->

Interestingly, in two-agent Markov games, whether the reward is known beforehand or not may lead to different sample complexity lower-bounds, as we will see in §3.1. We thus point out this separation here for clarity.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 2 (Reward-Agnostic & Reward-Free)", "weight": 1.0} -->

The reward-agnostic case we advocate here is closely related to the recent novel algorithmic framework of *reward-free* RL, where there are also two phases, *exploration* and *planning*, while trajectories are only collected in the exploration phase, without any reward knowledge, and various reward functions are fed to the algorithm for evaluation in the planning phase. One key difference is that the reward-free setting aims to be effective for *all* reward function in the planning phase *simultaneously*, while the reward-agnostic setting only focuses on handling the underlying single-reward (or a few, e.g., polynomial number of, reward functions) that is not pre-specified. Being less general than the pure reward-free setting, the sample complexity bounds are thus possibly better, as we will show in §3.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Model-Based Approach with Generative Model", "weight": 1.0} -->

As a standard setting, suppose that we have access to a *generative model/sampler*, which can provide us with samples $s^{\prime} \sim P{( \cdot |s,a,b)}$ for any $(s,a,b)$. The model-based MARL algorithm simply calls the sampler $N$ times at each state-joint-action pair $(s,a,b)$, and constructs an empirical estimate of the transition model $P$, denoted by $\hat{P}$, following

<!-- chunk {"id": "body-0021", "role": "body", "section": "Model-Based Approach with Generative Model", "weight": 1.0} -->

Here $\text{count}{(s^{\prime},s,a,b)}$ is the number of times the state-action pair $(s,a,b)$ forces a transition to state $s^{\prime}$. Note that the reward function is not estimated, in either the reward-aware or reward-agnostic cases, as for the former, the sample complexity of estimating $r$ is only a lower order term, and $r$ is thus typically assumed to be known; while for the latter, no reward information is even available in the sampling processes. This model-based approach via estimating $P$ inherently handles both cases. Such a model-estimation can be implemented by both agents independently.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Planning Oracle", "weight": 1.0} -->

The reward function, together with the empirical transition model $\hat{P}$ and the components $(\mathcal{S},\mathcal{A},\mathcal{B},\gamma)$ in the true model $\mathcal{G}$, constitutes an empirical game model $\hat{\mathcal{G}}$. As in Azar et al.; Agarwal et al.; Jin et al.; Li et al. for single-agent RL, we assume that an efficient planning oracle is available, which takes $\hat{\mathcal{G}}$ as input, and outputs a policy pair $(\hat{\mu},\hat{\nu})$. This oracle decouples the statistical and computational aspects of the empirical model $\hat{\mathcal{G}}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Planning Oracle", "weight": 1.0} -->

The output policy pair, referred to as being *near-equilibrium*, is assumed to satisfy certain $\epsilon_{opt}$-order of equilibrium, in terms of value functions, and we evaluate the performance of $(\hat{\mu},\hat{\nu})$ on the original MG $\mathcal{G}$. Common planning algorithms include value iteration and (generalized) policy iteration, which are efficient in finding the ($\epsilon$-)NE of $\hat{\mathcal{G}}$. In addition, it is not hard to have an oracle that is smooth in generating policies, i.e., the change of the approximate NE policies can be bounded by the changes of the NE value. See our Definition 7 ‣ 3.3 Near-Optimality in Finding ϵ-NE Policy ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity") later for a formal statement. Finally, we note that our definition of model-based approach in the generative-model-setting follows from that, which separates these two stages explicitly.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Planning Oracle", "weight": 1.0} -->

In general, model-based RL approaches do not have to separate the two stages, see e.g., Bayesian RL, and model-based RL in online exploration settings.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Main Results", "weight": 1.0} -->

We now introduce the main results of this paper. For notational convenience, we use ${\hat{V}}^{\mu,\nu}$, ${\hat{V}}^{\mu, \ast}$, ${\hat{V}}^{\ast,\nu}$, and ${\hat{V}}^{\ast}$ to denote the value under $(\mu,\nu)$, the best-response value under $\mu$ and $\nu$, and the NE value, under the empirical game model $\hat{\mathcal{G}}$, respectively. A similar convention is also used for Q-functions.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Lower Bounds", "weight": 1.0} -->

We first establish lower bounds on both approximating the NE value function and learning the $\epsilon$-NE policy pair, in both reward-aware and reward-agnostic cases.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Near-Optimality in Finding $\\epsilon$-Approximate NE Value", "weight": 1.0} -->

We now establish the near-minimax optimal sample complexities of model-based MARL. Note that theses results apply to both reward-aware and reward-agnostic cases, as the implementation of our model-based approach does not rely on the reward function. We start by showing the sample complexity to achieve an $\epsilon$-approximate NE value.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Near-Optimality in Finding $\\epsilon$-NE Policy", "weight": 1.0} -->

Admittedly, Corollary 6 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity") does not fully exploit the *model-based* approach, since it finds the NE policy according to the Q-value estimate ${\hat{Q}}^{\hat{\mu},\hat{\nu}}$, instead of using the output policy pair $(\hat{\mu},\hat{\nu})$ directly. This loses a factor of $1 - \gamma$. To improve the sample complexity of obtaining the NE policies, we first introduce the following definition of a smooth Planning Oracle.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Proofs", "weight": 1.0} -->

We first introduce some additional notation for convenience.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Important Lemmas", "weight": 1.0} -->

We start with the component-wise error bounds.

<!-- chunk {"id": "body-0031", "role": "body", "section": "An Auxiliary Markov Game", "weight": 1.0} -->

Motivated by the *absorbing MDP* technique in Agarwal et al., we introduce an *absorbing Markov game*, in order to handle the interdependence between $\hat{P}$ and ${\hat{V}}^{\mu,\nu}$, for any $\mu,\nu$ (which may also depend on $\hat{P}$), which will show up frequently in the analysis.

<!-- chunk {"id": "body-0032", "role": "body", "section": "An Auxiliary Markov Game", "weight": 1.0} -->

We now define a new Markov game $\mathcal{G}_{s,u}$ as follows (with $s \in \mathcal{S}$ and $u \in {\mathbb{R}}$ a constant): $\mathcal{G}_{s,u}$ is identical to $\mathcal{G}$, except that ${P_{\mathcal{G}_{s,u}}{(\left. s \middle| {s,a,b} \right.)}} = 1$ for all ${(a,b)} \in {\mathcal{A} \times \mathcal{B}}$, namely, state $s$ is an *absorbing* state; and the instantaneous reward at $s$ is always ${({1 - \gamma})}u$. The rest of the reward function and the transition model of $\mathcal{G}_{s,u}$ are the same as those of $\mathcal{G}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "An Auxiliary Markov Game", "weight": 1.0} -->

For notational simplicity, we now use $X_{s,u}^{\mu,\nu}$ to denote $X_{\mathcal{G}_{s,u}}^{\mu,\nu}$, where $X$ can be either the value functions $Q$ and $V$, or the reward function $r$, under the model $\mathcal{G}_{s,u}$. Obviously, for any policy pair $(\mu,\nu)$, ${V_{s,u}^{\mu,\nu}{(s)}} = u$ for the absorbing state $s$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

In this paper, we have established the first (near-)minimax optimal sample complexity for model-based MARL, when a generative model is available. Our setting was focused on the basic model in MARL --- infinite-horizon discounted two-player zero-sum Markov games. By noticing that reward is not used in the sampling process of this model-based approach, we have separated the reward-aware and reward-agnostic cases, and established sample complexity lower bounds correspondingly, a unique separation in the multi-agent context. We have then shown that this simple model-based approach is near-minimax optimal in the reward-aware case, with only a gap in the dependence on ${|\mathcal{A}|},{|\mathcal{B}|}$; and is indeed minimax-optimal in the reward-agnostic case.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

This separation and the (near-)optimal results have not only justified the sample-efficiency of this simple approach, but also reflected both its power (easily handling multiple reward functions known in hindsight), and its limitation (less adaptive and can hardly achieve the optimal $\overset{\sim}{\mathcal{O}}{({{|\mathcal{A}|} + {|\mathcal{B}|}})}$). We believe that our results may shed light on the choice of model-free and model-based approaches in various MARL scenarios in practice.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

Our results naturally open up the following interesting future directions. First, besides the turn-based setting in Sidford et al. and the episodic setting in the concurrent work Bai et al., the minimax-optimal sample complexity in *all* parameters for *model-free* algorithms is still open. As discussed in §3, in the reward-aware case, the $\overset{\sim}{\Omega}{({{|\mathcal{A}|} + {|\mathcal{B}|}})}$ lower bound may only be attainable by model-free ones. It would be interesting to compare the results with our model-based ones, in both reward-aware and reward-agnostic cases, to better understand their pros and cons in various MARL settings. It would also be interesting to explore the (near-)optimal sample complexity or regret of model-based approaches in other MARL scenarios, such as when no generative model is available, episodic and average-reward settings, general-sum Markov games, and the setting with function approximation.
