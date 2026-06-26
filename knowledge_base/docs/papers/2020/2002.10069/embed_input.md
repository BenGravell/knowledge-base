<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robust Learning-Based Control via Bootstrapped Multiplicative Noise

Topics include Control, Optimal control, Robust control, Adaptive control, Reinforcement learning, Model-based, System identification, Multiplicative noise, Stochastic parameters, Bootstrap, Regret.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Assembles a pipeline for automatically designing controllers from data that perform well throughout the data acquisition and system operation timeline. Uncertainty is quantified with a statistical bootstrap and designed against by using a multiplicative noise framework to achieve robustness. The aim is to achieve both good robustness in the low-data short-term transient as well as good performance in the high-data long-term steady state condition.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Despite decades of research and recent progress in adaptive control and reinforcement learning, there remains a fundamental lack of understanding in designing controllers that provide robustness to inherent non-asymptotic uncertainties arising from models estimated with finite, noisy data. We propose a robust adaptive control algorithm that explicitly incorporates such non-asymptotic uncertainties into the control design. The algorithm has three components: a least-squares nominal model estimator; a bootstrap resampling method that quantifies non-asymptotic variance of the nominal model estimate; and a non-conventional robust control design method using an optimal linear quadratic regulator (LQR) with multiplicative noise. A key advantage of the proposed approach is that the system identification and robust control design procedures both use stochastic uncertainty representations, so that the actual inherent statistical estimation uncertainty directly aligns with the uncertainty the robust controller is being designed against. We show through numerical experiments that the proposed robust adaptive controller can significantly outperform the certainty equivalent controller on both expected regret and measures of regret risk.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent high profile successes and the resulting hype in machine learning and reinforcement learning are generating renewed interest in adaptive control and system identification, which have their own decades-long histories ˚ Astr¨ om and Wittenmark; Ljung. Classical work on adaptive control and system identification largely focused on asymptotics, including stability, consistency, asymptotic variance, etc. Emerging research at the intersection of learning and control shifts focus to non-asymptotic statistical analyses, including regret and sample efficiency in various adaptive control and learning algorithms Abbasi-Yadkori and Szepesv´ ari; Dean et al..

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In both classical and emerging work in learning and control, robustness has been a key issue. The classical focus on asymptotics led to a strong emphasis on certainty-equivalent adaptive control, where inevitable uncertainty in model estimates is ignored for control design and unsurprisingly can lead to serious lack of robustness. It remains poorly understood how to best interface both asymptotic and non-asymptotic uncertainty descriptions of model estimates with robust control design methods. One of the main difficulties is a mismatch in uncertainty descriptions: system identification almost universally uses stochastic data models 1, whereas robust control traditionally uses set-based descriptions and worst-case design. This can lead to unnecessary conservatism when the assumed model uncertainty sets are poorly aligned with inherent statistical model uncertainty. 1. A notable exception is set membership identification Milanese and Vicino, which maintains a set of models that could have produced the data within some error bound and interfaces somewhat more naturally with certain traditional robust control design methods.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The contributions of the present work are as follows: 1. We propose a robust adaptive control algorithm where the model uncertainty description and robust control design method both use stochastic uncertainty representations. 2. We show via numerical experiments that the proposed robust adaptive controller can significantly outperform the certainty equivalent controller on both expected regret and measures of regret risk.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The algorithm has three components: a least-squares nominal model estimator; a bootstrap resampling method that quantifies non-asymptotic variance of the nominal model estimate; and a non-conventional robust control design method using an optimal linear quadratic regulator (LQR) with multiplicative noise. This approach provides a natural interface between two widely used and highly effective methods from statistics and optimal control theory (namely, bootstrap sample variance and LQR). It is known that certainty equivalent adaptive control can achieve asymptotic optimality and statistical efficiency with an order optimal rate Chen and Guo; Kumar and Varaiya; Mania et al.. However, neither of these imply anything about non-asymptotic optimality or robustness.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We consider adaptive control of the discrete-time linear dynamical system where x t ∈ R n is the system state, u t ∈ R m is the control input, and w t is i.i.d. process noise with zero mean and covariance matrix W. The system matrices (A,B) are assumed unknown, so an adaptive controller is to be designed based only on state-input trajectory data x 0: t:= [x 0,..., x t], u 0: t -1 = [u 0,..., u t -1]. We consider the linear quadratic adaptive optimal control problem where Q ⪰ 0 and R ⪰ 0 are cost matrices, and the optimization is over (measureable) history dependent feedback policies π = { π t } T -1 t =0 with u t = π t (x 0: t, u 0: t -1).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The constant J ∗ in the stage costs represents the optimal infinite-horizon average steady state cost when the system matrices (A,B) are known, which results from a static linear state feedback, u t = Kx t, whose gain matrix K can be computed via several known methods, including value iteration, policy iteration, and semidefinite programming. This constant gives the stage cost an interpretation as regret.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The finite horizon objective in emphasizes the non-asymptotic performance of the adaptive controller. This stands in contrast to a majority of classical work on adaptive control, which tends to focus on asymptotic performance and stability. Note that regret is a random variable that ideally should be small, and there are various ways to measure its size, including expected regret, regret variance, and measures of regret risk, such as value at risk or conditional value at risk.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

It has been long known that this problem can be solved in principle by redefining the state as the (infinite-dimensional) joint conditional distribution over the original state and unknown model parameters and applying dynamic programming Bellman. However, this approach is intractable even for the most trivial instances. Since computing the optimal policy exactly appears to be intractable, we instead aim to design a computationally implementable controller with good performance and robustness properties, i.e., one that achieves both small expected regret and small regret risk. In particular, our algorithm accounts for uncertainty in various directions by modeling them as multiplicative noises, in contrast to the isotropic robustness afforded by the system-level synthesis in Dean et al.. We compare with a certainty equivalent adaptive controller, where uncertainty is ignored and a controller is designed as if the point model estimates were exact.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Robust Adaptive Control via Bootstrapping and Multiplicative Noise", "weight": 1.0} -->

Our robust adaptive control algorithm is summarized in Figure 1 and Algorithm 1. The algorithm has three main components: a least-squares nominal model estimator; a bootstrap resampling method that quantifies non-asymptotic variance of the nominal model estimate; and a non-conventional robust control design method using an optimal LQR with multiplicative noise. data-driven adaptive control architecture Figure 1: Block diagram of our robust adaptive control algorithm.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Algorithm 1 Robust Adaptive Control", "weight": 1.0} -->

Input: exploration time t explore, input excitation covariance U, number of bootstrap resamples N b, model uncertainty scaling parameter γ, cost matrices Q ⪰ 0, R ⪰ 0 1: x 0 ∼ N (0, X 0 ) 2: for t = 0,..., T -1 do 3: if t ≤ t explore then 4: u t ∼ N (0, U ) 5: x t +1 = Ax t + Bu t + w t 6: else 7: ( ˆ A t, ˆ B t ) = OrdinaryLeastSquares ( x 0: t, u 0: t -1 ) 8: ( ˆ Σ A t, ˆ Σ B t ) = BootstrapModelVariance ( x 0: t, u 0: t -1 ) 9: ˆ K t = MultiplicativeNoiseLQR ( ˆ A t, ˆ B t, Q, R, γ ˆ Σ A t, γ ˆ Σ B t ) 10: e t ∼ N (0, ‖ ( ˆ Σ A t, ˆ Σ B t ) ‖ U ) 11: u t = ˆ K t x t + e t 12: x t +1 = Ax

<!-- chunk {"id": "body-0014", "role": "body", "section": "Least Squares Estimation for the Nominal Model", "weight": 1.0} -->

The first component of the algorithm is a standard least-squares estimator for the unknown system matrices from state-input trajectory data. In particular, at time t from data (x 0: t, u 0: t -1), we form the estimate More explicitly, defining the data matrices X ᵀ t = [x 1 x 2 · · · x t], Z ᵀ t = [x 0 x 1 · · · x t -1 u 0 u 1 · · · u t -1] then the least squares estimate can be written as A non-degenerate model estimate is obtained only when Z ᵀ t Z t is invertible, so learning is divided into a pure exploration phase until a user-specified time t explore > n + m and subsequently an exploration-exploitation phase, where the estimated model is used to design a control policy. The exploration component of the input signal is iid Gaussian noise with user-specified covariance matrix U; it is well known that for any U ≻ 0 the least-squares estimator is consistent under our modeling assumptions. The exploration noise is designed to fade out with the bootstrap-estimated model uncertainty, which yields asymptotic optimality.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Least Squares Estimation for the Nominal Model", "weight": 1.0} -->

Under mild assumptions, the least-squares estimator can be implemented recursively to significantly simplify the repeated computation in as data arrives (e.g. Simon).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Bootstrap Resampling to Quantify Non-Asymptotic Model Uncertainty", "weight": 1.0} -->

There are inevitably errors in the least-squares estimate obtained from any finite data record, due to the process noise affecting the system dynamics. Due to dependence in the time series data, unfortunately it is not straightforward to analytically characterize non-asymptotic uncertainty in the least-squares estimate using standard statistical techniques. Therefore, to quantify non-asymptotic uncertainty in the model estimate, we propose a time series bootstrap resampling procedure. There are three broad bootstrap methods for time series H¨ ardle et al.: Parametric bootstrap; Semi-parametric bootstrap with resampled residuals; Non-parametric bootstrap with block resampling. In parametric and semi-parametric methods, bootstrap data are simulated from the nominal model with the process noise sampled iid with replacement either from an assumed distribution or from residuals calculated with the nominal model. Dependence in the data is preserved by construction. In non-parametric methods, overlapping time blocks of consecutive data are sampled from the original data to preserve dependence.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Bootstrap Resampling to Quantify Non-Asymptotic Model Uncertainty", "weight": 1.0} -->

For definiteness, a semi-parametric bootstrap with resampled residuals for the least-squares estimator discussed above is summarized in Algorithm 2.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Multiplicative Noise LQR", "weight": 1.0} -->

The least squares estimator and boostrap provide both a nominal estimate of the system model and an estimate of the covariance of the nominal model error. These quantities provide precisely the input data needed to compute an optimal policy for the LQR problem with multiplicative noise from the generalized Riccati equation. This policy is known to provide robustness to uncertainties in the parameters of the nominal model Bernstein and Greeley. Furthermore, the uncertainty

<!-- chunk {"id": "body-0019", "role": "body", "section": "Algorithm 2 Semi-Parametric Bootstrap", "weight": 1.0} -->

Input: trajectory data (x 0: t, u 0: t -1), nominal model estimate (ˆ A t, ˆ B t), residuals ˆ w τ = x τ +1 -(ˆ A t x τ + ˆ B t u τ), τ = 0,..., t -1, number of bootstrap resamples N b Output: Bootstrap sample covariance ˆ Σ A t = 1 N b -1 ∑ N b k =1 vec (ˆ A k t -ˆ A t) vec (ˆ A k t -ˆ A t) ᵀ Bootstrap sample covariance ˆ Σ B t = 1 N b -1 ∑ N b k =1 vec (ˆ B k t -ˆ B t) vec (ˆ B k t -ˆ B t) ᵀ in the nominal model estimate used in this control design method is richly structured and derived directly from the finite available data.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Algorithm 2 Semi-Parametric Bootstrap", "weight": 1.0} -->

We introduce a parameter γ which provides a fixed scaling of the model uncertainty. Note that γ = 0 corresponds to certainty equivalent adaptive control, and as γ increases, more weight is placed on uncertainty in the nominal model. Existence of a solution to the generalized Riccati equation depends not just on stabilizability of the nominal system ( A,B ), but also on the meansquare stabilizability of the multiplicative noise system. When the multiplicative noise variances are too large, it may be impossible to stabilize the system in the mean-square sense. In this case, we scale down the model variances at each time step if necessary to compute a mean-square stabilizing control gain via bisection; see Algorithm 3.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Algorithm 2 Semi-Parametric Bootstrap", "weight": 1.0} -->

In particular, we verify the system with specified γ is mean-square stabilizable by checking whether the generalized Riccati equation in admits a positive semidefinite solution; if not, we find the upper limit γ max = c γ γ via bisection (e.g. Burden et al. ) on a scaling c γ ∈.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Algorithm 3 Multiplicative Noise LQR", "weight": 1.0} -->

Input: Nominal model matrices A, B, cost matrices Q, R, multiplicative noise scaling γ and covariances ˆ Σ A, ˆ Σ B, bisection tolerance ϵ > 0 1: Find largest c γ ∈ via bisection such that there exists a feasible solution to Output: Cost matrix P, gain matrix K

<!-- chunk {"id": "body-0023", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

For brevity, we abbreviate 'certainty-equivalent' as 'CE' and 'robustness via multiplicative noise' as 'RMN'. To evaluate the performance of the proposed RMN algorithm relative to CE control, we performed Monte Carlo sampling to estimate the distribution of several key quantities: instantaneous regret, model error, and multiplicative noise variances.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The instantaneous regret is heavy-tailed in the sense that the effect of outliers with non-negligible probability is significant: some exceptionally poor sequences of model estimates induce extremely high costs relative to the median. For this reason, to facilitate the most direct comparison of CE and the proposed RMN approach, we train the models using both control schemes on identical offline training data. This way the effect of outlier model estimates is applied uniformly to both algorithms, since at each time the algorithms are faced with exactly the same model estimates. In an online adaptive control setting, where the training data are the actual state trajectories experienced under adaptive control, a direct comparison of the approaches is more difficult. While we observe qualitatively similar benefits of the proposed approach, our future work will study this setting with a greater number of Monte Carlo samples to reduce the effect of outliers.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The training data are generated by initializing the state at the origin, applying random controls distributed according to a standard Gaussian distribution (zero-mean, identity-covariance), and simulating the evolution of the state with the additive process noise specified by the problem data W. The resulting training data are a set of state trajectories x ( k ) 0: t and input trajectories u ( k ) 0: t -1. Model and uncertainty estimates are generated at time t according to Algorithm 1 using training data only up to time t. The optimal cost is empirically calculated by averaging over all Monte Carlo samples the cost incurred by trajectories under optimal control u t = K ∗ x t, K ∗ = DARE ( A,B,Q,R ) for each additive noise realization, i.e.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The empirical cost under adaptive control c ( k ) t is calculated similarly without averaging over Monte Carlo samples. Instantaneous regret is calculated by subtracting the empirical cost under optimal control from the empirical cost under adaptive control using each scheme i.e. r ( k ) t = c ( k ) t -c ∗ t.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We evaluated the CE and RMN algorithms on a scalar system with true system and cost parameters A = 1, B = 1, Q = 1, R = 0, W = 1. The level of additive process noise is significant enough that an appreciable number of model estimates remain poor for many timesteps; this is necessary to observe a difference between CE and RMN control. We simulated the system over a time horizon of T = 200 steps. We drew N s = 100, 000 independent Monte Carlo samples and N b = 100 bootstrap samples at each time step for uncertainty estimation. We used unity scaling of the multiplicative noise ( γ = 1 ) and a tolerance of ϵ = 0. 01 for bisection to find the largest scaling c γ of multiplicative noise variance in the multiplicative noise LQR algorithm. We used an exploration time of t explore = 5 which ensures the least-squares estimate is non-degenerate. The figures have x-axis limits truncated to [ t explore, T ].

<!-- chunk {"id": "body-0028", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In Figure 2 we plot statistics of instantaneous regret using CE control and using RMN control. We are chiefly interested in performance in terms of expected regret and upper quantiles, which correspond to regret risk. Figure 2 demonstrates that the multiplicative noise control achieves much lower instantaneous regret in terms of both the mean and upper quantiles. In particular, we see that the performance of the multiplicative noise control is clearly many orders of magnitude better between the start and t = 80, t = 40, t = 20 for the 99.9th, 99th and 95th quantiles, respectively. After several time steps the model estimates improve and uncertainty estimates become sufficiently small that the difference between CE and RMN control becomes insignificant. The heaviness of regret tails is shown by the massive difference between the mean and median.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In Figure 3 we plot statistics of the nominal model estimate errors, which are applicable to both control schemes. This shows that the least-squares estimator provides models of increasing accuracy as time goes, as expected. In Figure 4 we plot statistics of the multiplicative noise variances using RMN control. This shows that the multiplicative noise variances accurately reflect the true model error, i.e., the boostrap model uncertainty estimator gives reasonable estimates.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The benefits of RMN control over CE control more generally obviously cannot be inferred from this single instance. Indeed other preliminary numerical results on higher dimensional examples indicate that on some problem data (A, B, Q, R, W) the benefits of RMN control and how best to select the algorithm parameters are unclear, especially in initial stages when there is very high uncertainty around the nominal model estimates. However, there are at least some systems, like the one shown here, that are controlled with significantly lower risk using RMN control. We expect that by explicitly incorporating model uncertainty into the adaptive control design, it should be possible to realize the observed robustness benefits more broadly, which motivates further theoretical study. Code which realizes the algorithms of this paper and generates the reported results is available from Figure 2: Instantaneous regret vs time for the example system using using certainty-equivalent (a) and multiplicative noise (b) control.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We proposed a robust adaptive control algorithm that uses the bootstrap to estimate model estimate covariances and a non-conventional multiplicative noise LQR robust control method. Ongoing and future work will go towards providing finite-time theoretical performance guarantees using tools from high-dimensional statistics, finding algorithm parameters that ensure uniform improvements over certainty-equivalent control for any system, and implementing model uncertainty estimates using recursive least-squares to alleviate computational burden.
