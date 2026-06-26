<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Rainbow: Combining Improvements in Deep Reinforcement Learning

Topics include Reinforcement learning, Benchmarks, Learning, Rainbow.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The deep reinforcement learning community has made several independent improvements to the DQN algorithm. However, it is unclear which of these extensions are complementary and can be fruitfully combined. This paper examines six extensions to the DQN algorithm and empirically studies their combination. Our experiments show that the combination provides state-of-the-art performance on the Atari 2600 benchmark, both in terms of data efficiency and final performance. We also provide results from a detailed ablation study that shows the contribution of each component to overall performance.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The many recent successes in scaling reinforcement learning (RL) to complex sequential decision-making problems were kick-started by the Deep Q-Networks algorithm (DQN; ? ?, ?). Its combination of Q-learning with convolutional neural networks and experience replay enabled it to learn, from raw pixels, how to play many Atari games at human-level performance. Since then, many extensions have been proposed that enhance its speed or stability.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Double DQN (DDQN; ? ?) addresses an overestimation bias of Q-learning (?), by decoupling selection and evaluation of the bootstrap action. Prioritized experience replay (?) improves data efficiency, by replaying more often transitions from which there is more to learn. The dueling network architecture (?) helps to generalize across actions by separately representing state values and action advantages. Learning from multi-step bootstrap targets (?; ?), as used in A3C (?), shifts the bias-variance trade-off and helps to propagate newly observed rewards faster to earlier visited states. Distributional Q-learning (?) learns a categorical distribution of discounted returns, instead of estimating the mean. Noisy DQN (?) uses stochastic network layers for exploration. This list is, of course, far from exhaustive.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Each of these algorithms enables substantial performance improvements in isolation. Since they do so by addressing radically different issues, and since they build on a shared framework, they could plausibly be combined. In some cases this has been done: Prioritized DDQN and Dueling DDQN both use double Q-learning, and Dueling DDQN was also combined with prioritized experience replay. In this paper we propose to study an agent that combines all the aforementioned ingredients. We show how these different ideas can be integrated, and that they are indeed largely complementary. In fact, their combination results in new state-of-the-art results on the benchmark suite of 57 Atari 2600 games from the Arcade Learning Environment (?), both in terms of data efficiency and of final performance. Finally we show results from ablation studies to help understand the contributions of the different components.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Agents and environments", "weight": 1.0} -->

At each discrete time step $t = {0,1,{2\ldots}}$, the environment provides the agent with an observation $S_{t}$, the agent responds by selecting an action $A_{t}$, and then the environment provides the next reward $R_{t + 1}$, discount $\gamma_{t + 1}$, and state $S_{t + 1}$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Agents and environments", "weight": 1.0} -->

This interaction is formalized as a Markov Decision Process, or MDP, which is a tuple $\langle\mathcal{S},\mathcal{A},T,r,\gamma\rangle$, where $\mathcal{S}$ is a finite set of states, $\mathcal{A}$ is a finite set of actions, $T{(s,a,s')} = P{\lbrack S_{t + 1} = s' \mid S_{t} = s,A_{t} = a\rbrack}$ is the (stochastic) transition function, ${r{(s,a)}} = {{\mathbb{E}}{\lbrack{{{R_{t + 1} \mid S_{t}} = s},{A_{t} = a}}\rbrack}}$ is the reward function, and $\gamma \in {\lbrack 0,1\rbrack}$ is a discount factor.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Agents and environments", "weight": 1.0} -->

In our experiments MDPs will be episodic with a constant $\gamma_{t} = \gamma$, except on episode termination where $\gamma_{t} = 0$, but the algorithms are expressed in the general form.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Agents and environments", "weight": 1.0} -->

On the agent side, action selection is given by a policy $\pi$ that defines a probability distribution over actions for each state. From the state $S_{t}$ encountered at time $t$, we define the discounted return $G_{t} = {\sum_{k = 0}^{\infty}{\gamma_{t}^{(k)}R_{t + k + 1}}}$ as the discounted sum of future rewards collected by the agent, where the discount for a reward $k$ steps in the future is given by the product of discounts before that time, $\gamma_{t}^{(k)} = {\prod_{i = 1}^{k}\gamma_{t + i}}$. An agent aims to maximize the expected discounted return by finding a good policy.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Agents and environments", "weight": 1.0} -->

The policy may be learned directly, or it may be constructed as a function of some other learned quantities. In value-based reinforcement learning, the agent learns an estimate of the expected discounted return, or value, when following a policy $\pi$ starting from a given state, ${v^{\pi}{(s)}} = {E_{\pi}{\lbrack{\left. G_{t} \middle| S_{t} \right. = s}\rbrack}}$, or state-action pair, ${q^{\pi}{(s,a)}} = {E_{\pi}{\lbrack{{\left. G_{t} \middle| S_{t} \right. = s},{A_{t} = a}}\rbrack}}$. A common way of deriving a new policy from a state-action value function is to act $\epsilon$-greedily with respect to the action values.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Agents and environments", "weight": 1.0} -->

This corresponds to taking the action with the highest value (the greedy action) with probability $({1 - \epsilon})$, and to otherwise act uniformly at random with probability $\epsilon$. Policies of this kind are used to introduce a form of exploration: by randomly selecting actions that are sub-optimal according to its current estimates, the agent can discover and correct its estimates when appropriate. The main limitation is that it is difficult to discover alternative courses of action that extend far into the future; this has motivated research on more directed forms of exploration.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Deep reinforcement learning and DQN", "weight": 1.0} -->

Large state and/or action spaces make it intractable to learn Q value estimates for each state and action pair independently. In deep reinforcement learning, we represent the various components of agents, such as policies $\pi{(s,a)}$ or values $q{(s,a)}$, with deep (i.e., multi-layer) neural networks. The parameters of these networks are trained by gradient descent to minimize some suitable loss function.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Deep reinforcement learning and DQN", "weight": 1.0} -->

In DQN (?) deep networks and reinforcement learning were successfully combined by using a convolutional neural net to approximate the action values for a given state $S_{t}$ (which is fed as input to the network in the form of a stack of raw pixel frames). At each step, based on the current state, the agent selects an action $\epsilon$-greedily with respect to the action values, and adds a transition ($S_{t},A_{t},R_{t + 1},\gamma_{t + 1},S_{t + 1}$) to a replay memory buffer (?), that holds the last million transitions. The parameters of the neural network are optimized by using stochastic gradient descent to minimize the loss where $t$ is a time step randomly picked from the replay memory. The gradient of the loss is back-propagated only into the parameters $\theta$ of the online network (which is also used to select actions); the term $\overline{\theta}$ represents the parameters of a target network; a periodic copy of the online network which is not directly optimized.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Deep reinforcement learning and DQN", "weight": 1.0} -->

The optimization is performed using RMSprop (?), a variant of stochastic gradient descent, on mini-batches sampled uniformly from the experience replay. This means that in the loss above, the time index $t$ will be a random time index from the last million transitions, rather than the current time. The use of experience replay and target networks enables relatively stable learning of Q values, and led to super-human performance on several Atari games.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Extensions to DQN", "weight": 1.0} -->

DQN has been an important milestone, but several limitations of this algorithm are now known, and many extensions have been proposed. We propose a selection of six extensions that each have addressed a limitation and improved overall performance. To keep the size of the selection manageable, we picked a set of extensions that address distinct concerns (e.g., just one of the many addressing exploration).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Double Q-learning", "weight": 1.0} -->

Conventional Q-learning is affected by an overestimation bias, due to the maximization step in Equation 1, and this can harm learning. Double Q-learning (?), addresses this overestimation by decoupling, in the maximization performed for the bootstrap target, the selection of the action from its evaluation. It is possible to effectively combine this with DQN (?), using the loss This change was shown to reduce harmful overestimations that were present for DQN, thereby improving performance.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Prioritized replay", "weight": 1.0} -->

DQN samples uniformly from the replay buffer. Ideally, we want to sample more frequently those transitions from which there is much to learn. As a proxy for learning potential, prioritized experience replay (?) samples transitions with probability $p_{t}$ relative to the last encountered absolute TD error: where $\omega$ is a hyper-parameter that determines the shape of the distribution. New transitions are inserted into the replay buffer with maximum priority, providing a bias towards recent transitions. Note that stochastic transitions might also be favoured, even when there is little left to learn about them.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Dueling networks", "weight": 1.0} -->

The dueling network is a neural network architecture designed for value based RL. It features two streams of computation, the value and advantage streams, sharing a convolutional encoder, and merged by a special aggregator (?). This corresponds to the following factorization of action values: where $\xi$, $\eta$, and $\psi$ are, respectively, the parameters of the shared encoder $f_{\xi}$, of the value stream $v_{\eta}$, and of the advantage stream $a_{\psi}$; and $\theta = {\{\xi,\eta,\psi\}}$ is their concatenation.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Multi-step learning", "weight": 1.0} -->

Q-learning accumulates a single reward and then uses the greedy action at the next step to bootstrap. Alternatively, forward-view multi-step targets can be used (?). We define the truncated $n$-step return from a given state $S_{t}$ as A multi-step variant of DQN is then defined by minimizing the alternative loss, Multi-step targets with suitably tuned $n$ often lead to faster learning (?).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Distributional RL", "weight": 1.0} -->

We can learn to approximate the distribution of returns instead of the expected return. Recently Bellemare, Dabney, and Munos proposed to model such distributions with probability masses placed on a discrete support $\mathbf{z}$, where $\mathbf{z}$ is a vector with $N_{\text{atoms}} \in {\mathbb{N}}^{+}$ *atoms*, defined by $z^{i} = {v_{\min} + {{({i - 1})}\frac{v_{\max} - v_{\min}}{N_{\text{atoms}} - 1}}}$ for $i \in {\{ 1,\ldots,N_{\text{atoms}}\}}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Distributional RL", "weight": 1.0} -->

The approximating distribution $d_{t}$ at time $t$ is defined on this support, with the probability mass $p_{\theta}^{i}{(S_{t},A_{t})}$ on each atom $i$, such that $d_{t} = {({\mathbf{z}},{{\mathbf{p}}_{\theta}{(S_{t},A_{t})}})}$. The goal is to update $\theta$ such that this distribution closely matches the actual distribution of returns.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Distributional RL", "weight": 1.0} -->

To learn the probability masses, the key insight is that return distributions satisfy a variant of Bellman's equation. For a given state $S_{t}$ and action $A_{t}$, the distribution of the returns under the optimal policy $\pi^{\ast}$ should match a target distribution defined by taking the distribution for the next state $S_{t + 1}$ and action $a_{t + 1}^{\ast} = {\pi^{\ast}{(S_{t + 1})}}$, contracting it towards zero according to the discount, and shifting it by the reward (or distribution of rewards, in the stochastic case).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Distributional RL", "weight": 1.0} -->

A distributional variant of Q-learning is then derived by first constructing a new support for the target distribution, and then minimizing the Kullbeck-Leibler divergence between the distribution $d_{t}$ and the target distribution $d_{t}' \equiv {({R_{t + 1} + {\gamma_{t + 1}{\mathbf{z}}}},{{\mathbf{p}}_{\overline{\theta}}{(S_{t + 1},{\overline{a}}_{t + 1}^{\ast})}})}$, Here $\Phi_{\mathbf{z}}$ is a L2-projection of the target distribution onto the fixed support $\mathbf{z}$, and ${\overline{a}}_{t + 1}^{\ast} = {{{\arg\max}_{a}q_{\overline{\theta}}}{(S_{t + 1},a)}}$ is the greedy action with respect

<!-- chunk {"id": "body-0024", "role": "body", "section": "Distributional RL", "weight": 1.0} -->

As in the non-distributional case, we can use a frozen copy of the parameters $\overline{\theta}$ to construct the target distribution. The parametrized distribution can be represented by a neural network, as in DQN, but with $N_{\text{atoms}} \times N_{\text{actions}}$ outputs. A softmax is applied independently for each action dimension of the output to ensure that the distribution for each action is appropriately normalized.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Noisy Nets", "weight": 1.0} -->

The limitations of exploring using $\epsilon$-greedy policies are clear in games such as Montezuma's Revenge, where many actions must be executed to collect the first reward. Noisy Nets (?) propose a noisy linear layer that combines a deterministic and noisy stream, where $\epsilon^{b}$ and $\epsilon^{w}$ are random variables, and $\odot$ denotes the element-wise product. This transformation can then be used in place of the standard linear ${\mathbf{y}} = {{\mathbf{b}} + {\text{W}{\mathbf{x}}}}$. Over time, the network can learn to ignore the noisy stream, but will do so at different rates in different parts of the state space, allowing state-conditional exploration with a form of self-annealing.

<!-- chunk {"id": "body-0026", "role": "body", "section": "The Integrated Agent", "weight": 1.0} -->

In this paper we integrate all the aforementioned components into a single integrated agent, which we call Rainbow.

<!-- chunk {"id": "body-0027", "role": "body", "section": "The Integrated Agent", "weight": 1.0} -->

First, we replace the 1-step distributional loss with a multi-step variant. We construct the target distribution by contracting the value distribution in $S_{t + n}$ according to the cumulative discount, and shifting it by the truncated $n$-step discounted return. This corresponds to defining the target distribution as $d_{t}^{(n)} = {({R_{t}^{(n)} + {\gamma_{t}^{(n)}{\mathbf{z}}}},{{\mathbf{p}}_{\overline{\theta}}{(S_{t + n},a_{t + n}^{\ast})}})}$. The resulting loss is where, again, $\Phi_{\mathbf{z}}$ is the projection onto $\mathbf{z}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "The Integrated Agent", "weight": 1.0} -->

We combine the multi-step distributional loss with double Q-learning by using the greedy action in $S_{t + n}$ selected according to the *online network* as the bootstrap action $a_{t + n}^{\ast}$, and evaluating such action using the *target network*.

<!-- chunk {"id": "body-0029", "role": "body", "section": "The Integrated Agent", "weight": 1.0} -->

In standard proportional prioritized replay (?) the absolute TD error is used to prioritize the transitions. This can be computed in the distributional setting, using the mean action values. However, in our experiments all distributional Rainbow variants prioritize transitions by the KL loss, since this is what the algorithm is minimizing: The KL loss as priority might be more robust to noisy stochastic environments because the loss can continue to decrease even when the returns are not deterministic.

<!-- chunk {"id": "body-0030", "role": "body", "section": "The Integrated Agent", "weight": 1.0} -->

The network architecture is a dueling network architecture adapted for use with return distributions. The network has a shared representation $f_{\xi}{(s)}$, which is then fed into a value stream $v_{\eta}$ with $N_{\text{atoms}}$ outputs, and into an advantage stream $a_{\xi}$ with $N_{\text{atoms}} \times N_{\text{actions}}$ outputs, where $a_{\xi}^{i}{({f_{\xi}{(s)}},a)}$ will denote the output corresponding to atom $i$ and action $a$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "The Integrated Agent", "weight": 1.0} -->

For each atom $z^{i}$, the value and advantage streams are aggregated, as in dueling DQN, and then passed through a softmax layer to obtain the normalised parametric distributions used to estimate the returns' distributions: where $\phi = {f_{\xi}{(s)}}$ and ${{\overline{a}}_{\psi}^{i}{(s)}} = {\frac{1}{N_{\text{actions}}}{\sum_{a'}{a_{\psi}^{i}{(\phi,a')}}}}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "The Integrated Agent", "weight": 1.0} -->

We then replace all linear layers with their noisy equivalent described in Equation. Within these noisy linear layers we use factorised Gaussian noise (?) to reduce the number of independent noise variables.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experimental Methods", "weight": 1.0} -->

We now describe the methods and setup used for configuring and evaluating the learning agents.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Evaluation Methodology", "weight": 1.0} -->

We evaluated all agents on 57 Atari 2600 games from the arcade learning environment (?). We follow the training and evaluation procedures of ? (?) and van Hasselt et al. (?). The average scores of the agent are evaluated during training, every 1M steps in the environment, by suspending learning and evaluating the latest agent for 500K frames. Episodes are truncated at 108K frames (or 30 minutes of simulated play), as in van Hasselt et al. (?).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Evaluation Methodology", "weight": 1.0} -->

Agents' scores are normalized, per game, so that 0% corresponds to a random agent and 100% to the average score of a human expert. Normalized scores can be aggregated across all Atari levels to compare the performance of different agents. It is common to track the *median* human normalized performance across all games. We also consider the number of games where the agent's performance is above some fraction of human performance, to disentangle where improvements in the median come. The *mean* human normalized performance is potentially less informative, as it is dominated by a few games (e.g., Atlantis) where agents achieve scores orders of magnitude higher than humans do.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Evaluation Methodology", "weight": 1.0} -->

Besides tracking the median performance as a function of environment steps, at the end of training we re-evaluate the best agent snapshot using two different testing regimes. In the no-ops starts regime, we insert a random number (up to 30) of no-op actions at the beginning of each episode (as we do also in training). In the human starts regime, episodes are initialized with points randomly sampled from the initial portion of human expert trajectories (?); the difference between the two regimes indicates the extent to which the agent has over-fit to its own trajectories.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Evaluation Methodology", "weight": 1.0} -->

Due to space constraints, we focus on aggregate results across games. However, in the appendix we provide full learning curves for all games and all agents, as well as detailed comparison tables of raw and normalized scores, in both the no-op and human starts testing regimes.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Evaluation Methodology", "weight": 1.0} -->

Min history to start learning Adam learning rate Target Network Period Prioritization importance sampling β Distributional min/max values Table 1: Rainbow hyper-parameters

<!-- chunk {"id": "body-0039", "role": "body", "section": "Hyper-parameter tuning", "weight": 1.0} -->

All Rainbow's components have a number of hyper-parameters. The combinatorial space of hyper-parameters is too large for an exhaustive search, therefore we have performed limited tuning. For each component, we started with the values used in the paper that introduced this component, and tuned the most sensitive among hyper-parameters by manual coordinate descent.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Hyper-parameter tuning", "weight": 1.0} -->

DQN and its variants do not perform learning updates during the first $200K$ frames, to ensure sufficiently uncorrelated updates. We have found that, with prioritized replay, it is possible to start learning sooner, after only $80K$ frames.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Hyper-parameter tuning", "weight": 1.0} -->

DQN starts with an exploration $\epsilon$ of 1, corresponding to acting uniformly at random; it anneals the amount of exploration over the first 4M frames, to a final value of 0.1 (lowered to 0.01 in later variants). Whenever using Noisy Nets, we acted fully greedily ($\epsilon = 0$), with a value of $0.5$ for the $\sigma_{0}$ hyper-parameter used to initialize the weights in the noisy stream^11^1The noise was generated on the GPU. Tensorflow noise generation can be unreliable on GPU. If generating the noise on the CPU, lowering $\sigma_{0}$ to 0.1 may be helpful.. For agents without Noisy Nets, we used $\epsilon$-greedy but decreased the exploration rate faster than was previously used, annealing $\epsilon$ to 0.01 in the first $250K$ frames.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Hyper-parameter tuning", "weight": 1.0} -->

We used the Adam optimizer (?), which we found less sensitive to the choice of the learning rate than RMSProp. DQN uses a learning rate of $\alpha = 0.00025$ In all Rainbow's variants we used a learning rate of $\alpha/4$, selected among $\{{\alpha/2},{\alpha/4},{\alpha/6}\}$, and a value of $1.5 \times 10^{- 4}$ for Adam's $\epsilon$ hyper-parameter.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Hyper-parameter tuning", "weight": 1.0} -->

For replay prioritization we used the recommended proportional variant, with priority exponent $\omega$ of $0.5$, and linearly increased the importance sampling exponent $\beta$ from 0.4 to 1 over the course of training. The priority exponent $\omega$ was tuned comparing values of $\{ 0.4,0.5,0.7\}$. Using the KL loss of distributional DQN as priority, we have observed that performance is very robust to the choice of $\omega$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Hyper-parameter tuning", "weight": 1.0} -->

The value of $n$ in multi-step learning is a sensitive hyper-parameter of Rainbow. We compared values of $n = {1,3,{\text{and~}5}}$. We observed that both $n = 3$ and $5$ did well initially, but overall $n = 3$ performed the best by the end.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Hyper-parameter tuning", "weight": 1.0} -->

The hyper-parameters (see Table 1) are identical across all 57 games, i.e., the Rainbow agent really is a *single* agent setup that performs well across all the games.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Analysis", "weight": 1.0} -->

In this section we analyse the main experimental results. First, we show that Rainbow compares favorably to several published agents. Then we perform ablation studies, comparing several variants of the agent, each corresponding to removing a single component from Rainbow.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Comparison to published baselines", "weight": 1.0} -->

In Figure 1 we compare the Rainbow's performance (measured in terms of the median human normalized score across games) to the corresponding curves for A3C, DQN, DDQN, Prioritized DDQN, Dueling DDQN, Distributional DQN, and Noisy DQN. We thank the authors of the Dueling and Prioritized agents for providing the learning curves of these, and report our own re-runs for DQN, A3C, DDQN, Distributional DQN and Noisy DQN. The performance of Rainbow is significantly better than any of the baselines, both in data efficiency, as well as in final performance. Note that we match final performance of DQN after 7M frames, surpass the best final performance of these baselines in 44M frames, and reach substantially improved final performance.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Comparison to published baselines", "weight": 1.0} -->

In the final evaluations of the agent, after the end of training, Rainbow achieves a median score of 223% in the no-ops regime; in the human starts regime we measured a median score of 153%. In Table 2 we compare these scores to the published median scores of the individual baselines.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Comparison to published baselines", "weight": 1.0} -->

In Figure 2 (top row) we plot the number of games where an agent has reached some specified level of human normalized performance. From left to right, the subplots show on how many games the different agents have achieved 20%, 50%, 100%, 200% and 500% human normalized performance. This allows us to identify where the overall improvements in performance come. Note that the gap in performance between Rainbow and other agents is apparent at all levels of performance: the Rainbow agent is improving scores on games where the baseline agents were already good, as well as improving in games where baseline agents are still far from human performance.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Learning speed", "weight": 1.0} -->

As in the original DQN setup, we ran each agent on a single GPU. The 7M frames required to match DQN's final performance correspond to less than 10 hours of wall-clock time. A full run of 200M frames corresponds to approximately 10 days, and this varies by less than 20% between all of the discussed variants. The literature contains many alternative training setups that improve performance as a function of wall-clock time by exploiting parallelism, e.g., ? (?), ? (?), and ? (?). Properly relating the performance across such very different hardware/compute resources is non-trivial, so we focused exclusively on algorithmic variations, allowing apples-to-apples comparisons. While we consider them to be important and complementary, we leave questions of scalability and parallelism to future work.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Ablation studies", "weight": 1.0} -->

Since Rainbow integrates several different ideas into a single agent, we conducted additional experiments to understand the contribution of the various components, in the context of this specific combination.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Ablation studies", "weight": 1.0} -->

To gain a better understanding of the contribution of each component to the Rainbow agent, we performed ablation studies. In each ablation, we removed one component from the full Rainbow combination. Figure 3 shows a comparison for median normalized score of the full Rainbow to six ablated variants. Figure 2 (bottom row) shows a more detailed breakdown of how these ablations perform relative to different thresholds of human normalized performance, and Figure 4 shows the gain or loss from each ablation for every game, averaged over the full learning run.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Ablation studies", "weight": 1.0} -->

Prioritized replay and multi-step learning were the two most crucial components of Rainbow, in that removing either component caused a large drop in median performance. Unsurprisingly, the removal of either of these hurt early performance. Perhaps more surprisingly, the removal of multi-step learning also hurt final performance. Zooming in on individual games (Figure 4), we see both components helped almost uniformly across games (the full Rainbow performed better than either ablation in 53 games out of 57).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Ablation studies", "weight": 1.0} -->

Distributional Q-learning ranked immediately below the previous techniques for relevance to the agent's performance. Notably, in early learning no difference is apparent, as shown in Figure 3, where for the first 40 million frames the distributional-ablation performed as well as the full agent. However, without distributions, the performance of the agent then started lagging behind. When the results are separated relatively to human performance in Figure 2, we see that the distributional-ablation primarily seems to lags on games that are above human level or near it.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Ablation studies", "weight": 1.0} -->

In terms of median performance, the agent performed better when Noisy Nets were included; when these are removed and exploration is delegated to the traditional $\epsilon$-greedy mechanism, performance was worse in aggregate (red line in Figure 3). While the removal of Noisy Nets produced a large drop in performance for several games, it also provided small increases in other games (Figure 4).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Ablation studies", "weight": 1.0} -->

In aggregate, we did not observe a significant difference when removing the dueling network from the full Rainbow. The median score, however, hides the fact that the impact of Dueling differed between games, as shown by Figure 4. Figure 2 shows that Dueling perhaps provided some improvement on games with above-human performance levels (# games $> {200\%}$), and some degradation on games with sub-human performance (# games $> {20\%}$).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Ablation studies", "weight": 1.0} -->

Also in the case of double Q-learning, the observed difference in median performance (Figure 3) is limited, with the component sometimes harming or helping depending on the game (Figure 4). To further investigate the role of double Q-learning, we compared the predictions of our trained agents to the actual discounted returns computed from clipped rewards. Comparing Rainbow to the agent where double Q-learning was ablated, we observed that the actual returns are often higher than $10$ and therefore fall outside the support of the distribution, spanning from $- 10$ to $+ 10$. This leads to underestimated returns, rather than overestimations. We hypothesize that clipping the values to this constrained range counteracts the overestimation bias of Q-learning. Note, however, that the importance of double Q-learning may increase if the support of the distributions is expanded.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Ablation studies", "weight": 1.0} -->

In the appendix, for each game we show final performance and learning curves for Rainbow, its ablations, and baselines.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have demonstrated that several improvements to DQN can be successfully integrated into a single learning algorithm that achieves state-of-the-art performance. Moreover, we have shown that within the integrated algorithm, all but one of the components provided clear performance benefits. There are many more algorithmic components that we were not able to include, which would be promising candidates for further experiments on integrated agents. Among the many possible candidates, we discuss several below.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have focused here on value-based methods in the Q-learning family. We have not considered purely policy-based RL algorithms such as trust-region policy optimisation (?), nor actor-critic methods (?; ?).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Discussion", "weight": 1.5} -->

A number of algorithms exploit a sequence of data to achieve improved learning efficiency. Optimality tightening (?) uses multi-step returns to construct additional inequality bounds, instead of using them to replace the 1-step targets used in Q-learning. Eligibility traces allow a soft combination over n-step returns (?). However, sequential methods all leverage more computation per gradient than the multi-step targets used in Rainbow. Furthermore, introducing prioritized sequence replay raises questions of how to store, replay and prioritise sequences.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Discussion", "weight": 1.5} -->

Episodic control (?) also focuses on data efficiency, and was shown to be very effective in some domains. It improves early learning by using episodic memory as a complementary learning system, capable of immediately re-enacting successful action sequences.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Discussion", "weight": 1.5} -->

Besides Noisy Nets, numerous other exploration methods could also be useful algorithmic ingredients: among these Bootstrapped DQN (?), intrinsic motivation (?) and count-based exploration (?). Integration of these alternative components is fruitful subject for further research.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this paper we have focused on the core learning updates, without exploring alternative computational architectures. Asynchronous learning from parallel copies of the environment, as in A3C (?), Gorila (?), or Evolution Strategies (?), can be effective in speeding up learning, at least in terms of wall-clock time. Note, however, they can be less data efficient.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Discussion", "weight": 1.5} -->

Hierarchical RL has also been applied with success to several complex Atari games. Among successful applications of HRL we highlight h-DQN (?) and Feudal Networks (?).

<!-- chunk {"id": "body-0066", "role": "body", "section": "Discussion", "weight": 1.5} -->

The state representation could also be made more efficient by exploiting auxiliary tasks such as pixel control or feature control (?), supervised predictions (?) or successor features (?).

<!-- chunk {"id": "body-0067", "role": "body", "section": "Discussion", "weight": 1.5} -->

To evaluate Rainbow fairly against the baselines, we have followed the common domain modifications of clipping rewards, fixed action-repetition, and frame-stacking, but these might be removed by other learning algorithm improvements. Pop-Art normalization (?) allows reward clipping to be removed, while preserving a similar level of performance. Fine-grained action repetition (?) enabled to learn how to repeat actions. A recurrent state network (?) can learn a temporal state representation, replacing the fixed stack of observation frames. In general, we believe that exposing the real game to the agent is a promising direction for future research.
