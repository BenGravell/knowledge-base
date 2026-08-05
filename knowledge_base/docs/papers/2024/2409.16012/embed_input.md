<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

PRESTO: Fast Motion Planning Using Diffusion Models Based on Key-Configuration Environment Representation

Topics include PRESTO, Motion planning, Diffusion, Diffusion models, Trajectory optimization, Collision-free.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce a learning-guided motion planning framework that generates seed trajectories using a diffusion model for trajectory optimization. Given a workspace, our method approximates the configuration space (C-space) obstacles through an environment representation consisting of a sparse set of task-related key configurations, which is then used as a conditioning input to the diffusion model. The diffusion model integrates regularization terms that encourage smooth, collision-free trajectories during training, and trajectory optimization refines the generated seed trajectories to correct any colliding segments. Our experimental results demonstrate that high-quality trajectory priors, learned through our C-space-grounded diffusion model, enable the efficient generation of collision-free trajectories in narrow-passage environments, outperforming previous learning- and planning-based baselines.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning involves finding a smooth and collision-free path in a high-dimensional configuration space (C-space). Classical motion planning algorithms typically use either sampling-based methods[lavalle1998rapidly, lavalle2001rapidly, kavraki1996probabilistic] or optimization-based methods[ratliff2009chomp, schulman2014motion]to address motion planning across various domains. However, in high-dimensional C-spaces with narrow passages, sampling-based methods incur high computational costs due to large search spaces and small volume of solutions. While optimization-based methods can serve as an alternative, such methods are sensitive to initialization and may become stuck in local optima, often failing to find a feasible path. Consequently, both approaches have limitations when dealing with complex motion planning problems under restricted computational resources.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent works leverage generative models to directly learn trajectory distributions instead [janner2022planning, huang2023diffusion, carvalho2023motion]. By casting motion planning as sampling from a learned distribution, these models can efficiently generate trajectories within a consistent computational budget. However, they often struggle to generalize to new, complex C-spaces, resulting in high collision rates in the generated trajectories, because most of these approaches use the workspace as input to neural networks instead of the C-space. Instead, we propose representing the environment in terms of key configurations[kim2019adversarial], a sparse set of task-related configurations from prior motion planning data. The resulting model no longer needs to learn a generalizable mapping between workspace and C-space obstacle representations, improving generalization and reducing training complexity.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

PRESTO aims to generate collision-free trajectories in complex, unseen C-spaces. First, we approximate these C-spaces using key configurations from prior data and generate trajectories based on this representation. A conditional diffusion model, trained with a motion planning loss, provides initial solutions that are subsequently refined through trajectory optimization.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another challenge is designing a training objective for generative models tailored to motion planning.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Existing diffusion models for motion planning use DDPM-based losses[ho2020denoising,janner2022planning,carvalho2023motion] that focus on reconstruction quality[saharia2022imagen]. However, this reconstruction objective does not account for underlying task constraints, resulting in degraded performance on tasks that require precise outputs and complex constraints[giannone2023aligning]. To overcome this, we incorporate TrajOpt-inspired motion-planning costs[schulman2014motion]directly into the training pipeline of a diffusion model, minimizing trajectory-optimization costs associated with collision avoidance and trajectory smoothness. As a result, the model learns to generate smooth and collision-free trajectories. Further, to ensure that generated trajectories satisfy hard constraints such as collision avoidance, we feed the diffusion model's outputs as initial solutions for subsequent trajectory optimization.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Trajectory generation pipeline of PRESTO. We obtain the environment representation for an unseen problem by checking the collision states at the key configurations used during training. Using the trained conditional diffusion model, we generate multiple trajectories conditioned on this representation and then select the least-colliding trajectory after post-processing.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We name our unified framework PRESTO (Planning with Environment Representation, Sampling, and Trajectory Optimization). Figure[fig:header] summarizes our framework: 1) an environment representation based on key configurations (blue block); 2) a training pipeline for a diffusion model that directly integrates motion-planning costs (green block); and 3) a diffusion-based sampling-and-optimization framework for motion planning, where the diffusion model provides initial trajectories for trajectory optimization (orange block). We evaluate PRESTO in simulated environments where a robot operates in a fixed scene populated with randomly shaped and arranged objects. The results show that the synergy between the high-quality trajectory priors generated by our diffusion model and the trajectory optimization post-processing efficiently generates collision-free trajectories in narrow passages within a limited computational budget.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Description", "weight": 1.0} -->

\(\mathcal{C}\) be a \(d\)-dimensional C-space, which is divided into two subspaces: \(\mathcal{C}\_o\) representing C-space obstacles, and \(\mathcal{C}\_f = \mathcal{C} \setminus \mathcal{C}\_o\) representing the collision-free C-space. We denote the robot's configuration as a \(d\)-dimensional vector \(q \in \mathcal{C}\). A trajectory is represented as a sequence of waypoint configurations \(\tau = (q\_0, q\_1, \ldots, q\_T)\). Given the start configuration $q_s$ and goal configuration $q_g$, the objective of motion planning is to find a collision-free path \(\tau \in \mathcal{C}\_f\) from $q_s$ to $q_g$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Description", "weight": 1.0} -->

In this work, we assume that we are provided with a dataset $\mathcal{D}=\{\mathcal{D}_m\}_{m=1}^{M}$ obtained from solving $M$ past planning problems, where each data point $\mathcal{D}_m=\{q_s, q_g, \tau, \mathcal{G}\}$ consists of a start configuration $q_s$, a goal configuration $q_g$, a trajectory $\tau$, and an environment geometry $\mathcal{G}$. We assume consistent environment fixtures but varying object shapes and locations across problems. We use an optimization-based planner to compute ground-truth trajectories for training data. Our goal is to develop a generative model that provides a good initial solution for trajectory optimization, even in environments with unseen obstacles and their arrangements.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Method", "weight": 1.0} -->

PRESTO comprises of three key components, illustrated in Figure[fig:header]. First, we generate a set of key configurations and their collision states from the motion planning dataset. Based on the resulting representation, we train a conditional diffusion model that incorporates motion-planning costs to guide the model toward smooth and collision-free trajectories. Finally, we feed the trajectories generated by the diffusion model to trajectory optimization. Each component of our framework is detailed in the following sections.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Environment Representation", "weight": 1.0} -->

We represent the environment as an approximation of its C-space using a collection of key configurations selected from the dataset. We denote the set of key configurations as \(\{\overline{q}^k\}\_{k=1}^K\), where the number of key configurations \(K\) determines the resolution of the environment's C-space approximation A larger $K$ increases the resolution of the C-space approximation, but it also raises the computational overhead at query time.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Environment Representation", "weight": 1.0} -->

For each motion planning problem, we compute the environment representation $\phi \in \{0, 1\}^{K}$ as a binary vector that specifies the collision states of each key configuration. In our setups, we use $K=1025$. [algo:key-config] describes our procedure for generating key configurations, which is a modified version of the algorithm originally proposed by Kim et al.[kim2018aaai]. It takes the dataset $\mathcal{D}$ and the hyperparameters ${d_q^{\text{min}}, d_x^{\text{min}}, c, K}$. Here, $d_q^{\text{min}}$ denotes the minimum C-space distance between key configurations, $d_x^{\text{min}}$ represents the minimum workspace distance for end-effector tips, and $c$is the bound on the proportion of environments where a key configuration is occupied.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Environment Representation", "weight": 1.0} -->

We initialize the key configuration set as an empty set (line 1) and sample new configurations until the target size is reached (lines 2-11). At each step, a configuration is uniformly sampled from $\mathcal{D}$ (lines 3-4) and filtered based on three conditions (lines 5-10). To avoid duplicates, we ensure the new configuration is sufficiently distant from existing ones in both C-space and workspace (lines 5-6), while also limiting the proportion of collision states across different environments to prioritize informative configurations By limiting the proportion of collision states, we filter out configurations that never result in collisions, as they provide no meaningful information about the environment If all criteria are met, the configuration is added to the buffer (lines 8-10). This process generates key configurations that effectively capture task-relevant C-space regions for motion planning.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Training Conditional Diffusion Modelssec:train", "weight": 1.0} -->

Figure[fig:pipeline] (bottom) illustrates our model architecture, which is based on the Diffusion Transformer (DiT)[Peebles2022DiT]. Our model takes as inputs the current diffusion step $i$, the noisy trajectory at the $i$-th step $\tau_{i}$, the environment representation $\phi$, and the start and goal joint configurations $q_{s}$ and $q_{g}$. We use v-prediction[salimans2022vpred] during inference to enhance sample quality[saharia2022imagen].

<!-- chunk {"id": "body-0017", "role": "body", "section": "Training Conditional Diffusion Modelssec:train", "weight": 1.0} -->

To process the inputs, the trajectory $\tau_{i}$ is first patchified and tokenized by an MLP, as in DiT[Peebles2022DiT]. The diffusion step $i$ and the start and goal configurations $q_s$ and $q_g$ are mapped to high-dimensional frequency embeddings[Peebles2022DiT] to capture small changes. The embedded trajectory patches are given as input tokens to the transformer, while $i$, $\phi$, $q_s$, and $q_g$are incorporated as conditioning inputs to align sampled trajectories with the current scene and endpoint constraints.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Training Conditional Diffusion Modelssec:train", "weight": 1.0} -->

The DiT comprises six transformer blocks to process the trajectories, where each block incorporates Adaptive Layer Normalization (AdaLN) [Peebles2022DiT] that transforms the output features based on the conditioning inputs. In AdaLN, a separate MLP maps conditioning inputs to the transform parameters as ${\gamma, g, b} = \text{MLP}({i, \phi, q_s, q_g})$, applied to the output $x$ as $\hat{x} = x + \gamma \odot ((1 + g) \odot \text{LN}(x) + b)$, where $\text{LN}(x)$ denotes layer normalization and $\odot$denotes element-wise multiplication. This allows the model to adjust its output based on the current scene and the diffusion iteration.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Training Conditional Diffusion Modelssec:train", "weight": 1.0} -->

Training with Motion-Planning Costs Our training objective includes three terms: Diffusion Loss, Collision Loss, and Smoothing Loss. While Diffusion Loss implements the standard reconstruction objective used in diffusion models, we add Collision Loss and Smoothing Loss to encourage the model to learn the motion planning constraints.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Training Conditional Diffusion Modelssec:train", "weight": 1.0} -->

- Diffusion Loss: This term $\mathcal{L}_{\text{diffusion}}$ represents the standard loss function used for training conditional diffusion models based on the DDPM framework. - Collision Loss: Inspired by TrajOpt[schulman2014motion], this term encourages the model to generate trajectories that maintain a safe distance from objects and other links.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Training Conditional Diffusion Modelssec:train", "weight": 1.0} -->

The first term accounts for the collision between the $i$-th link $\mathcal{A}_i$ and the $j$-th obstacle $\mathcal{O}_j$, while the second term denotes self-collision among different links $\mathcal{A}_i$ and $\mathcal{A}_j$, where $i \neq j$. - Smoothing Loss: This term penalizes the L2-norm between adjacent configurations, defined as $ \mathcal{L}_{\text{smooth}} = \sum_{t} \left\| q_{t} - q_{t-1} \right\|^2$. It regulates the distances between consecutive configurations to encourage shorter and smoother trajectories for the robot.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Training Conditional Diffusion Modelssec:train", "weight": 1.0} -->

We use a weighted sum of the loss terms to train our model: $\mathcal{L} = w_1 \mathcal{L}_{\text{diffusion}} + w_2 \mathcal{L}_{\text{coll}} + w_3 \mathcal{L}_{\text{smooth}}$, with $w_1=1.0$, $w_2=0.05$, and $w_3=0.005$. While the model is not highly sensitive to these values, $w_2$is kept small for stable training.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Trajectory Generation", "weight": 1.0} -->

Figure[fig:pipeline] (top) provides an overview of our trajectory generation process. The inputs ${q_s, q_g, \phi}$ specify the motion planning problem, where $q_s$ and $q_g$ are the start and goal configurations, and $\phi$ is the environment representation from the key configurations' collision states. During denoising, we use batch sampling to leverage GPU parallelization, enhancing the likelihood of finding collision-free trajectories among the diffusion model’s stochastic outputs. Our sampling follows the Denoising Diffusion Implicit Model[song2020denoising], which accelerates the process by using fewer denoising iterations during inference than during training. We then apply trajectory optimization to post-process the sampled trajectories and select the one with the lowest collision cost.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Trajectory Generation", "weight": 1.0} -->

We detail our trajectory generation in Algorithm First, we compute the environment representation $\phi$ by checking the collision states of the key configurations ${\overline{q}}$ (line 1). Next, we initialize the denoising process with a batch of random noise $\tau_N$ sampled from an isotropic Gaussian distribution (line 2). At each of the $N$ iterations, we predict a denoised trajectory $\tau_{i-1}$ from $\tau_i$, conditioned on $\phi$ and the current step $i$ (line5), and then apply endpoint constraints to ensure connectivity between the start $q_s$ and the goal $q_g$, as in Diffuser[janner2022planning] (line6). The resulting trajectories $\tau_{\text{seed}}$ provide initialization for post-processing (line 9). In our experiments, we denoise $B=4$ trajectories over $N=64$iterations.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Trajectory Generation", "weight": 1.0} -->

In the post-processing phase, we refine the sampled trajectories using a fixed number of trajectory optimization iterations [schulman2014motion] to address potential collisions (line 10). To accelerate this process, we employ cuRobo[sundaralingam2023curobo], which can batch-process the trajectories while eliminating data exchange across devices. Afterward, we select the trajectory with the fewest collisions (line 11).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

We evaluate our method on a motion planning task in which the Franka Emika Panda robot arm[franka-panda] traverses a 3-tier shelf with various objects in simulation (Figure[fig:benchmark], top).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

We report the success rate (%), the collision rate (%), and the penetration depth (m) across 180 problems. (Top) The evaluation environments feature consistent 3-tier shelf fixtures with randomized object positions that vary across levels. (Bottom) We show PRESTO's performance changes across domains and computational budgets compared to the baselines.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Our training domain consists of 5,000 environments, where 1-6 objects (cuboid, cylinder, sphere) are placed in random poses within each shelf slot. For each scene, we first sample collision-free initial and target joint positions within the workspace and then generate motion plans via cuRobo[sundaralingam2023curobo]. We collect a total of 50,000 environment-trajectory pairs (trajectory length $T = 1000$) annotated with key-configuration labels as in Algorithm[algo:key-config].

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

While the evaluation domain is generated using a similar procedure, we partition the dataset into four difficulty levels, each consisting of 180 problems. This helps assess the performance of PRESTOand the baselines on unseen scenes of varying complexity.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

The shelf is empty, as shown in Figure[fig:benchmark] (top left). Although the environment remains consistent, the task is challenging due to the shelf’s non-convex workspace and the need to connect random start and goal configurations. - Level 2-3: Each slot contains one object for Level 2 and two objects for Level 3, adding complexity to the C-space and requiring environment-conditional collision-free trajectory generation, as shown in Figure[fig:benchmark] (top center). - Level 4: Each slot contains 3-4 objects, as shown in Figure[fig:benchmark] (top right). These environments are the most challenging due to narrow passages between obstacles, increased C-space complexity, and slower collision-checking and distance calculations among many objects.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

- Success rate: the percentage of collision-free trajectories within the batch. Higher is better. - Collision rate: the average fraction of colliding segments in each trajectory. This metric reflects the likelihood that each joint configuration is collision-free, even if collisions occur elsewhere in the trajectory. - Penetration depth: the average maximum penetration depth in each trajectory. This metric quantifies the severity of collision, measuring worst-case deviation from a collision-free trajectory.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

To systematically evaluate how performance changes across different computational budgets, we vary the number of optimization iterations during post-processing. The Bi-RRTbaseline was evaluated on an AMD Ryzen 9 5900X and all other baselines were evaluated on an NVIDIA A5000.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Ablation study results. We report the success rate (%), the collision rate (%), and the penetration depth (m) averaged across 180 problems for PRESTO and the self-variant baselines. (Left) We show performance changes with varying post-processing iterations. (Right) We present the performance of trajectories directly generated by the diffusion models without post-processing.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Quantitative Evaluation", "weight": 1.0} -->

In our experiments, we evaluate the following claims: Diffusion models using key-configuration representations generalize better to unseen environments than those using point-cloud representations. Incorporating motion-planning costs into diffusion-model training enables models to better learn task constraints like collision avoidance than when using only the reconstruction-based objective. By seeding trajectories, our method outperforms pure planners in computational efficiency and learning-based approaches in trajectory quality.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Quantitative Evaluation", "weight": 1.0} -->

To validate our claims, we compare our model's performance against the following baselines, representative of each approach, as presented in Figure [fig:benchmark] (bottom). a pure planner based on LaValle et al.[lavalle2001rapidly], specifically RRT-connect[kuffner2000rrt]. Bi-RRT searches bidirectionally by growing random trees from both start and goal configurations to find collision-free paths in an unknown C-space. Although it is probabilistically complete, it empirically struggles with slow searches in narrow passages. Since its success rate depends on the provided time, we evaluate its performance across different search timeouts. a pure planner from Schulman et al.[schulman2014motion] that optimizes trajectories using a hinge penalty for collisions and configuration distances. The optimization scheme in TrajOpt is the same as in PRESTO, without the initial seed from our diffusion model. We use a GPU-accelerated implementation from cuRobo[sundaralingam2023curobo] and control the computational budget by adjusting optimization iterations.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Quantitative Evaluation", "weight": 1.0} -->

a baseline from Huang et al.[huang2023diffusion] uses a conditional diffusion model for trajectory planning through sampling. Unlike PRESTO, this baseline conditions on point-cloud inputs encoded by Point Transformer[zhao2021point] instead of a C-space representation. We use the author's original network implementation, trained on our dataset. - Motion Planning Diffusion (MPD): a baseline from Carvalho et al.[carvalho2023motion] uses a diffusion model for trajectory planning through sampling. Unlike PRESTO, MPD employs unconditional diffusion models and relies on sampling guidance for trajectory constraints such as collision avoidance or connecting start and goal configurations. We adapt their network to our setup and training dataset.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Quantitative Evaluation", "weight": 1.0} -->

Comparison to Pure Learning Algorithms We consider pure learning algorithms, SceneDiffuser and MPD, which neither use a key-configuration environment representation (Claim 1) nor a motion-planning objective for training diffusion models (Claim 2). We evaluate each baseline's diffusion model performance without trajectory optimization post-processing, as indicated by the large black, yellow, and purple dots in Figure[fig:benchmark] corresponding to PRESTO, SceneDiffuser, and MPD. PRESTO consistently outperforms both across all levels. For example, in Level 3, PRESTO achieves a 52.2% success rate, while SceneDiffuser and MPD achieve only 0.6% and 12.2%, respectively.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Quantitative Evaluation", "weight": 1.0} -->

Comparison to Pure Planners Compared to Bi-RRT, PRESTO uses diffusion-learned trajectory priors to generate collision-free trajectories more efficiently, especially in narrow passages. In Level 4, PRESTO achieves a 90% success rate in 1.0 second, compared to 2.3 seconds for Bi-RRT. Furthermore, as environment complexity increases, Bi-RRT struggles to find valid segments, widening the success gap from 97.8% vs. 70.6% in Level 1 to 90.6% vs. 46.7% in Level 4 under a 1-second computational budget. Next, we consider TrajOpt, an optimization-based method. Despite PRESTO's computational overhead for running the diffusion model, its high-quality initial trajectories lead to faster convergence in complex domains (Claim 3). For example, in Level 2, PRESTO achieves a 97.2% success rate in 1.0 second despite an initial overhead of 0.2 seconds, while TrajOpt remains below 60% in the same time.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Quantitative Evaluation", "weight": 1.0} -->

The success rate gap with a 1-second computational budget grows from 26.7% in Level 1 to 37.3% in Level 4, demonstrating PRESTO's effectiveness in complex environments.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Ablation Studiessec:ablation", "weight": 1.0} -->

To analyze the impact of our contributions and discuss the claims from Section[sec:main\_results], we conduct ablation studies using variants of our method, with results shown in Figure[fig:ablation]. Additional studies are available on our project website.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Ablation Studiessec:ablation", "weight": 1.0} -->

- Point-Cloud Conditioning: To validate Claim 1, we train a variant of PRESTO conditioned on an equivalent number of workspace point clouds instead of key configurations. We use a patch-based transformer[yu2021pointbert] to encode the point clouds, keeping the rest of the architecture unchanged. - Training Without TrajOpt: To validate Claim 2, we train a variant of PRESTO without motion-planning costs (Collision Loss and Distance Loss). The rest of the architecture remains unchanged.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Ablation Studiessec:ablation", "weight": 1.0} -->

Generalization of Key-Configuration Representation (Claim 1) Compared to PRESTO, Point-Cloud Conditioning exhibits performance degradation across problem levels and post-processing iterations: collision rates and penetration depth remain higher, and worsen with increased problem complexity. For instance, in Level 1-2, PRESTO outperforms Point-Cloud Conditioning by 1.4% in success rate, 0.3% in collision rate, and 0.001m in penetration depth. In Level 3-4, the gaps increase to 3.6%, 1.4%, and 0.013m. This highlights the advantage of using C-space representations over point-cloud-based conditioning in complex scenes.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Ablation Studiessec:ablation", "weight": 1.0} -->

Efficacy of Training with Motion-Planning Costs (Claim 2) Compared to PRESTO, Training Without TrajOpt exhibits performance degradation across all levels. Though less severe than Point-Cloud Conditioning, the trend is consistent: for example, in Level 1-2, PRESTO outperforms Training Without TrajOpt by an average of 1.81% in success rate and 0.2% in collision rate. In Level 3-4, the performance gap increases to 2.7% in success rate and 0.7%in collision rate. This shows that incorporating motion-planning costs for training diffusion models improves trajectory quality across various domains.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Ablation Studiessec:ablation", "weight": 1.0} -->

Efficacy of Post-Processing (Claim 3) We observe that applying trajectory optimization during post-processing improves performance across all levels. Additionally, we validate that the success of PRESTO is largely due to the high-quality, nearly collision-free initial trajectories obtained from our diffusion model. As shown in Figure[fig:ablation] (right), PRESTO in Level 4 outperforms Point-Cloud Conditioning by achieving a much smaller penetration depth (0.037 m vs. 0.123 m), despite similar initial success rates (51.1% vs. 47.2%), leading to faster convergence during trajectory optimization.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We present PRESTO, a learning-guided motion planning framework that integrates diffusion-based trajectory sampling with post-processing trajectory optimization. Incorporating C-space environment representations based on key configurations and a motion-planning training objective, our framework efficiently generates collision-free trajectories in unseen environments. Simulated experiments demonstrate the efficacy of our framework compared to both diffusion-based planning approaches and conventional motion planning methods. In this work, we assumed known environment geometry for ground-truth collision states at key configurations. Future work could extend the framework to handle partial observability of unseen geometries.
