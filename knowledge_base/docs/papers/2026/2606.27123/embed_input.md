<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Proposal-Conditioned Latent Diffusion for Closed-Loop Traffic Scenario Generation

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Closed-loop traffic simulation remains challenging because it must generate interactive multi-agent behaviors that are scene-consistent and controllable throughout rollout. Prior diffusion-based approaches achieve strong realism, but their computational cost can hinder deployment in time-constrained replanning loops for autonomous vehicle planning and simulation. We present a diffusion-based scenario generation framework conditioned on instance-centric scene context and multimodal proposal priors, with optional test-time guidance for shaping safety-critical behaviors. A compact action-latent representation and proposal-based initialization improve sampling efficiency and reduce per-step runtime without retraining. Experiments on the Waymo Open Motion Dataset demonstrate a favorable balance among realism, safety, and controllability across diverse interactive scenarios, while showing that test-time guidance enables systematic trade-offs among competing objectives.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Validating autonomous vehicles, AVs, demands systematic exposure to safety-critical events that, by definition, occur rarely in naturalistic driving data. On-road testing is expensive and slow while simulated testing provides an inexpensive alternative as long as the simulated traffic is sufficiently realistic and includes a diverse set of meaningful edge cases.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prior research has contributed to the development of multi-agent scenario generation methodologies along two complementary directions. Realism-focused methods learn data-driven priors from large-scale datasets and generate highly realistic multi-agent behavior. However, these methods provide little control over the safety-critical aspects of the generated scenarios. Conversely, adversarial methods focus on generating scenarios that include collisions or near-miss events and may prioritize collision events at the expense of plausibility, such as agents violating road boundaries or kinematic constraints. Bridging this dichotomy is essential. Effective verification and validation requires scenarios that are simultaneously challenging and plausible to yield actionable safety insights.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Controllable multi-agent motion generation using diffusion models presents a potential solution to the challenge of providing both controllability and plausibility. The iterative nature of diffusion model-based denoising facilitates the use of test-time guidance and objective composition without the need for retraining. Nevertheless, reverse sampling typically involves many sequential steps which limits throughput in closed-loop environments where replanning must occur frequently and can make runtime efficiency a bottleneck for AV planning and simulation. Furthermore, joint guidance across multiple agents increases the computational complexity associated with the diffusion process and can lead to kinematically inconsistent trajectories. Starting the reverse process from a data-informed Gaussian prior can reduce the number of steps while preserving closed-loop fidelity.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fig. 1: Our approach is proposal-informed diffusion for closed-loop traffic simulation, initializing sampling from instance-centric marginal priors.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our key contributions: We propose a proposal-conditioned joint diffusion policy for closed-loop simulation that conditions on instance-centric scene context and per-agent marginal proposals, explicitly modeling joint interaction rather than composing independent futures.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We map proposal trajectories to a compact action latent via PCA and use proposal statistics to construct a shifted Gaussian start distribution, enabling few-step reverse diffusion at test time without retraining.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We apply differentiable map, collision, and game-theoretic objectives as latent-space guidance to trade realism vs stress-testing in closed-loop rollouts.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Adversarial Scenario Generation", "weight": 1.0} -->

Safety-critical scenarios are infrequent in logged driving data, motivating approaches based on importance sampling and reinforcement learning to identify failures. STRIVE introduced gradient-based adversarial optimization using a learned traffic prior and subsequent methods improved physical plausibility through kinematic constraints in KING and closed-loop adversarial training in CAT. Recent work has also leveraged human-driving priors for adversarial scenario generation. A recurring tension remains that optimizing exclusively for adversarial objectives can produce unrealistic behaviors whereas strict realism constraints may reduce adversarial effectiveness. Our guidance design addresses this tension by enabling safety edits while maintaining realism in closed-loop rollouts.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-B Data-Driven Traffic Simulation", "weight": 1.0} -->

Traffic simulation has moved from rule-based models such as IDM and MOBIL toward data-driven policies and generative simulators trained on large-scale driving datasets.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Data-Driven Traffic Simulation", "weight": 1.0} -->

Imitation-learning simulators that simultaneously roll out all agents such as TrafficSim and generative scenario augmentation methods such as TrafficGen enhance realism and diversity. Other systems provide scalable evaluation simulators built on large datasets such as Waymax. When paired with simple hand-designed policies (e.g., IDM), such platforms are better viewed as scalable evaluation backends than strong realism baselines. They also offer limited mechanisms for targeted safety-critical editing while preserving interactive closed-loop consistency. Our method aims to add this editing capability while keeping joint interaction fidelity under replanning.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-C Diffusion Models for Scenario Generation", "weight": 1.0} -->

Diffusion models are effective for multimodal trajectory generation and flexible conditioning. MotionDiffuser uses compressed representations to enable controllable joint prediction and variants such as MID model trajectory ambiguity with Transformer denoisers. Intention-aware denoising has also been explored for trajectory prediction. To reduce inference cost, leapfrog diffusion initialization such as LED aims to skip denoising steps. A practical limitation remains the computational demand at test time. Joint multi-agent diffusion can require many reverse steps and guidance that differentiates through the reverse process can further increase runtime. We address this by proposal-conditioned initialization and compact action latents that reduce steps without changing the model class. Unlike that refines trajectories starting from standard diffusion noise, our primary efficiency gain comes from proposal-conditioned initialization in a compact action latent, which changes the starting distribution and makes few-step DDIM viable in closed-loop replanning.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-D Guided and Controllable Diffusion", "weight": 1.0} -->

Controllable diffusion is commonly achieved via classifier guidance or classifier-free guidance. Composable diffusion shows that multiple objectives can be combined at inference by summing guidance terms. In planning, Diffusion-ES explores gradient-free optimization. Game-aware approaches explicitly model strategic interaction in GameFormer and motivate game-theoretic guidance for safety-critical scenario synthesis. Our formulation adapts these ideas to multi-agent closed-loop simulation with guidance applied in a compact latent space to control behavior without retraining.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-D Guided and Controllable Diffusion", "weight": 1.0} -->

Collectively, prior work highlights a recurring tension between realism, controllability and efficiency. We address it with proposal-conditioned joint diffusion that preserves interaction fidelity while enabling low-latency guidance for targeted safety edits.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-D Guided and Controllable Diffusion", "weight": 1.0} -->

Fig. 2: Our architecture illustration. An instance-centric symmetric scene encoder maps agent history and map context into a scene context c and marginal futures that are converted to an action-prior latent via PCA to condition a joint Transformer denoiser for multi-agent trajectory generation. We optionally apply inference-time guidance to refine sampled plans for behavior control and safety-critical scenarios.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Methodology", "weight": 1.0} -->

We first summarize the architecture in Fig. 2, then detail the formulation and inference procedure.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Problem formulation", "weight": 1.0} -->

We consider a simulated traffic scenario with $N$ agents. Agent $i$ at physical time $t$ has state where $(x_{t}^{i},y_{t}^{i})$ is planar position, $\psi_{t}^{i}$ is heading, and $v_{t}^{i}$ is speed. The action is where $a_{t}^{i}$ is longitudinal acceleration and $\dot{\psi}_{t}^{i}$ is yaw rate. We distinguish an ego agent that follows a fixed known policy and a set of reactive agents. At each replanning time $\tau$, the simulator provides the current closed loop state $\mathbf{X}_{\mathrm{init}}(\tau)$ together with observation history $H_{\tau}$ and map context $M_{\tau}$. Our goal is to learn a reactive policy $g$ that maps the current state, history, and map context to a joint action plan for the reactive agents over a horizon of $T_{u}$ steps.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Problem formulation", "weight": 1.0} -->

The joint plan is where $\mathcal{R}$ denotes the set of reactive agents. Equivalently, $g:(\mathbf{X}_{\mathrm{init}}(\tau),H_{\tau},M_{\tau})\mapsto\mathbb{R}^{|\mathcal{R}|\times T_{u}\times 2}$. The policy maps the current closed loop situation to a plan and the output of $g$ is a finite horizon action sequence. The generated actions are rolled out by a differentiable kinematic model with sampling period $\Delta t$. In closed loop simulation, the ego agent executes its fixed policy, the reactive agents execute the first part of $\mathbf{U}_{\tau}$, and replanning repeats at the next replanning time.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Instance-Centric Scene Encoding", "weight": 1.0} -->

We use an instance-centric scene encoding that represents agents and map elements in a shared token space and produces both scene context features and per-agent marginal trajectory proposals. We provide a brief explanation of this method here and refer to for a more detailed introduction. Each scene is decomposed into a set of agent instances and a set of map polyline instances. Each instance is expressed in its own local frame. For an agent instance, the local frame origin is the last observed pose at replanning time $\tau$ and the local $x$ axis is aligned with the agent heading at that time. The agent input features include a fixed length history of motion and kinematics in this local frame. For a map polyline instance, the local frame origin is the polyline centroid. The local $x$ axis is aligned with the polyline tangent direction defined by the polyline geometry. In our implementation, the tangent is the unit direction induced by the ordered polyline points from first to last after consistent ordering. Traffic light state is represented as a categorical attribute of lane elements and is embedded into the polyline features.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Instance-Centric Scene Encoding", "weight": 1.0} -->

Let $c_{i}\in\mathbb{R}^{2}$ denote the instance center in a common scene frame and $q_{i}\in\mathbb{R}^{2}$ the unit direction associated with instance $i$ (agent heading or lane tangent). We define the displacement $p_{i\to j}=c_{j}-c_{i}$ and the relation descriptor where $\angle(\cdot,\cdot)$ returns a signed wrapped angle in $(-\pi,\pi]$. An MLP maps $r_{ij}$ to an edge embedding $e_{ij}\in\mathbb{R}^{D}$. A stack of Symmetric Fusion Transformer layers, abbreviated SFT, refines $Z$ using attention conditioned on these relational embeddings. This yields a scene context representation $\hat{\mathbf{c}}_{\tau}$. The encoder also outputs $K$ marginal future trajectory proposals per agent with associated scores.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-C Marginal priors and PCA latent construction", "weight": 1.0} -->

Given the $K$ proposal futures and their probabilities, each proposal trajectory is mapped to an action sequence using an inverse dynamics routine consistent with the rollout model. Each action is $\mathbf{u}=[a,\dot{\psi}]^{\top}$, resulting in a flattened interleaved vector where $D_{u}=2T_{u}$ is the action dimension per agent over the horizon. Action sequences are compressed into a low-dimensional latent space using principal component analysis (PCA). We compute global affine statistics $(\boldsymbol{\mu}_{u},\boldsymbol{\sigma}_{u})$ over all action sequences in the training set (across agents and proposals) and fix them for normalization. With these statistics and PCA components $\mathbf{V}\in\mathbb{R}^{D_{u}\times d}$, where $\oslash$ denotes elementwise division.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-C Marginal priors and PCA latent construction", "weight": 1.0} -->

This process yields (i) a latent target $\mathbf{y}_{0}$ from the ground-truth action sequence and (ii) for each agent $i$, a set of latent proposal modes $\{\mathbf{y}^{i,(k)}\}_{k=1}^{K}$. Across all agents, the marginal prior set is $\{\mathbf{y}^{i,(k)}\mid i=1..N,\,k=1..K\}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-D Latent diffusion denoiser", "weight": 1.0} -->

A diffusion model generates a clean latent plan by learning to reverse a gradual noising process. The clean joint latent plan is $\mathbf{y}_{0}\in\mathbb{R}^{N\times d}$. For each diffusion step $s$, we define a noisy version $\tilde{\mathbf{y}}_{s}$ obtained by applying a variance preserving forward process to $\mathbf{y}_{0}$. b\) Forward process and training objective. We use a variance preserving diffusion process defined by a noise schedule $\{\beta_{s}\}_{s=1}^{S}$. We set The quantity $\bar{\alpha}_{s}$ determines how much of the clean signal remains at step $s$. Small $s$ yields $\bar{\alpha}_{s}$ close to one and $\tilde{\mathbf{y}}_{s}$ close to $\mathbf{y}_{0}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-D Latent diffusion denoiser", "weight": 1.0} -->

We initialize the noise scale using the marginal proposal set produced by the scene encoder. For agent $i$ we have proposal latents $\{\mathbf{y}_{i,(k)}\}_{k=1}^{K}\subset\mathbb{R}^{d}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-D Latent diffusion denoiser", "weight": 1.0} -->

This equation defines the noised latent under the schedule $\{\bar{\alpha}_{s}\}$; it is obtained by injecting step-dependent noise according to $\bar{\alpha}_{s}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-D Latent diffusion denoiser", "weight": 1.0} -->

The denoiser $D_{\theta}(\tilde{\mathbf{y}}_{s},s,\hat{\mathbf{c}}_{\tau},\mathcal{P}_{\tau})$ predicts the scaled noise term $\boldsymbol{\sigma}^{\text{train}}_{y}\odot\boldsymbol{\epsilon}$ from the noisy input $\tilde{\mathbf{y}}_{s}$ and the conditioning. We train it with the standard DDPM noise prediction loss At inference we optionally use DDIM to reduce the number of denoising steps while keeping the same denoiser.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-D Latent diffusion denoiser", "weight": 1.0} -->

Inverse PCA map used for rollout. Given a noisy latent, we form the one step estimate of the clean latent and map it back to action sequences using the fixed PCA inverse and fixed affine statistics computed once from the training set. For each agent $i$, where $\hat{\mathbf{y}}^{i}\in\mathbb{R}^{d}$, $\mathbf{V}\in\mathbb{R}^{D_{u}\times d}$, and $\hat{\mathbf{u}}^{i}\in\mathbb{R}^{D_{u}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-D Latent diffusion denoiser", "weight": 1.0} -->

The vector is then reshaped into $\{\hat{\mathbf{u}}_{t}^{i}\}_{t=1}^{T_{u}}$ with $\hat{\mathbf{u}}_{t}^{i}=[\hat{a}_{t}^{i},\ \dot{\hat{\psi}}_{t}^{i}]^{\top}$. We then roll out We define a state matching loss on the rollout and combine it with the diffusion loss as, where $\lambda_{\mathrm{state}}=0.5$ and $\lambda_{\mathrm{diff}}=1$. c\) Shifted Gaussian initialization from proposal statistics. Motivated by OptTrajDiff's proposal-informed Gaussian initialization, we warm-start the reverse process from a Gaussian whose mean and diagonal scale are given by Eq.. At reverse step $S$, we sample

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-E Guidance at inference", "weight": 1.0} -->

We optionally refine sampled plans using gradient-based guidance in latent space at inference time.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-E Guidance at inference", "weight": 1.0} -->

Here, $\hat{\mathbf{y}}_{0\mid s}$ is the one-step analytic estimate of the clean latent implied by the denoiser at the sampled diffusion step $s$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-E Guidance at inference", "weight": 1.0} -->

Objective-based guidance. We define a cost $J(\hat{\mathbf{X}})$ on the rolled-out trajectories and refine the sampled plan to reduce it. In our experiments, where $J_{\mathrm{map}}$ penalizes map violations using an off-road signed-distance proxy and $J_{\mathrm{coll}}$ penalizes near-term overlaps using a smooth distance-based proxy. At inference, we decode the denoiser output to actions, roll out $\hat{\mathbf{X}}$, and apply a gradient step that updates the latent plan: optionally, only in late reverse steps and without backpropagating through $D_{\theta}$ across diffusion steps.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-E Guidance at inference", "weight": 1.0} -->

The guidance (i) tightens constraint satisfaction in rare corner cases and (ii) performs targeted, counterfactual edits without retraining. The same mechanism can incorporate additional differentiable objectives.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-E Guidance at inference", "weight": 1.0} -->

Safety-critical game-theoretic guidance. We model safety-critical interactions as a pursuit--evasion game with an IBR-style refinement during guided sampling. Agents are split into ego-controlled and adversarial sets, with costs $J_{\mathrm{ego}}(\hat{\mathbf{X}})$ and $J_{\mathrm{adv}}(\hat{\mathbf{X}})$. From the current latent estimate $\hat{\mathbf{y}}_{0}$, we alternate a few best-response updates: adversaries increase $J_{\mathrm{ego}}$, ego agents decrease it, and each step decodes and rolls out before computing gradients. This adapts both sides and produces interactive, scene-consistent adversarial scenarios.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-E Guidance at inference", "weight": 1.0} -->

initial state X0; replanning interval Δr; horizon Tu; ego policy πego; rollout model f; SIMPL encoder; denoiser Dθ 3: Encode the current scene at Xτ to obtain context $\hat{\mathbf{c}}_{\tau}$ and marginal proposals {(yτ(k), πτ(k))}k = 1K 4: Sample a joint latent plan $\hat{\mathbf{y}}_{0,\tau}$ by reverse diffusion conditioned on $\hat{\mathbf{c}}_{\tau}$ and {(yτ(k), πτ(k))}k = 1K 5: Decode $\hat{\mathbf{y}}_{0,\tau}$ to a joint action plan $\hat{\mathbf{U}}_{\tau}=\{\hat{\mathbf{u}}^{i}_{t}\}_{i=1..N,\,t=1..T_{u}}$ 6: Roll out

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-E Guidance at inference", "weight": 1.0} -->

$\hat{\mathbf{X}}_{\tau}=f(\mathbf{X}_{\tau},\hat{\mathbf{U}}_{\tau})$ 7: Execute the first Δr steps: ego uses πego, reactive agents use $\hat{\mathbf{U}}_{\tau}$ Algorithm 1 Closed-loop simulation with latent diffusion policy

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-A Dataset", "weight": 1.0} -->

The experiments utilize the Waymo Open Motion Dataset (WOMD), which contains over 500 hours of driving data collected across multiple cities in the United States. Each scenario comprises a 9-second segment, including 1 second of history and an 8-second prediction horizon. We train the diffusion model on a randomly sampled subset of 200k scenarios for efficiency. Closed-loop ablations utilize 500 randomly selected scenarios from the WOMD validation split.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A Dataset", "weight": 1.0} -->

Diffusion training details. We use two-stage training: a marginal proposal model first provides SIMPL context and per-agent multi-modal proposals, then a joint latent diffusion model is trained on the resulting proposal-derived priors. The second-stage DDPM uses a variance-preserving process over the joint standardized PCA latent plan with $d=32$, $S=100$ diffusion steps and a linear $\beta$ schedule $\beta_{s}\in[10^{-4},5\cdot 10^{-2}]$. The Transformer denoiser uses hidden size 128, 8 attention heads, dropout 0.3, $\lambda_{\mathrm{state}}=0.5$ and $\lambda_{\mathrm{diff}}=1$. We use AdamW with learning rate $5e{-4}$, weight decay $10^{-3}$ and bfloat16 mixed precision.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Baselines and Training Setup", "weight": 1.0} -->

We select baselines to isolate the main modeling choices: IDM provides a low-compute rule-based reference, SIMPL-AR tests marginal proposal selection without joint diffusion, the unguided joint diffusion baseline isolates guidance, and the context-only ablation removes proposal-informed initialization. All methods use the state/action definitions from Sec. III and the rollout model $f$ from Eq.. All learned models are trained on a single NVIDIA H100 GPU.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B1 IDM (rule-based baseline)", "weight": 1.0} -->

The IDM baseline is a lightweight deterministic reference. Each non-ego agent follows IDM-style longitudinal control along an assigned lane centerline with heuristic car-following and a default desired speed, without SIMPL predictions or diffusion sampling. This is a simple rule-based reference rather than a calibrated microscopic traffic simulator.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B2 SIMPL-AR (collision-aware selection)", "weight": 1.0} -->

At each replanning time $\tau$, SIMPL predicts $K=6$ multi-modal futures per reactive agent with confidence scores. We convert each proposal to actions via inverse dynamics, roll out with $f$, and select one mode per agent by approximately minimizing with a lightweight circle-overlap proxy where $p^{i,(k_{i})}_{\tau}$ is the confidence score of the selected mode, $\lambda_{\mathrm{coll}}$ weights the collision penalty, and $r_{i}$ is a circle radius derived from the agent footprint. $T_{\mathrm{look}}$ is the collision lookahead horizon. This SIMPL-AR setup is consistent with a prior WOSAC-style simulator that builds autoregressive closed-loop execution on top of multi-modal motion predictors plus lightweight rollout-time consistency checks.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-B3 Joint diffusion baseline (no guidance)", "weight": 1.0} -->

The stage-2 baseline uses the same architecture and training setup as the main model and is trained for 25 epochs. At inference, it samples a joint latent plan $\mathbf{y}\in\mathbb{R}^{N\times 32}$ conditioned on SIMPL scene context $\hat{\mathbf{c}}_{\tau}$ and the marginal prior set, then decodes to actions and rolls out with $f$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-B4 Diffusion without prior initialization (context-only)", "weight": 1.0} -->

This ablation removes proposal-informed prior initialization and marginal-prior tokens while still conditioning on the SIMPL scene encoding. Reverse diffusion is initialized from a standard Gaussian rather than the shifted Gaussian in Eq.. The same stage-2 architecture is trained for 25 epochs.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C Closed-loop evaluation", "weight": 1.0} -->

We evaluate with receding-horizon closed-loop simulation in Waymax. At each replanning time $\tau$, we sample a joint $8$ s rollout for all reactive agents (up to $N=64$ closest to SDC), execute the first control step at $10$ Hz, and then replan from the updated simulator state.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-D Metrics", "weight": 1.0} -->

We report standard closed-loop safety and fidelity metrics aligned with prior controllable simulation work: collision rate for interaction feasibility, off-road rate for map consistency, minADE for positional accuracy, and Wasserstein-1 acceleration/jerk histograms for kinematic naturalness. We do not report Waymo Open Sim Agents Challenge metrics, which require the official evaluator and large-scale submission protocol.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-D Metrics", "weight": 1.0} -->

Off-road. A binary flag indicating that an agent departs the drivable road surface. We determine this using the agent position relative to oriented road-graph (lane-edge) reference points and report the off-road rate as the fraction of agents that become off-road at any point during rollout, aggregated over all agents and generated scenarios.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-D Metrics", "weight": 1.0} -->

Collision. Collision rate, reported as the fraction of agents that participate in at least one collision during rollout.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-D Metrics", "weight": 1.0} -->

Realism. Following prior work, we report the average Wasserstein-1 distance between *L1-normalized* histograms of longitudinal acceleration, lateral acceleration and jerk computed from generated trajectories and ground-truth trajectories, aggregated over all agents and timesteps.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-D Metrics", "weight": 1.0} -->

Best-of-$N$ displacement error (minADE). For each scene, we compute the minimum average $\ell_{2}$ displacement error to the logged future over $N$ stochastic rollouts, then average over valid agents and scenes.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-D Metrics", "weight": 1.0} -->

Accelerated sampling and runtime. To reduce test-time latency, we use DDIM sampling and vary the number of reverse steps to expose an explicit balance between speed and quality. We report per-replanning runtime together with safety and realism metrics in Table II.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-D Metrics", "weight": 1.0} -->

SIMPL-AR (collision-aware selection) Ours † (w/o Prior Init) † Trained from scratch without prior initialization from SIMPL marginal proposals. The SIMPL scene encoding is still used as context. TABLE I: Closed-loop simulation metrics. For diffusion models we report mean and standard deviation over 5 random seeds. Deterministic baselines are shown without variance.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-D Metrics", "weight": 1.0} -->

Ours (w/o Prior Init) TABLE II: Accelerated DDIM sampling ablation with a fixed model and varying reverse diffusion steps. Runtime per replanning step.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-D Metrics", "weight": 1.0} -->

Fig. 3: Qualitative results. Top: Nominal policy (w/o guidance) our method produces scene-consistent predictions for many reactive agents that remain interactive and map-adherent. Middle: Objective-based guidance encourages stronger lane adherence and safer behaviors (agent 9 accelerating while other agents stay on the road). Bottom: Game-theoretic guidance where agent 2 (magenta) attacks the ego evader (green).

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-D Metrics", "weight": 1.0} -->

Ego Adv Coll [%] ↑ TABLE III: Safety-game guidance aggressiveness ablation (100 scenarios). We vary wpursue and η (fixed model and scenarios) and report mean ± std over R = 3 seeds.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Tables I and II indicate a consistent pattern in closed-loop multi-agent simulation. Enforcing *joint* scene consistency improves interactive feasibility compared to composing agents independently while map and kinematic fidelity remain sensitive to representation choices and training objectives.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Closed-loop performance trends. The rule-based and marginal/autoregressive baselines provide reasonable rollouts but can exhibit interaction failures when multiple agents' futures are combined without an explicit joint consistency mechanism. In contrast, joint diffusion denoising couples agents through shared refinement steps conditioned on the same scene context which tends to reduce multi-agent conflicts and improve interaction coherence in closed-loop rollouts. However, improvements are not uniform across metrics and residual map violations and kinematic artifacts remain. For example, in Table I, our *unguided* model reduces the collision rate from 11.70% to 4.83% and reduces the off-road rate from 9.10% to 3.27% while maintaining comparable realism and positional accuracy. Qualitative rollouts are shown in Fig. 3. These findings suggest that interaction modeling is important but not sufficient on its own to guarantee strong map adherence and physically consistent motion. Performance also depends on accurate scene encoding, map priors and the rollout model assumptions.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Ablations without proposal-informed initialization further suggest that proposal priors help keep sampling stable by constraining the reverse process toward plausible regions of the trajectory space. When this initialization is removed, the denoiser must rely more heavily on context-only conditioning which can increase sensitivity to sampling variance and exacerbate rare failure modes.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Effects of accelerated sampling and step count. We evaluate sampling efficiency by varying the number of reverse DDIM denoising steps per replanning iteration, with all other model and scenario settings fixed and report closed-loop safety and fidelity metrics. The DDIM ablation study in Table II shows that modest denoising steps can preserve quality while reducing latency. Runtime increases approximately in proportion to the number of denoising steps, whereas the benefit of additional refinement diminishes beyond a moderate step count. With proposal-informed initialization, even a small number of reverse steps can preserve quality, whereas very few steps leave limited opportunity to resolve multi-agent conflicts and improve constraint satisfaction when initialization is removed. At high denoising steps, additional computation may produce smaller improvements in average closed-loop metrics and may shift sampling behavior toward increased variability which does not necessarily improve mean collision or off-road rates. In our experiments, 5 to 10 reverse denoising steps consistently provide the most favorable balance relative to larger step counts which add compute without proportional gains in closed-loop metrics.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Without proposal-informed initialization, the context-only variant generally needs more reverse steps to achieve comparable closed-loop quality, indicating slower convergence toward plausible joint trajectories. This balance becomes increasingly important when guidance is enabled, as guidance increases computation per step and may dominate runtime at higher step counts. Efficiency comes from denoising a compact joint action-latent, warm-starting the reverse process with proposal-informed initialization and using only a small number of denoising steps at test time which keeps replanning latency low without retraining.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Guidance, Behavior and Limitations. Objective-based guidance provides a practical mechanism for targeted scenario editing and constraint tightening without retraining and it enables controllable behavior shifts while preserving interactive rollouts. In our experiments, it consistently improves safety-oriented outcomes when tuned with moderate weights. Its effectiveness depends on the differentiability and calibration of the chosen objectives. Guidance can introduce compromises: stronger optimization pressure for a specific objective may slightly degrade other fidelity metrics if the objective is imperfectly aligned with the data distribution. Moreover, gradient-based guidance introduces computational overhead and can be sensitive to hyperparameters such as step size and weighting.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Guidance aggressiveness. Table III varies the pursuit weight $w_{\mathrm{pursue}}$ and step size $\eta$ to control adversarial guidance strength. More aggressive settings increase the ego and adversary collision rate and impact severity, including higher impact speed but also increase off-road rate and reduce realism. This balance is essential for testing a policy under different criticality levels.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This work presents a diffusion-based method for closed-loop traffic scenario generation that produces realistic, interactive multi-agent behavior while remaining controllable at test time. The method combines instance-centric scene conditioning with a joint latent diffusion policy to generate scene-consistent rollouts under replanning. A key component is proposal-informed Gaussian initialization. Rather than starting reverse diffusion from isotropic Gaussian noise, initialization occurs from a shifted Gaussian whose mean and scale are computed from a marginal proposal model. This biases sampling toward plausible behaviors and improves sampling quality for joint generation.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Closed-loop simulation results indicate that joint denoising improves interaction consistency relative to composing marginal rollouts while inference-time guidance enables targeted scenario editing including safety-critical and adversarial interactions. Overall, the framework supports challenging yet plausible scenario generation for evaluation. Future work includes reporting Waymo Open Sim Agents Challenge metrics using the official evaluator and submission protocol, exploring scene-level rollout losses that penalize multi-agent inconsistency and training with closed-loop policy learning. We also plan to incorporate language conditioning for more intuitive control over scenarios.
