## Introduction

Self-driving cars have been the focus of significant research and development over the past decade. Some companies are tantalizingly close to deploying commercial self-driving taxi services that would make urban transportation cheaper and safer. Progress in self-driving cars has been largely driven by new datasets that helped fuel dramatic improvements in machine learning approaches to object detection and motion forecasting. However, the critical motion planning and decision-making algorithms that ultimately determine driving behavior have yet to see similar benefits from machine learning.

Classical planning and decision-making algorithms for self-driving cars rely heavily on hand-engineered components. Developers will typically hand-tune the scoring function that determines which behaviors are desirable. Manually adjusting features and weights can be a painstaking process -- improving performance in one area often causes unintended regressions elsewhere. Our planner avoids the need to manually craft detailed features or tune weights by learning these components from expert demonstrations using a maximum entropy IRL framework.

Our DriveIRL system works by *generating*, *checking*, and *scoring* trajectories for our vehicle. We use simple and interpretable modules to do the relatively easy tasks of generating a diverse set of ego trajectories and checking that they are safe. Careful construction of the proposed trajectories ensures that they a) are dynamically feasible, b) follow the route, c) satisfy assumptions from the vehicle controller, and d) are diverse. We then apply a lightweight *safety filter* that ensures that each trajectory satisfies a recursive safety guarantee: if we execute the first part of the trajectory, there exists a safe continuation of that trajectory which avoids collision. The learning component of our model focuses entirely on appropriately scoring these trajectories based on the expert demonstrations. Our design directs the model capacity towards hard-to-specify nuances in behavior (e.g., speed profiles, clearances) instead of also creating "nice" trajectories and avoiding obviously unsafe behavior.

DriveIRL achieves strong real-world driving performance on the Las Vegas Strip. The Strip is a major thoroughfare in Las Vegas which connects many of the major hotels and casinos. Challenges include dense traffic, aggressive cut-ins, erratic drivers, and busy passenger pickup/dropoff zones near the hotels. We deployed DriveIRL on a self-driving car and drove fully autonomously on the Strip in these scenarios, showing the practical utility of our approach.

Our main contributions towards learning-based planning for self-driving cars are:

The first learning-based planner to drive a car in dense, urban traffic using IRL.

A simple yet powerful modeling framework that focuses learning on the aspect of driving that is most challenging to specify.

Detailed evaluation of our planner on a real-world dataset that we will make public.

Figure 1: DriveIRL architecture. The learned scoring component is indicated with a dotted boundary.

## Related work

Classical planning: Traditional approaches formulate the planning problem as search over an appropriately constructed graph or trajectory optimization. These methods often have strong theoretical guarantees on convergence to an optimal solution and are relatively easy to interpret. However, the cost function that defines desired behavior is often hand-engineered, and in practice requires painstaking tuning to produce appropriate behavior.

Imitation learning (IL): IL methods attempt to directly imitate the actions of an expert driver. It has seen applications to self-driving cars starting with the pioneering work of ALVINN. More recently, an end-to-end driving policy was learned from camera images to control actions for lane keeping.

A fundamental issue with IL is that there is a distribution shift from training to deployment, as small errors lead to the model operating outside of its training data, which then leads to larger errors. ChauffeurNet uses behavioral cloning with extensive data augmentation to mitigate the distribution shift issue, and UrbanDriver uses an offline policy gradient method with closed-loop rollouts during training to automatically create appropriate data augmentation. TrafficSim similarly uses closed-loop training, but with a focus on creating traffic simulation. While data augmentation improves our performance, it is not as critical since our trajectory generation mechanism pulls the car towards the lane center, reducing divergence.

Closely related is work by Zeng et al. which learns a costmap over the environment to score a set of procedurally generated trajectories. Our approach improves on trajectory generation since we ensure map compliance, as well as on scoring flexibility since we do not impose the assumption of an additive costmap. Furthermore, we demonstrate our model on a vehicle in dense urban traffic.

Another similar approach is that of Vitelli et al., where a hybrid model with a learned planner and an interpretable fallback layer drive in San Francisco. Our IRL-based model is simpler and less reliant on a fallback layer. Furthermore, the recursive check of our safety filter is less conservative.

Reinforcement learning (RL): RL approaches learn a driving policy by optimizing a reward function. The standard approach requires a simulator to update the environment that the driving policy interacts with. There have been a variety of approaches that have shown strong performance in simulation.

Real-world applications of RL for self-driving cars have been rarer, likely due to the difficulty in modeling the environment and specifying the reward function. An early notable example is Riedmiller et al., where they learn a steering policy for a real car. More recently, lane following was demonstrated using deep RL. This approach controlled both speed and steering on a real car. We contrast the rural driving evaluations above with our experiments in busy Las Vegas.

Inverse reinforcement learning (IRL): IRL methods assume that the expert is optimizing an unknown cost function, which is learned from expert demonstrations. An early application of IRL to self-driving cars was for parking lot navigation. The method learned multiple different driving styles from a handful of demonstrations. However, the environment was static and the formulation assumes a linear combination of carefully handcrafted features.

Our approach is based on the popular maximum entropy formulation of IRL, which avoids ambiguities inherent in matching feature expectations. The maximum entropy IRL approach was extended to deep learning in Wulfmeier et al., which avoided the need for laborious hand-engineering of features, and applied to simple benchmarks. The work of Huang et al. is the most related to our approach, but their model only learns a handful of feature weights while still assuming a linear combination of handcrafted features. In addition, their method is validated on a highway driving dataset and not on a real vehicle.

## Inverse Reinforcement Learning Planner

In this section, we describe our Inverse Reinforcement Learning (IRL) Planner as shown in Fig. 1. Our system consists of three main stages: trajectory generation (Sec. 3.2), safety filtering (Sec. 3.3), and trajectory scoring (Sec. 3.4). We rely on simple and reliable hand-engineered modules for trajectory generation and safety, and focus on learning how to score trajectories.

### Input and output

Input: We encode the environment (or scene) around our self-driving car using a mid-level representation. We assume that the ego is localized within a high-definition map and that objects are detected and tracked by a Perception system. Other road users (e.g., cars, bicyclists, and pedestrians) are represented by object type, an oriented bounding box, and speed. The high-definition map provides lane center-lines, road boundaries, traffic light locations, pedestrian crosswalks, speed limits, and other semantic information. We also provide a route, which indicates the lanes that the ego should traverse to make progress towards its goal.

We refer to the *scene context* at a given timestamp as a) the ego dynamic state $\mathcal{S}$ (speed, acceleration, steering), b) the other road users $\mathcal{U}$ (type, oriented bounding box, speed), c) the map $\mathcal{M}$, and d) the ego's desired route $\mathcal{R}$. The model receives the *scene context* at the current timestamp as well as a specified number of previous timestamps (e.g., the past 1 second) as history $\mathcal{H}$.

Output: Our planner generates multiple ego trajectories and scores each one according to how closely it matches what an expert would do given the scene context. A trajectory is a discrete sequence of future states of the ego, where we assume that there is a fixed timestep between all states. Let $s_{t} = {(x,y,\theta,v)}$ represent a state at time $t$, with position ($x$, $y$), heading $\theta$, and speed $v$. All values are with respect to the ego's geometric center in a fixed coordinate frame. The trajectory $\tau = {\lbrack s_{1},\ldots,s_{T}\rbrack}$, where $T$ is the planned time horizon, that is ranked the best among a set of trajectories $\mathcal{T}$, is used as a reference for the vehicle's tracking and actuator controller.

### Trajectory generation

The trajectory generation module uses the scene context to synthesize a diverse set of possible future motions for the ego. Important considerations for the ego's trajectory are that it a) is dynamically feasible, and b) satisfies all requirements of the low-level tracking and actuator control (i.e., levels of continuity, minimum turn radius, minimum acceleration from a stop). Secondary considerations are that the trajectory is compliant with the map (e.g., it stays on the road). While these considerations do not preclude using a learned trajectory generation module, we found that a hand-engineered trajectory generator best satisfied the considerations above.

The trajectory generator uses i) the current ego state $\mathcal{S}$, ii) the route $\mathcal{R}$, and iii) the map $\mathcal{M}$ to create a diverse set of ego trajectories $\mathcal{T}$, namely ${(\mathcal{S},\mathcal{R},\mathcal{M})}\mapsto\mathcal{T}$. The generator integrates a desired acceleration profile along the route ahead of the ego. In our experiments, we specified a range of constant acceleration profiles ranging from a hard brake (${- 5.0}\ {m/s^{2}}$) to a moderate acceleration ($1.5\ {m/s^{2}}$). As the ego will not always be on the lane center-line (due to vehicle controller tracking errors), we smoothly connect the initial ego pose with the route with Dubins paths LaValle where turning radii are a fixed set of parameters. In a typical scene, the trajectory generator usually creates $50$-$150$ trajectories depending on the ego state and route. Some examples are shown in the Fig 2. Appendix A.1 provides results to validate that the generated trajectories are of good quality.

Figure 2: Proposed trajectories for the ego (red rectangle). Each trajectory is shown in translucent white dot-line. Overlap is due to multiple acceleration profiles. All trajectories return to the route.

### Safety filter

Figure 3: Safety filter. Left: toy scenario with three trajectories (ego is in red, vehicle ahead is in yellow). Middle: modified trajectories. Right: unsafe trajectories excluded from trajectory set.

Before scoring candidate trajectories, we apply an interpretable safety filter (Fig 3) to guarantee basic safety (i.e., no collisions). It consists of:

a set of world assumptions used to predict the behavior of the non-ego road users,

a set of trajectory modifiers which are applied to the ego trajectory, and

a set of safety checks which the modified ego trajectory needs to pass.

For a candidate trajectory to be considered safe, it must pass all safety checks, under the given trajectory modifications and assumptions about the other road users. See A.2 for details.

Our safety filter is similar in spirit to the fallback layer proposed by Vitelli et al., except that 1) it directly filters the proposed trajectories, rather than projecting the output trajectory to an ad-hoc trajectory set, and 2) the trajectory modifier effectively implements a recursive safety guarantee with minimal assumptions and checks, without compromising comfort.

### Trajectory scoring with maximum entropy IRL

Appropriately scoring trajectories is the core challenge of our planning approach. This difficulty is because proper driving behavior is heavily influenced by the environment around us, including other road user behavior and goals, of which we only have a partial understanding.

Trajectories are scored by a deep neural network trained with a maximum entropy IRL loss. We use expert demonstrations collected from a skilled human driving our vehicle. The loss favors trajectories that most closely match the expert demonstration $\tau^{\star}$ in feature space. In particular, let $r{(\tau)}$ represent the reward of the trajectory $\tau \in \mathcal{T}$, the probability of a trajectory $\tau^{\ast}$ being selected according to the maximum entropy principle is ${P{(\tau^{\star})}} = \frac{{\exp r}{(\tau^{\star})}}{\sum\limits_{\tau}{{\exp r}{(\tau)}}}$.

The negative log-likelihood loss (NLL) on a dataset $D$ is defined as ${\ell{(D)}} = {- {\sum\limits_{d \in D}{{\log P}{({\tau^{\star}{(d)}})}}}}$ where $\tau^{\star}{(d)}$ is the demonstrated trajectory on the token $d \in D$. To address data imbalance issues, we augment NLL with focal loss (with a $\gamma$ of $2.0$)

Features: We compute features for each proposed trajectory to use as inputs to our neural network. These features can be based on any combination of a proposed trajectory $\tau$, ego state $\mathcal{S}$, other road users $\mathcal{U}$, the map $\mathcal{M}$, route $\mathcal{R}$, and history $\mathcal{H}$, meaning that $F_{i}:{{(\tau,\mathcal{S},\mathcal{U},\mathcal{M},\mathcal{R},\mathcal{H})}\mapsto f_{i} \in {\mathbb{R}}^{k_{i}}}$, where $F_{i}$ is the feature extraction function corresponding to feature $i$ and $k_{i}$ is its dimension.

Time-to-collision (TTC): the minimum number of seconds before the ego would collide with another road user in the (predicted) future. Evaluated at multiple points.

ACCInfo: the ego speed, the distance to the road user ahead, the speed of the road user ahead, and the relative speed of the road user ahead. Evaluated at multiple points.

MaxJerk: the maximum jerk ($\ {m/s^{3}}$) along the trajectory.

MaxLateralAccel: the max lateral acceleration ($\ {m/s^{2}}$) along the trajectory.

PastCoupling: concatenation of the future trajectory and the one second of past ego poses to model learn to maintain the coherence between the past, present, and future trajectories.

SpeedLimit: how closely the trajectory obeys the speed limit. Evaluated at multiple points.

More implementation details can be found in the Appendix A.3.

Motion prediction: Some of the features computed for each proposed trajectory require an estimate of where other road users will be in the future, such as Time-to-collision (TTC) and ACCInfo. We use an Intelligent Driver Model (IDM) as our prediction model for other cars, with a conservative acceleration value to avoid assuming that stationary vehicles will speed up. We use a constant velocity model for pedestrians and for vehicles without a nearby lane.

Model architecture: To score a trajectory, we adopt an architecture in which the extracted features are processed separately before interacting with one another through a masked self-attention mechanism.

Figure 4: Detailed trajectory scoring architecture.

Under this architecture, each input feature $f_{i}$, as a temporal sequence of related vehicle-environment interaction data, is first normalized through an application of a BatchNorm1D layer before being fed to an LSTM module with one layer and a hidden size of $20$. The output of the LSTM becomes the input to a feed-forward module and then a self-attention mechanism with two heads and an embedding dimension of $120$. Here we employ zero-masking of the queries to encode position. By taking into account other features through self-attention, the model produces for each feature a "corrected" output embedding that can now be passed to a feed-forward network which converts it into a scalar and then a $\tanh$ activation to produce a feature score $y_{i}$. The final score for the trajectory is the sum of these feature scores after they are multiplied by the corresponding learnable feature weight parameters $w_{i}$: ${r{(\tau)}} = {\sum\limits_{i}{w_{i}y_{i}}}$. In total, our base (best) model has $\approx {88,700}$ trainable parameters.

## Experiments

The proposed inverse reinforcement leaning planner was evaluated on a large-scale dataset and the results are presented in the following. The dataset we used is described in Sec 4.1. The metrics for comparison is explained in Sec 4.2. Various model ablation studies and the comparison with baseline are shown in Sec 4.3 and 4.4. We demonstrated both simulation results and the real-world driving tests in Sec 4.5 and 4.6 respectively.

### Dataset

We created a self-driving car dataset that captures real-world urban driving in the center of Las Vegas. Our dataset is a part of the nuPlan dataset that will be made public. It includes object annotations and high-definition maps. Vehicles, pedestrians, and bicyclists are automatically annotated using an offline perception system (similar in spirit to Qi et al. ) and viewed as ground truth. We performed filtering and extracted 182,032 scenarios, each 11 seconds in duration (1 second past, 10 seconds future), for a total of approximately 556 hours. Our main interest was to learn good adaptive cruise control (ACC) behavior. Thus, we filtered out scenarios where the ego made lane changes or deviated far from the lane. After filtering, we performed a 3:1:1 split for train, val, and test sets. Tab. 1 shows a detailed distribution of our dataset by scenario tags. The tags in the table are not mutually exclusive and a scenario can belong to multiple tags. More detailed definitions for the scenario tags are in Appendix A.4.

Table 1: A detailed distribution of our dataset (182, 032 total 11-second scenarios).

### Metrics

We evaluate our model using a variety of metrics to give a full picture of driving. To approximate real-world conditions, we perform a closed-loop replay for each scenario for a duration of 10 seconds. We initialize the ego at the start of the scene, compute a planned trajectory, move along that trajectory for one step, replay the other agents, and repeat. Then, we compute metrics on the resulting executed trajectory as averages over the full scene duration.

Metric computation: Evaluation was done with a time step size of $0.2$ seconds and a total duration of $10$ seconds. The model was given $1$ second of ground truth past prior to the start of the scene. Other road users were updated by replaying their positions from the database.

Metric categories: We have four high level categories of metrics that contain "low level" metrics and high level summary metrics that act as a score for the category. The categories for our metrics are Safety, Comfort, Progress, and $\ell_{2}$ (with a yaw penalty of $2.5$). Further details about our metric categories and the low level computations that make them up can be found in Appendix A.5.

Metric limitations: Currently, there are two major limitations to our metrics evaluation.

The use of replay for other agents. Since other vehicles do not react to the ego (e.g., if we drive slower than the expert in the data), the overall "Safety" score is a lower bound on safety.

No controller or vehicle dynamic simulation for the Ego. We currently "teleport" the ego along its trajectory, causing jerk to be erroneously high in some cases. Similar to safety, this makes our "Comfort" score a lower bound on what we actually observe in real world driving.

### Model ablations

In our experiments, we use a batch size of $64$ and an Adam optimizer with an initial learning rate of $10^{- 3}$. Additionally, we use a "cosine annealing with warm restarts" scheduler, which gradually lowers the learning rate to a minimum of $10^{- 4}$ and resets it every seven epochs. All models are trained over 20 epochs on eight AWS g4dn-metal instances with eight 16 GB NVIDIA Tesla T4 GPUs each. Because closed-loop simulation is computationally expensive, we randomly sampled $1,000$ scenarios from our evaluation set for ablation studies and $3,000$ scenarios from the test set for the final performance evaluation against other baselines. Training and closed-loop metrics evaluation takes about an hour per epoch.

Feature importance: To understand the importance of each hand-engineered feature and the main contribution of each, an ablation study for features is conducted and summarized in Tab. 2. The relative importance of each feature is shown by dropping one of them out at a time. We claim that all the features are important because the Base model which includes all features got the highest scores across all high-level metrics and had lowest Collision rate. Even though the $\ell_{2}$ error is a bit higher compared to No MaxJerk, the $0.089$ $m$ difference is not significant in the qualitative results. The results also demonstrated the importance of PastCoupling feature in ensuring Comfort. The experiment also showed that TTC feature contributes significantly to reducing the collision rate.

Table 2: Ablation study on the importance of each feature. The row indicates the feature removed from the baseline model. See Sec. 3.4 for definitions.

Data augmentation: Data augmentation is important to ensure that our model can learn how to recover from errors. Since the reference trajectory is never followed perfectly by the vehicle, errors can accumulate. We perturb the ego's initial state during training to reduce the sensitivity to such errors. For our low noise baseline, we use zero-mean Gaussian data augmentation for longitudinal offset ($1.2\ {m\text{/}}$ std), lateral offset ($0.8\ {m\text{/}}$ std), heading offset ($0.1\ {{rad}\text{/}}$ std), and velocity ($0.1\ {m\text{/}s}$ std). For the high noise ablation, we respectively use $2.5\ {m\text{/}}$ std, $1.5\ {m\text{/}}$ std, $0.3\ {{rad}\text{/}}$ std, and $0.2\ {m\text{/}s}$ std. We clamp velocity to avoid negative values. Several example images are shown in A.6.

Base (low noise)

Low past + present

Table 3: Comparison between different augmentation schemes.

Architecture: We perform several ablations on the model architecture before selecting an architecture in which the extracted features are processed separately before interacting with one another through a masked self-attention mechanism. We show in Tab. 4 that the other two extremes, namely, concatenating all input features and using them as one monolithic feature in a single feedforward network or siloing all input features (not allowing any interaction through attention or otherwise) have resulted in inferior performance. It is also seen that input normalization and attention input masking are beneficial.

Table 4: Comparison between different model architectures.

Loss: Tab. 5 shows that it is better to maximize the probability the projection of the ground truth onto the trajectory set (the best approximation in average $\ell_{2}$ norm) instead of the ground truth itself. This makes sense because the ground truth does not come from the same distribution as the proposals and is not available at inference time. Filtering possibly unsafe trajectories from the set before finding the ground truth projection is also crucial to obtaining a safe model. Doing the projection using the average $\ell_{2}$ norm instead of an $\ell_{2}$ norm with a yaw error penalty also seems favorable. Lastly from the same table, we can see that using focal loss as in Equation 1 improves performance. Another experiment in Appendix A.7 that compares focal loss against training on a better balanced dataset also shows that using focal loss is actually more effective for DriveIRL.

Possibly unsafe demo

Demo w/ weighted yaw

Without focal loss

Table 5: Comparison between different loss functions.

### Baselines

In this section, we evaluate our model on a test dataset and compare it with an Intelligent Driver Model (IDM) and a constant speed (CS) lane follow model. The IDM baseline is a reasonable choice because it is a well-known version of an expert planner that focuses on adaptive cruise control. Meanwhile, the CS lane follow model is a simple lower-bound. The results are shown in Tab. 6. Our base model plus safety filter outperforms others in all safety related metrics, and that shows the safety filter protects the vehicle on several collision cases our model cannot handle perfectly. Without the safety filter, our base model still outperforms the IDM baseline. The IDM model has significantly higher $\ell_{2}$ error, indicating that the IDM model does not drive like a human expert. Furthermore, our base model also has higher scores in all safety related metrics in both high- and low-level scores like collision rate and tailgate rate.

Base + Safety (ours)

Table 6: Baselines on the test set. IDM = Intelligent Driver Model. CS = constant speed.

### Simulation results

Fig. 5 exhibits some qualitative closed-loop simulation results of our planner driving in typical scenarios. These scenarios are shown as a sequence of snapshots along the closed-loop rollout. The ego vehicle is shown as a red rectangle, the expert vehicle is in blue, and other vehicles are in yellow. The orange line is the planned route (along the lane centerline) and the purple circles represent the planned trajectory for the next $6$ seconds. Our planner shows good performance over a range of scenarios, exhibiting reasonable and consistent behavior over $10$ second rollouts.

(a) Ego starting from a stop.

(b) Ego stopping for the lead vehicle.

(c) Adaptive cruise control.

Figure 5: Qualitative driving performance in common scenarios. Full-size images are in A.8.

### Real-world driving

Prior to deploying on public roads, DriveIRL was rigorously tested in both simulation and on private, closed-course routes. The simulation tests consist of the same Las Vegas Strip route that was our deployment goal, and involve a high-fidelity dynamics model for the ego vehicle and numerous actors exhibiting a wide variety of behaviors. When deployed on the Strip, the vehicle was piloted by a vehicle operator who was trained to take over for unsafe behavior and situations outside of our operating domain, including construction zones, bus stops, and yielding for emergency vehicles.

On the Strip, our planner handled challenging scenarios such as heavy traffic, aggressive cut-ins, unpredictable drivers, and busy passenger pick-up/drop-off zones near the hotels and casinos. Without the safety filter, the vehicle remained in autonomous mode for 8.8 miles of the 11-mile route. Overrides occurred for mandatory takeover regions and twice for undesired behavior. With the safety filter, the vehicle remained in autonomous mode for 6.9 of 8.5 miles, with takeovers only occurring due to mandatory takeover regions.

Figure 6: Smoothly stopping behind a vehicle in dense traffic on the Las Vegas Strip.

Fig. 6 shows a typical maneuver where our self-driving vehicle smoothly stops for a vehicle ahead while surrounded by multiple vehicles. In Sec. A.9, we have included video clips with more real-world driving maneuvers. These videos are grouped in categories such as cut-ins, driving around passenger pickup/dropoff zones, driving with a vehicle ahead and stopping behind a vehicle.

## Conclusions

We introduced DriveIRL: the first learning-based planner to control a car in dense, urban traffic using inverse reinforcement learning. By designing an architecture split into ego trajectory *generation*, *checking*, and *scoring*, we were able to leverage simple and reliable methods for the relatively easy tasks of trajectory generation and safety checking. This architecture allowed the trajectory scoring component of our system to focus on learning nuanced driving behavior important for good performance in dense traffic. We demonstrated our planner on the busy Las Vegas Strip, where it showed strong real-world performance on challenging scenarios such as cut-ins, abrupt braking, and cluttered hotel pickup/dropoff zones.
