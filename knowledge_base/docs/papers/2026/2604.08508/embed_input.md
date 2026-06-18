<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sumo: Dynamic and Generalizable Whole-Body Loco-Manipulation

Topics include Robotics, Control barrier functions, Control, Sumo.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a sim-to-real approach that enables legged robots to dynamically manipulate large and heavy objects with whole-body dexterity. Our key insight is that by performing test-time steering of a pre-trained whole-body control policy with a sample-based planner, we can enable these robots to solve a variety of dynamic loco-manipulation tasks. Interestingly, we find our method generalizes to a diverse set of objects and tasks with no additional tuning or training, and can be further enhanced by flexibly adjusting the cost function at test time. We demonstrate the capabilities of our approach through a variety of challenging loco-manipulation tasks on a Spot quadruped robot in the real world, including uprighting a tire heavier than the robot's nominal lifting capacity and dragging a crowd-control barrier larger and taller than the robot itself. Additionally, we show that the same approach can be generalized to humanoid loco-manipulation tasks, such as opening a door and pushing a table, in simulation. Project code and videos are available at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Humans and animals physically interact with the world in creative ways: Their ability to gracefully make and break contact with their environment enables them to traverse treacherous terrain and move objects several times larger than themselves. Achieving similar levels of athletic intelligence for robotic systems has been a long-standing challenge. Over the past decade, developments in numerical optimization \[cleach2024, grandia2023perceptive, bledt2018cheetah\] and machine learning \[hwangbo2019learning, cheng2024parkour\] have made significant progress towards building robots with agility and dexterity \[suh2025dexterous, qi2025simple\]. The next research frontier lies in enabling robots to manipulate objects during locomotion, or so-called loco-manipulation. So far, research on loco-manipulation has largely focused on learning from human demonstrations through teleoperation or video imitation, which are usually limited to quasi static table-top settings and fails to leverage the passive dynamics of the object or the robot. Algorithms and systems that enable a robot to autonomously coordinate its entire body to dynamically move large and heavy objects during loco-manipulation have, so far, been elusive.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper studies loco-manipulation problems in which the manipulated object is large, heavy, or geometrically complex enough that success requires dynamic coordination of the robot's whole body. Recent works have shown impressive in-the-wild locomotion agility enabled by reinforcement learning (RL). However, adapting RL to each new manipulation task often requires substantial reward engineering, retraining, and compute, and can be difficult to generalize beyond the training distribution. On the other hand, sample-based model-predictive control (MPC) has proven to be a simple and training-free method for contact-rich manipulation \[howell2022mjpc, alvarez2025real, li2025_judo, li2024drop\]. Yet sample-based MPC struggles to find good solutions for high-degree-of-freedom robots or dynamically unstable tasks, which frequently occur in quadruped and humanoid loco-manipulation.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our approach combines the strengths of both. We start from a pre-trained generalist whole-body control policy learned with RL and use real-time sample-based MPC to steer it for contact-rich manipulation of previously unseen objects. This hierarchy addresses key shortcomings of both end-to-end RL and sample-based MPC while preserving their main advantages. RL provides a robust whole-body controller when the training distribution can be modeled with sufficient randomization \[2025relic\]. In turn, the low-level policy reduces the effective action space for online planning and stabilizes the dynamics, mitigating the divergence issues associated with single-shooting rollouts of unstable systems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our framework, which we call Sumo, enables the high-level sample-based controller to steer the policy effectively for real-world manipulation. Our experiments reveal two interesting properties of this approach. First, hierarchical structure simplifies loco-manipulation. Compared to end-to-end MPC, planning in the command space of a pre-trained whole-body policy reduces the effective search space and stabilizes the robot's contact-rich dynamics. Compared to end-to-end RL, the same hierarchy achieves similar or better success with much simpler task objectives and without task-specific retraining. Second, planning enables generalization. Here, we define generalization as reusing the same controller on new objects and new task objectives by changing only the planner's object model or cost function at test time, without retraining. Keeping high-level decision making online allows the same framework to make these adaptations directly at deployment. The result is a robust yet flexible framework that enables quadruped and humanoid robots to use their entire body to manipulate objects with complex geometries and with sizes and weights comparable to the robots themselves, Fig. LABEL:fig:teaser_robot_tasks.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A hierarchical framework that combines a pre-trained generalist whole-body control policy and test-time planning for dynamic whole-body loco-manipulation.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A set of experimental comparisons showing that hierarchical structure simplifies loco-manipulation by reducing search difficulty and task-specification complexity relative to end-to-end MPC and end-to-end RL baselines.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

A set of experimental comparisons showing that test-time planning enables adaptation to new objects and new task objectives without retraining by changing the object model or cost function at deployment.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A set of eight real-world demonstrations on the Spot quadruped robot and four demonstrations on the G1 humanoid robot in simulation covering diverse and challenging loco-manipulation scenarios.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

An open-source benchmark and dataset focusing on loco-manipulation tasks with objects that require whole-body coordination due to their size and weight relative to the robots' physical limits.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is organized as follows: In Sec. II, we discuss the previous success of RL and sample-based MPC, as well as their pitfalls. Additionally, we review recent approaches to loco-manipulation. In Sec. III, we detail the Sumo framework and key design decisions. In Sec. IV, we analyze the performance, test-time flexibility, and sample efficiency of Sumo against baseline algorithms in controlled simulation. In Sec. V, we further demonstrate the capabilities of our framework on a diverse set of challenging loco-manipulation tasks on a real-world Spot quadruped robot and a simulation G1 humanoid robot. Finally, we conclude in Sec. VI by addressing the limitations of the current system and propose directions for future research.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Reinforcement Learning for Whole-Body Control", "weight": 1.0} -->

Deep reinforcement learning aims to learn neural-network policies via self-play trial and error. In robotics, the advancements in large-scale parallel simulation platforms \[mittal2023orbit, mujoco_warp2025\] on accelerated hardware (such as GPUs) have significantly reduced the cost of collecting data in simulation. As a result, on-policy RL algorithms, such as PPO \[schulman2017ppo\], have become a staple in the sim-to-real policy optimization paradigm. Additionally, RL naturally incorporates robust policy optimization via domain randomization techniques \[tobin2017domain\], reducing the so-called sim-to-real gap.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Reinforcement Learning for Whole-Body Control", "weight": 1.0} -->

Despite its promise, this RL paradigm faces several significant drawbacks in practice: First, RL typically requires dense reward design to find efficient policies with finite compute \[ng1999policy, andrychowicz2017hindsight\]. Second, the final policy is often sensitive to reward design, and finding a suitable reward term itself is often a non-trivial and manual search problem. Because of these practical shortcomings, researchers typically have to go through a time-consuming loop of reward engineering, policy training, and hardware testing, before going back to reward engineering for each task. While the recent emergence of LLMs \[yu2023language, ma2023eureka\] can automate this process to some degree, reliably finding suitable rewards that lead to successful sim-to-real transfer still requires (expert) human-in-the-loop intervention, especially when policy optimization is time-consuming.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Reinforcement Learning for Whole-Body Control", "weight": 1.0} -->

The sim-to-real RL paradigm has been particularly successful for legged robot locomotion \[hwangbo2019learning, cheng2024parkour\], where rewards have become relatively standardized and one can carefully design curricula for difficult terrain variations. However, in open-world manipulation, robots are faced with reasoning over a diverse set of scenarios including objects that vary in size, weight, geometry, friction, etc. This test-time diversity makes randomizing all possible distributions challenging at training time for sim-to-real RL. As a result, successful real-world manipulation, so far, has come from learning from demonstrations \[chi2024diffusionpolicy\].

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Reinforcement Learning for Whole-Body Control", "weight": 1.0} -->

In this work, we take advantage of RL's strength---learning robust locomotion policies over complex terrains offline---and leave the complexity of generalizable contact-rich decision making to online search via sample-based MPC.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Sample-Based MPC", "weight": 1.0} -->

Sample-based MPC is a family of zeroth-order trajectory-optimization methods that aims to solve for an optimal control sequence over a (typically short) prediction horizon. Sample-based MPC has been derived from many perspectives, including path integrals \[williams2016\], information theory \[williams2018\], importance sampling \[zhang2014crossentropy\], and diffusion \[pan2024modelbaseddiffusiontrajectoryoptimization\]. Additionally, sample-based MPC methods are closely related to other derivative-free optimization algorithms such as CMA-ES \[hansen2016cma\]. Notably, similar to zeroth-order RL, which typically requires lots of compute *offline*, sample-based MPC can be viewed as an *online* policy-gradient method \[qiu2025zerothorder\] that is entirely training-free, making it extremely flexible at test time.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Sample-Based MPC", "weight": 1.0} -->

Because of its parallel nature and ease of implementation, this family of trajectory optimization algorithms has grown in popularity in recent years, along with the rise of modern parallel computing hardware. The derivative-free nature of sample-based MPC is amenable to contact-rich dynamics and learned black-box deep neural network dynamics models, where computing derivatives is expensive or unreliable \[tracy2025trajectory, zhang2025wholebodymodelpredictivecontrollegged\], which often occurs in contact-rich control. In contrast, classical gradient-based methods such as the iterative linear-quadratic regulator (iLQR) \[jacobsonMayne1970DDP, li2004iterative\] and direct-collocation \[kelly2017introduction\] typically struggle in these scenarios without additional care to modify the derivatives \[cleach2024\].

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Sample-Based MPC", "weight": 1.0} -->

Online sample-based MPC has two main pitfalls: the curse of dimensionality and unstable dynamical systems. As an online search algorithm, sample-based MPC suffers from the curse of dimensionality that stems from high-dimensional input spaces associated with highly articulated robots and longer prediction horizons. Recent works have proposed to reduce the temporal dimensionality by sampling over low-order spline control points \[howell2022mjpc, li2025_judo, alvarez2025real\], making sample-based MPC tractable in real-time for robots like dexterous hands, quadrupeds, and humanoids. Furthermore, sample-based MPC generally relies on single-shooting dynamics rollouts, leading to divergence on open-loop unstable systems, which commonly occur in legged robotics.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Sample-Based MPC", "weight": 1.0} -->

In our framework, by leveraging a low-level WBC policy, the sample-based MPC enjoys the benefit of sampling in a reduced action space on a stabilized dynamical system, drastically improving sample efficiency during online search.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-C Loco-Manipulation", "weight": 1.0} -->

Building robots that manipulate objects during locomotion, or so-called "loco-manipulation", has become an increasingly important yet challenging research direction as it inherits the fundamental challenges of both manipulation and locomotion for legged robots. Prior works have deployed both model-based methods \[alvarez2025real\] and RL methods \[sferrazza2024humanoidbench\] to achieve joint locomotion and manipulation of objects. Notably, several works have investigated using legs as manipulators \[2025relic, cheng2023legmanip, arm2024pedipulate, cheng2025rambo\].

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-C Loco-Manipulation", "weight": 1.0} -->

For humanoid loco-manipulation, retargeting human motions has become a popular method to bootstrap downstream learning and optimization \[yang2025omniretarget, zhang_slomo_2023\]. However, these teleoperation and retargeting approaches are much less applicable to non-anthropomorphic robots, like Spot. \[sleiman2023versatile\] explores building a planning and control framework for legged robot loco-manipulation, but the control module requires fixed contact modes during planning and is limited to quasi-static behaviors.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-C Loco-Manipulation", "weight": 1.0} -->

Different from existing literature, we focus on manipulating objects that are larger than the robot itself or heavier than the maximum lifting capacity of the robot, thus requiring the robot to efficiently coordinate its entire body to solve these tasks. Our method naturally incorporates RL and online MPC while retaining detailed robot dynamics and collision geometry, and without requiring fixed contact modes during planning \[cheng2025rambo, sleiman2023versatile\].

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-D Hybrid RL-MPC Methods", "weight": 1.0} -->

Many recent works aim to leverage the robustness of RL policies together with the structure of model-based control \[dtc, cheng2025rambo, cajun2023, jeon2025residualmpc\]. This broad family includes RL-augmented whole-body controllers, optimization-guided tracking policies, and residual policies around MPC controllers. These methods have demonstrated strong tracking, locomotion, and force-control capabilities by using model-based components to provide structure, reference motions, or low-level constraints while learned policies improve robustness. Sumo is closely related to this line of work, but studies a complementary setting: autonomous, goal-conditioned loco-manipulation in which no teleoperator, expert motion library, or task-specific model-based planner provides a reference motion. In this setting, the online optimizer must reason over object interactions and manipulation objectives directly.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-D Hybrid RL-MPC Methods", "weight": 1.0} -->

More broadly, a common design pattern in hybrid RL-MPC for contact-rich robotics is a high-level RL, low-level MPC hierarchy \[dtc, cheng2025rambo, cajun2023, jeon2025residualmpc\]. Sumo instead explores the alternative high-level MPC, low-level RL paradigm, motivated by the recent emergence of powerful generalist tracking policies \[2025relic, li2026omnitrackgeneralmotiontracking, luo2025sonicsupersizingmotiontracking\] that typically interface with task-space teleoperation or follow motion references. By using MPC to steer such a policy online, we can synthesize dynamic behaviors from task objectives at deployment rather than depending on teleoperated or planner-generated references. Planning over pretrained robot policies has also been explored in tabletop manipulation \[vgps, jain2025smoothseanevermade\] where the base policy is trained via imitation learning, but to our knowledge has not been studied in dynamic, contact-rich loco-manipulation settings where the base policy is trained via RL.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Sumo", "weight": 1.0} -->

In this section, we provide a detailed description of our hierarchical control framework, which we call Sumo, that uses a high-level sample-based controller to steer a pre-trained whole-body control policy to perform whole-body loco-manipulation with quadruped and humanoid robots.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Overview", "weight": 1.0} -->

Our system, detailed in Figure 2, uses a pre-trained steerable whole-body control policy that takes in the current state and desired torso, arm, and optionally leg commands of the robot and outputs the low-level joint commands for the quadruped or humanoid robot at $50$Hz. At the high-level, we use a sample-based MPC policy (e.g., MPPI, CEM, etc.) that takes in the current state estimate and updates the desired torso and arm commands for the low-level locomotion policy at $20$Hz. Together, our framework enables complex loco-manipulation skills that can only be achieved through whole-body contact-rich coordination, such as uprighting and stacking a fallen tire heavier than the robot's lifting capacity (Fig. 7 (a) (e)), and uprighting and dragging a crowd control barrier larger than the robot itself (Fig. 7 (b) (f)).

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Pre-Trained Whole-Body Control Policy", "weight": 1.0} -->

For the low-level policy, we use an existing whole-body control policy trained via RL that takes high-level commands and outputs the joint-level commands for the entire robot. Methods for training humanoid and quadruped policies have been studied extensively in the literature and are widely available \[hwangbo2019learning, cheng2024parkour\]. We do not aim to improve whole-body control capabilities in this paper, and instead focus on their downstream applications for loco-manipulation. Specifically, we use the Relic policy \[2025relic\] which is designed for multi-limb loco-manipulation on the Spot quadruped robot. In particular, the Relic policy enables stable gaits with only three legs and allows the robot to use the fourth leg as a manipulator in addition to its arm and torso. This setup allows the high-level sampling-based controller to automatically reason about using multiple limbs or a combination of limbs and torso to manipulate an otherwise challenging object.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B Pre-Trained Whole-Body Control Policy", "weight": 1.0} -->

For the G1 humanoid robot, we use the standard velocity-tracking policy from MJLab \[mjlab2025\] that takes in the desired torso velocity commands. While this policy is not explicitly trained for loco-manipulation and does not take in the desired arm commands, we find that simply overriding the arm commands with target commands from the high-level sampling-based MPC is also effective.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B Pre-Trained Whole-Body Control Policy", "weight": 1.0} -->

While we believe these are natural choices for low-level policies for the Spot and G1 robots, one can similarly choose other policies over arbitrary input spaces from which the sample-based controller can sample. We focus on the benefits of leveraging an existing whole-body control policy in this paper and leave testing different whole-body control policies to future work, as researchers actively expand the capabilities of whole-body control policies.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-C Policy-in-the-Loop Parallel Rollouts", "weight": 1.0} -->

A key component of our system is a policy-in-the-loop MuJoCo physics simulation that allows us to sample actions in the input space of the low-level locomotion policy instead of the whole-body joint-level action space of the entire robot as was done in previous works \[alvarez2025real, li2025_judo\]. This design choice is critical for online sample efficiency for several reasons: First, this allows the sample-based MPC to sample in a lower-dimensional action space, mitigating the curse of dimensionality commonly seen for search algorithms. Second, with the low-level locomotion policy as a stabilizing controller, we avoid the well-known divergence issues associated with single-shooting methods applied to unstable dynamics that commonly occur with legged robots. Finally, because the whole-body control policy handles the locomotion part of the problem, this setup allows us to design much simpler cost function that only needs to encode manipulation objectives.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-C Policy-in-the-Loop Parallel Rollouts", "weight": 1.0} -->

We implement the policy-in-the-loop parallel simulation by augmenting the CPU-based MuJoCo physics engine \[todorov2012mujoco\] in C++ using thread pool. In Table I we report the rollout times of $32$ parallel rollouts over $1.5$ seconds with and without the low-level policy on an Intel Core i7-12700K CPU. Indeed, the low-level policy adds overhead to the physics simulation, but the total times are faster than the $20$Hz or $50$ms update rate of the sample-based MPC.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-D High-Level Sample-Based MPC", "weight": 1.0} -->

Naturally, the high-level sample-based MPC can sample over any action space supported as inputs to the low-level policy. In practice, we choose to sample actions over a compact, task-relevant control vector, then rely on the low-level policy to map this to a full whole-body command. Here, we describe the details for the Spot robot with the Relic policy, but similar principles apply to other robots and low-level policies. We use $\mathbf{a}$ to denote the action space for the sample-based MPC, $\mathbf{c}$ to denote the commands to the WBC policy, and $\mathbf{u}$ to denote the joint-level control to the robot.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-D High-Level Sample-Based MPC", "weight": 1.0} -->

By default, we only sample over the base velocities $\mathbf{a}_{base} \in {\mathbb{R}}^{3}$ and arm joint angle targets $\mathbf{a}_{arm} \in {\mathbb{R}}^{6}$ for the arm, excluding the gripper. To pad remaining policy commands, we set leg targets to zero (the low-level policy automatically outputs leg joint commands to track desired base velocities) and use default values for the torso pitch, roll, and height targets and set the gripper to a closed position. This base setup is sufficient for many loco-manipulation tasks but can be further enhanced by reasoning over legs, torso, and gripper commands at test time for tasks that require multi-limb coordination or gripper dexterity.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-D High-Level Sample-Based MPC", "weight": 1.0} -->

To reason over the torso roll, pitch, and height commands, we can simply add those dimensions $\mathbf{a}_{\text{torso}} \in {\mathbb{R}}^{3}$ to the action space.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-D High-Level Sample-Based MPC", "weight": 1.0} -->

Note that it is also possible to use rear legs for manipulation, but our implementation chooses to only focus on front legs as they cover most practical loco-manipulation tasks.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-D High-Level Sample-Based MPC", "weight": 1.0} -->

This design allows us to flexibly choose task-specific action spaces to be any combination of $\mathbf{a} = {\lbrack\mathbf{a}_{\text{base}},\mathbf{a}_{\text{arm}},\mathbf{a}_{\text{torso}},\mathbf{a}_{\text{leg}},\mathbf{a}_{\text{gripper}}\rbrack}$ for the sample-based MPC. Additionally, the selection variables allow the controller to reason over different manipulation modalities at test time. Note that our sample-based MPC naturally reasons over both continuous and discrete decision variables which would be challenging for traditional gradient-based optimal control algorithms.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-D High-Level Sample-Based MPC", "weight": 1.0} -->

For the G1 humanoid robot, we similarly sample over the ${SE}{}$ velocities for the torso and the arm joint angle targets for the arm. While it is straight forward to enable more inter-limb coordination by using a more steerable underlying low-level policy \[liao2025beyondmimic\], we leave this investigation as a future direction.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experimental Analysis", "weight": 1.0} -->

In this section, we use simulation experiments in MuJoCo \[todorov2012mujoco\] to analyze three advantages of Sumo: hierarchical structure simplifies loco-manipulation, test-time search enables generalization, and Sumo achieves higher sample efficiency than a hierarchical RL policy.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-A Task Definition and Experiment Setup", "weight": 1.0} -->

In this section, we consider two types of loco-manipulation tasks on the Spot quadruped robot: moving an object to a goal position (Move) and reorienting an object to the upright orientation (Upright). In both cases, we consider five objects covering a range of size, weight, and geometry representative of real-world scenarios: a $1.5$ kg box, a chair, a car tire, a tire rack, and a traffic cone.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-A Task Definition and Experiment Setup", "weight": 1.0} -->

For Move tasks, we consider success if the object is within $0.1$ meters of the goal and velocity is less than $0.05$ m/s within $30$ seconds. For Upright tasks, we consider task success if the object is within $0.1$ radians of the upright orientation and angular velocity is less than $0.05$ rad/s within $30$ seconds.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-A Task Definition and Experiment Setup", "weight": 1.0} -->

(a) Move Object Tasks
(b) Upright Object Tasks
Figure 5: Top: comparison of Sumo (yellow, ours), E2E RL (purple), and hierarchical RL (navy, HRL) on pushing five different objects to a goal. Sumo generalizes to new objects by replacing the object model at test time, whereas E2E RL and HRL policies trained only on box pushing fail on the other objects. Bottom: Sumo generalizes to uprighting objectives by changing the planner cost at test time, whereas the same E2E RL and HRL policies fail without additional training.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-A Task Definition and Experiment Setup", "weight": 1.0} -->

To simplify the analysis, we restrict the Sumo high-level planner to only control the torso ${SE}{}$ velocities and joint angle targets for the arm in this section and leave exploring more expressive policy behaviors to Sec. V.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-A Task Definition and Experiment Setup", "weight": 1.0} -->

where $\mathbf{p}_{\text{obj}}$, $\mathbf{p}_{\text{goal}}$, and $\mathbf{p}_{\text{gripper}}$ are the positions of the object, goal, and gripper in world frame, respectively, $\mathbf{v}_{\text{obj}}$ is the linear velocity of the object, and $w_{\text{goal}},w_{\text{gripper}},w_{\text{vel}}$ are weighting coefficients.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-A Task Definition and Experiment Setup", "weight": 1.0} -->

where $\mathbf{q}_{\text{obj}}$ and $\mathbf{q}_{\text{upright}}$ are the quaternions of the object and upright orientation, respectively, and $w_{\text{Upright}},w_{\text{gripper}}$ are weighting coefficients.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-A Task Definition and Experiment Setup", "weight": 1.0} -->

For all Sumo experiments, we use a Cross-Entropy Method (CEM) optimizer with a prediction horizon of $1.5$ seconds, $32$ rollouts, and update the action distribution with three elite samples at a frequency of $20$Hz. We sample over four spline control points along the prediction horizon and interpolate the remaining actions. Finally, we linearly schedule the noise variance ramping from $0.02$ to $0.6$ over the prediction horizon. All experiments are conducted synchronously on a desktop computer equipped with an Intel Core i7-12700K CPU and 64GB of RAM. Current robot and object states are provided by the ground-truth simulator.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-B Hierarchical Structure Simplifies Loco-Manipulation", "weight": 1.0} -->

We first evaluate whether hierarchical structure simplifies loco-manipulation. Fig. 4 compares Sumo against both real-time MPC (E2E MPC) and end-to-end RL (E2E RL) on the Move tasks. This comparison isolates the benefit of planning in the command space of a pre-trained whole-body controller rather than optimizing directly over joint-level actions or learning a task-specific end-to-end policy.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-B Hierarchical Structure Simplifies Loco-Manipulation", "weight": 1.0} -->

For the E2E MPC baseline, we use the same CEM optimizer, which is used in Sumo and common for locomotion and manipulation \[li2025_judo, howell2022mjpc, alvarez2025real\], whose action space is the joint-level commands of the robot.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-B Hierarchical Structure Simplifies Loco-Manipulation", "weight": 1.0} -->

where $J_{\text{Locomotion}}$ is the locomotion-related cost from \[howell2022mjpc\] and $J_{\text{Move}}$ is defined. Additionally, we allow the E2E MPC to update at $50$Hz to match Sumo's low-level policy frequency.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-B Hierarchical Structure Simplifies Loco-Manipulation", "weight": 1.0} -->

For the E2E RL baseline, we train a state-based, goal-conditioned single-task policy that controls the $19$-DoF joints of Spot to move an object to a goal location. We train the policy using PPO in MJLab \[mjlab2025\] with $4096$ parallel environments for $5000$ iterations. We use $15$ reward terms, including terms that encourage natural walking through a phase-based gait and foot-height schedule, progress toward the manipulation goal, and shaping that encourages the gripper to approach the object and the robot to stay behind it. The policy also receives bonuses when it reaches the goal and keeps the object within $0.2$m, which we count as success. As with Sumo, we tune the reward until the policy reliably solves the box task, then apply the same setup to four additional objects without further task-specific reward engineering. In both baselines, we make a best-faith effort to tune hyperparameters to achieve the best performance.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-B Hierarchical Structure Simplifies Loco-Manipulation", "weight": 1.0} -->

We find that Sumo successfully solves all five Move tasks with at least $80\%$ success across $20$ evaluation trials, with some tasks at $100\%$ success. In contrast, E2E MPC struggles to consistently solve these tasks, achieving at most $50\%$ success. E2E RL is competitive on the box, chair, and cone, but degrades sharply on more complex geometries such as the tire and tire rack. We summarize these results in Fig. 4.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-B Hierarchical Structure Simplifies Loco-Manipulation", "weight": 1.0} -->

These experiments show that hierarchical structure simplifies loco-manipulation in two complementary ways. Compared to E2E MPC, planning in the task space of a pre-trained low-level policy reduces the effective search space and stabilizes the robot's contact-rich dynamics. Compared to E2E RL, Sumo achieves similar or better success with only $3$ reward terms and no task-specific retraining or tuning, whereas E2E RL requires $15$ reward terms and about $2$ hours of GPU compute per task. This comparison also motivates the next question: once a low-level whole-body controller is fixed, should the high-level policy be learned or optimized online at test time?

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-C Test-Time Search Enables Generalization", "weight": 1.0} -->

We next ask whether the high-level decision-making module should be learned or optimized online. Our experiments show that keeping this layer online is what enables generalization in our setting. Here, generalization means reusing the same learned controller on new objects and new task objectives by changing only the planner's object model or cost at test time, without retraining. This distinction matters because RL policies are typically trained for a *known* distribution of environments and objects, whereas open-world manipulation introduces geometries, masses, and contact conditions that are difficult to model comprehensively at training time.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-C Test-Time Search Enables Generalization", "weight": 1.0} -->

Fig. 5 (a) shows that a hierarchical RL policy trained to move a $1.5$ kg box to a goal does not generalize reliably once object geometry and weight move beyond its training distribution, even after randomizing the box size, weight, and friction. While the hierarchical RL policy achieves a $100\%$ success rate on this training task, its performance degrades quickly on objects such as the tire and traffic cone. In contrast, our method can generalize to different objects *without additional training* by simply replacing the object model. All tasks here use the same cost function and hyperparameters described in Eq..

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-C Test-Time Search Enables Generalization", "weight": 1.0} -->

Fig. 5 (b) shows the same advantage for different task objectives. By changing the planner cost function at test time, similar in spirit to guidance for diffusion models \[janner2022diffuser\], we replace the goal-directed objective with the orientation objective in Eq. and enable the robot to reliably upright different objects without additional training. In contrast, the same RL policy cannot be steered to upright different objects without additional training.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-D Sample-Based MPC Provides High Practical Efficiency", "weight": 1.0} -->

Finally, we compare the practical iteration speed of sample-based MPC and RL during hyperparameter tuning. The goal of this experiment is not a hardware-normalized compute comparison, but rather a wall-clock comparison of the tuning loop practitioners would run in practice. In Fig. 6, we mimic this process by performing a Bayesian optimization over the cost weights in for the Move Box task for both Hierarchical RL and Sumo to find the weights that maximize the success rate. We perform five independent optimization runs and track the maximum success rate over time across $50$ trials. Both methods achieve similar asymptotic performance, but Sumo reaches the same performance with an order-of-magnitude less compute time. For Sumo, we measure the compute time as CPU hours on a desktop computer equipped with an Intel Core i7-12700K CPU and 64GB of RAM, and RL training time is measured as GPU hours on an NVIDIA RTX A6000 GPU.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Autonomous Demonstrations with Sumo", "weight": 1.0} -->

In this section, we move from controlled simulation analysis to full-task demonstrations on eight Spot tasks in the real world and four G1 tasks in simulation. Together, these case studies test whether the same hierarchical framework can handle diverse manipulation modes and object interactions beyond the simplified analysis tasks. Unlike the simplified cost functions used in Sec. IV, these demonstrations use task-specific cost functions tailored to each task; full descriptions are provided in the appendix.

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-A Spot Quadruped Loco-Manipulation", "weight": 1.0} -->

In the first case study, we evaluate Sumo on a diverse set of challenging loco-manipulation tasks on the Boston Dynamics Spot quadruped. These tasks stress three recurring difficulties: objects that are larger than the robot or heavier than the arm payload, contact conditions and geometries that create large sim-to-real gaps, and distinct manipulation modes such as uprighting, stacking, dragging, and pushing. The tasks and corresponding performance are summarized in Table II.

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-A Spot Quadruped Loco-Manipulation", "weight": 1.0} -->

For all hardware deployments, we use the same set of optimizer parameters as detailed in Sec. IV. To estimate the robot and object states, we fuse the Spot robot joint encoder reading at $333$Hz with motion-capture (MoCap) measurements for torso and object positions and orientations at $120$Hz using a low-pass filter. We compute the dynamics rollouts and CEM updates asynchronously on a desktop computer equipped with an AMD Threadripper Pro 5995WX CPU with $64$ cores, which sends joint-level commands to the Spot robot via WiFi.

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-A Spot Quadruped Loco-Manipulation", "weight": 1.0} -->

Below, we briefly describe each task to provide qualitative context for the quantitative results in Table II.

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-A Spot Quadruped Loco-Manipulation", "weight": 1.0} -->

Tire Upright: In Fig. 7 (a), the robot is tasked to upright a tire of $15$kg, which is heavier than the maximum lifting capacity of $11$kg of the Spot arm. Additionally, the rubber tire presents hard-to-model geometries and friction properties, causing a large sim-to-real gap. Using a combination of its arm, torso, and legs, Sumo enables the robot to complete the task $10$ out of $10$ trials with an average completion time of $9.2 \pm 4.7$s, Tab. II.

<!-- chunk {"id": "body-0062", "role": "body", "section": "V-A Spot Quadruped Loco-Manipulation", "weight": 1.0} -->

Crowd Barrier Upright: In Fig. 7 (b), the robot is tasked to upright a crowd barrier of $16$kg from a lying position. Using its arm and gripper, our method enables the robot to complete the task $9$ out of $10$ trials with an average completion time of $10.5 \pm 7.1$s, Tab. II.

<!-- chunk {"id": "body-0063", "role": "body", "section": "V-A Spot Quadruped Loco-Manipulation", "weight": 1.0} -->

Traffic Cone Upright: In Fig. 7 (c), the robot is tasked to upright a traffic cone of $3.5$kg. Using its arm, our method enables the robot to complete the task $9$ out of $10$ trials with an average completion time of $10.2 \pm 7.9$s, Tab. II.

<!-- chunk {"id": "body-0064", "role": "body", "section": "V-A Spot Quadruped Loco-Manipulation", "weight": 1.0} -->

Chair Upright: In Fig. 7 (d), the robot is tasked to upright a chair of $16.5$kg. Using its arm and body, our method enables the robot to complete the task $8$ out of $10$ trials with an average completion time of $27.3 \pm 19.1$s, Tab. II.

<!-- chunk {"id": "body-0065", "role": "body", "section": "V-A Spot Quadruped Loco-Manipulation", "weight": 1.0} -->

Tire Stack: In Fig. 7 (e), the robot is tasked to stack a $15$kg tire on top of another tire. In addition to large weight and deformation, the friction coefficient between the rubber tires is high, which current simulators struggle to simulate accurately, causing an even larger sim-to-real gap. Using a combination of its arm, torso, and legs, our method enables the robot to complete the task $8$ out of $10$ trials with an average completion time of $16.5 \pm 8.4$s, Tab. II.

<!-- chunk {"id": "body-0066", "role": "body", "section": "V-A Spot Quadruped Loco-Manipulation", "weight": 1.0} -->

Crowd Barrier Drag: In Fig. 7 (f), the robot is tasked to drag a crowd barrier of $15$kg in upright orientation. The robot uses the gripper to grasp the barrier and drags it towards a goal position with its arm and body. Our method enables the robot to complete the task $9$ out of $10$ trials with an average completion time of $20.2 \pm 6.7$s, Tab. II.

<!-- chunk {"id": "body-0067", "role": "body", "section": "V-A Spot Quadruped Loco-Manipulation", "weight": 1.0} -->

Tire Rack Drag: In Fig. 7 (g), the robot is tasked to drag a tire rack of $10$kg. The robot uses the gripper to grasp the tire rack and drags it towards a goal position. Our method enables the robot to complete the task $9$ out of $10$ trials with an average completion time of $19.1 \pm 6.2$s, Tab. II.

<!-- chunk {"id": "body-0068", "role": "body", "section": "V-A Spot Quadruped Loco-Manipulation", "weight": 1.0} -->

Rugged Box Push: In Fig. 7 (h), the robot is tasked to push a $20$kg box to a goal. Using its arm and body, our method enables the robot to complete the task $10$ out of $10$ trials with an average completion time of $38.3 \pm 16.9$s, Tab. II.

<!-- chunk {"id": "body-0069", "role": "body", "section": "V-B G1 Humanoid Loco-Manipulation", "weight": 1.0} -->

In the second case study, we show that Sumo can also be applied to humanoid robots. Through simulated experiments using a Unitree G1, our method uses a pre-trained locomotion policy that is widely available \[mjlab2025\], and solves loco-manipulation tasks such as pushing a box and opening a door. Simulation performances are summarized in Table III.

<!-- chunk {"id": "body-0070", "role": "body", "section": "V-B G1 Humanoid Loco-Manipulation", "weight": 1.0} -->

Box Pushing In Fig. 8 (a), the robot is tasked to push a $10$kg box to a target position. Using its arms and body, our method enables the robot to complete the task $9$ out of $10$ trials with an average completion time of $11.83 \pm 2.97$s, Tab. III.

<!-- chunk {"id": "body-0071", "role": "body", "section": "V-B G1 Humanoid Loco-Manipulation", "weight": 1.0} -->

Chair Pushing In Fig. 8 (b), the robot is tasked with pushing a $16.5$kg chair to a goal. Using its arms and body, our method enables the robot to complete the task $10$ out of $10$ trials with an average completion time of $6.86 \pm 0.288$s, Tab. III.

<!-- chunk {"id": "body-0072", "role": "body", "section": "V-B G1 Humanoid Loco-Manipulation", "weight": 1.0} -->

Door Opening In Fig. 8 (c), the robot is asked to open a door. Using its arm and body, our method enables the robot to complete the task $10$ out of $10$ trials with an average completion time of $4.73 \pm 0.98$s, Tab. III.

<!-- chunk {"id": "body-0073", "role": "body", "section": "V-B G1 Humanoid Loco-Manipulation", "weight": 1.0} -->

Table Pushing In Fig. 8 (d), the robot is tasked with pushing a $10$kg table to a goal. Using its arms and body, our method enables the robot to complete the task $8$ out of $10$ trials with an average completion time of $4.86 \pm 1.65$s, Tab. III.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

This paper explores the combination of RL pre-training and test-time sample-based MPC for whole-body loco-manipulation. We find this approach, which we call Sumo, excels at challenging tasks involving large and heavy objects that cannot be solved via pick-and-place-style manipulation. We also find that the decomposition of difficult loco-manipulation tasks into a two-stage optimization problem makes the sub-problems much more tractable. Additionally, we show that using sample-based MPC as a high-level policy enables test-time task flexibility and generalization that is difficult for RL.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

Sumo still has several shortcomings and avenues for future work: First, we rely on a MoCap system for robot and object state estimation and are restricted to laboratory settings. Future work should explore incorporating fully onboard perception systems that allow the robot to navigate challenging terrains during loco-manipulation. Second, as an algorithm relying entirely on sim-to-real transfer, the "sim-to-real gap" remains a significant challenge. While modeling the robot and object dynamics perfectly is impossible and often not necessary, building a "good enough" model for control remains an art that requires some trial and error. In fact, we believe real-time MPC as the high-level policy significantly accelerates this tuning loop compared to RL training. Nevertheless, Sumo can undoubtedly benefit from system-identification and model-learning methods that update object parameters on the fly from real-world interactions. Finally, Sumo, in its current form, does not leverage any human priors. Future work should explore incorporating pre-trained foundation models that can automatically guide robot behaviors without manually engineered rewards.
