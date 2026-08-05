<!-- arxiv-full-text:v1 {"arxiv_id": "2605.07215", "source": "arxiv-html"} -->

## Introduction

Motion planning is central to robotics, enabling autonomous systems to generate collision-free, dynamically feasible trajectories in cluttered environments. While sampling-based methods such as PRM and RRT^⋆^ provide strong exploration and asymptotic guarantees, their trajectories often require substantial post-processing for smoothness and dynamic feasibility. Consequently, trajectory optimization has become essential for high-performance planning in manipulation, mobile robotics, and aerial systems.

Optimization-based planners---including CHOMP, sequential convex programming, and Gaussian process methods ---represent trajectories in continuous time and optimize for smoothness, collision avoidance, and dynamic constraints. These approaches achieve impressive speed and scalability, but they rely on differentiable cost representations and remain susceptible to local minima in highly nonconvex environments.

Stochastic trajectory optimization broadens the class of tractable objectives by introducing sampling. STOMP and path-integral methods such as PI^2^ perturb candidate trajectories and update them via cost-weighted averaging, enabling optimization under non-differentiable and discontinuous costs. A natural question arises: what objective does STOMP implicitly optimize?

We show that STOMP minimizes the reverse KL divergence from a Boltzmann trajectory distribution, revealing an elegant variational inference structure underlying its updates. This connection places STOMP within a broader inference-based planning framework, where trajectory costs define a Boltzmann distribution whose high-probability mass concentrates on desirable plans. Gaussian variational inference formulations (GVIMP) approximate this distribution with a structured Gaussian family, providing uncertainty quantification and a principled KL-divergence objective.

Building on this insight, we develop a proximal inference algorithm that stabilizes STOMP's updates. Proximal methods augment each iterate with a penalty on the distance from the current solution, effectively creating a trust region that prevents overly aggressive steps. In the distributional setting, this naturally extends to KL-divergence penalties between successive proposals, controlling how rapidly the trajectory distribution evolves. By combining the variational inference perspective with proximal regularization, we obtain closed-form mean updates computable via importance-weighted Monte Carlo sampling---a simple, derivative-free algorithm that inherits STOMP's flexibility while offering principled stability guarantees.

We reveal that STOMP implicitly minimizes KL divergence from a Boltzmann trajectory distribution, establishing its variational inference structure and motivating principled algorithmic improvements.

We propose *Proximal Inference for Stochastic Trajectory Optimization (PISTO)*, which augments the reverse-KL objective with a proximal penalty between successive Gaussian proposals. This formulation admits a trust-region interpretation, stabilizes optimization dynamics, and yields closed-form mean updates computable via importance-weighted Monte Carlo sampling.

We demonstrate PISTO's effectiveness across diverse robotics tasks: on motion planning benchmarks, PISTO achieves 89% success rate---outperforming CHOMP (63%), STOMP (68%), and natural gradient descent (76%)---while running twice as fast as competing stochastic methods. On contact-rich MuJoCo tasks, PISTO consistently outperforms CEM and MPPI baselines in reward despite non-differentiable dynamics.

## Related Work

### Planning as Inference

The interpretation of optimal control as probabilistic inference connects to linearly-solvable control, path-integral methods, and variational formulations in RL. Within motion planning, Toussaint applied message passing on graphical models, while Stein Variational approaches maintain trajectory distributions via particle-based inference. Our work builds on the Planning as Inference paradigm, which showed that trajectory optimization with control-energy regularization is equivalent to KL-divergence minimization from a Boltzmann distribution. We solve the inference problem using a proximal inference algorithm that provides stable optimization and efficient Monte Carlo estimation. Other works under this paradigm are closely related. The variational and heteroscedasticity GP planners either rely on pre-defined kernels, induction point approximations, or start and goal states, which cannot be easily extended to control space optimization. Mixtures of Gaussian Processes for Trajectory Optimization (MGPTO) obtains a multi-modal trajectory using a STOMP-style cost-weighted stochastic gradient estimate. P-GVIMP leverages GPU parallel computation to accelerate the mean and covariance updates in a gradient-descent landscape.

### Trajectory Optimization

Gradient-based methods such as CHOMP, TrajOpt, and GPMP achieve fast convergence but require differentiable costs. Sampling-based methods relax this requirement: STOMP uses cost-weighted averaging, path integral methods (PI^2^, MPPI ) derive updates from stochastic control, and CEM fits distributions to elite samples. Our method differs : (i) revealing STOMP's variational inference structure via KL-divergence; (ii) introducing proximal regularization for trust-region stability; and (iii) deriving closed-form updates amenable to importance sampling.

Our method introduces three key innovations over these approaches: (i) an explicit connection between STOMP's objective and KL-divergence minimization, revealing its variational inference structure; (ii) proximal regularization that stabilizes updates with a trust-region interpretation; and (iii) a reversed KL formulation yielding closed-form mean updates amenable to unbiased importance sampling.

## Stochastic Trajectory Optimization as Variational Inference Planning

In this section, we establish the theoretical foundation of our approach by connecting classical stochastic trajectory optimization with variational inference. We begin by introducing the STOMP framework, followed by its interpretation as a variational inference problem.

### III-A Stochastic Trajectory Optimization (STOMP)

Stochastic Trajectory Optimization for Motion Planning (STOMP) is a gradient-free optimization framework designed to handle non-differentiable and discontinuous cost functions. It explores the trajectory space by generating stochastic perturbations around a nominal trajectory and updating it based on the exponentiated cost of these samples.

Let $Y\in\mathbb{R}^{n(T+1)}$ represent the mean of a $T$-length state trajectory, defined as $Y\triangleq\{x_{t}\}_{t=0}^{T}$. STOMP seeks to minimize the expectation of a cost functional over a proposal Gaussian distribution $\tilde{Y}\sim\mathcal{N}(Y,\Sigma)$: where $S(\tilde{Y})=\sum_{t=0}^{T}V(\tilde{Y}_{t})$ is the state-dependent potential (e.g., obstacle avoidance) and $R=A^{\top}A$ is the control cost matrix for double integrator dynamics, with $A\in\mathbb{R}^{(T-1)\times(T+1)}$ the finite-difference acceleration operator applying the stencil $/\Delta t^{2}$ at interior nodes.

This stochastic formulation allows the planner to \"smooth\" the cost landscape, effectively escaping local minima that often trap purely gradient-based methods.

### III-B Variational Inference Interpretation of STOMP

The objective (1 ‣ III Stochastic Trajectory Optimization as Variational Inference Planning ‣ PISTO: Proximal Inference for Stochastic Trajectory Optimization")) admits a Variational Inference (VI) interpretation that recasts trajectory optimization as approximating an optimal path distribution. Any cost function over trajectories induces a Boltzmann distribution where low-cost trajectories receive high probability mass; this construction underlies the connection between optimal control and inference and path-integral methods. In (1 ‣ III Stochastic Trajectory Optimization as Variational Inference Planning ‣ PISTO: Proximal Inference for Stochastic Trajectory Optimization")), the state-dependent potential $S(\tilde{Y})$ captures task-specific objectives such as obstacle avoidance, while the control cost $\frac{1}{2}\tilde{Y}^{\top}R\tilde{Y}$ with $R=A^{\top}A$ corresponds to a Gaussian smoothness prior $\mathcal{N}(0,R^{-1})$ favoring low-acceleration paths. Combining the two yields the main result connecting STOMP to VI.

### Theorem 1 (Variational Inference Formulation of STOMP)

Consider the stochastic trajectory optimization objective (1 ‣ III Stochastic Trajectory Optimization as Variational Inference Planning ‣ PISTO: Proximal Inference for Stochastic Trajectory Optimization")). Let $\Sigma\succ 0$ be a fixed covariance and $R\succ 0$ be the control cost matrix. Minimizing $\mathcal{J}_{1}$ over the mean trajectory $Y$ is equivalent to solving the variational inference problem: where the target distribution is the energy-based posterior:

### Proof

## Proximal Inference for Stochastic Trajectory Optimization

We introduce a novel paradigm for solving the motion planning inference problem: Proximal Inference for Stochastic Trajectory Optimization (PISTO). PISTO reverses the argument order in the KL divergence and augments the objective with a Gaussian proximal term, converting each iteration into a proximal inference minimization whose optimizer admits a closed-form expectation representation amenable to Monte Carlo estimation.

### IV-A Solution to the Reverse KL Minimization Problem

We first introduce an important moment-matching solution result in reverse KL minimization problems.

### Lemma 1 (Reverse KL Minimization and Moment-matching Solution)

Consider the reverse KL objective obtained by swapping distributions in (3. ‣ III-B Variational Inference Interpretation of STOMP ‣ III Stochastic Trajectory Optimization as Variational Inference Planning ‣ PISTO: Proximal Inference for Stochastic Trajectory Optimization")): where ${\mathbb{Y}}^{\star}\propto e^{-S(\tilde{Y})}\mathcal{N}(0,R^{-1})$. The gradient of the objective (5. ‣ IV-A Solution to the Reverse KL Minimization Problem ‣ IV Proximal Inference for Stochastic Trajectory Optimization ‣ PISTO: Proximal Inference for Stochastic Trajectory Optimization")) with respect to $Y$ is and the optimal mean is given by With the choice $\Sigma=R^{-1}$ and proposal distribution $\tilde{Y}\sim\mathcal{N}(Y,R^{-1})$, the importance sampling estimator is where $\varepsilon_{m}\sim\mathcal{N}(0,R^{-1})$ are i.i.d. samples.

The proof of Lemma 1. ‣ IV-A Solution to the Reverse KL Minimization Problem ‣ IV Proximal Inference for Stochastic Trajectory Optimization ‣ PISTO: Proximal Inference for Stochastic Trajectory Optimization") can be found .

### IV-B The main PISTO Formulation

### Theorem 2 (Proximal Inference Update)

Consider the proximal update for the VI problem (3. ‣ III-B Variational Inference Interpretation of STOMP ‣ III Stochastic Trajectory Optimization as Variational Inference Planning ‣ PISTO: Proximal Inference for Stochastic Trajectory Optimization")): where $\eta>0$ is the step size parameter, $Y_{k}$ is the current iterate, and ${\mathbb{Y}}^{\star}\propto e^{-S(\tilde{Y})}\mathcal{N}(0,R^{-1})$ is the target distribution. Then the proximal update is equivalent to KL projection onto a surrogate distribution: where the surrogate target ${\mathbb{Y}}^{\star}_{k}$ admits the explicit form

### Proof

### Remark 1

The surrogate distribution ${\mathbb{Y}}^{\star}_{k}$ geometrically interpolates between the true target ${\mathbb{Y}}^{\star}$ and the current Gaussian approximation $\mathcal{N}(Y_{k},\Sigma)$. As $\eta\to\infty$, the surrogate converges to the true target, recovering standard VI. For finite $\eta$, the proximal term regularizes the update, improving numerical stability and convergence.

### IV-C Moment-matching Solution to the Proximal Inference

Eq. (11. ‣ IV-B The main PISTO Formulation ‣ IV Proximal Inference for Stochastic Trajectory Optimization ‣ PISTO: Proximal Inference for Stochastic Trajectory Optimization")) indicates that each proximal iteration is itself a VI problem with respect to the surrogate distribution ${\mathbb{Y}}^{\star}_{k}$, which is typically easier to handle than the original Boltzmann distribution. To compute the update, we solve the reverse KL-minimization projection To sample from ${\mathbb{Y}}^{\star}_{k}$, we rewrite it in a tilted-Gaussian form by completing the square. Letting $\gamma\triangleq\frac{\eta}{\eta+1}$, we obtain where $P=\gamma R+(1-\gamma)\Sigma^{-1}$ and $\mu_{k}=(1-\gamma)P^{-1}\Sigma^{-1}Y_{k}$. This representation reveals that ${\mathbb{Y}}^{\star}_{k}$ behaves like a Gaussian whose mean is shifted by the proximal term, modulated by an exponential tilt involving the cost function: Applying the gradient identity from (6. ‣ IV-A Solution to the Reverse KL Minimization Problem ‣ IV Proximal Inference for Stochastic Trajectory Optimization ‣ PISTO: Proximal Inference for Stochastic Trajectory Optimization")) to the reverse KL-minimizing objective and setting it to zero yields the following result.

### Theorem 3 (Moment-Matching Update)

The solution to the reverse KL-minimization projection satisfies the condition which admits the closed-form moment-matching update That is, the next iterate is simply the mean of the surrogate distribution ${\mathbb{Y}}^{\star}_{k}$.

### IV-D Importance Sampling

To estimate the expectation in (17. ‣ IV-C Moment-matching Solution to the Proximal Inference ‣ IV Proximal Inference for Stochastic Trajectory Optimization ‣ PISTO: Proximal Inference for Stochastic Trajectory Optimization")), we employ importance sampling from a Gaussian proposal distribution. Similar to Eq. (8. ‣ IV-A Solution to the Reverse KL Minimization Problem ‣ IV Proximal Inference for Stochastic Trajectory Optimization ‣ PISTO: Proximal Inference for Stochastic Trajectory Optimization")), the weight at iteration $k$ is In the common choice $\Sigma=R^{-1}$, the expression simplifies considerably, as $P=R$ and $\mu_{k}=(1-\gamma)Y_{k}$: Using these weights, we obtain a Monte-Carlo estimation of the proximal update: where $\varepsilon_{m}\sim\mathcal{N}(0,R^{-1}),\;m=1,\dots,M$ are sampled independently. This Monte Carlo estimator completes the proximal inference update, providing a stable and efficient mechanism for refining the Gaussian approximation at each iteration.

1:Accumulated cost S(⋅), smoothness matrix R, Cholesky factor L with LL⊤ = R−1, sample size M, proximal parameter η, current iterate Yk, temperature τ 3:Compute $\gamma\leftarrow\dfrac{\eta}{\eta+1}$ 4:Sample: Draw {εm}m = 1M where εm = Lzm, zm ∼ 𝒩(0, I) 5:Evaluate: For each m = 1, …, M, compute importance weights $$w_{m}\leftarrow\exp\!\Big(-\frac{\gamma}{\tau}\,S(Y_{k}+\varepsilon_{m})-(\varepsilon_{m})^{\top}R\,Y_{k}\Big)$$ 6:Normalize: Compute normalized weights $$\bar{w}_{m}\leftarrow\frac{w_{m}}{\sum_{j=1}^{M}w^{(j)}},\quad\forall m$$ 7:Update: Compute weighted mean $$Y_{k+1}\leftarrow Y_{k}+\sum_{m=1}^{M}\bar{w}_{m}\,\varepsilon_{m}$$ Figure 1: Results of PISTO in different motion planning benchmarking scenes.

(a) The PushT Task. Optimization time: 260.62(s).

(b) The Humanoid Running Task. Optimization time: 142.21(s).

(c) The Humanoid Standing Up Task. Optimization time: 168.11(s).

Figure 2: The optimization results for contact-rich tasks.

Figure 3: Results of different planners in the Kitchen scene in the database.

### IV-E Policy Optimization for Contact-Rich Tasks

We now extend PISTO to policy optimization in the action space, where the decision variable is the *control sequence* $U=\{u_{t}\}_{t=0}^{T-1}$ and states evolve according to known dynamics models.

### Formulation

Given initial state $x_{0}\in\mathbb{R}^{d_{x}}$, consider the finite-horizon optimal control problem: subject to the dynamics and control constraints: where $U=(u_{0},\ldots,u_{T-1})\in\mathbb{R}^{T\times d_{u}}$, $c:\mathbb{R}^{d_{x}}\times\mathbb{R}^{d_{u}}\to\mathbb{R}$ is the stage cost, $g:\mathbb{R}^{d_{x}}\times\mathbb{R}^{d_{u}}\to\mathbb{R}^{d_{x}}$ is the dynamics model, and $\mathcal{U}=[\underline{u},\bar{u}]$ is the admissible control set.

### Composite Structure of the Objective

The state trajectory is uniquely determined by the initial condition and control sequence via recursive application of. We formalize this through the *flow map* $\phi_{t}:\mathbb{R}^{d_{x}}\times\mathbb{R}^{t\times d_{u}}\to\mathbb{R}^{d_{x}}$: with the convention $\phi_{0}(x_{0})=x_{0}$. Substituting into and defining the *rollout cost* the optimal control problem reduces to the form of (1 ‣ III Stochastic Trajectory Optimization as Variational Inference Planning ‣ PISTO: Proximal Inference for Stochastic Trajectory Optimization")): where the quadratic term $\frac{1}{2}\tilde{U}^{\top}R\tilde{U}$ regularizes the control sequence for temporal smoothness. Algorithm 1 applies directly in this setting, with each sample $\tilde{U}^{(i)}\sim\mathcal{N}(U,\Sigma)$ evaluated by rolling out the dynamics $\phi_{t}$ to obtain $S(\tilde{U}^{(i)};x_{0})$. This formulation enables PISTO to optimize directly in control space without requiring differentiability of $g$ or $c$, and admits efficient parallelization of rollouts on modern GPU hardware.

### IV-F Covariance and Proximal Step Size Annealing

To balance exploration and exploitation, we implement covariance scheduling with adaptive temperature scaling. We scale the smoothness matrix, $\bar{R}=\sigma_{k}\times R$, and use $\bar{R}$ matrix as the actual matrix that we sample. The covariance scale $\sigma_{k}$ follows cosine annealing: where $k$ is the current iteration and $K_{\mathrm{max}}$ the maximum. We introduce an adaptive annealing scheme for the proximal step size parameter $\eta$ governing the exploration-exploitation trade-off in importance-weighted trajectory optimization. We also introduce an additional temperature parameter $\tau$ to scale the impact of the adaptive proximal step size. The importance weights are $w_{m}\propto\exp\left(-\frac{\gamma}{\tau}S(Y_{k}+\varepsilon_{m})-(\varepsilon_{m})^{\top}RY_{k}\right)$. We anneal $\eta$ from small to large values via an exponential schedule $\eta(t)=\eta_{\text{initial}}\cdot(\eta_{\text{final}}/\eta_{\text{initial}})^{t/T}$, where small $\eta$ encourages exploration through nearly uniform weights while large $\eta$ exploits high-reward samples with peaked weights. The temperature $\tau$ amplifies only the energy term, leaving regularization unaffected, enabling independent control over reward sensitivity and trajectory smoothness ^00^footnotetext: For STOMP, we employed the official implementation Figure 4: Benchmark Performance Statistics

## Experiments

All experiments were run on a computer with an Intel Core i7-12800H CPU. The MuJoCo experiments were run on a computer with an NVIDIA RTX 4090 GPU. The code for this paper is implemented in C++ for the motion planning tasks, and in Python for the trajectory optimization tasks in MuJoCo.

### V-A Motion Planning for Robot Arms

For collision avoidance, we define the state cost $V(Y_{t})$ using two formulations. The *signed-distance* cost approximates the robot as a union of spheres and evaluates where $F(\cdot)$ is the forward kinematics, $d_{\mathrm{sdf}}(\cdot)$ queries a precomputed signed distance field (SDF), and the hinge function $h_{\delta}(\cdot)$ penalizes penetrations within margin $\delta$. The non-differentiable *indicator* cost, used in MoveIt benchmarking experiments, imposes a fixed penalty on detected collision: The weights $\Sigma_{\rm obs}$ and $W_{\rm obs}$ are task-dependent hyper-parameters.

### V-B Policy Optimization Tasks

We tested the PISTO algorithm on various tasks defined in MuJoCo. We used Bayesian optimization-based parameter sweeping to obtain the recommended parameters for each task. Figure 2 illustrates the optimization process for a standing up task for a $17$-DOF humanoid robot. Table I records the achieved rewards for different tasks. Planning and Runtime Results: Table I records PISTO's performance in contact-rich trajectory optimization tasks, compared with CEM and MPPI methods. The results are averaged over $50$ independent runs. Our proposed PISTO algorithm significantly outperforms both baselines across all five contact-rich tasks, achieving approximately $1.5\times$ improvement on Walker2d and $2.8\times$ on HumanoidRun compared to the best baseline, while converting negative MPPI performance on PushT ($-0.17$) into a positive reward of $0.46$. PISTO also runs $1.4\times$--$3.2\times$ faster than baselines on most tasks, with particularly notable speedups on HumanoidRun ($36.5$s vs. $\sim$`<!-- -->`{=html}115s). The tight standard deviations indicate reliable convergence despite discontinuous contact dynamics. Notably, PISTO achieves successful results for the $17$-DOF humanoid running and standing-up tasks within minutes. These results validate PISTO's robustness for trajectory optimization in hybrid dynamical systems.

Motion Planning (7-DOF Manipulator) Reward (Per step) Trajectory Optimization for Contact-Rich Tasks TABLE I: Benchmarking Results: Motion Planning and Trajectory Optimization

### V-C Benchmarking with MoveIt Motion Planning Algorithms

We further benchmark PISTO against several representative optimization-based baselines using MoveIt, including the official implementations of STOMP and CHOMP, as well as a natural gradient descent (NGD) method. Experiments are conducted on the Franka Emika Panda across seven manipulation environments from the MotionBenchMaker dataset, including *Kitchen*, *Bookshelf Tall*, *Bookshelf Thin*, *Table Pick*, *Table Under Pick*, *Box*, and *Cage*, with over 300 planning tasks in total.

For a fair comparison, all planners are initialized using the same joint-space straight-line interpolation between the start and goal configurations. We repeat each planning task 20 times with different random seeds. A run is considered successful if the resulting trajectory is collision-free and satisfies joint limits. Figure 4 summarizes the benchmarking results in terms of success rate, planning time, path length, and path clearance.

## Conclusion

We presented the Proximal Inference for Stochastic Trajectory Optimization (PISTO), a principled algorithm for motion planning formulated as Gaussian variational inference. By revealing STOMP's implicit variational structure, we introduced a proximal formulation that regularizes updates via KL penalties, yielding closed-form moment-matching updates amenable to importance sampling. The resulting algorithm is simple, derivative-free, and parallelizable. Experiments demonstrated that PISTO achieves 89% success on motion planning benchmarks---outperforming CHOMP, STOMP, and natural gradient baselines---while additional MuJoCo experiments validated its effectiveness for high-dimensional, contact-rich tasks. Future work includes incorporating gradients when available, jointly optimizing mean and covariance, and extending to receding-horizon MPC.

### A Proofs

### Proof of Theorem 1. ‣ III-B Variational Inference Interpretation of STOMP ‣ III Stochastic Trajectory Optimization as Variational Inference Planning ‣ PISTO: Proximal Inference for Stochastic Trajectory Optimization")

Define the accumulated state cost $S(\tilde{Y})=\sum_{t=0}^{T}V(\tilde{Y}_{t})$. Since the covariance $\Sigma$ is fixed, the expectation of the quadratic deviation term simplifies via the trace identity $\mathbb{E}[(\tilde{Y}-Y)^{\top}R(\tilde{Y}-Y)]=\operatorname{tr}(R\Sigma)$. Thus, We recognize that $\mathbb{E}_{\tilde{Y}}[S(\tilde{Y})]=-\mathbb{E}_{\tilde{Y}}[\log e^{-S(\tilde{Y})}]$. Combining this with the KL divergence between Gaussians, where the last two terms are constants, we obtain by introducing the un-normalized ${\mathbb{Y}}^{\star}\propto e^{-S(\tilde{Y})}\mathcal{N}(0,R^{-1})$. Here, the constant is independent of $Y$. Since only the mean $Y$ is optimized, minimizing $\mathcal{J}_{1}$ is equivalent to minimizing the KL divergence to the target posterior ${\mathbb{Y}}^{\star}$.

### Proof of Theorem 2. ‣ IV-B The main PISTO Formulation ‣ IV Proximal Inference for Stochastic Trajectory Optimization ‣ PISTO: Proximal Inference for Stochastic Trajectory Optimization")

Let $q_{Y}$ and $q_{Y_{k}}$ denote the density functions of $\mathcal{N}(Y,\Sigma)$ and $\mathcal{N}(Y_{k},\Sigma)$, respectively. The proximal objective can be written as Factoring out the coefficient $\frac{\eta+1}{\eta}$ yields where we identify the surrogate distribution as Substituting the explicit form of ${\mathbb{Y}}^{\star}$ completes the proof.

### B Implementation Details

### Elite Sample Selection

To improve convergence and reduce variance, we incorporate elite-set selection within the importance sampling step. Given $M$ rollouts, we define an elite subset $\mathcal{M}_{e}\subset\{1,\dots,M\}$ containing samples in the lowest $K_{\mathrm{elite}}$-th percentile of cost. Importance weights for $m\notin\mathcal{M}_{e}$ are set to zero, while for $m\in\mathcal{M}_{e}$: where $J(\cdot)$ is the trajectory cost and $\tau$ is an adaptive temperature. This selective pressure ensures updates are driven by successful explorations, enabling efficient navigation of non-convex cost landscapes.

### Momentum-Accelerated Exponential Moving Average

To stabilize convergence and accelerate optimization, we apply a momentum-based update scheme. Let $\hat{Y}_{k+1}$ denote the candidate trajectory computed as the weighted expectation over the elite set $\hat{Y}_{k+1}=\sum_{m\in\mathcal{M}_{e}}w_{m}(Y_{k}+\varepsilon_{m}).$ We compute the update direction $\Delta_{k}=\hat{Y}_{k+1}-Y_{k}$ and maintain a momentum buffer $v_{k}$ via exponential moving average: where $\beta\in[0,1)$ is the momentum decay coefficient. The trajectory is then updated as: $Y_{k+1}=Y_{k}+\lambda v_{k+1},$ where $\lambda\in(0,1]$ is the step size. This two-stage temporal regularization dampens oscillations through directional smoothing while providing momentum for navigating non-smooth cost regions. We also allow the Adam-type gradient update rule as an option.
