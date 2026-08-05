<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Improving Robustness via Risk Averse Distributional Reinforcement Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

One major obstacle that precludes the success of reinforcement learning in real-world applications is the lack of robustness, either to model uncertainties or external disturbances, of the trained policies. Robustness is critical when the policies are trained in simulations instead of real world environment. In this work, we propose a risk-aware algorithm to learn robust policies in order to bridge the gap between simulation training and real-world implementation. Our algorithm is based on recently discovered distributional RL framework. We incorporate CVaR risk measure in sample based distributional policy gradients (SDPG) for learning risk-averse policies to achieve robustness against a range of system disturbances. We validate the robustness of risk-aware SDPG on multiple environments.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement learning (RL) has been successful in achieving human level or even better performance in multiple games such as Atari and Go. However, one of the major factors hindering the application of RL to real-world continuous control tasks is the modeling gap between simulation and real-world which can lead to unpredictable, and often unwanted, results. More specifically, learning policies requires a large amount of training data, which is expensive to collect if trained directly in real-world environment. Thus, simulators are often used for learning policies before deploying to real-world problems. However, such simulation models usually contain uncertainties, i.e., a reality gap, which makes the policies trained in simulation less desirable in real applications. In this paper, we propose an algorithm to improve the robustness of RL against such model uncertainties.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

There are two popular approaches to robust RL: by minimizing the expected loss in the worst case via minimax formulations and by considering risk-sensitive optimization criteria during training. The relation between the two has been studied in Jacobson; Coraluppi and Marcus; Glover and Doyle; Fleming and McEneaney. Our proposed algorithm falls into the latter. In particular, we incorperate risk-sensitive criteria within distributional reinforcement learning (DRL) framework. Instead of modeling the value function as the expected sum of rewards, the DRL framework suggests to work with the full distribution of random returns, known as value or return distribution, i.e., ${Q^{\pi}{(x,a)}} = {{\mathbb{E}}Z^{\pi}{(x,a)}}$, where $Z^{\pi}{(x,a)}$ denotes the return distribution. The return distribution $Z$ in DRL framework provides tremendous flexibility to incorporate risk in the training process.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In DRL, the return distribution is usually represented by discrete categorical form, quantile function, or samples. D4PG and SDPG are actor-critic type policy gradient algorithms based on DRL and have demonstrated much better performance as compared to its non-distributional counterpart (DDPG) for continuous control tasks. In SDPG, the return distribution is represented via samples as opposed to discrete categorical representation in D4PG, which has shown advantages in terms of sample efficiency as well as maximum rewards. Even though D4PG and SDPG learn the return distribution, they optimize the mean value of the returns and therefore, are susceptible to model uncertainties. In this work, we incorporate risk-sensitive criteria for optimizing the policy in SDPG algorithm to achieve robustness against a range of disturbances in the system. Specifically, we focus on conditional value at risk (CVaR), a widely adopted risk measure.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We perform multiple experiments to illustrate the robustness of the learned policy incorporating the risk during training against the risk-neutral policy. We demonstrate the robustness of our risk-averse SDPG algorithm against system disturbances on multiple OpenAI Gym environments for continuous control tasks including BipedalWalker, HalfCheetah, and Walker2d.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Related Work: There have been a few methods which accounted for risk within DRL framework including Morimura et al.; Dabney et al.; Tang et al.. The distributional-SARSA-with-CVaR proposed in Morimura et al. deals with discrete action space with only a small number of states. Although implicit quantile network (IQN) proposed in Dabney et al. improved upon traditional deep Q-networks (DQNs) and studied risk-sensitive policies in Atari games, it is a value function based approach and thus not suitable for tasks with continuous action space. Worst cases policy gradients (WCPG) proposed in Tang et al. models the return distribution $Z$ as Gaussian in order to calculate CVaR in closed form, but this restriction may undermine the advantages of DRL. In terms of taxonomy presented by Garcıa and Fernández, our approach lies in the risk-sensitive criterion.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The contributions of this work are as follows: (a) We propose a novel RL algorithm to learn robust policies for continuous control tasks. Our algorithm is based on the recently discovered DRL framework. The fact that DRL learns the distribution instead of the mean of the cost-to-go function makes it suitable for risk-sensitive learning. We further took advantage our recent algorithm SDPG to evaluate the risk criteria efficiently using samples. (b) We empirically evaluate the performance of our algorithm on multiple OpenAI Gym environments.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Rest of the document is organized as follows. First we briefly discuss background on DRL, SDPG, and risk measures in Section 2. Next, we present our risk-averse SDPG algorithm in Section 3 followed by experimental results in Section 4. Finally, Section 5 concludes the paper.

<!-- chunk {"id": "body-0010", "role": "body", "section": "DRL", "weight": 1.0} -->

Distributional reinforcement learning (DRL) models intrinsic randomness of return in form of full return distribution for each state-action pair Apparently, Q-function is the mean of return distribution, i.e., ${Q^{\pi}{(x,a)}} = {{\mathbb{E}}Z^{\pi}{(x,a)}}$. The return distribution satisfies distributional Bellman's equation where the equality is in the probability sense.

<!-- chunk {"id": "body-0011", "role": "body", "section": "DRL", "weight": 1.0} -->

Different methods have been proposed to parameterize a return distribution in DRL. C51 and D4PG use discrete categorical distribution, QR-DQN and IQN utilize quantiles, and VDGL and SDPG use samples to model a return distribution. These DRL algorithms have shown significant performance improvements over non-distributional counterparts in multiple environments including Atari games and DeepMind Control Suite.

<!-- chunk {"id": "body-0012", "role": "body", "section": "SDPG", "weight": 1.0} -->

Sample based policy gradient (SDPG) is an actor-critic type policy gradient method within DRL framework where return distribution is represented by samples through a reparametrization technique. The actor network in SDPG parameterizes the policy while the critic network is trained to mimic the return distribution determined via distributional Bellman equation based on samples. A flow diagram of the critic in SDPG is shown in Figure 1. The critic network $G_{\phi}$ in SDPG learns the return distribution by utilizing quantile Huber loss as a surrogate of Wasserstein distance: where $z_{1} \geq z_{2} \geq {\ldotsz_{n}}$ are samples after sorting.

<!-- chunk {"id": "body-0013", "role": "body", "section": "SDPG", "weight": 1.0} -->

Using the distributional policy gradient theorem, the gradient of the loss function of the actor network $\pi_{\theta}$ is computed as Figure 1: Flow diagram of SDPG.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Risk Measures", "weight": 1.0} -->

The notion of risk in RL is related to the fact that even an optimal policy may perform poorly in some cases due to the stochastic nature of the problem. Risk-aware methods in RL have considered different forms of risk including the variance of the return, worst outcomes, exponential utility function, value at risk (VaR), and conditional value at risk (CVaR). In this work, we focus on CVaR.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Risk Measures", "weight": 1.0} -->

CVaR of a random variable $Z$ at level $\alpha \in {\lbrack 0,1\rbrack}$ is defined as^11^1In this case we are incorporating CVaR while maximizing reward, which is opposite to incorporating CVaR while minimizing cost. Moreover, CVaR given by is lower-tail CVaR resulting in risk-averse policy.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Risk Measures", "weight": 1.0} -->

When $\alpha = 0$, CVaR becomes expectation of the random variable which reduces to risk-neutral setting.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Risk averse SDPG", "weight": 1.0} -->

In order to take risk into account in policy learning, we utilize the return distribution to incorporate risk. We use CVaR as the risk-measure to learn the policy. Similar to SDPG, the risk-sensitive SDPG consists of two neural networks: a critic and an actor. The critic network $G_{\phi}$, parameterized by $\phi$, generates samples representing the return distribution by reparameterizing noise for each state-action pair. These samples are compared against the target samples determined via distributional Bellman equation given. The quantile Huber loss is used for updating the critic network as given by Equation.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Risk averse SDPG", "weight": 1.0} -->

Require: Learning rates β1 and β2, CVaR level α, batch size M, sample size n, exploration constant δ, Initialize the the actor network (π) parameters θ, critic network (G) parameters ϕ randomly Initialize target networks ${(\overset{\sim}{\theta},\overset{\sim}{\phi})}\leftarrow{(\theta,\phi)}$ for the number of environment steps do Sample M number of transitions {(xti, ati, rti, xt + 1i)}i = 1M from the replay pool Sample noise {qji}j = 1n ∼ 𝒩 and ${\{{\overset{\sim}{q_{j}}}^{i}\}}_{j = 1}^{n} \sim {\mathcal{N}{}}$, for i = 1, …, M Apply Bellman update to create samples (of return distribution) ${{\overset{\sim}{z}}_{j}^{i} = {r_{t}^{i} +

<!-- chunk {"id": "body-0019", "role": "body", "section": "Risk averse SDPG", "weight": 1.0} -->

{\pi_{\theta}{(x_{t}^{i})}}}$ Update target networks ${(\overset{\sim}{\theta},\overset{\sim}{\phi})}\leftarrow{(\theta,\phi)}$ Observe (xt xt + 1) and draw reward rt Store (xt rt, xt + 1, at + 1) in replay pool until learner finishes Algorithm 1 Risk-averse SDPG The actor network $\pi_{\theta}$, parameterized by $\theta$, outputs the action $\pi_{\theta}{(x)}$ given a state $x$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Risk averse SDPG", "weight": 1.0} -->

The actor network incorporates risk as feedback from the critic network $G_{\phi}$ in terms of the gradients of the empirical CVaR (given by Equation 8) of the return distribution with respect to the actions determined by the policy. This feedback is used to update the actor network by applying distributional form of the policy gradient theorem. Therefore, the gradient of the actor network loss function is where ${\hat{v}}_{n,\alpha} = z_{\lfloor{n{({1 - \alpha})}}\rfloor}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Risk averse SDPG", "weight": 1.0} -->

All the steps of risk-averse SDPG algorithm are described in Algorithm 1. The network parameters of actor and critic networks are updated alternatively in stochastic gradient ascent/descent fashion.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate the robustness of our risk-averse SDPG algorithm against system disturbances on multiple OpenAI Gym continuous control tasks. For both actor and critic networks, we use a two layer feedforward neural network with hidden layer sizes of 400 and 300, respectively, and rectified linear units (ReLU) between each hidden layer. We also used batch normalization on all the layers of both networks. Moreover, the output of the actor network is passed through a hyperbolic tangent (Tanh) activation unit. In all experiments we use learning rates of $\beta_{1} = \beta_{2} = {1 \times 10^{- 4}}$, batch size $M = 256$, exploration constant $\delta = 0.3$, and $\zeta = 1$. Across all the tasks, we use $n = 51$ number of samples to represent return distributions. Moreover, we run each task for a maximum of 1000 steps per episode. We consider four different levels of disturbances on action forces to evaluate the robustness of learned policies at different $\alpha$ levels of CVaR. We parameterize the disturbances in terms of Gaussian noise added to action forces during evaluation.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experiments", "weight": 1.0} -->

We consider the disturbances at multiple noise scales to illustrate the robustness. For each environment, we consider different $NoiseLevel$ of the disturbances depending on the highest action value corresponding to the domain. Specifically, ${NoiseLevel} = {0.3 \times a_{max}}$ is the variance of the added zero mean Gaussian noise with $a_{max}$ being the highest possible action value corresponding to the environment. Due to the lack of a perfect actuator, the experiments model scenarios when we deploy the policy to the real-world.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experiments", "weight": 1.0} -->

We consider the following environments in our experiments: BipedalWalker-v2, HalfCheetah-v2, and Walker2d-v2. The task of an agent in all the three domains is to walk (run) as fast as possible without falling down and the reward is given for moving forward. We choose these environments because the reward has a large penalty when the robot falls down. These environments are not safe as compared to the other environments; the risky environment will have a value distribution with higher variance, which means there will be a higher probability that worst case scenario happens regardless of the expected reward. The state in BipedalWalker-v2 domain is 24-dimensional representing hull angle speed, angular velocity, horizontal speed, vertical speed, position of joints and joints angular speed, legs contact with ground, and $10$ lidar rangefinder measurements. The action space consists of actuator motor torques at 4 different joints. For both HalfCheetah-v2 and Walker2d-v2 domains, the state space is 18 dimensional consisting of positions, angles, and velocities of different joints while the dimension of action space is 6 consisting of actuator torques.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Experiments", "weight": 1.0} -->

In each environment, we learn policies at different CVaR values $\alpha$ and evaluate the learned policies over 1000 trajectories for multiple levels of action disturbances. We also present the estimates of cumulative distribution functions (CDFs) from a total of 5000 rewards of trajectories. For all experiments in various environments, our risk-averse algorithms show similar performance during training compared to risk-neutral one.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we proposed a robust RL algorithm for real-world applications with continuous state action spaces. Our algorithm is based on distributional reinforcement learning which is an idea framework for integrating risk. We utilized sample based policy gradients in this framework and incorporated CVaR to learn risk-averse policies. We demonstrated the robustness of the resulting policies against a range of disturbances in multiple environments. Even though we focused on a special type of risk measure, CVaR, in this work, our framework is compatible with any utility function based risk measure. We will explore these options thoroughly via experiments in the future.
