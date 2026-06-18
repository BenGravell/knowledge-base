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

We propose SCD, a gradient-free optimization algorithm, and its MPC instantiation, OT-MPC. Unlike other sampling-based methods, SCD updates particles based on both cost and geometric proximity---enabling local refinement while preserving diversity.

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

Let $\mathbf{X}$ and $\mathbf{U}$ denote the sets of state and control sequences of horizon $t_{f}$. The task is specified by a cost function $J:{{\mathbf{X} \times \mathbf{U}}\rightarrow\mathbf{R}_{+}}$. A common choice is,

<!-- chunk {"id": "body-0017", "role": "body", "section": "Optimal Control Problem Formulation", "weight": 1.0} -->

though $J{(\mathbf{x},\mathbf{u})}$ need not be continuous or differentiable. Let $\Phi{(\mathbf{u};x_{0})}$ denote the *rollout* map, which returns the state-control trajectory satisfying eq. 2.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-A Optimal Control via Variational Inference", "weight": 1.0} -->

The OT-MPC algorithm solves eq. P using SCD (Section V), which approximately samples from a target distribution that concentrates probability mass at the minima of $S{(\mathbf{u};x_{0})}$. This target is derived using the control-as-inference framework, which reformulates eq. P as a Bayesian inference problem in which $\mathbf{u}$ are the latent variables to be inferred.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Optimal Control via Variational Inference", "weight": 1.0} -->

Select a prior $P{(\mathbf{u})}$ and define a binary random variable $o \in {\{ 0,1\}}$ to indicate whether controls $\mathbf{u}$ are optimal.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A Optimal Control via Variational Inference", "weight": 1.0} -->

The inverse temperature $\beta$ controls concentration: as $\beta\rightarrow 0$, $Q\rightarrow P$; as $\beta\rightarrow\infty$, probability concentrates at the global minima of $S$. In practice, $Q^{\star} \notin \mathbf{Q}$, so algorithms like OT-MPC and MPPI approximate it within $\mathbf{Q}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B The Path Integral Method for Sampling Controls", "weight": 1.0} -->

This section briefly describes how MPPI solves eq. 8. The objective eq. 8 is equivalent to the free energy variational inequality in the MPPI literature. The distinction between the two inequalities is only in terminology.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Sinkhorn Coordinate Descent", "weight": 1.0} -->

This section describes *Sinkhorn Coordinate Descent* (SCD), a gradient-free algorithm that evolves $N$ particles $\mathbf{z} = {(z_{i})}_{i = 1}^{N}$ toward the target distribution $Q^{\star}{(z)}$ using $M$ proposals $\mathbf{y} = {(y_{j})}_{j = 1}^{M}$ sampled from a reference distribution $R{(\left. \mathbf{y} \middle| \mathbf{x} \right.)}$. Note that the reference may optionally depend on the particle values. Unlike importance sampling, which computes a single global average, SCD incorporates geometric information through the EOT cost computed via Algorithm 1. This section presents SCD independently of the control setting; section VI instantiates it for MPC.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Sinkhorn Coordinate Descent", "weight": 1.0} -->

The proposals are sampled from a distribution $R{(\left. \mathbf{y} \middle| \mathbf{z} \right.)}$, which is optionally conditioned on the particle values.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Sinkhorn Coordinate Descent", "weight": 1.0} -->

The particle marginal ${q{(\mathbf{z})}} \in \mathbf{\Delta}^{N}$ can be set arbitrarily, e.g., it can be defined analogously to $p{(\mathbf{y})}$ or a uniform distribution to encourage exploration.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Sinkhorn Coordinate Descent", "weight": 1.0} -->

where $\mathbf{\Gamma}^{({k + 1})} ≔ {\mathbf{\Gamma}{({q{(\mathbf{z}^{({k + 1})})}},{p{(\mathbf{y})}})}}$ is the coupling constraint induced by the current particles. The coupling update eq. 16b is solved efficiently via Algorithm 1. The particle update eq. 16a generally requires first-order optimization, with gradients available via the envelope theorem. However, for quadratic costs the solution is closed-form, e.g:
