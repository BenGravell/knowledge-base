<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor

Topics include Reinforcement learning, Actor-critic, Maximum entropy reinforcement learning, Off-policy, Continuous control, Deep reinforcement learning, Entropy regularization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes Soft Actor-Critic (SAC), an off-policy actor-critic algorithm that augments the standard RL objective with an entropy term, simultaneously maximizing reward and policy entropy. The resulting algorithm is sample-efficient, stable across random seeds, and avoids the brittle convergence of competing methods.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Model-free deep reinforcement learning (RL) algorithms have been demonstrated on a range of challenging decision making and control tasks. However, these methods typically suffer from two major challenges: very high sample complexity and brittle convergence properties, which necessitate meticulous hyperparameter tuning. Both of these challenges severely limit the applicability of such methods to complex, real-world domains. In this paper, we propose soft actor-critic, an off-policy actor-critic deep RL algorithm based on the maximum entropy reinforcement learning framework. In this framework, the actor aims to maximize expected reward while also maximizing entropy. That is, to succeed at the task while acting as randomly as possible. Prior deep RL methods based on this framework have been formulated as Q-learning methods. By combining off-policy updates with a stable stochastic actor-critic formulation, our method achieves state-of-the-art performance on a range of continuous control benchmark tasks, outperforming prior on-policy and off-policy methods. Furthermore, we demonstrate that, in contrast to other off-policy algorithms, our approach is very stable, achieving very similar performance across different random seeds.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model-free deep reinforcement learning (RL) algorithms have been applied in a range of challenging domains, from games to robotic control. The combination of RL and high-capacity function approximators such as neural networks holds the promise of automating a wide range of decision making and control tasks, but widespread adoption of these methods in real-world domains has been hampered by two major challenges. First, model-free deep RL methods are notoriously expensive in terms of their sample complexity. Even relatively simple tasks can require millions of steps of data collection, and complex behaviors with high-dimensional observations might need substantially more. Second, these methods are often brittle with respect to their hyperparameters: learning rates, exploration constants, and other settings must be set carefully for different problem settings to achieve good results. Both of these challenges severely limit the applicability of model-free deep RL to real-world tasks.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

One cause for the poor sample efficiency of deep RL methods is on-policy learning: some of the most commonly used deep RL algorithms, such as TRPO, PPO or A3C, require new samples to be collected for each gradient step. This quickly becomes extravagantly expensive, as the number of gradient steps and samples per step needed to learn an effective policy increases with task complexity. Off-policy algorithms aim to reuse past experience. This is not directly feasible with conventional policy gradient formulations, but is relatively straightforward for Q-learning based methods. Unfortunately, the combination of off-policy learning and high-dimensional, nonlinear function approximation with neural networks presents a major challenge for stability and convergence. This challenge is further exacerbated in continuous state and action spaces, where a separate actor network is often used to perform the maximization in Q-learning. A commonly used algorithm in such settings, deep deterministic policy gradient (DDPG), provides for sample-efficient learning but is notoriously challenging to use due to its extreme brittleness and hyperparameter sensitivity.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We explore how to design an efficient and stable model-free deep RL algorithm for continuous state and action spaces. To that end, we draw on the maximum entropy framework, which augments the standard maximum reward reinforcement learning objective with an entropy maximization term. Maximum entropy reinforcement learning alters the RL objective, though the original objective can be recovered using a temperature parameter. More importantly, the maximum entropy formulation provides a substantial improvement in exploration and robustness: as discussed by Ziebart, maximum entropy policies are robust in the face of model and estimation errors, and as demonstrated, they improve exploration by acquiring diverse behaviors. Prior work has proposed model-free deep RL algorithms that perform on-policy learning with entropy maximization, as well as off-policy methods based on soft Q-learning and its variants. However, the on-policy variants suffer from poor sample complexity for the reasons discussed above, while the off-policy variants require complex approximate inference procedures in continuous action spaces.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we demonstrate that we can devise an off-policy maximum entropy actor-critic algorithm, which we call soft actor-critic (SAC), which provides for both sample-efficient learning and stability. This algorithm extends readily to very complex, high-dimensional tasks, such as the Humanoid benchmark with 21 action dimensions, where off-policy methods such as DDPG typically struggle to obtain good results. SAC also avoids the complexity and potential instability associated with approximate inference in prior off-policy maximum entropy algorithms based on soft Q-learning. We present a convergence proof for policy iteration in the maximum entropy framework, and then introduce a new algorithm based on an approximation to this procedure that can be practically implemented with deep neural networks, which we call soft actor-critic. We present empirical results that show that soft actor-critic attains a substantial improvement in both performance and sample efficiency over both off-policy and on-policy prior methods. We also compare to twin delayed deep deterministic (TD3) policy gradient algorithm, which is a concurrent work that proposes a deterministic algorithm that substantially improves on DDPG.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Maximum Entropy Reinforcement Learning", "weight": 1.0} -->

The temperature parameter $\alpha$ determines the relative importance of the entropy term against the reward, and thus controls the stochasticity of the optimal policy. The maximum entropy objective differs from the standard maximum expected reward objective used in conventional reinforcement learning, though the conventional objective can be recovered in the limit as $\alpha\rightarrow 0$. For the rest of this paper, we will omit writing the temperature explicitly, as it can always be subsumed into the reward by scaling it by $\alpha^{- 1}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Maximum Entropy Reinforcement Learning", "weight": 1.0} -->

This objective has a number of conceptual and practical advantages. First, the policy is incentivized to explore more widely, while giving up on clearly unpromising avenues. Second, the policy can capture multiple modes of near-optimal behavior. In problem settings where multiple actions seem equally attractive, the policy will commit equal probability mass to those actions. Lastly, prior work has observed improved exploration with this objective, and in our experiments, we observe that it considerably improves learning speed over state-of-art methods that optimize the conventional RL objective function. We can extend the objective to infinite horizon problems by introducing a discount factor $\gamma$ to ensure that the sum of expected rewards and entropies is finite. Writing down the maximum entropy objective for the infinite horizon discounted case is more involved and is deferred to Appendix A.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Maximum Entropy Reinforcement Learning", "weight": 1.0} -->

Prior methods have proposed directly solving for the optimal Q-function, from which the optimal policy can be recovered. We will discuss how we can devise a soft actor-critic algorithm through a policy iteration formulation, where we instead evaluate the Q-function of the current policy and update the policy through an *off-policy* gradient update. Though such algorithms have previously been proposed for conventional reinforcement learning, our method is, to our knowledge, the first off-policy actor-critic method in the maximum entropy reinforcement learning framework.

<!-- chunk {"id": "body-0011", "role": "body", "section": "From Soft Policy Iteration to Soft Actor-Critic", "weight": 1.0} -->

Our off-policy soft actor-critic algorithm can be derived starting from a maximum entropy variant of the policy iteration method. We will first present this derivation, verify that the corresponding algorithm converges to the optimal policy from its density class, and then present a practical deep reinforcement learning algorithm based on this theory.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Derivation of Soft Policy Iteration", "weight": 1.0} -->

We will begin by deriving soft policy iteration, a general algorithm for learning optimal maximum entropy policies that alternates between policy evaluation and policy improvement in the maximum entropy framework. Our derivation is based on a tabular setting, to enable theoretical analysis and convergence guarantees, and we extend this method into the general continuous setting in the next section. We will show that soft policy iteration converges to the optimal policy within a set of policies which might correspond, for instance, to a set of parameterized densities.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Derivation of Soft Policy Iteration", "weight": 1.0} -->

In the policy evaluation step of soft policy iteration, we wish to compute the value of a policy $\pi$ according to the maximum entropy objective in Equation 1. For a fixed policy, the soft Q-value can be computed iteratively, starting from any function $Q:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ and repeatedly applying a modified Bellman backup operator $\mathcal{T}^{\pi}$ given by

<!-- chunk {"id": "body-0014", "role": "body", "section": "Derivation of Soft Policy Iteration", "weight": 1.0} -->

is the soft state value function. We can obtain the soft value function for any policy $\pi$ by repeatedly applying $\mathcal{T}^{\pi}$ as formalized below.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Soft Actor-Critic", "weight": 1.0} -->

As discussed above, large continuous domains require us to derive a practical approximation to soft policy iteration. To that end, we will use function approximators for both the Q-function and the policy, and instead of running evaluation and improvement to convergence, alternate between optimizing both networks with stochastic gradient descent. We will consider a parameterized state value function $V_{\psi}{(\mathbf{s}_{t})}$, soft Q-function $Q_{\theta}{(\mathbf{s}_{t},\mathbf{a}_{t})}$, and a tractable policy $\pi_{\phi}{(\left. \mathbf{a}_{t} \middle| \mathbf{s}_{t} \right.)}$. The parameters of these networks are $\psi,\theta$, and $\phi$. For example, the value functions can be modeled as expressive neural networks, and the policy as a Gaussian with mean and covariance given by neural networks. We will next derive update rules for these parameter vectors.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Soft Actor-Critic", "weight": 1.0} -->

The state value function approximates the soft value. There is no need in principle to include a separate function approximator for the state value, since it is related to the Q-function and policy according to Equation 3. This quantity can be estimated from a single action sample from the current policy without introducing a bias, but in practice, including a separate function approximator for the soft value can stabilize training and is convenient to train simultaneously with the other networks. The soft value function is trained to minimize the squared residual error

<!-- chunk {"id": "body-0017", "role": "body", "section": "Soft Actor-Critic", "weight": 1.0} -->

where $\mathcal{D}$ is the distribution of previously sampled states and actions, or a replay buffer. The gradient of Equation 5 can be estimated with an unbiased estimator

<!-- chunk {"id": "body-0018", "role": "body", "section": "Soft Actor-Critic", "weight": 1.0} -->

where the actions are sampled according to the current policy, instead of the replay buffer. The soft Q-function parameters can be trained to minimize the soft Bellman residual

<!-- chunk {"id": "body-0019", "role": "body", "section": "Soft Actor-Critic", "weight": 1.0} -->

which again can be optimized with stochastic gradients

<!-- chunk {"id": "body-0020", "role": "body", "section": "Soft Actor-Critic", "weight": 1.0} -->

The update makes use of a target value network $V_{\overline{\psi}}$, where $\overline{\psi}$ can be an exponentially moving average of the value network weights, which has been shown to stabilize training. Alternatively, we can update the target weights to match the current value function weights periodically (see Appendix E).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Soft Actor-Critic", "weight": 1.0} -->

There are several options for minimizing $J_{\pi}$. A typical solution for policy gradient methods is to use the likelihood ratio gradient estimator, which does not require backpropagating the gradient through the policy and the target density networks. However, in our case, the target density is the Q-function, which is represented by a neural network an can be differentiated, and it is thus convenient to apply the reparameterization trick instead, resulting in a lower variance estimator. To that end, we reparameterize the policy using a neural network transformation

<!-- chunk {"id": "body-0022", "role": "body", "section": "Soft Actor-Critic", "weight": 1.0} -->

where $\epsilon_{t}$ is an input noise vector, sampled from some fixed distribution, such as a spherical Gaussian. We can now rewrite the objective in Equation 10 as

<!-- chunk {"id": "body-0023", "role": "body", "section": "Soft Actor-Critic", "weight": 1.0} -->

where $\pi_{\phi}$ is defined implicitly in terms of $f_{\phi}$, and we have noted that the partition function is independent of $\phi$ and can thus be omitted. We can approximate the gradient of Equation 12 with

<!-- chunk {"id": "body-0024", "role": "body", "section": "Soft Actor-Critic", "weight": 1.0} -->

where $\mathbf{a}_{t}$ is evaluated at $f_{\phi}{(\epsilon_{t};\mathbf{s}_{t})}$. This unbiased gradient estimator extends the DDPG style policy gradients to any tractable stochastic policy.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Soft Actor-Critic", "weight": 1.0} -->

Our algorithm also makes use of two Q-functions to mitigate positive bias in the policy improvement step that is known to degrade performance of value based methods. In particular, we parameterize two Q-functions, with parameters $\theta_{i}$, and train them independently to optimize $J_{Q}{(\theta_{i})}$. We then use the minimum of the Q-functions for the value gradient in Equation 6 and policy gradient in Equation 13, as proposed by Fujimoto et al.. Although our algorithm can learn challenging tasks, including a 21-dimensional Humanoid, using just a single Q-function, we found two Q-functions significantly speed up training, especially on harder tasks. The complete algorithm is described in Algorithm 1. The method alternates between collecting experience from the environment with the current policy and updating the function approximators using the stochastic gradients from batches sampled from a replay buffer. In practice, we take a single environment step followed by one or several gradient steps (see Appendix D for all hyperparameter).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Soft Actor-Critic", "weight": 1.0} -->

Using off-policy data from a replay buffer is feasible because both value estimators and the policy can be trained entirely on off-policy data. The algorithm is agnostic to the parameterization of the policy, as long as it can be evaluated for any arbitrary state-action tuple.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experiments", "weight": 1.0} -->

The goal of our experimental evaluation is to understand how the sample complexity and stability of our method compares with prior off-policy and on-policy deep reinforcement learning algorithms. We compare our method to prior techniques on a range of challenging continuous control tasks from the OpenAI gym benchmark suite and also on the rllab implementation of the Humanoid task. Although the easier tasks can be solved by a wide range of different algorithms, the more complex benchmarks, such as the 21-dimensional Humanoid (rllab), are exceptionally difficult to solve with off-policy algorithms. The stability of the algorithm also plays a large role in performance: easier tasks make it more practical to tune hyperparameters to achieve good results, while the already narrow basins of effective hyperparameters become prohibitively small for the more sensitive algorithms on the hardest benchmarks, leading to poor performance.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experiments", "weight": 1.0} -->

We compare our method to deep deterministic policy gradient (DDPG), an algorithm that is regarded as one of the more efficient off-policy deep RL methods; proximal policy optimization (PPO), a stable and effective on-policy policy gradient algorithm; and soft Q-learning (SQL), a recent off-policy algorithm for learning maximum entropy policies. Our SQL implementation also includes two Q-functions, which we found to improve its performance in most environments. We additionally compare to twin delayed deep deterministic policy gradient algorithm (TD3), using the author-provided implementation. This is an extension to DDPG, proposed concurrently to our method, that first applied the double Q-learning trick to continuous control along with other improvements. We have included trust region path consistency learning (Trust-PCL) and two other variants of SAC in Appendix E. We turned off the exploration noise for evaluation for DDPG and PPO. For maximum entropy algorithms, which do not explicitly inject exploration noise, we either evaluated with the exploration noise (SQL) or use the mean action (SAC).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments", "weight": 1.0} -->

The source code of our SAC implementation^11^1github.com/haarnoja/sac and videos^22^2[sites.google.com/view/soft-actor-critic](sites.google.com/view/soft-actor-critic) are available online.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Comparative Evaluation", "weight": 1.0} -->

The results show that, overall, SAC performs comparably to the baseline methods on the easier tasks and outperforms them on the harder tasks with a large margin, both in terms of learning speed and the final performance. For example, DDPG fails to make any progress on Ant-v1, Humanoid-v1, and Humanoid (rllab), a result that is corroborated by prior work. SAC also learns considerably faster than PPO as a consequence of the large batch sizes PPO needs to learn stably on more high-dimensional and complex tasks. Another maximum entropy RL algorithm, SQL, can also learn all tasks, but it is slower than SAC and has worse asymptotic performance. The quantitative results attained by SAC in our experiments also compare very favorably to results reported by other methods in prior work, indicating that both the sample efficiency and final performance of SAC on these benchmark tasks exceeds the state of the art. All hyperparameters used in this experiment for SAC are listed in Appendix D.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

The results in the previous section suggest that algorithms based on the maximum entropy principle can outperform conventional RL methods on challenging tasks such as the humanoid tasks. In this section, we further examine which particular components of SAC are important for good performance. We also examine how sensitive SAC is to some of the most important hyperparameters, namely reward scaling and target value update smoothing constant.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Stochastic vs. deterministic policy", "weight": 1.0} -->

Soft actor-critic learns stochastic policies via a maximum entropy objective. The entropy appears in both the policy and value function. In the policy, it prevents premature convergence of the policy variance (Equation 10). In the value function, it encourages exploration by increasing the value of regions of state space that lead to high-entropy behavior (Equation 5). To compare how the stochasticity of the policy and entropy maximization affects the performance, we compare to a deterministic variant of SAC that does not maximize the entropy and that closely resembles DDPG, with the exception of having two Q-functions, using hard target updates, not having a separate target actor, and using fixed rather than learned exploration noise. Figure 2 compares five individual runs with both variants, initialized with different random seeds. Soft actor-critic performs much more consistently, while the deterministic variant exhibits very high variability across seeds, indicating substantially worse stability. As evident from the figure, learning a stochastic policy with entropy maximization can drastically stabilize training. This becomes especially important with harder tasks, where tuning hyperparameters is challenging.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Stochastic vs. deterministic policy", "weight": 1.0} -->

In this comparison, we updated the target value network weights with hard updates, by periodically overwriting the target network parameters to match the current value network (see Appendix E for a comparison of average performance on all benchmark tasks).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Policy evaluation", "weight": 1.0} -->

Since SAC converges to stochastic policies, it is often beneficial to make the final policy deterministic at the end for best performance. For evaluation, we approximate the maximum a posteriori action by choosing the mean of the policy distribution. Figure 3(a) ‣ Figure 3 ‣ Stochastic vs. deterministic policy. ‣ 5.2 Ablation Study ‣ 5 Experiments ‣ Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor") compares training returns to evaluation returns obtained with this strategy indicating that deterministic evaluation can yield better performance. It should be noted that all of the training curves depict the sum of rewards, which is different from the objective optimized by SAC and other maximum entropy RL algorithms, including SQL and Trust-PCL, which maximize also the entropy of the policy.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Reward scale", "weight": 1.0} -->

Soft actor-critic is particularly sensitive to the scaling of the reward signal, because it serves the role of the temperature of the energy-based optimal policy and thus controls its stochasticity. Larger reward magnitudes correspond to lower entries. Figure 3(b) ‣ Figure 3 ‣ Stochastic vs. deterministic policy. ‣ 5.2 Ablation Study ‣ 5 Experiments ‣ Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor") shows how learning performance changes when the reward scale is varied: For small reward magnitudes, the policy becomes nearly uniform, and consequently fails to exploit the reward signal, resulting in substantial degradation of performance. For large reward magnitudes, the model learns quickly at first, but the policy then becomes nearly deterministic, leading to poor local minima due to lack of adequate exploration. With the right reward scaling, the model balances exploration and exploitation, leading to faster learning and better asymptotic performance. In practice, we found reward scale to be the only hyperparameter that requires tuning, and its natural interpretation as the inverse of the temperature in the maximum entropy framework provides good intuition for how to adjust this parameter.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Target network update", "weight": 1.0} -->

It is common to use a separate target value network that slowly tracks the actual value function to improve stability. We use an exponentially moving average, with a smoothing constant $\tau$, to update the target value network weights as common in the prior work. A value of one corresponds to a hard update where the weights are copied directly at every iteration and zero to not updating the target at all. In Figure 3(c) ‣ Figure 3 ‣ Stochastic vs. deterministic policy. ‣ 5.2 Ablation Study ‣ 5 Experiments ‣ Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor"), we compare the performance of SAC when $\tau$ varies. Large $\tau$ can lead to instabilities while small $\tau$ can make training slower. However, we found the range of suitable values of $\tau$ to be relatively wide and we used the same value (0.005) across all of the tasks. In Figure 4 (Appendix E) we also compare to another variant of SAC, where instead of using exponentially moving average, we copy over the current network weights directly into the target network every 1000 gradient steps.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Target network update", "weight": 1.0} -->

We found this variant to benefit from taking more than one gradient step between the environment steps, which can improve performance but also increases the computational cost.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We present soft actor-critic (SAC), an off-policy maximum entropy deep reinforcement learning algorithm that provides sample-efficient learning while retaining the benefits of entropy maximization and stability. Our theoretical results derive soft policy iteration, which we show to converge to the optimal policy. From this result, we can formulate a soft actor-critic algorithm, and we empirically show that it outperforms state-of-the-art model-free deep RL methods, including the off-policy DDPG algorithm and the on-policy PPO algorithm. In fact, the sample efficiency of this approach actually exceeds that of DDPG by a substantial margin. Our results suggest that stochastic, entropy maximizing reinforcement learning algorithms can provide a promising avenue for improved robustness and stability, and further exploration of maximum entropy methods, including methods that incorporate second order information (e.g., trust regions ) or more expressive policy classes is an exciting avenue for future work.
