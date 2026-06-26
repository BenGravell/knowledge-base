<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

PBP: Path-based Trajectory Prediction for Autonomous Driving

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Trajectory prediction plays a crucial role in the autonomous driving stack by enabling autonomous vehicles to anticipate the motion of surrounding agents. Goal-based prediction models have gained traction in recent years for addressing the multimodal nature of future trajectories. Goal-based prediction models simplify multimodal prediction by first predicting 2D goal locations of agents and then predicting trajectories conditioned on each goal. However, a single 2D goal location serves as a weak inductive bias for predicting the whole trajectory, often leading to poor map compliance, i.e., part of the trajectory going off-road or breaking traffic rules. In this paper, we improve upon goal-based prediction by proposing the Path-based prediction (PBP) approach. PBP predicts a discrete probability distribution over reference paths in the HD map using the path features and predicts trajectories in the path-relative Frenet frame. We applied the PBP trajectory decoder on top of the HiVT scene encoder and report results on the Argoverse dataset.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our experiments show that PBP achieves competitive performance on the standard trajectory prediction metrics, while significantly outperforming state-of-the-art baselines in terms of map compliance.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

To safely navigate through traffic while offering passengers a smooth ride, autonomous vehicles need the ability to predict the trajectories of surrounding agents. There is inherent uncertainty in predicting the future, making this a challenging task. Agent trajectories tend to be highly non-linear over long prediction horizons. Additionally, the distribution of future trajectories is multimodal; in a given scene an agent could have multiple plausible goals and could take various paths to each goal.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In spite of these challenges, agent motion is not completely unconstrained. Vehicles tend to follow the direction of motion ascribed to their lanes, make legal turns and lane changes, and stop at stop signs and crosswalks. Bicyclists tend to use the bike lane, and pedestrians tend to walk along sidewalks and crosswalks. High-definition (HD) maps of traffic scenes efficiently represent such constraints on agent motion and have thus been a critical component of autonomous driving datasets. In fact, it has been shown in many prior works that a key requirement of the trajectory prediction task for a real-world autonomous driving system is to predict map-compliant trajectories -- trajectories that don't go off-road or violate traffic rules over long prediction horizons. For example, incorrectly predicting a non-map-compliant trajectory that encroaches into the oncoming traffic lane could cause the ego vehicle to brake hard or even make dangerous maneuvers on the road. As a result, prediction map compliance w.r.t. the provided HD map is central to our proposed approach and experimental evaluation.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prior works have leveraged HD maps for trajectory prediction in two distinct ways. First, the HD map is often used as an input to the model. Early works use rasterized HD maps and CNN encoders. More recent works directly encode vectorized HD maps using PointNet encoders, graph neural networks or transformer layers. The map encoding is then used by a multimodal prediction header to output $K$ trajectories and their probabilities. A drawback of multimodal prediction headers is that they need to learn a complex one-to-many mapping from the entire scene context to multiple future trajectories, often leading to non-map-compliant predictions.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address this shortcoming, a few recent works additionally use the HD map for goal-based prediction. Goal-based prediction models associate each mode of the trajectory distribution to a 2D goal location sampled from the HD map. They predict a discrete distribution over the sampled goals, and then predict trajectories conditioned on each goal. This simplifies the mapping learned by the prediction header, and also makes each mode of the trajectory distribution more interpretable. However, 2D goal locations serve as a weak inductive bias to condition predictions, and may lead to imprecise trajectories for each goal.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we seek to improve upon goal-based trajectory prediction. We argue that reference paths rather than 2D goals are the appropriate HD map element to condition predicted trajectories. We define reference paths as segments of lane centerlines close to the agent of interest that the agent may follow over the prediction horizon. We propose a novel path classifier that predicts a discrete probability distribution over the candidate reference paths and a trajectory completion module that predicts trajectories conditioned on each path in the Frenet frame. Figure 1 shows an overview of our approach. In particular, our approach has two key advantages over goal-based prediction: Path features instead of goal features: We predict trajectories conditioned on feature descriptors of the entire reference path instead of just 2D goal locations. This is a more informative feature descriptor and leads to more map-compliant trajectories over longer prediction horizons compared to goal-based prediction.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prediction in the Frenet frame: The reference paths allow us to predict trajectories in the Frenet frame relative to the path. Compared to the Cartesian frame with varying lane locations and curvatures, predictions in the Frenet frame have much lower variance, which leads to more map-compliant trajectories that better generalize to novel scene layouts.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our path-based trajectory decoder is modular by design and could be used with any existing scene encoder such as VectorNet, LaneGCN, Scene Transformer, Wayformer, etc. Here, we build our decoder on top of the recently proposed HiVT encoder that achieved competitive results on the Argoverse dataset and has a publicly available code base. Our results on the Argoverse dataset show that our path-based decoder achieves competitive performance in terms of the standard minADE, minFDE, and miss rate metrics, while significantly outperforming the HiVT baseline and goal-based prediction in terms of map compliance metrics.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our contributions can be summarized as follows: We propose a novel path-based trajectory prediction (PBP) approach that improves upon traditional goal-based prediction.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We applied our PBP trajectory decoder on top of the HiVT scene encoder. The resulting model achieves the best map compliance metric on the Argoverse leaderboard while being competitive in terms of prediction error metrics.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present extensive ablation studies comparing different trajectory decoder approaches on the Argoverse validation set.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Problem statement", "weight": 1.0} -->

The map context $\mathcal{M}$ is represented as a set of discretized lane segments ${\{ l_{j}\}}_{j = 1}^{L}$ and their connections. The prediction model is required to forecast the future state of each agent ${\{{\mathbf{P}}^{a}\}}_{Future} = {\{{\mathbf{P}}_{1}^{a},{\mathbf{P}}_{2}^{a},\cdots,{\mathbf{P}}_{T}^{a}\}}$ over the time horizon $T > 0$. In order to capture the uncertainties of the agents' future behaviors, the model will output $K$ trajectory predictions and their probabilities ${\{ p_{k}\}}_{k = 1}^{K}$ for each agent.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-B Overall architecture", "weight": 1.0} -->

The overall architecture of our PBP model is illustrated in Figure 2, which consists of four main components. The scene encoder generates agent and map embeddings from agent-map and agent-agent interactions (Section III-C). The candidate path sampler samples the candidate paths from the map for each agent (Section III-D). The path classifier predicts the probability of each sampled path (Section III-E). Finally, the trajectory regressor decodes trajectories conditioned on the selected paths (Section III-F).

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-C Scene encoding", "weight": 1.0} -->

The scene encoder module creates agent feature vectors from the scene for each agent. In this work, we borrowed the scene encoder module from the HiVT model, a recently proposed trajectory prediction model that achieves state-of-the-art performance on Argoverse. The HiVT scene encoder represents each scene as a set of vectorized entities. It uses this representation to encode the scene by hierarchical aggregation of the spatial-temporal information. First, rotational invariant local feature vectors are encoded for each agent with a transformer module to aggregate neighboring agents' information as well as local map structure. Next, global interactions between agents are aggregated into each agent's feature vector to capture the scene-level context. The outputs of the encoder are the feature vectors for each agent denoted by $\mathbf{F}_{\mathbf{a}}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-D Candidate sampling", "weight": 1.0} -->

The objective of the candidate sampling module is to create a set of candidate reference paths for each agent by traversing the lane graph. A reference path is defined as a sequence of connected lane segments $r_{i} = {\{ l_{i,1},l_{i,2},\cdots,l_{i,R_{i}}\}}$. The starting point of the reference path for an agent $a$ is supposed to be in the vicinity of the agent's current location ${\mathbf{P}}_{0}^{a}$, and the endpoint is supposed to be in the vicinity of the agent's future trajectory endpoint ${\mathbf{P}}_{T}^{a}$, as is illustrated in Figure 1.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-D Candidate sampling", "weight": 1.0} -->

To select the candidate reference path for an agent $a$, we first select a set of *seed lane segments* that will be considered as the path starting points. We used a simple heuristic to select the seed lane segments by picking the lane segments that are within a distance range of the agent's current location and have their lane directions within a range of the agent's current heading. By picking the seed lanes this way, we will have candidate paths starting from not only the agent's current lane but also the neighbor lanes, which allows the model to predict lane-changing trajectories.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-D Candidate sampling", "weight": 1.0} -->

From the seed lane segments, we run a breadth-first search to find the candidate paths. The output of the candidate sampling module is a set of candidate reference paths for each agent, denoted as $\mathcal{R}^{a} = {\{ r_{i}^{a}\}}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-E Path classification", "weight": 1.0} -->

Given the set of candidate reference paths, the path classification module predicts the probability distribution over them using the agent and path features.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-E Path classification", "weight": 1.0} -->

To encode the features ${\mathbf{F}}_{p,i}$ of a path $r_{i} = {\{ l_{i,1},l_{i,2},\cdots,l_{i,R_{i}}\}}$, we pick the the start segment $l_{i,1}$, the middle segment $l_{{i,R_{i}}/{/2}}$, and the end segment $l_{i,R_{i}}$ of the path, and use their coordinates and direction vectors as the raw feature. We encode those raw features with an MLP to a feature vector ${\mathbf{F}}_{p}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-E Path classification", "weight": 1.0} -->

In addition to the agent and path features, we also create an agent-path pair feature that captures the interactions between the agent and the path. We use the distance vectors and angle deltas from the agent's current location to the start, middle, and end segments of the path as the raw features. We then use another MLP network to encode them to an agent-path pair feature vector ${\mathbf{F}}_{a,{(p,i)}}$ We concatenate the agent feature ${\mathbf{F}}_{a}$, path feature ${\mathbf{F}}_{p}$, and agent-path pair feature ${\mathbf{F}}_{a,{(p,i)}}$ together and run them through another MLP network to predict the probability distribution over all candidate paths of the agent, trained with the cross-entropy loss as $\mathcal{L}_{cls}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-E Path classification", "weight": 1.0} -->

We decide the ground-truth reference path $r_{GT}^{a}$ of the agent $a$ based on its ground-truth future trajectory ${\{{\mathbf{P}}^{a}\}}_{Future}$, similar to the ground-truth goal selection in goal-based prediction. At inference time, we use non-maximum suppression (NMS) to sample a set of $K$ diverse paths to decode the trajectory predictions.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-E Path classification", "weight": 1.0} -->

PBP in Cartesian frame TABLE I: Decoder ablations on Argoverse validation set.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-F Frenet frame trajectory decoding", "weight": 1.0} -->

The trajectory regressor module decodes trajectories conditioned on the reference paths. One key difference between our trajectory regressor and the one used in traditional goal-based prediction is that it has the information of the whole reference path instead of just the final goal endpoint. To leverage this path information, we designed our trajectory regressor to decode trajectories in the path-relative Frenet frame.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-F Frenet frame trajectory decoding", "weight": 1.0} -->

During training, we use a teacher-forcing technique and train the trajectory regressor using the ground-truth reference path $r_{GT}^{a}$. We transform the ground-truth trajectory ${\mathbf{P}}_{Future}^{a}$ to the Frenet frame w.r.t. $r_{GT}^{a}$, with longitudinal component ${\{ s_{t}^{a}\}}_{t = {1\cdots T}}$ and lateral component ${\{ d_{t}^{a}\}}_{t = {1\cdots T}}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-F Frenet frame trajectory decoding", "weight": 1.0} -->

The loss function is defined as smooth $L1$ losses of the longitudinal and lateral components in the Frenet frame: The total loss is a weighted sum of the path classification loss and the trajectory regression loss over all agents: After predicting the trajectories in the Frenet frame, we transform them back to the Cartesian frame using the corresponding reference path, using the formulas.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-G Path-free prediction for non-map-compliant agents", "weight": 1.0} -->

In order to robustly handle non-map-compliant agents (i.e., agents whose behaviors are not compliant with the annotated map), we additionally train a path-free trajectory decoder with the same architecture as the original HiVT decoder. We also train a binary classifier to select the predictions between the two decoders for each agent. The path-free decoder and its classifier share the same scene encoder as the PBP decoder and use the agent feature vector ${\mathbf{F}}_{a}$ as the input. During training, we label an agent as a path-free agent if its ground-truth trajectory is more than 5 meters away from any candidate reference path.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A Dataset", "weight": 1.0} -->

We evaluate our model using the public Argoverse dataset. Argoverse includes track histories of agents published at 10 Hz and vectorized HD maps. The task involves predicting the future trajectory of a focal agent in each scenario over a prediction horizon of 3 seconds, conditioned on 2 seconds of track histories and the HD map of the scene.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B Implementation details", "weight": 1.0} -->

We implemented our path-based prediction decoder on top of the open-source HiVT-64 scene encoder. We followed a similar training scheme as the original HiVT model for PBP and its variants. We used 8 AWS T4 GPUs for model training and evaluation. We trained each model for 64 epochs with a batch size of 4 and the Adam optimizer with a learning rate of 0.0005 and a decay weight of 0.0001.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-C Metrics", "weight": 1.0} -->

Best-of-K metrics: We report results using the standard metrics used for multimodal trajectory prediction: minADE$_{K}$, minFDE$_{K}$ and miss rate (MR$_{K}$). The standard metrics compute prediction errors using the best of $K$ predicted trajectories, in order to not penalize diverse but plausible modes predicted by the model. The minADE$_{K}$ metric averages the L2 norms of displacement errors between the ground truth and the best mode over the prediction horizon. The minFDE$_{K}$ metric computes the L2 norm of the displacement error between the final predicted waypoint of the best mode and the final waypoint in the ground truth. Finally, miss rate computes the fraction of all predictions where none of the $K$ predicted trajectories are within 2 meters of the ground truth. We report results for $K$=1 and $K$=6, following the convention used in Argoverse.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-C Metrics", "weight": 1.0} -->

Map compliance metrics: A key limitation of the standard best-of-k metrics is that they fail to penalize implausible predictions, even if they veer off-road or violate lane directions. Ideally, we want all $K$ predictions to be plausible and map-compliant. Thus, we additionally report two map-compliance metrics. Offroad rate measures the fraction of the predicted waypoints at a given horizon falling outside the drivable area. This is closely related to Argoverse's drivable area compliance (DAC) metric, but our offroad rate metric measures each individual waypoint and can report map compliance as a function of the prediction horizon as in Figure 3. Lane deviation measures the L2 distance between a predicted waypoint and the nearest lane centerline. It captures map compliance signals even when the waypoint is inside the drivable area. We report the two map-compliance metrics averaged over all waypoints along the whole prediction horizon and all $K = 6$ trajectories.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-D Decoder ablation study", "weight": 1.0} -->

We first perform a set of controlled experiments comparing our PBP model with path classification and Frenet frame trajectory decoder against the following alternative prediction decoders.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-D Decoder ablation study", "weight": 1.0} -->

Multimodal regression: This is the original HiVT-64 model. It directly regresses multimodal predictions with the winner-takes-all loss.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-D Decoder ablation study", "weight": 1.0} -->

Anchor-based: This decoder is used in MultiPath. It predicts offsets with respect to fixed anchor trajectories. We obtain the anchors using K-means clustering on the train set.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-D Decoder ablation study", "weight": 1.0} -->

Goal-based: The goal-based prediction decoder uses only the goal endpoint features (no path features) in its goal classification module and decodes trajectories conditioned on goal endpoints (no Frenet frame).

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-D Decoder ablation study", "weight": 1.0} -->

PBP in Cartesian frame: This decoder performs path classification as in PBP but decodes trajectories in the Cartesian frame instead of the Frenet frame.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-D Decoder ablation study", "weight": 1.0} -->

For fair comparisons, we implemented all decoders using the same HiVT-64 encoder as PBP. The results are shown in Table I, and we observe the following.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-D Decoder ablation study", "weight": 1.0} -->

Significantly better map compliance. PBP and goal-based prediction achieve significantly lower offroad rates and lane deviation errors than multimodal regression and anchor-based decoders. This effect is even more pronounced over longer prediction horizons, as shown in Figure 3.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-D Decoder ablation study", "weight": 1.0} -->

Advantage over goal-based prediction. Compared to goal-based prediction, PBP achieves overall lower prediction errors in terms of minFDE and MR and better map compliance metrics, because of the usage of richer path features. From Figure 3, goal-based prediction has strong map compliance at the final waypoint (i.e., goal endpoint), but it has higher offroad rates at the intermediate waypoints than PBP because of the missing path information.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-D Decoder ablation study", "weight": 1.0} -->

Slightly worse mode diversity than goal-free decoders. PBP's minFDE$_{6}$ metric is slightly worse than the multimodal regression baseline by 1%. This lower diversity is because PBP's predictions are constrained to lanes (as is shown in Figure 4). We argue that it is a fair trade-off to have more map-compliant predictions for real-world autonomous driving applications.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-E Comparison against the state-of-the-art", "weight": 1.0} -->

We submitted our PBP model to the Argoverse leaderboard. Table II reports our results along with the top entries on the leaderboard. Our model achieves the highest drivable area compliance (DAC) on the leaderboard, outperforming state-of-the-art in terms of map compliance, while being competitive in terms of minADE$_{1}$, minFDE$_{1}$, and MR$_{1}$. Those results are consistent with our ablation study results on the validation set. PBP's top-$6$ metrics are slightly worse than the top leaderboard submissions, but note that most of them used extensive model ensembling (e.g., ), while our submission used only one single pair of encoder and decoder. Our inference latency is 72.7 $ms$ on an AWS T4 GPU, with 43.0 $ms$ on the scene encoder and 29.7 $ms$ on the trajectory decoder.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we propose PBP, a novel path-based prediction approach. In contrast to the traditional goal-based prediction approaches, PBP performs classification on the whole reference path instead of just the goal endpoint. The additional reference path information improves the path classification accuracy and allows PBP to decode trajectories in the path-relative Frenet frame. Evaluation results show that the path-based prediction approach makes the trajectory predictions significantly more map-compliant compared to the traditional multimodal regression and goal-based prediction approaches, while maintaining competitive or better prediction accuracy.
