<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Continuous Control with Deep Reinforcement Learning

Topics include Policy gradients, Reinforcement learning, Q-learning, Robustness, Planning, Control, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We adapt the ideas underlying the success of Deep Q-Learning to the continuous action domain. We present an actor-critic, model-free algorithm based on the deterministic policy gradient that can operate over continuous action spaces. Using the same learning algorithm, network architecture and hyper-parameters, our algorithm robustly solves more than 20 simulated physics tasks, including classic problems such as cartpole swing-up, dexterous manipulation, legged locomotion and car driving. Our algorithm is able to find policies whose performance is competitive with those found by a planning algorithm with full access to the dynamics of the domain and its derivatives. We further demonstrate that for many of the tasks the algorithm can learn policies end-to-end: directly from raw pixel inputs.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

One of the primary goals of the field of artificial intelligence is to solve complex tasks from unprocessed, high-dimensional, sensory input. Recently, significant progress has been made by combining advances in deep learning for sensory processing with reinforcement learning, resulting in the "Deep Q Network" (DQN) algorithm that is capable of human level performance on many Atari video games using unprocessed pixels for input. To do so, deep neural network function approximators were used to estimate the action-value function.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, while DQN solves problems with high-dimensional observation spaces, it can only handle discrete and low-dimensional action spaces. Many tasks of interest, most notably physical control tasks, have continuous (real valued) and high dimensional action spaces. DQN cannot be straightforwardly applied to continuous domains since it relies on a finding the action that maximizes the action-value function, which in the continuous valued case requires an iterative optimization process at every step.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

An obvious approach to adapting deep reinforcement learning methods such as DQN to continuous domains is to to simply discretize the action space. However, this has many limitations, most notably the curse of dimensionality: the number of actions increases exponentially with the number of degrees of freedom. For example, a 7 degree of freedom system (as in the human arm) with the coarsest discretization $a_{i} \in \left\{ {- k},0,k \right\}$ for each joint leads to an action space with dimensionality: $3^{7} = 2187$. The situation is even worse for tasks that require fine control of actions as they require a correspondingly finer grained discretization, leading to an explosion of the number of discrete actions. Such large action spaces are difficult to explore efficiently, and thus successfully training DQN-like networks in this context is likely intractable. Additionally, naive discretization of action spaces needlessly throws away information about the structure of the action domain, which may be essential for solving many problems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work we present a model-free, off-policy actor-critic algorithm using deep function approximators that can learn policies in high-dimensional, continuous action spaces. Our work is based on the deterministic policy gradient (DPG) algorithm (itself similar to NFQCA, and similar ideas can be found in ). However, as we show below, a naive application of this actor-critic method with neural function approximators is unstable for challenging problems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Here we combine the actor-critic approach with insights from the recent success of Deep Q Network (DQN). Prior to DQN, it was generally believed that learning value functions using large, non-linear function approximators was difficult and unstable. DQN is able to learn value functions using such function approximators in a stable and robust way due to two innovations: 1. the network is trained off-policy with samples from a replay buffer to minimize correlations between samples; 2. the network is trained with a 'target' Q network to give consistent targets during temporal difference backups. In this work we make use of the same ideas, along with batch normalization, a recent advance in deep learning.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In order to evaluate our method we constructed a variety of challenging physical control problems that involve complex multi-joint movements, unstable and rich contact dynamics, and gait behavior. Among these are classic problems such as the cartpole swing-up problem, as well as many new domains. A long-standing challenge of robotic control is to learn an action policy directly from raw sensory input such as video. Accordingly, we place a fixed viewpoint camera in the simulator and attempted all tasks using both low-dimensional observations (e.g. joint angles) and directly from pixels.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our model-free approach which we call Deep DPG (DDPG) can learn competitive policies for all of our tasks using low-dimensional observations (e.g. cartesian coordinates or joint angles) using the same hyper-parameters and network structure. In many cases, we are also able to learn good policies directly from pixels, again keeping hyperparameters and network structure constant ^11^1You can view a movie of some of the learned policies at A key feature of the approach is its simplicity: it requires only a straightforward actor-critic architecture and learning algorithm with very few "moving parts", making it easy to implement and scale to more difficult problems and larger networks. For the physical control problems we compare our results to a baseline computed by a planner that has full access to the underlying simulated dynamics and its derivatives (see supplementary information). Interestingly, DDPG can sometimes find policies that exceed the performance of the planner, in some cases even when learning from pixels (the planner always plans over the underlying low-dimensional state space).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Algorithm", "weight": 1.0} -->

It is not possible to straightforwardly apply Q-learning to continuous action spaces, because in continuous spaces finding the greedy policy requires an optimization of $a_{t}$ at every timestep; this optimization is too slow to be practical with large, unconstrained function approximators and nontrivial action spaces. Instead, here we used an actor-critic approach based on the DPG algorithm.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Algorithm", "weight": 1.0} -->

The DPG algorithm maintains a parameterized actor function $\mu{(\left. s \middle| \theta^{\mu} \right.)}$ which specifies the current policy by deterministically mapping states to a specific action. The critic $Q{(s,a)}$ is learned using the Bellman equation as in Q-learning. The actor is updated by following the applying the chain rule to the expected return from the start distribution $J$ with respect to the actor parameters: Silver et al. proved that this is the *policy gradient*, the gradient of the policy's performance ^22^2In practice, as in commonly done in policy gradient implementations, we ignored the discount in the state-visitation distribution $\rho^{\beta}$..

<!-- chunk {"id": "body-0012", "role": "body", "section": "Algorithm", "weight": 1.0} -->

As with Q learning, introducing non-linear function approximators means that convergence is no longer guaranteed. However, such approximators appear essential in order to learn and generalize on large state spaces. NFQCA, which uses the same update rules as DPG but with neural network function approximators, uses batch learning for stability, which is intractable for large networks. A minibatch version of NFQCA which does not reset the policy at each update, as would be required to scale to large networks, is equivalent to the original DPG, which we compare to here. Our contribution here is to provide modifications to DPG, inspired by the success of DQN, which allow it to use neural network function approximators to learn in large state and action spaces online. We refer to our algorithm as Deep DPG (DDPG, Algorithm 1).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Algorithm", "weight": 1.0} -->

One challenge when using neural networks for reinforcement learning is that most optimization algorithms assume that the samples are independently and identically distributed. Obviously, when the samples are generated from exploring sequentially in an environment this assumption no longer holds. Additionally, to make efficient use of hardware optimizations, it is essential to learn in minibatches, rather than online.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Algorithm", "weight": 1.0} -->

As in DQN, we used a replay buffer to address these issues. The replay buffer is a finite sized cache $\mathcal{R}$. Transitions were sampled from the environment according to the exploration policy and the tuple $(s_{t},a_{t},r_{t},s_{t + 1})$ was stored in the replay buffer. When the replay buffer was full the oldest samples were discarded. At each timestep the actor and critic are updated by sampling a minibatch uniformly from the buffer. Because DDPG is an off-policy algorithm, the replay buffer can be large, allowing the algorithm to benefit from learning across a set of uncorrelated transitions.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Directly implementing Q learning (equation 4) with neural networks proved to be unstable in many environments. Since the network $Q{(s,\left. a \middle| \theta^{Q} \right.)}$ being updated is also used in calculating the target value (equation 5), the Q update is prone to divergence. Our solution is similar to the target network used in but modified for actor-critic and using "soft" target updates, rather than directly copying the weights. We create a copy of the actor and critic networks, $Q'{(s,\left. a \middle| \theta^{Q'} \right.)}$ and $\mu'{(\left. s \middle| \theta^{\mu'} \right.)}$ respectively, that are used for calculating the target values. The weights of these target networks are then updated by having them slowly track the learned networks: $\theta'\leftarrow{{\tau\theta} + {{({1 - \tau})}\theta'}}$ with $\tau \ll 1$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Algorithm", "weight": 1.0} -->

This means that the target values are constrained to change slowly, greatly improving the stability of learning. This simple change moves the relatively unstable problem of learning the action-value function closer to the case of supervised learning, a problem for which robust solutions exist. We found that having both a target $\mu'$ and $Q'$ was required to have stable targets $y_{i}$ in order to consistently train the critic without divergence. This may slow learning, since the target network delays the propagation of value estimations. However, in practice we found this was greatly outweighed by the stability of learning.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Algorithm", "weight": 1.0} -->

When learning from low dimensional feature vector observations, the different components of the observation may have different physical units (for example, positions versus velocities) and the ranges may vary across environments. This can make it difficult for the network to learn effectively and may make it difficult to find hyper-parameters which generalise across environments with different scales of state values.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Algorithm", "weight": 1.0} -->

One approach to this problem is to manually scale the features so they are in similar ranges across environments and units. We address this issue by adapting a recent technique from deep learning called *batch normalization*. This technique normalizes each dimension across the samples in a minibatch to have unit mean and variance. In addition, it maintains a running average of the mean and variance to use for normalization during testing (in our case, during exploration or evaluation). In deep networks, it is used to minimize covariance shift during training, by ensuring that each layer receives whitened input. In the low-dimensional case, we used batch normalization on the state input and all layers of the $\mu$ network and all layers of the $Q$ network prior to the action input (details of the networks are given in the supplementary material). With batch normalization, we were able to learn effectively across many different tasks with differing types of units, without needing to manually ensure the units were within a set range.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Algorithm", "weight": 1.0} -->

A major challenge of learning in continuous action spaces is exploration. An advantage of off-policies algorithms such as DDPG is that we can treat the problem of exploration independently from the learning algorithm. We constructed an exploration policy $\mu'$ by adding noise sampled from a noise process $\mathcal{N}$ to our actor policy $\mathcal{N}$ can be chosen to suit the environment. As detailed in the supplementary materials we used an Ornstein---Uhlenbeck process to generate temporally correlated exploration for exploration efficiency in physical control problems with inertia (similar use of autocorrelated noise was introduced in).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Randomly initialize critic network Q (s, a|θQ) and actor μ (s|θμ) with weights θQ and θμ. Initialize target network Q′ and μ′ with weights θQ′ ← θQ, θμ′ ← θμ Initialize replay buffer R Initialize a random process 𝒩 for action exploration Receive initial observation state s1 Select action at = μ (st|θμ) + 𝒩t according to the current policy and exploration noise Execute action at and observe reward rt and observe new state st + 1 Sample a random minibatch of N transitions (si, ai, ri, si + 1) from R Update critic by minimizing the loss: $L = {\frac{1}{N}{\sum_{i}{({y_{i} - {Q{(s_{i},\left.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Results", "weight": 1.0} -->

We constructed simulated physical environments of varying levels of difficulty to test our algorithm. This included classic reinforcement learning environments such as cartpole, as well as difficult, high dimensional tasks such as gripper, tasks involving contacts such as puck striking (*canada*) and locomotion tasks such as *cheetah*. In all domains but *cheetah* the actions were torques applied to the actuated joints. These environments were simulated using MuJoCo. Figure 1 shows renderings of some of the environments used in the task.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Results", "weight": 1.0} -->

In all tasks, we ran experiments using both a low-dimensional state description (such as joint angles and positions) and high-dimensional renderings of the environment. As in DQN, in order to make the problems approximately fully observable in the high dimensional environment we used action repeats. For each timestep of the agent, we step the simulation 3 timesteps, repeating the agent's action and rendering each time. Thus the observation reported to the agent contains 9 feature maps (the RGB of each of the 3 renderings) which allows the agent to infer velocities using the differences between frames. The frames were downsampled to 64x64 pixels and the 8-bit RGB values were converted to floating point scaled to $\lbrack 0,1\rbrack$. See supplementary information for details of our network structure and hyperparameters.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Results", "weight": 1.0} -->

We evaluated the policy periodically during training by testing it without exploration noise. Figure 2 shows the performance curve for a selection of environments. We also report results with components of our algorithm (i.e. the target network or batch normalization) removed. In order to perform well across all tasks, both of these additions are necessary. In particular, learning without a target network, as in the original work with DPG, is very poor in many environments.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Results", "weight": 1.0} -->

Surprisingly, in some simpler tasks, learning policies from pixels is just as fast as learning using the low-dimensional state descriptor. This may be due to the action repeats making the problem simpler. It may also be that the convolutional layers provide an easily separable representation of state space, which is straightforward for the higher layers to learn on quickly.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Results", "weight": 1.0} -->

Table 1 summarizes DDPG's performance across all of the environments (results are averaged over 5 replicas). We normalized the scores using two baselines. The first baseline is the mean return from a naive policy which samples actions from a uniform distribution over the valid action space. The second baseline is iLQG, a planning based solver with full access to the underlying physical model and its derivatives. We normalize scores so that the naive policy has a mean score of $0$ and iLQG has a mean score of $1$. DDPG is able to learn good policies on many of the tasks, and in many cases some of the replicas learn policies which are superior to those found by iLQG, even when learning directly from pixels.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Results", "weight": 1.0} -->

It can be challenging to learn accurate value estimates. Q-learning, for example, is prone to over-estimating values. We examined DDPG's estimates empirically by comparing the values estimated by $Q$ after training with the true returns seen on test episodes. Figure 3 shows that in simple tasks DDPG estimates returns accurately without systematic biases. For harder tasks the Q estimates are worse, but DDPG is still able learn good policies.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Results", "weight": 1.0} -->

To demonstrate the generality of our approach we also include Torcs, a racing game where the actions are acceleration, braking and steering. Torcs has previously been used as a testbed in other policy learning approaches. We used an identical network architecture and learning algorithm hyper-parameters to the physics tasks but altered the noise process for exploration because of the very different time scales involved. On both low-dimensional and from pixels, some replicas were able to learn reasonable policies that are able to complete a circuit around the track though other replicas failed to learn a sensible policy.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The work combines insights from recent advances in deep learning and reinforcement learning, resulting in an algorithm that robustly solves challenging problems across a variety of domains with continuous action spaces, even when using raw pixels for observations. As with most reinforcement learning algorithms, the use of non-linear function approximators nullifies any convergence guarantees; however, our experimental results demonstrate that stable learning without the need for any modifications between environments.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Interestingly, all of our experiments used substantially fewer steps of experience than was used by DQN learning to find solutions in the Atari domain. Nearly all of the problems we looked at were solved within 2.5 million steps of experience (and usually far fewer), a factor of 20 fewer steps than DQN requires for good Atari solutions. This suggests that, given more simulation time, DDPG may solve even more difficult problems than those considered here.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Conclusion", "weight": 1.5} -->

A few limitations to our approach remain. Most notably, as with most model-free reinforcement approaches, DDPG requires a large number of training episodes to find solutions. However, we believe that a robust model-free approach may be an important component of larger systems which may attack these limitations.
