<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Gentle Object Manipulation with Curiosity-Driven Deep Reinforcement Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Robots must know how to be gentle when they need to interact with fragile objects, or when the robot itself is prone to wear and tear. We propose an approach that enables deep reinforcement learning to train policies that are gentle, both during exploration and task execution. In a reward-based learning environment, a natural approach involves augmenting the (task) reward with a penalty for non-gentleness, which can be defined as excessive impact force. However, augmenting with only this penalty impairs learning: policies get stuck in a local optimum which avoids all contact with the environment. Prior research has shown that combining auxiliary tasks or intrinsic rewards can be beneficial for stabilizing and accelerating learning in sparse-reward domains, and indeed we find that introducing a surprise-based intrinsic reward does avoid the no-contact failure case. However, we show that a simple dynamics-based surprise is not as effective as penalty-based surprise. Penalty-based surprise, based on predicting forceful contacts, has a further benefit: it encourages exploration which is contact-rich yet gentle. We demonstrate the effectiveness of the approach using a complex, tendon-powered robot hand with tactile sensors. Videos are available at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep reinforcement learning (RL) can be used to train policies that achieve superhuman performance on Atari games and Go, learn locomotion tasks, and perform complex robotic manipulation skills. However, deploying deep RL on real-world robots often leads to a considerable amount of wear and tear over time, on both the robot itself and the environment, because existing approaches require many trials to learn and often rely on simple stochastic exploration. If robots were able to explore and learn safely, minimizing excessive forces and impacts, they would last longer before needing repairs, and the objects they interact with would not need to be replaced as often.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, destructive or risky behaviors by robots trained with RL go beyond the exploration phase. Agents trained solely to maximize a reward signal will often converge on policies which are high velocity and thus high impact, resulting in so-called "bang-bang control," which may be optimal in terms of returns, but is potentially damaging or dangerous to the robot and the environment. As a further motivation, we might care about gentleness in terms of task execution itself, for instance if the robot needs to pick-and-place an object, but either the object and/or goal location is fragile. In particular, when robot manipulation involves humans (e.g., feeding a patient), being gentle is important. In these situations, we would like robots to accomplish the given task in a reasonable amount of time, while minimizing applied force and impact as much as possible.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Thus, in order to broadly deploy deep RL on real robots, we need an approach for training policies that are gentle, both during exploration and task execution. A naïve approach is to constrain the maximum torques that a robot's motors can exert. However, many manipulation tasks require occasional, momentary, or variable high force (e.g., hammering a nail or turning a lever); the torque limit cannot be any lower than this, otherwise the robot will not be able to complete the task. But we do not want the robot to freely exert this much force along its entire trajectory. Alternatively, one could constrain the total amount of force or impact allowed, but this requires knowing *a priori* the minimum total amount necessary for accomplishing the task.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Instead, our approach is to give the robot negative rewards for actions that are not gentle, for instance those that result in high impact forces. Incorporating this in the reward function is a natural approach for encoding preferences about *how* robots should perform a task (e.g., driving style ), and can be seen as an intrinsic "pain" signal that encourages learning safer policies. However, perhaps unsurprisingly, adding this penalty often makes it much harder for an agent to learn a successful policy; instead, it gets stuck in a local optimum of avoiding contact altogether, because it encounters the penalties before ever obtaining the task reward, and thus learns a policy that is dominated by aversion to pain.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To motivate agents to interact with the environment *and* do it gently, we propose balancing this "pain" signal by adding another intrinsic signal, this one positive, for curiosity. In particular, we reward the agent for *surprising* experiences---those that contradict the agent's current understanding of the world. A concrete example of this is giving intrinsic rewards for transitions that have low probability under a learned dynamics model. However, we find that using this kind of *dynamics-based surprise* is not as effective as using a *penalty-based surprise*, that leads robots to be explicitly curious about the non-gentleness penalty itself. In this formulation, the agent makes predictions about the pain penalty that will result from a given state and action, and erroneous predictions deliver a small positive reward.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although this curiosity about pain may seem somewhat counterintuitive, it has been shown that humans are specifically curious about painful or unpleasant experiences; moreover, it is well known that children engage in physical risk-seeking behavior. This is also observed in other species in the form of play fighting, and seems to have an evolutionary benefit. Research in developmental psychology suggests that risky play is essential to the development of children, by allowing them to test their physical limits, improve hand-eye coordination, and learn to avoid or adapt in dangerous environments.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by this specialized form of curiosity, our work takes a step toward using deep RL to train policies for gentle, object- and contact-centric manipulation. In this work, gentleness is defined as minimizing impact forces. We demonstrate that our proposed approach, which introduces both a penalty for excessive impact forces and a curiosity reward focused on this penalty, enables efficient and safe exploration, precise task execution, and successful manipulation of fragile objects.

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-A Markov Decision Process", "weight": 1.0} -->

A Markov Decision Process (MDP) is defined as a tuple $(\mathcal{S},\mathcal{A},\mathcal{P},\mathcal{R},\gamma)$, where $\mathcal{S}$ is the state space, $\mathcal{A}$ is the action space, $\mathcal{P}:{{S \times A \times S}\mapsto{\mathbb{R}}}$ specifies the transition probabilities, $\mathcal{R}:{{S \times A \times S}\mapsto{\mathbb{R}}}$ specifies the reward function, and $\gamma \in {\lbrack 0,1\rbrack}$ is the discount factor.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-A Markov Decision Process", "weight": 1.0} -->

A policy $\pi$ is a function that maps each state to a distribution over actions ($\pi:{\mathcal{S}\rightarrow\Delta_{\mathcal{A}}}$, where $\Delta_{\mathcal{A}}$ is the probability simplex on $\mathcal{A}$). Reinforcement learning optimizes policies to maximize expected returns (i.e.,

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A Markov Decision Process", "weight": 1.0} -->

Typically $\mathcal{R}$ specifies how well the policy is doing in terms of accomplishing a task. In this work, we augment $\mathcal{R}$ with several types of auxiliary rewards, in order to train policies for contract-centric, low-impact manipulation.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-B Deep Reinforcement Learning", "weight": 1.0} -->

The policy $\pi$ can be represented by a function parameterized by $\theta$; for instance, $\theta$ may be a weighting on predefined features of the state. In deep RL, $\theta$ is the parameterization of a neural network. We use Distributed Distributional Deterministic Policy Gradients (D4PG) to train our policies, but in principle our proposed approach is algorithm-agnostic.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-B Deep Reinforcement Learning", "weight": 1.0} -->

D4PG is an actor-critic algorithm used to train policies for continuous control, where both the actor and critic are parameterized by neural networks. The critic is a distributional action-value function: it takes the current state $s_{t}$ and action $a_{t}$ as input, and outputs a categorical distribution over the predicted $Q{(s_{t},a_{t})}$. It is trained with off-policy evaluation, on batches of transitions $(s_{t},a_{t},s_{t + 1})$ sampled from a replay buffer. The actor is a deterministic policy: it takes in the current state $s_{t}$ as input, and outputs an action $a_{t}$. During training, the actor's policy is updated using gradients that are computed only with respect to the critic, such that actions are adjusted in the direction of increased Q-values.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-C Formalizing gentleness", "weight": 1.0} -->

In this work, we define being gentle as minimizing impact. This is closely related to the notion of impact force in physics, which is the maximum amount of force experienced during a collision. However, we consider a more general definition of "impact," that does not only apply to cases when the initial applied force is zero. Instead, assuming a discrete time step, we define impact $m_{t}$ as

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-C Formalizing gentleness", "weight": 1.0} -->

where $f_{t}$ is the sensed force at time step $t$. In other words, for a robot to be gentle, it should minimize *increases in sensed force*. To illustrate, consider a robot that needs to push a heavy object with a force of 20N. If the robot increases the applied force from zero to 20N in a fraction of a second, the action is more likely to cause damage compared to amortizing the increase in force over several seconds.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Proposed Approach", "weight": 1.0} -->

In order to train policies that exhibit gentle manipulation, we propose to augment the original reward ($r_{t}$) with an impact force penalty ($r_{t}^{f}$) and an intrinsic reward based on surprise ($r_{t}^{s}$). Agents are trained to maximize the total expected return,

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-A Impact penalty", "weight": 1.0} -->

The impact force penalty acts as an intrinsic pain signal to encourage agents to accomplish manipulation tasks in a more gentle way. Of course, in order to accomplish any manipulation task, small impacts are necessary---at some point the robot needs to go from zero to non-zero applied force on an object, in order to manipulate it. So, the impact penalty should scale non-linearly with the level of impact, by taking into account the *acceptability* of a particular amount of impact.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Impact penalty", "weight": 1.0} -->

Let ${a_{\lambda}{(m)}} \in {\lbrack 0,1\rbrack}$, parametrized by $\lambda$, be the acceptability of an amount of impact $m$. This is a monotonically increasing function, that should be designed according to how resilient the robot and environment are to impacts. For instance, if the robot is interacting with very fragile objects, then the range of acceptable impacts should be smaller. Ideally, this function should express the probability of damage (to either robot or environment) from a given amount of impact, and could be learned from experience of actual damage.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A Impact penalty", "weight": 1.0} -->

where the sum is over force sensors at different locations on the robot (e.g., the fingers of a robot hand). In our experiments, we set $\lambda = {\lbrack 2,2\rbrack}^{\top}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-A Impact penalty", "weight": 1.0} -->

However, if the environment reward merely combines the task reward and the impact penalty, that is, $r_{t}^{\prime} = {r_{t} + r_{t}^{f}}$, we find that policies get reliably stuck in a local optimum of not making contact with anything in the environment---the agent learns to be afraid of contact, since it encounters the impact penalty before the sparse task reward, hindering exploration.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B Dynamics-based surprise", "weight": 1.0} -->

The purpose of adding surprise-based intrinsic rewards is to encourage policies to make *contact* with objects in the environment but still in a *gentle* way. For an agent to be "surprised," it must have some predictor of future states, i.e., a model. In the case of dynamics-based surprise, this model is a learned dynamics model that takes in the current state and action, and predicts the mean and variance of the next state. We train an ensemble of neural networks for the dynamics model, in order to have predictive uncertainty. Predictive uncertainty is useful for capturing novelty: in the case of environments with deterministic dynamics, if the networks in the ensemble either individually have high variance in their predictions, or have high variance across the ensemble, then this indicates a novel area that should be explored further.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B Dynamics-based surprise", "weight": 1.0} -->

Each of the $M$ networks in the ensemble outputs the mean and variance of a Gaussian for each dimension $d$ of the prediction.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Dynamics-based surprise", "weight": 1.0} -->

where $\mathbf{x}$ denotes the input and $\theta_{i}$ are the parameters of the $i$th network in the ensemble. During training, each network is randomly initialized, and they are trained on different batches of transitions. We choose $M = 5$, as recommended by related work.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B Dynamics-based surprise", "weight": 1.0} -->

To compute dynamics-based surprise intrinsic reward $r_{t}^{s}$, we approximate the dynamics model's predicted distribution over next states with a single Gaussian per output dimension $d$, to measure how much variance there is *across* networks in the ensemble. The mean and variance of this is

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B Dynamics-based surprise", "weight": 1.0} -->

This intrinsic reward is computed with respect to a target dynamics model, which is updated every 5000 iterations; this makes training more stable, so that the agent is not trying to surprise a model that is constantly changing. In addition, we wait for the dynamics model to become more accurate before providing intrinsic rewards to the agent: after 20,000 training steps for experiments in simulation, and after 8,000 training steps on the real robot.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-C Penalty-based surprise", "weight": 1.0} -->

Motivated by the role of risk-seeking behavior in childhood learning, we propose to reward the agent for being curious about the impact penalty itself. In other words, we add a reward to focus the learning and exploration of the agent on the intrinsic pain signal, with two motivations: to enable better prediction of pain, and to encourage contacts by mitigating some of the penalty. To compute the penalty-based surprise reward $r_{t}^{s_{p}}$, we train an impact penalty predictor in parallel with the agent, with the same implementation as the general dynamics model (an ensemble of five neural networks).

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-C Penalty-based surprise", "weight": 1.0} -->

To compute the intrinsic reward, we do not use the negative log-likelihood directly, as was done with the dynamics reward, because it would make high impact forces acceptable as long as the prediction likelihood in those areas was low enough, leading to very non-gentle actions by the agent. Rather, we would like agents to focus on learning about areas with low penalty (i.e., areas where impacts occur but are small), so that they learn how to be gentle. For areas of high penalty, it is enough for the agent to just know that the penalty is high, not necessarily *exactly* how high it is.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-C Penalty-based surprise", "weight": 1.0} -->

where ${a_{\lambda^{\prime}}{(r_{t}^{f})}} \in {\lbrack 0,1\rbrack}$ is the acceptability of a particular penalty $r_{t}^{f}$. This is a monotonically increasing function, that should be chosen based on how much penalty the robot may experience for the sake of exploration or task completion. We use a sigmoid function for this acceptability, as we did for impact $a_{\lambda}{(m)}$ (Sec. IV-A).

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-C Penalty-based surprise", "weight": 1.0} -->

Note that $\lambda$ and $\lambda^{\prime}$ play different roles: $\lambda$ modulates the mapping of impact forces to pain penalties, whereas $\lambda^{\prime}$ controls the trade-off between these pain penalties and the agent's penalty-focused curiosity. The choice of $\lambda^{\prime}$ may be adjusted dynamically during learning; the higher $\lambda_{2}^{\prime}$ is, the easier it is for the robot to learn the task, at the cost of higher impact forces on average.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-C Penalty-based surprise", "weight": 1.0} -->

In order to augment the reward with this convex combination, we need to choose $r_{t}^{s_{p}}$ such that $r_{t}^{s_{p}} + r_{t}^{f}$ is equal to. In addition, we only provide this intrinsic reward if the penalty is non-zero, because the purpose is to encourage the agent to (cautiously) learn more about the penalty.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-C Penalty-based surprise", "weight": 1.0} -->

In the same way as dynamics-based surprise, this penalty-based surprise intrinsic reward is computed with respect to a target impact penalty predictor model, which is updated every 1000 iterations, and we do not provide intrinsic rewards to the agent until after 20,000 training steps for simulation experiments, and after 8,000 training steps for real robot experiments.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-D Agent architecture and implementation details", "weight": 1.0} -->

As mentioned, we use D4PG to train an actor (e.g., policy) and critic (e.g., action-value function). We use a separate critic for each of the reward components: the task reward critic encodes ${\hat{Q}}^{t}{(s_{t},a_{t})}$, the penalty-based surprise critic encodes ${\hat{Q}}^{s_{p}}{(s_{t},a_{t})}$, the dynamics-based surprise critic encodes ${\hat{Q}}^{s}{(s_{t},a_{t})}$, and the impact penalty critic encodes ${\hat{Q}}^{f}{(s_{t},a_{t})}$. The separation of the critics supports more stable learning. The components of the agent with penalty-based surprise are illustrated in Figure 1.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-D Agent architecture and implementation details", "weight": 1.0} -->

The output of the actor is passed through a tanh, so that it is between -1 and +1. This output specifies delta position: it is added to the current position and then clipped based on the minimum and maximum joint angle per action dimension, to obtain the action. The actor network consists of two fully-connected layers of 300 and 200 hidden units each. Each of the critic networks consists of two fully-connected layers of 400 and 300 hidden units each. The distributional output of the critic has support $({- 100},100)$ and 101 bins. For both the actor and critic networks, the first hidden layer is followed by layer normalization and a tanh, and all other hidden layers are followed by exponential linear unit (ELU) activations. For D4PG, we used a batch size of 256 and a replay buffer of 1 million transitions.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-D Agent architecture and implementation details", "weight": 1.0} -->

The dynamics model consists of three ensembles, one each for predicting the three types of state features: joint position, joint velocity, and touch. The non-gentleness predictor model consists of a single ensemble. Each of these ensembles consists of five neural networks, with three fully-connected layers of 128 hidden units each. All hidden layers are followed by rectified linear unit (ReLU) activations.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

Our goal is to learn policies that are safer, with less forceful impacts, while also improving sample efficiency and overall task performance.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

an impact penalty and a dynamics-based surprise intrinsic reward ($r_{t}^{f} + r_{t}^{s}$)

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments", "weight": 1.0} -->

an impact penalty and a penalty-based surprise intrinsic reward ($r_{t}^{f} + r_{t}^{s_{p}}$).

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-A Experimental domain", "weight": 1.0} -->

We run experiments both in simulation with MuJoCo and on a physical robot. The robot platform we use is the Shadow Dexterous Hand, with five fingers and a total of 24 degrees of freedom, actuated by 20 motors. We use this platform for several reasons: because it is actuated by antagonistic tendons, it is more susceptible to wear-and-tear (and thus gentle exploration and manipulation has greater potential benefit); it can be equipped with high-fidelity tactile sensors; and it is anthropomorphic and well suited for handling fragile objects.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-A Experimental domain", "weight": 1.0} -->

In simulation, each fingertip has a spatial touch sensor attached, with three channels and a spatial resolution of $4 \times 4$: one for normal force and two for tangential forces. We simplify this by taking the absolute value and then summing across the spatial dimensions, to obtain a 3D force vector for each fingertip. The impact force $m_{t}^{i}$ is then the sum over the increase in force per channel for fingertip $i$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-A Experimental domain", "weight": 1.0} -->

On our real-world Shadow Hand, BioTac® sensors provide a more complex array of tactile signals. To compute the forces exerted by each finger, readings from the pressure channel of each tactile sensor were acquired and then normalized to match the range of the simulated tactile sensors. In this way, it was possible to directly compare results in simulation and on the real robot, without having to change the parameters of the task or learning algorithm.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-A Experimental domain", "weight": 1.0} -->

The state consists of proprioception (joint position and joint velocity) and touch. The action space is 20-dimensional. We use position control and a control rate of 20 Hz, both in simulation and on the physical robot.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-A Experimental domain", "weight": 1.0} -->

The environment consists of the Shadow Hand and a single block (Fig. 2, Fig. 7); the task reward $r_{t}$ depends on the experiment. Focusing on this simple environment enables us to clearly characterize the effectiveness of our three approaches for training low-impact policies. We find that even in this simple environment, learning policies for gentle manipulation is challenging for most approaches. Results from the simulated environment are presented first.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-B Exploration with impact penalty", "weight": 1.0} -->

First, we are interested in whether these approaches enable training policies that are gentle during exploration. We investigate this in a no-reward setting, where the policy receives intrinsic rewards (either from dynamics-based surprise or penalty-based surprise) and the intrinsic pain penalty, but no task reward. The goal is for policies to be gentle (i.e., experience low impact) while still exploring effectively, in terms of interacting with objects in the environment.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-B Exploration with impact penalty", "weight": 1.0} -->

As a baseline, we trained policies with only dynamics-based surprise intrinsic rewards, without an impact penalty. As expected, these policies experience a large amount of impact while exploring: the maximum amount of impact experienced per rollout is in the 5 to 15N range (Fig. 3, left). This suggests that this form of curiosity is not practical for running on real-world robots, if either the robot or the objects it interacts with are susceptible to wear and tear.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-B Exploration with impact penalty", "weight": 1.0} -->

When we add the impact penalty, we do observe more gentle exploration: there is a significant decrease in the maximum amount of impact experienced per rollout (now in the 0 to 5N range), for both kinds of intrinsic reward. However, having penalty-based surprise intrinsic rewards leads to more gentle touching, whereas dynamics-based surprise leads to the policy exploring interesting configurations of the hand, but with limited touching (Fig. 3, center and right).

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-C Manipulation with impact penalty", "weight": 1.0} -->

Next, we are interested in whether these approaches enable training policies that learn how to perform a task gently, while still being relatively sample-efficient. In the task, the episode terminates with a reward of +1 if the hand presses the block with any fingerpad (thus activating the touch sensor) with a force greater than 5N. A non-gentle way of achieving this is to go from no contact to 5N of applied force in a single timestep; in contrast, policies trained to be gentle should more gradually increase to 5N of applied force.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-C Manipulation with impact penalty", "weight": 1.0} -->

This task is simple: without an impact penalty, agents learn this task quickly (Fig. 4, top), although with a significant amount of impact (Fig. 2, top center). However, once impact penalties are added, if there is no form of surprise-based intrinsic rewards to counteract them, then agents fail to learn the task---they get trapped in a local optimum of avoiding contact with the environment, since they experience penalties from contact before discovering how to perform the task (Fig. 2, center).

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-C Manipulation with impact penalty", "weight": 1.0} -->

In line with the results from our previous experiment, in which we observed that dynamics-based surprise leads to only limited gentle touching in the presence of impact penalties, we saw that penalty-based surprise was much more effective in terms of agents learning how to perform the task gently, with low impacts (Fig. 5). Even more, these agents learned as quickly as ones trained without the impact penalty (Fig. 4, top). This may be because this task is particularly contact-focused (in general manipulation tasks are contact-focused, but to varying degrees), so it is a setting in which contact-focused exploration is especially helpful. We also compare our approach with agents trained using the Intrinsic Curiosity Module (ICM) proposed. Similarly to the agents trained with dynamics-based surprise, these agents do not successfully learn the task.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-D Manipulation of fragile objects", "weight": 1.0} -->

Finally, we made the task more difficult by introducing a 'fragile block'. This is analogous to a manipulation task involving fragile objects, such as picking ripe fruit or assisting humans. This fragile block 'breaks' if the impact force at any point is greater than 3N, and the episode terminates with a negative reward of -0.5. The reward for completing the task is +5. Now, policies trained with only the task reward are unable to learn the task at all, because they accidentally break the block a few times, and learn that any contact with the block is undesirable. There is no reward shaping that incentivizes these policies to try interacting with the block in a gentle way.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-D Manipulation of fragile objects", "weight": 1.0} -->

In contrast, policies trained with the impact penalty are better able to learn the task. As before, penalty-based surprise intrinsic rewards are more effective than dynamics-based ones in terms of how quickly policies are able to learn the task (Fig. 4, bottom).

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-D Manipulation of fragile objects", "weight": 1.0} -->

Fig. 6 plots the evolution of reward components over time obtained by the agent trained on task reward, impact penalty and penalty-based surprise intrinsic reward. Each reward component in this plot is the average over batches sampled from the agent's replay buffer. The total reward (blue) is the combination of the pain surprise reward, the task reward, and the pain penalty. The dashed vertical line indicates the timestep when the intrinsic reward starts to be applied (i.e. after 20,000 timesteps). Before this point, the total reward is only affected by the task reward and the impact penalty.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-E Real robot experiments", "weight": 1.0} -->

We also conducted experiments for the two manipulation tasks on a real Shadow Dexterous Hand. The setup used for these experiments is shown in Fig. 7. A force/torque sensor is attached to a foam block, and is used to measure the force on the block.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-E Real robot experiments", "weight": 1.0} -->

As in the experiments in simulation, for the first task, the episode terminates with a reward of +1 if the hand presses the block with any fingerpad with a force greater than 5N. For the fragile objects case, the episodes terminate with a negative reward if the impact force at any point is greater than 3N, and the reward for completing the task is +5.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-E Real robot experiments", "weight": 1.0} -->

As baselines, we also ran a random agent, and agents trained using the Intrinsic Curiosity Module (ICM) proposed. Although these agents sometimes randomly hit the block, they do not consistently solve the tasks, and their interaction with the block often includes high-impact forces that exceed 5N.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-E Real robot experiments", "weight": 1.0} -->

We evaluated the different agents over 25,000 training steps. Since this is a shorter time window compared to that of the experiments executed in simulation, we increased the learning rate by one order of magnitude (from 0.0001 to 0.001). In line with the results obtained in simulation, we saw that penalty-based surprise was much more effective in learning how to perform the task gently, both in terms of learning speed (Fig. 8) and minimizing impacts (Fig. 9). The agent trained with dynamics-based surprise continues exploring the (complex) dynamics of the system on the real robot, and thus struggles to learn the simple manipulation task. On the other hand, the agent trained with penalty-based surprise is not only successful on the simple manipulation task, but notably it is the one that learns the task of manipulation of fragile objects more consistently.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

Our work takes a step toward using deep RL to train policies for gentle, contact-rich manipulation. Although curiosity has long been established as a source of endogenous motivation for artificial agents exploring the world, it may be too broad and general to drive an agent towards contact-rich policies, especially when penalties are used to discourage high-impact interactions. We found that in this scenario, choosing the appropriate focus of curiosity is important for incentivizing agents to interact gently with the environment. This enables efficient and safe exploration, precise task execution, and successful manipulation of fragile objects. Although the proposed approach is demonstrated on relatively simple tasks, we believe that it paves the way towards a new direction in curiosity research, one that identifies more nuanced types of curiosity and intrinsic motivation for deep RL agents.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

A main direction of future work is to apply this approach to more complex tasks, for instance in dynamic environments. In addition, this work only considers one aspect of being gentle---impact. Our approach could be used to train policies while minimizing other sources of wear and tear, for instance total force (rather than the increase in force), or the torques exerted by a robot's motors (which would reduce energy consumption as well ). Additionally, we note that although we use a multimodal robot environment---integrating tactile and proprioceptive sensors---we have not incorporated vision, which would provide an additional observation to support tactile and force predictions. Future work will seek to establish the value of contact-focused curiosity across this broader multimodal landscape.
