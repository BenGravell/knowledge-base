## Introduction

Navigating autonomous robots through dense and dynamic environments poses a formidable challenge due to significant uncertainties, including the robot's state, model, environmental conditions, and interactions with other agents. Achieving desired behaviors under such conditions often necessitates using intricate cost functions and constraints, resulting in complex, nonlinear, non-convex, and occasionally discontinuous problem formulations. The dynamic nature of the environment introduces potential unexpected changes, demanding rapid adaptability in the robot's actions.

To address these challenges, one approach is to cast the problem in a stochastic optimal control setting, where they can be mathematically represented as stochastic Hamilton-Jacobi-Bellman (HJB) equations. However, solving these equations numerically can be challenging due to the curse of dimensionality. Pioneering work demonstrated that the stochastic HJB equations can be linearized for control-affine systems, and their solution can be approximated through sampling using the path integral formulation \[(https://arxiv.org/html/2401.09241v2#bib.bib1)\]. Implemented in a receding horizon fashion, Model Predictive Path Integral (MPPI) control \[(https://arxiv.org/html/2401.09241v2#bib.bib2), (https://arxiv.org/html/2401.09241v2#bib.bib3)\], and its Information-Theoretic counterpart \[(https://arxiv.org/html/2401.09241v2#bib.bib4), (https://arxiv.org/html/2401.09241v2#bib.bib5)\] have been initially used for racing a small-scale rally car. MPPI has also been successfully applied to several other planning problems, such as for autonomous vehicles with dynamic obstacles \[(https://arxiv.org/html/2401.09241v2#bib.bib6)\], solving games \[(https://arxiv.org/html/2401.09241v2#bib.bib7)\], flying drones in partially observable environments \[(https://arxiv.org/html/2401.09241v2#bib.bib8)\], performing complex maneuvers \[(https://arxiv.org/html/2401.09241v2#bib.bib9)\] and used in combination with adaptive control schemes \[(https://arxiv.org/html/2401.09241v2#bib.bib10)\]. It has also been adapted to multi-agent systems for formation flying \[(https://arxiv.org/html/2401.09241v2#bib.bib11)\], cooperative behavior \[(https://arxiv.org/html/2401.09241v2#bib.bib12)\], and simultaneous prediction and planning \[(https://arxiv.org/html/2401.09241v2#bib.bib13)\]. Furthermore, MPPI has shown promise in manipulating objects with robot arms\[(https://arxiv.org/html/2401.09241v2#bib.bib14)\] including model uncertainties \[(https://arxiv.org/html/2401.09241v2#bib.bib15)\], in pushing tasks \[(https://arxiv.org/html/2401.09241v2#bib.bib16), (https://arxiv.org/html/2401.09241v2#bib.bib17)\] and planning motion for four-legged walking robots \[(https://arxiv.org/html/2401.09241v2#bib.bib18)\]. MPPI is a model-based approach that requires a model to forward simulate trajectories given sampled inputs. Recent work has utilized physics engines to simulate samples \[(https://arxiv.org/html/2401.09241v2#bib.bib19), (https://arxiv.org/html/2401.09241v2#bib.bib20)\], eliminating the need for explicitly defining the dynamics of agents and the environment, thus providing a significant advantage in contact-rich manipulation tasks.

Figure 1: Top: Usually, MPPI only takes samples around a previous plan. Here, the environment changes unexpectedly, and all the sampled trajectories are in collision, which leads to computing a new plan that also collides. Bottom: our Biased-MPPI adds ancillary controllers to the sampling distribution, quickly converging to a collision avoidance maneuver.

One of the critical challenges in applying MPPI to dynamic environments is ensuring the algorithm's performance and reliability. The success of MPPI heavily relies on the choice of sampling distribution, which is crucial, especially in real-time scenarios. Most existing literature uses the previously computed input sequence as the mean of a Gaussian distribution for sampling \[(https://arxiv.org/html/2401.09241v2#bib.bib2)\], with the variance being tunable. However, using the previous input sequence may trap the algorithm in local minima. This can lead to catastrophic failures in the presence of unexpected disturbances or changes in the environment \[(https://arxiv.org/html/2401.09241v2#bib.bib21)\] ([Fig. 1](https://arxiv.org/html/2401.09241v2#S1.F1 "In I Introduction ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers")).

This paper explores the application of MPPI in dynamic environments, emphasizing the need to improve its performance and reliability in the face of unexpected disturbances and rapidly changing conditions.

### I-A Previous Work

Several works tried to make the method more efficient or more robust. Early work \[(https://arxiv.org/html/2401.09241v2#bib.bib22)\] proposed using Expectation Propagation instead of Monte Carlo sampling, demonstrating better efficiency in scenarios with hard constraints. Other works instead accelerate the convergence of MPPI by leveraging gradient descent updates \[(https://arxiv.org/html/2401.09241v2#bib.bib23)\]. Another option to be more reactive to environmental changes is to iteratively converge to a solution through adaptive importance sampling \[(https://arxiv.org/html/2401.09241v2#bib.bib24)\]. This, however, requires multiple iterations between each planning time step, diminishing the parallelizability of MPPI. Many other works propose improving the algorithm's convergence by somehow changing its sampling distribution. This can be done by substituting the Gaussian used for sampling with a different hand-crafted distribution \[(https://arxiv.org/html/2401.09241v2#bib.bib25)\] or by directly learning a distribution from data \[(https://arxiv.org/html/2401.09241v2#bib.bib26), (https://arxiv.org/html/2401.09241v2#bib.bib27)\]. Given that MPPI allows for tuning the variance of the sampling distribution \[(https://arxiv.org/html/2401.09241v2#bib.bib3)\], some works sought to improve the efficiency of the scheme by adapting the covariance online via covariance steering \[(https://arxiv.org/html/2401.09241v2#bib.bib28), (https://arxiv.org/html/2401.09241v2#bib.bib29)\]. Other ways to improve efficiency can be to fit splines to the sampled inputs \[(https://arxiv.org/html/2401.09241v2#bib.bib14)\] or to constrain the distribution to sample areas that are known to contain low-cost trajectories \[(https://arxiv.org/html/2401.09241v2#bib.bib18)\]. Previous works have also experimented with ancillary controllers. In \[(https://arxiv.org/html/2401.09241v2#bib.bib30)\], authors propose to sample inputs around a path previously computed by RRT. Other works instead robustify MPPI by switching to an iLQG controller \[(https://arxiv.org/html/2401.09241v2#bib.bib21)\] or by integrating one into the system's model \[(https://arxiv.org/html/2401.09241v2#bib.bib31)\]. Previous work also compares an MPPI that samples around a previously computed input, an input sequence computed by a sequential linear-quadratic MPC, and a learned sampling policy \[(https://arxiv.org/html/2401.09241v2#bib.bib18)\]. In general, however, the original derivations of MPPI \[(https://arxiv.org/html/2401.09241v2#bib.bib5)\] only allow samples to be drawn from a uni-modal Gaussian distribution, usually centered around the previous control sequence, which can hamper performance and reduce reactivity to unexpected changes in the environment.

### I-B Contributions

We propose a Biased-MPPI, for which we provide mathematical derivations that allow for arbitrary changes to the sampling distribution. We discuss the impact of introducing biases in the sampling distribution on the overall method. We experiment with an importance sampler that utilizes multiple classical and learning-based ancillary controllers simultaneously to take more informative samples, which can be seen as a control fusion scheme. Through simulated and real-world experiments, we demonstrate the impact of taking suggestions from several underlying controllers on robustness to model uncertainties and local minima, reactivity to unexpected events, and sampling efficiency.

## Preliminaries

In this section, we provide a concise introduction to the key concepts of MPPI within the Information-Theoretic framework. For more details, we direct the reader to prior research \[(https://arxiv.org/html/2401.09241v2#bib.bib5)\]. We begin by defining a function:

which we will denote as the free energy of the system. Here, $V$ represents a sequence of inputs, $\mathbb{P}$ is a base measure, $\lambda$ is a tuning parameter, $S{(V)}$ is a cost, and $x_{0}$ represents the system's initial state. It can be shown that:

Here, $\mathbb{Q}$ represents a probability measure that characterizes the controlled input distribution, and ${\mathbb{K}}{\mathbb{L}}{({\mathbb{Q}}||{\mathbb{P}})}$ denotes the KL-Divergence between the base measure and the controlled measure. (https://arxiv.org/html/2401.09241v2#S2.E2 "In II Preliminaries ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers") signifies that the free energy serves as a lower bound for the expected cost under the controlled distribution plus a control cost represented by the KL-Divergence. Hence, determining a control distribution that achieves this lower bound minimizes the expected cost and control cost. We can define a control distribution ${\mathbb{Q}}^{\ast}$ through its Radon-Nikodym derivative to the base measure:

Substituting $\mathbb{Q}$ with ${\mathbb{Q}}^{\ast}$ in (https://arxiv.org/html/2401.09241v2#S2.E2 "In II Preliminaries ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers"), we can prove that ${\mathbb{Q}}^{\ast}$ is an optimal control distribution in the sense that it achieves the lower bound. The idea is now to align our control distribution $\mathbb{Q}$ with the optimal distribution ${\mathbb{Q}}^{\ast}$ though KL minimization, which results in the optimal input sequence $U^{\ast}$:

Now, considering a discrete-time system:

Here, $x_{t} \in {\mathbb{R}}^{n}$ represents the state vector at time step $t$, $F{( \cdot )}$ is the state transition model, $v_{t} \in {\mathbb{R}}^{m}$ denotes the noisy input, $u_{t} \in {\mathbb{R}}^{m}$ is the commanded input, and $\Sigma$ corresponds to the natural input variance of the system. If $\mathbb{P}$ and $\mathbb{Q}$ are the uncontrolled and controlled measures, respectively, we can define them through their probability density functions:

It can be proven from (https://arxiv.org/html/2401.09241v2#S2.E4 "In II Preliminaries ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers") that the optimal control input at time $t$ is the mean input under the optimal distribution:

We can estimate such mean sampling from our controlled distribution via importance sampling:

with the importance sampling weight $\omega{(V)}$ being:

We can, therefore, sample $K$ noisy input sequences:

where $t$ is a time step and $T_{H}$ is the planning horizon. A practical choice often made in MPPI is to take $u_{t}$ as a time-shifted version of the previously computed approximation of the optimal control sequence. We roll out the sampled $V^{k}$ into state trajectories using the system's model $F{( \cdot )}$, evaluate their cost $S{(V)}$, compute the weights $\omega{(V)}$, get a new estimate of the optimal input sequence $U^{\ast}$ via (https://arxiv.org/html/2401.09241v2#S2.E7 "In II Preliminaries ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers") and iterate. In LABEL:eq::original_weight, the control cost is multiplied and divided by $\lambda$. Not having control over the magnitude of the terms at the exponential can cause numerical issues. A change of base measure $\mathbb{P}$ can solve the problem \[(https://arxiv.org/html/2401.09241v2#bib.bib5)\]. One might also need a higher variance $\Sigma_{s}$ for sampling compared to the natural variance of the system $\Sigma$ \[(https://arxiv.org/html/2401.09241v2#bib.bib32)\]. This again introduces terms at the exponential independent from $\lambda$. Moreover, introducing an arbitrary, potentially multi-modal sampling distribution ${\mathbb{Q}}_{s}$ is difficult. All these issues stem from the ratio ${{p{(v)}}/q}{(\left. V \middle| U \right.)}$ in LABEL:eq::original_weight. Our approach addresses this by showing that accepting a bias in the solution can eliminate the ratio and allow for arbitrary sampling distributions.

## Proposed Approach

### III-A Biased-MPPI

Let us first redefine the cost function as:

We then define the free-energy with this new cost:

where, as in \[(https://arxiv.org/html/2401.09241v2#bib.bib5)\], we applied Jensen's inequality. We can simplify the right-hand side as follows:

The free energy inequality is then:

Thus, while we start with $\overset{\sim}{S}{(V)}$, the free energy serves as a lower bound for the expected original cost $S{(V)}$ under the controlled distribution plus lambda times the KL-Divergence between the controlled and sampling distribution. An optimal control distribution achieving the lower bound would minimize the original cost $S{(V)}$ while pushing the controlled distribution to align with the sampling distribution, effectively introducing a bias toward the sampling distribution. We define a controlled distribution ${\mathbb{Q}}^{\ast}$ as:

Under ${\mathbb{Q}}^{\ast}$, the KL-Divergence becomes:

Substituting into (https://arxiv.org/html/2401.09241v2#S3.E12 "In III-A Biased-MPPI ‣ III Proposed Approach ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers") and simplifying leads to:

This proves that ${\mathbb{Q}}^{\ast}$ is the optimal distribution in that it achieves the lower bound in (https://arxiv.org/html/2401.09241v2#S3.E12 "In III-A Biased-MPPI ‣ III Proposed Approach ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers"). Following the steps in \[(https://arxiv.org/html/2401.09241v2#bib.bib5)\], we can align our controlled distribution $\mathbb{Q}$ to ${\mathbb{Q}}^{\ast}$ as in (https://arxiv.org/html/2401.09241v2#S2.E6 "In II Preliminaries ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers"), except we can now use our sampling distribution:

with importance sampling weights:

Note that our change of cost (https://arxiv.org/html/2401.09241v2#S3.E10 "In III-A Biased-MPPI ‣ III Proposed Approach ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers") resulted in the optimal control being biased towards the sampling distribution, as shown in (https://arxiv.org/html/2401.09241v2#S3.E12 "In III-A Biased-MPPI ‣ III Proposed Approach ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers"). However, this simplified the weights $\omega{(V)}$ and allowed us to design arbitrary sampling distributions ${\mathbb{Q}}_{s}$. In \[(https://arxiv.org/html/2401.09241v2#bib.bib5)\], $S{(V)}$ was defined as the state-dependent cost. However, this restriction was made to relate the approach to path integral control \[(https://arxiv.org/html/2401.09241v2#bib.bib1)\]. Such relation was only shown exactly when $\mathbb{P}$ is the distribution induced by an uncontrolled continuous-time control-affine system. This restriction is not required in the Information-Theoretic framework, which allows for a larger class of systems, and one can add input costs in S(V).

### III-B Sampling from Ancillary Controllers

There are several ways one could design an arbitrary sampling distribution. This paper focuses on taking most samples around a previously computed input distribution and some samples from hand-crafted policies.

In particular, we design a set of task-specific ancillary controllers, these being, e.g., open-loop motion primitives, reference tracking feedback controllers, or learning-based strategies to propose $J$ input sequences $U^{j} = {\lbrack u_{0}^{j},u_{1}^{j},\ldots,u_{t}^{j},\ldots,u_{T_{H}}^{j}\rbrack}$. These ancillary controllers are described for each experiment in [Sections IV](https://arxiv.org/html/2401.09241v2#S4 "IV Illustrative Experiment ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers") and [V](https://arxiv.org/html/2401.09241v2#S5 "V Simulated Motion Planning Experiments ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers"). We then choose the K sampled input sequences $V_{s}^{k}$ as,

meaning that, at each time step, we take one sample from each of the $J$ ancillary controllers, and the remaining $K - J$ samples are taken according to the classical MPPI strategy.

### III-C Autotuning the Inverse Temperature

As in \[(https://arxiv.org/html/2401.09241v2#bib.bib20)\] and similarly to \[(https://arxiv.org/html/2401.09241v2#bib.bib18)\], we autotune the inverse temperature $\lambda$ online based on the normalization factor $\eta$.

In all experiments, this can roughly keep the number of samples with a significant weight between $\eta_{min}$ and $\eta_{max}$.

## Illustrative Experiment

We apply our Biased-MPPI to a rotary inverted pendulum \[(https://arxiv.org/html/2401.09241v2#bib.bib33)\] ([Fig. 2](https://arxiv.org/html/2401.09241v2#S4.F2 "In IV Illustrative Experiment ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers")) in simulation to visualize its main features.

Figure 2: Left, Quanser Qube-Servo, and right, its diagram. The arm’s rotation, θ, is the actuated angle. The angle between the pendulum and the upright position, α, is not actuated.

Figure 3: Input and state evolution during a pendulum experiment with Biased-MPPI. We show the samples taken and the resulting planned input sequence over the planning horizon for three instances. While we sample all ancillary controllers in each instance, we highlight the one with the most influence on the planned input sequence.

### IV-A Swing-up and tracking

Starting at the bottom equilibrium with $\theta_{0} = 0$ and $\alpha_{0} = \pi$, the task is to swing up the pendulum to $\alpha_{r} = 0$ while keeping the arm close to $\theta_{r} = 1$. Thus, the running cost is:

The system has dynamics ${x{({t + 1})}} = {F{({x{(t)}},{u{(t)}})}}$, where the state of the system at time-step $t$ is denoted as ${x{(t)}} = {\lbrack\theta_{t},\alpha_{t},\overset{˙}{\theta_{t}},\overset{˙}{\alpha_{t}}\rbrack}^{T}$, and $u$ represents the system's input. The nonlinear model is derived from the Lagrange equations. To design linear controllers, the model is linearized at the top equilibrium using Euler-Lagrange's method \[(https://arxiv.org/html/2401.09241v2#bib.bib34)\]. To showcase resilience against model uncertainties, the parameters of the simulation's pendulum model are multiplied by $1 + \gamma$ in each experiment, where $\gamma \sim {\mathcal{N}{(0,0.05)}}$. The seed is consistent across methods. The system is dicretized and controllers run at $50Hz$, the controller plans $T_{H} = 50$ steps ahead ($1s$), covariance $\Sigma_{s} = 0.5$, $\eta_{min} = 2$ and $\eta_{max} = 5$.

### IV-A1 Ancillary Controllers

We design three ancillary controllers as a baseline and to guide the sampling strategy.

### Linear Quadratic Regulator (LQR)

designed using the `lqr` command in Matlab, stabilizes the pendulum at the top equilibrium.

### Linear Quadratic Integral (LQI)

tracks the reference $\theta_{r}$ while maintaining the pendulum at the top equilibrium. It is synthesized with the `lqi` command in Matlab.

### A nonlinear Energy-Based Controller (EBC)

is designed as in \[(https://arxiv.org/html/2401.09241v2#bib.bib34)\] to swing up the pendulum to the top equilibrium by increasing the potential energy of the system \[(https://arxiv.org/html/2401.09241v2#bib.bib35)\].

### IV-A2 Switching Controller

We introduce as baseline a switching strategy (https://arxiv.org/html/2401.09241v2#S4.E18 "In IV-A2 Switching Controller ‣ IV-A Swing-up and tracking ‣ IV Illustrative Experiment ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers") that combines all ancillary controllers. It swings up the pendulum using the input from the ECB, $u_{ebc}$, until $\alpha$ is within $\alpha_{catch} = 0.2$ of the top equilibrium. The LQR controller, with $u_{lqr}$, then stabilizes the pendulum. Once the pendulum is close to the top equilibrium ($\alpha_{track} = 0.05$) with angular velocity below ${\overset{˙}{\alpha}}_{track} = 0.1$ rad/s, the LQI, with $u_{lqi}$, is engaged for reference tracking.

### IV-A3 Results

[Fig. 3](https://arxiv.org/html/2401.09241v2#S4.F3 "In IV Illustrative Experiment ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers") depicts a pendulum experiment's input and state evolution with Biased-MPPI, also showcasing the samples taken and the ancillary controllers' influence on the plan. At the beginning of the experiment, ECB rapidly swings up the pendulum, heavily influencing Biased-MPPI's planned input. Once near equilibrium, LQR provides a stabilizing sequence, closely tracked by Biased-MPPI. As stability is achieved, LQI suggests an input sequence swiftly bringing the arm towards the reference, albeit with high velocities. Hence, Biased-MPPI, while influenced by LQI, opts for a lower amplitude input sequence due to cost function (https://arxiv.org/html/2401.09241v2#S4.E17 "In IV-A Swing-up and tracking ‣ IV Illustrative Experiment ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers").

[Fig. 4](https://arxiv.org/html/2401.09241v2#S4.F4 "In IV-A3 Results ‣ IV-A Swing-up and tracking ‣ IV Illustrative Experiment ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers") displays the distribution of total costs, defined as $\sum_{t = 0}^{T_{end}}{C_{p}{({x{(t)}})}}$ where $T_{end} = 250$ ($5s$) is the end of the episode, and the distribution of total efforts, defined as $\sum_{t = 0}^{T_{end}}{|{u{(t)}}|}$, across 50 experiments. Biased-MPPI consistently outperforms both the switching strategy and the classic MPPI, regardless of the number of samples used. Moreover, the results indicate that including ancillary controllers in the proposed Biased-MPPI vastly improves the sampling efficiency, requiring fewer samples for better performance and enhancing the algorithm's robustness to model uncertainties.

Figure 4: Total cost and control effort over 50 pendulum swing-ups with randomized model parameters.

## Simulated Motion Planning Experiments

Interaction-Aware (IA) MPPI \[(https://arxiv.org/html/2401.09241v2#bib.bib13)\] is a decentralized communication-free motion planning method that predicts short-term goals of other agents with a constant velocity model and, under homogeneity and rationality assumptions, each agent simultaneously plans and predicts motions for all agents. In its cost function, IA-MPPI encourages adherence to navigation rules, such as giving the right-of-way to agents from the right and preferring the right-hand side during head-on encounters. We will investigate the effects of biasing its sampling scheme with ancillary controllers. The agents are vessels modeled using Roboat's model \[(https://arxiv.org/html/2401.09241v2#bib.bib36)\]. Controllers run at $10Hz$, plan $T_{H} = 100$ steps ahead ($10s$), with $\Sigma_{s} = {diag{(6,{\ 6},{\ 0.12},{\ 0.12})}}$, $\eta_{min} = 5$ and $\eta_{max} = 10$.

### V-A Solving an Intersection

(a) Using a classical MPPI sampling scheme, the agents remain in a local minimum where both want to pass first, resulting in a collision.

(b) Using the proposed Biased-IA-MPPI, the orange agent gives way to the blue agent as soon as it is clear that both agents want to cross.

Figure 5: Two vessels cross each other’s path while penalized when not giving the right-of-way to agents coming from their right. The large circles are the agents’ true local goals extracted from a global path. IA-MPPI is decentralized and communication-free, so the small dots are the goals vessels estimate of one another using constant velocity. The trajectories in blue are those the blue agent has planned for itself and predicted for the other, and the same goes for the orange agent.

An issue that can arise with classical MPPI formulation, which only takes samples around what was previously considered to be optimal, is the difficulty, once in one, of jumping out of local minima. This is particularly evident in IA-MPPI, especially in a crossing scenario. In this experiment, depicted in [Fig. 5](https://arxiv.org/html/2401.09241v2#S5.F5 "In V-A Solving an Intersection ‣ V Simulated Motion Planning Experiments ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers"), two identical vessels start with zero velocity and have to cross each other's paths. In their cost function, described in previous work \[(https://arxiv.org/html/2401.09241v2#bib.bib13)\], the decentralized and communication-free IA-MPPI is encouraged to get each of the vessels across the intersection while being penalized for not yielding to the agent coming from the right-hand side.

### V-A1 Ancillary Controllers

To help switch out of local minima and improve sampling efficiency, four ancillary controllers are sampled using the proposed Biased-MPPI.

### Go-Slow

a sequence of inputs commanding a small amount of thrust to the vessel's side thrusters.

### Go-Fast

commands a large thrust.

### Braking

gives a zero velocity reference.

### Go-to-Goal

computes a velocity reference that takes each vessel towards its corresponding local goal at each time step of the planning horizon.

The velocity references proposed by the Braking and Go-to-Goal maneuvers are converted to input thrusts with a linear $\mathcal{H}_{\infty}$ controller, which is robust to model non-linearities, designed using the `musyn` command in Matlab.

### V-A2 Results

With an initial velocity of zero, each agent anticipates an unobstructed intersection crossing. This expectation is based on a constant velocity prediction, as they assume the opposing agent will remain stationary. In [Fig. 5(a)](https://arxiv.org/html/2401.09241v2#S5.F5.sf1 "In Fig. 5 ‣ V-A Solving an Intersection ‣ V Simulated Motion Planning Experiments ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers"), the classic IA-MPPI fails to switch from planning to cross first to a slower maneuver that yields since all of the samples are taken around the previous plan, leading to a collision. In [Fig. 5(b)](https://arxiv.org/html/2401.09241v2#S5.F5.sf2 "In Fig. 5 ‣ V-A Solving an Intersection ‣ V Simulated Motion Planning Experiments ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers"), our Biased-IA-MPPI approach can swiftly switch between modes when it becomes evident that the vessel with the right-of-way will cross the intersection.

In [Table I](https://arxiv.org/html/2401.09241v2#S5.T1 "In V-A2 Results ‣ V-A Solving an Intersection ‣ V Simulated Motion Planning Experiments ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers"), we see that in 50 experiments, our Biased-IA-MPPI achieves zero collisions and rule violations for any number of samples, compared to the IA-MPPI based on the classical MPPI sampling scheme, which results in several. Thanks to the ancillary controllers, our Biased-IA-MPPI also travels straight to the goal, reducing the distance traveled. While our Biased-IA-MPPI has a lower variance in arrival times, it is not always faster on average. This confirms the results proved in (https://arxiv.org/html/2401.09241v2#S3.E12 "In III-A Biased-MPPI ‣ III Proposed Approach ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers"), i.e. the Braking and Go-Slow maneuvers are biasing towards a slower trajectory.

TABLE I: Results of 50 crossings for an increasing number of samples K. Metrics are reported for successful runs.

### V-B Interaction-Aware Planning with Four Vessels

To further test Biased-IA-MPPI, we run 50 experiments with randomized initial conditions and goals, where four agents have to navigate in cooperation in the Herengracht, an urban canal in Amsterdam, challenging due to its narrow sections under two bridges. The canal map and an example of successful navigation are shown in [Fig. 6](https://arxiv.org/html/2401.09241v2#S5.F6 "In V-B2 Results ‣ V-B Interaction-Aware Planning with Four Vessels ‣ V Simulated Motion Planning Experiments ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers").

### V-B1 Ancillary Controllers

We use all of the ancillary controllers described in [Section V-A1](https://arxiv.org/html/2401.09241v2#S5.SS1.SSS1 "V-A1 Ancillary Controllers ‣ V-A Solving an Intersection ‣ V Simulated Motion Planning Experiments ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers"). Additionally, we use a learning-based trajectory prediction model adapted and trained for urban vessels \[(https://arxiv.org/html/2401.09241v2#bib.bib37)\]. However, we do not use this model for predictions. We track the trajectories it provides with an $\mathcal{H}_{\infty}$ controller to generate input sequences, which Biased-MPPI can consider in its sampling scheme.

### V-B2 Results

In [Table II](https://arxiv.org/html/2401.09241v2#S5.T2 "In V-B2 Results ‣ V-B Interaction-Aware Planning with Four Vessels ‣ V Simulated Motion Planning Experiments ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers"), results from 50 experiments show that with 50 samples, our Biased-IA-MPPI is cautious, leading to 10 deadlocks, possibly biased by the Braking maneuver. In contrast, the conventional IA-MPPI approach, without the ancillary controller, results in 16 collisions.

Figure 6: Four agents navigating in the Herengracht. Video.

TABLE II: Results for 50 runs of four-agent experiments in the Herengracht with randomized initial conditions and goals for an increasing number of samples K.

As the number of samples increases, the bias from the ancillary controllers diminishes, causing Biased-IA-MPPI to behave less conservatively. Consequently, the number of deadlocks approaches zero, but a few collisions may occur. With both methods, over half of the successful experiments incur at least a rule violation. In these crowded scenes, violations are common, e.g., not stopping to yield to an agent with priority when it is still relatively far away. Still, in both collision counts and the number of experiments resulting in rule violations, our Biased-IA-MPPI consistently outperforms IA-MPPI using the traditional sampling method.

Figure 7: Agents’ traveled distance and travel time over 50 experiments in the Herengracht. Metrics are reported for experiments that were successful with both methods.

[Fig. 7](https://arxiv.org/html/2401.09241v2#S5.F7 "In V-B2 Results ‣ V-B Interaction-Aware Planning with Four Vessels ‣ V Simulated Motion Planning Experiments ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers") displays both methods' quartiles, min, max, and outliers of successful experiments. The ancillary controllers direct the sampling distribution towards lower-cost areas of the state space, significantly reducing travel distances. Despite this, as predicted by (https://arxiv.org/html/2401.09241v2#S3.E12 "In III-A Biased-MPPI ‣ III Proposed Approach ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers"), Biased-IA-MPPI also exhibits a bias towards slightly slower movement due to "Braking" and "Go-Slow" maneuvers, resulting in similar travel times as the regular IA-MPPI.

## Real-World Motion Planning Experiment

A Clearpath Jackal robot attempts to drive to a goal as fast as possible ($\sim {{2m}/s}$) while avoiding a box. Halfway through, the box is thrown in front of the robot. The position and the velocity of the box and the robot are estimated using information from a motion capture system. The velocity-controlled robot is modeled as a unicycle, and the box's position is propagated through the planning horizon using a constant velocity model. The cost function is defined as,

where $p_{t,r}$, $p_{g}$ and $p_{t,b}$ are the position of the robot, the goal, and the box, respectively, at time $t$. Controllers run at $10Hz$, plan $T_{H} = 50$ steps ahead ($5s$), with $K = 300$ samples, covariance $\Sigma_{s} = {0.5 \cdot I_{2 \times 2}}$, $\eta_{min} = 5$ and $\eta_{max} = 10$.

Figure 8: Visualized are the top 50 sampled trajectories, color-graded by their cost. (a) Classic MPPI is about to crash. (b) Our Biased-MPPI avoids collision. See video.

### VI-1 Ancillary Controllers

We sample a Braking maneuver, i.e., a zero velocity reference throughout the horizon.

### VI-2 Results

[Fig. 8](https://arxiv.org/html/2401.09241v2#S6.F8 "In VI Real-World Motion Planning Experiment ‣ Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers") shows the top 50 sampled trajectories sampled by (a), MPPI, and (b), our proposed Biased-MPPI. When the box is unexpectedly thrown in front of the robot, MPPI only samples trajectories that collide with the box. Given the cost function, MPPI prefers the samples that remain in collision for the least time. On the other hand, sampling also a zero velocity reference, Biased-MPPI quickly converges to a braking maneuver, avoiding the collision altogether. MPPI resulted in six collisions in over ten experiments, while Biased-MPPI resulted in none.

## Conclusions

In this paper, we have derived a sampling scheme for Model Predictive Path Integral (MPPI) control that removes computationally problematic terms and allows for the design of arbitrary sampling distributions as long as a bias in the solution is allowed. We proposed using classical and learning-based ancillary controllers for several control and motion planning experiments to bias the sampling distribution and achieve more efficient sampling and better performances. We demonstrated how the proposed algorithm can act as a control fusion scheme, taking suggestions from an arbitrary number of controllers and improving upon them. The resulting Biased-MPPI was shown to be better performing and more robust to model uncertainties compared to classical controllers and the baseline MPPI method, achieving faster swing-ups for a rotational inverted pendulum as well as safer, closer to optimal trajectories in interaction-aware motion planning experiments in constrained multi-agent environments, all while requiring less samples. The overall gains in safety, performance, and sample efficiency come at the expense of a potentially harmful bias, as shown with the sampling of Braking and Go-Slow maneuvers, which can result in slower trajectories. In the future, our approach could be employed as a potential solution to complex multi-modal problems. For example, a higher-level task planner could propose several ancillary controllers and alternative plans, which could all be sampled to achieve global solutions.
