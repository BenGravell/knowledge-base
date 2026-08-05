<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

OpenAI Gym

Topics include OpenAI Gym, Reinforcement learning, Benchmarking, Simulation environments, Research infrastructure, Standardized interface, Open-source software.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces OpenAI Gym as a common interface and benchmark collection for reinforcement learning experiments. Its main contribution is infrastructural: standardizing environments, result sharing, and evaluation workflows so RL algorithms can be compared more consistently.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

OpenAI Gym is a toolkit for reinforcement learning research. It includes a growing collection of benchmark problems that expose a common interface, and a website where people can share their results and compare the performance of algorithms. This whitepaper discusses the components of OpenAI Gym and the design decisions that went into the software.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement learning (RL) is the branch of machine learning that is concerned with making sequences of decisions. RL has a rich mathematical theory and has found a variety of practical applications [bertsekas1995dynamic]. Recent advances that combine deep learning with reinforcement learning have led to a great deal of excitement in the field, as it has become evident that general algorithms such as policy gradients and Q-learning can achieve good performance on difficult problems, without problem-specific engineering [,Schulman15TRPO,mnih2016asynchronous].

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To build on recent progress in reinforcement learning, the research community needs good benchmarks on which to compare algorithms. A variety of benchmarks have been released, such as the Arcade Learning Environment (ALE) [Bellemare13ALE], which exposed a collection of Atari 2600 games as reinforcement learning problems, and recently the RLLab benchmark for continuous control [duan2016benchmarking], to which we refer the reader for a survey on other RL benchmarks, including [RLPy,RLGlue,PyBrain,RLLibCapital,dimitrakakis2014reinforcement]. OpenAI Gym aims to combine the best elements of these previous benchmark collections, in a software package that is maximally convenient and accessible. It includes a diverse collection of tasks (called environments) with a common interface, and this collection will grow over time. The environments are versioned in a way that will ensure that results remain meaningful and reproducible as the software is updated.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Alongside the software library, OpenAI Gym has a website (gym.openai.comgym.openai.com) where one can find scoreboards for all of the environments, showcasing results submitted by users. Users are encouraged to provide links to source code and detailed instructions on how to reproduce their results.

<!-- chunk {"id": "body-0007", "role": "body", "section": "reward, and boolean flag indicating if the episode is complete", "weight": 1.0} -->

ob2, rew1, done1, info1 = env.step(a1) ob100, rew99, done99, info2 = env.step(a99)

<!-- chunk {"id": "body-0008", "role": "body", "section": "Design Decisions", "weight": 1.0} -->

The design of OpenAI Gym is based on the authors' experience developing and comparing reinforcement learning algorithms, and our experience using previous benchmark collections. Below, we will summarize some of our design decisions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Design Decisions", "weight": 1.0} -->

Environments, not agents. Two core concepts are the agent and the environment. We have chosen to only provide an abstraction for the environment, not for the agent. This choice was to maximize convenience for users and allow them to implement different styles of agent interface. First, one could imagine an online learning style, where the agent takes (observation, reward, done) as an input at each timestep and performs learning updates incrementally. In an alternative batch update style, a agent is called with observation as input, and the reward information is collected separately by the RL algorithm, and later it is used to compute an update. By only specifying the agent interface, we allow users to write their agents with either of these styles.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Design Decisions", "weight": 1.0} -->

Emphasize sample complexity, not just final performance. The performance of an RL algorithm on an environment can be measured along two axes: first, the final performance; second, the amount of time it takes to learnthe sample complexity. To be more specific, final performance refers to the average reward per episode, after learning is complete. Learning time can be measured in multiple ways, one simple scheme is to count the number of episodes before a threshold level of average performance is exceeded. This threshold is chosen per-environment in an ad-hoc way, for example, as 90% of the maximum performance achievable by a very heavily trained agent.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Design Decisions", "weight": 1.0} -->

Both final performance and sample complexity are very interesting, however, arbitrary amounts of computation can be used to boost final performance, making it a comparison of computational resources rather than algorithm quality.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Design Decisions", "weight": 1.0} -->

Encourage peer review, not competition. The OpenAI Gym website allows users to compare the performance of their algorithms. One of its inspiration is which hosts a set of machine learning contests with leaderboards. However, the aim of the OpenAI Gym scoreboards is not to create a competition, but rather to stimulate the sharing of code and ideas, and to be a meaningful benchmark for assessing different methods.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Design Decisions", "weight": 1.0} -->

RL presents new challenges for benchmarking. In the supervised learning setting, performance is measured by prediction accuracy on a test set, where the correct outputs are hidden from contestants. In RL, it's less straightforward to measure generalization performance, except by running the users' code on a collection of unseen environments, which would be computationally expensive. Without a hidden test set, one must check that an algorithm did not overfiton the problems it was tested on (for example, through parameter tuning).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Design Decisions", "weight": 1.0} -->

We would like to encourage a peer review process for interpreting results submitted by users. Thus, OpenAI Gym asks users to create a Writeup describing their algorithm, parameters used, and linking to code. Writeups should allow other users to reproduce the results. With the source code available, it is possible to make a nuanced judgement about whether the algorithm overfitto the task at hand.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Design Decisions", "weight": 1.0} -->

Strict versioning for environments. If an environment changes, results before and after the change would be incomparable. To avoid this problem, we guarantee than any changes to an environment will be accompanied by an increase in version number. For example, the initial version of the CartPole task is named Cartpole-v0, and if its functionality changes, the name will be updated to Cartpole-v1.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Design Decisions", "weight": 1.0} -->

By default, environments are instrumented with a Monitor, which keeps track of every time step (one step of simulation) and reset(sampling a new initial state) are called. The Monitor's behavior is configurable, and it can record a video periodically. It also is sufficient to produce learning curves. The videos and learning curve data can be easily posted to the OpenAI Gym website.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Design Decisions", "weight": 1.0} -->

Images of some environments that are currently part of OpenAI Gym.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Environments", "weight": 1.0} -->

OpenAI Gym contains a collection of Environments (POMDPs), which will grow over time. See fig:envs for examples.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Environments", "weight": 1.0} -->

- Classic control and toy text: small-scale tasks from the RL literature. - Algorithmic: perform computations such as adding multi-digit numbers and reversing sequences. Most of these tasks require memory, and their difficulty can be chosen by varying the sequence length. - Atari: classic Atari games, with screen images or RAM as input, using the Arcade Learning Environment [Bellemare13ALE]. - Board games: currently, we have included the game of Go on 9x9 and 19x19 boards, where the Pachi engine [baudivs2011pachi] serves as an opponent. - 2D and 3D robots: control a robot in simulation. These tasks use the MuJoCo physics engine, which was designed for fast and accurate robot simulation [todorov2012mujoco]. A few of the tasks are adapted from RLLab [duan2016benchmarking].

<!-- chunk {"id": "body-0020", "role": "body", "section": "Environments", "weight": 1.0} -->

Since the initial release, more environments have been created, including ones based on the open source physics engine Box2D or the Doom game engine via VizDoom

<!-- chunk {"id": "body-0021", "role": "body", "section": "Future Directions", "weight": 1.0} -->

In the future, we hope to extend OpenAI Gym in several ways.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Future Directions", "weight": 1.0} -->

- Multi-agent setting. It will be interesting to eventually include tasks in which agents must collaborate or compete with other agents. - Curriculum and transfer learning. Right now, the tasks are meant to be solved from scratch. Later, it will be more interesting to consider sequences of tasks, so that the algorithm is trained on one task after the other. Here, we will create sequences of increasingly difficult tasks, which are meant to be solved in order. - Real-world operation. Eventually, we would like to integrate the Gym API with robotic hardware, validating reinforcement learning algorithms in the real world.
