<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Residual-Conservative Model Predictive Path Integral Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sampling-based model predictive control methods handle nonlinear dynamics and complex cost landscapes through Monte Carlo rollouts, yet typically employ fixed constraint penalties that do not adapt to model-plant mismatch. This paper proposes Residual-Conservative Model Predictive Path Integral Control (RC-MPPI), a sampling-based MPC framework that modulates safety conservatism online using the prediction-execution residual. RC-MPPI combines three coupled mechanisms: residual-dependent constraint tightening, adaptive safety-cost shaping, and residual-adaptive sampling modulation through exploration contraction and temperature relaxation. The temperature adaptation reflects a key insight: when the model is inaccurate, rollout cost evaluations become unreliable, and increasing temperature reduces overcommitment to apparent cost rankings. Under Lipschitz dynamics and sub-Gaussian disturbances, we derive probabilistic bounds on constraint violation and show that the joint effect of the adaptive mechanisms reduces violation probability as the residual grows. A rollout-cost uncertainty analysis further shows that model-plant mismatch perturbs MPPI importance weights in proportion to residual magnitude and inversely with temperature, providing theoretical justification for residual-adaptive temperature relaxation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Simulations on an LTI point-mass system and a planar 2R manipulator show improved safety margin, success rate, and control efficiency compared with vanilla MPPI under significant model-plant mismatch.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Low-cost robotic and embedded control platforms frequently exhibit execution variability arising from actuation lag, saturation, unmodeled inner-loop dynamics, and limited sensing fidelity. When high-level planners rely on simplified or nominal actuator models, such effects induce model-plant mismatch that can compromise constraint satisfaction. In receding-horizon implementations, this mismatch is persistent and state-dependent rather than a one-time disturbance.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Sampling-based model predictive control methods, such as Model Predictive Path Integral (MPPI) control, handle nonlinear dynamics and complex cost landscapes through Monte Carlo rollouts and importance weighting. However, standard formulations assume a fixed nominal model and employ static constraint penalties or barrier functions that do not adapt to model-plant mismatch. When model-plant mismatch grows, fixed safety mechanisms may become insufficient.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper addresses the problem of online conservatism adaptation under model-plant mismatch. Rather than performing real-time parameter identification or maintaining a full disturbance belief, we exploit the prediction--execution residual, the directly measurable discrepancy between predicted and realized state transitions, as a lightweight signal of model-plant mismatch, and embed it into the sampling-based MPC objective via three coupled adaptive mechanisms.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The resulting method, Residual-Conservative MPPI (RC-MPPI), enforces safety through residual-dependent constraint tightening and amplified penalty scaling, while the MPPI temperature is *relaxed* in proportion to the observed prediction--execution residual. Standard MPPI treats temperature as a fixed exploration parameter; under model-plant mismatch, however, this conflates genuine cost differences with artifacts of an inaccurate model. RC-MPPI instead treats temperature as an epistemic parameter encoding confidence in rollout cost evaluations. We show that the $\ell_{1}$ deviation between true and nominal importance weights is bounded by $2C_{\Delta}\bar{s}_{k}/\beta_{k}$, where $C_{\Delta}$ captures cost sensitivity to model-plant mismatch and $\bar{s}_{k}$ is the filtered residual. Since this bound grows with mismatch and shrinks with temperature, raising $\beta_{k}$ as $\bar{s}_{k}$ increases directly limits the distortion of MPPI weights by corrupted rollout cost rankings.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

RC-MPPI, a sampling-based MPC scheme with three coupled residual-adaptive mechanisms: constraint tightening, penalty scaling, and residual-adaptive sampling modulation comprising temperature relaxation and exploration contraction, with no additional computational cost over standard MPPI. Temperature is treated as an epistemic parameter encoding confidence in rollout cost evaluations under model-plant mismatch.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

A probabilistic safety analysis grounded in an $N$-step horizon prediction error bound (Theorem 1. ‣ III-A Residual Estimation ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control")), establishing that the joint effect of all three mechanisms monotonically reduces constraint violation probability with growing residual (Proposition 2. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control")).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A rollout-cost uncertainty analysis (Proposition 3. ‣ V-B Rollout-Cost Sensitivity Analysis ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control")) showing that mismatch-induced perturbations of MPPI importance weights are bounded by $2C_{\Delta}\bar{s}_{k}/\beta_{k}$, providing theoretical justification for raising temperature as model-plant mismatch grows.

<!-- chunk {"id": "body-0011", "role": "body", "section": "System Model", "weight": 1.0} -->

Consider a discrete-time system with state $\mathbf{x}_{k}\in\mathcal{X}\subseteq\mathbb{R}^{n_{x}}$ and control $\mathbf{u}_{k}\in\mathcal{U}\subseteq\mathbb{R}^{n_{u}}$, where $\mathcal{X}$ and $\mathcal{U}$ are compact sets. The controller plans using a nominal parametric predictor where $\theta$ denotes the nominal model parameter. The true system evolves as $\mathbf{x}_{k+1}=\tilde{f}(\mathbf{x}_{k},\mathbf{u}_{k})+\mathbf{w}_{k}$, where $\tilde{f}$ is the true (unknown) dynamics and $\mathbf{w}_{k}\in\mathbb{R}^{n_{x}}$ is a stochastic process disturbance.

<!-- chunk {"id": "body-0012", "role": "body", "section": "System Model", "weight": 1.0} -->

The controller receives noisy state measurements $\mathbf{y}_{k}=\mathbf{x}_{k}+\mathbf{v}_{k}$, where $\mathbf{v}_{k}\in\mathbb{R}^{n_{x}}$ is the measurement noise. At each time step $k$, the controller optimizes over a finite planning horizon of $N\geq 1$ steps. Safety is encoded by a constraint function $h:\mathcal{X}\rightarrow\mathbb{R}$, where the safe set is $\mathcal{X}_{s}:=\{\mathbf{x}\in\mathcal{X}\mid h(\mathbf{x})\leq 0\}$ and $h$ is Lipschitz with constant $L_{h}>0$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 3 (Nominal MPPI Competence)", "weight": 1.0} -->

Under zero prediction--execution residual ($\bar{s}_{k}=0$, as defined in ), vanilla MPPI with nominal temperature $\beta_{0}$ achieves constraint satisfaction with probability at least $1-\delta_{0}$ for some $\delta_{0}\in$, and the prior mean control sequence $\bar{\mathbf{U}}$ (initialized from the shifted solution of the previous time step) lies in the safe region with probability at least $1-\delta_{0}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Remark 1 (Practical validity of Assumption 3. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control\"))", "weight": 1.0} -->

Assumption 3. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control") is behavioral, not structural: it requires no convexity or geometric property of the cost landscape, only that the baseline works when the model is accurate. This is consistent with the simulation results in Section VII, where vanilla MPPI performs competently under moderate mismatch conditions.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Remark 2 (Practical validity of Assumption 4. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control\"))", "weight": 1.0} -->

Assumption 4. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control") is satisfied by sensors with finite resolution or hardware-level clipping, which is standard on low-cost robotic and embedded platforms. It separates measurement noise, which is bounded by sensor characteristics, from process disturbance $\mathbf{w}_{k}$, which is modeled as sub-Gaussian to capture environment uncertainty.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Residual Estimation", "weight": 1.0} -->

After executing $\mathbf{u}_{k-1}$ and measuring $\mathbf{y}_{k}=\mathbf{x}_{k}+\mathbf{v}_{k}$, the one-step prediction residual is A scalar mismatch indicator $s_{k}:=\|\mathbf{W}_{r}\mathbf{r}_{k}\|$ (invertible weighting matrix $\mathbf{W}_{r}$) is filtered as Define the aggregated horizon disturbance which accumulates the stochastic disturbances over the planning horizon weighted by the Lipschitz expansion factor $L_{f}$. Since $\mathbf{r}_{k}$ depends only on $\mathbf{y}_{k}$, $\mathbf{y}_{k-1}$, and $\mathbf{u}_{k-1}$, the filtered statistic $\bar{s}_{k}$ is $\mathcal{F}_{k+1}$-measurable.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Residual Estimation", "weight": 1.0} -->

By Assumption 2. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control"), the future disturbances $\mathbf{w}_{k},\ldots,\mathbf{w}_{k+N-1}$ are independent of $\mathcal{F}_{k+1}$, so $\boldsymbol{\xi}_{k+N}$ is independent of $\bar{s}_{k}$ given $\mathcal{F}_{k+1}$. This separation is the key that allows the deterministic residual-dependent term $c_{r}\bar{s}_{k}+c_{0}$ and the stochastic term $\|\boldsymbol{\xi}_{k+N}\|$ to be bounded independently in Theorem 1. ‣ III-A Residual Estimation ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control").

<!-- chunk {"id": "body-0018", "role": "body", "section": "Residual-Conservative MPPI", "weight": 1.0} -->

RC-MPPI augments vanilla MPPI with three residual-driven mechanisms that tighten safety and reduce model-confidence as execution mismatch grows. Algorithm 1 summarizes the per-step procedure.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Residual-Conservative MPPI", "weight": 1.0} -->

1: Measure yk; compute rk via; update s̄k via 3: Sample ϵ(i) ∼ 𝒩(0, 𝜍k2I); roll out 4: Evaluate Z(i) with barrier αkϕ(h(x) + m(s̄k)) 5: Compute weights at temperature βk; update uk via; execute uk Algorithm 1 Residual-Conservative MPPI (RC-MPPI) Step 1 converts the raw measurement into a scalar mismatch signal $\bar{s}_{k}$. Step 2 translates that signal into three coupled residual-adaptive mechanisms: (i) residual-dependent barrier tightening $m(\bar{s}_{k})$ that deforms the effective safe set; (ii) amplified barrier penalty $\alpha_{k}$ that strengthens the cost signal against unsafe rollouts; and (iii) residual-adaptive temperature relaxation $(\varsigma_{k},\beta_{k})$ that contracts exploration and softens importance weights to reflect reduced confidence in cost evaluations under an inaccurate model. Steps 3--5 are standard MPPI rollout and update, now operating under the residual-adapted cost and sampling distribution.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Residual-Conservative MPPI", "weight": 1.0} -->

When $\bar{s}_{k}\approx 0$ all three modulations vanish and RC-MPPI reduces to vanilla MPPI.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-A Risk-Sensitive MPPI", "weight": 1.0} -->

MPPI minimizes the entropic (free-energy) cost functional where $\beta>0$ is the *temperature*. Larger $\beta$ reduces sensitivity to cost differences across rollouts, producing a more uniform weight distribution; smaller $\beta$ sharpens the weights onto the lowest-cost rollout.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A Risk-Sensitive MPPI", "weight": 1.0} -->

In RC-MPPI, $\beta$ encodes *confidence in rollout cost evaluations*. When the model is accurate, small $\beta$ concentrates mass on the genuinely best rollout. When the model is wrong, cost evaluations are unreliable, and large $\beta$ prevents over-commitment to a rollout that merely *appears* optimal under the mismatched model. This interpretation is formalized in Proposition 3. ‣ V-B Rollout-Cost Sensitivity Analysis ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control"), which shows that the sensitivity of importance weights to rollout-cost uncertainty scales as $2C_{\Delta}\bar{s}_{k}/\beta_{k}$, providing theoretical justification for raising $\beta_{k}$ as model-plant mismatch grows.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Residual-dependent tightening", "weight": 1.0} -->

where $c_{r}$ and $c_{0}$ are the explicit horizon-dependent constants from Theorem 1. ‣ III-A Residual Estimation ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control"): $c_{r}=S_{N}\|\mathbf{W}_{r}^{-1}\|/\rho$ and $c_{0}=(L_{f}^{N}+S_{N})\bar{v}$. The margin thus scales with horizon $N$ and Lipschitz constant $L_{f}$: longer horizons or more expansive dynamics require greater tightening, as expected.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Residual-adaptive sampling modulation", "weight": 1.0} -->

As $\bar{s}_{k}$ increases: $\varsigma_{k}\downarrow$ contracts exploration; $\beta_{k}\uparrow$ softens importance weights to reflect reduced model confidence.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 4 (Complementary roles of $\\alpha_{k}$ and $\\beta_{k}$)", "weight": 1.0} -->

$\alpha_{k}$ amplifies the barrier signal so unsafe rollouts incur large cost regardless of temperature. $\beta_{k}$ controls exploitation of that signal. Although $\beta_{k}\uparrow$ softens weights, the barrier cost $\alpha_{k}\phi(m(\bar{s}_{k}))$ grows as $O(\bar{s}_{k}^{2})$ while $\beta_{k}$ grows as $O(\bar{s}_{k})$: their ratio diverges, and unsafe rollouts receive asymptotically zero weight despite the rising temperature (Lemma 1. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control")(ii)). The performance advantage of $\beta\uparrow$ over $\beta\downarrow$ under mismatch is established in Proposition 3. ‣ V-B Rollout-Cost Sensitivity Analysis ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control").

<!-- chunk {"id": "body-0026", "role": "body", "section": "Residual-Adaptive Safety Analysis", "weight": 1.0} -->

Terminal constraint satisfaction is a standard analysis paradigm in receding-horizon control, and probabilistic formulations are well-established in stochastic and chance-constrained MPC. We adopt this framework to bound the probability that the nominal terminal prediction violates the safety constraint $h(\mathbf{x}_{k+N})\leq 0$, and show that all three RC-MPPI mechanisms jointly reduce this probability as model-plant mismatch grows. Proposition 1. ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") establishes a baseline from constraint tightening. Lemma 1. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") and Lemma 2. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") characterize temperature adaptation and trajectory concentration. Proposition 2. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") gives the joint bound, and Corollary 2.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Residual-Adaptive Safety Analysis", "weight": 1.0} -->

‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") establishes that RC-MPPI achieves at least the constraint satisfaction probability of vanilla MPPI, with strict improvement whenever $\bar{s}_{k}>0$. Separately, Proposition 3. ‣ V-B Rollout-Cost Sensitivity Analysis ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") establishes that raising $\beta_{k}$ reduces the sensitivity of importance weights to rollout-cost uncertainty induced by model-plant mismatch, providing theoretical justification for the residual-adaptive temperature rule.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 5 (Synergistic improvement)", "weight": 1.0} -->

The leading exponential captures geometric tightening alone; $\Gamma\leq 1$ provides additional multiplicative reduction. Critically, rising $\beta_{k}$ does *not* degrade safety: quadratic barrier growth dominates linear temperature growth. As $\bar{s}_{k}\to 0$, $\Gamma\to 1$ recovering Corollary 1. ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control").

<!-- chunk {"id": "body-0029", "role": "body", "section": "V-B Rollout-Cost Sensitivity Analysis", "weight": 1.0} -->

We now prove that the $\beta\uparrow$ strategy is not merely safe but *preferable* above an explicit mismatch threshold. The key additional ingredient is Lemma 3. ‣ V-B Rollout-Cost Sensitivity Analysis ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control"), which bounds how model-plant mismatch perturbs the rollout cost landscape.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 6 (Scope and connection to model uncertainty)", "weight": 1.0} -->

Lemma 3. ‣ V-B Rollout-Cost Sensitivity Analysis ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") shows that the residual $\bar{s}_{k}$ upper-bounds the mismatch-induced rollout-cost uncertainty, and Proposition 3. ‣ V-B Rollout-Cost Sensitivity Analysis ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") shows that the resulting MPPI weight perturbation is bounded by $2C_{\Delta}\bar{s}_{k}/\beta_{k}$. Thus, raising $\beta_{k}$ under growing mismatch reduces sensitivity to unreliable cost rankings, while simultaneous constraint tightening and penalty amplification maintain safety. However, Proposition 3. ‣ V-B Rollout-Cost Sensitivity Analysis ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") does not advocate unbounded temperature increase: in the limit $\beta_{k}\to\infty$, importance weights become uniform and the MPPI update degenerates to unguided random averaging.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 6 (Scope and connection to model uncertainty)", "weight": 1.0} -->

In RC-MPPI this is prevented by the clipping, which keeps $\beta_{k}\leq\beta_{\max}$, so temperature relaxation remains moderate and the controller retains directional guidance from the cost landscape.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 7 (Residual vs. stochastic disturbance)", "weight": 1.0} -->

$\bar{s}_{k}$ captures *systematic* mismatch (actuator lag, saturation, model error) while $\boldsymbol{\xi}_{k+N}$ models *stochastic* disturbances. RC-MPPI separates these: $m(\bar{s}_{k})$ compensates for structured bias by shrinking the effective safe set, while the exponential bound (15. ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control")) quantifies remaining stochastic violation probability due to $\boldsymbol{\xi}_{k+N}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Episodic Model Adaptation", "weight": 1.0} -->

On the fast time scale, $\bar{s}_{k}$ drives online adaptation without modifying $\theta$. On the slow scale, model parameters are updated episodically, reducing prediction error and relaxing safety margins.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Simulation Study", "weight": 1.0} -->

We evaluate RC-MPPI on two systems of increasing complexity. The implementation is available.

<!-- chunk {"id": "body-0035", "role": "body", "section": "VII-A1 Setup", "weight": 1.0} -->

The state $\mathbf{x}=[p_{x},p_{y},v_{x},v_{y}]^{\top}$ evolves according to the nominal discrete-time LTI model $\mathbf{x}_{k+1}=\mathbf{A}\mathbf{x}_{k}+\mathbf{B}\mathbf{u}_{k}$ with with $\Delta t=0.1$ s. The MPPI horizon is $T=40$ with $K=2048$ rollouts and input bound $u_{\max}=4$. The obstacle is centered at $\mathbf{c}^{\star}=[2.5,0]^{\top}$ with radius $r=1.5$ m. The goal is $\mathbf{p}_{g}=^{\top}$. A trial is considered successful if the goal is reached within $0.25$ m and no obstacle violation occurs.

<!-- chunk {"id": "body-0036", "role": "body", "section": "VII-A2 Model-Plant Mismatch", "weight": 1.0} -->

The true plant includes a severe first-order actuator lag with $\tau=0.9$ s and $\alpha=1-\exp(-\Delta t/\tau)\approx 0.105$. The planner assumes the nominal LTI model and therefore systematically overestimates achievable velocity changes near the obstacle, producing persistent model-plant mismatch.

<!-- chunk {"id": "body-0037", "role": "body", "section": "VII-A4 Results", "weight": 1.0} -->

We performed $n=50$ paired-seed Monte Carlo trials of 300 control steps each (Table I, Fig. 1). Vanilla MPPI achieves a success rate of $0.64$, minimum clearance $0.05\pm 0.10$ m, and $4.16\pm 6.32$ violation steps. RC-MPPI increases the success rate to $0.94$, improves minimum clearance to $0.13\pm 0.09$ m, and reduces violation steps to $0.62\pm 2.63$. These results indicate substantially improved safety and constraint satisfaction under severe actuator lag and model-plant mismatch.

<!-- chunk {"id": "body-0038", "role": "body", "section": "VII-A4 Results", "weight": 1.0} -->

RC-MPPI exhibits a modest increase in time-to-goal ($232.78\pm 22.71\rightarrow 249.00\pm 12.62$ steps) and path length ($15.85\pm 0.90\rightarrow 16.42\pm 0.74$ m), consistent with the intended safety--efficiency tradeoff. As residuals increase, constraint tightening, penalty amplification, exploration contraction, and temperature relaxation collectively bias the controller toward safer trajectories rather than aggressive obstacle-skimming behavior.

<!-- chunk {"id": "body-0039", "role": "body", "section": "VII-A4 Results", "weight": 1.0} -->

The representative trial (seed 21, Fig. 1) illustrates this tradeoff. Vanilla MPPI penetrates the obstacle region (minimum clearance $-0.082$ m, 21 violation steps), whereas RC-MPPI maintains positive clearance ($0.193$ m), incurs no violations, and successfully reaches the goal.

<!-- chunk {"id": "body-0040", "role": "body", "section": "VII-A4 Results", "weight": 1.0} -->

Fig. 1: Safety–efficiency tradeoff under severe actuator lag (seed 21, τ = 0.9 s). Vanilla MPPI (red dashed) penetrates the obstacle and accumulates 21 violation steps, whereas RC-MPPI (blue solid) maintains positive clearance and successfully reaches the goal through a more conservative trajectory.

<!-- chunk {"id": "body-0041", "role": "body", "section": "VII-B1 Setup", "weight": 1.0} -->

The nominal planner rolls out the discrete-time Euler-integrated equations of motion for a planar (horizontal) 2R arm, where $\mathbf{u}_{k}\in\mathbb{R}^{2}$ is the joint torque command, $\mathbf{M}^{n}(\mathbf{q})$ is the $2\times 2$ inertia matrix and $\mathbf{C}^{n}(\mathbf{q},\dot{\mathbf{q}})\dot{\mathbf{q}}$ is the Coriolis/centripetal vector, both evaluated under the nominal parameters $(M_{1}^{n},M_{2}^{n})$. Gravity is absent (horizontal plane). The timestep is $\Delta t=0.02$ s. The goal position is $\mathbf{p}_{g}=[1.35,0.35]^{\top}$ m.

<!-- chunk {"id": "body-0042", "role": "body", "section": "VII-B1 Setup", "weight": 1.0} -->

A circular obstacle is located at $\mathbf{o}=[0.85,0.20]^{\top}$ with radius $0.15$ m. The MPPI configuration uses $K=1024$ rollouts and horizon $T=35$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "VII-B2 Model-Plant Mismatch", "weight": 1.0} -->

Three independent mismatch sources are simultaneously present: first-order actuator lag ($\tau_{\mathrm{servo}}=0.15$ s), torque saturation at $\pm 6$ N$\cdot$m per joint, measurement noise ($\eta_{q}=0.002$ rad, $\eta_{\dot{q}}=0.010$ rad/s).

<!-- chunk {"id": "body-0044", "role": "body", "section": "VII-B2 Model-Plant Mismatch", "weight": 1.0} -->

Together with the inertial parameter mismatch, these effects produce persistent prediction--execution residuals that activate the RC-MPPI adaptation mechanisms.

<!-- chunk {"id": "body-0045", "role": "body", "section": "VII-B3 Results", "weight": 1.0} -->

We performed $n=50$ paired-seed Monte Carlo trials of 200 control steps each (Table II). The manipulator experiment shows a substantial benefit from residual-adaptive conservatism. Vanilla MPPI succeeds in 56% of trials, whereas RC-MPPI achieves a success rate of 96%. Violation steps decrease from $3.08\pm 4.41$ to $0.10\pm 0.57$, and minimum link clearance improves from approximately $-0.00\pm 0.03$ m to $0.02\pm 0.01$ m.

<!-- chunk {"id": "body-0046", "role": "body", "section": "VII-B3 Results", "weight": 1.0} -->

RC-MPPI also improves task efficiency in this experiment: time-to-goal decreases from $100.56\pm 89.47$ to $26.24\pm 36.13$ steps, end-effector path length decreases from $5.29\pm 0.41$ to $3.97\pm 0.22$ m, and control energy decreases from $3681.03\pm 446.17$ to $1490.88\pm 156.49$. The representative trial (Fig. 2) illustrates the trajectory-level safety improvement: RC-MPPI maintains positive clearance and converges rapidly to the goal, whereas vanilla MPPI approaches or penetrates the obstacle boundary. Fig. 3 further shows that RC-MPPI maintains strictly positive link clearance throughout the trial, while vanilla MPPI crosses the zero boundary. These results support the interpretation that residual-driven tightening, penalty scaling, exploration contraction, and temperature relaxation jointly prevent overcommitment to unreliable nominal rollouts under inertial mismatch, actuator lag, saturation, and measurement noise.

<!-- chunk {"id": "body-0047", "role": "body", "section": "VII-B3 Results", "weight": 1.0} -->

Fig. 2: Representative manipulator trial showing safety and convergence improvement. Vanilla MPPI (red dashed) frequently approaches or penetrates the obstacle boundary under model mismatch, whereas RC-MPPI (blue solid) maintains positive clearance and converges rapidly to the goal. Shaded disk: true obstacle.

<!-- chunk {"id": "body-0048", "role": "body", "section": "VII-B3 Results", "weight": 1.0} -->

Fig. 3: Link clearance over time for the representative manipulator trial (seed 0). At each step, clearance is the minimum distance from the obstacle center to either link segment, minus the obstacle radius. RC-MPPI (blue solid) maintains strictly positive clearance throughout, whereas Vanilla MPPI (red dashed) approaches and crosses the zero boundary, incurring constraint violations.

<!-- chunk {"id": "body-0049", "role": "body", "section": "VII-B3 Results", "weight": 1.0} -->

Min link clearance (m) TABLE II: 2R manipulator system (n = 50, K = 1024). Mean±std.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper presented RC-MPPI, a residual-aware sampling-based MPC framework that modulates safety conservatism through three coupled mechanisms: residual-dependent constraint tightening, adaptive safety penalty scaling, and residual-adaptive sampling modulation comprising temperature relaxation and exploration contraction. The probabilistic safety analysis, grounded in an $N$-step horizon prediction error bound (Theorem 1. ‣ III-A Residual Estimation ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control")), establishes that the joint effect of all three mechanisms monotonically reduces constraint violation probability with growing residual, and that RC-MPPI achieves at least the constraint satisfaction probability of vanilla MPPI with strict improvement whenever model-plant mismatch is nonzero. The rollout-cost uncertainty analysis further shows that mismatch-induced weight perturbations are bounded by $2C_{\Delta}\bar{s}_{k}/\beta_{k}$, providing theoretical justification for treating temperature as an epistemic parameter encoding confidence in rollout cost evaluations rather than solely as an exploration parameter.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Paired-seed Monte Carlo simulations on an LTI point-mass system and a planar 2R manipulator confirm that RC-MPPI consistently improves constraint satisfaction, success rate, and control efficiency over vanilla MPPI under significant model-plant mismatch, with the performance gap widening as model uncertainty grows. Future work will investigate hardware validation on robotic platforms, integration with learned residual dynamics models, and extensions to belief-space and multi-agent sampling-based MPC formulations.
