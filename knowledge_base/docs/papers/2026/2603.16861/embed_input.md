<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

MolmoB0T: Large-Scale Simulation Enables Zero-Shot Manipulation

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A prevailing view in robot learning is that simulation alone is not enough; effective sim-to-real transfer is widely believed to require at least some real-world data collection or task-specific fine-tuning to bridge the gap between simulated and physical environments. We challenge that assumption. With sufficiently large-scale and diverse simulated synthetic training data, we show that zero-shot transfer to the real world is not only possible, but effective for both static and mobile manipulation. We introduce MolmoBot-Engine, a fully open-source pipeline for procedural data generation across robots, tasks, and diverse simulated environments in MolmoSpaces. With it, we release MolmoBot-Data, a dataset of 1.8 million expert trajectories for articulated object manipulation and pick-and-place tasks. We train three policy classes: MolmoBot, a Molmo2-based multi-frame vision-language model with a flow-matching action head; MolmoBot-Pi0, which replicates the pi_0 architecture to enable direct comparison; and MolmoBot-SPOC, a lightweight policy suitable for edge deployment and amenable to RL fine-tuning.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We evaluate on two robotic platforms: the Franka FR3 for tabletop manipulation tasks and the Rainbow Robotics RB-Y1 mobile manipulator for door opening, drawer manipulation, cabinet interaction, and mobile pick-and-place. Without any real-world fine-tuning, our policies achieve zero-shot transfer to unseen objects and environments. On tabletop pick-and-place, MolmoBot achieves a success rate of 79.2% in real world evaluations across 4 settings, outperforming pi_0.5 at 39.2%. Our results demonstrate that procedural environment generation combined with diverse articulated assets can produce robust manipulation policies that generalize broadly to the real world.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robotics foundation models are increasingly being built by a small number of well-resourced industrial labs. NVIDIA's GR00T \[nvidia2025gr00tn1openfoundation\], Physical Intelligence's $\pi_{0}$ \[black2024pi_0, black2025pi_05\], and Google DeepMind's Gemini Robotics \[team2025gemini\] frames large-scale real-world training as the basis for generalist manipulation agents that act in the physical world. Despite their utility, much of what matters most for training such systems remains difficult for the broader community to study: the full data mixtures, collection processes, filtering decisions, scaling regimes, and training recipes behind the strongest models are often only partially disclosed. As a result, the knowledge of what it actually takes to build a robotics foundation model from scratch remains concentrated within a small set of institutional actors rather than broadly accessible to the field.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the absence of open recipes for building these models end-to-end, much of the community has gravitated toward adapting existing systems rather than understanding the ingredients required to train them. This tendency is reinforced by a widely held assumption in robotics: that simulation alone is not enough for manipulation, and that sim-to-real gap becomes manageable only after introducing some amount of real-world data for adaptation. Under this view, simulation is useful for pretraining, bootstrapping, or stress-testing, but not as a sufficient substrate for producing robust real-world manipulation policies on its own.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We challenge that assumption. We show that when simulation is scaled aggressively, across a diversity of environments, embodiments, articulated assets, and tasks, it can support zero-shot transfer to real-world mobile manipulation without any real-world fine-tuning, photorealistic rendering, or explicit domain adaptation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This challenge arises from our prior work on navigation, SPOC \[ehsani2024spoc\]. SPOC showed that this tension can be overcome through scaled simulation data for navigation. Imitating shortest-path experts across hundreds of thousands of procedurally generated houses produces navigation policies that transfer zero-shot to real environments. A natural next question arises: can scaled simulated data enable zero-shot transfer for manipulation?

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To study this question, we introduce MolmoBot-Engine, a fully open-source pipeline for procedural data generation across robots, tasks, and diverse simulated environments, and MolmoBot-Data, a dataset of 1.7 million expert trajectories spanning articulated object manipulation and pick-and-place. MolmoBot-Engine is built on top of a subset of our recently released MolmoSpaces \[molmospaces2026\], an ecosystem of 232k environments with 48k manipulable objects across 8 types of tasks. We procedurally generate robot trajectories across a variety of manipulation tasks, including tasks such as door opening, which requires whole-body manipulation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Using this data, we train three policy classes. Our flagship model, MolmoBot, is built on top of Molmo2 \[clark2026molmo2\], our video-language model capable of ingesting past frames for context. We augment this architecture with a DiT-based flow-matching action head that is layerwise coupled to the vision-language backbone. Each action layer cross-attends to the corresponding intermediate hidden states of the underlying VLM, while also incorporating robot-state features, allowing actions to be generated from multi-scale multimodal representations. Aside from MolmoBot, we also train MolmoBot-Pi0, which exactly replicates the $\pi_{0}$ architecture for controlled comparison; and MolmoBot-SPOC, a lightweight non-VLA policy suitable for edge deployment and future RL fine-tuning.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate these policies on two robotic platforms: the Rainbow Robotics RB-Y1 mobile manipulator for door opening, drawer manipulation, cabinet interaction, and mobile pick-and-place, and the Franka FR3 for tabletop pick-and-place. Across both platforms, our policies transfer zero-shot from simulation to unseen real-world objects and environments, and outperform $\pi_{0.5}$ in our real-world evaluations. Specifically, on tabletop pick-and-place, our best MolmoBot achieves a success rate of 79.2% in real world evaluations across 4 settings while $\pi_{0.5}$ achieves 39.2%.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide ablations demonstrating the importance of data scale and diversity, and show through MolmoBot-Pi0 that our data yields strong performance even when the architecture is held constant. Our MolmoBot-Pi0 achieves a success rate of 46.7% in real world evaluations, improving upon $\pi_{0.5}$ at 39.2% when using the same architecture and training with MolmoBot-Data from scratch.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Broadly, our results suggest that the barrier to general-purpose manipulation may be less about an irreducible sim-to-real gap, and more about whether the community has access to sufficiently large, diverse, and open simulation pipelines for training robotics foundation models. We provide that access by open-sourcing all components.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Imitation learning for manipulation", "weight": 1.0} -->

Imitation learning is the leading paradigm for robot manipulation. Initial methods focused on behavior cloning that map observations to actions \[pomerleau2015alvinn, Zhang2017DeepIL\], while later work introduced hierarchical structures and temporal abstractions to address long-horizon tasks more effectively \[Lynch2019LearningLP\]. Recently, generative modeling techniques such as diffusion policies \[Chi2023DiffusionPV\] have been introduced, demonstrating strong performance on manipulation benchmarks.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Imitation learning for manipulation", "weight": 1.0} -->

Recent developments have extended imitation learning to vision-language-action (VLA) models that integrate language understanding with perception and control within a unified architecture. Systems such as RT-1 \[Brohan2022RT1RT\] and RT-2 \[Brohan2023RT2VM\] showcase that increasing model capacity and utilizing multi-task robot datasets enable policies to perform hundreds of manipulation tasks conditioned on natural language instructions. More recently, $\pi_{0}$ and its subsequent variants \[black2024pi_0, black2025pi_05\] applied a flow-matching action representation that enabled continuous action generation and supports generalist policies capable of cross-embodiment learning. Other recent works that explore cross-embodiment training using heterogeneous real-world robot datasets include X-VLA\[Zheng2025XVLAST\] that conditions a shared policy on embodiment-specific prompt tokens for multi-robot training, and LAP-VLA\[zha2026lap\] that aligns robot control with languages by representing actions as language tokens.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Imitation learning for manipulation", "weight": 1.0} -->

Although these systems exhibit impressive capabilities, they depend heavily on large-scale real-world robot demonstrations. In contrast, this work investigates training VLA policies exclusively from simulation-generated trajectories while preserving strong real-world performance.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Large-scale dataset and simulation", "weight": 1.0} -->

The advancement of generalist robot policies is closely associated with the availability of large-scale datasets. Several initiatives have gathered extensive real-world demonstrations spanning diverse tasks and embodiments, enabling learning from heterogeneous trajectories \[10611477openxembodiment\]. Datasets like DROID \[khazatsky2024droid\] offer large collection of manipulation demonstrations for training contemporary VLA models.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Large-scale dataset and simulation", "weight": 1.0} -->

Owing to the high cost and logistical challenges of real-world data collection, recent research has increasingly emphasized simulation or synthetic datasets. GraspVLA \[deng2025graspvla\] explores VLA policies trained on simulated grasping demonstrations, while the InternVLA family (InternVLA-M, InternVLA-A, InternVLA-H/N) \[tian2025interndata\] demonstrates large-scale pretraining for manipulation, action planning, navigation, and humanoid control using synthetic trajectories. Additionally, work such as PartInstruct \[Yin2025PartInstructPI\] and Infinigen-Articulated \[joshi2025proceduralgenerationarticulatedsimulationready\] illustrates the effectiveness of procedurally generated simulation datasets in supporting robot learning research.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Large-scale dataset and simulation", "weight": 1.0} -->

Our work extends this line of research by introducing MolmoBot-Engine, a fully open-source pipeline that enables scalable data generation in simulation across different robots, tasks, and diverse environments, and MolmoBot-Data, a large-scale generated dataset of expert manipulation trajectories. By combining procedural scene generation with diverse rigid and articulated assets, our dataset enables training generalist policies that transfer to real-world deployment without any real-world demonstrations.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Articulated and mobile manipulation", "weight": 1.0} -->

Manipulating articulated objects such as doors, drawers, and cabinets remains challenging due to complex contact dynamics and partially observable object states. Mobile manipulation introduces additional complexity, requiring coordination among navigation, perception, and manipulation. Most large-scale manipulation systems concentrate on fixed-base manipulators operating in tabletop environments, where perception and workspace constraints are less complex \[khazatsky2024droid, Brohan2023RT2VM\]. Several recent works that explore mobile manipulation typically address only a subset of the problem. For instance, some approaches focus on navigation relying on fixed-base manipulation skills for overall mobile manipulation tasks \[Wu2025MoToAZ\], or demonstrate only the feasibility of mobile manipulation platforms through real-world teleportation datasets \[wu2024tidybot\] or real-world online adaptation strategies \[Xiong2024AdaptiveMM\]. Other prior work has explored articulation-aware policies that incorporate object geometry and motion constraints. For example, FlowBot3D \[eisner2022flowbot3d\] learns manipulation flows to guide robot interaction with articulated objects.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Articulated and mobile manipulation", "weight": 1.0} -->

Despite these advances, mobile manipulation remains underexplored within large-scale imitation learning frameworks. A recent work used simulations to collect a scalable dataset and demonstrated that sim-to-real transfer outperformed human teleoperators \[xue2025doorman\]. However, for particular articulated categories, such as door opening, solutions remain task-specific. This study evaluates policies on both a tabletop manipulator and a mobile manipulator that performs multiple tasks such as mobile pick-and-place and door opening. The results demonstrate that large-scale simulation-generated data can produce policies that generalize to both articulated and mobile manipulation scenarios without real-world demonstrations.

<!-- chunk {"id": "body-0021", "role": "body", "section": "MolmoBot-Engine: A scalable manipulation data engine", "weight": 1.0} -->

We introduce MolmoBot-Engine, a procedural data generation pipeline for scalable robotic manipulation training, illustrated in Fig. 2. Our key insight is that manipulation policies benefit more from diversity across objects, configurations, and viewpoints than from photorealistic rendering. By rendering procedurally generated MolmoSpaces \[molmospaces2026\] environments in MuJoCo simulator with extensive domain randomization, we generate large-scale demonstration data at a fraction of the cost of real-world collection.

<!-- chunk {"id": "body-0022", "role": "body", "section": "MolmoBot-Engine: A scalable manipulation data engine", "weight": 1.0} -->

We note that MolmoBot-Engine is inherently constrained by the capabilities of the simulation platform. We focus on rigid body and articulated object manipulation (pick/pick-and-place and door/drawer/cabinet opening), as these are both tractable to model for modern simulators, as well as interesting and challenging tasks still unsolved by modern generalist policies. We hope this contribution can help towards extending simulation data generation to new classes of manipulation such as exceedingly contact-rich or soft-body manipulation.

<!-- chunk {"id": "body-0023", "role": "body", "section": "MolmoSpaces environments and assets", "weight": 1.0} -->

We leverage the objects and scenes in MolmoSpaces \[molmospaces2026\], a large collection of procedurally generated indoor environments with realistic architectural variation, room layouts, and object placement, and individual rigid objects that can be procedurally added to any scene.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Environment setup", "weight": 1.0} -->

Each episode takes place in one of the more than 200k available pre-built MolmoSpaces scenes. The layout, furniture, and static objects remain fixed, but we can adapt every scene for specific tasks by sampling from a large pool of objects and placing task-relevant objects in suitable locations for each possible task specification (e.g., we can place objects to fulfill the role of receptacle targets, pickup targets, or just as additional distractors, for various manipulation tasks). Besides this, we can also randomize visual and physical parameters.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Asset sourcing", "weight": 1.0} -->

Rigid objects for pick-and-place tasks are sourced from iTHOR \[Kolve2017AI2THORAI\] and Objaverse \[Deitke2022ObjaverseAU\], filtered for graspable size (placement receptacles with bounding boxes of side under 50 cm along the $x$ and $y$ axes and vertical size up to 15 cm, pickup objects with $xy$-plane diagonal less than that for the receptacle) and watertight collider meshes. For task roles like the receptacle target in a pick-and-place task, we additionally ensure semantic relevance by filtering based on the object metadata provided by MolmoSpaces.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Domain randomization", "weight": 1.0} -->

We extensively perform domain randomization across three axes: environment randomization, action randomization (Sec. 3.2), and camera perturbation (Sec. 3.3.3). In addition to this, during model training we also perform image augmentation.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Domain randomization", "weight": 1.0} -->

Lighting: Number of lights (\[1--N\]), positions, intensities, colors, and shadow properties. We sample both point and directional lights to simulate diverse indoor conditions.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Domain randomization", "weight": 1.0} -->

Textures: Surface materials are randomized across placed objects and, where supported, existing scene elements. We sample from procedural textures and real-world texture maps sourced from AI2THOR assets \[kolve2017ai2thor\].

<!-- chunk {"id": "body-0029", "role": "body", "section": "Domain randomization", "weight": 1.0} -->

Dynamics: Friction coefficients, object masses, and joint damping are sampled within plausible ranges to encourage robust control policies.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Pose randomization", "weight": 1.0} -->

Manipulable assets are placed at randomized 6-DoF poses within the environment, subject to collision constraints and reachability from the robot's workspace. We ensure diverse approach angles by sampling asset orientations relative to the robot base.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Robot configuration", "weight": 1.0} -->

We generate data for two robot platforms to enable both mobile manipulation and tabletop evaluation. Additional robot platforms can be easily added by future work.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Franka FR3", "weight": 1.0} -->

A 7-DoF Franka FR3 arm with a Robotiq 2F-85 parallel-jaw gripper, mounted on a fixed pedestal (0.58 m height). We use the DROID \[khazatsky2024droid\] configuration to enable direct comparison with DROID-trained baselines and evaluation on existing benchmarks. Following DROID, data generation and evaluation are run at 15 Hz.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Rainbow RB-Y1", "weight": 1.0} -->

A mobile manipulator with a holonomic base (3-DoF: $x,y,\theta$), a 6-DoF torso, a 2-DoF head (pan, tilt), and two 7-DoF arms, each equipped with a mechanically coupled parallel-jaw gripper. The base is controlled in planar joint-position mode; the head is passively set at initialization and not actuated during episodes.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Initial joint-configuration randomization", "weight": 1.0} -->

At episode initialization, each move group's joint positions are sampled as $q_{0} + \delta$, where $q_{0}$ is a nominal home configuration and $\delta_{i}\mathcal{U}{({- r_{i}},r_{i})}$ with per-joint noise magnitudes $r_{i}$. For both robots, the arm noise magnitudes are *graduated*: proximal joints receive smaller perturbations and distal joints larger ones.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Initial joint-configuration randomization", "weight": 1.0} -->

Concretely, the Franka arm uses $\mathbf{r}_{\text{arm}} = {\lbrack 0.025,0.05,0.075,0.1,0.125,0.15,0.175\rbrack}$ rad (chosen via a Jacobian-weighted heuristic to bound TCP displacement to 10 cm), and each RB-Y1 arm uses $\mathbf{r}_{\text{arm}} = {\lbrack 0.05,0.05,0.075,0.1,0.125,0.15,0.175\rbrack}$ rad. The RB-Y1 additionally randomizes head pan and tilt ($0.2$ rad $11.4$ each) and gripper aperture ($0.01$ rad). Torso and base initial joint positions are not perturbed.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Action noise injection", "weight": 1.0} -->

During data collection, noise is injected into expert actions to prevent policies from overfitting to exact action replay. The noise is *action-proportional*: its standard deviation scales with the magnitude of the commanded displacement, so stationary commands receive no noise and large motions receive proportionally more.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Action noise injection", "weight": 1.0} -->

For arm move groups, noise is applied in TCP space and then mapped back to joint space via the Jacobian pseudo-inverse. Specifically, we compute the commanded TCP displacement ${\Delta\mathbf{x}} = {J\Delta\mathbf{q}}$ from the Jacobian $J$ and the joint-space command $\Delta\mathbf{q}$. Position noise is sampled from a truncated Gaussian with $\sigma_{\text{pos}} = {\alpha\Delta\mathbf{x}_{\text{pos}}}$ and clipped to $2$ cm, where $\alpha = 0.1$ is a scale factor. Rotation noise uses $\sigma_{\text{rot}} = {0.1\sigma_{\text{pos}}}$, clipped to $0.1$ rad ($5.7$).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Action noise injection", "weight": 1.0} -->

The resulting 6-DoF TCP noise vector $\mathbf{\epsilon}_{\text{tcp}}$ is projected to joint space by solving ${J\mathbf{\epsilon}_{q}} = \mathbf{\epsilon}_{\text{tcp}}$ in the least-squares sense, and the noisy command is clipped to joint limits.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Action noise injection", "weight": 1.0} -->

For the RB-Y1 base, planar noise is applied directly to $(x,y,\theta)$ commands using clipped Gaussians with $\sigma = {0.1\Delta\mathbf{p}}$, bounded to $2$ cm in position and $0.05$ rad ($2.8$) in heading. Action noise is disabled during simulated evaluation.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Gripper handling", "weight": 1.0} -->

Gripper close and open commands execute over fixed durations of 0.5 s and 0.25 s, respectively, followed by a settle period (move_settle_time$= 0.1$ s for the Franka; up to max_grasping_timesteps$= 5$ control steps for the RB-Y1) during which the arm is held stationary. This simulates real-world grasp settling time and ensures the object is stably grasped before subsequent arm motion resumes.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Camera pose", "weight": 1.0} -->

Per-episode perturbation to camera extrinsics is described in Section 3.3.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Sensor Configuration", "weight": 1.0} -->

After placing objects and applying domain randomization, we configure the robot's sensors for the episode. We describe the camera systems for each platform, followed by additional sensor modalities.

<!-- chunk {"id": "body-0043", "role": "body", "section": "FR3 camera system", "weight": 1.0} -->

We generate data for five camera viewpoints for the Franka FR3, to provide diverse viewpoints for tabletop manipulation. In this work, we only train with the wrist camera and one randomized exocentric camera; the rest are present in MolmoBot-Data to provide for future work.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Wrist camera", "weight": 1.0} -->

A gripper-mounted camera analogous to a ZED Mini, with 52° vertical FOV (4° noise). Position is perturbed by 1.5cm lateral, 0.5cm vertical, and 2cm in depth; orientation by 8° in roll and 4° in pitch and yaw.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Fixed shoulder camera", "weight": 1.0} -->

A robot-mounted exocentric camera positioned at a fixed offset from the robot base, with 71° FOV and light randomization (5cm position, 8° orientation). Placement is constrained to maintain visibility of task objects.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Randomized exocentric cameras", "weight": 1.0} -->

Three freely-placed cameras sample positions around the workspace center: two ZED2 analogues (64--72° FOV) and one GoPro analogue (137--140° FOV). For each camera, we sample distance (0.2--0.8m for ZED2, 0.2--0.5m for GoPro), height (0.05--0.6m above workspace), and azimuth (full 360°). Lookat target is the workspace center with 10cm noise. Placement is rejected and resampled (up to 20 attempts) if task objects and gripper are not visible.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Randomized exocentric cameras", "weight": 1.0} -->

All FR3 cameras render at $624352$, chosen to be close to the real-world resolution of $640360$ while keeping both dimensions a multiple of 16 for video encoding.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Head camera", "weight": 1.0} -->

A head-mounted camera analogous to a GoPro in wide mode, rendered at 1024576 and cropped to 768576 (4:3 aspect ratio) in post-processing. We use a vertical FOV of 139° with 3° noise. Position is perturbed by 1cm in each axis, orientation by 4° around each axis, and randomized fisheye warping is applied per-frame during training.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Wrist cameras", "weight": 1.0} -->

Left and right wrist-mounted cameras analogous to Intel RealSense D405 sensors. These render at 1024576 (16:9 aspect ratio) with 58° vertical FOV and 4° FOV noise. Position noise is 1.5cm lateral, 0.5cm vertical, and 1cm in depth; orientation noise is 8° in roll and 4° in pitch and yaw. Depth is recorded for the benefit of future dataset utility but unused during training.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Robot state", "weight": 1.0} -->

We record the joint positions and velocities, TCP poses for each gripper, and the robot base pose.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Action labels", "weight": 1.0} -->

We record actions in multiple representations: commanded joint positions (absolute and relative to current joint positions), end-effector twist relative to current pose, and absolute end-effector pose. This enables training with different action parameterizations from the same trajectories.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Task state", "weight": 1.0} -->

We record the object start and goal poses, grasp state indicators, policy phase, and retry counts from the expert policy.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Camera parameters", "weight": 1.0} -->

We record the intrinsic and extrinsic parameters for each camera, enabling projection between 2D and 3D coordinates and potential depth-based augmentation. We also record points in the image frame on objects of interest in all cameras.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Camera parameters", "weight": 1.0} -->

Depth images are recorded for RGB-D camera analogues but were not used in any of the training runs reported in this work.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Rigid object manipulation", "weight": 1.0} -->

We define four rigid-body manipulation tasks, each evaluated with both the stationary Franka FR3 and mobile RB-Y1 manipulators.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Rigid object manipulation", "weight": 1.0} -->

Pick: Grasp a target object and lift it above its starting height. Success requires that the object is no longer supported by any non-robot surface and has been raised by at least 1 cm.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Rigid object manipulation", "weight": 1.0} -->

Pick-and-place: Transport a target object to a specified receptacle. The task succeeds when at least 50% of the object's weight is supported by the receptacle, and the receptacle has not been displaced by more than 10 cm or rotated by more than 45.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Rigid object manipulation", "weight": 1.0} -->

Pick-and-place-next-to: Place a target object adjacent to a reference object on the same surface. Success requires the surface-to-surface distance in the XY plane to lie within $\lbrack 0,\, 5\rbrack$ cm and the reference object to remain within 15 cm of its initial position.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Rigid object manipulation", "weight": 1.0} -->

Pick-and-place-color: Place an object on a receptacle identified by color (e.g., "place on the red plate"). Two receptacles identical (except for color) are placed in the scene; success criteria match pick-and-place.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Articulated object manipulation", "weight": 1.0} -->

We define two articulated-object tasks, evaluated with the mobile RB-Y1.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Articulated object manipulation", "weight": 1.0} -->

Open: Open a nearby articulated object (e.g., cabinet, drawer, oven, dishwasher) to at least 67% of its joint range.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Articulated object manipulation", "weight": 1.0} -->

Open-door: Open a nearby hinged door to at least 67% of its hinge joint range. The instruction is conditioned on the robot's starting pose relative to the door, yielding either "push the door open" or "pull the door open."

<!-- chunk {"id": "body-0063", "role": "body", "section": "Language instructions", "weight": 1.0} -->

During training, each task episode is accompanied by a natural-language instruction whose referring expressions are sampled at episode initialization rather than fixed. For each object referenced in the instruction, we compute CLIP-based similarity scores between candidate referring expressions and all distractor objects in the scene, then sample an expression via a softmax distribution (temperature $\tau = 0.02$) over the similarity-margin scores. This produces diverse yet unambiguous expressions (e.g., "the ceramic mug" vs. "the mug" depending on context). Expressions whose similarity margin falls below 0.03 or whose absolute target similarity is below 0.1 are filtered out to avoid ambiguous referrals. Further details on referral expressions are provided in Sec. A.2.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Expert planners", "weight": 1.0} -->

For each task, we generate expert demonstrations at scale via scripted demonstrators that iteratively sample grasps, verify feasibility, and execute motion for each task phase. Expert demonstrators for the Franka FR3 use IK-based interpolation, and for RB-Y1 use the CuRobo \[sundaralingam2023curobo\] motion generator to coordinate the many degrees of freedom with collision-aware motion planning.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Grasp sampling and filtering", "weight": 1.0} -->

Candidate loading and ranking: We load pre-computed 6-DoF grasps for each object, transform them into the world frame (including flipped variants), and rank them by a weighted cost that combines TCP proximity, rotation similarity, vertical alignment, and distance to the object center of mass.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Grasp sampling and filtering", "weight": 1.0} -->

Collision filtering: The top-ranked candidates are tested for gripper--scene collision by placing phantom collision bodies at each candidate pose in MuJoCo and running broadphase collision detection in batches of up to 128.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Grasp sampling and filtering", "weight": 1.0} -->

IK feasibility: Non-colliding candidates are checked for kinematic reachability via batch inverse kinematics (batches of up to 256). The highest-ranked feasible grasp is selected.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Phase-based trajectory generation", "weight": 1.0} -->

Each task is decomposed into a fixed sequence of phases, with motion planned independently per phase.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Phase-based trajectory generation", "weight": 1.0} -->

For pick-and-place tasks, the phases are: Pregrasp Grasp Lift Preplace Place Postplace Stow. For the RB-Y1 demonstrator, the Preplace and Place phases are combined, and we omit the additional Stow phase. In other words, the policy will first move to a pregrasp pose offset along the grasp approach axis, move to the grasp pose and close the gripper, lift the object, move to a pose above the receptacle before lowering to the placement pose and opening the gripper, and finally moving back to the home position.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Phase-based trajectory generation", "weight": 1.0} -->

Pick-and-place-next-to and pick-and-place-color are the same as pick-and-place, differing only in placement pose.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Phase-based trajectory generation", "weight": 1.0} -->

Pick tasks proceed similarly to pick-and-place, but terminate after the Lift phase.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Phase-based trajectory generation", "weight": 1.0} -->

For the open and open-door tasks, the phases are: Pregrasp Grasp Articulate Postarticulate. After grasping the handle, articulation-specific end-effector waypoints are computed: a circular arc about the hinge axis for revolute joints (doors), or a linear path along the slide axis for prismatic joints (drawers). The planner solves for each waypoint sequentially using IK or trajectory optimization.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Retry behavior", "weight": 1.0} -->

Each demonstrator is equipped with retry behavior. While executing a task, if the demonstrator detects a mistake (the object fell out of the grasp, the robot failed to acquire the grasp, etc.) it will reset to the first phase of the trajectory and try again. If more than 3 retries are triggered in an episode, it is terminated and discarded. This explicit retry behavior imbues policies with the ability to handle and recover from mistakes or disturbances.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Motion planning for RB-Y1 with CuRobo", "weight": 1.0} -->

For the RB-Y1, we use CuRobo \[sundaralingam2023curobo\] for GPU-accelerated collision-aware trajectory optimization. For each phase requiring collision-free motion (e.g., pre-grasp approach, placement), the planner constructs a cuboid-approximated collision world from the mesh-based MuJoCo scene, then plans in batches: multiple candidate goal poses are evaluated in parallel (default batch size of 4, up to 4 batches), and the trajectory with the least total joint displacement is selected. When a waypoint cannot be reached within a fixed number of control steps, the planner re-plans from the current configuration, up to a maximum of 5 re-planning attempts per phase. We provide additional details on CuRobo configuration in Appendix A.1.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Dataset Statistics", "weight": 1.0} -->

Table 1 summarizes MolmoBot-Data. We generate 1.7M episodes comprising 295M frames across more than 11k unique target object assets, more than 9k receptacle object assets, and more than 94k environments, which are further modified by the procedural addition of task-relevant per-episode objects.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Comparison to prior datasets", "weight": 1.0} -->

Table 2 compares MolmoBot-Data to prior manipulation datasets.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Generation throughput", "weight": 1.0} -->

A key advantage of simulation-based data generation is scalability. Using 100 NVIDIA A100 80GB GPUs, we generate approximately 660 successful episodes per GPU-hour (with about 50% of the time spent on rollouts and the rest on scene setup and task sampling) or, equivalently, more than 88 hours of robot experience per hour of wall-clock time. The full MolmoBot-Data dataset was generated in approximately 6,500 GPU-hours. This represents a near 2.6× data throughput^11^1Using ALOHA \[zhao2023learning\] as reference, where the effective real-time factor of a single human demonstrator is 1/3 for tasks of similar duration to ours, due to episode reset overhead or operator mistakes. compared to real-world data collection at equivalent scale with human demonstrators, enabling rapid iteration on data composition and task design as well as rapid adoption of new robotics platforms.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Models and training", "weight": 1.0} -->

We train three policy classes on MolmoBot-Data, enabling comparison across architectures and against external baselines.

<!-- chunk {"id": "body-0079", "role": "body", "section": "MolmoBot: VLM-based manipulation policy", "weight": 1.0} -->

MolmoBot builds on Molmo2-4B \[clark2026molmo2\], a vision-language model pretrained on large-scale image-text data. The architecture consists of three components: a vision encoder that processes RGB observations from input camera views a language model which jointly encodes visual features and task instructions, and a DiT-based flow matching action head that predicts robot actions, as visualized in Fig. 4.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Vision encoder", "weight": 1.0} -->

Visual observations are encoded via SigLIP2 \[siglip2\] and projected into the language model's embedding space. We freeze the vision encoder and the projector weights during training and train only the action head and the language model. We train MolmoBot to ingest up to $F = 3$ frames per view. We encode each image individually and image tokens for each 22 patch windows are pooled into a single vector using a multi-headed attention layer, where the mean of the patches serves as the query. Each image is encoded with $192$ tokens. We concatenate image tokens from available camera views (head-mounted, external, and wrist cameras, depending on the platform), interleaved with text tokens encoding the image indices and view indices when appropriate. Optionally, we encode the corresponding initial-timestep images to provide context about the starting scene configuration.

<!-- chunk {"id": "body-0081", "role": "body", "section": "LLM", "weight": 1.0} -->

The LLM takes as input the visual tokens interleaved with image indices jointly with the tokenized language instruction. For tasks requiring spatial grounding, we optionally condition on 2D point coordinates specifying target objects or placement locations; these are injected as special tokens in the instruction stream (e.g., \ OBJECT \</points\>). We use bi-directional attention for the vision tokens and causal attention for the text tokens during training and inference.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Action head", "weight": 1.0} -->

The action head is a DiT \[peebles2023scalable\] which contains self-attention and cross-attention in each layer, where it attends to features of the Molmo2 backbone via cross-attention. Following recent work on flow matching for action prediction \[black2024pi_0\], the DiT iteratively denoises action chunks conditioned on a continuous timestep embedding $t{\lbrack 0,1\rbrack}$. The timestep embedding is used by each DiT block to modulate the embedding via adaptive layer normalization \[black2025pi_05\].

<!-- chunk {"id": "body-0083", "role": "body", "section": "Action head", "weight": 1.0} -->

MolmoBot's action head has the same number of layers as the LLM encoder, and each action layer cross-attends to the hidden states of the input sequence (including the encoding of both vision and language) of the corresponding LLM layer. LLM and DiT have different hidden dimensions, so hidden states from the LLM are also projected to DiT's hidden dimension. We also encode robot states through a single-layer MLP, and concatenate them to the end of the VLM sequence before entering cross-attention at each layer. We train the action head to predict chunks of $H = 16$ actions and execute 8 before re-querying the policy following \[zhao2023learning\].

<!-- chunk {"id": "body-0084", "role": "body", "section": "Action representation", "weight": 1.0} -->

We parameterize actions in joint space using two representations: absolute joint positions and joint position deltas. Both are continuous values representing the target configuration for each joint. At each timestep, the policy predicts targets for all actuated joints, including the gripper. For the RB-Y1's mobile base, we additionally predict base velocity commands (linear and angular) which are concatenated to the joint action. Joint-space control avoids the computational overhead and potential singularities of inverse kinematics at execution time. We train separate model variants on absolute and delta representations for the Franka FR3 task and compare their performance in Section 5. We only use delta policies for training the mobile manipulation task.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Single-frame training", "weight": 1.0} -->

We train MolmoBot with the behavior cloning objective. We train with a batch size of 1024 and train the model for $200K$ steps for the static manipulation task and for $100K$ steps for the mobile manipulation task. We use a learning rate of $110^{- 5}$, using a $2k$ step warm up for the LLM and a $200$ step warm up for the action head. When sampling training examples from an expert roll-out, we up-sample steps with retry grasping behavior by $3$, steps with a successful pick by $2$ and task completion behavior by $2$. The motivation is to improve the model's grasping behavior and avoid picking objects after task completion.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Single-frame training", "weight": 1.0} -->

Our action head has a significantly lighter compute footprint than the VLM encoder. We leverage this during training by sampling multiple time steps $T$ per example to denoise in parallel. This enables us to train the model at multiple time steps for a given observation and action pair. This in turn improves the convergence and the accuracy of the model. We use $T = 8$ to train all MolmoBots unless otherwise stated and report performance with various settings in section 5. We denote the single frame model MolmoBot-Img.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Multi-frame training", "weight": 1.0} -->

We train two multi-frame MolmoBots denoted as MolmoBot (F=2) and MolmoBot (F=3) with number of frames $F = 2$ and $F = 3$ respectively. For the multi-frame training, we initialize the model with the weights from MolmoBot-Img and train the model for $50K$ steps while keeping all the other training details the same as MolmoBot-Img. When using multiple frames, the model takes as input the frame from the cameras at the current state and the frames sampled $D$ steps ago. We use $D = 8$ in all our experiments. Practically, the $F = 3$ model takes the current state, the state $0.5$ second before the current state and the state $1$ second before the current state.

<!-- chunk {"id": "body-0088", "role": "body", "section": "MolmoBot-Pi0", "weight": 1.0} -->

To isolate the effect of MolmoBot-Data on real-world VLA performance, we present MolmoBot-Pi0, a VLA with identical architecture as $\pi_{0}$ \[black2024pi_0\], trained entirely on our synthetic data from the initial Paligemma weights. This enables head-to-head comparisons with existing SOTA VLAs, controlling for modeling or architecture changes.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Architecture", "weight": 1.0} -->

Following \[black2024pi_0\], MolmoBot-Pi0 uses the Paligemma 3B VLM with a flow-matching action expert. We use the openpi \[openpi\] codebase for all MolmoBot-Pi0 modeling code, ensuring equivalence with $\pi_{0}$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Training protocol", "weight": 1.0} -->

We train for 200k steps at a batch size of 1024 with a learning rate of $510^{- 5}$, using a 1k step warmup. To prevent overfitting to simulation rendering artifacts, we freeze the entirety of the SigLIP vision encoder. Robot actions are supervised as absolute joint positions, following findings from PolaRiS \[jain2025polaris\]. All other training parameters (flow matching timestep sampling, other optimizer hyperameters, etc.) are left as the default values.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Overview", "weight": 1.0} -->

SPOC \[ehsani2024spoc\] is a transformer-based architecture that demonstrated that imitation learning from shortest-path experts across hundreds of thousands of procedurally generated houses can produce navigation policies that transfer zero-shot to real-world environments. Inspired by this architecture, MolmoBot-SPOC introduces a lightweight transformer-based policy with several modifications that make it suitable for our static and mobile manipulation tasks.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Visual, Language, and Proprioceptive Encoding", "weight": 1.0} -->

Visual observations from all camera inputs are encoded using a SigLIP2-Base patch 16/256 image encoder \[siglip2\], retaining the full set of patch tokens. Language goal instructions are encoded separately using the SigLIP text encoder \[siglip\]. The resulting token sequences consist of visual patch embeddings, language goal tokens, and the robot's current joint state projected into the model's token dimension via a learned linear projection. These tokens are concatenated along the sequence dimension to form the cross-attention memory of the action decoder (Fig. 4). For tasks that provide spatial goal specifications, MolmoBot-SPOC optionally incorporates point-based goal encodings into the cross-attention memory. Depending on the task, one or two 2D pixel coordinates are provided: a single normalized image coordinate $(x,y)$ for pick, open, and door-open tasks, or two coordinates $(x_{1},y_{1},x_{2},y_{2})$ for pick-and-place tasks.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Visual, Language, and Proprioceptive Encoding", "weight": 1.0} -->

Each coordinate is first passed through a sinusoidal positional encoder and then projected into the model's token dimension using a linear layer. A learned coordinate position embedding is added to each encoded point, and the resulting point tokens are concatenated with the other inputs in the cross-attention memory. MolmoBot-SPOC does not condition on any trajectory history; only the current timestep's observations and state are used. Optionally, we encode the corresponding initial-timestep images to provide context about the starting scene configuration when using point-based goal specification.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Action representation and quantile binning", "weight": 1.0} -->

MolmoBot-SPOC formulates action prediction as a discrete classification problem. Continuous action values are tokenized using a quantile binning strategy. Prior to binning, actions are normalized using the 1st and 99th percentiles of the training distribution, rescaling and clipping values to the $\lbrack{- 1},1\rbrack$ range based on empirical quantiles. The normalized action space for each dimension is then divided into 256 bins, where bin boundaries correspond to equally spaced quantiles of the data (i.e., the $k/256$ quantile for $k = {1,\ldots,256}$). This produces data-adaptive bins that are approximately uniformly populated, yielding a well-calibrated discrete representation of the continuous action space. The decoder predicts a categorical distribution over the 256 bins independently for each action dimension at every timestep in the chunk and is trained using a standard cross-entropy loss.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Parallel action decoding", "weight": 1.0} -->

Following \[zhao2023learning\], MolmoBot-SPOC replaces the autoregressive decoder used in SPOC with a non-causal parallel decoder (Fig. 4). Instead of predicting actions sequentially, the decoder predicts an entire chunk of $DT$ action tokens in a single forward pass, where $D$ is the number of robot action dimensions and $T = 16$ is the fixed chunk length. The decoder is provided with $DT$ learnable query embeddings---one for each $(\text{action dimension},\text{timestep})$ pair in the chunk. Using bidirectional self-attention allows each query token to attend to all others within the chunk. Temporal structure is encoded using sinusoidal positional encodings applied over the flattened sequence of $DT$ positions, which are added to the learnable query embeddings before decoding.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Data mixing", "weight": 1.0} -->

Table 3 details the different training sets we use to train all the Franka FR3 policies. Pick-and-place Random Height comprises of pick and place tasks with the robot position initialized at random heights, while Pick-and-place Fixed Height initializes the model at the default droid position \[khazatsky2024droid\]. Training with randomized heights makes the model more robust to inference time variations. Pick-and-place-color trains the model to attend to the color attribute in input task and Pick-and-place-next-to training helps improve the models spatial understanding. Table 4 details the various data mixtures used to train RB-Y1 policies. Door-open is a specialized door opening task, while the Open task includes training samples to open cabinets and drawers.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Data augmentation", "weight": 1.0} -->

We use image augmentation to improve our models' sim to real transfer. Specifically, we use ColorJitter, GaussianBlur, RandomPosterize, RandomSharpness and RandomGrayscale with different probabilities. Furthermore, we add prompt randomization during training to make the robot robust to inference time variation in language instruction. Further details on prompt randomization are detailed in Sec. A.2.1.

<!-- chunk {"id": "body-0098", "role": "body", "section": "DROID Input/Output", "weight": 1.0} -->

For all MolmoBot models trained for the DROID platform, we train on 2 of the cameras detailed in Sec. 3.3.3: the wrist ZED Mini camera, and one randomized exocentric ZED 2 camera. In addition to images, the current joint angles are also given to the model. All MolmoBot DROID models output actions as absolute joint position commands.

<!-- chunk {"id": "body-0099", "role": "body", "section": "RB-Y1 Input/Output", "weight": 1.0} -->

For all MolmoBot models trained for the RB-Y1 platform, we train on all 3 generated camera views: the head and both wrist cameras. MolmoBot-SPOC Articulated uses the repeated first frame of the trajectory and a normalized image point to ground the task spatially. The point is sampled from ten candidates that are on the desired task object to be manipulated. MolmoBot uses similar point conditioning for the door and articulated tasks. We also provide current joint angles. All RB-Y1 models output torso and arm actions as delta joint position commands, and mobile base commands as linear and angular offsets from the current pose.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Experiments", "weight": 1.0} -->

To illustrate the performance and generality of MolmoBot policies and the MolmoBot-Engine, we train and evaluate on multiple tasks in various real-world and simulated settings.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Experiments", "weight": 1.0} -->

We begin with real-world evaluations, demonstrating the policies' strong zero-shot sim2real transfer in multiple settings. We further corroborate these results with diverse simulation evaluations, including on an established manipulation benchmark. Finally, we ablate key design and data-mixture decisions and analyze the recipe for sim2real transfer.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Experiments", "weight": 1.0} -->

Crucially, all models are only trained on sim, with zero task-specific or real-world post-training or finetuning. All MolmoBot policies have never seen any real-robot data.

<!-- chunk {"id": "body-0103", "role": "body", "section": "DROID", "weight": 1.0} -->

For our DROID evaluations, we compare against $\pi_{0}\text{-DROID}$ \[black2024pi_0\] and $\pi_{0.5}\text{-DROID}$ \[black2025pi_05\], which are SOTA open-weights manipulation policies for DROID. Both are trained with \>10k hours of real-world manipulation demonstrations, and $\pi_{0.5}$ further improves by adding new innovations like subgoal prediction, heterogenous cotraining, and more. Therefore, $\pi_{0}$ is the most closely comparable baseline in terms of modeling decisions, while $\pi_{0.5}$ represents one of the best generalist manipulation policies available today. Note that unlike MolmoBot-Data, the data used to pretrain the $\pi$-family models is not publicly available, limiting future reproduction or study by the field at large.

<!-- chunk {"id": "body-0104", "role": "body", "section": "RB-Y1", "weight": 1.0} -->

The RB-Y1 has significantly less community adoption than DROID. MolmoBot policies are therefore, to our knowledge, the first generalizable pick-and-place and articulated object manipulation policies available for the RB-Y1. Lacking other generalist baselines, we reserve quantitative comparisons for our DROID evaluations.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Setup", "weight": 1.0} -->

We evaluate MolmoBot policies and baselines using three different physical DROID platforms, in four real-world environments across two geographical locations and institutions. In each environment, we evaluate each policy on 10 pick-and-place tasks, with 3 trials each. Cumulatively, each policy is evaluated 120 times. Evaluation environments are pictured in Fig. 5, and further details on real-world environment and task design are provided in Sec. B.1 in the appendix.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Setup", "weight": 1.0} -->

For pick-and-place tasks, given a task prompt (e.g. "put the banana in the black bowl"), the policy must move the specified object to be stably in or on the given receptacle. If the policy accomplishes this for a reasonable amount of time within the episode horizon (900 steps), the trial is counted as a success. Failure to do so within the episode horizon, or exhibiting unsafe behavior (high-speed collisions, etc.) before success counts as a task failure.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Results", "weight": 1.0} -->

In our real-world static manipulation evaluations, MolmoBot policies exhibit strong zero-shot sim2real transfer, as illustrated in Fig. 7. MolmoBot and MolmoBot-Img significantly outperform $\pi_{0.5}\text{-DROID}$ while MolmoBot-Pi0 is competitive, all without the benefit of $\pi_{0.5}\text{-DROID}$'s architectural improvements. Additionally, all MolmoBot policies perform much better than $\pi_{0}$. Despite having identical architectures, MolmoBot-Pi0 significantly outperforms $\pi_{0}$ in our evaluations. Therefore, this difference in performance can only be explained by data.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Results", "weight": 1.0} -->

This suggests that the diversity of simulated demonstration data is sufficient to deliver performance on-par or better than commensurate amounts of real-world data, the diversity of which is limited by real-world cost and practicality. We further study to what extent different types of data diversity and scale impact policy performance in Sec. 5.3.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Setup", "weight": 1.0} -->

We evaluate the MolmoBot Door Specialist policy on a door opening task in three real-world environments, each featuring a distinct pull door with different visual textures, handle configurations, and surrounding scene context. Unlike push doors, pull doors require the robot to precisely grasp the handle and exert a pulling force, making the task significantly more challenging --- the robot cannot rely on contact-rich recovery strategies or simply driving into the door to produce motion. Each environment also features distinct wall geometry and background clutter, testing the generalization of the policy across varied visual conditions. Episodes were executed at a 100ms inference timestep for safety reasons, which is slower than the timestep used during simulation evaluation.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Setup", "weight": 1.0} -->

For our simulation results, we evaluate both MolmoBot and MolmoBot-SPOC across four tasks. Pick and pick-and-place are evaluated in the MSProcObja scene dataset, while open is evaluated in the MSProcCrafted dataset, and Door Open in the MSProc dataset. Pick, open, and door-open benchmarks consist of 2,000 episodes each, while pick-and-place uses 1,000 episodes. We report the oracle success rate, where an episode is considered successful if the task reports 5 consecutive successful steps at any point during the trajectory. Simulation evaluation was run with an inference dt of 800ms; in other words, we execute 8 of the predicted actions from a given action chunk where each action has a dt of 100ms.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Results", "weight": 1.0} -->

In the real results represented by Tab. 5, we observed 4 out of 9 trials with handle grasp success and 2 out of 9 trials with door opening success. A recurring source of failure across Door 1 and Door 3 was difficulty grasping the handle. Both of these doors have handles positioned on the right side of the door, a configuration that is underrepresented in typical door interaction datasets and in our training data, which may explain the policy's reduced grasping reliability in these cases. In contrast, Door 2, whose handle configuration was more commonly represented, saw successful grasps in all three trials.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Results", "weight": 1.0} -->

Several trials were also affected by hardware faults, where the robot triggered its own emergency stop at various stages of execution. Once the e-stop is activated, the gripper cannot be reset mid-episode, meaning that if a fault occurs during the grasp phase the robot is unable to recover and the episode fails regardless of subsequent behaviour. In trials where faults occurred during the opening phase (Door 2, Trials 2 and 3), the robot had already successfully grasped the handle and was able to complete the door opening despite the fault, suggesting that the policy had committed to a successful trajectory before the fault manifested.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Simulation Evaluation", "weight": 1.0} -->

In Sec. 5.1, we demonstrated that MolmoBot policies demonstrate strong performance in real-world evaluations. However, real evaluations are expensive, and therefore have relatively large associated uncertainty and reduced controllability. To address this, we conduct systematic simulation evaluations, providing greatly reduced uncertainty, making trends more clearly visible, and enabling thorough data-mixing ablations.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Setup", "weight": 1.0} -->

We evaluate on held-out procedural houses with asset instances unseen during training, following an evaluation protocol similar to MolmoSpaces \[molmospaces2026\]. For each task, we generate evaluation episodes across a large number of held-out houses and report the oracle success rate (task completion at any timestep). For pick-and-place tasks, we also report the success at end (success conditions being fulfilled at the final timestep). Full details on evaluation tasks are provided in section˜B.2.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Tasks", "weight": 1.0} -->

We evaluate on a progression of increasingly difficult tasks (table˜6) in 1000 episode benchmarks. We begin with a simple pick task in a controlled configuration and limited object diversity (Pick MSProc). The next set of tasks introduces more challenging object and viewpoint distributions in three variants: standard MuJoCo rendering (Pick Classic), photorealistic filament rendering (Pick) which is out of distribution for our training data, and heavily randomized camera viewpoints (Pick Random-Cam). Pick tasks are allotted 20 seconds for completion. We then evaluate pick-and-place variants including placing objects inside a receptacle (Pick&Place), next to a target (PnP Next-To), and in a receptacle of a specified color (PnP Color), all using filament rendering. We consider a Next-To episode as a success if the object to be moved is placed within $5$ cm of the target object. Pick-and-place tasks are allotted 40 seconds due to their increased difficulty. We report only oracle success (task completed at any timestep) for pick tasks, as termination behavior is not well-defined for object lifting.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Tasks", "weight": 1.0} -->

For pick-and-place tasks, we report both final success rate and oracle success rate. The gap between these metrics reflects whether the policy can recognize task completion and disengage appropriately rather than continuing to manipulate the object after placement.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Tasks", "weight": 1.0} -->

Pick Rand.-Cam.
Pick&amp;Place

<!-- chunk {"id": "body-0118", "role": "body", "section": "Baselines", "weight": 1.0} -->

We compare against several existing vision-language-action models. $\pi_{0.5}$ \[black2025pi_05\] is evaluated both zero-shot and after fine-tuning on MolmoBot-Data for 15K steps in order to adapt it to simulation. We also evaluate StereoVLA \[deng2025stereovla\], LAP-VLA \[zha2026lap\], and X-VLA \[Zheng2025XVLAST\] zero-shot.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Results", "weight": 1.0} -->

Our models outperform all baselines across tasks. On the least-variation Pick MSProc task, MolmoBot (F=2) achieves 93.5% success compared to 48.0% for the strongest baseline ($\pi_{0.5}$-Finetune). The gap widens on more challenging distributions: on Pick Random-Cam, our models achieve 40--66% success while $\pi_{0.5}$ variants reach only 8--30%. Other VLA baselines (StereoVLA, LAP-VLA, X-VLA) fail almost entirely on our evaluation suite, with success rates below 7% on most tasks. On pick-and-place tasks, which require both grasping and placement, MolmoBot variants achieve 63--67% oracle success on Pick&Place. $\pi_{0.5}$-Finetune achieves 43.5% oracle success on this task. Notably, our models generalize to compositional instructions (PnP Color) where they must identify the correct receptacle by color, achieving 57--62% final success.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Results", "weight": 1.0} -->

Averaging across simulation tasks, MolmoBot (F=2) achieves 64.1% compared to 10.1% for $\pi_{0.5}$ zero-shot. MolmoBot-Pi0, which uses the $\pi_{0}$ architecture trained on our data, achieves 41.8%---substantially higher than $\pi_{0.5}$ zero-shot and competitive with $\pi_{0.5}$-Finetune on pick tasks---demonstrating that much of the performance gain comes from MolmoBot-Data rather than architectural differences. On real-world evaluation, MolmoBot (F=2) achieves 79.2% success, compared to 31.3% for $\pi_{0.5}$. Interestingly, $\pi_{0.5}$-Finetune is competitive with our best policies on PnP NextTo, achieving best oracle success though not final success.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Results", "weight": 1.0} -->

This supports the notion that fine-tuning real-world-native policies on sim data to bridge the real-to-sim gap enables reasonable comparisons, further bolstered by our results in the real world.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Results", "weight": 1.0} -->

Pick MSProc (sim)
Pick Kitchen (real)

<!-- chunk {"id": "body-0123", "role": "body", "section": "Results", "weight": 1.0} -->

Table˜7 evaluates models using only the fixed-shoulder camera, a more constrained setup that matches typical single-camera deployments. We test in simulation (Pick MSProc, 1000 episodes) and on 30 real-world trials in a kitchen environment (Pick Kitchen).

<!-- chunk {"id": "body-0124", "role": "body", "section": "Results", "weight": 1.0} -->

In simulation, our models maintain strong performance: MolmoBot variants achieve 91--93% success, while MolmoBot-SPOC reaches 70.4%. $\pi_{0.5}$-Finetune achieves 48.0% and $\pi_{0.5}$ zero-shot 18.1%. DreamZero performs zero-shot competitively at 44.3% while StereoVLA and LAP-VLA again perform poorly (6.6% and 19.4%).

<!-- chunk {"id": "body-0125", "role": "body", "section": "Results", "weight": 1.0} -->

On real-world evaluation, our models demonstrate successful zero-shot sim-to-real transfer. MolmoBot-Img peaks on this real world subset at 86.6% followed by MolmoBot (F=3) at 73.3% success and MolmoBot (F=2) at 70.0%. All variants perform better than $\pi_{0.5}$ zero-shot at 63.3%. The MolmoBot-SPOC achieves 36.6%, lower than the VLA variants but notable given its substantially smaller size and suitability for edge deployment. These results confirm that policies trained entirely on MolmoBot-Data transfer to real environments without fine-tuning.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Results", "weight": 1.0} -->

We additionally evaluate on external benchmarks SIMPLER \[li2024evaluating\] and LIBERO \[liu2023libero\], reimplemented for our DROID setup. These benchmarks were designed for in-domain evaluation of policies trained on specific demonstration datasets (RT-1/Bridge and LIBERO demonstrations, respectively) rather than zero-shot generalization. We find that while MolmoBot outperforms baselines on these benchmarks, the tight coupling between task specifications and benchmark-specific assets severely limits their utility for assessing generalist manipulation policies. Full results and discussion are provided in Appendix C.

<!-- chunk {"id": "body-0127", "role": "body", "section": "RB-Y1 Results", "weight": 1.0} -->

Table 8 reports zero-shot simulation performance across all RB-Y1 policies. MolmoBot Multitask outperforms MolmoBot-SPOC across all shared tasks, which we attribute to several factors. First, MolmoBot's frozen VLM backbone provides rich visual representations that generalize well without task-specific finetuning, whereas MolmoBot-SPOC's smaller transformer architecture has more limited capacity. Second, MolmoBot Multitask was trained jointly across all tasks, which may have enabled positive transfer between related manipulation behaviors. Although MolmoBot-SPOC demonstrates more modest performance in these evaluations, its compact scale enables future on-policy reinforcement learning in simulation, which has been shown to yield substantial performance gains \[hu2024flareachievingmasterfuladaptive\].

<!-- chunk {"id": "body-0128", "role": "body", "section": "Data Ablations", "weight": 1.0} -->

In this section, we study how several properties of the training data affect performance, including data scale, the number of unique objects, the number of unique houses, and image augmentation. We observe some expected trends, such as performance improving monotonically as the amount of training data increases. We also find some surprising results, such as increasing the number of unique house environments having little effect on performance. All data ablations report performance on the pick task for the MolmoBot-Img model trained for $24K$ steps with batch size 512.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Evaluation Details", "weight": 1.0} -->

Unlike Sec. 5.1, the data ablation real-world evaluations are on the pick task. The evaluations are performed with the DROID platform in the workroom environment (pictured in Fig. 5), but with different objects: a roll of blue tape, mug, aerosol can, banana, pill bottle, and wooden spoon. Evaluations are done in three groups of three objects, with five trials for each object. For object class ablations, we adjust the object list slightly such that two out of the six objects are strictly in unseen classes for all top 100: apple and screwdriver replace the tape and wooden spoon. Success is judged by the evaluator when the object is fully off the table by approximately 2cm or more. Our simulation results are for Pick-Classic, as detailed in Sec. 5.2. For each picking evaluation, the task prompt is formatted as: "pick up the \<object\>".

<!-- chunk {"id": "body-0130", "role": "body", "section": "Scaling Number of Demonstrations", "weight": 1.0} -->

To study how performance changes with the data scale, we vary the total number of training demonstrations while keeping the number of house environments and object classes fixed. Concretely, we train MolmoBot-Img on datasets containing 10K, 25K, and 50K demonstrations sampled from the same set of 5K environments and 12.4K object categories. We evaluate the model for the pick task in both simulation and real. We observe predictable scaling trends as pick performance for both domains improves with the number of demonstrations (figure 8 (a)).

<!-- chunk {"id": "body-0131", "role": "body", "section": "Scaling Environment Diversity", "weight": 1.0} -->

For this ablation we vary the number of unique houses in the training set while keeping the total number of demonstrations fixed. Specifically, we contrast many demonstrations from fewer houses with fewer demonstrations spread across more houses. We fix the data scale at 50K trajectories. Unexpectedly, we find that increasing the number of unique training environments has little effect on downstream performance (Figure 8). This suggests that, for the pick task, performance is driven more by the total amount of interaction data than by scaling environment diversity.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Scaling Object Diversity", "weight": 1.0} -->

We train MolmoBot-Img with a fixed number of 50K trajectories while sampling from 5 to 100 objects. We find that performance improves as expected for the simulated evaluation (Figure 8 (c)). However, the performance on DROID does not have a clear trend with respect to object diversity. We hypothesize that the number of objects beyond a small number does not improve performance on DROID because the number of objects in the evaluation is limited and semantically common such as apple and cup.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Model Ablations", "weight": 1.0} -->

As in Sec. 5.3, our model ablation experiments are run in the real-world on the pick task in the workroom environment, and on Pick-Classic in simulation.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Timesteps sampled during training", "weight": 1.0} -->

We sampled multiple time steps $T$ per example and denoise in parallel during to improve the convergence and the accuracy of the model. We ablate the choice for $T{\{ 1,2,4,8\}}$ during training and report the performance of MolmoBot-Img (Figure 9). Performance on simulation benchmarks improves as $T$ increases and peaks at $T = 8$, suggesting the increase $T$ helps. However, while the result on real subset of 30 examples is not as clear, with the performance peaking at $T = 4$.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Action representation", "weight": 1.0} -->

We compare MolmoBot-Img trained using absolute and delta representations on the complete multi-task data mix for $200K$ steps each for the Franka FR3 policies (Figure 9). On the Franka FR3 task, the absolute policy significantly outperforms the delta policy in real setting, while the simulation results are on-par for both policies. The significant gap in real across 3 of our benchmarks strongly suggests that absolute joint policy models transfer better to real world tasks.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we demonstrate that zero-shot transfer to the real world is not only possible, but effective for both static and mobile manipulation. We introduce MolmoBot-Engine, use it to generate MolmoBot-Data and then use that to train three policy classes: MolmoBot, MolmoBot-Pi0 and MolmoBot-SPOC. We evaluate on two robotic platforms: the Franka FR3 for tabletop manipulation tasks and the Rainbow Robotics RB-Y1 mobile manipulator. Without any real-world fine-tuning, our policies achieve zero-shot transfer to unseen objects and environments. On tabletop pick-and-place, MolmoBot achieves a success rate of 79.2% in real world evaluations demonstrating that procedural environment generation combined with diverse articulated assets can produce robust manipulation policies that generalize broadly to the real world. We release MolmoBot-Engine to enable the community to extend this approach to new robots, tasks, and object categories.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Conclusion", "weight": 1.5} -->

While a promising step for scaling up simulation-based pre-training, there are still several avenues of improvement for MolmoBot. MolmoBot-Engine is fundamentally constrained by assets that can currently be accurately simulated. We focus on rigid body and articulated object manipulation---tasks where modern simulators provide sufficient fidelity for transfer. Extending to contact-rich manipulation (e.g., insertion, peg-in-hole), deformable objects (cloth, rope, food), or tasks requiring accurate fluid or granular dynamics remains an open challenge. We believe that coupled with advances in physics-based and generative *world model* simulators, our recipe of massive-scale procedural generation may extend to these more challenging tasks requiring contact-rich dexterity and deformables. We are excited by the potential frontiers of open research this work enables.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Author Contributions", "weight": 1.0} -->

This project was made possible through the equal contributions of all four co-first authors, who are listed in alphabetical order.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Author Contributions", "weight": 1.0} -->

Abhay Deshpande led data generation for Franka FR3, efforts around MolmoBot-Pi0 training, and real evaluation for Franka FR3.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Author Contributions", "weight": 1.0} -->

Maya Guru led data generation for RB-Y1 object manipulation + drawer/cabinet articulation, MolmoBot-SPOC architecture + training for mobile manipulation, and real evaluation for RB-Y1.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Author Contributions", "weight": 1.0} -->

Rose Hendrix led the project, wrote large parts of the core data engine and scaling infrastructure, and advised on all components.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Author Contributions", "weight": 1.0} -->

Snehal Jauhri led data generation for RB-Y1 door opening and MolmoBot training for mobile manipulation.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Author Contributions", "weight": 1.0} -->

Ainaz Eftehar led MolmoBot-SPOC architecture and training for static manipulation.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Author Contributions", "weight": 1.0} -->

Rohun Tripathi led MolmoBot single and multi-frame architecture and training, focusing on static manipulation.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Author Contributions", "weight": 1.0} -->

Jordi Salvador assisted with data scaling, infrastructure, and simulation evaluation.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Author Contributions", "weight": 1.0} -->

Max Argus assisted with simulation evaluations and benchmark creation.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Author Contributions", "weight": 1.0} -->

Matthew Wallingford led the ablation training and evaluation. Assisted with paper writing.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Author Contributions", "weight": 1.0} -->

Haoquan Fang contributed the base Molmo2+DiT architecture and the initial flow matching training pipeline.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Author Contributions", "weight": 1.0} -->

Wilbert Pumacay assisted with OOD simulation evaluation and additional benchmarks.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Author Contributions", "weight": 1.0} -->

Yejin Kim assisted with RB-Y1 real evaluation and data generation.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Author Contributions", "weight": 1.0} -->

Quinn Pfeifer, Ying-Chun Lee, Piper Wolters, Omar Rayyan, Mingtong Zhang, and Jiafei Duan assisted with simulation and real evaluation.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Author Contributions", "weight": 1.0} -->

Karen Farley managed the project.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Author Contributions", "weight": 1.0} -->

Winson Han and Eli Vanderbilt designed the figures in this report and helped with visualizations.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Author Contributions", "weight": 1.0} -->

Dieter Fox, Ali Farhadi and Georgia Chalvatzaki advised the project.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Author Contributions", "weight": 1.0} -->

Dhruv Shah and Ranjay Krishna were co-PIs for the project.
