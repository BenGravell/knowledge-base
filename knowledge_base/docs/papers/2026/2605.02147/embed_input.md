<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sampling-Based Control via Entropy-Regularized Optimal Transport

Topics include Model predictive control, Predictive control, Robotics, Real-time systems, Online algorithms, Sampling-based methods, Optimization, Control, Sampling, Optimal transport.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sampling-based model predictive control methods like MPPI and CEM are essential for real-time control of nonlinear robotic systems, particularly where discontinuous dynamics preclude gradient-based optimization. However, these methods derive from information-theoretic objectives that are agnostic to the geometry of the control problem, leading to pathological behaviors such as mode-averaging when the cost landscape is complex. We present OT-MPC, a sampling-based algorithm that overcomes these limitations through an entropy-regularized optimal transport formulation. By computing an optimal coupling between candidate control sequences and low-cost proposals, OT-MPC refines candidates toward nearby promising samples while coordinating updates across the ensemble to maintain coverage of the solution space. We derive closed-form, gradient-free updates via the Sinkhorn algorithm, enabling real-time performance. Experiments on navigation, manipulation, and locomotion tasks demonstrate improved success rates over existing methods.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Sampling-based model predictive control is a workhorse for real-time control of nonlinear and contact-rich robotic systems. Algorithms like Model Predictive Path Integral (MPPI) and the Cross-Entropy Method (CEM) leverage parallel simulation to optimize complex cost functions by sampling and scoring candidate trajectories. Unlike gradient-based methods, they require only the ability to evaluate trajectory costs---making them compatible with black-box simulators and learning-based models. This flexibility makes them a common choice for manipulation and locomotion, where gradients are unavailable or expensive.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite their success, the information-theoretic foundation of these methods leads to fundamental limitations. MPPI aggregates cost information by taking a weighted average over all samples, with weights given by exponentiated trajectory costs. Since this average ignores where samples lie in the space, it produces *mode-averaging*: the resulting control does not represent any local minimum, but a blend of multiple minima. For instance, a robot navigating around an obstacle will average trajectories on either side---steering directly into a collision. CEM avoids mode-averaging through elite selection, but this mechanism induces *mode-seeking* behavior that commits aggressively to one mode and limits exploration.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Both failure modes stem from the control-as-inference formulation underlying these methods, which frames optimal control as sampling from a Gibbs distribution over trajectories. The resulting objective is an information-theoretic divergence---typically the KL divergence---which quantifies *how* probability mass is distributed but not *where*. Methods derived from such objectives therefore aggregate sample information *globally*, without regard to spatial arrangement. The result is no inherent mechanism for local refinement, mode preservation, or ensemble coordination. Prior work has sought to address these shortcomings, but existing approaches are typically *post hoc* heuristic modifications.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This article addresses these shortcomings at a foundational level by developing Sinkhorn Coordinate Descent (SCD), a sampling-based optimization algorithm derived from an optimal transport (OT) variational principle. Unlike information-theoretic divergences, OT objectives such as the Wasserstein distance measure not only whether two distributions assign probability mass similarly, but also the cost of transforming one into the other---incorporating spatial information. Entropy regularization softens the coupling and enables efficient computation via the Sinkhorn algorithm. The resulting MPC algorithm, Optimal Transport MPC (OT-MPC), computes an optimal coupling between particles and low-cost proposals, then updates each particle toward its weighted barycenter. Like MPPI, this algorithm requires only cost evaluations, making it compatible with non-smooth dynamics and non-differentiable costs. Experiments on navigation, manipulation, and locomotion demonstrate improved success rates over existing methods.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. In summary, this article contributes the following to the theory and practice of sampling-based control: We propose SCD, a gradient-free optimization algorithm, and its MPC instantiation, OT-MPC. Unlike other sampling-based methods, SCD updates particles based on both cost and geometric proximity---enabling local refinement while preserving diversity.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We establish theoretical properties of SCD, including monotone descent, convergence guarantees, and closed-form updates for quadratic costs.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate empirically that OT-MPC achieves higher success rates than MPPI, CEM, and SV-MPC on challenging navigation, manipulation, and locomotion tasks.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Variational Inference for Model-Predictive Control", "weight": 1.0} -->

Sampling-based MPC methods such as MPPI and CEM frame optimal control as variational inference, approximating a Gibbs distribution over low-cost trajectories. Both methods use information-theoretic objectives---MPPI minimizes KL divergence via importance sampling, while CEM fits a parametric distribution to elite samples. As discussed in the introduction, the former leads to mode-averaging and the latter to mode-seeking. Recent variants address these issues through annealing schedules, covariance adaptation, warm-starting, and mixture models, but these are heuristics that do not change the variational objective.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Variational Inference for Model-Predictive Control", "weight": 1.0} -->

The closest work conceptually is the Tsallis VI-MPC, which also modifies the divergence in the inference formulation. That work unifies MPPI and CEM through a generalized entropy objective that interpolates between mode-averaging and mode-seeking behavior. Similarly, OT-MPC replaces the KL divergence, but with an optimal transport objective that incorporates spatial information rather than adjusting the entropy's tail behavior. Other VI-MPC methods leverage gradient information: Stein variational approaches use the score function to update particles, and recent DDP-based methods use second-order derivatives. Gradient-free variants of SVGD exist but require careful selection of an auxiliary distribution and suffer from high-variance updates. In contrast, OT-MPC is zeroth-order and only requires cost evaluations.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Optimal Transport in Robotics and Control", "weight": 1.0} -->

Optimal transport has been used in robotics to formulate control objectives---steering multi-agent systems to goal configurations, covariance steering for robust planning, and imitation learning. These applications use OT to define *what* to achieve; OT-MPC instead uses OT to determine *how* to solve the control problem.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-B Optimal Transport in Robotics and Control", "weight": 1.0} -->

Diffusion models, now widely used for policy learning, can be viewed as solving an optimal transport problem between noise and data distributions. However, diffusion transports particles independently via a learned score function. SCD instead computes an explicit coupling between particles and proposals, with marginal constraints that coordinate updates and prevent mode collapse.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Optimal Transport in Robotics and Control", "weight": 1.0} -->

The most similar existing algorithm to OT-MPC is MPOT, which also uses the Sinkhorn algorithm for trajectory optimization. The key distinction is where the task objective enters the formulation: MPOT encodes the control cost directly in the transport cost matrix, steering waypoints toward globally low-cost regions, and OT-MPC encodes costs through the marginal weights and reserves the transport cost for geometric proximity. This separation enables particles to move toward nearby promising proposals rather than distant optima, providing the local refinement that avoids mode-averaging and respects the geometry of the space.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Optimal Control Problem Formulation", "weight": 1.0} -->

This section formulates the optimal control problems solved by OT-MPC using the control-as-inference perspective, which is mathematically equivalent to the free energy duality in the MPPI literature.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Optimal Control Problem Formulation", "weight": 1.0} -->

Consider a deterministic discrete-time system with state $x_{t}\in\mathbf{R}^{n}$, control $u_{t}\in\mathbf{R}^{m}$, initial condition $x_{0}$, and dynamics: Let $\mathbf{X}$ and $\mathbf{U}$ denote the sets of state and control sequences of horizon $t_{f}$. The task is specified by a cost function $J:\mathbf{X}\times\mathbf{U}\to\mathbf{R}_{+}$. A common choice is, though $J(\mathbf{x},\mathbf{u})$ need not be continuous or differentiable. Let $\Phi(\mathbf{u};x_{0})$ denote the *rollout* map, which returns the state-control trajectory satisfying eq. 2.

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-A Optimal Control via Variational Inference", "weight": 1.0} -->

The OT-MPC algorithm solves eq. P using SCD (Section V), which approximately samples from a target distribution that concentrates probability mass at the minima of $S(\mathbf{u};x_{0})$. This target is derived using the control-as-inference framework, which reformulates eq. P as a Bayesian inference problem in which $\mathbf{u}$ are the latent variables to be inferred.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-A Optimal Control via Variational Inference", "weight": 1.0} -->

Select a prior $P(\mathbf{u})$ and define a binary random variable $o\in\{0,1\}$ to indicate whether controls $\mathbf{u}$ are optimal. Optimal sequences can be generated by sampling from the posterior: Since sampling from this posterior is intractable, we seek a variational approximation by finding the distribution in a tractable family $\mathbf{Q}\subseteq\mathbf{\Delta}(\mathbf{U})$ closest in KL divergence: Rearranging yields the *evidence lower bound* (ELBO): The standard choice of likelihood is the exponentiated cost: under which the ELBO becomes: When $\mathbf{Q}=\mathbf{\Delta}(\mathbf{U})$, the solution is the Gibbs measure: The inverse temperature $\beta$ controls concentration: as $\beta\to 0$, $Q\to P$; as $\beta\to\infty$, probability concentrates at the global minima of $S$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Optimal Control via Variational Inference", "weight": 1.0} -->

In practice, ${Q}^{\star}\notin\mathbf{Q}$, so algorithms like OT-MPC and MPPI approximate it within $\mathbf{Q}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-B The Path Integral Method for Sampling Controls", "weight": 1.0} -->

This section briefly describes how MPPI solves eq. 8. The objective eq. 8 is equivalent to the free energy variational inequality in the MPPI literature. The distinction between the two inequalities is only in terminology.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B The Path Integral Method for Sampling Controls", "weight": 1.0} -->

The MPPI algorithm restricts $\mathbf{Q}$ to Gaussian distributions with fixed covariance: where $\mathbf{\Sigma}=(\Sigma_{t})_{t=0}^{t_{f}}$ is a known covariance sequence and $\bar{\mathbf{u}}=(\bar{u}_{t})_{t=0}^{t_{f}}$ is the mean to be optimized. Since ${Q}^{\star}$ cannot be sampled directly, importance sampling approximates the minimum mean square error (MMSE) estimator: where $\mathbf{u}_{j}=\bar{\mathbf{u}}+\delta\mathbf{u}_{j}$ with $\delta\mathbf{u}_{j}\sim\mathcal{N}(0,\mathbf{\Sigma})$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Sinkhorn Coordinate Descent", "weight": 1.0} -->

This section describes *Sinkhorn Coordinate Descent* (SCD), a gradient-free algorithm that evolves $N$ particles $\mathbf{z}=(z_{i})_{i=1}^{N}$ toward the target distribution ${Q}^{\star}(z)$ using $M$ proposals $\mathbf{y}=(y_{j})_{j=1}^{M}$ sampled from a reference distribution $R(\mathbf{y}|\mathbf{x})$. Note that the reference may optionally depend on the particle values. Unlike importance sampling, which computes a single global average, SCD incorporates geometric information through the EOT cost computed via Algorithm 1. This section presents SCD independently of the control setting; section VI instantiates it for MPC.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Sinkhorn Coordinate Descent", "weight": 1.0} -->

The proposals are sampled from a distribution $R(\mathbf{y}|\mathbf{z})$, which is optionally conditioned on the particle values. The target marginal $p(\mathbf{y})\in\mathbf{\Delta}^{M}$ is defined via self-normalizing importance sampling: The particle marginal $q(\mathbf{z})\in\mathbf{\Delta}^{N}$ can be set arbitrarily, e.g., it can be defined analogously to $p(\mathbf{y})$ or a uniform distribution to encourage exploration.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Sinkhorn Coordinate Descent", "weight": 1.0} -->

Together with a cost function $c:\mathbf{R}^{n}\times\mathbf{R}^{n}\to\mathbf{R}$, these define an EOT problem over particle positions: The SCD algorithm solves this EOT problem via alternating optimization of particles and coupling: where $\mathbf{\Gamma}^{(k+1)}\coloneqq\mathbf{\Gamma}(q(\mathbf{z}^{(k+1)}),p(\mathbf{y}))$ is the coupling constraint induced by the current particles. The coupling update eq. 16b is solved efficiently via Algorithm 1. The particle update eq. 16a generally requires first-order optimization, with gradients available via the envelope theorem. However, for quadratic costs the solution is closed-form, e.g:

<!-- chunk {"id": "body-0025", "role": "body", "section": "Model-Predictive Control via Entropic Optimal Transport", "weight": 1.0} -->

This section instantiates SCD for control, creating *Optimal Transport MPC* (OT-MPC). We specify the particle representation, proposal distribution, and computational trade-offs.

<!-- chunk {"id": "body-0026", "role": "body", "section": "VI-A Trajectory Optimization via Sinkhorn Coordinate Descent", "weight": 1.0} -->

Each particle $z_{i}=(u_{i}^{0},u_{i}^{1},\ldots,u_{i}^{t_{f}-1})$ represents a candidate control sequence. The proposal weights follow the Gibbs distribution $p_{j}\propto\exp(-\beta S(y_{j};x_{0}))$, where $\beta>0$ is an inverse temperature controlling concentration at low-cost proposals. Particles receive uniform weights $q_{i}=1/N$ to encourage exploration. At each MPC cycle, we run $K$ iterations of SCD, drawing fresh proposals each iteration, then execute the first control from the lowest-cost particle. Standard warm-starting applies: particles are shifted forward in time and the final segment is reinitialized.

<!-- chunk {"id": "body-0027", "role": "body", "section": "VI-B Proposal Distribution", "weight": 1.0} -->

The proposal distribution $R(\mathbf{y}|\mathbf{z})$ balances local refinement against global exploration. We use a mixture to sample proposals: where $\rho\in$ controls the exploration rate. The first component perturbs existing particles, enabling local refinement around promising solutions. The second component $R_{\mathrm{global}}$ provides global coverage---either uniform over the control bounds or a broad Gaussian centered at zero.

<!-- chunk {"id": "body-0028", "role": "body", "section": "VI-B Proposal Distribution", "weight": 1.0} -->

The perturbation covariance $\Sigma$ can be isotropic ($\sigma^{2}I$) or structured to reflect problem geometry. For trajectory optimization, temporal correlations often improve sample quality: perturbations that vary smoothly across timesteps produce dynamically coherent candidates, whereas independent noise at each timestep yields low-quality erratic trajectories.

<!-- chunk {"id": "body-0029", "role": "body", "section": "VI-C Hyperparameter Selection", "weight": 1.0} -->

OT-MPC introduces three key hyperparameters beyond those shared with MPPI: the entropy regularization $\varepsilon$, the relaxation parameter $\eta$, and the number of particles $N$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "VI-C Hyperparameter Selection", "weight": 1.0} -->

The regularization $\varepsilon$ controls coupling sparsity. Small $\varepsilon$ yields near-deterministic assignment where each particle couples primarily to its nearest low-cost proposal; this accelerates convergence but risks premature commitment. Large $\varepsilon$ spreads coupling mass broadly, maintaining diversity but slowing refinement. We find $\varepsilon$ in the range $[0.01,0.1]$ times the median pairwise distance works well across tasks.

<!-- chunk {"id": "body-0031", "role": "body", "section": "VI-C Hyperparameter Selection", "weight": 1.0} -->

The relaxation parameter $\eta\in(0,1]$ governs step size toward the barycenter. Full steps ($\eta=1$) converge fastest when proposals are fixed, but cause oscillation when proposals are resampled each iteration. Damped updates ($\eta\approx 0.5$) provide stability at the cost of slower convergence. In practice, $\eta$ between $0.3$ and $0.7$ balances these concerns.

<!-- chunk {"id": "body-0032", "role": "body", "section": "VI-C Hyperparameter Selection", "weight": 1.0} -->

The particle count $N$ determines the capacity to represent multimodal structure. Too few particles collapse to a single mode; too many incur unnecessary coupling cost. We observe diminishing returns beyond $N\approx 10$--$20$ for problems with two to four distinct modes. Since the coupling cost scales as $\mathcal{O}(NM)$, a practical heuristic is to set $N\ll M$, using many proposals for exploration but few particles to track the discovered modes.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate OT-MPC across a diverse set of robotics control tasks ranging from navigation, locomotion to manipulation. The experiments are designed to test and evaluate whether the optimal transport coupling improves the performance on tasks with multimodal cost landscapes that generally cause other sampling based methods to struggle.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

Baselines. We benchmark against MPPI, CEM and Stein Variational Model-Predictive Control (SV-MPC) on the lower-dimensional tasks such as bicycle navigation and planar Push-T task. We decided to exclude CEM and SV-MPC from higher dimensional system for the following reasons. As the state dimensions increase the CEM's elite selection mechanism performs poorly as it discards majority of the cost information and fails to capture complex cost landscapes. SV-MPC, which builds on SVGD requires differentiable and smooth dynamics and cost functions which may not be feasible for complex and larger dimensional systems that includes rich contact dynamics and sparse cost structure (e.g. indicator functions for collision). As OT-MPC and MPPI are both zeroth order sampling based methods, OT-MPC can be fairly compared against MPPI.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

MPPI Variants. OT-MPC generalizes MPPI in the cases $N=1$ or $\varepsilon\to\infty$ because SCD recovers the MPPI importance-weighted average exactly (Section V). The two methods share the same high-level structure---sample proposals, roll out dynamics, evaluate costs, update candidate controls. They differ only in how the candidates integrate sample information: MPPI uses a global weighted average while OT-MPC uses optimal transport. Comparing against vanilla MPPI therefore *isolates the contribution of the OT-based update rule*. Most enhancements to MPPI, e.g., colored noise, annealing schedules, and log-space formulations, improve proposal generation and scoring but do not modify the aggregation step, and thus *transfer directly to OT-MPC without modification*.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

Hyperparameter Tuning. To ensure fair comparison, the hyperparameters for all control algorithm are tuned using Optuna with the same hyperparameter tuning objective and whenever possible with the same sampling budget. Complete details on *cost structures, hyperparameter values, implementation details and additional visualization of successes and failures* are provided in the Appendix. Videos and an interactive 3D visualizer for qualitative inspection of trajectories are available on the project page.

<!-- chunk {"id": "body-0037", "role": "body", "section": "VII-A Car (Bicycle) Obstacle Avoidance", "weight": 1.0} -->

We first evaluate OT-MPC on a car navigation task using a kinematic bicycle model with states $(x,y,\theta,v)$ representing the position, heading and velocity of the system and with linear acceleration and steering angle as control inputs. The objective is to navigate the car from a starting location to a goal location through a dense obstacle field avoiding collision. We benchmark OT-MPC against MPPI, CEM, and SV-MPC across 300 Monte Carlo trials with randomly generated initializations, goal locations and obstacle field at two difficulty levels: Easy (sparser obstacles) and Hard (denser obstacle field). The hyperparameters of all the controllers were tuned using Optuna for a fair comparison. Table I shows the benchmark results and we can see that OT-MPC achieves the highest success rate (99% on Easy and 93.5% on Hard), outperforming MPPI and other control algorithms. The performance gap widens in the Hard settings where the denser obstacles create more multimodal cost landscapes and control schemes like MPPI struggle due to mode-averaging.

<!-- chunk {"id": "body-0038", "role": "body", "section": "VII-A Car (Bicycle) Obstacle Avoidance", "weight": 1.0} -->

Other details regarding the parameters, cost structure and breakdown of the benchmark results can be found in the Appendix C.

<!-- chunk {"id": "body-0039", "role": "body", "section": "VII-B 2D Push-T", "weight": 1.0} -->

The planar Push-T task is a well-known manipulator task used to evaluate controllers in a multimodal scenario. The objective here is to push and align a T-shaped block from a randomly perturbed initial location to a goal location using a circular pusher. This is an inherently difficult task for standard MPC and sampling based controllers due to the hybrid contact dynamics and sparse costs. Here the states of the system are the pusher position as well as the position and orientation of the T-block and we use velocity control to move the pusher. We benchmark our OT-MPC with other controllers across 50 randomly generated initial and goal configuration for the T-block. The results of the benchmark are provided in Table I. We can clearly observe the superior performance of OT-MPC (76% success) compared to the other control algorithms. Again here MPPI struggles due to mode-averaging in this contact-rich settings where there might be multiple viable solutions. SV-MPC was not able to solve this problem, due to the lack of meaningful gradients from the hybrid contact dynamics.

<!-- chunk {"id": "body-0040", "role": "body", "section": "VII-C Quadrotor Dense Obstacle Avoidance", "weight": 1.0} -->

In order to evaluate OT-MPC in higher dimensional systems, we have considered the 12DOF Quadrotor with thrust-torque control navigating in a dense obstacle field from a starting location to a goal avoiding collision. We tested our OT-MPC controller against MPPI across 100 trials each on three different environment difficulty settings - Easy (50 obstacles), Medium (100 obstacles), Hard (100 obstacles in tighter configuration). As shown in Table I OT-MPC outperform MPPI in both Medium (100% vs 60%) and Hard (92% vs 19%) settings. We observed that the low success rate in MPPI is not due to collision with obstacle but rather due to MPPI failing to find a feasible path in this dense obstacle field and often gets stuck in local minima while OT-MPC's multimodal approach helps alleviate this issue.

<!-- chunk {"id": "body-0041", "role": "body", "section": "VII-D Two Quadrotor Cooperative Load Carrying", "weight": 1.0} -->

Car Obstacle Easy Car Obstacle Hard Quad. Obstacle Easy Quad. Obstacle Medium Quad. Obstacle Hard Quad. Carry Normal Quad. Carry Hard TABLE I: Benchmark results comparing OT-MPC (ours) with various control schemes on a variety of robotics control tasks. The average steps for each task is computed using only successful runs. † The low standard deviation is due to the fact that MPPI only completed two runs successfully.

<!-- chunk {"id": "body-0042", "role": "body", "section": "VII-D Two Quadrotor Cooperative Load Carrying", "weight": 1.0} -->

We have extended our quadrotor experiment to two-quadrotor system trying to cooperatively carry a suspended load from an initial location to a goal. Here we have a 27DOF system (Two 12DOF quadrotors and 3D position of the suspended load) with a 6-dimensional control - thrust-torque control for each quadrotor but with yaw torque control disabled due to cable constraints. To increase the complexity of the experiment, we have designed the environment in which the two-quadrotor system must navigate through an opening in the wall to reach the other side (goal). We have benchmark MPPI and OT-MPC in two different difficulty setting with locations of holes and initial states of the system randomized - Normal (2.0m x 2.0m opening) and Hard (1.2m x 1.4m opening). The benchmark result from 100 runs (each) are shown in Table I and we observe that OT-MPC performs exceptionally well in both Normal (91 % vs 22%) and Hard (75%, 10%) when compared to MPPI.

<!-- chunk {"id": "body-0043", "role": "body", "section": "VII-D Two Quadrotor Cooperative Load Carrying", "weight": 1.0} -->

Here the narrow opening creates a bottleneck where both quadrotors need to coordinate precisely to navigate through and MPPI 's mode-averaging disrupts this coordination.

<!-- chunk {"id": "body-0044", "role": "body", "section": "VII-E Franka Push-T", "weight": 1.0} -->

We extended the planar Push-T task to full 3D manipulation setting using a Franka Panda arm and end-effector poking stick. The Franka state is 14-dimensional (joint positions and velocities) with 7-dimensional joint position control. Along with the T-block states (13 dimensional - position, quaternion, velocity and angular velocity) and End-Effector states (7-dimensional - End-effector position and quaternion), the total system is 34-dimensional. We parameterize the control trajectories using cubic splines to produce smooth joint motion. The objective here is to push a T-Block from an initial pose to a goal using the end-effector stick. We benchmark over 50 trials with randomized T-Block configurations. MPPI initially showed low success rate on this task, requiring significantly more hyperparameter tuning effort compared to OT-MPC to achieve competitive performance. After extensive tuning, as shown in Table I we were able to reach similar success rate (66% for OT-MPC vs 64% for MPPI).

<!-- chunk {"id": "body-0045", "role": "body", "section": "VII-E Franka Push-T", "weight": 1.0} -->

This result shows that OT-MPC can achieve good performance with less tuning in complex tasks and can probably outperform MPPI, if similar tuning effort is used.

<!-- chunk {"id": "body-0046", "role": "body", "section": "VII-F Quadruped Locomotion", "weight": 1.0} -->

We also evaluated the effectiveness of our controller on a simulated Unitree Go2 quadruped on locomotion task in different terrains. The Go2 quadruped is 37-dimensional system where the control inputs are the joint position of 12 leg joints. We employ a cubic hermite spline parameterization to sample smooth joint positions and velocities that enables us to produce coherent motions and the gaits emerge naturally from the sampling-based optimization rather than requiring reference trajectories or predefined gaits. We tuned our cost function weights for both MPPI and OT-MPC in flat terrain to produce stable walking gait. To test generalization capability, we then evaluate these algorithms on out of distribution environments like inclined ramp (mild inclination) and narrow bridge crossing. The results are shown in Table II. Since here we want to evaluate the locomotion performance, we have decided to report the average steps and median distance to goal across 5 terrain configurations. Both MPPI and OT-MPC achieve stable locomotion, however, OT-MPC achieves significantly lower average steps compared to MPPI indicating superior locomotion performance.

<!-- chunk {"id": "body-0047", "role": "body", "section": "VII-G Quadruped Box Pushing", "weight": 1.0} -->

We have also extended our Quadruped locomotion task to a contact rich loco-manipulation task where the quadruped is tasked with pushing a box from a starting location to a goal location. Here with the addition of the box, the state space expands to 37 robot states and 13 box states (position, quaternions, velocity and angular velocities). We benchmark the performance of MPPI and OT-MPC across 100 trials with randomized initial robot pose and box initializations (based on difficulty. See Appendix C for details). Table II shows the benchmark results and we can see that OT-MPC performs better while maintaining lower average steps and median distance to goal.

<!-- chunk {"id": "body-0048", "role": "body", "section": "VII-H Computational Overhead", "weight": 1.0} -->

For tasks with JAX-vectorized rollouts, Table III reports per-iteration and wall-clock times. OT-MPC achieves comparable or faster wall-clock times on most tasks despite the additional Sinkhorn step. This is because Optuna consistently selects fewer proposals per OT-MPC iteration. The transport coupling extracts more information per sample, reducing the number of rollouts needed. Since rollouts dominate compute, this efficiency more than compensates for the Sinkhorn overhead.

<!-- chunk {"id": "body-0049", "role": "body", "section": "VII-H Computational Overhead", "weight": 1.0} -->

For the Franka and Go2 experiments, sequential MuJoCo rollouts dominate wall-clock time, making overall timings unrepresentative of algorithmic cost. To isolate the OT-MPC overhead, we measured the per-iteration cost of the Sinkhorn solve and barycentric update: 1.6 ms for Franka ($8\times 800$ coupling) and 0.2 ms for Go2 ($8\times 50$).

<!-- chunk {"id": "body-0050", "role": "body", "section": "VII-H Computational Overhead", "weight": 1.0} -->

Two Quad Carry TABLE III: Computation times for JAX-vectorized environments. Each method uses its Optuna-tuned sample count.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper addresses the fundamental limitations of existing sampling-based optimal control algorithms, e.g., MPPI and CEM, caused by their information-theoretic foundations. The variational principles from which they are derived cannot incorporate geometric information, resulting in solutions that blend distinct modes or commit prematurely to one. To ameliorate these limitations, we derive a novel sampling algorithm, Sinkhorn Coordinate Descent (SCD), founded in optimal transport rather than information theory, and instantiate it in a model-predictive control scheme (OT-MPC). The optimal transport cost structure incorporates geometric proximity---enabling both local refinement and mode preservation behaviors not found in existing methods.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Moreover, we established theoretical properties of SCD including monotone descent and convergence guarantees, and demonstrated empirically that OT-MPC outperforms MPPI, CEM, and SV-MPC across navigation, manipulation, and locomotion tasks. The performance gap is most pronounced in settings with multimodal cost landscapes---e.g., dense obstacle fields, contact-rich manipulation, and coordinated multi-robot control---where existing methods struggle.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Limitations. OT-MPC incurs additional computational cost from Sinkhorn iterations compared to MPPI. Its complexity scales as $\mathcal{O}(NM)$ per iteration compared to the $\mathcal{O}(M)$ for an MPPI update---however, OT-MPC did not incur a significant overhead for the quantities of particles used in our experiments ($N\approx 10$--$20$). The algorithm's performance depends on the entropy regularization $\varepsilon$. Small values risk premature commitment while excessively large values slow refinement. We provided practical guidelines, but adaptive scheduling remains an open question. Finally, because particles update toward barycenters of proposals, exploration is fundamentally limited by proposal coverage---poor initialization or overly local sampling can still cause diversity collapse.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Future Work. There are a number of exciting avenues for future work. As a novel sampling algorithm, SCD has broad application beyond OT-MPC and would benefit from detailed comparisons to other sampling methods to identify its strengths and weaknesses across problem classes. There are also various algorithmic extensions to explore. For example, there are opportunities to dynamically adapt the proposal distribution by extending particles from points to Gaussian distributions or leveraging natural connections between OT and Laguerre tessellations to create a semi-discrete algorithm. Finally, the theoretical results we established for SCD are for the setting where proposals are fixed---generalizing them to situations where proposals are resampled can better inform our understanding of this algorithm.
