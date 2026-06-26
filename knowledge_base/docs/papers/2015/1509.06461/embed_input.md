<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Deep Reinforcement Learning with Double Q-learning

Topics include Reinforcement learning, Q-learning, Neural networks, Learning, Function approximation.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The popular Q-learning algorithm is known to overestimate action values under certain conditions. It was not previously known whether, in practice, such overestimations are common, whether they harm performance, and whether they can generally be prevented. In this paper, we answer all these questions affirmatively. In particular, we first show that the recent DQN algorithm, which combines Q-learning with a deep neural network, suffers from substantial overestimations in some games in the Atari 2600 domain. We then show that the idea behind the Double Q-learning algorithm, which was introduced in a tabular setting, can be generalized to work with large-scale function approximation. We propose a specific adaptation to the DQN algorithm and show that the resulting algorithm not only reduces the observed overestimations, as hypothesized, but that this also leads to much better performance on several games.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Abstract", "weight": 1.5} -->

The popular Q-learning algorithm is known to overestimate action values under certain conditions. It was not previously known whether, in practice, such overestimations are common, whether they harm performance, and whether they can generally be prevented. In this paper, we answer all these questions affirmatively. In particular, we first show that the recent DQN algorithm, which combines Q-learning with a deep neural network, suffers from substantial overestimations in some games in the Atari 2600 domain. We then show that the idea behind the Double Q-learning algorithm, which was introduced in a tabular setting, can be generalized to work with large-scale function approximation. We propose a specific adaptation to the DQN algorithm and show that the resulting algorithm not only reduces the observed overestimations, as hypothesized, but that this also leads to much better performance on several games.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Abstract", "weight": 1.5} -->

The goal of reinforcement learning is to learn good policies for sequential decision problems, by optimizing a cumulative future reward signal. Q-learning is one of the most popular reinforcement learning algorithms, but it is known to sometimes learn unrealistically high action values because it includes a maximization step over estimated action values, which tends to prefer overestimated to underestimated values.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Abstract", "weight": 1.5} -->

In previous work, overestimations have been attributed to insufficiently flexible function approximation and noise. In this paper, we unify these views and show overestimations can occur when the action values are inaccurate, irrespective of the source of approximation error. Of course, imprecise value estimates are the norm during learning, which indicates that overestimations may be much more common than previously appreciated.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Abstract", "weight": 1.5} -->

It is an open question whether, if the overestimations do occur, this negatively affects performance in practice. Overoptimistic value estimates are not necessarily a problem in and of themselves. If all values would be uniformly higher then the relative action preferences are preserved and we would not expect the resulting policy to be any worse. Furthermore, it is known that sometimes it is good to be optimistic: optimism in the face of uncertainty is a well-known exploration technique. If, however, the overestimations are not uniform and not concentrated at states about which we wish to learn more, then they might negatively affect the quality of the resulting policy. Thrun and Schwartz give specific examples in which this leads to suboptimal policies, even asymptotically.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Abstract", "weight": 1.5} -->

To test whether overestimations occur in practice and at scale, we investigate the performance of the recent DQN algorithm. DQN combines Q-learning with a flexible deep neural network and was tested on a varied and large set of deterministic Atari 2600 games, reaching human-level performance on many games. In some ways, this setting is a best-case scenario for Q-learning, because the deep neural network provides flexible function approximation with the potential for a low asymptotic approximation error, and the determinism of the environments prevents the harmful effects of noise. Perhaps surprisingly, we show that even in this comparatively favorable setting DQN sometimes substantially overestimates the values of the actions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Abstract", "weight": 1.5} -->

We show that the idea behind the Double Q-learning algorithm, which was first proposed in a tabular setting, can be generalized to work with arbitrary function approximation, including deep neural networks. We use this to construct a new algorithm we call Double DQN. We then show that this algorithm not only yields more accurate value estimates, but leads to much higher scores on several games. This demonstrates that the overestimations of DQN were indeed leading to poorer policies and that it is beneficial to reduce them. In addition, by improving upon DQN we obtain state-of-the-art results on the Atari domain.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Deep Q Networks", "weight": 1.0} -->

A deep Q network (DQN) is a multi-layered neural network that for a given state $s$ outputs a vector of action values $Q{(s, \cdot;{\mathbf{θ}})}$, where $\mathbf{θ}$ are the parameters of the network. For an $n$-dimensional state space and an action space containing $m$ actions, the neural network is a function from ${\mathbb{R}}^{n}$ to ${\mathbb{R}}^{m}$. Two important ingredients of the DQN algorithm as proposed by Mnih et al. are the use of a target network, and the use of experience replay. The target network, with parameters ${\mathbf{θ}}^{-}$, is the same as the online network except that its parameters are copied every $\tau$ steps from the online network, so that then ${\mathbf{θ}}_{t}^{-} = {\mathbf{θ}}_{t}$, and kept fixed on all other steps.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Deep Q Networks", "weight": 1.0} -->

The target used by DQN is then For the experience replay, observed transitions are stored for some time and sampled uniformly from this memory bank to update the network. Both the target network and the experience replay dramatically improve the performance of the algorithm.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Double Q-learning", "weight": 1.0} -->

The max operator in standard Q-learning and DQN, in and, uses the same values both to select and to evaluate an action. This makes it more likely to select overestimated values, resulting in overoptimistic value estimates. To prevent this, we can decouple the selection from the evaluation. This is the idea behind Double Q-learning.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Double Q-learning", "weight": 1.0} -->

In the original Double Q-learning algorithm, two value functions are learned by assigning each experience randomly to update one of the two value functions, such that there are two sets of weights, $\mathbf{θ}$ and ${\mathbf{θ}}'$. For each update, one set of weights is used to determine the greedy policy and the other to determine its value. For a clear comparison, we can first untangle the selection and evaluation in Q-learning and rewrite its target as The Double Q-learning error can then be written as Notice that the selection of the action, in the $\arg\max$, is still due to the online weights ${\mathbf{θ}}_{t}$. This means that, as in Q-learning, we are still estimating the value of the greedy policy according to the current values, as defined by ${\mathbf{θ}}_{t}$. However, we use the second set of weights ${\mathbf{θ}}_{t}'$ to fairly evaluate the value of this policy.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Double Q-learning", "weight": 1.0} -->

This second set of weights can be updated symmetrically by switching the roles of $\mathbf{θ}$ and ${\mathbf{θ}}'$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Overoptimism due to estimation errors", "weight": 1.0} -->

Q-learning's overestimations were first investigated by Thrun and Schwartz, who showed that if the action values contain random errors uniformly distributed in an interval $\lbrack{- \epsilon},\epsilon\rbrack$ then each target is overestimated up to $\gamma\epsilon\frac{m - 1}{m + 1}$, where $m$ is the number of actions. In addition, Thrun and Schwartz give a concrete example in which these overestimations even asymptotically lead to sub-optimal policies, and show the overestimations manifest themselves in a small toy problem when using function approximation. Later van Hasselt argued that noise in the environment can lead to overestimations even when using tabular representation, and proposed Double Q-learning as a solution.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Overoptimism due to estimation errors", "weight": 1.0} -->

In this section we demonstrate more generally that estimation errors of any kind can induce an upward bias, regardless of whether these errors are due to environmental noise, function approximation, non-stationarity, or any other source. This is important, because in practice any method will incur some inaccuracies during learning, simply due to the fact that the true values are initially unknown.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Overoptimism due to estimation errors", "weight": 1.0} -->

The result by Thrun and Schwartz cited above gives an upper bound to the overestimation for a specific setup, but it is also possible, and potentially more interesting, to derive a lower bound.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Double DQN", "weight": 1.0} -->

The idea of Double Q-learning is to reduce overestimations by decomposing the max operation in the target into action selection and action evaluation. Although not fully decoupled, the target network in the DQN architecture provides a natural candidate for the second value function, without having to introduce additional networks. We therefore propose to evaluate the greedy policy according to the online network, but using the target network to estimate its value. In reference to both Double Q-learning and DQN, we refer to the resulting algorithm as Double DQN. Its update is the same as for DQN, but replacing the target $Y_{t}^{\text{DQN}}$ with In comparison to Double Q-learning, the weights of the second network ${\mathbf{θ}}_{t}'$ are replaced with the weights of the target network ${\mathbf{θ}}_{t}^{-}$ for the evaluation of the current greedy policy. The update to the target network stays unchanged from DQN, and remains a periodic copy of the online network.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Double DQN", "weight": 1.0} -->

This version of Double DQN is perhaps the minimal possible change to DQN towards Double Q-learning. The goal is to get most of the benefit of Double Q-learning, while keeping the rest of the DQN algorithm intact for a fair comparison, and with minimal computational overhead.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Empirical results", "weight": 1.0} -->

In this section, we analyze the overestimations of DQN and show that Double DQN improves over DQN both in terms of value accuracy and in terms of policy quality. To further test the robustness of the approach we additionally evaluate the algorithms with random starts generated from expert human trajectories, as proposed by Nair et al..

<!-- chunk {"id": "body-0020", "role": "body", "section": "Empirical results", "weight": 1.0} -->

Our testbed consists of Atari 2600 games, using the Arcade Learning Environment. The goal is for a single algorithm, with a fixed set of hyperparameters, to learn to play each of the games separately from interaction given only the screen pixels as input. This is a demanding testbed: not only are the inputs high-dimensional, the game visuals and game mechanics vary substantially between games. Good solutions must therefore rely heavily on the learning algorithm --- it is not practically feasible to overfit the domain by relying only on tuning.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Empirical results", "weight": 1.0} -->

We closely follow the experimental setting and network architecture outlined by Mnih et al.. Briefly, the network architecture is a convolutional neural network with 3 convolution layers and a fully-connected hidden layer (approximately 1.5M parameters in total). The network takes the last four frames as input and outputs the action value of each action. On each game, the network is trained on a single GPU for 200M frames, or approximately 1 week.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Results on overoptimism", "weight": 1.0} -->

More extreme overestimations are shown in the middle two plots, where DQN is highly unstable on the games Asterix and Wizard of Wor. Notice the log scale for the values on the $y$-axis. The bottom two plots shows the corresponding scores for these two games. Notice that the increases in value estimates for DQN in the middle plots coincide with decreasing scores in bottom plots. Again, this indicates that the overestimations are harming the quality of the resulting policies. If seen in isolation, one might perhaps be tempted to think the observed instability is related to inherent instability problems of off-policy learning with function approximation. However, we see that learning is much more stable with Double DQN, suggesting that the cause for these instabilities is in fact Q-learning's overoptimism. Figure 3 only shows a few examples, but overestimations were observed for DQN in all 49 tested Atari games, albeit in varying amounts.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Quality of the learned policies", "weight": 1.0} -->

Overoptimism does not always adversely affect the quality of the learned policy. For example, DQN achieves optimal behavior in Pong despite slightly overestimating the policy value. Nevertheless, reducing overestimations can significantly benefit the stability of learning; we see clear examples of this in Figure 3. We now assess more generally how much Double DQN helps in terms of policy quality by evaluating on all 49 games that DQN was tested.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Quality of the learned policies", "weight": 1.0} -->

As described by Mnih et al. each evaluation episode starts by executing a special no-op action that does not affect the environment up to 30 times, to provide different starting points for the agent. Some exploration during evaluation provides additional randomization. For Double DQN we used the exact same hyper-parameters as for DQN, to allow for a controlled experiment focused just on reducing overestimations. The learned policies are evaluated for 5 mins of emulator time (18,000 frames) with an $\epsilon$-greedy policy where $\epsilon = 0.05$. The scores are averaged over 100 episodes. The only difference between Double DQN and DQN is the target, using $Y_{t}^{\text{DoubleDQN}}$ rather than $Y^{\text{DQN}}$. This evaluation is somewhat adversarial, as the used hyper-parameters were tuned for DQN but not for Double DQN.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Quality of the learned policies", "weight": 1.0} -->

To obtain summary statistics across games, we normalize the score for each game as follows: The 'random' and 'human' scores are the same as used by Mnih et al., and are given in the appendix.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Quality of the learned policies", "weight": 1.0} -->

Table 1, under no ops, shows that on the whole Double DQN clearly improves over DQN. A detailed comparison (in appendix) shows that there are several games in which Double DQN greatly improves upon DQN. Noteworthy examples include Road Runner (from 233% to 617%), Asterix (from 70% to 180%), Zaxxon (from 54% to 111%), and Double Dunk (from 17% to 397%).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Quality of the learned policies", "weight": 1.0} -->

The Gorila algorithm, which is a massively distributed version of DQN, is not included in the table because the architecture and infrastructure is sufficiently different to make a direct comparison unclear. For completeness, we note that Gorila obtained median and mean normalized scores of 96% and 495%, respectively.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Robustness to Human starts", "weight": 1.0} -->

Double DQN (tuned) Table 2: Summary of normalized performance up to 30 minutes of play on 49 games with human starts. Results for DQN are from Nair et al..

<!-- chunk {"id": "body-0029", "role": "body", "section": "Robustness to Human starts", "weight": 1.0} -->

One concern with the previous evaluation is that in deterministic games with a unique starting point the learner could potentially learn to remember sequences of actions without much need to generalize. While successful, the solution would not be particularly robust. By testing the agents from various starting points, we can test whether the found solutions generalize well, and as such provide a challenging testbed for the learned polices.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Robustness to Human starts", "weight": 1.0} -->

We obtained 100 starting points sampled for each game from a human expert's trajectory, as proposed by Nair et al.. We start an evaluation episode from each of these starting points and run the emulator for up to 108,000 frames (30 mins at 60Hz including the trajectory before the starting point). Each agent is only evaluated on the rewards accumulated after the starting point.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Robustness to Human starts", "weight": 1.0} -->

For this evaluation we include a tuned version of Double DQN. Some tuning is appropriate because the hyperparameters were tuned for DQN, which is a different algorithm. For the tuned version of Double DQN, we increased the number of frames between each two copies of the target network from 10,000 to 30,000, to reduce overestimations further because immediately after each switch DQN and Double DQN both revert to Q-learning. In addition, we reduced the exploration during learning from $\epsilon = 0.1$ to $\epsilon = 0.01$, and then used $\epsilon = 0.001$ during evaluation. Finally, the tuned version uses a single shared bias for all action values in the top layer of the network. Each of these changes improved performance and together they result in clearly better results.^33^3Except for Tennis, where the lower $\epsilon$ during training seemed to hurt rather than help.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Robustness to Human starts", "weight": 1.0} -->

Table 2 reports summary statistics for this evaluation on the 49 games from Mnih et al.. Double DQN obtains clearly higher median and mean scores. Again Gorila DQN is not included in the table, but for completeness note it obtained a median of 78% and a mean of 259%. Detailed results, plus results for an additional 8 games, are available in Figure 4 and in the appendix. On several games the improvements from DQN to Double DQN are striking, in some cases bringing scores much closer to human, or even surpassing these.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Robustness to Human starts", "weight": 1.0} -->

Double DQN appears more robust to this more challenging evaluation, suggesting that appropriate generalizations occur and that the found solutions do not exploit the determinism of the environments. This is appealing, as it indicates progress towards finding general solutions rather than a deterministic sequence of steps that would be less robust.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Discussion", "weight": 1.5} -->

This paper has five contributions. First, we have shown why Q-learning can be overoptimistic in large-scale problems, even if these are deterministic, due to the inherent estimation errors of learning. Second, by analyzing the value estimates on Atari games we have shown that these overestimations are more common and severe in practice than previously acknowledged. Third, we have shown that Double Q-learning can be used at scale to successfully reduce this overoptimism, resulting in more stable and reliable learning. Fourth, we have proposed a specific implementation called Double DQN, that uses the existing architecture and deep neural network of the DQN algorithm without requiring additional networks or parameters. Finally, we have shown that Double DQN finds better policies, obtaining new state-of-the-art results on the Atari 2600 domain.
