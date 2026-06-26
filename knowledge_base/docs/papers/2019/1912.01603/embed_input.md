<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Dream to Control: Learning Behaviors by Latent Imagination

Topics include World models, Deep learning, Reinforcement learning, Latent, Imagination, Complex behaviors.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Build on the predecessor work PlaNet and learns an actor-critic model in place of online planning with the cross entropy method.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Learned world models summarize an agent's experience to facilitate learning complex behaviors. While learning world models from high-dimensional sensory inputs is becoming feasible through deep learning, there are many potential ways for deriving behaviors from them. We present Dreamer, a reinforcement learning agent that solves long-horizon tasks from images purely by latent imagination. We efficiently learn behaviors by propagating analytic gradients of learned state values back through trajectories imagined in the compact state space of a learned world model. On 20 challenging visual control tasks, Dreamer exceeds existing approaches in data-efficiency, computation time, and final performance.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Intelligent agents can achieve goals in complex environments even though they never encounter the exact same situation twice. This ability requires building representations of the world from past experience that enable generalization to novel situations. World models offer an explicit way to represent an agent's knowledge about the world in a parametric model that can make predictions about the future.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

When the sensory inputs are high-dimensional images, latent dynamics models can abstract observations to predict forward in compact state spaces. Compared to predictions in image space, latent states have a small memory footprint that enables imagining thousands of trajectories in parallel. Learning effective latent dynamics models is becoming feasible through advances in deep learning and latent variable models.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Behaviors can be derived from dynamics models in many ways. Often, imagined rewards are maximized with a parametric policy or by online planning. However, considering only rewards within a fixed imagination horizon results in shortsighted behaviors. Moreover, prior work commonly resorts to derivative-free optimization for robustness to model errors, rather than leveraging analytic gradients offered by neural network dynamics.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present Dreamer, an agent that learns long-horizon behaviors from images purely by latent imagination. A novel actor critic algorithm accounts for rewards beyond the imagination horizon while making efficient use of the neural network dynamics. For this, we predict state values and actions in the learned latent space as summarized in Figure 1. The values optimize Bellman consistency for imagined rewards and the policy maximizes the values by propagating their analytic gradients back through the dynamics.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In comparison to actor critic algorithms that learn online or by experience replay, world models can interpolate past experience and offer analytic gradients of multi-step returns for efficient policy optimization.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The key contributions of this paper are summarized as follows: Learning long-horizon behaviors by latent imagination Model-based agents can be shortsighted if they use a finite imagination horizon. We approach this limitation by predicting both actions and state values. Training purely by imagination in a latent space lets us efficiently learn the policy by propagating analytic value gradients back through the latent dynamics.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Empirical performance for visual control We pair Dreamer with existing representation learning methods and evaluate it on the DeepMind Control Suite with image inputs, illustrated in Figure 2. Using the same hyper parameters for all tasks, Dreamer exceeds previous model-based and model-free agents in terms of data-efficiency, computation time, and final performance.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Reinforcement learning", "weight": 1.0} -->

We formulate visual control as a partially observable Markov decision process (POMDP) with discrete time step $t \in {\lbrack 1;T\rbrack}$, continuous vector-valued actions $a_{t} \sim {p{({a_{t}{}_{}},a_{< t})}}$ generated by the agent, and high-dimensional observations and scalar rewards ${o_{t},r_{t}} \sim {p{(o_{t},{r_{t}{}_{< t}},a_{< t})}}$ generated by the unknown environment. The goal is to develop an agent that maximizes the expected sum of rewards $E_{p}\left( {\sum_{t = 1}^{T}r_{t}} \right)$. Figure 2 shows a selection of our tasks.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Agent components", "weight": 1.0} -->

The classical components of agents that learn in imagination are dynamics learning, behavior learning, and environment interaction. In the case of Dreamer, the behavior is learned by predicting hypothetical trajectories in the compact latent space of the world model. As outlined in Figure 3 and detailed in Algorithm 1, Dreamer performs the following operations throughout the agent's life time, either interleaved or in parallel: Learning the latent dynamics model from the dataset of past experience to predict future rewards from actions and past observations. Any learning objective for the world model can be incorporated with Dreamer. We review existing methods for learning latent dynamics in Section 4.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Agent components", "weight": 1.0} -->

Learning action and value models from predicted latent trajectories, as described in Section 3. The value model optimizes Bellman consistency for imagined rewards and the action model is updated by propagating gradients of value estimates back through the neural network dynamics.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Agent components", "weight": 1.0} -->

Executing the learned action model in the world to collect new experience for growing the dataset.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Latent dynamics", "weight": 1.0} -->

Dreamer uses a latent dynamics model that consists of three components. The representation model encodes observations and actions to create continuous vector-valued model states $s_{t}$ with Markovian transitions. The transition model predicts future model states without seeing the corresponding observations that will later cause them. The reward model predicts the rewards given the model states, We use $p$ for distributions that generate samples in the real environment and $q$ for their approximations that enable latent imagination. Specifically, the transition model lets us predict ahead in the compact latent space without having to observe or imagine the corresponding images. This results in a low memory footprint and fast predictions of thousands of imagined trajectories in parallel.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Latent dynamics", "weight": 1.0} -->

The model mimics a non-linear Kalman filter, latent state space model, or HMM with real-valued states. However, it is conditioned on actions and predicts rewards, allowing the agent to imagine the outcomes of potential action sequences without executing them in the environment.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Learning Behaviors by Latent Imagination", "weight": 1.0} -->

(a) Learn dynamics from experience (b) Learn behavior in imagination (c) Act in the environment Figure 3: Components of Dreamer. (a) From the dataset of past experience, the agent learns to encode observations and actions into compact latent states, for example via reconstruction, and predicts environment rewards. (b) In the compact latent space, Dreamer predicts state values and actions that maximize future value predictions by propagating gradients back through imagined trajectories. (c) The agent encodes the history of the episode to compute the current model state and predict the next action to execute in the environment. See Algorithm 1 for pseudo code of the agent.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Learning Behaviors by Latent Imagination", "weight": 1.0} -->

Initialize dataset 𝒟 with S random seed episodes.; Initialize neural network parameters θ, ϕ, ψ randomly.; while not converged do for update step c = 1..C do Draw B data sequences {(, ot, rt)}t = kk + L ∼ 𝒟.; Compute model states st ∼ pθ (st t − 1, at − 1, ot).; Update θ using representation learning.; Imagine trajectories {(sτ, aτ)}τ = tt + H from each st.; Predict rewards E(qθ (rτ τ)) and values vψ (sτ).; Compute value estimates Vλ (sτ) via Equation 6.; Update $\phi\leftarrow{\phi + {\alpha\nabla_{\phi}{\sum_{\tau = t}^{t + H}{V_{\lambda}{(s_{\tau})}}}}}$.; Update $\psi\leftarrow{\psi - {\alpha\nabla_{\psi}{\sum_{\tau = t}^{t +

<!-- chunk {"id": "body-0019", "role": "body", "section": "Learning Behaviors by Latent Imagination", "weight": 1.0} -->

for time step t = 1..T do Compute st ∼ pθ (st t − 1, at − 1, ot) from history.; Compute at ∼ qϕ (at t) with the action model.; Add exploration noise to action.; Add experience to dataset 𝒟 ← 𝒟 ∪ {(ot rt)t = 1T}.; Model components Representation pθ (st t - 1, at - 1, ot) Transition qθ (st t - 1, at - 1) Reward qθ (rt t) Action qϕ (at t) Value vψ (st) Hyper parameters Seed episodes S Collect interval C Batch size B Sequence length L Imagination horizon H Learning rate α Figure 4: Imagination horizons. We compare the final performance of Dreamer, learning an action model without value prediction, and online planning using PlaNet. Learning a state value model to estimate rewards beyond the imagination horizon makes Dreamer more robust to the horizon length. The agents use pixel reconstruction for representation learning and an action repeat of R = 2.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Learning Behaviors by Latent Imagination", "weight": 1.0} -->

Dreamer learns long-horizon behaviors in the compact latent space of a learned world model by efficiently leveraging the neural network latent dynamics. For this, we propagate stochastic gradients of multi-step returns through neural network predictions of actions, states, rewards, and values using reparameterization. This section describes the main contribution of our paper.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Imagination environment", "weight": 1.0} -->

The latent dynamics define a Markov decision process that is fully observed because the compact model states $s_{t}$ are Markovian. We denote imagined quantities with $\tau$ as the time index. Imagined trajectories start at the true model states $s_{t}$ of observation sequences drawn from the agent's past experience. They follow predictions of the transition model $s_{\tau} \sim {q{({s_{\tau}{}_{\tau - 1}},a_{\tau - 1})}}$, reward model $r_{\tau} \sim {q{({r_{\tau}{}_{\tau}})}}$, and a policy $a_{\tau} \sim {q{({a_{\tau}{}_{\tau}})}}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Imagination environment", "weight": 1.0} -->

The objective is to maximize expected imagined rewards $E_{q}\left( {\sum_{\tau = t}^{\infty}{\gamma^{\tau - t}r_{\tau}}} \right)$ with respect to the policy.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Action and value models", "weight": 1.0} -->

Consider imagined trajectories with a finite horizon $H$. Dreamer uses an actor critic approach to learn behaviors that consider rewards beyond the horizon. We learn an action model and a value model in the latent space of the world model for this. The action model implements the policy and aims to predict actions that solve the imagination environment. The value model estimates the expected imagined rewards that the action model achieves from each state $s_{\tau}$, | | Value model: | | | ${{v_{\psi}{(s_{\tau})}} \approx {E_{q{(\cdot |s_{\tau})}}\left({\sum_{\tau = t}^{t + H}{\gamma^{\tau - t}r_{\tau}}} \right)}}.$ | | | The action and value models are trained cooperatively as typical in policy iteration: the action model aims to maximize an estimate of the value, while the value model aims to match an estimate of the value that changes as the action model changes.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Action and value models", "weight": 1.0} -->

We use dense neural networks for the action and value models with parameters $\phi$ and $\psi$, respectively. The action model outputs a tanh-transformed Gaussian with sufficient statistics predicted by the neural network. This allows for reparameterized sampling that views sampled actions as deterministically dependent on the neural network output, allowing us to backpropagate analytic gradients through the sampling operation,

<!-- chunk {"id": "body-0025", "role": "body", "section": "Value estimation", "weight": 1.0} -->

To learn the action and value models, we need to estimate the state values of imagined trajectories ${\{ s_{\tau},a_{\tau},r_{\tau}\}}_{\tau = t}^{t + H}$. These trajectories branch off of the model states $s_{t}$ of sequence batches drawn from the agent's dataset of experience and predict forward for the imagination horizon $H$ using actions sampled from the action model. State values can be estimated in multiple ways that trade off bias and variance, where the expectations are estimated under the imagined trajectories. $V_{R}$ simply sums the rewards from $\tau$ until the horizon and ignores rewards beyond it. This allows learning the action model without a value model, an ablation we compare to in our experiments. $V_{N}^{k}$ estimates rewards beyond $k$ steps with the learned value model. Dreamer uses $V_{\lambda}$, an exponentially-weighted average of the estimates for different $k$ to balance bias and variance.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Value estimation", "weight": 1.0} -->

Figure 4 shows that learning a value model in imagination enables Dreamer to solve long-horizon tasks while being robust to the imagination horizon. The experimental details and results on all tasks are described in Section 6.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Learning objective", "weight": 1.0} -->

To update the action and value models, we first compute the value estimates $V_{\lambda}{(s_{\tau})}$ for all states $s_{\tau}$ along the imagined trajectories. The objective for the action model $q_{\phi}{({a_{\tau}{}_{\tau}})}$ is to predict actions that result in state trajectories with high value estimates. The objective for the value model $v_{\psi}{(s_{\tau})}$, in turn, is to regress the value estimates, The value model is updated to regress the targets, around which we stop the gradient as typical. The action model uses analytic gradients through the learned dynamics to maximize the value estimates. To understand this, we note that the value estimates depend on the reward and value predictions, which depend on the imagined states, which in turn depend on the imagined actions.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Learning objective", "weight": 1.0} -->

Since all steps are implemented as neural networks, we analytically compute ${\nabla_{\phi}E_{q_{\theta},q_{\phi}}}\left({\sum_{\tau = t}^{t + H}{V_{\lambda}{(s_{\tau})}}} \right)$ by stochastic backpropagation. We use reparameterization for continuous actions and latent states and straight-through gradients for discrete actions. The world model is fixed while learning behaviors.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Learning objective", "weight": 1.0} -->

In tasks with early termination, the world model also predicts the discount factor from each latent state to weigh the time steps in Equations 7 and 8 by the cumulative product of the predicted discount factors, so terms are weighted down based on how likely the imagined trajectory would have ended.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Comparison to actor critic methods", "weight": 1.0} -->

Agents using Reinforce gradients, such as A3C and PPO, employ value baselines to reduce gradient variance, while Dreamer backpropagates through the value model. This is similar to deterministic or reparameterized actor critics, such as DDPG and SAC. However, these do not leverage gradients through transitions and only maximize immediate Q-values. MVE and STEVE extend them to multi-step Q-learning with learned dynamics to provide more accurate Q-value targets. We predict state values, which is sufficient for policy optimization since we backpropagate through the dynamics. Refer to Section 5 for a more detailed comparison to related work.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Learning Latent Dynamics", "weight": 1.0} -->

Learning behaviors in imagination requires a world model that generalizes well. We focus on latent dynamics models that predict forward in a compact latent space, facilitating long-term predictions and allowing the agent to imagine thousands of trajectories in parallel. Several objectives for learning representations for control have been proposed. We review three approaches for learning representations to use with Dreamer: reward prediction, image reconstruction, and contrastive estimation.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Reward prediction", "weight": 1.0} -->

Latent imagination requires a representation model $p{({s_{t}{}_{t - 1}},a_{t - 1},o_{t})}$, transition model $q{(s_{t}{}_{t - 1},a_{t - 1},)}$, and reward model $q{({r_{t}{}_{t}})}$, as described in Section 2. In principle, this could be achieved by simply learning to predict future rewards given actions and past observations. With a large and diverse dataset, such representations should be sufficient for solving a control task. However, with a finite dataset and especially when rewards are sparse, learning about observations that correlate with rewards is likely to improve the world model.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Reconstruction", "weight": 1.0} -->

We first describe the world model used by PlaNet that learns latent dynamics by reconstructing images as shown in Figure 3(a). The world model consists of the following components, where the observation model is only used to provide a learning signal, The components are optimized jointly to increase the variational lower bound or more generally the variational information bottleneck. As derived in Appendix B, the bound includes reconstruction terms for observations and rewards and a KL regularizer.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Reconstruction", "weight": 1.0} -->

The expectation is taken under the dataset and representation model, | | | ${\mathcal{J}_{REC} \doteq {{E_{p}\left({\sum\limits_{t}\left({\mathcal{J}_{O}^{t} + \mathcal{J}_{R}^{t} + \mathcal{J}_{D}^{t}} \right)} \right)} + \text{const}}}\qquad{\mathcal{J}_{O}^{t} \doteq {{\ln q}{({o_{t}{}_{t}})}}}$ | | \(10\) | We implement the transition model as a recurrent state space model, the representation model by combining the RSSM with a convolutional neural network applied to the image observation, the observation model as a transposed CNN, and the reward model as a dense network. The combined parameter vector $\theta$ is updated by stochastic backpropagation.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Reconstruction", "weight": 1.0} -->

Figure 5 shows video predictions of this model. We refer to Appendix A and Hafner et al. model details.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Contrastive estimation", "weight": 1.0} -->

Predicting pixels can require high model capacity. We can also encourage mutual information between model states and observations by instead predicting the states from the images. This replaces the observation model with a state model, While the reconstruction objective used the fact that the observation marginal is a constant, we now face the state marginal. As shown in Appendix B, this can be estimated via noise contrastive estimation by averaging the state model over observations $o'$ of the current sequence batch. Intuitively, $q{({s_{t}{}_{t}})}$ makes the state predictable from the current image while $\ln{\sum_{o'}{q{({s_{t}{}'})}}}$ keeps it diverse to prevent collapse, We implement the state model as a CNN and again optimize the bound with respect to the combined parameter vector $\theta$ using stochastic backpropagation. While avoiding pixel prediction, the amount of information this bound can extract efficiently is limited. We empirically compare reward, reconstruction, and contrastive objectives in our experiments in Figure 8.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Control with latent dynamics", "weight": 1.0} -->

E2C and RCE embed images to predict forward in a compact space to solve simple tasks. World Models learn latent dynamics in a two-stage process to evolve linear controllers in imagination. PlaNet learns them jointly and solves visual locomotion tasks by latent online planning. SOLAR solves robotic tasks via guided policy search in latent space. I2A hands imagined trajectories to a model-free policy, while Lee et al. and Gregor et al. learn belief representations to accelerate model-free agents.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Imagined multi-step returns", "weight": 1.0} -->

VPN, MVE, and STEVE learn dynamics for multi-step Q-learning from a replay buffer. AlphaGo combines predictions of actions and state values with planning, assuming access to the true dynamics. Also assuming access to the dynamics, POLO plans to explore by learning a value ensemble. MuZero learns task-specific reward and value models to solve challenging tasks but requires large amounts of experience. PETS, VisualMPC, and PlaNet plan online using derivative-free optimization. POPLIN improves over online planning by self-imitation. Piergiovanni et al. learn robot policies by imagination with a latent dynamics model. Planning with neural network gradients was shown on small problems but has been challenging to scale.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Analytic value gradients", "weight": 1.0} -->

DPG, DDPG, and SAC leverage gradients of learned immediate action values to learn a policy by experience replay. SVG reduces the variance of model-free on-policy algorithms by analytic value gradients of one-step model predictions. Concurrent work by Byravan et al. uses latent imagination with deterministic models for navigation and manipulation tasks. ME-TRPO accelerates an otherwise model-free agent via gradients of predicted rewards for proprioceptive inputs. DistGBP uses model gradients for online planning in simple tasks.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiments", "weight": 1.0} -->

We experimentally evaluate Dreamer on a variety of control tasks. We designed the experiments to compare Dreamer to current best methods in the literature, and to evaluate its ability to solve tasks with long horizons, continuous actions, discrete actions, and early termination. We further compare the orthogonal choice of learning objective for the world model. The source code for all our experiments and videos of Dreamer are available at

<!-- chunk {"id": "body-0041", "role": "body", "section": "Control tasks", "weight": 1.0} -->

We evaluate Dreamer on 20 visual control tasks of the DeepMind Control Suite Tassa et al., illustrated in Figure 2. These tasks pose a variety of challenges, including sparse rewards, contact dynamics, and 3D scenes. We selected the tasks on which Tassa et al. report non-zero performance from image inputs. Agent observations are images of shape $64 \times 64 \times 3$, actions range from $1$ to $12$ dimensions, rewards range from $0$ to $1$, episodes last for $1000$ steps and have randomized initial states. We use a fixed action repeat of $R = 2$ across tasks. We further evaluate the applicability of Dreamer to discrete actions and early termination on a subset of Atari games and DeepMind Lab levels as detailed in Appendix C.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Implementation", "weight": 1.0} -->

Our implementation uses TensorFlow Probability. We use a single Nvidia V100 GPU and 10 CPU cores for each training run. The training time for our Dreamer implementation is about $3$ hours per $10^{6}$ environment steps on the control suite, compared to $11$ hours for online planning using PlaNet, and the $24$ hours used by D4PG to reach similar performance. We use the same hyper parameters across all continuous tasks, and similarly across all discrete tasks, detailed in Appendix A. The world models are learned via reconstruction unless specified.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Baseline methods", "weight": 1.0} -->

The highest reported performance on the continuous tasks is achieved by D4PG, an improved variant of DDPG that uses distributed collection, distributional Q-learning, multi-step returns, and prioritized replay. We include the scores for D4PG with pixel inputs and A3C with state inputs from Tassa et al.. PlaNet learns the same world model as Dreamer and selects actions via online planning without an action model and drastically improves over D4PG and A3C in data efficiency. We re-run PlaNet with $R = 2$ for a unified experimental setup. For Atari, we show the final performance of SimPLe, DQN and Rainbow reported by Castro et al., and for DeepMind Lab that of IMPALA as a guideline.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Performance", "weight": 1.0} -->

To evaluate the performance of Dreamer, we compare it to state-of-the-art reinforcement learning agents. The results are summarized in Figure 6. With an average score of $823$ across tasks after $5 \times 10^{6}$ environment steps, Dreamer exceeds the performance of the strong model-free D4PG agent that achieves an average of $786$ within $10^{8}$ environment steps. At the same time, Dreamer inherits the data-efficiency of PlaNet, confirming that the learned world model can help to generalize from small amounts of experience. The empirical success of Dreamer shows that learning behaviors by latent imagination with world models can outperform top methods based on experience replay.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Long horizons", "weight": 1.0} -->

To investigate its ability to learn long-horizon behaviors, we compare Dreamer to alternatives for deriving behaviors from the world model at various horizon lengths. For this, we learn an action model to maximize imagined rewards without a value model and compare to online planning using PlaNet. Figure 4 shows the final performance for different imagination horizons, confirming that the value model makes Dreamer more robust to the horizon and performs well even for short horizons. Performance curves for all 19 tasks with horizon of 20 are shown in Appendix D, where Dreamer outperforms the alternatives on 16 of 20 tasks, with 4 ties.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Representation learning", "weight": 1.0} -->

Dreamer can be used with any differentiable dynamics model that predicts future rewards given actions and past observations. Since the representation learning objective is orthogonal to our algorithm, we compare three natural choices described in Section 4: pixel reconstruction, contrastive estimation, and pure reward prediction. Figure 8 shows clear differences in task performance for different representation learning approaches, with pixel reconstruction outperforming contrastive estimation on most tasks. This suggests that future improvements in representation learning are likely to translate to higher task performance with Dreamer. Reward prediction alone was not sufficient in our experiments. Further ablations are included in the appendix of the paper.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We present Dreamer, an agent that learns long-horizon behaviors purely by latent imagination. For this, we propose an actor critic method that optimizes a parametric policy by propagating analytic gradients of multi-step values back through learned latent dynamics. Dreamer outperforms previous methods in data-efficiency, computation time, and final performance on a variety of challenging continuous control tasks with image inputs. We further show that Dreamer is applicable to tasks with discrete actions and early episode termination. Future research on representation learning can likely scale latent imagination to environments of higher visual complexity.
