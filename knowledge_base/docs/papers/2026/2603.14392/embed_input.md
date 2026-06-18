<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

WestWorld: A Knowledge-Encoded Scalable Trajectory World Model for Diverse Robotic Systems

Topics include Robotics, Few-shot learning, Scalability, Generalization, Planning, Control, Learning, WestWorld.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Trajectory world models play a crucial role in robotic dynamics learning, planning, and control. While recent works have explored trajectory world models for diverse robotic systems, they struggle to scale to a large number of distinct system dynamics and overlook domain knowledge of physical structures. To address these limitations, we introduce WestWorld, a knoWledge-Encoded Scalable Trajectory World model for diverse robotic systems. To tackle the scalability challenge, we propose a novel system-aware Mixture-of-Experts (Sys-MoE) that dynamically combines and routes specialized experts for different robotic systems via a learnable system embedding. To further enhance zero-shot generalization, we incorporate domain knowledge of robot physical structures by introducing a structural embedding that aligns trajectory representations with morphological information. After pretraining on 89 complex environments spanning diverse morphologies across both simulation and real-world settings, WestWorld achieves significant improvements over competitive baselines in zero- and few-shot trajectory prediction. Additionally, it shows strong scalability across a wide range of robotic environments and significantly improves performance on downstream model-based control for different robots. Finally, we deploy our model on a real-world Unitree Go1, where it demonstrates stable locomotion performance. The code is available at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Trajectory world models are essential for robotic dynamics learning, planning, and control based on low-level sensory data. However, building a trajectory world model for diverse robotic systems poses two key challenges: i) sensor and actuator heterogeneity, where the variance in types and sampling rates hinders shared representations, and ii) system dynamics gaps caused by diverse kinematic structures across different robotic systems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address these challenges, a few recent studies discretize continuous states and actions across diverse systems into tokens via quantization and leverage flexible Transformer architectures for joint training. Although these approaches enable multi-system pretraining within a single dense model, they still face scalability and generalization limitations across diverse robotic dynamics for two main reasons. First, existing approaches force different system dynamics to share a common set of model parameters, leading to gradient conflicts and negative transfer that impede effective scaling as robot diversity grows. Second, these methods overlook robot morphological information when modeling trajectories, thereby lacking the physical inductive biases required for zero-shot generalization to unseen robotic systems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To overcome these limitations, we develop WestWorld, a knowledge-encoded scalable trajectory world model that incorporates domain knowledge of robot morphology to learn the underlying dynamics of diverse robotic systems (see Fig. 1). Developing such a model poses two key challenges: i) learning distinct system dynamics at scale while avoiding task interference across different robots, and ii) incorporating physical structural information as an inductive bias to enhance zero-shot generalization. To address the first challenge of scalability, we propose a system-aware mixture-of-experts (Sys-MoE) that implicitly learns distinct system dynamics through expert learning. Unlike existing trajectory world models, which learn multiple system dynamics using a single large dense model, the proposed Sys-MoE dynamically combines and routes specialized experts for different robotic systems via a learnable system embedding. This design mitigates task interference across robots, thus significantly improving scalability. For the second challenge of generalization, we introduce a structure-based channel embedding that aligns low-level state trajectories with morphology information, thereby improving the model's ability to generalize to unseen robotic systems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We pretrain the proposed WestWorld on 89 complex environments using a combination of simulated and real-world data. Extensive experiments show that our method substantially outperforms strong baselines in both zero-shot and few-shot trajectory prediction. Moreover, it enables scalable training across diverse robotic systems without sacrificing performance and significantly improves the performance of downstream tasks such as model-based control.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our contributions include: 1) We propose WestWorld, a novel system-aware MoE architecture for scaling up the training of trajectory world models across diverse robotic systems; 2) We introduce knowledge-encoded structural embedding that provides an explicit inductive bias to enhance zero- and few-shot generalization to unseen robotic systems; 3) We conduct extensive experiments to verify the scalability and generalizability of our method, showing its superiority over strong baselines; and 4) We apply our model to downstream model-based control and further extend it to real-world Unitree Go1 deployment, demonstrating its strong performance in planning tasks.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Overview of WestWorld", "weight": 1.0} -->

To enable scalable pretraining and zero-shot generalization across diverse robotic systems, we propose WestWorld, a knowledge-encoded scalable trajectory world model with a system-aware Mixture-of-Experts (MoE) design. As shown in Fig. 1, the proposed model consists of two core components: Knowledge-Encoded Embedding Modular and System-Aware MoE.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Overview of WestWorld", "weight": 1.0} -->

The core idea is to first perform channel-wise normalization and discretize each scalar variable for tokenization. The resulting representations are then processed by Knowledge-Encoded Embedding Modular, which extracts the robot's morphological connectivity and injects structural embeddings as an inductive bias into trajectory representations. These structure-aware embeddings are subsequently fed into multiple System-Aware MoE blocks for dynamics modeling. Finally, a linear decoder maps the hidden states to future trajectory predictions. We detail these two core components in the following.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Knowledge-Encoded Embedding Modular", "weight": 1.0} -->

Motivation. Existing trajectory world models are predominantly data-driven, relying solely on state-action observations and largely ignoring domain knowledge that different robotic morphologies should obey distinct physical constraints. The lack of encoding explicit structural information makes it difficult for these models to capture the underlying system dynamics and limits their ability to generalize across environments. We hypothesize that robots with similar connectivity patterns often exhibit shared high-level dynamical behaviors (e.g., SLIP-like locomotion ). This insight motivates us to incorporate morphological connectivity into model design as an inductive bias. Below, we first introduce the trajectory data tokenization before diving into proposed knowledge-encoded structural embedding.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Knowledge-Encoded Embedding Modular", "weight": 1.0} -->

Trajectory Tokenization. Given a trajectory, we treat each state or action dimension at time step $t$ as a *scalar channel*. Let $x_{t}^{(m)} \in {\mathbb{R}}$ denote the value of channel $m$ at time $t$, where $m$ represents the index of state channels or action channels. We apply channel-wise min--max normalization, and discretize it into a $K$-bin categorical vector through $\mathbf{\phi}:{{\mathbb{R}}\rightarrow{\mathbb{R}}^{K}}$ following. We further analyze the effect of different numbers of bins in Appendix D.2. We then map $\mathbf{\phi}{(x_{t}^{(m)})}$ to a $d$-dimensional embedding via a learned projection.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Knowledge-Encoded Embedding Modular", "weight": 1.0} -->

After that, we incorporate timestep embeddings, channel order index embeddings, and modality indicator (state or action) embeddings, yielding ${\mathbf{z}}_{t}^{(m)} \in {\mathbb{R}}^{d}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Knowledge-Encoded Embedding Modular", "weight": 1.0} -->

Knowledge-Encoded Structural Embedding. To incorporate morphology structure priors into latent representations, we introduce a knowledge-encoded structural embedding, as shown in Fig. 1 (a). Specifically, we first model each articulated object as a rooted kinematic tree and convert it to a binary tree using the left-child-right-sibling (LCRS) transformation. Each body node is assigned three traversal indices from pre-/in-/post-order walks. For object $i$ and its body node $j$, let $\left( \pi_{pre}^{i,j},\pi_{in}^{i,j},\pi_{post}^{i,j} \right)$ denote these indices. In scenes with multiple articulated objects, we additionally assign an object identifier $\pi_{obj}^{i}$: the robot is indexed as $\pi_{obj}^{i} = 0$, and other objects are ordered by increasing Euclidean distance to the robot (see Appendix B for an example).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Knowledge-Encoded Embedding Modular", "weight": 1.0} -->

With this tuple indices, we can uniquely identify each robot body node in the LCRS-converted binary tree derived from the robot's structure.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Knowledge-Encoded Embedding Modular", "weight": 1.0} -->

where each ${\mathbf{e}}_{\{{obj},{pre},{in},{post}\}}{( \cdot )}$ denotes a structural encoder that maps a discrete index to a $d/4$-dimensional vector, and their concatenation forms ${\mathbf{p}}^{(i,j)} \in {\mathbb{R}}^{d}$. Finally, we inject morphology knowledge by adding ${\mathbf{p}}^{(i,j)}$ to the corresponding state/action embeddings, yielding structure-aware trajectory embeddings that are used as inputs to our model.

<!-- chunk {"id": "body-0016", "role": "body", "section": "System-Aware MoE Block", "weight": 1.0} -->

Motivation. Robotic systems with diverse morphologies often exhibit markedly different dynamics, making it difficult to develop a single unified model that accurately captures their underlying dynamics. When such dissimilar dynamics are trained simultaneously using shared parameters, optimization is prone to gradient conflicts and task interference, leading to poor scalability. To address this challenge, we introduce a novel system-aware Mixture-of-Experts (Sys-MoE) block for learning distinct system dynamics, in which each expert tries to learn part of underlying system dynamics. Our key insight is that complex system dynamics can be effectively approximated by composing a set of basis dynamics with system-dependent coefficients.

<!-- chunk {"id": "body-0017", "role": "body", "section": "System-Aware MoE Block", "weight": 1.0} -->

Block design. To scale joint training across diverse robotic systems while mitigating interference, we parameterize the transition model in Eq. with a stack of *Sys-MoE Blocks*. Each block contains two parts: i) an attention-based aggregation module that fuses state--action information, and ii) a system-aware MoE layer that captures diverse system dynamics. We detail the two parts below.

<!-- chunk {"id": "body-0018", "role": "body", "section": "System-Aware MoE Block", "weight": 1.0} -->

i\) Attention-based aggregation. As shown in Fig. 1(b), we use attention to aggregate information across state channels and to inject action-dependent control signals, while naturally supporting variable state/action dimensionalities across systems. Concretely, we apply: 1) self-attention to capture correlations among state variables, and then use 2) cross-attention to condition state features on the action embeddings. To enable $k$-step prediction in a single forward pass, we concatenate the history state embeddings with $k$ learnable query embeddings $\{{\mathbf{q}}_{t},\ldots,{\mathbf{q}}_{{t + k} - 1}\}$, which serve as latent queries for future states.

<!-- chunk {"id": "body-0019", "role": "body", "section": "System-Aware MoE Block", "weight": 1.0} -->

At each time step, self-attention is computed as

<!-- chunk {"id": "body-0020", "role": "body", "section": "System-Aware MoE Block", "weight": 1.0} -->

where self-attention is applied along the state channel, and ${LN}{( \cdot )}$ is layer normalization.

<!-- chunk {"id": "body-0021", "role": "body", "section": "System-Aware MoE Block", "weight": 1.0} -->

This operation injects action-dependent signals while remaining compatible with variable action dimensionalities.

<!-- chunk {"id": "body-0022", "role": "body", "section": "System-Aware MoE Block", "weight": 1.0} -->

ii\) System-aware MoE layer. After obtaining the action-conditioned latent states above, we model continuous-time system dynamics using a system-aware Mixture-of-Experts (Sys-MoE) layer, as shown in Fig. 1(b). Unlike the MoE design commonly used in large language models, where routing selects experts to directly produce token embeddings from the input, our routing is *system-aware*. Specifically, we introduce a learnable system embedding that propagates through the SSM to extract system-level properties of the underlying dynamics. The resulting system embeddings are then used to compute mixture weights over experts, so that the model forms a system-conditioned combination of different experts.

<!-- chunk {"id": "body-0023", "role": "body", "section": "System-Aware MoE Block", "weight": 1.0} -->

Let $L = {h + k}$ be the number of state embeddings after concatenating history states with $k$ queries. For each state channel $m$, we denote the attention outputs as ${\hat{\mathbf{S}}}_{1:L}^{(m)} = {\{{\hat{\mathbf{s}}}_{{t - h}:{t - 1}}^{(m)},{\hat{\mathbf{s}}}_{t:{{t + k} - 1}}^{(m)}\}}$, where the last $k$ tokens correspond to the query positions. We append a learnable system embedding ${\mathbf{e}} \in {\mathbb{R}}^{d}$ to attention outputs, yielding

<!-- chunk {"id": "body-0024", "role": "body", "section": "System-Aware MoE Block", "weight": 1.0} -->

where ${\mathbf{U}}_{1:{L + 1}}^{(m)}$ denotes the SSM outputs for all embeddings. In our implementation, ${SSM}{( \cdot )}$ follows a Mamba-style selective SSM, enabling causal computation and efficient long-range dependency modeling.

<!-- chunk {"id": "body-0025", "role": "body", "section": "System-Aware MoE Block", "weight": 1.0} -->

We use the output of the system embedding, ${\mathbf{U}}_{L + 1}$, to extract system-aware properties for routing.

<!-- chunk {"id": "body-0026", "role": "body", "section": "System-Aware MoE Block", "weight": 1.0} -->

where $w_{p}$ is the $p$-th entry of $\mathbf{w}$, and each expert $E_{p}{( \cdot )}$ is implemented as an MLP. Finally, we stack multiple Sys-MoE blocks to increase expressivity for complex system dynamics.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Objective Function", "weight": 1.0} -->

After stacking Sys-MoE Blocks, we obtain the per-channel output sequence ${\mathbf{Y}}_{1:L}^{(m)}$ We apply a linear decoder head to produce logits over $K$ uniform bins. Concretely, for each channel $m$ outputs, we compute

<!-- chunk {"id": "body-0028", "role": "body", "section": "Objective Function", "weight": 1.0} -->

During inference time, we run the model in a sequence-to-sequence manner, enabling multi-step prediction in a single forward pass.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we pretrain WestWorld on large-scale, diverse robotic datasets and conduct extensive experiments to evaluate: (i) zero-shot generalization to unseen environments, (ii) few-shot adaptation under domain shifts, (iii) scalability as the number of pretraining environments increases, and (iv) improvements in downstream control tasks across diverse robotic systems enabled by pretraining.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

Diverse Pretraining Datasets. For pretraining the proposed trajectory world model, we collect a large amount of simulated and real-world data: i) UniTraj dataset, which contains 80 simulated robotic environments; and ii) 9 real-world robot-arm datasets from the Open X-Embodiment. A detailed list of the pretraining and evaluation environments used in our experiments is provided in Appendix C.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

Baseline Methods. We compare our method against several state-of-the-art trajectory world models. MLP Ensemble: a widely used baseline in model-based RL for learning probabilistic dynamics through an ensemble of multilayer perceptrons. TDM: a Transformer-based model built upon the Gato architecture, which flattens spatial and temporal features into a single sequence and applies one-dimensional attention for autoregressive prediction. TrajWorld: a Transformer-based trajectory model that employs temporal-variate attention for autoregressive rollout.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

Implementation Details. We follow each baseline's original pretraining configuration. Detailed training and implementation settings for WestWorld and all baselines are provided in Appendix D. For fairness, all baseline models are pretrained from scratch on the above same dataset as the proposed WestWorld.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Main Results", "weight": 1.0} -->

Evaluation on Zero-shot Performance. We first evaluate the zero-shot performance of our model on three unseen robotic environments that share similar structural morphology with those in the pretraining data. Specifically, we use datasets from three environments as our testbeds. These include Hopper and Walker2D from D4RL, as well as a real-world dataset of a mobile Franka manipulator interacting with articulated objects. We evaluate 100-step consecutive predictions using a 50-step history window as input. Mean Absolute Error (MAE) and Mean Squared Error (MSE) are used to assess the accuracy of long-horizon prediction.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Main Results", "weight": 1.0} -->

As shown in Table 1, our method achieves the best performance across all three unseen environments in long-horizon prediction. This improvement is attributed to the combination of our system-aware MoE architecture and the structural inductive bias introduced through morphology-aware design. The MoE design enables the model to learn distinct dynamics for different morphologies while mitigating task interference during pretraining. We further report unnormalized zero-shot errors in the original physical space in Appendix E.1, showing that the gains remain consistent under physically meaningful units. In addition, we visualize trajectory plots for all three robots in Fig. 2. We can see that WestWorld tracks the ground-truth dynamics substantially more closely than the baselines over the 100-step horizon. The reason is that, in a zero-shot setting on unseen but structurally similar systems, our model selects appropriate experts to produce accurate dynamics predictions, whereas baseline methods lack morphology-aware representations and fail to generalize.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Main Results", "weight": 1.0} -->

Evaluation on Few-shot Adaptation. To examine the benefits of pretraining for learning distinct robotic dynamics under limited data, we also evaluate few-shot performance on three real-world datasets that exhibit a significant domain gap from the pretraining distribution: i) Cassie bipedal jumping, ii) Unitree A1 quadruped locomotion (Tang et al., ), and iii) UR5 tabletop manipulation. For each dataset, we fine-tune using only 10 episodes, employ early stopping based on performance on a validation split, and report MAE and MSE on held-out test trajectories.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Main Results", "weight": 1.0} -->

We can see from Table 2 that our method consistently outperforms all baselines across the three robotic systems despite the large morphology and dynamics gap from the pretraining data. This demonstrates that the pretrained model provides a strong initialization and improves performance even when adapting to systems with substantial domain differences.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Main Results", "weight": 1.0} -->

To further quantify the impact of pretraining, we compare few-shot learning curves of WestWorld with and without pretraining. Overall, pretraining significantly improves final prediction accuracy across all three robots. Detailed results are provided in Appendix E.2.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Main Results", "weight": 1.0} -->

Evaluation on Scalability. We further verify the scalability of our method by varying the $N$ number of robotic environments while keeping the data budget per environment fixed. Specifically, we evaluate $N \in {\{ 1,2,5,10,20,30,50,60,89\}}$ environments. Due to the different data availability across the expanded settings, the exact training and evaluation splits vary slightly across $N$; detailed task-level subsets and split protocols are provided in Appendix C.4. We compare our method with the state-of-the-art TrajWorld under the same data split for each setting.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Main Results", "weight": 1.0} -->

All models take a 50-step history window as input and produce 100-step consecutive predictions. Fig. 4 reports the long-horizon prediction errors at each $N$ environments. We observe that the accuracy of our method remains low and does not vary significantly with increasing $N$. The results show that our method can simultaneously learn distinct system dynamics across diverse environments. Conversely, TrajWorld's performance degrades significantly as the number of environments increases. A plausible explanation is that optimizing a single shared model across multiple dissimilar dynamics exacerbates gradient interference and negative transfer, thereby limiting scalability.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Main Results", "weight": 1.0} -->

To further analyze scalability, we visualize Sys-MoE routing weights for three distinct systems in Fig. 3. Across systems, the router exhibits sparse, system-dependent expert selection. These results support our key insight: complex dynamics can be effectively approximated by composing a set of basis dynamics modules with system-dependent coefficients. Such system-aware design mitigates interference in multi-system joint learning and enables scalable pretraining across diverse robotic systems.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Main Results", "weight": 1.0} -->

Evaluation on Downstream Control Task. In addition, we evaluate whether pretraining improves downstream model-based control across diverse robotic systems, which aims to isolate the effect of pretraining on dynamics modeling. Jointly optimizing the controller or policy is a separate question and is not considered here. We consider three robotic systems with distinct dynamics: Walker2D, Hopper from OpenAI Gym, and Unitree Go1. For each system, we collect an offline trajectory dataset from the environment. We then compare two training regimes for each world model: (i) fine-tuning from a pretrained checkpoint and (ii) training from scratch under the same dataset. After training, we deploy the learned dynamics model within MPPI, a commonly used sampling-based MPC controller. Additional details of the MPPI implementation are provided in Appendix D.4.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Main Results", "weight": 1.0} -->

We set the MPPI planning horizon to $100$ for Walker2D and Hopper, and to $40$ for Go1. The setting is challenging: MPPI relies on long-horizon rollouts, so small model errors can compound and degrade control. In addition, the planner may explore actions that push the system outside the offline training distribution, further causing compounding errors and suboptimal control.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Main Results", "weight": 1.0} -->

Table 3 reports the accumulated episode reward. We draw two key observations. First, for nearly all methods and systems, pretraining consistently improves control performance compared with training from scratch. This suggests that pretraining yields dynamics representations that generalize better under distribution shift between offline training and online MPC rollouts. Second, WestWorld achieves the best performance across all three systems under both training regimes, with particularly large gains after pretraining. This indicates that our scalable model design and morphology-informed inductive bias significantly improve downstream control performance.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Main Results", "weight": 1.0} -->

Additionally, we conduct a real-world deployment on the Unitree Go1. For real-time execution, we distill WestWorld into a lightweight two-layer student model and fine-tune it using simulated Go1 control data. To provide a side-by-side comparison, we apply the same distillation, fine-tuning, and MPPI deployment protocol to the strongest baseline TrajWorld. In real-world deployment, the distilled WestWorld model successfully completes the straight-walking task toward the target goal (Fig. 5), while the distilled TrajWorld model fails to reliably stand up and walk forward. This result is consistent with the downstream control results in Table 3, where WestWorld achieves the best Go1 performance under the same MPPI setting.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Main Results", "weight": 1.0} -->

This setting is particularly challenging because MPPI relies on long-horizon rollouts, where small model errors can compound and degrade control performance. In addition, both models are trained and fine-tuned using simulation data, and sim-to-real gaps, including actuator and contact mismatch, ground friction variation, battery-dependent torque limits, and state-estimation noise, can further amplify rollout errors and lead to suboptimal control. Under this setting, the improved dynamics prediction of WestWorld enables more stable action selection in MPPI and transfers to real-world execution. Details of the distillation and deployment protocol are provided in Appendix G. A demo video is available at

<!-- chunk {"id": "body-0046", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

We also explore the impact of two core components on model performance: 1) knowledge-encoded embedding (KNEE) modular and 2) system-aware Mixture-of-Experts (Sys-MoE) layer. Both ablation studies are performed during pretraining and subsequently evaluated under the same zero-shot experimental setting using three robotic systems: Hopper, Walker2D, and Franka. We report long-horizon dynamics prediction errors using MAE and MSE.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Effect of the KNEE Modular. To isolate the role of structural inductive bias, we remove the knowledge-encoded structural embedding during pretraining (denoted as "w/o structural embedding"). As shown in Table 4, removing structural embedding leads to a clear degradation on Hopper and Walker2D, which have more complex morphologies, while the drop on Franka is smaller. This results show that structural embedding is particularly beneficial for unseen complex robotic systems, where explicitly modeling physical connectivity helps align trajectory representations with system structure and improves zero-shot generalization.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Effect of the Sys-MoE Layer. To assess the importance of the Sys-MoE layer, we replace it with a dense SSM layer. For a fair comparison, we increase the depth of the dense-SSM variant so that its total number of parameters is comparable to that of our model. As shown in Table 4, this replacement degrades performance across tasks despite comparable model capacity. These results indicate that the Sys-MoE design is critical for jointly modeling diverse robotic dynamics, as it mitigates inter-task interference during multi-system training.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Based on the ablation study, we conclude that both KNEE and Sys-MoE are essential for model generalization and scalable pretraining.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Discussion", "weight": 1.5} -->

We also study parameter-efficient fine-tuning and provide a detailed inference-time latency comparison against autoregressive transformer baselines. Detailed analyses are deferred to Appendix F.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion and Limitation", "weight": 1.5} -->

In this work, we introduced WestWorld, a knowledge-encoded scalable trajectory world model designed for diverse robotics dynamics. Specifically, the proposed model leverages a Sys-MoE block to scale across diverse robotics dynamics and integrates morphology-aware structural embeddings to improve generalization ability. Extensive experimental results show that it significantly improves zero- and few-shot prediction performance on unseen robotic systems, enhances model scalability, as well as boosts downstream model-based control performance.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion and Limitation", "weight": 1.5} -->

Despite its remarkable performance, WestWorld currently focuses on trajectory modeling and does not explicitly incorporate visual observations. In the future, we will extend WestWorld into a multimodal world model that fuses both vision and trajectory signals.
