## Introduction

Figure 2: Characteristics of latent world model approaches. Methods are grouped by training paradigm. End-to-end methods (PLDM) learn the encoder and predictor jointly from pixels without pre-trained representations or heuristics like stop-gradient or EMAs, but require many hyperparameters and lack collapse guarantees. Foundation-based methods (DINO-WM) avoid collapse by freezing a pre-trained vision encoder, forgoing end-to-end learning. Task-specific methods (Dreamer, TD-MPC) require reward signals or privileged state access. LeWM combines the strengths of all three: end-to-end, task-agnostic, pixel-based, reconstruction- and reward-free, with a single hyperparameter with provable anti-collapse guarantees.

A central goal of artificial intelligence is to develop agents that acquire skills across diverse tasks and environments using a single, unified learning par adigm---one that operates directly from sensory inputs of its surroundings--without hand-engineered state representations or domain-specific calibration. Vision is ideally suited for this aim: cameras are inexpensive and scalable, and learning from pixels enables fully end-to-end training from raw sensory input to action. World Models (WMs) are a powerful family of methods that learn to predict the consequences of actions in the environment. When successful, WMs allows agents to plan and to improve themselves solely form their model of the world, i.e., in imagination space. This is particularly valuable in the offline setting, where agents must learn from fixed datasets without environment interaction---leveraging the model to generate synthetic experience and evaluate counterfactual action sequences.

A recent popular approach for learning world models is the Joint Embedding Predictive Architecture (JEPA). Instead of attempting to model every aspect of the environment, JEPA focuses on capturing the most relevant features needed to predict future states. Concretely, JEPA learns to encode observations into a compact, low-dimensional latent space and models temporal dynamics by predicting the latent representation of future observations.

However, despite their conceptual simplicity, existing JEPA methods are highly prone to collapse. In this failure mode, the model maps all inputs to nearly identical representations to trivially satisfy the temporal prediction objective leading to unusable representations. Preventing collapse is therefore one of the central challenges in training JEPA models. Many influential works have proposed methods to address this issue. Yet, these approaches typically rely on heuristic regularization, multi-objective loss functions, external sources of information, or architectural simplifications such as pre-trained encoders. In practice, these strategies often introduce additional instability or significantly increase training complexity (see App. C).

To overcome these limitations, we propose LeWorldModel (LeWM), the first method to learn a stable JEPA end-to-end from raw pixels without heuristics, principled, and simple (cf. Fig 1). We evaluate LeWM across a diverse set of manipulation, navigation, and locomotion tasks in both 2D and 3D environments. In addition, we probe its intuitive physical understanding through targeted probing and surprise-quantification evaluations in latent space. Overall, our key findings and contributions are:

We propose an end-to-end JEPA method for learning a latent world model from raw pixels on a single GPU. The method relies on a simple and stable two-term objective that remains robust across architectures and hyperparameter choices, while enabling efficient logarithmic-time hyperparameter search.

Our experiment demonstrates that LeWM achieves competitive control performance across diverse 2D and 3D tasks with only a compact 15M-parameter model, surpassing existing end-to-end JEPA-based approaches while remaining competitive with foundation-model-based world models at substantially lower cost, enabling planning up to $48 \times$ faster.

We evaluate physical understanding in the latent space through probing of physical quantities and a violation-of-expectation test for detecting unphysical trajectories.

## Related Work

Figure 3: Planning time and performance under fixed compute. Left: Planning time comparison averaged over 50 runs. Encoding observations with ∼ 200× fewer tokens than DINO-WM allows LeWM to achieve planning speeds comparable to PLDM while being up to ∼ 50× faster than DINO-WM. Center–Right: Planning performance under the same computational budget (fixed FLOPs). LeWM significantly outperforms DINO-WM on Push-T (center) and OGBench-Cube (right). See App. D for planning setup details.

World Models aim to learn predictive models of environment dynamics from data, enabling agents to reason about future states in imagination. A prominent class of WMs consists of *generative* approaches that explicitly model environment dynamics in pixel space. These action-conditioned generative models act as learned simulators by producing future observations conditioned on past states and actions. Generative world models have been successfully applied to simulate existing game-like environments. For example, IRIS, DIAMOND, $\Delta$-IRIS, OASIS, and DreamerV4 model environments such as Minecraft, Counter-Strike, and Crafter, improving policy sample efficiency in reinforcement learning. Other methods generate entirely new interactive simulators, e.g., Genie and HunyuanWorld, while learned simulators have also been applied to robot policy evaluation. Importantly, many generative WMs assume access to datasets containing reward signals, enabling joint modeling of dynamics and value-relevant information for downstream reinforcement learning. In contrast, we focus on the reward-free setting, corresponding to the setup considered in the JEPA line of work, which aims at learning generic, task-agnostic world models from observational data without relying on reward supervision.

JEPA is a framework for learning world models that predict the dynamic evolution of a system in a compact, low-dimensional latent space. Since their introduction by LeCun, JEPA methods have evolved considerably, differing mainly in their target tasks and in the strategies used to learn non-collapsing representations. One prominent line of work applies JEPA to self-supervised representation learning by predicting the latent embeddings of masked input patches. Examples include I-JEPA for images, V-JEPA for videos, and Echo-JEPA and Brain-JEPA for medical data. These approaches typically employ an exponential moving average (EMA) of the target encoder together with stop-gradient (SG) updates to stabilize training and prevent representation collapse. However, the theoretical understanding of EMA and SG remains limited, as they do not in general correspond to the minimization of a well-defined objective. A second line of work uses the JEPA recipe for action-conditioned latent world modeling. Some approaches rely on pretrained encoders to obtain representations. This avoids collapse but limits the expressivity of representation to the pretrained encoder used. In contrast, PLDM learns representations end-to-end using VICReg with additional regularization terms, at the cost of known training instabilities and scalability limitations. Several works further improve stability by incorporating auxiliary signals or architectural components, such as proprioceptive inputs or action decoders. In this work, we propose a stable method for training end-to-end JEPAs directly from raw pixels using a simple two-term loss: a predictive objective on future embeddings and a regularization objective that enforces Gaussian-distributed embeddings.

Planning with Latent Dynamics. World Models pioneered learning policies directly from compact latent representations of high-dimensional observations. Some works leverage learned latent dynamics models to train policies using reinforcement learning. In these approaches, the generative world model acts as a simulator in which trajectories are rolled out in imagination, allowing policy optimization to occur largely in imagination in latent space. Once training is complete, the policy is executed directly, and the world model is no longer required at test time. More recent works instead perform planning directly in the latent space at test time using Model Predictive Control (MPC).

Figure 4: Latent Planning with LeWorldModel. Given an initial observation o1 and a goal og, the world model learned in Fig. 2 performs planning in the LeWM latent space. The initial state embedding z1 and the goal embedding zg are obtained from the encoder. The predictor then rolls out future latent states up to a horizon H. A latent cost between the final predicted state and the goal embedding guides a solver to optimize the action sequence. This prediction–optimization loop is repeated until convergence to a good plan candidate.

## Method: LeWorldModel

In this section, we introduce LeWorldModel (LeWM). We first describe the streamlined training procedure used to learn the latent world model from offline data, including the dataset, model architecture, and training objective. We then explain how the learned model can be leveraged for decision making through latent planning using model predictive control (MPC).

### Learning the Latent World Model

### Offline Dataset

We consider a fully offline and reward-free setting. LeWorldModel is trained solely from unannotated trajectories of observations and actions, without access to reward signals or task specifications. This setup aligns with the JEPA line of work, which aims to learn generic, task-agnostic world models from observational data. Our objective is not to optimize behavior for a specific task, but to learn representations that capture environment dynamics and can later be controlled or adapted to a diverse set of tasks.

The training data consists of trajectories of length $T$ composed of raw pixel observations ${\mathbf{o}}_{1:T}$ and associated actions ${\mathbf{a}}_{1:T}$. Trajectories are collected offline from behavior policies with no optimality requirements; they may be pseudo-expert or exploratory, as long as they sufficiently cover the environment dynamics. Additional implementation details (batch size, resolution, and sub-trajectory construction) are provided in App. D.

### Model Architecture

LeWM is built upon two components: an encoder and a predictor. The encoder maps a given frame observation ${\mathbf{o}}_{t}$ into a compact, low-dimensional latent representation ${\mathbf{z}}_{t}$. The predictor models the environment dynamics in latent space by predicting the embedding of the next frame observation ${\hat{\mathbf{z}}}_{t + 1}$ given the latent embedding ${\mathbf{z}}_{t}$ and an action ${\mathbf{a}}_{t}$.

The encoder is implemented as a Vision Transformer (ViT). Unless otherwise specified, we use the tiny configuration ($\sim$`<!-- -->`{=html}5M parameters) with a patch size of 14, 12 layers, 3 attention heads, and hidden dimensions of 192. The observation embedding ${\mathbf{z}}_{t}$ is constructed from the \[CLS\] token embedding of the last layer, followed by a projection step. The projection step maps the \[CLS\] token embedding into a new representation space using a 1-layer MLP with Batch Normalization. This step is necessary because the final ViT layer applies a Layer Normalization, which prevents our anti-collapse objective from being optimized effectively.

The predictor is a transformer with 6 layers, 16 attention heads, and 10% dropout ($\sim$`<!-- -->`{=html}10M parameters). Actions are incorporated into the predictor through Adaptive Layer Normalization (AdaLN) applied at each layer. The AdaLN parameters are initialized to zero to stabilize training and ensure that action conditioning impacts the predictor training progressively. The predictor takes as input a history of $N$ frame representations and predicts the next frame representation auto-regressively with temporal causal masking to avoid looking at future embeddings. The predictor is also followed by a projector network with the same implementation as the one used for the encoder. All components of our world model are learned jointly using the loss described in the following paragraph.

### Training Objective

Our objective is to learn latent representations useful for predicting the future, i.e., modeling the environment dynamics. LeWorldModel training objective is the sum of two terms: a prediction loss and a regularization loss. The prediction loss $\mathcal{L}_{pred}$ (teacher-forcing) computes the error between the predicted embedding of consecutive time-steps:

Through the prediction loss, the encoder is incentivized to learn a predictable representation for the predictor.

However, if alone, the loss in Eq. 1 leads to representation collapse, yielding a trivial solution in which the encoder maps all inputs to a constant representation. To prevent this behavior, we introduce an anti-collapse regularization term that promotes feature diversity in the embedding space. Specifically, we adopt the Sketched-Isotropic-Gaussian Regularizer (SIGReg) due to its simplicity, scalability, and stability. SIGReg encourages the latent embeddings to match an isotropic Gaussian target distribution.

Let ${\mathbf{Z}} \in {\mathbb{R}}^{N \times B \times d}$ denote the tensor of latent embeddings collected over the history length $N$, the batch size $B$, and where $d$ denotes the embedding dimension. Assessing normality directly in high-dimensional spaces is challenging, as most classical normality tests are designed for univariate data and do not scale reliably with dimensionality. SIGReg circumvents this limitation by projecting embeddings onto $M$ random unit-norm directions ${\mathbf{u}}^{(m)} \in {\mathbb{S}}^{d - 1}$ and optimizing the univariate Epps--Pulley test statistic $T{( \cdot )}$ along the resulting one-dimensional projections ${\mathbf{h}}^{(m)} = {{\mathbf{Z}}{\mathbf{u}}^{(m)}}$, as illustrated in Fig.1. By the Cramér--Wold theorem, matching all one-dimensional marginals is equivalent to matching the full joint distribution.

Additional details on SIGReg and the definition of the Epps--Pulley statistical test are provided in appendix A.

The complete LeWM training objective is defined as:

The method introduces only two training hyperparameters: the number of random projections $M$ used in SIGReg and the regularization weight $\lambda$. Unless otherwise specified, we use $M = 1024$ projections and $\lambda = 0.1$. In practice, we observe that the number of projections has negligible impact on downstream performance (see Sec. 4 and App. G), making $\lambda$ the only effective hyperparameter to tune. This greatly simplifies hyperparameter selection, as $\lambda$ can be efficiently optimized using a simple bisection search with logarithmic complexity. We do not employ stop-gradient, exponential moving averages, or additional stabilization heuristics. Gradients are propagated through all components of the loss, and all parameters are optimized jointly in an end-to-end manner, resulting in a streamlined and easy-to-implement training procedure. The training logic is summarized in Alg. 9.

### Latent Planning

At inference time, we perform trajectory optimization in our world model latent space, as illustrated in Fig.4. Given an initial observation ${\mathbf{o}}_{1}$, we initialize a candidate action sequence randomly and iteratively rollout predicted latent states up to a planning horizon $H$. The model predicts latent transitions according to

Planning is performed by optimizing the action sequence to minimize a terminal latent goal-matching objective,

where ${\hat{\mathbf{z}}}_{H}$ is the predicted latent state at the end of the rollout and ${\mathbf{z}}_{g}$ is the latent embedding of the goal observation ${\mathbf{o}}_{g}$. The world model parameters remain fixed during planning. This procedure corresponds to a finite-horizon optimal control problem,

which we solve using the Cross-Entropy Method (CEM), a sampling method that iteratively selects the best plan and updates the parameters of the sampling distribution with the statistics of the best plans. The planning horizon $H$ trades off long-term lookahead against increased computational cost and model bias. In particular, auto-regressive rollouts accumulate prediction errors as the horizon grows, which can deteriorate the quality of the optimized action sequence. To mitigate this effect, we adopt a Model Predictive Control (MPC) strategy: only the first $K$ planned actions are executed before replanning from the updated observation. We provide more details on the planning strategy in appendix D.

## Latent Planning Performance

### Planning evaluation setup

Figure 5: Environments used for evaluation. Left: Push-T, a 2D manipulation task where the agent must push a block toward a target configuration, commonly used as a robotics benchmark. Center: OGBench-Cube, a visually richer 3D manipulation environment where a robotic arm interacts with a cube to reach a target position. Center: Two-Room, a simple 2D navigation environment where an agent moves between rooms to reach target positions. Right: Reacher, a task where a 2-joint arm needs to reach a target configuration in a 2D plane. All environments have a continuous action space. More details on environment and datasets are available in appendix E.

### Environments

We evaluate LeWM on a diverse set of tasks, including navigation, motion planning and manipulation, in both two- and three-dimensional environments, all illustrated in Fig. 5. We provide more details on dataset generation and environments in App. E.

### Baselines

We compare the performance of LeWM against several baselines: DINO-WM and PLDM, two state-of-the-art JEPA-based methods; a goal-conditioned behavioral cloning policy (GCBC); and two goal-conditioned offline reinforcement learning algorithms, GCIVL and GCIQL. Among these baselines, PLDM is the closest to our setup, as it also learns a world model end-to-end directly from pixel observations. However, it relies on a seven-term training objective derived from the VICReg criterion, which introduces training instability and increases the complexity of hyperparameter tuning. DINO-WM, in contrast, models dynamics using DINOv2 as feature encoder to mitigate representation collapse, but its original formulation additionally incorporates other modalities, such as proprioceptive inputs; for a fair comparison, unless specified otherwise, we exclude proprioceptive information from DINO-WM. Additional implementation details for the baselines (App. C) and evaluation settings (App. F.1) are provided in the appendix. For each method, we keep the hyperparameters fixed across all environments.

### Towards Efficient Planning with WMs

We report planning performance in Fig. 6. LeWM outperforms PLDM on the more challenging planning tasks, achieving an 18% higher success rate on PushT, while remaining competitive with DINO-WM. Notably, on PushT, LeWM (pixels-only) surpasses DINO-WM even when DINO-WM has access to additional proprioceptive information, demonstrating LeWM's ability to capture underlying task-relevant quantities. Interestingly, LeWM performs worse on the simplest environment, Two-Room. A possible explanation is that the low diversity and low intrinsic dimensionality of this dataset make it difficult for the encoder to match the isotropic Gaussian prior enforced by SIGReg in a high-dimensional latent space, which may lead to a less structured latent representation. This highlights a potential limitation of the SIGReg regularization in very low-complexity environments.

Moreover, when comparing planning speedups (Fig. 3), LeWM achieves a $48 \times$ faster planning time, with the full planning completing in under one second while preserving competitive performance across tasks. This planning time remains consistent across environments for a fixed planning setup, narrowing the gap toward real-time control.

### Towards Stable Training of World Models

### Ablations

We perform ablations on several design choices of LeWM. First, we analyze the sensitivity of SIGReg to its internal parameters, namely the number of random projections and the number of integration knots. The performance is largely unaffected by these quantities, indicating that they do not require careful tuning. As a result, the regularization weight $\lambda$ remains the only effective hyperparameter. Since only a single hyperparameter needs to be tuned, grid search can be performed efficiently using a simple bisection strategy ($\mathcal{O}{({\log n})}$), whereas PLDM requires search in polynomial time ($\mathcal{O}{(n^{6})}$). We also study the effect of the embedding dimensionality. While the representation dimension must be sufficiently large for the method to perform well, performance quickly saturates beyond a certain threshold, suggesting that the approach is robust to the precise choice of encoder capacity. Additionally, we examine the impact of the encoder architecture by replacing the default ViT encoder with a ResNet-18 backbone (Tab. 8). LeWM achieves competitive performance with both architectures, indicating that it is largely agnostic to the choice of vision encoder. Details on all ablations are available in App. G.

### Training Curves

We report the training loss curves on PushT for LeWM in Fig. 18 and PLDM in Fig. 19. The two-term objective of LeWM exhibits smooth and monotonic convergence: the prediction loss decreases steadily while the SIGReg regularization term drops sharply in the early phase of training before plateauing, indicating that the latent distribution quickly approaches the isotropic Gaussian target. In contrast, PLDM's seven-term objective displays noisy and non-monotonic behavior across several of its loss components. These observations highlight a key advantage of LeWM: by reducing the training objective to only two well-behaved terms, the training becomes significantly more stable, removing the need to balance competing gradients from multiple regularizers.

Figure 6: Planning performance across environments. Results are shown for Two-Room (left), Reacher (center 1), PushT (center-2) and OGBench-Cube (right). LeWM consistently outperforms PLDM and DINO-WM on Push-T and Reacher. On OGBench-Cube, DINO-WM slightly outperforms LeWM, possibly due to the higher visual complexity and the 3D nature of the environment, which makes encoder training more challenging. In the simpler Two-Room environment, PLDM and DINO-WM outperform LeWM, which may be explained by the SIGReg regularization encouraging a Gaussian distribution in a high-dimensional latent space, while the intrinsic dimensionality of the environment is much lower.

## Quantifying Physical Understanding in LeWM

In this section, we evaluate the quality of the dynamics captured by LeWM's latent space, either by learning to extract physical quantities from latent embeddings or by measuring the world model's ability to detect changes in physics.

### Physical Structure of the Latent Space

### Probing physical quantities

As a first measure of physical understanding, we evaluate which physical quantities are recoverable from LeWM's latent representations. We train both linear and non-linear probes to predict physical quantities of interest from a given embedding. Results on the Push-T environment are reported in Tab. 1. Our method consistently outperforms PLDM while remaining competitive with representations produced by large pretrained models such as DINOv2. We provide probing results on other environments in App. F.2.

Table 1: Physical latent probing results on Push-T. LeWM consistently outperforms PLDM while remaining competitive with DINO-WM. The strong probing performance of DINO-WM on certain properties may stem from its foundation-model pretraining: the DINOv2 encoder is trained on two orders of magnitude more data (∼124M images) spanning a far more diverse distribution, which likely allows it to capture some physical properties in its embeddings by default.

Figure 7: Predictor rollout on OGBench-Cube. We visualize decoded latent plans from LeWM given context and action sequences. Each rollout encodes three image observations as context, then autoregressively generates future latents conditioned on the actions in an open-loop fashion. Latents are decoded via a decoder trained a posteriori. The imagined rollout suggests that latent representations capture the global scene structure while finer details like end-effector angle are not fully preserved. Additional rollouts for Push-T and OGBench-Cube are provided in Fig. 9.

### Decoding Latent Space

To further assess the information captured in the latent representation, we report in Fig. 10 images produced by a decoder trained to reconstruct pixel observations from a single latent embedding (192 dim) during training. Although reconstruction is never used during training, the decoder is able to recover the visual scene from the learned representation, confirming that the low-dimensional and compact latent space retains sufficient information about the underlying physical state. Details on the decoder architecture are provided in App. D.

### Visualizing Latent Space

We further visualize the structure of the latent space using t-SNE. Fig. 13 provides a qualitative visualization of the latent space in the PushT environment. The visualization suggests that the learned representation captures the spatial structure of the environment, preserving neighborhood relationships and relative positions in the latent space.

### Temporal Latent Path Straightening

Inspired by the temporal straightening hypothesis from neuroscience and recent work , we measure the cosine similarity between consecutive latent velocity vectors throughout training (Eq. 9). We find that LeWM's latent trajectories become increasingly straight on PushT over training as a purely emergent phenomenon, without any explicit regularization encouraging this behavior, cf. Fig. 17. Remarkably, LeWM achieves higher temporal straightness than PLDM, despite PLDM employing a dedicated temporal smoothness regularization term. We detail our findings in App. H.

### Violation-of-expectation Framework

Figure 8: Violation-of-expectation evaluation across three environments. Each plot shows LeWM surprise along three trajectories: an unperturbed reference, a visually perturbed trajectory with abrupt object color change, and a physically perturbed trajectory where objects teleport to random positions. Teleportation violates physical continuity and produces a pronounced surprise spike, while the unperturbed trajectory stays at a low baseline. The increase is significant for teleportation across all environments (paired t-test, p &lt; 0.01) but weaker and non-significant for color changes, indicating greater sensitivity to physical than visual perturbations. Environments, left to right: TwoRoom, PushT, OGBench Cube.

Another approach to quantifying physical understanding is the ability to detect violations of the learned world model. Inspired by the violation-of-expectation (VoE) paradigm used in developmental psychology and recently adopted in machine learning, this framework evaluates whether a model assigns higher surprise to events that contradict learned physical regularities.

Following prior work, we quantify surprise by measuring the discrepancy between the model's predicted future observations and the actual observed future. We evaluate this framework across three environments: TwoRoom, PushT, and OGBench Cube. For each environment, we introduce two types of perturbations. The first is a visual perturbation, where the color of an object changes abruptly during the trajectory. The second is a physical perturbation, where one or more objects are teleported to a random location, violating the expected physical continuity of the scene. Fig. 8 shows that LeWM consistently assigns higher surprise to frames containing physical violations compared to their unperturbed counterparts. We provide more details on VoE in App. F.3.

## Conclusion

We introduced LeWorldModel (LeWM), a stable end-to-end method for learning latent world models. LeWM is a Joint-Embedding Predictive Architecture in which an encoder maps image observations to a latent space and a predictor models temporal dynamics by forecasting future embeddings conditioned on actions. Across continuous control environments with raw pixel inputs, LeWM outperforms prior approaches in data efficiency, planning time, training time, and stability while remaining competitive in task performance. Training stability stems from explicitly encouraging latent embeddings toward an isotropic Gaussian distribution to prevent collapse, offering a scalable and principled alternative to existing work.

### Limitations & Future Work

Several limitations point to future directions. Planning remains restricted to short horizons, motivating hierarchical world modeling for long-horizon reasoning. Our method also relies on offline datasets with sufficient coverage; in particular, low data diversity weakens SIGReg in simple, low-dimensional environments where matching a high-dimensional Gaussian prior is harder. Pre-training on large, diverse video datasets could provide stronger priors and reduce domain-specific data needs. Finally, dependence on action labels could be alleviated by inverse dynamics modeling.
