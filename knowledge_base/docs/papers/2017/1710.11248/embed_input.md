<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Robust Rewards with Adversarial Inverse Reinforcement Learning

Topics include Reinforcement learning, Inverse reinforcement learning, Robustness, Control, Learning, AIRL, Adversarial inverse reinforcement learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Reinforcement learning provides a powerful and general framework for decision making and control, but its application in practice is often hindered by the need for extensive feature and reward engineering. Deep reinforcement learning methods can remove the need for explicit engineering of policy or value features, but still require a manually specified reward function. Inverse reinforcement learning holds the promise of automatic reward acquisition, but has proven exceptionally difficult to apply to large, high-dimensional problems with unknown dynamics. In this work, we propose adverserial inverse reinforcement learning (AIRL), a practical and scalable inverse reinforcement learning algorithm based on an adversarial reward learning formulation. We demonstrate that AIRL is able to recover reward functions that are robust to changes in dynamics, enabling us to learn policies even under significant variation in the environment seen during training. Our experiments show that AIRL greatly outperforms prior methods in these transfer settings.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

While reinforcement learning (RL) provides a powerful framework for automating decision making and control, significant engineering of elements such as features and reward functions has typically been required for good practical performance. In recent years, deep reinforcement learning has alleviated the need for feature engineering for policies and value functions, and has shown promising results on a range of complex tasks, from vision-based robotic control to video games such as Atari and Minecraft. However, reward engineering remains a significant barrier to applying reinforcement learning in practice. In some domains, this may be difficult to specify (for example, encouraging "socially acceptable" behavior), and in others, a naïvely specified reward function can produce unintended behavior. Moreover, deep RL algorithms are often sensitive to factors such as reward sparsity and magnitude, making well performing reward functions particularly difficult to engineer.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inverse reinforcement learning (IRL) refers to the problem of inferring an expert's reward function from demonstrations, which is a potential method for solving the problem of reward engineering. However, inverse reinforcement learning methods have generally been less efficient than direct methods for learning from demonstration such as imitation learning, and methods using powerful function approximators such as neural networks have required tricks such as domain-specific regularization and operate inefficiently over whole trajectories. There are many scenarios where IRL may be preferred over direct imitation learning, such as re-optimizing a reward in novel environments or to infer an agent's intentions, but IRL methods have not been shown to scale to the same complexity of tasks as direct imitation learning. However, adversarial IRL methods hold promise for tackling difficult tasks due to the ability to adapt training samples to improve learning efficiency.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Part of the challenge is that IRL is an ill-defined problem, since there are many optimal policies that can explain a set of demonstrations, and many rewards that can explain an optimal policy. The maximum entropy (MaxEnt) IRL framework introduced by Ziebart et al. handles the former ambiguity, but the latter ambiguity means that IRL algorithms have difficulty distinguishing the true reward functions from those shaped by the environment dynamics. While shaped rewards can increase learning speed in the original training environment, when the reward is deployed at test-time on environments with varying dynamics, it may no longer produce optimal behavior, as we discuss in Sec. 5. To address this issue, we discuss how to modify IRL algorithms to learn rewards that are invariant to changing dynamics, which we refer to as disentangled rewards.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose adversarial inverse reinforcement learning (AIRL), an inverse reinforcement learning algorithm based on adversarial learning. Our algorithm provides for simultaneous learning of the reward function and value function, which enables us to both make use of the efficient adversarial formulation and recover a generalizable and portable reward function, in contrast to prior works that either do not recover a reward functions, or operates at the level of entire trajectories, making it difficult to apply to more complex problem settings. Our experimental evaluation demonstrates that AIRL outperforms prior IRL methods on continuous, high-dimensional tasks with unknown dynamics by a wide margin. When compared to GAIL, which does not attempt to directly recover rewards, our method achieves comparable results on tasks that do not require transfer. However, on tasks where there is considerable variability in the environment from the demonstration setting, GAIL and other IRL methods fail to generalize. In these settings, our approach, which can effectively disentangle the goals of the expert from the dynamics of the environment, achieves superior results.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Adversarial Inverse Reinforcement Learning (AIRL)", "weight": 1.0} -->

In practice, using full trajectories as proposed by GAN-GCL can result in high variance estimates as compared to using single state, action pairs, and our experimental results show that this results in very poor learning. We could instead propose a straightforward conversion of Eqn. 2 into the single state and action case, where: As in the trajectory-centric case, we can show that, at optimality, ${f^{\ast}{(s,a)}} = {{\log\pi^{\ast}}{(\left. a \middle| s \right.)}} = {A^{\ast}{(s,a)}}$, the advantage function of the optimal policy. We justify this, as well as a proof that this algorithm solves the IRL problem in Appendix A.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Adversarial Inverse Reinforcement Learning (AIRL)", "weight": 1.0} -->

This change results in an efficient algorithm for imitation learning. However, it is less desirable for the purpose of reward learning. While the advantage is a valid optimal reward function, it is a heavily entangled reward, as it supervises each action based on the action of the optimal policy for the training MDP. Based on the analysis in the following Sec. 5, we cannot guarantee that this reward will be robust to changes in environment dynamics. In our experiments we demonstrate several cases where this reward simply encourages mimicking the expert policy $\pi^{\ast}$, and fails to produce desirable behavior even when changes to the environment are made.

<!-- chunk {"id": "body-0009", "role": "body", "section": "The Reward Ambiguity Problem", "weight": 1.0} -->

We now discuss why IRL methods can fail to learn robust reward functions. First, we review the concept of reward shaping. Ng et al. describe a class of reward transformations that preserve the optimal policy. Their main theoretical result is that under the following reward transformation, the optimal policy remains unchanged, for any function $\Phi:{\mathcal{S}\rightarrow{\mathbb{R}}}$. Moreover, without prior knowledge of the dynamics, this is the only class of reward transformations that exhibits policy invariance. Because IRL methods only infer rewards from demonstrations given from an optimal agent, they cannot in general disambiguate between reward functions within this class of transformations, unless the class of learnable reward functions is restricted.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The Reward Ambiguity Problem", "weight": 1.0} -->

We argue that shaped reward functions may not be robust to changes in dynamics. We formalize this notion by studying policy invariance in two MDPs $M,M'$ which share the same reward and differ only in the dynamics, denoted as $T$ and $T'$, respectively.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The Reward Ambiguity Problem", "weight": 1.0} -->

Suppose an IRL algorithm recovers a shaped, policy invariant reward $\hat{r}{(s,a,s')}$ under MDP $M$ where $\Phi \neq 0$. Then, there exists MDP pairs $M,M'$ where changing the transition model from $T$ to $T'$ breaks policy invariance on MDP $M'$. As a simple example, consider deterministic dynamics ${T{(s,a)}}\rightarrow s'$ and state-action rewards ${\hat{r}{(s,a)}} = {{{r{(s,a)}} + {\gamma\Phi{({T{(s,a)}})}}} - {\Phi{(s)}}}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "The Reward Ambiguity Problem", "weight": 1.0} -->

It is easy to see that changing the dynamics $T$ to $T'$ such that ${T'{(s,a)}} \neq {T{(s,a)}}$ means that $\hat{r}{(s,a)}$ no longer lies in the equivalence class of Eqn. 3 for $M'$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Disentangling Rewards from Dynamics", "weight": 1.0} -->

First, let the notation $Q_{r,T}^{\ast}{(s,a)}$ denote the optimal Q-function with respect to a reward function $r$ and dynamics $T$, and $\pi_{r,T}^{\ast}{(\left. a \middle| s \right.)}$ denote the same for policies. We first define our notion of a "disentangled" reward.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Learning Disentangled Rewards with AIRL", "weight": 1.0} -->

In the method presented in Section 4 ‣ Learning Robust Rewards with Adversarial Inverse Reinforcement Learning"), we cannot learn a state-only reward function, $r_{\theta}{(s)}$, meaning that we cannot guarantee that learned rewards will not be shaped. In order to decouple the reward function from the advantage, we propose to modify the discriminator of Sec. 4 ‣ Learning Robust Rewards with Adversarial Inverse Reinforcement Learning") with the form: where $f_{\theta,\phi}$ is restricted to a reward approximator $g_{\theta}$ and a shaping term $h_{\phi}$ as The additional shaping term helps mitigate the effects of unwanted shaping on our reward approximator $g_{\theta}$ (and as we will show, in some cases it can account for all shaping effects). The entire training procedure is detailed in Algorithm 1. Our algorithm resembles GAIL and GAN-GCL, where we alternate between training a discriminator to classify expert data from policy samples, and update the policy to confuse the discriminator.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Learning Disentangled Rewards with AIRL", "weight": 1.0} -->

1: Obtain expert trajectories τiE 2: Initialize policy π and discriminator Dθ, ϕ. 4: Collect trajectories τi = (s0, a0, …, sT, aT) by executing π. 5: Train Dθ, ϕ via binary logistic regression to classify expert data τiE from samples τi. 6: Update reward rθ, ϕ (s, a, s′) ← log Dθ, ϕ (s, a, s′) − log (1 − Dθ, ϕ (s, a, s′)) 7: Update π with respect to rθ, ϕ using any policy optimization method. Algorithm 1 Adversarial inverse reinforcement learning The advantage of this approach is that we can now parametrize $g_{\theta}{(s)}$ as solely a function of the state, allowing us to extract rewards that are disentangled from the dynamics of the environment in which they were trained. In fact, under this restricted case, we can show the following under deterministic environments with a state-only ground truth reward (proof in Appendix C): where $r^{\ast}$ is the true reward function.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Learning Disentangled Rewards with AIRL", "weight": 1.0} -->

Since $f^{\ast}$ must recover to the advantage as shown in Sec. 4 ‣ Learning Robust Rewards with Adversarial Inverse Reinforcement Learning"), $h$ recovers the optimal value function $V^{\ast}$, which serves as the reward shaping term.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Learning Disentangled Rewards with AIRL", "weight": 1.0} -->

To be consistent with Sec. 4 ‣ Learning Robust Rewards with Adversarial Inverse Reinforcement Learning"), an alternative way to interpret the form of Eqn. 4 is to view $f_{\theta,\phi}$ as the advantage under deterministic dynamics In stochastic environments, we can instead view $f{(s,a,s')}$ as a single-sample estimate of $A^{\ast}{(s,a)}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Experiments", "weight": 1.0} -->

In our experiments, we aim to answer two questions: Can AIRL learn disentangled rewards that are robust to changes in environment dynamics?

<!-- chunk {"id": "body-0019", "role": "body", "section": "Experiments", "weight": 1.0} -->

Is AIRL efficient and scalable to high-dimensional continuous control tasks?

<!-- chunk {"id": "body-0020", "role": "body", "section": "Experiments", "weight": 1.0} -->

To answer 1, we evaluate AIRL in transfer learning scenarios, where a reward is learned in a training environment, and optimized in a test environment with significantly different dynamics. We show that rewards learned with our algorithm under the constraint presented in Section 5 still produce optimal or near-optimal behavior, while naïve methods that do not consider reward shaping fail. We also show that in small MDPs, we can recover the exact ground truth reward function.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Experiments", "weight": 1.0} -->

To answer 2, we compare AIRL as an imitation learning algorithm against GAIL and the GAN-based GCL algorithm proposed by Finn et al., which we refer to as GAN-GCL, on standard benchmark tasks that do not evaluate transfer. Note that Finn et al. does not implement or evaluate GAN-GCL and, to our knowledge, we present the first empirical evaluation of this algorithm. We find that AIRL performs on par with GAIL in a traditional imitation learning setup while vastly outperforming it in transfer learning setups, and outperforms GAN-GCL in both settings. It is worth noting that, except, our method is the only IRL algorithm that we are aware of that scales to high dimensional tasks with unknown dynamics, and although GAIL resembles an IRL algorithm in structure, it does not recover disentangled reward functions, making it unable to re-optimize the learned reward under changes in the environment, as we illustrate below.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Experiments", "weight": 1.0} -->

For our continuous control tasks, we use trust region policy optimization as our policy optimization algorithm across all evaluated methods, and in the tabular MDP task, we use soft value iteration. We obtain expert demonstrations by training an expert policy on the ground truth reward, but hide the ground truth reward from the IRL algorithm. In this way, we simulate a scenario where we wish to use RL to solve a task but wish to refrain from manual reward engineering and instead seek to learn a reward function from demonstrations. Our code and additional supplementary material including videos will be available at and hyper-parameter and architecture choices are detailed in Appendix D.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Recovering true rewards in tabular MDPs", "weight": 1.0} -->

We first consider MaxEnt IRL in a toy task with randomly generated MDPs. The MDPs have 16 states, 4 actions, randomly drawn transition matrices, and a reward function that always gives a reward of $1.0$ when taking an action from state 0. The initial state is always state 1.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Recovering true rewards in tabular MDPs", "weight": 1.0} -->

The optimal reward, learned reward with a state-only reward function, and learned reward using a state-action reward function are shown in Fig. 2. We subtract a constant offset from all reward functions so that they share the same mean for visualization - this does not influence the optimal policy. AIRL with a state-only reward function is able to recover the ground truth reward, but AIRL with a state-action reward instead recovers a shaped advantage function.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Recovering true rewards in tabular MDPs", "weight": 1.0} -->

We also show that in the transfer learning setup, under a new transition matrix $T'$, the optimal policy under the state-only reward achieves optimal performance (it is identical to the ground truth reward) whereas the state-action reward only improves marginally over uniform random policy. The learning curve for this experiment is shown in Fig 2.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Disentangling Rewards in Continuous Control Tasks", "weight": 1.0} -->

To evaluate whether our method can learn disentangled rewards in higher dimensional environments, we perform transfer learning experiments on continuous control tasks. In each task, a reward is learned via IRL on the training environment, and the reward is used to reoptimize a new policy on a test environment. We train two IRL algorithms, AIRL and GAN-GCL, with state-only and state-action rewards. We also include results for directly transferring the policy learned with GAIL, and an oracle result that involves optimizing the ground truth reward function with TRPO. Numerical results for these environment transfer experiments are given in Table 1.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Disentangling Rewards in Continuous Control Tasks", "weight": 1.0} -->

The first task involves a 2D point mass navigating to a goal position in a small maze when the position of the walls are changed between train and test time. At test time, the agent cannot simply mimic the actions learned during training, and instead must successfully infer that the goal in the maze is to reach the target. The task is shown in Fig. 4. Only AIRL trained with state-only rewards is able to consistently navigate to the goal when the maze is modified. Direct policy transfer and state-action IRL methods learn rewards which encourage the agent to take the same path taken in the training environment, which is blocked in the test environment. We plot the learned reward in Fig. 4.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Disentangling Rewards in Continuous Control Tasks", "weight": 1.0} -->

In our second task, we modify the agent itself. We train a quadrupedal "ant" agent to run forwards, and at test time we disable and shrink two of the front legs of the ant such that it must significantly change its gait.We find that AIRL is able to learn reward functions that encourage the ant to move forwards, acquiring a modified gait that involves orienting itself to face the forward direction and crawling with its two hind legs. Alternative methods, including transferring a policy learned by GAIL (which achieves near-optimal performance with the unmodified agent), fail to move forward at all. We show the qualitative difference in behavior in Fig. 5.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Disentangling Rewards in Continuous Control Tasks", "weight": 1.0} -->

We have demonstrated that AIRL can learn disentangled rewards that can accommodate significant domain shift even in high-dimensional environments where it is difficult to exactly extract the true reward. GAN-GCL can presumably learn disentangled rewards, but we find that the trajectory-centric formulation does not perform well even in learning rewards in the original task, let alone transferring to a new domain. GAIL learns successfully in the training domain, but does not acquire a representation that is suitable for transfer to test domains.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Disentangling Rewards in Continuous Control Tasks", "weight": 1.0} -->

GAIL, policy transfer \hdashlineTRPO, ground truth Table 1: Results on transfer learning tasks. Mean scores (higher is better) are reported over 5 runs. We also include results for TRPO optimizing the ground truth reward, and the performance of a policy learned via GAIL on the training environment.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Benchmark Tasks for Imitation Learning", "weight": 1.0} -->

Finally, we evaluate AIRL as an imitation learning algorithm against the GAN-GCL and the state-of-the-art GAIL on several benchmark tasks. Each algorithm is presented with 50 expert demonstrations, collected from a policy trained with TRPO on the ground truth reward function. For AIRL, we use an unrestricted state-action reward function as we are not concerned with reward transfer. Numerical results are presented in Table 2.These experiments do not test transfer, and in a sense can be regarded as "testing on the training set," but they match the settings reported in prior work.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Benchmark Tasks for Imitation Learning", "weight": 1.0} -->

We find that the performance difference between AIRL and GAIL is negligible, even though AIRL is a true IRL algorithm that recovers reward functions, while GAIL does not. Both methods achieve close to the best possible result on each task, and there is little room for improvement. This result goes against the belief that IRL algorithms are indirect, and less efficient that direct imitation learning algorithms. The GAN-GCL method is ineffective on all but the simplest Pendulum task when trained with the same number of samples as AIRL and GAIL. We find that a discriminator trained over trajectories easily overfits and provides poor learning signal for the policy.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Benchmark Tasks for Imitation Learning", "weight": 1.0} -->

Our results illustrate that AIRL achieves the same performance as GAIL on benchmark imitation tasks that do not require any generalization. On tasks that require transfer and generalization, illustrated in the previous section, AIRL outperforms GAIL by a wide margin, since our method is able to recover disentangled rewards that transfer effectively in the presence of domain shift.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Benchmark Tasks for Imitation Learning", "weight": 1.0} -->

\hdashlineAIRL State Only (ours) Table 2: Results on imitation learning benchmark tasks. Mean scores (higher is better) are reported across 5 runs.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented AIRL, a practical and scalable IRL algorithm that can learn disentangled rewards and greatly outperforms both prior imitation learning and IRL algorithms. We show that rewards learned with AIRL transfer effectively under variation in the underlying domain, in contrast to unmodified IRL methods which tend to recover brittle rewards that do not generalize well and GAIL, which does not recover reward functions at all. In small MDPs where the optimal policy and reward are unambiguous, we also show that we can exactly recover the ground-truth rewards up to a constant.
