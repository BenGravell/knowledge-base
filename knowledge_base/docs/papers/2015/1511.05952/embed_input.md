<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Prioritized Experience Replay

Topics include Reinforcement learning, Online algorithms, Learning, Prioritized experience replay, DQN.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Experience replay lets online reinforcement learning agents remember and reuse experiences from the past. In prior work, experience transitions were uniformly sampled from a replay memory. However, this approach simply replays transitions at the same frequency that they were originally experienced, regardless of their significance. In this paper we develop a framework for prioritizing experience, so as to replay important transitions more frequently, and therefore learn more efficiently. We use prioritized experience replay in Deep Q-Networks (DQN), a reinforcement learning algorithm that achieved human-level performance across many Atari games. DQN with prioritized experience replay achieves a new state-of-the-art, outperforming DQN with uniform replay on 41 out of 49 games.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Online reinforcement learning (RL) agents incrementally update their parameters (of the policy, value function or model) while they observe a stream of experience. In their simplest form, they discard incoming data immediately, after a single update. Two issues with this are (a) strongly correlated updates that break the i.i.d. assumption of many popular stochastic gradient-based algorithms, and (b) the rapid forgetting of possibly rare experiences that would be useful later.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Experience replay* addresses both of these issues: with experience stored in a replay memory, it becomes possible to break the temporal correlations by mixing more and less recent experience for the updates, and rare experience will be used for more than just a single update. This was demonstrated in the Deep Q-Network (DQN) algorithm, which stabilized the training of a value function, represented by a deep neural network, by using experience replay. Specifically, DQN used a large sliding window replay memory, sampled from it uniformly at random, and revisited each transition^11^1 A transition is the atomic unit of interaction in RL, in our case a tuple of (state $S_{t - 1}$, action $A_{t - 1}$, reward $R_{t}$, discount $\gamma_{t}$, next state $S_{t}$). We choose this for simplicity, but most of the arguments in this paper also hold for a coarser ways of chunking experience, e.g. into sequences or episodes. eight times on average.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In general, experience replay can reduce the amount of experience required to learn, and replace it with more computation and more memory -- which are often cheaper resources than the RL agent's interactions with its environment.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we investigate how *prioritizing* which transitions are replayed can make experience replay more efficient and effective than if all transitions are replayed uniformly. The key idea is that an RL agent can learn more effectively from some transitions than from others. Transitions may be more or less surprising, redundant, or task-relevant. Some transitions may not be immediately useful to the agent, but might become so when the agent competence increases. Experience replay liberates online learning agents from processing transitions in the exact order they are experienced. Prioritized replay further liberates agents from considering transitions with the same frequency that they are experienced.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, we propose to more frequently replay transitions with high expected learning progress, as measured by the magnitude of their temporal-difference (TD) error. This prioritization can lead to a loss of diversity, which we alleviate with stochastic prioritization, and introduce bias, which we correct with importance sampling. Our resulting algorithms are robust and scalable, which we demonstrate on the Atari 2600 benchmark suite, where we obtain faster learning and state-of-the-art performance.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Prioritized Replay", "weight": 1.0} -->

Using a replay memory leads to design choices at two levels: which experiences to store, and which experiences to replay (and how to do so). This paper addresses only the latter: making the most effective use of the replay memory for learning, assuming that its contents are outside of our control (but see also Section 6).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Motivating Example", "weight": 1.0} -->

To understand the potential gains of prioritization, we introduce an artificial 'Blind Cliffwalk' environment (described in Figure 1, left) that exemplifies the challenge of exploration when rewards are rare. With only $n$ states, the environment requires an exponential number of random steps until the first non-zero reward; to be precise, the chance that a random sequence of actions will lead to the reward is $2^{- n}$. Furthermore, the most relevant transitions (from rare successes) are hidden in a mass of highly redundant failure cases (similar to a bipedal robot falling over repeatedly, before it discovers how to walk).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Motivating Example", "weight": 1.0} -->

We use this example to highlight the difference between the learning times of two agents. Both agents perform Q-learning updates on transitions drawn from the same replay memory. The first agent replays transitions uniformly at random, while the second agent invokes an oracle to prioritize transitions. This oracle greedily selects the transition that maximally reduces the global loss in its current state (in hindsight, after the parameter update). For the details of the setup, see Appendix B.1. Figure 1 (right) shows that picking the transitions in a good order can lead to exponential speed-ups over uniform choice. Such an oracle is of course not realistic, yet the large gap motivates our search for a practical approach that improves on uniform random replay.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Prioritizing with TD-error", "weight": 1.0} -->

The central component of prioritized replay is the criterion by which the importance of each transition is measured. One idealised criterion would be the amount the RL agent can learn from a transition in its current state (expected learning progress). While this measure is not directly accessible, a reasonable proxy is the magnitude of a transition's TD error $\delta$, which indicates how 'surprising' or unexpected the transition is: specifically, how far the value is from its next-step bootstrap estimate. This is particularly suitable for incremental, online RL algorithms, such as SARSA or Q-learning, that already compute the TD-error and update the parameters in proportion to $\delta$. The TD-error can be a poor estimate in some circumstances as well, e.g. when rewards are noisy; see Appendix A for a discussion of alternatives.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Prioritizing with TD-error", "weight": 1.0} -->

To demonstrate the potential effectiveness of prioritizing replay by TD error, we compare the uniform and oracle baselines in the Blind Cliffwalk to a 'greedy TD-error prioritization' algorithm. This algorithm stores the last encountered TD error along with each transition in the replay memory. The transition with the largest absolute TD error is replayed from the memory. A Q-learning update is applied to this transition, which updates the weights in proportion to the TD error. New transitions arrive without a known TD-error, so we put them at maximal priority in order to guarantee that all experience is seen at least once. Figure 2 (left), shows that this algorithm results in a substantial reduction in the effort required to solve the Blind Cliffwalk task.^22^2 Note that a random (or optimistic) initialization of the Q-values is necessary with greedy prioritization. If initializing with zero instead, unrewarded transitions would appear to have zero error initially, be placed at the bottom of the queue, and not be revisited until the error on other transitions drops below numerical precision.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Prioritizing with TD-error", "weight": 1.0} -->

Implementation: To scale to large memory sizes $N$, we use a binary heap data structure for the priority queue, for which finding the maximum priority transition when sampling is $O{}$ and updating priorities (with the new TD-error after a learning step) is $O{({\log N})}$. See Appendix B.2.1 for more details.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Stochastic Prioritization", "weight": 1.0} -->

However, greedy TD-error prioritization has several issues. First, to avoid expensive sweeps over the entire replay memory, TD errors are only updated for the transitions that are replayed. One consequence is that transitions that have a low TD error on first visit may not be replayed for a long time (which means effectively never with a sliding window replay memory). Further, it is sensitive to noise spikes (e.g. when rewards are stochastic), which can be exacerbated by bootstrapping, where approximation errors appear as another source of noise. Finally, greedy prioritization focuses on a small subset of the experience: errors shrink slowly, especially when using function approximation, meaning that the initially high error transitions get replayed frequently. This lack of diversity that makes the system prone to over-fitting.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Stochastic Prioritization", "weight": 1.0} -->

To overcome these issues, we introduce a stochastic sampling method that interpolates between pure greedy prioritization and uniform random sampling. We ensure that the probability of being sampled is monotonic in a transition's priority, while guaranteeing a non-zero probability even for the lowest-priority transition. Concretely, we define the probability of sampling transition $i$ as

<!-- chunk {"id": "body-0016", "role": "body", "section": "Stochastic Prioritization", "weight": 1.0} -->

where $p_{i} > 0$ is the priority of transition $i$. The exponent $\alpha$ determines how much prioritization is used, with $\alpha = 0$ corresponding to the uniform case.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Stochastic Prioritization", "weight": 1.0} -->

The first variant we consider is the direct, proportional prioritization where $p_{i} = {{|\delta_{i}|} + \epsilon}$, where $\epsilon$ is a small positive constant that prevents the edge-case of transitions not being revisited once their error is zero. The second variant is an indirect, rank-based prioritization where $p_{i} = \frac{1}{{rank}{(i)}}$, where ${rank}{(i)}$ is the rank of transition $i$ when the replay memory is sorted according to $|\delta_{i}|$. In this case, $P$ becomes a power-law distribution with exponent $\alpha$. Both distributions are monotonic in $|\delta|$, but the latter is likely to be more robust, as it is insensitive to outliers. Both variants of stochastic prioritization lead to large speed-ups over the uniform baseline on the Cliffwalk task, as shown on Figure 2 (right).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Stochastic Prioritization", "weight": 1.0} -->

Implementation: To efficiently sample from distribution, the complexity cannot depend on $N$. For the rank-based variant, we can approximate the cumulative density function with a piecewise linear function with $k$ segments of equal probability. The segment boundaries can be precomputed (they change only when $N$ or $\alpha$ change). At runtime, we sample a segment, and then sample uniformly among the transitions within it. This works particularly well in conjunction with a minibatch-based learning algorithm: choose $k$ to be the size of the minibatch, and sample exactly one transition from each segment -- this is a form of stratified sampling that has the added advantage of balancing out the minibatch (there will always be exactly one transition with high magnitude $\delta$, one with medium magnitude, etc). The proportional variant is different, also admits an efficient implementation based on a 'sum-tree' data structure (where every node is the sum of its children, with the priorities as the leaf nodes), which can be efficiently updated and sampled. See Appendix B.2.1 for more additional details.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Annealing the Bias", "weight": 1.0} -->

The estimation of the expected value with stochastic updates relies on those updates corresponding to the same distribution as its expectation. Prioritized replay introduces bias because it changes this distribution in an uncontrolled fashion, and therefore changes the solution that the estimates will converge to (even if the policy and state distribution are fixed). We can correct this bias by using importance-sampling (IS) weights

<!-- chunk {"id": "body-0020", "role": "body", "section": "Annealing the Bias", "weight": 1.0} -->

that fully compensates for the non-uniform probabilities $P{(i)}$ if $\beta = 1$. These weights can be folded into the Q-learning update by using $w_{i}\delta_{i}$ instead of $\delta_{i}$. For stability reasons, we always normalize weights by $1/{\max_{i}w_{i}}$ so that they only scale the update downwards.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Annealing the Bias", "weight": 1.0} -->

In typical reinforcement learning scenarios, the unbiased nature of the updates is most important near convergence at the end of training, as the process is highly non-stationary anyway, due to changing policies, state distributions and bootstrap targets; we hypothesize that a small bias can be ignored in this context (see also Figure 12 in the appendix for a case study of full IS correction on Atari). We therefore exploit the flexibility of *annealing* the amount of importance-sampling correction over time, by defining a schedule on the exponent $\beta$ that reaches $1$ only at the end of learning. In practice, we linearly anneal $\beta$ from its initial value $\beta_{0}$ to $1$. Note that the choice of this hyperparameter interacts with choice of prioritization exponent $\alpha$; increasing both simultaneously prioritizes sampling more aggressively at the same time as correcting for it more strongly.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Annealing the Bias", "weight": 1.0} -->

Importance sampling has another benefit when combined with prioritized replay in the context of non-linear function approximation (e.g. deep neural networks): here large steps can be very disruptive, because the first-order approximation of the gradient is only reliable locally, and have to be prevented with a smaller global step-size. In our approach instead, prioritization makes sure high-error transitions are seen many times, while the IS correction reduces the gradient magnitudes (and thus the effective step size in parameter space), and allowing the algorithm follow the curvature of highly non-linear optimization landscapes because the Taylor expansion is constantly re-approximated.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Annealing the Bias", "weight": 1.0} -->

We combine our prioritized replay algorithm into a full-scale reinforcement learning agent, based on the state-of-the-art Double DQN algorithm. Our principal modification is to replace the uniform random sampling used by Double DQN with our stochastic prioritization and importance sampling methods (see Algorithm 1).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Annealing the Bias", "weight": 1.0} -->

1: Input: minibatch k, step-size η, replay period K and size N, exponents α and β, budget T.
2: Initialize replay memory ℋ = ⌀, Δ = 0, p1 = 1
3: Observe S0 and choose A0 ∼ πθ (S0)
6: Store transition (St − 1,At − 1,Rt,γt,St) in ℋ with maximal priority pt = maxi &lt; tpi
9: Sample transition j ∼ P (j) = pjα/∑ipiα
10: Compute importance-sampling weight wj = (N ⋅ P (j))−β/maxiwi
11: Compute TD-error δj = Rj + γj Qtarget (Sj,arg maxaQ (Sj,a)) − Q (Sj − 1,Aj − 1)
12: Update transition priority pj ← |δj|
15: Update weights θ ← θ + η ⋅ Δ, reset Δ = 0
16: From time to time copy weights into target network θtarget ← θ
Algorithm 1 Double DQN with proportional prioritization

<!-- chunk {"id": "body-0025", "role": "body", "section": "Atari Experiments", "weight": 1.0} -->

With all these concepts in place, we now investigate to what extent replay with such prioritized sampling can improve performance in realistic problem domains. For this, we chose the collection of Atari benchmarks with their end-to-end RL from vision setup, because they are popular and contain diverse sets of challenges, including delayed credit assignment, partial observability, and difficult function approximation. Our hypothesis is that prioritized replay is generally useful, so that it will make learning with experience replay more efficient without requiring careful problem-specific hyperparameter tuning.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Atari Experiments", "weight": 1.0} -->

We consider two baseline algorithms that use uniform experience replay, namely the version of the DQN algorithm from the Nature paper, and its recent extension Double DQN that substantially improved the state-of-the-art by reducing the over-estimation bias with Double Q-learning. Throughout this paper we use the tuned version of the Double DQN algorithm. For this paper, the most relevant component of these baselines is the replay mechanism: all experienced transitions are stored in a sliding window memory that retains the last $10^{6}$ transitions. The algorithm processes minibatches of 32 transitions sampled uniformly from the memory. One minibatch update is done for each 4 new transitions entering the memory, so all experience is replayed 8 times on average. Rewards and TD-errors are clipped to fall within $\lbrack{- 1},1\rbrack$ for stability reasons.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Atari Experiments", "weight": 1.0} -->

We use the identical neural network architecture, learning algorithm, replay memory and evaluation setup as for the baselines (see Appendix B.2). The only difference is the mechanism for sampling transitions from the replay memory, with is now done according to Algorithm 1 instead of uniformly. We compare the baselines to both variants of prioritized replay (rank-based and proportional).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Atari Experiments", "weight": 1.0} -->

Only a single hyperparameter adjustment was necessary compared to the baseline: Given that prioritized replay picks high-error transitions more often, the typical gradient magnitudes are larger, so we reduced the step-size $\eta$ by a factor 4 compared to the (Double) DQN setup. For the $\alpha$ and $\beta_{0}$ hyperparameters that are introduced by prioritization, we did a coarse grid search (evaluated on a subset of 8 games), and found the sweet spot to be $\alpha = 0.7$, $\beta_{0} = 0.5$ for the rank-based variant and $\alpha = 0.6$, $\beta_{0} = 0.4$ for the proportional variant. These choices are trading off aggressiveness with robustness, but it is easy to revert to a behavior closer to the baseline by reducing $\alpha$ and/or increasing $\beta$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Atari Experiments", "weight": 1.0} -->

We produce the results by running each variant with a single hyperparameter setting across all games, as was done for the baselines. Our main evaluation metric is the *quality of the best policy*, in terms of average score per episode, given start states sampled from human traces. These results are summarized in Table 1 and Figure 3, but full results and raw scores can be found in Tables 7 and 6 in the Appendix. A secondary metric is the *learning speed*, which we summarize on Figure 4, with more detailed learning curves on Figures 7 and 8.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Atari Experiments", "weight": 1.0} -->

DQN Double DQN (tuned) baseline rank-based baseline rank-based proportional Median 48% 106% 111% 113% 128% Mean 122% 355% 418% 454% 551% &gt; baseline – 41 – 38 42 &gt; human 15 25 30 33 33 # games 49 49 57 57 57
Table 1: Summary of normalized scores. See Table 6 in the appendix for full results.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Atari Experiments", "weight": 1.0} -->

We find that adding prioritized replay to DQN leads to a substantial improvement in score on 41 out of 49 games (compare columns 2 and 3 of Table 6 or Figure 9 in the appendix), with the median normalized performance across 49 games increasing from $48\%$ to $106\%$. Furthermore, we find that the boost from prioritized experience replay is *complementary* to the one from introducing Double Q-learning into DQN: performance increases another notch, leading to the current state-of-the-art on the Atari benchmark (see Figure 3). Compared to Double DQN, the median performance across 57 games increased from $111\%$ to $128\%$, and the mean performance from $418\%$ to $551\%$ bringing additional games such as River Raid, Seaquest and Surround to a human level for the first time, and making large jumps on others (e.g. Gopher, James Bond 007 or Space Invaders). Note that mean performance is not a very reliable metric because a single game (Video Pinball) has a dominant contribution.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Atari Experiments", "weight": 1.0} -->

Prioritizing replay gives a performance boost on almost all games, and on aggregate, learning is twice as fast (see Figures 4 and 8). The learning curves on Figure 7 illustrate that while the two variants of prioritization usually lead to similar results, there are games where one of them remains close to the Double DQN baseline while the other one leads to a big boost, for example Double Dunk or Surround for the rank-based variant, and Alien, Asterix, Enduro, Phoenix or Space Invaders for the proportional variant. Another observation from the learning curves is that compared to the uniform baseline, prioritization is effective at reducing the delay until performance gets off the ground in games that otherwise suffer from such a delay, such as Battlezone, Zaxxon or Frostbite.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Discussion", "weight": 1.5} -->

In the head-to-head comparison between rank-based prioritization and proportional prioritization, we expected the rank-based variant to be more robust because it is not affected by outliers nor error magnitudes. Furthermore, its heavy-tail property also guarantees that samples will be diverse, and the stratified sampling from partitions of different errors will keep the total minibatch gradient at a stable magnitude throughout training. On the other hand, the ranks make the algorithm blind to the relative error scales, which could incur a performance drop when there is structure in the distribution of errors to be exploited, such as in sparse reward scenarios. Perhaps surprisingly, both variants perform similarly in practice; we suspect this is due to the heavy use of clipping (of rewards and TD-errors) in the DQN algorithm, which removes outliers. Monitoring the distribution of TD-errors as a function of time for a number of games (see Figure 10 in the appendix), and found that it becomes close to a heavy-tailed distribution as learning progresses, while still differing substantially across games; this empirically validates the form of Equation 1.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Discussion", "weight": 1.5} -->

Figure 11, in the appendix, shows how this distribution interacts with Equation 1 to produce the effective replay probabilities.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Discussion", "weight": 1.5} -->

While doing this analysis, we stumbled upon another phenomenon (obvious in retrospect), namely that some fraction of the visited transitions are never replayed before they drop out of the sliding window memory, and many more are replayed for the first time only long after they are encountered. Also, uniform sampling is implicitly biased toward out-of-date transitions that were generated by a policy that has typically seen hundreds of thousands of updates since. Prioritized replay with its bonus for unseen transitions directly corrects the first of these issues, and also tends to help with the second one, as more recent transitions tend to have larger error -- this is because old transitions will have had more opportunities to have them corrected, and because novel data tends to be less well predicted by the value function.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Discussion", "weight": 1.5} -->

We hypothesize that deep neural networks interact with prioritized replay in another interesting way. When we distinguish learning the value given a representation (i.e., the top layers) from learning an improved representation (i.e., the bottom layers), then transitions for which the representation is good will quickly reduce their error and then be replayed much less, increasing the learning focus on others where the representation is poor, thus putting more resources into distinguishing aliased states -- if the observations and network capacity allow for it.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Extensions", "weight": 1.0} -->

Prioritized Supervised Learning: The analogous approach to prioritized replay in the context of supervised learning is to sample non-uniformly from the dataset, each sample using a priority based on its last-seen error. This can help focus the learning on those samples that can still be learned, devoting additional resources to the (hard) boundary cases, somewhat similarly to boosting. Furthermore, if the dataset is imbalanced, we hypothesize that samples from the rare classes will be sampled disproportionately often, because their errors shrink less fast, and the chosen samples from the common classes will be those nearest to the decision boundaries, leading to an effect similar to hard negative mining. To check whether these intuitions hold, we conducted a preliminary experiment on a class-imbalanced variant of the classical MNIST digit classification problem, where we removed $99\%$ of the samples for digits $0,1,2,3,4$ in the training set, while leaving the test/validation sets untouched (i.e., those retain class balance).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Extensions", "weight": 1.0} -->

We compare two scenarios: in the informed case, we reweight the errors of the impoverished classes artificially (by a factor $100$), in the uninformed scenario, we provide no hint that the test distribution will differ from the training distribution. See Appendix B.3 for the details of the convolutional neural network training setup. Prioritized sampling (uninformed, with $\alpha = 1$, $\beta = 0$) outperforms the uninformed uniform baseline, and approaches the performance of the informed uniform baseline in terms of generalization (see Figure 5); again, prioritized training is also faster in terms of learning speed.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Extensions", "weight": 1.0} -->

Off-policy Replay: Two standard approaches to off-policy RL are rejection sampling and using importance sampling ratios $\rho$ to correct for how likely a transition would have been on-policy. Our approach contains analogues to both these approaches, the replay probability $P$ and the IS-correction $w$. It appears therefore natural to apply it to off-policy RL, if transitions are available in a replay memory. In particular, we recover weighted IS with $w = \rho$, $\alpha = 0$, $\beta = 1$ and rejection sampling with $p = {\min{(1;\rho)}}$, $\alpha = 1$, $\beta = 0$, in the proportional variant. Our experiments indicate that intermediate variants, possibly with annealing or ranking, could be more useful in practice -- especially when IS ratios introduce high variance, i.e., when the policy of interest differs substantially from the behavior policy in some states.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Extensions", "weight": 1.0} -->

Of course, off-policy correction is complementary to our prioritization based on expected learning progress, and the same framework can be used for a hybrid prioritization by defining $p = {\rho \cdot {|\delta|}}$, or some other sensible trade-off based on both $\rho$ and $\delta$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Extensions", "weight": 1.0} -->

Feedback for Exploration: An interesting side-effect of prioritized replay is that the total number $M_{i}$ that a transition will end up being replayed varies widely, and this gives a rough indication of how useful it was to the agent. This potentially valuable signal can be fed back to the exploration strategy that generates the transitions. For example, we could sample exploration hyperparameters (such as the fraction of random actions $\epsilon$, the Boltzmann temperature, or the amount of of intrinsic reward to mix in) from a parametrized distribution at the beginning of each episode, monitor the usefulness of the experience via $M_{i}$, and update the distribution toward generating more useful experience. Or, in a parallel system like the Gorila agent, it could guide resource allocation between a collection of concurrent but heterogeneous 'actors', each with different exploration hyperparameters.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Extensions", "weight": 1.0} -->

Prioritized Memories: Considerations that help determine which transitions to replay are likely to also be relevant for determining which memories to store and when to erase them (e.g. when it becomes likely that they will never be replayed anymore). An explicit control over which memories to keep or erase can help reduce the required total memory size, because it reduces redundancy (frequently visited transitions will have low error, so many of them will be dropped), while automatically adjusting for what has been learned already (dropping many of the 'easy' transitions) and biasing the contents of the memory to where the errors remain high. This is a non-trivial aspect, because memory requirements for DQN are currently dominated by the size of the replay memory, no longer by the size of the neural network. Erasing is a more final decision than reducing the replay probability, thus an even stronger emphasis of diversity may be necessary, for example by tracking the age of each transitions and using it to modulate the priority in such a way as to preserve sufficient old experience to prevent cycles.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Extensions", "weight": 1.0} -->

The priority mechanism is also flexible enough to permit integrating experience from *other sources*, such as from a planner or from human expert trajectories, since knowing the source can be used to modulate each transition's priority, e.g. in such a way as to preserve a sufficient fraction of external experience in memory.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper introduced prioritized replay, a method that can make learning from experience replay more efficient. We studied a couple of variants, devised implementations that scale to large replay memories, and found that prioritized replay speeds up learning by a factor 2 and leads to a new state-of-the-art of performance on the Atari benchmark. We laid out further variants and extensions that hold promise, namely for class-imbalanced supervised learning.
