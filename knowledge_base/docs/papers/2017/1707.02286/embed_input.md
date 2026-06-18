<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Emergence of Locomotion Behaviours in Rich Environments

Topics include Policy gradients, Reinforcement learning, Robustness, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The reinforcement learning paradigm allows, in principle, for complex behaviours to be learned directly from simple reward signals. In practice, however, it is common to carefully hand-design the reward function to encourage a particular solution, or to derive it from demonstration data. In this paper explore how a rich environment can help to promote the learning of complex behavior. Specifically, we train agents in diverse environmental contexts, and find that this encourages the emergence of robust behaviours that perform well across a suite of tasks. We demonstrate this principle for locomotion - behaviours that are known for their sensitivity to the choice of reward. We train several simulated bodies on a diverse set of challenging terrains and obstacles, using a simple reward function based on forward progress. Using a novel scalable variant of policy gradient reinforcement learning, our agents learn to run, jump, crouch and turn as required by the environment without explicit reward-based guidance. A visual depiction of highlights of the learned behavior can be viewed following.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement learning has demonstrated remarkable progress, achieving high levels of performance in Atari games, 3D navigation tasks, and board games. What is common among these tasks is that there is a well-defined reward function, such as the game score, which can be optimised to produce the desired behaviour. However, there are many other tasks where the "right" reward function is less clear, and optimisation of a naïvely selected one can lead to surprising results that do not match the expectations of the designer. This is particularly prevalent in continuous control tasks, such as locomotion, and it has become standard practice to carefully handcraft the reward function, or else elicit a reward function from demonstrations.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reward engineering has led to a number of successful demonstrations of locomotion behaviour, however, these examples are known to be brittle: they can lead to unexpected results if the reward function is modified even slightly, and for more advanced behaviours the appropriate reward function is often non-obvious in the first place. Also, arguably, the requirement of careful reward design sidesteps a primary challenge of reinforcement learning: how an agent can learn for itself, directly from a limited reward signal, to achieve rich and effective behaviours. In this paper we return to this challenge.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our premise is that rich and robust behaviours will emerge from simple reward functions, if the environment itself contains sufficient richness and diversity. Firstly, an environment that presents a spectrum of challenges at different levels of difficulty may shape learning and guide it towards solutions that would be difficult to discover in more limited settings. Secondly, the sensitivity to reward functions and other experiment details may be due to a kind of overfitting, finding idiosyncratic solutions that happen to work within a specific setting, but are not robust when the agent is exposed to a wider range of settings. Presenting the agent with a diversity of challenges thus increases the performance gap between different solutions and may favor the learning of solutions that are robust across settings.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We focus on a set of novel locomotion tasks that go significantly beyond the previous state-of-the-art for agents trained directly from reinforcement learning. They include a variety of obstacle courses for agents with different bodies (*Quadruped*, *Planar Walker*, and *Humanoid* ). The courses are procedurally generated such that every episode presents a different instance of the task.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our environments include a wide range of obstacles with varying levels of difficulty (e.g. steepness, unevenness, distance between gaps). The variations in difficulty present an implicit curriculum to the agent -- as it increases its capabilities it is able to overcome increasingly hard challenges, resulting in the emergence of ostensibly sophisticated locomotion skills which may naïvely have seemed to require careful reward design or other instruction. We also show that learning speed can be improved by explicitly structuring terrains to gradually increase in difficulty so that the agent faces easier obstacles first and harder obstacles only when it has mastered the easy ones.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In order to learn effectively in these rich and challenging domains, it is necessary to have a reliable and scalable reinforcement learning algorithm. We leverage components from several recent approaches to deep reinforcement learning. First, we build upon robust policy gradient algorithms, such as trust region policy optimization (TRPO) and proximal policy optimization (PPO), which bound parameter updates to a trust region to ensure stability. Second, like the widely used A3C algorithm and related approaches we distribute the computation over many parallel instances of agent and environment. Our distributed implementation of PPO improves over TRPO in terms of wall clock time with little difference in robustness, and also improves over our existing implementation of A3C with continuous actions when the same number of workers is used.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper proceeds as follows. In Section 2 we describe the distributed PPO (DPPO) algorithm that enables the subsequent experiments, and validate its effectiveness empirically. Then in Section 3 we introduce the main experimental setup: a diverse set of challenging terrains and obstacles. We provide evidence in Section 4 that effective locomotion behaviours emerge directly from simple rewards; furthermore we show that terrains with a "curriculum" of difficulty encourage much more rapid progress, and that agents trained in more diverse conditions can be more robust.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Large scale reinforcement learning with Distributed PPO", "weight": 1.0} -->

Our focus is on reinforcement learning in rich simulated environments with continuous state and action spaces. We require algorithms that are robust across a wide range of task variation, and that scale effectively to challenging domains. We address each of these issues in turn.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Robust policy gradients with Proximal Policy Optimization", "weight": 1.0} -->

Deep reinforcement learning algorithms based on large-scale, high-throughput optimization methods, have produced state-of-the-art results in discrete and low-dimensional action spaces, e.g. on Atari games and 3D navigation. In contrast, many prior works on continuous action spaces (e.g. ), although impressive, have focused on comparatively small problems, and the use of large-scale, distributed optimization is less widespread and the corresponding algorithms are less well developed (but see e.g. ). We present a robust policy gradient algorithm, suitable for high-dimensional continuous control problems, that can be scaled to much larger domains using distributed computation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Robust policy gradients with Proximal Policy Optimization", "weight": 1.0} -->

Policy gradient estimates can have high variance (e.g. ) and algorithms can be sensitive to the settings of their hyperparameters. Several approaches have been proposed to make policy gradient algorithms more robust. One effective measure is to employ a *trust region* constraint that restricts the amount by which any update is allowed to change the policy. A popular algorithm that makes use of this idea is trust region policy optimization (TRPO; ). In every iteration given current parameters $\theta_{old}$, TRPO collects a (relatively large) batch of data and optimizes the surrogate loss ${J_{TRPO}{(\theta)}} = {{\mathbb{E}}_{\rho_{\theta_{old}}{(\tau)}}\left\lbrack {\sum_{t}{\gamma^{t - 1}\frac{\pi_{\theta}{(\left. a_{t} \middle| s_{t} \right.)}}{\pi_{\theta_{old}}{(\left.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Robust policy gradients with Proximal Policy Optimization", "weight": 1.0} -->

The Proximal Policy Optimization (PPO) algorithm can be seen as an approximate version of TRPO that relies only on first order gradients, making it more convenient to use with recurrent neural networks (RNNs) and in a large-scale distributed setting. The trust region constraint is implemented via a regularization term. The coefficient of this regularization term is adapted depending on whether the constraint had previously been violated or not (a similar idea but without the adaptive coefficient has also been used ). Algorithm Box 1 shows the core PPO algorithm in pseudo-code.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Robust policy gradients with Proximal Policy Optimization", "weight": 1.0} -->

Algorithm 1 Proximal Policy Optimization (adapted from )

<!-- chunk {"id": "body-0015", "role": "body", "section": "Robust policy gradients with Proximal Policy Optimization", "weight": 1.0} -->

In algorithm 1, the hyperparameter ${KL}_{target}$ is the desired change in the policy per iteration. The scaling term $\alpha > 1$ controls the adjustment of the KL-regularization coefficient if the actual change in the policy stayed significantly below or significantly exceeded the target KL (i.e. falls outside the interval $\lbrack{\beta_{low}{KL}_{target}},{\beta_{high}{KL}_{target}}\rbrack$).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Scalable reinforcement learning with Distributed PPO", "weight": 1.0} -->

To achieve good performance in rich, simulated environments, we have implemented a distributed version of the PPO algorithm (DPPO). Data collection and gradient calculation are distributed over workers. We have experimented with both synchronous and asynchronous updates and have found that averaging gradients and applying them synchronously leads to better results in practice.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Scalable reinforcement learning with Distributed PPO", "weight": 1.0} -->

The original PPO algorithm estimates advantages using the complete sum of rewards. To facilitate the use of RNNs with batch updates while also supporting variable length episodes we follow a strategy similar to and use truncated backpropagation through time with a window of length $K$. This makes it natural (albeit not a requirement) to use $K$-step returns also for estimating the advantage, i.e. we sum the rewards over the same $K$-step windows and bootstrap from the value function after $K$-steps: ${\hat{A}}_{t} = {{{\sum_{i = 1}^{K}{\gamma^{i - 1}r_{t + i}}} + {\gamma^{K - 1}V_{\phi}{(s_{t + K})}}} - {V_{\phi}{(s_{t})}}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Scalable reinforcement learning with Distributed PPO", "weight": 1.0} -->

The publicly available implementation of PPO by John Schulman adds several modifications to the core algorithm. These include normalization of inputs and rewards as well as an additional term in the loss that penalizes large violations of the trust region constraint. We adopt similar augmentations in the distributed setting but find that sharing and synchronization of various statistics across workers requires some care. The implementation of our distributed PPO (DPPO) is in TensorFlow, the parameters reside on a parameter server, and workers synchronize their parameters after every gradient step. Pseudocode and further details are provided in the supplemental material.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Evaluation of Distributed PPO", "weight": 1.0} -->

We compare DPPO to several baseline algorithms. The goal of these experiments is primarily to establish that the algorithm allows robust policy optimization with limited parameter tuning and that the algorithm scales effectively. We therefore perform the comparison on a selected number of benchmark tasks related to our research interests, and compare to two algorithmic alternatives: TRPO and continuous A3C. For details of the comparison please see the supplemental material.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Benchmark tasks", "weight": 1.0} -->

We consider three continuous control tasks for benchmarking the algorithms. All environments rely on the Mujoco physics engine. Two tasks are locomotion tasks in obstacle-free environments and the third task is a planar target-reaching task that requires memory. *Planar walker*: a simple bipedal walker with 9 degrees-of-freedom (DoF) and 6 torque actuated joints. It receives a primary reward proportional to its forward velocity, additional terms penalize control and the violation of box constraints on torso height and angle. Episodes are terminated early when the walker falls. *Humanoid*: The humanoid has 28 DoF and 21 acutated joints. The humanoid, too, receives a reward primarily proportional to its velocity along the x-axis, as well as a constant reward at every step that, together with episode termination upon falling, encourage it to not fall. *Memory reacher*: A random-target reaching task with a simple 2 DoF robotic arm confined to the plane. The target position is provided for the first 10 steps of each episode during which the arm is not allowed to move.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Benchmark tasks", "weight": 1.0} -->

When the arm is allowed to move, the target has already disappeared and the RNN memory must be relied upon in order for the arm to reach towards the correct target location. The reward in this task is the distance between the positions of end-effector and target, and it tests the ability of DPPO to optimize recurrent network policies.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Results", "weight": 1.0} -->

Results depicted in Fig. 1 show that DPPO achieves performance similar to TRPO and that DPPO scales well with the number of workers used, which can significantly reduce wall clock time. Since it is fully gradient based it can also be used directly with recurrent networks as demonstrated by the *Memory reacher* task. DPPO is also faster (in wallclock) than our implementation of A3C when the same number of workers is used.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Methods: environments and models", "weight": 1.0} -->

Our goal is to study whether sophisticated locomotion skills can emerge from simple rewards when learning from varied challenges with a spectrum of difficulty levels. Having validated our scalable DPPO algorithm on simpler benchmark tasks, we next describe the settings in which we will demonstrate the emergence of more complex behavior.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Training environments", "weight": 1.0} -->

In order to expose our agents to a diverse set of locomotion challenges we use a physical simulation environment roughly analogous to a platform game, again implemented in Mujoco. We procedurally generate a large number of different terrains with a variety of obstacles; a different instance of the terrain and obstacles is generated in each episode.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Bodies", "weight": 1.0} -->

We consider three different torque-controlled bodies, described roughly in terms of increasing complexity. *Planar walker*: a simple walking body with 9 DoF and 6 actuated joints constrained to the plane. *Quadruped*: a simple three-dimensional quadrupedal body with 12 DoF and 8 actuated joints. *Humanoid*: a three-dimensional humanoid with 21 actuated dimensions and 28 DoF. The bodies can be seen in action in figures 4, 5, and 7 respectively. Note that the *Planar walker* and *Humanoid* bodies overlap with those used in the benchmarking tasks described in the previous section, however the benchmark tasks only consisted of simple locomotion in an open plane.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Rewards", "weight": 1.0} -->

We keep the reward for all tasks simple and consistent across terrains. The reward consists of a main component proportional to the velocity along the x-axis, encouraging the agent to make forward progress along the track, plus a small term penalizing torques. For the walker the reward also includes the same box constraints on the pose as in section 2. For the quadruped and humanoid we penalize deviations from the center of the track, and the humanoid receives an additional reward per time-step for not falling. Details can be found in the supplemental material. We note that differences in the reward functions across bodies are the consequence of us adapting previously proposed reward functions (cf. e.g. ) rather than the result of careful tuning, and while the reward functions vary slightly across bodies we do not change them to elicit different behaviors for a single body.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Terrain and obstacles", "weight": 1.0} -->

All of our courses are procedurally generated; in every episode a new course is generated based on pre-defined statistics. We consider several different terrain and obstacle types: (a) *hurdles*: hurdle-like obstacles of variable height and width that the walker needs to jump or climb over; (b) *gaps*: gaps in the ground that must be jumped over; (c) *variable terrain*: a terrain with different features such as ramps, gaps, hills, etc.; (d) *slalom walls*: walls that form obstacles that require walking around, (e) *platforms*: platforms that hover above the ground which can be jumped on or crouched under. Courses consist of a sequence of random instantiations of the above terrain types within user-specified parameter ranges.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Terrain and obstacles", "weight": 1.0} -->

We train on different types of courses: single-type courses (e.g. gaps only, hurdles only, etc.); mixtures of single-type courses (e.g. every episode a different terrain type is chosen); and mixed terrains (individual courses consisting of more than one terrain type). We consider stationary courses for which the obstacle statistics are effectively fixed over the the length of the course, and "curriculum" courses in which the difficulty of the terrain increases gradually over the length of the course. Fig. 3 shows a few different course types.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Observations", "weight": 1.0} -->

The agents receive two sets of observations: a set of egocentric, "proprioceptive" features containing joint angles and angular velocities; for the *Quadruped* and *Humanoid* these features also contain the readings of a velocimeter, accelerometer, and a gyroscope positioned at the torso providing egocentric velocity and acceleration information, plus contact sensors attached to the feet and legs. The *Humanoid* also has torque sensors in the joints of the lower limbs. a set of "exteroceptive" features containing task-relevant information including the position with respect to the center of the track as well as the profile of the terrain ahead. Information about the terrain is provided as an array of height measurements taken at sampling points that translate along the x- and y-axis with the body and the density of which decreases with distance from the body. The *Planar Walker* is confined to the $xz$-plane (i.e. it cannot move side-to-side), which simplifies its perceptual features. See supplemental material for details.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Policy parameterization", "weight": 1.0} -->

Similar to we aim to achieve a separation of concerns between the basic locomotion skills and terrain perception and navigation. We structure our policy into two subnetworks, one of which receives only proprioceptive information, and the other which receives only exteroceptive information. As explained in the previous paragraph with proprioceptive information we refer to information that is independent of any task and local to the body while exteroceptive information includes a representation of the terrain ahead. We compared this architecture to a simple fully connected neural network and found that it greatly increased learning speed. Fig. 2 shows a schematic.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Results", "weight": 1.0} -->

We apply the Distributed PPO algorithm to a variety of bodies, terrains, and obstacles. Our aim is to establish whether simple reward functions can lead to the emergence of sophisticated locomotion skills when agents are trained in rich environments. We are further interested whether the terrain structure can affect learning success and robustness of the resulting behavior.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Planar Walker", "weight": 1.0} -->

We train the walker on *hurdles*, *gaps*, *platforms*, and *variable terrain* separately, on a mixed course containing all features interleaved, and on a mixture of terrains (i.e. the walker was placed on different terrains in different episodes). It acquired a robust gait, learned to jump over hurdles and gaps, and to walk over or crouch underneath platforms. All of these behaviors emerged spontaneously, without special cased shaping rewards to induce each separate behaviour. Figure 4 shows motion sequences of the *Planar Walker* traversing a rubble-field, jumping over a hurdle, and over gaps, and crouching under a platform. Examples of the respective behaviors can be found in the supplemental video. The emergence of these skills was robust across seeds. At the end of learning the *Planar Walker* jumped over hurdles nearly as tall as its own body.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Quadruped", "weight": 1.0} -->

The quadruped is a generally less agile body than the walker but it adds a third dimension to the control problem. We considered three different terrain types: *variable terrain*, *slalom walls*, *gaps*, and a variation of the *hurdles* terrain which contained *obstacles* that can be avoided, and others that require climbing or jumping.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Quadruped", "weight": 1.0} -->

The *Quadruped*, too, learns to navigate most obstacles quite reliably, with only small variations across seeds. It discovers that jumping up or forward (in some cases with surprising accuracy) is a suitable strategy to overcome *hurdles*, and *gaps*, and it learns to navigate walls, turning left and right as appropriate -- in both cases despite only receiving reward for moving forward. For the variation of the *hurdles*-terrain it learns to distinguish between obstacles that it can and / or has to climb over, and those it has to walk around. The *variable terrain* may seem easy but is, in fact, surprisingly hard because the body shape of the *Quadruped* is poorly suited (i.e. the legs of the quadruped are short compared to the variations in the terrain). Nevertheless it learns strategies to traverse reasonably robustly. Fig. 5 shows some representative motion sequences; further examples can be found in the supplemental video.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Analyses", "weight": 1.0} -->

We investigate whether the nature of the terrain affects learning. In particular, it is easy to imagine that training, for instance, very tall hurdles only will not be effective. For training to be successful in our setup it is required that the walker occasionally "solves" obstacles by chance -- and the probability of this happening, is, of course, minuscule when all hurdles are very tall. We verify this by training a *Planar Walker* on two different types of *hurdles*-terrains. The first possesses stationary statistics with high- and low hurdles being randomly interleaved. In the second terrain the difficulty, as given by the minimum and maximum height of the hurdles, increases gradually over the length of the course. We measure learning progress by evaluating policies during learning on two test terrains, an easy one with shallow hurdles and a difficult one with tall hurdles. Results are shown in Fig. 6a for a representative *Planar Walker* policy. The policy trained on the terrain with gradually increasing difficulty improves faster than the one trained on a stationary terrain.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Analyses", "weight": 1.0} -->

We further study whether training on varying terrains leads to more robust gaits compared to usual task of moving forward on a plane. To this end we train *Planar Walker* and *Quadruped* policies on a flat course as well as on the (more challenging) hurdles. We then evaluate representative policies from each experiment with respect to their robustness to (a) unobserved variations in surface friction, (b) unobserved rumble-strips, (c) changes in the model of the body, (d) unobserved inclines / declines of the ground. Results depicted in Fig. 6b show a trend of training on hurdles increasing robustness on other forms of unobserved variation in the terrain.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Humanoid", "weight": 1.0} -->

Our final set of experiments considers the 28-DoF *Humanoid*, a considerably more complex body than *Planar Walker* and *Quadruped*. The set of terrains is qualitatively similar to the ones used for the other bodies, including *gaps*, *hurdles*, a *variable terrain*, as well as the *slalom walls*. We also trained agents on mixtures of the above terrains.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Humanoid", "weight": 1.0} -->

As for the previous experiments we considered a simple reward function, primarily proportional to the velocity along the x-axis (see above). We experimented with two alternative termination conditions: (a) episodes were terminated when the minimum distance between head and feet fell below 0.9m; (b) episodes were terminated when the minimum distance between head and ground fell below 1.1m.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Humanoid", "weight": 1.0} -->

In general, the humanoid presents a considerably harder learning problem largely because with its relatively large number of degrees of freedoms it is prone to exploit redundancies in the task specification and / or to get stuck in local optima, resulting in entertaining but visually unsatisfactory gaits. Learning results tend to be sensitive to the particular algorithm, exploration strategy, reward function, termination condition, and weight initialization.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Humanoid", "weight": 1.0} -->

The results we obtained for the humanoid were indeed much more diverse than for the other two bodies, with significant variations across seeds for the same setting of the hyperparameters. Some of the variations in the behaviors were associated with differences in learning speed and asymptotic performance (suggesting a local optimum); others were not (suggesting alternative solution strategies).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Humanoid", "weight": 1.0} -->

Nevertheless we obtained for each terrain several well performing agents, both in terms of performance and in terms of visually pleasing gaits. Fig. 7 shows several examples of agents trained on *gaps*, *hurdles*, *slalom walls*, and *variable terrain*. As in the previous experiments the terrain diversity and the inherent curriculum led the agents to discover robust gaits, the ability to overcome obstacles, to jump across gaps, and to navigate slalom courses. We highlight several solution strategies for each terrain in the supplemental video, including less visually appealing ones. To test the robustness of the learned behaviors we further constructed two test courses with (a) statistics rather different from the training terrains and (b) unobserved perturbations in the form of see-saws and random forces applied to the *Humanoid*'s torso, which is also presented in the video. Qualitatively we see moderately large levels of robustness to these probe challenges (see supplemental video).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have investigated the question whether and to what extent training agents in a rich environment can lead to the emergence of behaviors that are not directly incentivized via the reward function. This departs from the common setup in control where a reward function is carefully tuned to achieve particular solutions. Instead, we use deliberately simple and generic reward functions but train the agent over a wide range of environmental conditions. Our experiments suggest that training on diverse terrain can indeed lead to the development of non-trivial locomotion skills such as jumping, crouching, and turning for which designing a sensible reward is not easy. While we do not claim that environmental variations will be sufficient, we believe that training agents in richer environments and on a broader spectrum of tasks than is commonly done today is likely to improve the quality and robustness of the learned behaviors -- and also the ease with which they can be learned. In that sense, choosing a seemingly more complex environment may actually make learning easier.
