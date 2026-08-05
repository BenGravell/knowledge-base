<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We establish finite-sample closed-loop stability guarantees for Model Predictive Path Integral (MPPI) control applied to discrete-time Linear Time-Invariant (LTI) systems with additive Gaussian process disturbances. The key observation is that, for unconstrained LTI/quadratic systems with the DARE terminal cost, the exact finite-horizon MPC law has the same first control action as the infinite-horizon LQR law for every planning horizon. Thus, finite-sample MPPI can be analyzed as a stochastic perturbation of LQR. First, we show that the MPPI control law approximates the LQR feedback with high probability. The approximation error decomposes into a Monte Carlo term that decreases with the sample count and an infinite-sample temperature bias that persists at finite temperature but vanishes as the temperature is reduced. The resulting constants are written in terms of the horizon-dependent stacked cost matrices, making explicit that the finite-sample certificate is parametrized by the selected planning horizon. Second, we use a Lyapunov perturbation argument to prove practical exponential stability in expectation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

On sample paths that remain in a compact Lyapunov sublevel set over a finite operating horizon, the expected state norm decays exponentially up to three residual floors: a process-noise floor, an MPPI approximation floor, and a confidence floor from the per-step sampling failure probability. The sufficient sample threshold is explicit and computable from the DARE solution, LQR stability margin, MPPI sampling parameters, temperature, and planning horizon. In the joint limit of infinite samples and vanishing temperature bias, the result recovers the stochastic LQR stability bound.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model Predictive Path Integral (MPPI) control is a sampling-based receding-horizon method that has achieved strong empirical performance across robotics and autonomous systems, including off-road navigation, legged locomotion, and aerial vehicles. Its central appeal is that it requires no gradient of the cost or dynamics: at each time step it draws $M$ random control perturbations, rolls them out in parallel (GPU-accelerated), and forms an importance-weighted average that approximates the information-theoretic optimal. This gradient-free, massively parallel structure makes MPPI uniquely attractive for nonlinear and non-smooth problems where classical gradient-based MPC solvers struggle.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite a growing body of work on MPPI theory, the question of *closed-loop stability* under receding-horizon execution remains largely unresolved. In particular, it is unclear under what conditions the state $x_{k}$ remains bounded and converges when MPPI is implemented with a finite sample count $M$ and subjected to persistent process disturbances. This is not merely an academic concern: without stability guarantees, practitioners cannot reason systematically about how many samples are sufficient or how performance degrades as $M$ decreases. The difficulty is that finite-sample approximation errors arise at every control update and interact with stochastic disturbances over the horizon, making one-step optimization guarantees insufficient for establishing long-term closed-loop behavior.

<!-- chunk {"id": "body-0006", "role": "body", "section": "I-A Prior Work and the Remaining Gap", "weight": 1.0} -->

MPPI foundations. The original MPPI derivation frames control as minimization of a KL-divergence between a controlled and an uncontrolled trajectory distribution, with the importance-weighted update arising as the solution to this information-theoretic problem. Williams et al. extend this to a full information-theoretic MPC framework. Wagener et al. unify sampling-based MPC methods through online learning with Bregman divergences.

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-A Prior Work and the Remaining Gap", "weight": 1.0} -->

Approximation error and optimizer convergence. Yoon et al. established open-loop $O(M^{-1/2})$ sampling-complexity bounds for Monte Carlo estimates of the path-integral optimal control, laying the groundwork for quantitative convergence analysis. Yi et al. provide the first convergence analysis of MPPI as an optimizer, showing that the importance-weighted update contracts toward the optimal control sequence at a linear rate for quadratic costs and characterizing the contraction rate as a function of the sampling covariance $\Sigma_{\epsilon}$ and temperature $\lambda$. Homburger et al. study optimality gaps in deterministic and stochastic MPPI. Fazlyab et al. interpret MPPI as preconditioned gradient descent on a KL-regularized free-energy objective, connecting information-theoretic control to first-order optimization. Collectively, these works establish increasingly strong guarantees on the optimization step performed by MPPI, but they do not address the stability of the resulting receding-horizon closed-loop system.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A Prior Work and the Remaining Gap", "weight": 1.0} -->

Robust MPPI and performance bounds. Gandhi et al. propose a Robust MPPI architecture with an augmented nominal--actual state representation and derive a bound on free-energy growth as a function of constraint violation level, tracking controller performance, and sampling error. This gives a performance certificate for a specific architecture but does not constitute a Lyapunov-based closed-loop stability proof.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-A Prior Work and the Remaining Gap", "weight": 1.0} -->

Contraction theory and CLF-based MPC. Lohmiller and Slotine establish contraction theory as a framework for global convergence: any two trajectories contract at a uniform exponential rate, independently of initial conditions. Manchester and Slotine develop Control Contraction Metrics (CCMs) that provide constructive synthesis conditions for contracting feedback policies. Mayne et al. provide the classical MPC stability framework based on a CLF terminal cost and a terminal invariant set; we replace the terminal set requirement with a global CLF, removing the need for a terminal constraint set altogether.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-A Prior Work and the Remaining Gap", "weight": 1.0} -->

The open problem. A recent survey by Honda identifies closed-loop stability of path-integral MPC as a major open problem. Optimizer convergence and closed-loop stability address fundamentally different questions: the former asks whether a single MPPI planning step produces a good control update for a fixed state, whereas the latter asks whether the state trajectory generated by repeated receding-horizon execution remains bounded over time. This paper addresses this gap for the LTI/quadratic setting by combining finite-sample MPPI approximation bounds with a Lyapunov perturbation argument.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

This paper provides, to the best of our knowledge, the first closed-loop stability certificate for MPPI on LTI systems. Specifically: Finite-sample approximation bound (Lemma 3. ‣ III-A Finite-Sample Approximation of the Infinite-Sample MPPI Update ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems")): We decompose the MPPI approximation error into two components: a finite-sample Monte Carlo error bounded by $\varepsilon_{M}(\eta)=O(M^{-1/2})$ with probability at least $1-\eta$, and an infinite-sample temperature bias $b_{\infty}(x_{k},\bar{U})$ that persists as $M\to\infty$. The bias is characterized in closed form via the bias gain $\kappa_{\lambda}$ (Proposition 1.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

‣ III-A Finite-Sample Approximation of the Infinite-Sample MPPI Update ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems")) and vanishes as $\lambda\to 0$. This two-component decomposition is the finite-$M$ statement that CoVO-MPC leaves open.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

Exponential stability in expectation (Theorem 1. ‣ III-C Closed-Loop Practical Stability ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems")): The stopped process satisfies an unconditional Lyapunov bound for all $k\geq 0$. On sample paths satisfying $\tau_{R}>T$, which occur with probability at least $1-\delta$, the unstopped process satisfies (36. ‣ III-C Closed-Loop Practical Stability ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems")) for all $0\leq k\leq T$ and all $M\geq M^{*}$, Explicit sample threshold (Corollary 1.

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

‣ III-E Explicit Sample Requirement ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems")): in terms of the LQR stability margin $\alpha_{P}$, system dimensions, and confidence level $1-\eta$, computable from the DARE solution.

<!-- chunk {"id": "body-0015", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

ISS interpretation (Proposition 2. ‣ III-D ISS Interpretation ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems")): The main bound is recast as a practical Input-to-State Stability estimate with three explicit gains connecting the result to the ISS framework standard in robust MPC.

<!-- chunk {"id": "body-0016", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

The key technical ideas are threefold. First, finite-sample MPPI is interpreted as a perturbation of LQR with magnitude $O(M^{-1/2})$, decomposed into a Monte Carlo component and a temperature-bias component. Second, a Gaussian completing-the-square argument characterizes the infinite-sample bias in closed form via $\kappa_{\lambda}\to 0$ as $\lambda\to 0$. Third, high-probability invariance of the Lyapunov sublevel set $\Omega_{R}$ is established via a supermartingale argument (Lemma 5. ‣ III-C Closed-Loop Practical Stability ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems")), resolving the circularity between the compact-set assumption and the concentration bounds. Embedding these ingredients within the classical MPC stability framework of Mayne et al. yields explicit stability and sample-complexity guarantees. In the limit $M\to\infty$, the result recovers the standard stochastic LQR stability certificate.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

At each time step, MPPI approximately solves the finite-horizon optimal control problem | | $\displaystyle J(x_{k},U)$ | $\displaystyle=\sum_{i=0}^{N-1}\left(x_{k+i}^{\top}Qx_{k+i}+u_{k+i}^{\top}Ru_{k+i}\right)$ | | \(2\) | where $U=\{u_{k},\ldots,u_{k+N-1}\}$, $Q\succeq 0$, $R\succ 0$, and $P\succ 0$ is the stabilizing solution of the DARE. For unconstrained linear-quadratic systems, this choice embeds the infinite-horizon cost-to-go beyond the prediction horizon, causing the finite-horizon optimum to coincide with the LQR feedback law and providing the Lyapunov structure used in classical MPC stability analysis.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The MPPI control update is where $\epsilon_{i}^{(j)}\sim\mathcal{N}(0,\Sigma_{\epsilon})$ are i.i.d. sampling perturbations and The applied control is the first element $u_{k}=u_{0}^{\mathrm{MPPI}}$, and the nominal sequence $\bar{U}$ is updated according to the standard receding-horizon shift.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The corresponding infinite-horizon LQR problem is whose optimal controller is where $P\succ 0$ satisfies the DARE Under standard stabilizability and detectability assumptions, $A_{\mathrm{cl}}:=A-BK$ is Schur stable and $V(x)=x^{\top}Px$ satisfies where $\alpha_{P}:=\lambda_{\min}(Q+K^{\top}RK)>0$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Since the finite-horizon optimum coincides with the LQR solution under the above construction, the central question becomes how closely the finite-sample MPPI update tracks this optimum.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Assumptions 1. ‣ II Problem Formulation ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems")--2. ‣ II Problem Formulation ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems") are the minimal conditions under which the DARE has a unique positive-definite solution. If $Q\succ 0$, detectability is automatic.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 3 (DARE Terminal Cost)", "weight": 1.0} -->

The terminal cost $P$ in is the unique positive-definite solution to the DARE.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 3 (DARE Terminal Cost)", "weight": 1.0} -->

This choice is canonical: $P$ is simultaneously the LQR optimal cost-to-go and the unique matrix satisfying the CLF decrease condition, which is the terminal cost condition required by the Mayne et al. framework. Crucially, it also ensures that the finite-horizon optimum of $J(x_{k},U)$ coincides exactly with the infinite-horizon LQR solution $u_{k}^{\mathrm{LQR}}=-Kx_{k}$ for any planning horizon $N\geq 1$, eliminating any horizon-truncation contribution to the approximation error.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 4 (MPPI Sampling)", "weight": 1.0} -->

MPPI draws $M$ i.i.d. perturbation sequences $\epsilon_{i}^{(j)}\sim\mathcal{N}(0,\Sigma_{\epsilon})$, $\Sigma_{\epsilon}\succ 0$, independent across time steps.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 5 (Bounded Warm-Start Map)", "weight": 1.0} -->

The MPPI nominal sequence is updated by a measurable warm-start map where $\mathcal{S}:\mathbb{R}^{mN}\to\mathbb{R}^{mN}$ is the receding-horizon shift operator, $\mathcal{U}_{N}\subset\mathbb{R}^{mN}$ is a compact set with diameter $D_{\mathcal{U}}<\infty$, and $\Pi_{\mathcal{U}_{N}}$ denotes projection onto $\mathcal{U}_{N}$. The projection may be implemented by clipping, saturation, or any bounded warm-start rule, and guarantees $\bar{U}_{k}\in\mathcal{U}_{N}$ for all $k\geq 0$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Assumption 5. ‣ II Problem Formulation ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems") serves two purposes: it guarantees $\|\bar{U}_{k}\|\leq D_{\mathcal{U}}$ for all $k$, which bounds the bias coefficients $\beta_{0}$ in Definition 1. ‣ III-C Closed-Loop Practical Stability ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems") and the bad-event constant $C_{\mathrm{bad}}$; and it provides the compact domain $\mathcal{U}_{N}$ over which the uniform lower bound $\underline{Z}$ in Lemma 1. ‣ III-A Finite-Sample Approximation of the Infinite-Sample MPPI Update ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems") is attained.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 6 (Bounded MPPI Update)", "weight": 1.0} -->

The implemented MPPI control satisfies almost surely for some constant $\bar{u}$. This is enforced in practice by actuator saturation, truncated Gaussian sampling of $\epsilon_{i}^{(j)}$, or the projection $\Pi_{\mathcal{U}_{N}}$ of Assumption 5. ‣ II Problem Formulation ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems"), all of which bound the applied control almost surely.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Assumption 6. ‣ II Problem Formulation ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems") is required to make the bad-event Lyapunov bound mathematically clean. Without it, Gaussian perturbations are unbounded and the step $\mathbb{E}[\tilde{V}_{k+1}\mathbf{1}_{\mathcal{G}_{k}^{c}}\mid\mathcal{F}_{k}]\leq C_{\mathrm{bad}}\eta$ would require a Cauchy--Schwarz argument yielding a $\sqrt{\eta}$ rather than $\eta$ residual at the Lyapunov level. Assumption 6. ‣ II Problem Formulation ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems") is satisfied by every practical MPPI implementation that clips perturbations or saturates the applied control.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Main Results", "weight": 1.0} -->

This section establishes that finite-sample MPPI is a stochastic approximation of the corresponding infinite-sample MPPI update. The difference between infinite-sample MPPI and LQR appears explicitly as a bias term. Stability follows whenever this bias and the finite-sample error are small enough relative to the LQR Lyapunov decrease margin.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A Finite-Sample Approximation of the Infinite-Sample MPPI Update", "weight": 1.0} -->

For a state $x_{k}$ and nominal control sequence $\bar{U}\in\mathbb{R}^{mN}$, let $\mathcal{E}\sim\mathcal{N}(0,I_{N}\otimes\Sigma_{\epsilon})$ denote the stacked MPPI perturbation sequence and let $\epsilon_{0}\in\mathbb{R}^{m}$ denote its first control block. Define the unnormalized MPPI weight The infinite-sample MPPI perturbation mean is and the corresponding infinite-sample MPPI control is $u_{k}^{\infty}:=\bar{u}_{0}+\mu_{\infty}(x_{k},\bar{U})$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 5 (Role of the Planning Horizon)", "weight": 1.0} -->

Under Assumption 3. ‣ II Problem Formulation ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems"), the deterministic finite-horizon optimizer has the same first control component as the infinite-horizon LQR law for every horizon $N\geq 1$. In particular, if $U_{N}^{*}(x)$ denotes the $N$-step optimal control sequence for the cost, then its first block satisfies $[U_{N}^{*}(x)]_{0}=-Kx=u_{k}^{\mathrm{LQR}}$ independently of $N$. Thus the DARE terminal cost removes any horizon-truncation error in the nominal optimal feedback law.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 5 (Role of the Planning Horizon)", "weight": 1.0} -->

This does not imply that the finite-sample MPPI certificate is independent of $N$. The stacked Hessian $H_{N}$, the linear term $F_{N}$, the sampling dimension $mN$, the compact warm-start set $\mathcal{U}_{N}$, and the concentration constant $C_{\mathcal{X},\mathcal{U}}$ generally depend on the planning horizon. Consequently, the bias coefficients $\beta_{\infty}$, $\beta_{0}$, the finite-sample error $\varepsilon_{M}(\eta)$, and the sufficient sample threshold $M^{*}$ may depend on $N$. The horizon-independent part of the result is the nominal LQR feedback recovered by the exact finite-horizon optimizer, not the MPPI sample complexity.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-C Closed-Loop Practical Stability", "weight": 1.0} -->

Write $u_{k}^{\mathrm{MPPI}}=u_{k}^{\mathrm{LQR}}+d_{k}$ where $d_{k}:=u_{k}^{\mathrm{MPPI}}-u_{k}^{\mathrm{LQR}}$. By Lemma 3. ‣ III-A Finite-Sample Approximation of the Infinite-Sample MPPI Update ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems"), with probability at least $1-\eta$, $\|d_{k}\|\leq b_{\infty}(x_{k},\bar{U}_{k})+\varepsilon_{M}(\eta)$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-C Closed-Loop Practical Stability", "weight": 1.0} -->

Fix a Lyapunov sublevel set where $R$ will be chosen in Lemma 5. ‣ III-C Closed-Loop Practical Stability ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems") to guarantee trajectories remain in $\Omega_{R}$ with probability at least $1-\delta$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 7", "weight": 1.0} -->

Lemma 5. ‣ III-C Closed-Loop Practical Stability ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems") resolves the circularity in the compact-set argument: the concentration bounds of Lemmas 1. ‣ III-A Finite-Sample Approximation of the Infinite-Sample MPPI Update ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems")--3. ‣ III-A Finite-Sample Approximation of the Infinite-Sample MPPI Update ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems") require $x_{k}\in\Omega_{R}$ almost surely, but forward invariance in expectation alone does not guarantee this. By choosing $R$ according to (30.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 7", "weight": 1.0} -->

‣ III-C Closed-Loop Practical Stability ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems")), $x_{k}\in\Omega_{R}$ for all $0\leq k\leq T$ with probability at least $1-\delta$, so the concentration bounds hold on this event over the finite horizon $T$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 8 (Recovery of the LQR Limit)", "weight": 1.0} -->

If $\bar{U}=U^{*}$ at every step (Proposition 1. ‣ III-A Finite-Sample Approximation of the Infinite-Sample MPPI Update ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems") Part 1), then $\kappa_{\lambda}=0$, $\beta_{\infty}=\beta_{0}=0$, and $e_{M}(\eta)=\varepsilon_{M}(\eta)\to 0$ as $M\to\infty$. The bound converges to the stochastic LQR bound. If $\kappa_{\lambda}>0$, increasing $M$ removes only the Monte Carlo error $\varepsilon_{M}(\eta)$; the residual $\beta_{0}=\kappa_{\lambda}D_{\mathcal{U}}$ is the irreducible temperature-smoothing bias.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 9", "weight": 1.0} -->

The bound (38. ‣ III-D ISS Interpretation ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems")) decomposes into three floors: (i) $\gamma_{w}\sqrt{\mathrm{tr}(\Sigma_{w})}$ is the process-noise floor, unavoidable under persistent Gaussian disturbances; (ii) $\gamma_{M}e_{M}(\eta)$ is the MPPI approximation floor, containing both the temperature bias $\beta_{0}=\kappa_{\lambda}D_{\mathcal{U}}$ and the Monte Carlo error $\varepsilon_{M}(\eta)$ --- only the latter vanishes as $M\to\infty$; (iii) $\gamma_{\eta}\sqrt{\eta}$ is the confidence floor from the per-step good-event failure probability.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 9", "weight": 1.0} -->

The localization event $\{\tau_{R}>T\}$ has probability at least $1-\delta$ for any chosen $T$, $\delta$, and $R$ satisfying Lemma 5. ‣ III-C Closed-Loop Practical Stability ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems"). By taking $T$ large and $\delta$ small, the certificate covers any operationally relevant horizon at any desired confidence level.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 10 (Bounded Noise and Infinite-Horizon Invariance)", "weight": 1.0} -->

The finite-horizon localization $\{\tau_{R}>T\}$ in Theorem 1. ‣ III-C Closed-Loop Practical Stability ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems") is not an artifact of the proof technique but reflects a fundamental property of unbounded Gaussian noise: for any fixed bounded set $\Omega_{R}$, persistent $\mathcal{N}(0,\Sigma_{w})$ disturbances guarantee $\mathbb{P}(\tau_{R}<\infty)=1$, so the infinite-horizon event $\{\tau_{R}=\infty\}$ has probability zero regardless of $M$ or the stability margin. The finite-horizon framework adopted here is therefore the honest statement under Gaussian process noise, and it matches the structure of the companion nonlinear paper exactly.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 10 (Bounded Noise and Infinite-Horizon Invariance)", "weight": 1.0} -->

If the process noise is bounded almost surely, for example by using a truncated or clipped Gaussian $w_{k}\sim\mathcal{N}(0,\Sigma_{w})$ conditioned on $\|w_{k}\|\leq w_{\max}$, then the infinite-horizon claim $\mathbb{P}(\tau_{R}<\infty)\leq\delta$ becomes achievable. Under bounded noise, a single disturbance realization cannot exit $\Omega_{R}$ in one step when $R$ is chosen sufficiently large relative to $w_{\max}$, so the passage $k\to\infty$ in the supermartingale argument is valid and Lemma 5. ‣ III-C Closed-Loop Practical Stability ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems") upgrades to $\mathbb{P}(\tau_{R}\leq T)\leq\delta$ for all $T$ simultaneously.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 10 (Bounded Noise and Infinite-Horizon Invariance)", "weight": 1.0} -->

Extending the present framework to bounded noise models, and characterizing the approximation gap between clipped and true Gaussian noise in terms of the truncation parameter $w_{\max}$, is left as future work.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-A Setup", "weight": 1.0} -->

We benchmark on the double-integrator This is the 2-state position--velocity subsystem of the 4-state UAV double-integrator used in Section IV-A of, specialized to the obstacle-free quadratic-cost case with the DARE terminal cost used in the present theory. The simulation infrastructure from is reused and extended with receding-horizon execution and the closed-loop stability diagnostics described below. All simulations are GPU-accelerated via PyTorch on an NVIDIA GeForce RTX 4060. Simulation code is publicly available at The DARE yields giving closed-loop eigenvalues approximately $\{0.3616,0.0928\}$ and spectral radius $\rho(A_{\mathrm{cl}})\approx 0.3616$. The process noise is $\Sigma_{w}=\sigma_{w}^{2}I_{2}$ with $\sigma_{w}\in\{0.05,0.10,0.20\}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-A Setup", "weight": 1.0} -->

The MPPI parameters are horizon $N=10$, temperature $\lambda=1.0$, and isotropic Gaussian perturbations $\epsilon\sim\mathcal{N}(0,I_{mN})$. Since the input is scalar, $m=1$. Unless otherwise stated, the initial condition is $x_{0}=^{\top}$ and Monte Carlo averages are computed over 300 closed-loop trials.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-A Setup", "weight": 1.0} -->

The numerical sample threshold is computed from Corollary 1. ‣ III-E Explicit Sample Requirement ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems") using the benchmark constant $C_{1}=0.22$, giving $M^{*}=153$ at confidence parameter $\eta=0.05$. This value is the analytical certificate threshold for this benchmark, not a universal MPPI constant.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-B Analytical Parameter Summary", "weight": 1.0} -->

Table I records the theoretical quantities computed from the DARE solution and used for comparison with simulation. $\sqrt{\lambda_{\max}(P)/\lambda_{\min}(P)}$ TABLE I: Analytical stability parameters for the double integrator.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-B Analytical Parameter Summary", "weight": 1.0} -->

The certificate decay rate $\rho=0.943$ is substantially looser than the LQR spectral radius $\rho_{\mathrm{LQR}}=0.362$, a gap of approximately $2.6\times$. This is expected: the proof uses worst-case perturbation bounds and norm inequalities to obtain a closed-form guarantee. The experiments below test whether the certified threshold $M^{*}$ is qualitatively consistent with the empirically observed onset of stable behavior.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-C Experiment 1: Bound Envelope and Closed-Loop Response", "weight": 1.0} -->

The cases $M=200$ and $M=1000$ satisfy $M\geq M^{*}=153$ and fall within the analytical certificate; $M=50<M^{*}$ is an uncertified comparison. The plotted envelope includes the nominal exponential decay term and the process-noise floor, but not an explicitly calibrated finite-sample MPPI approximation floor. Therefore Fig. 1 should be interpreted as a qualitative comparison of decay behavior rather than as a direct numerical verification of the full bound in Theorem 1. ‣ III-C Closed-Loop Practical Stability ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems"). The empirical trajectories decay rapidly and remain bounded for the certified sample counts, while their steady-state levels are dominated by finite-$M$ approximation effects and process noise. This behavior is consistent with the theorem, whose full residual contains both the process-noise floor and the MPPI approximation floor.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-D Experiment 2: Empirical Decay Rate vs. Sample Count", "weight": 1.0} -->

For each $M\in\{10,20,50,100,200,500,1000,5000,10^{4}\}$, we estimate an empirical decay factor $\hat{\rho}(M)$ from 300 noise-free closed-loop trajectories using the median Lyapunov ratio $V(x_{k+1})/V(x_{k})$ over the initial transient. The median is preferred over log-linear fitting on mean norms because the latter hits the floating-point noise floor before the transient fully decays at fast spectral radii. Results are shown in Fig. 2.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-D Experiment 2: Empirical Decay Rate vs. Sample Count", "weight": 1.0} -->

At $M=10$ and $M=20$ the system is unstable ($\hat{\rho}>1$); at $M=50$ it is marginally stable ($\hat{\rho}=0.995$) but uncertified. At $M=200$, the first sweep point satisfying $M\geq M^{*}$, $\hat{\rho}=0.939\leq\rho=0.943$, confirming the certificate. For all $M\geq M^{*}$ in the sweep, $\hat{\rho}\leq\rho$, with values $\{0.939,0.929,0.886,0.821,0.755\}$ at $M\in\{200,500,1000,5000,10^{4}\}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-D Experiment 2: Empirical Decay Rate vs. Sample Count", "weight": 1.0} -->

The rate improves monotonically, approaching but not reaching $\rho_{\mathrm{LQR}}=0.362$ because the finite-temperature Gibbs-weighted update is not the exact deterministic LQR law.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-E Experiment 3: Phase Portrait", "weight": 1.0} -->

Fig. 3 plots 30 sample trajectories in the $(x_{1},x_{2})$ plane for $M=50$ (uncertified) and $M=500$ (certified) at $\sigma_{w}=0.1$ over $T=35$ steps, with the LQR $2\sigma$ steady-state ellipse (axes $0.14\times 0.29$) overlaid.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-E Experiment 3: Phase Portrait", "weight": 1.0} -->

Trajectories under $M=500$ concentrate near the origin with mean terminal norm $0.92$, while those under $M=50$ remain more dispersed with mean terminal norm $1.65$. No divergence ($\|x_{T}\|>5$) occurs in either case, confirming that below-certificate behavior is uncertified, not necessarily unstable.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-F Experiment 4: Analytical vs. Empirical $M^{*}$", "weight": 1.0} -->

Table II and Fig. 4 compare the analytical threshold $M^{*}=153$ from Corollary 1. ‣ III-E Explicit Sample Requirement ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems") with an empirical threshold $\hat{M}^{*}$, defined as the smallest tested sample count for which the noise-free decay diagnostic satisfies $\hat{\rho}(M)<0.99$. This criterion is empirical and should not be confused with the sufficient condition in the theorem.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-F Experiment 4: Analytical vs. Empirical $M^{*}$", "weight": 1.0} -->

The empirical threshold $\hat{M}^{*}=30$ is approximately $5\times$ smaller than the analytical threshold and is independent of $\sigma_{w}$ across all tested noise levels. The $\sigma_{w}$-independence is consistent with the structure of Corollary 1. ‣ III-E Explicit Sample Requirement ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems"): the sufficient sample count controls whether the MPPI approximation error is absorbed by the nominal Lyapunov decay, a condition that depends on the control-approximation quality rather than directly on the process noise, which affects only the residual steady-state level.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-F Experiment 4: Analytical vs. Empirical $M^{*}$", "weight": 1.0} -->

The $5\times$ gap between $M^{*}$ and $\hat{M}^{*}$ reflects the expected conservatism of a worst-case Lyapunov certificate relative to an average-case Monte Carlo diagnostic. Worst-case Young's inequality steps in the proof consume half the Lyapunov margin as slack, and the concentration constant $C_{1}=0.22$ is calibrated conservatively for the maximum-over-$k$ guarantee rather than the typical single-step behavior. This level of conservatism is standard for Lyapunov-based stochastic stability certificates.

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-G Experiment 5: ESS as a Diagnostic", "weight": 1.0} -->

For $M=500$ and $\sigma_{w}=0.1$, Fig. 5 tracks the online effective sample size alongside $\|x_{k}\|$ over $T=200$ steps.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-G Experiment 5: ESS as a Diagnostic", "weight": 1.0} -->

The mean normalized ESS is $\mathrm{ESS}_{k}/M\approx 0.003$. This low value is normal for MPPI: importance weights intentionally concentrate on low-cost trajectories, so $\mathrm{ESS}/M$ of order $10^{-3}$--$10^{-2}$ is typical in practice. The more informative signal is the *relative* variation of ESS over time: transient drops in ESS correlate with high-cost regions or poor alignment of the sampling distribution with locally useful control directions, not with instability per se.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-G Experiment 5: ESS as a Diagnostic", "weight": 1.0} -->

The theoretical threshold $M^{*}/M=153/500=0.306$ is never met in this run, yet the trajectory converges stably. This confirms that $M^{*}$ is a sufficient certificate threshold, not a necessary condition, and ESS is a qualitative sampling-quality diagnostic rather than a binary stability indicator.

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-H Discussion of Results", "weight": 1.0} -->

The experiments support three conclusions.

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-H Discussion of Results", "weight": 1.0} -->

Sufficiency, not necessity. The analytical threshold $M^{*}$ is a sufficient certificate, not a sharp phase-transition boundary. For $M\geq M^{*}$, the certified decay bound $\hat{\rho}\leq\rho=0.943$ holds in all tested cases. For $M<M^{*}$, the theorem makes no stability claim; empirical convergence for $M$ as small as $30$ simply indicates that the certificate is conservative.

<!-- chunk {"id": "body-0062", "role": "body", "section": "IV-H Discussion of Results", "weight": 1.0} -->

Expected conservatism of the decay bound. The certificate gives $\rho=0.943$, approximately $2.6\times$ looser than $\rho_{\mathrm{LQR}}=0.362$, a standard consequence of worst-case norm inequalities in Lyapunov-based certificates for sampling-based controllers.

<!-- chunk {"id": "body-0063", "role": "body", "section": "IV-H Discussion of Results", "weight": 1.0} -->

Conservatism of the sample threshold. The analytical threshold $M^{*}=153$ is approximately $5\times$ larger than the empirically sufficient $\hat{M}^{*}=30$. This gap is not a failure of the theorem but an inherent feature of worst-case analysis: the certificate must hold for all LTI systems satisfying the given parameters, whereas the diagnostic measures only the typical behavior of this specific benchmark. Tighter constants---via improved concentration inequalities or problem-specific calibration of $C_{1}$---could close this gap at the cost of a less broadly applicable bound.

<!-- chunk {"id": "body-0064", "role": "body", "section": "IV-H Discussion of Results", "weight": 1.0} -->

Overall, the simulation study validates the qualitative message of Theorem 1. ‣ III-C Closed-Loop Practical Stability ‣ III Main Results ‣ Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems"): sufficiently many MPPI samples produce certified LQR-like closed-loop stability, and the explicit threshold $M^{*}$ is conservative but computable and practically informative.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper established a finite-sample closed-loop stability certificate for MPPI applied to discrete-time LTI systems with quadratic costs and additive Gaussian process noise. The analysis exploits a special structure of the unconstrained LTI/quadratic setting: with the DARE terminal cost, the exact finite-horizon MPC optimizer has the same first control action as the infinite-horizon LQR law for every planning horizon. Hence, for a fixed horizon $N$, MPPI can be analyzed as a finite-sample stochastic perturbation of the LQR feedback.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The main result shows that, when the MPPI sample count is sufficiently large, the closed loop satisfies a practical exponential stability bound of the form The three residual terms correspond to process noise, finite-sample and finite-temperature MPPI approximation error, and the confidence loss from the per-step sampling failure probability. The sufficient sample threshold is explicit and computable from the DARE solution, the LQR stability margin, the input matrix, the MPPI sampling parameters, and the selected planning horizon.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The proof combines a high-probability finite-sample MPPI approximation bound with a Lyapunov perturbation argument. Once the MPPI approximation error is below the Lyapunov stability margin, the nominal LQR decrease absorbs the sampling-induced perturbation, while the additive Gaussian disturbance produces a residual noise floor. The result therefore connects sampling-based MPPI with classical MPC stability theory and provides a first LTI/quadratic setting in which finite-sample MPPI admits an explicit closed-loop stability certificate.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Future Work", "weight": 1.5} -->

Several extensions remain open. First, the present result is stated for the unconstrained LTI/quadratic case. Extending the theory to constrained MPC would require replacing the LQR baseline with a stabilizing constrained MPC law, together with recursive feasibility, terminal-set, and constraint-satisfaction assumptions. Because Gaussian process noise can violate hard constraints with nonzero probability, constrained stochastic MPPI also requires a separate treatment of safety, feasibility, and chance or tube-based constraint satisfaction.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Future Work", "weight": 1.5} -->

Second, the certificate is horizon-parametrized. The exact deterministic first action is independent of the planning horizon because of the DARE terminal cost, but the MPPI approximation constants generally depend on the stacked horizon-$N$ cost matrices, sampling covariance, and warm-start set. Obtaining uniform-in-horizon sample-complexity bounds would require additional structural estimates on these horizon-dependent quantities.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Future Work", "weight": 1.5} -->

Third, this paper treats the LTI foundation case. Companion work extends the stability framework to nonlinear systems using contraction-theoretic and CLF-based arguments, and to adaptive noise covariance estimation, where closed-loop data are used to improve the estimate of $\Sigma_{w}$ and tighten the residual noise-floor term.
