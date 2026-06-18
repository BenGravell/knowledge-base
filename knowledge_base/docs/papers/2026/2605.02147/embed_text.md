## Introduction

Sampling-based model predictive control is a workhorse for real-time control of nonlinear and contact-rich robotic systems. Algorithms like Model Predictive Path Integral (MPPI) and the Cross-Entropy Method (CEM) leverage parallel simulation to optimize complex cost functions by sampling and scoring candidate trajectories. Unlike gradient-based methods, they require only the ability to evaluate trajectory costs---making them compatible with black-box simulators and learning-based models. This flexibility makes them a common choice for manipulation and locomotion, where gradients are unavailable or expensive.

Despite their success, the information-theoretic foundation of these methods leads to fundamental limitations. MPPI aggregates cost information by taking a weighted average over all samples, with weights given by exponentiated trajectory costs. Since this average ignores where samples lie in the space, it produces *mode-averaging*: the resulting control does not represent any local minimum, but a blend of multiple minima. For instance, a robot navigating around an obstacle will average trajectories on either side---steering directly into a collision. CEM avoids mode-averaging through elite selection, but this mechanism induces *mode-seeking* behavior that commits aggressively to one mode and limits exploration.

Figure 1: The proposed OT-MPC algorithm controlling a Unitree Go2 quadruped. Colored curves show planned foot trajectories from different candidate solutions at a key decision point where multiple gait strategies are viable. OT-MPC naturally maintains diverse candidates when the cost landscape is multimodal; when candidates converge to a single mode, local proposal sampling concentrates refinement where it is needed.

Both failure modes stem from the control-as-inference formulation underlying these methods, which frames optimal control as sampling from a Gibbs distribution over trajectories. The resulting objective is an information-theoretic divergence---typically the KL divergence---which quantifies *how* probability mass is distributed but not *where*. Methods derived from such objectives therefore aggregate sample information *globally*, without regard to spatial arrangement. The result is no inherent mechanism for local refinement, mode preservation, or ensemble coordination. Prior work has sought to address these shortcomings, but existing approaches are typically *post hoc* heuristic modifications.

This article addresses these shortcomings at a foundational level by developing Sinkhorn Coordinate Descent (SCD), a sampling-based optimization algorithm derived from an optimal transport (OT) variational principle. Unlike information-theoretic divergences, OT objectives such as the Wasserstein distance measure not only whether two distributions assign probability mass similarly, but also the cost of transforming one into the other---incorporating spatial information. Entropy regularization softens the coupling and enables efficient computation via the Sinkhorn algorithm. The resulting MPC algorithm, Optimal Transport MPC (OT-MPC), computes an optimal coupling between particles and low-cost proposals, then updates each particle toward its weighted barycenter. Like MPPI, this algorithm requires only cost evaluations, making it compatible with non-smooth dynamics and non-differentiable costs. Experiments on navigation, manipulation, and locomotion demonstrate improved success rates over existing methods.

Contributions. In summary, this article contributes the following to the theory and practice of sampling-based control:

We propose SCD, a gradient-free optimization algorithm, and its MPC instantiation, OT-MPC. Unlike other sampling-based methods, SCD updates particles based on both cost and geometric proximity---enabling local refinement while preserving diversity.

We establish theoretical properties of SCD, including monotone descent, convergence guarantees, and closed-form updates for quadratic costs.

We demonstrate empirically that OT-MPC achieves higher success rates than MPPI, CEM, and SV-MPC on challenging navigation, manipulation, and locomotion tasks.

## Related Work

The OT-MPC algorithm inherits the control-as-inference formulation common to sampling-based MPC but replaces the information-theoretic objective with an optimal transport one. We first review variational inference methods and then discuss prior uses of optimal transport in robotics.

### II-A Variational Inference for Model-Predictive Control

Sampling-based MPC methods such as MPPI and CEM frame optimal control as variational inference, approximating a Gibbs distribution over low-cost trajectories. Both methods use information-theoretic objectives---MPPI minimizes KL divergence via importance sampling, while CEM fits a parametric distribution to elite samples. As discussed in the introduction, the former leads to mode-averaging and the latter to mode-seeking. Recent variants address these issues through annealing schedules, covariance adaptation, warm-starting, and mixture models, but these are heuristics that do not change the variational objective.

The closest work conceptually is the Tsallis VI-MPC, which also modifies the divergence in the inference formulation. That work unifies MPPI and CEM through a generalized entropy objective that interpolates between mode-averaging and mode-seeking behavior. Similarly, OT-MPC replaces the KL divergence, but with an optimal transport objective that incorporates spatial information rather than adjusting the entropy's tail behavior. Other VI-MPC methods leverage gradient information: Stein variational approaches use the score function to update particles, and recent DDP-based methods use second-order derivatives. Gradient-free variants of SVGD exist but require careful selection of an auxiliary distribution and suffer from high-variance updates. In contrast, OT-MPC is zeroth-order and only requires cost evaluations.

### II-B Optimal Transport in Robotics and Control

Optimal transport has been used in robotics to formulate control objectives---steering multi-agent systems to goal configurations, covariance steering for robust planning, and imitation learning. These applications use OT to define *what* to achieve; OT-MPC instead uses OT to determine *how* to solve the control problem.

Diffusion models, now widely used for policy learning, can be viewed as solving an optimal transport problem between noise and data distributions. However, diffusion transports particles independently via a learned score function. SCD instead computes an explicit coupling between particles and proposals, with marginal constraints that coordinate updates and prevent mode collapse.

The most similar existing algorithm to OT-MPC is MPOT, which also uses the Sinkhorn algorithm for trajectory optimization. The key distinction is where the task objective enters the formulation: MPOT encodes the control cost directly in the transport cost matrix, steering waypoints toward globally low-cost regions, and OT-MPC encodes costs through the marginal weights and reserves the transport cost for geometric proximity. This separation enables particles to move toward nearby promising proposals rather than distant optima, providing the local refinement that avoids mode-averaging and respects the geometry of the space.

## Background: Optimal Transport

Figure 2: Overview of OT-MPC. (a) Proposals are sampled to explore the trajectory space. (b) The Sinkhorn algorithm computes a soft coupling between candidates (bold curves) and proposals factoring in both cost and proximity. Colors indicate which to which proposals the candidate is most strongly coupled. (c) Each candidate updates toward its coupled proposals via a barycentric projection eq. 17—refining locally while preserving distinct modes. (d) The lowest-cost candidate is executed. Unlike MPPI, which averages all samples globally, OT-MPC couples each candidate to nearby proposals—avoiding the mode-averaging that would steer directly into the obstacle and enabling local refinement of candidates within each mode.

Optimal transport (OT) finds the minimum-cost coupling between two distributions. For probability mass functions $q \in \mathbf{\Delta}^{N}$ and $p \in \mathbf{\Delta}^{M}$, a coupling is a joint distribution $\Gamma \in \mathbf{R}_{+}^{N \times M}$ with marginals ${\Gamma1_{M}} = q$ and ${\Gamma^{\mathsf{T}}1_{N}} = p$; denote this set $\mathbf{\Gamma}{(q,p)}$. Given a cost matrix $C \in \mathbf{R}^{N \times M}$, the OT problem minimizes total transport cost. When the cost reflects distance, OT metrizes the space of distributions---for instance, yielding the Wasserstein distance when $C_{ij} = {\|{x_{i} - y_{j}}\|}^{2}$. Unlike the KL divergence, which compares distributions pointwise without regard to the underlying space, OT incorporates geometric structure through the cost matrix.

The OT problem is a linear program with $\mathcal{O}{({N^{3}{\log N}})}$ complexity, but entropy regularization enables efficient approximate solutions via the Sinkhorn algorithm. The entropic OT (EOT) problem is:

where ${H{(\Gamma)}} ≔ {- {\sum_{i,j}{\Gamma_{ij}{({{\log\Gamma_{ij}} - 1})}}}}$ is the entropy. The unique solution has the form $\Gamma_{ij}^{\star} = {u_{i}K_{ij}v_{j}}$ with $K_{ij} = {\exp\left( {- {C_{ij}/\varepsilon}} \right)}$, where the scaling vectors $u,v$ are computed by alternating projections onto the marginal constraints (Algorithm 1). As $\varepsilon\rightarrow 0$, the coupling becomes sparse, deterministic coupling $\Gamma^{\star}$ as converges to the unregularized OT solution. As $\varepsilon\rightarrow\infty$, the coupling ignores the transport cost and $\Gamma^{\star}\rightarrow{qp^{\mathsf{T}}}$.

Input: Cost matrix C ∈ RN × M, marginals q ∈ RN, p ∈ RM, regularization ε &gt; 0.
Output: Optimal coupling Γ⋆ ∈ RN × M.
// Can warm start

Algorithm 1 Sinkhorn Algorithm (Sink)

## Optimal Control Problem Formulation

This section formulates the optimal control problems solved by OT-MPC using the control-as-inference perspective, which is mathematically equivalent to the free energy duality in the MPPI literature.

Consider a deterministic discrete-time system with state $x_{t} \in \mathbf{R}^{n}$, control $u_{t} \in \mathbf{R}^{m}$, initial condition $x_{0}$, and dynamics:

Let $\mathbf{X}$ and $\mathbf{U}$ denote the sets of state and control sequences of horizon $t_{f}$. The task is specified by a cost function $J:{{\mathbf{X} \times \mathbf{U}}\rightarrow\mathbf{R}_{+}}$. A common choice is,

though $J{(\mathbf{x},\mathbf{u})}$ need not be continuous or differentiable. Let $\Phi{(\mathbf{u};x_{0})}$ denote the *rollout* map, which returns the state-control trajectory satisfying eq. 2. The optimal control problem is:

### IV-A Optimal Control via Variational Inference

The OT-MPC algorithm solves eq. P using SCD (Section V), which approximately samples from a target distribution that concentrates probability mass at the minima of $S{(\mathbf{u};x_{0})}$. This target is derived using the control-as-inference framework, which reformulates eq. P as a Bayesian inference problem in which $\mathbf{u}$ are the latent variables to be inferred.

Select a prior $P{(\mathbf{u})}$ and define a binary random variable $o \in {\{ 0,1\}}$ to indicate whether controls $\mathbf{u}$ are optimal. Optimal sequences can be generated by sampling from the posterior:

Since sampling from this posterior is intractable, we seek a variational approximation by finding the distribution in a tractable family $\mathbf{Q} \subseteq {\mathbf{\Delta}{(\mathbf{U})}}$ closest in KL divergence:

Rearranging yields the *evidence lower bound* (ELBO):

The standard choice of likelihood is the exponentiated cost:

under which the ELBO becomes:

When $\mathbf{Q} = {\mathbf{\Delta}{(\mathbf{U})}}$, the solution is the Gibbs measure:

The inverse temperature $\beta$ controls concentration: as $\beta\rightarrow 0$, $Q\rightarrow P$; as $\beta\rightarrow\infty$, probability concentrates at the global minima of $S$. In practice, $Q^{\star} \notin \mathbf{Q}$, so algorithms like OT-MPC and MPPI approximate it within $\mathbf{Q}$.

### IV-B The Path Integral Method for Sampling Controls

This section briefly describes how MPPI solves eq. 8. The objective eq. 8 is equivalent to the free energy variational inequality in the MPPI literature. The distinction between the two inequalities is only in terminology.

The MPPI algorithm restricts $\mathbf{Q}$ to Gaussian distributions with fixed covariance:

where $\mathbf{\Sigma} = {(\Sigma_{t})}_{t = 0}^{t_{f}}$ is a known covariance sequence and $\overline{\mathbf{u}} = {({\overline{u}}_{t})}_{t = 0}^{t_{f}}$ is the mean to be optimized. Since $Q^{\star}$ cannot be sampled directly, importance sampling approximates the minimum mean square error (MMSE) estimator:

where $\mathbf{u}_{j} = {\overline{\mathbf{u}} + {\delta\mathbf{u}_{j}}}$ with ${\delta\mathbf{u}_{j}} \sim {\mathcal{N}{(0,\mathbf{\Sigma})}}$. This yields the MPPI update:

## Sinkhorn Coordinate Descent

This section describes *Sinkhorn Coordinate Descent* (SCD), a gradient-free algorithm that evolves $N$ particles $\mathbf{z} = {(z_{i})}_{i = 1}^{N}$ toward the target distribution $Q^{\star}{(z)}$ using $M$ proposals $\mathbf{y} = {(y_{j})}_{j = 1}^{M}$ sampled from a reference distribution $R{(\left. \mathbf{y} \middle| \mathbf{x} \right.)}$. Note that the reference may optionally depend on the particle values. Unlike importance sampling, which computes a single global average, SCD incorporates geometric information through the EOT cost computed via Algorithm 1. This section presents SCD independently of the control setting; section VI instantiates it for MPC.

The proposals are sampled from a distribution $R{(\left. \mathbf{y} \middle| \mathbf{z} \right.)}$, which is optionally conditioned on the particle values. The target marginal ${p{(\mathbf{y})}} \in \mathbf{\Delta}^{M}$ is defined via self-normalizing importance sampling:

The particle marginal ${q{(\mathbf{z})}} \in \mathbf{\Delta}^{N}$ can be set arbitrarily, e.g., it can be defined analogously to $p{(\mathbf{y})}$ or a uniform distribution to encourage exploration. Together with a cost function $c:{{\mathbf{R}^{n} \times \mathbf{R}^{n}}\rightarrow\mathbf{R}}$, these define an EOT problem over particle positions:

The SCD algorithm solves this EOT problem via alternating optimization of particles and coupling:

$\mathbf{z}^{({k + 1})}$ ${\leftarrow{{\operatorname{argmin}\limits_{\mathbf{z}}\mathcal{L}_{\varepsilon}^{c}}{(\mathbf{z},\Gamma^{(k)};\mathbf{y})}}},$ (16a)
$\Gamma^{({k + 1})}$ ${\leftarrow{{\operatorname{argmin}\limits_{\Gamma \in \mathbf{\Gamma}^{({k + 1})}}\mathcal{L}_{\varepsilon}^{c}}{(\mathbf{z}^{({k + 1})},\Gamma;\mathbf{y})}}},$ (16b)

where $\mathbf{\Gamma}^{({k + 1})} ≔ {\mathbf{\Gamma}{({q{(\mathbf{z}^{({k + 1})})}},{p{(\mathbf{y})}})}}$ is the coupling constraint induced by the current particles. The coupling update eq. 16b is solved efficiently via Algorithm 1. The particle update eq. 16a generally requires first-order optimization, with gradients available via the envelope theorem. However, for quadratic costs the solution is closed-form, e.g:

### Proposition 1 (Barycentric Update)

When ${c{(z,y)}} = {\|{z - y}\|}_{2}^{2}$, the minimizer of $\mathbf{z}\mapsto{\mathcal{L}_{\varepsilon}^{c}{(\mathbf{z},\Gamma;\mathbf{y})}}$ is the barycentric projection:
