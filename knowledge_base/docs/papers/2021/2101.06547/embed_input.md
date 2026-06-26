<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

LookOut: Diverse Multi-Future Prediction and Planning for Self-Driving

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we present LookOut, a novel autonomy system that perceives the environment, predicts a diverse set of futures of how the scene might unroll and estimates the trajectory of the SDV by optimizing a set of contingency plans over these future realizations. In particular, we learn a diverse joint distribution over multi-agent future trajectories in a traffic scene that covers a wide range of future modes with high sample efficiency while leveraging the expressive power of generative models. Unlike previous work in diverse motion forecasting, our diversity objective explicitly rewards sampling future scenarios that require distinct reactions from the self-driving vehicle for improved safety. Our contingency planner then finds comfortable and non-conservative trajectories that ensure safe reactions to a wide range of future scenarios. Through extensive evaluations, we show that our model demonstrates significantly more diverse and sample-efficient motion forecasting in a large-scale self-driving dataset as well as safer and less-conservative motion plans in long-term closed-loop simulations when compared to current state-of-the-art models.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Self-driving vehicles (SDVs) have the potential to enhance considerably the safety of our roads as, unlike humans, they can constantly scan the surrounding environment without getting distracted or being impaired while driving. Key to the success of a self-driving vehicle is its ability to perceive its surroundings and predict the future trajectory of the traffic participants, particularly those that might affect its decision making. These predictions are then exploited by the motion planning module to plan a safe and comfortable maneuver towards the goal.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Forecasting the behavior of traffic participants is very challenging as humans do not always follow the rules of the road and sometimes exhibit erratic behaviors. Furthermore, the scene might unroll in many possible ways in the future, depending heavily on the interactions between actors (e.g., at a merge, either actor A yields to actor B or vice versa). While most works predict each actor's future independently, recent approaches model actor interactions and can produce samples that explain the full scene in a consistent manner. However, they require prohibitively large numbers of samples to cover the long-tails of the distribution. This is problematic since these long tails are critical for safety, as failing to take them into account might result in an accident (e.g., an impaired driver running a red traffic light perpendicularly to the SDV's intended trajectory). Thus, there is a need to develop prediction systems that can efficiently sample the diverse set of possible futures. Unfortunatelly, existing approaches are not sample efficient as they trivially encourage diversity in euclidean space, thus utilizing samples to cover irrelevant actors or actions that do not impact the SDV's behavior.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, existing motion planners cannot take advantage of prediction systems that produce scene-consistent samples. Instead, they optimize the expected cost by sampling the marginal distribution of each actor independently, thus ignoring the fact that some of these futures cannot happen at the same time (e.g., either the horizontal or vertical traffic can flow at a 4-way stop, but not both). These planners also assume that the SDV must commit to a single long-term trajectory, when in practice it can execute a short-term action and re-plan as newer sensor observations become available. As a consequence, they result in suboptimal and overly conservative trajectories, e.g., the SDV braking prematurely to react to an unlikely future instead of maintaining its speed as long as it is able to stop safely and comfortably later.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we propose LookOut, a full end-to-end autonomy system that detects actors in the scene, predicts a diverse set of consistent futures with high sample efficiency, and plans an action that behaves defensively to potential hazards while not overreacting to low probability dangers far into the future. In particular, to address the sample inefficiency and limited mode coverage in motion forecasting we formulate this task as a diverse set prediction problem, where each element in the set reflects one possible future at the scene level. To enable this set to cover the future modes that matter for our decision making, we directly optimize the diversity of the downstream ego-vehicle motion plans. Then, a scenario scoring module estimates the probability of each future in the set, enabling our planner to account for unlikely but safety-critical scenarios without being overly conservative. Finally, we propose a novel contingency planner that is able to leverage multiple consistent futures by planning separate long-term responses for each of future, while sharing an initial short-term action that behaves non-conservatively with respect to the futures and avoids immediate collision. Fig. 1 shows an example of two diverse futures and the corresponding shared action and contingent plans.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate the effectiveness of our approach in large-scale open-loop and closed-loop experiments that comprise a wide variety of complex scenarios. Our extensive experiments show that LookOut's driving is significantly safer as well as less conservative than previous state-of-the-art approaches. Furthermore, there exists a trade-off between diversity and reconstruction quality of the forecasts; our approach can produce much better reconstruction than other methods with similar diversity and higher diversity with similar reconstruction capability.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Motion Forecasting", "weight": 1.0} -->

A common approach for actor modeling has been to independently predict the trajectory of each actor. These predictions can be represented as closed-form gaussian distributions, a classification or energy over a discrete grid/graph/set structure, or trajectory samples of a stochastic model. One approach to tractably model the traffic multimodality jointly across actors is to stochastically sample one possible future scenario at a time, by sampling latent variables that encode the joint scene dynamics, and then decode the future trajectories. These are mainly divided into autoregressive models, and implicit latent variable models. However, these methods require a high number of samples to characterize the scene. In contrast, work in diverse motion forecasting has focused on achieving high sample-efficiency to cover the main modes of the distribution. This is especially important in self-driving as SDVs need to be able to anticipate rare or dangerous behavior by other actors on the road in order to plan safe responses. Recent work has explored how to encourage more diverse predictions from pretrained variational inference models. They train new encoders that output a fixed number of jointly diverse samples of latent variables.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Motion Forecasting", "weight": 1.0} -->

The formulation in directly outputs the set of latent codes, and evaluates their diversity based on determinantal point processes (DPP). In the work of, a set of multivariate gaussian distributions are sampled jointly via reparameterization trick with a shared noise, and a diversity loss based on the L2-distance between motion forecast samples is used to increase diversity in the predictions. Alternatively, trains a conditional GAN to output diverse samples using Farthest Point Sampling on the latent space to spread out over more modes of the latent space. Finally, trains their trajectory samples to stay within the drivable area, allowing for greater diversity while retaining admissibility. While these works achieve greater diversity and accuracy in motion prediction, it is unclear how these improvements translate into better motion planning for autonomous agents.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Planning", "weight": 1.0} -->

In motion planning the goal is to generate a trajectory for the self-driving vehicle to drive safely, comfortably, and progressing toward the goal. A popular approach to achieve this task is to design a cost function that encodes all the objectives above and find a minimum-cost trajectory. Such optimizations have been solved using continuous-optimization, sampling, or search. These methods achieve safety by including a collision cost in the objective function which is computed with respect to the predicted trajectories of actors in the scene. However, in probabilistic settings where the predictions take the form of trajectory distributions, the above methods compute the collision cost in expectation, minimizing the expected cost over all future predicted scenarios with a single plan. Given a set of joint diverse predictions, it is possible that the SDV will need to plan for a greater number of unlikely, but safety-critical future scenarios that will require it drive defensively (e.g. yield, change lanes). However, it is undesirable to always brake preemptively for such rare scenarios, or ignore them altogether.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Planning", "weight": 1.0} -->

Work in optimization-based motion planning plan for such rare scenarios by picking trajectory plans that ensure it can react to them safely, while also optimizing for objectives such as progress and comfort. splits the planned trajectory into an initial shared section, and a set of branched plans that could be taken from the end of the shared section. predict the probability that a defensive maneuver will be necessary in the near future, and decide whether to postpone the decision to the future (where more information will be available).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Diverse Prediction and Planning", "weight": 1.0} -->

In this section, we break down the autonomy problem of mapping sensor data to an executable action into several modules which provide interpretability of the SDV decision making. Towards this goal, we first learn a joint perception and future prediction model that detects relevant objects and estimates the joint distribution over all actors' future trajectories with an implicit latent variable model (Section 3.1). Despite its sample inefficiency, such generative model allows us to learn a very powerful and efficient trajectory decoder from latent samples. Next, we leverage this decoder to learn a diverse latent sampler that achieves high sample efficiency from the planner's perspective (Section 3.2). Then, we estimate the probability of each future realization in the set (Section 3.3). Finally, we design a novel contingency planner that plans a safe trajectory for each possible future without being overly cautious (Section 3.4). Fig. 2 depicts an overview of our approach.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Joint Perception and Motion Forecasting", "weight": 1.0} -->

In order to extract features useful for both detection and motion forecasting, we employ a convolutional backbone network inspired, which takes as input a history of voxelized LiDAR sweeps and a raster HD map, both in bird's eye view (BEV) centered around the SDV. We then perform multi-class object detection with a shallow convolutional header to recognize the presence, BEV pose and dimensions of vehicles, pedestrians and bicyclists, and apply rotated RoI align to extract small feature crops from the scene context around each actor's location. Finally, an actor CNN with max-pooling reduces the feature map of each actor $n$ into a feature vector, $x_{n}^{local}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Joint Perception and Motion Forecasting", "weight": 1.0} -->

Since this local context lacks global information about the actor's pose with respect to the rest of the scene, we include the BEV centroid and rotation relative to the SDV $x_{n}^{global} = {\{ c_{x,n},c_{y,n},a_{n}\}}$ as additional features, obtaining the final actor context $x_{n} = {\lbrack x_{n}^{local},x_{n}^{global}\rbrack} \in {\mathbb{R}}^{D}$, where $\lbrack \cdot, \cdot \rbrack$ denotes channel-wise concatenation. We refer to the set of all the detected actors' contexts as $X = {\{ x_{1},x_{2},\ldots,x_{N}\}}$. The details about the LiDAR and map parameterization as well as the backbone network, object detector header, and actor CNN are left for the supplementary materials as they are not the focus of our work and are highly inspired by previous literature.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Joint Perception and Motion Forecasting", "weight": 1.0} -->

We parameterize the trajectory of each actor with a temporal series of the actor centroid in 2-dimensional Euclidean space, i.e., $y_{n} \in {\mathbb{R}}^{2T}$, where each trajectory is predicted in the actor's relative coordinate frame in Bird's Eye View (BEV) defined by its centroid and heading. Our latent variable model then characterizes the joint distribution over actors' trajectories as follows: where $Z = {\{ z_{1},z_{2},\ldots,z_{N}\}}$ is a set of continuous latent variables that capture latent scene dynamics, and Y$= {\{ y_{1},y_{2},\ldots,y_{N}\}}$ is the future trajectories of all actors. We assume a fixed prior ${p{(\left.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Joint Perception and Motion Forecasting", "weight": 1.0} -->

Z \middle| X \right.)}} \approx {p{(Z)}} = {\prod_{n = 1}^{N}{p{(z_{n})}}}$, where $z_{n} \sim {\mathcal{N}{(0,I)}} \in {\mathbb{R}}^{L}$. Following, we adopt an implicit^11^1"Implicit" means $p{(\left. Y \middle| {X,Z} \right.)}$ does not have analytical form. decoder $Y = {f_{\theta}{(X,Z)}}$, where $f_{\theta}$ is a deterministic function parameterized by a spatially-aware Graph Neural Network (GNN). Since from observational data we only obtain $(X,Y)$ pairs, a posterior or encoder function $q_{\phi}$ is introduced to approximate the true posterior distribution $p{(\left.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Joint Perception and Motion Forecasting", "weight": 1.0} -->

Z \middle| {X,Y} \right.)}$ during training, also parameterized by a GNN. This encoder function helps this model learn a powerful decoder, since given only $X$ there could be many feasible $Y$ due to the inherent multi-modality and uncertainty of the future.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Joint Perception and Motion Forecasting", "weight": 1.0} -->

The backbone network, detection header, actor CNN, encoder, and decoder are trained jointly for the tasks of object detection and motion forecasting. We use binary cross-entropy with hard negative mining per class for the presence of an actor, and Huber loss for the regression targets (i.e., pose and dimension). See the supplementary materials for more details. We use the CVAE framework for the latent variable model, which optimizes the evidence lower bound (ELBO) of the log-likelihood ${\log p}{(\left. Y \middle| X \right.)}$. Because the deterministic decoder leads to an implicit distribution over $Y$, we use Huber loss $\ell_{\delta}$ as the reconstruction loss, and reweight the KL term with $\beta$ as proposed: where the first term minimizes the reconstruction error between the trajectory samples $Y = \left. \{ y_{n}^{t} \middle| {{\forall n},t}\} \right.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Joint Perception and Motion Forecasting", "weight": 1.0} -->

So far we have learned a powerful model of the future from which we can generate scene consistent samples for all actors in the scene. In particular, inference in this model works as follows: First, we encode the sensor data into actor contexts $X$. Then, we sample $K$ times from the prior $\left. \{{Z_{k} \sim {p{(Z)}}} \middle| {\forall k}\} \right.$, and decode the scene latent samples deterministically in parallel to obtain each of the $K$ futures $\left. \{{Y_{k} = {f_{\theta}{(X,Z_{k})}}} \middle| {\forall k}\} \right.$. Despite the high expressivity of this model and its attractive parallel sampling, it has two major drawbacks: (i) sample inefficiency, and (ii) no closed-form likelihood.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Joint Perception and Motion Forecasting", "weight": 1.0} -->

In the following, we address (i) by learning to sample jointly a diverse set of latent codes that map into a covering distribution over trajectories and, (ii) by learning a categorical distribution over the diverse futures in the set.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Planning-Centric Diverse Sampler", "weight": 1.0} -->

The goal here is to remediate the sample inefficiency of the scene-level generative model presented in Section 3.1 while exploiting its expressivity. To do so, we learn a diverse sampling function $\mathcal{M}:{X\mapsto\mathbf{Z}}$ that maps the actor contexts $X$ coming from sensor data around each actor into a compact set of scene latent samples $\mathbf{Z} = {\{ Z_{1},\ldots,Z_{K}\}}$ whose decoded trajectories $\mathbf{Y}$ achieve good coverage. This sampler will then replace the Monte Carlo sampling from the prior distribution $p{(Z)}$ during inference, as illustrated in Fig. 3.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Planning-Centric Diverse Sampler", "weight": 1.0} -->

Since we want to leverage the decoder trained in Sec. 3.1, which was trained to decode samples from a Gaussian approximate posterior, we would like the distribution over the set of latents induced by the diverse sampler to also be a Gaussian in order to reduce the distributional shift. Thus, we assume ${p{(\left. \mathbf{Z} \middle| X \right.)}} = {\prod_{k = 1}^{K}{p{(\left. Z_{k} \middle| X \right.)}}}$ where ${p{(\left. Z_{k} \middle| X \right.)}} = {\mathcal{N}{(\mu_{k},\Sigma_{k})}}$, $\mu_{k} \in {\mathbb{R}}^{NL}$, and $\Sigma_{k} \in {\mathbb{R}}^{{{NL} \times N}L}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Planning-Centric Diverse Sampler", "weight": 1.0} -->

To handle the fact that the input $X \in {\mathbb{R}}^{ND}$ can vary in size (i.e. the number of actors $N$ varies from scene to scene), we parameterize $\mathcal{M}$ with a pair of GNNs: one to generate the means and another to generate the covariances. Both GNNs assume a fully connected graph where each node is anchored to an actor, and initialize the node states as $\{ x_{n}\}$. Then, we perform message passing to aggregate information over the whole scene at each node. Finally, each node in the first GNN predicts $a_{n} \in {\mathbb{R}}^{KL}$ via an MLP.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Planning-Centric Diverse Sampler", "weight": 1.0} -->

The diverse latent codes $\mathbf{Z}$ can then be deterministically decoded via $Y_{k} = {f_{\theta}{(X,Z_{k})}}$ with the decoder learned in Section 3.1. Through sampling and decoding, we obtain a set of $K$ future trajectory realizations of all actors in the scene $\mathbf{Y} = {\{ Y_{1},\ldots,Y_{K}\}}$. This process is parallel since it is performed by leveraging a pair of GNNs that perform all $K$ latent mapping in a single round of message passing $\mathbf{Z} \sim {\mathcal{M}{(X,\varepsilon;\eta)}}$. Then, we can batch the $K$ latent samples to decode them in parallel $\mathbf{Y} = {f_{\theta}{(\mathbf{Z},X)}}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Planning-Centric Diverse Sampler", "weight": 1.0} -->

The objective of this diverse sampler is to be able to generate a set of futures $\mathbf{Y}$ that are diverse while recovering well the ground-truth observations $Y_{\text{gt}}$, which we can express through an energy $E{(\mathbf{Y},Y_{\text{gt}})}$. Moreover, to encourage minimal distribution shift to the inputs of the pretrained decoder $f_{\theta}$, we also minimize the KL divergence between all the diverse latent distributions $p{({Z = \left. Z_{k} \middle| X \right.})}$ and the prior distribution $p{(Z)}$. In practice, this term makes the learning much more stable. To find the right balance between these two objectives, we add a hyperparameter $\beta$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Planning-Centric Diverse Sampler", "weight": 1.0} -->

Overall, the minimization can be formulated as: where $\mathbf{Y} = {\{ Y_{1},\ldots,Y_{K}\}}$, $Y_{k} = {f_{\theta}{(X,Z_{k})}}$, $Z_{k} = {\mathcal{M}_{\eta_{k}}{(X,\varepsilon)}}$ and the minimization is with respect to learnable parameters of the pair of GNNs $\eta$. Note that the decoder is fixed, i.e., $\theta$ is not optimized. This is key to maintain a high realism of the decoded trajectories, since the diversity objective can be otherwise cheated (e.g., by making other actors "appear" right in front of the SDV).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Planning-Centric Diverse Sampler", "weight": 1.0} -->

Our energy function is composed of a few terms that promote the diversity while preserving data reconstruction: We now define the energy terms in more details.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Planning Diversity Energy", "weight": 1.0} -->

We want to increase prediction diversity in order to anticipate distinct future scenarios that require different SDV plans (e.g., a vehicle cuts in front of the SDV vs. keeps driving on its original lane). Thus, we promote diverse samples that matter for the downstream task of motion planning by maximizing the following reward function: where $\tau_{i} = {\tau{(Y_{i})}}$ refers to the SDV trajectory planned for predicted scene sample $Y_{i}$ by our contingency motion planner outlined in Section 3.4. Since the optimal planned trajectory for each scene $\tau_{i}$ is not differentiable with respect to $Y_{i}$, we leverage the REINFORCE gradient estimator to express the energy $E_{p}$ as a function of the log-likelihood under the diverse sampler where ${{\log p}{(Z_{i},Z_{j})}} = {{{\log p}{(Z_{j})}} + {{\log p}{(Z_{i})}}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Planning Diversity Energy", "weight": 1.0} -->

The approximation comes from a Monte Carlo estimation of the marginalization over $\mathbf{Z}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "General Diversity Energy", "weight": 1.0} -->

Since the signal from the planning-based diversity can be sparse for scenes that do not have any actors interacting with the SDV, we additionally encourage diversity in the behaviors of all actors: With our proposed diverse sampler, each $\mathbf{Y}$ induced by a different noise $\varepsilon$ efficiently covers well the distribution over futures. Thus, during inference we can simply take the set induced by the mode $\varepsilon = 0$ to eliminate all randomness. We note that determinism is important in self-driving for safety, verification, and reproducibility.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Scenario Probability Estimation", "weight": 1.0} -->

The diverse set of $K$ future realizations $\mathbf{Y} = {\{ Y_{1},\ldots,Y_{K}\}}$ provides the coverage needed for safe motion planning. However, for accurate risk assessment we need to estimate the probability distribution over each future realization in the set. To achieve this goal, we augment our model to also output a score for all future realizations $l = {s_{\psi}{(X,\mathbf{Y})}}$, where $s_{\psi}$ is a GNN that takes as input the actor features and all $K$ sample future scenarios. We can then easily recover a distribution over such scores by re-normalization. Thus, the probability of each sample is Since we only have access to a single ground truth realization (i.e., the one that occur in the training log), we train the scoring function $s_{\psi}$ to match the approximate categorical distribution over future scenarios $q{(\left.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Scenario Probability Estimation", "weight": 1.0} -->

Y_{k} \middle| X \right.)}$ under the $\text{KL}{({p_{\psi} \parallel q})}$ divergence. We define this approximate distribution as follows: where $\alpha = 10$ is a temperature hyperparameter we chose empirically.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Contingency Planner", "weight": 1.0} -->

The goal of the motion planning module is to generate safe, comfortable and not overly conservative trajectories for the SDV to execute. We achieve this through Model Predictive Control, where a trajectory is planned considering a finite horizon, and is executed until a new trajectory is replanned upon availability of a new LiDAR sweep. Most planning frameworks in the literature take an optimization-based approach where the trajectory that minimizes the expected cost is selected for execution: where $\mathcal{T}_{0:T}{(\text{x}_{0})}$ denotes the set of possible trajectories starting from SDV state $\text{x}_{0}$ up to the horizon $T$, and $c$ denotes the planner cost function. Note that the expectation is over the distribution of possible future realizations of all actors $P{(Y)}$. However, the above formulation does not exploit the fact that only one of the predicted scenarios will happen in the future and is conversely optimizing for a single trajectory that is "good" in expectation.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Contingency Planner", "weight": 1.0} -->

Note that if we change the expectation in Eq. 12 to the max operator, the planner will optimize for the worst-case scenario regardless of its likelihood. Consequently the planner will become over-conservative, e.g., it will apply a hard-break for a very low probability scenario where a vehicle crosses SDV lane, as shown.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Contingency Planner", "weight": 1.0} -->

In this paper, we take a different approach where instead of finding a single motion plan for multiple futures, we generate a single common immediate action, followed by a set of future trajectories, one for each future realization of the scene, as shown in Fig. 4. This contingency planning paradigm finds an immediate action $\tau_{0:t}$ that is safe with respect to all the possible realizations in $Y$ and comfortably bridges into a set of contingent trajectories, where each is specifically planned for a single future realization. Such decision-postponing avoids over-conservative behaviors while staying safe until more information is obtained. Importantly, the described safe motion planning is only possible if the set of predicted future scenarios is diverse, and covers possible realizations, including low likelihood events.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Contingency Planner", "weight": 1.0} -->

Specifically, we plan a short-term trajectory that is safe with respect to all possible futures and allows a proper contingent plan for each future realization: where ${g{(\text{x},Y)}} = {{\min_{\tau_{t:T} \in {\mathcal{T}_{t:T}{(\text{x})}}}c}{(\tau_{t:T},Y)}}$ represents the minimum cost trajectory from time $t$ to $T$ starting from the state x and assuming a single future realization $Y$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Cost Function", "weight": 1.0} -->

The planner cost function ${c{( \cdot )}} = {\sum_{i}{w_{i}s_{i}{( \cdot )}}}$ is a linear combination of various carefully crafted subcosts $s_{i}$ that encode different aspects of driving including safety, comfort, traffic-rules and the route. Here, $w = \left. \{ w_{i} \middle| {\forall i}\} \right.$ is a set of learnable parameters. However, learning these parameters in the contingency planning paradigm (Eq. 13) is an open problem since we only have expert demonstrations for the future that occured at the time of the log. Thus, we leave this for future work, and leverage the weights learned through Eq. 12. Regarding the subcosts, collision and safety-distance subcosts penalize SDV trajectories that overlap with the predicted trajectories of other actors or have high speed in close distance to them. Similarly, trajectories that violate a headway buffer to the lead vehicle are penalized.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Cost Function", "weight": 1.0} -->

Other subcosts promote driving within the lane and road boundaries, and penalize trajectories that go above speed-limit or violate a red-traffic light. Finally, motion jerk, high forward acceleration, deceleration, and lateral acceleration of the trajectories are penalized to promote comfortable maneuvers. The details of all the subcosts can be found in the supplementary materials.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Inference", "weight": 1.0} -->

We take a sampling approach to solve the minimization in Eq. 13. Specifically, we generate a set of pairs $\{{(\tau_{0:t},{\mathcal{T}_{t:T}{(\tau_{t})}})}\}$, which include possible short-term trajectories $\tau_{0:t}$ and their possible subsequent set of trajectories $\mathcal{T}_{t:T}{(\tau_{t})})$. It is important to consider a dense set of initial actions such that the final executed trajectory is smooth and comfortable. Similarly, a dense set of long-term trajectories enables the planner to find a proper contingent plan for the future and thus obtain a more accurate cost-to-go for the initial action.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Inference", "weight": 1.0} -->

In order to manage the complexity of the search space above, we take the following sampling strategy: (i) first a set of (spatial) paths are generated, (ii) for each path, a set of initial velocity profiles are sampled, creating the set of short-term trajectories, (iii) conditioned on the end state of these initial trajectories, another set of velocity profiles are sampled for the rest of the planning horizon assuming the SDV follows the same path. In total, the sample set contains $\approx$ 240 actions and for each action there are $\approx$ 260 long-term trajectories. The above path and velocity generation are done in Frenet-frame of the desired lane center line, by sampling lateral and longitudinal profiles. For more details see the supplementary materials.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section we describe our experimental setup, followed by the results and discussions.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Dataset", "weight": 1.0} -->

ATG4D is composed of over one million frames of LiDAR, HD maps with very accurate object tracks. It was collected with careful expert drivers in several North American cities. All models are trained to predict 5-second trajectories, given 1 second of LiDAR history. We evaluate motion forecasting in the test set of this dataset.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Closed-loop simulator", "weight": 1.0} -->

We use a simulated LiDAR environment for closed-loop experiments where we evaluate the quality of our end-to-end driving model, recreated from real static environments and actors. These scenarios are curated from real driving logs to be particularly challenging, and they do not overlap with those in ATG4D in order to evaluate generalization. When replaying the scenario, the actors switch to reactive actors if the scenario diverges from the original one due to SDV actions. The simulation is unrolled for $\sim$`<!-- -->`{=html}18 seconds at intervals of 100 milliseconds, which is the same time it takes to acquire a new LiDAR sweep in the data collection vehicle. We note that all training happens on real offline data, but it transfers well to the simulated environment due to its high realism.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Baselines", "weight": 1.0} -->

For motion forecasting, we use state-of-the-art baselines in multi-modal and diverse prediction, all of them trained end-to-end with the same backbone network and object detector architectures for a fair comparison, following the experimental setup. MultiPath, CVAE, CVAE-DPP and CVAE-DLow model the distribution over each actor's future trajectories independently. Thus, to construct a scene sample for these baselines we sample a random trajectory for each actor, following. For approaches that model the joint distribution over all actors' future trajectories, we benchmark against ESP and ILVM. To compare LookOut to the baselines in the motion planning task, we use the state-of-the-art PLT planner (Eq. 12) for those motion forecasting models that did not propose a planner.

<!-- chunk {"id": "body-0045", "role": "body", "section": "End-to-end driving metrics (closed-loop)", "weight": 1.0} -->

We measure the collision rate (CR) to reflect the driving safety. This is the percentage of simulations in which there is at least 1 collision between the SDV and another actor. We also evaluate the progress made by the SDV on its desired route throughout the simulation horizon, measured in meters from the starting location, as well as the progress per collision, giving an idea of the ratio between non-conservativeness and safety. Finally, we measure the mean jerk and acceleration applied as a metric of the driving comfort. As the autonomy unrolls its own actions for long time periods, potentially diverging from the path the expert-driver executed, these metrics capture the quality of the end-to-end system, including its robustness to distributional shift.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Sub-system level metrics (open-loop)", "weight": 1.0} -->

In the open-loop evaluations, our model is evaluated on real data from the logs in the ATG4D dataset (i.e., the scenes visited by the expert driver), as opposed to closed-loop evaluations where we unroll our own plans. To evaluate the object detection quality we measure the standard mean-average precision (mAP), but defer the results to the supplementary because all the models share the same perception backbone architecture, and it is not the focus of this paper. To measure the reconstruction capability and the diversity of the scene-level motion forecasts, we use $K = 15$ scene samples, meaning that there are 15 distinct future scenarios predicted, each with 1 trajectory per actor. The minimum scene average displacement error (minSADE) measures how well we recall the ground-truth trajectory, while the mean scene average displacement error (meanSADE) measures the precision of the predicted distribution as proposed. To evaluate how the diversity of these predictions impact the subsequent contingent plans, we measure the pairwise plan average self-distance (meanPlanASD), i.e., the average distance between the contingent plans for 2 distinct futures.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Sub-system level metrics (open-loop)", "weight": 1.0} -->

Additionally, we also compute the scene average self-distance (meanSASD), which computes the average pairwise distance among scene samples as a way to measure general diversity as proposed.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Planning benchmark", "weight": 1.0} -->

The closed-loop experiment results for motion planning are shown in Table 1. LookOut outperforms the baselines in almost all metrics. In particular, we see a 21% increase in progress per collision to the next best baseline for this metric, CVAE + PLT. This is a combination of having 8% fewer collisions in addition to 12% greater progress, showing our model is able to avoid dangerous scenarios on the road without slowing down (i.e., it provides additional safety while being less conservative). For completeness, the results of the baselines paired with our contingency planner are available in the supplementary.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Diversity tradeoffs", "weight": 1.0} -->

The open-loop experiment results are shown in Fig. 5. LookOut achieves the safest plans, makes the most progress, and achieves the best prediction reconstruction while being among the most diverse methods. In the baselines, we see how more diversity often makes the plans more unsafe, diminishes the progress throughout the route, and regresses the reconstruction quality of the motion forecasts. In contrast, our method escapes this "diversity curse". Importantly, the predictions given to our contingency planner are very accurate and diverse at the same time. This allows our model to make cautious, safe plans without the shortcomings of too much irrelevant or excessively variant predictions. Here, the baselines use the PLT planner, but we include the same plots with the contingency planner in the supplementary materials.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Table 2 shows the impact of our main contributions.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Diverse sampler vs. Monte Carlo sampling", "weight": 1.0} -->

$M_{1}$ samples independently from the the prior $p{(Z)}$. We can see that when using LookOut's diverse sampler we achieve almost the same comfort and progress, while being able to anticipate and avoid significantly more collisions.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Planning diversity energy", "weight": 1.0} -->

$M_{2}$ shows that the planning diversity energy is critical for increasing the driving safety (28% lower collision rate). We also observe an improvement in jerk and a regression in lateral acceleration. We hypothesize that this energy term favors early and preventive lateral displacements instead of late hard brakes from the planner. Further investigation is left for future work.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Scenario scoring vs. uniform probabilities", "weight": 1.0} -->

$M_{3}$ removes the scenario scoring, assigning each diverse scenario an equal probability as input to the planner. We can see that scenario scoring improves safety and progress, showing us that it prevents the SDV from unnecessary premature braking to avoid low-probability risks.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Contingency planner vs. PLT", "weight": 1.0} -->

The ablation $M_{4}$ demonstrates the importance of the contingency planner as it improves almost every metric when compared to the PLT planner, notably reducing collisions by 38%.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have proposed a prediction and planning model that generates more diverse motion forecasts and safer trajectories for the SDV. Our prediction model learns to generate multimodal trajectory samples from a joint distribution over actor trajectories. Unlike previous diverse forecasting approaches, we directly optimize for predicting rare behavior that could impact the SDV, and estimate the probability distribution over these samples for more accurate risk assessment. Our contingency planner improves the decision making over these diverse samples. Our experiments on closed-loop simulations and a large-scale dataset demonstrate that our model drives safer and less conservatively than previous state-of-the-art models.
