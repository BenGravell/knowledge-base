## Introduction

Trajectory world models are essential for robotic dynamics learning, planning, and control based on low-level sensory data. However, building a trajectory world model for diverse robotic systems poses two key challenges: i) sensor and actuator heterogeneity, where the variance in types and sampling rates hinders shared representations, and ii) system dynamics gaps caused by diverse kinematic structures across different robotic systems.

To address these challenges, a few recent studies discretize continuous states and actions across diverse systems into tokens via quantization and leverage flexible Transformer architectures for joint training. Although these approaches enable multi-system pretraining within a single dense model, they still face scalability and generalization limitations across diverse robotic dynamics for two main reasons. First, existing approaches force different system dynamics to share a common set of model parameters, leading to gradient conflicts and negative transfer that impede effective scaling as robot diversity grows. Second, these methods overlook robot morphological information when modeling trajectories, thereby lacking the physical inductive biases required for zero-shot generalization to unseen robotic systems.

To overcome these limitations, we develop WestWorld, a knowledge-encoded scalable trajectory world model that incorporates domain knowledge of robot morphology to learn the underlying dynamics of diverse robotic systems (see Fig. 1). Developing such a model poses two key challenges: i) learning distinct system dynamics at scale while avoiding task interference across different robots, and ii) incorporating physical structural information as an inductive bias to enhance zero-shot generalization. To address the first challenge of scalability, we propose a system-aware mixture-of-experts (Sys-MoE) that implicitly learns distinct system dynamics through expert learning. Unlike existing trajectory world models, which learn multiple system dynamics using a single large dense model, the proposed Sys-MoE dynamically combines and routes specialized experts for different robotic systems via a learnable system embedding. This design mitigates task interference across robots, thus significantly improving scalability. For the second challenge of generalization, we introduce a structure-based channel embedding that aligns low-level state trajectories with morphology information, thereby improving the model's ability to generalize to unseen robotic systems.

We pretrain the proposed WestWorld on 89 complex environments using a combination of simulated and real-world data. Extensive experiments show that our method substantially outperforms strong baselines in both zero-shot and few-shot trajectory prediction. Moreover, it enables scalable training across diverse robotic systems without sacrificing performance and significantly improves the performance of downstream tasks such as model-based control.

Our contributions include: 1) We propose WestWorld, a novel system-aware MoE architecture for scaling up the training of trajectory world models across diverse robotic systems; 2) We introduce knowledge-encoded structural embedding that provides an explicit inductive bias to enhance zero- and few-shot generalization to unseen robotic systems; 3) We conduct extensive experiments to verify the scalability and generalizability of our method, showing its superiority over strong baselines; and 4) We apply our model to downstream model-based control and further extend it to real-world Unitree Go1 deployment, demonstrating its strong performance in planning tasks.

## Related Work

World Models for Single Robots. World models serve as a foundational tool for sequential decision-making in embodied agents, enabling them to model, understand, and predict environmental dynamics. In robotics, one line of work leverages video generation models as world models to synthesize temporally coherent observations, thereby implicitly capturing underlying physical dynamics. Another line of research develops action-conditioned *dynamics* world models that explicitly predict future states for planning and control. These dynamics world models can be broadly categorized into video world models and trajectory world models, offering complementary perspectives for learning physical dynamics.

In this work, we focus on studying low-level trajectory world models. Generalizing such models across diverse robotic systems is non-trivial, since trajectories are derived from heterogeneous sensors and actuators with mismatched channel semantics across systems. Thus, most existing trajectory world models are tailored to a single robot, and transferring to new platforms typically requires retraining or substantial adaptation. In contrast, our work aims to learn a unified trajectory world model that scales across diverse robotic systems.

Trajectory World Model for Diverse Robotics. Recent works have explored trajectory world models for diverse robotic systems. A key challenge is handling varying sensor and actuator dimensionalities across different robots. A common strategy is to zero-pad inputs to a shared maximum dimension. However, padding-based approaches suffer from dimensionality limits and often degrade generalization across environments. To address this, a few recent studies treat states and actions as token sequences and jointly train flexible Transformer architectures across multiple robots. Despite enabling joint pretraining across diverse robots, their scalability and generalization remain limited. First, most existing methods learn heterogeneous robotic systems using a single shared set of model parameters, which induces cross-system interference as robot diversity grows and makes scaling difficult. Second, these methods treat trajectories purely as token sequences while ignoring robot morphology information, which results in poor zero-shot generalization to unseen robotics.

Unlike prior works, we propose a system-aware MoE model that incorporates robot structural information to enable both scalable pretraining and strong zero-shot performance.

## Preliminaries

Figure 1: The overall architecture of our proposed WestWorld, consisting of two core components: (a) a Knowledge-Encoded Embedding Modular that injects structural embeddings as an inductive bias into trajectory representations, and (b) a System-aware MoE block that models diverse system dynamics via system-aware expert routing.

Notations. The detailed descriptions of important notations are presented in Table 5 in Appendix A.

Problem Statement. A robotic system can be viewed as a controlled dynamical process with state space $\mathcal{S}$, action space $\mathcal{A}$, and transition dynamics $\mathbf{f}$. In practice, the state ${\mathbf{s}}_{t} \in \mathcal{S}$ consists of physical sensor readings such as joint positions and joint velocities, while the action ${\mathbf{a}}_{t} \in \mathcal{A}$ represents control commands such as joint torques. Model-based control relies on an internal dynamics model to support planning by rolling out candidate action sequences in imagination.

In this work, we use a *trajectory world model* purely as a dynamics model that predicts future states $\mathbf{s}$ conditioned on action interactions $\mathbf{a}$. Formally, a world model parameterizes a transition distribution

which can be used to unroll state trajectories under a proposed action sequence. A rollout induces a trajectory

and the model is trained on the recorded trajectories $\mathcal{D} = {\{\tau_{i}\}}$ by maximizing predictive accuracy of future states.

The goal of this work is to develop a pretrained trajectory world model to learn the system dynamics across varying robotic systems and environments. Given a trajectory dataset from $n$ distinct robotic systems, $\{\mathcal{D}_{1},\mathcal{D}_{2},\ldots,\mathcal{D}_{n}\}$, our objective is to learn a single model $\theta$ that captures the dynamics of all $n$ systems. Specifically, given a history of $h$ past states and actions, the model tries to predict the next $k$ future states, conditioned on a sequence of $k$ future actions.

## Proposed Method

### Overview of WestWorld

To enable scalable pretraining and zero-shot generalization across diverse robotic systems, we propose WestWorld, a knowledge-encoded scalable trajectory world model with a system-aware Mixture-of-Experts (MoE) design. As shown in Fig. 1, the proposed model consists of two core components: Knowledge-Encoded Embedding Modular and System-Aware MoE.

The core idea is to first perform channel-wise normalization and discretize each scalar variable for tokenization. The resulting representations are then processed by Knowledge-Encoded Embedding Modular, which extracts the robot's morphological connectivity and injects structural embeddings as an inductive bias into trajectory representations. These structure-aware embeddings are subsequently fed into multiple System-Aware MoE blocks for dynamics modeling. Finally, a linear decoder maps the hidden states to future trajectory predictions. We detail these two core components in the following.

### Knowledge-Encoded Embedding Modular

Motivation. Existing trajectory world models are predominantly data-driven, relying solely on state-action observations and largely ignoring domain knowledge that different robotic morphologies should obey distinct physical constraints. The lack of encoding explicit structural information makes it difficult for these models to capture the underlying system dynamics and limits their ability to generalize across environments. We hypothesize that robots with similar connectivity patterns often exhibit shared high-level dynamical behaviors (e.g., SLIP-like locomotion ). This insight motivates us to incorporate morphological connectivity into model design as an inductive bias. Below, we first introduce the trajectory data tokenization before diving into proposed knowledge-encoded structural embedding.

Trajectory Tokenization. Given a trajectory, we treat each state or action dimension at time step $t$ as a *scalar channel*. Let $x_{t}^{(m)} \in {\mathbb{R}}$ denote the value of channel $m$ at time $t$, where $m$ represents the index of state channels or action channels. We apply channel-wise min--max normalization, and discretize it into a $K$-bin categorical vector through $\mathbf{\phi}:{{\mathbb{R}}\rightarrow{\mathbb{R}}^{K}}$ following. We further analyze the effect of different numbers of bins in Appendix D.2. We then map $\mathbf{\phi}{(x_{t}^{(m)})}$ to a $d$-dimensional embedding via a learned projection. After that, we incorporate timestep embeddings, channel order index embeddings, and modality indicator (state or action) embeddings, yielding ${\mathbf{z}}_{t}^{(m)} \in {\mathbb{R}}^{d}$. For convenience, we stack the per-channel embeddings from states and actions at time step $t$ into ${\mathbf{S}}_{t} \triangleq {\lbrack{\mathbf{s}}_{t}^{},\ldots,{\mathbf{s}}_{t}^{(M_{s})}\rbrack}^{\top} \in {\mathbb{R}}^{M_{s} \times d}$ and ${\mathbf{A}}_{t} \triangleq {\lbrack{\mathbf{a}}_{t}^{},\ldots,{\mathbf{a}}_{t}^{(M_{a})}\rbrack}^{\top} \in {\mathbb{R}}^{M_{a} \times d}$, where $M_{s}$ and $M_{a}$ are the numbers of state and action channels.

Knowledge-Encoded Structural Embedding. To incorporate morphology structure priors into latent representations, we introduce a knowledge-encoded structural embedding, as shown in Fig. 1 (a). Specifically, we first model each articulated object as a rooted kinematic tree and convert it to a binary tree using the left-child-right-sibling (LCRS) transformation. Each body node is assigned three traversal indices from pre-/in-/post-order walks. For object $i$ and its body node $j$, let $\left( \pi_{pre}^{i,j},\pi_{in}^{i,j},\pi_{post}^{i,j} \right)$ denote these indices. In scenes with multiple articulated objects, we additionally assign an object identifier $\pi_{obj}^{i}$: the robot is indexed as $\pi_{obj}^{i} = 0$, and other objects are ordered by increasing Euclidean distance to the robot (see Appendix B for an example). With this tuple indices, we can uniquely identify each robot body node in the LCRS-converted binary tree derived from the robot's structure. Then, we embed these indices to obtain a structure embedding:

where each ${\mathbf{e}}_{\{{obj},{pre},{in},{post}\}}{( \cdot )}$ denotes a structural encoder that maps a discrete index to a $d/4$-dimensional vector, and their concatenation forms ${\mathbf{p}}^{(i,j)} \in {\mathbb{R}}^{d}$. Finally, we inject morphology knowledge by adding ${\mathbf{p}}^{(i,j)}$ to the corresponding state/action embeddings, yielding structure-aware trajectory embeddings that are used as inputs to our model.

### System-Aware MoE Block

Motivation. Robotic systems with diverse morphologies often exhibit markedly different dynamics, making it difficult to develop a single unified model that accurately captures their underlying dynamics. When such dissimilar dynamics are trained simultaneously using shared parameters, optimization is prone to gradient conflicts and task interference, leading to poor scalability. To address this challenge, we introduce a novel system-aware Mixture-of-Experts (Sys-MoE) block for learning distinct system dynamics, in which each expert tries to learn part of underlying system dynamics. Our key insight is that complex system dynamics can be effectively approximated by composing a set of basis dynamics with system-dependent coefficients.

Block design. To scale joint training across diverse robotic systems while mitigating interference, we parameterize the transition model in Eq. with a stack of *Sys-MoE Blocks*. Each block contains two parts: i) an attention-based aggregation module that fuses state--action information, and ii) a system-aware MoE layer that captures diverse system dynamics. We detail the two parts below.

i\) Attention-based aggregation. As shown in Fig. 1(b), we use attention to aggregate information across state channels and to inject action-dependent control signals, while naturally supporting variable state/action dimensionalities across systems. Concretely, we apply: 1) self-attention to capture correlations among state variables, and then use 2) cross-attention to condition state features on the action embeddings. To enable $k$-step prediction in a single forward pass, we concatenate the history state embeddings with $k$ learnable query embeddings $\{{\mathbf{q}}_{t},\ldots,{\mathbf{q}}_{{t + k} - 1}\}$, which serve as latent queries for future states.

At each time step, self-attention is computed as

where self-attention is applied along the state channel, and ${LN}{( \cdot )}$ is layer normalization. We then condition ${\overset{\sim}{\mathbf{S}}}_{t}$ on the action embeddings ${\mathbf{A}}_{t}$ via multi-head cross-attention:

This operation injects action-dependent signals while remaining compatible with variable action dimensionalities.

ii\) System-aware MoE layer. After obtaining the action-conditioned latent states above, we model continuous-time system dynamics using a system-aware Mixture-of-Experts (Sys-MoE) layer, as shown in Fig. 1(b). Unlike the MoE design commonly used in large language models, where routing selects experts to directly produce token embeddings from the input, our routing is *system-aware*. Specifically, we introduce a learnable system embedding that propagates through the SSM to extract system-level properties of the underlying dynamics. The resulting system embeddings are then used to compute mixture weights over experts, so that the model forms a system-conditioned combination of different experts.

Let $L = {h + k}$ be the number of state embeddings after concatenating history states with $k$ queries. For each state channel $m$, we denote the attention outputs as ${\hat{\mathbf{S}}}_{1:L}^{(m)} = {\{{\hat{\mathbf{s}}}_{{t - h}:{t - 1}}^{(m)},{\hat{\mathbf{s}}}_{t:{{t + k} - 1}}^{(m)}\}}$, where the last $k$ tokens correspond to the query positions. We append a learnable system embedding ${\mathbf{e}} \in {\mathbb{R}}^{d}$ to attention outputs, yielding

We apply an SSM layer to obtain outputs ${\mathbf{U}}_{\ell}$:

where ${\mathbf{U}}_{1:{L + 1}}^{(m)}$ denotes the SSM outputs for all embeddings. In our implementation, ${SSM}{( \cdot )}$ follows a Mamba-style selective SSM, enabling causal computation and efficient long-range dependency modeling.

We use the output of the system embedding, ${\mathbf{U}}_{L + 1}$, to extract system-aware properties for routing. A router produces mixture weights over $P$ experts via a softmax gate:

Given the output ${\mathbf{U}}_{1:L}^{(m)}$, the Sys-MoE block outputs ${\mathbf{Y}}_{1:L}^{(m)}$ is computed as a weighted combination of expert predictions:

where $w_{p}$ is the $p$-th entry of $\mathbf{w}$, and each expert $E_{p}{( \cdot )}$ is implemented as an MLP. Finally, we stack multiple Sys-MoE blocks to increase expressivity for complex system dynamics.

### Objective Function

After stacking Sys-MoE Blocks, we obtain the per-channel output sequence ${\mathbf{Y}}_{1:L}^{(m)}$ We apply a linear decoder head to produce logits over $K$ uniform bins. Concretely, for each channel $m$ outputs, we compute

We train the model with a next-token cross-entropy loss on the state channels to match the categorical representation of the inputs:

During inference time, we run the model in a sequence-to-sequence manner, enabling multi-step prediction in a single forward pass.

Figure 2: Trajectory plot comparison of our method and three baselines for 100-step rollout prediction on three robots: Walker2D foot joint angle, Hopper foot angular velocity, and Franka end-effector y position, given a 50-step history window as input. We can observe that our method tracks the ground-truth dynamics substantially more closely than the baselines over the 100-step horizon.

## Experiments

In this section, we pretrain WestWorld on large-scale, diverse robotic datasets and conduct extensive experiments to evaluate: (i) zero-shot generalization to unseen environments, (ii) few-shot adaptation under domain shifts, (iii) scalability as the number of pretraining environments increases, and (iv) improvements in downstream control tasks across diverse robotic systems enabled by pretraining.

Diverse Pretraining Datasets. For pretraining the proposed trajectory world model, we collect a large amount of simulated and real-world data: i) UniTraj dataset, which contains 80 simulated robotic environments; and ii) 9 real-world robot-arm datasets from the Open X-Embodiment. A detailed list of the pretraining and evaluation environments used in our experiments is provided in Appendix C.

Baseline Methods. We compare our method against several state-of-the-art trajectory world models. MLP Ensemble: a widely used baseline in model-based RL for learning probabilistic dynamics through an ensemble of multilayer perceptrons. TDM: a Transformer-based model built upon the Gato architecture, which flattens spatial and temporal features into a single sequence and applies one-dimensional attention for autoregressive prediction. TrajWorld: a Transformer-based trajectory model that employs temporal-variate attention for autoregressive rollout.

Implementation Details. We follow each baseline's original pretraining configuration. Detailed training and implementation settings for WestWorld and all baselines are provided in Appendix D. For fairness, all baseline models are pretrained from scratch on the above same dataset as the proposed WestWorld.

### Main Results

Table 1: Zero-shot generalization performance of different models on three dynamical systems. Errors are computed in the normalized space and reported as MAE and MSE ( × 10−2); lower is better.

Table 2: Few-shot generalization performance on three robotic systems. Results are computed in the normalized space and reported as MAE and MSE ( × 10−2) averaged over three random seeds (mean ± standard deviation); lower is better.

Figure 3: Sys-MoE routing weights across six layers (L1–L6), each containing four experts (E1–E4), for three robotic systems. Color indicates the router weight, where brighter values correspond to higher expert activation. The router exhibits near-sparse, system-dependent expert specialization, suggesting that different systems are modeled by different combinations of experts to capture their distinct dynamics.

Evaluation on Zero-shot Performance. We first evaluate the zero-shot performance of our model on three unseen robotic environments that share similar structural morphology with those in the pretraining data. Specifically, we use datasets from three environments as our testbeds. These include Hopper and Walker2D from D4RL, as well as a real-world dataset of a mobile Franka manipulator interacting with articulated objects. We evaluate 100-step consecutive predictions using a 50-step history window as input. Mean Absolute Error (MAE) and Mean Squared Error (MSE) are used to assess the accuracy of long-horizon prediction.

As shown in Table 1, our method achieves the best performance across all three unseen environments in long-horizon prediction. This improvement is attributed to the combination of our system-aware MoE architecture and the structural inductive bias introduced through morphology-aware design. The MoE design enables the model to learn distinct dynamics for different morphologies while mitigating task interference during pretraining. We further report unnormalized zero-shot errors in the original physical space in Appendix E.1, showing that the gains remain consistent under physically meaningful units. In addition, we visualize trajectory plots for all three robots in Fig. 2. We can see that WestWorld tracks the ground-truth dynamics substantially more closely than the baselines over the 100-step horizon. The reason is that, in a zero-shot setting on unseen but structurally similar systems, our model selects appropriate experts to produce accurate dynamics predictions, whereas baseline methods lack morphology-aware representations and fail to generalize.

Evaluation on Few-shot Adaptation. To examine the benefits of pretraining for learning distinct robotic dynamics under limited data, we also evaluate few-shot performance on three real-world datasets that exhibit a significant domain gap from the pretraining distribution: i) Cassie bipedal jumping, ii) Unitree A1 quadruped locomotion (Tang et al., ), and iii) UR5 tabletop manipulation. For each dataset, we fine-tune using only 10 episodes, employ early stopping based on performance on a validation split, and report MAE and MSE on held-out test trajectories.

We can see from Table 2 that our method consistently outperforms all baselines across the three robotic systems despite the large morphology and dynamics gap from the pretraining data. This demonstrates that the pretrained model provides a strong initialization and improves performance even when adapting to systems with substantial domain differences.

To further quantify the impact of pretraining, we compare few-shot learning curves of WestWorld with and without pretraining. Overall, pretraining significantly improves final prediction accuracy across all three robots. Detailed results are provided in Appendix E.2.

Figure 4: Comparison between our method against the best performing SOTA by scaling the number of environments.

Evaluation on Scalability. We further verify the scalability of our method by varying the $N$ number of robotic environments while keeping the data budget per environment fixed. Specifically, we evaluate $N \in {\{ 1,2,5,10,20,30,50,60,89\}}$ environments. Due to the different data availability across the expanded settings, the exact training and evaluation splits vary slightly across $N$; detailed task-level subsets and split protocols are provided in Appendix C.4. We compare our method with the state-of-the-art TrajWorld under the same data split for each setting.

All models take a 50-step history window as input and produce 100-step consecutive predictions. Fig. 4 reports the long-horizon prediction errors at each $N$ environments. We observe that the accuracy of our method remains low and does not vary significantly with increasing $N$. The results show that our method can simultaneously learn distinct system dynamics across diverse environments. Conversely, TrajWorld's performance degrades significantly as the number of environments increases. A plausible explanation is that optimizing a single shared model across multiple dissimilar dynamics exacerbates gradient interference and negative transfer, thereby limiting scalability.

To further analyze scalability, we visualize Sys-MoE routing weights for three distinct systems in Fig. 3. Across systems, the router exhibits sparse, system-dependent expert selection. These results support our key insight: complex dynamics can be effectively approximated by composing a set of basis dynamics modules with system-dependent coefficients. Such system-aware design mitigates interference in multi-system joint learning and enables scalable pretraining across diverse robotic systems.

Table 3: Downstream model-based control performance using MPPI on Walker2D, Hopper, and Unitree Go1. We report accumulated episode reward (higher is better) averaged over the evaluation episodes. All methods are evaluated with fixed random seeds and identical MPPI hyperparameters for fair comparison.

Ours w/o Structural embedding

Table 4: Ablation results under the zero-shot setting. We ablate the Sys-MoE layer by replacing it with a dense SSM, and ablate the structural encoding by removing it during pretraining. Results are computed in the normalized space and reported as MAE and MSE ( × 10−2); lower is better.

Evaluation on Downstream Control Task. In addition, we evaluate whether pretraining improves downstream model-based control across diverse robotic systems, which aims to isolate the effect of pretraining on dynamics modeling. Jointly optimizing the controller or policy is a separate question and is not considered here. We consider three robotic systems with distinct dynamics: Walker2D, Hopper from OpenAI Gym, and Unitree Go1. For each system, we collect an offline trajectory dataset from the environment. We then compare two training regimes for each world model: (i) fine-tuning from a pretrained checkpoint and (ii) training from scratch under the same dataset. After training, we deploy the learned dynamics model within MPPI, a commonly used sampling-based MPC controller. Additional details of the MPPI implementation are provided in Appendix D.4.

We set the MPPI planning horizon to $100$ for Walker2D and Hopper, and to $40$ for Go1. The setting is challenging: MPPI relies on long-horizon rollouts, so small model errors can compound and degrade control. In addition, the planner may explore actions that push the system outside the offline training distribution, further causing compounding errors and suboptimal control.

Table 3 reports the accumulated episode reward. We draw two key observations. First, for nearly all methods and systems, pretraining consistently improves control performance compared with training from scratch. This suggests that pretraining yields dynamics representations that generalize better under distribution shift between offline training and online MPC rollouts. Second, WestWorld achieves the best performance across all three systems under both training regimes, with particularly large gains after pretraining. This indicates that our scalable model design and morphology-informed inductive bias significantly improve downstream control performance.

Additionally, we conduct a real-world deployment on the Unitree Go1. For real-time execution, we distill WestWorld into a lightweight two-layer student model and fine-tune it using simulated Go1 control data. To provide a side-by-side comparison, we apply the same distillation, fine-tuning, and MPPI deployment protocol to the strongest baseline TrajWorld. In real-world deployment, the distilled WestWorld model successfully completes the straight-walking task toward the target goal (Fig. 5), while the distilled TrajWorld model fails to reliably stand up and walk forward. This result is consistent with the downstream control results in Table 3, where WestWorld achieves the best Go1 performance under the same MPPI setting.

This setting is particularly challenging because MPPI relies on long-horizon rollouts, where small model errors can compound and degrade control performance. In addition, both models are trained and fine-tuned using simulation data, and sim-to-real gaps, including actuator and contact mismatch, ground friction variation, battery-dependent torque limits, and state-estimation noise, can further amplify rollout errors and lead to suboptimal control. Under this setting, the improved dynamics prediction of WestWorld enables more stable action selection in MPPI and transfers to real-world execution. Details of the distillation and deployment protocol are provided in Appendix G. A demo video is available at

Figure 5: Real-world deployment on Unitree Go1. The distilled-and-fine-tuned WestWorld serves as the dynamics predictor in MPPI and enables the robot to walk straight toward the target goal. A side-by-side comparison with TrajWorld is provided in the project website at

### Ablation Studies

We also explore the impact of two core components on model performance: 1) knowledge-encoded embedding (KNEE) modular and 2) system-aware Mixture-of-Experts (Sys-MoE) layer. Both ablation studies are performed during pretraining and subsequently evaluated under the same zero-shot experimental setting using three robotic systems: Hopper, Walker2D, and Franka. We report long-horizon dynamics prediction errors using MAE and MSE.

Effect of the KNEE Modular. To isolate the role of structural inductive bias, we remove the knowledge-encoded structural embedding during pretraining (denoted as "w/o structural embedding"). As shown in Table 4, removing structural embedding leads to a clear degradation on Hopper and Walker2D, which have more complex morphologies, while the drop on Franka is smaller. This results show that structural embedding is particularly beneficial for unseen complex robotic systems, where explicitly modeling physical connectivity helps align trajectory representations with system structure and improves zero-shot generalization.

Effect of the Sys-MoE Layer. To assess the importance of the Sys-MoE layer, we replace it with a dense SSM layer. For a fair comparison, we increase the depth of the dense-SSM variant so that its total number of parameters is comparable to that of our model. As shown in Table 4, this replacement degrades performance across tasks despite comparable model capacity. These results indicate that the Sys-MoE design is critical for jointly modeling diverse robotic dynamics, as it mitigates inter-task interference during multi-system training.

Based on the ablation study, we conclude that both KNEE and Sys-MoE are essential for model generalization and scalable pretraining.

### Discussion

We also study parameter-efficient fine-tuning and provide a detailed inference-time latency comparison against autoregressive transformer baselines. Detailed analyses are deferred to Appendix F.

## Conclusion and Limitation

In this work, we introduced WestWorld, a knowledge-encoded scalable trajectory world model designed for diverse robotics dynamics. Specifically, the proposed model leverages a Sys-MoE block to scale across diverse robotics dynamics and integrates morphology-aware structural embeddings to improve generalization ability. Extensive experimental results show that it significantly improves zero- and few-shot prediction performance on unseen robotic systems, enhances model scalability, as well as boosts downstream model-based control performance.

Despite its remarkable performance, WestWorld currently focuses on trajectory modeling and does not explicitly incorporate visual observations. In the future, we will extend WestWorld into a multimodal world model that fuses both vision and trajectory signals.
