<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sample-based Distributional Policy Gradient

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Distributional reinforcement learning (DRL) is a recent reinforcement learning framework whose success has been supported by various empirical studies. It relies on the key idea of replacing the expected return with the return distribution, which captures the intrinsic randomness of the long term rewards. Most of the existing literature on DRL focuses on problems with discrete action space and value based methods. In this work, motivated by applications in robotics with continuous action space control settings, we propose sample-based distributional policy gradient (SDPG) algorithm. It models the return distribution using samples via a reparameterization technique widely used in generative modeling and inference. We compare SDPG with the state-of-art policy gradient method in DRL, distributed distributional deterministic policy gradients (D4PG), which has demonstrated state-of-art performance. We apply SDPG and D4PG to multiple OpenAI Gym environments and observe that our algorithm shows better sample efficiency as well as higher reward for most tasks.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement learning (RL) has shown potential in solving a variety of complex problems in robotics and control. RL algorithms can be roughly divided into two categories: value function based and policy gradient methods. Value function based algorithms do not explicitly parameterize the policy, but rather obtain the policy from a learned value function. SARSA and Q-learning are popular methods for estimation of the value function based on Bellman equation. Recently, deep Q-networks (DQNs) have been utilized to approximate value function and have demonstrated to achieve human-level performance on computer games. Alternative to value function based approaches, policy gradient methods improve a parameterized policy based on the policy gradient theorem and has shown to be more effective in continuous action space control setting. In particular, deep deterministic policy gradient (DDPG) utilizes neural networks to parameterize the policy and have been successful in solving continuous control tasks.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Instead of modeling the value function as the expected sum of the discounted rewards, recently proposed distributional reinforcement learning (DRL) framework suggests to work with the full distribution of random returns, known as value or return distribution. Several typical DRL algorithms such as C51, D4PG, and QR-DQN have shown significant performance improvements over non-distributional counterparts in multiple environments including Atari games and DeepMind Control Suite. In DRL, the return distribution is usually represented by discrete categorical form or quantile function. Most of existing work within DRL framework are value function based and thus are not suitable for tasks with continuous action space. One of the exceptions is D4PG, an actor-critic type policy gradient algorithm based on DRL. It has demonstrated much better performance as compared to its non-distributional counterpart (DDPG). However, it still suffers from various drawbacks such as sample inefficiency and extra burden of parameter tuning and projection, which is largely due to the fact that the return distribution in D4PG is modeled by a discrete categorical distribution.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we advocate using samples for representing return distribution instead of categorical form or quantiles. Our algorithm which we call sample based distributional policy gradient (SDPG) learns the return distribution by directly generating the return samples via reparameterizing some simple random (e.g. Gaussian) noise samples. SDPG is an actor-critic type policy gradient based algorithm within DRL framework which employs two neural networks: an actor network to parameterize the policy and a critic network to mimic the target return distribution determined via the distributional Bellman equation based on samples. Since the return distribution is usually 1-dimensional, we leverage the quantile Huber loss as a surrogate of the Wasserstein distance for comparing return distributions and thereby learning the critic network.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

From a theoretical perspective, SDPG has the following advantages over D4PG: There is no discretization over the value distributions. The value function network is capable of generating any value distributions, which is in general not categorical as in D4PG.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

SDPG does not require the knowledge of the range of the return distribution a prior. In contrast, D4PG requires the domain knowledge in terms of bounds on the return distribution.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

No projection is required, instead, Wasserstein distance (quantile Huber loss) gives finer comparison between return distributions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Once the model is trained, the value distribution can be recovered easily to arbitrary precision by sampling. In contrast, in D4PG, the resolution of the value distribution is fixed once trained.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Empirically, we compare the performance of our algorithm with that of D4PG on multiple OpenAI Gym environments for continuous control tasks. We observe that SDPG exhibits better sample efficiency and performs better than or on-par with D4PG in term of rewards in almost all the environments.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Related Work: Most of the algorithms proposed under DRL framework are value function based methods that would run into scalability issue for problems with continuous action space. The C51 algorithm, a value based algorithm, represented the return distribution using a discrete distribution parameterized by 51 number of uniformly spaced atoms in a specified range. Later, the QR-DQN algorithm proposed to use discrete set of quantiles to represent the return distribution and demonstrated its effectiveness over C51 algorithm on the Atari 2600 games. QR-DQN was further extended in IQN to learn the full quantile function. D4PG and Reactor are existing policy gradient based methods within DRL framework; D4PG dealt with control problems in continuous action space, whereas Reactor was studied in discrete action settings. However, D4PG also utilized the discrete categorical form to represent the return distribution similar to C51 algorithm, which limits the expressive power of the value distribution network. There have been several works on utilizing samples to represent the return distributions. Generative adversarial networks (GANs), sample based generative models, have been employed in value function based approaches: GAN-DQN, value distribution GAN learning (VDGL), and GAN-DDQN.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

GAN-DQN focused on discrete action space and did not show significant improvement over traditional value based methods such as Q-Learning and DQN. Moreover, VDGL utilized GANs to learn multivariate return distributions and thereby learning the value function. Also GAN-DDQN combined GAN and IQN to learn the value function for resource allocation in communication systems. An important point to note is that apart from being value based approaches, the existing GAN based DRL methods employ two networks -- a generator and a discriminator -- for generating return samples by solving a saddle-point problem. In contrast, we utilize quantile Huber loss, as a surrogate of the Wasserstein distance, directly from samples, which results in a single objective rather than saddle-point formulation thereby eliminating the need of a discriminator for learning the return distribution.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Rest of the paper is organized as follows. In Section 2, we present related background on DRL and sample based modeling of a distribution. The SDPG algorithm is proposed in Section 3. Experimental results are presented in Section 4 followed by the conclusions in Section 5.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Distributional RL", "weight": 1.0} -->

We consider a standard RL problem with underlying model $(\mathcal{X},\mathcal{A},R,P,\gamma)$ where, as usual, $\mathcal{X},\mathcal{A}$ denote the state and action spaces respectively, $R{(x,a)}$ is the reward of taking action $a$ at state $x$, $P{(\cdot \mid x,a)}$ is the transition kernel and $0 < \gamma < 1$ is the discount factor. The reward $R$ can be random in general. This is different to the convention where $R{(x,a)}$ is the expected reward. The state and action spaces could be either discrete or continuous, though we focus on the more challenging continuous setting. The goal of RL is to find a stationary policy $\pi$ to maximize the long-term accumulated reward Since we focus on continuous-state-action tasks, we restrict the policy $\pi$ to be deterministic, that is, $a_{t} = {\pi{(x_{t})}}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Distributional RL", "weight": 1.0} -->

The Q-function, denoted by $Q^{\pi}{(x,a)}$, describes the expected reward of the agent from taking action $a \in \mathcal{A}$ from state $x \in \mathcal{X}$, that is, It satisfies Bellman's equation Here we have adopted the convention that $x'$ denotes the state succeeding $x$, i.e., $x' \sim P{(\cdot \mid x,a)}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Distributional RL", "weight": 1.0} -->

In, the authors proposed distributional reinforcement learning (DRL), which relies on a random version of Q-function, defined by namely, $Q^{\pi}$ is the statistical mean of the random variable $Z^{\pi}$. So in principle, one should be able to recover everything based on $Q^{\pi}$ using $Z^{\pi}$. Moreover, the return distribution $Z^{\pi}$ contains extra information such as variance that may be used to incorporate risk in the RL framework. The $Z$ function satisfies a modified Bellman's equation where the equation holds in the probability sense.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Distributional RL", "weight": 1.0} -->

Multiple approaches have been proposed to model the return distribution $Z^{\pi}{(x,a)}$ including distribution quantiles and discrete categorical distribution. In (D4PG), the return distribution is modeled by a categorical discretization at each $(x,a)$ pair. More specifically, $Z^{\pi}{(x,a)}$ is described a probability vector/histogram with fixed bins. The positions of the bins are chosen a prior that need to be tuned according to the environment under consideration.

<!-- chunk {"id": "body-0018", "role": "body", "section": "D4PG", "weight": 1.0} -->

The DRL was extended to the policy gradient framework. In policy gradient framework, the policy $\pi$ is modeled by a network $\pi_{\theta}$ directly. For continuous-state task, a widely used method is deterministic policy gradient (DPG), which relies on the deterministic policy gradient theorem. Let $J{(\theta)}$ be the average return with control strategy $\pi_{\theta}$, then This theorem is generalized to the DRL setting, stated as This result follows directly from the fact. The distributed distributional deterministic policy gradients (D4PG) algorithm is based on this extension of policy gradient theorem. It is an actor-critic type algorithm in which the critic learns the return distribution $Z^{\pi}$ via a neural network. Similar to, the distribution is modeled by a categorical discretization at each $(x,a)$ pair. The actor $\pi_{\theta}$ is updated via the generalized policy gradient theorem with the expectation being replaced by empirical average.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Optimal transport", "weight": 1.0} -->

Optimal (mass) transport (OT) is a powerful mathematical tool to study probability distributions. Given two random variable $X,Y$ in the Euclidean space associated with probability distribution $\mu_{X},\mu_{Y}$, the OT problem seeks the solution to with $\Pi{(\mu_{X},\mu_{Y})}$ denoting the set of feasible joint distributions of $X$ and $Y$. The unit cost function $c{(x,y)}$ is often taken to be ${\|{x - y}\|}^{p}$, $1 \leq p < \infty$, in which case, defines the Wasserstein distance $W_{p}{(\mu_{X},\mu_{Y})}$ between $\mu_{X}$ and $\mu_{Y}$. It has an equivalent form The Wasserstein distance is a metric and possesses many nice properties, including the weak continuity, which gives reasonable measure of difference between two distributions with disjoint supports.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Optimal transport", "weight": 1.0} -->

This property is extremely useful in data science as most datasets indeed lie in low-dimensional sub-manifold and therefore any small perturbation can lead to disjoint supports. One representative application relying on this property is the Wasserstein generative adversarial networks.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Optimal transport", "weight": 1.0} -->

Computing the Wasserstein distance requires solving a linear programming. Despite the recent development of algorithms in OT algorithms, computation complexity remains a bottleneck of it. One exception is the one-dimensional problem, which has closed-form solution. Let $F_{X},F_{Y}$ be the CDFs of $X,Y$ respectively, then When only samples generated by $\mu_{X},\mu_{Y}$ are available, then their Wasserstein distance can be approximated as follows. Let ${\{ x_{1},x_{2},\ldots,x_{n}\}},{\{ y_{1},y_{2},\ldots,y_{n}\}}$ be i.i.d.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Optimal transport", "weight": 1.0} -->

However as noted, Equation does not give unbiased approximation of the Wasserstein distance. In general, that is, minimizing the distance to the empirical distribution ${\hat{\mu}}_{Y}$ composed of samples from one distribution is not equivalent to minimizing the distance to that distribution $\mu_{Y}$ itself. To circumvent this difficulty, we borrow tools from quantile regression method and use quantile Huber loss as a surrogate of the Wasserstein distance. This is given by with $\tau_{i} = \frac{i}{n}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Reparameterization", "weight": 1.0} -->

Reparameterization is an effective method to model random variables, especially in case when the goal is to sample from a target distribution instead of modeling them directly using function approximations. Briefly, to model a random variable $X$ with distribution $\mu_{X}$, reparameterization trick seek a neural network to map a simple random variable $\epsilon$ (e.g. Gaussian) to the target random variable $X$, that is, $X = {G{(\epsilon)}}$. The hope is that after training, the random variable $G{(\epsilon)}$ is closed to $X$ in the probability sense. This is extremely useful for sampling purpose because one only needs to sample from simple distribution $\epsilon$ in order to generate samples of $X$. The reparameterization trick has been widely used in generative adversarial networks (GANs) where the generator is a map from simple random variable to target data set. It has also been used in variational auto-encoder to model the encoder.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Algorithm", "weight": 1.0} -->

A flow diagram of our SDPG algorithm is shown in Figure 1. We model the return distribution by samples reparameterized via a simple noise distribution (we use zero-mean Gaussian distribution with unit variance in our implementation). The critic network $G_{\phi}$, which is a neural network with parameters $\phi$, generates the return samples $z_{1},z_{2},\ldots,z_{n}$ for each state and action pair by transforming the noise samples $q_{1},q_{2},\ldots,q_{n}$. These generated samples are compared against the samples ${\overset{\sim}{z}}_{1},{\overset{\sim}{z}}_{2},\ldots,{\overset{\sim}{z}}_{n}$ generated using the distributional Bellman equation (given by) employed in the target critic network $G_{\overset{\sim}{\phi}}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Algorithm", "weight": 1.0} -->

The critic network is learned by minimizing the quantile Huber loss as defined, which is a surrogate of the Wasserstein distance between the two 1-dimensional return distributions. Therefore, the loss function for critic network is where $z_{1} \geq z_{2} \geq {\ldotsz_{n}}$ are samples after sorting. We emphasize that the sorting is important here to associate each sample with a reasonable $\hat{\tau}$. This is different to where $\hat{\tau}$ itself is the random seed over $\lbrack 0\,\, 1\rbrack$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Algorithm", "weight": 1.0} -->

The actor network $\pi_{\theta}$, parameterized by $\theta$, outputs the action $\pi_{\theta}{(x)}$ given a state $x$. The actor network receives feedback from the critic network $G_{\phi}$ in terms of the gradients of the return distribution with respect to the actions determined by the policy. This feedback is used to update the actor network by applying distributional form of the policy gradient theorem given. Therefore, the gradient of the actor network loss function is All the steps of our SDPG algorithm are described in Algorithm 1. The network parameters of actor and critic networks are updated alternatively in stochastic gradient ascent/descent fashion.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Algorithm", "weight": 1.0} -->

In contrast to the categorical parameterization of the return distribution considered in D4PG, we use samples to represent the return distribution. Since the return distribution is required to be differentiable with respect to the network parameters in order to be learned, we utilize reparameterization trick discussed in Section 2.4 to model the return distribution via random noise input. This allows us to learn a continuous distribution via samples as opposed to a discrete-valued categorical distribution in D4PG. Moreover, D4PG requires a projection step in every iteration during training in order to make the target distribution resulting from the distributional Bellman equation coincide with the support of categorical parameterized distribution being learned; SDPG eliminates the need of such a projection step during training. Furthermore, the range of the discretized grid required in D4PG must be tuned according to the reward values for each environment; SDPG does not require such tuning. Another advantage of SDPG is that one can recover the return distribution to arbitrary precision by sampling from the trained critic network.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Algorithm", "weight": 1.0} -->

However, the resolution of the return distribution is fixed in D4PG and the critic network has to be trained again from the scratch if one wants to change the resolution.\Figure 2: Illustration of each OpenAI Gym environment. From left to right: Pendulum-v0, LunarLanderContinuous-v2, BipedalWalker-v2, Reacher-v2, Swimmer-v2, Ant-v2, HalfCheetah-v2, Humanoid-v2.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

We compare the performance of proposed SDPG with D4PG algorithm on a range of challenging continuous control tasks from the OpenAI Gym environments. Figure 2 shows example screenshots of samples from different domains considered in our experiments. Note that in the original D4PG paper, the environments considered were from DeepMind Control Suite where the rewards are bounded between 0 to 1 for all the domains. In and, it was demonstrated that D4PG outperforms DDPG in almost all the environments and therefore, we compare our algorithm with the only existing policy gradient method in DRL -- D4PG. All the experiments are performed using TensorFlow with one NVIDIA TITAN Xp GPU.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

For both actor and critic networks, we use a two layer feedforward neural network with hidden layer sizes of 400 and 300, respectively, and rectified linear units (ReLU) between each hidden layer. We also used batch normalization on all the layers of both networks. Moreover, the output of the actor network is passed through a hyperbolic tangent (Tanh) activation unit.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

In all experiments we use learning rates of $\alpha = \beta = {1 \times 10^{- 4}}$, batch size $M = 256$, exploration constant $\delta = 0.3$, and $\zeta = 1$. We use a replay table of size $R = {1 \times 10^{6}}$ for all the domains except $R = {0.2 \times 10^{6}}$ for Pendulum and LunarLanderContinuous. Across all the tasks, for D4PG we use 51 atoms to represent the categorical distribution and similarly, for SDPG we use $n = 51$ number of samples to represent return distributions. Moreover, we run each task for a maximum of 1000 steps per episode. Note that SDPG is a centralized algorithm at this moment for a single agent. Thus, the distributed algorithm in D4PG is deactivated for fair comparison. One can easily establish a distributed version of SDPG. Since SDPG requires sorting operation during training, SDPG takes a little more time per episode (almost $\times 1.3$) than D4PG.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Training and Evaluation", "weight": 1.0} -->

First we demonstrate the ability of the critic network to learn the return distribution utilizing the variant of Huber loss as in Equation based on the distributional Bellman equation. Figure 3 shows the histograms of the samples generated by the learned critic network and the corresponding histograms of samples generated based on the distributional Bellman equation on BipedalWalker-v2 domain. Clearly, the histograms match almost perfectly which demonstrates that the critic network in SDPG successfully learns the target return distribution determined via the distributional Bellman equation. Note that this learned critic network can be used to generate as many samples as required (see Figure 4) to approximate the return distribution at arbitrary resolution.\Next, we study the effect of varying number of samples representing the return distribution while training. Figure 5 depicts the training curves with different samples on Ant-v2 domain. For a fixed number of samples, the algorithm is trained for five different seeds: the solid lines represent the mean returns over five trials and the shaded region represent the corresponding standard deviation. Initially, increasing the number of samples improves the performance in terms of efficiency as well as returns.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Training and Evaluation", "weight": 1.0} -->

However, when using 100 samples for training although an improvement in efficiency is observed, the returns have gone down significantly.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Training and Evaluation", "weight": 1.0} -->

For comparison, we train five different instances of each algorithm with different random seeds, with each performing one evaluation rollout every 5000 environment steps. Figure 6 shows the comparison of mean returns on different environments. It is evident form the figure that SDPG exhibits significantly better sample efficiency than D4PG on almost all the environments. Moreover in terms of average returns, SDPG performs better than D4PG on all the domains except Humanoid-v2. This maybe due to insufficient training steps. The performance of SDPG for Humanoid-v2 keeps increasing during the entire training process and this trend is expected to continue.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Training and Evaluation", "weight": 1.0} -->

We evaluate the performance of our algorithm, SDPG, based on two criteria: average returns and sample efficiency. Table 1 lists the maximal mean returns (the average of the maximal returns over different trials) along with the standard deviation. The average returns are evaluated every 5000 training steps over 100 episodes. We observe that the returns for SDPG are significantly better than D4PG for all the environments except Humanoid. To compare the sample efficiency of D4PG and SDPG, we list the number of episodes needed to reach certain return threshold in Table 2. The episode numbers reported in the table are averaged over 5 different trials and for each trial the episode number is the number of episodes required before the reward crosses a certain threshold. It is evident that SDPG requires significantly smaller number of episodes than D4PG on many environments.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, driven by applications in continuous action space, we proposed sample-based distributional policy gradient (SDPG) algorithm for learning the policy within DRL framework. This algorithm is a combination of an actor-critic type of policy gradient method and DRL. Departing from the existing state-of-art distributional policy gradient algorithm D4PG, the sampled-based reparameterization technique used in SDPG enables us to learn the return distribution to arbitrary resolution. We compared the performance of SDPG with D4PG on multiple OpenAI Gym environments. Our algorithm showed better sample efficiency than D4PG in most environments and performed better than D4PG in terms of average returns.
