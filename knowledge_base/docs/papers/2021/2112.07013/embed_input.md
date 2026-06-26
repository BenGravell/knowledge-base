<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

PantheonRL: A MARL Library for Dynamic Training Interactions

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present PantheonRL, a multiagent reinforcement learning software package for dynamic training interactions such as round-robin, adaptive, and ad-hoc training. Our package is designed around flexible agent objects that can be easily configured to support different training interactions, and handles fully general multiagent environments with mixed rewards and n agents. Built on top of StableBaselines3, our package works directly with existing powerful deep RL algorithms. Finally, PantheonRL comes with an intuitive yet functional web user interface for configuring experiments and launching multiple asynchronous jobs. Our package can be found at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Multiagent reinforcement learning (MARL) is becoming increasingly important as more AI systems are being deployed. Many potential applications of MARL involve dynamic interactions between agents, such as agents adapting to each other, ad-hoc coordination, and more (Fig 1). However, experimenting with these dynamic interactions using modern deep RL frameworks can be a difficult process. Existing MARL libraries are largely designed around training a fix set of agents, making them unsuitable for experimenting with more dynamic and adaptive agent interactions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose $\mathsf{P}\mathsf{a}\mathsf{n}\mathsf{t}\mathsf{h}\mathsf{e}\mathsf{o}\mathsf{n}\mathsf{R}\mathsf{L}$, an easy-to-use and extensible MARL software package that focuses on dynamic interactions between agents.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The goals of our package are: to support adaptive MARL, with dynamic training interactions ranging from self-play, round-robin, adaptive (few-shot), and ad-hoc (zero-shot) training, to build on top of existing powerful deep RL libraries, in particular $\mathsf{S}\mathsf{t}\mathsf{a}\mathsf{b}\mathsf{l}\mathsf{e}\mathsf{B}\mathsf{a}\mathsf{s}\mathsf{e}\mathsf{l}\mathsf{i}\mathsf{n}\mathsf{e}\mathsf{s}\mathsf{3}$ ($\mathsf{S}\mathsf{B}\mathsf{3}$), to provide a web user interface for launching and monitoring experiments, with support for the different dynamic training interactions described above.

<!-- chunk {"id": "body-0006", "role": "body", "section": "PantheonRL Framework", "weight": 1.0} -->

One of our desiderata is to build upon powerful single agent reinforcement learning (SARL) libraries. Our main design choice is thus: how do we interface with SARL algorithms, which train a policy network with input/output designated by the state/action space of an OpenAI Gym environment? Directly running a SARL algorithm on top of a joint multiagent environment (with joint observations and joint actions) is possible, but this produces a monolithic joint policy network that is undesirable for our first desiderata -- to support adaptive MARL with dynamic training interactions.

<!-- chunk {"id": "body-0007", "role": "body", "section": "PantheonRL Framework", "weight": 1.0} -->

Instead, our design is to split the training of each of the $n$ agents as separate SARL instances, so that we produce $n$ cleanly distinct policy networks that can be composed or finetuned for downstream adaptive MARL tasks. We next describe how we designed the environments and agents in a way that supports an intuitive API.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Joint / Projected Environments", "weight": 1.0} -->

Existing multiagent environments are generally defined as a *joint environment*, with a Gym step function handling $n$ actions and observations. Each joint environment implicitly defines $n$ *projected environments* that are Hidden-Parameter MDPs. The $i$-th projected environment handles the $i$-th agent's actions and observations, and has hidden-parameters characterized by the policies of the other $n - 1$ agents.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Joint / Projected Environments", "weight": 1.0} -->

Given a joint environment, we require only specification of the state/action spaces of the $n$ projected environments. $\mathsf{P}\mathsf{a}\mathsf{n}\mathsf{t}\mathsf{h}\mathsf{e}\mathsf{o}\mathsf{n}\mathsf{R}\mathsf{L}$ then automatically links with SARL algorithms to produce individual agent policies for each agent.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Ego / Partner Agents", "weight": 1.0} -->

$\mathsf{P}\mathsf{a}\mathsf{n}\mathsf{t}\mathsf{h}\mathsf{e}\mathsf{o}\mathsf{n}\mathsf{R}\mathsf{L}$ differentiates between an ego agent and the other $n - 1$ partner agents. Each agent is equipped with its own replay buffer and learning algorithm. A critical design feature is that each agent's learning algorithm can be chosen from off-the-shelf $\mathsf{S}\mathsf{B}\mathsf{3}$ algorithms, such as PPO, without any modifications.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Ego / Partner Agents", "weight": 1.0} -->

We distinguish the ego agent role for two reasons. First, when doing round-robin training or adaptation, we often want to fix the ego agent and sample partners from a pool of possible partners. Second, to provide an intuitive API similar to that of $\mathsf{S}\mathsf{B}\mathsf{3}$, we use the ego agent as the entry-point to the training procedure of all agents. In other words, ${\mathsf{e}\mathsf{g}\mathsf{o}}.{{\mathsf{l}\mathsf{e}\mathsf{a}\mathsf{r}\mathsf{n}}{}}$ will step through the environment, which triggers the learning algorithm of all the partner agents. The triggers are implemented so that all agents reuse the same joint trajectories, to avoid naively collecting the joint trajectories $n$ times.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Ego / Partner Agents", "weight": 1.0} -->

We highlight again the importance of $\mathsf{P}\mathsf{a}\mathsf{n}\mathsf{t}\mathsf{h}\mathsf{e}\mathsf{o}\mathsf{n}$'s compatibility with $\mathsf{S}\mathsf{B}\mathsf{3}$ in giving our framework great flexibility. Each agent can specify its own learning algorithm imported directly from $\mathsf{S}\mathsf{B}\mathsf{3}$. Designing our API around the ego agent also gives us access to many of the single-agent logging, debugging, and monitoring utilities of $\mathsf{S}\mathsf{B}\mathsf{3}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Web User Interface", "weight": 1.0} -->

In addition to full-fledged command-line invocations, $\mathsf{P}\mathsf{a}\mathsf{n}\mathsf{t}\mathsf{h}\mathsf{e}\mathsf{o}\mathsf{n}\mathsf{R}\mathsf{L}$ provides an easy-to-use web interface for launching and monitoring experiments. The web interface is valuable for prototyping MARL experiments, especially the dynamic training interactions supported by our package. This minimizes $\mathsf{P}\mathsf{a}\mathsf{n}\mathsf{t}\mathsf{h}\mathsf{e}\mathsf{o}\mathsf{n}\mathsf{R}\mathsf{L}$'s initial user overhead, which is often non-trivial for other MARL packages. A demo of the user interface can be found at ` The website guides the user in selecting the experiment parameters in stages -- first configuring the environment, and then configuring each individual agent.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Web User Interface", "weight": 1.0} -->

The parameters are presented as dropdown menus, check boxes, buttons, and more, which help reduce a user's mental load during selection. The configurations also allow the user to save/load agent policies and trajectories for later experiments.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Web User Interface", "weight": 1.0} -->

Not only is the website visually intuitive, it is also highly functional. One of the main features of the website is its asynchronous design. Built on top of Flask, the website allows a user to launch multiple asynchronous training jobs in the background. After the training jobs have launched, the website can either pull lightweight logging information to display to the user, or spawn a full Tensorboard service in the background to give the user complete monitoring capabilities. Moreover, the website stores a user's session information in a database, and supports login/logout if the user wants to manage multiple sessions.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Dynamic Training Interactions", "weight": 1.0} -->

Here, we demonstrate the simplicity of our API when training dynamic MARL interactions. The examples are on a $2$-player environment, but they extend to $n$-player environments just as easily. First, we train an ego agent in a round-robin style by pitting it against two partner agents (Listing 1). Partner 1 is loaded from a previously trained PPO policy, but we wrap it as a StaticPolicyAgent so that its policy does not update anymore. Partner 2 will update its policy using A2C, and the ego agent will update its policy using PPO.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Dynamic Training Interactions", "weight": 1.0} -->

1env = gym.make(’OvercookedMultiEnv-v0’) 2partner_1 = PPO.load(partner_1_file) 3env.add_partner_agent(StaticPolicyAgent(partner_1.policy)) 4partner_2 = A2C(’MlpPolicy’, env) 5env.add_partner_agent(OnPolicyAgent(partner_2)) 6ego_a = PPO(’MlpPolicy’, env, verbose=1) 7ego_a.learn(total_timesteps=500000) Listing 1 Example round-robin python training script Next, we will evaluate partner adaptation by loading a previously trained ego agent, and pairing it with the partner 2 agent we just trained (Listing 2). Since we want the ego agent to adapt to the partner, we set partner 2 to not update its policy. Other training paradigms like ad-hoc pairing and standard MARL can be specified in a similar fashion.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Dynamic Training Interactions", "weight": 1.0} -->

1env = gym.make(’OvercookedMultiEnv-v0’) 2env.add_partner_agent(StaticPolicyAgent(partner_2.policy)) 3ego_b = PPO.load(ego_b_file, env=env) 4ego_b.learn(total_timesteps=500000) Listing 2 Example adaptation script $\mathsf{P}\mathsf{a}\mathsf{n}\mathsf{t}\mathsf{h}\mathsf{e}\mathsf{o}\mathsf{n}\mathsf{R}\mathsf{L}$ provides a concise API while allowing for great flexibility in customizing training interactions, including the pool of partner agents, the toggling of partner updates, and the training algorithm for each individual agent.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Discussion", "weight": 1.5} -->

With focus on adaptive MARL and dynamic training interactions, $\mathsf{P}\mathsf{a}\mathsf{n}\mathsf{t}\mathsf{h}\mathsf{e}\mathsf{o}\mathsf{n}\mathsf{R}\mathsf{L}$ is a valuable addition to the MARL software ecosystem. The modularity of the agent policies combined with the inheritance of $\mathsf{S}\mathsf{t}\mathsf{a}\mathsf{b}\mathsf{l}\mathsf{e}\mathsf{B}\mathsf{a}\mathsf{s}\mathsf{e}\mathsf{l}\mathsf{i}\mathsf{n}\mathsf{e}\mathsf{s}\mathsf{3}$ capabilities together give users a flexible and powerful library for experimenting with complex multiagent interactions.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Discussion", "weight": 1.5} -->

To top it off, our intuitive yet functional web user interface, equipped with clean visuals and asynchronous job launches, makes $\mathsf{P}\mathsf{a}\mathsf{n}\mathsf{t}\mathsf{h}\mathsf{e}\mathsf{o}\mathsf{n}\mathsf{R}\mathsf{L}$ a suitable library for a wide range of users.
