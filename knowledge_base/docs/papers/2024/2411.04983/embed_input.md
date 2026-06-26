<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

DINO-WM: World Models on Pre-trained Visual Features Enable Zero-shot Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The ability to predict future outcomes given control actions is fundamental for physical reasoning. However, such predictive models, often called world models, remains challenging to learn and are typically developed for task-specific solutions with online policy learning. To unlock world models' true potential, we argue that they should 1) be trainable on offline, pre-collected trajectories, 2) support test-time behavior optimization, and 3) facilitate task-agnostic reasoning. To this end, we present DINO World Model (DINO-WM), a new method to model visual dynamics without reconstructing the visual world. DINO-WM leverages spatial patch features pre-trained with DINOv2, enabling it to learn from offline behavioral trajectories by predicting future patch features. This allows DINO-WM to achieve observational goals through action sequence optimization, facilitating task-agnostic planning by treating goal features as prediction targets.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We demonstrate that DINO-WM achieves zero-shot behavioral solutions at test time on six environments without expert demonstrations, reward modeling, or pre-learned inverse models, outperforming prior state-of-the-art work across diverse task families such as arbitrarily configured mazes, push manipulation with varied object shapes, and multi-particle scenarios.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robotics and embodied AI have seen tremendous progress in recent years. Advances in imitation learning and reinforcement learning have enabled agents to learn complex behaviors across diverse tasks. Despite this progress, generalization remains a major challenge. Existing approaches predominantly rely on policies that, once trained, operate in a feed-forward manner during deployment---mapping observations to actions without any further optimization or reasoning. Under this framework, successful generalization inherently requires agents to possess solutions to all possible tasks and scenarios once training is complete, which is only possible if the agent has seen similar scenarios during training. However, it is neither feasible nor efficient to learn solutions for all potential tasks and environments in advance.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Instead of learning the solutions to all possible tasks during training, an alternate is to fit a dynamics model on training data and optimize task-specific behavior at runtime. These dynamics models, also called world models, have a long history in robotics and control. More recently, several works have shown that world models can be trained on raw sensory data. This enables flexible use of model-based optimization to obtain policies as it circumvents the need for explicit state-estimation. Despite this, significant challenges remains in its use for solving general-purpose tasks.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To understand the challenges in world modeling, let us consider the two broad paradigms in learning world models: online and offline. In the online setting, access to the environment is often required so data can be continuously collected to improve the world model, which in turn improves the policy and the subsequent data collection. However, the online world model is only accurate in the cover of the policy that was being optimized. Hence, while it can be used to train powerful task-specific policies, it requires retraining for every new task even in the same environment. Instead, in the offline setting, the world model is trained on an offline dataset of collected trajectories in the environment, which removes its dependence on the task specificity given sufficient coverage in the dataset. However, when required to solve a task, methods in this domain require strong auxiliary information which can take the form of expert demonstrations, structured keypoints, access to pretrained inverse models or dense reward functions, all of which reduce the generality of using offline world models. The central question to building better offline world models is if there is alternate auxiliary information that does not compromise its generality?

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we present DINO-WM, a new and simple method to build task-agnostic world models from an offline dataset of trajectories. DINO-WM models the world dynamics on compact embeddings of the world, rather than the raw observations themselves. For the embedding, we use pretrained patch-features from the DINOv2 model, which provides both a spatial and object-centric representation prior. We conjecture that this pretrained representation enables robust and consistent world modeling, which relaxes the necessity for task-specific data coverage. Given these visual embeddings and actions, DINO-WM uses the ViT architecture to predict future embeddings. Once this model is trained on the offline dataset, planning to solve tasks is constructed as visual goal reaching, i.e. to reach a future desired goal given the current observation. Since the predictions by DINO-WM are high quality (see Figure 4), we can simply use model predictive control with inference-time optimization to reach desired goals without any extra information during testing.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

DINO-WM is experimentally evaluated on six environment suites spanning maze navigation, sliding manipulation, robotic arm control, and deformable object manipulation tasks. Our experiments reveal the following findings: DINO-WM produce high-quality future world modeling that can be measured by improved visual reconstruction from trained decoders. On LPIPS metrics for our hardest tasks, this improves upon prior state-of-the-art work by 56% (See Section 4.7).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Given the latent world models trained using DINO-WM, we show high success for reaching arbitrary goals on our hardest tasks, improving upon prior work by 45% on average (See Section 4.3).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

DINO-WM can be trained across environment variations within a task family (e.g. different maze layouts for navigation or different object shapes for manipulation) and achieve higher rates of success compared to prior work (See Section 4.5).

<!-- chunk {"id": "body-0011", "role": "body", "section": "DINO World Models", "weight": 1.0} -->

Overview and Problem formulation: Our work follows the vision-based control task framework, which models the environment as a partially observable Markov decision process (POMDP). The POMDP is defined by the tuple $(\mathcal{O},\mathcal{A},p)$, where $\mathcal{O}$ represents the observation space, and $\mathcal{A}$ denotes the action space. The dynamics of the environment is modeled by the transition distribution $p{({o_{t + 1} \mid {o_{\leq t},a_{\leq t}}})}$, which predicts future observations based on past actions and observations.

<!-- chunk {"id": "body-0012", "role": "body", "section": "DINO World Models", "weight": 1.0} -->

In this work, we aim to learn task-agnostic world models from precollected offline datasets, and use these world models to perform visual reasoning and control at test time. At test time, our system starts from an arbitrary environment state and is provided with a goal observation in the form of an RGB image, in line with prior works, and is asked to perform a sequence of actions $a_{0},\ldots,a_{T}$ to reach the goal state. This approach differs from the world models used in online reinforcement learning (RL) where the objective is to optimize the rewards for a fixed set of tasks at hand, or from text-conditioned world models, where the goals are specified through text prompts.

<!-- chunk {"id": "body-0013", "role": "body", "section": "DINO-based World Models (DINO-WM)", "weight": 1.0} -->

We model the dynamics of the environment in the latent space. More specifically, at each time step $t$, our world model consists of the following components: where the observation model encodes image observations to latent states $z_{t}$, and the transition model takes in a history of past latent states of length $H$. The decoder model takes in a latent $z_{t}$, and reconstructs the image observation $o_{t}$. We use $\theta$ to denote the parameters of these models. Note that our decoder is entirely optional, as the training objectives for the decoder is independent for training the rest part of the world model. This eliminates the need to reconstruct images both during training and testing, which reduces computational costs compared to otherwise coupling together the training of the observational model and the decoder, as. We ablate and show the effectiveness of this choice in Appendix A.4.3.

<!-- chunk {"id": "body-0014", "role": "body", "section": "DINO-based World Models (DINO-WM)", "weight": 1.0} -->

DINO-WM models only the information available from offline trajectory data in an environment, in contrast to recent online RL world models that also require task-relevant information, such as rewards, discount factors, and termination conditions.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Observation Model", "weight": 1.0} -->

To learn a generic world model across many environments and the real world, we argue that the observation model should 1) be task and environment independent, and 2) capture rich spatial information for navigation and manipulation. Contrary to previous works where the observation model is always learned for the task at hand, we argue instead that it can be inefficient and often not possible to learn a good observation model from scratch when facing a new environment, as perception is a general task that benefits from large-scale internet data. Therefore, we use the pre-trained DINOv2 model as our world model's observation model, leveraging its strong spatial understanding for tasks like object detection, semantic segmentation, and depth estimation. The observation model remains frozen during training and testing. At each time step $t$, it encodes an image $o_{t}$ to patch embeddings $z_{t} \in {\mathbb{R}}^{N \times E}$, where $N$ denotes the number of patches, and $E$ denotes the embedding dimension. This process is visualized in Figure 2.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Transition Model", "weight": 1.0} -->

We adopt the ViT architecture for the transition model due to its suitability for processing patch features. We remove the tokenization layer, as it operates on patch embeddings, effectively transforming it into a decoder-only transformer. We further make a few modifications to the architecture to allow for additional conditioning on proprioception and controller actions.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Transition Model", "weight": 1.0} -->

Our transition model takes in a history of past latent states $z_{{t - H}:{t - 1}}$ and actions $a_{{t - H}:{t - 1}}$, where $H$ is a hyperparameter denoting the context length of the model, and predicts the latent state at next time step $z_{t}$. To properly capture the temporal dependencies, where the world state at time $t$ should only depend on previous observations and actions, we implement a causal attention mechanism in the ViT model, enabling the model to predict latents autoregressively at a frame level. Specifically, each patch vector $z_{t}^{i}$ for the latent state $z_{t}$ attends to ${\{ z_{{t - H}:{t - 1}}^{i}\}}_{i = 1}^{N}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Transition Model", "weight": 1.0} -->

This is different from past work IRIS which similarly represents each observation as a sequence of vectors, but autoregressively predict $z_{t}^{i}$ at a token level, attending to ${\{ z_{{t - H}:{t - 1}}^{i}\}}_{i = 1}^{N}$ as well as ${\{ z_{t}^{i}\}}_{i = 1}^{< k}$. We argue that predicting at a frame level and treating patch vectors of one observation as a whole better captures global structure and temporal dynamics, modeling dependencies across the entire observation rather than isolated tokens, leading to improved temporal generalization. The effectiveness of this attention mask has been shown in our ablation experiments in Appendix A.4.2 To model the effect of the agent's action to the environment, we condition the world model's predictions on these actions.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Transition Model", "weight": 1.0} -->

Specifically, we concatenate the $K$-dimensional action vector, mapped from the original action representation using a multi-layer perceptron (MLP), to each patch vector $z_{t}^{i}$ for $i = {1,\ldots,N}$. When proprioceptive information is available, we incorporate it similarly by concatenating it to the observation latents, thereby integrating it into the latent states.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Transition Model", "weight": 1.0} -->

We train the world model with teacher forcing. During training, we slice the trajectories into segments of length $H + 1$, and compute a latent consistency loss on each of the $H$ predicted frames. For each frame, we compute where $\phi$ is the action encoder model that can map actions to higher dimensions. Note that our world model training is entirely performed in latent space, without the need to reconstruct the original pixel images.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Decoder for Interpretability", "weight": 1.0} -->

To aid in visualization and interpretability, we use a stack of transposed convolution layers to decode the patch representations back to image pixels, similar as. Given a pre-collected dataset, we optimize the parameters $\theta$ of the decoder $q_{\theta}$ with a simple reconstruction loss defined as: The training of the decoder is entirely independent of the transition model training, offering several advantages: 1) The decoder does not affect the world model's reasoning and planning capabilities for solving downstream tasks, and 2) There is no need to reconstruct raw pixel images during planning, thereby reducing computational costs. Nevertheless, the decoder remains valuable as it enhances the interpretability of the world model's predictions. While backpropagating this decoder loss to the predictor is possible, we ablate this choice and find that it negatively impacts performance compared to omitting the decoder loss. Full details are provided in Appendix A.4.3.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Visual Planning with DINO-WM", "weight": 1.0} -->

To evaluate the quality of the world model, we perform trajectory optimization at test time and measure performance. While the planning methods themselves are fairly standard, they serve as means to emphasize the quality of the world models. For this purpose, our world model receives the current observation $o_{0}$ and a goal observation $o_{g}$, both represented as RGB images. We formulate planning as the process of searching for a sequence of actions that the agent would take to reach $o_{g}$. We employ model predictive control (MPC), which facilitates planning by considering the outcomes of future actions.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Visual Planning with DINO-WM", "weight": 1.0} -->

We utilize the cross-entropy method (CEM) to optimize the sequence of actions at each iteration. The planning cost is defined as the mean squared error (MSE) between the current latent state and the goal's latent state, given by The MPC framework and CEM optimization procedure are detailed in Appendix A.5.1. Since our world model is differentiable, a possibly more efficient approach is to optimize this objective through gradient descent (GD), allowing the world model to directly guide the agent toward a specific goal. The details of GD are provided in Appendix A.5.2. However, we empirically observe that CEM outperforms GD in our experiments with full results in Appendix A.5.3. We hypothesize that incorporating regularizations during training and in the planning objectives could further improve performance, and leave this for future work.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experiments", "weight": 1.0} -->

Our experiments are designed to address the following key questions: 1) Can we effectively train DINO-WM using precollected offline datasets? 2) Once trained, can DINO-WM be used for visual planning? 3) To what extent does the quality of the world model depend on pre-trained visual representations? 4) Does DINO-WM generalize to new configurations, such as variations in spatial layouts and object arrangements? We train and evaluate DINO-WM across six environment suites (full description in Appendix A.1) and compare it to a variety of state-of-the-art world models that predict in either latent space or raw pixel space.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Environments and Tasks", "weight": 1.0} -->

We evaluate six environment suites with varying dynamics complexity, some of which are drawn from standard robotics benchmarks, such as D4RL and DeepMind Control Suite, as shown in Figure 3. These environments include maze navigation (Maze, Wall), fine-grained control for tabletop pushing (PushT) and robotic arm control (Reach), and deformable object manipulation with an XArm (Rope, Granular).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Environments and Tasks", "weight": 1.0} -->

In all environments, the task is to reach a randomly sampled goal state specified by a target observation, starting from arbitrary initial states. For PushT, target configurations are sampled to ensure feasibility within 25 steps. For Granular, targets require gathering all particles into a square with randomized locations and sizes. Observations in all environments are RGB images of size. A full description of the environments is provided in Appendix A.1.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Baselines", "weight": 1.0} -->

We compare DINO-WM with the following state-of-the-art models commonly used for control. For IRIS, DreamerV3, and TD-MPC2, we train the models with our offline datasets without any reward or task information, and perform MPC on the learned world model for solving downstream tasks.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Baselines", "weight": 1.0} -->

IRIS: IRIS encodes visual inputs into tokens via a discrete autoencoder and predicts future tokens using a GPT Transformer, enabling policy and value learning through imagination.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Baselines", "weight": 1.0} -->

DreamerV3: DreamerV3 encodes visual inputs into categorical representations, predicts future states and rewards, and trains an actor-critic policy from imagined trajectories.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Baselines", "weight": 1.0} -->

TD-MPC2: TD-MPC2 learns a decoder-free world model in latent space and uses reward signals to optimize the latents.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Baselines", "weight": 1.0} -->

AVDC: AVDC uses a diffusion model to generate task execution videos from an initial observation and textual goal. We provide qualitative evaluations and MPC planning results for an action-conditioned variant in Appendix A.6.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Optimizing Behaviors with DINO-WM", "weight": 1.0} -->

With a trained world model, we study if DINO-WM can be used for zero-shot planning directly in the latent space.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Optimizing Behaviors with DINO-WM", "weight": 1.0} -->

For Maze, Reach, PushT, and Wall environments, we sample 50 initial and goal states and measure the success rate across all instances. Due to the environment stepping time for the Rope and Granular environments, we evaluate the Chamfer Distance (CD) on 10 instances for them. In Granular, we sample a random configuration from the validation set, with the goal of pushing the materials into a square shape at a randomly selected location and scale.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Optimizing Behaviors with DINO-WM", "weight": 1.0} -->

As seen in Table 1, on simpler environments such as Wall and PointMaze, DINO-WM is on par with state-of-the-art world models like DreamerV3. However, DINO-WM significantly outperforms prior work at manipulation environments where rich contact information and object dynamics need to be accurately inferred for task completion. We notice that for TD-MPC2, the lack of reward signal makes it difficult to learn good latent representations, which subsequently results in poor performance. Visualizations of planning on all environments can be found in Appendix A.10.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Optimizing Behaviors with DINO-WM", "weight": 1.0} -->

Does DINO-WM learn better environment dynamics as more data become available? We conduct a set of ablation experiments in Appendix A.4.1, showing that the planning performance scales positively with the amount of training data. We also present the full inference and planning times for DINO-WM in Appendix A.8, showing significant speedup over traditional simulation, particularly in the computationally intensive deformable environments.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Does pre-trained visual representations matter?", "weight": 1.0} -->

We use different pre-trained general-purpose encoders as the observation model of the world model, and evaluate their downstream planning performance. Specifically, we use the following encoders commonly used in robotics control and general perception: R3M, ImageNet pretrained ResNet-18 and DINO CLS. Detailed descriptions of these encoders are in Appendix A.3.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Does pre-trained visual representations matter?", "weight": 1.0} -->

In the PointMaze task, which involves simple dynamics and control, we observe that world models with various observation encoders all achieve near-perfect success rates. However, as the environment's complexity increases---requiring more precise control and spatial understanding---world models that encode observations as a single latent vector show a significant drop in performance. We posit that patch-based representations better capture spatial information, in contrast to models like R3M, ResNet, and DINO CLS, which reduce observations to a single global feature vector, losing crucial spatial details necessary for manipulation tasks.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Generalizing to Novel Environment Configurations", "weight": 1.0} -->

We evaluate the generalization of our world models not only across different goals but also across various environment configurations. We construct three environment families---WallRandom, PushObj, and GranularRandom---where the model is tested on unseen configurations with random goals. Detailed descriptions of the environments can be found in Appendix A.2.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Generalizing to Novel Environment Configurations", "weight": 1.0} -->

Model WallRandom PushObj GranularRandom SR ↑ SR ↑ CD ↓ IRIS 0.06 0.14 0.86 DreamerV3 0.76 0.18 1.53 R3M 0.40 0.16 1.12 ResNet 0.40 0.14 0.98 DINO CLS 0.64 0.18 1.36 Ours 0.82 0.34 0.63 Table 3: Planning results for offline world models on three suites with unseen environment configurations.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Generalizing to Novel Environment Configurations", "weight": 1.0} -->

From Table 5, we observe that DINO-WM demonstrates significantly better performance in WallRandom, indicating that model has effectively learned the general concepts of walls and doors, even when they are positioned in locations unseen during training. In contrast, other methods struggle to accurately identify the door's position and navigate through it. The PushObj task remains challenging for all methods, as the model was only trained on the four object shapes, which makes it difficult to precisely infer relevant physical parameters. In GranularRandom, the agent encounters fewer than half the particles present during training, resulting in out-of-distribution images compared to the training instances. Nevertheless, DINO-WM accurately encodes the scene and successfully gathers the particles into a designated square location with the lowest Chamfer Distance (CD) compared to the baselines, demonstrating better scene understanding. We hypothesize that this is due to DINO-WM's observation model encoding the scene as patch features, making the variance in particle number still within the distribution for each image patch.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Qualitative comparisons with generative video models", "weight": 1.0} -->

Given the prominence of generative video models, it's natural to assume they could serve as world models. We compare DINO-WM with AVDC, a diffusion-based generative model. As shown in Figure 6, while AVDC can generate visually realistic future images, these images lack physical plausibility. Large, unrealistic changes can occur within a single timestep, and the model struggles to reach the exact goal state. Future advancements in generative models may help address these issues.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Qualitative comparisons with generative video models", "weight": 1.0} -->

We further compare DINO-WM with a variant of AVDC, where the diffusion model is trained to generate the next observation $o_{t + 1}$ conditioned on the current observation $o_{t}$ and action $a_{t}$. As detailed in Appendix A.6, the action-conditioned diffusion model diverges from the ground truth observations over long-term predictions, making it insufficient for accurate task planning.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Decoding and Interpreting the Latents", "weight": 1.0} -->

Although DINO-WM operates in latent space and the observation model is not trained with pixel reconstruction objectives, training a decoder aids in interpreting predictions. We evaluate the image quality of predicted futures across all models and find that our approach outperforms others, even those whose encoders are trained with environment-specific reconstruction objectives. Open-loop rollouts in Figure 4 demonstrate DINO-WM's robustness despite the lack of explicit pixel supervision. We report the Learned Perceptual Image Patch Similarity (LPIPS) on the world models' predicted future frames, which assesses perceptual similarity by comparing deep representations of images, with lower scores reflecting closer visual similarity. Additional results, including Structural Similarity Index (SSIM), are provided in Appendix A.7.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduce DINO-WM, a simple yet effective technique for modeling visual dynamics in latent space without the need for pixel-space reconstruction. We have demonstrated that DINO-WM captures environmental dynamics and generalizes to unseen configurations, independent of task specifications, enabling visual reasoning at test time and generating zero-shot solutions for downstream tasks through planning. DINO-WM takes a step toward bridging the gap between task-agnostic world modeling and reasoning and control, offering promising prospects for generic world models in real-world applications.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Limitations and Future Work: First, DINO-WM assumes having access to offline datasets with sufficient state-action coverage, which can be challenging to obtain for highly complex environments. This can potentially be addressed by combining DINO-WM with exploration strategies and updating the model as new experiences are available. Second, DINO-WM still relies on the availability of ground truth actions from agents, which may not always be feasible when training with vast video data from the internet. Lastly, while we currently plan in action space for downstream task solving, an extension of this work could involve developing a hierarchical structure that integrates high-level planning with low-level control policies to enable solving more fine-grained control tasks.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Impact Statement", "weight": 1.0} -->

This paper presents work whose goal is to facilitate the learning and applications of task-agnostic world models. There are many potential societal consequences of our work, none which we feel must be specifically highlighted here.
