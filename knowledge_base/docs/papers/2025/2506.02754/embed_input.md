<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Safely Learning Controlled Stochastic Dynamics

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We address the problem of safely learning controlled stochastic dynamics from discrete-time trajectory observations, ensuring system trajectories remain within predefined safe regions during both training and deployment. Safety-critical constraints of this kind are crucial in applications such as autonomous robotics, finance, and biomedicine. We introduce a method that ensures safe exploration and efficient estimation of system dynamics by iteratively expanding an initial known safe control set using kernel-based confidence bounds. After training, the learned model enables predictions of the system's dynamics and permits safety verification of any given control. Our approach requires only mild smoothness assumptions and access to an initial safe control set, enabling broad applicability to complex real-world systems. We provide theoretical guarantees for safety and derive adaptive learning rates that improve with increasing Sobolev regularity of the true dynamics. Experimental evaluations demonstrate the practical effectiveness of our method in terms of safety, estimation accuracy, and computational efficiency.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider the problem of safely learning the dynamics of controlled continuous-time stochastic systems from discrete-time observations of trajectory data. This setting is common in applications such as robotics, finance, and healthcare, where system dynamics are only partially known and must be estimated from data. A key challenge in these applications is ensuring safety during both the learning phase and subsequent deployment \[Bonalli et al. Lew et al., \]. As an example, consider an autonomous robot navigating a partially known and turbulent environment, as illustrated in Figure. While the deterministic part of the dynamics may be approximately modeled using prior knowledge, the stochastic disturbances due to wind or sensor noise are often unknown and must be learned. Collecting data through naive exploration can result in unsafe trajectories, potentially causing damage to the system or its environment. A second example arises in financial portfolio management, where the drift component of asset prices may be known from historical data, but market volatility remains uncertain. Safety here may correspond to the requirement that the portfolio value stays above a critical threshold with high probability, simulating portfolio loss aversion in risk-sensitive financial decision-making.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

These examples highlight a common need: learning stochastic dynamics of a system from data, while ensuring safety throughout the process. This requires ensuring that all executed trajectories remain within a predefined safe region with high probability. In addition, at deployment time, the learned model should enable prediction of whether a proposed control input satisfies the safety requirements, including those not encountered during training \[Wabersich and Zeilinger Lindemann et al., \].

<!-- chunk {"id": "body-0005", "role": "body", "section": "Outline of contributions", "weight": 1.0} -->

The contributions of this work are as follows.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Outline of contributions", "weight": 1.0} -->

Safe learning method. We derive a method that safely learns controlled stochastic dynamics, where safety is defined as the requirement that system trajectories remain within a designated set of safe states with high probability. Our approach incrementally expands the known safe control set by selecting novel controls to evaluate, collecting corresponding trajectory data, and refining three models: a dynamics model for predicting state evolution, a safety model that estimates the probability of remaining within the safe region, and a reset model that captures the probability of returning the system to its initial state distribution, enabling repeated safe exploration under uncertainty. Alongside these models, we refine uncertainty estimates using kernel-based confidence bounds. After training, these models enable prediction of dynamics, safety, and reset feasibility for any given control, including those not seen during training.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Outline of contributions", "weight": 1.0} -->

Provably safe exploration and adaptive estimation rates. We prove that the proposed method guarantees safety and derive learning rates for system estimation, with rates that are adaptive to the Sobolev regularity of the underlying dynamics. Crucially, our approach requires only smooth dynamics (with respect to time, state, and control variables) and an initial non-empty set of known safe controls. These mild assumptions make the method applicable to a broad range of complex real-world systems subject to stochastic disturbances, found in diverse areas including robotics, fluid flow control, and chemical reaction control \[Martin and Salaün Plappert et al. Morton et al. Peters et al. Fu et al. Wei et al., \].

<!-- chunk {"id": "body-0008", "role": "body", "section": "Outline of contributions", "weight": 1.0} -->

Experimental validation. We empirically demonstrate the performance of the approach in terms of safety, estimation accuracy, and computational efficiency. Specifically, we evaluate it on a benchmark two-dimensional stochastic dynamical system evolving in a bounded, safety-critical environment under stochastic perturbations. An open-source Python implementation is provided (available at github.com/lmotte/dynamics-safe-learn).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Controlled SDE", "weight": 1.0} -->

Let $X$ be a dynamical system governed by a non-linear, $n$-dimensional controlled SDE \[Bonalli and Bonnet Lew et al., \],

<!-- chunk {"id": "body-0010", "role": "body", "section": "Example 1 (Second-order dynamical system)", "weight": 1.0} -->

captures second-order dynamics under control $u$ and state-dependent diffusion $a\left( {X{(t)}} \right)$. Real-world examples include drones navigating turbulent environments (where $u$ represents thrust or steering, and $a{( \cdot )}$ models wind turbulence), fluid-dynamical systems \[Batchelor, \], and molecular dynamics (where $u$ captures external forces such as optical traps, and $a{( \cdot )}$ reflects spatially varying thermal fluctuations \[Volpe and Volpe Marago et al. Pesce et al., \]).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Safe control", "weight": 1.0} -->

Let $X_{u}$ denote the solution to Eq. under the control $u \in \mathcal{H}$. Let $u_{\theta}:{{{\lbrack 0,T_{\max}\rbrack} \times {\mathbb{R}}^{n}}\rightarrow{\mathbb{R}}^{d}}$ denote a family of controls parameterized by $\theta \in D \subset {\mathbb{R}}^{m}$, where $D$ is a compact subset of ${\mathbb{R}}^{m}$. Such a finite-dimensional parameterization is a mild assumption that is widely prevalent in many real-world applications, including robotics \[Berkenkamp et al., \], process control \[Seborg et al., \], and financial engineering \[Merton, \].

<!-- chunk {"id": "body-0012", "role": "body", "section": "Safe control", "weight": 1.0} -->

We define the safety level of the control $u_{\theta}$ at time $t \in {\lbrack 0,T_{\max}\rbrack}$ as

<!-- chunk {"id": "body-0013", "role": "body", "section": "Safe control", "weight": 1.0} -->

We define the safety level up to time $T \in {\lbrack 0,T_{\max}\rbrack}$ of the control $u_{\theta}$ as

<!-- chunk {"id": "body-0014", "role": "body", "section": "Learning problem", "weight": 1.0} -->

We formulate the problem of safely learning controlled stochastic dynamical systems as the estimation of the probability density map

<!-- chunk {"id": "body-0015", "role": "body", "section": "Learning problem", "weight": 1.0} -->

where $p_{\theta}{(t,x)}$ is the density of the state $X_{u_{\theta}}{(t)}$ under control $u_{\theta}$, well-defined by standard existence and uniqueness results. To estimate this density, we collect a dataset of trajectories

<!-- chunk {"id": "body-0016", "role": "body", "section": "Learning problem", "weight": 1.0} -->

where each $w_{i}^{k}$ denotes an independent Brownian motion sample path driving the stochastic trajectory, and $M_{k}$ denotes the number of time steps in trajectory $k$. All controls $u_{\theta_{k}}$ are required to be safe. Specifically, the minimal probability of remaining within the safe region up to the time horizons ${(T_{k})}_{k = 1}^{K} = {(t_{M_{k}})}_{k = 1}^{K}$ is constrained by

<!-- chunk {"id": "body-0017", "role": "body", "section": "Learning problem", "weight": 1.0} -->

This problem poses a fundamental challenge due to the coupling between learning and safety: accurately estimating the density $p_{\theta}$ requires data, but collecting data must respect safety constraints defined by $s^{\infty}$, which themselves depend on the very dynamics encoded in $p_{\theta}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumptions", "weight": 1.0} -->

As formalized by the No-Free-Lunch Theorem \[Devroye et al., \], learning is only possible under prior assumptions. We now state and discuss the key assumptions used in this work.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption (A1) (Initial safe controls)", "weight": 1.0} -->

For $\varepsilon \in {\lbrack 0,1\rbrack}$, a non-empty set $S_{0} \subset {D \times {\lbrack 0,T_{\max}\rbrack}}$ is provided such that

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption (A1) (Initial safe controls)", "weight": 1.0} -->

This assumption ensures that at least one control is known to be safe at the outset, allowing safe exploration to begin. In fact, $S_{0}$ may be as small as a singleton; only one known safe control is required. Without such a point, safe learning cannot be initiated. We express the assumption in set form to allow for larger safe sets, which can accelerate exploration while preserving guarantees. This is a standard assumption in the literature of safe UCB methods \[Sui et al. Turchetta et al. Berkenkamp et al., \], and is realistic in many applications including robotics \[Sukhija et al., \] and safety-critical process control \[Qin and Badgwell, \], where systems naturally start in safe conditions, e.g., $S_{0} = {\{{(0,\theta)}:{\theta \in D}\}}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Resetting control", "weight": 1.0} -->

Let $h:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ define a region in the state space from which resets are feasible. Specifically, if ${h{({X{(t)}})}} \geq 0$, then it is feasible to reset the system to the initial distribution $p_{0}$. Formally, this means there exists a mechanism (or control) that reinitializes the system from the current state $X{(t)}$ to a new state independently sampled from $p_{0}$. We define the reset level at time $t \in {\lbrack 0,T_{\max}\rbrack}$ for a given control $u_{\theta}$ as

<!-- chunk {"id": "body-0022", "role": "body", "section": "Resetting control", "weight": 1.0} -->

The function $h$ delimits a region of the state space from which resets are feasible. Larger reset regions correspond to greater operational flexibility. In simulated environments, where resets are effectively cost-free, the reset region can cover the entire state space ${\mathbb{R}}^{n}$. In contrast, real-world systems typically require substantial resources or manual intervention, making resets feasible only in restricted regions (e.g., near the original distribution $p_{0}$).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption (A2) (Initial resetting controls)", "weight": 1.0} -->

For $\xi \in {\lbrack 0,1\rbrack}$, a non-empty set $R_{0} \subset {D \times {\lbrack 0,T_{\max}\rbrack}}$ is provided such that

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption (A2) (Initial resetting controls)", "weight": 1.0} -->

This assumption guarantees the existence of at least one control capable of returning the system to the reset region with high probability. Assumption (A2) (Initial resetting controls). ‣ Resetting control. ‣ 3 Assumptions ‣ Safely Learning Controlled Stochastic Dynamics") enables the generation of independent sample paths starting from the same initial conditions, which is crucial for evaluating variance and managing uncertainty during safe exploration. As with Assumption (A1) (Initial safe controls). ‣ 3 Assumptions ‣ Safely Learning Controlled Stochastic Dynamics"), one known reset point is sufficient, though larger reset sets accelerate learning. A simple case is $R_{0} = {\{{(0,\theta)}:{\theta \in D}\}}$, corresponding to systems that can always be reset from the initial condition. In practice, reset feasibility depends on system constraints: for instance, batch chemical reactors can often be reset only in early phases, before irreversible reactions occur \[Seborg et al., \]. In contrast, many autonomous systems like drones or driving robots can usually be reset, at least during training.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption (A3) (Smoothness of system dynamics)", "weight": 1.0} -->

This smoothness assumption ensures that the system dynamics are sufficiently regular for our purposes. It is standard in statistical learning theory and underpins our convergence guarantees \[Pillaud-Vivien et al., \]. Sobolev regularity of the drift and diffusion terms in the underlying stochastic differential equation is expected to imply Sobolev regularity of the resulting state densities under standard conditions. This follows from classical results in parabolic PDE theory, where solutions typically gain regularity relative to the coefficients, roughly two derivatives in space and one in time. A formal analysis of this connection is beyond the scope of the present work and is left for future investigation.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Proposed method", "weight": 1.0} -->

We propose a method for safely exploring and learning system dynamics over a parameterized control space $\mathcal{H} = {\{ u_{\theta}\mid{\theta \in D \subset {\mathbb{R}}^{m}}\}}$. Following the safe UCB framework \[Sui et al. Bottero et al., \], our goal is to select controls that reduce model uncertainty while ensuring, with high probability, that trajectories (i) remain within the safe region and (ii) end in the reset region. We jointly learn three models: a dynamics model (state densities), a safety model (safety probabilities), and a reset model (reset probabilities), each equipped with confidence bounds from a shared kernel. This enables active exploration under high-probability constraints. After training, the learned models support inference on unseen inputs and yield a certified control set that can be deployed with safety guarantees.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Proposed method", "weight": 1.0} -->

The known safe-resettable set is expanded iteratively by alternating between system estimation (Section 4.2) and safe sampling (Section 4.3), leveraging prior knowledge of the initial safe and reset sets as well as the regularity of the dynamics ${(\theta,t,x)}\mapsto{p_{\theta}{(t,x)}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Proposed method", "weight": 1.0} -->

A step-by-step breakdown of the overall method is provided in Appendix B, with algorithm tables for each module and their computational complexities.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Initialization", "weight": 1.0} -->

Let $N \in {\mathbb{N}}$ denote the current iteration. We initialize at $N = 0$ using the known safe set $S_{0} \subset {D \times {\lbrack 0,T_{\max}\rbrack}}$ and reset set $R_{0} \subset {D \times {\lbrack 0,T_{\max}\rbrack}}$. We define the initial safe-resettable set

<!-- chunk {"id": "body-0030", "role": "body", "section": "Initialization", "weight": 1.0} -->

We select ${(\theta_{0},t_{0},T_{0})} \in \Gamma_{0}$, ensuring that the control is known to be safe over $\lbrack 0,T_{0}\rbrack$ and ends in the reset region.

<!-- chunk {"id": "body-0031", "role": "body", "section": "System estimation", "weight": 1.0} -->

In this step, we update the dynamics, safety, and reset models based on the observed trajectories, and compute predictive uncertainty for each.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Estimation at $(\\theta_{N},t_{N})$", "weight": 1.0} -->

At iteration $N$, the control $u_{\theta_{N}}$ is evaluated using $Q$ stochastic trajectories. Here, $N$ indexes the iteration, and $i$ indexes the $i$-th trajectory simulated under that control, each corresponding to an independent sample $w_{i}^{N}$ of the Brownian motion driving the system.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Estimation at $(\\theta_{N},t_{N})$", "weight": 1.0} -->

We then compute estimates of the safety and reset probabilities

<!-- chunk {"id": "body-0034", "role": "body", "section": "Estimation at $(\\theta_{N},t_{N})$", "weight": 1.0} -->

Let the collection of values at all observed points $\left( {(\theta_{i},t_{i})} \right)_{i = 1}^{N}$ be

<!-- chunk {"id": "body-0035", "role": "body", "section": "Model update", "weight": 1.0} -->

We fit kernel ridge regressors for the density, safety, and reset functions using a Matérn kernel $k$ (with Sobolev smoothness $\nu$) and regularization $\lambda > 0$

<!-- chunk {"id": "body-0036", "role": "body", "section": "Model update", "weight": 1.0} -->

where ${k{(\theta,t)}} \triangleq {({k{({(\theta,t)},{(\theta_{i},t_{i})})}})}_{i = 1}^{N}$, $K \triangleq {({k{({(\theta_{i},t_{i})},{(\theta_{j},t_{j})})}})}_{{i,j} = 1}^{N}$, and $\lambda$ is a regularization term. Although training data consist of discrete-time observations, learned regression models are defined over continuous time, a distinction seldom addressed in the literature.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Model update", "weight": 1.0} -->

The predictive uncertainty at $(\theta,t)$ is given by

<!-- chunk {"id": "body-0038", "role": "body", "section": "Safe sampling", "weight": 1.0} -->

We now select a new point to sample by maximizing uncertainty over the safe-resettable region.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Feasibility criteria", "weight": 1.0} -->

A point $(\theta,t,T)$ is feasible if (i) $t \leq T$, (ii) the system remains safe up to time $T$, i.e., ${s^{\infty}{(\theta,T)}} \geq {1 - \varepsilon}$, and (iii) the trajectory ends in the reset region with high probability, i.e., ${r{(\theta,T)}} \geq {1 - \xi}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Feasibility criteria", "weight": 1.0} -->

We implement these constraints via lower confidence bounds (LCBs)

<!-- chunk {"id": "body-0041", "role": "body", "section": "Feasibility criteria", "weight": 1.0} -->

where ${\beta_{N}^{s},\beta_{N}^{r}} > 0$ are confidence parameters set from known upper bounds on the RKHS norms of the safety and reset functions.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Feasibility criteria", "weight": 1.0} -->

We then define the safe-resettable feasible set

<!-- chunk {"id": "body-0043", "role": "body", "section": "Sampling rule", "weight": 1.0} -->

We choose the next $(\theta_{N + 1},t_{N + 1},T_{N + 1})$ by maximizing uncertainty over the feasible set

<!-- chunk {"id": "body-0044", "role": "body", "section": "Sampling rule", "weight": 1.0} -->

Optimization is performed using discretization or gradient-based methods. Several computational techniques for efficient optimization are presented in the Appendix.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Stopping rule", "weight": 1.0} -->

We stop the exploration once the maximum uncertainty over the feasible set falls below a threshold $\eta > 0$

<!-- chunk {"id": "body-0046", "role": "body", "section": "Stopping rule", "weight": 1.0} -->

ensuring that exploration concludes once the models reaches the desired level of accuracy.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The derivation in Appendix A.7 shows that the confidence parameters depend on upper bounds of the RKHS norms of the safety and reset functions. These bounds may be available from prior knowledge of the system's regularity. We view this prior knowledge as a reasonable minimal assumption for guaranteeing safe learning under unknown dynamics. When unavailable, the bounds can be conservatively overestimated, ensuring safety but potentially leading to slower exploration. Developing adaptive strategies to estimate these quantities without prior knowledge is a promising direction for future work, for instance through online adaptation via the doubling trick \[Shalev-Shwartz and others, \].

<!-- chunk {"id": "body-0048", "role": "body", "section": "Safety and estimation guarantees for Sobolev dynamics", "weight": 1.0} -->

Safety and exploration guarantees for safe kernelized UCB methods have been developed in prior work \[Sui et al. Bottero et al., \], grounded in kernelized bandit theory \[Srinivas et al. Valko et al. Janz et al., \], which in turn builds on linear bandit results \[Dani et al. Auer, \]. Building on this foundation, we establish novel theoretical guarantees for safe exploration and dynamics estimation under Sobolev regularity. Complete proofs are deferred to Appendix A.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

We evaluate our method on a representative smooth nonlinear stochastic system. Specifically, the experiments aim to assess the following: (i) satisfaction of safety and reset constraints, (ii) efficiency of exploration under different safety thresholds, (iii) prediction accuracy for dynamics, safety, and reset maps, (iv) computational cost and scalability.

<!-- chunk {"id": "body-0050", "role": "body", "section": "System and environment", "weight": 1.0} -->

We consider a 2D second-order dynamical system whose acceleration is directly controlled by the input. The system evolves according to the controlled SDE

<!-- chunk {"id": "body-0051", "role": "body", "section": "System and environment", "weight": 1.0} -->

with $X_{c} = {}$, $\sigma = 2$, and $A = 5$. The initial state follows $\mathcal{N}{(0,{\sigma_{0}I_{{\mathbb{R}}^{2}}})}$ with $\sigma_{0} = 0.1$, and the maximal time horizon is $T_{\max} = 20$. The system evolves within the bounded safe region ${({- 10},10)}^{2}$, and each trajectory must end in the reset region defined as a disk of radius 2.5 centered at the origin. Such models arise in robotics and autonomous navigation, involving trajectory control with localized disturbances (e.g., slippery or uneven terrain). Figure illustrates the effect of such state-dependent noise through 100 trajectories generated under different controls.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Control space", "weight": 1.0} -->

Controls are parameterized as sequences of $m$ fixed accelerations of magnitude $v$, applied in directions $(\theta_{1},\ldots,\theta_{m})$. During the exploration phase $({0 \leq t \leq T_{explo}})$, each direction $\theta_{i}$ is applied over intervals of equal length, yielding

<!-- chunk {"id": "body-0053", "role": "body", "section": "Control space", "weight": 1.0} -->

with damping term $- V$ ensuring velocity convergence.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Control space", "weight": 1.0} -->

with damping factor $\kappa > 0$. Controls are clipped to keep the system within the safe region. We set $v = 2.0$, $\kappa = 0.5$, $m = 2$, $T_{explo} = 6$, and $n_{\text{steps}} = 500$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Method's hyperparameters", "weight": 1.0} -->

Our method depends on several hyperparameters that govern safety thresholds $(\varepsilon,\xi)$, confidence levels $(\beta_{s},\beta_{r})$, kernel smoothness $(\lambda,\gamma)$, and bandwidth $R$, with distinct values for estimating dynamics and constraints. We test ${(\varepsilon,\xi)} \in {\{ 0.1,\, 0.3,\, 0.5,\infty\}}$, with 1000 iterations and initial safe control $({- {\pi/3}},{\pi/3})$. Candidate selection for uncertainty maximization is restricted to a local subset for efficiency. A detailed discussion of each hyperparameter's role, tuning procedure, and practical heuristics is provided in Appendix B.3.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Exploration rate and coverage", "weight": 1.0} -->

In Figure, we plot the selected controls after 1000 iterations for various threshold pairs $\varepsilon = \xi$, with values increasing from left to right in $\{ 0.1,\, 0.3,\, 0.5,{+ \infty}\}$. Figures and clearly illustrate the exploration-safety trade-off. Relaxing thresholds leads to broader control coverage and faster information gain, but with decreased safety guarantees. Conversely, strict thresholds restrict exploration, particularly around regions with safety or reset probabilities close to the specified thresholds. This aligns with the intuition supported by our theoretical analysis: sample complexity tends to increase in regions where smaller uncertainty is required to proceed safely. As a result, these regions act as bottlenecks, slowing down the process and potentially stopping exploration within the connected component that satisfies the constraints and includes the initial safe control. Additional results on information gain across iterations are provided in Appendix C.2.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Safety and reset level prediction", "weight": 1.0} -->

In Table, we quantify the accuracy of the learned model for various threshold pairs $\varepsilon = \xi$ in $\{ 0.1,\, 0.3,\, 0.5,{+ \infty}\}$ by evaluating the prediction quality of the safety and reset levels over 1000 predictions. We report the mean squared error (MSE) and the standard deviation, with the ground truth provided by Monte Carlo estimates based on 100 samples. In Figure, we plot the learned safety and reset maps, whose accuracies can be qualitatively assessed by comparing their values with those in Figure. As expected, prediction accuracy improves as safety constraints are relaxed, due to the broader coverage of the control space.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Dynamics prediction", "weight": 1.0} -->

To verify that our method captures the underlying system dynamics, we compare predicted trajectory densities with ground-truth trajectories under known-safe controls. Qualitative results show close agreement in both mean and variance. Full visualizations and evaluation details are provided in Appendix C.1.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Computational considerations", "weight": 1.0} -->

Our method runs end-to-end in under 32 minutes on standard hardware, covering candidate selection, simulation, evaluation, and model updates. Appendix B.4 provides runtimes, hardware specs, and potential optimizations (e.g., sketching, parallelization), confirming the method's practicality on standard hardware.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced a provably safe and efficient method for learning controlled stochastic dynamics from trajectory data. By leveraging kernel-based confidence bounds and smoothness assumptions, our method incrementally expands an initial safe control set, ensuring that all trajectories remain within predefined safety regions throughout the learning process. Theoretical guarantees were established for both safety and estimation accuracy, with learning rates that adapt to the Sobolev regularity of the true dynamics. Numerical experiments corroborate our theoretical findings regarding safety and estimation accuracy. By tuning the safety ($\varepsilon$) and reset ($\xi$) thresholds, users can explicitly control the trade-off between conservative safety satisfaction and exploratory behavior. While our experimental validation focuses on a low-dimensional setting, the theoretical results scale with dimension: the convergence rates for the proposed estimators decrease polynomially with dimension and can mitigate the curse of dimensionality under sufficient smoothness. This makes the method applicable to higher-dimensional systems, which we plan to investigate in future work.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Further research will include validation on physical systems (e.g., autonomous robots), improved scalability through fast kernel methods (e.g., sketching or incremental updates), comparisons with safe RL baselines, systematic analyses of kernel and threshold selection, and extensions to handle abrupt dynamics and non-diffusive disturbances such as jump processes arising in pedestrian--vehicle interactions and hybrid systems. These developments will further support applications in safety-critical control and decision-making under uncertainty.
