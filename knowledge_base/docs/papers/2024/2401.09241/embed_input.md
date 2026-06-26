<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers

Topics include Model predictive path integral control, Trajectory optimization, Sampling-based control, Informed sampling, Ancillary controller.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Biased-MPPI augments the MPPI sampling distribution by biasing it toward trajectories suggested by one or more ancillary controllers (e.g., path-following or optimization-based), improving sample efficiency and trajectory quality while preserving the exploration benefits of random sampling.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Motion planning for autonomous robots in dynamic environments poses numerous challenges due to uncertainties in the robot's dynamics and interaction with other agents. Sampling-based MPC approaches, such as Model Predictive Path Integral (MPPI) control, have shown promise in addressing these complex motion planning problems. However, the performance of MPPI relies heavily on the choice of sampling distribution. Existing literature often uses the previously computed input sequence as the mean of a Gaussian distribution for sampling, leading to potential failures and local minima. In this paper, we propose a novel derivation of MPPI that allows for arbitrary sampling distributions to enhance efficiency, robustness, and convergence while alleviating the problem of local minima. We present an efficient importance sampling scheme that combines classical and learning-based ancillary controllers simultaneously, resulting in more informative sampling and control fusion. Several simulated and real-world demonstrate the validity of our approach.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Navigating autonomous robots through dense and dynamic environments poses a formidable challenge due to significant uncertainties, including the robot's state, model, environmental conditions, and interactions with other agents. Achieving desired behaviors under such conditions often necessitates using intricate cost functions and constraints, resulting in complex, nonlinear, non-convex, and occasionally discontinuous problem formulations. The dynamic nature of the environment introduces potential unexpected changes, demanding rapid adaptability in the robot's actions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address these challenges, one approach is to cast the problem in a stochastic optimal control setting, where they can be mathematically represented as stochastic Hamilton-Jacobi-Bellman (HJB) equations. However, solving these equations numerically can be challenging due to the curse of dimensionality. Pioneering work demonstrated that the stochastic HJB equations can be linearized for control-affine systems, and their solution can be approximated through sampling using the path integral formulation. Implemented in a receding horizon fashion, Model Predictive Path Integral (MPPI) control, and its Information-Theoretic counterpart have been initially used for racing a small-scale rally car. MPPI has also been successfully applied to several other planning problems, such as for autonomous vehicles with dynamic obstacles, solving games, flying drones in partially observable environments, performing complex maneuvers and used in combination with adaptive control schemes. It has also been adapted to multi-agent systems for formation flying, cooperative behavior, and simultaneous prediction and planning. Furthermore, MPPI has shown promise in manipulating objects with robot arms including model uncertainties, in pushing tasks and planning motion for four-legged walking robots.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

MPPI is a model-based approach that requires a model to forward simulate trajectories given sampled inputs. Recent work has utilized physics engines to simulate samples, eliminating the need for explicitly defining the dynamics of agents and the environment, thus providing a significant advantage in contact-rich manipulation tasks.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

One of the critical challenges in applying MPPI to dynamic environments is ensuring the algorithm's performance and reliability. The success of MPPI heavily relies on the choice of sampling distribution, which is crucial, especially in real-time scenarios. Most existing literature uses the previously computed input sequence as the mean of a Gaussian distribution for sampling, with the variance being tunable. However, using the previous input sequence may trap the algorithm in local minima. This can lead to catastrophic failures in the presence of unexpected disturbances or changes in the environment (Fig. 1).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper explores the application of MPPI in dynamic environments, emphasizing the need to improve its performance and reliability in the face of unexpected disturbances and rapidly changing conditions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-A Previous Work", "weight": 1.0} -->

Several works tried to make the method more efficient or more robust. Early work proposed using Expectation Propagation instead of Monte Carlo sampling, demonstrating better efficiency in scenarios with hard constraints. Other works instead accelerate the convergence of MPPI by leveraging gradient descent updates. Another option to be more reactive to environmental changes is to iteratively converge to a solution through adaptive importance sampling. This, however, requires multiple iterations between each planning time step, diminishing the parallelizability of MPPI. Many other works propose improving the algorithm's convergence by somehow changing its sampling distribution. This can be done by substituting the Gaussian used for sampling with a different hand-crafted distribution or by directly learning a distribution from data. Given that MPPI allows for tuning the variance of the sampling distribution, some works sought to improve the efficiency of the scheme by adapting the covariance online via covariance steering. Other ways to improve efficiency can be to fit splines to the sampled inputs or to constrain the distribution to sample areas that are known to contain low-cost trajectories. Previous works have also experimented with ancillary controllers. In, authors propose to sample inputs around a path previously computed by RRT.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-A Previous Work", "weight": 1.0} -->

Other works instead robustify MPPI by switching to an iLQG controller or by integrating one into the system's model. Previous work also compares an MPPI that samples around a previously computed input, an input sequence computed by a sequential linear-quadratic MPC, and a learned sampling policy. In general, however, the original derivations of MPPI only allow samples to be drawn from a uni-modal Gaussian distribution, usually centered around the previous control sequence, which can hamper performance and reduce reactivity to unexpected changes in the environment.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

We propose a Biased-MPPI, for which we provide mathematical derivations that allow for arbitrary changes to the sampling distribution. We discuss the impact of introducing biases in the sampling distribution on the overall method. We experiment with an importance sampler that utilizes multiple classical and learning-based ancillary controllers simultaneously to take more informative samples, which can be seen as a control fusion scheme. Through simulated and real-world experiments, we demonstrate the impact of taking suggestions from several underlying controllers on robustness to model uncertainties and local minima, reactivity to unexpected events, and sampling efficiency.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A Biased-MPPI", "weight": 1.0} -->

We can simplify the right-hand side as follows: The free energy inequality is then: Thus, while we start with $\overset{\sim}{S}{(V)}$, the free energy serves as a lower bound for the expected original cost $S{(V)}$ under the controlled distribution plus lambda times the KL-Divergence between the controlled and sampling distribution. An optimal control distribution achieving the lower bound would minimize the original cost $S{(V)}$ while pushing the controlled distribution to align with the sampling distribution, effectively introducing a bias toward the sampling distribution.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A Biased-MPPI", "weight": 1.0} -->

We define a controlled distribution ${\mathbb{Q}}^{\ast}$ as: Under ${\mathbb{Q}}^{\ast}$, the KL-Divergence becomes: Substituting into 12 and simplifying leads to: This proves that ${\mathbb{Q}}^{\ast}$ is the optimal distribution in that it achieves the lower bound in 12. Following the steps, we can align our controlled distribution $\mathbb{Q}$ to ${\mathbb{Q}}^{\ast}$ as in 6, except we can now use our sampling distribution: with importance sampling weights: | | | ${\omega{(V)}} = {\frac{1}{\eta}{\exp\left({- {\frac{1}{\lambda}\overset{\sim}{S}{(V)}}} \right)}\left(\frac{p{(V)}}{q_{s}{(V)}} \right)}$ | | \(14\) | | |

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Biased-MPPI", "weight": 1.0} -->

In, $S{(V)}$ was defined as the state-dependent cost. However, this restriction was made to relate the approach to path integral control. Such relation was only shown exactly when $\mathbb{P}$ is the distribution induced by an uncontrolled continuous-time control-affine system. This restriction is not required in the Information-Theoretic framework, which allows for a larger class of systems, and one can add input costs in S(V).

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-B Sampling from Ancillary Controllers", "weight": 1.0} -->

There are several ways one could design an arbitrary sampling distribution. This paper focuses on taking most samples around a previously computed input distribution and some samples from hand-crafted policies.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-B Sampling from Ancillary Controllers", "weight": 1.0} -->

In particular, we design a set of task-specific ancillary controllers, these being, e.g., open-loop motion primitives, reference tracking feedback controllers, or learning-based strategies to propose $J$ input sequences $U^{j} = {\lbrack u_{0}^{j},u_{1}^{j},\ldots,u_{t}^{j},\ldots,u_{T_{H}}^{j}\rbrack}$. These ancillary controllers are described for each experiment in Sections IV and V. We then choose the K sampled input sequences $V_{s}^{k}$ as, meaning that, at each time step, we take one sample from each of the $J$ ancillary controllers, and the remaining $K - J$ samples are taken according to the classical MPPI strategy.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-C Autotuning the Inverse Temperature", "weight": 1.0} -->

As in and similarly to, we autotune the inverse temperature $\lambda$ online based on the normalization factor $\eta$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-C Autotuning the Inverse Temperature", "weight": 1.0} -->

In all experiments, this can roughly keep the number of samples with a significant weight between $\eta_{min}$ and $\eta_{max}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Illustrative Experiment", "weight": 1.0} -->

We apply our Biased-MPPI to a rotary inverted pendulum (Fig. 2) in simulation to visualize its main features.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A Swing-up and tracking", "weight": 1.0} -->

Starting at the bottom equilibrium with $\theta_{0} = 0$ and $\alpha_{0} = \pi$, the task is to swing up the pendulum to $\alpha_{r} = 0$ while keeping the arm close to $\theta_{r} = 1$. Thus, the running cost is: The system has dynamics ${x{({t + 1})}} = {F{({x{(t)}},{u{(t)}})}}$, where the state of the system at time-step $t$ is denoted as ${x{(t)}} = {\lbrack\theta_{t},\alpha_{t},\overset{˙}{\theta_{t}},\overset{˙}{\alpha_{t}}\rbrack}^{T}$, and $u$ represents the system's input. The nonlinear model is derived from the Lagrange equations. To design linear controllers, the model is linearized at the top equilibrium using Euler-Lagrange's method.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-A Swing-up and tracking", "weight": 1.0} -->

To showcase resilience against model uncertainties, the parameters of the simulation's pendulum model are multiplied by $1 + \gamma$ in each experiment, where $\gamma \sim {\mathcal{N}{(0,0.05)}}$. The seed is consistent across methods. The system is dicretized and controllers run at $50Hz$, the controller plans $T_{H} = 50$ steps ahead ($1s$), covariance $\Sigma_{s} = 0.5$, $\eta_{min} = 2$ and $\eta_{max} = 5$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A1 Ancillary Controllers", "weight": 1.0} -->

We design three ancillary controllers as a baseline and to guide the sampling strategy.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Linear Quadratic Regulator (LQR)", "weight": 1.0} -->

designed using the `lqr` command in Matlab, stabilizes the pendulum at the top equilibrium.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Linear Quadratic Integral (LQI)", "weight": 1.0} -->

tracks the reference $\theta_{r}$ while maintaining the pendulum at the top equilibrium. It is synthesized with the `lqi` command in Matlab.

<!-- chunk {"id": "body-0025", "role": "body", "section": "A nonlinear Energy-Based Controller (EBC)", "weight": 1.0} -->

is designed as in to swing up the pendulum to the top equilibrium by increasing the potential energy of the system.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-A2 Switching Controller", "weight": 1.0} -->

We introduce as baseline a switching strategy 18 that combines all ancillary controllers. It swings up the pendulum using the input from the ECB, $u_{ebc}$, until $\alpha$ is within $\alpha_{catch} = 0.2$ of the top equilibrium. The LQR controller, with $u_{lqr}$, then stabilizes the pendulum. Once the pendulum is close to the top equilibrium ($\alpha_{track} = 0.05$) with angular velocity below ${\overset{˙}{\alpha}}_{track} = 0.1$ rad/s, the LQI, with $u_{lqi}$, is engaged for reference tracking.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-A3 Results", "weight": 1.0} -->

Fig. 3 depicts a pendulum experiment's input and state evolution with Biased-MPPI, also showcasing the samples taken and the ancillary controllers' influence on the plan. At the beginning of the experiment, ECB rapidly swings up the pendulum, heavily influencing Biased-MPPI's planned input. Once near equilibrium, LQR provides a stabilizing sequence, closely tracked by Biased-MPPI. As stability is achieved, LQI suggests an input sequence swiftly bringing the arm towards the reference, albeit with high velocities. Hence, Biased-MPPI, while influenced by LQI, opts for a lower amplitude input sequence due to cost function 17.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-A3 Results", "weight": 1.0} -->

Fig. 4 displays the distribution of total costs, defined as $\sum_{t = 0}^{T_{end}}{C_{p}{({x{(t)}})}}$ where $T_{end} = 250$ ($5s$) is the end of the episode, and the distribution of total efforts, defined as $\sum_{t = 0}^{T_{end}}{|{u{(t)}}|}$, across 50 experiments. Biased-MPPI consistently outperforms both the switching strategy and the classic MPPI, regardless of the number of samples used. Moreover, the results indicate that including ancillary controllers in the proposed Biased-MPPI vastly improves the sampling efficiency, requiring fewer samples for better performance and enhancing the algorithm's robustness to model uncertainties.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Simulated Motion Planning Experiments", "weight": 1.0} -->

Interaction-Aware (IA) MPPI is a decentralized communication-free motion planning method that predicts short-term goals of other agents with a constant velocity model and, under homogeneity and rationality assumptions, each agent simultaneously plans and predicts motions for all agents. In its cost function, IA-MPPI encourages adherence to navigation rules, such as giving the right-of-way to agents from the right and preferring the right-hand side during head-on encounters. We will investigate the effects of biasing its sampling scheme with ancillary controllers. The agents are vessels modeled using Roboat's model. Controllers run at $10Hz$, plan $T_{H} = 100$ steps ahead ($10s$), with $\Sigma_{s} = {diag{(6,{\ 6},{\ 0.12},{\ 0.12})}}$, $\eta_{min} = 5$ and $\eta_{max} = 10$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-A Solving an Intersection", "weight": 1.0} -->

(a) Using a classical MPPI sampling scheme, the agents remain in a local minimum where both want to pass first, resulting in a collision.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-A Solving an Intersection", "weight": 1.0} -->

(b) Using the proposed Biased-IA-MPPI, the orange agent gives way to the blue agent as soon as it is clear that both agents want to cross.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-A Solving an Intersection", "weight": 1.0} -->

An issue that can arise with classical MPPI formulation, which only takes samples around what was previously considered to be optimal, is the difficulty, once in one, of jumping out of local minima. This is particularly evident in IA-MPPI, especially in a crossing scenario. In this experiment, depicted in Fig. 5, two identical vessels start with zero velocity and have to cross each other's paths. In their cost function, described in previous work, the decentralized and communication-free IA-MPPI is encouraged to get each of the vessels across the intersection while being penalized for not yielding to the agent coming from the right-hand side.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-A1 Ancillary Controllers", "weight": 1.0} -->

To help switch out of local minima and improve sampling efficiency, four ancillary controllers are sampled using the proposed Biased-MPPI.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Go-Slow", "weight": 1.0} -->

a sequence of inputs commanding a small amount of thrust to the vessel's side thrusters.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Go-to-Goal", "weight": 1.0} -->

computes a velocity reference that takes each vessel towards its corresponding local goal at each time step of the planning horizon.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Go-to-Goal", "weight": 1.0} -->

The velocity references proposed by the Braking and Go-to-Goal maneuvers are converted to input thrusts with a linear $\mathcal{H}_{\infty}$ controller, which is robust to model non-linearities, designed using the `musyn` command in Matlab.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-A2 Results", "weight": 1.0} -->

With an initial velocity of zero, each agent anticipates an unobstructed intersection crossing. This expectation is based on a constant velocity prediction, as they assume the opposing agent will remain stationary. In Fig. 5(a), the classic IA-MPPI fails to switch from planning to cross first to a slower maneuver that yields since all of the samples are taken around the previous plan, leading to a collision. In Fig. 5(b), our Biased-IA-MPPI approach can swiftly switch between modes when it becomes evident that the vessel with the right-of-way will cross the intersection.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-A2 Results", "weight": 1.0} -->

In Table I, we see that in 50 experiments, our Biased-IA-MPPI achieves zero collisions and rule violations for any number of samples, compared to the IA-MPPI based on the classical MPPI sampling scheme, which results in several. Thanks to the ancillary controllers, our Biased-IA-MPPI also travels straight to the goal, reducing the distance traveled. While our Biased-IA-MPPI has a lower variance in arrival times, it is not always faster on average. This confirms the results proved in 12, i.e. the Braking and Go-Slow maneuvers are biasing towards a slower trajectory.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-B Interaction-Aware Planning with Four Vessels", "weight": 1.0} -->

To further test Biased-IA-MPPI, we run 50 experiments with randomized initial conditions and goals, where four agents have to navigate in cooperation in the Herengracht, an urban canal in Amsterdam, challenging due to its narrow sections under two bridges. The canal map and an example of successful navigation are shown in Fig. 6.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-B1 Ancillary Controllers", "weight": 1.0} -->

We use all of the ancillary controllers described in Section V-A1. Additionally, we use a learning-based trajectory prediction model adapted and trained for urban vessels. However, we do not use this model for predictions. We track the trajectories it provides with an $\mathcal{H}_{\infty}$ controller to generate input sequences, which Biased-MPPI can consider in its sampling scheme.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-B2 Results", "weight": 1.0} -->

In Table II, results from 50 experiments show that with 50 samples, our Biased-IA-MPPI is cautious, leading to 10 deadlocks, possibly biased by the Braking maneuver. In contrast, the conventional IA-MPPI approach, without the ancillary controller, results in 16 collisions.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-B2 Results", "weight": 1.0} -->

As the number of samples increases, the bias from the ancillary controllers diminishes, causing Biased-IA-MPPI to behave less conservatively. Consequently, the number of deadlocks approaches zero, but a few collisions may occur. With both methods, over half of the successful experiments incur at least a rule violation. In these crowded scenes, violations are common, e.g., not stopping to yield to an agent with priority when it is still relatively far away. Still, in both collision counts and the number of experiments resulting in rule violations, our Biased-IA-MPPI consistently outperforms IA-MPPI using the traditional sampling method.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-B2 Results", "weight": 1.0} -->

Fig. 7 displays both methods' quartiles, min, max, and outliers of successful experiments. The ancillary controllers direct the sampling distribution towards lower-cost areas of the state space, significantly reducing travel distances. Despite this, as predicted by 12, Biased-IA-MPPI also exhibits a bias towards slightly slower movement due to "Braking" and "Go-Slow" maneuvers, resulting in similar travel times as the regular IA-MPPI.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Real-World Motion Planning Experiment", "weight": 1.0} -->

A Clearpath Jackal robot attempts to drive to a goal as fast as possible ($\sim {{2m}/s}$) while avoiding a box. Halfway through, the box is thrown in front of the robot. The position and the velocity of the box and the robot are estimated using information from a motion capture system. The velocity-controlled robot is modeled as a unicycle, and the box's position is propagated through the planning horizon using a constant velocity model. The cost function is defined as, where $p_{t,r}$, $p_{g}$ and $p_{t,b}$ are the position of the robot, the goal, and the box, respectively, at time $t$. Controllers run at $10Hz$, plan $T_{H} = 50$ steps ahead ($5s$), with $K = 300$ samples, covariance $\Sigma_{s} = {0.5 \cdot I_{2 \times 2}}$, $\eta_{min} = 5$ and $\eta_{max} = 10$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "VI-1 Ancillary Controllers", "weight": 1.0} -->

We sample a Braking maneuver, i.e., a zero velocity reference throughout the horizon.

<!-- chunk {"id": "body-0046", "role": "body", "section": "VI-2 Results", "weight": 1.0} -->

Fig. 8 shows the top 50 sampled trajectories sampled by (a), MPPI, and (b), our proposed Biased-MPPI. When the box is unexpectedly thrown in front of the robot, MPPI only samples trajectories that collide with the box. Given the cost function, MPPI prefers the samples that remain in collision for the least time. On the other hand, sampling also a zero velocity reference, Biased-MPPI quickly converges to a braking maneuver, avoiding the collision altogether. MPPI resulted in six collisions in over ten experiments, while Biased-MPPI resulted in none.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this paper, we have derived a sampling scheme for Model Predictive Path Integral (MPPI) control that removes computationally problematic terms and allows for the design of arbitrary sampling distributions as long as a bias in the solution is allowed. We proposed using classical and learning-based ancillary controllers for several control and motion planning experiments to bias the sampling distribution and achieve more efficient sampling and better performances. We demonstrated how the proposed algorithm can act as a control fusion scheme, taking suggestions from an arbitrary number of controllers and improving upon them. The resulting Biased-MPPI was shown to be better performing and more robust to model uncertainties compared to classical controllers and the baseline MPPI method, achieving faster swing-ups for a rotational inverted pendulum as well as safer, closer to optimal trajectories in interaction-aware motion planning experiments in constrained multi-agent environments, all while requiring less samples. The overall gains in safety, performance, and sample efficiency come at the expense of a potentially harmful bias, as shown with the sampling of Braking and Go-Slow maneuvers, which can result in slower trajectories. In the future, our approach could be employed as a potential solution to complex multi-modal problems.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusions", "weight": 1.0} -->

For example, a higher-level task planner could propose several ancillary controllers and alternative plans, which could all be sampled to achieve global solutions.
