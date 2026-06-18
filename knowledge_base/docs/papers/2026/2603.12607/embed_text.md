## Introduction

Autonomous driving requires robust motion planning to navigate complex and dynamic traffic environments safely and efficiently. Traditional planning approaches have predominantly relied on rule-based algorithms, where the behavior of an autonomous vehicle (AV) is explicitly defined through handcrafted rules. While these methods provide interpretable decision-making, they demand substantial engineering effort to design and modify rules in various driving environments, resulting in a lack of adaptability to new traffic scenarios. To overcome these challenges, Imitation Learning (IL) has emerged as a promising alternative, enabling models to learn driving policies directly from expert human demonstrations. By leveraging large-scale real-world datasets, such as nuPlan, IL-based approaches can capture a wide range of driving behaviors without relying on manually defined rules or reward functions.

Most IL-based planners are trained by minimizing trajectory imitation losses that measure the distance between predicted trajectories and ground-truth (GT) trajectories. However, such objectives are not always aligned with real-world driving requirements, such as collision avoidance or road boundary compliance. In some cases, IL models prioritize generating trajectories that closely match the GT rather than actively avoiding collisions, as illustrated in Figure 1. This observation indicates that motion planning is not merely about matching human trajectories, but about correctly understanding the driving context and selecting appropriate actions accordingly. In real-world driving situations, diverse environmental factors (e.g., vehicles, pedestrians, and road structures) interact simultaneously in complex ways, and different combinations of these factors lead to distinct decision-making criteria. Therefore, robust IL-based planning requires both accurate context understanding of the driving scene and the ability to perform context-adaptive planning, adjusting driving strategies according to the situation.

Accurately understanding driving context requires the ability to capture how the surrounding environment evolves over time. This evolution is not solely characterized by the independent motions of nearby objects, but by the evolving spatial relationships between the autonomous vehicle and its surrounding environment. Such relational dynamics reflect driving patterns implicitly inherent in human demonstration data and should be explicitly learned for robust IL-based planning. However, many existing IL-based planners predominantly rely on independent future predictions of individual agents, often limited to vehicles, without sufficiently modeling their spatial relationships with broader scene elements such as road structures or static obstacles, leading to insufficient relational modeling in scene representations.

Beyond context understanding, context-adaptive planning requires the ability to adjust driving strategies across situations. Even when driving situations appear similar, appropriate driving strategies can differ depending on the surrounding context and interaction patterns, making them difficult to handle with a single fixed policy. However, existing IL-based planners rely on a single shared policy network, which biases learning toward common scenarios and limits the model's ability to reflect behavior variations required across different contexts. As a result, these planners are vulnerable to adopting adaptive driving strategies in complex or rarely encountered driving situations.

To address these limitations, we propose CarPLAN (Context-Adaptive and Robust Planner), a novel IL-based motion planning framework designed to jointly achieve nuanced context understanding and context-adaptive planning. CarPLAN is built on the key insight that robust planning requires not only capturing rich contextual information from driving scenes, but also adapting driving strategies based on the captured context. Accordingly, CarPLAN explicitly models the contextual structure of the scene and leverages it to guide adaptive decision-making across diverse driving situations.

Specifically, we aim to equip the encoder with enhanced spatial awareness of surrounding elements---such as vehicles, pedestrians, lanes, and road boundaries---relative to the ego vehicle. To this end, we introduce the Displacement-Aware Predictive Loss, a self-supervised objective that enforces predictive constraints on the displacement between the ego vehicle and surrounding scene elements. We design the Displacement-Aware Predictive Encoder (DPE), which forecasts future displacement vectors between the AV and nearby entities based on their current relative positions (see Figure LABEL:fig:intro). The Displacement-Aware Predictive Loss measures the deviation between the predicted and ground-truth displacement vectors, guiding the encoder to encode spatial relationships with surrounding objects in its feature representations. Importantly, the DPE functions solely as a training-time supervisory signal and can be deactivated during inference, introducing no additional runtime computational overhead.

Figure 1: Challenges in imitation learning. Minimizing imitation loss alone does not guarantee safe planning. This example demonstrates that a lower L1 loss could result in lane departures or collisions.

We also introduce the Context-Adaptive Multi-Expert Decoder (CMD), which leverages a set of specialized expert networks tailored to different driving contexts. We integrate the Mixture of Experts (MoE) framework, a proven approach in large language models for enhancing performance on complex tasks, into the decoder in our CarPLAN. By dynamically selecting the most relevant experts based on the scene context, our approach improves adaptability and robustness in decision-making across diverse driving conditions. To support this mechanism, we further design a Scene-Aware Router, which analyzes the dynamic scene structure to determine the most suitable expert network for each planning instance.

We evaluate CarPLAN on the widely used nuPlan benchmark. Our CarPLAN achieved state-of-the-art (SOTA) performance across all closed-loop simulation metrics. In particular, it attained a remarkable score of 84.6 in the reactive simulation and 91.4 in the non-reactive simulation on the benchmark. Furthermore, CarPLAN demonstrated robust performance on the more challenging -Hard, which includes complex and difficult driving scenarios. To further examine generalization ability, we also conducted a reactive simulation on the Waymax benchmark, where CarPLAN consistently achieved performance improvements over baseline methods across diverse scenarios.

The main contributions of this paper are summarized below:

We propose CarPLAN, a novel approach for IL-based motion planning that enhances the model's awareness of its surroundings, the proposed DPE predicts future displacement vectors between AV and objects in the scene.

CarPLAN adopts MoE for context-adaptive planning in diverse environments. This idea enhances the planner's ability to interpret and adapt to varying scenes, resulting in improved trajectory planning.

CarPLAN achieves SOTA performance on nuPlan benchmark and demonstrates strong robustness and generalization on challenging benchmarks, including -Hard and Waymax.

## Related works

### II-A Imitation Learning-based Planning

Imitation Learning has emerged as a prominent approach for motion planning in autonomous driving, as it enables models to learn directly from expert demonstrations without relying on handcrafted rules or explicit reward functions. PlanTF addressed spurious correlations in imitation learning by using only the AV's present state and introduced the AV states dropout that was selectively masked during training to prevent reliance on specific kinematic states. PLUTO mitigated causal confusion in imitation learning through contrastive learning with data augmentation, using negative samples such as leading agent dropout and traffic light inversion. RaSc introduced a risk-aware planning approach by leveraging pairwise TTC with other agents. To learn risk awareness, it enforced self-consistency by predicting pairwise TTC for all agents and aligning its planned trajectories with these predictions. BeTopNet enhanced prediction and planning consistency by explicitly modeling multi-agent future behaviors through topological reasoning based on braid theory. Diffusion-Planner proposed a transformer-based diffusion model that refines future trajectories through iterative denoising, capturing interaction-aware behaviors and enabling rule-free planning via classifier guidance. CarPlanner introduced a consistent auto-regressive trajectory planner that sequentially generates future steps conditioned on previous outputs, incorporating mode-consistent sampling and expert-guided rewards.

### II-B Mixture of Experts

The Mixture of Experts (MoE) architecture dynamically activates multiple specialized experts based on input contexts, efficiently allocating model capacity to enhance task performance. Recent advances have demonstrated its effectiveness across diverse domains. Switch Transformer utilized sparse expert activation for computational efficiency and large-scale model scalability. DeepseekMoE introduced shared and routed experts to minimize redundancy by clearly separating common and specialized knowledge. Expert-choice routing allowed each expert to specialize in specific subsets of input distributions, increasing overall model adaptability. FLAN-MOE demonstrated improved performance by integrating instruction-tuning with the MoE framework, enhancing experts' task-specific specialization.

Figure 2: Overall structure of CarPLAN. CarPLAN comprises two main networks: DPE and CMD. DPE is trained to predict the displacements or velocity between the AV and surrounding scene elements at each future timestep, generating Displacement-Aware Features. CMD utilizes multiple experts, dynamically selected by the Scene-Aware Router, to generate the AV’s future trajectory.

## CarPLAN

### III-A Overview

The overall architecture of CarPLAN is depicted in Figure 2. CarPLAN first encodes input data consisting of the AV, surrounding agents, and high-definition (HD) map through Scene Encoder, generating comprehensive scene context features. Subsequently, the Displacement Predictor predicts future displacement between the AV and surrounding scene elements, producing Displacement-Aware Features. These features are trained to encode relative spacing from surrounding objects through the Displacement-Aware Predictive Loss, which enforces predictive self-supervised constraints on displacement vectors. Next, given a Trajectory Query $Q_{traj}$, the Scene-Aware Router dynamically selects the most relevant expert networks by analyzing the $Q_{traj}$ jointly with the Displacement-Aware Features. Specifically, it selects the top-$K$ Routed Experts. The selected experts extract scenario-specific features tailored to the current driving context, while Shared Experts extract general driving features. Both features are aggregated and then used by the Trajectory Head and Score Head to generate the AV's $M$ multi-modal future trajectories with their confidence scores.

### III-B Problem Formulation

This work addresses the critical challenge of AV planning in complex urban environments, aiming to generate safe future trajectories that consider the scene contexts and interactions with dynamic agents (e.g., vehicles, bicycles, and pedestrians). We consider a driving scene consisting of an AV, surrounding agents, and a vectorized map. The state information of all agents over the historical horizon $T_{h}$ is represented as $A_{0:N_{a}} = {\{ A_{a}^{{- T_{h}}:0}\}}_{a = 0}^{N_{a}}$, where $A_{0}$ corresponds to the states of the AV, and $A_{1:N_{a}}$ represents those of the surrounding agents. Each state includes the position, heading, velocity, size, and category of the agent. For the vectorized map, we define $P_{1:N_{p}}$ as a collection of map elements, represented as points that compose lane geometry, crosswalks, road boundaries, and so . Additionally, multiple centerlines in the form of polylines are provided as guidance for the AV to navigate toward its goal position, denoted as $L_{g} = {\{ L_{k}\}}_{k = 1}^{N_{K}}$, where $N_{K}$ represents the number of centerlines connected to the goal in the current scene. The goal position corresponds to the last point of a long logged sequence, which is much longer than the planned trajectory's prediction horizon. Given all these conditions, the objective of planning is to generate the $M$ trajectory states of AV over $T_{f}$ future time steps, $\hat{Y} = {\{{\hat{y}}_{m}^{1:T_{f}}\}}_{m = 1}^{M}$ and their corresponding confidence scores $\hat{C} = {\{{\hat{c}}_{m}\}}_{m = 1}^{M}$.

### III-C Displacement-Aware Predictive Encoder

DPE consists of the Scene Encoder and the Displacement Predictor. The Scene Encoder employs the Transformer Encoder to generate a unified representation of the overall scene, capturing interactions among traffic participants. The Displacement Predictor utilizes the unified scene representation to forecast the future displacement of the AV relative to each surrounding element.

### III-C1 Scene Encoder

The Scene Encoder processes $A_{0}$, $A_{1:N_{a}}$, and $P_{1:N_{p}}$ to encode them jointly through Transformer. Specifically, these elements are encoded into $S_{av}$, $S_{agent}$, and $S_{map}$ using modality-specific encoding modules, as suggested . These encoded features are concatenated as $S = {\lbrack S_{av};S_{agent};S_{map}\rbrack}$, and then fed to a Transformer Encoder to generate the scene context features $S^{\prime} = {\lbrack S_{av}^{\prime};S_{agent}^{\prime};S_{map}^{\prime}\rbrack} \in {\mathbb{R}}^{{({1 + N_{a} + N_{p}})} \times D}$, where $\lbrack \cdot \rbrack$ denotes a concatenation operation.

### III-C2 Displacement Predictor

The Displacement Predictor guides the Scene Encoder to generate Displacement-Aware Features $F^{D} = S^{\prime}$, which encode information on relative spacing to scene elements. This is achieved by training DPE to predict future displacement vectors between the AV and surrounding traffic and dynamic objects. To effectively capture the relational information between the AV and the neighboring agents, we concatenate the AV feature $F_{av}^{D}$ with the agent features $F_{agent}^{D}$ channel-wise, resulting in the features $F_{agent}$. Similarly, we concatenate $F_{av}^{D}$ with the map features $F_{map}^{D}$ channel-wise to obtain $F_{map}$. Then, after concatenating $F_{agent}$ and $F_{map}$, DispHead is applied to predict the displacement vectors at $T_{f}$ future timesteps, i.e.,

where $\text{DispHead}{( \cdot )}$ consists of two MLP layers. Note that the process of predicting the future displacement is performed only during the training phase, not during inference.

### III-D Context-Adaptive Multi-Expert Decoder

CMD utilizes the MoE framework to enable context-adaptive planning across diverse driving scenarios. It consists of multiple iterative decoding layers, each incorporating a Scene-Aware Router and Scene-Specific Experts. The Trajectory Query $Q_{traj}$ is initialized from centerlines $L_{g}$ using the encoding method proposed in and is iteratively refined across multiple layers.

Scene-Specific Experts employ multiple expert decoders to generate the AV's future trajectory based on Displacement-Aware Features and Trajectory Queries. We utilize two types of experts: $N$ Routed Experts and $N_{s}$ Shared Experts. These expert decoders refine the Trajectory Query while capturing semantic scene information.

The Scene-Aware Router processes Displacement-Aware Features to extract high-level scene representations, which are then used to select the most suitable Top-$K$ Routed Experts. Notably, Shared Experts are always activated, regardless of expert selection. Finally, the Trajectory Head and Score Head predict the AV's future trajectories and their corresponding confidence scores.

### III-D1 Scene-Aware Router

The Scene-Aware Router produces the probability scores for Routed Experts based on Trajectory Query $Q_{traj}$ and Displacement-Aware Features $F^{D}$. Using $Q_{traj}$ as the query and the Displacement-Aware Features $F^{D}$ as the key and value, the Scene-Aware Router performs

where $\text{SA}{( \cdot )}$ and $\text{CA}{( \cdot )}$ represent self-attention and cross-attention operations, respectively.

Therefore, $Q_{Routed}$ captures the AV's driving intention as well as its relationship with the surrounding scene. Subsequently, $Q_{Routed}$ is passed through an MLP layer followed by a softmax function to predict the scores for the $N$ Routed Experts. For each query, we select the top-$K$ Specific Experts based on these scores:

where $E$ represents the indices of the experts selected by the Top-$K$ operation, and $R_{i}$ denotes the score of the $i$-th expert selected for each query.

### III-D2 Scene-Specific Experts

Scene-Specific Experts transform the Trajectory Query $Q_{traj}$ while integrating relevant information for AV planning. Before this transformation, an operation similar to Equation 2 is performed using $Q_{traj}$ as the query and the Displacement-Aware Features $F^{D}$ as the key and value, producing the features $Q_{Expert}^{\prime}$. Next, the top-$K$ Routed Experts and Shared Experts, each composed of Feed-Forward Networks (FFNs), independently process each element of $Q_{Expert}^{\prime}$. Note that the top-$K$ Routed Experts are selected by the Scene-Aware Router.

Finally, the features produced by the Routed Experts and Shared Experts are combined to generate the scene-aware feature $F_{sa}$, formulated as

where $S_{i}{( \cdot )}$ and $E_{i}{( \cdot )}$ denote the outputs of the $i$-th Shared Expert and the $i$-th Routed Expert, respectively. Notice that the outputs of the top-$K$ Routed Experts are weighted by the scores produced by the Scene-Aware Router.

After passing through a total of $L_{dec}$ layers, the extracted final scene-aware features $F_{sa}$ are used to generate the AV's future trajectory $\hat{Y}$ and confidence score $\hat{C}$ through a regression head and a classification head.

### III-E Learning Process

The total loss $L_{total}$ used to train CarPLAN is given by

where $L_{plan}$, $L_{disp}$, and $L_{bal}$ represent the Planning Loss, Displacement-Aware Predictive Loss, and Expert Balancing Loss, respectively. The Planning Loss $L_{plan}$ is computed using the smooth L1 loss and cross-entropy loss, $L_{plan} = {{L1_{smooth}{(Y,\hat{Y})}} + {\text{CrossEntropy}{(C,\hat{C})}}}$, where $Y$ and $C$ are the AV's ground truth trajectory and score. The Displacement-Aware Predictive Loss $L_{disp}$ is calculated using the smooth L1 loss from

where $x_{a}^{t}$ denotes the positions of agent $a$ at $t$ timestep and $D_{1:{N_{a} + N_{p}}}^{1:T_{f}}$ is the ground truth displacement of surrounding scene elements over $T_{f}$ horizon. Lastly, we employ the Expert Balance Loss $L_{bal}$ to guarantee a balanced selection of experts.

TABLE I: Closed-loop simulation results , -Hard, and -Random. The “–” symbol means the metric is unknown.

## Experiments

TABLE II: Performance on the nuPlan benchmark with post-processing.

### IV-A Experimental Settings

### IV-A1 Benchmark and Metrics

We conducted extensive evaluations on the nuPlan dataset, which contains 1,300 hours of real-world urban driving data spanning 75 scenario types. The, -Hard, and -Random benchmarks are used to assess performance across both general and challenging driving scenarios, with evaluation metrics based on the Open-Loop Score (OLS) and Closed-Loop Score (CLS). OLS is computed using distance errors between the planned trajectories and the logged trajectories. In contrast, CLS assesses the outcomes of driving simulations generated from the model's predictions, considering factors such as safety, efficiency, and ride comfort. CLS is further divided into CLS-NR (Non-Reactive) and CLS-R (Reactive), depending on how surrounding agents are simulated. In CLS-NR, agents strictly follow the logged trajectories from the dataset, reflecting real-world driving conditions. In CLS-R, agents adapt their behavior based on the Intelligent Driver Model (IDM), allowing them to react dynamically to the ego vehicle.

In addition to the nuPlan benchmark, we further evaluated the proposed model on the Waymax benchmark to assess its generalization capability across benchmarks. Waymax is a large-scale reactive closed-loop simulation framework built on the Waymo Open Motion Dataset (WOMD), providing real-world driving environments with diverse traffic interactions. Similar to the CLS-R setting in nuPlan, the ego vehicle is controlled by the planner, while surrounding agents react dynamically within the simulation. Closed-loop performance in Waymax is evaluated using Arrival Rate (AR), Off-road Rate (OR), Collision Rate (CR), and Progress Rate (PR). AR measures whether the ego vehicle successfully completes the driving task without safety violations. OR and CR capture off-road and collision events, respectively, while PR reflects progress along the expert driving route.

### IV-A2 Implementation Details

We utilized agent states from the past $T_{h} = 2$ seconds, sampled at 10Hz. To mitigate the shortcut learning issue identified , only the current state of the AV was used. Both the Scene Encoder and CMD consist of four stacked layers. In CMD, the first layer employs a single feed-forward network (FFN) without a Mixture of Experts (MoE), while the remaining layers incorporate two shared expert decoders and 16 routed expert decoders. When integrating with post-processing, we followed the method suggested . The detailed configurations for our model are provided in the Supplementary Material.

TABLE III: Ablation study of CarPLAN.
SSE: Scene-Specific Experts, SAR: Scene-Aware Router.

### IV-B Performance Comparison

Table I presents the performance of CarPLAN on the nuPlan dataset, evaluated using OLS, CLS-NR, and CLS-R metrics. CarPLAN establishes new state-of-the-art performance across all CLS benchmarks, outperforming the latest planners by significant margins. While achieving superior CLS performance, CarPLAN maintains competitive OLS scores without significant compromise, which shows that CarPLAN exhibits human-like driving behavior. On the benchmark, CarPLAN achieves a CLS-NR score of 91.4 and a CLS-R score of 84.6, surpassing the previous best models, Diffusion-Planner and BeTopNet, by 1.5 and 0.9 points, respectively. On the -Hard benchmark, CarPLAN also outperforms its competitors, demonstrating its ability to handle complex and challenging driving scenarios.

Table II presents the performance in hybrid scenarios, where learning-based planners are combined with rule-based post-processing. CarPLAN achieves state-of-the-art performance across most benchmarks, except for CLS-NR on the -Random benchmark, where it ranks second, trailing the best-performing model by a margin of 0.2 points.

### IV-C Ablation Study

We conducted an ablation study to assess the contributions of CarPLAN's core components. Evaluation was conducted on the -Hard benchmark using the CLS-NR metric. Additionally, we employed Colli (collision avoidance) and DAC (drivable area compliance) as supplementary evaluation metrics.

### IV-C1 Contributions of Main Components

Table III presents the contribution of each component to overall performance. The first row represents the baseline model, which consists of only the scene encoder and a Transformer decoder to generate future trajectories for the AV. Integrating DPE into the baseline model increases the CLS-NR score by $1.5$ points, demonstrating the effectiveness of incorporating scene awareness. Next, we add Scene-Specific Experts without DPE, using a simple multi-layer perceptron (MLP)-based router that does not employ its own self- or cross-attention. This modification improves performance by $1.0$ points over the baseline. When we enable both Scene-Specific Experts and Scene-Aware Router only without DPE, the CLS-NR score gap becomes $1.9$ points compared to the baseline. Finally, incorporating both DPE and CMD together results in a total improvement of $3.1$ points over the baseline. In particular, the Colli and DAC metrics improve by $3.6$ and $2.2$ points over the baseline, indicating that the proposed ideas significantly enhance safety in planning.

TABLE IV: Ablation study for DPE target.

### IV-C2 Ablation Study for DPE Target

We explored different configurations of DPE by predicting future displacement vectors : No Target, agents only, map components only, and both. Table IV presents the performance for each case. Incorporating displacement predictions for surrounding agents alone improves the CLS-NR score by $0.7$ points over the No Target setting, while including HD map elements alone results in an improvement by $0.5$ points. When displacement vectors for both agents and map components are predicted, as in our CarPLAN, we observe a $1.2$ point improvement in CLS-NR, along with $1.5$ and $0.4$ point gains in Colli and DAC, respectively. These results confirm the enhanced awareness of both dynamic agents and traffic structures in our CarPLAN.

TABLE V: Ablation study for CMD.

### IV-C3 Effect of Expert Routing and Shared Experts

Table V analyzes the impact of the number of routed experts, Top-$K$ selection, and the inclusion of two additional shared experts on performance. The results show that the best performance is achieved when Top-2 experts are selected from 16 routed experts, with two shared experts enabled. Increasing or decreasing the number of experts to 32 or 8 does not lead to any performance improvement. Notably, the presence of two shared experts provides a significant performance boost. The shared experts are responsible for capturing general and context-invariant driving patterns, while the routed experts focus on scenario-specific behaviors. This complementary design allows the model to maintain globally consistent driving representations while adapting to diverse contexts, leading to improved robustness in planning.

TABLE VI: Inference Efficiency Analysis

Figure 3: Visualization of expert selection scores across layers. The dark red vehicle represents the AV, while the yellow and red lines indicate the ground truth (GT) and the predicted future trajectory with the highest score, respectively. The softmax scores are displayed for layers 2, 3, and 4. (a) In two distinct straight-driving scenarios, differences in the distribution of surrounding agents lead to distinct expert selections. (b) In similar driving scenarios, expert selection remains mostly consistent.

### IV-C4 Inference Efficiency Analysis

Table VI presents the efficiency analysis of CarPLAN under different module configurations. In our design, the Displacement-Aware Predictive Encoder (DPE) is used only during training, allowing it to be excluded during inference. As a result, the inference-time computational cost mainly stems from the MoE-based decoder architecture. While the proposed method introduces a modest increase in latency and FLOPs, it still achieves real-time inference at approximately 15 FPS. More importantly, this overhead is accompanied by substantial performance gains, indicating a favorable efficiency--performance trade-off. It is also worth noting that the current implementation does not apply any system-level optimization of the MoE structure. Inference efficiency can be further improved through standard techniques such as expert pruning or parallel execution (e.g., CUDA streams).

TABLE VII: Ablation study on the Waymax benchmark.

### IV-C5 Ablation Study on the Waymax Benchmark

On the Waymax benchmark, Table VII presents experimental results evaluating the effect of the proposed modules by integrating them into a baseline planner. In this setting, the proposed DPE and CMD are incrementally incorporated into the encoder and decoder of the baseline model. The results show that integrating either DPE or CMD individually yields consistent performance improvements, while their combined use achieves the highest performance across all evaluation metrics. These findings indicate that displacement-aware relational encoding and context-adaptive decoding effectively contribute to performance improvements, and further demonstrate that the core design of CarPLAN generalizes well across different benchmarks.

Figure 4: Qualitative results on closed-loop simulations in nuPlan benchmark. The yellow trajectory represents the recorded actual trajectory of the vehicle, while the red trajectory indicates the model’s predicted trajectory with the highest probability at each timestep. The dark red vehicle represents the AV, and black vehicles or pedestrians that turn red signify a collision occurrence. Red dashed boxes highlight critical events observed during the simulation.

Figure 5: Qualitative results on closed-loop simulations in Waymax benchmark. The blue dots represent the trajectory executed during the closed-loop simulation. The blue bounding box denotes the AV, while gray bounding boxes indicate surrounding vehicles and boxes that turn red indicate a collision event during simulation. Green circles correspond to traffic lights in the green phase. Dark gray dots illustrate the road layout, and light gray dots represent centerlines. Red dashed boxes highlight critical events observed during the simulation.

### IV-D Qualitative Analysis

### IV-D1 Visualization of Activated Expert's Score in CMD

To illustrate the expert selection behavior in CMD, Figure 3 visualizes the expert scores obtained at each layer across different driving scenes. First, we observe that expert selection varies across CMD layers, indicating that the model dynamically adapts expert selection at different layers. In Figure 3 (a), we examine two cases of straight-driving scenarios with different distributions of surrounding vehicles. The proposed Scene-Aware Router recognizes these as distinct situations and optimizes expert selection accordingly, producing different expert combinations. Conversely, in Figure 3 (b), the two cases exhibit similar road topology and distributions of surrounding agents. In this scenario, the Scene-Aware Router selects a similar expert combination.

### IV-D2 Qualitative Results on closed-loop simulation

Figure 4 presents a qualitative evaluation of the proposed CarPLAN, comparing its planning results with those of PLUTO in closed-loop simulations using nuPlan. In Figure 4 (a), PLUTO generates a conservative trajectory in a complex scene with dense traffic and pedestrians, whereas CarPLAN produces a more flexible trajectory appropriate for the current situation, enabling more context-adaptive decisions. Figure 4 (b) demonstrates CarPLAN's ability to recognize a pedestrian crossing the road and appropriately reduce speed, highlighting its effectiveness in enhancing safety in dynamic environments. Figure 5 presents qualitative results from closed-loop simulations in Waymax, comparing CarPLAN with PLUTO. In Figure 5 (a), PLUTO fails to maintain a safe distance from a nearby vehicle and results in a collision, whereas CarPLAN preserves an appropriate safety margin and avoids the collision. Figure 5 (b) shows that PLUTO struggles to maintain sufficient clearance from the road boundary and deviates from the drivable area, while CarPLAN remains within the drivable region.

## Conclusion

In this paper, we introduced CarPLAN, an IL-based planning method designed to more accurately capture human driving behavior. CarPLAN first integrates DPE, which models human-like behavior by maintaining relative spacing with surrounding agents and map components. DPE is trained to predict the future displacement vectors between the AV and scene elements, enabling the model to account for relative spacing in the planning process. To handle complex and dynamic driving scenes, CarPLAN employs CMD, which facilitates context-adaptive decoding. CMD utilizes multiple expert decoders that are dynamically selected based on scene structure, allowing the model to effectively adapt to diverse driving conditions. Our experiments on the nuPlan benchmark demonstrate that by integrating these components, CarPLAN consistently outperforms state-of-the-art learning-based planning methods in a variety of closed-loop simulations. Moreover, results on the Waymax benchmark indicate that CarPLAN generalizes well across different benchmarks.

Our study assumes the availability of perfect perception, relying on accurate object states and HD map information provided by external perception modules. As a future direction, we aim to extend our framework to an end-to-end autonomous driving system, where CarPLAN is jointly trained with the perception module. In addition, we plan to extend CarPLAN toward an action-conditioned world model that predicts how future spatial relationships evolve conditioned on the ego vehicle's actions, rather than assuming a single deterministic displacement.
