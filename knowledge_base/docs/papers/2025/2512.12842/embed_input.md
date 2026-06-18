<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SAGA: Open-World Mobile Manipulation via Structured Affordance Grounding

Topics include Robotics, Foundation models, Few-shot learning, Generalization, Control, SAGA.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present SAGA, a versatile and adaptive framework for visuomotor control that can generalize across various environments, task objectives, and user specifications. To efficiently learn such capability, our key idea is to disentangle high-level semantic intent from low-level visuomotor control by explicitly grounding task objectives in the observed environment. Using an affordance-based task representation, we express diverse and complex behaviors in a unified, structured form. By leveraging multimodal foundation models, SAGA grounds the proposed task representation to the robot's visual observation as 3D affordance heatmaps, highlighting task-relevant entities while abstracting away spurious appearance variations that would hinder generalization. These grounded affordances enable us to effectively train a conditional policy on multi-task demonstration data for whole-body control. In a unified framework, SAGA can solve tasks specified in different forms, including language instructions, selected points, and example demonstrations, enabling both zero-shot execution and few-shot adaptation. We instantiate SAGA on a quadrupedal manipulator and conduct extensive experiments across eleven real-world tasks. SAGA consistently outperforms end-to-end and modular baselines by substantial margins.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Together, these results demonstrate that structured affordance grounding offers a scalable and effective pathway toward generalist mobile manipulation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Generalist robots need to seamlessly integrate semantic and geometric understanding to solve diverse and complex tasks in unstructured environments. In mobile manipulation \[khatib1999mobile, thakar2023survey\] in particular, performing a single task may require concurrent or sequential interactions with multiple objects of different affordances. An example is shown in Fig. 1, where a robot is tasked with retrieving snack bags from a shelf using a duster as a tool. During execution, the robot must select actions to achieve the task objectives while accounting for the geometry and configuration of surrounding objects. The difficulty is further compounded by the wide range of ways in which users specify task objectives, ranging from natural language to example trajectories, and the variations in how these specifications are expressed. Achieving such broad generalization across environments, objectives, and specifications remains a central challenge for modern robotic systems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent advances in multimodal foundation models \[achiam2023gpt, team2023gemini, radford2021clip\] have created unprecedented opportunities for open-world robotics. These models can perform strong visual recognition and semantic reasoning over an open set of concepts, yet still lack nuanced physical understanding required for control. To close the perception-action loop, end-to-end robot foundation models have been trained to directly fuse visual observations with high-level user specifications \[brohan2023rt, black2024pi_0\]. However, such models must implicitly learn to parse abstract concepts (e.g., "fluffy duster," "maroon stair"), ground them to raw sensory input, and generate control signals within a black-box model. As a result, their generalization capabilities depend on prohibitively large datasets that attempt to span the combinatorial diversity of real-world scenarios, often leading to sharp performance degradation when deployed outside their training distributions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Alternatively, modular frameworks adopt a more structured design, leveraging pre-trained multimodal foundation models for high-level reasoning, while resorting to hand-engineered modules for low-level execution \[huang2023voxposer, shen2023F3RM\]. Although more data-efficient, most of these frameworks are less robust in unstructured environments and often constrained to narrowly defined behaviors, such as grasping, limiting their application to sophisticated domains like mobile manipulation. Together, these limitations highlight the need for a new paradigm that can retain the open-world reasoning capabilities of foundation models while enabling robust, data-efficient visuomotor control in complex mobile manipulation settings.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we present Structured Affordance Grounding for Action (SAGA), a versatile and adaptable framework for open-world mobile manipulation. To enable broad generalization, our key insight is to disentangle high-level semantic intent from low-level visuomotor control by explicitly grounding task objectives in visual observations. As illustrated in Fig. 1, we express each task using a set of affordance--entity pairs that specify what to interact with and how the interaction should be performed. Leveraging multimodal foundation models \[achiam2023gpt, radford2021clip\], SAGA grounds this structured task representation into 3D space as affordance heatmaps. These grounded representations focus the downstream policy on desired behaviors in the context of relevant objects while abstracting away spurious semantic or visual variations that impede generalization, enabling data-efficient learning across a wide range of mobile manipulation tasks. Using the proposed task representation as a unified interface, SAGA supports visuomotor control specified in various forms, including instructions, points, and demonstrations, enabling both zero-shot execution and few-shot adaptation for diverse and complex tasks.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We instantiate SAGA on a quadrupedal mobile manipulation platform operating in cluttered real-world environments. Trained on multi-task demonstration trajectories, SAGA efficiently learns to solve diverse and complex mobile manipulation tasks without requiring extensive robot data. Across eleven real-world tasks evaluated in zero-shot and few-shot settings, SAGA exhibits strong generalization and consistently outperforms competitive baselines by substantial margins.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, the key contributions of this work are threefold. First, we introduce a structured, affordance-based task representation that unifies diverse task objectives and user specifications. Second, we propose a heatmap-conditioned visuomotor control algorithm that grounds task objectives in the 3D space, enabling data-efficient and robust policy learning on multi-task robot data. Finally, we instantiate and evaluate this framework on a quadrupedal manipulator, demonstrating strong generalization in unseen real-world tasks. Together, these contributions of SAGA advance the vision of open-world robotic control for mobile manipulation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We consider the problem of mobile manipulation in unstructured environments, where a robot is commanded to interact with objects based on the high-level user specification. The robot receives the observation composed of onboard RGB-D views and proprioceptive states, and produces the whole-body action that jointly controls torso and arm motion.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In this work, we allow the user specification to be given in one of three common forms: *Language* instructions offer the most general and expressive way to specify task objectives. *Point* inputs allow the user to designate relevant entities by selecting regions in the robot's visual observations, providing direct and precise guidance. *Demonstration* consists of one or a few example trajectories that illustrate the desired behavior when a text or spatial description is unavailable.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Our objective is to learn a policy $\pi$ that computes the action $a$ based on the observation $o$ and the user specification $u$. Following \[walke2023bridgedata, black2024pi_0\], we train this policy through imitation learning on real-world, multi-task demonstrations with annotated language instructions. At test time, the robot executes or adapts to novel tasks involving previously unseen environments, task objectives, and user specifications.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Method", "weight": 1.0} -->

We present Structured Affordance Grounding for Action (SAGA), a framework for versatile and adaptive mobile manipulation by grounding task objectives explicitly in the 3D space. Achieving this requires addressing several key challenges. First, how to represent task objectives in a structured form while covering diverse behaviors. Second, how to ground this representation into the robot's observations to decouple high-level semantics from low-level visuomotor control. Third, how to robustly generate actions conditioned on the grounded representation. Fourth, how to support tasks specified through diverse user inputs. Finally, how to deploy this framework on real mobile manipulation systems.

<!-- chunk {"id": "body-0014", "role": "body", "section": "IV-A Affordance-Entity Pairs as Task Representation", "weight": 1.0} -->

To support broad generalization across task objectives, we propose a structured task representation that effectively expresses diverse and complex physical interactions in a unified manner. We represent the objectives of each task using a set of affordance--entity pairs that specify what the robot should interact with and how the interaction should be conducted. For example, the sweeping task in Fig. 1 can be expressed as a dictionary {grasp: "duster handle", function: "duster head", indirect_contact: "snack", place: "woven basket", step_on: "maroon stair"}. In contrast to prior work \[shen2023F3RM, liu2024visual\] that focuses only on narrowly scoped skills, SAGA spans a set of affordance types beyond grasping, enabling flexible composition of multiple objectives within the same formulation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "IV-A Affordance-Entity Pairs as Task Representation", "weight": 1.0} -->

Formally, the set of affordance-entity pairs are encoded as ${\{{(w_{k},z_{k})}\}}_{k = 1}^{K}$, where $w_{k}$ is one of $K$ affordance types and $z_{k} \in {\mathbb{R}}^{M}$ is a $M$-dimensional entity embedding. Each embedding characterizes the semantic properties of the entity for identifying their location and spatial extent in the visual observation of the environment. These embeddings can be obtained from language or visual descriptions extracted from the user specification $u$ using a pretrained multimodal encoder $\psi{( \cdot )}$ \[radford2021clip\], which will be detailed Sec. IV-D. Embeddings are set to zero if the corresponding affordance is irrelevant for the task, ensuring a fixed-dimensional task representation.

<!-- chunk {"id": "body-0016", "role": "body", "section": "IV-A Affordance-Entity Pairs as Task Representation", "weight": 1.0} -->

While such affordance--entity pairs typically capture most essential task objectives, additional information might need to be specified for certain behaviors. For instance, a sweeping motion might require specifying not only the target entities but also a motion direction "from right to left". Thus, we augment $c$ with a motion embedding $z_{\text{motion}}$ computed using the motion information extracted from $u$. Since the affordance--entity pairs already encode the primary semantics, this motion embedding remains compact yet ensuring the expressiveness of $c$. As shown in Fig.

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-A Affordance-Entity Pairs as Task Representation", "weight": 1.0} -->

For long-horizon tasks with multiple stages, we follow \[huang2023voxposer, fangandliu2024moka\] to decompose the task into a sequence of subtasks $\lbrack c_{1},c_{2},\ldots\rbrack$, where each element is represented same as in Eq. 1.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-A Affordance-Entity Pairs as Task Representation", "weight": 1.0} -->

Now we have a unified, entity-centric representation that covers broad task objectives. Next, we explain how this representation enables generalizable visuomotor control through spatial grounding, while deferring how $c$ is computed from different user specifications to Sec. IV-D.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-B Structured Affordance Grounding", "weight": 1.0} -->

Robust visuomotor control requires grounding the task representation to the robot's observation. Although expressive, the entity embeddings in this representation often contain detailed semantic or visual information irrelevant to physical interaction, which can hinder generalization if supplied directly to the policy. For instance, variations in texture or phrasing (e.g., "yellow duster" vs. "fluffy cleaning tool") should not affect the intended motion, yet their latent embeddings can differ substantially. Instead of directly predicting actions based on the entity embeddings, we convert each of them into an affordance heatmap that marks the spatial information of the target entity for each affordance type. This grounding preserves the fine-grained structure of the task objectives while abstracting away nonessential semantics.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-B Structured Affordance Grounding", "weight": 1.0} -->

Inspired by \[shen2023F3RM, liu2024visual\], we compute the heatmap by encoding the visual observation into the same latent space with the entity embeddings and measuring their similarity. In contrast to focusing on grasping only, we compute a multi-channel heatmaps for a compositional set of affordance types. Given an RGB-D image in the observation $o$, we extract visual embedding ${\psi{(o)}} \in {\mathbb{R}}^{W \times H \times M}$ using the same pretrained multimodal encoder for producing the entity embeddings.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B Structured Affordance Grounding", "weight": 1.0} -->

where $h_{k}^{i}$ reflects how strongly pixel $i$ corresponds to the affordance associated with $w_{k}$. As shown in Fig. 2, stacking across $K$ affordance types yields a $W \times H \times K$ tensor as the heatmap, representing the grounded task semantics on the 2D visual observation of the environment.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B Structured Affordance Grounding", "weight": 1.0} -->

To tightly align the heatmap with the geometry of the environment, we lift the heatmap into 3D along with the point cloud $x$ computed from the depth channel from $o$. Each 3D point is thus associated with a $K$-dimensional affordance feature, forming a heatmap-informed point cloud $\lbrack x,h\rbrack$. This grounds task objectives to the environment in a structured manner for the downstream visuomotor control.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-C Heatmap-Conditioned Visuomotor Control", "weight": 1.0} -->

Unlike end-to-end policies that directly combine raw RGB images with high-level user specifications \[brohan2022rt, black2024pi_0\], the SAGA policy operates on the heatmap-informed point cloud. This design enables the policy to focus on the spatial and geometric information needed for physical interactions, leading to efficient generalization across diverse scenarios.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-C Heatmap-Conditioned Visuomotor Control", "weight": 1.0} -->

A major challenge for the policy is maintaining consistent grounding as the environment evolves. A straightforward design would recompute affordance heatmaps at every timestep $t$ from the latest observation $o_{t}$. However, this would require repeatedly running the heavy multimodal encoder and can often become brittle once objects self-occlude during execution. Instead, we compute the affordance heatmaps $h = h_{0}$ once from the initial observation $o_{0}$, which typically provides a clean and complete view of the scene. As the robot and objects move, the policy learns to implicitly align $o_{0}$ and $o_{t}$ through their shared point cloud structure, maintaining spatio-temporal correspondence without regenerating heatmaps.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-C Heatmap-Conditioned Visuomotor Control", "weight": 1.0} -->

Formally, the policy is denoted as $\pi{({a_{t:{{t + T} - 1}} \mid {c,o_{0},o_{t}}})}$, where a $T$-step action chunk \[chi2023diffusion\] is predicted at each timestep to ensure temporal consistency and mitigate compounding error. We instantiate $\pi$ as a conditional diffusion policy using a two-stream PointNet encoder \[qi2017pointnet\]. One stream embeds the heatmap-informed point cloud $\lbrack x_{0},h\rbrack$, capturing globally grounded task semantics. The other stream embeds the current point cloud $x_{t}$, capturing the local geometry required for real-time interaction. Their features are fused with the motion embedding contained in $c$ and the proprioceptive state to produce a latent representation encoding both what needs to be achieved and how the scene is changing.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-C Heatmap-Conditioned Visuomotor Control", "weight": 1.0} -->

A diffusion head is applied at the end to predict the $T$-step action chunk $a_{t:{{t + T} - 1}}$ to perform closed-loop control.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-C Heatmap-Conditioned Visuomotor Control", "weight": 1.0} -->

We train the policy through conditional imitation learning, which leverages multi-task demonstration data to efficiently align actions with diverse specifications. During training, an annotated multi-task dataset is provided as $\mathcal{D} = {\{\tau^{j}\}}_{j = 1}^{|\mathcal{D}|}$. Each trajectory $\tau^{j}$ in the dataset consists of the sequence of observations $o_{t}^{j}$ and actions $a_{t}^{j}$ as well as the task representation $c^{j}$, which is computed from annotated text descriptions. To reduce over-sensitivity to perception and specification variations, heatmap augmentation is applied during training by randomly rescaling and sharpening each channel of the computed heatmap. This encourages the policy to focus on spatial and semantic structures rather than exact heatmap magnitudes, mitigating brittleness to shifts in task phrasing, encoder error, or sensing noise.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-D Versatile Interfacing to User Specifications", "weight": 1.0} -->

A major advantage of SAGA is that its structured task representation serves as a unified, modality-agnostic interface for specifying user intent. As shown in Fig. 2, we employ the trained SAGA policy for the three common modalities of user specifications described in Sec. III, spanning both zero-shot execution (language, point) and few-shot adaptation (demonstration), to demonstrate its versatility.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-D Versatile Interfacing to User Specifications", "weight": 1.0} -->

Language. Following \[fangandliu2024moka\], we employ a VLM \[achiam2023gpt\] to decompose the instruction into a sequence of subtasks, and extract the text description for the motion and target entities. Using the multimodal encoder \[radford2021clip\], these texts are converted into entity embeddings and the motion embedding. By outsourcing high-level semantic reasoning and visual recognition to pretrained foundation models, SAGA can perform diverse and complex physical interactions for an open set of objects and task goals.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-D Versatile Interfacing to User Specifications", "weight": 1.0} -->

Point. Given the selected pixel location $p_{k}$ for each affordance type $w_{k}$, the corresponding visual embedding $\psi{(o_{0})}^{p_{k}}$ can naturally serve as the entity embedding $z_{k}$ for the specified affordance $w_{k}$. Note that the points need not be precisely specified on the exact position where the robot should grasp or contact the object, as different parts of the same object usually share similar embeddings for a well trained encoder. To further improve the robustness, we compute $z_{k}$ as the average over a local $3 \times 3$ window centered around $p_{k}$. This enables intuitive and convenient user interface without requiring language parsing or policy fine-tuning.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-D Versatile Interfacing to User Specifications", "weight": 1.0} -->

Because the mapping $c\rightarrow h\rightarrow a$ is fully differentiable, the optimization can be effectively conducted via backpropagation to embeddings in $c$, analogous to soft prompt tuning \[jia2022visual\]. This novel paradigm, which we refer to as *heatmap tuning*, enables few-shot adaptation without ground truth instructions while retaining the capabilities of the pre-trained policy.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-E Mobile Manipulation System Summary", "weight": 1.0} -->

SAGA is instantiated on a quadrupedal manipulator as illustrated in Fig. 2. We summarize the key components of this instantiation in details below.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-E Mobile Manipulation System Summary", "weight": 1.0} -->

Robot platform. We deploy SAGA on a Spot robot equipped with a 6-DoF arm and a parallel-jaw gripper \[bostondynamics_spot\]. One wrist-mounted and two forward-facing cameras provide multi-view RGB-D observations with known extrinsic and intrinsic parameters. The observation $o_{t}$ also includes a 19-dimensional proprioceptive state encoding torso pose, end-effector pose, and finger position. Following \[chi2023diffusion\], each $SE{}$ pose is represented as a 9-dimensional vector. The 21-dimensional action specifies 9-dimensional target poses for the torso and the end-effector, together with binary flags as defined in \[brohan2022rt\].

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-E Mobile Manipulation System Summary", "weight": 1.0} -->

Affordance types. Based on \[fangandliu2024moka\], we consider eight affordance types that span core mobile manipulation capabilities as described in Tab. I. These affordances can be combined either sequentially or concurrently to express complex objectives. For example, a task may require grasp a mug and place it on a rack while avoiding a laptop. Importantly, SAGA supports both under-specified and over-specified commands thanks to the expressiveness of the learned policy. For instance, a user may specify only grasp when the mug is distant, or additionally include walk to the table, with the trained policy resolving the ambiguity based on the environment context.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-E Mobile Manipulation System Summary", "weight": 1.0} -->

Model and training. To ensure spatial consistency across time, all observations and actions are expressed in the same frame, centered at the end-effector at $t$. At runtime, RGB-D streams from all cameras are independently converted to point clouds and affordance heatmaps then fused together. The fused cloud is cropped to a $2\text{m}$ workspace and uniformly downsampled to $N = 1024$ points for real-time inference. The policy network and pretraining follow \[ze20243d\], while few-shot adaptation optimizes only the task representation $c$ with an elevated learning rate of $1 \times 10^{- 3}$ to enable fast convergence.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

We conduct extensive experiments and analyses to evaluate the effectiveness of SAGA. Specifically, we aim to study the following questions: Q1: Does the proposed task representation effectively capture diverse task objectives and ground them reliably in the environment? Q2: How well does SAGA generalize to novel tasks and environments in zero-shot manners compared to state-of-the-art baselines? Q3: Can the unified task representation support different forms of user specification and enable fast adaptation?

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

Target region for placing the grasped object

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments", "weight": 1.0} -->

Functional part of the grasped object

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments", "weight": 1.0} -->

Scene entity directly contacted by the gripper

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiments", "weight": 1.0} -->

Scene entity contacted by the function entity

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experiments", "weight": 1.0} -->

Entity the robot must not contact or traverse

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experiments", "weight": 1.0} -->

Entity to approach and bring within gripper reach

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experiments", "weight": 1.0} -->

Entity for the robot to set foot on

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

We evaluate SAGA on real-world mobile manipulation tasks to assess its generalizability, robustness, and adaptability.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

Training data. As shown in Fig. 3, we collect 2,410 demonstration trajectories via teleoperation, covering a diverse set of behaviors with annotated affordances, including pulling a cart (grasp, walk_to), poking with a shovel (grasp, function, indirect_contact), closing a laptop (direct_contact), etc. Object instances, spatial configurations, and scene layouts are randomized across environments to promote broad generalization. Each trajectory contains up to 600 steps, resulting in approximately 1.3M state--action pairs in total. Notably, this dataset is two orders of magnitude smaller than those used by prior generalist robot policies \[black2024pi_0\], underscoring the substantially higher efficiency of our approach.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

Testing tasks. We construct testing environments resembling household, office, and retail spaces, each containing unseen furniture and object instances. Across these environments, we define three long-horizon tasks, each decomposed into three sequential sub-tasks, yielding nine evaluation tasks as shown in Tab. II. Each task is indexed as $i$--$j$, where $i$ denotes the scenario and $j$ the sub-task. To assess heatmap-tuning, we additionally design two tasks requiring object-level and task-level adaptations as described in Sec. V-C.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

Push a basket beside the table using the gripper

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

Sweep a snack into the basket with a brush

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

Approach the shelf and step onto the stair

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

Pick horizontally from shelf and place in basket

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

Lift up the shopping basket from the ground

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

Walk to an object and place it into the open drawer

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

Pick up an object and put it into the open drawer

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

Close the open drawer with the gripper

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

Baselines. We compare SAGA with four baseline methods. DP3 \[ze20243d\] is a diffusion policy originally designed for task-specific training. We convert it to a multi-task policy using the embedding of the language instruction computed by \[radford2021clip\] as the task representation. CodeDiffuser \[yin2025codediffuser\] explicitly extracts entity descriptions from the original language instruction using a VLM and uses binary masks to exclude distractor objects from the input point clouds. $\pi_{0}$ \[black2024pi_0\] trains a VLA model end-to-end based on the input RGB images and langauge instructions. We further include depth images to its inputs for fair comparison and fine-tune the model on our collected dataset. For few-shot adaptation, we additionally compare with SKIL \[wang2025skil\], which adapts to new tasks using learned keypoint representations. CodeDiffuser is excluded from few-shot adaptation and SKIL from zero-shot execution, as their formulations do not directly support those settings. All methods are trained and evaluated following the same protocols for fair comparison.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-B Zero-Shot Execution", "weight": 1.0} -->

We first evaluate all methods conditioned on natural language instructions and additionally evaluate a variant of our method using the point specifications. We denote our model variants as SAGA-Language and SAGA-Point. The average success rates across 10 trials are reported in Fig. 5. Both SAGA variants achieve high success rates across all tasks. Even in tasks composing multiple affordance types (e.g., sweeping with previously unseen tools), SAGA maintains strong performance. Moreover, given the same affordance types (e.g., grasp and place), the trained policy can behave differently in accordance with different environment contexts, performing top-down, horizontal, or mobile grasping respectively. Between the two variants, SAGA-Point achieves modestly higher success rates, as a selected point directly identifies the region of interest and resolve semantic ambiguity, which is particularly helpful when multiple objects share similar semantics.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-B Zero-Shot Execution", "weight": 1.0} -->

In contrast, baselines lacking structured task representations exhibit systematic failure patterns. DP3 and CodeDiffuser frequently mislocalize the target objects, leading to unstable grasps and incorrect contacts. While CodeDiffuser uses a VLM to segment target objects, its binary mask representation combines all target objects together without distinguishing how each object should be interacted, resulting in ambiguous intents. Despite extensive pretraining, the end-to-end trained $\pi_{0}$ does not effectively adapt to the quadrupedal manipulator, which is unseen in its pre-training dataset, due to its massive model size and the relatively small fine-tuning data (less than 0.2% of the original dataset). Consequently, its output actions exhibit mode collapse, only occasionally succeeding on less complex tasks (e.g., Push, Close). These results highlight the advantages of structured affordance grounding for efficiently learning robust mobile manipulation in open-world settings.

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-C Few-Shot Adaptation", "weight": 1.0} -->

We next evaluate whether SAGA can adapt to novel tasks using only 10 demonstrations via the heatmap-tuning procedure introduced in Sec. IV-D. We consider two representative settings: (i) object-level adaptation (sort vegetable), where an in-distribution affordance set (e.g., grasp, place) is applied to previously unseen objects, and (ii) task-level adaptation (clean-avoid), where the robot is asked to solve the task specified by a novel combination of affordance types (grasp, avoid, and indirect_contact) unseen during policy training.

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-C Few-Shot Adaptation", "weight": 1.0} -->

We evaluate SAGA and baselines in few-shot manners without language instructions, as well as a zero-shot variant of SAGA given ground-truth instructions. As shown in Fig. 6, SAGA achieves reasonable zero-shot successes and rapidly improves success rates through heatmap tuning, reaching stable and reliable execution with only ten demonstrations. By optimizing the task representation while keeping the visuomotor policy frozen, the adapted task representations highlight the relevant affordance regions on the point cloud, leading to affordance heatmaps of the quality comparable to ground truth heatmaps computed from instructions and points, as shown in Fig. 7. In contrast, all baselines perform poorly in zero-shot and struggle to adapt effectively. DP3 and SKIL can sometimes approach and grasp objects but exhibit unstable trajectories, leading to inconsistent performance and frequent task failure.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

We presented SAGA, a unified framework for open-world mobile manipulation that explicitly grounds task objectives in 3D geometry. By representing tasks as affordance--entity pairs and mapping them into affordance heatmaps, SAGA decouples high-level semantic reasoning from low-level visuomotor control. This structured grounding enables a single conditional policy to robustly perform diverse tasks across varying environments and objectives. Moreover, the proposed task representation serves as a modality-agnostic interface, allowing the trained policy to be conditioned from language instructions, mouse clicks, or example demonstrations. Extensive real-world evaluations on a quadrupedal manipulator demonstrate strong generalization, robust task execution, and rapid adaptation, significantly outperforming prior end-to-end and modular baselines. These results highlight the promise of spatially grounded task representations for scalable and generalizable robot learning in the real world.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

Despite these advances, several limitations suggest promising directions for future work. First, the current affordance vocabulary, while expressive for a wide range of tasks, remains tailored to single-arm mobile manipulation. Extending to bimanual, dexterous, or humanoid systems will likely require designing or learning affordance types that capture richer interaction semantics. Second, while prioritizing spatially grounded affordances and object geometry significantly improves robustness and generalization, complex tasks involving deformable objects or nuanced material properties may benefit from incorporating compact visual cues to complement the affordance-informed point cloud within a unified representation. Finally, advances in multimodal encoders and correspondence estimation may enable more reliable online updating of affordance grounding during execution, further improving performance in dynamic and partially observed environments.
