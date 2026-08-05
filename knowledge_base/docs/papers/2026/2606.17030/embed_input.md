<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce Qwen-RobotWorld, a language-conditioned video world model for embodied intelligence. With natural language as a unified action interface, it predicts physically grounded future visual trajectories from current observations across robotic manipulation, autonomous driving, indoor navigation, and human-to-robot transfer. This unified formulation provides three promising application directions: synthetic data generation for policy training augmentation, scalable virtual environments for policy evaluation, and language-guided planning signals for downstream robot control. This is achieved through a three-part design: a) Double-Stream MMDiT with MLLM Action Encoding, where a 60-layer double-stream diffusion transformer couples frozen Qwen2.5-VL semantics with video-VAE latents through layer-wise joint attention; b) Embodied World Knowledge (EWK), an 8.6M video-text corpus (200M+ frames) with action-language mapping over 20+ embodiments and 500+ action categories; and c) General+Expert Progressive Curriculum, a two-stage training strategy that first learns general visual priors and then injects embodied specialization under a shared language interface.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Extensive results show strong competitiveness: ranks 1st overall on EWMBench and DreamGen Bench, outperforms all open-source models on WorldModelBench and PBench. Additional zero-shot analyses on RoboTwin-IF benchmark further support robust generalization and multi-view consistency.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Embodied intelligence requires agents to perceive, reason, and act within physical environments---spanning robotic manipulation at tabletop scale, autonomous navigation through urban traffic, and wayfinding across indoor spaces. Training such systems directly in the real world is costly, inefficient, and fraught with safety risks. World models offer a scalable alternative: by learning environment dynamics from observational data, they serve as interactive training platforms that allow embodied agents to acquire and refine behaviors without physical deployment.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A world model can be formalized as a state transition function: given a current state $s_{t}$ and an action $a_{t}$, it predicts the resulting state $s_{t+1}=f(s_{t},a_{t})$ 57. In video-based world models, states are visual observations (video frames or their latent representations), and the model generates future visual trajectories conditioned on the current observation and an action signal. The action $a_{t}$ can take various forms---low-level motor commands, high-level waypoint trajectories, or natural language instructions. Among these, natural language is the most general and accessible action representation 57: a single instruction such as "pick up the red cup and place it on the shelf" implicitly encodes the complete action sequence, goal state, and physical constraints, without requiring robot-specific control interfaces. Language actions can furthermore be utilized in two complementary directions: as an explicit input fused into the model's condition signal to govern state transitions, or as an output inferred post-hoc from generated video to serve as an action label.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This flexibility positions language-conditioned world models as universal simulation backbones that generalize across embodied platforms without interface redesign.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, a fundamental tension currently limits world model effectiveness. General video generation models 38; 18 learn rich visual priors from internet-scale data but fail to accurately model embodied physics---contact dynamics, rigid-body structural constraints, and action-consequence relationships that are critical for physically plausible state transitions. Domain-specific embodied models 1; 8; 48, conversely, are tailored to individual scenarios (e.g., tabletop manipulation or driving); they rely on structured, robot-specific action representations such as joint angles or waypoints, which cannot generalize across embodiment types or task categories, fundamentally limiting their utility as cross-platform simulation environments.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Bridging this gap requires grounding diverse embodied experiences in general visual priors, with natural language as the unified action interface that enables cross-scenario and cross-task integration. Different embodied domains provide complementary physical knowledge that collectively enriches the world model's state transition function: manipulation teaches fine-grained contact physics and object-state transformations within confined workspaces; autonomous driving teaches large-scale multi-agent dynamics and 3D scene geometry through ego-motion parallax and scene-scale transitions; indoor navigation teaches room-scale spatial reasoning, where language instructions must be grounded into spatially coherent visual trajectories over extended horizons. Because these domains share a common language interface, they can be trained jointly---with each domain's physical knowledge reinforcing the others rather than conflicting. Furthermore, translating human demonstrations into robot executions through video editing opens a practical pathway to scale embodied training data beyond the limits of physical robot collection.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present Qwen-RobotWorld, a language-conditioned video world model in the Qwen series that realizes this vision through tightly coupled innovations in architecture, data, and training. Beyond high-fidelity action-conditioned prediction, the model serves as a unified backbone that, with task-specific adaptation, can support three representative embodied world model applications: a synthetic data engine, a policy evaluation environment, and an action planner.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Architecture: Double-Stream MMDiT with MLLM Action Encoding (§3). To implement language-conditioned state transitions, we adopt a double-stream Multimodal Diffusion Transformer (MMDiT) backbone. An understanding stream processes rich semantic features extracted by a frozen Qwen2.5-VL encoder, representing the action $a_{t}$; a generation stream processes visual latents from a video-compatible VAE, representing the visual state $s_{t}$. The two streams interact via joint attention at every layer, enabling bidirectional cross-modal fusion throughout the denoising process.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Using an MLLM as the action encoder---rather than lightweight encoders such as T5 42 or CLIP 41---yields two key advantages: its deep language understanding accurately parses complex, compositional instructions into precise condition signals that govern fine-grained state transitions; its internalized world knowledge (e.g., that robot arms are rigid bodies with fixed link lengths and joint constraints) implicitly constrains the space of physically plausible transitions, and---combined with T2I co-training---prevents object deformation across video frames without requiring explicit geometric prompts, a common failure mode in models lacking such semantic grounding.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Data: Embodied World Knowledge Dataset (§2). To train a state transition function that generalizes across embodied domains, we construct the Embodied World Knowledge (EWK) dataset---approximately 8.6M video-text pairs comprising over 200M observation frames. The corpus spans four embodied domains alongside general video data (30% of the total): manipulation ($\sim$`<!-- -->`{=html}5.9M samples, 20+ robot morphologies, 1300+ skills) provides the core embodied foundation; autonomous driving ($\sim$`<!-- -->`{=html}200K samples from Waymo, NVIDIA PhysicalAI-AD, Bench2Drive, and Sekai) contributes large-scale ego-motion and multi-agent dynamics; indoor navigation (6K+ language-guided episodes from VLNVerse) provides room-scale spatial reasoning grounded in continuous trajectories; and human-to-robot transfer data---generated via an automated MANO 43-to-robot pipeline across 14 robot morphologies---enables cross-embodiment video editing.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

A central methodological contribution is our action-language mapping framework, which standardizes actions across 20+ robot embodiment types and 500+ action categories into a unified natural language interface, yielding approximately 8.6M high-quality cross-scenario, cross-task embodied video-text pairs. This is complemented by task-aware temporal segmentation (ensuring each sample captures a complete, well-defined state transition) and a hierarchical five-layer viewpoint-aware annotation pipeline that substantially improves caption specificity and downstream instruction-following.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Training: From General Priors to Embodied Specialization (§4). We adopt a two-stage progressive training curriculum. In pretraining, joint training across T2I, T2V, and TI2V tasks over general-domain data builds foundational visual priors, with T2I specifically anchoring geometrically correct object morphology that transfers to video generation. In the SFT stage, embodied data is introduced progressively (70% embodied, 30% general) through a four-phase mixing schedule: single-view manipulation $\rightarrow$ multi-view expansion $\rightarrow$ multi-view concatenated generation $\rightarrow$ complex tasks and cross-domain data. Within the embodied portion, manipulation dominates at $\sim$`<!-- -->`{=html}90% sampling weight to ensure depth of physical grounding, while multi-view concatenation and navigation/driving data each receive $\sim$`<!-- -->`{=html}5% to provide breadth.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

This general + expert joint training paradigm---unified under the natural language action interface---enables stable co-training across diverse scenarios and tasks, with each domain's physical knowledge mutually reinforcing the others. Asymmetric 3D RoPE positional encoding and multi-view concatenation training enable geometrically consistent synthesis across synchronized camera views without architectural modification.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Evaluated on four established benchmarks, Qwen-RobotWorld achieves competitive performance across cross-scenario and cross-task settings. It outperforms all open-source models on WorldModelBench (8.99, 3rd overall), attaining perfect physics adherence scores across Newton's laws, mass conservation, fluid dynamics, and gravity---on par with leading closed-source models---while achieving strong instruction following (2.33/3.0). It ranks 1st overall on EWMBench (4.60), with substantially leading motion fidelity in HSD (0.566, +33% over the runner-up) and top scene consistency (0.914). On DreamGen Bench, the model ranks 1st overall (4.952) across three robotic embodiment subsets, excelling in object-level compositional generalization. On PBench, it outperforms all open-source models (0.804), with domain understanding placing 3rd overall (0.857) and motion smoothness ranking 2nd among open-source models (0.990).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

Qualitative results further showcase generalization across cross-task video editing---including human-to-robot transfer, where the model synthesizes realistic robot execution from a human demonstration video without robot-specific prompting---as well as autonomous driving scene synthesis and room-scale indoor navigation generation; additional zero-shot performance on RoboTwin-IF benchmark further support robust transfer under complex instructions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our contributions are summarized as follows: Framework. We propose Qwen-RobotWorld, a language-conditioned video world model that treats natural language as a universal action interface to unify cross-scenario and cross-task embodied capabilities. By jointly training manipulation, driving, navigation, and human-to-robot transfer under a shared language interface, the model achieves complementary physical generalization that no single-domain model can match.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

Data. We propose an action-language mapping framework that standardizes 20+ robot embodiment types and 500+ action categories into a unified natural language interface, and construct approximately 8.6M high-quality, cross-scenario, cross-task embodied video-text pairs constituting the EWK dataset.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

Training. We propose a general + expert joint training paradigm that, under the unified natural language interface, equips the model with both broad world modeling capability and deep embodied domain expertise, enabling stable and scalable co-training across diverse scenarios and tasks.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

Performance. Qwen-RobotWorld achieves comprehensive improvements on cross-scenario and cross-task embodied evaluation metrics, ranking 1st overall on EWMBench and DreamGen Bench and outperforming all open-source models on WorldModelBench and PBench.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Data", "weight": 1.0} -->

The central challenge in training a universal embodied world model is not data scale alone, but representational heterogeneity: robotic manipulation actions are expressed as joint angles or end-effector waypoints, driving as steering commands and velocity profiles, and navigation as heading vectors---each requiring a separate model or interface per domain. We resolve this through an action-language mapping framework that converts heterogeneous actions from 20+ robot embodiment types and 500+ action categories into a unified natural language interface. Under this unified interface, videos from a Franka gripper, an autonomous vehicle, and an indoor navigation agent all become instances of the same language-conditioned video generation task, enabling cross-scenario and cross-task joint training under a single model without any domain-specific control interface. As shown in Figure 1, this framework produces approximately 6M high-quality, cross-scenario, cross-task embodied video--text pairs, which we further augment with general video data (30% of the total) to construct the Embodied World Knowledge (EWK) dataset: a corpus of 8.6M video--text pairs comprising over 200M observation frames.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Action-Language Mapping", "weight": 1.0} -->

The action-language mapping framework addresses a fundamental asymmetry in embodied data: the visual states (video frames) are already in a common pixel space, but the action representations are fragmented across incompatible modalities. Our framework resolves this by projecting all action signals onto a shared natural language space, so that the same diffusion transformer can learn $s_{t+1}=f(s_{t},a_{t})$ regardless of the underlying physical domain.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Why Language as the Unified Action Interface", "weight": 1.0} -->

Unlike low-level action representations---joint angles, end-effector waypoints, force-torque commands---which are hardware-specific and require a separate control interface per embodiment, natural language offers a universal, embodiment-agnostic action interface. A single instruction such as "grasp the red cup and lift it vertically" implicitly encodes the full action sequence, goal state, and physical constraints, without any knowledge of the underlying kinematic chain. By training the model to predict the next visual state $s_{t+1}$ from a language action $a_{t}$ alone, we obtain a simulation backbone that generalizes across embodiments---whether a Franka gripper, an Aloha dual-arm system, or a humanoid---without retraining or re-engineering robot-specific interfaces.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Why Language as the Unified Action Interface", "weight": 1.0} -->

This generality, however, places demanding requirements on annotation quality: each caption must function as a complete, self-contained action specification, precise enough that the model can predict $s_{t+1}$ from $a_{t}$ and $s_{t}$ alone, without access to any robot metadata or proprioceptive signals.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Hierarchical Five-Layer Annotation", "weight": 1.0} -->

To consistently produce such action-rich captions across 20+ robot embodiment types and 500+ action categories, we design a hierarchical annotation framework with five progressive layers. The first three form a structured chain-of-thought that decomposes each visual state transition into interpretable components: Task Goal Layer---infer the high-level intent of the transition (what should change between $s_{t}$ and $s_{t+1}$), integrating external instructions with observed video content; Action Detail Layer---decompose the action $a_{t}$ into spatio-temporal trajectories, micro-actions, speed, and force, with mandatory explicit declaration of viewpoint information (egocentric main view, wrist view, external view, or concatenated multi-view combinations); Physical Feedback Layer---describe the observable consequences of the action on the environment (object displacement, deformation, contact state changes), grounding each transition in verifiable physical outcomes.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Hierarchical Five-Layer Annotation", "weight": 1.0} -->

Based on this analysis, two granularities of action descriptions are generated: Comprehensive Description (50--100 words)---fully specifies the viewpoint--agent--action--feedback quadruple, providing a rich action signal for precise state transition prediction; Concise Description (15--30 words)---retains only the essential viewpoint--agent--key action elements, enabling the model to handle brief, high-level commands at inference time.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Hierarchical Five-Layer Annotation", "weight": 1.0} -->

We enforce four quality control principles: operation focus (only agent actions and object interactions), viewpoint definition (explicit viewpoint type and semantic role), objectivity (only visible dynamics), and physical verifiability (only visually verifiable outcomes). In training, we sample from comprehensive and concise descriptions with equal probability (50% each), so the model learns to execute both detailed trajectory specifications and brief task-level commands.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Coverage: 20+ Robot Embodiments, 500+ Action Categories", "weight": 1.0} -->

The framework is applied across all data domains. On the embodiment axis, it covers human hands, seven robot arm configurations (single-arm gripper, dual-arm gripper, single-arm dexterous hand, dual-arm dexterous hand, mobile dual-arm, half-humanoid, and full humanoid), ego vehicle (surround-view cameras), pedestrian/drone, and mobile navigation agent---representing 20+ distinct robot embodiments in total, as sourced from RoboCoin (15 robot models across three structural categories), Robomind (4 morphologies), InternData-A1 (4 robot models), Groot-XE, and various other datasets.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Coverage: 20+ Robot Embodiments, 500+ Action Categories", "weight": 1.0} -->

On the action axis, it spans 500+ action categories derived from the explicit motion primitive vocabularies across our training datasets---Agibot-World alone defines 84 distinct manipulation primitives (grasp, push, pour, fold, wipe, cut, etc.)---supplemented by unique primitives from other manipulation datasets and locomotion/navigation actions (turning, lane-changing, waypoint following, obstacle avoidance, etc.), organized into four tiers: manipulation primitives, long-horizon compositions, locomotion and navigation, and dynamic and deformable interactions. This systematic coverage ensures that the resulting embodied video-text pairs span a semantically rich and physically diverse action space that no single domain could provide.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Data Collection", "weight": 1.0} -->

EgoHOD 40, EPIC-Kitchens 11, Egocentric-10k 7 Daily grasping & kitchen Dexterity & coordination prior Single/dual-arm, humanoids Rigid & deformable objects Single-arm (gripper + dexterous hand) Synced ego + wrist + external Temporal & multi-view consistency Head + dual wrist Multi-view grasping prior Tool use & in-hand InternData-A1 49, Robotwin 9, Groot-XE 5, RT1 6 Mixed arms (simulated) Waymo E2E 54, NVIDIA PhysicalAI-AD 36 Urban driving & traffic Large-scale motion & 3D geometry Ego vehicle (sim) Sim diversity & GT annotations 134 indoor scenes, lang-guided 3D reasoning & lang-trajectory align Human → 14 robot arms Video editing supervision Table 1: Detailed inventory of the Embodied World Knowledge (EWK) training data mixture, organized by domain.

<!-- chunk {"id": "body-0032", "role": "body", "section": "General Data", "weight": 1.0} -->

General world data lays the foundation for the model to grasp basic physical laws and form accurate visual representations. This category encompasses diverse videos and still images from the internet. Video data are standardized to 24 FPS and support multiple resolutions and aspect ratios (1:1, 2:3, 3:2, 3:4, 4:3, 9:16, 16:9, etc.). Image data integrates high-quality static photographs, serving as visual quality anchors that establish precise representations of object appearance, material texture, and spatial composition. All general data is annotated with natural language descriptions generated by Qwen2.5-VL 3; annotations omit viewpoint-specific information to maintain flexibility and generality. Notably, we adopt a conservative stance on AI-generated content (AIGC): general data excludes AI-produced images and videos, as these often introduce visual artifacts, physical inconsistencies, and implicit biases that could undermine the model's generalization capabilities.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Embodied Manipulation Data", "weight": 1.0} -->

To enable the world model to acquire grounded physical understanding across scenarios and tasks, we build a structured data mixture spanning manipulation, driving, navigation, and cross-embodiment transfer domains, as summarized in Table 1. For the core manipulation domain, we organize the data around four dimensions: Multi-Embodiment, Multi-Task, Multi-Scenario, and Multi-View.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Multi-Embodiment", "weight": 1.0} -->

Manipulation data spans a spectrum of embodiments---human hands, single-arm grippers, dual-arm dexterous systems, mobile manipulators, and full-body humanoids---so the model learns to separate task-level intent from embodiment-specific kinematics. Human manipulation data (EgoHOD 40, EPIC-Kitchens 11) provides a dexterity ceiling: the model observes what physically capable interaction looks like, acquiring priors for fluid hand--eye coordination and tool use. Robot data then teaches the model how those same intents map onto diverse mechanical morphologies. By exposing the model to both human demonstrations and robot executions of overlapping tasks (e.g., Robomind 55, RoboCoin 56), it learns embodiment-invariant action semantics---the ability to predict "what should happen next" regardless of whether the actor is a two-finger gripper or a seven-finger dexterous hand.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Multi-Task", "weight": 1.0} -->

The manipulation corpus covers a skill hierarchy from atomic contact-level actions to extended multi-step procedures, teaching the model to operate at multiple temporal granularities. Short-horizon datasets (Bridge V2 51, RH20T 13) provide dense coverage of fundamental interaction primitives---grasping, pushing, inserting---that ground the model's understanding of contact physics and object affordances. Long-horizon datasets (Agibot-World 2, Galaxea 16) chain these primitives into coherent sequences, forcing the model to maintain state tracking and causal reasoning across dozens of steps. Additionally, dynamic-interaction datasets (Humanoid Everyday 59) introduce high-velocity, whole-body motions that test the model's ability to predict outcomes under significant momentum and balance constraints. Together, this range ensures the model can reason about both "what happens when you press here" and "what happens after ten sequential decisions."

<!-- chunk {"id": "body-0036", "role": "body", "section": "Multi-Scenario", "weight": 1.0} -->

Multi-scenario coverage advances along two complementary axes: breadth across real environments, and extension to simulator-rendered scenarios. Along the first axis, physical interaction manifests differently depending on context---a kitchen counter presents different lighting, clutter density, and surface properties than a factory floor or an outdoor worksite. Our manipulation data is therefore predominantly real-world, spanning domestic kitchens, workshops, laboratories, and unstructured outdoor settings, exposing the model to genuine variation in illumination, occlusion, material appearance, and background complexity---so it does not brittly overfit to any single environment. Along the second axis, we incorporate photorealistic simulation data (InternData-A1 49) as a first-class complement. This is motivated by the VLA landscape: a substantial portion of policy models are trained in simulators, and virtually all are evaluated there using standardized benchmarks such as LIBERO 33, SimplerEnv 29, and RLBench 23. A world model intended as a general simulation backbone must therefore generate faithfully under simulator-style appearances and physics, bridging the visual domain gap between real and synthetic observations so it can serve both sim-to-real transfer and closed-loop evaluation pipelines.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Multi-Scenario", "weight": 1.0} -->

The simulation portion additionally supplies precisely controlled variations in lighting, object pose, and camera placement that further strengthen visual robustness.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Multi-View", "weight": 1.0} -->

Single-view data teaches the model to predict plausible futures from a fixed perspective, but many physically critical events are partially or fully occluded from any single camera. Synchronized multi-view recordings (Agibot-World 2, Robomind 55) expose the model to the same event from head-mounted, wrist-mounted, and external viewpoints simultaneously. This serves two purposes: during training, cross-view correspondence acts as a geometric regularizer, implicitly teaching the model about object shape, depth, and spatial relationships; at inference, the model can generate from any individual viewpoint or compose multi-view outputs that remain mutually consistent. Approximately 1.6M of our 6M embodied samples include synchronized 2--4 view concatenations, providing substantial multi-view supervision without dominating the corpus.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Autonomous Driving Data", "weight": 1.0} -->

While manipulation data captures fine-grained object interactions within a confined workspace, autonomous driving data exposes the model to a substantially larger motion space with diverse maneuvers (turning, lane changing, acceleration) spanning a much wider range of velocities and trajectories. Driving scenes also contain rich multi-agent dynamics---surrounding vehicles, pedestrians, and cyclists interacting under traffic rules---requiring the world model to learn how multiple objects move, occlude, and influence each other over time. Furthermore, the large camera displacement provides dense supervisory signal for 3D scene geometry through parallax and perspective changes, strengthening the model's capacity for view synthesis and spatial reasoning.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Autonomous Driving Data", "weight": 1.0} -->

We curate multi-view driving videos from four large-scale datasets: Waymo E2E 54 (real-world driving, 8 surround-view cameras, 7,044 clips / 11.3h), NVIDIA PhysicalAI-AD 36 (real-world driving, 5 cameras with 30^∘^--120^∘^ FoV, 1,342,418 clips / 1,715.9h), Bench2Drive 24 (CARLA-simulated driving under 9,881 diverse traffic scenarios, 6 cameras, 384,948 clips / 511.2h), and Sekai 44 (egocentric pedestrian walking and drone videos, 9,995 clips / 166.6h with scene and weather annotations). In total, the driving data comprises 1,744,405 clips spanning 2,405 hours. We apply a unified three-stage processing pipeline: frame extraction with trajectory unification into a common waypoint format, action-based clip segmentation (2--8 s) according to ego maneuver transitions, and caption generation combining structured trajectory descriptions with optional VLM augmentation.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Egocentric Indoor Navigation Data", "weight": 1.0} -->

Egocentric indoor navigation data provides a complementary perspective to both manipulation and driving data. Unlike manipulation which focuses on fine-grained object interactions within a confined workspace, and driving which operates in large-scale outdoor environments, indoor navigation requires the model to understand room-scale spatial layouts, obstacle-aware path planning, and the mapping from textual navigation commands to spatially coherent visual trajectories.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Egocentric Indoor Navigation Data", "weight": 1.0} -->

Following VLNVerse 31, we collect physically grounded egocentric navigation data using NVIDIA Isaac Sim 35 with photorealistic rendering and continuous control. We gather 6,064 successful navigation episodes across 134 indoor scenes, each consisting of an egocentric RGB video ($256\times 256$ resolution at 10 FPS) paired with natural language navigation instructions. The trajectories average approximately 8.2 m in length (ranging from 4 to 17.5 m), accumulating a total traversal distance of roughly 49.8 km and approximately 5.8 hours of continuous first-person navigation video. The instructions are provided in two formats: single-string step-by-step directives (3,031 episodes, averaging 67.2 words) and multi-granularity descriptions at formal, natural, and casual registers (3,033 episodes).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Egocentric Indoor Navigation Data", "weight": 1.0} -->

Video generation models trained on such traversal data can acquire emergent 3D consistency and spatial coherence across frames 17; 4, while the physically grounded, action-conditioned nature of each sequence encourages the model to internalize depth reasoning, geometric consistency, and obstacle-aware planning 45; 20; 60. By grounding language instructions in continuous egocentric traversals, this data enables the world model to jointly learn language understanding, 3D spatial reasoning, and embodied action prediction within indoor environments.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Human-to-Robot Transfer Data", "weight": 1.0} -->

To train the model on cross-embodiment visual correspondence without physical robot collection, we curate two complementary sources of human-to-robot transfer data. The first is a large-scale human-robot paired dataset constructed from egocentric bimanual manipulation recordings via an automated pipeline: 3D hand keypoints are extracted through MANO 43 reconstruction and retargeted to robot end-effector trajectories, human hands are removed via video inpainting, and 14 robot arm models are rendered into the inpainted scene using MuJoCo 50 inverse kinematics, yielding four aligned video streams per episode (original human video, hand-removed scene, pure simulation, and robot-overlaid scene). The diversity of 14 embodiments within shared scenes ensures the editing capability generalizes across robot morphologies.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Human-to-Robot Transfer Data", "weight": 1.0} -->

The second source addresses a fundamental limitation of direct rendering: simplified renderers ignore scene illumination, cast shadows, and material-dependent specular reflections, creating a photometric gap between rendered and real observations. To bridge this, we build upon the open-sourced InternA1 dataset 49, which uses NVIDIA Isaac Sim 35 to provide photorealistic RGB observations with environment lighting and accurate shadows. Using the same dynamics parameters and robot URDFs, we render matched egocentric views in MuJoCo 50---without lighting or shadow effects---producing paired samples that share identical geometry and viewpoint while differing in photometric realism. This paired data enables the model to learn the visual mapping between simplified rendering and photorealistic observations, covering Franka Emika Panda, AgileX Split Aloha, ARX Lift2, and AgiBot Genie1 across single-arm, dual-arm, mobile dual-arm, and humanoid configurations, with approximately 80K episodes spanning pick-and-place, articulated object manipulation, and multi-object rearrangement tasks.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Data Processing", "weight": 1.0} -->

We design a unified data processing pipeline that transforms heterogeneous raw data from diverse embodied and general video sources into high-quality, consistently formatted training samples. As illustrated in Figure 2, the pipeline consists of four stages: Raw Data Collection, Video Preprocessing, Hierarchical Annotation, and Caption Quality Filtering with Iterative Prompt Refinement. Stages 2 and 3 apply domain-adaptive operations depending on source data characteristics, while Stage 4 forms a closed feedback loop that routes underperforming captions back for targeted re-annotation.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Stage 1: Raw Data Collection", "weight": 1.0} -->

The pipeline begins by ingesting raw video data from five source categories spanning both general and embodied domains. General Video provides internet-scale visual diversity from documentaries, professional stock libraries, and curated web clips. Manipulation data covers a broad spectrum of robot embodiments---single-arm grippers, dual-arm systems, dexterous hands, mobile platforms, and humanoids---from datasets including EgoHOD, Bridge V2, DROID, RoboMind, Agibot-World, and others. Autonomous Driving contributes large-scale ego-motion and multi-agent dynamics from Waymo, Bench2Drive, NVIDIA PhysicalAI-AD, and Sekai. Indoor Navigation supplies language-guided spatial reasoning episodes from VLNVerse across 134 indoor scenes. Human-to-Robot Transfer provides paired human demonstration and robot execution data constructed via our automated MANO-to-robot pipeline across 14 robot types.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Stage 2: Video Preprocessing", "weight": 1.0} -->

Raw videos undergo domain-adaptive preprocessing to produce uniformly structured clips suitable for training. We apply five complementary operations depending on the source data characteristics: Frame Extraction. For short-horizon task videos (typically single-step manipulations lasting 2--8 s), we extract frames at a target rate that captures the essential phases of the interaction---approach, contact, manipulation, and result---ensuring each sample contains the complete causal chain of the atomic action.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Stage 2: Video Preprocessing", "weight": 1.0} -->

Frame Interpolation. When source videos have insufficient frame rates for smooth motion learning, we apply temporal interpolation to increase frame density, preserving continuous motion trajectories critical for modeling fine-grained contact dynamics and object-state transitions.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Stage 2: Video Preprocessing", "weight": 1.0} -->

Sub-task Splitting. For long-horizon episodes involving multi-step procedures (e.g., sequential pick-and-place, complex assembly), we decompose the video into semantically coherent sub-task segments. Each segment captures a complete atomic action with clear start and end states, preventing the partial-execution artifacts that arise from naive uniform truncation.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Stage 2: Video Preprocessing", "weight": 1.0} -->

Main-View Selection. For multi-camera recordings where only a primary viewpoint is needed (e.g., single-view manipulation training), we select the most informative camera stream---typically the egocentric or external view that best captures the interaction region---discarding redundant angles.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Stage 2: Video Preprocessing", "weight": 1.0} -->

Multi-View Concatenation. Conversely, for multi-view co-training, we concatenate synchronized clips from 2--4 camera viewpoints into a single horizontal layout, preserving temporal alignment across views. This enables the model to learn cross-view geometric consistency and synchronized state transitions without architectural modifications.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Stage 3: Hierarchical Annotation", "weight": 1.0} -->

Preprocessed videos pass through our five-layer hierarchical annotation framework (Section 2.1), which generates viewpoint-aware captions at two granularities---comprehensive (50--100 words) and concise (15--30 words)---sampled with equal probability during training. The prompt template used by the annotation model is shown above.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Stage 4: Caption Quality Filtering", "weight": 1.0} -->

To ensure annotation quality across the diverse range of scenarios, tasks, and embodiments in our corpus, we implement a closed-loop quality filtering system combining automated assessment with human oversight. Captions that fail quality checks are routed back to Stage 3 for targeted re-annotation, forming an iterative refinement loop.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Stage 4: Caption Quality Filtering", "weight": 1.0} -->

Judge Pipeline. An automated LLM-based judge assesses each caption along several dimensions, including factual accuracy, specificity, instruction clarity, and viewpoint consistency. Specifically, it evaluates whether the caption correctly describes the video content, provides sufficient detail beyond generic descriptions, can function as an actionable command, and maintains spatial references consistent with the camera perspective. Captions that do not satisfy any of these criteria are flagged for further review.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Stage 4: Caption Quality Filtering", "weight": 1.0} -->

Human Evaluation. A subset of captions---particularly those near judgment thresholds or from underrepresented domains---undergoes manual review by human annotators who validate correctness, identify systematic failure patterns, and provide ground-truth corrections that inform subsequent prompt refinements.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Stage 4: Caption Quality Filtering", "weight": 1.0} -->

Iterative Prompt Refinement. When the judge pipeline identifies consistent underperformance in specific categories, we trigger targeted prompt redesign along three axes: scenario-specific retries (e.g., outdoor lighting conditions, kitchen environments), task-specific retries (e.g., articulated object manipulation, fluid pouring), and embodiment-specific retries (e.g., humanoid bimanual coordination, dexterous hand manipulation). Each retry employs a specialized prompt template tailored to the failure mode, and the refined captions are re-evaluated through the judge pipeline until they meet quality standards. This iterative loop ensures that no scenario, task, or embodiment category suffers from systematically poor annotations due to one-size-fits-all prompting.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Stage 4: Caption Quality Filtering", "weight": 1.0} -->

Final Corpus Statistics. After the complete four-stage pipeline, the final training corpus comprises approximately 8.6M video-text pairs (over 200M observation frames), with embodied data accounting for 70% and general data for 30%. Within the embodied portion, single-view manipulation data constitutes the majority at $\sim$`<!-- -->`{=html}4.3M samples, followed by $\sim$`<!-- -->`{=html}1.6M multi-view concatenated samples with synchronized 2--4 camera views, and $\sim$`<!-- -->`{=html}200K navigation and driving samples.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

As shown in Figure 3, the model consists of three components: an MLLM as the action encoder, a VAE as the state encoder/decoder, and an MMDiT 12 as the transition function, organized in a double-stream design.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

MLLM --- Action Encoder. We employ a frozen Qwen2.5-VL 3 to encode user inputs into condition signals. For a given input text $S$, it extracts last-layer hidden states $\mathbf{h}=\phi(S)$, serving as the action condition.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

VAE --- State Encoder/Decoder. The VAE encodes video frames into latent representations $\mathbf{z}=\mathcal{E}(\mathbf{x})$ and decodes predicted latents back into visual observations. We adopt the Wan-VAE 52 architecture, which handles both image and video modalities.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

MMDiT --- Transition Function. The MMDiT adopts a double-stream architecture: the understanding stream receives the MLLM encoding $\mathbf{h}$ (projected via a trainable connector), and the generation stream receives noisy state latents from the VAE. At each block, the two streams interact via joint attention. The backbone comprises 60 double-stream blocks with 24 attention heads (head dimension 128), hidden size 3,072, and patch size 2×2. Total parameters: MLLM 7B, VAE 127M (encoder 54M + decoder 73M), MMDiT 20B. The context length supports up to 48,360 video tokens.

<!-- chunk {"id": "body-0063", "role": "body", "section": "3D Rotary Position Encoding", "weight": 1.0} -->

We employ 3D RoPE 47; 21 to independently encode the temporal, spatial height, and spatial width dimensions. Rather than allocating dimensions uniformly, we use an asymmetric split: 16 dimensions for the temporal axis and 56 dimensions each for height and width, totaling 128 dimensions (pe_axes_dim = ). The temporal axis receives fewer dimensions as adjacent frames are strongly correlated; the spatial axes receive more to capture the greater diversity of object positions and scene layouts. We also apply Scalable RoPE 52 to support generalization to varying resolutions and durations at inference.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Scene2Robot", "weight": 1.0} -->

Building upon the double-stream MMDiT architecture (§3.1) and the asymmetric 3D RoPE encoding (§3.2), we design Scene2Robot, a multi-segment conditioning mechanism that repurposes the same backbone for cross-embodiment video synthesis, as illustrated in Figure 4.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Scene2Robot", "weight": 1.0} -->

First-Frame Conditioning (TI2V Baseline). For standard text-image-to-video tasks, the first frame serves as a fixed visual condition: its VAE latents are assigned timestep $t{=}0$ in the generation stream and excluded from the denoising loss, while the frozen Qwen2.5-VL encodes the text instruction into the understanding stream. Because the double-stream joint attention (§3.1) fuses both signals at every layer, the generation tokens can simultaneously attend to the visual anchor and the semantic action specification, producing temporally coherent continuations grounded in the language command.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Scene2Robot", "weight": 1.0} -->

Multi-Segment Extension for Human-to-Robot Transfer. Human-to-robot transfer poses a video editing problem: the model must reference both the scene context (background, object layout, lighting) and the target robot's motion trajectory from a simulated demonstration. We address this by extending first-frame conditioning to a three-segment input sequence, all processed within the same VAE--MMDiT pipeline without any architectural modification: Scene condition ($F$ frames): the original human demonstration video, with human hands masked out, encoded by the VAE to provide appearance, spatial layout, and object state information.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Scene2Robot", "weight": 1.0} -->

Robot reference ($F$ frames): a simulated robot execution rendered via MuJoCo, encoded by the VAE, supplying the target embodiment's kinematic trajectory and morphology.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Scene2Robot", "weight": 1.0} -->

Generation ($F$ frames): noisy latents to be denoised into the final photorealistic robot execution video.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Scene2Robot", "weight": 1.0} -->

Segments and share the same $t{=}0$ assignment as first-frame conditioning and are excluded from loss computation; only segment receives gradient updates during training. The 3D RoPE encoding (§3.2) assigns each segment its own temporal index range, allowing the model to distinguish temporal positions across segments. Joint attention in every MMDiT block then enables the generation tokens to simultaneously attend to scene appearance from segment, robot motion from segment, and the MLLM action semantics from the understanding stream. This tripartite conditioning enables the model to synthesize photorealistic robot executions that faithfully preserve both the scene context and the instructed manipulation behavior.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

We propose a joint training paradigm in which general scene generation and robot manipulation prediction are unified under a single natural language interface as the same conditional video generation task, with the model continuously receiving gradient updates from both data regimes throughout training. This shared formulation allows general world priors and embodied action priors to reinforce each other through a common backbone, enabling stable cross-scenario and cross-task co-training. The curriculum proceeds in two progressive stages: pretraining establishes broad world foundations, and SFT deepens embodied specialization while preserving the general-expert balance.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Pretraining Stage: Establishing General World Foundation", "weight": 1.0} -->

General World Priors. We curate over 200M real-world observation samples from 14 high-quality video platforms, covering natural scenes, daily life, and sports. This breadth allows the model to internalize domain-agnostic world priors---object motion, lighting variation, collision dynamics---that form the general backbone for later embodied generalization. We further incorporate multi-camera synchronized observations with 3D RoPE spatial encoding, establishing preliminary cross-view geometric consistency as a spatial foundation for multi-view embodied generation.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Pretraining Stage: Establishing General World Foundation", "weight": 1.0} -->

Human Interaction Priors. We introduce large-scale first-person hand manipulation data (Ego4D 19, EPIC-Kitchen 11, etc.). Human demonstration serves as a natural bridge between general and embodied: by learning grasping, tool use, and object manipulation from everyday human behavior, the model builds action priors and affordance understanding that transfer directly to robot operation in later stages.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Pretraining Stage: Establishing General World Foundation", "weight": 1.0} -->

Multi-Task Joint Training. T2I, T2V, and TI2V tasks are trained jointly on a shared backbone, serving as the core mechanism through which general and embodied capabilities coexist in one model. The T2I task learns sharp visual representations from general image data, acting as a visual quality anchor whose object morphology knowledge automatically transfers to video generation tasks through the shared backbone, preventing deformation and identity inconsistency. Task ratios gradually shift from pure T2I toward full three-task joint training, so the model operates stably across multiple generation modes by the end of pretraining.

<!-- chunk {"id": "body-0074", "role": "body", "section": "SFT Stage: Embodied Specialization", "weight": 1.0} -->

The SFT stage progressively deepens embodied expertise while keeping general world data in every training batch, ensuring that embodied specialization and general world modeling capability advance together rather than trade off.

<!-- chunk {"id": "body-0075", "role": "body", "section": "SFT Stage: Embodied Specialization", "weight": 1.0} -->

Progressive Embodied Knowledge Injection. We adopt a four-phase data mixing schedule. In early training, multi-embodiment robot data and human hand manipulation data co-dominate: human action priors guide the learning of cross-embodiment operation commonalities, while robot data strengthens concrete execution representations. We then gradually increase wrist-view and third-person view data to broaden viewpoint coverage. Building on this, we introduce multi-view concatenated training: synchronized first frames from multiple cameras are spatially concatenated as a single input, requiring the model to jointly generate subsequent frames for all views simultaneously, forcing the attention layers to establish cross-view spatial correspondences and achieve geometrically consistent multi-view generation. In the final phase, scarce high-complexity tasks (pouring, folding, bimanual coordination, multi-material interaction) and long-horizon reasoning data are targeted for supplementation to push the frontier of embodied capability. Throughout this process, general world data continuously participates in every training batch, jointly acting on the same backbone alongside embodied data to ensure that embodied specialization and general world modeling capability advance together.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Training Objective and Infrastructure", "weight": 1.0} -->

We adopt the flow matching objective 32; 34, where input videos are encoded into latent space via the VAE encoder and noise is sampled from a standard normal distribution. Qwen2.5-VL encodes text inputs as guidance signal. Timesteps are sampled from a log-normal distribution with adaptive shifting based on video sequence length 12. For TI2V tasks, the first-frame timestep is fixed at 0 to ensure that the generation process is conditioned on the given observation frame. Training is conducted with Megatron-LM 46 using a hybrid parallelism strategy, with selective activation recomputation 26 applied to a subset of dual-stream blocks to balance memory usage and training throughput.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Experiments", "weight": 1.0} -->

We conduct comprehensive evaluations on four benchmarks spanning embodied manipulation, physical reasoning, and general video quality. Across these benchmarks, our model delivers consistently strong results, achieving state-of-the-art performance on EWMBench for embodied world modeling (Overall 4.60, +0.55 over LVP), ranking 1st overall on DreamGen Bench (Total 4.952), and 1st among open-source models on WorldModelBench (Total 8.99).

<!-- chunk {"id": "body-0078", "role": "body", "section": "Experiments", "weight": 1.0} -->

Quantitative Evaluation (§5.1). We evaluate against two categories of baselines: general video generation models---Sora2 38, Veo3 18, Wan2.6 53, Kling 27, and LTX-2 30; and embodied world models---Cosmos 1, WoW 10, LVP 8, Vidar 14, and GigaWorld 48.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Experiments", "weight": 1.0} -->

Qualitative Analysis (§5.2). We evaluate manipulation capabilities along three progressive dimensions: fine-grained language grounding, generalization across embodiments, tasks, and viewpoints, and zero-shot robustness against strong baselines.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Experiments", "weight": 1.0} -->

Cross-Domain Generalization (§5.3) further covers human-to-robot transfer, autonomous driving, and indoor navigation as supplementary tasks.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Quantitative Evaluation", "weight": 1.0} -->

Unless noted otherwise, quantitative tables use boldface for the best value in each column and underline for the second best.

<!-- chunk {"id": "body-0082", "role": "body", "section": "EWMBench: Embodied Motion Fidelity", "weight": 1.0} -->

Benchmark. EWMBench 58 evaluates embodied world models on three dimensions: scene consistency (SceneC), motion correctness (HSD, Dyn, nDTW), and semantic alignment (Diversity, BLEU, CLIP, Logics). The benchmark contains 21 samples across 7 tasks with clear action-ordering constraints.

<!-- chunk {"id": "body-0083", "role": "body", "section": "EWMBench: Embodied Motion Fidelity", "weight": 1.0} -->

Results. Table 2 shows our model ranks 1st overall with a score of 4.60, outperforming the runner-up LVP (4.05) by $+0.55$. We lead in motion fidelity---HSD (0.566) surpasses LVP (0.425) by 33%---and achieve top performance in scene consistency (SceneC: 0.914) and logic constraint satisfaction (Logics: 1.00).

<!-- chunk {"id": "body-0084", "role": "body", "section": "DreamGen Bench", "weight": 1.0} -->

Benchmark. DreamGen Bench 61 evaluates the quality of robot videos generated by video world models, measuring instruction following (IF) and physics alignment (PA) across three subsets of the GR1 robot embodiment: environment generalization (GR1-Env), object generalization (GR1-Object), and behavior generalization (GR1-Behavior). IF is assessed using Qwen2.5-VL 3 as the evaluator.

<!-- chunk {"id": "body-0085", "role": "body", "section": "DreamGen Bench", "weight": 1.0} -->

Results. Table 3 shows our model achieves the highest total score of 4.952, ranking 1st overall. We lead in GR1-Object IF (0.878, 1st), demonstrating strong object-level compositional generalization, and physics alignment is consistent across all subsets (PA: 0.828/0.840/0.781). GR1-Behavior IF (0.832) slightly trails LVP (0.889) and GigaWorld (0.884), indicating long-horizon behavior generalization as a direction for further improvement.

<!-- chunk {"id": "body-0086", "role": "body", "section": "PBench: Physical Behavior Evaluation", "weight": 1.0} -->

Benchmark. PBench 37 evaluates models on two complementary aspects: Domain Score, which measures physical behavior understanding via QA pairs assessed by Qwen2.5-VL across six domains (AV, Robot, Industry, Physics, Human, Common Sense); and Quality Score, which measures visual quality via eight VBench 22 metrics including image-to-video consistency, aesthetic quality, motion smoothness, and subject consistency. The Overall Score is the average of the two.

<!-- chunk {"id": "body-0087", "role": "body", "section": "PBench: Physical Behavior Evaluation", "weight": 1.0} -->

Quality Metrics (VBench) Table 4: Performance comparison on PBench.

<!-- chunk {"id": "body-0088", "role": "body", "section": "PBench: Physical Behavior Evaluation", "weight": 1.0} -->

Results. As shown in Table 4, our model outperforms all among open-source models with an overall score of 0.804. Domain understanding is our strongest dimension (0.857, 3rd overall), surpassing most closed-source models. Motion smoothness also stands out (0.990, 2nd among open-source models), reflecting consistent temporal coherence in generation. Aesthetic quality (0.455) and imaging quality (0.649) are relatively lower, primarily because our model is purpose-built for embodied tasks and operates at a lower output resolution than general-purpose video generators, which reduces VBench's pixel-level quality scores; nonetheless, this resolution is fully sufficient for downstream robot control tasks.

<!-- chunk {"id": "body-0089", "role": "body", "section": "WorldModelBench: Physical Reasoning and Instruction Following", "weight": 1.0} -->

Benchmark. WorldModelBench 28 evaluates models on three dimensions: instruction following (0--3 scale), common sense (frame and temporal quality), and physics adherence (5 violation types: Newton's laws, mass conservation, fluid dynamics, penetration, gravity). The benchmark contains 350 instances across 7 domains with 56 subdomains.

<!-- chunk {"id": "body-0090", "role": "body", "section": "WorldModelBench: Physical Reasoning and Instruction Following", "weight": 1.0} -->

Results. Table 5 shows our model outperforms all open-source models (8.99, 3rd overall), trailing only closed-source Wan2.6 and Veo3. We achieve perfect physics adherence (1.00) across all four categories and strong instruction following (2.33/3.0), with the common-sense gap attributable to our lower output resolution.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Fine-Grained Language Grounding", "weight": 1.0} -->

Precise grounding of language in visual actions is foundational to Qwen-RobotWorld's design as a language-conditioned world model. Figure 5 evaluates this capability at two levels. (a) Contrastive pairs: given identical initial frames, the model produces qualitatively distinct videos when a single keyword differs---target object identity, action type, or spatial placement---demonstrating fine-grained semantic discrimination beyond generic manipulation priors. (b) Complex instructions: the model handles long-horizon sequential tasks with multi-step dependencies and abstract goal instructions that require inferring the manipulation sequence from context, decomposing each into a temporally coherent execution without explicit sub-task prompts.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Zero-Shot Robustness on RoboTwin-IF", "weight": 1.0} -->

Building on the single-model capabilities demonstrated above, we next examine whether these gains persist under controlled model-to-model comparisons. Aggregate embodied-world-model scores can entangle three different failure sources: instruction mismatch, cross-view inconsistency, and generic visual degradation. To isolate these factors, we perform a zero-shot side-by-side comparison on four Unitree G1 tasks against two strong embodied baselines, LVP and Cosmos2.5-14B. Figure 7 shows that Qwen-RobotWorld more consistently preserves language-grounded execution (correct object/action correspondence and cleaner goal completion) while maintaining coherent multi-view trajectories. The two baselines show different failure patterns. LVP more often produces incomplete task execution, while Cosmos2.5-14B tends to exhibit weaker alignment between the instruction and the generated manipulation outcomes in more complex cases.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Zero-Shot Robustness on RoboTwin-IF", "weight": 1.0} -->

To validate this behavior under a benchmark setting, we evaluate zero-shot performance on RoboTwin-IF (Instruction Following), a newly proposed benchmark built on the RoboTwin simulator with many newly constructed complex tasks. Notably, although Qwen-RobotWorld mixes only a small amount of open-source RoboTwin data during training, it still shows strong zero-shot performance on RoboTwin-IF together with stable multi-view consistency across synchronized camera streams. These results suggest that the model's gains are not limited to a few qualitative examples, but generalize to more challenging unseen embodied tasks. Overall, Qwen-RobotWorld demonstrates stronger zero-shot robustness than prior baselines by better aligning instruction following, action realism, and cross-view coherence in a unified generation framework.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Cross-Domain Generalization", "weight": 1.0} -->

Beyond manipulation-centric evaluation, we assess the model's generalization to supplementary task families beyond the core manipulation domain. Figure 9 shows human-to-robot transfer across eight target embodiments, where the model preserves task intent from human demonstrations while adapting motion to embodiment-specific kinematic constraints. Figure 10 covers mobility scenarios, including autonomous driving episodes from Bench2Drive, NVIDIA PhysicalAI-AD, Sekai, and Waymo, and egocentric indoor navigation episodes from VLNVerse. Together, these results indicate that the learned language-conditioned transition model generalizes beyond a single embodiment or scenario family.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this report, we present Qwen-RobotWorld, a language-conditioned world model framework for embodied intelligence that unifies robotic manipulation, autonomous driving, indoor navigation, and human-to-robot transfer under a shared natural language action interface. To realize this objective, we develop a three-part system: a double-stream MMDiT architecture with MLLM action encoding for semantically precise and physically grounded generation, the Embodied World Knowledge (EWK) dataset with large-scale cross-embodiment action-language alignment, and a general+expert progressive curriculum that couples broad visual priors with embodied specialization. This design enables one common backbone that can be adapted toward three representative embodied world model applications---synthetic data generation, policy evaluation, and action planning. Across both benchmark evaluations and zero-shot analyses, Qwen-RobotWorld demonstrates strong, consistent performance and robust multi-view instruction-following generalization. We hope this work provides a practical foundation for building embodied world models that are not only perceptually strong, but also functionally useful for downstream robotic learning and control.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Authors", "weight": 1.0} -->

Jie Zhang^\*\*^ \* Equal contribution., Xiaoyue Chen^11^footnotemark: 1, Anzhe Chen, Dayiheng Liu, Deqing Li, Gengze Zhou, Hale Yin, Haoqi Yuan, Haoyang Li, Jiahao Li, Jiazhao Zhang, Jingren Zhou, Kaiyuan Gao, Kun Yan, Lihan Jiang, Ningyuan Tang, Pei Lin, Qihang Peng, Shengming Yin, Tianhe Wu, Tianyi Yan, Xiao Xu, Yan Shu, Yanran Zhang, Ye Wang, Yi Wang, Yilei Chen, Yixian Xu, Yiyang Huang, Yuxiang Chen, Zekai Zhang, Zhendong Wang, Zixing Lei, Zhixuan Liang, Zihao Liu, Zikai Zhou, Chenxu Lv^22^footnotemark: 2, Xiong-Hui Chen^††^ † Corresponding author., Chenfei Wu^22^footnotemark: 2
