<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

GPUDrive: Data-driven, Multi-agent Driving Simulation at 1 Million FPS

Topics include Reinforcement learning, Multi-agent systems, Datasets, Optimization, Planning, Learning, GPUDrive.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Multi-agent learning algorithms have been successful at generating superhuman planning in various games but have had limited impact on the design of deployed multi-agent planners. A key bottleneck in applying these techniques to multi-agent planning is that they require billions of steps of experience. To enable the study of multi-agent planning at scale, we present GPUDrive. GPUDrive is a GPU-accelerated, multi-agent simulator built on top of the Madrona Game Engine capable of generating over a million simulation steps per second. Observation, reward, and dynamics functions are written directly in C++, allowing users to define complex, heterogeneous agent behaviors that are lowered to high-performance CUDA. Despite these low-level optimizations, GPUDrive is fully accessible through Python, offering a seamless and efficient workflow for multi-agent, closed-loop simulation. Using GPUDrive, we train reinforcement learning agents on the Waymo Open Motion Dataset, achieving efficient goal-reaching in minutes and scaling to thousands of scenarios in hours. We open-source the code and pre-trained agents at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Multi-agent learning has been impactful across a wide range of fully cooperative and zero-sum games. However, its impact on multi-agent planning for settings that mix humans and robots has been muted. In contrast to the ubiquity of multi-agent learning-based agents in zero-sum games, multi-agent planners for most practical robotic systems are not derived from the output of game-theoretically sound learning algorithms. While it is hard to characterize the space of deployed planners since many of them are proprietary, the majority likely use a mixture of collected data for the prediction of human motion and hand-tuned costs. These are then fed into a cost-based trajectory optimizer or into a planner based on imitation learning. This approach has been highly effective in scaling up real-world autonomy but can struggle with reasoning about long-term behavior, contingency planning, and interaction with humans in rare, complex scenarios.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The divergence in preferred technique between these two domains is partially the outcome of two distinct, challenging components of real-world multi-agent planning. First, unlike zero-sum games, it is necessary to play a human-compatible strategy that is difficult to identify without data. Second, generating the billions of samples needed for multi-agent learning algorithms is difficult with existing simulators. The former challenge is difficult for multi-agent learning since there is not a clear equilibrium concept that algorithms should be pursuing. The latter problem is a challenge for simulators since it is difficult to simulate embodied multi-agent environments at appropriately high rates.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address these challenges and unlock multi-agent learning as a tool for generating capable self-driving planners, we introduce GPUDrive. GPUDrive is a simulator intended to mix real-world driving data with simulation speeds that enable the application of sample-inefficient but effective RL algorithms to the design of autonomous planners. GPUDrive runs at over a million steps per second on both consumer-grade and datacenter-class GPUs and has a sufficiently light memory footprint to support hundreds to thousands of simultaneous worlds (environments) with hundreds of agents per world. GPUDrive supports the simulation of a variety of sensor modalities, from LIDAR to a human-like view cone, enabling GPUDrive to be used for studying the effects of different sensor types on resultant agent characteristics. Finally, GPUDrive takes in driving logs and maps from existing self-driving datasets, enabling the mixing of tools from imitation learning with reinforcement learning algorithms. This enables the study of both the development of autonomous vehicles and the learning of models of human driving, cycling, and walking behavior.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our contributions are: We provide a multi-agent, GPU-accelerated, and data-driven simulator that runs at over a million steps per second (Section 4.1). Our simulator provides a testbed: Investigating the capability of learning algorithms to solve challenges related to self-play or autonomous coordination.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Researching the effects of limited or human-like perception on agent behavior.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide gymnasium environments in both torch and jax that can be easily configured with standard open-source multi-agent RL and imitation learning libraries. Additionally, we open-sourced two policy-gradient training loops that can be readily used to develop agents.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We release implementations of tuned RL algorithms that can process $30$ million steps of experience per hour on consumer-grade GPUs. These can be used to train $95$% goal-reaching agents across 1000 different multi-agent scenarios in 15 hours on relatively accessible hardware.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We open-source these strong driving baseline agents that achieve 95% of their goals on a subset of scenes. These are integrated into the simulator so that the simulator comes with default, reactive agents.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Frameworks for batched simulators", "weight": 1.0} -->

There are various open-source frameworks available that support hardware-accelerated reinforcement learning environments. These environments are generally written directly in an acceleration framework such as Numpy, Jax, or Pytorch. In terms of multi-agent accelerated environments, standard benchmarks include JaxMARL, Jumanji, VMAS Gigastep which primarily feature fully cooperative or fully competitive tasks. Each benchmark requires the design of custom accelerated structures per environment. In contrast, GPUDrive focuses on a mixed motive setting and is built atop Madrona, an extensible ECS-based framework in C++, enabling GPU acceleration and parallelization across environments. Madrona comes with vectorization of key components of embodied simulation such as collision checking and sensors such as LIDAR. GPUDrive can support hundreds of controllable agents in more than 100,000 distinct scenarios, offering a distinct generalization challenge and scale relative to existing benchmarks. Moreover, GPUDrive includes a large dataset of human demonstrations, enabling imitation learning, inverse RL, and combined IL-RL approaches.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Simulators for autonomous driving research and development", "weight": 1.0} -->

Table 1 shows an overview of current simulators used in autonomous driving research. The purpose of GPUDrive is to facilitate the systematic study of behavioral, coordination, and control aspects of autonomous driving and multi-agent learning more broadly. As such, visual complexity is reduced, which differs from several existing simulators, which (partially) focus on perception challenges in driving. Driving simulators close to GPUDrive in terms of either features or speed include MetaDrive, nuPlan, Nocturne, and Waymax which all utilize real-world data. Unlike MetaDrive and nuPlan, our simulator is GPU-accelerated. Like GPUDrive, Waymax is a JAX-based GPU-accelerated simulator that achieves high throughput through JIT compilation and efficient use of accelerators. With respect to Waymax, our simulator supports a wider range of possible sensor modalities (Section 3.2) including LIDAR and human-like views, can scale to nearly thirty times more worlds (see Section 4.1), and comes with performant reinforcement learning baselines. However, it does not currently come with reactive IDM agents like Waymax though it does come with pre-trained simulated agents based on RL policies.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Driving agents in simulators and algorithms", "weight": 1.0} -->

Existing simulators often feature baseline agents for interaction, such as low-dimensional car following models that describe vehicle dynamics through a limited set of variables or parameters. Rule-based agents exhibit predetermined behaviors, like car-following agents such as the IDM model, or parameterized behavior agents like CARLA's TrafficManager. Some simulators offer recorded human driving logs for interaction through replaying the human driving logs. Additionally, certain simulators provide learning-based agents, leveraging reinforcement learning techniques. In GPUDrive, we provide both human driving logs and high-performing reinforcement learning agents.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Simulation Engine", "weight": 1.0} -->

Learning to safely navigate complex scenarios in a multi-agent setting requires generating many billions of environment samples. To feed sample-hungry learning algorithms, GPUDrive is built on top of Madrona, an Entity-Component-State system designed for high-throughput reinforcement learning environments. In the Madrona framework, multiple independent worlds (each containing an independent number of agents^††^†In the Waymo Open Motion Dataset, an agent constitutes a vehicle, cyclist, or pedestrian. ) are executed in parallel on an accelerator via a shared engine.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Simulation Engine", "weight": 1.0} -->

However, the simulation of driving poses a unique set of challenges which require careful technical design choices to solve. First, road objects, such as road edges and lane lines are frequently represented as polylines (i.e. connected sets of points). These polylines can consist of hundreds of points as they are sampled at every $0.1$ meters, leading to even small maps having upwards of tens of thousands of points. This can blow up the memory requirements of each world as well as lead to significant redundancy in agent observations. Second, the large numbers of agents and road objects can make collision checking a throughput bottleneck. Finally, there is immense variability in the number of agents and road objects in a particular scene. Each world allocates memory to data structures that track its state and accelerate simulation code. Though independent, each world incurs a memory footprint proportional to the maximum number of agents across all worlds. In this way, the performance of GPUDrive is sensitive to the variation in agent counts across all the worlds in a batch.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Simulation Engine", "weight": 1.0} -->

These challenges are partially resolved via the following mechanisms. First, a primary acceleration data structure leveraged by GPUDrive is a Bounding Volume Hierarchy (BVH). The BVH keeps track of all physics entities and is used to easily exclude candidate pairs for collisions. This allows us to then run a reduced-size collision check on potential collision candidate pairs. The use of a BVH avoids invoking a collision check that would otherwise always be quadratic in the number of agents in a world. Secondly, we observed that a lot of the lines in the geometry of the roads are straight. This allows us to omit many intermediate points while only suffering a minor hit in the quality of the curves. We apply a polyline decimation algorithm (Visvalingham-Whyatt Algorithm) to approximate straight lines and filter out low-importance points in the polylines. With this modification, we can reduce the number of points by 10-15 times and significantly improve the step times while decreasing memory usage. Finally, rather than allocate memory for the maximum number of agents in a scene (as is likely necessary in frameworks like Jax), we only allocate memory equal to the actual number of instantiated agents.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Simulator features", "weight": 1.0} -->

We provide an overview of some of the pertinent simulator features as well as sharp edges and limitations of the simulator as a guide to potential users.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Dataset", "weight": 1.0} -->

GPUDrive represents its map as a series of polylines and does not require a connectivity map of the lanes. As such, it can be made compatible with most driving datasets given the pre-processing of the roads into the polyline format. Currently, GPUDrive supports the Waymo Open Motion Dataset (WOMD) which is available under a non-commercial license. We show four representative example scenarios from the WOMD in Figure 2. The WOMD consists of a set of over 100,000 multi-agent traffic scenarios, each of which contains the following key elements: 1) Road map - the layout and structure of a road, such as a highway or parking garage. 2) Logged human trajectories from vehicles, cyclists, and pedestrians. 3) Road objects, such as stop signs and crosswalks. Figure 7 depicts an example of an intersection traffic scenario as rendered in GPUDrive.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Sensor modalities", "weight": 1.0} -->

GPUDrive supports a variety of observation spaces intended to enable heterogeneous types of agents. Fig. 7 depicts the three types of supported state spaces. The first mode is somewhat unphysical in which all agents and road objects within a fixed radius are observable to the agent. This mode is intended primarily for debugging and quick testing, enabling a user to minimize the amount of partial observability in the environment. The other two modes are based on a GPU-accelerated LIDAR scan, representing what an autonomous vehicle would be able to see and what a human would likely be able to see respectively. Both modes are based on casting LIDAR rays; to model human vision we simply restrict the LIDAR rays to emanate in a smaller, controllable-sized cone that can be rotated through an action corresponding to head rotation. Note that since all objects are represented as bounding boxes of fixed height, the LIDAR observations are over-conservative as, in reality, it is frequently possible to see over the hoods of cars as their height is lower than the body of the rest of the car.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Agent dynamics", "weight": 1.0} -->

By default, agents are stepped using a standard Ackermann bicycle model (Details in Appendix B) with actions corresponding to steering and acceleration. This model enables the dynamics of objects to be affected by their length, creating different dynamics for small cars as opposed to large cars like trucks. However, this model is not fully invertible which can make it challenging to use as a model for imitation learning. To enable full invertibility for imitation learning, we also support the simplified bicycle model, taken from Waymax, which is a double-integrator in the position and velocity and updates its yaw as: where $\theta$ is the yaw, $s$ is the steering command, $v$ is the velocity, and $a$ is the acceleration at time $t$ respectively. $\Delta t$ is the timestep. This model is always invertible given an unbounded set of steering and acceleration actions but is independent of the vehicle length. See the appendix for full details on the models.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Agent dynamics", "weight": 1.0} -->

Note that this model does not factor in the length of the car, causing both long and short objects to have identical dynamics. However, we have observed that computing the expert actions and then using them to mimic the expert trajectory under this model leads to lower tracking error than the default bicycle model.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Rewards", "weight": 1.0} -->

All agents are given a target goal to reach; this goal is selected by taking the last recorded position in the vehicle's logged trajectory. A goal is reached when agents are within some configurable distance $\delta$ of the goal. By default, agents in GPUDrive receive a reward of $1$ for achieving their goal and otherwise receive a reward of $0$. There are additional configurable collision penalties or other rewards based on agent-vehicle distances or agent-road distances though these are not used in the experiments reported in this work.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Termination conditions", "weight": 1.0} -->

We terminate an agent's episode when they achieve their goal position and support an option to also terminate the episode if the agent collides. As it is not clear where an agent should go next after it reaches its goal, we simply remove it from the scene afterwards (we note that an alternative might be to generate a new goal for the agent to drive to). Car and cyclist agents are considered to be in collision when they drive through a road edge while pedestrian agents are allowed to cross road edges.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Environment interface", "weight": 1.0} -->

As GPUDrive is implemented in C++, we provide a Pythonic interface through nanobind. We create environments for both torch and jax that conform to the Gymnasium API so users can use the simulator entirely through Python if they prefer.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Available driving simulation agents", "weight": 1.0} -->

We use reinforcement learning to train a set of agents that reach their goals $95$% of the time on a subset of $1000$ training scenes. While this number is far below the capability of human drivers, these agents are reactive in a distinct fashion from parametrized driver models in other simulators. In particular, many logged-data simulators construct reactivity by having the driver follow along its logged trajectory but decelerate if an agent passes in front of it. In contrast, these agents can maneuver and negotiate without remaining constrained to a logged trajectory. These trained agents are extremely aggressive about reaching their goals and can be used as an out-of-distribution test for proposed driving agents. The training procedure and more details can be found in Section 4.2.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Simulator sharp-edges", "weight": 1.0} -->

We note the following limitations of the benchmark: Absence of a map. The current version of the simulator does not have a well-defined notion of lanes or a higher-level road map which makes it challenging for algorithmic approaches that require maps. The absence of this feature also makes it challenging to define rewards such as \"stay lane-centered.\" Convex objects only. Collision checking relies on the objects being represented as convex objects.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Simulator sharp-edges", "weight": 1.0} -->

Unsolvable goals. Due to incorrect labels of some road points in the Waymo dataset, such as an exit to a parking lot being labeled as an impassable road edge, some agent goals (roughly 2%) are unreachable. For these agents, we default them to simply replaying their logged trajectory and do not treat them as agents.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Simulator sharp-edges", "weight": 1.0} -->

Initialization modes: In many scenarios, a significant portion of agents (25-75%) are already at or very close to their goal positions, such as parked cars. To highlight the difficulty of controlling agents, GPUDrive supports different initialization modes. By default, the initialization mode is set to "all nontrivial" meaning that only agents more than 2 meters away from their target positions are considered controllable. Note that while this sharply reduces the number of agents in the scene, it more accurately represents actual driving challenges.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Simulator performance", "weight": 1.0} -->

The following Sections describe the simulator speed. Section 4.1 first shows the raw simulator speed and peak goodput (throughput achieved by the valid number of agents in a scene). Section 4.2 then investigates the impact on reinforcement learning workflows by evaluating the time it takes to train reinforcement learning agents through Independent PPO (IPPO), a widely used multi-agent learning algorithm. The performance results here are from IPPO implemented with PufferLib. A slower IPPO implementation based on Stable Baselines 3 is also available in the repo.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Simulation speed", "weight": 1.0} -->

Since scenarios contain a variable number of agents, we introduce a metric called Agent Steps Per Second (ASPS) to measure the sample throughput of the simulator. We define the ASPS as the total number of agents across all worlds in a batch that can be fully stepped in a second: where $A_{k}$ is the set of agents in the $k^{th}$ world, $S$ is the number of steps taken, and $\Delta T$ is the number of seconds elapsed. Figure 3 examines the scaling of the simulator as the number of simulated worlds, which represents the amount of parallelism, increases. To measure performance, we sample random batches of scenarios of size equal to the number of worlds, so that every world is a unique scenario with $K$ agents. On the left-hand side of Figure 3, we compare the performance of GPUDrive to Nocturne (CPU, no parallelism), a CPU-accelerated version of Nocturne via Pufferlib (16 CPU cores) and Waymax Gulino et al..

<!-- chunk {"id": "body-0031", "role": "body", "section": "Simulation speed", "weight": 1.0} -->

Empirically, the maximum achievable ASPS of Nocturne is 15,000 (blue dotted line) though we note that additional speedups may be possible. GPUDrive achieves a peak ASPS of 2.3 million steps, which is 2 to 3 orders of magnitude faster compared to Nocturne. This performance also surpasses that of Waymax, a JAX-based simulator, where we could not run more than 16 environments in parallel due to Out of Memory (OOM) issues.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Simulation speed", "weight": 1.0} -->

In addition to the ASPS, we report another metric to indicate the number of controllable agents that are stepped per second. In the Waymo Open Motion Dataset, each scenario contains a varying number of moving agents (Examples in Figure 2). By default, our system only classifies something as a controllable agent if its movement is necessary to achieve the goal. Therefore, parked cars throughout the episode are not considered controllable agents. To illustrate what this looks like, we plot the distribution of controllable agents across a subset of scenes in Figure 3.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Simulation speed", "weight": 1.0} -->

Considering the variance of controllable agents per scene, the right-hand side of Figure 3 depicts the Controlled Agent Steps Per Second (CASPS). CASPS reflects the expected performance of our system when utilizing the Waymo Open Motion Dataset with a randomly sampled subset of scenarios. Due to the significant variability in agents throughout the dataset, the highest CASPS is notably lower than the ASPS, at around 200,000. Note that this can be improved by strategically selecting scenes, such as filtering for dense scenes with a high number of controllable agents.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Simulation speed", "weight": 1.0} -->

Lastly, we demonstrate the speed of different observation spaces in Figure 4. We observe that using LiDAR is approximately three times faster than using the radial filter observation (Details about the supported observation spaces are found in Section 3.2).

<!-- chunk {"id": "body-0035", "role": "body", "section": "End-to-end speed and performance", "weight": 1.0} -->

The purpose of GPUDrive is to facilitate research and development in multi-agent algorithms by 1) reducing the completion time of experiments, and 2) enabling academic research labs to achieve scale on a limited computing budget. Ultimately, we are interested in the rate at which a machine learning researcher or practitioner can iterate on ideas using GPUDrive. This section highlights what our simulator enables in this regard by studying the end-to-end process of learning policies in our simulator.

<!-- chunk {"id": "body-0036", "role": "body", "section": "End-to-end speed and performance", "weight": 1.0} -->

In absolute terms, the number of controlled agent steps per second for the Pufferlib PPO implementation ranges from 200K to 500K, depending on the hardware used and factors such as the number of visible road points per agent.

<!-- chunk {"id": "body-0037", "role": "body", "section": "End-to-end speed and performance", "weight": 1.0} -->

As shown in Fig. 5, GPUDrive allows us to solve scenes in minutes. Next, we investigate how the individual scene completion time, the time it takes to solve a single scenario, changes as we increase the total number of scenarios we train. In practice, it may be desirable to train agents on thousands of scenarios. Therefore, we ask whether it is feasible to fully leverage the simulator's capabilities with a single GPU.

<!-- chunk {"id": "body-0038", "role": "body", "section": "End-to-end speed and performance", "weight": 1.0} -->

Interestingly, we find that the amortized sample efficiency increases with the size dataset of scenes we train. Figure 6 shows the average completion time per scenario as we increase the dataset. For instance, using IPPO with 32 scenarios takes 2 minutes per scenario. In contrast, solving 1024 unique scenarios takes about 200 minutes, which amounts to only 15 seconds per scenario. We expect that these scaling benefits will continue as we further increase the size of the training dataset. This suggests that GPUDrive should enable effective utilization of the large WOMD dataset comprising 100,000 diverse traffic scenarios, even with limited computational resources.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Measuring remaining unsolved tasks", "weight": 1.0} -->

The Waymo Open Motion Dataset contains a total of 103,354 traffic scenarios. In this paper, we demonstrate that an agent can achieve 95% performance on a subset of 1000 scenes after 15 hours of training. Additionally, we show that the time required to solve scenarios decreases as the dataset size increases. Our analysis of the failure rates in the current best-performing policy suggests that the goal-reaching limit is around 98%, due to mislabeled road edges in the dataset, which render some goals unreachable because they are located beyond uncrossable roads. An important direction for future work is developing agents that achieve near-perfect performance, with a goal-reaching rate approaching 100% and a 0% collision rate while addressing the limitations posed by data inaccuracies in the benchmark.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we present GPUDrive, a GPU-accelerated, multi-agent, and data-driven simulator. GPUDrive is intended to help generate the billions of samples that are likely needed to achieve effective reinforcement learning for multi-agent driving planners. By building atop the Madrona Engine, we can scale GPUDrive to hundreds of worlds with potentially thousands of agents leading to throughput of millions of steps per second. This throughput occurs while synthesizing complex observations such as LiDAR. We show that this throughput has consequent implications for training reinforcement learning agents, leading to the ability to train agents to solve any particular scene in minutes and in seconds when amortized across many scenes. We release the simulator and integrated trained agents to enable further research.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Future work and simulator extensions", "weight": 1.5} -->

This paper represents an initial step toward scaling reinforcement learning for multi-agent planning in safety-critical, mixed human-autonomous settings. Several important opportunities remain for future work: Agent performance: Training agents to navigate without crashing in any scenario, matching human capabilities, remains an unresolved challenge. Currently, agents trained in GPUDrive achieve a 95% success rate in a few hours, but this still falls short of the standards we aim. Getting to 100% goal reaching performance is left for future work.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Future work and simulator extensions", "weight": 1.5} -->

Integrating multiple datasets: Future work will focus on integrating various datasets, such as NuPlan or NuScenes. This integration will enable training on data from multiple geographic locations, including Boston and Singapore. To achieve this, we need to establish a data-processing pipeline that ensures the datasets are converted into a format compatible with the simulator.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Future work and simulator extensions", "weight": 1.5} -->

Diverse realistic sim agents: We plan to extend GPUDrive by introducing a variety of simulation agents that represent a broad range of human-like behaviors. This will improve sim realism.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Reproducibility Statement", "weight": 1.0} -->

The simulator's source code and data are available at To ease reproducibility, we provide Dockerfiles to simplify setup. The experiments in the paper can be reproduced using a single file on a single A100 in 16 hours or slightly longer for less performant hardware. The data has been pulled from the Waymo Motion dataset and parsed into JSON files that are used to initialize the simulator; these are all available from Huggingface datasets.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Ethics Statement", "weight": 1.0} -->

This paper presents GPUDrive, a GPU-accelerated simulator for multi-agent learning in autonomous driving. We use publicly available datasets, such as the Waymo Open Motion Dataset, which are anonymized to protect privacy. GPUDrive is intended for research purposes and not for real-world deployment without further validation. We recognize the risks of autonomous systems and emphasize the importance of safety and fairness in their application. Although this work does not involve human participants directly, it leverages real-world data that may reflect human behavior, and we strive to avoid harm or discrimination. The codebase, pre-trained agents, and evaluation scripts are openly available to promote transparency. There are no conflicts of interest or external sponsorships affecting this research. We are committed to ethical practices in data handling, model deployment, and research integrity.
