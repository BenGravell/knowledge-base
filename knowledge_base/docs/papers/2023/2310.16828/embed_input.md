<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

TD-MPC2: Scalable, Robust World Models for Continuous Control

Topics include Reinforcement learning, Trajectory optimization, Robustness, Online algorithms, Optimization, Control, Learning, TD-MPC2.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

TD-MPC is a model-based reinforcement learning (RL) algorithm that performs local trajectory optimization in the latent space of a learned implicit (decoder-free) world model. In this work, we present TD-MPC2: a series of improvements upon the TD-MPC algorithm. We demonstrate that TD-MPC2 improves significantly over baselines across 104 online RL tasks spanning 4 diverse task domains, achieving consistently strong results with a single set of hyperparameters. We further show that agent capabilities increase with model and data size, and successfully train a single 317M parameter agent to perform 80 tasks across multiple task domains, embodiments, and action spaces. We conclude with an account of lessons, opportunities, and risks associated with large TD-MPC2 agents. Explore videos, models, data, code, and more at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Training large models on internet-scale datasets has led to generalist models that perform a wide variety of language and vision tasks (Brown et al. He et al. Kirillov et al., ). The success of these models can largely be attributed to the availability of enormous datasets, and carefully designed architectures that reliably scale with model and data size. While researchers have recently extended this paradigm to robotics (Reed et al. Brohan et al., ), a generalist embodied agent that learns to perform diverse control tasks via low-level actions, across multiple embodiments, from large uncurated (*i.e.*, mixed-quality) datasets remains an elusive goal. We argue that current approaches to generalist embodied agents suffer from *(a)* the assumption of near-expert trajectories for behavior cloning which severely limits the amount of available data (Reed et al. Lee et al. Kumar et al. Schubert et al. Driess et al. Brohan et al., ), and *(b)* a lack of scalable continuous control algorithms that are able to consume large uncurated datasets.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement Learning (RL) is an ideal framework for extracting expert behavior from uncurated datasets. However, most existing RL algorithms (Lillicrap et al. Haarnoja et al., ) are designed for single-task learning and rely on per-task hyperparameters, with no principled method for selecting those hyperparameters. An algorithm that can consume large multi-task datasets will invariably need to be robust to variation between different tasks (*e.g.*, action space dimensionality, difficulty of exploration, and reward distribution). In this work, we present TD-MPC2: a significant step towards achieving this goal. TD-MPC2 is a model-based RL algorithm designed for learning generalist world models on large uncurated datasets composed of multiple task domains, embodiments, and action spaces, with data sourced from behavior policies that cover a wide range of skill levels, and without the need for hyperparameter-tuning.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our algorithm, which builds upon TD-MPC, performs local trajectory optimization in the latent space of a learned implicit (decoder-free) world model. While the TD-MPC family of algorithms has demonstrated strong empirical performance in prior work (Hansen et al. Yuan et al. Yang et al. Feng et al. Chitnis et al. Zhu et al. Lancaster et al., ), most successes have been limited to single-task learning with little emphasis on scaling. As shown in Figure, naïvely increasing model and data size of TD-MPC often leads to a net *decrease* in agent performance, as is commonly observed in RL literature. In contrast, scaling TD-MPC2 leads to consistently improved capabilities. Our algorithmic contributions, which have been key to achieving this milestone, are two-fold: ** improved algorithmic robustness by revisiting core design choices, and ** careful design of an architecture that can accommodate datasets with multiple embodiments and action spaces without relying on domain knowledge.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The resulting algorithm, TD-MPC2, is scalable, robust, and can be applied to a variety of single-task and multi-task continuous control problems using a *single* set of hyperparameters.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate TD-MPC2 across a total of $\mathbf{1}\mathbf{0}\mathbf{4}$ diverse continuous control tasks spanning 4 task domains: DMControl, Meta-World, ManiSkill2, and MyoSuite. We summarize our results in Figure, and visualize task domains in Figure. Tasks include high-dimensional state and action spaces (up to $\mathcal{A} \in {\mathbb{R}}^{39}$), image observations, sparse rewards, multi-object manipulation, physiologically accurate musculoskeletal motor control, complex locomotion (*e.g.* Dog and Humanoid embodiments), and cover a wide range of task difficulties. Our results demonstrate that TD-MPC2 consistently outperforms existing model-based and model-free methods, using the *same* hyperparameters across all tasks. Here, "Locomotion" and "Pick YCB" are particularly challenging subsets of DMControl and ManiSkill2, respectively.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We further show that agent capabilities increase with model and data size, and successfully train a single $317$M parameter world model to perform $\mathbf{8}\mathbf{0}$ tasks across multiple task domains, embodiments, and action spaces. In support of open-source science, we publicly release $\mathbf{3}\mathbf{0}\mathbf{0}$+ model checkpoints, datasets, and code for training and evaluating TD-MPC2 agents, which is available at We conclude the paper with an account of lessons, opportunities, and risks associated with large TD-MPC2 agents.

<!-- chunk {"id": "body-0009", "role": "body", "section": "TD-MPC2", "weight": 1.0} -->

Our work builds upon TD-MPC, a model-based RL algorithm that performs local trajectory optimization (planning) in the latent space of a learned implicit world model. TD-MPC2 is a practical algorithm for training massively multitask world models. Specifically, we propose a series of improvements to the TD-MPC algorithm, which have been key to achieving strong algorithmic robustness (can use the same hyperparameters across all tasks) and scaling its world model to $\mathbf{3}\mathbf{0}\mathbf{0} \times$ more parameters than previously. We introduce the TD-MPC2 algorithm in the following, and provide a full list of algorithmic improvements in Appendix A.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Learning an Implicit World Model", "weight": 1.0} -->

Learning a generative model of the environment using a reconstruction (decoder) objective is tempting due to its rich learning signal. However, accurately predicting raw future observations (*e.g.*, images or proprioceptive features) over long time horizons is a difficult problem, and does not necessarily lead to effective control. Rather than explicitly modeling dynamics using reconstruction, TD-MPC2 aims to learn a *maximally useful* model: a model that accurately predicts *outcomes* (returns) conditioned on a sequence of actions. Specifically, TD-MPC2 learns an *implicit*, control-centric world model from environment interaction using a combination of joint-embedding prediction, reward prediction, and TD-learning, *without* decoding observations. We argue that this alternative formulation of model-based RL is key to modeling large datasets with modest model sizes. The world model can subsequently be used for decision-making by performing local trajectory optimization (planning) following the MPC framework.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Learning an Implicit World Model", "weight": 1.0} -->

where $\mathbf{s}$ and $\mathbf{a}$ are states and actions, $\mathbf{z}$ is the latent representation, and $\mathbf{e}$ is a learnable task embedding for use in multitask world models. For visual clarity, we will omit $\mathbf{e}$ in the following unless it is particularly relevant. The policy prior $p$ serves to guide the sample-based trajectory optimizer (planner), and to reduce the computational cost of TD-learning. During online interaction, TD-MPC2 maintains a replay buffer $\mathcal{B}$ with trajectories, and iteratively *(i)* updates the world model using data sampled from $\mathcal{B}$, and *(ii)* collects new environment data by planning with the learned model.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Learning an Implicit World Model", "weight": 1.0} -->

Model objective. The $h,d,R,Q$ components are jointly optimized to minimize the objective

<!-- chunk {"id": "body-0013", "role": "body", "section": "Learning an Implicit World Model", "weight": 1.0} -->

where $sg$ is the stop-grad operator, $(\mathbf{z}_{t}^{\prime},{\hat{r}}_{t},{\hat{q}}_{t})$ are defined in Equation, $q_{t} \doteq {r_{t} + {\gamma\overline{Q}{(\mathbf{z}_{t}^{\prime},{p{(\mathbf{z}_{t}^{\prime})}})}}}$ is the TD-target at step $t$, $\lambda \in {(0,1\rbrack}$ is a constant coefficient that weighs temporally farther time steps less, and $CE$ is the cross-entropy. $\overline{Q}$ used to compute the TD-target is an exponential moving average (EMA) of $Q$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Learning an Implicit World Model", "weight": 1.0} -->

As the magnitude of rewards may differ drastically between tasks, TD-MPC2 formulates reward and value prediction as a discrete regression (multi-class classification) problem in a $\log$-transformed space, which is optimized by minimizing cross-entropy with $r_{t},q_{t}$ as soft targets (Bellemare et al. Kumar et al. Hafner et al., ).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Learning an Implicit World Model", "weight": 1.0} -->

Policy objective. The policy prior $p$ is a stochastic maximum entropy (Ziebart et al. Haarnoja et al., ) policy that learns to maximize the objective

<!-- chunk {"id": "body-0016", "role": "body", "section": "Learning an Implicit World Model", "weight": 1.0} -->

where $\mathcal{H}$ is the entropy of $p$ which can be computed in closed form. Gradients of $\mathcal{L}_{p}{(\theta)}$ are taken wrt. $p$ only. As magnitude of the value estimate $Q{(\mathbf{z}_{t},{p{(\mathbf{z}_{t})}})}$ and entropy $\mathcal{H}$ can vary greatly between datasets and different stages of training, it is necessary to balance the two losses to prevent premature entropy collapse. A common choice for automatically tuning $\alpha,\beta$ is to keep one of them constant, and adjusting the other based on an entropy target or moving statistics. In practice, we opt for tuning $\alpha$ via moving statistics, but empirically did not observe any significant difference in results between these two options.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Learning an Implicit World Model", "weight": 1.0} -->

Architecture. All components of TD-MPC2 are implemented as MLPs with intermediate linear layers followed by LayerNorm and Mish activations. To mitigate exploding gradients, we normalize the latent representation by projecting $\mathbf{z}$ into $L$ fixed-dimensional simplices using a softmax operation. A key benefit of embedding $\mathbf{z}$ as simplices (as opposed to *e.g.* a discrete representation or squashing) is that it naturally biases the representation towards sparsity without enforcing hard constraints (see Appendix H for motivation and implementation). We dub this normalization scheme *SimNorm*. Let $V$ be the dimensionality of each simplex $\mathbf{g}$ constructed from $L$ partitions (groups) of $\mathbf{z}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Learning an Implicit World Model", "weight": 1.0} -->

where $\mathbf{z}^{\circ}$ is the simplicial embedding of $\mathbf{z}$, $\lbrack \cdot \rbrack$ denotes concatenation, and $\tau > 0$ is a temperature parameter that modulates the "sparsity" of the representation. As we will demonstrate in our experiments, SimNorm is essential to the training stability of TD-MPC2. Finally, to reduce bias in TD-targets generated by $\overline{Q}$, we learn an *ensemble* of $Q$-functions using the objective from Equation and maintain $\overline{Q}$ as an EMA of each $Q$-function. We use $5$ $Q$-functions in practice. Targets are then computed as the minimum of two randomly sub-sampled $\overline{Q}$-functions.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Model Predictive Control with a Policy Prior", "weight": 1.0} -->

TD-MPC2 derives its closed-loop control policy by planning with the learned world model. Specifically, our approach leverages the MPC framework for local trajectory optimization using Model Predictive Path Integral (MPPI) as a derivative-free optimizer with sampled action sequences $(\mathbf{a}_{t},\mathbf{a}_{t + 1},\ldots,\mathbf{a}_{t + H})$ of length $H$ evaluated by rolling out *latent* trajectories with the model. At each decision step, we estimate parameters $\mu^{*},\sigma^{*}$ of a time-dependent multivariate Gaussian with diagonal covariance such that expected return is maximized, *i.e.*,

<!-- chunk {"id": "body-0020", "role": "body", "section": "Model Predictive Control with a Policy Prior", "weight": 1.0} -->

where ${{\mu,\sigma} \in {\mathbb{R}}^{H \times m}},{\mathcal{A} \in {\mathbb{R}}^{m}}$. Equation is solved by iteratively sampling action sequences from $\mathcal{N}{(\mu,\sigma^{2})}$, evaluating their expected return, and updating $\mu,\sigma$ based on a weighted average. Notably, Equation estimates the full RL objective introduced in Section by bootstrapping with the learned terminal value function beyond horizon $H$. TD-MPC2 repeats this iterative planning process for a fixed number of iterations and executes the first action $\mathbf{a}_{t} \sim {\mathcal{N}{(\mu_{t}^{*},\sigma_{t}^{*})}}$ in the environment.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Model Predictive Control with a Policy Prior", "weight": 1.0} -->

To accelerate convergence of planning, a fraction of action sequences originate from the policy prior $p$, and we warm-start planning by initializing $(\mu,\sigma)$ as the solution to the previous decision step shifted by $1$. Refer to Hansen et al. for more details about the planning procedure.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Training Generalist TD-MPC2 Agents", "weight": 1.0} -->

The success of TD-MPC2 in diverse single-task problems can be attributed to the algorithm outlined above. However, learning a large generalist TD-MPC2 agent that performs a variety of tasks across multiple task domains, embodiments, and action spaces poses several unique challenges: *(i)* how to learn and represent task semantics? *(ii)* how to accommodate multiple observation and action spaces without specific domain knowledge? *(iii)* how to leverage the learned model for few-shot learning of new tasks? We describe our approach to multitask model learning in the following.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Training Generalist TD-MPC2 Agents", "weight": 1.0} -->

Learnable task embeddings. To succeed in a multitask setting, an agent needs to learn a common representation that takes advantage of task similarities, while still retaining the ability to differentiate between tasks at test-time. When task or domain knowledge is available, *e.g.* in the form of natural language instructions, the task embedding $\mathbf{e}$ from Equation may encode such information. However, in the general case where domain knowledge cannot be assumed, we may instead choose to *learn* the task embeddings (and, implicitly, task relations) from data. TD-MPC2 conditions all of its five components with a learnable, fixed-dimensional task embedding $\mathbf{e}$, which is jointly trained together with other components of the model. To improve training stability, we constrain the $\ell_{2}$-norm of $\mathbf{e}$ to be $\leq 1$; this also leads to more semantically coherent task embeddings in our experiments.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Training Generalist TD-MPC2 Agents", "weight": 1.0} -->

When finetuning a multitask TD-MPC2 agent to a new task, we can choose to either initialize $\mathbf{e}$ as the embedding of a semantically similar task, or simply as a random vector.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Training Generalist TD-MPC2 Agents", "weight": 1.0} -->

Action masking. TD-MPC2 learns to perform tasks with a variety of observation and action spaces, without any domain knowledge. To do so, we zero-pad all model inputs and outputs to their largest respective dimensions, and mask out invalid action dimensions in predictions made by the policy prior $p$ during both training and inference. This ensures that prediction errors in invalid dimensions do not influence TD-target estimation, and prevents $p$ from falsely inflating its entropy for tasks with small action spaces. We similarly only sample actions along valid dimensions during planning.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate TD-MPC2 across a total of $\mathbf{1}\mathbf{0}\mathbf{4}$ diverse continuous control tasks spanning 4 task domains: DMControl, Meta-World, ManiSkill2, and MyoSuite. Tasks include high-dimensional state and action spaces (up to $\mathcal{A} \in {\mathbb{R}}^{39}$), sparse rewards, multi-object manipulation, physiologically accurate musculoskeletal motor control, complex locomotion (*e.g.* Dog and Humanoid embodiments), and cover a wide range of task difficulties. We also include $\mathbf{1}\mathbf{0}$ DMControl tasks with visual observations. In support of open-source science, we publicly release $\mathbf{3}\mathbf{0}\mathbf{0}$+ model checkpoints, datasets, and code for training and evaluating TD-MPC2 agents, which is available at

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experiments", "weight": 1.0} -->

Comparison to existing methods. How does TD-MPC2 compare to state-of-the-art model-free (SAC) and model-based (DreamerV3, TD-MPC) methods for data-efficient continuous control?

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experiments", "weight": 1.0} -->

Scaling. Do the algorithmic innovations of TD-MPC2 lead to improved agent capabilities as model and data size increases? Can a single agent learn to perform diverse skills across multiple task domains, embodiments, and action spaces?

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments", "weight": 1.0} -->

Analysis. How do the specific design choices introduced in TD-MPC2 influence downstream task performance? How much does planning contribute to its success? Are the learned task embeddings semantically meaningful? Can large multi-task agents be adapted to unseen tasks?

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

Baselines. Our primary baselines represent the state-of-the-art in data-efficient RL, and include ** Soft Actor-Critic (SAC), a model-free actor-critic algorithm based on maximum entropy RL, ** DreamerV3, a model-based method that optimizes a model-free policy with rollouts from a learned generative model of the environment, and ** the original version of TD-MPC, a model-based RL algorithm that performs local trajectory optimization (planning) in the latent space of a learned *implicit* (non-generative) world model. Additionally, we also compare against current state-of-the-art visual RL methods ** CURL, an extension of SAC that uses a contrastive auxiliary objective, and ** DrQ-v2, a model-free RL algorithm that uses data augmentation. SAC and TD-MPC use task-specific hyperparameters, whereas TD-MPC2 uses the same hyperparameters across all tasks.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

Additionally, it is worth noting that both SAC and TD-MPC use a larger batch size of $512$, while $256$ is sufficient for stable learning with TD-MPC2. Similarly, DreamerV3 uses a high update-to-data (UTD) ratio of $512$, whereas TD-MPC2 uses a UTD of $1$ by default. We use a $5$M parameter TD-MPC2 agent in all experiments (unless stated otherwise). For reference, the DreamerV3 baseline has approx. $20$M learnable parameters. See Appendix H for more details.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Results", "weight": 1.0} -->

Comparison to existing methods. We first compare the data-efficiency of TD-MPC2 to a set of strong baselines on $\mathbf{1}\mathbf{0}\mathbf{4}$ diverse tasks in an online RL setting. Aggregate results are shown in Figure. We find that TD-MPC2 outperforms prior methods across all task domains. The MyoSuite results are particularly noteworthy, as we did not run *any* TD-MPC2 experiments on this benchmark prior to the reported results. Individual task performances on some of the most difficult tasks (high-dimensional locomotion and multi-object manipulation) are shown in Figure and Figure. TD-MPC2 outperforms baselines by a large margin on these tasks, despite using the same hyperparameters across all tasks. Notably, TD-MPC sometimes diverges due to exploding gradients, whereas TD-MPC2 remains stable. We provide per-task visualization of gradients in Appendix G.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Results", "weight": 1.0} -->

Similarly, we observe that DreamerV3 experiences occasional numerical instabilities (*Dog*) and generally struggles with tasks that require fine-grained object manipulation (*lift*, *pick*, *stack*). See Appendix D for the full single-task RL results.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Results", "weight": 1.0} -->

Massively multitask world models. To demonstrate that our proposed improvements facilitate scaling of world models, we evaluate the performance of $5$ multitask models ranging from $1$M to $317$M parameters on a collection of $\mathbf{8}\mathbf{0}$ diverse tasks that span multiple task domains and vary greatly in objective, embodiment, and action space. Models are trained on a dataset of $545$M transitions obtained from the replay buffers of $240$ single-task TD-MPC2 agents, and thus contain a wide variety of behaviors ranging from random to expert policies. The task set consists of all $50$ Meta-World tasks, as well as $30$ DMControl tasks. The DMControl task set includes $19$ original DMControl tasks, as well as $11$ new tasks. For completeness, we include a separate set of scaling results on the $30$-task DMControl subset ($345$M transitions) as well.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Results", "weight": 1.0} -->

Due to our careful design of the TD-MPC2 algorithm, scaling up is straightforward: to improve rate of convergence we use a $4 \times$ larger batch size ($1024$) compared to the single-task experiments, but make no other changes to hyperparameters.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Results", "weight": 1.0} -->

Scaling TD-MPC2 to $\mathbf{3}\mathbf{1}\mathbf{7}$M parameters. Our scaling results are shown in Figure. To summarize agent performance with a single metric, we produce a normalized score that is an average of all individual task success rates (Meta-World) and episode returns normalized to the $\lbrack 0,100\rbrack$ range (DMControl). We observe that agent capabilities consistently increase with model size on both task sets. Notably, performance does not appear to have saturated for our largest models ($317$M parameters) on either dataset, and we can thus expect results to continue improving beyond our considered model sizes. We refrain from formulating a scaling law, but note that normalized score appears to scale linearly with the log of model parameters. We also report approximate training costs in Table. The $317$M parameter model can be trained with limited computational resources. To better understand why multitask model learning is successful, we explore the task embeddings learned by TD-MPC2.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Results", "weight": 1.0} -->

Intriguingly, tasks that are semantically similar (*e.g.*, Door Open and Door Close) are close in the learned task embedding space. However, embedding similarity appears to align more closely with task *dynamics* (embodiment, objects) than objective (walk, run). This makes intuitive sense, as dynamics are tightly coupled with control.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Results", "weight": 1.0} -->

Few-shot learning. While our work mainly focuses on the *scaling* and *robustness* of world models, we also explore the efficacy of finetuning pretrained world models for few-shot learning of unseen tasks. Specifically, we pretrain a $19$M parameter TD-MPC2 agent on $70$ tasks from DMControl and Meta-World, and naïvely finetune the full model to each of $10$ held-out tasks ($5$ from each domain) via online RL with an initially empty replay buffer and no changes to hyperparameters. Aggregate results are shown in Figure. We find that TD-MPC2 improves $\mathbf{2} \times$ over learning from scratch on new tasks in the low-data regime ($20$k environment steps^11^1$20$k environment steps corresponds to $20$ episodes in DMControl and $100$ episodes in Meta-World.). Although finetuning world models to new tasks is very much an open research problem, our exploratory results are promising. See Appendix E for experiment details and individual task curves.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Results", "weight": 1.0} -->

Ablations. We ablate most of our design choices for TD-MPC2, including choice of actor, various normalization techniques, regression objective, and number of $Q$-functions. Our main ablations, shown in Figure, are conducted on three of the most difficult online RL tasks, as well as large-scale multitask training ($80$ tasks). We observe that all of our proposed improvements contribute meaningfully to the robustness and strong performance of TD-MPC2 in both single-task RL and multi-task RL. Interestingly, we find that the relative importance of each design choice is consistent across both settings. Lastly, we also ablate normalization of the learned task embeddings, shown in Appendix F. The results indicate that maintaining a normalized task embedding space ($\ell_{2}$-norm of $1$) is moderately important for stable multitask training, and results in more meaningful task relations.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Results", "weight": 1.0} -->

Visual RL. We mainly consider high-dimensional continuous control tasks with proprioceptive state observations in this work. However, TD-MPC2 can be readily applied to tasks with other input modalities as well. To demonstrate this, we replace the encoder of TD-MPC2 with a shallow convolutional encoder, and benchmark it against current state-of-the-art methods for visual RL on 10 DMControl tasks of varying difficulty. Results are shown in Figure. TD-MPC2 performs comparably to the two best baselines, DrQ-v2 and DreamerV3, without *any* changes to hyperparameters.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Lessons, Opportunities, and Risks", "weight": 1.0} -->

Lessons. Historically, RL algorithms have been notoriously sensitive to architecture, hyperparameters, characteristics of the task, and even random seed, with no principled method for tuning the algorithms. As a result, successful application of deep RL often requires large teams of experts with significant computational resources (Berner et al. Schrittwieser et al. Ouyang et al., ). TD-MPC2 -- along with several other contemporary RL methods (Yarats et al. Ye et al. Hafner et al., ) -- seek to democratize use of RL (*i.e.*, lowering the barrier of entry for smaller teams of academics, practitioners, and individuals with fewer resources) by improving robustness of existing open-source algorithms. We firmly believe that improving algorithmic robustness will continue to have profound impact on the field. A key lesson from the development of TD-MPC2 is that the community has yet to discover an algorithm that truly masters *everything* out-of-the-box.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Lessons, Opportunities, and Risks", "weight": 1.0} -->

While *e.g.* DreamerV3 has delivered strong results on challenging tasks with discrete action spaces (such as Atari games and Minecraft), we find that TD-MPC2 produces significantly better results on difficult continuous control tasks. At the same time, extending TD-MPC2 to discrete action spaces remains an open problem.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Lessons, Opportunities, and Risks", "weight": 1.0} -->

Opportunities. Our scaling results demonstrate a path for model-based RL in which massively multitask world models are leveraged as *generalist* world models. While multi-task world models remain relatively underexplored in literature, prior work suggests that the implicit world model of TD-MPC2 may be better suited than reconstruction-based approaches for tasks with large visual variation. We envision a future in which implicit world models are used zero-shot to perform diverse tasks on *seen* embodiments (Xu et al. Yang et al., ), finetuned to quickly perform tasks on *new* embodiments, and combined with existing vision-language models to perform higher-level cognitive tasks in conjunction with low-level physical interaction. Our results are promising, but such level of generalization will likely require several orders of magnitude more tasks than currently available. Lastly, we want to remark that, while TD-MPC2 relies on rewards for task learning, it is useful to adopt a generalized notion of reward as simply a metric for task completion.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Lessons, Opportunities, and Risks", "weight": 1.0} -->

Such metrics already exist in the wild, *e.g.*, success labels, human preferences or interventions, or the embedding distance between a current observation and a goal (Eysenbach et al. Ma et al., ) within a pre-existing learned representation. However, leveraging such rewards for large-scale pretraining is an open problem. To accelerate research in this area, we are releasing $\mathbf{3}\mathbf{0}\mathbf{0}$+ TD-MPC2 models, including 12 multitask models, as well as datasets and code, and we are beyond excited to see what the community will do with these resources.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Lessons, Opportunities, and Risks", "weight": 1.0} -->

Risks. While we are excited by the potential of generalist world models, several challenges remain: *(i)* misspecification of task rewards can lead to unintended outcomes that may be difficult to anticipate, *(ii)* handing over unconstrained autonomy of physical robots to a learned model can result in catastrophic failures if no additional safety checks are in place, and *(iii)* data for certain applications may be prohibitively expensive for small teams to obtain at the scale required for generalist behavior to emerge, leading to a concentration of power. Mitigating each of these challenges will require new research innovations, and we invite the community to join us in these efforts.
