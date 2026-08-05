<!-- arxiv-full-text:v1 {"arxiv_id": "2309.03750", "source": "arxiv-html"} -->

## Introduction

To safely navigate through traffic while offering passengers a smooth ride, autonomous vehicles need the ability to predict the trajectories of surrounding agents. There is inherent uncertainty in predicting the future, making this a challenging task. Agent trajectories tend to be highly non-linear over long prediction horizons. Additionally, the distribution of future trajectories is multimodal; in a given scene an agent could have multiple plausible goals and could take various paths to each goal.

In spite of these challenges, agent motion is not completely unconstrained. Vehicles tend to follow the direction of motion ascribed to their lanes, make legal turns and lane changes, and stop at stop signs and crosswalks. Bicyclists tend to use the bike lane, and pedestrians tend to walk along sidewalks and crosswalks. High-definition (HD) maps of traffic scenes efficiently represent such constraints on agent motion and have thus been a critical component of autonomous driving datasets. In fact, it has been shown in many prior works that a key requirement of the trajectory prediction task for a real-world autonomous driving system is to predict map-compliant trajectories -- trajectories that don't go off-road or violate traffic rules over long prediction horizons. For example, incorrectly predicting a non-map-compliant trajectory that encroaches into the oncoming traffic lane could cause the ego vehicle to brake hard or even make dangerous maneuvers on the road. As a result, prediction map compliance w.r.t. the provided HD map is central to our proposed approach and experimental evaluation.

Prior works have leveraged HD maps for trajectory prediction in two distinct ways. First, the HD map is often used as an input to the model. Early works use rasterized HD maps and CNN encoders. More recent works directly encode vectorized HD maps using PointNet encoders, graph neural networks or transformer layers. The map encoding is then used by a multimodal prediction header to output $K$ trajectories and their probabilities. A drawback of multimodal prediction headers is that they need to learn a complex one-to-many mapping from the entire scene context to multiple future trajectories, often leading to non-map-compliant predictions.

Figure 1: Overview of path-based prediction. Path-based prediction predicts trajectories conditioned on reference paths rather than 2D goals. We sample reference paths using the lane network from HD maps, predict a discrete distribution over the sampled paths, and predict future trajectories in the Frenet frame relative to the paths. Finally, we transform the trajectories back to the Cartesian frame relative to the target agent to obtain multimodal predictions.

To address this shortcoming, a few recent works additionally use the HD map for goal-based prediction. Goal-based prediction models associate each mode of the trajectory distribution to a 2D goal location sampled from the HD map. They predict a discrete distribution over the sampled goals, and then predict trajectories conditioned on each goal. This simplifies the mapping learned by the prediction header, and also makes each mode of the trajectory distribution more interpretable. However, 2D goal locations serve as a weak inductive bias to condition predictions, and may lead to imprecise trajectories for each goal.

In this work, we seek to improve upon goal-based trajectory prediction. We argue that reference paths rather than 2D goals are the appropriate HD map element to condition predicted trajectories. We define reference paths as segments of lane centerlines close to the agent of interest that the agent may follow over the prediction horizon. We propose a novel path classifier that predicts a discrete probability distribution over the candidate reference paths and a trajectory completion module that predicts trajectories conditioned on each path in the Frenet frame. Figure 1 shows an overview of our approach. In particular, our approach has two key advantages over goal-based prediction: Path features instead of goal features: We predict trajectories conditioned on feature descriptors of the entire reference path instead of just 2D goal locations. This is a more informative feature descriptor and leads to more map-compliant trajectories over longer prediction horizons compared to goal-based prediction.

Prediction in the Frenet frame: The reference paths allow us to predict trajectories in the Frenet frame relative to the path. Compared to the Cartesian frame with varying lane locations and curvatures, predictions in the Frenet frame have much lower variance, which leads to more map-compliant trajectories that better generalize to novel scene layouts.

Our path-based trajectory decoder is modular by design and could be used with any existing scene encoder such as VectorNet, LaneGCN, Scene Transformer, Wayformer, etc. Here, we build our decoder on top of the recently proposed HiVT encoder that achieved competitive results on the Argoverse dataset and has a publicly available code base. Our results on the Argoverse dataset show that our path-based decoder achieves competitive performance in terms of the standard minADE, minFDE, and miss rate metrics, while significantly outperforming the HiVT baseline and goal-based prediction in terms of map compliance metrics.

Our contributions can be summarized as follows: We propose a novel path-based trajectory prediction (PBP) approach that improves upon traditional goal-based prediction.

We applied our PBP trajectory decoder on top of the HiVT scene encoder. The resulting model achieves the best map compliance metric on the Argoverse leaderboard while being competitive in terms of prediction error metrics.

We present extensive ablation studies comparing different trajectory decoder approaches on the Argoverse validation set.

Figure 2: Model architecture: Our model consists of four key modules. The scene encoder encodes the agent history and HD map information (Section III-C). The candidate path sampler samples candidate paths for each agent from the lane graph (Section III-D). The path classifier predicts a discrete distribution over the reference paths (Section III-E). Finally, the trajectory regressor decodes trajectory predictions in the path-relative Frenet frame conditioned on the paths (Section III-F).

## Related work

Map-compliant trajectory prediction: Leveraging the HD-map and predicting map-compliant trajectories has been the focus of a large number of works on trajectory prediction. Several works have proposed novel HD map encoders, trajectory decoders conditioned on HD maps, and even novel metrics and auxiliary loss functions for map-compliance. In this work, we propose a path-based prediction approach that significantly improves prediction map compliance.

Goal-free multimodal prediction: The distribution of future trajectories is multimodal due to unknown intents of agents. Machine learning models for trajectory prediction thus need to learn a one-to-many mapping from the HD map and past states of agents, to multiple future trajectories. Prior work has addressed this using two approaches. The first approach is to implicitly learn the trajectory distribution using latent variable models such as GANs, CVAEs, and normalizing flows, where samples from the model represent plausible future trajectories. The other common approach is to use a multimodal regression header that outputs a fixed number of trajectories along with their probabilities. Such models are trained using the winner takes all/variety loss. Some recent works, use DETR-like learned tokens to output $K$ distinct trajectories.

Goal-based prediction: Goal-based prediction models partly address the above limitations by associating each mode of the trajectory distribution to a 2D goal in the HD map. TNT samples a sparse set of goals along lane centerlines. LaneRCNN uses nodes in a lane graph to predict goal locations. HOME and GoHOME predict goal heatmaps along a grid and graph representation of the HD map, and sample goal locations to optimize for the minFDE or miss rate metrics. Finally, DenseTNT first predicts a dense goal heatmap along lanes, before using a second learned model to sample goals from the heatmap. We improve upon goal-based prediction models by conditioning our predictions on reference paths in the HD map rather than goals. Reference paths provide our trajectory decoder with more informative feature descriptors than 2D goal coordinates, and additionally allow us to predict in the path-relative Frenet frame.

Frenet frame trajectory decoding: There are some existing models that predict trajectories in path-relative Frenet frame, such as GoalNet, DAC, and WIMP. PBP has two key differences from those works. First, PBP has a different definition of its reference paths from those works. The reference paths in GoalNet, DAC, and WIMP are fixed-lengthed paths in the lane level. To generate the reference paths, GoalNet and DAC start from the agent's current position and search along the lane graph for a fixed distance. Such reference paths only capture the agent's high-level intention (e.g., go straight or turn right) but do not capture other uncertainties such as change of speed profiles. As a result, GoalNet, DAC, and WIMP all predict $M$ trajectory modes within each reference path to achieve multimodal prediction. On the other hand, PBP's reference paths are sequences of lane segments with variable lengths, and PBP relies entirely on its path classification to achieve multimodal prediction since a reference path can uniquely define a predictive mode. To highlight the difference, PBP considers around 600 candidate reference paths per agent, while GoalNet and DAC only consider less than three reference paths per agent. Second, DAC and WIMP do not have a learned path classification module to predict path probabilities or a path classification loss as a training objective. DAC uses a heuristic algorithm to rank paths based on the distance-along-lane score and centerline-yaw score, and WIMP finds only one single closest reference path for each agent using a heuristic algorithm. On the other hand, PBP has a path classification module that predicts the probability distribution over all candidate paths.

PRIME also predicts trajectories in the Frenet frame, but it uses a model-based trajectory generator (a quartic polynomial) to sample trajectories. In contrast, PBP's trajectory generator is entirely learned, allowing it to generate a variety of motion profiles in the Frenet frame.

## PBP: Path-based prediction

### III-A Problem statement

The objective of a trajectory prediction model is to forecast the future trajectories of a set of agents in the scene, given their past history positions and map context. We denote the past history positions of an agent $a$ by ${\{{\mathbf{P}}^{a}\}}_{Past} = {\{{\mathbf{P}}_{{- T'} + 1}^{a},{\mathbf{P}}_{{- T'} + 2}^{a},\cdots,{\mathbf{P}}_{0}^{a}\}}$ where ${\mathbf{P}}_{t}^{a} = {(x_{t}^{a},y_{t}^{a})}$ is a 2-D coordinate position, and $T' > 0$ is the past history length. The map context $\mathcal{M}$ is represented as a set of discretized lane segments ${\{ l_{j}\}}_{j = 1}^{L}$ and their connections. The prediction model is required to forecast the future state of each agent ${\{{\mathbf{P}}^{a}\}}_{Future} = {\{{\mathbf{P}}_{1}^{a},{\mathbf{P}}_{2}^{a},\cdots,{\mathbf{P}}_{T}^{a}\}}$ over the time horizon $T > 0$. In order to capture the uncertainties of the agents' future behaviors, the model will output $K$ trajectory predictions and their probabilities ${\{ p_{k}\}}_{k = 1}^{K}$ for each agent.

### III-B Overall architecture

The overall architecture of our PBP model is illustrated in Figure 2, which consists of four main components. The scene encoder generates agent and map embeddings from agent-map and agent-agent interactions (Section III-C). The candidate path sampler samples the candidate paths from the map for each agent (Section III-D). The path classifier predicts the probability of each sampled path (Section III-E). Finally, the trajectory regressor decodes trajectories conditioned on the selected paths (Section III-F).

### III-C Scene encoding

The scene encoder module creates agent feature vectors from the scene for each agent. In this work, we borrowed the scene encoder module from the HiVT model, a recently proposed trajectory prediction model that achieves state-of-the-art performance on Argoverse. The HiVT scene encoder represents each scene as a set of vectorized entities. It uses this representation to encode the scene by hierarchical aggregation of the spatial-temporal information. First, rotational invariant local feature vectors are encoded for each agent with a transformer module to aggregate neighboring agents' information as well as local map structure. Next, global interactions between agents are aggregated into each agent's feature vector to capture the scene-level context. The outputs of the encoder are the feature vectors for each agent denoted by $\mathbf{F}_{\mathbf{a}}$.

### III-D Candidate sampling

The objective of the candidate sampling module is to create a set of candidate reference paths for each agent by traversing the lane graph. A reference path is defined as a sequence of connected lane segments $r_{i} = {\{ l_{i,1},l_{i,2},\cdots,l_{i,R_{i}}\}}$. The starting point of the reference path for an agent $a$ is supposed to be in the vicinity of the agent's current location ${\mathbf{P}}_{0}^{a}$, and the endpoint is supposed to be in the vicinity of the agent's future trajectory endpoint ${\mathbf{P}}_{T}^{a}$, as is illustrated in Figure 1.

To select the candidate reference path for an agent $a$, we first select a set of *seed lane segments* that will be considered as the path starting points. We used a simple heuristic to select the seed lane segments by picking the lane segments that are within a distance range of the agent's current location and have their lane directions within a range of the agent's current heading. By picking the seed lanes this way, we will have candidate paths starting from not only the agent's current lane but also the neighbor lanes, which allows the model to predict lane-changing trajectories.

From the seed lane segments, we run a breadth-first search to find the candidate paths. The output of the candidate sampling module is a set of candidate reference paths for each agent, denoted as $\mathcal{R}^{a} = {\{ r_{i}^{a}\}}$.

### III-E Path classification

Given the set of candidate reference paths, the path classification module predicts the probability distribution over them using the agent and path features.

To encode the features ${\mathbf{F}}_{p,i}$ of a path $r_{i} = {\{ l_{i,1},l_{i,2},\cdots,l_{i,R_{i}}\}}$, we pick the the start segment $l_{i,1}$, the middle segment $l_{{i,R_{i}}/{/2}}$, and the end segment $l_{i,R_{i}}$ of the path, and use their coordinates and direction vectors as the raw feature. We encode those raw features with an MLP to a feature vector ${\mathbf{F}}_{p}$.

In addition to the agent and path features, we also create an agent-path pair feature that captures the interactions between the agent and the path. We use the distance vectors and angle deltas from the agent's current location to the start, middle, and end segments of the path as the raw features. We then use another MLP network to encode them to an agent-path pair feature vector ${\mathbf{F}}_{a,{(p,i)}}$ We concatenate the agent feature ${\mathbf{F}}_{a}$, path feature ${\mathbf{F}}_{p}$, and agent-path pair feature ${\mathbf{F}}_{a,{(p,i)}}$ together and run them through another MLP network to predict the probability distribution over all candidate paths of the agent, trained with the cross-entropy loss as $\mathcal{L}_{cls}$. We decide the ground-truth reference path $r_{GT}^{a}$ of the agent $a$ based on its ground-truth future trajectory ${\{{\mathbf{P}}^{a}\}}_{Future}$, similar to the ground-truth goal selection in goal-based prediction. At inference time, we use non-maximum suppression (NMS) to sample a set of $K$ diverse paths to decode the trajectory predictions.

PBP in Cartesian frame TABLE I: Decoder ablations on Argoverse validation set.

### III-F Frenet frame trajectory decoding

The trajectory regressor module decodes trajectories conditioned on the reference paths. One key difference between our trajectory regressor and the one used in traditional goal-based prediction is that it has the information of the whole reference path instead of just the final goal endpoint. To leverage this path information, we designed our trajectory regressor to decode trajectories in the path-relative Frenet frame.

For each selected reference path $r_{i}^{a}$, the trajectory regressor predicts a trajectory in path-relative Frenet frame, with longitudinal component ${\{{\hat{s}}_{t}^{a}\}}_{t = {1\cdots T}}$ and lateral component ${\{{\hat{d}}_{t}^{a}\}}_{t = {1\cdots T}}$, whose inputs include agent features ${\mathbf{F}}_{a}$, path features ${\mathbf{F}}_{p,i}$, and agent history in Frenet frame ${\mathbf{P}}_{{Past},r_{i}^{a}}^{a}$.

During training, we use a teacher-forcing technique and train the trajectory regressor using the ground-truth reference path $r_{GT}^{a}$. We transform the ground-truth trajectory ${\mathbf{P}}_{Future}^{a}$ to the Frenet frame w.r.t. $r_{GT}^{a}$, with longitudinal component ${\{ s_{t}^{a}\}}_{t = {1\cdots T}}$ and lateral component ${\{ d_{t}^{a}\}}_{t = {1\cdots T}}$.

The loss function is defined as smooth $L1$ losses of the longitudinal and lateral components in the Frenet frame: The total loss is a weighted sum of the path classification loss and the trajectory regression loss over all agents: After predicting the trajectories in the Frenet frame, we transform them back to the Cartesian frame using the corresponding reference path, using the formulas.

### III-G Path-free prediction for non-map-compliant agents

In order to robustly handle non-map-compliant agents (i.e., agents whose behaviors are not compliant with the annotated map), we additionally train a path-free trajectory decoder with the same architecture as the original HiVT decoder. We also train a binary classifier to select the predictions between the two decoders for each agent. The path-free decoder and its classifier share the same scene encoder as the PBP decoder and use the agent feature vector ${\mathbf{F}}_{a}$ as the input. During training, we label an agent as a path-free agent if its ground-truth trajectory is more than 5 meters away from any candidate reference path.

TABLE II: Comparison to the state-of-the-art models on the Argoverse leaderboard

## Experiments

### IV-A Dataset

We evaluate our model using the public Argoverse dataset. Argoverse includes track histories of agents published at 10 Hz and vectorized HD maps. The task involves predicting the future trajectory of a focal agent in each scenario over a prediction horizon of 3 seconds, conditioned on 2 seconds of track histories and the HD map of the scene.

### IV-B Implementation details

We implemented our path-based prediction decoder on top of the open-source HiVT-64 scene encoder. We followed a similar training scheme as the original HiVT model for PBP and its variants. We used 8 AWS T4 GPUs for model training and evaluation. We trained each model for 64 epochs with a batch size of 4 and the Adam optimizer with a learning rate of 0.0005 and a decay weight of 0.0001.

### IV-C Metrics

Best-of-K metrics: We report results using the standard metrics used for multimodal trajectory prediction: minADE$_{K}$, minFDE$_{K}$ and miss rate (MR$_{K}$). The standard metrics compute prediction errors using the best of $K$ predicted trajectories, in order to not penalize diverse but plausible modes predicted by the model. The minADE$_{K}$ metric averages the L2 norms of displacement errors between the ground truth and the best mode over the prediction horizon. The minFDE$_{K}$ metric computes the L2 norm of the displacement error between the final predicted waypoint of the best mode and the final waypoint in the ground truth. Finally, miss rate computes the fraction of all predictions where none of the $K$ predicted trajectories are within 2 meters of the ground truth. We report results for $K$=1 and $K$=6, following the convention used in Argoverse.

Map compliance metrics: A key limitation of the standard best-of-k metrics is that they fail to penalize implausible predictions, even if they veer off-road or violate lane directions. Ideally, we want all $K$ predictions to be plausible and map-compliant. Thus, we additionally report two map-compliance metrics. Offroad rate measures the fraction of the predicted waypoints at a given horizon falling outside the drivable area. This is closely related to Argoverse's drivable area compliance (DAC) metric, but our offroad rate metric measures each individual waypoint and can report map compliance as a function of the prediction horizon as in Figure 3. Lane deviation measures the L2 distance between a predicted waypoint and the nearest lane centerline. It captures map compliance signals even when the waypoint is inside the drivable area. We report the two map-compliance metrics averaged over all waypoints along the whole prediction horizon and all $K = 6$ trajectories.

### IV-D Decoder ablation study

We first perform a set of controlled experiments comparing our PBP model with path classification and Frenet frame trajectory decoder against the following alternative prediction decoders.

Multimodal regression: This is the original HiVT-64 model. It directly regresses multimodal predictions with the winner-takes-all loss.

Anchor-based: This decoder is used in MultiPath. It predicts offsets with respect to fixed anchor trajectories. We obtain the anchors using K-means clustering on the train set.

Goal-based: The goal-based prediction decoder uses only the goal endpoint features (no path features) in its goal classification module and decodes trajectories conditioned on goal endpoints (no Frenet frame).

PBP in Cartesian frame: This decoder performs path classification as in PBP but decodes trajectories in the Cartesian frame instead of the Frenet frame.

Figure 3: Offroad rate.

For fair comparisons, we implemented all decoders using the same HiVT-64 encoder as PBP. The results are shown in Table I, and we observe the following.

Significantly better map compliance. PBP and goal-based prediction achieve significantly lower offroad rates and lane deviation errors than multimodal regression and anchor-based decoders. This effect is even more pronounced over longer prediction horizons, as shown in Figure 3.

Advantage over goal-based prediction. Compared to goal-based prediction, PBP achieves overall lower prediction errors in terms of minFDE and MR and better map compliance metrics, because of the usage of richer path features. From Figure 3, goal-based prediction has strong map compliance at the final waypoint (i.e., goal endpoint), but it has higher offroad rates at the intermediate waypoints than PBP because of the missing path information.

Slightly worse mode diversity than goal-free decoders. PBP's minFDE$_{6}$ metric is slightly worse than the multimodal regression baseline by 1%. This lower diversity is because PBP's predictions are constrained to lanes (as is shown in Figure 4). We argue that it is a fair trade-off to have more map-compliant predictions for real-world autonomous driving applications.

Figure 4: Qualitative comparison between original HiVT-64 and PBP. The first column shows the predictions from HiVT-64, and the second column shows the predictions from PBP. The blue, green, and red lines represent past history, ground-truth, and top-6 prediction trajectories, respectively.

### IV-E Comparison against the state-of-the-art

We submitted our PBP model to the Argoverse leaderboard. Table II reports our results along with the top entries on the leaderboard. Our model achieves the highest drivable area compliance (DAC) on the leaderboard, outperforming state-of-the-art in terms of map compliance, while being competitive in terms of minADE$_{1}$, minFDE$_{1}$, and MR$_{1}$. Those results are consistent with our ablation study results on the validation set. PBP's top-$6$ metrics are slightly worse than the top leaderboard submissions, but note that most of them used extensive model ensembling (e.g., ), while our submission used only one single pair of encoder and decoder. Our inference latency is 72.7 $ms$ on an AWS T4 GPU, with 43.0 $ms$ on the scene encoder and 29.7 $ms$ on the trajectory decoder.

### IV-F Qualitative examples

Figure 4 shows a few qualitative comparisons between the HiVT-64 baseline (using multimodal regression) and PBP. The results show PBP predicts map-compliant trajectories from all modes, while HiVT-64 has many offroad predictions. The example on the last row shows that PBP is able to correctly predict lane-changing trajectories because the path candidates also contain paths on the neighbor lanes.

## Conclusion

In this paper, we propose PBP, a novel path-based prediction approach. In contrast to the traditional goal-based prediction approaches, PBP performs classification on the whole reference path instead of just the goal endpoint. The additional reference path information improves the path classification accuracy and allows PBP to decode trajectories in the path-relative Frenet frame. Evaluation results show that the path-based prediction approach makes the trajectory predictions significantly more map-compliant compared to the traditional multimodal regression and goal-based prediction approaches, while maintaining competitive or better prediction accuracy.
