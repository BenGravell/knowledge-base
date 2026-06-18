<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Dexterous multi-fingered hands are extremely versatile and provide a generic way to perform a multitude of tasks in human-centric environments. However, effectively controlling them remains challenging due to their high dimensionality and large number of potential contacts. Deep reinforcement learning (DRL) provides a model-agnostic approach to control complex dynamical systems, but has not been shown to scale to high-dimensional dexterous manipulation. Furthermore, deployment of DRL on physical systems remains challenging due to sample inefficiency. Consequently, the success of DRL in robotics has thus far been limited to simpler manipulators and tasks. In this work, we show that model-free DRL can effectively scale up to complex manipulation tasks with a high-dimensional 24-DoF hand, and solve them from scratch in simulated experiments. Furthermore, with the use of a small number of human demonstrations, the sample complexity can be significantly reduced, which enables learning with sample sizes equivalent to a few hours of robot experience. The use of demonstrations result in policies that exhibit very natural movements and, surprisingly, are also substantially more robust.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Multi-fingered dexterous manipulators are crucial for robots to function in human-centric environments, due to their versatility and potential to enable a large variety of contact-rich tasks, such as in-hand manipulation, complex grasping, and tool use. However, this versatility comes at the price of high dimensional observation and action spaces, complex and discontinuous contact patterns, and under-actuation during non-prehensile manipulation. This makes dexterous manipulation with multi-fingered hands a challenging problem.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Dexterous manipulation behaviors with multi-fingered hands have previously been obtained using model-based trajectory optimization methods. However, these methods typically rely on accurate dynamics models and state estimates, which are often difficult to obtain for contact rich manipulation tasks, especially in the real world. Reinforcement learning provides a model agnostic approach that circumvents these issues. Indeed, model-free methods have been used for acquiring manipulation skills, but so far have been limited to simpler behaviors with 2-3 finger hands or whole-arm manipulators, which do not capture the challenges of high-dimensional multi-fingered hands.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

DRL research has made significant progress in improving performance on standardized benchmark tasks, such as the OpenAI gym benchmarks. However, the current benchmarks are typically quite limited both in the dimensionality of the tasks and the complexity of the interactions. Indeed, recent work has shown that simple linear policies are capable of solving many of the widely studied benchmark tasks. Thus, before we can develop DRL methods suitable for dexterous manipulation with robotic hands, we must set up a suite of manipulation tasks that exercise the properties that are most crucial for real-world hands: high dimensionality, rich interactions with objects and tools, and sufficient task variety. To that end, we begin by proposing a set of 4 dexterous manipulation tasks in simulation, which are illustrated in Figure 1. These tasks are representative of the type of tasks we expect robots to be proficient: grasping and moving objects, in-hand manipulation, and tool usage among others. Using these representative tasks, we study how DRL can enable learning of dexterous manipulation skills.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We find that existing RL algorithms can indeed solve these dexterous manipulation tasks, but require significant manual effort in reward shaping. In addition, the sample complexity of these methods is very poor, thus making real world training infeasible, and the resulting policies exhibit idiosyncratic strategies and poor robustness. To overcome this challenge, we propose to augment the policy search process with a small number of human demonstrations collected in virtual reality (VR). In particular, we find that pre-training a policy with behavior cloning, and subsequent fine-tuning with policy gradient along with an augmented loss to stay close to the demonstrations, dramatically reduces the sample complexity, enabling training within the equivalent of a few real-world robot hours. The use of human demonstrations also provides additional desirable qualities such as human-like smooth behaviors and robustness to variations in the environment. Although success remains to be demonstrated on hardware, our results in this work indicate that DRL methods when augmented with demonstrations are a viable option for real-world learning of dexterous manipulation skills.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate, in simulation, dexterous manipulation with high-dimensional human-like five-finger hands using model-free DRL. To our knowledge, this is the first empirical result that demonstrates model-free learning of tasks of this complexity.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that with a small number of human demonstrations, the sample complexity can be reduced dramatically and brought to levels which can be executed on physical systems.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We also find that policies trained with demonstrations are more human-like as well as robust to variations in the environment. We attribute this to human priors in the demonstrations which bias the learning towards more robust strategies.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a set of dexterous hand manipulation tasks, which would be of interest to researchers at the intersection of robotic manipulation and machine learning.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Model-based trajectory optimization", "weight": 1.0} -->

: Model-based trajectory optimization methods have demonstrated impressive results in simulated domains, particularly when the dynamics can be adjusted or relaxed to make them more tractable (as, e.g., in computer animation). Unfortunately, such approaches struggle to translate to real-world manipulation since prespecifying or learning complex models on real world systems with significant contact dynamics is very difficult. Although our evaluation is also in simulation, our algorithms do not make any assumption about the structure of the dynamics model, requiring only the ability to generate sample trajectories. Our approach can be executed with minimal modification on real hardware, with the limitation primarily being the number of real-world samples required. As we will show, this can be reduced significantly with a small number of demonstrations, suggesting the possibility of performing learning directly in the real world.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Model-free reinforcement learning", "weight": 1.0} -->

Model-free RL methods and versions with deep function approximators do not require a model of the dynamics, and instead optimize the policy directly. However, their primary drawback is the requirement for a large number of real-world samples. Some methods like PoWER overcome this limitation through the use of simple policy representations such as DMPs and demonstrate impressive results. However, more complex representations may be needed in general for more complex tasks and to incorporate rich sensory information. More recently, RL methods with rich neural network function approximators have been studied in the context of basic manipulation tasks with 7-10 DoF manipulators, and have proposed a variety of ways to deal with the sample complexity. Prior work has demonstrated model-free RL in the real world with simulated pre-training and parallelized data collection for lower-dimensional whole-arm manipulation tasks. Our work builds towards model-free DRL on anthropomorphic hands, by showing that we can reduce sample complexity of learning to practical levels with a small number of human demonstrations. Prior work has demonstrated learning of simpler manipulation tasks like twirling a cylinder with a similar morphology using guided policy search, and extended this approach to also incorporate demonstrations.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Model-free reinforcement learning", "weight": 1.0} -->

However, the specific tasks we demonstrate are substantially more complex featuring a large number of contact points and tool use, as detailed in Section III.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Imitation learning", "weight": 1.0} -->

In imitation learning, demonstrations of successful behavior are used to train policies that imitate the expert providing these successful trajectories. A simple approach to imitation learning is behavior cloning (BC), which learns a policy through supervised learning to mimic the demonstrations. Although BC has been applied successfully in some instances like autonomous driving, it suffers from problems related to distribution drift. Furthermore, pure imitation learning methods cannot exceed the capabilities of the demonstrator since they lack a notion of task performance. In this work, we do not just perform imitation learning, but instead use imitation learning to bootstrap the process of reinforcement learning. The bootstrapping helps to overcome exploration challenges, while RL fine-tuning allows the policy to improve based on actual task objective.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Combining RL with demonstrations", "weight": 1.0} -->

Methods based on dynamic movement primitives (DMPs) have been used to effectively combine demonstrations and RL to enable faster learning. Several of these methods use trajectory-centric policy representations, which although well suited for imitation, do not enable feedback on rich sensory inputs. Although such methods have been applied to some dexterous manipulation tasks, the tasks are comparatively simpler than those illustrated in our work. Using expressive function approximators allow for complex, nonlinear ways to use sensory feedback, making them well-suited to dexterous manipulation.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Combining RL with demonstrations", "weight": 1.0} -->

In recent work, demonstrations have been used for pre-training a Q-function by minimizing TD error. Additionally demonstrations have been used to guide exploration through reward/policy shaping but these are often rule-based or work on discrete spaces making them difficult to apply to high dimensional dexterous manipulation. The work most closely related to ours is DDPGfD, where demonstrations are incorporated into DDPG by adding them to the replay buffer. This presents a natural and elegant way to combine demonstrations with an off-policy RL method. In concurrent work, this approach was combined with hindsight experience replay. The method we propose in this work bootstraps the policy using behavior cloning, and combines demonstrations with an on-policy policy gradient method. Off-policy methods, when successful, tend to be more sample efficient, but are generally more unstable. On-policy methods on the other hands are more stable, and scale well to high dimensional spaces. Our experimental results indicate that with the incorporation of demonstrations, the sample complexity of on-policy methods can be dramatically reduced, while retaining their stability and robustness. Indeed, the method we propose significantly outperforms DDPGfD.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Combining RL with demonstrations", "weight": 1.0} -->

Concurrent works with this paper have also proposed to integrate demonstrations into reward functions, and there have been attempts to learn with imperfect demonstrations. Overall, we note that the general idea of bootstrapping RL with supervised training is not new. However, the extent to which it helps with learning of complex dexterous manipulation skills is surprising and far from obvious.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Dexterous Manipulation Tasks", "weight": 1.0} -->

The real world presents a plethora of interesting and important manipulation tasks. While solving individual tasks via custom manipulators in a controlled setting has led to success in industrial automation, this is less feasible in an unstructured settings like the home. Our goal is to pick a minimal task-set that captures the technical challenges representative of the real world. We present four classes of tasks - object relocation, in-hand manipulation, tool use, and manipulating environmental props (such as doors). Each class exhibits distinctive technical challenges, and represent a large fraction of tasks required for proliferation of robot assistance in daily activities -- thus being potentially interesting to researchers at the intersection of robotics and machine learning. All our task environments expose hand (joint angles), object (position and orientation), and target (position and orientation) details as observations, expect desired position of hand joints as actions, and provides an oracle to evaluate success. We now describe the four classes in light of the technical challenges they present.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A1 Object relocation (Figure 2)", "weight": 1.0} -->

Object relocation is a major class of problems in dexterous manipulation, where an object is picked up and moved to a target location. The principal challenge here from an RL perspective is exploration, since in order to achieve success, the hand has to reach the object, grasp it, and take it to the target position -- a feat that is very hard to accomplish without priors in the form of shaped rewards or demonstrations.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A2 In-hand Manipulation -- Repositioning a pen (Figure 3)", "weight": 1.0} -->

In hand-manipulation maneuvers like re-grasping, re-positioning, twirling objects etc. involve leveraging the dexterity of a high DOF manipulator to effectively navigate a difficult landscape filled with constraints and discontinuities imposed by joint limits and frequently changing contacts. Due to the large number of contacts, conventional model-based approaches which rely on accurate estimates of gradients through the dynamics model struggle in these problem settings. The major challenge in these tasks is representing the complex solutions needed for different maneuvers. For these reason, sampling based DRL methods with rich neural network function approximators are particularly well suited for this class of problems. Previous work on in-hand manipulation with RL has considered simpler tasks such as twirling a cylinder, but our tasks involve omni-directional repositioning which involves significantly more contact use. Collecting human demonstrations for this task was challenging due to lack of tactile feedback in VR. Instead, to illustrate the effectiveness of our proposed algorithms, we used a computational expert trained using RL on a well shaped reward for many iterations. This expert serves to give demonstrations which are used to speed up training from scratch.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A3 Manipulating Environmental Props (Figure 4)", "weight": 1.0} -->

Real-world robotic agents will require constant interaction and manipulation in human-centric environments. Tasks in this class involve modification of the environment itself - opening drawers for fetching, moving furniture for cleaning, etc. The solution is often multi-step with hidden subgoals (e.g undo latch before opening doors), and lies on a narrow constrained manifold shaped primarily by the inertial properties and the under actuated dynamics of the environment.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A4 Tool Use -- Hammer (Figure 5)", "weight": 1.0} -->

Humans use tools such as hammers, levers, etc. to augment their capabilities. These tasks involve co-ordination between the fingers and the arm to apply the tool correctly. Unlike object relocation, the goal in this class of tasks is to use the tool as opposed to just relocating it. Not all successful grasp leads to effective tool use. Effective tool use requires multiple steps involving grasp reconfiguration and careful motor co-ordination in order to impart the required forces. In addition, effective strategies needs to exhibit robust behaviors in order to counter and recover from destabilizing responses from the environment.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A4 Tool Use -- Hammer (Figure 5)", "weight": 1.0} -->

Further details about the tasks, including detailed shaped reward functions, physics parameters etc.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Experimental setup", "weight": 1.0} -->

To accomplish the tasks laid out above, we use a high degree of freedom dexterous manipulator and a virtual reality demonstration system which we describe below.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B1 ADROIT hand", "weight": 1.0} -->

We use a simulated analogue of a highly dexterous manipulator -- ADROIT, which is a 24-DoF anthropomorphic platform designed for addressing challenges in dynamic and dexterous manipulation. The first, middle, and ring fingers have 4 DoF. Little finger and thumb have 5 DoF, while the wrist has 2 DoF. Each DoF is actuated using position control and is equipped with a joint angle sensor (Figure 6).

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B2 Simulator", "weight": 1.0} -->

Our experimental setup uses the MuJoCo physics simulator. The stable contact dynamics of MuJoCo makes it well suited for contact rich hand manipulation tasks. The kinematics, the dynamics, and the sensing details of the physical hardware were carefully modeled to encourage physical realism. In addition to dry friction in the joints, all hand-object contacts have planar friction. Object-fingertip contacts support torsion and rolling friction. Though the simulation supports tactile feedback, we do not use it in this work for simplicity, but expect that its use will likely improve the performance.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-C Demonstrations", "weight": 1.0} -->

Accurate demonstrations data are required to help accelerate various learning algorithms. Standard methods like kinesthetic teaching are impractical with complex systems like ones we study in this work. We use an updated version of the Mujoco HAPTIX system. The system uses the CyberGlove III system for recording the fingers, HTC vive tracker for tracking the base of the hand and HTC vive headset for stereoscopic visualization. This moves the process of demonstration data collection from the real world to virtual reality, allowing for several high fidelity demonstrations for tasks involving large number of contacts and dynamic phenomena such as rolling, sliding, stick-slip, deformations and soft contacts. Since the demonstrations are provided in simulation, physically consistent details of the movements can be easily recorded. We gathered 25 successful demonstrations for all our tasks (with task randomization as outlined in captions of Figure 2, 3, 5, and 4), with each demonstration consisting of the state-action trajectories needed to perform the task in simulation.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-C Demonstrations", "weight": 1.0} -->

To combat distribution drift, a small amount of noise (uniform random $\lbrack{- 0.1},0.1\rbrack$ radians) is added to the actuators per timestep so that the policy can better capture relevant statistics about the data.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Demo Augmented Policy Gradient (DAPG)", "weight": 1.0} -->

In this work, we use a combination of RL and imitation learning to solve complex dexterous manipulation problems. To reduce sample complexity and help with exploration, we collect a few expert demonstrations using the VR system described in Section III-C, and incorporate these into the RL process. We first present some RL preliminaries, followed by the base RL algorithm we use for learning, and finally describe our procedure to incorporate demonstrations.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A Preliminaries", "weight": 1.0} -->

We model the control problem as a Markov decision process (MDP), which is defined using the tuple: $\mathcal{M} = {\{\mathcal{S},\mathcal{A},\mathcal{R},\mathcal{T},\rho_{0},\gamma\}}$. $\mathcal{S} \in {\mathbb{R}}^{n}$ and $\mathcal{A} \in {\mathbb{R}}^{m}$ represent the state and actions. $\mathcal{R}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ is the reward function which measures task progress. In the ideal case, this function is simply an indicator function for task completion (i.e. a sparse task completion reward). In practice, various forms of shaped rewards that incorporate human priors on how to accomplish the task might be required to make progress on the learning problem.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Preliminaries", "weight": 1.0} -->

$\mathcal{T}:{{\mathcal{S} \times \mathcal{A}}\rightarrow\mathcal{S}}$ is the transition dynamics, which can be stochastic. In model-free RL, we do not assume knowledge about this transition function, and require only sampling access to this function. $\rho_{0}$ is the probability distribution over initial states and $\gamma \in {\lbrack 0,1)}$ is a discount factor. We denote the demonstrations data set using $\rho_{D} = \left\{ \left( s_{t}^{(i)},a_{t}^{(i)},s_{t + 1}^{(i)},r_{t}^{(i)} \right) \right\}$, where $t$ indexes time and $i$ indexes different trajectories. These demonstrations can be used to guide reinforcement learning and significantly reduce sample complexity of RL.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A Preliminaries", "weight": 1.0} -->

We consider parameterized policies $\pi_{\theta}$, and hence wish to optimize for the parameters $(\theta)$. Thus, we overload notation and use $\eta{(\pi)}$ and $\eta{(\theta)}$ interchangeably.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-B Natural Policy Gradient", "weight": 1.0} -->

In this work, we primarily consider policy gradient methods, which are a class of model-free RL methods. In policy gradient methods, the parameters of the policy are directly optimized to maximize the objective, $\eta{(\theta)}$, using local search methods such as gradient ascent. In particular, for this work we consider the NPG algorithm.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B Natural Policy Gradient", "weight": 1.0} -->

where $\delta$ is the step size choice. A number of pre-conditioned policy gradient methods have been developed in literature and in principle any of them could be used. Our implementation of NPG for the experiments is based on Rajeswaran et al..

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-C Augmenting RL with demonstrations", "weight": 1.0} -->

RL is only able to solve the tasks we consider with careful, laborious task reward shaping.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-C Augmenting RL with demonstrations", "weight": 1.0} -->

While RL eventually solves the task with appropriate shaping, it requires an impractical number of samples to learn - in the order of a 100 hours for some tasks.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-C Augmenting RL with demonstrations", "weight": 1.0} -->

The behaviors learned by pure RL have unnatural appearance, are noisy and are not as robust to environmental variations.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-C Augmenting RL with demonstrations", "weight": 1.0} -->

Combining demonstrations with RL can help combat all of these issues. Demonstrations help alleviate the need for laborious reward shaping, help guide exploration and decrease sample complexity of RL, while also helping produce robust and natural looking behaviors.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-C1 Pretraining with behavior cloning", "weight": 1.0} -->

Policy gradient methods typically perform exploration by utilizing the stochasticity of the action distribution defined by the policy itself. If the policy is not initialized well, the learning process could be very slow with the algorithm exploring state-action spaces that are not task relevant. To combat this, we use behavior cloning (BC) to provide an informed policy initialization that efficiently guides exploration. Use of demonstrations circumvents the need for reward shaping often used to guide exploration. This idea of pretraining with demonstrations has been used successfully in prior work, and we show that this can dramatically reduce the sample complexity for dexterous manipulation tasks as well.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-C1 Pretraining with behavior cloning", "weight": 1.0} -->

The optimizer of the above objective, called the behavior cloned policy, attempts to mimic the actions taken in the demonstrations at states visited in the demonstrations. In practice, behavior cloning does not guarantee that the cloned policy will be effective, due to the distributional shift between the demonstrated states and the policy's own states. Indeed, we observed experimentally that the cloned policies themselves were usually not successful.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-C2 RL fine-tuning with augmented loss", "weight": 1.0} -->

Though behavior cloning provides a good initialization for RL, it does not optimally use the information present in the demonstration data. Different parts of the demonstration data are useful in different stages of learning, especially for tasks involving a sequence of behaviors. For example, the hammering task requires behaviors such as reaching, grasping, and hammering. Behavior cloning by itself cannot learn a policy that exhibits all these behaviors in the correct sequence with limited data. The result is that behavior cloning produces a policy that can often pick up the hammer but seldom swing it close to the nail. The demonstration data contains valuable information on how to hit the nail, but is lost when the data is used only for initialization. Once RL has learned to pick up the hammer properly, we should use the demonstration data to provide guidance on how to hit the nail.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-C2 RL fine-tuning with augmented loss", "weight": 1.0} -->

Here $\rho_{\pi}$ represents the dataset obtained by executing policy $\pi$ on the MDP, and $w{(s,a)}$ is a weighting function. This augmented gradient is then used in eq. to perform a co-variant update. If ${w{(s,a)}} = {0{\forall{(s,a)}}}$, then we recover the policy gradient in eq.. If ${w{(s,a)}} = {c{\forall{(s,a)}}}$, with sufficiently large $c$, it reduces to behavior cloning, as in eq.. However, we wish to use both imitation and reinforcement learning, so we require an alternate weighting function. The analysis in suggests that eq. is also valid for mixture trajectory distributions of the form $\rho = {{\alpha\rho_{\pi}} + {{({1 - \alpha})}\rho_{D}}}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-C2 RL fine-tuning with augmented loss", "weight": 1.0} -->

Thus, a natural choice for the weighting function would be ${w{(s,a)}} = {A^{\pi}{(s,a)}{\forall{(s,a)}}} \in \rho_{D}$. However, it is not possible to compute this quantity without additional rollouts or assumptions.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C2 RL fine-tuning with augmented loss", "weight": 1.0} -->

where $\lambda_{0}$ and $\lambda_{1}$ are hyperparameters, and $k$ is the iteration counter. The decay of the weighting term via $\lambda_{1}^{k}$ is motivated by the premise that initially the actions suggested by the demonstrations are at least as good as the actions produced by the policy. However, towards the end when the policy is comparable in performance to the demonstrations, we do not wish to bias the gradient. Thus, we asymptotically decay the auxiliary objective. We empirically find that the performance of the algorithm is not very sensitive to the choice of these hyperparameters. For all the experiments, $\lambda_{0} = 0.1$ and $\lambda_{1} = 0.95$ was used.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

Our results study how RL methods can learn dexterous manipulation skills, comparing several recent algorithms and reward conditions. First, we evaluate the capabilities of RL algorithms to learn dexterous manipulation behaviors from scratch on the tasks outlined in Section III. Subsequently, we demonstrate the benefits of incorporating human demonstrations with regard to faster learning, increased robustness of trained policies, and ability to cope with sparse task completion rewards.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-A Reinforcement Learning from Scratch", "weight": 1.0} -->

Can existing RL methods cope with the challenges presented by the high dimensional dexterous manipulation tasks?

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-A Reinforcement Learning from Scratch", "weight": 1.0} -->

Do the resulting policies exhibit desirable properties like robustness to variations in the environment?

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-A Reinforcement Learning from Scratch", "weight": 1.0} -->

Are the resulting movements safe for execution on physical hardware, and are elegant/nimble/human-like?

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-A Reinforcement Learning from Scratch", "weight": 1.0} -->

In order to benchmark the capabilities of DRL with regard to the dexterous manipulation tasks outlined in Section III, we evaluate the NPG algorithm described briefly in Section V, and the DDPG algorithm, which has recently been used in a number of robotic manipulation scenarios. Both of these methods have demonstrated state of the art results in popular DRL continuous control benchmarks, and hence serve as a good representative set. We score the different methods based on the percentage of successful trajectories the trained policies can generate, using a sample size of 100 trajectories. We find that with sparse task completion reward signals, the policies with random exploration never experience success (except in the in-hand task) and hence do not learn.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-A Reinforcement Learning from Scratch", "weight": 1.0} -->

In order to enable these algorithms to learn, we incorporate human priors on how to accomplish the task through careful reward shaping. With the shaped rewards, we find that NPG is indeed able to achieve high success percentage on these tasks (Figure 7), while DDPG was unable to learn successful policies despite considerable hyperparameter tuning. DDPG can be very sample efficient, but is known to be very sensitive to hyperparameters and random seeds, which may explain the difficulty of scaling it to complex, high-dimensional tasks like dexterous manipulation.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-A Reinforcement Learning from Scratch", "weight": 1.0} -->

Although incorporation of human knowledge via reward shaping is helpful, the resulting policies: (a) often exhibit unnatural looking behaviors, and (b) are too sample inefficient to be useful for training on the physical hardware. While it is hard to mathematically quantify the quality of generated behaviors, Figure 8 and the accompanying video clearly demonstrate that the learned policies produce behaviors that are erratic and not human-like. Such unnatural behaviors are indeed quite prevalent in the recent DRL results. Furthermore, we take the additional step of analyzing the robustness of these policies to variations in environments that were not experienced during training. To do so, we take into account the policy trained for the object relocation task and vary the mass and size of the object that has to be relocated. We find that the policies tend to over-fit to the specific objects they were trained to manipulate and is unable to cope with variations in the environment as seen in Figure 9.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-A Reinforcement Learning from Scratch", "weight": 1.0} -->

We attribute the artifacts and brittleness outlined above to the way in which human priors are incorporated into the policy search process. The mental models of solution strategies that humans have for these tasks are indeed quite robust. However it is challenging to distill this mental model or intuition into a mathematical reward function. As we will show in the next section, using a data driven approach to incorporate human priors, in the form of demonstrations, alleviates these issues to a significant extent.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-B Reinforcement Learning with Demonstrations", "weight": 1.0} -->

Does incorporating demonstrations via DAPG reduce the learning time to practical timescales?

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-B Reinforcement Learning with Demonstrations", "weight": 1.0} -->

How does DAPG compare to other model-free methods that incorporate demonstrations, such as DDPGfD ?

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-B Reinforcement Learning with Demonstrations", "weight": 1.0} -->

Does DAPG acquire robust and human-looking behaviors without reward shaping?

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-B Reinforcement Learning with Demonstrations", "weight": 1.0} -->

We employ the DAPG algorithm in Section IV-C ‣ Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations") on the set of hand tasks and compare with the recently proposed DDPGfD method. DDPGfD builds on top of the DDPG algorithm, and incorporates demonstrations to bootstrap learning: Adding demonstrations to the replay buffer; Using prioritzed experience replay; Using n-step returns; Adding regularizations to the policy and critic networks. Overall, DDPGfD has proven effective on arm manipulation tasks with sparse rewards in prior work, and we compare performance of DAPG against DDPGfD on our dexterous manipulation tasks.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-B Reinforcement Learning with Demonstrations", "weight": 1.0} -->

For this section of the evaluation we use only sparse task completion rewards, since we are using demonstrations. With the use of demonstrations, we expect the algorithms to implicitly learn the human priors on how to accomplish the task. Figure 10 presents the comparison between the different algorithms. DAPG convincingly outperforms DDPGfD in all the tasks well before DDPGfD even starts showing signs of progress. Furthermore, DAPG is able to train policies for these complex tasks in under a few robot hours Table I. In particular, for the object relocation task, DAPG is able to train policies almost 30 times faster compared to learning from scratch. This indicates that RL methods in conjunction with demonstrations, and in particular DAPG, are viable approaches for real world training of dexterous manipulation tasks.

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-B Reinforcement Learning with Demonstrations", "weight": 1.0} -->

When analyzing the robustness of trained policies to variations in the environment, we find that policies trained with DAPG are significantly more robust compared to the policies trained with shaped rewards (Figure 9). Furthermore, a detail that can be well appreciated in the accompanying video is the human-like motions generated by the policy. The policies trained with DAPG better capture the human priors from the demonstrations, and generate policies that are more robust and exhibit qualities that are inherently expected but hard to mathematically specify.

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-B Reinforcement Learning with Demonstrations", "weight": 1.0} -->

In our final experiment, we also explore how robustness can be further improved by training on a distribution (ensemble) of training environments, where each environment differs in terms of the physical properties of the manipulated object (its size and mass). By training policies to succeed on the entire ensemble, we can acquire policies that are explicitly trained for robustness, similar in spirit to previously proposed model ensemble methods. Interestingly, we observe that for difficult control problems like high dimensional dexterous manipulation, RL from scratch with shaped rewards is unable to learn a robust policy for a diverse ensemble of environments in a time frame comparable to the time it takes to master a single instance of the task. On the other hand, DAPG is still able to succeed in this setting and generates even more robust policies, as shown in Figure 9.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we developed a set of manipulation tasks representative of the types of tasks we encounter in everyday life. The tasks involve the control of a 24-DoF five-fingered hand. We also propose a method, DAPG, for incorporating demonstrations into policy gradient methods. Our empirical results compare model-free RL from scratch using two state-of-the-art DRL methods, DDPG and NPG, as well their demonstration-based counterparts, DDPGfD and our DAPG algorithm. We find that NPG is able to solve these tasks, but only after significant manual reward shaping. Furthermore, the policies learned under these shaped rewards are not robust, and produce idiosyncratic and unnatural motions. After incorporating human demonstrations, we find that our DAPG algorithm acquires policies that not only exhibit more human-like motion, but are also substantially more robust. Furthermore, we find that DAPG can be up to 30x more sample efficient than RL from scratch with shaped rewards. DAPG is able to train policies for the tasks we considered in under 5 hours, which is likely practical to run on real systems.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Although success remains to be demonstrated on real hardware, given the complexity of the tasks in our evaluation and the sample-efficiency of our DAPG method, we believe that our work provides a significant step toward practical real-world learning of complex dexterous manipulation. In future work, we hope to learn policies on real hardware systems, further reduce sample complexity by using novelty based exploration methods, and learn policies from only raw visual inputs and tactile sensing.
