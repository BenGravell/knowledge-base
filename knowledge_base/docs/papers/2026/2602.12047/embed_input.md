<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Safety beyond the Training Data: Robust Out-of-Distribution MPC via Conformalized System Level Synthesis

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a novel framework for robust out-of-distribution planning and control using conformal prediction (CP) and system level synthesis (SLS), addressing the challenge of ensuring safety and robustness when using learned dynamics models beyond the training data distribution. We first derive high-confidence model error bounds using weighted CP with a learned, state-control-dependent covariance model. These bounds are integrated into an SLS-based robust nonlinear model predictive control (MPC) formulation, which performs constraint tightening over the prediction horizon via volume-optimized forward reachable sets. We provide theoretical guarantees on coverage and robustness under distributional drift, and analyze the impact of data density and trajectory tube size on prediction coverage. Empirically, we demonstrate our method on nonlinear systems of increasing complexity, including a 4D car and a {12D} quadcopter, improving safety and robustness compared to fixed-bound and non-robust baselines, especially outside of the data distribution.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Provably-safe planning under unknown dynamics is crucial for real-world robotics. This poses difficulties for classical planners, which assume precise models; in practice, model error and uncertainty are unavoidable. Data-driven planners can learn dynamics from data but may exploit model inaccuracies, leading to unsafe behavior. This motivates uncertainty-constrained planners that quantify prediction error between true and learned dynamics to ensure robust, safe execution (DBLP:journals/ral/; DBLP:conf/icra/; wasiela2024learning). These methods estimate spatially-varying model error bounds to compute reachable tubes, which are used to constrain closed-loop behavior within a "trusted domain" where the model is accurate. This domain is typically selected as a bounded region around the training data, preventing generated plans from straying far from the data. However, in practice, data scarcity often forces robots to operate temporarily out of distribution (OOD), tolerating degraded performance while maintaining safety. Moreover, these planners are slow and do not exploit gradient information to efficiently optimize closed-loop behavior that actively reduces model uncertainty.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address these gaps, we propose CP-SLS-MPC, a fast optimization-based robust feedback motion planner that uses the learned dynamics to jointly plan open-loop nominal trajectories and closed-loop tracking controllers via robust model predictive control (MPC). Our method uses weighted conformal prediction (CP) to bound the model error and system level synthesis (SLS) (anderson2019system) to compute reachable sets, which are used to constrain the true closed-loop system to be safe with high probability, enabling robust temporary OOD operation. CP-SLS-MPC updates the model error bounds with online data to encourage cautious behavior when OOD, such as staying further from obstacles. CP-SLS-MPC also uses gradient data from a model error predictor to efficiently guide plans toward low-error regions, enabling near-real-time replanning. Our contributions are: A fast optimization-based MPC method with learned dynamics ensuring finite-sample, probabilistic safety of the true system using state-control-dependent CP error bounds in the MPC.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Theoretical analysis for high-probability safety and bounding the OOD coverage gap.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Numerical validation on a simulated nonlinear 4D car and 12D quadcopter, improving safety and prediction accuracy even in OOD scenarios over uncertainty-unware MPC baselines.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Predictive Control", "weight": 1.0} -->

Learning-based MPC unifies disturbance estimation with planning (hewing2020learning), but typically lacks state-dependent error bounds and cannot steer plans towards low-error regions. Robust (rawlings2017model) and tube MPC (mayne2005robust) ensure constraint satisfaction under disturbance, but in typical formulations, directly enforcing constraints on the closed-loop trajectory is nonconvex, leading to conservative overapproximations (singh2018robust). In contrast, SLS (anderson2019system; chen2024robust), or disturbance-feedback MPC (GOULART2006523), provides a convex parameterization of closed-loop responses for linear time-varying (LTV) systems, enabling constraint satisfaction under disturbance (bartos2025stochastic). SLS also extends to data-driven settings (xue2021data; furieri2022neural) and nonlinear dynamics (leeman2025robust_TAC), where the problem is decomposed into an optimization over nominal trajectories and closed-loop LTV error dynamics.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Predictive Control", "weight": 1.0} -->

In this work, we inform SLS with state-dependent, CP-calibrated error bounds to enable safe planning toward low-error regions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Planning with Learned Dynamics", "weight": 1.0} -->

Many model-based reinforcement learning methods plan with learned models but lack safety guarantees (DBLP:journals/ftml/). Some methods estimate reachable tubes for safe exploration (berkenkamp2016safe), but assume a controller is given. The most closely related method (DBLP:conf/cdc/; chou2022safe) safely plans with learned dynamics by constraining invariant tubes to lie in a "trusted domain" near training data. This demands dense data coverage; in contrast, we enable the robot to move beyond the training data while assuring probabilistic safety. Subsequent model error-aware planners (DBLP:conf/corl/) improve planning speed but lack formal guarantees. Also closely related is marques2024quantifyingaleatoricepistemicdynamics, which bounds model error via CP but cannot extrapolate OOD as it uses exchangeable CP. Other methods aim to improve dynamics predictions in OOD scenarios (DBLP:journals/corr/abs-2403-12245) but do not focus on planning.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Conformal Prediction (CP)", "weight": 1.0} -->

CP (vovk2005algorithmic) is a distribution-free method for constructing prediction regions from data from black-box models, making it well-suited for safe trajectory prediction and planning (DBLP:journals/ral/; DBLP:conf/l4dc/; DBLP:conf/nips/; DBLP:conf/cdc/; muenprasitivej2025probabilistically). The most closely related methods are DBLP:conf/l4dc/, which triggers a safe fallback policy in OOD scenarios for MPC, and DBLP:conf/cdc/; DBLP:conf/l4dc/, which use WCP to address time-series correlations in MPC for tracking fixed trajectories. However, these methods do not use state-dependent uncertainty, and form prediction sets using a fixed spatially-invariant norm ball. Thus, the MPC cannot distinguish between state-space regions where the model is accurate and those where it is inaccurate, thereby degrading performance.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Conformal Prediction (CP)", "weight": 1.0} -->

In contrast, our method designs trajectories that are valid OOD and actively encourages uncertainty reduction, steering the MPC toward regions of lower model error, using a learned state-dependent error covariance matrix.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Conformal Prediction (CP)", "weight": 1.0} -->

We use weighted CP to convert raw non-conformity scores, quantifying a mismatch between between $\hat{f}(x,u)$ and $f(x,u)$, into a calibrated threshold that yields $(1-\alpha)$ coverage (vovk2005algorithmic). Let $\mathcal{D}_{\mathrm{calib}}:={(x_{i},u_{i},f(x_{i},u_{i}))}_{i=1}^{n}$ and choose a nonconformity score function $s:\mathcal{X}\times\mathcal{U}\times\mathcal{X}\to\mathbb{R}_{\geq 0}$. Set $s_{i}:=s(x_{i},u_{i},f(x_{i},u_{i}))$. Calibration proceeds in three steps.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Conformal Prediction (CP)", "weight": 1.0} -->

We (i) form the weighted empirical distribution $\hat{S}$ with weights, $\{\tilde{w}_{1},\ldots,\tilde{w}_{n},\tilde{w}_{\textrm{test}}\}\subseteq^{n+1}$, where $\delta_{s_{i}}$ is the Dirac delta centered at $s_{i}$, (ii) calibrate the threshold $q_{1-\alpha}:=Q_{1-\alpha}(\hat{S})$ with the $1-\alpha$ quantile $Q_{1-\alpha}(\cdot)$, and (iii) define the conformal prediction set (CP set) at $(x_{\textrm{test}},u_{\textrm{test}})$ as Traditional (non-exchangeable) CP uses uniform weights,

<!-- chunk {"id": "body-0014", "role": "body", "section": "Conformal Prediction (CP)", "weight": 1.0} -->

$\tilde{w}_{i}=\tilde{w}_{\text{test}}=\frac{1}{n+1}$, and assumes exchangeability, which may fail under spatio-temporal distribution shifts; WCP does not assume this.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Conformal Prediction (CP)", "weight": 1.0} -->

We denote $(s_{1},s_{2},\ldots,s_{\textrm{test}})\sim S^{\textrm{test}}$; moreover, let $S^{i}$ be the joint distribution obtained by replacing $s_{i}$ with the unknown test score, i.e., $(s_{1},s_{2},\ldots,s_{i-1},s_{\textrm{test}},s_{i+1},\ldots,s_{n})\sim S^{i}$. WCP guarantees where $d_{\textrm{TV}}(\cdot)$ is the total-variation distance and $\textstyle\sum_{i=1}^{n}\tilde{w}_{i}d_{\textrm{TV}}(S^{i},S^{\textrm{test}})$ quantifies the coverage gap due to distribution shift (it vanishes under exchangeability).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Conformal Prediction (CP)", "weight": 1.0} -->

In practice, the weights can be selected to trade off coverage gap size $\sum_{i}\tilde{w}_{i}d_{\textrm{TV}}(S^{i},S^{\textrm{test}})$ and CP set size $|\mathcal{C}(x_{\textrm{test}},u_{\textrm{test}};q_{1-\alpha})|$, yielding uncertainty sets suitable for robust MPC with learned dynamics. WCP is essential for planning with learned dynamics to account for distribution shifts between training and execution data, state/control correlations during execution, and visits to OOD regions of the state/control space.

<!-- chunk {"id": "body-0017", "role": "body", "section": "SLS", "weight": 1.0} -->

SLS (anderson2019system) is a robust control framework for uncertain LTV systems where $A_{k}\in\mathbb{R}^{n_{x}\times n_{x}}$, $B_{k}\in\mathbb{R}^{n_{x}\times n_{u}}$, and $E_{k}\in\mathbb{R}^{n_{x}\times n_{x}}$, and $\xi_{k}\in\mathcal{B}^{n_{x}}$ is a disturbance. SLS can be used to jointly optimize a nominal trajectory, a tracking controller, and a closed-loop reachable tube overapproximation computed by propagating worst-case disturbances over time.

<!-- chunk {"id": "body-0018", "role": "body", "section": "SLS", "weight": 1.0} -->

To track the nominal $(\textbf{z},\textbf{v})$, SLS defines a disturbance-feedback controller and closed-loop state response, where $\bm{\Phi}^{\mathrm{u}}_{k,j}\in\mathbb{R}^{n_{u}\times n_{x}}$ and $\bm{\Phi}^{\mathrm{x}}_{k,j}\in\mathbb{R}^{n_{x}\times n_{x}}$ define the closed-loop response of as an affine function of $\{\xi_{k}\}$, To ensure that - represent the closed-loop state/control response, $\bm{\Phi}^{\mathrm{x}}_{k,j}$ and $\bm{\Phi}^{\mathrm{u}}_{k,j}$ must satisfy With SLS, we can guarantee that the closed-loop trajectories of and remain in the reachable tubes

<!-- chunk {"id": "body-0019", "role": "body", "section": "SLS", "weight": 1.0} -->

To robustly satisfy nonlinear constraints of the form, we can enforce the tightened constraints, obtained by linearizing $g_{i}$, for all $i\in\{1,\ldots,n_{c}\}$, around the nominal trajectory: where $g_{i}^{\textrm{lin}}(z_{k},v_{k})$ is a linearization error bound term (details are omitted for brevity; see (zhan2025robustly, Eq.)). This ensures that the closed-loop dynamics satisfy for all $k\in\{1,\ldots,T\}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Our goal is to 1) estimate calibrated error bounds on the learned dynamics $\hat{f}$ that hold with high probability and to 2) use these bounds within a robust MPC framework, with a prediction horizon of $T$ steps, to guarantee robust constraint satisfaction with high probability. Specifically, we solve: Problem 1: Learning and Calibration. Using $\mathcal{D}_{\textrm{train}}$, learn an approximate dynamics model $\hat{f}:\mathcal{X}\times\mathcal{U}\rightarrow\mathcal{X}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Here, $\alpha\in$ is user-specified and $\tilde{\alpha}\in\alpha,1)$ absorbs the coverage gap in ([5 ‣ 3 Preliminaries and Problem Statement ‣ Safety Beyond the Training Data: Robust Out-of-Distribution MPC via Conformalized System Level Synthesis")).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Problem 2: Planning. Using the learned model $\hat{f}$ and error bound $\mathcal{E}$ of Prob. 1, solve a robust MPC problem for $\hat{f}$ ensuring that the constraints are satisfied for the true closed-loop dynamics (i.e., under $f$ in ) with probability at least $1-\tilde{\alpha}$, jointly over $T$ prediction steps, for a single MPC solve, and with probability at least $1-\hat{\alpha}$ for $R$ MPC solves (i.e., $R-1$ replanning steps), where $\hat{\alpha}\in(\tilde{\alpha},1)$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Method", "weight": 1.0} -->

We outline our method, CP-SLS-MPC, which uses WCP for high-probability state-control-dependent model error bounding (Sec. 4.1) and integrates it into an uncertainty-constrained SLS-based robust MPC optimization (Sec. 4.2). Finally, we discuss practical implementation (Sec. 4.3).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Model Training and Model Error Bounding via Conformal Prediction", "weight": 1.0} -->

To tackle Prob. 1, we first train the dynamics $\hat{f}$ on the training dataset $\mathcal{D}_{\textrm{train}}$ by minimizing a mean-squared-error loss $\textstyle\sum_{k=1}^{N_{\textrm{train}}}\|f(x_{k},u_{k})-\hat{f}(x_{k},u_{k})\|_{2}$. Then, for any nominal state $z\in\mathcal{X}$ and control input $v\in\mathcal{U}$, we seek to bound the error of the learned dynamics model $\|\hat{f}(z,v)-f(z,v)\|_{2}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Model Training and Model Error Bounding via Conformal Prediction", "weight": 1.0} -->

To encode spatially-varying error, we train a heuristic uncertainty model $\mathbf{\Sigma}:\mathcal{X}\times\mathcal{U}\to\mathbb{R}^{n_{x}\times n_{x}}$, an NN, with a multivariate Gaussian negative-log-likelihood (MGNLL) loss (dasgupta2007line): MGNLL is selected to train $\mathbf{\Sigma}$ to output an uncalibrated covariance matrix which locally approximates the shape and magnitude of $\hat{f}$'s error dispersion at a given state-control pair. WCP's calibration procedure reconciles the inexact gaussian assumption (of MGNLL) made of the error dispersion by scaling the covariance matrix.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Model Training and Model Error Bounding via Conformal Prediction", "weight": 1.0} -->

Intuitively, $\mathcal{C}(z_{k},v_{k};{q_{1-\alpha_{k}}})$ is an ellipsoid centered at the predicted next state $\hat{f}(z_{k},v_{k})$, with a radius given by the quantile of the weighted non-conformity scores.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Informing SLS-based Planning with CP Model Error Bounds", "weight": 1.0} -->

Since $\hat{f}$ is more accurate in the training domain, we modify $J(\mathbf{z},\mathbf{v})$ to include an active error reduction cost $J_{\mathrm{active}}(\mathbf{z},\mathbf{v})$ (see App. D.4) minimizing the distance of $(\mathbf{z},\mathbf{v})$ to in-distribution calibration points. Constraint (21b) ensures nominal dynamic feasibility, while (21c) and (21d) enforce SLS conditions for the LTV approximation obtained by linearizing $\hat{f}$ around $(\mathbf{z},\mathbf{v})$, with model error bound $V(z_{j},v_{j})$. Constraint (21e) enforces robust state-control satisfaction using bounds on the closed-loop response derived by informing SLS with CP.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Informing SLS-based Planning with CP Model Error Bounds", "weight": 1.0} -->

Since SLS guarantees an overapproximation of the true reachable tube, the closed-loop trajectory executing $(\mathbf{z},\mathbf{v},\bm{\Phi}^{\mathrm{x}},\bm{\Phi}^{\mathrm{u}})$ over the $T$-step horizon satisfies with high probability, and safety is maintained with high, though diminishing, probability over iterative replanning steps. The following result addresses Prob.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Practical Implementation via SCP", "weight": 1.0} -->

To efficiently solve the NLP, we propose CP-SLS-MPC (Alg. 1). CP-SLS-MPC uses sequential convex programming (SCP) (malyuta2022convex; messerer2021survey). Each SCP iteration solves a second-order cone program (SOCP) (Alg. 1, line 6), obtained by linearizing $\hat{f}$ around the current nominal trajectory $(\textbf{z},\textbf{v})$ and convexifying the constraint tightenings in (21e), yielding an update $(\mathbf{z}_{\textrm{lin}}^{*},\mathbf{v}_{\textrm{lin}}^{*})$ to the nominal trajectory.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Practical Implementation via SCP", "weight": 1.0} -->

To solve this SOCP efficiently, we use the solver in leeman2024fast, which iterates between solving a QP for $(\mathbf{z},\mathbf{v})$ and Riccati recursions for $(\bm{\Phi}^{\mathrm{x}},\bm{\Phi}^{\mathrm{u}})$ (line 7). For efficiency, we apply a real-time iteration scheme (Gros02012020), limiting SCP to one iteration per step (leeman2025guaranteed), and omit linearization error (zhan2025robustly), which is small in practice (Sec. 6). At each step, we execute the first control input $v_{1}$ (line 9), shift the previous solution for initialization (line 5), and re-solve via SCP. Moreover, we improve OOD robustness by updating the error set $\mathcal{V}$ with online observations (line 10).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Practical Implementation via SCP", "weight": 1.0} -->

Augmenting the error set updates the quantile $q_{1-\alpha_{k}}(z_{k},v_{k})$, which in turn alters constraint (21d) via, reducing the coverage gap and increasing the likelihood that the closed-loop dynamics remain within the computed reachable tubes.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Practical Implementation via SCP", "weight": 1.0} -->

1:procedure CP-SLS-MPC(𝒟calib, horizon T, ℱ, x̄0, terminal set 𝒳f) 2: t ← 1 and (z, v)← Nominal Solution ⊳ Initialize the problem with start state x̄0 3: 𝒱 ← {(xi, ui, f(xi, ui) − f̂(xi, ui))}i = 1Ncalib, ∀(xi, ui, f(xi, ui)) ∈ 𝒟calib ⊳ Initialize error set 𝒱 4: while xt ∉ 𝒳f do ⊳ 𝒳f is included as a terminal cost, App D.3 5: x̄0 ← xt; initialize (z, v) with shifted previous solution ⊳ Initialize with the current state 6: Linearize around (z, v); compute V(zk, vk) via, 𝒱; form SOCP 7: (zlin*, vlin*), Φx, Φu← SOCP solution ⊳ Single iteration of leeman2024fast. 8: Update (z, v) ← (z, v) + (zlin*, vlin*).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Practical Implementation via SCP", "weight": 1.0} -->

9: ut ← v1; xt + 1 ← f(xt, ut) ⊳ Closed loop control; state update 10: 𝒱 ← 𝒱 ∪ {(xt, ut, xt + 1 − f̂(xt, ut))}; t ← t + 1 ⊳ Online data update

<!-- chunk {"id": "body-0034", "role": "body", "section": "Theoretical Analysis: Bounding the Coverage Gap", "weight": 1.0} -->

To bound the coverage gap, we assume non-conformity scores from the calibration set $\mathcal{D}_{\mathrm{calib}}$ are independent of the score at the nominal point $(z_{k},v_{k})$, though they may come from different distributions. We also assume a Lipschitz-type bound on the distribution drift between ${S_{i,k}}$ and $S_{k,k}$, i.e., for $\epsilon\in\mathbb{R},\epsilon>0$, where $s_{i}\sim S_{i}$ and $\tilde{S}$ is the non-conformity score distribution of $(z,v)$. is a practical assumption, stating that the dynamics error distribution shifts gradually over the state-control space. The next theorem shows a overbound on the calibration error $d_{\textrm{TV}}(S_{i,k},S_{k,k})$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Results", "weight": 1.0} -->

We evaluate our method on robust planning with learned 4D Dubins' (see App. B.1) and 12D quadcopter dynamics (see App. B.2). Comparisons (see App. C for details) include naïve, uncalibrated MPC on the learned dynamics $\hat{f}$ without robust constraint tightenings, denoted as vanilla MPC (V-MPC), and a fixed hyper-ball variant of our method (CP-Ball), where $\mathbf{\Sigma}(z_{k},v_{k})$ in is replaced with $I_{n_{x}}$, highlighting the benefit of state-dependent CP-Ellipsoid (our method) uncertainty sets. CP-Ball is an adaptation of DBLP:conf/l4dc/, using the L2-norm of errors as the non-conformity score. Direct use of DBLP:conf/l4dc/ was not feasible, as it only collects online data points, requiring horizon lengths longer than 150 points for successful deployment. Training details, model architectures, and cost functions are in App.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Results", "weight": 1.0} -->

D. Our implementation uses Acados (verschueren2020acadosmodularopensourceframework) and L4CasADi (salzmann2024l4casadi) and is run on an M4 Pro MacBook (12 cores, 24 GB RAM). We report average MPC step time, prediction error $|f(x,u)-\hat{f}(x,u)|$, and minimum obstacle distance. All trials use horizon $T=15$ with $\alpha_{k}=0.1/15$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Dubins': In Domain (ID)", "weight": 1.0} -->

First, we validate that our approach maintains performance compared to baselines in ID scenarios without a major loss of computational efficiency. We used the car dynamics in and selected start and goal states training distribution (equivalently the feasible set for the ID results). We define $\mathcal{F}=\{(x,u)\mid p_{x}\,p_{y}\,\|[p_{x},p_{y}]^{\top}-[2.5,0]\|_{2}\geq 1\}$, Figure 2: Friction Car. We plot all approaches and forecasted MPC steps & tubes for CP-Ellipsoid. with bounds on $p_{x}$ and $p_{y}$ and a 1-m radius obstacle centered at $(2.5,0)$. Across 10 runs, all three approaches (V-MPC, CP-Ball, and CP-Ellipsoid) safely reached the goal while avoiding the obstacle; however, V-MPC does not perform constraint tightening and lacks safety guarantees.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Dubins': In Domain (ID)", "weight": 1.0} -->

In Table 1, CP-Ball and CP-Ellipsoid have larger obstacle proximity--a byproduct of the constraint tightening (Table 1). Finally, the one-step prediction error for $\hat{f}$ remains inside the ball and ellipsoid over $99.33\%=100(1-\frac{0.1}{15})\%$ during execution--validating the coverage guarantees (Fig. 8 in App. F). In the training domain, we expect V-MPC to have similar success rates as our method since $\hat{f}$ is accurate; this changes in OOD settings. We find that our approach avoids the obstacle ID, without a major slowdown from constraint tightening computations.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Dubins': OOD", "weight": 1.0} -->

To evaluate OOD performance, we train a dynamics and uncertainty model where $p_{y}\in\cup$ and modify the dynamics to steer the car's angle toward the obstacle for $p_{y}\in$ (see App. B.1), while placing the feasible set of the rollout (same as the ID experiment) OOD. In this setting, we vary the calibration set size from 2,250 to 4,250 points (Fig. 1) for CP-Ellipsoid, ensuring the start and goal are outside the training domain.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Dubins': OOD", "weight": 1.0} -->

As shown in Fig. 1, the one-step prediction errors initially lie outside the predicted ellipsoid but gradually return within it as online calibration points are collected. Moreover, with fewer initial calibration points, the online adaptation occurs more rapidly, resulting in a higher coverage of errors in the ellipsoid. The plot also shows that the one-step tubes in $\theta$ are wider for smaller $\mathcal{D}_{\mathrm{calib}}$, indicating that data scarcity increases conservativeness. The goal is reliably reached, suggesting that the SLS tubes, when informed by CP, enable robust OOD performance.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Dubins': Disjoint Training Domains (Friction Car)", "weight": 1.0} -->

To evaluate OOD obstacle avoidance under limited online data, we construct disjoint training regions (similar to the OOD setup) where $p_{y}\in\cup$. The start and goal positions are randomly sampled from different regions, ensuring that all feasible trajectories must traverse OOD areas to reach the goal. In the OOD region, we apply the same steering modification as in the previous experiment, while adding $p_{y}$ dependent acceleration dynamics (see App. B.1 for details). Across 10 runs, V-MPC failed twice, the CP-Ball failed once, and CP-Ellipsoid was consistently successful. These differences arise from reduced obstacle clearance (Table 1) observed in the CP-Ball and V-MPC cases. Fig. 3 shows that both CP-Ball and CP-Ellipsoid reach the goal, but CP-Ellipsoid maintains a greater distance from the obstacle, as evident from its forecasted trajectories and uncertainty tubes. Fig. 3 also illustrates that the state-dependent ellipsoids expand along the direction of motion, as increased forecasted $y$-motion leads to higher $y$-direction uncertainty.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Dubins': Disjoint Training Domains (Friction Car)", "weight": 1.0} -->

A result from an extra run is in App. F.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Dubins': Active Uncertainty Reduction", "weight": 1.0} -->

Finally, to evaluate active uncertainty reduction, we trained $\hat{f}$ and $\mathbf{\Sigma}$ without sampling data in a circular region centered at $(p_{x},p_{y})=(2.5,0.0)$ with a radius of 1 meter, and introduced friction and attractive steering dynamics within this unseen region. Thus the feasible set contains an OOD region, where rollouts are permitted to traverse. Despite this, the active uncertainty reduction method achieves lower prediction error by planning a longer path that remains in the training domain (Table 2 App. F). Moreover, Fig. 3 shows the log-volume of the uncertainty tubes, showing that the active uncertainty cost ( in App. D.4) yields smaller tubes (Fig. 3, green) compared to the baseline without this cost (Fig. 3, orange).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Dubins': Active Uncertainty Reduction", "weight": 1.0} -->

Min. Obstacle Dist. (m) Table 1: Mean and standard deviation of computation times and prediction errors and the mean minimum obstacle distance for vanilla-MPC (V-MPC), the CP-Ball (Ball), and CP-Ellipsoid (Ellipsoid).

<!-- chunk {"id": "body-0045", "role": "body", "section": "12D Quadcopter", "weight": 1.0} -->

To evaluate the scalability of our method to higher-dimensional systems, we train a 12D quadcopter dynamics model. Using this model, we plan trajectories such that the spatial coordinates $(p_{x},p_{y},p_{z})$ remain outside a sphere centered at $(2.5,2.5,2.5)$ with a radius of 0.8 meters -- leaving a 0.2-meter-thick shell around the sphere that is out of distribution and characterized by increased downward acceleration. To improve the performance of the uncertainty model, we modify its weighting by blending the covariance matrix with the identity matrix to reduce conservativeness, i.e., using $((1-\tau)I+\tau\mathbf{\Sigma}(z,v))$ instead of $\mathbf{\Sigma}(z,v)$. With this approach, the CP-Ellipsoid method successfully planned 8 out of 10 trajectories (one failure was due to numerical instability, which did not result in collision), whereas V-MPC approach succeeded in only 4 out of 10 runs.

<!-- chunk {"id": "body-0046", "role": "body", "section": "12D Quadcopter", "weight": 1.0} -->

While this demonstrates improved robustness over V-MPC, the failed case suggests faster tube expansion may be necessary to ensure consistent collision avoidance. Fig. 4 shows an example quadcopter trajectory, demonstrating that our CP-informed tubes maintain safe obstacle proximity.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we developed an efficient framework for robust out-of-distribution MPC with learned dynamics, using WCP and SLS. We provided theoretical guarantees ensuring that the rollout satisfy constraints with high probability, and introduced an uncertainty reduction cost function to encourage the system to remain within the training domain when possible. Through experiments on variants of the 4D Dubins car and 12D quadcopter, we demonstrated that the CP-SLS-MPC framework achieves robust performance even when using learned dynamics that generalize poorly OOD. \\acksWe thank Devesh Nath for insightful discussions and feedback on this work.
