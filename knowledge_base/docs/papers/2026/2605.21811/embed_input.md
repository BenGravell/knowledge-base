<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Robotic dexterous manipulation requires continuously reconciling objectives and constraints defined on heterogeneous geometric spaces: a robot controlled on a R^ configuration manifold may need to track end effector poses on SE while satisfying obstacle avoidance margins in R. We present Safe Pullback Bundle Dynamical Systems (SafePBDS), a geometrically consistent framework that computes optimal, certifiably safe configuration manifold accelerations from objectives and safety requirements on arbitrary task manifolds. SafePBDS builds on prior work that combines predefined task manifold dynamical systems to produce autonomous motion. Its first innovation is a pullback control barrier function construction, which converts task manifold safety conditions into linear constraints on configuration manifold accelerations. The second innovation is a task manifold action interface that allows a high-level policy to inject low dimensional residual motions; zero input recovers the autonomous behavior, while safety is preserved under arbitrary inputs. This lets high-level policies efficiently steer exploration while leaving precise motion to the autonomous behavior. We validate SafePBDS in simulation and on a 23-DOF Franka Panda-Allegro Hand platform. On dexterous grasping, SafePBDS achieves a 92.5% success rate across 20 household objects and 120 trials.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Using the action interface, the method can exclude any one of the four fingers during grasping via a one-dimensional action, achieving 94.4% 3-finger grasp success across 3 objects and 36 trials. The efficient planning and safety guarantee of SafePBDS also enables the first model-based, fully actuated palm-down in-hand reorientation, exceeding 360^(circ) of yaw rotation in both directions under varying object weight and wrist motion.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robotic dexterous manipulation requires reasoning over quantities defined on different geometric spaces, including positions in Cartesian space, orientations on $\mathrm{SO}$, and joint limits in generalized coordinates. Some of these quantities correspond to soft objectives, such as null-space redundancy resolution and task prioritization, while others impose hard constraints that must never be violated, such as collision avoidance, closed-loop kinematic constraints, and force closure. Moreover, real-world perturbations and modeling errors require the system to respond quickly via feedback during execution. Successful manipulation therefore demands continuously resolving objectives and constraints defined on heterogeneous geometric spaces in real time.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contemporary data driven methods attempt to sidestep these challenges by learning end-to-end policies that implicitly encode all objectives and constraints. Deep reinforcement learning (DRL) and behavior cloning can capture globally coordinated behaviors and are often straightforward to deploy. However, the resulting policies often remain specialized to a single task or embodiment. Vision-language-action models (VLAs) have shown impressive generalization on arm-gripper manipulation, but their extension to multi-fingered hands remains limited by the complexity of dexterous motion and the difficulty of collecting multi-fingered manipulation data. Additionally, all aforementioned black-box policies can fail catastrophically outside the training distribution, motivating the need to incorporate certifiable structure for safety guarantees.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

At the other end of the spectrum, trajectory optimization can explicitly reason about constraints and dynamics to produce certifiable motion plans. However, solving these optimizations is computationally expensive, prone to getting stuck in local minima, require specific engineering tricks such as fixed contact pairs, and the resulting plans are essentially one-shot. Adapting them to online perturbations requires expensive replanning at rates that are typically incompatible with high-frequency dexterous manipulation control.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A third family of approaches is the *vector field policy*, which maps each state to a desired velocity or acceleration through a globally defined vector field. Because these policies are defined analytically, they enable fast reactive behavior, and properties such as stability can often be certified by construction. Several frameworks compose per-task vector fields using Riemannian geometry, but existing formulations either lack geometric consistency or treat safety as a soft property. Moreover, because most vector field policies are inherently local, they can become trapped in local minima. A recent example, DextrAH-G, combines vector field policies with learning-based methods to mitigate this lack of global planning, but the resulting policies remain limited by the vector field formulation.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Among vector field policies, Pullback Bundle Dynamical Systems (PBDS) stands out for achieving geometric consistency. By building on the coordinate invariant simple mechanical control system (SMCS), PBDS provides a fully geometric formulation that works on arbitrary Riemannian manifolds. However, PBDS has two important limitations. First, *safety constraints are soft*: metric-based constraints enter the optimization as additional weighted objectives and can therefore be violated when they conflict with other tasks; moreover, these objectives may become ill-defined in unsafe regions. Second, *there is no action interface*: the system provides no mechanism for a higher-level policy to inject task manifold commands, limiting its use to autonomous policies fixed at design time.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present SafePBDS (Safe Pullback Bundle Dynamical Systems), a framework that addresses both limitations of PBDS while preserving the geometric and compositional properties. SafePBDS extends PBDS with hard safety guarantees and external controllability while retaining its geometric consistency. At each control step, a constrained quadratic program takes in real-time observations and composes desired autonomous behaviors, safety constraints, and action inputs into a single acceleration target. This is enabled by the following: *Pullback control barrier functions (CBFs)* that enforce task manifold safety as hard constraints on the configuration manifold acceleration by pulling back the constraints through smooth task maps. We derive formulations for two prominent higher-order CBF variants, exponential (ECBF) and backstepping (BCBF), and show their respective dependencies on task manifold geometries.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A *task manifold action interface* that lets a higher-level policy inject inputs on selected task manifolds. Our formulation guarantees that zero input recovers the autonomous behavior and that safety is preserved under arbitrary inputs.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We also provide extensive evaluations of SafePBDS: *Simulation experiments* on an $\mathbb{S}^{2}$ double integrator and a 7-DOF robot arm validate the theoretical properties of our framework: chart invariance, task manifold metric effects, recovery from unsafe states, and the action interface.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Hardware experiments* on a 23-DOF arm--hand system (Franka Panda + Allegro Hand) demonstrate (a) autonomous dexterous grasping of 20 household objects at a 92.5% success rate (111/120 trials), including a 3-finger ablation at 94.4% (34/36); and (b) robust in-hand reorientation under palm-down and variable wrist orientations, achieving over $360^{\circ}$ rotation in both directions.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is organized as follows. Section II reviews related literature. Section III introduces the necessary theoretical background. Section IV derives the pullback ECBF and BCBF formulations. Section V presents the task manifold action interface. Sections VII and VIII present simulation and hardware experiments, respectively.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Multi-task motion planning on manifolds", "weight": 1.0} -->

Reactive multi-objective control in Euclidean task manifolds is classically addressed by operational space control, which composes Cartesian objectives through null space projection. This line of work establishes key ingredients but does not provide a geometrically consistent or coordinate free framework for composing manifold valued tasks.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Multi-task motion planning on manifolds", "weight": 1.0} -->

A major step toward manifold-valued policy composition is the introduction of *Riemannian Motion Policies* (RMPs), which compose acceleration-level policies through metric-weighted pullback; RMPflow later extends this construction to tree-structured task hierarchies. However, the original RMP formulation is not chart-invariant, so the resulting policy depends on the choice of local coordinates. A related line of work is the *Optimization Fabrics* and *Geometric Fabrics* framework, which provides a Finsler-geometric foundation for stable reactive policy design. Across this family of methods, however, safety-related behaviors are typically encoded in the reactive policy itself rather than enforced as hard constraints at runtime. Unresolved geometric consistency issues also leave them short of a complete solution to composing tasks defined on heterogeneous manifolds.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Multi-task motion planning on manifolds", "weight": 1.0} -->

*Pullback Bundle Dynamical Systems* (PBDS) resolves the geometric consistency issue by realizing simple mechanical control systems (SMCSs) on task manifolds and combining them through a metric-weighted least-squares problem. In doing so, PBDS establishes a principled foundation for geometrically consistent control synthesis on manifolds. However, PBDS inherits the broader limitation above: safety-related tasks enter the least-squares objective as soft costs and may therefore be violated under competing task pressures. PBDS also remains purely autonomous, with no mechanism for a higher-level planner or learned policy to steer the system at runtime. Our work addresses both limitations.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Control barrier functions on manifolds", "weight": 1.0} -->

Control barrier functions (CBFs) certify forward invariance of a safe set by imposing an affine inequality on the control input at runtime. The earliest formulations assume the safety function has relative degree one with respect to the input. This assumption fails for systems where position-level safety must be enforced through acceleration-level control. Two families of methods address this higher-relative-degree setting. *Exponential CBFs* (ECBFs) apply pole-placement design to the chain of Lie derivatives of the safety function, collapsing the higher-order condition into a single linear constraint on the input. A related generalization, high-order CBFs (HOCBFs), relaxes the linear pole-placement structure of ECBFs to a sequence of class-$\mathcal{K}$ comparison functions. Backstepping CBFs (BCBFs) instead build a CBF from a safe virtual controller for the lower-order subsystem and lift it to the full system; for second-order systems with position constraints, this construction reduces to lifting a safe velocity field to an acceleration-level constraint.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Control barrier functions on manifolds", "weight": 1.0} -->

Recent work has generalized the CBF methodology beyond Euclidean spaces to manifold-valued states. Wu and Sreenath extend CBF synthesis to mechanical systems evolving on Riemannian configuration manifolds, with demonstrations on the spherical pendulum ($\mathbb{S}^{2}$) and the 3D pendulum ($\mathrm{SO}$). More recently, De Sa et al. develop a general theory of geometric CBFs on control systems defined over bundles, and use it to generalize kinetic-energy CBF backstepping to SMCSs. These works establish geometric CBFs on individual configuration manifolds; SafePBDS instead defines safety on *task* manifolds so that hard constraints naturally expressed in different geometric spaces (e.g. end effector poses and joint angle limits) can be composed with the PBDS task structure.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-C Dexterous manipulation", "weight": 1.0} -->

We focus on two dexterous manipulation problems targeted in our hardware evaluation: multi-fingered *grasping* and *in-hand reorientation*. Both require coordinating objectives and constraints defined on heterogeneous spaces, including force closure and friction-cone conditions in contact space, fingertip and link clearance in Cartesian space, joint limits in the configuration manifold, and reachability in $\mathrm{SE}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-C1 Grasping", "weight": 1.0} -->

The theory of static multi-fingered grasping is well established. We refer the reader to for broader surveys of grasp synthesis and focus on methods that provide explicit physical-feasibility guarantees, as in our work. A central challenge in certifiable grasp synthesis is that precise local constraints must be satisfied while searching over multiple global grasp modalities (see for a grasp taxonomy). This challenge has motivated optimization-based pipelines that incorporate analytical grasp-quality objectives, sometimes used to refine learned grasp predictions. In most such methods, however, the relevant physical conditions enter as relaxed scalar penalties and therefore do not provide strict guarantees on the final grasp. Wu et al. address this limitation by formulating grasp refinement as a bilevel optimization in which force closure is imposed as an exact inner constraint, yielding grasps with certified physical feasibility at the solution. Li et al. further introduce the min-weight metric as a surrogate objective for force closure certification. However, both and certify grasp feasibility offline and do not maintain it online under execution-time perturbations.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-C1 Grasping", "weight": 1.0} -->

Lum et al. combine reinforcement learning with a Geometric Fabric to enforce arm joint limits and collision avoidance during grasp execution, but do not certify grasp conditions such as force closure. Shaw Cortez et al. use a CBF-based safety filter to preserve grasp validity (e.g., preventing slip and singularities) during in-hand adjustments, but do not discuss how the grasp is initially achieved.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-C2 In-hand reorientation", "weight": 1.0} -->

In-hand reorientation can be broadly divided by palm orientation. In the *palm-up* setting, gravity helps retain the object, allowing brief release-and-regrasp maneuvers. In the *palm-down* setting, the object must remain securely grasped throughout the motion. Both have proven challenging, and most prior work has relied on deep reinforcement learning with sim-to-real transfer, beginning with palm-up and extending to palm-down more recently; see for a broader survey. While these learned methods demonstrate impressive dexterity, they do not provide formal safety guarantees and typically require substantial tuning and reward engineering to work on hardware. Analytical approaches are much less common; existing work often exploits mechanical compliance and underactuation to reduce the planning burden. Suh et al. propose a contact-trust-region formulation for contact-rich MPC and demonstrate palm-up cube reorientation with a fully actuated Allegro hand. To the best of our knowledge, our work is the first to achieve palm-down and variable-wrist-pose in-hand reorientation on a fully actuated general-purpose dexterous hand without relying on either machine learning or mechanical compliance.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Example 1 (Reaching with obstacle avoidance)", "weight": 1.0} -->

A 7-DOF Franka Emika Panda arm is to reach a goal end effector pose while avoiding a fixed workspace obstacle. The configuration is given by seven joint angles $\sigma=(\sigma^{1},\ldots,\sigma^{7})$ with joint limits $\sigma^{j}_{-}\leq\sigma^{j}\leq\sigma^{j}_{+}$. Forward kinematics yields the end effector pose and the pose of each link for collision checking. The motion policy must reconcile objectives on heterogeneous spaces: *End effector tracking* in end effector pose.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Example 1 (Reaching with obstacle avoidance)", "weight": 1.0} -->

*Joint limits* in the configuration manifold.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Example 1 (Reaching with obstacle avoidance)", "weight": 1.0} -->

This system is implemented in simulation in Section VII.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Example 1 (Reaching with obstacle avoidance)", "weight": 1.0} -->

Manifolds and Maps Configuration manifold (dimension m) Task manifold for task i (dimension ni) Tangent and cotangent bundles of M Tangent-bundle point; v ∈ TpM Differential and Jacobian of fi Time derivative of Jfi, i.e. vℓ ∂2fi/∂xℓ∂xj Higher-order task map, (p, v) ↦ (fi(p), (dfi)p(v)) Second fundamental form of f Riemannian metrics on M and Ni Inner product of metric g; on N also ⟨⋅, ⋅⟩N Levi-Civita connections on M and N Christoffel symbols on M and N Sharp operator, g♯: T*M → TM (and task manifold analogue) Riemannian gradient: ⟨grad h, v⟩g = dh(v) $\sigma(t),\,\dot{\sigma},\,\ddot{\sigma}$ Configuration curve on M; velocity and coordinate acceleration task manifold curve on N Dissipative force map TNi → T*Ni SMCS input codistribution Weighting pseudometric (task priority) Lower-right block of wi in local coordinates Control input (generalized force

<!-- chunk {"id": "body-0027", "role": "body", "section": "Example 1 (Reaching with obstacle avoidance)", "weight": 1.0} -->

one-form) Affine distribution of second-order vectors at (p, v) Safe acceleration set (pullback CBFs) Vertical-bundle and actuation projections Optimal autonomous acceleration Control task map, input ul ∈ T*Nl, behavior metric, weighting pseudometric Control Barrier Functions (ECBF) Safety function (indexed h0, j for multiple constraints) Safe set {x: h0(x) ≥ 0}, contained in informal safe region 𝒮 ⊆ N Extended class-𝒦∞ function ECBF gain vector; κ⊤ ∈ ℝ1 × r (scalars κ1, κ2 for r = 2) Auxiliary functions and sets in the ECBF recursion; pi are negated eigenvalues of F − Gκ⊤ Backstepping CBF (BCBF) Lifted BCBF candidate on TN Nominal and safe velocity fields on N (pre/post-filter) Half-Sontag safety filter quantities Open domain on which ξ̃ is a strict CBF Strict-margin augmentation and BCBF scaling Numerical padding for h0 (distinct from ε) TABLE I: Notation Summary.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-A Differential geometry and geometric mechanical systems", "weight": 1.0} -->

We present a brief introduction to Riemannian geometry; for further details, we refer the reader to. Let $M$ be a smooth $m$-dimensional manifold with tangent bundle $TM$ and cotangent bundle $T^{*}M$. A *Riemannian metric* $g$ is a smooth assignment of an inner product $g_{p}\colon T_{p}M\times T_{p}M\to\mathbb{R}$ to each point $p\in M$; the pair $(M,g)$ is called a *Riemannian manifold*.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A Differential geometry and geometric mechanical systems", "weight": 1.0} -->

The metric induces the sharp isomorphism $g^{\sharp}\colon T^{*}M\to TM$, which maps each covector $\alpha\in T_{x}^{*}M$ to the unique vector $g^{\sharp}(\alpha)\in T_{x}M$ satisfying The *Riemannian gradient* of a smooth function $h$ is defined by $\operatorname{grad}h=g^{\sharp}(dh)$, or equivalently, $\langle\operatorname{grad}h,v\rangle_{g}=dh(v)$ for all tangent vectors $v$. The Levi-Civita connection induced by $g$ is denoted by $\nabla$, so that the covariant acceleration along a curve $\sigma(t)$ is given by $\nabla_{\dot{\sigma}}\dot{\sigma}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A Differential geometry and geometric mechanical systems", "weight": 1.0} -->

When two manifolds $M$ and $N$ must be disambiguated, we write ${}^{M}\!\nabla$, ${}^{N}\!\nabla$ for their Levi-Civita connections and ${}^{M}\!\Gamma$, ${}^{N}\!\Gamma$ for the corresponding Christoffel symbols.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 1", "weight": 1.0} -->

SMCS is control affine since the sharp map is a linear operator.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 2", "weight": 1.0} -->

$g^{kl}$ converts the force covectors $u$ and $d\Phi$ into accelerations. When $g$ is the kinetic energy metric, $g^{kl}$ plays the role of an inverse mass matrix. $\Gamma^{k}_{ij}\dot{\sigma}^{i}\dot{\sigma}^{j}$ corrects the coordinate acceleration $\ddot{\sigma}^{k}$ into a true acceleration on the curved manifold similar to the Coriolis and centripetal terms.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Example 1 (continued)", "weight": 1.0} -->

For the 7-DOF arm reaching task, the configuration manifold is the open box of joint limits equipped with the flat product metric $g_{M}=\delta_{ij}$. Although the physical joint limits are closed, we use strict inequalities so that $M$ is a smooth manifold without boundary; the distinction makes no difference in practice.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B Pullback bundle dynamical system (PBDS)", "weight": 1.0} -->

In order to construct a motion policy that combines multiple desired task behaviors, proposes designing a stable mechanical control system (SMCS) on each task manifold of interest and combining them via a weighted least-squares optimization over the resulting task accelerations. Consider smooth task maps $f_{i}:M\rightarrow N_{i}$, $i=1,\ldots,K$, that map the configuration manifold $M$ (of dimension $m$) to task manifolds $N_{i}$ (of dimension $n_{i}$).

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B Pullback bundle dynamical system (PBDS)", "weight": 1.0} -->

On each $N_{i}$ one designs an SMCS that exhibits a desired behavior by choosing a potential function $\Phi_{i}:N_{i}\rightarrow\mathbb{R}$, a Riemannian metric $g_{i}$ on $N_{i}$ (together with its Levi-Civita connection $\nabla_{i}$), and a dissipative force map $\mathcal{F}_{D,i}:TN_{i}\rightarrow T^{*}\!N_{i}$. We illustrate the role of $f_{i}$, $g_{i}$, $\Phi_{i}$, and $\mathcal{F}_{D,i}$ on the running 7-DOF arm scenario (Example 1. ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) in the continuation block following Definition III.2.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-B Pullback bundle dynamical system (PBDS)", "weight": 1.0} -->

‣ III-B Pullback bundle dynamical system (PBDS) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation"). Together, these determine a second-order dynamical system on $TN_{i}$, which can be pulled back to a dynamical system on the pullback bundle where $\coprod$ denotes the disjoint union and $\pi_{N_{i}}:TN_{i}\rightarrow N_{i}$ is the tangent bundle projection. Concretely, the fiber of $f_{i}^{*}TN_{i}$ over a point $p\in M$ is the tangent space $T_{f_{i}(p)}N_{i}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-B Pullback bundle dynamical system (PBDS)", "weight": 1.0} -->

Given these pullback constructions, two operators are introduced that capture, respectively, the *desired* task manifold acceleration produced by each local PBDS and the *resulting* task manifold acceleration induced by a candidate configuration manifold acceleration. The first operator, maps a state $(p,v)\in TM$ to the *desired* pullback task acceleration. It is defined as the vertical-bundle projection of the velocity of the local PBDS curve at $(p,v)$: where $G_{i}$ encodes the dynamics of the local PBDS defined by $(f_{i},g_{i},\Phi_{i},\mathcal{F}_{D,i})$, and $\dot{\gamma}^{a}_{v_{p},i}$ is the resulting task manifold acceleration. The pullback construction ensures that $S_{i}$ is globally well-defined; see for a detailed derivation. In local coordinates, the desired acceleration evaluates to The second operator is defined as maps a candidate configuration manifold acceleration to its *resulting* task manifold acceleration.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-B Pullback bundle dynamical system (PBDS)", "weight": 1.0} -->

Let $\mathcal{D}_{\dot{\sigma}(t)}\subseteq T_{\dot{\sigma}(t)}TM$ denote the affine distribution of second-order vectors at $\dot{\sigma}(t)=(p,v)\in TM$, i.e. $\mathcal{D}_{(p,v)}=\{((p,v),(v,a^{a})):a^{a}\in\mathbb{R}^{n}\}$. Additionally, let $w_{i}$ be a Riemannian *weighting pseudometric* on $TN_{i}$ that controls the priority of task $i$ relative to the other tasks, and let $F_{i}:TM\rightarrow TN_{i}$, $(p,v)\mapsto(f_{i}(p),(df_{i})_{p}(v))$ be the higher-order task map.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 3", "weight": 1.0} -->

The multi-task PBDS (10. ‣ III-B Pullback bundle dynamical system (PBDS) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) outputs the coordinate acceleration $\ddot{\sigma}$. The optimization variable $a^{a}\in T_{p}M$ in (10. ‣ III-B Pullback bundle dynamical system (PBDS) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) represents the coordinate second derivative $d^{2}\sigma^{k}/dt^{2}$, and the operators $S_{i}$ and $Z_{i}$ involve only the task manifold metrics $g_{i}$ and weights $w_{i}$. Consequently, the PBDS framework is oblivious to the geometry of $M$. Intuitively, PBDS produces the task manifold desired behavior, which is independent of the robot's configuration manifold dynamics.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 3", "weight": 1.0} -->

In practice, an acceleration tracking controller must be used to track $\ddot{\sigma}$ and account for the configuration manifold dynamics, which stems from the physical system dynamics.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Example 1 (continued)", "weight": 1.0} -->

The end effector tracking objective decomposes into orientation tracking on $\mathrm{SO}$ and position tracking on $\mathbb{R}^{3}$; per, an additional joint space damping task is required for stability. This yields 3 SMCSs on a different manifold: *Orientation tracking* on $N_{\mathrm{ori}}=\mathrm{SO}$, task map $f_{\mathrm{ori}}\colon M\to\mathrm{SO}$ given by the end effector orientation from forward kinematics, attractor potential $\Phi_{\mathrm{ori}}$ centered at a goal orientation, and linear damping $\mathcal{F}_{D,\mathrm{ori}}$. In the implementation we use the unit quaternion parameterization (i.e. the universal double cover $\mathbb{S}^{3}\to\mathrm{SO}$); see Appendix XII.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Example 1 (continued)", "weight": 1.0} -->

*Position tracking* on $N_{\mathrm{pos}}=\mathbb{R}^{3}$ with the identity metric, task map $f_{\mathrm{pos}}\colon M\to\mathbb{R}^{3}$ given by the end effector position, attractor potential $\Phi_{\mathrm{pos}}$ centered at a goal position, and linear damping $\mathcal{F}_{D,\mathrm{pos}}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Example 1 (continued)", "weight": 1.0} -->

*Joint space damping* with identity task map $f_{\mathrm{jd}}=\mathrm{id}_{M}$, no potential, and linear damping $\mathcal{F}_{D,\mathrm{jd}}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Example 1 (continued)", "weight": 1.0} -->

In the implementation, the attractor and damping of each tracking SMCS are realized as separate PBDS tasks on the same manifold, so the multi-task PBDS comprises 5 tasks total (orientation attractor, orientation damping, position attractor, position damping, and joint space damping). These tasks compose into a multi-task PBDS through Definition III.2. ‣ III-B Pullback bundle dynamical system (PBDS) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation") with weighting pseudometrics $w_{i}$ tuned by task priority.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-C Control barrier functions (CBFs)", "weight": 1.0} -->

While multi-task PBDS (11 ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) allows encouraging safe behavior through metric-based constraints \[6, Section III.C\], it does not provide a hard guarantee. Additionally, metric-based constraints are ill-defined in unsafe regions. We now review control barrier functions, which provide the tools to overcome this limitation.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-C Control barrier functions (CBFs)", "weight": 1.0} -->

Consider a safety problem on a task manifold $N$ (e.g. obstacle avoidance constraints for the end effector), where $\mathcal{S}\subseteq N$ denotes a safe region: the system is safe if the state $x\in\mathcal{S}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-C1 Exponential CBF (ECBF)", "weight": 1.0} -->

When the safety constraint $h_{0}$ has relative degree $r\geq 2$ with respect to the control input, i.e. the first $r{-}1$ time derivatives of $h_{0}$ are independent of $u$ and $u$ first appears explicitly in $h_{0}^{(r)}$, the standard relative-degree-one CBF condition cannot be applied directly. The exponential CBF (ECBF) framework of addresses this by enforcing a linear constraint on the $r$th derivative of $h_{0}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-C1 Exponential CBF (ECBF)", "weight": 1.0} -->

By the comparison lemma, under this constraint, $h_{0}(x(t))\geq C\,e^{(F-G\bm{\kappa}^{\top})t}\,\eta_{b}(x_{0})$. Therefore, safety ($h_{0}\geq 0$) is guaranteed if the right-hand side remains nonnegative. To this end, introduces a family of auxiliary functions $\nu_{i}$ and corresponding sets $\mathcal{C}^{\nu}_{i}$: where $p_{1},\ldots,p_{r}$ are the roots of the characteristic polynomial $F-G\bm{\kappa}^{\top}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 4", "weight": 1.0} -->

The totally-negative requirement is stronger than the standard Hurwitz condition, which permits complex eigenvalues with negative real parts. This is because the recursive argument in \[2, Proposition 6 and Theorem 7\] establishes forward invariance of each $\mathcal{C}^{\nu}_{i}$ by showing that $\dot{\nu}_{i-1}\geq 0$ on $\partial\mathcal{C}^{\nu}_{i-1}$ only when $p_{i}>0$. The eigenvalue bound (19. ‣ III-C1 Exponential CBF (ECBF) ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) couples the pole locations to the initial state: the poles cannot be placed arbitrarily fast without violating the requirement that $\nu_{i}(x_{0})\geq 0$. In practice, the ECBF can be designed via pole placement, choosing $p_{i}$ large enough for rapid convergence while satisfying (19.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 4", "weight": 1.0} -->

‣ III-C1 Exponential CBF (ECBF) ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")). The constraint (18. ‣ III-C1 Exponential CBF (ECBF) ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) is then enforced pointwise via a quadratic program (QP) at each time step.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Evaluating (18. ‣ III-C1 Exponential CBF (ECBF) ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) requires computing time derivatives of $h_{0}$ up to order $r$, which in turn depend on time derivatives of the state up to order $r$. For the SMCS (1. ‣ III-A Differential geometry and geometric mechanical systems ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")), which is second order, $r=2$, and the two conditions reduce to: 1) $p_{1},p_{2}>0$ with $\kappa_{1}=p_{1}p_{2}$ and $\kappa_{2}=p_{1}+p_{2}$, and 2) $p_{1}\geq-\dot{h}_{0}(x_{0})/h_{0}(x_{0})$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-C2 Backstepping CBF (BCBF)", "weight": 1.0} -->

An alternative to the ECBF that avoids computing higher-order derivatives, which amplify measurement noise and incur additional autograd cost, is backstepping CBF (BCBF). In BCBF, the safety specification on $N$ is lifted to a CBF on $TN$ by introducing an auxiliary safe velocity field on $N$. Below we recite the key geometric generalization results. For simplicity, we assume the system is fully actuated ($\pi_{\mathcal{A}}=\mathrm{Id}$) and refer the reader to for the general (including underactuated) case and proof details. In practice, most manipulators are fully- or over-actuated.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Step 1: Construct a safe velocity field", "weight": 1.0} -->

Given a nominal velocity field $\xi$ on $N$ (so $\xi(x)\in T_{x}N$), one applies a smooth safety filter to obtain a *safe velocity field* $\tilde{\xi}:N\to TN$, $x\mapsto\tilde{\xi}(x)\in T_{x}N$, that renders $\mathcal{C}_{0}$ forward invariant under first-order dynamics $\dot{x}=\tilde{\xi}(x)$. Following, one uses the *half-Sontag formula*: The half-Sontag formula is a smooth, closed-form safety filter: it adds a correction along $\operatorname{grad}h_{0}$ that is just large enough to enforce the CBF condition $d(h_{0})_{x}\xi_{\mathrm{HS}}\geq-\alpha(h_{0}(x))$, and vanishes when $\xi$ already satisfies it.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Step 1: Construct a safe velocity field", "weight": 1.0} -->

The nominal velocity field $\xi$ can be chosen freely based on the application; a natural choice within the PBDS framework is $\xi(x)=-\operatorname{grad}\Phi|_{x}$, which drives the system toward the minimum of the task potential.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Step 1: Construct a safe velocity field", "weight": 1.0} -->

To provide a strict margin for the backstepping step, one further augments $\xi_{\mathrm{HS}}$ with an additional gradient term: for some $\delta>0$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Step 2: Lift to a CBF on $TN$", "weight": 1.0} -->

Using the safe velocity field $\mu_{x}$ from Step 1, one defines a candidate CBF on the tangent bundle: where $\varepsilon>0$ is a design parameter controlling the tradeoff between the safety margin and the allowable velocity deviation from $\mu_{x}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Pullback CBF for Task Manifold Safety", "weight": 1.0} -->

While metric-based tasks for safety were proposed, they present several limitations: *Exit behavior:* due to the symmetry of the metric-based velocity field, the constraint task must be deactivated when attempting to leave the safe set.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Pullback CBF for Task Manifold Safety", "weight": 1.0} -->

*Undefined behavior upon violation:* the metric $g=\exp(1/(2x^{2}))$ used in is undefined on the constraint boundary $x=0$, so no recovery mechanism exists once the constraint is violated.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Pullback CBF for Task Manifold Safety", "weight": 1.0} -->

*No guaranteed constraint satisfaction:* the constraint is ultimately enforced as one task among many in the multi-task PBDS QP (10. ‣ III-B Pullback bundle dynamical system (PBDS) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")), and the desired acceleration produced by the constraint task may not be fully realized.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Pullback CBF for Task Manifold Safety", "weight": 1.0} -->

We address these limitations by incorporating pullback control barrier functions, which produce sufficient conditions for a configuration-controlled robot to enforce task manifold safety. For brevity, we drop the task manifold index in this section. Consider a safety set $\mathcal{S}\subseteq N$ and a safety function $h_{0}:N\rightarrow\mathbb{R}$ that defines the safety of the system.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Assumption 1 (Surjective submersive task map)", "weight": 1.0} -->

The task map $f:M\rightarrow N$ is a surjective submersion, so the system is fully actuated on $N$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Remark 6", "weight": 1.0} -->

The safe set in the configuration manifold is the preimage $f^{-1}(\mathcal{C}_{0})=\{p\in M\mid(h_{0}\circ f)(p)\geq 0\}$, which may not be connected. Since trajectories are continuous, forward invariance of $f^{-1}(\mathcal{C}_{0})$ implies forward invariance of each connected component individually.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Remark 6", "weight": 1.0} -->

Since the PBDS framework builds on the SMCS (1. ‣ III-A Differential geometry and geometric mechanical systems ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")), the system is second order. We present adaptations of both the ECBF from and the BCBF from enforce task manifold safety constraints on configuration manifold acceleration.

<!-- chunk {"id": "body-0064", "role": "body", "section": "IV-A Geometric Kinematics", "weight": 1.0} -->

While the safety constraint is defined in the task manifold $N$, the control input in PBDS is the configuration manifold coordinate acceleration $\ddot{\sigma}$. Thus, we begin by deriving the geometric kinematics relating the configuration and task manifold accelerations.

<!-- chunk {"id": "body-0065", "role": "body", "section": "IV-A1 Velocity Relationship", "weight": 1.0} -->

Let $x(t)$ be a curve on $N$, $\sigma(t)$ be a curve on $M$ where $f(\sigma(t))=x(t)$. In local coordinates, differentiating $x^{\alpha}=f^{\alpha}(\sigma)$ with respect to time yields where $Jf$ is the Jacobian of the task map. In coordinate-free notation, this is $\dot{x}=df\,\dot{\sigma}$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "IV-A2 Acceleration Relationship", "weight": 1.0} -->

Differentiating the velocity relation gives the coordinate acceleration on $N$: The covariant accelerations on $N$ and $M$ are given in coordinates by Rearranging for $\ddot{\sigma}^{k}$ and substituting into yields Substituting into and using $\dot{x}^{\mu}=\frac{\partial f^{\mu}}{\partial\sigma^{i}}\dot{\sigma}^{i}$ yields where $(\nabla df)(\dot{\sigma},\dot{\sigma})$ denotes the second fundamental form of the map $f$ as.

<!-- chunk {"id": "body-0067", "role": "body", "section": "IV-B Task manifold ECBF", "weight": 1.0} -->

As is a relative degree 2 system, we examine the first and second derivatives of the constraint function $h_{0}$ along the system trajectories.

<!-- chunk {"id": "body-0068", "role": "body", "section": "IV-B Task manifold ECBF", "weight": 1.0} -->

The first derivative of $h_{0}(x(t))$ is computed by the chain rule: For the second derivative, we differentiate and substitute $\dot{x}^{\alpha}=\frac{\partial f^{\alpha}}{\partial\sigma^{i}}\dot{\sigma}^{i}$: Substituting the coordinate acceleration expansion into and applying the chain rule identities Applying the ECBF constraint from Definition III.4.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Remark 7 (Metric independence)", "weight": 1.0} -->

The constraint (41. ‣ IV-B Task manifold ECBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) involves only coordinate partial derivatives of $h_{0}\circ f$ and the coordinate acceleration $\ddot{\sigma}^{i}$. Intuitively, $h_{0}\circ f$ has no knowledge of $N$, so no geometric quantities of $N$ appear. Since SafePBDS controls $\ddot{\sigma}$, the ECBF constraint contains no geometric quantities altogether.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Remark 8 (Covariant form for non-flat $M$)", "weight": 1.0} -->

For any choice of Riemannian metric $g_{M}$ on $M$, substituting $\ddot{\sigma}^{k}=({}^{M}\!\nabla_{\dot{\sigma}}\dot{\sigma})^{k}-{}^{M}\!\Gamma^{k}_{ij}\dot{\sigma}^{i}\dot{\sigma}^{j}$ from into (41. ‣ IV-B Task manifold ECBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) and using the Riemannian Hessian identity yields the equivalent geometric form

<!-- chunk {"id": "body-0071", "role": "body", "section": "Remark 9 (Behavior outside $\\mathcal{C}_{0}$)", "weight": 1.0} -->

As long as $h_{0}$ is smooth and well defined outside $\mathcal{C}_{0}$, the ECBF constraint guarantees the system will converge asymptotically to $\{x\mid h_{0}(x)\geq 0\}$ from any initial condition, with convergence rate governed by the eigenvalues $-p_{1},-p_{2}$ via. This contrasts with the metric-based constraint enforcement, where the metric $g=\exp(1/(2x^{2}))$ is undefined on the constraint boundary $h_{0}(x)=0$. In practice, one may offset $h_{0}$ so that $h_{0}(x)\geq-\epsilon$ represents safety; the ECBF then drives the system to $\{x\mid h_{0}(x)\geq-\epsilon\}$ in finite time.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Example 1 (continued)", "weight": 1.0} -->

*Workspace obstacle clearance* for robot link $i$ is encoded on the task manifold $N_{\mathrm{obs},i}=\mathbb{R}$ with task map $f_{\mathrm{obs},i}\colon M\to N_{\mathrm{obs},i}\colon\sigma\mapsto d(\mathrm{geom}_{i},\mathrm{obs})$, the signed distance between the link $i$ collision geometry and the obstacle. The safety function $h_{0,\mathrm{obs},i}\colon N_{\mathrm{obs},i}\to\mathbb{R}$ is given by $h_{0,\mathrm{obs},i}(x)=x-d_{\min}$, where $d_{\min}\geq 0$ is a minimum clearance margin.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Example 1 (continued)", "weight": 1.0} -->

*Joint limits* for joint $j$ are encoded on the task manifold $N_{\mathrm{lim},j}=\mathbb{R}$ with task map $f_{\mathrm{lim},j}\colon M\to N_{\mathrm{lim},j}\colon\sigma\mapsto\sigma^{j}$. The safety functions $h_{0,j}^{-},h_{0,j}^{+}\colon N_{\mathrm{lim},j}\to\mathbb{R}$ are $h_{0,j}^{-}(x)=x-\sigma^{j}_{-}$ and $h_{0,j}^{+}(x)=\sigma^{j}_{+}-x$, for $j=1,\ldots,7$. Both families have relative degree 2 with respect to the task state. Each safety function yields a linear constraint on $\ddot{\sigma}$ via Theorem IV.1.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Example 1 (continued)", "weight": 1.0} -->

‣ IV-B Task manifold ECBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation").

<!-- chunk {"id": "body-0075", "role": "body", "section": "IV-C Task manifold BCBF", "weight": 1.0} -->

Here we derive the BCBF safety constraint for the PBDS system. Note that by Assumption 1. ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation"), the task map $f$ is a surjective submersion, so the system is fully actuated on $N$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Remark 10", "weight": 1.0} -->

Assumption 1. ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation") ensures the system can be controlled in any direction on the tangent space of the task manifold, so the supremum over accelerations is unbounded if $e_{x}\neq 0$. This significantly simplifies the CBF design process.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Remark 11", "weight": 1.0} -->

Unlike the ECBF formulation, the BCBF depends on the choice of Riemannian metric on $N$: the safe velocity field $\tilde{\xi}$, the velocity error norm $\|e_{x}\|_{N}$, the covariant derivative $\nabla_{\dot{x}}\tilde{\xi}$, and the inner product in all involve the metric. Intuitively, this is because the backstepping construction compares the current velocity $\dot{x}$ against the safe velocity field $\tilde{\xi}$ using the metric on $N$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Remark 12 (Strict vs. non-strict inequalities)", "weight": 1.0} -->

The ECBF constraint (41. ‣ IV-B Task manifold ECBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) uses a non-strict inequality ($\geq$), following, with the regularity condition (that $0$ is a regular value of $h_{0}$) assumed in Definition III.3. ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation"). The BCBF constraint (46. ‣ IV-C Task manifold BCBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) uses a strict inequality ($>$), following. The strict inequality is a stronger condition: it implies regularity \[11, Remark 1\], but not vice versa, since it additionally requires the existence of a control input that makes $h$ strictly increase on $\{h=0\}$.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Remark 12 (Strict vs. non-strict inequalities)", "weight": 1.0} -->

In the backstepping construction, this strict margin arises naturally from the $\delta\,\operatorname{grad}h_{0}$ augmentation in (23 ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")). Note that the actual enforcement constraint used in Proposition 1. ‣ IV-C Task manifold BCBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation") is the non-strict $\dot{h}\geq-\alpha(h)$; the strict inequality in Theorem IV.3. ‣ IV-C Task manifold BCBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation") establishes that valid controls exist.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Remark 13 (Recovery outside $\\mathcal{C}_{0}$)", "weight": 1.0} -->

For the BCBF, if $h_{0}$ is smooth on all of $N$, the half-Sontag formula (20 ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) produces a globally smooth safe velocity field $\tilde{\xi}$, so the candidate $h$ (25 ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) is well-defined on all of $TN$. The non-strict enforcement constraint $\dot{h}\geq-\alpha(h)$ is then satisfiable everywhere: when $e_{x}\neq 0$, full actuation makes the supremum unbounded; when $e_{x}=0$, the half-Sontag formula guarantees $d(h_{0})_{x}\,\tilde{\xi}\geq-\alpha(h_{0}(x))$ globally.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Remark 13 (Recovery outside $\\mathcal{C}_{0}$)", "weight": 1.0} -->

If $h<0$, a comparison argument using $\alpha\in\mathcal{K}_{\infty}^{e}$ shows $h(t)\to 0$, recovering safety. The domain $\Omega_{0}$ from Lemma III.2. ‣ Step 1: Construct a safe velocity field. ‣ III-C2 Backstepping CBF (BCBF) ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation") is only required for the strict inequality in Theorem IV.3. ‣ IV-C Task manifold BCBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation"), which establishes $h$ as a CBF in the formal sense, but does not limit the practical recovery behavior.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Remark 14 (Practical considerations)", "weight": 1.0} -->

In practice, finite differencing is often used to compute derivatives and smooth functions that are Lipschitz continuous but not everywhere differentiable. Additionally, due to numerical errors and latency, it is possible to get small CBF violations despite satisfying CBF constraints. Such issues may be mitigated by padding the safety function in (13. ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) by a small margin $\epsilon_{\mathrm{pad}}>0$, which we apply in our implementation.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Task manifold actions", "weight": 1.0} -->

In the autonomous SafePBDS framework (Definition IV.1. ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")), runtime decision-making is limited to adjusting the weighting pseudometrics $w_{i}$. However, one may wish to steer the system directly in a task manifold $N$, for example to incorporate commands from a higher-level planner or a learned policy. We therefore propose a mechanism that exposes control inputs while preserving the safety and compositional structure of the PBDS framework. We seek the following desiderata: The action space may be lower dimensional than the configuration dimension $m$.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Task manifold actions", "weight": 1.0} -->

If so desired, all $m$ dimensions may be controlled.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Task manifold actions", "weight": 1.0} -->

The action represents a residual force on top of the autonomous PBDS dynamics: when the action is zero, the system follows the autonomous behavior.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Task manifold actions", "weight": 1.0} -->

To this end, consider $L$ *control task maps* $f_{l}:M\rightarrow N_{l}$, $l=1,\ldots,L$, each equipped with a weighting pseudometric $w_{l}$ on $TN_{l}$ and a Riemannian behavior metric $g_{l}$ on $N_{l}$. These may coincide with some of the $K$ autonomous task maps, or they may be entirely separate. For each control task, the user supplies a force-like input $u_{l}\in T^{*}\!N_{l}$, which is converted to an acceleration-level quantity via the sharp (musical isomorphism) $u_{l}^{\sharp}=g_{l}^{\sharp}(u_{l})\in TN_{l}$ (in coordinates, $g_{l}^{-1}\,u_{l}$).

<!-- chunk {"id": "body-0087", "role": "body", "section": "Remark 15", "weight": 1.0} -->

If one interprets $\bar{a}$ as the resulting acceleration of a task manifold SMCS (Equation (1. ‣ III-A Differential geometry and geometric mechanical systems ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation"))), the second sum in (48. ‣ V Task manifold actions ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) acts as an additional task manifold force.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Remark 16", "weight": 1.0} -->

$\bar{a}$ is not necessarily a unique minimizer. In practice, since $\bar{a}$ is used to warm start the numerical solver, it is typically selected when all $u_{l}=0$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Remark 17 (Desiderata)", "weight": 1.0} -->

The three desiderata from the beginning of this section are satisfied by construction: each control task map $f_{l}:M\rightarrow N_{l}$ may have $n_{l}\leq m$, so the total action dimension $\sum_{l=1}^{L}n_{l}$ can be less than $m$; if the control task maps collectively form a submersion (i.e., $\operatorname{rank}\bigl[\,Jf_{1}^{\top}\cdots Jf_{L}^{\top}\bigr]=m$), all $m$ degrees of freedom are controllable; and Theorem V.1. ‣ V Task manifold actions ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation") guarantees that zero control input recovers the autonomous behavior.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Example 1 (continued)", "weight": 1.0} -->

To expose a one-dimensional action space that selects among qualitatively distinct avoidance behaviors (e.g. routing the elbow on either side of a workspace obstacle), we use a control task map given by the coordinate projection onto joint 1, with identity behavior metric $g=1$ and a positive scalar weighting pseudometric $w$. The action input $u\in\mathbb{R}$ injects an acceleration on joint 1; flipping the sign of $u$ steers the arm into a different homotopy class of safe paths around the obstacle, while $u=0$ recovers the autonomous behavior by Theorem V.1. ‣ V Task manifold actions ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation"). This is demonstrated in Section VII-B.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Evaluation: Simulated $\\mathbb{S}^{2}$ Double Integrator", "weight": 1.0} -->

Using a point robot on $\mathbb{S}^{2}$, we first validate the theoretical properties of SafePBDS, in particular chart invariance, safety guarantees, multi-task composition, and effects of our action space design. All experiment configurations in this section are summarized in Table II. Additional details are available in Appendix XI.

<!-- chunk {"id": "body-0092", "role": "body", "section": "System definition", "weight": 1.0} -->

Consider a point robot with unit mass traveling on the surface of a unit sphere. The configuration manifold of the robot is $\mathbb{S}^{2}$, which has a natural embedding $\bar{\varphi}:\mathbb{S}^{2}\hookrightarrow\mathbb{R}^{3}$. We consider the atlas $\left\{(U_{N},\varphi_{N}),(U_{S},\varphi_{S})\right\}$ formed by the north and south pole stereographic projection charts.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Configuration Dynamics", "weight": 1.0} -->

Since PBDS does not account for the configuration manifold geometry (Remark 3 ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")), we treat the chart coordinates as $\mathbb{R}^{2}$ and integrate with a fourth-order Runge--Kutta scheme when simulating the system forward.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Task Dynamics", "weight": 1.0} -->

Following, we use the chart-to-embedding task map $f=\bar{\varphi}_{\alpha}\colon\mathbb{R}^{2}\to\mathbb{R}^{3}$, with an attractor potential and dissipative force defined on the embedding $\mathbb{R}^{3}$.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Safety constraint", "weight": 1.0} -->

We choose the safety task as staying at least arclength $r$ from a point $x_{o}\in\mathbb{S}^{2}$. The safety function (Definition III.3. ‣ III-C Control barrier functions (CBFs) ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) is $h_{0}(y)=\arccos\!\bigl(\bar{\varphi}_{\alpha}(y)\cdot x_{o}\bigr)-r,$ with $\alpha\in\{N,S\}$ the active chart. The safe set is $\mathcal{C}_{0}=\{y\in\mathbb{R}^{2}:h_{0}(y)\geq 0\}$.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Safety constraint", "weight": 1.0} -->

For BCBF, we set $\xi=0$ and compare two metrics: the round metric $g_{ij}=\frac{4}{(1+\|y\|^{2})^{2}}\delta_{ij}$, which is the pullback of the embedded $\mathbb{S}^{2}$ metric through the stereographic chart, and the flat metric $\delta_{ij}$, which treats the chart coordinates as Euclidean.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Safety constraint", "weight": 1.0} -->

Safety (chart, metric) Autonomous: metric dependence and chart switching BCBF (Switch, round) Autonomous: safety recovery TABLE II: Run configurations for the 𝕊2 double integrator experiments.

<!-- chunk {"id": "body-0098", "role": "body", "section": "VI-B Autonomous SafePBDS on $\\mathbb{S}^{2}$", "weight": 1.0} -->

First, we validate the theoretical properties of ECBFs and BCBFs in SafePBDS without task manifold actions, shown in Figure 2(a--b).

<!-- chunk {"id": "body-0099", "role": "body", "section": "Metric dependence and chart switching", "weight": 1.0} -->

As expected from Remark 7. ‣ IV-B Task manifold ECBF ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation"), ECBF is metric-independent. The two BCBF runs produce visibly different avoidance trajectories, since BCBF depends on the metric via $\operatorname{grad}h_{0}$, $\|e_{x}\|_{N}$, and $\nabla_{\dot{x}}\tilde{\xi}$; the BCBF also stays farther from the unsafe set boundary due to the additional "safe velocity tracking error" penalty (second term in ). We verify chart switching by varying the configuration manifold chart between north and south. This is the safety-augmented analogue of the chart switching experiment in \[6, Fig. 5\]. Run (iv) matches the fixed-chart reference (i) on $\mathbb{S}^{2}$, confirming that the SafePBDS produce consistent behavior across chart choices and can be deployed on atlases with multiple charts.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Safety recovery", "weight": 1.0} -->

To test recovery, we run both an ECBF and a BCBF trajectory starting from inside the unsafe set. Both formulations drive the system out of the unsafe region and converge to the goal. The ECBF constrains only $h_{0}\geq 0$ and recovers along the most direct path. The BCBF's safe velocity field deviation penalty causes its recovery to maintain a larger clearance from the obstacle boundary.

<!-- chunk {"id": "body-0101", "role": "body", "section": "VI-C Steered SafePBDS on $\\mathbb{S}^{2}$", "weight": 1.0} -->

Next, we demonstrate the properties of the task manifold actions (Section V). We use an ECBF safety constraint and an identity control task map $f_{l}=\mathrm{id}\colon\mathbb{R}^{2}\to\mathbb{R}^{2}$ on the active chart. We place the obstacle so the system faces two valid avoidance paths on each side of the obstacle. We run five trajectories (viii)-(xii), all shown in Figure 2(c): *Autonomous* ($u=0$): the system breaks symmetry via a small positional offset and converges to one side.

<!-- chunk {"id": "body-0102", "role": "body", "section": "VI-C Steered SafePBDS on $\\mathbb{S}^{2}$", "weight": 1.0} -->

*$+u_{\perp}$*: a tangential action perpendicular to the start--goal geodesic with $\|u_{\perp}\|=1$, steering the robot to the same side as the autonomous bias.

<!-- chunk {"id": "body-0103", "role": "body", "section": "VI-C Steered SafePBDS on $\\mathbb{S}^{2}$", "weight": 1.0} -->

*$-u_{\perp}$*: flipping the sign steers the robot to the opposite side, resolving the topological ambiguity that the autonomous dynamics alone cannot.

<!-- chunk {"id": "body-0104", "role": "body", "section": "VI-C Steered SafePBDS on $\\mathbb{S}^{2}$", "weight": 1.0} -->

*$u_{\mathrm{unsafe}}$*: a large action ($\|u\|=10$) continuously pointing toward the obstacle center. SafePBDS prevents the constraint violation, and safety is maintained ($h_{0}(t)\geq 0$) despite the adversarial action.

<!-- chunk {"id": "body-0105", "role": "body", "section": "VI-C Steered SafePBDS on $\\mathbb{S}^{2}$", "weight": 1.0} -->

*$-u_{\perp}$ on the south pole chart*: we repeat (x) on the south pole chart to verify chart invariance under action inputs.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Evaluation: Simulated 7-DOF Robot Arm", "weight": 1.0} -->

We instantiate the running 7-DOF arm scenario (Example 1. ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) in MuJoCo to validate the pullback CBF for workspace obstacle avoidance and the action space formulation for behavior modality selection. The arm starts at its home configuration; goals and obstacles vary per experiment as detailed below. Additional details are provided in Appendix XII.

<!-- chunk {"id": "body-0107", "role": "body", "section": "VII-A Autonomous SafePBDS on the 7-DOF Arm", "weight": 1.0} -->

We validate the pullback ECBF by comparing the full SafePBDS system against an ablation that removes the obstacle avoidance ECBFs while keeping joint limit ECBFs active.

<!-- chunk {"id": "body-0108", "role": "body", "section": "6-DOF pose ($\\mathrm{SE}$) tracking", "weight": 1.0} -->

A spherical obstacle (radius $0.10$ m) is placed in between the start and goal positions. Figure 3(a) shows the full system (purple) deflecting around the obstacle, while the ablation (red, dashed) passes through it. Both converge to the goal pose.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Random orientation ($\\mathrm{SO}$) tracking", "weight": 1.0} -->

We sample 50 scenarios that each track a goal orientation (a $30^{\circ}$-$150^{\circ}$ rotation about a random axis) with a randomly placed spherical obstacle (radius $8$ cm). Position tracking is forfeited due to the difficulty of randomly finding a reachable goal pose under the obstacle avoidance constraint. Scenarios with obstacle clearance below $5$ cm are rejected and resampled. The full system is safe in all 50 runs (min $h_{\mathrm{obs}}=+0.010$), whereas the ablation violates the obstacle constraint in 11 of 50 runs (min $h_{\mathrm{obs}}=-0.080$); all runs reach the goal orientation.

<!-- chunk {"id": "body-0110", "role": "body", "section": "VII-B Steered SafePBDS on the 7-DOF Arm", "weight": 1.0} -->

We validate the action interface (Section V) using end effector position ($\mathbb{R}^{3}$) tracking, which leaves four redundant degrees of freedom for the action input to exploit. When an obstacle lies in the robot's workspace, the deterministic autonomous system defaults to one avoidance path, yet multiple safe paths exist. The action inputs allow an operator or high-level planner to select among these configurations with minimal input, instantiating the homotopy class selection application described in the running example (Example 1. ‣ III Preliminaries ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")). We apply a brief constant scalar action on the first joint: $u=\pm 15$ for the first 3.5 s, then $u=0$. Flipping the sign of this scalar results in trajectories of distinct homotopy classes: the $+u$ arm (blue) passes on one side while the $-u$ arm (purple) passes on the other (Figure 3(b)). Both trajectories converge to the goal while preserving safety.

<!-- chunk {"id": "body-0111", "role": "body", "section": "VII-B Steered SafePBDS on the 7-DOF Arm", "weight": 1.0} -->

This highlights a key practical advantage of the steered SafePBDS: qualitatively different behaviors can be selected using simple, transient inputs, while the autonomous dynamics and safety constraints handle the details of the motion.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Evaluation: Hardware Experiments", "weight": 1.0} -->

We validate SafePBDS on hardware with two dexterous manipulation tasks: autonomous grasping of diverse household objects (Section VIII-C) and in-hand reorientation via finger gaiting (Section VIII-D ‣ VIII Evaluation: Hardware Experiments ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")).

<!-- chunk {"id": "body-0113", "role": "body", "section": "VIII-A Robot Setup", "weight": 1.0} -->

All hardware experiments are performed with a Franka Emika Panda 7-DOF arm and a Wonik Allegro 16-DOF dexterous hand, for a combined 23-DOF system. The arm is controlled at 20 Hz via the Deoxys framework, using the joint impedance controller when PBDS is active, and the joint position controller for the pre-grasp approach. The hand is commanded over ZMQ using a mix of joint-level PD and Cartesian fingertip impedance modes. Runtime perception uses an Intel RealSense D435 camera with Segment Anything for segmentation and FoundationPose for 6-DOF pose tracking at 10 Hz, which updates an object pose in a MuJoCo simulation that the PBDS controller runs against. Object meshes are obtained by scanning with KIRI Engine on a LiDAR-equipped iPhone. Full control, perception, and modeling details are given in Appendix XIII.

<!-- chunk {"id": "body-0114", "role": "body", "section": "VIII-B Manifold Setup and Task Specification", "weight": 1.0} -->

The configuration manifold $M=\prod_{i=1}^{m}(\sigma^{i}_{-},\,\sigma^{i}_{+})$ is an open subset of $\mathbb{R}^{m}$ equipped with the flat product metric. The combined arm-hand system used for dexterous grasping has $m=23$; for in-hand reorientation (Section VIII-D ‣ VIII Evaluation: Hardware Experiments ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation")) the arm is controlled separately and $m=16$.

<!-- chunk {"id": "body-0115", "role": "body", "section": "VIII-B Manifold Setup and Task Specification", "weight": 1.0} -->

The grasping and finger-gaiting behaviors share the same overall structure: a joint space PBDS damping task, a family of pullback ECBF safety tasks, and task manifold action tasks driven by a higher-level planner. The safety tasks comprise (i) joint limit ECBFs; (ii) force closure ECBFs based on the $l^{*}$ metric for one four-finger-grasp variant and four per-finger-excluded variants; (iii) fingertip lift-distance ECBFs that keep each non-grasping fingertip away from the object surface; (iv) pairwise finger-finger distance ECBFs that prevent fingertip collisions; (v) per-fingertip table avoidance ECBFs; and (vi) link-object distance ECBFs that keep non-fingertip links clear of the object (per-link CBFs for grasping; per-finger distal phalanx ECBFs for in-hand reorientation). The action tasks expose a per-finger controller on the 1D fingertip-to-object distance. For grasping, additional controllers on the 3D palm position and on the 3D average fingertip position.

<!-- chunk {"id": "body-0116", "role": "body", "section": "VIII-B Manifold Setup and Task Specification", "weight": 1.0} -->

For in-hand reorientation, an additional action task drives the gaited fingertip's 3D position toward a planner-supplied target in the frame of the contact plane spanned by the three in-contact fingertips. In total, $84$ ECBF tasks are instantiated for the grasping policy and $61$ for the in-hand reorientation policy, a subset of which is active at each control step.

<!-- chunk {"id": "body-0117", "role": "body", "section": "VIII-B Manifold Setup and Task Specification", "weight": 1.0} -->

A finite-state machine modulates task weights to coordinate the grasp and gaiting phases. It selects the active force closure variant as fingers enter or leave contact, and toggles the per-finger lift-distance CBFs depending on whether each finger is stationary or in transit. The full enumeration of task maps, safety functions, and ECBF gains is given in Appendix XIII.2.

<!-- chunk {"id": "body-0118", "role": "body", "section": "VIII-C Dexterous Grasping", "weight": 1.0} -->

We apply SafePBDS to autonomous grasping of diverse household objects.

<!-- chunk {"id": "body-0119", "role": "body", "section": "VIII-C1 Scene Setup and Test Protocol", "weight": 1.0} -->

We select 20 household objects (Fig. 4) with mass ranging from $64$ to $613$ g and longest bounding box dimension ranging from roughly $6$ to $29$ cm. At the start of each trial, FoundationPose reports the object's 6-DOF pose, and a wrist pose sampler proposes top-down wrist pose candidates that are filtered for reachability, clearance, and aperture fit. The top-ranked candidate is executed in two stages: first, a Deoxys-controlled approach to the wrist pose (via a $15$ cm waypoint above the pose followed by a direct descent); second, SafePBDS takes over the full $23$-DOF arm-hand system and runs the PBDS QP at each control step. During the SafePBDS phase, two action tasks are composed: per-finger 1D fingertip-to-object distance controllers that drive each fingertip onto the object surface, and a 3D average-fingertip centering controller that aligns the four-fingertip centroid with the object's geometric center, for a total of $4\times 1+3=7$ action dimensions.

<!-- chunk {"id": "body-0120", "role": "body", "section": "VIII-C1 Scene Setup and Test Protocol", "weight": 1.0} -->

The force closure ECBF (Section VIII-B) is activated as the fingertips approach the object, so that the final squeeze converges to a certified force-closed grasp. A trial is recorded as a *success* if the object is successfully lifted with all four fingers in contact, a *partial success* if it is stably lifted with one finger not in contact, and a *failure* otherwise. The candidate filtering pipeline, action gain schedule, and full execution protocol are given in Appendix XIV.

<!-- chunk {"id": "body-0121", "role": "body", "section": "VIII-C1 Scene Setup and Test Protocol", "weight": 1.0} -->

To showcase the flexibility of our framework, we additionally evaluate grasping with one of the four fingers excluded. The active force closure ECBF is switched to the per-finger-excluded variant, so that $l^{*}$ is computed over the three in-contact fingers, while the excluded finger is held clear of the object by retargeting its fingertip-to-object distance action to a fixed clearance and enabling its fingertip lift-distance ECBF. No other policy modification is required.

<!-- chunk {"id": "body-0122", "role": "body", "section": "VIII-C2 Results", "weight": 1.0} -->

SafePBDS achieves an overall success rate of $111/120$ ($92.5\%$) on the $20$ household objects, with $15$ of $20$ attaining full $6/6$ success. Figure 7 plots each (object, pose) trial group against object weight and the vertical bounding-box length at that pose. Partial successes and failures concentrate among objects with small vertical extents (roughly $\leq 10$ cm) and high weight. Low vertical extent is less forgiving of pose estimation errors and leaves less table clearance, while high weight requires grasp forces that approach the limits of the low-level impedance controller and the hand's hardware capabilities.

<!-- chunk {"id": "body-0123", "role": "body", "section": "VIII-C2 Results", "weight": 1.0} -->

The 3-finger ablation (Figure 6) succeeds in $34/36$ trials ($94.4\%$): thanks to the autonomous PBDS behavior, a high-level decision policy can reliably choose which finger to exclude despite the complexity of dexterous precision grasping.

<!-- chunk {"id": "body-0124", "role": "body", "section": "VIII-D Palm-Down In-Hand Reorientation (IHR)", "weight": 1.0} -->

We apply SafePBDS to palm-down IHR, where the goal is to rotate a grasped object about the palm normal axis with the palm normal facing down. This is significantly more challenging than the more common "IHR with palm facing up" in literature (e.g. ); with the palm facing down, the object must be securely grasped throughout the process. To tackle the combinatorial complexity of finger gaiting sequences, we leverage offline planning in simulation to discover feasible reorientation trajectories, which are then deployed on hardware.

<!-- chunk {"id": "body-0125", "role": "body", "section": "VIII-D1 Simulation Pre-Planning", "weight": 1.0} -->

The main challenge in IHR is choosing which finger to move and where to move it. We address this with a depth-first tree search over finger-object contact states, where each node has all four fingers in contact and each edge corresponds to relocating one finger. The search tree is rooted at an initial grasp obtained by reusing the top-down grasping pipeline of Section VIII-C on a $6$ cm diameter bottle. A priority queue at each depth orders nodes by the cumulative $z$-axis yaw rotation achieved along the path from the root, while a balance constraint caps the disparity in per-finger move counts so that no single finger is overused.

<!-- chunk {"id": "body-0126", "role": "body", "section": "VIII-D1 Simulation Pre-Planning", "weight": 1.0} -->

For each movable finger at a node, $12$ candidate extensions are generated by a predetermined grid of steps along the object surface. Fingers are not allowed to move consecutively and the max gaiting step count difference across fingers is 1. This leaves at most $3$ movable fingers and a maximum branching factor of $36$. To prevent the search from getting stuck with a never-movable finger, a cyclic sequence of "next movable" fingers is assigned so that at each tree depth, the "next movable" finger must be movable after the candidate extension. Each candidate is forward-simulated under SafePBDS and a four-phase (LIFTING, TRAVERSING, DROPPING, ADJUSTING) primitive, and an accepted candidate becomes a tree edge. Throughout the primitive, the three-finger grasp is maintained by the corresponding force closure ECBF and pairwise fingertip spacing ECBFs (the object itself may still move). In TRAVERSING and DROPPING, the force closure ECBF excluding the next movable finger is additionally activated.

<!-- chunk {"id": "body-0127", "role": "body", "section": "VIII-D1 Simulation Pre-Planning", "weight": 1.0} -->

A candidate is accepted when, on reaching ADJUSTING, the moving finger is aligned with its target contact, the hand is at rest, all four fingers are back in contact, the force closure ECBF excluding the next movable finger is non-negative, and the object tilt from the rotation axis is below $10^{\circ}$. Loss of contact at any in-contact finger during the rollout aborts execution and rejects the candidate. A simplified illustration is shown in Figure 1. More details are given in Appendix XV. Figure 8 ‣ VIII Evaluation: Hardware Experiments ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation") shows the resulting search trees.

<!-- chunk {"id": "body-0128", "role": "body", "section": "VIII-D1 Simulation Pre-Planning", "weight": 1.0} -->

(a) Clockwise rotation, static arm (b) Counterclockwise rotation, swinging arm with weighted object Figure 9: In-hand reorientation on hardware. Snapshots are arranged temporally from left to right.(a) Clockwise rotation with the arm held static and empty bottle. (b) Counterclockwise rotation with the arm swinging and 2.5 oz loose weight in the bottle, demonstrating robustness under load and motion.

<!-- chunk {"id": "body-0129", "role": "body", "section": "VIII-D2 Scene Setup and Test Protocol", "weight": 1.0} -->

A human operator places the object in between the finger cage, and the fingers grasp the object using the initial grasping configuration in the motion plan. The joint angles from the planned finger gaiting sequence are then played back open loop. To evaluate robustness of our plans, we test each plan under three conditions: (i) with the arm held static and no added payload, (ii) with the arm held static and up to 98 grams of weight incrementally added into the bottle, and (iii) with the arm swinging and 70 grams of loose weight inside the bottle.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Discussion", "weight": 1.5} -->

This paper presents SafePBDS (Safe Pullback Bundle Dynamical Systems), a geometric motion generation framework that extends PBDS with task manifold safety guarantees and an action interface. At each control step, two convex QPs are solved sequentially: the first defines the autonomous safe acceleration, and the second injects the action input around it. The resulting configuration space acceleration is certifiably safe and recovers the autonomous task dynamics when the action input vanishes. We validate its theoretical properties in simulation on an $\mathbb{S}^{2}$ double integrator and a 7-DOF Franka arm. On a 23-DOF Franka--Allegro hardware system, SafePBDS attains $92.5\%$ grasp success across 20 household objects, and $94.4\%$ for 3-finger grasps through simple action changes enabled by the action interface. Finally, SafePBDS enables the first model-based robust palm-down in-hand reorientation, producing over $360^{\circ}$ rotation in both directions under varying object weight and arm motion.

<!-- chunk {"id": "body-0131", "role": "body", "section": "IX-A Limitations", "weight": 1.0} -->

Like other vector-field policies, SafePBDS solves a local motion generation problem: over long horizons, the system may become trapped in local minima, and escaping them must be handled by the higher-level policy that provides the action input. In addition, SafePBDS is kinematic and therefore requires a lower-level tracker to realize the commanded accelerations, or an impedance controller when compliant contact forces are needed. Finally, the pullback derivations assume surjective submersion task maps and a fully or over-actuated robot; underactuated systems are therefore outside the scope of the present framework.

<!-- chunk {"id": "body-0132", "role": "body", "section": "IX-B Future work", "weight": 1.0} -->

On the application side, an important direction is to combine the action interface enabled by SafePBDS with more advanced decision-making policies, such as reinforcement learning or vision-language-action models. On the theoretical side, relaxing the Assumption 1. ‣ IV Pullback CBF for Task Manifold Safety ‣ Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation") will allow SafePBDS to handle a broader class of objectives, including tasks with singularities or nonsmooth task maps. In addition, incorporating robot dynamics and the contact forces required for manipulation, rather than relying on an acceleration tracker or impedance controller, will allow SafePBDS to reason directly about interaction forces alongside geometric safety.
