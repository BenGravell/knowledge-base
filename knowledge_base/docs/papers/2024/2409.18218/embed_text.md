## Introduction

We are interested in developing policies that drive realistically like a human, reason about complex interactions, and handle safety-critical scenarios. While previous methods have demonstrated improved performance by applying supervised learning with gradually increasing dataset sizes, such an approach has several limitations. Collecting driving datasets at scale is extremely expensive, requiring fleets of vehicles deployed for long stretches of time. Furthermore, a central challenge of self-driving is handling rare edge cases safely, while the majority of nominal driving data is repetitive and contains little learning signal. Upsampling existing curated scenarios may help with data imbalance, but is ultimately limited by the existing collected set of logs. Yet purposefully inducing additional safety-critical scenarios in the real-world for data collection is too dangerous of a solution at scale. *How can we continue to scale training data without relying solely on real-world collection?*

One approach is to have policies explore novel states by leveraging closed-loop simulation and methods like reinforcement learning. However, since other actors in simulation typically exhibit nominal behavior, the resulting simulations can still be repetitive and unchallenging. Likewise, leveraging a self-play approach where a policy interacts with itself in multiagent simulation can suffer from the same issue if the policy converges to nominal and cooperative behavior. One can leverage human prior knowledge and design additional synthetic scenarios targeting particularly difficult interactions like cut-ins, but scaling the diversity of these scenarios can be difficult even with procedural generation approaches. The realism of the scenarios may also be lacking since actor behaviors are often scripted and hand-specified, which can lead to a sim-to-real gap in policies trained on these scenarios. Alternatively, adversarial optimization can be used to find trajectories that result in collision scenarios in an automated fashion. To ensure the usefulness of these scenarios for training, various solvability regularization approaches can be used (*e.g*. ensure the adversary doesn't collide with the pre-recorded trajectory, or ensure a kinematically feasible solution exists). Nevertheless, scenarios can still easily end up being too easy or too difficult for the learning policy, depending on the design of such terms.

To address these shortcomings, we propose an *asymmetric self-play* mechanism in which challenging, solvable, and realistic scenarios naturally emerge from interactions between policies with differing objectives. We introduce the notion of a teacher and student policy (also referred to as Alice and Bob respectively in the literature), where the teacher aims to generate scenarios that the student cannot solve but the teacher itself can. This produces challenging training scenarios for the student as opposed to repeatedly training on nominal data where the learning signal is weak. Because the teacher and student improve together, novel scenarios that continue to be difficult for the student can be proposed by the teacher over the entire course of training, leading to a natural curriculum of increasingly difficult scenarios, similar to how humans learn. Finally, both policies are regularized to stay close to the data distribution to maintain realism and prevent policy collapse.

Our experiments show learning to drive via asymmetric self-play results in more realistic and robust policies. When applied to the multiagent traffic simulation problem setting, we learn actor policies with significantly reduced collision rates in both nominal scenarios and held out out-of-distribution scenarios, while still maintaining other realism metrics. We further show that these policies can *zero-shot transfer* to generate scenarios for new, unseen policies. This allows us to first efficiently train privileged traffic agents with self-play at scale using lightweight state simulation, before deploying these agents to interact with an end-to-end autonomy policy using high-fidelity sensor simulation. Our experiments show that training autonomy on the resulting dataset leads to far higher goal success rates and lower collision rates compared to alternatives like adversarial approaches or using real data alone.

## Related Work

### Learning to drive

Pioneered in, numerous works have explored learning to drive for applications in autonomous driving and traffic simulation. A popular approach is open-loop behavior cloning (BC), which reduces learning to drive to a supervised learning problem. However, BC suffers from compounding errors from distribution shift in closed-loop execution and a variety of techniques have been proposed to address this problem, including data augmentation, regularization based on prior knowledge, uncertainty-based regularization, inference-time search, *etc*. Another approach is to train the driving policy in closed-loop with closed-loop imitation learning, reinforcement learning, or a combination of the two. Here, the driving policy is exposed to and learns from states induced by the consequences of its actions, thereby minimizing distribution shift. Despite these algorithmic, model, and data-scale improvements, learning-based policies still exhibit higher-than-human failure rates, especially in highly-interactive scenarios. As an orthogonal approach to learning better driving policies, in this work, we explore improvements in the training data *composition and curriculum* by automatically generating challenging scenarios, demonstrating its efficacy in both autonomous driving and traffic simulation.

### Challenging scenarios

Learning to handle long-tail situations from data is difficult when the majority of real-world driving data is uneventful with little learning signal. One can up-sample challenging examples from a large set of real world logs, but this limits us to a fixed set of existing logs, and collecting more at scale (especially safety-critical ones) can be expensive and unsafe. Hand-designed synthetic scenarios that expose the driving policy to challenging interactions can be used, but it is tedious to create realistic scenarios in this way and scaling these approaches to cover the diversity of the real world is impractical. Adversarial methods can automatically discover challenging scenarios by optimizing a fixed objective for difficulty using gradient-based optimization, Bayesian optimization, tree search, evolutionary algorithms, rare-event simulation, reinforcement learning, or retrieval augmented generation. To ensure that the adversarial scenarios are useful for training, various constraints are added to encourage solvability and realism. Unlike adversarial approaches which typically attack a fixed policy, our self-play approach allows the teacher and student to continually update and improve. Likewise, our solvability objective directly considers the *current* student policy rather than surrogates like the logged trajectory or the result of a separate optimization process, resulting in more relevant scenarios for training.

### Self-play

Self-play training is a popular approach to learning policies in increasingly complex and diverse environments by having them interact among copies of themselves, with recent high-profile successes in Go, StarCraft, Dota 2, Diplomacy, *etc*. In the context of self-driving, learns RL policies in multiagent merge traffic by having them interact in scenarios with simple rules-based agents initially and then increasingly capable past copies of themselves. More generally, rules-based agents can be omitted and standard multiagent reinforcement learning (MARL) approaches can be used. However, since the RL policies share a common objective, the training scenarios become increasingly uneventful and repetitive for learning as the policies converge in capabilities and learn to cooperate. In contrast, we propose to use an asymmetric self-play mechanism where a teacher (Alice) learns to propose challenging but self-solvable scenarios, and a student (Bob) learns to solve them. Whereas asymmetric self-play was first proposed for goal-discovery in RL, we use asymmetric self-play to scale our training data beyond what's available from the real world and learn increasingly realistic and robust driving policies. To this end, we also augment the teacher's objective to propose scenarios that are realistic as well.

## Asymmetric Self-play for Driving

### Problem Formulation

We begin by introducing the multiagent traffic modeling formulation. A traffic scenario over $T$ timesteps consists of a high definition (HD) map $\mathbf{m}$, the joint states ${\mathbf{s}}_{1:T}$ for $N$ actors over $T$ timesteps, and the corresponding actions ${\mathbf{a}}_{1:{T - 1}}$. We use $s_{t}^{i}$ to denote the $i$-th actor's state at time $t$, which consists of its position, heading, velocity, bounding box, and class in 2D bird's eye view. Likewise, we use $a_{t}^{i}$ to denote the $i$-th actor's action at time $t$, which consists of its acceleration and steering angle. Given the HD map $\mathbf{m}$ and initial states ${\mathbf{s}}_{1}$, we model the distribution over possible rollouts as:

where $\pi$ is a multiagent policy controlling all actors jointly and $p{(\left. {\mathbf{s}}_{t + 1} \middle| {{\mathbf{s}}_{t},{\mathbf{a}}_{t}} \right.)}$ is the state transition dynamics, which we model with a kinematic bicycle model on a per-actor basis.

### Asymmetric Self-Play Learning

Figure 2: Method Overview. We sample an initial scene and designate adversarial actors at random. The teacher must control adversarial actors such that the student fails, but itself passes. Adversarial actions are replayed to keep the scenario the same.

Toward our goal of automatically generating *challenging, solvable,* and *realistic* scenarios for learning to drive, we design an asymmetric self-play mechanism where a teacher policy learns to propose scenarios that it can pass but a student policy fails. During training, the teacher will either control all actors in the scene or interact with a subset of student-controlled actors. When the teacher interacts with the student, it aims to cause student-controlled actors to collide; and when the teacher controls all actors, it aims to demonstrate a collision-free solution instead. The student can then improve their driving by learning to avoid collisions in the proposed scenarios. As the two are jointly trained, the teacher continually adapts their proposals to the student's capabilities throughout learning.

Concretely, let $\pi_{T}$ and $\pi_{S}$ be the multiagent teacher and student policies respectively. A scene can be entirely controlled by the teacher by only sampling actions from $\pi_{T}$ (Eq. 1). However, it is also possible for the two policies to *interact* by controlling different actors within the same scene. If we partition $N$ actors into two sets $\mathcal{T}$ and $\mathcal{S}$, then the two policies $\pi_{T}$ and $\pi_{S}$ can come together as $\pi_{TS}$ to jointly control the scene,

and ${\pi_{TS}{(\left. {\mathbf{a}}_{t} \middle| {{\mathbf{s}}_{\leq t},{\mathbf{m}}} \right.)}} = {\prod_{i = 1}^{N}{\pi_{TS}{(\left. a_{t}^{i} \middle| {{\mathbf{s}}_{\leq t},{\mathbf{m}}} \right.)}}}$.

The teacher's goal is to generate challenging, solvable, and realistic scenarios, so we define its objective as:

Here $c_{i}{({\mathbf{s}})}$ is an indicator function that equals 1 if actor $i$ fails (collides) and 0 otherwise. The first term $C{(\pi_{TS},\mathcal{S})}$ thus encourages the teacher to generate challenging scenarios where student-controlled actors fail. The second term $- {C{(\pi_{T},N)}}$ encourages the teacher $\pi_{T}$ to generate solvable scenarios where it can demonstrate a collision-free rollout when controlling all $N$ actors. The final term $\beta{({{I_{\text{data}}{(\pi_{T})}} + {I_{\text{data}}{(\pi_{TS})}}})}$ encourages the teacher to generate realistic scenarios (when the teacher controls all actors and when the teacher interacts with the student respectively), where $p_{\text{data}}$ is the data distribution^11^1 We approximate $p_{\text{data}}$ by using the ground truth rollout ${\mathbf{s}}_{\text{data}}$ from real logs and assuming ${p_{\text{data}}{({\mathbf{s}},\left. {\mathbf{a}} \middle| {\mathbf{c}} \right.)}} \propto {\exp\left\lbrack {- {D{({\mathbf{s}},{\mathbf{s}}_{\text{data}})}}} \right\rbrack}$ where $D$ is the Huber loss. and $\beta$ is a hyperparameter controlling the regularization strength.

Conversely, the student's objective is to control its actors to avoid failures and behave realistically when interacting with the teacher.

Our learning framework is inspired by and resembles single-agent asymmetric self-play where the teacher searches for goal states that the student cannot reach. In our multiagent setting, the notion of a reachable state is instead replaced with the notion of a solvable scenario, which depends on *interaction* between the teacher and student. Over the course of training, the teacher and student learn together to generate a curriculum until an equilibrium is reached.

### Theoretical Analysis

We now prove that for universal policies, our asymmetric self-play objective trains the student to pass all scenarios that have a reasonably realistic solution.

### Definition 1

A policy $\pi_{Y}$ is $\alpha$-$\beta$-optimal if $\forall\pi_{X}$ where ${I_{\text{data}}{(\pi_{XY})}} > \alpha$ and ${C{(\pi_{X},N)}} = 0$,

Intuitively, an $\alpha$-$\beta$-optimal policy will only fail an $\alpha$-realistic solvable scenario (as demonstrated by ${C{(\pi_{X},N)}} = 0$) if the log likelihood of all possible solutions is at least $1/\beta$ lower than the log likelihood of the failure under the data distribution, where $\beta > 0$ controls the realism regularization strength and is arbitrarily set.

### Lemma 1

If $\pi_{T}$ and $\pi_{S}$ are in equilibrium ($\pi_{T}$ cannot improve without changing $\pi_{S}$ and vice versa), then $R_{T} \leq {2\betaI_{\text{data}}{(\pi_{TS})}}$.

### Proof

Assume that $R_{T} > {2\betaI_{\text{data}}{(\pi_{TS})}}$. Then it follows \\linenomathAMS

However, Eq. 9 shows that then $\pi_{S}$ can improve its return (Eq. 6) by simply copying $\pi_{T}$, which contradicts the equilibrium assumption. ∎

### Theorem 3.1

If $\pi_{T}$ and $\pi_{S}$ are in equilibrium, then $\pi_{S}$ is $\alpha$-$\beta$-optimal, where $\alpha = {{I_{\text{data}}{(\pi_{TS})}} + \frac{1}{2\beta}}$.

### Proof

Assume that $\pi_{S}$ is not optimal. Then there must exist a $\pi_{X}$ where ${I_{\text{data}}{(\pi_{XS})}} > \alpha$ and ${C{(\pi_{X},N)}} = 0$ for which

where Eq. 11 uses the fact that ${C{(\pi_{X},N)}} = 0$, Eq. 12 comes from adding $\beta\left( {{I_{\text{data}}{(\pi_{XS})}} + {I_{\text{data}}{(\pi_{X})}}} \right)$ to both sides, and Eq. 13 comes from substituting in ${I_{\text{data}}{(\pi_{XS})}} > \alpha$ and applying Lemma 1. However, this shows that $\pi_{T}$ can improve by copying $\pi_{X}$, contradicting the equilibrium assumption. ∎

Thus we see under the proposed asymmetric self-play objective, a student in equilibrium with the teacher should solve any reasonably realistic solution.

### Ensuring Fair-play

While Eq. 3 encourages teacher-solvable scenarios, the teacher has an unfair advantage as it can coordinate all actors. For example, the teacher may try to identify student-controlled actors and propose more difficult (and potentially unsolvable) scenarios only for the student. This impedes the student's ability to learn and thus motivates additional restrictions on the teacher.

### 3-player formulation

To address unfair coordination, we can divide the teacher into two sub-policies, adversary and demonstrator. When $\pi_{T}$ is used to control all $N$ actors, the adversary sub-policy controls actors in $\mathcal{T}$ and the demonstrator sub-policy controls actors in $\mathcal{S}$. Thus any coordination the demonstrator may try with the adversary can in principle be learned by the student, as their architectures are now identical.

### Replay actions

Note that the teacher's reward in Eq. 3 is a function of a pair of rollouts sampled from $\pi_{T},\pi_{TS}$ using *identical initial conditions* ${\mathbf{s}}_{1},{\mathbf{m}}$. We can replay states for actors in $\mathcal{T}$ in one simulation from the pair. Let ${\overline{\mathbf{a}}}_{\leq T}$ be actions sampled from $\pi_{TS}$. Then when rolling out $\pi_{T}$, we instead use the modified policy

where $\delta$ is the Dirac-$\delta$ function. This prevents the teacher from treating itself differently and enforces it to solve the exact same scenario subjected to the student. While the equation above is illustrative for when actors in $\pi_{T}$ is replayed, during training, we randomly select whether $\pi_{T}$ or $\pi_{TS}$ is replayed.

### Implementation

Figure 3: Policy Architecture. We encode K lane graph nodes and state history for N actors over H history timesteps into D-dimensional features. A transformer backbone with M blocks uses factorized attention to extract features before decoding them into actor steering and acceleration. The teacher policy additionally encodes actor type (if an actor is in 𝒯) and target information; the student does not observe this information.

### Neural Network Architecture

We implement our policy network with a viewpoint-invariant transformer. Given a lane graph $\mathbf{m}$ with $K$ nodes, we first use a viewpoint-invariant map encoder to extract a set of lane graph node features,

For each actor $i$, our state encoder uses a multi-layer perceptron (MLP) to extract features for its past state $s_{t - H}^{i},\ldots,s_{t}^{i}$ over the past horizon $H \geq 1$,

where $\oplus$ is the concatenation operator, $v_{t^{\prime}}^{i},\ell^{i},w^{i}$ is the actor's velocity, length, and width, and $\varphi_{t\rightarrow t}^{i}$ is the PairPose relative positional features between the actor's position at the current time $t$ and past time $t^{\prime}$; *i.e*., $g_{i\rightarrow j}^{a}$ in \[20, Eq. 1\]. Each actor feature ${\mathbf{h}}_{t^{\prime}}^{i}$ encodes the $i$-th actor's state at $t^{\prime}$ in its local coordinate frame at $t$, therefore preserving viewpoint-invariance.

Next, we use a stack of interleaving actor-to-map, actor-to-actor, and actor-to-time transformer layers to efficiently model actor and lane graph interactions. Our actor-to-time layer uses standard self-attention, with sinusoidal positional encoding to break the symmetry across time. To model actor-to-actor interactions in a viewpoint-invariant manner, we extend standard self-attention to use relative positional encodings between actors. For the $i$-th actor at time $t^{\prime}$, we compute attention with key ${\mathbf{k}}_{i}$, queries ${\{{\mathbf{q}}_{i,j}\}}_{j = 1}^{N}$, and values ${\{{\mathbf{v}}_{i,j}\}}_{j = 1}^{N}$,

where $\varphi_{t^{\prime}}^{i\rightarrow j}$ is the PairPose features between actors $i$ and $j$ at time $t^{\prime}$.

We use the same attention mechanism in our actor-to-map layer with two modifications for efficiency: *1)* we use actor-to-map only for the current time $t$ and *2)* we limit its queries and values to the actor's $k$ nearest lane graph nodes.

Finally, our action decoder uses an MLP to deterministically predict each actor's steering and acceleration from its features ${\mathbf{h}}_{t}^{i}$ at the current time $t$ after $M$ blocks of transformer layers.

The policy can then be unrolled in the environment in a sliding window fashion.

### Optimization

We describe how to optimize Eqs. 3 and 6 in practice. During training, we randomly assign agents into $\mathcal{T}$. For ease of optimization, we *1)* relax the discrete indicator function $c_{i}{({\mathbf{s}})}$ to a differentiable collision loss, *2)* assign a specific target actor for each actor in $\mathcal{T}$ for which the collision loss is active,^22^2 Always targeting the closest actor showed similar results, but the ability to target a specific actor is useful in the zero-shot setting (to target the external policy). and *3)* apply an additional distance loss to encourage each adversarial actor towards its target. To encode the information that actor $i$ targets actor $j$, we have

where $\mathbf{e}$ is a learnable embedding to indicate the actor is in $\mathcal{T}$ and the PairPose features provide positional information on the target. In the 3-player formulation, only the adversarial sub-policy has access to this information. Finally, as our relaxed reward is differentiable, we can use backpropagation through time to directly optimize the learning objective.

## Experiments

### Realistic Traffic Simulation

### Datasets

We use three different datasets to evaluate our model's performance. Argoverse2 Motion is a collection of 250k urban scenarios curated for challenging multiagent-interactions. Agents are given 5s of history before unrolling for 6s. Our policy observes all actors but only controls focal and scored agents while the remaining actors are replayed due to noisy or incomplete annotations.

Next, Highway is a collection of over 1000 highway logs collected over various locations including on-ramps, off-ramps, forks, merges, and curved roads. Agents are given 3s of history before unrolling for 10s. As Highway consists of high-quality human labels, all actors are controlled.

Finally, Safety is a collection of over 100 hand-designed safety-critical highway scenarios with various edge cases including aggressive actor cut-ins, lead actor hard-braking, actors stopped on shoulder, etc. These scenarios are simulated and involve actors that are scripted to induce safety-critical interactions while the actor policy controls the ego actor that is meant to be tested. As Safety scenarios are simulated and interactive to the policy being evaluated, no ground truth human demonstrations are available. We use Safety to evaluate models trained on Highway without any fine-tuning, measuring their out-of-distribution generalization to highly-interactive, safety-critical scenarios.

Figure 4: Qualitative Comparison. We show TrafficSim (top) and Ours (bottom) on Argoverse2. Our method learns better interaction reasoning to avoid collisions realistically. Colored actors are controlled; gray actors are replayed.

### Traffic Modelling Metrics

We use a suite of metrics to evaluate the realism of traffic simulation agents. Final displacement error (FDE) measures the L2 error between the agent's simulated future and ground truth (GT) position at the end of the rollout. Collision percent is used to evaluate actors' interaction reasoning, and Offroad percent evaluates actors' map understanding. We also measure the distributional similarity of various actor features. This is done by fitting histograms to agents' linear speed, linear acceleration, angular speed, distance to road boundary, and distance to the closest actor, before taking the Jensen-Shannon divergence (JSD) to the GT statistics. Following, GT statistics are computed for each actor separately, with time being considered independent. These are then averaged to form our composite JSD metric.

### Baselines

We compare our approach against the current state-of-the-art for traffic simulation. Closed-loop IL is our supervised learning baseline that is trained to regress expert states using closed-loop policy unrolling. TrafficSim further incorporates prior knowledge to closed-loop IL using a differentiable collision loss. For our standard symmetric self-play baseline, we adapt the multiagent RL (MARL) approach in SMARTS to our setting by applying a factorized PPO loss to the multiagent policy to optimize a hand-designed reward. Emb. Syn. is a curation-based approach which sub-samples the dataset using a learned difficulty classifier. As uses an extremely large internal dataset containing a 14k hours of driving, to adapt their approach to the datasets used in this work, we *1)* directly select the snippets where the baseline IL model fails in rather than training a difficulty classifier and *2)* finetune the baseline IL model on the selected snippets instead of training from scratch. KING is a gradient-based adversarial approach where the adversarial objective is backpropagated through bicycle model dynamics. We adapt to generate adversarial training examples with the same realism regularization term as ours (stay close to the logged trajectory) for training the base traffic policy. All baselines are adapted to use the same input/output representation, model architecture, and environment dynamics. More details can be found in the supplementary.

Emb. Syn. (Curation)

Table 1: Traffic Simulation Results. On Safety, Highway, and Argoverse2, our approach obtains the best collision rates without sacrificing other realism metrics.

### Results

Recall that models trained on Highway are evaluated on Safety without fine-tuning. Tab. 1 shows that the IL baseline consistently achieves the best reconstruction metrics but struggles with interaction reasoning, resulting in higher collision rates. By adding in prior knowledge using the differentiable collision loss, TrafficSim can reduce the collision rate with some trade-off in other realism metrics. MARL struggles the most as it is difficult to capture realistic human-like driving with a handcrafted reward alone. Curation is ineffective at our dataset scale, even for Argoverse2 which is among the largest publicly available datasets. This is potentially because Argoverse2 is already curated. KING reduces collision rate on Safety but still struggles with nominal collisions. This could be due to the fact that the realism of the adversarial trajectories is lacking, lowering their transferability. Our approach consistently achieves the best overall realism, achieving the lowest collision rates with minimal sacrifice in other metrics, and generalizes the best to the Safety set.

### Zero-shot Scenario Generation for Learnable Autonomy

In Sec. 4.1, we have shown that after self-play training, the teacher has helped the student learn a more realistic and robust policy for multiagent traffic simulation. We now evaluate the teacher's ability to zero-shot transfer to generate scenarios for *new unseen* policies. The ability for zero-shot transfer not only shows that the teacher policy has learned *generally applicable* training scenarios but also provides an efficient way to improve more expensive policies. Traffic simulation agents use low dimensional (bicycle model) states as input, so they can be efficiently trained at scale with lightweight and efficient simulation. Agents can then be deployed to interact with end-to-end autonomy policies that require additional more expensive high-fidelity sensor simulation. This allows us to generate training scenarios for the autonomy policy by simply deploying our teacher policy to target the external policy, without needing to retrain in the more expensive simulation setting.

Table 2: End-to-end autonomy results on Safety and Highway. (↑/↓) denotes higher/lower is better, (Δ) denotes closer to expert is better. Among the unprivileged methods, we obtain the best overall performance, with emphasis on Safety.

### Learnable Autonomy Systems

To evaluate the generalizability of our approach, we consider training two distinct autonomy paradigms on datasets generated using our approach versus various baselines. Our object-based autonomy estimates actor locations with a discrete set of bounding boxes and trajectories using a joint perception and prediction backbone. Our object-free autonomy estimates actor locations with continuous occupancy probabilities across the scene to be used for motion planning. Both approaches sample trajectories in Frenet frame before costing each trajectory and selecting the min-cost trajectory. Costs are computed as a linear combination of several trajectory features, where weights are learned using max margin. Expert demonstrations are generated using an oracle planner with privileged access to ground truth actor states and future plans. As both autonomy approaches use LiDAR input, LidarSim is used for training-dataset generation and evaluation in closed-loop simulation. More details can be found in the supplementary.

### Autonomy Evaluation

We evaluate an autonomy's nominal driving with Highway in reactive log replay^33^3Actors are constrained to their original path, with a heuristic policy controlling their acceleration so that actors can react to the ego vehicle during closed-loop simulation., and safety-critical performance with Safety (both datasets described in Sec. 4.1). For our primary system performance and safety metrics, Goal Success Rate (GSR) measures if the ego reaches its goal without violating traffic rules or colliding, and Collision (Col) measures collisions with the ego vehicle. We use secondary metrics to measure other aspects of driving quality. Minimum Time-To-Collision (mTTC) is computed between the ego vehicle and other actors assuming constant velocity and acceleration. Progress (Prog) is the distance traveled over the scene. Plan to Execution (P2E) is the deviation between the ego plan and its executed trajectory, measuring a notion of planning consistency. Acceleration (Accel) is the average of the longitudinal and lateral acceleration, measuring discomfort. Primary metrics have a clear direction where higher/lower is better. Secondary metrics are less clear (*e.g*. progress should be high but not compromise safety/speed-limit, P2E should be low in general but high when encountering unexpected behaviors). Thus secondary metrics are better if they are closer to the expert.

### Baselines

Our first baseline is using Highway in reactive log replay. Next, we use Closed-loop IL and Adversarial (Sec. 4.1) to generate datasets. Finally, we report two privileged approaches: *1)* the performance of the expert autonomy and *2)* the performance of training directly on the Safety test set.

### Results

Tab. 2 shows that nominal driving (Highway, IL) does not contain enough exposure to edge cases for autonomy to generalize to the Safety set. Adversarial generation improves performance but is still lacking. We posit that the per-scenario optimization process reaches local optima that our approach has learned to avoid over the course of training. Similarly, our model also learns more general notions of realism, compared to the per-scenario objective of staying close to the logged trajectory. These factors are particularly pronounced for our object-free autonomy, which relies on more difficult scenarios during training but results in more conservative driving. Thus, we achieve high-quality driving performance for both Safety and Highway evaluation, closely matching the performance of the privileged approaches across both autonomy paradigms.

### Ablation and Analysis

In this section, we ablate various aspects of our asymmetric self-play learning objective and model architecture using the traffic simulation setting as a test bed. We also provide additional analysis of the training dynamics of our approach.

### Ablation

Table 3: Teacher loss design.

Table 4: Teacher architecture design.

First we ask, *how important is it for challenging scenarios to be solvable and realistic?* We ablate the solvability and realism terms in the teacher objective in Eq. 3; Tab. 4 shows that both are necessary for the student to learn realistic and robust behavior. Without solvability, the teacher generates extremely difficult scenarios, resulting in an overly cautious student which avoids collisions on Safety but drives poorly in nominal scenarios, exhibiting unnecessary and extreme evasive maneuvers. Without any realism, scenarios become so extreme that they no longer even transfer to Safety.

Next we ask, *how effective are the fair-play architectural design choices presented in Sec. 3.4?* Tab. 4 shows that combining the 3-player and replay approach results in the best overall performance. Using neither of the two achieves a very low Safety collision rate at the cost of greatly increasing nominal collisions. This is because the teacher overestimates the solvability of a scenario, leading to similar outcomes as when the solvability loss term is omitted.

### Adversarial Success vs. Student Performance

Figure 5: (Left): When the student is training, adversarial success plateaus but the student continually improves. (Center): When the student is frozen, adversarial success improves along with teacher performance. (Right): Our approach dominates the Pareto frontier obtained from naively increasing collision loss weight.

We wish to analyze the correlation between adversarial success, (the teacher's ability to find solvable scenarios that the student fails) and the performance of the student. Fig. 5 (left) shows the teacher's return (minus realism) and the student's performance on Safety. Despite the teacher's return staying flat, the student continually improves. Because the student trains with the teacher, it is difficult for the teacher to consistently outperform the student to improve its objective. Fig. 5 (right) shows the teacher's performance when the student is frozen. In this case teacher can continually increase its return by exploiting scenarios the frozen student fails. However, there is less incentive for the teacher to increase the difficulty of the training scenarios, resulting in the teacher having worse performance compared to a continually improving student.

### Pareto Frontier

We show in Fig. 5 (right) that the improvements of our approach cannot be obtained by increasing the weight on the differentiable collision loss in TrafficSim. Our results suggest that difficult scenarios are more useful for learning robust policies while maintaining performance on nominal driving.

## Conclusion and Limitations

We have presented an asymmetric self-play approach for learning to drive, where solvable and realistic scenarios naturally emerge from the interactions of a teacher and student policy. We have shown that the resulting student policy can power more realistic and robust traffic simulation agents across several datasets, and the teacher policy can zero-shot generalize to generating scenarios for unseen end-to-end autonomy policies without needing expensive retraining. While the results are promising, we recognize some existing limitations. Firstly, the specific *type* of scenarios the teacher finds is not controllable; incorporating advances in controllable traffic simulation or exploring alternative reward designs and training schemes to encourage diversity can be interesting directions to explore. Exploring alternative failure modes besides collision (*e.g*. off-road, unrealistic behaviors, perception failures) is another promising avenue for future work.
