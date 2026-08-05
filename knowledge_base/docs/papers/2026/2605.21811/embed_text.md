<!-- arxiv-full-text:v1 {"arxiv_id": "2605.21811", "source": "arxiv-html"} -->

## Introduction

Robotic dexterous manipulation requires reasoning over quantities defined on different geometric spaces, including positions in Cartesian space, orientations on $\mathrm{SO}$, and joint limits in generalized coordinates. Some of these quantities correspond to soft objectives, such as null-space redundancy resolution and task prioritization, while others impose hard constraints that must never be violated, such as collision avoidance, closed-loop kinematic constraints, and force closure. Moreover, real-world perturbations and modeling errors require the system to respond quickly via feedback during execution. Successful manipulation therefore demands continuously resolving objectives and constraints defined on heterogeneous geometric spaces in real time.

Figure 1: Overview of SafePBDS. At each control step, tasks on heterogeneous manifolds (Ni, gi) are pulled back to the configuration manifold M and composed into a safe acceleration ā via quadratic programs. (Left) Representative tasks include an autonomous joint-damping SMCS (blue), a high-level finger-position action (red), and a force-closure CBF safety constraint (green), each connected to M by a task map. (Right) On a 16-DOF Allegro Hand, these components combine to achieve palm-down in-hand reorientation (Section VIII-D).

Contemporary data driven methods attempt to sidestep these challenges by learning end-to-end policies that implicitly encode all objectives and constraints. Deep reinforcement learning (DRL) and behavior cloning can capture globally coordinated behaviors and are often straightforward to deploy. However, the resulting policies often remain specialized to a single task or embodiment. Vision-language-action models (VLAs) have shown impressive generalization on arm-gripper manipulation, but their extension to multi-fingered hands remains limited by the complexity of dexterous motion and the difficulty of collecting multi-fingered manipulation data. Additionally, all aforementioned black-box policies can fail catastrophically outside the training distribution, motivating the need to incorporate certifiable structure for safety guarantees.

At the other end of the spectrum, trajectory optimization can explicitly reason about constraints and dynamics to produce certifiable motion plans. However, solving these optimizations is computationally expensive, prone to getting stuck in local minima, require specific engineering tricks such as fixed contact pairs, and the resulting plans are essentially one-shot. Adapting them to online perturbations requires expensive replanning at rates that are typically incompatible with high-frequency dexterous manipulation control.

A third family of approaches is the *vector field policy*, which maps each state to a desired velocity or acceleration through a globally defined vector field. Because these policies are defined analytically, they enable fast reactive behavior, and properties such as stability can often be certified by construction. Several frameworks compose per-task vector fields using Riemannian geometry, but existing formulations either lack geometric consistency or treat safety as a soft property. Moreover, because most vector field policies are inherently local, they can become trapped in local minima. A recent example, DextrAH-G, combines vector field policies with learning-based methods to mitigate this lack of global planning, but the resulting policies remain limited by the vector field formulation.

Among vector field policies, Pullback Bundle Dynamical Systems (PBDS) stands out for achieving geometric consistency. By building on the coordinate invariant simple mechanical control system (SMCS), PBDS provides a fully geometric formulation that works on arbitrary Riemannian manifolds. However, PBDS has two important limitations. First, *safety constraints are soft*: metric-based constraints enter the optimization as additional weighted objectives and can therefore be violated when they conflict with other tasks; moreover, these objectives may become ill-defined in unsafe regions. Second, *there is no action interface*: the system provides no mechanism for a higher-level policy to inject task manifold commands, limiting its use to autonomous policies fixed at design time.

We present SafePBDS (Safe Pullback Bundle Dynamical Systems), a framework that addresses both limitations of PBDS while preserving the geometric and compositional properties. SafePBDS extends PBDS with hard safety guarantees and external controllability while retaining its geometric consistency. At each control step, a constrained quadratic program takes in real-time observations and composes desired autonomous behaviors, safety constraints, and action inputs into a single acceleration target. This is enabled by the following: *Pullback control barrier functions (CBFs)* that enforce task manifold safety as hard constraints on the configuration manifold acceleration by pulling back the constraints through smooth task maps. We derive formulations for two prominent higher-order CBF variants, exponential (ECBF) and backstepping (BCBF), and show their respective dependencies on task manifold geometries.

A *task manifold action interface* that lets a higher-level policy inject inputs on selected task manifolds. Our formulation guarantees that zero input recovers the autonomous behavior and that safety is preserved under arbitrary inputs.

We also provide extensive evaluations of SafePBDS: *Simulation experiments* on an $\mathbb{S}^{2}$ double integrator and a 7-DOF robot arm validate the theoretical properties of our framework: chart invariance, task manifold metric effects, recovery from unsafe states, and the action interface.

*Hardware experiments* on a 23-DOF arm--hand system (Franka Panda + Allegro Hand) demonstrate (a) autonomous dexterous grasping of 20 household objects at a 92.5% success rate (111/120 trials), including a 3-finger ablation at 94.4% (34/36); and (b) robust in-hand reorientation under palm-down and variable wrist orientations, achieving over $360^{\circ}$ rotation in both directions.

The remainder of this paper is organized as follows. Section II reviews related literature. Section III introduces the necessary theoretical background. Section IV derives the pullback ECBF and BCBF formulations. Section V presents the task manifold action interface. Sections VII and VIII present simulation and hardware experiments, respectively.

## Related work

Given the breadth of the motion planning and robotic manipulation literature, we restrict our attention to topics directly related to this work. For the adjacent literature, we refer the reader to recent surveys on optimization-based task and motion planning, robot manipulation in contact, motion planning for manipulators in dynamic environments, deep reinforcement learning for robotics, and imitation learning for contact-rich manipulation.

### II-A Multi-task motion planning on manifolds

Reactive multi-objective control in Euclidean task manifolds is classically addressed by operational space control, which composes Cartesian objectives through null space projection. This line of work establishes key ingredients but does not provide a geometrically consistent or coordinate free framework for composing manifold valued tasks.

A major step toward manifold-valued policy composition is the introduction of *Riemannian Motion Policies* (RMPs), which compose acceleration-level policies through metric-weighted pullback; RMPflow later extends this construction to tree-structured task hierarchies. However, the original RMP formulation is not chart-invariant, so the resulting policy depends on the choice of local coordinates. A related line of work is the *Optimization Fabrics* and *Geometric Fabrics* framework, which provides a Finsler-geometric foundation for stable reactive policy design. Across this family of methods, however, safety-related behaviors are typically encoded in the reactive policy itself rather than enforced as hard constraints at runtime. Unresolved geometric consistency issues also leave them short of a complete solution to composing tasks defined on heterogeneous manifolds.

*Pullback Bundle Dynamical Systems* (PBDS) resolves the geometric consistency issue by realizing simple mechanical control systems (SMCSs) on task manifolds and combining them through a metric-weighted least-squares problem. In doing so, PBDS establishes a principled foundation for geometrically consistent control synthesis on manifolds. However, PBDS inherits the broader limitation above: safety-related tasks enter the least-squares objective as soft costs and may therefore be violated under competing task pressures. PBDS also remains purely autonomous, with no mechanism for a higher-level planner or learned policy to steer the system at runtime. Our work addresses both limitations.

### II-B Control barrier functions on manifolds

Control barrier functions (CBFs) certify forward invariance of a safe set by imposing an affine inequality on the control input at runtime. The earliest formulations assume the safety function has relative degree one with respect to the input. This assumption fails for systems where position-level safety must be enforced through acceleration-level control. Two families of methods address this higher-relative-degree setting. *Exponential CBFs* (ECBFs) apply pole-placement design to the chain of Lie derivatives of the safety function, collapsing the higher-order condition into a single linear constraint on the input. A related generalization, high-order CBFs (HOCBFs), relaxes the linear pole-placement structure of ECBFs to a sequence of class-$\mathcal{K}$ comparison functions. Backstepping CBFs (BCBFs) instead build a CBF from a safe virtual controller for the lower-order subsystem and lift it to the full system; for second-order systems with position constraints, this construction reduces to lifting a safe velocity field to an acceleration-level constraint.

Recent work has generalized the CBF methodology beyond Euclidean spaces to manifold-valued states. Wu and Sreenath extend CBF synthesis to mechanical systems evolving on Riemannian configuration manifolds, with demonstrations on the spherical pendulum ($\mathbb{S}^{2}$) and the 3D pendulum ($\mathrm{SO}$). More recently, De Sa et al. develop a general theory of geometric CBFs on control systems defined over bundles, and use it to generalize kinetic-energy CBF backstepping to SMCSs. These works establish geometric CBFs on individual configuration manifolds; SafePBDS instead defines safety on *task* manifolds so that hard constraints naturally expressed in different geometric spaces (e.g. end effector poses and joint angle limits) can be composed with the PBDS task structure.

### II-C Dexterous manipulation

We focus on two dexterous manipulation problems targeted in our hardware evaluation: multi-fingered *grasping* and *in-hand reorientation*. Both require coordinating objectives and constraints defined on heterogeneous spaces, including force closure and friction-cone conditions in contact space, fingertip and link clearance in Cartesian space, joint limits in the configuration manifold, and reachability in $\mathrm{SE}$.

### II-C1 Grasping

The theory of static multi-fingered grasping is well established. We refer the reader to for broader surveys of grasp synthesis and focus on methods that provide explicit physical-feasibility guarantees, as in our work. A central challenge in certifiable grasp synthesis is that precise local constraints must be satisfied while searching over multiple global grasp modalities (see for a grasp taxonomy). This challenge has motivated optimization-based pipelines that incorporate analytical grasp-quality objectives, sometimes used to refine learned grasp predictions. In most such methods, however, the relevant physical conditions enter as relaxed scalar penalties and therefore do not provide strict guarantees on the final grasp. Wu et al. address this limitation by formulating grasp refinement as a bilevel optimization in which force closure is imposed as an exact inner constraint, yielding grasps with certified physical feasibility at the solution. Li et al. further introduce the min-weight metric as a surrogate objective for force closure certification. However, both and certify grasp feasibility offline and do not maintain it online under execution-time perturbations. Lum et al. combine reinforcement learning with a Geometric Fabric to enforce arm joint limits and collision avoidance during grasp execution, but do not certify grasp conditions such as force closure. Shaw Cortez et al. use a CBF-based safety filter to preserve grasp validity (e.g., preventing slip and singularities) during in-hand adjustments, but do not discuss how the grasp is initially achieved.

### II-C2 In-hand reorientation

In-hand reorientation can be broadly divided by palm orientation. In the *palm-up* setting, gravity helps retain the object, allowing brief release-and-regrasp maneuvers. In the *palm-down* setting, the object must remain securely grasped throughout the motion. Both have proven challenging, and most prior work has relied on deep reinforcement learning with sim-to-real transfer, beginning with palm-up and extending to palm-down more recently; see for a broader survey. While these learned methods demonstrate impressive dexterity, they do not provide formal safety guarantees and typically require substantial tuning and reward engineering to work on hardware. Analytical approaches are much less common; existing work often exploits mechanical compliance and underactuation to reduce the planning burden. Suh et al. propose a contact-trust-region formulation for contact-rich MPC and demonstrate palm-up cube reorientation with a fully actuated Allegro hand. To the best of our knowledge, our work is the first to achieve palm-down and variable-wrist-pose in-hand reorientation on a fully actuated general-purpose dexterous hand without relying on either machine learning or mechanical compliance.

## Preliminaries

Our method draws on differential geometry, pullback bundle dynamical systems, and control barrier functions, which we introduce in this section. Before formalizing each construct, we anchor the exposition with the following running example.

### Example 1 (Reaching with obstacle avoidance)

A 7-DOF Franka Emika Panda arm is to reach a goal end effector pose while avoiding a fixed workspace obstacle. The configuration is given by seven joint angles $\sigma=(\sigma^{1},\ldots,\sigma^{7})$ with joint limits $\sigma^{j}_{-}\leq\sigma^{j}\leq\sigma^{j}_{+}$. Forward kinematics yields the end effector pose and the pose of each link for collision checking. The motion policy must reconcile objectives on heterogeneous spaces: *End effector tracking* in end effector pose.

*Obstacle avoidance* in link-obstacle distances.

*Joint limits* in the configuration manifold.

This system is implemented in simulation in Section VII.

Manifolds and Maps Configuration manifold (dimension m) Task manifold for task i (dimension ni) Tangent and cotangent bundles of M Tangent-bundle point; v ∈ TpM Differential and Jacobian of fi Time derivative of Jfi, i.e. vℓ ∂2fi/∂xℓ∂xj Higher-order task map, (p, v) ↦ (fi(p), (dfi)p(v)) Second fundamental form of f Riemannian metrics on M and Ni Inner product of metric g; on N also ⟨⋅, ⋅⟩N Levi-Civita connections on M and N Christoffel symbols on M and N Sharp operator, g♯: T*M → TM (and task manifold analogue) Riemannian gradient: ⟨grad h, v⟩g = dh(v) $\sigma(t),\,\dot{\sigma},\,\ddot{\sigma}$ Configuration curve on M; velocity and coordinate acceleration task manifold curve on N Dissipative force map TNi → T*Ni SMCS input codistribution Weighting pseudometric (task priority) Lower-right block of wi in local coordinates Control input (generalized force one-form) Affine distribution of second-order vectors at (p, v) Safe acceleration set (pullback CBFs) Vertical-bundle and actuation projections Optimal autonomous acceleration Control task map, input ul ∈ T*Nl, behavior metric, weighting pseudometric Control Barrier Functions (ECBF) Safety function (indexed h0, j for multiple constraints) Safe set {x: h0(x) ≥ 0}, contained in informal safe region 𝒮 ⊆ N Extended class-𝒦∞ function ECBF gain vector; κ⊤ ∈ ℝ1 × r (scalars κ1, κ2 for r = 2) Auxiliary functions and sets in the ECBF recursion; pi are negated eigenvalues of F − Gκ⊤ Backstepping CBF (BCBF) Lifted BCBF candidate on TN Nominal and safe velocity fields on N (pre/post-filter) Half-Sontag safety filter quantities Open domain on which ξ̃ is a strict CBF Strict-margin augmentation and BCBF scaling Numerical padding for h0 (distinct from ε) TABLE I: Notation Summary.

### III-A Differential geometry and geometric mechanical systems

We present a brief introduction to Riemannian geometry; for further details, we refer the reader to. Let $M$ be a smooth $m$-dimensional manifold with tangent bundle $TM$ and cotangent bundle $T^{*}M$. A *Riemannian metric* $g$ is a smooth assignment of an inner product $g_{p}\colon T_{p}M\times T_{p}M\to\mathbb{R}$ to each point $p\in M$; the pair $(M,g)$ is called a *Riemannian manifold*. The metric induces the sharp isomorphism $g^{\sharp}\colon T^{*}M\to TM$, which maps each covector $\alpha\in T_{x}^{*}M$ to the unique vector $g^{\sharp}(\alpha)\in T_{x}M$ satisfying The *Riemannian gradient* of a smooth function $h$ is defined by $\operatorname{grad}h=g^{\sharp}(dh)$, or equivalently, $\langle\operatorname{grad}h,v\rangle_{g}=dh(v)$ for all tangent vectors $v$. The Levi-Civita connection induced by $g$ is denoted by $\nabla$, so that the covariant acceleration along a curve $\sigma(t)$ is given by $\nabla_{\dot{\sigma}}\dot{\sigma}$. When two manifolds $M$ and $N$ must be disambiguated, we write ${}^{M}\!\nabla$, ${}^{N}\!\nabla$ for their Levi-Civita connections and ${}^{M}\!\Gamma$, ${}^{N}\!\Gamma$ for the corresponding Christoffel symbols.

The Euler-Lagrange equations for a mechanical system admit a coordinate-free formulation on Riemannian manifolds, known as a *simple mechanical control system*:

### Definition III.1 (Simple Mechanical Control System)

A *simple mechanical control system* (SMCS) is a tuple $(M,g,\Phi,\mathcal{F})$, where $M$ is an $m$-dimensional smooth manifold (the *configuration manifold*), $g$ is a Riemannian metric on $M$ (the *kinetic energy metric*), $\Phi\in C^{\infty}(M)$ is the *potential function*, and $\mathcal{F}\subset T^{*}M$ is a rank-$p$ codistribution on $M$ (the *input codistribution*). The equations of motion are where $u\in\mathcal{E}(\sigma,\mathcal{F})$, the space of sections of $T^{*}M$ along $\sigma$ such that $u(t)\in\mathcal{F}_{\sigma(t)}$, is the control one-form. In coordinates, (1. ‣ III-A Differential geometry and geometric mechanical systems ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) becomes where $\Gamma^{k}_{ij}$ are the Christoffel symbols of $g$ and $u_{l}$ are the components of $u$.

### Remark 1

SMCS is control affine since the sharp map is a linear operator.

### Remark 2

$g^{kl}$ converts the force covectors $u$ and $d\Phi$ into accelerations. When $g$ is the kinetic energy metric, $g^{kl}$ plays the role of an inverse mass matrix. $\Gamma^{k}_{ij}\dot{\sigma}^{i}\dot{\sigma}^{j}$ corrects the coordinate acceleration $\ddot{\sigma}^{k}$ into a true acceleration on the curved manifold similar to the Coriolis and centripetal terms.

### Example 1 (continued)

For the 7-DOF arm reaching task, the configuration manifold is the open box of joint limits equipped with the flat product metric $g_{M}=\delta_{ij}$. Although the physical joint limits are closed, we use strict inequalities so that $M$ is a smooth manifold without boundary; the distinction makes no difference in practice.

### III-B Pullback bundle dynamical system (PBDS)

In order to construct a motion policy that combines multiple desired task behaviors, proposes designing a stable mechanical control system (SMCS) on each task manifold of interest and combining them via a weighted least-squares optimization over the resulting task accelerations. Consider smooth task maps $f_{i}:M\rightarrow N_{i}$, $i=1,\ldots,K$, that map the configuration manifold $M$ (of dimension $m$) to task manifolds $N_{i}$ (of dimension $n_{i}$). On each $N_{i}$ one designs an SMCS that exhibits a desired behavior by choosing a potential function $\Phi_{i}:N_{i}\rightarrow\mathbb{R}$, a Riemannian metric $g_{i}$ on $N_{i}$ (together with its Levi-Civita connection $\nabla_{i}$), and a dissipative force map $\mathcal{F}_{D,i}:TN_{i}\rightarrow T^{*}\!N_{i}$. We illustrate the role of $f_{i}$, $g_{i}$, $\Phi_{i}$, and $\mathcal{F}_{D,i}$ on the running 7-DOF arm scenario (Example 1. ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) in the continuation block following Definition III.2. ‣ III-B Pullback bundle dynamical system (PBDS) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation"). Together, these determine a second-order dynamical system on $TN_{i}$, which can be pulled back to a dynamical system on the pullback bundle where $\coprod$ denotes the disjoint union and $\pi_{N_{i}}:TN_{i}\rightarrow N_{i}$ is the tangent bundle projection. Concretely, the fiber of $f_{i}^{*}TN_{i}$ over a point $p\in M$ is the tangent space $T_{f_{i}(p)}N_{i}$. The framework of constructs on $f_{i}^{*}TN_{i}$ a pullback connection $f_{i}^{*}\nabla_{i}$, a compatible pullback metric $f_{i}^{*}g_{i}$, pullback dissipative forces $f_{i}^{*}\mathcal{F}_{D,i}$, and a pullback gradient operator $f_{i}^{*}\operatorname{grad}\Phi_{i}$, all of which are globally well-defined.

Given these pullback constructions, two operators are introduced that capture, respectively, the *desired* task manifold acceleration produced by each local PBDS and the *resulting* task manifold acceleration induced by a candidate configuration manifold acceleration. The first operator, maps a state $(p,v)\in TM$ to the *desired* pullback task acceleration. It is defined as the vertical-bundle projection of the velocity of the local PBDS curve at $(p,v)$: where $G_{i}$ encodes the dynamics of the local PBDS defined by $(f_{i},g_{i},\Phi_{i},\mathcal{F}_{D,i})$, and $\dot{\gamma}^{a}_{v_{p},i}$ is the resulting task manifold acceleration. The pullback construction ensures that $S_{i}$ is globally well-defined; see for a detailed derivation. In local coordinates, the desired acceleration evaluates to The second operator is defined as maps a candidate configuration manifold acceleration to its *resulting* task manifold acceleration. It is defined as the vertical-bundle projection of the differential of the pullback differential $f_{i}^{*}df_{i}$: For $a=\bigl((p,v),(v,a^{a})\bigr)\in\mathcal{D}_{(p,v)}$ (defined below), the local expression is where $(\dot{J}f_{i})^{\alpha}_{j}(p,v)=v^{\ell}\,\partial^{2}f_{i}^{\alpha}/\partial x^{\ell}\partial x^{j}$.

Let $\mathcal{D}_{\dot{\sigma}(t)}\subseteq T_{\dot{\sigma}(t)}TM$ denote the affine distribution of second-order vectors at $\dot{\sigma}(t)=(p,v)\in TM$, i.e. $\mathcal{D}_{(p,v)}=\{((p,v),(v,a^{a})):a^{a}\in\mathbb{R}^{n}\}$. Additionally, let $w_{i}$ be a Riemannian *weighting pseudometric* on $TN_{i}$ that controls the priority of task $i$ relative to the other tasks, and let $F_{i}:TM\rightarrow TN_{i}$, $(p,v)\mapsto(f_{i}(p),(df_{i})_{p}(v))$ be the higher-order task map. A best-compromise acceleration is then obtained by minimizing the weighted sum of task-acceleration tracking errors:

### Definition III.2 (Multi-Task PBDS, \[6, Definition III.2\])

Let $\{f_{i}:M\longrightarrow N_{i}\}_{i=1,\ldots,K}$ be smooth task maps for Riemannian task manifolds $(N_{i},g_{i})$, with corresponding smooth potential functions $\Phi_{i}:N_{i}\longrightarrow\mathbb{R}$, dissipative forces $\mathcal{F}_{D,i}:TN_{i}\longrightarrow T^{*}\!N_{i}$, and weighting pseudometrics (positive semidefinite Riemannian metric) $w_{i}$ on $TN_{i}$. Then the set $\{(f_{i},g_{i},\Phi_{i},\mathcal{F}_{D,i},w_{i})\}_{i=1,\ldots,K}$ forms a *multi-task PBDS* with curves $\sigma:[0,\infty)\longrightarrow M$ satisfying The dynamics (10. ‣ III-B Pullback bundle dynamical system (PBDS) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) are globally well-defined and smooth on $TM$; see for details. Since (10. ‣ III-B Pullback bundle dynamical system (PBDS) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) is a least-squares problem over the free variable $a^{a}\in T_{p}M$, it admits the local closed-form solution where $(\cdot)^{\dagger}$ is the pseudoinverse, $w_{i}^{a}\in\mathbb{R}^{n_{i}\times n_{i}}$ is the lower-right block of the local matrix representation of $w_{i}$ (the only block that contributes after the vertical-bundle projections in $S_{i}$ and $Z_{i}$), and with $\dot{\gamma}^{a}_{\dot{\sigma},i}$ given by (6 ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) evaluated at $p=\sigma(t)$, $v=\dot{\sigma}(t)$.

### Remark 3

The multi-task PBDS (10. ‣ III-B Pullback bundle dynamical system (PBDS) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) outputs the coordinate acceleration $\ddot{\sigma}$. The optimization variable $a^{a}\in T_{p}M$ in (10. ‣ III-B Pullback bundle dynamical system (PBDS) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) represents the coordinate second derivative $d^{2}\sigma^{k}/dt^{2}$, and the operators $S_{i}$ and $Z_{i}$ involve only the task manifold metrics $g_{i}$ and weights $w_{i}$. Consequently, the PBDS framework is oblivious to the geometry of $M$. Intuitively, PBDS produces the task manifold desired behavior, which is independent of the robot's configuration manifold dynamics. In practice, an acceleration tracking controller must be used to track $\ddot{\sigma}$ and account for the configuration manifold dynamics, which stems from the physical system dynamics.

### Example 1 (continued)

The end effector tracking objective decomposes into orientation tracking on $\mathrm{SO}$ and position tracking on $\mathbb{R}^{3}$; per, an additional joint space damping task is required for stability. This yields 3 SMCSs on a different manifold: *Orientation tracking* on $N_{\mathrm{ori}}=\mathrm{SO}$, task map $f_{\mathrm{ori}}\colon M\to\mathrm{SO}$ given by the end effector orientation from forward kinematics, attractor potential $\Phi_{\mathrm{ori}}$ centered at a goal orientation, and linear damping $\mathcal{F}_{D,\mathrm{ori}}$. In the implementation we use the unit quaternion parameterization (i.e. the universal double cover $\mathbb{S}^{3}\to\mathrm{SO}$); see Appendix XII.

*Position tracking* on $N_{\mathrm{pos}}=\mathbb{R}^{3}$ with the identity metric, task map $f_{\mathrm{pos}}\colon M\to\mathbb{R}^{3}$ given by the end effector position, attractor potential $\Phi_{\mathrm{pos}}$ centered at a goal position, and linear damping $\mathcal{F}_{D,\mathrm{pos}}$.

*Joint space damping* with identity task map $f_{\mathrm{jd}}=\mathrm{id}_{M}$, no potential, and linear damping $\mathcal{F}_{D,\mathrm{jd}}$.

In the implementation, the attractor and damping of each tracking SMCS are realized as separate PBDS tasks on the same manifold, so the multi-task PBDS comprises 5 tasks total (orientation attractor, orientation damping, position attractor, position damping, and joint space damping). These tasks compose into a multi-task PBDS through Definition III.2. ‣ III-B Pullback bundle dynamical system (PBDS) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation") with weighting pseudometrics $w_{i}$ tuned by task priority.

### III-C Control barrier functions (CBFs)

While multi-task PBDS (11 ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) allows encouraging safe behavior through metric-based constraints \[6, Section III.C\], it does not provide a hard guarantee. Additionally, metric-based constraints are ill-defined in unsafe regions. We now review control barrier functions, which provide the tools to overcome this limitation.

Consider a safety problem on a task manifold $N$ (e.g. obstacle avoidance constraints for the end effector), where $\mathcal{S}\subseteq N$ denotes a safe region: the system is safe if the state $x\in\mathcal{S}$.

### Definition III.3 (Safety function)

A smooth function $h_{0}:N\rightarrow\mathbb{R}$ with $0$ as a regular value and whose superlevel set satisfies is called a *safety function*.

Forward invariance of the set $\mathcal{C}_{0}$ implies that any trajectory initialized in $\mathcal{C}_{0}$ remains in $\mathcal{C}_{0}$ for all future times, ensuring that the system always satisfies safety constraints. Safety may be enforced by selecting appropriate control inputs $u$ that govern the evolution of $h_{0}$. To characterize how $u$ relates to $h_{0}$, we present two families of techniques from the literature. Throughout, we let $\alpha\in\mathcal{K}_{\infty}^{e}$ denote an extended class-$\mathcal{K}_{\infty}$ function, i.e., a continuous, strictly increasing function $\alpha:\mathbb{R}\to\mathbb{R}$ satisfying $\alpha=0$ and $\lim_{r\to\pm\infty}\alpha(r)=\pm\infty$. For a task manifold CBF we write $(x,\dot{x})\in TN$ for a tangent-bundle point, where $\dot{x}\in T_{x}N$; we fix a Riemannian metric $g$ on $N$, and the norm $\|\cdot\|_{N}$, gradient $\operatorname{grad}$, and inner product $\langle\cdot,\cdot\rangle_{N}$ below are all taken with respect to $g$.

We first introduce the class of systems under consideration. A *control-affine system* on a manifold $N$ takes the form where $f_{0}$ is a drift vector field on $N$, $B(x)=(B_{1}(x),\ldots,B_{m_{u}}(x))$ collects $m_{u}$ input vector fields with $B(x)\,u=\sum_{k=1}^{m_{u}}B_{k}(x)\,u_{k}\in T_{x}N$, and $U$ is the set of admissible inputs. In the context of the SMCS (1. ‣ III-A Differential geometry and geometric mechanical systems ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")), the state is $(x,\dot{x})\in TN$ and the control input $u$ enters through the acceleration, so the system has relative degree two with respect to a safety function $h_{0}(x)$.

### III-C1 Exponential CBF (ECBF)

When the safety constraint $h_{0}$ has relative degree $r\geq 2$ with respect to the control input, i.e. the first $r{-}1$ time derivatives of $h_{0}$ are independent of $u$ and $u$ first appears explicitly in $h_{0}^{(r)}$, the standard relative-degree-one CBF condition cannot be applied directly. The exponential CBF (ECBF) framework of addresses this by enforcing a linear constraint on the $r$th derivative of $h_{0}$.

The input-output linearized dynamics of $h_{0}$ under the virtual input $\mu=h_{0}^{(r)}$ take the linear form $\dot{\eta}_{b}=F\,\eta_{b}+G\,\mu$, $h_{0}=C\,\eta_{b}$, where $(F,G,C)$ is in controllable canonical form. Consider the input constraint $\mu\geq-\bm{\kappa}^{\top}\eta_{b}(x)$ with gains $\bm{\kappa}^{\top}=[\kappa_{1},\ldots,\kappa_{r}]\in\mathbb{R}^{1\times r}$. By the comparison lemma, under this constraint, $h_{0}(x(t))\geq C\,e^{(F-G\bm{\kappa}^{\top})t}\,\eta_{b}(x_{0})$. Therefore, safety ($h_{0}\geq 0$) is guaranteed if the right-hand side remains nonnegative. To this end, introduces a family of auxiliary functions $\nu_{i}$ and corresponding sets $\mathcal{C}^{\nu}_{i}$: where $p_{1},\ldots,p_{r}$ are the roots of the characteristic polynomial $F-G\bm{\kappa}^{\top}$. Forward invariance of $\mathcal{C}_{0}$ then requires the following conditions on $\bm{\kappa}$:

### Definition III.4 (Exponential CBF )

A safety function $h_{0}$ of relative degree $r$ with respect to (14 ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) is an *exponential CBF* if there exists a row vector $\bm{\kappa}\in\mathbb{R}^{r}$ such that for all $x\in\mathrm{Int}(\mathcal{C}_{0})$, results in $h_{0}(x(t))\geq C\,e^{(F-G\bm{\kappa}^{\top})t}\,\eta_{b}(x_{0})\geq 0$ whenever $h_{0}(x_{0})\geq 0$.

### Theorem III.1 (\[2, Theorem 8\])

Suppose $\bm{\kappa}$ is chosen such that $F-G\bm{\kappa}^{\top}$ is Hurwitz and totally negative (resulting in negative real poles), and its eigenvalues satisfy whenever $\nu_{i-1}(x_{0})>0$. Then $\mu\geq-\bm{\kappa}^{\top}\eta_{b}(x)$ guarantees that $h_{0}(x)$ is an exponential CBF.

### Remark 4

The totally-negative requirement is stronger than the standard Hurwitz condition, which permits complex eigenvalues with negative real parts. This is because the recursive argument in \[2, Proposition 6 and Theorem 7\] establishes forward invariance of each $\mathcal{C}^{\nu}_{i}$ by showing that $\dot{\nu}_{i-1}\geq 0$ on $\partial\mathcal{C}^{\nu}_{i-1}$ only when $p_{i}>0$. The eigenvalue bound (19. ‣ III-C1 Exponential CBF (ECBF) ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) couples the pole locations to the initial state: the poles cannot be placed arbitrarily fast without violating the requirement that $\nu_{i}(x_{0})\geq 0$. In practice, the ECBF can be designed via pole placement, choosing $p_{i}$ large enough for rapid convergence while satisfying (19. ‣ III-C1 Exponential CBF (ECBF) ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")). The constraint (18. ‣ III-C1 Exponential CBF (ECBF) ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) is then enforced pointwise via a quadratic program (QP) at each time step.

### Remark 5

Evaluating (18. ‣ III-C1 Exponential CBF (ECBF) ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) requires computing time derivatives of $h_{0}$ up to order $r$, which in turn depend on time derivatives of the state up to order $r$. For the SMCS (1. ‣ III-A Differential geometry and geometric mechanical systems ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")), which is second order, $r=2$, and the two conditions reduce to: 1) $p_{1},p_{2}>0$ with $\kappa_{1}=p_{1}p_{2}$ and $\kappa_{2}=p_{1}+p_{2}$, and 2) $p_{1}\geq-\dot{h}_{0}(x_{0})/h_{0}(x_{0})$.

### III-C2 Backstepping CBF (BCBF)

An alternative to the ECBF that avoids computing higher-order derivatives, which amplify measurement noise and incur additional autograd cost, is backstepping CBF (BCBF). In BCBF, the safety specification on $N$ is lifted to a CBF on $TN$ by introducing an auxiliary safe velocity field on $N$. Below we recite the key geometric generalization results . For simplicity, we assume the system is fully actuated ($\pi_{\mathcal{A}}=\mathrm{Id}$) and refer the reader to for the general (including underactuated) case and proof details. In practice, most manipulators are fully- or over-actuated.

### Step 1: Construct a safe velocity field

Given a nominal velocity field $\xi$ on $N$ (so $\xi(x)\in T_{x}N$), one applies a smooth safety filter to obtain a *safe velocity field* $\tilde{\xi}:N\to TN$, $x\mapsto\tilde{\xi}(x)\in T_{x}N$, that renders $\mathcal{C}_{0}$ forward invariant under first-order dynamics $\dot{x}=\tilde{\xi}(x)$. Following, one uses the *half-Sontag formula*: The half-Sontag formula is a smooth, closed-form safety filter: it adds a correction along $\operatorname{grad}h_{0}$ that is just large enough to enforce the CBF condition $d(h_{0})_{x}\xi_{\mathrm{HS}}\geq-\alpha(h_{0}(x))$, and vanishes when $\xi$ already satisfies it. The nominal velocity field $\xi$ can be chosen freely based on the application; a natural choice within the PBDS framework is $\xi(x)=-\operatorname{grad}\Phi|_{x}$, which drives the system toward the minimum of the task potential.

To provide a strict margin for the backstepping step, one further augments $\xi_{\mathrm{HS}}$ with an additional gradient term: for some $\delta>0$.

### Lemma III.2 (Lemma 2 in )

Let $h_{0}$ be the smooth safety function and $\mathcal{C}_{0}$ be the safe set as in Definition III.3. ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation"), and let $\alpha\in\mathcal{K}_{\infty}^{e}$. There exists an open set $\Omega_{0}\supset\mathcal{C}_{0}$ on which the safe velocity field (23 ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) satisfies the strict CBF condition

### Step 2: Lift to a CBF on $TN$

Using the safe velocity field $\mu_{x}$ from Step 1, one defines a candidate CBF on the tangent bundle: where $\varepsilon>0$ is a design parameter controlling the tradeoff between the safety margin and the allowable velocity deviation from $\mu_{x}$.

### Step 3: Enforce the BCBF constraint

### Theorem III.3 (Backstepping CBF )

The function $h$ in (25 ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) is a CBF for the SMCS on $T\Omega_{0}$, i.e., there exist control inputs satisfying for all $(x,\dot{x})\in T\Omega_{0}$.

Since $h(x,\dot{x})\leq h_{0}(x)$ for all $(x,\dot{x})\in TN$ by construction (25 ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")), forward invariance of the set $\{(x,\dot{x})\in TN:h(x,\dot{x})\geq 0\}$ immediately implies safety:

### Corollary III.1 (Safety \[11, Proposition 2\])

Let $u$ be any locally Lipschitz control input satisfying $\dot{h}(x,\dot{x},u)\geq-\alpha(h(x,\dot{x}))$ for all $(x,\dot{x})\in T\Omega_{0}$. If $h(x,\dot{x})\geq 0$, then $x(t)\in\mathcal{C}_{0}$ for all $t\geq 0$.

The BCBF approach has two practical advantages over the ECBF: it avoids computing second (or higher) derivatives of $h_{0}$ along the system dynamics, and the resulting CBF constraint (26. ‣ Step 3: Enforce the BCBF constraint. ‣ III-C2 Backstepping CBF (BCBF) ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) is affine in $u$, yielding a standard QP. Furthermore, the backstepping construction extends naturally to the Riemannian manifold setting via the geometric framework of. Conversely, the ECBF has the advantage that its constraint (18. ‣ III-C1 Exponential CBF (ECBF) ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) depends only on Lie derivatives of $h_{0}$ along the system vector fields and is therefore independent of any choice of Riemannian metric on $N$, whereas the BCBF relies on metric-dependent quantities ($\operatorname{grad}h_{0}$, $\|\cdot\|_{N}$, $\nabla_{\dot{x}}\mu_{x}$, $u^{\sharp}$).

## Pullback CBF for Task Manifold Safety

While metric-based tasks for safety were proposed, they present several limitations: *Exit behavior:* due to the symmetry of the metric-based velocity field, the constraint task must be deactivated when attempting to leave the safe set.

*Undefined behavior upon violation:* the metric $g=\exp(1/(2x^{2}))$ used in is undefined on the constraint boundary $x=0$, so no recovery mechanism exists once the constraint is violated.

*No guaranteed constraint satisfaction:* the constraint is ultimately enforced as one task among many in the multi-task PBDS QP (10. ‣ III-B Pullback bundle dynamical system (PBDS) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")), and the desired acceleration produced by the constraint task may not be fully realized.

We address these limitations by incorporating pullback control barrier functions, which produce sufficient conditions for a configuration-controlled robot to enforce task manifold safety. For brevity, we drop the task manifold index in this section. Consider a safety set $\mathcal{S}\subseteq N$ and a safety function $h_{0}:N\rightarrow\mathbb{R}$ that defines the safety of the system. We additionally make the following assumption, which is typically satsified in fully actuated and redundant robotic manipulators:

### Assumption 1 (Surjective submersive task map)

The task map $f:M\rightarrow N$ is a surjective submersion, so the system is fully actuated on $N$.

### Remark 6

The safe set in the configuration manifold is the preimage $f^{-1}(\mathcal{C}_{0})=\{p\in M\mid(h_{0}\circ f)(p)\geq 0\}$, which may not be connected. Since trajectories are continuous, forward invariance of $f^{-1}(\mathcal{C}_{0})$ implies forward invariance of each connected component individually.

Since the PBDS framework builds on the SMCS (1. ‣ III-A Differential geometry and geometric mechanical systems ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")), the system is second order. We present adaptations of both the ECBF from and the BCBF from enforce task manifold safety constraints on configuration manifold acceleration. By constraining the configuration manifold acceleration to lie in a safe set $\mathcal{A}_{\mathrm{safe}}$, we arrive at the following:

### Definition IV.1 (Autonomous SafePBDS)

The union of $K$ PBDS behavior tasks and $J$ pullback-CBF safety tasks, forms a multi-task PBDS with curves $\sigma:0,\infty)\longrightarrow M$ satisfying where $\mathcal{A}_{\mathrm{safe}}$ is the intersection of the pullback-CBF constraints induced by the $J$ safety tasks (Theorems [IV.1. ‣ IV-B Task manifold ECBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation") and IV.3. ‣ IV-C Task manifold BCBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")). For a BCBF safety task, $\bm{\kappa}_{j}$ is replaced by its BCBF parameters $(\xi_{j},\varepsilon_{j})$.

The remainder of this section derives pullback CBFs under the ECBF and BCBF formulations. The key idea is to pullback the task manifold CBF conditions through the task map to obtain safety constraints expressed entirely in configuration manifold inputs and the robot's state.

For the purpose of SafePBDS, which is controlled by configuration manifold coordinate acceleration $\ddot{\sigma}$, we show that both the pullback ECBF and pullback BCBF yield linear constraints on $\ddot{\sigma}$. Therefore, safety can be enforced by adding linear constraints to the PBDS QP (10. ‣ III-B Pullback bundle dynamical system (PBDS) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")). By substituting in Equation (2. ‣ III-A Differential geometry and geometric mechanical systems ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")), our derivation can be extended to general systems with non-flat configuration manifolds and SMCS dynamics (1. ‣ III-A Differential geometry and geometric mechanical systems ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")).

### IV-A Geometric Kinematics

While the safety constraint is defined in the task manifold $N$, the control input in PBDS is the configuration manifold coordinate acceleration $\ddot{\sigma}$. Thus, we begin by deriving the geometric kinematics relating the configuration and task manifold accelerations.

### IV-A1 Velocity Relationship

Let $x(t)$ be a curve on $N$, $\sigma(t)$ be a curve on $M$ where $f(\sigma(t))=x(t)$. In local coordinates, differentiating $x^{\alpha}=f^{\alpha}(\sigma)$ with respect to time yields where $Jf$ is the Jacobian of the task map. In coordinate-free notation, this is $\dot{x}=df\,\dot{\sigma}$.

### IV-A2 Acceleration Relationship

Differentiating the velocity relation gives the coordinate acceleration on $N$: The covariant accelerations on $N$ and $M$ are given in coordinates by Rearranging for $\ddot{\sigma}^{k}$ and substituting into yields Substituting into and using $\dot{x}^{\mu}=\frac{\partial f^{\mu}}{\partial\sigma^{i}}\dot{\sigma}^{i}$ yields where $(\nabla df)(\dot{\sigma},\dot{\sigma})$ denotes the second fundamental form of the map $f$ as.

### IV-B Task manifold ECBF

As is a relative degree 2 system, we examine the first and second derivatives of the constraint function $h_{0}$ along the system trajectories.

The first derivative of $h_{0}(x(t))$ is computed by the chain rule: For the second derivative, we differentiate and substitute $\dot{x}^{\alpha}=\frac{\partial f^{\alpha}}{\partial\sigma^{i}}\dot{\sigma}^{i}$: Substituting the coordinate acceleration expansion into and applying the chain rule identities Applying the ECBF constraint from Definition III.4. ‣ III-C1 Exponential CBF (ECBF) ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation") with $r=2$ to yields the task manifold formulation:

### Theorem IV.1 (Task manifold ECBF)

A safety function $h_{0}$ (Definition III.3. ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) is a task manifold ECBF for a PBDS system if there exists $\ddot{\sigma}\in T_{\sigma}M$ such that where the gains $\kappa_{1},\kappa_{2}$ satisfy the pole placement and initial-condition requirements in Definition III.4. ‣ III-C1 Exponential CBF (ECBF) ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation").

### Proof

Substituting into the ECBF condition $\ddot{h}_{0}\geq-\kappa_{2}\dot{h}_{0}-\kappa_{1}h_{0}$ and rearranging yields (41. ‣ IV-B Task manifold ECBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")). By the comparison lemma, the evolution of $h_{0}$ satisfies where $\eta_{b}=[h_{0},\dot{h}_{0}]^{\top}$. With $\kappa_{1}=p_{1}p_{2}$ and $\kappa_{2}=p_{1}+p_{2}$ for $p_{1},p_{2}>0$, the matrix exponential decays and the right-hand side remains nonnegative provided the initial state satisfies $x_{0}\in\mathcal{C}_{0}\cap\mathcal{C}^{\nu}_{1}$, i.e. $h_{0}(x_{0})\geq 0$ and $\dot{h}_{0}(x_{0})+p_{1}h_{0}(x_{0})\geq 0$. ∎

### Remark 7 (Metric independence)

The constraint (41. ‣ IV-B Task manifold ECBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) involves only coordinate partial derivatives of $h_{0}\circ f$ and the coordinate acceleration $\ddot{\sigma}^{i}$. Intuitively, $h_{0}\circ f$ has no knowledge of $N$, so no geometric quantities of $N$ appear. Since SafePBDS controls $\ddot{\sigma}$, the ECBF constraint contains no geometric quantities altogether.

### Remark 8 (Covariant form for non-flat $M$)

For any choice of Riemannian metric $g_{M}$ on $M$, substituting $\ddot{\sigma}^{k}=({}^{M}\!\nabla_{\dot{\sigma}}\dot{\sigma})^{k}-{}^{M}\!\Gamma^{k}_{ij}\dot{\sigma}^{i}\dot{\sigma}^{j}$ from into (41. ‣ IV-B Task manifold ECBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) and using the Riemannian Hessian identity yields the equivalent geometric form

### Remark 9 (Behavior outside $\mathcal{C}_{0}$)

As long as $h_{0}$ is smooth and well defined outside $\mathcal{C}_{0}$, the ECBF constraint guarantees the system will converge asymptotically to $\{x\mid h_{0}(x)\geq 0\}$ from any initial condition, with convergence rate governed by the eigenvalues $-p_{1},-p_{2}$ via. This contrasts with the metric-based constraint enforcement , where the metric $g=\exp(1/(2x^{2}))$ is undefined on the constraint boundary $h_{0}(x)=0$. In practice, one may offset $h_{0}$ so that $h_{0}(x)\geq-\epsilon$ represents safety; the ECBF then drives the system to $\{x\mid h_{0}(x)\geq-\epsilon\}$ in finite time.

### Example 1 (continued)

*Workspace obstacle clearance* for robot link $i$ is encoded on the task manifold $N_{\mathrm{obs},i}=\mathbb{R}$ with task map $f_{\mathrm{obs},i}\colon M\to N_{\mathrm{obs},i}\colon\sigma\mapsto d(\mathrm{geom}_{i},\mathrm{obs})$, the signed distance between the link $i$ collision geometry and the obstacle. The safety function $h_{0,\mathrm{obs},i}\colon N_{\mathrm{obs},i}\to\mathbb{R}$ is given by $h_{0,\mathrm{obs},i}(x)=x-d_{\min}$, where $d_{\min}\geq 0$ is a minimum clearance margin.

*Joint limits* for joint $j$ are encoded on the task manifold $N_{\mathrm{lim},j}=\mathbb{R}$ with task map $f_{\mathrm{lim},j}\colon M\to N_{\mathrm{lim},j}\colon\sigma\mapsto\sigma^{j}$. The safety functions $h_{0,j}^{-},h_{0,j}^{+}\colon N_{\mathrm{lim},j}\to\mathbb{R}$ are $h_{0,j}^{-}(x)=x-\sigma^{j}_{-}$ and $h_{0,j}^{+}(x)=\sigma^{j}_{+}-x$, for $j=1,\ldots,7$. Both families have relative degree 2 with respect to the task state. Each safety function yields a linear constraint on $\ddot{\sigma}$ via Theorem IV.1. ‣ IV-B Task manifold ECBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation").

### IV-C Task manifold BCBF

Here we derive the BCBF safety constraint for the PBDS system. Note that by Assumption 1. ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation"), the task map $f$ is a surjective submersion, so the system is fully actuated on $N$.

### Lemma IV.2

In the task manifold PBDS setup, the BCBF candidate $h$ given in (25 ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) has time derivative The proof is given in Appendix X.

### Theorem IV.3 (Task manifold BCBF)

The function $h$ in (25 ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) is a task manifold BCBF on $T\Omega_{0}$ for a PBDS system if for all $(\sigma,\dot{\sigma})\in TM$ with $(f(\sigma),df\,\dot{\sigma})\in T\Omega_{0}$, where $x=f(\sigma)$, $\dot{x}=df\,\dot{\sigma}$, and $h$, $\dot{h}$ are given by (25 ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) and.

### Proof

We verify (46. ‣ IV-C Task manifold BCBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) for all $(\sigma,\dot{\sigma})\in TM$ with $(f(\sigma),df\,\dot{\sigma})\in T\Omega_{0}$. Let $x=f(\sigma)$ and $\dot{x}=df\,\dot{\sigma}$. If $e_{x}=0$ (i.e. $\dot{x}=\tilde{\xi}$), the $\varepsilon$-terms in vanish and where the inequality follows from Lemma III.2. ‣ Step 1: Construct a safe velocity field. ‣ III-C2 Backstepping CBF (BCBF) ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation"), and the last equality from $h(x,\dot{x})=h_{0}(x)$ whenever $e_{x}=0$ by (25 ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")). If $e_{x}\neq 0$, the term $-\varepsilon\langle e_{x},df({}^{M}\!\nabla_{\dot{\sigma}}\dot{\sigma})\rangle_{N}$ in is affine in $\ddot{\sigma}$, with linear coefficient $-\varepsilon\,g_{\alpha\beta}\,e^{\beta}\frac{\partial f^{\alpha}}{\partial\sigma^{k}}$ (free index $k$ on $M$). Since $f$ is a submersion ($Jf$ has full row rank) and $e_{x}\neq 0$, this coefficient is nonzero, so $\dot{h}$ can be made arbitrarily large by choosing $\ddot{\sigma}\in T_{\sigma}M$, giving $\sup\dot{h}=+\infty$. ∎

### Remark 10

Assumption 1. ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation") ensures the system can be controlled in any direction on the tangent space of the task manifold, so the supremum over accelerations is unbounded if $e_{x}\neq 0$. This significantly simplifies the CBF design process.

### Proposition 1 (Task manifold safety under BCBF)

Let $\tilde{\xi}$ be a safe velocity field as in Lemma III.2. ‣ Step 1: Construct a safe velocity field. ‣ III-C2 Backstepping CBF (BCBF) ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation"), and let $\ddot{\sigma}$ satisfy the non-strict BCBF constraint $\dot{h}\geq-\alpha(h(x,\dot{x}))$ for all $(x,\dot{x})\in T\Omega_{0}$. For any initial state with $h(x,\dot{x})\geq 0$, the closed-loop trajectory satisfies $x(t)\in\mathcal{C}_{0}$ for all $t\geq 0$.

### Proof

Since $\alpha\in\mathcal{K}_{\infty}^{e}$ satisfies $\alpha=0$ and is strictly increasing, the non-strict constraint $\dot{h}\geq-\alpha(h)$ implies forward invariance of $\{h\geq 0\}$ by the comparison lemma, so $h(x(t),\dot{x}(t))\geq 0$ for all $t\geq 0$. Since $h_{0}(x)\geq h(x,\dot{x})$ by (25 ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")), we conclude $h_{0}(x(t))\geq 0$, and hence $x(t)\in\mathcal{C}_{0}$ for all $t\geq 0$. ∎

### Remark 11

Unlike the ECBF formulation, the BCBF depends on the choice of Riemannian metric on $N$: the safe velocity field $\tilde{\xi}$, the velocity error norm $\|e_{x}\|_{N}$, the covariant derivative $\nabla_{\dot{x}}\tilde{\xi}$, and the inner product in all involve the metric. Intuitively, this is because the backstepping construction compares the current velocity $\dot{x}$ against the safe velocity field $\tilde{\xi}$ using the metric on $N$.

### Remark 12 (Strict vs. non-strict inequalities)

The ECBF constraint (41. ‣ IV-B Task manifold ECBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) uses a non-strict inequality ($\geq$), following, with the regularity condition (that $0$ is a regular value of $h_{0}$) assumed in Definition III.3. ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation"). The BCBF constraint (46. ‣ IV-C Task manifold BCBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) uses a strict inequality ($>$), following. The strict inequality is a stronger condition: it implies regularity \[11, Remark 1\], but not vice versa, since it additionally requires the existence of a control input that makes $h$ strictly increase on $\{h=0\}$. In the backstepping construction, this strict margin arises naturally from the $\delta\,\operatorname{grad}h_{0}$ augmentation in (23 ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")). Note that the actual enforcement constraint used in Proposition 1. ‣ IV-C Task manifold BCBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation") is the non-strict $\dot{h}\geq-\alpha(h)$; the strict inequality in Theorem IV.3. ‣ IV-C Task manifold BCBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation") establishes that valid controls exist.

### Remark 13 (Recovery outside $\mathcal{C}_{0}$)

For the BCBF, if $h_{0}$ is smooth on all of $N$, the half-Sontag formula (20 ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) produces a globally smooth safe velocity field $\tilde{\xi}$, so the candidate $h$ (25 ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) is well-defined on all of $TN$. The non-strict enforcement constraint $\dot{h}\geq-\alpha(h)$ is then satisfiable everywhere: when $e_{x}\neq 0$, full actuation makes the supremum unbounded; when $e_{x}=0$, the half-Sontag formula guarantees $d(h_{0})_{x}\,\tilde{\xi}\geq-\alpha(h_{0}(x))$ globally. If $h<0$, a comparison argument using $\alpha\in\mathcal{K}_{\infty}^{e}$ shows $h(t)\to 0$, recovering safety. The domain $\Omega_{0}$ from Lemma III.2. ‣ Step 1: Construct a safe velocity field. ‣ III-C2 Backstepping CBF (BCBF) ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation") is only required for the strict inequality in Theorem IV.3. ‣ IV-C Task manifold BCBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation"), which establishes $h$ as a CBF in the formal sense, but does not limit the practical recovery behavior.

### Remark 14 (Practical considerations)

In practice, finite differencing is often used to compute derivatives and smooth functions that are Lipschitz continuous but not everywhere differentiable. Additionally, due to numerical errors and latency, it is possible to get small CBF violations despite satisfying CBF constraints. Such issues may be mitigated by padding the safety function in (13. ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) by a small margin $\epsilon_{\mathrm{pad}}>0$, which we apply in our implementation.

## Task manifold actions

In the autonomous SafePBDS framework (Definition IV.1. ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")), runtime decision-making is limited to adjusting the weighting pseudometrics $w_{i}$. However, one may wish to steer the system directly in a task manifold $N$, for example to incorporate commands from a higher-level planner or a learned policy. We therefore propose a mechanism that exposes control inputs while preserving the safety and compositional structure of the PBDS framework. We seek the following desiderata: The action space may be lower dimensional than the configuration dimension $m$.

If so desired, all $m$ dimensions may be controlled.

The action represents a residual force on top of the autonomous PBDS dynamics: when the action is zero, the system follows the autonomous behavior.

To this end, consider $L$ *control task maps* $f_{l}:M\rightarrow N_{l}$, $l=1,\ldots,L$, each equipped with a weighting pseudometric $w_{l}$ on $TN_{l}$ and a Riemannian behavior metric $g_{l}$ on $N_{l}$. These may coincide with some of the $K$ autonomous task maps, or they may be entirely separate. For each control task, the user supplies a force-like input $u_{l}\in T^{*}\!N_{l}$, which is converted to an acceleration-level quantity via the sharp (musical isomorphism) $u_{l}^{\sharp}=g_{l}^{\sharp}(u_{l})\in TN_{l}$ (in coordinates, $g_{l}^{-1}\,u_{l}$).

### Definition V.1 (Steerable SafePBDS)

Let $\bar{a}$ be the optimal autonomous acceleration (27. ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")). Given $L$ control inputs $u_{l}\in T^{*}\!N_{l}$, each defined in control task manifolds $f_{l}:M\rightarrow N_{l}$, the acceleration under action input is where $S_{i}$ and $Z_{i}$ are defined in Section III-B ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation").

The first term is identical to the autonomous objective (10. ‣ III-B Pullback bundle dynamical system (PBDS) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")); the second term shifts the autonomous acceleration by the control input $u_{l}^{\sharp}$. Since $Z_{i}$ is affine in the acceleration and the constraint set $\mathcal{D}_{\dot{\sigma}}\cap\mathcal{A}_{\mathrm{safe}}$ is characterized by linear inequalities (Section IV), the steered problem (48. ‣ V Task manifold actions ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) remains a convex QP and can be solved with the same infrastructure as the autonomous problem. Algorithm 1 summarizes the per-step procedure with the safety constraints written out.

0: state (σ, σ̇) ∈ TM; behavior tasks {(fi, gi, Φi, ℱD, i, wi)}i = 1K; safety tasks indexed by 𝒥E (ECBF, Theorem IV.1) and 𝒥B (BCBF, Theorem IV.3); control tasks {(fl, gl, wl, ul)}l = 1L. 0: coordinate acceleration $\ddot{\sigma}\in T_{\sigma}M$. 3: intersect 𝒜safe with the half-space $$\tfrac{\partial(h_{0,j}\circ f_{j})}{\partial\sigma^{k}}a^{k}\geq-\tfrac{\partial^{2}(h_{0,j}\circ f_{j})}{\partial\sigma^{k}\partial\sigma^{\ell}}\dot{\sigma}^{k}\dot{\sigma}^{\ell}\\-\kappa_{2,j}\dot{h}_{0,j}-\kappa_{1,j}h_{0,j}$$ 6: intersect 𝒜safe with ḣj(σ, σ̇, a) ≥ −αj (hj(xj, ẋj)), where ḣj is given by 8: QP 1 (autonomous safe acceleration): $$\bar{a}\leftarrow\operatorname*{arg\,min}_{a\in\mathcal{A}_{\mathrm{safe}}}\ \sum^{K}_{i=1}\tfrac{1}{2}\lVert Z_{i}(a)-S_{i}(\dot{\sigma})\rVert^{2}_{F_{i}^{*}w_{i}}$$ 9: QP 2 (steered acceleration): solve for $\ddot{\sigma}$ given ā, with a ∈ 𝒜safe 10: return $\ddot{\sigma}$ Algorithm 1 SafePBDS control step

### Theorem V.1 (Autonomous behavior recovery)

If all control inputs $u_{l}=0$, $\bar{a}$ is a minimizer of (48. ‣ V Task manifold actions ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")).

### Proof

Since $Z_{i}$ is affine in $a$ and the feasible set $\mathcal{D}_{\dot{\sigma}(t)}\cap\mathcal{A}_{\mathrm{safe}}$ is characterized by linear constraints (Section IV), Equation (48. ‣ V Task manifold actions ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) is a convex QP for which the KKT conditions are necessary and sufficient. Let $Aa\leq b$ denote the assembled linear constraints. Setting $u_{l}=0$, the KKT stationarity condition of (48. ‣ V Task manifold actions ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) is with $Aa\leq b$, $\lambda\geq 0$, and $\lambda^{\top}(Aa-b)=0$.

By construction, $\bar{a}\in\mathcal{D}_{\dot{\sigma}(t)}\cap\mathcal{A}_{\mathrm{safe}}$, so primal feasibility holds. Since $Z_{l}$ is affine in $a$, the gradient of $\lVert Z_{l}(a)-Z_{l}(\bar{a})\rVert^{2}_{F_{l}^{*}w_{l}}$ vanishes at $a=\bar{a}$. The stationarity condition thus reduces to that of the autonomous problem (Definition IV.1. ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")), which $\bar{a}$ satisfies with optimal autonomous problem dual variables $\bar{\lambda}$. As the feasible set is identical, all KKT conditions are satisfied and $\bar{a}$ minimizes (48. ‣ V Task manifold actions ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")). ∎

### Remark 15

If one interprets $\bar{a}$ as the resulting acceleration of a task manifold SMCS (Equation (1. ‣ III-A Differential geometry and geometric mechanical systems ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation"))), the second sum in (48. ‣ V Task manifold actions ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) acts as an additional task manifold force.

### Remark 16

$\bar{a}$ is not necessarily a unique minimizer. In practice, since $\bar{a}$ is used to warm start the numerical solver, it is typically selected when all $u_{l}=0$.

### Remark 17 (Desiderata)

The three desiderata from the beginning of this section are satisfied by construction: each control task map $f_{l}:M\rightarrow N_{l}$ may have $n_{l}\leq m$, so the total action dimension $\sum_{l=1}^{L}n_{l}$ can be less than $m$; if the control task maps collectively form a submersion (i.e., $\operatorname{rank}\bigl[\,Jf_{1}^{\top}\cdots Jf_{L}^{\top}\bigr]=m$), all $m$ degrees of freedom are controllable; and Theorem V.1. ‣ V Task manifold actions ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation") guarantees that zero control input recovers the autonomous behavior.

### Example 1 (continued)

To expose a one-dimensional action space that selects among qualitatively distinct avoidance behaviors (e.g. routing the elbow on either side of a workspace obstacle), we use a control task map given by the coordinate projection onto joint 1, with identity behavior metric $g=1$ and a positive scalar weighting pseudometric $w$. The action input $u\in\mathbb{R}$ injects an acceleration on joint 1; flipping the sign of $u$ steers the arm into a different homotopy class of safe paths around the obstacle, while $u=0$ recovers the autonomous behavior by Theorem V.1. ‣ V Task manifold actions ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation"). This is demonstrated in Section VII-B.

## Evaluation: Simulated $\mathbb{S}^{2}$ Double Integrator

Using a point robot on $\mathbb{S}^{2}$, we first validate the theoretical properties of SafePBDS, in particular chart invariance, safety guarantees, multi-task composition, and effects of our action space design. All experiment configurations in this section are summarized in Table II. Additional details are available in Appendix XI.

### VI-A System Setup

### System definition

Consider a point robot with unit mass traveling on the surface of a unit sphere. The configuration manifold of the robot is $\mathbb{S}^{2}$, which has a natural embedding $\bar{\varphi}:\mathbb{S}^{2}\hookrightarrow\mathbb{R}^{3}$. We consider the atlas $\left\{(U_{N},\varphi_{N}),(U_{S},\varphi_{S})\right\}$ formed by the north and south pole stereographic projection charts. We can define corresponding maps $\bar{\varphi}_{N}:\mathbb{R}^{2}\rightarrow\mathbb{R}^{3}$ and $\bar{\varphi}_{S}:\mathbb{R}^{2}\rightarrow\mathbb{R}^{3}$ from chart coordinates $(y_{1},y_{2})$ to embedding coordinates $(x_{1},x_{2},x_{3})$.

### Configuration Dynamics

Since PBDS does not account for the configuration manifold geometry (Remark 3 ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")), we treat the chart coordinates as $\mathbb{R}^{2}$ and integrate with a fourth-order Runge--Kutta scheme when simulating the system forward.

### Task Dynamics

Following, we use the chart-to-embedding task map $f=\bar{\varphi}_{\alpha}\colon\mathbb{R}^{2}\to\mathbb{R}^{3}$, with an attractor potential and dissipative force defined on the embedding $\mathbb{R}^{3}$.

### Safety constraint

We choose the safety task as staying at least arclength $r$ from a point $x_{o}\in\mathbb{S}^{2}$. The safety function (Definition III.3. ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) is $h_{0}(y)=\arccos\!\bigl(\bar{\varphi}_{\alpha}(y)\cdot x_{o}\bigr)-r,$ with $\alpha\in\{N,S\}$ the active chart. The safe set is $\mathcal{C}_{0}=\{y\in\mathbb{R}^{2}:h_{0}(y)\geq 0\}$. For BCBF, we set $\xi=0$ and compare two metrics: the round metric $g_{ij}=\frac{4}{(1+\|y\|^{2})^{2}}\delta_{ij}$, which is the pullback of the embedded $\mathbb{S}^{2}$ metric through the stereographic chart, and the flat metric $\delta_{ij}$, which treats the chart coordinates as Euclidean.

Safety (chart, metric) Autonomous: metric dependence and chart switching BCBF (Switch, round) Autonomous: safety recovery TABLE II: Run configurations for the 𝕊2 double integrator experiments.

### VI-B Autonomous SafePBDS on $\mathbb{S}^{2}$

First, we validate the theoretical properties of ECBFs and BCBFs in SafePBDS without task manifold actions, shown in Figure 2(a--b).

### Metric dependence and chart switching

As expected from Remark 7. ‣ IV-B Task manifold ECBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation"), ECBF is metric-independent. The two BCBF runs produce visibly different avoidance trajectories, since BCBF depends on the metric via $\operatorname{grad}h_{0}$, $\|e_{x}\|_{N}$, and $\nabla_{\dot{x}}\tilde{\xi}$; the BCBF also stays farther from the unsafe set boundary due to the additional "safe velocity tracking error" penalty (second term in ). We verify chart switching by varying the configuration manifold chart between north and south. This is the safety-augmented analogue of the chart switching experiment in \[6, Fig. 5\]. Run (iv) matches the fixed-chart reference (i) on $\mathbb{S}^{2}$, confirming that the SafePBDS produce consistent behavior across chart choices and can be deployed on atlases with multiple charts.

### Safety recovery

To test recovery, we run both an ECBF and a BCBF trajectory starting from inside the unsafe set. Both formulations drive the system out of the unsafe region and converge to the goal. The ECBF constrains only $h_{0}\geq 0$ and recovers along the most direct path. The BCBF's safe velocity field deviation penalty causes its recovery to maintain a larger clearance from the obstacle boundary.

Figure 2: Pullback CBF and action interface on 𝕊2; run indices match Table II and the legend. (a) Autonomous runs (i)–(vii) on the same scene; recovery runs (vi)–(vii) start inside the obstacle (× marker). (b) h0(t) (top, shaded region is h0 < 0) and geodesic distance to goal (bottom) for the same runs. (c) (viii)–(xii): tangential actions ±u⟂ select opposite homotopy classes, uunsafe is clipped by the CBF, and (xii) repeats (x) on the south pole chart to verify chart invariance.

### VI-C Steered SafePBDS on $\mathbb{S}^{2}$

Next, we demonstrate the properties of the task manifold actions (Section V). We use an ECBF safety constraint and an identity control task map $f_{l}=\mathrm{id}\colon\mathbb{R}^{2}\to\mathbb{R}^{2}$ on the active chart. We place the obstacle so the system faces two valid avoidance paths on each side of the obstacle. We run five trajectories (viii)-(xii), all shown in Figure 2(c): *Autonomous* ($u=0$): the system breaks symmetry via a small positional offset and converges to one side.

*$+u_{\perp}$*: a tangential action perpendicular to the start--goal geodesic with $\|u_{\perp}\|=1$, steering the robot to the same side as the autonomous bias.

*$-u_{\perp}$*: flipping the sign steers the robot to the opposite side, resolving the topological ambiguity that the autonomous dynamics alone cannot.

*$u_{\mathrm{unsafe}}$*: a large action ($\|u\|=10$) continuously pointing toward the obstacle center. SafePBDS prevents the constraint violation, and safety is maintained ($h_{0}(t)\geq 0$) despite the adversarial action.

*$-u_{\perp}$ on the south pole chart*: we repeat (x) on the south pole chart to verify chart invariance under action inputs.

## Evaluation: Simulated 7-DOF Robot Arm

We instantiate the running 7-DOF arm scenario (Example 1. ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) in MuJoCo to validate the pullback CBF for workspace obstacle avoidance and the action space formulation for behavior modality selection. The arm starts at its home configuration; goals and obstacles vary per experiment as detailed below. Additional details are provided in Appendix XII.

### VII-A Autonomous SafePBDS on the 7-DOF Arm

We validate the pullback ECBF by comparing the full SafePBDS system against an ablation that removes the obstacle avoidance ECBFs while keeping joint limit ECBFs active. We test end effector tracking in two setups:

### 6-DOF pose ($\mathrm{SE}$) tracking

A spherical obstacle (radius $0.10$ m) is placed in between the start and goal positions. Figure 3(a) shows the full system (purple) deflecting around the obstacle, while the ablation (red, dashed) passes through it. Both converge to the goal pose.

### Random orientation ($\mathrm{SO}$) tracking

We sample 50 scenarios that each track a goal orientation (a $30^{\circ}$-$150^{\circ}$ rotation about a random axis) with a randomly placed spherical obstacle (radius $8$ cm). Position tracking is forfeited due to the difficulty of randomly finding a reachable goal pose under the obstacle avoidance constraint. Scenarios with obstacle clearance below $5$ cm are rejected and resampled. The full system is safe in all 50 runs (min $h_{\mathrm{obs}}=+0.010$), whereas the ablation violates the obstacle constraint in 11 of 50 runs (min $h_{\mathrm{obs}}=-0.080$); all runs reach the goal orientation.

### VII-B Steered SafePBDS on the 7-DOF Arm

We validate the action interface (Section V) using end effector position ($\mathbb{R}^{3}$) tracking, which leaves four redundant degrees of freedom for the action input to exploit. When an obstacle lies in the robot's workspace, the deterministic autonomous system defaults to one avoidance path, yet multiple safe paths exist. The action inputs allow an operator or high-level planner to select among these configurations with minimal input, instantiating the homotopy class selection application described in the running example (Example 1. ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")). We apply a brief constant scalar action on the first joint: $u=\pm 15$ for the first 3.5 s, then $u=0$. Flipping the sign of this scalar results in trajectories of distinct homotopy classes: the $+u$ arm (blue) passes on one side while the $-u$ arm (purple) passes on the other (Figure 3(b)). Both trajectories converge to the goal while preserving safety. This highlights a key practical advantage of the steered SafePBDS: qualitatively different behaviors can be selected using simple, transient inputs, while the autonomous dynamics and safety constraints handle the details of the motion.

Figure 3: 7-DOF arm: workspace safety and steered action. (a) Obstacle avoidance during 6-DOF pose tracking: the full system (purple) deflects around the obstacle, while the ablation without the obstacle CBF (red, dashed) passes through it (penetration in orange); coordinate frames at equal arc length intervals show orientation converging to the goal. (b) Behavior selection with action inputs and position-only (ℝ3) tracking: flipping the sign of a single joint 1 action steers the forearm to opposite sides of the obstacle (blue vs. purple), while the end effector converges to the same position goal (green); the initial configuration (gray) and final silhouettes are shown for reference.

## Evaluation: Hardware Experiments

We validate SafePBDS on hardware with two dexterous manipulation tasks: autonomous grasping of diverse household objects (Section VIII-C) and in-hand reorientation via finger gaiting (Section VIII-D ‣ VIII Evaluation: Hardware Experiments ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")).

### VIII-A Robot Setup

All hardware experiments are performed with a Franka Emika Panda 7-DOF arm and a Wonik Allegro 16-DOF dexterous hand, for a combined 23-DOF system. The arm is controlled at 20 Hz via the Deoxys framework, using the joint impedance controller when PBDS is active, and the joint position controller for the pre-grasp approach. The hand is commanded over ZMQ using a mix of joint-level PD and Cartesian fingertip impedance modes. Runtime perception uses an Intel RealSense D435 camera with Segment Anything for segmentation and FoundationPose for 6-DOF pose tracking at 10 Hz, which updates an object pose in a MuJoCo simulation that the PBDS controller runs against. Object meshes are obtained by scanning with KIRI Engine on a LiDAR-equipped iPhone. Full control, perception, and modeling details are given in Appendix XIII.

Figure 4: Hardware setup for the dexterous manipulation experiments: a 7-DOF arm equipped with a 16-DOF dexterous hand, a camera for runtime perception, and household objects used for grasping and in-hand reorientation.

Figure 5: 4-finger grasp examples across representative object categories. All four fingers form a force closure grasp under SafePBDS, with the per-finger fingertip-to-object distance and centroid centering action tasks driving the fingertips onto the object surface.

### VIII-B Manifold Setup and Task Specification

The configuration manifold $M=\prod_{i=1}^{m}(\sigma^{i}_{-},\,\sigma^{i}_{+})$ is an open subset of $\mathbb{R}^{m}$ equipped with the flat product metric. The combined arm-hand system used for dexterous grasping has $m=23$; for in-hand reorientation (Section VIII-D ‣ VIII Evaluation: Hardware Experiments ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) the arm is controlled separately and $m=16$.

The grasping and finger-gaiting behaviors share the same overall structure: a joint space PBDS damping task, a family of pullback ECBF safety tasks, and task manifold action tasks driven by a higher-level planner. The safety tasks comprise (i) joint limit ECBFs; (ii) force closure ECBFs based on the $l^{*}$ metric for one four-finger-grasp variant and four per-finger-excluded variants; (iii) fingertip lift-distance ECBFs that keep each non-grasping fingertip away from the object surface; (iv) pairwise finger-finger distance ECBFs that prevent fingertip collisions; (v) per-fingertip table avoidance ECBFs; and (vi) link-object distance ECBFs that keep non-fingertip links clear of the object (per-link CBFs for grasping; per-finger distal phalanx ECBFs for in-hand reorientation). The action tasks expose a per-finger controller on the 1D fingertip-to-object distance. For grasping, additional controllers on the 3D palm position and on the 3D average fingertip position. For in-hand reorientation, an additional action task drives the gaited fingertip's 3D position toward a planner-supplied target in the frame of the contact plane spanned by the three in-contact fingertips. In total, $84$ ECBF tasks are instantiated for the grasping policy and $61$ for the in-hand reorientation policy, a subset of which is active at each control step.

A finite-state machine modulates task weights to coordinate the grasp and gaiting phases. It selects the active force closure variant as fingers enter or leave contact, and toggles the per-finger lift-distance CBFs depending on whether each finger is stationary or in transit. The full enumeration of task maps, safety functions, and ECBF gains is given in Appendix XIII.2.

### VIII-C Dexterous Grasping

We apply SafePBDS to autonomous grasping of diverse household objects.

### VIII-C1 Scene Setup and Test Protocol

We select 20 household objects (Fig. 4) with mass ranging from $64$ to $613$ g and longest bounding box dimension ranging from roughly $6$ to $29$ cm. At the start of each trial, FoundationPose reports the object's 6-DOF pose, and a wrist pose sampler proposes top-down wrist pose candidates that are filtered for reachability, clearance, and aperture fit. The top-ranked candidate is executed in two stages: first, a Deoxys-controlled approach to the wrist pose (via a $15$ cm waypoint above the pose followed by a direct descent); second, SafePBDS takes over the full $23$-DOF arm-hand system and runs the PBDS QP at each control step. During the SafePBDS phase, two action tasks are composed: per-finger 1D fingertip-to-object distance controllers that drive each fingertip onto the object surface, and a 3D average-fingertip centering controller that aligns the four-fingertip centroid with the object's geometric center, for a total of $4\times 1+3=7$ action dimensions. The force closure ECBF (Section VIII-B) is activated as the fingertips approach the object, so that the final squeeze converges to a certified force-closed grasp. A trial is recorded as a *success* if the object is successfully lifted with all four fingers in contact, a *partial success* if it is stably lifted with one finger not in contact, and a *failure* otherwise. The candidate filtering pipeline, action gain schedule, and full execution protocol are given in Appendix XIV.

To showcase the flexibility of our framework, we additionally evaluate grasping with one of the four fingers excluded. The active force closure ECBF is switched to the per-finger-excluded variant, so that $l^{*}$ is computed over the three in-contact fingers, while the excluded finger is held clear of the object by retargeting its fingertip-to-object distance action to a fixed clearance and enabling its fingertip lift-distance ECBF. No other policy modification is required.

### VIII-C2 Results

Figure 7 summarizes the 4-finger grasping results (per-object trial counts in Table A2 of Appendix XIV). Figure 5 shows representative 4-finger executions, and Figure 6 shows the 3-finger variants for each excluded finger.

Figure 6: 3-finger grasping variants for the three test objects. Each image is labeled with the excluded finger, which is held clear of the object while the remaining three fingers form a force closure grasp under SafePBDS. Across the three objects and four exclusions, tested at three table locations each (36 trials), SafePBDS achieves 34/36 (94.4%); both failures occur on the wide object (bottom row) with the thumb excluded, where its width forces the remaining index–ring pinch to span near the limits of the hand’s reachable workspace. Per-object counts are listed in Appendix Table A3.

Figure 7: Per-(object, pose) grasp outcomes plotted against object weight and the vertical bounding-box length at the tested pose. Marker color encodes the per-group success score (success = 1, partial = 0.5, failure = 0, averaged over the 2–6 trials in each group, shown on a 0–100% scale); shape encodes which bounding-box axis is oriented upward (longest, middle, or shortest); and size is proportional to trial count.

SafePBDS achieves an overall success rate of $111/120$ ($92.5\%$) on the $20$ household objects, with $15$ of $20$ attaining full $6/6$ success. Figure 7 plots each (object, pose) trial group against object weight and the vertical bounding-box length at that pose. Partial successes and failures concentrate among objects with small vertical extents (roughly $\leq 10$ cm) and high weight. Low vertical extent is less forgiving of pose estimation errors and leaves less table clearance, while high weight requires grasp forces that approach the limits of the low-level impedance controller and the hand's hardware capabilities.

The 3-finger ablation (Figure 6) succeeds in $34/36$ trials ($94.4\%$): thanks to the autonomous PBDS behavior, a high-level decision policy can reliably choose which finger to exclude despite the complexity of dexterous precision grasping.

### VIII-D Palm-Down In-Hand Reorientation (IHR)

We apply SafePBDS to palm-down IHR, where the goal is to rotate a grasped object about the palm normal axis with the palm normal facing down. This is significantly more challenging than the more common "IHR with palm facing up" in literature (e.g. ); with the palm facing down, the object must be securely grasped throughout the process. To tackle the combinatorial complexity of finger gaiting sequences, we leverage offline planning in simulation to discover feasible reorientation trajectories, which are then deployed on hardware.

### VIII-D1 Simulation Pre-Planning

The main challenge in IHR is choosing which finger to move and where to move it. We address this with a depth-first tree search over finger-object contact states, where each node has all four fingers in contact and each edge corresponds to relocating one finger. The search tree is rooted at an initial grasp obtained by reusing the top-down grasping pipeline of Section VIII-C on a $6$ cm diameter bottle. A priority queue at each depth orders nodes by the cumulative $z$-axis yaw rotation achieved along the path from the root, while a balance constraint caps the disparity in per-finger move counts so that no single finger is overused.

For each movable finger at a node, $12$ candidate extensions are generated by a predetermined grid of steps along the object surface. Fingers are not allowed to move consecutively and the max gaiting step count difference across fingers is 1. This leaves at most $3$ movable fingers and a maximum branching factor of $36$. To prevent the search from getting stuck with a never-movable finger, a cyclic sequence of "next movable" fingers is assigned so that at each tree depth, the "next movable" finger must be movable after the candidate extension. Each candidate is forward-simulated under SafePBDS and a four-phase (LIFTING, TRAVERSING, DROPPING, ADJUSTING) primitive, and an accepted candidate becomes a tree edge. Throughout the primitive, the three-finger grasp is maintained by the corresponding force closure ECBF and pairwise fingertip spacing ECBFs (the object itself may still move). In TRAVERSING and DROPPING, the force closure ECBF excluding the next movable finger is additionally activated. A candidate is accepted when, on reaching ADJUSTING, the moving finger is aligned with its target contact, the hand is at rest, all four fingers are back in contact, the force closure ECBF excluding the next movable finger is non-negative, and the object tilt from the rotation axis is below $10^{\circ}$. Loss of contact at any in-contact finger during the rollout aborts execution and rejects the candidate. A simplified illustration is shown in Figure 1. More details are given in Appendix XV. Figure 8 ‣ VIII Evaluation: Hardware Experiments ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation") shows the resulting search trees.

(a) Clockwise rotation, static arm (b) Counterclockwise rotation, swinging arm with weighted object Figure 9: In-hand reorientation on hardware. Snapshots are arranged temporally from left to right.(a) Clockwise rotation with the arm held static and empty bottle. (b) Counterclockwise rotation with the arm swinging and 2.5 oz loose weight in the bottle, demonstrating robustness under load and motion.

### VIII-D2 Scene Setup and Test Protocol

A human operator places the object in between the finger cage, and the fingers grasp the object using the initial grasping configuration in the motion plan. The joint angles from the planned finger gaiting sequence are then played back open loop. To evaluate robustness of our plans, we test each plan under three conditions: (i) with the arm held static and no added payload, (ii) with the arm held static and up to 98 grams of weight incrementally added into the bottle, and (iii) with the arm swinging and 70 grams of loose weight inside the bottle.

### VIII-D3 Results

Figure 9 ‣ VIII Evaluation: Hardware Experiments ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation") illustrates examples of the task execution. Using the same open loop motion plan across all three conditions, SafePBDS achieves over $360^{\circ}$ rotation in both directions. We attribute this robustness to the fact that our IHR plan is certifiably in force closure. This demonstrates that SafePBDS offloads the burden on a higher-level planner (in this case the tree search) and allows a simple strategy to achieve highly constrained and difficult manipulation tasks.

Figure 8: Offline IHR motion plan trees for (a) clockwise and (b) counterclockwise target rotations. Each node represents a finger gaiting state, and the highlighted path from the root achieves the largest cumulative yaw.

## Discussion

This paper presents SafePBDS (Safe Pullback Bundle Dynamical Systems), a geometric motion generation framework that extends PBDS with task manifold safety guarantees and an action interface. At each control step, two convex QPs are solved sequentially: the first defines the autonomous safe acceleration, and the second injects the action input around it. The resulting configuration space acceleration is certifiably safe and recovers the autonomous task dynamics when the action input vanishes. We validate its theoretical properties in simulation on an $\mathbb{S}^{2}$ double integrator and a 7-DOF Franka arm. On a 23-DOF Franka--Allegro hardware system, SafePBDS attains $92.5\%$ grasp success across 20 household objects, and $94.4\%$ for 3-finger grasps through simple action changes enabled by the action interface. Finally, SafePBDS enables the first model-based robust palm-down in-hand reorientation, producing over $360^{\circ}$ rotation in both directions under varying object weight and arm motion.

### IX-A Limitations

Like other vector-field policies, SafePBDS solves a local motion generation problem: over long horizons, the system may become trapped in local minima, and escaping them must be handled by the higher-level policy that provides the action input. In addition, SafePBDS is kinematic and therefore requires a lower-level tracker to realize the commanded accelerations, or an impedance controller when compliant contact forces are needed. Finally, the pullback derivations assume surjective submersion task maps and a fully or over-actuated robot; underactuated systems are therefore outside the scope of the present framework.

### IX-B Future work

On the application side, an important direction is to combine the action interface enabled by SafePBDS with more advanced decision-making policies, such as reinforcement learning or vision-language-action models. On the theoretical side, relaxing the Assumption 1. ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation") will allow SafePBDS to handle a broader class of objectives, including tasks with singularities or nonsmooth task maps. In addition, incorporating robot dynamics and the contact forces required for manipulation, rather than relying on an acceleration tracker or impedance controller, will allow SafePBDS to reason directly about interaction forces alongside geometric safety.
