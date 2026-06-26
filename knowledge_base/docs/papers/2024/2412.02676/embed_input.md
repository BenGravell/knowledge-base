<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Planning-Guided Diffusion Policy Learning for Generalizable Contact-Rich Bimanual Manipulation

Topics include Diffusion policy, Bimanual manipulation, Contact-rich manipulation, Motion planning, Imitation learning, Generalization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces GLIDE, a planning-guided diffusion-policy approach for contact-rich bimanual manipulation with limited demonstrations. The central contribution is using model-based motion planning to shape diffusion-policy learning so manipulation policies generalize better across object states and task variations.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Contact-rich bimanual manipulation involves precise coordination of two arms to change object states through strategically selected contacts and motions. Due to the inherent complexity of these tasks, acquiring sufficient demonstration data and training policies that generalize to unseen scenarios remain a largely unresolved challenge. Building on recent advances in planning through contacts, we introduce Generalizable Planning-Guided Diffusion Policy Learning (GLIDE), an approach that effectively learns to solve contact-rich bimanual manipulation tasks by leveraging model-based motion planners to generate demonstration data in high-fidelity physics simulation. Through efficient planning in randomized environments, our approach generates large-scale and high-quality synthetic motion trajectories for tasks involving diverse objects and transformations. We then train a task-conditioned diffusion policy via behavior cloning using these demonstrations. To tackle the sim-to-real gap, we propose a set of essential design options in feature extraction, task representation, action prediction, and data augmentation that enable learning robust prediction of smooth action sequences and generalization to unseen scenarios. Through experiments in both simulation and the real world, we demonstrate that our approach can enable a bimanual robotic system to effectively manipulate objects of diverse geometries, dimensions, and physical properties.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

From warehouse logistics to home services, a broad range of essential robotic applications relies on manipulation involving multi-contact interactions between objects and the manipulators. For example, as shown in Fig. LABEL:fig:teaser, the task is to control two robotic arms to manipulate different objects to a specified target pose. These objects are often bulky and heavy, making them not directly graspable by the end-effectors. To rearrange and reorient the object, the two arms must hold the object robustly through contacts at multiple links, and then reorient the object over possibly long horizons that take multiple contact phases to reach the goal. Due to such inherent complexity, solving contact-rich bimanual manipulation for diverse and complex objects remains an open challenge.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To tackle this challenge, recent advances in model-based planning methods utilizing smoothed contact models have begun to demonstrate effectiveness However, such motion planners need complete knowledge of object states and environment geometry, thereby limiting their ability to operate in novel environments where objects exhibit diverse geometries and physical properties. Additionally, their computational overhead prevents them from generating trajectories online, which can be a critical limitation, especially in dynamic environments that require real-time adaptation. These limitations highlight the need for approaches that can effectively and robustly perform contact-rich bimanual manipulation over diverse objects.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Alternatively, an increasing number of works have aimed to acquire generalizable contact-rich manipulation skills by learning from trajectory data. In spite of the promising progress, key challenges remain, particularly for bimanual manipulation with complex embodiments. First, training robust, generalizable policies for complex visuomotor skills usually requires large scale, high-quality trajectory data such as expert demonstrations. However, it is particularly difficult and costly to collect demonstrations for complex systems and tasks like contact-rich bimanual manipulations using traditional approaches such as teleoperation in the real world. Second, for approaches that learn policies using simulation data, the reality gap in perception and dynamics poses notable challenges for effective policy deployment and generalization. Such challenges also become more significant as the complexity of the task increases.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose a method that learns generalizable contact-rich bimanual manipulation, specifically reorientation of bulky and heavy objects, by addressing the aforementioned challenges. Our approach, named Generalizable PLanning-GuIded Diffusion Policy LEarning (GLIDE), is built upon recent advances in diffusion policies and model-based motion planning to boost scalability for both data and model. Using a contact-implicit trajectory optimization solver, which derives its efficiency from a smoothed linear approximation of local robot-object contact dynamics, we generate massive and high-quality demonstration data for contact-rich bimanual manipulation in physics simulation. Compared to prior long-horizon motion planning methods that exhibit high computational costs, this planner significantly improves data generation efficiency with minimal impact on trajectory quality. Additionally, we implement our planner to greedily approach the goal object states, further speeding up synthetic data generation. To learn generalizable visuomotor skills for contact-rich and bimanual manipulation, we build on recent advancements in diffusion policy that effectively capture multimodal action distributions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast to, which learns a specific set of parameters for each task, we design a task-conditioned diffusion policy network that controls the robot to manipulate the object to arbitrary target poses specified by the users. To bridge the reality gap between the simulation and the real-world system, we introduce a set of essential design choices regarding feature extraction, task representation, action prediction, and data augmentation, which significantly improve our policy's performance in sim-to-real transfer. We evaluate GLIDE in a series of simulated and real-world contact-rich bimanual manipulation tasks involving both in-distribution and out-of-distribution (OOD) objects. Through detailed analysis, we demonstrate that our approach can robustly accomplish contact-rich bimanual manipulation in unseen scenarios.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Method", "weight": 1.0} -->

GLIDE centers around two key focuses: generating diverse and high-quality training data for contact-rich bimanual manipulation tasks and learning visuomotor policies that can generalize to unseen environments and task specifications.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Method", "weight": 1.0} -->

In this section, we will first describe the problem formulation for learning generalizable contact-rich bimanual manipulation. Next, we will propose a data synthesis pipeline that uses an efficient contact-rich planner. Finally, we will devise a conditional diffusion policy that generates action sequences given observed point clouds and task specifications.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-A Problem Formulation", "weight": 1.0} -->

We consider the problem of controlling a bimanual robotic system to change the pose of objects. Such objects can be bulky and heavy, and thus cannot be directly grasped by the end-effectors. To accomplish this task, the two robot arms need to strategically approach the object to make contact and then reorient the object to the target pose. For complex objects and challenging target poses, this process might take multiple rounds of approaching and manipulation due to the limitation of the configuration space of the robot. To enable generalization to unseen objects, we do not assume the shape and initial pose of the object to be known. Instead, the robot only receives visual observations of the environment.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A Problem Formulation", "weight": 1.0} -->

Formally, we define the problem with the environment state space $\mathcal{S}$, the observation space $\mathcal{O}$, the action space $\mathcal{A}$, the task space $\mathcal{C}$, and the time horizon $H$. In each episode, the robot starts at an initial environment state $s_{0} \in \mathcal{S}$ and is commanded to change the environment according to a task specification $c \in \mathcal{C}$. At each time step $t = {1,\ldots,H}$, the robot receives the observation $o_{t} \in \mathcal{O}$ and takes an action $a_{t} \in \mathcal{A}$. To solve this problem, we aim to learn a single policy $\pi_{\theta}{(\left. a \middle| {o,c} \right.)}$ with a trainable set of parameters $\theta$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A Problem Formulation", "weight": 1.0} -->

Due to the complexity of the dynamics and control in bimanual manipulation tasks, directly collecting massive and high-quality data in the real world is hard. Instead, we aim to generate synthetic demonstration data $\mathcal{D}$ to train the policy $\pi$. As no real-world training data is collected and used, we would need to design the policy network and learning algorithm such that the policy trained on $\mathcal{D}$ is transferrable to the real world at deployment.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Problem Formulation", "weight": 1.0} -->

In this work, we specifically consider a table-top environment involving two 7-DoF robotic arms without end-effectors, as shown in Fig. LABEL:fig:teaser. The policy does not know the true environment state $s_{t}$ but receives the observation $o_{t}$ as a depth image taken from a fixed RGBD camera converted into point clouds as well as the proprioceptive joint states of the robot. The target object to manipulate is supported by the table surface, and the task is defined by a transformation of the object pose in ${\mathbb{S}}{\mathbb{E}}{}$. At each time step, we compute the task specification $c_{t}$ as the transformation between the current object pose and the target pose as part of the inputs to the policy $\pi$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-B Demonstration Synthesis via Efficient Planning", "weight": 1.0} -->

To scalably generate demonstrations for our bimanual object reorientation task, we use motion planning that leverages privileged object and robot states in simulation to produce trajectories. We build upon the planning-through-contact framework in and incorporate the very recent advances in in our planning pipeline, which proposes a smoothed linear approximation of local robot-object contact dynamics that significantly improves planning efficiency.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-B Demonstration Synthesis via Efficient Planning", "weight": 1.0} -->

Our planner's input include (i) the initial state of the system, $s_{0}\operatorname{:-}{(q_{0}^{a},q_{0}^{u})}$, where $q_{0}^{a}$ is the robot joint angles and $q_{0}^{u}$ the object pose; and (ii) the goal object pose $q_{goal}^{u}$. An action $a$ consists of commanded joint angles for both arms. The planner generates a sequence of actions $T\operatorname{:-}{(a_{0},a_{1},\ldots)}$ that takes the object from the initial pose to the goal pose. Compared with with the sampling-based planner, we greedily approach the goal to speed up computation and encourage consistency in the demonstrations. The greedy approach did not significantly impact the planner's success rate in practice.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-B Demonstration Synthesis via Efficient Planning", "weight": 1.0} -->

The resulting planner, summarized in Algorithm 1, consists of the following components: A contact sampler that generates robot joint configurations $q_{\text{grasp}}^{a}$ where the robot arms make contact with the object in a way that facilitates manipulation (i.e., a "grasp"). In our implementation, we use inverse kinematics to generate grasps where the robot's distal links can stably pinch and hold the object.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-B Demonstration Synthesis via Efficient Planning", "weight": 1.0} -->

A collision-free planner using bidirectional RRT with shortcutting to plan a collision-free trajectory from the current robot joint configuration $q^{a}$ to the next grasp $q_{\text{grasp}}^{a}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B Demonstration Synthesis via Efficient Planning", "weight": 1.0} -->

A contact planner which, given a current robot configuration $q^{a}$ that is already grasping the object and the object's current configuration $q^{u}$, greedily moves the object towards the goal configuration $q_{\text{goal}}^{u}$ as much as possible while ensuring that the robot does not exceed joint limits.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Demonstration Synthesis via Efficient Planning", "weight": 1.0} -->

2 Output: Action trajectory T 10 while qa not at joint limit and qu ≠ qgoalu do Algorithm 1 Demonstration Synthesis via Planning Contact Planner Details. Much prior work has focused on trajectory optimization through contact, but their high computational costs due to long-horizon trajectory optimization and the exponential number of contact modes prohibit efficient trajectory generation. To reduce these costs, we adopt a single step variant of trajectory optimization and solve it through the approach. In short, we use a linear approximation $f_{\text{local}}$ of the local contact dynamics to solve the optimization problem with the following objective: Here, $q_{+}^{u} = {f_{\text{local}}{(q^{u},q^{a},a)}}$ denotes the object's approximate configuration after the robot action $a$ is taken, and $\mathbf{Q}$ and $\mathbf{R}$ are user-specified cost matrices.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Demonstration Synthesis via Efficient Planning", "weight": 1.0} -->

Filtered Behavior Cloning. As the collected trajectories are often suboptimal due to the approximality of the contact dynamics and the stochasticity of the RRT in the planner, directly performing behavior cloning on all trajectories leads to poor policy performance. To address this, we extract high-quality demonstrations by filtering trajectories via rollouts in a high-fidelity simulator to verify their accuracy. The trajectories in which the object doesn't reach the goal and the suboptimal trajectories that take too long to reach the goal are discarded in this process. Finally, we rebalance the trajectories to be uniformly distributed across objects and render uncolored point clouds for policy training. We save the resultant subset of demonstration trajectories as the dataset $\mathcal{D}$ to train the policy.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-C Diffusion Policy Learning from Synthetic Demonstrations", "weight": 1.0} -->

Given the synthetic demonstrations $\mathcal{D}$, we train a diffusion policy $\pi_{\theta}{(\left. a \middle| {s,c} \right.)}$ for contact-rich bimanual manipulation via behavior cloning. To enable $\pi_{\theta}$ to predict suitable manipulation actions for unseen scenarios and effectively transfer the learned knowledge to the real world, we introduce a set of essential design options to existing diffusion policy learning methods for the feature extraction, task representation, and action prediction.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-C Diffusion Policy Learning from Synthetic Demonstrations", "weight": 1.0} -->

To extract the geometric information of the environment from the noisy point cloud observations, we design a feature extraction backbone for $\pi_{\theta}$ that can facilitate generalization to unseen objects based on and. To enable generalization to unseen environments, we clip the point clouds within the robot's workspace and remove the irrelevant background objects in each frame. Additionally, to address the reality gap and sensor noise encountered in the real world, we introduce a Flying Point Augmentation approach, where we randomly add large Gaussian noise to the points with a small probability (e.g., 0.5%). We find that this approach significantly improves our policy's real-world performance while requiring minimal implementation effort.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-C Diffusion Policy Learning from Synthetic Demonstrations", "weight": 1.0} -->

While and aim to learn a predefined set of tasks using a different set of parameters for each task, we train a single policy that takes the task specification $c$ as an additional input. As described in Sec. III-A, instead of assuming the object shape is known and directly specifying a target object pose, we implicitly specify the target pose using the initial visual observation $o_{0}$ along with the delta transformation $c_{0}$ from the initial object pose in $o_{0}$ to the target object pose. In each subsequent time step $t$, we recompute the transformation $c_{t}$ from the current pose to the target pose given the current observation $o_{t}$. Without knowing the object shape and pre-defining an object frame, we propose to obtain $c_{t}$ by segmenting the target object in $o_{0}$ using an open-vocabulary segmentation algorithm, selecting keypoints using the farthest point sampling within the segmentation, and then tracking the keypoints in the 3D space through real-time object tracking.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Diffusion Policy Learning from Synthetic Demonstrations", "weight": 1.0} -->

We design the prediction head of the policy network to robustly generate smooth and feasible motion trajectories. Following, our policy predicts an action sequence of $T_{a}$ steps. We use a larger $T_{a} = 20$ at test time to improve performance and train our policy with $T_{a} = 64$. Additionally, prior work like usually directly predicts the absolute end-effector poses or joint angles as actions. However, we observe that this can result in poor generalization to unseen objects and non-smooth trajectories in the real world. To address this issue, we instead re-design the prediction head to predict the residual joint position actions $a_{{t + 1}:{t + T_{a}}} = {\{{q_{i} - q_{t}}\}}_{i = {t + 1}}^{t + T_{a}}$ with $q_{t}$ being the current joint positions at time step $t$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C Diffusion Policy Learning from Synthetic Demonstrations", "weight": 1.0} -->

Compared to absolute joint actions, the residual joint actions are much more consistent in scales and shifts across training trajectories, resulting in significantly better real-world policy performance.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experiments", "weight": 1.0} -->

We design our experiments to answer the following questions: Does GLIDE effectively perform contact-rich bimanual object manipulation on objects whose geometries, dimensions, and physical properties are within the distribution of training demonstrations? How well does GLIDE generalize to objects with challenging geometries and physical properties? How important are the design choices in GLIDE to the performance?

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-A Environments and Tasks", "weight": 1.0} -->

We perform bimanual object reorientation on a flat table using two 7-DoF KUKA LBR iiwa arms in both the Drake simulator and the real world. We use a Realsense D455 camera mounted 2 meters above the table to capture real-world visual observations, and we actuate three joints per arm following. In simulation, we synthesize planner demonstrations following our approach in Sec. III-B and then retain 12,000 successful trajectories for policy training (Sec. III-C). During both demonstration generation and policy evaluation, we randomize object assets along with their initial and goal poses. An episode is successful if the final object pose is within 10 cm and 0.2 rad of the goal. The demonstration generation process takes about two days on a 96-CPU machine.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A Environments and Tasks", "weight": 1.0} -->

For object assets used for demonstration generation and policy training, we generate 2,000 rectangular box primitives with randomized dimensions, mass, and friction coefficients. While we train our policy exclusively on box primitives, we show that it can achieve good generalization performance on objects with OOD geometries and physical properties.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B Experiment Design", "weight": 1.0} -->

Task (In-Dist Eval) Random Rotation (Easy) Random Rotation (Medium) Random Rotation (Hard) Random Rotation (Overall) Task (Real OOD Eval) TABLE I: Bimanual object reorientation success rates in both simulation and the real world for in-distribution objects. We report results for our point cloud policy and also include the planner results as a reference (note that the planner runs significantly slower than our policy and requires access to complete knowledge of object geometry, and is thus infeasible for real world deployment). For vanilla DP3 baseline results, see the last row of Tab. V and the first column of Tab. V. TABLE II: Success rates of real-world policy evaluation using out-of-distribution containers (which are visualized in Fig. 1 - Right). We evaluate our policy using both empty and overfilled containers.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B Experiment Design", "weight": 1.0} -->

To comprehensively assess GLIDE's performance in contact-rich bimanual object reorientation, we evaluate it on objects with geometries, dimensions, and physical properties within the distribution of demonstration trajectories (i.e., "In-Distribution Evaluation"). Additionally, we put GLIDE to the test and evaluate its ability to generalize to challenging, unseen objects outside of training distribution ("Out-of-Distribution (OOD) Evaluation"). Despite the perception and control challenges posed by the diverse shapes and physical properties of OOD real world objects, we hope that our policy can still effectively infer object boundaries from our processed point clouds where irrelevant backgrounds are removed, from which it can determine the necessary robot joint movements to approach and manipulate the object.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B Experiment Design", "weight": 1.0} -->

Furthermore, to enable a fine-grained analysis of GLIDE's success and limitations, we design our experiments to encompass increasing levels of task difficulty: Fixed Rotation: Let $\Delta\theta$ represent the orientation difference between the initial and goal object poses. In our "Fixed Rotation" setting, we set $\Delta\theta$ to a constant value across all demonstration and evaluation episodes (in our experiments, ${\Delta\theta} = 45^{\circ}$). Additionally, we initialize object orientations in multiples of $\frac{\pi}{2}$ (for boxes, their edges are aligned parallel to the table edges). Although simpler than the "Random Rotation" setting below, this setup is already challenging as it requires the policy to generalize to diverse objects with randomized positions.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-B Experiment Design", "weight": 1.0} -->

Random Rotation: Both $\Delta\theta$ and the initial object orientation are fully randomized. We further subdivide $\Delta\theta$ into 3 levels of difficulties (visualized in Fig. 4): Easy (${|{\Delta\theta}|} \leq 45^{\circ}$); Medium ($45 < {|{\Delta\theta}|} \leq 90^{\circ}$); Hard ($90^{\circ} < {|{\Delta\theta}|} \leq 150^{\circ}$)^11^1We set ${|{\Delta\theta}|} \leq 150^{\circ}$ as it is very challenging to generate successful demonstrations for ${|{\Delta\theta}|} > 150^{\circ}$ with our current planner.. As $|{\Delta\theta}|$ increases, it becomes more likely that the robot needs to perform multiple rounds of approaching and manipulation to reach the object to the goal orientation due to the limitation of robot's configuration space.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B Experiment Design", "weight": 1.0} -->

We generate demonstration sets for both the "Fixed Rotation" and "Random Rotation" tasks and train a diffusion policy on each. For the "Random Rotation" task, we evaluate a single policy across all three levels of task difficulty.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-C In-Distribution Evaluation", "weight": 1.0} -->

We perform in-distribution evaluation of GLIDE in both simulation and the real world. In simulation, we randomly sample boxes whose dimensions and physical properties are within our demonstration's distribution. In the real world, we randomly choose a set of everyday boxes from the same distribution, as shown in Fig. 1. We conduct 100 policy evaluation trials in simulation and 25 trials in the real world. Additionally, we include our motion planner's success rates in simulation as a reference. Note that the planner runs slower than our policy and requires access to complete knowledge of object geometry, which is infeasible for real-world evaluation. Due to the highly stochastic nature of our planner, we evaluate it over a larger number of 600 trials.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-C In-Distribution Evaluation", "weight": 1.0} -->

We present our results in Tab. II, and we include qualitative visualizations of policy rollouts in the first row of Fig. LABEL:fig:teaser and the left and middle columns of Fig. 4. Overall, GLIDE demonstrates strong performance on in-distribution objects in both simulation and the real world. Notably, by guiding diffusion policy learning through motion planning, our policy significantly improves the performance over motion planning while being much faster and does not require prior knowledge of object shapes. However, there is still significant room for improvement in the highly challenging setting where the policy must manipulate the object towards a distant target orientation over a long horizon. Later in Sec. IV-F, we will analyze these failure cases in detail and suggest directions for future improvements.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-D Out-of-Distribution (OOD) Evaluation", "weight": 1.0} -->

We evaluate GLIDE's ability to generalize to out-of-distribution objects in the real world using a set of containers shown in Fig. 1-Right. These containers differ from the rigid boxes in both geometry and physical properties: some have curved edges or a wider top than the bottom, while others are deformable, made from soft materials like rubber or fabric. We conduct 16 evaluation trials with the containers empty and another 16 trials with them overfilled with miscellaneous objects. As illustrated in the third row of Fig. LABEL:fig:teaser and the right column of Fig. 4, overfilled containers introduce irregular object boundaries and object weights heavier than those during training, adding further challenges for our policy. Results are shown in Tab. II. GLIDE demonstrates robustness and generalization to OOD shapes and object properties, with a slight performance drop compared to in-distribution evaluation in Tab. II. Notably, the success rates are similar across both empty and overfilled containers, despite their distinct geometries and weight, showcasing GLIDE's robustness in handling diverse and challenging scenarios.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-D Out-of-Distribution (OOD) Evaluation", "weight": 1.0} -->

Additionally, we evaluate GLIDE on inflatable toys as shown in Fig. 4 and the second row of Fig. LABEL:fig:teaser. These toys present even larger distribution shifts from the training objects, featuring legged bases instead of the rectangular bottoms seen in boxes and containers. Additionally, their higher center of mass makes them prone to tipping if the two robot arms do not act with precise coordination. GLIDE achieves 52% for the fixed rotation task and 28% for the random rotation task, further demonstrating its potential to adapt and generalize to challenging objects.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-E Ablations", "weight": 1.0} -->

In this section, we analyze the importance of different design choices to GLIDE's performance. In Tab. V, we ablate the residual robot joint action prediction and the flying point augmentation approaches we introduced in Sec. III-C to improve GLIDE's sim-to-real transfer. While these techniques show minimal impact in simulation, they significantly enhance policy performance in real-world evaluations. Omitting either approach results in a notable drop in real-world performance. In Tab. V, we ablate the number of action prediction steps $T_{a}$ for our diffusion policy evaluation. We find that a larger $T_{a} = 20$, compared to prior work with $T_{a} = 8$, results in smoother trajectories and better performance. However, further increasing $T_{a}$ can degrade performance due to the lack of real-time feedback, which limits the policy's ability to make timely adaptations during object manipulation. In Tab. V, we study how the number of planner-generated demonstrations impacts policy performance.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-E Ablations", "weight": 1.0} -->

We find that thousands of demonstrations are needed for good policy performance on the easier "Fixed Rotation" task, with significantly more required for the challenging "Random Rotation" task. We also find that the performance doesn't plateau as we scale up the number of demonstrations, suggesting that further scaling up demonstration generation will continue to improve policy effectiveness.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-E Ablations", "weight": 1.0} -->

Flying Point Aug Success (Sim, In-Dist) Success (Real, In-Dist) Task (Sim, In-Dist Eval) Task (Sim, In-Dist Eval) TABLE III: Ablation of different point cloud diffusion policy design choices on our fixed 45∘ clockwise object rotation task. TABLE IV: Ablation on the number of action prediction steps Ta for diffusion policy evaluation. We use Ta = 64 for training. TABLE V: Ablation on the number of expert planner demonstrations for diffusion policy learning.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-F Failure Mode Analysis", "weight": 1.0} -->

While our method demonstrates effective generalizable bimanual contact-rich manipulation, there is still room for improvement on highly challenging scenarios requiring manipulating objects to distant target orientations.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-F Failure Mode Analysis", "weight": 1.0} -->

Among 52% of failure cases in our "Random Rotation-Hard" experiments, the robot is stuck in a poor joint configuration that prevents further object rotation, as illustrated in the wrapped figure. Additionally, object slippage occurs in 20% of cases due to unstable contact, and in 16% of cases, the robot exceeds torque limits by squeezing the object too hard. To address these failure scenarios, generating demonstrations from more diverse initial states, including near-failure situations, would be a promising avenue for future work.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented GLIDE, a planning-guided diffusion policy learning method for generalizable contact-rich bimanual manipulation. Leveraging the recent advances in efficient model-based planning through contact, we generate large-scale, high-quality demonstration trajectories in simulation. We then perform visuomotor imitation learning using a task-conditioned point cloud diffusion policy, and we propose essential design choices in feature extraction, task representation, and action prediction that enable effective policy generalization to unseen scenarios and sim-to-real transfer. Evaluations in both simulation and the real-world demonstrate our policy's effectiveness in manipulating objects with diverse geometries, dimensions, and physical properties. In this paper, we have only used primitive shapes for data synthesis and demonstrated table-top manipulation tasks. Future directions include further diversifying training environments with objects from large datasets and scaling up our approach to more dexterous and dynamic tasks.
