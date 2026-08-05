<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Building Explicit World Model for Zero-Shot Open-World Object Manipulation

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Open-world object manipulation remains a fundamental challenge in robotics. While Vision-Language-Action (VLA) models have demonstrated promising results, they rely heavily on large-scale robot action demonstrations, which are costly to collect and can hinder out-of-distribution generalization. In this paper, we propose an explicit-world-model-based framework for open-world manipulation that achieves zero-shot generalization by constructing a physically grounded digital twin of the environment. The framework integrates open-set perception, digital-twin reconstruction, sampling and evaluation of interaction strategies. By constructing a digital twin of the environment, our approach efficiently explores and evaluates manipulation strategies in physic-enabled simulator and reliably deploys the chosen strategy to the real world. Experimentally, the proposed framework is able to perform multiple open-set manipulation tasks without any task-specific action demonstrations, proving strong zero-shot generalization on both the task and object levels.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Open-world manipulation has recently become a popular research frontier in robotics, aiming to enable robots to perform diverse tasks commanded by humans in unstructured environments. In such settings, robots must have the ability to infer task goals from natural language, perceive and interact physically with previously unseen objects. This open-ended nature introduces fundamental challenges in semantic and physical understanding.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent works have explored Vision--Language--Action (VLA) models, which leverage large-scale vision--language backbones plus an action head to predict robot actions for diverse tasks. Despite strong performance on manipulation benchmarks, VLAs often struggle to generalize beyond the training distribution and rely on large amounts of costly robot demonstration data for supervision. Another line of research investigates world models, which predict the consequences of actions rather than directly imitating demonstrations, either through implicit dynamics modeling or explicit world construction. By reasoning over action outcomes, world-model-based approaches offer improved generalization to unseen objects and tasks.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most existing world models are image- or video-based. While these 2D models can generate visually compelling predictions, they typically lack explicit 3D structure and physical constraints, which limits their ability to faithfully capture real-world dynamics and physical laws. In contrast, explicit world models represent the environment with geometrically and physically meaningful digital-twin assets. However, prior explicit-world-model approaches either target specialized problem settings, such as articulated-object manipulation toward desired joint configurations, or still rely on task-specific demonstrations to train policies. As a result, a method that can generalize zero-shot to both novel objects and novel tasks remains needed.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose an explicit world-model-based framework for object manipulation in open-world environments. In such settings, target objects are not predefined, and the robot must operate on previously unseen, open-set objects. A central challenge is therefore to accurately reconstruct a digital twin from onboard 2D observations, which are inherently partial and can be further degraded by occlusions, e.g., from the gripper during grasping. To address this challenge, our framework combines modern generative and visual foundation models with classical point-cloud registration techniques to reconstruct digital twins that are both geometrically accurate and semantically consistent. Given a high-level task specification, we then sample diverse interaction strategies within the reconstructed world model. A physics engine is used to simulate the outcomes of these candidate strategies, and a large vision--language model (VLM) evaluates their consistency with the task prompts to select the most promising action sequence. The entire pipeline operates without any task-specific training and is independent of robot embodiment, enabling zero-shot generalization to novel objects and tasks.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The contributions of this work are listed as follows: An explicit world model based manipulation framework that achieves zero-shot generalization to novel rigid objects and task specifications, without task-specific training or demonstrations.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A dynamic digital twin construction pipeline that reconstructs object meshes from onboard observation, and aligns scales and poses to real objects for simulation-consistent transfer.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

A VLM-based evaluation module that evaluates the success probabilities of simulated outcomes of sampled action candidates.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We validate our system by evaluating digital-twin construction accuracy and conducting real-robot experiments on multiple open-set, semantically subtle manipulation tasks with previously unseen objects, reporting both qualitative and quantitative results.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Open-world manipulation", "weight": 1.0} -->

Manipulation has long been a popular topic in robotics due to its substantial practical value. Traditional reinforcement learning and imitation learning methods have achieved good performance in this domain, but they typically require training a separate policy for each task, and thus exhibit limited generalization. In contrast, open-world manipulation demands a system that can generate policies for a broad, open-ended set of tasks.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Open-world manipulation", "weight": 1.0} -->

In the early stage, researchers explored leveraging pretrained vision--language foundation models to achieve strong generalization. A common paradigm is to use a foundation model to infer task-specific affordances or a coarse trajectory/keypoints for open-ended instructions. In, the authors both choose to use VLM to predict 2D keypoints, and lift to 3D trajectories. While this approach can generalize well, the task success depends heavily on the accuracy of the model predictions. It typically lacks closed-loop verification and real-time reaction to ensure that the desired outcome is achieved. Thus, in more complete scenarios, this purely feedforward fashion can break down.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Open-world manipulation", "weight": 1.0} -->

Motivated by these limitations, subsequent work has moved toward Vision--Language--Action (VLA) models. VLA models typically adopt a pretrained VLM as the backbone to encode observations and natural-language task instructions, with additionally an action head to produce executable control commands or policies. This design is architecturally concise and can directly inherit strong semantic priors from large pretrained VLMs. However, action data is a fundamentally different modality from language and vision, and a backbone pretrained primarily on discrete tokens of 2D vision and language does not naturally handle this continuous data representation. As a result, VLA performance and robustness remain strongly bottlenecked by the scale and quality of action supervision.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Open-world manipulation", "weight": 1.0} -->

Recently, the emergence of models such as Pi and the release of large-scale Open X-Embodiment datasets have signaled a community-wide effort to scale up VLA training data and push toward an actionable scaling law. Nevertheless, collecting diverse, high-quality robot action trajectories remains expensive and difficult to standardize across embodiments and sensing configurations. Fully realizing the benefits of scaling-up will likely take time.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B World Models", "weight": 1.0} -->

World models were originally introduced in reinforcement learning to improve sample efficiency by enabling agents to *imagine* the consequences of interactions in a learned latent space. By encapsulating the environment dynamics, a world model allows an agent to roll out hypothetical futures, support planning, and make informed decisions without executing every action in the real world.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B World Models", "weight": 1.0} -->

With the recent surge of video diffusion models, much of the progress has focused on image- or video-based world models. Despite producing visually compelling predictions, such 2D world models often struggle to provide explicit 3D structure and physical consistency, due to their 2D training data and underlying 2D representations. This limitation makes it difficult to faithfully reason about geometry, contact, and dynamics required for manipulation.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B World Models", "weight": 1.0} -->

In parallel, another line of research constructs *explicit* world models by leveraging 3D reconstruction or generation techniques, typically focusing on object-centric reconstructions of the entities involved in the task. In, authors propose an explicit-world-model framework that reconstructs a sim-ready digital twin from visual observations and leverages physics-based simulation to train imitation learning policy. Jiang et al. construct explicit world models for articulated objects and plan trajectories via sampling-based model predictive control within a physics simulator, without requiring demonstrations or reinforcement learning.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B World Models", "weight": 1.0} -->

Although these approaches also leverage explicit world models, our focus is different. Compared, which focuses on articulated-object manipulation toward target joint configurations, our framework supports a wider range of open-set manipulation tasks beyond articulated joint-angle goals. In contrast to, which still relies on task demonstrations to train imitation-learning policies, our method enables zero-shot generalization to previously unseen tasks, without requiring any task-specific demonstrations.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Problem Statement", "weight": 1.0} -->

Formally, given the visual observations $I$ of the scene (e.g., RGB-D images), and a natural language task instruction $C$, the objective is to build a world model $W$, and find an $a$ that successfully achieves the goal described by $C$ in the real world. That is, we first build a world model $W$ where $\tau=(s,o)$ is the future states and observations generated by world model $W$, given the current observation $I$ and sampled action $a$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Problem Statement", "weight": 1.0} -->

Then, | | $\displaystyle a^{*}=\arg\max_{a\in\mathcal{A(I)}}E_{\tau\sim p_{W}(\cdot\mid I,a)}[R(C,\tau)],$ | | \(2\) | | | $\displaystyle\mathcal{A}=\{a_{i}\}\sim\pi(\cdot\mid I,C),\;i=1,\ldots,N$ | | | where $\mathcal{A}$ denotes the space of sampled candidate actions from a sample policy $\pi(\cdot\mid I,C)$, parameterized by end-effector poses, $a^{*}$ is the selected best action and $R(C,\tau)$ is a score function that measures the score of $\tau$ given the natural language task instruction $C$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Problem Statement", "weight": 1.0} -->

In this paper, we aim to build an explicit world model that can generate plausible future states and observations $\tau$. We also designed a prior-based sample policy $\pi$ and a VLM-based result checker to measure the success score of $\tau$. We focus on rigid objects. Handling deformable and articulated objects would require incorporating elasticity modeling, joint constraints, and contact deformation into the world model. We leave these extensions to future research.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B System Overview", "weight": 1.0} -->

An overview of the full framework is illustrated in Figure 1. Given an RGB-D image of the scene and a text instruction (e.g., "put the blue cup standing with its opening upside on the right wooden block"), the system outputs a complete manipulation plan and executes it on a real-world manipulator. To achieve our goal, the framework consists of four main components: Open-set Segmentation and Grasping (Section III-C), Digital Twin Construction (Section III-D), and Manipulation Strategy Sampling (Section III-E).

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-C Open-set Segmentation and Grasping", "weight": 1.0} -->

In this module, we first employ GPT-4o and Grounded-SAM to segment any objects related to the given task prompt. Specifically, we query the GPT-4o with the RGB image and a prompt question (e.g., "What objects in the picture are involved in the task 'put the blue cup standing with its opening upside on the right wooden block'? Return their names in two categories as directly manipulated objects and other interactive objects."). The VLM here allows our method to generalize to arbitrary objects beyond a closed set of predefined classes. Once the object are identified, we use Grounded-SAM to segment the target objects from the input image. This gives us accurate 2D segmentation masks $\tilde{M}_{\text{obj}}$ for both directly manipulated objects (e.g., cup) and other interactive objects involved in interaction (e.g., right wooden block).

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-C Open-set Segmentation and Grasping", "weight": 1.0} -->

For object grasping, we adopt AnyGrasp as our grasp pose prediction module, which is trained on a large number of real-world grasping data and has demonstrated strong robustness in open-set, general-purpose grasping tasks. The grasp pose predictor, denoted as $f_{g}(\cdot)$, takes an input RGB-D image $I$ and outputs a set of grasp pose candidates $\tilde{g}=f_{g}(I)$. The predicted grasp candidates $\tilde{g}$ are densely distributed among all graspable objects in the scene. To reduce computational overhead, we first retain only the top 1000 predictions ranked by confidence. For instance-level grasping, we reuse the masks $\tilde{M}_{\text{obj}}$ of the target objects obtained from the open-set segmentation module, retaining only those associated with the object of interest.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Open-set Segmentation and Grasping", "weight": 1.0} -->

Given the $\tilde{M}_{\text{obj}}$ of the target objects, we perform back-projection on the masked RGB-D image $I_{obj}$ to obtain the corresponding partial 3D point cloud $P_{\text{obj}}$. Each grasp candidate in $\tilde{g}$ is then evaluated based on its spatial proximity to the surface of $P_{\text{obj}}$. Specifically, we retain only those grasp poses which lie within a predefined distance threshold from the segmented object's surface points, Figure 2: The proposed digital twin construction module, containing the mesh generation and two-stage pose alignment. We first generate a textured mesh from the masked RGB image via Hunyuan3D 2.0. During coarse alignment, we render RGB and depth images from a set of hypopaper poses and compare their similarities with real-world observation in DINO feature space, and select the one that best matches the real-world observation. The resulting coarse pose is then refined using RANSAC and ICP on the partial point cloud back-projected from the depth image.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C Open-set Segmentation and Grasping", "weight": 1.0} -->

To improve the robustness of the grasping, we also add a grasp result checker. After the execution of grasping, we inquire the GPT-4o with the observation from the bottom camera if the gripper successfully grasped the target object, and if the answer is no (the grasping fails or someone deliberately takes the object off), the system will keep trying to find the object and grasp it.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-D Digital Twin Construction", "weight": 1.0} -->

The objective of this module is to construct accurate 3D meshes of the target objects, align them with real-world observations, and predict their material properties, enabling reliable use in simulation-based interaction and planning.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-D Digital Twin Construction", "weight": 1.0} -->

This project adopts Hunyuan 3D 2.0 as the 3D generation module. However, the mesh generated by the 3D generation module is in unit scale and canonical pose. Therefore, it is necessary to align the generated mesh with the real-world observation by estimating the appropriate scale and 6-DoF pose. Since only partial object geometry is observed (often limited to a single visible side) and additional occlusions may be introduced by the gripper, classical point cloud based alignment methods tend to perform poorly in this scenario. To address this, we proposed two-stage pose alignment pipeline, performs mesh-observation matching in a coarse-to-fine manner, as shown in Fig 2.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-D Digital Twin Construction", "weight": 1.0} -->

Let $\tilde{P}$ denote the set of hypothesized coarse object poses sampled in 6D space (translation and rotation). For each hypothesized pose $\tilde{p}\in\tilde{P}$, the corresponding textured 3D mesh is rendered to obtain both the RGB image $\tilde{I}\text{rgb}$ and the depth image $\tilde{I}\text{depth}$. The following equation describes this rendering process: Then, we compare the similarities of these rendered views with the real-world observation $I_{obs}$ to select the most promising hypothesis as an initial coarse pose estimate. Here we use DINOv2 as the feature extractor and compute the cosine similarities, We then select the hypothesized pose with the highest similarity to the real-world observation as the coarse pose estimate. Using this pose, we render a depth image of the generated mesh and back-project it to obtain a partial point cloud that corresponds to the observed view.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-D Digital Twin Construction", "weight": 1.0} -->

This transformation effectively converts the challenging partial-to-complete alignment problem into a partial-to-partial alignment problem, thereby enabling the use of conventional point cloud registration methods, such as RANSAC and ICP, for further fine alignment.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-D Digital Twin Construction", "weight": 1.0} -->

The coarse alignment produces two roughly aligned point clouds that still differ in scale. To estimate the scale factor, we compare the dimensions of the 3D bounding boxes derived from the partial point clouds of both the rendered mesh and the real observation, and adjust the mesh dimensions to match the real-world object. Following this, we refine the transformation using a combination of RANSAC and ICP, yielding an accurate alignment between the generated mesh and the real object. We examined our mesh alignment pipeline and the results are in Sec. IV-B.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-D Digital Twin Construction", "weight": 1.0} -->

Moreover, Inspired by Xu et al., who leveraged an LLM together with a curated material library to infer the material and physical properties of an object from its masked image, we utilize the reasoning capability of GPT-4o to predict the material of the object. The predicted material can then be used to assign corresponding physical properties in the simulation environment.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-E Manipulation Strategy Sampling", "weight": 1.0} -->

Once the digital twin of the environment is constructed, we integrate it into a physics-enabled simulation environment to perform manipulation strategy sampling. In this work, we adopt NVIDIA Isaac Sim as the simulation platform. We then sample 6-DoF poses for the grasped object, representing candidate manipulation goals. The simulated outcome of each sample is then evaluated to determine whether the manipulation strategy successfully completes the task. This process allows us to test diverse candidate strategies without executing them on the real robot.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-E Manipulation Strategy Sampling", "weight": 1.0} -->

To improve sampling efficiency and reduce the size of the search space, the translation component of the dynamic object's pose is constrained to be near the most probable interaction region, which is predicted by GPT-4o plus Grounded-SAM, as illustrated in Fig. 3a. The segmented region is back-projected into 3D space to obtain a point cloud, from which we compute the centroid as reference for the initial estimate of the translation component.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-E Manipulation Strategy Sampling", "weight": 1.0} -->

After constraining the translation around the interaction area, we sample different rotation angles, which are reachable by the robot arm, to generate diverse 6-DoF pose hypotheses. For each sample, we spawn the non-directly manipulated object at its real-world pose and the grasped object at the sampled pose, and the Kinova arm with proper joint values computed by an inverse kinematics solver.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-E Manipulation Strategy Sampling", "weight": 1.0} -->

For each simulated strategy sample, we render an RGB image as the observation for each candidate from a fixed, front-facing viewpoint with a $-60^{\circ}$ tilt, shown in Fig 3 b on the left. We then query GPT-4o with the rendered image and the natural language task instruction to determine whether the observed outcome satisfies the instruction. This yields weak binary labels $y_{i}\in\{0,1\}$ for each end-effector pose ($\mathbf{t}_{i},\mathbf{q}_{i}$), where $\mathbf{t}_{i}\in\mathbb{R}^{3}$ is translation and $\mathbf{q}_{i}=[w\;x\;y\;z]^{\top}$ is a unit quaternion. The strategies deemed successful by the GPT-4o are prioritized for real-robot execution.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-E Manipulation Strategy Sampling", "weight": 1.0} -->

To obtain calibrated success probabilities, we train a Gaussian Process (GP) classifier over SE on the LLM-provided labels $\{(\mathbf{t}_{i},\mathbf{q}i),y_{i}\}$. At test time, the GP outputs calibrated success probabilities. We use the predicted probabilities to rank all candidate strategies and select the one with the highest likelihood of success for real-robot execution.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A Experiments Setup", "weight": 1.0} -->

Our experiments contain two parts. First, we tested the digital twin alignment accuracy. The second part was nine different real-world manipulation tasks. The selected tasks are designed to validate the system's ability to understand both semantic instructions and spatial relations, and also the ability to complete various open-world manipulation tasks without seeing the objects or demonstrations before. without grasp in the gripper foam box container grasped in the gripper TABLE I: Comparison of mesh alignment performance between our two-stage alignment pipeline and direct alignment.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-A Experiments Setup", "weight": 1.0} -->

We used the 7-DoF Kinova Gen3 Lite robotic arm.Two Intel RealSense D405 stereo cameras were mounted on the gripper and the front bottom on the mobile base, respectively. The bottom camera has a 25 degree elevation angle to better observe the grasped object. For computational resources, we have an NVIDIA RTX 2070 GPU with 6GB RAM on a laptop for Isaac Sim simulation, and an NVIDIA RTX 3090 GPU workstation with 24GB RAM for computer vision models like Grounded-SAM and Hunyuan 3D 2.0.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B Digital Twin Alignment Accuracy", "weight": 1.0} -->

In this experiment, we compare our proposed two-stage mesh alignment pipeline with a direct alignment baseline, which applies RANSAC and ICP directly to the generated mesh. Ideally, the pose error of each object would serve as a more informative metric for evaluating alignment performance; however, ground-truth object poses are unavailable in the real-world setup, and coordinate frames are not consistently fixed for each generated mesh. Therefore, we evaluate alignment performance using two complementary metrics: alignment success rate, which measures the correctness of the estimated object pose, and root mean square error (RMSE), which assesses the geometric precision of the alignment.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B Digital Twin Alignment Accuracy", "weight": 1.0} -->

We conduct experiments across multiple object categories, both being placed freely and under grasping scenarios. Since ground-truth meshes are also unavailable, we use Hunyuan 3D to generate meshes for all samples. Both the proposed and baseline alignment pipelines use the same generated meshes for a fair comparison. The qualitative results are shown in Fig. 4, and quantitative results are summarized in Table I.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-B Digital Twin Alignment Accuracy", "weight": 1.0} -->

The results demonstrate that our proposed two-stage mesh alignment method substantially improves the alignment success rate compared with direct alignment using RANSAC and ICP. The direct alignment baseline relies solely on minimizing point-to-point distances without a reliable initialization, which often leads to convergence to local minima or incorrect correspondences. In contrast, our method leverages an initial coarse alignment stage guided by appearance similarity, effectively narrowing the search space for fine alignment and improving robustness to noise and scale differences. Overall, our method achieves a much higher alignment success rate while maintaining comparable geometric accuracy, validating the effectiveness of the two-stage pipeline for robust and generalizable mesh-to-scene alignment.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-C Real Robot Task Performance", "weight": 1.0} -->

We performed 9 real robot experiments for a total 96 attempts on our system, as shown in Fig. 5. The selected tasks are designed to validate the system's ability to understand both semantic instructions and spatial relations, and also the ability to complete various open-world tasks without seeing the objects before or fine-tuning on these tasks. Relying on these properties, our system shows the potential to tackle the open-world object manipulation problem in a novel way.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C Real Robot Task Performance", "weight": 1.0} -->

The success rates for the selected tasks are reported in Table II. We observe that six of the nine tasks reach a success rate of at least 75%. The other three tasks perform less reliably, and we discuss possible reasons in the later failure analysis.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-C Real Robot Task Performance", "weight": 1.0} -->

Put the banana into the basket Put the lemon into the white cup Put the yellow cube into the white box Put the yellow cube into the blue can Stack the green cube onto the yellow cube Put the long cutlery box on the two boxes, like a bridge Put the long cutlery box into the gap between two boxes Put the blue cup upside on the wooden box Put the blue cup upside down on the wooden box TABLE II: Task success rate of different manipulation scenarios.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-C Real Robot Task Performance", "weight": 1.0} -->

To provide a comprehensive evaluation of the entire system, we record the success/failure results of all major components, including object grasping, mesh alignment, interaction area segmentation, strategy sampling in simulation, sampling result checking, and real robot execution. The results are visualized as a Sankey diagram as shown in Fig 6.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-C Real Robot Task Performance", "weight": 1.0} -->

Most of the failures came up from the result checker and final execution stage. The result checker failure denotes that the visual information were not clear enough, at least for an LLM, to make correct judgments. We also conducted a task-level failure analysis as illustrated in Fig.7, and it shows that most of the result checker failures happened in the "cup on/upside down on the boxes", since the visual features of a cup standing upside and upside down were ambiguous. Overall, the LLM-based checker did demonstrate strong generalization and semantic understanding across different object configurations. However, its sensitivity to visual ambiguity suggests that incorporating multimodal feedback (e.g., depth or contact information) could further improve its robustness.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-C Real Robot Task Performance", "weight": 1.0} -->

The real robot execution failure means that although the action candidates were successful in the simulator, the real robot execution still failed, indicating the sim-to-real gap was nontrivial. Several factors contribute to this discrepancy. First, the physics engine of Isaac Sim, though highly realistic, cannot perfectly replicate real-world contact dynamics. In an attempt to mitigate this gap, we incorporated material property estimation to better parameterize physical attributes in Isaac Sim. However, the range of adjustable parameters remains limited for rigid body objects. In particular, hollow or deformable structures, such as plastic cubes in the 'Stack cubes' task, cannot yet be accurately modeled or detected based solely on visual appearance, leading to further inconsistencies between simulated and real interactions. Second, the robot hardware precision and control latency introduce minor pose and timing errors that can accumulate during execution, especially for tasks with tight spatial constraints. Third, sensor noise and calibration errors (e.g., camera extrinsics and depth inaccuracies) can cause small misalignment between the reconstructed scene and the actual setup.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This work presented a novel framework that constructs a mesh-based explicit world model to enable action sampling and evaluation for open-world manipulation tasks. Our approach leverages VLMs and a simulator to reason about object dynamics and choose successful actions without any demonstrations. Experimental results demonstrate that the proposed two-stage mesh alignment pipeline is able to support the accuracy and robustness of digital twin reconstruction, providing more reliable object pose estimation. With the constructed explicit world model, the system is capable of performing dynamic reasoning and strategy evaluation across diverse manipulation tasks, and achieves successful transfer from simulation to real-world execution, proven by real robot experiments.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion", "weight": 1.5} -->

While the proposed framework demonstrates promising results, the simulation-based strategy sampling process remains computationally demanding, which currently prevents real-time deployment. Future work will focus on improving computational efficiency to facilitate efficient real-world deployment.
