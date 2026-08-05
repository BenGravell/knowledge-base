<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

DriveIRL: Driving in Real Life with Inverse Reinforcement Learning

Topics include Autonomous driving, Inverse reinforcement learning, Motion planning, Imitation learning, Real-world deployment.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Inverse Reinforcement Learning-based planner demonstrated on a real self-driving car in dense urban traffic. Trained on large-scale human driving logs. The architecture design is critical to the success of the approach: there is a classical trajectory generator (based on Dubins paths, pre-computed acceleration profiles, and access to a clean road geometry model) capable of generating diverse safe trajectories, a safety filter that removes all trajectory candidates that are not forward recursively safe, and the learned model is only for assigning scores to the safety-filtered trajectory candidates. Includes a useful set of standardized evaluation metrics for learned planners (see Appendix A.5).

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we introduce the first published planner to drive a car in dense, urban traffic using Inverse Reinforcement Learning (IRL). Our planner, DriveIRL, generates a diverse set of trajectory proposals and scores them with a learned model. The best trajectory is tracked by our self-driving vehicle's low-level controller. We train our trajectory scoring model on a 500+ hour real-world dataset of expert driving demonstrations in Las Vegas within the maximum entropy IRL framework. DriveIRL's benefits include: a simple design due to only learning the trajectory scoring function, a flexible and relatively interpretable feature engineering approach, and strong real-world performance. We validated DriveIRL on the Las Vegas Strip and demonstrated fully autonomous driving in heavy traffic, including scenarios involving cut-ins, abrupt braking by the lead vehicle, and hotel pickup/dropoff zones. Our dataset, a part of nuPlan, has been released to the public to help further research in this area.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Self-driving cars have been the focus of significant research and development over the past decade. Some companies are tantalizingly close to deploying commercial self-driving taxi services that would make urban transportation cheaper and safer. Progress in self-driving cars has been largely driven by new datasets[nuscenes2019,sun2020waymo-open-dataset,chang2019argoverse,geiger2012kitti] that helped fuel dramatic improvements in machine learning approaches to object detection [zhou2018voxelnet,lang2019pointpillars] and motion forecasting [cui2019multimodal,chai2019multipath,phan2020covernet]. However, the critical motion planning and decision-making algorithms that ultimately determine driving behavior have yet to see similar benefits from machine learning.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Classical planning and decision-making algorithms for self-driving cars rely heavily on hand-engineered components Developers will typically hand-tune the scoring function that determines which behaviors are desirable. Manually adjusting features and weights can be a painstaking process improving performance in one area often causes unintended regressions elsewhere. Our planner avoids the need to manually craft detailed features or tune weights by learning these components from expert demonstrations using a maximum entropy IRL framework.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our DriveIRL system works by generating, checking, and scoring trajectories for our vehicle. We use simple and interpretable modules to do the relatively easy tasks of generating a diverse set of ego trajectories and checking that they are safe. Careful construction of the proposed trajectories ensures that they a) are dynamically feasible, b) follow the route, c) satisfy assumptions from the vehicle controller, and d) are diverse. We then apply a lightweight safety filter that ensures that each trajectory satisfies a recursive safety guarantee: if we execute the first part of the trajectory, there exists a safe continuation of that trajectory which avoids collision. The learning component of our model focuses entirely on appropriately scoring these trajectories based on the expert demonstrations. Our design directs the model capacity towards hard-to-specify nuances in behavior (e.g., speed profiles, clearances) instead of also creating nicetrajectories and avoiding obviously unsafe behavior.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

DriveIRL achieves strong real-world driving performance on the Las Vegas Strip. The Strip is a major thoroughfare in Las Vegas which connects many of the major hotels and casinos. Challenges include dense traffic, aggressive cut-ins, erratic drivers, and busy passenger pickup/dropoff zones near the hotels. We deployed DriveIRL on a self-driving car and drove fully autonomously on the Strip in these scenarios, showing the practical utility of our approach.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

- The first learning-based planner to drive a car in dense, urban traffic using IRL. - A simple yet powerful modeling framework that focuses learning on the aspect of driving that is most challenging to specify. - Detailed evaluation of our planner on a real-world dataset that we will make public.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

DriveIRL architecture. The learned scoring component is indicated with a dotted boundary.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Inverse Reinforcement Learning Planner", "weight": 1.0} -->

In this section, we describe our Inverse Reinforcement Learning (IRL) Planner as shown in Fig.[fig:model]. Our system consists of three main stages: trajectory generation (Sec.[subsec:traj-gen]), safety filtering (Sec.[subsec:safety-filter]), and trajectory scoring (Sec.[subsec:traj-score]). We rely on simple and reliable hand-engineered modules for trajectory generation and safety, and focus on learning how to score trajectories.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Input and output", "weight": 1.0} -->

We encode the environment (or scene) around our self-driving car using a mid-level representation. We assume that the ego is localized within a high-definition map and that objects are detected and tracked by a Perception system. Other road users (e.g., cars, bicyclists, and pedestrians) are represented by object type, an oriented bounding box, and speed. The high-definition map provides lane center-lines, road boundaries, traffic light locations, pedestrian crosswalks, speed limits, and other semantic information. We also provide a route, which indicates the lanes that the ego should traverse to make progress towards its goal. scene context at a given timestamp as a) the ego dynamic state $\mathcal{S}$ (speed, acceleration, steering), b) the other road users $\mathcal{U}$ (type, oriented bounding box, speed), c) the map $\mathcal{M}$, and d) the ego's desired route $\mathcal{R}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Input and output", "weight": 1.0} -->

The model receives the scene context at the current timestamp as well as a specified number of previous timestamps (e.g., the past 1 second) as history $\mathcal{H}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Input and output", "weight": 1.0} -->

Our planner generates multiple ego trajectories and scores each one according to how closely it matches what an expert would do given the scene context. A trajectory is a discrete sequence of future states of the ego, where we assume that there is a fixed timestep between all states. Let $s_t = (x, y, \theta, v)$ represent a state at time $t$, with position ($x$, $y$), heading $\theta$, and speed $v$. All values are with respect to the ego's geometric center in a fixed coordinate frame. The trajectory $\tau = [s_1, \ldots, s_T]$, where $T$ is the planned time horizon, that is ranked the best among a set of trajectories $\mathcal{T}$, is used as a reference for the vehicle's tracking and actuator controller.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Trajectory generation", "weight": 1.0} -->

The trajectory generation module uses the scene context to synthesize a diverse set of possible future motions for the ego. Important considerations for the ego's trajectory are that it a) is dynamically feasible, and b) satisfies all requirements of the low-level tracking and actuator control (i.e., levels of continuity, minimum turn radius, minimum acceleration from a stop). Secondary considerations are that the trajectory is compliant with the map (e.g., it stays on the road). While these considerations do not preclude using a learned trajectory generation module, we found that a hand-engineered trajectory generator best satisfied the considerations above.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Trajectory generation", "weight": 1.0} -->

The trajectory generator uses i) the current ego state $\mathcal{S}$, ii) the route $\mathcal{R}$, and iii) the map $\mathcal{M}$ to create a diverse set of ego trajectories $\mathcal{T}$, namely $\mathcal{(S, R, M)}\mapsto \mathcal{T}$. The generator integrates a desired acceleration profile along the route ahead of the ego. In our experiments, we specified a range of constant acceleration profiles ranging from a hard brake ($\SI{-5.0}{\meter \per \second^2}$) to a moderate acceleration ($\SI{1.5}{\meter \per \second^2}$). As the ego will not always be on the lane center-line (due to vehicle controller tracking errors), we smoothly connect the initial ego pose with the route with Dubins paths[lavalle2006planning-algos] where turning radii are a fixed set of parameters.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Trajectory generation", "weight": 1.0} -->

In a typical scene, the trajectory generator usually creates $50$-$150$ trajectories depending on the ego state and route. Some examples are shown in the Fig [fig:trajecotry\_set]. Appendix[app:trajectory-quality]provides results to validate that the generated trajectories are of good quality.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Trajectory generation", "weight": 1.0} -->

Proposed trajectories for the ego (red rectangle). Each trajectory is shown in translucent white dot-line. Overlap is due to multiple acceleration profiles. All trajectories return to the route.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Safety filter", "weight": 1.0} -->

Safety filter. Left: toy scenario with three trajectories (ego is in red, vehicle ahead is in yellow). Middle: modified trajectories. Right: unsafe trajectories excluded from trajectory set.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Safety filter", "weight": 1.0} -->

Before scoring candidate trajectories, we apply an interpretable safety filter (Fig [fig:safety-filter]) to guarantee basic safety (i.e., no collisions).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Safety filter", "weight": 1.0} -->

- a set of world assumptions used to predict the behavior of the non-ego road users, - a set of trajectory modifiers which are applied to the ego trajectory, and - a set of safety checks which the modified ego trajectory needs to pass.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Safety filter", "weight": 1.0} -->

For a candidate trajectory to be considered safe, it must pass all safety checks, under the given trajectory modifications and assumptions about the other road users. [app:safety-filter-details]for details.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Safety filter", "weight": 1.0} -->

Our safety filter is similar in spirit to the fallback layer proposed by [vitelli2021safety-net], except that 1) it directly filters the proposed trajectories, rather than projecting the output trajectory to an ad-hoc trajectory set, and 2) the trajectory modifier effectively implements a recursive safety guarantee with minimal assumptions and checks, without compromising comfort.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Trajectory scoring with maximum entropy IRL", "weight": 1.0} -->

Appropriately scoring trajectories is the core challenge of our planning approach. This difficulty is because proper driving behavior is heavily influenced by the environment around us, including other road user behavior and goals, of which we only have a partial understanding.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Trajectory scoring with maximum entropy IRL", "weight": 1.0} -->

Trajectories are scored by a deep neural network trained with a maximum entropy IRL loss We use expert demonstrations collected from a skilled human driving our vehicle. The loss favors trajectories that most closely match the expert demonstration $\tau^{\star}$ in feature space. In particular, let $r(\tau)$ represent the reward of the trajectory $\tau \in \mathcal{T}$, the probability of a trajectory $\tau^{\ast}$ being selected according to the maximum entropy principle is $P(\tau^{\star}) = \frac{\exp{r(\tau^{\star})}}{\sum\limits_{\tau} \exp{r(\tau)}}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Trajectory scoring with maximum entropy IRL", "weight": 1.0} -->

The negative log-likelihood loss (NLL) on a dataset $\ell(D) = -\sum\limits_{d \in D}{\log{P(\tau^{\star}(d))}}$ where $\tau^{\star}(d)$ is the demonstrated trajectory on the token $d \in D$. To address data imbalance issues, we augment NLL with focal loss[lin2017focal] (with a $\gamma$ of $2.0$) $$\ell(D) = -\sum\limits_{d \in D}{(1-P(\tau^{\star}(d)))^{\gamma}\log{P(\tau^{\star}(d))}}.$$ We compute features for each proposed trajectory to use as inputs to our neural network.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Trajectory scoring with maximum entropy IRL", "weight": 1.0} -->

These features can be based on any combination of a proposed trajectory $\tau$, ego state $\mathcal{S}$, other road users $\mathcal{U}$, the map $\mathcal{M}$, route $\mathcal{R}$, and history $\mathcal{H}$, meaning that $F_i: (\tau, \mathcal{S}, \mathcal{U}, \mathcal{M}, \mathcal{R}, \mathcal{H}) \mapsto f_i \in \mathbb{R}^{k_{i}}$, where $F_i$ is the feature extraction function corresponding to feature $i$ and $k_i$is its dimension.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Trajectory scoring with maximum entropy IRL", "weight": 1.0} -->

- Time-to-collision (TTC): the minimum number of seconds before the ego would collide with another road user in the (predicted) future. Evaluated at multiple points. - ACCInfo: the ego speed, the distance to the road user ahead, the speed of the road user ahead, and the relative speed of the road user ahead. Evaluated at multiple points. - MaxJerk: the maximum jerk ($\SI{}{\meter \per \second^3}$) along the trajectory. - MaxLateralAccel: the max lateral acceleration ($\SI{}{\meter \per \second^2}$) along the trajectory. - PastCoupling: concatenation of the future trajectory and the one second of past ego poses to model learn to maintain the coherence between the past, present, and future trajectories. - SpeedLimit: how closely the trajectory obeys the speed limit. Evaluated at multiple points.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Trajectory scoring with maximum entropy IRL", "weight": 1.0} -->

More implementation details can be found in the Appendix Some of the features computed for each proposed trajectory require an estimate of where other road users will be in the future, such as Time-to-collision (TTC) and ACCInfo. We use an Intelligent Driver Model (IDM)[treiber2000congested-idm]as our prediction model for other cars, with a conservative acceleration value to avoid assuming that stationary vehicles will speed up. We use a constant velocity model for pedestrians and for vehicles without a nearby lane.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Trajectory scoring with maximum entropy IRL", "weight": 1.0} -->

To score a trajectory, we adopt an architecture in which the extracted features are processed separately before interacting with one another through a masked self-attention mechanism.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Trajectory scoring with maximum entropy IRL", "weight": 1.0} -->

Under this architecture, each input feature $f_i$, as a temporal sequence of related vehicle-environment interaction data, is first normalized through an application of a BatchNorm1D layer before being fed to an LSTM module with one layer and a hidden size of $20$. The output of the LSTM becomes the input to a feed-forward module and then a self-attention mechanism with two heads and an embedding dimension of $120$. Here we employ zero-masking of the queries to encode position. By taking into account other features through self-attention, the model produces for each feature a corrected output embedding that can now be passed to a feed-forward network which converts it into a scalar and then a $\tanh$ activation to produce a feature score $y_i$. The final score for the trajectory is the sum of these feature scores after they are multiplied by the corresponding learnable feature weight parameters $w_i$: $r(\tau) = \sum\limits_{i} w_i y_i$. In total, our base (best) model has $\approx88,700$trainable parameters.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

The proposed inverse reinforcement leaning planner was evaluated on a large-scale dataset and the results are presented in the following. The dataset we used is described in Sec [subsec:dataset]. The metrics for comparison is explained in Sec [subsec:metrics]. Various model ablation studies and the comparison with baseline are shown in Sec [subsec:model-ablations] and [subsec:baseline]. We demonstrated both simulation results and the real-world driving tests in Sec [subsec:sim-result] and [subsec:realworld-driving]respectively.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Dataset", "weight": 1.0} -->

We created a self-driving car dataset that captures real-world urban driving in the center of Las Vegas. Our dataset is a part of the nuPlan[caesar2021nuplan] dataset that will be made public. It includes object annotations and high-definition maps. Vehicles, pedestrians, and bicyclists are automatically annotated using an offline perception system (similar in spirit to [qi2021offboard-auto-label]) and viewed as ground truth. We performed filtering and extracted 182,032 scenarios, each 11 seconds in duration (1 second past, 10 seconds future), for a total of approximately 556 hours. Our main interest was to learn good adaptive cruise control (ACC) behavior. Thus, we filtered out scenarios where the ego made lane changes or deviated far from the lane. After filtering, we performed a 3:1:1 split for train, val, and test sets. Tab.[tab:dataset-distribution] shows a detailed distribution of our dataset by scenario tags. The tags in the table are not mutually exclusive and a scenario can belong to multiple tags.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Dataset", "weight": 1.0} -->

More detailed definitions for the scenario tags are in Appendix[app:scenario\_tags].

<!-- chunk {"id": "body-0034", "role": "body", "section": "Dataset", "weight": 1.0} -->

A detailed distribution of our dataset ($182,032$ total $11$-second scenarios).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Dataset", "weight": 1.0} -->

| Tags | Straight | Right | Left | Stopped | Slow | Intersection | Close | ASV |

<!-- chunk {"id": "body-0036", "role": "body", "section": "Metrics", "weight": 1.0} -->

We evaluate our model using a variety of metrics to give a full picture of driving. To approximate real-world conditions, we perform a closed-loop replay for each scenario for a duration of 10 seconds. We initialize the ego at the start of the scene, compute a planned trajectory, move along that trajectory for one step, replay the other agents, and repeat. Then, we compute metrics on the resulting executed trajectory as averages over the full scene duration.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Metrics", "weight": 1.0} -->

Evaluation was done with a time step size of $0.2$ seconds and a total duration of $10$ seconds. The model was given $1$second of ground truth past prior to the start of the scene. Other road users were updated by replaying their positions from the database.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Metrics", "weight": 1.0} -->

We have four high level categories of metrics that contain low level metrics and high level summary metrics that act as a score for the category. The categories for our metrics are Safety, Comfort, Progress, and $\ell_2$ (with a yaw penalty of $2.5$). Further details about our metric categories and the low level computations that make them up can be found in Appendix[app:metricbreakdown].

<!-- chunk {"id": "body-0039", "role": "body", "section": "Metrics", "weight": 1.0} -->

Currently, there are two major limitations to our metrics evaluation.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Metrics", "weight": 1.0} -->

The use of replay for other agents. Since other vehicles do not react to the ego (e.g., if we drive slower than the expert in the data), the overall Safetyscore is a lower bound on safety.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Metrics", "weight": 1.0} -->

No controller or vehicle dynamic simulation for the Ego. We currently teleport the ego along its trajectory, causing jerk to be erroneously high in some cases. Similar to safety, this makes our Comfortscore a lower bound on what we actually observe in real world driving.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Model ablations", "weight": 1.0} -->

In our experiments, we use a batch size of $64$ and an Adam optimizer with an initial learning rate of $10^{-3}$. Additionally, we use a cosine annealing with warm restarts scheduler, which gradually lowers the learning rate to a minimum of $10^{-4}$ and resets it every seven epochs. All models are trained over 20 epochs on eight AWS g4dn-metal instances with eight 16 GB NVIDIA Tesla T4 GPUs each. Because closed-loop simulation is computationally expensive, we randomly sampled $1,000$ scenarios from our evaluation set for ablation studies and $3,000$scenarios from the test set for the final performance evaluation against other baselines. Training and closed-loop metrics evaluation takes about an hour per epoch.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Model ablations", "weight": 1.0} -->

To understand the importance of each hand-engineered feature and the main contribution of each, an ablation study for features is conducted and summarized in Tab.[tab:feature-importance]. The relative importance of each feature is shown by dropping one of them out at a time. We claim that all the features are important because the Base model which includes all features got the highest scores across all high-level metrics and had lowest Collision rate. Even though the $\ell_2$ error is a bit higher compared to No MaxJerk, the $0.089$ $m$ difference is not significant in the qualitative results. The results also demonstrated the importance of PastCoupling feature in ensuring Comfort. The experiment also showed that TTCfeature contributes significantly to reducing the collision rate.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Model ablations", "weight": 1.0} -->

Ablation study on the importance of each feature. The row indicates the feature removed from the baseline model. See Sec.subsec:traj-score for definitions.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Model ablations", "weight": 1.0} -->

| Model | Safety | Comfort | Progress | $\ell_2$ (w/ yaw) | Collision | Tailgate | Data augmentation is important to ensure that our model can learn how to recover from errors. Since the reference trajectory is never followed perfectly by the vehicle, errors can accumulate. We perturb the ego's initial state during training to reduce the sensitivity to such errors. For our low noise baseline, we use zero-mean Gaussian data augmentation for longitudinal offset ($\SI{1.2}{\meter}$ std), lateral offset ($\SI{0.8}{\meter}$ std), heading offset ($\SI{0.1}{\radian}$ std), and velocity ($\SI{0.1}{\meter \per \second}$ std).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Model ablations", "weight": 1.0} -->

For the high noise ablation, we respectively use $\SI{2.5}{\meter}$ std, $\SI{1.5}{\meter}$ std, $\SI{0.3}{\radian}$ std, and $\SI{0.2}{\meter \per \second}$ std. We clamp velocity to avoid negative values. Several example images are shown in [section:da].

<!-- chunk {"id": "body-0047", "role": "body", "section": "Model ablations", "weight": 1.0} -->

Comparison between different augmentation schemes.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Model ablations", "weight": 1.0} -->

| Model | Safety | Comfort | Progress | $\ell_2$ (w/ yaw) | Collision | Tailgate | We perform several ablations on the model architecture before selecting an architecture in which the extracted features are processed separately before interacting with one another through a masked self-attention mechanism. We show in Tab.[tab:model-architecture]that the other two extremes, namely, concatenating all input features and using them as one monolithic feature in a single feedforward network or siloing all input features (not allowing any interaction through attention or otherwise) have resulted in inferior performance. It is also seen that input normalization and attention input masking are beneficial.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Model ablations", "weight": 1.0} -->

Comparison between different model architectures.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Model ablations", "weight": 1.0} -->

| Model | Safety | Comfort | Progress | $\ell_2$ (w/ yaw) | Collision | Tailgate | Tab.[tab:loss-function] shows that it is better to maximize the probability the projection of the ground truth onto the trajectory set (the best approximation in average $\ell_2$ norm) instead of the ground truth itself. This makes sense because the ground truth does not come from the same distribution as the proposals and is not available at inference time. Filtering possibly unsafe trajectories from the set before finding the ground truth projection is also crucial to obtaining a safe model. Doing the projection using the average $\ell_2$ norm instead of an $\ell_2$ norm with a yaw error penalty also seems favorable. Lastly from the same table, we can see that using focal loss as in Equation[eq:loss-function] improves performance. Another experiment in Appendix[app:data\_curation]that compares focal loss against training on a better balanced dataset also shows that using focal loss is actually more effective for DriveIRL.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Model ablations", "weight": 1.0} -->

Comparison between different loss functions.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Model ablations", "weight": 1.0} -->

| Metric | Safety | Comfort | Progress | $\ell_2$ (w/ yaw) | Collision | Tailgate |

<!-- chunk {"id": "body-0053", "role": "body", "section": "Baselines", "weight": 1.0} -->

In this section, we evaluate our model on a test dataset and compare it with an Intelligent Driver Model (IDM) [treiber2000congested-idm] and a constant speed (CS) lane follow model. The IDM baseline is a reasonable choice because it is a well-known version of an expert planner that focuses on adaptive cruise control. Meanwhile, the CS lane follow model is a simple lower-bound. The results are shown in Tab.[tab:baselines]. Our base model plus safety filter outperforms others in all safety related metrics, and that shows the safety filter protects the vehicle on several collision cases our model cannot handle perfectly. Without the safety filter, our base model still outperforms the IDM baseline. The IDM model has significantly higher $\ell_2$error, indicating that the IDM model does not drive like a human expert. Furthermore, our base model also has higher scores in all safety related metrics in both high- and low-level scores like collision rate and tailgate rate.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Baselines", "weight": 1.0} -->

Baselines on the test set. IDM = Intelligent Driver Model. CS = constant speed.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Baselines", "weight": 1.0} -->

| Metric | Safety | Comfort | Progress | $\ell_2$ (w/ yaw) | Collision | Tailgate |

<!-- chunk {"id": "body-0056", "role": "body", "section": "Simulation results", "weight": 1.0} -->

Fig.[fig:sim-scenarios] exhibits some qualitative closed-loop simulation results of our planner driving in typical scenarios. These scenarios are shown as a sequence of snapshots along the closed-loop rollout. The ego vehicle is shown as a red rectangle, the expert vehicle is in blue, and other vehicles are in yellow. The orange line is the planned route (along the lane centerline) and the purple circles represent the planned trajectory for the next $6$ seconds. Our planner shows good performance over a range of scenarios, exhibiting reasonable and consistent behavior over $10$second rollouts. [Ego starting from a stop.] [Ego stopping for the lead vehicle.] [Adaptive cruise control.]

<!-- chunk {"id": "body-0057", "role": "body", "section": "Simulation results", "weight": 1.0} -->

Qualitative driving performance in common scenarios. Full-size images are inapp:simulation\_videos.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Real-world driving", "weight": 1.0} -->

Prior to deploying on public roads, DriveIRL was rigorously tested in both simulation and on private, closed-course routes. The simulation tests consist of the same Las Vegas Strip route that was our deployment goal, and involve a high-fidelity dynamics model for the ego vehicle and numerous actors exhibiting a wide variety of behaviors. When deployed on the Strip, the vehicle was piloted by a vehicle operator who was trained to take over for unsafe behavior and situations outside of our operating domain, including construction zones, bus stops, and yielding for emergency vehicles.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Real-world driving", "weight": 1.0} -->

On the Strip, our planner handled challenging scenarios such as heavy traffic, aggressive cut-ins, unpredictable drivers, and busy passenger pick-up/drop-off zones near the hotels and casinos. Without the safety filter, the vehicle remained in autonomous mode for 8.8 miles of the 11-mile route. Overrides occurred for mandatory takeover regions and twice for undesired behavior. With the safety filter, the vehicle remained in autonomous mode for 6.9 of 8.5 miles, with takeovers only occurring due to mandatory takeover regions.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Real-world driving", "weight": 1.0} -->

Smoothly stopping behind a vehicle in dense traffic on the Las Vegas Strip. [fig:stopping-02] shows a typical maneuver where our self-driving vehicle smoothly stops for a vehicle ahead while surrounded by multiple vehicles. In Sec.[app:real-clips], we have included video clips with more real-world driving maneuvers. These videos are grouped in categories such as cut-ins, driving around passenger pickup/dropoff zones, driving with a vehicle ahead and stopping behind a vehicle.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We introduced DriveIRL: the first learning-based planner to control a car in dense, urban traffic using inverse reinforcement learning. By designing an architecture split into ego trajectory generation, checking, and scoring, we were able to leverage simple and reliable methods for the relatively easy tasks of trajectory generation and safety checking. This architecture allowed the trajectory scoring component of our system to focus on learning nuanced driving behavior important for good performance in dense traffic. We demonstrated our planner on the busy Las Vegas Strip, where it showed strong real-world performance on challenging scenarios such as cut-ins, abrupt braking, and cluttered hotel pickup/dropoff zones.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We would like to thank our colleagues Juraj Kabzan, Dimitris Geromichalos, Christopher Eriksen, Whye Kit Fong, Gordon Gustafson, Qiang Xu, Elena Corina Grigore, and Sunaya Bajracharya for their help and support throughout this project.
