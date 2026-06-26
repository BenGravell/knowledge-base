<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Reference-Free Formula Drift with Reinforcement Learning: From Driving Data to Tire Energy-Inspired, Real-World Policies

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The skill to drift a car - i.e., operate in a state of controlled oversteer like professional drivers - could give future autonomous cars maximum flexibility when they need to retain control in adverse conditions or avoid collisions. We investigate real-time drifting strategies that put the car where needed while bypassing expensive trajectory optimization. To this end, we design a reinforcement learning agent that builds on the concept of tire energy absorption to autonomously drift through changing and complex waypoint configurations while safely staying within track bounds. We achieve zero-shot deployment on the car by training the agent in a simulation environment built on top of a neural stochastic differential equation vehicle model learned from pre-collected driving data. Experiments on a Toyota GR Supra and Lexus LC 500 show that the agent is capable of drifting smoothly through varying waypoint configurations with tracking error as low as 10 cm while stably pushing the vehicles to sideslip angles of up to 63°.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Existing autonomous vehicles are constrained to operate in a conservative driving envelope with low lateral accelerations. However, in certain situations, it may be necessary to temporarily operate the vehicle beyond its natural stability limits to avoid a collision. This style of driving is exemplified by drifting, a challenging cornering technique that involves deliberately saturating the rear tires to make the car slide while countersteering to maintain high sideslip angles. Skilled human drivers display incredible vehicle control and agility in drifting competitions, routinely sliding their cars within inches of concrete walls. Taking inspiration from their performance, this paper investigates an RL-based approach to stably push autonomous vehicles to their maximum agility potential.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prior work has demonstrated steady-state stabilization, course angle tracking, and, ultimately, reference trajectory tracking while drifting. Nonlinear model predictive control (MPC) with vehicle models based on expert knowledge or neural networks has largely supplanted earlier explicit feedback schemes. However, these MPC controllers rely on reference trajectories that are computed ahead of time by dynamic programming over a limited number of trajectory segments, rule and sampling-based planning, or trajectory optimization. With the sole exception of, which demonstrates real-time trajectory replanning to a goal region, the question of how to drift with no reference trajectory while tracking arbitrary waypoint configurations remains largely unexplored.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement learning (RL) could, in theory, provide drifting policies in such settings. Cutler et al. show steady-state drift on a scale car with steering-only policies. In and, an RL agent learns to follow the trajectory of an expert human demonstration in simulation. Validation of such approaches on full-size cars has been limited, although Tóth et al. demonstrate drift stabilization on a steady-state trajectory. Most similar to our work, Domberg et al. design a reward for drifting along a general path that penalizes the lateral deviation and includes a heuristic term to encourage high, but bounded, sideslip angles. Although the simulation results are promising, transfer to a scale car is less successful in scenarios with transient drift behavior. To date, no work has shown drifting policies tracking arbitrary waypoints on a full-scale vehicle.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present the first RL-based drifting approach that builds on judging criteria of competitive drifting to achieve maximum agility via tire energy optimization. enables accurate tracking of varying and complex waypoint configurations without a reference trajectory. enables zero-shot transfer to the vehicle by training policies on physics-informed, neural stochastic differential equation (SDE) vehicle models from actual driving data.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We validate the proposed approach on a full-size Toyota GR Supra and Lexus LC 500. Our results show strong sim-to-real transfer capabilities, high agility, and high waypoint tracking accuracy on several tracks, including those in Figure 1.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Data-Driven Simulation with Neural SDEs", "weight": 1.0} -->

This section introduces the uncertainty-aware and physics-constrained neural SDE vehicle model, trained from real-world data and used as a simulator for policy optimization. The uncertainty-aware nature of the model obviates the need for explicit domain randomization for sim-to-real transfer.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Data-Driven Simulation with Neural SDEs", "weight": 1.0} -->

We employ the single-track assumption to describe the vehicle's dynamics. The vehicle position is expressed in a curvilinear coordinate system relative to a reference path, as shown in Figure 2. The position coordinate is given by the distance $s$ along the path, the relative heading $\Delta\phi$ to a planned course $\phi^{ref}$, and the lateral deviation $e$ from the path centerline. The vehicle state $x = {\lbrack r,V,\beta,\omega_{r},e,{\Delta\phi},s\rbrack}$ includes the yaw rate $r$, velocity $V$, sideslip angle $\beta$, rear wheelspeed $\omega_{r}$, lateral error $e$, and angular deviation $\Delta\phi$ while the control input $u = {\lbrack\delta,\tau^{e}\rbrack}$ represents the desired steering angle and engine torque.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Neural SDE vehicle model", "weight": 1.0} -->

We build on the neural SDE framework proposed in to learn expressive, uncertainty-aware vehicle dynamics models from $\mathcal{T}$. The model is given by where $W$ is a $4$-dimensional Wiener process, $\Sigma^{\theta}:{{{\mathbb{R}}^{4} \times \mathcal{U}}\rightarrow{\mathbb{R}}^{4 \times 4}}$ is the SDE's diffusion term, and $a,b$, $m$, $R$, and $G$ represent the distance from the center of mass to the front axle, the distance to the rear axle, the vehicle mass, the wheel radius, and the gear ratio. Other parameters such as the yaw inertia $I_{z}^{\theta}$, drivetrain inertia $I_{w}^{\theta}$, or affine map $E^{\theta}$ from the engine to wheel torque are learned from $\mathcal{T}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-B Track encoding and waypoint configuration", "weight": 1.0} -->

In designing the simulation environment for the RL training, we encode all track information with the map $s\mapsto{({E^{ref}{(s)}},{N^{ref}{(s)}},{\phi^{ref}{(s)}},{\kappa^{ref}{(s)}},{e_{\min}^{ref}{(s)}},{e_{\max}^{ref}{(s)}})}$, where $E^{ref}$, $N^{ref}$, and $\phi^{ref}$ are the east, north, and heading coordinates of the centerline, respectively, $\kappa^{ref}$ is the track local curvature, and the lateral deviations $e_{\min}^{ref}$ and $e_{\max}^{ref}$ encode the track bounds.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Track encoding and waypoint configuration", "weight": 1.0} -->

*Therefore, with the learned $\theta^{opt}$ and the path dynamics above, we can simulate the vehicle's motion on the track by integrating the neural SDE model defined on the full state $x = {\lbrack r,V,\beta,\omega_{r},e,{\Delta\phi},s\rbrack}$.* Waypoint setup.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-B Track encoding and waypoint configuration", "weight": 1.0} -->

Given the track information, one of the goals of the RL agent is to minimize the distance to a set of waypoints ${\{{(c_{i},s_{i}^{wp},E_{i}^{wp},N_{i}^{wp})}\}}_{i = 1}^{n^{wp}}$, where $c_{i} \in {\lbrack{- b},a\rbrack}$ (illustrated in Figure 2) parameterizes a point on the vehicle's longitudinal centerline whose planar coordinates must coincide with the east $E_{i}^{wp}$ and north $N_{i}^{wp}$ coordinates at $s = s_{i}^{wp}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Track encoding and waypoint configuration", "weight": 1.0} -->

*For example, if $c_{i} = 0$, $c_{i} = {- b}$, or $c_{i} = a$, the waypoint must coincide with the center of the vehicle, the front bumper, or the rear bumper, respectively, at $s = s_{i}^{wp}$.* Through elementary kinematics, we can express the east $E_{i}$ and north $N_{i}$ coordinates of $c_{i}$ at the path distance $s$ as where ${\Phi{(s)}} = {{{\phi^{ref}{(s)}} + {\Delta\phi}} - \beta}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Tire Energy-Inspired RL Drifting Policies", "weight": 1.0} -->

In this section, we describe the design of an RL agent that learns to drift autonomously by maximizing tire energy absorption while accurately tracking arbitrary waypoint configurations and safely staying within the track bounds. We train the agent in a simulation environment built on top of the learned neural SDE vehicle model described in Section II.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Observation space and policy design", "weight": 1.0} -->

We design the observations and actions of the RL agent to capture essential features of the environment and vehicle's state. Such features enforce generalization to unseen tracks and waypoints as well as smooth and human-like control.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Observation space and policy design", "weight": 1.0} -->

Observation space. The agent's observations are all derived from the vehicle's state $x$ and past applied control.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Observation space and policy design", "weight": 1.0} -->

State variables. We use only the components $r$, $V$, $\beta$, $\omega_{r}$, and $\Delta\Phi$ of $x$ in the observation design.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Observation space and policy design", "weight": 1.0} -->

Path curvature gradient. Given a lookahead $d^{look}$ and horizon $n^{look}$, we compute $\kappa_{i} = {\kappa^{ref}{({s + {d^{look}i}})}}$ for $i \leq n^{look}$. Then, the observation is given by the gradient vector ${\Delta\kappa} = {\{{\kappa_{i} - \kappa_{i - 1}}\}}_{i = 1}^{n^{look}}$, a design choice to improve the generalization to changes in the curvature.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Observation space and policy design", "weight": 1.0} -->

*Intuitively, $\mathcal{B}{({\Delta s_{i}})}$ acts as a masking function enabling the agent to focus only on waypoints that are within a certain range of the vehicle's path distance, while $\Delta s_{i}^{wp}$ informs both on the proximity and whether the waypoint has been traversed or not.* We then use both ${\Delta s^{wp}} = {\{{\Delta s_{i}^{wp}}\}}_{i = 1}^{n^{wp}}$ and $d^{wp} = {\{ d_{i}^{wp}\}}_{i = 1}^{n^{wp}}$ as waypoint observations, or only the next few closest waypoints if $n^{wp}$ is too high.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Observation space and policy design", "weight": 1.0} -->

Past control and time step. We include the past control $u_{- 1}$ and the duration $\Delta t$ over which it was applied.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Observation space and policy design", "weight": 1.0} -->

Policy design. We modify the policy network structure to ensure that it outputs physically-feasible control inputs in $\mathcal{U}$ and such that the rate of change of the inputs is bounded by $\mathcal{U}^{rate}$. Given an observation $o$, we define the policy as where ${\hat{\mathcal{U}}}^{rate}$ and ${\overset{\sim}{\mathcal{U}}}^{rate}$ are adequate constants to transform ${\lbrack{- 1},1\rbrack} \times {\lbrack{- 1},1\rbrack}$ back to $\mathcal{U}^{rate}$, the policy ${\overline{\pi}}^{\theta}$ is a stochastic Gaussian policy network, and $\overline{o}$ is the observation $o$ without the time step. Finally, the environment clips $\pi^{\theta}$ in $\mathcal{U}$ before simulating the neural SDE vehicle model.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Reward design", "weight": 1.0} -->

Our reward function is inspired by judging criteria for single-car runs in professional drift competitions. The drivers are evaluated based on the extent to which they can maintain "a high degree of angle," "maintain momentum," and drive with "fluidity," all while accurately hitting a small number of pre-defined points on the track. We propose tire energy as the reward signal to enable drifting with "high angles" without relying on a hard-coded heuristic on the slip angle. We then add rewards on the waypoints, track progress, smooth actions and drift transitions, and track bounds.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Reward design", "weight": 1.0} -->

Tire energy. The corresponding reward is given by where the first term represents the energy contribution from the rear lateral tire force and corresponding velocity slip, and the second term is the longitudinal contribution. This term strongly encourages the vehicle to maintain a large drift angle without directly rewarding the sideslip angle, which could interfere with behavior during transient drift maneuvers where the slip angle must pass through zero.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Reward design", "weight": 1.0} -->

Waypoints. We use separate rewards for task progress $\Delta s^{wp}$ and the distance to waypoints. They are given by Smoothness. We enforce smooth transitions and human-like control inputs during drift maneuvers by penalizing large accelerations of the vehicle and the rate of changes of control inputs. The corresponding rewards are given by where ${\lambda_{r},\lambda_{\beta},\lambda_{\omega},\lambda_{V}} \in {\mathbb{R}}_{+}$ and $\lambda_{rate} \in {\mathbb{R}}_{+}^{2}$ are hyperparameters to weight the contribution of each term.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Reward design", "weight": 1.0} -->

Track bounds. We penalize proximity to track edges with where the reward is inversely proportional to the bumper's distance to the edges and reaches $- 10^{6}$ beyond the edges.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Reward design", "weight": 1.0} -->

The final reward is given as a linear combination of the above rewards weighted by hyperparameters $\lambda_{tire}$, $\lambda_{pgr}$, $\lambda_{wp}$, $\lambda_{edge}$, and weighted by $1$ for the rewards $R^{eqbr}$ and $R^{rate}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-C Massively parallel RL agent training", "weight": 1.0} -->

Although any adequate off-the-shelf RL algorithm can be used to train the drifting policy, we choose the Proximal Policy Optimization (PPO) algorithm due to its simplicity, easy customization, and massive parallelization capabilities.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-C Massively parallel RL agent training", "weight": 1.0} -->

Episode termination. During policy training and evaluation, we terminate an episode when any of the lateral deviations $e$, $e^{front}$, or $e^{rear}$ exceeds the track bounds $e_{\max}^{ref}{(s)}$ or $e_{\min}^{ref}{(s)}$. The episode also terminates for non-increasing path distance evolution over a single environment step, which indicates the vehicle is going backward. Finally, we limit the episode duration with a maximum path distance $s^{goal}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-C Massively parallel RL agent training", "weight": 1.0} -->

Policy smoothness and noise robustness. Existing approaches and their results have highlighted the challenges of obtaining smooth, non-oscillatory, and human-like control from an RL drift policy, even for steady-state drift. In addition to the reward $R^{rate}$ that encourages smooth policies by penalizing large changes in the controls, we add to the PPO's policy loss an observation-dependent term $\mathcal{J}_{jac}^{\theta}$, weighted by $\lambda_{jac}$. The term $\mathcal{J}_{jac}^{\theta}$ enforces directly in the network structure smoothness, diminish oscillatory response, and increase noise robustness. To this end, we regularize an approximation of the Frobenius norm of the policy network's Jacobian. This approach has not only been shown to improve generalization capabilities and noise robustness when compared to other existing regularization techniques but also adds only a small computational overhead to the RL training algorithm.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-C Massively parallel RL agent training", "weight": 1.0} -->

$\mathcal{J}_{jac}^{\theta}$ is given by where ${\overline{\pi}}_{mean}^{\theta}$ represents the mean of the Gaussian network ${\overline{\pi}}^{\theta}$ in and $\nu \in {\mathbb{R}}^{2}$ is a vector sampled from the normal distribution $\mathcal{N}{(0,{\mathbb{I}})}$. The loss $\mathcal{J}_{jac}^{\theta}$ can be added to the PPO-Clip objective when performing mini-batch updates.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-C Massively parallel RL agent training", "weight": 1.0} -->

Parallel training. We vectorize the integration scheme of the neural SDE model to enable massively parallel training. Each initial state is sampled from a distribution that covers a wide range of initial conditions and with the path distance randomly sampled to satisfy $s \leq s^{goal}$. To avoid the policy overfitting a fixed time step, we randomly sample the integration time step $\Delta t$ from a uniform distribution.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

We validate our approach on two vehicles with different physical properties and control capabilities. First, we demonstrate zero-shot transfer capabilities to full-size vehicles from a small amount of driving data. Then, we verify that the learned policies can generalize to varying waypoint configurations, and are robust to changes in the environment. Finally, we conduct an ablation study to show the benefits of Jacobian regularization for smooth, human-like control responses. Unless explicitly stated otherwise, all variables are in the SI system of units.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Experimental platforms and training setup", "weight": 1.0} -->

We deploy the approach on a Toyota GR Supra and a Lexus LC 500, as shown in Figure 1. The Supra is modified with a more powerful engine, drift-specific steering and suspension, and more responsive actuators, while the Lexus is merely modified to permit autonomous control, making it a particularly challenging platform for autonomous drifting. The vehicles' large differences in dynamics response make them ideal platforms for evaluating RL policies and their ability to push the limits of the vehicle's performance. For both vehicles, we use onboard vehicle state estimation using a GPS and IMU, as well as the CPU of an onboard ruggedized PC to evaluate the policy network and send the steering and engine torque commands to a hard real-time computer (dSpace MicroAutoBox II) for low-level control. We refer to and for details on the Supra and Lexus, respectively, and their parameters $a$, $b$, $R$, $m$, $\mathcal{U}$, and $\mathcal{U}^{rate}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Experimental platforms and training setup", "weight": 1.0} -->

Driving dataset. We train neural SDE-based simulators for the Supra and Lexus using manual and autonomous drifting trajectories collected from the vehicles. The Supra dataset consists of $17$ attempts at drifting and tracking the centerline of a donut and a figure-8 trajectory, while the Lexus contains $21$ attempts, each attempt lasting between $10$ and $60$ seconds. Besides, we collect the Lexus dataset by alternating between two set of tires with different characteristics: $14$ trajectories are from tire type $1$ ($T_{1}$) and the rest from tire type $2$ ($T_{2}$).

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-A Experimental platforms and training setup", "weight": 1.0} -->

Training neural SDE-based simulators. We use the same architecture for each vehicle's neural SDE-based simulator. The Supra's simulator is trained exclusively on the Supra dataset, and the same is true for the Lexus. $\Sigma^{\theta}$ is a diagonal matrix parametrized by a neural network with two hidden layers of $16$ neurons each and $\tanh$ activations. Following the architecture of $\Sigma^{\theta}$, ${NN}_{0}^{\theta}$ and ${NN}^{\theta}$ in the tire force design only have $8$ neurons each. The unknown parameters $I_{z}^{\theta}$, $I_{w}^{\theta}$, and $f_{0}^{\theta}$ are learnable scalar values. We train the models using Adam optimizer with a learning rate of $10^{- 3}$ and a batch size of $128$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-A Experimental platforms and training setup", "weight": 1.0} -->

Each state-action sequence in a batch of data is randomly sampled such that its duration is between $0.5$ and $2$ seconds. We use the Euler-Maruyama integration scheme to compute the loss $\mathcal{J}_{nll}^{\theta}$, and we use $5$ predicted particles to estimate the expectation in the loss.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A Experimental platforms and training setup", "weight": 1.0} -->

RL agent design and hyperparameters. The agent can observe changes $\Delta\kappa$ of the track curvature up to $40$ meters ahead: we use $n^{look} = 4$ and $d^{look} = 10$. We use $\gamma_{1} = 0.01$, $\gamma_{2} = 20$, $\gamma_{3} = {- 24}$, and $\gamma_{4} = 26$ to define the waypoint observations $\Delta s^{wp}$ and $d^{wp}$. That is, the observation $d_{i}^{wp}$ of the $i$-th waypoint is zero except when ${s - s_{i}^{wp}} \in {\lbrack{- 48},2\rbrack}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-A Experimental platforms and training setup", "weight": 1.0} -->

The reward weights are given by $\lambda_{tire} = 2.5$, $\lambda_{pgr} = 10$, $\lambda_{wp} = 5000$, $\lambda_{edge} = 0.001$, $\lambda_{r} = \lambda_{\beta} = 1.0$, $\lambda_{\omega} = 0.01$, $\lambda_{V} = 0$, and $\lambda_{rate} = {\lbrack 0.1,10^{- 7}\rbrack}$. We randomly sample the time step $\Delta t$ between $0.01$ and $0.05$ seconds for each environment step. We use $\lambda_{jac} = 10^{- 5}$ for the Jacobian regularization term and use a single sample $\nu$ to estimate the expectation in $\mathcal{J}_{jac}^{\theta}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-A Experimental platforms and training setup", "weight": 1.0} -->

We use the default hyperparameters of PPO, except for choosing $0.0001$ as the learning rate and vectorizing the training over $2048$ environments.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B Zero-shot, sim-to-real transfer across different vehicles", "weight": 1.0} -->

We evaluate the proposed approach on a range of pre-defined track and waypoint configurations. The experiments demonstrate that, given a vehicle, track, and waypoint configuration, the RL policy trained on the corresponding neural SDE simulator can (a) be directly deployed on the actual vehicle and (b) achieve high performance in terms of agility (sideslip angle) and waypoint accuracy (see Table 1), all while being stable and driving within the track bounds.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-B Zero-shot, sim-to-real transfer across different vehicles", "weight": 1.0} -->

Drifting with the Lexus. Contrary to the Supra, it is challenging to use the Lexus for aggressive drift maneuvers without spinning out due to limitations in its actuator response. We train and evaluate RL policies on a few modifications of the Supra's track and waypoint configurations. In particular, we modify the size of the tracks and include both front and rear bumper-based waypoints. We report our findings in Figure 5. We observe the same trend as with the Supra, where the Lexus achieves an average waypoint tracking error of $9.61 \pm 3$ cm and $24.3 \pm 11$ cm on the donut and figure-8 (Fig8, $T_{1 - 2} - T_{1}$), respectively, while operating at the limits of its steering capabilities to reach slip angles as high as $45^{\circ}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-C Policy generalization and robustness", "weight": 1.0} -->

Generalization to waypoint configurations. Instead of optimizing the policy for a fixed waypoint configuration, we modify the simulator to initialize each episode with a random waypoint configuration and train the RL policy to adapt and generalize to changing test conditions. The waypoint selection process randomly picks front or rear bumper-based waypoints, with at least $50$ meters between them and as close as $0.5$ meters away from both track edges. After the policy is trained, we fix the waypoint configuration as illustrated in Figure 4 and evaluate three runs of the policy on the Toyota Supra. Figure 4 shows that the RL policy can perform well on a new waypoint configuration, with an average tracking error of $27 \pm 4$ cm for the first (front bumper) waypoint and $17.9 \pm 3$ cm for the second (rear bumper) waypoint. Figure 4 also illustrates how smooth the RL policy is at transiting between the inside and outside waypoints while maintaining high slip angles. Additionally, we evaluate the policy in simulation with $20$ different waypoint configurations and obtain an average tracking error of $23.3 \pm 6$ cm.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C Policy generalization and robustness", "weight": 1.0} -->

Robustness to environmental changes. We evaluate the robustness of the learned policies by swapping the Lexus tires between type $T_{1}$ and $T_{2}$, and analyzing the drift performance. The figure-8 experiment shown in Figure 5 summarizes our findings. We show that the policy (*Fig8, $T_{2}$*)--trained on a neural SDE simulator fitting the Lexus dataset with tire $T_{2}$ only--when evaluated on the Lexus with tire $T_{1}$ (labeled as *Fig8, $\left. T_{2} \middle| T_{1} \right.$* in the plot), achieves low waypoint tracking accuracy while often spinning out or going off track. In contrast, the policy (*Fig8, $T_{1 - 2}$*)--trained on a simulator fitting both tires $T_{1}$ and $T_{2}$--when evaluated on $T_{1}$ and $T_{2}$ tires, can drift smoothly without spinning out or going off track.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-C Policy generalization and robustness", "weight": 1.0} -->

We observe better waypoint tracking accuracy when, at test time, the Lexus is equipped with tire $T_{1}$ (due to the ratio of $T_{1}$ trajectories in the dataset) compared to a more conservative driving and high waypoint tracking error when the Lexus is equipped with $T_{2}$. Such results suggest that model randomization during training can be used with the proposed framework to improve policy generalization.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-D Ablation study: Jacobian regularization", "weight": 1.0} -->

We investigate the effect of $\lambda_{jac}$ on the RL policy's control performance. We train in an identical manner two policies in simulation on the Supra donut track: One without Jacobian regularization $\lambda_{jac} = 0$ and one with $\lambda_{jac} = 10^{- 5}$. The resulting policies yield similar performance in terms of the total reward attained, and Figure 6 shows the steering and engine torque response on a five-second snapshot when simulating the policies. The figure shows that the policy trained with Jacobian regularization achieves a smoother control response, lower oscillations, and higher robustness to noise, making it better suited to deployment on hardware.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We propose the first RL-based drifting approach applied to a full-size vehicle that can drift, without a reference trajectory, across a general path defined by waypoints, all while pushing the car to its limits of agility through the principle of maximum tire energy absorption. Extensive experiments with a Toyota GR Supra and Lexus LC 500 demonstrate the effectiveness of the approach.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Although we show promising results in using RL to navigate through complex waypoint configurations with high agility, the current formulation, similar to existing approaches, depends on full state estimation and precise track information. Future research could investigate drifting policies that work by fusing partial state estimates and visual-based measurements from LiDAR or RGB-D cameras. Other interesting future research directions are policies that leverage brake actuators to improve stability and flexibility, adapt to changes in road conditions, and generalize across different platforms or tracks.
