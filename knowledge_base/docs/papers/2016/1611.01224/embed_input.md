<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sample Efficient Actor-Critic with Experience Replay

Topics include Reinforcement learning, Optimization, Control, Learning, Sampling.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents an actor-critic deep reinforcement learning agent with experience replay that is stable, sample efficient, and performs remarkably well on challenging environments, including the discrete 57-game Atari domain and several continuous control problems. To achieve this, the paper introduces several innovations, including truncated importance sampling with bias correction, stochastic dueling network architectures, and a new trust region policy optimization method.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Realistic simulated environments, where agents can be trained to learn a large repertoire of cognitive skills, are at the core of recent breakthroughs in AI [Bellemare:2013,Mnih:2015,Schulman:2015,Narasimhan:2015,Mnih:2016,Brockman:2016,Oh:2016]. With richer realistic environments, the capabilities of our agents have increased and improved. Unfortunately, these advances have been accompanied by a substantial increase in the cost of simulation. In particular, every time an agent acts upon the environment, an expensive simulation step is conducted. Thus to reduce the cost of simulation, we need to reduce the number of simulation steps (i.e. samples of the environment). This need for sample efficiency is even more compelling when agents are deployed in the real world. [Lin:1992] has gained popularity in deep $Q$-learning [Mnih:2015,Schaul:2015,Wang:2016,Narasimhan:2015], where it is often motivated as a technique for reducing sample correlation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Replay is actually a valuable tool for improving sample efficiency and, as we will see in our experiments, state-of-the-art deep $Q$-learning methods [Schaul:2015,Wang:2016] have been up to this point the most sample efficient techniques on Atari by a significant margin. However, we need to do better than deep $Q$-learning, because it has two important limitations. First, the deterministic nature of the optimal policy limits its use in adversarial Second, finding the greedy action with respect to the $Q$function is costly for large action spaces.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy gradient methods have been at the heart of significant advances in AI and robotics [silver2014deterministic,lillicrap2015continuous,alphago,levine2015end,Mnih:2016,Schulman:2015,heess2015svg]. Many of these methods are restricted to continuous domains or to very specific tasks such as playing Go. The existing variants applicable to both continuous and discrete domains, such as the on-policy asynchronous advantage actor critic (A3C) of [Mnih:2016], are sample inefficient.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The design of stable, sample efficient actor critic methods that apply to both continuous and discrete action spaces has been a long-standing hurdle of reinforcement learning (RL). We believe this paper is the first to address this challenge successfully at scale. More specifically, we introduce an actor critic with experience replay (ACER) that nearly matches the state-of-the-art performance of deep $Q$-networks with prioritized replay on Atari, and substantially outperforms A3C in terms of sample efficiency on both Atari and continuous control domains.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

ACER capitalizes on recent advances in deep neural networks, variance reduction techniques, the off-policy Retrace algorithm [Munos:2016] and parallel training of RL agents[Mnih:2016]. Yet, crucially, its success hinges on innovations advanced in this paper: truncated importance sampling with bias correction, stochastic dueling network architectures, and efficient trust region policy optimization.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the theoretical front, the paper proves that the Retrace operator can be rewritten from our proposed truncated importance sampling with bias correction technique.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Discrete Actor Critic with Experience Replay", "weight": 1.0} -->

Off-policy learning with experience replay may appear to be an obvious strategy for improving the sample efficiency of actor-critics. However, controlling the variance and stability of off-policy estimators is notoriously hard. Importance sampling is one of the most popular approaches for off-policy learning [Meuleau:2000,Jie:2010,Levin:2013]. In our context, it proceeds as follows. Suppose we retrieve a trajectory $\{x_0, a_{0}, r_0, \mu(\cdot | x_0), \cdots, x_{k}, a_{k}, r_{k}, \mu(\cdot | x_{k})\}$, where the actions have been sampled according to the behavior policy $\mu$, from our memory of experiences.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Discrete Actor Critic with Experience Replay", "weight": 1.0} -->

Then, the importance weighted policy gradient is given: $$\widehat{g}^{\mbox{\small imp}} = \left(\prod_{t = 0}^k \rho_{t} \right) \sum_{t = 0}^k \left(\sum_{i = 0}^k \gamma^i r_{t+i}\right) \nabla_{\theta}\log \pi_{\theta}(a_t|x_t),$$ where $\rho_{t} = \frac{\pi(a_{t}|x_{t})}{\mu(a_{t}|x_{t})}$ denotes the importance weight. This estimator is unbiased, but it suffers from very high variance as it involves a product of many potentially unbounded importance weights. To prevent the product of importance weights from exploding, [wawrzynski2009real] truncates this product. Truncated importance sampling over entire trajectories, although bounded in variance, could suffer from significant bias.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Discrete Actor Critic with Experience Replay", "weight": 1.0} -->

[Degris:2012] attacked this problem by using marginal value functions over the limiting distribution of the process to yield the following approximation of the gradient: g^{\mbox{\small marg}} = \mathbb{E}_{x_t \sim \beta, a_t \sim \mu}\left[\rho_t \nabla_{\theta} \log \pi_{\theta}(a_t|x_t) Q^{\pi}(x_t, a_t)\right], where $\mathbb{E}_{x_t \sim \beta, a_t \sim \mu}[\cdot]$ is the expectation with respect to the limiting distribution $\beta(x) = \lim_{t\rightarrow \infty} P(x_t=x|x_0,\mu)$ with behavior policy $\mu$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Discrete Actor Critic with Experience Replay", "weight": 1.0} -->

To keep the notation succinct, we will replace $\mathbb{E}_{x_t \sim \beta, a_t \sim \mu}[\cdot]$ with $\mathbb{E}_{x_ta_t}[\cdot]$and ensure we remind readers of this when necessary.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Discrete Actor Critic with Experience Replay", "weight": 1.0} -->

Two important facts about equation ([eqn:offpac]) must be highlighted. First, note that it depends on $Q^{\pi}$ and not on $Q^{\mu}$, consequently we must be able to estimate $Q^{\pi}$. Second, we no longer have a product of importance weights, but instead only need to estimate the marginal importance weight $\rho_t$. Importance sampling in this lower dimensional space (over marginals as opposed to trajectories) is expected to exhibit lower variance. [Degris:2012] estimate $Q^{\pi}$ in equation([eqn:offpac]) using lambda returns: $R^{\lambda}_{t} = r_t + (1-\lambda)\gamma V(x_{t+1}) + \lambda \gamma \rho_{t+1} R^{\lambda}_{t+1}$. This estimator requires that we know how to choose $\lambda$ ahead of time to trade off bias and variance.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Discrete Actor Critic with Experience Replay", "weight": 1.0} -->

Moreover, when using small values of $\lambda$to reduce variance, occasional large importance weights can still cause instability.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Discrete Actor Critic with Experience Replay", "weight": 1.0} -->

In the following subsection, we adopt the Retrace algorithm of [Munos:2016] to estimate $Q^{\pi}$. Subsequently, we propose an importance weight truncation technique to improve the stability of the off-policy actor critic of[Degris:2012], and introduce a computationally efficient trust region scheme for policy optimization. The formulation of ACER for continuous action spaces will require further innovations that are advanced in Section[sec:cont].

<!-- chunk {"id": "body-0016", "role": "body", "section": "Multi-Step Estimation of the State-Action Value Function", "weight": 1.0} -->

In this paper, we estimate $Q^{\pi}(x_t, a_t)$ using Retrace[Munos:2016]. Given a trajectory generated under the behavior policy $\mu$, the Retrace estimator can be expressed recursively as follows For ease of presentation, we consider only $\lambda = 1$ for Retrace.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Multi-Step Estimation of the State-Action Value Function", "weight": 1.0} -->

Retrace is an off-policy, return-based algorithm which has low variance and is proven to converge (in the tabular case) to the value function of the target policy for any behavior policy, see[Munos:2016].

<!-- chunk {"id": "body-0018", "role": "body", "section": "Multi-Step Estimation of the State-Action Value Function", "weight": 1.0} -->

The recursive Retrace equation depends on the estimate $Q$. To compute it, in discrete action spaces, we adopt a convolutional neural network with two heads that outputs the estimate $Q_{\theta_v}(x_t, a_t)$, as well as the policy $\pi_{\theta}(a_t|x_t)$. This neural representation is the same as in[Mnih:2016], with the exception that we output the vector $Q_{\theta_v}(x_t, a_t)$ instead of the scalar $V_{\theta_v}(x_t)$. The estimate $V_{\theta_v}(x_t)$ can be easily derived by taking the expectation of $Q_{\theta_v}$ under $\pi_{\theta}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Multi-Step Estimation of the State-Action Value Function", "weight": 1.0} -->

To approximate the policy gradient $g^{\mbox{\small marg}}$, ACER uses $Q^{\mbox{\small ret}}$ to estimate $Q^{\pi}$. As Retrace uses multi-step returns, it can significantly reduce bias in the estimation of the policy gradient An alternative to Retrace here is $Q(\lambda)$ with off-policy corrections which we discuss in more detail in Appendixsec:opc.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Multi-Step Estimation of the State-Action Value Function", "weight": 1.0} -->

To learn the critic $Q_{\theta_{v}}(x_t, a_t)$, we again use $Q^{\mbox{\small ret}}(x_t, a_t)$ as a target in a mean squared error loss and update its parameters $\theta_{v}$ with the following standard gradient: $$(Q^{\mbox{\small ret}}(x_t, a_t) - Q_{\theta_{v}}(x_t, a_t)) \nabla_{\theta_{v}}Q_{\theta_{v}}(x_t, a_t)).$$ Because Retrace is return-based, it also enables faster learning of the critic. Thus the purpose of the multi-step estimator $Q^{\mbox{\small ret}}$in our setting is twofold: to reduce bias in the policy gradient, and to enable faster learning of the critic, hence further reducing bias.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Importance Weight Truncation with Bias Correction", "weight": 1.0} -->

The clipping of the importance weight in the first term of equation ([eqn:compTrickExact]) ensures that the variance of the gradient estimate is bounded. The correction term (second term in equation([eqn:compTrickExact])) ensures that our estimate is unbiased. Note that the correction term is only active for actions such that $\rho_{t}(a) > c$. In particular, if we choose a large value for $c$, the correction term only comes into effect when the variance of the original off-policy estimator of equation([eqn:offpac]) is very high. When this happens, our decomposition has the nice property that the truncated weight in the first term is at most $c$ while the correction weight $\left[\frac{\rho_{t}(a)-c}{\rho_{t}(a)}\right]_+$ in the second term is at most $1$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Importance Weight Truncation with Bias Correction", "weight": 1.0} -->

We model $Q^{\pi}(x_t,a)$ in the correction term with our neural network approximation $Q_{\theta_v}(x_t, a_t)$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Importance Weight Truncation with Bias Correction", "weight": 1.0} -->

x_t)Q_{\theta_v}(x_t, a) \right) \right].$$ ([eqn:compTrick]) involves an expectation over the stationary distribution of the Markov process.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Importance Weight Truncation with Bias Correction", "weight": 1.0} -->

We can however approximate it by sampling trajectories $\{x_0, a_{0}, r_0, \mu(\cdot | x_0), \cdots, x_{k}, a_{k}, r_{k}, \mu(\cdot | x_{k})\}$ generated from the behavior policy $\mu$. Here the terms $\mu(\cdot | x_t)$ are the policy vectors.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Importance Weight Truncation with Bias Correction", "weight": 1.0} -->

the classical baseline $V_{\theta_v}(x_t)$ to reduce variance.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Importance Weight Truncation with Bias Correction", "weight": 1.0} -->

It is interesting to note that, when $c=\infty$, ([eqn:update]) recovers (off-policy) policy gradient up to the use of Retrace. When $c=0$, ([eqn:update]) recovers an actor critic update that depends entirely on $Q$ estimates. In the continuous control domain, ([eqn:update]) also generalizes Stochastic Value Gradients if $c=0$ and the reparametrization trick is used to estimate its second term [heess2015svg].

<!-- chunk {"id": "body-0027", "role": "body", "section": "Efficient Trust Region Policy Optimization", "weight": 1.0} -->

The policy updates of actor-critic methods do often exhibit high variance. Hence, to ensure stability, we must limit the per-step changes to the policy. Simply using smaller learning rates is insufficient as they cannot guard against the occasional large updates while maintaining a desired learning speed. Trust Region Policy Optimization (TRPO) [Schulman:2015]provides a more adequate solution. [Schulman:2015]approximately limit the difference between the updated policy and the current policy to ensure safety. Despite the effectiveness of their TRPO method, it requires repeated computation of Fisher-vector products for each update. This can prove to be prohibitively expensive in large domains.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Efficient Trust Region Policy Optimization", "weight": 1.0} -->

In this section we introduce a new trust region policy optimization method that scales well to large problems. Instead of constraining the updated policy to be close to the current policy (as in TRPO), average policy networkthat represents a running average of past policies and forces the updated policy to not deviate far from this average.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Efficient Trust Region Policy Optimization", "weight": 1.0} -->

We decompose our policy network in two parts: and a deep neural network that generates the statistics $\phi_{\theta}(x)$ of this distribution. That is, given $f$, the policy is completely characterized by the network $\phi_{\theta}$: $\pi(\cdot | x) = f(\cdot | \phi_{\theta}(x))$. For example, in the discrete domain, we choose $f$ to be the categorical distribution with a probability vector $\phi_{\theta}(x)$ as its statistics. The probability vector is of course parameterised by $\theta$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Efficient Trust Region Policy Optimization", "weight": 1.0} -->

We denote the average policy network as $\phi_{\theta_a}$ and update its parameters $\theta_a$ softly after each update to the policy parameter $\theta$: $\theta_a \leftarrow \alpha \theta_a + (1- \alpha)\theta.$ Consider, for example, the ACER policy gradient as defined in Equation ([eqn:update]), but with respect to $\phi$: $$\widehat{g}_t^{\mbox{\small acer}} &=& \bar{\rho}_{t} \nabla_{\phi_{\theta}(x_t)} \log f(a_t | \phi_{\theta}(x)) [Q^{\mbox{\small ret}}(x_t, a_t) - V_{\theta_v}(x_t)] \nonumber \\&& + \underset{a \sim \pi}{\mathbb{E}}

<!-- chunk {"id": "body-0031", "role": "body", "section": "Efficient Trust Region Policy Optimization", "weight": 1.0} -->

\left(\left[\frac{\rho_{t}(a) - c}{\rho_{t}(a)} \right]_+ \nabla_{\phi_{\theta}(x_t)} \log f(a_t | \phi_{\theta}(x))[Q_{\theta_v}(x_t, a)- V_{\theta_v}(x_t)] \right).$$ Given the averaged policy network, our proposed trust region update involves two stages.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Efficient Trust Region Policy Optimization", "weight": 1.0} -->

In the first stage, we solve the following optimization problem with a linearized KL divergence constraint: & \underset{z}{\text{minimize}} & & \frac{1}{2}\| \hat{g}^{\mbox{\small acer}}_t - z\|^2_2 \\& & \nabla_{\phi_{\theta}(x_t)} D_{KL}\left[f(\cdot | \phi_{\theta_a}(x_t)) \| f(\cdot | \phi_{\theta}(x_t)) \right]^T z \leq \delta Since the constraint is linear, the overall optimization problem reduces to a simple quadratic programming problem, the solution of which can be easily derived in closed form using the KKT conditions.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Efficient Trust Region Policy Optimization", "weight": 1.0} -->

Letting $k = \nabla_{\phi_{\theta}(x_t)} D_{KL}\left[f(\cdot | \phi_{\theta_a}(x_t) \| f(\cdot | \phi_{\theta}(x_t)\right]$, the solution is: $$z^* = \hat{g}^{\mbox{\small acer}}_t - \max\left\{0, \frac{ k^T \hat{g}^{\mbox{\small acer}}_t - \delta}{\| k\|^2_2}\right\} k$$ This transformation of the gradient has a very natural form. If the constraint is satisfied, there is no change to the gradient with respect to $\phi_\theta(x_t)$. Otherwise, the update is scaled down in the direction of $k$, thus effectively lowering rate of change between the activations of the current policy and the average policy network.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Efficient Trust Region Policy Optimization", "weight": 1.0} -->

In the second stage, we take advantage of back-propagation. Specifically, the updated gradient with respect to $\phi_{\theta}$, that is $z^*$, is back-propagated through the network to compute the derivatives with respect to the parameters. The parameter updates for the policy network follow from the chain rule: $ \frac{\partial \phi_{\theta}(x) }{\partial \theta}z^*$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Efficient Trust Region Policy Optimization", "weight": 1.0} -->

The trust region step is carried out in the space of the statistics $f$, and not in the space of the policy parameters. This is done deliberately so as to avoid an additional back-propagation step through the policy network.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Efficient Trust Region Policy Optimization", "weight": 1.0} -->

We would like to remark that the algorithm advanced in this section can be thought of as a general strategy for modifying the backward messages in back-propagation so as to stabilize the activations.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Efficient Trust Region Policy Optimization", "weight": 1.0} -->

Instead of a trust region update, one could alternatively add an appropriately scaled KL cost to the objective function as proposed by This approach, however, is less robust to the choice of hyper-parameters in our experience.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Efficient Trust Region Policy Optimization", "weight": 1.0} -->

The ACER algorithm results from a combination of the above ideas, with the precise pseudo-code appearing in Appendix A master algorithm (Algorithm[alg:a2cMaster]) calls ACER on-policy to perform updates and propose trajectories. It then calls ACER off-policy component to conduct several replay steps. When on-policy, ACER effectively becomes a modified version of A3C where $Q$ instead of $V$baselines are employed and trust region optimization is used.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Results on Atari", "weight": 1.0} -->

We use the Arcade Learning Environment of [Bellemare:2013]to conduct an extensive evaluation. We deploy one single algorithm and network architecture, with fixed hyper-parameters, to learn to play 57 Atari games given only raw pixel observations and game rewards. This task is highly demanding because of the diversity of games, and high-dimensional pixel-level observations.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Results on Atari", "weight": 1.0} -->

Our experimental setup uses $16$ actor-learner threads running on a single machine with no GPUs. We adopt the same input pre-processing and network architecture as[Mnih:2015]. Specifically, the network consists of a convolutional layer with 32 $8 \times 8$ filters with stride $4$ followed by another convolutional layer with 64 $4 \times 4$ filters with stride $2$, followed by a final convolutional layer with 64 $3 \times 3$ filters with stride $1$, followed by a fully-connected layer of size $512$. Each of the hidden layers is followed by a rectifier nonlinearity. The network outputs a softmax policy and $Q$ values.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Results on Atari", "weight": 1.0} -->

ACER improvements in sample complexity on Atari. On each plot, the median of the human-normalized score across all 57 Atari games is presented for 4 ratios of replay with 0 replay corresponding to on-policy A3C. The colored solid and dashed lines represent ACER with and without trust region updating respectively. The environment steps are counted over all threads. The gray curve is the original DQN agent[Mnih:2015] and the black curve is one of the Prioritized Double DQN agents from [Schaul:2015].

<!-- chunk {"id": "body-0042", "role": "body", "section": "Results on Atari", "weight": 1.0} -->

When using replay, we add to each thread a replay memory that is up to $50\,000$ frames in size. The total amount of memory used across all threads is thus similar in size to that of DQN [Mnih:2015]. For all Atari experiments, we use a single learning rate adopted from an earlier implementation of A3C without further tuning. We do not anneal the learning rates over the course of training We otherwise adopt the same optimization procedure as in[Mnih:2016]. Specifically, we adopt entropy regularization with weight $0.001$, discount the rewards with $\gamma = 0.99$, and perform updates every $20$ steps ($k=20$ in the notation of Section[sec:async]). In all our experiments with experience replay, we use importance weight truncation with $c=10$. We consider training ACER both with and without trust region updating as described in Section[sec:TR]. When trust region updating is used, we use $\delta=1$ and $\alpha = 0.99$for all experiments.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Results on Atari", "weight": 1.0} -->

To compare different agents, we adopt as our metric the median of the human normalized score over all 57 games. The normalization is calculated such that, for each game, human scores and random scores are evaluated to 1, and 0 respectively. The normalized score for a given game at time $t$ is computed as the average normalized score over the past $1$ million consecutive frames encountered until time $t$. For each agent, we plot its cumulative maximum median score over time. The result is summarized in Figure[fig:atari\_median].

<!-- chunk {"id": "body-0044", "role": "body", "section": "Results on Atari", "weight": 1.0} -->

The four colors in Figure [fig:atari\_median] correspond to four replay ratios (0, 1, 4 and 8) with a ratio of 4 meaning that we use the off-policy component of ACER 4 times after using the on-policy component (A3C). That is, a replay ratio of 0 means that we are using A3C. The solid and dashed lines represent ACER with and without trust region updating respectively. The gray and black curves are the original DQN[Mnih:2015] and Prioritized Replay agent of[Schaul:2015]agents respectively.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Results on Atari", "weight": 1.0} -->

As shown on the left panel of Figure [fig:atari\_median], replay significantly increases data efficiency. We observe that when using the trust region optimizer, the average reward as a function of the number of environmental steps increases with the ratio of replay. This increase has diminishing returns, but with enough replay, ACER can match the performance of the best DQN agents. Moreover, it is clear that the off-policy actor critics (ACER) are much more sample efficient than their on-policy counterpart (A3C).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Results on Atari", "weight": 1.0} -->

The right panel of Figure [fig:atari\_median]shows that ACER agents perform similarly to A3C when measured by wall clock time. Thus, in this case, it is possible to achieve better data-efficiency without necessarily compromising on computation time. In particular, ACER with a replay ratio of 4 is an appealing alternative to either the prioritized DQN agent or A3C.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Continuous Actor Critic with Experience Replay", "weight": 1.0} -->

Retrace requires estimates of both $Q$ and $V$, but we cannot easily integrate over $Q$ to derive $V$ in continuous action spaces. In this section, we propose a solution to this problem in the form of a novel representation for RL, as well as modifications necessary for trust region updating.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Policy Evaluation", "weight": 1.0} -->

Retrace provides a target for learning $Q_{\theta_v}$, but not for learning $V_{\theta_v}$. We could use importance sampling to compute $V_{\theta_v}$ given $Q_{\theta_v}$, but this estimator has high variance.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Policy Evaluation", "weight": 1.0} -->

A schematic of the Stochastic Dueling Network. In the drawing, $[u_1, \cdots, u_n]$ are assumed to be samples from $\pi_{\theta}(\cdot | x_t)$. This schematic illustrates the concept of SDNs but does not reflect the real sizes of the networks used.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Policy Evaluation", "weight": 1.0} -->

In addition to SDNs, however, we also construct the following novel target for estimating $V^{\pi}$: $$V^{target}(x_t) = \min\left\{1, \frac{\pi(a_t|x_t)}{\mu(a_t|x_t)} \right\}\left(Q^{\mbox{\small ret}}(x_t, a_t) - Q_{\theta_v}(x_t, a_t)\right) + V_{\theta_v}(x_t).$$ The above target is also derived via the truncation and bias correction trick; for more details, see Appendix[sec:vTargetDerivation].

<!-- chunk {"id": "body-0051", "role": "body", "section": "Policy Evaluation", "weight": 1.0} -->

Finally, when estimating $Q^{\mbox{\small ret}}$ in continuous domains, we implement a slightly different formulation of the truncated importance weights $\bar{\rho}_{t} = \min\left\{1, \left(\frac{\pi(a_{t}|x_{t})}{\mu(a_{t}|x_{t})}\right)^{\frac{1}{d}}\right\}$, where $d$ is the dimensionality of the action space. Although not essential, we have found this formulation to lead to faster learning.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Trust Region Updating", "weight": 1.0} -->

To adopt the trust region updating scheme (Section[sec:TR]) in the continuous one simply has to choose a distribution $f$ and a gradient specification $\hat{g}^{\mbox{\small acer}}_t$suitable for continuous action spaces.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Trust Region Updating", "weight": 1.0} -->

For the distribution $f$, we choose Gaussian distributions with fixed diagonal covariance and mean $\phi_{\theta}(x)$. $\hat{g}^{\mbox{\small acer}}_t$ in continuous action spaces, consider the ACER policy gradient for the stochastic dueling network, but with respect to $\phi$: $$g^{\mbox{\small acer}}_t &=& \mathbb{E}_{x_t} \left[\mathbb{E}_{a_t} \biggl[\bar{\rho}_t \nabla_{\phi_{\theta}(x_t)} \log f(a_t | \phi_{\theta}(x_t)) (Q^{\mbox{\small opc}}(x_t, a_t) - V_{\theta_v}(x_t)) \biggl] \right. \nonumber \\& & \left.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Trust Region Updating", "weight": 1.0} -->

+ \underset{a \sim \pi}{\mathbb{E}} \left(\left[\frac{\rho_{t}(a) - c}{\rho_{t}(a)} \right]_+ (\widetilde{Q}_{\theta_v}(x_{t}, a)- V_{\theta_v}(x_t)) \nabla_{\phi_{\theta}(x_t)} \log f(a | \phi_{\theta}(x_t)) \right) In the above definition, we are using $Q^{\mbox{\small opc}}$ instead of $Q^{\mbox{\small ret}}$. Here, $Q^{\mbox{\small opc}}(x_t, a_t)$ is the same as Retrace with the exception that the truncated importance ratio is replaced with $1$[Harutyunyan:2016]. Please refer to Appendix[sec:opc] an expanded discussion on this design choice.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Trust Region Updating", "weight": 1.0} -->

\nabla_{\phi_{\theta}(x_t)} \log f(a_t' | \phi_{\theta}(x_t)).$$ $f$ and $\hat{g}^{\mbox{\small acer}}_t$, we apply the same steps as detailed in Section[sec:TR]to complete the update.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Trust Region Updating", "weight": 1.0} -->

The precise pseudo-code of ACER algorithm for continuous spaces results is presented in Appendix

<!-- chunk {"id": "body-0057", "role": "body", "section": "Results on MuJoCo", "weight": 1.0} -->

We evaluate our algorithms on $6$ continuous control tasks, all of which are simulated using the MuJoCo physics engine [todorov2012mujoco]. For descriptions of the tasks, please refer to Appendix [sec:appen\_control:domains]. Briefly, the tasks with action dimensionality in brackets are: cartpole (1D), reacher (3D), cheetah (6D), fish (5D), walker (6D) and humanoid (21D). These tasks are illustrated in Figure[fig:cont\_results]. [Top] Screen shots of the continuous control [Bottom] Performance of different methods on these tasks. ACER outperforms all other methods and shows clear gains for the higher-dimensionality tasks (humanoid, cheetah, walker and fish). The proposed trust region method by itself improves the two baselines (truncated importance sampling and A3C) significantly.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Results on MuJoCo", "weight": 1.0} -->

To benchmark ACER for continuous control, we compare it to its on-policy counterpart both with and without trust region updating. We refer to these two baselines as A3C and Trust-A3C. Additionally, we also compare to a baseline with replay where we truncate the importance weights over trajectories as in For a detailed description of this baseline, please refer to Appendix[sec:appen\_control]. Again, we run this baseline both with and without trust region updating, and refer to these choices as Trust-TIS and TIS respectively. Last but not least, we refer to our proposed approach with SDN and trust region updating as simply ACER. All five setups are implemented in the asynchronous A3C framework.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Results on MuJoCo", "weight": 1.0} -->

All the aforementioned setups share the same network architecture that computes the policy and state values. We maintain an additional small network that computes $A$ values in the case of ACER. We use $n=5$ (using the notation in Equation ([eqn:sdn])) in all SDNs. Instead of mixing on-policy and replay learning as done in the Atari domain, ACER for continuous actions is entirely off-policy, with experiences generated from the simulator When using replay, we add to each thread a replay memory that is $5,000$ frames in size and perform updates every $50$ steps ($k=50$ in the notation of Section[sec:async]). The rate of the soft updating ($\alpha$ as in Section[sec:TR]) is set to $0.995$ in all setups involving trust region updating. The truncation threshold $c$ is set to $5$for ACER.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Results on MuJoCo", "weight": 1.0} -->

We use diagonal Gaussian policies with fixed diagonal covariances where the diagonal standard deviation is set to For all setups, we sample the learning rates log-uniformly For setups involving trust region updating, we also sample $\delta$ uniformly in the range $[0.1, 2]$. With all setups, we use $30$sampled hyper-parameter settings.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Results on MuJoCo", "weight": 1.0} -->

The empirical results for all continuous control tasks are shown Figure [fig:cont\_results], where we show the mean and standard deviation of the best $5$ out of $30$ hyper-parameter settings over which we searched For videos of the policies learned with ACER, please see: For sensitivity analyses with respect to the hyper-parameters, please refer to Figures [fig:sen\_lr] and [fig:sen\_contstraint]in the Appendix.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Results on MuJoCo", "weight": 1.0} -->

In continuous control, ACER outperforms the A3C and truncated importance sampling baselines by a very significant margin.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Results on MuJoCo", "weight": 1.0} -->

Here, we also find that the proposed trust region optimization method can result in huge improvements over the baselines. The high-dimensional continuous action policies are much harder to optimize than the small discrete action policies in Atari, and hence we observe much higher gains for trust region optimization in the continuous control domains. In spite of the improvements brought in by trust region optimization, ACER still outperforms all other methods, specially in higher dimensions.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Ablations", "weight": 1.0} -->

To further tease apart the contributions of the different components of ACER, we conduct an ablation analysis where we individually remove Retrace / Q($\lambda$) off-policy correction, SDNs, trust region, and truncation with bias correction from the algorithm. As shown in Figure[fig:ablation], Retrace and off-policy correction, SDNs, and trust region are critical: removing any one of them leads to a clear deterioration of the performance. Truncation with bias correction did not alter the results in the Fish and Walker2d tasks. However, in Humanoid, where the dimensionality of the action space is much higher, including truncation and bias correction brings a significant boost which makes the originally kneeling humanoid stand. Presumably, the high dimensionality of the action space increases the variance of the importance weights which makes truncation with bias correction important. For more details on the experimental setup please see Appendix [appen:ablation].

<!-- chunk {"id": "body-0065", "role": "body", "section": "Ablations", "weight": 1.0} -->

| | Fish | Walker2d | Humanoid | Ablation analysis evaluating the effect of different components of ACER. Each row compares ACER with and without one component. The columns represents three control tasks. Red lines, in all plots, represent ACER whereas green lines ACER with missing components. This study indicates that all 4 components studied improve performance where 3 are critical to success. Note that the ACER curve is of course the same in all rows.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

Retrace is a very recent development in reinforcement learning. In fact, this work is the first to consider Retrace in the policy gradients setting. For this reason, and given the core role that Retrace plays in ACER, it is valuable to shed more light on this technique. In this section, we will prove that Retrace can be interpreted as an application of the importance weight truncation and bias correction trick advanced in this paper.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

Consider the following equation: \gamma \rho_{t+1} Q^{\pi}(x_{t+1}, a_{t+1})\right].$$ If we apply the weight truncation and bias correction trick to the above equation \gamma \bar{\rho}_{t+1} Q^{\pi}(x_{t+1}, a_{t+1}) + \gamma \underset{a \sim \pi}{\mathbb{E}} \left(\left[\frac{\rho_{t+1}(a)-c}{\rho_{t+1}(a)}\right]_+ Q^{\pi}(x_{t+1}, a) \right) By recursively expanding $Q^{\pi}$ as in Equation([eqn:qpiTBC]), we can represent $Q^{\pi}(x, a)$ as: \sum_{t \geq 0} \gamma^{t}

<!-- chunk {"id": "body-0068", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

When $Q^{\pi}$ is not available, we can replace it with our current estimate $Q$ to get a return-based esitmate of $Q^{\pi}$. This operation also defines an operator: $${\cal B} Q(x, a) = \mathbb{E}_{\mu} \left[\sum_{t \geq 0} \gamma^{t} \left(\prod_{i=1}^{t} \bar{\rho}_{i} \right) \left(r_t + \gamma \underset{b \sim \pi}{\mathbb{E}} \left(\left[\frac{\rho_{t+1}(b)-c}{\rho_{t+1}(b)}\right]_+ Q(x_{t+1}, b) \right) In the following proposition, we show that ${\cal B}$ is a contraction operator with a unique fixed point $Q^{\pi}$and that it is equivalent to the Retrace operator.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

The above proposition not only shows an alternative way of arriving at the same operator, but also provides a different proof of contraction for Retrace. Please refer to Appendix [sec:retraceAsTrick]for the regularization conditions and proof of the above proposition. ${\cal B}$, and therefore Retrace, generalizes both the Bellman operator ${\cal T}^{\pi}$ and importance sampling. Specifically, when $c=0$, ${\cal B} = {\cal T}^{\pi}$ and when $c=\infty$, ${\cal B}$ recovers importance sampling; see Appendix[sec:retraceAsTrick].

<!-- chunk {"id": "body-0070", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

Retrace is a very recent development in reinforcement learning. In fact, this work is the first to consider Retrace in the policy gradients setting. For this reason, and given the core role that Retrace plays in ACER, it is valuable to shed more light on this technique. In this section, we will prove that Retrace can be interpreted as an application of the importance weight truncation and bias correction trick advanced in this paper.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

The above propositions not only confirm that retrace is a contraction, but also show a new way of deriving retrace.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

Retrace is defined by a specific choice of the trace cutting coefficients $c=\lambda\min(1,\mu/\pi)$. Other choices are possible with similar guarantees. This choice has been made for several reasons but this is definitively not the optimal solution in any sense! So there is no principle way of deriving Retrace. Retrace is just a choice. Please refer to Appendix[sec:retraceAsTrick]of the proofs for the above propositions.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

We have proposed a beautiful thing. People love it because it wins. Wins. It's gonna be great.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

We have introduced a stable off-policy actor critic that scales to both continuous and discrete action spaces. This approach integrates several recent advances in RL in a principle manner. In addition, it integrates three innovations advanced in this paper: truncated importance sampling with bias correction, stochastic dueling networks and an efficient trust region policy optimization method.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

We showed that the method not only matches the performance of the best known methods on Atari, but that it also outperforms popular techniques on several continuous control problems.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

The efficient trust region optimization method advanced in this paper performs remarkably well in continuous domains. It could prove very useful in other deep learning domains, where it is hard to stabilize the training process.
