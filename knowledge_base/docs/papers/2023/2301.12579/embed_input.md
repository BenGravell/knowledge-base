<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sample Efficient Deep Reinforcement Learning via Local Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The focus of this work is sample-efficient deep reinforcement learning (RL) with a simulator. One useful property of simulators is that it is typically easy to reset the environment to a previously observed state. We propose an algorithmic framework, named uncertainty-first local planning (UFLP), that takes advantage of this property. Concretely, in each data collection iteration, with some probability, our meta-algorithm resets the environment to an observed state which has high uncertainty, instead of sampling according to the initial-state distribution. The agent-environment interaction then proceeds as in the standard online RL setting. We demonstrate that this simple procedure can dramatically improve the sample cost of several baseline RL algorithms on difficult exploration tasks. Notably, with our framework, we can achieve super-human performance on the notoriously hard Atari game, Montezuma's Revenge, with a simple (distributional) double DQN. Our work can be seen as an efficient approximate implementation of an existing algorithm with theoretical guarantees, which offers an interpretation of the positive empirical results.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Simulators are ubiquitous in modern reinforcement learning (RL). They correspond to either to the environment itself (as in chess, go, and video games ) or to a simplified model of the true environment (such as robotic arm manipulation, car driving, or plasma shape control in fusion ). Simulators have been widely used in RL research. Many standard benchmarks in RL involve simulators, for example, Atari games, Mujoco simulation engine, OpenAI Gym, DeepMind control suite, and DeepMind Lab. Somewhat surprisingly, the majority of RL algorithms use the agent-environment interaction protocols that mimic learning in the real world during training, and do not explicitly take advantage of favorable simulator properties. In particular, the standard interaction protocol, called *online access*, assumes that the agent can only follow the dynamics of the environment during learning. In this work, we consider the *local access* protocol, where the agent is allowed to revisit any previously observed state in addition to following the dynamics. This protocol can easily be implemented with simulators for many commonly used RL environments (see, e.g., Appendix B).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Local access has received less attention from the RL community compared online access. On the theory side, several recent works show that local access makes sample-efficient learning possible in settings where it has not been shown in the online access setting. On the empirical side, the *vine* method in TRPO uses local access to obtain better estimates of the value function, and the Go-Explore algorithm of Ecoffet et al. relies on local access to achieve state-of-the-art performance on several hard-exploration Atari games. Intuitively, the main advantage of local access is that we can directly reset the simulator to the states that can provide more information to the agent, and thus improve the exploration of the state space.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Contributions", "weight": 1.0} -->

We propose a general algorithmic framework for RL with a simulator under the local access protocol. Our framework, named *uncertainty-first local planning* (UFLP), revisits states from the agent's history based on the uncertainty about their value.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Contributions", "weight": 1.0} -->

We instantiate this framework with several base RL agents (deep Q-networks, policy iteration) and uncertainty estimates (ensemble, feature covariance, approximate counts, random network distillation).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contributions", "weight": 1.0} -->

We demonstrate that UFLP can significantly improve the sample cost compared to online access on difficult exploration tasks, including the Deep Sea and Cartpole Swingup benchmarks in bsuite and hard-exploration Atari games: Montezuma's Revenge and PrivateEye. In particular, for the Deep Sea environment, by leveraging UFLP, many RL agents can easily solve the task, whereas in the online access setting they can only obtain zero reward. For Montezuma's Revenge, applying UFLP on top of a simple double DQN results in a super-human score.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

Our work also opens up a new research avenue for improving sample efficiency when learning with simulators.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Local access protocol", "weight": 1.0} -->

Simulators are routinely used in RL algorithms that leverage Monte Carlo tree search, including prominent examples such as AlphaGo and AlphaZero. One major difference between the tree-search setting and the setting that we consider in this paper is that the tree-search algorithms usually make the assumption that the agent has local access to the simulator during *evaluation*, whereas we only consider local access during training. This means that once the training is finished, the agent is evaluated against the environment without access to the simulator. Therefore, our framework is more suitable for applications that require fast inference when the agent is deployed. Moreover, most tree-search approaches do not select states to revisit strategically; instead, they expand the search tree based on visitation counts, rather than more general uncertainty metrics.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Local access protocol", "weight": 1.0} -->

One notable example of RL with local access protocol is the Go-Explore algorithm. This algorithm operates under the local access protocol and revisits states deemed to be "promising" in history. It then uses backward learning-from-demonstrations to learn a robust policy. While Go-Explore achieves or surpasses the state of the art on $11$ Atari games, the algorithm design, especially the state revisiting rule, uses heuristics tailored to these games, and it is unclear how to combine this method with other uncertainty metrics or more general RL agents. By contrast, in this paper, we propose a *general algorithm framework* that can be combined with most existing RL agents in order to improve their performance.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Local access protocol", "weight": 1.0} -->

Besides Go-Explore, a few other prior works have studied the use of local access. In an early literature on real-time dynamic programming, it has been shown that prioritizing revisiting states with higher uncertainty is helpful for achieving faster convergence. However, these works mainly focus on tabular MDPs and only consider the value iteration algorithm. On the contrary, our general framework is suitable for function approximation and can be combined with other types of agents beyond value iteration. In the vine method in the TRPO algorithm, local access is used to obtain more accurate estimates of the value function. This differs from our work since we focus on improving exploration of deep RL agents. Restart distributions have also been explored in Tavakoli et al., who consider revisiting states uniformly at random, according to TD error, and according to episode returns, in combination with the PPO algorithm. Revisiting based on high episode returns improves the performance of PPO on a sparse-reward task deemed hard-exploration. However, it is unclear that the same approach would be successful in environments such as Deep Sea, where discovering an episode with a positive return requires non-trivial exploration.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Local access protocol", "weight": 1.0} -->

A very recent work by Lan et al. focuses on generalization of RL agents to out-of-distribution trajectories using local access to a simulator. Their algorithm can be considered as a special case in our framework.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Local access protocol", "weight": 1.0} -->

On the theoretical side, several recent works have proposed sample- and computationally-efficient algorithms under the local access protocol and with linearly-realizable action-value functions. The works of Yin et al., Hao et al., and Weisz et al. maintain a *core set* of previously-visited states that cover different parts of the feature space. In the online access setting, a similar idea is used in the policy cover policy gradient (PCPG) algorithm of Agarwal et al. and the follow-up work of Zanette et al.. Our work is motivated by the approaches of Yin et al. and Hao et al., but adapted to the practical setting of value learning with neural network function approximation, where the core set is more difficult to define rigorously.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Uncertainty estimation and exploration in RL", "weight": 1.0} -->

Successful methods for learning in MDPs typically rely on estimates of uncertainty about the value of state-action pairs in order to encourage the agent to explore the environment. One type of exploration strategies rely on uncertainty-based *intrinsic rewards* or *bonuses*. Uncertainty metrics based on feature covariance have been used in theoretical RL works with linear function approximation. Empirically, popular approaches include approximate count, random network distillation (RND), and curiosity-driven exploration. Recent successful approaches have constructed bonuses based on nearest-neighbors in the current episode, as well as RND to capture longer-term uncertainty. Another set of approaches rely on randomized value functions. We discuss these methods in more detail in Section 5.1.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

An infinite-horizon discounted Markov decision process (MDP) can be characterized by a tuple $(\mathcal{S},\mathcal{A},R,P,\mu_{0},\gamma)$, where $\mathcal{S}$ is the state space, $\mathcal{A}$ is the action space, $R:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\lbrack 0,1\rbrack}}$ is the reward function, $P:{{\mathcal{S} \times \mathcal{A}}\rightarrow\Delta_{\mathcal{S}}}$ is the probability transition kernel, $\mu_{0}$ is the initial state distribution, and $\gamma \in {}$ is the discount factor. Both $P$ and $R$ are unknown. In this paper, we only consider finite action space ${|\mathcal{A}|} < \infty$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

At each state $s$, if the agent picks an action $a \in \mathcal{A}$, the environment evolves to a random next state $s^{\prime}$ according to the distribution $P{(\left. s^{\prime} \middle| {s,a} \right.)}$ and generates a stochastic reward $r \in {\lbrack 0,1\rbrack}$ with ${{\mathbb{E}}{\lbrack\left. r \middle| {s,a} \right.\rbrack}} = {R{(s,a)}}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Simulator Interaction Protocol", "weight": 1.0} -->

We distinguish between three protocols for interacting with the MDP simulator (or environment) commonly used in the literature.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Simulator Interaction Protocol", "weight": 1.0} -->

*Online access*. The initial state $s_{0}$ is sampled from the initial state distribution $\mu_{0}$. The agent can only reset the environment to a (possibly random) initial state, or move to the next state given an action by following the MDP dynamics.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Simulator Interaction Protocol", "weight": 1.0} -->

*Local access*. The agent can reset the environment to a random initial state, or to a state that has previously been observed.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Simulator Interaction Protocol", "weight": 1.0} -->

*Random access*. The agent can query the simulator with *any* state-action pair of its choice to obtain a reward and a sample of the next state. This is often referred as the *access to a generative model* in literature.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Simulator Interaction Protocol", "weight": 1.0} -->

Most RL algorithms use the online access protocol, which also mimics learning in the real world. Random access is primarily considered in theoretical works, as it enables sample-efficient learning in settings where this is impossible under online access. Unfortunately, this interaction protocol is often difficult or impossible to support in large-scale MDPs where the agent may not even know which states exist or are plausible. For example, for random access, the agent would need to know which positions and velocities of a robotic arm are valid according to physics, or which images correspond to a valid frame of a video game. The local access protocol does not suffer from this issue, as the agent is only allowed to revisit previously observed states which are known to be plausible. Local access is also easy to implement in most simulators, for example by checkpointing the simulator state.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Simulator Interaction Protocol", "weight": 1.0} -->

The intuition on why using local access can improve sample efficiency of policy optimization is that we can directly reset the simulator to the states that can provide more information to the agent. In other words, we can directly start data collection from the states with high uncertainty. In the online access mode, exploration methods such as additive bonus and Thompson sampling have been designed to achieve the similar goal; however, in this setting, the agent still has to start from the initial state, reach an uncertain state, and then collect data there. Therefore, local access saves the sample cost by leveraging the resetting ability of simulators.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Algorithm Framework", "weight": 1.0} -->

In this section, we present an algorithm framework for policy optimization with local access to a simulator.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Algorithm Framework", "weight": 1.0} -->

A *simulator* (or environment) that we can reset to any state that has been observed during the learning process, denoted by Env in the following. We denote the operation of resetting the environment to a given observed state $s$ by $\text{𝙴𝚗𝚟}.{\text{Reset}{(s)}}$. We also denote the operation of stepping the environment (taking an action and moving to the next state) by $\text{𝙴𝚗𝚟}.{\text{Step}{(a)}}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Algorithm Framework", "weight": 1.0} -->

A *base agent* (Agent) that can take actions given the observation of a state $s$ ($\text{𝙰𝚐𝚎𝚗𝚝}.{\text{Act}{(s)}}$) and update itself ($\text{𝙰𝚐𝚎𝚗𝚝}.{\text{Update}{}}$) given collected data. In fact, any agent for online-access RL can be used as a base agent in our framework.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Algorithm Framework", "weight": 1.0} -->

A *function* $u:{{\mathcal{S} \times \mathcal{A}}\mapsto{\mathbb{R}}}$ that measures the *uncertainty* of the agent about the value of state-action pairs. In some cases, we only define the uncertainty of the states, i.e., $u:{\mathcal{S}\mapsto{\mathbb{R}}}$. This function is are typically updated during learning.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Algorithm Framework", "weight": 1.0} -->

A *history buffer* $\mathcal{H}$. Each element in $\mathcal{H}$ contains all the necessary information to reset the environment to a particular state $s$. Note that the history buffer differs from the replay buffer, which is usually used to maintain state-action transition tuples and update the agent. In the following, we omit the role of the replay buffer and mainly focus on the use of the history buffer.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Algorithm Framework", "weight": 1.0} -->

Similarly to online access, our framework includes a data collection process, where the agent interacts with the environment and collects data, and a learning process where the agent is updated. The major difference in our framework is that we need to specify a starting state-action pair in the data collection process; more specifically, we reset the simulator to a given state, take a given action, move to the next state and follow the agent's action selection afterwards. This process, denoted by $\text{DataCollection}{(\text{𝙴𝚗𝚟},\text{𝙰𝚐𝚎𝚗𝚝},s_{0},a_{0},\mathcal{H})}$ is described in Algorithm 1.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Algorithm Framework", "weight": 1.0} -->

Input: environment Env, base agent Agent, starting state-action s0, a0, history buffer ℋ.
while end of episode not reached do

<!-- chunk {"id": "body-0030", "role": "body", "section": "Algorithm Framework", "weight": 1.0} -->

With these components, we are ready to present our algorithm framework, *uncertainty-first local planning* (UFLP). Here, we use the term *planning* to distinguish our learning setting from the online access mode where data must be collected episode-by-episode during training. In UFLP, in each data collection iteration, with probability $p_{\text{init}} \in {\lbrack 0,1\rbrack}$, we sample an initial state $s_{0}$ according to the initial state distribution $\mu_{0}$ and start data collection from $s_{0}$. Otherwise, we sample a batch of $B$ elements from the history buffer $\mathcal{H}$, denoted by $\mathcal{H}_{B}$, pair these states with all possible actions, and choose the highest-uncertainty state-action pair as the starting point, i.e., we choose the starting point according to

<!-- chunk {"id": "body-0031", "role": "body", "section": "Algorithm Framework", "weight": 1.0} -->

As we can see, if $p_{\text{init}} = 1$, the algorithm reduces to the online access mode. We present details of our framework in Algorithm 2, where we use ${Unif}{\lbrack 0,1\rbrack}$ to denote a random number that is sampled uniformly at random from $\lbrack 0,1\rbrack$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Algorithm Framework", "weight": 1.0} -->

Inputs: environment Env, base agent Agent, probability of starting from initial state pinit ∈, history buffer batch size B, uncertainty metric u.
while termination criteria not met do
if Unif ≤ pinit or ℋ = ⌀ then
Sample B elements from ℋ, denoted by ℋB.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Algorithm Framework", "weight": 1.0} -->

One intuition behind the criterion that chooses an uncertain state as a starting point is that it expands the subset of the state space that we can use to start the data collection process, which in turn helps control extrapolation errors in value function estimation. Revisiting uncertain states can also improve sample efficiency in environments where states that are important for decision-making are difficult to reach.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Algorithm Framework", "weight": 1.0} -->

We also note that in practice, storing all the states that the agent has visited during training may require too much memory. Therefore, we implement the history buffer $\mathcal{H}$ using a FIFO queue. Another note is that if we only have an uncertainty metric for states rather than state-action pairs, we can choose the most uncertain state in $\mathcal{H}_{B}$ and pair it with a random action, i.e.,

<!-- chunk {"id": "body-0035", "role": "body", "section": "Algorithm Framework", "weight": 1.0} -->

Our experiments in Section 6.1 for bsuite environments use Eq. 1 and those in Section 6.2 for Atari games use Eq. 2.^11^1We also experimented with Eq. 1 for Atari games. However, Eq. 2 led to slightly better results, and thus we report the Atari results with Eq.. 2.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Algorithm Framework", "weight": 1.0} -->

Next, we describe several instantiations of base agents and uncertainty metrics that can be used with the local access protocol.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Base Agents", "weight": 1.0} -->

For base agents, we consider the following commonly used ones: double deep Q network (DDQN), bootstrapped DDQN (BootDDQN), distributional DDQN, and approximate policy iteration (PI).

<!-- chunk {"id": "body-0038", "role": "body", "section": "DDQN", "weight": 1.0} -->

Double DQN is an improvement of the original DQN agent by Mnih et al..

<!-- chunk {"id": "body-0039", "role": "body", "section": "DDQN", "weight": 1.0} -->

where $\theta$ denotes the parameters of the Q-network, and $\theta^{\prime}$ denotes the parameters of the target network that is periodically updated. During acting, one can use the standard $\epsilon$-greedy strategy, where with probability $\epsilon$, we take a random action, and otherwise we act greedily w.r.t. $Q{(s,a;\theta)}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "DDQN", "weight": 1.0} -->

To improve exploration, one can use an additive bonus, a.k.a. optimism. There are two common approaches. First, adding an *acting-time* bonus means that we fit the Q-network using Eq. 3 and select actions according to

<!-- chunk {"id": "body-0041", "role": "body", "section": "DDQN", "weight": 1.0} -->

where $u{(s,a)}$ is the uncertainty metric and $c > 0$ is a scaling factor. A similar approach has been discussed in Chen et al.. The second approach is to add an *intrinsic reward* to the reward $r_{t}$ provided by the environment, i.e., replace $r_{t}$ in Eq. 3 with

<!-- chunk {"id": "body-0042", "role": "body", "section": "DDQN", "weight": 1.0} -->

and train the Q-network with $r_{t}^{\prime}$. This approach has been widely used in the literature. In the following, we call the DDQN agent with acting-time bonus and intrinsic reward DDQN-Bonus and DDQN-Intrinsic, respectively.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Bootstrapped DDQN", "weight": 1.0} -->

Another approach to improving exploration of the DQN agent is to mimic the behavior of Thompson sampling. Osband et al. proposed the boostrapped DQN agent to achieve this goal. Here we replace the DQN loss with the DDQN loss in Eq. 3 and thus we name this agent bootstrapped DDQN (BootDDQN). This agent maintains an ensemble of $M$ Q-networks. For the $m$-th network, the parameters are a summation of a trainable component $\theta_{m}$ and a fixed randomized prior network $\theta_{m}^{p}$, and thus the Q-network can be denoted by $Q{(s,a;{\overset{\sim}{\theta}}_{m})}$, where ${\overset{\sim}{\theta}}_{m}:={\theta_{m} + \theta_{m}^{p}}$. The randomized prior $\theta_{m}^{p}$ is independently initialized at the beginning of the algorithm and kept fixed during training.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Bootstrapped DDQN", "weight": 1.0} -->

During the learning process, we use the data from the replay buffer to update all the ensemble members. This means that we minimize

<!-- chunk {"id": "body-0045", "role": "body", "section": "Bootstrapped DDQN", "weight": 1.0} -->

where ${\overset{\sim}{\theta}}_{m}^{\prime}$ is the parameter for the target network of the $m$-th ensemble member. As for acting, at the beginning of each data collection iteration, we first sample an ensemble index $m \sim {\text{Unif}{\lbrack M\rbrack}}$ and then use this ensemble member throughout this iteration, i.e., ${\text{Act}{(s)}} = {{\arg{\max_{a \in \mathcal{A}}Q}}{(s,a;{\overset{\sim}{\theta}}_{m})}}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Distributional DDQN", "weight": 1.0} -->

This agent was originally proposed by Bellemare et al.. Instead of predicting the expectation of the cumulative reward using the Q-network, we predict its distribution. Define the $n$ *atoms* as ${v_{\min},{v_{\min} + \delta},\ldots,v_{\max}}:={v_{\min} + {{({n - 1})}\delta}}$ and let ${Q{(s,a;\theta)}} \in {\mathbb{R}}^{n}$ be the PMF of a discrete distribution over the $N$ atoms and $\overline{Q}{(s,a;\theta)}$ be its expectation. The loss during training $L_{\text{Dist}}{(\theta)}$ measures the Kullback--Leibler divergence between the predicted distribution and its TD target. See Bellemare et al. for more details.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Policy Iteration", "weight": 1.0} -->

We also experiment with an agent based on approximate policy iteration (PI). Here, we update the Q-function using least-squares Monte Carlo.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Policy Iteration", "weight": 1.0} -->

Note that in standard PI, Q-functions are estimated using *on-policy* data, i.e. the data generated since the most recent policy update. In this implementation, we simply sample transitions uniformly from the history, including off-policy data. This approach has been shown to implicitly regularize policy iteration updates. When acting, the agent acts either greedily with respect to $Q{(s,a;\theta)}$ or using an acting-time bonus as in Eq. 4 (PI-Bonus).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Uncertainty Estimation", "weight": 1.0} -->

We consider several methods for evaluating agent uncertainty: standard deviation of ensemble predictions (for bootstrapped DDQN), covariance of random state-action features, approximate counts, and random network distillation (RND).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Covariance-based uncertainty", "weight": 1.0} -->

This method assumes that we have available a function $\phi:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}^{d}}$ that maps state-action pairs to $d$-dimensional feature vectors. While acting, we keep track of the unnormalized covariance matrix of the feature vectors, i.e.,

<!-- chunk {"id": "body-0051", "role": "body", "section": "Covariance-based uncertainty", "weight": 1.0} -->

We can extract the feature $\phi$ using a pre-trained representation, a randomly initialized neural network, or a combination of both. In this work, we extract random Fourier features from the state, denoted as $\psi{(s)}$ and compute state-action features as ${\phi{(s,a)}} = {{\psi{(s)}} \otimes e_{a}}$, where $e_{a}$ is an $|\mathcal{A}|$-dimensional action indicator vector. Note that in practice, we can maintain the matrix $\Phi^{- 1}$ in a computationally efficient manner by leveraging the Sherman--Morrison formula.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Approximate counts", "weight": 1.0} -->

Another uncertainty metric is to keep approximate counts of the state-action pairs. More specifically, we design a discretization of the state space $\mathcal{S}$, denoted by $\overline{\mathcal{S}}$ (${|\overline{\mathcal{S}}|} < \infty$). Let $\psi:{\mathcal{S}\mapsto\overline{\mathcal{S}}}$ be the function that maps a state to its corresponding discrete element in $\overline{\mathcal{S}}$. Then we can use the following uncertainty metric

<!-- chunk {"id": "body-0053", "role": "body", "section": "Approximate counts", "weight": 1.0} -->

where $n{(s,a)}$ is the visitation count of $({\psi{(s)}},a)$ in the $\overline{\mathcal{S}} \times \mathcal{A}$ space. Note that the approximate-count based method is a special case of the covariance-based uncertainty with $\psi{( \cdot )}$ considered as a one-hot encoded feature vector.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Approximate counts", "weight": 1.0} -->

In this paper, we use this method particularly for image observations in Atari games. More specifically, we downsample the image to a smaller size by average pooling, and then discretize the pixel values. Using the terminology in Go-Explore, we call each discrete element in $\overline{\mathcal{S}}$ a *cell*. Although Go-Explore uses a similar downsampling method, the state-revisiting rule in our UFLP framework is much simpler than in Go-Explore.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Random network distillation (RND)", "weight": 1.0} -->

In RND, uncertainty is given by the error of a neural network $\hat{f}:{\mathcal{S}\mapsto{\mathbb{R}}^{k}}$ trained to predict the features of the observations given by a fixed randomly initialized neural network $f:{\mathcal{S}\mapsto{\mathbb{R}}^{k}}$. The $\ell_{2}$ error is used as the uncertainty metric for the states, i.e.,

<!-- chunk {"id": "body-0056", "role": "body", "section": "Random network distillation (RND)", "weight": 1.0} -->

The use of this metric in our work differs from the original RND work of Burda et al., where this error is used as an intrinsic reward.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we evaluate the benefits of local vs. online access by training agents on difficult exploration tasks. We use two (bsuite) environments: Deep Sea and Cartpole Swingup, and four Atari games: Montezuma's Revenge, PrivateEye, Venture, and Pitfall. These games are known to correspond to difficult exploration problems. In Appendix B, we provide details on how to checkpoint and restore the environment state using Python, for both bsuite and Atari. We also provide our hyperparameter choices in Appendix C. For all the figures in this section, the shaded area shows the $95\%$ confidence interval.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Behavior Suite Experiments", "weight": 1.0} -->

We first introduce the two bsuite environments that we use in this section. Illustrations of the two environments can be found in Figure 1.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Deep Sea", "weight": 1.0} -->

The environment is an $N \times N$ grid with one-hot state encoding. The agent starts from the top left corner of the grid and descends down-left or down-right in each timestep, depending on the action. There is a small cost of $r = {- {0.01/N}}$ for moving right, and $r = 0$ for moving left. If the agent reaches the bottom-right corner, taking only "right" actions, it gets a reward of $+ 1$. This is a simple but challenging exploration problem, due to the fact that exploring uniformly at random only has a $2^{- N}$ chance of finding the high-reward state.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Cartpole Swingup", "weight": 1.0} -->

The goal is to swing up and balance an unactuated pole by applying forces to a cart at its base. The physics model conforms to Barto et al.. The pole starts from a random position pointing down, and the agent can apply a force of $- 1$, $0$, or $1$ to the cart. There is a small cost of $r = {- 0.1}$ for applying a non-zero force. The agent gets a reward of $+ 1$ if the pole is within a small angle of being upright and the cart is within a small range around the origin. We consider two versions of this environment: *default* and *hard* versions, where the hard version has sparser rewards. More details on how the rewards are defined in the two versions can be found in Appendix C.2.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Cartpole Swingup", "weight": 1.0} -->

Our experiments for bsuite environments involve four agents: BootDDQN, DDQN-Bonus, vanilla DDQN, and PI-Bonus. For BootDDQN, we use standard deviation of the ensemble as the uncertainty metric $u_{\text{std}}$. For all other agents, we use the covariance-based uncertainty $u_{\text{cov}}$. The confidence intervals are calculated with $10$ random seeds for Deep Sea and $20$ seeds for Cartpole Swingup. DDQN-Intrinsic does not converge in our Deep Sea and Cartpole Swingup experiments due to numerical issues. Therefore, we do not report the results of DDQN-Intrinsic in this section.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Deep Sea results", "weight": 1.0} -->

We first compare the return of the agents on Deep Sea with size $N = 50$ in the online and local access (UFLP) settings. We use $p_{\text{init}} = 0.1$ and history buffer batch size $B = {|\mathcal{H}|}$ (i.e., we choose the most uncertain state-action pair from the entire history buffer) for all the local access runs. As we can see from Figure 2, local access leads to significantly higher mean return for each agent. In fact, in the online setting, except for BootDDQN, none of the agents can get a return that is significantly higher than $0$ within $3 \times 10^{5}$ simulator queries. Therefore, in this hard-exploration environment, local access significantly improves the sample efficiency.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Deep Sea results", "weight": 1.0} -->

We also investigate the role of $p_{\text{init}}$ and history buffer batch size $B$ in Deep Sea. In Figure 3(a), we plot the normalized area under curve (AUC) for the the convergence curves in Figure 2 as a function of $p_{\text{init}}$.^22^2By normalization, we mean that we divide the AUC by the total number of simulator queries during training. This quantity reflects how fast the return converges. The best performance is achieved with a relatively small $p_{\text{init}}$ (e.g., $0.0 \sim 0.3$) for most agents. This demonstrates the benefits of data collection from intermediate states. In Figure 3, we compare the sample efficiency of BootDDQN with ${B = {1,5}},$ and $|\mathcal{H}|$. As we can see, the best performance is achieved with $B = {|\mathcal{H}|}$, i.e., choosing the most uncertain element in the history buffer.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Deep Sea results", "weight": 1.0} -->

This demonstrates the importance of starting from an uncertain state in Deep Sea. In Appendix A.1, we provide similar results for other agents.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Deep Sea results", "weight": 1.0} -->

In Figure 4, we show the number of queries needed to achieve mean return $0.95$, for the BootDDQN agent, as a function of the size of the Deep Sea environment $N$, to illustrate the scaling of the sample cost. Our results indicates a near-optimal dependency of $\mathcal{O}{(N^{2.47})}$. ^33^3The optimal sample scale is $\mathcal{O}{(N^{2})}$, proportional to the number of all possible state-action pairs.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Cartpole Swingup results", "weight": 1.0} -->

For the default version of Cartpole Swingup, we find that for BootDDQN and DDQN-Bonus agents, the sample efficiency of online and local access modes are similar (Figure 5(a)), whereas for the PI-Bonus agent, local access leads to a significant improvement (Figure 5(b)). This indicates that for environments with relatively dense reward, the benefit of local access can be small, especially for value-based agents. For the hard version, for both BootDDQN and DDQN-Bonus agents, we find that local access leads to a significant improvement over online access (Figure 5(c)). We did not observe positive rewards in the hard version of Cartpole Swingup using the PI-Bonus agent, regardless of the access protocol. In Figure 5(d), we show that the best performance can be achieved with a relatively small $p_{\text{init}}$, e.g., $0.2$, for the hard version of Cartpole Swingup. One observation is that when $p_{\text{init}} = 0.0$, the performance is bad.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Cartpole Swingup results", "weight": 1.0} -->

We hypothesize that this is because for $p_{\text{init}} = 0.0$, we only observe a single initial state from the initial-state distribution, and the agent may not have enough information on how to act from other initial states.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Montezuma's Revenge", "weight": 1.0} -->

Montezuma's Revenge (MR) has sparser rewards than most ALE environments. The agent only receives positive rewards after performing a long series of specific actions. MR has been viewed as one of the most difficult exploration challenges for deep RL. A few approaches surpassing average human performance of 4753 points include RND, NGU and MEME. The SOTA of 43K is achieved by Go-Explore.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Pitfall", "weight": 1.0} -->

This is another highly challenging exploration game in ALE. In addition to sparse positive rewards, Pitfall includes distractor rewards, such as small negative rewards for hitting an enemy, and is only partially observable. Most agents obtain zero reward, and a few exceptions include NGU MEME, and Go-Explore.

<!-- chunk {"id": "body-0070", "role": "body", "section": "PrivateEye", "weight": 1.0} -->

This is also a sparse reward game. The average human performance is 69K.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Venture", "weight": 1.0} -->

Rewards are denser than in the $3$ other games, and the average human score is 1187.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Venture", "weight": 1.0} -->

As base agents, we use the DDQN and distributional DDQN implementations in the Acme framework for distributed RL. In Acme, agent functionality is split into multiple actors, which collect data and write to the replay buffer, and a single learner which updates the agent parameters based on replay data. In our implementation, the actors also write to a common (smaller) history buffer, and choose states to reset to from the history buffer based on uncertainty. We experiment with two different uncertainty metrics: approximate counts and RND. For approximate counts, we downsample the grayscale game images to a shape of $$, and discretize the pixel values to $8$ levels. For RND, the random features are extracted by the Q-network architecture followed by a 2-layer MLP with embedding size $1024$. The predictor also has the same architecture. More implementation details and hyperparameters are given in Appendix C.3. All the confidence intervals in this section are calculated using $5$ random seeds.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Venture", "weight": 1.0} -->

We first evaluate agents on Montezuma's Revenge. For the online setting, we use the vanilla DDQN and DDQN-Intrinsic agents, with the intrinsic reward based on approximate-count uncertainty. For the local setting, we combine DDQN with both approximate-count and RND based uncertainty. We also experiment with DDQN-Intrinsic in the local setting with approximate counts.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Venture", "weight": 1.0} -->

We also observe improvement for the DDQN-Intrinsic agent using local access (Figure 6). However, since DDQN-Intrinsic already has an exploration bonus in the intrinsic reward, the additional benefit of local planning is relatively small. We note that for DDQN-Intrinsic, to get good performance in the local setting, we need to choose a larger value of $p_{\text{init}}$, i.e., $0.7$. This means that we need to reduce the amount of local access iterations in order to reach a good balance between exploration and exploitation.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Venture", "weight": 1.0} -->

We evaluate the performance of distributional DDQN with UFLP ($p_{\text{init}} = 0.3$) for both approximate-count and RND uncertainty on all four Atari games. As we can see in Figure 8, on Montezuma's Revenge, local planning dramatically improves the score of the baseline algorithm to a super-human level. On PrivateEye, local access improves the sample complexity and stability of the baseline algorithm. Venture results are neutral, possibly because the rewards are relatively dense and thus the exploration problem is less challenging compared to other games. On Pitfall, both local and and online access versions fail to obtain positive scores. We conjecture that this is due to the partially-observable nature of this MDP; indeed, prior works that have obtained positive scores have relied on side information, stateful policies, or both.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Venture", "weight": 1.0} -->

We summarize all Atari results in Appendix A.3 and include the highest scores obtained by actors during data collection. Note that actor returns are sometimes considerably higher than those of the learned policy (greedy w.r.t. the Q-function), e.g. $14300$ vs. $7100$ for Montezuma's Revenge and $1800$ vs. $0$ for Pitfall. This suggests the performance of the DDQN agents could be improved by more effective learning (not addressed here) in addition to exploration.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Conclusions and Future Directions", "weight": 1.0} -->

We propose a new algorithmic framework for learning with a simulator under the local access protocol. We demonstrate that our proposed uncertainty-first approach to revisiting states in history can dramatically improve the sample cost of several baseline algorithms on sparse-reward environments. An important direction for future work is improving the quality of uncertainty estimation in MDPs, since the this directly affects the effectiveness of the framework. Another interesting direction for future work is to extend this approach to partially observed environments.
