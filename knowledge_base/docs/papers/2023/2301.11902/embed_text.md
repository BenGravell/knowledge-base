<!-- arxiv-full-text:v1 {"arxiv_id": "2301.11902", "source": "ar5iv"} -->

## Introduction

A key challenge of motion planning for autonomous vehicles (AV)s is reasoning about the interaction between the ego vehicle and neighboring agents. The task is commonly divided into two subproblems: trajectory prediction for other agents, and ego motion planning with prediction. Trajectory prediction has seen substantial progress in recent years, coming from simple kineamtic models to powerful deep learning models capable of generating high-quality, multi-modal predictions. However, motion planning with such high-capacity prediction models remains a challenge.

Typical AV planners simplify the ego behavior planning problem into *trajectory planning*, where a single trajectory is sought that minimizes an expected cost over *all* predicted futures within the planning horizon. Such trajectory planning leads to overly conservative plans because it ignores the new information to be acquired about other agents in subsequent time steps, and the effects of ego actions on the behavior of other agents.

In fact, in decision-making literature, people have long been pursuing a closed-loop policy instead of an open-loop plan as the former is shown to be optimal for problems such as Markov decision processes (MDP).

TABLE I: Comparison of existing policy planning methods and TPP where “DL” is short for compatibility with deep-learned prediction models, “EC” stands for ego-conditioning, “Interp” is short for interpretable, “MS” stands for multistage, and “Scalability” means the capability to scale to complicated scenes with large number of agents.

Figure 1: Structure of TPP: the ego motion sampler generates the trajectory tree, which is fed to the prediction model for ego-conditioned prediction to generate the scenario tree. Then we solve for the ego motion policy via dynamic programming.

To highlight the difference between a *motion policy* and a single trajectory, consider the scenario depicted on the right end of Fig. 1. The ego vehicle (blue) needs to move pass the adjacent vehicle (red). Within the planning horizon, the red vehicle either maintains its current lane or cuts in front of the ego vehicle. A traditional planner seeks a single trajectory that performs well in both situations and thus will not choose to pass since lane change is a plausible choice for the red vehicle at current time. Alternatively, a motion policy may choose to nudge forward for the first part of the horizon, observe (by leveraging a forecasting model) the behavior of the adjacent vehicle, and then decide the subsequent motion. If the red vehicle already started a lane change, the ego vehicle brakes to avoid collision; if the red vehicle stays in its own lane, since the ego vehicle is already next to the red vehicle, a sudden lane change is very unlikely, the ego vehicle can then move past the red vehicle.

In the field of robotics, policy planning often takes the form of *contingency planning*, with the key idea of preparing multiple plans for different likely futures. To differentiate the two concepts, we view contingency planning as a simplified policy planning variant with only one stage of reasoning. Unfortunately, continuous-space policy planning with high-capacity prediction models is computationally prohibitive, and despite various simplifications, practical policy planning for AVs remains an open problem.

In this paper we introduce Tree Policy Planning (TPP), a practical policy planner that meets the requirements of real-world autonomous driving, specifically, TPP is designed with the following desiderata: compatible with state-of-the-art deep-learned predictive models for trajectory forecasting plans with closed-loop ego-conditioning, i.e., factors in the ego vehicle's influence on other agents allows for multistage reasoning that leverages the agents' future reactive behavior interpretable and easily tunable scales to scenarios with a large number of agents We compare existing policy planning works with TPP in Table I. To the best of our knowledge, TPP is the first algorithm that fulfils our desiderata.

The key idea of TPP is to convert the continuous space motion planning problem into a tractable finite-horizon MDP by constructing two trees: an *ego trajectory tree* carrying ego motion candidates, and a *scenario tree* that contains multiple behavior modes for neighboring agents. The algorithm is illustrated in Fig. 1. It consists of three components: an ego motion sampler that generates the ego trajectory tree, a deep-learned multi-stage prediction model that generates the scenario tree, and a dynamic program module that solves for the optimal policy with respect to the constructed MDP.

We evaluate TPP in closed-loop simulation based on a recently proposed realistic data-driven traffic model. Our results show that TPP achieves good closed-loop driving performance in real-world scenarios from the nuScenes dataset, and significantly outperforms non-policy planning baselines. The algorithm is highly parallelizable, and can run in real time.

## Related works

Various contingency planning algorithms have been proposed and they can be viewed as different approximations of policy planning. A complete policy planning algorithm should be capable of multi-stage reasoning with bi-directional interactions between the agent and the environment. Since the ego is always reacting to the environment, the concept of bi-directional interaction is also referred to as ego-conditioning, emphasizing on the environment reacting to the ego agent. The application of autonomous driving also asks for high quality trajectories, accurate prediction, interpretability, and scalability. All these features combined makes it difficult to realize a non-compromising policy planning algorithm for autonomous vehicles. As a result, different simplification methods have been proposed. Limited to one stage, proposed a trajectory optimization method with one trajectory for each scene evolution mode, similar ideas are also seen in where a predefined set of modes are evaluated online. uses a deep-learned prediction model to generate the modes. performs multistage reasoning via branch MPC and leveraged ego-conditioning, yet requires a simple differentiable prediction model.

Partially Observed Markov Decision Process (POMDP) is a classic policy planning method, yet cannot generate high quality trajectories or use powerful deep-learned prediction models. Game theoretic approaches are well-known for reasoning about bi-directional interactions, yet assume some simple fixed behavior model of the environment, e.g. rational or noisy Boltzmann. performs policy planning by training a neural network to react to the environment behavior, yet gives up on multistage reasoning, and is not interpretable and hard to tune.

Table I summarizes the various existing methods and their compromises, and we would like to show in the remainder of the paper that TPP closes the gap to a practical policy planning method for AV.

## Tree Policy Planning

TPP generates the ego motion policy in three steps as shown in Fig. 1. First, the ego motion sampler generates an *ego trajectory tree*, $\mathbf{r}$, given the current ego state and a lane map (when available). The ego trajectory tree consists of connected, dynamically feasible trajectory segments that together represent candidate ego-vehicle trajectories the planner can choose . Second, the prediction module is a deep learned model that generates multi-modal predictions of the environment in the form of a *scenario tree*, $\mathbf{e}$. Finally, the dynamic programming module converts $\mathbf{r}$ and $\mathbf{e}$ into an MDP and finds an optimal policy via dynamic programming.

We use the following notation. Let $s_{r}$ denote the state of the ego vehicle and $s_{e}$ denote the state of the environment, including the state of nearby agents and the location of static obstacles. For the trajectory tree, $r_{j}^{i}$ denotes the $j$-th node of stage $i$ and and the root node is simply $r^{0}$. The nodes in the scenario tree are labeled the same way. We enforce that all nodes of the same stage contain trajectories of the same duration with $t_{0}^{i}$ and $t_{f}^{i}$ being the starting and ending time of the $i$-th stage. The trajectory of a any node other than the root needs to follow the trajectory of its parent node. For both trees, $\text{Par}{( \cdot )}$ denotes the parent of a node and $\text{Ch}{( \cdot )}$ denote the set of children of a node, e.g., ${\text{Par}{(r_{1}^{1})}} = r^{0}$, ${\text{Ch}{(e_{0}^{1})}} = {\{ e_{0}^{2},e_{1}^{2}\}}$ for the two trees in Fig. 1.

Next, we discuss the three components in detail.

### III-A Ego-motion sampler

The ego motion sampler generates a set of dynamically feasible trajectory options for planning to consider, and organizes them into a trajectory tree.

Terminal point sampling. We first sample a set of terminal points and then find a feasible trajectory to the terminal point. Terminal points are sampled from a fixed set of acceleration-steering values, as well as along (and near to) lane centerlines when lane information is available.

Spline fitting. We then fit a spline from the current ego state to the terminal point following. Given the current ego state ${s_{r}{\lbrack 0\rbrack}} = {\lbrack X_{0},Y_{0},v_{0},\psi_{0}\rbrack}^{\intercal}$ and a terminal condition ${s_{r}{\lbrack T\rbrack}} = {\lbrack X_{T},Y_{T},v_{T},\psi_{T}\rbrack}^{\intercal}$, we use two separate polynomials $X{\lbrack t\rbrack}$ and $Y{\lbrack t\rbrack}$ to parameterize the $X,Y$ coordinates such that the resulting spline connects the two points and the boundary conditions are met: | | $X{\lbrack 0\rbrack}$ | ${= X_{0}}\quad$ | $X{\lbrack T\rbrack}$ | $= X_{T}$ | | \(1\) | | | $Y{\lbrack 0\rbrack}$ | ${= Y_{0}}\quad$ | $Y{\lbrack T\rbrack}$ | $= Y_{T}$ | | | | | $\overset{˙}{X}{\lbrack 0\rbrack}$ | ${= {v_{0}{\cos\psi_{0}}}}\quad$ | $\overset{˙}{X}{\lbrack T\rbrack}$ | $= {v_{T}{\cos\psi_{T}}}$ | | | | | $\overset{˙}{X}{\lbrack 0\rbrack}$ | ${= {v_{0}{\sin\psi_{0}}}}\quad$ | $\overset{˙}{X}{\lbrack T\rbrack}$ | ${= {v_{T}{\sin\psi_{T}}}}.$ | | | With four boundary conditions on each polynomial, two 3rd order (cubic) polynomial can be uniquely determined, which allows us to directly compute the coefficient of $X{\lbrack t\rbrack}$ and $Y{\lbrack t\rbrack}$ in closed-form and calculate the trajectory from $X{\lbrack t\rbrack}$ and $Y{\lbrack t\rbrack}$. Finally we drop trajectories that violate dynamic constraints.

Tree construction. In practice, trajectory trees are grown stage by stage, starting from the current state as root $r^{0}$. We set an upper bound on the number of children a node can have, and randomly drop children nodes if the limit is exceeded. In each stage we grow children branches in parallel, thus the time complexity is linear in stage number.

### III-B Multi-stage prediction model

A critical part of TPP is the prediction model that generates a scenario tree. For policy planning, we need a scene-centric, ego-conditioned, and multi-stage prediction model. We will first review these requirements and then show examples of deep-learning models satisfying our requirements.

Requirements. First, the prediction model needs to predict *multiple modes* of the trajectory distribution for each agent. Second, predictions must be scene-centric, i.e., outputting modes of the joint trajectory distribution of all relevant agents in the scene. Branches of our scenario tree corresponds to modes of the joint distribution so that our planner will be able to evaluate ego trajectory candidates against joint futures effectively. Examples for multi-modal scene-scentric predictions include. Third, we need ego-conditioning (EC), i.e., prediction results should be conditioned on the ego vehicle's hypothetical future motion. Ego conditioning allows the planner to leverage the reactive behaviors of the environment towards the ego vehicle and is a known technique in prediction literature. However, training a EC prediction model remains challenging as the ground truth under counterfactual ego future motion is not known.

Lastly, we need to generate modes of the predicted trajectory distribution in *multiple stages*. That is, the generated scenario tree contains multiple stages with each node branching into multiple children after each stage. Multistage prediction allows the ego agent to depend its future motion on the future multimodal observation of the environment (similar to a decision tree) and the stage number can be freely set as a design choice. Details on converting existing models to enable multistage prediction can be found in the appendix.

Model architectures. To evaluate TPP's flexibility w.r.t. different prediction models, we tested it with three vastly distinct prediction models. The first model is a rasterized model with CNN backbone and a CVAE; the second model is the PredictionNet model with a Unet backbone, and the third model is the Agentformer model. All models are modified to enable multistage prediction and ego-conditioning. Details can be found in the appendix.

### III-C Dynamic programming

The dynamic programming module takes the ego trajectory tree $\mathbf{r}$ and the scenario tree $\mathbf{e}$, along with a handcrafted cost function $l$ and finds an optimal ego motion policy.

Intuitively, our algorithm constructs a discrete MDP over $\mathbf{r}$ and $\mathbf{e}$ and finds an optimal policy through dynamic programming. More specifically, states of the MDP are nodes of the scenario/trajectory trees that represent the joint ego and environment state; transitions are given by the tree parent/children edges in the two trees; and rewards are defined by the integral of the cost over the time segment. We then solve for the optimal finite-horizon *policy* for the discrete MDP using dynamic programming, i.e., calculating the value function backwards in stage via the Bellman equation. With the optimal policy, the continuous-time trajectory is recovered from the trajectory tree by executing the trajectory segments according to the policy. In practice we use a cost function $l$ with standard terms for collision avoidance, lane keeping, goal reaching, and ride comfort; and a dynamically extended unicycle model for the vehicle dynamics.

Next we provide a formal discussion of the TPP algorithm.

## Formal discussion

### IV-A Analysis without ego-conditioning

In our motion planning problem we are interested in minimizing the expected cumulative cost over a horizon: where $l$ is the running cost function that depends on the ego state $s$ and the environment state $s_{e}$, $T$ is the planning horizon. Our planning algorithm operates on the two trees $\mathbf{r}$ and $\mathbf{e}$ with the same number of stages, so the cumulative cost can be rewritten as where $r^{i}$ and $e^{i}$ are the nodes the ego vehicle and the environment take at stage $i$, and ${L_{i}{(r^{i},e^{i})}} = {\int_{t_{0}^{i}}^{t_{f}^{i}}{l{({s^{r^{i}}{(t)}},{s_{e}^{e^{i}}{(t)}})}{dt}}}$. Due to the stochasticity of the environment, we aim to minimize ${\mathbb{E}}_{e^{0:N}}{\lbrack{\sum_{i = 0}^{N}{L_{i}{(r^{i},e^{i})}}}\rbrack}$, where the expectation is on $e^{i}$, the actual branch the environment takes and the distribution is given as part of the prediction. For simplicity, we shall present the result assuming $\mathbf{e}$ is not ego-conditioned, i.e., there is a single $\mathbf{e}$, and later show that the result can be easily extended to the case with ego-conditioning.

The end result is a policy that chooses which node to execute for the next stage given the current ego and environment node, i.e., $r^{i + 1} = {\pi^{\star}{(r^{i},e^{i})}}$, where $\pi^{\star}$ is the optimal policy. The form of the policy is determined by the assumption about the information flow, i.e., during stage $i$, the ego vehicle can observe the environment's response $e^{i}$, and choose the ego motion among the children nodes of the current node $r^{i}$. To obtain the optimal policy, a value function is needed: which is the expected cost-to-go. The dynamic program goes backwards in stage and is trivial for the last stage: For stage i where $i < N$, we have Since $e^{i + 1}$ is enumerable, the expectation is calculated as where the branching probability of the scenario tree is given by the prediction model. Further define where $r^{i} = {\text{Par}{(r^{i + 1})}}$. We name this function $Q$ function as it is analogous to the $Q$ function in reinforcement learning where here $b^{k + 1}$ is the action we need to choose.

The value function is then obtained backwards in stage: The optimal policy is then

### Theorem 1 (Optimality)

The policy in is the optimal policy with respect to the cost .

### Proof

The proof is by induction. For stage $N$, the cost is a constant, $\pi^{\star}$ is trivially optimal, and $V{(r^{N},e^{N})}$ is the cost-to-go. For $0 \leq i < N$, assume $V{(r^{i + 1},e^{i + 1})}$ is the expected cost-to-go function at stage $i + 1$, then by the principle of optimality, the optimal node to take at stage $i + 1$ is which is exactly $\pi^{\star}{(r^{i},e^{i})}$. This in turn shows that This is true for all nodes in $\mathbf{r}$ and $\mathbf{e}$, then by induction, $\pi^{\star}{(s^{i},e^{i})}$ is the optimal policy for all $i \in {\{ 0,1,\ldots,N\}}$. ∎

### IV-B Extension to ego-conditioned prediction

In the case where the scenario tree is ego-conditioned, the algorithm structure stays roughly the same. To generate the ego-conditioned trajectory prediction, we first run the ego motion sampler to generate the trajectory tree, then the trajectory tree is "flattened " to create the ego-conditioning (EC) modes. E.g., for trees in Fig. 1, the flattened EC modes are shown in Fig. 2.

Figure 2: Flattened trajectory tree as ego-conditioning modes Under each EC mode, the prediction model generates a distinct scenario tree conditioned on the ego vehicle's motion. To keep the planning problem under ego-conditioning well-defined, the ensemble of EC scenario trees needs to satisfy a condition called causal consistency.

### Definition 1 (Causal consistency)

The ensemble of EC scenario tree is causally consistent (CC) if for any stage $i \leq N$, any two scenario trees under different EC modes, if the conditioned ego trajectories are identical up to stage $i$, the two scenario trees are identical up to stage $i$.

This condition guarantees the causality of the policy planning problem as for any particular stage $i$ within the prediction horizon, no future information beyond stage $i$ affects the prediction up to stage $i$. While causal consistency seems trivial, it may be violated by a multi-stage prediction model without special care. For example, if the EC trajectory is encoded as a whole for all stages, the scenario trees generated are not causally consistent.

### Proposition 1 (Sufficient condition for CC)

Assume that a multi-stage ego-conditioned prediction model generates the trajectory prediction stage by stage and the EC prediction is deterministic, then the generated ensemble of EC scenario trees is causally consistent.

### Remark 1

For stochastic prediction models, the generated scenario trees are causally consistent if the random seeds are shared among all EC modes with the same EC trajectory.

The proof is omitted here. It is straightforward to show that the 3 prediction models in Section III-B are CC.

Given causally consistent EC predictions, only two terms change in the policy planning algorithm. First, all nodes of the scenario tree now depend on one of the nodes of trajectory tree of the same stage, and are denoted as $e^{i}{(r^{i})}$ to emphasize the dependence. Note that the dependence is on $r^{i}$ instead of the whole ego trajectory due to causal consistency. Second, the branching probability now depends on the ego node, and is denoted as ${\mathbb{P}}{\lbrack\left. e_{j}^{i + 1} \middle| {{e^{i}{(r^{i})}},r^{i}} \right.\rbrack}$.

Formally, we are solving a finite-horizon MDP with a joint state of $(r^{i},e^{i})$ and the cost defined. The action space is ${A{(r^{i})}} = {\text{Ch}r^{i}}$, the next ego maneuver, and the transition probability is Interestingly, the value function can be defined exactly the same way as Similarly, the Q function is now where $\text{Ch}{({e^{i}{(r^{i})}},r^{i + 1})}$ denotes the set of children nodes following $e^{i}{(r^{i})}$ on the tree associated with $r^{i + 1}$. The optimal policy is then defined as

### Theorem 2

Given a causally consistent ensemble of EC scenario trees, the policy in is the optimal policy with respect to the cost function ${\mathcal{J} = {\sum_{i = 0}^{N}{L_{i}{(r^{i},{e^{i}{(r^{i})}})}}}}.$

### Proof

The proof essentially follows the same steps as the proof of Theorem 1 ‣ IV-A Analysis without ego-conditioning ‣ IV Formal discussion ‣ Tree-structured Policy Planning with Learned Behavior Models"). Starting from stage $N$, the cost is constant, thus $\pi^{\star}$ is trivially optimal and $V{(r^{N},{e^{N}{(r^{N})}})}$ is the cost-to-go. For all $0 \leq i < N$, assume for all $r^{i + 1}$, $V{(r^{i + 1},{e^{i + 1}{(r^{i + 1})}})}$ is the expected cost-to-go function at stage $i + 1$. Then for any $r^{i}$, the cost-to-go to take any children node $r^{i + 1} \in {\text{Ch}{(r^{i})}}$ is ${L_{i}{(r^{i},{e^{i}{(r^{i})}})}} + {{\mathbb{E}}{\lbrack\left. {V{(r^{i + 1},{e^{i + 1}{(r^{i + 1})}})}} \middle| {e^{i}{(r^{i})}} \right.\rbrack}}$, which is exactly $Q{(r^{i + 1},{e^{i}{(r^{i})}})}$. It follows that $\pi^{\star}{(r^{i},{e^{i}{(r^{i})}})}$ gives the optimal $b^{i + 1}$ within $\text{Ch}{(r^{i})}$ and the cost-to-go function of stage $i$ is computed as The optimality of $\pi^{\star}$ is then proved by induction. ∎

## Experiments

TABLE II: Prediction metrics average displacement error (ADE) and final displacement error (FDE) of the three models. The mean is taken over all modes.

### V-A Training of prediction model

We configure TPP with three different prediction models. Apart from the model architecture, the experimental setup is the same. Prediction models are trained with the nuScenes dataset, comprised of 1000 scenes lasting for 20 seconds collected in urban areas of Boston and Singapore. For simplicity, only vehicles are considered. All prediction models use 2 stages and the branching factor is 4.

Loss function. Our training loss is a weighted sum of the following terms: prediction loss that penalizes the error between the predicted trajectories and the ground truth; EC collision loss that penalizes collisions between the predicted trajectories and the conditioned ego trajectory; collision loss that penalizes collisions between predicted trajectories of different agents in the scene; and additional standard regularization losses specific to the model architecture.

Ego conditioning. One natural choice of the ego trajectory for ego-conditioning is the ground truth future trajectory. In addition, to expose the model to more diverse ego trajectories, we perturb the ground truth ego trajectory with noise generated via the Ornstein--Uhlenbeck process as alternative ego trajectories. However, since the ground truth for surrounding agents under the counterfactual ego motion is not available, for the lack of a better choice, we still use the original ground truth as the target for the EC trajectory prediction. We penalize collision between the predicted trajectories of surrounding agents and the conditioned ego trajectory so that the model learns to avoid the conditioned ego trajectory.

Training results. We report standard ADE/FDE prediction metrics for the three prediction models in Table II. The results show that all three models learn reasonable predictions.

Figure 3: Example scene from simulation: the ego vehicle (blue) cuts in front of the red vehicle and then swerve around the green static vehicle in front. The ego trajectory tree is shown in magenta, the colored line shows agents’ actual trajectory.

### V-B Experimental setup

Closed-loop simulation. We evaluate TPP in BITS, a closed-loop AV simulation environment proposed . Each simulation scene is initialized with a scene from the nuScenes dataset and then evolves forward with a policy for each agent. One agent is chosen as the ego vehicle and controlled by TPP or its alternatives. All other agents runs the learned BITS policy that generates realistic and diverse behavior of road vehicles. Additionally, to incite more interactions between agents, we "spawn" new agents around the ego vehicle to challenge the planner throughout the simulation duration.

Metrics. We use three key metrics: collision rate, offroad rate, and area coverage. The first two are calculated as the percentage of time steps where the ego vehicle is in collision (offroad). The coverage metric is calculated with a kernel density estimation (KDE) procedure following, and it captures the effectiveness of the ego plan in terms of liveness and distance travelled. The evaluation is done on 100 scenes from the evaluation split of nuScenes (not used for training).

Baselines. We consider three baselines, the first two are non-contingent counterpart of TPP. For fair comparison, the two baselines share the same ego-motion sampler and ego-conditioning prediction model as TPP, the first baseline, named non-contingency robust (NCR), considers all possible trajectories predicted by the prediction model (similar to ); while the second baseline, named non-policy greedy (NCG), only avoids the most likely prediction mode (similar to ). The third baseline uses a kinematic prediction model with 2 modes: maintaining speed and braking, and share the same multi-stage tree structure.

TABLE III: Closed loop simulation results with TPP and the baselines, the default Agentformer model uses a discrete latent space and Agentformer (Gaussian) is its variant with a Gaussian latent space. TPP significantly outperform the baselines with the same ego trajectory tree and prediction model (bold means best).

### V-C Results

Fig. 3 shows snapshots of the simulation with TPP where the ego vehicle (blue) cuts in front of the red vehicle and then change lane again to avoid the parked green vehicle. The magenta lines show the ego trajectory tree, and the colorful line shows the rollout trajectories of the agents. The quantitative results are shown in Tables III and IV, and we make the following observations. Simulation videos can be found here.

TPP outperforms the baselines. As shown in Table III, TPP significantly outperforms the two non-policy baselines on crash and offroad rate under all 3 prediction models while achieving similar coverage. Even under a simple kinematic model, the performance is better than non-policy planners with sophisticated prediction models. TPP with deep-learned prediction models performs better than with a simple kinematic model, indicating the deep-learned prediction model benefits the closed-loop performance.

Better predictions do not mean better plan. Interestingly, from Table III, the "better" prediction model measured by ADE/FDE does not necessarily lead to better closed-loop performance. For example, the rasterized model is the simplest and "worst" model among the three, yet TPP with it outperforms the other two in terms of crash rate.

Ego-conditioning is useful. Table IV compares TPP with or without ego-conditioning. Ego-conditioning improves the closed-loop performance considerably in most cases, especially the coverage metric, hinting that the ego vehicle is more comfortable moving through traffic when it expects reaction from other agents.

Temporal consistency is important. Additionally, we tested the Agentformer model with Gaussian latent space, where the prediction requires sampling of the latent variable at every inference call, compared to using discrete latent space where sampling is not needed. While the prediction ADE/FDE is similar, the closed-loop performance with the Gaussian latent is significantly worse. We suspect this is due to the poor temporal consistency between predictions of consecutive time steps. While both TPP and the two baselines saw performance degradation under the Gaussian latent, the policy planner relies on more sophisticated prediction/planning interaction, thus suffers more than the two baselines.

TABLE IV: Ablation study of ego-conditioning, the first and second number are the metrics with and without ego conditioning. Most metrics see degradation when ego-conditioning is disabled (bold means better).

TABLE V: Runtime of the three key components Runtime analysis. Table V shows the runtime of the three components of TPP on an Nvidia 3090 GPU (most computation is done on GPU). It should be noted that all runtime is recorded on unoptimized Python code and there is significant space of improvement. For example, the long runtime for PredictionNet is mainly due to rasterization, and we know its runtime can be as low as 5ms with the proper engineering, e.g., efficient CUDA code for rasterization. While the runtime for prediction models is not very informative and is not the focus of this paper, it is quite clear that ego motion sampling and dynamic programming can be done very efficiently. With proper optimization, we believe that TPP can be easily implemented in real time. We plan to release the code upon publication.

## Conclusion

We present TPP, a policy planner capable of generating multistage motion policies that react to the environment. It is centered around an ego trajectory tree and a scenario tree that predicts the environment behavior, both containing multiple stages. Ego-conditioning is applied to leverage the reactive behavior of the environment under the ego vehicle's presence. The closed-loop simulation result shows that TPP significantly outperform two non-policy benchmarks and the runtime test suggest that such sophisticated policy planner can be run in real time. Our planned future works include study more flexible topology of the trees and enable event-triggered branching improve the efficiency of computation, especially under ego-conditioning adaptive and personalized policy planning.
