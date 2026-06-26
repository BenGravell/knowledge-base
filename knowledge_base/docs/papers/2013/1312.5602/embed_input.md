<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Playing Atari with Deep Reinforcement Learning

Topics include Deep reinforcement learning, Q-learning, Atari, Convolutional networks, Experience replay, Pixel control, Value functions, Arcade learning environment.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents the first DQN result: a convolutional neural network trained by Q-learning directly from Atari pixels with a single architecture reused across games. Its importance is showing that deep networks can learn control policies from high-dimensional observations without hand-engineered state, outperforming prior methods on most tested games and setting the template for later deep RL systems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present the first deep learning model to successfully learn control policies directly from high-dimensional sensory input using reinforcement learning. The model is a convolutional neural network, trained with a variant of Q-learning, whose input is raw pixels and whose output is a value function estimating future rewards. We apply our method to seven Atari 2600 games from the Arcade Learning Environment, with no adjustment of the architecture or learning algorithm. We find that it outperforms all previous approaches on six of the games and surpasses a human expert on three of them.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Learning to control agents directly from high-dimensional sensory inputs like vision and speech is one of the long-standing challenges of reinforcement learning (RL). Most successful RL applications that operate on these domains have relied on hand-crafted features combined with linear value functions or policy representations. Clearly, the performance of such systems heavily relies on the quality of the feature representation.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent advances in deep learning have made it possible to extract high-level features from raw sensory data, leading to breakthroughs in computer vision and speech recognition. These methods utilise a range of neural network architectures, including convolutional networks, multilayer perceptrons, restricted Boltzmann machines and recurrent neural networks, and have exploited both supervised and unsupervised learning. It seems natural to ask whether similar techniques could also be beneficial for RL with sensory data.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

However reinforcement learning presents several challenges from a deep learning perspective. Firstly, most successful deep learning applications to date have required large amounts of hand-labelled training data. RL algorithms, on the other hand, must be able to learn from a scalar reward signal that is frequently sparse, noisy and delayed. The delay between actions and resulting rewards, which can be thousands of timesteps long, seems particularly daunting when compared to the direct association between inputs and targets found in supervised learning. Another issue is that most deep learning algorithms assume the data samples to be independent, while in reinforcement learning one typically encounters sequences of highly correlated states. Furthermore, in RL the data distribution changes as the algorithm learns new behaviours, which can be problematic for deep learning methods that assume a fixed underlying distribution.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper demonstrates that a convolutional neural network can overcome these challenges to learn successful control policies from raw video data in complex RL environments. The network is trained with a variant of the Q-learning algorithm, with stochastic gradient descent to update the weights. To alleviate the problems of correlated data and non-stationary distributions, we use an experience replay mechanism which randomly samples previous transitions, and thereby smooths the training distribution over many past behaviors.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We apply our approach to a range of Atari 2600 games implemented in The Arcade Learning Environment (ALE). Atari 2600 is a challenging RL testbed that presents agents with a high dimensional visual input ($210 \times 160$ RGB video at 60Hz) and a diverse and interesting set of tasks that were designed to be difficult for humans players. Our goal is to create a single neural network agent that is able to successfully learn to play as many of the games as possible. The network was not provided with any game-specific information or hand-designed visual features, and was not privy to the internal state of the emulator; it learned from nothing but the video input, the reward and terminal signals, and the set of possible actions---just as a human player would. Furthermore the network architecture and all hyperparameters used for training were kept constant across the games. So far the network has outperformed all previous RL algorithms on six of the seven games we have attempted and surpassed an expert human player on three of them. Figure 1 provides sample screenshots from five of the games used for training.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Deep Reinforcement Learning", "weight": 1.0} -->

Recent breakthroughs in computer vision and speech recognition have relied on efficiently training deep neural networks on very large training sets. The most successful approaches are trained directly from the raw inputs, using lightweight updates based on stochastic gradient descent. By feeding sufficient data into deep neural networks, it is often possible to learn better representations than handcrafted features. These successes motivate our approach to reinforcement learning. Our goal is to connect a reinforcement learning algorithm to a deep neural network which operates directly on RGB images and efficiently process training data by using stochastic gradient updates.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Deep Reinforcement Learning", "weight": 1.0} -->

Tesauro's TD-Gammon architecture provides a starting point for such an approach. This architecture updates the parameters of a network that estimates the value function, directly from on-policy samples of experience, $s_{t},a_{t},r_{t},s_{t + 1},a_{t + 1}$, drawn from the algorithm's interactions with the environment (or by self-play, in the case of backgammon). Since this approach was able to outperform the best human backgammon players 20 years ago, it is natural to wonder whether two decades of hardware improvements, coupled with modern deep neural network architectures and scalable RL algorithms might produce significant progress.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Deep Reinforcement Learning", "weight": 1.0} -->

In contrast to TD-Gammon and similar online approaches, we utilize a technique known as *experience replay* where we store the agent's experiences at each time-step, $e_{t} = {(s_{t},a_{t},r_{t},s_{t + 1})}$ in a data-set $\mathcal{D} = {e_{1},\ldots,e_{N}}$, pooled over many episodes into a *replay memory*. During the inner loop of the algorithm, we apply Q-learning updates, or minibatch updates, to samples of experience, $e \sim \mathcal{D}$, drawn at random from the pool of stored samples. After performing experience replay, the agent selects and executes an action according to an $\epsilon$-greedy policy. Since using histories of arbitrary length as inputs to a neural network can be difficult, our Q-function instead works on fixed length representation of histories produced by a function $\phi$. The full algorithm, which we call *deep Q-learning*, is presented in Algorithm 1.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Deep Reinforcement Learning", "weight": 1.0} -->

This approach has several advantages over standard online Q-learning. First, each step of experience is potentially used in many weight updates, which allows for greater data efficiency. Second, learning directly from consecutive samples is inefficient, due to the strong correlations between the samples; randomizing the samples breaks these correlations and therefore reduces the variance of the updates. Third, when learning on-policy the current parameters determine the next data sample that the parameters are trained. For example, if the maximizing action is to move left then the training samples will be dominated by samples from the left-hand side; if the maximizing action then switches to the right then the training distribution will also switch. It is easy to see how unwanted feedback loops may arise and the parameters could get stuck in a poor local minimum, or even diverge catastrophically. By using experience replay the behavior distribution is averaged over many of its previous states, smoothing out learning and avoiding oscillations or divergence in the parameters. Note that when learning by experience replay, it is necessary to learn off-policy (because our current parameters are different to those used to generate the sample), which motivates the choice of Q-learning.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Deep Reinforcement Learning", "weight": 1.0} -->

In practice, our algorithm only stores the last $N$ experience tuples in the replay memory, and samples uniformly at random from $\mathcal{D}$ when performing updates. This approach is in some respects limited since the memory buffer does not differentiate important transitions and always overwrites with recent transitions due to the finite memory size $N$. Similarly, the uniform sampling gives equal importance to all transitions in the replay memory. A more sophisticated sampling strategy might emphasize transitions from which we can learn the most, similar to prioritized sweeping.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Deep Reinforcement Learning", "weight": 1.0} -->

Initialize replay memory 𝒟 to capacity N Initialize action-value function Q with random weights Initialise sequence s1 = {x1} and preprocessed sequenced ϕ1 = ϕ (s1) With probability ϵ select a random action at otherwise select at = maxaQ* (ϕ (st), a; θ) Execute action at in emulator and observe reward rt and image xt + 1 Set st + 1 = st xt + 1 and preprocess ϕt + 1 = ϕ (st + 1) Sample random minibatch of transitions (ϕj, aj, rj, ϕj + 1) from 𝒟 Set $y_{j} = \left\{ \begin{array}{ll} r_{j} & {\text{for terminal~}\phi_{j + 1}} \\{r_{j} + {\gamma{\max_{a'}Q}{(\phi_{j + 1},a';\theta)}}} & {\text{for non-terminal~}\phi_{j + 1}} \end{array} \right.$ Perform a gradient descent step on (yj − Q

<!-- chunk {"id": "body-0015", "role": "body", "section": "Deep Reinforcement Learning", "weight": 1.0} -->

(ϕj, aj; θ))2 according to equation 3 Algorithm 1 Deep Q-learning with Experience Replay

<!-- chunk {"id": "body-0016", "role": "body", "section": "Preprocessing and Model Architecture", "weight": 1.0} -->

Working directly with raw Atari frames, which are $210 \times 160$ pixel images with a 128 color palette, can be computationally demanding, so we apply a basic preprocessing step aimed at reducing the input dimensionality. The raw frames are preprocessed by first converting their RGB representation to gray-scale and down-sampling it to a $110 \times 84$ image. The final input representation is obtained by cropping an $84 \times 84$ region of the image that roughly captures the playing area. The final cropping stage is only required because we use the GPU implementation of 2D convolutions, which expects square inputs. For the experiments in this paper, the function $\phi$ from algorithm 1 applies this preprocessing to the last $4$ frames of a history and stacks them to produce the input to the $Q$-function.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Preprocessing and Model Architecture", "weight": 1.0} -->

There are several possible ways of parameterizing $Q$ using a neural network. Since $Q$ maps history-action pairs to scalar estimates of their Q-value, the history and the action have been used as inputs to the neural network by some previous approaches. The main drawback of this type of architecture is that a separate forward pass is required to compute the Q-value of each action, resulting in a cost that scales linearly with the number of actions. We instead use an architecture in which there is a separate output unit for each possible action, and only the state representation is an input to the neural network. The outputs correspond to the predicted Q-values of the individual action for the input state. The main advantage of this type of architecture is the ability to compute Q-values for all possible actions in a given state with only a single forward pass through the network.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Preprocessing and Model Architecture", "weight": 1.0} -->

We now describe the exact architecture used for all seven Atari games. The input to the neural network consists is an $84 \times 84 \times 4$ image produced by $\phi$. The first hidden layer convolves $16$ $8 \times 8$ filters with stride $4$ with the input image and applies a rectifier nonlinearity. The second hidden layer convolves $32$ $4 \times 4$ filters with stride $2$, again followed by a rectifier nonlinearity. The final hidden layer is fully-connected and consists of $256$ rectifier units. The output layer is a fully-connected linear layer with a single output for each valid action. The number of valid actions varied between $4$ and $18$ on the games we considered. We refer to convolutional networks trained with our approach as Deep Q-Networks (DQN).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Experiments", "weight": 1.0} -->

So far, we have performed experiments on seven popular ATARI games -- Beam Rider, Breakout, Enduro, Pong, Q\*bert, Seaquest, Space Invaders. We use the same network architecture, learning algorithm and hyperparameters settings across all seven games, showing that our approach is robust enough to work on a variety of games without incorporating game-specific information. While we evaluated our agents on the real and unmodified games, we made one change to the reward structure of the games during training only. Since the scale of scores varies greatly from game to game, we fixed all positive rewards to be $1$ and all negative rewards to be $- 1$, leaving $0$ rewards unchanged. Clipping the rewards in this manner limits the scale of the error derivatives and makes it easier to use the same learning rate across multiple games. At the same time, it could affect the performance of our agent since it cannot differentiate between rewards of different magnitude.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Experiments", "weight": 1.0} -->

In these experiments, we used the RMSProp algorithm with minibatches of size 32. The behavior policy during training was $\epsilon$-greedy with $\epsilon$ annealed linearly from $1$ to $0.1$ over the first million frames, and fixed at $0.1$ thereafter. We trained for a total of $10$ million frames and used a replay memory of one million most recent frames.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Experiments", "weight": 1.0} -->

Following previous approaches to playing Atari games, we also use a simple frame-skipping technique. More precisely, the agent sees and selects actions on every $k^{th}$ frame instead of every frame, and its last action is repeated on skipped frames. Since running the emulator forward for one step requires much less computation than having the agent select an action, this technique allows the agent to play roughly $k$ times more games without significantly increasing the runtime. We use $k = 4$ for all games except Space Invaders where we noticed that using $k = 4$ makes the lasers invisible because of the period at which they blink. We used $k = 3$ to make the lasers visible and this change was the only difference in hyperparameter values between any of the games.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Training and Stability", "weight": 1.0} -->

In supervised learning, one can easily track the performance of a model during training by evaluating it on the training and validation sets. In reinforcement learning, however, accurately evaluating the progress of an agent during training can be challenging. Since our evaluation metric, as suggested, is the total reward the agent collects in an episode or game averaged over a number of games, we periodically compute it during training. The average total reward metric tends to be very noisy because small changes to the weights of a policy can lead to large changes in the distribution of states the policy visits. The leftmost two plots in figure 2 show how the average total reward evolves during training on the games Seaquest and Breakout. Both averaged reward plots are indeed quite noisy, giving one the impression that the learning algorithm is not making steady progress. Another, more stable, metric is the policy's estimated action-value function $Q$, which provides an estimate of how much discounted reward the agent can obtain by following its policy from any given state. We collect a fixed set of states by running a random policy before training starts and track the average of the maximum^22^2The maximum for each state is taken over the possible actions. predicted $Q$ for these states.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Training and Stability", "weight": 1.0} -->

The two rightmost plots in figure 2 show that average predicted $Q$ increases much more smoothly than the average total reward obtained by the agent and plotting the same metrics on the other five games produces similarly smooth curves. In addition to seeing relatively smooth improvement to predicted $Q$ during training we did not experience any divergence issues in any of our experiments. This suggests that, despite lacking any theoretical convergence guarantees, our method is able to train large neural networks using a reinforcement learning signal and stochastic gradient descent in a stable manner.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Main Evaluation", "weight": 1.0} -->

We compare our results with the best performing methods from the RL literature. The method labeled Sarsa used the Sarsa algorithm to learn linear policies on several different feature sets hand-engineered for the Atari task and we report the score for the best performing feature set. Contingency used the same basic approach as Sarsa but augmented the feature sets with a learned representation of the parts of the screen that are under the agent's control. Note that both of these methods incorporate significant prior knowledge about the visual problem by using background subtraction and treating each of the 128 colors as a separate channel. Since many of the Atari games use one distinct color for each type of object, treating each color as a separate channel can be similar to producing a separate binary map encoding the presence of each object type. In contrast, our agents only receive the raw RGB screenshots as input and must *learn* to detect objects on their own.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Main Evaluation", "weight": 1.0} -->

In addition to the learned agents, we also report scores for an expert human game player and a policy that selects actions uniformly at random. The human performance is the median reward achieved after around two hours of playing each game. Note that our reported human scores are much higher than the ones in Bellemare et al.. For the learned methods, we follow the evaluation strategy used in Bellemare et al. and report the average score obtained by running an $\epsilon$-greedy policy with $\epsilon = 0.05$ for a fixed number of steps. The first five rows of table 1 show the per-game average scores on all games. Our approach (labeled DQN) outperforms the other learning methods by a substantial margin on all seven games despite incorporating almost no prior knowledge about the inputs.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Main Evaluation", "weight": 1.0} -->

We also include a comparison to the evolutionary policy search approach from in the last three rows of table 1. We report two sets of results for this method. The HNeat Best score reflects the results obtained by using a hand-engineered object detector algorithm that outputs the locations and types of objects on the Atari screen. The HNeat Pixel score is obtained by using the special 8 color channel representation of the Atari emulator that represents an object label map at each channel. This method relies heavily on finding a deterministic sequence of states that represents a successful exploit. It is unlikely that strategies learnt in this way will generalize to random perturbations; therefore the algorithm was only evaluated on the highest scoring single episode. In contrast, our algorithm is evaluated on $\epsilon$-greedy control sequences, and must therefore generalize across a wide variety of possible situations. Nevertheless, we show that on all the games, except Space Invaders, not only our max evaluation results (row $8$), but also our average results (row $4$) achieve better performance.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Main Evaluation", "weight": 1.0} -->

Finally, we show that our method achieves better performance than an expert human player on Breakout, Enduro and Pong and it achieves close to human performance on Beam Rider. The games Q\*bert, Seaquest, Space Invaders, on which we are far from human performance, are more challenging because they require the network to find a strategy that extends over long time scales.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper introduced a new deep learning model for reinforcement learning, and demonstrated its ability to master difficult control policies for Atari 2600 computer games, using only raw pixels as input. We also presented a variant of online Q-learning that combines stochastic minibatch updates with experience replay memory to ease the training of deep networks for RL. Our approach gave state-of-the-art results in six of the seven games it was tested, with no adjustment of the architecture or hyperparameters.
