<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robust Data-Driven Output Feedback Control via Bootstrapped Multiplicative Noise

Topics include Data-driven control, Output feedback control, Robust control, Adaptive control, System identification, Subspace identification, Bootstrap resampling, Uncertainty quantification, Finite-sample uncertainty, Multiplicative noise, Stochastic uncertainty models, Dynamic output feedback, Filter-controller co-design, Structured uncertainty, Non-asymptotic robustness, Stability robustness, Sample complexity, Certainty-equivalent, Learning-based control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Assembles a pipeline for adaptive control that uses a statistical bootstrap to estimate uncertainties in system parameters and a multiplicative-noise device to design a controller that is robust to the size and direction of the estimated uncertainties.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a robust data-driven output feedback control algorithm that explicitly incorporates inherent finite-sample model estimate uncertainties into the control design. The algorithm has three components: a subspace identification nominal model estimator; a bootstrap resampling method that quantifies non-asymptotic variance of the nominal model estimate; and a non-conventional robust control design method comprising a coupled optimal dynamic output feedback filter and controller with multiplicative noise. A key advantage of the proposed approach is that the system identification and robust control design procedures both use stochastic uncertainty representations, so that the actual inherent statistical estimation uncertainty directly aligns with the uncertainty the robust controller is being designed against. Moreover, the control design method accommodates a highly structured uncertainty representation that can capture uncertainty shape more effectively than existing approaches. We show through numerical experiments that the proposed robust data-driven output feedback controller can significantly outperform a certainty equivalent controller on various measures of sample complexity and stability robustness.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The intersection of data-driven learning and model-based control continues to provide significant research challenges despite its long history and vast research literature. Recent work has focused on non-asymptotic analysis of sample complexity, regret, and robustness, in contrast to a classical focus on asymptotics and stability. Approaches for data-driven control can be broadly divided into two categories: 'model-based' (or 'indirect'), in which a model for the system dynamics is first learned from data and then used to design a control policy, and 'model-free' (or 'direct'), in which a control policy is learned directly from data without explicitly learning a model for the system dynamics. Model-based approaches can be further divided into two categories: certainty equivalent, in which uncertainty in the learned model is ignored during control design, and robust, in which uncertainty in the learned model is explicitly accounted for in control design.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Much recent work has considered the full state feedback setting, and some results have very recently been obtained in the partially observed output feedback setting. Finite-sample bounds for system identification from input-state data have been obtained in Simchowitz et al.; Dean et al. and from input-output data in Care et al.; Tsiamis and Pappas; Sun et al.; Jedra and Proutiere; Oymak and Ozay; Sarkar et al.. Sample complexity and regret bounds for the Linear Quadratic Gaussian problem are described in Zheng et al.; Zhang et al. and Lale et al.; Simchowitz et al., respectively.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the partially observed setting, issues around robustness to model uncertainty are much more pronounced than in the full state feedback setting, a fact long known in control theory Doyle. Certainty equivalent approaches that ignore model uncertainty can lead to fragile designs, while existing approaches the incorporate model uncertainty often utilize very coarse uncertainty representations (e.g., spectral norm balls), even when obtaining order optimal statistical sample complexity or regret rates. A good balance between performance and robustness in practice requires carefully constructed and structured uncertainty representations; just as much effort should go into estimating from data the shape (not just size) of model uncertainty as the nominal model itself. This becomes especially important as the uncertainty dimension increases: structured uncertainties may have far less volume (in model space) than unstructured ones, thereby enabling superior performance. Developing algorithms with good non-asymptotic performance and robustness properties remains a significant challenge, both in theory and in practice. To address this challenge, Gravell and Summers proposed a data-driven robust control scheme via bootstrapped multiplicative noise for systems with perfect full state measurements; the present work extends these ideas to the partially observed output feedback setting.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. The contributions of the present work are as follows: 1. We propose a robust data-driven output feedback control algorithm where the model uncertainty description and robust control design method both use highly structured stochastic uncertainty representations. 2. We present a novel semi-parametric bootstrap algorithm for quantifying structured parametric uncertainty in state space models obtained from subspace identification algorithms using input-output data. 3. We show via numerical experiments that the proposed robust data-driven output feedback controller can significantly outperform a certainty equivalent controller on various measures of sample complexity and stability robustness. We make open-source code implementing the algorithms and experiments freely available.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The algorithm has three components: a subspace identification nominal model estimator; a novel semi-parametric bootstrap resampling method that quantifies non-asymptotic variance of the nominal model estimate; and a non-conventional robust control design method using an optimal linear quadratic coupled estimator-controller with multiplicative noise. This approach provides a natural interface between several highly effective methods from system identification, statistics, and optimal control theory (namely, subspace identification, bootstrap resampling, and robust control).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Formulation: Data-Driven Output Feedback Control", "weight": 1.0} -->

We consider data-driven control of the discrete-time linear dynamical system where x t ∈ R n is the system state, u t ∈ R m is the control input, y t ∈ R p is the measured output, and w t and v t are i.i.d. process and measurement noises with zero mean and covariance matrices W and V, respectively. The system matrices (A,B,C) and noise covariances (W,V) are grouped into the true model M = (A,B,C,W,V) which is assumed unknown. 1 Given only on a single training trajectory of finite length T of input-output data D T = (y train 0: T, u train 0: T -1) generated by the true system a data-driven input-output history-dependent control policy u t = π (y 0: t, u 0: t -1) is to be designed. We assume that the input signal that produced the training trajectory was persistently exciting to avoid identifiability issues (see Definition 5 of Van Overschee and De Moor).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Formulation: Data-Driven Output Feedback Control", "weight": 1.0} -->

The performance of an arbitrary policy π is characterized by the infinite-horizon time-averaged linear-quadratic output-input criterion 1. We assume the order n of the underlying system is known; future work will address systems with unknown order. where Y ≻ 0 and R ≻ 0 are penalty matrices, u t = π (y 0: t, u 0: t -1), the initial state x 0 is a random vector with zero mean and identity covariance independent of the noises w t and v t, and the expectation is taken with respect to the process and measurement noise sequences and the initial state. Notice that this formulation permits one to choose the output penalty Y ≻ 0, which can be specified even if the true underlying state x t and system model are unknown. The output-input performance criterion is equivalent, up to a shift by a problem-dependent constant, to a stateinput performance criterion with a penalty matrix Q = C ᵀ Y C ⪰ 0, such that so that minimization of H is tantamount to minimization of J, which is shifted by a positive constant Tr(Y V) that does not depend on the policy.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Formulation: Data-Driven Output Feedback Control", "weight": 1.0} -->

We focus on a sequential design pipeline, in which the data is first used to identify a system model ˆ M (D T) and then an output feedback control policy π ˆ M (D T) is designed based on the identified model; note that the identified model ˆ M (D T) is more generic and may have alternative or additional structure compared to the true model M. A linear dynamic compensator is a policy which combines a linear state estimator with a linear state estimate feedback in the form Such a compensator is fully specified by the triple (F, K, L), and the specification need not depend on the state x t or system matrices (A,B,C) of the underlying system.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation: Data-Driven Output Feedback Control", "weight": 1.0} -->

The optimal cost is the constant J ∗ = min π J (π) = J (π M), which is achieved when the true model M is known and used in the canonical linear quadratic Gaussian (LQG) control policy π M, a linear dynamic compensator with F = A + BK -LC and gain matrices (K,L) computed (separately) as the solution to two decoupled algebraic Riccati equations, which can be accomplished via several well-known methods such as the dynamic programming techniques of policy iteration and value iteration Bertsekas, convex semidefinite programming Boyd et al., and specialized direct linear algebraic methods Laub. Therefore, we restrict attention to the class of linear dynamic compensators.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Formulation: Data-Driven Output Feedback Control", "weight": 1.0} -->

Using a compensator (F, K, L), the closed-loop system dynamics become the autonomous stochastic difference equation Denote the following augmented closed-loop matrices The stability of the closed-loop system is characterized by the spectrum of the matrix Φ, namely if ρ (Φ) < 1 then the closed-loop system is stable in the sense that the covariance of the augmented state [x t ˆ x t] ᵀ converges to a finite positive definite matrix as t → ∞. With such stability, the steady-state value matrix P ′ and the steady-state covariance S ′ of [x ᵀ t ˆ x ᵀ t] ᵀ are found by solving the discrete-time Lyapunov equations With a slight abuse of notation, the performance criterion can be expressed and computed as Denote the performance criterion and closed-loop system matrix under a linear dynamic compensator (ˆ F T, ˆ K T, ˆ L T) designed with the T -step data record D T as J T = J (ˆ F T, ˆ K T, ˆ L T) from and Φ T, respectively.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Formulation: Data-Driven Output Feedback Control", "weight": 1.0} -->

The quantity of primary interest is J T J ∗ ∈ [1, ∞), which represents the normalized infinite-horizon performance at time T. Since the policy is computed based on a model identified from noisy finite data, the ratio J T J ∗ is a random variable. We are interested in its finite sample behavior and finiteness (which relates to stability robustness); in particular, we would like to know not only in how the mean or median scale with the data length T, but also how the upper tails scale. These properties depend on whether and how inherent uncertainty in the identified model is accounted for in the controller design. Certainty equivalent approaches ignore the model uncertainty altogether, which may lead to serious finite sample robustness issues. Here we aim to explicitly incorporate the model uncertainty in the controller design. In particular, we propose a robust data-driven output feedback control algorithm that explicitly accounts for finite-sample model uncertainty in an identified model using a multiplicative noise framework, estimated via the bootstrap.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Robust Control via Bootstrapped Multiplicative Noise", "weight": 1.0} -->

Our robust data-driven control algorithm is summarized in Algorithm 1, The algorithm has three main components: a subspace identification nominal model estimator; a bootstrap resampling method that quantifies non-asymptotic variance of the nominal model estimate; and a non-conventional robust control design method using an optimal LQG with multiplicative noise.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Algorithm 1 Robust Data-Driven Output Feedback Control", "weight": 1.0} -->

Input: single trajectory data D T = ( y train 0: T, u train 0: T -1 ), number of bootstrap resamples N b, model uncertainty scaling parameter γ, penalty matrices Y ≻ 0, R ≻ 0

<!-- chunk {"id": "body-0017", "role": "body", "section": "Subspace Identification for Nominal Model Estimation", "weight": 1.0} -->

The first component of the algorithm is a subspace identification algorithm to estimate the unknown system matrices from input-output trajectory data. Subspace identification algorithms have been developed and studied for several decades Van Overschee and De Moor. There are several variations, which all involve constructing block Hankel matrices from the data and estimating certain subspaces via singular value decompositions, from which the system matrices and noise covariances can be retrieved. Any of these can be used within the proposed framework, but for concreteness we use the so-called N4SID algorithm Van Overschee and De Moor. Based on the input-output data (y train 0: T, u train 0: T -1), the subspace identification algorithm produces a nominal estimate of the system state space matrices and the process and measurement noise covariances: Due to space constraints we refer readers to the literature, e.g. 'Combined Algorithm 1' in Chapter 4 of Van Overschee and De Moor, for details of the subspace identification algorithm.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Subspace Identification for Nominal Model Estimation", "weight": 1.0} -->

Due to non-uniqueness of state space representations, the system matrices are estimated within a similarity transformation of an underlying unknown representation. Based on the input-output data and the estimated system matrices, subspace algorithms generate residuals of the process and measurement noises { ˆ w τ } t -1 τ =0, { ˆ v τ } T -1 τ =0 from which sample average covariance estimates [ˆ W T ˆ U T ˆ U ᵀ T ˆ V T] are produced. Because the estimated system matrices (ˆ A T, ˆ B T, ˆ C T) do not share a state coordinate system with the true system matrices (A,B,C), even though the true cross-covariance between w t and v t is assumed zero, the cross-covariance of the estimates disturbances ˆ w t and ˆ v t may be non-zero and must be estimated and accounted for in the compensator design.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Bootstrap Resampling to Quantify Non-Asymptotic Model Uncertainty", "weight": 1.0} -->

There are inevitably errors in model estimates obtained from subspace identification using any finite data record, due to the process and measurement noises. It is difficult to analytically characterize non-asymptotic uncertainty in these estimates. Quantifying uncertainty in subspace identification estimates has been considered in Viberg et al.; Bauer et al.; Bauer and Jansson; Reynders et al., which focus on asymptotic results. Bootstrapping has been used to quantify non-asymptotic uncertainty in Bittanti and Lovera for input-output quantities such as frequency response or pole locations. However, to our best knowledge, these uncertainty quantifications have not been used for control design.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Bootstrap Resampling to Quantify Non-Asymptotic Model Uncertainty", "weight": 1.0} -->

To quantify non-asymptotic uncertainty in the model estimate, we propose a novel semi-parametric time series bootstrap resampling procedure. In semi-parametric methods, bootstrap data are simulated from the nominal model with the process and measurement noise sampled i.i.d. with replacement from residuals calculated with the nominal model H¨ ardle et al.. Dependence in the data is preserved by construction. There are also purely parametric and non-parametric versions of the bootstrap. Generally, the semi- and nonparametric bootstraps are less sensitive to assumptions about the model and the noise distribution, while the semi- and pure parametric bootstraps have better small sample performance when the model is correctly specified. The bootstrap resamples allow for various estimates of finite-sample uncertainty associated with the nominal model; here, we will utilize an estimate of the covariance of the model parameters. For concreteness, a semi-parametric bootstrap with resampled residuals discussed above is summarized in Algorithm 2.

<!-- chunk {"id": "body-0021", "role": "body", "section": "State-space Alignment", "weight": 1.0} -->

Due to non-uniqueness of state space representations, the uncertainty representation should not be obtained directly from a sample covariance of the bootstrap resamples. Instead, for each resample we first find a similarity transformation that minimizes the total squared error to the nominal state space model, and then compute a sample covariance in the transformed coordinates. Ideally, we would form and solve the following optimization problem which attempts to bring the source model (¯ A, ¯ B, ¯ C) as close to the nominal model (ˆ A, ˆ B, ˆ C) as possible by selecting the decision matrix T that defines the coordinate transformation. Notice that the coordinates of the nominal model (ˆ A, ˆ B, ˆ C) are treated as a ground truth to which the source model (¯ A, ¯ B, ¯ C) should be aligned; reversing their roles would yield a different, less meaningful transformation. The constants ψ A, ψ B, ψ C are user-selected to tune the relative weight of the alignment of A, B, and C. For simplicity these are set to unity; further tuning of these constants is left to future work.

<!-- chunk {"id": "body-0022", "role": "body", "section": "State-space Alignment", "weight": 1.0} -->

This problem has been referred to as the 'realization alignment' problem; however, as noted by Jimenez et al., there are several mathematical issues which complicate solving this problem to global optimality, including the non-compactness of GL (n) and nonconvexity of ˜ d. The approach developed in Jimenez et al. to address these issues is specialized to a certain class of LTI systems, namely those with C full column rank, which may not include the LTI systems which result from the subspace identification algorithm we use in this work, and is therefore not appropriate for the current setting.

<!-- chunk {"id": "body-0023", "role": "body", "section": "State-space Alignment", "weight": 1.0} -->

As an alternative, we use a slightly different objective which does not involve the inverse of the transform matrix T, and is in fact linear in the transform matrix T and is no longer constrained to GL (n): Another alternative is the dual problem where the inverse transform matrix T -1 is used as the decision variable instead. Notice that the solution of is the same as that of a problem of the form of with the roles of the target (ˆ A, ˆ B, ˆ C) and source (¯ A, ¯ B, ¯ C) models reversed. However, in general the solutions T to each of the problems, and are not the same; the choice between and is somewhat arbitrary, so we choose the former. The problem is unconstrained, smooth, and strictly convex; as such there is a unique global minimizer located at the stationary point where the derivative of the objective vanishes.

<!-- chunk {"id": "body-0024", "role": "body", "section": "State-space Alignment", "weight": 1.0} -->

Explicitly, the derivative of the objective can be found by expressing the objective in terms of the trace as then using standard matrix derivative rules e.g. Petersen and Pedersen to obtain the derivative Setting the derivative equal to zero yields a linear matrix equation in T, in fact a kind of generalized Lyapunov equation, which can be solved e.g. via vectorization and Kronecker products and solution of a linear vector equation: where G and H are the matrices It is assumed that G is invertible so that this equation is solvable and results in an invertible transformation matrix T. Then the transformed system matrices are computed as Note that in the special case when the nominal model (ˆ A, ˆ B, ˆ C) and the source model (¯ A, ¯ B, ¯ C) are related exactly by a similarity transformation, the solution T to the optimization problem is precisely this similarity transform, the optimal objective value is identically zero, and we obtain exact matching (˜ A, ˜ B, ˜ C) = (ˆ A, ˆ B, ˆ C). This coordinate alignment is incorporated into the model covariance estimation Algorithm 2.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Algorithm 2 Semi-parametric Bootstrap Model Covariance Estimation", "weight": 1.0} -->

Input: trajectory data ( y 0: t, u 0: t -1 ), nominal model estimate ( ˆ A t, ˆ B t, ˆ C t ), residuals { ˆ w τ } t τ =0, { ˆ v τ } t τ =0, number of bootstrap resamples N b

<!-- chunk {"id": "body-0026", "role": "body", "section": "Algorithm 2 Semi-parametric Bootstrap Model Covariance Estimation", "weight": 1.0} -->

- 4: Generate data ¯ x τ +1 = ˆ A t ¯ x τ + ˆ B t ¯ u τ + ˜ w τ, ¯ y τ = ˆ C t ¯ x τ + ˜ v τ, τ = 0,..., t -1, where ˜ w 0: t -1 and ˜ v 0: t -1 are i.i.d. resamples with replacement from residuals ˆ w 0: t -1 and ˆ v 0: t -1 Output: Bootstrap sample covariance ˆ Σ A t = 1 N b -1 ∑ N b k =1 vec (˜ A k t -ˆ A t) vec (˜ A k t -ˆ A t) ᵀ Bootstrap sample covariance ˆ Σ C t = 1 N b -1 ∑ N b k =1 vec (˜ C k t -ˆ C t) vec (˜ C k t -ˆ C t) ᵀ Bootstrap sample covariance ˆ Σ B t = 1 N b -1 ∑ N b k =1 vec (˜ B k t -ˆ B t) vec (˜ B k t -ˆ B t) ᵀ

<!-- chunk {"id": "body-0027", "role": "body", "section": "Multiplicative Noise LQG: Combined Controller and State Estimator", "weight": 1.0} -->

The model covariance estimate generated from bootstrap resampling interfaces quite naturally with a variant of the optimal linear quadratic output feedback controller that incorporates multiplicative noise, which has a long history in control theory but is far less widely known than its additive noise counterpart (Wonham; Bernstein and Greeley; De Koning; Gravell et al.). Consider the optimal control problem to find an output feedback controller u t = π (y 0: t) for dynamics perturbed by multiplicative noise where ¯ A t, ¯ B t, and ¯ C t are i.i.d. zero-mean random matrices with a joint covariance structure over their entries governed by the covariance matrices Σ A:= E [vec(¯ A) vec(¯ A) ᵀ] ∈ R n 2 × n 2, Σ B:= E [vec(¯ B) vec(¯ B) ᵀ] ∈ R nm × nm, Σ C:= E [vec(¯ C) vec(¯ C) ᵀ] ∈ R pn × pn which quantify uncertainty in the nominal system matrices (A,B,C).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Multiplicative Noise LQG: Combined Controller and State Estimator", "weight": 1.0} -->

The expectation is taken with respect to all of the basic random quantities in the problem, namely x 0, { ¯ A t }, { ¯ B t }, { ¯ C t }, { w t }, { v t }.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Multiplicative Noise LQG: Combined Controller and State Estimator", "weight": 1.0} -->

Due to the multiplicative noise, the state distribution is non-Gaussian even when all primitive distributions are Gaussian, so the Kalman filter is not necessarily the optimal state estimator. However, the optimal linear output feedback controller can be exactly computed, and consists of a multiplicative noise linear dynamic compensator of the form. In this case, there is no separation between estimation and control, so the optimal controller and estimator gains (K,L) must be jointly computed. Specifically, the optimal gains can be computed by solving the coupled nonlinear matrix equations in symmetric matrix variables X = (X 1, X 2, X 3, X 4) where { α i, A i } n 2 i =1, { β j, B j } nm j =1, and { λ j, C j } pn j =1 are the eigenvalues and reshaped eigenvectors of Σ A, Σ B, and Σ C, respectively, and The associated optimal cost is then given by These equations are solved using a value iteration algorithm, described in De Koning.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Multiplicative Noise LQG: Combined Controller and State Estimator", "weight": 1.0} -->

In the absence of multiplicative noise, they reduce to the familiar separated algebraic Riccati equations for optimal estimation and control. The solutions are denoted Both the optimal controller and estimator gains depend explicitly on the model uncertainty, as quantified by the variances of the system matrices, as well as the process and measurement noise covariances. This policy is known to provide robustness to uncertainties in the parameters of the nominal model (Bernstein and Greeley). Furthermore, the uncertainty in the nominal model estimate used in this control design method is richly structured and derived directly from the finite available data.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Multiplicative Noise LQG: Combined Controller and State Estimator", "weight": 1.0} -->

In the proposed data-driven control algorithm, we simply substitute the estimated nominal model and model covariance matrices obtained from the subspace identification and bootstrap methods into the multiplicative noise compensator design equations. We also introduce a parameter γ which provides a fixed scaling of the model uncertainty. Note that γ = 0 corresponds to certainty equivalent control, and as γ increases, more weight is placed on uncertainty in the nominal model. For γ ∈, this approach can be interpreted as shrinkage estimation of the model sample covariance matrices towards certainty equivalence Ledoit and Wolf. Existence of a solution to the generalized Riccati equation depends not just on stabilizability and detectability of the nominal system ( A,B,C ), but also on the mean-square stabilizability via dynamic output feedback of the multiplicative noise system (called mean-square compensatability in De Koning ). When the multiplicative noise variances are too large, it may be impossible to stabilize the system in the mean-square sense.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Multiplicative Noise LQG: Combined Controller and State Estimator", "weight": 1.0} -->

In this case, we scale down the model variances to compute a mean-square stabilizing dynamic output feedback controller; see Algorithm 3. In particular, we verify the system with specified γ is mean-square stabilizable by checking whether the generalized Riccati equation admits a positive semidefinite solution; if not, we find the upper limit γ max = c γ γ via bisection (e.g. Burden et al. ) on a scaling c γ ∈.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Algorithm 3 Multiplicative Noise LQG", "weight": 1.0} -->

Input: Nominal model matrices A, B, C, additive disturbance covariances W, V, U, penalty ma- trices Q, R, covariances Σ A, Σ B, Σ C, scaling γ, bisection tolerance ϵ > 0 1: Find largest c γ ∈ via bisection such that there exists a feasible solution to

<!-- chunk {"id": "body-0034", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Weexamined the following 2-state shift register with system, penalty, and noise covariance matrices where the output penalty was Y = 1 leading to the given value for Q = C ᵀ Y C. The first state stores the previous value of the second state, the second state is determined solely by the control input, and the output is the difference of the two states. This system is based on the one described in Recht, wherein it was shown that the system is extremely sensitive to model identification errors. In particular, despite the open-loop system being perfectly stable with zero eigenvalues, the system under optimal linear quadratic state feedback control is nearly unstable such that any small error in the estimated system matrices produce an unstable closed-loop system. Therefore, this system is likely to see a benefit from the proposed robust control synthesis approach.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The training data D T were generated by initializing the state at the origin, applying random controls distributed according to a Gaussian distribution with zero-mean and scaled identity covariance where the scaling was equal to the sum of the largest singular values of W and V (to ensure a sufficiently strong signal-to-noise ratio), and simulating the evolution of the state with the additive process and measurement noise specified by the problem data ( W,V ).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

For brevity, we abbreviate the control design schemes 'certainty-equivalent control' as 'CE' and 'robust control via multiplicative noise' as 'RMN'. To evaluate the performance of RMN relative to CE, we performed Monte Carlo trials to estimate the distribution of several key quantities: infinite-horizon performance, spectral radius of the closed-loop system, model error, and multiplicative noise variances. In each Monte Carlo trial, the actual additive noise disturbances w t, v t were drawn independently. The level of additive noise was significant enough that an appreciable number of model estimates remained poor for many timesteps, highlighting the behavior of CE and RMN in the critical high-uncertainty regime. We simulated the system and evaluated quantities for the trajectory lengths T ∈ { 20, 40, 80, 160, 320 } according to Algorithm 1; all of the trajectory lengths were sufficiently long to ensure the estimates in subspace identification were non-degenerate. We drew N s = 100, 000 independent Monte Carlo samples and N b = 100 bootstrap samples at each time step for uncertainty estimation.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We used unity scaling of the multiplicative noise ( γ = 1 ) and a tolerance of ϵ = 0. 01 for bisection to find the largest scaling c γ of multiplicative noise variance in the multiplicative noise LQG algorithm.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

From Figure 1 we see that for T = 20 the nominal model is fairly accurate but clearly misspecified, and that the bootstrap distribution of models captures the true deviation of the nominal model from the true system, as the true system parameters fall within the distribution of bootstrap samples. This is an accurate representative of the N s = 100, 000 Monte Carlo samples.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In Figure 2 we plot statistics of performance and spectral radius using both control schemes, while in Figure 3 we plot statistics of the differences between the performance and spectral radius. We are chiefly interested in the expected value and upper quantiles of performance, which correspond to average performance and risk of poor performance. We see that CE leads to both worse average behavior and riskier behavior as reflected by the distribution of the performance. In particular, we see that the performance of RMN is clearly better during times between T = 20 and T = 80, dropping at the 99th percentile from 2. 318 to 1. 077 whereas CE suffers 12. 091 to 1. 089. This can also be explained from the spectral radius, which is larger across all timesteps and statistics, corresponding to a less stable system. In particular, at the beginning between T = 20 and T = 80 when uncertainty is highest, RMN yields spectral radii at the 99th percentile that drop from 0. 903 to 0. 843 while CE yields 0. 985 to 0. 916, nearer to instability and allowing the state to travel far from the origin, resulting in high cost.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

With increasing T the model estimates improved and uncertainty estimates became sufficiently small that the difference between CE and RMN control was insignificant.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In Figure 4 we plot statistics of the nominal model estimate errors, which are applicable to both control schemes. We see that the nominal system matrices ˆ A, ˆ B, and ˆ C produced by the subspace identification algorithm approached the true parameters (after a suitable alignment transformation). This is mirrored by the decrease in the multiplicative noise variances, showing that the multiplicative noise variances accurately reflect the true model error, i.e., the bootstrap model uncertainty estimator gives reasonable estimates.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

From Figure 5 we see that at the very beginning when the uncertainty is extremely high, the multiplicative noise variance sometimes had to be reduced significantly in order to admit a solution to the generalized Riccati equation. Over time as the uncertainty decreased, the multiplicative noises were used with their native scaling almost all of the time.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Code which realizes the algorithms of this paper and generates the reported results is available.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We proposed a data-driven robust control algorithm that uses the bootstrap to estimate model estimate covariances and a non-conventional multiplicative noise LQG robust output feedback compensator synthesis to explicitly account for model uncertainty. Future work will go towards providing finite-time theoretical performance guarantees using tools from high-dimensional statistics and exploring alternative bootstrap uncertainty quantification schemes and robust control synthesis frameworks based e.g. on linear matrix inequalities and System Level Synthesis.
