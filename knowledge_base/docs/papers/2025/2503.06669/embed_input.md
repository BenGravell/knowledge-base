<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

AgiBot World Colosseo: A Large-Scale Manipulation Platform for Scalable and Intelligent Embodied Systems

Topics include Robot manipulation, Datasets, Vision-language-action models, Generalist robot policies, Dexterous manipulation, Scalable robot data.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces AgiBot World Colosseo, a large-scale manipulation dataset and platform, together with the GO-1 generalist policy trained on its trajectories. The paper is primarily a data-scaling and infrastructure contribution for embodied manipulation, with policy results showing how latent action representations can exploit the dataset.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We explore how scalable robot data can address real-world challenges for generalized robotic manipulation. Introducing AgiBot World, a large-scale platform comprising over 1 million trajectories across 217 tasks in five deployment scenarios, we achieve an order-of-magnitude increase in data scale compared to existing datasets. Accelerated by a standardized collection pipeline with human-in-the-loop verification, AgiBot World guarantees high-quality and diverse data distribution. It is extensible from grippers to dexterous hands and visuo-tactile sensors for fine-grained skill acquisition. Building on top of data, we introduce Genie Operator-1 (GO-1), a novel generalist policy that leverages latent action representations to maximize data utilization, demonstrating predictable performance scaling with increased data volume. Policies pre-trained on our dataset achieve an average performance improvement of 30% over those trained on Open X-Embodiment, both in in-domain and out-of-distribution scenarios. GO-1 exhibits exceptional capability in real-world dexterous and long-horizon tasks, achieving over 60% success rate on complex tasks and outperforming prior RDT approach by 32%.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

By open-sourcing the dataset, tools, and models, we aim to democratize access to large-scale, high-quality robot data, advancing the pursuit of scalable and general-purpose intelligence.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Manipulation is a cornerstone task in robotics, enabling the agent to interact with and adapt to the physical world. While significant progress has been made in general-purpose foundational models for natural language processing and computer vision, robotics lags behind due to the difficulty of (high-quality) data collection. In the controlled lab setting, simple tasks such as pick-and-place have been well studied. Yet for the open-set real-world setting, tasks spanning from fine-grained object interaction, mobile manipulation to collaborative tasks, remains a formidable challenge. These tasks require not only physical dexterity but also the ability to generalize across diverse environment and scenarios, a merit beyond the reach of current robotic systems. The widely accepted reason is the lack of high-quality data---unlike images and text, which are abundant and standardized, robotic datasets suffer from fragmented clips due to heterogeneous hardware and unstandardized collection procedure, leading to low-quality and inconsistent outcome. In this work we ask, how could we resolve the real-world complexity effectively by scaling up real-world robot data?

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent efforts, such as Open X-Embodiment (OXE), have addressed by aggregating and standardizing existing datasets. Despite advancements on large-scale cross-embodiment learning, the resulting policy is constrained within naive, short-horizon tasks and can weakly generalize to out-of-domain scenarios. DROID collected expert data through crowd-sourcing from diverse real-life scenes. The absence of data quality assurance (with human feedback) and the reliance on a constrained hardware setup (i.e., featuring fixed, single-arm robots), limit its real-world applicability and broader effectiveness. More recently, Lin et al. explored scaling laws governing generalizability across intra-category objects and environments, albeit limited to a few simple, single-step tasks. These efforts represent a notable advancement toward developing generalist policies, moving beyond the traditional focus on single-task learning within narrow domains. Nevertheless, existing robot learning datasets remain constrained by their reliance on short-horizon tasks in highly controlled laboratory environments, failing to adequately capture the complexity and diversity inherent in real-world manipulation tasks.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To achieve general-purpose robotic intelligence, it is essential to develop datasets that scale in size and diversity while capturing real-world variability, supported by general-purpose humanoid robots for robust skill acquisition, a standardized data collection pipeline with assured quality, and carefully curated tasks reflecting real-world challenges.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

As depicted in Fig. 1, we introduce AgiBot World Colosseo, a full-stack large-scale robot learning platform curated for advancing bimanual manipulation in scalable and intelligent embodied systems. A full-scale 4000-square-meter facility is constructed to represent five major domains---domestic, retail, industrial, restaurant, and office environment---all dedicated to high-fidelity data collection in authentic everyday scenarios. With over 1 million trajectories collected from 100 real robots, AgiBot World offers unprecedented diversity and complexity. It spans over 100 real-world scenarios, addressing challenging tasks such as fine-grained manipulation, tool usage, and multi-robot synergistic collaboration. Unlike prior datasets, AgiBot World dataset collection is carried out with a fully standardized pipeline, ensuring high data quality and scalability, while incorporating human-in-the-loop verification to guarantee reliability. Our hardware setup includes mobile base humanoid robots with whole-body control, dexterous hands, and visuo-tactile sensors, enabling rich, multimodal data collection.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Each episode is meticulously designed, featuring multiple camera views, depth information, camera calibration, and language annotations for both the overall task and each individual sub-steps. This well-rounded hardware setup, combined with various long-horizon, real-world tasks, opens new avenues for developing next-generation generalist policies and fosters diverse future research in robotics.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our experimental results highlight the transformative potential of the AgiBot World dataset. Policies pre-trained on our dataset achieve an average success rate improvement of 30% compared to those trained on the prior large-scale robot dataset OXE. Notably, even when utilizing only a fraction of our dataset---equivalent to 1/10 of the data volume in hours compared to OXE---the generalizability of pretrained policies is elevated by 18%. These findings underscore the dataset's efficacy in bridging the gap between controlled laboratory environments and real-world robotic applications. Following our dataset, to address the limitations of previous robot foundation models that heavily rely on in-domain robot datasets, we present Genie Operator-1 (GO-1), a novel generalist policy that utilizes latent action representations to enable learning from heterogeneous data and efficiently bridges general-purpose vision-language models (VLMs) with robotic sequential decision-making.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Through unified pre-training on web-scale data, spanning human videos to our high-quality robot dataset, GO-1 achieves superior generalization and dexterity, outperforming prior generalist policies such as RDT and our variant without latent action planner. Moreover, we demonstrate that GO-1's performance exhibits robust scalability with increasing dataset size, underscoring its potential for sustained advancement as larger datasets become available.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Beyond its immediate impact, AgiBot World lays a strong foundation for future research in robotic manipulation. By open-sourcing the dataset, toolchain, and pre-trained models, we aim to foster community-wide innovation, enabling researchers to explore more authentic and diverse applications from household assistant to industrial automation. AgiBot World is more than yet another dataset; it is a step toward scalable, general-purpose robotic intelligence, empowering robots to tackle the complexities of the real world.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contribution. 1) We construct AgiBot World dataset, a multifarious robot learning dataset accompanied by open-source tools to advance research on policy learning at scale. As a pioneering initiative, AgiBot World employs an inclusive optimized pipeline, from scene configuration, task design, data collection, to human-in-the-loop verification, which ensures unparalleled data quality. 2) We propose GO-1, a robot foundation policy using latent action representations to unlock web-scale pre-training on web data. Empowered by AgiBot World dataset, it outperforms prior generalist policies in generalization and dexterity.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Limitation. All evaluations are conducted in real-world scenarios. We are currently developing the simulation environment, aligning with the real-world setup and aiming to reflect real-world policy deployment outcome. It would thereby facilitate fast and reproducible evaluation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "AgiBot World: Platform and Data", "weight": 1.0} -->

AgiBot World is a full-stack and open-source embodied intelligence ecosystem. Based on the hardware platform developed by us, AgiBot G1, we construct AgiBot World--- an open-source robot manipulation dataset collected by more than 100 homogeneous robots, providing high-quality data for challenging tasks spanning a wide spectrum of real-life scenarios. The latest version contains 1,001,552 trajectories, with a total duration of 2976.4 hours, covering 217 specific tasks, 87 skills, and 106 scenes. We go beyond basic tabletop tasks such as pick-and-place in lab environments; instead, concentrate on real-world scenarios involving dual-arm manipulation, dexterous hands, and collaborative tasks. AgiBot World aims to provide an inclusive benchmark to drive the future development of advanced and robust algorithms.

<!-- chunk {"id": "body-0016", "role": "body", "section": "AgiBot World: Platform and Data", "weight": 1.0} -->

We plan to release all resources to enable the community build upon AgiBot World. The dataset is available under the CC BY-NC-SA 4.0 license, along with the model checkpoints and code.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Hardware: A Versatile Humanoid Robot", "weight": 1.0} -->

The hardware platform is the cornerstone of AgiBot World, determining the lower limit of its quality. The standardization of hardware is also the key to streamlining distributed data collection and ensuring reproducible results. We meticulously develop a novel hardware platform for AgiBot World, distinguished by visuo-tactile sensors, durable 6-DoF dexterous hands with humanoid configuration.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Hardware: A Versatile Humanoid Robot", "weight": 1.0} -->

As illustrated in Fig. 1, our robotic platform features dual 7-DoF arms, a mobile chassis, and an adjustable waist. The end effectors are modular, allowing for the use of either a standard gripper or a 6-DoF dexterous hand, depending on task requirements. For tasks necessitating tactile feedback, a gripper equipped with visuo-tactile sensors is utilized. The robot is outfitted with eight cameras: an RGB-D camera and three fisheye cameras for the front view, RGB-D or fisheye cameras mounted on each end-effector, and two fisheye cameras positioned at the rear. Image observations and proprioceptive states, including joint and end-effector positions, are recorded at a control frequency of 30 Hz.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Hardware: A Versatile Humanoid Robot", "weight": 1.0} -->

We employ two teleoperation systems: VR headset control and whole-body motion capture control. The VR controller maps the hand gesture to the end-effector translation and rotation, which is subsequently converted to joint angles through inverse kinematics. The thumbsticks and buttons on the controller enable robot base and body movement, while the trigger buttons control end-effector actuation. However, the VR controller restricts the dexterous hand to only a few predefined gestures. To extensively unlock our robot's capabilities, we adapt a motion capture system which records the data of human joints, including the fingers, and maps them to robot posture, enabling more nuanced control, including individual finger movements, torso pose, and head orientation. This system provides posture flexibility and execution precision that are required in achieving more complex manipulation tasks.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Data Collection: Protocol and Quality", "weight": 1.0} -->

The data collection session, as shown in Fig. 2, can be broadly divided into three phases. Before formally commencing data collection, we first conduct preliminary data acquisition to validate the feasibility of each task and establish corresponding collection standards. After feasibility validation and review of the collection standards, skilled teleoperators arrange the initial scene and formally begin data collection according to the established standards. All data undergoes an initial validity verification locally, such as verifying the absence of missing frames. Once the data is confirmed to be complete, it is uploaded to the cloud for the next phase. During post-processing, the data annotators will verify whether each episode meets the collection standards established in phase 1 and provide language annotations.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Data Collection: Protocol and Quality", "weight": 1.0} -->

Failure recovery. During data collection, teleoperators may occasionally commit errors, such as inadvertently dropping objects while manipulating the robotic arms. However, they are often able to recover from these errors and successfully complete the task without requiring a full reconfiguration of the setup. Rather than discarding such trajectories, we retain them and manually annotate each with corresponding failure reasons and timestamps. These trajectories, referred to as failure recovery data, constitute approximately one percent of the dataset. We consider them invaluable for achieving policy alignment and failure reflection, essential for advancing the next generation of robot foundation models.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Data Collection: Protocol and Quality", "weight": 1.0} -->

Human-in-the-loop. Concurrent with feedback collection from data annotators, we adopt a human-in-the-loop approach to assess and refine data quality. This process involves an iterative cycle of collecting a small set of demonstrations, training a policy, and deploying the resulting policy to evaluate data availability. Based on the policy's performance, we iteratively refine the data collection pipeline to address identified gaps or inefficiencies. For instance, during real-world deployment, the model exhibits prolonged pauses at the onset of actions, aligning with data annotator feedback highlighting inconsistent transitions and excessive idle time in the collected data. In response, we revise the data collection protocols and introduce a post-processing step to eliminate idle frames, thereby enhancing the dataset's overall utility for policy learning. This feedback-driven methodology ensures continuous improvement in data quality.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-C Dataset Statistics and Analysis: Beyond Scale", "weight": 1.0} -->

AgiBot World is developed through a large-scale data collection facility, which spans over 4,000 square meters. This extensive environment contains over 3,000 unique objects in a variety of scenes, meticulously designed to reflect real-world settings. The dataset covers a wide range of scenarios and scene setups, ensuring both scale and diversity in the pursuit of generalizable robot policy.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-C Dataset Statistics and Analysis: Beyond Scale", "weight": 1.0} -->

Reconstructing the diversity of the real world. Key statistics of our dataset are presented in Fig. 3. AgiBot World provides extensive coverage across five key domains: domestic, retail, industrial, restaurant, and office environments. Within each domain, we further define specific scene categories. For instance, the domestic domain includes detailed environments such as bedrooms, kitchens, living rooms, and balconies, while the retail domain features distinct areas like shelving units and fresh produce sections. Our dataset also features over 3,000 distinct objects, systematically categorized across various scenes. These objects span a wide range of everyday items, including food, furniture, clothing, electronic devices, and more. The distribution of object categories, as illustrated in Fig. 3(a), highlights the relative frequency of different object types within each scene.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Dataset Statistics and Analysis: Beyond Scale", "weight": 1.0} -->

Long-horizon manipulation. A distinguishing feature of the AgiBot World dataset is its emphasis on long-horizon manipulation. As shown in Fig. 3(b), prior datasets predominantly focus on tasks involving single atomic skills, with most trajectories lasting no more than 5 seconds. In contrast, AgiBot World is built upon continuous and complete tasks composed by multiple atomic skills, like "make a coffee". Trajectories in our dataset typically span approximately 30 seconds, some of which last over 2 minutes. We also provide key-frame and instruction annotation for each sub-step to facilitate policy learning in such challenging scenarios.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C Dataset Statistics and Analysis: Beyond Scale", "weight": 1.0} -->

Comprehensive skill coverage. In terms of task design, while generic atomic skills, such as "pick-and-place", dominate the majority of tasks, we have intentionally incorporated tasks that emphasize less frequently used but highly valuable skills, such as "chop" and "plug" (as shown in Fig. 3(c)). This ensures that our dataset adequately represents a broad spectrum of skills, providing sufficient data for each to support robust policy learning.

<!-- chunk {"id": "body-0027", "role": "body", "section": "AgiBot World: Model", "weight": 1.0} -->

To effectively utilize our high-quality AgiBot World dataset and enhance the policy's generalizability, we propose a hierarchical Vision-Language-Latent-Action (ViLLA) framework with three training stages, as depicted in Fig. 4. Compared to Vision-Language-Action (VLA) model where action is vision-language conditioned, the ViLLA model predicts latent action tokens, conditioned on the generation of subsequent robot control actions.

<!-- chunk {"id": "body-0028", "role": "body", "section": "AgiBot World: Model", "weight": 1.0} -->

In Stage 1, we project consecutive images into a latent action space by training an encoder-decoder latent action model (LAM) on internet-scale heterogeneous data. This allows the latent action to serve as an intermediate representation, bridging the gap between general image-text inputs and robotic actions. In Stage 2, these latent actions act as pseudo-labels for the latent planner, facilitating embodiment-agnostic long-horizon planning and leveraging the generalizability of the pre-trained VLM. Finally, in Stage 3, we introduce the action expert and jointly train it with the latent planner to support the learning of dexterous manipulation.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A Latent Action Model", "weight": 1.0} -->

Despite considerable advancements in gathering diverse robot demonstrations, the volume of action-labeled robot data remains limited relative to web-scale datasets. To broaden the data pool by incorporating internet-scale human videos lacking action labels and cross-embodiment robot data, we employ latent actions in Stage 1 to model the inverse dynamics of consecutive frames. This approach enables the transfer of real-world dynamics from heterogeneous data sources into universal manipulation knowledge.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A Latent Action Model", "weight": 1.0} -->

To extract latent actions from video frames $\{ I_{t},I_{t + H}\}$, the latent action model is constructed around an inverse dynamics model-based encoder $\mathbf{I}{(\left. z_{t} \middle| {I_{t},I_{t + H}} \right.)}$ and a forward dynamics model-based decoder $\mathbf{F}{(\left. I_{t + H} \middle| {I_{t},z_{t}} \right.)}$. The encoder employs a spatial-temporal transformer with casual temporal masks following Bruce et al., while the decoder is a spatial transformer that takes the initial frame and discretized latent action tokens $z_{t} = {\lbrack z_{t}^{0},\ldots,z_{t}^{k - 1}\rbrack}$ as input, with $k$ set to 4.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Latent Action Model", "weight": 1.0} -->

The latent action tokens are quantized using a VQ-VAE objective, with a codebook of size $|C|$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B Latent Planner", "weight": 1.0} -->

With the aim of establishing a solid foundation for scene and object understanding and general reasoning ability, the ViLLA model harnesses a VLM pre-trained on web-scale vision-language data and incorporates a latent planner for embodiment-agnostic planning within the latent action space. We use InternVL2.5-2B as the VLM backbone due to its strong transfer learning capabilities. The two-billion parameter scale has proven effective for robotic tasks in our preliminary experiments, as well as in prior studies. Multiview image observations are first encoded using InternViT before being projected into the language space. The latent planner consists of 24 transformer layers, which enable layer-by-layer conditioning from the VLM backbone with full bidirectional attention.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-B Latent Planner", "weight": 1.0} -->

Specifically, given multiview input images $\left( I_{t}^{h},I_{t}^{l},I_{t}^{r} \right)$ (typically from the head, left wrist, and right wrist) at timestep $t$, along with a language instruction $l$ describing the ongoing task, the latent planner predicts latent action tokens: $\mathbf{P}\left( z_{t} \middle| {I_{t}^{h},I_{t}^{l},I_{t}^{r},l} \right)$, with supervision produced by the LAM encoder based on the head view: $z_{t}:={\mathbf{I}{(I_{t}^{h},I_{t + H}^{h})}}$. Since the latent action space is orders of magnitude smaller than the discretized low-level actions used in OpenVLA, this approach also facilitates the efficient adaptation of general-purpose VLMs into robot policies.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-C Action Expert", "weight": 1.0} -->

To achieve high-frequency and dexterous manipulation, Stage 3 integrates an action expert that utilizes a diffusion objective to model the continuous distribution of low-level actions. Although the action expert shares the same architectural framework as the latent planner, their objectives diverge: the latent planner generates discretized latent action tokens through masked language modeling, while the action expert regresses low-level actions via an iterative denoising process. Both expert modules are conditioned hierarchically on preceding modules, including the action expert itself, ensuring coherent integration and information flow within the dual-expert system.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-C Action Expert", "weight": 1.0} -->

The action expert decodes low-level action chunks, denoted by $A_{t} = {\lbrack a_{t},a_{t + 1},\ldots,a_{t + H}\rbrack}$ with $H = 30$, using proprioceptive state $p_{t}$ over an interval of $H$ timesteps: $\mathbf{A}\left( A_{t} \middle| {I_{t}^{h},I_{t}^{l},I_{t}^{r},p_{t},l} \right)$. During inference, the VLM, latent planner, and action expert are synergistically combined within the generalist policy GO-1, which initially predicts $k$ latent action tokens and subsequently conditions the denoising process to produce the final control signals.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiment and Analysis", "weight": 1.0} -->

We evaluate the real-world performance of policies pre-trained on different data sources including the AgiBot World dataset, demonstrating the effectiveness credited from the GO-1 model in policy learning.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-A1 Evaluation Tasks", "weight": 1.0} -->

Here we choose a comprehensive set of tasks that span various dimensions of policy capabilities from AgiBot World for evaluation, including tool-usage (Wipe Table), deformable objects manipulation (Fold Shorts), human-robot interaction (Handover Bottle), language-following (Restock Beverage), etc. Moreover, we design 2 unseen scenarios for each task, covering position generalization, visual distractors, and language generalization, delivering thorough generalization evaluations for policies. The evaluated tasks, also partially shown in Fig. 5, are: 1) "Restock Bag": Pick up the snack from the cart and place it on the supermarket shelf; 2) "Table Bussing": Clear tabletop debris into the trash can; 3) "Pour Water": Grasp the kettle handle, lift the kettle and pour water into the cup; 4) "Restock Beverage": Pick up the bottled beverage from the cart and place it on the supermarket shelf; 5) "Fold Shorts": Fold the shorts laid flat on the table in half twice; 6) "Wipe Table": Clean water spills using the sponge.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-A1 Evaluation Tasks", "weight": 1.0} -->

Scoring rubrics. The evaluation metric employs a normalized score, computed as the average across 10 rollouts per task, scenario, and method. Each episode scores 1.0 for full success, with fractional scores for partial success, enabling a nuanced performance assessment.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-A2 Implementation Details", "weight": 1.0} -->

The AgiBot World alpha dataset is an early-stage subset, containing partial tasks and roughly 14% of the trajectories in the full beta version. (a.k.a. last row in Tab. I). Following the completion of the third-stage pre-training, the pre-trained GO-1 exhibits basic competency in task completion. Unless otherwise specified, we further enhance the model by fine-tuning it using high-quality, task-specific demonstrations, enabling adaptation to new tasks for evaluation. For GO-1, fine-tuning is conducted with a learning rate of 2e-5, a batch size of 768, and 30,000 optimization steps.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-B Does AgiBot World boost policy learning at scale?", "weight": 1.0} -->

We choose the open-source RDT model to study how much the AgiBot World dataset can help policy learning. The task completion scores for three tasks are detailed in Fig. 6. Models pre-trained on the AgiBot World dataset demonstrate a significant improvement in the "Table Bussing" task, nearly tripling performance. On average, the completion score increases by 0.30 and 0.29 for in-distribution and out-of-distribution setups, respectively. Notably, the AgiBot World alpha dataset, despite having a significantly smaller data volume than OXE, achieves a higher success rate, underscoring the exceptional data quality of our dataset.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-C Is GO-1 a more capable generalist policy?", "weight": 1.0} -->

We evaluate GO-1 on five tasks of varying complexity, categorized by their visual richness and task horizon. The results, as shown in Fig. 5, are averaged over 30 trials per task, with 10 trials conducted in a seen setup and 20 trials under variations or distractions. GO-1 significantly outperforms RDT and $\pi_{0}$, particularly in tasks such as "Pour Water", which demands robustness to object positions, and "Restock Beverage", which highlights instruction-following capabilities. The inclusion of the latent planner yields an average improvement of 0.12 task completion score.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-D Does GO-1's ability scale with data size?", "weight": 1.0} -->

To investigate whether a power-law scaling relationship exists between the size of pre-training data and policy capability, we conduct an analysis using 10% subsets of the alpha, 100% alpha, and beta dataset, where the number of training trajectories are ranged from 9.2k to 1M. We evaluate the out-of-the-box performance of resulting policies on four seen tasks in pre-training. As shown in Fig. 7(a), the policy's performance exhibits a predictable power-law scaling relationship with the number of trajectories, supported by a Pearson correlation coefficient of $r = 0.97$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-E How does data quality impact policy learning?", "weight": 1.0} -->

We explore the impact of quality checks introduced in our human-in-the-loop data collection on policy learning. Specifically, we provide an ablation study by fine-tuning an RDT model using both verified (528 trajectories) and unverified (482 trajectories) data from the "Wipe Table" task. Verification refers to our "human-in-the-loop" quality assurance method. As shown in Fig. 7(b), being larger in quantity does not necessarily translate to improved performance, while a smaller set of human-verified data yields a 0.18 boost in the completion score, underscoring the importance of high-quality data for policy learning.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduce AgiBot World, an open-source ecosystem aimed at democratizing access to large-scale, high-quality robot learning datasets. It is complete with toolchains and foundation models to advance embodied general intelligence through community collaboration. Our dataset distinguishes itself through unparalleled scale, diversity, and quality, underpinned by carefully crafted tasks. Policy learning evaluations confirm AgiBot World's value in enhancing performance and generalizability. To further explore its impact, we develop GO-1, a generalist policy utilizing latent actions for web-scale pre-training. GO-1 excels in real-world complex tasks, outperforming existing generalist policies and demonstrating scalable performance with increased data volume. We invite the broader community to collaborate in fostering an ecosystem and maximizing the potential of our extensive dataset.
