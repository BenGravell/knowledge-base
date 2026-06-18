<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Barkour: Benchmarking Animal-level Agility with Quadruped Robots

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Animals have evolved various agile locomotion strategies, such as sprinting, leaping, and jumping. There is a growing interest in developing legged robots that move like their biological counterparts and show various agile skills to navigate complex environments quickly. Despite the interest, the field lacks systematic benchmarks to measure the performance of control policies and hardware in agility. We introduce the Barkour benchmark, an obstacle course to quantify agility for legged robots. Inspired by dog agility competitions, it consists of diverse obstacles and a time based scoring mechanism. This encourages researchers to develop controllers that not only move fast, but do so in a controllable and versatile way. To set strong baselines, we present two methods for tackling the benchmark. In the first approach, we train specialist locomotion skills using on-policy reinforcement learning methods and combine them with a high-level navigation controller. In the second approach, we distill the specialist skills into a Transformer-based generalist locomotion policy, named Locomotion-Transformer, that can handle various terrains and adjust the robot's gait based on the perceived environment and robot states.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Using a custom-built quadruped robot, we demonstrate that our method can complete the course at half the speed of a dog. We hope that our work represents a step towards creating controllers that enable robots to reach animal-level agility.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

There has been a proliferation of legged robot development inspired by animal mobility. Recent notable examples include the ETH ANYmal, the MIT Mini Cheetah, the KAIST RaiBo, Unitree A1/Go1, and the Boston Dynamics Spot robots. An important research question in this field is how to develop a controller that enables legged robots to exhibit animal-level agility while also being able to generalize across various obstacles and terrains. Through the exploration of both learning and traditional control-based methods, there has been significant progress in enabling robots to walk across a wide range of terrains. These robots are now capable of walking in a variety of indoor and outdoor environments, such as up and down stairs, through bushes, and over unpaved roads and rocky or even sandy beaches.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite advances in robot hardware and control, a major challenge in the field is the lack of standardized and intuitive methods for evaluating the effectiveness of locomotion controllers. Ad-hoc metrics are often used to present results, which complicates the comparing of results. To address this issue, it is essential to establish metrics that can accurately measure robot agility and to define a standard set of tasks that can serve as a common evaluation framework, similar to how the DeepMind Control Suite has been widely adopted in the field of reinforcement learning (RL).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A good benchmark set for agile legged locomotion should be non-trivial or not easily exploitable, and require a diverse set of primitive behaviors that quadrupeds showcase in real environments. Well-established benchmarks already exist to measure animal performance, for example, dog agility competitions. In these competitions, participants race their dogs through a pre-set obstacle course. A variety of obstacles including weave poles, jumps, tunnels, an A-frame, a seesaw, and a pause table test diverse locomotion skills. The performance is evaluated based on time, and there are penalties for errors such as completing obstacles in the wrong order, tackling an obstacle from the wrong direction, or touching the jump bars while leaping.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inspired by dog agility competitions, we introduce Barkour (Fig. 1), a challenging parkour course designed specifically for quadruped robots. We propose Barkour as a comprehensive benchmark suite for evaluating the agility of legged robots. We select a few representative obstacles (the weave poles, an A-frame, a jump board, and starting/ending pause tables) and fit the setup in a $25\ m^{2}$ area. We design an agility scoring system inspired by the dog competition rules: to get a high score, the legged robot must complete the entire Barkour course within a time limit determined by the configuration of the obstacles. The faster the robot, the higher the final score.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To solve the tasks in our Barkour benchmark suite, we introduce a simulation setup and two learning-based baselines as references. Our first approach involves training specialist policies in simulation that can overcome each individual obstacle. The specialist policies are then orchestrated by a high-level navigation controller that selects the appropriate specialist policy based on the location of the robot. In our second approach, we take inspiration from recent work on training generalist agents and develop a transformer-based generalist locomotion policy, named *Locomotion-Transformer*, which tackles all Barkour obstacles using a single policy network. To demonstrate the effectiveness of the learned agile skills, we deploy the simulation-trained policies in a zero-shot manner on a custom-built quadruped robot in a real-world Barkour setup.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

A benchmark (*Barkour*) for agile quadruped robot locomotion inspired by dog agility competitions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Two learning-based approaches (specialist and generalist (*Locomotion-Transformer*) policies) that can complete the benchmark agilely which can serve as baselines to benchmark future algorithms.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

A detailed analysis of zero-shot sim-to-real transfer using a custom-built quadruped robot.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Barkour benchmark for measuring agility", "weight": 1.0} -->

Making robots move like animals or humans is a goal shared by many researchers in the robotics community. Animals and their behaviors have been an inspiration for many robots. In this work we aim to make this connection quantitative by introducing Barkour, an agility benchmark that assesses the overall agility skills of quadruped robots. The Barkour benchmark is inspired by dog agility competitions, which we believe provides a setting to quantitatively evaluate small to medium-sized quadruped robots. Dogs exhibit a wide range of agile locomotion skills and behaviors and dog agility events have well-defined rules. Dog agility competitions capture a diverse set of skills and have clear metrics based on timing and behaviors to compare performances of different dogs. A careful design of obstacles, metrics, and coverage of skill diversity is also crucial for creating a benchmark for robotics. Hence, we reuse many elements common to dog agility competitions: obstacle definitions, a time-based metric, and penalties for rules violations.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Barkour benchmark for measuring agility", "weight": 1.0} -->

We use an area of $5\ m$ $\times$ $5\ m$ within which we place four unique obstacles (Fig. 2). This is a denser setup with a smaller footprint than a typical dog competition to allow for repeated deployment in a standard robotics lab. We chose the obstacle types that provide diversity over required primitive skills such as running, sideways movement, climbing and jumping, while keeping the smaller footprint. Starting from the start table, the robot must weave through a set of poles, traverse an A-frame, jump across a broad jump and then make its way onto the end table. All obstacles are fixed in place.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Barkour score", "weight": 1.0} -->

The *agility score* $R_{\text{agility}}$ measures how fast a robot can successfully complete all obstacles in Barkour. The score is calculated based on real dog competitions^22^2Regulations for Agility Trials and Agility Course Test (ACT) rules/scoring from the American Kennel Club (AKC). See standard course time for 8-inch Division Novice A and B Agility Standard Class. with some simplifications. A score of $1.0$ indicates that the robot solved the entire course within *allotted course time* $t_{\text{allotted}}$. Starting from $1.0$, the robot can receive two types of deductions: a $0.1$ penalty for each failed or skipped obstacle and a $0.01$ penalty for each full second the robot exceeds $t_{\text{allotted}}$. An episode is completed when the robot reaches the end table, otherwise it is terminated when $R_{\text{agility}}$ reaches $0$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Barkour score", "weight": 1.0} -->

The score^33^3Typically represented as $\lbrack{0 - 100}\rbrack$ points in real dog competitions.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Barkour score", "weight": 1.0} -->

The allotted course time is the sum of the *nominal size* $d_{\text{obstacle}}$ of each obstacle, divided by the target average speed. The nominal size is an estimate of the length of typical trajectory to complete a given obstacle, including the distance leading up to and away from it. Based on the rule book for real dog competitions and the size of the robot, we set the target average speed to $v_{\text{target}} =$$1.69\ {m\ s^{- 1}}$. This target average speed can be scaled up for larger robots.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Barkour score", "weight": 1.0} -->

In the context of this paper, we consider four types of obstacles with nominal obstacle sizes and allotted times given in Table I. Appendix -B provides detailed definitions of each type of obstacle, including the physical setup, acceptance criteria, etc.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Barkour score", "weight": 1.0} -->

Note that real dog competitions often include other types of penalties (e.g., smaller deductions if a dog retries an obstacle), whereas Barkour only deducts points for failed/skipped obstacles or excess time. This makes implementing the scoring mechanism in both sim and real much easier and significantly less error prone.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Barkour score", "weight": 1.0} -->

In this work, we chose a small area with a small number of obstacles and simpler metrics for ease of repeated and controlled hardware experimentation, and kept diversity of skills and measurability as high priorities. As is the case for real dog agility competitions, our proposed metric, environment, and simulation setup can be easily adapted to a different number of obstacles, a larger area, or other variables.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Two Baseline Solutions", "weight": 1.0} -->

One goal of this work is to demonstrate that by working towards our proposed Barkour benchmark, we can advance our techniques and insights in obtaining controllers with better agility. To achieve this, we present two learning-based methods to synthesize agile controllers for a real quadruped robot and establish baselines for the proposed Barkour benchmark. An overview of the two learning methods is shown in Fig. 3.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Two Baseline Solutions", "weight": 1.0} -->

In the first baseline, we train three specialist policies for different tasks in a physics simulation with an on-policy Reinforcement Learning algorithm (Section IV-A). Each specialist policy is trained with a reward function and a terrain curriculum tailored to the corresponding task. We apply domain randomization for transferring the simulation-trained policies to the real world. We then design a high-level navigation controller (Section IV-C) that switches between different specialist policies and generates velocity commands for the specialist policies to overcome different obstacles.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Two Baseline Solutions", "weight": 1.0} -->

In the second baseline, we train a single generalist policy that can handle all Barkour tasks. To achieve this, we collect a dataset with all the specialist policies and distill them into a unified Transformer-based locomotion policy, which we name Locomotion-Transformer. We then combine Locomotion-Transformer with a simplified navigation controller that only needs to provide the waypoints for the low-level policy to tackle the full obstacle course.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-A Specialist Policy Learning", "weight": 1.0} -->

Our first baseline trains three specialist policies to cover all the core agility skills required in the Barkour benchmark: fast omni-directional walking on uneven terrain, climbing up and down a slope, and jumping over a board. The first policy is used to solve the start/end tables and weave pole tasks, the second solves the A-Frame task, and the third solves the Broad Jumping task. All the specialist policies are trained using PPO in LeggedGym, which uses the GPU-powered NVidia IsaacGym. Specialist model architecture details can be found in Appendix -H. We also investigated the TPU-powered Brax simulator for training, as presented in Appendix -L.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-A1 Observation and Action Space", "weight": 1.0} -->

The observation space of the specialist policies include desired base velocities $\overline{v} = {(\overline{v_{x}},\overline{v_{y}},\overline{\omega_{z}})}$, robot proprioceptive information $s^{\text{p}} = {(\mathbf{g},\theta,\omega_{z})}$, terrain perception $s^{\text{v}}$, and the last robot action $a_{t - 1}$, where $\overline{v_{x}},\overline{v_{y}},\overline{\omega_{z}}$ are the desired linear velocity (front/back, left/right) and the desired angular velocity in yaw in the robot's local frame, $\mathbf{g}$ is the projected gravity vector in the robot local frame, $\theta$ is the robot joint angles, and $\omega_{z}$ is the yaw velocity.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-A1 Observation and Action Space", "weight": 1.0} -->

Given that we are working with a partially-observable system (POMDP), we further include a observation history of length $0.3\ s$ for the robot proprioception.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-A1 Observation and Action Space", "weight": 1.0} -->

In our approach, perception is modeled as a heightfield in the vicinity of the robot following the method used by Miki et al. To construct the heightfield $s^{\text{v}}$, we select a grid of locations on the terrain surrounding the robot and measure their relative heights with respect to the center of the robot's torso. This grid translates and rotates with the robot, always maintaining alignment with its heading. The shape of the heightfield is customized to suit the requirements of each task, which are elaborated in the corresponding sections below.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-A1 Observation and Action Space", "weight": 1.0} -->

We choose the action space to be the target motor angles measured from a nominal standing pose.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-A2 Reward Function", "weight": 1.0} -->

Similar to Rudin et al., our reward function consists of multiple terms that fall into two categories: Task and Regularization. Task rewards encourage the robot to perform the desired skills, such as running forward or turning, while regularization rewards shape the behavior of the robot, such as low energy consumption and high stability. Section -H lists the reward terms that we use in this work.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A3 Omni-directional Walking Policy", "weight": 1.0} -->

The Omni-directional Walking Policy (OWP) is trained to follow a velocity command in all directions on uneven terrains. It demonstrates the ability of the controller to quickly adjust the speed profile and the robot's orientation, which are critical skills for the weave pole and pause table tasks.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A3 Omni-directional Walking Policy", "weight": 1.0} -->

OWP takes all three categories of observations as input and is trained with randomly sampled velocity commands. The training environment for OWP follows the general uneven terrain curriculum designed by Rudin et al, which consists of mild slopes, stairs, and random steps. Please refer to Appendix -E for details of the observation space, the velocity sampling, and the reward structure.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A4 Slope Climbing Policy", "weight": 1.0} -->

For the A-frame task, the robot must agilely climb up and down a $30\ {^\circ}$ slope. Due to the large angle of the slope, the robot operates near the limit of available traction. It needs to precisely manage the trade-off between its speed and its ability to maintain friction with the ground. We find that simply including the target slope terrain during OWP training cannot solve this task.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A4 Slope Climbing Policy", "weight": 1.0} -->

To tackle this task, we train a specialized Slope Climbing Policy (SCP). SCP shares the same observation space, actions space, and reward function as OWP. However, it differs from OWP training in two aspects. First, SCP is trained with a curriculum of increasing slope angles from $5\ {^\circ}$ to $33\ {^\circ}$, as shown in the leftmost simulation image in Fig. 3. Second, since the key skill required in the A-Frame task is to climb up and down the slope, we can focus the training on moving agilely in the frontal direction instead of training the policy to move fast in all directions. For details on the terrain curriculum and the training config, see Appendix -F.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A5 Jumping Policy", "weight": 1.0} -->

In the jumping task, the robot needs to jump over a board that is $0.5\ m$ long, which is longer than its body. This requires not only moving fast, but also stepping precisely (as close to the broad jump as possible, but not on it). To train the Jumping Policy (JP), we use a 3-stage curriculum, including flat terrain running, gap training, and fine-tuning with more randomizations (Appendix -G).

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A6 Domain Randomization", "weight": 1.0} -->

To bridge the sim-to-real gap, we employ the technique of domain randomization. The randomized parameters are listed in Table II. We find that the default domain randomization scheme designed by Rudin et al. works well when the robot velocity is relatively low (slower than $1\ {m\ s^{- 1}}$). However, for more agile motions, such as jumping or slope climbing, where the speed of the robot can exceed $2\ {m\ s^{- 1}}$, we observe a notable sim-to-real gap. To overcome this challenge, we incorporate additional randomization including torso inertia, motor modeling, and joint static friction. Torso inertia randomization enables the agent to better control the orientation of the body at high speed, and motor modeling and joint static friction are known important factors for quadruped sim-to-real. We find these to be critical for successful transfer of policies to the real hardware.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B Locomotion-Transformer: A Generalist Locomotion Policy", "weight": 1.0} -->

Our second baseline aims to train a single generalist locomotion policy that can tackle all obstacles, thereby removing the necessity for ad-hoc switching between individual specialist policies and promoting generalization capabilities to different obstacle and terrain configurations. Our generalist policy, *Locomotion-Transformer*, is trained by distilling the specialist policies via behavioral cloning with a Transformer sequence model, similar to. Although prior work has demonstrated that generalist policies can also be learned via reinforcement learning by simultaneously training on multiple environments, the diverse curricula and reward structures in our problem setting makes it challenging.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B1 Data Collection", "weight": 1.0} -->

Collecting the right interaction data that covers the state distribution on which the policy is going to operate is critical to successful policy distillation. To learn the generalist, we collect an offline dataset by rolling out individual specialist policies in simulated environments that are same as the training settings of the specialist. We collect $17,636$ simulated episodes, equivalent to $57.58$ hours of robot time, across four different types of environments: random steps, stairs, gaps, and slopes. More details on the data collection setup used in this work and a data card (Table VI) can be found in Appendix -J.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B2 Transformer Model", "weight": 1.0} -->

$s^{\text{v}}$ contains all types of heightfields that are originally designed for each individual environment (see details in Section IV-A). The model predicts the next action $a_{t}$ at the last position, and is trained on an L2 regression loss. We tokenize the most recent elevation image with a two-layer convolutional encoder network for each type of heightfield. The proprioceptive states (along with the velocity commands) and actions are each tokenized with one projection layer. We use a context window of $0.3$s, the same as in the specialist policy, which amounts to a size of $W = 15$. For terrain perception, we combine both heightfields from OWP and JP to cover the terrain near and in front of the robot. We use ReLU activation to encode each observation input. The model architecture hyperparameters can be found in Appendix -K.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-C High Level Navigation Controller", "weight": 1.0} -->

The specialist policies allow the quadruped to tackle different individual obstacles. However, to complete the Barkour benchmark, the robot must also make decisions on how to navigate the field and transition between behaviors while following specific rules of the obstacle course. To achieve this, we design a high-level state machine-based navigation controller to command our locomotion policies and guide the robot through the entire course. The navigation controller has access to the full state of the environment and the ground truth robot pose, and outputs appropriate velocity commands for the robot.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-C High Level Navigation Controller", "weight": 1.0} -->

Specifically, we place a sequence of waypoints around the obstacles that serve as sub-goals to guide the robot through each obstacle in the Barkour benchmark. Each waypoint specifies a desired position and heading orientation for the robot to reach. Every timestep, the high-level navigation controller computes linear and angular velocity commands to take the robot to the desired poses. An error tolerance is also encoded in each waypoint to determine when to switch to the next waypoint. When using the specialist policies, each waypoint also includes a behavior type to dictate which specialist policy to use. On the other hand, the generalist Locomotion-Transformer policy only needs the velocity commands. More details about this calculation can be found in Appendix -I.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Robot Hardware", "weight": 1.0} -->

Exploring the influence of the Barkour benchmark on enhancing the agility of quadruped robots necessitates considerable controller development and thorough real hardware experimentation. This poses significant challenges on the reliability and repeatability of the robot hardware, especially given the highly agile movements we strive. Moreover, quadruped animals exhibit diverse body configurations compared to typical quadruped robots, which can significantly affect their capacity for agile motion. Consequently, we believe that hardware optimization and customization are critical in bridging the agility gap between legged robots and their animal counterparts.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Robot Hardware", "weight": 1.0} -->

As a result, we developed a small quadruped robot in-house to evaluate its learned agile skills using the Barkour benchmark. The robot (Fig. 5) is similar in size to the Unitree A1 and MIT Mini-Cheetah robots. The robot weighs $11.5\ {kg}$, and has $220\ {mm}$ upper limbs and $190\ {mm}$ lower limbs. The front-to-back hip-to-hip distance is $380\ {mm}$ and the distance between the left and right legs is $290\ {mm}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Robot Hardware", "weight": 1.0} -->

We use T-Motor -6 actuators, which are controlled by Elmo G-/100SE2S motor drivers running at $24\ V$. The actuators provide a peak output torque of $12\ {N\ m}$ at each joint.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Robot Hardware", "weight": 1.0} -->

For our experiments, we use both the robot's onboard sensors (Parker 3DMCX5-AHRS IMU, joint position, velocity, torque) as well as an external motion capture system (Phasespace X2E) to track the robot's position and orientation in the obstacle course. We control the robot using an off-board workstation with two Intel Xeon Gold 6154 CPUs via a CAN bus connected to each leg. The learned policies send position commands at $50\ {Hz}$, and the PD control loop runs at $1\ {kHz}$. For all hardware experiments, the PD gains are set to ($20\ {N\ m\ {rad}^{- 1}}$, $0.5\ {N\ m\ s\ {rad}^{- 1}}$).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Robot Hardware", "weight": 1.0} -->

As part of the development of the benchmark and methods, we evaluated approximately 3600 Barkour attempts across two robots, which corresponds to about 24 hours of continuous operation time and approximately $60\ {km}$ of robot moving distance.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Experiments and Discussions", "weight": 1.0} -->

We evaluate the specialist and generalist policies within our hierarchical control framework on Barkour tasks.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Experiments and Discussions", "weight": 1.0} -->

*Is Barkour a good benchmark for agility?*

<!-- chunk {"id": "body-0047", "role": "body", "section": "Experiments and Discussions", "weight": 1.0} -->

*Can we solve Barkour benchmark using the frameworks proposed in Section IV and how does it compare to animal agility?*

<!-- chunk {"id": "body-0048", "role": "body", "section": "Experiments and Discussions", "weight": 1.0} -->

*How important are the design choices we made during specialist and generalist policy training?*

<!-- chunk {"id": "body-0049", "role": "body", "section": "VI-A Why Barkour as a Benchmark", "weight": 1.0} -->

The benchmark is effective for several reasons. Firstly, it requires diverse motion capabilities to complete the course, which effectively exposes potential limitations on agile skill discovery. Secondly, the benchmark effectively tests the maneuverability and control precision of the locomotion controller at high speeds due to the complex routes required to finish the course as illustrated in Fig. 6, and scoring being tied to the completion time of the course. In the event that the robot misses the correct gate in the weave poles section, touches the jump board, or if the robot is too slow, the overall score is penalized. Lastly, we found that the benchmark is well-suited for real animal counterparts, as demonstrated in our experiments involving two small dogs. The comparison between the performance of the real dogs and robots highlights opportunities for improvement in both hardware (such as the need for flexible spines) and algorithmic approaches. It is worth noting that the real dogs never failed to complete any of the obstacles and were significantly faster than our provided baselines.

<!-- chunk {"id": "body-0050", "role": "body", "section": "VI-B Barkour Evaluation using Combined Specialist Policies", "weight": 1.0} -->

First, we evaluate the performance of specialist policies combined on all Barkour tasks. We show a sample behavior of the robot in Fig. 6. In this run, the robot completes the course by traversing all of the obstacles in $20.4\ s$. While the robot completes all the obstacles, this specific run receives 0.91 agility score due to the extra time it took compared to the allotted time of $10.64\ s$. One can see that the robot completes the weave poles section at a $90\ {^\circ}$ angle, which is enforced by our high level controller, due to the narrow passages between the last few poles. The velocity of the robot during the same run is shown in Fig. 7. The robot's forward velocity varies between $0.5\ {m\ s^{- 1}}$ and $1\ {m\ s^{- 1}}$ during the weave poles. It reaches a velocity as high as $2.3\ {m\ s^{- 1}}$ during the jumping phase.

<!-- chunk {"id": "body-0051", "role": "body", "section": "VI-B Barkour Evaluation using Combined Specialist Policies", "weight": 1.0} -->

For comparison, we ran the same course with two small dogs: a Pomeranian/Chihuahua ($3.2\ {kg}$, $33\ {cm}$ height at withers) and a Dachshund ($4\ {kg}$, $20\ {cm}$ height at withers). After getting familiar with the course, they both reached a maximum score ($1.0$) by reaching the final pause table in approximately $9\ s$ (videos in supplementary).

<!-- chunk {"id": "body-0052", "role": "body", "section": "VI-B Barkour Evaluation using Combined Specialist Policies", "weight": 1.0} -->

We test the robustness of the hierarchical controller by running it $71$ times. Fig. 8 shows that the robot completes the course in most of these runs, while falling down or tipping over 6 times. In $40$ of the runs, the robot touches the jump board and still scores approximately $0.73$. In $25$ of these runs, the robot completes all 5 obstacles scoring $0.87$ on average. As shown in Table III, the mean score of all the runs is around $0.77$ with an average base forward velocity of $0.74\ {m\ s^{- 1}}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "VI-B Barkour Evaluation using Combined Specialist Policies", "weight": 1.0} -->

The decomposition of these runs (Table IV into the different obstacles shows that the specialist policies complete the weave poles at around the nominal (target) speed, while the broad jump is faster and the A-frame is slower. The robot completes the weave poles and A-frame with a 100% success rate, while the broad jump, requiring particularly more agile behavior, succeeds 38% of the time.

<!-- chunk {"id": "body-0054", "role": "body", "section": "VI-B1 Omni-directional Walking Policy", "weight": 1.0} -->

This policy is capable of producing consistent trotting motions in both simulation and real hardware. The motion is highly stable when the robot is commanded to move between ${- 1.5}\ {m\ s^{- 1}}$ and $1.5\ {m\ s^{- 1}}$ in the forward and backward directions and between ${- 1}\ {m\ s^{- 1}}$ and $1\ {m\ s^{- 1}}$ laterally with a yaw rate between ${- 2.5}\ {{rad}\ s^{- 1}}$ and $2.5\ {{rad}\ s^{- 1}}$ on flat ground. With the policy, the robot can step up and down steps of up to $0.1\ m$, which corresponds to about one third of the robot's standing height. During our $60$ specialist policy trials, OWP succeeds at the weave poles every time, taking $9.27\ s$ on average.

<!-- chunk {"id": "body-0055", "role": "body", "section": "VI-B1 Omni-directional Walking Policy", "weight": 1.0} -->

Compared with real dogs that can complete this section in less than $4\ s$, OWP takes significantly more time because the robot does not have a flexible spine, and the robot is much wider and has to re-orient itself sideways to fit the narrow passages between the poles.

<!-- chunk {"id": "body-0056", "role": "body", "section": "VI-B2 Slope Climbing Policy", "weight": 1.0} -->

This policy can run on the steep $30\ {^\circ}$ A-frame using a trotting gait while maintaining a speed of more than $0.6\ {m\ s^{- 1}}$. The same policy climbs down the A-frame reaching $1.5\ {m\ s^{- 1}}$. The policy exhibits consistent performance ($100\%$ success rate) regardless of variations in the initial position or angle of attack as long as the robot remains within the width of the A-frame.

<!-- chunk {"id": "body-0057", "role": "body", "section": "VI-B3 Jumping Policy", "weight": 1.0} -->

This policy demonstrates a bounding gait when traversing flat terrain. To clear the broad jump gap of $0.5\ m$, the robot accelerates from nearly stationary at a distance of $2\ m$ in front of the jump and reaches a velocity of $2.3\ {m\ s^{- 1}}$ at the jump. An example of the center of mass speed and trajectory can be observed in Fig. 7. In 38% of trials, the robot is able to clear the $0.5\ m$ gap, using its momentum to jump farther than would be possible with a standing jump. In most of the failure cases, the robot touches the edge of the jump board either before lift-off or after landing. A typical example of the policy on the broad jump obstacle is shown in Fig. 9.

<!-- chunk {"id": "body-0058", "role": "body", "section": "VI-C Barkour Evaluation using Locomotion-Transformer", "weight": 1.0} -->

We now evaluate the performance of the generalist policy, which is distilled using the data generated by the specialist policies. Unlike the combined specialist policies that require the high-level navigation policy to select which specialist policy to use, our Locomotion-Transformer model absorbs all the low-level skills of the specialists and thus can be deployed on the robot without explicit hints on which obstacle it is handling. Therefore, we use a simplified navigation policy that only outputs the velocity command to the policy during evaluation.

<!-- chunk {"id": "body-0059", "role": "body", "section": "VI-C Barkour Evaluation using Locomotion-Transformer", "weight": 1.0} -->

We evaluate Locomotion-Transformer on the real Barkour setup with $19$ trials, which can be seen in Figure 8. In general, we observe slightly lower performance for the Locomotion-Transformer policy compared to the combined specialist policies (also seen in Table III). A major reason for this is that the Locomotion-Transformer policy does not have information about the obstacle type being tackled and has to infer relevant information from terrain and proprioceptive observations, which increases the difficulties of the task.

<!-- chunk {"id": "body-0060", "role": "body", "section": "VI-C Barkour Evaluation using Locomotion-Transformer", "weight": 1.0} -->

On the other hand, we want to highlight two advantages of the generalist Locomotion-Transformer policy. First, by using a single generalist policy, we achieve smoother transitions between different obstacles. As seen in the supplementary video, when transitioning between different specialist policies, the robot may exhibit jerky motions when the previous specialist policy reaches a state that is unfamiliar to the following policy. Meanwhile, the Locomotion-Transformer achieves smooth transitions among different behaviors including different gaits.

<!-- chunk {"id": "body-0061", "role": "body", "section": "VI-C Barkour Evaluation using Locomotion-Transformer", "weight": 1.0} -->

Another advantage of the Locomotion-Transformer policy is that it's more general and flexible. By removing the reliance on explicitly knowing the obstacle type, the Locomotion-Transformer works for a wider range of environments without requiring domain expertise to specify which policy to use. To demonstrate the flexibility and generalization capability of Locomotion-Transformer, we adjusted the order of the Barkour obstacles to create a new course: the robot must perform fast $90\ {^\circ}$ turning, then go to the end of the A-Frame and perform the A-Frame task backwards. Next, the robot must do a broad jump towards the start table and climb up the table. With specialist policies, one would need to re-assign different policies to different sub-goals and fine-tune the transitions between different policies; the Locomotion-Transformer can generalize to this new route by simply providing a set of new sub-goals to denote the desired route. The results in Fig. 10 show that the robot succeeds in climbing the A-frame from the opposite end and going over the broad jump in a different location.

<!-- chunk {"id": "body-0062", "role": "body", "section": "VI-C Barkour Evaluation using Locomotion-Transformer", "weight": 1.0} -->

We have shown that the generalist Locomotion-Transformer policy is able to execute a wide range of high-level commands provided by a navigation controller and achieves a high Barkour score.

<!-- chunk {"id": "body-0063", "role": "body", "section": "VI-C Barkour Evaluation using Locomotion-Transformer", "weight": 1.0} -->

*Is the Transformer-based framework also capable of learning high-level behaviors*?

<!-- chunk {"id": "body-0064", "role": "body", "section": "VI-C Barkour Evaluation using Locomotion-Transformer", "weight": 1.0} -->

*Is it possible to train a Locomotion-Transformer policy from a hardware dataset*?

<!-- chunk {"id": "body-0065", "role": "body", "section": "VI-C Barkour Evaluation using Locomotion-Transformer", "weight": 1.0} -->

We answer these questions affirmatively in Appendix -D by training and deploying a course-specific Locomotion-Transformer policy from hardware data.

<!-- chunk {"id": "body-0066", "role": "body", "section": "VI-D Is Training Specialist Policies Necessary?", "weight": 1.0} -->

We have demonstrated that it is possible to train individual specialist policies for each task and distill them into one generalist policy to solve the Barkour benchmark. However, one question remains: *Is it possible to train a single agent using RL that combines the capabilities of all specialist policies subsection IV-A?*

<!-- chunk {"id": "body-0067", "role": "body", "section": "VI-D Is Training Specialist Policies Necessary?", "weight": 1.0} -->

To answer this question, we train a single multi-task policy using our IsaacGym-based training pipeline. We construct a training terrain curriculum by mixing the terrains from all three specialist policy types. During RL training, $50\%$ of the data are from the slope environment for training Slope Climbing Policy, $30\%$ are from the general uneven terrain for training Omni-directional Walking Policy, and $20\%$ are from the gap environment for the Jumping Policy. We follow the same curriculum for each terrain type as described in Section IV-A. We use the reward function from training the Omni-directional Walking Policy to obtain a policy that takes a velocity command as input.

<!-- chunk {"id": "body-0068", "role": "body", "section": "VI-D Is Training Specialist Policies Necessary?", "weight": 1.0} -->

We deploy the trained policy on the real robot and find that the resulting policy can robustly walk down the start table and finish the weaving pole task. However, it cannot climb up the A-Frame even though we have already adjusted the training data distribution to bias towards the slope task. This demonstrates that the steep slope necessitates the use of a specialist training. In addition, the policy cannot successfully perform the broad jump. This experiment also demonstrates the difficulties and diversity of the skills required to solve the proposed Barkour benchmark.

<!-- chunk {"id": "body-0069", "role": "body", "section": "VI-E Locomotion-Transformer Ablations", "weight": 1.0} -->

We investigate several design choices behind Locomotion-Transformer, including model architecture, model size, training dataset size, and context length. To enable rapid model iteration, we report PyBullet simulation Barkour scores. For each experiment, we train three models with different random seeds and report the mean and standard deviation of the respective mean evaluation scores.

<!-- chunk {"id": "body-0070", "role": "body", "section": "VI-E1 Model architecture", "weight": 1.0} -->

To understand if the transformer architecture is necessary, we trained an MLP (a larger version of the specialist policy architecture) on the same dataset. As shown in Fig. 11(a) ‣ Figure 11 ‣ VI-E Locomotion-Transformer Ablations ‣ VI Experiments and Discussions ‣ Barkour: Benchmarking Animal-level Agility with Quadruped Robots"), the distilled MLP policy performs substantially worse than the Transformer policy.

<!-- chunk {"id": "body-0071", "role": "body", "section": "VI-E2 Context length", "weight": 1.0} -->

In Fig. 11(b) ‣ Figure 11 ‣ VI-E Locomotion-Transformer Ablations ‣ VI Experiments and Discussions ‣ Barkour: Benchmarking Animal-level Agility with Quadruped Robots"), we show the Locomotion-Transformer performance with different context lengths. Using a longer context length is more effective, suggesting that the Transformer is able to leverage past state information.

<!-- chunk {"id": "body-0072", "role": "body", "section": "VI-E3 Dataset size", "weight": 1.0} -->

In Fig. 11(c) ‣ Figure 11 ‣ VI-E Locomotion-Transformer Ablations ‣ VI Experiments and Discussions ‣ Barkour: Benchmarking Animal-level Agility with Quadruped Robots"), we train Locomotion-Transformer models with 1%, 10%, and 100% of the training data. While 1% ($\sim$`<!-- -->`{=html}176 episodes) is insufficient for training a competitive policy, 10% ($\sim$`<!-- -->`{=html}1760 episodes) and 100% result in similar performance. We note that using a larger or more diverse dataset may lead to improved sim-to-real performance, which we leave as investigation for future work.

<!-- chunk {"id": "body-0073", "role": "body", "section": "VI-E4 Model size", "weight": 1.0} -->

Fig. 11(d) ‣ Figure 11 ‣ VI-E Locomotion-Transformer Ablations ‣ VI Experiments and Discussions ‣ Barkour: Benchmarking Animal-level Agility with Quadruped Robots") shows that increasing the size of the Locomotion-Transformer model can lead to improved performance, which mirrors similar results in other domains such as language. However, deploying these models on real robots places strict bounds on inference latency and therefore model size.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We present Barkour, a benchmark to evaluate the agility of quadruped robots. Inspired by dog agility competitions, Barkour is a testbed with an intuitive scoring mechanism that requires combination of various agile skills. Furthermore, it can be easily adapted to robots of various sizes or extended by adding or rearranging obstacles while retaining the same metrics.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Conclusion", "weight": 1.5} -->

To set a strong baseline and make progress towards the Barkour benchmark, we explore a learning-based sim-to-real approach and proposed two baseline solutions. In both solutions, we first train a set of specialist policies that excel at tackling individual tasks by leveraging recent developments in fast simulation techniques with on-policy RL algorithms. While in the first solution, we manually design a state machine to switch between different specialist policies. In the second solution, we distill these skills into a generalist Transformer-based policy, named Locomotion-Transformer, that can automatically and smoothly transition between different obstacles. Our results show that Locomotion-Transformer can exhibit multiple agile skills required by the proposed benchmark and can automatically switch between them depending on the sensed environment and the commands received from a high-level navigation controller. As a validation of our approach, we also demonstrate that the policies can generalize to other obstacle configurations.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We believe that providing a benchmark for legged robotics, especially for agility, is an important first step to quantify the progress towards animal-level agility for quadruped robots. The Barkour benchmark is far from solved. While our baseline solutions can reach a peak agility score of 0.91 and complete the course in approx. $20\ s$, an untrained dog achieved 1.0 agility score and can complete the course in about half the robot's time (approx. $9\ s$). There is still a big gap in agility between robots and their animal counterparts, as demonstrated in this benchmark. Additionally, the fact that state-of-the-art RL methods fail to learn a single policy to complete the course further underscored the complexity and value of Barkour as a benchmark. We believe that Barkour will serve the robotics community as an important testbed for different learning and control methods and different hardware designs.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Limitations and Future Work", "weight": 1.5} -->

Our proposed approach sets a strong baseline on the benchmark. However, as the scores reflect, Barkour is not fully solved and there is still notable room to push towards dog-level agility by improving speed and robustness. We believe that bridging this gap necessitates a collective endeavor from the research community, and the suggested Barkour benchmark can help effectively track this progress.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Limitations and Future Work", "weight": 1.5} -->

One limitation of the current proposed baseline methods is that we use privileged information such as the CAD model of the environment and the position of the robot (via a Motion-Capture system) in the world frame. An important future work direction is to explore Barkour using only on-board sensors for both low-level locomotion skills and high-level navigation controller.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Limitations and Future Work", "weight": 1.5} -->

An equally exciting direction for future research on Barkour is to evaluate the impact of modifications to robot hardware, different form-factors, and sensors on performance or training speed. Finally, we are also looking into evaluating Barkour in an interactive setting, closer to real-world dog agility competitions, with a human leading a robot through the course.
