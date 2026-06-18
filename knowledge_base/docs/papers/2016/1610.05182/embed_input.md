<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning and Transfer of Modulated Locomotor Controllers

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study a novel architecture and training procedure for locomotion tasks. A high-frequency, low-level "spinal" network with access to proprioceptive sensors learns sensorimotor primitives by training on simple tasks. This pre-trained module is fixed and connected to a low-frequency, high-level "cortical" network, with access to all sensors, which drives behavior by modulating the inputs to the spinal network. Where a monolithic end-to-end architecture fails completely, learning with a pre-trained spinal module succeeds at multiple high-level tasks, and enables the effective exploration required to learn from sparse rewards. We test our proposed architecture on three simulated bodies: a 16-dimensional swimming snake, a 20-dimensional quadruped, and a 54-dimensional humanoid. Our results are illustrated in the accompanying video at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

A newborn antelope attempts its first steps only minutes after birth and is capable of walking within half an hour. A human baby, when lifted so that its feet just graze the ground, will step in a cyclical walking motion. Nature provides clear examples of evolutionarily determined, innate behaviors of surprising complexity, and basic locomotor circuits are well-developed prior to any significant goal-directed experience. The innate structure simplifies the production of goal-directed behavior by confining exploration to stable and coherent, yet flexible dynamics.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the other hand, machine learning's recent success stories have emphasized rich models with weakly-defined prior structure, sculpted by large amounts of data. And indeed, several recent studies have shown that end-to-end reinforcement learning approaches are capable of generating high-quality motor control policies using generic neural networks. A key question is how to get the best of both worlds: to build modular, hierarchical components that support coherent exploration while retaining the richness and flexibility of data-driven learning.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Here, we aim to create flexible motor primitives using a reinforcement learning method. We explore an approach based on a general-purpose, closed-loop motor controller that is designed to be modulated by another system. When modulated by random noise, this low-level controller generates stable and coherent exploratory behavior. A higher-level controller can then recruit these motor behaviors to simplify the solution of complex tasks. As a result, it can learn effective control strategies given only weak feedback, including tasks where reward is only provided infrequently after completion of a goal (a natural description of many tasks).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our architecture takes inspiration from the division of labor in neurobiological motor control. Biological motor primitives are formed by spinal cord interneurons, which mediate both fast, reflexive actions and the elementary constituents of motor behaviors like locomotion and reaching. The spinal cord has direct sensory inputs that measure muscle tension and load, joint position, and haptic information from the skin. These sensory modalities are *proprioceptive* ("taken from near") because they carry information measured at close range to the body as opposed to the *exteroceptive* ("taken from afar") modalities like vision, audition and olfaction. Cortical motor neurons produce voluntary motor behavior primarily through the modulation of these interneuron populations.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Hierarchy*: The controller is subdivided into a low-level controller, which computes direct motor commands (e.g. joint torques), and a high-level controller, which selects among abstract motor behaviors.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Modulation*: The high-level controller outputs a signal that modulates the behavior of the low-level controller, through a communication bottleneck.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Information hiding*: The low-level controller has direct access only to task-independent, proprioceptive information. For the control problems considered in this paper, this proprioceptive information contains, for instance, the joint angles and velocities of the body and haptic information. Notably, it does not include information about absolute position or orientation in space or task-specific information such as a goal location. The high-level controller has access to all necessary proprioceptive and exteroceptive information.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Multiple time scales*: While the low-level controller operates at a basic control rate (i.e., it receives an observation and produces an action at every time step in the simulation), the high-level controller can operate at a slower rate, updating the modulatory control signal to the low-level controller less frequently.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

These design decisions are intended to create an abstraction barrier between the low and high levels: Separating the high level from the physics and detailed demands of motor actuation and likewise, sheltering the low-level controller from specific task objectives so it can acquire domain-general functionality. Below we present results demonstrating that our architecture solves several non-trivial control problems. A more detailed analysis of the implications of the design decisions listed above is, however, left for future work.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Architecture", "weight": 1.0} -->

We now describe the architecture of the hierarchical controller in greater detail (see Fig. 1). The setup is the standard agent-environment interaction model. At each point in time $t$, an agent executes an action $a_{t}$, and subsequently receives a reward $r_{t}$ and a new observation $o_{t + 1}$. Its goal is to maximize the expected sum of discounted future rewards $R_{t} = {\sum_{t^{\prime} = t}^{\infty}{\gamma^{t^{\prime} - t}r_{t^{\prime}}}}$, known as the *return*.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Architecture", "weight": 1.0} -->

The agent is characterized by a policy $\pi$ with parameters $\theta$ which specify a distribution over actions as a function of the history $h_{t} = {(o_{1},a_{1},{\ldotso_{t - 1}},a_{t - 1},o_{t})}$, i.e. $a_{t} \sim \pi{( \cdot |h_{t};\theta)}.$^11^1In this work, we did not find it necessary to include the actions in the history and left them out. The stochastic policy is defined by the composition of networks for the high-level controller $F_{H}$ and low-level controller $F_{L}$. This combined network outputs the parameters of the action distribution $\pi$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Architecture", "weight": 1.0} -->

In the experiments below, actions are multi-dimensional, and we parameterize the action distribution as a factorized Normal distribution with mean and variance being functions of $h_{t}$: $a_{t} \sim \pi{( \cdot |h_{t})} = \mathcal{N}{( \cdot |\mu{(h_{t})},\sigma^{2}{(h_{t})})}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Architecture", "weight": 1.0} -->

where $o_{t}^{F}$ is the full observation (including task-specific information), $z_{t}$ is the recurrent state of the high-level controller, $K$ is the control interval, and $\tau{(t)}$ is the most recent update time for the high-level control signal.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Learning locomotor controllers with policy gradients", "weight": 1.0} -->

We use an actor-critic policy gradient framework for learning during pre-training as well as transfer. We consider both fully observed (MDPs) and partially observed problems (POMDPs).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Generalized advantage estimation", "weight": 1.0} -->

We perform gradient ascent in the expected discounted return $J = {{\mathbb{E}}\left\lbrack R_{0} \right\rbrack}$, where the expectation is taken with respect to the trajectory distribution induced by the policy and the environment dynamics.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Generalized advantage estimation", "weight": 1.0} -->

We also use estimates of the return $R_{t}^{\lambda^{\prime}}$ as targets for the value function, so that the loss for value function training is

<!-- chunk {"id": "body-0019", "role": "body", "section": "Generalized advantage estimation", "weight": 1.0} -->

Note that we allow for different values of $\lambda$ and $\lambda^{\prime}$ for computing the policy and value function updates, respectively. Additionally, although each $R_{t}^{\lambda^{\prime}}$ nominally includes value function terms dependent on $\omega$ from future time steps, we do not differentiate with respect to them, as is typical for temporal difference learning.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Policy gradient with hierarchical noise", "weight": 1.0} -->

The policy gradient framework outlined above performs on-policy learning where the stochasticity of the policy is used for exploration. Choosing the action distribution $\pi$ to be a diagonal Gaussian is common due to its simplicity. At the same time, as we will demonstrate below, it can lead to very poor exploratory behavior, especially in high-dimensional action spaces. Due to its restricted form, it is unable to describe correlations across action dimensions or time steps. Actuating physical bodies with this form of white noise tends to produce undirected, twitchy movements that are attenuated by the second-order dynamics of the physics.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Policy gradient with hierarchical noise", "weight": 1.0} -->

In contrast, our low-level controllers are feedback controllers that produce pre-trained locomotor behavior. Modulating this behavior appropriately can lead to exploratory behavior that is more consistent in space and time. Thus, we allow stochasticity not only at the output of the low-level controller but also in the high-level controller. More precisely, in transfer training we treat the high-level controller as a stochastic network where

<!-- chunk {"id": "body-0022", "role": "body", "section": "Policy gradient with hierarchical noise", "weight": 1.0} -->

This hierarchical model can be optimized in different ways.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Policy gradient with hierarchical noise", "weight": 1.0} -->

Since we have knowledge of $\epsilon_{\tau}$, we can now evaluate ${{\nabla_{\theta}\log}\pi}{(\left. a_{t} \middle| {z_{\tau},\epsilon_{\tau}} \right.)}$, which would otherwise be difficult for a latent variable model. The policy gradient estimate in equation is simply formed by backpropagating directly into the high-level controller.^22^2 Using a value function for bootstrapping in combination with hierarchical noise requires extra care since $c_{t}$ affects future primitive actions. This could be accounted for by making $V$ dependent on $c_{t}$, or by bootstrapping only after resampling $c_{t}$. In our experiments we ignore this influence on the value and use $V{(h_{t};\omega)}$ as above.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Policy gradient with hierarchical noise", "weight": 1.0} -->

This high-level noise can achieve a dramatically different effect from i.i.d. noise added to each action dimension independently at every time step. Since the high-level noise is held constant over the high-level control interval and transformed by the low-level controller, it induces spatially and temporally correlated stochasticity at the primitive action level.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate our framework on three physical domains: a swimming snake, a quadruped and a humanoid. The snake has 6-links with a 5 dimensional action space and can propel itself forward by exploiting frictional forces. The quadruped has a 8 dimensional action space with two joints per leg. The humanoid has 21 action dimensions. For the following motor control problems, the core challenge is to learn basic locomotion. For more complex behaviors like navigation, the locomotion pattern can be reused. In addition to the description below, we encourage the reader to watch the supplemental videos^33^3High-quality version at

<!-- chunk {"id": "body-0026", "role": "body", "section": "Training methodology", "weight": 1.0} -->

We train our hierarchical motor controller on a simple *pre-training* task, and then evaluate its performance in one or more *transfer* tasks. This involves training the low-level controller (which will be re-used later) jointly with a provisional high-level controller which provides task-specifc information during pre-training and hence ensures controllability of the low-level controller. The pre-training task, which facilitates the development of generic locomotion skills, is described by an informative shaping reward and requires the controller to move each creature from a random initial configuration to a randomly positioned target.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Training methodology", "weight": 1.0} -->

After pre-training the provisional high-level controller is discarded and the weights of low-level controller are frozen. For each transfer task a new high-level controller is trained to modulate the inputs of the frozen low-level controller. The transfer tasks are most naturally described by *sparse* reward functions which are zero everywhere except at goal states. In order to obtain any reward, these tasks demand temporally-extended, structured exploration, posing a significant challenge for reinforcement learning methods. We use multiple transfer tasks for each domain to test the versatility of the learned low-level controllers.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Training methodology", "weight": 1.0} -->

We implemented our experiments using the asynchronous actor-critic framework introduced. For each experiment and architecture (pre-training and transfer), we perform a coarse grid search over the following hyper-parameters: learning rate, relative scaling of learning rate for the value function, $\lambda$, $\lambda^{\prime}$, and the length of the backpropagation-through-time truncation window. Unless noted otherwise we report results for the hyper-parameter setting which performed best over an average of 5 repeated experiments.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Training methodology", "weight": 1.0} -->

Depending on the transfer task we compare learning with the pre-trained low-level controller to learning a feedforward (*FF*) or recurrent policy (*LSTM*) from scratch; and we also compare to re-using a pre-learned FF network where we only learn a new input layer (*init FF*; the new input layer is to account for the fact that the observation space may change between pre-training and transfer task, or that the new task requires a different mapping from observations to motor behavior).

<!-- chunk {"id": "body-0030", "role": "body", "section": "6-link snake", "weight": 1.0} -->

Pre-training task The pre-training task initializes the snake at an origin with a random orientation and a random configuration of the joint angles. It is required to swim towards a fixed target over 300 time-steps, which requires being able to turn and swim straight. The low-level controller's sensory input consists of the joint angles, the angular velocities, and the velocities of the 6 segments in their local coordinate frames. The provisional high-level controller is also exposed to an egocentric (i.e., relative to the body frame) representation of the target position. A shaping reward in the form of the negative of the distance to the target is given at every step. The modulatory input from the high-level controller to the low-level controller is updated every $K = 10$ time steps.

<!-- chunk {"id": "body-0031", "role": "body", "section": "6-link snake", "weight": 1.0} -->

Analysis of the locomotor primitives The training task is easily solved. To assess the locomotor primitives embodied by the learned low-level controller, we remove the high-level controller and modulate the low-level controller with i.i.d. Gaussian noise sampled every 10 steps. The resulting behavior, obtained by initializing the swimmer at the origin in a random configuration and running for 4000 time steps, is shown in Figure 3. Using the center of the most anterior body segment as a reference point, swimming trajectories are shown. Clearly, the locomotor primitives produce coherent swimming behavior, and the nature of the input noise determines the structure of the behavior. In the absence of high-level modulation, the snake swims nearly straight; increasing the amplitude of modulatory noise leads to more variable trajectories. For comparison, we also show the behavior elicited by the commonly used zero-mean i.i.d. Gaussian noise applied directly as motor commands, which produces barely any displacement of the body, even at high noise levels.

<!-- chunk {"id": "body-0032", "role": "body", "section": "6-link snake", "weight": 1.0} -->

The largest standard deviation we tested was 0.8, which is large compared to the action range $\lbrack{- 1},1\rbrack$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "6-link snake", "weight": 1.0} -->

Transfer task 1: Target-seeking The first transfer task is a partially-observed target-seeking task with a sparse reward function (see Fig. 2, left). The high-level controller egocentrically senses the vector from head to the green target region's center but only when the target center is within $\pm 60^{\circ}$ of the head direction. At the beginning of each episode, both the snake and target are deposited at random, with a minimum distance between them. To solve this task, the snake needs to learn a strategy to turn around until it sees the target and then swim towards it. Each episode lasts 800 time steps, and reward is delivered when the snake's head is within the target region.

<!-- chunk {"id": "body-0034", "role": "body", "section": "6-link snake", "weight": 1.0} -->

Transfer task 2: Canyon traversal The snake must swim through a simple canyon (Fig. 2, right). Perceptual input to the high-level controller is given in the form of a $10$ pixel strip from an egocentric depth camera attached to the head. A positive reward is received when the swimmer has successfully navigated from start to end. An episode is terminated 25 steps after the snake's head has passed the canyon exit or after 3000 steps, whichever comes first.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Quadruped", "weight": 1.0} -->

Pre-training task Like the snake, the quadruped is initialized in a random orientation at the origin and must move to a target positioned randomly in its vicinity. The reward at each step is the (negative) distance to the target, and an episode lasts for 300 steps. The 34-dimensional input to the low-level controller is formed by the joint angles and angular velocities, the output of contact sensors attached to the legs and the ball-shaped torso, the velocity of the torso (translational and rotational) in the coordinate frame of the torso, and a 3-dimensional feature indicating the deviation of the torso's north pole from the z-axis. The high-level controller additionally receives the relative position of the target (36 dimensional input in total) and communicates with the low-level controller every 10 steps.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Quadruped", "weight": 1.0} -->

Analysis of the locomotor primitives Figure 6 provides an analysis of the behavior of the quadruped when actuated with i.i.d. Gaussian motor noise (left three plots) versus the randomly-modulated locomotor primitives (right four plots). Like the results shown for the snake in Figure 3, it is clear that the low-level controller achieves much better coverage of the space.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Quadruped", "weight": 1.0} -->

Transfer task 1: Target-seeking The quadruped has to move to a random target as quickly as possible. Reward is given when the quadruped's torso is inside the green region. Episodes last for 600 steps. The difficulty of the task can be varied by adjusting the minimum initial distance between the quadruped and the target; if this distance is large, exploration becomes a key challenge. We evaluated the pre-learned low-level controller on two difficulty levels of the task, one with small minimum initial distances and one with large minimum distances, respectively. In both cases, the newly learned high-level controller receives the relative position of the target in addition to the proprioceptive features provided to the fixed low-level controller.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Quadruped", "weight": 1.0} -->

Transfer task 2: Soccer The quadruped is placed with a ball inside a walled pitch, as shown in Figure 5. To receive a reward, it needs to manipulate the ball into the red "goal zone," which consists of two half-circles covering the floor and the back wall of the pitch. The goal zone has higher friction than the rest of the pitch to prevent the ball from simply bouncing away (simulating a goal net), and there is a small resistance that needs to be overcome when the ball is pushed into the zone while on the floor.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Quadruped", "weight": 1.0} -->

We consider two versions of the task that differ in their initial conditions. In a restricted version the quadruped and ball are positioned and oriented randomly in non-overlapping areas close to the center line of the pitch. The initial position for the ball is closer to the goal than that of the quadruped. In the less restricted version both ball and quadruped can be initialized further away from the center line and the ball can be placed further away from the goal than the quadruped so that the quadruped has to move away from the goal to position itself behind the ball. Note that even in the restricted version the quadruped is not necessarily facing the goal after initialization.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Quadruped", "weight": 1.0} -->

The high-level controller senses the proprioceptive features alongside features indicating the relative displacements from both the ball and center of the goal and the velocity of the ball in the body frame. Reward is only provided when the ball has graced the goal zone. From this sparse feedback, the quadruped must learn both how to navigate to the ball and also how to manipulate the ball into the goal zone. The task poses a severe exploration problem to the quadruped as solutions of the two subtasks are not guided by shaping rewards.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Quadruped", "weight": 1.0} -->

The results for the transfer tasks are shown in Figure 7. For the target-seeking task, we show results for the two different levels of difficulty. The hierarchical policy with pre-trained locomotor primitives very rapidly learns to solve both task variants. In contrast, a policy that is trained from scratch only learns a satisfactory solution to the simpler version. Very little progress is made on the hard version of the task over the 200,000 episodes shown due to the very sparse learning signal and poor exploration.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Quadruped", "weight": 1.0} -->

The hierarchical policy with locomotor primitives also makes good progress on the soccer task. For the restricted version of the task quantitative results are shown in Figure 7c. We obtain players that learn to score goals for many initial configurations of the quadruped and ball. Attempts to solve the soccer task from scratch do not succeed. For the more challenging version learning is slower and results are more sensitive to initial conditions and learning parameters. Nevertheless, we obtain several players that fetch the ball, pursue it if necessary, and score (see video).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Humanoid", "weight": 1.0} -->

In a final set of experiments, we applied the approach to a particularly challenging 27 degree-of-freedom control problem: the humanoid model shown in Figure 8. With 21 actuators the problem is much higher dimensional than the others. Moreover, whereas the snake and quadruped are passively stable, keeping the humanoid from falling is a non-trivial control problem in itself.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Humanoid", "weight": 1.0} -->

Pre-training task The training task consists of a simple multi-task setup: In every episode the humanoid is initialized in a standing position facing in the direction of the x-axis and is required to either move straight, or follow a leftward or a rightward circle of a fixed radius (5m). The reward function consists of a small quadratic control penalty, a positive constant stay-alive reward, the velocity in the desired direction (forward or along the circle) clipped at 2.5m/s, and, for the circle tasks, a quadratic penalty for deviating from the desired distance to the center point of the circle. Episodes last for up to 300 steps but are terminated when height of the humanoid falls below 0.9m.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Humanoid", "weight": 1.0} -->

The input to the low-level controller consists of proprioceptive features describing the configuration of the body relative to the model root (torso) and ground, and associated velocities. The high-level controller additionally receives the relative position of the target as input. The control interval for the high-level controller is $K = 10$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Humanoid", "weight": 1.0} -->

Analysis of the locomotor primitives Controlling the humanoid is a challenging problem and learning in the pre-training task is more sensitive to initial conditions and learning parameters than for the quadruped and snake. Nevertheless, we obtained several well performing policies with some variability across the gaits. Analyzing several of the associated low-level controllers in the same way as in the previous sections revealed that the locomotor primitives encode quite stable walking behaviors, typically taking hundreds of steps before falling (Fig. 8a).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Humanoid", "weight": 1.0} -->

Transfer task: Slalom Our transfer task consists of a slalom walk where the humanoid is presented with a sequence of virtual gates to pass through. A reward of 5 is given for passing a gate, and missing a gate results in termination of the episode. No other reward is given. After a gate has been passed, the next gate is positioned randomly to the left or the right of the previous one. The newly trained high-level controller receives the proprioceptive features provided to the low-level controller as input, as well as the relative position and orientation of the next gate.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Humanoid", "weight": 1.0} -->

We trained high-level controllers to solve the transfer task using some of the pre-trained low-level controllers and obtained several good solutions in which the humanoid learned to actively navigate the gates. Nevertheless, as expected from the already somewhat diverse set of solutions to the pretraining task, not all low-level controllers were equally suitable for solving the transfer task. And for a given low-level controller we further observed a much stronger sensitivity to the learning parameters and the initial conditions during transfer (see also section C.1 in the appendix). Considering the complexity of the humanoid and the relatively small number of constraints imposed by the pre-training task this is, however, perhaps not too surprising. We expect that a richer, more constrained pre-training regime would lead to more uniformly versatile and robust low-level controllers.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have provided a preliminary investigation of a hierarchical motor control architecture that can learn low-level motor behaviors and transfer them to new tasks. Our architecture contains two levels of abstraction that differ both in their access to sensory information and in the time scales at which they operate. Our design encourages the low-level controller to focus on the specifics of reactive motor control, while a high-level controller directs behavior towards the task goal by communicating a modulatory signal.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our investigation departs from the common but unnatural setting where an agent is trained on a single task. Instead, we exploit the fact that many complex motor behaviors share low-level structure by building reusable low-level controllers for a variety of tasks. We found our method to be especially effective when attempting challenging transfer tasks with sparse rewards where exploration via "motor babbling" is unlikely to accrue reward at all. This is illustrated in the transfer tasks for the swimmer, quadruped, and humanoid, in which direct end-to-end learning failed, but our method produced solutions.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We believe that the general idea of reusing learned behavioral primitives is important, and the design principles we have followed represent possible steps towards this goal. Our hierarchical design with information hiding has enabled the construction of low-level motor behaviors that are sheltered from task-specific information, enabling their reuse. However, the detailed individual and joint contributions of the features of our architecture remain to be investigated more thoroughly in future work (in particular the role and relevance of different time scales), alongside strategies to increase the reliability and stereotypy of the low-level behaviors, especially for difficult control problems such as humanoid walking.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our approach currently depends on the assumption that we can propose a set of low-level tasks that are simple to solve yet whose mastery in turn facilitates the solution of other high-level tasks. For motor behavior, we believe this assumption holds rather generally, as walking, for example, underpins a multitude of more complex tasks. By instilling a relatively small number of reusable skills into the low-level controllers, we expect that a large number of more complicated tasks involving composition of multiple behaviors should become solvable. We believe that this general direction could open new avenues for solving complex real-world, robotic control problems.
