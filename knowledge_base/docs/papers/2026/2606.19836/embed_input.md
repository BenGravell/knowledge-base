<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

World Engine: Towards the Era of Post-Training for Autonomous Driving

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Autonomous vehicles must operate safely in the real world, where errors can have severe consequences. Although modern end-to-end driving policies excel in routine scenarios, their reliability is limited by the scarcity of safety-critical ``long-tail'' events in real driving datasets. These rare interactions define the practical safety boundary of the learned policy, yet they are difficult to collect at scale in the real world. Here we show that this fundamental limitation can be addressed by post-training pre-trained driving models on synthesized high-stakes interactions. We introduce World Engine, a generative framework that reconstructs high-fidelity interactive environments from real-world logs and systematically extrapolates them into realistic safety-critical variations. This paradigm enables reinforcement-based post-training to align policies with safety constraints, circumventing the physical risks inherent in real-world exploration. On a public benchmark built on nuPlan, World Engine substantially reduces failures in rare safety-critical scenarios and yields significantly larger gains than scaling pre-training data alone.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Furthermore, when deployed on a production-scale autonomous driving system, the resulting policy reduces simulated collisions and demonstrates measurable improvements in on-road testing, showing that post-training on synthesized, safety-critical interactions offers a scalable and effective pathway to safer autonomous driving. The full codebase suite, including training, is released to the public.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Artificial intelligence is undergoing a fundamental transition from digital cognition to Physical AI. Autonomous driving stands as one of the most advanced and socially consequential instances of this shift. Unlike virtual agents, autonomous vehicles perceive, reason, and act directly within the physical world, operating under the strict constraint of irreversibility: errors manifest as physical harm, economic loss, or threats to human safety. As such systems increasingly integrate into daily life, the central challenge is no longer basic task capability, but reliability under safety-critical conditions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Modern end-to-end autonomous driving systems, trained on millions of kilometres of fleet logs, can now handle the vast majority of everyday scenarios with human-level proficiency. However, this average-case performance masks a critical vulnerability: the operational safety boundary is defined not by the common, but by the "long tail" of rare events. While uneventful driving is abundant in training data, the abrupt pedestrian crossings, aggressive cut-ins, and complex adversarial interactions that could cause accidents remain statistically sparse.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This scarcity exposes a structural paradox at the heart of autonomous driving: the most safety-critical behaviours must be learned from the scarcest data. Unlike digital domains, where failures can be exhaustively explored, autonomous driving operates under rigid ethical, legal, and social constraints, and society cannot afford to collect safety-critical data at scale. Consequently, the most valuable learning signals residing at the boundary of safe control are systematically missing from naturalistic datasets.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Addressing this paradox remains the central obstacle to safe autonomy. Scaling data collection alone yields diminishing returns; accumulating millions of uneventful logs does little to improve robustness in rare moments. Current learning-based systems are thus forced to extrapolate beyond their training distributions, leading to brittle behaviour and unpredictable failures when confronted with novel or compounded risks. For autonomous driving to be safely deployable at scale, the field must move beyond passive data accumulation and establish new learning paradigms that explicitly address this long-tail data regime.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A potential solution to this data gap is suggested by the recent evolution of Large Language Models (LLMs). While scaling pre-training on massive corpora yields broad linguistic competence, standard models often struggle with complex, multi-step reasoning---a domain where high-quality natural data is inherently sparse. The field has responded by moving beyond passive pre-training towards post-training paradigms, which use synthesized reasoning chains by prompting and reinforcement learning to bridge these gaps. This shift is exemplified by systems such as DeepSeek-R1 and AlphaProof, which achieve superhuman performance in mathematical problem-solving and Olympiad-level competitions. Their success validates a crucial principle for autonomous driving: when naturally occurring driving data fails to adequately cover rare but safety-critical situations, learning must be actively guided through synthesis to densify the sparse, high-value regions of the data distribution.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Drawing on this insight, we introduce World Engine (WE), a learning framework that bridges the gap between the rarity of safety-critical events and the need for structured learning in autonomous driving systems. World Engine discovers failure-prone scenarios from real-world logs, reconstructs them into high-fidelity interactive worlds with diverse traffic variations, and applies reinforcement learning-based post-training to improve planner safety without exposing the real world to additional risk (Fig. 1).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To demonstrate the effectiveness of World Engine, we apply it to train and evaluate end-to-end autonomous driving agents on a large-scale open-source real-world driving dataset, including sensor data, HD maps and 3D annotations of traffic objects: nuPlan. We develop a photorealistic driving simulator using state-of-the-art neural rendering techniques to enable closed-loop evaluations of these agents. On this academic benchmark, we focus on a curated set of safety-critical long-tail scenarios and evaluate models in closed-loop rollouts, where compounding errors and the interactive reactions of other agents can lead to collisions or off-road failures. Across these rare cases, the full World Engine pipeline substantially improves closed-loop driving quality over the supervised pre-trained baseline, achieving higher success rates under imminent hazards.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, our data-scaling study reveals that simply increasing pre-training data yields diminishing returns on rare cases, whereas World Engine post-training delivers substantially larger gains than even doubling the pre-training data; extrapolating the scaling trend suggests that it remains competitive even against an order-of-magnitude ($\sim$`<!-- -->`{=html}10$\times$) increase in pre-training data (Fig. 2).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, we validate the proposed framework on a production-scale autonomous driving system. We train an end-to-end planning model on over 80,000 hours of real-world driving logs, resulting in a substantially strong base model. We then apply reinforcement post-training with World Engine to further improve its performance. We evaluate the model using an industry-grade closed-loop simulation platform with over 10,000 scenarios. Results show that, despite the strong baseline, the collision rate is reduced by up to 45.5% after post-training. We further validate the approach through a 200-kilometre real-world on-road test, achieving zero disengagements and improved safety in safety-critical scenarios. These results demonstrate that such post-training paradigms can further enhance the safety of already strong autonomous driving systems in real-world settings.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Overview of World Engine", "weight": 1.0} -->

The autonomous driving problem can be formulated as an end-to-end learning task that maps raw sensor observations to control actions. In this work, we instantiate this formulation using real-world driving logs (e.g., nuPlan), where sensor data and structured annotations are used to reconstruct interactive environments for training and evaluation. A key challenge lies in the scarcity of safety-critical and long-tail interactions in real-world driving logs, which fundamentally limits planner robustness (Fig. 1a). We introduce World Engine, a unified framework that shifts the closed-loop interactive data distribution toward long-tail scenarios beyond what real-world collection alone can provide, and adapts the end-to-end model through reinforcement learning post-training (Fig. 1b).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Overview of World Engine", "weight": 1.0} -->

The framework follows a four-stage pipeline: pre-train a base driving agent on large-scale real-world logs and leverage it to discover failure-prone long-tail events, reconstruct each discovered case into a photorealistic interactive simulation via 3D Gaussian Splatting, augment the reconstructed scenarios with diverse traffic variations through a controllable behaviour world model, and refine the agent via reinforcement post-training on the resulting rollouts (Fig. 1e). The following subsections describe each stage in detail.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Pre-training and Long-tail Event Discovery", "weight": 1.0} -->

The first step in World Engine is to identify the scenarios where learning matters most. Rather than synthesizing rare events from scratch or relying on manually designed scenarios, we ground event discovery in real-world driving logs, as they naturally capture complex multi-agent interactions, contextual dependencies, and realistic edge cases that are difficult to faithfully construct through manual design or synthetic perturbations.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Pre-training and Long-tail Event Discovery", "weight": 1.0} -->

We begin by training a base end-to-end autonomous driving model via imitation learning on large-scale driving data. This pre-trained agent serves as both a strong behavioural prior and a diagnostic probe: we feed each logged scenario to the base agent, obtain its planned trajectory, and execute a non-reactive rollout against the logged traffic in a lightweight simulator that operates on 3D bounding boxes and HD maps. Scenarios in which the agent's trajectory collides with logged objects or departs the road are flagged as safety-critical, as they reveal conditions where the current policy fails. These failure-prone cases constitute the long-tail subset that World Engine targets for augmentation.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Pre-training and Long-tail Event Discovery", "weight": 1.0} -->

This discovery strategy offers two advantages. First, the selected events are grounded in real sensor data and real traffic configurations, which ensures that the resulting training distribution remains physically plausible. Second, because the base agent itself defines the boundary of competence, the discovered events are directly aligned with the regions where post-training can yield the largest improvement.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Simulation Engine", "weight": 1.0} -->

Once a long-tail event is identified, the next step is to turn it into a simulation environment where the driving agent can practice and learn. We refer to this component as the simulation engine: it reconstructs each discovered scenario into a photorealistic, interactive world and orchestrates closed-loop rollouts where the ego agent and surrounding traffic interact in real time, enabling novel ego trajectories beyond the original recording.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Simulation Engine", "weight": 1.0} -->

The core of the simulation engine is a 3D Gaussian Splatting (3DGS)-based reconstruction pipeline. The simulator directly supplies object-level tracks and 3D bounding boxes for all dynamic agents, which are used to decompose the scene into a compositional scene graph separating the static background (roads, buildings, vegetation) from dynamic foreground objects (vehicles, pedestrians, cyclists). Each element is represented by a set of 3D Gaussians fitted to multi-view observations from the driving logs. This decomposition allows independent manipulation of individual objects---repositioning, removing, or altering the trajectory of any traffic participant---while preserving the photorealistic quality of the static surroundings (Fig. 1c). This capability is critical for generating diverse traffic variations.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Simulation Engine", "weight": 1.0} -->

A key property of this representation is free-viewpoint rendering: once the scene is reconstructed, it can be rendered from any camera pose, not only those recorded in the original log. This is essential for closed-loop simulation, where both the ego vehicle and surrounding traffic agents may follow trajectories that differ from the original log. As the ego agent takes novel actions and other agents are repositioned or re-planned, the simulation engine produces corresponding sensor observations in real time, maintaining visual fidelity to real-world camera data. The real-time rendering capability enables thousands of rollouts per scenario, which is necessary for reinforcement learning post-training at scale.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Behaviour World Model", "weight": 1.0} -->

While the simulation engine provides photorealistic sensor observations, the behaviour of surrounding traffic agents must also be modelled to enable meaningful closed-loop interaction. To achieve this, we introduce the behaviour world model, which generates realistic and diverse trajectories for surrounding agents that respond to the ego vehicle's actions.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Behaviour World Model", "weight": 1.0} -->

At its core, the behaviour world model is a learned diffusion model that treats multi-agent trajectory generation as a structured denoising process. Given the current scene context---including map topology, historical agent states, and the ego vehicle's planned action---the model generates future trajectories for all surrounding agents simultaneously. The stochastic nature of the diffusion process naturally produces diverse behaviour samples: the same initial condition can yield cooperative, aggressive, or hesitant traffic responses depending on the denoising path.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Behaviour World Model", "weight": 1.0} -->

Beyond stochastic generation, the model supports controllable behaviour synthesis through two mechanisms. First, goal conditioning allows desired endpoints or waypoints to be flexibly specified for individual agents---ranging from explicit constraints for targeted scenario generation to probabilistic sampling for coverage---steering their trajectories toward particular configurations such as cut-in manoeuvres or sudden lane changes. Second, optimization guidance steers the denoising process at each step by evaluating each candidate trajectory against a desired behavioural objective---for instance, favouring interactions that approach collision thresholds or penalising lane departures---and progressively nudging the generation toward compliant outputs. This requires no retraining of the base model, as the guidance operates solely during sampling.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Behaviour World Model", "weight": 1.0} -->

For flexibility, the simulation framework also supports alternative traffic models: log replay for deterministic reproduction of recorded behaviour, and an Intelligent Driver Model (IDM) for rule-based reactive traffic. These modes can be mixed within a single scenario, allowing some agents to follow the learned diffusion model while others replay logged trajectories or follow rule-based control. This combination of stochastic diversity, controllable generation, and flexible traffic modelling enables World Engine to produce counterfactual interactions that probe safety-critical dynamics. A single long-tail scenario can be expanded into hundreds of variations, each presenting different traffic responses that test the ego agent under a broad range of interactive conditions (Fig. 1d).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Reinforcement Post-training", "weight": 1.0} -->

The simulation engine and behaviour world model together produce diverse closed-loop rollouts from long-tail scenarios. Reinforcement post-training closes the loop by using these rollouts to refine the driving agent.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Reinforcement Post-training", "weight": 1.0} -->

We formulate the driving task as a partially observable Markov decision process (POMDP), where the agent receives camera observations, maintains internal state estimates, and outputs driving actions. The objective is to learn a policy that maximizes cumulative reward---reflecting safety (e.g., avoiding collisions and maintaining safe distances), comfort (e.g., smooth acceleration with low jerk), and progress (e.g., forward motion along the route)---while remaining close to the pre-trained policy. This balance is achieved through a behaviour-regularized reinforcement learning formulation, where a KL divergence penalty constrains the post-trained policy to stay near the pre-trained prior. The regularization prevents catastrophic forgetting of common driving competence while allowing targeted improvement in safety-critical regimes.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Reinforcement Post-training", "weight": 1.0} -->

The training data for post-training is drawn from a mixture of two sources: real-world logged trajectories and simulated rollouts generated by World Engine. The real data preserves the distribution of common driving situations, while the simulated data densifies the rare and safety-critical regions. This experience mixing strategy ensures that the agent improves on long-tail events without degrading performance on everyday driving by combining data-level and policy-level regularization: real-world log mixing preserves coverage of common scenarios, while the KL constraint limits deviations from the pre-trained policy.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Reinforcement Post-training", "weight": 1.0} -->

Within the simulated rollout, hard experience mining further selects the most informative frames for supervision. Not all frames in a rollout are equally valuable: we retain those where the current policy exhibits failure or near-failure behaviour, such as imminent collisions, off-road departures, or large deviations from human driving, and use them as prioritized training samples. By focusing supervision on these hard frames, the agent learns disproportionately from the moments where improvement matters most. A dense reward function provides intermediate feedback across safety, efficiency, and comfort objectives, guiding the reinforcement learning process---together with hard experience mining---toward safe and human-aligned driving behaviour.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Reinforcement Post-training", "weight": 1.0} -->

The four components described above---pre-training and long-tail event discovery, simulation engine, behaviour world model, and reinforcement post-training---form a closed-loop pipeline. Starting from a pre-trained agent, World Engine discovers its failure modes, reconstructs the corresponding scenarios into interactive worlds, generates diverse traffic variations, and uses the resulting rollouts for reinforcement post-training.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Reinforcement Post-training", "weight": 1.0} -->

This pipeline enables scalable post-training from rare events grounded in real data. Because every training scenario originates from an actual driving log, the learning signal remains physically plausible. Because the behaviour world model and simulation engine can generate many variations of each scenario, the agent encounters a rich distribution of interactive conditions far beyond what passive data collection can provide. And finally, because reinforcement post-training applies behaviour-regularized reinforcement learning, the resulting policy improves safety in critical regimes without sacrificing competence in common situations.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Implementation of World Engine", "weight": 1.0} -->

In this section, we describe the concrete implementation of World Engine on the publicly available dataset nuPlan, which serves as a reference implementation of our framework and is used for all our controlled ablation studies and quantitative analysis. Building upon this foundation, World Engine is also deployed and evaluated on a mass-produced ADAS development stack. Although the industrial setup involves additional engineering considerations, it preserves the same conceptual pipeline and learning objectives. The academic implementation therefore serves as a faithful abstraction of the system used in practice.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Simulation Engine", "weight": 1.0} -->

The photorealistic simulation engine is the key to enabling online exploration and data curation for training an end-to-end planner. It consists of two parts: reconstruction and controllable rendering.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Simulation Engine", "weight": 1.0} -->

In the reconstruction stage, we reconstruct the driving logs with a 3DGS-based approach. Given a set of images and LiDAR points captured within a spatial-temporal driving log, the reconstruction task aims to learn a 3DGS representation that can faithfully reproduce the observed sensor data while recovering the underlying geometric structure. With the 3D bounding box annotation of traffic agents, the dynamic objects are reconstructed separately from static background through a scene graph-based design. To ensure high-fidelity novel-view rendering, we incorporate dense geometric constraints, including depth and surface normal supervision during reconstruction, ensuring consistent structure and high-quality extrapolated views under novel camera poses.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Simulation Engine", "weight": 1.0} -->

In the controllable rendering stage, the simulation engine renders the corresponding sensor observations with given input ego pose and sensor extrinsic and intrinsic at timestamp $t$, along with the positions and heading angles of other non-ego vehicles. The 6-degree-of-freedom poses of both ego and non-ego vehicles are calibrated with the ground plane estimated from their trajectories. Controllable rendering is achieved by explicitly manipulating the reconstructed dynamic objects in the scene and rendering the camera observations from the updated ego camera location. Thanks to the efficient rasterization of 3DGS, the simulation engine supports real-time image rendering, enabling closed-loop simulation and scalable online data generation.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Simulation Engine", "weight": 1.0} -->

We next describe the detailed representation, rendering process, and optimization objectives used in the simulation engine.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Scene representation", "weight": 1.0} -->

To model dynamic driving scenes within a single traversal, Gaussian primitives are organized into a scene graph that separates static background structure from dynamic scene content. Specifically, the scene graph consists of two types of nodes: static nodes $\mathcal{G}_{\text{static}}$, representing stationary elements such as roads and buildings, and dynamic nodes $\mathcal{G}_{\text{dyn}}$, capturing moving traffic participants that may appear or disappear over time. This design enables stable reconstruction of the static environment while allowing dynamic objects to be independently manipulated during simulation and rollout.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Appearance modelling", "weight": 1.0} -->

We mitigate photometric inconsistency by two-stage calibration. First, LiDAR-guided exposure alignment is applied to correct global brightness variations by matching colours of projected LiDAR points across views. Second, we introduce learnable per-camera affine colour transforms, parameterized by a channel-wise scale and bias, which are shared across time for each camera and optimized jointly with the scene representation. These affine transforms absorb residual camera-specific photometric differences, improving cross-camera consistency during reconstruction.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Rendering and objectives", "weight": 1.0} -->

Pixel colours are obtained via alpha compositing in depth order: $\mathbf{c}_{p}=\sum_{i}\mathbf{c}_{i,p}\,\alpha_{i,p}\prod_{j<i}(1-\alpha_{j,p}),$ where $\mathbf{c}_{i,p}$ is the SH-evaluated colour contribution of Gaussian $G_{i}$ at pixel $p$, and $\alpha_{i,p}$ its projected opacity. During World Engine rollout, deployed simulation engine generates observation through states $\mathcal{O}=\mathcal{P}_{\psi}(\mathcal{S})$ in parallel.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Rendering and objectives", "weight": 1.0} -->

The Gaussian parameters are further optimized using a weighted combination of reconstruction and regularization objectives. For reconstruction loss, rendered images are supervised using a combination of $\ell_{1}$ loss and SSIM. Regularization objectives further introduce depth and normal regularization. Sparse LiDAR depth is incorporated using an inverse-depth loss: To improve local geometric consistency and prevent overfitting, a patch-wise normalized cross-correlation loss is applied: where $\Omega$ denotes the set of depth patches. For normal regularization, rendered normal maps are regularized using pseudo-normals $N$ computed from depth gradients, together with a total variation penalty: To prevent degenerate Gaussian shapes, a flattening regularizer is applied: where $\mathbf{s}_{i}$ denotes the anisotropic scale of Gaussian $G_{i}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Details of reconstruction pipeline", "weight": 1.0} -->

Reconstruction starts from a driving scenario identified by a key frame within a specific driving log. Given the key frame timestamp, we extract a spatio-temporal clip consisting of 3 seconds of history and 8 seconds of future frames, using sensor data sampled at 10 Hz. If the vehicle trajectory within the extracted time window spans less than 50 meters, we extend the end of the clip until either the accumulated trajectory length reaches 50 meters or the end of the driving log is encountered. This ensures sufficient spatial coverage for stable reconstruction.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Details of reconstruction pipeline", "weight": 1.0} -->

To avoid redundant static observations caused by prolonged low-speed or stationary periods, we downsample frames in segments where the ego vehicle speed falls below a predefined threshold. In addition, clips extracted from nearby key frames may partially overlap in time and space. To prevent repeated reconstruction of highly similar content, overlapping clips are merged and reconstructed jointly as a single scene instance.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Handling of image distortion", "weight": 1.0} -->

We observe that raw camera images exhibit significant lens distortion, which adversely affects both reconstruction quality and pose estimation. All raw images are undistorted using OpenCV with an optimal undistortion mode that preserves the original field of view during reconstruction. At inference time, we render the image using the optimal undistorted camera intrinsics, and then map it back to the original distorted image space to match the raw image.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Simulation platform and metrics", "weight": 1.0} -->

We implement a simulation platform that integrates simulation engine with behaviour world model, and serves as the execution backbone for reinforcement post-training and evaluation. The simulator is responsible for generating closed-loop rollouts, computing task-specific metrics and rewards, and recording rollout data for subsequent training and analysis. To ensure compatibility with diverse end-to-end planners, the simulation platform communicates with external planning models through a lightweight file-based interface. At each simulation step, the simulator serializes sensor observations and scene states to disk, while the planner reads these inputs and returns planned trajectories, which are then executed in the simulator. For traffic agent modelling, the simulator supports either log replay or a reactive Intelligent Driver Model (IDM). Trajectory tracking is executed using an LQR controller with a bicycle dynamic model. For open-loop evaluation, we use the PDM Score introduced in the NAVSIM benchmark. For closed-loop evaluation in the World Engine simulator, we report both per-scene success rate (SR) and closed-loop PDM Score (PDMS^∗^).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Simulation platform and metrics", "weight": 1.0} -->

SR measures whether the ego vehicle completes the episode without collision or off-road failure, while PDMS^∗^ evaluates the quality of the closed-loop trajectory under interactive simulation, providing a complementary progress- and safety-aware metric.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Behaviour World Model", "weight": 1.0} -->

While the simulation engine provides photorealistic observation of the surrounding environment, the dynamics of traffic agents still need to be modelled to facilitate a comprehensive traffic simulator for end-to-end model training. This behaviour world model goes beyond traditional rule-based or log-replay simulations by utilizing a generative diffusion framework capable of synthesizing both stochastic and adversarial behaviours.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Behaviour World Model", "weight": 1.0} -->

We frame traffic layout simulation as a sequence modelling task, where driving scenarios are represented as structured tokenized states for both agent behaviours and map features, enabling simultaneous prediction of all agent futures. Concretely, the agent behaviours are defined as $\mathbf{x}\in\mathbb{R}^{A\times\mathcal{T}\times D}$, where $A$ denotes the maximum agent capacity, $\mathcal{T}$ represents the physical temporal horizon, and $D$ signifies the dimensionality of agent attributes. Static environmental features are encoded in the map tensor $\mathbf{c}\in\mathbb{R}^{L\times N\times D^{{}^{\prime}}}$, representing $L$ lanes with $N$ points per lane and $D^{{}^{\prime}}$ attributes (coordinates and types).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Behaviour World Model", "weight": 1.0} -->

Building upon this vectorized representation, the behavioural world model $T_{\theta}$ employs a Diffusion Transformer (DiT) that generates the agent tensor $\mathbf{x}$ by reversing a stochastic differential process. Let $\mathbf{x}^{0}\in\mathcal{X}$ represent a clean agent feature from the distribution $p(\mathbf{x})$. Training begins with an initial state $\mathbf{x}^{0}$, which undergoes progressive noise injection over time steps $\mathbf{k}=[k_{a,\tau}]\in(0,1]^{A\times\mathcal{T}}$ where each $k_{a,\tau}$ represents the degree of Gaussian noise added to corresponding tokens, until reaching a Gaussian noise distribution at $\mathbf{x}^{k}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Behaviour World Model", "weight": 1.0} -->

The model is optimized by minimizing the mean-square error (MSE): where $\mathbf{\alpha}_{\mathbf{k}}$, $\mathbf{\sigma}_{\mathbf{k}}$ are scale weights that describe the magnitude of the data $\mathbf{x}^{0}$ and the noise $\epsilon$ at the denoising step $\mathbf{k}$, $\theta$ parameterizes the denoiser $\epsilon_{\theta}$, and $\mathbf{c}$ is the map tensor guiding the denoising process. During sampling, all agent tokens are iteratively generated from the standard Gaussian noise with the denoising step. To enable goal-oriented generation, the model sets a keep mask $\mathbf{m}_{c}$ to ensure targets and past tokens remain fixed during sampling: where $\mathbf{s}$ is the next denoising step, $\mu$ and $\Sigma$ are determined by DiT $\epsilon_{\theta}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Behaviour World Model", "weight": 1.0} -->

To ensure that generated scenarios align with realistic driving priors, we incorporate classifier guidance, adjusting the agent tensor $\mathbf{x}$ iteratively to enforce behavioural constraints at each denoising step. Concretely, we separate overlapping agents along their centreline's opposite direction to avoid collisions, smooth trajectories, and pull agents toward the nearest lanes for on-road driving.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Reinforcement Post-training", "weight": 1.0} -->

The simulation engine and behaviour world model create diverse counterfactual scenarios, yet these corner cases still need exploratory feedback guided by human priors. The reinforcement post-training stage combines experience curation with reinforcement learning to turn diverse experience into human-aligned improvements.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Reinforcement Post-training", "weight": 1.0} -->

The reinforcement learning task of autonomous driving can be formulated by the POMDP $\{\mathcal{O},\mathcal{S},\mathcal{A},r,\gamma\}\subset\mathcal{\tau}$ over future horizon $T$. $o\in\mathcal{O}$ is the observation (i.e., image) from raw sensors. $s\in\mathcal{S}$ denotes the state information of ego vehicle, traffic participants and map. $a\in\mathcal{A}$ is the driving action. $\mathcal{T}_{\theta}(s_{t+1}|s_{t},a_{t})$ is the world model; $r:\mathcal{S}\times\mathcal{A}\rightarrow\mathbb{R}$ denotes the shaped reward, and $\pi_{\text{ref}}$ denotes the pre-trained policy distribution.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Reinforcement Post-training", "weight": 1.0} -->

The optimal driving policy $\pi_{\phi}(a|o)$ is learned by maximizing the cumulated expected value of reward $R(\tau)=\sum_{t=0}^{T}\gamma^{t}r(s_{t},a_{t})$. We express this objective as a behaviour-regularized reinforcement learning problem: where $\lambda$ is the regularization weight toward the pre-trained driving expert $\pi_{\text{ref}}$. The experience distribution $p$ is defined as a mixture of real logged trajectories and simulated transitions generated by the world model and simulation engine: Logged transitions $\tau\sim p_{\mathrm{real}}$ are drawn from human driving data.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Reinforcement Post-training", "weight": 1.0} -->

Simulated transitions $p_{\mathrm{sim}}$ are produced by rolling out the policy $a_{t}\sim\pi_{\phi}(\cdot\mid o_{t})$ within the world model $s_{t+1}\sim\mathcal{T}_{\theta}(\cdot\mid s_{t},a_{t})$ and simulation engine $o_{t}\sim\mathcal{P}_{\psi}(s_{t})$. This mixture yields a unified experience source and allows the overall objective to be formulated as a regularized policy optimization problem.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Reward shaping", "weight": 1.0} -->

The shaped reward function provides structured feedback that guides the policy toward safe and human-aligned behaviour during post-training. For each trajectory, we compute signals that reflect core driving objectives, including collision avoidance, drivable-area compliance, ego progress along the route, time-to-collision margin, and ride comfort. These rewards help distinguish high-quality behaviours from poor ones and amplify the contribution of informative corner cases. Experiences with higher driving quality naturally yield higher returns, while unsafe or implausible behaviours receive lower values. This ensures the policy learns not only from diverse and counterfactual scenarios but also understands which outcomes are desirable.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Hard experience mining", "weight": 1.0} -->

Given mixture experience distribution $p$, hard experience mining gathers informative experiences from both logged data and world-model rollouts. We focus on a mixture of scenario clips that reveal rare or safety-critical interactions, such as near collisions, challenging negotiations, recovery manoeuvres, or clear departures from human driving. These mixed samples vary in driving quality, and are assigned different weighted learning curricula. All candidate samples are further checked for physical plausibility. The resulting mixture of high-quality corner cases helps the system learn from instructive experiences while remaining grounded in human driving.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Base End-to-End Driving Model", "weight": 1.0} -->

In recent years, a variety of end-to-end planning methods have emerged, leveraging onboard sensor data that typically include surround-view cameras and, optionally, LiDAR inputs, together with ego-vehicle information such as IMU poses, localization, and navigation commands. These models aim to predict the vehicle's future trajectory over several seconds, which is subsequently used by the control module to control vehicle motion. They are generally trained in a supervised manner by imitating human driving behaviour. To further enhance spatial understanding and overall planning performance, these models are often jointly optimized with multiple auxiliary tasks, such as object detection, map element detection, motion prediction, and occupancy estimation.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Base End-to-End Driving Model", "weight": 1.0} -->

In this work, we adopt a standardized and robust model architecture. Specifically, we employ a BEVFormer encoder to process multi-camera inputs and other sensory data, generating a fixed-size BEV feature representation that effectively captures the surrounding spatial context from a bird's-eye-view perspective. An object tracking decoder and a map segmentation decoder are included for perception supervision following the design of UniAD. A scoring-based planning decoder is included, which selects the best trajectory across a pre-defined trajectory vocabulary, conditioned on BEV feature.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Experiment", "weight": 1.0} -->

We evaluate the proposed World Engine on two test settings: a visually realistic, challenging closed-loop simulation built upon a real-world dataset, and a large-scale closed-loop simulation and field testing on mass-produced Autonomous Driver Assistance System (ADAS).

<!-- chunk {"id": "body-0059", "role": "body", "section": "NuPlan experiments", "weight": 1.0} -->

The nuPlan dataset comprises 1,282 hours of driving logs, of which approximately 10% include synchronized sensor data. Each vehicle is equipped with 8 surrounding cameras and 5 LiDAR sensors operating at 10 Hz. We adopt the widely used navtrain split for training, which contains exactly 103,288 scenes, each defined by a key frame with 1.5 seconds of historical context and a 4-second future horizon. Evaluation is performed on the navtest, which consists of 12,146 scenes, as well as a rare-event subset of navtest comprising 288 failure-prone scenarios. The closed-loop simulation and evaluation is conducted on the rare scenes.

<!-- chunk {"id": "body-0060", "role": "body", "section": "NuPlan experiments", "weight": 1.0} -->

For data-scaling experiments, the amount of pre-training data is varied from 12.5% to 100% of navtrain. Unless otherwise specified, the base agent used for post-training is pre-trained on navtrain~50pct~. The model backbone consists of a ResNet-50 and a feature pyramid network (FPN) that takes as input 8 camera views with 4 temporal frames per view. The extracted features are processed by a six-layer BEVFormer encoder and a six-layer planning decoder, as well as parallel tracking and mapping decoders. In total, the model contains 58.3 million trainable parameters. Pre-training is carried out on eight NVIDIA H100 GPUs and consists of two stages: perception pre-training for 164 hours over 40 epochs, followed by planning pre-training for 15 hours over 8 epochs. After pre-training, we evaluate the base model on navtrain~50pct~ and identify 5,340 long-tail scenes. Using World Engine, we generate a dataset of 31,508 frames from these scenarios, which is subsequently used for reinforcement-learning-based post-training.

<!-- chunk {"id": "body-0061", "role": "body", "section": "NuPlan experiments", "weight": 1.0} -->

The post-training stage costs 11 hours over 8 epochs.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Huawei ADS experiments", "weight": 1.0} -->

The pre-training dataset is collected from both internal testing fleets and user vehicles spanning multiple vehicle models. Each vehicle is equipped with a heterogeneous sensor suite, including ten surrounding cameras, a fused LiDAR, radar, GPS, and an inertial measurement unit (IMU). After large-scale data mining, automatic labelling, and dataset balancing, the final dataset used for pre-training comprises approximately 80,000 hours of driving data, organized into more than 10 million clips of 25 seconds each. During post-training, we mix 1.0 million clips generated by World Engine with 5.0 million clips sampled from common driving data. Pre-training is conducted on Ascend 910B Neural Processing Units (NPUs) for a total of 40,000 NPU-hours, followed by 15,000 NPU-hours of post-training. For on-road evaluation, the trained policy is deployed on a Huawei AITO M9 vehicle in development mode. In this setting, minimal post-processing is applied: the model outputs are combined with a lightweight control module and used to directly actuate the vehicle chassis.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Huawei ADS experiments", "weight": 1.0} -->

Although exhaustive route-level deduplication between the pre-training corpus and the on-road test routes is infeasible at this data scale, the specific real-world interactions encountered during testing---including the cut-in event documented in Fig. 5c,d---are inherently non-reproducible and could not have been present in any logged training data, providing a genuine test of out-of-distribution generalisation.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Safety-critical Closed-loop Simulation", "weight": 1.0} -->

To evaluate the effectiveness of World Engine post-training, we construct a fully open-sourced, reproducible benchmark of safety-critical driving scenes built on the publicly available nuPlan dataset, which comprises 128 hours of real-world driving logs, including sensor data, annotated traffic agents, and high-definition maps. The benchmark is constructed from the official test split of nuPlan, ensuring that all evaluation scenarios are disjoint from the data used for pre-training. The benchmark focuses on rare cases---short sequences where baseline models are most likely to fail, such as near-collision, off-road deviation, or abrupt interactions with other agents (Fig. 3b). Each test case represents a localized 3D collision-centric scenario extracted from large-scale driving logs, and faithfully reconstructed within the World Engine simulation environment. Each simulation clip spans 4 seconds, capturing the most failure-prone temporal window in which the driving model must react to an imminent hazard. We perform open-loop evaluation using the metric PDM Score and closed-loop evaluation in World Engine simulation using the success rate metric (Fig. 3a).

<!-- chunk {"id": "body-0065", "role": "body", "section": "Safety-critical Closed-loop Simulation", "weight": 1.0} -->

A scenario is considered successful if the vehicle passes the four-second episode without a collision or off-road infraction, reflecting its ability to maintain safe and controllable behaviour under stress.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Safety-critical Closed-loop Simulation", "weight": 1.0} -->

To examine the data efficiency of World Engine post-training, we design a scaling experiment that varies the amount of pre-training data from 12k to 103k scenes and evaluates each model on three metrics: open-loop PDM Score on common cases, open-loop PDM Score on rare cases, and closed-loop success rate on rare cases (Fig. 2a). We then apply World Engine post-training starting from the 50k-scene base model and compare the resulting gains against the pre-training scaling curve. While increasing pre-training data yields steady but saturating improvements---particularly on rare cases where safety-critical events are scarce---World Engine post-training produces gains that exceed the scaling trend on all three metrics. The open-loop improvements confirm that the post-trained agent learns better trajectory planning, while the closed-loop gains further show that this improved planning translates into safer interactive behaviour under compounding dynamics. In particular, World Engine post-training on the 50k-scene base model already surpasses the performance of a model pre-trained on more than twice as much data.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Safety-critical Closed-loop Simulation", "weight": 1.0} -->

When extrapolating the scaling curve, achieving comparable closed-loop gains through pre-training alone would require approximately an order-of-magnitude more real-world data, highlighting that targeted post-training on synthesized rare events is a far more data-efficient path to safety improvement than scaling passive data collection.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Safety-critical Closed-loop Simulation", "weight": 1.0} -->

We additionally compare different post-training data sources and interaction models (Fig. 2b--d and Table 1). Post-training on common driving logs provides limited or even negative benefit for rare closed-loop evaluation: although it improves common open-loop PDMS, it slightly reduces rare closed-loop PDMS^∗^ from 60.98 to 60.20, indicating that common logs alone do not address long-tail interactive failures. Post-training on rare logged scenes improves rare open-loop PDMS from 47.14 to 59.20, but yields only limited closed-loop gains, suggesting that fixed rare logs are insufficient for robust interactive behaviour. Rare synthetic replays further improve rare open-loop PDMS and substantially increase closed-loop success rate, but they yield the lowest ego progress in this comparison, indicating that binary success alone does not fully capture progress-aware closed-loop driving quality.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Safety-critical Closed-loop Simulation", "weight": 1.0} -->

In contrast, rare rollouts without the behaviour world model provide reactive closed-loop experience, better preserve common-case performance, and improve rare closed-loop PDMS^∗^ to 67.33. Incorporating augmented traffic interactions through the behaviour world model yields the best overall rare closed-loop performance, achieving the highest PDMS^∗^ of 70.12 and the highest success rate of 88.89%, while maintaining strong common open-loop PDMS. Full quantitative results, including success rate, ego progress, and PDMS^∗^, are provided in Table 1. supervised fine-tuning on rare logs post-training on common logs post-training on rare logs post-training on rare synthetic replays post-training on rare rollouts w/o Behaviour WM post-training with World Engine Table 1: Comparison of post-training paradigms on the nuPlan benchmark. We compare different post-training strategies using open-loop PDM Score (PDMS) on common and rare scenarios, and closed-loop metrics on rare scenarios. SR denotes success rate, EP denotes ego progress, and PDMS∗ denotes the closed-loop PDM Score.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Safety-critical Closed-loop Simulation", "weight": 1.0} -->

The base model achieves 85.64 and 47.14 open-loop PDMS on common and rare cases, respectively, with 73.66% SR, 46.71 EP, and 60.98 PDMS∗ in rare closed-loop evaluation. Supervised fine-tuning on rare logs provides only modest improvements over the base model. Post-training on common logs improves common open-loop PDMS but degrades rare closed-loop SR and PDMS∗, reducing SR from 73.66% to 69.62% and PDMS∗ from 60.98 to 60.20, highlighting the need for long-tail event discovery. Post-training on rare logs substantially improves rare open-loop PDMS to 59.20, but does not improve rare closed-loop SR. Post-training on rare synthetic replays improves rare open-loop PDMS to 62.69 and SR to 87.19%, but reduces common open-loop PDMS to 82.61 and yields the lowest EP of 32.49, suggesting that binary rare-case success can improve while common-case retention and progress-aware driving quality degrade.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Safety-critical Closed-loop Simulation", "weight": 1.0} -->

Post-training on rare rollouts without the behaviour world model recovers strong common open-loop performance and achieves the highest EP of 56.74, together with an improved PDMS∗ of 67.33. The full World Engine pipeline, which incorporates behaviour-world-model traffic augmentation, achieves the best overall rare closed-loop performance, with the highest SR of 88.89% and the highest PDMS∗ of 70.12, while also obtaining the highest common open-loop PDMS of 88.95. Relative to the base model, World Engine improves rare closed-loop SR by 15.23 percentage points and PDMS∗ by 9.14; relative to rare rollouts without the behaviour world model, it improves SR by 10.93 percentage points and PDMS∗ by 2.79. These results show that combining long-tail event discovery, reactive generated rollouts, and behaviour-model traffic augmentation yields the strongest overall closed-loop safety and driving-quality gains while maintaining strong open-loop performance.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Production-scale Driving Validation", "weight": 1.0} -->

To validate World Engine at production scale, we apply it to Huawei Advanced Driving System (ADS), an autonomous driving system deployed on over one million vehicles and capable of point-to-point driving in both urban and highway settings. We leverage the development and testing stack of the system, where an end-to-end model directly takes sensor inputs and produces trajectories to the control module to drive the vehicle. We first train the base end-to-end model on more than 80,000 hours of real-world driving data collected from over 100 cities. Following the same pipeline as the earlier experiments, we identify failure-prone scenarios from the training logs, reconstruct them via 3DGS-based rendering, augment traffic interactions through the behaviour world model, and refine the base model through reinforcement post-training.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Production-scale Driving Validation", "weight": 1.0} -->

We evaluate the post-trained model using the industrial quality assurance system, which performs asynchronous, hardware-in-the-loop closed-loop simulations on production on-board hardware. In each simulation, rendered sensor streams are fed to the end-to-end model running on the vehicle's computing unit, forming a full sensor-to-control closed loop. Each test scenario runs for approximately 20 seconds; across all scenarios the simulation totals over 60 hours, equivalent to roughly 3,000 km of driving---all consisting of eventful, interaction-rich situations rather than uneventful cruising. Across six safety metrics spanning general and rare driving scenarios, World Engine post-training consistently reduces failure events (Fig. 4a). In rare interaction scenarios (1,206 test cases), collisions with pedestrians and cyclists decrease by 15.8% and collisions at intersections decrease by 24.1%. In rare cut-in scenarios (643 test cases), cut-in collisions decrease by 45.5% and time-to-collision events decrease by 13.4%.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Production-scale Driving Validation", "weight": 1.0} -->

These safety gains do not come at the cost of general driving performance: across 10,986 common cases, dynamic collisions decrease by 13.2% and static collisions by 20.0%, indicating that long-tail post-training also improves everyday driving competence. A representative simulation case is shown in Fig. 4b,c: the base model fails to brake in time and collides with a cut-in vehicle, while the post-trained model decelerates proactively and avoids contact.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Production-scale Driving Validation", "weight": 1.0} -->

We further conduct on-road testing over multiple runs totalling approximately 200 km across routes in Shanghai (Fig. 5a,b). Across all three runs, the post-trained model completes the full 200 km with zero disengagements, whereas the base model triggers one safety-critical intervention. Even a single intervention over 200 km remains a substantial reliability failure for deployment, particularly because it occurs in a rare but safety-critical cut-in interaction. Fig. 5c,d illustrate this incident: an adjacent vehicle, unaware of the test vehicle approaching from behind, begins to merge into the ego lane. The base model fails to respond to the cut-in and even attempts to accelerate; the adjacent vehicle is forced to abort its lane change abruptly to avoid a collision (Fig. 5c)---a situation that poses clear safety risks. Under a similar condition, the post-trained model recognizes the cut-in early and smoothly adjusts its speed, allowing the ego vehicle to pass safely without requiring evasive action from either party (Fig. 5d). These results, together with additional nighttime driving scenarios (Fig. 6), demonstrate that the safety improvements from World Engine transfer from simulation to real-world deployment on production vehicles.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

World Engine reframes autonomous driving learning under the long-tail regime as a post-training problem: instead of relying on passive fleet-scale collection to eventually observe rare events, it discovers failure-prone scenarios from real logs, reconstructs them into interactive photorealistic worlds, expands them through counterfactual traffic variations, and improves end-to-end planners via reinforcement learning. Across a safety-critical closed-loop benchmark reconstructed from nuPlan, post-training in World Engine improves success rate and trajectory feasibility, and can deliver closed-loop gains comparable to adding substantially more pre-training data, highlighting a data-efficient path for safety alignment when rare events are the bottleneck. Scaling to a mass-produced ADAS stack, World Engine reduces failure rates in a safety-critical benchmark (up to 45.5% in cut-in tests) while maintaining performance on common cases, suggesting that targeted long-tail post-training can improve safety without sacrificing everyday driving competence. From a practical standpoint, these results carry significant implications for the industry.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

Our data-scaling analysis shows that World Engine post-training can match the safety gains of approximately 10$\times$ more pre-training data when extrapolating the scaling curve, which in practice would require proportionally larger fleets, longer collection campaigns, and substantially higher annotation costs. By shifting the focus from passive data accumulation to targeted synthesis and reinforcement on rare events, World Engine offers a more cost-effective path to resolving long-tail safety problems and can substantially shorten the iteration cycle for improving autonomous driving systems.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Limitations", "weight": 1.5} -->

We note several limitations of the current framework. First, the long-tail event discovery stage can only identify failure modes that are already present in the collected driving logs. If a safety-critical scenario type has never been recorded---for example, an unusual road geometry or an entirely novel agent behaviour---it cannot be discovered or reconstructed by the current pipeline. Extending discovery beyond logged data, for instance through procedural scenario generation or adversarial search in a learned latent space, remains an open direction. Second, the fidelity of World Engine is bounded by its two simulation components. The 3DGS-based simulation engine produces high-quality images near the recorded trajectories but degrades when the simulated ego path deviates substantially from the original log, introducing visual artefacts that may affect policy learning. The behaviour world model, while capable of diverse traffic generation, does not yet capture all real-world interaction patterns with high fidelity, particularly those involving pedestrians, cyclists, or unstructured road users. Narrowing this sim-to-real gap is essential for further improving the transfer of post-training gains to deployment.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Limitations", "weight": 1.5} -->

Third, the reward function used in reinforcement post-training is based on principled but manually defined signals, such as collision avoidance, lane adherence, and route progress. These rewards encode general safety and driving objectives, yet they may not capture all the nuances of human driving preferences. Developing learned or verifiable reward functions that can adapt to more complex driving norms is a promising avenue for future work.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Scalability and iterative refinement", "weight": 1.0} -->

The current framework is validated with a single round of post-training. A natural extension is iterative refinement, where the improved agent is re-evaluated to discover new failure modes, and successive rounds of World Engine post-training are applied. However, in our experiments with the relatively small model (58.3M parameters), we observe that multiple rounds of post-training tend to destabilize the policy, likely because the model lacks sufficient capacity to absorb corrections without interfering with previously learned behaviours. Whether larger models or more sophisticated regularization strategies can support stable multi-round post-training remains an open question. A related observation concerns how failure modes evolve as the base model scales. In the Huawei ADS experiments, where the base model is trained on over 80,000 hours of data, the proportion of scenarios identified as long-tail events is substantially smaller than in the academic setting. Importantly, even with fewer discovered long-tail events, post-training still yields meaningful safety improvements. This finding indicates that World Engine can continue to provide gains as base models grow stronger, targeting an increasingly narrow but consequential set of failure modes.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Future work on world modelling", "weight": 1.5} -->

In this work, we develop a world modelling framework for autonomous driving that combines 3DGS-based neural rendering with a behaviour world model to generate realistic and controllable behaviours of surrounding agents. The proposed approach satisfies key requirements for post-training, including controllability, realism, efficiency, and robustness. A current limitation arises from imperfections in 3DGS reconstruction, particularly when large deviations occur between simulated rollout trajectories and the original real-world trajectories. As video generation technology continues to advance, this world modelling framework could be extended to video-based world models, which have shown promise in embodied navigation and beyond-the-view scene imagination, offering improved realism, controllability, and diversity.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Towards general Physical AI", "weight": 1.0} -->

The core insight behind World Engine---that safety-critical learning requires active synthesis rather than passive collection---is not specific to driving. Any Physical AI system that must operate reliably in the real world faces the same structural challenge: the most consequential failures are the hardest to observe in natural data. Robot manipulation systems, legged locomotion policies, and surgical robots all share this property. In these areas, the long tail of rare but high-consequence events defines the practical safety boundary, and is systematically under-represented in training data. The discover--world-modelling--post-train pipeline introduced in this work offers a general template for addressing this challenge. Given a pre-trained policy and a set of recorded task executions, one can identify failure-prone episodes, reconstruct them into interactive worlds, generate diverse variations, and apply reinforcement post-training to improve robustness in the identified regimes.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Towards general Physical AI", "weight": 1.0} -->

The specific instantiation of each stage will vary across domains---3DGS rendering and behaviour world models may be replaced by video world models or physics-based simulation depending on the application---but the overall logic remains the same: ground learning in real failures, expand coverage through controllable synthesis, and refine the policy through targeted reinforcement. We believe that this paradigm of post-training on synthesized rare events, bridging pre-training on broad natural distributions with targeted reinforcement on safety-critical regimes, represents a promising direction for building reliably safe Physical AI systems.
