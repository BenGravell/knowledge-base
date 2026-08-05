<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

RISE: Self-Improving Robot Policy with Compositional World Model

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Despite the sustained scaling on model capacity and data acquisition, Vision-Language-Action (VLA) models remain brittle in contact-rich and dynamic manipulation tasks, where minor execution deviations can compound into failures. While reinforcement learning (RL) offers a principled path to robustness, on-policy RL in the physical world is constrained by safety risk, hardware cost, and environment reset. To bridge this gap, we present RISE, a scalable framework of robotic reinforcement learning via imagination. At its core is a Compositional World Model that (i) predicts multi-view future via a controllable dynamics model, and (ii) evaluates imagined outcomes with a progress value model, producing informative advantages for the policy improvement. Such compositional design allows state and value to be tailored by best-suited yet distinct architectures and objectives. These components are integrated into a closed-loop self-improving pipeline that continuously generates imaginary rollouts, estimates advantages, and updates the policy in imaginary space without costly physical interaction. Across three challenging real-world tasks, RISE yields significant improvement over prior art, with more than +35% absolute performance increase in dynamic brick sorting, +45% for backpack packing, and +35% for box closing, respectively.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The trajectory of embodied intelligence has been reshaped by the scaling of foundation models. Particularly, VLA models have emerged as the dominant paradigm for generalist robot control, leveraging massive pre-training on web-scale data to acquire broad semantic understanding and instruction-following capabilities. Despite the progress on high-level semantic competence, such VLAs still fall short of robust manipulation under complex physical dynamics, such as precise grasping of moving objects or effective bi-manual coordination. This discrepancy highlights the inherent limitation of Imitation Learning (IL), a core mechanism enabling VLAs to generate executable actions. Concretely, IL is inherently limited by the quality and coverage of the expert demonstrations while suffering from the exposure bias problem: once the robot drifts slightly off the expert's manifold, it lacks the recovery skills to correct its course, leading to compounding errors. Reinforcement Learning (RL), which improves agents through their own success and failure, offers a potential remedy.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In virtual simulators such as LIBERO, agents can play massive interactions in parallel, where both state and reward updates are controllable and accessible. Such properties of highly-crafted simulators have inspired successful RL adaptations upon recent VLAs. Nonetheless, such controllability and parallelization do not hold in a real-world regime, where robot executions are serial, time-consuming, and labor-intensive due to manual monitoring and resets, as depicted in Fig. 1(a). These physical challenges largely confine previous methods of real-world RL to offline data with heavy distribution shift to current policy. Ultimately, the policy improvement could be bottlenecked without sufficient on-policy data stream.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The gap between the simulator and the physical world motivates the development of world models, which first learn from passive experience and then simulate future outcomes conditioned on different actions. Nevertheless, constructing a world model applicable to real-world robotics poses fundamental challenges. For control, world models must faithfully follow actions to represent the accurate consequences. Despite the improved visual realism by integrating high-capacity generative models, how to improve controllability over various actions remains an open problem. Furthermore, learning from imagination necessitates informative learning signals for intermediate actions, rather than relying solely on a binary indicator. Otherwise, determining terminal success would require the world model to simulate the entire task execution, which is beyond the reliable horizon of most generative world models.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To handle these issues, we present RISE, a holistic learning framework that Reinforces robot foundation model via Imagination to enable SElf-improving, as shown in Fig. 1(b). At its core is an online learning environment achieved by a learned world model. Inspired by prior works that decompose world modeling into tractable sub-problems to flexibly leverage heterogeneous architectures and priors, we build a Compositional World Model that factorizes the simulation problem into two objectives, dynamics prediction and value estimation, allowing each to be instantiated with architectures and training objectives best suited to its role.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Built on an efficient video diffusion model, we pre-train our dynamics model on large-scale robot datasets with a Task-centric Batching strategy to improve action controllability, which contributes to effective fine-tuning on targeted tasks. The value model is initialized from a pre-trained VLA backbone and adapted with both progress estimate and Temporal-Difference learning objectives, providing dense and failure-sensitive evaluation of imagined states. These components are combined to compute advantages for candidate actions, enabling stable policy improvement via advantage-conditioned training. As a result, RISE performs on-policy reinforcement learning effectively in imagination. As presented in Fig. 2, we rigorously evaluate RISE on a suite of real-world tasks that stress-test dynamic adaptation and precision. The results demonstrate that RISE outperforms previous RL methods by a non-trivial margin, while avoiding costly real-world trial-and-error.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our contributions are threefold: We propose RISE, a principled framework for robotic reinforcement learning, that enables autonomous self-improvement in a scalable and online manner. RISE overcomes the physical restrictions posed by prior art by shifting the robotic interactions from physical environment to imaginative space. At the core of this system is an online learning environment achieved by a Compositional World Model that builds reliable dynamics and value estimates for real-world tasks. We unveil critical design choices to derive stable learning signals for policy improvement. Through extensive experiments on dexterous tasks, we demonstrate that RISE exhibits significantly higher performance compared to existing RL methods.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We view our work as the first study on leveraging world models as an effective learning environment for challenging real-world manipulation, bootstrapping performance on tasks requiring high dynamics, dexterity, and precision. Code is available: Figure 2: Evaluation task suite of RISE. Left: Tabletop setting. Right: Zoomed-in details of each task procedure. Dynamic Brick Sorting involves precisely picking up colored bricks from a moving conveyor and placing them into the corresponding color-designated bins. Backpack Packing requires the robot to open, insert clothes, lift, and zip the backpack. Box Closing necessitates subtle controls to fold the flap and tuck the tab into the box precisely.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A World Model Formulation", "weight": 1.0} -->

We aim to construct a world model consisting of a dynamics model for predicting future states and a value model for predicting rewards over different courses of action. Crucially, these predicted rewards are converted into advantages to guide RL training. Formally, let $o_{t}=[m_{t}^{1},\dots,m_{t}^{n}]$ be the multi-view observation at time $t$ with $n$ camera views. We apply a history window of length $N$ as $\mathbf{O}_{t}=\{o_{t-N},\dots,o_{t-1},o_{t}\}$ to capture temporal dependency.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A World Model Formulation", "weight": 1.0} -->

The conditional action $\mathbf{a}_{t}$ is drawn from a running policy $\pi$ as $\mathbf{a}_{t}=[a_{t},a_{t+1},\dots,a_{t+H-1}]\sim\pi(\cdot|o_{t},\ell)$, where $\mathbf{a}_{t}$ is commonly applied as a sequence of actions with chunk length $H$, *i.e.*, action chunk, and $\ell$ is a language instruction describing the task.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A World Model Formulation", "weight": 1.0} -->

The dynamics model $\mathcal{D}$ predicts future observations $\{\hat{o}_{t+1},\dots,\hat{o}_{t+H}\}$ conditioned on both the historical context and the proposed action sequence: To evaluate the utility of imagined trajectories, we further introduce a value model $\mathcal{V}$, which assigns a progress signal towards successful completion conditioned on observation and task instruction as $\mathcal{V}(\hat{o}_{t},\ell)$. We define the advantage as the average cumulative improvement across the entire chunk. Specifically, we compute the difference between the value of each predicted future observation $\hat{o}_{t+k}$ and the initial observation $o_{t}$ as the reward of action $a_{t+k}$, then take the expectation over the horizon of the action chunk as the advantage: where $A$ is associated with the action chunk proposed by the policy $\pi$, forming the learning signal for policy optimization.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A World Model Formulation", "weight": 1.0} -->

The interaction between $\mathcal{D}$ and $\mathcal{V}$ occurs in imagination space, and both modules are compatible with multi-view images.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Reinforcement Learning", "weight": 1.0} -->

We formulate the problem as a standard RL setting with decision-making process as a Markov Decision Process (MDP) characterized by the tuple $(\mathcal{O},\ell,\mathcal{A},H,r)$. At each timestep $t$, given an observation $o_{t}\in\mathcal{O}$ and task instruction $\ell$, the policy $\pi$ generates an action sequence $\mathbf{a}_{t}\in\mathcal{A}^{H}$ of horizon $H$, obtaining reward $r$ for each step. The interaction between the policy and the environment induces a trajectory distribution $\rho_{\pi}(\tau)$, where $\tau=(o_{0},\mathbf{a}_{0},\dots,o_{T})\in\mathcal{O}\times\mathcal{A}\cdots\mathcal{O}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Reinforcement Learning", "weight": 1.0} -->

The objective is to maximize the expected return $\mathcal{J}(\pi)=\mathbb{E}_{\tau\sim\rho_{\pi}}[\sum_{t=0}^{T}r(o_{t},\mathbf{a}_{t})]$. To quantify the quality of a specific action sequence relative to the average policy performance, we utilize the advantage function $A^{\pi}(o_{t},\mathbf{a}_{t},\ell)$, estimated via Eq. 2.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Reinforcement Learning", "weight": 1.0} -->

To ensure stable improvement over a reference policy $\pi_{\text{ref}}$, we adopt the probabilistic inference framework from $\pi^{*}_{0.6}$. Rather than maximizing a regularized objective directly, we construct a target distribution $\hat{\pi}$ by weighting $\pi_{\text{ref}}$ with the probability of improvement $I$: Since improvement is fully determined by the advantage value, we have $p(I|A^{\pi_{\text{ref}}})\equiv p(I|\mathbf{a}_{t},o_{t},\ell)$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Reinforcement Learning", "weight": 1.0} -->

Applying Bayes' rule allows us to express the improvement likelihood as a density ratio: Substituting Eq. 4 into the target distribution and setting $\beta=1$ cancels the unconditional prior $\pi_{\text{ref}}$, yielding the simplified objective $\hat{\pi}(\mathbf{a}_{t}|o_{t},\ell)=\pi_{\text{ref}}(\mathbf{a}_{t}\mid I,o_{t},\ell)$. Practically, we implement this by conditioning the policy on discretized advantages, guiding generation toward high-return trajectories.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Methodology", "weight": 1.0} -->

Our approach is structured as follows: In Sec. III-A, we propose a Compositional World Model that composes dynamics prediction with value estimation, providing an interactive environment with informative learning signals. In Sec. III-B, we establish a Policy Warm-up stage on real-world experience to anchor the policy to practical behavioral distribution and equip it with advantage-conditioned capabilities. In Sec. III-C, we present a Self-Improving Loop that iteratively generates imaginary rollouts and optimizes the policy within the world model. Implementation details with compute allocation are covered in Sec. III-D.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Compositional World Model", "weight": 1.0} -->

Scalable RL necessitates precise environment modeling to map current states and policy actions to future dynamics and rewards. To this end, we introduce a Compositional World Model to disentangle dynamics prediction from value estimation, thereby enabling independent architectural optimization for each component. Starting from a context observation, the dynamics model emulates a faithful future under the candidate action chunk, which would be evaluated by the value model to derive an advantage for policy improvement. We show samples from imagination in Fig. 3 qualitatively. Crucially, the model is employed exclusively during training, imposing zero computational overhead at inference. The training recipe and inference pipeline of our world model are shown in Fig. 4.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Compositional World Model", "weight": 1.0} -->

Controllable Dynamics Model. Reliably simulating future states for RL yields two fundamental requirements: (i) The generation latency should not be prohibitively high, which would bottleneck the throughput of the RL system. (ii) The generated states should not only be plausible in visuals but also consistent with the conditional actions. Thereby, we initialize our dynamics model from pre-trained Genie Envisioner, *i.e.*, GE-base variant, which inherits the architectural advances in LTX-Video and features a favorable trade-off between generation quality and inference speed. In comparison, advanced world models such as Cosmos takes more than 10 minutes for synthesizing 25 multi-view observations, whereas GE only requires less than 2 seconds to achieve such a horizon, leading to 300x speedup. Such generation efficiency is a critical pillar for applicable RL training.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Compositional World Model", "weight": 1.0} -->

Despite its efficiency, GE-Base is originally conditioned on text rather than fine-grained robot actions. To endow the model with precise action controllability that could be further transferred into task-specific scenarios, we further optimize the model on large-scale action-labeled datasets, including Agibot World and Galaxea, by incorporating an additional light-weight action encoder. Additionally, we impose stronger noise on context frames compared to the original GE-base training, to improve the generation robustness when encountering motion blurs and visual artifacts that might occur in both recorded and synthesized data. Nevertheless, fine-tuning a controllable world model on heterogeneous action data is prone to instability and slow convergence when diverse tasks and visual domains are included within the same batch for each optimization iteration. We mitigate this issue with a Task-Centric Batching strategy, where each batch is sampled from a small fraction of tasks while covering more samples of the same task correlated with different actions. Intuitively, this batching strategy prioritizes action diversity under the same scene over scenario diversity for batch optimization, thus contributing to improved action controllability.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Compositional World Model", "weight": 1.0} -->

Empirically, applying this strategy improves both task-specific fine-tuning efficiency, as in Table V, and stronger policy improvement, as in Table IV. With these design choices, our dynamics model is capable of providing fast and faithful multi-view state prediction to support the self-improving loop.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Compositional World Model", "weight": 1.0} -->

Progress Value Model. Imagination-based policy improvement critically depends on a reward-related signal that is (i) dense over long horizons and (ii) sensitive to subtle failures in contact-rich manipulation. We therefore learn a value estimator $\mathcal{V}$ that maps sensory observations to a scalar value used to score imagined rollouts. $\mathcal{V}$ is parameterized from a pre-trained VLA policy $\pi_{0.5}$, that brings in two advantages. First, $\pi_{0.5}$ has been trained on broad robot datasets and thus carries robot-centric understanding that transfers naturally to value estimation. Second, the policy backbone is compatible with multi-view inputs, whereas generic VLMs are mostly developed on single-view images without such adaptation.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Compositional World Model", "weight": 1.0} -->

As for training, we warm-start $\mathcal{V}$ with a simple temporal progress estimate as objective, which equips our value model with a coarse understanding of monotonic temporal structure. where $t$ indexes the current timestep within an episode of length $T$. While progress regression provides a dense signal, it is often overly smooth and can be insensitive to failures, especially in contact-rich settings where execution errors might be subtle in visuals. To conquer this, we augment the progress loss with Temporal-Difference (TD) learning, which uses both successful demonstrations and failure rollouts to establish a value function that distinguishes success from errors.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Compositional World Model", "weight": 1.0} -->

Our final value learning objective simply combines both terms $\mathcal{L}_{\mathcal{V}}=\mathcal{L}_{\text{prog}}+\mathcal{L}_{\text{TD}}$ to leverage both the learning stability and error sensitivity provided by two terms, respectively.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Policy Warm-up on Real-world Experience", "weight": 1.0} -->

Before performing the on-policy improvement, we first warm-start the learning process with offline-collected data, which anchors the policy to a physically plausible behavior distribution on the targeted task, avoiding careless exploration in the later stage. Both data composition and training objective mainly follow RECAP. For each task, we fine-tune the pre-trained policy, *i.e.*, $\pi_{0.5}$, on offline collected data, comprising expert demonstrations, policy rollout with success and failure, and human-intervened correction. During training, the policy is conditioned on an advantage signal, labeled by our learned value model $\mathcal{V}$ as in Eq. 2, by treating $\hat{o}_{t+k}$ as later frames from an offline recorded video. Different from the practice in RECAP that labels advantage for offline data and policy rollout, in early experiments, we found that assigning advantages for both sources yields worse results than labeling for rollout only.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Policy Warm-up on Real-world Experience", "weight": 1.0} -->

Thereby, only rollout data is assigned the learned advantages whereas both expert and human correction data are directly paired with optimal advantages, denoted as $\mathds{1}{}$, in our experiments. Consequently, this warm-up stage empowers the policy to absorb action data in different qualities, which is critical for the next self-improvement stage that learns from trial-and-error in an online manner.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Policy Warm-up on Real-world Experience", "weight": 1.0} -->

Dynamic Brick Sorting TABLE I: Performance comparisons on real-world tasks. We evaluate success rates and scores across three diverse tasks, ranging from dynamic sorting to precise packing. RISE exhibits superior performance compared to baselines in all scenarios.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-C Self Improving with World Model", "weight": 1.0} -->

With the advantage conditioning capability acquired from the warm-up stage on offline data, we then apply the compositional world model as an interactive simulator to improve the policy. The self-improving loop executes the Rollout stage and Training stage iteratively, as shown in Fig. 5.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-C Self Improving with World Model", "weight": 1.0} -->

Rollout Stage. To start off, we sample an initial state from the warm-up offline dataset. Along with the observation, we additionally prompt the rollout policy $\pi_{\text{rollout}}$ with an optimal advantage $\mathds{1}{}$, to infer an action with positive intent.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-C Self Improving with World Model", "weight": 1.0} -->

Visual history and action proposal are fed into the dynamics model to synthesize the next $H$ visual states. These imagined states are then evaluated by the value model to compute the actual advantage of the proposed action, denoted as $A^{\pi_{\text{rollout}}}(o_{t},\hat{\mathbf{a}}_{t},\ell)$. We define $\mathds{1}{}$ as the prompted advantage for inferring optimal actions, whereas $A^{\pi_{\text{rollout}}}(o_{t},\hat{\mathbf{a}}_{t},\ell)$ denotes the evaluated advantage, reflecting the true utility of the generated action. This advantage is discretized into one of $N$ uniform bins representing the practical advantage of the action in the current state. To broaden the state coverage during the online training process, imagined states would also serve as input for the subsequent rollout. From each offline state, such consecutive interaction would be conducted at most two times, considering the known error accumulation issue of generative video models.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-C Self Improving with World Model", "weight": 1.0} -->

The rollout policy parameters are updated via an Exponential Moving Average (EMA), blended from behavior policy weights. One major difference between RISE and prior approaches that also leverage world model as learning environment is that RISE avoids explicitly simulating terminal states to obtain rewards, yet produces chunk-wise advantage for proposed actions directly.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-C Self Improving with World Model", "weight": 1.0} -->

Training Stage. The on-policy rollout data $\langle o,\hat{a},A\rangle$ form batch samples to optimize the policy. The VLA is trained to minimize the distance between its output and the proposed action $\hat{a}$, given the evaluated advantage $A$ as a condition. This allows the policy to learn from both high-advantage successes and low-advantage failures discovered in imagination. To prevent catastrophic forgetting during exploration, we also mix offline labeled data into the batch data. Both offline and online experiences are leveraged under unified learning objective: which is optimized under generic flow-matching criteria.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-D Implementation Details", "weight": 1.0} -->

World Model Training. The dynamics model goes through two phases. The pre-training stage on Galaxea and Agibot World is conducted on 16 NVIDIA H100 GPUs with a global batch size of 512, taking about seven days. Subsequently, for task-specific fine-tuning, we utilize 8 NVIDIA H100 GPUs with a global batch size of 64, which takes about three days to complete. Parameterized from a pre-trained VLA, the value model is directly fine-tuned on task-specific data, thanks to the robot-centric knowledge inherited from the policy backbone. We apply progress estimate loss only for the first 10k training steps and include TD learning loss additionally for the remaining 40k steps. With a total batch size of 64 on 8 GPUs, the model converges in about one day of training. Importantly, both modules of our world model are only applied during the policy learning phase, thus posing zero inference overhead during real-world policy execution.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-D Implementation Details", "weight": 1.0} -->

Policy Training. The policy warm-up phase largely follows the training procedure of RECAP on an offline collected dataset, where the policy is conditioned on advantage labeled by our learned value model. The following self-improving stage then goes around 10k steps. For both stages, global batch size is 64 on 8 GPUs.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-D Implementation Details", "weight": 1.0} -->

Task-specific Data. Both our world model and policy share the same set of offline data for each task, including expert demonstrations and policy rollouts with success and failure, except that policy learning also consumes a fraction of DAgger data to enrich the recovery mode, similar to RECAP.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Evaluations", "weight": 1.0} -->

We conduct a comprehensive evaluation to investigate the capabilities of RISE. In particular, we focus on the following questions: Comparative Analysis: Does RISE outperform existing mainstream RL and IL methods, particularly in real-world dexterous and long-horizon tasks? Design Choices: How can the world model be effectively integrated into the RL loop, and is each module design essential?

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A Real-world Experimental Setup", "weight": 1.0} -->

Our real-world experiments employ a dual 7-DoF AgileX robot with absolute joint control. We benchmark three dexterous, long-horizon tasks, including: Dynamic Brick Sorting: The robot is required to sort diverse bricks dynamically on an operating conveyor belt, shown in Fig. 2(a), Backpack Packing: This task presents challenges involving compliant and deformable object manipulation as in Fig. 2(b). Box Closing The task requires precise bi-manual coordination to package a cup, as in Fig. 2(c). Notably, ablations are conducted on the most challenging task in practice, *i.e.*, Dynamic Brick Sorting. Hyperparameters remain fixed across variants. Detailed robot setup and evaluation metrics are included in the Appendix.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Main Results", "weight": 1.0} -->

Baselines. We benchmark RISE against state-of-the-art imitation and reinforcement learning baselines. Each counterpart is developed with a close compute budget. Implementation and data composition for each variant are detailed in the Appendix. $\pi_{0.5}$: A state-of-the-art VLA pre-trained on web-scale multi-robot data and fine-tuned on task demonstrations. $\pi_{0.5}$ + DAgger: An interactive baseline utilizing on-policy human corrections to mitigate exposure bias. $\pi_{0.5}$ + PPO: A standard online RL baseline fine-tuning VLA weights via PPO. $\pi_{0.5}$ + DSRL: A sample-efficient method steering frozen VLAs by optimizing diffusion latent noise via RL.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B Main Results", "weight": 1.0} -->

RECAP: An advantage-conditioned offline RL approach originally built off a proprietary pre-trained policy, *i.e.*, $\pi_{0.6}$. Due to the inaccessibility of $\pi_{0.6}$, we apply this approach to $\pi_{0.5}$ upon the same parameter-tuning and offline data corpora as ours.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B Main Results", "weight": 1.0} -->

Results. We present quantitative results in Table I, reporting both Success Rate and Stage-wise Score, with evaluation criteria provided in the Appendix. Although $\pi_{0.5}$ offers preliminary capability, we observe that online adaptation (PPO, DSRL) incurs severe instability. This leads to performance degradation, *e.g.*, a sharp drop (35%$\to$ 10%) in the Dynamic Brick Sorting task. RECAP validates the benefit of advantage conditioning but falls short of RISE. Notably, our method yields a 40% margin in Backpack Packing, while increasing success rates to 85% and 95% on the brick and box tasks, respectively. Overall, RISE significantly outperforms all RL and IL baselines across all tasks, with consistently high success rate.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-C Ablation Study", "weight": 1.0} -->

What ratio of the offline data should be allocated during RL training? Relying solely on online experience often leads to performance collapse due to the distribution shift between offline demonstrations and online rollouts. To address this, we investigate the optimal mixing ratio of offline data to retain performance. As shown in Table II, we observe a distinct trade-off. When the offline data ratio is too low (*e.g.*, $0.1$), the success rate plummets to $5\%$. This confirms our hypothesis that insufficient offline retention leads to catastrophic forgetting in the face of massive online data. Conversely, an excessive ratio (*e.g.*, $0.9$) also degrades performance. We attribute this to over-regularization, where the policy becomes too constrained to the offline distribution, hindering its ability to explore and discover superior policies.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-C Ablation Study", "weight": 1.0} -->

Can VLA models benefit from world-model generated online actions or states? To validate this, we evaluate three variants: a baseline without online signals, one with online actions only, and the full RISE with both. Our results confirm the necessity of online signals. As shown in Table III, introducing online actions increases the success rate from $35\%$ to $40\%$. We attribute this improvement to the expanded action space exploration; unlike the static behavioral mode typically found in offline data, online rollouts allow the VLA to distinguish between high-advantage actions and suboptimal failures. Crucially, incorporating online states further raises the success rate to $70\%$. This suggests that dynamically generated online states provide a richer, virtually unbounded training distribution, overcoming the limitations of fixed offline datasets.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C Ablation Study", "weight": 1.0} -->

Experiment #1: Fine-tuning on our real world tasks Experiment #2: Fine-tuning on Bridge dataset TABLE V: Quantitative comparison of dynamics models. ↑ (↓) denotes higher (lower) is better. Our method shows superior motion accuracy (EPE) and perceptual quality across both real-world tasks in Fig. 2 and the Bridge dataset.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-C Ablation Study", "weight": 1.0} -->

How significant is the impact of the modules on RISE? Quantitative results in Table IV highlight the criticality of each component. In the dynamics model, removing visual pre-training drops sorting accuracy by 32.15% and completion to 15%, underscoring the need for visual priors. Absence of task-centric design reduces completion by 30%, validating the filtering of distractions. For the value model, ablating progress regression lowers success by 20%, confirming the importance of dense signals. Furthermore, omitting TD learning leads to a 35% decline, demonstrating its role in robust estimation.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-C Ablation Study", "weight": 1.0} -->

How reliable is the dynamics model? We compare RISE with Cosmos and Genie Envisioner (GE) to investigate the reliability. We evaluate generation quality using PSNR, SSIM, LPIPS, and FVD, alongside optical flow end-point error (EPE) for action controllability. Quantitatively, Table V underscores the superiority of RISE across all baselines under identical experimental settings. Notably, the significant reduction in EPE validates our task-centric pre-training, confirming that prioritizing action-conditioned dynamics effectively enhances motion awareness beyond standard pixel-level reconstruction. Qualitatively (Fig. 6), while baselines suffer from blurring and kinematic inconsistencies, RISE generates physically plausible dynamics with high fidelity. Additional comparisons are provided in the Appendix.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-A World Models for Robot Learning", "weight": 1.0} -->

World models have been envisioned as a pathway to enable effective planning and learning through internal imagination. Early approaches in robotics and control focused on abstract state modeling in latent space with low-capacity dynamics model, which are limited in capturing the rich visual and contact dynamics required for real-world manipulation. Recent advances in large-scale generative modeling renewed world modeling in high-fidelity observation space. However, adapting such models to serve as interactive environments for reinforcement learning remains challenging. Most approaches prioritize visual plausibility over action controllability, incurring prohibitive inference costs that prevent their use inside a reinforcement learning loop. Beyond dynamics prediction, reward and value shaping also introduce an additional bottleneck to apply these models to policy improvement. Prior efforts heavily rely on sparse terminal rewards or heuristic distance towards the goal state, which provide insufficient guidance for long-horizon manipulation and are brittle under long-term prediction errors. Importantly, prior works center around either simulated benchmarks, low-level control problems, or short-term tasks (*e.g.*, pick and place), with limited validation in real-world tasks under contact-rich and complex dynamics.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-A World Models for Robot Learning", "weight": 1.0} -->

Motivated by prior efforts that carefully integrate heterogeneous modules to tackle the challenging world modeling problem, we seamlessly compose a dynamics model and a value function to achieve faithful simulation for various actions.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-B Reinforcement Learning for Foundation Policies", "weight": 1.0} -->

Reinforcement learning is increasingly used to strengthen VLA foundation policies on robustness and precision of manipulation. A large body of work adapts VLA post-training with RL within simulated environments, where interactions are cheap, resettable, and parallelizable. However, such scalability does not hold in the physical world, where interactions are serial, slow, and labor-intensive. Thereby, prior work on real-world RL is constrained to heavily reuse off-policy data while online interactions are performed on limited robot hardware only, which potentially bottlenecks the policy improvement and is hard to scale. Regarding learning stability, some work proposes to freeze the large-scale pre-trained policy while optimizing an additional residual policy or input noise distribution only. With most parameters unchanged, such approaches sacrifice the adaptability of the policy to target tasks. In contrast, RECAP enables finetuning the pre-trained policy via an advantage-conditioned formulation, eliminating the complexity of adjusting the denoising chain for diffusion or flow-matching policy. To derive reliable advantages for policy optimization, recent works resort to vision language models with a progress estimate formulation, which is numerically stable and free from laborious annotations.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-B Reinforcement Learning for Foundation Policies", "weight": 1.0} -->

However, such an objective is prone to the over-fitting problem and is less sensitive to subtle failures. Distinguished from prior approaches, we enable on-policy RL by shifting the learning environment from the physical world into an imaginative space via a learned world model. Furthermore, our value model benefits from both progress estimate and Temporal-Difference learning in stability and failure sensitivity.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced RISE, a framework for on-policy reinforcement learning of robot foundation policies through imagination. RISE replaces the physical environment with imagination during training, enabling scalable online improvement without the prohibitive cost and risk of real-world exploration. Central to the system is a compositional world model that coherently orchestrates dynamics and value models, built from proper recipes, to efficiently emulate state and estimate advantage for policy improvement. Across real-world tasks spanning dynamic interaction, deformable-object handling, and bi-manual coordination, RISE consistently outperforms strong post-training baselines, proving that world models can be applied as an effective learning environment to improve policy performance on challenging manipulation tasks. We hope this work serves as a reference for the community in exploring scalable self-improving VLA models.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Limitations and future work", "weight": 1.5} -->

The Gap between Imagination and Realism. The effectiveness of RISE is constrained by the accuracy and coverage of the learned world model. Although our compositional design improves controllability and consistency relative to prior generative simulators, the model can still produce physically implausible transitions in rare or underrepresented scenarios. Addressing this gap requires future work on uncertainty-aware imagination and principled integration of physical constraints that explicitly encode geometry properties.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Limitations and future work", "weight": 1.5} -->

The Simulated--Real Data Balance. Our results indicate that a non-trivial amount of real-world data remains essential to anchor the learning procedure. However, the optimal ratio between simulated rollouts and real-world experience requires further parameter tuning. Understanding the effectiveness and principles of these offline data represents an open problem.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Limitations and future work", "weight": 1.5} -->

From Physical Cost to Compute Cost. RISE shifts the primary bottleneck in robot learning from physical interaction to computation. While this trade-off releases the burden of physical interaction, training high-fidelity world models incurs a high computational cost. Improving the efficiency of world models will be critical for the compute-constrained regime.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Limitations and future work", "weight": 1.5} -->

Outlook. Taken together, these limitations suggest a promising pathway in integrating learned simulation into a broader data ecosystem, where model-based reinforcement learning complements scarce physical interaction. Discovering the right balance between these two key components points to a future of adaptive, robust, and sample-efficient robotic intelligence.
