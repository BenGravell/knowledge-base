<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Multi-Agent Path Integral Control for Interaction-Aware Motion Planning in Urban Canals

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Autonomous vehicles that operate in urban environments shall comply with existing rules and reason about the interactions with other decision-making agents. In this paper, we introduce a decentralized and communication-free interaction-aware motion planner and apply it to Autonomous Surface Vessels (ASVs) in urban canals. We build upon a sampling-based method, namely Model Predictive Path Integral control (MPPI), and employ it to, in each time instance, compute both a collision-free trajectory for the vehicle and a prediction of other agents' trajectories, thus modeling interactions. To improve the method's efficiency in multi-agent scenarios, we introduce a two-stage sample evaluation strategy and define an appropriate cost function to achieve rule compliance. We evaluate this decentralized approach in simulations with multiple vessels in real scenarios extracted from Amsterdam's canals, showing superior performance than a state-of-the-art trajectory optimization framework and robustness when encountering different types of agents.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

With rising population density, cities are forced to enhance their mobility and transportation strategies. The City of Amsterdam aims to reduce the load on road infrastructure by transporting goods and people on the urban waterways. This presents a great opportunity to operate Autonomous Surface Vessels (ASVs) such as Roboat in urban canals. However, this is a very technically challenging task due to the complex and dynamic nature of the environment. Narrow canals, complex dynamics, static obstacles, and human-piloted vessels must be dealt with while obeying existing canal regulations. Model Predictive Path Integral Control (MPPI) offers a parallelizable sampling-based framework for solving motion planning tasks with such complex dynamics and discontinuous costs as those exhibited in our domain. Unlike methods based on constrained optimization, which need to rely on convex approximations of the free space and on inflating the ego and obstacle agents into ellipsoidal shapes for collision avoidance, MPPI can account for the exact and potentially non-convex shape of both static and dynamic obstacles. This promises to be a significant advantage in tight interaction-rich environments. Still, another important aspect of achieving safe and efficient navigation in crowded spaces is accounting for cooperation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

For these reasons, we propose a method to decentralize MPPI in order to navigate among non-communicating agents while providing interaction awareness and generating cooperative motion plans. We introduce awareness of navigation rules through discontinuous costs. Moreover, the proposed method can run in real-time thanks to our two-stage sample evaluation strategy and CPU parallelization.

<!-- chunk {"id": "body-0005", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

Cooperative and interactive motion planning for robotics is a challenging problem with a vast literature.

<!-- chunk {"id": "body-0006", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

The most well-known examples for planning in dynamic environments are the Dynamic Window Approach (DWA), Reciprocal Velocity Obstacle (RVO), its extension Optimal Reciprocal Collision Avoidance (ORCA), and Artificial Potential Fields (APF). While these methods are highly efficient, they often lead to reactive behaviors.

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

Model-free reinforcement learning algorithms have been successfully trained in simulation with hand-crafted reward functions to navigate among human crowds, but generalization and collision avoidance are not guaranteed.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

Game theoretic approaches have been implemented in the context of autonomous cars to perform lane changes, merging and to solve unsignalized intersections. However, they rely on a coarse discretization of the action space and do not scale well with the number of agents.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

Model Predictive Control (MPC) based on trajectory optimization is a popular approach when it comes to local motion planning. In a multi-agent setting, however, the actions of the other agents are required to proceed with the motion planning of the ego-agent. In a distributed MPC was developed for motion planning with multiple drones relying on ideal communication. A way to avoid communication is to estimate each agent's state and predict their future motion using, for example, a constant velocity model or learning-based techniques. However, as long as we first predict and then plan, large parts of the state-space can be perceived as unsafe by the motion planner. This can be overcome by modeling interaction, such that the ego-agent is aware that its actions can influence the actions of the other agents around it. Unfortunately, accounting for such a model while planning with constrained optimization techniques can become computationally expensive.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

In contrast to optimization-based methods, MPPI solves for the best control trajectory at each step by forward simulating the behavior of the full system. To achieve this, MPPI uses a parallelizable sampling-based framework to rollout simulations, allowing it to find an approximate solution to non-linear, non-convex, discontinuous Stochastic Optimal Control (SOC) problems. Compared to other SOC methods such as iterative Linear Quadratic Gaussian (iLQG) or Differential Dynamic Programming (DDP), MPPI does not require linearization of the system dynamics or quadratic approximation of the cost function. This makes MPPI particularly well-suited to our target task of ASV navigation in urban canals since the regulation-based interactions explicitly give rise to non-differentiable costs. Moreover, MPPI's fast parallelizable computations could solve interaction-aware motion planning problems while still running in real-time. When deployed to centralized multi-agent systems, however, the classic MPPI approach shows a significant increase in the number of samples required with an increasing number of agents.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

We propose an interaction-aware motion planning method based on MPPI which can generate cooperative plans in environments with non-communicating agents accounting for the full dynamics of the system and the exact shapes of the obstacles. To summarize our contributions: We propose a decentralized architecture that can operate with limited or no communication under the assumption that other agents' states can be sensed exactly and that all the agents in the environment behave rationally.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

To reduce the number of samples required to plan for multi-agent systems, we propose a two-stage sample evaluation technique that improves sample efficiency.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

We formulate the objectives of the navigation task into an appropriate cost function to achieve rule compliance.

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

To demonstrate the performance of our method, we compare it to a state-of-the-art regulations-aware optimization-based MPC in several simulated experiments set up in real sections of Amsterdam's canals. The proposed decentralized MPPI is also compared to the centralized version in environments with crowds of up to four interacting vessels. Finally, we demonstrate the robustness of the algorithm in scenarios where a human-driven vessel does not behave rationally and provide insights into the computation times.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A MPPI Algorithm", "weight": 1.0} -->

The presented work is based on the MPPI derivations. With this method, we can solve SOC problems for discrete-time dynamical systems of the form, with state $\mathbf{q}$, time step $t$, nonlinear state transition function $\mathcal{F}$ and noisy input $\overset{\sim}{\mathbf{u}}$ with variance $\mathbf{\Sigma}$ and mean $\mathbf{u}$, where $\mathbf{u}$ is the input we command to the system.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A MPPI Algorithm", "weight": 1.0} -->

The algorithm samples $K$ input sequences ${{\overset{\sim}{U}}_{k},k} \in {\lbrack 1,K\rbrack}$ from a distribution $\mathcal{N}{(\mathbf{u}_{t},{\nu\mathbf{\Sigma}})}$ (with scaling parameter $\nu$) and simulates them into $K$ state trajectories $Q_{k}$ over a horizon $T$ as, Each sample is rated by computing the total cost $S_{k}$, which includes a stage cost and a terminal cost. Importance sampling weights $w_{k}$ are then computed based on the cost of the sample $k$ minus the minimum sampled cost $S_{min}$ as, with normalization factor $\eta$ and tuning parameter $\lambda$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A MPPI Algorithm", "weight": 1.0} -->

The resulting control input sequence $U^{*}$, which approximates the optimal control input sequence, is computed, Then, the first input $u_{0}^{*}$ of the computed sequence $U^{*}$ is applied to the system.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Vessel State and Dynamics", "weight": 1.0} -->

We define the multi-agent state similarly to. The state of agent $i$ is defined as the concatenation of its position, heading, and associated velocities, The full system state is then formed by stacking the individual states of each of the agents in the set $\mathcal{M} = {\{ 0,1,\ldots,m\}}$, The ASV we use is modeled as a nonlinear second order system. Since the vessel sails at low speeds, we discard Coriolis and centripetal effects.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-C Global Planning", "weight": 1.0} -->

To help navigate large maps, we provide the ego-agent with a global path. Such a path is generated via the ROS navigation stack with its path planning plugin. Instead of directly tracking this global path, we look for a local goal $\mathbf{p}_{g}$ on the global path at a given look-ahead distance $r_{\text{𝐩}_{g}}$ (Fig. 5). Compared to just rigorously tracking the global path, this local goal approach gives the local planner more freedom to perform collision avoidance and other maneuvers.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Decentralized Interaction-aware Model Predictive Path Integral Control", "weight": 1.0} -->

In the following we outline the proposed architecture, state the changes to the classic MPPI framework and present the regulation-aware cost function along with the local goal prediction used for the decentralized computation of the cost.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Approach and Architecture", "weight": 1.0} -->

Our decentralized MPPI approach relies on each agent running its own MPPI solver for its local multi-agent system to anticipate the actions of other agents (see Fig. 2). That is, for agent $i$, the MPPI state and control output are defined as, where $\left(. \right)_{j}^{i}$ signifies a variable that agent $i$ estimates of agent $j$. In the centralized case described in Section II-A, the system state is fully observable and the inputs computed by the central controller will be those executed by each agent. When we move to the decentralized case, the positions and velocities of other agents must be communicated or observed. Furthermore, while each agent samples control actions for all other agents in the MPPI rollouts, at execution time, there is no guarantee that other agents will behave accordingly. To focus on the decentralized coordination problem, we make a few assumptions.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Approach and Architecture", "weight": 1.0} -->

First, we assume noise-free observations of the positions and velocities of other agents, i.e. $\mathbf{q}_{j}^{i} = \mathbf{q}_{j}$. Second, we assume that all agents behave rationally and that they are minimizing the same global cost. We later show in our experiments that the controller is still able to perform well when this assumption is violated. Third, in our experiments we only consider scenarios with homogeneous agents, meaning that they all have the same dynamics. This third assumption is not required in general as considering different dynamical models for different agents is possible as long as models are known. Fig. 3 shows a simulated encounter between two ASVs running our decentralized algorithm without communication.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Two-stage Sample Evaluation", "weight": 1.0} -->

With an increasing number of agents, it is increasingly likely for at least one agent to collide with a static obstacle in most rollouts. In the classical implementation of MPPI, this leads to most rollouts receiving a high cost and being effectively rejected, resulting in a very low sample efficiency. Therefore we propose to decouple the sampling into two stages as shown in Algorithm 1. Control-samples $U_{j,k}$ are evaluated in parallel for every agent $j \in \mathcal{M}$, predicting the set of individual trajectories $Q_{j,k}$ with agent-centric costs $S_{j,k}$ (eq. 9). At this point all samples with cost larger than the collision penalty $C_{\text{collision}}$ are immediately discarded (lines 3 and 4 of Algorithm 1). To build the expected number of system samples $K$ we sample uniformly from the remaining non-colliding samples of each agent and unify these into full system samples, i.e. by stacking as in eq..

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Two-stage Sample Evaluation", "weight": 1.0} -->

For each system sample $Q_{k}$ the complete configuration cost $S_{k}$ is evaluated by adding the stored agent-centric costs $S_{j,k}$ with any costs arising from collisions between vessels and regulation violations (line 14, Algorithm 1).

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Two-stage Sample Evaluation", "weight": 1.0} -->

1:U ⊳ previous control sequence (hot start) 2:q⊳ current system state 5:for each agent j ∈ ℳ do⊳ independent rollouts 6: for each sample k do 8: ${\overset{\sim}{U}}_{j,k} = {U_{j} + \mathcal{E}_{j,k}}$ 9: Qj, k← simulateSystem$(\mathbf{q}_{j},{\overset{\sim}{U}}_{j,k})$ 10: Sj, k← getIndividualCost$(Q_{j,k},{\overset{\sim}{U}}_{j,k},\mathbf{p}_{j,g})$ 12: discardSample$(Q_{j,k},{\overset{\sim}{U}}_{j,k},\mathcal{E}_{j,k},S_{j,k})$ 13:Uniformly sample from the remaining valid input sequences to rebuild K full system samples

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Two-stage Sample Evaluation", "weight": 1.0} -->

17:return $U^{*} = {U + {\sum_{k = 1}^{K}{w_{k}\mathcal{E}_{k}}}}$ Algorithm 1 Decentralized MPPI for agent i (agent-specific superscripts are dropped for clarity)

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-C Cost Formulation", "weight": 1.0} -->

The sample cost ${S_{k},{\forall k}} \in {\lbrack 1,K\rbrack}$ evaluation is split into agent-centric and configuration costs. Both are considered instantaneous costs and are evaluated for every time-step $t$ within the horizon $T$ and each sample $k$. The agent-centric cost $S_{j,k,t}$ (in the following $S_{\text{agent}}$) is evaluated for agent $j$ for sample $k$ and defined as, $C_{\text{static}}$ returns a constant penalty $C_{\text{collision}}$ if the vessel enters occupied space and $C_{\text{rotation}}$ is based on a linear penalty for rotation velocities ($k_{\text{rot, slow}}$ for velocities ${\|\mathbf{v}\|}_{2} < {0.5\text{m/s}}$, $k_{\text{rot}}$ otherwise).

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-C Cost Formulation", "weight": 1.0} -->

The tracking cost is, where $k_{\text{tracking}}$ is a scaling factor, $\text{𝐩}_{g}$ is the agent's local goal, $\text{𝐩}_{t}$ is the predicted agent position at time $t$ and $\text{𝐩}_{t_{0}}$ is the vessel position at the start of the prediction horizon. $C_{\text{speed}}$ is a constant penalty applied when the current speed is higher than the maximum speed. The sample cost is given, with $\gamma$ as a tuning parameter.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-C Cost Formulation", "weight": 1.0} -->

The configuration cost $S_{k,t}$ (in the following $S_{\text{configuration}}$) is evaluated for every timestep $t$ within the horizon $T$ for every sample $k$ and combines dynamic collisions and regulation violations, Dynamic collisions are defined as those between multiple vessels and are penalized with the same constant $C_{\text{collision}}$ and the regulation cost $C_{\text{regulation}}$ is derived from the two main traffic rules (i) *avoiding to the right* in head-on encounters and (ii) *right of way* for crossing scenarios similar to COLREGs. Regulation compliance is determined by a relative position and relative velocity check. Regarding the position, we check if there is a vessel with significant velocity (${\|\mathbf{v}\|} > {{0.5m}/s}$) on starboard side within a given radius (Fig 4).

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-C Cost Formulation", "weight": 1.0} -->

Regarding the relative velocities, we evaluate if another vessel approaches from the right, where $\delta$ defines the angular margin, and if the other vessel is approaching the ego-vessel head-on via, Therefore if we detect a vessel on starboard side and the velocities satisfy, we consider the ego-agent as breaking the right-of-way rule (Fig. 4 left). If instead, we detect a vessel on starboard side with opposite velocity, we consider it as passing on the right (Fig. 4 right).

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-D Local Goal Prediction", "weight": 1.0} -->

The proposed decentralized version of interaction-aware MPPI requires estimating the local goals for all non-ego vessels (line 2, Algorithm 1). We use a constant velocity model such that agent $i$ estimates the goal of agent $j$ as, with $k_{s}$ as a scaling factor and $\delta T$ as step size. If the predicted goal is in collision, we project back along the vector towards $\mathbf{p}_{j}^{i}$ and choose the first unoccupied point as shown in Fig. 5.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

We perform extensive experiments in several maps taken from real canal sections of Amsterdam, namely the Herengracht (HG), Prinsengracht (PG), Bloemgracht (BG), and the intersection between Bloemgracht and Lijnbaansgracht (BGLG). In all experiments, the dimensions of both the map and the vessel are represented faithfully. In Section IV-A we compare our method in two-agent scenarios with an optimization-based MPC, in Section IV-B we test our method in interaction-rich four-agent scenarios, in Section IV-C we demonstrate the robustness to non-rational human-driven agents, while in Section IV-D we discuss the computation times of the proposed method. All experiments running MPPI use a horizon $T$ of 100 time-steps with step-size ${\delta T} = {0.1s}$, input variance $\Sigma = {\text{diag}{(0.5,0.5,0.01,0.01)}}$ and exploration scaling factor $\nu = 12$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

We use $K = {\{ 2000,6000\}}$ samples for two- and four-agent scenarios, respectively. Each version of the MPPI shown in the experiments (centralized, decentralized, decentralized with no communications) uses our proposed two-stage sampling technique.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

(a) Prinsengracht. MPPI understands that the blue vessel can safely cross in front of the vessel with the right of way (orange) without slowing it down. RA-MPCC is not confident and ends up blocking the way, pushing the orange vessel out of its route.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

(b) Bloemgracht. The MPPI agents cooperate to perform collision avoidance, while RA-MPCC ends up in a deadlock.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

(c) Bloemgracht-Lijnbaansgracht. The MPPI agents correctly solve the crossing according to the right of way. RA-MPCC, not understanding interactions, deems much of the state-space as occupied therefore steering left and right. Eventually, the agent with the right of way has to stop and pass behind, violating the navigation rules.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-A Comparison with Optimization-based MPC", "weight": 1.0} -->

We compare our method to a state-of-the-art optimization-based decentralized motion planner designed for ASVs in urban canals, namely the Regulations Aware Model Predictive Contouring Controller (RA-MPCC). The three scenarios on which we compare are an unprotected left turn (Fig. 5(a) ‣ Figure 6 ‣ IV Experiments ‣ Multi-Agent Path Integral Control for Interaction-Aware Motion Planning in Urban Canals")), a head-on encounter (Fig. 5(b) ‣ Figure 6 ‣ IV Experiments ‣ Multi-Agent Path Integral Control for Interaction-Aware Motion Planning in Urban Canals")) and a crossing (Fig. 5(c) ‣ Figure 6 ‣ IV Experiments ‣ Multi-Agent Path Integral Control for Interaction-Aware Motion Planning in Urban Canals")). These three scenarios were then run 100 times with randomized initial conditions and global goals using the proposed centralized, decentralized, and decentralized with no communication MPPI as well as the RA-MPCC. For all controller types, the randomization was kept equal (i.e. same random seed).

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A Comparison with Optimization-based MPC", "weight": 1.0} -->

Table I summarizes the results, where we compare the number of runs that ended successfully, in a deadlock, or in a collision. Of the runs that ended successfully, we report the number of rule violations. We also report the average time to complete the scenario, defined as the moment in which all agents reach their goal, and the total average distance, which is the sum of the average distances traveled by all agents.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-A Comparison with Optimization-based MPC", "weight": 1.0} -->

All controllers were encouraged through the cost function to keep a velocity around the speed limit (around 1.7m/s). From the table, however, it stands out that the RA-MPCC navigates much slower and therefore has much longer arrival times. This is both because of how its cost function is defined, but also because the RA-MPCC has to plan within convex obstacle-free areas, which can sometimes be quite small and slow down the pace. Instead, MPPI considers the exact occupancy map without any need for pre-processing.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-A Comparison with Optimization-based MPC", "weight": 1.0} -->

While it is easy to give a discontinuous penalty to the MPPI whenever a sample violates a navigation rule, the RA-MPCC has to use continuous cost functions to encourage rule compliance. This, however, inadvertently introduces repulsive forces between the two agents, which then tend to push each other into corners, which is the main cause of deadlocks in the Prinsengracht and the Bloemgracht-Lijnbaansgracht scenarios. In the Bloemgracht head-on encounter, the RA-MPCC gets to its destination only about half of the time. Given that the RA-MPCC has to inflate the ego-agent in a set of circles, the obstacle agent into an ellipsoid, and the static obstacle map has to be pre-processed into convex regions, there is barely enough space to pass in the most narrow section of the canal. This, combined with the lack of understanding that the two agents can cooperate to solve the maneuver, leads to a large number of deadlocks.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-A Comparison with Optimization-based MPC", "weight": 1.0} -->

Collisions with the RA-MPCC instead happen for two reasons. Number one, the method first approximates the static obstacle with polygons, which are then decomposed into convex shapes, to which we can then find linear constraints by solving a quadratic program. However, there is no guarantee that the polygons contain all of the original obstacle. Safety margins are added, but margins too large means that some narrow canals are simply impossible to navigate. Number two, the optimization can often just fail, especially in more difficult and risky situations. When this happens, the algorithm just applies zero input, and if the boat has enough momentum it can drift into a collision.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-A Comparison with Optimization-based MPC", "weight": 1.0} -->

Moreover, while our interaction-aware MPPI could plan with a horizon of 100 steps, the RA-MPPC could only plan 20 steps to meet the 10Hz control loop.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-B Navigation in Crowded Environments", "weight": 1.0} -->

The proposed method is also capable of resolving scenarios with more than two agents. In Table II we show the results for 20 runs in crowded environments with four agents. The experiments are run in the maps shown in Fig. 7, where the vessels are exposed to many encounters in very narrow spaces. The results show that the centralized and decentralized method with shared local goals (with communication) can resolve the task successfully while behaving cooperatively. The decentralized version of our approach with no communication (thus predicting goals for other vessels) incurs in a collision in the tight Bloemgracht's intersection. With the four agents so close to each other, the vessels need to perform large avoidance maneuvers. This causes the estimated local goals and corresponding predictions to diverge drastically from the ground truth. However, similarly to the results in Table I, decentralization has little effect on arrival time, total distance, and rule violations.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C Navigation among Human-piloted Vessels", "weight": 1.0} -->

As long as the human-piloted agent behaves rationally, the resulting trajectories are very similar to the ones presented in Fig. 6, where all agents are autonomous. Therefore, in Fig. 8 we demonstrate how the proposed decentralized MPPI with no communication can cope with irrational agents.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-D Computational Complexity", "weight": 1.0} -->

As previously found in the literature, we confirm that MPPI scales linearly with an increasing number of agents (with constant sample number $K$). Table III shows that the algorithm runs at about 10Hz with two agents, therefore in real-time, and down to less than 4Hz with five agents. We want to stress that this was achieved with parallelization of the sampling procedure over the CPU (Intel® Xeon® W-2123 CPU @ 3.60GHz × 8, 64 GB). Parallelizing this algorithm on a GPU would be highly beneficial, allowing for real-time control of several agents.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Within this work, we developed an MPPI controller for decentralized interaction-aware navigation in urban canals. In multiple sets of randomized scenarios, we demonstrate that our method outperforms a state-of-the-art MPC in terms of success rate, deadlocks, collisions, rule violations, and arrival times. In extensive experiments among several rational autonomous agents and case studies with potentially non-cooperative human drivers, we show robust operation while providing insights into the limitations of the approach. We display that decentralizing the MPPI does not sacrifice performance. Moreover, we demonstrate that the method would be able to run in real-time with multiple agents. In the future, however, a GPU implementation would vastly reduce the computation time. Moreover, the sampling distribution can be improved, thus requiring fewer samples to obtain a good approximation of the optimal control.
