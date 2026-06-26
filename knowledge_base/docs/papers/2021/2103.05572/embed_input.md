<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Risk-Averse RRT* Planning with Nonlinear Steering and Tracking Controllers for Nonlinear Robotic Systems under Uncertainty

Topics include Nonlinear systems, Uncertain systems, Robotics, Tracking control, Nonlinear programming, Model predictive control, Reference trajectory, Multiplicative noise, Linear quadratic regulator, Safe planning, Risk-averse, Rapidly-exploring random tree.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Assembles a motion planning and control architecture that focuses on mitigating the effect of stochastic disturbances by modeling and accounting for it explicitly in both the planner and the controller, performing uncertainty propagation between the planner-controller interface to ensure alignment numerically. Trajectory optimization using a generic nonlinear programming solver is used as the local steering function inside the RRT, which gives high quality trajectories, but is very expensive at runtime. Useful empirical comparison between vanilla LQR, the multiplicative-noise-as-robustified-LQR-design methodology described in 2004.08019, and full high-powered NMPC tracking control in a more realistic and sophisticated post-perception stack.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a two-phase risk-averse architecture for controlling stochastic nonlinear robotic systems. We present Risk-Averse Nonlinear Steering RRT* (RANS-RRT*) as an RRT* variant that incorporates nonlinear dynamics by solving a nonlinear program (NLP) and accounts for risk by approximating the state distribution and performing a distributionally robust (DR) collision check to promote safe planning. The generated plan is used as a reference for a low-level tracking controller. We demonstrate three controllers: finite horizon linear quadratic regulator (LQR) with linearized dynamics around the reference trajectory, LQR with robustness-promoting multiplicative noise terms, and a nonlinear model predictive control law (NMPC). We demonstrate the effectiveness of our algorithm using unicycle dynamics under heavy-tailed Laplace process noise in a cluttered environment.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Safe deployment of mobile robots in uncertain dynamic environments, such as urban streets and crowded airspaces, requires a systematic accounting of various risks, both within and across layers in an autonomy stack. These autonomy stacks are naturally partitioned into a hierarchy of i) a high-level planner which generates a reference trajectory (often) offline before system operation, and ii) a low-level controller whose purpose is to track the reference trajectory in an online fashion and incorporate feedback to mitigate the effect of disturbances. The survey examines several approaches for motion planning and control of autonomous ground vehicles and suggests two additional upper layers in the hierarchy, namely route planning and behavioral decision-making. In this paper, we assume such route plans and behavioral decisions are encapsulated by the motion planning and control problems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many motion planning algorithms have been developed under deterministic settings and assume linear robot dynamics in order to simplify their analysis and design. However, in practice, robotic systems are inherently both nonlinear and stochastic in nature due to external disturbances and noisy onboard sensors. In the presence of model uncertainty or process noise, the resulting trajectory is only a nominal reference and there are no guarantees of its safety. To account for the stochastic components and to provide probabilistic guarantees, motion planning under uncertainty has been considered in several lines of recent research. Specifically, risk-aware motion planning algorithms for linear robot dynamics were developed recently using CVaR- and Wasserstein metric- based formulations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A chance-constrained version of RRT and RRT\* respectively were proposed, where chance constraints were used to encode the risk of constraint violation to provide probabilistic feasibility guarantees for robots with linear dynamics under additive uncertainties. On the other hand, these approaches made questionable assumptions of Gaussianity for system uncertainties ostensibly to maintain computational tractability. It was shown in that such assumptions can lead to significant miscalculations of risk, and hence moment-based ambiguity sets were formulated to propose a distributionally robust variant of RRT called DR-RRT. This approach was extended in to design an asymptotically optimal RRT\* using output feedback with linear quadratic regulator and Kalman filter-based state estimation. Here we take a first step towards designing risk-aware nonlinear steering-based motion plans for nonlinear robotic systems. This is closely aligned with the problem addressed by authors. A low-level tracking controller is implemented to successfully track a given reference trajectory in the presence of uncertain process disturbances. In this work, we assume perfect state estimates are available and consider full-state feedback controllers.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The linear-quadratic regulator (LQR) controller being the most common can be obtained through dynamic programming where a quadratic cost involving state deviation and control effort is minimized. The LQR controller can further be generalized to achieve robust stability under parametric model uncertainties by designing it to mean-square stabilize the system with the inclusion of multiplicative noises as described in (LQRm). However, both LQR controllers cannot handle state and input constraints. On the other hand, NMPC explicitly considers both state and input constraints. The authors in used the nonlinear model-predictive control (NMPC) to track the LQR-RRT\* trajectory to make up for linearization error. By contrast, we use NMPC to track a risk-averse RRT\* trajectory generated by a nonlinear program (NLP)-based steering function which much more closely resembles the low-level NMPC controller.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present RANS-RRT\*, a new sampling-based motion planner for nonlinear robotic systems which constructs dynamically feasible trajectories that satisfy distributionally robust state constraints to promote safety.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate our proposed approach on unicycle dynamics under heavy-tailed Laplace process noise in a cluttered environment. We provide a comparative study of the collision-avoidance rate, state deviation and control costs, and computational expense of three low-level reference tracking controllers i) LQR, ii) LQRm and iii) NMPC, across a range of disturbance strengths, through Monte Carlo simulations.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows. The notation, preliminaries and problem formulations are presented in §Notations, Preliminaries & Problem Formulation. The proposed nonlinear dynamics-based high level motion planner is elucidated in §II. Low-level tracking controllers are described in §III. Simulation results are reported and analyzed in §IV. Finally, the paper is closed in §V along with directions for future research.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Notations, Preliminaries & Problem Formulation", "weight": 1.0} -->

The set of real numbers and natural numbers are denoted by ${\mathbb{R}},{\mathbb{N}}$ respectively. The subset of natural numbers between ${a,b} \in {\mathbb{N}}$ with $a < b$ is denoted by $\lbrack{a:b}\rbrack$. The operator $\backslash$ denotes set subtraction and $\mid C\mid$ denotes the cardinality of the set $C$. An identity matrix in dimension $n$ is denoted by $I_{n}$. The operator ${( \cdot )}^{c}$ denotes the set complement.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-A Environment and Obstacles Specification", "weight": 1.0} -->

Consider a robot in an environment $\mathcal{X} \subseteq {\mathbb{R}}^{n}$ with static obstacles. It is expected to navigate the environment $\mathcal{X}$ while safely avoiding obstacles at all times. We denote the set of all obstacles by $\mathcal{B}$ with ${|\mathcal{B}|} = F > 0$. The environment and obstacles (assumed disjoint) are convex polytopes and hence can each be represented as a conjunction of halfspace constraints. The space occupied by the $i^{th}$ obstacle in $\mathcal{B}$ is denoted $\mathcal{O}_{i}$. The union of the space occupied by all obstacles is $\mathcal{C}:={\cup_{i = 1}^{F}\mathcal{O}_{i}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-A Environment and Obstacles Specification", "weight": 1.0} -->

Hence the free space in the environment is given by For a given deterministic state $s \in {\mathbb{R}}^{n}$, the condition for collision avoidance with all obstacles is where each individual obstacle avoidance constraint can be expressed as and the condition for collision avoidance with the environment bounds is where $n_{ob_{i}}$ are the number of constraints for obstacle $\mathcal{O}_{i}$ and $n_{env}$ are those of the environment. The total number of constraints is denoted $n_{total} = {n_{env} + {\sum_{i = 1}^{F}n_{ob_{i}}}}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-B Robot System Dynamics", "weight": 1.0} -->

For all time instances $k \in {\mathbb{N}}$, we model the robot as a discrete-time nonlinear dynamical system given: where ${{x,w} \in {\mathbb{R}}^{n}},{u \in {\mathbb{R}}^{m}}$ are the system state, additive disturbance, and control input, respectively, at the time step indexed in the brackets, $x_{0} \in {\mathbb{R}}^{n}$ is the initial state, and $f:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}^{n}}$ is the robot dynamics that represents the nonlinear transformation. The disturbances $w{\lbrack k\rbrack}$ are assumed independent and identically distributed according to some prescribed distribution ${\mathbb{P}}_{k}^{w} \sim {(0,\Sigma_{k}^{w})}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "I-C Unscented Transformation and Moment Estimation", "weight": 1.0} -->

The unscented transformation (UT) can be used to estimate the statistics of a random variable which undergoes a nonlinear transformation. An ensemble of ${2n} + 1$ samples called sigma points are generated deterministically and propagated individually through the nonlinear transformation to yield an ensemble of transformed sigma points. The weighted statistics of the transformed sigma points approximate the statistics of the transformed random variable. Though parameters that generate the sigma points can be tailored for specific distributions, there is no pre-defined set of rules that work in general for all distributions. For a discrete-time nonlinear robot system as, we can use the UT to estimate the mean and covariance of the next state given the current one.

<!-- chunk {"id": "body-0016", "role": "body", "section": "I-C Unscented Transformation and Moment Estimation", "weight": 1.0} -->

To do so, the ensemble of ${2n} + 1$ sigma points are obtained as follows where ${(\sqrt{{({n + \lambda})}\Sigma_{x}{\lbrack{k - 1}\rbrack}})}_{i}$ is the $i^{th}$ row or column of the matrix $\sqrt{{({n + \lambda})}\Sigma_{x}{\lbrack{k - 1}\rbrack}}$ obtained through Cholesky decomposition. Then, the weights below are used to scale $\chi_{i}{\lbrack k\rbrack}$ in the estimation of the mean and covariance $\lambda = {{{\hat{\alpha}}^{2}{({n + \kappa})}} - n}$ is a scaling parameter where $\hat{\alpha},\hat{\beta},\kappa$ are used to tune the unscented transformation.

<!-- chunk {"id": "body-0017", "role": "body", "section": "I-C Unscented Transformation and Moment Estimation", "weight": 1.0} -->

Usually $\hat{\beta} = 2$ is a good choice for Gaussian uncertainties, $\kappa = {3 - n}$ is a good choice for $\kappa$, and $0 \leq \hat{\alpha} \leq 1$ is an appropriate choice for $\hat{\alpha}$, where a larger value for $\hat{\alpha}$ spreads the sigma points further from the mean. Using the above-obtained sigma points and the weights defined, the estimated mean and covariance of the random variable $x{\lbrack k\rbrack}$ under the dynamics, assuming Gaussian noise $w$, are computed as follows.

<!-- chunk {"id": "body-0018", "role": "body", "section": "I-D Moment-Based Ambiguity Set for The State Distribution", "weight": 1.0} -->

The state ${x{\lbrack k\rbrack}{\forall k}} \in {\mathbb{N}}_{> 0}$ is a random vector. The state $x{\lbrack{k - 1}\rbrack}$, under input $u{\lbrack{k - 1}\rbrack}$ and the noise $w{\lbrack{k - 1}\rbrack}$, evolves to $x{\lbrack k\rbrack}$. Due to the difficulty in estimating the distribution of a random variable under a nonlinear transformation, we will assume that a state $x{\lbrack k\rbrack}$ belongs to an unknown distribution ${\mathbb{P}}_{k}^{x}$. Since we can estimate its first two moments, we can consider a moment-based ambiguity set $\mathcal{P}_{k}^{x}$ with the estimated moments. This will guarantee robustness to errors in propagating the state distribution due to the nonlinear dynamics.

<!-- chunk {"id": "body-0019", "role": "body", "section": "I-D Moment-Based Ambiguity Set for The State Distribution", "weight": 1.0} -->

It can also provide robustness to moment estimation errors. The mean and covariance we consider for the ambiguity set are the ones we estimate through the UT and thus we get the following estimate for the ambiguity set: For Gaussian inputs, the above moment estimates from UT are accurate up to the third-order approximation and for the case of non-Gaussian, the approximations are accurate to at least the second-order as described.

<!-- chunk {"id": "body-0020", "role": "body", "section": "I-E Nonlinear Motion Planning Problem", "weight": 1.0} -->

The planning problem provides a high-level solution that can then be used by low-level tracking controllers. This plan can be computed offline and requires finding an optimal reference trajectory that satisfies the robot dynamics, state and input constraints, and risk constraints. In this work, we consider the following planning problem.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The risk constraint (6. ‣ I-E Nonlinear Motion Planning Problem ‣ Notations, Preliminaries & Problem Formulation ‣ Risk-Averse RRT* Planning with Nonlinear Steering and Tracking Controllers for Nonlinear Robotic Systems Under Uncertainty")) is infinite dimensional and generally non-convex which makes solving this problem a challenge.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 1", "weight": 1.0} -->

To understand the stage risk constraints (6. ‣ I-E Nonlinear Motion Planning Problem ‣ Notations, Preliminaries & Problem Formulation ‣ Risk-Averse RRT* Planning with Nonlinear Steering and Tracking Controllers for Nonlinear Robotic Systems Under Uncertainty")) in the context of trajectory safety, let $P^{S}$ denote the event that plan $P$ succeeds and $P^{F}$ be the complementary event (i.e. failure). Consider the specification that a plan succeeds with high probability ${{{\mathbb{P}}{(P^{S})}} \geq {1 - \beta}},{\beta \in {\lbrack 0,0.5\rbrack}}$ or equivalently that it fails with low probability ${{\mathbb{P}}{(P^{F})}} \leq \beta$. Failure requires at least one stage risk constraints to be violated.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Using the fact that and applying Boole's law, the probability of the success event can be lower bounded as follows: If the stage risks $\forall k \in {\lbrack 0:T\rbrack}$ are equal, meaning $\alpha_{k} = \alpha$, then $\beta = {{({T + 1})}\alpha}$. Furthermore, if the stage risk $\alpha_{k} = \alpha$ is equally distributed over all $n_{total}$ constraints, then, the risk bound for a single constraint is $\alpha/n_{total}$ and the risk bound for a single obstacle $\mathcal{O}_{i}$ (or the environment $\mathcal{X}$) is ${\alphan_{ob_{i}}}/n_{total}$ (or ${\alphan_{env}}/n_{total}$) (this will be discussed more in §II-C).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 2", "weight": 1.0} -->

In general, $T$ may not be known ahead of time. For sampling-based planners, $T$ depends on the random nodes sampled. In such cases, an upper bound can be used $T_{max} \geq T$. The choices of $T_{max}$, the risk bound on the plan's failure $\beta$, and the risk budget allocation across time steps and constraints are design parameters. Alternatively, it is also possible to build up the risk bounds from the individual constraints into a risk bound on the whole plan.

<!-- chunk {"id": "body-0025", "role": "body", "section": "I-F Nonlinear Reference Trajectory Tracking Problem", "weight": 1.0} -->

Given a reference trajectory $\overline{x}{\lbrack k\rbrack}$ for $k \in {\lbrack 0:T\rbrack}$ generated by the high-level motion planner, the reference tracking problem involves minimizing deviations of the state $x{\lbrack k\rbrack}$ from the reference state $\overline{x}{\lbrack k\rbrack}$ subject to the nonlinear dynamics and realizations of all system uncertainties. This problem is formally presented below.

<!-- chunk {"id": "body-0026", "role": "body", "section": "High Level Planner: RANS-RRT\\*", "weight": 1.0} -->

The high-level planner finds an optimal (or approximately optimal) plan for the low-level controller to execute. If the plan gets close to obstacles, tracking might fail due to process noise. By incorporating uncertainty in the high-level planner, a more conservative, but safe, trajectory is designed. In this work, we present an approximate solution to the problem in Definition 1. ‣ I-E Nonlinear Motion Planning Problem ‣ Notations, Preliminaries & Problem Formulation ‣ Risk-Averse RRT* Planning with Nonlinear Steering and Tracking Controllers for Nonlinear Robotic Systems Under Uncertainty") using rapidly exploring random trees. We propose RANS-RRT\*: a Risk-Averse, Nonlinear Steering RRT\* planner. Below, we discuss: 1) the NLP problem used to steer between tree nodes, 2) the mean and covariance propagation along such a trajectory segment, 3) the treatment of uncertainty and risk, 4) the RANS-RRT\* algorithm, and 5) a trajectory shortening post-processing step.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-A NLP Steering", "weight": 1.0} -->

Our RANS-RRT\* algorithm employs a nonlinear steering law to compute a trajectory $\mathcal{T}$ of length $N$ consisting of state and input pairs $\mathcal{T} = \left\{ {(s_{0},u_{0})},\ldots,{(s_{N},u_{N})} \right\}$ that drive an initial state $s_{init}$ to a final one $s_{des}$. The first state belongs to the RANS-RRT\* tree $\mathcal{T}$ and the other is either a sampled state or another tree state. NLP steering is defined below.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-B Mean and Covariance Propagation", "weight": 1.0} -->

NLP steering returns the trajectory $\mathcal{T} = \left\{ {(s_{0},u_{0})},\ldots,{(s_{N - 1},u_{N - 1})},{(s_{N})} \right\}$. To use this in the RANS-RRT\* tree $\mathcal{T}$, as a trajectory between two nodes, we need the mean state, covariance of the state, and control law. Since the dynamics are nonlinear and the NMPC control policy is the solution of a constrained optimization problem without an explicit form as a function of the state, it is extremely challenging to incorporate the NMPC feedback law into the RANS-RRT\* trajectories. As such, we use the open-loop controls of the NLP trajectory $\mathcal{T}$. As a byproduct, we also require the mean states in the RANS-RRT\* trajectory to match the states of the NLP trajectory $\mathcal{T}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-B Mean and Covariance Propagation", "weight": 1.0} -->

With the mean states and inputs fixed according to $\mathcal{T}$, we only need to estimate the covariance at the mean states. To do so, we use the UT with the NLP controls and match the UT mean states with the NLP states. This returns covariances associated with every state that are used in enforcing risk bounds.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-C Risk Treatment", "weight": 1.0} -->

Consider a mean state and covariance pair in the RANS-RRT\* trajectories $({\hat{x}{\lbrack k\rbrack}},{\hat{\Sigma}{\lbrack k\rbrack}})$. The risk constraint associate with this time step has the form Since $\mathcal{C}$ is a union of the obstacle sets, we use Boole's law to get: We allocate the risk bound equally among the constraints by setting the risk bound for being in $\mathcal{O}_{i}$ to ${\alpha_{k}n_{ob_{i}}}/n_{total}$ and that of not being in the environment to ${\alpha_{k}n_{env}}/n_{total}$. Thus: and hence, the desired risk constraint is enforced.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-C Risk Treatment", "weight": 1.0} -->

k\rbrack}}} > b_{{env},j}}$ we can apply Boole's to and get Thus, bound is satisfied if As, we have the following: where follows from the Fréchet-Boole lower bound.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-C Risk Treatment", "weight": 1.0} -->

We then have the following result: which holds as $n_{ob_{i}} \geq 1$, i.e. by enforcing the left-hand-side, the right-hand-side (desired constraint) is guaranteed. Therefore, (6. ‣ I-E Nonlinear Motion Planning Problem ‣ Notations, Preliminaries & Problem Formulation ‣ Risk-Averse RRT* Planning with Nonlinear Steering and Tracking Controllers for Nonlinear Robotic Systems Under Uncertainty")) is satisfied if Using \[3, Theorem 3.1\]

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-D Algorithm", "weight": 1.0} -->

RANS-RRT\* is presented in Algorithm 1. The free space is first sampled and the tree is initialized with the initial state (the root of the tree) and the initial covariance of zero (lines 1-1). Then the sampled states $x_{samples}$ are traversed. For every state $S \in x_{samples}$, the nearest node in the tree $S_{nearest} \in \mathcal{T}$ is found (line 1). If the distance between $S$ and $S_{nearest}$ is larger than some threshold, a closer state $S_{lim}$ is returned along the same direction (line 1). In line 1, NLP steering is performed to find a trajectory from $S_{nearest}$ to $S_{lim}$ within the steering horizon $N$. If steering fails, the sample is skipped. Else, a RANS-RRT\* trajectory (mean states, covariances, and inputs) is returned. In line 1, the trajectory is checked for collisions.

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-D Algorithm", "weight": 1.0} -->

A collision is detected if any of the risk-tightened constraints are violated at any of the mean states, in which case the sample is skipped. If safe, the trajectory may be added to the tree after checking nearby nodes for a more optimal trajectory as done in RRT\* (line 1). Then, the trajectory is added to the tree (line 1) and $\mathcal{T}$ undergoes the RRT\* rewiring set (line 1). Note that the rewire step also uses the same steering and collision check functions described before. When an optimal trajectory is queried, the trajectory with the smallest total NLP steering cost (output cost of Definition 3. ‣ II-A NLP Steering ‣ II High Level Planner: RANS-RRT* ‣ Risk-Averse RRT* Planning with Nonlinear Steering and Tracking Controllers for Nonlinear Robotic Systems Under Uncertainty")) is returned.

<!-- chunk {"id": "body-0035", "role": "body", "section": "II-D Algorithm", "weight": 1.0} -->

Result: RANS-RRT* Tree 𝒯 Algorithm 1 RANS-RRT* - Tree Expansion

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 3", "weight": 1.0} -->

RANS-RRT\* only *approximately* solves the problem in Definition 1. ‣ I-E Nonlinear Motion Planning Problem ‣ Notations, Preliminaries & Problem Formulation ‣ Risk-Averse RRT* Planning with Nonlinear Steering and Tracking Controllers for Nonlinear Robotic Systems Under Uncertainty") because 1) the risk treatment step *approximately* solves the infinite-dimensional constraint (6. ‣ I-E Nonlinear Motion Planning Problem ‣ Notations, Preliminaries & Problem Formulation ‣ Risk-Averse RRT* Planning with Nonlinear Steering and Tracking Controllers for Nonlinear Robotic Systems Under Uncertainty")), 2) the covariance estimation step using UT is *imperfect* for non-Gaussian distributions, and 3) the covariance propagation assumes the estimated means and NLP means *coincide*, which is used to keep the problem tractable. Hence, we do not make any formal risk-bound guarantees. Nonetheless, as we will see in the experimental results section, the padding added to obstacles through the DR collision check step makes the algorithm significantly robust to disturbances.

<!-- chunk {"id": "body-0037", "role": "body", "section": "II-E Post-Processing: Trajectory Shortening", "weight": 1.0} -->

In the RANS-RRT\* algorithm, the horizon $N$ used for solving the NLP steering problem is fixed. This is done to obtaining a decision on whether a trajectory exists between two nodes after solving one NLP problem. Ideally, we would want to solve the NLP steering problem with the shortest steering horizon. However, this is not trivial and might involve solving the steering problem with an increasing horizon after each failure (up to a certain upper bound). Since the NLP steering problem is computationally expensive, repeating the process would quickly make the problem intractable. To that end, we set the NLP steering horizon to a constant value $N:=N_{hl}$ during RANS-RRT\* but perform a post-processing trajectory-shortening step to the optimal trajectory.

<!-- chunk {"id": "body-0038", "role": "body", "section": "II-E Post-Processing: Trajectory Shortening", "weight": 1.0} -->

The post-processing step considers each trajectory $traj_{k}$ between two RANS-RRT\* nodes and obtains a new NLP steering trajectory by solving the problem in Definition 3. ‣ II-A NLP Steering ‣ II High Level Planner: RANS-RRT* ‣ Risk-Averse RRT* Planning with Nonlinear Steering and Tracking Controllers for Nonlinear Robotic Systems Under Uncertainty") for a different steering horizon $N$. $N$ is initially set to a small estimated value (which we assign based on the trajectory length and the robot dynamics). If NLP steering fails, $N$ is incremented $N = {N + 1}$ and the process is repeated while $N < N_{hl}$ (at which point the original trajectory is used). If a trajectory is found, the same covariance propagation and DR collision-avoidance steps as done in RANS-RRT\* are performed. If the DR checks fail, $N$ is incremented and the process continues. If they succeed, the RANS-RRT\* trajectory is updated with the shorter one.

<!-- chunk {"id": "body-0039", "role": "body", "section": "II-E Post-Processing: Trajectory Shortening", "weight": 1.0} -->

We observed significantly shorter trajectories after performing this step. Furthermore, since the trajectory time is fixed based on the trajectory steering horizon ($t = {N\Deltat}$ where $\Deltat$ is the discrete-time step), RANS-RRT\* trajectories have fixed duration regardless of the distance between nodes (causing slow and fast trajectories) whereas the shortened trajectories have different times leading to smoother trajectories.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Tracking Controllers", "weight": 1.0} -->

The low-level problem in Definition 2. ‣ I-F Nonlinear Reference Trajectory Tracking Problem ‣ Notations, Preliminaries & Problem Formulation ‣ Risk-Averse RRT* Planning with Nonlinear Steering and Tracking Controllers for Nonlinear Robotic Systems Under Uncertainty") was specified as the evaluation criterion of performance of the tracking controllers. However, our tracking controllers do not exactly solve the low-level problem in Definition 2. ‣ I-F Nonlinear Reference Trajectory Tracking Problem ‣ Notations, Preliminaries & Problem Formulation ‣ Risk-Averse RRT* Planning with Nonlinear Steering and Tracking Controllers for Nonlinear Robotic Systems Under Uncertainty"), but instead approximately solve it using established control design methodologies. Compared with Definition 2. ‣ I-F Nonlinear Reference Trajectory Tracking Problem ‣ Notations, Preliminaries & Problem Formulation ‣ Risk-Averse RRT* Planning with Nonlinear Steering and Tracking Controllers for Nonlinear Robotic Systems Under Uncertainty"), the proposed tracking controllers make the following approximations. The LQR and LQRm controllers assume dynamics are linearized about the reference trajectory (so only holds approximately), and the input constraint (5.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Tracking Controllers", "weight": 1.0} -->

‣ I-E Nonlinear Motion Planning Problem ‣ Notations, Preliminaries & Problem Formulation ‣ Risk-Averse RRT* Planning with Nonlinear Steering and Tracking Controllers for Nonlinear Robotic Systems Under Uncertainty")) is ignored. LQRm attempts to mitigate the effects of linearization error by treating the model errors as multiplicative noise. NMPC solves an optimal control problem more similar to the one in Definition 2. ‣ I-F Nonlinear Reference Trajectory Tracking Problem ‣ Notations, Preliminaries & Problem Formulation ‣ Risk-Averse RRT* Planning with Nonlinear Steering and Tracking Controllers for Nonlinear Robotic Systems Under Uncertainty"), but the finite horizon $T$ is generally shorter and the effect of the process noise (4. ‣ I-E Nonlinear Motion Planning Problem ‣ Notations, Preliminaries & Problem Formulation ‣ Risk-Averse RRT* Planning with Nonlinear Steering and Tracking Controllers for Nonlinear Robotic Systems Under Uncertainty")) is ignored by replacing the stochastic dynamics with their expectation. Furthermore, we chose to add a state constraint that requires the nominal state to be in the environment $\mathcal{X}$. Details of the control design techniques are given throughout the remainder of this section for completeness.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Tracking Controllers", "weight": 1.0} -->

In all low-level controllers we use identical low-level cost functions. This facilitates a fair comparison between controllers, as the same objective is approximately optimized. We use stage costs which are quadratic in the state deviation and input: where ${\delta_{x}{\lbrack k\rbrack}} = {{x{\lbrack k\rbrack}} - {\overline{x}{\lbrack k\rbrack}}}$ and the penalty matrices $Q{\lbrack k\rbrack}$ and $R{\lbrack k\rbrack}$ are symmetric positive definite for all $k$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-A Robot dynamics", "weight": 1.0} -->

We consider the problem of navigating a robot with unicycle dynamics from an initial state to a final set of states.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-A Robot dynamics", "weight": 1.0} -->

The discrete-time unicycle nonlinear dynamics obtained through forward-Euler discretization of the corresponding continuous-time dynamics are given: where ${{p_{x}{\lbrack k\rbrack}},{p_{y}{\lbrack k\rbrack}}} \in {\mathbb{R}}$ are the horizontal and vertical positions of the robot, ${\theta{\lbrack k\rbrack}} \in {\mathbb{R}}$ is the heading of the robot relative to the $x$-axis of an assigned world frame, ${{\nu{\lbrack k\rbrack}},{\omega{\lbrack k\rbrack}}} \in {\mathbb{R}}$ are the linear and angular velocity control inputs, and ${w_{x}{\lbrack k\rbrack}},{w_{y}{\lbrack k\rbrack}},{w_{\theta}{\lbrack k\rbrack}}$ are the

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-A Robot dynamics", "weight": 1.0} -->

disturbances affecting each state, all expressed at timestamp $k$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-A Robot dynamics", "weight": 1.0} -->

The quantity $\Deltat$ is the sampling time in seconds between any two timestamps $k,{k + 1}$. With short-hand notations the dynamics in (III-A) and corresponding Jacobians can be written in the compact form as

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-B Generalized linear-quadratic control", "weight": 1.0} -->

In this subsection we propose and derive the solution to a generalized linear-quadratic control problem (LQP), which will be useful in the sequel. Consider the following finite-horizon stochastic dynamic game: with linear dynamics and quadratic stage costs where the expectation is with respect to the random variables which are distributed as where $\mathcal{D}{(0,X)}$ is any distribution with mean zero and covariance $X$, and the random variables ${x{\lbrack 0\rbrack}},{\{{w{\lbrack k\rbrack}},{\alpha{\lbrack k\rbrack}},{\beta{\lbrack k\rbrack}},{\gamma{\lbrack k\rbrack}}\}}_{k = 0}^{T - 1}$ are assumed statistically independent.

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-B Generalized linear-quadratic control", "weight": 1.0} -->

The variables have the following meanings: ${x{\lbrack k\rbrack}} \in {\mathbb{R}}^{n}$ is the state, ${u{\lbrack k\rbrack}} \in {\mathbb{R}}^{m}$ is a control input, ${v{\lbrack k\rbrack}} \in {\mathbb{R}}^{c}$ is an adversarial input, ${z{\lbrack k\rbrack}} \in {\mathbb{R}}^{p}$ is an exogenous signal, and ${w{\lbrack k\rbrack}} \in {\mathbb{R}}^{d}$ is a disturbance. This formulation allows the policies to be shaped by the exogenous signal $z$ and its interaction with the state $x$ and inputs $u$ and $v$; specifically, in the sequel we will choose $z$ to be the concatenated reference state and input trajectory.

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-B Generalized linear-quadratic control", "weight": 1.0} -->

The matrices ${E{\lbrack k\rbrack}} \in {\mathbb{R}}^{n \times d}$ specify how the additive disturbance $w{\lbrack k\rbrack}$ enters the dynamics.

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-B Generalized linear-quadratic control", "weight": 1.0} -->

The matrices ${G{\lbrack k\rbrack}} \in {\mathbb{R}}^{{({n + m + c + p})} \times {({n + m + c + p})}}$ are assumed to satisfy block semidefiniteness conditions that make the stage costs $g{\lbrack k\rbrack}{({x{\lbrack k\rbrack}},{u{\lbrack k\rbrack}},{v{\lbrack k\rbrack}},{z{\lbrack k\rbrack}})}$ convex in the state $x{\lbrack k\rbrack}$, control input $u{\lbrack k\rbrack}$, and exogenous signal $z{\lbrack k\rbrack}$, and concave in the adversarial input $v{\lbrack k\rbrack}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-B Generalized linear-quadratic control", "weight": 1.0} -->

The matrices $G{\lbrack k\rbrack}$ specify quadratic cost weights for each state, control input, adversarial input, and exogenous signal. Notice that the stage costs $g{\lbrack k\rbrack}$ and dynamics $f{\lbrack k\rbrack}$ in the LQP are different from those used in the high-level planner, i.e. $g_{hl}{\lbrack k\rbrack}$ and $f_{hl}{\lbrack k\rbrack}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-B Generalized linear-quadratic control", "weight": 1.0} -->

Optimal policies can be computed from optimal cost functions via dynamic programming backwards in time. The initial cost function is i.e. a convex quadratic polynomial of $x{\lbrack T\rbrack}$. The subsequent cost functions are found via the dynamic programming equation: where $\mathcal{Q}{\lbrack k\rbrack}$ is the state-action cost function where expectation is with respect to ${w{\lbrack k\rbrack}},{\alpha{\lbrack k\rbrack}},{\beta{\lbrack k\rbrack}},{\gamma{\lbrack k\rbrack}}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "III-B Generalized linear-quadratic control", "weight": 1.0} -->

We will show that if the current cost function $J{\lbrack{k + 1}\rbrack}{(x)}$ is quadratic in $x$, i.e. has the form then the prior cost function $J{\lbrack k\rbrack}{(x)}$ is also quadratic in $x$, i.e. and we will provide the explicit relation between $P{\lbrack k\rbrack}$, $q{\lbrack k\rbrack}$, $r{\lbrack k\rbrack}$ and $P{\lbrack{k + 1}\rbrack}$, $q{\lbrack{k + 1}\rbrack}$, $r{\lbrack{k + 1}\rbrack}$, which will also be needed to compute the optimal policies.

<!-- chunk {"id": "body-0054", "role": "body", "section": "III-B Generalized linear-quadratic control", "weight": 1.0} -->

Then, arguing by induction and noting that by assumption the terminal cost function $J{\lbrack T\rbrack}{(x)}$ is quadratic in $x$, all cost functions until $k = 0$ are quadratic in $x$ with the same form.

<!-- chunk {"id": "body-0055", "role": "body", "section": "III-B Generalized linear-quadratic control", "weight": 1.0} -->

We begin by evaluating the state-action cost function using the assumption that $J{\lbrack{k + 1}\rbrack}{(x)}$ is quadratic in $x$: To ease notation, for the following development we will drop the indices $\lbrack k\rbrack$ and $\lbrack{k + 1}\rbrack$, so where the last step follows by the zero mean and independence assumptions on the relevant random variables. Since $\mathcal{Q}{(x,u,v,z)}$ is convex in $u$, the minimum with respect to $u$ is found when the gradient with respect to $u$ is equal to 0: Likewise, since $\mathcal{Q}{(x,u,v,z)}$ is concave in $v$, the maximum with respect to $v$ is found when the gradient with respect to $v$ is equal to 0: Rewrite the expressions for $u$ and $v$ as Now we decouple the expressions for $u$ and $v$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "III-B Generalized linear-quadratic control", "weight": 1.0} -->

First substitute into to obtain where the gains are defined as An analogous calculation for $v$ yields where the gains are defined as Substituting the optimal input into the state-action cost function, we obtain the optimal cost function Grouping terms in quadratic, linear, and constant quantities of the state, we find indeed that $J{\lbrack k\rbrack}{(x)}$ is a convex quadratic of the state, i.e.

<!-- chunk {"id": "body-0057", "role": "body", "section": "III-B Generalized linear-quadratic control", "weight": 1.0} -->

Notice that the control policies do not depend on the scalar part of the cost $r{\lbrack k\rbrack}$ or the noise covariance $W{\lbrack k\rbrack}$, so it is not strictly necessary to compute $r{\lbrack k\rbrack}$ or require specification of $E{\lbrack k\rbrack}$, $W{\lbrack k\rbrack}$ for the purpose of control.

<!-- chunk {"id": "body-0058", "role": "body", "section": "III-B Generalized linear-quadratic control", "weight": 1.0} -->

Thus, we have Algorithm 2 to solve the generalized linear quadratic optimal control problem.

<!-- chunk {"id": "body-0059", "role": "body", "section": "III-C Tracking with Linear Controller", "weight": 1.0} -->

In order to apply optimal linear control, we linearize the discrete-time nonlinear dynamics about various operating points in the joint state-input space. From this section, we notate $f = f_{hl}$. A first-order Taylor series approximation of $f{(x,u,w)}$ evaluated at the operating point ($\overline{x},\overline{u},\overline{w}$) is The low-level controller receives a reference trajectory, a sequence of states, inputs and disturbances, from the high-level planner, denoted as ${\{{({\overline{x}{\lbrack k\rbrack}},{\overline{u}{\lbrack k\rbrack}},{\overline{w}{\lbrack k\rbrack}})}\}}_{k = 0}^{T}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "III-C Tracking with Linear Controller", "weight": 1.0} -->

The low-level controller will use these as the operating points about which to linearize the dynamics, i.e. will assume the dynamics We will also assume that the reference trajectory satisfies the nonlinear dynamics constraint, i.e.

<!-- chunk {"id": "body-0061", "role": "body", "section": "III-C Tracking with Linear Controller", "weight": 1.0} -->

Using this assumption, the dynamics in simplify to Defining the state-, input-, and disturbance-deviation variables the dynamics in can be rewritten as which is clearly seen as linear time-varying dynamics in the deviation variables.

<!-- chunk {"id": "body-0062", "role": "body", "section": "III-C Tracking with Linear Controller", "weight": 1.0} -->

We now define general stage costs which are quadratic in the state, input, deviation of state from reference state, and deviation of input from reference input: where ${Q{\lbrack k\rbrack}},{R{\lbrack k\rbrack}}$ are positive semidefinite matrices which penalize deviation of the state and input from the origin and ${Q_{\delta}{\lbrack k\rbrack}},{R_{\delta}{\lbrack k\rbrack}}$ are positive semidefinite matrices which penalize the deviation of the state and input from the reference.

<!-- chunk {"id": "body-0063", "role": "body", "section": "III-C Tracking with Linear Controller", "weight": 1.0} -->

We provide equations in this level of generality, but practically the most meaningful thing to do is set $Q = 0$ and $R_{\delta} = 0$; the former because keeping the robot near the (absolute) origin in state-space is contrary to our goals, and the latter because we really only care about the total control effort expended, which can be smaller than that used by the reference open-loop input sequence in the event that serendipitous disturbance realizations drive the robot towards the reference states "for free." Choosing the particular values for $Q_{\delta}$ and $R$ is a somewhat subjective task, but we will use diagonal and time-invariant matrices with "reasonable" values chosen that empirically give a good balance between reference tracking and control effort. We also make the assumption that the disturbance-deviations are independent, zero-mean and have covariance $W{\lbrack k\rbrack}$, i.e.

<!-- chunk {"id": "body-0064", "role": "body", "section": "III-C Tracking with Linear Controller", "weight": 1.0} -->

Using the linearized dynamics, the time-additive quadratic stage-costs, and the disturbance distribution assumption, we obtain the linear-quadratic optimal tracking problem We now show how to bring this tracking problem into the form of the generalized linear quadratic problem. First, it is clear that the dynamics and disturbance distribution have the required form already. Next, rewrite the state and input in terms of the deviations and references as so the stage cost can be expressed as Treating the concatenated reference state and input trajectory as an exogenous signal, i.e. the stage cost can be expressed as At this point we re-introduce the additional terms which promote robustness of the linearized controller, as discussed in Section III-B. We assume an additive adversary disturbance affects the state-deviation dynamics directly, as well as state-deviation- and input-deviation- and adversary-input-multiplicative noises. We will only consider a quadratic penalty on the adversary input characterized by symmetric positive definite matrix $S$. Thus, the robustified linear-quadratic tracking problem becomes which matches the required form of the stage costs. Thus, we can apply Algorithm 2 to compute the optimal policies.

<!-- chunk {"id": "body-0065", "role": "body", "section": "III-C Tracking with Linear Controller", "weight": 1.0} -->

At runtime, the control inputs are computed as which can again be interpreted as the summation of a closed-loop feedback term of the state-deviation and an open-loop feedforward term. As long as the state of the system remains close to the reference trajectory, the linearized dynamics will remain a good approximation and the linear controller will yield good reference tracking.

<!-- chunk {"id": "body-0066", "role": "body", "section": "III-E Robust LQR", "weight": 1.0} -->

We seek to promote robustness against errors in the state-space matrices due to linearization about states other than the reference trajectory, which occurs due to the process disturbance. Observing the Jacobians, only mis-specifications in heading $\theta$ change the entries. We assume that the heading deviation from reference is uniformly upper bounded as For the unicycle model, it is straightforward to construct appropriate 2D bounding boxes in the space of A and B matrices that fully contain every possible Jacobian. Consider the $1,1$- and $2,1$-entries of the $B$ matrix Through trigonometric relations depicted by Figure 1, we obtain the robustness regions where ${{c{\lbrack k\rbrack}} = {\cos{({\theta{\lbrack k\rbrack}})}}},{{s{\lbrack k\rbrack}} = {\sin{({\theta{\lbrack k\rbrack}})}}}$ and where the scales are bounded as Figure 1: Geometry of B matrices under linearization about various states.

<!-- chunk {"id": "body-0067", "role": "body", "section": "III-E Robust LQR", "weight": 1.0} -->

The thick circular arc segment is the locus of all possible B when θ is interval bounded. The shaded box represents the set of B on which the controller is designed to achieve low cost.

<!-- chunk {"id": "body-0068", "role": "body", "section": "III-E Robust LQR", "weight": 1.0} -->

Note that the robustness region is conservative as it extends in the $A_{2}$ and $B_{2}$ directions twice as far as strictly necessary. This is done merely as a matter of convenience so that the center of the robustness region remains at ($A{\lbrack k\rbrack}$, $B{\lbrack k\rbrack}$) regardless of $\delta\theta_{\max}$. It has been proved in that, in the infinite-horizon time-invariant setting, the inclusion of (fictitious) multiplicative noise in the control design induces robustness to static model perturbations in the same directions as the multiplicative noise. This inspires the inclusion of such multiplicative noises with variance and directions related to the desired robustness region over which we desire to minimize quadratic cost. We include the robust LQR in our comparison to demonstrate the benefit of our NMPC controller over a simpler robust control method.

<!-- chunk {"id": "body-0069", "role": "body", "section": "III-F NMPC", "weight": 1.0} -->

NMPC can be used to approximate the nonlinear optimal trajectory tracking problem. NMPC accomplishes that by reducing the problem into a sequence of open-loop optimization problems over a horizon $N_{ll}$ where after solving an NLP to track a reference trajectory, only the first input is applied and the horizon is shifted back. The NMPC tracking NLP is given below.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

RANS-RRT\* plans were generated on a machine with an Intel Core i7 6700K CPU and 16 of RAM. The low-level Monte Carlo simulations were performed on a machine with a Ryzen 7 2700X and 64GB of RAM. The NLP is modeled with CasADi Opti and solved with IPOPT. We showcase RANS-RRT\* in action in three different environments. Each environment consisted of a root node (white triangle), a goal area (dashed green rectangle), and a $10 \times 10$ environment with 4 rectangular obstacles for its sides (black boundary). Environments 1 and 3 (Figures 4(a) and 4(c)) have 5 rectangular obstacles (black rectangles) while environment 2 (Figure 4(b)) has only 3 such obstacles. The robot is assumed to occupy a single point. Its controls bounds are $\pm 0.5$ units/sec for linear velocity and $\pm \pi$rad/sec for angular velocity. The RANS-RRT\* steering horizon is $N = N_{hl} = 30$ and the NMPC planning horizon is $N_{ll} = 10$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

The discrete-time step was ${\Deltat} = 0.2$sec. The planner control cost matrix was ${R{\lbrack k\rbrack}} = {\text{diag}{({\lbrack 1,1\rbrack})}}$. The tracking (LQR, robust LQR, and NMPC) cost matrices were ${Q{\lbrack k\rbrack}} = {\text{diag}{({\lbrack 100,100,10\rbrack})}}$ and ${R{\lbrack k\rbrack}} = {\text{diag}{({\lbrack 1,1\rbrack})}}$ for all $k = {\lbrack 0:T - 1\rbrack}$, and ${Q{\lbrack T\rbrack}} = {10Q{\lbrack 0\rbrack}}$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

We used a high-level plan risk bound of $\beta = 0.1$. It is divided equally across the time steps $T_{max} = 1000$ and among the obstacle constraints. The process noise distribution ${\mathbb{P}}_{k}^{w}$ was taken as a multivariate Laplace distribution with zero mean and covariance $\Sigma^{w} = {{5 \cdot 10^{- 7}}I_{n}}$. The same variance was used for all states and is denoted by $\sigma_{w}^{2}:={5 \cdot 10^{- 7}}$. We also refer to this as the noise level. In the tracking step, we evaluated performance under different (greater) noise levels.

<!-- chunk {"id": "body-0073", "role": "body", "section": "IV-A RANS-RRT\\* Results", "weight": 1.0} -->

Constructing the RANS-RRT\* trees in Figures 4(a)-4(c) took 36, 23, and 28 minutes respectively. Each tree started with $2000$ randomly sampled nodes but only $1102$, $802$, and $865$ nodes were deemed feasible and safe and added to the trees, respectively. The RANS-RRT\* trajectories were conservative in the sense that they avoided getting too close to obstacles. Small gaps, such as to the right of the goal in Figure 4(c) or on the right side of the environment in Figure 4(b), were implicitly deemed too risky and avoided. On the other hand, a tree grown using the standard RRT\* in the same environment in Figure 4(d) discovered such risky gaps and thereby returned an unsafe (risky) trajectory. In fact, it is easy to see that the optimal path to the goal in Figure 4(d) scrapes by an obstacle and hence would result in a collisions even for small process noise.

<!-- chunk {"id": "body-0074", "role": "body", "section": "IV-B Low-Level Tracking Results", "weight": 1.0} -->

We used open-loop control and three low-level closed-loop controllers 1) LQR, 2) robust LQR, and 3) NMPC, to track a high-level trajectory in the environment shown in Figure 4(c) under realization of the Laplace noise. For each noise level, $1000$ Monte Carlo simulations were performed. The resulting trajectories are plotted in Figure 2. As expected, the noise level assumed for the high-level plan $\sigma_{w}^{2} = {5 \cdot 10^{- 7}}$ was insignificant: even open-loop control succeeded. However, as the noise level increased, open-loop control began to fail. At around $\sigma_{w}^{2} = 0.001$, the open-loop control almost always failed, while the other controllers almost always succeeded. From there, the feedback controllers began failing more frequently. Robust LQR did slightly better than LQR with fewer collisions for each noise level. Both were outperformed by NMPC which was better able to reject the more aggressive noise, leading to notably fewer collisions.

<!-- chunk {"id": "body-0075", "role": "body", "section": "IV-B Low-Level Tracking Results", "weight": 1.0} -->

The largest noise levels tested for which the plan failure risk bound of $10$ percent was satisfied were $0.003$ for LQR and robust LQR and $0.0035$ for NMPC. These are, respectively, $6000$ and $7000$ folds larger than the assumed noise covariance $\sigma_{w}^{2} = 0.0000005$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "IV-B Low-Level Tracking Results", "weight": 1.0} -->

For comparison, we ran the same experiment, but with the distributionally robust obstacle padding disabled. The planner returned trajectories which passed near obstacle boundaries, as shown in the tree in Figure 4(d), with realized trajectories plotted in Figures 8 and 7. Consequently, the reference trajectory itself was extremely unsafe, as evidenced by the high failure rates exhibited in Figure 3. Only at an extremely low noise level $\sigma_{w}^{2} = 0.0000005$ was NMPC able to reliably avoid collisions, while the LQR and LQRm controllers failed to do so. However with slightly more noise at the level $\sigma_{w}^{2} = 0.00001$, all control schemes led to significant probability of collision (greater than $35\%$). By contrast, the RANS-RRT\* reference trajectory was so safe that even open-loop control led to a low probability of collision (less than $10\%$) at this noise level $\sigma_{w}^{2} = 0.00001$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "IV-B Low-Level Tracking Results", "weight": 1.0} -->

This trend continued all the way up through the noise level $\sigma_{w}^{2} = 0.001$ with the probability of collision along the non-robust reference trajectory continuing to degrade, while the robust reference trajectory remained nearly perfectly safe with any of the low-level feedback controllers, thus demonstrating the clear benefit of RANS-RRT\* over vanilla RRT\*. Eventually the noise became too powerful and collisions became a near certainty regardless of the planner or controller used.

<!-- chunk {"id": "body-0078", "role": "body", "section": "IV-B Low-Level Tracking Results", "weight": 1.0} -->

In Figure 6 the realized trajectories obtained through the Monte Carlo simulations are plotted for $\sigma_{w}^{2} = 0.0035$. The performance metrics for $\sigma_{w}^{2} = 0.0000005$ and $\sigma_{w}^{2} = 0.0035$ are tabulated in Tables I and II respectively. We use the following metrics to evaluate the effectiveness of each tracking controller: The number of collisions: the number of Monte Carlo trials in which the realized trajectory collided with an obstacle.

<!-- chunk {"id": "body-0079", "role": "body", "section": "IV-B Low-Level Tracking Results", "weight": 1.0} -->

The average run time: the time taken to run the entire Monte Carlo trial, conditionally averaged across all collision-free trajectories, which is necessary as simulations terminate immediately upon collision.

<!-- chunk {"id": "body-0080", "role": "body", "section": "IV-B Low-Level Tracking Results", "weight": 1.0} -->

With $\sigma_{w}^{2} = 0.0000005$, the trajectory was short enough so that collisions did not occur even with purely open-loop control, although the trajectories began to diverge from the reference. The closed-loop controllers exhibited minimal state deviations, as reflected in the significantly lower average $\delta_{x}$ cost. The difference in $\delta_{x}$ and $u$ costs between each closed-loop controller was insignificant; since the state remained extremely close to the reference, the inputs generated by each controller were very similar.

<!-- chunk {"id": "body-0081", "role": "body", "section": "IV-B Low-Level Tracking Results", "weight": 1.0} -->

However with $\sigma_{w}^{2} = 0.0035$ as shown in Figure 6, the following observations were made. Almost all open-loop trajectories ended with collisions as shown in Figure 6(a). Compared to the standard LQR, robust LQR led to a lower number of collisions and state-deviation cost as shown in Figures 6(b), 6(c) but both were significantly outperformed by NMPC. NMPC trajectories generally remained closer to the reference than LQR or robust LQR along with lower number of collision as the robot moved through the corridor as shown in Figure 6(d). However, NMPC's closer reference tracking and collision-avoidance came at a price, as it used more control effort than LQR and robust LQR. Likewise, the more sophisticated computations involved in solving the NLPs in NMPC led to a longer average run time. It is evident that under both the noise settings, the NMPC outperforms other controllers in tracking the given reference trajectory to reach the goal with low failure rate and a better cost.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

We proposed a risk-averse control architecture tailored for safely controlling stochastic nonlinear robotic systems, which combines a novel nonlinear steering-based variant of RRT\* called RANS-RRT\* that accounts for risk by performing DR collision checks with low-level reference tracking controllers. We performed thorough numerical experiments using unicycle dynamics, compared three controllers, and observed better performance from NMPC than LQR variants. We showed that the despite the usage of very small noise level assumptions in the high-level planner, the low-level controllers performed well under moderate and aggressive disturbance realizations. Future research involves considering a full nonlinear sensor model while incorporating the exact DR risk constraints in the optimization problems of both the levels of autonomy stack for accurate risk assessment. We will also seek to decrease the computation time of NMPC through the usage of code generation tools.
