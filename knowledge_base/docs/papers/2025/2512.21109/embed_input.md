<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robust and Efficient MuJoCo-based Model Predictive Control via Web of Affine Spaces Derivatives

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

MuJoCo is a powerful and efficient physics simulator widely used in robotics. One common way it is applied in practice is through Model Predictive Control (MPC), which uses repeated rollouts of the simulator to optimize future actions and generate responsive control policies in real time. To make this process more accessible, the open source library MuJoCo MPC (MJPC) provides ready-to-use MPC algorithms and implementations built directly on top of the MuJoCo simulator. However, MJPC relies on finite differencing (FD) to compute derivatives through the underlying MuJoCo simulator, which is often a key bottleneck that can make it prohibitively costly for time-sensitive tasks, especially in high-DOF systems or complex scenes. In this paper, we introduce the use of Web of Affine Spaces (WASP) derivatives within MJPC as a drop-in replacement for FD. WASP is a recently developed approach for efficiently computing sequences of accurate derivative approximations. By reusing information from prior, related derivative calculations, WASP accelerates and stabilizes the computation of new derivatives, making it especially well suited for MPC's iterative, fine-grained updates over time.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We evaluate WASP across a diverse suite of MJPC tasks spanning multiple robot embodiments. Our results suggest that WASP derivatives are particularly effective in MJPC: it integrates seamlessly across tasks, delivers consistently robust performance, and achieves up to a 2mathsfx speedup compared to an FD backend when used with derivative-based planners, such as iLQG. In addition, WASP-based MPC outperforms MJPC's stochastic sampling-based planners on our evaluation tasks, offering both greater efficiency and reliability. To support adoption and future research, we release an open-source implementation of MJPC with WASP derivatives fully integrated.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

MuJoCo is a powerful and efficient physics simulator widely used in robotics. One way it is applied in practice is through Model Predictive Control (MPC), which uses repeated rollouts of the simulator to optimize future actions and generate responsive control policies in real time. MPC can be implemented on top of a simulator like MuJoCo by differentiating through the simulator, allowing the outer optimization loop to follow derivative information and continuously "surf" the function landscape downhill toward a local minimum over time. To make this process more accessible, the open source library MuJoCo MPC (MJPC) provides ready-to-use MPC algorithms and implementations built directly on top of the MuJoCo simulator.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In theory, it is possible to leverage automatic differentiation (AD) tools to conveniently compute exact derivatives of the underlying simulator. For instance, MuJoCo offers XLA and Warp backends to use state-of-the-art AD implementations. However, in the context of MPC, these exact derivatives often prove too narrow in scope, as they capture only highly local sensitivities of the nonlinear dynamics. Because MPC repeatedly differentiates through short-horizon rollouts of these complex dynamics, the resulting derivatives can become excessively sharp or ill-conditioned, which frequently leads to numerical instability.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In turn, MJPC relies solely on finite differencing (FD) to compute derivatives through the underlying MuJoCo simulator. FD estimates derivatives by perturbing each input dimension and measuring the resulting change in the simulator's output. At a high level, FD seems well suited for MPC: it is straightforward to apply, requiring only standard forward passes without modifications to the simulator's source code, and its small approximation error in the derivatives can contribute to greater numerical stability by smoothing out sharp or ill-conditioned derivatives that arise from exact differentiation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite these advantages, FD becomes inefficient for high-DOF systems or complex scenes. Each input dimension must be perturbed independently, so the number of simulator calls grows linearly with the dimensionality of the state and action spaces. For robots with many joints or environments featuring rich contact dynamics, this approach can require hundreds or even thousands of additional rollouts for a single derivative evaluation. Although parallelization can mitigate part of this cost, the unfavorable scaling remains a fundamental limitation. As a result, the computational burden often dominates the control loop, making it challenging for MJPC to sustain the fast update rates required for real-time robotics.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we introduce the use of Web of Affine Spaces (WASP) derivatives within MJPC as a drop-in replacement for FD. WASP is a recently developed method for efficiently computing sequences of approximate derivatives by reusing information from prior, related evaluations, enabling faster computation and improved numerical stability. Our premise is that these properties make WASP a good fit for MPC, where derivatives are recomputed repeatedly along closely related trajectories. However, prior evaluations of WASP have been limited to kinematics-based functions, and its effectiveness in dynamics-based MPC settings remains untested. A key contribution of this work is to evaluate the extent to which WASP's advantages carry over to MPC problems involving full physics simulation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate WASP across a diverse suite of MJPC tasks spanning multiple robot embodiments (some shown in Figure 1). Our results suggest that WASP derivatives are particularly effective in MJPC: it integrates seamlessly across tasks, delivers consistently robust performance, and achieves up to a 2$\mathsf{x}$ speedup compared to an FD backend when used with derivative-based planners, such as iLQG. In addition, WASP-based MPC outperforms MJPC's stochastic sampling-based planners on our evaluation tasks, offering both greater efficiency and reliability.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To support adoption and further research, we provide an open-source implementation of MJPC that incorporates WASP derivatives. This release makes it easy for practitioners to experiment with WASP as a drop-in replacement for FD, enabling immediate evaluation of its efficiency, stability, and accuracy tradeoffs in real-world control tasks.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Model Predictive Control Primer", "weight": 1.0} -->

Model Predictive Control (MPC) is a control strategy that repeatedly simulates forward dynamics to predict future states, then optimizes a short horizon of actions to minimize a cost function before executing the first action and replanning. Specifically, MPC typically reasons over the following components: A fixed time-step, $\Delta t$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Model Predictive Control Primer", "weight": 1.0} -->

An ordered index set, $\mathcal{I}\equiv\{0,1,2,\dots,T\}$, where each index corresponds to a physical time point in the discrete horizon $\{0,\Delta t,2\Delta t,\dots,T\Delta t\}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Model Predictive Control Primer", "weight": 1.0} -->

An ordered set of controls, $U\equiv\{\mathbf{u}_{i}\mid i\in\mathcal{I}\setminus\{T\}\}$. The exclusion of $T$ reflects that no control is applied at the terminal state.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Model Predictive Control Primer", "weight": 1.0} -->

A system dynamics function, $f$, that maps a state and action pair at one index to the state at the next index, i.e., $f(\mathbf{x}_{i},\mathbf{u}_{i})=\mathbf{x}_{i+1}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Model Predictive Control Primer", "weight": 1.0} -->

The goal of MPC is to compute controls $U$ that, through the system dynamics $f$, produce corresponding states $X$ minimize (or at least reduce) the cost $J$. This optimization is repeated in real time: the first control $\mathbf{u}_{0}$ from the current solution is applied to the robot, and the search for the next solution begins immediately thereafter.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Strategies for Solving MPC", "weight": 1.0} -->

At a high level, methods for solving the MPC problem specified in §II-A are grouped into two categories: derivative-based methods and stochastic sampling-based methods. Derivative-based methods typically involve the following steps: Rollout candidate states $X$ using candidate controls $U$ and the system dynamics function $f$. Typically, $U$ is taken from the most recent solution as a warm start.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Strategies for Solving MPC", "weight": 1.0} -->

Compute $\frac{\partial\ell}{\partial\mathbf{x}_{i}}\in\mathbb{R}^{1\times d_{x}}$ and $\frac{\partial\ell}{\partial\mathbf{u}_{i}}\in\mathbb{R}^{1\times d_{u}}$. These are called cost derivatives. For some algorithms, second-order cost derivatives are also computed at this step.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Strategies for Solving MPC", "weight": 1.0} -->

Take some step over all controls, e.g., $\mathbf{u}_{i}\leftarrow\mathbf{u}_{i}+\alpha\frac{\partial J}{\partial\mathbf{u}_{i}}^{\top}$. The actual step here is algorithm-dependent and can use various different optimization strategies (e.g., line search or trust region method).

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Strategies for Solving MPC", "weight": 1.0} -->

Optionally, re-rollout candidate states $X$ based on the just updated controls $U$ using the system dynamics function $f$ and repeat Steps 2--6 until some termination condition is reached.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Strategies for Solving MPC", "weight": 1.0} -->

Return answer, $U^{*}$ and send the first command, $\mathbf{u}_{0}^{*}$ to the robot.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Strategies for Solving MPC", "weight": 1.0} -->

In contrast, stochastic sampling-based methods, optimize by evaluating and refining a distribution over candidate control sequences rather than relying on derivatives. These methods typically involve the following steps: Initialize a distribution over candidate control sequences $U$, often centered around the most recent solution for warm starting.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B Strategies for Solving MPC", "weight": 1.0} -->

Sample a batch of candidate control sequences $\{U^{(k)}\}_{k=1}^{K}$ from the distribution.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B Strategies for Solving MPC", "weight": 1.0} -->

For each sampled sequence $U^{(k)}$, rollout the corresponding states $X^{(k)}$ using the system dynamics function $f$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B Strategies for Solving MPC", "weight": 1.0} -->

Evaluate the cost $J(X^{(k)},U^{(k)})$ for each trajectory.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B Strategies for Solving MPC", "weight": 1.0} -->

Update the sampling distribution parameters based on the best-performing trajectories.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-B Strategies for Solving MPC", "weight": 1.0} -->

Repeat Steps 2--5 until some termination condition is met (e.g., maximum iterations or convergence of the distribution).

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-B Strategies for Solving MPC", "weight": 1.0} -->

Return the best control sequence $U^{*}$ found and send the first command, $\mathbf{u}_{0}^{*}$, to the robot.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-B Strategies for Solving MPC", "weight": 1.0} -->

Both derivative-based and stochastic sampling-based strategies have proven effective, but they commonly excel in different regimes. For instance, derivative-based methods achieve fast convergence when accurate model derivatives are available and the function landscape is reasonably smooth, while stochastic approaches may offer more robustness in highly nonlinear or discontinuous settings where derivatives are unreliable.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-B Strategies for Solving MPC", "weight": 1.0} -->

In this paper, our focus is on improving derivative-based methods for MPC, though we also compare against stochastic-based methods in our evaluation.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-C MuJuCo MPC Algorithms", "weight": 1.0} -->

In MJPC, the system dynamics function $f$ is provided by the MuJoCo physics engine itself. MJPC includes implementations of both derivative-based and stochastic sampling-based methods, offering a spectrum of planners with different trade-offs in speed, robustness, and sample efficiency.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-C MuJuCo MPC Algorithms", "weight": 1.0} -->

Specifically, The derivative-based planners include gradient descent; and iterative Linear Quadratic Gaussian (iLQG). The stochastic sampling-based planners include predictive sampling; robust sampling; cross-entropy; and sample gradient methods. Our evaluation in this paper (§V) systematically assesses all of these planners provided in MJPC.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-D MuJoCo MPC Differentiation", "weight": 1.0} -->

Our work is primarily addressing the potential bottleneck in Step 2 of the derivative-based strategy steps in §II-B. While Step 3 also involves computing derivatives, these cost derivatives are typically computed analytically and, thus, do not require further investigation.

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-D MuJoCo MPC Differentiation", "weight": 1.0} -->

MuJoCo currently computes model derivatives using finite differencing (FD). This process generally takes the following form: where $\frac{\partial f}{\partial\mathbf{x}_{i}}[:,j]$ and $\frac{\partial f}{\partial\mathbf{u}_{i}}[:,k]$ refer to the $j$-th and $k$-th columns in these matrices, respectively, $\mathbf{e}_{j}$ and $\mathbf{e}_{k}$ denote one-hot vectors where only the $j$-th and $k$-th elements are one and all others are zero, and $\epsilon$ is a small scalar value (e.g., $1e^{-5}$).

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-D MuJoCo MPC Differentiation", "weight": 1.0} -->

Note that the FD processes in Equations 1 and 2 must be run for all $d_{x}$ columns in $\frac{\partial f}{\partial\mathbf{x}_{i}}$, all $d_{u}$ columns in $\frac{\partial f}{\partial\mathbf{u}_{i}}$, and all $T+1$ time points. Thus, a single update to $U$ requires $d_{x}*(T+1)+d_{u}*T+1$ calls to the system dynamics function $f$ which, itself, can be fairly expensive.

<!-- chunk {"id": "body-0035", "role": "body", "section": "II-D MuJoCo MPC Differentiation", "weight": 1.0} -->

While parallelization may help in practice, it typically applies to only one loop dimension. In MJPC, for example, computations are distributed across CPU threads along the time index $i$. Even so, the workload may remain prohibitive when the state or control dimension ($n$ or $m$) is large or when evaluating the dynamics $f$ is particularly costly.

<!-- chunk {"id": "body-0036", "role": "body", "section": "II-E Other Derivative Computation Strategies", "weight": 1.0} -->

Automatic Differentiation (AD) is a natural alternative to FD, supported by mature software implementations. AD can be applied in either forward mode or reverse mode, and both have gained popularity in robotics. Several differentiable simulators, such as gradSim, PlasticineLab, and lcp-physics, employ reverse-mode AD to compute model derivatives. More recently, ad-trait introduced the first operator-overloading AD library in Rust, supporting both modes and integrating with a Rust-based robotics library. MuJoCo offers XLA and Warp backends to use state-of-the-art AD implementations, though these have not been integrated into MJPC.

<!-- chunk {"id": "body-0037", "role": "body", "section": "II-E Other Derivative Computation Strategies", "weight": 1.0} -->

Despite these advances, Suh et al. highlight that characteristics of contact dynamics, such as stiffness and discontinuities, can compromise the utility of AD, producing non-informative derivatives and numerical instability. Exact derivatives often prove too narrow in scope, as they capture only highly local sensitivities of the nonlinear dynamics. Because MPC repeatedly differentiates through short-horizon rollouts of these complex dynamics, the resulting derivatives can become excessively sharp or ill-conditioned, which frequently leads to numerical instability.

<!-- chunk {"id": "body-0038", "role": "body", "section": "II-E Other Derivative Computation Strategies", "weight": 1.0} -->

Building on MuJoCo's FD implementation, Zhang et al. proposed a heuristic to accelerate computation by skipping derivative evaluations at selected time points and interpolating them from nearby evaluations along the planning horizon. This strategy is complementary to our approach: their method reduces costs from long horizons, while ours targets the scaling issues introduced by high DoF systems. In practice, the two techniques could be combined, and we plan to explore these connections in future work.

<!-- chunk {"id": "body-0039", "role": "body", "section": "II-F Problem Statement", "weight": 1.0} -->

The primary bottleneck in derivative-based MPC arises in Step 2 of the solution process outlined in §II-B, where model derivatives must be repeatedly computed through the system dynamics function. Our goal is to accelerate these derivative computations in MJPC, thereby reducing the overall time required for each MPC iteration. Our goal is to continue to treat the MuJoCo physics engine as a black-box model, without requiring any modifications to its source code. Crucially, any such acceleration must preserve robustness: the resulting control sequences should continue to yield stable, low-cost trajectories, ensuring that long-horizon task performance, as measured by returns from $J$, remains uncompromised.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Web of Affine Spaces Derivatives", "weight": 1.0} -->

Our strategy for accelerating model derivatives while maintaining robustness in MJPC is to incorporate the use of Web of Affine Spaces (WASP) derivatives. In this section, we overview the WASP approach.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-A Coherence-based Approximate Derivatives", "weight": 1.0} -->

At a high level, WASP is an approach designed to compute a sequence of approximate derivatives: for some differentiable function $f$ and sequence of inputs $(\ \cdots\mathbf{x}_{k-1},\mathbf{x}_{k},\mathbf{x}_{k+1},\cdots\)$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-A Coherence-based Approximate Derivatives", "weight": 1.0} -->

The key insight associated with WASP is that derivatives need not be computed from scratch. In many applications, especially those rooted in iterative optimization, the function inputs evolve gradually over time, one leading into the next. As a result, the corresponding sequence of derivatives tends to exhibit temporal or spatial coherence, i.e., adjacent elements in the sequence share similarities. Thus, by reusing information from previous, closely related derivative computations, WASP seeks to accelerate derivative estimation while preserving accuracy.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-B WASP Overview", "weight": 1.0} -->

At its core, the WASP approach formulates derivative estimation as a constrained least-squares problem. Each iteration of the algorithm requires only a single Jacobian-vector product (JVP), which defines an affine subspace guaranteed to contain the true derivative. The optimization then seeks the transpose of an approximate derivative that lies within this affine subspace, enforced via a hard constraint, while simultaneously aligning with prior, related computations encoded in the objective function.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-B WASP Overview", "weight": 1.0} -->

This optimization is formalized as follows: Here, $\Delta\mathbf{X}\in\mathbb{R}^{n\times n}$ is referred to as the tangent matrix, whose columns represent input directions used to define the local linear neighborhood. The variable $\mathbf{D}\in\mathbb{R}^{m\times n}$ denotes the candidate Jacobian being optimized. The matrix $\hat{\Delta\mathbf{F}}\in\mathbb{R}^{m\times n}$ provides approximate JVPs corresponding to the directions in $\Delta\mathbf{X}$, defined as $\hat{\Delta\mathbf{F}}\approx\frac{\partial f}{\partial\mathbf{x}}\big|_{\mathbf{x}_{k}}\ \Delta\mathbf{X}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-B WASP Overview", "weight": 1.0} -->

The hard constraint enforces consistency in one chosen direction, where $\Delta\mathbf{x}_{i}$ is the $i$-th column of $\Delta\mathbf{X}$, and $\Delta\mathbf{f}_{i}$ is the corresponding ground-truth JVP at $\mathbf{x}_{k}$. This single JVP is estimated using finite differencing: The goal is for $\hat{\Delta\mathbf{F}}$ to require only a small number of new Jacobian-vector products (JVPs) per derivative computation, while the remaining columns preserve sufficient information from previous evaluations to yield a highly accurate approximation.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-B WASP Overview", "weight": 1.0} -->

In previous work, Rakita et al. derive a closed form solution for Equation 4 using a KKT system. They also show how to precompute and cache certain matrices in this solution to accelerate the solution at runtime.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-C Control over WASP Approximation", "weight": 1.0} -->

The WASP approach affords a convenient tradeoff between accuracy and efficiency. At a high level, this tradeoff is dictated by how many JVPs are computed (via function calls to the function $f$) to update $\hat{\Delta\mathbf{F}}$ per approximate solution, $\hat{\frac{\partial f}{\partial\mathbf{x}}}\big|_{\mathbf{x}_{k}}$. Using more JVPs yields a more accurate approximation, but at the cost of increased runtime due to more evaluations of $f$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-C Control over WASP Approximation", "weight": 1.0} -->

Four parameters are used to control the number of JVPs used per solution, denoted as $p_{max},p_{min},p_{\theta},p_{n}$. Here, $p_{max}$ and $p_{min}$ set a maximum and minimum on the number of JVPs, respectively. The $p_{\theta}$ and $p_{n}$ stop the JVP calculations and return a result when the current approximate derivative elicits approximate JVPs that sufficiently match the angle and norm of ground truth JVPs, respectively (fully detailed by Rakita et al. ). Lower values of $p_{\theta}$ and $p_{n}$ correspond to stricter accuracy thresholds, leading to more JVPs and higher computational cost.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

In this section, we describe how the WASP derivative approach is integrated into the MuJoCo MPC (MJPC) framework. We outline the practical aspects of adapting WASP to MJPC's planning pipeline, highlight tunable parameters that allow users to balance speed and accuracy, and discuss extensions to the MJPC graphical interface that make these capabilities accessible in practice.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-A WASP in MJPC", "weight": 1.0} -->

In MJPC, WASP derivatives are used to compute the model derivative matrices $\frac{\partial f}{\partial\mathbf{x}_{i}}\in\mathbb{R}^{d_{x}\times d_{x}}$ and $\frac{\partial f}{\partial\mathbf{u}_{i}}\in\mathbb{R}^{d_{x}\times d_{u}}$ at each time index $i$, overviewed in §II-B. Each time point along the planning horizon is treated as an independent instance of WASP. These instances can run independently in parallel and can optionally plug directly into MuJoCo's existing parallelization over the time horizon. This design ensures that the benefits of WASP scale naturally with MJPC's parallel execution model.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-A WASP in MJPC", "weight": 1.0} -->

Each WASP instance requires its own approximate JVP matrix, $\hat{\Delta\mathbf{F}}$. For model derivatives with respect to states, we maintain $\hat{\Delta\mathbf{F}}_{x,i}\in\mathbb{R}^{d_{x}\times d_{x}}$, and for derivatives with respect to controls, $\hat{\Delta\mathbf{F}}_{u,i}\in\mathbb{R}^{d_{x}\times d_{u}}$. These matrices are updated incrementally as new JVPs are computed during planning.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-A WASP in MJPC", "weight": 1.0} -->

In addition, each WASP instance requires a tangent matrix $\Delta\mathbf{X}$ to define the local linear neighborhood. These are $\Delta\mathbf{X}_{x,i}\in\mathbb{R}^{d_{x}\times d_{x}}$ for state derivatives and $\Delta\mathbf{X}_{u,i}\in\mathbb{R}^{d_{u}\times d_{u}}$ for control derivatives. However, since the tangent matrices are constant throughout runtime, we provide an option to reuse the same matrices across all time points, reducing memory requirements. In this case, only two matrices are maintained globally: $\Delta\mathbf{X}_{x}\in\mathbb{R}^{d_{x}\times d_{x}}$ and $\Delta\mathbf{X}_{u}\in\mathbb{R}^{d_{u}\times d_{u}}$. This shared-tangent setting is the default used in our evaluation.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-A WASP in MJPC", "weight": 1.0} -->

Following the analysis and recommendations of Rakita et al., all tangent matrices are chosen to be orthonormal to ensure favorable numerical properties.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-A WASP in MJPC", "weight": 1.0} -->

Finally, we directly incorporate these changes into the MuJoCo source code alongside the existing FD implementation in the C programming language. This integration allows WASP to function as a true drop-in replacement for all downstream MuJoCo-based applications, including our present study of MPC in MJPC.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-B Tunable Parameters", "weight": 1.0} -->

As introduced in §III-C, WASP has four low-level parameters ($p_{max},p_{min},p_{\theta},p_{n}$) that govern how many JVPs are used per derivative solution, trading off between accuracy and efficiency. To simplify this interface in MJPC, we expose only two parameters for users to adjust: a fraction parameter, denoted as frac, and a tolerance parameter, denoted as tol.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-B Tunable Parameters", "weight": 1.0} -->

Formally, these parameters are defined as follows: In other words, frac is a normalized value in the range $(0,1]$ relating $p_{min}$ and $p_{max}$, and tol is a stand-in label when $p_{\theta}$ and $p_{n}$ are equal, as is always the convention in our implementation. Also, we always fix $p_{max}$ to be the full number of inputs to the function (Rakita et al. show that WASP reduces to finite differencing at this number of JVPs); thus, frac is only a function of $p_{min}$, making it easier to adjust with respect to the fixed $p_{max}$ on a normalized scale.

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-B Tunable Parameters", "weight": 1.0} -->

Both parameters can be applied separately to the state and control derivative computations, which we denote as $(\texttt{frac}_{x},\texttt{tol}_{x})$ and $(\texttt{frac}_{u},\texttt{tol}_{u})$, respectively.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Evaluation", "weight": 1.0} -->

We demonstrate the efficacy of WASP derivatives in MJPC through three experiments. In this section, we overview these experiments and present our results. All experiments were executed on a desktop computer with an Intel i7 5.4GHz 28-core processor and 32 GB of RAM.

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-A Evaluation Tasks", "weight": 1.0} -->

We selected tasks from the MJPC benchmark suite based on three criteria: The task must satisfy $d_{x}+d_{u}\geq 10$ to ensure non-trivial computational complexity.

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-A Evaluation Tasks", "weight": 1.0} -->

The task must be solvable using at least one derivative-based planner with an FD backend to establish a performance baseline.

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-A Evaluation Tasks", "weight": 1.0} -->

The task must span a meaningful duration rather than being instantaneous to allow performance measurement over multiple planning iterations.

<!-- chunk {"id": "body-0062", "role": "body", "section": "V-A Evaluation Tasks", "weight": 1.0} -->

Based on these criteria, we evaluated ten locomotion tasks spanning various robot morphologies and complexities as shown in Fig. 1: Quadrotor ($d_{x}+d_{u}=16$): A UAV achieving a set of positional goals while at the same time avoiding collisions with obstacles.

<!-- chunk {"id": "body-0063", "role": "body", "section": "V-A Evaluation Tasks", "weight": 1.0} -->

Swimmer ($d_{x}+d_{u}=26$): An underwater snake robot navigating through fluid dynamics.

<!-- chunk {"id": "body-0064", "role": "body", "section": "V-A Evaluation Tasks", "weight": 1.0} -->

Quadruped Tasks ($d_{x}+d_{u}=48$): Six distinct locomotion behaviors (stand, climb, walk, canter, trot, gallop) of a four-legged robot with complex contact dynamics.

<!-- chunk {"id": "body-0065", "role": "body", "section": "V-A Evaluation Tasks", "weight": 1.0} -->

Biped Balance ($d_{x}+d_{u}=48$): A four-legged robot dog maintaining upright posture with only its hind legs contact the ground.

<!-- chunk {"id": "body-0066", "role": "body", "section": "V-A Evaluation Tasks", "weight": 1.0} -->

Humanoid Walk ($d_{x}+d_{u}=75$): A humanoid robot executing stable walking gaits These tasks represent diverse challenges in robotics control, from aerial navigation to legged locomotion with varying contact patterns. All tasks use default MJPC parameters unless otherwise specified, with planning horizon $T=50$, timestep $\Delta t=0.01$s, and the impedance ratio is set to $\text{impratio}=100$, making the frictional constraints much stiffer relative to normal constraints to obtain high-fidelity contact dynamics.

<!-- chunk {"id": "body-0067", "role": "body", "section": "V-B Experiment 1: WASP vs. FD", "weight": 1.0} -->

In Experiment 1, we compare WASP and FD as derivative backends in MJPC. Here, we outline the procedure, metrics, comparisons, and results for Experiment 1.

<!-- chunk {"id": "body-0068", "role": "body", "section": "V-B1 Procedure", "weight": 1.0} -->

For each task, we run the derivative-based planner(s) over a 30-second simulation window, recording performance metrics at each planning iteration.

<!-- chunk {"id": "body-0069", "role": "body", "section": "V-B1 Procedure", "weight": 1.0} -->

Parameters $\texttt{tol}_{x}$ and $\texttt{tol}_{u}$ were fixed at 0.5 in Experiment 1. Parameters $\texttt{frac}_{x}$ and $\texttt{frac}_{u}$ were minimally tuned ahead of time. Specifically, we started with parameters $\texttt{frac}_{x}=\texttt{frac}_{u}=0.3$ then incrementally raised both parameters until the robot first succeeds at the task. Typically, task success is evident when the Performance Ratio (explained below) exceeds a value of $0.7$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "V-B2 Metrics", "weight": 1.0} -->

We evaluate performance using three primary metrics: where a speedup greater than 1 indicates WASP is faster, and a performance ratio close to 1 indicates comparable task performance.

<!-- chunk {"id": "body-0071", "role": "body", "section": "V-B3 Comparisons", "weight": 1.0} -->

We compare two planners in Experiment 1: iLQG using an FD backend; and iLQG using a WASP backend. In preliminary experiments, we found that iLQG outperformed gradient descent on all of our tasks, so we only present these results here for simplicity. For full tables including gradient descent, please see our paper website \[link removed for blind review\].

<!-- chunk {"id": "body-0072", "role": "body", "section": "V-B4 Results", "weight": 1.0} -->

Task WASP Params M.D. Speedup Speedup Perf.

<!-- chunk {"id": "body-0073", "role": "body", "section": "V-B4 Results", "weight": 1.0} -->

from 1.26× to 2.08× compared to FD for model derivative computation across all tasks while maintaining at least sufficient task performance (defined here as Performance Ratio $\geq 0.7)$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "V-B4 Results", "weight": 1.0} -->

Notably, for some tasks (Quadrotor, Swimmer, and Quadruped Stand), WASP achieves performance ratios greater than 1, indicating improved task performance despite using approximated derivatives. We speculate that these results arise from slight approximation errors aiding in escaping local minima, though a deeper investigation is left for future work.

<!-- chunk {"id": "body-0075", "role": "body", "section": "V-C Experiment 2: WASP-based iLQG vs. Sampling-Based Planners", "weight": 1.0} -->

In Experiment 2, we compare WASP-based iLQG with stochastic sampling-based planners in MJPC. This section outlines the procedure, metrics, comparisons, and results for Experiment 2.

<!-- chunk {"id": "body-0076", "role": "body", "section": "V-C1 Procedure", "weight": 1.0} -->

The procedure in Experiment 2 is the same as Experiment 1 (§V-B1) including all parameter settings.

<!-- chunk {"id": "body-0077", "role": "body", "section": "V-C2 Metrics", "weight": 1.0} -->

Our metrics in Experiment 2 are similar to those in Experiment 1 (§V-B2): differing in two way: we remove the M.D. Speedup metric as stochastic sampling-based planners do not take model derivatives; and the Speedup metric replaces average planning time with FD in the numerator with average planning time for a given sampling-based planner.

<!-- chunk {"id": "body-0078", "role": "body", "section": "V-C2 Metrics", "weight": 1.0} -->

A speedup greater than or close to 1 with performance ratio greater than 1 indicates the WASP-based iLQG is faster or as fast as sampling-based planners with better task performance.

<!-- chunk {"id": "body-0079", "role": "body", "section": "V-C3 Comparisons", "weight": 1.0} -->

We compare five planners in Experiment 2: iLQG using a WASP backend; Predicative Sampling Robust Sampling; Cross Entropy Method; and Sample Gradient. Planners 2--5 are all of the stochastic sampling-based planners offered in MJPC.

<!-- chunk {"id": "body-0080", "role": "body", "section": "V-D Experiment 3: Parameter Robustness Analysis", "weight": 1.0} -->

In Experiment 3, we assess WASP's sensitivity to parameter selection. This section outlines the procedure, metrics, comparisons, and results.

<!-- chunk {"id": "body-0081", "role": "body", "section": "V-D1 Procedure", "weight": 1.0} -->

We only assess the quadruped trotting task over 1000 planning iterations, recording performance metrics at each iteration.

<!-- chunk {"id": "body-0082", "role": "body", "section": "V-D2 Metrics", "weight": 1.0} -->

Our metrics in Experiment 3 are: Cost evolution: Task performance as measured by cost function over iterations; Computation time: Model derivative calculation time in milliseconds; and Simulation steps: Number of forward simulations required.

<!-- chunk {"id": "body-0083", "role": "body", "section": "V-D3 Comparisons", "weight": 1.0} -->

We compare five parameter configurations against FD baseline: $(\texttt{frac}_{x},\texttt{frac}_{u})=(0.5,0.5)$: Balanced baseline. $(\texttt{frac}_{x},\texttt{frac}_{u})=(0.5,0.3)$: Reduced action accuracy. $(\texttt{frac}_{x},\texttt{frac}_{u})=(0.5,0.1)$: Minimal action accuracy. $(\texttt{frac}_{x},\texttt{frac}_{u})=(0.3,0.5)$: Reduced state accuracy. $(\texttt{frac}_{x},\texttt{frac}_{u})=(0.1,0.5)$: Minimal state accuracy.

<!-- chunk {"id": "body-0084", "role": "body", "section": "V-D4 Results", "weight": 1.0} -->

Results for Experiment 3 are shown in Figure 3. At a high level, we see that WASP is reasonably robust to parameter variations. When reducing $\texttt{frac}_{u}$ while maintaining $\texttt{frac}_{x}=0.5$ (purple and yellow lines), the planner maintains stable performance with consistent computational savings. However, reducing $\texttt{frac}_{x}$ while maintaining $\texttt{frac}_{u}=0.5$ (orange and red lines) causes instability, evidenced by cost spikes and erratic simulation counts. These results suggest that iLQG is particularly sensitive to the state transition accuracy, consistent with prior analysis by Todorov et al..

<!-- chunk {"id": "body-0085", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our work demonstrates that replacing finite differencing (FD) with Web of Affine Spaces (WASP) derivatives substantially improves the efficiency of derivative-based planning in MJPC. Across a broad set of locomotion tasks, WASP consistently reduced the computational burden of model derivative evaluations while maintaining, and in some cases even improving, task performance. The resulting speedups for model derivative computation of 1.26--2.08$\mathsf{x}$ enabled iLQG-based planners to operate faster than stochastic sampling-based planners, while delivering stronger and more reliable control. These findings suggest that coherence-based derivative approximations can offer a compelling balance between efficiency and robustness in iterative control settings.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Discussion", "weight": 1.5} -->

Beyond efficiency, our evaluation highlights how approximate derivatives can at times improve task outcomes compared to exact FD. We speculate that mild approximation error introduces a form of regularization, smoothing sharp gradients that often arise in contact-rich environments and helping optimization escape poor local minima. This effect, while encouraging, warrants deeper study in future work to fully understand its implications. In addition, our parameter sensitivity analysis showed that WASP is generally robust to variations, with accuracy in state transitions being more critical than control accuracy, a finding that aligns with prior analyses of iLQG.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Discussion", "weight": 1.5} -->

Importantly, WASP integrates directly into MJPC as a drop-in replacement, requiring no changes to the simulator's source code and allowing users to seamlessly switch between FD and WASP backends. This design lowers the barrier to adoption and creates opportunities for broader use in research and practice, particularly in scenarios where rapid derivative evaluations are essential for real-time performance. To support adoption, we also provide a fully open-source implementation of MJPC with WASP derivatives, making it straightforward for practitioners and researchers to experiment with these capabilities in their own applications.

<!-- chunk {"id": "body-0088", "role": "body", "section": "VI-A Limitations and Future Directions", "weight": 1.0} -->

While promising, this study has several limitations. First, all experiments were conducted in simulation, primarily on locomotion benchmarks. Since our contribution concerns derivative computation within a simulator-based MPC stack, simulation provides the appropriate controlled setting for measuring computational cost and numerical stability without hardware confounds. We therefore treat sim-to-real transfer as orthogonal to the present work, though extending to physical systems is a natural next step.

<!-- chunk {"id": "body-0089", "role": "body", "section": "VI-A Limitations and Future Directions", "weight": 1.0} -->

Second, both FD and WASP-based gradient planners struggled on contact-rich manipulation tasks, where short MPC horizons and discontinuous contact dynamics often lead to failures. These difficulties appear largely independent of the derivative approximation, pointing to structural limitations of short-horizon gradient-based MPC. Addressing them will likely require architectural changes, such as longer horizons or hybrid derivative- and sampling-based methods.

<!-- chunk {"id": "body-0090", "role": "body", "section": "VI-A Limitations and Future Directions", "weight": 1.0} -->

Finally, WASP's accuracy parameters require manual tuning to balance speed and fidelity. Developing principled or adaptive selection schemes could further improve robustness and usability.

<!-- chunk {"id": "body-0091", "role": "body", "section": "VI-A Limitations and Future Directions", "weight": 1.0} -->

Overall, we view this work as a step toward integrating coherence-based derivative approximations into real-time MPC. By demonstrating meaningful speed and stability gains within MJPC, we aim to expand the practical alternatives to finite differencing and encourage broader exploration of structured approximate derivatives in robotics control.
