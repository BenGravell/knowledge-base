<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Human2Any: Human-to-Robot Transfer via Constraint-Aware Compositional Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Human videos are a scalable source of supervision for robot manipulation, as they are abundant and naturally capture rich object interactions. However, transferring human demonstrations to robots remains challenging due to embodiment mismatch, scene variation, and robot-specific feasibility constraints. We present Human2Any, a framework for learning reusable object-centric interaction priors from human videos without requiring real-world robot demonstrations in the target task contexts. Human2Any represents manipulation through object-object interaction motion, capturing task-relevant scene changes while abstracting away embodiment-specific details. It composes learned interaction priors with robot-side feasibility reasoning and motion planning, allowing the same human-derived knowledge to adapt to different embodiments, scene geometries, and task contexts. We validate Human2Any across diverse manipulation settings, including real-world experiments on a Franka tabletop setup and an RBY-1 humanoid mobile robot, demonstrating robust interaction-centric manipulation without real-world robot training data.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Learning manipulation systems that can generate feasible and purposeful motions for solving everyday tasks remains a fundamental yet challenging problem. While behavior cloning (BC) has achieved remarkable progress in recent years, its generalization to diverse environments---such as varying object geometries, poses, and scene layouts---heavily depends on both the quality and quantity of training data. Unfortunately, the collection of high-quality, embodiment-aligned demonstrations, typically obtained through robot teleoperation, is time-consuming and costly, which significantly limits scalability.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, *learning from human videos* has emerged as a promising paradigm for teaching robots at scale. Unlike robot demonstrations, human videos are abundant and diverse, but their most transferable signal is not the human body motion itself; rather, it is the *object-centric interaction structure* underlying the task. Human videos capture rich manipulation strategies: they show how objects change state *because of* purposeful interactions---reach, grasp, insert, pour---across long horizons and varied objects, layouts, and styles. This diversity is ideal for learning *compositional* skills, but directly imitating human motion is mismatched to robot embodiment. Trajectory-level reproducibility is inherently context-dependent: a motion that works in one scene may be infeasible on the robot due to reachability, joint limits, or collisions. As the layout changes, previously infeasible motions may become feasible, and vice versa. Thus, the key is not to copy a particular trajectory, but to extract structure that remains stable across embodiments and contexts.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This raises a central challenge: *how can we harness the breadth of human videos to learn transferable interaction models that can be adapted to robot-specific constraints?* We tackle this problem through the lens of object-centric motion generation. Our key insight is that what transfers is the *interaction structure*: which objects participate, when contacts form and break, and how object states evolve. Accordingly, we represent the manipulation process as a factor graph that explicitly disentangles agent--object and object--object interactions (Fig. 1). The object--object factors capture agent-agnostic motion distributions learned from human videos, while the agent--object factors and feasibility terms account for embodiment-specific constraints such as grasping, reachability, and collision avoidance. At test time, we sample and refine graph variables under the robot's in-context constraints to produce robot-feasible interaction sequences that preserve the goal-achieving structure observed in video. This formulation scales the acquisition of diverse object-centric motion models while retaining structure-aware adaptability across embodiments and task scenarios, unifying compositional reasoning and constraint satisfaction within a sampling-and-scoring procedure.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our main contributions are summarized as follows: $\bullet$ We formulate manipulation as an object-centric factor graph that separates human-transferable object--object interaction factors from robot-specific agent--object feasibility factors, enabling motion learning from human videos with test-time robot adaptation. $\bullet$ We represent skills as compositions of object-centric motion models and develop a foundation-model-based pipeline to extract object motions from unstructured human videos. $\bullet$ We introduce a constraint-aware sampler that scores and resamples candidate motion compositions under in-context constraints to produce robot-feasible motions. $\bullet$ We validate the approach across multiple robot embodiments and long-horizon tasks, demonstrating generalization, cross-embodiment adaptability, and planning efficiency.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Learning Interaction Priors from Video", "weight": 1.0} -->

Human videos provide rich object-interaction demonstrations, but their motions are not directly executable by robots due to embodiment mismatch and scene-dependent constraints. We treat each video as a tool object interacting with a target object, e.g., a cup tilting toward a bowl or a utensil being placed on a bowl, and extract object geometry and relative object motion while discarding human-specific arm and hand motion. As shown in Fig. 2, Human2Any learns object--object interaction priors from human videos and robot-specific agent--object priors from embodiment-specific grasp data, then composes them with robot- and scene-specific feasibility reasoning at deployment.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Learning Interaction Priors from Video", "weight": 1.0} -->

Interaction-Centric Task Representation. We consider tasks specified by a high-level skeleton $\mathcal{S}=[s^{1},\ldots,s^{K}]$, where each phase $s^{k}=\langle a^{k},\mathcal{O}^{k}\rangle$ denotes an interaction type $a^{k}$ and the involved objects $\mathcal{O}^{k}$. There are three interaction types: free-space motion, agent--object interaction, and object--object interaction. Free-space motion connects interaction phases; agent--object interaction establishes robot-specific contact with a tool object; and object--object interaction describes how a tool object moves relative to a target object.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Learning Interaction Priors from Video", "weight": 1.0} -->

The key transferable representation is the object--object interaction trajectory $\tau^{\mathrm{rel}}=\{\mathbf{T}^{\mathrm{rel}}(h)\}_{h=0}^{H-1}$, where $\mathbf{T}^{\mathrm{rel}}(h)\in\mathrm{SE}$ denotes the tool-object pose relative to the target object at time $h$. This representation captures task-relevant interaction motion while removing the human embodiment from the supervision signal. In this work, we focus on prehensile manipulation, where the robot maintains a rigid attachment to the tool object during interaction. This allows robot execution to be recovered from object--object interaction motion and a grasp pose.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Learning Interaction Priors from Video", "weight": 1.0} -->

Object--Object Priors from Human Videos. For each processed demonstration, we assume access to the tool and target object point clouds $\mathbf{P}^{A},\mathbf{P}^{B}\in\mathbb{R}^{N\times 3}$ and the corresponding object-centric relative trajectory $\tau^{\mathrm{rel}}=\{\mathbf{T}^{\mathrm{rel}}_{h}\}_{h=0}^{H-1}$. In our implementation, these are estimated from RGB-D videos using off-the-shelf segmentation and tracking tools; details are provided in the appendix. Given tracked 3D keypoints $\xi^{3d}\in\mathbb{R}^{H\times M\times 3}$, we estimate $\tau^{\mathrm{rel}}$ using the Kabsch algorithm with RANSAC.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Learning Interaction Priors from Video", "weight": 1.0} -->

We trim each trajectory to frames near the interaction segment using a task-dependent distance threshold from the final interaction pose, approximately $0.15$--$0.2$ m across tasks. This yields $\mathcal{D}_{\mathrm{os}}=\{(\mathbf{P}^{A}_{i},\mathbf{P}^{B}_{i},\tau^{\mathrm{rel}}_{i})\}_{i=1}^{|\mathcal{D}_{\mathrm{os}}|}$ for training object--object interaction samplers.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Learning Interaction Priors from Video", "weight": 1.0} -->

Robot-Specific Agent--Object Priors. Object--object priors specify how objects should interact, but the robot must still choose an embodiment-specific way to grasp and control the tool object. We therefore train an agent--object prior for each robot embodiment using simulated grasp data. Each sample contains a tool-object point cloud $\mathbf{P}^{A}$ and a robot end-effector trajectory $\tau^{e}$ for reaching and grasping the object, forming $\mathcal{D}_{\mathrm{ro}}=\{(\mathbf{P}^{A}_{i},\tau^{e}_{i})\}_{i=1}^{|\mathcal{D}_{\mathrm{ro}}|}$. The resulting prior $p_{\theta_{\mathrm{ro}}}(\tau^{e}\mid\mathbf{P}^{A})$ captures embodiment-specific grasping behavior while remaining separate from the object--object interaction prior.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Learning Interaction Priors from Video", "weight": 1.0} -->

This separation allows object-level interaction knowledge learned from human videos to be reused across different robot embodiments, while robot-specific execution is handled through the agent--object prior and test-time feasibility reasoning.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Learning Interaction Priors from Video", "weight": 1.0} -->

Diffusion Trajectory Prior Training. We instantiate object--object and agent--object priors as conditional diffusion models over pose trajectories. Given a clean trajectory $\mathbf{x}_{0}$, the forward process generates noisy samples $\mathbf{x}_{t}=\sqrt{\bar{\alpha}_{t}}\mathbf{x}_{0}+\sqrt{1-\bar{\alpha}_{t}}\boldsymbol{\epsilon}$, where $\boldsymbol{\epsilon}\sim\mathcal{N}(\mathbf{0},\mathbf{I})$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Learning Interaction Priors from Video", "weight": 1.0} -->

The model predicts the injected noise by minimizing $\mathcal{L}(\theta)=\mathbb{E}_{t,\mathbf{x}_{0},\boldsymbol{\epsilon}}[\|\boldsymbol{\epsilon}-\boldsymbol{\epsilon}_{\theta}(\mathbf{x}_{t},t,\tilde{c})\|_{2}^{2}]$, where $\tilde{c}$ denotes the corresponding point-cloud conditioning input. For object--object priors, $\tilde{c}=(\mathbf{P}^{A},\mathbf{P}^{B})$; for agent--object priors, $\tilde{c}=\mathbf{P}^{A}$. We apply rigid transformations to both point clouds and trajectories during training to improve robustness to object poses and scene layouts. Additional details are provided in the Appendix.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Constraint-Aware Composition", "weight": 1.0} -->

At deployment, the robot observes a context $c$ containing the robot model, scene point cloud, and task skeleton. Each learned prior can generate diverse candidate motion segments, but independently plausible segments may not compose into an executable robot trajectory. We therefore formulate test-time execution as constraint-aware composition: jointly selecting motion segments that remain likely under the learned priors while satisfying robot- and scene-specific constraints.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Test-Time Context and Trajectory Assembly", "weight": 1.0} -->

Let $\mathbf{x}^{1:K}=\{\mathbf{x}^{1},\ldots,\mathbf{x}^{K}\}$ denote sampled motion segments for the $K$ phases in the task skeleton. We define an assembly operator $\Gamma(\mathbf{x}^{1:K},c)$ that converts these segments into a full robot trajectory and evaluates feasibility under the current context. For agent--object segments, $\Gamma$ directly uses the sampled end-effector trajectory. For object--object segments, $\Gamma$ converts the sampled relative object trajectory into end-effector targets using the grasp transform provided by the preceding agent--object segment. Under the rigid grasp assumption, this conversion is $\mathbf{T}^{e}(h)=\mathbf{T}^{\mathrm{rel}}(h)\mathbf{T}^{e}$, where $\mathbf{T}^{e}$ is the end-effector pose after grasping the tool object.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Test-Time Context and Trajectory Assembly", "weight": 1.0} -->

The assembled trajectory is then checked for kinematic feasibility, collision avoidance, and task-specific constraints between segments.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Test-Time Context and Trajectory Assembly", "weight": 1.0} -->

This feasibility depends on both the robot embodiment and the current scene. For example, in PourInBowl, a sampled cup-to-bowl trajectory may be plausible at the object level but infeasible if the wrist collides with nearby obstacles or the pouring pose lies outside the robot workspace. Another candidate with a different grasp or pouring direction may remain feasible. Thus, object--object priors alone are insufficient; sampled interactions must be composed with robot- and scene-specific constraints at test time.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Test-Time Context and Trajectory Assembly", "weight": 1.0} -->

Composition by Rejection Sampling. A natural composition strategy is to sample each segment independently from its learned prior and accept the composition only if $\Gamma(\mathbf{x}^{1:K},c)$ is executable. Let $\mathcal{E}$ denote the event that the assembled trajectory satisfies all constraints, and let $q(c)=\Pr(\mathcal{E}=1\mid c)$ be the feasible mass under this independent proposal. The expected number of trials is $\mathbb{E}[N_{\mathrm{trial}}]=1/q(c)$. This strategy becomes inefficient when feasible compositions occupy only a small region of the joint sample space, which often occurs under tight grasp, kinematic, and collision constraints.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Constraint-Aware Steering", "weight": 1.0} -->

Fig. 3 illustrates why independent sampling can be inefficient. Each sampler assigns high probability to locally plausible samples, shown as the two circles, but only a small subset of their joint combinations satisfies the global composition constraint, such as being parallel to a reference direction. Rejection sampling checks feasibility only after complete samples are generated, wasting computation on incompatible combinations. In contrast, our method guides generation toward feasible compositions during denoising.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Constraint-Aware Steering", "weight": 1.0} -->

The feasibility likelihood is $p(\mathcal{E}=1\mid\mathbf{x}^{1:K},c)\propto\exp(\beta\mathcal{S}(\Gamma(\mathbf{x}^{1:K},c),c))$, where $\mathcal{S}$ scores the assembled trajectory under the current in-context constraints, and $\beta$ controls the strength of steering.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Constraint-Aware Steering", "weight": 1.0} -->

The denoised segment estimates are assembled by $\Gamma$ and scored with weights $w_{t,i}\propto\exp(\beta\mathcal{S}(\Gamma(\hat{\mathbf{x}}^{\,1:K}_{0,i},c),c))$. Particles are resampled according to these weights before the next reverse-diffusion step.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Constraint-Aware Steering", "weight": 1.0} -->

The score $\mathcal{S}$ is soft rather than binary: it can incorporate continuous measures such as IK residuals, collision margins, and motion-planning feasibility. Therefore, particles need not be fully executable at early denoising steps; steering gradually reallocates computation toward particles whose denoised estimates are closer to satisfying the constraints. The full procedure is provided in the Appendix.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

We implement $\Gamma$ using MPlib to synthesize free-space motions and verify kinematic and collision constraints directly on observed scene point clouds, avoiding the need for explicit object mesh models during planning. Once a feasible trajectory is found, we execute it with platform-specific controllers: OSC at $20\,\mathrm{Hz}$ for Franka end-effector targets, and joint-position control for the RBY-1 torso, arms, and dexterous hands, with PD control for mobile-base tracking. Camera, perception, and additional planning details are provided in the appendix.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experiments", "weight": 1.0} -->

Our experiments evaluate whether Human2Any enables scalable and transferable manipulation learning from object-centric interaction motion. Specifically, we test six hypotheses. H1: Human2Any can acquire challenging manipulation skills without embodiment-aligned robot data. H2: Human2Any generalizes to new task contexts without in-context data. H3: Human2Any can execute real-world manipulation tasks without real-world robot training data. H4: Human2Any transfers across substantially different robot embodiments. H5: Constraint-aware steering is critical for efficient and feasible composition. H6: Human2Any benefits from scaled interaction-motion data.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experimental Setup and Baselines", "weight": 1.0} -->

Simulation tasks. We design three MuJoCo-based domains from MimicLab: PourInBowl, HangMugTree, and PrepareTable (Fig. 4, top). These tasks evaluate fine-grained motion, long-horizon control, and compositional generalization. Each domain includes three variants with distinct layouts, object arrangements, and interaction contexts. Within each variant, objects are further randomized by approximately $0.1$ m translation and $30^{\circ}$ rotation. We train on two variants and reserve the third for OOD evaluation. Detailed task descriptions are provided in the appendix.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experimental Setup and Baselines", "weight": 1.0} -->

Real-world tasks. We evaluate real-world execution without real-world robot training data on two distinct platforms: a Franka tabletop setup and an RBY-1 humanoid with dexterous hands (Fig. 4, bottom). For Franka, we use PourInBowl, HangMugTree, and SortUtensils; for RBY-1, we use PourCup and UseRoller. We run ten trials per task with varied object shapes and randomized poses to test robustness across real-world configurations.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experimental Setup and Baselines", "weight": 1.0} -->

Baselines. We compare against DP3, an in-domain behavior cloning policy trained with 100 robot demonstrations per task in simulation and 50 real-robot demonstrations per task in real-world experiments; Im2Flow2Act, which predicts 2D object flow from human videos and translates it into robot actions using simulation data; and a Rejection Sampling ablation that uses the same learned components as Human2Any but disables steering.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Main Results: Zero-Shot Composition and Generalization", "weight": 1.0} -->

We first evaluate Human2Any on the simulation benchmark in Tab. 1, testing challenging skill acquisition without embodiment-aligned robot demonstrations (H1), generalization to new task contexts without in-context data (H2), and the benefit of constraint-aware steering (H5). Each domain contains two in-distribution variants (S1--S2) and one OOD variant with substantially different scene layouts, object arrangements, and interaction contexts.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Main Results: Zero-Shot Composition and Generalization", "weight": 1.0} -->

Reject Sampling (No Steering) Table 1: Simulation benchmark results. Success rate comparison across three manipulation tasks under in-distribution (ID; S1–S2) and out-of-distribution (OOD) settings. ID and OOD report average success rates over the corresponding settings.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Main Results: Zero-Shot Composition and Generalization", "weight": 1.0} -->

Human2Any solves challenging tasks without embodiment-aligned data. Across the three domains, Human2Any achieves the strongest overall performance. DP3 performs substantially worse despite using 100 robot demonstrations per task, suggesting that direct action regression struggles with diverse object shapes, poses, layouts, and long-horizon error accumulation. Im2Flow2Act also underperforms, indicating that flow-based action translation does not sufficiently capture embodiment feasibility and 3D scene constraints. These results support H1.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Main Results: Zero-Shot Composition and Generalization", "weight": 1.0} -->

Human2Any generalizes to new contexts without in-context data. On OOD variants with unseen layouts and object arrangements, Human2Any maintains strong performance and outperforms baselines across all domains. This suggests that object--object interaction motion decouples task-relevant interaction structure from specific training layouts, enabling generalization to new poses, shapes, and scene contexts. These results support H2.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Main Results: Zero-Shot Composition and Generalization", "weight": 1.0} -->

Constraint-aware steering improves feasible composition. Compared with Rejection Sampling, which uses the same learned components but disables steering, Human2Any achieves more consistent performance and stronger OOD generalization. Thus, jointly steering generation with in-context constraints is more effective than independently sampling and filtering candidates, supporting H5.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Real-world Evaluation", "weight": 1.0} -->

We further evaluate Human2Any on real robot platforms to test whether human-derived interaction priors can be deployed without real-world robot data in the target task contexts (H3) and transferred across substantially different embodiments (H4). Additional snapshots and videos are provided in the appendix and supplementary material.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Real-world Evaluation", "weight": 1.0} -->

Human2Any solves real-world tasks without real-world robot data. On the Franka tabletop setup, we evaluate Human2Any on PourInBowl, HangMugTree, and SortUtensils (Tab. 2). These tasks require precise object interactions, grasp-conditioned execution, and robustness to variation in object shape and state. Across ten trials per task, Human2Any executes the learned interaction motions in real scenes without real-world robot demonstrations, supporting H3.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Real-world Evaluation", "weight": 1.0} -->

Human2Any transfers across diverse robot embodiments. We further deploy Human2Any on the RBY-1 humanoid mobile robot for PourCup and UseRoller. Compared with the Franka setup, RBY-1 has substantially different kinematics. Human2Any achieves success rates of $0.6$ and $0.7$ on the two tasks, respectively, showing that the learned interaction priors are not tied to a specific robot morphology. By resolving embodiment-specific constraints at test time, Human2Any adapts the same object--object interaction knowledge across diverse robot platforms, supporting H4.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Ablation Study: Dissecting Key Components", "weight": 1.0} -->

Steering improves generation quality and efficiency. (H5) As shown in Fig. 5(a), steering reallocates particles from low-feasibility regions toward samples that better satisfy grasp, kinematic, collision, and scene constraints during denoising. Qualitative snapshots show assemblies becoming increasingly feasible, with high-quality samples in green and low-quality samples in red. At the task level, Human2Any achieves the highest throughput across all simulation domains, measured as successful trials within a one-hour budget including inference, planning, and execution (Fig. 5(b)). This shows that steering improves both motion quality and sampling efficiency by reducing computation spent on infeasible candidates.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Ablation Study: Dissecting Key Components", "weight": 1.0} -->

Performance improves with interaction-motion data scale. (H6) We study data scaling on PourInBowl by varying the quantity and diversity of object-centric interaction trajectories (Fig. 5(b)). Performance improves with richer motion data, suggesting that Human2Any can effectively leverage diverse interaction supervision. Since these trajectories share the same form as motion extracted from human videos, this provides indirect evidence for scalability with larger human-video sources.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Limitations", "weight": 1.5} -->

Human2Any focuses on prehensile manipulation and assumes a rigid attachment between the end-effector and tool object, allowing robot control targets to be recovered from a fixed grasp pose and object--object interaction motion. Relaxing this assumption with learned dynamics models could enable broader non-prehensile skills such as in-hand dexterous manipulation. Human2Any assumes that the task skeleton is provided; integrating it with task planning or language-guided decomposition would yield a more complete task-and-motion planning system. The current implementation lacks online failure detection and replanning, which would improve robustness under perception noise, object slippage, and unexpected scene changes, especially in long-horizon execution.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented Human2Any, a framework for transferring interaction-centric manipulation knowledge from human videos to robots without real-world robot demonstrations. By representing manipulation as object-centric motion, Human2Any separates embodiment-agnostic interaction learning from robot-specific execution through in-context feasibility reasoning and motion planning. Experiments in simulation and on real Franka and RBY-1 platforms show that Human2Any can solve fine-grained and long-horizon tasks while generalizing across object shapes, scene layouts, and robot embodiments.
