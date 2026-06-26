<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

KIPPO: Koopman-Inspired Proximal Policy Optimization

Topics include Convex optimization, Policy gradients, Reinforcement learning, Stability analysis, Optimization, Control, Learning, KIPPO, Koopman, Proximal policy optimization.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Reinforcement Learning (RL) has made significant strides in various domains, and policy gradient methods like Proximal Policy Optimization (PPO) have gained popularity due to their balance in performance, training stability, and computational efficiency. These methods directly optimize policies through gradient-based updates. However, developing effective control policies for environments with complex and non-linear dynamics remains a challenge. High variance in gradient estimates and non-convex optimization landscapes often lead to unstable learning trajectories. Koopman Operator Theory has emerged as a powerful framework for studying non-linear systems through an infinite-dimensional linear operator that acts on a higher-dimensional space of measurement functions. In contrast with their non-linear counterparts, linear systems are simpler, more predictable, and easier to analyze. In this paper, we present Koopman-Inspired Proximal Policy Optimization (KIPPO), which learns an approximately linear latent-space representation of the underlying system's dynamics while retaining essential features for effective policy learning. This is achieved through a Koopman-approximation auxiliary network that can be added to the baseline policy optimization algorithms without altering the architecture of the core policy or value function.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Extensive experimental results demonstrate consistent improvements over the PPO baseline with 6-60% increased performance while reducing variability by up to 91% when evaluated on various continuous control tasks.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

RL provides a powerful framework for sequential decision-making tasks, enabling agents to learn optimal behaviors through interaction with their environment. Policy optimization, a core component of this framework, determines the optimal mapping from states to actions that maximizes an agent's cumulative returns. Policy gradient methods excel in continuous control tasks by directly optimizing policies through gradient-based updates. However, developing effective control policies for environments with complex and non-linear dynamics remains a challenge. This challenge, combined with non-convex optimization landscapes, leads to high-variance gradient estimates and unstable updates. The optimization process often diverges or oscillates, impeding convergence to optimal policies.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The field of dynamical systems studies mathematical models of evolving processes, focusing on patterns, stability, and long-term behavior Although linear systems are more predictable, many real-world systems are non-linear, where small changes in initial conditions can lead to drastically different outcomes. Koopman Operator Theory, a powerful tool for studying non-linear systems, finds a linearized description in a higher-dimensional space of measurement functions, known as the Koopman observable space. This process maps original state variables to observable functions, extracting useful state information. The Koopman operator, an infinite-dimensional linear operator, evolves these observables linearly in time, enabling linear descriptions of non-linear systems. Data-driven methods like DMD and deep learning advances have enabled approximating the Koopman operator directly from data.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Visualization of \glsentryshort*{KIPPO}'s improvements relative to the \glsentryshort*{PPO} baseline in terms of average performance (mean, higher is better --- left) and consistency (std., lower is better --- right) across four trials per environment.}\label{fig:results\_envs\_main\_percdiff} Building on these foundations, we propose KIPPO, a method that uses Koopman-inspired representation learning to address a key challenge of policy gradient methods like PPO: high-variance gradient estimates in complex, non-linear environments. Rather than seeking perfectly linear representations of non-linear systems, our approach introduces an inductive bias that encourages approximate linearity along policy trajectories. This soft constraint simplifies underlying dynamics while preserving essential features for policy learning. We achieve this through a Koopman-approximation auxiliary network and targeted constraints that balance the complexity of latent dynamics. KIPPO's architecture uses state encoders/decoders and linear transition matrices to predict future states over a fixed horizon, imposing structure on the latent space while minimizing information loss.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

By combining advances in deep learning with Koopman theory principles, this approach simplifies system behavior and improves policy performance.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our approach creates a mutually beneficial feedback loop: policy gradients identify important state space regions through exploratory rollouts, while our linearization technique reduces gradient variance specifically in these critical regions. By focusing linearization efforts locally along policy-explored trajectories instead of attempting global linearization. This targeted approach maintains computational efficiency while delivering benefits precisely where they matter most for the current policy.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

- Koopman-Inspired Policy Optimization. We propose KIPPO, an on-policy algorithm that incorporates Koopman operator principles directly into policy gradient updates. By learning an approximately linear latent-space representation, KIPPOstabilizes gradient estimates and enhances control over non-linear dynamics. - Decoupled Auxiliary Representation Learning. KIPPO adds an auxiliary network to policy gradient baselines like PPO without altering the core policy or value function architecture. This design allows the policy to train on a simpler, encoded state space while the auxiliary network enforces a linear-like structure. As a result, standard PPOhyperparameters and training loops remain largely intact. - Performance and Stability Improvements. Across MuJoCo and Box2D tasks, KIPPO consistently achieves 660% higher mean returns and a 2691% reduction in variance compared to baseline PPO, as shown in Fig.[fig:results\_envs\_main\_percdiff]. These empirical gains attest to the efficacy of Koopman-inspired constraints in mitigating high-variance updates and accelerating convergence.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is organized as follows: [sec:background] presents essential background. Sec.[sec:method] describes the KIPPO framework in detail. Sec.[sec:exp\_res] presents extensive experimental results across multiple environments. Sec.[sec:conclusion]concludes the paper by summarizing our findings and outlining promising directions for future research.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Methodology", "weight": 1.0} -->

The \glsentryshort{KIPPO} framework architecture. The state autoencoder (encoder \(\gls{state-encoder}\) and decoder \(\gls{state-decoder}\)) learns a compact latent representation of environment states. The action encoder \(\gls{action-encoder}\) maps actions to this feature space. Within the latent space, dynamics are governed by the linear state-transition matrix \(\gls{koop-mat-state}\) and control matrix \(\gls{koop-mat-action}\). The policy optimization algorithm operates on the encoded states \(\gls{state-obs}\_t = \gls{state-encoder}(\gls{state}\_t)\).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Methodology", "weight": 1.0} -->

This architecture enables the reformulation of nonlinear environments into a structure aligned with Koopman control theory Eq.~eq:koopman\_control.}\label{fig:kippo-architecture} KIPPO introduces a Koopman-inspired representation learning framework that operates independently alongside the core policy optimization process. This approach unifies traditional RLwith Koopman operator theory while maintaining practical implementability.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Methodology", "weight": 1.0} -->

- Decoupled Optimization: Representation learning and policy optimization are deliberately separated to prevent interference between objectives, where the core policy algorithm remains unchanged, operating on encoded states without modification to its optimization process - Local Linearization: Rather than attempting global linearization, the framework focuses on simplifying dynamics along policy-explored trajectories - Balanced Complexity: Loss functions are designed to balance the competing objectives of simplification and information preservation KIPPO['s] key innovation is its targeted approach to linearity, expressed as $\gls{state-encoder}(\gls{state}_{t+1}) \approx \gls{koop-mat-state} \gls{state-encoder}(\gls{state}_t) + \gls{koop-mat-action} \gls{action-encoder}(\gls{action}_t)$. Unlike networks with standard linear output layers, KIPPOenforces linear dynamics across time steps as a soft constraint, applying this only to policy-explored trajectories.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Methodology", "weight": 1.0} -->

This creates an inductive bias on temporal transitions rather than static mappings, promoting stable gradient flow while avoiding the computational burden of global linearization.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Architecture Design", "weight": 1.0} -->

Building upon these design principles, the core innovation of KIPPOlies in learning a latent representation where complex, non-linear environment dynamics can be effectively approximated by linear operations within regions of the state space explored by the current policy.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Architecture Design", "weight": 1.0} -->

While sharing similarities with representation learning and data compression, KIPPO employs a higher-dimensional latent space than the original state space. This design choice follows from Koopman theory, which demonstrates that non-linear dynamics can be linearized through appropriate lifting to higher-dimensional spaces of observable functions.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Architecture Design", "weight": 1.0} -->

- A state autoencoder consisting of an encoder \(\gls{state-encoder}: \gls{state-space} \to \gls{reals}^m\) and decoder \(\gls{state-decoder}: \gls{reals}^m \to \gls{state-space}\), which respectively map states to latent representations and reconstruct original states - An action encoder \(\gls{action-encoder}: \gls{action-space} \to \gls{reals}^k\) that maps actions to the latent space - Linear system matrices \(\gls{koop-mat-state} \in \gls{reals}^{m\times m}\) and \(\gls{koop-mat-action} \in \gls{reals}^{m\times k}\) that govern the dynamics within the latent space The encoder and decoder networks use MLP with hyperbolic tangent (tanh) activation functions, chosen for their smooth gradients and bounded output

<!-- chunk {"id": "body-0018", "role": "body", "section": "Architecture Design", "weight": 1.0} -->

All trainable parameters employ Xavier uniform initialization to promote stable learning in deep networks, except for \(\gls{koop-mat-state}\), which uses orthogonal initialization for stable gradient flow, and \(\gls{koop-mat-action}\), which starts with zeros to allow gradual learning of control effects. The number of layers and neurons per layer remain consistent across the state encoder, decoder, and action encoder networks, typically using 2-3 hidden layers with 64-256 units each. This architectural consistency helps maintain balanced representational capacity across components while remaining computationally efficient.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Architecture Design", "weight": 1.0} -->

The use of non-linear activation functions might appear counterintuitive given our goal of linear dynamics. However, these non-linearities are essential for learning effective Koopman observables, enabling the networks to discover appropriate lifting functions that map the original system to a space where linear approximations become effective along policy-relevant trajectories. While the Koopman operator governing the evolution of observables is inherently linear, the method of obtaining these observables need not be linear. These non-linearities enable the MLPto act as universal function approximators, making them well-suited for approximating the Koopman observables in the latent space.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Architecture Design", "weight": 1.0} -->

The dimensions of the state-transition matrix \(\gls{koop-mat-state}\) and control matrix \(\gls{koop-mat-action}\)correspond to the chosen latent space dimensionality. This is typically set to 2-4 times the state dimension, providing sufficient capacity to capture complex dynamics without excessive computational overhead. These matrices are learnable parameters optimized alongside other components, enabling the framework to learn environment-specific representations directly from experience.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Architecture Design", "weight": 1.0} -->

These components work together to approximate the Koopman operator's action on observable functions, with the encoders serving as learnable observable functions and the linear matrices capturing the evolution of these observables. This connection to Koopman theory provides theoretical grounding for our approach while remaining practically implementable within the

<!-- chunk {"id": "body-0022", "role": "body", "section": "Future State Prediction Process", "weight": 1.0} -->

The prediction process forecasts states over horizon \(\gls{horizon}\) using learned linear latent-space dynamics. For an initial state \(\gls{state}\_0\) and an action sequence \(\gls{action}\_{0:\gls{horizon}}\), the process begins with the initial encoding of the state into a latent representation, \(y\_0 = \phi\_x(x\_0)\). This is followed by an iterative prediction using learned dynamics, expressed as \(\gls{state-pred-obs}\_{h+1} = \gls{koop-mat-state} y\_{h} + \gls{koop-mat-action} \gls{action-encoder}(\gls{action}\_{h})\).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Future State Prediction Process", "weight": 1.0} -->

This process yields a sequence of predicted latent states, which can be decoded back to the original state space using \(\gls{state-pred}\_{h+1} = \gls{state-decoder}(\gls{state-pred-obs}\_{h+1})\).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Future State Prediction Process", "weight": 1.0} -->

The process implements the finite-dimensional approximation of the Koopman-based control formulation from Eq. [eq:koopman\_control], where \(\gls{state-encoder}\) and \(\gls{action-encoder}\) represent \(\gls{state-obs-func}\) and \(\gls{action-obs-func}\), respectively. This process primarily constrains the learning of the latent representation to reduce gradient variance, rather than for generating additional training data or performing planning. Importantly, this serves as a soft constraint; perfect linearity is not required, but the representation is encouraged to be approximately linear along policy trajectories to enable more stable policy optimization.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Future State Prediction Process", "weight": 1.0} -->

The multi-step prediction shapes representations by enforcing temporal consistency only along current-policy trajectories, avoiding unrealistic global linearity assumptions.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Future State Prediction Process", "weight": 1.0} -->

KIPPOto benefit from structured representations without requiring lookahead or model predictive control. Unlike model-based planning methods, we never use the learned model for planning; our method focuses on variance reduction through temporal coherence. We deliberately chose this novel application of predictive models solely for variance reduction rather than for planning. It specifically addresses the noisy updates that challenge policy gradient methods.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Future State Prediction Process", "weight": 1.0} -->

The prediction horizon \(\gls{horizon}\) balances computational cost against prediction depth. Empirically, horizons of 8-32 steps are effective, with longer horizons benefiting environments with significant temporal dependencies or sparse rewards. As analyzed in Appendix[app:hypers:horizon] and Table[tab:effect\_horizon], longer horizons benefit moderately complex environments but offer diminishing returns or instability in very simple or highly complex ones.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Future State Prediction Process", "weight": 1.0} -->

Detailed implementation steps for the prediction process are provided in the supplementary material (app:impl:pred).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Loss Formulation", "weight": 1.0} -->

Drawing inspiration from Koopman operator theory, KIPPO employs three complementary loss components, reconstruction loss, latent-space prediction loss, and state-space prediction loss, that shape the latent space to achieve four key properties, including 1) informativeness where essential information from the original state space is preserved, ensuring the agent can make decisions based on accurate representations, 2) simplification where system dynamics is represented using linear approximation specifically along policy trajectories, rather than globally across the entire state space, 3) predictability where accurate multi-step predictions can be achieved within explored regions, enabling better temporal coherence and reduced gradient variance, and 4) consistencywhere the representation aligns with true environment dynamics for effective policy learning.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Reconstruction Loss", "weight": 1.0} -->

The reconstruction loss ensures the latent space retains sufficient information for accurate state reconstruction: $$\gls{loss-ki-rec}(t) = \left\{\gls{state-decoder}(\gls{state-encoder}(\gls{state}_t)) - \gls{state}_t\right\}^2$$ This loss primarily addresses informativenesswhile aligning with Koopman theory principles, where observable functions are typically assumed to be invertible. This formulation allows a bijective mapping between the original state space and latent space, maintaining a meaningful connection that supports both representation learning and policy optimization.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Reconstruction Loss", "weight": 1.0} -->

Note that the action reconstruction loss is omitted since the sole purpose of the action encoder is to influence state transitions in the latent space, and the accuracy of action encoding is implicitly enforced through future state prediction losses. Empirical studies also confirm that including action reconstruction terms does not yield significant performance improvements.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Latent-Space Prediction Loss", "weight": 1.0} -->

The latent-space prediction loss primarily targets simplification and predictabilitywithin policy-relevant regions.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Latent-Space Prediction Loss", "weight": 1.0} -->

It encourages learning a representation where dynamics can be effectively approximated by linear operations along policy-explored trajectories: $$\gls{loss-ki-pred-ls}(t) = \frac{1}{\gls{horizon}} \sum_{h=1}^{\gls{horizon}} \gls{binary-mask}_{t,h}\,\bigl(\gls{state-pred-obs}_{t+h} - \gls{state-encoder}(\gls{state}_{t+h})\bigr)^2$$ where \(\gls{binary-mask}\_{t,h}\) handles episode boundaries through a binary mask: 1, & \text{if trajectory not ended by step }(t + h - 1), \\The binary mask is essential for handling variable-length trajectories, such that the prediction process is not penalized for discontinuities introduced by environment resets at episode boundaries.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Latent-Space Prediction Loss", "weight": 1.0} -->

The loss term facilitates the learning of representations where dynamics can be effectively approximated by linear operations, as \(\gls{state-pred-obs}\_{t+h}\) is generated using linear matrices \(\gls{koop-mat-state}\) and \(\gls{koop-mat-action}\). It also enhances predictability by minimizing multi-step prediction errors directly in the latent space, while supporting simplification by encouraging the encoder to find representations where linear predictions maintain accuracy over multiple timesteps.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Latent-Space Prediction Loss", "weight": 1.0} -->

This loss term is particularly important for maintaining the framework's Koopman-inspired aspects, as it drives the learning of representations that align with Koopman theory's principle of lifting non-linear dynamics to spaces where linear approximations become effective.

<!-- chunk {"id": "body-0036", "role": "body", "section": "State-Space Prediction Loss", "weight": 1.0} -->

The state-space prediction loss primarily addresses consistency and predictability, maintaining fidelity to true dynamics while ensuring meaningful state predictions: $$\gls{loss-ki-pred-ss}(t) = \frac{1}{\gls{horizon}} \sum_{h=1}^{\gls{horizon}} \gls{binary-mask}_{t,h}\,\bigl(\gls{state-decoder}(\gls{state-pred-obs}_{t+h}) - \gls{state}_{t+h}\bigr)^2$$ The loss helps prevent the latent space from diverging too far from physically meaningful representations, which is essential for learning effective control policies.

<!-- chunk {"id": "body-0037", "role": "body", "section": "State-Space Prediction Loss", "weight": 1.0} -->

This dual-space prediction approach ensures the latent dynamics align with true environment behavior when mapped back to state space. It also promotes learning of latent representations that maintain predictive power across multiple timesteps, indirectly reinforcing informativeness by requiring accurate long-term state reconstruction. The improved temporal consistency from these representations helps reduce gradient variance in policy updates, though we never use these predictions for planning.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Total Representation Loss", "weight": 1.0} -->

The total representation loss is a weighted sum of the three components: $$\gls{loss-ki-wsum} = \frac{1}{\gls{total-steps}}\sum_{t=0}^{\gls{total-steps}} \left(\gls{loss-weight-ki-rec} \gls{loss-ki-rec}(t) + \gls{loss-weight-ki-pred-ls} \gls{loss-ki-pred-ls}(t) + \gls{loss-weight-ki-pred-ss} \gls{loss-ki-pred-ss}(t)\right)$$ where \(\gls{total-steps}\) represents the number of steps collected during rollouts.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Total Representation Loss", "weight": 1.0} -->

The weights \(\gls{loss-weight-ki-rec}\), \(\gls{loss-weight-ki-pred-ls}\), and \(\gls{loss-weight-ki-pred-ss}\) incorporate several factors, including relative scales between latent and state space dimensionalities, task-specific requirements, and environment characteristics. Sec.[sec:ablation]investigates the impact of each loss term on both the return and stability of learning.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Overview of Training Process", "weight": 1.0} -->

The training process in KIPPOalternates between rollout and optimization phases until reaching a predetermined number of environment steps. During rollouts, the agent collects states, actions, rewards, and additional sequences needed for representation losses, storing them in separate buffers. Each rollout phase collects 2,048 environment steps across multiple trajectories, resetting the environment when necessary to ensure diverse experiences.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Overview of Training Process", "weight": 1.0} -->

KIPPO and PPO use identical on-policy rollouts and operate with the same available information. KIPPO utilizes future states solely as auxiliary loss targets (never as policy inputs), which is consistent with standard auxiliary objective practices in on-policy RL. During both training and inference, both methods receive identical trajectories and current-state information, with KIPPO applying state encoding while PPOuses raw states.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Overview of Training Process", "weight": 1.0} -->

The optimization phase processes the collected data to update all components. The algorithm divides 2,048 steps into 32 mini-batches, computing the three key losses to update representation learning components.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Overview of Training Process", "weight": 1.0} -->

The total framework loss combines the weighted representation loss and standard $$\gls{loss-kippo} = \gls{loss-ki-wsum} + \gls{loss-ppo}$$ Both components update their parameters using the Adam optimizer. The optimization process runs for 10 epochs, allowing refinement of both the latent representation and the policy. After optimization, a new rollout phase begins, continuing this cycle until reaching 1 million environment steps.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Overview of Training Process", "weight": 1.0} -->

The latent representation is learned incrementally throughout training, with parameters adapting gradually across rollout-optimization cycles. We observe stability, with representations evolving smoothly between updates, maintaining consistent state encodings, and preventing disruptive changes that could destabilize learning. This is particularly important for policy gradient methods sensitive to sudden representation shifts.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Overview of Training Process", "weight": 1.0} -->

A key feature is the complete decoupling of representation learning from policy optimization. The representation learning components optimize independently from policy and value networks. This separation ensures improvements stem from the learned representation. Detailed optimization phase implementation and pseudocode are provided in Appendix [app:impl:optim].

<!-- chunk {"id": "body-0046", "role": "body", "section": "Experiments and Results", "weight": 1.0} -->

We evaluate the effectiveness of KIPPO compared to baseline PPO and RPOalgorithms across diverse continuous control tasks, measuring both performance improvements and reduced variability.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Environments", "weight": 1.0} -->

We evaluate six continuous control environments from Gymnasium using MuJoCo and Box2D, forming a comprehensive testbed with diverse complexity levels and control challenges. The environments' varying non-linearity and temporal dependencies help evaluate the algorithm's robustness and its ability to learn effective representations in the Koopman observable space. We chose these testbeds to systematically evaluate how our approach reduces gradient variance across different complexity levels while keeping the analysis tractable.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Environments", "weight": 1.0} -->

To facilitate discussion, we classify the six environments by their complexity levels, defined using the dimensions of the state space, $|\mathcal{S}|$, and the action space, $|\mathcal{A}|$. An environment is considered to have low complexity if $|\mathcal{S}| + |\mathcal{A}| < 10$, medium complexity if $ 10 \leq |\mathcal{S}| + |\mathcal{A}| < 20$, and high complexity if $|\mathcal{S}| + |\mathcal{A}| \geq 20$. This is summarized in tab:envs\_difficulty. For detailed specifications of the environments, please refer to app:setup:envs.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Environments", "weight": 1.0} -->

Environments and their complexity levels based on the dimensionality of their state and action spaces.}\label{tab:envs\_difficulty} \textbf{Environment} & \textbf{Complexity} & \textbf{|\gls{state-space}|} & \textbf{|\gls{action-space}|} \\Walker2d-v4 & High & 17 & 6 \\

<!-- chunk {"id": "body-0050", "role": "body", "section": "Training Configuration", "weight": 1.0} -->

For meaningful comparisons, we implement our benchmarks using the PPO and RPO implementations from the CleanRL library. We maintain CleanRL's default hyperparameters for both algorithms.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Training Configuration", "weight": 1.0} -->

Each experiment uses 4 random initialization seeds per environment. We selected 4 seeds as a balance between the original PPO paper's 3 seeds and CleanRL's standard 5 seeds. These seeds determine both the environment's initial states and model parameter initialization. To ensure fair comparison, we use identical random seeds and initialization patterns across all methods. Each training run consists of exactly 1 million environment steps. We provide hardware specifications and runtime measurements in Appendix[app:setup:compute].

<!-- chunk {"id": "body-0052", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

Given the inherent stochasticity in both environment and learning processes, we employ the EWMA of episodic returns to capture learning trends effectively: $$\text{\glsentryshort{EWMA}}_t = \alpha \cdot \text{\glsentryshort{EWMA}}_{t-1} + (1 - \alpha) \cdot \gls{return}_t,$$ where $G_t$ is the expected (discounted) return, summing rewards weighted by $\gamma^t$ at each time step; and empirically determined \(\alpha=0.05\). $\alpha$balances responsiveness to recent changes with historical context, reducing noise by filtering short-term fluctuations and ensuring robustness against outliers.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

We also use the $$\text{\glsentryshort{CTE}} = \frac{1}{\gls{horizon}} \sum_{h=1}^{\gls{horizon}} \frac{1}{h}\sum_{k=1}^{h} \lvert \gls{state-pred}_k - \gls{state}_k \rvert$$ where $k$ indices the individual timestep. While EWMA evaluates the overall agent performance, CTE specifically measures the representation quality by comparing predicted states (state-pred) with actual states (state) across varying horizons.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

For a comprehensive evaluation, we analyze both metrics through their means and standard deviations (SD) across 4 independent training runs.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Comparison with Baselines", "weight": 1.0} -->

We conduct the first set of experiments by comparing KIPPO['s] performance with two baseline policy gradient methods, PPO and RPO, selected due to either popularity or state-of-the-art performance. The comparison is summarized in tab:results\_envs\_main. Fig.[fig:results\_envs\_main\_percdiff] presents the percent difference in these metrics relative to the PPO baseline.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Comparison with Baselines", "weight": 1.0} -->

Per-environment overview of the main results comparing \glsentryshort{KIPPO} and the baseline \glsentryshort{PPO} and \glsentryshort{RPO} in terms of mean and std. of final episodic returns \gls{EWMA} across four trials.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Comparison with Baselines", "weight": 1.0} -->

The bold font highlights the best performance.}\label{tab:results\_envs\_main} \textbf{Environment} & \multicolumn{2}{c}{\textbf{PPO}} & \multicolumn{2}{c}{\textbf{RPO}} & \multicolumn{2}{c}{\textbf{KIPPO}} \\& Mean & Std & Mean & Std & Mean & Std \\InvertedPendulum-v4 & 897.57 & 41.61 & 892.33 & 36.46 & \bfseries 998.18 & \bfseries 3.57 \\tab:results\_envs\_main and Fig.[fig:results\_envs\_main\_percdiff], we observe that KIPPO achieves overwhelmingly better mean performance in all environments, with improvements ranging from 6.36% to 60.26% for the PPO baseline and from 11.86% to 142.18% for the RPO baseline.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Comparison with Baselines", "weight": 1.0} -->

KIPPO also shows lower SD in most environments, demonstrating enhanced consistency across seeds, reducing variance by 26.89-91.43% versus PPO (one exception) and 58.94-90.21% versus RPO(two exceptions). We will further discuss the exceptional cases in the ablation study.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Comparison with Baselines", "weight": 1.0} -->

This dual improvement in performance and stability highlights the fundamental advantage of incorporating Koopman-inspired representation. For a more granular view of performance evolution, we provide detailed learning curves in app:train\_curves.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Ablation Study of Loss Components", "weight": 1.0} -->

To understand the mechanisms underlying KIPPO['s] performance advantages, we conduct a systematic ablation study of its core components. tab:effect\_losses\_partial shows the result of one environment. For the other five environments, please refer to tab:effect\_losses in app:ablation\_losses.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Ablation Study of Loss Components", "weight": 1.0} -->

Effect of the loss function components on final episodic returns (\glsentryshort*{EWMA}) values and prediction error (\glsentryshort*{CTE}). The baseline is shown as the first row for each environment.}\label{tab:effect\_losses\_partial} \textbf{Environment} & \(\gls{loss-ki-rec}\) & \(\gls{loss-ki-pred-ls}\) & \(\gls{loss-ki-pred-ss}\) & \multicolumn{2}{c}{\textbf{\gls{EWMA}}} & \multicolumn{2}{c}{\textbf{\gls{CTE}}} \\& & & & Mean & Std. & Mean & Std.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Ablation Study of Loss Components", "weight": 1.0} -->

\\% & --- & --- & \chk & 971.46 & 32.02 & \bfseries 0.001 & \bfseries 0.000 \\% & --- & \chk & \chk & 950.25 & 91.69 & \bfseries 0.001 & \bfseries 0.000 \\& \chk & --- & \chk & 977.78 & 21.09 & \bfseries 0.001 & \bfseries 0.000 \\& \chk & \chk & \chk & \bfseries 998.18 & \bfseries 3.57 & \bfseries 0.001 & \bfseries 0.000 \\Several key findings emerge from Figs. [fig:rel\_impr\_means\_loss\_combinations], [fig:rel\_impr\_stds\_loss\_combinations] and Tables[tab:effect\_losses\_partial], [tab:effect\_losses]. Note that the first row per environment represents baseline PPO performance.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Ablation Study of Loss Components", "weight": 1.0} -->

First, the reconstruction loss alone yields results comparable to those of the baseline. Second, integrating all losses produces the best mean EWMA and lowest standard deviation in most cases. Third, the mean CTE decreases systematically with the incorporation of additional loss components. And finally, the latent-space prediction loss consistently reduces both CTEmean and standard deviation.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Ablation Study of Loss Components", "weight": 1.0} -->

While the ablation results in Tables [tab:effect\_losses\_partial] and [tab:effect\_losses] highlight the contributions of each loss component, they also reveal that KIPPO['s] overall gains depend strongly on the level of non-linearity (complexity) of each environment. We hypothesize a sublinear (logarithmic) relationship between performance gain and complexity, meaning that beyond a certain point, additional non-linearity or complexity diminishes marginal returns and raises variance. [fig:rel\_impr\_means\_combined] shows our evaluation of *KIPPO across varying environment complexities. We analyze two key metrics compared to the *PPObaseline: relative improvement in average performance (mean) and consistency of results (SD).

<!-- chunk {"id": "body-0065", "role": "body", "section": "Ablation Study of Loss Components", "weight": 1.0} -->

The mean percent improvement of environments with various levels of complexity in performance gain (Left) and variance reduction (Right) of final returns by KIPPO compared to PPO.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Ablation Study of Loss Components", "weight": 1.0} -->

KIPPO scales effectively across a broad range of non-linear control tasks but hits an upper limit as complexity grows. In simpler domains, overemphasizing latent-space predictions can harm stability unless balanced by state-space constraints. In extreme tasks, significant raw gains come with heightened variance. Thus, KIPPO extends PPO's performance boundary significantly, but the underlying non-linearities impose a logarithmicor sublinear bound on further improvements.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Sensitivity Analysis and Limitations", "weight": 1.0} -->

In this set of experiments, we conduct extensive parameter sensitivity studies, particularly focusing on the latent dimension and prediction horizon to better understand Comprehensive quantitative results are available in Appendices[app:hypers:latent] and[app:hypers:horizon].

<!-- chunk {"id": "body-0068", "role": "body", "section": "Sensitivity Analysis and Limitations", "weight": 1.0} -->

We observe that performance gains diminish in environments with highly discontinuous transitions (e.g., collisions), contact-rich interactions, or multi-modal behaviors, as the linear latent dynamics struggle with abrupt changes. Despite enforcing approximate linearity only along policy trajectories as a soft constraint, environments with highly chaotic dynamics remain challenging.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Sensitivity Analysis and Limitations", "weight": 1.0} -->

In environments with sparse rewards, the advantage over baseline PPOis less pronounced, suggesting that reduced gradient variance benefits are most impactful with frequent feedback signals. We view Koopman-based dynamics as an inductive bias particularly well-suited for certain control problems rather than as a universally valid model. These selected environments provide a controlled setting to test our core hypothesis: linearized latent dynamics can reduce gradient variance in policy optimization.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Sensitivity Analysis and Limitations", "weight": 1.0} -->

KIPPO takes approximately 15% longer than PPO(15 hours vs. 13 hours for 24 parallel models) due to construction of prediction sequences and computation of multi-step prediction losses. However, this computational overhead exists only during training; at inference time, only the encoder is used with negligible additional computational cost.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Sensitivity Analysis and Limitations", "weight": 1.0} -->

To identify the most influential hyperparameters, we train a random forest regressor to predict final returns from hyperparameter configurations. [fig:res\_hypers\_importance] shows that the latent-space prediction loss weight (loss-weight-ki-pred-ls) has the highest importance, followed by the latent dimension and state-space prediction loss weight (each 0.20). For return variability, the three loss weights (each 0.20) dominate, followed by the prediction horizon (0.15).

<!-- chunk {"id": "body-0072", "role": "body", "section": "Sensitivity Analysis and Limitations", "weight": 1.0} -->

Hyperparameter importance scores derived from a random forest regressor.}\label{fig:res\_hypers\_importance}

<!-- chunk {"id": "body-0073", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

KIPPO addresses key challenges in policy gradient methods through stable policy optimization for complex non-linear control tasks. Our experiments demonstrate the effectiveness of Koopman-inspired representation learning in policy optimization as showcased in PPO and RPO. This architecture naturally extends to other on-policy algorithms, including TRPO and A2C.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

KIPPOstems from a synergistic bidirectional relationship: policy gradients generate exploratory rollouts that guide which latent regions to linearize, while the resulting representations reduce gradient variance in precisely those regions, creating a more effective feedback loop than decoupled representation learning. This mechanism retains gradient variance reduction benefits even when extended beyond on-policy methods.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

Future directions include extending to: 1) off-policy algorithms like DDPG, TD3, and SAC; 2) value-based methods for enhancing Q-function learning; and 3) discrete domains through appropriate latent space formulations. Further research opportunities involve handling discontinuous dynamics and investigating representation robustness under noise and distribution shifts.
