<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Imitation Is Not Enough: Robustifying Imitation with Reinforcement Learning for Challenging Driving Scenarios

Topics include Imitation learning, Reinforcement learning, Autonomous driving, Robustness, Closed-loop evaluation, Safety.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Shows that large-scale behavior cloning for urban driving can be materially improved by reinforcement learning with simple safety- and reliability-oriented rewards. The paper is useful as evidence that imitation alone can under-handle rare and challenging driving scenarios even when the demonstration corpus is very large.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Imitation learning (IL) is a simple and powerful way to use high-quality human driving data, which can be collected at scale, to produce human-like behavior. However, policies based on imitation learning alone often fail to sufficiently account for safety and reliability concerns. In this paper, we show how imitation learning combined with reinforcement learning using simple rewards can substantially improve the safety and reliability of driving policies over those learned from imitation alone. In particular, we train a policy on over 100k miles of urban driving data, and measure its effectiveness in test scenarios grouped by different levels of collision likelihood. Our analysis shows that while imitation can perform well in low-difficulty scenarios that are well-covered by the demonstration data, our proposed approach significantly improves robustness on the most challenging scenarios (over 38% reduction in failures). To our knowledge, this is the first application of a combined imitation and reinforcement learning approach in autonomous driving that utilizes large amounts of real-world human driving data.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Building an autonomous driving system that is deployable at scale presents many difficulties. First and foremost is the challenge of handling the numerous rare and challenging edge cases that occur in real-world driving. To this end, imitative learning based approaches have been proposed that allow the performance of the method to scale with the amount of data available. While situations that are well represented in the demonstration data are likely to be handled correctly by such a policy, more unusual or dangerous situations that occur only rarely in the data might cause the imitation policy -- which has not been explicitly instructed on what constitutes a risky or inappropriate response -- to respond unpredictably. The problem is compounded by complex interactions, where human expert driving data in similar scenarios may be scarce and sub-optimal.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Reinforcement Learning (RL) has the potential to resolve this by leveraging explicit reward functions that tell the policy what constitutes safe or unsafe outcomes (e.g., collisions). Furthermore, because RL methods train in closed-loop, RL policies can establish causal relationships between observations, actions, and outcomes. This yields policies that are less vulnerable to covariate shifts and spurious correlations commonly seen in open loop IL, and aware of safety considerations encoded in their reward function, but which are only implicit in the demonstrations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

However, relying on RL alone, e.g. is also problematic because it heavily depends on reward design, which is an open challenge in autonomous driving. Without accounting for imitation fidelity, driving policies trained with RL may be technically safe but unnatural, and may have a hard time making forward progress in situations that demand human-like driving behavior to coordinate with other agents and follow driving conventions. IL and RL offer complementary strengths: IL increases realism and eases the reward design burden and RL improves safety and robustness, especially in rare and challenging scenarios in the absence of abundant data (Fig. 1).

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In this paper we focus on the driving scenarios that are most likely to exhibit safety and reliability concerns, leveraging the difficulty estimation. Our proposed method, BC-SAC, combines IL and RL with a *simple* reward function, and trains on difficult driving scenarios. Difficulty is estimated via a classifier that estimates the likelihood of a collision or near-miss when re-simulated with a pre-trained planning policy. Our proposed reward function enforces safety of the agent, while natural driving behaviors are implicitly learned with IL. The training data comes from a subset of real-world human driving data (over 100k miles of real-world urban driving data). We demonstrate that this approach substantially improves the safety and reliability of policies learned over imitation alone without compromising on human-like behavior, showing 38% and 40% improvements over pure IL and RL baselines.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The main contributions of our work are: We conduct the first large-scale application of a combined IL and RL approach in autonomous driving utilizing large amounts of real-world urban human driving data (over 100k miles) and a *simple* reward function. We systematically evaluate its performance and baseline performance by slicing the dataset by difficulty, demonstrating that combining IL and RL improves safety and reliability of policies over those learned from imitation alone (over 38% reduction in safety events on the most difficult bucket).

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Adversarial Imitation/IRL
IRL, GAIL, MGAIL

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-A Markov Decision Processes (MDPs)", "weight": 1.0} -->

In this work, we cast the autonomous driving policies learning problem as a Markov decision process. Following standard formalism, we define an MDP as a tuple $\{\mathcal{S},\mathcal{A},\mathcal{T},\mathcal{R},\gamma,\rho_{0}\}$. $\mathcal{S}$ and $\mathcal{A}$ denote the state and action spaces, respectively. $\mathcal{T}$ denotes to transition model. $\mathcal{R}$ represents the reward function, and $\gamma$ represents the discount factor. $\rho_{0}$ represents the initial state distribution.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-B Imitation Learning (IL)", "weight": 1.0} -->

IL constructs an optimal policy by mimicking an expert. We assume an expert (an optimal policy), denoted as $\pi_{\beta}$, produces a dataset of trajectories $\mathcal{D} = {\{ s_{0},a_{0},\cdots,s_{N},a_{N}\}}$ through interaction with the environment. The learner's goal is to train a policy $\pi$ that imitates the $\pi_{\beta}$. In practice, we only observe the expert states, so we estimate expert actions using inverse dynamics. For example, behavioral cloning (BC) trains the policy via a log-likelihood objective, ${\mathbb{E}}_{{s,a} \sim \mathcal{D}}\left\lbrack {{\log\pi}{(\left. a \middle| s \right.)}} \right\rbrack$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-B Imitation Learning (IL)", "weight": 1.0} -->

Alternatively, closed loop approaches include inverse RL (IRL) and adversarial IL (GAIL, MGAIL ), which instead aim to more directly match the occupancy measure or state-action visitation distribution between the policy and the expert, rather than indirectly through the conditional action distribution. In principle, this can resolve the covariate shift issue that affects open loop imitation.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-C Reinforcement Learning (RL)", "weight": 1.0} -->

RL aims to learn an optimal policy through an iterative, online trial and error process. In this work we use off-policy, value-based RL algorithms such as $Q$-learning.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-C Reinforcement Learning (RL)", "weight": 1.0} -->

In this work, we use an actor-critic method for training continuous control policies. Typical actor-critic methods alternate between training a critic $Q$ to minimize the Bellman error and an actor $\pi$ to maximize the value function.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-C Reinforcement Learning (RL)", "weight": 1.0} -->

and $\overline{Q}$ denotes a target network that is a copy of the critic through which gradients do not pass.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Learning to Drive with RL-Augmented BC", "weight": 1.0} -->

We wish to design an approach that benefits from the complementary strengths of IL and RL. Imitation provides an abundant source of learning signal without the need for reward design, and RL addresses the weaknesses of IL in rare and challenging scenarios where data is scarce. Following this intuition, we formulate an objective that utilizes the learning signal from demonstrations where data is abundant and the reward signal where data is scarce.

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-A Behavior Cloned Soft Actor-Critic (BC-SAC)", "weight": 1.0} -->

While in principle a variety of RL methods could be combined with IL to optimize Eq. 4, a convenient choice for efficient training is to use actor-critic algorithms, in which case the policy can be optimized with respect to Eq. 4 simply by adding the imitation learning objective to the expected value of the Q-function (i.e., the critic), similarly to DAPG or TD3+BC.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-A Behavior Cloned Soft Actor-Critic (BC-SAC)", "weight": 1.0} -->

The critic update remains the same as in SAC, outlined in Eq 1 ‣ III BACKGROUND ‣ Imitation Is Not Enough: Robustifying Imitation with Reinforcement Learning for Challenging Driving Scenarios"). With the appropriate setting of $\lambda$, this objective encourages the policy to mimic the expert data when it is within the data distribution $\mathcal{D}$. However, in out-of-distribution states the policy primarily relies on reward to learn. Fig. 2 visualizes this concept.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-B Reward Function", "weight": 1.0} -->

While designing a reward function to capture "good" driving behavior is an open-challenge, we can side-step this issue by relying on the imitation learning loss to primarily guide the policy, while the simple reward function only needs to encode safety constraints. To this end, we use a combination of collision and off-road distances as our reward signal. The collision reward is

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-B Reward Function", "weight": 1.0} -->

where $d_{\text{collision}}$ is the Euclidean distance in meters of the closest points between the ego vehicle and a nearest bounding box of other vehicles; $d_{\text{c\_offset}}$ (default 1.0) is an offset added to encourage the vehicle to keep a distance from nearby objects. The off-road reward is

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B Reward Function", "weight": 1.0} -->

where $d_{\text{to-edge}}$ is the distance in meters of the vehicle to the nearest road edge (negative being on-road, positive being off-road). $d_{\text{o\_offset}}$ (default 1.0) is an offset to encourage the vehicle to keep a distance to road edge. We combine the rewards additively, such that ${R = {R_{\text{collision}} + R_{\text{off-road}}}}.$

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-C Forward and Inverse Vehicle Dynamics Models", "weight": 1.0} -->

We update the vehicle's state using the kinematic bicycle dynamics model, which computes the vehicle's next pose $(x,y,\theta)$ given a steering and acceleration action $a = {(a_{\text{steer}},a_{\text{accel}})}$. In order to obtain expert actions for imitation learning, we use an inverse dynamics model to solve for the actions that would have achieved the same states as the logged trajectories in our dataset. These expert actions are found by minimizing the MSE of the corners' $(x,y)$ positions between the inferred state $\mathcal{T}{(s_{t},a_{t})}$ and ground-truth next state $s_{t + 1}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-D Model Architecture", "weight": 1.0} -->

We use a dual actor-critic architecture similar to TD3 and SAC: the main components are an actor network $\pi{(\left. a \middle| s \right.)}$, a double $Q$-critic network $Q{(s,a)}$ and a target double $Q$-critic network $\overline{Q}{(s,a)}$. Each network has a separate Transformer observation encoder described in that encodes features including all vehicle states, road-graph points, traffic lights signals, and route goals. The actor network outputs a $\tanh$-squashed diagonal Gaussian distribution parameterized by a mean $\mu$ and variance $\sigma$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-E Training on Difficult Examples", "weight": 1.0} -->

The performance of learning-based methods strongly depends on the training data distribution, especially in safety-critical settings with long-tail distributions ). Autonomous driving falls in this category: most scenarios are mundane, but a sizable minority of scenarios have critical safety concerns. Following, which demonstrated that training on more difficult examples results in better performance than using unbiased training distributions, we explore how the training distribution affects the method performance.

<!-- chunk {"id": "body-0025", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

Datasets. We use a dataset (denoted All) consisting of over 100k miles of expert driving trajectories, split into 10 second segments, collected from a fleet of vehicles operating in San Francisco (SF). We divide these segments into 6.4 million for training and 10k for testing. Trajectories from the same vehicle operating on the same day are stored in the same partition to avoid train-test leakage. The trajectories, which are sampled at 15 Hz, contain features describing the autonomous vehicle (AV) state and the state of the environment as measured by the AV's perception system. We use the *difficulty model* described by as a proxy for measuring the rarity of events, since it is difficult to directly construct a scenario-level out-of-distribution estimator, and challenging scenarios are generally less frequent. Given a run segment, the difficulty model predicts whether a segment will result in a collision or near-miss when re-simulated with an internal AV planner. We trained the difficulty model in a supervised manner using cross-entropy loss on a dataset consisting of 5.6k positive examples and 80k negative examples, with binary human labels.

<!-- chunk {"id": "body-0026", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

We create the Top1 and subsets by selecting the top 1% (40k train, 1.2k test), 10% (400k train, 19k test), and 50% (2 million train, 66k test) percentiles of difficulty model scores from a chronologically separate dataset of 4 million segments, respectively.

<!-- chunk {"id": "body-0027", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

Simulation. As mentioned in Sec. IV-C, vehicle dynamics are modeled using a 2D bicycle dynamics model. The behavior of other vehicles and pedestrians in the scene are replayed from the logs (log-playback), similarly to. While this means that agents are non-reactive, it ensures that the behavior of other agents is human-like, and the inclusion of imitative losses discourages the learned policy to deviate too far from the logs, which would cause the log-playback agents to become unrealistic. We also use short segments of 10s to mitigate pose divergence.

<!-- chunk {"id": "body-0028", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

Baselines. We compare our method to both open-loop (*BC* ) and closed-loop (*MGAIL* ) imitative methods. The latter takes advantage of closed loop training and the differentiability of the simulator dynamics. For completeness, we also include a SAC baseline to represent an RL-only approach.

<!-- chunk {"id": "body-0029", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

*Failure Rate*: Percentage of the run segments that have at least one *Collision* or *Off-road* event at any timestep. *Collision* is true if the bounding box of the ego vehicle intersects with a bounding box of another object. *Off-road* is true if the bounding box of the ego vehicle deviates from the drivable surface according to the map.

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

*Route Progress Ratio*: Ratio of the distance traveled along the route by the policy compared to the expert demonstration. We project the ego vehicle's state onto the route and compute the total length from the start of the route.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-B Results", "weight": 1.0} -->

We evaluate the baseline methods (BC, MGAIL, SAC) and our method (BC-SAC) trained on several subsets of the training dataset (All and Top1), and evaluate against subsets of the evaluation set (Top1 All) in Table II. All configurations are evaluated with three random seeds, reporting mean and standard deviation. Previously, showed that training MGAIL on yields similar performance with training on All. Similarly, we find that all methods perform best when trained. Notably, BC trained on Top1 performs significantly worse compared to training on All or, which reflects the fact that imitation learning methods rely on large amounts of data to implicitly infer driving preferences. In contrast, BC-SAC performs robustly when trained on Top1. Given that all methods perform best when trained, we focus on that setting in the following subsections.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-B Results", "weight": 1.0} -->

BC-SAC comparison to imitation methods (BC, MGAIL) in the challenging scenarios. Figure 4 compares BC-SAC against BC and MGAIL across the evaluation dataset slices according to difficulty levels. BC-SAC achieves better performance overall, especially in the more challenging slices where the performance of both BC and MGAIL substantially degrade. Additionally, BC-SAC has the lowest variance across scenarios of varying difficulty in performance ($\sigma = 0.37$) vs. BC ($\sigma = 1.29$) and MGAIL ($\sigma = 0.78$).

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-B Results", "weight": 1.0} -->

BC-SAC comparison to RL-only training (SAC). In all configurations, BC-SAC outperforms SAC in terms of safety metrics (Table II), likely because BC-SAC also utilizes learning signal from large amount of demonstrations. SAC generates actions that deviate significantly from the demonstrations with more boundary action values yielding unnatural (more swerves) and uncomfortable (abrupt acceleration) driving behavior (Figure 5). With a BC loss, BC-SAC generates an action distribution similar to the logs.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-B Results", "weight": 1.0} -->

Reward shaping and RL / IL weights. We conduct a set of ablation studies to answer how the form of the reward function and the weights on the RL and imitation components influence final performance. We use a smaller dataset constructed by sampling 10% of the data and compare: our full reward vs. a discrete binary reward (Fig 6 Right), off-road and collision reward term weights (Fig 6 Left), off-road and collision offset parameters (Fig 7), and the weight on the RL and IL terms in the objective (Fig 8). The results indicate that the proposed shaped reward improves overall performance over the simpler sparse reward with an appropriate choice of reward parameters, and a balance between imitation and RL terms leads to the best performance.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-B Results", "weight": 1.0} -->

Progress-safety balance. While our work focuses on safety-critical scenarios, in Fig 8 Right, we show that introducing a small amount of a progress reward leads to significantly more progress without major regressions in safety metrics. However, large progress rewards lead to degradation in performance.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-B Results", "weight": 1.0} -->

In-depth failure analysis. Table III presents a detailed analysis of failure modes on a set of 80 sampled scenarios from the Top1 and buckets. We categorize failures into 6 broad buckets. CLIP (clipping): small collisions that occur when a vehicle collides with an object on the side while moving. OFF (off-road): failures when the agent drives off the road. LAN (bad lane): an agent encroaches into another lane, either the wrong lane or a bad merge, which results in a collision. COLL (collision): collision where the planning agent is at fault and drives into another vehicle. RED (red light): red light violations that result in collisions. Finally, DIV (log divergence): collisions where a sim agent collides with the planning agent due to divergence from the logs.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-B Results", "weight": 1.0} -->

Overall, MGAIL tends to have more clipping collisions and off-road events. Fig 9 shows two of the cases where RL improves over IL. We hypothesize that our method improves in these cases because MGAIL, as an imitation method, lacks an explicit penalty for collisions, and thus is not sensitive to small collisions during otherwise realistic behavior. On the other hand, the collisions encountered by BC-SAC tend to be cases where the collision is not directly the result of the AV planner's action, but the planner diverges from the logs in a way such that it is hit by other vehicles. Because BC-SAC also is not explicitly rewarded for following traffic rules (though it inherits this behavior via imitation), we also see a small amount of failures due to that.

<!-- chunk {"id": "body-0038", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

We presented a method for robust autonomous driving in challenging driving scenarios, that combines imitation learning with RL (BC-SAC), paired with a simple safety reward, and trained on large datasets of real-world driving. Overall, the method significantly improves safety and reliability in challenging scenarios, resulting in more than 38% reduction in safety events of the most difficult scenarios compared to IL-only and RL-only baselines. Our extensive experiments examined the roles of training datasets, reward shaping and IL / RL objective terms. BC-SAC inherits implicit human-like driving behaviors from imitation, while RL is a fail-safe for handling out-of-distribution safety scenarios. Similarly to the IL-only settings, training on the top 10% of the most challenging scenarios yields the most robust performance in the combined IL and RL setting. While this work mainly focused on optimizing safety-related rewards, a natural extension is to incorporate other factors into the objective, such as progress, traffic rule adherence, and passenger comfort.

<!-- chunk {"id": "body-0039", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

Besides the reward function, this approach does not account for unexpected behavior of other agents in response to out-of-distribution actions on the part of the ego vehicle, and it still requires heuristically choosing the tradeoff between the IL and RL objectives. A promising future work direction would be to enable reactive sim agents for training and evaluation and to extend the approach to enforce safety as an explicit constraint, perhaps in combination with methodology to mitigate distributional shift.
