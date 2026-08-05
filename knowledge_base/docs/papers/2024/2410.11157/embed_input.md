<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Safety on the Fly: Constructing Robust Safety Filters via Policy Control Barrier Functions at Runtime

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Control Barrier Functions (CBFs) have proven to be an effective tool for performing safe control synthesis for nonlinear systems. However, guaranteeing safety in the presence of disturbances and input constraints for high relative degree systems is a difficult problem. In this work, we propose the Robust Policy CBF (RPCBF), a practical approach for constructing robust CBF approximations online via the estimation of a value function. We establish conditions under which the approximation qualifies as a valid CBF and demonstrate the effectiveness of the RPCBF-safety filter in simulation on a variety of high relative degree input-constrained systems. Finally, we demonstrate the benefits of our method in compensating for model errors on a hardware quadcopter platform by treating the model errors as disturbances. Website including code: www.oswinso.xyz/rpcbf/

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction and Related Works", "weight": 1.5} -->

In the realm of autonomous systems, providing safety guarantees is crucial, especially in critical applications such as autonomous driving and healthcare robotics. Control Barrier Functions (CBFs) have proven to be an effective tool to maintain and certify the safety of dynamical systems. In particular, they can be applied as a Safety Filter (SF) that minimally modifies arbitrary control inputs to ensure safety, making them especially valuable when integrated with learning-based controllers.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction and Related Works", "weight": 1.5} -->

Despite their theoretical advantages, significant challenges remain in the practical application and construction of CBFs. First, constructing CBFs is non-trivial, specifically for high relative degree systems with input constraints. Second, the safety guarantees of CBF-based controllers depend on having an accurate system model, which is rarely the case for systems in real life. This makes the safety guarantees of such controllers sensitive to model uncertainties.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction and Related Works", "weight": 1.5} -->

Learning Control Barrier Functions. To minimize reliance on extensive domain knowledge, a recent trend is to learn neural CBFs that approximate CBFs using Neural Networks (NNs). Neural CBFs have been successfully applied to high-dimensional systems, including multi-agent control scenarios, and have been extended to handle parametric uncertainties and obstacles with unknown dynamics. Although using NNs as CBFs offers universal approximation capabilities, it requires certifying them as valid CBFs to ensure safety guarantees and limits their interpretability. Furthermore, using a naive approach to learning neural CBFs by minimizing a loss that encourages the CBF conditions can lead to a small or even empty forward-invariant set. Thus, presents a method to construct CBFs using policy evaluation of *any* policy. They show that the policy value function is a CBF and learn an NN approximation. In this setting, the policy value function represents the maximum-over-time constraint violation, indicating how suitable a state is for a system following a specific policy. However, their approach does not consider uncertainties in the system dynamics.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction and Related Works", "weight": 1.5} -->

Robust Safety. Controllers that are robust to disturbances are essential for ensuring the safety of autonomous systems in the real world. This has been studied before in robust CBFs, which guarantee safety under bounded disturbances. However, constructing robust CBFs is inherently more difficult than constructing standard CBFs, especially under input constraints. Hamilton-Jacobi reachability analysis can be used to compute robust control-invariant sets, which can then be subsequently used for constructing robust CBFs. However, reachability analysis in itself is challenging, with grid-based partial Differential Equation (DE) solvers being limited to state dimensions below five, while deep learning-based solvers require subsequent NN verification to check for solution accuracy. Moreover, both learning-based CBF approaches and deep learning-based reachability solvers depend on predefined system dynamics and disturbance assumptions, which are difficult to adapt, limiting their flexibility once deployed, as retraining cannot be performed on the system. Thus, train a value network with the avoidance set and disturbance bounds as inputs, however this increases training data requirements and complicates evaluating how well the learned network represents the true value function.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction and Related Works", "weight": 1.5} -->

As an alternative to robust safety, other works focus on risk-aware safety, which aims to ensure safety with high probability by modeling disturbances probabilistically and incorporating risk measures. Unlike robust methods, which ensure constraint satisfaction for all disturbances within a bounded set but may be overly conservative, risk-aware approaches typically rely on knowledge of the disturbance's probability distribution. In this work, we focus on robust safety.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction and Related Works", "weight": 1.5} -->

We propose a practical approach for constructing a CBF approximation at runtime, which can be derived for any system dynamics and disturbance bounds without requiring (re)training. We establish conditions under which the resulting CBF approximation qualifies as a valid CBF. Our method constructs CBFs by evaluating the value function of *any* policy, which has been shown to be a valid CBF. By leveraging finite-horizon policy rollouts, we enable a more detailed analysis of safety guarantees than NN approximations. We apply this approach to construct approximations of robust CBFs.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction and Related Works", "weight": 1.5} -->

Contributions. We summarize our contributions as follows.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction and Related Works", "weight": 1.5} -->

We propose a method of constructing (robust) CBFs using the (robust) policy value function and a real-time approximation that can be used at runtime.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction and Related Works", "weight": 1.5} -->

We demonstrate real-time performance and the benefits of our robust CBFs on a hardware quadcopter, where robustness to model errors is key for collision prevention.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Problem Statement", "weight": 1.0} -->

We consider a disturbed continuous-time, control-affine dynamical system of the form with state $\mathbf{x}_{t}\in\mathcal{X}\subseteq\mathbb{R}^{n}$, control input $\mathbf{u}_{t}\in\mathcal{U}\subseteq\mathbb{R}^{m}$ and unknown, bounded, smooth disturbance $\mathbf{d}_{\mathrm{min}}\leq\mathbf{d}_{t}\leq\mathbf{d}_{\mathrm{max}}$ with $\mathbf{d}_{\mathrm{min}},\mathbf{d}_{\mathrm{max}}\in\mathbb{R}^{d}$ (e.g., estimated from empirical data), where $\mathbf{d}_{t}$ can be time-varying. The functions $f$ and $g$ are assumed to be locally Lipschitz continuous.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Problem Statement", "weight": 1.0} -->

Let $\mathcal{A}\subset\mathcal{X}$ denote the set of states to be avoided.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem 1 (Safety Filter Synthesis)", "weight": 1.0} -->

We focus on solving 1. ‣ II-A Problem Statement ‣ II Preliminaries ‣ Safety on the Fly: Constructing Robust Safety Filters via Policy Control Barrier Functions at Runtime") using (zeroing) CBFs.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Safety Filters using Control Barrier Functions", "weight": 1.0} -->

We begin by providing a standard definition of a CBF in the non-robust case, which we extend to the robust case for Policy Control Barrier Functions (PCBFs) in the next section. Define the undisturbed system to be a particular case of the disturbed system without disturbances ($\mathbf{d}=0$), by Let $B:\mathcal{X}\rightarrow\mathbb{R}$ be a continuously differentiable function, with $\mathcal{C}=\{\mathbf{x}\in\mathcal{X}\,|\,B(\mathbf{x})\leq 0\}$ as its $0$-sublevel set.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Safety Filters using Control Barrier Functions", "weight": 1.0} -->

Let $\alpha:\mathbb{R}\rightarrow\mathbb{R}$ be an extended class-$\kappa_{\infty}$ function^11^1Extended class-$\kappa_{\infty}$ is the set of continuous, strictly increasing functions $\alpha:(-\infty,\infty)\rightarrow(-\infty,\infty)$ with $\alpha=0$.. Then, $B$ is a CBF for the undisturbed system on $\mathcal{X}$ if with $L_{f}B\coloneq\nabla B^{\mathsf{T}}f$ and $L_{g}B\coloneq\nabla B^{\mathsf{T}}g$. It then follows that any control input $\mathbf{u}\in K_{\mathrm{cbf}}$ with renders $\mathcal{C}$ forward-invariant.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Safety Filters using Control Barrier Functions", "weight": 1.0} -->

In other words, there exists an $\mathbf{u}\in\mathcal{U}$ such that any trajectory starting within $\mathcal{C}$ remains in $\mathcal{C}$. Asymptotic stability of $\mathcal{C}$ can be achieved by extending (4b) to hold for all $\mathbf{x}\in\mathcal{X}$. Since the right hand side of (4b) is linear in $\mathbf{u}$, given a CBF $B$, we can solve 1. ‣ II-A Problem Statement ‣ II Preliminaries ‣ Safety on the Fly: Constructing Robust Safety Filters via Policy Control Barrier Functions at Runtime") for using the following Quadratic Program (QP)-based controller: While CBFs can be applied to guarantee safety for a known undisturbed system, three major challenges remain: How do we synthesize a valid CBF that satisfies (4b) for high relative degree systems with input constraints?

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Safety Filters using Control Barrier Functions", "weight": 1.0} -->

How do we synthesize a robust CBF that ensures safe control for the disturbed system?

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Safety Filters using Control Barrier Functions", "weight": 1.0} -->

How can we efficiently derive a CBF at runtime for different system dynamics and disturbance assumptions?

<!-- chunk {"id": "body-0020", "role": "body", "section": "(Robust) Policy Control Barrier Functions", "weight": 1.0} -->

To address the above challenges, we leverage the insight from that CBFs can be constructed by deriving the policy value function through the evaluation of *any* policy. Rather than approximating the policy value function with an NN as, we propose a real-time approximation that avoids NNs and can be derived at runtime through a finite-horizon numerical approximation. We further extend this approach to the robust case and introduce Robust Policy Control Barrier Functions (RPCBFs) and subsequently propose a sampling-based approximation that can be derived at runtime. Next, we revisit the formulation of PCBFs and describe our extensions and approximations.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Constructing CBFs via Policy Evaluation", "weight": 1.0} -->

Based, we first derive the PCBF formulation for the undisturbed system. Assume that the avoid set $\mathcal{A}$ can be described as the super-level set of a function $h:\mathcal{X}\rightarrow\mathbb{R}$ (e.g., the negative distance to the constraint): Note that $h(\mathbf{x})>0$ for states that are already in the failure set, whereas $B(\mathbf{x})>0$ for states from which failure is inevitable in the future under the given dynamics and input constraints. In the absence of input constraints, $h$ and $B$ may coincide. We denote by $\mathbf{x}_{t}^{\pi}$ the resulting state at time $t$ when starting from the initial state $\mathbf{x}_{0}$ and following policy $\pi:\mathcal{X}\rightarrow\mathcal{U}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Constructing CBFs via Policy Evaluation", "weight": 1.0} -->

Furthermore, we define the *maximum-over-time* value function for the undisturbed system in as As stated in \[35, Theorem 1\], the *policy value function* $V^{h,\pi}_{\infty}$ is a CBF for the undisturbed system in for any $\pi$, since $V^{h,\pi}_{\infty}$ satisfies the following two inequalities $\forall\mathbf{x}\in\mathcal{X}$ which imply (4a) and (4b). For details, we refer to. The key intuition here is that $V^{h,\pi}_{\infty}$ provides an upper bound on the worst future constraint violation $h$ under the optimal policy since the optimal policy will do no worse than $\pi$. Thus, CBFs can be constructed via policy evaluation of any policy. We refer to $\pi$ as the design policy, noting that the nominal policy $\pi_{\mathrm{nom}}$ differs from the design policy.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Finite Horizon Approximation of PCBFs", "weight": 1.0} -->

A key challenge with the policy value function $V^{h,\pi}_{\infty}$ is that its definition requires an infinite-horizon. While tackles this problem by using an NN to learn $V^{h,\pi}_{\infty}$ with a loss derived using dynamic programming, we take a different approach and perform a finite-horizon approximation that can be computed without the use of an NN, enabling a more in-depth analysis of the resulting safety guarantees. Expanding $V^{h,\pi}_{\infty}$: where the approximation is made by dropping the $V_{\infty}^{h,\pi}(\mathbf{x}_{T})$ "tail". The question is then whether the finite-horizon approximation $V_{T}^{h,\pi}$ is a CBF and can provide safety guarantees.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Finite Horizon Approximation of PCBFs", "weight": 1.0} -->

We can at least answer this in the affirmative when the approximation in (10 Policy Control Barrier Functions ‣ Safety on the Fly: Constructing Robust Safety Filters via Policy Control Barrier Functions at Runtime")) is an equality, i.e., the maximum occurs in $[0,T{\color[rgb]{0,0,0})}$. We state this formally in the following theorem.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark (Connections to Backup Controller / CBFs)", "weight": 1.0} -->

Since the zero sublevel set of $V^{h,\pi}_{\infty}$ is a CI set under $\pi$, (9 Policy Control Barrier Functions ‣ Safety on the Fly: Constructing Robust Safety Filters via Policy Control Barrier Functions at Runtime")) can also be seen as Backup CBF with backup controller $\pi$ and no known CI terminal set. Unlike this (and other similar approaches ), our approach replaces the need for a known CI set with the requirement of a sufficiently long horizon $T$. Thus, the design policy $\pi$ can be chosen arbitrarily and is not required to steer the system into a CI set. Furthermore, we demonstrate that the naive approximation of $h$ over a time-discretized state trajectory introduces gradient errors. To address this, we present an improved time-discretization using cubic splines in section III-C Policy Control Barrier Functions ‣ Safety on the Fly: Constructing Robust Safety Filters via Policy Control Barrier Functions at Runtime").

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark (Connections to Model Predictive Control (MPC))", "weight": 1.0} -->

The finite-horizon approximation here is closely related to the use of MPC by practitioners. More precisely, although a terminal constraint set is often required to theoretically guarantee recursive feasibility of finite-horizon MPC, practitioners often apply MPC without the use of such a terminal constraint set to wide success \[19, 4"), 44, 36\]. Our decision to drop the $V^{h,\pi}_{\infty}(\mathbf{x}_{T}^{\pi})$ term can be viewed as being similar to dropping the terminal constraint set. Another similarity is the choice of horizon $T$. Namely, recursive feasibility holds in MPC given a sufficiently large horizon, similar to Corollary 1 Policy Control Barrier Functions ‣ Safety on the Fly: Constructing Robust Safety Filters via Policy Control Barrier Functions at Runtime"). However, the MPC horizon length is limited, as it requires solving a potentially nonlinear and non-convex optimization problem online, with computational complexity typically scaling cubically with $T$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark (Connections to Model Predictive Control (MPC))", "weight": 1.0} -->

A key advantage of PCBF-SFs is that they only solve the simpler (CBF-QP), whose computation time is unaffected by $T$, see Section IV-D.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark (Connections to Predictive Safety Filter (PSF) )", "weight": 1.0} -->

The finite-horizon approximation is closely related to the PSF, which implicitly represents the safe set via a finite-horizon MPC problem with terminal constraints or long horizons for recursive feasibility. Unlike PCBF-SFs, the PSF requires solving a potentially nonlinear and nonconvex optimization problem online with complexity scaling cubically in $T$. PCBF-SFs only require solving the simpler (CBF-QP). However, while the PSF may find a locally optimal solution, the conservativeness of the PCBF-SF depends on $\pi$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-C Time Discretization of Policy Control Barrier Functions", "weight": 1.0} -->

Another challenge lies in how to compute the maximum in (10 Policy Control Barrier Functions ‣ Safety on the Fly: Constructing Robust Safety Filters via Policy Control Barrier Functions at Runtime")). The states $\mathbf{x}_{t}^{\pi}$ can be solved numerically using an ordinary DE solver, resulting in a time-discretized state trajectory. It is tempting to then consider taking the maximum $h$ over this trajectory, i.e., for time discretization $\Delta t$, However, the gap between (10 Policy Control Barrier Functions ‣ Safety on the Fly: Constructing Robust Safety Filters via Policy Control Barrier Functions at Runtime")) and (13 Policy Control Barrier Functions ‣ Safety on the Fly: Constructing Robust Safety Filters via Policy Control Barrier Functions at Runtime")) is particularly disastrous when computing the gradient. We illustrate this in the following example for the Double Integrator (DI).

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-C Time Discretization of Policy Control Barrier Functions", "weight": 1.0} -->

Example: Gradient Error on the Double Integrator. Consider a DI with positive velocity $v_{0}>0$ decelerating with $\pi(\mathbf{x})=a=-1$. The dynamics are defined by $\dot{p}=v$, $\dot{v}=a$ with initial state $\mathbf{x}_{0}=[p_{0},v_{0}]$ and constraints $h(\mathbf{x})=p\leq 0$. For the continuous-time case, the gradient can be derived as After (exact) time discretization with timestep $\Delta t$, the time-discretized states can be computed as We now show that the gradient of $V^{h,\pi}_{\infty}$ depends on $\Delta t$ and denote by $\nabla V^{h,\pi}_{\infty,\Delta t}$ the resulting gradient. Let $\tau$ be the integer time step $k$ at which the maximum position is reached.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-C Time Discretization of Policy Control Barrier Functions", "weight": 1.0} -->

The maximum position is then given by with $\frac{\partial p_{\mathrm{max}}}{\partial v_{0}}=\tau\Delta t$, which is a function of $\tau$. Although $\tau$ also depends on $v_{0}$, it is piecewise constant and has zero derivative since it only takes integer values. Comparing the gradients of $V^{h,\pi}_{\infty}$ with $V^{h,\pi}_{\infty,\Delta t}$ in fig. 2 Policy Control Barrier Functions ‣ Safety on the Fly: Constructing Robust Safety Filters via Policy Control Barrier Functions at Runtime"), we see a large error between the two with discontinuities in the discrete-time gradient in $\Delta t$. This is particularly problematic when the gradient is used in a gradient-based optimization algorithm such as (CBF-QP).

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-C Time Discretization of Policy Control Barrier Functions", "weight": 1.0} -->

Improved Time-Discretization using Cubic Splines. To reduce the error in the time-discretized value function approximation (13 Policy Control Barrier Functions ‣ Safety on the Fly: Constructing Robust Safety Filters via Policy Control Barrier Functions at Runtime")), we propose to approximate $h(\mathbf{x}_{t}^{\pi})$ by fitting a cubic spline to the points $\{h(\mathbf{x}_{k\Delta t}^{\pi})\}_{k=0}^{H-1}$. The $\max$ over the cubic spline can then be computed in closed-form by solving the roots of a quadratic to yield a better approximation of $\sup_{0\leq t<T}h(\mathbf{x}_{t}^{\pi})$ than the naive maximization (13 Policy Control Barrier Functions ‣ Safety on the Fly: Constructing Robust Safety Filters via Policy Control Barrier Functions at Runtime")).

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-C Time Discretization of Policy Control Barrier Functions", "weight": 1.0} -->

Intuitively, this resolves the gradient error due to integer-valued $\tau$ from the previous example because the maximum of the cubic spline can now happen between timesteps. We can also formally quantify the error in both the cubic spline value and its gradient. Let $\tilde{h}:0,\infty)\to\mathbb{R}$ denote the cubic spline approximation of $h$ as a function of time, and let $\tilde{V}^{h,\pi}_{\infty,\Delta t}(\mathbf{x}_{0})\coloneqq\sup_{t\geq 0}\tilde{h}(t)$. Using \[[15, Chapter 5\], we obtain the error bounds In the previous example of the DI, since $h$ is exactly quadratic, applying cubic splines results in zero gradient error (fig. 2 Policy Control Barrier Functions ‣ Safety on the Fly: Constructing Robust Safety Filters via Policy Control Barrier Functions at Runtime")).

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-C Time Discretization of Policy Control Barrier Functions", "weight": 1.0} -->

If $\mathop{}\!\mathrm{d}^{4}/\mathop{}\!\mathrm{d}t^{4}\;h(\mathbf{x}_{t})$ can be bounded, the bounds (17 Policy Control Barrier Functions ‣ Safety on the Fly: Constructing Robust Safety Filters via Policy Control Barrier Functions at Runtime")) can then be used to suitably modify (CBF-QP) to guarantee safety. A larger $\Delta t$ will therefore result in a more conservative SF.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-D Robust Extension of PCBFs", "weight": 1.0} -->

We extend PCBF to handle disturbances by defining the robust value function equivalent of (6 Policy Control Barrier Functions ‣ Safety on the Fly: Constructing Robust Safety Filters via Policy Control Barrier Functions at Runtime")) as it can be shown with similar proof that $V^{h,\pi}_{\infty}$ is a robust CBF, i.e., it satisfies (4a) and, for $B(\mathbf{x})\leq 0$, 1:Input: Initial State x0, Policy π, Constraint function h, Horizon T = HΔt, Number of disturbance samples N 3: Sample disturbance trajectory {dki}k = 1H − 1 4: Rollout the policy π on disturbed system 5: Compute sup0 ≤ t < Th(xti) using cubic splines 8:Compute the gradient ∇VT, Nh, π(x0) using automatic differentiation Algorithm 1 Robust Policy CBF (RPCBF) Solving for robust controls that satisfy (19 Policy Control Barrier Functions ‣ Safety on the Fly: Constructing Robust Safety Filters via Policy Control Barrier Functions at Runtime")) renders the zero sublevel set robust forward-invariant.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-D Robust Extension of PCBFs", "weight": 1.0} -->

However, deriving the worst-case disturbance is generally intractable because it requires evaluating all possible disturbance trajectories. Instead, we propose to only consider $N$ disturbance trajectories and take the worst-case out of the $N$ samples, resulting in the following RPCBF approximation: We summarize our approach in algorithm 1 Policy Control Barrier Functions ‣ Safety on the Fly: Constructing Robust Safety Filters via Policy Control Barrier Functions at Runtime") and fig. 3 Policy Control Barrier Functions ‣ Safety on the Fly: Constructing Robust Safety Filters via Policy Control Barrier Functions at Runtime"). Note that algorithm 1 Policy Control Barrier Functions ‣ Safety on the Fly: Constructing Robust Safety Filters via Policy Control Barrier Functions at Runtime") must be executed once per control loop to obtain the value $V^{h,\pi}_{T,N}$ and gradient $\nabla V^{h,\pi}_{T,N}$ for the current state for use in (CBF-QP). Different approaches can be implemented to perform informed sampling of disturbances.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-D Robust Extension of PCBFs", "weight": 1.0} -->

For bounded disturbances, the worst-case scenario often occurs at the vertices of the disturbance set (e.g., for disturbance-affine dynamics). Consequently, we choose to sample from a mixture of the uniform distribution $\mathcal{U}(\mathbf{d}_{\mathrm{min}},\mathbf{d}_{\mathrm{max}})$ and the uniform distribution over the vertices. Using better optimizers to approximate the worst-case samples will be left to future work.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-D Robust Extension of PCBFs", "weight": 1.0} -->

While the finite-sample approximation does not guarantee robustness to any disturbance, it does ensure robustness to the specific sampled disturbances within the finite horizon. As the number of informed samples approaches infinity, the approximation increasingly captures the true worst-case scenarios. Theoretical guarantees for this sampling-based approach could be established using random set theory, as demonstrated. Furthermore, statistical risk measures could be used instead of the worst-case out of $N$ samples. For instance, using who bound the risk measure evaluation of a random variable whose distribution is unknown. However, we leave this for future work. For the simulation and hardware experiments below, we use PCBF and RPCBF to refer to their time-discretized finite-horizon and finite-sample approximations as described in this section.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Simulation Experiments", "weight": 1.0} -->

We evaluate the performance of (R)PCBF in simulation for high relative degree systems with box control constraints.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Simulation Experiments", "weight": 1.0} -->

Baselines. We compare against the following SFs, which similarly do not incorporate NNs in their approach.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Simulation Experiments", "weight": 1.0} -->

Handcrafted Candidate CBF (HOCBF): We construct a *candidate* CBF via a Higher-Order CBF on $h$ without considering input constraints.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Simulation Experiments", "weight": 1.0} -->

Approximate Nominal MPC-based PSF (MPC): A trajectory optimization problem is solved, imposing the safety constraints while penalizing deviations from the nominal policy. We consider the undisturbed system without assuming access to a known robust forward-invariant set, thus not imposing a terminal constraint.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Simulation Experiments", "weight": 1.0} -->

Systems. We consider four systems: a DI, a Segway, an F-16 fighter jet (ground collision avoidance problem), and AutoRally, a 1/5 autonomous vehicle. On the DI, we consider position bounds ($|p|\leq 1$), while the Segway asks for an upright handlebar and considers position bounds ($|\theta|\leq 0.3\pi$, $|p|\leq 2)$, $\Delta t=0.1$. For the F-16, safety is defined as box constraints on states like altitude. Since this system is not control-affine in the throttle, we leave the throttle as the output of a P controller, resulting in a $16$-dimensional state space and a $3$-dimensional control space. In AutoRally, a crash occurs when the car stops after hitting the track boundary, while a collision involves contact without stopping. For each system, we define $J$ continuously differentiable constraint functions $h_{j}$ tailored to the problem at hand.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Simulation Experiments", "weight": 1.0} -->

For example, for the DI system we set $h_{0}=p-1$ and $h_{1}=-(p+1)$. From these we derive $J$ corresponding CBFs, which yield to $J$ constraints in (CBF-QP). For the DI and the Segway, we assume unknown but bounded time-varying disturbances on the mass, for the F-16 unknown but bounded matched disturbances ($d=1$), and for the AutoRally additive truncated Gaussian noise. Keep in mind that our approach does not require designing/learning a new CBF for different systems, disturbance assumptions, or input constraints, but simply requires swapping the dynamics, specifying the disturbance and constraints. During testing, we consider a constant zero-control nominal policy for the DI, maximum acceleration for the Segway, a PID controller for the F-16, and Model Predictive Path Integral (MPPI) control for AutoRally.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-A Influence of Horizon Length on Undisturbed Segway", "weight": 1.0} -->

While the infinite-horizon policy value function is a CBF, we use a finite-horizon approximation, making the SF performance horizon-dependent. To illustrate this, we assess the impact of different horizon lengths on the PCBF-SF, see fig. 4. We plot the state space from where $\pi_{\mathrm{nom}}$ can influence the output of the SF (*Filter Boundary*) and from where the SF preserves safety (*Safe Region*). For CBF-based filters, the filter boundary is defined by the CBF's zero level set. The safe region is determined for a $\pi_{\mathrm{nom}}$ by solving (CBF-QP) and rolling out the system over a horizon $\bar{T}=30s$. For a short PCBF horizon, i.e., $T=5s$, the true CI set is overapproximated. Consequently, the SF fails to preserve safety, as illustrated by the resulting unsafe example trajectory. In contrast, a longer horizon of $T=10s$ provides a much closer approximation of the true CI set.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-A Influence of Horizon Length on Undisturbed Segway", "weight": 1.0} -->

This is evident when comparing it to an even longer horizon, such as $T=30s$, which does not result in a visibly smaller safe region, indicating that $T=10s$ is already sufficient.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-B Behavior on Disturbed Double Integrator and Segway", "weight": 1.0} -->

We explore the robustness of different SFs, examining the filter boundary and safe region, derived for one sampled disturbance trajectory per state, as shown in fig. 5. We visualize rolled-out trajectories for $\bar{N}$ sampled disturbance trajectories (uniformly sampled and on the vertices) from selected initial states within the filter boundary. On the DI, only the RPCBF-SF achieves safety for all $\bar{N}$ sampled disturbance trajectories. Since the RPCBF accounts for the worst-case among the $N$ sampled disturbances, the filter boundary is more conservative. On the Segway, MPC violates the safety constraints in all cases and hence has an empty filter boundary and safe region. Only the RPCBF-SF achieves safe trajectories for all considered samples. Next, we evaluate the (R)PCBF-SFs at uniformly distributed initial states, see fig. 6. The RPCBF-SF achieves safety for all evaluated states within its zero-level set and the sampled disturbances, while the PCBF overapproximates the safe set.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-C Simulations on AutoRally", "weight": 1.0} -->

Finally, to assess the safety improvements brought about by the proposed (R)PCBF, we integrate the HOCBF and the proposed methods with Shield-MPPI (SMPPI), and test them on AutoRally. Figure 7 shows that SMPPI using RPCBF generates the safest trajectories. The statistics of the safety performance of the controllers are shown in table I.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-C Simulations on AutoRally", "weight": 1.0} -->

Mean Collisions per Lap TABLE I: Collision & Crash Rate on AutoRally. MPPI causes the most collisions and crashes. SMPPI-HOCBF and SMPPI-PCBF improve safety, while SMPPI-RPCBF minimizes collisions & crashes.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Hardware Experiments", "weight": 1.0} -->

We conduct hardware experiments on the Crazyflie platform to test the robustness of the proposed RPCBF-SF to real-world disturbances (see fig. 1).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Hardware Experiments", "weight": 1.0} -->

Using the onboard position PID controller, we model the system as a DI, assuming that position setpoints are converted to accelerations onboard and treat the model error as an acceleration disturbance. We randomly generate nominal trajectories and treat the corresponding positions as the nominal control. A circular obstacle is placed at the densest part of the trajectory to encourage collisions. We use $T=5s$ (50 steps at $\Delta t=\qty{0.1}{}$) and $N=64$. The RPCBF-SF runs at a frequency of \\qty100 on a laptop.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Hardware Experiments", "weight": 1.0} -->

We run the (R)PCBF-SFs with $\alpha=5$ for $6$ nominal trajectories; fig. 9 shows results for $3$ of them. The RPCBF-SF remains safe throughout, while the PCBF-SF always collides.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Hardware Experiments", "weight": 1.0} -->

We next vary the choice of the class-$\kappa$ function $\alpha$ and plot the results in fig. 10. While the non-robust PCBF-SF does not collide with the obstacle when $\alpha$ is sufficiently small, this requires fine-tuning and is difficult to know beforehand. On the other hand, the RPCBF-SF is safe for all values of $\alpha$ we tested, allowing $\alpha$ to be used as a parameter that controls the behavior without also simultaneously affecting safety.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

In this work, we proposed the Robust Policy Control Barrier Function (RPCBF), a method for constructing robust CBFs using the robust policy value function derived from rolling out a design policy. Subsequently, we introduced a real-time approximation that can be derived online, with conditions for its validity as a CBF. Simulation experiments demonstrate that a safety filter constructed using the RPCBF yields improved safety and more accurate estimation of the robust control-invariant set compared to existing methods. Hardware experiments on a quadcopter highlight the importance of accounting for model errors to ensure safety.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

Future work will focus on analyzing the safety guarantees of the RPCBFs approximation, considering the finite-horizon, time-discretization, and sampling-based approach. Additionally, while the RPCBF acts as a CBF for any design policy if a long enough horizon is considered, conservativeness depends on the design policy. Deriving a policy to reduce conservativeness while maintaining infinite horizon guarantees is an important research direction. Moreover, extending our method to time-varying constraints and integrating real-time onboard perception are important directions for future work.
