<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Comparison of Action Spaces for Learning Manipulation Tasks

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Designing reinforcement learning (RL) problems that can produce delicate and precise manipulation policies requires careful choice of the reward function, state, and action spaces. Much prior work on applying RL to manipulation tasks has defined the action space in terms of direct joint torques or reference positions for a joint-space proportional derivative (PD) controller. In practice, it is often possible to add additional structure by taking advantage of model-based controllers that support both accurate positioning and control of the dynamic response of the manipulator. In this paper, we evaluate how the choice of action space for dynamic manipulation tasks affects the sample complexity as well as the final quality of learned policies. We compare learning performance across three tasks (peg insertion, hammering, and pushing), four action spaces (torque, joint PD, inverse dynamics, and impedance control), and using two modern reinforcement learning algorithms (Proximal Policy Optimization and Soft Actor-Critic). Our results lend support to the hypothesis that learning references for a task-space impedance controller significantly reduces the number of samples needed to achieve good performance across all tasks and algorithms.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent work in model-free reinforcement learning (RL) has demonstrated the ability to solve difficult high-dimensional problems in robotics. However, formulating a successful learning problem requires both expert knowledge and extensive experimentation to design the reward function, state space, and action space of the underlying Markov decision process (MDP). In many cases, we can take advantage of existing partial models of the problem (e.g., the equations of motion for a robot arm) to avoid learning dynamics that are well understood, and thus simplify learning. This paper is aimed at evaluating how learning performance can be improved across a set of example dynamic manipulation tasks by choosing action spaces that take advantage of model-based controllers.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Two popular choices of action spaces in the robotics RL literature are direct torque control and joint-space proportional derivative (PD) control. These action spaces are favorable because they are easy to implement, require relatively little information about the underlying system dynamics, and inject very little bias into the learning problem. On the other hand, these action spaces require learning to compensate for dynamic effects (e.g., inertial, gravitational, and centrifugal forces) that we are frequently able to model accurately. We expect that this may reduce learning performance, even for very simple manipulation tasks. Indeed, it is often necessary in practice to implement gravity compensation to learn successful manipulation strategies using torque control.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Johannink et al. have shown that formulating the learning task to learn residuals to a hand-crafted model-based controllers can improve learning efficiency. Another approach is to design the action space in terms of references for an underlying model-based controller. Inverse dynamics and task-space impedance control strategies have been successful for manipulation tasks because of their ability to achieve compliant interaction with the world, especially in the presence of uncertainty. Early success in high-tolerance peg insertion tasks, for example, was a result of the intelligent incorporation of mechanical compliance. In principle, RL algorithms that control joint torques directly can learn compliant manipulation strategies; however, it is not clear how this impacts sample efficiency and the quality of the resulting policy.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We hypothesize that taking advantage of model-based controllers and defining action spaces as reference inputs to these controllers can 1) improve the sample efficiency of learning manipulation tasks and 2) result in higher quality learned policies. In this paper, we provide preliminary evidence in support of this hypothesis using two modern on-policy (Proximal Policy Optimization, PPO ) and off-policy (Soft Actor-Critic, SAC ) RL algorithms across four choices of action spaces for three simulated manipulation tasks (nail hammering, object pushing, and peg insertion).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Learning Algorithms", "weight": 1.0} -->

Reinforcement learning problems are posed in the framework of Markov decision processes (MDP), which are defined by a set of states, $\mathcal{S}$, actions, $\mathcal{A}$, stochastic dynamics, $p{(\left. s_{t + 1} \middle| {s_{t},a_{t}} \right.)}$, a reward function $r{(s,a)}$, and a discount factor, $\gamma$. The reinforcement learning objective is to compute the policy, $\pi^{\ast}{(s,a)}$, that maximizes the expected discounted sum of rewards, ${\mathbb{E}}_{s,a}\left( {\sum_{t}{\gamma^{t}r_{t}}} \right)$. Since we are interested in the choice of action space and its effect on learning performance, we vary that element of the MDP while keeping the states, rewards, and discount factor fixed.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Learning Algorithms", "weight": 1.0} -->

We train all learning tasks with two state-of-the-art on- and off-policy reinforcement learning algorithms: Proximal Policy Optimization (PPO) and Soft Actor-Critic (SAC). Implementations of both are made available by the stable-baselines project, a software fork of the OpenAI baselines package.

<!-- chunk {"id": "body-0009", "role": "body", "section": "III-A Proximal Policy Optimization (PPO)", "weight": 1.0} -->

The Proximal Policy Optimization algorithm is an on-policy policy gradient method that uses an actor-critic framework to jointly learn the optimal policy as well as the optimal value function. Similar to Trust Region Policy Optimization (TRPO), PPO stabilizes policy training by penalizing large policy updates, an idea similar to trust-region methods or regularization techniques from the optimization literature. Because PPO is on-policy, each update must be computed with samples taken from the current policy, which can generally result in high sample complexity.

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-B Soft Actor-Critic (SAC)", "weight": 1.0} -->

The Soft Actor-Critic algorithm is an off-policy reinforcement learning method that is based on soft Q-learning (SQL). Unlike many RL algorithms, SAC optimizes a "maximum entropy" objective,

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-B Soft Actor-Critic (SAC)", "weight": 1.0} -->

which encourages exploration according to a temperature parameter $\alpha$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-B Soft Actor-Critic (SAC)", "weight": 1.0} -->

In this maximum entropy framework, the optimal policy is given by the soft Bellman equation which provides the basis for the SQL algorithm. SAC makes a number of improvements on SQL by automatically tuning the temperature parameter, $\alpha$, using double Q-learning, similar to the Twin Delayed DDPG (TD3) algorithm, to correct for overestimation in the Q-function, and learning not only the Q-functions and the policy but also the value function. Furthermore, because SAC is an off-policy algorithm it uses a replay buffer to reuse information from recent rollouts for sample-efficient training.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Action Spaces", "weight": 1.0} -->

There are a number of common control techniques employed by the RL community as well as in traditional manipulation. We analyze the performance of four common controllers on their performance in learning: direct torque control, proportional derivative (PD) control, an inverse dynamics (ID) controller, and an impedance controller. In traditional robotic control, the choice of controller to implement often considers a tradeoff between ease of implementation (torque and PD control are relatively simple), with the performance that can be gained by considering the dynamics of the system being controlled (ID and impedance control both attempt to compensate for the system dynamics). We hypothesize that we will see a similar tradeoff when designing the action space for an RL problem in terms of these controllers.

<!-- chunk {"id": "body-0014", "role": "body", "section": "IV-A Direct Torque Input", "weight": 1.0} -->

The most common action space for reinforcement learning for robots in simulation maps actions directly to joint torques. This control strategy is trivial to implement and introduces minimal bias into the learning process in the sense that the policy can arbitrarily shape the robot's behavior within physical constraints. One criticism of controlling torques directly is that doing so requires the learned controller to compensate for the full dynamics of the robot, including gravity, Coriolis, and centrifugal forces. Additionally, it is possible for policies to output high-frequency torque signals, so care usually has to be taken to encourage smooth policy outputs before learned policies can be deployed on hardware.

<!-- chunk {"id": "body-0015", "role": "body", "section": "IV-A Direct Torque Input", "weight": 1.0} -->

In our experiments, we found that even learning to compensate for gravity was difficult and required long training times when it did succeed. As a result, we augment the direct torque controller with a gravity compensation controller to improving training. This is a common technique and is easily justified by the fact that many robot arms have built-in gravity compensation controllers that must be treated as part of the closed-loop dynamics. Furthermore, because motors at proximal joints move more mass than those at distal joints, they tend to exert more torque. We found it beneficial for training to scale the torques at each joint by the cumulative mass of all of the child links. The resulting control law is

<!-- chunk {"id": "body-0016", "role": "body", "section": "IV-A Direct Torque Input", "weight": 1.0} -->

where $u$ are the control torques, $\pi$ is the policy, $s$ is the state, $m_{s}$ is a vector representing the subtree mass of each joint, and $g{(q)}$ is the position dependant gravity compensation control term. The operator $\odot$ is used to indicate element-wise vector multiplication.

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-B PD Control", "weight": 1.0} -->

Another controller that makes minimal assumptions about the system dynamics is proportional derivative (PD) control. PD control can provide good tracking performance but at the cost of large gains, resulting in very stiff movements.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-B PD Control", "weight": 1.0} -->

Similar to torque control, PD control suffers from scaling problems because the effective mass at each of the joints in an articulated body may span many orders of magnitude. This requires very different gains across each of the joints. In our experiments, we scale the proportional gains, $K_{p}$, by the subtree mass, and we choose the derivative gains, $K_{d}$, to be either the approximate critical damping gains or the maximum stable damping gains

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-B PD Control", "weight": 1.0} -->

where ${\overset{\sim}{K}}_{p}$ is a vector of unscaled proportional gains and $\Deltat$ is the simulation timestep.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-C Inverse Dynamics Control", "weight": 1.0} -->

The dynamics of an articulated body system can be written in terms of the manipulator equation,

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-C Inverse Dynamics Control", "weight": 1.0} -->

where $H$, $C$, and $G$ are the mass matrix, Coriolis/centrifugal, and gravity terms respectively, and $B$ and $J$ map control inputs, $u$, and external forces $\lambda$ to generalized forces. If $B$ is full rank, we can compute the control input, $u$, that corresponds to an arbitrary acceleration, $\overset{¨}{q}$. In the absence of external forces the inverse dynamics are given by

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-C Inverse Dynamics Control", "weight": 1.0} -->

where ${\overset{¨}{q}}_{\text{des}}$ is the desired acceleration. It is common to combine inverse dynamics and PD control with the control law

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-C Inverse Dynamics Control", "weight": 1.0} -->

In our experiments we set the damping gains to be the critical damping gains

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-C Inverse Dynamics Control", "weight": 1.0} -->

Note that because the accelerations are mapped through the mass matrix, this controller doesn't suffer from the same scaling issues that arise in torque control and PD control.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-D Impedance Control", "weight": 1.0} -->

While the three previous controllers are all configuration space controllers, the impedance controller is a task space controller. Impedance control regulates the end effector dynamics to mimic a mechanical spring-damper system,

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-D Impedance Control", "weight": 1.0} -->

where $x$ is the end effector pose, $B$ is a damping matrix, and $K$ is a stiffness matrix. Taking two time derivatives of the end effector pose with respect to the joint coordinates, we get the relation $\overset{¨}{x} = {{J\overset{¨}{q}} + {\overset{˙}{J}\overset{˙}{q}}}$, where $J$ is the end effector Jacobian. Again, using the inverse dynamics, we can write the control law as

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-D Impedance Control", "weight": 1.0} -->

In our experiments, we use a simplified control law

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-D Impedance Control", "weight": 1.0} -->

because computing $\overset{˙}{J}\overset{˙}{q}$ in MuJoCo is computationally expensive. We can justify this as impedance control with an additional nonlinear damping term, $- {J^{+}\overset{˙}{J}\overset{˙}{q}}$. Finally, since our arm has seven degrees of freedom, we damp out motions in the null space of the Jacobian with an additional damping term, ${({I - {J^{+}J}})}B_{\text{null}}\overset{˙}{q}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluated the performance of these action spaces on three representative manipulation tasks from the RL literature: peg insertion, nail hammering, and object pushing. Our experiments are performed on a model of a 7 degree of freedom Kuka IIWA 14 arm. Figure 1 illustrates the setup for each of the three experiments. All experiments were simulated in MuJoCo. The hyperparameters for each experiment can be found in the Appendix, and all of the code used for these experiments is publicly available in our GitHub repository.

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-A Peg Insertion Environment", "weight": 1.0} -->

Peg insertion is one of the most common manipulation tasks in robot assembly and requires navigating narrow bottlenecks in configuration space. This experiment consists of inserting a peg, rigidly affixed to the end effector, into a hole with 2 mm clearance. In order to provide a generous comparison with the torque controller, gravity is disabled in the simulation. The observations consist of joint positions and velocities, the relative pose between the tip of the peg and the bottom of the hole, and the velocity of the end effector. The reward function is quadratic in the peg tip distance, $\Deltap$, and the orientation error, $\Delta\theta$,

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-A Peg Insertion Environment", "weight": 1.0} -->

The peg tip distance is computed from the relative position between the hole and the peg tip and the orientation error is the relative angle between the peg orientation and the hole orientation.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-B Hammering Environment", "weight": 1.0} -->

Hammering requires the controlled accumulation and delivery of momentum to a specific location in task space. The "nail" is 20 cm long and experiences static friction that can resist 20 N of force; we found this to be sufficiently high to require multi-impact hammering strategies rather than brute force pushing strategies. Similarly to the insertion task, gravity was disabled in order to learn useful strategies with the torque controller. The observations consist of joint positions and velocities, the nail position and velocity, the relative pose between the hammer face and the head of the nail, and the end effector velocity. The reward function is linear in the nail height as well as the peg velocity,

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-B Hammering Environment", "weight": 1.0} -->

Note that this reward structure is sparse, meaning that it is possible for the robot to experience many episodes without receiving any rewards.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-C Object Pushing Environment", "weight": 1.0} -->

In this experiment, we consider the problem of pushing an object from one position to another without tipping it over. The object is a rectangular prism, 30cm long, 2cm in width, and 6cm in height, and it is initialized to be standing on its narrow side. The robot is equipped with the same peg-like end effector from the insertion task. Unlike the hammering and insertion experiments, gravity is required to keep the block in contact with the table and provide frictional forces, so rather than disabling gravity we add a gravity compensation torque to the torque controller as well as the PD controller. The observations consist of the joint positions and velocities, the relative pose between the end effector and the center of the block, and the end effector velocity. The reward function is

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-C Object Pushing Environment", "weight": 1.0} -->

where $\Deltap_{\text{block}}$ and $\Delta\theta_{\text{block}}$ are the relative position and orientation of the block respectively. The desired pose, $\Deltah_{\text{peg}}$, is the difference in height between the height of the block and the height of the peg, and $\Delta\theta_{\text{peg}}$ is the angle between the axis of the peg and vertical. The last two terms encourage the end effector to remain in-plane with the block, and the coefficients $k_{\text{h}}$ and $k_{\theta}$ are small to minimize unnecessary bias.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Results", "weight": 1.0} -->

The results of each of our experiments are collected in Table I. The success criteria for the three tasks are: 80% average nail depth for the hammer task, 80% success rate for the insertion task, and 80% of the normalized distance to the goal for the pushing task. In all of our experiments, we found the impedance controller action space to have learned the fastest, often followed by the inverse dynamics controller, PD controller, and then the torque controller. The favorable performance of the impedance controller can be understood in terms of the simplifying effect it has on the underlying task dynamics.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Results", "weight": 1.0} -->

* 111The torque action space did not cross the 80% threshold before 5 million steps.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Results", "weight": 1.0} -->

The role of compliance is highlighted in the pushing task. In order to keep the block upright while pushing it to the desired location, the interactions need to be gentle. Large contact forces can cause the block to topple, incurring a large cost for the remainder of an episode. Without the proper compliance, an algorithm can learn to avoid the block altogether. The impedance controller, the inverse dynamics controller, and the PD controller all have some inherent compliance and learn relatively quickly how to manipulate the block without knocking it over. The torque controller, however, has no inherent compliance and struggles with the task, learning three times slower than the impedance controller when trained with PPO and failing altogether when trained with SAC. There are also some qualitative differences between the learning curves for PPO and SAC. This can be attributed to the peculiarities of the two algorithms; PPO is gradient based and has asymptotic convergence guarantees, whereas Q-learning with function approximation, the basis for SAC, is known to suffer from instabilities during learning.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Results", "weight": 1.0} -->

Somewhat surprisingly, the inverse dynamics controller shows improved performance over PD controller across five of the six experiments. It would have been reasonable to expect that, since both controllers are using a PD loop with comparable stiffnesses for feedback control, their performance would have been roughly equivalent on all tasks. It is noteworthy that this discrepancy is largest for the hammering task, where velocities are large, highlighting the sensitivity of these learning methods to the dynamics of the underlying system. During a hammer swing, inertial forces, rather than the feedback terms, can dominate the dynamics of the PD controller. The inverse dynamics controller, however, compensates for this inertial coupling between joints.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Results", "weight": 1.0} -->

One of the biggest characteristics that sets the impedance controller apart, however, is that actions are specified in task space rather than configuration space. Because there is usually a straightforward mapping between the quantities in the reward function and the action space, the impedance controller often discovers useful behaviors much more quickly, without the extended exploration phase that the joint space controllers tend to exhibit. In the peg insertion task, for example, the space of successful joint configurations is quite complex, while the set of successful end effector poses is relatively simple. While the impedance control policy only needs to discover this simple set of poses, a joint space controller must also learn to solve an inverse kinematics problem to perform the insertion. Figure 2 shows this phenomenon most clearly in the case of the hammering task. There, the impedance controller discovers the location of the nail very quickly and soon after completes the task. The joint space controllers require much more exploration before discovering the nail, then require longer training periods to refine the details of the task after the nail is located.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Results", "weight": 1.0} -->

Qualitatively the policies learned in the different action spaces are also very different. The impedance, inverse dynamics, and PD controllers all exhibit slow, controlled motions whereas the torque controller tends to exhibit more aggressive motions with seemingly uncontrolled collisions with the environment. The impedance controller can exhibit odd artifacts near kinematic singularities during early training, but these are less noticeable in policies that have converged.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Results", "weight": 1.0} -->

It is worth mentioning that we have gone to significant lengths to provide the best possible implementation of both the torque controller and the PD controller. Without care to scale the action space at each link by the mass of the child links, learning is significantly slower. In the presence of gravity, the torque controller learns none of the tasks, and in order for the PD controller to successfully complete the tasks, the gains would need to be increased by an order of magnitude, hindering its ability to be compliant in the presence of contact.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We evaluated learning performance for three dynamic manipulation tasks using four different action spaces: direct torque control, joint PD, inverse dynamics, and task-space impedance control. Action spaces defined in terms of torque control and PD control learned significantly slower than impedance control or inverse dynamics control on all of our experiments. These results are complementary to the results by Peng et al. in that PD control improves sample efficiency over direct torque control. However, we show that there can be additional benefit by wrapping the PD controller in an inverse dynamics routine, and that in many situations task-space impedance control has significant benefits over all of the joint space policies.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Choosing the action space represents a trade-off between the engineering effort required to build and calibrate model-based controllers, and sample efficiency during learning. While it is sometimes desirable to prioritize simplicity of implementation, we expect that learning efficiency can usually be improved by incorporating model-based controllers that simplify some or all of the underlying task dynamics.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusions", "weight": 1.0} -->

One criticism of using model-based controllers in conjunction with model-free learning is additional dependence on having a model of the robot. While some of the details of the dynamics of manipulators---such as static friction in the joints---can be difficult to model, the inertial and kinematic model of the manipulators are often well known. The key point is that even if we cannot model all of the relevant dynamics in the learning task (e.g., we made no attempt to model the contact interaction between the robot and environment), there still may be value in exploiting what models are available to reduce the complexity of the learning problem, similar to previous findings on residual learning.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Finally, the experiments presented here do not address the potential for model mismatch between simulation and hardware. We expect policies learned with model errors to be able to compensate for the mismatch during learning, but it is unclear how this may affect learning performance and transfer of learned policies from simulation to hardware. We plan to investigate this further in future work.
