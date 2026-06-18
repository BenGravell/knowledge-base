<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Leveraging Demonstrations for Deep Reinforcement Learning on Robotics Problems with Sparse Rewards

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a general and model-free approach for Reinforcement Learning (RL) on real robotics with sparse rewards. We build upon the Deep Deterministic Policy Gradient (DDPG) algorithm to use demonstrations. Both demonstrations and actual interactions are used to fill a replay buffer and the sampling ratio between demonstrations and transitions is automatically tuned via a prioritized replay mechanism. Typically, carefully engineered shaping rewards are required to enable the agents to efficiently explore on high dimensional control problems such as robotics. They are also required for model-based acceleration methods relying on local solvers such as iLQG (e.g. Guided Policy Search and Normalized Advantage Function). The demonstrations replace the need for carefully engineered rewards, and reduce the exploration problem encountered by classical RL approaches in these domains. Demonstrations are collected by a robot kinesthetically force-controlled by a human demonstrator. Results on four simulated insertion tasks show that DDPG from demonstrations out-performs DDPG, and does not require engineered rewards. Finally, we demonstrate the method on a real robotics task consisting of inserting a clip (flexible object) into a rigid object.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The latest generation of collaborative robots are designed to eliminate cumbersome path programming by allowing humans to *kinesthetically guide* a robot through a desired motion. This approach dramatically reduces the time and expertise required to get a robot to solve a novel task, but there is still a fundamental dependence on scripted trajectories. Consider the task of inserting a wire into a connector: it is difficult to imagine any predefined motion which can handle variability in wire shape and stiffness. To solve these sorts of tasks, it is desirable to have a richer control policy which considers a large amount of feedback including states, forces, and even raw images. Reinforcement Learning (RL) offers, in principle, a method to learn such policies from exploration, but the amount of actual exploration required has prohibited its use in real applications. In this paper we address this challenge by combining the demonstration and RL paradigms into a single framework which uses kinesthetic demonstrations to guide a deep-RL algorithm. Our long-term vision is for it to be possible to provide a few minutes of demonstrations, and have the robot rapidly and safely learn a policy to solve arbitrary manipulation tasks.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The primary alternative to demonstrations for guiding RL agents in continuous control tasks is reward shaping. Shaping is typically achieved using a hand-coded function, such as Cartesian distance to a goal site, which provides a smoothly varying reward signal for every state the agent visits. While attractive in theory, reward shaping can lead to bizarre behavior or premature convergence to local minima, and in practice requires considerable engineering and experimentation to get right. By contrast, it is often quite natural to express a task goal as a sparse reward function, e.g. +1 if the wire is inserted, and 0 otherwise. Our central contribution is to show that off-policy replay-memory-based RL (e.g. DDPG) is a natural vehicle for injecting demonstration data into sparse-reward tasks, and that it obviates the need for reward-shaping. In contrast to on-policy RL algorithms, such as classical policy gradient, DDPG can accept and learn from arbitrary transition data. Furthermore, the replay memory allows the agent to maintain these transitions for long enough to propagate the sparse rewards throughout the value function.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present results of simulation experiments on a set of robot insertion problems involving rigid and flexible objects. We then demonstrate the viability of our approach on a real robot task consisting of inserting a clip (flexible object) into a rigid object. This task is realized by a Sawyer robotic arm, using demonstrations collected by kinesthetically controlling an arm by the wrist. Our results suggest that sparse rewards and a few human demonstrations are a practical alternative to shaping for teaching robots to solve challenging continuous control tasks.

<!-- chunk {"id": "body-0006", "role": "body", "section": "DDPG from Demonstrations", "weight": 1.0} -->

Our algorithm modifies DDPG to take advantage of demonstrations. The demonstrations are of the form of RL transitions: $(s,a,s^{\prime},r)$. DDPGfD loads the demonstration transitions into the replay buffer before the training begins and keeps all transitions forever.

<!-- chunk {"id": "body-0007", "role": "body", "section": "DDPG from Demonstrations", "weight": 1.0} -->

DDPGfD uses prioritized replay to enable efficient propagation of the reward information, which is essential in problems with sparse rewards. Prioritized experience replay modifies the agent to sample more important transitions from its replay buffer more frequently. The probability of sampling a particular transition $i$ is proportional to its priority, ${P{(i)}} = \frac{p_{i}^{\alpha}}{\sum_{k}p_{k}^{\alpha}}$, where $p_{i}$ is the priority of the transition. DDPGfD uses $p_{i} = {\delta_{i}^{2} + {\lambda_{3}{|{{\nabla_{a}Q}{(s_{i},\left.

<!-- chunk {"id": "body-0008", "role": "body", "section": "DDPG from Demonstrations", "weight": 1.0} -->

a_{i} \middle| \theta^{Q} \right.)}}|}^{2}} + \epsilon + \epsilon_{D}}$, where $\delta_{i}$ is the last TD error calculated for this transition, the second term represents the loss applied to the actor, $\epsilon$ is a small positive constant to ensure all transitions are sampled with some probability, $\epsilon_{D}$ is a positive constant for demonstration transitions to increase their probability of getting sampled, and $\lambda_{3}$ is used to weight the contributions. To account for the change in the distribution, updates to the network are weighted with importance sampling weights, $w_{i} = {({\frac{1}{N} \cdot \frac{1}{P{(i)}}})}^{\beta}$. DDPGfD uses $\alpha = 0.3$ and $\beta = 1$ as we want to learn about the correct distribution from the very beginning.

<!-- chunk {"id": "body-0009", "role": "body", "section": "DDPG from Demonstrations", "weight": 1.0} -->

In addition, the prioritized replay is used to prioritize samples between the demonstration and agent data, controlling the ratio of data between the two in a natural way.

<!-- chunk {"id": "body-0010", "role": "body", "section": "DDPG from Demonstrations", "weight": 1.0} -->

A second modification for the sparse reward case is to use a mix of 1-step and n-step returns when updating the critic function. Incorporating n-step returns helps propagate the Q-values along the trajectories. The $n$-step return loss consists of using rollouts (forward view) of size $n$ of a policy $\pi$ close to the current policy $\pi{(.|\theta^{\pi})}$ in order to evaluate the action-value function $Q{(.|\theta^{Q})}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "DDPG from Demonstrations", "weight": 1.0} -->

A third modification is to do multiple learning updates per environment step. If a single learning update per environment step is used, each transition will only be sampled as many times as the size of the minibatch. Choosing a balance between gathering fresher data and doing more learning is in general a complicated trade-off. If our data is stale, the samples from the replay buffer no longer represent the distribution of states our current policy would experience. This can lead to wrong Q values in states which were not previously visited and potentially cause our policy and values to diverge. However in our case we require data efficiency and therefore we need to use each transition several times. In our experiments, we could increase the number of learning updates to $20$ without affecting the per-update learning efficiency. In practice, we used the value of $40$ which provided a good balance between learning from previous interaction (data efficiency) and stability.

<!-- chunk {"id": "body-0012", "role": "body", "section": "DDPG from Demonstrations", "weight": 1.0} -->

Finally, L2 regularization on the parameters of the actor and the critic networks are added to stabilize the final learning performance.

<!-- chunk {"id": "body-0013", "role": "body", "section": "DDPG from Demonstrations", "weight": 1.0} -->

Transitions from a human demonstrator are added to the replay buffer.

<!-- chunk {"id": "body-0014", "role": "body", "section": "DDPG from Demonstrations", "weight": 1.0} -->

Prioritized replay is used for sampling transitions across both the demonstration and agent data.

<!-- chunk {"id": "body-0015", "role": "body", "section": "DDPG from Demonstrations", "weight": 1.0} -->

Learning multiple times per environment step.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Our approach is designed for problems in which it is easy to specify a goal state, but difficult to specify a smooth distance function for reward shaping that does not lead to sub-optimal behavior. One example of this is insertion tasks in which the goal state for the plug is at the bottom of a socket, but the only path to reach it, and therefore the focus of exploration, is at the socket opening. While this may sound like a minor distinction, we found in our initial experiments that DDPG with a simple goal-distance reward would quickly find a path to a local minimum on the *outside* of the socket, and fail to ever explore around the opening.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We therefore sought to design a set of insertion tasks that presented a range of exploration difficulties. Our tasks are illustrated in Fig. 1. The first (Fig. 1(a)) is a classic peg-in-hole task, in which both bodies are rigid, and the plug is free to rotate along the insertion axis. The second (Fig. 1(b)) models a drive-insertion problem into an ATX-style computer chassis. Both bodies are again rigid, but in this case the drive orientation is relevant. The third task (Fig. 1(c)) models the problem of inserting a two-pronged deformable plastic clip into a housing. The clip is modeled as three separate bodies with hinge joints at the base of each prong. These joints are spring-loaded, and the resting state pinches inwards as is common with physical connectors to maintain pressure on the housing. The final task (Fig. 1(d)) is a simplified cable insertion task in which the plug is modeled as a 20-link chain of capsules coupled by ball-joints. This cable is highly under-actuated, but otherwise shares the same task specification as the peg-in-hole task.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We created two reward functions for our experiments.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

where $x_{i}$ is the position of the $i^{th}$ tip site on the plug, $g_{i}$ is the $i^{th}$ goal site on the socket, $W_{g}$ contains weighting coefficients for the goal site error vector, and $\epsilon$ is a proximity threshold. If this tolerance was reached, the robot received the reward signal and the episode was immediately terminated.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

The second reward function is a shaped reward which composes terms for two movement phases: a reaching phase $c_{o}$ to align the plug to the socket opening, and an inserting phase $c_{g}$ to reach the socket goal. Both terms compute a weighted $\ell_{2}$-distance between the plug tip(s) and their respective goal site(s). The distance from the goal to the opening site (*i.e.*

<!-- chunk {"id": "body-0021", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

where $g_{i}$ is the $i^{th}$ goal site, $o_{i}$ is the $i^{th}$ opening site, $W_{g}$ and $W_{o}$ are weighting coefficients for the goal and opening site errors, respectively, $I$ is the indicator function, and $\alpha$ and $\beta$ are scaling parameters for log-transforming these distances into rewards ranging from $0$ to $1$. Note that tuning the weighting of each dimension in $W_{g}$ and $W_{o}$ must be done very carefully for the agent to learn the real desired task. In addition, the shaping of both stages must be balanced out in a delicate manner.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

All tasks utilized a single vertically mounted robot arm. The robot was a Sawyer 7-DOF torque-controlled arm from Rethink Robotics, instrumented with a cuff for kinesthetic teaching. We utilized the Mujoco simulator to simulate the Sawyer using publicly available kinematics and mesh files. In the simulation experiments the actions were joint velocities, the rewards were sparse or shaped as described above, and the observations included joint position and velocity, joint-torque feedback, and the global pose of the socket and plug. In both the simulation and real world experiments the object being inserted was rigidly attached to the gripper, and the socket was fixed to a table top.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

In addition to the four simulation tasks, we also constructed a real world clip insertion problem using a physical Sawyer robot. In the real robot experiment the clip was rigidly mounted to the robot gripper using a 3D printed attachment. The socket position was provided to the robot, and rewards were computed by evaluating the distance from the clip prongs (available via the robot's kinematics) to the goal sites in the socket as described above. In real robot experiments the observations included the robot joint position and velocity, gravity-compensated torque feedback from the joints, and the relative pose of the plug tip sites in the socket opening site frames.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Demonstration data collection", "weight": 1.0} -->

To collect the demonstration data in simulated tasks, we used a Sawyer robotic arm. The arm was kinesthetically force controlled by a human demonstrator. In simulation an agent was running a hard-coded joint space P-controller to match the joint positions of the simulated Sawyer robot to the joint positions of the real one. This agent was using the same action space as the DDPGfD agent which allowed the demonstration transitions to be added directly to the agent's replay buffer.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Demonstration data collection", "weight": 1.0} -->

For providing demonstration for the real world tasks we used the same setup, this time controlling a second robotic arm. Separating the arm we were controlling and the arm which solved the task ensured that the demonstrator did not affect the dynamics of the environment from the agent's perspective. For each experiment, we collected 100 episodes of human demonstrations which were on average about 25 steps ($\approx 5$s) long. This involved a total of 10-15 minutes of robot interaction time per task.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Results", "weight": 1.0} -->

In our first experiment we compared our approach to DDPG on sparse and shaped variants of the four simulated robotic tasks presented in Sec. 4. In addition, we show rewards for the demonstrations themselves as well as supervised imitation of the demonstrations. The DDPG implementation utilized all of the optimizations we incorporated into DDPGfD, including prioritized replay, n-step returns, and $\ell$-2 regularization. For each task we evaluated the agent with both the shaped and sparse versions of the reward, with results shown in Figure 3. All traces plot the shaped-reward value achieved, regardless of which reward was given to the agent. All of these experiments were performed with fixed hyper-parameters, tuned in advance.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Results", "weight": 1.0} -->

We can see that in the case where we have hand-tuned shaping rewards all algorithms can solve the task. The results show that DDPGfD always out-performs DDPG, even when DDPG is given a well-tuned shaping reward. In contrast, DDPGfD learns nearly as well with sparse rewards as with shaping rewards. DDPGfD even out-performs DDPG on the hard drive insertion task, where the demonstrations are relatively poor. In general, DDPGfD not only learns to solve the task, but learns to solve it more efficiently than the demonstrations, usually learning to insert the object in 2-4x fewer steps than the demonstrations. DDPGfD also learns more reliably, as the percentile plots are much wider for DDPG. Doing purely supervised learning of the demonstration policy performs poorly in every task.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Results", "weight": 1.0} -->

In our second experiment we examined the effect of varying the quantity of demonstration data on agent performance. Fig. 4(a) compares learning curves for DDPGfD agents initialized with 1, 2, 3, 5, 10, and 100 expert trajectories on the sparse-reward clip-insertion task. DDPGfD is capable of solving this task with only a single demonstration, and we see diminishing returns with 50-100 demonstrations. This was surprising, since each demonstration contains only one state transition with non-zero reward.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Results", "weight": 1.0} -->

Finally, we show results of DDPGfD learning the clip insertion task on physical Sawyer robot in Figure 4(b). DDPGfD was able to learn a robust insertion policy on the real robot. DDPGfD with sparse rewards outperforms shaped DDPG, showing that DDPGfD achieves faster learning without the extra engineering.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper we presented DDPGfD, an off-policy RL algorithm which uses demonstration trajectories to quickly bootstrap performance on challenging motor tasks specified by sparse rewards. DDPGfD utilizes a prioritized replay mechanism to prioritize samples across both demonstration and self-generated agent data. In addition, it incorporates n-step returns to better propagate the sparse rewards across the entire trajectory.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Most work on RL in high-dimensional continuous control problems relies on well-tuned shaping rewards both for communicating the goal to the agent as well as easing the exploration problem. While many of these tasks can be defined by a terminal goal state fairly easily, tuning a proper shaping reward that does not lead to degenerate solutions is very difficult. This task only becomes more difficult when you move to multi-stage tasks such as insertion. In this work, we replaced these difficult to tune shaping reward functions with demonstrations of the task from a human demonstrator. This eases the exploration problem without requiring careful tuning of shaping rewards.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In our experiments we sought to determine whether demonstrations were a viable alternative to shaping rewards for training object insertion tasks. Insertion is an important subclass of object manipulation, with extensive applications in manufacturing. In addition, it is a challenging set of domains for shaping rewards, as it requires two stages: one for reaching the insertion point, and one for inserting the object. Our results suggest that Deep-RL is poised to have a large impact on real robot applications by extending the learning-from-demonstration paradigm to include richer, force-sensitive policies.
