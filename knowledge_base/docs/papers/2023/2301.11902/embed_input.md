<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Tree-structured Policy Planning with Learned Behavior Models

Topics include Vehicles, Deep learning, Datasets, Optimization, Planning, Learning, TPP, Propose tree policy planning, Markov decision process.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Autonomous vehicles (AVs) need to reason about the multimodal behavior of neighboring agents while planning their own motion. Many existing trajectory planners seek a single trajectory that performs well under all plausible futures simultaneously, ignoring bi-directional interactions and thus leading to overly conservative plans. Policy planning, whereby the ego agent plans a policy that reacts to the environment's multimodal behavior, is a promising direction as it can account for the action-reaction interactions between the AV and the environment. However, most existing policy planners do not scale to the complexity of real autonomous vehicle applications: they are either not compatible with modern deep learning prediction models, not interpretable, or not able to generate high quality trajectories. To fill this gap, we propose Tree Policy Planning (TPP), a policy planner that is compatible with state-of-the-art deep learning prediction models, generates multistage motion plans, and accounts for the influence of ego agent on the environment behavior.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The key idea of TPP is to reduce the continuous optimization problem into a tractable discrete Markov Decision Process (MDP) through the construction of two tree structures: an ego trajectory tree for ego trajectory options, and a scenario tree for multi-modal ego-conditioned environment predictions. We demonstrate the efficacy of TPP in closed-loop simulations based on real-world nuScenes dataset and results show that TPP scales to realistic AV scenarios and significantly outperforms non-policy baselines.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A key challenge of motion planning for autonomous vehicles (AV)s is reasoning about the interaction between the ego vehicle and neighboring agents. The task is commonly divided into two subproblems: trajectory prediction for other agents, and ego motion planning with prediction. Trajectory prediction has seen substantial progress in recent years, coming from simple kineamtic models to powerful deep learning models capable of generating high-quality, multi-modal predictions. However, motion planning with such high-capacity prediction models remains a challenge.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Typical AV planners simplify the ego behavior planning problem into *trajectory planning*, where a single trajectory is sought that minimizes an expected cost over *all* predicted futures within the planning horizon. Such trajectory planning leads to overly conservative plans because it ignores the new information to be acquired about other agents in subsequent time steps, and the effects of ego actions on the behavior of other agents.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In fact, in decision-making literature, people have long been pursuing a closed-loop policy instead of an open-loop plan as the former is shown to be optimal for problems such as Markov decision processes (MDP).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To highlight the difference between a *motion policy* and a single trajectory, consider the scenario depicted on the right end of Fig. 1. The ego vehicle (blue) needs to move pass the adjacent vehicle (red). Within the planning horizon, the red vehicle either maintains its current lane or cuts in front of the ego vehicle. A traditional planner seeks a single trajectory that performs well in both situations and thus will not choose to pass since lane change is a plausible choice for the red vehicle at current time. Alternatively, a motion policy may choose to nudge forward for the first part of the horizon, observe (by leveraging a forecasting model) the behavior of the adjacent vehicle, and then decide the subsequent motion. If the red vehicle already started a lane change, the ego vehicle brakes to avoid collision; if the red vehicle stays in its own lane, since the ego vehicle is already next to the red vehicle, a sudden lane change is very unlikely, the ego vehicle can then move past the red vehicle.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the field of robotics, policy planning often takes the form of *contingency planning*, with the key idea of preparing multiple plans for different likely futures. To differentiate the two concepts, we view contingency planning as a simplified policy planning variant with only one stage of reasoning. Unfortunately, continuous-space policy planning with high-capacity prediction models is computationally prohibitive, and despite various simplifications, practical policy planning for AVs remains an open problem.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we introduce Tree Policy Planning (TPP), a practical policy planner that meets the requirements of real-world autonomous driving, specifically, TPP is designed with the following desiderata: compatible with state-of-the-art deep-learned predictive models for trajectory forecasting plans with closed-loop ego-conditioning, i.e., factors in the ego vehicle's influence on other agents allows for multistage reasoning that leverages the agents' future reactive behavior interpretable and easily tunable scales to scenarios with a large number of agents We compare existing policy planning works with TPP in Table I. To the best of our knowledge, TPP is the first algorithm that fulfils our desiderata.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The key idea of TPP is to convert the continuous space motion planning problem into a tractable finite-horizon MDP by constructing two trees: an *ego trajectory tree* carrying ego motion candidates, and a *scenario tree* that contains multiple behavior modes for neighboring agents. The algorithm is illustrated in Fig. 1. It consists of three components: an ego motion sampler that generates the ego trajectory tree, a deep-learned multi-stage prediction model that generates the scenario tree, and a dynamic program module that solves for the optimal policy with respect to the constructed MDP.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate TPP in closed-loop simulation based on a recently proposed realistic data-driven traffic model. Our results show that TPP achieves good closed-loop driving performance in real-world scenarios from the nuScenes dataset, and significantly outperforms non-policy planning baselines. The algorithm is highly parallelizable, and can run in real time.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Related works", "weight": 1.0} -->

Various contingency planning algorithms have been proposed and they can be viewed as different approximations of policy planning. A complete policy planning algorithm should be capable of multi-stage reasoning with bi-directional interactions between the agent and the environment. Since the ego is always reacting to the environment, the concept of bi-directional interaction is also referred to as ego-conditioning, emphasizing on the environment reacting to the ego agent. The application of autonomous driving also asks for high quality trajectories, accurate prediction, interpretability, and scalability. All these features combined makes it difficult to realize a non-compromising policy planning algorithm for autonomous vehicles. As a result, different simplification methods have been proposed. Limited to one stage, proposed a trajectory optimization method with one trajectory for each scene evolution mode, similar ideas are also seen in where a predefined set of modes are evaluated online. uses a deep-learned prediction model to generate the modes. performs multistage reasoning via branch MPC and leveraged ego-conditioning, yet requires a simple differentiable prediction model.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Related works", "weight": 1.0} -->

Partially Observed Markov Decision Process (POMDP) is a classic policy planning method, yet cannot generate high quality trajectories or use powerful deep-learned prediction models. Game theoretic approaches are well-known for reasoning about bi-directional interactions, yet assume some simple fixed behavior model of the environment, e.g. rational or noisy Boltzmann. performs policy planning by training a neural network to react to the environment behavior, yet gives up on multistage reasoning, and is not interpretable and hard to tune.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Related works", "weight": 1.0} -->

Table I summarizes the various existing methods and their compromises, and we would like to show in the remainder of the paper that TPP closes the gap to a practical policy planning method for AV.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Tree Policy Planning", "weight": 1.0} -->

TPP generates the ego motion policy in three steps as shown in Fig. 1. First, the ego motion sampler generates an *ego trajectory tree*, $\mathbf{r}$, given the current ego state and a lane map (when available). The ego trajectory tree consists of connected, dynamically feasible trajectory segments that together represent candidate ego-vehicle trajectories the planner can choose. Second, the prediction module is a deep learned model that generates multi-modal predictions of the environment in the form of a *scenario tree*, $\mathbf{e}$. Finally, the dynamic programming module converts $\mathbf{r}$ and $\mathbf{e}$ into an MDP and finds an optimal policy via dynamic programming.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Tree Policy Planning", "weight": 1.0} -->

We use the following notation. Let $s_{r}$ denote the state of the ego vehicle and $s_{e}$ denote the state of the environment, including the state of nearby agents and the location of static obstacles. For the trajectory tree, $r_{j}^{i}$ denotes the $j$-th node of stage $i$ and and the root node is simply $r^{0}$. The nodes in the scenario tree are labeled the same way. We enforce that all nodes of the same stage contain trajectories of the same duration with $t_{0}^{i}$ and $t_{f}^{i}$ being the starting and ending time of the $i$-th stage. The trajectory of a any node other than the root needs to follow the trajectory of its parent node.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Tree Policy Planning", "weight": 1.0} -->

Next, we discuss the three components in detail.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Ego-motion sampler", "weight": 1.0} -->

The ego motion sampler generates a set of dynamically feasible trajectory options for planning to consider, and organizes them into a trajectory tree.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Ego-motion sampler", "weight": 1.0} -->

Terminal point sampling. We first sample a set of terminal points and then find a feasible trajectory to the terminal point. Terminal points are sampled from a fixed set of acceleration-steering values, as well as along (and near to) lane centerlines when lane information is available.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Ego-motion sampler", "weight": 1.0} -->

Tree construction. In practice, trajectory trees are grown stage by stage, starting from the current state as root $r^{0}$. We set an upper bound on the number of children a node can have, and randomly drop children nodes if the limit is exceeded. In each stage we grow children branches in parallel, thus the time complexity is linear in stage number.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Multi-stage prediction model", "weight": 1.0} -->

A critical part of TPP is the prediction model that generates a scenario tree. For policy planning, we need a scene-centric, ego-conditioned, and multi-stage prediction model. We will first review these requirements and then show examples of deep-learning models satisfying our requirements.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Multi-stage prediction model", "weight": 1.0} -->

Requirements. First, the prediction model needs to predict *multiple modes* of the trajectory distribution for each agent. Second, predictions must be scene-centric, i.e., outputting modes of the joint trajectory distribution of all relevant agents in the scene. Branches of our scenario tree corresponds to modes of the joint distribution so that our planner will be able to evaluate ego trajectory candidates against joint futures effectively. Examples for multi-modal scene-scentric predictions include. Third, we need ego-conditioning (EC), i.e., prediction results should be conditioned on the ego vehicle's hypothetical future motion. Ego conditioning allows the planner to leverage the reactive behaviors of the environment towards the ego vehicle and is a known technique in prediction literature. However, training a EC prediction model remains challenging as the ground truth under counterfactual ego future motion is not known.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Multi-stage prediction model", "weight": 1.0} -->

Lastly, we need to generate modes of the predicted trajectory distribution in *multiple stages*. That is, the generated scenario tree contains multiple stages with each node branching into multiple children after each stage. Multistage prediction allows the ego agent to depend its future motion on the future multimodal observation of the environment (similar to a decision tree) and the stage number can be freely set as a design choice. Details on converting existing models to enable multistage prediction can be found in the appendix.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Multi-stage prediction model", "weight": 1.0} -->

Model architectures. To evaluate TPP's flexibility w.r.t. different prediction models, we tested it with three vastly distinct prediction models. The first model is a rasterized model with CNN backbone and a CVAE; the second model is the PredictionNet model with a Unet backbone, and the third model is the Agentformer model. All models are modified to enable multistage prediction and ego-conditioning. Details can be found in the appendix.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Dynamic programming", "weight": 1.0} -->

The dynamic programming module takes the ego trajectory tree $\mathbf{r}$ and the scenario tree $\mathbf{e}$, along with a handcrafted cost function $l$ and finds an optimal ego motion policy.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C Dynamic programming", "weight": 1.0} -->

Intuitively, our algorithm constructs a discrete MDP over $\mathbf{r}$ and $\mathbf{e}$ and finds an optimal policy through dynamic programming. More specifically, states of the MDP are nodes of the scenario/trajectory trees that represent the joint ego and environment state; transitions are given by the tree parent/children edges in the two trees; and rewards are defined by the integral of the cost over the time segment. We then solve for the optimal finite-horizon *policy* for the discrete MDP using dynamic programming, i.e., calculating the value function backwards in stage via the Bellman equation. With the optimal policy, the continuous-time trajectory is recovered from the trajectory tree by executing the trajectory segments according to the policy. In practice we use a cost function $l$ with standard terms for collision avoidance, lane keeping, goal reaching, and ride comfort; and a dynamically extended unicycle model for the vehicle dynamics.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-C Dynamic programming", "weight": 1.0} -->

Next we provide a formal discussion of the TPP algorithm.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-A Analysis without ego-conditioning", "weight": 1.0} -->

In our motion planning problem we are interested in minimizing the expected cumulative cost over a horizon: where $l$ is the running cost function that depends on the ego state $s$ and the environment state $s_{e}$, $T$ is the planning horizon. Our planning algorithm operates on the two trees $\mathbf{r}$ and $\mathbf{e}$ with the same number of stages, so the cumulative cost can be rewritten as where $r^{i}$ and $e^{i}$ are the nodes the ego vehicle and the environment take at stage $i$, and ${L_{i}{(r^{i},e^{i})}} = {\int_{t_{0}^{i}}^{t_{f}^{i}}{l{({s^{r^{i}}{(t)}},{s_{e}^{e^{i}}{(t)}})}{dt}}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A Analysis without ego-conditioning", "weight": 1.0} -->

Due to the stochasticity of the environment, we aim to minimize ${\mathbb{E}}_{e^{0:N}}{\lbrack{\sum_{i = 0}^{N}{L_{i}{(r^{i},e^{i})}}}\rbrack}$, where the expectation is on $e^{i}$, the actual branch the environment takes and the distribution is given as part of the prediction. For simplicity, we shall present the result assuming $\mathbf{e}$ is not ego-conditioned, i.e., there is a single $\mathbf{e}$, and later show that the result can be easily extended to the case with ego-conditioning.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A Analysis without ego-conditioning", "weight": 1.0} -->

The end result is a policy that chooses which node to execute for the next stage given the current ego and environment node, i.e., $r^{i + 1} = {\pi^{\star}{(r^{i},e^{i})}}$, where $\pi^{\star}$ is the optimal policy. The form of the policy is determined by the assumption about the information flow, i.e., during stage $i$, the ego vehicle can observe the environment's response $e^{i}$, and choose the ego motion among the children nodes of the current node $r^{i}$. To obtain the optimal policy, a value function is needed: which is the expected cost-to-go. The dynamic program goes backwards in stage and is trivial for the last stage: For stage i where $i < N$, we have Since $e^{i + 1}$ is enumerable, the expectation is calculated as where the branching probability of the scenario tree is given by the prediction model.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Analysis without ego-conditioning", "weight": 1.0} -->

Further define where $r^{i} = {\text{Par}{(r^{i + 1})}}$. We name this function $Q$ function as it is analogous to the $Q$ function in reinforcement learning where here $b^{k + 1}$ is the action we need to choose.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A Analysis without ego-conditioning", "weight": 1.0} -->

The value function is then obtained backwards in stage: The optimal policy is then

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-B Extension to ego-conditioned prediction", "weight": 1.0} -->

In the case where the scenario tree is ego-conditioned, the algorithm structure stays roughly the same. To generate the ego-conditioned trajectory prediction, we first run the ego motion sampler to generate the trajectory tree, then the trajectory tree is "flattened " to create the ego-conditioning (EC) modes. E.g., for trees in Fig. 1, the flattened EC modes are shown in Fig. 2.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 1", "weight": 1.0} -->

For stochastic prediction models, the generated scenario trees are causally consistent if the random seeds are shared among all EC modes with the same EC trajectory.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The proof is omitted here. It is straightforward to show that the 3 prediction models in Section III-B are CC.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Given causally consistent EC predictions, only two terms change in the policy planning algorithm. First, all nodes of the scenario tree now depend on one of the nodes of trajectory tree of the same stage, and are denoted as $e^{i}{(r^{i})}$ to emphasize the dependence. Note that the dependence is on $r^{i}$ instead of the whole ego trajectory due to causal consistency. Second, the branching probability now depends on the ego node, and is denoted as ${\mathbb{P}}{\lbrack\left. e_{j}^{i + 1} \middle| {{e^{i}{(r^{i})}},r^{i}} \right.\rbrack}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Formally, we are solving a finite-horizon MDP with a joint state of $(r^{i},e^{i})$ and the cost defined. The action space is ${A{(r^{i})}} = {\text{Ch}r^{i}}$, the next ego maneuver, and the transition probability is Interestingly, the value function can be defined exactly the same way as Similarly, the Q function is now where $\text{Ch}{({e^{i}{(r^{i})}},r^{i + 1})}$ denotes the set of children nodes following $e^{i}{(r^{i})}$ on the tree associated with $r^{i + 1}$. The optimal policy is then defined as

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-A Training of prediction model", "weight": 1.0} -->

We configure TPP with three different prediction models. Apart from the model architecture, the experimental setup is the same. Prediction models are trained with the nuScenes dataset, comprised of 1000 scenes lasting for 20 seconds collected in urban areas of Boston and Singapore. For simplicity, only vehicles are considered. All prediction models use 2 stages and the branching factor is 4.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-A Training of prediction model", "weight": 1.0} -->

Loss function. Our training loss is a weighted sum of the following terms: prediction loss that penalizes the error between the predicted trajectories and the ground truth; EC collision loss that penalizes collisions between the predicted trajectories and the conditioned ego trajectory; collision loss that penalizes collisions between predicted trajectories of different agents in the scene; and additional standard regularization losses specific to the model architecture.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-A Training of prediction model", "weight": 1.0} -->

Ego conditioning. One natural choice of the ego trajectory for ego-conditioning is the ground truth future trajectory. In addition, to expose the model to more diverse ego trajectories, we perturb the ground truth ego trajectory with noise generated via the Ornstein--Uhlenbeck process as alternative ego trajectories. However, since the ground truth for surrounding agents under the counterfactual ego motion is not available, for the lack of a better choice, we still use the original ground truth as the target for the EC trajectory prediction. We penalize collision between the predicted trajectories of surrounding agents and the conditioned ego trajectory so that the model learns to avoid the conditioned ego trajectory.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-A Training of prediction model", "weight": 1.0} -->

Training results. We report standard ADE/FDE prediction metrics for the three prediction models in Table II. The results show that all three models learn reasonable predictions.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-B Experimental setup", "weight": 1.0} -->

Closed-loop simulation. We evaluate TPP in BITS, a closed-loop AV simulation environment proposed. Each simulation scene is initialized with a scene from the nuScenes dataset and then evolves forward with a policy for each agent. One agent is chosen as the ego vehicle and controlled by TPP or its alternatives. All other agents runs the learned BITS policy that generates realistic and diverse behavior of road vehicles. Additionally, to incite more interactions between agents, we "spawn" new agents around the ego vehicle to challenge the planner throughout the simulation duration.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-B Experimental setup", "weight": 1.0} -->

Metrics. We use three key metrics: collision rate, offroad rate, and area coverage. The first two are calculated as the percentage of time steps where the ego vehicle is in collision (offroad). The coverage metric is calculated with a kernel density estimation (KDE) procedure following, and it captures the effectiveness of the ego plan in terms of liveness and distance travelled. The evaluation is done on 100 scenes from the evaluation split of nuScenes (not used for training).

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-B Experimental setup", "weight": 1.0} -->

Baselines. We consider three baselines, the first two are non-contingent counterpart of TPP. For fair comparison, the two baselines share the same ego-motion sampler and ego-conditioning prediction model as TPP, the first baseline, named non-contingency robust (NCR), considers all possible trajectories predicted by the prediction model (similar to ); while the second baseline, named non-policy greedy (NCG), only avoids the most likely prediction mode (similar to ). The third baseline uses a kinematic prediction model with 2 modes: maintaining speed and braking, and share the same multi-stage tree structure.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-C Results", "weight": 1.0} -->

Fig. 3 shows snapshots of the simulation with TPP where the ego vehicle (blue) cuts in front of the red vehicle and then change lane again to avoid the parked green vehicle. The magenta lines show the ego trajectory tree, and the colorful line shows the rollout trajectories of the agents. The quantitative results are shown in Tables III and IV, and we make the following observations. Simulation videos can be found here.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-C Results", "weight": 1.0} -->

TPP outperforms the baselines. As shown in Table III, TPP significantly outperforms the two non-policy baselines on crash and offroad rate under all 3 prediction models while achieving similar coverage. Even under a simple kinematic model, the performance is better than non-policy planners with sophisticated prediction models. TPP with deep-learned prediction models performs better than with a simple kinematic model, indicating the deep-learned prediction model benefits the closed-loop performance.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-C Results", "weight": 1.0} -->

Better predictions do not mean better plan. Interestingly, from Table III, the "better" prediction model measured by ADE/FDE does not necessarily lead to better closed-loop performance. For example, the rasterized model is the simplest and "worst" model among the three, yet TPP with it outperforms the other two in terms of crash rate.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-C Results", "weight": 1.0} -->

Ego-conditioning is useful. Table IV compares TPP with or without ego-conditioning. Ego-conditioning improves the closed-loop performance considerably in most cases, especially the coverage metric, hinting that the ego vehicle is more comfortable moving through traffic when it expects reaction from other agents.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-C Results", "weight": 1.0} -->

Temporal consistency is important. Additionally, we tested the Agentformer model with Gaussian latent space, where the prediction requires sampling of the latent variable at every inference call, compared to using discrete latent space where sampling is not needed. While the prediction ADE/FDE is similar, the closed-loop performance with the Gaussian latent is significantly worse. We suspect this is due to the poor temporal consistency between predictions of consecutive time steps. While both TPP and the two baselines saw performance degradation under the Gaussian latent, the policy planner relies on more sophisticated prediction/planning interaction, thus suffers more than the two baselines.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We present TPP, a policy planner capable of generating multistage motion policies that react to the environment. It is centered around an ego trajectory tree and a scenario tree that predicts the environment behavior, both containing multiple stages. Ego-conditioning is applied to leverage the reactive behavior of the environment under the ego vehicle's presence. The closed-loop simulation result shows that TPP significantly outperform two non-policy benchmarks and the runtime test suggest that such sophisticated policy planner can be run in real time. Our planned future works include study more flexible topology of the trees and enable event-triggered branching improve the efficiency of computation, especially under ego-conditioning adaptive and personalized policy planning.
