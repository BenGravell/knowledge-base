<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Planning by Simulation: Motion Planning with Learning-Based Parallel Scenario Prediction for Autonomous Driving

Topics include Autonomous driving, Motion planning, Scenario generation, Simulation, Trajectory prediction.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces Planning by Simulation, where parallel learned scenario prediction evaluates candidate ego plans by simulating how surrounding agents may respond. The paper targets the feedback loop between planning and prediction rather than treating forecast accuracy as a standalone objective.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Planning safe trajectories for autonomous vehicles is essential for operational safety but remains extremely challenging due to the complex interactions among traffic participants. Recent autonomous driving frameworks have focused on improving prediction accuracy to explicitly model these interactions. However, some methods overlook the significant influence of the ego vehicle's planning on the possible trajectories of other agents, which can alter prediction accuracy and lead to unsafe planning decisions. In this paper, we propose a novel motion Planning approach by Simulation with learning-based parallel scenario prediction (PS). PS deduces predictions iteratively based on Monte Carlo Tree Search (MCTS), jointly inferring scenarios that cooperate with the ego vehicle's planning set. Our method simulates possible scenes and calculates their costs after the ego vehicle executes potential actions. To balance and prune unreasonable actions and scenarios, we adopt MCTS as the foundation to explore possible future interactions encoded within the prediction network. Moreover, the query-centric trajectory prediction streamlines our scene generation, enabling a sophisticated framework that captures the mutual influence between other agents' predictions and the ego vehicle's planning. We evaluate our framework on the Argoverse 2 dataset, and the results demonstrate that our approach effectively achieves parallel ego vehicle planning.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In autonomous driving, the fundamental capacity is to make efficient, safe, and human-like decisions. Both interpretable and inexplicable methods have emerged in research on how to make better decisions. A growing trend of leveraging large-scale data in end-to-end learning-based planning has been shown in recent years. End-to-end autonomous driving systems are fully differentiable programs that take raw sensor data as input and produce a decision as output. This jointly optimized solution has shown actual improvements in driving. However, uncertainty from surrounding vehicles and pedestrians may significantly affect the robustness of end-to-end systems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Recently, large language model has sprung up and demonstrates abilities to empower autonomous driving in logical reasoning and generating answers. OpenAI o1, the latest large language model, achieves complicated logical inference in high-level physics and coding problems. Unlike the early large language model, OpenAI o1 embeds a long internal chain of thought after pre-training and post-training, which helps replanning and self-modification to improve robustness. Inspired by these thoughts, we propose a new end-to-end framework like OpenAI o1, which conducts robust search based on end-to-end predictions. Different from directly outputting a single trajectory from end-to-end models, we use learned-based scenario prediction as a parallelizable simulator and plan by choosing the best out of different possible futures, as shown in Figure 1.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Prediction provides possible trajectories of vehicles and pedestrians for downstream decisions. Note that the prediction in this paper is scenario oriented, which means that not only other traffic participants but also the ego vehicle (e2e planning) are predicted simultaneously.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In view of the multi-modality of prediction, not all planning modules are suitable for combining with prediction. Monte Carlo tree search (MCTS), an intelligent tree search method that balances exploration and exploitation, has a natural advantage on unfolding parallel circumstances of multiple possible decisions, which dramatically helps evaluate cost. Some works propose a deep-learning heuristic MCTS algorithm to simulate surrounding space during planning. Although they have achieved competitive results, there remain two main drawbacks: Preordered nodes are repeatedly used while predicting the latest circumstance. These models fail to reuse past computations and operate streamingly. These methods define discrete yaw rates and accelerated speed as action sets. A finite discrete action set may cause the planned trajectory to have a nonnegligible gap with the actual trajectory. Besides, the expansion of the search tree may generate an unreasonable branch that contradicts the laws of physics.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Most prediction networks combined with search-based planning are agent-centric modeling scheme. They require re-normalizing and re-encoding the input whenever the observation window slides forward, leading to redundant computations if they are directly and repeatedly invoked. Query-centric trajectory prediction, different from agent-centric prediction, enables the reuse of past computations by learning representations independent of the global spacetime coordinate system. Sharing the invariant scene features among all target agents in the Monte Carlo search tree further allows the parallelism of simulating tree-like future.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Motivated by these observations, we propose an iterative motion Planning by Simulation through learning-based parallel scenario prediction (PS) for autonomous driving based on MCTS, as shown in Figure 2. Our model first generates an optional action set and then cooperates ego vehicle actions and other agents' future trajectories to ratiocinate future scenarios in parallel. The major contributions of this paper are summarized as: A planning framework with data-driven interaction-aware inference capabilities, which is more robust than pure learning-based planning and more scalable than rule-based counterpart.

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

An iterative planning structure guided by trajectory prediction, which in turn influences the prediction results.

<!-- chunk {"id": "body-0011", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

A reliable and efficient planning set generation method, along with a reusable prediction network based on coordinate transformation. Comprehensive experiments and comparisons are conducted to validate the performance.

<!-- chunk {"id": "body-0012", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The related literature is reviewed in section II. Our method is detailed in section III. Experimental results are elaborated in section IV. Finally, a conclusion is drawn in section V.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A MCTS-based Planning", "weight": 1.0} -->

MCTS is a searching algorithm that combines the classical tree search and reinforcement learning. AlphaGo and AlphaZero have defeated human world champions by combining an MCTS with deep reinforcement learning. Originating from similar game theory and artificial intelligence, MCTS also has applications in various autonomous fields, showcasing its adaptability and robustness. It is suitable for various tasks in multi-robot active perception. In autonomous driving control, MCTS has been leveraged to enhance feedback steering controllers for autonomous vehicles. By adapting MCTS to behavior planning, some works harness their intrinsic ability to balance exploration and exploitation, making it well-suited to the intricate, and uncertain nature of real-world traffic scenarios.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Frenét Frame Trajectory Generation", "weight": 1.0} -->

Rather than formulating the trajectory generation problem directly in Cartesian Coordinates, the Frenét frame method switches to find the best lateral and longitudinal acceleration changes along the dynamic reference lane. Some works augment decision-making with Frenét frame path generator, improving the pedestrian handling ability by predicting their behavior. Other works project the semantic elements to the Frenét frame representation to provide a constraint-satisfied trajectory. In addition, Frenét frame-based planners also perform well at high-speed driving scenarios. However, few works incorporate the Frenét frame with a tree-like planner.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-C Query-centric Trajectory Prediction", "weight": 1.0} -->

A critical design in trajectory prediction is the reference coordinate system in which the representation is encoded, which would influence efficiency connected with planning. Scene-centric coordinate frame, sharing representation of world state, may sacrifice pose-invariance. Agent-coordinate frame, which is intrinsically pose-invariant, scales linearly with the number of agents. They do not support being partially tested when a small part of historical trajectories have changed. Query-centric methods, encoding relative information, avoid the above problems and are suitable for tree search-based planners. This frame can also be used in end-to-end autonomous driving, where the sparse queries completely represent the whole driving scenario across space and time.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-D Interactive Prediction and Planning", "weight": 1.0} -->

In classical autonomous vehicle tasks, separating prediction and planning layers limits the planner to reacting to predictions uninformed by the ego planned trajectory. Some works couple these layers via game theory that uses a novel interactive multi-agent neural network policy as part of its predictive model. DTPP introduces a query-centric Transformer model that performs efficient ego-conditioned motion prediction, which guides tree-simulation planner to be pruned and expanded.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-D Interactive Prediction and Planning", "weight": 1.0} -->

Our method is different from previous works. We introduce MCTS as a comprehensive decision-making framework for behavior planning, integrating Frenét frame to generate driving actions, which achieves layer-by-layer development of future scenarios. Besides, we utilize query-centric encoding framework to predict new nodes in our planner.

<!-- chunk {"id": "body-0018", "role": "body", "section": "METHOD", "weight": 1.0} -->

The proposed framework with its associated prediction model is illustrated in Figure 2. Our planner is based on top of MCTS, with node pruning enabled by Frenét frame and cost evaluation. Besides, deep integration with trajectory prediction model significantly improves planning performance and efficiency. The key idea behind tree-structured planning is to approximate the intractable continuous-space policy planning problem by sampling a discrete set of ego trajectories in multiple stages. This structure forms a trajectory tree. Together with predicting the motion of other agents conditioned on each ego trajectory segment, we get a scenario tree. Given a sequence of past observed states $\left\{ s_{1}^{t},s_{2}^{t},\ldots,s_{N}^{t} \right\}_{t = 1}^{T}$, and high-definition map information $M$, we aim to choose the most appropriate action $a \in A$ for ego agent to carry out at time $T + 1$ that minimize cost $C$. $N$ represents the number of agents in the scene.

<!-- chunk {"id": "body-0019", "role": "body", "section": "METHOD", "weight": 1.0} -->

1:sequence of past observed states {s1t, s2t, …, sNt}t = 1T and high-definition map information M 2:the most appropriate action a 3:function Select Action(sn = 1, …, NT, d) Algorithm 1 Planning Process

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Planning Process", "weight": 1.0} -->

Our proposed planning algorithm is outlined in Algorithm 1. We set $\left\{ s_{n}^{i} \right\}_{n = 1}^{N}$,$i \geq T$ as node states in the tree, amongst $s_{n}^{i} = \left( x_{n}^{i},y_{n}^{i},{v(x)_{n}^{i}},{v(y)_{n}^{i}},\theta_{n}^{i} \right)$, separately representing the $x$ axis and $y$ axis position, $x$ axis and $y$ axis velocity and steering angle. Different from normal binary action setting in autonomous driving, we define action $A = \left\{ 0.5,1.5,\ldots,13.5,14.5 \right\}$ as the target speed set calculated for Frenét frame, which further generates paths in accordance with the law of kinematics alongside road center line.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Planning Process", "weight": 1.0} -->

12: $a\leftarrow{{{argmax}_{a}Q(s,a)} + {c\sqrt{\frac{{\log N}{(s)}}{N{(s,a)}}}}}$ Algorithm 2 Simulation Process As outlined in Algorithm 2 and as shown in Figure 3, The basic steps of our planner are similar to traditional MCTS. First, the selection step chooses a node that maximizes the upper confidence bound (UCB) near the current node. UCB helps balance exploration and exploitation. Once reaching a state that is not part of the explored set, new leaves are expanded by iterating over all possible actions at the expansion step. After that, many random simulations are performed to a fixed depth to evaluate the value of the leaves at the rollout step. We simulate the final scene from the leaf node by setting the ego vehicle's random action. Finally, the statistics of all selected nodes are updated through backpropagation. With these four steps, our planner generates a growing asymmetric tree through continuous iterations until we meet a maximum number of simulations and the car has reached the goal point.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Planning Process", "weight": 1.0} -->

Then we evaluate the performance and execute the action with maximum reward.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Planning Process", "weight": 1.0} -->

During the search, at selection step, we execute the action $a \in A$ that maximizes ${Q(s,a)} + {c\sqrt{\frac{{\log N}{(s)}}{N{(s,a)}}}}$, where $N(s)$ and $N(s,a)$ track the number of times that a state and state-action pair are visited. Here $c$ is a hyper-parameter controlling the amount of exploration in the search. It encourages exploring less visited $(s,a)$ pairs and relies on $Q(s,a)$ to estimate well explored pairs.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Planning Process", "weight": 1.0} -->

Our mean novelty is how to create child nodes given a target speed. Instead of using a single kinematic model, we update the ego vehicle state through the optimal Frenét frame method and update other agents by jointly predicting using selected nodes under the scene.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-A Implementation Details", "weight": 1.0} -->

We evaluate our method in simulations of diverse urban driving scenarios from Argoverse 2, with a 5-second observation window and a 6-second planning horizon at 10 Hz. The goal is to assess our model's planning in real-world scenarios. In the simulation, dynamic agents potentially interact with each other. Our route planner aims to find an appropriate route for the ego-vehicle to execute under 5 seconds agents' trajectories and lane polygons. All the experiments are conducted on a desktop equipped with an Intel I7-8700K CPU and a single NVIDIA RTX 4090.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B Scenarios and Results", "weight": 1.0} -->

To verify that our proposed method can automatically adapt to different traffic conditions with different semantic information, we present our planner results of four representative test cases and what will happen if ego vehicle does not operate our actions. 1) Vehicles in the opposing lanes make a left turn. As illustrated in Figure 6-(a), it is used to verify the capability of dynamically adjusting speed changes facing uncertain hinder and keeping among the speed limit at the same time. We can see that improper speed change may cause a collision or a hard brake. 2) The ego vehicle initiates a left lane change into the gap between two adjacent vehicles. This case is to validate the capability of dealing with rapidly approaching vehicles from the rear and rear-side. As illustrated in Figure 6-(b), our method conducts a safe and smooth lane change without collision with sluggish front care and aggressive rear vehicle. 3) Target vehicle at the intersection merges. This scenario shows that our method plans efficient trajectories when the lateral vehicle at the intersection tries to merge into the traffic flow. As shown in Figure 6-(c), the inadequate plan may cause a rear end or exceed the speed limit. 4) Ego vehicle overtakes on crowded road.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-B Scenarios and Results", "weight": 1.0} -->

This case is used to verify the capability of quickly responding to complex interactions with other agents during traffic negotiation. As shown in Figure 6-(d), when the front vehicle suddenly stops, and the ego vehicle has to change lanes with a rapidly moving vehicle, our method efficiently finds safe and feasible trajectories.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-C Comparisons", "weight": 1.0} -->

We compared the following algorithms in scenarios S1--S4. To highlight the concept of query-centric trajectory modeling, we employed a rule-based prediction approach, specifically utilizing a constant velocity lane-following strategy. This method is referred to as PS-Rule in the table. To prove the necessity of cyclic utilization between prediction and planning, we tested only inferring prediction once for each action, named as PS-Niter. Specifically, we applied a fixed action set rather than our adaptive action generation in the third ablation study, denoted as PS-Fix in the table.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-C Comparisons", "weight": 1.0} -->

We use three metrics to evaluate the performance of these methods: completion Time, average velocity and collision distance. Completion Time and average velocity relate to efficiency. They evaluate how fast we reach a target while complying with some speed limitations. Collision distance shows the minimized distance between surrounding agents and the ego vehicle. These three indexes are abbreviated as C.T., A.V., and C.D., respectively, in Table I.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-C Comparisons", "weight": 1.0} -->

In Scenario 1, while the fixed action set method aims to enable the vehicle to reach the target point more efficiently, it results in an average speed exceeding the 15 m/s limit. In Scenarios 2 and 4, certain ablation methods lead to collisions. For Scenario 3, both the rule-based prediction method and the fixed action set method may cause abrupt acceleration.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-C Comparisons", "weight": 1.0} -->

Utilizing prediction methods Forecast-MAE and FJMP from Argoverse 2, we conducted evaluations across the four aforementioned scenarios. Extra metrics Planning Error (P.E.) from actual planning trajectory is calculated. The results are averaged, yielding the data presented in Table II. We can see that PS has faster completion time than planners with prediction that output trajectories directly.

<!-- chunk {"id": "body-0032", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

In this paper, we present a trajectory planning system, PS, that integrates planning and prediction by inferring potential trajectories of surrounding agents through an Monte Carlo search tree. The system continuously predicts future trajectories by feeding ego vehicle plans into the search tree, enabling dynamic trajectory exploration. The use of a Frenét frame-based ego planner and query-driven trajectory encoding ensures efficient and feasible nodes expansion within the search tree. Our proposed approach supports parallel scene simulations with reasonable actions. Key future research directions include developing cost learning mechanisms to replace the fixed cost function and adopting trajectory prediction based on continuous action sets.
