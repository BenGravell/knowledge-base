<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Towards Learning-based Planning: The nuPlan Benchmark for Real-world Autonomous Driving

Topics include Autonomous driving, Vehicles, Safety, Datasets, Benchmarks, Planning, Learning, nuPlan, Machine learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Machine Learning (ML) has replaced traditional handcrafted methods for perception and prediction in autonomous vehicles. Yet for the equally important planning task, the adoption of ML-based techniques is slow. We present nuPlan, the world's first real-world autonomous driving dataset, and benchmark. The benchmark is designed to test the ability of ML-based planners to handle diverse driving situations and to make safe and efficient decisions. To that end, we introduce a new large-scale dataset that consists of 1282 hours of diverse driving scenarios from 4 cities (Las Vegas, Boston, Pittsburgh, and Singapore) and includes high-quality auto-labeled object tracks and traffic light data. We exhaustively mine and taxonomize common and rare driving scenarios which are used during evaluation to get fine-grained insights into the performance and characteristics of a planner. Beyond the dataset, we provide a simulation and evaluation framework that enables a planner's actions to be simulated in closed-loop to account for interactions with other traffic participants. We present a detailed analysis of numerous baselines and investigate gaps between ML-based and traditional methods. Find the nuPlan dataset and code at nuplan.org.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the last decade, autonomous vehicle perception and prediction have been revolutionized by deep learning-based methods trained on large-scale datasets. While similar attempts have been made in the field of learning-based or neural planning, these are not yet able to surpass their rule-based counterparts. One possible reason is the difficulty of generalizing driving scenarios when learned from a limited number of examples. Furthermore, driving scenarios typically follow a long-tail distribution, which further exacerbates the generalization issue. Finally, learning-based planning lacks formal safety guarantees, thus making it potentially unsafe and challenging to certify.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce the nuPlan dataset and simulation framework for autonomous vehicle planning. Our goal is to create a testbed for open-loop and closed-loop planning starting in real-world scenarios. This test bed is then used to compare traditional, learning-based, and hybrid planners. nuPlan enables numerous novel types of research, such as learning-based planning, the interplay between prediction and planning, and end-to-end planning using a large amount of published sensor data.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We release the largest dataset for autonomous driving to date, with a total of 1282h from 4 cities. We also publish an unprecedented 128h of sensor data.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop techniques to auto-label the dataset with accurate object tracks, traffic lights, and scenario labels.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We publish our closed-loop simulation and evaluation framework and compare the performance of traditional and learning-based planners to identify gaps.

<!-- chunk {"id": "body-0008", "role": "body", "section": "II-A Datasets", "weight": 1.0} -->

Tab. I provides an overview of large-scale prediction and planning datasets with more than 20h of data. We omit smaller datasets like Interaction, highD, inD, OpenDD and CommonRoad and subsets of datasets not focused on prediction or planning. With the exception of nuPlan and CommonRoad, all datasets focus on prediction (motion forecasting). Offline perception is crucial to train and evaluate planners using high-quality object tracks, but only present in Waymo, MONA and nuPlan. Likewise, the availability of traffic light statuses is crucial for realistic traffic simulation, but only Waymo and Lyft contain these and only from an online perception system, rather than developing offline traffic light status inference as in nuPlan. To assess planning performance we need to focus on specific scenarios and evaluate them in closed-loop. nuPlan is the first dataset to feature both scenario tags and a closed-loop simulation framework. Lyft provides interactive tutorials for closed-loop simulation, but they lack the modular framework, evaluation server, and hold-out test set of nuPlan. Finally, we need a large-scale dataset to generalize well.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-A Datasets", "weight": 1.0} -->

Only the Lyft, Shifts and nuPlan datasets provide more than 1000h of driving data and nuPlan was the first such dataset that provides lidar and camera sensor data (128h), although Waymo later also released compressed lidar data.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-B Simulation", "weight": 1.0} -->

Many works in the literature use proprietary simulators. While sharing their approaches to planning, they do not provide enough information to reproduce their experimental results. Graphical simulators like CARLA and AirSim focus on photorealistic rendering, but lack the realism of real-world maps and agent behavior. CommonRoad was the first open-source simulator focused on planning. However, CommonRoad does not provide a real world dataset as the basis for the simulation, instead resorting to a small number of manually crafted scenarios and tools to import other datasets, albeit without any sensor data. With nuPlan we aim to overcome the above limitations by releasing a large-scale real-world dataset and an open-source closed-loop simulator. Following the release of nuPlan, ScenarioNet focused specifically on Reinforcement Learning and integrated nuPlan and other datasets into their pipeline. They also interfaced with MetaDrive that enables graphical simulation of nuPlan.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-C Planning", "weight": 1.0} -->

Classical planning. The planning problem has long been treated as an optimization problem in the traditional approaches. By carefully designing a cost function, the optimization aims to generate the optimal trajectory that minimizes the cost function in the corresponding search space (e.g., A\* search, sampling-based methods, dynamic programming ). While these approaches enjoy the theoretical guarantees on the convergence to an optimal solution, hand-crafting the cost function that represents the human-like driving behavior is challenging. In practice, many studies rely on tremendous engineering efforts to fine-tune the solution.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-C Planning", "weight": 1.0} -->

Learning based planning. Pioneering by the study of, the idea of using a neural network to imitate expert driver and directly output driving control command provides an alternative planning solution. With the recent success of deep learning, the learning based planning received considerable attention.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-C Planning", "weight": 1.0} -->

Imitation learning (IL) and inverse reinforcement learning (IRL): IL trains a model to either map the sensor data directly (end-to-end system), or indirectly through the perception and prediction models (modularized system), to the expert driver actions (e.g. steering and speed profile). With the advancements in deep learning literature, IL studies adopt the state-of-the-art supervised learning models architectures to learn better scene representations. IL often suffers from a poor generalization where the compounding error leads to driving scenarios that are outside of the training data, known as "covariate shift". Carefully designed data augmentation is often used to address this issue. As an alternative to directly imitating the driver behavior, IRL aims to learn an unknown reward function that explains expert demonstrations. Once learned, such reward function is used to infer the optimal trajectory from a set of pre-defined or generated trajectories. The maximum entropy formulation of IRL has been applied to autonomous driving where the reward function is estimated based on a set of handcrafted features.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-C Planning", "weight": 1.0} -->

Reinforcement learning (RL): RL learns the optimal driving behavior by interacting with the environment and optimizing a given reward function. RL is well-suited for handling the interaction between the agent and the environment in a sequential decision process. However, due to its learning by "trial-and-error" search nature, studies in RL rely on the driving simulation to provide the environment. These studies have demonstrated strong performance in simulations. The real-world applications of RL in autonomous driving are also reported.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-C Planning", "weight": 1.0} -->

Hybrid solutions. Hybrid solutions are proposed to leverage the advantages of both the classical and learning based planning. Several studies use learning to improve the classical planning algorithm. These include using a learning model to guide the exploration for sampling-based path-planners, using a learning model to improve the efficiency of sampling-based motion-planners in high dimensional setting, applying optimizer to actively rectifies the learning model's plan to satisfy the safety and comfort requirements. Other studies leverage the classical planning to generate the trajectory candidates, which are passed to an ML-based model to evaluate.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-C Planning", "weight": 1.0} -->

System design. While planning is the ultimate goal of the autonomous driving system, different system designs to assemble the perception and prediction introduce opportunities and challenges to improve the planning performance. Most autonomous driving systems use a multi-stage pipeline of independent tasks like perception, prediction and planning. The hope is that the performance gain on individual tasks translates to a better planning performance. In contrast, various studies consider multi-task learning (MTL) where they jointly train models to perform perception, prediction and planning simultaneously. These works have shown that MTL achieves better data utilization at lower computation cost. Recently, some studies leverage the query-based design in transformer architectures to integrate all tasks in a unified framework that is trainable end-to-end. Such a framework encourages better spatio-temporal feature learning from the sensor data and directly improves the planning performance.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Dataset", "weight": 1.0} -->

In this section, we describe how we collect the nuPlan dataset. We enhance it by auto-labeling the object tracks of other agents and traffic lights, as well as mining for scenarios that are relevant for tracking.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Data collection", "weight": 1.0} -->

We collected data from 4 cities (Boston, Pittsburgh, Las Vegas, and Singapore) to build a benchmark dataset for ML-based planning. In total, we have 1282 hours of challenging and real-world driving scenarios. For example, double parking in Boston, custom precedence patterns for left turns in Pittsburgh, crowded pick-up and drop-off points (PUDOs) in casinos in Las Vegas, and left-hand traffic in Singapore. We exclude heavy rain and night data, as these would impact the quality of our perception system (see Sec. III-B).

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Data collection", "weight": 1.0} -->

Manual driving. We use Chrysler Pacifica Plug-in Hybrid Electric Vehicles (PHEV) to drive in these cities. See Fig. for the sensor setup. Our vehicle operators (VOs) are instructed to use a natural driving style and drive safely. Since our focus is on planning, it is crucial that we drive manually, while most other datasets use a combination of manual and automated driving, which may lead the planner to imitate less desirable driving behavior. The VOs drive from a predefined starting point to a goal using a known route. For example, we drive between various hotels and casinos on the Las Vegas strip, which are typical routes for our robotaxi and are known and mapped beforehand.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Data collection", "weight": 1.0} -->

Sensor data. Sensor data include lidar point clouds and camera images. Due to the vast scale of the full sensor dataset (200+ TB), we only release a subset of the sensor data which totals 128 hours. This subset was selected to satisfy all stratification constraints as described below.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Data collection", "weight": 1.0} -->

Maps. Similar to nuScenes, nuPlan provides detailed human-annotated 2D high-definition semantic maps of the driving locations. We release rasterized and vectorized maps. While rasterized maps are useful for simplicity and efficient lookup, vectorized maps provide more precise geometric information and metadata. Examples of semantic map layers are lanes, car parks, crosswalks and stop lines.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Auto-labeling", "weight": 1.0} -->

In order to faithfully reconstruct various driving scenarios, we develop an auto-labeling system. It first generates the tracks for all the objects in the scene; then traffic light statuses are inferred from these tracks. Based on the above labels, we can reliably mine different driving scenarios.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Auto-labeling", "weight": 1.0} -->

Offline perception. We build an offline perception system to label the objects in the scene automatically. Compared with the online perception systems used in many other datasets, the offline version is not constrained by latency and causality. Therefore, the fidelity of the generated tracks is drastically higher, enabling us to evaluate planning performance under very limited perception noise.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Auto-labeling", "weight": 1.0} -->

Inspired, our offline perception system contains three stages: 3D object detection, offline tracking, and global track refinement. The detector in the first stage takes the point clouds from both the top lidar and side lidars as input and detects the bounding boxes through a large neural network. The offline tracker leverages both past and future detections in an extended time window to generate tracks. In the last step, a novel network is developed to load both tracks and points clouds within the tracks to refine the attributes of all the bounding boxes of vehicle class, such as positions, headings, sizes and velocity.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Auto-labeling", "weight": 1.0} -->

Traffic light status. To create a realistic simulation of the environment, it is crucial to capture the traffic light statuses. Existing datasets lack traffic lights or use online vision-based systems to detect their statuses. In contrast, we develop a novel offline system to automatically label the statuses of traffic lights by inferring them from the motion of the actors present in the scene. Our labeling system is able to cover all lanes with observed agents.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Auto-labeling", "weight": 1.0} -->

We make use of the detections and tracks produced by our offline perception system, as well as map information. To infer a green traffic light status within a given intersection, we determine if there are agents moving within the intersection in the direction controlled by the particular traffic light. To infer a red traffic light status, we check for agents slowing down or being stationary in the lane that approaches the intersection and controlled by the particular traffic light.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Auto-labeling", "weight": 1.0} -->

Scenario mining. Traditional approaches to evaluate planning performance are dominated by monotonous lane following scenarios. To get a fine-grained understanding of the planning performance, we develop a scenario taxonomy and scenario mining algorithms using low-level attributes like vehicle speed and state transitions. The attributes can be inferred from offline perception tracks and traffic light statuses. In total, we have 73 unique scenario types.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Simulation", "weight": 1.0} -->

nuPlan provides a simulation framework that is modular and flexible to work with different datasets and setups. The simulation is initialized with the real-world observations captured in the dataset, namely raw sensor data or object tracks. Given these environment observations, an agent model can be used to predict the future trajectories of all agents. Observations and agent trajectories are passed to a planner that predicts the best route for the ego vehicle given the other agents' routes. Finally, a controller converts the intended route into a feasible trajectory. The simulation can either playback the actions recorded in the dataset (open-loop) or allow the simulation to deviate from the recording by incorporating the ego's actions (closed-loop). Below are the simulation components in detail.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A Agents", "weight": 1.0} -->

Of the 6 object classes, vehicle, pedestrian, generic object, traffic cone, barrier, bicycle, construction zone sign, 3 are moving object classes simulated as agents: vehicles, pedestrians, and cyclists. Agents are dynamic objects that can move as the scenario evolves.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A Agents", "weight": 1.0} -->

A well-known method is to simply propagate agents according to the logged data. We refer to these as non-reactive log-replay agents. Log-replay agents are used to simulate scenarios both in open-loop and closed-loop, a near-perfect recreation of the recorded data. However, closed-loop simulation quickly diverges if the planner decides to take different actions from what is recorded in the log. Thus, in closed-loop simulation agents can be also simulated with the aim to interact with the ego vehicle and with each other by producing novel simulation states that resemble real agent behaviors. We refer to these as reactive agents. Reactive agents are only relevant in closed-loop simulation and by definition open-loop simulation uses non-reactive agents.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Agents", "weight": 1.0} -->

We develop reactive agents following the Intelligent Driver Model (IDM) policy. IDM agents are initialized with the initial pose and velocity of the logged agents. The agents follow the lane center line of the underlying map. The longitudinal control is dictated by the IDM policy. This allows the agents to react to the ego's actions, as well as other reactive agents. In turn, this reduces false collisions and lets scenarios play out for longer. Note that we only apply this policy to vehicles, while Vulnerable Road Users (VRUs) are replayed from the log. We choose not to model VRUs as reactive agents as their behavior is often uncooperative and thus hard to model.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B Controller", "weight": 1.0} -->

In nuPlan, planners provide a trajectory as a sequence of poses in $SE{}$, without any kinematic feasibility requirement. This trajectory is assumed to be sampled at specific times in the future according to the simulation configuration. To assert kinematic feasibility and prevent users from cheating, we require the use of a controller. nuPlan provides the flexibility to use any controller, such as perfect tracking, which simply interpolates poses along the planned trajectory.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-B Controller", "weight": 1.0} -->

We developed a two-stage controller to propagate the simulation in closed-loop. This controller consists of two parts, a trajectory tracker and a motion model to forward-integrate the simulation. We implement a Linear Quadratic Regulator (LQR) as the tracker. The found optimal control policy is then fed to the second part of the simulation controller, a kinematic bicycle model which is forward-integrated to propagate the simulation state. Alternatively, we also support different trackers in the two-stage controller, such as an iterative-LQR tracker.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-C Evaluation", "weight": 1.0} -->

Different metrics and frameworks have been explored for scoring models in prediction and motion planning benchmarks. In this paper, we select a set of metrics and design an aggregation method to compare the performance of planners. In open-loop, we only evaluate the closeness of the planner generated trajectory to the human-driven trajectory. The open-loop metrics are modified Average Displacement Error (ADE), Final Displacement Error (FDE), Average Heading Error (AHE), Final Heading Error (FHE), and Miss Rate (MR) in which we calculate the metrics over different horizons and report their average score. For closed-loop, we use a combination of metrics to evaluate lawfulness and compliance with traffic rules consisting of no at-fault collisions, trajectories inside drivable area, no trajectories in lanes belonging to oncoming traffic, not driving above the speed limit and maintaining enough Time To Collision (TTC) with other road users, metrics to evaluate progress towards the goal and measure the rider comfort.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-C Evaluation", "weight": 1.0} -->

All metrics' scores are normalized to the range $\lbrack{0 - 1}\rbrack$ using thresholds that are selected based on legal requirements and natural human driving. A higher score indicates a better performance.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-C Evaluation", "weight": 1.0} -->

The final score of a planner is computed by averaging the scores for its generated trajectories across all scenarios. The score of a trajectory in a scenario is given by a hybrid weighted average of all metrics' scores.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-C Evaluation", "weight": 1.0} -->

The rest of the metrics are weighted according to their importance (See Tab.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-C Evaluation", "weight": 1.0} -->

We define the score for each challenge (open-loop, closed-loop non-reactive, and closed-loop reactive) as the average scenario score across all scenarios for that challenge.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-C Evaluation", "weight": 1.0} -->

AHE and FHE within bound

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-C Evaluation", "weight": 1.0} -->

ADE and FDE within bound

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experiments", "weight": 1.0} -->

Here we present a number of planning baselines and their results when evaluated on the nuPlan benchmark. We analyze how the planning performance is impacted by lower quality perception inputs, as well as how it generalizes to other cities. Finally, we discuss the new state-of-the-art set by the submissions to the first nuPlan challenge.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-A Planning baselines", "weight": 1.0} -->

We implement several planning methods that are representative of the literature.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Simple Planner", "weight": 1.0} -->

The Simple planner has little planning capability. The planner plans a straight line at a constant speed. The only logic of this planner is to decelerate if the current velocity exceeds the max velocity.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Planner", "weight": 1.0} -->

The Intelligent Driver Model (IDM) planner is essentially an Adaptive Cruise Control (ACC) policy. The planner consists of two parts: path planning and longitudinal control. The path planning component is a breadth-first search algorithm. It finds a center-line path toward the mission goal extracted from the underlying map structure. The longitudinal control follows the IDM policy. The policy describes how fast the planner should go based on the distance between itself and the closest leading agent.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Raster ML planner", "weight": 1.0} -->

Similar to the encoder, the raster planner uses ResNet-50 as the backbone to encode features from an ego-centric multi-channel raster representing the ego, the agents and the map. The model directly outputs the final ego trajectory. The planner does not perform any post-processing on the predicted ego trajectory.

<!-- chunk {"id": "body-0046", "role": "body", "section": "UrbanDriver ML Planner", "weight": 1.0} -->

We adopted an open-loop training variant of the UrbanDriver model as a representative machine learning planner baseline. The model processes vectorized agents and map inputs into local feature descriptors that are passed to a global attention mechanism for yielding a predicted ego trajectory. We train the model using imitation learning to match expert trajectories available in the nuPlan dataset. Data augmentation is additionally performed on the agents and expert trajectory provided during training to mitigate data distribution drift encountered during closed-loop simulation. This version was used for the challenge. We also implemented a multi-step prediction baseline variant as discussed and originally proposed to further address the distribution shift, for the experiments in this work but do not open-source this implementation.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-B Main results", "weight": 1.0} -->

Tab. III shows the planning results for the proposed baselines in each of the three challenge setups. Supervised learning-based planners excel in an open-loop setting. This is unsurprising as the task is akin to the traditional motion forecasting challenge. This suggests that an ML planner can choose to make similar decisions to a human driver in open-loop settings. However, ML planners still struggle to overcome the distribution shift in closed-loop. A closed-loop scenario can develop into a new situation that was never present in the training dataset. Even techniques such as data augmentation and closed-loop training fail to overcome this domain gap. This is evident in both the literature and our experiments. Rule-based planners, on the other hand, face no such issues. Policies like IDM can produce decent driving behavior. This is confirmed by the metrics as it achieved the highest scores for closed-loop. It should be noted though that the reactive agents are also modelled with a similar IDM. The use of similar assumptions on the vehicle behavior may result in giving the IDM planner an unfair advantage over other planners in closed-loop evaluation.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-B Main results", "weight": 1.0} -->

It is evident that sufficiently sophisticated rule-based planners still outperform purely learned planners in closed-loop settings.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-C Perturbation", "weight": 1.0} -->

As the nuPlan dataset is created with offline perception, to capture the original probability distribution of data collected online, we injected uniform noise on the detections. Noise was added in the dimensions and the pose of the detected agents, with variance extracted by comparing offline and online detections. The scores of planners under nominal and noise-injected simulations in closed-loop reactive mode are presented in Tab. IV. A version of UrbanDriver trained on the perturbed data is called UrbanDriverOnline, which shows a performance deterioration compared to the nominal model on both nominal and injected data. This indicates the value of high-quality offline annotations in the dataset and the learning pipeline.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-D Generalization", "weight": 1.0} -->

The location generalization experiment is shown in Tab. V. The experiment aims to test a model's generalization capabilities. The UrbanDriver model was trained purely on data from Las Vegas. The model was tested separately on scenarios from Singapore, Boston, Pittsburgh, and Las Vegas. The open-loop performance dropped by 53.8%, while closed-loop non-reactive and closed-loop reactive performance dropped by 35.1% and 41.5% respectively. The worst-performing location is Singapore. This can be explained by the left-hand traffic, while the model was trained on right-hand traffic. One insight is that the correlation between the model's open-loop and closed-loop performance is relatively weak. The difference between open and closed-loop scores across Singapore, Boston, and Pittsburgh is only 16.3%, while for Las Vegas it is more than double at 37.3%. This indicates that a good motion forecasting model does not translate to closed-loop capabilities. Thus a major challenge is to overcome the domain gap between open-loop and closed-loop before tackling larger generalization problems.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-E nuPlan challenge", "weight": 1.0} -->

In the nuPlan motion planning challenge contestants create a planner to traverse a set of diverse and challenging scenarios across all four cities. Tab. VI shows the Overall Score, which is the average across Open-loop, Closed-loop Non-reactive, and Closed-loop Reactive challenges of the top four planners. In the open-loop challenge, planners that incorporated supervised learned methods scored relatively well. In the closed-loop challenges, planners employed a combination of learned and handcrafted components. A common theme was the use of a learned model to first predict the ego's planned trajectory. uses a raster-based model that outputs a spatial-temporal heatmap for the ego and an occupancy map for the surrounding agents. are vector-based using transformers as a backbone. Once the trajectory is obtained, the planner has a further refinement stage used to ensure kinematic feasibility and collision avoidance. The highest-scoring planner in closed-loop was mostly rule-based. It generates a handful of trajectories by perturbing the center line laterally at different velocities. Trajectories are selected with a heuristic that considers factors such as collision, drivable areas, traffic laws, and comfort.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-E nuPlan challenge", "weight": 1.0} -->

An ML-generated trajectory is fused to correct the long-term planned horizon. This limited the influence of the learned model. We draw two conclusions from the challenge results. First, ML-based methods require additional post-processing for closed-loop driving. Second, hybrid methods appear to be the most effective approach, combining traditional and data-driven methods.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented nuPlan, the first real-world driving benchmark and the largest existing labeled autonomous driving dataset. The dataset consists of 1282 hours of diverse driving scenarios across 4 cities as well as an unprecedented 128 hours of raw sensor data and is accompanied by an evaluation framework powered by a closed-loop simulator; the dataset and the evaluation framework are publicly available. We investigated the state of current rule-based and learned-based planners by evaluating multiple approaches on the nuPlan dataset across challenging driving scenarios. The first public nuPlan challenge demonstrated that rule-based planners outperform purely ML-based ones, but hybrid planners with learned-based components show the most promise in handling difficult scenarios. In the future, we plan to mine for richer long-tail driving scenarios, design scenario-based metrics, provide ML-based planning and agent baselines and explore end-to-end planner training directly from sensor data.
