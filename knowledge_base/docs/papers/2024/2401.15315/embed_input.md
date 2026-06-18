<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Online Belief Prediction for Efficient POMDP Planning in Autonomous Driving

Topics include Autonomous driving, POMDPs, Belief-space planning, Belief-state planning, Trajectory prediction.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Learns an online belief-update model for other traffic agents and pairs it with an efficient POMDP planner. The main value is the closed-loop belief-state machinery, which lets predictions adapt as ego intentions and traffic interactions evolve.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Effective decision-making in autonomous driving relies on accurate inference of other traffic agents' future behaviors. To achieve this, we propose an online belief-update-based behavior prediction model and an efficient planner for Partially Observable Markov Decision Processes (POMDPs). We develop a Transformer-based prediction model, enhanced with a recurrent neural memory model, to dynamically update latent belief state and infer the intentions of other agents. The model can also integrate the ego vehicle's intentions to reflect closed-loop interactions among agents, and it learns from both offline data and online interactions. For planning, we employ a Monte-Carlo Tree Search (MCTS) planner with macro actions, which reduces computational complexity by searching over temporally extended action steps. Inside the MCTS planner, we use predicted long-term multi-modal trajectories to approximate future updates, which eliminates iterative belief updating and improves the running efficiency. Our approach also incorporates deep Q-learning (DQN) as a search prior, which significantly improves the performance of the MCTS planner. Experimental results from simulated environments validate the effectiveness of our proposed method.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The online belief update model can significantly enhance the accuracy and temporal consistency of predictions, leading to improved decision-making performance. Employing DQN as a search prior in the MCTS planner considerably boosts its performance and outperforms an imitation learning-based prior. Additionally, we show that the MCTS planning with macro actions substantially outperforms the vanilla method in terms of performance and efficiency.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Decision-making under uncertainties is crucial for the safety of autonomous driving systems. In particular, human traffic participants' behaviors are a primary source of uncertainties, which imposes significant challenges to the safe navigation of autonomous vehicles (AVs) in real-world scenarios. The Partially Observable Markov Decision Process (POMDP) offers a mathematically sound framework to address this problem. However, most POMDP planners in autonomous driving have limited capabilities, as they only represent the hidden states of other agents with specific semantic meanings, which restricts their capability and scalability in complex real-world situations. To overcome this issue, several studies propose enhancing POMDP planning with learned neural network policy and value priors. However, within the context of autonomous driving, learning the state transition function (i.e., predicting the future actions of other agents) is the most challenging part of POMDP planning. Therefore, we aim to integrate POMDP planning with deep learning-based prediction models and develop an online behavior prediction model for effective planning.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

One challenge is adapting the prediction model to an online and closed-loop setting. We propose a neural memory-based belief update model that optimizes closed-loop prediction performance and learns through online interactions. Specifically, our proposed model uses a Transformer-based encoder to map the observation to latent space. At each time step in online training or testing, we utilize a gated recurrent unit (GRU) model to update the latent belief state of the AV about each tracked agent by considering their last latent states, the current latent observations, and the intention of the ego agent. We then employ a decoder to map the latent belief state back into the explicit belief state, represented by distributions of intentions (long-term trajectories) for other agents. Our neural memory model can significantly improve the temporal consistency and probability estimation accuracy of behavior prediction models in online testing. Our model is designed to capture the dynamic interactions between the AV and other agents, as opposed to open-loop conditional prediction models.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another challenge lies in developing a computationally efficient POMDP planner for AVs. We adopt the Monte-Carlo tree search (MCTS) algorithm and incorporate several enhancements. First, we leverage a macro-action-based method that searches over action sequences or motion primitives, allowing a more in-depth search within a limited computation budget. Additionally, we use predicted multi-modal long-term trajectories from the online prediction model to approximate future transitions for other agents within the planning horizon, which improves computational efficiency while ensuring planning performance. Lastly, we train a deep Q-value network based on the environment reward feedback during the online learning process, which is used as the search prior for the MCTS planner.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, we focus on the decision-making under uncertainty problem for AVs, and we have proposed several learning-based enhancements for effective POMDP planning. The core idea of our approach is illustrated in Fig.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a neural memory-based belief update model that provides online and closed-loop agent behavior prediction for AV planning. Refer to Section III-B.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce a macro-action-based MCTS planning method for AVs, which integrates the online prediction model for future approximation and a Q-value function network that acts as a heuristic guide. See Section III-C.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We establish an online learning framework of belief update model and Q-value network and validate our proposed method with a real-world driving dataset and simulated driving environment. Refer to Section III-D.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A Problem Statement", "weight": 1.0} -->

We formulate the AV decision-making problem as a POMDP, which is defined by the tuple $(\mathcal{S},\mathcal{A},\mathcal{O},\mathcal{Z},\mathcal{T},\mathcal{R})$. $\mathcal{S}$ is the state space and $\mathbf{s}_{t}^{i}$ denotes the state of traffic agent $i$ and time $t$. $\mathbf{a}_{t}^{e} \in \mathcal{A}$ is the action space for the ego agent.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A Problem Statement", "weight": 1.0} -->

The ego (decision-making) agent cannot directly observe the internal state $\mathbf{s}^{i}$ of other agents, which can encompass attributes such as the agent's navigational goals, behavioral traits, and intentions. Therefore, the ego agent maintains a belief state $\mathbf{b}_{t} = {\{\mathbf{b}_{t}^{i}\}}_{{i = 1}:N}$ as an estimate of the intentions of its surrounding $N$ agents.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Problem Statement", "weight": 1.0} -->

where $\mathbf{a}^{e}$ is the action of the ego agent.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Problem Statement", "weight": 1.0} -->

We assume that the ego agent makes decisions based on its current belief of the surrounding agents; thus, the entire history of observations is taken into consideration implicitly in the ego agent's actions. We aim to find the approximately optimal ego policy, denoted by $\pi{(\left. \mathbf{a}_{t} \middle| \mathbf{b}_{t} \right.)}$,

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Problem Statement", "weight": 1.0} -->

where $T$ is the horizon and $\gamma \in {}$ is the discount factor.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Problem Statement", "weight": 1.0} -->

Specifically, we represent the state of an agent $\mathbf{s}^{i}$ as its intention or future plan. We maintain a latent belief of the ego agent about the states of other agents, which can be decoded back to an explicit belief state, such as probabilistic intentions or multi-modal future trajectories. To achieve this, we employ an encoder network that maps the observation to a latent space, and a GRU network to update the latent belief state, which is then decoded to possible trajectories per agent. The overall POMDP planning framework is illustrated in Fig. 2.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-B Neural Recurrent Belief Update", "weight": 1.0} -->

Observation. The observation space typically includes the historical trajectories of agents (including the ego) $\mathbf{o}^{a} \in {\mathbb{R}}^{N_{a} \times T_{h} \times D_{a}}$ and map polylines $\mathbf{o}^{m} \in {\mathbb{R}}^{N_{m} \times N_{w} \times D_{m}}$, where $N_{a}$ is the number of agents, $T_{f}$ is the fixed history steps, $N_{m}$ is the number of polylines, and $N_{w}$ is the number of waypoints in a polyline. Note that their positional attributes are normalized according to their respective origin coordinates. We encode the historical states of agents using GRU networks and multi-layer perceptron (MLP) networks to encode the map elements, and we apply max-pooling to reduce the waypoint axis.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B Neural Recurrent Belief Update", "weight": 1.0} -->

Finally, we concatenate these elements to obtain an encoding of the scene $\mathbf{h} \in {\mathbb{R}}^{{({N_{a} + N_{m}})} \times D}$, where $D$ is the hidden feature dimension.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Neural Recurrent Belief Update", "weight": 1.0} -->

Subsequently, we employ a Transformer network with query-centric multi-head attention to extract the relationships between these scene elements in a symmetric manner. Since each agent is encoded in their local coordinates rather than a global coordinate, it is invariant to the position change of the ego agent and thus facilitates belief update. Specifically, we apply pair-wise attention calculation for each query token from encoding $\mathbf{h}$, and the query, key, and value inputs of the attention module are derived as follows.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Neural Recurrent Belief Update", "weight": 1.0} -->

where $i,j$ are the indexes of query tokens, and $PE$ stands for positional encoding, which is a feed-forward network.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Neural Recurrent Belief Update", "weight": 1.0} -->

We denote the encoding process as a function with parameters $f_{\theta}$ and the final encoding as $\mathbf{z} \in {\mathbb{R}}^{{({N_{a} + N_{m}})} \times D}$, and we can retrieve $N$ agents of interest from the scene encoding.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Neural Recurrent Belief Update", "weight": 1.0} -->

Belief Update. We denote the belief update network as $f_{\rho}$, which takes as input the last latent state ${\overset{\sim}{\mathbf{b}}}_{t - 1}^{i} \in {\mathbb{R}}^{D}$, the current encoded observation $\mathbf{z}_{t}^{i}$, and the ego agent's planned actions (short-term trajectory) relative to each agent $\mathbf{a}_{t - 1}^{i,e} \in {\mathbb{R}}^{T_{o} \times 3}$. We define the initial latent belief as ${\overset{\sim}{\mathbf{b}}}_{0}^{i} \triangleq \mathbf{z}_{0}^{i}$, and the belief update process can be formulated as follows.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Neural Recurrent Belief Update", "weight": 1.0} -->

where $\mathbf{b}_{t}^{i}$ represents the explicit belief state, and $f_{\phi}$ is the trajectory decoder network that decodes multi-modal predictions from the latent belief state.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Neural Recurrent Belief Update", "weight": 1.0} -->

The structure of the belief update network is illustrated in Fig. 2(c). We first account for the influence of the ego agent's action on the state of the tracked agent. For this, we use two MLPs - one is utilized to encode the ego agent's relative trajectory, and the other is used to predict a gating value. We use this gating value to control the flow of information to the belief update because some agents may not be influenced by the ego agent. Afterward, the ego agent's influence is combined with the encoded observation to update the belief state through the GRU cell. Note that some agents may be occluded for a few timesteps, and we take the last available belief state of those agents in the update.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Neural Recurrent Belief Update", "weight": 1.0} -->

Trajectory Prediction. Given the latent belief state about an agent ${\overset{\sim}{\mathbf{b}}}_{t}^{i}$, we use an MLP $f_{\phi}$ to decode from the latent belief to explicit belief, which is represented by a Gaussian mixture model (GMM) of future trajectories $\mathbf{b}^{i} \in {\mathbb{R}}^{M \times T_{f} \times D_{f}}$. This GMM comprises $M$ modalities and $T_{f}$ future timesteps, and features at each step include $x$ and $y$ coordinates, variances $\sigma_{x}$ and $\sigma_{y}$, and probability $p$. It is important to note that the decoder $f_{\phi}$ can also be used for the encoded observation $\mathbf{z}^{i}$, as in most existing offline motion prediction models.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-C Macro-action-based MCTS Planner", "weight": 1.0} -->

We use the belief state of the ego agent over other agents $\mathbf{b}_{t} = {\{\mathbf{b}_{t}^{i}\}}_{{i = 1}:N}$ to approximate the future updates within the planning horizon (multi-modal long-term trajectories). This effectively simplifies the POMDP problem into a belief-state MDP, which can be efficiently solved using the MCTS algorithm. We employ receding horizon planning and construct a new policy for the current belief each time a new observation is received. Furthermore, to optimize the quality and efficiency of the MCTS planner, we employ macro-actions.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-C Macro-action-based MCTS Planner", "weight": 1.0} -->

Macro-actions. A macro-action is a sequence of instantaneous actions over a time duration, and they can be learned from data and differ in length. For simplicity, we employ fixed-length heuristic macro-actions (high-level discrete intentions, such as overtaking and turning). We assume that the routing module provides a reference path, such that we can generate macro-actions based on this reference path.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-C Macro-action-based MCTS Planner", "weight": 1.0} -->

where $s$ and $l$ represent the longitudinal and lateral directions along the reference path, $s{}$, $l{}$, $\overset{˙}{s}{}$ are the initial state of the node, $\Delta\tau$ is the time interval, and $T_{o}$ is the macro-action length. Then, we can transform the states in the Frenet frame back into the Cartesian frame $\left( {x{(\tau)}},{y{(\tau)}},{v{(\tau)}},{a{(\tau)}} \right)$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-C Macro-action-based MCTS Planner", "weight": 1.0} -->

Objective Function. We calculate the cost of macro-actions considering collision risk, ride comfort, deviation from the route, and desired speed.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-C Macro-action-based MCTS Planner", "weight": 1.0} -->

where $T_{d} = \frac{T_{f}}{T_{o}}$ is the search depth, $w_{i}$ is the weight, and $c_{i}$ is the cost term at time segment $n$. The ride comfort factor includes acceleration, jerk, and lateral acceleration of the trajectory, and the desired speed cost is the difference between the current speed and speed limit. Each cost term is averaged across all timesteps in the node.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-C Macro-action-based MCTS Planner", "weight": 1.0} -->

where $\mathbf{s}^{e}$ is the state of the ego agent determined by the generated macro-actions, $\mathbf{b}^{i}{(j)}$ is the $j$-th predicted trajectory of agent $i$, $p_{j}$ is the predicted likelihood of that trajectory. $\mathbb{1}_{overlap}$ is a binary indicator to check whether the two trajectories collide, and $p_{th}$ is a threshold to filter out low probability futures.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-C Macro-action-based MCTS Planner", "weight": 1.0} -->

1:MCTS planner TP, observation encoder fθ, belief update network fρ, trajectory decoder fϕ, Q-value network Qϵ, N number of predicted agents.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-C Macro-action-based MCTS Planner", "weight": 1.0} -->

tracker $B\leftarrow{B \cup {\{{\overset{\sim}{\mathbf{b}}}_{t}^{i}\}}}$ 14: Decode probabilistic trajectories $\mathbf{b}_{t}^{i} = {f_{\phi}{({\overset{\sim}{\mathbf{b}}}_{t}^{i})}}$ 16: Calculate prior Pr(zte,ae) for root node using Eq. 9 17: Compute action sequence a* ← TP({bti}i = 1: N,Pr) 18: Execute first action ate ← a0* Algorithm 1 MCTS with online belief prediction model

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-C Macro-action-based MCTS Planner", "weight": 1.0} -->

MCTS Algorithm. MCTS consists of several key steps: selection, expansion, evaluation, and backup, and this process is repeated multiple times until a termination condition is reached. We focus on the selection step in the following, and more details about MCTS can be found.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-C Macro-action-based MCTS Planner", "weight": 1.0} -->

where $\overset{\sim}{Q}{(s,a)}$ is the expected return, $n_{a}$ is the number of times the node has been visited, $N_{p}$ is the total number of times the parent node has been visited, and $C_{p}$ is a temperature parameter used to balance exploration and exploitation.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-C Macro-action-based MCTS Planner", "weight": 1.0} -->

DQN Guidance. DQN is used in MCTS as an action prior to bias exploring high-rewarding areas in the search tree. The prior $Pr{(a)}$ is given by the learned Q-value network $Q_{\epsilon}$, and we apply this prior to the root node, while setting the prior to a uniform distribution in other nodes.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-C Macro-action-based MCTS Planner", "weight": 1.0} -->

where $\mathbf{z}_{t}^{e}$ is the encoded observation state for the ego agent at the current time, which is retrieved from the observation encoder and contains necessary information including its past states, other agents, and road maps.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-C Macro-action-based MCTS Planner", "weight": 1.0} -->

The proposed POMDP deep predictive planning algorithm can be summarized in Algorithm 1.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-D Learning Framework", "weight": 1.0} -->

Offline Learning. In this stage, we train the observation encoder $f_{\theta}$ with the multi-modal trajectory decoder $f_{\phi}$ using an offline driving dataset. We employ the following loss on the selected positive GMM component (the mode with the smallest L2 distance to ground truth) for a specific agent at a future time step.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-D Learning Framework", "weight": 1.0} -->

1:pre-trained observation encoder fθ, belief update network fρ, trajectory decoder fϕ, twin Q-value network Qϵ1, 2, training steps Nt, exploration rate λ
2:Initialize the replay buffer R
4: Initialize episodic observation buffer O and trajectory
6: while episode not terminated do
7: Collect and store agent observations in O
8: Encode observations to latent space z using fθ
9: Predict trajectories using fρ and fϕ and store in P
10: Select action a: with probability λ, sample random
11: action; otherwise use MCTS planner
12: Execute action a, observe reward r, and obtain
13: next latent state z′
14: Store transition (z,a,r,z′) in replay buffer R
15: Update Qϵ1, 2 by sampling from R
17: Update fρ and fϕ using prediction results from P and
18: ground truth data from O in hindsight
20:return Trained networks fρ, fϕ, Qϵ1
Algorithm 2 Online learning process

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-D Learning Framework", "weight": 1.0} -->

Online Learning. In this stage, we fix the weights of the observation encoder and learn the belief update model $f_{\rho}$ and fine-tune the trajectory decoder $f_{\phi}$ in a driving simulator. At the end of an episode, we obtain a prediction buffer and an observation buffer that contains the positions of all agents at each timestep. We utilize the GMM loss in Eq. 10 to minimize the prediction loss at each valid time step in hindsight. In addition, we leverage the clipped double Q-learning to learn a Q-value network $Q_{\epsilon}$ to guide the tree search planner.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-D Learning Framework", "weight": 1.0} -->

where $r_{col} = {- 10}$ is the penalty imposed if the ego vehicle collides with any other agents, $r_{prog}$ is the distance traveled by the ego vehicle, and $r_{expert}$ is the state difference between the agent and logged human expert, which could encode other driving features that are hard to manually design. Since the true state of the environment can only be obtained at the current step, and future states are approximated by the model, the Q-value network is used to guide the selection at the root node.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-D Learning Framework", "weight": 1.0} -->

We jointly learn the belief update and Q-network (with the MCTS planner) to improve the overall decision-making performance. The procedure for online belief update model learning and Q-learning is summarized in Algorithm 2.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-A Dataset and Simulator", "weight": 1.0} -->

We employ the Waymo Open Motion Dataset (WOMD) to train the models and replay the traffic data for surrounding agents in the MetaDrive simulator to conduct online training and testing. Additionally, we set the agent behavior to be reactive in the simulator, allowing other agents to perform basic reactive actions, such as avoiding collisions from the rear end of the ego vehicle. Fig. 3 shows a replayed scenario from WOMD in the MetaDrive simulator and the obtained observation space for the ego agent.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-B Implementation Details", "weight": 1.0} -->

Data. In the offline learning stage, we select 20,000 scenarios from the WOMD, each with a duration of 20 seconds. For online learning, we randomly choose 2,000 scenarios from the training set for simulation-based replay. In the testing phase, we select an additional 200 scenarios from the WOMD. Note that we exclude static scenarios where the ego vehicle travels less than 20 meters, such as waiting at red lights.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-B Implementation Details", "weight": 1.0} -->

Neural Networks. We select the closest $N_{a} = 16$ agents to the ego vehicle and their observed historical horizon is $T_{h} = 20$ timesteps. Additionally, we incorporate $N_{m} = 50$ map polylines in encoding, each comprising $N_{w} = 20$ waypoints. The Transformer encoder has $3$ attention layers and a hidden dimension of $D = 256$. The trajectory decoder outputs $M = 6$ possible trajectories for an agent, $8$ seconds into the future $T_{f} = 80$. In the belief update network, the ego agent's action is represented by a short-term trajectory ($T_{o} = 20$), which is processed relative to each tracked agent and encoded. The Q-value network is an MLP that takes as input the hidden state of the ego agent and outputs the values of actions.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-B Implementation Details", "weight": 1.0} -->

MCTS Planner. The planning horizon is set to $T_{f} = 80$ timesteps, with a time interval of ${\Delta t} = {0.1s}$, and the option length is set to $T_{o} = 20$. This significantly reduces the search depth to $T_{d} = 4$. We track the belief states of $N = 8$ agents and set the probability threshold for calculating collision risk to $p_{th} = 0.15$. The options at each node are derived from combinations of lateral velocity $v_{l} = {{{\lbrack{- 1},0,1\rbrack}m}/s}$ and longitudinal acceleration $a = {{{\lbrack{- 4},{- 2},0,1,3\rbrack}m}/s^{2}}$. Lateral velocity is only considered if the acceleration is ${- 2},0,1$, leading to a total of $11$ options. We also ensure that the velocity remains non-negative.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-B Implementation Details", "weight": 1.0} -->

The planner executes a total of $100$ search iterations and applies a discount factor $\gamma = 0.8$ and temperature parameter $C_{p} = 100$ after careful tuning.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-B Implementation Details", "weight": 1.0} -->

Offline learning. We utilize the AdamW optimizer for model training, conducting $40$ training epochs. The learning rate begins at ${2e} - 4$ and is halved every $5$ epochs. The model is trained on an NVIDIA A100 GPU with a batch size of 256.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-B Implementation Details", "weight": 1.0} -->

Online Learning. We train the models in the simulator with $N_{t} = {300,000}$ steps. We employ Adam optimizer to train the networks and the learning rate starts with ${3e} - 4$ and reduces by $30\%$ every $50,000$ steps. The exploration rate $\lambda$ starts with $0.8$ and decays to $0.05$ in the middle of training. The discount factor for Q-learning is $\gamma = 0.99$, the replay buffer size is $100,000$, and the batch size is $128$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-B Implementation Details", "weight": 1.0} -->

Testing. The runtime of the prediction model and MCTS planner is tested on a laptop equipped with an AMD 7945HX CPU and NVIDIA RTX 4060 GPU.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-C Main Results", "weight": 1.0} -->

Baselines. In testing, we compare our method against several strong baseline approaches: RL (DQN) method, intelligent driver model (IDM), and differentiable integrated prediction and planning (DIPP). We also integrate well-established trajectory prediction models from the WOMD benchmark, such as MTR and GameFormer, into the MCTS planner to test their performance on planning. To ensure a fair comparison, we scale down these models to match the size of ours and train them using the same dataset.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-C Main Results", "weight": 1.0} -->

Moreover, we introduce several ablated versions of our approach. The offline model denotes the prediction model that operates without online belief updates (i.e., decoding trajectories directly from encoded observations), and is only trained on the offline dataset. The proposed online update model has two variants: one incorporates the ego agent's intentions in the online belief update, and the other does not. Furthermore, we evaluate the effectiveness of employing imitation learning (IL) (i.e., predicted future trajectory for the ego vehicle) and DQN as prior in the MCTS planner. For training comparisons, we introduce two baselines: a DQN agent and an MCTS planner that includes an online belief update model but omits Q-learning.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-C Main Results", "weight": 1.0} -->

Metrics. The task-related metrics include success rate, average episode reward, task time (defined as the average number of steps per episode), and average log divergence (L2 distance) measuring the deviation of the ego vehicle from logged behavior. Regarding prediction performance, we employ three key metrics: minimum average displacement error (minADE), consistency (variation in predictions across consecutive frames), and score accuracy (whether the highest probability is correctly assigned to the closest modality to the ground truth).

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-C Main Results", "weight": 1.0} -->

where $\mathbf{b}_{t - 1}$ is the prediction result from the last time frame, and this metric is averaged across all timesteps in the episode.

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-C Main Results", "weight": 1.0} -->

Training Results. We train different methods using three random seeds, and the training results are depicted in Fig. 4. The DQN agent shows the worst performance in terms of success rate, and learning the online prediction model without Q-learning significantly influences the MCTS planner's effectiveness, mainly due to the deviation from expert trajectories. While the MCTS planner with an online prediction model and deep Q-learning shows favorable effectiveness, its performance can be further enhanced with the online model that integrates the ego agent's intentions into the belief update process. This approach achieves the highest reward, highlighting the efficacy of closed-loop interaction modeling.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-C Main Results", "weight": 1.0} -->

MCTS + DQN + Online update (w/ ego)

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-C Main Results", "weight": 1.0} -->

Testing Results. We evaluate our proposed method against other baselines in the testing scenarios, and the results are summarized in Table I. The key conclusions and findings are as follows. The DQN agent shows the weakest performance, while the rule-based IDM agent and the optimization-based DIPP method are more effective. Using established prediction models with our DQN-guided MCTS planner shows comparable performance to our offline-trained model but is less effective in planning than the online prediction model. The basic MCTS method without DQN guidance performs significantly worse, and DQN guidance is more effective than IL guidance. The prediction consistency of offline models is substantially worse than that of online belief update models. While offering similar prediction accuracy, the online belief update model significantly enhances prediction consistency and the accuracy of intention probability estimations, leading to improved decision-making performance. Incorporating the ego vehicle's intention into the belief update process in the online prediction model can further improve the decision-making performance in terms of the episode reward. Some qualitative results are presented in Fig. 5, which reveal that our proposed online update model provides more consistent and accurate trajectory predictions of interacting agents compared to the offline prediction model.

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-C Main Results", "weight": 1.0} -->

The online prediction model can continuously improve its prediction accuracy (in terms of trajectory ADE and probability) by receiving new observations over time. The closed-loop testing results showcase the online prediction model's much better prediction consistency.

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-D Ablation Study", "weight": 1.0} -->

Influence of macro-action length. We investigate the impact of varying macro-action lengths on the performance of the MCTS planner, as detailed in Table II. We find that shorter action lengths lead to increased computation time and lower success rate and episode reward. This is because, within a limited number of search iterations, a deeper search depth makes it increasingly difficult to find better actions. Conversely, extending the macro-action length to 40, which essentially simplifies the process into two-stage planning, yields a success rate comparable to a macro-action length of 20, but the episode reward at this length is reduced. Consequently, a macro-action length of 20 appears to provide a good balance between performance and computational efficiency.

<!-- chunk {"id": "body-0062", "role": "body", "section": "IV-D Ablation Study", "weight": 1.0} -->

Influence of probability threshold. We examine the effects of the probability threshold in the collision risk cost (Eq. 7) on planning performance. Setting $p_{th} = 0$ includes all predicted futures in planning, and we also set up an alternative approach that only considers the most likely predicted future. The results in Table III reveal that incorporating all uncertainties yields a high success rate but a lower episode reward compared to $p_{th} = 0.15$. This indicates that while accounting for all uncertainties ensures task completion, it often results in deviations from the human trajectory and thus decreased rewards. Utilizing the most likely future leads to suboptimal performance in terms of both success and reward, highlighting the limitations of optimistic planning strategies.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We develop an online behavior prediction model for POMDP planning in autonomous driving. Specifically, we propose a recurrent neural belief update model and a macro-action-based MCTS planner guided by deep Q-learning. We introduce an online learning framework, which combines belief update learning and deep Q-learning to guide tree search. We validate our framework in simulated environments based on real-world driving scenarios. The experimental results indicate that our proposed online belief update model can significantly improve temporal consistency and accuracy. Furthermore, DQN guidance considerably boosts the efficacy of the MCTS planner, resulting in improved decision-making performance. Future research could extend this framework to broader POMDP settings by learning to update both actual physical states and future intentions. Moreover, the macro-action generation process can be improved by learning from expert data and by making the macro-actions more flexible in terms of their length, manipulation, and termination criteria.
