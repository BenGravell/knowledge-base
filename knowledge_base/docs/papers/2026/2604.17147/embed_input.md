<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

ScenarioControl: Vision-Language Controllable Vectorized Latent Scenario Generation

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce ScenarioControl, the first vision-language control mechanism for learned driving scenario generation. Given a text prompt or an input image, Scenario-Control synthesizes diverse, realistic 3D scenario rollouts - including map, 3D boxes of reactive actors over time, pedestrians, driving infrastructure, and ego camera observations. The method generates scenes in a vectorized latent space that represents road structure and dynamic agents jointly. To connect multimodal control with sparse vectorized scene elements, we propose a cross-global control mechanism that integrates crossattention with a lightweight global-context branch, enabling fine-grained control over road layout and traffic conditions while preserving realism. The method produces temporally consistent scenario rollouts from the perspectives different actors in the scene, supporting long-horizon continuation of driving scenarios. To facilitate training and evaluation, we release a dataset with text annotations aligned to vectorized map structures. Extensive experiments validate that the control adherence and fidelity of ScenarioControl compare favorable to all tested methods across all experiments.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Large-scale datasets have been indispensable for the progress of autonomous driving, providing multi-modal labeled data across regions and conditions. However, real-world logs alone are insufficient to capture rare but safety-critical events, such as wrong-way drivers. Evaluating these edge cases is essential for safe and reliable systems, yet relying solely on collected data is highly sample-inefficient.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Simulators bridge this gap by enabling safe, repeatable, and scalable experimentation. Traditional rule-based simulators such as CARLA, SMARTS, and MetaDrive provide controllable virtual worlds for perception and planning research, yet their handcrafted world design limits realism and diversity, particularly for rare events. Recent generative approaches, such as Driving Diffusion and Panacea, introduce controllability by conditioning on structured "control layouts" derived from existing scenarios which steer generation by projecting logged scenes into intermediate control representations. Behavior- and interaction-level methods control agent dynamics to create challenging closed-loop interactions, but commonly assume a given road graph and initial scene context. Even for a given initial scenario description, these methods often struggle to generate long-tail events as the datasets used to train them contain few of such examples. To the best of our knowledge, no existing method allows for vision-language-controlled scenario generation.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In parallel, diffusion-based and data-driven simulation work has made substantial progress on generating realistic and diverse driving scenes from data. These methods treat scenario synthesis as a generative modeling problem over vectorized or rasterized representations, either placing actors on an existing road graph or generating both the road graph and actor positions jointly. Generative models have been shown to produce high-fidelity structured outputs -- road topology and traffic participants that are directly consumable by downstream components such as motion planning, sensor simulation, end-to-end driving, and multimodal future generation. However, a crucial gap remains: while realism and diversity are consistently improving, the controllability at the scenario-level of the layouts themselves is still limited. Generation is either entirely uncontrolled - by sampling from the latent space - or with control signals taken from existing scenarios, and extrapolation does not expose interpretable control knobs. We propose ScenarioControl to bridge this gap. ScenarioControl enables vision-language control of diffusion-based generation, unlocking controllable synthesis of structured driving scenarios and camera sensor simulation for the ego, and any other actor in the scene.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unlike other methods, it does so without relying on given logged scene configurations or auto-labeled control layouts. The resulting scenarios are plug-and-play with established simulators and autonomy stacks.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To this end, we introduce a novel cross-global control mechanism that conditions sparse vectorized scene tokens on dense features, from either a text prompt or a dashcam ego image, via two complementary branches: a cross-attention branch for fine-grained control and a lightweight global-context branch for capturing high-level scene intent. Conditioning on natural language and visual cues enables goal-directed scenario synthesis that both reflects real-world context and targets specific long-tail regimes. By steering road geometry, agent placement, and traffic conditions with a text prompt or a single ego dashcam-style image, generation moves beyond unconstrained sampling while preserving realistic structure and dynamics, crucial for synthesizing safety-critical cases and building targeted evaluation/training sets. In addition to enabling prompt- and image-conditioned scene generation, ScenarioControl also supports scene outpainting and long-horizon video continuation, maintaining temporal and visual consistency. We confirm ScenarioControl's fidelity and controllability with quantitative experiments, while qualitative results demonstrate adherence to conditioning and diverse long-horizon rollouts.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a vision--language conditioned vectorized latent diffusion model that generates full vectorized driving scenes, including lane topology, agent placement, and traffic signals conditioned on text prompts or dash-cam-style ego images.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce a new conditioning mechanism that fuses sparse, vectorized road layouts with dense prompt and image representations, enabling fine-grained control over generation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate controllability, diversity, and fidelity of the generated scenarios for arbitrary actors in the scene, confirming that the proposed method performs favorably compared to existing methods while providing fine-grained vision-language control.

<!-- chunk {"id": "body-0011", "role": "body", "section": "ScenarioControl", "weight": 1.0} -->

In the following, we first describe our scene representation and vectorized scene generation method (Sec. 3.1). Next, we describe the proposed conditioning mechanisms for camera observations or natural language text prompts (Sec. 3.2), also illustrated by Figure 1. In Sec. 3.3 and Figure 2, we describe scenario-guided video generation through vision-language control.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Scene Representation and Generation", "weight": 1.0} -->

We generate the initial scene by jointly modeling the underlying map structure and the actors' initial states in a bird's-eye-view (BEV) representation with elevation information. Specifically, we generate each scene within a ${{64m} \times 64}m$ field of view. A scene is then defined as a graph $\mathcal{I} = {\{\mathcal{O},\mathcal{M}\}}$, comprising a set of objects $\mathcal{O}$ and a map structure $\mathcal{M} = {\{\mathcal{L},\mathbf{A}\}}$. The map structure consists lane centerlines $\mathcal{L}$ and their connectivity graph $\mathbf{A}$. Our objective is to sample a scene $\mathcal{I} \sim p{( \cdot |\mathcal{C})}$ from some distribution $p$, conditioned on inputs $\mathcal{C}$, which can be either an image captured from the perspective of an agent in the scene or a text prompt describing the scene.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Scene Representation and Generation", "weight": 1.0} -->

In contrast to existing scenario diffusion approaches that abstract the environment in a purely two-dimensional BEV representation, we augment the object parametrization with vertical structure by incorporating elevation $z$ and object height $h$. This provides essential elevation cues for downstream camera and sensor-data synthesis, facilitating faithful reprojection of generated scenarios into the image domain as shown in Fig. 5.

<!-- chunk {"id": "body-0014", "role": "body", "section": "ScenarioControl for Vectorized Latent Diffusion", "weight": 1.0} -->

We propose a controllable vectorized latent diffusion model, as illustrated in Fig. 1, where we introduce the *cross-global control mechanism* that fuses sparse vector tokens with dense attention-based conditioning from prompts and images.

<!-- chunk {"id": "body-0015", "role": "body", "section": "ScenarioControl for Vectorized Latent Diffusion", "weight": 1.0} -->

First, we train a transformer-based vectorized autoencoder that encodes scene elements into a compact latent representation. We then train a diffusion model with $\epsilon$-predictor $\epsilon_{\theta}$ over the latents of the autoencoder $\mathbf{Z} = {\lbrack\mathbf{Z}_{\mathcal{O}},\mathbf{Z}_{\mathcal{L}}\rbrack}$ with variable cardinalities $(N_{o},N_{l})$. With condition $\mathcal{C}$, we minimize the DDPM $\epsilon$-prediction objective with

<!-- chunk {"id": "body-0016", "role": "body", "section": "ScenarioControl for Vectorized Latent Diffusion", "weight": 1.0} -->

where $\mathbf{Z}_{\tau}$ are noisy latents at step $\tau$, composed of $N_{o}$ object latents and $N_{l}$ lane latents, and the noise vector decomposes as $\mathbf{\epsilon} = {(\mathbf{\epsilon}_{\mathcal{O}},\mathbf{\epsilon}_{\mathcal{L}})}$. The conditioning inputs $\mathcal{C}$ comprise dense control signals $\mathcal{C}_{I}$ (*image*) and $\mathcal{C}_{P}$ (*prompt*) used in cross-attention, and the default control tokens $\overline{c}$ that encode the number of agents and lanes $N = {(N_{o},N_{l})}$ and the scene/domain label $\mathcal{s}$ (e.g., Singapore, Las Vegas, Boston, Pittsburgh in nuPlan), injected via AdaLN-Zero conditioning.

<!-- chunk {"id": "body-0017", "role": "body", "section": "ScenarioControl for Vectorized Latent Diffusion", "weight": 1.0} -->

We next describe the proposed multi-modal control mechanism in more detail, which supports conditioning from both scene prompts and agent-perspective images.

<!-- chunk {"id": "body-0018", "role": "body", "section": "ScenarioControl for Vectorized Latent Diffusion", "weight": 1.0} -->

Prompt Conditioning. Given a prompt describing the present scene and actors, we employ a text encoder $\mathcal{E}_{P}$ that extracts token embeddings as

<!-- chunk {"id": "body-0019", "role": "body", "section": "ScenarioControl for Vectorized Latent Diffusion", "weight": 1.0} -->

where $M_{P}$ is the number of prompt tokens and $d_{P}$ is the embedding dimension of the text encoder. The embeddings $\mathbf{E}_{P}$ are then projected through an MLP layer with the *linear projection weights* $\mathbf{W}_{P}$ to obtain control tokens $\mathbf{F}_{P} \in {\mathbb{R}}^{M_{P} \times d}$, where $d$ denotes the latent dimension used for agent or lane representations

<!-- chunk {"id": "body-0020", "role": "body", "section": "ScenarioControl for Vectorized Latent Diffusion", "weight": 1.0} -->

These prompt control tokens enter the control mechanism/attention by providing keys/values and are combined with the self-attention outputs.

<!-- chunk {"id": "body-0021", "role": "body", "section": "ScenarioControl for Vectorized Latent Diffusion", "weight": 1.0} -->

Agent-Perspective Image Conditioning. Given a forward-facing agent-perspective image $\mathcal{C}_{I}$, e.g., a dashcam style image, we extract dense features with a vision backbone $\mathcal{E}_{I}$ and depth estimator $\mathcal{E}_{D}$ as

<!-- chunk {"id": "body-0022", "role": "body", "section": "ScenarioControl for Vectorized Latent Diffusion", "weight": 1.0} -->

where $M_{I}$ denotes the number of image tokens, $d_{\text{feat}}$ the feature dimension of the vision backbone, and $d_{\text{depth}}$ the dimension of the estimated depth map. We use pretrained models for both the vision backbone and the depth estimator, and both are frozen during training. Both image features and depth maps are projected to the model's hidden dimension $d$ via learned linear mappings. Further, we add a non-trainable sine-cosine positional embedding $\mathbf{P}$ to the image features and depth maps, enforcing a shared spatial encoding across modalities

<!-- chunk {"id": "body-0023", "role": "body", "section": "ScenarioControl for Vectorized Latent Diffusion", "weight": 1.0} -->

where $\mathbf{W}_{\text{feat}}$ and $\mathbf{W}_{\text{depth}}$ are learned *linear projection weights* mapping modality-specific features to the shared hidden dimension $d$, and $\mathbf{P}$ ensures alignment within the same image coordinate frame across both image features and depth maps. Finally, we concatenate these position-aware tokens to form the control feature representation $\mathbf{F}_{I} = {\lbrack\mathbf{F}_{\text{feat}},\mathbf{F}_{\text{depth}}\rbrack}$.\

<!-- chunk {"id": "body-0024", "role": "body", "section": "ScenarioControl for Vectorized Latent Diffusion", "weight": 1.0} -->

Cross-Global Control Mechanism. Given the conditioning features, $\mathbf{F}_{I}$ and $\mathbf{F}_{P}$, we introduce a control mechanism to steer scenario generation. We employ $N_{\text{DM}}$ factorized attention blocks, each applying (in order) object-to-lane, lane-to-lane, lane-to-object, and object-to-object self-attention (SA) over the stacked object and lane tokens. The conditioning inputs are injected into each (CA) component, which we detail in the following section. An overview of the full mechanism is illustrated in Fig. 1.

<!-- chunk {"id": "body-0025", "role": "body", "section": "ScenarioControl for Vectorized Latent Diffusion", "weight": 1.0} -->

Conditioning vectorized scene tokens (lanes and agents) on agent-perspective images or scene prompt embeddings is inherently *unaligned*: a single scene token may depend on evidence from arbitrary subsets of conditioning tokens (e.g., occluded actors, distant lane cues, or globally specified textual constraints). Although cross-attention can, in principle, model such dependencies by allowing each query to attend to all keys, it provides little inductive structure and can be sample-inefficient when learning global context.

<!-- chunk {"id": "body-0026", "role": "body", "section": "ScenarioControl for Vectorized Latent Diffusion", "weight": 1.0} -->

We therefore compute cross-attention through two parallel branches that share the key/value projections of the conditioning stream. Given scene queries $\mathbf{Q} \in {\mathbb{R}}^{N_{q} \times d}$ and conditioning tokens $\mathbf{F} \in {\mathbb{R}}^{N_{k} \times d}$, we first compute cross-attention

<!-- chunk {"id": "body-0027", "role": "body", "section": "ScenarioControl for Vectorized Latent Diffusion", "weight": 1.0} -->

implemented efficiently with FlashAttention. In parallel, we introduce a small set of learned latent tokens $\mathbf{T} \in {\mathbb{R}}^{L \times d}$ that aggregate global context from $\mathbf{F}$, and expose this compact summary back to the scene queries

<!-- chunk {"id": "body-0028", "role": "body", "section": "ScenarioControl for Vectorized Latent Diffusion", "weight": 1.0} -->

with cost $\mathcal{O}{({{LN_{k}} + {N_{q}L}})}$. We combine both branches $\mathbf{Y} = {\mathbf{Y}_{1} + {\text{tanh}{(g)}\mathbf{Y}_{2}}}$ with a learned gate $g$. The gate is initialized such that ${\tanh{(g)}} \approx 0$ (i.e., $g = 0$), ensuring that the module initially reduces exactly to standard cross-attention. During training, the model can then progressively improve by selectively incorporating the additional global-context pathway. Since both pathways share the $\mathbf{K}{( \cdot )}$ and $\mathbf{V}{( \cdot )}$ projections, the parameter overhead remains minimal. Finally, the output is fused with multi-head self-attention via AdaLN-Zero modulation.

<!-- chunk {"id": "body-0029", "role": "body", "section": "ScenarioControl for Vectorized Latent Diffusion", "weight": 1.0} -->

Count Injection $f_{count}$. Graph-based representations offer a natural handle for controlling scene complexity: the number of lanes and agents can be set directly by initializing the corresponding numbers of lane and object nodes. For instance, generating a two-lane highway can be guided by instantiating the matching number of lane nodes, while in the image/prompt-conditioned setting, these counts can also be inferred from the conditioning signal. We therefore train a lightweight attention-based regressor $f_{\text{count}}$ that predicts the number of agents and lanes $(N_{o},N_{l})$ from the conditioning tokens $\mathbf{F}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "ScenarioControl for Vectorized Latent Diffusion", "weight": 1.0} -->

We note that compared to raster encodings or post-hoc control modules (e.g., ControlNet/T2I-Adapter ), our method directly operates on variable-length vector tokens, thereby preserving topology (lane connectivity) and scene structure.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Video Generation and Continuation", "weight": 1.0} -->

The use of vectorized scene graph representation $\mathcal{I}$ allows for direct BEV behavior simulation (with elevation) and camera sensor video synthesis without requiring an additional learned lifting step, as is the case for rasterized representations. For behavior simulation, the vectorized representation is used directly, while for video generation it is projected into the camera coordinate frame to create control inputs for a video diffusion model, both described in detail in the following.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Video Generation and Continuation", "weight": 1.0} -->

Behavior Simulation. Real-world cameras capture far beyond the 64m of an initial scenario layout. We use diffusion outpainting to construct large-scale scenes, which are then temporally rolled out using a behavior model $\mathcal{B}_{T}$ to produce diverse and behaviorally consistent agent trajectories. From this, we obtain scenario rollout representations ${\{\mathcal{I}_{t}\}}_{t = 1}^{T}$, which we reproject from BEV to camera space as wireframe sequences ${\{{\hat{\mathcal{C}}}_{\text{wire},t}\}}_{t = 1}^{T}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Video Generation and Continuation", "weight": 1.0} -->

Sensor Video Generation. We adapt a video generation model $\mathcal{V}_{i}$ to generate photorealistic clips from the behavior simulation. We train two variants: an image-conditioned model that uses the first frame $\mathcal{C}_{I}$ for appearance, and a prompt-conditioned model where the scene appearance is controlled by prompt description. Both are also trained to adhere to control sequences (wireframe renders of the behavior simulation) ${\{{\hat{\mathcal{C}}}_{\text{wire},t}\}}_{t = 1}^{T}$ to obtain photorealistic multi-frame renders ${\{{\hat{I}}_{t}\}}_{t = 0}^{T}$ that follow the simulated agent behavior (see Figure 2). Since we ground the video generation with the vectorized scene representation, we can transform the camera pose and generate videos from the perspectives of agents other than the ego agent whose camera capture was used to initialize the scene.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Video Generation and Continuation", "weight": 1.0} -->

We do so by re-rendering the wireframe representation with different camera extrinsics while maintaining a consistent text prompt.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Video Generation and Continuation", "weight": 1.0} -->

After adaptation, the model achieves fine-grained control of traffic behavior -- either as part of a video continuation task with the first-frame conditioning or in completely novel traffic situations from a prompt. Examples of controlled rollouts are reported in Figures 5 and 6, respectively.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Training", "weight": 1.0} -->

We adopt a two-stage training strategy. We first train the encoder $f_{e}$ and decoder $f_{d}$ to learn a reliable projection into the latent space. Next, we train the generative control mechanism and freeze the $f_{e},f_{d}$ weights and only train the dense condition blocks as described in Sec. 3.2, leveraging either the condition on Prompt or Image conditions.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Training", "weight": 1.0} -->

Additionally, we also employ *classifier-free guidance* (CFG). Specifically, the conditioning inputs $\mathbf{F}_{I}$ and $\mathbf{F}_{P}$ are randomly dropped with probability $p_{\text{CFG}}$ during training, encouraging the model to learn both conditional and unconditional behaviors. At inference, the guided prediction is computed as

<!-- chunk {"id": "body-0038", "role": "body", "section": "Training", "weight": 1.0} -->

where $w$ is the guidance weight controlling the strength of conditioning.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Training", "weight": 1.0} -->

Scene Layouts. At test time, we support three generation modes that reflect the asymmetry between prompt and image conditioning. Text prompts can describe the full surrounding around the ego agent, whereas a single camera frame only constrains the visible region in front of the ego. We therefore define two canonical scene layouts with dimension of 64x64m: 1. an ego-centered crop $\mathcal{F}_{P}$ and 2. a forward-only crop $\mathcal{F}_{I}$, obtained by shifting the crop such that the ego lies near the edge, to maximize coverage ahead.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Training", "weight": 1.0} -->

Crucially, we train the model on the same layout types used at inference, enabling consistent long-horizon rollouts. In practice, we use prompt-controlled synthesis for $\mathcal{F}_{P}$, image-conditioned completion for $\mathcal{F}_{I}$, and forward outpainting to extend either crop beyond the current field-of-view by sampling additional scene-graph nodes. Completion and outpainting are realized with masked denoising: latents corresponding to observed nodes are clamped, while the remaining tokens are sampled conditioned on $\mathcal{C}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Training", "weight": 1.0} -->

Collision Penalty. In practice, conditioning on prompt and images can induce *cluttered* scene hypotheses: images contain occlusions and missing context, while prompt is often underspecified. Both effects can place multiple agents into the same plausible region, resulting in overlapping boxes in the decoded scene graph. To encourage physically consistent layouts, we add a collision penalty $\mathcal{L}_{\text{col}}$ during training. Concretely, we decode intermediate latents at selected timesteps and compute pairwise $(i,j)$ overlaps ($\text{overlap}{(i,j)}$) between predicted agents $i,j$ with an intersection-over-union of their corresponding bounding boxes. We define the collision regularization loss as

<!-- chunk {"id": "body-0042", "role": "body", "section": "Training", "weight": 1.0} -->

where $\zeta$ controls smoothness. Since decoding is unreliable at low signal-to-noise ratios, we weight the penalty by $w_{\tau} = {1 - \sqrt{1 - {\overline{\alpha}}_{\tau}}}$, emphasizing later diffusion steps (smaller $\tau$) where the predicted geometry is more meaningful. This regularizer reduces agent overlap in the initial scene and improves global scene consistency under ambiguous conditioning.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Training", "weight": 1.0} -->

Implementation Details. Further details on scene definitions, model architecture, and training and inference procedures are provided in the appendix.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Vision-language Scenario Dataset", "weight": 1.0} -->

To facilitate the training of our vision and language conditioned model, we curate a dataset consisting of images, natural language descriptions, and BEV maps. We select driving scenarios with corresponding camera captures from the nuPlan dataset. To generate scene-level captions (e.g., "An intersection with a red light and multiple vehicles on the road. Pedestrians are standing on the sidewalk."), we first render BEV visualization images for each scene and use a VLM (GPT-4.1-mini) to produce descriptive captions.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Vision-language Scenario Dataset", "weight": 1.0} -->

This process results in a large-scale dataset containing approximately 500K high-quality captions, providing a rich foundation for training and evaluating our multimodal model. We provide additional details and dataset samples in the Appendix.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Experiments", "weight": 1.0} -->

Next, we first introduce the relevant evaluation metrics in Sec. 5.1. We then compare our proposed Cross-Global Control conditioning mechanism with other popular conditioning mechanisms in Sec. 5.2. Subsequently, we demonstrate superior adherence to control input with significant overlap in scene content in Sec. 5.3. Next, we analyze the inclusion to predict the actor and lane counts, $f_{count}$, and to suppress collisions through the loss $\mathcal{L}_{\text{col}}$. Lastly, we provide a generalization experiment on the Waymo motion dataset in Sec. 5.5. As our method focuses on *controllable* scenario generation, unconditioned comparison with prior methods are orthogonal but can still be found in the Appendix.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

Our evaluation focuses on two key aspects: generation quality and controllability. For generation realism, we adopt the same lane- and agent-level metrics as and are presented in the appendix. For controllability we introduce a set of control metrics to assess adherence to the provided conditioning signals that build on top of Agent Accuracy, Collision Rate and Control Adherence.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

Agent Accuracy. As a first step, we match generated agents to ground-truth agents and evaluate placement accuracy using average precision (AP). We compute ${AP}_{\delta}$ under center-point distance thresholds $\delta \in {{\{ 1.0,\, 2.0,\, 3.0\}}m}$ and report their mean, yielding an equally weighted measure of how well the control signal localizes agents. For the image-conditioned setting, AP is evaluated only for agents within the camera field of view (FOV), whereas for the prompt-conditioned setting, AP is computed over all generated agents.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

Collision Rate. We calculate the intersection over union over all predicted agents and report the fraction of scenarios with collisions in which actors and/or scene object bounding boxes intersect.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

Control Adherence. To quantify how well the predicted global, lane, and agent attributes follow the intended controls, we report three complementary metrics: Cosine Control Similarity (CCS), Shuffled Perturbation Gap (SPG), and Control Sensitivity Correlation (CSC), which are detailed in the appendix. CCS measures the alignment between the conditioning signal and the corresponding change in the generated scene, capturing direct controllability. SPG evaluates causal dependence by comparing the model's response to correct versus randomly shuffled conditions; a larger gap indicates stronger conditional consistency. CSC measures the correlation between variations in the conditioning input and variations in the generated output, reflecting the sensitivity and smoothness of control. We evaluate across three levels (global, lane, and agent) to separately assess control over large-scale layout, map structure, and agents.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Analysis of Control Mechanism", "weight": 1.0} -->

We validate our cross-global control module by comparing it against a broad set of attention designs commonly used for fusing dense conditioning signals with token sequences. To our knowledge, this is the first study that systematically evaluates such mechanisms for conditioning a *vectorized 3D scene graph* on dense prompt or image features. Specifically, we compare against simple concatenation, full cross-attention, gated attention, linear attention, AgentAttention, SAAP cross-attention, windowed attention, deformable attention, and squeezed attention. Quantitative results on lane- and agent-control metrics are reported in Tab. 3 with a qualitative result shown in Figure 7.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Analysis of Control Mechanism", "weight": 1.0} -->

Overall, attention-based conditioning mechanisms consistently outperform simple concatenation, and this trend holds for both prompt- and image-conditioned control. In the image-conditioned setting, our method reduces collision rate by $43.4\%$ and improves global CSC by $52.8\%$ over concatenation; moreover, it also improves over full cross-attention with a $2.7\%$ gain in agent CSC and a $4.6\%$ gain in AP, while also achieving stronger global and lane control. In the prompt-conditioned setting, our method also surpasses all other baselines on most controllability metrics. This confirms that our cross-global attention better captures the dense-to-sparse correspondences needed to align scene tokens with the specified controls $\mathcal{F}_{i}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Analysis of Control Adherence", "weight": 1.0} -->

Figures 3 and 4 illustrate controlled initial scenes generated with image and prompt conditioning, respectively: image inputs preserve visible structure and yield plausible completions of unobserved regions, while text prompts focus on key differentiators like intersection types allowing for more diverse sampling.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Analysis of $f_{\\text{count}}$ and $\\mathcal{L}_{col}$", "weight": 1.0} -->

Table 4 analyzes supervision for predicting the number of actors and lane elements from the conditioning signal via $f_{\text{count}}$, and for encouraging actor separation via the collision loss. The ablation study is conducted on a subset of the test set. Adding the collision loss consistently reduces collisions in the generated scenarios, regardless of whether $f_{\text{count}}$ is enabled. Using $f_{\text{count}}$ further lowers collision rate but also reduces AP, reflecting a trade-off: when the count is predicted rather than provided, the model tends to miss unseen or occluded actors outside the FOV. This reduces the number of placed agents, which decreases AP and, as a side effect, lowers the collision rate.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Generalization", "weight": 1.0} -->

We find that ScenarioControl generalizes across driving datasets to. We evaluate transfer to the Waymo Open Motion dataset and report results in Tab. 2. By injecting explicit text prompts as control signals during generation, our model produces scenarios that better match the target distribution, outperforming Scenario Dreamer across all reported metrics by up to 143%.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Comparisons to Agent Placement Techniques", "weight": 1.0} -->

ScenarioControl generates both lane topology and agent placements, producing truly novel scene realizations with a given conditioning signal. It can also be applied in map-conditioned settings: by encoding a pre-existing lane topology from an existing map and denoising only the agent latents the model places vehicles on a provided road topology without altering the underlying geometry. This allows a direct comparison with methods such as TrafficGen that focus solely on agent placement given a fixed map context.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Comparisons to Agent Placement Techniques", "weight": 1.0} -->

TrafficGen is an autoregressive method that generates vehicle initial states conditioned on the road context without any vision-language control, sampling actor positions following a general data distribution. Our text-conditioned model achieves an agent AP of 26.8%, compared to 5.5% for TrafficGen, representing a $\propto$ 4$\times$ improvement. This confirms that grounding agent placement in a conditioning prompt provides a strong signal for realistic and accurate vehicle initialization, substantially outperforming unconditioned placement on the same maps. The experiments are carried out on 14688 scenarios from the test split of the Waymo Open Motion dataset.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduce ScenarioControl, a multimodal conditional method for generating controllable and realistic driving scenarios with text prompts or images. We achieve prompt and visual conditioning through our proposed cross-global attention mechanism for vectorized scenarios that fuse dense multimodal cues with sparse map--agent structures. Additionally, the proposed method supports sensor video generation, producing temporally consistent renderings that visually ground the synthesized scenarios. Through extensive evaluations, we confirm that our control mechanism is favorable for prompt and image conditions, while allowing for diversity and fidelity, effectively bridging structured scenario simulation with realistic sensor-level inputs and human-interpretable guidance.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our method opens several promising directions for further research. An interesting direction is to leverage controllable scene generation to help autonomous vehicles anticipate traffic situations beyond line of sight information by synthesizing plausible continuations of partially observed environments. Extending our method to full multi-view and long-horizon visual conditioning could further improve consistency. Finally, extending the latent representation to unify initial scene generation and traffic simulation could allow the capture of additional semantics such as intent, weather, or interaction cues -- providing even finer control over scenario structure and agent behavior.
