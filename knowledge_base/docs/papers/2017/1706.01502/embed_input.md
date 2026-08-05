<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

UCB Exploration via Q-Ensembles

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We show how an ensemble of Q^*-functions can be leveraged for more effective exploration in deep reinforcement learning. We build on well established algorithms from the bandit setting, and adapt them to the Q-learning setting. We propose an exploration strategy based on upper-confidence bounds (UCB). Our experiments show significant gains on the Atari benchmark.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep reinforcement learning seeks to learn mappings from high-dimensional observations to actions. Deep $Q$-learning ([mnih2015human]) is a leading technique that has been used successfully, especially for video game benchmarks. However, fundamental challenges remain, for example, improving sample efficiency and ensuring convergence to high quality solutions. Provably optimal solutions exist in the bandit setting and for small MDPs, and at the core of these solutions are exploration schemes. However these provably optimal exploration techniques do not extend to deep RL in a straightforward way. [osband2016deep]) is a previous attempt at adapting a theoretically verified approach to deep RL. In particular, it draws inspiration from posterior sampling for reinforcement learning (PSRL, [osband2013more,osband2016posterior]), which has near-optimal regret bounds. PSRL samples an MDP from its posterior each episode and exactly solves $Q^*$, its optimal $Q$-function. However, in high-dimensional settings, both approximating the posterior over MDPs and solving the sampled MDP are intractable.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Bootstrapped DQN avoids having to establish and sample from the posterior over MDPs by instead approximating the posterior over $Q^*$. In addition, bootstrapped DQN uses a multi-headed neural network to represent the $Q$-ensemble. While the authors proposed bootstrapping to estimate the posterior distribution, their empirical findings show best performance is attained by simply relying on different initializations for the different heads, not requiring the sampling-with-replacement process that is prescribed by bootstrapping.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we design new algorithms that build on the $Q$-ensemble approach from [osband2016deep]. However, instead of using posterior sampling for exploration, we use the uncertainty estimates from the $Q$-ensemble. Specifically, we propose the UCB exploration strategy. This strategy is inspired by established UCB algorithms in the bandit setting and constructs uncertainty estimates of the $Q$-values. In this strategy, agents are optimistic and take actions with the highest UCB. We demonstrate that our algorithms significantly improve performance on the Atari benchmark.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Exploration in reinforcement learning", "weight": 1.0} -->

A notable early optimality result in reinforcement learning was the proof by Watkins and Dayan [watkins1989learning,watkins1992q] that an online $Q$-learning algorithm is guaranteed to converge to the optimal policy, provided that every state is visited an infinite number of times. However, the convergence of Watkins' Q-learning can be prohibitively slow in MDPs where $\epsilon$-greedy action selection explores state space randomly. Later work developed reinforcement learning algorithms with provably fast (polynomial-time) convergence ([kearns2002near,brafman2002r,strehl2006pac]). At the core of these provably-optimal learning methods is some exploration strategy, which actively encourages the agent to visit novel state-action pairs. For example, R-MAX optimistically assumes that infrequently-visited states provide maximal reward, and delayed $Q$-learning initializes the $Q$-function with high values to ensure that each state-action is chosen enough times to drive the value down.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Exploration in reinforcement learning", "weight": 1.0} -->

Since the theoretically sound RL algorithms are not computationally practical in the deep RL setting, deep RL implementations often use simple exploration methods such as $\epsilon$-greedy and Boltzmann exploration, which are often sample-inefficient and fail to find good policies. One common approach of exploration in deep RL is to construct an exploration bonus, which adds a reward for visiting state-action pairs that are deemed to be novel or informative. In particular, several prior methods define an exploration bonus based on a density model or dynamics model. Examples include VIME by [houthooft2016vime], which uses variational inference on the forward-dynamics model, and [tang2016exploration], [bellemare2016unifying], [ostrovski2017count], [fu2017ex2]. While these methods yield successful exploration in some problems, a major drawback is that this exploration bonus does not depend on the rewards, so the exploration may focus on irrelevant aspects of the environment, which are unrelated to reward.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Bayesian reinforcement learning", "weight": 1.0} -->

Earlier works on Bayesian reinforcement learning include [dearden1998bayesian, dearden1999model]. [dearden1998bayesian] studied Bayesian $Q$-learning in the model-free setting and learned the distribution of $Q^*$-values through Bayesian updates. The prior and posterior specification relied on several simplifying assumptions, some of which are not compatible with the MDP setting. [dearden1999model] took a model-based approach that updates the posterior distribution of the MDP. The algorithm samples from the MDP posterior multiple times and solving the $Q^*$ values at every step. This approach is only feasible for RL problems with very small state space and action space. [strens2000bayesian] proposed posterior sampling for reinforcement learning (PSRL). PSRL instead takes a single sample of the MDP from the posterior in each episode and solves the $Q^*$ values. Recent works including [osband2013more] and [osband2016posterior] established near-optimal Bayesian regret bounds for episodic RL.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Bayesian reinforcement learning", "weight": 1.0} -->

[sorg2012variance]models the environment and constructs exploration bonus from variance of model parameters. These methods are experimented on low dimensional problems only, because the computational cost of these methods is intractable for high dimensional RL.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Bootstrapped DQN", "weight": 1.0} -->

Inspired by PSRL, but wanting to reduce computational cost, prior work developed approximate methods. [osband2014generalization] proposed randomized least-square value iteration for linearly-parameterized value functions. Bootstrapped DQN [osband2016deep] applies to $Q$-functions parameterized by deep neural networks. Bootstrapped DQN ([osband2016deep]) maintains a $Q$-ensemble, represented by a multi-head neural net structure to parameterize $K \in \mathbb{N}_+$ $Q$-functions. This multi-head structure shares the convolution layers but includes multiple heads, each of which defines a $Q$-function $Q_k$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Bootstrapped DQN", "weight": 1.0} -->

Bootstrapped DQN diversifies the $Q$-ensemble through two mechanisms. The first mechanism is independent initialization. The second mechanism applies different samples to train each $Q$-function. These $Q$-functions can be trained simultaneously by combining their loss functions with the help of a random mask $m_{\tau} \in \mathbb{R}_+^K$ $$L = \sum\nolimits_{\tau \in B_{\mathrm{mini}} }\sum\nolimits_{k=1}^K m_{\tau}^k \cdot (Q^k(s, a; \theta) - y_{\tau}^{Q_k})^2,$$ where $y_{\tau}^{Q_k}$ is the target of the $k$th $Q$-function. Thus, the transition $\tau$ updates $Q_k$ only if $m_{\tau}^k$ is nonzero.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Bootstrapped DQN", "weight": 1.0} -->

To avoid the overestimation issue in DQN, bootstrapped DQN calculates the target value $y_{\tau}^{Q_k}$ using the approach of Double DQN ([van2016deep]), such that the current $Q_k(\cdot; \theta_t)$ network determines the optimal action and the target network $Q_k(\cdot; \theta^-)$ estimates the value $$y_{\tau}^{Q_k} = r + \gamma \max_a Q^k(s', \argmax_a Q_k(s', a; \theta_t); \theta^-).$$ In their experiments on Atari games, [osband2016deep] set the mask $m_{\tau}=(1, \dots, 1)$ such that all $\{Q_k\}$ are trained with the same samples and their only difference is initialization.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Bootstrapped DQN", "weight": 1.0} -->

Bootstrapped DQN picks one $Q_k$ uniformly at random at the start of an episode and follows the greedy action $a_t = \argmax_a Q_k(s_t, a)$ for the whole episode.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Approximating Bayesian $\\boldsymbol{Q}$-learning with $\\boldsymbol{Q}$-Ensembles", "weight": 1.0} -->

Ignoring computational costs, the ideal Bayesian approach to reinforcement learning is to maintain a posterior over the MDP. However, with limited computation and model capacity, it is more tractable to maintain a posterior of the $Q^*$-function. In this section, we first derive a posterior update formula for the $Q^*$-function under full exploration assumption and this formula turns out to depend on the transition Markov chain (section:bayes-Q). The Bellman equation emerges as an approximation of the log-likelihood. This motivates using a $Q$-ensemble as a particle-based approach to approximate the posterior over $Q^*$-function and an Ensemble Voting algorithm (section:approximation).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Bayesian update for $\\boldsymbol{Q}^*$", "weight": 1.0} -->

An MDP is specified by the transition probability $T$ and the reward function $R$. Unlike prior works outlined in Section[section:bayesian] which learned the posterior of the MDP, we will consider the joint distribution over $(Q^*, T)$. Note that $R$ can be recovered from $Q^*$ given $T$. So $(Q^*, T)$ determines a unique MDP. In this section, we assume that the agent samples $(s, a)$ according to a fixed distribution. The corresponding reward $r$ and next state $s'$ given by the MDP append to $(s, a)$ to form a transition $\tau = (s, a, r, s’)$, for updating the posterior of $(Q^*, T)$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Bayesian update for $\\boldsymbol{Q}^*$", "weight": 1.0} -->

Recall that the $Q^*$-function satisfies the Bellman equation $$Q(s, a) = r + \mathbb{E}_{s' \sim T(\cdot |s, a)} \left[\gamma \max_{a'}Q(s', a') \right].$$ Denote the joint prior distribution as $p(Q^*, T)$ and the posterior as $\tilde{p}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Bayesian update for $\\boldsymbol{Q}^*$", "weight": 1.0} -->

We apply Bayes' formula to expand the posterior: \tilde{p}(Q^*, T | \tau) & = \frac{ p(\tau | Q^*, T) \cdot p(Q^*, T) }{Z(\tau)} \nonumber \\& = \frac{p(Q^*, T) \cdot p(s' | Q^*, T, (s, a)) \cdot p(r | Q^*, T, (s, a, s')) \cdot p(s,a) }{Z(\tau)}, where $Z(\tau)$ is a normalizing constant and the second equality is because $s$ and $a$ are sampled randomly from $\mathcal{S}$ and $\mathcal{A}$. Next, we calculate the two conditional probabilities in [eqn:bayes]. First, where the first equality is because given $T$, $Q^*$ does not influence the transition.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Bayesian update for $\\boldsymbol{Q}^*$", "weight": 1.0} -->

Second, & = \mathbbm{1}_{\{ Q^*(s, a) = r + \gamma \cdot \mathbb{E}_{s'' \sim T(\cdot|s, a)} \max_{a'} Q^*(s'', a') \}} \nonumber\\where $\mathbbm{1}_{\{\cdot\}}$ is the indicator function and in the last equation we abbreviate it as $\mathbbm{1}(Q^*, T)$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Bayesian update for $\\boldsymbol{Q}^*$", "weight": 1.0} -->

Substituting[eqn:cond-1] and [eqn:cond-2] into [eqn:bayes], we obtain the joint posterior of $Q^*$ and $T$ after observing an additional randomly sampled transition $\tau$ $$\tilde{p}(Q^*, T | \tau) = \frac{p(Q^*, T) \cdot T(s'|s, a) \cdot p(s,a)}{Z(\tau)} \cdot \mathbbm{1}(Q^*, T).$$ We point out that the exact $Q^*$-posterior update [eqn:bayes-update] is intractable in high-dimensional RL due to the large space of $(Q^*, T)$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "$\\boldsymbol{Q}$-learning with $\\boldsymbol{Q}$-ensembles", "weight": 1.0} -->

In this section, we make several approximations to the $Q^*$-posterior update and derive a tractable algorithm. First, we approximate the prior of $Q^*$ by sampling $K \in \mathbb{N}_+$ independently initialized $Q^*$-functions $\{Q_k\}_{k=1}^K$. Next, we update them as more transitions are sampled. The resulting $\{Q_k\}$ approximate samples drawn from the posterior. The agent chooses the action by taking a majority vote from the actions determined by each $Q_k$. We display our method, Ensemble Voting, in Algorithm[algo:approx-bayes-q].

<!-- chunk {"id": "body-0021", "role": "body", "section": "$\\boldsymbol{Q}$-learning with $\\boldsymbol{Q}$-ensembles", "weight": 1.0} -->

We derive the update rule for $\{Q_k\}$ after observing a new transition $\tau=(s, a, r, s')$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "$\\boldsymbol{Q}$-learning with $\\boldsymbol{Q}$-ensembles", "weight": 1.0} -->

At iteration $i$, given $Q^*=Q_{k, i}$ the joint probability of $(Q^*, T)$ factors into Substitute [eqn:prior-factor] into [eqn:bayes-update] and we obtain the corresponding posterior for each $Q_{k, i+1}$ at iteration $i+1$ as \tilde{p}(Q_{k, i+1}, T|\tau) &= \frac{p(T|Q_{k, i}) \cdot T(s'|s, a) \cdot p(s, a) }{Z(\tau)} \cdot \mathbbm{1}(Q_{k, i+1}, T).\\\tilde{p}(Q_{k, i+1} | \tau) &= \int_{T} \tilde{p}(Q_{k, i+1}, T|\tau) \mathrm{d} T = p(s, a) \cdot \int_{T}

<!-- chunk {"id": "body-0023", "role": "body", "section": "$\\boldsymbol{Q}$-learning with $\\boldsymbol{Q}$-ensembles", "weight": 1.0} -->

where we apply a limit representation of the indicator function in the third equation. The fourth equation is due to the bounded convergence theorem. The inequality is Jensen's inequality. The last equation [eqn:ind-hold]replaces the limit with an indicator function.

<!-- chunk {"id": "body-0024", "role": "body", "section": "$\\boldsymbol{Q}$-learning with $\\boldsymbol{Q}$-ensembles", "weight": 1.0} -->

A sufficient condition for [eqn:update-Q-k] is to maximize the lower-bound of the posterior distribution in [eqn:ind-hold] by ensuring the indicator function in [eqn:ind-hold] to hold.

<!-- chunk {"id": "body-0025", "role": "body", "section": "$\\boldsymbol{Q}$-learning with $\\boldsymbol{Q}$-ensembles", "weight": 1.0} -->

We can replace [eqn:update-Q-k] with the following update $$Q_{k, i+1} \leftarrow \argmin_{Q_{k, i+1}} \operatorname{\mathbb{E}}_{T \sim \tilde{p}(T|Q_{k,i}, \tau)} \big[Q_{k, i+1}(s, a) -\big(r + \gamma \cdot \mathbb{E}_{s'' \sim T(\cdot|s, a)} \max_{a'} Q_{k, i+1}(s'', a') \big) \big]^2.$$ However, [eqn:Q-k] is not tractable because the expectation in [eqn:Q-k] is taken with respect to the posterior $\tilde{p}(T|Q_{k, i}, \tau)$ of the transition $T$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "$\\boldsymbol{Q}$-learning with $\\boldsymbol{Q}$-ensembles", "weight": 1.0} -->

To overcome this challenge, we approximate the posterior update by reusing the one-sample next state $s'$ from $\tau$ such that $$Q_{k, i+1} \leftarrow \argmin_{Q_{k, i+1}} \big[Q_{k, i+1}(s, a) -\big(r + \gamma \cdot \max_{a'} Q_{k, i+1}(s', a') \big) \big]^2.$$ Instead of updating the posterior after each transition, we use an experience replay buffer $B$ to store observed transitions and sample a minibatch $B_{\mathrm{mini}}$ of transitions $(s, a, r, s')$ for each update.

<!-- chunk {"id": "body-0027", "role": "body", "section": "$\\boldsymbol{Q}$-learning with $\\boldsymbol{Q}$-ensembles", "weight": 1.0} -->

In this case, the batched update of each $Q_{k, i}$ to $Q_{k, i+1}$ becomes a standard Bellman update $$Q_{k, i+1} \leftarrow \argmin_{Q_{k, i+1}} \mathbb{E}_{(s, a, r, s') \in B_{\mathrm{mini}}} \big[Q_{k, i+1}(s, a) -\big(r + \gamma \cdot \max_{a'} Q_{k, i+1}(s', a') \big) \big]^2.$$ For stability, Algorithm[algo:approx-bayes-q] also uses a target network for each $Q_{k}$ as in Double DQN in the batched update. We point out that the action choice of Algorithm[algo:approx-bayes-q]is exploitation only. In the next section, we propose two exploration strategies.

<!-- chunk {"id": "body-0028", "role": "body", "section": "$\\boldsymbol{Q}$-learning with $\\boldsymbol{Q}$-ensembles", "weight": 1.0} -->

Input: $K \in \mathbb{N}_+$ copies of independently initialized $Q^*$-functions $\{Q_k\}_{k=1}^K$. Let $B$ be a replay buffer storing transitions for training Obtain initial state from environment $s_0$ step $t=1, \dots$ until end of episode Pick an action according to $a_t = \mathrm{Majority Vote}(\{\argmax_a Q_k(s_t, a)\}_{k=1}^K)$ Execute $a_t$. Receive state $s_{t+1}$ and reward $r_t$ from the environment Add $(s_t, a_t, r_t, s_{t+1})$ to replay buffer $B$ At learning interval, sample random minibatch and update $\{Q_k\}$

<!-- chunk {"id": "body-0029", "role": "body", "section": "UCB Exploration Strategy Using $\\boldsymbol{Q}$-Ensembles", "weight": 1.0} -->

In this section, we propose optimism-based exploration by adapting the UCB algorithms ([auer2002finite, audibert2009exploration]) from the bandit setting. The UCB algorithms maintain an upper-confidence bound for each arm, such that the expected reward from pulling each arm is smaller than this bound with high probability. At every time step, the agent optimistically chooses the arm with the highest UCB. [auer2002finite] constructed the UCB based on empirical reward and the number of times each arm is chosen.

<!-- chunk {"id": "body-0030", "role": "body", "section": "UCB Exploration Strategy Using $\\boldsymbol{Q}$-Ensembles", "weight": 1.0} -->

[audibert2009exploration] incorporated the empirical variance of each arm's reward into the UCB, such that at time step $t$, an arm $A_t$ is pulled according to $$A_t = \argmax_{i}\Big\{ \hat{r}_{i, t} + c_1 \cdot \sqrt{\frac{\hat{V}_{i,t} \log(t) }{n_{i,t}}} + c_2 \cdot \frac{\log(t)}{n_{i, t}} \Big\}$$ where $\hat{r}_{i, t}$ and $\hat{V}_{i,t}$ are the empirical reward and variance of arm $i$ at time $t$, $n_{i, t}$ is the number of times arm $i$ has been pulled up to time $t$, and $c_1, c_2$are positive constants.

<!-- chunk {"id": "body-0031", "role": "body", "section": "UCB Exploration Strategy Using $\\boldsymbol{Q}$-Ensembles", "weight": 1.0} -->

We extend the intuition of UCB algorithms to the RL setting. Using the outputs of the $\{Q_k\}$ functions, we construct a UCB by adding the empirical standard deviation $\tilde{\sigma}(s_t, a)$ of $\{Q_k(s_t, a)\}_{k=1}^K$ to the empirical mean $\tilde{\mu}(s_t, a)$ of $\{Q_k(s_t, a)\}_{k=1}^K$. The agent chooses the action that maximizes this UCB $$a_t \in \argmax_a \big\{ \tilde{\mu}(s_t, a)+ \lambda \cdot \tilde{\sigma}(s_t, a)\big\},$$ where $\lambda \in \mathbb{R}_+$is a hyperparameter. [algo:second-improv], which incorporates the UCB exploration. The hyperparemeter $\lambda$ controls the degrees of exploration.

<!-- chunk {"id": "body-0032", "role": "body", "section": "UCB Exploration Strategy Using $\\boldsymbol{Q}$-Ensembles", "weight": 1.0} -->

In Section[section:exp], we compare the performance of our algorithms on Atari games using a consistent set of parameters.

<!-- chunk {"id": "body-0033", "role": "body", "section": "UCB Exploration Strategy Using $\\boldsymbol{Q}$-Ensembles", "weight": 1.0} -->

UCB Exploration with $Q$-Ensembles Input: Value function networks $Q$ with $K$ outputs $\{Q_k\}_{k=1}^K$. Hyperparameter $\lambda$. Let $B$ be a replay buffer storing experience for training. Obtain initial state from environment $s_0$ step $t=1, \dots$ until end of episode Pick an action according to $a_t \in \argmax_a \big\{ \tilde{\mu}(s_t, a)+ \lambda \cdot \tilde{\sigma}(s_t, a)\big\}$ Receive state $s_{t+1}$ and reward $r_t$ from environment, having taken action $a_t$ Add $(s_t, a_t, r_t, s_{t+1})$ to replay buffer $B$ At learning interval, sample random minibatch and update $\{Q_k\}$ according to[eqn:approx-Q-k-update]

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiment", "weight": 1.0} -->

- does Ensemble Voting, Algorithm[algo:approx-bayes-q], improve upon existing algorithms including Double DQN and bootstrapped DQN? - is the proposed UCB exploration strategy of Algorithm[algo:second-improv] effective in improving learning compared to Algorithm[algo:approx-bayes-q]? - how does UCB exploration compare with prior exploration methods such as the count-based exploration method of [bellemare2016unifying]?

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiment", "weight": 1.0} -->

We evaluate the algorithms on each Atari game of the Arcade Learning Environment ([bellemare2013arcade]). We use the multi-head neural net architecture of [osband2016deep]. We fix the common hyperparameters of all algorithms based on a well-tuned double DQN implementation, which uses the Adam optimizer ([kingma2014adam]), different learning rate and exploration schedules compared to [mnih2015human]. Appendix [app:param] tabulates the hyperparameters. The number of $\{Q_k\}$ functions is $K=10$. Experiments are conducted on the OpenAI Gym platform ([brockman2016openai]) and trained with $40$ million frames and $2$trials on each game.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiment", "weight": 1.0} -->

- we compare Algorithm[algo:approx-bayes-q] against Double DQN and bootstrapped DQN, - we isolate the impact of UCB exploration by comparing Algorithm[algo:second-improv] with $\lambda=0.1$, denoted as $\texttt{ucb exploration}$, against Algorithm[algo:approx-bayes-q]. - we compare Algorithm[algo:approx-bayes-q] and Algorithm[algo:second-improv] with the count-based exploration method of [bellemare2016unifying]. - we aggregate the comparison according to different categories of games, to understand when our methods are suprior.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiment", "weight": 1.0} -->

Figure[fig:normalized] compares the normalized learning curves of all algorithms across Atari games. Overall, Ensemble Voting, Algorithm[algo:approx-bayes-q], outperforms both Double DQN and bootstrapped DQN. With exploration, $\texttt{ucb exploration}$improves further by outperforming Ensemble Voting. [app:table], we tabulate detailed results that compare our algorithms, Ensemble Voting and $\texttt{ucb exploration}$, against prior methods. In Table[tab:my\_label], we tabulate the maximal mean reward in $100$ consecutive episodes for Ensemble Voting, $\texttt{ucb exploration}$, bootstrapped DQN and Double DQN. Without exploration, Ensemble Voting already achieves higher maximal mean reward than both Double DQN and bootstrapped DQN in a majority of Atari games. $\texttt{ucb exploration}$ achieves the highest maximal mean reward among these four algorithms in 30 games out of the total 49 games evaluated. Figure[fig:all] displays the learning curves of these five algorithms on a set of six Atari games.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiment", "weight": 1.0} -->

Ensemble Voting outperforms Double DQN and bootstrapped DQN. $\texttt{ucb exploration}$outperforms Ensemble Voting. [tab:compare\_with\_bellemare], we compare our proposed methods with the count-based exploration method A3C+ of [bellemare2016unifying]based on their published results of A3C+ trained with 200 million frames. We point out that even though our methods were trained with only 40 million frames, much less than A3C+'s 200 million frames, UCB exploration achieves the highest average reward in 28 games, Ensemble Voting in 10 games, and A3C+ in 10 games. Our approach outperforms A3C+.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiment", "weight": 1.0} -->

Finally to understand why and when the proposed methods are superior, we aggregate the comparison results according to four categories: Human Optimal, Score Explicit, Dense Reward, and Sparse Reward. These categories follow the taxonomy in Table 1 of [ostrovski2017count]. Out of all games evaluated, 23 games are Human Optimal, 8 are Score Explicit, 8 are Dense Reward, and 5 are Sparse Reward. The comparison results are tabulated in Table[tab:compare\_each\_category], where we see $\texttt{ucb exploration}$ achieves top performance in more games than Ensemble Voting, Double DQN, and Bootstrapped DQN in the categories of Human Optimal, Score Explicit, and Dense Reward. In Sparse Reward, both $\texttt{ucb exploration}$ and Ensemble Voting achieve best performance in 2 games out of total of 5. Thus, we conclude that $\texttt{ucb exploration}$improves prior methods consistently across different game categories within the Arcade Learning Environment.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiment", "weight": 1.0} -->

Comparison of algorithms in normalized learning curve. The normalized learning curve is calculated as follows: first, we normalize learning curves for all algorithms in the same game to the interval $$; next, average the normalized learning curve from all games for each algorithm.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experiment", "weight": 1.0} -->

Comparison of UCB Exploration and Ensemble Voting against Double DQN and Bootstrapped DQN.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We proposed a $Q$-ensemble approach to deep $Q$-learning, a computationally practical algorithm inspired by Bayesian reinforcement learning that outperforms Double DQN and bootstrapped DQN, as evaluated on Atari. The key ingredient is the UCB exploration strategy, inspired by bandit algorithms. Our experiments show that the exploration strategy achieves improved learning performance on the majority of Atari games.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Hyperparameters", "weight": 1.0} -->

We tabulate the hyperparameters in our well-tuned implementation of double DQN in Table[table:param]: | hyperparameter | value | descriptions | Double DQN hyperparameters. These hyperparameters are selected based on performances of seven Atari games: Beam Rider, Breakout, Pong, Enduro, Qbert, Seaquest, and Space Invaders. $Interp(\cdot, \cdot)$ is linear interpolation between two values.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Results tables", "weight": 1.0} -->

| | Bootstrapped DQN | Double DQN | Ensemble Voting | UCB-Exploration | Comparison of maximal mean rewards achieved by agents. Maximal mean reward is calculated in a window of $100$ consecutive episodes. Bold denotes the highest value in each row.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Results tables", "weight": 1.0} -->

| | Ensemble Voting | UCB-Exploration | A3C+ | Comparison of Ensemble Voting, UCB Exploration, both trained with 40 million frames and A3C+ of, trained with 200 million frames | Category | Total | Bootstrapped DQN | Double DQN | Ensemble Voting | UCB-Exploration | Comparison of each method across different game categories. The Atari games are separated into four categories: human optimal, score explicit, dense reward, and sparse reward. In each row, we present the number of games in this category, the total number of games where each algorithm achieves the optimal performance according to Table tab:my\_label. The game categories follow the taxonomy in Table 1 of

<!-- chunk {"id": "body-0046", "role": "body", "section": "InfoGain exploration", "weight": 1.0} -->

In this section, we also studied an InfoGain exploration bonus, which encourages agents to gain information about the $Q^*$-function and examine its effectiveness. We found it had some benefits on top of Ensemble Voting, but no uniform additional benefits once already using Q-ensembles on top of Double DQN. We describe the approach and our experimental findings here. [sun2011planning], we define the information gain from observing an additional transition $\tau_n$ as $$H_{\tau_t| \tau_1, \dots, \tau_{n-1}} = D_{KL}(\tilde{p}(Q^*|\tau_1, \dots, \tau_n) || \tilde{p}(Q^*|\tau_1, \dots, \tau_{n-1}))$$ where $\tilde{p}(Q^* |\tau_1, \dots, \tau_n)$ is the posterior distribution of $Q^*$ after observing a sequence of transitions $(\tau_1, \dots, \tau_n)$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "InfoGain exploration", "weight": 1.0} -->

The total information gain is $$H_{\tau_1, \dots, \tau_N} = \sum\nolimits_{n=1}^N H_{\tau_n| \tau_1, \dots, \tau_{n-1}}.$$ Our Ensemble Voting, Algorithm[algo:approx-bayes-q], does not maintain the posterior $\tilde{p}$, thus we cannot calculate[eqn:info-gain] explicitly. Instead, inspired by [lakshminarayanan2016simple], we define an InfoGain exploration bonus that measures the disagreement among$\{Q_k\}$. Note that $$H_{\tau_1, \dots, \tau_N} + \mathsf{H}(\tilde{p}(Q^*|\tau_1, \dots, \tau_N)) = \mathsf{H}(p(Q^*)),$$ where $\mathsf{H}(\cdot)$ is the entropy.

<!-- chunk {"id": "body-0048", "role": "body", "section": "InfoGain exploration", "weight": 1.0} -->

If $H_{\tau_1, \dots, \tau_N}$ is small, then the posterior distribution has high entropy and high residual information. Since $\{Q_k\}$ are approximate samples from the posterior, high entropy of the posterior leads to large discrepancy among $\{Q_k\}$. Thus, the exploration bonus is monotonous with respect to the residual information in the posterior $\mathsf{H}(\tilde{p}(Q^*|\tau_1, \dots, \tau_N))$. We first compute the Boltzmann distribution for each $Q_k$ $$P_{\mathsf{T}, k} (a|s) = \frac{\exp\big(Q_k(s, a)/\mathsf{T}\big)}{\sum\nolimits_{a'} \exp\big(Q_k(s, a')/\mathsf{T}\big)},$$ where $\mathsf{T} > 0$ is a temperature parameter.

<!-- chunk {"id": "body-0049", "role": "body", "section": "InfoGain exploration", "weight": 1.0} -->

+ \rho \cdot b_{\mathsf{T}}(s),$$ where $\rho \in \mathbb{R}_+$is a hyperparameter that controls the degree of exploration.

<!-- chunk {"id": "body-0050", "role": "body", "section": "InfoGain exploration", "weight": 1.0} -->

The exploration bonus $b_{\mathsf{T}}(s_t)$ encourages the agent to explore where $\{Q_k\}$ disagree. The temperature parameter $\mathsf{T}$ controls the sensitivity to discrepancies among $\{Q_k\}$. When $\mathsf{T} \rightarrow +\infty$, $\{P_{\mathsf{T}, k}\}$ converge to the uniform distribution on the action space and $b_{\mathsf{T}}(s) \rightarrow 0$. When $\mathsf{T}$ is small, the differences among $\{Q_k\}$ are magnified and $b_{\mathsf{T}}(s)$is large. [algo:infogain], which incorporates our InfoGain exploration bonus into Algorithm[algo:second-improv]. The hyperparameters $\lambda$, $\mathsf{T}$ and $\rho$vary for each game.

<!-- chunk {"id": "body-0051", "role": "body", "section": "InfoGain exploration", "weight": 1.0} -->

UCB + InfoGain Exploration with $Q$-Ensembles Input: Value function networks $Q$ with $K$ outputs $\{Q_k\}_{k=1}^K$. Hyperparameters $\mathsf{T}, \lambda$, and $\rho$. Let $B$ be a replay buffer storing experience for training.

<!-- chunk {"id": "body-0052", "role": "body", "section": "InfoGain exploration", "weight": 1.0} -->

Obtain initial state from environment $s_0$ step $t=1, \dots$ until end of episode Pick an action according to $a_t \in \argmax_a \big\{ \tilde{\mu}(s_t, a)+ \lambda \cdot \tilde{\sigma}(s_t, a)\big\}$ Receive state $s_{t+1}$ and reward $r_t$ from environment, having taken action $a_t$ Calculate exploration bonus $b_{\mathsf{T}}(s_t)$ according to [eqn:bonus] Add $(s_t, a_t, r_t + \rho \cdot b_{\mathsf{T}}(s_t), s_{t+1})$ to replay buffer $B$ At learning interval, sample random minibatch and update $\{Q_k\}$

<!-- chunk {"id": "body-0053", "role": "body", "section": "Performance of UCB+InfoGain exploration", "weight": 1.0} -->

We demonstrate the performance of the combined UCB+InfoGain exploration in Figure[fig:normalized\_with\_infogain] and Figure[fig:normalized\_with\_infogain]. We augment the previous figures in Section[section:exp] with the performance of $\texttt{ucb+infogain exploration}$, where we set $\lambda=0.1, \rho=1$, and $\mathsf{T}=1$ in Algorithm[algo:infogain]. [fig:normalized\_with\_infogain]shows that combining UCB and InfoGain exploration does not lead to uniform improvement in the normalized learning curve.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Performance of UCB+InfoGain exploration", "weight": 1.0} -->

At the individual game level, Figure [fig:normalized\_with\_infogain] shows that the impact of InfoGain exploration varies. UCB exploration achieves sufficient exploration in games including Demon Attack and Kangaroo and Riverraid, while InfoGain exploration further improves learning on Enduro, Seaquest, and Up N Down. The effect of InfoGain exploration depends on the choice of the temperature $\mathsf{T}$. The optimal temperature parameter varies across games. In Figure[fig:temperature], we display the behavior of $\texttt{ucb+infogain exploration}$with different temperature values. Thus, we see the InfoGain exploration bonus, tuned with the appropriate temperature parameter, can lead to improved learning for games that require extra exploration, such as ChopperCommand, KungFuMaster, Seaquest, UpNDown.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Performance of UCB+InfoGain exploration", "weight": 1.0} -->

Comparison of all algorithms in normalized curve. The normalized learning curve is calculated as follows: first, we normalize learning curves for all algorithms in the same game to the interval $$; next, average the normalized learning curve from all games for each algorithm.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Performance of UCB+InfoGain exploration", "weight": 1.0} -->

Comparison of algorithms against Double DQN and bootstrapped DQN.

<!-- chunk {"id": "body-0057", "role": "body", "section": "UCB+InfoGain exploration with different temperatures", "weight": 1.0} -->

Comparison of UCB+InfoGain exploration with different temperatures versus UCB exploration.
