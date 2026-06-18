<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Deep Learning Warm Starts for Trajectory Optimization on the International Space Station

Topics include Optimal control, Trajectory optimization, Robotics, Safety, Neural networks, Deep learning, Real-time systems, Optimization, Control, Learning, ISS, Sequential convex programming, International space station.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Trajectory optimization is a cornerstone of modern robot autonomy, enabling systems to compute trajectories and controls in real-time while respecting safety and physical constraints. However, it has seen limited usage in spaceflight applications due to its heavy computational demands that exceed the capability of most flight computers. In this work, we provide results on the first in-space demonstration of using machine learning-based warm starts for accelerating trajectory optimization for the Astrobee free-flying robot onboard the International Space Station (ISS). We formulate a data-driven optimal control approach that trains a neural network to learn the structure of the trajectory generation problem being solved using sequential convex programming (SCP). Onboard, this trained neural network predicts solutions for the trajectory generation problem and relies on using the SCP solver to enforce safety constraints for the system. Our trained network reduces the number of solver iterations required for convergence in cases including rotational dynamics by 60% and in cases with obstacles drawn from the training distribution of the warm start model by 50%. This work represents a significant milestone in the use of learning-based control for spaceflight applications and a stepping stone for future advances in the use of machine learning for autonomous guidance, navigation, & control.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Trajectory generation is a hallmark problem of aerospace guidance, navigation, & control (GNC) and involves the computation of a state and control trajectory that satisfies system dynamics and mission operational constraints. Traditionally, trajectory generation for space systems is carried out with significant ground-in-the-loop involvement, where mission designers construct the trajectory using large-scale nonlinear programming \[Betts1998, Betts2010\] or primer-vector techniques \[HandelsmanLion1967, Russell2007\]. However, with the advent of a new era of spaceflight involving an increasing number of missions in cislunar space \[HolzingerChowEtAl2021\] and a burgeoning interest for in-space servicing capabilities, the current state-of-practice in trajectory generation for space systems falls short in fulfilling the needs of upcoming missions. In particular, there is a pressing need to be able to compute trajectories autonomously onboard spacecraft and allow for scaling to an increasing number of missions without incurring significant operational costs.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A key challenge in enabling onboard trajectory generation is that the nonlinear optimization algorithms used to formulate and solve these problems remain too computationally expensive for resource-constrained flight computers. Indeed, despite recent advances in embedded convex optimization solvers \[ErenPrachEtAl2017, LiuLuEtAl2017, MalyutaYuEtAl2021, MalyutaEtAl2022\], most practical problems of interest in spacecraft applications fall under the class of non-convex optimization problems for which finding solutions remains even more computationally expensive. In this work, we draw inspiration from data-driven optimal control, a nascent area of research that has emerged using machine learning to quickly synthesize solutions for the trajectory generation problem, to bridge this computational gap while providing the necessary safety guarantees for the system.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present experimental results on the use of data-driven optimal control for the Astrobee free-flying robot. The Astrobee robot is a guest science platform operating onboard the International Space Station \[BualatSmithEtAl2018\] and serves as a proving ground for new technologies developed for spacecraft robotic applications. The trajectory generation problem for Astrobee entails solving a highly non-convex optimization problem and for which a new class of trajectory optimization solvers using sequential convex programming (SCP) have emerged to successfully tackle. We showcase how data-driven optimal control techniques allow for the use of such SCP algorithms for real-time, onboard for generating trajectories that satisfy system constraints while safely avoiding obstacles.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Statement of Contributions: Our work presents experimental results from the first flight demonstration of data-driven optimal control used to generate trajectories for the Astrobee robot. We use the Guaranteed Sequential Trajectory Optimization (GuSTO) algorithm \[BonalliCauligiEtAl2019, BonalliBylardEtAl2019\] to solve the free-flyer trajectory optimization problem. We then train a neural network to learn the mapping between problem inputs and GuSTO-generated solutions. To create training data, we run GuSTO on randomized motion plans using a simulator of the International Space Station (ISS) and Astrobee dynamics. The trained neural network is integrated into the Astrobee flight software \[Astrobee\] and was tested during an experimental session on board the ISS on February 13, 2025.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide experimental results with the Astrobee free-flying robot conducted on the ISS in February 2025, which represents the first use of machine learning-based control in the ISS microgravity environment and, to the best of the authors' knowledge, for a free-flying robot.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our learned warm starts significantly reduce the number of solver iterations required for convergence in complex, non-convex planning tasks, including a 60% reduction in iterations required for convergence in scenarios involving rotational dynamics, and a 50% reduction in cases with obstacle configurations sampled from the warm start model's training distribution.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

As a result of these tests, we advance the Technology Readiness Level (TRL) of deep learning-based trajectory optimization from TRL-3 (experiments from ground based benchmarks) to TRL-5 (testing in a relevant environment).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Technical Background", "weight": 1.0} -->

0: Reference trajectory $\left( {\overline{\mathbf{x}}}^{0},{\overline{\mathbf{u}}}^{0} \right)$, Parameters Δ0 &gt; 0, ωmax &gt; ω0 ≥ 1, ε &gt; 0; Trust region scaling 0 &lt; βfail &lt; 1, βsucc &gt; 1, 0 &lt; ρ0 &lt; ρ1 &lt; 1, γfail &gt; 1 1: for k = 1, 2, …, Nmax,iter do 4: Compute model accuracy ratio ρk 10: $\Delta^{k + 1}\leftarrow\begin{cases} {\min\left( {\beta_{\text{succ}}\Delta^{k}},\Delta^{0} \right)} &amp; {{\text{if~}\rho^{k}} &lt; \rho^{0}} \\ \Delta^{k} &amp; \text{otherwise} 11: $\omega^{k +

<!-- chunk {"id": "body-0011", "role": "body", "section": "Technical Background", "weight": 1.0} -->

1}\leftarrow\begin{cases} \omega^{0} &amp; {{\text{if~}\overline{g}\left( \mathbf{x}^{k},\mathbf{u}^{k} \right)} \leq \varepsilon} \\ {\gamma_{\text{fail}}\omega^{k}} &amp; \text{otherwise} 21: return State and control trajectories (xk,uk) at iteration k Algorithm 1 GuSTO [BonalliCauligiEtAl2019]

<!-- chunk {"id": "body-0012", "role": "body", "section": "Technical Background", "weight": 1.0} -->

In this section, we introduce the GuSTO framework \[BonalliCauligiEtAl2019\] for solving the trajectory generation problem and the parametric SCP formulation we use for amortized optimization.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A Sequential Convex Programming via GuSTO", "weight": 1.0} -->

In our work, we consider parametrized trajectory optimization problems of the form,

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Sequential Convex Programming via GuSTO", "weight": 1.0} -->

where the state $x_{t} \in {\mathbb{R}}^{n_{x}}$ and control $u_{t} \in {\mathbb{R}}^{n_{u}}$ are continuous decision variables. Here, the stage cost $g_{t}{( \cdot )}$ and terminal cost $g_{N}{( \cdot )}$ are assumed to be convex functions without loss of generality. The key challenge in solving stems from the dynamics $\psi_{t}{( \cdot )}$ and inequality constraints $f_{t,i}{( \cdot )}$, which are assumed smooth but non-convex. The objective function and constraints are functions of the parameter vector $\theta \in \Theta$, where $\Theta \subseteq {\mathbb{R}}^{n_{p}}$ is the admissible set of parameters.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Sequential Convex Programming via GuSTO", "weight": 1.0} -->

The GuSTO solution procedure solves Equation in an iterative fashion by constructing a series of convex approximations,

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Sequential Convex Programming via GuSTO", "weight": 1.0} -->

We note that, in accordance with the GuSTO solution procedure, $\hat{f}{( \cdot )}$ is included in penalty form using the $\omega_{k}{\max{({\hat{f}{(x_{t},u_{t})}},0)}}$ operation, which is a non-smooth expression that can be rewritten using linear constraints \[NocedalWright2006\]. Finally, a trust region constraint ${\|{x_{t} - {\overline{x}}_{t}}\|} \leq \Delta_{k}$ facilitates improved convergence by restricting the solution of the convex approximation to remain "close" to the linearization $(\overline{x},\overline{u})$ and this constraint is similarly rewritten in penalty form as $\omega_{k}{\max{({{\|{x_{t} - \overline{x}}\|}_{2} - \Delta_{k}},0)}}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Sequential Convex Programming via GuSTO", "weight": 1.0} -->

This reference trajectory is used to construct the convex problem given in Eq. and recover the new solution $(\mathbf{x}^{k},\mathbf{u}^{k})$. If the new solution $(\mathbf{x}^{k},\mathbf{u}^{k})$ violates the trust region constraint, then the solution is rejected (Lines -). Otherwise, an additional check proceeds by computing the model accuracy ratio $\rho^{k}$ defined in Equation 5 from \[BonalliCauligiEtAl2019\]. If $\rho^{k} > \rho^{1}$, then the new solution is rejected (Lines -). Otherwise, the solution is accepted and the parameters $\Delta^{k}$ and $\omega^{k}$ also updated (Lines -).

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Sequential Convex Programming via GuSTO", "weight": 1.0} -->

0: Training parameters {θi}i = 1Nd, batch size Nbs &lt; Nd and Nepoch training epochs.
1: Initialize training batch 𝒟 ← ⌀ and randomized neural network parameters ϕ0.
7: Sample batch {θi,(xi*,ui*)}i = 1Nbs from 𝒟
10: return Trained neural network parameters ϕk
Algorithm 2 Learning the Problem-Solution Mapping

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B Learning the Optimal Control Structure", "weight": 1.0} -->

The key insight of amortized optimization is that the solution to the optimization problem in Eq. is largely influenced by the parameters $\theta \in \Theta$ and that there exists a "problem-solution" mapping between parameters $\theta$ and the solution $(\mathbf{x}^{\ast},\mathbf{u}^{\ast})$. As such, the goal of amortized optimization is to learn this mapping in a data-driven fashion by simulating various parameters $\theta$ from representative problems of interest and repurposing this learned mapping to accelerate solution times onboard for new problems.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Learning the Optimal Control Structure", "weight": 1.0} -->

Algorithm sketches the high-level overview of the training procedure used to learn this problem-solution mapping for trajectory generation problems as found in \[BanerjeeEtAl2020, CauligiCulbertsonEtAl2022\]. The procedure begins by sampling representative parameters for problems of interest, e.g., initial and goal conditions, obstacles, among others (Line ‣ 2). Next, the optimal solution $(\mathbf{x}_{i}^{\ast},\mathbf{u}_{i}^{\ast})$ is solved for using GuSTO and added to the training set (Lines -). Finally, the neural network parameters $\phi$ are updated using stochastic gradient descent to minimize the loss function, i.e., cross-entropy loss for classification and mean squared error for regression formulations (Lines -).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Approach", "weight": 1.0} -->

We utilize a two-stage approach for learning the structure of the Astrobee motion planning problem, following the framework of \[BanerjeeEtAl2020\]. In the first stage, we generate training data offline using a simple simulator of the ISS presented in \[BualatSmithEtAl2018\] and use the GuSTO algorithm \[BonalliCauligiEtAl2019, BonalliBylardEtAl2019\] to find a local solution for the Astrobee motion planning problem. We then train a neural network to learn the problem-solution mapping between the motion planning problem parameters to the solution found by GuSTO. In the second stage, this learned neural network is deployed online and used to generate candidate warm start solutions given new motion planning queries. This warm start is then provided to the GuSTO solver to enforce runtime safety constraints for the system. This approach is illustrated in Figure.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A Astrobee Optimal Control Formulation", "weight": 1.0} -->

Here, we formulate the optimal control formulation used for the Astrobee free-flyer trajectory generation problem.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-A Astrobee Optimal Control Formulation", "weight": 1.0} -->

System Dynamics: The trajectory generation problem for Astrobee entails solving for a six degree-of-freedom state trajectory and a control trajectory including translational and rotational inputs. Specifically, the 13 dimensional state for the free-flying spacecraft robot model consists of position $r \in {\mathbb{R}}^{3}$, velocity $v \in {\mathbb{R}}^{3}$, the quaternion representation of attitude $q \in \mathcal{S} \subseteq {\mathbb{R}}^{4}$, and angular velocity $\omega \in {\mathbb{R}}^{3}$, and the control variables are the force $F \in {\mathbb{R}}^{3}$ and moment $M \in {\mathbb{R}}^{3}$. The continuous-time dynamics are given by

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-A Astrobee Optimal Control Formulation", "weight": 1.0} -->

where $m$ and $J$ are the robot mass and inertia tensor, respectively, and $\Xi{(\omega)}$ is the quaternion kinematics matrix \[Shuster1993\]. State constraints for this system include norm bounds for velocity and angular velocity, as well as norm bound control constraints for the force and moment. We further enforce a non-convex equality constraint to satisfy the quaternion manifold constraint,

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-A Astrobee Optimal Control Formulation", "weight": 1.0} -->

where $x_{\text{init}}$ is the initial state provided by state estimation and $\mathcal{X}_{\text{goal}}$ is the terminal set defined within a tolerance $\delta_{\text{goal}} > 0$ about the goal position $r_{\text{goal}} \in {\mathbb{R}}^{3}$,

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-A Astrobee Optimal Control Formulation", "weight": 1.0} -->

Vehicle Constraints: To satisfy Astrobee vehicle limits, we enforce conic bounds on the speeds,

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-A Astrobee Optimal Control Formulation", "weight": 1.0} -->

where $v_{\text{max}}$ and $\omega_{\text{max}}$ are the maximum translational and rotational speeds, respectively. Finally, we enforce actuator limits on the forces and moments,

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-A Astrobee Optimal Control Formulation", "weight": 1.0} -->

Collision Avoidance Constraints: For collision avoidance with surrounding obstacles, we enforce a safety constraint using the signed distance function \[SchulmanDuanEtAl2014\],

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A Astrobee Optimal Control Formulation", "weight": 1.0} -->

where a negative value ${\text{sd}{(x_{t})}} < 0$ indicates collision with an obstacle and we seek to enforce a minimum clearance $\delta_{\text{sd}} > 0$. For this work, we assume axis-aligned bounding boxes only and compute the signed distance function manually by assuming a simple spherical robot footprint for Astrobee.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A Astrobee Optimal Control Formulation", "weight": 1.0} -->

Trajectory Generation Problem: Collecting these constraints, the nonlinear optimization problem used to model the Astrobee trajectory generation problem is given,

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Astrobee Optimal Control Formulation", "weight": 1.0} -->

Here, the non-convex constraints include the rotational kinematics and dynamics (Eq. ), the quaternion norm constraint (Eq. ), and the collision avoidance constraint (Eq. ). This optimization problem can be solved using the GuSTO solver in Algorithm.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B Supervised Learning from Optimized Trajectories", "weight": 1.0} -->

We train a neural network to predict trajectory solutions for new planning problems by learning from optimized examples. Training data is generated offline by sampling representative problem parameters $\theta$, which include the robot's start and goal states as well as virtual obstacles.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-B Supervised Learning from Optimized Trajectories", "weight": 1.0} -->

We sample problems from two simulation environments provided by the Astrobee software suite: (i) a planar ${{2\text{m}} \times 2}\text{m}$ granite table simulating the testbed at NASA Ames, and (ii) the Japanese Experiment Module (JEM) on the ISS, approximated as a ${{{{1.5\text{m}} \times 6.4}\text{m}} \times 1.7}\text{m}$ 3D volume in ISS coordinates. Start and goal positions are sampled uniformly in each environment, with start and goal attitudes sampled uniformly over ${SO}{}$. All trajectories begin and end with zero linear and angular velocity. Obstacles are sampled as axis-aligned cuboids with random dimensions and are placed within $1\text{m}$ of the workspace origin.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B Supervised Learning from Optimized Trajectories", "weight": 1.0} -->

For each sampled problem, we formulate a trajectory optimization problem as defined in Eq., incorporating dynamics and collision-avoidance constraints. We solve each instance using the GuSTO algorithm, producing optimized state and control trajectories $(\mathbf{x},\mathbf{u})$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B Supervised Learning from Optimized Trajectories", "weight": 1.0} -->

To prepare the data for learning, each dimension of the state and control trajectories is fit with a $p^{\text{th}}$-order polynomial in time, where $p = 3$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B Supervised Learning from Optimized Trajectories", "weight": 1.0} -->

where ${\mathbf{α}}_{j}$ and ${\mathbf{β}}_{j}$ are the polynomial coefficients. The state is 13-dimensional and the control is 6-dimensional, resulting in an output size of ${{({13 + 6})} \times 4} = 76$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B Supervised Learning from Optimized Trajectories", "weight": 1.0} -->

The neural network receives as input the problem specification: the start and goal poses (7D each, consisting of position and quaternion) and a fixed-size 6D vector representing the obstacle geometry, for a total of 20 input dimensions. It outputs the fitted polynomial coefficients $({\mathbf{α}}_{j},{\mathbf{β}}_{j})$. The network is a fully connected feedforward model with three hidden layers of sizes 256, 512, and 256, with ReLU activations and uniformly initialized weights. Training minimizes the mean squared error between the predicted and ground truth coefficients.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B Supervised Learning from Optimized Trajectories", "weight": 1.0} -->

The final training set consists of approximately 11,000 trajectories sampled from the ISS environment and 2,000 trajectories from the granite table. Details of the simulation environments are provided in the next section.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

The Astrobee platform is a free-flying, 30-cm wide, cube-shaped robot developed by NASA Ames Research Center to enable a wide range of autonomous manipulation and inspection tasks aboard the ISS \[BualatSmithEtAl2018\]. Astrobee is a holonomic robot with six degrees-of-freedom, actuated by twelve independent thrusters that draw air from the ISS cabin environment.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

This section describes the key software components, testing environments, and unique challenges involved in integrating and validating our trajectory optimization software on the Astrobee platform across simulation, ground, and flight experiments.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-A Software Integration", "weight": 1.0} -->

Our software was implemented in C++ and integrated into a fork of NASA's Astrobee flight software (FSW) \[Astrobee, BualatSmithEtAl2018, SmithBarlowEtAl2016\], which is publicly available^11^1 Astrobee FSW runs on three onboard processors: an ARM-based low-level processor (LLP) for propulsion control, another ARM-based mid-level processor (MLP) for the primary flight software, and an Android-based high-level processor (HLP) for relaying and processing guest science commands \[fluckiger2018astrobee\]. Our planner executed on the MLP, with lightweight modifications to the HLP interface for experiment coordination.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-A Software Integration", "weight": 1.0} -->

Astrobee's FSW uses the Robot Operating System (ROS) middleware, with approximately 46 nodelets grouped into 14 processes. The default framework consists of planning (Planner), mapping (Mapper), localization (Extended Kalman Filter EKF), control (CTL), and a force allocation module (FAM), all orchestrated by a managing node, the choreographer \[fluckiger2018astrobee\]. Our trajectory optimization was implemented as a new planner node, 'planner_scp', that subscribes and publishes to the same topics as the existing planners, namely 'planner_qp' and 'planner_trapezoidal', based on quadratic programming (QP) and trapezoidal motion planning respectively. The choreographer node was configured to call our planner as an additional option.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-A Software Integration", "weight": 1.0} -->

External libraries were integrated within the Astrobee FSW stack, specifically OSQP \[StellatoBanjacEtAl2020\] for solving the optimization problem and LibTorch \[PaszkeGrossEtAl2017\] for machine learning. Cross-compilation of these libraries, particularly LibTorch, was a significant challenge, as discussed later in this section. However, inference of the lightweight feedforward model was sufficiently performant on the MLP.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-B Testing Environments", "weight": 1.0} -->

Our testing followed a three-phase progression: simulation, ground testing, and finally, on-orbit flight testing.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Simulation", "weight": 1.0} -->

The Astrobee software stack includes a high-fidelity Gazebo-based simulator with two environments: a planar 3-DOF "granite table" world that emulates the facility at NASA Ames, and a 6-DOF ISS world based on the Japanese Experiment Module (JEM) within which Astrobee operates. Simulation allowed early software validation in both 2D and 3D microgravity scenarios.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Ground Testing", "weight": 1.0} -->

The integrated software was tested on Astrobee hardware at the NASA Ames granite table facility, where Astrobee floats on a 2D air-bearing platform within a mock-up of the ISS interior, as shown in Figure 3(a). Over multiple day-long test sessions, we iterated on algorithm tuning and operations design, with support from the Ames team.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Flight Testing", "weight": 1.0} -->

Flight experiments were performed aboard the ISS as a "crew-minimal" operation, involving 35 minutes of crew time for setup and teardown, and four hours of autonomous operation. The concept of operations (CONOPS) involved undocking Astrobee, moving it to a designated "HOME" pose, and executing multiple round-trip trajectories beginning and ending at "HOME". Each trajectory was executed twice: once from a cold start and once from a warm start that required neural network inference onboard.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Flight Testing", "weight": 1.0} -->

Commands for trajectory start and goal poses, warm/cold initialization settings, and virtual obstacle placement were sent by ground operators, who remained on standby for teleoperation if needed. A total of 18 trajectories (each with multiple sub-segments) were executed during the test session. A second Astrobee, configured identically, remained docked as a backup but was not needed. After the flight, experiment logs, images, and videos were downlinked for post-processing and analysis (the results of which are presented in Section VI). A short video is available on YouTube^22^2

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-C Challenges", "weight": 1.0} -->

Cross-compilation of external libraries posed a significant challenge for hardware integration, as was also noted in prior work on Astrobee hardware \[doerr2024reswarm\]. Nonetheless, this effort achieved the first successful cross-compilation of PyTorch as a learning-based control framework on Astrobee.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-C Challenges", "weight": 1.0} -->

A practical hurdle was tuning the runtime of the planner to operate within the timing constraints of Astrobee's flight software, particularly the choreographer node. Processor load varied across trajectories and testing sessions, affecting how many optimization iterations could be completed in time. We addressed this by introducing dynamic ROS parameters to adjust iteration limits, convergence tolerances, and time discretization, to achieve reliable and robust planner performance.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-C Challenges", "weight": 1.0} -->

Another challenge was the performance of Astrobee's localization module, which relies on detecting visual features in a known map of the ISS. Some areas of the JEM module are feature-sparse, leading to degraded pose estimates and drift, even when the planner produced optimal trajectories. To mitigate this, we worked with the NASA Ames team to identify feature-rich regions, minimized rotational motion to improve tracking, and implemented abort logic with teleop fallback to recover from localization failures.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Iterations to converge (run time in seconds) ↓", "weight": 1.0} -->

Learned Warm Starts Accelerate Convergence Without Sacrificing Optimality: A core hypothesis of this work is that learned warm starts can accelerate trajectory optimization without degrading solution quality. Table I confirms that warm and cold starts achieve nearly identical optimal costs across all trajectory categories, including highly non-convex cases with rotation and obstacle avoidance. Figure illustrates that both approaches converge to the same trajectory, with warm starts beginning closer to the solution, reflecting the robustness of SCP methods \[MaoSzmukEtAl2016\].

<!-- chunk {"id": "body-0053", "role": "body", "section": "Iterations to converge (run time in seconds) ↓", "weight": 1.0} -->

The primary benefit of warm starts lies in convergence speed. Figure shows per-instance reductions in solver iterations: each line links a cold and warm start for the same problem instance, black markers denote sample means, and bars show 95% confidence intervals. The predominance of downward-sloping lines demonstrates statistically significant acceleration across problem instances. The few upward-sloping outliers arise from out-of-distribution obstacle scenarios, discussed as a limitation later. This confirms that warm-starting is an effective and practical strategy for real-time trajectory optimization.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Iterations to converge (run time in seconds) ↓", "weight": 1.0} -->

Iteration Gains Are Most Pronounced in Non-Convex Regimes: To analyze when warm starting is helpful, we partition the trajectories into four categories: translation only, rotation only, obstacle avoidance with seen (in-distribution) obstacles, and obstacle avoidance with unseen (out-of-distribution) obstacles.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Iterations to converge (run time in seconds) ↓", "weight": 1.0} -->

For translation-only trajectories, Figure shows that warm and cold starts converge in nearly the same number of iterations. The problem is convex, so learned priors are unnecessary. In these convex translation-only cases, the relatively large iteration count arises from the numerical settings rather than problem difficulty. Each trajectory was discretized at 20 Hz over long horizons (up to 40 s), yielding hundreds of timesteps ($N = 800$) and tens of thousands of decision variables. We also enforced tight solver tolerances ($10^{- 5}$--$10^{- 8}$) to ensure that the fine-grained trajectories remained dynamically consistent with Astrobee's onboard controller, with strict tracking tolerances. This high-accuracy configuration improves hardware robustness but increases the conditioning of the quadratic program and, consequently, the number of ADMM iterations required by OSQP. In contrast, our earlier work \[BanerjeeEtAl2020\] solved the same trajectory optimization problems with coarser discretizations ($N \leq 100$) and looser tolerances, converging in only 10--100 iterations.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Iterations to converge (run time in seconds) ↓", "weight": 1.0} -->

In contrast to the lack of improvement in translation-only cases, the rotation-only trajectories show a significant benefit, i.e., warm starts reduce iteration counts by over 60% on average. This is because attitude dynamics, parameterized by quaternions, are non-convex, and poor initializations can violate feasibility or cause slow convergence. The learned model implicitly encodes rotational structure from prior data, enabling faster convergence by proposing trajectories that satisfy rotational feasibility earlier in the optimization. This ability of the warm start to encode the rotational structure is qualitatively visible in Figure.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Iterations to converge (run time in seconds) ↓", "weight": 1.0} -->

Obstacle avoidance tasks also show a large acceleration, i.e., up to 50% fewer iterations when obstacles match those seen in the training distribution. The warm start model implicitly learns common avoidance patterns and initializes trajectories that navigate around the obstacle effectively. The SCP solver benefits from this informed guess, requiring fewer iterations to converge to a feasible and optimal trajectory. However, this benefit vanishes for unseen obstacles.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Iterations to converge (run time in seconds) ↓", "weight": 1.0} -->

Generalization to Unseen Obstacles is Limited by Model Architecture: Performance degrades when obstacle configurations deviate from the training distribution. For obstacles not seen during training, warm starts provide no benefit and exhibit higher variance. In most of these cases, warm starts initialize with infeasible trajectories, e.g., passing through the obstacle, which the optimizer must then repair over many iterations. The iteration counts in these cases match or exceed those of cold starts.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Iterations to converge (run time in seconds) ↓", "weight": 1.0} -->

This result reflects the limited expressivity of the current feedforward architecture, which lacks spatial reasoning and contextual understanding. As shown in prior work \[shi2022neural, li2022trajectory\], feedforward models struggle to generalize when training coverage is insufficient. More expressive architectures, e.g., transformer-based priors with attention mechanisms \[BridenGurgaEtAl2025b, GuffantiGammelliEtAl2024\], could better capture task context and improve generalization in unfamiliar environments. Another approach to mitigate unseen obstacles in low-dimensional systems is to use an RRT planner to generate a feasible initial trajectory.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Iterations to converge (run time in seconds) ↓", "weight": 1.0} -->

Trajectory Visualizations Reveal Qualitative Differences in Initialization: Figure shows example trajectories across categories. In translation-only tasks, both warm and cold trajectories begin reasonably close to the solution, converging quickly. Obstacle avoidance tasks illustrate how warm starts tend to choose a path that matches prior experience, which the solver then refines. For rotation tasks, cold starts begin with linear and suboptimal orientation trajectories, while warm starts begin smoother and closer to the optimal solution, providing a better initialization.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Iterations to converge (run time in seconds) ↓", "weight": 1.0} -->

Importantly, in all cases the final trajectory is the same, reaffirming that the optimization dominates the solution quality. However, the warm start initialization provides a better starting point, reducing the number of iterations required by the solver and improving computational efficiency.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Iterations to converge (run time in seconds) ↓", "weight": 1.0} -->

Implications for Onboard and Adaptive Planning: These results have important implications for autonomy algorithms in time- and compute-constrained settings, such as space robotics. Learned warm starts can significantly reduce computation time for complex planning tasks, particularly when dynamics or obstacles introduce non-convexity. The results showed a 50-60% reduction in number of iterations required for convergence, which can enable faster re-planning and unlock real-time operations in these resource-constrained environments.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Iterations to converge (run time in seconds) ↓", "weight": 1.0} -->

More broadly, these results highlight the promise of adaptive, learning-guided planners that accelerate optimization in structured environments while remaining robust to distributional shifts. By training on diverse environments and incorporating more expressive architectures \[BridenGurgaEtAl2025b, GuffantiGammelliEtAl2024\], future systems could generalize more effectively to unseen scenarios. Augmenting these approaches with out-of-distribution (OOD) detection \[BanerjeeSharmaEtAl2022, SinhaSchmerlingEtAl2023\] would enable planners to fall back to cold starts or alternative initializations when model confidence is low, ensuring that reliance on learned priors is modulated intelligently based on context. This points toward a new generation of planners that dynamically balance learned priors for initialization with fallback mechanisms to maintain reliability in dynamic and uncertain environments.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we presented the first flight results on the use of machine learning to warm start and significantly accelerate runtimes for onboard trajectory optimization for the Astrobee free-flying robot. Through our experimental tests onboard the ISS in February, 2025, we demonstrated how our trained network reduces the number of solver iterations required for convergence in complex, non-convex planning tasks, including a 60% iteration reduction for convergence in scenarios involving rotational dynamics and a 50% reduction in cases with obstacles drawn from the training distribution of the warm start model. Through this effort, we aim to demonstrate how machine learning can be safely infused for onboard guidance, navigation, & control and unlock frontiers in autonomous capabilities for the next generation of spaceflight missions.
