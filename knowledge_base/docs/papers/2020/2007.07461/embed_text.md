## Introduction

Recent years have witnessed numerous successes of reinforcement learning (RL) in many applications, e.g., playing strategy games, playing the game of Go, autonomous driving, and security. Most of these successful applications involve more than one decision-maker, giving birth to the surging interests and efforts in studying multi-agent RL (MARL) recently, especially on the theoretical side. See also comprehensive surveys on MARL in Busoniu et al.; Zhang et al.; Nguyen et al..

In general MARL, all agents affect both the state transition and the rewards of each other, while each agent may possess different, sometimes even totally conflicting objectives. Without knowledge of the model, the agents have to resort to data to either estimate the model, improve their own policy, and/or infer other agents' policies. One fundamental challenge in MARL is the emergence of *non-stationarity* during the learning process: when multiple agents improve their policies concurrently and directly using samples, the environment becomes non-stationary from each agent's perspective. This has posed great challenge to development of effective MARL algorithms based on single-agent ones, especially *model-free* ones, as the condition for guaranteeing convergence in the latter fails to hold in MARL. One tempting remedy for this non-stationarity issue is the simple while intuitive method --- model-based^11^1Note that we here follow the convention of model-based approach in the generative model setting, which separates these two stages explicitly. In general, model-based RL approaches do not have to separate the two stages, see e.g., Bayesian RL, and model-based RL in online exploration settings. MARL: one first estimates an empirical model using data, and then finds the optimal, more specifically, equilibrium policies in this empirical model, via planning. Model-based MARL naturally decouples the *learning* and *planning* phases, and can be incorporated with *any* black-box planning algorithm that is efficient, e.g., value iteration and (generalized) policy iteration. More importantly, after estimating the model, this approach can potentially handle *more than one* MARL tasks with different reward functions but a common transition model, without re-sampling the data. Being able to handle this *reward-agnostic* case greatly expands the power of such a model-based approach.

Though intuitive and widely-used, rigorous theoretical justifications for these model-based MARL methods are relatively rare. In this work, our goal is to answer the following standing question: how good is the performance of this naïve "plug-in" method in terms of non-asymptotic sample complexity? To this end, we focus on arguably the most basic MARL setting since Littman: two-player discounted zero-sum Markov games (MGs) with simultaneous-move agents, given only access to a generative model. This generative model allows agents to sample the MG, and query the next state from the transition process, given any state-action pair as input. The generative model setting has been a benchmark in RL when studying the sample efficiency of algorithms. Indeed, this model allows for the study of sample-based multi-agent planning over a long horizon, and helps develop better understanding of the statistical properties of the algorithms, decoupled from the exploration complexity.

Motivated by recent minimax optimal complexity results for single-agent model-based RL, we address the question above with a positive answer: the model-based MARL approach can achieve near-minimax optimal sample complexity --- in terms of dependencies on the size of the state space, the horizon, and the desired accuracy --- for finding both the Nash equilibrium (NE) value and the NE policies. We also provide a separation in the achievable sample complexity, unique to the multi-agent setting, where, with regards to the dependencies on the number of actions, the naïve model-based approach is sub-optimal. A detailed description is provided next.

### Contributions

We establish the sample complexities of model-based MARL in zero-sum discounted Markov games, when a generative model is available. First, observing that the sampling process in this setting is agnostic to the reward function, we distinguish between two algorithmic frameworks: *reward-aware* and *reward-agnostic* cases, depending on whether the reward is revealed *before* or *after* the sampling. The model-based approach can inherently handle both cases, especially the latter case with multiple reward functions, without re-sampling the data. Second, by establishing lower bounds for both cases, we show that there is indeed a separation in sample complexity, which is unique in the multi-agent setting. Third, we show that up to some logarithmic factors, the model-based approach is indeed minimax optimal in all parameters in the more challenging reward-agnostic case, and has only a gap on the ${|\mathcal{A}|},{|\mathcal{B}|}$ (both agents' action space size) dependence in the reward-aware case. This separation and the (near-)minimax results have not only justified the sample efficiency of this simple approach, but also highlighted both its power (easily handling multiple reward functions known in hindsight) and its limitation (less adaptive and can hardly achieve optimal complexity with reward knowledge), particularly arising in the multi-agent RL context. These results are first-of-their-kind in model-based MARL, and among the first (near-)minimax results in general MARL, to the best of our knowledge. We also believe that this separation may shed some light on the choice of model-free and model-based approaches in various MARL scenarios in practice, and provide new understandings for algorithm-design in other MARL settings, e.g., with no generative model, and going beyond two-player zero-sum MGs.

### Related Work

Stemming from the formative work Littman, MARL has been mostly studied under the framework of Markov games. There has been no shortage of provably convergent MARL algorithms ever since then. However, most of these early results are Q-learning-based (thus model-free) and asymptotic, with no sample complexity guarantees. To establish *non-asymptotic* results, Pérolat et al.; Fan et al.; Zhang et al. have studied the sample complexity of *batch* model-free MARL methods. There are also increasing interests in policy-based (thus also model-free) methods for solving special MGs with non-asymptotic convergence guarantees. No result on the (near-)minimax optimality of these complexities has been established prior to the present work.

Specific to the two-player zero-sum setting, Jia et al. and Sidford et al. have considered *turn-based MGs*, a special case of the simultaneous-move MGs considered here, with a generative model. Specifically, Sidford et al. established near-optimal sample complexity of $\overset{\sim}{\mathcal{O}}{({{({1 - \gamma})}^{- 3}\epsilon^{- 2}})}$ for a variant of Q-learning for this setting. More recently, Bai and Jin; Xie et al. have established both regret and sample complexity guarantees for episodic zero-sum MGs, without a generative model, with focus on efficient exploration. The work in Shah et al. also focused on the turn-based setting, and combined Monte-Carlo Tree Search and supervised learning to find the NE values. In contrast, model-based MARL theory has relatively limited literature. Brafman and Tennenholtz proposed the R-MAX algorithm for average-reward MGs, with polynomial sample complexity. Wei et al. developed a model-based upper confidence algorithm with polynomial sample complexities for the same setting. These methods differ from ours, as they are either specific model-free approaches, or not clear yet if they are (near-)minimax optimal in the corresponding setups. Concurrent to our work, Bai et al. developed *model-free* algorithms with near-optimal sample complexities in episodic settings without a generative model. The results are optimal in ${|\mathcal{S}|},{|\mathcal{A}|},{|\mathcal{B}|}$ dependence, but not in the horizon $H$. Finally, we note that MARL in Markov games is not restricted to the competitive setting of two-player zero-sum, and the studies in (multi-player) cooperative/potential settings and general-sum settings also exist, and is not the focus of the present paper.

In the single-agent regime, there has been extensive literature on non-asymptotic efficiency of RL in MDPs; see Kearns and Singh; Kakade; Strehl et al.; Jaksch et al.; Azar et al.; Osband and Van Roy; Dann and Brunskill; Azar et al.; Wang; Sidford et al.; Jin et al.; Li et al.. Amongst them, we highlight the minimax optimal ones: Azar et al. and Azar et al. have provided minimax optimal results for sample complexity and regret in the settings with and without a generative model, respectively. Specifically, Azar et al. has shown that to achieve the $\epsilon$-optimal *value* in Markov decision processes (MDPs), at least $\overset{\sim}{\Omega}{({{|\mathcal{S}|}{|\mathcal{A}|}{({1 - \gamma})}^{- 3}\epsilon^{- 2}})}$ samples are needed, for $\epsilon \in {(0,1\rbrack}$. They also showed that to find an $\epsilon$-optimal *policy*, the same minimax complexity order in $1 - \gamma$ and $\epsilon$ can be attained, if $\epsilon \in {(0,{{({1 - \gamma})}^{- {1/2}}{|\mathcal{S}|}^{- {1/2}}}\rbrack}$ and the total sample complexity is $\overset{\sim}{\mathcal{O}}{({{|\mathcal{S}|}^{2}{|\mathcal{A}|}})}$, which is in fact *linear* in the model size. Later, Sidford et al. has proposed a Q-learning based approach to attain this lower bound and remove the extra dependence on $|\mathcal{S}|$, for $\epsilon \in {(0,1\rbrack}$. More recently, Agarwal et al. developed new techniques based on *absorbing MDPs*, to show that model-based RL also achieves the lower bound for finding an $\epsilon$-optimal *policy*, with a larger $\epsilon$ range of $(0,{({1 - \gamma})}^{- {1/2}}\rbrack$^22^2While preparing the present work, Li et al. has further improved the minimax optimal results in Agarwal et al., in that they cover the entire range of sample sizes. We believe the improvement can also be incorporated in the MARL setting here, which is left as our future work.. Finally, our separation of the reward-agnostic case is motivated by the recent novel framework of reward-free RL in Jin et al..

## Preliminaries

### Zero-Sum Markov Games

Consider a zero-sum MG^33^3We will hereafter refer to this model simply as a *MG*. $\mathcal{G}$ characterized by $(\mathcal{S},\mathcal{A},\mathcal{B},P,r,\gamma)$, where $\mathcal{S}$ is the state space; $\mathcal{A},\mathcal{B}$ are the action spaces of agents $1$ and $2$, respectively; $P:{{\mathcal{S} \times \mathcal{A} \times \mathcal{B}}\rightarrow{\Delta{(\mathcal{S})}}}$ denotes the transition probability of states; $r:{{\mathcal{S} \times \mathcal{A} \times \mathcal{B}}\rightarrow{\lbrack 0,1\rbrack}}$ denotes the reward function^44^4Our results can be generalized to other ranges of reward function by a standard reduction, see e.g., Sidford et al., and randomized reward functions. of agent $1$ (thus $- r$ is the bounded reward function of agent $2$); and $\gamma \in {\lbrack 0,1)}$ is the discount factor. The goal of agent $1$ (agent $2$) is to maximize (minimize) the long-term accumulative discounted reward. In MARL, the agents aim to achieve this goal using data samples collected from the model.

At each time $t$, agent $1$ (agent $2$) has a stationary (not necessarily deterministic) policy $\mu:{\mathcal{S}\rightarrow{\Delta{(\mathcal{A})}}}$ ($\nu:{\mathcal{S}\rightarrow{\Delta{(\mathcal{B})}}}$), where $\Delta{(\mathcal{X})}$ denotes the space of all probability measures over $\mathcal{X}$, so that $a_{t} \sim \mu{( \cdot |s_{t})}$ ($b_{t} \sim \nu{( \cdot |s_{t})}$). The state makes a transition from $s_{t}$ to $s_{t + 1}$ following the probability distribution $P{( \cdot |s_{t},a_{t},b_{t})}$, given $(a_{t},b_{t})$. As in the MDP model, one can define the *state-value function* under a pair of joint policies $(\mu,\nu)$ as

Note that ${V^{\mu,\nu}{(s)}} \in {\lbrack 0,{1/{({1 - \gamma})}}\rbrack}$ for any $s \in \mathcal{S}$ as $r \in {\lbrack 0,1\rbrack}$, and the expectation is taken over the random trajectory produced by the joint policy $(\mu,\nu)$. Also, the *state-action/Q-value function* under $(\mu,\nu)$ is defined by

The solution concept considered is the (approximate) *Nash equilibrium*, as defined below.

### Definition 1 (($\epsilon$-)Nash Equilibrium)

For a zero-sum MG $(\mathcal{S},\mathcal{A},\mathcal{B},P,r,\gamma)$, a *Nash equilibrium policy* pair $(\mu^{\ast},\nu^{\ast})$ satisfies the following pair of inequalities^55^5In game theory, this pair is commonly referred to as *saddle-point inequalities*. for any $s \in \mathcal{S}$, $\mu \in {\Delta{(\mathcal{A})}^{|\mathcal{S}|}}$, and $\nu \in {\Delta{(\mathcal{B})}^{|\mathcal{S}|}}$

If (1Nash Equilibrium) ‣ Zero-Sum Markov Games. ‣ 2 Preliminaries ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity")) holds with some $\epsilon > 0$ relaxation, i.e., for some policy $(\mu^{\prime},\nu^{\prime})$, such that

then $(\mu^{\prime},\nu^{\prime})$ is an *$\epsilon$-Nash equilibrium policy* pair.

By Shapley; Patek, there exists a Nash equilibrium policy pair ${(\mu^{\ast},\nu^{\ast})} \in {{{\Delta{(\mathcal{A})}^{|\mathcal{S}|}} \times \Delta}{(\mathcal{B})}^{|\mathcal{S}|}}$ for two-player discounted zero-sum MGs. The state-value $V^{\ast}:=V^{\mu^{\ast},\nu^{\ast}}$ is referred to as the *value of the game*. The corresponding Q-value function is denoted by $Q^{\ast}$. The objective of the two agents is to find the NE policy of the MG, namely, to solve the saddle-point problem

for every $s \in \mathcal{S}$, where the order of $\max$ and $\min$ can be interchanged. For notational convenience, for any policy $(\mu,\nu)$, we define

and denote the corresponding optimizers by $\nu{(\mu)}$ and $\mu{(\nu)}$, respectively. We refer to these values and optimizers as the *best-response* values and policies, given $\mu$ and $\nu$, respectively.

### Reward-Aware v.s. Reward-Agnostic

We first differentiate between two algorithmic mechanisms in the generative-model setting. In the reward-aware case, the reward function is either known to the agents, or can at least be estimated from data. The reward knowledge can thus be used to potentially guide the sampling process, making the algorithm *adaptive*. In the reward-agnostic case, reward knowledge is not used to guide sampling, and is possibly only revealed after the sampling. This especially fits in the scenario when there is more than one reward function of interest, or when the reward function is engineered iteratively, since it can now handle a class of reward functions that are not pre-specified, without re-sampling the data for each of them. Existing works in single-agent settings have no such a separation, as the sample complexity of estimating the reward function is typically of lower order, and the reward function is thus assumed to be known. In particular, the model-based approaches in Azar et al.; Agarwal et al.; Li et al. are reward-agnostic, while the model-free approaches in Sidford et al. are reward-aware. Interestingly, in two-agent Markov games, whether the reward is known beforehand or not may lead to different sample complexity lower-bounds, as we will see in §3.1. We thus point out this separation here for clarity.

### Remark 2 (Reward-Agnostic & Reward-Free)

The reward-agnostic case we advocate here is closely related to the recent novel algorithmic framework of *reward-free* RL, where there are also two phases, *exploration* and *planning*, while trajectories are only collected in the exploration phase, without any reward knowledge, and various reward functions are fed to the algorithm for evaluation in the planning phase. One key difference is that the reward-free setting aims to be effective for *all* reward function in the planning phase *simultaneously*, while the reward-agnostic setting only focuses on handling the underlying single-reward (or a few, e.g., polynomial number of, reward functions) that is not pre-specified. Being less general than the pure reward-free setting, the sample complexity bounds are thus possibly better, as we will show in §3.

### Model-Based Approach with Generative Model

As a standard setting, suppose that we have access to a *generative model/sampler*, which can provide us with samples $s^{\prime} \sim P{( \cdot |s,a,b)}$ for any $(s,a,b)$. The model-based MARL algorithm simply calls the sampler $N$ times at each state-joint-action pair $(s,a,b)$, and constructs an empirical estimate of the transition model $P$, denoted by $\hat{P}$, following

Here $\text{count}{(s^{\prime},s,a,b)}$ is the number of times the state-action pair $(s,a,b)$ forces a transition to state $s^{\prime}$. Note that the reward function is not estimated, in either the reward-aware or reward-agnostic cases, as for the former, the sample complexity of estimating $r$ is only a lower order term, and $r$ is thus typically assumed to be known; while for the latter, no reward information is even available in the sampling processes. This model-based approach via estimating $P$ inherently handles both cases. Such a model-estimation can be implemented by both agents independently.

### Planning Oracle

The reward function, together with the empirical transition model $\hat{P}$ and the components $(\mathcal{S},\mathcal{A},\mathcal{B},\gamma)$ in the true model $\mathcal{G}$, constitutes an empirical game model $\hat{\mathcal{G}}$. As in Azar et al.; Agarwal et al.; Jin et al.; Li et al. for single-agent RL, we assume that an efficient planning oracle is available, which takes $\hat{\mathcal{G}}$ as input, and outputs a policy pair $(\hat{\mu},\hat{\nu})$. This oracle decouples the statistical and computational aspects of the empirical model $\hat{\mathcal{G}}$. The output policy pair, referred to as being *near-equilibrium*, is assumed to satisfy certain $\epsilon_{opt}$-order of equilibrium, in terms of value functions, and we evaluate the performance of $(\hat{\mu},\hat{\nu})$ on the original MG $\mathcal{G}$. Common planning algorithms include value iteration and (generalized) policy iteration, which are efficient in finding the ($\epsilon$-)NE of $\hat{\mathcal{G}}$. In addition, it is not hard to have an oracle that is smooth in generating policies, i.e., the change of the approximate NE policies can be bounded by the changes of the NE value. See our Definition 7 ‣ 3.3 Near-Optimality in Finding ϵ-NE Policy ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity") later for a formal statement. Finally, we note that our definition of model-based approach in the generative-model-setting follows from that in, which separates these two stages explicitly. In general, model-based RL approaches do not have to separate the two stages, see e.g., Bayesian RL, and model-based RL in online exploration settings.

## Main Results

We now introduce the main results of this paper. For notational convenience, we use ${\hat{V}}^{\mu,\nu}$, ${\hat{V}}^{\mu, \ast}$, ${\hat{V}}^{\ast,\nu}$, and ${\hat{V}}^{\ast}$ to denote the value under $(\mu,\nu)$, the best-response value under $\mu$ and $\nu$, and the NE value, under the empirical game model $\hat{\mathcal{G}}$, respectively. A similar convention is also used for Q-functions.

### Lower Bounds

We first establish lower bounds on both approximating the NE value function and learning the $\epsilon$-NE policy pair, in both reward-aware and reward-agnostic cases.

### Lemma 3 (Lower Bound for Reward-Aware Case)

Let $\mathcal{G}$ be an unknown zero-sum MG, and the agents learn in a reward-aware case, i.e., the reward knowledge is available during sampling. Then, there exist ${\epsilon_{0},\delta_{0}} > 0$, such that for all $\epsilon \in {(0,\epsilon_{0})}$, $\delta \in {(0,\delta_{0})}$, the sample complexity of learning an $\epsilon$-NE policy pair, or an $\epsilon$-approximate NE value, i.e., finding a $\hat{Q}$ such that ${\|{\hat{Q} - Q^{\ast}}\|}_{\infty} \leq \epsilon$ for $\mathcal{G}$, with a generative model with probability at least $1 - \delta$, is ${\overset{\sim}{\Omega}\left( {{|\mathcal{S}|}{({{|\mathcal{A}|} + {|\mathcal{B}|}})}{({1 - \gamma})}^{- 3}\epsilon^{- 2}{\log{({1/\delta})}}} \right)}.$

The proof of Lemma 3 ‣ 3.1 Lower Bounds ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"), via a straightforward adaptation from the lower bounds for MDPs, is provided in §A.1. In particular, one can design a two-player zero-sum Markov game such that one of the players is dummy -- she has no control on the reward nor the transition dynamics. Then, the existing lower bound in Azar et al.; Feng et al. for MDPs leads to the desired result. Note that as in Azar et al.; Sidford et al.; Agarwal et al.; Li et al., the reward function is *known* in this case. As we will show momentarily, our sample complexity is tight in $1 - \gamma$ and $|\mathcal{S}|$, while has a gap in ${|\mathcal{A}|},{|\mathcal{B}|}$ dependence ($\overset{\sim}{\mathcal{O}}{({{|\mathcal{A}|}{|\mathcal{B}|}})}$ versus $\overset{\sim}{\Omega}{({{|\mathcal{A}|} + {|\mathcal{B}|}})}$). In §A.1, we discuss that the $\overset{\sim}{\Omega}{({{|\mathcal{A}|} + {|\mathcal{B}|}})}$ lower bound may not be improved in this reward-aware case, and might be attainable by *model-free* algorithms instead (as $\overset{\sim}{\mathcal{O}}{({{|\mathcal{A}|}{|\mathcal{B}|}})}$ is inherent in model-based approaches due to estimating $P$). Interestingly, in the concurrent work Bai et al., under a different MARL setting, such an $\overset{\sim}{\Omega}{({{|\mathcal{A}|} + {|\mathcal{B}|}})}$ complexity is indeed shown to be attainable by a model-free algorithm with *online* updates.

On the other hand, note that our model-based approach can inherently also handle the more challenging reward-agnostic case. Indeed, estimating the transition model $P$ seems a bit of an overkill for the reward-aware case, in terms of sample complexity. A natural two-part question then becomes: what is the sample complexity lower bound in this more challenging reward-agnostic case, and can the model-based approach attain it? We formally answer the first part of the question in the following theorem, whose proof is deferred to §A.2, and answer the second part in §3.2 and §3.3.

### Theorem 4 (Lower Bound for Reward-Agnostic Case)

Let $\mathcal{G}$ be an unknown zero-sum MG, and the agents learn in a reward-agnostic case, i.e., they first call the generative model for sampling, without reward knowledge, and then are fed with the reward function $r$ in $\mathcal{G}$, for finding either an $\epsilon$-NE policy pair, or an $\epsilon$-approximate NE value for $\mathcal{G}$. Then, there exist ${\epsilon_{0},\delta_{0}} > 0$, such that for all $\epsilon \in {(0,\epsilon_{0})}$, $\delta \in {(0,\delta_{0})}$, the sample complexity of achieving either goal with probability at least $1 - \delta$, is

Compared to Lemma 3 ‣ 3.1 Lower Bounds ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"), the dependence on ${|\mathcal{A}|},{|\mathcal{B}|}$ is increased from $\overset{\sim}{\Omega}{({{|\mathcal{A}|} + {|\mathcal{B}|}})}$ to $\overset{\sim}{\Omega}{({{|\mathcal{A}|}{|\mathcal{B}|}})}$. Several remarks are now in order. First, this suggests that without guidance from the reward, the reward-agnostic case can be more challenging to tackle. The intuition is that, when the reward is only given in hindsight, which might be chosen adversarially, costs the algorithm to at least sample at all ${|\mathcal{A}|}{|\mathcal{B}|}$ elements in the Q-value $Q{(s, \cdot, \cdot )}$ at each state $s$ often enough. Second, when reduced to the single-agent setting (e.g., with ${|\mathcal{B}|} = 1$), such a separation disappears, showing its unique emergence in the multi-agent setting, and explaining why these two cases were not differentiated explicitly in the single-agent literature. Third, this lower bound is also related to the reward-free setting with a single unknown reward (not infinitely many as in Jin et al. ).

The basic intuition regarding the separation between the lower bounds in reward-aware and reward-agnostic cases, when compared to the single-agent setting (where there is no such a separation), is the insensitivity of Nash equilibrium (NE) to the changes in payoff matrices in two-player zero-sum games. In particular, NE in general depends on the joint behavior and preferences of both agents. Specifically, to construct the lower bound (even in the single-agent case, see e.g., Azar et al.; Feng et al. ), we needed to carefully perturb the Q-value function at each state-action pair of some null hypothesis instance, so that the solution (which is the maximum in the single-agent case, and Nash equilibrium in the multi-agent case) is also changed in the perturbed alternative hypothesis cases. Hence, for each alternative hypothesis case, we need to change the NE by only changing $\mathcal{O}{}$ elements in the payoff matrix, i.e., the Q-value table. In the reward-aware setting, since the reward is known (or can be estimated accurately with negligible sample complexity), we can only perturb the transition matrix to perturb the Q-value table, which share the same size (i.e., the degree-of-freedom). Due to the insensitivity, we can hardly construct $\Theta{({{|\mathcal{A}|}{|\mathcal{B}|}})}$ different hard cases (as needed to construct a $\Omega{({{|\mathcal{A}|}{|\mathcal{B}|}})}$ lower bound) while by only perturbing $\mathcal{O}{}$ elements in the transition matrix in each case. Note that such a perturbation can be effective in the single-agent MDP setting, as by only perturbing one element in the transition matrix, the maximum of the Q-value can be changed, see e.g., Azar et al.; Feng et al..

In contrast, in the reward-agnostic setting, the reward information is given after the sampling phase and the estimation of the model. This way, more freedom is allowed to construct $\Theta{({{|\mathcal{A}|}{|\mathcal{B}|}})}$ different hard cases, by adversarially choosing the reward function afterwards. In particular, the Q-value will be affected by both the transition matrix and the reward, and with polynomial number of reward functions, we were able to construct Q-value tables in $\Theta{({{|\mathcal{A}|}{|\mathcal{B}|}})}$ different hard cases. Note that taking a union bound over the polynomial number of reward functions do not affect the total sample complexity, as it is still dominated by the sample complexity of estimating the transition matrix. In other words, the freedom of constructing and perturbing the reward functions adversarially afterwards forces the algorithm to estimate all the elements in the transition matrix well, in order to handle the reward-agnostic setting. This has been inherently done by our model-based approach. We defer more details about the lower bounds comparison in Appendix A.

### Near-Optimality in Finding $\epsilon$-Approximate NE Value

We now establish the near-minimax optimal sample complexities of model-based MARL. Note that theses results apply to both reward-aware and reward-agnostic cases, as the implementation of our model-based approach does not rely on the reward function. We start by showing the sample complexity to achieve an $\epsilon$-approximate NE value.

### Theorem 5 (Finding $\epsilon$-Approximate NE Value)

Suppose that the policy pair $(\hat{\mu},\hat{\nu})$ is obtained from the Planning Oracle using the empirical model $\hat{\mathcal{G}}$, which satisfies

Then, for any $\delta \in {(0,1\rbrack}$ and $\epsilon \in {(0,{1/{({1 - \gamma})}^{1/2}}\rbrack}$, if

for some absolute constant $c$, it holds that with probability at least $1 - \delta$,

Theorem 5 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity") shows that if the planning error $\epsilon_{opt}$ is made small, e.g., with the order of $\mathcal{O}{({{({1 - \gamma})}\epsilon})}$, then the Nash equilibrium Q-value can be estimated with a sample complexity of $\overset{\sim}{\mathcal{O}}{({{|\mathcal{S}|}{|\mathcal{A}|}{|\mathcal{B}|}{({1 - \gamma})}^{- 3}\epsilon^{- 2}})}$, as $N$ queries are made for each $(s,a,b)$ pair. This planning error can be achieved by performing any efficient black-box optimization technique over the empirical model $\hat{\mathcal{G}}$. Examples of such oracles include value iteration and (generalized) policy iteration. Moreover, note that, in contrast to the single-agent setting, where only a $\max$ operator is used, a $\min\max$ (or $\max\min$) operator is used in these algorithms, which involves solving a *matrix game* at each state. This can be solved as a linear program, with at best polynomial runtime complexity. This in total leads to an efficient polynomial runtime complexity algorithm.

As per Lemma 3 ‣ 3.1 Lower Bounds ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"), our $\overset{\sim}{\mathcal{O}}{({{|\mathcal{S}|}{|\mathcal{A}|}{|\mathcal{B}|}{({1 - \gamma})}^{- 3}\epsilon^{- 2}})}$ complexity is near-minimax optimal for the reward-aware case, in that it is tight in the dependence of $1 - \gamma$ and $|\mathcal{S}|$, and sublinear in the model-size (which is ${|\mathcal{S}|}^{2}{|\mathcal{A}|}{|\mathcal{B}|}$). However, there is a gap on the ${|\mathcal{A}|},{|\mathcal{B}|}$ dependence ($\overset{\sim}{\mathcal{O}}{({{|\mathcal{A}|}{|\mathcal{B}|}})}$ versus $\overset{\sim}{\mathcal{O}}{({{|\mathcal{A}|} + {|\mathcal{B}|}})}$). Unfortunately, without further assumption on the MG, e.g., being turn-based, the model-based algorithm can hardly avoid the $\overset{\sim}{\mathcal{O}}{({{|\mathcal{S}|}{|\mathcal{A}|}{|\mathcal{B}|}})}$ dependence, as it is required to estimate each $\hat{P}{( \cdot |s,a,b)}$ accurately to perform the planning. It is only minimax-optimal if the action-space size of one agent dominates the other's (e.g., ${|\mathcal{A}|} \gg {|\mathcal{B}|}$).

In the reward-agnostic case, as per Theorem 4 ‣ 3.1 Lower Bounds ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"), $\overset{\sim}{\mathcal{O}}{({{|\mathcal{S}|}{|\mathcal{A}|}{|\mathcal{B}|}{({1 - \gamma})}^{- 3}\epsilon^{- 2}})}$ is indeed minimax-optimal, and is tight in all ${|\mathcal{S}|},{|\mathcal{A}|},{|\mathcal{B}|}$ and $1 - \gamma$ dependence. More significantly, in this case, more than one reward functions can be handled simultaneously, as long as the transition model is estimated accurately enough. Specifically, with $M$ reward functions, by letting $\delta = {\delta/M}$ in Theorem 5 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity") and using union bounds, the sample complexity of finding $\epsilon$-approximate NE value corresponding to all $M$ reward functions becomes $\overset{\sim}{\mathcal{O}}{({{\log{(M)}}{|\mathcal{S}|}{|\mathcal{A}|}{|\mathcal{B}|}{({1 - \gamma})}^{- 3}\epsilon^{- 2}})}$, which, with $M$ being polynomial in ${|\mathcal{S}|},{|\mathcal{A}|},{|\mathcal{B}|}$, is of the same order as that in Theorem 5 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity").

However, this (near-)optimal result does not necessarily lead to near-optimal sample complexity for obtaining the $\epsilon$-NE *policies*. We first use a direct translation to obtain such an $\epsilon$-NE policy pair based on Theorem 5 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"), for *any* Planning Oracle.

### Corollary 6 (Finding $\epsilon$-NE Policy)

Let $(\hat{\mu},\hat{\nu})$ and $N$ satisfy the conditions in Theorem 5 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"). Let

and $(\overset{\sim}{\mu},\overset{\sim}{\nu})$ be the one-step Nash equilibrium of ${\hat{Q}}^{\hat{\mu},\hat{\nu}}$, namely, for any $s \in \mathcal{S}$

Then, with probability at least $1 - \delta$,

namely, $(\overset{\sim}{\mu},\overset{\sim}{\nu})$ constitutes a $2\overset{\sim}{\epsilon}$-Nash equilibrium policy pair.

Corollary 6 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity") is equivalently to saying that the sample complexity of achieving an $\epsilon$-NE policy pair is $\overset{\sim}{\mathcal{O}}{({{({1 - \gamma})}^{- 5}\epsilon^{- 2}})}$. This is worse than the model-based single-agent setting, and also worse than both the model-free single-agent and turn-based two-agent settings, where $\overset{\sim}{\mathcal{O}}{({{({1 - \gamma})}^{- 3}\epsilon^{- 2}})}$ can be achieved for learning the optimal policy. This also has a gap from the lower bound in both Lemma 3 ‣ 3.1 Lower Bounds ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity") and Theorem 4 ‣ 3.1 Lower Bounds ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"). Note that the above sample complexity still matches that of the Empirical QVI in Azar et al. if $\epsilon \in {(0,1\rbrack}$ for single-agent RL, but with a larger choice of $\epsilon$ of $(0,{({1 - \gamma})}^{- {1/2}}\rbrack$. As the Markov game setting is more challenging than MDPs, it is not clear yet if the lower bounds in Lemma 3 ‣ 3.1 Lower Bounds ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity") and Theorem 4 ‣ 3.1 Lower Bounds ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity") in finding $\epsilon$-NE policies can be achieved, using a general Planning Oracle. In contrast, we show next that a stable Planning Oracle can indeed (almost) match the lower bounds.

### Near-Optimality in Finding $\epsilon$-NE Policy

Admittedly, Corollary 6 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity") does not fully exploit the *model-based* approach, since it finds the NE policy according to the Q-value estimate ${\hat{Q}}^{\hat{\mu},\hat{\nu}}$, instead of using the output policy pair $(\hat{\mu},\hat{\nu})$ directly. This loses a factor of $1 - \gamma$. To improve the sample complexity of obtaining the NE policies, we first introduce the following definition of a smooth Planning Oracle.

### Definition 7 (Smooth Planning Oracle)

A smooth Planning Oracle generates policies that are smooth with respect to the NE Q-values of the empirical model. Specifically, for two empirical models ${\hat{\mathcal{G}}}_{1}$ and ${\hat{\mathcal{G}}}_{2}$, the generated near-equilibrium policy pair $({\hat{\mu}}_{1},{\hat{\nu}}_{1})$ and $({\hat{\mu}}_{2},{\hat{\nu}}_{2})$ satisfy that for each $s \in \mathcal{S}$, $\parallel {\hat{\mu}}_{1}{( \cdot |s)} - {\hat{\mu}}_{2}{( \cdot |s)} \parallel_{TV} \leq C \cdot \parallel {\hat{Q}}_{1}^{\ast} - {\hat{Q}}_{2}^{\ast} \parallel_{\infty}$ and $\parallel {\hat{\nu}}_{1}{( \cdot |s)} - {\hat{\nu}}_{2}{( \cdot |s)} \parallel_{TV} \leq C \cdot \parallel {\hat{Q}}_{1}^{\ast} - {\hat{Q}}_{2}^{\ast} \parallel_{\infty}$ for some constant^66^6We allow $C$ to depend polynomially on ${|\mathcal{A}|},{|\mathcal{B}|}$, which, as we will show later, does not affect the sample complexity as it appears as $\log C$. $C > 0$, where ${\hat{Q}}_{i}^{\ast}$ is the NE Q-value of ${\hat{\mathcal{G}}}_{i}$ for $i = {1,2}$, and $\parallel \cdot \parallel_{TV}$ is the total variation distance.

Such a smooth Planning Oracle can be readily obtained in several ways. For example, one simple (but possibly computationally expensive) approach is to output the average over the entire policy space, using a *softmax* randomization over best-response values induced by ${\hat{Q}}^{\ast}$. Specifically, for agent $1$, the output $\hat{\mu}$ is given by

where $\tau > 0$ is some temperature constant. The output of $\hat{\nu}$ is analogous. With a small enough $\tau$, $\hat{\mu}$ approximates the exact solution to $\operatorname{argmax}\limits_{u \in {\Delta{(\mathcal{A})}}}{{\min\limits_{\vartheta \in {\Delta{(\mathcal{B})}}}{\mathbb{E}}_{{a \sim u},{b \sim \vartheta}}}{\lbrack{{\hat{Q}}^{\ast}{(s,a,b)}}\rbrack}}$, the NE policy given ${\hat{Q}}^{\ast}$. Moreover, notice that $\hat{\mu}$ satisfies the smoothness condition in Definition 7 ‣ 3.3 Near-Optimality in Finding ϵ-NE Policy ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"). This is because for each $u \in {\Delta{(\mathcal{A})}}$ in the integral: i) the softmax function is Lipschitz continuous with respect to ${\min\limits_{\vartheta \in {\Delta{(\mathcal{B})}}}{\mathbb{E}}_{{a \sim u},{b \sim \vartheta}}}\left\lbrack {{\hat{Q}}^{\ast}{(s,a,b)}} \right\rbrack$ with Lipschitz constant $1/\tau$; ii) the best-response value ${\min\limits_{\vartheta \in {\Delta{(\mathcal{B})}}}{\mathbb{E}}_{{a \sim u},{b \sim \vartheta}}}\left\lbrack {{\hat{Q}}^{\ast}{(s,a,b)}} \right\rbrack$ is smooth with respect to ${\hat{Q}}^{\ast}$. Thus, such an oracle is an instance of a smooth Planning Oracle.

Another more tractable way to obtain $(\hat{\mu},\hat{\nu})$ is by directly solving a *regularized* matrix game induced by ${\hat{Q}}^{\ast}$. Specifically, one solves

for each $s \in \mathcal{S}$, where $\Omega_{i}$ is the regularizer for agent $i$'s policy, usually a strongly convex function, $\tau_{i} > 0$ are the temperature parameters. This strongly-convex-strongly-concave saddle point problem admits a unique solution, and can be solved efficiently. This regularization has been widely used in both single-agent MDPs, and learning in games, to improve both the exploration and convergence.

With small enough $\tau_{i}$ (with the order of $\mathcal{O}{(\epsilon)}$, see §B.1), the solution to will be $\epsilon$-close to that of the unregularized one. More importantly, many commonly used regularizations, including negative entropy, Tsallis entropy and Rényi entropy with certain parameters, naturally yield a smooth Planning Oracle; see Lemma 24 in §B.1 for a formal statement. Note that the smoothness of the oracle does not affect the sample complexity of our model-based MARL algorithm.

Now we present another theorem, which gives the $\epsilon$-Nash equilibrium *policy pair* directly, with the (near-)minimax optimal sample complexity of $\overset{\sim}{\mathcal{O}}{({{|\mathcal{S}|}{|\mathcal{A}|}{|\mathcal{B}|}{({1 - \gamma})}^{- 3}\epsilon^{- 2}})}$.

### Theorem 8 (Finding $\epsilon$-NE Policy with a Smooth Planning Oracle)

Suppose that the policy pair $(\hat{\mu},\hat{\nu})$ is obtained from a smooth Planning Oracle using the empirical model $\hat{\mathcal{G}}$ (see Definition 7 ‣ 3.3 Near-Optimality in Finding ϵ-NE Policy ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity")), which satisfies

Then, for any $\delta \in {(0,1\rbrack}$ and $\epsilon \in {(0,{1/{({1 - \gamma})}^{1/2}}\rbrack}$, if

for some absolute constant $c$, then, letting $\overset{\sim}{\epsilon}:={\epsilon + {{4\epsilon_{opt}}/{({1 - \gamma})}}}$, with probability at least $1 - \delta$,

namely, $(\hat{\mu},\hat{\nu})$ constitutes a $2\overset{\sim}{\epsilon}$-Nash equilibrium policy pair.

Theorem 8 ‣ 3.3 Near-Optimality in Finding ϵ-NE Policy ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity") shows that the sample complexity of achieving an $\epsilon$-NE policy can be near-minimax optimal for the reward-aware case, and minimax-optimal for the reward-agnostic case, if a smooth Planning Oracle is used. The dependence on $|\mathcal{S}|$ and $1 - \gamma$ also matches the only known near-optimal complexity in MGs in Sidford et al., with a turn-based setting and a model-free algorithm. Inherited from Agarwal et al., this improves the second result in Azar et al. that also has $\overset{\sim}{\mathcal{O}}{({{({1 - \gamma})}^{- 3}\epsilon^{- 2}})}$ in finding an $\epsilon$-optimal policy, by removing the dependence on ${|\mathcal{S}|}^{- {1/2}}$ and enlarging the choice of $\epsilon$ from $(0,{{({1 - \gamma})}^{- {1/2}}{|\mathcal{S}|}^{- {1/2}}}\rbrack$ to $(0,{({1 - \gamma})}^{- {1/2}}\rbrack$, and removing a factor of $|\mathcal{S}|$ in the total sample complexity for any fixed $\epsilon$. In addition, Theorem 8 ‣ 3.3 Near-Optimality in Finding ϵ-NE Policy ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity") also applies to the multi-reward setting, as Theorem 5 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"), by taking a union bound argument over all reward functions in the reward-agnostic case. If the number of reward functions $M$ is of order $\text{poly}{({|\mathcal{S}|},{|\mathcal{A}|},{|\mathcal{B}|})}$, the sample complexity of handling multiple reward functions has the same order as that in Theorem 8 ‣ 3.3 Near-Optimality in Finding ϵ-NE Policy ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity").

Theorems 5 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity") and 8 ‣ 3.3 Near-Optimality in Finding ϵ-NE Policy ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity") together justify that, this simple model-based MARL algorithm is indeed sample-efficient, in approximating both the Nash equilibrium values and policies. Moreover, our separation of the reward-aware and reward-agnostic cases highlights both the power (easily handling multiple reward functions), and the limitation (less adaptive and can hardly achieve $\overset{\sim}{\mathcal{O}}{({{|\mathcal{A}|} + {|\mathcal{B}|}})}$) of the model-based approach, particularly arising in the multi-agent RL context.

## Proofs

We first introduce some additional notation for convenience.

### Notation

For a matrix $X \in {\mathbb{R}}^{m \times n}$, $X \geq c$ for some scalar $c \in {\mathbb{R}}$ means that each element of $X$ is no-less than $c$. For a vector $x$, we use ${(x^{2})},\sqrt{x},{|x|}$ to denote the component-wise square, square-root, and absolute value of $x$. We use $P_{{(s,a,b)},s^{\prime}}$ to denote the transition probability $P{(\left. s^{\prime} \middle| {s,a,b} \right.)}$, and $P_{s,a,b}$ to denote the vector $P{( \cdot |s,a,b)}$. We also use $P^{\mu,\nu}$ to denote the transition probability of state-action pairs induced by the policy pair $(\mu,\nu)$, which is defined as

Hence, the Q-value function can be written as

Also, for any $V \in {\mathbb{R}}^{|\mathcal{S}|}$, we define the vector ${{Var}_{P}{(V)}} \in {\mathbb{R}}^{{|\mathcal{S}|} \times {|\mathcal{A}|} \times {|\mathcal{B}|}}$ as

Then, we define $\Sigma_{\mathcal{G}}^{\mu,\nu}$ to be the variance of the discounted reward under the MG $\mathcal{G}$, i.e.,

It can be shown (see an almost identical formula for MDPs in ) that $\Sigma_{\mathcal{G}}^{\mu,\nu}$ satisfies some *Bellman-type* equation for any policy pair $(\mu,\nu)$:

It can also be verified that ${\|\Sigma_{\mathcal{G}}^{\mu,\nu}\|}_{\infty} \leq {\gamma^{2}/{({1 - \gamma})}^{2}}$. Before proceeding further, we provide a roadmap for the proof.

### Proof Roadmap

Our proof mainly consists of the following steps:

Helper lemmas and a crude bound. We first establish several important lemmas, including the component-wise error bounds for the final Q-value errors, the variance error bound, and a crude error bound that directly uses Hoeffding's inequality. Some of the results are adapted from the single-agent setting to zero-sum MGs, see Agarwal et al.. See §4.1.

Establishing an auxiliary Markov game. To improve the crude bound, we build up an *absorbing Markov game*, in order to handle the statistical dependence between $\hat{P}$ and some value function generated by $\hat{P}$, which occurs as a product in the component-wise bound above. By carefully designing the auxiliary game, we establish a Bernstein-like concentration inequality, despite this dependency. See §4.2, more precisely, Lemmas 17 and 18.

Final bound for $\epsilon$-approximate NE value. Lemma 17 in Step 2 allows us to exploit the variance bound, see Lemma 11, to obtain an $\overset{\sim}{\mathcal{O}}{(\sqrt{{1/{\lbrack{({1 - \gamma})}^{3}\rbrack}}N})}$ order bound on the Q-value error, leading to a $\overset{\sim}{\mathcal{O}}{({{({1 - \gamma})}^{- 3}\epsilon^{- 2}})}$ near-minimax optimal sample complexity for achieving the $\epsilon$-approximate NE value. See §4.3.

Final bounds for $\epsilon$-NE policy. Based on the final bound in Step 3, we then establish a $\overset{\sim}{\mathcal{O}}{({{({1 - \gamma})}^{- 5}\epsilon^{- 2}})}$ sample complexity for obtaining an $\epsilon$-NE policy pair, by solving an additional matrix game over the output Q-value ${\hat{Q}}^{\hat{\mu},\hat{\nu}}$. See §4.4. In addition, given a smooth Planning Oracle, by Lemma 18 in Step 2, and more careful self-bounding techniques, we establish a $\overset{\sim}{\mathcal{O}}{({{({1 - \gamma})}^{- 3}\epsilon^{- 2}})}$ sample complexity for achieving such an $\epsilon$-NE policy, directly using the output policies $(\hat{\mu},\hat{\nu})$. See §4.5.

### Important Lemmas

We start with the component-wise error bounds.

### Lemma 9 (Component-Wise Bounds)

For any policy pair $(\mu,\nu)$, it follows that

where we recall that $\nu{(\mu)}$ and $\mu{(\nu)}$ denote the best-response policy given $\mu$ and $\nu$, respectively (see ). Moreover, we have

Proof First, note that

proving the first equation. Also,

where we recall that $\hat{\nu{(\mu)}}{( \cdot |s)} \in \operatorname{argmin}{\hat{V}}^{\mu,\nu}{(s)}$ for all $s \in \mathcal{S}$. By similar arguments, recalling that $\nu{(\mu)}{( \cdot |s)} \in \operatorname{argmin}V^{\mu,\nu}{(s)}$ for all $s$, we have

Similar arguments yield the third inequality in the first argument.

For the second argument, we have

which, combined with triangle inequality, yields the first inequality. Similarly, we have

Using triangle inequality proves the second inequality. For (10 ‣ 4.1 Important Lemmas ‣ 4 Proofs ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"))-(11 ‣ 4.1 Important Lemmas ‣ 4 Proofs ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity")), we similarly have

Notice that for any $\mu \in {\Delta{(\mathcal{A})}^{|\mathcal{S}|}}$ and $\nu \in {\Delta{(\mathcal{B})}^{|\mathcal{S}|}}$,

Combining - and -, together with triangle inequality, we arrive at (10 ‣ 4.1 Important Lemmas ‣ 4 Proofs ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"))-(11 ‣ 4.1 Important Lemmas ‣ 4 Proofs ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity")), and complete the proof. \

We establish the decomposition in (8 ‣ 4.1 Important Lemmas ‣ 4 Proofs ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"))-(9 ‣ 4.1 Important Lemmas ‣ 4 Proofs ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity")) for the following intuition and reasons. The error in (8 ‣ 4.1 Important Lemmas ‣ 4 Proofs ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"))-(9 ‣ 4.1 Important Lemmas ‣ 4 Proofs ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity")) contains three terms: the first and third terms ${\|{Q^{\mu,\nu} - {\hat{Q}}^{\mu,\nu}}\|}_{\infty}$ and ${{\hat{Q}}^{\ast}\parallel}_{\infty} - {\|{{\hat{Q}}^{\mu^{\ast}, \ast} - Q^{\ast}}\|}_{\infty}$ are the differences of the Q-value for some policy pairs in the true and estimated models, respectively, which will be handled later based on the statistical error of the model estimation; the second term ${\|{{\hat{Q}}^{\mu,\nu} - {\hat{Q}}^{\ast}}\|}_{\infty}$ is the *optimization error* we obtained from the algorithm that solves the empirical game, which will be controlled with an efficient Planning Oracle. To deal with the statistical errors, we first introduce the following lemma, which is adapted from Lemma $2$ in Agarwal et al..

### Lemma 10

For any policy pair $(\mu,\nu)$ and vector $v \in {\mathbb{R}}^{{|\mathcal{S}|} \times {|\mathcal{A}|} \times {|\mathcal{B}|}}$, ${\|{{({I - {\gammaP^{\mu,\nu}}})}^{- 1}v}\|}_{\infty} \leq {{\| v\|}_{\infty}/{({1 - \gamma})}}$.

Proof The proof is straightforward. Letting $w = {{({I - {\gammaP^{\mu,\nu}}})}^{- 1}v}$, we have $v = {{({I - {\gammaP^{\mu,\nu}}})}w}$. Triangle inequality yields ${\| v\|}_{\infty} \geq {{\| w\|}_{\infty} - {\gamma{\|{P^{\mu,\nu}w}\|}_{\infty}}} \geq {{\| w\|}_{\infty} - {\gamma{\| w\|}_{\infty}}}$, which completes the proof. \

Next we establish the Bellman property of a policy pair $(\mu,\nu)$'s variance and its accumulation. This has been observed for MDPs before in Munos and Moore; Lattimore and Hutter; Azar et al.; Agarwal et al.. We establish the counterpart for Markov games as follows.

### Lemma 11

For any policy pair $(\mu,\nu)$ and MG $\mathcal{G}$ with transition model $P$, we have

Proof The proof follows that of. For any positive vector $v$, by Jensen's inequality, we have

Also, observe that

Combining and yields

In addition, by, we have $\Sigma_{\mathcal{G}}^{\mu,\nu} = {\gamma^{2}{({I - {\gamma^{2}P^{\mu,\nu}}})}^{- 1}{{Var}_{P}{(V_{\mathcal{G}}^{\mu,\nu})}}}$. Letting $v = {{Var}_{P}{(V_{\mathcal{G}}^{\mu,\nu})}}$ in and noticing that ${\|\Sigma_{\mathcal{G}}^{\mu,\nu}\|}_{\infty} \leq {\gamma^{2}/{({1 - \gamma})}^{2}}$ completes the proof. \

Finally, if we just apply Hoeffding's inequality, we obtain the following concentration argument, upon which we will improve to obtain our final results.

### Lemma 12

Let $(\mu^{\ast},\nu^{\ast})$ be the Nash equilibrium policy pair under the actual model $\mathcal{G}$. Then, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$, we have

Proof First note that $V^{\ast}$ is fixed and independent of the randomness in $\hat{P}$. Due to the boundedness of $V^{\ast}$ that ${\| V^{\ast}\|}_{\infty} \leq {({1 - \gamma})}^{- 1}$, and the union of Hoeffding bounds over $\mathcal{S} \times \mathcal{A} \times \mathcal{B}$, we have that with probability at least $1 - \delta$

On the other hand, let $\mathcal{T}_{\mu,\nu}$ be the Bellman operator under the true transition model $P$, using any joint policy $(\mu,\nu)$, i.e., for any $s \in \mathcal{S}$ and ${(s,a,b)} \in {\mathcal{S} \times \mathcal{A} \times \mathcal{B}}$, $V \in {\mathbb{R}}^{|\mathcal{S}|}$ and $Q \in {\mathbb{R}}^{{|\mathcal{S}|} \times {|\mathcal{A}|} \times {|\mathcal{B}|}}$:

Similarly, let ${\hat{\mathcal{T}}}_{\mu,\nu}$ be the corresponding operator defined under the estimated transition $\hat{P}$. Note that ${\hat{Q}}^{\mu,\nu}$ and $Q^{\ast}$ are the fixed points of ${\hat{\mathcal{T}}}_{\mu,\nu}$ and $\mathcal{T}_{\mu^{\ast},\nu^{\ast}}$, respectively. We thus have

To show the first argument, letting $\mu = \mu^{\ast}$ and $\nu = \nu^{\ast}$, we have

Using (4.1) to bound the last term in, and solving for ${\|{Q^{\ast} - {\hat{Q}}^{\mu^{\ast},\nu^{\ast}}}\|}_{\infty}$ from, we obtain the first argument.

For the second argument, letting $\mu = \mu^{\ast}$ and $\nu = \hat{\nu{(\mu^{\ast})}}$ (note that ${\hat{Q}}^{\mu^{\ast}, \ast} = {\hat{Q}}^{\mu^{\ast},\hat{\nu{(\mu^{\ast})}}}$), we have

where the first inequality is due to the non-expansiveness of the $\min$ operator. Using (4.1) to bound the last term in, and solving for ${\|{Q^{\ast} - {\hat{Q}}^{\mu^{\ast}, \ast}}\|}_{\infty}$ from, we obtain the second argument. Similarly, we can obtain the third argument.

For the fourth argument, letting $\mu = {\hat{\mu}}^{\ast}$ and $\nu = {\hat{\nu}}^{\ast}$, the NE policy under $\hat{P}$ (note that ${\hat{Q}}^{{\hat{\mu}}^{\ast},{\hat{\nu}}^{\ast}} = {\hat{Q}}^{\ast}$), we have

where the inequalities are due to the non-expansivenesses of both the $\max$ and the $\min$ operators. This, combined with, completes the proof. \

The argument above will lead to a crude bound, with an additional $1/{({1 - \gamma})}$ dependence compared to our main results in Theorem 5 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity") and Theorem 8 ‣ 3.3 Near-Optimality in Finding ϵ-NE Policy ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"). The key reason is that we used some self-bounding of the error terms, e.g., ${\|{Q^{\ast} - {\hat{Q}}^{\mu^{\ast},\nu^{\ast}}}\|}_{\infty}$, which appears on both sides of the inequality, with a $\gamma$ discounting on the right-hand side. This way, by subtracting the term on the right-hand side, we have an additional $1/{({1 - \gamma})}$ order after dividing $({1 - \gamma})$ on both sides. This was essentially due to the fact that the direct concentration argument can only deal with the concentration of $\left\| {{({\hat{P} - P})}V^{\ast}} \right\|_{\infty}$, where $\hat{P}$ and $V^{\ast}$ are not dependent as $V^{\ast}$ is a fixed vector. To obtain sharper rates, one has to directly deal with the quantities as $\left\| {{({\hat{P} - P})}\hat{V}} \right\|_{\infty}$, where $\hat{V}$ denotes some value function obtained from the empirical model, and is correlated with $\hat{P}$. Properly handling this interdependence will be the focus of our proof next.

### An Auxiliary Markov Game

Motivated by the *absorbing MDP* technique in Agarwal et al., we introduce an *absorbing Markov game*, in order to handle the interdependence between $\hat{P}$ and ${\hat{V}}^{\mu,\nu}$, for any $\mu,\nu$ (which may also depend on $\hat{P}$), which will show up frequently in the analysis.

We now define a new Markov game $\mathcal{G}_{s,u}$ as follows (with $s \in \mathcal{S}$ and $u \in {\mathbb{R}}$ a constant): $\mathcal{G}_{s,u}$ is identical to $\mathcal{G}$, except that ${P_{\mathcal{G}_{s,u}}{(\left. s \middle| {s,a,b} \right.)}} = 1$ for all ${(a,b)} \in {\mathcal{A} \times \mathcal{B}}$, namely, state $s$ is an *absorbing* state; and the instantaneous reward at $s$ is always ${({1 - \gamma})}u$. The rest of the reward function and the transition model of $\mathcal{G}_{s,u}$ are the same as those of $\mathcal{G}$. For notational simplicity, we now use $X_{s,u}^{\mu,\nu}$ to denote $X_{\mathcal{G}_{s,u}}^{\mu,\nu}$, where $X$ can be either the value functions $Q$ and $V$, or the reward function $r$, under the model $\mathcal{G}_{s,u}$. Obviously, for any policy pair $(\mu,\nu)$, ${V_{s,u}^{\mu,\nu}{(s)}} = u$ for the absorbing state $s$.

In addition, we define $U_{s}$ for some state $s$ to choose $u$ from, which is a set of evenly spaced elements in the interval $\lbrack{{V^{\ast}{(s)}} - \Delta},{{V^{\ast}{(s)}} + \Delta}\rbrack$ for some $\Delta > 0$, i.e., $U_{s} \subset {\lbrack{{V^{\ast}{(s)}} - \Delta},{{V^{\ast}{(s)}} + \Delta}\rbrack}$. An appropriately chosen size of $|U_{s}|$ will be the key in the proof. We also use ${\hat{P}}_{\mathcal{G}_{s,u}}$ to denote the transition model of the absorbing MG for the empirical MG $\hat{\mathcal{G}}$, denoted by ${\hat{\mathcal{G}}}_{s,u}$. Specifically, at all non-absorbing states, ${\hat{P}}_{\mathcal{G}_{s,u}}$ is identical to $\hat{P}$; while at the absorbing state, ${{\hat{P}}_{\mathcal{G}_{s,u}}{(\left. s \middle| {s,a,b} \right.)}} = 1$ for any ${(a,b)} \in {\mathcal{A} \times \mathcal{B}}$. The corresponding value functions are for short denoted by ${\hat{V}}_{s,u}^{\mu,\nu}$ and ${\hat{Q}}_{s,u}^{\mu,\nu}$. Similar as in the original MG, we also use ${\hat{V}}_{s,u}^{\ast}$ to denote the NE value under the model ${\hat{\mathcal{G}}}_{s,u}$, and use ${\hat{V}}_{s,u}^{\mu, \ast}$ and ${\hat{V}}_{s,u}^{\ast,\nu}$ to denote the best-response values of some given $\mu$ and $\nu$, under the model ${\hat{\mathcal{G}}}_{s,u}$. Now we first have the following lemma based on Bernstein's inequality; see a similar argument in Lemma 5 in Agarwal et al..

### Lemma 13

For fixed state $s$, action $(a,b)$, a finite set $U_{s}$, and $\delta > 0$, it holds that for all $u \in U_{s}$, with probability greater than $1 - \delta$,

where $P_{s,a,b}$ and ${\hat{P}}_{s,a,b}$ are the transition models extracted from the original game $\mathcal{G}$ and its empirical version $\hat{\mathcal{G}}$, respectively (not related to either $\mathcal{G}_{s,u}$ or ${\hat{\mathcal{G}}}_{s,u}$), and $({\hat{\mu}}_{s,a},{\hat{\nu}}_{s,a})$ is the output of the Planning Oracle using the auxiliary empirical model ${\hat{\mathcal{G}}}_{s,u}$

Proof The key observation is that the random variables ${\hat{P}}_{s,a,b}$ and ${\hat{V}}_{s,u}^{\ast}$ are independent. Using Bernstein's inequality along with a union bound over all $u \in U_{s}$, we obtain the first inequality. The other inequalities follow similarly, as ${\hat{P}}_{s,a,b}$ is independent of ${\hat{V}}_{s,u}^{\mu^{\ast}, \ast}$, ${\hat{V}}_{s,u}^{\ast,\nu^{\ast}}$, ${\hat{V}}_{s,u}^{\mu^{\ast},\nu^{\ast}}$, $V^{{\hat{\mu}}_{s,u}, \ast}$, and $V^{\ast,{\hat{\nu}}_{s,u}}$. This is because the latter terms are all decided by the original game $\mathcal{G}$, and/or the auxiliary empirical game ${\hat{\mathcal{G}}}_{s,u}$ (not the original empirical game $\hat{\mathcal{G}}$). \

Note that the arguments in Lemma 13 do not hold, if we replace ${\hat{V}}_{s,u}^{\ast}$ by ${\hat{V}}^{\ast}$, or ${\hat{V}}_{s,u}^{\mu^{\ast}, \ast}$ by ${\hat{V}}^{\mu^{\ast}, \ast}$, or ${\hat{V}}_{s,u}^{\ast,\nu^{\ast}}$ by ${\hat{V}}^{\ast,\nu^{\ast}}$. It will neither hold if we replace ${\hat{V}}_{s,u}^{\mu^{\ast}, \ast}$ and $V^{{\hat{\mu}}_{s,u}, \ast}$ by some ${\hat{V}}^{\mu, \ast}$ and $V^{\mu, \ast}$, for any $\mu$ that is dependent on $\hat{P}$, e.g., the NE policy ${\hat{\mu}}^{\ast}$ for the original empirical game $\hat{\mathcal{G}}$. This is one of the key subtleties that are worth emphasizing.

Next we establish two helpful lemmas that help guide the choices of $U_{s}$, so that ${\hat{V}}_{s,u}^{\ast}$ (resp. ${\hat{V}}_{s,u}^{\mu^{\ast}, \ast}$, ${\hat{V}}_{s,u}^{\ast,\nu^{\ast}}$, and ${\hat{V}}_{s,u}^{\mu^{\ast},\nu^{\ast}}$) will be a good approximate of ${\hat{V}}^{\ast}$ (resp. ${\hat{V}}^{\mu^{\ast}, \ast}$, ${\hat{V}}^{\ast,\nu^{\ast}}$, and ${\hat{V}}^{\mu^{\ast},\nu^{\ast}}$).

### Lemma 14

For the absorbing state $s$, and any joint policy $(\mu,\nu)$, suppose that $u^{\ast} = {V_{\mathcal{G}}^{\ast}{(s)}}$, $u^{\mu, \ast} = {V_{\mathcal{G}}^{\mu, \ast}{(s)}}$, $u^{\ast,\nu} = {V_{\mathcal{G}}^{\ast,\nu}{(s)}}$, and $u^{\mu,\nu} = {V_{\mathcal{G}}^{\mu,\nu}{(s)}}$. Then,

Proof For the first formula, we need to verify that $V_{\mathcal{G}}^{\ast}$ satisfies the optimal (Nash equilibrium) Bellman equation for the game $\mathcal{G}_{s,u^{\ast}}$. To this end, note that if $s^{\prime} = s$, then $u^{\ast} = {V_{\mathcal{G}}^{\ast}{(s)}}$ satisfies the Bellman equation trivially, since $s$ is absorbing with the value ${V_{s,u^{\ast}}^{\ast}{(s)}} = u^{\ast}$.

On the other hand, for any $s^{\prime} \neq s$, the outgoing transition model at $s^{\prime}$ in $\mathcal{G}_{s,u^{\ast}}$ is the same as that in $\mathcal{G}$, and $V_{\mathcal{G}}^{\ast}{(s^{\prime})}$ per se satisfies the Bellman equation in $\mathcal{G}$ (which are the same for $\mathcal{G}_{s,u^{\ast}}$ at these states $s^{\prime} \neq s$). Thus, $V_{\mathcal{G}}^{\ast}$ satisfies the Bellman equation in $\mathcal{G}_{s,u^{\ast}}$ for all states. This proves the first equation. The proofs for the remaining three equations are analogous. \

Perfect choices of $u$ have been specified in Lemma 14 above. Moreover, we need to quantify how the value changes if we deviate from these perfect choices, i.e., the robustness to misspecification of $u$. This result is formally established in the following lemma; see also Lemma 7 in Agarwal et al. for a similar result.

### Lemma 15

For any state $s$, ${u,u^{\prime}} \in {\mathbb{R}}$, and joint policy pair $(\mu,\nu)$, we have

Proof Note that ${\|{r_{s,u} - r_{s,u^{\prime}}}\|}_{\infty} = {{({1 - \gamma})}{|{u - u^{\prime}}|}}$, since the reward functions only differ at $s$, where ${r_{s,u}{(s,a,b)}} = {{({1 - \gamma})}u}$ and ${r_{s,u^{\prime}}{(s,a,b)}} = {{({1 - \gamma})}u^{\prime}}$. We denote the NE policy pair in $\mathcal{G}_{s,u}$ by $(\mu_{s,u}^{\ast},\nu_{s,u}^{\ast})$. Thus,

where uses the fact that at the NE,

implying the relationships of the corresponding Q-values; is by definition; uses the observation that $P_{s,u}^{\mu_{s,u}^{\ast},\nu_{s,u^{\prime}}^{\ast}}$ is the same as $P_{s,u^{\prime}}^{\mu_{s,u}^{\ast},\nu_{s,u^{\prime}}^{\ast}}$ (transition is not affected by the value of $u$). Similarly, we can establish the lower bound that ${Q_{s,u}^{\ast} - Q_{s,u^{\prime}}^{\ast}} \geq {- {|{u - u^{\prime}}|}}$, which proves ${\|{Q_{s,u}^{\ast} - Q_{s,u^{\prime}}^{\ast}}\|}_{\infty} \leq {|{u - u^{\prime}}|}$. Moreover, we have

which proves the first inequality.

For the second one, recalling that the best-response policy of $\mu$ under $\mathcal{G}_{s,u}$ being $\nu_{s,u}{(\mu)}$, we have

where uses the definition of a best-response value, plugs in the best-response policy $\nu_{s,u^{\prime}}{(\mu)}$, and also uses the fact that the transition does not depend on the value $u$. A lower bound can be established by noticing that $Q_{s,u^{\prime}}^{\mu, \ast} = {\min_{\nu}Q_{s,u^{\prime}}^{\mu,\nu}} \leq Q_{s,u^{\prime}}^{\mu,{\nu_{s,u}{(\mu)}}}$. This proves ${\|{Q_{s,u}^{\mu, \ast} - Q_{s,u^{\prime}}^{\mu, \ast}}\|}_{\infty} \leq {|{u - u^{\prime}}|}$. Furthermore, notice that

which proves the second inequality. Similar arguments can also be used to establish the third and the fourth inequalities. This completes the proof. \

We are now ready to show the main result in this section.

### Lemma 16

For any state $s$, joint action pair $(a,b)$, and a finite set $U_{s}$, with probability greater than $1 - \delta$, we have

Moreover, recalling that $({\hat{\mu}}_{s,u},{\hat{\nu}}_{s,u})$ is the output of the Planning Oracle using ${\hat{\mathcal{G}}}_{s,u}$, we have

Proof First, for all $u \in U_{s}$ and with probability greater than $1 - \delta$, we have

where - use triangle inequality, is due to Lemma 13, and uses the facts that $\sqrt{{Var}_{P_{s,a,b}}{({X + Y})}} \leq {\sqrt{{Var}_{P_{s,a,b}}{(X)}} + \sqrt{{Var}_{P_{s,a,b}}{(Y)}}}$, and $\sqrt{{Var}_{P_{s,a,b}}{(X)}} \leq {\| X\|}_{\infty}$. Moreover, by Lemmas 14 and 15, we obtain that

which, combined with and taken minimization over all $u \in U_{s}$, yields the first inequality. Proofs for the remaining inequalities are analogous, except that for the last two, the norms ${\|{V^{\hat{\mu}, \ast} - V^{{\hat{\mu}}_{s,u}, \ast}}\|}_{\infty}$ and ${\|{V^{\ast,\hat{\nu}} - V^{\ast,{\hat{\nu}}_{s,u}}}\|}_{\infty}$ are kept and not further bounded. \

Next we establish the important result that characterizes the errors $|{{({P - \hat{P}})}{\hat{V}}^{\ast}}|$, $|{{({P - \hat{P}})}{\hat{V}}^{\mu^{\ast}, \ast}}|$, $|{{({P - \hat{P}})}{\hat{V}}^{\ast,\nu^{\ast}}}|$, and $|{{({P - \hat{P}})}{\hat{V}}^{\mu^{\ast},\nu^{\ast}}}|$, which could not have been handled without the arguments above, due to the dependence between $\hat{P}$ and ${\hat{V}}^{\ast}$ (and also ${\hat{V}}^{\mu^{\ast}, \ast}$, ${\hat{V}}^{\ast,\nu^{\ast}}$, and ${\hat{V}}^{\mu^{\ast},\nu^{\ast}}$).

### Lemma 17

For any $\delta \in {(0,1\rbrack}$, with probability greater than $1 - \delta$, it holds that

where $\Delta_{\delta,N}^{\prime}$ is defined as

and $c$ is some absolute constant.

Proof Let $U_{s}$ denote a set with evenly spaced elements in the interval $\lbrack{{V^{\ast}{(s)}} - \Delta_{{\delta/2},N}},{{V^{\ast}{(s)}} + \Delta_{{\delta/2},N}}\rbrack$, with ${|U_{s}|} = {2/{({1 - \gamma})}^{2}}$, and $\Delta_{\delta,N}$ being defined in Lemma 12. Lemma 12 shows that with probability greater than $1 - {\delta/2}$,

for all $s \in \mathcal{S}$. Since each subinterval determined by $U_{s}$ is of length ${2\Delta_{{\delta/2},N}}/{({{|U_{s}|} - 1})}$, and ${\hat{V}}^{\ast}{(s)}$ will fall into one of them, we know that

where we have used the fact that ${|U_{s}|} \geq {{1/{({1 - \gamma})}^{2}} + 1}$. We then choose $\delta/2$ to be $\delta/{({2{|\mathcal{S}|}{|\mathcal{A}|}{|\mathcal{B}|}})}$ in Lemma 16, so that it holds for all states and joint actions with probability greater than $1 - {\delta/2}$. By substitution and noting that the two events in Lemmas 12 and 16 both fail with probability $\delta/2$, we obtain the first inequality by properly choosing the constant $c$. Similarly, for the other two inequalities, note that Lemma 12 can be applied to show that ${\hat{V}}^{\mu^{\ast}, \ast}{(s)}$, ${\hat{V}}^{\ast,\nu^{\ast}}{(s)}$, and ${\hat{V}}^{\mu^{\ast},\nu^{\ast}}{(s)}$, all lie in the interval in (centered at $V^{\ast}{(s)}$). By similar arguments, the remaining three inequalities can be proved (note that Lemma 16 can be applied to ${\hat{V}}^{\mu^{\ast}, \ast}{(s)}$, ${\hat{V}}^{\ast,\nu^{\ast}}{(s)}$, and ${\hat{V}}^{\mu^{\ast},\nu^{\ast}}{(s)}$, as well). \

Lastly, with a smooth Planning Oracle, see Definition 7 ‣ 3.3 Near-Optimality in Finding ϵ-NE Policy ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"), we can similarly establish the following error bounds on $|{{({P - \hat{P}})}V^{\hat{\mu}, \ast}}|$ and $|{{({P - \hat{P}})}V^{\ast,\hat{\nu}}}|$, thanks to Lemma 16.

### Lemma 18

With a smooth Planning Oracle that has a smooth constant $C$ (see Definition 7 ‣ 3.3 Near-Optimality in Finding ϵ-NE Policy ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity")), for any $\delta \in {(0,1\rbrack}$, with probability greater than $1 - \delta$, it holds that

where $\Delta_{\delta,N}^{\operatorname{\prime\prime}}$ is defined as

for some absolute constant $c$.

Proof Following the proof of Lemma 17, let $U_{s}$ denote a set with evenly spaced elements in the interval $\lbrack{{V^{\ast}{(s)}} - \Delta_{{\delta/2},N}},{{V^{\ast}{(s)}} + \Delta_{{\delta/2},N}}\rbrack$, with $\Delta_{\delta,N}$ being defined in Lemma 12. By Lemma 12, we know that ${\hat{V}}^{\ast}{(s)}$ lies in this interval with probability greater than $1 - {\delta/2}$, for all $s \in \mathcal{S}$. Now we choose ${|U_{s}|} = {{({C + 1})}/{({1 - \gamma})}^{4}}$, where $C$ is the smooth coefficient in Definition 7 ‣ 3.3 Near-Optimality in Finding ϵ-NE Policy ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"). As ${\hat{V}}^{\ast}{(s)}$ will fall into one of the subintervals determined by $U_{s}$, we have

which also uses the fact ${|U_{s}|} \geq {{C/{({1 - \gamma})}^{4}} + 1}$. Furthermore, by Definition 7 ‣ 3.3 Near-Optimality in Finding ϵ-NE Policy ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity") and the proof of Lemma 15, we have

On the other hand, we have

where uses Hölder's inequality, and follows by expanding the Q-value functions, using, and noticing that ${\| Q^{{\hat{\mu}}_{s,u}, \ast}\|}_{\infty} \leq {1/{({1 - \gamma})}}$. Combining and, and taking $\min$ over $u \in U_{s}$, we have

The rest of the proof follows the arguments of Lemma 17, which combines the last two inequalities in Lemma 16 to obtain the desired bound. Note that the absolute constant here might be different from that in Lemma 17. The proof for the second inequality is analogous. \

Note that compared to Lemma 17, Lemma 18 has to additionally deal with the interdependence between $\hat{P}$ and $V^{\hat{\mu}, \ast}$ (as well as that between $\hat{P}$ and $V^{\ast,\hat{\nu}}$). What can be guaranteed before, in the absorbing MGs, is that the value function can be controlled to be close to that in the original MG (see Lemmas 14 and 15, and the proof of Lemma 16). However, in general, it is unclear how much the NE policy changes, as well as how much the best-response value in the original true MG changes. This calls for some stability of the NE policy, and was made possible due to the smoothness of our Planning Oracle (see -). Lemma 18 will play an important role in obtaining the near-optimal sample complexity in Theorem 8 ‣ 3.3 Near-Optimality in Finding ϵ-NE Policy ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity") (see §4.5).

### Proof of Theorem 5 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity")

We are now ready to prove Theorem 5 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"). To this end, we first establish the following lemma.

### Lemma 19

For any policy pair $(\hat{\mu},\hat{\nu})$ that satisfies the condition in Theorem 5 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"), there exists some absolute constant $c$ such that

Proof Note that

where is due to Lemma 9 ‣ 4.1 Important Lemmas ‣ 4 Proofs ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"); uses triangle inequality; and is due to the non-negativeness of the entries in ${({I - {\gammaP^{\hat{\mu},\hat{\nu}}}})}^{- 1}$, the sub-optimality of $(\hat{\mu},\hat{\nu})$, and Lemma 10. Since the first term in can be bounded using Lemma 17, we have

where uses the fact that $\sqrt{{Var}_{P}{({X + Y})}} \leq {\sqrt{{Var}_{P}{(X)}} + \sqrt{{Var}_{P}{(Y)}}}$; is due to Lemma 11, the fact that $\sqrt{{Var}_{P}{({V^{\hat{\mu},\hat{\nu}} - {\hat{V}}^{\hat{\mu},\hat{\nu}}})}} \leq {\|{V^{\hat{\mu},\hat{\nu}} - {\hat{V}}^{\hat{\mu},\hat{\nu}}}\|}_{\infty}$, and ${\|{{\hat{V}}^{\hat{\mu},\hat{\nu}} - {\hat{V}}^{\ast}}\|}_{\infty} \leq \epsilon_{opt}$; is due to ${\|{V^{\hat{\mu},\hat{\nu}} - {\hat{V}}^{\hat{\mu},\hat{\nu}}}\|}_{\infty} \leq {\|{Q^{\hat{\mu},\hat{\nu}} - {\hat{Q}}^{\hat{\mu},\hat{\nu}}}\|}_{\infty}$. Solving for ${\|{Q^{\hat{\mu},\hat{\nu}} - {\hat{Q}}^{\hat{\mu},\hat{\nu}}}\|}_{\infty}$ in yields the desired inequality.

For the second inequality, by Lemma 9 ‣ 4.1 Important Lemmas ‣ 4 Proofs ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"), we first have

Thus, we obtain that

For the first term in the $\max$ operator above, by similar arguments from -, we have

where is due to Lemma 17, uses triangle inequality, and uses Lemma 11. Solving for $\left\| {Q^{\mu^{\ast},\nu^{\ast}} - {\hat{Q}}^{\mu^{\ast},\nu^{\ast}}} \right\|_{\infty}$ gives the bound for it.

Similarly, the second term in the $\max$ operator in can be bounded by

which can be solved to obtain a bound for $\left\| {Q^{\mu^{\ast},\hat{\nu{(\mu^{\ast})}}} - {\hat{Q}}^{\mu^{\ast}, \ast}} \right\|_{\infty}$. Combining the two bounds and, we prove the second inequality in the lemma. The proof for the third inequality is analogous. \

With Lemma 19 in hand, we are ready to prove Theorem 5 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"). Note that the condition on $N$ in Theorem 5 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity") makes $\alpha_{\delta,N} < {1/2}$. Thus, by (8 ‣ 4.1 Important Lemmas ‣ 4 Proofs ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"))-(9 ‣ 4.1 Important Lemmas ‣ 4 Proofs ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity")) in Lemma 9 ‣ 4.1 Important Lemmas ‣ 4 Proofs ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity") with $(\mu,\nu)$ being replaced by $(\hat{\mu},\hat{\nu})$, we have

Substituting in the bounds of ${\|{Q^{\hat{\mu},\hat{\nu}} - {\hat{Q}}^{\hat{\mu},\hat{\nu}}}\|}_{\infty}$, ${\|{Q^{\ast} - {\hat{Q}}^{\mu^{\ast}, \ast}}\|}_{\infty}$, and ${\|{Q^{\ast} - {\hat{Q}}^{\ast,\nu^{\ast}}}\|}_{\infty}$ in Lemma 19, we arrive at the final bound for ${\|{Q^{\hat{\mu},\hat{\nu}} - Q^{\ast}}\|}_{\infty}$:

With a certain choice of $c$, we have ${\|{Q^{\hat{\mu},\hat{\nu}} - Q^{\ast}}\|}_{\infty} \leq {{{2\epsilon}/3} + {{5\gamma\epsilon_{opt}}/{({1 - \gamma})}}}$.

For the last argument in Theorem 5 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"), by triangle inequality, with the same constant $c$ used above, we have

which completes the proof.

### Proof of Corollary 6 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity")

We now prove Corollary 6 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"), based on Theorem 5 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"). For any state $s$, we have

where uses the fact that

and is due to the fact that

by definition of $\overset{\sim}{\mu}$. Hence together with Theorem 5 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"), implies that

By similar arguments, we have

Combining and yields

which completes the proof.

### Proof of Theorem 8 ‣ 3.3 Near-Optimality in Finding ϵ-NE Policy ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity")

We now prove the second main result, Theorem 8 ‣ 3.3 Near-Optimality in Finding ϵ-NE Policy ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"). First, following the proof of Corollary 6 ‣ 3.2 Near-Optimality in Finding ϵ-Approximate NE Value ‣ 3 Main Results ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"), it suffices to prove that ${V^{\ast} - V^{\hat{\mu}, \ast}} \leq \overset{\sim}{\epsilon}$, ${V^{\ast,\hat{\nu}} - V^{\ast}} \leq \overset{\sim}{\epsilon}$, since they together imply that $(\hat{\mu},\hat{\nu})$ is a $2\overset{\sim}{\epsilon}$-Nash equilibrium. The following analysis is devoted to proving this argument.

The idea is similar to that presented in §4.3, i.e., we use the component-wise error decompositions in Lemma 9 ‣ 4.1 Important Lemmas ‣ 4 Proofs ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"), but use (10 ‣ 4.1 Important Lemmas ‣ 4 Proofs ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"))-(11 ‣ 4.1 Important Lemmas ‣ 4 Proofs ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity")) instead. In particular, letting $\mu = \hat{\mu}$ and $\nu = \hat{\nu}$, we have

Note that the bounds for ${\|{{\hat{Q}}^{\mu^{\ast}, \ast} - Q^{\ast}}\|}_{\infty}$ and ${\|{{\hat{Q}}^{\ast,\nu^{\ast}} - Q^{\ast}}\|}_{\infty}$ have already been established in Lemma 19 (without dependence on $\epsilon_{opt}$ and the Planning Oracle). It now suffices to bound ${\|{Q^{\hat{\mu}, \ast} - {\hat{Q}}^{\hat{\mu}, \ast}}\|}_{\infty}$ and ${\|{Q^{\ast,\hat{\nu}} - {\hat{Q}}^{\ast,\hat{\nu}}}\|}_{\infty}$. For the former term, by Lemma 9 ‣ 4.1 Important Lemmas ‣ 4 Proofs ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity"), we first have

Thus, we know that

The first term in the $\max$ operator, where the policies in the pair $(\hat{\mu},\hat{\nu{(\hat{\mu})}})$ are both obtained from the empirical model $\hat{\mathcal{G}}$, can be bounded similarly as that for ${\|{Q^{\hat{\mu},\hat{\nu}} - {\hat{Q}}^{\hat{\mu},\hat{\nu}}}\|}_{\infty}$ in Lemma 19. Specifically, following -, we have

where uses triangle inequality, and is due to the optimization error of $\hat{\mu}$. Then, to bound $\gamma\left\| {{({I - {\gammaP^{\hat{\mu},\hat{\nu{(\hat{\mu})}}}}})}^{- 1}\left| {{({P - \hat{P}})}{\hat{V}}^{\ast}} \right|} \right\|_{\infty}$, the rest of the proof is analogous to the derivations in -, by replacing $\hat{\nu}$ therein by $\hat{\nu{(\hat{\mu})}}$, and bound ${\|{{\hat{V}}^{\hat{\mu}, \ast} - {\hat{V}}^{\ast}}\|}_{\infty}$ by $\epsilon_{opt}$. Solving for ${\|{Q^{\hat{\mu},\hat{\nu{(\hat{\mu})}}} - {\hat{Q}}^{\hat{\mu}, \ast}}\|}_{\infty}$ yields the desired bound for the first term in the $\max$ in, namely, there exists some constant $c$ such that with probability greater than $1 - \delta$,

where $\alpha_{\delta,N}^{\prime}$ is defined as

For the second term in the $\max$ in, note that $\hat{\mu}$ is obtained from $\hat{\mathcal{G}}$, while $\nu{(\hat{\mu})}$ is obtained from the true model $\mathcal{G}$. Note that this mismatch is one key difference from the single-agent setting and the above proof for the first term. By Lemma 18, it holds that

where uses the norm-like triangle-inequality property of $\sqrt{{Var}_{P}{(V)}}$ and triangle inequality, is due to Lemma 11, and the facts that $\sqrt{{Var}_{P}{(X)}} \leq {\| X\|}_{\infty}$, ${\|{V^{\hat{\mu}, \ast} - {\hat{V}}^{\hat{\mu},{\nu{(\hat{\mu})}}}}\|}_{\infty} \leq {\|{Q^{\hat{\mu}, \ast} - {\hat{Q}}^{\hat{\mu},{\nu{(\hat{\mu})}}}}\|}_{\infty}$, and Lemma 10. Moreover, notice that

where uses triangle inequality, uses the norm-like triangle inequality of $\sqrt{{Var}_{P}{(V)}}$ and $\sqrt{{Var}_{\hat{P}}{(V)}}$, and the fact ${|{\sqrt{X} - \sqrt{Y}}|} \leq \sqrt{|{X - Y}|}$ for ${X,Y} \geq 0$, and uses $\sqrt{{Var}_{P}{(X)}} \leq {\| X\|}_{\infty}$ and the definition of $\parallel \cdot \parallel_{\infty}$. In addition, we know that with probability at least $1 - \delta$,

due to Hoeffding bound and ${\| V^{\ast}\|}_{\infty} \leq {1/{({1 - \gamma})}}$. Combining and (4.5) yields

Solving for ${\|{Q^{\hat{\mu}, \ast} - {\hat{Q}}^{\hat{\mu},{\nu{(\hat{\mu})}}}}\|}_{\infty}$ further leads to

for some absolute constant $c$.

Now we substitute (4.5) and (4.5) into, to complete the bound in. If the first term in the $\max$ in is larger, and noticing that the choice of $N$ in the theorem can make $\alpha_{\delta,N}^{\prime} < {1/5}$ (4.5), and Lemma 19 together lead to

with some absolute constant $c$, where we have replaced the term $\log{({1/{({1 - \gamma})}^{2}})}$ in the bounds for ${\|{Q^{\ast} - {\hat{Q}}^{\mu^{\ast}, \ast}}\|}_{\infty}$ and ${\|{Q^{\ast} - {\hat{Q}}^{\ast,\nu^{\ast}}}\|}_{\infty}$ in Lemma 19 (including that in the definition of $\alpha_{\delta,N}$) by $\log{({{({C + 1})}/{({1 - \gamma})}^{4}})}$, a larger number. If the second term in the $\max$ in is larger (4.5), and Lemma 19 together yield

where we have used the fact that $\alpha_{\delta,N}^{\prime} < {1/5}$. Taking infinity norm on both sides and solving for ${\|{V^{\hat{\mu}, \ast} - V^{\ast}}\|}_{\infty}$, we have

with some absolute constant $c$ (which can be different from that in (4.5)). Using the choice of $N$ in the theorem, and combining (4.5) and, we finally have ${V^{\ast} - V^{\hat{\mu}, \ast}} \leq {\epsilon + {{4\epsilon_{opt}}/{({1 - \gamma})}}}$. Note that on the right-hand side of, the $N$ that makes the third term to be $\mathcal{O}{(\epsilon)}$ is $\overset{\sim}{\mathcal{O}}{({1/{\lbrack{{({1 - \gamma})}^{8/3}\epsilon^{4/3}}\rbrack}})}$, which is dominated by $\overset{\sim}{\mathcal{O}}{({1/{\lbrack{{({1 - \gamma})}^{3}\epsilon^{2}}\rbrack}})}$ when $\epsilon \in {(0,{1/{({1 - \gamma})}^{1/2}}\rbrack}$. In addition, to make $\alpha_{\delta,N}^{\prime} < {1/5}$, $N$ should be larger than $\overset{\sim}{\mathcal{O}}{({1/{({1 - \gamma})}^{2}})}$, which is consistent with both the first and third terms on the right-hand side of to be $\overset{\sim}{\mathcal{O}}{({1/{({1 - \gamma})}^{1/2}})}$, determining the allowed range of $\epsilon$ to be $(0,{1/{({1 - \gamma})}^{1/2}}\rbrack$. This proves the first bound in the theorem.

The proof for completing the bound in is analogous: using Lemmas 18 and 9 ‣ 4.1 Important Lemmas ‣ 4 Proofs ‣ Model-Based Multi-Agent RL in Zero-Sum Markov Games with Near-Optimal Sample Complexity") to bound ${\|{Q^{\ast,\hat{\nu}} - {\hat{Q}}^{\ast,\hat{\nu}}}\|}_{\infty}$, which is then substituted into. This completes the proof.

## Concluding Remarks

In this paper, we have established the first (near-)minimax optimal sample complexity for model-based MARL, when a generative model is available. Our setting was focused on the basic model in MARL --- infinite-horizon discounted two-player zero-sum Markov games. By noticing that reward is not used in the sampling process of this model-based approach, we have separated the reward-aware and reward-agnostic cases, and established sample complexity lower bounds correspondingly, a unique separation in the multi-agent context. We have then shown that this simple model-based approach is near-minimax optimal in the reward-aware case, with only a gap in the dependence on ${|\mathcal{A}|},{|\mathcal{B}|}$; and is indeed minimax-optimal in the reward-agnostic case. This separation and the (near-)optimal results have not only justified the sample-efficiency of this simple approach, but also reflected both its power (easily handling multiple reward functions known in hindsight), and its limitation (less adaptive and can hardly achieve the optimal $\overset{\sim}{\mathcal{O}}{({{|\mathcal{A}|} + {|\mathcal{B}|}})}$). We believe that our results may shed light on the choice of model-free and model-based approaches in various MARL scenarios in practice.

Our results naturally open up the following interesting future directions. First, besides the turn-based setting in Sidford et al. and the episodic setting in the concurrent work Bai et al., the minimax-optimal sample complexity in *all* parameters for *model-free* algorithms is still open. As discussed in §3, in the reward-aware case, the $\overset{\sim}{\Omega}{({{|\mathcal{A}|} + {|\mathcal{B}|}})}$ lower bound may only be attainable by model-free ones. It would be interesting to compare the results with our model-based ones, in both reward-aware and reward-agnostic cases, to better understand their pros and cons in various MARL settings. It would also be interesting to explore the (near-)optimal sample complexity or regret of model-based approaches in other MARL scenarios, such as when no generative model is available, episodic and average-reward settings, general-sum Markov games, and the setting with function approximation.
