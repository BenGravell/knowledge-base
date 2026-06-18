<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-efficient Deep Reinforcement Learning for Dexterous Manipulation

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Deep learning and reinforcement learning methods have recently been used to solve a variety of problems in continuous control domains. An obvious application of these techniques is dexterous manipulation tasks in robotics which are difficult to solve using traditional control theory or hand-engineered approaches. One example of such a task is to grasp an object and precisely stack it on another. Solving this difficult and practically relevant problem in the real world is an important long-term goal for the field of robotics. Here we take a step towards this goal by examining the problem in simulation and providing models and techniques aimed at solving it. We introduce two extensions to the Deep Deterministic Policy Gradient algorithm (DDPG), a model-free Q-learning based method, which make it significantly more data-efficient and scalable. Our results show that by making extensive use of off-policy data and replay, it is possible to find control policies that robustly grasp objects and stack them. Further, our results hint that it may soon be feasible to train successful stacking policies by collecting interactions on real robots.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Dexterous manipulation is a fundamental challenge in robotics. Researchers have long been seeking a way to enable robots to robustly and flexibly interact with fixed and free objects of different shapes, materials, and surface properties in the context of a broad range of tasks and environmental conditions. Such flexibility is very difficult to achieve with manually designed controllers. The recent resurgence of neural networks and "deep learning" has inspired hope that these methods will be as effective in the control domain as they are for perception. And indeed, in simulation, recent work has used neural networks to learn solutions to a variety of control problems from scratch (e.g. ).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

While the flexibility and generality of learning approaches is promising for robotics, these methods typically require a large amount of data that grows with the complexity of the task. What is feasible on a simulated system, where hundreds of millions of control steps are possible, does not necessarily transfer to real robot applications due to unrealistic learning times. One solution to this problem is to restrict the generality of the controller by incorporating task specific knowledge, e.g. in the form of dynamic movement primitives, or in the form of strong teaching signals, e.g. kinesthetic teaching of trajectories. Recent works have had some success learning flexible neural network policies directly on real robots (e.g. ), but tasks as complex as grasping-and-stacking remain daunting.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

An important issue for the application of learning methods in robotics is to understand how to make the best use of collected data, which can be expensive to obtain, both in terms of time and money. To keep learning times reasonably low even in complex scenarios, it is crucial to find a practical compromise between the generality of the controller and the necessary restrictions of the task setup. This is the gap that we aim to fill in this paper: exploring the potential of a learning approach that keeps prior assumptions low while keeping data consumption in reasonable bounds. Simultaneously, we are interested in approaches that are broadly applicable, robust, and practical.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we provide a simulation study that investigates the possibility of learning complex manipulation skills end-to-end with a general purpose model-free deep reinforcement learning algorithm. The express goal of this work is to assess the feasibility of performing analogous end-to-end learning experiments on real robotics hardware and to provide guidance with respect to the choice of learning algorithm and experimental setup and the performance that we can hope to achieve.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The task which we consider to this end is that of picking up a Lego brick from the table and stacking it onto a second nearby brick using a robotic arm with 9 degrees of freedom (DoF), six in the arm and three for the fingers in the gripper. In addition to having a high-dimensional state and action space, the task exemplifies several of the challenges that are encountered in real-world manipulation problems. Firstly, it involves contact-rich interactions between the robotic arm and two freely moving objects. Secondly it requires mastering several sub-skills (reaching, grasping, and stacking). Each of these sub-skills is challenging in its own right as they require both precision (for instance, successful stacking requires accurate alignment of the two bricks) and as well as robust generalization over a large state space (e.g. different initial positions of the bricks and the initial configuration of the arm). Finally, there exist non-trivial and long-ranging dependencies between the solutions for different subtasks: for instance, the ability to successfully stack the brick in the later part of the task depends critically on having picked up the brick in a sensible way beforehand.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the algorithm side we build on the Deep Deterministic Policy Gradient (DDPG; ), a general purpose model-free reinforcement learning algorithm for continuous action spaces, and extend it in two ways (section V): firstly, we improve the the data efficiency of the algorithm by scheduling updates of the network parameters independently of interactions with the environment. Secondly, we overcome the computational and experimental bottlenecks of single-machine single-robot learning by introducing a distributed version of DDPG which allows data collection and network training to be spread out over multiple computers and robots.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We further propose two broadly applicable strategies that allow us to inject prior knowledge into the learning process in order to help reliably find solutions to complex tasks and further reduce the amount of environmental interaction. The first of these strategies is a recipe for designing effective shaping rewards for compositional tasks (section VI), while the second (section VII) uses a suitable bias in the distribution of initial states to achieve an effect akin to a curriculum or a form of apprenticeship learning.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In combination these contributions allow us to reliably learn robust policies for the full task from scratch in less than 10 million environment transitions. This corresponds to less than 10 hours of interaction time on 16 robots, thus entering a regime that no longer seems unrealistic with modern experimental setups. In addition, when states from successful trajectories are used as the start states for learning trials the full task can be learned with 1 million transitions (i.e. less than 1 hour of interaction on 16 robots). To our knowledge our results provide the first demonstration of solving complex manipulation problems involving multiple freely moving objects. They are also encouraging as a sensible lower bound for real-world experiments suggesting that it may indeed be possible to learn such non-trivial manipulation skills directly on real robots.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Task and experimental setup", "weight": 1.0} -->

The full task that we consider in this paper is to use the arm to pick up one Lego Duplo brick from the table and stack it onto the remaining brick. This "composite" task can be decomposed into several subtasks, including grasping and stacking.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Task and experimental setup", "weight": 1.0} -->

In every episode the arm starts in a random configuration with the positioning of gripper and brick appropriate for the task of interest. We implement the experiments in a physically plausible simulation in MuJoCo with the simulated arm being closely matched to a real-world Jaco arm^11^1Jaco is a robotics arm developed by Kinova Robotics setup in our lab. Episodes are terminated after 150 steps, with each step corresponding to 50ms of physical simulation time. This means that the agent has 7.5 seconds to perform the task. Unless otherwise noted we give a reward of one upon successful completion of the task and zero otherwise.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Task and experimental setup", "weight": 1.0} -->

The observation vector provided to the agent contains information about the angles and angular velocities of the 6 joints of the arm and 3 fingers of the gripper. In addition, we provide information about the position and orientation of the two bricks and relative distances of the two bricks to the pinch position of the gripper, i.e. roughly the position where the fingertips would meet if the fingers are closed. The 9-dimensional continuous action directly sets the velocities of the arm and finger joints. In experiments not reported in this paper we have tried using an observation vector containing only the raw state of the brick in addition to the arm configuration (i.e. without the vector between the end-effector and brick) and found that this increased the number of environment interactions needed roughly by a factor of two to three.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Task and experimental setup", "weight": 1.0} -->

The only hyper-parameter that we optimize for each experimental condition is the learning rate. For each condition we train and measure the performance of 10 agents with different random initial network parameters. After every 30 training episodes the agent is evaluated for 10 episodes. We used the mean performance at each evaluation phase as the performance measure presented in all plots. We found empirically that 10 episodes of evaluation gave a reasonable proxy for performance in the studied tasks. In the plots the line shows the mean performance for the set and the shaded regions correspond to the range between the worst and best performing agent in the set. In all plots the x-axis represents the number of environment transitions seen so far at an evaluation point (in millions) and the y-axis represent episode return.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Asynchronous DPG with variable replay steps", "weight": 1.0} -->

In this section we study two methods for extending the DDPG algorithm and find that they can have significant effect on data and computation efficiency, in some cases making the difference between finding a solution to a task or not.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Multiple mini-batch replay steps", "weight": 1.0} -->

Deep neural networks can require many steps of gradient descent to converge. In a supervised learning setting this affects purely computation time. In reinforcement learning, however, neural network training is interleaved with the acquisition of interaction experience, and the nature of the latter is affected by the state of the former -- and vice versa -- so the situation is more complicated. To gain a better understanding of this interaction we modified the original DDPG algorithm as described in to perform a fixed but configurable number of mini-batch updates per step in the environment. In one update was performed after each new interaction step.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Multiple mini-batch replay steps", "weight": 1.0} -->

We refer to DDPG with a configurable number of update steps as DPG-R and tested the impact of this modification on the two primitive tasks Grasp and StackInHand. The results are shown in Fig. 2. It is evident that the number of update steps has a dramatic effect on the amount of experience data required for learning successful policies. After one million interactions the original version of DDPG with a single update step (blue traces) appears to have made no progress towards a successful policy for stacking, and only a small number of controllers have learned to grasp. Increasing the number of updates per interaction to 5 greatly improves the results (green traces), and with 40 updates (purple) the first successful policies for stacking and grasping are obtained after 200,000 and 300,000 interactions respectively (corresponding to 1,300 and 2,000 episodes). It is notable that although the improvement is task dependent and the dependence between update steps and convergence is clearly not linear, in both cases we continue to see a reduction in total environment interaction up to 40 update steps, the maximum used in the experiment.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Multiple mini-batch replay steps", "weight": 1.0} -->

One may speculate as to why changing the number of updates per environment step has such a pronounced effect. One hypothesis is that, loosely speaking and drawing an analogy to supervised learning, insufficient training leads to underfitting of the policy and value network with respect to the already collected training data. Unlike in supervised learning, however, where the dataset is typically fixed, the quality of the policy directly feeds back into the data acquisition process since the policy network is used for exploration, thus affecting the quality the data used in future iterations of network training.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Multiple mini-batch replay steps", "weight": 1.0} -->

We have observed in various experiments (not listed here) that other aspects of the network architecture and training process can have a similar effect on the extent of underfitting. Some examples include the type of non-linearities used in the network layers, the size of layers and the learning rate. It is important to note that one cannot replicate the effect of multiple replay steps simply by increasing the learning rate. In practice we find that attempts to do so make training unstable.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Asynchronous DPG", "weight": 1.0} -->

While increasing the number of update steps relative to the number of environment interactions greatly improves the data efficiency of the algorithm it can also strongly increase the computation time. In the extreme case, in simulation, when the overall run time is dominated by the network updates it may scale linearly with the number of replay steps. In this setting it is desirable to be able to parallelize the update computations.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Asynchronous DPG", "weight": 1.0} -->

In a real robotics setup the overall run time is typically dominated by the collection of robot interactions. In this case it is desirable to be able to collect experience from multiple robots simultaneously (e.g. as in ).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Asynchronous DPG", "weight": 1.0} -->

We therefore develop an asynchronous version of DPG that allows parallelization of training and environment interaction by combining multiple instances of an DPG-R actor and critic that each share their network parameters and can be configured to either share or have independent experience replay buffers. This is inspired by the A3C algorithm proposed, and also analogous to. We found that this strategy is also an effective way to share parameters for DPG. That is, we employ asynchronous updates whereby each worker has its own copy of the parameters and uses it for computing gradients which are then applied to a shared parameter instance without any synchronization. We use the Adam optimizer with local non-shared first-order statistics and a single shared instance of second-order statistics. The pseudo code of the asynchronous DPG-R is shown in algorithm box 1.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Asynchronous DPG", "weight": 1.0} -->

Initialize global shared critic and actor network parameters:θQ'' and θμ''
Pseudo code for each learner thread:
Initialize critic network Q (s,a|θQ) and actor μ (s|θμ) with weights θQ and θμ. Initialize target network Q′ and μ′ with weights:θQ′ ← θQ, θμ′ ← θμ
Initialize replay buffer R
Receive initial observation state s1
Select action at = μ (st|θμ) + 𝒩t according to the current policy and exploration noise
Perform action, observe reward rt and new state st + 1
Sample a random minibatch of N transitions (si,ai,ri,si + 1) from R
Perform asynchronous update of the shared parameters of the critic by minimizing the loss:$L = {\frac{1}{N}{\sum_{i}{({y_{i} - {Q{(s_{i},\left.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Asynchronous DPG", "weight": 1.0} -->

Copy the shared parameters to the local ones:θQ ← θQ'', θμ ← θμ''
Every S update steps, update the target networks:θQ′ ← θQ, θμ′ ← θμ
Algorithm 1 (A)DPG-R algorithm

<!-- chunk {"id": "body-0025", "role": "body", "section": "Asynchronous DPG", "weight": 1.0} -->

Overall these results show that distributing neural network training and data collection across multiple computers and robots can be an extremely effective way of reducing the overall run time of experiments and thus making it feasible to run more challenging experiments. We make extensive use of asynchronous DPG for remaining the experiments.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Composite shaping rewards", "weight": 1.0} -->

In the previous section we discussed how the ability of DDPG to exploit information that is available in the acquired interaction data affects learning speed. One important factor that determines what information is available from this data is the nature of the reward function. The reward function in the previous section was "sparse" or "pure" reward where a reward of 1 was given for states that correspond to successful task completion (brick lifted above 3cm for grasp; for stack) and 0 otherwise. For this reward to be useful for learning it is of course necessary that the agent is able to enter this goal region in state space with whatever exploration strategy is chosen. This was indeed the case for the two subtasks in isolation, but it is highly unlikely for the full task: without further guidance naïve random exploration is very unlikely to lead to a successful grasp and stack as we also experimentally verify in Fig. 5.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Composite shaping rewards", "weight": 1.0} -->

One commonly used solution to this problem is to provide informative shaping rewards that allow a learning signal to be obtained even with simple exploration strategies, e.g. by embedding information about the value function in the reward function for every transition acquired from the environment. For instance, for a simple reaching problem with a robotic arm we could define a shaping reward that takes into account the distance between the end-effector and the target.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Composite shaping rewards", "weight": 1.0} -->

While this a convenient way of embedding prior knowledge about the solution and is a widely and successfully used approach for simple problems it comes with several caveats, especially for complex sequential or compositional tasks such as the one we are interested in here.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Composite shaping rewards", "weight": 1.0} -->

Firstly, while a suitable shaping reward may be easy to construct for simple problems for more complex composite tasks, such as the one considered in this paper, a suitable reward function is often non-obvious and may require considerable effort and experimentation. Secondly, and related to the previous point, the use of a shaping reward typically alters the solution to the optimization problem.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Composite shaping rewards", "weight": 1.0} -->

The effect of this can be benign but especially when it comes to complex tasks a small mistake may lead to complete failure of learning as we will demonstrate below. Thirdly, in a robotics setup not all information that would be desirable to define a good shaping reward may be easily available. For instance, in the manipulation problem considered in this paper determining the position of the Lego bricks requires extra instrumentation of the experimental setup.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Composite shaping rewards", "weight": 1.0} -->

In this section we propose and analyze several possible reward functions for our full Stack task, aiming to provide a recipe that can be applied to other tasks with similar compositional structure. Shaping rewards are typically defined based on some notion of distance from or progress towards a goal state. We attempt to transfer this idea to our compositional setup via, what we call, composite (shaping) rewards. These reward functions return an increasing reward as the agent completes components of the full task. They are either piecewise constant or smoothly varying across different regions of the state space that correspond to completed subtasks. In the case of Stack we use the reward components described in table I.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Composite shaping rewards", "weight": 1.0} -->

hypothetical pinch site position of the fingers is in a box around the first brick position

<!-- chunk {"id": "body-0033", "role": "body", "section": "Composite shaping rewards", "weight": 1.0} -->

the first brick is located at least 3cm above the table surface, which is only possible if the arm is holding the brick

<!-- chunk {"id": "body-0034", "role": "body", "section": "Composite shaping rewards", "weight": 1.0} -->

distance of the pinch site to the first brick - non-linear bounded

<!-- chunk {"id": "body-0035", "role": "body", "section": "Composite shaping rewards", "weight": 1.0} -->

while grasped: distance of the first brick to the stacking site of the second brick - non-linear bounded

<!-- chunk {"id": "body-0036", "role": "body", "section": "Composite shaping rewards", "weight": 1.0} -->

These reward components can be combined in different ways. We consider three different composite rewards in additional to the original sparse task reward:\
Grasp shaping: Grasp brick 1 and Stack brick 1, i.e. the agent receives a reward of 0.25 when the brick 1 has been grasped and a reward of 1.0 after completion of the full task.\
Reach and grasp shaping: Reach brick 1, Grasp brick 1 and Stack brick 1, i.e. the agent receives a reward of 0.125 when being close to brick 1, a reward of 0.25 when brick 1 has been grasped, and a reward of 1.0 after completion of the full task.\
Full composite shaping: the sparse reward components as before in combination with the distance-based smoothly varying components.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Composite shaping rewards", "weight": 1.0} -->

Although the above reward functions are specific to the particular task, we expect that the idea of a composite reward function can be applied to many other tasks thus allowing learning for to succeed even for challenging problems. Nevertheless, great care must be taken when defining the reward function. We encountered several unexpected failure cases while designing the reward function components: e.g. reach and grasp components leading to a grasp unsuitable for stacking, agent not stacking the bricks because it will stop receiving the grasping reward before it receives reward for stacking and the agent flips the brick because it gets a grasping reward calculated with the wrong reference point on the brick.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Learning from instructive states", "weight": 1.0} -->

In the previous section we have described a strategy for designing effective reward functions for complex compositional tasks which alleviate the burden of exploration. We have also pointed out, however, that designing shaping rewards can be error prone and may rely on privileged information. In this section we describe a different strategy for embedding prior knowledge into the training process and improving exploration that reduces the reliance on carefully designed reward functions.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Learning from instructive states", "weight": 1.0} -->

Specifically we propose to let the distribution of states at which the learning agent is initialized at the beginning of an episode reflect the compositional nature of the task: In our case, instead of initializing the agent always at the beginning of the full task with both bricks on the table we can, for instance, choose to initialize the agent occasionally with the brick already in its hand and thus prepared for stacking in the same way as when learning the subtask StackInHand in section V. Trajectories of policies solving the task will have to visit this region of space before stacking the bricks and we can thus think of this initialization strategy as initializing the agent closer to the goal.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Learning from instructive states", "weight": 1.0} -->

More generally, we can choose to initialize episodes with states taken from anywhere along or close to successful trajectories. Suitable states can be either manually defined (as in section V), or they can be obtained from a human demonstrator or a previously trained agent that can partially solve the task. This can be seen as a form of apprenticeship learning in which we provide teacher information by influencing the state visitation distribution.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Learning from instructive states", "weight": 1.0} -->

We perform experiments with two alternative methods for generating the starting states. The first one uses manually defined initial states and amounts to the possibility discussed above: we initialize the learning agent in either the original starting states with both bricks located on the table or in states where the first brick is already in the gripper as if the agent just performed a successful grasp and lifted the brick. These two sets of start states correspond to those used in section V.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Learning from instructive states", "weight": 1.0} -->

The second method for generating instructive starting states can also be used on a real robot provided a human demonstrator or a pre-trained policy are available. It aims at initializing the learning agent along solution trajectory states in a more fine-grained fashion. We sample a random number of steps for each episode between one and the expected number of steps required to solve the task from the original starting states and then run the demonstrator for this number of steps. The final state of this process is then used as a starting state initialization for the learning agent which then acts in the environment for the remainder of the episode.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Learning from instructive states", "weight": 1.0} -->

The results of these experiments are shown in Figure 5. It shows results for the four reward functions considered in the previous section when combined with the simple augmented start state distribution. While there is still no learning for the basic sparse reward case, results obtained with all other reward functions are improved. In particular, even for the second simplest reward function (Grasp shaping) we now obtain some controllers that can solve the full task. Learning with the full composite shaping reward is faster and more robust than without the use of instructive states.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Learning from instructive states", "weight": 1.0} -->

The top left plot of Figure 5 (red trace) shows results for the case where the episode is initialized anywhere along trajectories from a pre-trained controller. We use this start state distribution in combination with the basic sparse reward for the overall case (Stack without shaping). Episodes were configured to be 50 steps, shorter than in the previous experiments, to be better suited to this setup with assisted exploration. During testing we still used episodes with 150 steps as before (so the traces are comparable). We can see a large improvement in performance in comparison to the two-state method variant even in the absence of any shaping rewards. We can learn a robust policy for all seeds within a total of 1 million environment transitions. This corresponds to less than 1 hour of interaction time on 16 simulated robots.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Learning from instructive states", "weight": 1.0} -->

Overall these results suggest that an appropriate start state distribution does not only greatly speed up learning, it also allows simpler reward function to be used. In our final experiment the simplest reward function, only indicating overall experimental success, was sufficient to solve the task. Considering the difficulties that can be associated with designing good shaping rewards this is an encouraging results.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Learning from instructive states", "weight": 1.0} -->

The robustness of the policies that we can train to the starting state variation are also quite encouraging. Table II lists the success rate by task from 1000 trials. You can find a video with trained policies performing the Grasp, StackInHand and Stack tasks from different initial states in the supplementary material.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have introduced two extensions to the DDPG algorithm which make it a powerful method for learning robust policies for complex continuous control tasks. Specifically, we have shown that by decoupling the frequency of network updates from the environment interaction we can substantially improve data-efficiency, to a level that in some cases makes the difference between finding a solution or not. The asynchronous version of DDPG which allows data collection and network training to be distributed over several computers and (simulated) robots has provided us with a close to linear speed up in wall-clock time for 16 parallel workers.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In addition, we presented two methods that help to guide the learning process towards good solutions and thus reduce the pressure on exploration strategies and speed up learning. The first, composite rewards, is a recipe for constructing effective reward functions for tasks that consist of a sequence of sub-tasks. The second, instructive starting states, can be seen as a lightweight form of apprenticeship learning that facilitates learning of long horizon tasks even with sparse rewards, a property of many real-world problems. Taken together, the algorithmic changes and exploration shaping strategies have allowed us to learn robust policies for the Stack task within a number of transitions that is feasible to collect in a real-robot system within a few days, or in significantly less time if multiple robots were used for training.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusion", "weight": 1.5} -->

It is of course a challenge to judge the transfer of results in simulation to the real world. We have taken care to design a physically realistic simulation, and in initial experiments, which we have performed both in simulation and on the physical robot, we generally find a good correspondence of performance and learning speed between simulation and real world. This makes us optimistic that our performance numbers also hold when going to the real world. A second caveat of our simulated setup is that it currently uses information about the state of the environment, which although not impossible to obtain on a real robot, may require additional instrumentation of the experimental setup, e.g. to determine the position of the two bricks in the work space. To address this second issue we are currently focusing on end-to-end learning directly from raw visual information. Here, we have some first results showing the feasibility of learning policies for grasping with a success rate of about 80% across different starting conditions.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We view the algorithms and techniques presented here as an important step towards applying versatile deep reinforcement learning methods for real-robot dexterous manipulation with perception.
