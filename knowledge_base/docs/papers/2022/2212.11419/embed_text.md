## INTRODUCTION

Building an autonomous driving system that is deployable at scale presents many difficulties. First and foremost is the challenge of handling the numerous rare and challenging edge cases that occur in real-world driving. To this end, imitative learning based approaches have been proposed that allow the performance of the method to scale with the amount of data available. While situations that are well represented in the demonstration data are likely to be handled correctly by such a policy, more unusual or dangerous situations that occur only rarely in the data might cause the imitation policy -- which has not been explicitly instructed on what constitutes a risky or inappropriate response -- to respond unpredictably. The problem is compounded by complex interactions, where human expert driving data in similar scenarios may be scarce and sub-optimal.

Reinforcement Learning (RL) has the potential to resolve this by leveraging explicit reward functions that tell the policy what constitutes safe or unsafe outcomes (e.g., collisions). Furthermore, because RL methods train in closed-loop, RL policies can establish causal relationships between observations, actions, and outcomes. This yields policies that are less vulnerable to covariate shifts and spurious correlations commonly seen in open loop IL, and aware of safety considerations encoded in their reward function, but which are only implicit in the demonstrations.

However, relying on RL alone, e.g. is also problematic because it heavily depends on reward design, which is an open challenge in autonomous driving. Without accounting for imitation fidelity, driving policies trained with RL may be technically safe but unnatural, and may have a hard time making forward progress in situations that demand human-like driving behavior to coordinate with other agents and follow driving conventions. IL and RL offer complementary strengths: IL increases realism and eases the reward design burden and RL improves safety and robustness, especially in rare and challenging scenarios in the absence of abundant data (Fig. 1).

Figure 1: The demonstration-reward trade-off. As the amount of data for a particular scenario decreases, reward signals become more important for learning. We show a few visual examples representing scenarios with different frequencies.

In this paper we focus on the driving scenarios that are most likely to exhibit safety and reliability concerns, leveraging the difficulty estimation from. Our proposed method, BC-SAC, combines IL and RL with a *simple* reward function, and trains on difficult driving scenarios. Difficulty is estimated via a classifier that estimates the likelihood of a collision or near-miss when re-simulated with a pre-trained planning policy. Our proposed reward function enforces safety of the agent, while natural driving behaviors are implicitly learned with IL. The training data comes from a subset of real-world human driving data (over 100k miles of real-world urban driving data). We demonstrate that this approach substantially improves the safety and reliability of policies learned over imitation alone without compromising on human-like behavior, showing 38% and 40% improvements over pure IL and RL baselines.

The main contributions of our work are: We conduct the first large-scale application of a combined IL and RL approach in autonomous driving utilizing large amounts of real-world urban human driving data (over 100k miles) and a *simple* reward function. We systematically evaluate its performance and baseline performance by slicing the dataset by difficulty, demonstrating that combining IL and RL improves safety and reliability of policies over those learned from imitation alone (over 38% reduction in safety events on the most difficult bucket).

Multipath, Precog, Trajectron++

Adversarial Imitation/IRL
IRL, GAIL, MGAIL

DQfD, DAPG, BC-SAC (ours)

TABLE I: A comparison of different learning-based approaches to robotic control and autonomous driving.

## RELATED WORK

Learning-based approaches in autonomous driving. We briefly summarize key properties of different learning-based algorithms for planning in Table I. IL was among the earliest and most popular learning-based approaches adopted for deriving driving policies. Controllable models trained with either IL or RL allow the user to specify high-level commands in the form of goals or control signals (e.g., left, right, straight) to combine higher-level route planning with low-level control.

Two drawbacks of IL methods are: open-loop IL (such as the widely used behavioral cloning approach ) suffers from covariate shift (which can be addressed with closed-loop training ), IL methods lack *explicit* knowledge of what constitutes good driving, such as collision avoidance. RL methods have been proposed that allow the policy to learn from explicit reward signals with closed-loop training and have been applied to tasks such as lane-keeping, intersection traversal, and lane changing. While these works show the efficacy of RL on specific scenarios, our work analyzes both the large-scale, aggregate performance *and* challenging and safety-critical edge cases that make autonomous driving difficult to deploy in a real-world system.

RL and other closed-loop methods for autonomous driving typically use simulation for training. There are a number of such public environments, which vary in how realistic they are, in particular what drives the simulated agents (e.g., expert-following/log playback, intelligent driving model (IDM), or other rule based systems and ML-based agents ), and whether scenarios are procedurally generated (e.g., ) or initialized from real-world driving scenes. In our experiments, we develop and evaluate in closed-loop on real-world data with other agents following logs.

Combining IL and RL. Methods such as DQfD, DDPGfD, and DAPG have shown that IL can help RL overcome exploration challenges in domains with known sparse rewards. Offline RL approaches, such as TD3+BC and CQL combine RL objectives with IL ones to regularize $Q$-learning updates and avoid overestimating out-of-distribution values. Our goal is not to propose a novel algorithmic combination of IL and RL, but rather to leverage this general approach to address challenges in autonomous driving at scale.

Addressing challenging and safety-critical scenarios for autonomous vehicles. learns policies that address long-tail scenarios in autonomous driving by using an ensemble of IL planners combined with model-predictive control. Another approach to improving safety is to augment a learned planner with a rule-based fallback layer that guarantees safety. Our work differs from these approaches, in that we directly incorporate safety awareness into the model learning process through a reward. Our method is also compatible with a fallback layer if needed, although we this is potential future work. Another way to improve robustness of polices is to increase the frequency of negative examples during training. collects failure data that covers various ways an unmanned aerial vehicle can crash, and the combined negative and positive data helps to train more robust policies. investigates the use of curriculum training to improve performance on challenging edge cases. While we also increase the exposure of the policy to challenging scenarios during training, we extend these findings by showing how RL yields outsized improvements on the hardest scenarios.

## BACKGROUND

### III-A Markov Decision Processes (MDPs)

In this work, we cast the autonomous driving policies learning problem as a Markov decision process. Following standard formalism, we define an MDP as a tuple $\{\mathcal{S},\mathcal{A},\mathcal{T},\mathcal{R},\gamma,\rho_{0}\}$. $\mathcal{S}$ and $\mathcal{A}$ denote the state and action spaces, respectively. $\mathcal{T}$ denotes to transition model. $\mathcal{R}$ represents the reward function, and $\gamma$ represents the discount factor. $\rho_{0}$ represents the initial state distribution. The objective is to find a policy $\pi$, a (stochastic) mapping from $\mathcal{S}$ to $\mathcal{A}$, that maximizes the expected discounted sum of rewards, ${\pi^{\ast} = {{\max_{\pi}{\mathbb{E}}_{\mathcal{T},\pi,\rho_{0}}}\left\lbrack {\sum_{t = 0}^{\infty}{\gamma^{t}R{(s_{t},a_{t})}}} \right\rbrack}}.$

### III-B Imitation Learning (IL)

IL constructs an optimal policy by mimicking an expert. We assume an expert (an optimal policy), denoted as $\pi_{\beta}$, produces a dataset of trajectories $\mathcal{D} = {\{ s_{0},a_{0},\cdots,s_{N},a_{N}\}}$ through interaction with the environment. The learner's goal is to train a policy $\pi$ that imitates the $\pi_{\beta}$. In practice, we only observe the expert states, so we estimate expert actions using inverse dynamics. For example, behavioral cloning (BC) trains the policy via a log-likelihood objective, ${\mathbb{E}}_{{s,a} \sim \mathcal{D}}\left\lbrack {{\log\pi}{(\left. a \middle| s \right.)}} \right\rbrack$. Alternatively, closed loop approaches include inverse RL (IRL) and adversarial IL (GAIL, MGAIL ), which instead aim to more directly match the occupancy measure or state-action visitation distribution between the policy and the expert, rather than indirectly through the conditional action distribution. In principle, this can resolve the covariate shift issue that affects open loop imitation.

### III-C Reinforcement Learning (RL)

RL aims to learn an optimal policy through an iterative, online trial and error process. In this work we use off-policy, value-based RL algorithms such as $Q$-learning. These methods aim to learn the state-action value function, defined as the expected future return when starting from a particular state and action:

In this work, we use an actor-critic method for training continuous control policies. Typical actor-critic methods alternate between training a critic $Q$ to minimize the Bellman error and an actor $\pi$ to maximize the value function. We use the entropy-regularized updates of Soft Actor-Critic (SAC):

and $\overline{Q}$ denotes a target network that is a copy of the critic through which gradients do not pass.

## Learning to Drive with RL-Augmented BC

We wish to design an approach that benefits from the complementary strengths of IL and RL. Imitation provides an abundant source of learning signal without the need for reward design, and RL addresses the weaknesses of IL in rare and challenging scenarios where data is scarce. Following this intuition, we formulate an objective that utilizes the learning signal from demonstrations where data is abundant and the reward signal where data is scarce. Specifically, we utilize a weighted mixture of the IL and RL objectives:

### IV-A Behavior Cloned Soft Actor-Critic (BC-SAC)

While in principle a variety of RL methods could be combined with IL to optimize Eq. 4, a convenient choice for efficient training is to use actor-critic algorithms, in which case the policy can be optimized with respect to Eq. 4 simply by adding the imitation learning objective to the expected value of the Q-function (i.e., the critic), similarly to DAPG or TD3+BC. Building on the widely used SAC framework, which further adds an entropy regularization objective to the actor, we obtain our full actor objective:

The critic update remains the same as in SAC, outlined in Eq 1 ‣ III BACKGROUND ‣ Imitation Is Not Enough: Robustifying Imitation with Reinforcement Learning for Challenging Driving Scenarios"). With the appropriate setting of $\lambda$, this objective encourages the policy to mimic the expert data when it is within the data distribution $\mathcal{D}$. However, in out-of-distribution states the policy primarily relies on reward to learn. Fig. 2 visualizes this concept.

### IV-B Reward Function

While designing a reward function to capture "good" driving behavior is an open-challenge, we can side-step this issue by relying on the imitation learning loss to primarily guide the policy, while the simple reward function only needs to encode safety constraints. To this end, we use a combination of collision and off-road distances as our reward signal. The collision reward is

where $d_{\text{collision}}$ is the Euclidean distance in meters of the closest points between the ego vehicle and a nearest bounding box of other vehicles; $d_{\text{c\_offset}}$ (default 1.0) is an offset added to encourage the vehicle to keep a distance from nearby objects. The off-road reward is

where $d_{\text{to-edge}}$ is the distance in meters of the vehicle to the nearest road edge (negative being on-road, positive being off-road). $d_{\text{o\_offset}}$ (default 1.0) is an offset to encourage the vehicle to keep a distance to road edge. We combine the rewards additively, such that ${R = {R_{\text{collision}} + R_{\text{off-road}}}}.$

### IV-C Forward and Inverse Vehicle Dynamics Models

We update the vehicle's state using the kinematic bicycle dynamics model, which computes the vehicle's next pose $(x,y,\theta)$ given a steering and acceleration action $a = {(a_{\text{steer}},a_{\text{accel}})}$. In order to obtain expert actions for imitation learning, we use an inverse dynamics model to solve for the actions that would have achieved the same states as the logged trajectories in our dataset. These expert actions are found by minimizing the MSE of the corners' $(x,y)$ positions between the inferred state $\mathcal{T}{(s_{t},a_{t})}$ and ground-truth next state $s_{t + 1}$.

Figure 2: Different objective influence. For in-distribution states, both IL and RL objectives provide learning signal. For out-of-distribution states, the RL objective dominates.

### IV-D Model Architecture

We use a dual actor-critic architecture similar to TD3 and SAC: the main components are an actor network $\pi{(\left. a \middle| s \right.)}$, a double $Q$-critic network $Q{(s,a)}$ and a target double $Q$-critic network $\overline{Q}{(s,a)}$. Each network has a separate Transformer observation encoder described in that encodes features including all vehicle states, road-graph points, traffic lights signals, and route goals. The actor network outputs a $\tanh$-squashed diagonal Gaussian distribution parameterized by a mean $\mu$ and variance $\sigma$.

### IV-E Training on Difficult Examples

The performance of learning-based methods strongly depends on the training data distribution, especially in safety-critical settings with long-tail distributions ). Autonomous driving falls in this category: most scenarios are mundane, but a sizable minority of scenarios have critical safety concerns. Following, which demonstrated that training on more difficult examples results in better performance than using unbiased training distributions, we explore how the training distribution affects the method performance.

## EXPERIMENTS

### V-A Experimental Setup

Datasets. We use a dataset (denoted All) consisting of over 100k miles of expert driving trajectories, split into 10 second segments, collected from a fleet of vehicles operating in San Francisco (SF). We divide these segments into 6.4 million for training and 10k for testing. Trajectories from the same vehicle operating on the same day are stored in the same partition to avoid train-test leakage. The trajectories, which are sampled at 15 Hz, contain features describing the autonomous vehicle (AV) state and the state of the environment as measured by the AV's perception system. We use the *difficulty model* described by as a proxy for measuring the rarity of events, since it is difficult to directly construct a scenario-level out-of-distribution estimator, and challenging scenarios are generally less frequent. Given a run segment, the difficulty model predicts whether a segment will result in a collision or near-miss when re-simulated with an internal AV planner. We trained the difficulty model in a supervised manner using cross-entropy loss on a dataset consisting of 5.6k positive examples and 80k negative examples, with binary human labels. We create the Top1 and subsets by selecting the top 1% (40k train, 1.2k test), 10% (400k train, 19k test), and 50% (2 million train, 66k test) percentiles of difficulty model scores from a chronologically separate dataset of 4 million segments, respectively.

Simulation. As mentioned in Sec. IV-C, vehicle dynamics are modeled using a 2D bicycle dynamics model. The behavior of other vehicles and pedestrians in the scene are replayed from the logs (log-playback), similarly to. While this means that agents are non-reactive, it ensures that the behavior of other agents is human-like, and the inclusion of imitative losses discourages the learned policy to deviate too far from the logs, which would cause the log-playback agents to become unrealistic. We also use short segments of 10s to mitigate pose divergence.

Baselines. We compare our method to both open-loop (*BC* ) and closed-loop (*MGAIL* ) imitative methods. The latter takes advantage of closed loop training and the differentiability of the simulator dynamics. For completeness, we also include a SAC baseline to represent an RL-only approach.

Metrics. We evaluate agents using two metrics:

*Failure Rate*: Percentage of the run segments that have at least one *Collision* or *Off-road* event at any timestep. *Collision* is true if the bounding box of the ego vehicle intersects with a bounding box of another object. *Off-road* is true if the bounding box of the ego vehicle deviates from the drivable surface according to the map.

*Route Progress Ratio*: Ratio of the distance traveled along the route by the policy compared to the expert demonstration. We project the ego vehicle's state onto the route and compute the total length from the start of the route.

Figure 3: Failure rates on the most challenging evaluation sets: Top1 and (lower is better, with training on All and ). BC-SAC consistently achieves the lowest error rates.

Figure 4: Failure rates of BC, MGAIL, and BC-SAC across scenarios of varying difficulty levels (50%-100%, lower is better). While all methods perform worse as the evaluation dataset becomes more challenging, BC-SAC always performs best and shows the least degradation.

TABLE II: Failure rates (lower is better) and progress ratios (higher is better)
of BC-SAC and baselines on different training/evaluation subsets.

Figure 5: Marginal action distributions. SAC/BC-SAC (orange) vs logs (blue).

### V-B Results

We evaluate the baseline methods (BC, MGAIL, SAC) and our method (BC-SAC) trained on several subsets of the training dataset (All and Top1), and evaluate against subsets of the evaluation set (Top1 All) in Table II. All configurations are evaluated with three random seeds, reporting mean and standard deviation. Previously, showed that training MGAIL on yields similar performance with training on All. Similarly, we find that all methods perform best when trained on. Notably, BC trained on Top1 performs significantly worse compared to training on All or, which reflects the fact that imitation learning methods rely on large amounts of data to implicitly infer driving preferences. In contrast, BC-SAC performs robustly when trained on Top1. Given that all methods perform best when trained on, we focus on that setting in the following subsections.

BC-SAC comparison to imitation methods (BC, MGAIL) in the challenging scenarios. Figure 4 compares BC-SAC against BC and MGAIL across the evaluation dataset slices according to difficulty levels. BC-SAC achieves better performance overall, especially in the more challenging slices where the performance of both BC and MGAIL substantially degrade. Additionally, BC-SAC has the lowest variance across scenarios of varying difficulty in performance ($\sigma = 0.37$) vs. BC ($\sigma = 1.29$) and MGAIL ($\sigma = 0.78$).

BC-SAC comparison to RL-only training (SAC). In all configurations, BC-SAC outperforms SAC in terms of safety metrics (Table II), likely because BC-SAC also utilizes learning signal from large amount of demonstrations. SAC generates actions that deviate significantly from the demonstrations with more boundary action values yielding unnatural (more swerves) and uncomfortable (abrupt acceleration) driving behavior (Figure 5). With a BC loss, BC-SAC generates an action distribution similar to the logs.

Reward shaping and RL / IL weights. We conduct a set of ablation studies to answer how the form of the reward function and the weights on the RL and imitation components influence final performance. We use a smaller dataset constructed by sampling 10% of the data and compare: our full reward vs. a discrete binary reward (Fig 6 Right), off-road and collision reward term weights (Fig 6 Left), off-road and collision offset parameters (Fig 7), and the weight on the RL and IL terms in the objective (Fig 8). The results indicate that the proposed shaped reward improves overall performance over the simpler sparse reward with an appropriate choice of reward parameters, and a balance between imitation and RL terms leads to the best performance.

Progress-safety balance. While our work focuses on safety-critical scenarios, in Fig 8 Right, we show that introducing a small amount of a progress reward leads to significantly more progress without major regressions in safety metrics. However, large progress rewards lead to degradation in performance.

Figure 6: Left: Off-road / collision weights. Off-road weight and collision weight add up to 2.0. The x-axis is the collision weight. A balanced choice of off-road and collision weights lead to the best performance. Right: Dense vs binary rewards. Binary reward is defined as − 1 when a safety event happens and 0 otherwise. Dense rewards lead to fewer safety events.

Figure 7: Off-road offset do_offset and collision offset dc_offset ablations. A small amount of offsets improves overall performance.

Figure 8: Left Imitation weights (log-scale) vs failure rates. Right Progress reward weights (log-scale) vs policy evaluation performance: safety event rate and route progress ratio.

Figure 9: Visualizations of a few scenarios where BC-SAC improves over imitation (MGAIL) and RL-only (SAC). The cyan car is controlled. Example 1: MGAIL collides with a pedestrian exiting a double parked car while BC-SAC leaves enough clearance. Example 2: MGAIL does not provide sufficient clearance and collides with the incoming vehicle. Example 3: SAC slows down in an intersection resulting in an rear collision. BC-SAC maintains a proper speed profile through the intersection without a collision.

TABLE III: Failure frequency categorizations, per type, incurred by BC-SAC and MGAIL on a small sample set (N=80). BC-SAC generally has fewer direct collisions and off-road events, but has a greater frequency of being hit by other objects.

In-depth failure analysis. Table III presents a detailed analysis of failure modes on a set of 80 sampled scenarios from the Top1 and buckets. We categorize failures into 6 broad buckets. CLIP (clipping): small collisions that occur when a vehicle collides with an object on the side while moving. OFF (off-road): failures when the agent drives off the road. LAN (bad lane): an agent encroaches into another lane, either the wrong lane or a bad merge, which results in a collision. COLL (collision): collision where the planning agent is at fault and drives into another vehicle. RED (red light): red light violations that result in collisions. Finally, DIV (log divergence): collisions where a sim agent collides with the planning agent due to divergence from the logs.

Overall, MGAIL tends to have more clipping collisions and off-road events. Fig 9 shows two of the cases where RL improves over IL. We hypothesize that our method improves in these cases because MGAIL, as an imitation method, lacks an explicit penalty for collisions, and thus is not sensitive to small collisions during otherwise realistic behavior. On the other hand, the collisions encountered by BC-SAC tend to be cases where the collision is not directly the result of the AV planner's action, but the planner diverges from the logs in a way such that it is hit by other vehicles. Because BC-SAC also is not explicitly rewarded for following traffic rules (though it inherits this behavior via imitation), we also see a small amount of failures due to that.

## CONCLUSIONS

We presented a method for robust autonomous driving in challenging driving scenarios, that combines imitation learning with RL (BC-SAC), paired with a simple safety reward, and trained on large datasets of real-world driving. Overall, the method significantly improves safety and reliability in challenging scenarios, resulting in more than 38% reduction in safety events of the most difficult scenarios compared to IL-only and RL-only baselines. Our extensive experiments examined the roles of training datasets, reward shaping and IL / RL objective terms. BC-SAC inherits implicit human-like driving behaviors from imitation, while RL is a fail-safe for handling out-of-distribution safety scenarios. Similarly to the IL-only settings, training on the top 10% of the most challenging scenarios yields the most robust performance in the combined IL and RL setting. While this work mainly focused on optimizing safety-related rewards, a natural extension is to incorporate other factors into the objective, such as progress, traffic rule adherence, and passenger comfort. Besides the reward function, this approach does not account for unexpected behavior of other agents in response to out-of-distribution actions on the part of the ego vehicle, and it still requires heuristically choosing the tradeoff between the IL and RL objectives. A promising future work direction would be to enable reactive sim agents for training and evaluation and to extend the approach to enforce safety as an explicit constraint, perhaps in combination with methodology to mitigate distributional shift.
