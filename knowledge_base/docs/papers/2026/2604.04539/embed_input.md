<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

FlashSAC: Fast and Stable Off-Policy Reinforcement Learning for High-Dimensional Robot Control

Topics include Reinforcement learning, Robotics, Stability analysis, Supervised learning, Distributed systems, Optimization, Control, Learning, FlashSAC, Proximal policy optimization.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Reinforcement learning (RL) is a core approach for robot control when expert demonstrations are unavailable. On-policy methods such as Proximal Policy Optimization (PPO) are widely used for their stability, but their reliance on narrowly distributed on-policy data limits accurate policy evaluation in high-dimensional state and action spaces. Off-policy methods can overcome this limitation by learning from a broader state-action distribution, yet suffer from slow convergence and instability, as fitting a value function over diverse data requires many gradient updates, causing critic errors to accumulate through bootstrapping. We present FlashSAC, a fast and stable off-policy RL algorithm built on Soft Actor-Critic. Motivated by scaling laws observed in supervised learning, FlashSAC sharply reduces gradient updates while compensating with larger models and higher data throughput. To maintain stability at increased scale, FlashSAC explicitly bounds weight, feature, and gradient norms, curbing critic error accumulation. Across over 60 tasks in 10 simulators, FlashSAC consistently outperforms PPO and strong off-policy baselines in both final performance and training efficiency, with the largest gains on high-dimensional tasks such as dexterous manipulation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In sim-to-real humanoid locomotion, FlashSAC reduces training time from hours to minutes, demonstrating the promise of off-policy RL for sim-to-real transfer.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The long-standing goal of robot learning is to develop agents that generalize across a wide range of tasks in the real world. While large-scale imitation learning from real-world data has recently yielded impressive results in robotic control, reinforcement learning (RL) from simulation remains a core paradigm when expert demonstrations are unavailable, incomplete, or insufficient.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To date, sim-to-real RL has been most successful in relatively constrained domains such as quadruped locomotion and gripper-based manipulation, which are characterized by low-dimensional state--action spaces and extremely high-throughput simulators. In this regime, on-policy methods such as Proximal Policy Optimization (PPO) have proven effective: PPO is stable, easy to tune, and its data inefficiency is acceptable when fresh on-policy data can be collected cheaply.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, this regime is becoming less representative of modern robot learning. Emerging applications---including humanoid locomotion, dexterous manipulation, and vision-based control ---involve much higher-dimensional state and action spaces, where policy evaluation and improvement from narrowly distributed on-policy data become substantially harder. Simultaneously, simulation grows increasingly expensive due to complex contact dynamics, and larger policy architectures further raise rollout costs. In this setting, repeatedly discarding past experience in favor of freshly collected data becomes increasingly inefficient in both sample complexity and wall-clock time.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Off-policy RL offers a natural alternative. By reusing diverse experience from a replay buffer, off-policy methods can achieve substantially higher data efficiency than on-policy approaches. This advantage is particularly appealing in high-dimensional robotic tasks, where broader data coverage can support better policy evaluation and improvement. Yet despite this promise, off-policy RL has not become the default choice for sim-to-real transfer, as it often suffers from slow training and instability.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A central challenge is learning an accurate value function from broad replay data. Off-policy methods train a critic $Q_{\theta}$ by minimizing a bootstrapped Bellman objective, where transitions $(s,a,r,s^{\prime})$ are sampled from a replay buffer $\mathcal{D}$ and $a^{\prime}\sim\pi(\cdot\mid s^{\prime})$. In high-dimensional settings, fitting this critic accurately over diverse replay data often requires many gradient updates, which not only increases training time but also compounds estimation errors through repeated bootstrapping, as the critic is optimized toward targets that depend on its own predictions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we present FlashSAC, a fast and stable off-policy RL algorithm built on Soft Actor-Critic. Motivated by scaling trends in supervised learning, FlashSAC sharply reduces the number of gradient updates while compensating with larger models and higher data throughput, improving training efficiency and better matching modern large-scale simulation pipelines. However, larger critics can further exacerbate instability under bootstrapping. To maintain stability, FlashSAC explicitly controls critic update dynamics by bounding weight, feature, and gradient norms, thereby preventing the accumulation of critic errors.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate FlashSAC on more than 60 locomotion and manipulation tasks across 10 simulators, spanning high-dimensional state-based control, vision-based control, and sim-to-real humanoid locomotion. Across this benchmark suite, FlashSAC consistently outperforms PPO and strong off-policy baselines in both final performance and training efficiency, with the largest gains on the most challenging tasks such as dexterous manipulation and humanoid locomotion. In sim-to-real humanoid walking, FlashSAC reduces training time from hours to minutes while maintaining stable real-world deployment, demonstrating that off-policy RL can be both fast and stable for scalable sim-to-real robot learning.

<!-- chunk {"id": "body-0011", "role": "body", "section": "On-Policy Reinforcement Learning", "weight": 1.0} -->

On-policy RL has been the dominant paradigm for simulation-based robot learning when environment interaction is cheap and massively parallelizable. Among on-policy methods, PPO is particularly popular for its stability, ease of implementation, and robustness to hyperparameter choices. Combined with modern high-throughput simulators, PPO has enabled successful sim-to-real transfer in relatively constrained domains such as quadruped locomotion and rigid-body manipulation. Its widespread adoption has motivated a line of work improving upon it, such as stronger trust-region guarantees, better exploration via expanding action space, and lower gradient variance via pathwise estimates.

<!-- chunk {"id": "body-0012", "role": "body", "section": "On-Policy Reinforcement Learning", "weight": 1.0} -->

However, on-policy methods fundamentally rely on freshly collected data and discard experience generated by earlier policies. As task dimensionality increases, achieving sufficient state--action coverage via on-policy rollouts becomes increasingly expensive. While importance sampling can, in principle, correct for policy mismatch and enable data reuse, importance weights in high-dimensional continuous action spaces exhibit extremely high variance, rendering this strategy impractical in modern robotic learning.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Off-Policy Reinforcement Learning", "weight": 1.0} -->

Off-policy RL decouples data collection from policy optimization by storing transitions in a replay buffer and reusing them across updates. This is especially appealing in high-dimensional robotic tasks, where diverse experience supports better policy evaluation than narrowly distributed on-policy rollouts.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Off-Policy Model-Based RL", "weight": 1.0} -->

Model-based RL further improves sample efficiency by learning environment dynamics and using them for planning or imagined rollouts. Recent approaches such as DreamerV3 and TD-MPC2 have demonstrated strong performance in vision-based domains by planning in learned latent spaces. However, learning accurate dynamics models and performing repeated planning procedures significantly increases per-step training cost, often limiting their scalability in wall-clock critical settings.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Off-Policy Model-Free RL", "weight": 1.0} -->

Model-free off-policy algorithms such as DDPG, TD3, and SAC learn policies and value functions directly from replayed experience without explicit dynamics models. Their simplicity and data reuse make them attractive for robotic control. However, as discussed in Section 1, off-policy model-free RL suffers from three persistent challenges: *slow training*, *unstable training dynamics*, and *exploration in high-dimensional action spaces*. The first two challenges stem from the bootstrapped Bellman objective illustrated in Equation 1: fitting a critic over diverse replay data in high-dimensional state-action spaces requires many gradient updates, directly increasing training time. Because critic targets depend on the critic's own predictions, approximation and extrapolation errors at poorly supported state-action pairs compound across updates. The third arises because the maximum-entropy formulation of SAC alone is often insufficient to maintain coherent exploration in high-dimensional action spaces, motivating dedicated noise mechanisms and exploration schemes.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Off-Policy Model-Free RL", "weight": 1.0} -->

Prior work has primarily addressed each challenge in isolation. To improve *speed*, one line of work scales data throughput via parallel simulation and large replay buffers. For example, FastTD3 and FastSAC achieve strong wall-clock efficiency in humanoid locomotion but relies on small networks (${\sim}$`<!-- -->`{=html}0.2M parameters), which limits its asymptotic performance. Scaling to larger networks is difficult in this setting, as increased model capacity exacerbates instability under bootstrapped training.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Off-Policy Model-Free RL", "weight": 1.0} -->

To improve *stability*, a second line of work constrains value-function sensitivity by bounding feature, weight, and gradient norms, or by other measures such as reinitialization, distillation, ensembling, and alternative critic target networks. These constraints limit error amplification under distribution shift and repeated bootstrapping, enabling training with larger networks that achieve higher asymptotic performance. However, the increased model capacity requires more gradient updates to converge, resulting in slower training in data-rich simulation regimes.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Off-Policy Model-Free RL", "weight": 1.0} -->

To improve *exploration*, a third line of work exploits off-policy RL's ability to decouple data collection from policy optimization, injecting temporally-correlated action noise to obtain coherent trajectories such as Ornstein--Uhlenbeck processes, pink noise, parameter-space noise, state-dependent exploration, and temporally-extended action repetition. However, exploration mechanisms alone leave the bottlenecks of slow and unstable training untouched, limiting their impact as model capacity and data throughput scale.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Off-Policy Model-Free RL", "weight": 1.0} -->

FlashSAC unifies these directions: it achieves fast training by sharply reducing gradient updates while scaling model capacity and data throughput, maintains stable training dynamics by jointly bounding weight, feature, and gradient norms, and adopts a lightweight noise-repetition scheme that produces temporally-correlated exploration without per-environment overhead.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Preliminary", "weight": 1.0} -->

In this section, we introduce the RL framework and algorithmic foundation upon which FlashSAC is built.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Markov Decision Process (MDP)", "weight": 1.0} -->

We model robotic control as a discounted Markov Decision Process (MDP), $\mathcal{M}=(\mathcal{S},\mathcal{A},P,r,\gamma)$, where $\mathcal{S}$ denotes the state space, $\mathcal{A}$ denotes the continuous action space, $P(s^{\prime}|s,a)$ denotes the transition dynamics, $r(s,a)$ denotes the reward function, and $\gamma\in0,1)$ is the discount factor.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Markov Decision Process (MDP)", "weight": 1.0} -->

At each timestep $t$, the agent observes $s_{t}\in\mathcal{S}$, samples an action $a_{t}\in\mathcal{A}$, receives a reward $r_{t}=r(s_{t},a_{t})$, and transitions to the next state $s_{t+1}\sim P(\cdot\mid s_{t},a_{t})$. The goal is to learn a policy $\pi(a|s)$ that maximizes the discounted sum of rewards.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Soft Actor Critic (SAC)", "weight": 1.0} -->

FlashSAC builds upon SAC \[, a widely used off-policy RL algorithm. SAC stores transitions $(s,a,r,s^{\prime})$ collected under past policies in a replay buffer $\mathcal{D}$, and trains the policy using samples drawn from this buffer.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Soft Actor Critic (SAC)", "weight": 1.0} -->

Beyond maximizing expected return, SAC incorporates an entropy regularization term that encourages exploration. This entropy maximization is particularly important in high-dimensional state--action spaces, where insufficient exploration can lead to poor coverage of the replay buffer and exacerbate approximation and extrapolation errors.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Soft Actor Critic (SAC)", "weight": 1.0} -->

To reduce approximation errors in bootstrapped value learning, SAC commonly employs clipped double Q-learning, maintaining two action-value functions $Q_{\phi_{1}}(s,a)$ and $Q_{\phi_{2}}(s,a)$. The minimum of the two estimates is used when forming targets, reducing the impact of optimistic value errors.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Soft Actor Critic (SAC)", "weight": 1.0} -->

Concretely, the policy $\pi_{\theta}(a|s)$ is optimized by minimizing where $\alpha>0$ controls the relative importance of entropy.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Soft Actor Critic (SAC)", "weight": 1.0} -->

Each critic is trained by minimizing a bootstrapped Bellman error using slowly updated target networks $\bar{\phi}_{1}$ and $\bar{\phi}_{2}$, which are updated via exponential moving average: where $\tau\in$ is the target update rate.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Soft Actor Critic (SAC)", "weight": 1.0} -->

For $i\in\{1,2\}$, the critic weights $\phi_{i}$ are optimized by minimizing the Bellman loss where the target value is

<!-- chunk {"id": "body-0029", "role": "body", "section": "FlashSAC", "weight": 1.0} -->

FlashSAC is a fast and stable off-policy RL algorithm for high-dimensional robotic control. It achieves strong asymptotic performance with fast wall-clock time through three complementary mechanisms: (i) fast training by scaling data and model while reducing gradient updates (§4.1), (ii) stable training by constraining critic update dynamics (§4.2), and (iii) broad exploration for diverse data coverage (§4.3).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Fast Training", "weight": 1.0} -->

On-policy methods such as PPO discard all collected data after each iteration. In high-dimensional robotic tasks where simulation is expensive, this data inefficiency becomes a critical bottleneck. Off-policy RL reuses past experience from a replay buffer, but conventionally requires many gradient updates per transition to extract sufficient learning signal, which slows wall-clock time and compounds bootstrapping errors.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Fast Training", "weight": 1.0} -->

FlashSAC takes a different approach inspired by the scaling trends observed in supervised learning: under a fixed compute budget, larger models trained with larger batches and fewer updates converge faster than smaller models with frequent updates. This principle has been difficult to apply in off-policy RL, because increased model capacity tends to amplify critic instability under bootstrapping. FlashSAC resolves this tension by stabilizing critic training through constrained update dynamics (§4.2), enabling a regime of high data throughput, large models, and infrequent gradient updates.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Massively Parallel Simulation", "weight": 1.0} -->

We collect data using $1024$ parallel simulation environments, enabling rapid accumulation of diverse trajectories. While many off-policy RL setups rely on a small number of environments, high-throughput data collection is critical for maintaining adequate coverage of the state-action space in high-dimensional tasks.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Large-Capacity Replay Buffer", "weight": 1.0} -->

FlashSAC uses a replay buffer of up to 10M transitions, an order of magnitude larger than the 1M commonly used in standard off-policy configurations. In high-dimensional tasks, rare but important state-action pairs can be easily overwritten in smaller buffers, leading to catastrophic forgetting and inducing extrapolation error. A larger buffer preserves such long-tail experiences and maintains the diversity of training data available to the critic throughout learning.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Large Model, Large Batch, Fewer Updates", "weight": 1.0} -->

Standard off-policy RL baselines use small MLPs (0.2-0.5M parameters, 2-3 layers) to avoid instability. In contrast, FlashSAC employs a 2.5M-parameter, 6-layer network for both the actor and critic, paired with a batch size of 2048 that nearly saturates GPU utilization. The updates-to-data ratio is set to 2/1024, meaning only 2 gradient updates are performed per 1024 new transitions. Although such infrequent updates are typically ineffective in off-policy RL, the combination of large batches, higher learning rates, and increased model capacity enables fast convergence with fewer updates.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Code Optimization", "weight": 1.0} -->

FlashSAC is implemented in PyTorch, with both training and inference JIT-compiled to minimize Python overhead. We use mixed-precision throughout training, which reduces wall-clock time by 5-10%.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Stable Training", "weight": 1.0} -->

Scaling data and model accelerates training but does not prevent instability arising from bootstrapped critic updates. In the Bellman backup, estimation errors at next-state action pairs propagate into the current Q-value targets and can be recursively amplified through repeated updates. This problem worsens with both state-action dimensionality and model capacity, making stability a prerequisite for scaling. FlashSAC addresses this by constraining weight, feature, and gradient norms throughout training via the following mechanisms.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Inverted Residual Backbone", "weight": 1.0} -->

The backbone stacks inverted residual blocks inspired by the Transformer feedforward block (Figure 2). Each block expands features to a higher dimension via an inverted bottleneck, projects back to the original dimension, and adds a residual connection to stabilize gradient propagation. After the final block, we apply RMSNorm to bound per-sample feature norms before value heads, preventing out-of-distribution inputs from producing unbounded activations that destabilize bootstrapping.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Pre-activation Batch Normalization", "weight": 1.0} -->

Replay data is collected by a mixture of evolving policies, inducing non-stationary input distributions. Without normalization, feature activations can saturate (e.g., dead ReLUs ), degrading gradient flow. We apply batch normalization before each nonlinearity to keep activations well-scaled. We choose batch normalization over layer normalization because it exploits large-batch statistics from diverse replay data, yielding a smoother loss landscape with a lower effective condition number.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Cross-Batch Value Prediction", "weight": 1.0} -->

Batch normalization computes statistics per batch, so the predicted Q-values and target Q-values receive different normalization when computed in separate forward passes. Following, we concatenate current and next-state transitions into a single batch so that both share the same statistics, ensuring consistency in the Bellman update.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Distributional Critic with Adaptive Reward Scaling", "weight": 1.0} -->

Following, we represent the Q-value as a categorical distribution over $n_{\text{atom}}$ atoms uniformly spaced on $[G_{\min},G_{\max}]$. The network predicts atom probabilities and is trained via cross-entropy loss against the projected Bellman target. This distributional formulation smooths the optimization landscape and reduces sensitivity to noisy targets.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Distributional Critic with Adaptive Reward Scaling", "weight": 1.0} -->

To keep returns within the distributional critic's fixed support, we normalize rewards directly rather than centering returns or scaling losses. We track the running discounted return variance $\sigma^{2}_{t,G}$ and maximum magnitude $G_{t,\max}$, and scale as: This bounds effective returns while maintaining a consistent scale throughout training.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Weight Normalization", "weight": 1.0} -->

Uncontrolled weight growth increases Q-value variance and amplifies estimation errors under bootstrapping. After each gradient step, we project each weight vector onto the unit-norm sphere and each normalization parameter vector $(\gamma,\beta)$ to norm $\sqrt{d}$. This constrains the network to encode information through direction rather than scale.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Exploration", "weight": 1.0} -->

Off-policy RL can decouple data collection from policy optimization, allowing exploration strategies that pursue broad state-action coverage independently of the current policy. FlashSAC employs two complementary mechanisms.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Unified Entropy Target", "weight": 1.0} -->

Maximum-entropy RL with automatic temperature tuning encourages sustained exploration, but requires specifying a target entropy. Standard practice sets this target per task, which is impractical across embodiments with varying action dimensions. We instead parameterize the target entropy via a fixed action standard deviation $\sigma_{\text{tgt}}$. For a Gaussian policy with diagonal covariance, this gives: which scales linearly with action dimension, ensuring consistent exploration across embodiments without per-task tuning. We set $\sigma_{\text{tgt}}=0.15$ in all experiments.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Noise Repetition", "weight": 1.0} -->

Temporally correlated action noise is commonly used to improve exploration in sparse-reward settings, with pink noise and Ornstein--Uhlenbeck noise being widely used. However, these methods are ill-suited to massively parallel simulations, as they require per-environment correlated-noise processes, which incur substantial computational and memory overhead.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Noise Repetition", "weight": 1.0} -->

We propose *Noise Repetition*, a lightweight alternative that induces temporal correlation using minimal local state. At each repetition interval, a noise vector $\epsilon\sim\mathcal{N}(0,I)$ is sampled for action selection and held constant for $k$ consecutive steps. The repetition length $k$ is drawn from a Zeta distribution with probability mass function $P(k)\propto k^{-s}$, favoring short repeat intervals while occasionally producing long, correlated action sequences.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate FlashSAC on a diverse suite of robotic control tasks, measuring both asymptotic performance and wall-clock time (measured on a single RTX 5090 GPU). Our experiments span low- and high-dimensional state-based control, vision-based control, and sim-to-real humanoid locomotion.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

We evaluate on 25 state-based control tasks drawn from four GPU-based simulators: IsaacLab, MuJoCo Playground, ManiSkill3, and Genesis, all of which enable large-scale sample collection at minimal wall-clock cost.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

The tasks span a wide range of state--action dimensionalities: Low-dim (15 tasks): Gripper-based manipulation (Franka) and quadruped locomotion (AnyMal-C/D, Unitree Go2).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

High-dim (10 tasks): Dexterous manipulation (Allegro, Shadow Hand) and humanoid locomotion (Unitree G1, H1, Booster T1).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

We compare FlashSAC against strong, widely adopted baselines: PPO: A highly optimized on-policy implementation from RSL-RL, representative of current best practices in sim-to-real robotic RL.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

FastTD3: A wall-clock--optimized off-policy method designed for high throughput simulations.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Whenever available, we report published results; otherwise, we reproduce results using official implementations.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Off-policy methods (FlashSAC and FastTD3) are trained for 50M environment steps. To probe asymptotic performance, PPO is trained for 200M steps, requiring approximately $3\times$ the compute of FlashSAC. While baseline methods use task-specific hyperparameter tuning, FlashSAC is evaluated using a single unified configuration across all tasks, varying only the discount factor $\gamma$ to match simulator defaults (e.g., $0.99$ for IsaacLab, $0.97$ for Playground).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

On low-dimensional tasks, FlashSAC slightly outperforms PPO (Figure 3.a). As consistent with prior findings, on-policy methods remain effective when state--action spaces are small, and simulation throughput is high enough to collect a large volume of samples.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

On high-dimensional tasks, FlashSAC demonstrates a clear and consistent advantage (Figure 3.b). Across dexterous manipulation and humanoid locomotion benchmarks, FlashSAC converges reliably to higher asymptotic performance while requiring substantially less wall-clock time than PPO.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

Compared to FastTD3, FlashSAC is markedly more stable, converging across all tasks where FastTD3 frequently fails or underperforms (e.g., Go2Walk, Franka Pull Cube). When both methods converge, FlashSAC achieves higher asymptotic performance, with the largest gains observed in humanoid locomotion, where larger model capacity is particularly beneficial.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

We further evaluate FlashSAC on 40 single-environment, CPU-based continuous-control tasks drawn from four established benchmarks: MuJoCo, DeepMind Control Suite, MyoSuite, and HumanoidBench. Unlike GPU-based simulators, these benchmarks use a single environment instance, placing greater emphasis on sample efficiency rather than wall-clock throughput.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

We compare FlashSAC against strong sample-efficient baselines: PPO: A highly optimized on-policy implementation from RSL-RL, included to assess whether on-policy methods remain viable in the low-sample regime.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

XQC: A recent off-policy method coupled with batch-normalization designed for high sample efficiency.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

SimbaV2: An improved variant of Simba for stable off-policy learning.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

TD-MPC2: A model-based method that combines off-policy RL with model-predictive planning.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

MR.Q: A recent model-free method using a model-based objective for better representation learning.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

As in the GPU-based setting, FlashSAC uses a single unified configuration across all tasks, with only minimal adjustments to match each benchmark's conventions. Since sample collection is considerably slower with a single environment, the CPU-based configuration differs from the GPU setting by reducing the batch size from 2048 to 512 and setting the update-to-data ratio to 1, reflecting the lower data throughput.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

As illustrated in Figure 5.2, FlashSAC consistently outperforms all baselines across representative tasks in this sample-efficient regime. Full per-task results appear in § 12. PPO performs particularly poorly here, as on-policy methods cannot reuse experience and thus suffer under limited sample budgets.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

These results confirm that the design choices in FlashSAC generalize beyond massively parallel GPU-based simulation: even in the classical single-environment setting, where sample efficiency is the primary bottleneck, FlashSAC matches or exceeds dedicated sample-efficient methods without task-specific tuning.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

We extend our evaluation to vision-based control, where high rendering cost and low environment throughput severely limit the number of transitions collected per unit time, making data efficiency critical. We evaluate on 8 tasks from the DMControl Suite, spanning manipulation and mono/bi-pedal locomotion. A complete task list is provided in § 9.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Given the low throughput of visual environments, we focus on off-policy baselines: DrQ-v2: A DDPG-based method that improves data efficiency through image augmentation.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

MR.Q: An off-policy method that incorporates a dynamics modeling objective to improve representation learning.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

As in the CPU-based state experiments (§ 5.2), sample collection is slow; we reuse the same hyperparameters from that setup, adapting only the following to match the standard DrQ-v2 configuration: (i) a lightweight convolutional encoder (3 convolutional layers followed by a linear bottleneck), (ii) frame stacking of the three most recent frames (84 × 84 × 9) for temporal reasoning without recurrent architectures, and (iii) 3-step returns for better credit assignment. All methods are trained for 1M environment steps with an action repeat of 2. Full details are in § 9.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

We note that the stabilization techniques in FlashSAC are orthogonal to such extensions; for example, MR.Q's representation learning objective could be layered on top for further gains in visual feature learning.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Sim-to-Real Transfer", "weight": 1.0} -->

Off-policy RL is often regarded as unreliable for sim-to-real transfer, particularly in high-dimensional systems, where training instability can lead to unsafe behaviors. We evaluate whether FlashSAC enables reliable sim-to-real transfer on a challenging 29-DoF Unitree G1 humanoid performing blind locomotion.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

We train blind locomotion policies in simulation using a terrain curriculum comprising pyramid stairs, discrete grids, waves, and pits. The curriculum consists of 10 terrain levels with stair heights ranging from 0 to 23cm (step width 32cm, platform width 3m). Terrain difficulty is increased automatically using a game-inspired curriculum. To facilitate sim-to-real transfer, we apply large-scale domain randomization alongside the terrain curriculum; full details are provided in § 11.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

As a baseline, we use PPO with the sim-to-real pipeline of. FlashSAC adopts the same sim-to-real adaptation techniques for a fair comparison. Both methods use implicit system identification via a context estimator and an asymmetric actor--critic formulation, where the critic receives privileged information (e.g., contact states and height maps) during training. Both methods share identical reward design and coefficients, combining velocity tracking with regularization terms penalizing foot slip, excessive torque, action discontinuities, and orientation instability. FlashSAC uses the same architecture and hyperparameters as in the state-based experiments 5.2.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

On flat terrain (Figure 1.(c)), FlashSAC achieves stable real-world locomotion after approximately 20 minutes of training, whereas PPO requires about 3 hours to reach comparable performance. The learned policy supports omnidirectional locomotion (forward, backward, and lateral) without re-training.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

The advantage of FlashSAC is more pronounced on rough terrain (Figure 6). In the real-world setup, the robot faces stairs of 15cm height, 60cm width, and 1.5m platform width---conditions unseen during training, which uses different stair dimensions. FlashSAC successfully climbs these stairs after approximately 4 hours of training, while PPO requires nearly 20 hours to achieve a similar capability.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

Overall, FlashSAC reduces the training time for sim-to-real humanoid locomotion by nearly an order of magnitude compared to PPO while maintaining stable and safe behaviors.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Analysis", "weight": 1.0} -->

In this section, we analyze the factors underlying FlashSAC's performance across four aspects. We first examine how off-policy learning yields broader state--action coverage than on-policy methods (§6.1). We then investigate three design choices central to FlashSAC: scaling data collection and model capacity for faster training (§6.2), architectural ablations that improve training stability (§6.3), and the effect of entropy and temporal correlation on exploration (§6.4). All experiments are conducted in four IsaacLab environments: cube reorientation with the Allegro and Shadow Hands, and flat and rough terrain locomotion with the G1.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Off-Policy vs On-Policy", "weight": 1.0} -->

We train FlashSAC for 1M steps on the IsaacLab Shadow Hand task with a replay buffer of size 1M, then collect 1M additional on-policy transitions by rolling out the final policy.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Scaling Ablation for Faster Training", "weight": 1.0} -->

We study how scaling data, model capacity, and reducing the number of gradient updates (§4.1) affects the compute efficiency of FlashSAC. We perform univariate ablations over five hyperparameters: batch size, replay buffer size, network width, network depth, and update-to-data (UTD) ratio.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Scaling Ablation for Faster Training", "weight": 1.0} -->

Figures 8.(b)--(e) exhibit trends consistent with established scaling laws: increasing batch size and model capacity, along with reducing the UTD ratio, accelerate convergence. Most existing off-policy RL methods rely on small architectures for training stability (e.g., width 128 with inverted bottlenecks and block depth 1), which limits convergence speed. The scaling mechanisms of FlashSAC enable higher-capacity models, resulting in substantially faster convergence.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Architectural Ablation for Stable Training", "weight": 1.0} -->

We analyze the contribution of each architectural component in FlashSAC (§4.2) to determine whether the proposed design stabilizes training. Beyond final task performance, we measure parameter, feature, and gradient norms throughout training as indicators of optimization stability. Following, we also measure the condition number of the critic loss landscape, where larger values correspond to poorly conditioned updates that can exacerbate critic error amplification.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Architectural Ablation for Stable Training", "weight": 1.0} -->

Starting from a standard MLP critic, we incrementally add: Residual Blocks, Batch Normalization, Post RMSNorm, Distributional Critics with Reward Scaling, and Weight Normalization. Figure 9 summarizes the results. As components are added, parameter, feature, and gradient norms remain bounded throughout training with no uncontrolled growth, indicating well-behaved critic updates and reduced error amplification. The condition number also decreases monotonically, reaching its lowest value with the full FlashSAC architecture.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Architectural Ablation for Stable Training", "weight": 1.0} -->

These gains in optimization stability directly translate to improved task performance (Figure 9.(a)), underscoring the importance of controlling update dynamics in off-policy RL. While weight normalization alone yields modest gains, it improves robustness in sample-limited regimes and is therefore retained in the final design.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Exploration Ablation", "weight": 1.0} -->

We analyze FlashSAC's exploration strategy (§4.3): unifying the entropy target $\sigma_{tgt}$ and noise repetition.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Lessons and Opportunities", "weight": 1.0} -->

We presented FlashSAC, a fast and stable off-policy RL framework for high-dimensional robotics. As the robotics community moves toward high-dimensional, perception-rich, and contact-intensive tasks, the scalability of on-policy RL becomes increasingly constrained. Off-policy RL is an appealing alternative, but its adoption has been limited by slow training speed and instability in critic learning arising from function approximation error and bootstrapped updates. FlashSAC addresses these challenges through two complementary mechanisms: scaling data and model capacity while reducing the number of gradient updates for faster training, and integrating explicit architectural constraints on critic updates for stable optimization. Together, these yield strong asymptotic performance and up to an order-of-magnitude reduction in wall-clock time compared to on-policy methods.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Lessons and Opportunities", "weight": 1.0} -->

Stabilized off-policy learning opens new opportunities for robot learning. Improved data efficiency makes it feasible to train larger policies, incorporate vision and other rich sensory inputs, and leverage slower but more realistic simulators. Off-policy methods also naturally support learning from a mixture of demonstrations and self-collected experience. While this work focuses on state-based control, extending these critic-stabilization principles to tactile-based learning is a promising direction for future work.
