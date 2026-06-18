<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes

Topics include Robotics, Datasets, SceneSmith.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Simulation has become a key tool for training and evaluating home robots at scale, yet existing environments fail to capture the diversity and physical complexity of real indoor spaces. Current scene synthesis methods produce sparsely furnished rooms that lack the dense clutter, articulated furniture, and physical properties essential for robotic manipulation. We introduce SceneSmith, a hierarchical agentic framework that generates simulation-ready indoor environments from natural language prompts. SceneSmith constructs scenes through successive stagesunicodex2013from architectural layout to furniture placement to small object populationunicodex2013each implemented as an interaction among VLM agents: designer, critic, and orchestrator. The framework tightly integrates asset generation through text-to-3D synthesis for static objects, dataset retrieval for articulated objects, and physical property estimation. SceneSmith generates 3-6x more objects than prior methods, with <2% inter-object collisions and 96% of objects remaining stable under physics simulation. In a user study with 205 participants, it achieves 92% average realism and 91% average prompt faithfulness win rates against baselines. We further demonstrate that these environments can be used in an end-to-end pipeline for automatic robot policy evaluation.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent progress in general-purpose robotics has been driven by large-scale foundation models that promise broad generalization across tasks, embodiments, and environments. Companies such as 1X and Sunday are now explicitly targeting the deployment of robots into arbitrary human homes. Achieving this vision requires robots that can robustly perceive, reason, and act across the long tail of real-world indoor environments---spaces that vary widely in layout, object composition, clutter, articulation, and physical interaction affordances.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A central challenge in developing such robots is how to train and evaluate them at scale before deployment. While real-world data collection is essential, it is costly, slow, and difficult to scale across the diversity of homes robots are expected to operate. As a result, simulation has emerged as a key tool for scalable robot training and evaluation, enabling rapid iteration, controlled experimentation, and safe testing of failure modes.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, most existing simulation environments remain overly simplistic and poorly matched to real human indoor spaces. Typical simulated environments consist of sparsely furnished rooms, limited object diversity, and largely static scenes. In contrast, real homes exhibit dense object arrangements, articulated furniture, and fine-grained clutter. For example, even a modest one-bedroom apartment may contain a kitchen cabinet densely packed with plates, bowls, and glasses---all individually manipulable and physically plausible. Such clutter is a central challenge in robotic manipulation, yet sparse simulated environments may fail to prepare robots for these conditions. This gap between simulated environments and real-world indoor scene distributions limits the effectiveness of simulation-based training and evaluation for general-purpose home robots. While manual environment design can produce high-quality scenes, this approach is costly, time-consuming, and does not scale easily.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We aim to close this gap by enabling the scalable generation of realistic, simulation-ready indoor environments that reflect the diversity and physical complexity of real homes. Specifically, we seek a framework that takes a natural-language description of an environment or task, and constructs a room- or house-level indoor environment through a sequence of grounded decisions, resulting in scenes that are immediately simulatable and suitable for robotic interaction. Samples from this framework should reflect real-world indoor scene distributions while matching the prompt and being physically feasible.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This problem spans both *asset generation*, producing individual objects with geometry and physical properties, and *scene generation*, where those assets are assembled into multi-room indoor environments with realistic layouts and object arrangements. Prior work has largely addressed these aspects in isolation. Asset-centric approaches focus on reconstructing or synthesizing individual objects with realistic geometrical and physical properties. Scene-centric approaches generate layouts or object arrangements assuming a fixed library of assets. In contrast, we aim to jointly generate simulation-ready assets and assemble them into complete house-level scenes, enabling end-to-end generation of environments suitable for robotics. Prior scene synthesis methods--whether procedural, data-driven, or LLM-based--primarily target furniture-level layout and visual realism, treating small objects, articulated assets, and physical properties as secondary. This is misaligned with robotics requirements, where dense arrangements of manipulable objects, hierarchical support relationships, and physically valid configurations are essential.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose SceneSmith, a hierarchical, agentic framework for generating simulation-ready indoor environments from natural language. SceneSmith constructs scenes through a sequence of stages--from architectural layout to furniture placement to small object population--organized as a tree where rooms and supporting surfaces form independent branches. Building upon recent advances in agentic AI, each stage is implemented as an interaction between three VLM agents: a designer that proposes scene modifications, a critic that evaluates feasibility and alignment, and an orchestrator that manages iterative refinement. Asset generation is tightly integrated through a routing mechanism that combines modern text-to-3D synthesis for static objects, dataset retrieval for articulated furniture, and physical property estimation, ensuring generated scenes are immediately usable for robotics simulation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate SceneSmith across 210 diverse room- and house-level prompts, demonstrating its ability to generate dense, articulated, and physically feasible indoor environments. In a user study with 205 participants, SceneSmith achieves 92.2% average realism win rate and 91.5% average prompt faithfulness win rate against baselines. SceneSmith generates 3-6x more objects than baselines (71.1 vs 11-23 objects per room on average) while maintaining $<$`<!-- -->`{=html}2% inter-object collisions and 95.6% of objects remaining stable under physics simulation, compared to 3-29% collisions and 8-61% stability for baselines. In addition, we demonstrate an end-to-end robot policy evaluation pipeline in which natural-language task descriptions are converted into diverse scene prompts, simulated robots execute policies in the generated environments, and an evaluator agent verifies task completion by jointly reasoning over symbolic scene state and visual observations. We also include qualitative demonstrations with teleoperation of a humanoid robot (RB-Y1) and zero-shot policy rollouts, further illustrating the suitability of SceneSmith scenes for robot simulation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce SceneSmith, a hierarchical, agentic framework for constructing simulation-ready indoor environments from natural language, designed to support scalable robot training and evaluation.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop an integrated asset generation and routing pipeline combining text-to-3D synthesis with retrieval for articulated objects, augmenting all assets with collision geometry and physical properties.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that SceneSmith outperforms all baselines in user studies and automated metrics, generating denser, collision-free, and physically stable scenes.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate SceneSmith in an end-to-end robotics evaluation pipeline, from natural-language task descriptions to automatic success verification.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Agentic Scene Construction for Simulation-Ready Environments", "weight": 1.0} -->

We present SceneSmith, a hierarchical agentic system for constructing simulation-ready indoor environments from natural language prompts. SceneSmith decomposes scene creation into a sequence of decisions over layout, furnishing, object population, and refinement. Each stage is implemented as an agentic interaction between a designer, a critic, and an orchestrator, each equipped with specialized tools.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Agentic Scene Construction for Simulation-Ready Environments", "weight": 1.0} -->

We begin by describing the scene representation and hierarchical construction process (Section 3.1). We then detail the agentic interactions and tool abstractions (Section 3.2). Next, we introduce the asset generation and routing pipeline used to produce simulation-ready objects (Section 3.3), followed by physical feasibility post-processing (Section 3.4). Finally, we describe an application to automatic robot policy evaluation using our generated scenes (Section 3.5).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Scene Hierarchy", "weight": 1.0} -->

Each object pairs a simulation-ready *asset* $\mathcal{A}_{i}$, comprising visual geometry, collision geometry, physical properties, and joint definitions if it is articulated, with a pose $\mathcal{X}_{i} \in {SE{}}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Scene Hierarchy", "weight": 1.0} -->

SceneSmith constructs scenes $\mathcal{S}$ through a tree of stages (Figure 2). The root stage generates architectural layout, determining the number of rooms $M$ and producing geometry $\mathcal{G}_{j}$ for each. This geometry specifies room extents and structural elements. Each room $\mathcal{R}_{j}$ is then populated independently by adding objects $\mathcal{O}_{j}$ through successive stages: furniture, wall-mounted objects, and ceiling fixtures. Each stage is guided by a room-specific prompt $\mathcal{T}_{j}$ derived from $\mathcal{T}$. Finally, selected supporting entities (furniture surfaces, wall shelves, floor regions) spawn additional branches for adding small manipulable objects to $\mathcal{O}_{j}$, each guided by an entity-specific prompt $\mathcal{T}_{j,k}$. All stages are implemented as agentic interactions (Section 3.2). This hierarchical prompt refinement enables local decisions to be made independently while remaining coherent with scene intent.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Scene Hierarchy", "weight": 1.0} -->

Finally, all room and manipuland branches are assembled into the flat scene representation $\mathcal{S}$, suitable for direct export to robot simulators.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Agentic Trio: Designer, Critic, and Orchestrator", "weight": 1.0} -->

Each stage of SceneSmith's hierarchical construction process is implemented as an interaction between three agents with complementary roles: a *designer*, a *critic*, and an *orchestrator*. This decomposition separates scene proposal, evaluation, and control flow, enabling structured refinement while keeping individual agent responsibilities simple. This separation reduces self-evaluation bias: an independent critic is better positioned to identify errors or omissions that a proposal-focused designer may overlook.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Agentic Trio: Designer, Critic, and Orchestrator", "weight": 1.0} -->

The designer proposes modifications to the scene state at the current stage using structured tools. The critic evaluates the resulting scene with respect to factors such as semantic plausibility, physical feasibility, and alignment with the stage objective, providing scalar scores and natural-language feedback. The orchestrator coordinates this interaction, tracking scores and determining when to accept a proposal, request further refinement, or terminate the stage. To prevent degradation during iterative refinement, the orchestrator maintains checkpoints of prior scene states and can revert changes when critic scores decrease.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Agentic Trio: Designer, Critic, and Orchestrator", "weight": 1.0} -->

Agent Tools. Agents interact with the scene exclusively through tools that provide structured observation and modification operations. We organize tools into functional categories that are shared across stages, including *state observation tools* (e.g., querying object metadata and poses), *visual observation tools* (e.g., rendering scene views), *scene modification tools* (e.g., placing or adjusting assets), *asset acquisition tools* for generating or retrieving simulation assets, and *feasibility verification tools* (e.g., collision and reachability checks). Object placement is performed relative to supporting surfaces. Agents specify $SE{}$ poses within a surface coordinate frame (e.g., on floors, walls, or shelves). Full $SE{}$ object poses arise by lifting these placements through the known pose of the supporting surface. In addition, certain stages expose *specialized tools* tailored to their construction context. For example, furniture placement stages include snapping tools that translate objects into contact-aligned relative configurations (e.g., chairs snapped toward tables or cabinets snapped against walls), as well as relational facing queries that evaluate whether an object is oriented toward or away from another object or architectural element.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Agentic Trio: Designer, Critic, and Orchestrator", "weight": 1.0} -->

Manipuland population stages additionally include tools for assembling multiple assets into composite object groups that are placed jointly (e.g., constructing a fruit bowl by placing individual fruit relative to a bowl and then placing the assembled group on a supporting surface). Agents may invoke arbitrarily many tools within a single turn, making complex edits via multiple atomic operations. A complete description of available tools is provided in Appendix A. Tool access is role-dependent: the designer has access to scene modification tools, the critic is restricted to observation and verification tools, and the orchestrator invokes designer and critic agents as tools while managing global control operations such as state rollback.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Agentic Trio: Designer, Critic, and Orchestrator", "weight": 1.0} -->

Agent Memory. SceneSmith maintains a persistent, agent-specific session memory within each construction stage, allowing agents to retain context across turns during iterative refinement. To bound context growth, each agent uses a turn-based memory in which the current and immediately preceding turn are retained in full, while earlier agent turns are replaced by LLM-generated summaries. Visual observations are stored in a bounded sliding window and discarded once no longer needed. Memory is reset between stages.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Asset Generation and Routing", "weight": 1.0} -->

SceneSmith integrates asset generation directly into the scene construction process, enabling open-set object vocabularies while ensuring simulation readiness. Given an asset request from a designer agent, an *asset router* resolves the request into one or more atomic assets and selects an appropriate acquisition strategy, returning validated simulation-ready objects.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Asset Generation and Routing", "weight": 1.0} -->

Generative Asset Synthesis. For static objects, SceneSmith primarily relies on generative text-to-3D synthesis rather than retrieval from existing asset libraries. Generating assets on demand also avoids training data contamination, enabling fair evaluation of robot policies on truly unseen objects. Given a textual object description, we generate a reference image using a text-to-image model (GPT Image 1.5), segment the foreground object using SAM3, and reconstruct a textured 3D mesh from the segmented image using SAM3D. The resulting mesh is canonicalized to a standard orientation, scaled to target dimensions specified in the asset request, and augmented with collision geometry and estimated physical properties (Figure 3).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Asset Generation and Routing", "weight": 1.0} -->

Articulated Object Library. For objects with movable parts, such as cabinets, drawers, or appliances, SceneSmith retrieves assets from ArtVIP, an articulated object library containing pre-authored multi-link models with joint definitions. We augment these with estimated physical properties (Appendix B.5). While generative methods are effective for static objects, in our experience, current text-to-3D approaches do not yet reliably produce articulated structure and kinematics suitable for robotics simulation.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Asset Generation and Routing", "weight": 1.0} -->

Thin Coverings. To represent flat decorative elements such as rugs, posters, or tablecloths, we introduce *thin coverings*: lightweight geometric surfaces paired with physically based materials. Thin coverings capture visual detail and clutter while avoiding unnecessary rigid-body complexity. We retrieve materials from ambientCG^11^1 and fall back to image-generated materials when library assets cannot satisfy the request (Appendix B.4).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Asset Generation and Routing", "weight": 1.0} -->

Asset Routing and Validation. The asset router decomposes composite requests into individually manipulable assets when needed (e.g., representing a fruit bowl as a bowl plus multiple fruit objects) and selects among generation, articulated retrieval, or thin covering strategies based on object type and placement context. All candidate assets undergo validation, including mesh integrity checks and VLM-based semantic verification. Assets that fail validation are regenerated or rerouted up to a fixed retry budget, after which failure feedback is returned to the agent. This routing and validation loop enables robust, scalable asset acquisition without manual curation (Appendices B.1, B.7).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Simulation Readiness", "weight": 1.0} -->

Architectural elements use volumetric geometry (e.g., walls with finite thickness) rather than planes, improving robustness to penetration under discrete time-stepping physics simulation. All objects are augmented with estimated physical properties (mass, center of mass, inertia, friction) during asset generation, enabling realistic dynamics (Appendix B.5). While SceneSmith's agentic construction process encourages semantically plausible and physically reasonable placements through iterative feedback, agents are not required to satisfy physical constraints exactly during generation. As a result, generated scenes may contain inter-object penetrations or objects placed in configurations that are not statically stable. To ensure that environments are directly simulatable, we apply a lightweight post-processing step after both furniture and manipuland placement stages that enforces physical feasibility.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Simulation Readiness", "weight": 1.0} -->

We first resolve inter-object penetrations by projecting object positions to the nearest collision-free configuration using nonlinear optimization, while preserving orientations, as. We then simulate the scene under gravity in Drake to allow unstable objects to settle into statically stable configurations. This minimizes penetrations and ensures static equilibrium without requiring manual intervention or object welding.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Application: Robot Policy Evaluation", "weight": 1.0} -->

As one application of SceneSmith, we present an end-to-end evaluation pipeline that connects natural-language robot tasks to generated environments, robot execution, and automated task verification. This enables scalable evaluation of robot policies in diverse, simulation-ready scenes without manual environment or evaluation predicate design.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Application: Robot Policy Evaluation", "weight": 1.0} -->

Given a natural-language task description (e.g., "find a fruit and place it on the table"), we first use a language model to generate a set of diverse scene prompts consistent with the task requirements. These prompts are passed to SceneSmith to produce multiple task-relevant indoor environments, allowing evaluation across varied layouts, object configurations, and clutter conditions.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Application: Robot Policy Evaluation", "weight": 1.0} -->

Robots then execute policies directly in the generated environments. As an example instantiation, we demonstrate this pipeline using a model-based pick-and-place policy that operates on the generated simulator scenes. While we use Drake for demonstration, our scenes can be exported to other major robotics simulators (e.g., MuJoCo, Isaac Sim, Genesis; see Appendix J).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Application: Robot Policy Evaluation", "weight": 1.0} -->

Finally, task completion is verified by an evaluator agent that jointly reasons over symbolic scene state and visual observations rendered from the simulator. The evaluator does not rely on fixed success predicates; instead, it uses structured tools to gather evidence for task completion, including querying object poses and rendering selected objects for visual inspection. This avoids hand-crafted success metrics and supports open-ended tasks, though at the cost of determinism. See Appendix L for details.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Baselines. We compare against five external baselines: HSM, a hierarchical framework using learned scene motifs; Holodeck, which uses constraint satisfaction for layout optimization; I-Design, a multi-role LLM pipeline; LayoutVLM, combining visual prompting with differentiable optimization; and SceneWeaver, a single-agent framework using iterative refinement. We evaluate LayoutVLM with both its original curated asset library and the larger Objaverse library used by Holodeck for fair comparison. A feature-level comparison with prior scene-generation systems is provided in Appendix K.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Ablations. We evaluate six ablations: NoCritic (initial design only), NotGenerated (HSSD assets instead of generated), NoAssetValidation (no asset validation), NoSpecializedTools (no specialized furniture or manipuland tools), NoObserveScene (no visual observations), and NoAgentMemory (no session memory).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Input Text Descriptions. We evaluate on 210 prompts across five categories: *SceneEval-100* room prompts, *Type Diversity* prompts covering underrepresented room types like pet stores and yoga studios, *Object Density* prompts for high object count scenarios, *Themed Scenes* with stylistic constraints, and *House-Level* multi-room prompts. The corpus spans both detailed instructions and sparse prompts, such as "A bedroom with a bed and a wardrobe." House-level prompts are limited to SceneSmith and Holodeck, the only multi-room baseline. See Appendix P for the complete prompt corpus.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Human Study. We conducted a pairwise comparison study with 205 crowdsourced participants, collecting 3,051 valid responses. Each comparison presents two scenes side-by-side with an interactive 3D viewer and asks two questions: which scene looks more realistic (forced choice), and which scene better follows the prompt requirements (with "Equal" option). See Appendix N.1 for details.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Automatic Evaluation. We use SceneEval with the following metrics: CNT (object count), ATR (object attributes), OOR (object-object relationships), OAR (object-architecture relationships), ACC (accessibility), NAV (navigability), and OOB (out-of-bounds). We note that these VLM-based metrics have limitations including false positives and negatives (Appendix M.2). We add two physics metrics using Drake to evaluate simulation-readiness: COL (collision rate) and STB (static equilibrium). Since baseline methods do not produce simulation-ready scenes, we augment their outputs with collision geometry and physical properties to enable fair comparison (Appendix M.2).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Scene Generation Results", "weight": 1.0} -->

#Obj

<!-- chunk {"id": "body-0041", "role": "body", "section": "Scene Generation Results", "weight": 1.0} -->

External Baselines (SceneSmith averages 71.1 ± 13.0 objects)

<!-- chunk {"id": "body-0042", "role": "body", "section": "Scene Generation Results", "weight": 1.0} -->

#Obj

<!-- chunk {"id": "body-0043", "role": "body", "section": "Scene Generation Results", "weight": 1.0} -->

Among ablations, the most impactful are NotGenerated (63.8% realism, 67.0% faithfulness), NoAssetValidation (63.0%, 62.2%), and NoObserveScene (61.5% realism), all showing significant effects. These results demonstrate that generative asset acquisition, asset validation, and visual feedback each contribute meaningfully. NoCritic, NoSpecializedTools, and NoAgentMemory show smaller effects (51--55% realism) that did not reach significance with our study power; detecting these would require 6-18x more comparisons. Notably, NoCritic achieves similar preference scores while being 70% cheaper (Appendix O.5), though it produces 24% fewer objects. While higher object density enables richer manipulation scenarios for robotics, NoCritic offers a cost-efficient alternative for applications where this trade-off is acceptable.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Scene Generation Results", "weight": 1.0} -->

Table 2 presents automated metrics. SceneSmith achieves the best performance on CNT, ATR, OOR, OAR, COL, and STB. Notably, we achieve 2.2x improvement on OOR over the best baseline. The lower ACC and NAV scores are expected given our 3-6x higher object density (71.1 vs 11-23 objects), which inherently reduces free space. The most striking difference is physics quality: SceneSmith achieves 1.2% collision rate versus 3-29% for baselines, and 95.6% stability versus 8-61%. The remaining collisions are slight penetrations (3.8mm mean depth) that are 3-12x shallower than baselines (Appendix O.1). This is a critical differentiator for robotics as our scenes are simulation-ready without post-hoc correction. House-level results are similar: SceneSmith generates 2.6x more objects (214 vs 81) while maintaining 0.9% collisions and 79.8% stability versus Holodeck's 3.8% and 17.9%.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Scene Generation Results", "weight": 1.0} -->

Beyond quantitative metrics, SceneSmith produces houses with realistic room connectivity. For example, a generated hotel scene has the entrance leading through the reception, en suite bathrooms accessible only through their associated bedrooms, and all rooms connected via a central hallway. In contrast, Holodeck often generates implausible layouts where an entire hotel might only be reachable through a guest room, or a second bedroom is accessible only through the first bedroom's bathroom (Figure 24). See Appendices N and O for additional quantitative and Appendix R for additional qualitative results.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Robot Policy Evaluation", "weight": 1.0} -->

We demonstrate the agentic robot policy evaluation pipeline from Section 3.5. We evaluate across 100 generated scenes spanning four pick-and-place tasks (three room-level, one house-level). To validate that the pipeline can discriminate between policies of varying quality, we compare a simple model-based policy against a deliberately degraded variant with relaxed motion constraints. The standard policy achieves 16% success versus 12% for the degraded variant, demonstrating that the automatic evaluation system can detect meaningful differences in policy quality. We manually verified all 300 evaluator judgments (100 scenes $\times$ 3 states: initial, standard policy, degraded policy) and found 99.7% agreement with human labels. The single disagreement was an ambiguous case where a fruit landed on the edge of a plate. See Appendix L for details and the project page for representative rollout videos.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Robot Simulation Demonstrations", "weight": 1.0} -->

Zero-shot policy rollout conditioned: “Take the apple from the bowl and place it onto the cutting board.”

<!-- chunk {"id": "body-0048", "role": "body", "section": "Robot Simulation Demonstrations", "weight": 1.0} -->

To demonstrate SceneSmith scenes in complementary robotic interaction settings, we run two qualitative robot simulation workflows. Teleoperation tests whether generated scenes support interactive manipulation and potential data collection in simulation. Zero-shot policy rollouts test whether the scenes are realistic enough for an externally trained generalist robot policy, trained primarily on real-world robot data, to operate without SceneSmith-specific tuning. For teleoperation, Figure 5 (top) shows an RB-Y1 manipulating a cabinet, with additional videos of navigation, articulated manipulation, and mobile pick-and-place on the project page. For zero-shot rollouts, we use the simulation setup from LBM Eval, replacing its environments with SceneSmith scenes, and run the text-conditioned robot policy from Lin et al.. Figure 5 (bottom) shows one representative rollout conditioned on "Take the apple from the bowl and place it onto the cutting board." In this example, the policy recognizes the apple in the bowl and the cutting board, then picks and places the apple as requested. The policy predates SceneSmith and has no SceneSmith rendering, physics, scene, or asset training data.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We present SceneSmith, a hierarchical agentic framework for generating simulation-ready indoor environments from natural language prompts. SceneSmith decomposes scene construction into hierarchical stages, each driven by designer-critic-orchestrator interactions, producing dense, physically valid scenes that capture the complexity of real homes. Our integrated asset pipeline combines generative text-to-3D synthesis with retrieval for articulated objects, enabling open-vocabulary generation while ensuring simulation readiness. Experiments demonstrate dramatic improvements over baselines: SceneSmith generates 3-6x more objects while achieving $<$`<!-- -->`{=html}2% inter-object collisions and 95.6% static stability, compared to 3-29% collisions and 8-61% stability for baselines. Human evaluators preferred SceneSmith with a 92% average win rate for realism and a 91% average for prompt faithfulness. Qualitative teleoperation and zero-shot policy rollouts further indicate that these generated scenes are suitable for interactive robot simulation beyond static scene-quality metrics. We believe these results mark a point where environment generation is no longer the primary bottleneck for scalable robot training and evaluation in simulation. We hope SceneSmith proves useful for robotics and beyond.
