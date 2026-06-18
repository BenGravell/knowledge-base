<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Waymo Open Sim Agents Challenge

Topics include Autonomous driving, Vehicles, WOSAC.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Simulation with realistic, interactive agents represents a key task for autonomous vehicle software development. In this work, we introduce the Waymo Open Sim Agents Challenge (WOSAC). WOSAC is the first public challenge to tackle this task and propose corresponding metrics. The goal of the challenge is to stimulate the design of realistic simulators that can be used to evaluate and train a behavior model for autonomous driving. We outline our evaluation methodology, present results for a number of different baseline simulation agent methods, and analyze several submissions to the 2023 competition which ran from March 16, 2023 to May 23, 2023. The WOSAC evaluation server remains open for submissions and we discuss open problems for the task.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Simulation environments allow cheap and fast evaluation of autonomous driving behavior systems, while also reducing the need to deploy potentially risky software releases to physical systems. While generation of synthetic sensor data was an early goal Pomerleau; Dosovitskiy et al. of simulation, use cases have evolved as perception systems have matured. Today, one of the most promising use cases for simulation is system safety validation via statistical model checking Corso et al.; Agha and Palmskog with Monte Carlo trials involving realistically modeled traffic participants, i.e., *simulation agents*.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Simulation agents are controlled objects that perform realistic behaviors in a virtual world. In this challenge, in order to reduce the computational burden and complexity of simulation, we focus on simulating agent behavior as captured by the outputs of a perception system, e.g., mid-level object representations Bansal et al.; Zhang et al. such as object trajectories, rather than simulating the underlying sensor data Yang et al.; Manivasagam et al.; Chen et al.; Tancik et al. (see Figure 1).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A requirement for modeling realistic behavior in simulation is the ability for sim agents to respond to arbitrary behavior of the autonomous vehicle (AV). "Pose divergence" or "simulation drift" Bergamini et al. is defined as the deviation between the AV's behavior in driving logs and its behavior during simulation, which may be represented through differing position, heading, speed, acceleration, and more. Directly replaying logged behavior of all other objects in the scene Lu et al.; Li et al.; Kothari et al. under arbitrary AV planning may have limited realism because of this pose divergence. Such log-playback agents tend to heavily overestimate the aggressiveness of real actors, as they are unwilling to deviate from their planned route under any circumstances. On the other hand, rule-based agents that follow heuristics such as the Intelligent Driver Model (IDM) Treiber et al. are overly accommodating and reactive. We seek to evaluate and encourage the development of sim agents that lie in the middle ground, adhering to a definition of *realism* that implies matching the full distribution of human behavior.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Multiple Vehicle System System Task Object Outputs Kinematic Evaluation Objectives Categories Constraints Multi-Agent Trajectory Forecasting ✓ ((xt,yt,θt,vtx,vty))t = 1T ✗ Open-Loop Kinematic accuracy and mode covering AV Motion Planning ✗ ((xt,yt,θt))t = 1T or controls ✓ Closed-Loop Safety, comfort, progress Agent and Environment Simulation ✓ (ot)t = 1T; ot ∈ 𝒪 ✗ Closed-Loop Distributional realism
Table 1: A comparison of three autonomous-vehicle behavior related tasks which involve generation of a desired future sequence of physical states: trajectory forecasting, planning, and simulation. Note that observations ot ∈ 𝒪 include simulated agent and environment properties.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To the best of our knowledge, to date there is no existing benchmark for evaluation of simulation agents. Benchmarks have spurred notable innovation in other areas related to autonomous driving research, especially for perception Geiger et al.; Caesar et al.; Sun et al.; Chang et al., motion forecasting Chang et al.; Zhan et al.; Ettinger et al.; Caesar et al.; Wilson et al., and motion planning Dosovitskiy et al.. We believe a standardized benchmark can likewise spur dramatic improvements for simulation agent development. Among these benchmarks, those focused on motion forecasting are perhaps most similar to simulation, but all involve open-loop evaluation, which is clearly deficient compared to our closed-loop evaluation. Furthermore, we introduce realism metrics which are suitable to evaluating long-term futures. Relevant datasets such as the Waymo Open Motion Dataset (WOMD) Ettinger et al. exist today that contain real-world agent behavior examples, and we build on top of WOMD to build WOSAC.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this challenge, we focus on a subset of the possible perception outputs, e.g., traffic light states or vehicle attributes are not modeled, but we leave this for future work.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The challenges our benchmark raises are unique, and if we can make real progress on it, we can show that we've solved one of the hard problems in self-driving. We have a number of open questions: Are there benefits to scene-centric, rather than agent-centric, simulation methods? What is the most useful generative modeling framework for the task? What degree of motion planning is needed for agent policies, and how far can marginal motion prediction take us? How can simulation methods be made more efficient? How can we design a benchmark and enforce various simulator properties? During our first iteration of the WOSAC challenge, user submissions have helped us answer a subset of these questions; for example, we observed that most methods found it most expedient to build upon state-of-the-art marginal motion prediction methods, i.e. operating in an agent-centric manner.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we describe in detail the Waymo Open Sim Agents Challenge (WOSAC) with the goal of stimulating interest in traffic simulation and world modeling.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

An evaluation framework for autoregressive traffic agents based on the approximate negative log likelihood they assign to logged data.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

An evaluation platform, an online leaderboard, available for submission at [

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

An empirical evaluation and analysis of various baseline methods, as well as several external submissions.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Traffic Simulation as Conditional Generative Modeling", "weight": 1.0} -->

Our goal is to encourage the design of traffic simulators by defining a data-driven evaluation framework and instantiating it with publicly accessible data. We focus on simulating agent behavior in a setting in which an offboard perception system is treated as fixed and given.\

<!-- chunk {"id": "body-0015", "role": "body", "section": "Traffic Simulation as Conditional Generative Modeling", "weight": 1.0} -->

Problem formulation. We formulate driving as a Hidden Markov Model $\mathcal{H} = \left( \mathcal{S},\mathcal{O},{p{(\left. o_{t} \middle| s_{t} \right.)}},{p{(\left. s_{t} \middle| s_{t - 1} \right.)}} \right)$, where $\mathcal{S}$ denotes the set of unobservable true world states, $\mathcal{O}$ denotes the set of observations, $p{(\left. o_{t} \middle| s_{t} \right.)}$ denotes the sampleable emission distribution, and $p{(\left. s_{t} \middle| s_{t - 1} \right.)}$ denotes the hidden Markovian state dynamics: the probability of the hidden state transitioning from $s_{t - 1}$ at timestep $t - 1$ to $s_{t}$ at time $t$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Traffic Simulation as Conditional Generative Modeling", "weight": 1.0} -->

Each $o_{t} \in O$ can be partitioned into AV- and environment-centric components that vary in time: $o_{t} = {\lbrack o_{t}^{\text{AV}},o_{t}^{\text{env}}\rbrack}$. $\mathcal{O}_{t}^{\text{env}}$ can in general contain a rich set of features, but for the purpose of our challenge, it contains solely the poses of the non-AV agents. We denote the true observation dynamics as ${p^{\text{world}}{(\left. o_{t} \middle| s_{t - 1} \right.)}} \doteq {{\mathbb{E}}_{p{({s_{t}|s_{t - 1}})}}p{(\left. o_{t} \middle| s_{t} \right.)}}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Traffic Simulation as Conditional Generative Modeling", "weight": 1.0} -->

$q^{\text{world}}$ must be autoregressive for $T$ steps, i.e., sim agent models must adhere to a 10Hz resampling procedure, re-observing the updated scene and consuming their previous outputs.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Traffic Simulation as Conditional Generative Modeling", "weight": 1.0} -->

$q^{\text{world}}$ must factorize according to Eq.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Traffic Simulation as Conditional Generative Modeling", "weight": 1.0} -->

where $q{(\left. o_{t}^{\text{env}} \middle| o_{< t}^{c} \right.)}$ is a traffic simulator, and $\pi{(\left. o_{t}^{\text{AV}} \middle| o_{< t}^{c} \right.)}$ is an AV policy^11^1We call this a policy because it is similar to the typical formulation of a policy in a decision process over actions, although not equivalent, because it is defined over next observations rather than current actions. It can be made equivalent to a standard policy $\pi{(\left. a_{t - 1}^{\text{AV}} \middle| o_{< t}^{c} \right.)}$ by defining the AV's action space $\mathcal{A}$ to be equivalent to its component of the observation space, and defining an action-dependent world model ${q^{\text{world}}{(\left.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Traffic Simulation as Conditional Generative Modeling", "weight": 1.0} -->

o_{t} \middle| {o_{< t}^{c},a_{t - 1}^{\text{AV}}} \right.)}} \doteq {\delta{({o_{t}^{\text{AV}} = a_{t - 1}^{\text{AV}}})}q{(\left. o_{t}^{\text{env}} \middle| o_{< t}^{c} \right.)}}$, where $\delta$ denotes the Dirac delta function.. Any submission that fails to satisfy both of these properties will not be considered on WOSAC leaderboards, as determined by challenge submission reports. Requiring them to be generative enables sampling from an arbitrary traffic simulator-AV policy pair. These two properties imply the probabilistic graphical model shown in Fig. 2, modified from Fig. 9 of Rhinehart et al.. Algorithms 1 and 2 illustrate valid and invalid submissions.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Traffic Simulation as Conditional Generative Modeling", "weight": 1.0} -->

Much of the challenge of modeling $p^{\text{world}}$ lies in the fact that in many situations $s_{t - 1} \in \mathcal{S}$, $p^{\text{world}}$ assigns density to multiple outcomes due to uncertainty from agents in the scene, which means that both $\pi{(\left. o_{t}^{\text{AV}} \middle| o_{< t}^{c} \right.)}$ and $q{(\left. o_{t}^{\text{env}} \middle| o_{< t}^{c} \right.)}$ often must contain multiple modes in order to perform well. We evaluate distribution-matching of $p^{\text{world}}$ relative to a dataset of logged outcomes. The required factorization into a AV observation-space policy and environment observation dynamics, ${q^{\text{world}}{(\left.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Traffic Simulation as Conditional Generative Modeling", "weight": 1.0} -->

o_{t}^{\text{env},a} \middle| o_{< t}^{c} \right.)}}}$, i.e., the environment observation dynamics factorizes into a sequence of $A$ observation-space policies, and the environment observation itself is partitioned into $A$ different components, one for each agent: $o_{t}^{\text{env}} = {\lbrack o_{t}^{\text{env},1},\ldots,o_{t}^{\text{env},A}\rbrack}$.\

<!-- chunk {"id": "body-0023", "role": "body", "section": "Traffic Simulation as Conditional Generative Modeling", "weight": 1.0} -->

Input: Map omap and traffic signals osignals. Initial actor states $o_{{{- H} - 1}:0} = \begin{Bmatrix}
\end{Bmatrix}$ where each $o_{t}^{\text{env}} = \begin{Bmatrix}
{o_{t}^{\text{env},1},\ldots,o_{t}^{\text{env},A}}
\end{Bmatrix}$ for the A actors in the scene. Output: Simulated observations $o_{1:T} = \begin{Bmatrix}
\end{Bmatrix}$ for T simulation timesteps.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Traffic Simulation as Conditional Generative Modeling", "weight": 1.0} -->

1:for t = 1, …, T do ⊳ Simulate for requested number of timesteps
2: otAV ← πAV(o &lt; t;omap,osignals)
3: for a = 1, …, A do ⊳ Produce next state for each actor at each timestep
4: otenv, a ← πa(o &lt; t;omap,osignals)
6:return $o_{1:T} = \begin{Bmatrix}
Algorithm 1 Valid: Factorized, Closed-Loop, Agent-Centric Simulation

<!-- chunk {"id": "body-0025", "role": "body", "section": "Traffic Simulation as Conditional Generative Modeling", "weight": 1.0} -->

Input: Map omap and traffic signals osignals. Initial actor states $o_{{{- H} - 1}:0} = \begin{Bmatrix}
\end{Bmatrix}$ where each $o_{t}^{\text{env}} = \begin{Bmatrix}
{o_{t}^{\text{env},1},\ldots,o_{t}^{\text{env},A}}
\end{Bmatrix}$ for the A actors in the scene. Output: Simulated observations $o_{1:T} = \begin{Bmatrix}
\end{Bmatrix}$ for T simulation timesteps.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Traffic Simulation as Conditional Generative Modeling", "weight": 1.0} -->

1:o1: TAV ← πAV(o &lt; 1;omap,osignals)
2:for a = 1, …, A do ⊳ Produce states at all future timesteps for each actor
3: o1: Tenv, a ← πa(o &lt; 1;omap,osignals)
4:return o1: T = {o1: Tenv, a: ∀a ∈ 1…A} ∪ {o1: TAV}
Algorithm 2 Invalid: Factorized, Open-Loop, Agent-Centric Simulation

<!-- chunk {"id": "body-0027", "role": "body", "section": "Dataset", "weight": 1.0} -->

For WOSAC, we use the test data from the v1.2.0 release of the Waymo Open Motion Dataset (WOMD) Ettinger et al.. We treat WOMD as a set $\mathcal{D}$ of scenarios where each scenario is a history-future pair $(o_{{{- H} - 1}:0},o_{\geq 1})$. This dataset offers a large quantity of high-fidelity object behaviors and shapes produced by a state-of-the-art offboard perception system. We use WOMD's 9 second 10 Hz sequences (comprising $H = 11$ observations from 1.1 seconds of history and 80 observations from 8 seconds of future data), which contain object tracks at 10 Hz and map data for the area covered by the sequence. Across the dataset splits, there exists 486,995 scenarios in train, 44,097 in validation, and 44,920 in test. These 9.1 second windows have been sampled with varying overlap from 103,354 mined segments of 20 second duration.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Dataset", "weight": 1.0} -->

Up to 128 agents (one of which must represent the AV) must be simulated in each scenario for the 8 second future (comprising 80 steps of simulation).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Dataset", "weight": 1.0} -->

Agent Definition We require simulation of all agents that have valid measurements at time $t = 0$, i.e. the last step of logged initial conditions before simulation begins. Because the test split data is sequestered, users will not have access to objects that appear after the time of handover, and so therefore could not be expected to simulate them. We require simulation of all three WOMD object types (vehicles, cyclists, and pedestrians). Objects' dimensions stay fixed as per the last step of history (while they do change in the original data).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Dataset", "weight": 1.0} -->

Submission We do not enforce any motion model (also because we have multiple agent types), which means users need to directly report $x$/$y$/$z$ centroid coordinates and heading of the objects' boxes (which could be generated directly or through an appropriate motion model). See the Appendix for additional information on the submission format.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Dataset", "weight": 1.0} -->

By allowing users to produce the simulations themselves, we reduce the burden on the user by avoiding the need to submit containerized software for an evaluation server.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Agents should generate realistic driving scenarios stochastically. We define "realistic agents" as those that match the actual distribution of scenarios observed during real-world driving. Unfortunately, we do not know the analytic form of the distribution, but we do have samples from it: the examples that make up WOMD. We therefore evaluate submissions using the approximate negative log likelihood (NLL) of real world samples under the distribution induced by the agents.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Evaluation", "weight": 1.0} -->

However, there are two problems with trying to minimize Equation 2 exactly in our problem setting. First, $o_{\geq 1}$ is high-dimensional. Instead of trying to parameterize the entire ground truth scenario and compute its NLL under a simulated distribution, we therefore parameterize scenarios with a smaller number of component metrics (see Section 4.2.1) and aggregate them together into a composite NLL metric (see Section 4.2.2). Second, agents may support sampling but not pointwise likelihood estimation Nowozin et al.. In fact, we only require challenge entrants to submit samples from their agents, and therefore have no way of knowing the exact likelihood of logged scenarios under different agent submissions. To avoid this problem, we standardize the NLL computation by fitting histograms to the 32 submitted samples of agent futures, and compute NLLs under the categorical distribution induced by normalizing the histograms.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Component Metrics", "weight": 1.0} -->

Breaking $\text{NLL}^{*}$ into component metrics has a few benefits. It mitigates the curse of dimensionality described in Section 4.2. It also adds more interpretability to the evaluation, allowing researchers to trade off between different types of errors.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Component Metrics", "weight": 1.0} -->

Time Series NLL: Given the time series nature of simulation data, two choices emerge for how to treat samples over multiple timesteps for a given object for a given run segment: to treat them as time-independent or time-dependent samples. In the latter case, users would be expected to not only reconstruct the general behaviors present in the logged data in one rollout, but also recreate those behaviors over the exact same time intervals. To allow more flexibility in agent behavior, we use the former formulation when computing NLLs, defining each component metric $m$ as an average (in log-space) over the time-axis, masked by validity $v_{t}$: $m = {\exp\left( {- {\frac{1}{\sum\limits_{t}{\mathbb{1}{\{ v_{t}\}}}}{\sum\limits_{t}{\mathbb{1}{\{ v_{t}\}}NLL_{t}}}}} \right)}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Component Metrics", "weight": 1.0} -->

However, we note that as a result, a logged oracle will not achieve likelihoods of 1.0, whereas in the latter formulation a logged oracle would.\

<!-- chunk {"id": "body-0037", "role": "body", "section": "Component Metrics", "weight": 1.0} -->

Definitions We compute NLLs over 9 measurements: kinematic metrics (linear speed, linear acceleration, angular speed, angular acceleration magnitude), object interaction metrics (distance to nearest object, collisions, time-to-collision), and map-based metrics (distance to road edge, and road departures). Please refer to Section A.6 of the Appendix for a complete description and additional implementation details.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Composite Metric", "weight": 1.0} -->

where $N$ is the number of scenarios and $M = 9$ is the number of component metrics. The component metrics $m$ and composite metric $\mathcal{M}$ are also parameterized by a number of samples $K = 32$. The value $m_{i,j}$ represents the likelihood for the $j^{th}$ metric on the $i^{th}$ example. The metric $\mathcal{M}$ is simply a convex combination (i.e. weighted average) over the component metrics, where the weight $w_{j}$ for the $j^{th}$ metric is set manually. In the interest of promoting safety, the weighting for collision and road departure NLLs are set to be $2 \times$ larger than the weight for the other component metrics.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

In Figure 4 and Table 3, we present quantitative results for a handful of methods. We describe each method in more detail in the sections below.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Baselines", "weight": 1.0} -->

Random Agent: An agent that produces random trajectories ${\{{(x_{t},y_{t},\theta_{t})}\}}_{t = 1}^{T}$, for $T = 80$, with ${x,y,\theta} \sim {\mathcal{N}{(\mu,\sigma^{2})}}$, with $\mu = 1.0$ and $\sigma = 0.1$, in the AV's coordinate frame.\
Constant Velocity Agent: An agent that extrapolates the trajectory using the last heading and speed recorded in the provided context/history. If no two-step difference can be computed based on the valid measurements (e.g. the object appeared only at the final step of context), we set a zero speed for such agents.\
Wayformer (Identical Samples) Agent: An agent that produces a hybrid of open-loop and closed-loop data using a Wayformer Nayakanti et al. motion prediction model, by executing model inference autoregressively at 2Hz.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Baselines", "weight": 1.0} -->

The agents execute the policy forward for 5 simulation steps, and then replan. Results with a 10 Hz replan rate instead are also shown in Table 3, and an ablation on the replan rate is provided in the Appendix. The maximum-likelihood trajectory for each agent is identically repeated 32 times to produce 32 samples. Each agent is executed by the same policy in an agent-centric frame, batched together for inference, thus complying with the required factorization.\
Wayformer (Diverse Samples) Agent: An agent that also utilizes Wayformer Nayakanti et al. -generated trajectories, but samples diverse agent plans, from $K$ possible trajectories according to their likelihood, instead of selecting the maximum-likelihood choice.\
Logged Oracle: Agent that directly copies trajectories from the WOMD test split, with 32 repetitions.\

<!-- chunk {"id": "body-0042", "role": "body", "section": "External Submissions", "weight": 1.0} -->

MultiVerse Transformer for Agent simulation (MVTA) Wang et al.: A method inspired by MTR Shi et al. that is trained and executed in closed-loop. MVTA uses a 'receding horizon' policy with a GMM head, and consumes vector inputs.

<!-- chunk {"id": "body-0043", "role": "body", "section": "External Submissions", "weight": 1.0} -->

MVTE: An enhanced version of MVTA Wang et al. that samples a MVTA model from a pool of model variants to increase simulation diversity across rollouts.

<!-- chunk {"id": "body-0044", "role": "body", "section": "External Submissions", "weight": 1.0} -->

MTR+++ Qian et al.: A hybrid open-loop/closed-loop method with a 0.5Hz replanning rate that is inspired by MTR Shi et al. and searches for the densest subgraph in a graph of non-colliding future trajectories.

<!-- chunk {"id": "body-0045", "role": "body", "section": "External Submissions", "weight": 1.0} -->

For a description of other evaluated external submissions, please refer to Section A.4 of the Appendix.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Learnings from the 2023 Challenge", "weight": 1.0} -->

During the course of our 2023 WOSAC Challenge, associated with the CVPR 2023 Workshop on Autonomous Driving, we received 24 test set submissions, and 16 validation set submissions, from 10 teams. We continue to receive submission queries to our evaluation server for our standing [leaderboard] as new teams submit new methods.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Learnings from the 2023 Challenge", "weight": 1.0} -->

Trends We observed several trends among submissions. First, the challenge champion, MVTA/MVTE Wang et al., was the only method to utilize and benefit from closed-loop training. Other methods that were trained in open-loop, such as MTR+++ Qian et al. or our Wayformer-derived Nayakanti et al. baseline, found operating at slower replan rates necessary to obtain high composite metric results (See Table 3). Second, almost all submissions used Transformer-based methods Vaswani et al., except for JointMultiPath++, which used LSTM and MCG blocks Varadarajan et al.. Third, all methods built primarily on top of existing motion prediction works, rather than upon existing motion planning works or sim agent methods from the literature. Only one method, MVTA/MVTE Wang et al., incorporated aspects of an existing sim agent work, TrafficSim Suo et al., as well as motion planning techniques, implementing a receding horizon planning policy. Thus, fourth, we observed the benefit of incorporating planning-based methods into a motion prediction framework.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Learnings from the 2023 Challenge", "weight": 1.0} -->

Fifth, most methods (excluding JointMultipath++ Wang and Zhen ) built upon the 2022 CVPR Waymo Open Motion Prediction challenge champion, MTR Shi et al., likely due to the open-source availability of its codebase and SOTA performance. Finally, all submissions operated in an agent-centric coordinate frame, rather than jointly sampling from a scene representation simultaneously.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Learnings from the 2023 Challenge", "weight": 1.0} -->

Likelihood Metrics Reward Diversity We found that our likelihood-based metrics reward models that produce diverse futures. For example, generating 32 diverse rollouts per scene with a Wayformer model performs 11% better on our evaluation metrics than a Wayformer model that produces 32 identical rollouts per scene (see Figure 4).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Learnings from the 2023 Challenge", "weight": 1.0} -->

Collision Minimization as an Algorithmic Objective Several methods designed algorithmic components to determine futures with a minimal number of collisions, e.g., MTR+++ Qian et al. which used clique-finding in an undirected graph of collision-free future trajectories, and CAD Chiu and Smith, which used rejection sampling on open-loop futures that created collisions. This objective aligns with human preference, but as close calls and collisions do occur in real driving data distributions, optimizing for this objective could be seen as trimming the tail of the distribution; distracted drivers generally do exist in everyday real world driving, and in certain scenarios, one would expect a low-quality planner to perform poorly and produce collisions with sim agents, and so such should be taken into consideration for generating realistic simulations. This suggests a limitation of the WOMD Ettinger et al., which has few examples from the tail distribution of real driving, and efforts to upsample collision data could prove useful.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Learnings from the 2023 Challenge", "weight": 1.0} -->

In addition, open-loop methods such as CAD Chiu and Smith that prune collisions after the fact could prune collisions caused by the AV rather than by the sim agents, yielding a misleadingly optimistic view of the AV's performance.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Learnings from the 2023 Challenge", "weight": 1.0} -->

Composite Metric vs. (min-)ADE and ADE: We see that among submissions to the test set, rankings by ADE and minADE and ranking by our NLL composite metric disagree. However, methods with lower minADE do tend to achieve higher composite scores; ADE does not exhibit such a trend.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Learnings from the 2023 Challenge", "weight": 1.0} -->

Composite Metric Results The ordinal ranking shown in Figure 4 and Table 3 indicates that learned, stochastic sim agents outperform not only heuristic baselines but also learned, deterministic sim agents. We consider a composite metric score of 0.722 as a practical upper bound on submissions, because it involves access to test data via an oracle.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Learnings from the 2023 Challenge", "weight": 1.0} -->

Component Metric Results In Table 3, we provide a breakdown of the composite metric into component metric results. As expected, the 'logged oracle' baseline achieves the highest likelihood in each of the 9 component metrics. The top performing method, MVTE Wang et al. scored highest on all but one component metric (linear acceleration likelihood), where CAD Chiu and Smith outperformed MVTE by 12% (likelihood of 0.253 vs. 0.222). Surprisingly, MVTE Wang et al. has angular acceleration likelihoods within a percentage point of the 'logged oracle' (0.481 vs. 0.489). The gap between the top performing learned method (MVTE) and 'logged oracle' in both collision likelihood (0.893 vs. 1.000) and distance-to-nearest object likelihood (0.383 vs. 0.485) indicates significant room for improvement in future work on interactive metrics.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

In Figure 3, we provide a qualitative comparison of various baselines on two WOMD scenarios. The results indicate that the complexity of behaviors within intersections far exceeds the capability of simple heuristics to predict. Collisions are evident from the constant velocity baselines in both examples. Additional qualitative examples from other sim agent methods are shown in Section A.5 of the Appendix.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Limitations", "weight": 1.5} -->

For our 2023 Challenge, we manually verified the validity of each submission according to factorization and closed-loop requirements discussed in each team's report, and we observed that the technical rules were subtle. Several of the submissions that used open-loop or hybrid open-loop/closed-loop methods may have limited applicability for some simulation applications.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Limitations", "weight": 1.5} -->

Even if we had instituted a benchmark based on Docker-containerized software submissions instead of uploading output trajectory submissions, enforcing our requirements algorithmically and automatically would still be challenging. Although many properties of function calls to Dockerized software can be measured, e.g. latency, as long as any arbitrary state is maintained by the user, the system could not enforce all details of the closed-loop nature of the function call. As a result, user-submitted simulation agent software would have to adhere to strict stateless input and output data APIs. The ability to do so would assist in removing ambiguity regarding whether methods that prune collisions post-hoc qualify as closed-loop.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Limitations", "weight": 1.5} -->

If a user provides containerized simulator submissions, one approach to encourage adherence to our requirements and to further incentivize closed-loop behavior would be to provide and interact with an AV policy that the user does not control. In our benchmark, the user was allowed to control the AV, albeit through an independent policy; the ability to evaluate simulator submissions on separate, held-out AV motion planning policies and on new scenarios would allow further valuable analysis.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Future Work", "weight": 1.5} -->

Object insertion and deletion are important aspects of the simulation problem, yet we intentionally introduced an assumption of no object insertion or deletion in order to reduce the complexity of the first iteration of the WOSAC challenge for users. Motion planners trained or evaluated in a simulator must have the capability to exercise caution regarding areas of occlusion from which new objects may emerge at any timestep. In a future iteration of the challenge, we plan to introduce realism metrics that reward properly-modeled object insertion and deletion, e.g. distributional metrics on the number of vehicles appearing or disappearing at each frame, or the distance of simulated objects from the autonomous vehicle. The data distribution in the WOMD dataset already includes such object insertion and deletion.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Future Work", "weight": 1.5} -->

Furthermore, we intentionally introduced an assumption of time-invariant object dimensions in our first iteration of WOSAC to simplify the modeling challenge for users. Time-variant object dimensions can be considered as a type of vehicle attribute, and object dimensions do actually change in the underlying data distribution provided in the WOMD dataset. We hope to include time-variant object dimension prediction as an aspect of the benchmark in future iterations.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Future Work", "weight": 1.5} -->

As discussed in Section 5.3, given the prevalence of collision minimization algorithmic components among submissions, one may presume that collisions are not heavily represented in WOMD Ettinger et al. data, or our metrics are limited in some way. Another approach would be to "fatten the tails" of the evaluation data distribution by generating synthetic, challenging initial conditions Bergamini et al.; Wang et al.; Tan et al.; Rempe et al.; Feng et al.; Ethan Pronovost, or mining more close calls and collisions from real driving data.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we have introduced a new challenge for evaluation of simulation agents, explaining the rationale for the different criteria we require. We invite the research community to continue to participate.
