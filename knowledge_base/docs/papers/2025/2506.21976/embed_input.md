<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SceneDiffuser++: City-Scale Traffic Simulation via a Generative World Model

Topics include Driving simulation, Traffic simulation, Generative world models, Diffusion models, Autonomous driving, City-scale simulation, Agent behavior modeling, Waymo open motion dataset.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends the SceneDiffuser line toward city-scale traffic simulation, integrating scene generation, agent behavior, dynamic spawning and removal, and environment state such as traffic lights into a single generative world model. The contribution is important because it moves from isolated scene snippets toward point-to-point synthetic driving miles over larger map regions.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The goal of traffic simulation is to augment a potentially limited amount of manually-driven miles that is available for testing and validation, with a much larger amount of simulated synthetic miles. The culmination of this vision would be a generative simulated city, where given a map of the city and an autonomous vehicle (AV) software stack, the simulator can seamlessly simulate the trip from point A to point B by populating the city around the AV and controlling all aspects of the scene, from animating the dynamic agents (e.g., vehicles, pedestrians) to controlling the traffic light states. We refer to this vision as CitySim, which requires an agglomeration of simulation technologies: scene generation to populate the initial scene, agent behavior modeling to animate the scene, occlusion reasoning, dynamic scene generation to seamlessly spawn and remove agents, and environment simulation for factors such as traffic lights. While some key technologies have been separately studied in various works, others such as dynamic scene generation and environment simulation have received less attention in the research community.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose SceneDiffuser++, the first end-to-end generative world model trained on a single loss function capable of point A-to-B simulation on a city scale integrating all the requirements above. We demonstrate the city-scale traffic simulation capability of SceneDiffuser++ and study its superior realism under long simulation conditions. We evaluate the simulation quality on an augmented version of the Waymo Open Motion Dataset (WOMD) with larger map regions to support trip-level simulation.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Imagine an ideal traffic simulation at the city-scale: Starting from a logged or synthetic scene, we initiate the simulation. The virtual world comes alive with agents behaving realistically: cars navigate roads, pedestrians cross streets, and interactions unfold naturally. A pedestrian emerges from behind a bus, prompting a reaction from the ego agent. Vehicles disappear and reappear as they become occluded and disoccluded. Turning onto a new road reveals a fresh stream of traffic. The ego vehicle responds to traffic signals, stopping at red lights and proceeding when they turn green. This simulation persists for a long duration, allowing trip-level evaluations of driving by generating a dynamically populated virtual city with continuous agent interactions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We refer to such a city-scale closed-loop traffic simulation system as CitySim. CitySim can enable point-to-point driving simulation for obtaining trip-level statistics. This allows holistic driving assessment, for instance trip-level travel time comparisons to average human drivers, pick-up and drop-off quality assessment, as well as evaluation of driving behaviors during the trip, including safety and driving quality. Such simulators also allow for playing out events that take longer to unfold, such as interactions between an AV and emergency vehicles. They can also facilitate pre-release evaluation of AV software by estimating safety and quality related rates, system-level hillclimbing, and system-level fault discovery. CitySim systems stand in contrast to simulation frameworks based on simulating logged events (usually $<$ 10s), which is the mainstream setup in most existing frameworks.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Transitioning from event-level simulation to trip-level simulation requires a step-function improvement in simulation capabilities. While event-level simulations are short in duration, naively extending them to longer durations triggers a host of realism issues. In longer simulation, the initial logged agents might leave the periphery of the AV while new agents might continuously and seamlessly appear, mandating dynamic agent generation to handle agent spawning and removal. The need for dynamic agent generation is more critical in cases where the AV takes a different route or speed profile which might result in the AV very quickly turning into an empty street. Furthermore, as the simulated AV heads into regions of the map not traversed in the initial log, traffic light states and other environment factors need to be simulated as well. Simulation artifacts arising from high pose divergence between the logged and simulated AV are referred to as "simulation drift".

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

These unrealistic behaviors in high pose divergence scenarios highlight three critical, yet often overlooked, capabilities in learned traffic simulation: dynamic agent generation (including *agent spawning* for new agents entering the scene, *agent removal* for agents exiting the scene), *occlusion reasoning*, and the dynamic handling of *critical environmental factors* like traffic lights. To our knowledge, most of the aforementioned technologies are not investigated in existing learned simulation models.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we bring together this vision of a realistic and dynamically populated virtual city that enables trip-level simulation in a single end-to-end learned, generative world model that we refer to as SceneDiffuser++. SceneDiffuser++ is a diffusion model that is solely trained on the diffusion denoising objective, yet supports all aforementioned capabilities via simple autoregressive rollout. Following Jiang et al., we model the problem as denoising the scene-tensor, with various key insights. First, we observe that agent spawning, removal and occlusion reasoning can be jointly modeled simply via predicting an additional validity (or equivalently, visibility) channel along with other agent features such as $x,y$, size, type, etc. Though conceptually simple, this requires diffusion to learn to generate sparse tensors without prespecified sparse structure. We propose a simple yet effective training loss formulation and inference-time diffusion sampler modification to allow stable training and sampling of such models. Finally, we propose a novel architecture change that allows simulating the joint rollouts of various non-homogeneous scene elements (e.g., agents and traffic lights with different feature sizes).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose novel ways to evaluate the realism of such trip-level simulation, and benchmark and ablate our design choices on a version of the Waymo Open Motion Dataset (WOMD) augmented with enlarged kilometer-scale map regions for long rollouts.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We conceptualize the novel city-scale traffic simulation task: CitySim, which focuses on trip-level simulations.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast to event-level simulations, we identify novel challenges from trip-level simulations, and propose novel evaluation metrics for evaluating the realism of agent spawning, removal, occlusion and traffic light simulation.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a unified generative world model: SceneDiffuser++, enabling realistic long simulations while accounting for dynamic agent generation, occlusion reasoning and traffic light simulation via simple autoregressive rollout using a novel method to generate sparse tensors.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate our performance on a map-augmented WOMD dataset and achieve state-of-the-art trip-level simulation realism.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Method", "weight": 1.0} -->

Scene Tensor We denote the scene tensor as ${\mathbf{x}}_{i} \in {\mathbb{R}}^{E_{i} \times \mathcal{T} \times D_{i}}$, where $E_{i}$ is the number of elements in the i-th scene tensor (e.g. agents, or traffic lights / signals) jointly modeled in the scene, $\mathcal{T}$ is the total number of modeled physical timesteps, and $D$ is the dimensionality of all the jointly modeled features. We learn to predict attributes for each element: for agents, these are validity $v$, positional coordinates $x,y,z$, heading $\gamma$, bounding box size $l,h,w$, and object type $k \in {\{\text{AV, car, pedestrian, cyclist}\}}$. For traffic lights, these are validity $v$, positional coordinates $x,y,z$ and a categorical traffic light state $s$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Method", "weight": 1.0} -->

All features are normalized to $({- 1},1)$ range while agent types are one-hot encoded. All positional coordinates are normalized by the AV's ego pose. We frame all the tasks considered in SceneDiffuser++ as multi-task inpainting tasks on these scene tensors, conditioned on an inpainting mask $\overline{{\mathbf{m}}_{i}} \in {\mathbb{B}}^{E_{i} \times \mathcal{T} \times D_{i}}$, the corresponding inpainting context values $\overline{{\mathbf{x}}_{i}}:={\overline{{\mathbf{m}}_{i}} \odot {\mathbf{x}}_{i}}$, and a set of global contexts $\mathbf{c}$ (such as roadgraph).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Method", "weight": 1.0} -->

Multi-Tensor We define a multi-tensor $\mathcal{X}:={{\{{\mathbf{x}}_{i}\}},{\forall i}}$ as a collection of scene tensors. See Fig. for an illustration of the multi-tensor structure and scene tensors. Without loss of generality, we learn $\mathcal{X} = {\{{\mathbf{x}}_{\text{agent}},{\mathbf{x}}_{\text{light}}\}}$ for the joint distribution of agents and traffic lights. We train a diffusion model to learn the conditional probability $p{(\left. \mathcal{X} \middle| \mathcal{C} \right.)}$ where $\mathcal{C}:={{\{\overline{{\mathbf{m}}_{i}},\overline{{\mathbf{x}}_{i}},{\mathbf{c}}_{i}\}},{\forall i}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Method", "weight": 1.0} -->

Note that we thus predict a validity mask $\overline{{\mathbf{v}}_{i}} \in {\mathbb{B}}^{E_{i},\mathcal{T}}$ for a given element (agent or traffic signal) at a given timestep (to account for there being $< E_{i}$ agents or lights in the scene or for occlusion).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Method", "weight": 1.0} -->

Tasks We formulate the various tasks, such as scene generation (SceneGen) and behavior prediction (BP) as different inpainting tasks. Following SceneDiffuser, the BP inpainting mask ${\mathbf{m}}_{\text{bp}}$ has 1 for all history steps and 0 for all future steps. SceneGen mask ${\mathbf{m}}_{\text{scenegen}}$ consists of 1 for randomly chosen context agents and 0 for agents to predict. The control mask ${\mathbf{m}}_{\text{control}}$ which consists of randomly sampled $\{ 0,1\}$, is applied on top of either the SceneGen or BP task for further controllability. This work is a special case of BP with additional agent validity prediction.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Method", "weight": 1.0} -->

Architecture While different event types may differ in the number of entities to predict and their feature dimensions, we adapt the same context encoder and Transformer denoiser backbone architecture as SceneDiffuser by homogenizing different scene tensors. We first project different scene tensors to the same hidden dimension, followed by concatenating along the 'elements' axis. After adopting the SceneDiffuser backbone, we apply the reverse process to split and unproject them into the respective scene tensors.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Method", "weight": 1.0} -->

Learning Sparse Tensors One of the major technical contributions of this work is a method for predicting sparse tensors using diffusion. While predicting sparse tensors is of critical importance in this work for learning agent spawning, removal and occlusion, the problem is generic pertaining to learning sparse signals using diffusion models.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Method", "weight": 1.0} -->

We define its inverse to be ${\mathcal{M}^{- 1}{({\mathbf{x}})}} = {{2{\mathbf{x}}} - 1}$. When the validity is False, the corresponding value are arbitrary, whereas when validity is True, the corresponding values are meaningful. We seek to jointly predict the values and validity mask. This presents a set of challenges to conventional diffusion model training. How do we supervise the training of values if some corresponding values do not have ground truth (since they are invalid)? Two alternatives arise: impute all invalid values to be zero, and train as if it's a dense tensor, or leave the invalid bits in the values unsupervised. We find that neither of these two approaches can work. Imputation of zeros for invalid values creates significant discontinuities in the signal, leading to unstable model training. Alternatively, if one leaves the invalid bits unsupervised, they are recurrently fed into the denoiser at inference time, leading to very rapid slippage into out-of-distribution values.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Method", "weight": 1.0} -->

We implement a simple yet effective alternative to these approaches, as described in Fig.. We first cast all values corresponding to invalid steps to zero with ${\mathbf{x}}\leftarrow{{{\mathbf{x}} \cdot \mathcal{M}}{({\mathbf{x}})}}$. Then we compute the loss based on Eqn.. For weight $\mathbf{w}$, we apply the loss mask in as illustrated in Fig., where all features in valid steps are supervised, and only the validity feature in invalid steps are supervised. During inference, we first sample ${\mathbf{z}}_{t = 1} \sim {\mathcal{N}{(0,{\mathbf{I}})}}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Method", "weight": 1.0} -->

We find the clipping step to be the most crucial inference-time trick for generating sparse tensors.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Method", "weight": 1.0} -->

We show in Sec. 4.3 that soft clipping is the most effective strategy that allows stable training and inference with minimal additional changes.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Trip-level Traffic Simulation Setup", "weight": 1.0} -->

Dataset We use the Waymo Open Motion Dataset (WOMD) for our trip-level traffic simulation experiments. WOMD includes tracks of all agents and corresponding vectorized maps in each scenario, and it offers a large quantity of high-fidelity object behaviors and shapes produced by a state-of-the-art offboard perception system. Each scenario in WOMD consists of 91 timesteps with a frequency of 10Hz, leading to a 9.1 second scenario. Although the scenario clips are much shorter than our trip-level simulation route, they contain all the critical agent behaviors (driving, entering, exiting, occlusion) and traffic light states (position detection, lane association, state changes). This feature allows us to use these short clips to train SceneDiffuser++ models that can simulate trip-level scenarios much longer than 9.1 seconds. However, during trip-level rollouts ($> {9.1s}$), we note that agents easily run out of the map and roadgraph extent, as the original WOMD dataset only contains map regions that cover where the AV can reach in 9.1 seconds.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Trip-level Traffic Simulation Setup", "weight": 1.0} -->

To conduct trip-level simulation, we asked for expanded maps from the WOMD dataset creators (all map elements within circles of 1km radius around any portion of the AV's trajectory) to generate a map-extended dataset that we call *WOMD-XLMap*.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Trip-level Traffic Simulation Setup", "weight": 1.0} -->

World Model vs. Planner Real simulation use cases require interaction between two disjoint models -- a planner and a simulator (world model). Specifically, the planner controls the AV's movement given the environment and other agents' movement. On the other hand, the world model controls the traffic lights and all other background agents' movement given the AV's movement. At each rollout step, the planner can only observe the world model's history output and cannot obtain its future predictions, and vice versa for world model. In other words, the planner and world model observe each other's predictions only after we rollout their predictions in the environment. In the case where we use the same method as both planner and world model, we ensure they do not share the same predictions by setting different seeds for random sampling.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Trip-level Traffic Simulation Setup", "weight": 1.0} -->

Method Comparisons We first compare with the *SceneDiffuser* model. Unlike SceneDiffuser++, SceneDiffuser does not model agent validity nor traffic light features. Therefore, during prolonged rollouts with SceneDiffuser, we simply assume that all the agents valid at the current step will remain valid in the future, while setting any future traffic light features as invalid. We also compare with the Intelligent Driver Model (*IDM*) model. To set the routes for IDM to drive for each agent, we start with each agent's initial location and randomly select a valid path with the lane graph on the map. For validity, we set all the agents' future validity to remain the same as their current validity. In our main experiment, we test each possible combination of planner and world model using the three methods.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Trip-level Traffic Simulation Setup", "weight": 1.0} -->

## Valid # Entering # Exiting Entering Exiting Offroad Collision Average TL TL World Model Planner Agents Agents Agents Distance Distance Rate Rate Speed Violation Transition Composite IDM IDM 0.4028 0.6357 0.5125 0.3780 0.5253 0.3578 0.3652 0.6570 - - 0.4793 SceneDiffuser IDM 0.5701 0.7027 0.5767 0.3830 0.3296 0.2765 0.3778 0.6213 - - 0.4797 SceneDiffuser++ IDM 0.3132 0.1947 0.2059 0.1620 0.1549 0.2428 0.4361 0.5908 0.1582 0.0589 0.2878 IDM SceneDiffuser 0.2941 0.7331 0.7279 - - 0.0846 0.1017 0.4917 - - - SceneDiffuser SceneDiffuser 0.4532 0.7114 0.6275 - 0.2759 0.2056 0.3217 0.4036 - - -

<!-- chunk {"id": "body-0031", "role": "body", "section": "Trip-level Traffic Simulation Setup", "weight": 1.0} -->

Metrics For long rollouts, we end up with significant divergence between the logged scene and the propagated scene rollout. Accordingly, it does not make sense to constrain the simulation to adhere closely to the logged data, as done in WOSAC. We also have no 1:1 correspondence between agents, as agents may enter and exit the scene freely.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Trip-level Traffic Simulation Setup", "weight": 1.0} -->

We use a sliding evaluation window over temporal segments of our long-duration rollouts and ensure that each window has the same temporal length as the log scenario. Then, at each temporal window, we collect the simulated metric value (e.g., number of valid agents) from all simulated scenarios to a list of sim metrics. We also collect all the metric values for the log data to a list of log metrics. We fit two histograms to the sim and log metric values. To measure the realism of the sim features, we compute the Jensen--Shannon (JS) Divergence between these histograms. Lower divergence between histograms indicates more realistic simulated scenarios. Then we compute the mean value over all the divergence values for all windows.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Trip-level Traffic Simulation Setup", "weight": 1.0} -->

Here we introduce the features over which we compute distributional metrics in our experiments: 1) *\# Valid Agents*: the number of agents that have at least one timestep that is valid in the scenario window; 2) *\# Entering/Exiting Agents*: the number of agents that are inserted or removed during the scenario window, respectively; 3) *\# Entering/Exiting Distance*: the distance to the AV of the entering or exiting agents at the first or last valid timestep in the scenario, respectively; 4) *Offroad Rate*: the fraction of all valid agents located offroad (e.g., in parking lots); 5) *Collision Rate*: the fraction of all valid agents that ever collide with other agents; 6) *Average Speed*: the average speed for all the valid agents in the scenario window; 7) *TL Violation*: the fraction of all valid agents that violate traffic light rules; 8) *TL Transition*^11^1 For TL Transition, we directly compute the divergence between log and sim transition probability matrices computed over all scenarios.: the transition probability between different traffic light states (e.g., from red to

<!-- chunk {"id": "body-0034", "role": "body", "section": "Trip-level Traffic Simulation Setup", "weight": 1.0} -->

green). Finally, we compute a Composite score that is the average of all the metrics.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Trip-level Traffic Simulation Setup", "weight": 1.0} -->

Simulation Configuration We follow the "Full AR" inference scheme of SceneDiffuser. We vary two key simulation parameters: 1) \# rollout steps: the total number of timesteps to rollout, and 2) \# replan steps: the number of timesteps between each planner / world model replanning. The smaller the \# replan steps, the more frequently the planner and world model are executed and interact with each other. In our main experiments, we set \# rollout steps = 600 (60 seconds @ 10Hz) and \# replan steps = 40, but we also explore the effects of replan frequencies in Sec. 4.3. Please refer to the Appendix for training and model details.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Trip-level Traffic Simulation Setup", "weight": 1.0} -->

## Rollout # Replan # Valid # Entering # Exiting Entering Exiting Offroad Collision Average TL TL Steps Steps Agents Agents Agents Distance Distance Rate Rate Speed Violation Transition Composite 600 10 0.3463 0.2308 0.2199 0.0952 0.1231 0.1581 0.3118 0.2681 0.1526 0.0584 0.1867 600 20 0.3286 0.2211 0.2165 0.0910 0.1030 0.1729 0.3702 0.2872 0.1539 0.0448 0.1937 600 80 0.2775 0.1853 0.1840 0.1522 0.1356 0.1461 0.4478 0.3204 0.1845 0.0668 0.2102 300 40 0.2526 0.1947 0.1860 0.1195 0.1075 0.1165 0.4128 0.2687 0.1579 0.0396 0.1936 1200 40 0.3457 0.2268 0.2259 0.1195 0.1129 0.1950 0.4172 0.3284 0.1715

<!-- chunk {"id": "body-0037", "role": "body", "section": "Trip-level Traffic Simulation Setup", "weight": 1.0} -->

## Valid # Entering # Exiting Entering Exiting Offroad Collision Average TL TL Prediction Mode Agents Agents Agents Distance Distance Rate Rate Speed Violation Transition Composite Hard Clipping 0.4927 0.4776 0.4094 0.1156 0.1245 0.0992 0.2602 0.2664 0.2099 0.0429 0.2498 Hard-Validity Clipping 0.5963 0.6510 0.5502 0.1741 0.1641 0.2072 0.2830 0.2780 0.2379 0.0435 0.3185 No Clipping 0.2426 0.2035 0.2139 0.1425 0.1029 0.3026 0.6697 0.3685 0.3123 0.1044 0.2663 Soft Clipping 0.3053 0.2120 0.2085 0.1183 0.1094 0.1595 0.4194 0.3061 0.1625 0.0448 0.2046
Table 3: Controlled evaluation of SceneDiffuser++ inference time validity decoding strategies, as measured by JS Divergence (↓).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Main Results", "weight": 1.0} -->

We show the main result of trip-level traffic simulation in Table. We group different experiment settings by which planner is used, and compare the metric results for the rollouts using different world models. Note that some entries are not available in this table. Because SceneDiffuser and IDM do not insert agents into the scene after the first scenario window, their Entering Distance and Exiting Distance results are poor, as expected; accordingly, when using SceneDiffuser Planner, IDM and SceneDiffuser world models, we don't report their entering distance in Table.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Main Results", "weight": 1.0} -->

Our model achieves significantly better performance in all metrics that relate to agent insertion and removal. For example, when we use IDM as the planner, using SceneDiffuser++ as the world model leads to much more realistic distributions of the number of valid, entering and exiting agents, as well as entering and exiting agents' distances. These results indicate that SceneDiffuser++ yields superior performance for predicting when and where to insert and remove agents. In contrast, using IDM or SceneDiffuser models leads to much higher divergence between real and simulated distributions. This result shows it is necessary to predict agent validity for trip-level simulation.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Main Results", "weight": 1.0} -->

We observe that using our model as a world model leads to, in aggregate, better Average Speed likelihood of the scenario. This is mainly due to the fact that our model is able to predict realistic agent insertion and removal. When agents are able to dynamically appear and exit the scenario, we allow the model to focus more on realistic agent behaviors, e.g. their speed. On the other hand, when the model has to predict features for all the agents that appear in the current step in the future, it has to maintain all the agents' proximity to the AV. Consequently, for SceneDiffuser, we observe all the agents tend to become static during trip-level simulation. We show this effect in Figure.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Main Results", "weight": 1.0} -->

We also note that the Offroad Rate and Collision Rate of our model when used as a world model is worse than that of using IDM and SceneDiffuser. There are a few reasons for this performance: First, during rollout, SceneDiffuser++ will insert agents into the scenario, regardless of how the planner drives before the next replan step. Therefore, it is possible that SceneDiffuser++ will insert agents onto the route of the planner in future steps. However, if no agents are inserted in the scenario (for IDM and SceneDiffuser), all the agents will follow their historic trajectories and drive on safe routes, meaning collisions are less likely. We show in Table that with more frequent replanning, our model leads to a much better collision rate metric. Additionally, we found that SceneDiffuser++ tends to insert a large amount of agents in parking lots that stay parked. These generated parked agents lead to worse offroad metrics.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Additional Analysis", "weight": 1.0} -->

Inference-time Clipping In Table, we present an ablation on soft vs. hard vs. hard-validity clipping for generating sparse tensors. We observe that only soft clipping of features leads to favorable distributions of the number of valid, entering and exiting agents. This indicates that any hard clipping with the validity value on the feature will render the model unable to reflect the agent validity distribution. In addition, we also show the results of a model trained to directly predict invalid agents' features to be 0, and not using clipping during inference (third row), but find this method leads to a higher collision rate, offroad rate, and TL violation rate, along with inferior TL transitions, demonstrating unstable feature prediction values.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Additional Analysis", "weight": 1.0} -->

Simulation Configurations In Table, we compare the results when using SceneDiffuser++ as both world model and planner under different \# rollout steps and \# replan steps.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Additional Analysis", "weight": 1.0} -->

We first show a comparison of different replan steps in the first three rows. We observe that: 1) with more frequent replanning (smaller \# replan steps), our model achieves better Collision Rate and Average Speed. This is because when the world model and planner can interact more frequently, they are more reactive to each other's behavior. 2) with less frequent replanning (larger \# replan steps), our model leads to better agent insertion and removal behavior. With less frequent replanning, the world model has more timesteps to control into the future, which allows SceneDiffuser++ to better plan when and where to insert agents over the full sequence. On the other hand, with a high replanning rate, only agents that will be predicted to enter into the scenario in the first few timesteps will be inserted, leading to an inferior distribution of agent validity.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Additional Analysis", "weight": 1.0} -->

In the next three rows, we show the ablation with the same replan frequency, but different planning horizons, from 30 seconds to 300 seconds. We observe that overall, the realism metrics drop when the model is rolled out over longer horizons. This is mainly due to error from the autoregressive rollout aggregating over time when rolling out over long horizons. Note that although the realism of the number of entering and exiting agents degrades over time, the respective entering or exiting distances stay quite stable. This might indicate that the aggregated error affects agent insertion timing more than insertion position.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Additional Analysis", "weight": 1.0} -->

Metric Window Curves In Fig., we plot the values of two metrics in Table over simulation timesteps for all world model methods using SceneDiffuser++ as planner. Our model achieves the best performance over all timesteps.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Additional Analysis", "weight": 1.0} -->

Qualitative Results In Fig. we show examples from 60-second rollouts of our model vs. SceneDiffuser, where we uniformly sample 5 frames from the total 600 steps of each rollouts. For both our model and SceneDiffuser, we roll out using the same model for both world model and planner. It is obvious that our model achieves a realistic trip-level rollout across a large map area with dynamic traffic lights, while SceneDiffuser gets stuck in the starting location, as seen in Figure. This is mainly due to two reasons: 1) SceneDiffuser does not predict future traffic light location and states, leading to confusion of the AV in the intersection without any traffic lights. 2) SceneDiffuser does not model agents exiting the scenario, therefore it is forced to keep all the agents within the visible range of the AV. Note how the agents in the bottom of the scenario were forced to unrealistically stop in order to keep themselves in the scenario. In comparison, SceneDiffuser++ deals with these issues with a unified model and makes trip-level simulation possible.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Additional Analysis", "weight": 1.0} -->

Next, we display realistic generated agent behaviors. In Fig. (a) we show that agents inserted into a parking lot can realistically navigate onto the main road and merge into traffic. Fig. (c) and Fig. (d) show that inserted agents comply with traffic light rules, indicating high realism of agent and traffic light interaction. Lastly, Fig. (b) shows generated agents can be inserted far from the AV.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Additional Analysis", "weight": 1.0} -->

Validity Prediction We visualize the predicted agent validity through 600 steps in Fig., comparing our model's output, the logged 'ground truth', and the pattern that IDM and SceneDiffuser both produce. Our model is able to insert and remove agents with realistic validity patterns that are very close to the ground-truth in the first 91 steps. On the other hand, IDM and SceneDiffuser only follow the last-step history validity, leading to a quite unnatural validity pattern. Finally, note that our model is able to insert a new agent to an agent row that was previously occupied by a removed agent (e.g., the last few rows), as long as the previous agent was removed longer ago than SceneDiffuser++'s history horizon. In this way, our method is able to insert any number of agents beyond the total number of agent indices by reusing any agent index where an agent was removed.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Additional Analysis", "weight": 1.0} -->

Traffic Light Transition We visualize the traffic light state transition probability matrix in Figure, where left is the logged ground-truth and right is SceneDiffuser++ prediction. In these figures, along the y-axis is the starting traffic light state and along the x-axis the ending traffic light state. We observe that SceneDiffuser++ traffic light state predictions rigorously follow the ground-truth state transition probability. Note that we remove all the state self-transitions (the diagonal entries) for clearer visualization.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have introduced SceneDiffuser++, a scene-level diffusion prior designed for city-scale traffic simulation. SceneDiffuser++ is a unified world model that enables trip-level long simulations with dynamic agent generation, occlusion reasoning, removal and traffic light simulation. We demonstrate SceneDiffuser++ has strong performance for long-term traffic simulation. We hope our work leads to more realistic trip-level simulation to improve AV safety.
