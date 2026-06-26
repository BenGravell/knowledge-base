<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

PointWorld: Scaling 3D World Models for In-the-Wild Robotic Manipulation

Topics include World models, Robot manipulation, 3D perception, Point cloud, Robot learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents PointWorld, a 3D world model that predicts action-conditioned point flows from RGB-D observations for robotic manipulation. The paper is useful because it moves world modeling from image/video prediction toward geometry-aware representations tied to robot action effects.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Humans anticipate, from a glance and a contemplated action of their bodies, how the 3D world will respond, a capability that is equally vital for robotic manipulation. We introduce PointWorld, a large pre-trained 3D world model that unifies state and action in a shared 3D space as 3D point flows: given one or few RGB-D images and a sequence of low-level robot action commands, PointWorld forecasts per-pixel displacements in 3D that respond to the given actions. By representing actions as 3D point flows instead of embodiment-specific action spaces (e.g., joint positions), this formulation directly conditions on physical geometries of robots while seamlessly integrating learning across embodiments. To train our 3D world model, we curate a large-scale dataset spanning real and simulated robotic manipulation in open-world environments, enabled by recent advances in 3D vision and simulated environments, totaling about 2M trajectories and 500 hours across a single-arm Franka and a bimanual humanoid.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Through rigorous, large-scale empirical studies of backbones, action representations, learning objectives, partial observability, data mixtures, domain transfers, and scaling, we distill design principles for large-scale 3D world modeling. With a real-time (0.1s) inference speed, PointWorld can be efficiently integrated in the model-predictive control (MPC) framework for manipulation. We demonstrate that a single pre-trained checkpoint enables a real-world Franka robot to perform rigid-body pushing, deformable and articulated object manipulation, and tool use, without requiring any demonstrations or post-training and all from a single image captured in-the-wild. Project website at

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

World modeling in unstructured environments is imperative for general-purpose robots: predicting how the world evolves from what the robot sees and intends to do with its body. Humans do this from a glance and a grasp, forecasting deformation, articulation, stability, and contact, revealing how much a world-modeling objective captures when conditioned on a contemplated action in 3D (Figure 3). Actions unfold where physics lives, in space and time: our aim is a predictive model that makes such spatially grounded, action-conditioned predictions from only perceptual inputs in open-world settings, a pinnacle goal of spatial intelligence.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A large body of work has studied world modeling from complementary angles. Physics-based models, while capable of highly accurate predictions, face sim-to-real gaps and require curated, environment-specific modeling. Learning-based dynamics models address this by learning from observed interaction, yet often depend on domain-specific inductive bias (e.g., full observability, objectness priors, or material specification). In parallel, large video generative models trained at scale are capable of producing photorealistic predictions but lack explicit action conditioning and often fall short on physical consistency. See Ai et al. for a recent survey. Despite progress, a gap remains between what current models predict and what humans can foresee from visual observations in the wild and a contemplated action.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our philosophy is unification for scaling: represent *state* and *action* in the same modality of 3D physical space. State is represented by a full-scene 3D point cloud built from RGB-D captures; actions are dense 3D point trajectories instantiated from the agent's own embodiment, typically known a priori (e.g., a robot description file), and thus forecastable over time. Under this representation, 3D world modeling equates to modeling *full-scene 3D point flow* under perturbations from a temporal sequence of robot points: given partially observed 3D scene points and those action points, predict per-point scene displacements over a horizon. While conceptually simple, this formulation ties raw sensory observation and an *embodiment-agnostic* action space in a shared representation through dynamics (what moves, how, and where) and implicitly captures objectness, articulation, and material properties, all through interaction between the robot's specific geometry (e.g., grippers, fingers) and the partially-observed scene.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

By modeling the *geometries of interaction* independent of goals, PointWorld aims to capture the single source of truth of the physical world, while naturally learning from heterogeneous embodiments, tasks, and trajectories (regardless of success or failure), akin to "next-token prediction" but for interaction over 3D space and time. We term our approach PointWorld.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

To provide supervision, we curate a large-scale dataset for 3D dynamics modeling, spanning hundreds of in-the-wild scenes with single-arm, bimanual, and whole-body interactions across both real and simulated domains. The dataset was built from existing robotic manipulation datasets, DROID and BEHAVIOR-1K. Since accurate 3D annotations are crucial for capturing precise contact in physical interactions, significant efforts were spent to build a custom pipeline to extract 3D point flows from the real-world dataset, enabled by recent advances in metric depth estimation, camera pose estimation, and point tracking. Leveraging the dataset, we distill important design decisions for large-scale 3D dynamics learning through rigorous investigations of backbone architectures, action representations, objectives, partial observability, data mixtures, scaling laws, and domain transfers under zero-shot and finetuned settings.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To demonstrate PointWorld's potential for manipulation, we integrate it with a model-predictive controller (MPC) for action inference on a real robot. As PointWorld predicts scene dynamics jointly over short action chunks in a single forward pass at a real-time latency (0.1s), it provides a natural and efficient integration with sampling-based MPC (e.g., MPPI ). We show that a single pre-trained checkpoint enables a real-world robot to perform rigid-body pushing, deformable and articulated object manipulation, and tool use, without requiring any demonstrations or post-training and all from a single image captured in-the-wild.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. (i) We introduce a large pre-trained 3D world model, PointWorld, that unifies state and action in a shared representation of 3D point flows, and present rigorous studies of its modeling recipe. (ii) We curate and open-source a large-scale high-quality 3D interaction dataset used for training PointWorld, totaling $\sim 2$M trajectories or $\sim 500$ hours. (iii) We demonstrate a single pre-trained PointWorld enables a real robot to perform diverse manipulation tasks from a single in-the-wild RGB-D capture, without requiring additional demonstrations or training.

<!-- chunk {"id": "body-0012", "role": "body", "section": "World Modeling", "weight": 1.0} -->

World models are predictive models that simulate future states given current state and action, categorized often by their state-action representations. Video models use pixel-space state, trained either with photometric reconstruction or joint-embedding predictions. 3D world models instead operate on meshes or explicit surfaces, radiance fields or Gaussians, or particles. Hybrid approaches additionally reason over hierarchical structures in world modeling. Action parameterizations range from low-level joint-space commands, to camera and navigation motions, textual prompts, and 2D cues. Robot actions can then be produced by online planning, offline policy synthesis, or inverse-dynamics models. PointWorld uses 3D point flow as shared state-action representation, emphasizing contact and geometry rather than appearance, conditions on 3D actions with specific geometry of given robot/gripper, interaction beyond only visible regions compared to 2D cues, and doing so with one (or sparse) input images (with estimated depth) in a single, real-time forward pass of a large pre-trained model (Figure 3).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Dynamics Models in Robotics", "weight": 1.0} -->

Dynamics models in robotics instantiate world models with robot action spaces. They include physics-based simulators and learning-based models. Crucial for robotics, they support policy learning, planning, model-based RL, exploration and online guidance, safety filtering, model-based design and verification, and policy evaluation. While existing dynamics models often require curated, scene-specific modeling, our aim is to pre-train a single dynamics model that generalizes across diverse in-the-wild environments. Using 3D flows as state-action space, it naturally encapsulates many action parameterizations used in prior works in an embodiment-agnostic manner: joint-space commands, end-effector actions, and motion primitives, while operating on partially observable RGB-D image(s) in the wild without scene reconstruction, priors on objectness or materials.

<!-- chunk {"id": "body-0014", "role": "body", "section": "2D and 3D Flows for Manipulation", "weight": 1.0} -->

Flows (or point tracks), which address correspondences across space and time, provide a powerful interface between perception and control. With advances in point tracking, recent works explored them as structured representations for policy learning, reward modeling, (sub-)goal specification, or as visual servoing targets. In this work, we leverage recent advances in 3D vision (depth, camera pose estimation, and point tracking ) to label 3D scene flows from large-scale real-world manipulation dataset (with robot flows obtained from known robot geometry, kinematics, and proprioception), which enables training of a large 3D world models via stable regression losses to capture robotic interactions with diverse objects in open-world environments.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Method", "weight": 1.0} -->

We formulate 3D world modeling as action-conditioned full-scene 3D point flow prediction (Section 3.1; Figure 2). We then describe how PointWorld may be used for action inference and discuss its use case in the framework of model predictive control that we explore in this work (Section 3.2).

<!-- chunk {"id": "body-0016", "role": "body", "section": "3D World Modeling with PointWorld", "weight": 1.0} -->

We model environment dynamics as a neural network $\mathcal{F}_{\theta}:\mathbf{S}\times\mathbf{A}\rightarrow\mathbf{S}$ parametrized by $\theta$ that predicts next state given current state and robot action, where $\mathbf{S}$ and $\mathbf{A}$ denote state and action spaces. Existing approaches typically formulate this as a single-step update $\mathbf{s}_{t+1}\,=\,\mathcal{F}_{\theta}\big(\mathbf{s}_{t},\mathbf{a}_{t}\big)$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "3D World Modeling with PointWorld", "weight": 1.0} -->

In contrast, we adopt a multi-step (chunked) formulation for data-driven modeling: the model predicts future states over a horizon $H$ in a single forward pass $\mathcal{F}^{H}_{\theta}:(\mathbf{s}_{t},\mathbf{a}_{t:t+H-1})\rightarrow\mathbf{s}_{t+1:t+H}$, which improves temporal consistency and amortizes computation. We use $H=10$ steps and 0.1s per step.

<!-- chunk {"id": "body-0018", "role": "body", "section": "State Representation", "weight": 1.0} -->

Building a world model requires a deliberate choice of a state space $\mathbf{S}$, with state at time $t$ denoted by $\mathbf{s}_{t}\in\mathbf{S}$. In this work, we use *point flows* (referred also as particles ) as the environment state. Formally, let $\mathbf{s}_{t}=\{\,(\mathbf{p}_{t,i},\,\mathbf{f}^{S}_{i})\,\}_{i=1}^{N_{S}}$ denote the point flows at time $t$, consisting of $N_{S}$ points with positions $\mathbf{p}_{t,i}\in\mathbb{R}^{3}$ and time-constant features $\mathbf{f}^{S}_{i}\in\mathbb{R}^{D_{S}}$ of dimension $D_{S}$ for each point.

<!-- chunk {"id": "body-0019", "role": "body", "section": "State Representation", "weight": 1.0} -->

Compared to alternative representations, point flows offer the following advantages for world modeling in manipulation: (i) emphasis on physical interactions between 3D geometries instead of appearance, akin to the role of physics simulators rather than renderers; (ii) accessibility from any RGB-D captures in partially observable environments while not assuming objectness or material priors; (iii) simple and stable training via L2 losses on displacements, without permutation matching; (iv) expressiveness to capture diverse fine-grained contact dynamics. To obtain the point flows, from one or a few calibrated RGB‑D views, we mask robot pixels via forward kinematics (using the URDF and joint configuration) and back‑project the remaining pixels to obtain $\mathbf{p}_{t,i}$. Note that since the model takes in a static point set from the environment as input, and correspondence is preserved only within the model's forward pass (i.e., its "imagination"), no separate point tracker is required for inference, and point count may vary between forward passes.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Action Representation", "weight": 1.0} -->

To learn from heterogeneous embodiments (different kinematics, gripper geometries, and even different numbers of grippers), we again use 3D point flows. However, unlike scene point flows which are obtained from RGB-D captures, robot point flows are generated by forecasting the robot's own geometry via forward kinematics using its URDF (known a priori). This is an intentional design for ensuring "imagined actions" are *fully*, rather than partially, observable while being represented in an *embodiment-agnostic* way--crucial in cases where contact occurs in occluded regions (e.g., holding and transporting a large box with egocentric view).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Action Representation", "weight": 1.0} -->

Specifically, given a sequence of joint configurations $\{\mathbf{q}_{t+k}\}_{k=0}^{H}$, we sample robot surface points once at time $t$, attach each to its corresponding link, and propagate them with forward kinematics to obtain an ordered set of $N_{R}$ robot points $\{\,(\mathbf{r}_{t+k,j},\,\mathbf{f}^{R}_{t+k,j})\,\}_{j=1}^{N_{R}}$ at each time step $t{+}k$, where $\mathbf{r}_{t+k,j}\in\mathbb{R}^{3}$ denotes the position of point $j$ at time $t{+}k$ and $\mathbf{f}^{R}_{t+k,j}\in\mathbb{R}^{D_{R}}$ is its time-varying feature vector of dimension $D_{R}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Action Representation", "weight": 1.0} -->

We treat this collection as the action at time $t{+}k$ and denote it by $\mathbf{a}_{t+k}$. This yields an embodiment‑agnostic description of *interaction geometry* over the horizon. In practice, most robot surface points never contact the scene; for efficiency, we sample robot point flows from only the grippers (a few hundred points per gripper depending on its geometry). See Section 5.2 for experiments.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Dynamics Prediction", "weight": 1.0} -->

Given the above state-action representations, we now have a static full-scene point cloud $\mathbf{s}_{t}$ and a temporal sequence of robot point-flow actions $\mathbf{a}_{t:t+H-1}$ as inputs to the model. Instead of designing custom architectures, we deliberately build on top of state-of-the-art point cloud backbones to distill the core principles that enable scalable, large-scale 3D world modeling. Towards this goal, we concatenate the initial scene points with the time‑stacked robot points to form a single point cloud processed by the backbone. Scene points are featurized with frozen DINOv3 by projecting them to 2D views, while robot points are featurized with temporal embedding. The point cloud backbone processes the concatenated point cloud and outputs features for all points. A shared MLP head then predicts per-point displacements of the scene points at each step within a chunk of length $H$ in a single forward pass.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Dynamics Prediction", "weight": 1.0} -->

This chunked formulation delivers extremely efficient inference capable of evaluating many candidate trajectories with a real-time latency ($0.1\,\mathrm{s}$ per batched forward pass), which stands in contrast to pixel-based approaches that typically require seconds-long inference due to the use of diffusion objectives.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Training Objective", "weight": 1.0} -->

While the formulation lends itself to standard regression objectives, 3D world modeling introduces two distinctive challenges that require careful design: (i) due to full-scene prediction, the robot often manipulates only a small subset of the scene, so most points are static and standard L2 loss leads to very sparse training signal; (ii) real-world data is noisy, so we need to regularize the model to be robust to this noise. To address challenge (i), we adopt a weighted regression objective, reweighting each point at each timestep by a soft movement likelihood $m_{k,i}\in$ computed from ground-truth motion so as to focus the loss on moving points. Letting $\delta_{k,i}\geq 0$ denote the norm of the ground-truth displacement vector for point $i$ at step $k$, we set $m_{k,i}=\sigma\big(\kappa(\delta_{k,i}-\tau)\big)$, where $\sigma$ is the logistic sigmoid, and $\tau$ and $\kappa$ are non-negative displacement-threshold and temperature parameters, respectively.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Training Objective", "weight": 1.0} -->

We then normalize these likelihoods to obtain weights $w_{k,i}=m_{k,i}/\sum_{k,i}m_{k,i}$ for each point $i$ at step $k$. To address challenge (ii), we adopt aleatoric uncertainty regularization by predicting a scalar log-variance $s_{k,i}$ for each point $i$ at step $k$ and further using a Huber loss on the residual. Formally, the full training objective becomes: where $\rho_{\delta}$ is the elementwise Huber loss, and $\mathbf{\hat{P}}_{t+k,i}$ and $\mathbf{P}_{t+k,i}$ are the predicted and ground-truth positions of point $i$ at step $k$, respectively. In practice, we also ignore the points that are deemed not visible by the 2D tracker used to provide the pseudo ground-truth (more details in Section 4).

<!-- chunk {"id": "body-0027", "role": "body", "section": "PointWorld for Robotic Manipulation", "weight": 1.0} -->

A pre-trained PointWorld enables diverse use cases in robotics, as discussed in Section 2. In this work, we specifically investigate whether a single pre-trained PointWorld can enable action inference in unseen, in-the-wild real-world environments from only a single RGB-D capture, without any additional demonstrations or post-training at deployment time. To this end, we integrate PointWorld in an MPC framework with a sampling-based planner MPPI that plans a sequence of $T$ end‑effector pose targets in $\mathrm{SE}$ given a cost function defined in the model's state space. Specifically, given a calibrated RGB-D capture, we first form a scene point set as described in Section 3.1, yielding an initial state $\mathbf{s}_{0}$. We then sample $K$ action perturbations $\ell_{1:K}$ using a time-correlated (cubic-spline) noise distribution, which are added to a nominal end‑effector trajectory.

<!-- chunk {"id": "body-0028", "role": "body", "section": "PointWorld for Robotic Manipulation", "weight": 1.0} -->

For each sampled trajectory $\mathbf{E}^{(\ell)}_{1:T}$, the corresponding robot point-flow actions $\mathbf{a}_{1:T}^{(\ell)}$ are constructed, scene flows are rolled out by PointWorld conditioned on $\mathbf{a}_{1:T}^{(\ell)}$, and a trajectory cost $J^{(\ell)}$ is accumulated. The nominal trajectory is iteratively refined by computing exponentiated weights $\omega_{\ell}\propto\exp(-J^{(\ell)}/\beta)$ over samples and updating the nominal as a weighted average of sampled trajectories, where $\beta$ is non-negative temperature.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Dataset Curation and Evaluation Protocol", "weight": 1.0} -->

Accurate, large-scale 3D data is essential for the world model in Section 3 to generalize in the wild. Apart from requiring action labels, the dataset needs to also have accurate spatial perception (i.e., high-fidelity depth), hand-eye calibration (i.e., camera extrinsics in robot base frame), and per-pixel correspondence matching amid occlusions (i.e., point tracking). While large efforts have been made for collecting diverse real-world manipulation datasets, obtaining their 3D annotations has previously been challenging. Our key observation is that recent advances in 3D vision---metric depth estimation, camera pose estimation, and dense point tracking---are maturing to provide a markerless offline pipeline that operates purely on recorded data to produce such a dataset of interest (Figure 5 top-left). Photorealistic simulation complements this with ground-truth supervision. Combining both, we curate a dataset of about $2$M trajectories ($500$ hours) spanning single-arm, bimanual, and whole-body teleoperated interactions across in-the-wild real scenes and simulated home-scale environments.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Dataset Curation and Evaluation Protocol", "weight": 1.0} -->

To the best of our knowledge, this constitutes the largest 3D dynamics modeling dataset, which we fully open-source.

<!-- chunk {"id": "body-0031", "role": "body", "section": "3D Annotation for Real-World Data", "weight": 1.0} -->

We leverage DROID, a robot manipulation dataset with diverse in-the-wild interactions recorded by two external cameras and a wrist-mounted camera. Although DROID provides sensor depth and camera extrinsics, the depth often degrades in open-world environments and camera poses are inaccurate due to imperfect calibration. Frontier 3D reconstruction models such as VGGT jointly estimate depth and camera parameters from RGB images and often look visually plausible, but yield overly smoothed depth maps and camera poses that can deviate from ground-truth by tens of centimeters.

<!-- chunk {"id": "body-0032", "role": "body", "section": "3D Annotation for Real-World Data", "weight": 1.0} -->

After extensive experimentation, we adopt a three-stage annotation pipeline that combines several learned models with a dedicated optimization procedure. First, we replace sensor depth with stereo-estimated depth from FoundationStereo, which is particularly effective at the close working distances typical of manipulation. Second, we compute camera extrinsics by refining VGGT-initialized camera poses with an optimization procedure that aligns robot depth observations to the known robot mesh. Third, given accurate depth and extrinsics, we perform per-pixel point tracking using CoTracker3. CoTracker3 is a 2D point tracker that outputs image-space correspondences and a visibility map; we lift these tracks to 3D using the refined depth and camera poses and carry over the visibility labels so that occluded points are excluded from supervision during model training. With this pipeline, we recover reliable tracked 3D point flows for over 60% of DROID (nearly 200 hours of raw human teleoperation) and obtain reconstructed point clouds that both qualitatively and quantitatively improve over both original dataset and alternative annotation methods (Figure 5).

<!-- chunk {"id": "body-0033", "role": "body", "section": "3D Annotation for Real-World Data", "weight": 1.0} -->

To further assess extrinsics accuracy in the absence of ground truth in the real world, we treat the best 1% of scenes under the original dataset extrinsics (as measured by depth reprojection loss) as a proxy for the true extrinsics. Relative to this reference, our optimized extrinsics achieve a median translation and rotation error of 1.8 cm and 1.9 degrees.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Simulation (BEHAVIOR-1K)", "weight": 1.0} -->

To complement real-world data, we use BEHAVIOR-1K (B1K), which provides about $1100$ hours of teleoperated (pre-filtering) interaction in photorealistic home-scale environments with bimanual, whole-body, and mobile manipulation. We obtain ground-truth 3D point flows by leveraging known simulation state. Because the dataset focuses on long-horizon activities while PointWorld focuses on short-horizon interaction dynamics, we filter trajectories using privileged information accessible in simulation. We retain only trajectories with active contacts between robot and objects and those with nonzero object motion. More details are in Appendix.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Model Evaluation Protocol", "weight": 1.0} -->

We evaluate predicted point flow from PointWorld and other baselines using a per-point, per-timestep $\ell_{2}$ distance over the prediction horizon. Because most scene points remain static during robot interaction, we focus on the metric on moving points ($\ell_{2}$ mover), as measured by ground-truth data and filter the full set of points using the movement likelihood introduced in Section 3. For real-world domains, we further denoise the evaluation data by training a separate expert model only on the held-out test split to flag unreliable flows via the uncertainty objective from Section 3, retaining only the top 80% of points measured by model confidence. All evaluated models are trained exclusively on the imperfect training set and are evaluated on the expert-filtered test set. Details in Appendix.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Interpretation of the Metric", "weight": 1.0} -->

This dense per-point $\ell_{2}$ metric is highly discriminative when comparing methods and reveals systematic differences in rollout fidelity that task-level success rates often fail to expose. Because all errors are measured over one-second horizons, absolute metric differences can appear modest, since even large motions move points by only a few centimeters, yet we empirically observe that small numerical differences often correspond to pronounced qualitative gains in rollout fidelity. Given the scale of the evaluation set (approx. $40{,}000$ robot trajectories with $10{,}000$ point flows each), standard errors for the $\ell_{2}$ metrics are negligible ($\leq 10^{-5}$m), so we report means only.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

Focusing on real-world data, we chart a roadmap of empirical lessons we learned for scaling 3D world models (Section 5.1, Figure 7). We then discuss targeted ablations along complementary design axes for PointWorld (Section 5.2). Using real and simulated data, we quantify in-domain, cross-domain, and held-out generalization under zero-shot and finetuned settings (Section 5.3). Finally, we study PointWorld for MPC-based action inference on a physical robot in the wild without extra demonstrations or finetuning (Section 5.4). All experiments are constructed to isolate a single modeling choice under controlled setups compared to baselines unless otherwise stated.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Scaling 3D World Models: A Roadmap", "weight": 1.0} -->

Modern point cloud backbone (PTv3 ) is effective, efficient, and scalable for 3D world modeling. Graph-based neural dynamics (GBND) models are widely used for dynamics modeling due to their relational inductive bias. Scaling a GBND baseline to our dataset reveals two challenges (Table 1). Memory consumption grows rapidly because maintaining high-dim features for all points in a scene is expensive. Purely local message passing struggles under partial observability, since long-range effects must traverse noisy hops. Motivated by these limitations, we study alternative point cloud architectures, moving from PointNet, PointNet++, sparse convolutional nets to transformers. Among these, PointTransformerV3 (PTv3) delivers the strongest modeling power. Its point serialization mirrors GBND's local grouping, while U-net hierarchy enables attention over progressively coarser point sets for long-range modeling and substantial parameter growth. Table 1 shows that it scales to $957\times$ GBND while keeping modest memory and runtime increases. These results motivate PTv3 as the default backbone.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Scaling 3D World Models: A Roadmap", "weight": 1.0} -->

Movement weighting, uncertainty regularization, Huber loss stabilize 3D world model learning on real-world data. Discussed in Section 3, naïve $\ell_{2}$ loss is hard to optimize because only a fraction of points move ($1$--$5\%$). Noisy real-world data exacerbates this. We therefore adopt movement weighting, uncertainty regularization, and a Huber loss on 3D residuals. Movement weighting alone over-emphasizes noisy signals, but the uncertainty head and robust loss temper the weights and reduce overfitting. Together, these changes stabilize training and improve accuracy relative to an unweighted $\ell_{2}$ baseline.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Scaling 3D World Models: A Roadmap", "weight": 1.0} -->

Pre-trained 2D features offer critical priors and substantial gains. High-quality pretrained 3D representations remain scarce despite compelling 3D geometry. Methods such as Sonata make encouraging progress but often lag behind in fine-grained scenes. Following, we hypothesize that dense features from DINOv3 provide objectness priors without explicit segmentation. We therefore project points into calibrated cameras and attach features from multiple layers from a frozen DINOv3. This simple addition substantially boosts accuracy over the baseline.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Scaling 3D World Models: A Roadmap", "weight": 1.0} -->

Model size scaling is necessary to ingest large-scale world modeling data. With architecture, objective, and features in place, we expand depth and width within the same PTv3 blueprint. Aligned with scaling-law observations in vision and language modeling, scaling model size from 50M to 1B parameters yields smooth, log-linear gains (Figure 9) similarly for 3D world modeling.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Scaling 3D World Models: A Roadmap", "weight": 1.0} -->

Taken together, all these levers---backbone, training objective, pre-trained feature, and model scaling---yield substantial gains over the original GBND baseline.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Ablations", "weight": 1.0} -->

Representing actions as point flows on grippers balances effective, efficient contact reasoning and enables positive transfer across heterogeneous embodiments. In PointWorld, robot actions are dense point flows over grippers with $300$--$500$ points per gripper. We compare against four baselines: (i) whole-body point flows with the same number of points (sparser coverage), (ii) whole-body point clouds with $2000$ points (similar density as ours), (iii) 6-DoF end-effector pose and gripper openness, and (iv) joint positions and gripper openness. The last two low-dim variants omit robot points, which the flow-based models concatenate with scene features. We train all models jointly on both DROID and B1K data, where DROID uses a single-arm Franka and B1K uses a bimanual humanoid. Results are in Figure 11. On B1K, representing contact spatially lets point-flow actions outperform low-dim alternatives (end-effector poses and joint positions). Sparse whole-body flows underperform gripper-only flows, likely due to insufficient resolution to capture precise contact.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Ablations", "weight": 1.0} -->

Dense whole-body flows help but still lag behind, as gradients must pass through inactive points and incur compute overhead. On real-world DROID, both whole-body point-flow baselines underperform low-dim baselines. A plausible explanation is that extensive robot points obscure already-sparse learning signals from noisy real-world data. Gripper-only flows address this issue and attain the best performance, underscoring their effectiveness on real-world data and their ability to obtain positive transfer across heterogeneous embodiments in both domains.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Ablations", "weight": 1.0} -->

Using chunked prediction in both training and inference reduces rollout drift while improving compute efficiency. PointWorld performs 10-step chunked prediction (equivalent to 1 second). We ablate this design choice against two autoregressive baselines: (i) teacher-forcing (GT input each step) and (ii) self-feeding with $10$k warmup steps, plus sliding-window inference ($W{=}1,5$) using the same chunked model. Results are shown in Figure 12. Teacher-forcing outperforms self-feeding when training and inference strategies are aligned. Evaluating a chunk-trained model with $W{=}1$ (equivalent to self-feeding) incurs the strongest performance degradation; $W{=}5$ recovers some accuracy but degrades after the trained window. Matching chunked prediction in training and testing over the full horizon minimizes drift while amortizing compute with only a single forward pass (vs. 2--10 for autoregressive), highlighting chunking as both more accurate and more compute-efficient design choice.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Ablations", "weight": 1.0} -->

PointWorld is robust to different levels of partial observability and benefits from additional cameras in both training and inference. We train four variants that differ only in camera count for RGB-D observations: one, two, three, or a random draw of up to three cameras. We then evaluate all models on three settings with up to three cameras. Results are in Figure 13. Error on moving points stays sub-centimeter with negligible standard errors, but using more cameras at train time consistently reduces error at test time. Interestingly, models trained with fixed camera count perform better when more cameras are available at inference. The random-view model is most robust across all test camera counts, suggesting that exposure to varied observability helps the model infer objectness and physical properties under partial observability at inference time.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Ablations", "weight": 1.0} -->

Prediction error decreases roughly log-linearly with both model size and data. Inspired by scaling laws from language and vision, we test whether PointWorld follows similar trends. On DROID, we vary model capacity (50M--1B) and data fraction (5%--100%). Each curve sweeps one axis only. In log space we observe approximately linear behavior for both axes (Figure 9), suggesting predictable gains from extra data and capacity.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Generalization and Transfer", "weight": 1.0} -->

We study PointWorld's generalization across in-domain, cross-domain, and to held-out real-world environments under zero-shot and finetuned settings. Each finetuning uses $1/20$ of the original training iterations. Results are in Table 2.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Generalization and Transfer", "weight": 1.0} -->

PointWorld generalizes within domains. We study in-domain transfer on held-out splits of DROID and B1K that are unseen during training. On B1K the model achieves sub-centimeter mover error on held-out trajectories, while DROID performance on held-out remains similar to training despite real-world variations. This indicates that PointWorld does not simply memorize training samples.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Generalization and Transfer", "weight": 1.0} -->

Pre-trained PointWorld can be efficiently finetuned (20x fewer updates) for both real-to-sim and sim-to-real transfer. We study cross-domain transfer by evaluating how a model pre-trained on DROID generalizes to B1K, and vice versa. Zero-shot transfer between simulation and real domains remains challenging. Yet, finetuning with only $5\%$ of the original training steps rapidly narrows the gap to domain-specific models trained from scratch using $20\times$ more updates. The effect is symmetric: real-to-sim and sim-to-real transfers both benefit. Empirically, we observe training on real-world data provide better transfer than reverse, plausibly due to the higher scene diversity of the real-world data.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Generalization and Transfer", "weight": 1.0} -->

PointWorld zero-shot generalizes to unseen real-world environments, surpasses specialists if finetuned with 20x fewer updates, and benefits from real-sim co-training. To study held-out real generalization, we hold out data from the CLVR lab within DROID and evaluate how well a model pre-trained on the remaining DROID data generalizes to that lab. The held-out set is split into $90\%$ train and $10\%$ test. Zero-shot models never see these frames, while finetuned variants access only the $90\%$ subset. PointWorld pre-trained on the remaining DROID data achieves on-par performance with specialists trained on the held-out lab despite changes in background, lighting, object, and possibly motion distribution. With finetuning, it quickly surpasses the specialist. We observe simulation-pretrained models do not outperform scratch baselines yet reach comparable accuracy with finetuning. Finally, a model pre-trained on combined DROID and B1K mix delivers mildly stronger zero-shot performance than DROID-only.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Model-Based Planning with PointWorld", "weight": 1.0} -->

Pre-trained on diverse interactions, we test whether PointWorld can be zero-shot deployed for manipulation on a physical robot in the wild. For evaluation, we use a Franka setup similar to DROID, mounted on a wheeled base and equipped with one RealSense D435 camera. Depth is estimated using FoundationStereo. For each task, we manually draw an object mask and specify target positions through a GUI tool. Each optimization rolls out 30 steps (3 autoregressive forward passes). With only the pre-trained model and a shared MPC framework, PointWorld optimizes actions for real‑world tasks: non‑prehensile pushing of rigid objects (tissue box, book), deformable manipulation (folding a scarf, placing a pillow), articulated manipulation (opening a microwave and closing a drawer, with revolute and prismatic joints), and tool use (sweeping with a duster or broom).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Model-Based Planning with PointWorld", "weight": 1.0} -->

Tasks and success rates are shown in Figure 8, indicating the pre-trained PointWorld captures transferable interaction dynamics, including contact reasoning under partial observability (rigid pushing), implicitly inferring articulation and deformation of objects (articulated and deformable manipulation), and object-object interactions (tool use).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced PointWorld, a large pre-trained 3D world model, that predicts 3D environment dynamics given in-the-wild RGB-D capture(s) and robot actions under a shared representation of 3D point flows. To train the model, we leveraged recent advances in 3D vision and curated a large-scale dataset for action-conditioned 3D world modeling, with high-quality depth maps, camera poses, and 3D tracks. Through empirical evaluations, we rigorously studied the recipe for scaling 3D world model training, including backbone designs, action representations, learning objectives, partial observability, data mixtures, domain transfers, and scaling laws. Pre-trained on diverse data, a single PointWorld model enabled practical manipulation behaviors in the real world, including non-prehensile pushing, deformable and articulated object manipulation, and tool use.
