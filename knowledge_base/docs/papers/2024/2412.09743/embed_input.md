<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Should We Learn Contact-Rich Manipulation Policies from Sampling-Based Planners?

Topics include Motion planning, Robotics, Diffusion models, Sampling-based methods, Optimization, Planning, Learning, Sampling, Behavior cloning, Rapidly-exploring random tree.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The tremendous success of behavior cloning (BC) in robotic manipulation has been largely confined to tasks where demonstrations can be effectively collected through human teleoperation. However, demonstrations for contact-rich manipulation tasks that require complex coordination of multiple contacts are difficult to collect due to the limitations of current teleoperation interfaces. We investigate how to leverage model-based planning and optimization to generate training data for contact-rich dexterous manipulation tasks. Our analysis reveals that popular sampling-based planners like rapidly exploring random tree (RRT), while efficient for motion planning, produce demonstrations with unfavorably high entropy. This motivates modifications to our data generation pipeline that prioritizes demonstration consistency while maintaining solution diversity. Combined with a diffusion-based goal-conditioned BC approach, our method enables effective policy learning and zero-shot transfer to hardware for two challenging contact-rich manipulation tasks.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many everyday manipulation tasks require coordinating multiple contacts with objects using different parts of the body, such as opening a bottle or carrying a large box. To endow robots with true autonomy, acquiring proficiency in these contact-rich dexterous manipulation skills is crucial. However, executing such skills demands intricate coordination between the hands, the arms, and even the whole body, which leads to a high-dimensional action space. Compared to single-arm, gripper-based tasks such as pick-and-place, contact-rich dexterous manipulation is also more likely to introduce multi-modality to the solution, i.e., there can be more than one way to accomplish the task.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent years have witnessed a rising trend of learning robotic manipulation skills from human teleoperation. Together with the advances in generative modeling through diffusion models, behavior cloning (BC) methods have demonstrated their capabilities to learn multi-modal and long-horizon tasks under the simple paradigm of supervised learning. However, human teleoperation as a data collection method comes with significant limitations. Firstly, as mainstream teleoperation interfaces only support tracking the robot end effectors, demonstrations that involve full-arm contacts and multi-finger coordination are challenging to collect. Furthermore, the data collection process is inherently bottlenecked by the availability of human operators, making it difficult to scale robot learning in the same way as vision and language tasks.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

These limitations have motivated recent work in leveraging synthetic data generated through physics-based simulators. Such data can be produced through various approaches: reinforcement learning (RL), model-based trajectory optimization, or a combination of both. This teacher-student training paradigm, where a BC agent learns from an algorithmic expert, has shown success across domains including autonomous driving, legged locomotion, and dexterous manipulation. Given these successes, recent attention has turned to a critical question: how can we produce and curate high-quality data to improve student policy performance? Prior studies define data quality by the distribution shift between the expert that generates the data and the learned policy, arguing that the best data offers sufficient coverage while maintaining low entropy.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

While RL methods have achieved impressive progress in contact-rich dexterous manipulation, they do not provide a disentangled way to control the action entropy of the policy. Most RL algorithms heavily rely on careful reward shaping, making it difficult to balance exploration, task performance, and constraint satisfaction while controlling data quality. If a reward term were added to encourage low-entropy action, it could also affect exploration and degrade task performance.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, model-based planning and optimization methods offer more granular control over the data generation process through explicit sampling mechanisms and domain-specific priors. Indeed, recent works have shown that data produced by model-based planning and optimization can be used to directly train an end-to-end policy via BC for collision-free motion planning or legged locomotion. For contact-rich manipulation, recent advances in search- and sampling-based planning through contact have emerged as a promising model-based alternative to RL. Such approaches can solve contact-rich dexterous manipulation tasks with significantly fewer samples while allowing for straightforward design of cost functions and strict satisfaction of constraints.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we study how to leverage model-based planners to produce high-qualit data for learning contact-rich manipulation skills.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that using inconsistent, high-entropy demonstrations degrades policy performance when learning contact-rich manipulation skills through BC.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Drawing from 1), we present a data generation pipeline that produces consistent training data to facilitate effective policy learning.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We conduct extensive experiments and analysis, validating our hypothesis on challenging contact-rich manipulation tasks using a diffusion-based goal-conditioned BC approach.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

AllegroHand: an in-hand object rotation task depicted in the top row of Fig. LABEL:fig:tasks, where a 16-DoF dexterous hand needs to re-orient the cube to a desired orientation.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

IiwaBimanual: a bimanual manipulation task depicted in the bottom row of Fig. LABEL:fig:tasks, where two robot arms are required to rotate an over-sized object by $180\ {{^\circ}\text{/}}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Both tasks require reasoning over a long horizon of complex multi-contact interactions with frequent contact switches, presenting significant challenges for both RL and human teleoperation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Method", "weight": 1.0} -->

Fig. provides an overview of our method. First, we obtain a training dataset via a multi-stage data curation pipeline: 1. a model-based planner using smoothed contact dynamics proposes a plan, 2. this plan is then executed in a physics simulator without contact smoothing to produce state-action trajectories. 3. the reached states are labeled as goals using hindsight goal relabeling. Using the generated dataset, we learn a goal-conditioned diffusion policy mapping the observations directly to actions.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Planning-Guided Data Synthesis", "weight": 1.0} -->

Our method relies on efficient model-based planning. In this section, we first review a rapidly exploring random tree (RRT)-based planner proposed, which we summarize in Algorithm. In Section III, we present task-specific planner modifications as we show this RRT-based planner creates high-entropy data when used for expert demonstration, leading to poor policy performance.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A1 Planning through contact", "weight": 1.0} -->

To allow efficient planning, the planner follows a quasi-dynamic formulation proposed, where the effect of velocity and acceleration is assumed to be negligible. Hence, the system state $\mathbf{s} \equiv \mathbf{q}$ simply consists of the robot joint positions $\mathbf{q}^{rbt} \in {\mathbb{R}}^{n_{rbt}}$ and the object pose $\mathbf{q}^{obj}$, either in ${\mathbb{S}}{\mathbb{E}}{}$ or ${\mathbb{S}}{\mathbb{E}}{}$ depending on the task. The action $\mathbf{a}$ represents the joint position commands that will be tracked by a PD controller.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A1 Planning through contact", "weight": 1.0} -->

1 Input: q0 = [q0rbt, q0obj], qgoalobj, pgrasp
4 while qobj ≠ qgoalobj do
11 qsubgoalrbt ← SampleGrasp(qsubgoalobj)
17 qnearest ← Nearest(qsubgoal)
21 qnew, a ← PlanContact(qnearest,qsubgoal)
23 𝒯.addEdge(qnearest,a,qnew)
Algorithm 1 Contact RRT

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A1 Planning through contact", "weight": 1.0} -->

Given the initial robot configuration $\mathbf{q}_{0}^{rbt}$, the object pose $\mathbf{q}_{0}^{obj}$, and the goal object pose $\mathbf{q}_{goal}^{obj}$, the planner switches between sampling a new grasp at the given object pose or sampling an object pose that is reached by solving an inverse dynamics problem. Specifically, given a system state $\mathbf{s} \equiv \mathbf{q} = {\lbrack\mathbf{q}^{obj},\mathbf{q}^{rbt}\rbrack}$, $\text{PlanContact}{(\mathbf{q},\mathbf{q}_{des})}$ solves for an action $\mathbf{a}$ to bring the object closer to a desired pose $\mathbf{q}_{des}^{obj}$ by solving the following optimization problem

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A1 Planning through contact", "weight": 1.0} -->

where $f{( \cdot, \cdot )}$ denotes the system dynamics and $g{( \cdot, \cdot )}$ the state and action bounds such as object pose limits and robot joint limits. The contact dynamics in $f{( \cdot, \cdot )}$ is smoothed and approximated as linear around an appropriately-chosen nominal point and within a convex trust region around the point such that Problem can be solved efficiently using convex optimization. In the case of sampling a new grasp, the planner randomly picks an existing node in the tree and replace the robot configuration with the newly sampled grasp. This new node will be directly added to the tree as we assume the system is always in static equilibrium and the new grasp can be reached by a collision-free planner while the object pose remains unchanged. Once the tree reaches proximity to the goal configuration, it is straightforward to find a shortest path from the root node to the goal.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-A2 Simulation Rollout", "weight": 1.0} -->

Note that we use smoothed contact model in our planner and assume the system to be quasi-dynamic. Such simplifications create discrepancies between the plan and its rollout under second-order dynamics, whether in a full physics simulator or the real world. As such, naively imitating the plan could lead to a policy that deviates from the intended goal. Therefore, we execute the plan in a physics simulator without contact smoothing to obtain the demonstrations. Note that simply executing the entire plan in an open-loop fashion by commanding the planned robot joint angles may lead to a large deviation of the object pose from the plan. We thus rollout the plan in smaller chunks. At the beginning of each chunk, we reset the system state to the planned one. These chunks naturally arise from the fact that a contact-rich plan can be divided into contact segments and collision-free segments where the robot makes a regrasp and establishes new contacts. A chunk consists of a contact segment and the contiguous collision-free segment. During training, each chunk is treated as a standalone demonstration to avoid discontinuity caused by the state reset.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B Goal-Conditioned Behavior Cloning", "weight": 1.0} -->

We cast the policy learning problem within the framework of goal-conditioned imitation learning (GCIL). The goal $\mathbf{g} \in {{\mathbb{S}}{\mathbb{E}}{}}$ or ${\mathbb{S}}{\mathbb{E}}{}$ is specified by a desired object pose. To address the potential non-Markovianity in our system, we consider a policy that takes as input a history of states $\mathbf{O}_{t} \equiv \mathbf{s}_{{t - h_{o}}:t}$. We also output a sequence of actions $\mathbf{A}_{t} \equiv \mathbf{a}_{t:{t + h_{a}}}$ instead of a single-step action, which has been shown to promote action consistency and reduce compounding errors.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B Goal-Conditioned Behavior Cloning", "weight": 1.0} -->

Note that the demonstrations can be multi-modal as the task can be achieved in more than one way. To model such multi-modal data, we choose Denoising Diffusion Probabilistic Model (DDPM) to be the action head of the policy, as prior work has demonstrated its ability to capture multi-modal distributions. At training time, a denoising network $\epsilon_{\mathbf{θ}}{({\mathbf{A}_{t} + \mathbf{\epsilon}_{k}},\mathbf{O}_{t},\mathbf{g},k)}$ represented by a 1D U-Net learns to predict a Gaussian noise $\mathbf{\epsilon}_{k}$ at different variance levels $k$ from a corrupted sample $\mathbf{A}_{t} + \mathbf{\epsilon}_{k}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B Goal-Conditioned Behavior Cloning", "weight": 1.0} -->

The denoising network is trained with the loss ${MSE{(\mathbf{\epsilon}_{k},{\epsilon_{\mathbf{θ}}{({\mathbf{A}_{t} + \mathbf{\epsilon}_{k}},\mathbf{O}_{t},\mathbf{g},k)}})}}.$ Following, we use Feature-wise Linear Modulation (FiLM) for observation and goal conditioning. As shown in Fig., the observation history and the goal embeddings are fused by a cross-attention block before being fed to the FiLM layer. The encoder is a simple Multilayer Perceptron (MLP).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Data Curation and Planner Modifications", "weight": 1.0} -->

In this section, we take a closer look at how the design choices made to the planning algorithm can significantly impact the policy performance. Recent research emphasizes the importance of low action entropy in expert demonstrations for imitation learning (IL), particularly in low-data regimes. Even with highly expressive models such as diffusion policy, accurately matching the expert distribution becomes challenging when demonstrations have high variability at rarely visited states, as there are insufficient training data to resolve the underlying action distribution. As we will show, despite its widespread success in robot motion planning, RRT exhibits this exact unfavorable property when used for generating expert demonstrations. This insight motivates modifications to our planning framework that prioritizes demonstration consistency over planning completeness, which yield data better suited for policy learning.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Data Curation and Planner Modifications", "weight": 1.0} -->

To illustrate these data generation challenges, we now examine our manipulation tasks and the data curation process in further detail.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Bimanual Manipulation", "weight": 1.0} -->

In the task IiwaBimanual, the manipuland is a cylinder with a height of $0.3\ {m\text{/}}$ and a diameter of $0.6\ {m\text{/}}$. As this is a planar task, we model the object pose by its position in the $xy$-plane and its yaw angle, i.e. $\mathbf{q}^{obj} \equiv {\lbrack x,y,\theta\rbrack}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-A Bimanual Manipulation", "weight": 1.0} -->

The task is to rotate the object by $180\ {{^\circ}\text{/}}$ from the initial orientation of $\theta_{0} = {0\ {{^\circ}\text{/}}}$ and a random initial position to a fixed goal pose $\mathbf{q}_{goal}^{obj} = {\lbrack{0.65\ {m\text{/}}},{0\ {m\text{/}}},{180\ {{^\circ}\text{/}}}\rbrack}$. We select a large goal orientation of $180\ {{^\circ}\text{/}}$ to ensure the robots would encounter joint limits during the task, necessitating regrasping to rotate the object to the desired pose.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Random initialization", "weight": 1.0} -->

When generating the demonstrations, we initialize the object position uniformly inside a ${0.4\ {m\text{/}}} \times {0.7\ {m\text{/}}}$ region centered at the goal position and sample a random robot configuration that does not collide with the object.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Training parameters", "weight": 1.0} -->

The networks are trained using AdamW at a learning rate of $1 \times 10^{- 4}$ for $50$ epochs with a batch size of $256$ samples. We use a cosine learning rate scheduler and adopt exponential moving average of weights to improve training stability as typically practiced for training diffusion models. The number of diffusion denoising steps is set to $100$ during training and $20$ for inference.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Success criteria", "weight": 1.0} -->

The task is considered successful when the position error is less than $0.1\ {m\text{/}}$ and the orientation error is less than $0.2\ {{rad}\text{/}}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A1 Planner design", "weight": 1.0} -->

While the RRT-based planner presented in II-A efficiently solves contact-rich manipulation tasks such as IiwaBimanual, it is worth noting that the planner samples subgoals at each tree expansion. We hypothesize this sampling strategy leads to a high-entropy action distribution that is more difficult to learn, especially in the low-data regime. To verify our hypothesis, we design a greedy planner as described in Algorithm to generate more consistent demonstrations. This greedy planner iteratively solves Problem without sampling subgoals for the object pose. While it still samples the grasp, it only does so when the joint limits are reached.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A1 Planner design", "weight": 1.0} -->

1 Input: q0rbt, q0obj, qgoalobj
3 qrbt ← q0rbt, qobj ← q0obj, P ← list
4 while qobj ≠ qgoalobj do
5 qrbt ← SampleGrasp(qobj)
6 while qrbt not at joint limit and qobj ≠ qgoalobj do
Algorithm 2 Greedy Search

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-A2 Performance analysis", "weight": 1.0} -->

To investigate how the action entropy affects the policy performance. We generate datasets of different sizes that respectively contain $100$, $500$, $1000$, and $5000$ demonstrations using the RRT-based planner and the greedy planner. Since we do not have access to the distribution $p{(\left. \mathbf{a} \middle| {\mathbf{O},\mathbf{g}} \right.)}$, directly calculating its entropy is challenging. Instead, we characterize the action entropy by measuring the action's effect from a few aspects.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-A2 Performance analysis", "weight": 1.0} -->

Object velocity direction We measure the entropy of the discretized object velocity direction. For linear velocity, we divide the $xy$-plane into $B = 16$ equal sub-quadrants and assign the linear velocity direction to one of these sub-quadrants. For angular velocity, we assign the movement into three discrete classes: clockwise rotation, counter-clockwise rotation, and no rotation. Moreover, instead of calculating the entropy over the entire state space, we focus only on the $xy$-plane and discretize it into a grid where each cell measures ${0.05\ {m\text{/}}} \times {0.05\ {m\text{/}}}$. We obtain the velocity direction by calculating the position and orientation differences between $h_{a} = 60$ steps, where $h_{a}$ is the length of the action sequences predicted by the policy. The probability $p_{b}$ is calculated by counting the frequencies of the velocities falling into each sub-quadrants at each cell on the $xy$-plane.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-A2 Performance analysis", "weight": 1.0} -->

Progress towards the goal Additionally, we introduce an interesting quantity to characterize the behavior of the planners. Consider a segment between two consecutive regrasps, we calculate how much progress the planner has made in terms of a weighted distance to the goal ${D{(q,q_{goal})}} = {{\parallel{p_{goal} - p}\parallel} + {0.2{\parallel{\log{({R^{\mathsf{T}}R_{goal}})}}\parallel}}}$, where the object pose $q = {(p,R)}$ is expressed as the translation vector $p$ and the rotation matrix $R$. The progress is then defined by the difference between the initial and the final weighted distance to goal of that segment.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-A2 Performance analysis", "weight": 1.0} -->

Regrasp Finally, a particularly important aspect to consider for contact-rich manipulation skills is the regrasp event, where the robot breaks current contacts and establish new contacts. Intuitively, we prefer regrasps to occur at similar phases and occur less frequently, such that each of them has more samples to learn, as contact-switch is a much more complex phenomenon than collision-free movement. To visualize the regrasp entropy, we normalize the demonstration completion time to $\lbrack 0,1\rbrack$ and discretize it into $25$ intervals; for each interval, we calculate the entropy for the Bernouli event "the robot made a regrasp", hence $B = 2$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-A2 Performance analysis", "weight": 1.0} -->

Fig. a shows the plot of the object velocity direction entropy for the IiwaBimanual (IB) task. The RRT-based planner has higher entropy in most of the positions than the greedy planner. Fig. c shows the histogram of the per-contact-segment progress towards the goal. Typically, a demonstration consists of \\qtyrange510 contact segments. Having a more spread-out distribution, the RRT-based planner exhibits consistently higher entropy. Interestingly, for the IiwaBimanual task, the RRT-based planner occasionally makes negative progress, moving away from the goal. This is not surprising as RRT samples subgoals stochastically. Furthermore, the bar plots in Fig. a and b shows that the regrasp entropy of the RRT-based planner stays close to 1 most of the time for the IiwaBimanual task, suggesting that a regrasp can take place with a probability of approximately $50\%$. To further illustrate the difference between the two planners, we show example demonstration trajectories generated by them in Fig..

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-A2 Performance analysis", "weight": 1.0} -->

Table I shows the policy performance measured by the task success rate for $100$ random initial object positions. The randomization range is slightly shrunken to a ${0.3\ {m\text{/}}} \times {0.6\ {m\text{/}}}$ region centered at the goal at test time such that the training set has a broader coverage to handle edge cases that arise at the boundary of the workspace. Using the same training parameters and network architecture, the policy trained on the data generated by the greedy planner significantly outperforms the one trained on RRT-generated data. Indeed, it reaches near perfect success rate given only $100$ demonstrations. The performance gap decreases as we further scale the dataset size, but the policy trained on the RRT-generated data plateaus around $85\%$ success rate. Interestingly, the state coverage of the RRT-based planner is slightly better than the greedy planner, which is not surprising given its property of probabilistic completeness. However, the performance gap suggests that the relationship between state coverage and policy performance is more nuanced than commonly believed, a finding that aligns with the analysis presented.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-B In-Hand Re-Orientation", "weight": 1.0} -->

With the insights gained from the IiwaBimanual task, we now consider a more complex task: 3D in-hand cube reorientation using a 16-DoF Allegro hand. The length of the cube is $6\ {{cm}\text{/}}$. The object pose $\mathbf{q}^{obj} \in {{\mathbb{S}}{\mathbb{E}}{}}$ is represented by the flattened homogeneous transformation matrix with the last row omitted. The goal is specified as the relative transformation between the current and the desired object pose.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-B In-Hand Re-Orientation", "weight": 1.0} -->

AllegroHand-Easy where the goal object orientation is constructed by first randomly selecting one of the $24$ cube rotational symmetries (hence the RPY angles are multiples of $90\ {{^\circ}\text{/}}$) which we will term as the *canonical* orientations, and then rotating it by a random yaw angle between -$45\ {{^\circ}\text{/}}$ and $45\ {{^\circ}\text{/}}$. This variant is easier because all four corners of the bottom face of the cube are in contact with the palm at the goal pose, which reduces the possibility of slipping.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-B In-Hand Re-Orientation", "weight": 1.0} -->

AllegroHand-Hard where the goal object orientation is uniformly sampled from ${\mathbb{S}}{\mathbb{O}}{}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-B In-Hand Re-Orientation", "weight": 1.0} -->

In both task variants, the goal position is a predefined nominal position located approximately at the center of the palm.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-B1 Planner modifications", "weight": 1.0} -->

Drawing from our previous analysis, we now consider how to generate more consistent demonstrations with low action entropy for this task. Although the greedy planner performs well for a planar task, the AllegroHand task needs to search through a much higher-dimensional configuration space with more challenging configuration-space obstacles. Therefore, a greedy search strategy will struggle to find a path to the goal. However, exploring the state space in an RRT fashion has its own challenges: it not only produces demonstrations with high action entropy as our analysis revealed, but also suffers from inefficiency in high-dimensional space.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-B1 Planner modifications", "weight": 1.0} -->

As neither RRT nor greedy search can generate demonstrations effective for BC, we adopt a new global contact planner proposed. This planner ensures both completeness and consistency by constructing a sparse Probabilistic Roadmap (PRM) and reusing it for all queries. Specifically, the roadmap includes all canonical orientations as nodes. Furthermore, it can be shown by Monte Carlo estimation that any orientation in ${\mathbb{S}}{\mathbb{O}}{}$ lies within $63\ {{^\circ}\text{/}}$ of a canonical orientation. Hence, given any start and goal orientation, the planner can first find their respective nearest canonical orientations and then traverse through all other canonical orientations to connect the start and goal configuration.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-B1 Planner modifications", "weight": 1.0} -->

The $24$ canonical orientations form a graph that can be connected by three simple primitives 1.: $90\ {{^\circ}\text{/}}$ rotation about the world pitch axis, 2.: $45\ {{^\circ}\text{/}}$ rotation about the world yaw axis, and 3.: -$45\ {{^\circ}\text{/}}$ rotation about the world yaw axis. These primitives are constructed by solving Problem iteratively. The planner also pre-computes a fixed set of grasps for the canonical orientations as opposed to sampling them from all feasible ones. Constraining grasps to a pre-computed set and using fixed primitives reduce the variability inherent in sampling, but still maintains solution diversity through multiple possible shortest paths in the graph.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-B1 Planner modifications", "weight": 1.0} -->

In summary, the planner creates a PRM where canonical orientations and their associated grasps form nodes, connected by pre-computed primitives. During planning, start and goal configurations are connected to this graph through solving Problem and finding the optimal path through the graph using Dijkstra's algorithm.

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-B1 Planner modifications", "weight": 1.0} -->

To compare the behavior of the RRT-based planner with the PRM-based planner, we design a simplified task AllegroHand-Yaw: rotating the object in-hand by $180\ {{^\circ}\text{/}}$ along the yaw axis, which is similar to the IiwaBimanual task. We make this simplification because effectively characterizing velocity entropy for objects in ${\mathbb{S}}{\mathbb{E}}{}$ is challenging. In particular, Fig. b, Fig. and Fig. d-f show similar results to the IiwaBimanual task, suggesting that RRT-based planner produces significantly higher-entropy data.

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-B2 Data split", "weight": 1.0} -->

We collect $1000$ demonstrations of rotating the cube to a uniformly sampled goal orientation in ${\mathbb{S}}{\mathbb{O}}{}$. The demonstration always starts from an open-hand configuration with the cube placed at randomly selected canonical orientation, then perturbed by a random translation between $- {3\ {{cm}\text{/}}}$ and $3\ {{cm}\text{/}}$ and a random yaw rotation between $- {45\ {{^\circ}\text{/}}}$ and $45\ {{^\circ}\text{/}}$. We additionally collect $5000$ demonstrations where the cube is rotated from a canonical orientation by an angle between $0\ {{^\circ}\text{/}}$ and $63\ {{^\circ}\text{/}}$ about a uniformly randomly sampled axis, representing the actions required to bring the object to the goal from the nearest canonical orientation. This dataset split addresses the imbalance in our demonstrations.

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-B2 Data split", "weight": 1.0} -->

As described previously, the majority of demonstrations consist of pre-computed actions that rotate the cube between canonical orientations. However, the final sequence of actions---rotating the cube from the nearest canonical orientation to the goal---varies significantly. This variable portion requires substantially more training samples to learn effectively.

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-B3 Hybrid policy", "weight": 1.0} -->

To further mitigate the difficulty caused by the dataset imbalance, we implement a hybrid policy approach using two components: 1. a main policy trained on $1000$ demonstrations reaching arbitrary goals from perturbed canonical orientations, and 2. an adjustment policy trained specifically on the $5000$ demonstrations focusing on final orientation adjustments. At deployment, when the cube reaches the canonical orientation nearest to the goal, we command the hand to an open-hand configuration and then activate the adjustment policy. In our experiments, this hybrid policy strategy improves success rate by about $10\%$ in simulation compared to a unified policy trained on all $6000$ demonstrations.

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-B3 Hybrid policy", "weight": 1.0} -->

Interestingly, we note that the training parameters for the AllegroHand tasks are kept the ssame as the ones for IiwaBimanual, suggesting that diffusion policy are not sensitive to hyper parameters tuning, which is consistent with the findings from prior work.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Experiments", "weight": 1.0} -->

Can we learn a policy for contact-rich manipulation from model-based planners?

<!-- chunk {"id": "body-0054", "role": "body", "section": "Experiments", "weight": 1.0} -->

Can we zero-shot transfer the learned policy to hardware?

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-A Evaluation Metric", "weight": 1.0} -->

We consider the following metrics to evaluate the performance of the policy 1. Orientation error: The orientation error is measured by the difference between the intended and the actual orientation of the object at the terminal step, measured by the norm of the relative axis angle. 2. Position errorThe position error is measured by the $l_{2}$-norm of the difference between the intended and the actual position of the object at the terminal step. 3. Task success rateThe error threshold for task success is $10\ {{cm}\text{/}}$ in position and $0.2\ {{rad}\text{/}}$ ($11.5\ {{^\circ}\text{/}}$) in orientation for IiwaBimanual and $3\ {{cm}\text{/}}$ in position and $0.4\ {{rad}\text{/}}$ ($23.0\ {{^\circ}\text{/}}$) in orientation for AllegroHand.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-B Experiment Setup", "weight": 1.0} -->

The observation history horizon $h_{o}$ is $10$ and $3$ steps for the AllegroHand and IiwaBimanual tasks respectively, and the action horizon $h_{a}$ is $40$ and $60$ steps respectively; for the AllegroHand task, each step takes $0.05\ {s\text{/}}$ and for the IiwaBimanual tasks $0.1\ {s\text{/}}$, which is the same as the discretization step length for the training data. We choose a relatively long action prediction horizon because we observe jerky motions when the prediction horizon is short, potentially due to the policy switching between different modes of the action distribution. This can be mitigated by warm-starting the inference with the previous action prediction, which we leave for future work.

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-C Simulation Evaluation", "weight": 1.0} -->

We evaluate the tasks in simulation using the best performing checkpoint during training. We execute the policy from $100$ random initial object poses and report the success rate along with the error mean and standard deviation in Table II(a). Error metrics are calculated in two ways: across all trials, and separately for successful trials only, as some failure cases (e.g., when the object falls off the table or the hand) might result in large errors, and the statistics could be skewed by these outliers.

<!-- chunk {"id": "body-0058", "role": "body", "section": "*AllegroHand*", "weight": 1.0} -->

As described in Section III-B3, we adopt a hybrid policy strategy for the AllegroHand task, as we observe it improves the success rate for both AllegroHand-Easy and AllegroHand-Hard compared to the unified policy trained on all demonstrations. We believe this performance gap is caused by the data imbalance in our dataset. While we overweight the fine adjustment demonstrations ($5000$ vs. $1000$) in our dataset when training the unified policy, determining the optimal data mixture ratio remains a complex challenge that exceeds the scope of this work. For both unified and hybrid policies, one of the most common failure modes we observe is the policy fails to react to out-of-distribution scenarios not present in training data. This is unsurprising given our use of pre-computed primitives in the demonstrations. While techniques like DAgger could potentially address these failures through data augmentation with corrective behaviors, our planner is currently unable to find solutions from arbitrary system configurations, making it difficult to apply DAgger.

<!-- chunk {"id": "body-0059", "role": "body", "section": "*IiwaBimanual*", "weight": 1.0} -->

The policy for IiwaBimanual is trained on $100$ demonstrations generated by the greedy planner. While the policy has high success rate in simulation, we do occasionally see chattering-like behaviors where the policy switches between different action modes, hence clockwise and counter-clockwise rotations. As a result, the policy often takes longer than necessary to complete the task.

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-D Hardware Evaluation", "weight": 1.0} -->

For hardware experiments, we use an OptiTrack motion capture system to provide the object pose. Table. II(b) shows the error metrics for the hardware experiments.

<!-- chunk {"id": "body-0061", "role": "body", "section": "*AllegroHand*", "weight": 1.0} -->

For hardware evaluations of the AllegroHand task, we adopt the hybrid policy strategy. We place the cube at the center of the palm with an initial orientation close to the identity at the beginning of each evaluation. To make sure the goals are spread out across ${\mathbb{S}}{\mathbb{O}}{}$, we generate goal orientations by applying random rotational perturbations to the $24$ canonical orientations. For AllegroHand-Easy, we add a random yaw rotation within the range $\lbrack{- {45\ {{^\circ}\text{/}}}},{45\ {{^\circ}\text{/}}}\rbrack$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "*AllegroHand*", "weight": 1.0} -->

For AllegroHand-Hard, we sample the perturbation using the axis-angle representation, where the rotation angle ranges from $0\ {{^\circ}\text{/}}$ to $63\ {{^\circ}\text{/}}$ about a random 3D unit vector axis (recall that any element in ${\mathbb{S}}{\mathbb{O}}{}$ can be reached this way). For both task variants, $15$ out of $24$ trials are successful, representing a $62.5\%$ success rate. Hence, the success rate for AllegroHand-Hard is comparable with simulation while AllegroHand-Easy sees some performance degradation. The most common failure mode occurs when the object lands in configurations not present in training data, leaving the policy unable to recover. While this failure mode exists in simulation, it occurs more frequently on hardware, likely due to the sim-to-real gap. Interestingly, we observe the policy sometimes taking a long action sequence to reach canonical orientations that could have been achieved with fewer primitives.

<!-- chunk {"id": "body-0063", "role": "body", "section": "*AllegroHand*", "weight": 1.0} -->

We hypothesize this is due to the network incorrectly interpolating between goals in the training data.

<!-- chunk {"id": "body-0064", "role": "body", "section": "*IiwaBimanual*", "weight": 1.0} -->

We execute the policy with the object placed at $20$ initial positions; $18$ out of $20$ trials are successful, representing a $90\%$ success rate. The failure cases occur when the initial object position is placed at the boundary of the training data distribution, and the orientation error for the failed trials are around $15\ {{^\circ}\text{/}}$, only slightly above the error threshold. We note that our real-world setup has a slight model mismatch from the simulation. For example, the mass of the object is $1.25\ {{kg}\text{/}}$, but in simulation, we set it to be $1.0\ {{kg}\text{/}}$; the object shape is not perfectly cylindrical and measures only $0.59\ {m\text{/}}$ in diameter instead of the $0.6\ {m\text{/}}$ in simulation. We further note that we do not domain randomize parameters such as the geometry of the object and the robot or the friction coefficients during training or data generation.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we demonstrate that model-based motion planning offers a compelling alternative to human teleoperation for generating training data for contact-rich manipulation tasks. This approach eliminates the bottleneck of manual data collection while enabling the generation of demonstrations for complex tasks that are challenging to demonstrate through current teleoperation interfaces, such as those involving full-arm contacts and multi-finger coordination.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Conclusion", "weight": 1.5} -->

However, our analysis reveals an important nuance: the effectiveness of learning from planned demonstrations heavily depends on how we design the planning algorithm. While popular sampling-based planners like RRT excel at global planning, they can generate demonstrations with high action entropy that are difficult to learn, especially in low-data regimes. This insight motivates us to modify our data generation pipeline to prioritize demonstration consistency while maintaining adequate state space coverage and solution diversity. Our empirical results show that policies trained on more consistent demonstrations significantly outperform those trained on data from standard RRT planners. By combining careful planner design with diffusion-based generative modeling, our approach successfully learns challenging contact-rich manipulation skills that can be zero-shot transferred to hardware. These results suggest that model-based planning is indeed a valuable tool for scaling up BC beyond simple gripper-based tasks. Nevertheless, we acknowledge that generating data entirely from simulation comes with its own limitations. For example, contact interactions between non-rigid objects cannot yet be realistically simulated or effectively planned, making it difficult to apply our approach to soft hands or deformable objects. This may be addressed by using simulated data for pre-training and real-world data for post-training, which we leave for future work.
