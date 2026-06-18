<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Socially Aware Motion Planning with Deep Reinforcement Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

For robotic vehicles to navigate safely and efficiently in pedestrian-rich environments, it is important to model subtle human behaviors and navigation rules (e.g., passing on the right). However, while instinctive to humans, socially compliant navigation is still difficult to quantify due to the stochasticity in people's behaviors. Existing works are mostly focused on using feature-matching techniques to describe and imitate human paths, but often do not generalize well since the feature values can vary from person to person, and even run to run. This work notes that while it is challenging to directly specify the details of what to do (precise mechanisms of human navigation), it is straightforward to specify what not to do (violations of social norms). Specifically, using deep reinforcement learning, this work develops a time-efficient navigation policy that respects common social norms. The proposed method is shown to enable fully autonomous navigation of a robotic vehicle moving at human walking speed in an environment with many pedestrians.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent advances in sensing and computing technologies have spurred greater interest in various applications of autonomous ground vehicles. In particular, researchers have explored using robots to provide personal mobility services and luggage carrying support in complex, pedestrian-rich environments (e.g., airports and shopping malls). These tasks often require the robots to be capable of navigating efficiently and safely in close proximity of people, which is challenging because pedestrians tend to follow subtle social norms that are difficult to quantify, and pedestrians' intents (i.e., goals) are usually not known.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A common approach treats pedestrians as dynamic obstacles with simple kinematics, and employs specific reactive rules for avoiding collision. Since these methods do not capture human behaviors, they sometimes generate unsafe/unnatural movements, particularly when the robot operates near human walking speed. To address this issue, more sophisticated motion models have been proposed, which would reason about the nearby pedestrians' hidden intents to generate a set of predicted paths. Subsequently, classical path planning algorithms would be employed to generate a collision-free path for the robot. Yet, separating the navigation problem into disjoint prediction and planning steps can lead to the *freezing robot problem*, in which the robot fails to find any feasible action because the predicted paths could mark a large portion of the space untraversable. A key to resolving this problem is to account for cooperation, that is, to model/anticipate the impact of the robot's motion on the nearby pedestrians.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Existing work on cooperative, socially compliant navigation can be broadly classified into two categories, namely model-based and learning-based. Model-based approaches are typically extensions of multiagent collision avoidance algorithms, with additional parameters introduced to account for social interactions. For instance, to distinguish between human--human and human--robot interactions, the extended social forces model augments the potential field algorithm with additional terms that specify the repulsive forces (e.g., strength and range) governing each type of interaction. Model-based methods are designed to be computationally efficient as they often correspond to intuitive geometric relations; yet, it is unclear whether humans do follow such precise geometric rules. In particular, the force parameters often need to be tuned individually, and can vary significantly for different pedestrians. Also, it has been observed that model-based methods can lead to oscillatory paths.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In comparison, learning-based approaches aim to develop a policy that emulates human behaviors by matching feature statistics, such as the minimum separation distance to pedestrians. In particular, Inverse Reinforcement Learning (IRL) has been applied to learn a cost function from human demonstration (teleoperation), and a probability distribution over the set of joint trajectories with nearby pedestrians. Compared with model-based approaches, learning-based methods have been shown to produce paths that more closely resemble human behaviors, but often at a much higher computational cost. This is because computing/matching trajectory features often requires anticipating the joint paths of all nearby pedestrians, and might depend on some unobservable information (e.g., pedestrians' goals). More importantly, since human behaviors are inherently stochastic, the feature statistics calculated on pedestrians' paths can vary significantly from person to person, and even run to run for the same scenario. This raises concerns over whether such feature-matching methods are generalizable to different environments.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In short, existing works are mostly focused on modeling and replicating the detailed mechanisms of social compliance, which remains difficult to quantify due to the stochasticity in people's behaviors. In comparison, humans can intuitively evaluate whether a behavior is acceptable. In particular, human navigation (or teleoperation) is time-efficient and generally respects a set of simple social norms (e.g., "passing on the right"). Building on a recent paper, we characterize these properties in a reinforcement learning framework, and show that human-like navigation conventions emerge from solving a cooperative collision avoidance problem.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main contributions of this work are (i) introducing socially aware collision avoidance with deep reinforcement learning (SA-CADRL) for explaining/inducing socially aware behaviors in a RL framework, (ii) generalizing to multiagent ($n > 2$) scenarios through developing a symmetrical neural network structure, and (iii) demonstrating on robotic hardware autonomous navigation at human walking speed in a pedestrian-rich environment.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-A Collision Avoidance with Deep Reinforcement Learning", "weight": 1.0} -->

A multiagent collision avoidance problem can be formulated as a sequential decision making problem in a reinforcement learning framework. Let $\mathbf{s}_{t},\mathbf{u}_{t}$ denote an agent's state and action at time $t$, and let $\overset{\sim}{\mathbf{s}_{t}}$ denote the state of a nearby agent. To capture the uncertainty in nearby agents' intents, the state vector is partitioned into observable and unobservable parts, that is $\mathbf{s}_{t} = {\lbrack\mathbf{s}_{t}^{o},\mathbf{s}_{t}^{h}\rbrack}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Collision Avoidance with Deep Reinforcement Learning", "weight": 1.0} -->

Let the observable states be the agent's position, velocity, and radius (size), $\mathbf{s}^{o} = {\lbrack p_{x},p_{y},v_{x},v_{y},r\rbrack} \in {\mathbb{R}}^{5}$; let the unobservable states be the agent's intended goal position, preferred speed, and orientation, $\mathbf{s}^{h} = {\lbrack p_{gx},p_{gy},v_{pref},\psi\rbrack} \in {\mathbb{R}}^{4}$; and let the action be the agent's velocity, $\mathbf{u}_{t} = \mathbf{v}_{t}$. It will be explained in Section IV that the observable states can be readily obtained from sensor measurements.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Collision Avoidance with Deep Reinforcement Learning", "weight": 1.0} -->

The objective is to develop a policy, $\pi:{\left( \mathbf{s}_{t},{\overset{\sim}{\mathbf{s}_{t}}}^{o} \right)\mapsto\mathbf{u}_{t}}$, that minimizes the expected time to goal ${\mathbb{E}}{\lbrack t_{g}\rbrack}$ while avoiding collision with nearby agents,

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Collision Avoidance with Deep Reinforcement Learning", "weight": 1.0} -->

where Equation 2 is the collision avoidance constraint, Equation 3 is the goal constraint, Equation 4 is the agents' kinematics, and the expectation in Equation 1 is with respect to the other agent's unobservable states (intents) and policy.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Collision Avoidance with Deep Reinforcement Learning", "weight": 1.0} -->

This problem can be formulated in a reinforcement learning (RL) framework by considering an agent's joint configuration with its neighbor, $\mathbf{s}^{jn} = \left\lbrack \mathbf{s},{\overset{\sim}{\mathbf{s}}}^{o} \right\rbrack$. In particular, a reward function, $R_{col}{(\mathbf{s}^{jn},\mathbf{u})}$, can be specified to reward the agent for reaching its goal and penalize the agent for colliding with others. The unknown state-transition model, $P{(\mathbf{s}_{t + 1}^{jn},\left. \mathbf{s}_{t}^{jn} \middle| \mathbf{u}_{t} \right.)}$, takes into account the uncertainty in the other agent's motion due to its hidden intents (${\overset{\sim}{\mathbf{s}}}^{h}$).

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Collision Avoidance with Deep Reinforcement Learning", "weight": 1.0} -->

Solving the RL problem amounts to finding the optimal value function that encodes an estimate of the expected time to goal,

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Collision Avoidance with Deep Reinforcement Learning", "weight": 1.0} -->

where $\gamma \in {\lbrack 0,1)}$ is a discount factor. The optimal policy can be retrieved from the value function, that is

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Collision Avoidance with Deep Reinforcement Learning", "weight": 1.0} -->

A major challenge in finding the optimal value function is that the joint state $\mathbf{s}^{jn}$ is a continuous, high-dimensional vector, making it impractical to discretize and enumerate the state space. Recent advances in reinforcement learning address this issue by using deep neural networks to represent value functions in high-dimensional spaces, and have demonstrated human-level performance on various complex tasks. While several recent works have applied deep RL to motion planning, they are mainly focused on single agent navigation in unknown static environments, and with an emphasis on computing control inputs directly from raw sensor data (e.g., camera images). In contrast, this work extends the collision avoidance with deep reinforcement learning framework (CADRL) to characterize and induce socially aware behaviors in multiagent systems.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Characterization of Social Norms", "weight": 1.0} -->

It has been widely observed that humans tend to follow simple navigation norms to avoid colliding with each other, such as passing on the right and overtaking on the left. Albeit intuitive, it remains difficult to quantify the precise mechanisms of social norms, such as when to turn and how much to turn when passing another pedestrian; and the problem exacerbates as the number of nearby pedestrians increases. This is largely due to the stochasticity in people's motion (e.g., speed, smoothness), which can vary significantly among different individuals.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Characterization of Social Norms", "weight": 1.0} -->

(d) with diff. radii and speeds

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Characterization of Social Norms", "weight": 1.0} -->

Rather than trying to quantify human behaviors directly, this work notes that the complex normative motion patterns can be a consequence of simple local interactions. For instance, an intuitive pairwise collision avoidance rule can cause simulated agents moving in the same direction to form lanes in long corridors. Thus, we conjecture that rather than a set of precisely defined procedural rules, social norms are the emergent behaviors from a time-efficient, reciprocal collision avoidance mechanism. Reciprocity implicitly encodes a model of the other agents' behavior, which is the key for enabling cooperation without explicit communication. Also, note that reciprocity does not require a unique set of navigation rules, since both the left-handed and the right-handed rules can resolve path conflicts as shown in Fig. 2. Similarly, human navigation conventions are not unique, as the strength (e.g., separation distance) and passing direction vary in different countries.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Characterization of Social Norms", "weight": 1.0} -->

Existing works have reported that human navigation (or teleoperation of a robot) tends to be cooperative and time-efficient. This work notes that these two properties are encoded in the CADRL formulation through using the min-time reward function and the reciprocity assumption ($\overset{\sim}{\pi} = \pi$). Furthermore, it was interesting to observe that while no behavioral rules (e.g., function forms) were imposed in the problem formulation, CADRL policy exhibits certain navigation conventions, as illustrated in Fig. 3. In particular, Fig. 3(a) illustrates two CADRL agents passing on the right of each other, showing signs of conforming to mutually agreed rules. More importantly, this preference in passing direction is robust to small deviations in the initial condition, as shown in Fig. 3(b). As the offset increases, the CADRL agents eventually change passing direction in favor of shorter, smoother paths (Fig. 3(c)). Recall no communication took place and each agent's intent (e.g., goal) is not known to the other.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Characterization of Social Norms", "weight": 1.0} -->

However, the cooperative behaviors emerging from a CADRL solution are not consistent with human interpretation. For instance, two CADRL agents with different sizes and preferred speeds show a preference to pass on the left of each other (Fig. 3(d)). This is because an agent's state $\mathbf{s}$ is defined to be the concatenation of its position, velocity, size and goal, so it is unlikely that an emerging tie breaking navigation convention would solely depend on the relative position (as human social norms). Moreover, the cooperative behaviors of CADRL cannot be controlled -- they are largely dependent on the initialization of the value network and set of randomly generated training test cases. The next section will address this issue and present a method to induce behaviors that respect human social norms.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Approach", "weight": 1.0} -->

The following presents the socially aware multiagent collision avoidance with deep reinforcement learning algorithm (SA-CADRL). We first describe a strategy for shaping normative behaviors for a two-agent system in the RL framework, and then generalize the method to multiagent scenarios.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Inducing Social Norms", "weight": 1.0} -->

Recall the RL training process seeks to find the optimal value function Equation 5, which maps from an agent's joint state with its neighbor, $\mathbf{s}^{jn} = \left\lbrack \mathbf{s},{\overset{\sim}{\mathbf{s}}}^{o} \right\rbrack$, to a scalar value that encodes the expected time to goal. To reduce redundancy (up to a rotation and translation), this work uses a local coordinate frame with the x-axis pointing towards an agent's goal, as shown in Fig. 4. Specifically, each agent's state is parametrized as

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Inducing Social Norms", "weight": 1.0} -->

This work notes that social norms are one of the many ways to resolve a symmetrical collision avoidance scenario, as illustrated in Fig. 2. To induce a particular norm, a small bias can be introduced in the RL training process in favor of one set of behaviors over others. For instance, to encourage passing on the right, states (configurations) with another agent approaching from the undesirable side can be penalized (green region in Figure 4). The advantage of this approach is that violations of a particular social norm are usually easy to specify; and this specification need *not* be precise. This is because the addition of a penalty breaks the symmetry in the collision avoidance problem, thereby favoring behaviors respecting the desired social norm. This work uses the following specification of a reward function $R_{norm}$ for inducing the right-handed rules (Fig. 4),

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Inducing Social Norms", "weight": 1.0} -->

The parameters defining the penalty set $\mathcal{S}_{norm}$ affect the rate of convergence. With Equation 10-Equation 12, the SA-CADRL policy converged within 700 episodes (exhibiting the desired behaviors such as passing on the right on all validation test cases). With a 30% smaller penalty set (i.e., shrinking the shaded regions in Fig. 4), convergence occurred after 1250 episodes. Larger penalty sets, however, could lead to instability or divergence. Also, as long as training converges, the penalty sets' size does not have a major effect on the learned policy. This is expected because the desired behaviors are not in the penalty set. Similarly, Equation 9-Equation 12 can be modified to induce left-handed rules. We trained two SA-CADRL policies to learn left-handed and right-handed norms starting from the same initialization, the results of which are shown in Fig. 6. The learned policies exhibited similar qualitative behaviors as shown in Fig. 2. Also note that training is performed on randomly generated test cases, and not on the validation test cases.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Training a Multiagent Value Network", "weight": 1.0} -->

The CADRL work trained a two-agent network with three fully connected hidden layers, and used a minimax scheme for scaling up to multiagent ($n > 2$) scenarios. Since training was solely performed on a two-agent system, it was difficult to encode/induce higher order behaviors, such as accounting for the relations between nearby agents. This work addresses this problem by developing a method that allows for training on multiagent scenarios directly.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Training a Multiagent Value Network", "weight": 1.0} -->

To capture the multiagent system's symmetrical structure, a neural network with weight-sharing and max-pooling layers is employed, as shown in Fig. 5. For a four-agent network shown in Fig. 5(b), the three nearby agents' observed states can be swapped (blue input blocks) without affecting the output value. This condition is enforced through weight-sharing, as shown in Fig. 5(a). Two of such symmetrical layers are used, followed by a max-pooling layer for aggregating features and two fully-connected layers for computing a scalar value. This work uses the rectified linear unit (ReLU) as the activation function in the hidden layers.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Training a Multiagent Value Network", "weight": 1.0} -->

The input to the n-agent network is a generalization of Equation 7-Equation 8, that is, $\mathbf{s}^{jn} = {\lbrack\mathbf{s},{\overset{\sim}{\mathbf{s}}}^{o,1},{\ldots{\overset{\sim}{\mathbf{s}}}^{o,{n - 1}}}\rbrack}$, where the superscripts enumerate the nearby agents. The norm-inducing reward function is defined similarly as Equation 9, where a penalty is given if an agent's joint configuration with the *closest* nearby agent belongs to the penalty set $\mathcal{S}_{norm}$. The overall reward function is the sum of the original CADRL reward and the norm-inducing reward, that is, ${R{( \cdot )}} = {{R_{col}{( \cdot )}} + {R_{norm}{( \cdot )}}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B Training a Multiagent Value Network", "weight": 1.0} -->

1 initialize and duplicate a value net with n agents V (⋅;θ,n), V′ ← V
2 initialize experience sets E ← ⌀, Eb ← ⌀
8 with prob ϵf, mirror every traj s0: tfi in the x-axis
9 for every agent i do
16 for every C episodes do
Algorithm 1 Deep V-learning for SA-CADRL

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B Training a Multiagent Value Network", "weight": 1.0} -->

The procedure for training a multiagent SA-CADRL policy is outlined in Algorithm 1, which follows similarly as. A value network is first initialized by training on an n-agent trajectory dataset through neural network regression (line 1). Using this value network Equation 6 and following an $\epsilon$-greedy policy, a set of trajectories can be generated on random test cases (line 5-7). The trajectories are then turned into state-value pairs and assimilated into the experience sets $E,E_{b}$ (line 10-11). A subset of state-value pairs is sampled from the experience sets, and subsequently used to update the value network through back-propagation (line 12-13). The process repeats for a pre-specified number of episodes (line 3-4).

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B Training a Multiagent Value Network", "weight": 1.0} -->

Compared with CADRL, two important modifications are introduced in the training process. First, two experience sets, $E,E_{b}$, are used to distinguish between trajectories that reached the goals and those that ended in a collision (line 2, 11). This is because a vast majority ($\geq {90\%}$) of the random generated test cases were fairly simple, requiring an agent to travel mostly straight towards its goal. The bad experience set $E_{b}$ improves the rate of learning by focusing on the scenarios that fared poorly for the current policy. Second, during the training process, trajectories generated by SA-CADRL are reflected in the x-axis with probability $\epsilon_{f}$ (line 8). By inspection of Fig. 2, this operation flips the paths' topology (left-handedness vs right-handedness). Since a trajectory can be a few hundred steps long according to Equation 6, it could take a long time for an $\epsilon$-greedy policy to explore the state space and find an alternative topology.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B Training a Multiagent Value Network", "weight": 1.0} -->

In particular, empirical results show that, without this procedure, policies can still exhibit the wrong passing side after 2000 training episodes. This procedure exploits symmetry in the problem to explore different topologies more efficiently.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B Training a Multiagent Value Network", "weight": 1.0} -->

Furthermore, an $n$-agent network can be used to generate trajectories for scenarios with fewer agents (line 5). In particular, when there are $p \leq n$ agents, the inputs in Fig. 5(b) corresponding to the non-existent agents^11^1Consider an agent with two nearby agents using a four-agent network. can be filled by adding virtual agents -- replicating the states of the closest nearby agent and set the binary bit ${\overset{\sim}{b}}_{on}$ to zero Equation 8. The use of this parametrization avoids the need for training many different networks. A left-handed and a right-handed four-agent SA-CADRL policies are trained using the network structure shown in Fig. 5. Sample trajectories generated by these policies are shown in Fig. 7, which demonstrate the preferred behaviors of each respective set of social norms.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Computational Details", "weight": 1.0} -->

The size and connections in the multiagent network shown in Fig. 5 are tuned to obtain good performance (ensure convergence and produce time-efficient paths) while achieving real-time performance. In particular, on a computer with an i7-5820K CPU, a Python implementation of a four-agent SA-CADRL policy takes on average 8.7ms for each query of the value network (finding an action). Furthermore, offline training (Algorithm 1) took approximately nine hours to complete 3,000 episodes. In comparison, a two-agent network took approximately two hours for 1,000 training episodes. The four-agent system took much longer to train because its state space is much larger (higher dimensional) than that of the two-agent system. The training process was repeated multiple times and all runs converged to a similar policy -- exhibiting the respective desired social norms on all test cases in an evaluation set.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Computational Details", "weight": 1.0} -->

Furthermore, this work generated random test cases with sizes and velocities similar to that of normal pedestrians, such that $r \in {\lbrack 0.2,\, 0.5\rbrack}$m, and $v_{pref} \in {\lbrack 0.3,\, 1.8\rbrack}$m/s. Also, a desired minimum separation of 0.2m is specified through the collision reward $R_{col}$, which penalizes an agent for getting too close to its neighbors.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B Simulation Results", "weight": 1.0} -->

Three copies of four-agent SA-CADRL policies were trained, one without the norm inducing reward $R_{norm}$, one with the left-handed $R_{norm}$, and the other with the right-handed $R_{norm}$. On perfectly symmetrical test cases, such as those shown in Figs. 3 and 6, the left and right-handed SA-CADRL policies always select the correct passing side according to the respective norm. To demonstrate that SA-CADRL can balance between finding time-efficient paths and respecting social norms, these policies are further evaluated on randomly generated test cases.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B Simulation Results", "weight": 1.0} -->

In particular, we compute the average extra time to reach the goals^22^2${\overline{t}}_{e} = {\frac{1}{n}{\sum_{i = 1}^{n}{\lbrack{t_{g}^{i} - {{\|{\mathbf{p}_{0}^{i} - \mathbf{p}_{g}^{i}}\|}_{2}/v_{pref}^{i}}}\rbrack}}}$, where $t_{g}^{i}$ is the $i$th agent's time to reach its goal, and the second term is a lower bound of $t_{g}^{i}$ (straight toward goal at the preferred speed)., the minimum separation distance, and the relative preference between left-handedness and right-handedness. Norm preference is calculated by counting the proportion of trajectories that violate the left-handed or the right-handed version of Equation 10-Equation 12 for more than 0.5 second.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B Simulation Results", "weight": 1.0} -->

To ensure the test set is left-right balanced, each random test case is duplicated and reflected in the x-axis. Evidently, the optimal reciprocal collision avoidance (ORCA) algorithm -- a reactive, rule-based method that computes a velocity vector based on an agent's joint geometry with its neighbors -- attains nearly 50-50 left/right-handedness on these test sets (first row of Table I).

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Simulation Results", "weight": 1.0} -->

The same four-agent SA-CADRL policies are used to generate trajectories for both the two-agent and the four-agent test sets. On the two-agent test set, all RL-based methods produced more time-efficient paths than ORCA^33^3ORCA specifies a reactive, geometric rule for computing a collision-free velocity vector, but it does not anticipate the evolution of an agent's state with respect to other agents nearby. Thus, ORCA can generate shortsighted actions and oscillatory paths (see for a detailed explanation).. CADRL exhibited a slight preference to the right (40-60 split). The four-agent SA-CADRL (none) policy, in comparison, exhibited a stronger preference than ORCA and CADRL in each of the passing, crossing, and overtaking scenarios (third row in Table I). This observation suggests that (i) certain navigation conventions could emerge as a means of resolving symmetrical collision avoidance scenarios, and (ii) the conventions don't always correspond to human social norms.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B Simulation Results", "weight": 1.0} -->

For instance, SA-CADRL (none) prefers passing on the right but also overtaking on the right, which is a mix between right-handed and left-handed rules. In contrast, the SA-CADRL policies trained with $R_{norm}$ exhibited a strong preference (85-15 split) of the respective social norm. Recall that this ratio is not 1 because there is a tradeoff between time-optimality and social compliance, as illustrated in Fig. 3. This tradeoff can be controlled by tuning $q_{n}$ in Equation 9. Evidently, SA-CADRL (lh/rh) achieves better social compliance at a cost of an approximately 20% larger ${\overline{t}}_{e}$, because satisfying the norms often requires traveling a longer path.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B Simulation Results", "weight": 1.0} -->

Similarly, the bottom rows of Table I show that in the four-agent test set, all RL-based methods outperformed ORCA, and SA-CADRL (lh/rh) exhibited behaviors that respect the social norms. CADRL produced paths that are closer to time-optimal than the other algorithms, but sometimes came very close (within 0.1m) to other agents. This close proximity occurred because CADRL was trained on a two-agent system, so its action choice is dominated by the single closest neighbor; possibly leading CADRL to select an action that avoids the closest neighbor but drives towards a third agent. In contrast, all SA-CADRL policies were trained on four-agent systems and they all maintained a larger average separation distance.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-B Simulation Results", "weight": 1.0} -->

Extra time to goal ${\overline{t}}_{e}$(s)
Min separation dist. (m)
Norm preference (%) [left-handed / right-handed]

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-C Hardware Experiment", "weight": 1.0} -->

The SA-CADRL policy is implemented on a robotic vehicle for autonomous navigation in an indoor environment with many pedestrians, as shown in Fig. 1. The differential-drive vehicle is outfitted with a Lidar for localization, three Intel Realsenses for free space detection, and four webcams for pedestrian detection. Pedestrian detection and tracking is achieved by combining Lidar's pointcloud data with camera images. The speed, velocity, and size (radius) of a pedestrian are estimated by clustering the pointcloud data. The estimated radius includes a buffer (comfort) zone as reported. Obstacles within a 10m $\times$ 10m square (perception range) centered at vehicle are detected and used to populate an occupancy map, shown as the white square in Fig. 8(a). Interested readers are referred to for more details on the perception system and hardware construction of the robot.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C Hardware Experiment", "weight": 1.0} -->

Motion planning uses the diffusion map algorithm for finding global paths and SA-CADRL for local collision avoidance. In particular, the diffusion map algorithm considers *static* obstacles in the environment to find a subgoal within the vehicle's planning horizon (5m), which is shown at the end of the green line in Fig. 8(a). Also, a set of feasible directions (heading and range) is computed, which corresponds to the free space in the occupancy map (white square). The feasible directions are visualized as the thin blue lines emanating from the vehicle. SA-CADRL takes in the set of detected pedestrians shown as the colored disks, and chooses an action (velocity vector) from the feasible directions to move the vehicle toward the subgoal. SA-CADRL's decision is shown as the blue arrow in Fig. 8(a), which does not necessarily line up with the subgoal. Note that pedestrians can be detected beyond the 5m static planning horizon, thus allowing socially aware interaction at a longer range. This whole sense-plan-execute cycle is fast enough to operate in real-time at 10Hz on a Gigabyte Brix computer onboard the vehicle.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-C Hardware Experiment", "weight": 1.0} -->

Using this motion planning strategy, the vehicle was able to navigate fully autonomously in a dynamic indoor environment. In particular, the vehicle is issued randomly generated goals ten times, with an average distance between successive goals of more than 50 meters. During the experiment, an average of 10.2 persons came within 2m of the vehicle each minute. All encountered pedestrians are part of the regular daily traffic, and not testers/personnel associated with this work. For example, there were undergraduate students going between lectures and tourists visiting the campus. At a nominal speed of 1.2m/s, which is approximately the average human walking pace, the vehicle maintained safe distance to the pedestrians and generally respected social norms. While a safety driver was walking approximately five meters behind vehicle, he never had to intervene or take over control at any time during the ten runs. Since people in North America follow the right-handed rule, the SA-CADRL policy with right-handed norms is used for the hardware experiment, which causes the vehicle to generally pass pedestrians on the right and overtake on the left. For examples, snippets of the experiment are shown in Fig. 8. A hardware demonstration video can be found at

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This work presented SA-CADRL, a multiagent collision avoidance algorithm that considers and exhibits socially compliant behaviors. In particular, in a reinforcement learning framework, a pair of simulated agents navigate around each other to learn a policy that respect human navigation norms, such as passing on the right and overtaking on the left in a right-handed system. This approach is further generalized to multiagent ($n > 2$) scenarios through the use of a symmetrical neural network structure. Moreover, SA-CADRL is implemented on robotic hardware, which enabled fully autonomous navigation at human walking speed in a dynamic environment with many pedestrians. Future work will consider the relationships between nearby pedestrians, such as a group of people who walk together.
