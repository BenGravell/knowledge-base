<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research

Topics include Reinforcement learning, Multi-agent systems, Autonomous driving, Vehicles, Safety, Graphs, Datasets, Benchmarks, Online algorithms, Distributed systems, Planning, Learning, Waymax, Machine learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Simulation is an essential tool to develop and benchmark autonomous vehicle planning software in a safe and cost-effective manner. However, realistic simulation requires accurate modeling of nuanced and complex multi-agent interactive behaviors. To address these challenges, we introduce Waymax, a new data-driven simulator for autonomous driving in multi-agent scenes, designed for large-scale simulation and testing. Waymax uses publicly-released, real-world driving data (e.g., the Waymo Open Motion Dataset) to initialize or play back a diverse set of multi-agent simulated scenarios. It runs entirely on hardware accelerators such as TPUs/GPUs and supports in-graph simulation for training, making it suitable for modern large-scale, distributed machine learning workflows. To support online training and evaluation, Waymax includes several learned and hard-coded behavior models that allow for realistic interaction within simulation. To supplement Waymax, we benchmark a suite of popular imitation and reinforcement learning algorithms with ablation studies on different design decisions, where we highlight the effectiveness of routes as guidance for planning agents and the ability of RL to overfit against simulated agents.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Due to the cost and risk of deploying autonomous vehicles (AVs) in the real world, simulation is a crucial tool in the research and development of autonomous driving software. The two primary challenges of a simulator are speed and realism: we wish for a simulator to be fast in order to cost-effectively train/evaluate on many hours of synthetic driving experience, and we wish for a simulator to be diverse and realistic in terms vehicle behavior in order to minimize the sim-to-real gap, such that performance in the simulator correlates with real-world performance.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Existing work in simulation for autonomous driving has made significant progress in recent years. Simulators such as CARLA, Sim4CV and SUMMIT focus on photo-realistic rendering of driving scenarios, enabling users to train and evaluate driving solutions. However, a major simulation challenge still remains in the generation of diverse scenarios and realistic behavior for other agents (such as vehicles and pedestrians) in the scene, and as the driving field has matured, behavior challenges have been shown to be a significant bottleneck to scaling. To this end, there is still a need for simulation tools that provide (a) realistic, closed-loop simulation of agent behavior, and (b) high speed and throughput to support modern trends in machine learning that use large models and datasets.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address these challenges, we propose Waymax- a *differentiable*, *hardware-accelerated* and *multi-agent* simulator that is built using *real-world driving data* from the Waymo Open Dataset. Waymax aims to provide, within simulation, a faithful reproduction of the data and types of challenges a real autonomous driving agent would face, such as those shown in Fig. 1. Waymax simulates challenging obstacles present in urban driving, such as pedestrians and cyclists, and provides high-level route information for the ego vehicle to follow. To optimize runtime speed and facilitate rapid development, Waymax is written using JAX, which allows simulation to be run entirely on accelerators such as graphics and tensor processing units (GPUs and TPUs). To provide better simulation realism, Waymax uses diverse scenarios initialized from the Waymo Open Motion Dataset (WOMD), which contains over 250 hours of real driving data collected in dense urban environments. Waymax data loading and processing can be extended to other popular datasets without loss of generality.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our contributions are two-fold. First, we introduce the Waymax simulator, which is a multi-agent simulator for autonomous driving that is (a) hardware-accelerated, (b) provides features and routes information from real driving data, and (c) constructs scenarios upon a large and diverse dataset of real-world driving. Our second contribution is in providing a set of common benchmarks and simulated agents that allow researchers to score and benchmark their autonomous planning methods in closed-loop. We show-case the flexibility of Waymax by training behavior algorithms for an autonomous vehicle in different setups (imitation, on and off policy RL, etc) against a range of different interactive agents.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

(a) Waiting for a turn into oncoming traffic.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

(a) The route is the union of logged trajectories and driveable futures.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

(b) Reactive simulated agents stopping to avoid collision.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Simulators for Autonomous Driving", "weight": 1.0} -->

Waymax is a *differentiable*, *hardware-accelerated* and *multi-agent* simulator that is built on top of *real-world driving data*. We compare our work to other related publicly available simulators in Table 1. The closest works to ours are multi-agent autonomous driving simulators which use real driving data to initialize scenarios and logged behavior, such as Nocturne, MetaDrive, and nuPlan. In comparison, our simulator is designed to support hardware-accelerated training, the agent models can be connected in-graph for training and inference, and the simulation is differentiable. We provide a full set of features including pedestrians, cyclists, and traffic lights available in WOMD, and the inferred routes for goal-conditioned policy and progress metrics. Additionally reactive sim agent models are provided to facilitate realistic simulation. TorchDriveSim is the only public simulator that supports differentiable simulation for in-graph acceleration. In comparison, we provide rich and diverse real-world human expert driving data from WOMD.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Simulators for Autonomous Driving", "weight": 1.0} -->

It is worth noting that the driving policy modeling problem is primarily focused on behavior than perception, thereby, we do not intend to support sensor simulation, such as, which represents another important research area for autonomous driving perception.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Learning-based Driving Agents", "weight": 1.0} -->

In the context of autonomous driving, open-loop imitation learning (IL), known as behavior cloning (BC), has been applied to predict driving behaviors of other road users as well as the ego vehicle. It is widely known that BC suffers from covariate shift and causal confusion. Closed-loop methods including adversarial imitation learning and reinforcement learning (RL) methods have been proposed to address these challenges by learning from feedback and explicit hand designed rewards in the simulator. Despite the excitement of machine learning as an avenue towards devising autonomous driving policies, benchmarking different learned policies on large scale real world datasets remains a challenge. To enable accelerated and effective autonomous driving agents research, Waymax enables standard training and evaluation workflows and reliable benchmarking in both open and closed-loop settings; we also provide the implementation of a representative set of IL and RL baselines and report their performance against a standard set of metrics on Waymax as references.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Simulator Features", "weight": 1.0} -->

In this section, we give an overview of the features of Waymax and its interface to the user. Waymax is a simulator that supports controlling arbitrary number of objects in a scene. A primary goal of Waymax is to initialize from real-world driving scenarios to model complex interactions between vehicles, pedestrians, and traffic lights, and following a goal or route provided by high-level planner. Additionally, Waymax is designed to be both fast and flexible - each component discussed in this section can easily be modified or replaced by an user to suit their own project needs. We discuss the scenarios and datasets in Sec. 3.1, state representation in Sec. 3.2, and the dynamics and action representation in Sec. 3.3. Waymax includes a suite of common metrics described in Sec. 3.4, and several options for modeling the behavior of dynamic objects (vehicles and pedestrians) in the scene, outlined in Sec. 3.5.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Scenarios and Datasets", "weight": 1.0} -->

In contrast to simulators that generate synthetic scenarios (e.g. CARLA ), Waymax utilizes real-world driving logs to instantiate driving scenarios, and runs for a fixed number of steps. We provide default support for the Waymo Open Motion Dataset (WOMD), which includes over $100,000$ trajectories snippets and 7.64 million unique objects to interact or control. Each trajectory snippet is 9 seconds recorded with 0.1 Hz. The trajectory contains pose and velocity information for all objects in a scene, including the autonomous vehicle (AV), other vehicles, pedestrians, and cyclists. For each scenario, we take the static information such as the road graph and initialize dynamic objects using the first second of logged information. Then, agent models (described in Sec. 3.5) will be used to control the dynamic objects such as pedestrians and the other vehicles through the simulation steps. Note importantly, users can inject multiple agent models and dynamics model to Waymax environment where each model can control multiple objects.

<!-- chunk {"id": "body-0015", "role": "body", "section": "State and Observation spaces", "weight": 1.0} -->

The first component of defining autonomous driving as a sequential control problem is defining the state space. We include two types of data in the state: dynamic data which can change over the course of an episode and across scenarios, and static data which remains the same during an episode but varies across scenarios. The dynamic data in the state consists of the position, rotation, velocity, and bounding box dimensions for all vehicles, cyclists, and pedestrians in a scene, along with the color of traffic light signals (red, yellow, green). The static data includes the road and lane boundaries sampled as a 3D point-cloud (known as the "roadgraph"), as well as on-route and off-route paths for the ego vehicle. Each agent views the simulator state through a user-defined observation function, which can induce *partial observability*. We provide a default observation function that transforms the location of all other vehicles to the agent's own coordinate frame, and sub-samples the roadgraph via distance.

<!-- chunk {"id": "body-0016", "role": "body", "section": "On-Route and Off-Route Paths", "weight": 1.0} -->

We augment each scenario with feasible paths that the AV could take from its initial position. A path is represented as a sequence of points, which are a subset of the roadgraph points. Each path is computed by performing a depth-first-search traversal of the roadgraph from the starting position. Together, these paths describe all the ways in which the AV can legally drive in the scenario. Similar to the "road-route\", a path is considered on-route if it follows the same road as the AV's logged trajectory. The remainder of the paths that are not on-route are deemed to be off-route. Fig. 1(a) ‣ Figure 2 ‣ 1 Introduction ‣ Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research") gives an example of on-route paths. These paths are useful for computing metrics as well as developing goal-conditioned planning and interactive agents.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Object Dynamics", "weight": 1.0} -->

The object dynamics defines what 'actions' an object would expect and how its state would evolve given an action. Waymax allows the user to define a dynamics model and provides several pre-defined options for controlling the physical dynamics of vehicles in simulation: 1) the delta action space, which is suitable for all types of objects, uses position difference (the delta term $\Delta x,\Delta y,\Delta\theta)$) between two consecutive states; and the bicycle action space ($(a,\kappa)$, which is only for vehicles, uses acceleration and steering curvature). The equations defining these dynamics can be found in Appendix A.1.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Metrics", "weight": 1.0} -->

Waymax provides a set of intuitive metrics to evaluate the ego vehicle as well as simulated agents for safety and correctness of behavior (such as obeying traffic rules, not colliding), as well as comfort and progress. All metrics in Waymax are computed in closed-loop, meaning that they are computed by running the agent in simulation, rather than in open-loop, where metrics are computed on a per-timestep basis without feedback from simulation.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Route Progress Ratio", "weight": 1.0} -->

The route progress ratio measures how far the ego vehicle drives along the goal route compared to the logged trajectory. At time step $t$, this metric associates the vehicle's position to the closest point $x{(t)}$ in an on-route path. It then computes the distance along the path from the start of the path to $x{(t)}$, denoted as $d_{x{(t)}}$. The route progress ratio is then defined as $\frac{d_{x{(t)}} - d_{p}}{d_{q} - d_{p}}$, where $d_{p}$ and $d_{q}$ are the distances along the path to the initial and final positions of the vehicle's logged trajectory, respectively. Since the vehicle can continue driving after reaching its destination, this ratio could be greater than 1.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Off-Route", "weight": 1.0} -->

The off-route metric is a binary value indicating if the vehicle is following an on-route path. If the vehicle is sufficiently closer to an off-route path than on-route path or it is far enough away from an on-route path, it is considered off-route.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Off-Road", "weight": 1.0} -->

The off-road metric triggers if a vehicle drives off the road. This is measured relative to the oriented roadgraph points. If a vehicle is on the left side of an oriented road edge, it is considered on the road; otherwise the vehicle is considered off-road.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Collision", "weight": 1.0} -->

The collision metric is a binary metric that measures if the vehicle is in collision with another object in the scene. For each pair of objects, if the 2D top-down view of their bounding boxes overlap in the same timestep, they are considered in collision.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Kinematic Infeasibility Metric", "weight": 1.0} -->

The kinematic infeasibility metric computes a binary value of whether a transition is kinematically feasible for the vehicle. Given two consecutive states, we first estimate the acceleration and steering curvature using the inverse kinematics defined in Appendix A.1, and check if the values are out of bounds. We empirically set the limit of acceleration magnitude to be 6 $m/s^{2}$ and the steering curvature magnitude to be 0.3 $m^{- 1}$. In order to determine these empirically, we fit the logged trajectories of the ego agent with our steering and acceleration action space. We then chose the limits to be roughly the maximum (rounding up for some slack) of the values we observed in the logs.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Displacement Error", "weight": 1.0} -->

The average displacement error metric (ADE) measures how far the simulation deviates from logged behavior. It is defined as the L2 distance between each object's current XY position and the corresponding position recorded in the logs at the current timestep, averaged across all timesteps.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Simulated Agent Behavior", "weight": 1.0} -->

An important part of constructing a simulator for autonomous driving is realistic behavior for simulated agents other than the AV. Waymax, as a multi-agent simulator, gives the user the ability to control the behavior of all objects in simulation. This allows the user to control agents with any model of choice, such as learned behavior models. However, to support training AV agents out-of-the-box, Waymax also includes a rule-based reactive agent model based on the intelligent driver model (IDM). IDM describes a rule for updating the acceleration of a vehicle to avoid collisions based on the proximity and relative velocity of the vehicle to the object directly in front of the vehicle, as demonstrated in Fig. 1(b) ‣ Figure 2 ‣ 1 Introduction ‣ Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research"). The IDM agent in Waymax follows the logged path that is recorded in the data, but uses IDM to adjust the speed profile to avoid collisions and accelerate on free roads.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Software API", "weight": 1.0} -->

We now outline the Waymax software components and interfaces. In order to support a wide variety of research workflows, Waymax is designed as a collection of inter-operable libraries while maintaining fast simulation speed. The main libraries comprise of a set of common data-structures, a distributed data-loading library, simulator components such as metrics and dynamics, and a Gym-like environment interface. Each component of the simulator can be modified, replaced, or used standalone by the user. In this manner, users who only need one component of Waymax (e.g. only metrics, or only data loading), or who wish to significantly modify the behavior of the simulator (such as generating synthetic scenerios) can easily do so through Waymax's APIs.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Environment Interface", "weight": 1.0} -->

Users primarily interact with Waymax as a partially-observable stochastic game. The Waymax interface follows the the Brax design to only define functionally pure initialization and transition functions. This stateless design enables efficient optimization through JAX's JIT compiler and functional libraries, and easily allows users to implement control algorithms that require backtracking, such as search. In contrast with stateful simulators, such as OpenAI Gym and DM Control, Waymax users need to maintain the simulator state within a simulation loop and interact with the simulator primarily through two functions: The reset(scenario) function takes as input a raw scenario, performs any initialization necessary such as populating the simulation history, and returns the initial state object.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Environment Interface", "weight": 1.0} -->

The step(state, action) function takes as input the current state, the actions for all agents, and computes the successor state as well as the new observation and metrics. The actions argument is a data structure that contains a data tensor of actions for each agent, as well as a validity mask which denotes which agents the user wishes to control. step then returns these results in a new timestep object.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Run one episode until termination", "weight": 1.0} -->

state = env.reset(next(dataset)) while not done: action = policy(env.observe(state)) state = env.step(state, action) Using these two functions, a user can run a simple, but complete simulation of a stochastic game between multiple agents, such as in the following pseudocode example: In addition, we do provide adapters to convert the functionally pure Waymax simulator into a stateful one to support existing codebases.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Hardware Acceleration and In-graph training", "weight": 1.0} -->

Waymax supports both hardware acceleration on GPUs and TPUs, as well as combining training and simulation within the same computation graph (referred to as "in-graph" training), which allows training and simulation to happen entirely on the accelerator without communication bottlenecks through the host machine. These features are possible because Waymax is written entirely using the JAX library, which converts operations into XLA, a linear algebra instruction set and optimizing compiler which supports execution on CPU, GPU, or TPU. In-graph training requires the modeling and training code to be written using an XLA-compatible frontend such as JAX, or Tensorflow. The XLA compiler can then optimize combined training and simulation program to produce a single computation graph that can be run entirely on hardware accelerators, without communication costs between the accelerator and host device.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Single and Multi-agent Simulation", "weight": 1.0} -->

While the base multi-agent environment allows us to do sim-agents (multi-agent) learning similar as in Nocturne, MetaDrive, the ultimate goal of the autonomous driving problem is to train an AV planning agent. Thus, Waymax supports both multi-agent simulation that allows users to control arbitrary objects within the scenario, as well as a single-agent workflow where a single AV agent is trained using learned or rule-based models to control the other vehicles in the scene.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Single and Multi-agent Simulation", "weight": 1.0} -->

While it might be possible to put multiple policies in one environment directly, it is certainly not a flexible way as it is hard to coordinate different policies or change policies. Waymax provides two interfaces for different use-cases: The MultiAgentEnvironment provides an interface for multi-agent and sim-agent problems. The user provides simultaneous actions for all controlled objects in the scene, as well as a mask to indicate which objects should be controlled.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Single and Multi-agent Simulation", "weight": 1.0} -->

The PlanningAgentEnvironment exposes an interface for controlling only the ego vehicle in the scene. All other agents are controlled by user-specified sim agents or log playback (Fig. 3).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

We now evaluate both Waymax as a simulator and the performance of several reference agents simulated using Waymax. We first evaluate the computational performance of Waymax in Sec. 5.1 under various configurations. Second, we perform an empirical study of several benchmark agents for planning in Sec. 5.3, where we compare the performance of several broad categories of learned planning algorithms (such as imitation learning and reinforcement learning) against both logged agents and reactive simulated agents. For the second part, our goals was to showcase potential options for using Waymax, so we opted for simple design choices and a breadth of configurations, and we expect that the performance of the baseline agents could be significantly improved in future work.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Runtime Benchmark", "weight": 1.0} -->

In Tab. 2, we present the runtime performance of Waymax using a CPU (Intel Xeon W-2135@3.7GHz) and a GPU (Nvidia-V100). We evaluate the performance of both multi-agent and the single-agent environment with different batch size. All functions are jit compiled and runtime is reported in millisecond. Following WOMD, the environment controls up to 128 objects in one scene. Note that the Step function computes both the state transition and the reward. While users specify customized reward function, for this runtime evaluation, we use the negative sum of all metrics in 3.4 as the reward, which measures the effect of computing all metrics. When considering batch size 1 and using a GPU, Waymax achieves over 1000Hz for Step function and over 2000Hz if only considering the Transition. More importantly, as Waymax supports batching, Step only takes 2.86ms using a batch size of 16. Note this is much faster than running batch size one for 16 times and gives an equivalent runtime of over 5000Hz per example (i.e. closer to 500 times faster than using a CPU).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Runtime Benchmark", "weight": 1.0} -->

Noticeably the Metrics function consumes more computation then the Transition function because the Off-Road metric needs to find nearby roadgraph points, which is a slow operation.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Rollout", "weight": 1.0} -->

We also benchmark a Rollout function which rolls out the environment given an Actor for an entire episode (i.e., 80 steps for WOD). This is especially useful to provide faster inference and evaluation. In the last column of Tab. 2, we show the runtime of Rollout with an ExpertActor that derives grouth-truth actions from logged trajectory. It is faster than running Step function 80 times. More importantly, we can see that running on GPU has a consistent 2 orders of magnitude speedup. As a point of reference, evaluating the full WOD evaluation dataset (44K scenarios) with 8-V100 machine takes less than 2min.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Expert", "weight": 1.0} -->

We provide a number of expert agent models to provide groundtruth actions for open-loop training. Each agent uses the inverse function of the action spaces defined in Section 3.3 to fit an action to the logged trajectory. For discrete action spaces, the inverse is computed by discretizing the continuous inverse.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Behavior Prediction Model (Wayformer)", "weight": 1.0} -->

As a point of reference, we adapt the state-of-the-art Wayformer behavior prediction model to the planning setting. Originally, the Wayformer predicts multiple $8$-second future trajectories given a $1$-second context history. To adapt it to the planning setting, we autoregressively feed in its predictions as the context history and choose the most likely trajectory. We found that making predictions at a lower frequency than the environment frequency improved performance, so we predict $5$-step long trajectories and only replan every $5$ steps.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Behavior Cloning", "weight": 1.0} -->

We re-use the encoder portion of Wayformer followed by a $4$-layer residual MLP to maximize the log likelihood of the expert actions. For continuous actions, we used a 6-component Gaussian Mixture Model. For discrete actions, we used a softmax layer to compute action probabilities.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Model-Free Reinforcement Learning - DQN", "weight": 1.0} -->

We used the Acme implementation of prioritized replay double DQN.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Model-Free Reinforcement Learning - DQN", "weight": 1.0} -->

We used the same architecture as in discrete BC for the Q-network, interpreting the logits of the model as Q-values.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Planning Benchmark Results", "weight": 1.0} -->

To showcase the flexibility of our environment, we trained a number of baselines on different action spaces and algorithms as shown in Table 3 and evaluated the metrics defined in Section 3.4. We evaluated each agent against the IDM sim agent and conditioned it on the route by adding the points from all the on-route paths as an additional input group to the Wayformer encoder. These points represent the on-route subset of the roadgraph points. All agents are trained for the planning agent task and thus only provide predictions for the autonomous vehicle. See Appendix A.2 for training details.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Planning Benchmark Results", "weight": 1.0} -->

As expected, the expert agents have low off-road and collision rates. The nominal values represent noise in the bounding boxes and logged data and serve as a lower bound for performance. The expert using the discrete bicycle action space has comparable performance to the other experts, confirming that the discretization is sufficiently fine.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Planning Benchmark Results", "weight": 1.0} -->

For open-loop imitation, the discrete action space performs best, possibly because it is easier to model multi-modal behavior. Furthermore, it outperforms the adapted Wayformer model, likely due to the fact that it is trained explicitly for this task. This serves as a check that the Waymax environment is producing the correct training data.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Route Conditioning Ablation", "weight": 1.0} -->

To showcase the utility of route conditioning, we compare the performance of route conditioned versus non-route conditioned behavior cloning agents Table 4 shows that the route conditioned agent is substantially better at following the route, while also achieving a lower off-road rate, collision rate, and log ADE. These results indicate that the route provides a strong signal for the planning task.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Route Conditioning Ablation", "weight": 1.0} -->

Agent (Action Space) Route Progress Ratio (%) Expert (Bicycle Discrete) BC (Bicycle Discrete) + Route Table 4: Experimental ablation comparing performance with and without route conditioning.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Sim Agent Ablation", "weight": 1.0} -->

In Table 5, we show the effect of training and evaluating an imitation agent against IDM sim agents versus playing back logged trajectories. As expected, evaluating with the IDM agent produces fewer collisions than evaluating with log playback. However, training an RL agent with IDM agents was less effective than training against logged agents. We believe this is because the RL agent tends to overfit or exploit the behavior of 'easier' IDM agents. Since IDM will stop for the SDC to avoid collisions, the RL agent does not have as much incentive to learn how to avoid collisions itself. We can see that when an IDM-trained agent is evaluated against logged agents, the collision rate is over 4x higher than when evaluated against IDM agents.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have presented Waymax, a multi-agent simulator for autonomous driving. Waymax provides diverse scenarios drawn from real driving data, and supports hardware acceleration and distributed training for efficient and cost-effective training of machine-learned models. It is also designed with flexibility in mind - Waymax is written as a collection of inter-operable libraries for data loading, metric computation, and simulation, which can support a wide variety of research problems that are not limited to just the planning evaluations presented in this work. We conclude by benchmarking several common approaches to planning with ablation studies over different dynamics and action representations, which provide a set of strong baselines for benchmarking future work.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In addition to hardware acceleration, Waymax also enables the exploration of methods utilizing differentiable simulation, as the entire simulation can be assembled within a single JAX computation graph. Prior work has shown that differentiable simulation can improve the efficiency of policy optimization methods as they can rely on a "reparameterized" or pass-through gradient to reduce the variance of the gradient estimate. We believe that this is a promising line of future work to be explored.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

As mentioned previously, the problem of sim-to-real transfer is a critical issue in autonomous driving, as it is cheap and desirable to evaluate in simulation but difficult to guarantee that the same performance and level of safety will carry over to the real world. While in Waymax we have made design decisions to minimize this gap (such as using real-world data to seed scenarios), this remains an important limitation for any simulation-based framework. A fruitful line of future work is to close the gap between simulated and real-world performance, potentially using techniques such as domain randomization or combining real and synthetic data.
