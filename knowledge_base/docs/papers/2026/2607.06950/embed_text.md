<!-- arxiv-full-text:v1 {"arxiv_id": "2607.06950", "source": "arxiv-html"} -->

## Introduction

Low-cost robotic and embedded control platforms frequently exhibit execution variability arising from actuation lag, saturation, unmodeled inner-loop dynamics, and limited sensing fidelity. When high-level planners rely on simplified or nominal actuator models, such effects induce model-plant mismatch that can compromise constraint satisfaction. In receding-horizon implementations, this mismatch is persistent and state-dependent rather than a one-time disturbance.

Sampling-based model predictive control methods, such as Model Predictive Path Integral (MPPI) control, handle nonlinear dynamics and complex cost landscapes through Monte Carlo rollouts and importance weighting. However, standard formulations assume a fixed nominal model and employ static constraint penalties or barrier functions that do not adapt to model-plant mismatch. When model-plant mismatch grows, fixed safety mechanisms may become insufficient.

This paper addresses the problem of online conservatism adaptation under model-plant mismatch. Rather than performing real-time parameter identification or maintaining a full disturbance belief, we exploit the prediction--execution residual, the directly measurable discrepancy between predicted and realized state transitions, as a lightweight signal of model-plant mismatch, and embed it into the sampling-based MPC objective via three coupled adaptive mechanisms.

The resulting method, Residual-Conservative MPPI (RC-MPPI), enforces safety through residual-dependent constraint tightening and amplified penalty scaling, while the MPPI temperature is *relaxed* in proportion to the observed prediction--execution residual. Standard MPPI treats temperature as a fixed exploration parameter; under model-plant mismatch, however, this conflates genuine cost differences with artifacts of an inaccurate model. RC-MPPI instead treats temperature as an epistemic parameter encoding confidence in rollout cost evaluations. We show that the $\ell_{1}$ deviation between true and nominal importance weights is bounded by $2C_{\Delta}\bar{s}_{k}/\beta_{k}$, where $C_{\Delta}$ captures cost sensitivity to model-plant mismatch and $\bar{s}_{k}$ is the filtered residual. Since this bound grows with mismatch and shrinks with temperature, raising $\beta_{k}$ as $\bar{s}_{k}$ increases directly limits the distortion of MPPI weights by corrupted rollout cost rankings.

RC-MPPI, a sampling-based MPC scheme with three coupled residual-adaptive mechanisms: constraint tightening, penalty scaling, and residual-adaptive sampling modulation comprising temperature relaxation and exploration contraction, with no additional computational cost over standard MPPI. Temperature is treated as an epistemic parameter encoding confidence in rollout cost evaluations under model-plant mismatch.

A probabilistic safety analysis grounded in an $N$-step horizon prediction error bound (Theorem 1. ‣ III-A Residual Estimation ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control")), establishing that the joint effect of all three mechanisms monotonically reduces constraint violation probability with growing residual (Proposition 2. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control")).

A rollout-cost uncertainty analysis (Proposition 3. ‣ V-B Rollout-Cost Sensitivity Analysis ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control")) showing that mismatch-induced perturbations of MPPI importance weights are bounded by $2C_{\Delta}\bar{s}_{k}/\beta_{k}$, providing theoretical justification for raising temperature as model-plant mismatch grows.

## Related Work

Model Predictive Path Integral (MPPI) control is a sampling-based approximation of stochastic optimal control derived from information-theoretic principles. By performing importance sampling over trajectory rollouts and computing a soft-min update, MPPI enables real-time nonlinear control without explicit gradient computation. In baseline implementations, constraints are handled through soft penalties, barrier-like shaping, or rollout truncation; however, hard rejection of infeasible trajectories reduces the effective sample size, leading to weight degeneracy. To address safety requirements, recent work integrates Control Barrier Functions into MPPI. Shield-MPPI introduces a CBF-inspired shielding mechanism, and guaranteed-safe MPPI variants employ composite CBF constructions. Other approaches propagate uncertainty explicitly: unscented MPPI uses sigma-point approximations, and belief-space stochastic MPPI enforces approximate chance constraints.

More broadly, chance-constrained MPC enforces probabilistic constraint satisfaction, and classical risk-sensitive control penalizes tail events through exponential cost transformations. Robust MPC enforces safety through tube-based tightening, and learning-based MPC incorporates model adaptation while preserving constraint satisfaction. RC-MPPI complements these directions by modulating conservatism using the filtered prediction--execution residual. A distinguishing feature is the treatment of temperature as an *epistemic* parameter encoding confidence in rollout cost evaluations, supported by a rollout-cost uncertainty analysis that links model-plant mismatch, importance-weight sensitivity, and adaptive temperature selection.

## System Model

Consider a discrete-time system with state $\mathbf{x}_{k}\in\mathcal{X}\subseteq\mathbb{R}^{n_{x}}$ and control $\mathbf{u}_{k}\in\mathcal{U}\subseteq\mathbb{R}^{n_{u}}$, where $\mathcal{X}$ and $\mathcal{U}$ are compact sets. The controller plans using a nominal parametric predictor where $\theta$ denotes the nominal model parameter. The true system evolves as $\mathbf{x}_{k+1}=\tilde{f}(\mathbf{x}_{k},\mathbf{u}_{k})+\mathbf{w}_{k}$, where $\tilde{f}$ is the true (unknown) dynamics and $\mathbf{w}_{k}\in\mathbb{R}^{n_{x}}$ is a stochastic process disturbance. The controller receives noisy state measurements $\mathbf{y}_{k}=\mathbf{x}_{k}+\mathbf{v}_{k}$, where $\mathbf{v}_{k}\in\mathbb{R}^{n_{x}}$ is the measurement noise. At each time step $k$, the controller optimizes over a finite planning horizon of $N\geq 1$ steps. Safety is encoded by a constraint function $h:\mathcal{X}\rightarrow\mathbb{R}$, where the safe set is $\mathcal{X}_{s}:=\{\mathbf{x}\in\mathcal{X}\mid h(\mathbf{x})\leq 0\}$ and $h$ is Lipschitz with constant $L_{h}>0$.

### Assumption 1 (Local Lipschitz Nominal Dynamics)

There exists $L_{f}>0$ such that for all $(\mathbf{x},\mathbf{u}),(\mathbf{x}^{\prime},\mathbf{u})$ in $\mathcal{X}\times\mathcal{U}$, $\|f_{\theta}(\mathbf{x},\mathbf{u})-f_{\theta}(\mathbf{x}^{\prime},\mathbf{u})\|\leq L_{f}\|\mathbf{x}-\mathbf{x}^{\prime}\|$.

### Assumption 2 (Sub-Gaussian Disturbance)

$\mathbf{w}_{k}$ is i.i.d. sub-Gaussian with scalar variance proxy $\sigma_{x}^{2}>0$: there exist $a_{1},a_{2}>0$ such that $\mathbb{P}(\|\mathbf{w}_{k}\|\geq t)\leq a_{1}\exp(-a_{2}t^{2}/\sigma_{x}^{2})$ for all $t\geq 0$. Furthermore, $\mathbf{w}_{k}$ is independent of the natural filtration $\mathcal{F}_{k}:=\sigma(\mathbf{x}_{0},\mathbf{w}_{0},\mathbf{v}_{0},\ldots,\mathbf{w}_{k-1},\mathbf{v}_{k-1})$ generated by the system history up to time $k$.

### Assumption 3 (Nominal MPPI Competence)

Under zero prediction--execution residual ($\bar{s}_{k}=0$, as defined in ), vanilla MPPI with nominal temperature $\beta_{0}$ achieves constraint satisfaction with probability at least $1-\delta_{0}$ for some $\delta_{0}\in$, and the prior mean control sequence $\bar{\mathbf{U}}$ (initialized from the shifted solution of the previous time step) lies in the safe region with probability at least $1-\delta_{0}$.

### Remark 1 (Practical validity of Assumption 3. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control"))

Assumption 3. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control") is behavioral, not structural: it requires no convexity or geometric property of the cost landscape, only that the baseline works when the model is accurate. This is consistent with the simulation results in Section VII, where vanilla MPPI performs competently under moderate mismatch conditions.

### Assumption 4 (Bounded Measurement Noise)

The measurement noise satisfies $\|\mathbf{v}_{k}\|\leq\bar{v}$ almost surely for some $\bar{v}>0$.

### Remark 2 (Practical validity of Assumption 4. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control"))

Assumption 4. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control") is satisfied by sensors with finite resolution or hardware-level clipping, which is standard on low-cost robotic and embedded platforms. It separates measurement noise, which is bounded by sensor characteristics, from process disturbance $\mathbf{w}_{k}$, which is modeled as sub-Gaussian to capture environment uncertainty.

### III-A Residual Estimation

After executing $\mathbf{u}_{k-1}$ and measuring $\mathbf{y}_{k}=\mathbf{x}_{k}+\mathbf{v}_{k}$, the one-step prediction residual is A scalar mismatch indicator $s_{k}:=\|\mathbf{W}_{r}\mathbf{r}_{k}\|$ (invertible weighting matrix $\mathbf{W}_{r}$) is filtered as Define the aggregated horizon disturbance which accumulates the stochastic disturbances over the planning horizon weighted by the Lipschitz expansion factor $L_{f}$. Since $\mathbf{r}_{k}$ depends only on $\mathbf{y}_{k}$, $\mathbf{y}_{k-1}$, and $\mathbf{u}_{k-1}$, the filtered statistic $\bar{s}_{k}$ is $\mathcal{F}_{k+1}$-measurable. By Assumption 2. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control"), the future disturbances $\mathbf{w}_{k},\ldots,\mathbf{w}_{k+N-1}$ are independent of $\mathcal{F}_{k+1}$, so $\boldsymbol{\xi}_{k+N}$ is independent of $\bar{s}_{k}$ given $\mathcal{F}_{k+1}$. This separation is the key that allows the deterministic residual-dependent term $c_{r}\bar{s}_{k}+c_{0}$ and the stochastic term $\|\boldsymbol{\xi}_{k+N}\|$ to be bounded independently in Theorem 1. ‣ III-A Residual Estimation ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control").

### Theorem 1 (Implementable Horizon Prediction Error Bound)

Under Assumptions 1. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control")--4. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control"), conditioned on $\mathcal{F}_{k+1}$, the terminal prediction error $\mathbf{e}_{k+N}:=\mathbf{x}_{k+N}-\hat{\mathbf{x}}_{k+N}$ satisfies are $\mathcal{F}_{k+1}$-measurable planning-time constants, and $\boldsymbol{\xi}_{k+N}$ is independent of $\mathcal{F}_{k+1}$ with sub-Gaussian variance proxy $\sigma_{x}^{2}(L_{f}^{2N}-1)/(L_{f}^{2}-1)$.

### Proof

Step 1 (One-step residual-to-deviation). The one-step prediction residual satisfies $\mathbf{r}_{k}=(\mathbf{x}_{k}-\hat{\mathbf{x}}_{k|k-1})+\mathbf{v}_{k}$, so The filter recursion gives $\bar{s}_{k}\geq\rho s_{k}$, hence $s_{k}\leq\rho^{-1}\bar{s}_{k}$, yielding Step 2 ($N$-step error propagation). Let $\boldsymbol{\delta}_{t}:=\mathbf{x}_{k+t}-\hat{\mathbf{x}}_{k+t}$ with $\|\boldsymbol{\delta}_{0}\|\leq\bar{v}$ (since $\hat{\mathbf{x}}_{k}=\mathbf{y}_{k}=\mathbf{x}_{k}+\mathbf{v}_{k}$). The recursion with $\|\boldsymbol{\Delta}_{k+t}\|\leq\|\mathbf{W}_{r}^{-1}\|s_{k+t+1}+\bar{v}$ gives, upon unrolling over $N$ steps, where $\bar{s}_{k}^{N}:=\max_{0\leq t\leq N-1}s_{k+t+1}$ and $S_{N}=(L_{f}^{N}-1)/(L_{f}-1)$ for $L_{f}>1$ (or $N$ for $L_{f}=1$).

Step 3 (Replacing $\bar{s}_{k}^{N}$ with $\bar{s}_{k}$). Under the planning-window stationarity condition, the mismatch level does not increase over the horizon $[k,k+N-1]$, so $\bar{s}_{k}^{N}\leq s_{k}$ almost surely. The filter recursion gives $\bar{s}_{k}\geq\rho s_{k}$, hence $s_{k}\leq\rho^{-1}\bar{s}_{k}$. Chaining these two inequalities yields so substituting gives the $\mathcal{F}_{k+1}$-measurable bound (5. ‣ III-A Residual Estimation ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control")) with $c_{r}=S_{N}\|\mathbf{W}_{r}^{-1}\|/\rho$ and $c_{0}=(L_{f}^{N}+S_{N})\bar{v}$.

Step 4 (Sub-Gaussian tail of $\boldsymbol{\xi}_{k+N}$). Since $\boldsymbol{\xi}_{k+N}=\sum_{t=0}^{N-1}L_{f}^{N-1-t}\mathbf{w}_{k+t}$ is a weighted sum of independent sub-Gaussian disturbances with squared coefficient sum $\sum_{t=0}^{N-1}L_{f}^{2t}=(L_{f}^{2N}-1)/(L_{f}^{2}-1)$, it is sub-Gaussian with the stated variance proxy. Independence from $\mathcal{F}_{k+1}$ follows from Assumption 2. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control"). ∎

## Residual-Conservative MPPI

RC-MPPI augments vanilla MPPI with three residual-driven mechanisms that tighten safety and reduce model-confidence as execution mismatch grows. Algorithm 1 summarizes the per-step procedure.

1: Measure yk; compute rk via; update s̄k via 3: Sample ϵ(i) ∼ 𝒩(0, 𝜍k2I); roll out 4: Evaluate Z(i) with barrier αkϕ(h(x) + m(s̄k)) 5: Compute weights at temperature βk; update uk via; execute uk Algorithm 1 Residual-Conservative MPPI (RC-MPPI) Step 1 converts the raw measurement into a scalar mismatch signal $\bar{s}_{k}$. Step 2 translates that signal into three coupled residual-adaptive mechanisms: (i) residual-dependent barrier tightening $m(\bar{s}_{k})$ that deforms the effective safe set; (ii) amplified barrier penalty $\alpha_{k}$ that strengthens the cost signal against unsafe rollouts; and (iii) residual-adaptive temperature relaxation $(\varsigma_{k},\beta_{k})$ that contracts exploration and softens importance weights to reflect reduced confidence in cost evaluations under an inaccurate model. Steps 3--5 are standard MPPI rollout and update, now operating under the residual-adapted cost and sampling distribution. When $\bar{s}_{k}\approx 0$ all three modulations vanish and RC-MPPI reduces to vanilla MPPI.

### IV-A Risk-Sensitive MPPI

MPPI minimizes the entropic (free-energy) cost functional where $\beta>0$ is the *temperature*. Larger $\beta$ reduces sensitivity to cost differences across rollouts, producing a more uniform weight distribution; smaller $\beta$ sharpens the weights onto the lowest-cost rollout.

In RC-MPPI, $\beta$ encodes *confidence in rollout cost evaluations*. When the model is accurate, small $\beta$ concentrates mass on the genuinely best rollout. When the model is wrong, cost evaluations are unreliable, and large $\beta$ prevents over-commitment to a rollout that merely *appears* optimal under the mismatched model. This interpretation is formalized in Proposition 3. ‣ V-B Rollout-Cost Sensitivity Analysis ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control"), which shows that the sensitivity of importance weights to rollout-cost uncertainty scales as $2C_{\Delta}\bar{s}_{k}/\beta_{k}$, providing theoretical justification for raising $\beta_{k}$ as model-plant mismatch grows.

### Trajectory cost

| | $\displaystyle Z(\mathbf{U})=$ | $\displaystyle\sum_{t=0}^{N-1}\!\Big(\ell_{\mathrm{trk}}(\mathbf{x}_{k+t})+\ell_{u}(\mathbf{u}_{k+t})+\ell_{\mathrm{safe}}(\mathbf{x}_{k+t};\bar{s}_{k})\Big)$ | | \(8\) | | | | $\displaystyle+\ell_{f}(\mathbf{x}_{k+N}),$ | | | where $\ell_{\mathrm{trk}}(\mathbf{x})=\|\mathbf{x}-\mathbf{x}^{\mathrm{ref}}\|_{\mathbf{Q}}^{2}$ with positive definite weight matrices $\mathbf{Q},\mathbf{Q}_{f}\succ 0$, $\ell_{u}(\mathbf{u})=\|\mathbf{u}\|_{\mathbf{R}}^{2}$ with $\mathbf{R}\succ 0$, $\phi(z)=\max(0,z)^{2}$, $m(\bar{s}_{k})$ is the residual-dependent tightening margin defined, and $\ell_{f}(\mathbf{x})=\|\mathbf{x}-\mathbf{x}^{\mathrm{ref}}_{k+N}\|_{\mathbf{Q}_{f}}^{2}$.

### Importance sampling update

Perturbations $\boldsymbol{\epsilon}^{(i)}\sim\mathcal{N}(0,\varsigma_{k}^{2}\mathbf{I})$ form sequences $\mathbf{U}^{(i)}=\mathbf{U}+\boldsymbol{\epsilon}^{(i)}$ with costs $Z^{(i)}:=Z(\mathbf{U}^{(i)})$.

### IV-B Residual-Conservative Barrier Modulation

### Residual-dependent tightening

where $c_{r}$ and $c_{0}$ are the explicit horizon-dependent constants from Theorem 1. ‣ III-A Residual Estimation ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control"): $c_{r}=S_{N}\|\mathbf{W}_{r}^{-1}\|/\rho$ and $c_{0}=(L_{f}^{N}+S_{N})\bar{v}$. The margin thus scales with horizon $N$ and Lipschitz constant $L_{f}$: longer horizons or more expansive dynamics require greater tightening, as expected.

### Remark 3 (Implementation)

For $h(\mathbf{x})=r-d(\mathbf{x})$, radius inflation $r_{\mathrm{eff}}=r+\mathrm{clip}(\kappa_{r}\bar{s}_{k},0,\Delta r_{\max})$ implements tightening since $h(\mathbf{x})+m(\bar{s}_{k})=(r+m(\bar{s}_{k}))-d(\mathbf{x})$, where $\mathrm{clip}(v,0,\Delta r_{\max}):=\min(\max(v,0),\Delta r_{\max})$ saturates the inflation to the interval $[0,\Delta r_{\max}]$.

### Residual-aware penalty scaling

### Residual-adaptive sampling modulation

As $\bar{s}_{k}$ increases: $\varsigma_{k}\downarrow$ contracts exploration; $\beta_{k}\uparrow$ softens importance weights to reflect reduced model confidence.

### Remark 4 (Complementary roles of $\alpha_{k}$ and $\beta_{k}$)

$\alpha_{k}$ amplifies the barrier signal so unsafe rollouts incur large cost regardless of temperature. $\beta_{k}$ controls exploitation of that signal. Although $\beta_{k}\uparrow$ softens weights, the barrier cost $\alpha_{k}\phi(m(\bar{s}_{k}))$ grows as $O(\bar{s}_{k}^{2})$ while $\beta_{k}$ grows as $O(\bar{s}_{k})$: their ratio diverges, and unsafe rollouts receive asymptotically zero weight despite the rising temperature (Lemma 1. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control")(ii)). The performance advantage of $\beta\uparrow$ over $\beta\downarrow$ under mismatch is established in Proposition 3. ‣ V-B Rollout-Cost Sensitivity Analysis ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control").

## Residual-Adaptive Safety Analysis

Terminal constraint satisfaction is a standard analysis paradigm in receding-horizon control, and probabilistic formulations are well-established in stochastic and chance-constrained MPC. We adopt this framework to bound the probability that the nominal terminal prediction violates the safety constraint $h(\mathbf{x}_{k+N})\leq 0$, and show that all three RC-MPPI mechanisms jointly reduce this probability as model-plant mismatch grows. Proposition 1. ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") establishes a baseline from constraint tightening. Lemma 1. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") and Lemma 2. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") characterize temperature adaptation and trajectory concentration. Proposition 2. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") gives the joint bound, and Corollary 2. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") establishes that RC-MPPI achieves at least the constraint satisfaction probability of vanilla MPPI, with strict improvement whenever $\bar{s}_{k}>0$. Separately, Proposition 3. ‣ V-B Rollout-Cost Sensitivity Analysis ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") establishes that raising $\beta_{k}$ reduces the sensitivity of importance weights to rollout-cost uncertainty induced by model-plant mismatch, providing theoretical justification for the residual-adaptive temperature rule.

### Proposition 1 (Terminal Safety Bound)

Under Assumptions 1. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control")--2. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control"), let $d_{\mathrm{safe}}:=-h(\hat{\mathbf{x}}_{k+N})>0$ denote the nominal terminal safety margin. Applying Theorem 1. ‣ III-A Residual Estimation ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control") to bound the terminal prediction error, if $d_{\mathrm{safe}}\geq m(\bar{s}_{k})$, then

### Proof

Since $h$ is Lipschitz with constant $L_{h}$, so $\{h(\mathbf{x}_{k+N})>0\}\subseteq\{L_{h}\|\mathbf{e}_{k+N}\|>d_{\mathrm{safe}}\}$. By Theorem 1. ‣ III-A Residual Estimation ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control"), $\|\mathbf{e}_{k+N}\|\leq c_{r}\bar{s}_{k}+c_{0}+\|\boldsymbol{\xi}_{k+N}\|$, so multiplying by $L_{h}$ and using $m(\bar{s}_{k})=L_{h}(c_{r}\bar{s}_{k}+c_{0})$ gives $L_{h}\|\mathbf{e}_{k+N}\|\leq m(\bar{s}_{k})+L_{h}\|\boldsymbol{\xi}_{k+N}\|$. Therefore, Since $\boldsymbol{\xi}_{k+N}$ is independent of $\bar{s}_{k}$ given $\mathcal{F}_{k+1}$ by Theorem 1. ‣ III-A Residual Estimation ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control"), the sub-Gaussian tail bound of Assumption 2. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control") applies conditionally with $t=(d_{\mathrm{safe}}-m(\bar{s}_{k}))/L_{h}$, yielding (15. ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control")). ∎

### Corollary 1 (Consistency with Nominal MPPI)

The modulation functions -- are continuous in $\bar{s}_{k}$. Consequently, and RC-MPPI reduces to standard MPPI with nominal temperature $\beta_{0}$ and fixed safety shaping.

### Proof

Direct substitution of $\bar{s}_{k}=0$ into --, using continuity of each expression in $\bar{s}_{k}$. ∎

### V-A Joint Safety via Adaptive Weighting

### Lemma 1 (Temperature-Averaging Under Mismatch)

\(i\) \[Update variance reduction.\] The MPPI control update satisfies Hence the variance bound is nonincreasing in $\beta_{k}$. Since RC-MPPI increases $\beta_{k}$ as the residual indicator $\bar{s}_{k}$ grows, the control update becomes increasingly averaged, and the variance bound tightens under larger model-plant mismatch.

\(ii\) \[Barrier suppression.\] Any unsafe rollout ($h(\mathbf{x}^{(i)}_{k+N})>0$) satisfies Since $\alpha_{k}\phi(m(\bar{s}_{k}))\sim O(\bar{s}_{k}^{2})$ while $\beta_{k}\sim O(\bar{s}_{k})$, the exponent diverges to $-\infty$: unsafe rollouts receive asymptotically zero weight.

### Proof

Part (i). Following the importance sampling formulation of MPPI, let $p=\mathcal{N}(0,\varsigma_{k}^{2}\mathbf{I})$ denote the prior sampling distribution over control perturbations, and let $q$ denote the importance-weighted posterior induced by the MPPI weights. Let $\mathbf{U}:=\{\mathbf{u}_{k},\ldots,\mathbf{u}_{k+N-1}\}$ denote the control sequence over the planning horizon. A standard Gibbs-measure perturbation inequality gives where $\mathrm{diam}(Z):=\max_{i}Z^{(i)}-\min_{i}Z^{(i)}$ is the range of rollout costs. The bound is nonincreasing in $\beta_{k}$. Since RC-MPPI increases $\beta_{k}$ as $\bar{s}_{k}$ grows, the variance bound tightens under larger model-plant mismatch.

Part (ii). For any unsafe rollout $i$ with $h(\mathbf{x}^{(i)}_{k+N})>0$, the barrier term $\alpha_{k}\phi(h(\mathbf{x}^{(i)}_{k+N})+m(\bar{s}_{k}))$ is strictly positive. Since $\phi(z)=\max(0,z)^{2}$ and $h(\mathbf{x}^{(i)}_{k+N})>0$ implies $h(\mathbf{x}^{(i)}_{k+N})+m(\bar{s}_{k})>m(\bar{s}_{k})>0$, we have for any safe rollout $j$. Substituting into the weight formula gives which proves (17. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control")). To show this ratio vanishes as $\bar{s}_{k}$ grows, note that while from and, $\alpha_{k}\sim O(\bar{s}_{k})$ and $\beta_{k}\sim O(\bar{s}_{k})$. Therefore, so the weight ratio (17. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control")) converges to zero and unsafe rollouts receive asymptotically negligible weight. ∎

### Lemma 2 (Rollout Concentration)

Let $\mathbf{x}_{k+t}$ denote the unperturbed nominal rollout obtained by propagating $f_{\theta}$ from $\hat{\mathbf{x}}_{k}=\mathbf{y}_{k}$ under the mean control sequence $\mathbf{U}$, and let $\mathbf{x}^{(i)}_{k+t}$ denote the $i$-th Monte Carlo rollout obtained by propagating $f_{\theta}$ under the perturbed control sequence $\mathbf{U}^{(i)}=\mathbf{U}+\boldsymbol{\epsilon}^{(i)}$ with $\boldsymbol{\epsilon}^{(i)}\sim\mathcal{N}(0,\varsigma_{k}^{2}\mathbf{I})$, where $\varsigma_{k}$ is the residual-adaptive sampling standard deviation defined. Both trajectories are initialized from $\hat{\mathbf{x}}_{k}$ and propagated under the nominal model $f_{\theta}$ --- the true plant is not involved. This bound is used in Proposition 2. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") to quantify the probability that a perturbed rollout reaches the unsafe region $\{h(\mathbf{x}^{(i)}_{k+N})>0\}$. For any rollout $i$ and step $t\geq 1$, Since RC-MPPI reduces $\varsigma_{k}$ as $\bar{s}_{k}$ increases via, the bound (18. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control")) tightens and the Monte Carlo rollouts concentrate more tightly around the unperturbed nominal rollout under larger model-plant mismatch.

### Proof

Let $\boldsymbol{\delta}_{t}^{(i)}:=\mathbf{x}_{k+t}^{(i)}-\mathbf{x}_{k+t}$ denote the deviation between the $i$-th Monte Carlo rollout and the unperturbed nominal rollout, both propagated under $f_{\theta}$ from the same initial state $\hat{\mathbf{x}}_{k}=\mathbf{y}_{k}$. Since both trajectories are initialized from the same state, $\boldsymbol{\delta}_{0}^{(i)}=0$. The deviation between the perturbed and unperturbed rollouts evolves under Assumption 1. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control") as where $\boldsymbol{\epsilon}_{k+t}^{(i)}\sim\mathcal{N}(0,\varsigma_{k}^{2}\mathbf{I})$ is the MPPI sampling perturbation applied at step $t$ of rollout $i$. Note that no true plant dynamics appear here --- both trajectories follow $f_{\theta}$, so the deviation is driven purely by the control perturbations $\boldsymbol{\epsilon}^{(i)}$. Recursively unrolling the inequality yields Since $\boldsymbol{\delta}_{t}^{(i)}$ is a linear combination of independent Gaussian perturbations, it is itself Gaussian with covariance bounded by Therefore each coordinate of $\boldsymbol{\delta}_{t}^{(i)}$ is sub-Gaussian with variance proxy at most $L_{f}^{2t}\varsigma_{k}^{2}$. Applying the standard sub-Gaussian tail inequality and a union bound over the $n_{x}$ state coordinates gives which proves (18. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control")). ∎

### Proposition 2 (Joint Adaptive Safety Bound)

Under Assumptions 1. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control")--3. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control"), with $d_{\mathrm{safe}}\geq m(\bar{s}_{k})$ and applying Theorem 1. ‣ III-A Residual Estimation ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control") to bound the terminal prediction error, | | | $\displaystyle\mathbb{P}\!\left(h(\mathbf{x}_{k+N})>0\,\middle|\,\mathcal{F}_{k+1}\right)$ | | \(19\) | | | | $\displaystyle\leq c_{1}\exp\!\left(-\frac{c_{2}\bigl(d_{\mathrm{safe}}-m(\bar{s}_{k})\bigr)^{2}}{\sigma_{x}^{2}}\right)\Gamma(\bar{s}_{k}),$ | | |

### Proof

Step 1. Proposition 1. ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") gives the baseline exponential. Step 2. By Lemma 1. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control")(ii), the total unsafe weight is bounded by $\exp(-\alpha_{k}\phi(m(\bar{s}_{k}))/\beta_{k})$; although $\beta_{k}\uparrow$, the $O(\bar{s}_{k}^{2})$ numerator dominates the $O(\bar{s}_{k})$ denominator, so the exponent diverges to $-\infty$. Step 3. By Lemma 2. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control"), reaching the unsafe region requires deviation $\geq d_{\mathrm{safe}}/L_{f}^{N}$, with probability $\leq 2n_{x}\exp(-d_{\mathrm{safe}}^{2}/2L_{f}^{2N}\varsigma_{k}^{2})$. Step 4. Combining Steps 2--3 via $\exp(-A)\exp(-B)=\exp(-(A+B))$ gives $\Gamma$ (absorbing $2n_{x}$ into $c_{1}$); multiplying with Step 1 gives (19. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control")). Monotonicity: $\varsigma_{k}\downarrow$ drives the second exponent more negative; $\alpha_{k}\phi(m(\bar{s}_{k}))/\beta_{k}\sim O(\bar{s}_{k}^{2})$ drives the first more negative. Hence $\Gamma\in(0,1]$ nonincreasing. ∎

### Corollary 2 (RC-MPPI Dominates Vanilla MPPI Under Mismatch)

Under Assumptions 1. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control")--3. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control"), suppose $d_{\mathrm{safe}}\geq m(\bar{s}_{k})$. Applying Theorem 1. ‣ III-A Residual Estimation ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control") to bound the terminal prediction error and invoking Proposition 2. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control"), | | | $\displaystyle\mathbb{P}(h(\mathbf{x}_{k+N})>0\mid\mathcal{F}_{k+1})$ | | \(20\) | | | | $\displaystyle\leq c_{1}\exp\!\left(-\frac{c_{2}\bigl(d_{\mathrm{safe}}-m(\bar{s}_{k})\bigr)^{2}}{\sigma_{x}^{2}}\right)\Gamma(\bar{s}_{k})$ | | | | | | $\displaystyle\leq\delta_{0},$ | | | so RC-MPPI achieves constraint satisfaction with probability at least $1-\delta_{0}$.

### Proof

The first inequality is Proposition 2. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control"). For the second, note that $\Gamma(\bar{s}_{k})\in(0,1]$ is nonincreasing in $\bar{s}_{k}$ with $\Gamma=1$. At $\bar{s}_{k}=0$, Proposition 2. ‣ V-A Joint Safety via Adaptive Weighting ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") reduces to Proposition 1. ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") with $m=L_{h}c_{0}$, and the bound equals $\delta_{0}$ by Assumption 3. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control"). For $\bar{s}_{k}>0$, $\Gamma(\bar{s}_{k})<1$ gives strict improvement over the vanilla MPPI baseline. ∎

### Remark 5 (Synergistic improvement)

The leading exponential captures geometric tightening alone; $\Gamma\leq 1$ provides additional multiplicative reduction. Critically, rising $\beta_{k}$ does *not* degrade safety: quadratic barrier growth dominates linear temperature growth. As $\bar{s}_{k}\to 0$, $\Gamma\to 1$ recovering Corollary 1. ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control").

### V-B Rollout-Cost Sensitivity Analysis

We now prove that the $\beta\uparrow$ strategy is not merely safe but *preferable* above an explicit mismatch threshold. The key additional ingredient is Lemma 3. ‣ V-B Rollout-Cost Sensitivity Analysis ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control"), which bounds how model-plant mismatch perturbs the rollout cost landscape.

### Lemma 3 (Bounded Cost Perturbation)

Under Assumptions 1. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control")--2. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control") and Theorem 1. ‣ III-A Residual Estimation ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control"), conditioned on $\mathcal{F}_{k+1}$, let $\mathbf{U}:=\{\mathbf{u}_{k},\ldots,\mathbf{u}_{k+N-1}\}\in\mathcal{U}^{N}$ denote the control trajectory over the planning horizon. The trajectory cost perturbation satisfies uniformly over $\mathbf{U}\in\mathcal{U}^{N}$, where $C_{\Delta}:=N(\alpha_{k}L_{h}L_{f}^{N}+W_{\max})(\tilde{c}_{r}+\tilde{c}_{0})$ and $W_{\max}$ is the maximum cost weight. Here $C_{\Delta}$ and $\bar{s}_{k}$ are both $\mathcal{F}_{k+1}$-measurable, so the bound is a deterministic statement given the observed history.

### Proof

Under Assumption 1. ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control") and Theorem 1. ‣ III-A Residual Estimation ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control"), the true and nominal state trajectories deviate by at most $L_{f}^{t}(\tilde{c}_{r}\bar{s}_{k}+\tilde{c}_{0})$ at step $t$. Each cost term is Lipschitz in $\mathbf{x}$ with constant bounded by $W_{\max}(1+\alpha_{k}L_{h}L_{f}^{N})$. Summing over $N$ steps and bounding $\sum_{t=0}^{N-1}L_{f}^{t}\leq NL_{f}^{N}$ gives (21. ‣ V-B Rollout-Cost Sensitivity Analysis ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control")). ∎

### Proposition 3 (Weight Sensitivity Under Rollout-Cost Uncertainty)

Suppose the nominal rollout costs used by MPPI are perturbed by model uncertainty as for each sampled rollout $i=1,\ldots,K$. Let denote the MPPI importance weight at temperature $\beta$. Then, applying Lemma 3. ‣ V-B Rollout-Cost Sensitivity Analysis ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control"), the sensitivity of the importance weights to rollout-cost uncertainty is bounded as Consequently, increasing $\beta$ reduces the effect of model-induced rollout-cost uncertainty on the MPPI update. Since Lemma 3. ‣ V-B Rollout-Cost Sensitivity Analysis ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") shows that this uncertainty grows with the residual magnitude $\bar{s}_{k}$, the residual-adaptive rule $\beta_{k}=\beta_{0}(1+\kappa_{\beta}\bar{s}_{k})$ reduces overcommitment to cost rankings that become unreliable under large model-plant mismatch.

### Proof

Let $Z(\tau)=Z^{\mathrm{nom}}+\tau\Delta$ for $\tau\in$. By the mean-value theorem, For the softmax weights with negative costs, Since $|\Delta_{j}|\leq C_{\Delta}\bar{s}_{k}$ and Summing over $i$ and using $\sum_{i}w_{i}=1$ gives Thus the influence of model-induced rollout-cost errors on the MPPI weights scales as $C_{\Delta}\bar{s}_{k}/\beta$. Increasing $\beta$ therefore reduces sensitivity to uncertain rollout rankings. Since Lemma 3. ‣ V-B Rollout-Cost Sensitivity Analysis ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") bounds the rollout-cost uncertainty by a residual-dependent term, the adaptive choice $\beta_{k}\uparrow$ under large $\bar{s}_{k}$ directly implements residual-adaptive temperature relaxation. ∎

### Remark 6 (Scope and connection to model uncertainty)

Lemma 3. ‣ V-B Rollout-Cost Sensitivity Analysis ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") shows that the residual $\bar{s}_{k}$ upper-bounds the mismatch-induced rollout-cost uncertainty, and Proposition 3. ‣ V-B Rollout-Cost Sensitivity Analysis ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") shows that the resulting MPPI weight perturbation is bounded by $2C_{\Delta}\bar{s}_{k}/\beta_{k}$. Thus, raising $\beta_{k}$ under growing mismatch reduces sensitivity to unreliable cost rankings, while simultaneous constraint tightening and penalty amplification maintain safety. However, Proposition 3. ‣ V-B Rollout-Cost Sensitivity Analysis ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control") does not advocate unbounded temperature increase: in the limit $\beta_{k}\to\infty$, importance weights become uniform and the MPPI update degenerates to unguided random averaging. In RC-MPPI this is prevented by the clipping , which keeps $\beta_{k}\leq\beta_{\max}$, so temperature relaxation remains moderate and the controller retains directional guidance from the cost landscape.

### Remark 7 (Residual vs. stochastic disturbance)

$\bar{s}_{k}$ captures *systematic* mismatch (actuator lag, saturation, model error) while $\boldsymbol{\xi}_{k+N}$ models *stochastic* disturbances. RC-MPPI separates these: $m(\bar{s}_{k})$ compensates for structured bias by shrinking the effective safe set, while the exponential bound (15. ‣ V Residual-Adaptive Safety Analysis ‣ Residual-Conservative Model Predictive Path Integral Control")) quantifies remaining stochastic violation probability due to $\boldsymbol{\xi}_{k+N}$.

## Episodic Model Adaptation

On the fast time scale, $\bar{s}_{k}$ drives online adaptation without modifying $\theta$. On the slow scale, model parameters are updated episodically, reducing prediction error and relaxing safety margins.

### Lemma 4 (Prediction Loss Reduction)

Let $\mathcal{L}(\theta):=\frac{1}{M}\sum_{i=1}^{M}\|\mathbf{y}_{i}-f_{\theta}(\mathbf{x}_{i},\mathbf{u}_{i})\|^{2}$ denote the empirical prediction loss. If $\theta^{+}$ is obtained by a descent step from $\theta$ on $\mathcal{L}$, then $\mathcal{L}(\theta^{+})\leq\mathcal{L}(\theta)$.

### Proof

A descent step ensures $\mathcal{L}(\theta^{+})\leq\mathcal{L}(\theta)$ by definition; $\theta$ is always a feasible starting point. ∎

### Theorem 2 (Decreasing Conservatism Under Model Improvement)

If $\mathbb{E}\|\mathbf{r}(\theta^{+})\|\leq\mathbb{E}\|\mathbf{r}(\theta)\|$, then $\mathbb{E}[m(\bar{s}(\theta^{+}))]\leq\mathbb{E}[m(\bar{s}(\theta))]$.

### Proof

Since $s_{k}=\|\mathbf{W}_{r}\mathbf{r}_{k}\|\leq\|\mathbf{W}_{r}\|\|\mathbf{r}_{k}\|$, reduced $\mathbb{E}\|\mathbf{r}\|$ implies reduced $\mathbb{E}[s_{k}]$. Linearity of then gives $\mathbb{E}[\bar{s}_{t}]=(1-\rho)\mathbb{E}[\bar{s}_{t-1}]+\rho\mathbb{E}[s_{t}]$, so $\mathbb{E}[\bar{s}_{t}]$ decreases. Since $m(\bar{s})=L_{h}(c_{r}\bar{s}+c_{0})$ is nondecreasing in $\bar{s}$, it follows that $\mathbb{E}[m(\bar{s}(\theta^{+}))]\leq\mathbb{E}[m(\bar{s}(\theta))]$. ∎ As accuracy improves, residuals decrease, margins relax, and $\beta_{k}$ returns toward $\beta_{0}$, recovering nominal MPPI behavior.

## Simulation Study

We evaluate RC-MPPI on two systems of increasing complexity. The implementation is available .

### VII-A LTI Point-Mass System

### VII-A1 Setup

The state $\mathbf{x}=[p_{x},p_{y},v_{x},v_{y}]^{\top}$ evolves according to the nominal discrete-time LTI model $\mathbf{x}_{k+1}=\mathbf{A}\mathbf{x}_{k}+\mathbf{B}\mathbf{u}_{k}$ with with $\Delta t=0.1$ s. The MPPI horizon is $T=40$ with $K=2048$ rollouts and input bound $u_{\max}=4$. The obstacle is centered at $\mathbf{c}^{\star}=[2.5,0]^{\top}$ with radius $r=1.5$ m. The goal is $\mathbf{p}_{g}=^{\top}$. A trial is considered successful if the goal is reached within $0.25$ m and no obstacle violation occurs.

### VII-A2 Model-Plant Mismatch

The true plant includes a severe first-order actuator lag with $\tau=0.9$ s and $\alpha=1-\exp(-\Delta t/\tau)\approx 0.105$. The planner assumes the nominal LTI model and therefore systematically overestimates achievable velocity changes near the obstacle, producing persistent model-plant mismatch.

### VII-A3 RC-MPPI Parameters

Running-cost weights are $(w_{g},w_{v},w_{u},w_{T})=(5,0.1,0.01,50)$ with $w_{\mathrm{obs}}=10^{4}$. The residual statistic is with $(w_{p},w_{v}^{\prime})=(1.0,0.5)$ and filtering parameter $\rho=0.2$. Residual-adaptive modulation uses $\kappa_{r}=1.0$, $\Delta r_{\max}=1.0$ m, $\kappa_{\varsigma}=0.5$, and $\kappa_{\beta}=5.0$. The MPPI temperature follows $\beta_{k}=\beta_{0}(1+\kappa_{\beta}\bar{s}_{k})$ subject to clipping.

### VII-A4 Results

We performed $n=50$ paired-seed Monte Carlo trials of 300 control steps each (Table I, Fig. 1). Vanilla MPPI achieves a success rate of $0.64$, minimum clearance $0.05\pm 0.10$ m, and $4.16\pm 6.32$ violation steps. RC-MPPI increases the success rate to $0.94$, improves minimum clearance to $0.13\pm 0.09$ m, and reduces violation steps to $0.62\pm 2.63$. These results indicate substantially improved safety and constraint satisfaction under severe actuator lag and model-plant mismatch.

RC-MPPI exhibits a modest increase in time-to-goal ($232.78\pm 22.71\rightarrow 249.00\pm 12.62$ steps) and path length ($15.85\pm 0.90\rightarrow 16.42\pm 0.74$ m), consistent with the intended safety--efficiency tradeoff. As residuals increase, constraint tightening, penalty amplification, exploration contraction, and temperature relaxation collectively bias the controller toward safer trajectories rather than aggressive obstacle-skimming behavior.

The representative trial (seed 21, Fig. 1) illustrates this tradeoff. Vanilla MPPI penetrates the obstacle region (minimum clearance $-0.082$ m, 21 violation steps), whereas RC-MPPI maintains positive clearance ($0.193$ m), incurs no violations, and successfully reaches the goal.

Fig. 1: Safety–efficiency tradeoff under severe actuator lag (seed 21, τ = 0.9 s). Vanilla MPPI (red dashed) penetrates the obstacle and accumulates 21 violation steps, whereas RC-MPPI (blue solid) maintains positive clearance and successfully reaches the goal through a more conservative trajectory.

TABLE I: LTI point-mass system. Mean±std.

### VII-B Planar 2R Manipulator

### VII-B1 Setup

The true manipulator parameters are $L_{1}=1.0$ m, $L_{2}=0.8$ m, $M_{1}=1.0$ kg, and $M_{2}=0.8$ kg. The nominal planner intentionally uses mismatched inertial parameters The state is $\mathbf{x}=[q_{1},q_{2},\dot{q}_{1},\dot{q}_{2}]^{\top}$ with bounded torque input $|u_{k,i}|\leq 6$ N$\cdot$m ($i=1,2$). The nominal planner rolls out the discrete-time Euler-integrated equations of motion for a planar (horizontal) 2R arm, where $\mathbf{u}_{k}\in\mathbb{R}^{2}$ is the joint torque command, $\mathbf{M}^{n}(\mathbf{q})$ is the $2\times 2$ inertia matrix and $\mathbf{C}^{n}(\mathbf{q},\dot{\mathbf{q}})\dot{\mathbf{q}}$ is the Coriolis/centripetal vector, both evaluated under the nominal parameters $(M_{1}^{n},M_{2}^{n})$. Gravity is absent (horizontal plane). The timestep is $\Delta t=0.02$ s. The goal position is $\mathbf{p}_{g}=[1.35,0.35]^{\top}$ m. A circular obstacle is located at $\mathbf{o}=[0.85,0.20]^{\top}$ with radius $0.15$ m. The MPPI configuration uses $K=1024$ rollouts and horizon $T=35$.

### VII-B2 Model-Plant Mismatch

Three independent mismatch sources are simultaneously present: first-order actuator lag ($\tau_{\mathrm{servo}}=0.15$ s), torque saturation at $\pm 6$ N$\cdot$m per joint, measurement noise ($\eta_{q}=0.002$ rad, $\eta_{\dot{q}}=0.010$ rad/s).

Together with the inertial parameter mismatch, these effects produce persistent prediction--execution residuals that activate the RC-MPPI adaptation mechanisms.

### VII-B3 Results

We performed $n=50$ paired-seed Monte Carlo trials of 200 control steps each (Table II). The manipulator experiment shows a substantial benefit from residual-adaptive conservatism. Vanilla MPPI succeeds in 56% of trials, whereas RC-MPPI achieves a success rate of 96%. Violation steps decrease from $3.08\pm 4.41$ to $0.10\pm 0.57$, and minimum link clearance improves from approximately $-0.00\pm 0.03$ m to $0.02\pm 0.01$ m.

RC-MPPI also improves task efficiency in this experiment: time-to-goal decreases from $100.56\pm 89.47$ to $26.24\pm 36.13$ steps, end-effector path length decreases from $5.29\pm 0.41$ to $3.97\pm 0.22$ m, and control energy decreases from $3681.03\pm 446.17$ to $1490.88\pm 156.49$. The representative trial (Fig. 2) illustrates the trajectory-level safety improvement: RC-MPPI maintains positive clearance and converges rapidly to the goal, whereas vanilla MPPI approaches or penetrates the obstacle boundary. Fig. 3 further shows that RC-MPPI maintains strictly positive link clearance throughout the trial, while vanilla MPPI crosses the zero boundary. These results support the interpretation that residual-driven tightening, penalty scaling, exploration contraction, and temperature relaxation jointly prevent overcommitment to unreliable nominal rollouts under inertial mismatch, actuator lag, saturation, and measurement noise.

Fig. 2: Representative manipulator trial showing safety and convergence improvement. Vanilla MPPI (red dashed) frequently approaches or penetrates the obstacle boundary under model mismatch, whereas RC-MPPI (blue solid) maintains positive clearance and converges rapidly to the goal. Shaded disk: true obstacle.

Fig. 3: Link clearance over time for the representative manipulator trial (seed 0). At each step, clearance is the minimum distance from the obstacle center to either link segment, minus the obstacle radius. RC-MPPI (blue solid) maintains strictly positive clearance throughout, whereas Vanilla MPPI (red dashed) approaches and crosses the zero boundary, incurring constraint violations.

Min link clearance (m) TABLE II: 2R manipulator system (n = 50, K = 1024). Mean±std.

## Conclusion

This paper presented RC-MPPI, a residual-aware sampling-based MPC framework that modulates safety conservatism through three coupled mechanisms: residual-dependent constraint tightening, adaptive safety penalty scaling, and residual-adaptive sampling modulation comprising temperature relaxation and exploration contraction. The probabilistic safety analysis, grounded in an $N$-step horizon prediction error bound (Theorem 1. ‣ III-A Residual Estimation ‣ III System Model ‣ Residual-Conservative Model Predictive Path Integral Control")), establishes that the joint effect of all three mechanisms monotonically reduces constraint violation probability with growing residual, and that RC-MPPI achieves at least the constraint satisfaction probability of vanilla MPPI with strict improvement whenever model-plant mismatch is nonzero. The rollout-cost uncertainty analysis further shows that mismatch-induced weight perturbations are bounded by $2C_{\Delta}\bar{s}_{k}/\beta_{k}$, providing theoretical justification for treating temperature as an epistemic parameter encoding confidence in rollout cost evaluations rather than solely as an exploration parameter. Paired-seed Monte Carlo simulations on an LTI point-mass system and a planar 2R manipulator confirm that RC-MPPI consistently improves constraint satisfaction, success rate, and control efficiency over vanilla MPPI under significant model-plant mismatch, with the performance gap widening as model uncertainty grows. Future work will investigate hardware validation on robotic platforms, integration with learned residual dynamics models, and extensions to belief-space and multi-agent sampling-based MPC formulations.
