<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

PISTO: Proximal Inference for Stochastic Trajectory Optimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Stochastic trajectory optimization methods like STOMP enable planning with non-differentiable costs, offering substantial flexibility over gradient-based approaches. We show that STOMP implicitly minimizes the KL divergence from a Boltzmann trajectory distribution, revealing an elegant Variational Inference (VI) structure underlying its updates. Building on this insight, we propose the \textit{Proximal Inference for Stochastic Trajectory Optimization} (PISTO) algorithm that stabilizes the updates by augmenting the objective with a KL regularization between successive Gaussian proposals. This proximal formulation admits a trust-region interpretation and yields closed-form mean updates computable as expectations under a surrogate distribution. We estimate these expectations via importance-weighted Monte Carlo sampling, producing a simple, derivative-free algorithm that inherits STOMP's ability to handle non-differentiable and discontinuous costs without modification. On robot arm motion planning benchmarks, PISTO achieves an 89\% success rate - outperforming CHOMP (63\%) and STOMP (68\%) - while producing shorter, smoother paths at twice the speed of competing stochastic methods.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We further validate PISTO on contact-rich MuJoCo locomotion and manipulation tasks, where it consistently outperforms both CEM and MPPI baselines in reward.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning is central to robotics, enabling autonomous systems to generate collision-free, dynamically feasible trajectories in cluttered environments. While sampling-based methods such as PRM and RRT^⋆^ provide strong exploration and asymptotic guarantees, their trajectories often require substantial post-processing for smoothness and dynamic feasibility. Consequently, trajectory optimization has become essential for high-performance planning in manipulation, mobile robotics, and aerial systems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimization-based planners---including CHOMP, sequential convex programming, and Gaussian process methods ---represent trajectories in continuous time and optimize for smoothness, collision avoidance, and dynamic constraints. These approaches achieve impressive speed and scalability, but they rely on differentiable cost representations and remain susceptible to local minima in highly nonconvex environments.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stochastic trajectory optimization broadens the class of tractable objectives by introducing sampling. STOMP and path-integral methods such as PI^2^ perturb candidate trajectories and update them via cost-weighted averaging, enabling optimization under non-differentiable and discontinuous costs. A natural question arises: what objective does STOMP implicitly optimize?

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that STOMP minimizes the reverse KL divergence from a Boltzmann trajectory distribution, revealing an elegant variational inference structure underlying its updates. This connection places STOMP within a broader inference-based planning framework, where trajectory costs define a Boltzmann distribution whose high-probability mass concentrates on desirable plans. Gaussian variational inference formulations (GVIMP) approximate this distribution with a structured Gaussian family, providing uncertainty quantification and a principled KL-divergence objective.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Building on this insight, we develop a proximal inference algorithm that stabilizes STOMP's updates. Proximal methods augment each iterate with a penalty on the distance from the current solution, effectively creating a trust region that prevents overly aggressive steps. In the distributional setting, this naturally extends to KL-divergence penalties between successive proposals, controlling how rapidly the trajectory distribution evolves. By combining the variational inference perspective with proximal regularization, we obtain closed-form mean updates computable via importance-weighted Monte Carlo sampling---a simple, derivative-free algorithm that inherits STOMP's flexibility while offering principled stability guarantees.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We reveal that STOMP implicitly minimizes KL divergence from a Boltzmann trajectory distribution, establishing its variational inference structure and motivating principled algorithmic improvements.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose *Proximal Inference for Stochastic Trajectory Optimization (PISTO)*, which augments the reverse-KL objective with a proximal penalty between successive Gaussian proposals. This formulation admits a trust-region interpretation, stabilizes optimization dynamics, and yields closed-form mean updates computable via importance-weighted Monte Carlo sampling.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate PISTO's effectiveness across diverse robotics tasks: on motion planning benchmarks, PISTO achieves 89% success rate---outperforming CHOMP (63%), STOMP (68%), and natural gradient descent (76%)---while running twice as fast as competing stochastic methods. On contact-rich MuJoCo tasks, PISTO consistently outperforms CEM and MPPI baselines in reward despite non-differentiable dynamics.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Planning as Inference", "weight": 1.0} -->

The interpretation of optimal control as probabilistic inference connects to linearly-solvable control, path-integral methods, and variational formulations in RL. Within motion planning, Toussaint applied message passing on graphical models, while Stein Variational approaches maintain trajectory distributions via particle-based inference. Our work builds on the Planning as Inference paradigm, which showed that trajectory optimization with control-energy regularization is equivalent to KL-divergence minimization from a Boltzmann distribution. We solve the inference problem using a proximal inference algorithm that provides stable optimization and efficient Monte Carlo estimation. Other works under this paradigm are closely related. The variational and heteroscedasticity GP planners either rely on pre-defined kernels, induction point approximations, or start and goal states, which cannot be easily extended to control space optimization. Mixtures of Gaussian Processes for Trajectory Optimization (MGPTO) obtains a multi-modal trajectory using a STOMP-style cost-weighted stochastic gradient estimate. P-GVIMP leverages GPU parallel computation to accelerate the mean and covariance updates in a gradient-descent landscape.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Trajectory Optimization", "weight": 1.0} -->

Gradient-based methods such as CHOMP, TrajOpt, and GPMP achieve fast convergence but require differentiable costs. Sampling-based methods relax this requirement: STOMP uses cost-weighted averaging, path integral methods (PI^2^, MPPI ) derive updates from stochastic control, and CEM fits distributions to elite samples. Our method differs: (i) revealing STOMP's variational inference structure via KL-divergence; (ii) introducing proximal regularization for trust-region stability; and (iii) deriving closed-form updates amenable to importance sampling.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Trajectory Optimization", "weight": 1.0} -->

Our method introduces three key innovations over these approaches: (i) an explicit connection between STOMP's objective and KL-divergence minimization, revealing its variational inference structure; (ii) proximal regularization that stabilizes updates with a trust-region interpretation; and (iii) a reversed KL formulation yielding closed-form mean updates amenable to unbiased importance sampling.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Stochastic Trajectory Optimization as Variational Inference Planning", "weight": 1.0} -->

In this section, we establish the theoretical foundation of our approach by connecting classical stochastic trajectory optimization with variational inference. We begin by introducing the STOMP framework, followed by its interpretation as a variational inference problem.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Stochastic Trajectory Optimization (STOMP)", "weight": 1.0} -->

Stochastic Trajectory Optimization for Motion Planning (STOMP) is a gradient-free optimization framework designed to handle non-differentiable and discontinuous cost functions. It explores the trajectory space by generating stochastic perturbations around a nominal trajectory and updating it based on the exponentiated cost of these samples.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Stochastic Trajectory Optimization (STOMP)", "weight": 1.0} -->

Let $Y\in\mathbb{R}^{n(T+1)}$ represent the mean of a $T$-length state trajectory, defined as $Y\triangleq\{x_{t}\}_{t=0}^{T}$. STOMP seeks to minimize the expectation of a cost functional over a proposal Gaussian distribution $\tilde{Y}\sim\mathcal{N}(Y,\Sigma)$: where $S(\tilde{Y})=\sum_{t=0}^{T}V(\tilde{Y}_{t})$ is the state-dependent potential (e.g., obstacle avoidance) and $R=A^{\top}A$ is the control cost matrix for double integrator dynamics, with $A\in\mathbb{R}^{(T-1)\times(T+1)}$ the finite-difference acceleration operator applying the stencil $/\Delta t^{2}$ at interior nodes.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Stochastic Trajectory Optimization (STOMP)", "weight": 1.0} -->

This stochastic formulation allows the planner to \"smooth\" the cost landscape, effectively escaping local minima that often trap purely gradient-based methods.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B Variational Inference Interpretation of STOMP", "weight": 1.0} -->

The objective (1 ‣ III Stochastic Trajectory Optimization as Variational Inference Planning ‣ PISTO: Proximal Inference for Stochastic Trajectory Optimization")) admits a Variational Inference (VI) interpretation that recasts trajectory optimization as approximating an optimal path distribution. Any cost function over trajectories induces a Boltzmann distribution where low-cost trajectories receive high probability mass; this construction underlies the connection between optimal control and inference and path-integral methods. In (1 ‣ III Stochastic Trajectory Optimization as Variational Inference Planning ‣ PISTO: Proximal Inference for Stochastic Trajectory Optimization")), the state-dependent potential $S(\tilde{Y})$ captures task-specific objectives such as obstacle avoidance, while the control cost $\frac{1}{2}\tilde{Y}^{\top}R\tilde{Y}$ with $R=A^{\top}A$ corresponds to a Gaussian smoothness prior $\mathcal{N}(0,R^{-1})$ favoring low-acceleration paths. Combining the two yields the main result connecting STOMP to VI.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Proximal Inference for Stochastic Trajectory Optimization", "weight": 1.0} -->

We introduce a novel paradigm for solving the motion planning inference problem: Proximal Inference for Stochastic Trajectory Optimization (PISTO). PISTO reverses the argument order in the KL divergence and augments the objective with a Gaussian proximal term, converting each iteration into a proximal inference minimization whose optimizer admits a closed-form expectation representation amenable to Monte Carlo estimation.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-A Solution to the Reverse KL Minimization Problem", "weight": 1.0} -->

We first introduce an important moment-matching solution result in reverse KL minimization problems.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The surrogate distribution ${\mathbb{Y}}^{\star}_{k}$ geometrically interpolates between the true target ${\mathbb{Y}}^{\star}$ and the current Gaussian approximation $\mathcal{N}(Y_{k},\Sigma)$. As $\eta\to\infty$, the surrogate converges to the true target, recovering standard VI. For finite $\eta$, the proximal term regularizes the update, improving numerical stability and convergence.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-C Moment-matching Solution to the Proximal Inference", "weight": 1.0} -->

Eq. (11. ‣ IV-B The main PISTO Formulation ‣ IV Proximal Inference for Stochastic Trajectory Optimization ‣ PISTO: Proximal Inference for Stochastic Trajectory Optimization")) indicates that each proximal iteration is itself a VI problem with respect to the surrogate distribution ${\mathbb{Y}}^{\star}_{k}$, which is typically easier to handle than the original Boltzmann distribution. To compute the update, we solve the reverse KL-minimization projection To sample from ${\mathbb{Y}}^{\star}_{k}$, we rewrite it in a tilted-Gaussian form by completing the square. Letting $\gamma\triangleq\frac{\eta}{\eta+1}$, we obtain where $P=\gamma R+(1-\gamma)\Sigma^{-1}$ and $\mu_{k}=(1-\gamma)P^{-1}\Sigma^{-1}Y_{k}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-C Moment-matching Solution to the Proximal Inference", "weight": 1.0} -->

This representation reveals that ${\mathbb{Y}}^{\star}_{k}$ behaves like a Gaussian whose mean is shifted by the proximal term, modulated by an exponential tilt involving the cost function: Applying the gradient identity from (6. ‣ IV-A Solution to the Reverse KL Minimization Problem ‣ IV Proximal Inference for Stochastic Trajectory Optimization ‣ PISTO: Proximal Inference for Stochastic Trajectory Optimization")) to the reverse KL-minimizing objective and setting it to zero yields the following result.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-D Importance Sampling", "weight": 1.0} -->

To estimate the expectation in (17. ‣ IV-C Moment-matching Solution to the Proximal Inference ‣ IV Proximal Inference for Stochastic Trajectory Optimization ‣ PISTO: Proximal Inference for Stochastic Trajectory Optimization")), we employ importance sampling from a Gaussian proposal distribution. Similar to Eq. (8. ‣ IV-A Solution to the Reverse KL Minimization Problem ‣ IV Proximal Inference for Stochastic Trajectory Optimization ‣ PISTO: Proximal Inference for Stochastic Trajectory Optimization")), the weight at iteration $k$ is In the common choice $\Sigma=R^{-1}$, the expression simplifies considerably, as $P=R$ and $\mu_{k}=(1-\gamma)Y_{k}$: Using these weights, we obtain a Monte-Carlo estimation of the proximal update: where $\varepsilon_{m}\sim\mathcal{N}(0,R^{-1}),\;m=1,\dots,M$ are sampled independently.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-D Importance Sampling", "weight": 1.0} -->

This Monte Carlo estimator completes the proximal inference update, providing a stable and efficient mechanism for refining the Gaussian approximation at each iteration.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-D Importance Sampling", "weight": 1.0} -->

1:Accumulated cost S(⋅), smoothness matrix R, Cholesky factor L with LL⊤ = R−1, sample size M, proximal parameter η, current iterate Yk, temperature τ 3:Compute $\gamma\leftarrow\dfrac{\eta}{\eta+1}$ 4:Sample: Draw {εm}m = 1M where εm = Lzm, zm ∼ 𝒩(0, I) 5:Evaluate: For each m = 1, …, M, compute importance weights $$w_{m}\leftarrow\exp\!\Big(-\frac{\gamma}{\tau}\,S(Y_{k}+\varepsilon_{m})-(\varepsilon_{m})^{\top}R\,Y_{k}\Big)$$ 6:Normalize: Compute normalized weights

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-D Importance Sampling", "weight": 1.0} -->

(a) The PushT Task. Optimization time: 260.62(s).

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-D Importance Sampling", "weight": 1.0} -->

(b) The Humanoid Running Task. Optimization time: 142.21(s).

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-D Importance Sampling", "weight": 1.0} -->

(c) The Humanoid Standing Up Task. Optimization time: 168.11(s).

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-E Policy Optimization for Contact-Rich Tasks", "weight": 1.0} -->

We now extend PISTO to policy optimization in the action space, where the decision variable is the *control sequence* $U=\{u_{t}\}_{t=0}^{T-1}$ and states evolve according to known dynamics models.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Composite Structure of the Objective", "weight": 1.0} -->

The state trajectory is uniquely determined by the initial condition and control sequence via recursive application of. We formalize this through the *flow map* $\phi_{t}:\mathbb{R}^{d_{x}}\times\mathbb{R}^{t\times d_{u}}\to\mathbb{R}^{d_{x}}$: with the convention $\phi_{0}(x_{0})=x_{0}$. Substituting into and defining the *rollout cost* the optimal control problem reduces to the form of (1 ‣ III Stochastic Trajectory Optimization as Variational Inference Planning ‣ PISTO: Proximal Inference for Stochastic Trajectory Optimization")): where the quadratic term $\frac{1}{2}\tilde{U}^{\top}R\tilde{U}$ regularizes the control sequence for temporal smoothness.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Composite Structure of the Objective", "weight": 1.0} -->

Algorithm 1 applies directly in this setting, with each sample $\tilde{U}^{(i)}\sim\mathcal{N}(U,\Sigma)$ evaluated by rolling out the dynamics $\phi_{t}$ to obtain $S(\tilde{U}^{(i)};x_{0})$. This formulation enables PISTO to optimize directly in control space without requiring differentiability of $g$ or $c$, and admits efficient parallelization of rollouts on modern GPU hardware.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-F Covariance and Proximal Step Size Annealing", "weight": 1.0} -->

To balance exploration and exploitation, we implement covariance scheduling with adaptive temperature scaling. We scale the smoothness matrix, $\bar{R}=\sigma_{k}\times R$, and use $\bar{R}$ matrix as the actual matrix that we sample. The covariance scale $\sigma_{k}$ follows cosine annealing: where $k$ is the current iteration and $K_{\mathrm{max}}$ the maximum. We introduce an adaptive annealing scheme for the proximal step size parameter $\eta$ governing the exploration-exploitation trade-off in importance-weighted trajectory optimization. We also introduce an additional temperature parameter $\tau$ to scale the impact of the adaptive proximal step size. The importance weights are $w_{m}\propto\exp\left(-\frac{\gamma}{\tau}S(Y_{k}+\varepsilon_{m})-(\varepsilon_{m})^{\top}RY_{k}\right)$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-F Covariance and Proximal Step Size Annealing", "weight": 1.0} -->

We anneal $\eta$ from small to large values via an exponential schedule $\eta(t)=\eta_{\text{initial}}\cdot(\eta_{\text{final}}/\eta_{\text{initial}})^{t/T}$, where small $\eta$ encourages exploration through nearly uniform weights while large $\eta$ exploits high-reward samples with peaked weights. The temperature $\tau$ amplifies only the energy term, leaving regularization unaffected, enabling independent control over reward sensitivity and trajectory smoothness ^00^footnotetext: For STOMP, we employed the official implementation Figure 4: Benchmark Performance Statistics

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

All experiments were run on a computer with an Intel Core i7-12800H CPU. The MuJoCo experiments were run on a computer with an NVIDIA RTX 4090 GPU. The code for this paper is implemented in C++ for the motion planning tasks, and in Python for the trajectory optimization tasks in MuJoCo.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-A Motion Planning for Robot Arms", "weight": 1.0} -->

For collision avoidance, we define the state cost $V(Y_{t})$ using two formulations. The *signed-distance* cost approximates the robot as a union of spheres and evaluates where $F(\cdot)$ is the forward kinematics, $d_{\mathrm{sdf}}(\cdot)$ queries a precomputed signed distance field (SDF), and the hinge function $h_{\delta}(\cdot)$ penalizes penetrations within margin $\delta$. The non-differentiable *indicator* cost, used in MoveIt benchmarking experiments, imposes a fixed penalty on detected collision: The weights $\Sigma_{\rm obs}$ and $W_{\rm obs}$ are task-dependent hyper-parameters.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-B Policy Optimization Tasks", "weight": 1.0} -->

We tested the PISTO algorithm on various tasks defined in MuJoCo. We used Bayesian optimization-based parameter sweeping to obtain the recommended parameters for each task. Figure 2 illustrates the optimization process for a standing up task for a $17$-DOF humanoid robot. Table I records the achieved rewards for different tasks. Planning and Runtime Results: Table I records PISTO's performance in contact-rich trajectory optimization tasks, compared with CEM and MPPI methods. The results are averaged over $50$ independent runs. Our proposed PISTO algorithm significantly outperforms both baselines across all five contact-rich tasks, achieving approximately $1.5\times$ improvement on Walker2d and $2.8\times$ on HumanoidRun compared to the best baseline, while converting negative MPPI performance on PushT ($-0.17$) into a positive reward of $0.46$. PISTO also runs $1.4\times$--$3.2\times$ faster than baselines on most tasks, with particularly notable speedups on HumanoidRun ($36.5$s vs. $\sim$`<!-- -->`{=html}115s).

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-B Policy Optimization Tasks", "weight": 1.0} -->

The tight standard deviations indicate reliable convergence despite discontinuous contact dynamics. Notably, PISTO achieves successful results for the $17$-DOF humanoid running and standing-up tasks within minutes. These results validate PISTO's robustness for trajectory optimization in hybrid dynamical systems.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-B Policy Optimization Tasks", "weight": 1.0} -->

Motion Planning (7-DOF Manipulator) Reward (Per step) Trajectory Optimization for Contact-Rich Tasks TABLE I: Benchmarking Results: Motion Planning and Trajectory Optimization

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-C Benchmarking with MoveIt Motion Planning Algorithms", "weight": 1.0} -->

We further benchmark PISTO against several representative optimization-based baselines using MoveIt, including the official implementations of STOMP and CHOMP, as well as a natural gradient descent (NGD) method. Experiments are conducted on the Franka Emika Panda across seven manipulation environments from the MotionBenchMaker dataset, including *Kitchen*, *Bookshelf Tall*, *Bookshelf Thin*, *Table Pick*, *Table Under Pick*, *Box*, and *Cage*, with over 300 planning tasks in total.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-C Benchmarking with MoveIt Motion Planning Algorithms", "weight": 1.0} -->

For a fair comparison, all planners are initialized using the same joint-space straight-line interpolation between the start and goal configurations. We repeat each planning task 20 times with different random seeds. A run is considered successful if the resulting trajectory is collision-free and satisfies joint limits. Figure 4 summarizes the benchmarking results in terms of success rate, planning time, path length, and path clearance.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented the Proximal Inference for Stochastic Trajectory Optimization (PISTO), a principled algorithm for motion planning formulated as Gaussian variational inference. By revealing STOMP's implicit variational structure, we introduced a proximal formulation that regularizes updates via KL penalties, yielding closed-form moment-matching updates amenable to importance sampling. The resulting algorithm is simple, derivative-free, and parallelizable. Experiments demonstrated that PISTO achieves 89% success on motion planning benchmarks---outperforming CHOMP, STOMP, and natural gradient baselines---while additional MuJoCo experiments validated its effectiveness for high-dimensional, contact-rich tasks. Future work includes incorporating gradients when available, jointly optimizing mean and covariance, and extending to receding-horizon MPC.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Elite Sample Selection", "weight": 1.0} -->

To improve convergence and reduce variance, we incorporate elite-set selection within the importance sampling step. Given $M$ rollouts, we define an elite subset $\mathcal{M}_{e}\subset\{1,\dots,M\}$ containing samples in the lowest $K_{\mathrm{elite}}$-th percentile of cost. Importance weights for $m\notin\mathcal{M}_{e}$ are set to zero, while for $m\in\mathcal{M}_{e}$: where $J(\cdot)$ is the trajectory cost and $\tau$ is an adaptive temperature. This selective pressure ensures updates are driven by successful explorations, enabling efficient navigation of non-convex cost landscapes.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Momentum-Accelerated Exponential Moving Average", "weight": 1.0} -->

To stabilize convergence and accelerate optimization, we apply a momentum-based update scheme. Let $\hat{Y}_{k+1}$ denote the candidate trajectory computed as the weighted expectation over the elite set $\hat{Y}_{k+1}=\sum_{m\in\mathcal{M}_{e}}w_{m}(Y_{k}+\varepsilon_{m}).$ We compute the update direction $\Delta_{k}=\hat{Y}_{k+1}-Y_{k}$ and maintain a momentum buffer $v_{k}$ via exponential moving average: where $\beta\in[0,1)$ is the momentum decay coefficient. The trajectory is then updated as: $Y_{k+1}=Y_{k}+\lambda v_{k+1},$ where $\lambda\in(0,1]$ is the step size. This two-stage temporal regularization dampens oscillations through directional smoothing while providing momentum for navigating non-smooth cost regions.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Momentum-Accelerated Exponential Moving Average", "weight": 1.0} -->

We also allow the Adam-type gradient update rule as an option.
