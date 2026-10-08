<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SkipVLA: Skipping VLA Steps with Classical Planning for Fast Robot Manipulation

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Vision-Language-Action (VLA) models are a class of generalist robot policies that map camera images and language instructions directly to robot actions. While promising, these models remain slow at test time, particularly for long-horizon tasks that require many queries to the policy. Recent efforts reduce VLA latency by distilling smaller models, overlapping asynchronous action chunks, or pairing the VLA with a fast low-level policy, but still run a learned policy for the entire task. In contrast to VLA, classical motion planners quickly find collision-free motions, but require an explicit goal and have no semantic understanding of the task. In this work, we present SkipVLA, a hybrid policy that combines a pretrained VLA with a classical motion planner, using the planner for free-space motion and querying the VLA only for contact-rich skills such as grasping and placing. SkipVLA reuses the frozen vision-language backbone of the VLA to predict a target pose for each planned motion, and learns this predictor without additional demonstrations introduced into the system by using what was already learnt by the large VLA.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We evaluate SkipVLA with three VLAs on 13 LIBERO tasks in simulation and three pick-and-place tasks on a physical 6-DoF YAM arm, demonstrating up to 2.5x faster task completion and significantly lower energy consumption while achieving the same task success rate.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Vision-Language-Action (VLA) models have emerged as a promising approach for generalist robot manipulation. By pairing pretrained vision-language backbones with expressive action heads, VLAs map raw camera observations and natural-language task instructions directly to robot actions. This unified formulation enables open-vocabulary instruction following, cross-scene generalization, and long-horizon task execution without handcrafted heuristics.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite their expressive capability, VLAs face a severe practical limitation: high inference latency. Generating each action chunk requires forward passes through multi-billion-parameter networks, resulting in latencies that far exceed the robot's control cycle. In long-horizon tasks requiring dozens or hundreds of queries, this overhead leads to sluggish execution, high energy consumption on edge compute platforms, and compromised reactive safety.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prior work to reduce VLA latency typically distills smaller models, overlaps asynchronous action chunks, or pairs the VLA with a fast low-level policy in a hierarchical setup. However, each introduces notable trade-offs: distilled models frequently suffer performance degradation; asynchronous chunking risks executing stale actions that push the policy out of distribution; and hierarchical setups require training a completely new policy network from scratch for specialized subtasks. Crucially, all of these methods treat manipulation as a monolithic end-to-end learning problem, querying large neural networks even during simple, unconstrained motions.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In reality, manipulation tasks exhibit a natural physical decomposition: they alternate between short, *contact-rich manipulation* skills (e.g., grasping, reorienting, or placing) and long stretches of *free-space transit* (e.g., reaching toward an object or navigating to a receptacle). Contact-rich manipulation requires adaptive, closed-loop visuomotor feedback to manage complex physical contacts, a domain where learned VLAs excel. In contrast, free-space transit is a purely geometric and kinematic problem that requires collision avoidance but minimal semantic reasoning.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Classical motion planners, such as sampling-based algorithms and trajectory optimizers, solve this geometric problem rapidly, generating collision-free trajectories in microseconds to milliseconds with formal safety guarantees. However, classical planners are semantically blind, i.e., they require explicit goal poses and cannot infer them from natural language. Methods that prompt foundation models for zero-shot spatial keypoints and only rely on geometric optimization for the entire task struggle with the delicate contact dynamics that VLAs naturally handle.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

This motivates a hybrid architecture that reserves the VLA for contact-rich interactions, offloads free-space transit to a fast classical planner, and uses the VLA's frozen representations to predict the planner's target poses.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To this end, we introduce SkipVLA, a modular hybrid policy that dynamically interleaves a pretrained VLA with a classical motion planner. SkipVLA scores candidate 3D object bounding boxes, conditioned on the base VLA's frozen vision-language features, to determine collision-free hover targets. A classical planner navigates the robot through free space to the target pose, then hands control to the VLA for contact-rich manipulation. Once the manipulation completes as signaled by a gripper state transition, control returns to the planner. We train the target predictor using self-supervision extracted from existing demonstration trajectories at gripper events, requiring no manual annotations, architectural changes, or policy retraining. Our main contributions are: We present SkipVLA, a plug-and-play framework that accelerates manipulation by routing free-space transit to classical motion planners and reserving pretrained VLAs solely for contact-rich skills.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop a lightweight scoring head that uses the VLA's frozen vision-language tokens to predict 3D target poses and can be trained on an existing imitation learning dataset with no additional annotation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate SkipVLA across 13 tasks on the LIBERO benchmark in simulation and three physical tasks on a 6-DoF YAM arm, spanning three distinct VLA backbones ($\pi_{0.5}$, SmolVLA, and MolmoAct2) and multiple motion planners (VAMP and cuRoboV2).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

SkipVLA achieves up to a $2.5\times$ wall-clock speedup ($59.6\%$ latency reduction) and cuts compute energy by over $52\%$ on an NVIDIA Jetson Thor.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Method", "weight": 1.0} -->

We propose SkipVLA which augments a generalist VLA policy $\pi^{\text{vla}}$ with a lightweight, low-latency classical control module $\pi^{\text{fast}}$ ($\Delta t_{\text{lat}}^{\text{fast}}\ll\Delta t_{\text{lat}}^{\text{vla}}$). It dynamically routes between classical motion planning (for free-space transit) and a VLA (for contact-rich manipulation) (see Fig. 2).

<!-- chunk {"id": "body-0015", "role": "body", "section": "IV-A Problem Formulation and Objective", "weight": 1.0} -->

We achieve this hybrid execution through an indicator module $I$ that determines which policy to execute at each timestep. Given an observation $\mathcal{O}_{s}$, task instruction $L$, and proprioceptive state $\mathbf{p}_{s}$, the indicator outputs a binary decision $I_{s}\in\{0,1\}$, yielding the hybrid policy: The latency of the hybrid policy at step $s$ is expressed as: Trajectory-level objective. To keep the latency low, the $\pi^{\text{fast}}$ module is designed to be lightweight using classical motion planning. However, classical motion planners (such as RRT or PRM) generate collision-free paths that optimize geometric or kinematic criteria rather than mimicking human demonstration trajectories step by step. Consequently, a per-action imitation loss as in Eq. would incorrectly penalize such valid transit trajectories, even when they reach the destination or the target pose safely and faster.

<!-- chunk {"id": "body-0016", "role": "body", "section": "IV-A Problem Formulation and Objective", "weight": 1.0} -->

To address this, we use a trajectory-level *imitation learning* objective where, rather than matching every action, the trajectory rolled out by $\pi^{\text{hyb}}$ is constrained to pass through key *waypoints* of the expert trajectory, which ensures successful task completion. To minimize total execution time, the overall objective can be expressed as follows: where $\tau^{\text{hyb}}$ is the trajectory rolled out by $\pi^{\text{hyb}}$, $\tau^{e}$ is the corresponding expert trajectory, $\mathcal{T}(\tau^{\text{hyb}})$ is the execution time, and $\lambda>0$ is a hyper-parameter of choice. $\ell_{\text{traj}}(\tau^{\text{hyb}},\tau^{e})=0$ implies the hybrid trajectory passes through all required key waypoints, ensuring task completion.

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-A Problem Formulation and Objective", "weight": 1.0} -->

Key-waypoints extraction. The trajectory $\tau$ for completing a task can be partitioned into segments, each associated with a subtask. Broadly, these subtasks fall into two categories: *active object manipulation*, where the robot's end-effector or gripper performs grasping, reorientation, or other contact-rich interactions with the object; and *reach-and-place* (approach/placement), where the robot primarily moves its end-effector with or without a grasped object.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-A Problem Formulation and Objective", "weight": 1.0} -->

In more detail, given a trajectory $\tau$, we partition it as $\tau=[\tau^{1},\tau^{2}\cdots\tau^{n}$\], where we concatenate each segment $\tau^{j}$ corresponding to either active object manipulation or reach-and-place.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Problem Formulation and Objective", "weight": 1.0} -->

For an expert trajectory segment $\tau^{e,j}$ corresponding to active object manipulation, the matching segment $\tau^{\text{hyb},j}$ rolled out by $\pi^{\text{hyb}}$ should closely follow the expert at each step to ensure successful completion of the subgoal. On the other hand, for an expert reach-and-place segment $\tau^{e,j}$, successful completion requires the corresponding segment $\tau^{\text{hyb},j}$ to match only the initial and final end-effector poses.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A Problem Formulation and Objective", "weight": 1.0} -->

Additionally, $N_{j}=|\tau^{\text{hyb},j}|$ and $N_{j}^{e}=|\tau^{e,j}|$ indicate the lengths of the respective segments, while $d(\cdot,\cdot)$ denotes the chosen distance metric.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B Implementation Details", "weight": 1.0} -->

In this section, we detail the design of the fast control module $\pi^{\text{fast}}$ and the policy indicator module $I$. Our hybrid policy $\pi^{\text{hyb}}$ is designed to allocate tasks to the policies based on their complexity: $\pi^{\text{fast}}$ executes reach-and-place subtasks, while $\pi^{\text{vla}}$ handles active object manipulation. This division leverages the fact that contact-rich manipulation demands expressive, learned visuomotor control, whereas free-space transit is purely geometric and can be completed significantly faster using classical motion planning.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B Implementation Details", "weight": 1.0} -->

Fast control module $\pi^{\text{fast}}$. The fast control module $\pi^{\text{fast}}$ is composed of two key components: a *target pose predictor* $f_{\text{tgt}}$ and a *low-level motion planner* $\mathcal{P}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B Implementation Details", "weight": 1.0} -->

The target pose predictor $f_{\text{tgt}}$ maps the current observation $\mathcal{O}_{s}$, language instruction $L$, and current proprioceptive state $\mathbf{p}_{s}$ to the target end-effector pose at the end of the current subtask (trajectory segment), denoted by $\mathbf{p}^{\text{tgt}}_{s}$ as: The low-level motion planner $\mathcal{P}$ then takes the current state $\mathbf{p}_{s}$, target pose $\mathbf{p}^{\text{tgt}}_{s}$, and current observation $\mathcal{O}_{s}$ to generate an action sequence $(a_{s},\dots,a_{s+m})$ of horizon $m$ that moves the robot from $\mathbf{p}_{s}$ to $\mathbf{p}^{\text{tgt}}_{s}$ while avoiding collisions, i.e.,

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Implementation Details", "weight": 1.0} -->

The target pose predictor identifies the relevant object for the current subtask and determines a collision-free hover pose directly above it. Specifically, from the observation $\mathcal{O}_{s}$, we first extract 3D bounding boxes $\mathcal{B}=\{\mathbf{b}_{i}\}_{i=1}^{M}$ for the objects in the scene, where $\mathbf{b}_{i}=(\mathbf{c}_{i},\mathbf{e}_{i})$ consists of 3D centroid $\mathbf{c}_{i}\in\mathbb{R}^{3}$ and 3D extents $\mathbf{e}_{i}\in\mathbb{R}^{3}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B Implementation Details", "weight": 1.0} -->

We score candidate object boxes by cross-attention between a learned positional embedding of each bounding box $\mathbf{b}_{i}$ (acting as the query) and the vision-language feature tokens extracted from the scene (acting as keys and values).

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B Implementation Details", "weight": 1.0} -->

The target object is selected via $\hat{i}=\arg\max_{i}r_{i}$, and a top-down, collision-free hover pose above candidate box $\mathbf{b}_{\hat{i}}$ is assigned as the target pose $\mathbf{p}^{\text{tgt}}_{s}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-B Implementation Details", "weight": 1.0} -->

We extract the vision-language features $\mathbf{F}_{\text{vl}}$ using the vision-language backbone of $\pi^{\text{vla}}$ to reuse its pretrained representations. Only the positional embedding $\phi_{\text{pos}}$, cross-attention projections, and the scoring MLP are trained from scratch. The target pose predictor is only called once at the beginning of every reach-and-place phase ($I=1$).

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-B Implementation Details", "weight": 1.0} -->

Low-level motion planner $\mathcal{P}$. Our framework is agnostic to the planner choice, and we instantiate $\mathcal{P}$ using classical motion planners such as cuRoboV2 and VAMP.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Implementation Details", "weight": 1.0} -->

Policy indicator module $I$. Learning task boundaries directly from visual observations is an active research area. As in this work, we focus on hybridizing the VLA with a fast motion planner; we choose an effective and fast heuristic based on gripper state and target pose proximity to indicate the task boundaries.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B Implementation Details", "weight": 1.0} -->

The policy begins in a reach-and-place phase ($I_{0}=1$), using $\pi^{\text{fast}}$ to navigate toward the target pose $\mathbf{p}^{\text{tgt}}_{s}$. Once the end-effector reaches the target ($d(\mathbf{p}_{s}^{ee},\mathbf{p}^{\text{tgt}}_{s})<\epsilon_{d}$, where $\epsilon_{d}>0$ is some tolerance threshold), control is handed over to $\pi^{\text{vla}}$ ($I_{s}=0$). Once active manipulation is complete, signaled by a toggle in the gripper state ($g_{s}\neq g_{s-1}$), the indicator switches back to $I_{s}=1$, returning control to $\pi^{\text{fast}}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B Implementation Details", "weight": 1.0} -->

Formally, let $g_{s}\in\{0,1\}$ be the binary gripper state (open or closed) at step $s$, $\mathbf{p}_{s}^{ee}$ be the end-effector pose, and $\mathbf{p}^{\text{tgt}}_{s}$ be the active target pose.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-C Training the Hybrid Architecture", "weight": 1.0} -->

Our hybrid policy design naturally simplifies the optimization in Eq. and does not require end-to-end policy optimization. First, we freeze the pretrained $\pi^{\text{vla}}$, which already handles contact-rich manipulation. Furthermore, $\mathcal{P}$ guarantees reachability to any valid goal pose with minimal latency; the reach-and-place trajectory loss in Eq. is minimized whenever the target pose $\mathbf{p}^{\text{tgt}}_{s}$ is correctly predicted. Consequently, optimizing Eq. reduces solely to training the target pose predictor $f_{\text{tgt}}$ (specifically its box-scoring head) to identify the target object.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-C Training the Hybrid Architecture", "weight": 1.0} -->

Automated data generation and training. To train the target scoring function without manual annotation, we extract supervision directly from expert demonstration trajectories. Reach-and-place segments correspond to free-space transit motions that precede an interaction. We detect the completion of each reach-and-place segment by identifying gripper events, namely any change in the gripper state across a threshold (closing to grasp or opening to release). At this gripper event, the target object or receptacle is identified by finding the bounding box closest to the robot's end-effector $\mathbf{p}^{ee}_{\text{event}}$ as: We then assign $i^{*}$ as the ground-truth target for all preceding states $\mathcal{O}_{s}$ within that reach-and-place segment.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-C Training the Hybrid Architecture", "weight": 1.0} -->

For any observation $\mathcal{O}_{s}$, given candidate bounding boxes $\mathcal{B}$ and frozen vision-language tokens $\mathbf{F}_{\text{vl}}$, the scoring head computes relevance scores $\{r_{i}\}_{i=1}^{M}$ according to Eq.. We optimize the trainable parameters of $f_{\text{tgt}}$ using a cross-entropy loss: This allows SkipVLA to learn robust target prediction across varying viewpoints throughout transit, requiring no additional data collection or manual annotations.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-C Training the Hybrid Architecture", "weight": 1.0} -->

Wall Clock Time (s) ↓ Table I: LIBERO-object Evaluation. We evaluate SkipVLA across 10 pick and place tasks in simulation. We also ablate the indicator heuristics to show the model’s adaptability. We calculate statistics over successful trials only. Bold: best; underline: second-best in each backbone block. Numbers shown as Mean ± Standard Deviation (Median).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

Our evaluation investigates whether interleaving a fast, point-to-point classical motion planner with a VLA model achieves faster execution and better compute efficiency than purely end-to-end VLA execution without compromising on task success. Specifically, our experiments aim to answer two core questions: Efficiency: Does offloading free-space transit to a classical planner significantly reduce wall-clock execution time and VLA query frequency across varying task horizons without compromising on task success?

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

Modularity: Is the framework robust to variations in the underlying planner, latent context representation, and indicator function?

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-A Simulation Experiments", "weight": 1.0} -->

On a standardized benchmark, we test for task speedup, VLA query reduction, and task completion.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-A Simulation Experiments", "weight": 1.0} -->

Task setup & benchmark. We evaluate on $13$ top-down pick-and-place tasks drawn from two suites in the LIBERO tabletop benchmark: LIBERO-Object (short-horizon, single-object manipulation) and LIBERO-10 (longer-horizon multi-object manipulation). We deliberately select tasks solvable via top-down grasps since our objective is not to stress-test complex grasp synthesis, but to isolate and measure the efficiency gains of hybrid planning. We train a lightweight multi-head cross-attention scorer with a 3-layer MLP bounding box encoder on the human teleoperation demonstrations from LIBERO using all 50 demonstrations per task, 650 demonstrations in total.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-A Simulation Experiments", "weight": 1.0} -->

Wall Clock Time (s) ↓ Table II: LIBERO-10 Evaluation. We evaluate SkipVLA across 3 pick and place tasks in simulation against 2 baselines. We also ablate the indicator heuristics to show the model’s adaptability. We calculate statistics over successful trials only. Bold: best; underline: second-best in each backbone block. Numbers shown as Mean ± Standard Deviation (Median).

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-A Simulation Experiments", "weight": 1.0} -->

Baselines & evaluation metrics. As our base VLAs, we choose $\pi_{0.5}$, a large-scale pretrained model with $3.5B$ parameters, and SmolVLA, a comparatively smaller and faster model with $0.5B$ parameters. For both of these VLAs, we use the publicly released fine-tuned weights on LIBERO. We experiment with using our SkipVLA framework on each VLA and report results using different planner algorithms, such as VAMP and cuRoboV2.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-A Simulation Experiments", "weight": 1.0} -->

For evaluation, each method is repeated across $50$ trials per task, measuring success rate (SR, %), total successful attempts ($n_{succ}$), wall-clock time (Wall s), and VLA query count (VLA q). We use a hard limit of 600 environment steps in MuJoCo as a timeout.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-A Simulation Experiments", "weight": 1.0} -->

Results. We present the results in Tab. I and Tab. II. First, we note that, regardless of the planner, SkipVLA matches the base model's performance. Across both VLA base models, SkipVLA with VAMP as the planner reduces the wall-clock time by $40\%$ and $27\%$ on LIBERO-object and LIBERO-10, respectively. We also see a proportional drop in the number of VLA queries, indicating that the time reduction is largely due to fewer VLA queries. We also note that SkipVLA shows consistent performance regardless of the planner choice. While cuRoboV2 has a slightly higher success rate, VAMP demonstrates a shorter wall-clock time.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-A Simulation Experiments", "weight": 1.0} -->

Single-Object Put red block in box Multi-Object Put red & blue in box Precision Stacking Stack tower Table III: Real-World Evaluation. We evaluate SkipVLA against two baselines in the real world on a physical 6-DoF YAM robot arm across three tasks (20 trials per task). Statistics for wall-clock time, VLA calls, and energy are calculated only from successful trials. SR higher is better; all other metrics lower is better; bold and shading mark the better value within each backbone block.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-A Simulation Experiments", "weight": 1.0} -->

Ablation of indicator heuristics. We provide ablations on the heuristics to identify the task boundary. For this ablation, we use changes in object height as an indicator of the transition between reach-and-place and active manipulation; i.e., a change beyond a threshold denotes the transition. We choose Vamp as the planner. From Tab. I and Tab. II, we observe that the height-based heuristic performs comparably to other configurations, showing the stability of SkipVLA. However, our proposed indicator heuristics with the VAMP planner yield the shortest overall wall clock time, indicating the fastest task completion.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-B Real-World Experiments", "weight": 1.0} -->

Experiment setup. To validate our method in the real world, we deployed SkipVLA on a physical 6-DoF YAM manipulator. Our method is tested against two baselines across three tasks in the real world: $\pi_{0.5}$ and MolmoAct2, each fine-tuned on 50 teleoperated demonstrations per task.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-B Real-World Experiments", "weight": 1.0} -->

We evaluate across three top-down pick-and-place tasks of increasing horizon complexity. In addition to success rate, wall-clock time, and VLA query count, we also measure the total energy consumption per trial on the NVIDIA Jetson Thor onboard compute platform. Each task is evaluated over 20 independent trials: Single-Object: Put the red block in the box (90-second timeout).

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-B Real-World Experiments", "weight": 1.0} -->

Multi-Object: Put the red and blue blocks in the box (120-second timeout).

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-B Real-World Experiments", "weight": 1.0} -->

Multi-Object with precision placing: Stack three blocks into a tower (120-second timeout).

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-B Real-World Experiments", "weight": 1.0} -->

Main results. Consistent with our simulation results, SkipVLA outperforms both $\pi_{0.5}$ and MolmoAct2 across all tasks and measured metrics, as shown in Tab. III. Specifically, SkipVLA achieves substantial reductions in execution time across all three tasks: wall-clock completion time decreases by an average of $46.0\%$ on MolmoAct2 (up to $59.6\%$, a $2.47\times$ speedup) and $30.6\%$ on $\pi_{0.5}$. Concurrently, VLA queries drop by an average of $33.8\%$ across tasks (reducing calls by over half on MolmoAct2 for single-object), confirming that offloading free-space transit bypasses a large fraction of costly policy evaluations.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-B Real-World Experiments", "weight": 1.0} -->

Crucially, these efficiency gains come with matched or strictly improved success rates on every task: SkipVLA boosts multi-object placement from $90\%$ to a perfect $100\%$ on both backbones, and raises precision stacking success by $+15.0\%$ percentage points for $\pi_{0.5}$ and $+10.0\%$ percentage points for MolmoAct2.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-B Real-World Experiments", "weight": 1.0} -->

Next, in Fig. 4 we report our real-world results as a cumulative distribution that shows the fraction of episodes solved within a given wall-clock budget. As visible from the graphs, SkipVLA encloses a larger area under the curve than its baseline counterpart on every task, demonstrating that SkipVLA reaches a higher final success rate within a substantially smaller wall-clock budget. By bypassing the base VLA during free-space transit, the hybrid policy drastically reduces the number of required queries to the generative policies and offloads the work to a lightweight, fast, and efficient CPU-based motion planner (VAMP).

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-B Real-World Experiments", "weight": 1.0} -->

Energy comparison. As shown in Tab. III, SkipVLA is also substantially more energy-efficient on the Jetson Thor compute module, cutting per-trial energy consumption by an average of $52.4\%$ on MolmoAct2 and $29.1\%$ on $\pi_{0.5}$. This confirms that our hybrid approach achieves higher physical throughput with a strictly lighter energy footprint.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-B Real-World Experiments", "weight": 1.0} -->

Additional discussion. Although SkipVLA was designed primarily to reduce inference latency by minimizing VLA queries, we observe that it also improves task success rates, such as improving SmolVLA from $39.0\%$ to $82.0\%$ on LIBERO-Object and improving real-world precision stacking by approximately $20\%$. We attribute this gain to the planners, which limit compounding errors.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-B Real-World Experiments", "weight": 1.0} -->

Imitation learning bounds a policy's error as $\epsilon$ when its state remains within the experts' distribution. During policy rollout, an out-of-distribution shift in state compounds, incurring a cost bounded by $O(\epsilon T^{2})$ over task horizon $T$. In an end-to-end VLA, a small error during free-space transit can displace the robot out of distribution before it reaches the object, causing grasp failures. SkipVLA mitigates this in two ways: first, restricting VLA queries to short active-manipulation segments of length $T_{\text{manip}}\ll T$ shrinks the time horizon over which errors compound. Second, by planning collision-free paths directly to a nominal hover pose above the object, the classical planner physically re-anchors the robot to in-distribution initial states before each active-manipulation subtask, preventing error propagation to subsequent subtasks.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-B Real-World Experiments", "weight": 1.0} -->

Lastly, SkipVLA in this work is restricted to pick-and-place tasks due to design choices that were outside the scope of this project: the indicator $I$ depends on gripper-state transitions, which assumes that every active-manipulation segment ends in a grasp or release. Future work aims to make SkipVLA generalizable across all tasks by replacing the heuristic-based indicator with a learned, task-conditioned temporal segmentation module.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We present SkipVLA, a method for accelerating pretrained VLAs by offloading free-space motion to a classical motion planner. SkipVLA uses the planner to move the robot to a predicted target pose, hands control to the VLA for contact-rich skills, and returns control to the planner when the gripper opens or closes. A lightweight scoring head on the frozen vision-language backbone of the VLA selects the target object and is trained from existing demonstrations with labels extracted from gripper events. Compared to $\pi_{0.5}$ and MolmoAct2 on a physical 6-DoF YAM arm, SkipVLA completes tasks up to 2.5x faster and uses up to less half the energy of the baseline policy, while matching or improving success rate on every task. The speedup of SkipVLA is larger for the slower MolmoAct2 than for $\pi_{0.5}$ on every task. In simulation, SkipVLA also raises the success rate of SmolVLA significantly on our LIBERO experiments, suggesting that shorter VLA segments limit compounding error.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The performance of SkipVLA demonstrates that VLAs can benefit from classical motion planning without retraining the policy.
