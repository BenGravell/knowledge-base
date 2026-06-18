## Introduction

Controlling the physical world is an integral part and arguably a prerequisite of general intelligence. Indeed, the only known example of general-purpose intelligence emerged in primates which had been manipulating the world for millions of years.

Physical control tasks share many common properties and it is sensible to consider them as a distinct class of behavioural problems. Unlike board games, language and other symbolic domains, physical tasks are fundamentally continuous in state, time and action. Their dynamics are subject to second-order equations of motion, implying that the underlying state is composed of position-like and velocity-like variables, while state derivatives are acceleration-like. Sensory signals (i.e. observations) usually carry meaningful physical units and vary over corresponding timescales.

This decade has seen rapid progress in the application of Reinforcement Learning (RL) techniques to difficult problem domains such as video games. The Arcade Learning Environment was a vital facilitator of these developments, providing a set of standard benchmarks for evaluating and comparing learning algorithms. The DeepMind Control Suite provides a similar set of standard benchmarks for continuous control problems.

The OpenAI Gym currently includes a set of continuous control domains that has become the de-facto benchmark in continuous RL. The Control Suite is also a set of tasks for benchmarking continuous RL algorithms, with a few notable differences. We focus exclusively on continuous control, e.g. separating observations with similar units (position, velocity, force etc.) rather than concatenating into one vector. Our unified reward structure (see below) offers interpretable learning curves and aggregated suite-wide performance measures. Furthermore, we emphasise high-quality well-documented code using uniform design patterns, offering a readable, transparent and easily extensible codebase. Finally, the Control Suite has equivalent domains to all those in the Gym while adding many more^11^1With the notable exception of Philipp Moritz's "ant" quadruped, which we intend to replace soon, see Future Work..

In Section 2 we explain the general structure of the Control Suite and in Section 3 we describe each domain in detail. In Sections 4 and 5 we document the high and low-level Python APIs, respectively. Section 6 is devoted to our benchmarking results. We then conclude and provide a roadmap for future development.

## Structure and Design

The DeepMind Control Suite is a set of stable, well-tested continuous control tasks that are easy to use and modify. Tasks are written in \\hrefhttps://www.python.org/Python and physical models are defined using \\hrefhttp://mujoco.org/book/modeling.htmlMJCF. Standardised action, observation and reward structures make benchmarking simple and learning curves easy to interpret.

### Model and Task verification

Verification in this context means making sure that the physics simulation is stable and that the task is solvable:

Simulated physics can easily destabilise and diverge, mostly due to errors introduced by time discretisation. Smaller time-steps are more stable, but require more computation per unit simulation time, so the choice of time-step is always a trade-off between stability and speed. What's more, learning agents are better at discovering and exploiting instabilities.^22^2This phenomenon, sometimes known as Sims' Law, was first articulated in: "Any bugs that allow energy leaks from non-conservation, or even round-off errors, will inevitably be discovered and exploited".

It is surprisingly easy to write tasks that are much easier or harder than intended, that are impossible to solve or that can be solved by very different strategies than expected (i.e. "cheats"). To prevent these situations, the Atari™ games that make up ALE were extensively tested over more than 10 man-years^33^3Marc Bellemare, personal communication.. However, continuous control domains cannot be solved by humans, so a different approach must be taken.

In order to tackle both of these challenges, we ran variety of learning agents against all tasks, and iterated on each task's design until we were satisfied that the physics was stable and non-exploitable, and that the task is solved correctly by at least one agent. Tasks that are solvable by some learning agent were collated into the benchmarking set. Tasks were not solved by any learning agent are in the extra set of tasks.

### Reinforcement Learning

A continuous Markov Decision Process (MDP) is given by a set of states $\mathcal{S}$, a set of actions $\mathcal{A}$, a dynamics (transition) function $\mathbf{f}{(\mathbf{s},\mathbf{a})}$, an observation function $\mathbf{o}{(\mathbf{s},\mathbf{a})}$ and a scalar reward function $r{(\mathbf{s},\mathbf{a})}$.

: The state $\mathbf{s}$ is a vector of real numbers $\mathcal{S} \equiv {\mathbb{R}}^{\dim{(\mathcal{S})}}$, with the exception of spatial orientations which are represented by unit quaternions $\in {SU{}}$. States are initialised in some subset $\mathcal{S}_{\text{0}} \subseteq \mathcal{S}$ by the begin_episode() method. To avoid memorised "rote" solutions $\mathcal{S}_{\text{0}}$ is never a single state.

: With the exception of the LQR domain (see below), the action vector is in the unit box $\mathbf{a} \in \mathcal{A} \equiv \left\lbrack {- 1},1 \right\rbrack^{\dim{(\mathcal{A})}}$.

: While the state notionally evolves according to a continuous ordinary differential equation $\overset{˙}{\mathbf{s}} = {\mathbf{f}_{c}{(\mathbf{s},\mathbf{a})}}$, in practice temporal integration is discrete^44^4Most domains use MuJoCo's default semi-implicit Euler integrator, a few which have smooth, nearly energy-conserving dynamics use 4th-order Runge Kutta. with some fixed, finite time-step: $\mathbf{s}_{t + h} = {\mathbf{f}{(\mathbf{s}_{t},\mathbf{a}_{t})}}$.

: The function $\mathbf{o}{(\mathbf{s},\mathbf{a})}$ describes the observations available to the learning agent. With the exception of point-mass:hard (see below), all tasks are strongly observable, i.e. the state can be recovered from a single observation. Observation features which depend only on the state (position and velocity) are functions of the current state. Features which are also dependent on controls (e.g. touch sensor readings) are functions of the previous transition. Observations are implemented as a Python OrderedDict.

: The range of rewards in the Control Suite, with the exception of the LQR domain, are in the unit interval ${r{(\mathbf{s},\mathbf{a})}} \in {\lbrack 0,1\rbrack}$. Some tasks have "sparse" rewards ${r{(\mathbf{s},\mathbf{a})}} \in {\{ 0,1\}}$. This structure is facilitated by the tolerance() function, see Figure 2. Since terms produced by tolerance() are in the unit interval, both *averaging* and *multiplication* operations maintain that property, facillitating cost design.

Termination and Discount:

: Control problems are classified as finite-horizon, first-exit and infinite-horizon. Control Suite tasks have no terminal states or time limit and are therefore of the infinite-horizon variety. Notionally the objective is the continuous-time infinite-horizon average return $\lim_{T\rightarrow\infty}{T^{- 1}{\int_{0}^{T}{r{(\mathbf{s}_{t},\mathbf{a}_{t})}{dt}}}}$, but in practice all of our agents internally use the discounted formulation $\int_{0}^{\infty}{e^{- {t/\tau}}r{(\mathbf{s}_{t},\mathbf{a}_{t})}{dt}}$ or, in discrete time $\sum_{i = 0}^{\infty}{\gamma^{i}r{(\mathbf{s}_{i},\mathbf{a}_{i})}}$, where $\gamma = e^{- {h/\tau}}$ is the discount factor. In the limit $\tau\rightarrow\infty$ (equivalently $\gamma\rightarrow 1$), the policies of the discounted-horizon and average-return formulations are identical.

: While agents are expected to optimise for infinite-horizon returns, these are difficult to measure. As a proxy we use fixed-length episodes of 1000 time steps. Since all reward functions are designed so that $r \approx 1$ at or near a goal state, learning curves measuring total returns all have the same y-axis limits of $\lbrack\mathbf{0},\mathbf{1}\mathbf{0}\mathbf{0}\mathbf{0}\rbrack$, making them easier to interpret.

Figure 2: The tolerance(x, bounds=(lower, upper)) function will return 1 if x is within the bounds interval and 0 otherwise. If the optional margin argument is given, the output will decrease smoothly with distance from the interval, taking a value of value_at_margin at a distance of margin. Several types of sigmoid-like functions are available. Top: Three infinite-support sigmoids, for which value_at_margin must be positive. Bottom: Three finite-support support sigmoids with value_at_margin=0.

### MuJoCo physics

MuJoCo is a fast, minimal-coordinate, continuous-time physics engine. It compares favourably to other popular engines, especially for articulated, low-to-medium degree-of-freedom (DoF) models in contact with other bodies. The convenient \\hrefhttp://mujoco.org/book/modeling.htmlMJCF definition format and reconfigurable computation pipeline have made MuJoCo popular^55^5Along with the MultiBody branch of the \\hrefhttp://bulletphysics.org/wordpress/Bullet physics engine. for robotics and reinforcement learning research.

## Domains and Tasks

A domain refers to a physical model, while a task refers to an instance of that model with a particular MDP structure. For example the difference between the swingup and balance tasks of the cartpole domain is whether the pole is initialised pointing downwards or upwards, respectively. In some cases, e.g. when the model is procedurally generated, different tasks might have different physical properties. Tasks in the Control Suite are collated into tuples according predefined tags. In particular, tasks used for benchmarking are in the BENCHMARKING tuple, while those not used for benchmarking (because they are particularly difficult, or because they don't conform to the standard structure) are in the EXTRA tuple. All suite tasks are accessible via the ALL_TASKS tuple. In the domain descriptions below, names are followed by three integers specifying the dimensions of the state, control and observation spaces i.e. $\left( {\dim{(\mathcal{S})}},{\dim{(\mathcal{A})}},{\dim{(\mathcal{O})}} \right)$.

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Pendulum: The classic inverted pendulum. The torque-limited actuator is 1/6th as strong as required to lift the mass from motionless horizontal, necessitating several swings to swing up and balance. The swingup task has a simple sparse reward: 1 when the pole is within 30∘ of the vertical and 0 otherwise.

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Acrobot: The underactuated double pendulum, torque applied to the second joint. The goal is to swing up and balance. Despite being low-dimensional, this is not an easy control problem. The physical model conforms to rather than the earlier. Both swingup and swingup_sparse tasks with smooth and sparse rewards, respectively.

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Cart-pole: Swing up and balance an unactuated pole by applying forces to a cart at its base. The physical model conforms to. Four benchmarking tasks: in swingup and swingup_sparse the pole starts pointing down while in balance and balance_sparse the pole starts near the upright.

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.585]figure[\FBwidth]
Cart-k-pole (2 k + 2, 1, 3 k + 2): The cart-pole domain allows to procedurally adding more poles, connected serially. Two non-benchmarking tasks, two_poles and three_poles are available.

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Ball in cup: A planar ball-in-cup task. An actuated planar receptacle can translate in the vertical plane in order to swing and catch a ball attached to its bottom. The catch task has a sparse reward: 1 when the ball is in the cup, 0 otherwise.

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Point-mass: A planar point-mass receives a reward of 1 when within a target at the origin. In the easy task, one of simplest in the suite, the 2 actuators correspond to the global x and y axes. In the hard task the gain matrix from the controls to the axes is randomised for each episode, making it impossible to solve by memory-less agents; this task is not in the benchmarking set.

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Reacher: The simple two-link planar reacher with a randomised target location. The reward is one when the end effector penetrates the target sphere. In the easy task the target sphere is bigger than on the hard task (shown on the left).

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Finger: A 3-DoF toy manipulation problem based on. A planar ‘finger’ is required to rotate a body on an unactuated hinge. In the turn_easy and turn_hard tasks, the tip of the free body must overlap with a target (the target is smaller for the turn_hard task). In the spin task, the body must be continually rotated.

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Hopper: The planar one-legged hopper introduced in, initialised in a random configuration. In the stand task it is rewarded for bringing its torso to a minimal height. In the hop task it is rewarded for torso height and forward velocity.

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Fish: A fish is required to swim to a target. This domain relies on MuJoCo’s simplified fluid dynamics. Two tasks: in the upright task, the fish is rewarded only for righting itself with respect to the vertical, while in the swim task it is also rewarded for swimming to the target.

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Cheetah: A running planar biped based on. The reward r is linearly proportional to the forward velocity v up to a maximum of 10m/s i.e. r (v) = max (0,min (v/10,1)).

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Walker: An improved planar walker based on the one introduced in. In the stand task reward is a combination of terms encouraging an upright torso and some minimal torso height. The walk and run tasks include a component encouraging forward velocity.

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Manipulator: A planar manipulator is rewarded for bringing an object to a target location. In order to assist with exploration, in %10 of episodes the object is initialised in the gripper or at the target. Four manipulator tasks: {bring,insert}_{ball,peg} of which only bring_ball is in the benchmarking set. The other three are shown below.

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.415]figure[\FBwidth]
Manipulator extra: insert_ball: place the ball in the basket. bring_peg: bring the peg to the target peg (matching orientation). insert_peg: insert the peg into the slot.

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Stacker (6 k + 16, 5, 11 k + 26): Stack k boxes. Reward is given when a box is at the target and the gripper is away from the target, making stacking necessary. The height of the target is sampled uniformly from {1, …, k}.

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Swimmer (2 k + 4, k − 1, 4 k + 1): This procedurally generated k-link planar swimmer is based on but using MuJoCo’s high-Reynolds fluid drag model. A reward of 1 is provided when the nose is inside the target and decreases smoothly with distance like a Lorentzian. The two instantiations provided in the benchmarking set are the 6-link and 15-link swimmers.

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Humanoid: A simplified humanoid with 21 joints, based on the model in. Three tasks: stand, walk and run are differentiated by the desired horizontal speed of 0, 1 and 10m/s, respectively. Observations are in an egocentric frame and many movement styles are possible solutions e.g. running backwards or sideways. This facilitates exploration of local optima.

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Humanoid_CMU: A humanoid body with 56 joints, adapted from and based on the ASF model of subject #8 in the CMU Motion Capture Database. This domain has the same stand, walk and run tasks as the simpler humanoid. We include tools for parsing and playback of the CMU MoCap data, see below.

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
LQR (2n, m, 2n): n masses, of which m ≤ n are actuated, move on linear joints which are connected serially. The reward is a quadratic in the position and controls. Analytic transition and control-gain matrices are extracted from MuJoCo and the optimal policy and value functions are computed in lqr_solver.py using Riccati iterations. Since both controls and reward are unbounded, LQR is not in the benchmarking set.

### CMU Motion Capture Data

We enable humanoid_CMU to be used for imitation learning as in Merel et al. by providing tools for parsing, conversion and playback of human motion capture data from the CMU Motion Capture Database. The convert() function in the parse_amc module loads an AMC data file and returns a sequence of configurations for the humanoid_CMU model. The example script CMU_mocap_demo.py uses this function to generate a video.

## Reinforcement learning API

In this section we describe the following Python code:

The environment.Base class that defines generic RL interface.

The suite module that contains the domains and tasks defined in Section 3

The underlying MuJoCo bindings and the mujoco.Physics class that provides most of the functionality needed to interact with an instantiated MJCF model.

### The RL Environment class

The class environment.Base, found within the dm_control.rl.environment module, defines the following abstract methods:

$\bullet$ action_spec() and observation_spec()

: describe the actions accepted and the observations returned by an Environment. For all the tasks in the suite, actions are given as a single NumPy array. action_spec() returns an ArraySpec, with attributes describing the shape, data type, and optional minimum and maximum bounds for the action arrays. Observations consist of an OrderedDict containing one or more NumPy arrays. observation_spec() returns an OrderedDict of ArraySpecs describing the shape and data type of each corresponding observation.

$\bullet$ reset() and step()

: respectively start a new episode, and advance time given an action.

Starting an episode and running it to completion might look like

[⬇](data:text/plain;base64,c3BlYyA9IGVudi5hY3Rpb25fc3BlYygpCnRpbWVfc3RlcCA9IGVudi5yZXNldCgpCndoaWxlIG5vdCB0aW1lX3N0ZXAubGFzdCgpOgogIGFjdGlvbiA9IG5wLnJhbmRvbS51bmlmb3JtKHNwZWMubWluaW11bSwgc3BlYy5tYXhpbXVtLCBzcGVjLnNoYXBlKQogIHRpbWVfc3RlcCA9IGVudi5zdGVwKGFjdGlvbik=){download=""}

spec = env.action_spec()

time_step = env.reset()

while not time_step.last():

action = np.random.uniform(spec.minimum, spec.maximum, spec.shape)

time_step = env.step(action)

Both reset() and step() return a TimeStep namedtuple with fields \[step_type, reward, discount, observation\]:

$\bullet$ step_type

: is an enum taking a value in \[FIRST, MID, LAST\]. The convenience methods first(), mid() and last() return boolean values indicating whether the TimeStep's type is of the respective value.

: is a scalar float $\gamma \in {\lbrack 0,1\rbrack}$.

: is an OrderedDict of NumPy arrays matching the specification returned by observation_spec().

Whereas the step_type specifies whether or not the episode is terminating, it is the discount $\gamma$ that determines the termination type. $\gamma = 0$ corresponds to a terminal state^66^6i.e. where the sum of future reward is equal to the current reward. as in the first-exit or finite-horizon formulations. A terminal TimeStep with $\gamma = 1$ corresponds to the infinite-horizon formulation. In this case an agent interacting with the environment should treat the episode as if it could have continued indefinitely, even though the sequence of observations and rewards is truncated. All Control Suite tasks with the exception of LQR^77^7The LQR task terminates with $\gamma = 0$ when the state is very close to 0, which is a proxy for the infinite exponential convergence of stabilised linear systems. return $\gamma = 1$ at every step, including on termination.

### The suite module

To load an environment representing a task from the suite, use suite.load():

[⬇](data:text/plain;base64,ZnJvbSBkbV9jb250cm9sIGltcG9ydCBzdWl0ZQoKIyBMb2FkIG9uZSB0YXNrOgplbnYgPSBzdWl0ZS5sb2FkKGRvbWFpbl9uYW1lPSJjYXJ0cG9sZSIsIHRhc2tfbmFtZT0ic3dpbmd1cCIpCgojIEl0ZXJhdGUgb3ZlciBhIHRhc2sgc2V0Ogpmb3IgZG9tYWluX25hbWUsIHRhc2tfbmFtZSBpbiBzdWl0ZS5CRU5DSE1BUktJTkc6CiAgZW52ID0gc3VpdGUubG9hZChkb21haW5fbmFtZSwgdGFza19uYW1lKQogIC4uLg==){download=""}

from dm_control import suite

\# Load one task:

env = suite.load(domain_name=\"cartpole\", task_name=\"swingup\")

\# Iterate over a task set:

for domain_name, task_name in suite.BENCHMARKING:

env = suite.load(domain_name, task_name)

Wrappers can be used to modify the behaviour of control environments:

By default, Control Suite environments return low-dimensional feature observations. The pixel.Wrapper adds or replaces these with images.

[⬇](data:text/plain;base64,ZnJvbSBkbV9jb250cm9sLnN1aXRlLndyYXBwZXJzIGltcG9ydCBwaXhlbHMKZW52ID0gc3VpdGUubG9hZCgiY2FydHBvbGUiLCAic3dpbmd1cCIpCmVudl9hbmRfcGl4ZWxzID0gcGl4ZWxzLldyYXBwZXIoZW52KQojIFJlcGxhY2UgZXhpc3RpbmcgZmVhdHVyZXMgYnkgcGl4ZWwgb2JzZXJ2YXRpb25zLgplbnZfb25seV9waXhlbHMgPSBwaXhlbHMuV3JhcHBlcihlbnYsIHBpeGVsX29ubHk9RmFsc2UpCiMgUGl4ZWwgb2JzZXJ2YXRpb25zIGluIGFkZGl0aW9uIHRvIGV4aXN0aW5nIGZlYXR1cmVzLg==){download=""}

from dm_control.suite.wrappers import pixels

env = suite.load(\"cartpole\", \"swingup\")

env_and_pixels = pixels.Wrapper(env)

\# Replace existing features by pixel observations.

env_only_pixels = pixels.Wrapper(env, pixel_only=False)

\# Pixel observations in addition to existing features.

Models in the Control Suite use a common set of colours and textures for visual uniformity. As illustrated in the \\hrefhttps://youtu.be/rAai4QzcYbsvideo, this also allows us to modify colours in proportion to the reward, providing a convenient visual cue.

[⬇](data:text/plain;base64,ZW52ID0gc3VpdGUubG9hZCgiZmlzaCIsICJzd2ltIiwgdGFza19rd2FyZ3MsIHZpc3VhbGl6ZV9yZXdhcmQ9VHJ1ZSk=){download=""}

env = suite.load(\"fish\", \"swim\", task_kwargs, visualize_reward=True)

## MuJoCo Python interface

While the environment.Base class is specific to the Reinforcement Learning scenario, the underlying bindings and mujoco.Physics class provide a general-purpose wrapper of the MuJoCo engine. We use Python's \\hrefhttps://docs.python.org/3/library/ctypes.htmlctypes library to bind to MuJoCo structs, enums and functions.

The bindings provide easy access to all MuJoCo library functions, automatically converting NumPy arrays to data pointers where appropriate.

[⬇](data:text/plain;base64,ZnJvbSBkbV9jb250cm9sLm11am9jby53cmFwcGVyLm1qYmluZGluZ3MgaW1wb3J0IG1qbGliCmltcG9ydCBudW1weSBhcyBucAoKcXVhdCA9IG5wLmFycmF5KCguNSwgLjUsIC41LCAuNSkpCm1hdCA9IG5wLnplcm9zKCg5KSkKbWpsaWIubWp1X3F1YXQyTWF0KG1hdCwgcXVhdCkKCnByaW50KCJNdUpvQ28gY2FuIGNvbnZlcnQgdGhpcyBxdWF0ZXJuaW9uOiIpCnByaW50KHF1YXQpCnByaW50KCJUbyB0aGlzIHJvdGF0aW9uIG1hdHJpeDoiKQpwcmludChtYXQucmVzaGFwZSgzLDMpKQ==){download=""}

from dm_control.mujoco.wrapper.mjbindings import mjlib

mjlib.mju_quat2Mat(mat, quat)

print(\"MuJoCo can convert this quaternion:\")

print(\"To this rotation matrix:\")

print(mat.reshape)

[⬇](data:text/plain;base64,TXVKb0NvIGNhbiBjb252ZXJ0IHRoaXMgcXVhdGVybmlvbjoKWyAwLjUgIDAuNSAgMC41ICAwLjVdClRvIHRoaXMgcm90YXRpb24gbWF0cml4OgpbWyAwLiAgMC4gIDEuXQogWyAxLiAgMC4gIDAuXQogWyAwLiAgMS4gIDAuXV0=){download=""}

MuJoCo can convert this quaternion:

To this rotation matrix:

[⬇](data:text/plain;base64,ZnJvbSBkbV9jb250cm9sLm11am9jby53cmFwcGVyLm1qYmluZGluZ3MgaW1wb3J0IGVudW1zCnByaW50KGVudW1zLm1qdEpvaW50KQ==){download=""}

from dm_control.mujoco.wrapper.mjbindings import enums

print(enums.mjtJoint)

[⬇](data:text/plain;base64,bWp0Sm9pbnQobWpKTlRfRlJFRT0wLCBtakpOVF9CQUxMPTEsIG1qSk5UX1NMSURFPTIsIG1qSk5UX0hJTkdFPTMp){download=""}

mjtJoint(mjJNT_FREE=0, mjJNT_BALL=1, mjJNT_SLIDE=2, mjJNT_HINGE=3)

### The Physics class

The Physics class encapsulates MuJoCo's most commonly used functionality.

: Loading an MJCF model

The Physics.from_xml_string() method loads an MJCF model and returns a Physics instance:

[⬇](data:text/plain;base64,c2ltcGxlX01KQ0YgPSAiIiIKPG11am9jbz4KICA8d29ybGRib2R5PgogICAgPGxpZ2h0IG5hbWU9InRvcCIgcG9zPSIwIDAgMS41Ii8+CiAgICA8Z2VvbSBuYW1lPSJmbG9vciIgdHlwZT0icGxhbmUiIHNpemU9IjEgMSAuMSIvPgogICAgPGJvZHkgbmFtZT0iYm94IiBwb3M9IjAgMCAuMyI+CiAgICAgIDxqb2ludCBuYW1lPSJ1cF9kb3duIiB0eXBlPSJzbGlkZSIgYXhpcz0iMCAwIDEiLz4KICAgICAgPGdlb20gbmFtZT0iYm94IiB0eXBlPSJib3giIHNpemU9Ii4yIC4yIC4yIiByZ2JhPSIxIDAgMCAxIi8+CiAgICAgIDxnZW9tIG5hbWU9InNwaGVyZSIgcG9zPSIuMiAuMiAuMiIgc2l6ZT0iLjEiIHJnYmE9IjAgMSAwIDEiLz4KICAgIDwvYm9keT4KICA8L3dvcmxkYm9keT4KPC9tdWpvY28+CiIiIgpwaHlzaWNzID0gbXVqb2NvLlBoeXNpY3MuZnJvbV94bWxfc3RyaW5nKHNpbXBsZV9NSkNGKQ==){download=""}

physics = mujoco.Physics.from_xml_string(simple_MJCF)

The Physics.render() method outputs a numpy array of pixel values.

[⬇](data:text/plain;base64,cGl4ZWxzID0gcGh5c2ljcy5yZW5kZXIoKQ==){download=""}

pixels = physics.render()

Optional arguments to render can be used to specify the resolution, camera ID and whether to render RGB or depth images.

: Physics.model and Physics.data

MuJoCo's mjModel and mjData structs, describing static and dynamic simulation parameters, can be accessed via the model and data properties of Physics. They contain NumPy arrays that have direct, writeable views onto MuJoCo's internal memory. Because the memory is owned by MuJoCo an attempt to overwrite an entire array will fail:

[⬇](data:text/plain;base64,IyBUaGlzIHdpbGwgZmFpbDoKcGh5c2ljcy5kYXRhLnFwb3MgPSBucC5yYW5kb20ucmFuZG4ocGh5c2ljcy5tb2RlbC5ucSkKIyBUaGlzIHdpbGwgc3VjY2VlZDoKcGh5c2ljcy5kYXRhLnFwb3NbOl0gPSBucC5yYW5kb20ucmFuZG4ocGh5c2ljcy5tb2RlbC5ucSk=){download=""}

\# This will fail:

physics.data.qpos = np.random.randn(physics.model.nq)

\# This will succeed:

physics.data.qpos = np.random.randn(physics.model.nq)

: Setting the state with reset_context()

When setting the MujoCo state, derived quantities like global positions or sensor measurements are not updated. In order to facilitate synchronisation of derived quantities we provide the Physics.reset_context() context:

[⬇](data:text/plain;base64,d2l0aCBwaHlzaWNzLnJlc2V0X2NvbnRleHQoKToKICAgIyBtal9yZXNldCgpIGlzIGNhbGxlZCB1cG9uIGVudGVyaW5nIHRoZSBjb250ZXh0LgogICBwaHlzaWNzLmRhdGEucXBvc1s6XSA9IC4uLiAgIyBTZXQgcG9zaXRpb24sCiAgIHBoeXNpY3MuZGF0YS5xdmVsWzpdID0gLi4uICAjIHZlbG9jaXR5CiAgIHBoeXNpY3MuZGF0YS5jdHJsWzpdID0gLi4uICAjIGFuZCBjb250cm9sLgojIG1qX2ZvcndhcmQoKSBpcyBjYWxsZWQgdXBvbiBleGl0aW5nIHRoZSBjb250ZXh0LiBOb3cgYWxsIGRlcml2ZWQKIyBxdWFudGl0aWVzIGFuZCBzZW5zb3IgbWVhc3VyZW1lbnRzIGFyZSB1cC10by1kYXRlLg==){download=""}

with physics.reset_context():

\# mj_reset() is called upon entering the context.

physics.data.qpos = \... \# Set position,

physics.data.qvel = \... \# velocity

physics.data.ctrl = \... \# and control.

\# mj_forward() is called upon exiting the context. Now all derived

\# quantities and sensor measurements are up-to-date.

: Running the simulation

The physics.step() method is used to advance the simulation. Note that this method does not directly call MuJoCo's mj_step() function. At the end of an mj_step the state is updated, but the intermediate quantities stored in mjData were computed with respect to the *previous* state. To keep these derived quantities as closely synchronised with the current simulation state as possible, we use the fact that MuJoCo partitions mj_step into two parts: mj_step1, which depends only on the state and mj_step2, which also depends on the control. Our physics.step first executes mj_step2 (assuming mj_step1 has already been called), and then calls mj_step1, beginning the next step^88^8In the case of Runge-Kutta integration, we simply conclude each RK4 step with an mj_step1.. The upshot is that quantities that depend only on position and velocity (e.g. camera pixels) are synchronised with the current state, while quantities that depend on force/acceleration (e.g. touch sensors) are with respect to the previous transition.

It is often more convenient and less error-prone to refer to elements in the simulation by name rather than by index. Physics.named.model and Physics.named.data provide array-like containers that provide convenient named views:

[⬇](data:text/plain;base64,cHJpbnQoIlRoZSBnZW9tX3hwb3MgYXJyYXk6IikKcHJpbnQocGh5c2ljcy5kYXRhLmdlb21feHBvcykKcHJpbnQoIklzIG11Y2ggZWFzaWVyIHRvIGluc3BlY3QgdXNpbmcgUGh5c2ljcy5uYW1lZCIpCnByaW50KHBoeXNpY3MubmFtZWQuZGF0YS5nZW9tX3hwb3Mp){download=""}

print(\"The geom_xpos array:\")

print(physics.data.geom_xpos)

print(\"Is much easier to inspect using Physics.named\")

print(physics.named.data.geom_xpos)

[⬇](data:text/plain;base64,VGhlIGRhdGEuZ2VvbV94cG9zIGFycmF5OgpbWyAwLiAgIDAuICAgMC4gXQogWyAwLiAgIDAuICAgMC4zXQogWyAwLjIgIDAuMiAgMC41XV0KSXMgbXVjaCBlYXNpZXIgdG8gaW5zcGVjdCB1c2luZyBQaHlzaWNzLm5hbWVkOgogICAgICAgICAgIHggICAgICAgICB5ICAgICAgICAgegowICBmbG9vciBbIDAgICAgICAgICAwICAgICAgICAgMCAgICAgICBdCjEgICAgYm94IFsgMCAgICAgICAgIDAgICAgICAgICAwLjMgICAgIF0KMiBzcGhlcmUgWyAwLjIgICAgICAgMC4yICAgICAgIDAuNSAgICAgXQ==){download=""}

The data.geom_xpos array:

Is much easier to inspect using Physics.named:

These containers can be indexed by name for both reading and writing, and support most forms of NumPy indexing:

[⬇](data:text/plain;base64,d2l0aCBwaHlzaWNzLnJlc2V0X2NvbnRleHQoKToKICBwaHlzaWNzLm5hbWVkLmRhdGEucXBvc1sidXBfZG93biJdID0gMC4xCnByaW50KHBoeXNpY3MubmFtZWQuZGF0YS5nZW9tX3hwb3NbImJveCIsIFsieCIsICJ6Il1dKQ==){download=""}

with physics.reset_context():

physics.named.data.qpos\[\"up_down\"\] = 0.1

print(physics.named.data.geom_xpos\[\"box\", \[\"x\", \"z\"\]\])

[⬇](data:text/plain;base64,WyAwLiAgIDAuNF0=){download=""}

Note that in the example above we use a joint name to index into the generalised position array qpos. Indexing into a multi-DoF ball or free joint would output the appropriate slice.

We also provide convenient access to MuJoCo's mj_id2name and mj_name2id:

[⬇](data:text/plain;base64,cGh5c2ljcy5tb2RlbC5pZDJuYW1lKDAsICJnZW9tIik=){download=""}

physics.model.id2name(0, \"geom\")

[⬇](data:text/plain;base64,J2Zsb29yJw==){download=""}

## Benchmarking

We provide baselines for two commonly employed deep reinforcement learning algorithms A3C and DDPG, as well as the recently introduced D4PG. We refer to the relevant papers for algorithm motivation and details and here provide only hyperparameter, network architecture, and training configuration information (see relevant sections below).

We study both the case of learning with state derived features as observations and learning from raw-pixel inputs for all the tasks in the Control Suite. It is of course possible to look at control via combined state features and pixel features, but we do not study this case here. We present results for both final performance and learning curves that demonstrate aspects of data-efficiency and stability of training.

Establishing baselines for reinforcement learning problems and algorithms is notoriously difficult. Though we describe results for well-functioning implementations of the algorithms we present, it may be possible to perform better on these tasks with the same algorithms. For a given algorithm we ran experiments with a similar network architecture, set of hyperparameters, and training configuration as described in the original papers. We ran a simple grid search for each algorithm to find a well performing setting for each (see details for grid searches below). We used the same hyperparameters across all of the tasks (i.e. so that nothing is tuned per-task). Thus, it should be possible to improve performance on a given task by tuning parameters with respect to performance for that specific task. For these reasons, the results are not presented as upper bounds for performance with these algorithms, but rather as a starting point for comparison. It is also worth noting that we have not made a concerted effort to maximise data efficiency, for example by making many mini-batch updates using the replay buffer per step in the environment, as in Popov et al..

The following pseudocode block demonstrates how to load a single task in the benchmark suite, run a single episode with a random agent, and compute the reward as we do for the results reported here. Note that we run each environment for 1000 time steps and sum the rewards provided by the environment after each call to step. Thus, the maximum possible score for any task is 1000. For many tasks, the practical maximum is significantly less than 1000 since it may take many steps until it's possible to drive the system into a state that gives a full reward of 1.0 each time step.

[⬇](data:text/plain;base64,ZnJvbSBkbV9jb250cm9sIGltcG9ydCBzdWl0ZQoKZW52ID0gc3VpdGUubG9hZChkb21haW5fbmFtZSwgdGFza19uYW1lKQoKc3BlYyA9IGVudi5hY3Rpb25fc3BlYygpCnRpbWVfc3RlcCA9IGVudi5yZXNldCgpCnRvdGFsX3Jld2FyZCA9IDAuMApmb3IgXyBpbiByYW5nZSgxMDAwKToKICBhY3Rpb24gPSBucC5yYW5kb20udW5pZm9ybShzcGVjLm1pbmltdW0sIHNwZWMubWF4aW11bSwgc3BlYy5zaGFwZSkKICB0aW1lX3N0ZXAgPSBlbnYuc3RlcChhY3Rpb24pCiAgdG90YWxfcmV3YXJkICs9IHRpbWVfc3RlcC5yZXdhcmQ=){download=""}

from dm_control import suite

env = suite.load(domain_name, task_name)

spec = env.action_spec()

time_step = env.reset()

action = np.random.uniform(spec.minimum, spec.maximum, spec.shape)

time_step = env.step(action)

total_reward += time_step.reward

In the state feature case we ran 15 different seeds for each task with A3C and DDPG; for results with D4PG, which was generally found to be more stable, we ran 5 seeds. In the raw-pixel case we also ran 5 different seeds for each task. The seed sets the network weight initialisation for the associated run. In all cases, initial network weights were sampled using standard TensorFlow initialisers. In the figures showing performance on individual tasks (Figures 4-7), the lines denote the median performance and the shaded regions denote the 5^th^ and 95^th^ percentiles across seeds. In the tables showing performance for individual tasks (Tables 1 & 2) we report means and standard errors across seeds.

As well as studying performance on individual tasks, we examined the performance of algorithms across all tasks by plotting a simple aggregate measure. Figure 3 shows the mean performance over environment steps and wallclock time for both state features and raw-pixels. These measures are of particular interest: they offer a view into the generality of a reinforcement learning algorithm. In this aggregate view, it is clear that D4PG is the best performing agent in all metrics, with the exception that DDPG is more data efficient before $1e7$ environment steps. It is worth noting that the data efficiency for D4PG can be improved over DDPG by simply reducing the number of actor threads for D4PG (experiments not shown here), since with 32 actors D4PG is somewhat wasteful of environment data (with the benefit of being more efficient in terms of wall-clock).

Figure 3: Mean return across all tasks in the Control Suite plotted versus data (first column) and wallclock time (second column). The first row shows performance for A3C, DDPG and D4PG on the tasks using low-dimensional features as input. The second row shows the performance for D4PG on the tasks using only raw-pixels as input.

While we have made a concerted effort to ensure reproducible benchmarks, it's worth noting that there remain uncontrolled aspects that introduce variance into the evaluations. For example, some tasks have a randomly placed target or initialisation of the model, and the sequence of these are not fixed across runs. Thus, each learning run will see a different sequence of episodes, which will lead to variance in performance. This might be fixed by introducing a fixed sequence of initialisation for episodes, but this is not in any case a practical solution for the common case of parallelised training, so our benchmarks simply reflect variability in episode initialisation sequence.

### Algorithm and Architecture Details

: Mnih et al. proposed a version of the Advantage Actor Critic that could be trained asynchronously (A3C). Here we report results for the A3C trained with 32 workers per task. The network consisted of 2 MLP layers shared between actor and critic with 256 units in the first hidden layer. The grid search explored: learning rates, $\eta \in$ \[1e-2, 1e-3, 1e-4, 1e-5, 3e-5, 4e-5, 5e-5\]; unroll length $t_{\max} \in {\lbrack 20,100,1000\rbrack}$; activation functions for computing ${{\log\sigma}{( \cdot )}} \in {\lbrack{{Softplus}{(x)}},{\exp{({\log{({0.01 + {2\text{sigmoid}{(x)}}})}})}}\rbrack}$; number of units in the second hidden layer $\in {\lbrack 128,256\rbrack}$; annealing of learning rate $\in {\lbrack{true},{false}\rbrack}$. The advantage baseline was computed using a linear layer after the second hidden layer. Actions were sampled from a multivariate Gaussian with diagonal covariance, parameterized by the output vectors $\mu$ and $\sigma^{2}$. The value of the logarithm of $\sigma$ was computed using the second sigmoid activation function given above (which was found to be more stable than the ${Softplus}{(x)}$ function used in the original A3C manuscript), while $\mu$ was computed from a hyperbolic tangent, both stemming from the second MLP layer. The RMSProp optimiser was used with a decay factor of $\alpha = 0.99$, a damping factor of $\epsilon = 0.1$ and a learning rate starting at ${5e} - 5$ and annealed to $0$ throughout training using a linear schedule, with no gradient clipping. An entropy regularisation cost weighted at $\beta = {{3e} - 3}$ was added to the policy loss.

: Lillicrap et al. presented a Deep Deterministic Policy Gradients (DDPG) agent that performed well on an early version of the Control Suite. Here we present performance for straightforward single actor/learner implementation of the DDPG algorithm. Both actor and critic networks were MLPs with ReLU nonlinearities. The actor network had two layers of $300\rightarrow 200$ units respectively, while the critic network had two layers of $400\rightarrow 300$ units. The action vector was passed through a linear layer and summed up with the activations of the second critic layer in order to compute Q values. The grid search explored: discount factors, $\lambda \in {\lbrack 0.95,0.99\rbrack}$; learning rates, $\eta \in {\lbrack{{1e} - 2},{{1e} - 3},{{1e} - 4},{{1e} - 5}\rbrack}$ fixed to be the same for both networks; damping and spread parameters for the Ornstein--Uhlenbeck process, $\theta \in {\lbrack 0,0.15,0.85,1\rbrack}$ and $\mu \in {\lbrack 0.1,0.2,0.3,0.4\rbrack}$ respectively; hard (swap at intervals of 100 steps) versus soft ($\tau = {{1e} - 3}$) target updates. For the results shown here the two networks were trained with independent Adam optimisers Kingma and Ba, both with a learning rate of $\eta = {{1e} - 4}$, with gradients clipped at $\lbrack{- 1},1\rbrack$ for the actor network. The agent used discounting of $\lambda = 0.99$. As in the paper, we used a target network with soft updates and an Ohrstein-Uhlenbeck process to add an exploration noise that is correlated in time, with similar parameters, except for a slightly bigger $\sigma$ ($\theta = 0.15$, $\sigma = 0.3$, $\tau = {{1e} - 3}$). The replay buffer size was also kept to $1e6$, and training was done with a minibatch size of $64$.

: The Distributional Distributed Deep Deterministic Policy Gradients algorithm extends regular DDPG with the following features: First, the critic value function is modelled as a categorical distribution, using 101 categories spaced evenly across $\lbrack{- 150},150\rbrack$. Second, acting and learning are decoupled and deployed on separate machines using the Ape-X architecture described in. We used 32 CPU-based actors and a single GPU-based learner for benchmarking. D4PG additionally applies $N$-step returns with $N = 5$, and non-uniform replay sampling ($\alpha_{\text{sample}} = 0.6$) and eviction ($\alpha_{\text{evict}} = 0.6$) strategies using a sample-based distributional KL loss (see and for details). D4PG hyperparameters were the same as those used for DDPG, with the exception that hard target network updates are applied every 100 steps, and exploration noise is sampled from a Gaussian distribution with fixed $\sigma$ varying from $1/32$ to $1$ across the actors. A mini-batch size of $256$ was used.

### Results: Learning from state features

Due to the different parallelization architectures, the evaluation protocol for each agent was slightly different: DDPG was evaluated for 10 episodes for every 100000 steps (with no exploration noise), and A3C was trained with 32 workers and concurrently evaluated with another worker that updated its parameters every 3 episodes, which produced intervals of on average 96000 steps per update. The plots in Figure 4 and Figure 5 show the median and the 5th and 95th percentile of the returns for the first $1e8$ steps. Each agent was run 15 times per task using different seeds (except for D4PG which was run 5 times), using only low-dimensional state feature information. D4PG tends to achieve better results in nearly all of the tasks. Notably, it manages to reliably solve the manipulator:bring_ball task, and achieves a good performance in acrobot tasks. We found that part of the reason the agent did not go above $600$ in the acrobot task is due to the time it takes for the pendulum to be swung up, so its performance is probably close to the upper bound.

### Results: Learning from pixels

The DeepMind Control Suite can be configured to produce observations containing any combination of state vectors and pixels generated from the provided cameras. We also benchmarked a variant of D4PG that learns directly from pixel-only input, using $84 \times 84$ RGB frames from the $0^{th}$ camera. To process pixel input, D4PG is augmented with a simple 2-layer ConvNet. Both kernels are size $3 \times 3$ with 32 channels and ELU activation, and the first layer has stride 2. The output is fed through a single fully-connected layer with 50 neurons, with layer normalisation Ba et al. and tanh() activations. We explored four variants of the algorithm. In the first, there were separate networks for the actor and Q-critic. In the other three, the actor and critic shared the convolutional layers, and the actor and critic each had a separate fully connected layer before their respective outputs. The best performance was obtained by weight-sharing the convolutional kernel weights between the actor and critic networks, and only allowing these weights to be updated by the critic optimiser (i.e. truncating the policy gradients after the actor MLP). D4Pixels internally frame-stacks 3 consecutive observations as the ConvNet input.

Results for 1 day of running time are shown in Figure 7; we plot the results for the three shared-weights variants of D4PG, with gradients into the ConvNet from the actor (dotted green), critic (dashed green), or both (solid green). For the sake of comparison, we plot D4PG performance for low-dimensional features (solid blue) from Figure 5. The variant that employed separate networks for actor and critic performed significantly worse than the best of these and is not shown. Learning from pixel-only input is successful on many of the tasks, but fails completely in some cases. It is worth noting that the camera view for some of the task domains are not well suited to a pixel-only solution for the task. Thus, some of the failure cases are likely due to the difficulty of positioning a camera that simultaneously captures both the navigation targets as well as the details of the agents body: e.g., in the case of swimmer:swimmer6 and swimmer15 as well as fish:swim.

## Conclusion and future work

The DeepMind Control Suite is a starting place for the design and performance comparison of reinforcement learning algorithms for physics-based control. It offers a wide range of tasks, from near-trivial to quite difficult. The uniform reward structure allows for robust suite-wide performance measures.

The results presented here for A3C, DDPG, and D4PG constitute baselines using, to the best of our knowledge, well performing implementations of these algorithms. At the same time, we emphasise that the learning curves are not based on exhaustive hyperparameter optimisation, and that for a given algorithm the same hyperparameters were used across all tasks in the Control Suite. Thus, we expect that it may be possible to obtain better performance or data efficiency, especially on a per-task basis.

We are excited to be sharing the Control Suite with the wider community and hope that it will be found useful. We look forward to the diverse research the Suite may enable, and to integrating community contributions in future releases.

### Future work

Several elements are missing from the current release of the Control Suite.

Some features, like the lack of rich tasks, are missing by design. The Suite, and particularly the benchmarking set of tasks, is meant to be a stable, simple starting point for learning control. Task categories like full manipulation and locomotion in complex terrains require reasoning about a distribution of tasks and models, not only initial states. These require more powerful tools which we hope to share in the future in a different branch.

There are several features that we hoped to include but did not make it into this release; we intend to add these in the future. They include: a quadrupedal locomotion task, an interactive visualiser with which to view and perturb the simulation, support for C callbacks and multi-threaded dynamics, a MuJoCo TensorFlow op wrapper and Windows™ support.

Figure 4: Comparison of A3C, DDPG, D4PG agents over environment steps.

Figure 5: Comparison of A3C, DDPG and D4PG agents over 1 day of training time.

Figure 6: D4PG agent variants using pixel-only features over environment steps.

Figure 7: D4PG agent variants using pixel-only features over 1 day of training time.

Table 1: Mean and Standard Error of 100 episodes after 108 training steps for each seed.

Table 2: Mean and standard error of 100 episodes after 24 hours of training for each seed.
