<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning to Drive in a Day

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We demonstrate the first application of deep reinforcement learning to autonomous driving. From randomly initialised parameters, our model is able to learn a policy for lane following in a handful of training episodes using a single monocular image as input. We provide a general and easy to obtain reward: the distance travelled by the vehicle without the safety driver taking control. We use a continuous, model-free deep reinforcement learning algorithm, with all exploration and optimisation performed on-vehicle. This demonstrates a new framework for autonomous driving which moves away from reliance on defined logical rules, mapping, and direct supervision. We discuss the challenges and opportunities to scale this approach to a broader range of autonomous driving tasks.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous driving is a topic that has gathered a great deal of attention from both the research community and companies, due to its potential to radically change mobility and transport. Broadly, most approaches to date focus on formal logic which define driving behaviour in annotated 3D geometric maps. This can be difficult to scale, as it relies heavily on external mapping infrastructure rather than primarily using an understanding of the local scene.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In order to make autonomous driving a truly ubiquitous technology, we advocate for robotic systems which address the ability to drive and navigate in absence of maps and explicit rules, relying - just like humans - on a comprehensive understanding of the immediate environment while following simple higher level directions (e.g., turn-by-turn route commands). Recent work in this area has demonstrated that this is possible on rural country roads, using GPS for coarse localisation and LIDAR to understand the local scene.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the recent years, reinforcement learning (RL) -- a machine learning subfield focused on solving Markov Decision Problems (MDP) where an agent learns to select actions in an environment in an attempt to maximise some reward function -- has shown an ability to achieve super-human results at games such as Go or chess, a great deal of potential in simulated environments like computer games, and on simple tasks with robotic manipulators. We argue that the generality of reinforcement learning makes it a useful framework to apply to autonomous driving. Most importantly, it provides a corrective mechanism to improve learned autonomous driving behaviour.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We therefore present the first demonstration of a deep reinforcement learning agent driving a real car.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Mapping approaches", "weight": 1.0} -->

Since early examples, autonomous vehicle systems have been designed to navigate safely through complex environments using advanced sensing and control algorithms. These systems are traditionally composed of many specific independently engineered components, such as perception, state estimation, mapping, planning and control. However, because each component needs to be individually specified and tuned, this can be difficult to scale to more difficult driving scenarios due to complex interdependencies.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Mapping approaches", "weight": 1.0} -->

Significant effort has been focused on computer vision components for this modular approach. Localisation such as facilitates control of the vehicle within the mapped environment, while perception methods such as semantic segmentation enable the robot to interpret the scene. These modular tasks are supported by benchmarks such as and.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Mapping approaches", "weight": 1.0} -->

These modular mapping approaches are largely the focus of commercial efforts to develop autonomous driving systems; however, they present an incredibly complex systems engineering challenge, which has yet to be solved.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Imitation learning", "weight": 1.0} -->

A more recent approach to some driving tasks is imitation learning, which aims to learn a control policy by observing expert demonstrations. One important advantage of this approach is that it can use end-to-end deep learning, optimising all parameters of a model jointly with respect to an end goal thus reducing the effort of tuning of each component. However, imitation learning is also challenging to scale. It is impossible to obtain expert examples to imitate for every potential scenario an agent may encounter, and it is challenging to deal with distributions of demonstrated policies (e.g., driving in each lane).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Reinforcement learning", "weight": 1.0} -->

Reinforcement learning is a broad class of algorithms for solving Markov Decision Problems (MDPs).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Reinforcement learning", "weight": 1.0} -->

An MDP consists of: a set $\mathcal{S}$ of states, a set $\mathcal{A}$ of actions, a transition probability function $p:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathcal{P}{(\mathcal{S})}}}$, which to every pair ${(s,a)} \in {\mathcal{S} \times \mathcal{A}}$ assigns a probability distribution $p{(\cdot |s,a)}$ representing the probability of entering a state from state $s$ using action $a$, a reward function $R:{{\mathcal{S} \times \mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$, which describes the reward $R{(s_{t + 1},s_{t},a_{t})}$ associated with entering state $s_{t + 1}$ from state $s_{t}$ using action

<!-- chunk {"id": "body-0013", "role": "body", "section": "Reinforcement learning", "weight": 1.0} -->

$a_{t}$, a future discount factor $\gamma \in {\lbrack 0,1\rbrack}$ representing how much we care about future rewards.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Reinforcement learning", "weight": 1.0} -->

The solution of an MDP is a policy $\pi:{\mathcal{S}\rightarrow\mathcal{A}}$ that for every $s_{0} \in \mathcal{S}$ maximises: where the expectation is taken over states $s_{t + 1}$ sampled according to $p{(\left. s_{t + 1} \middle| {s_{t},{\pi{(s_{t})}}} \right.)}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Reinforcement learning", "weight": 1.0} -->

In our setting, we use a finite time horizon $T$ in place of infinity in the above formula. This is equivalent to one of the states being terminal, i.e. it cannot be escaped and any action at that state gives zero reward.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Reinforcement learning", "weight": 1.0} -->

Rearranging the above equation into a recurrent form, we get one of the two Bellman equations: Here the expectation is taken only over $s_{1}$ sampled according to $p{(\left. s_{1} \middle| {s_{0},{\pi{(s_{0})}}} \right.)}$. For reference, let us present the other Bellman equation: where $Q_{\pi}{(s_{0},a_{0})}$ is the expected cumulative discounted reward received while starting from state $s_{0}$ with action $a_{0}$ and following policy $\pi$ thereafter. Again the expectation is taken over $s_{1}$ sampled according to $p{(\left. s_{1} \middle| {s_{0},a_{0}} \right.)}$ In other words, reinforcement learning algorithms aim to learn a policy $\pi$ that obtains a high cumulative reward. They are generally split into two categories: model-based and model-free reinforcement learning.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Reinforcement learning", "weight": 1.0} -->

In the former approach, explicit models for the transition and reward functions are learnt, and then used to find a policy that maximises cumulative reward under those estimated functions. In the latter, we directly estimate the value $Q{(s,a)}$ of taking action $a$ in state $s$, and then follow a policy that selects the action with the highest estimated value in each state.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Reinforcement learning", "weight": 1.0} -->

Model-free reinforcement learning is extremely general. Using it, we can (in theory) learn any task we can imagine, whereas model-based algorithms can be only as good as the model learned. On the other hand, model-based methods tend to be more data-efficient than model-free ones. For further discussion, see.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Reinforcement learning", "weight": 1.0} -->

In autonomous driving, deep learning has been used to learn dynamics models for model-based reinforcement learning using off-line data. Reinforcement learning has also been used to learn autonomous driving agents in video games. However, this can simply the problem, with access to ground truth reward signals which are not available in the real-world, such as the angle of the car to the the lane.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Reinforcement learning", "weight": 1.0} -->

The closest work to this paper is from Riedmiller et al. who train a reinforcement learning agent which drives a vehicle to follow a GPS trajectory in an obstacle-free environment. They demonstrate learning on-board the vehicle using a dense reward function based on GPS thresholded tracking error. We build on this work in a number of ways; we demonstrate learning to drive with deep learning, from an image-based input, using a sparse reward function to lane follow.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Driving as a Markov Decision Process", "weight": 1.0} -->

A key focus of this paper is the set-up of driving as an MDP. Our goal is that of autonomous driving, and the exact definition of the state space $\mathcal{S}$, action space $\mathcal{A}$ and reward function $R$ are free for us to be defined. The transition model is implicitly fixed once a state and action representation is fixed, with the remaining degrees of freedom -- the transitions themselves -- dictated by the mechanics of the simulator/vehicle used.

<!-- chunk {"id": "body-0022", "role": "body", "section": "State space", "weight": 1.0} -->

Key to defining the state space is the definition of the observations $O_{t}$ that the algorithm receives at each time step. Many sensors have been developed in order to provide sophisticated observations for driving algorithms, not limited to LIDAR, IMUs, GPS units and IR depth sensors; an endless budget could be spent on advanced sensing technology. In this paper, we show that for simple driving tasks it is sufficient to use a monocular camera image, together with the observed vehicle speed and steering angle. Theoretically, state $s_{t}$ is to be a Markov representation of all previous observations. An approximation a fixed length approximately Markov state could be obtained, for example, using a Recurrent Neural Network to recursively combine observations. However, for the tasks we consider, the observation itself serves as a good enough approximation of the state.

<!-- chunk {"id": "body-0023", "role": "body", "section": "State space", "weight": 1.0} -->

A second consideration is how to treat the image itself: the raw image could be fed directly into the reinforcement learning algorithm through a series of convolutions; alternatively, a small compressed representation of the image, using, for example, a Variational Autoencoder (VAE), could be used. We compare the performance of reinforcement learning using these two approaches in Section IV. In our experiments, we train the VAE online from five purely random exploration episodes, using a KL loss and a L2 reconstruction loss.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Action space", "weight": 1.0} -->

Driving itself has what one might think are a natural set of actions: throttle, brake, signals etc. But what domain should the output of the reinforcement learning algorithm be? The throttle itself can be described as discrete, either on or off, or continuous, in a range isometric to. An alternative is to reparameterise the throttle in terms of a speed set-point, with throttle output by a classical controller in an attempt to match the set-point. Overall, experiments on a simple simulator (Section IV-A) showed that continuous actions, whilst somewhat harder to learn, provide for a smoother controller. We use a two-dimensional action space; steering angle in the range and speed setpoint in km/h.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Reward function", "weight": 1.0} -->

Design of reward functions can approach supervised learning -- given a lane classification system, a reward to learn lane-following can be set up in terms of minimising the predicted distance from centre of lane, the approach taken. This approach is limited in scale: the system can only be as good as the human intuition behind the hand-crafted reward. We do not take this approach. Instead, we define the reward as forward speed and terminate an episode upon an infraction of traffic rules -- thus the value of a given state $V{(s_{t})}$ corresponds to the average distance travelled before an infraction. A fault that may be identified is that the agent may choose to avoid more difficult manoeuvres, e.g. turning right in the UK (left in US). Command conditional rewards may be utilised in future work to avoid this.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Reinforcement Learning Algorithm -- Deep Deterministic Policy Gradients", "weight": 1.0} -->

We selected a simple continuous action domain model-free reinforcement learning algorithm: deep deterministic policy gradients (DDPG), to show that an off-the-shelf reinforcement learning algorithm with no task-specific adaptation is capable of solving the MDP posed in Section III-A.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Reinforcement Learning Algorithm -- Deep Deterministic Policy Gradients", "weight": 1.0} -->

DDPG consists of two function approximators: a critic $Q:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$, which estimates the value $Q{(s,a)}$ of the expected cumulative discounted reward upon using action $a$ in state $s$, trained to satisfy the Bellman equation under a policy given by the actor $\pi:{\mathcal{S}\rightarrow\mathcal{A}}$, which attempts to estimate a $Q$-optimal policy ${\pi{(s)}} = {{argmax}_{a}Q{(s,a)}}$; here $(s_{t},a_{t},r_{t + 1},d_{t + 1},s_{t + 1})$ is an experience tuple, a transition from state $s_{t}$ to $s_{t + 1}$ using action $a_{t}$ and receiving reward $r_{t + 1}$ and "done" flag

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Reinforcement Learning Algorithm -- Deep Deterministic Policy Gradients", "weight": 1.0} -->

$d_{t + 1}$, selected from a buffer of past experiences.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B Reinforcement Learning Algorithm -- Deep Deterministic Policy Gradients", "weight": 1.0} -->

The error in the Bellman equality, which the critic attempts to minimise, is termed the temporal difference ($TD$) error. Many variants of actor-critic methods exist, see e.g..

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B Reinforcement Learning Algorithm -- Deep Deterministic Policy Gradients", "weight": 1.0} -->

DDPG training is done online. Beyond the infrastructure of setting up such a buffer for use on a real vehicle (which requires it to be tolerant of missing/faulty episodes and any-time stoppable), reinforcement learning can be sped up by selecting the most "informative" examples from the replay buffer. We do so using a commonly established method called prioritised experience replay: we sample experience tuples with probability proportional to the $TD$ error made by the critic. The weights used for this sampling are updated upon each optimisation step with minimal overhead; new samples are given infinite weight to ensure all samples are seen at least once.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B Reinforcement Learning Algorithm -- Deep Deterministic Policy Gradients", "weight": 1.0} -->

DDPG is an off-policy learning algorithm, meaning that actions performed during training come from a policy distinct from the learn optimal policy by the actor. This happens in order to gain diverse state-action data outside of the narrow distribution that would be seen by the optimal policy, and thus increase robustness. We use a standard method of achieving this in the context of continuous reinforcement learning methods: our exploration policy is formed by adding discrete Ornstein-Uhlenbeck process noise to the optimal policy. Therefore, at each step we add to optimal actions noise $x_{t}$ given: where $\theta,\mu,\sigma$ are hyperparameters and ${\{\epsilon_{t}\}}_{t}$ are i.i.d. random variables sampled from the normal distribution $N{}$. These parameters need to be tuned carefully, as there is a direct trade-off between noise utility and comfort of the safety driver. Strongly mean reverting noise with lower variance is easier to anticipate, whilst higher variance noise provides better state-action space coverage.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B Reinforcement Learning Algorithm -- Deep Deterministic Policy Gradients", "weight": 1.0} -->

3: Waiting for environment reset 4: if task is train then 5: Run episode with noisy policy 6: if exploration time is over then 9: else if task is test then 10: Run episode with optimal policy 11: else if task is undo then 12: Revert previous train/test task 13: else if task is done then (a) Task-based workflow for on-vehicle training (b) Policy execution architecture, used to run episodes during model training or testing.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-C Task-based Training Architecture", "weight": 1.0} -->

Deployment of a reinforcement learning algorithm on a full-sized robotic vehicle running in a real world environment requires adjustment of common training procedures, to account for both driver intervention and external variables affecting the training.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-C Task-based Training Architecture", "weight": 1.0} -->

We structure the architecture of the algorithm as a simple state machine, outlined in Figure 2(a), in which the safety driver is in control of the different tasks. We define four tasks: train, test, undo and done. The definition of these tasks allows the system to be both interactive and stateful, favouring an on-demand execution of episodes instead of an a priori fixed schedule.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-C Task-based Training Architecture", "weight": 1.0} -->

The train and test tasks allow us to interact with the vehicle in autonomous mode, executing the current policy. The difference between the two tasks consists in noise being added to the model output and the model being optimised in training tasks, whereas test tasks run directly the model output actions. During early episodes, we skip optimisation to favour exploration of the state space. We continue the experiment until the test reward stops increasing.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-C Task-based Training Architecture", "weight": 1.0} -->

Each episode is executed until the system detects that automation is lost (i.e. the driver intervened). In a real world environment, the system can not reset automatically between episodes, unlike agents in simulation or in a constrained environment. We require a human driver to reset the vehicle to a valid starting state. Upon episode termination, while the safety driver performs this reset, the model is being optimised, minimising the time spent between episodes.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-C Task-based Training Architecture", "weight": 1.0} -->

The undo and done tasks depict the key differences in the architecture. The system may terminate an episode for a variety of valid reasons other than failing to drive correctly: these episodes can not be considered for the purposes of training. The undo task is introduced for this reason, as it allows us to undo the episode and restore the model as it was before running that episode. A common example in our experiments is encountering other drivers seeking to use the road being used as the environment. The done task allows us to gracefully exit the experiment at any given moment, and is helpful since the procedure is interactive and it doesn't run for a fixed number of episodes.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments", "weight": 1.0} -->

The main task we use to showcase the vehicle is that of lane-following; this is the same task as addressed, however done on a real vehicle as well as on simulation, and done from image input, without knowledge of lane position. It is a task core to driving, and was the cornerstone of the seminal ALVINN. We first accomplish this task in simulation in Section IV-A, and then use these results and knowledge of appropriate hyperparameters to demonstrate a solution on a real vehicle in Section IV-B.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments", "weight": 1.0} -->

For both simulation and real-world experiments we use a small convolutional neural network. Our model has four convolutional layers, with $3 \times 3$ kernels, stride of 2 and 16 feature dimensions, shared between the actor and critic models. We then flatten the encoded state and concatenate the vector the scalar state for the actor, additionally concatenating the actions for the critic network. For both networks we then apply one fully-connected layer with feature size 8 before regressing to the output. For the VAE experiments, a decoder of the same size as the encoder is used, replacing strided convolution with transposed convolution to upsample the features. A graphical depiction is shown in Figure 1.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-A Simulation", "weight": 1.0} -->

To test reinforcement learning algorithms in the context of lane following from image inputs we developed a 3D driving simulator, using Unreal Engine 4. It contains a generative model for country roads, supports varied weather conditions and road textures, and will in the future support more complex environments (see Figure 3 for game screenshots).

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-A Simulation", "weight": 1.0} -->

The simulator proved essential for tuning reinforcement learning parameters including: learning rates, number of gradient steps to take following each training episode and the correct termination procedure -- conservative termination leads to a better policy. It confirmed a continuous action space is preferable -- discrete led to a jerky policy -- and that DDPG is a suitable reinforcement learning algorithm. As described in the environment setup in Section III-A, reward granted in the simulator corresponded to the distance travelled before exiting lane, with new episodes resetting the car to the centre of the lane.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-A Simulation", "weight": 1.0} -->

We found that we could reliably learn to learn follow in simulation from raw images within 10 training episodes. Furthermore, we found little advantage to using a compressed state representation (provided by a Variational Autoencoder). We found the following hyperparameters to be most effective, which we use for our real world experiments: future discount factor of 0.9, noise half-life of 250 episodes, noise parameters of $\theta$ of 0.6 and $\sigma$ of 0.4, 250 optimisation steps between episodes with batch size 64 and gradient clipping of 0.005.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-B Real-world driving", "weight": 1.0} -->

Our real world driving experiments mimic in many ways those conducted in simulation. However, executing this experiment in the real world is significantly more challenging. Many environmental factors cannot be controlled, and real-time safety and control systems must be implemented. For these experiments, we use a 250 meter section of road. The car begins at the start of the road to commence training episodes. When the car deviates from the lane and enters an unrecoverable position, the safety driver takes control of the vehicle ending the episode. The vehicle is then returned to the center of the lane to begin the next episode. We use the same hyperparameters that we found to be effective in simulation, with the noise model adjusted to give vehicle behaviour similar to that in simulation under the dynamics of the vehicle itself.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-B Real-world driving", "weight": 1.0} -->

We conduct our experiments using a modified Renault Twizy vehicle, which is a two seater electric vehicle, shown in Figure 1. The vehicle weighs 500kg, has a top speed of 80 km/h and has a range of 100km on a single battery charge. We use a single monocular forward-facing video camera mounted in the centre of the roof at the front of the vehicle. We use retrofitted electric motors to actuate the brake and steering, and electronically emulate the throttle position to regulate torque to the wheels. All computation is done on-board using a single NVIDIA Drive PX2 computer. The vehicle's drive-by-wire automation automatically disengages if the safety driver intervenes, either by using vehicle controls (brake, throttle, or steering), toggling the automation mode, or pressing the emergency stop. An episode would terminate when either speed exceeded 10km/h, or drive-by-wire automation disengaged, indicating the safety driver has intervened. The safety driver would then reset the car to the centre of the road and continue with the next episode.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Disengagements", "weight": 1.0} -->

Deep RL from Pixels Deep RL from VAE TABLE I: Deep reinforcement learning results on an autonomous vehicle over a 250m length of road. We report the best performance for each model. We observe the baseline RL agent can learn to lane follow from scratch, while the VAE variant is much more efficient, learning to succesfully drive the route after only 11 training episodes.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Disengagements", "weight": 1.0} -->

Table I shows the results of these experiments. Here, the major finding is that reinforcement learning can solve this problem in a handful of trials. Using 250 optimisation steps with batch size 64 took approximately 25 seconds, which made the experiment extremely manageable, considering manoeuvring the car to the centre of the lane to commence the next episode takes approximately 10 seconds anyway. We also observe in the real world, where the visual complexity is much more difficult than simulation, a compressed state representation provided by a Variational Autoencoder trained online together with the policy greatly improved reliability of the algorithm. We compare our method to a zero policy (driving straight with constant speed) and random exploration noise, in order to confirm that the trial indeed required a non-trivial policy. ^11^1A video of the training process for our vehicle learning to drive the 250m length of private road with the stateful RL training architecture (Section III-C) is available at

<!-- chunk {"id": "body-0047", "role": "body", "section": "Discussion", "weight": 1.5} -->

This work presents the first application of deep reinforcement learning to a full sized autonomous vehicle. The experiments demonstrate we are able to learn to lane follow with under thirty minutes of training -- all done on on-board computers.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Discussion", "weight": 1.5} -->

In order to tune hyperparameters, we built a simple simulated driving environment where we experimented with reinforcement learning algorithms, maximising distance before a traffic infraction using DDPG as a canonical algorithm. The parameters found transferred amicably to the real-world, where we rapidly trained a policy to drive a real vehicle on a private road, with a reward signal consisting only of speed and termination upon control driver taking control. Notably, this reward requires no further information or maps of the environment. With more data, vehicles and larger models, this framework is general enough to scale to more complex driving tasks.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Discussion", "weight": 1.5} -->

Whilst viable, this approach will require translation of reinforcement learning research advancements, as well as work on core reinforcement learning algorithms if it is to become a leading approach for scaling autonomous driving. We conclude by discussing our thoughts on the future work required.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this work, we present a general reward function which asks the agent to maximise the distance travelled without intervention from a safety driver. While this reward function is general, it has a number of limitations. It does not consider conditioning on a given navigation goal. Furthermore, it is incredibly sparse. As our agent improves, interventions will become significantly less frequent, resulting in weaker training signal. It is likely that further work is required to design a more effective reward function to learn a super-human driving agent. This will involve the careful consideration of many safety and ethical issues.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Discussion", "weight": 1.5} -->

The second area for development suggested by the results here is a better state representation. Our experiments have shown that a simple Variational Autoencoder greatly improves the performance of DDPG in the context of driving a real vehicle. Beyond pixel-space autoencoders is a wealth of computer vision research addressing effective compression of images: here existing work in areas such as semantic segmentation, depth, egomotion and pixel-flow provide an excellent prior for what is important in driving scenes. This research needs to be integrated with reinforcement learning approaches for real tasks, both model-free and model-based.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Discussion", "weight": 1.5} -->

However, unsupervised state encoding alone will likely not be sufficient. In order to compress the state in a manner that makes it simple to learn a policy with just a small number of samples, information on which elements of the state (image observation) are important is required. This information should come from the reward and terminal signals. Reward and terminal information can be incorporated in an encoding in many ways, but one difficulty always prevails: credit allocation. Rewards obtained at a specific time step may be related to observations received many time-steps in the past. Thus good models used for this application will contain a temporal component.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Discussion", "weight": 1.5} -->

Two areas that could greatly improve the availability of data for the application of reinforcement learning to real autonomous driving are semi-supervised learning and domain transfer. Whilst only a small portion of driving data might have rewards and terminals associated with it, as those are costly to obtain, the image embeddings -- and perhaps other aspects of models -- could benefit from driving data captured from dashcams in every-day vehicles. These could be used to pre-train the image autoencoder. In the context of a model-based RL system, these could also be used to approximate state transition functions, whilst advances in semi-supervised learning might allow us to utilise this data without reward/terminal labels data. Domain transfer, on the other hand, may allow us to create simulations sufficiently convincing that data from these may be used to train a policy that can be transferred directly onto a real car.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Discussion", "weight": 1.5} -->

The algorithm used here is intentionally a common canonical approach, chosen to demonstrate the ease with which reinforcement learning may be applied to driving. Many improvements to it have been developed in the wider literature, including the use of natural gradients. Other research has looked at better transformation of observations into states, typically using an RNN, as well as methods to perform multi-step planning, as. It is no question that these could provide superior performance.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Discussion", "weight": 1.5} -->

New advances in model-based reinforcement provide alternative exciting avenues for autonomous driving research, with work such as showing outstanding performance of models when observing directly the state of a physical system. This could offer significant benefits to an image-based domain. Alternative model-based approaches include which learn to simulate episodes and learn in imagination.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Discussion", "weight": 1.5} -->

We hope this paper inspires more research into applying reinforcement learning research to autonomous driving, perhaps combining it with elements from other machine learning techniques such as imitation learning and control theory. The method here solved a simple driving task in half an hour -- what more could be done in a day?
