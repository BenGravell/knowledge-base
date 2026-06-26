<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Addressing Function Approximation Error in Actor-Critic Methods

Topics include Reinforcement learning, Q-learning, Learning, Function approximation.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In value-based reinforcement learning methods such as deep Q-learning, function approximation errors are known to lead to overestimated value estimates and suboptimal policies. We show that this problem persists in an actor-critic setting and propose novel mechanisms to minimize its effects on both the actor and the critic. Our algorithm builds on Double Q-learning, by taking the minimum value between a pair of critics to limit overestimation. We draw the connection between target networks and overestimation bias, and suggest delaying policy updates to reduce per-update error and further improve performance. We evaluate our method on the suite of OpenAI gym tasks, outperforming the state of the art in every environment tested.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In reinforcement learning problems with discrete action spaces, the issue of value overestimation as a result of function approximation errors is well-studied. However, similar issues with actor-critic methods in continuous control domains have been largely left untouched. In this paper, we show overestimation bias and the accumulation of error in temporal difference methods are present in an actor-critic setting. Our proposed method addresses these issues, and greatly outperforms the current state of the art.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Overestimation bias is a property of Q-learning in which the maximization of a noisy value estimate induces a consistent overestimation. In a function approximation setting, this noise is unavoidable given the imprecision of the estimator. This inaccuracy is further exaggerated by the nature of temporal difference learning, in which an estimate of the value function is updated using the estimate of a subsequent state. This means using an imprecise estimate within each update will lead to an accumulation of error. Due to overestimation bias, this accumulated error can cause arbitrarily bad states to be estimated as high value, resulting in suboptimal policy updates and divergent behavior.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper begins by establishing this overestimation property is also present for deterministic policy gradients, in the continuous control setting. Furthermore, we find the ubiquitous solution in the discrete action setting, Double DQN, to be ineffective in an actor-critic setting. During training, Double DQN estimates the value of the current policy with a separate target value function, allowing actions to be evaluated without maximization bias. Unfortunately, due to the slow-changing policy in an actor-critic setting, the current and target value estimates remain too similar to avoid maximization bias. This can be dealt with by adapting an older variant, Double Q-learning, to an actor-critic format by using a pair of independently trained critics. While this allows for a less biased value estimation, even an unbiased estimate with high variance can still lead to future overestimations in local regions of state space, which in turn can negatively affect the global policy. To address this concern, we propose a clipped Double Q-learning variant which leverages the notion that a value estimate suffering from overestimation bias can be used as an approximate upper-bound to the true value estimate.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This favors underestimations, which do not tend to be propagated during learning, as actions with low value estimates are avoided by the policy.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Given the connection of noise to overestimation bias, this paper contains a number of components that address variance reduction. First, we show that target networks, a common approach in deep Q-learning methods, are critical for variance reduction by reducing the accumulation of errors. Second, to address the coupling of value and policy, we propose delaying policy updates until the value estimate has converged. Finally, we introduce a novel regularization strategy, where a SARSA-style update bootstraps similar action estimates to further reduce variance.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our modifications are applied to the state of the art actor-critic method for continuous control, Deep Deterministic Policy Gradient algorithm (DDPG), to form the Twin Delayed Deep Deterministic policy gradient algorithm (TD3), an actor-critic algorithm which considers the interplay between function approximation error in both policy and value updates. We evaluate our algorithm on seven continuous control domains from OpenAI gym, where we outperform the state of the art by a wide margin.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Given the recent concerns in reproducibility, we run our experiments across a large number of seeds with fair evaluation metrics, perform ablation studies across each contribution, and open source both our code and learning curves.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Overestimation Bias", "weight": 1.0} -->

In Q-learning with discrete actions, the value estimate is updated with a greedy target $y = {r + {\gamma{\max_{a'}Q}{(s',a')}}}$, however, if the target is susceptible to error $\epsilon$, then the maximum over the value along with its error will generally be greater than the true maximum, ${{\mathbb{E}}_{\epsilon}{\lbrack{\max_{a'}{({{Q{(s',a')}} + \epsilon})}}\rbrack}} \geq {{\max_{a'}Q}{(s',a')}}$. As a result, even initially zero-mean error can cause value updates to result in a consistent overestimation bias, which is then propagated through the Bellman equation. This is problematic as errors induced by function approximation are unavoidable.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Overestimation Bias", "weight": 1.0} -->

While in the discrete action setting overestimation bias is an obvious artifact from the analytical maximization, the presence and effects of overestimation bias is less clear in an actor-critic setting where the policy is updated via gradient descent. We begin by proving that the value estimate in deterministic policy gradients will be an overestimation under some basic assumptions in Section 4.1 and then propose a clipped variant of Double Q-learning in an actor-critic setting to reduce overestimation bias in Section 4.2.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Overestimation Bias in Actor-Critic", "weight": 1.0} -->

In actor-critic methods the policy is updated with respect to the value estimates of an approximate critic. In this section we assume the policy is updated using the deterministic policy gradient, and show that the update induces overestimation in the value estimate.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Overestimation Bias in Actor-Critic", "weight": 1.0} -->

Without normalized gradients, overestimation bias is still guaranteed to occur with slightly stricter conditions. We examine this case further in the supplementary material. We denote $\pi_{\text{approx}}$ and $\pi_{\text{true}}$ as the policy with parameters $\phi_{\text{approx}}$ and $\phi_{\text{true}}$ respectively.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Overestimation Bias in Actor-Critic", "weight": 1.0} -->

As the gradient direction is a local maximizer, there exists $\epsilon_{1}$ sufficiently small such that if $\alpha \leq \epsilon_{1}$ then the *approximate* value of $\pi_{\text{approx}}$ will be bounded below by the *approximate* value of $\pi_{\text{true}}$: Conversely, there exists $\epsilon_{2}$ sufficiently small such that if $\alpha \leq \epsilon_{2}$ then the *true* value of $\pi_{\text{approx}}$ will be bounded above by the *true* value of $\pi_{\text{true}}$: If in expectation the value estimate is at least as large as the true value with respect to $\phi_{true}$, ${{\mathbb{E}}\left\lbrack {Q_{\theta}\left(s,{\pi_{\text{true}}{(s)}} \right)} \right\rbrack} \geq

<!-- chunk {"id": "body-0015", "role": "body", "section": "Overestimation Bias in Actor-Critic", "weight": 1.0} -->

{{\mathbb{E}}\left\lbrack {Q^{\pi}\left(s,{\pi_{\text{true}}{(s)}} \right)} \right\rbrack}$, then Equations and imply that if $\alpha < {\min{(\epsilon_{1},\epsilon_{2})}}$, then the value estimate will be overestimated: Although this overestimation may be minimal with each update, the presence of error raises two concerns.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Overestimation Bias in Actor-Critic", "weight": 1.0} -->

Firstly, the overestimation may develop into a more significant bias over many updates if left unchecked. Secondly, an inaccurate value estimate may lead to poor policy updates. This is particularly problematic because a feedback loop is created, in which suboptimal actions might be highly rated by the suboptimal critic, reinforcing the suboptimal action in the next policy update.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Overestimation Bias in Actor-Critic", "weight": 1.0} -->

Does this theoretical overestimation occur in practice for state-of-the-art methods? We answer this question by plotting the value estimate of DDPG over time while it learns on the OpenAI gym environments Hopper-v1 and Walker2d-v1. In Figure 1, we graph the average value estimate over 10000 states and compare it to an estimate of the true value. The true value is estimated using the average discounted return over 1000 episodes following the current policy, starting from states sampled from the replay buffer. A very clear overestimation bias occurs from the learning procedure, which contrasts with the novel method that we describe in the following section, Clipped Double Q-learning, which greatly reduces overestimation by the critic.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Clipped Double Q-Learning for Actor-Critic", "weight": 1.0} -->

While several approaches to reducing overestimation bias have been proposed, we find them ineffective in an actor-critic setting. This section introduces a novel clipped variant of Double Q-learning, which can replace the critic in any actor-critic method.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Clipped Double Q-Learning for Actor-Critic", "weight": 1.0} -->

In Double Q-learning, the greedy update is disentangled from the value function by maintaining two separate value estimates, each of which is used to update the other. If the value estimates are independent, they can be used to make unbiased estimates of the actions selected using the opposite value estimate. In Double DQN, the authors propose using the target network as one of the value estimates, and obtain a policy by greedy maximization of the current value network rather than the target network. In an actor-critic setting, an analogous update uses the current policy rather than the target policy in the learning target: In practice however, we found that with the slow-changing policy in actor-critic, the current and target networks were too similar to make an independent estimation, and offered little improvement.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Clipped Double Q-Learning for Actor-Critic", "weight": 1.0} -->

Instead, the original Double Q-learning formulation can be used, with a pair of actors ($\pi_{\phi_{1}}$, $\pi_{\phi_{2}}$) and critics ($Q_{\theta_{1}}$, $Q_{\theta_{2}}$), where $\pi_{\phi_{1}}$ is optimized with respect to $Q_{\theta_{1}}$ and $\pi_{\phi_{2}}$ with respect to $Q_{\theta_{2}}$: We measure the overestimation bias in Figure 2, which demonstrates that the actor-critic Double DQN suffers from a similar overestimation as DDPG (as shown in Figure 1). While Double Q-learning is more effective, it does not entirely eliminate the overestimation. We further show this reduction is not sufficient experimentally in Section 6.1.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Clipped Double Q-Learning for Actor-Critic", "weight": 1.0} -->

As $\pi_{\phi_{1}}$ optimizes with respect to $Q_{\theta_{1}}$, using an independent estimate in the target update of $Q_{\theta_{1}}$ would avoid the bias introduced by the policy update. However the critics are not entirely independent, due to the use of the opposite critic in the learning targets, as well as the same replay buffer. As a result, for some states $s$ we will have ${Q_{\theta_{2}}{(s,{\pi_{\phi_{1}}{(s)}})}} > {Q_{\theta_{1}}{(s,{\pi_{\phi_{1}}{(s)}})}}$. This is problematic because $Q_{\theta_{1}}{(s,{\pi_{\phi_{1}}{(s)}})}$ will generally overestimate the true value, and in certain areas of the state space the overestimation will be further exaggerated.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Clipped Double Q-Learning for Actor-Critic", "weight": 1.0} -->

To address this problem, we propose to simply upper-bound the less biased value estimate $Q_{\theta_{2}}$ by the biased estimate $Q_{\theta_{1}}$. This results in taking the minimum between the two estimates, to give the target update of our Clipped Double Q-learning algorithm: With Clipped Double Q-learning, the value target cannot introduce any additional overestimation over using the standard Q-learning target. While this update rule may induce an underestimation bias, this is far preferable to overestimation bias, as unlike overestimated actions, the value of underestimated actions will not be explicitly propagated through the policy update.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Clipped Double Q-Learning for Actor-Critic", "weight": 1.0} -->

In implementation, computational costs can be reduced by using a single actor optimized with respect to $Q_{\theta_{1}}$. We then use the same target $y_{2} = y_{1}$ for $Q_{\theta_{2}}$. If $Q_{\theta_{2}} > Q_{\theta_{1}}$ then the update is identical to the standard update and induces no additional bias. If $Q_{\theta_{2}} < Q_{\theta_{1}}$, this suggests overestimation has occurred and the value is reduced similar to Double Q-learning. A proof of convergence in the finite MDP setting follows from this intuition. We provide formal details and justification in the supplementary material.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Clipped Double Q-Learning for Actor-Critic", "weight": 1.0} -->

A secondary benefit is that by treating the function approximation error as a random variable we can see that the minimum operator should provide higher value to states with lower variance estimation error, as the expected minimum of a set of random variables decreases as the variance of the random variables increases. This effect means that the minimization in Equation will lead to a preference for states with low-variance value estimates, leading to safer policy updates with stable learning targets.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Addressing Variance", "weight": 1.0} -->

While Section 4 deals with the contribution of variance to overestimation bias, we also argue that variance itself should be directly addressed. Besides the impact on overestimation bias, high variance estimates provide a noisy gradient for the policy update. This is known to reduce learning speed as well as hurt performance in practice. In this section we emphasize the importance of minimizing error at each update, build the connection between target networks and estimation error and propose modifications to the learning procedure of actor-critic for variance reduction.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Accumulating Error", "weight": 1.0} -->

Due to the temporal difference update, where an estimate of the value function is built from an estimate of a subsequent state, there is a build up of error. While it is reasonable to expect small error for an individual update, these estimation errors can accumulate, resulting in the potential for large overestimation bias and suboptimal policy updates. This is exacerbated in a function approximation setting where the Bellman equation is never exactly satisfied, and each update leaves some amount of residual TD-error $\delta{(s,a)}$: It can then be shown that rather than learning an estimate of the expected return, the value estimate approximates the expected return minus the expected discounted sum of future TD-errors: If the value estimate is a function of future reward and estimation error, it follows that the variance of the estimate will be proportional to the variance of future reward and estimation error. Given a large discount factor $\gamma$, the variance can grow rapidly with each update if the error from each update is not tamed. Furthermore each gradient update only reduces error with respect to a small mini-batch which gives no guarantees about the size of errors in value estimates outside the mini-batch.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Target Networks and Delayed Policy Updates", "weight": 1.0} -->

In this section we examine the relationship between target networks and function approximation error, and show the use of a stable target reduces the growth of error. This insight allows us to consider the interplay between high variance estimates and policy performance, when designing reinforcement learning algorithms.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Target Networks and Delayed Policy Updates", "weight": 1.0} -->

Target networks are a well-known tool to achieve stability in deep reinforcement learning. As deep function approximators require multiple gradient updates to converge, target networks provide a stable objective in the learning procedure, and allow a greater coverage of the training data. Without a fixed target, each update may leave residual error which will begin to accumulate. While the accumulation of error can be detrimental in itself, when paired with a policy maximizing over the value estimate, it can result in wildly divergent values.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Target Networks and Delayed Policy Updates", "weight": 1.0} -->

To provide some intuition, we examine the learning behavior with and without target networks on both the critic and actor in Figure 3, where we graph the value, in a similar manner to Figure 1, in the Hopper-v1 environment. In (a) we compare the behavior with a fixed policy and in (b) we examine the value estimates with a policy that continues to learn, trained with the current value estimate. The target networks use a slow-moving update rate, parametrized by $\tau$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Target Networks and Delayed Policy Updates", "weight": 1.0} -->

While updating the value estimate without target networks ($\tau = 1$) increases the volatility, all update rates result in similar convergent behaviors when considering a fixed policy. However, when the policy is trained with the current value estimate, the use of fast-updating target networks results in highly divergent behavior.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Target Networks and Delayed Policy Updates", "weight": 1.0} -->

When do actor-critic methods fail to learn? These results suggest that the divergence that occurs without target networks is the result of policy updates with a high variance value estimate. Figure 3, as well as Section 4, suggest failure can occur due to the interplay between the actor and critic updates. Value estimates diverge through overestimation when the policy is poor, and the policy will become poor if the value estimate itself is inaccurate.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Target Networks and Delayed Policy Updates", "weight": 1.0} -->

If target networks can be used to reduce the error over multiple updates, and policy updates on high-error states cause divergent behavior, then the policy network should be updated at a lower frequency than the value network, to first minimize error before introducing a policy update. We propose delaying policy updates until the value error is as small as possible. The modification is to only update the policy and target networks after a fixed number of updates $d$ to the critic. To ensure the TD-error remains small, we update the target networks slowly $\theta'\leftarrow{{\tau\theta} + {{({1 - \tau})}\theta'}}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Target Networks and Delayed Policy Updates", "weight": 1.0} -->

By sufficiently delaying the policy updates we limit the likelihood of repeating updates with respect to an unchanged critic. The less frequent policy updates that do occur will use a value estimate with lower variance, and in principle, should result in higher quality policy updates. This creates a two-timescale algorithm, as often required for convergence in the linear setting. The effectiveness of this strategy is captured by our empirical results presented in Section 6.1, which show an improvement in performance while using fewer policy updates.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Target Policy Smoothing Regularization", "weight": 1.0} -->

A concern with deterministic policies is they can overfit to narrow peaks in the value estimate. When updating the critic, a learning target using a deterministic policy is highly susceptible to inaccuracies induced by function approximation error, increasing the variance of the target. This induced variance can be reduced through regularization. We introduce a regularization strategy for deep value learning, target policy smoothing, which mimics the learning update from SARSA. Our approach enforces the notion that similar actions should have similar value. While the function approximation does this implicitly, the relationship between similar actions can be forced explicitly by modifying the training procedure. We propose that fitting the value of a small area around the target action would have the benefit of smoothing the value estimate by bootstrapping off of similar state-action value estimates. In practice, we can approximate this expectation over actions by adding a small amount of random noise to the target policy and averaging over mini-batches.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Target Policy Smoothing Regularization", "weight": 1.0} -->

This makes our modified target update: | | | ${\epsilon \sim {\operatorname{clip}{({\mathcal{N}{(0,\sigma)}},{- c},c)}}},$ | | | where the added noise is clipped to keep the target close to the original action. The outcome is an algorithm reminiscent of Expected SARSA, where the value estimate is instead learned off-policy and the noise added to the target policy is chosen independently of the exploration policy. The value estimate learned is with respect to a noisy policy defined by the parameter $\sigma$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Target Policy Smoothing Regularization", "weight": 1.0} -->

Intuitively, it is known that policies derived from SARSA value estimates tend to be safer, as they provide higher value to actions resistant to perturbations. Thus, this style of update can additionally lead to improvement in stochastic domains with failure cases. A similar idea was introduced concurrently by Nachum et al., smoothing over $Q_{\theta}$, rather than $Q_{\theta'}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

We present the Twin Delayed Deep Deterministic policy gradient algorithm (TD3), which builds on the Deep Deterministic Policy Gradient algorithm (DDPG) by applying the modifications described in Sections 4.2, 5.2 and 5.3 to increase the stability and performance with consideration of function approximation error. TD3 maintains a pair of critics along with a single actor. For each time step, we update the pair of critics towards the minimum target value of actions selected by the target policy: | | | ${\epsilon \sim {\operatorname{clip}{({\mathcal{N}{(0,\sigma)}},{- c},c)}}}.$ | | | Every $d$ iterations, the policy is updated with respect to $Q_{\theta_{1}}$ following the deterministic policy gradient algorithm. TD3 is summarized in Algorithm 1.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments", "weight": 1.0} -->

Initialize critic networks Qθ1, Qθ2, and actor network πϕ with random parameters θ1, θ2, ϕ Initialize target networks θ1′ ← θ1, θ2′ ← θ2, ϕ′ ← ϕ Initialize replay buffer ℬ Select action with exploration noise a ∼ πϕ (s) + ϵ, ϵ ∼ 𝒩 (0, σ) and observe reward r and new state s′ Store transition tuple (s, a, r, s′) in ℬ Sample mini-batch of N transitions (s, a, r, s′) from ℬ ${\overset{\sim}{a}\leftarrow{{\pi_{\phi'}{(s')}} + \epsilon}},{\epsilon \sim {\operatorname{clip}{({\mathcal{N}{(0,\overset{\sim}{\sigma})}},{- c},c)}}}$ $y\leftarrow{r + {\gamma{\min_{i =

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments", "weight": 1.0} -->

{1,2}}Q_{\theta_{i}'}}{(s',\overset{\sim}{a})}}}$ Update critics θi ← argminθiN−1 ∑(y − Qθi (s, a))2 Update ϕ by the deterministic policy gradient: Update target networks: Figure 4: Example MuJoCo environments (a) HalfCheetah-v1, (b) Hopper-v1, (c) Walker2d-v1, (d) Ant-v1.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Evaluation", "weight": 1.0} -->

To evaluate our algorithm, we measure its performance on the suite of MuJoCo continuous control tasks, interfaced through OpenAI Gym (Figure 4). To allow for reproducible comparison, we use the original set of tasks from Brockman et al. with no modifications to the environment or reward.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Evaluation", "weight": 1.0} -->

For our implementation of DDPG, we use a two layer feedforward neural network of 400 and 300 hidden nodes respectively, with rectified linear units (ReLU) between each layer for both the actor and critic, and a final tanh unit following the output of the actor. Unlike the original DDPG, the critic receives both the state and action as input to the first layer. Both network parameters are updated using Adam with a learning rate of $10^{- 3}$. After each time step, the networks are trained with a mini-batch of a 100 transitions, sampled uniformly from a replay buffer containing the entire history of the agent.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Evaluation", "weight": 1.0} -->

The target policy smoothing is implemented by adding $\epsilon \sim {\mathcal{N}{(0,0.2)}}$ to the actions chosen by the target actor network, clipped to $({- 0.5},0.5)$, delayed policy updates consists of only updating the actor and target critic network every $d$ iterations, with $d = 2$. While a larger $d$ would result in a larger benefit with respect to accumulating errors, for fair comparison, the critics are only trained once per time step, and training the actor for too few iterations would cripple learning. Both target networks are updated with $\tau = 0.005$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Evaluation", "weight": 1.0} -->

To remove the dependency on the initial parameters of the policy we use a purely exploratory policy for the first 10000 time steps of stable length environments (HalfCheetah-v1 and Ant-v1) and the first 1000 time steps for the remaining environments. Afterwards, we use an off-policy exploration strategy, adding Gaussian noise $\mathcal{N}{(0,0.1)}$ to each action. Unlike the original implementation of DDPG, we used uncorrelated noise for exploration as we found noise drawn from the Ornstein-Uhlenbeck process offered no performance benefits.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Each task is run for 1 million time steps with evaluations every 5000 time steps, where each evaluation reports the average reward over 10 episodes with no exploration noise. Our results are reported over 10 random seeds of the Gym simulator and the network initialization.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Evaluation", "weight": 1.0} -->

We compare our algorithm against DDPG as well as the state of art policy gradient algorithms: PPO, ACKTR and TRPO, as implemented by OpenAI's baselines repository, and SAC, as implemented by the author's GitHub^11^1See the supplementary material for hyper-parameters and a discussion on the discrepancy in the reported results of SAC.. Additionally, we compare our method with our re-tuned version of DDPG, which includes all architecture and hyper-parameter modifications to DDPG without any of our proposed adjustments. A full comparison between our re-tuned version and the baselines DDPG is provided in the supplementary material.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Our results are presented in Table 1 and learning curves in Figure 5. TD3 matches or outperforms all other algorithms in both final performance and learning speed across all tasks.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

We perform ablation studies to understand the contribution of each individual component: Clipped Double Q-learning (Section 4.2), delayed policy updates (Section 5.2) and target policy smoothing (Section 5.3). We present our results in Table 2 in which we compare the performance of removing each component from TD3 along with our modifications to the architecture and hyper-parameters. Additional learning curves can be found in the supplementary material.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

The significance of each component varies task to task. While the addition of only a single component causes insignificant improvement in most cases, the addition of combinations performs at a much higher level. The full algorithm outperforms every other combination in most tasks. Although the actor is trained for only half the number of iterations, the inclusion of delayed policy update generally improves performance, while reducing training time.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

We additionally compare the effectiveness of the actor-critic variants of Double Q-learning and Double DQN, denoted DQ-AC and DDQN-AC respectively, in Table 2. For fairness in comparison, these methods also benefited from delayed policy updates, target policy smoothing and use our architecture and hyper-parameters. Both methods were shown to reduce overestimation bias less than Clipped Double Q-learning in Section 4. This is reflected empirically, as both methods result in insignificant improvements over TD3 - CDQ, with an exception in the Ant-v1 environment, which appears to benefit greatly from any overestimation reduction. As the inclusion of Clipped Double Q-learning into our full method outperforms both prior methods, this suggests that subduing the overestimations from the unbiased estimator is an effective measure to improve performance.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Overestimation has been identified as a key problem in value-based methods. In this paper, we establish overestimation bias is also problematic in actor-critic methods. We find the common solutions for reducing overestimation bias in deep Q-learning with discrete actions are ineffective in an actor-critic setting, and develop a novel variant of Double Q-learning which limits possible overestimation. Our results demonstrate that mitigating overestimation can greatly improve the performance of modern algorithms.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Due to the connection between noise and overestimation, we examine the accumulation of errors from temporal difference learning. Our work investigates the importance of a standard technique in deep reinforcement learning, target networks, and examines their role in limiting errors from imprecise function approximation and stochastic optimization. Finally, we introduce a SARSA-style regularization technique which modifies the temporal difference target to bootstrap off similar state-action pairs.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Taken together, these improvements define our proposed approach, the Twin Delayed Deep Deterministic policy gradient algorithm (TD3), which greatly improves both the learning speed and performance of DDPG in a number of challenging tasks in the continuous control setting. Our algorithm exceeds the performance of numerous state of the art algorithms. As our modifications are simple to implement, they can be easily added to any other actor-critic algorithm.
