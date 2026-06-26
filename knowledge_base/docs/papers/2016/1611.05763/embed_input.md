<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning to Reinforcement Learn

Topics include Reinforcement learning, Deep reinforcement learning, Meta-learning, Recurrent neural networks.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces deep meta-reinforcement learning, where a recurrent policy trained by a standard RL algorithm learns internal dynamics that behave like a separate fast adaptation procedure. The paper is a useful early bridge between deep RL, meta-learning, and neuroscience-inspired accounts of flexible behavior.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In recent years deep reinforcement learning (RL) systems have attained superhuman performance in a number of challenging task domains. However, a major limitation of such applications is their demand for massive amounts of training data. A critical present objective is thus to develop deep RL methods that can adapt rapidly to new tasks. In the present work we introduce a novel approach to this challenge, which we refer to as deep meta-reinforcement learning. Previous work has shown that recurrent networks can support meta-learning in a fully supervised context. We extend this approach to the RL setting. What emerges is a system that is trained using one RL algorithm, but whose recurrent dynamics implement a second, quite separate RL procedure. This second, learned RL algorithm can differ from the original one in arbitrary ways. Importantly, because it is learned, it is configured to exploit structure in the training domain. We unpack these points in a series of seven proof-of-concept experiments, each of which examines a key aspect of deep meta-RL. We consider prospects for extending and scaling up the approach, and also point out some potentially important implications for neuroscience.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent advances have allowed long-standing methods for reinforcement learning (RL) to be newly extended to such complex and large-scale task environments as Atari and Go. The key enabling breakthrough has been the development of techniques allowing the stable integration of RL with non-linear function approximation through deep learning. The resulting deep RL methods are attaining human- and often superhuman-level performance in an expanding list of domains. However, there are at least two aspects of human performance that they starkly lack. First, deep RL typically requires a massive volume of training data, whereas human learners can attain reasonable performance on any of a wide range of tasks with comparatively little experience. Second, deep RL systems typically specialize on one restricted task domain, whereas human learners can flexibly adapt to changing task conditions. Recent critiques have invoked these differences as posing a direct challenge to current deep RL research.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the present work, we outline a framework for meeting these challenges, which we refer to as deep meta-reinforcement learning, a label that is intended to both link it with and distinguish it from previous work employing the term "meta-reinforcement learning". The key concept is to use standard deep RL techniques to train a recurrent neural network in such a way that the recurrent network comes to implement its own, free-standing RL procedure. As we shall illustrate, under the right circumstances, the secondary learned RL procedure can display an adaptiveness and sample efficiency that the original RL procedure lacks.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The following sections review previous work employing recurrent neural networks in the context of meta-learning and describe the general approach for extending such methods to the RL setting. We then present seven proof-of-concept experiments, each of which highlights an important ramification of the deep meta-RL setup by characterizing agent performance in light of this framework. We close with a discussion of key challenges for next-step research, as well as some potential implications for neuroscience.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Deep meta-RL: Definition and key features", "weight": 1.0} -->

Importantly, Hochreiter's original work, as well as its subsequent extensions only addressed supervised learning (i.e. the auxiliary input provided on each step explicitly indicated the target output on the previous step, and the network was trained using explicit targets). In the present work we consider the implications of applying the same approach in the context of reinforcement learning. Here, the tasks that make up the training series are interrelated RL problems, for example, a series of bandit problems varying only in their parameterization. Rather than presenting target outputs as auxiliary inputs, the agent receives inputs indicating the action output on the previous step and, critically, the quantity of reward resulting from that action. The same reward information is fed in parallel to a deep RL procedure, which tunes the weights of the recurrent network.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Deep meta-RL: Definition and key features", "weight": 1.0} -->

It is this setup, as well as its result, that we refer to as deep meta-RL (although from here, for brevity, we will often simply call it meta-RL, with apologies to authors who have used that term previously). As in the supervised case, when the approach is successful, the dynamics of the recurrent network come to implement a learning algorithm entirely separate from the one used to train the network weights. Once again, after sufficient training, learning can occur within each task even if the weights are held constant. However, here the procedure the recurrent network implements is itself a full-fledged reinforcement learning algorithm, which negotiates the exploration-exploitation tradeoff and improves the agent's policy based on reward outcomes. A key point, which we will emphasize in what follows, is that this learned RL procedure can differ starkly from the algorithm used to train the network's weights. In particular, its policy update procedure (including features such as the effective learning rate of that procedure), can differ dramatically from those involved in tuning the network weights, and the learned RL procedure can implement its own approach to exploration.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Deep meta-RL: Definition and key features", "weight": 1.0} -->

Critically, as in the supervised case, the learned RL procedure will be fit to the statistics spanning the multi-task environment, allowing it to adapt rapidly to new task instances.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Formalism", "weight": 1.0} -->

Let us write as $\mathcal{D}$ a distribution (the prior) over Markov Decision Processes (MDPs). We want to demonstrate that meta-RL is able to learn a prior-dependent RL algorithm, in the sense that it will perform well on average on MDPs drawn from $\mathcal{D}$ or slight modifications of $\mathcal{D}$. An appropriately structured agent, embedding a recurrent neural network, is trained by interacting with a sequence of MDP environments (also called tasks) through episodes. At the start of a new episode, a new MDP task $m \sim \mathcal{D}$ and an initial state for this task are sampled, and the internal state of the agent (i.e., the pattern of activation over its recurrent units) is reset. The agent then executes its action-selection strategy in this environment for a certain number of discrete time-steps.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Formalism", "weight": 1.0} -->

At each step $t$ an action $a_{t} \in A$ is executed as a function of the whole history $\mathcal{H}_{t} = {\{ x_{0},a_{0},r_{0},\ldots,x_{t - 1},a_{t - 1},r_{t - 1},x_{t}\}}$ of the agent interacting in the MDP $m$ during the current episode (set of states ${\{ x_{s}\}}_{0 \leq s \leq t}$, actions ${\{ a_{s}\}}_{0 \leq s < t}$, and rewards ${\{ r_{s}\}}_{0 \leq s < t}$ observed since the beginning of the episode, when the recurrent unit was reset). The network weights are trained to maximize the sum of observed rewards over all steps and episodes.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Formalism", "weight": 1.0} -->

After training, the agent's policy is fixed (i.e. the weights are frozen, but the activations are changing due to input from the environment and the hidden state of the recurrent layer), and it is evaluated on a set of MDPs that are drawn either from the same distribution $\mathcal{D}$ or slight modifications of that distribution (to test the generalization capacity of the agent). The internal state is reset at the beginning of the evaluation of any new episode. Since the policy learned by the agent is history-dependent (as it makes uses of a recurrent network), when exposed to any new MDP environment, it is able to adapt and deploy a strategy that optimizes rewards for that task.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Experiments", "weight": 1.0} -->

In order to evaluate the approach to learning that we have just described, we conducted a series of six proof-of-concept experiments, which we present here along with a seventh experiment originally reported in a related paper. One particular point of interest in these experiments was to see whether meta-RL could be used to learn an adaptive balance between exploration and exploitation, as demanded of any fully-fledged RL procedure. A second and still more important focus was on the question of whether meta-RL can give rise to learning that gains efficiency by capitalizing on task structure.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Experiments", "weight": 1.0} -->

In order to examine these questions, we performed four experiments focusing on bandit tasks and two additional experiments focusing on Markov decision problems. All of our experiments (as well as the additional experiment we report) employ a common set of methods, with minor implementational variations. In all experiments, the agent architecture centers on a recurrent neural network feeding into a soft-max output representing discrete actions. As detailed below, the parameters of this network core, as well as some other architectural details, varied across experiments (see Figure 1 and Table 1). However, it is important to emphasize that comparisons between specific architectures are outside the scope of this paper. Our main aim is to illustrate and validate the meta-RL framework in a more general way. To this end, all experiments used the high-level task setup previously described: Both training and testing were organized into fixed-length episodes, each involving a task randomly sampled from a predetermined task distribution, with the LSTM hidden state initialized at the beginning of each episode. Task-specific inputs and action outputs are described in conjunction with individual experiments.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Experiments", "weight": 1.0} -->

In all experiments except where specified, the input included a scalar indicating the reward received on the preceding time-step as well as a one-hot representation of the action sampled on that time-step.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Experiments", "weight": 1.0} -->

All reinforcement learning was conducted using the Advantage Actor-Critic algorithm, as detailed in Mnih et al. and Mirowski et al. (see also Figure 1). Details of training, including the use of entropy regularization and a combined policy and value estimate loss, closely follow the methods detailed in Mirowski et al., with the exception that our experiments used a single thread unless otherwise noted. For a full listing of parameters refer to Table 1.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Bandit problems", "weight": 1.0} -->

As an initial setting for evaluating meta-RL, we studied a series of bandit problems. Except for a very limited set of bandit environments, it is intractable to compute the (prior-dependent) Bayesian-optimal strategy. Here we demonstrate that a recurrent system trained on a set of bandit environments drawn i.i.d. from a given distribution of environments produces a bandit algorithm which performs well on problems drawn from that distribution, and to a certain extent generalizes to related distributions. Thus, meta-RL learns a prior-dependent bandit algorithm.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Bandit problems", "weight": 1.0} -->

The specific bandit instantiation of the general meta-RL procedure described in Section 2.3 is defined as follows. Let $\mathcal{D}$ be a training distribution over bandit environments. The meta-RL system is trained on a sequence of bandit environments through episodes. At the start of a new episode, its LSTM state is reset and a bandit task $b \sim \mathcal{D}$ is sampled. A bandit task is defined as a set of distributions -- one for each arm -- from which rewards are sampled. The agent plays in this bandit environment for a certain number of trials and is trained to maximize observed rewards. After training, the agent's policy is evaluated on a set of bandit tasks that are drawn from a test distribution $\mathcal{D}'$, which can either be the same as $\mathcal{D}$ or a slight modification of it.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Bandit problems", "weight": 1.0} -->

We evaluate the resulting performance of the learned bandit algorithm by the cumulative regret, a measure of the loss (in expected rewards) suffered when playing sub-optimal arms. Writing $\mu_{a}{(b)}$ the expected reward of arm $a$ in bandit environment $b$, and ${\mu^{\ast}{(b)}} = {{\max_{a}\mu_{a}}{(b)}} = {\mu_{a^{\ast}{(b)}}{(b)}}$ (where $a^{\ast}{(b)}$ is one optimal arm) the optimal expected reward, we define the cumulative regret (in environment $b$) as ${R_{T}{(b)}} = {{\sum_{t = 1}^{T}{\mu^{\ast}{(b)}}} - {\mu_{a_{t}}{(b)}}}$, where $a_{t}$ is the arm (action) chosen at time $t$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Bandit problems", "weight": 1.0} -->

In experiment 4 (Restless bandits; Section 3.1.4), $\mu^{\ast}$ also depends on $t$. We report the performance (average over bandit environments drawn from the test distribution) either in terms of the cumulative regret: ${\mathbb{E}}_{b \sim \mathcal{D}'}{\lbrack{R_{T}{(b)}}\rbrack}$ or in terms of number of sub-optimal pulls: ${\mathbb{E}}_{b \sim \mathcal{D}'}{\lbrack{\sum_{t = 1}^{T}{{\mathbb{I}}{\{{a_{t} \neq {a^{\ast}{(b)}}}\}}}}\rbrack}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Bandits with independent arms", "weight": 1.0} -->

We first consider a simple two-armed bandit task to examine the behavior of meta-RL under conditions where theoretical guarantees exist and general purpose algorithms apply. The arm distributions are independent Bernoulli distributions (rewards are $1$ with probability $p$ and $0$ with probability $1 - p$), where the parameters of each arm ($p_{1}$ and $p_{2}$) are sampled independently and uniformly over $\lbrack 0,1\rbrack$. We denote by $\mathcal{D}_{i}$ the corresponding distribution over these independent bandit environments (where the subscript $i$ stands for independent arms).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Bandits with independent arms", "weight": 1.0} -->

At the beginning of each episode, a new bandit task is sampled and held constant for 100 trials. Training lasted for 20,000 episodes. The network is given as input the last reward, last action taken, and the trial number $t$, subsequently producing the action for the next trial $t + 1$ (Figure 1). After training, we evaluated on 300 new episodes with the learning rate set to zero (the learned policy is fixed).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Bandits with independent arms", "weight": 1.0} -->

Across model instances, we randomly sampled learning rate and discount, following Mnih et al.. For all figures, we plotted the average of the top 5 runs of 100 randomly sampled hyperparameter settings, where the top agents were selected from the first half of the 300 evaluation episodes and performance was plotted for the second half. We measured the cumulative expected regret across the episode, comparing with several algorithms tailored for this independent bandit setting: Gittins indices (which is Bayesian optimal in the finite-horizon case), UCB (which comes with theoretical finite-time regret guarantees), and Thompson sampling. Model simulations were conducted with the PymaBandits toolbox from and custom Matlab scripts.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Bandits with independent arms", "weight": 1.0} -->

As shown in Figure 2a (green line; "Independent"), meta-RL outperforms both Thompson sampling (gray dashed line) and UCB (light gray dashed line), although it performs less well compared to Gittins (black dashed line). To verify the critical importance of providing reward information to the LSTM, we removed this input, leaving all other inputs as before. As expected, performance was at chance levels on all bandit tasks.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Bandits with dependent arms (I)", "weight": 1.0} -->

As we have emphasized, a key property of meta-RL is that it gives rise to a learned RL algorithm that exploits consistent structure in the training distribution. In order to garner empirical evidence for this point, we tested the agent from our first experiment in a more structured bandit task. Specifically, we trained the system on two-arm bandits in which arm reward distributions are correlated. In this setting, unlike the one studied in the previous section, experience with either arm provides information about the other. Standard bandit algorithms, including UCB and Thompson sampling, perform suboptimally in this setting, as they are not designed to exploit such correlations. In some cases it is possible to tailor algorithms for specific arm structures, but extensive problem-specific analysis is typically required. Our approach aims to learn a structure-dependent bandit algorithm directly from experience with the target bandit domain.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Bandits with dependent arms (I)", "weight": 1.0} -->

We consider Bernoulli distributions where the parameters $(p_{1},p_{2})$ of the two arms are correlated in the sense that $p_{1} = {1 - p_{2}}$. We consider several training and test distributions. The uniform means that $p_{1} \sim {\mathcal{U}{({\lbrack 0,1\rbrack})}}$ (uniform distribution over the unit interval). The easy means that $p_{1} \sim {\mathcal{U}{({\{ 0.1,0.9\}})}}$ (uniform distribution over those two possible values), and similarly we call medium when $p_{1} \sim {\mathcal{U}{({\{ 0.25,0.75\}})}}$ and hard when $p_{1} \sim {\mathcal{U}{({\{ 0.4,0.6\}})}}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Bandits with dependent arms (I)", "weight": 1.0} -->

We denote by $\mathcal{D}_{u}$, $\mathcal{D}_{e}$, $\mathcal{D}_{m}$, and $\mathcal{D}_{h}$ the corresponding induced distributions over bandit environments. In addition we also considered the independent uniform distribution (as in the previous section, $\mathcal{D}_{i}$) where ${p_{1},p_{2}} \sim {\mathcal{U}{({\lbrack 0,1\rbrack})}}$ independently. Agents were both trained and tested on those five distributions over bandit environments (among which four correspond to correlated distributions: $\mathcal{D}_{u}$, $\mathcal{D}_{e}$, $\mathcal{D}_{m}$ and $\mathcal{D}_{h}$; and one to the independent case: $\mathcal{D}_{i}$).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Bandits with dependent arms (I)", "weight": 1.0} -->

As a validation of the names given to the task distributions ($\mathcal{D}_{e}$, $\mathcal{D}_{m}$, $\mathcal{D}_{h}$), results show that the easy task is easier to learn than the medium which itself is easier than the hard one (Figure 2f). This is compatible with the general notion that the hardness of a bandit problem is inversely proportional to the difference between the expected reward of the optimal and sub-optimal arms. We again note that withholding the reward input to the LSTM resulted in chance performance on even the easiest bandit task, as should be expected.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Bandits with dependent arms (II)", "weight": 1.0} -->

In the previous experiment, the agent could outperform standard bandit algorithms by making use of learned dependencies between arms. However, it could do this while always choosing what it believes to be the highest-paying arm. We next examine a problem where information can be gained by paying a short-term reward cost. Similar problems have been examined before as providing a challenge to standard bandit algorithms. In contrast, humans and animals make decisions that sacrifice immediate reward for information gain.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Bandits with dependent arms (II)", "weight": 1.0} -->

In this experiment, the agent was trained on 11-armed bandits with strong dependencies between arms. All arms had deterministic payouts. Nine "non-target" arms had reward $= 1$, and one "target" arm had reward $= 5$. Meanwhile, arm $a_{11}$ was always "informative", in that the target arm was indexed by 10 times $a_{11}$'s reward (e.g. a reward of 0.2 on $a_{11}$ indicated that $a_{2}$ was the target arm). Thus, $a_{11}$'s payouts ranged from 0.1 to 1. In each episode, the index of the target arm was randomly assigned. On the first trial of each episode, the agent could not know which arm was the target, so the informative arm returned expected reward 0.55 and every target arm returned expected reward 1.4. Choosing the informative arm thus meant foregoing immediate reward, but with the compensation of valuable information. Episodes were five steps long. Again, the reward on the previous trial was provided as an additional observation to the agent.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Bandits with dependent arms (II)", "weight": 1.0} -->

To facilitate learning, this was encoded in 1-hot format.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Bandits with dependent arms (II)", "weight": 1.0} -->

Results are shown in Figure 3 ‣ 3.1 Bandit problems ‣ 3 Experiments ‣ Learning to reinforcement learn"). The agent learned the optimal long-run strategy of sampling the informative arm once, despite the short-term cost, and then using the resulting information to exploit the high-value target arm. Thompson sampling, if supplied the true prior, searched potential target arms and exploited the target if found. UCB performed worse because it sampled every arm once even if the target arm was found early.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Restless bandits", "weight": 1.0} -->

In previous experiments we considered stationary problems where the agent's actions yielded information about task parameters that remained fixed throughout each episode. Next, we consider a bandit problem in which reward probabilities change over the course of an episode, with different rates of change (volatilities) in different episodes. To perform well, the agent must not only track the best arm, but also infer the volatility of the episode and adjust its own learning rate accordingly. In such an environment, learning rates should be higher when the environment is changing rapidly, because past information becomes irrelevant more quickly.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Restless bandits", "weight": 1.0} -->

We tested whether meta-RL would learn such a flexible RL policy using a two-armed Bernoulli bandit task with reward probabilities $p_{1}$ and 1-$p_{1}$. The value of $p_{1}$ changed slowly in "low vol" episodes and quickly in "high vol" episodes. The agent had no way of knowing which type of episode it was, except for its reward history within the episode. Figure 4a shows example "low vol" and "high vol" episodes. Reward magnitude was fixed at 1, and episodes were 100 steps long. UCB and Thompson sampling were again implemented for comparison. The confidence bound term $\sqrt{\frac{\chi{\log n}}{n_{i}}}$ in UCB had parameter $\chi$ which was set to 1, selected empirically for good performance on our data set. Thompson sampling's posterior update included knowledge of the Gaussian random walk, but with a fixed volatility for all episodes.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Restless bandits", "weight": 1.0} -->

As in the previous experiment, meta-RL achieved lower regret in test than Thompson sampling, UCB, or the Rescorla-Wagner (R-W) learning rule with the best fixed learning rate ($\alpha$=0.5). To test whether the agent adjusted its effective learning rate to match environments with different volatility levels, we fit R-W models to the agent's behavior, concatenating episodes into blocks of 10, where each block consisted of only "low vol" or only "high vol" episodes. We considered four different models encompassing different combinations of three parameters: learning rate $\alpha$, softmax inverse temperature $\beta$, and a lapse rate $\epsilon$ to account for unexplained choice variance not related to estimated value Economides et al.. Model "b" included only $\beta$, "ab" included $\alpha$ and $\beta$, "be" included $\beta$ and $\epsilon$, and "abe" included all three. All parameters were estimated separately on each block of 10 episodes.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Restless bandits", "weight": 1.0} -->

In models where $\epsilon$ and $\alpha$ were not free, they were fixed to 0 and 0.5, respectively. Model comparison by Bayesian Information Criterion (BIC) indicated that meta-RL's behavior was better described by a model with different learning rates for each block than a model with a fixed learning rate across blocks. As a control, we performed the same model comparison on the behavior produced by the best R-W agent, finding no benefit of allowing different learning rates across episodes (models "abe" and "ab" vs "be" and "b"; Figure 4c-d). In these models, the parameter estimates for meta-RL's behavior were strongly related to the volatility of the episodes, indicating that meta-RL adjusted its learning rate to the volatility of the episode, whereas model fitting the R-W behavior simply recovered the fixed parameters (Figure 4e-f).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Markov decision problems", "weight": 1.0} -->

The foregoing experiments focused on bandit tasks in which actions do not affect the task's underlying state. We turn now to MDPs where actions do influence state. We begin with a task derived from the neuroscience literature and then turn to a task, originally studied in the context of animal learning, which requires learning of abstract task structure. As in the previous experiments, our focus is on examining how meta-RL adapts to invariances in task structure. We wrap up by reviewing an experiment recently reported in a related paper, which demonstrates how meta-RL can scale to large-scale navigation tasks with rich visual inputs.

<!-- chunk {"id": "body-0038", "role": "body", "section": "The \"two-step task\"", "weight": 1.0} -->

Here we examine meta-RL in a setting that has been widely used in the neuroscience literature to distinguish the contribution of different systems viewed to support decision making. Specifically, this paradigm -- known as the "two-step task" -- was developed to dissociate a model-free system that caches values of actions in states, from a model-based system which learns an internal model of the environment and evaluates the value of actions at the time of decision-making through look-ahead planning. Our interest was in whether meta-RL would give rise to behavior emulating a model-based strategy, despite the use of a model-free algorithm (in this case A2C) to train the system weights.

<!-- chunk {"id": "body-0039", "role": "body", "section": "The \"two-step task\"", "weight": 1.0} -->

We used a modified version of the two-step task, designed to bolster the utility of model-based over model-free control. The task's structure is diagrammed in Figure 5a. From the first-stage state $S_{1}$, action $a_{1}$ leads to second-stage states $S_{2}$ and $S_{3}$ with probability 0.75 and 0.25, respectively, while action $a_{2}$ leads to $S_{2}$ and $S_{3}$ with probabilities 0.25 and 0.75. One second-stage state yielded a reward of 1.0 with probability 0.9 (and otherwise zero); the other yielded the same reward with probability 0.1. The identity of the higher-valued state was assigned randomly for each episode.

<!-- chunk {"id": "body-0040", "role": "body", "section": "The \"two-step task\"", "weight": 1.0} -->

Thus, the expected values for the two first-stage actions were either $r_{a}$ = 0.9 and $r_{b}$ = 0.1, or $r_{a}$ = 0.1 and $r_{b}$ = 0.9. All three states were represented by one-hot vectors, with the transition model held constant across episodes: i.e. only the expected value of the second stage states changed from episode to episode.

<!-- chunk {"id": "body-0041", "role": "body", "section": "The \"two-step task\"", "weight": 1.0} -->

We applied the conventional analysis used in the neuroscience literature to dissociate model-free from model-based control. This focuses on the "stay probability," that is, the probability with which a first-stage action is selected at trial $t + 1$ following a second-stage reward at trial $t$, as a function of whether trial $t$ involved a common transition (e.g. action $a_{1}$ at state $S_{1}$ led to $S_{2}$) or rare transition (action $a_{2}$ at state $S_{1}$ led to $S_{3}$). Under the standard interpretation, model-free control -- à la TD -- predicts that there should be a main effect of reward: First-stage actions will tend to be repeated if followed by reward, regardless of transition type, and such actions will tend not to be repeated (choice switch) if followed by non-reward (Figure 5b). In contrast, model-based control predicts an interaction between the reward and transition type, reflecting a more goal-directed strategy, which takes the transition structure into account.

<!-- chunk {"id": "body-0042", "role": "body", "section": "The \"two-step task\"", "weight": 1.0} -->

Intuitively, if you receive a second-stage reward (e.g. at $S_{2}$) following a rare transition (i.e. having taken action $a_{2}$ at state $S_{1}$), to maximize your chances of getting to this reward on the next trial based on your knowledge of the transition structure, the optimal first stage action is $a_{1}$ (i.e. switch).

<!-- chunk {"id": "body-0043", "role": "body", "section": "The \"two-step task\"", "weight": 1.0} -->

The results of the stay-probability analysis performed on the agent's choices show a pattern conventionally interpreted as implying the operation of model-based control (Figure 5c). As in previous experiments, when reward information was withheld at the level of network input, performance was at chance levels.

<!-- chunk {"id": "body-0044", "role": "body", "section": "The \"two-step task\"", "weight": 1.0} -->

If interpreted following standard practice in neuroscience, the behavior of the model in this experiment reflects a surprising effect: training with model-free RL gives rise to behavior reflecting model-based control. We hasten to note that different interpretations of the observed pattern of behavior are available, a point to which we will return below. However, notwithstanding this caveat, the results of the present experiment provide a further illustration of the point that the learning procedure that emerges from meta-RL can differ starkly from the original RL algorithm used to train the network weights, and takes a form that exploits consistent task structure.

<!-- chunk {"id": "body-0045", "role": "body", "section": "The \"two-step task\"", "weight": 1.0} -->

(c) LSTM A2C with reward input Figure 5: Three-state MDP modeled after the “two-step task” from Daw et al.. (a) MDP with 3 states and 2 actions. All trials start in state S1, with transition probabilities after taking actions a1 or a2 depicted in the graph. S2 and S3 result in expected rewards ra and rb (see text). (b) Predictions of choice probabilities given either a model-based strategy or a model-free strategy. Specifically, model-based strategies take into account transition probabilities and would predict an interaction between the amount of reward received on the last trial and the transition (common or uncommon) observed. (c) Agent displays a perfectly model-based profile when given the reward as input.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Learning abstract task structure", "weight": 1.0} -->

In the final experiment we conducted, we took a step towards examining the scalabilty of meta-RL, by studying a task that involves rich visual inputs, longer time horizons and sparse rewards. Additionally, in this experiment we studied a meta-learning task that requires the system to tune into an abstract task structure, in which a series of objects play defined roles which the system must infer.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Learning abstract task structure", "weight": 1.0} -->

The task was adapted from a classic study of animal behavior, conducted by Harlow. On each trial in the original task, Harlow presented a monkey with two visually contrasting objects. One of these covered a small well containing a morsel of food; the other covered an empty well. The animal chose freely between the two objects and could retrieve the food reward if present. The stage was then hidden and the left-right positions of the objects were randomly reset. A new trial then began, with the animal again choosing freely. This process continued for a set number of trials using the same two objects. At completion of this set of trials, two entirely new and unfamiliar objects were substituted for the original two, and the process began again. Importantly, within each block of trials, one object was chosen to be consistently rewarded (regardless of its left-right position), with the other being consistently unrewarded. What Harlow observed was that, after substantial practice, monkeys displayed behavior that reflected an understanding of the task's rules. When two new objects were presented, the monkey's first choice between them was necessarily arbitrary. But after observing the outcome of this first choice, the monkey was at ceiling thereafter, always choosing the rewarded object.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Learning abstract task structure", "weight": 1.0} -->

We anticipated that meta-RL should give rise to the same pattern of abstract one-shot learning. In order to test this, we adapted Harlow's paradigm into a visual fixation task, as follows. A 84x84 pixel input represented a simulated computer screen (see Figure 6a-c). At the beginning of each trial, this display was blank except for a small central fixation cross (red crosshairs). The agent selected discrete left-right actions which shifted its view approximately 4.4 degrees in the corresponding direction, with a small momentum effect (alternatively, a no-op action could be selected). The completion of a trial required performing two tasks: saccading to the central fixation cross, followed by saccading to the correct image. If the agent held the fixation cross in the center of the field of view (within a tolerance of 3.5 degrees visual angle) for a minimum of four time steps, it received a reward of 0.2. The fixation cross then disappeared and two images -- drawn randomly from the ImageNet dataset and resized to 34x34 -- appeared on the left and right side of the display (Figure 6b).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Learning abstract task structure", "weight": 1.0} -->

The agent's task was then to "select" one of the images by rotating until the center of the image aligned with the center of the visual field of view (within a tolerance of 7 degrees visual angle). Once one of the images was selected, both images disappeared and, after an intertrial interval of 10 time-steps, the fixation cross reappeared, initiating the next trial. Each episode contained a maximum of 10 trials or 3600 steps. Following Mirowski et al., we implemented an action repeat of 4, meaning that selecting an image took a minimum of three independent decisions (twelve primitive actions) after having completed the fixation. It should be noted, however, that the rotational position of the agent was not limited; that is, 360 degree rotations could occur, while the simulated computer screen only subtended 65 degrees.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Learning abstract task structure", "weight": 1.0} -->

Although new ImageNet images were chosen at the beginning of each episode (sampled with replacement from a set of 1000 images), the same images were re-used across all trials within an episode, though in randomly varying left-right placement, similar to the objects in Harlow's experiment. And as in that experiment, one image was arbitrarily chosen to be the "rewarded" image throughout the episode. Selection of this image yielded a reward of 1.0, while the other image yielded a reward of -1.0. During test, the A3C learning rate was set to zero and ImageNet images were drawn from a separate held-out set of 1000, never presented during training.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Learning abstract task structure", "weight": 1.0} -->

A grid search was conducted for optimal hyperparameters. At perfect performance, agents can complete one trial per 20-30 steps and achieve a maximum expected reward of 9 per 10 trials. Given the nature of the task -- which requires one-shot image-reward memory together with maintenance of this information over a relatively long timescale (i.e. over fixation-cross selections and across trials) -- we assessed the performance of not only a convolutional-LSTM architecture which receives reward and action as additional input (see Figure 1b and Table 1), but also a convolutional-stacked LSTM architecture used in a navigation task discussed below (see Figure 1c).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Learning abstract task structure", "weight": 1.0} -->

Agent performance is illustrated in Figure 6d-f. Whilst the single LSTM agent was relatively successful at solving the task, the stacked-LSTM variant exhibited much better robustness. That is, 43% of random seeds of the best hyperparameter set performed at ceiling (Figure 6e), compared to 26% of the single LSTM.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Learning abstract task structure", "weight": 1.0} -->

Like the monkeys in Harlow's experiment, the networks converge on an optimal policy: Not only does the agent successfully fixate to begin each trial, but starting on the second trial of each episode it invariably selects the rewarded image, regardless of which image it selected on the first trial(Figure 6f). This reflects an impressive form of one-shot learning, which reflects an implicit understanding of the task structure: After observing one trial outcome, the agent binds a complex, unfamiliar image to a specific task role.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Learning abstract task structure", "weight": 1.0} -->

Further experiments, reported elsewhere, confirmed that the same recurrent A3C system is also able to solve a substantially more difficult version of the task. In this task, only one image -- which was randomly designated to be either the rewarding item to be selected, or the unrewarding item to be avoided -- was presented on every trial during an episode, with the other image presented being novel on every trial.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Learning abstract task structure", "weight": 1.0} -->

(c) Right saccade and selection (e) Robustness over random seeds Figure 6: Learning abstract task structure in visually rich 3D environment. a-c) Example of a single trial, beginning with a central fixation, followed by two images with random left-right placement. d) Average performance (measured in average reward per trial) of top 40 out of 100 seeds during training. Maximum expected performance is indicated with black dashed line. e) Performance at episode 100,000 for 100 random seeds, in decreasing order of performance. f) Probability of selecting the rewarded image, as a function of trial number for a single A3C stacked LSTM agent for a range of training durations (episodes per thread, 32 threads).

<!-- chunk {"id": "body-0056", "role": "body", "section": "One-shot navigation", "weight": 1.0} -->

The experiments using the Harlow task demonstrate the capacity of meta-RL to operate effectively within a visually rich environment, with relatively long time horizons. Here we consider related experiments recently reported within the navigation domain, and discuss how these can be recast as examples of meta-RL -- attesting to the scaleability of this principle to more typical MDP settings that pose challenging RL problems due to dynamically changing sparse rewards.

<!-- chunk {"id": "body-0057", "role": "body", "section": "One-shot navigation", "weight": 1.0} -->

Specifically, we consider a setting where the environment layout is fixed but the goal changes location randomly each episode. Although the layout is relatively simple, the Labyrinth environment is richer and more finely discretized (cf VizDoom), resulting in long time horizons; a trained agent takes approximately 100 steps (10 seconds) to reach the goal for the first time in a given episode. Results show that a stacked LSTM architecture (Figure 1c), that receives reward and action as additional inputs equivalent to that used in our Harlow experiment achieves near-optimal behavior -- showing one-shot memory for the goal location after an initial exploratory period, followed by repeated exploitation (see Figure 7c). This is evidenced by a substantial decrease in latency to reach the goal for the first time (\~100 timesteps) compared to subsequent visits (\~30 timesteps). Notably, a feedforward network (see Figure 7c), that receives only a single image as observation, is unable to solve the task (i.e. no decrease in latency between successive goal rewards).

<!-- chunk {"id": "body-0058", "role": "body", "section": "One-shot navigation", "weight": 1.0} -->

Whilst not interpreted as such in Mirowski et al., this provides a clear demonstration of the effectiveness of meta-RL: a separate RL algorithm with the capability of one-shot learning emerges through training with a fixed and more incremental RL algorithm (i.e. policy gradient). Meta-RL can be viewed as allowing the agent to infer the optimal value function following initial exploration (see Figure 7d) -- with the additional LSTM providing information about the currently relevant goal location to the LSTM that outputs the policy over the extended timeframe of the episode. Taken together, meta-RL allows a base model-free RL algorithm to solve a challenging RL problem that might otherwise require fundamentally different approaches (e.g. based on successor representations or fully model-based RL).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusion", "weight": 1.5} -->

A current challenge in artificial intelligence is to design agents that can adapt rapidly to new tasks by leveraging knowledge acquired through previous experience with related activities. In the present work we have reported initial explorations of what we believe is one promising avenue toward this goal. Deep meta-RL involves a combination of three ingredients: Use of a deep RL algorithm to train a recurrent neural network, a training set that includes a series of interrelated tasks, network input that includes the action selected and reward received in the previous time interval. The key result, which emerges naturally from the setup rather than being specially engineered, is that the recurrent network dynamics learn to implement a second RL procedure, independent from and potentially very different from the algorithm used to train the network weights. Critically, this learned RL algorithm is tuned to the shared structure of the training tasks. In this sense, the learned algorithm builds in domain-appropriate biases, which can allow it to operate with greater efficiency than a general-purpose algorithm.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This bias effect was particularly evident in the results of our experiments involving dependent bandits (sections 3.1.2 and 3.1.3), where the system learned to take advantage of the task's covariance structure; and in our study of Harlow's animal learning task (section 3.2.2), where the recurrent network learned to exploit the task's structure in order to display one-shot learning with complex novel stimuli.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion", "weight": 1.5} -->

One of our experiments (section 3.2.1) illustrated the point that a system trained using a model-free RL algorithm can develop behavior that emulates model-based control. A few further comments on this result are warranted. As noted in our presentation of the simulation results, the pattern of choice behavior displayed by the network has been considered in the cognitive and neuroscience literatures as reflecting model-based control or tree search. However, as has been remarked in very recent work, the same pattern can arise from a model-free system with an appropriate state representation. Indeed, we suspect this may be how our network in fact operates. However, other findings suggest that a more explicitly model-based control mechanism can emerge when a similar system is trained on a more diverse set of tasks. In particular, Ilin et al. showed that recurrent networks trained on random mazes can approximate dynamic programming procedures. At the same time, as we have stressed, we consider it an important aspect of deep meta-RL that it yields a learned RL algorithm that capitalizes on invariances in task structure.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion", "weight": 1.5} -->

As a result, when faced with widely varying but still structured environments, deep meta-RL seems likely to generate RL procedures that occupy a grey area between model-free and model-based RL.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The two-step decision problem studied in Section 3.2.1 was derived from neuroscience, and we believe deep meta-RL may have important implications in that arena. The notion of meta-RL has been discussed previously in neuroscience but only in a narrow sense, according to which meta-learning adjusts scalar hyperparameters such as the learning rate or softmax inverse temperature. In recent work we have shown that deep meta-RL can account for a wider range of experimental observations, providing an integrative framework for understanding the respective roles of dopamine and the prefrontal cortex in biological reinforcement learning.
