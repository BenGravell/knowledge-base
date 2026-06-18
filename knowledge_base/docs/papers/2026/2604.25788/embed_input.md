<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning

Topics include Reinforcement learning, Imitation learning, Motion planning, Robotics, Benchmarks, Planning, Learning, KinDER.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Robotic systems that interact with the physical world must reason about kinematic and dynamic constraints imposed by their own embodiment, their environment, and the task at hand. We introduce KinDER, a benchmark for Kinematic and Dynamic Embodied Reasoning that targets physical reasoning challenges arising in robot learning and planning. KinDER comprises 25 procedurally generated environments, a Gymnasium-compatible Python library with parameterized skills and demonstrations, and a standardized evaluation suite with 13 implemented baselines spanning task and motion planning, imitation learning, reinforcement learning, and foundation-model-based approaches. The environments are designed to isolate five core physical reasoning challenges: basic spatial relations, nonprehensile multi-object manipulation, tool use, combinatorial geometric constraints, and dynamic constraints, disentangled from perception, language understanding, and application-specific complexity. Empirical evaluation shows that existing methods struggle to solve many of the environments, indicating substantial gaps in current approaches to physical reasoning. We additionally include real-to-sim-to-real experiments on a mobile manipulator to assess the correspondence between simulation and real-world physical interaction. KinDER is fully open-sourced and intended to enable systematic comparison across diverse paradigms for advancing physical reasoning in robotics.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

A central challenge in robotics that arises from embodied interaction with the real world is the need for *physical reasoning*. Broadly competent robots must be able to reason about the kinematic and dynamic limits dictated by their own morphology, the laws of physics imposed by their environment, and the task requirements specified by their users. These often-entangled constraints can turn semantically simple tasks into challenging puzzles. To store a book in a shelf, is it enough to move to the book, grasp it, move to the shelf, and place? That depends: is there a clear path to the book, or do obstacles need to be moved? Does the book need to be set down and re-grasped before a placement is feasible? Is there space in the shelf, or should the robot use its arm to gently push other books aside? The robot must not only answer these questions, but pose them in the first place---*reasoning about what to reason about* given only the available sensory observations.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the importance of physical reasoning to robotics, there is little consensus on the state of the art. Measuring physical reasoning is hard: no single task is sufficient (why not just memorize the solution?) and even procedurally-generated variations of a task cannot capture the challenge of physical reasoning in its full generality. Existing benchmarks (Section III) cover more general challenges for robot learning and planning---broad task diversity, long-horizon decision making, language grounding---or focus on full-fledged application-focused domains such as home assistance. As a result, it remains difficult to perform targeted evaluation of physical reasoning itself, disentangled from perception, language understanding, or domain-specific considerations.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Focus On Physical Reasoning
Basic Spatial Relations
Nonprehensile Multi-Object Manipulation
Combinatorial Geometric Constraints

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another reason for the lack of consensus is that physical reasoning has been studied from very different perspectives in separate subfields of robotics. Classical approaches such as task and motion planning (TAMP) use explicit models and optimization techniques to formulate and solve generalized constraint satisfaction problems. Model-free approaches such as reinforcement learning (RL) and imitation learning (IL) use data to compile away the need for explicit reasoning. Foundation model (FM) based approaches such as LLM, VLM, or VLA planning combine explicit reasoning in natural language with implicit understanding from pretraining. There is also broad interest in combining the complementary strengths of these approaches, but without clarity on the state of the art, it is difficult to make progress.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address these challenges, we propose (KinDER): a benchmark for Kinematic and Dynamic Embodied Reasoning.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

KinDERGarden: A collection of 25 simulated environments, each with infinite procedurally-generated variations, to capture different facets of physical reasoning.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

KinDERGym: A Python package that includes a Gymnasium-compatible environment API, a collection of parameterized skills and concepts, multiple teleoperation interfaces, and demonstration datasets.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

KinDERBench: A standardized benchmark for physical reasoning approaches, with 13 pre-implemented baselines from the literature on TAMP, RL, IL, and FM.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

All contributions are open-source and tested on multiple standard operating systems. To show that the simulated environments map onto real physical reasoning challenges, we additionally report real-to-sim-to-real results. Taken together, KinDER represents a significant step toward clarifying and advancing the state-of-the-art in robot physical reasoning.

<!-- chunk {"id": "body-0012", "role": "body", "section": "KinDER Core Challenges", "weight": 1.0} -->

We begin by presenting the core physical reasoning challenges that are prioritized in KinDER. To select these challenges, we started by reviewing existing work in robot planning and learning where individual physical reasoning problems are considered with one-off environments; and existing benchmarks in related areas (Section III). We then identified themes in that are not well-represented. In other words, we chose challenges at the frontier of active research, but where the current state-of-the-art remains unclear.

<!-- chunk {"id": "body-0013", "role": "body", "section": "KinDER Core Challenges", "weight": 1.0} -->

The five KinDER core challenges are illustrated by example in Figure 1. In Section III, we discuss coverage of these challenges in existing benchmarks. In Section IV, we detail how environments in KinDERGarden capture the challenges.

<!-- chunk {"id": "body-0014", "role": "body", "section": "KinDER Core Challenges", "weight": 1.0} -->

Basic Spatial Relations: To set a dinner table, load a dishwasher, or follow instructions with locative prepositions, robots must understand spatial relations between objects. They must have both a passive understanding (is the fork on the left of the plate?) and an active understanding (how can I put it there?).

<!-- chunk {"id": "body-0015", "role": "body", "section": "KinDER Core Challenges", "weight": 1.0} -->

Nonprehensile Multi-Object Manipulation: Generalized manipulation requires more than pick and place---robots should be able to push, pull, sweep, scoop, stir, and slap multiple objects at the same time. They should leverage, rather than strictly avoid, whole-arm and whole-body contact.

<!-- chunk {"id": "body-0016", "role": "body", "section": "KinDER Core Challenges", "weight": 1.0} -->

Tool Use: Robots should use objects to manipulate other objects---hammers, wrenches, hooks, sticks, trays, bins, and step-stools. They should understand not only common tool affordances, but also abstract mechanisms so that they can improvise, e.g., use a rock to pitch a tent.

<!-- chunk {"id": "body-0017", "role": "body", "section": "KinDER Core Challenges", "weight": 1.0} -->

Combinatorial Geometric Constraints: When object-object and robot-object collisions need to be avoided, e.g., while packing, retrieving, or navigating around objects in tight and cluttered spaces, robots must understand and work within implicit geometric constraints. These constraints are combinatorial: when the number of objects grows, the number of constraints (e.g., pairwise collisions) grows polynomially.

<!-- chunk {"id": "body-0018", "role": "body", "section": "KinDER Core Challenges", "weight": 1.0} -->

Dynamic Constraints: To carry a full cup of coffee, balance a delicate tray, scoop and pour without spilling, dribble and toss a basketball, or juggle, robots must use control to stabilize dynamical systems. They should understand and obey dynamic constraints, e.g., safety limits on velocity magnitudes or requirements implicit in a task (don't spill).

<!-- chunk {"id": "body-0019", "role": "body", "section": "KinDER Core Challenges", "weight": 1.0} -->

This list is by no means an exhaustive account of all the challenges associated with robot physical reasoning. Nonetheless, progress on these challenges would represent a significant step forward for the field. It is also worth noting that more general decision-making challenges are pervasive in KinDER---long task horizons, sparse feedback (goal-based rewards), broad task distributions, and time pressure during planning and execution. We omit these from the core list above to keep the focus on physical reasoning.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Benchmarks for Robot Learning and Planning", "weight": 1.0} -->

There has been a significant amount of work on benchmarking robot learning methods. Some benchmarks are geared toward imitation learning *or* reinforcement learning *or* foundation-model-based methods; others are explicitly designed to compare different families of techniques. Table-top manipulation is a common setting, but mobile and bimanual manipulation are also considered. The central technical challenges in these benchmarks include long time horizons, sparse rewards, natural language grounding, and broad task diversity (especially in terms of scene and object variation). For KinDER, we especially take inspiration from LIBERO and MimicLabs.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Benchmarks for Robot Learning and Planning", "weight": 1.0} -->

There is far less work on benchmarks for classical robot planning (e.g., task and motion planning). There are also separate benchmarks for motion planning and task planning. In particular, the International Planning Competition has been a longstanding catalyst for task planning research. To the best of our knowledge, the only benchmark for combined TAMP is the one proposed by Lagriffoul et al., which is not actively used. KinDER facilitates direct comparisons between robot planning and robot learning methods, and their combinations: KinDERGym provides parameterized skills and concepts, and KinDERBench reports results for both planning and learning methods.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Application-Driven Benchmarks", "weight": 1.0} -->

KinDER isolates fundamental challenges of physical reasoning so that researchers can get a clear signal as they work on these challenges. In this sense, KinDER is complementary to benchmarks that are explicitly driven by applications. Home assistance applications are especially well-covered by benchmarks such as ALFRED, AI2-THOR and ManipulaTHOR, BEHAVIOR-1k, Habitat, ManiSkill-HAB, and RoboCasa. Other notable and recent application-focused benchmarks include FurnitureBench for furniture assembly, CleanUpBench for sweeping and grasping, and CookBench for cooking. The need for physical reasoning naturally arises in these benchmarks, among many other challenges for robot perception, planning, and learning. KinDER is designed to evaluate and advance robot physical reasoning specifically.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Physical Reasoning Benchmarks", "weight": 1.0} -->

KinDER takes inspiration from benchmarks outside of robotics that focus on physical reasoning such as the Virtual Tools Game and PHYRE. See Melnik et al. for a survey. In contrast to many of these works, our intention is to advance robotics, rather than to better understand human physical reasoning. Nonetheless, drawing connections between KinDER and human-like physical reasoning approaches represents an opportunity for future work. From the perspective of this literature, important aspects of KinDER include: continuous spaces, multi-step (long-horizon) decision-making, procedural generation, and kinematic and dynamic constraints.

<!-- chunk {"id": "body-0024", "role": "body", "section": "KinDERGarden: Environments", "weight": 1.0} -->

Our first contribution is KinDERGarden, a collection of 25 environments for robot physical reasoning, grouped into four categories: Kinematic2D, Dynamic2D, Kinematic3D, and Dynamic3D. We first discuss what is common among all environments and then describe each category. See Appendix -A for details and Figure 2 for KinDER core challenge coverage.

<!-- chunk {"id": "body-0025", "role": "body", "section": "General Environment Structure", "weight": 1.0} -->

KinDERGarden environments inherit from the general Gymnasium API, which includes an observation space, action space, initial state distribution ${reset}{}$, and a ${step}{}$ function that takes an action as input and produces a next observation, reward, and termination indicator. Rewards are sparse: $- 1$ is given at every step until successful termination, which occurs only when a goal is achieved. All environments have an infinite task distribution that is implemented with procedural generation inside the ${reset}{}$ function; see Figure 3 for an example.

<!-- chunk {"id": "body-0026", "role": "body", "section": "General Environment Structure", "weight": 1.0} -->

The main design decision that distinguishes KinDER from the general Gymnasium API is that all environments use *object-centric states*. An object-centric state is a mapping from object names (e.g., $robot$, $hook$) to real-valued feature vectors. The dimensionality of each vector is determined by object *type*. For example, a $robot$ with type $MobileManipulator$ has features for the robot's base position and velocity in ${SE}{}$, arm configuration and velocity in ${\mathbb{R}}^{7}$, and gripper joint value in $\lbrack 0,1\rbrack$. A $hook$ with type $Movable$ has features for pose and velocity in ${SE}{}$ and bounding box dimensions in ${\mathbb{R}}^{3}$, among others. Another $Movable$ object (e.g., a $plate$) would have the same feature space. This design makes it easy to vary the number of objects, which can be useful for evaluating generalization and test-time scaling (Section VI).

<!-- chunk {"id": "body-0027", "role": "body", "section": "General Environment Structure", "weight": 1.0} -->

Baselines in KinDER can use object-centric states directly, but to facilitate experiments with standard learning-based approaches, we provide two other options. The first option is to use RGB image observations. The second is to commit to a *variant* of a KinDERGarden environment where the objects are constant. For example, in $Shelf3D$, the number of books can vary in general, but in the $b5$ variant, there are always 5 books. For constant-object variants, KinDERGarden flattens the object-centric state into a fixed-dimensionality vector. These environments are then compatible with standard reinforcement learning and imitation learning approaches.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Kinematic2D Environments", "weight": 1.0} -->

The Kinematic2D category includes six environments that are especially useful for studying tool use and combinatorial geometric constraints at a high level of abstraction. This category is *kinematic* in the sense that environment transitions are entirely determined by object poses and robot configurations (velocities and accelerations are not modeled); and *2D* in that it is implemented with 2D shapes. All environments have a robot with a circular base that moves in ${SE}{}$, an extendable 1D arm, and a rectangular vacuum on its end effector that can be activated or deactivated. When the vacuum is activated, all objects in its immediate vicinity become rigidly attached to the robot. Actions are constrained to make small changes to the robot's configuration. When an action is received, a tentative next state is computed. If that next state includes any collisions, the state is reverted. These environments are implemented in pure Python; no physics backend is used.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Dynamic2D Environments", "weight": 1.0} -->

The Dynamic2D category includes four environments that are especially useful for studying nonprehensile multi-object manipulation and tool use at a high level of abstraction. Unlike Kinematic2D, velocities and accelerations are modeled in this category. We use the Pymunk physics backend for dynamics. Similar to Kinematic2D, these environments feature a robot with a circular base and an extendable 1D arm. For the benefit of studying contact-rich dynamics, we use a two-fingered gripper on the end effector.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Dynamic2D Environments", "weight": 1.0} -->

Kinematic2D and Dynamic2D environments require qualitatively different forms of physical reasoning (Figure 4). For example, consider the contrast between $Obstruction2D$ (kinematic) and $DynObstruction2D$ (dynamic). In both environments, the goal is to move a target object onto a target region that may be initially obstructed by one or more obstacles. In the kinematic version, the robot has no choice but to pick and place the obstacles before picking and placing the target object. However, in the dynamic version, shortcuts are possible: if space constraints allow, the robot may be able to push the obstacles out of the way while holding the target.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Kinematic3D Environments", "weight": 1.0} -->

The Kinematic3D category includes five environments that are especially useful for studying spatial relations and combinatorial geometric constraints. These environments are kinematic in the same sense as Kinematic2D (no velocities or accelerations). We use object modeling, forward kinematics, and collision-checking methods from PyBullet to implement transitions in this environment. For consistency, all environments feature a TidyBot++ mobile base with a 7DOF Kinova Gen3 arm and a Robotiq 2F-85 gripper. When the gripper is closed, objects between the fingers become rigidly attached to the robot until the gripper is opened. As with Kinematic2D, actions are constrained to make small changes to the robot's configuration; states are reverted when collisions are detected.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Dynamic3D Environments", "weight": 1.0} -->

The Dynamic3D category includes 10 environments that collectively cover all five core physical reasoning challenges. Velocities and accelerations are modeled; we use the MuJoCo physics backend for dynamics. For consistency, we use the same TidyBot++ mobile manipulator as in Kinematic3D. Unlike Kinematic3D, grasping is dynamic---objects are never rigidly attached to the robot. Inspired by other MuJoCo-based benchmarks such as LIBERO, we use environment configuration files so that all Dynamic3D environments share the same Python code and differ only in their configurations. We also take inspiration from the BDDL specification language introduced in BEHAVIOR in our implementation of procedural task generation, and leverage object and scene assets from RoboCasa and MimicLabs respectively.

<!-- chunk {"id": "body-0033", "role": "body", "section": "KinDERGym: Accessible Software", "weight": 1.0} -->

Our second main contribution is KinDERGym, a pip-installable Python package that includes not only an interface to the environments in KinDERGarden, but also parameterized skills and concepts; teleoperation interfaces; and precollected demonstrations. To facilitate ease of use, we developed KinDERGym following strict software engineering standards including continuous integration, linting, type checking, autoformatting, and nearly 400 unit tests. We have tested Python versions 3.10, 3.11, 3.12, Ubuntu 20.04, 22.04, and 24.04, and macOS 12-15, and Windows 10.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Parameterized Skills and Concepts", "weight": 1.0} -->

KinDERGym provides utilities for defining parameterized skills and concepts that can be used for hierarchical planning and learning. Skills are implemented as options with associated PDDL operators and samplers. The options have both object parameters (the same as the PDDL operator) and additional parameters of any type (proposed by the sampler). For example, a ${Pick}{({object},\theta)}$ skill can be used to pick different objects with different relative grasps $\theta \in {{SE}{}}$. For generality, we allow option policies to maintain internal state. A common pattern is to generate and follow a motion plan.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Parameterized Skills and Concepts", "weight": 1.0} -->

Concepts are implemented as relational predicates with classifiers that ground in object-centric states. For example, ${On}{({object},{surface})}$ is a predicate with a classifier that evaluates to True in states where the $object$ is above and in contact with the $surface$. These predicates are used in the preconditions and effects of the skill operators. Together with the object-centric states, concepts can also be understood as defining a two-level scene graph.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Parameterized Skills and Concepts", "weight": 1.0} -->

In our experiments (Section VI), we use KinDERGym skills and concepts for the bilevel planning, LLM planning, and VLM planning baselines. However, the nature of physical reasoning is such that hierarchical task decompositions are not always readily apparent or easy to engineer. Designing or learning such skills remains an important direction for future work on physical reasoning that KinDER can support.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Teleoperation Interfaces and Demonstrations", "weight": 1.0} -->

KinDERGym includes multiple teleoperation interfaces that can be used to collect human demonstrations. Kinematic2D and Dynamic2D environments can be controlled through a mouse-and-keyboard interface, or through a PS5 video game controller. The mouse-and-keyboard interface includes joystick-like buttons that can be clicked and dragged to move the robot in ${SE}{}$. Keyboard commands extend and retract the arm, activate and deactivate the vacuum (for Kinematic2D), and open and close the gripper (for Dynamic2D). The PS5 controller similarly uses the joysticks to move the robot and buttons for the arm, vacuum, and gripper.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Teleoperation Interfaces and Demonstrations", "weight": 1.0} -->

Kinematic3D and Dynamic3D environments can be controlled through an iPhone web app, or through a Meta Quest 3S virtual reality headset and controller. The iPhone web app is based on the TidyBot++ interface, which uses the iPhone's gyroscope and accelerometer to capture spatial inputs. The teleoperator can toggle between base and arm control. For arm control, inputs are mapped to task (end effector) space and inverse kinematics is used to derive environment actions. The Meta Quest 3S interface uses the right-hand controller for task-space inputs and the left-hand controller for base movements. We additionally allow the teleoperator to select one or more camera angles, which can also be defined relative to the robot.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Teleoperation Interfaces and Demonstrations", "weight": 1.0} -->

For environments with parameterized skills and concepts implemented, we can also use planners to derive demonstrations at scale. As part of KinDERGym, we use a combination of teleoperation and planning to provide $\geq 100$ precollected demonstrations for 10 environments (Appendix -B). We encourage KinDER users to collect and open-source additional demonstrations using the teleoperation interfaces provided.

<!-- chunk {"id": "body-0040", "role": "body", "section": "KinDERBench: Baselines and Metrics", "weight": 1.0} -->

Our third contribution is KinDERBench, a standardized multi-metric benchmark for robot physical reasoning. We report results and release implementations for 13 baselines in 8 environments. In this section, we briefly describe the environments, baselines, and metrics, analyze the results, and present insights from additional experiments.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Environments", "weight": 1.0} -->

We select two representative environments with varying levels of difficulty from each of the four KinDERGarden categories. See Appendix -A for detailed descriptions.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Environments", "weight": 1.0} -->

$Motion2D$: The simplest Kinematic2D environment. The robot must move to reach a goal region. In this variant ($p0$), there are no obstacles.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Environments", "weight": 1.0} -->

$StickButton2D$: A Kinematic2D environment where a robot must press a button. The button is sometimes out of reach, requiring the robot to use a stick as a tool to press it. In this variant ($b1$), there is one button.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Environments", "weight": 1.0} -->

$DynObstruction2D$: The Dynamic2D environment in Figure 4. In this variant ($o1$), there is one obstacle.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Environments", "weight": 1.0} -->

$DynPushPullHook2D$: A Dynamic2D environment that requires using a hook to pull a target object surrounded by obstacles. In this variant ($o5$), there are five obstacles.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Environments", "weight": 1.0} -->

$BaseMotion3D$: The simplest Kinematic3D environment. The robot must move its base to reach a goal region. In this variant ($o0$), there are no obstacles.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Environments", "weight": 1.0} -->

$Transport3D$: A Kinematic3D environment where a box and one or more objects must be moved from the floor to a table. The box may be used as a container, but this is not required (and not always optimal). In this variant ($o2$), there are two objects in addition to the box.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Environments", "weight": 1.0} -->

$Shelf3D$: A Dynamic3D environment where objects must be packed into a space-constrained shelf. In this variant ($o1$), one object must be packed.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Environments", "weight": 1.0} -->

$SweepIntoDrawer3D$: A Dynamic3D environment where small objects on a countertop must be moved to an initially closed drawer, optionally using a sweeping tool. In this variant ($o5$), there are 5 objects.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Baselines", "weight": 1.0} -->

We evaluate 13 representative planning and learning baselines. See Appendix -C for details.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Baselines", "weight": 1.0} -->

Bilevel Planning (BP): A search-then-sample TAMP planner; uses skills and concepts.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Baselines", "weight": 1.0} -->

LLM Planning (LLMPlan): An LLM (GPT-5.2 ) planner; uses object-centric states and skills.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Baselines", "weight": 1.0} -->

VLM Planning (VLMPlan): A VLM (GPT-5.2 ) planner; uses *RGB images*, states, and skills.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Baselines", "weight": 1.0} -->

LLM In-context (LLMCon): An LLM (GPT-5.2 ) planner that is prompted with in-context examples and uses object-centric states and skills.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Baselines", "weight": 1.0} -->

VLM In-context (VLMCon): A VLM (GPT-5.2 ) planner that is prompted with in-context examples; uses *RGB images* along with states and skills.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Baselines", "weight": 1.0} -->

Model Predictive Control (MPC): We perform predictive sampling trajectory optimization using MPC with the ground-truth simulation transition functions and (sparse) reward function.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Baselines", "weight": 1.0} -->

Model-based Reinforcement Learning (MBRL): We use the demonstrations collected to train a neural (state-based) transition model and use MPC to select actions with the same sparse reward function.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Baselines", "weight": 1.0} -->

Generative Diffusion Planning: We train and evaluate Generative Skill Chaining (GSC) with our demonstration data annotated with skill labels.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Baselines", "weight": 1.0} -->

Proximal Policy Optimization (PPO): A standard *on-policy* deep reinforcement learning method.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Baselines", "weight": 1.0} -->

Soft Actor-Critic (SAC): A standard *off-policy* deep reinforcement learning method.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Baselines", "weight": 1.0} -->

Diffusion Policy (DP): Imitation learning over RGB images, trained with 100 demos per environment.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Baselines", "weight": 1.0} -->

DP + Environment States (DPES): Same as DP, but with states also provided as input.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Baselines", "weight": 1.0} -->

Finetuned VLA: A pretrained $\pi_{0.5}$ VLA fine-tuned on the same demos as DP.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

KinDERBench includes multiple metrics that capture different dimensions of efficiency and effectiveness in physical reasoning.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

Cumulative Rewards (Rwd): A measure of efficiency. Recall rewards are $- 1$ until success. This metric is considered only for successful episodes.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

Inference Time (Inf-Time): Another measure of efficiency. We report per-episode wall-clock time (sec).

<!-- chunk {"id": "body-0067", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

Another metric that is equally important but difficult to capture quantitatively is engineering cost: the amount of engineering needed to run a method in a new environment. For example, BP has a high engineering cost because it requires skills and concepts; RL has a much lower cost.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Benchmark Results", "weight": 1.0} -->

We present our main benchmark results in Table II. All baselines are evaluated over 5 random seeds with 50 evaluation episodes per seed. We report means in the main paper and standard deviations in Appendix -C. Overall, BP obtains the highest average success rate (0.57), followed by LLMCon (0.43), VLMCon (0.43), LLMPlan (0.34), VLMPlan (0.34), MPC (0.32), VLA (0.32), GSC (0.26), DPES (0.25), DP (0.24), PPO (0.13), MBRL (0.08), SAC (0.02). The general trend is expected: paying higher engineering costs and spending more inference time leads to dividends in success rates.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Benchmark Results", "weight": 1.0} -->

We now discuss baseline performance in detail, highlighting some of the more surprising results. First, given that both use the same parameterized skills, the gap between BP and LLMPlan/VLMPlan, especially in the more challenging environments, indicates that there remains room to improve the latter approaches. The comparison between LLMPlan/VLMPlan and LLMCon/VLMCon shows that in-context examples are important for the overall performance. Furthermore, the comparable performance between LLMPlan/VLMPlan suggests that the VLM is not able to meaningfully leverage the images that it receives in addition to the object-centric states.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Benchmark Results", "weight": 1.0} -->

Sweep Some Objects
Sweep All Objects

<!-- chunk {"id": "body-0071", "role": "body", "section": "Benchmark Results", "weight": 1.0} -->

The imitation learning baselines (DP, DPES, VLA) perform well overall, considering that they do not have access to parameterized skills. Interestingly, the VLA is the only baseline that achieves a non-trivial success rate (0.43) on the $DynPushPullHook2D$ task with 5 obstacles. Recall that this environment requires both tool use and nonprehensile multi-object manipulation. This result is surprising because the 2D rendering and physics is quite different from the data used to pretrain the VLA. Another surprising finding is the nontrivial success rate of DP (0.14) and DPES (0.04) on the long-horizon multi-stage $SweepIntoDrawer3D$, which requires the robot to open the drawer, grasp the sweeper, and then sweep multiple objects into the drawer. We also provide subtask success rates in Table III. We also see that DPES performs comparably to DP, despite its access to object-centric states. This suggests that DP is not able to meaningfully leverage the states, which is an interesting dual to the LLM/VLM case.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Benchmark Results", "weight": 1.0} -->

We also find that the MPC baseline performs well, given that it only receives the sparse reward functions. We attribute the good performance to the predictive sampling proposed. The MBRL performs worse than the MPC baseline, though they use the same planner, which demonstrates that the learned transition model is unreliable.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Benchmark Results", "weight": 1.0} -->

Finally, we find that the RL baselines (PPO and SAC) perform well only in short-horizon tasks, which is expected given the sparse rewards and lack of inductive bias given to these methods. In Appendix -B, we report additional results showing that dense rewards can improve performance, but success rates for RL remain low overall.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Additional Results", "weight": 1.0} -->

Out-of-Distribution Generalization: We next evaluate generalization to unseen scenarios for the imitation learning baselines (DP, VLA) that do not require environment-specific state vectors in the $DynObstruction2D$ environment. After training with 1 obstacle, we test with 0, 2, and 3 obstacles. Results are shown in Table IV. Although there is some performance degradation, both baselines perform surprisingly well in these out-of-distribution tasks. The VLA is particularly robust, perhaps due to pretraining.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Additional Results", "weight": 1.0} -->

Scaling Bilevel Planning: We finally evaluate the efficiency and effectiveness of bilevel planning in the $StickButton2D$ environment as the number of objects increases. In Table V, we see that the success rate and planning time substantially decrease and increase respectively. This highlights an opportunity for future work that uses learning to improve planning for physical reasoning at scale.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Real World Validation", "weight": 1.0} -->

We next demonstrate an example of real-to-sim-to-real with the TidyBot++ as the real robot and the $Shelf3D$ environment in KinDERGarden as the simulator (Figure 5). Our goal is to show that KinDERGarden corresponds to real-world physical reasoning challenges, while also highlighting the potential for future real-to-sim-to-real research using KinDER. We use an overhead camera to localize the robot and obtain object bounding boxes and poses using. Given the estimated robot and object poses, we initialize the robot states and object-centric states accordingly. We then generate a plan in the simulator and execute it back in the real world. See Appendix -D for additional discussion.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Limitations and Discussion", "weight": 1.5} -->

We conclude by acknowledging several limitations of the present work. First, as with any simulation-based benchmark, certain aspects of real-world physics and interaction are not fully captured. While the challenges emphasized here primarily target "mid-level" reasoning, where fine-grained physical details may be less critical, there exist important dimensions of physical reasoning for which real-world fidelity plays a more substantial role. Second, to maintain a manageable scope, we made a number of design choices that necessarily exclude other factors relevant to robotics and physical reasoning, including stochasticity, partial observability, diverse robot embodiments, and multi-robot coordination. Third, although we selected baseline methods that are standard and broadly representative, many alternative approaches were not evaluated. We look forward to actively supporting the community and maintaining KinDER open-source as researchers develop and evaluate more sophisticated methods.
