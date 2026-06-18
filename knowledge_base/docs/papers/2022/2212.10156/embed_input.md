<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Planning-Oriented Autonomous Driving

Topics include Autonomous driving, End-to-end planning, Multi-task learning, Perception and planning, NuScenes, Unified architectures.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces UniAD, a full-stack autonomous-driving network organized around planning rather than separate perception and prediction tasks. The paper is important as an end-to-end driving baseline because it explicitly coordinates modular driving subtasks through unified queries and evaluates their contribution to planning quality.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Modern autonomous driving system is characterized as modular tasks in sequential order, i.e., perception, prediction, and planning. In order to perform a wide diversity of tasks and achieve advanced-level intelligence, contemporary approaches either deploy standalone models for individual tasks, or design a multi-task paradigm with separate heads. However, they might suffer from accumulative errors or deficient task coordination. Instead, we argue that a favorable framework should be devised and optimized in pursuit of the ultimate goal, i.e., planning of the self-driving car. Oriented at this, we revisit the key components within perception and prediction, and prioritize the tasks such that all these tasks contribute to planning. We introduce Unified Autonomous Driving (UniAD), a comprehensive framework up-to-date that incorporates full-stack driving tasks in one network. It is exquisitely devised to leverage advantages of each module, and provide complementary feature abstractions for agent interaction from a global perspective. Tasks are communicated with unified query interfaces to facilitate each other toward planning. We instantiate UniAD on the challenging nuScenes benchmark.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

With extensive ablations, the effectiveness of using such a philosophy is proven by substantially outperforming previous state-of-the-arts in all aspects. Code and models are public.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

With the successful development of deep learning, autonomous driving algorithms are assembled with a series of tasks^11^1In the following context, we interchangeably use task, module, component, unit and node to indicate a certain task (*e.g*., detection)., including detection, tracking, mapping in perception; and motion and occupancy forecast in prediction. As depicted in Fig. 1(a), most industry solutions deploy standalone models for each task independently, as long as the resource bandwidth of the onboard chip allows. Although such a design simplifies the R&D difficulty across teams, it bares the risk of information loss across modules, error accumulation and feature misalignment due to the isolation of optimization targets.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A more elegant design is to incorporate a wide span of tasks into a multi-task learning (MTL) paradigm, by plugging several task-specific heads into a shared feature extractor as shown in Fig. 1(b). This is a popular practice in many domains, including general vision, autonomous driving^22^2In this paper, we refer to MTL in autonomous driving as tasks beyond perception. There is plenty of work on MTL within perception, *e.g*., detection, depth, flow, *etc*. This kind of literature is out of scope., such as Transfuser, BEVerse, and industrialized products, *e.g*., Mobileye, Tesla, Nvidia, *etc*. In MTL, the co-training strategy across tasks could leverage feature abstraction; it could effortlessly extend to additional tasks, and save computation cost for onboard chips. However, such a scheme may cause undesirable "negative transfer".

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

By contrast, the emergence of end-to-end autonomous driving unites all nodes from perception, prediction and planning as a whole. The choice and priority of preceding tasks should be determined in favor of planning. The system should be planning-oriented, exquisitely designed with certain components involved, such that there are few accumulative error as in the standalone option or negative transfer as in the MTL scheme. Table 1 describes the task taxonomy of different framework designs.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Following the end-to-end paradigm, one "tabula-rasa" practice is to directly predict the planned trajectory, without any explicit supervision of perception and prediction as shown in Fig. 1(c.1). Pioneering works verified this vanilla design in the closed-loop simulation. While such a direction deserves further exploration, it is inadequate in safety guarantee and interpretability, especially for highly dynamic urban scenarios. In this paper, we lean toward another perspective and ask the following question: *Toward a reliable and planning-oriented autonomous driving system, how to design the pipeline in favor of planning? which preceding tasks are requisite?*

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

An intuitive resolution would be to perceive surrounding objects, predict future behaviors and plan a safe maneuver explicitly, as illustrated in Fig. 1(c.2). Contemporary approaches provide good insights and achieve impressive performance. However, we argue that the devil lies in the details; previous works more or less fail to consider certain components (see block (c.2) in Table 1), being reminiscent of the planning-oriented spirit. We elaborate on the detailed definition and terminology, the necessity of these modules in the Supplementary.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To this end, we introduce UniAD, a Unified Autonomous Driving algorithm framework to leverage five essential tasks toward a safe and robust system as depicted in Fig. 1(c.3) and Table 1(c.3). UniAD is designed in a planning-oriented spirit. We argue that this is not a simple stack of tasks with mere engineering effort. A key component is the query-based design to connect all nodes. Compared to the classic bounding box representation, queries benefit from a larger receptive field to soften the compounding error from upstream predictions. Moreover, queries are flexible to model and encode a variety of interactions, *e.g*., relations among multiple agents. To the best of our knowledge, UniAD is the first work to comprehensively investigate the joint cooperation of such a variety of tasks including perception, prediction and planning in the field of autonomous driving.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The contributions are summarized as follows. (a) we embrace a new outlook of autonomous driving framework following a planning-oriented philosophy, and demonstrate the necessity of effective task coordination, rather than standalone design or simple multi-task learning. (b) we present UniAD, a comprehensive end-to-end system that leverages a wide span of tasks. The key component to hit the ground running is the query design as interfaces connecting all nodes. As such, UniAD enjoys flexible intermediate representations and exchanging multi-task knowledge toward planning. (c) we instantiate UniAD on the challenging benchmark for realistic scenarios. Through extensive ablations, we verify the superiority of our method over previous state-of-the-arts in all aspects.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

*We hope this work could shed some light on the target-driven design for the autonomous driving system, providing a starting point for coordinating various driving tasks.*

<!-- chunk {"id": "body-0013", "role": "body", "section": "Overview", "weight": 1.0} -->

As illustrated in Fig. 2, UniAD comprises four transformer decoder-based perception and prediction modules and one planner in the end. Queries $Q$ play the role of connecting the pipeline to model different interactions of entities in the driving scenario. Specifically, a sequence of multi-camera images is fed into the feature extractor, and the resulting perspective-view features are transformed into a unified bird's-eye-view (BEV) feature $B$ by an off-the-shelf BEV encoder in BEVFormer. Note that UniAD is not confined to a specific BEV encoder, and one can utilize other alternatives to extract richer BEV representations with long-term temporal fusion or multi-modality fusion. In TrackFormer, the learnable embeddings that we refer to as track queries inquire about the agents' information from $B$ to detect and track agents. MapFormer takes map queries as semantic abstractions of road elements (*e.g*., lanes and dividers) and performs panoptic segmentation of the map.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Overview", "weight": 1.0} -->

With the above queries representing agents and maps, MotionFormer captures interactions among agents and maps and forecasts per-agent future trajectories. Since the action of each agent can significantly impact others in the scene, this module makes joint predictions for all agents considered. Meanwhile, we devise an ego-vehicle query to explicitly model the ego-vehicle and enable it to interact with other agents in such a scene-centric paradigm. OccFormer employs the BEV feature $B$ as queries, equipped with agent-wise knowledge as keys and values, and predicts multi-step future occupancy with agent identity preserved. Finally, Planner utilizes the expressive ego-vehicle query from MotionFormer to predict the planning result, and keep itself away from occupied regions predicted by OccFormer to avoid collisions.

<!-- chunk {"id": "body-0015", "role": "body", "section": "TrackFormer", "weight": 1.0} -->

It jointly performs detection and multi-object tracking (MOT) without non-differentiable post-processing. Inspired, we take a similar query design. Besides the conventional detection queries utilized in object detection, additional track queries are introduced to track agents across frames. Specifically, at each time step, initialized detection queries are responsible for detecting newborn agents that are perceived for the first time, while track queries keep modeling those agents detected in previous frames. Both detection queries and track queries capture the agent abstractions by attending to BEV feature $B$. As the scene continuously evolves, track queries at the current frame interact with previously recorded ones in a self-attention module to aggregate temporal information, until the corresponding agents disappear completely (untracked in a certain time period). Similar to, TrackFormer contains $N$ layers and the final output state $Q_{A}$ provides knowledge of $N_{a}$ valid agents for downstream prediction tasks. Besides queries encoding other agents surrounding the ego-vehicle, we introduce one particular *ego-vehicle query* in the query set to explicitly model the self-driving vehicle itself, which is further used in planning.

<!-- chunk {"id": "body-0016", "role": "body", "section": "MapFormer", "weight": 1.0} -->

We design it based on a 2D panoptic segmentation method Panoptic SegFormer. We sparsely represent road elements as map queries to help downstream motion forecasting, with location and structure knowledge encoded. For driving scenarios, we set lanes, dividers and crossings as things, and the drivable area as stuff. MapFormer also has $N$ stacked layers whose output results of each layer are all supervised, while only the updated queries $Q_{M}$ in the last layer are forwarded to MotionFormer for agent-map interaction.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Prediction: Motion Forecasting", "weight": 1.0} -->

Recent studies have proven the effectiveness of transformer structure on the motion task, inspired by which we propose MotionFormer in the end-to-end setting. With highly abstract queries for dynamic agents $Q_{A}$ and static map $Q_{M}$ from TrackFormer and MapFormer respectively, MotionFormer predicts all agents' multimodal future movements, *i.e*., top-k possible trajectories, in a scene-centric manner. This paradigm produces multi-agent trajectories in the frame with a single forward pass, which greatly saves the computational cost of aligning the whole scene to each agent's coordinate. Meanwhile, we pass the *ego-vehicle query* from TrackFormer through MotionFormer to engage ego-vehicle to interact with other agents, considering the future dynamics. Formally, the output motion is formulated as $\left.

<!-- chunk {"id": "body-0018", "role": "body", "section": "MotionFormer", "weight": 1.0} -->

It is composed of $N$ layers, and each layer captures three types of interactions: agent-agent, agent-map and agent-goal point.

<!-- chunk {"id": "body-0019", "role": "body", "section": "MotionFormer", "weight": 1.0} -->

where MHCA, MHSA denote multi-head cross-attention and multi-head self-attention respectively. As it is also important to focus on the intended position, *i.e*.,

<!-- chunk {"id": "body-0020", "role": "body", "section": "MotionFormer", "weight": 1.0} -->

where ${\hat{\mathbf{x}}}_{T}^{l - 1}$ is the endpoint of the predicted trajectory of previous layer. $\text{DeformAttn}{(q,r,x)}$, a deformable attention module, takes in the query $q$, reference point $r$ and spatial feature $x$. It performs sparse attention on the spatial feature around the reference point. Through this, the predicted trajectory is further refined as aware of the endpoint surroundings. All three interactions are modeled in parallel, where the generated $Q_{a}$, $Q_{m}$ and $Q_{g}$ are concatenated and passed to a multi-layer perceptron (MLP), resulting query context $Q_{\text{ctx}}$. Then, $Q_{\text{ctx}}$ is sent to the successive layer for refinement or decoded as prediction results at the last layer.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Motion queries", "weight": 1.0} -->

The input queries for each layer of MotionFormer, termed motion queries, comprise two components: the query context $Q_{\text{ctx}}$ produced by the preceding layer as described before, and the query position $Q_{\text{pos}}$. Specifically, $Q_{\text{pos}}$ integrates the positional knowledge in four-folds as in Eq. 3: the position of scene-level anchors $I^{s}$; the position of agent-level anchors $I^{a}$; current location of the agent $i$ and the predicted goal point.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Motion queries", "weight": 1.0} -->

Here the sinusoidal position encoding $\text{PE}{( \cdot )}$ followed by an MLP is utilized to encode the positional points and ${\hat{\mathbf{x}}}_{T}^{0}$ is set as $I^{s}$ at the first layer (subscripts $i,k$ are also omitted). The scene-level anchor represents prior movement statistics in a global view, while the agent-level anchor captures the possible intention in the local coordinate. They are both clustered by k-means algorithm on the endpoints of ground-truth trajectories, to narrow down the uncertainty of prediction. Contrary to the prior knowledge, the start point provides customized positional embedding for each agent, and the predicted endpoint serves as a dynamic anchor optimized layer-by-layer in a coarse-to-fine fashion.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Non-linear Optimization", "weight": 1.0} -->

Different from conventional motion forecasting works which have direct access to ground truth perceptual results, *i.e*., agents' location and corresponding tracks, we consider the prediction uncertainty from the prior module in our end-to-end paradigm. Brutally regressing the ground-truth waypoints from an imperfect detection position or heading angle may lead to unrealistic trajectory predictions with large curvature and acceleration. To tackle this, we adopt a non-linear smoother to adjust the target trajectories and make them physically feasible given an imprecise starting point predicted by the upstream module.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Non-linear Optimization", "weight": 1.0} -->

where $\lambda_{\text{xy}}$ and $\lambda_{\text{goal}}$ are hyperparameters, the kinematic function set $\Phi$ has five terms including jerk, curvature, curvature rate, acceleration and lateral acceleration. The cost function regularizes the target trajectory to obey kinematic constraints. This target trajectory optimization is only conducted in training and does not affect inference.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Prediction: Occupancy Prediction", "weight": 1.0} -->

Occupancy grid map is a discretized BEV representation where each cell holds a belief indicating whether it is occupied, and the occupancy prediction task is to discover how the grid map changes in the future. Previous approaches utilize RNN structure for temporally expanding future predictions from observed BEV features. However, they rely on highly hand-crafted clustering post-processing to generate per-agent occupancy maps, as they are mostly agent-agnostic by compressing BEV features as a whole into RNN hidden states. Due to the deficient usage of agent-wise knowledge, it is challenging for them to predict the behaviors of all agents globally, which is essential to understand how the scene evolves. To address this, we present OccFormer to incorporate both scene-level and agent-level semantics in two aspects: a dense scene feature acquires agent-level features via an exquisitely designed attention module when unrolling to future horizons; we produce instance-wise occupancy easily by a matrix multiplication between agent-level features and dense scene features without heavy post-processing.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Prediction: Occupancy Prediction", "weight": 1.0} -->

OccFormer is composed of $T_{o}$ sequential blocks where $T_{o}$ indicates the prediction horizon. Note that $T_{o}$ is typically smaller than $T$ in the motion task, due to the high computation cost of densely represented occupancy. Each block takes as input the rich agent features $G^{t}$ and the state (dense feature) $F^{t - 1}$ from the previous layer, and generates $F^{t}$ for timestep $t$ considering both instance- and scene-level information. To get agent feature $G^{t}$ with dynamics and spatial priors, we max-pool motion queries from MotionFormer in the modality dimension denoted as $Q_{X} \in {\mathbb{R}}^{N_{a} \times D}$, with $D$ as the feature dimension.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Prediction: Occupancy Prediction", "weight": 1.0} -->

where $\lbrack \cdot \rbrack$ indicates concatenation. For the scene-level knowledge, the BEV feature $B$ is downscaled to $1/4$ resolution for training efficiency to serve as the first block input $F^{0}$. To further conserve training memory, each block follows a downsample-upsample manner with an attention module in between to conduct pixel-agent interaction at $1/8$ downscaled feature, denoted as $F_{\text{ds}}^{t}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Pixel-agent interaction", "weight": 1.0} -->

is designed to unify the scene- and agent-level understanding when predicting future occupancy. We take the dense feature $F_{\text{ds}}^{t}$ as queries, instance-level features as keys and values to update the dense feature over time. Detailedly, $F_{\text{ds}}^{t}$ is passed through a self-attention layer to model responses between distant grids, then a cross-attention layer models interactions between agent features $G^{t}$ and per-grid features. Moreover, to align the pixel-agent correspondence, we constrain the cross-attention by an attention mask, which restricts each pixel to only look at the agent occupying it at timestep $t$, inspired.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Pixel-agent interaction", "weight": 1.0} -->

The attention mask $O_{m}^{t}$ is semantically similar to occupancy, and is generated by multiplying an additional agent-level feature and the dense feature $F_{\text{ds}}^{t}$, where we name the agent-level feature here as mask feature $M^{t} = {\text{MLP}{(G^{t})}}$. After the interaction process in Eq. 7, $D_{\text{ds}}^{t}$ is upsampled to $1/4$ size of $B$. We further add $D_{\text{ds}}^{t}$ with block input $F^{t - 1}$ as a residual connection, and the resulting feature $F^{t}$ is passed to the next block.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Instance-level occupancy", "weight": 1.0} -->

It represents the occupancy with each agent's identity preserved. It could be simply drawn via matrix multiplication, as in recent query-based segmentation works. Formally, in order to get an occupancy prediction of original size $H \times W$ of BEV feature $B$, the scene-level features $F^{t}$ are upsampled to $F_{\text{dec}}^{t} \in {\mathbb{R}}^{C \times H \times W}$ by a convolutional decoder, where $C$ is the channel dimension. For the agent-level feature, we further update the coarse mask feature $M^{t}$ to the occupancy feature $U^{t} \in {\mathbb{R}}^{N_{a} \times C}$ by another MLP. We empirically find that generating $U^{t}$ from mask feature $M^{t}$ instead of original agent feature $G^{t}$ leads to superior performance.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Planning", "weight": 1.0} -->

Planning without high-definition (HD) maps or predefined routes usually requires a high-level command to indicate the direction to go. Following this, we convert the raw navigation signals (*i.e*., turn left, turn right and keep forward) into three learnable embeddings, named command embeddings. As the ego-vehicle query from MotionFormer already expresses its multimodal intentions, we equip it with command embeddings to form a "plan query". We attend plan query to BEV features $B$ to make it aware of surroundings, and then decode it to future waypoints $\hat{\tau}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Planning", "weight": 1.0} -->

where $\hat{\tau}$ is the original planning prediction, $\tau^{\ast}$ denotes the optimized planning, which is selected from multiple-shooting trajectories $\tau$ as to minimize cost function $f{( \cdot )}$. $\hat{O}$ is a classical binary occupancy map merged from the instance-wise occupancy prediction from OccFormer.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Planning", "weight": 1.0} -->

Here $\lambda_{\text{coord}}$, $\lambda_{\text{obs}}$, and $\sigma$ are hyperparameters, and $t$ indexes a timestep of future horizons. The $l_{2}$ cost pulls the trajectory toward the original predicted one, while the collision term $\mathcal{D}$ pushes it away from occupied grids, considering surrounding positions confined to $\mathcal{S} = \left. \{{(x,y)} \middle| {{{\parallel{{(x,y)} - \tau_{t}}\parallel}_{2} < d},{{\hat{O}}_{x,y}^{t} = 1}}\} \right.$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Learning", "weight": 1.0} -->

UniAD is trained in two stages. We first jointly train perception parts, *i.e*., the tracking and mapping modules, for a few epochs (6 in our experiments), and then train the model end-to-end for 20 epochs with all perception, prediction and planning modules. The two-stage training is found more stable empirically. We refer the audience to the Supplementary for details of each loss.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Shared matching", "weight": 1.0} -->

Since UniAD involves instance-wise modeling, pairing predictions to the ground truth set is required in perception and prediction tasks. Similar to DETR, the bipartite matching algorithm is adopted in the tracking and online mapping stage. As for tracking, candidates from detection queries are paired with newborn ground truth objects, and predictions from track queries inherit the assignment from previous frames. The matching results in the tracking module are reused in motion and occupancy nodes to consistently model agents from historical tracks to future motions in the end-to-end framework.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

We conduct experiments on the challenging nuScenes dataset. In this section, we validate the effectiveness of our design in three aspects: joint results revealing the advantage of task coordination and its effect on planning, modular results of each task compared with previous methods, and ablations on the design space for specific modules. Due to space limit, the full suite of protocols, some ablations and visualizations are provided in the Supplementary.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Joint Results", "weight": 1.0} -->

We conduct extensive ablations as shown in Table 2 to prove the effectiveness and necessity of preceding tasks in the end-to-end pipeline. Each row of this table shows the model performance when incorporating task modules listed in the second Modules column. The first row (ID-0) serves as a vanilla multi-task baseline with separate task heads for comparison. The best result of each metric is marked in bold, and the runner-up result is underlined in each column.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Roadmap toward safe planning", "weight": 1.0} -->

As prediction is closer to planning compared to perception, we first investigate the two types of prediction tasks in our framework, *i.e*., motion forecasting and occupancy prediction. In Exp.10-12, only when the two tasks are introduced simultaneously (Exp.12), both metrics of the planning L2 and collision rate achieve the best results, compared to naive end-to-end planning without any intermediate tasks (Exp.10, Fig. 1(c.1)). Thus we conclude that both these two prediction tasks are required for a safe planning objective. Taking a step back, in Exp.7-9, we show the cooperative effect of two types of prediction. The performance of both tasks get improved when they are closely integrated (Exp.9, -3.5% minADE, -5.8% minFDE, -1.3 MR(%), +2.4 IoU-f.(%), +2.4 VPQ-f.(%)), which demonstrates the necessity to include both agent and scene representations.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Roadmap toward safe planning", "weight": 1.0} -->

Meanwhile, in order to realize a superior motion forecasting performance, we explore how perception modules could contribute in Exp.4-6. Notably, incorporating both tracking and mapping nodes brings remarkable improvement to forecasting results (-9.7% minADE, -12.9% minFDE, -2.3 MR(%)). We also present Exp.1-3, which indicate training perception sub-tasks together leads to comparable results to a single task. Additionally, compared with naive multi-task learning (Exp.0, Fig. 1(b)), Exp.12 outperforms it by a significant margin in all essential metrics (-15.2% minADE, -17.0% minFDE, -3.2 MR(%)), +4.9 IoU-f.(%)., +5.9 VPQ-f.(%), -0.15$m$ avg.L2, -0.51 avg.Col.(%)), showing the superiority of our planning-oriented design.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Modular Results", "weight": 1.0} -->

Following the sequential order of perception-prediction-planning, we report the performance of each task module in comparison to prior state-of-the-arts on the nuScenes validation set. Note that UniAD jointly performs all these tasks with a single trained network. The main metric for each task is marked with gray background in tables.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Perception results", "weight": 1.0} -->

As for multi-object tracking in Table 3, UniAD yields a significant improvement of +6.5 and +14.2 AMOTA(%) compared to MUTR3D and ViP3D respectively. Moreover, UniAD achieves the lowest ID switch score, showing its temporal consistency for each tracklet. For online mapping in Table 4, UniAD performs well on segmenting lanes (+7.4 IoU(%) compared to BEVFormer), which is crucial for downstream agent-road interaction in the motion module. As our tracking module follows an end-to-end paradigm, it is still inferior to tracking-by-detection methods with complex associations such as Immortal Tracker, and our mapping results trail previous perception-oriented methods on specific classes. We argue that UniAD is to benefit final planning with perceived information rather than optimizing perception with full model capacity.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Prediction results", "weight": 1.0} -->

Motion forecasting results are shown in Table 5, where UniAD remarkably outperforms previous vision-based end-to-end methods. It reduces prediction errors by 38.3% and 65.4% on minADE compared to PnPNet-vision and ViP3D respectively. In terms of occupancy prediction reported in Table 6, UniAD gets notable advances in nearby areas, yielding +4.0 and +2.0 on IoU-near(%) compared to FIERY and BEVerse with heavy augmentations, respectively.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Planning results", "weight": 1.0} -->

Benefiting from rich spatial-temporal information in both the ego-vehicle query and occupancy, UniAD reduces planning L2 error and collision rate by 51.2% and 56.3% compared to ST-P3, in terms of the average value for the planning horizon. Moreover, it notably outperforms several LiDAR-based counterparts, which is often deemed challenging for perception tasks.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Fig. 3 visualizes the results of all tasks for one complex scene. The ego vehicle drives with notice to the potential movement of a front vehicle and lane. In the Supplementary, we show more visualizations of challenging scenarios and one promising case for the planning-oriented design, that inaccurate results occur in prior modules while the later tasks could still recover, *e.g*., the planned trajectory remains reasonable though objects have a large heading angle deviation or fail to be detected in tracking results. Besides, we analyze that failure cases of UniAD are mainly under some long-tail scenarios such as large trucks and trailers, shown in the Supplementary as well.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Effect of designs in MotionFormer", "weight": 1.0} -->

Table 8 shows that all of our proposed components described in Sec. 2.2 contribute to final performance regarding minADE, minFDE, Miss Rate and minFDE-mAP metrics. Notably, the rotated scene-level anchor shows a significant performance boost (-15.8% minADE, -11.2% minFDE, +1.9 minFDE-mAP(%)), indicating that it is essential to do motion forecasting in the scene-centric manner. The agent-goal point interaction enhances the motion query with the planning-oriented visual feature, and surrounding agents can further benefit from considering the ego vehicle's intention. Moreover, the non-linear optimization strategy improves the performance (-5.0% minADE, -8.4% minFDE, -1.0 MR(%), +0.7 minFDE-mAP(%)) by taking perceptual uncertainty into account in the end-to-end scenario.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Effect of designs in OccFormer", "weight": 1.0} -->

As illustrated in Table 9, attending each pixel to all agents without locality constraints (Exp.2) results in slightly worse performance compared to an attention-free baseline (Exp.1). The occupancy-guided attention mask resolves the problem and brings in gain, especially for nearby areas (Exp.3, +1.0 IoU-n.(%), +1.4 VPQ-n.(%)). Additionally, reusing the mask feature $M^{t}$ instead of the agent feature to acquire the occupancy feature further enhances performance.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Effect of designs in Planner", "weight": 1.0} -->

We provide ablations on the proposed designs in planner in Table 10, *i.e*., attending BEV features, training with the collision loss and the optimization strategy with occupancy. Similar to previous research, a lower collision rate is preferred for safety over naive trajectory mimicking (L2 metric), and is reduced with all parts applied in UniAD.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

We discuss the system-level design for the autonomous driving algorithm framework. A planning-oriented pipeline is proposed toward the ultimate pursuit for planning, namely UniAD. We provide detailed analyses on the necessity of each module within perception and prediction. To unify tasks, a query-based design is proposed to connect all nodes in UniAD, benefiting from richer representations for agent interaction in the environment. Extensive experiments verify the proposed method in all aspects.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

Limitations and future work. Coordinating such a comprehensive system with multiple tasks is non-trivial and needs extensive computational power, especially trained with temporal history. How to devise and curate the system for a lightweight deployment deserves future exploration. Moreover, whether or not to incorporate more tasks such as depth estimation, behavior prediction, and how to embed them into the system, are worthy future directions as well.
