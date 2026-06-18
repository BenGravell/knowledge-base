<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

DeepMind Control Suite

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The DeepMind Control Suite is a set of continuous control tasks with a standardised structure and interpretable rewards, intended to serve as performance benchmarks for reinforcement learning agents. The tasks are written in Python and powered by the MuJoCo physics engine, making them easy to use and modify. We include benchmarks for several learning algorithms. The Control Suite is publicly available . A video summary of all tasks is available .

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Controlling the physical world is an integral part and arguably a prerequisite of general intelligence. Indeed, the only known example of general-purpose intelligence emerged in primates which had been manipulating the world for millions of years.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Physical control tasks share many common properties and it is sensible to consider them as a distinct class of behavioural problems. Unlike board games, language and other symbolic domains, physical tasks are fundamentally continuous in state, time and action. Their dynamics are subject to second-order equations of motion, implying that the underlying state is composed of position-like and velocity-like variables, while state derivatives are acceleration-like. Sensory signals (i.e. observations) usually carry meaningful physical units and vary over corresponding timescales.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This decade has seen rapid progress in the application of Reinforcement Learning (RL) techniques to difficult problem domains such as video games. The Arcade Learning Environment was a vital facilitator of these developments, providing a set of standard benchmarks for evaluating and comparing learning algorithms. The DeepMind Control Suite provides a similar set of standard benchmarks for continuous control problems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The OpenAI Gym currently includes a set of continuous control domains that has become the de-facto benchmark in continuous RL. The Control Suite is also a set of tasks for benchmarking continuous RL algorithms, with a few notable differences. We focus exclusively on continuous control, e.g. separating observations with similar units (position, velocity, force etc.) rather than concatenating into one vector. Our unified reward structure (see below) offers interpretable learning curves and aggregated suite-wide performance measures. Furthermore, we emphasise high-quality well-documented code using uniform design patterns, offering a readable, transparent and easily extensible codebase. Finally, the Control Suite has equivalent domains to all those in the Gym while adding many more^11^1With the notable exception of Philipp Moritz's "ant" quadruped, which we intend to replace soon, see Future Work..

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 2 we explain the general structure of the Control Suite and in Section 3 we describe each domain in detail. In Sections 4 and 5 we document the high and low-level Python APIs, respectively. Section 6 is devoted to our benchmarking results. We then conclude and provide a roadmap for future development.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Structure and Design", "weight": 1.0} -->

The DeepMind Control Suite is a set of stable, well-tested continuous control tasks that are easy to use and modify. Tasks are written in \\href and physical models are defined using \\href Standardised action, observation and reward structures make benchmarking simple and learning curves easy to interpret.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Model and Task verification", "weight": 1.0} -->

Simulated physics can easily destabilise and diverge, mostly due to errors introduced by time discretisation. Smaller time-steps are more stable, but require more computation per unit simulation time, so the choice of time-step is always a trade-off between stability and speed. What's more, learning agents are better at discovering and exploiting instabilities.^22^2This phenomenon, sometimes known as Sims' Law, was first articulated: "Any bugs that allow energy leaks from non-conservation, or even round-off errors, will inevitably be discovered and exploited".

<!-- chunk {"id": "body-0010", "role": "body", "section": "Model and Task verification", "weight": 1.0} -->

It is surprisingly easy to write tasks that are much easier or harder than intended, that are impossible to solve or that can be solved by very different strategies than expected (i.e. "cheats"). To prevent these situations, the Atari™ games that make up ALE were extensively tested over more than 10 man-years^33^3Marc Bellemare, personal communication.. However, continuous control domains cannot be solved by humans, so a different approach must be taken.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Model and Task verification", "weight": 1.0} -->

In order to tackle both of these challenges, we ran variety of learning agents against all tasks, and iterated on each task's design until we were satisfied that the physics was stable and non-exploitable, and that the task is solved correctly by at least one agent. Tasks that are solvable by some learning agent were collated into the benchmarking set. Tasks were not solved by any learning agent are in the extra set of tasks.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

A continuous Markov Decision Process (MDP) is given by a set of states $\mathcal{S}$, a set of actions $\mathcal{A}$, a dynamics (transition) function $\mathbf{f}{(\mathbf{s},\mathbf{a})}$, an observation function $\mathbf{o}{(\mathbf{s},\mathbf{a})}$ and a scalar reward function $r{(\mathbf{s},\mathbf{a})}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

: The state $\mathbf{s}$ is a vector of real numbers $\mathcal{S} \equiv {\mathbb{R}}^{\dim{(\mathcal{S})}}$, with the exception of spatial orientations which are represented by unit quaternions $\in {SU{}}$. States are initialised in some subset $\mathcal{S}_{\text{0}} \subseteq \mathcal{S}$ by the begin_episode method. To avoid memorised "rote" solutions $\mathcal{S}_{\text{0}}$ is never a single state.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

: With the exception of the LQR domain (see below), the action vector is in the unit box $\mathbf{a} \in \mathcal{A} \equiv \left\lbrack {- 1},1 \right\rbrack^{\dim{(\mathcal{A})}}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

: While the state notionally evolves according to a continuous ordinary differential equation $\overset{˙}{\mathbf{s}} = {\mathbf{f}_{c}{(\mathbf{s},\mathbf{a})}}$, in practice temporal integration is discrete^44^4Most domains use MuJoCo's default semi-implicit Euler integrator, a few which have smooth, nearly energy-conserving dynamics use 4th-order Runge Kutta. with some fixed, finite time-step: $\mathbf{s}_{t + h} = {\mathbf{f}{(\mathbf{s}_{t},\mathbf{a}_{t})}}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

: The function $\mathbf{o}{(\mathbf{s},\mathbf{a})}$ describes the observations available to the learning agent. With the exception of point-mass:hard (see below), all tasks are strongly observable, i.e. the state can be recovered from a single observation. Observation features which depend only on the state (position and velocity) are functions of the current state. Features which are also dependent on controls (e.g. touch sensor readings) are functions of the previous transition. Observations are implemented as a Python OrderedDict.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

: The range of rewards in the Control Suite, with the exception of the LQR domain, are in the unit interval ${r{(\mathbf{s},\mathbf{a})}} \in {\lbrack 0,1\rbrack}$. Some tasks have "sparse" rewards ${r{(\mathbf{s},\mathbf{a})}} \in {\{ 0,1\}}$. This structure is facilitated by the tolerance function, see Figure 2. Since terms produced by tolerance are in the unit interval, both *averaging* and *multiplication* operations maintain that property, facillitating cost design.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

: Control problems are classified as finite-horizon, first-exit and infinite-horizon. Control Suite tasks have no terminal states or time limit and are therefore of the infinite-horizon variety.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

In the limit $\tau\rightarrow\infty$ (equivalently $\gamma\rightarrow 1$), the policies of the discounted-horizon and average-return formulations are identical.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

: While agents are expected to optimise for infinite-horizon returns, these are difficult to measure. As a proxy we use fixed-length episodes of 1000 time steps. Since all reward functions are designed so that $r \approx 1$ at or near a goal state, learning curves measuring total returns all have the same y-axis limits of $\lbrack\mathbf{0},\mathbf{1}\mathbf{0}\mathbf{0}\mathbf{0}\rbrack$, making them easier to interpret.

<!-- chunk {"id": "body-0021", "role": "body", "section": "MuJoCo physics", "weight": 1.0} -->

MuJoCo is a fast, minimal-coordinate, continuous-time physics engine. It compares favourably to other popular engines, especially for articulated, low-to-medium degree-of-freedom (DoF) models in contact with other bodies. The convenient \\href definition format and reconfigurable computation pipeline have made MuJoCo popular^55^5Along with the MultiBody branch of the \\href physics engine. for robotics and reinforcement learning research.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

A domain refers to a physical model, while a task refers to an instance of that model with a particular MDP structure. For example the difference between the swingup and balance tasks of the cartpole domain is whether the pole is initialised pointing downwards or upwards, respectively. In some cases, e.g. when the model is procedurally generated, different tasks might have different physical properties. Tasks in the Control Suite are collated into tuples according predefined tags. In particular, tasks used for benchmarking are in the BENCHMARKING tuple, while those not used for benchmarking (because they are particularly difficult, or because they don't conform to the standard structure) are in the EXTRA tuple. All suite tasks are accessible via the ALL_TASKS tuple. In the domain descriptions below, names are followed by three integers specifying the dimensions of the state, control and observation spaces i.e. $\left( {\dim{(\mathcal{S})}},{\dim{(\mathcal{A})}},{\dim{(\mathcal{O})}} \right)$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Pendulum: The classic inverted pendulum. The torque-limited actuator is 1/6th as strong as required to lift the mass from motionless horizontal, necessitating several swings to swing up and balance. The swingup task has a simple sparse reward: 1 when the pole is within 30∘ of the vertical and 0 otherwise.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Acrobot: The underactuated double pendulum, torque applied to the second joint. The goal is to swing up and balance. Despite being low-dimensional, this is not an easy control problem. The physical model conforms to rather than the earlier. Both swingup and swingup_sparse tasks with smooth and sparse rewards, respectively.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Cart-pole: Swing up and balance an unactuated pole by applying forces to a cart at its base. The physical model conforms to. Four benchmarking tasks: in swingup and swingup_sparse the pole starts pointing down while in balance and balance_sparse the pole starts near the upright.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.585]figure[\FBwidth]
Cart-k-pole (2 k + 2, 1, 3 k + 2): The cart-pole domain allows to procedurally adding more poles, connected serially. Two non-benchmarking tasks, two_poles and three_poles are available.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Ball in cup: A planar ball-in-cup task. An actuated planar receptacle can translate in the vertical plane in order to swing and catch a ball attached to its bottom. The catch task has a sparse reward: 1 when the ball is in the cup, 0 otherwise.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Point-mass: A planar point-mass receives a reward of 1 when within a target at the origin. In the easy task, one of simplest in the suite, the 2 actuators correspond to the global x and y axes. In the hard task the gain matrix from the controls to the axes is randomised for each episode, making it impossible to solve by memory-less agents; this task is not in the benchmarking set.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Reacher: The simple two-link planar reacher with a randomised target location. The reward is one when the end effector penetrates the target sphere. In the easy task the target sphere is bigger than on the hard task (shown on the left).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Finger: A 3-DoF toy manipulation problem based. A planar ‘finger’ is required to rotate a body on an unactuated hinge. In the turn_easy and turn_hard tasks, the tip of the free body must overlap with a target (the target is smaller for the turn_hard task). In the spin task, the body must be continually rotated.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Hopper: The planar one-legged hopper introduced, initialised in a random configuration. In the stand task it is rewarded for bringing its torso to a minimal height. In the hop task it is rewarded for torso height and forward velocity.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Fish: A fish is required to swim to a target. This domain relies on MuJoCo’s simplified fluid dynamics. Two tasks: in the upright task, the fish is rewarded only for righting itself with respect to the vertical, while in the swim task it is also rewarded for swimming to the target.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Cheetah: A running planar biped based. The reward r is linearly proportional to the forward velocity v up to a maximum of 10m/s i.e. r (v) = max (0,min (v/10,1)).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Walker: An improved planar walker based on the one introduced. In the stand task reward is a combination of terms encouraging an upright torso and some minimal torso height. The walk and run tasks include a component encouraging forward velocity.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Manipulator: A planar manipulator is rewarded for bringing an object to a target location. In order to assist with exploration, in %10 of episodes the object is initialised in the gripper or at the target. Four manipulator tasks: {bring,insert}_{ball,peg} of which only bring_ball is in the benchmarking set. The other three are shown below.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.415]figure[\FBwidth]
Manipulator extra: insert_ball: place the ball in the basket. bring_peg: bring the peg to the target peg (matching orientation). insert_peg: insert the peg into the slot.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Stacker (6 k + 16, 5, 11 k + 26): Stack k boxes. Reward is given when a box is at the target and the gripper is away from the target, making stacking necessary. The height of the target is sampled uniformly from {1, …, k}.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Swimmer (2 k + 4, k − 1, 4 k + 1): This procedurally generated k-link planar swimmer is based on but using MuJoCo’s high-Reynolds fluid drag model. A reward of 1 is provided when the nose is inside the target and decreases smoothly with distance like a Lorentzian. The two instantiations provided in the benchmarking set are the 6-link and 15-link swimmers.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Humanoid: A simplified humanoid with 21 joints, based on the model. Three tasks: stand, walk and run are differentiated by the desired horizontal speed of 0, 1 and 10m/s, respectively. Observations are in an egocentric frame and many movement styles are possible solutions e.g. running backwards or sideways. This facilitates exploration of local optima.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Humanoid_CMU: A humanoid body with 56 joints, adapted from and based on the ASF model of subject #8 in the CMU Motion Capture Database. This domain has the same stand, walk and run tasks as the simpler humanoid. We include tools for parsing and playback of the CMU MoCap data, see below.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
LQR (2n, m, 2n): n masses, of which m ≤ n are actuated, move on linear joints which are connected serially. The reward is a quadratic in the position and controls. Analytic transition and control-gain matrices are extracted from MuJoCo and the optimal policy and value functions are computed in lqr_solver.py using Riccati iterations. Since both controls and reward are unbounded, LQR is not in the benchmarking set.

<!-- chunk {"id": "body-0042", "role": "body", "section": "CMU Motion Capture Data", "weight": 1.0} -->

We enable humanoid_CMU to be used for imitation learning as in Merel et al. by providing tools for parsing, conversion and playback of human motion capture data from the CMU Motion Capture Database. The convert function in the parse_amc module loads an AMC data file and returns a sequence of configurations for the humanoid_CMU model. The example script CMU_mocap_demo.py uses this function to generate a video.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Reinforcement learning API", "weight": 1.0} -->

The environment.Base class that defines generic RL interface.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Reinforcement learning API", "weight": 1.0} -->

The suite module that contains the domains and tasks defined in Section 3

<!-- chunk {"id": "body-0045", "role": "body", "section": "Reinforcement learning API", "weight": 1.0} -->

The underlying MuJoCo bindings and the mujoco.Physics class that provides most of the functionality needed to interact with an instantiated MJCF model.

<!-- chunk {"id": "body-0046", "role": "body", "section": "The RL Environment class", "weight": 1.0} -->

The class environment.Base, found within the dm_control.rl.environment

<!-- chunk {"id": "body-0047", "role": "body", "section": "The RL Environment class", "weight": 1.0} -->

$\bullet$ action_spec and observation_spec

<!-- chunk {"id": "body-0048", "role": "body", "section": "The RL Environment class", "weight": 1.0} -->

: describe the actions accepted and the observations returned by an Environment. For all the tasks in the suite, actions are given as a single NumPy array. action_spec returns an ArraySpec, with attributes describing the shape, data type, and optional minimum and maximum bounds for the action arrays. Observations consist of an OrderedDict containing one or more NumPy arrays. observation_spec returns an OrderedDict of ArraySpecs describing the shape and data type of each corresponding observation.

<!-- chunk {"id": "body-0049", "role": "body", "section": "The RL Environment class", "weight": 1.0} -->

: respectively start a new episode, and advance time given an action.

<!-- chunk {"id": "body-0050", "role": "body", "section": "The RL Environment class", "weight": 1.0} -->

Starting an episode and running it to completion might look like

<!-- chunk {"id": "body-0051", "role": "body", "section": "The RL Environment class", "weight": 1.0} -->

[⬇](data:text/plain;base64,c3BlYyA9IGVudi5hY3Rpb25fc3BlYygpCnRpbWVfc3RlcCA9IGVudi5yZXNldCgpCndoaWxlIG5vdCB0aW1lX3N0ZXAubGFzdCgpOgogIGFjdGlvbiA9IG5wLnJhbmRvbS51bmlmb3JtKHNwZWMubWluaW11bSwgc3BlYy5tYXhpbXVtLCBzcGVjLnNoYXBlKQogIHRpbWVfc3RlcCA9IGVudi5zdGVwKGFjdGlvbik=){download=""}

<!-- chunk {"id": "body-0052", "role": "body", "section": "The RL Environment class", "weight": 1.0} -->

while not time_step.last:

<!-- chunk {"id": "body-0053", "role": "body", "section": "The RL Environment class", "weight": 1.0} -->

action = np.random.uniform(spec.minimum, spec.maximum, spec.shape)

<!-- chunk {"id": "body-0054", "role": "body", "section": "The RL Environment class", "weight": 1.0} -->

time_step = env.step(action)

<!-- chunk {"id": "body-0055", "role": "body", "section": "The RL Environment class", "weight": 1.0} -->

: is an enum taking a value in \[FIRST, MID, LAST\]. The convenience methods first, mid and last return boolean values indicating whether the TimeStep's type is of the respective value.

<!-- chunk {"id": "body-0056", "role": "body", "section": "The RL Environment class", "weight": 1.0} -->

: is a scalar float $\gamma \in {\lbrack 0,1\rbrack}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "The RL Environment class", "weight": 1.0} -->

: is an OrderedDict of NumPy arrays matching the specification returned by observation_spec.

<!-- chunk {"id": "body-0058", "role": "body", "section": "The RL Environment class", "weight": 1.0} -->

Whereas the step_type specifies whether or not the episode is terminating, it is the discount $\gamma$ that determines the termination type. $\gamma = 0$ corresponds to a terminal state^66^6i.e. where the sum of future reward is equal to the current reward. as in the first-exit or finite-horizon formulations. A terminal TimeStep with $\gamma = 1$ corresponds to the infinite-horizon formulation. In this case an agent interacting with the environment should treat the episode as if it could have continued indefinitely, even though the sequence of observations and rewards is truncated. All Control Suite tasks with the exception of LQR^77^7The LQR task terminates with $\gamma = 0$ when the state is very close to 0, which is a proxy for the infinite exponential convergence of stabilised linear systems. return $\gamma = 1$ at every step, including on termination.

<!-- chunk {"id": "body-0059", "role": "body", "section": "The suite module", "weight": 1.0} -->

To load an environment representing a task from the suite, use suite.load:

<!-- chunk {"id": "body-0060", "role": "body", "section": "The suite module", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZnJvbSBkbV9jb250cm9sIGltcG9ydCBzdWl0ZQoKIyBMb2FkIG9uZSB0YXNrOgplbnYgPSBzdWl0ZS5sb2FkKGRvbWFpbl9uYW1lPSJjYXJ0cG9sZSIsIHRhc2tfbmFtZT0ic3dpbmd1cCIpCgojIEl0ZXJhdGUgb3ZlciBhIHRhc2sgc2V0Ogpmb3IgZG9tYWluX25hbWUsIHRhc2tfbmFtZSBpbiBzdWl0ZS5CRU5DSE1BUktJTkc6CiAgZW52ID0gc3VpdGUubG9hZChkb21haW5fbmFtZSwgdGFza19uYW1lKQogIC4uLg==){download=""}

<!-- chunk {"id": "body-0061", "role": "body", "section": "The suite module", "weight": 1.0} -->

env = suite.load(domain_name=\"cartpole\", task_name=\"swingup\")

<!-- chunk {"id": "body-0062", "role": "body", "section": "The suite module", "weight": 1.0} -->

for domain_name, task_name in suite.BENCHMARKING:

<!-- chunk {"id": "body-0063", "role": "body", "section": "The suite module", "weight": 1.0} -->

env = suite.load(domain_name, task_name)

<!-- chunk {"id": "body-0064", "role": "body", "section": "The suite module", "weight": 1.0} -->

By default, Control Suite environments return low-dimensional feature observations. The pixel.Wrapper adds or replaces these with images.

<!-- chunk {"id": "body-0065", "role": "body", "section": "The suite module", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZnJvbSBkbV9jb250cm9sLnN1aXRlLndyYXBwZXJzIGltcG9ydCBwaXhlbHMKZW52ID0gc3VpdGUubG9hZCgiY2FydHBvbGUiLCAic3dpbmd1cCIpCmVudl9hbmRfcGl4ZWxzID0gcGl4ZWxzLldyYXBwZXIoZW52KQojIFJlcGxhY2UgZXhpc3RpbmcgZmVhdHVyZXMgYnkgcGl4ZWwgb2JzZXJ2YXRpb25zLgplbnZfb25seV9waXhlbHMgPSBwaXhlbHMuV3JhcHBlcihlbnYsIHBpeGVsX29ubHk9RmFsc2UpCiMgUGl4ZWwgb2JzZXJ2YXRpb25zIGluIGFkZGl0aW9uIHRvIGV4aXN0aW5nIGZlYXR1cmVzLg==){download=""}

<!-- chunk {"id": "body-0066", "role": "body", "section": "The suite module", "weight": 1.0} -->

from dm_control.suite.wrappers import pixels

<!-- chunk {"id": "body-0067", "role": "body", "section": "The suite module", "weight": 1.0} -->

env = suite.load(\"cartpole\", \"swingup\")

<!-- chunk {"id": "body-0068", "role": "body", "section": "The suite module", "weight": 1.0} -->

env_and_pixels = pixels.Wrapper(env)

<!-- chunk {"id": "body-0069", "role": "body", "section": "The suite module", "weight": 1.0} -->

\# Replace existing features by pixel observations.

<!-- chunk {"id": "body-0070", "role": "body", "section": "The suite module", "weight": 1.0} -->

env_only_pixels = pixels.Wrapper(env, pixel_only=False)

<!-- chunk {"id": "body-0071", "role": "body", "section": "The suite module", "weight": 1.0} -->

\# Pixel observations in addition to existing features.

<!-- chunk {"id": "body-0072", "role": "body", "section": "The suite module", "weight": 1.0} -->

Models in the Control Suite use a common set of colours and textures for visual uniformity. As illustrated in the \\href this also allows us to modify colours in proportion to the reward, providing a convenient visual cue.

<!-- chunk {"id": "body-0073", "role": "body", "section": "The suite module", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZW52ID0gc3VpdGUubG9hZCgiZmlzaCIsICJzd2ltIiwgdGFza19rd2FyZ3MsIHZpc3VhbGl6ZV9yZXdhcmQ9VHJ1ZSk=){download=""}

<!-- chunk {"id": "body-0074", "role": "body", "section": "The suite module", "weight": 1.0} -->

env = suite.load(\"fish\", \"swim\", task_kwargs, visualize_reward=True)

<!-- chunk {"id": "body-0075", "role": "body", "section": "MuJoCo Python interface", "weight": 1.0} -->

While the environment.Base class is specific to the Reinforcement Learning scenario, the underlying bindings and mujoco.Physics class provide a general-purpose wrapper of the MuJoCo engine. We use Python's \\href library to bind to MuJoCo structs, enums and functions.

<!-- chunk {"id": "body-0076", "role": "body", "section": "MuJoCo Python interface", "weight": 1.0} -->

The bindings provide easy access to all MuJoCo library functions, automatically converting NumPy arrays to data pointers where appropriate.

<!-- chunk {"id": "body-0077", "role": "body", "section": "MuJoCo Python interface", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZnJvbSBkbV9jb250cm9sLm11am9jby53cmFwcGVyLm1qYmluZGluZ3MgaW1wb3J0IG1qbGliCmltcG9ydCBudW1weSBhcyBucAoKcXVhdCA9IG5wLmFycmF5KCguNSwgLjUsIC41LCAuNSkpCm1hdCA9IG5wLnplcm9zKCg5KSkKbWpsaWIubWp1X3F1YXQyTWF0KG1hdCwgcXVhdCkKCnByaW50KCJNdUpvQ28gY2FuIGNvbnZlcnQgdGhpcyBxdWF0ZXJuaW9uOiIpCnByaW50KHF1YXQpCnByaW50KCJUbyB0aGlzIHJvdGF0aW9uIG1hdHJpeDoiKQpwcmludChtYXQucmVzaGFwZSgzLDMpKQ==){download=""}

<!-- chunk {"id": "body-0078", "role": "body", "section": "MuJoCo Python interface", "weight": 1.0} -->

from dm_control.mujoco.wrapper.mjbindings import mjlib

<!-- chunk {"id": "body-0079", "role": "body", "section": "MuJoCo Python interface", "weight": 1.0} -->

mjlib.mju_quat2Mat(mat, quat)

<!-- chunk {"id": "body-0080", "role": "body", "section": "MuJoCo Python interface", "weight": 1.0} -->

print(\"MuJoCo can convert this quaternion:\")

<!-- chunk {"id": "body-0081", "role": "body", "section": "MuJoCo Python interface", "weight": 1.0} -->

[⬇](data:text/plain;base64,TXVKb0NvIGNhbiBjb252ZXJ0IHRoaXMgcXVhdGVybmlvbjoKWyAwLjUgIDAuNSAgMC41ICAwLjVdClRvIHRoaXMgcm90YXRpb24gbWF0cml4OgpbWyAwLiAgMC4gIDEuXQogWyAxLiAgMC4gIDAuXQogWyAwLiAgMS4gIDAuXV0=){download=""}

<!-- chunk {"id": "body-0082", "role": "body", "section": "MuJoCo Python interface", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZnJvbSBkbV9jb250cm9sLm11am9jby53cmFwcGVyLm1qYmluZGluZ3MgaW1wb3J0IGVudW1zCnByaW50KGVudW1zLm1qdEpvaW50KQ==){download=""}

<!-- chunk {"id": "body-0083", "role": "body", "section": "MuJoCo Python interface", "weight": 1.0} -->

from dm_control.mujoco.wrapper.mjbindings import enums

<!-- chunk {"id": "body-0084", "role": "body", "section": "MuJoCo Python interface", "weight": 1.0} -->

[⬇](data:text/plain;base64,bWp0Sm9pbnQobWpKTlRfRlJFRT0wLCBtakpOVF9CQUxMPTEsIG1qSk5UX1NMSURFPTIsIG1qSk5UX0hJTkdFPTMp){download=""}

<!-- chunk {"id": "body-0085", "role": "body", "section": "MuJoCo Python interface", "weight": 1.0} -->

mjtJoint(mjJNT_FREE=0, mjJNT_BALL=1, mjJNT_SLIDE=2, mjJNT_HINGE=3)

<!-- chunk {"id": "body-0086", "role": "body", "section": "The Physics class", "weight": 1.0} -->

The Physics class encapsulates MuJoCo's most commonly used functionality.

<!-- chunk {"id": "body-0087", "role": "body", "section": "The Physics class", "weight": 1.0} -->

The Physics.from_xml_string

<!-- chunk {"id": "body-0088", "role": "body", "section": "The Physics class", "weight": 1.0} -->

[⬇](data:text/plain;base64,c2ltcGxlX01KQ0YgPSAiIiIKPG11am9jbz4KICA8d29ybGRib2R5PgogICAgPGxpZ2h0IG5hbWU9InRvcCIgcG9zPSIwIDAgMS41Ii8+CiAgICA8Z2VvbSBuYW1lPSJmbG9vciIgdHlwZT0icGxhbmUiIHNpemU9IjEgMSAuMSIvPgogICAgPGJvZHkgbmFtZT0iYm94IiBwb3M9IjAgMCAuMyI+CiAgICAgIDxqb2ludCBuYW1lPSJ1cF9kb3duIiB0eXBlPSJzbGlkZSIgYXhpcz0iMCAwIDEiLz4KICAgICAgPGdlb20gbmFtZT0iYm94IiB0eXBlPSJib3giIHNpemU9Ii4yIC4yIC4yIiByZ2JhPSIxIDAgMCAxIi8+CiAgICAgIDxnZW9tIG5hbWU9InNwaGVyZSIgcG9zPSIuMiAuMiAuMiIgc2l6ZT0iLjEiIHJnYmE9IjAgMSAwIDEiLz4KICAgIDwvYm9keT4KICA8L3dvcmxkYm9keT4KPC9tdWpvY28+CiIiIgpwaHlzaWNzID0gbXVqb2NvLlBoeXNpY3MuZnJvbV94bWxfc3RyaW5nKHNpbXBsZV9NSkNGKQ==){download=""}

<!-- chunk {"id": "body-0089", "role": "body", "section": "The Physics class", "weight": 1.0} -->

physics = mujoco.Physics.from_xml_string(simple_MJCF)

<!-- chunk {"id": "body-0090", "role": "body", "section": "The Physics class", "weight": 1.0} -->

The Physics.render method outputs a numpy array of pixel values.

<!-- chunk {"id": "body-0091", "role": "body", "section": "The Physics class", "weight": 1.0} -->

[⬇](data:text/plain;base64,cGl4ZWxzID0gcGh5c2ljcy5yZW5kZXIoKQ==){download=""}

<!-- chunk {"id": "body-0092", "role": "body", "section": "The Physics class", "weight": 1.0} -->

Optional arguments to render can be used to specify the resolution, camera ID and whether to render RGB or depth images.

<!-- chunk {"id": "body-0093", "role": "body", "section": "The Physics class", "weight": 1.0} -->

: Physics.model and Physics.data

<!-- chunk {"id": "body-0094", "role": "body", "section": "The Physics class", "weight": 1.0} -->

MuJoCo's mjModel and mjData structs, describing static and dynamic simulation parameters, can be accessed via the model and data properties of Physics. They contain NumPy arrays that have direct, writeable views onto MuJoCo's internal memory.

<!-- chunk {"id": "body-0095", "role": "body", "section": "The Physics class", "weight": 1.0} -->

[⬇](data:text/plain;base64,IyBUaGlzIHdpbGwgZmFpbDoKcGh5c2ljcy5kYXRhLnFwb3MgPSBucC5yYW5kb20ucmFuZG4ocGh5c2ljcy5tb2RlbC5ucSkKIyBUaGlzIHdpbGwgc3VjY2VlZDoKcGh5c2ljcy5kYXRhLnFwb3NbOl0gPSBucC5yYW5kb20ucmFuZG4ocGh5c2ljcy5tb2RlbC5ucSk=){download=""}

<!-- chunk {"id": "body-0096", "role": "body", "section": "The Physics class", "weight": 1.0} -->

physics.data.qpos = np.random.randn(physics.model.nq)

<!-- chunk {"id": "body-0097", "role": "body", "section": "The Physics class", "weight": 1.0} -->

physics.data.qpos = np.random.randn(physics.model.nq)

<!-- chunk {"id": "body-0098", "role": "body", "section": "The Physics class", "weight": 1.0} -->

: Setting the state with reset_context

<!-- chunk {"id": "body-0099", "role": "body", "section": "The Physics class", "weight": 1.0} -->

When setting the MujoCo state, derived quantities like global positions or sensor measurements are not updated. In order to facilitate synchronisation of derived quantities we provide the Physics.reset_context

<!-- chunk {"id": "body-0100", "role": "body", "section": "The Physics class", "weight": 1.0} -->

[⬇](data:text/plain;base64,d2l0aCBwaHlzaWNzLnJlc2V0X2NvbnRleHQoKToKICAgIyBtal9yZXNldCgpIGlzIGNhbGxlZCB1cG9uIGVudGVyaW5nIHRoZSBjb250ZXh0LgogICBwaHlzaWNzLmRhdGEucXBvc1s6XSA9IC4uLiAgIyBTZXQgcG9zaXRpb24sCiAgIHBoeXNpY3MuZGF0YS5xdmVsWzpdID0gLi4uICAjIHZlbG9jaXR5CiAgIHBoeXNpY3MuZGF0YS5jdHJsWzpdID0gLi4uICAjIGFuZCBjb250cm9sLgojIG1qX2ZvcndhcmQoKSBpcyBjYWxsZWQgdXBvbiBleGl0aW5nIHRoZSBjb250ZXh0LiBOb3cgYWxsIGRlcml2ZWQKIyBxdWFudGl0aWVzIGFuZCBzZW5zb3IgbWVhc3VyZW1lbnRzIGFyZSB1cC10by1kYXRlLg==){download=""}

<!-- chunk {"id": "body-0101", "role": "body", "section": "The Physics class", "weight": 1.0} -->

\# mj_reset is called upon entering the context.

<!-- chunk {"id": "body-0102", "role": "body", "section": "The Physics class", "weight": 1.0} -->

physics.data.qpos = \... \# Set position,

<!-- chunk {"id": "body-0103", "role": "body", "section": "The Physics class", "weight": 1.0} -->

physics.data.ctrl = \... \# and control.

<!-- chunk {"id": "body-0104", "role": "body", "section": "The Physics class", "weight": 1.0} -->

\# mj_forward is called upon exiting the context. Now all derived

<!-- chunk {"id": "body-0105", "role": "body", "section": "The Physics class", "weight": 1.0} -->

\# quantities and sensor measurements are up-to-date.

<!-- chunk {"id": "body-0106", "role": "body", "section": "The Physics class", "weight": 1.0} -->

The physics.step method is used to advance the simulation. Note that this method does not directly call MuJoCo's mj_step function. At the end of an mj_step the state is updated, but the intermediate quantities stored in mjData were computed with respect to the *previous* state. To keep these derived quantities as closely synchronised with the current simulation state as possible, we use the fact that MuJoCo partitions mj_step into two parts: mj_step1, which depends only on the state and mj_step2, which also depends on the control. Our physics.step first executes mj_step2 (assuming mj_step1 has already been called), and then calls mj_step1, beginning the next step^88^8In the case of Runge-Kutta integration, we simply conclude each RK4 step with an mj_step1.. The upshot is that quantities that depend only on position and velocity (e.g. camera pixels) are synchronised with the current state, while quantities that depend on force/acceleration (e.g. touch sensors) are with respect to the previous transition.

<!-- chunk {"id": "body-0107", "role": "body", "section": "The Physics class", "weight": 1.0} -->

It is often more convenient and less error-prone to refer to elements in the simulation by name rather than by index. Physics.named.model and Physics.named.data

<!-- chunk {"id": "body-0108", "role": "body", "section": "The Physics class", "weight": 1.0} -->

[⬇](data:text/plain;base64,cHJpbnQoIlRoZSBnZW9tX3hwb3MgYXJyYXk6IikKcHJpbnQocGh5c2ljcy5kYXRhLmdlb21feHBvcykKcHJpbnQoIklzIG11Y2ggZWFzaWVyIHRvIGluc3BlY3QgdXNpbmcgUGh5c2ljcy5uYW1lZCIpCnByaW50KHBoeXNpY3MubmFtZWQuZGF0YS5nZW9tX3hwb3Mp){download=""}

<!-- chunk {"id": "body-0109", "role": "body", "section": "The Physics class", "weight": 1.0} -->

print(\"The geom_xpos array:\")

<!-- chunk {"id": "body-0110", "role": "body", "section": "The Physics class", "weight": 1.0} -->

print(physics.data.geom_xpos)

<!-- chunk {"id": "body-0111", "role": "body", "section": "The Physics class", "weight": 1.0} -->

print(\"Is much easier to inspect using Physics.named\")

<!-- chunk {"id": "body-0112", "role": "body", "section": "The Physics class", "weight": 1.0} -->

print(physics.named.data.geom_xpos)

<!-- chunk {"id": "body-0113", "role": "body", "section": "The Physics class", "weight": 1.0} -->

[⬇](data:text/plain;base64,VGhlIGRhdGEuZ2VvbV94cG9zIGFycmF5OgpbWyAwLiAgIDAuICAgMC4gXQogWyAwLiAgIDAuICAgMC4zXQogWyAwLjIgIDAuMiAgMC41XV0KSXMgbXVjaCBlYXNpZXIgdG8gaW5zcGVjdCB1c2luZyBQaHlzaWNzLm5hbWVkOgogICAgICAgICAgIHggICAgICAgICB5ICAgICAgICAgegowICBmbG9vciBbIDAgICAgICAgICAwICAgICAgICAgMCAgICAgICBdCjEgICAgYm94IFsgMCAgICAgICAgIDAgICAgICAgICAwLjMgICAgIF0KMiBzcGhlcmUgWyAwLjIgICAgICAgMC4yICAgICAgIDAuNSAgICAgXQ==){download=""}

<!-- chunk {"id": "body-0114", "role": "body", "section": "The Physics class", "weight": 1.0} -->

Is much easier to inspect using Physics.named:

<!-- chunk {"id": "body-0115", "role": "body", "section": "The Physics class", "weight": 1.0} -->

[⬇](data:text/plain;base64,d2l0aCBwaHlzaWNzLnJlc2V0X2NvbnRleHQoKToKICBwaHlzaWNzLm5hbWVkLmRhdGEucXBvc1sidXBfZG93biJdID0gMC4xCnByaW50KHBoeXNpY3MubmFtZWQuZGF0YS5nZW9tX3hwb3NbImJveCIsIFsieCIsICJ6Il1dKQ==){download=""}

<!-- chunk {"id": "body-0116", "role": "body", "section": "The Physics class", "weight": 1.0} -->

physics.named.data.qpos\[\"up_down\"\] = 0.1

<!-- chunk {"id": "body-0117", "role": "body", "section": "The Physics class", "weight": 1.0} -->

print(physics.named.data.geom_xpos\[\"box\", \[\"x\", \"z\"\]\])

<!-- chunk {"id": "body-0118", "role": "body", "section": "The Physics class", "weight": 1.0} -->

[⬇](data:text/plain;base64,WyAwLiAgIDAuNF0=){download=""}

<!-- chunk {"id": "body-0119", "role": "body", "section": "The Physics class", "weight": 1.0} -->

Note that in the example above we use a joint name to index into the generalised position array qpos. Indexing into a multi-DoF ball or free joint would output the appropriate slice.

<!-- chunk {"id": "body-0120", "role": "body", "section": "The Physics class", "weight": 1.0} -->

[⬇](data:text/plain;base64,cGh5c2ljcy5tb2RlbC5pZDJuYW1lKDAsICJnZW9tIik=){download=""}

<!-- chunk {"id": "body-0121", "role": "body", "section": "The Physics class", "weight": 1.0} -->

[⬇](data:text/plain;base64,J2Zsb29yJw==){download=""}

<!-- chunk {"id": "body-0122", "role": "body", "section": "Benchmarking", "weight": 1.0} -->

We provide baselines for two commonly employed deep reinforcement learning algorithms A3C and DDPG, as well as the recently introduced D4PG. We refer to the relevant papers for algorithm motivation and details and here provide only hyperparameter, network architecture, and training configuration information (see relevant sections below).

<!-- chunk {"id": "body-0123", "role": "body", "section": "Benchmarking", "weight": 1.0} -->

We study both the case of learning with state derived features as observations and learning from raw-pixel inputs for all the tasks in the Control Suite. It is of course possible to look at control via combined state features and pixel features, but we do not study this case here. We present results for both final performance and learning curves that demonstrate aspects of data-efficiency and stability of training.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Benchmarking", "weight": 1.0} -->

Establishing baselines for reinforcement learning problems and algorithms is notoriously difficult. Though we describe results for well-functioning implementations of the algorithms we present, it may be possible to perform better on these tasks with the same algorithms. For a given algorithm we ran experiments with a similar network architecture, set of hyperparameters, and training configuration as described in the original papers. We ran a simple grid search for each algorithm to find a well performing setting for each (see details for grid searches below). We used the same hyperparameters across all of the tasks (i.e. so that nothing is tuned per-task). Thus, it should be possible to improve performance on a given task by tuning parameters with respect to performance for that specific task. For these reasons, the results are not presented as upper bounds for performance with these algorithms, but rather as a starting point for comparison. It is also worth noting that we have not made a concerted effort to maximise data efficiency, for example by making many mini-batch updates using the replay buffer per step in the environment, as in Popov et al..

<!-- chunk {"id": "body-0125", "role": "body", "section": "Benchmarking", "weight": 1.0} -->

The following pseudocode block demonstrates how to load a single task in the benchmark suite, run a single episode with a random agent, and compute the reward as we do for the results reported here. Note that we run each environment for 1000 time steps and sum the rewards provided by the environment after each call to step. Thus, the maximum possible score for any task is 1000. For many tasks, the practical maximum is significantly less than 1000 since it may take many steps until it's possible to drive the system into a state that gives a full reward of 1.0 each time step.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Benchmarking", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZnJvbSBkbV9jb250cm9sIGltcG9ydCBzdWl0ZQoKZW52ID0gc3VpdGUubG9hZChkb21haW5fbmFtZSwgdGFza19uYW1lKQoKc3BlYyA9IGVudi5hY3Rpb25fc3BlYygpCnRpbWVfc3RlcCA9IGVudi5yZXNldCgpCnRvdGFsX3Jld2FyZCA9IDAuMApmb3IgXyBpbiByYW5nZSgxMDAwKToKICBhY3Rpb24gPSBucC5yYW5kb20udW5pZm9ybShzcGVjLm1pbmltdW0sIHNwZWMubWF4aW11bSwgc3BlYy5zaGFwZSkKICB0aW1lX3N0ZXAgPSBlbnYuc3RlcChhY3Rpb24pCiAgdG90YWxfcmV3YXJkICs9IHRpbWVfc3RlcC5yZXdhcmQ=){download=""}

<!-- chunk {"id": "body-0127", "role": "body", "section": "Benchmarking", "weight": 1.0} -->

env = suite.load(domain_name, task_name)

<!-- chunk {"id": "body-0128", "role": "body", "section": "Benchmarking", "weight": 1.0} -->

action = np.random.uniform(spec.minimum, spec.maximum, spec.shape)

<!-- chunk {"id": "body-0129", "role": "body", "section": "Benchmarking", "weight": 1.0} -->

time_step = env.step(action)

<!-- chunk {"id": "body-0130", "role": "body", "section": "Benchmarking", "weight": 1.0} -->

total_reward += time_step.reward

<!-- chunk {"id": "body-0131", "role": "body", "section": "Benchmarking", "weight": 1.0} -->

In the state feature case we ran 15 different seeds for each task with A3C and DDPG; for results with D4PG, which was generally found to be more stable, we ran 5 seeds. In the raw-pixel case we also ran 5 different seeds for each task. The seed sets the network weight initialisation for the associated run. In all cases, initial network weights were sampled using standard TensorFlow initialisers. In the figures showing performance on individual tasks (Figures 4-7), the lines denote the median performance and the shaded regions denote the 5^th^ and 95^th^ percentiles across seeds. In the tables showing performance for individual tasks (Tables 1 & 2) we report means and standard errors across seeds.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Benchmarking", "weight": 1.0} -->

As well as studying performance on individual tasks, we examined the performance of algorithms across all tasks by plotting a simple aggregate measure. Figure 3 shows the mean performance over environment steps and wallclock time for both state features and raw-pixels. These measures are of particular interest: they offer a view into the generality of a reinforcement learning algorithm. In this aggregate view, it is clear that D4PG is the best performing agent in all metrics, with the exception that DDPG is more data efficient before $1e7$ environment steps. It is worth noting that the data efficiency for D4PG can be improved over DDPG by simply reducing the number of actor threads for D4PG (experiments not shown here), since with 32 actors D4PG is somewhat wasteful of environment data (with the benefit of being more efficient in terms of wall-clock).

<!-- chunk {"id": "body-0133", "role": "body", "section": "Benchmarking", "weight": 1.0} -->

While we have made a concerted effort to ensure reproducible benchmarks, it's worth noting that there remain uncontrolled aspects that introduce variance into the evaluations. For example, some tasks have a randomly placed target or initialisation of the model, and the sequence of these are not fixed across runs. Thus, each learning run will see a different sequence of episodes, which will lead to variance in performance. This might be fixed by introducing a fixed sequence of initialisation for episodes, but this is not in any case a practical solution for the common case of parallelised training, so our benchmarks simply reflect variability in episode initialisation sequence.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Algorithm and Architecture Details", "weight": 1.0} -->

: Mnih et al. proposed a version of the Advantage Actor Critic that could be trained asynchronously (A3C). Here we report results for the A3C trained with 32 workers per task. The network consisted of 2 MLP layers shared between actor and critic with 256 units in the first hidden layer.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Algorithm and Architecture Details", "weight": 1.0} -->

The grid search explored: learning rates, $\eta \in$ \[1e-2, 1e-3, 1e-4, 1e-5, 3e-5, 4e-5, 5e-5\]; unroll length $t_{\max} \in {\lbrack 20,100,1000\rbrack}$; activation functions for computing ${{\log\sigma}{( \cdot )}} \in {\lbrack{{Softplus}{(x)}},{\exp{({\log{({0.01 + {2\text{sigmoid}{(x)}}})}})}}\rbrack}$; number of units in the second hidden layer $\in {\lbrack 128,256\rbrack}$; annealing of learning rate $\in {\lbrack{true},{false}\rbrack}$. The advantage baseline was computed using a linear layer after the second hidden layer.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Algorithm and Architecture Details", "weight": 1.0} -->

Actions were sampled from a multivariate Gaussian with diagonal covariance, parameterized by the output vectors $\mu$ and $\sigma^{2}$. The value of the logarithm of $\sigma$ was computed using the second sigmoid activation function given above (which was found to be more stable than the ${Softplus}{(x)}$ function used in the original A3C manuscript), while $\mu$ was computed from a hyperbolic tangent, both stemming from the second MLP layer. The RMSProp optimiser was used with a decay factor of $\alpha = 0.99$, a damping factor of $\epsilon = 0.1$ and a learning rate starting at ${5e} - 5$ and annealed to $0$ throughout training using a linear schedule, with no gradient clipping. An entropy regularisation cost weighted at $\beta = {{3e} - 3}$ was added to the policy loss.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Algorithm and Architecture Details", "weight": 1.0} -->

: Lillicrap et al. presented a Deep Deterministic Policy Gradients (DDPG) agent that performed well on an early version of the Control Suite. Here we present performance for straightforward single actor/learner implementation of the DDPG algorithm. Both actor and critic networks were MLPs with ReLU nonlinearities. The actor network had two layers of $300\rightarrow 200$ units respectively, while the critic network had two layers of $400\rightarrow 300$ units. The action vector was passed through a linear layer and summed up with the activations of the second critic layer in order to compute Q values.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Algorithm and Architecture Details", "weight": 1.0} -->

The grid search explored: discount factors, $\lambda \in {\lbrack 0.95,0.99\rbrack}$; learning rates, $\eta \in {\lbrack{{1e} - 2},{{1e} - 3},{{1e} - 4},{{1e} - 5}\rbrack}$ fixed to be the same for both networks; damping and spread parameters for the Ornstein--Uhlenbeck process, $\theta \in {\lbrack 0,0.15,0.85,1\rbrack}$ and $\mu \in {\lbrack 0.1,0.2,0.3,0.4\rbrack}$ respectively; hard (swap at intervals of 100 steps) versus soft ($\tau = {{1e} - 3}$) target updates.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Algorithm and Architecture Details", "weight": 1.0} -->

For the results shown here the two networks were trained with independent Adam optimisers Kingma and Ba, both with a learning rate of $\eta = {{1e} - 4}$, with gradients clipped at $\lbrack{- 1},1\rbrack$ for the actor network. The agent used discounting of $\lambda = 0.99$. As in the paper, we used a target network with soft updates and an Ohrstein-Uhlenbeck process to add an exploration noise that is correlated in time, with similar parameters, except for a slightly bigger $\sigma$ ($\theta = 0.15$, $\sigma = 0.3$, $\tau = {{1e} - 3}$). The replay buffer size was also kept to $1e6$, and training was done with a minibatch size of $64$.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Algorithm and Architecture Details", "weight": 1.0} -->

: The Distributional Distributed Deep Deterministic Policy Gradients algorithm extends regular DDPG with the following features: First, the critic value function is modelled as a categorical distribution, using 101 categories spaced evenly across $\lbrack{- 150},150\rbrack$. Second, acting and learning are decoupled and deployed on separate machines using the Ape-X architecture described. We used 32 CPU-based actors and a single GPU-based learner for benchmarking. D4PG additionally applies $N$-step returns with $N = 5$, and non-uniform replay sampling ($\alpha_{\text{sample}} = 0.6$) and eviction ($\alpha_{\text{evict}} = 0.6$) strategies using a sample-based distributional KL loss (see and for details). D4PG hyperparameters were the same as those used for DDPG, with the exception that hard target network updates are applied every 100 steps, and exploration noise is sampled from a Gaussian distribution with fixed $\sigma$ varying from $1/32$ to $1$ across the actors.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Learning from state features", "weight": 1.0} -->

Due to the different parallelization architectures, the evaluation protocol for each agent was slightly different: DDPG was evaluated for 10 episodes for every 100000 steps (with no exploration noise), and A3C was trained with 32 workers and concurrently evaluated with another worker that updated its parameters every 3 episodes, which produced intervals of on average 96000 steps per update. The plots in Figure 4 and Figure 5 show the median and the 5th and 95th percentile of the returns for the first $1e8$ steps. Each agent was run 15 times per task using different seeds (except for D4PG which was run 5 times), using only low-dimensional state feature information. D4PG tends to achieve better results in nearly all of the tasks. Notably, it manages to reliably solve the manipulator:bring_ball task, and achieves a good performance in acrobot tasks. We found that part of the reason the agent did not go above $600$ in the acrobot task is due to the time it takes for the pendulum to be swung up, so its performance is probably close to the upper bound.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Learning from pixels", "weight": 1.0} -->

The DeepMind Control Suite can be configured to produce observations containing any combination of state vectors and pixels generated from the provided cameras. We also benchmarked a variant of D4PG that learns directly from pixel-only input, using $84 \times 84$ RGB frames from the $0^{th}$ camera. To process pixel input, D4PG is augmented with a simple 2-layer ConvNet. Both kernels are size $3 \times 3$ with 32 channels and ELU activation, and the first layer has stride 2. The output is fed through a single fully-connected layer with 50 neurons, with layer normalisation Ba et al. and tanh activations. We explored four variants of the algorithm. In the first, there were separate networks for the actor and Q-critic. In the other three, the actor and critic shared the convolutional layers, and the actor and critic each had a separate fully connected layer before their respective outputs.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Learning from pixels", "weight": 1.0} -->

The best performance was obtained by weight-sharing the convolutional kernel weights between the actor and critic networks, and only allowing these weights to be updated by the critic optimiser (i.e. truncating the policy gradients after the actor MLP). D4Pixels internally frame-stacks 3 consecutive observations as the ConvNet input.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Learning from pixels", "weight": 1.0} -->

Results for 1 day of running time are shown in Figure 7; we plot the results for the three shared-weights variants of D4PG, with gradients into the ConvNet from the actor (dotted green), critic (dashed green), or both (solid green). For the sake of comparison, we plot D4PG performance for low-dimensional features (solid blue) from Figure 5. The variant that employed separate networks for actor and critic performed significantly worse than the best of these and is not shown. Learning from pixel-only input is successful on many of the tasks, but fails completely in some cases. It is worth noting that the camera view for some of the task domains are not well suited to a pixel-only solution for the task. Thus, some of the failure cases are likely due to the difficulty of positioning a camera that simultaneously captures both the navigation targets as well as the details of the agents body: e.g., in the case of swimmer:swimmer6 and swimmer15 as well as fish:swim.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Conclusion and future work", "weight": 1.5} -->

The DeepMind Control Suite is a starting place for the design and performance comparison of reinforcement learning algorithms for physics-based control. It offers a wide range of tasks, from near-trivial to quite difficult. The uniform reward structure allows for robust suite-wide performance measures.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Conclusion and future work", "weight": 1.5} -->

The results presented here for A3C, DDPG, and D4PG constitute baselines using, to the best of our knowledge, well performing implementations of these algorithms. At the same time, we emphasise that the learning curves are not based on exhaustive hyperparameter optimisation, and that for a given algorithm the same hyperparameters were used across all tasks in the Control Suite. Thus, we expect that it may be possible to obtain better performance or data efficiency, especially on a per-task basis.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Conclusion and future work", "weight": 1.5} -->

We are excited to be sharing the Control Suite with the wider community and hope that it will be found useful. We look forward to the diverse research the Suite may enable, and to integrating community contributions in future releases.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Future work", "weight": 1.5} -->

Several elements are missing from the current release of the Control Suite.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Future work", "weight": 1.5} -->

Some features, like the lack of rich tasks, are missing by design. The Suite, and particularly the benchmarking set of tasks, is meant to be a stable, simple starting point for learning control. Task categories like full manipulation and locomotion in complex terrains require reasoning about a distribution of tasks and models, not only initial states. These require more powerful tools which we hope to share in the future in a different branch.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Future work", "weight": 1.5} -->

There are several features that we hoped to include but did not make it into this release; we intend to add these in the future. They include: a quadrupedal locomotion task, an interactive visualiser with which to view and perturb the simulation, support for C callbacks and multi-threaded dynamics, a MuJoCo TensorFlow op wrapper and Windows™ support.
