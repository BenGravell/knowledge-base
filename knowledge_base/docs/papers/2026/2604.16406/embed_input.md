<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Heterogeneous Self-Play for Realistic Highway Traffic Simulation

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Realistic highway simulation is critical for scalable safety evaluation of autonomous vehicles, particularly for interactions that are too rare to study from logged data alone. Yet highway traffic generation remains challenging because it requires broad coverage across speeds and maneuvers, controllable generation of rare safety-critical scenarios, and behavioral credibility in multi-agent interactions. We present PHASE, Policy for Heterogeneous Agent Self-play on Expressway, a context-aware self-play framework that addresses these three requirements through explicit per-agent conditioning for controllability, synthetic scenario generation for broad highway coverage, and closed-loop multi-agent training for realistic interaction dynamics. PHASE further supports different vehicle profiles, for example, passenger cars and articulated trailer trucks, within a single policy via vehicle-aware dynamics and context-conditioned actions, and stabilizes self-play with early termination of unrecoverable states, at-fault collision attribution, highway-aware reward shaping, coupled curricula, and robust policy optimization.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Despite being trained only on synthetic data, PHASE transfers zero-shot to 512 unseen high-interaction real scenarios in exiD, achieving a 96.3% success rate and reducing ADE/FDE from 6.57/12.07 m to 2.44/5.25 m relative to a prior self-play baseline. In a learned trajectory embedding space, it also improves behavioral realism over IDM, reducing Frechet trajectory distance by 13.1% and energy distance by 20.2%. These results show that synthetic self-play can provide a scalable route to controllable and realistic highway scenario generation without direct imitation of expert logs.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Highway driving is one of the most safety-critical settings for autonomous vehicles: interactions unfold at high speed, small prediction errors can escalate quickly, and rare events such as aggressive cut-ins or dense merging are difficult to capture in sufficient quantity from real-world logs alone. This makes simulation a core tool for development and validation. A highway simulator, however, must do more than replay recorded traffic. It must expose safety-critical interactions at scale, remain stable in closed-loop rollouts, and support stress testing across diverse traffic regimes.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Existing approaches only partially satisfy these requirements. Log replay and supervised trajectory prediction preserve realistic behavior, but are limited by the behaviors present in the data and can drift under closed-loop execution. Rule-based traffic models offer controllability, but often rely on simplified assumptions that fail to capture the richness of real multi-agent interactions. Recent self-play reinforcement learning (RL) methods offer a promising alternative by learning interactive behavior directly from closed-loop experience, and have shown strong results in urban driving, including on benchmarks derived from the Waymo Open Motion Dataset (WOMD). Yet these methods have been developed primarily for urban regimes and do not directly address the demands of highway traffic.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Highway simulation poses a distinct challenge. Compared with urban driving, highway traffic spans a broader speed range, exhibits greater variation in density and interaction style, and includes stronger physical heterogeneity across vehicle classes. A practical highway simulator must therefore satisfy three requirements simultaneously: broad coverage across speeds and maneuvers, controllable generation of rare safety-critical scenarios, and realistic multi-agent behavior in closed-loop interaction.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We address these challenges with PHASE, a self-play framework for controllable heterogeneous highway traffic generation. We formulate the problem as a conditioned goal-reaching Partially Observable Stochastic Game (POSG), in which each agent is assigned a Cartesian goal together with context variables such as target speed, longitudinal action range, and vehicle type. This conditioning provides explicit behavioral control, while a single policy handles both passenger cars and articulated tractor-trailers. As illustrated in Figure 1, varying the context variables while holding the base scene fixed produces distinct interaction patterns and allows users to steer scenario outcomes directly. To achieve broad coverage without relying on expert trajectory imitation, we train entirely on synthetic scenarios generated by an offline--online pipeline: lane-graph search constructs diverse start--goal pools offline, and online sampling randomizes agent count, lane-change composition, kinematics, and geometry. To preserve realistic behavior under self-play, we further combine simulation mechanisms, highway-aware reward design, coupled curricula, and robust policy optimization.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate PHASE in two complementary settings. On exiD, PHASE transfers zero-shot to unseen real highway scenarios and substantially outperforms a prior self-play baseline in both success rate and displacement error. In a learned trajectory embedding space built from proprietary real highway logs, it also produces trajectory distributions that align more closely with real traffic than IDM.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

A conditioned formulation for controllable heterogeneous highway simulation. We formulate highway traffic generation as a conditioned goal-reaching POSG in which a single policy controls both passenger cars and articulated tractor-trailers across a 0--40 m/s operating range through joint goal and context conditioning.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A scalable synthetic scenario generation pipeline for broad highway coverage. We introduce an offline--online generator that combines lane-graph endpoint search with controllable world sampling to produce diverse, map-consistent highway scenes without direct imitation from expert trajectory logs.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

A stable self-play training recipe for highway traffic. We combine simulation mechanisms, highway-aware reward shaping, coupled curricula, and robust optimization choices to make learning-from-scratch self-play practical in heterogeneous highway regimes.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Strong real-world transfer and improved behavioral realism. PHASE generalizes zero-shot to exiD and produces trajectory distributions that more closely match real highway driving than prior self-play and classical controller baselines.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Task Definition", "weight": 1.0} -->

We formulate highway traffic generation as a Partially Observable Stochastic Game (POSG), defined by the tuple

<!-- chunk {"id": "body-0014", "role": "body", "section": "Task Definition", "weight": 1.0} -->

Here, $\mathcal{I} = {\{ 1,\ldots,N\}}$ denotes the set of agents, $\mathcal{S}$ is the global joint state space, and $\mathcal{O}^{i}$ and $\mathcal{A}^{i}$ are the observation and action spaces of agent $i$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Task Definition", "weight": 1.0} -->

We define a *conditioned goal-reaching* task. Each agent $i$ is assigned a Cartesian goal location $g_{i} \in {\mathbb{R}}^{2}$ together with an individual conditioning context vector

<!-- chunk {"id": "body-0016", "role": "body", "section": "Task Definition", "weight": 1.0} -->

Here, $v_{\text{goal},i} \in {\lbrack 0,40\rbrack}$ m/s is the target cruising speed, $\alpha_{i} \in {\lbrack 0.1,1\rbrack}$ modulates the agent's longitudinal control range, $\mathcal{T}_{i} \in {\{\text{Car},\text{Truck}\}}$ specifies vehicle type, and $\mathcal{D}_{i} = {(\ell_{i},w_{i},\ell_{i}^{\text{tr}},w_{i}^{\text{tr}})}$ specifies vehicle dimensions, including corresponding trailer dimensions for articulated vehicles. Trailer terms are zero for passenger cars.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Task Definition", "weight": 1.0} -->

An episode is considered successful for agent $i$ if the agent reaches a designated target region around $g_{i}$ without collision over a finite horizon $T$. Target speed and yaw alignment are treated as soft objectives through reward shaping, while $\alpha_{i}$ defines the agent's control envelope rather than an additional success criterion.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Task Definition", "weight": 1.0} -->

The transition function $\mathcal{P}{({s^{\prime} \mid {s,\mathbf{a}}})}$ is determined by the underlying vehicle-dependent kinematics induced by $\mathcal{T}_{i}$ and $\mathcal{D}_{i}$. Because each agent's return depends directly on the actions of the other agents, the environment is inherently non-stationary from any single-agent perspective, motivating self-play for learning decentralized policies that induce coherent multi-agent traffic behavior.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Synthetic Scenario Generation", "weight": 1.0} -->

We train PHASE entirely in procedurally generated highway scenes to maximize coverage over traffic compositions, kinematics, and interaction patterns without relying on expert trajectory logs. The generator is controlled by seven parameters: the lane-change ratio $P_{lc}$, truck proportion $P_{\text{truck}}$, agent-count bounds $N_{\min}$ and $N_{\max}$, path-distance bounds $D_{\min}$ and $D_{\max}$, and a lane-change budget $K$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Synthetic Scenario Generation", "weight": 1.0} -->

Offline, for each map we construct a reusable tuple $(\text{map},\text{pool})$, where the pool contains candidate start--goal pairs. We first upsample the road geometry into a lane graph $G$ with nodes spaced at 1 m intervals and edges encoding lane continuity and left/right adjacency. For each sampled node, we run a bounded breadth-first search over longitudinal and lateral transitions to enumerate reachable endpoints whose path length lies in $\lbrack D_{\min},D_{\max}\rbrack$. Each frontier state tracks a signed lane-change count $c$, where left and right transitions update $c$ by $- 1$ and $+ 1$, respectively, and only states with ${|c|} \leq K$ are retained. Candidate endpoints are then partitioned into same-lane ($c = 0$) and lane-change ($c \neq 0$) sets, from which we sample goals to match the target lane-change ratio $P_{lc}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Synthetic Scenario Generation", "weight": 1.0} -->

Figure 2 shows example start--goal pairs from this offline pool.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Synthetic Scenario Generation", "weight": 1.0} -->

Online, we instantiate multiple worlds from each $(\text{map},\text{pool})$ tuple and sample scenarios independently within each world. We begin by sampling the number of agents as $N \sim {\mathcal{U}{\lbrack N_{\min},N_{\max}\rbrack}}$. A fraction $P_{\text{truck}}$ of the sampled agents are then designated as trucks and assigned truck-specific dynamics, while the remaining agents use car dynamics. We also randomize vehicle geometry on a per-agent basis. Finally, subject to collision checking, we sample each agent's initial state and goal from the offline pool.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Synthetic Scenario Generation", "weight": 1.0} -->

To set kinematics, we compute a base speed $v_{\text{base}}$ from the episode horizon and the average path length ${({D_{\min} + D_{\max}})}/2$, including safety buffers. Each agent then receives an initial speed

<!-- chunk {"id": "body-0024", "role": "body", "section": "Synthetic Scenario Generation", "weight": 1.0} -->

where $\epsilon_{\text{init},i}$ is a per-agent perturbation. We further sample a goal-speed offset $\epsilon_{\text{goal},i}$ and define

<!-- chunk {"id": "body-0025", "role": "body", "section": "Synthetic Scenario Generation", "weight": 1.0} -->

together with an action-range parameter $\alpha_{i} \sim {\mathcal{U}{(0.1,1.0)}}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Synthetic Scenario Generation", "weight": 1.0} -->

This offline--online design separates map-consistent route generation from online world randomization. In practice, it yields broad coverage over lane-change structure, traffic density, vehicle type, geometry, and target behavior, while preserving control through per-agent conditioning.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Observations, Actions, and Kinematic Models", "weight": 1.0} -->

Observation Space. We use an ego-centric observation space composed of the ego state, the 16 nearest neighboring agents, and local road geometry. The ego state includes current speed, vehicle dimensions, trailer dimensions, hitch angle, a truck indicator, relative goal position and heading, and the longitudinal action-range conditioning variable $\alpha_{i}$. To capture short-term control history, we also include current acceleration, steering angle, relative heading, and a 3-step history of acceleration and steering. Neighbor observations encode relative position, speed, orientation, and articulated bounding-box dimensions for surrounding traffic participants. Local road topology is represented by categorized spatial points describing drivable paths and boundaries. To improve robustness, we inject Gaussian noise into partner and map observations.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Observations, Actions, and Kinematic Models", "weight": 1.0} -->

Action Space. The action space is discrete and defined as the Cartesian product of bounded longitudinal and lateral inputs, specifically longitudinal jerk (m/s^3^) and steering rate (rad/s). At each step, the policy produces a discrete action token, which is subsequently mapped to continuous commands before being passed to the simulator. The selected longitudinal command is then scaled by the agent-specific conditioning variable $\alpha_{i}$, allowing the same policy structure to adapt its behavior to different vehicle capabilities. In practice, this conditioning allows a single policy to operate across a wide range of control envelopes, spanning agile passenger cars as well as heavy articulated trucks.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Observations, Actions, and Kinematic Models", "weight": 1.0} -->

Kinematic Model. Each agent is propagated with a standard discrete-time kinematic bicycle model using longitudinal jerk $j$ and steering rate $\overset{˙}{\delta}$. For articulated vehicles, we additionally update the hitch angle state $\phi$, clipped to $\lbrack{- {\pi/2}},{\pi/2}\rbrack$, according to

<!-- chunk {"id": "body-0030", "role": "body", "section": "Observations, Actions, and Kinematic Models", "weight": 1.0} -->

where $l_{\text{trailer}}$ is the trailer length.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Simulation Mechanisms", "weight": 1.0} -->

We introduce two simulation mechanisms to improve training stability: early termination of unrecoverable states and at-fault collision attribution.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Simulation Mechanisms", "weight": 1.0} -->

We early-terminate an agent when it enters a state from which reaching its assigned goal is no longer realistically plausible. Let $g_{i} \in {\mathbb{R}}^{2}$ denote the goal position expressed in the agent's local frame, and let $f_{i} \in {\mathbb{R}}^{2}$ denote the agent's forward unit vector. Agent $A_{i}$ is classified as unrecoverable if ${g_{i}^{\top}f_{i}} < 0$. Intuitively, this condition identifies states in which the goal lies behind the agent, indicating that the agent is moving away from its destination. Figure 3 illustrates two examples of such unrecoverable states in cases (a.1) and (a.2).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Simulation Mechanisms", "weight": 1.0} -->

It terminates agents traveling in an adjacent lane when the goal lies immediately to the left or right, thereby preventing unrealistic last-moment lane changes caused by extreme steering corrections near the goal.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Simulation Mechanisms", "weight": 1.0} -->

During the early stages of training, it prevents agents from collecting low-value trajectories that move away from the goal, which in turn improves sample efficiency and helps stabilize training.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Simulation Mechanisms", "weight": 1.0} -->

As in prior self-play work, we do not resolve collisions physically and instead penalize them through rewards. Unlike prior approaches, however, we penalize only the at-fault agent. We find this attribution rule important for training stability and performance. Formally, for a colliding pair $(A_{i},A_{j})$, let ${p_{i},p_{j}} \in {\mathbb{R}}^{2}$ denote effective global positions, and let $\ell_{j}$ denote the effective tractor or vehicle length of $A_{j}$. We assign fault to $A_{i}$ if

<!-- chunk {"id": "body-0036", "role": "body", "section": "Simulation Mechanisms", "weight": 1.0} -->

We define $F_{j}$ analogously. If neither agent is clearly behind the other (i.e., $F_{i} = F_{j} = 0$), we conservatively assign fault to both (${F_{i}\leftarrow 1},{F_{j}\leftarrow 1}$). Figure 3 (b) illustrates this collision-attribution mechanism.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Rewards", "weight": 1.0} -->

We use a mixture of sparse and dense reward terms to encourage safe, goal-consistent highway behavior while retaining useful learning signal early in training. For each agent $A_{i}$, the per-step reward is

<!-- chunk {"id": "body-0038", "role": "body", "section": "Rewards", "weight": 1.0} -->

Here, $R_{g,i}$ corresponds to goal completion, $R_{l,i}$ to lane-boundary compliance, $R_{f,i}$ to collision penalty, $R_{e,i}$ to road-edge penalty, $R_{t,i}$ to early-termination penalty, $R_{a,i}$ to alignment penalty, $R_{s,i}$ to speed-deviation penalty, and $R_{p,i}$ progress reward.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Rewards", "weight": 1.0} -->

Here, ${\overline{w}}_{( \cdot )} > 0$ are fixed weights and $\rho \in {\lbrack 0,1\rbrack}$ denotes curriculum progress. The curriculum multipliers $m_{g,i}{(\rho,w_{s,i},w_{a,i})}$, $m_{f}{(\rho)}$, $m_{e}{(\rho)}$, $m_{t}{(\rho)}$, and $m_{p}{(\rho)}$ are defined in Section 3.6 as functions of curriculum progress and, where applicable, goal-quality terms. Here, $F_{i}$ denotes the collision indicator, $G_{i}$ denotes the goal-achievement indicator, $E_{i}$ denotes the road-edge collision indicator, and $L_{i}$ denotes the lane-boundary collision indicator.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Rewards", "weight": 1.0} -->

For early termination, we set $T_{i}\leftarrow{\| g_{i}\|}_{2}$ when agent $i$ is terminated under the unrecoverable-state rule in Section 3.4. This penalizes goal-divergent failures more strongly when they occur far from the goal, while assigning smaller penalties to near-goal failures.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Rewards", "weight": 1.0} -->

We use ${w_{s,i},w_{a,i}} \in {\{ 0.1,1\}}$ to represent goal completion quality. The factor $w_{s,i}$ measures agreement with the target speed at the goal, and $w_{a,i}$ measures yaw alignment with the lane direction at the goal. These terms act as soft terminal preferences rather than hard feasibility constraints.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Rewards", "weight": 1.0} -->

Here, $d_{t,i}$ is the Euclidean distance to the goal, $\kappa > 1$ is a progress factor, and $\psi{(d)}$ is a distance-dependent decay term. The reward is normalized by speed so that faster agents are not favored purely because they cover more distance, and it is clipped for stability.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Rewards", "weight": 1.0} -->

Here, $\Delta\theta_{i}$ is the yaw-error term for agent $i$ and $\overline{T_{\text{ramp}}}$ is the alignment ramp horizon. This term increases as the agent approaches its goal, encouraging timely lane changes and reducing late, aggressive corrections. The ramp depends on an estimate of time-to-go, rather than raw distance, so that slower agents are not permitted larger heading errors at the same spatial distance.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Curricula", "weight": 1.0} -->

We use two coupled curricula: a reward curriculum and a scenario curriculum.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Curricula", "weight": 1.0} -->

Here, $w_{s,i}w_{a,i}$ is the goal-reward scaling term, and $\lambda > 1$ is the terminal curriculum multiplier that controls how strongly collision and off-road penalties are increased by the end of the curriculum. Thus, the goal-achievement multiplier is annealed, collision/off-road multipliers are ramped up, and the progress multiplier decays to $0$ at the terminal curriculum stage. Intuitively, this schedule gradually shifts optimization from dense guidance toward stricter emphasis on safety, alignment, and terminal behavior. Early in training, the progress reward helps agents discover goal-directed behavior; later, collision and off-road penalties become more dominant.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Curricula", "weight": 1.0} -->

For the scenario curriculum, we increase the lane-change ratio $P_{lc}$ and shift the agent-count distribution toward denser scenes at the end of training ($\rho = 1$). This late-stage curriculum exposes the policy to more congested, interaction-heavy traffic after it has already learned basic driving structure, which improves robustness and stability in challenging highway regimes.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Model", "weight": 1.0} -->

We parameterize PHASE with an MLP-based architecture augmented with cross-attention and attention pooling, as shown in Figure 4. Ego, partner-agent, and road-element features are first encoded separately. We then apply cross-attention between partner and road features to capture interactions between neighboring agents and local topology, followed by attention pooling to aggregate variable-sized inputs while preserving permutation invariance. In addition to the encoded observation, the policy receives the conditioning variables $(v_{\text{goal},i},\alpha_{i},\mathcal{T}_{i},\mathcal{D}_{i})$ as explicit inputs, which are concatenated with the ego feature embedding before the policy and value heads. The resulting representation is passed to separate policy and value heads.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Training", "weight": 1.0} -->

Highway self-play is less stable than the lower-speed urban settings considered in prior work because speed, density, and interaction complexity vary widely across scenarios. The same map can generate sparse, fast traffic or dense, slow traffic, and a single policy must learn across this full distribution. We therefore use three complementary design choices to improve training stability: DClamp-PPO for stable policy updates under coupled curriculum shifts, inverse-agent-count reweighting to balance gradient contributions across traffic densities, and action regularization toward smooth, near-zero-centered control.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Training", "weight": 1.0} -->

Training Algorithms. We use DClamp-PPO, a variant of PPO, to reduce instability during curriculum transitions. As curriculum progress $\rho$ increases, both the reward landscape and scenario distribution shift: dense progress guidance is reduced, terminal penalties become stronger, and later-stage scenarios become denser and more interactive. These coupled changes can cause standard PPO to overshoot. DClamp-PPO imposes a tighter effective trust region during such transitions, leading to smoother adaptation and fewer late-stage collapses.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Training", "weight": 1.0} -->

Sample Reweighting. Worlds with many agents produce more trajectories per update than sparse worlds. Without correction, dense worlds dominate the gradient and bias training toward slow, crowded traffic.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Training", "weight": 1.0} -->

Here, $\mathcal{W}$ is the set of sampled worlds in an update, $N_{w}$ is the number of agents in world $w$, and $\mathcal{L}_{\pi}^{(w,i)}$ is the policy loss for agent $i$ in world $w$. We apply the same reweighting to the value loss. This normalization makes each world contribute more evenly regardless of density and reduces the variance amplification induced by highly interactive dense scenes.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Training", "weight": 1.0} -->

Action Regularization. We replace the standard PPO entropy bonus with a KL regularizer toward a discrete action prior induced by a zero-mean Gaussian over the jerk--steering lattice. The prior is parameterized as $\mathcal{N}{(0,\Sigma_{0})}$, centered at zero jerk and zero steering rate.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Training", "weight": 1.0} -->

where $\lambda_{KL} > 0$ controls the regularization strength and $\Sigma_{0} \in {\mathbb{R}}^{2}$ sets the spread of the prior for steering rate and jerk invidually. This regularizer favors moderate, smoother controls while encouraging exploration.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Experiments and Results", "weight": 1.0} -->

We train a 670K-parameter policy from scratch on 22 highway maps in the United States, each spanning approximately 500 m. From these maps, we construct 77 distinct $(\text{map},\text{pool})$ tuples covering a range of speed regimes, traffic densities, and lane-change proportions, and instantiate 300 parallel worlds in GPUDrive. Key scenario statistics are summarized in Table 2. Training runs for 3 billion environment steps and takes approximately 80 hours on two NVIDIA A6000 GPUs. Table 2 reports the constant reward and curriculum parameters used throughout training.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Zero-shot Real-world Scenario Evaluation", "weight": 1.0} -->

We first evaluate zero-shot transfer on exiD, a real-world highway dataset with dense multi-agent interactions. We randomly sample 512 scenarios of length 10 s that contain at least one lane-change event. Agents are initialized at the start of each scenario and rolled out until the end, with action-range conditioning $\alpha_{i}$ sampled at random. All reported metrics are aggregated over the 512 scenarios and shown as mean $\pm$ standard deviation.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Zero-shot Real-world Scenario Evaluation", "weight": 1.0} -->

All policies are trained on the same synthetic training distribution using Optuna-optimized hyperparameters, and are then evaluated zero-shot on exiD without fine-tuning. Table 3 compares PHASE against a prior self-play baseline, together with ablations of both approaches. The -DClamp PHASE variant uses a standard PPO instead of DClamp-PPO.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Zero-shot Real-world Scenario Evaluation", "weight": 1.0} -->

PHASE substantially outperforms the prior self-play baseline across all task-level and trajectory-level metrics. In particular, it achieves a success rate of 96.3%, compared with 26.6% for the prior baseline, while reducing ADE/FDE from 6.57/12.07 m to 2.44/5.25 m. These gains indicate that the proposed conditioning, synthetic scenario generation, and stabilization design materially improve transfer to previously unseen real highway scenes.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Distributional Evaluation", "weight": 1.0} -->

Task completion alone does not determine whether a simulator reproduces realistic traffic behavior. We therefore evaluate whether the rollouts generated by PHASE match the statistical structure of real highway trajectories in a learned latent space. Following the evaluation perspective introduced in the Waymo Sim Agents Challenge, we compare simulated and real trajectories using distributional metrics rather than only task-level outcomes.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Distributional Evaluation", "weight": 1.0} -->

Each multi-agent trajectory sequence is embedded using the encoder of a state-of-the-art motion forecasting model, and we compare the resulting simulated and real trajectory distributions in the embedding space using Fréchet distance, energy distance, and Maximum Mean Discrepancy (MMD) with an RBF kernel. Our evaluation uses 33,398 trajectories from proprietary real highway driving logs together with corresponding simulator rollouts, and compares PHASE against a classical rule-based microscopic traffic model based on the Intelligent Driver Model (IDM); Table 4 reports the results.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Distributional Evaluation", "weight": 1.0} -->

Across all reported metrics, PHASE yields closer agreement with real trajectory distributions than IDM. In particular, Fréchet distance decreases from 6.3501 to 5.5199 and energy distance decreases from 0.0233 to 0.0186. MMD is also consistently lower across all tested RBF bandwidths, indicating that the improvement is not tied to a specific kernel scale. Precision and recall in the embedding space further suggest that both methods cover a broad portion of the real trajectory manifold, while PHASE produces slightly fewer out-of-distribution behaviors.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Distributional Evaluation", "weight": 1.0} -->

Quantitatively, we compare behavior-cluster centroids in the learned embedding space instead of the full embedding cloud. For each cluster, we measure the distance from the real-trajectory centroid to the IDM and PHASE centroids (Figure 5). Lower distances indicate better alignment with real data; PHASE is closer than IDM in most clusters, indicating more realistic behavior across modes.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

We introduced PHASE, a context-aware self-play framework for controllable and realistic highway traffic simulation. A single policy controls heterogeneous agents across a 0--40 m/s range, combining offline--online scenario generation, curriculum learning, and stable self-play. On exiD, PHASE transfers zero-shot and substantially outperforms prior self-play baselines on success and collision metrics. Distributional evaluation in a learned trajectory embedding space also shows closer alignment to real highway behavior than a classical rule-based baseline. These results suggest conditioned self-play is a practical, scalable route to realistic highway simulation for autonomous driving.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

Several directions remain for future work. First, scaling training to larger models and longer horizons may further improve robustness and coverage of rare interactions. Second, richer world models, including more diverse traffic participants, could broaden the scope of the work beyond the agent-agent interactions studied here. Finally, integrating perception and control within the same framework may enable a closer connection between simulation-agent and real-world driving.
