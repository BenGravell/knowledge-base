<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Reinforcement Learning-Based Oscillation Dampening: Scaling up Single-Agent RL Algorithms to a 100 AV Highway Field Operational Test

Topics include Reinforcement learning, Autonomous vehicles, Traffic flow smoothing, Field operational test, Single-agent reinforcement learning, Control deployment, Highway traffic, Safety validation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Documents the RL controller design and deployment path for a large automated-vehicle field test aimed at damping stop-and-go traffic oscillations. The paper is especially useful as an engineering account of moving from simulation and reward shaping to hardware constraints, safety considerations, and fleet-scale highway deployment.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this article, we explore the technical details of the reinforcement learning (RL) algorithms that were deployed in the largest field test of automated vehicles designed to smooth traffic flow in history as of 2023, uncovering the challenges and breakthroughs that come with developing RL controllers for automated vehicles. We delve into the fundamental concepts behind RL algorithms and their application in the context of self-driving cars, discussing the developmental process from simulation to deployment in detail, from designing simulators to reward function shaping. We present the results in both simulation and deployment, discussing the flow-smoothing benefits of the RL controller. From understanding the basics of Markov decision processes to exploring advanced techniques such as deep RL, our article offers a comprehensive overview and deep dive of the theoretical foundations and practical implementations driving this rapidly evolving field. We also showcase real-world case studies and alternative research projects that highlight the impact of RL controllers in revolutionizing autonomous driving. From tackling complex urban environments to dealing with unpredictable traffic scenarios, these intelligent controllers are pushing the boundaries of what automated vehicles can achieve. Furthermore, we examine the safety considerations and hardware-focused technical details surrounding deployment of RL controllers into automated vehicles.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

As these algorithms learn and evolve through interactions with the environment, ensuring their behavior aligns with safety standards becomes crucial. We explore the methodologies and frameworks being developed to address these challenges, emphasizing the importance of building reliable control systems for automated vehicles.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

As the automotive industry continues to evolve, the quest for safer and more efficient self-driving cars has become a top priority. To achieve this, engineers and researchers are turning to state-of-the-art techniques like reinforcement learning to create intelligent control systems that can navigate complex environments with unprecedented precision and adaptability. Reinforcement learning (RL), a subfield of machine learning, offers a promising avenue for training automated vehicles to make optimal decisions and actions in real-time scenarios. Unlike traditional rule-based approaches, RL-based controllers learn through trial and error, progressively refining their behavior based on feedback from the environment. This ability to adapt and improve over time makes RL an invaluable tool for enhancing the performance and reliability of automated vehicles.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Together with the other articles presented in this special issue, this article constitutes an element of the technical work involved in bringing together objective of the CIRCLES project: the MegaVanderTest (MVT), the largest deployment of automated vehicles (AVs) designed to smooth traffic flow in history as of 2023. These AVs are partially automated and limited to longitudinal control. They do not communicate between each other, but communicate with a central server to get information about the downstream state of the highway. This article discusses the following: Background material, including a short overview of reinforcement learning, human driver models, and policy gradient algorithms.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Problem formulation of the two classes of RL controllers designed for this experiment: Acceleration-based control and Adaptive Cruise Control (ACC)-based control.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Description of the work moving from the software to hardware platform, deployment onto real roadways, and the MVT field test week.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Result analysis of all controllers in simulation and in deployment Figure 1: Example setup of the trajectory simulator for evaluation. One vehicle, which we name trajectory leader, replays a velocity trajectory from the I-24 Trajectory Dataset. Following it are a combination of IDM-controlled human vehicles and automated vehicles (AVs) all on a single lane. This evaluation setup contains 8 platoons, each consisting of one AV followed by 24 human vehicles. The human vehicles are used to assess the smoothing performances of the AV. During training, only one platoon is simulated.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

We adhere to the conventional reinforcement learning (RL) framework, which seeks to optimize the discounted cumulative rewards within a finite time frame for a Partially Observable Markov Decision Process (POMDP).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

This POMDP can be officially characterized by the tuple $\mathcal{P} = {(\mathcal{S},\mathcal{A},T,R,T_{0},\gamma,\Omega,\mathcal{O})}$, where $\mathcal{S}$ symbolizes the set of states; $\mathcal{A}$ stands for the possible actions; the function $T:{{\mathcal{S} \times \mathcal{A} \times \mathcal{S}}\rightarrow{\mathbb{R}}}$ represents the conditional likelihood of moving to a subsequent state $s'$ given the current state $s$ and the chosen action $a$; $R:{{\mathcal{S} \times \mathcal{A} \times \mathcal{S}}\rightarrow{\mathbb{R}}}$ is the reward function; $T_{0}:{S\rightarrow{\mathbb{R}}}$ is the probability distribution of initial states; and $\gamma \in

<!-- chunk {"id": "body-0012", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

{(0,1\rbrack}$ is the discount coefficient applied to the accumulation of rewards.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

The last two parameters, $\Omega$ and $\mathcal{O}$, are included due to the concealed nature of the state: $\Omega$ refers to the observations of the hidden state, and $\mathcal{O}:{{\Omega \times \mathcal{S}}\rightarrow{\mathbb{R}}}$ stands for the conditional observation probability distribution.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

Given a POMDP, one can then sample an initial state $s_{0} \sim {T_{0}{( \cdot )}}$ and initial observation of that state $o_{0} \sim \mathcal{O}{( \cdot \mid s_{0})}$. The agent, which we denote as a stochastic conditional distribution $\pi_{\theta}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ parametrized by $\theta$, samples an action $a_{0} \sim \pi_{\theta}{( \cdot \mid s_{0})}$ from the observation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

That action is then used to generate a next state $s_{1} \sim T{( \cdot \mid s_{0},a_{0})}$ and observation of the state $o_{1} \sim \mathcal{O}{( \cdot \mid s_{1})}$, as well as a reward $r_{0} = {R{(s_{0},a_{0},s_{1})}}$. Iterating this process until termination (which can occur after a fixed time horizon or a certain termination condition) yields a trajectory $\tau = {(s_{i},o_{i},a_{i},r_{i})}_{i \geq 0}$. Let us define the return of a trajectory as the discounted sum of rewards ${G{(\tau)}} = {\sum_{i \geq 0}{\gamma^{i}r_{i}}}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

The goal for the agent is to maximize the expected return over all trajectories, and to learn an optimal policy $\pi^{\ast} = {{\arg{\max_{\pi}{{\mathbb{E}}_{\tau \sim {(\pi,\mathcal{P})}}G}}}{(\tau)}}$. More aspects of RL are explored in sidebars ''By Kathy Jang and Nathan Lichtlé'' and ''by Kathy Jang and Nathan Lichtlé''.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Human Driver Models", "weight": 1.0} -->

In order to train RL controllers, we simulate mixed-autonomy traffic where RL-controlled AVs interact with human-driven vehicles. In order to model human car-following behavior, we use the Intelligent Driver Model (IDM) to govern a vehicle's longitudinal motion according to its leading vehicle. To ensure authenticity, IDM parameters are selected to mimic key non-equilibrium features of real-world traffic, particularly dynamic instabilities (phantom traffic jams) with realistic wave growth and propagating stop-and-go waves caused by human driving behavior or even ACC. To trigger dynamic instabilities that the model possesses for suitably congested densities, zero-mean Gaussian noise is added to the acceleration in each time step. Additional safety measures are included to maintain acceleration bounds and to avoid collisions---note that pure IDM is mathematically collision-free, but discretized time-stepping and heterogeneous vehicle composition yields potential collision opportunities.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Human Driver Models", "weight": 1.0} -->

The IDM prescribes the acceleration of vehicle $\alpha$ as a function of its space gap (bumper-to-bumper distance to its leader vehicle) $s_{\alpha}$; its speed $v_{\alpha}$; and relative speed with the leader, $\Delta v_{\alpha}$: where $s^{\ast}$ is the desired space gap and is given: where $s_{0}$, $v_{0}$, $T$, $\delta$, $a$, and $b$ are known parameters. Parameter values are in Table 2.

<!-- chunk {"id": "body-0019", "role": "body", "section": "MegaController / Speed Planner", "weight": 1.0} -->

The *MegaController* (see ) is the outermost framework that addresses the challenge of smoothing traffic flow despite a limited penetration rate of automated vehicles by introducing two key components: the algorithm and the speed planner. The *Speed Planner*, discussed in further detail in its own standalone article, is a control framework for dynamic speed advisories in a traffic environment in which both automated and human-driven vehicles coexist. The speed planner is a centralized unit hosted on a server which incorporates various algorithms to handle computationally intensive tasks. The algorithms deployed on individual vehicles serve as operators, following the instructions provided by the centralized planner. The primary function of the Speed Planner is to design target speed profiles with the objective of minimizing vehicle energy consumption and maximizing overall traffic flow efficiency. The implemented Speed Planner is dependent on INRIX, a data source which provides the realtime average speed of road segments globally, including the segments of the *Interstate 24* (I-24) that the RL algorithm is deployed. INRIX data are typically represented in 500-800m segments, with high variability in segment size; approximately three minutes of latency; and is aggregated over all lanes across 60 seconds.

<!-- chunk {"id": "body-0020", "role": "body", "section": "MegaController / Speed Planner", "weight": 1.0} -->

Thus, while representing imperfect data, INRIX data provides a solid foundation upon which to develop prediction modules.

<!-- chunk {"id": "body-0021", "role": "body", "section": "By Kathy Jang and Nathan Lichtlé", "weight": 1.0} -->

*Reinforcement learning* has emerged as a powerful paradigm for enabling autonomous systems to learn and optimize their behavior through interaction with their environment. RL offers a unique approach to control system design by incorporating an agent's decision-making process and its impact on the environment. This sidebar provides a concise overview of RL, highlighting its key components and applications in the context of autonomous system control.

<!-- chunk {"id": "body-0022", "role": "body", "section": "By Kathy Jang and Nathan Lichtlé", "weight": 1.0} -->

RL revolves around the concept of an agent learning from its experiences in an environment. The agent takes actions based on its current state and receives feedback in the form of rewards or penalties, which reflect the desirability or undesirability of the agent's actions. By iteratively exploring the environment and adapting its actions based on the received rewards, the agent learns to optimize its behavior over time.

<!-- chunk {"id": "body-0023", "role": "body", "section": "By Kathy Jang and Nathan Lichtlé", "weight": 1.0} -->

RL MDP depicting how an agent interacts with its environment via actions, observations, and rewards.

<!-- chunk {"id": "body-0024", "role": "body", "section": "By Kathy Jang and Nathan Lichtlé", "weight": 1.0} -->

At the core of RL lies the *Markov Decision Process* (MDP) framework, which mathematically formalizes the problem of sequential decision-making under uncertainty. MDPs provide a principled representation of the agent's interaction with the environment, as illustrated in Figure 3, encapsulating the states, actions, transition dynamics, and rewards that govern the learning process. Algorithms such as Q-learning \[S1\], SARSA \[S2\], and policy gradient methods \[S3\] leverage MDPs to guide the agent's learning and decision-making processes.

<!-- chunk {"id": "body-0025", "role": "body", "section": "By Kathy Jang and Nathan Lichtlé", "weight": 1.0} -->

The Bellman equation, a central element to understanding the structure of the RL problem, is given by the following: {sequation} v_π(s) = ∑\_a ∈A(s)π(a\|s)∑\_s' ∈S, r∈Rp(s',r\|s,a)(r + γv_π(s')) The Bellman equation is used to model the value function, which describes the estimated value of a particular state. It operates under a dynamic programming paradigm, meaning that the estimate of the value function is calculated recursively. In practice, RL algorithms leverage other techniques like bootstrapping, function approximation or temporal difference learning such that the value of a state can be estimated without having to calculate all the way to the terminal state.

<!-- chunk {"id": "body-0026", "role": "body", "section": "By Kathy Jang and Nathan Lichtlé", "weight": 1.0} -->

One of the distinctive features of RL is its ability to handle complex, high-dimensional state and action spaces. Through the utilization of function approximation techniques, such as neural networks, RL algorithms can effectively learn representations of states and policies, enabling the control of systems with large state spaces or continuous actions \[S4\]. Deep RL, which combines deep neural networks with RL, has garnered significant attention in recent years due to its ability to handle complex control tasks, such as autonomous driving and robotics \[S5\].

<!-- chunk {"id": "body-0027", "role": "body", "section": "By Kathy Jang and Nathan Lichtlé", "weight": 1.0} -->

RL has found diverse applications in the realm of autonomous systems, including automated vehicles, robotics, and game-playing agents. In the context of automated vehicles, RL controllers can learn to navigate complex traffic scenarios, adapt to changing road conditions, and optimize driving strategies based on safety and efficiency objectives \[S6\]. By leveraging RL, autonomous systems can acquire adaptive and intelligent control policies, making them more capable of handling real-world challenges.

<!-- chunk {"id": "body-0028", "role": "body", "section": "By Kathy Jang and Nathan Lichtlé", "weight": 1.0} -->

However, RL also presents certain challenges and considerations. The exploration-exploitation trade-off, sample efficiency, and generalization to new environments are areas that continue to be actively researched. Moreover, ensuring the safety, interpretability, and ethical behavior of RL-based controllers remain crucial concerns in their practical deployment.

<!-- chunk {"id": "body-0029", "role": "body", "section": "By Kathy Jang and Nathan Lichtlé", "weight": 1.0} -->

In conclusion, RL provides a powerful paradigm for developing autonomous system control, enabling agents to learn and optimize their behavior through interaction with the environment. By leveraging the principles of RL, researchers and engineers can advance the capabilities of autonomous systems, paving the way for the realization of intelligent, adaptive, and efficient autonomous systems across various domains.
