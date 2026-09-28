<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Uncertainty quantification from finite data is central to machine learning, optimization, and automation systems, where decisions must remain reliable under limited samples and test-time distribution shift. Conformal prediction (CP) and distributionally robust optimization (DRO) offer two complementary approaches: CP constructs data-dependent prediction sets with distribution-free finite-sample validity under exchangeability, while DRO optimizes worst-case performance over an ambiguity set around an empirical distribution. We develop a unified probabilistic perspective on CP and DRO by viewing both as ways to turn finite calibration data into a data-dependent quantile estimator that a test score falls below with high probability. From this perspective, CP and DRO correct the empirical quantile along two coordinates of the same family of estimators: CP inflates the quantile level, whereas DRO shifts the quantile value through an ambiguity radius. Both methods provide the same calibration-conditional guarantee for the true distribution, requiring the target coverage to hold with high probability over the calibration sample.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Their constructions differ, however: CP uses a closed-form, distribution-free level correction, while DRO uses a value-space correction whose certified radius depends on properties of the unknown distribution and additionally guarantees coverage uniformly over the ambiguity set. This distinction emerges in the tails of the score distribution. Because CP relies on sparse upper-tail order statistics of the calibration samples, its level inflation barely moves the estimator when those samples are dense near the target quantile but overshoots when they are sparse, whereas a well-chosen DRO radius corrects in value space and may avoid this overshoot.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Modern applications in machine learning, robotics, and decision-making increasingly rely on data-driven methods. A fundamental challenge in these settings is to *quantify uncertainty using a finite set of samples*. Conformal prediction (CP) addresses this by constructing prediction sets with finite-sample distribution-free coverage guarantees under mild assumptions, such as data exchangeability. Distributionally robust optimization (DRO) instead optimizes worst-case performance over an ambiguity set of distributions, centered at the empirical distribution, yielding decisions that remain robust under distributional shift. CP and DRO originate from different communities and employ different problem formulations, leading to distinct methodologies, guarantees, and trade-offs. Nevertheless, both approaches can provide finite-sample high-coverage statistical guarantees from i.i.d. data.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Consider a set of calibration samples and a test sample drawn from the same unknown distribution, each assigned a scalar score. The goal is to construct a threshold from the calibration scores such that the test score falls below it with a target probability. Under *marginal* validity, this probability is taken jointly over the calibration and test samples. The target coverage then holds on average over possible calibration sets, but need not hold for the particular set observed. In contrast, *calibration-conditional* validity requires the target coverage to hold for the calibration set actually drawn. Because a finite calibration sample does not fully characterize the tail of the underlying distribution, this cannot hold for every calibration set, and one instead requires it to hold for all but a small fraction of them. We call the resulting statement a *two-level* guarantee: one level is the target coverage for the test sample, and the other is the confidence with which that coverage holds over the random calibration set.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper presents a comparative study of CP and DRO in the context of uncertainty quantification. We summarize their theoretical formulations, statistical properties, finite-sample behaviors, and provide side-by-side comparisons of coverage guarantees, conservativeness, and numerical performance. Our contributions are summarized as follows.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop a unified probabilistic perspective on CP and Wasserstein DRO by formulating both as finite-sample data-dependent quantile-estimation methods with calibration-conditional coverage guarantees.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the absence of test-time distribution shift, we connect CP and DRO through data-dependent quantile estimation: CP inflates the empirical quantile level, whereas DRO adds a value-space ambiguity radius. Both provide the same calibration-conditional guarantee for the true distribution, while DRO additionally certifies coverage uniformly over the realized ambiguity set. We further characterize their finite-sample and asymptotic behavior and explain how the score density near the target quantile affects conservativeness.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Under test-time distribution shift, we compare CP and DRO using shift models based on Wasserstein and Lévy--Prokhorov distances. We derive both CP and DRO estimators with calibration-conditional two-level guarantees and show how value-space and quantile-level corrections account for different forms of distribution shift.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We illustrate our theoretical findings on three representative tasks: image classification, multiple-choice question answering, and autonomous-driving trajectory prediction. The experiments compare the empirical coverage and conservativeness of CP and DRO estimators, assess satisfaction of the calibration-conditional two-level guarantees, and evaluate their robustness under distribution shift.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper aims to provide theoretical basis and practical guidance for selecting uncertainty-quantification methods in machine learning and decision-making from finite data.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Conformal prediction", "weight": 1.0} -->

CP addresses uncertainty quantification when the data-generating distribution is unknown. Instead of relying on parametric assumptions, CP constructs prediction sets or intervals that achieve finite-sample coverage guarantees under the mild assumption of data exchangeability. The idea originates from and was reformulated for regression problems, whose split-conformal construction underlies most modern use. Beyond this marginal-validity perspective, Vovk studied several notions of conditional validity for conformal predictors. Two are particularly relevant here. The first conditions on the training data, referred to as *training-conditional validity*, and corresponds to what we call calibration-conditional validity in this paper; Bian and Barber characterize when such guarantees are attainable. The second conditions on the test input, for which exact distribution-free guarantees are generally unattainable. Requiring coverage conditional on arbitrary subsets of the input space can lead to highly conservative prediction sets, whereas meaningful guarantees can be recovered over suitably restricted classes of conditioning sets. Conformalized quantile regression seeks to improve conditional adaptivity in practice by producing intervals whose widths adapt to input-dependent noise, or heteroscedasticity, while retaining marginal coverage. The results above assume exchangeability between calibration and test data.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Conformal prediction", "weight": 1.0} -->

A separate line of work relaxes this assumption, including methods for covariate shift with a known likelihood ratio and bounds on the coverage gap under departures from exchangeability. Angelopoulos et al. provide a unified theoretical treatment of conformal prediction that also covers distribution-shift settings. Several seminal works have established CP as a popular tool for reliable uncertainty quantification in machine learning, control, and autonomous systems.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Conformal prediction", "weight": 1.0} -->

In machine learning, CP offers a model-agnostic approach for converting model outputs into finite-sample calibrated prediction sets. Angelopoulos et al. developed CP-based uncertainty sets for image classification that remain valid while being substantially more compact than standard calibration baselines, and extended CP to federated learning by introducing a weaker notion of partial exchangeability suited to heterogeneous clients. In high-stakes applications, such as clinical imaging, highlighted the growing role of subgroup-adaptive CP coverage for fairer uncertainty quantification. More recently, CP has been adapted to large language models for multiple-choice question answering, generative language modeling, and improved validity guarantees for LLM outputs through enhanced conformal inference procedures.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Conformal prediction", "weight": 1.0} -->

CP has also been increasingly adopted in control, where it converts model and prediction uncertainty into finite-sample certificates for constraint satisfaction, safety, and verification. It has been used for distribution-free optimal control of linear stochastic systems and to quantify and robustify the uncertainty of model-based controllers. CP has further been embedded in stochastic model predictive control and in perception-based control under sensor uncertainty. Furthermore, it has been paired with high-level specifications and verification, including signal temporal logic control, conformal predictive programming for chance-constrained optimization, safety filters for reinforcement learning, and runtime verification of autonomous systems.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Conformal prediction", "weight": 1.0} -->

CP has also been applied in autonomous systems and robotics to convert model predictions into finite-sample calibrated uncertainty sets for planning, safety assurance, and interaction. Lindemann et al. incorporated CP into MPC-based safe planning in dynamic environments by calibrating trajectory-prediction uncertainty, while used CP to quantify uncertainty in diffusion dynamics models for uncertainty-aware planning. Luo et al. leveraged conformal calibration to obtain sample-efficient safety assurances with guaranteed false-negative rates, and extended this perspective from set prediction to direct calibration of autonomous decisions. Seo et al. used CP to calibrate epistemic-uncertainty thresholds in latent safety filters for avoiding out-of-distribution failures in robot navigation and manipulation. In human-robot interaction, used set-valued intent prediction to achieve risk-calibrated interaction under uncertain human intent.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Distributionally robust optimization", "weight": 1.0} -->

DRO addresses optimization under uncertainty by assuming that the true distribution lies within a specified family of distributions, known as an *ambiguity set*. This is a stronger assumption than that required by CP: CP relies only on exchangeability between calibration and test data, whereas DRO requires an ambiguity set that contains the true distribution, whose construction from finite data generally requires additional distributional assumptions. DRO then optimizes against the worst-case distribution in this set, providing robustness to finite-sample estimation error and distribution shift. Typical ambiguity sets are defined through moments, statistical divergences such as Kullback--Leibler distance, or probability metrics such as the Wasserstein distance. Among these, Wasserstein DRO has become particularly influential because it often combines computational tractability with finite-sample guarantees. Notably, Mohajerin Esfahani and Kuhn developed a data-driven Wasserstein DRO formulation with rigorous out-of-sample guarantees when the true distribution is unknown. Two questions are central to this formulation: how to evaluate the worst case over the ambiguity set, and how to choose the size of the set.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Distributionally robust optimization", "weight": 1.0} -->

Strong-duality results address the first by replacing the infinite-dimensional optimization over distributions with a tractable dual problem. Concentration results for the empirical measure address the second by specifying the radius of a Wasserstein ambiguity ball that contains the true distribution with prescribed confidence. Comprehensive treatments are given. These properties have made DRO an increasingly important tool in machine learning, control, and robotics, where uncertainty is often data-driven.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Distributionally robust optimization", "weight": 1.0} -->

In machine learning, DRO has been used both for robust training and for understanding existing learning objectives. Blanchet et al. showed that several standard estimators, including LASSO and logistic regression, can be recast as Wasserstein DRO problems, revealing a connection between robustness and regularization. Building on this perspective, developed a distributionally robust learning framework under Wasserstein ambiguity sets, encompassing regression, classification, and sequential decision-making problems. Chen and Paschalidis showed that Wasserstein DRO yields tractable formulations with guarantees against adversarial outliers. Gao provided finite-sample guarantees for broad classes of Wasserstein DRO learning problems without suffering from the curse of dimensionality, showing that the ambiguity radius balances empirical loss against loss variation. More recently, interpreted contrastive representation learning through the lens of DRO, showing that its training objective implicitly performs worst-case optimization over negative samples and using this to explain robustness to sampling bias.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Distributionally robust optimization", "weight": 1.0} -->

In control, DRO has been used to design controllers that are robust to distributional uncertainty in disturbances, dynamics, and constraints. One line of work builds data-driven ambiguity sets with finite-sample guarantees for control, in cooperative and time-varying settings, and applies them to stochastic optimal control and to safe and stable control synthesis via robust barrier and Lyapunov certificates. DRO has been used in model predictive control to provide closed-loop guarantees, recursive feasibility from data with total-variation and tube-based formulations. DRO has also been impactful in power and energy systems, where distributionally robust chance constraints bound constraint-violation risk under the unknown distribution of renewable generation and load, with applications to optimal power flow and economic dispatch.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Distributionally robust optimization", "weight": 1.0} -->

In autonomous systems and robotics, DRO has been used to make planning and control robust to uncertainty in state estimation, perception, and environment models and changes. Summers proposed a distributionally robust sampling-based planner that accounts for localization, dynamics, and obstacle uncertainties through worst-case risk allocation, while developed a rapidly exploring random tree algorithm that leverages Wasserstein ambiguity sets to provide finite-sample probabilistic safety guarantees in uncertain obstacle environments. Boskos et al. proposed a distributionally robust coordination algorithm to achieve optimal deployment of a multi-agent system, responding to events of interest with unknown probability distribution. Xu et al. incorporated Wasserstein distributionally robust chance constraints into safe-corridor trajectory optimization and derived a convex quadratic reformulation. DRO has also been increasingly applied to safe navigation under uncertainty, including sensing and localization errors, uncertain obstacle and pedestrian motion, and uncertainty from learned perception or environment models.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Unified perspective", "weight": 1.0} -->

Recent work has started to connect CP and DRO. Cauchois et al. developed a robust validation approach that uses CP-style prediction sets to guarantee coverage over an $f$-divergence ambiguity set around the source distribution, thereby linking distribution shift robustness to worst-case coverage control. Aolaritei et al. further developed a distributionally robust form of CP under Lévy-Prokhorov ambiguity sets, showing how local and global perturbations of the test distribution can be propagated through conformity scores to characterize worst-case quantiles and coverage. Guo utilized CP in a DRO formulation by centering the DRO ambiguity set at a fitted predictive distribution, rather than the empirical one, and calibrating the DRO radius using split CP across different problem instances.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Unified perspective", "weight": 1.0} -->

CP and DRO are not the only routes to distribution-free finite-sample guarantees. Classical distribution-free tolerance limits provide coverage from order statistics, with the required sample size following from a binomial tail. The scenario approach carries this idea into optimization: the solution of a convex program built from $K$ sampled constraints violates the true constraint with a known probability, and a sampling-and-discarding refinement, in which some of the sampled constraints are removed, yields a violation probability with a Beta distribution. More recently, wait-and-judge guarantees have been extended beyond convex programs to the nonconvex setting. O'Sullivan et al. show that ranking nonconformity scores is a one-dimensional scenario program with discarded constraints, and extend the argument to calibration-conditional CP. Calafiore further develops the connection between conformal calibration and scenario optimization, using it to allocate risk across multiple calibrated constraints. Broader comparisons of CP with scenario optimization and PAC-Bayes theory for verification and control are provided.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Unified perspective", "weight": 1.0} -->

Unlike prior works that primarily combine CP with distributionally robust ideas to obtain shift-robust coverage, we aim to develop a unified probabilistic framing of CP and DRO, characterize their connection in finite-sample quantile estimation, and provide a systematic comparison of their statistical behavior and practical trade-offs.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem Formulation and Preliminaries", "weight": 1.0} -->

Let $(\Omega,\mathcal{F},P)$ be a probability space, where $\Omega$ is the sample space, $\mathcal{F}$ is a $\sigma$-algebra, and $P$ is a probability measure. For $\mathcal{X}\subseteq\mathbb{R}$ with Borel $\sigma$-algebra $\mathcal{B}(\mathcal{X})$, denote by $\mathcal{P}(\mathcal{X})$ the set of all Borel probability measures on $\mathcal{X}$. Let $\mathbb{P}\in\mathcal{P}(\mathcal{X})$ denote the distribution of a random variable $R:\Omega\to\mathcal{X}$. We use $\mathbb{P}_{\text{test}}\in\mathcal{P}(\mathcal{X})$ to denote a test distribution that may differ from $\mathbb{P}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Problem Formulation and Preliminaries", "weight": 1.0} -->

For any distribution $\mathbb{Q}\in\mathcal{P}(\mathcal{X})$ and level $p\in$, define its $p$-quantile as For $n$ values $a_{1},\ldots,a_{n}\in\mathbb{R}\cup\{\infty\}$ and a level $p\in$, we write $\Quant_{p}(a_{1},\ldots,a_{n})$ for the $\left\lceil np\right\rceil$-th smallest of them, the empirical $p$-quantile. If $\mathbb{P}_{\text{test}}$ were known, the solution would be $q_{1-\delta}(\mathbb{P}_{\text{test}})$, available in closed form for standard families such as the Gaussian or the uniform.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem Formulation and Preliminaries", "weight": 1.0} -->

In practice $\mathbb{P}_{\text{test}}$ is unknown and $\alpha$ must be estimated from a calibration dataset $R^{},\ldots,R^{(K)}$ drawn i.i.d. from $\mathbb{P}$, denoted $R^{1:K}:=R^{},\ldots,R^{(K)}$. Since $\mathbb{P}$ may differ from $\mathbb{P}_{\text{test}}$, estimation requires a known bound on their discrepancy.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem 1", "weight": 1.0} -->

(Test-distribution quantile estimation): Let $\delta\in$ be a risk level, let $R^{1:K}$ be calibration scores drawn i.i.d. from $\mathbb{P}$, and let $\dist$ be a discrepancy on $\mathcal{P}(\mathcal{X})$ with a known budget $\gamma\geq 0$ such that $\dist(\mathbb{P},\mathbb{P}_{\text{test}})\leq\gamma$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Given $\delta$, $R^{1:K}$ and $(\dist,\gamma)$, compute the smallest $\alpha\in\mathbb{R}$ satisfying: We first consider the case $\mathbb{P}=\mathbb{P}_{\text{test}}$, and aim to construct an estimator $\bar{\alpha}=\bar{\alpha}(R^{1:K})$ such that $\mathbb{P}(R^{}\leq\bar{\alpha})\geq 1-\delta$ holds with high probability over the draw of the calibration samples. We define the problem as follows.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Problem 1.a", "weight": 1.0} -->

(Calibration-conditional quantile estimation): Consider Problem 1 with $\gamma=0$, i.e., $\mathbb{P}_{\text{test}}=\mathbb{P}$. Given a risk level $\delta\in$ and $K+1$ i.i.d. samples $R^{},R^{},\ldots,R^{(K)}$ from $\mathbb{P}$, construct a data-dependent threshold $\bar{\alpha}=\bar{\alpha}(R^{1:K})$ such that We refer to as a calibration-conditional coverage guarantee. The terminology emphasizes that, after the calibration samples $R^{1:K}$ are realized, the data-dependent threshold $\bar{\alpha}$ should cover an independent future test score $R^{}$ with probability at least $1-\delta$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Problem 1.a", "weight": 1.0} -->

The assumption that the calibration and test scores are drawn from the same distribution may fail in practice, e.g., when the calibration data are historical or collected under different environments, sensing conditions, populations, or tasks than the future test data. For example, a model calibrated on past observations may be deployed under a new temporal regime, or a language model calibrated on one benchmark or prompt distribution may be evaluated on another. To account for such calibration-test distribution shift, we consider Problem 1.b.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Problem 1.b", "weight": 1.0} -->

(Calibration-test shift-robust quantile estimation): Consider Problem 1 with $\gamma>0$. Given a risk level $\delta\in$, $K$ i.i.d. calibration samples $R^{1:K}$ drawn from $\mathbb{P}$, and an independent test sample $R^{}$ drawn from $\mathbb{P}_{\mathrm{test}}$, construct an estimator $\bar{\alpha}=\bar{\alpha}(R^{1:K})$ such that where $\mathbb{P}\neq\mathbb{P}_{\mathrm{test}}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Problem 1.b", "weight": 1.0} -->

In this paper, we present two methods for constructing the estimators in and: conformal prediction (CP) and distributionally robust optimization (DRO).

<!-- chunk {"id": "body-0034", "role": "body", "section": "CP and DRO Without Distribution Shift", "weight": 1.0} -->

In this section, we address Problem 1.a with CP and DRO when no test-time distribution shift is present. We first consider the CP approach.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Calibration-Conditional Conformal Prediction", "weight": 1.0} -->

Unfortunately, exact calibration-conditional guarantees of the form cannot be achieved in a finite-sample, distribution-free setting. Intuitively, after conditioning on a finite calibration set, the observed samples do not fully determine the unseen tail of the distribution; therefore, any finite threshold may fail to cover enough probability mass for some distribution consistent with the calibration data. Instead, presents a conformal prediction variant that provides calibration-conditional coverage guarantees of the form: where $\beta\in$ is a user-defined failure probability over the calibration data. For notational convenience, we write $\mathbb{P}^{K}=\mathbb{P}^{\otimes K}$ for the product measure of $K$ i.i.d. draws from $\mathbb{P}$, so that $\mathbb{P}^{K}$ denotes probability with respect to the samples $\{R^{1:K}\}$, and $\mathbb{E}^{K}$ the corresponding expectation over $R^{1:K}\sim\mathbb{P}^{K}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Calibration-Conditional Conformal Prediction", "weight": 1.0} -->

We intuitively interpret the statement in equation as "with probability no less than $1-\beta$ over the draw of calibration datapoints $R^{1:K}$, it holds that $R^{}\leq\bar{\alpha}(R^{1:K})$ with probability no less than $1-\delta$ over the draw of a test datapoint $R^{}$." Consequently, the outer probability measure $\mathbb{P}^{K}(\cdot)$ is defined over the randomness in $R^{1:K}$, while the inner probability measure $\mathbb{P}(\cdot)$ is defined over the randomness in $R^{}$. If $\beta\in$ is chosen to be very small, then one can approximately obtain calibration-conditional guarantees.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Calibration-Conditional Conformal Prediction", "weight": 1.0} -->

Classical split conformal prediction is typically formulated through the marginal coverage guarantee: which averages jointly over the randomness in the calibration sample $R^{1:K}$ and the independent test score $R^{}$. Consequently, marginal coverage does not control the coverage obtained for a particular realization of the calibration sample: calibration sets with coverage below $1-\delta$ may be compensated for by calibration sets with higher coverage.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Calibration-Conditional Conformal Prediction", "weight": 1.0} -->

The calibration-conditional guarantee in provides additional control by requiring that the target coverage holds for at least a $1-\beta$ fraction of calibration samples. The following result relates this two-level guarantee to marginal coverage.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 4.5 (Finite-sample non-vacuity)", "weight": 1.0} -->

For an estimator of the form $\Quant_{p_{K}}(R^{1:K},\infty)$, the appended value $\infty$ is inactive, and hence the estimator is finite, if and only if If $p_{K}>\frac{K}{K+1}$, the quantile selects the value $\infty$, yielding a vacuous prediction region. For the estimator in Lemma 4.2. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification"), the finite-threshold condition is Equivalently, the minimum calibration size is For Lemma 4.3.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 4.5 (Finite-sample non-vacuity)", "weight": 1.0} -->

‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification"), the threshold is the $j$-th order statistic with $j=K-\lfloor k\rfloor$, and $I_{1-\delta}(j,K+1-j)$ is decreasing in $j$. A finite threshold is therefore available when the largest admissible choice $j=K$ satisfies the beta-function condition. Since $\mathrm{Beta}(K,1)$ has cumulative distribution function $x^{K}$, this leads to: For Lemma 4.4. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification"), the corresponding condition is The variant in Lemma 4.4.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 4.5 (Finite-sample non-vacuity)", "weight": 1.0} -->

‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") can be sharper than Lemma 4.2. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") when $\delta$ is small, and the exact beta-function construction of Lemma 4.3. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") is sharper than both. Table 1 makes the comparison precise. The Hoeffding-based condition (12.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 4.5 (Finite-sample non-vacuity)", "weight": 1.0} -->

‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification")) forces $K_{\min}=\Theta\big(\ln(1/\beta)/\delta^{2}\big)$, whereas Lemmas 4.3. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") and 4.4. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") both scale as $\Theta\big(\ln(1/\beta)/\delta\big)$, with a much smaller constant for Lemma 4.3.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 4.5 (Finite-sample non-vacuity)", "weight": 1.0} -->

‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") by (14. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification")). These conditions suggest a small-sample limitation of the constructions above: when the required confidence correction is large relative to the calibration size, the only distribution-free threshold they supply is the vacuous value $\infty$. Table 1 summarizes the three lemmas: Lemma 4.3. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") is non-vacuous at a much smaller $K$. All three are evaluated in Sections 4.5 and 6.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 4.5 (Finite-sample non-vacuity)", "weight": 1.0} -->

We next turn to distributionally robust optimization (DRO), which supplies a threshold that is finite for every $K$. Rather than relying on a finite-sample calibration argument, DRO constructs a worst-case guarantee over an ambiguity set of probability distributions centered at the empirical distribution $\widehat{\mathbb{P}}_{K}=\frac{1}{K}\sum_{i=1}^{K}\delta_{R^{(i)}}$, where $\delta_{x}$ denotes the Dirac measure at $x$; by construction $q_{1-\delta}(\widehat{\mathbb{P}}_{K})=\Quant_{1-\delta}(R^{1:K})$. It attains the same calibration-conditional guarantee, at the cost of the distributional assumptions needed to certify its radius.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Distributionally Robust Optimization", "weight": 1.0} -->

To formalize the DRO construction, we introduce a Wasserstein ambiguity set that defines a set of possible distributions around the empirical distribution. For $\mathbb{P},\mathbb{Q}\in\mathcal{P}(\mathcal{X})$, we denote by $\Gamma(\mathbb{P},\mathbb{Q})$ the set of couplings, i.e., all joint distributions on $\mathcal{X}\times\mathcal{X}$ with marginals $\mathbb{P}$ and $\mathbb{Q}$. We consider the $\infty$-Wasserstein distance: Here $\operatorname{supp}(\pi)$ denotes the support of the coupling $\pi$, i.e., the smallest closed set $S\subseteq\mathcal{X}\times\mathcal{X}$ such that $\pi(S)=1$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Distributionally Robust Optimization", "weight": 1.0} -->

Given $\widehat{\mathbb{P}}_{K}$, we define an ambiguity set of distributions $\mathbb{Q}$ that are within $W_{\infty}$ distance of $r>0$ from $\widehat{\mathbb{P}}_{K}$: We use ${\cal M}^{r}(\widehat{\mathbb{P}}_{K})$ to construct a DRO-based quantile bound analogous to the conformal prediction result.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Distributionally Robust Optimization", "weight": 1.0} -->

A key step in the DRO construction is to choose the ambiguity radius $r$ so that the Wasserstein ball around the empirical distribution contains the true distribution with high probability. Following, Lemma 4.6 provides one such choice, $r=r_{K}(\beta)$, which ensures this containment with probability at least $(1-\beta)$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 4.8", "weight": 1.0} -->

(Robust joint coverage over the ambiguity ball): The guarantee in (21. ‣ 4.2 Distributionally Robust Optimization ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification")) holds for every realization of the calibration sample, so it survives taking expectations.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 4.8", "weight": 1.0} -->

No factor $1-\beta$ appears here, in contrast to Lemma 4.1: the confidence level enters only through the radius $r_{K}(\beta)$, and once that radius is fixed (21. ‣ 4.2 Distributionally Robust Optimization ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification")) holds surely rather than with probability $1-\beta$. $\bullet$ So far, we have presented CP- and DRO-based estimators of $\bar{\alpha}$, with their connections and key differences summarized in Table 2. Both inflate the empirical quantile to hedge against the gap between $\widehat{\mathbb{P}}_{K}$ and $\mathbb{P}$, but along different axes: CP raises the probability level at which the empirical quantile is evaluated, from the nominal $1-\delta$ to $1-\delta+\epsilon$, where the level inflation $\epsilon>0$ is the finite-sample correction supplied by Lemmas 4.2.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 4.8", "weight": 1.0} -->

‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification")--4.4. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification"); DRO instead enlarges the quantile value through a Wasserstein ambiguity radius. We refer to these as the *level* and *value* coordinates of the correction, the first living on the probability axis and the second in the units of the score. Their relative behavior depends on the tail of the underlying distribution, which we make precise as follows.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Statistical Properties of CP and DRO Estimators", "weight": 1.0} -->

Beyond coverage guarantees, it is important to understand the statistical behavior of the CP and DRO estimators, including consistency, finite-sample distributions, and asymptotic behavior because these properties guide how conservative or efficient each method is in practice. We first establish the statistical properties of the CP quantile estimator introduced in Lemma 4.2. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification"), whose level correction $\sqrt{\ln(1/\beta)/(2K)}$ is available in closed form, whereas the level $\delta^{\prime}$ of Lemma 4.3. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") is defined implicitly by a beta-function condition. Analogous results hold for the variants in (10.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Statistical Properties of CP and DRO Estimators", "weight": 1.0} -->

‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification")).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Choosing the Wasserstein Radius", "weight": 1.0} -->

The choice of the Wasserstein radius is central to the statistical interpretation and practical performance of DRO. Lemma 4.6 provides one sufficient choice of $r_{K}(\beta)$ such that: More generally, finite-sample Wasserstein radii can be constructed using measure-concentration or statistical-inference arguments. Such choices give the ambiguity set the interpretation of a high-confidence region for the unknown distribution. However, the resulting bounds may depend on unknown distributional constants and can be overly conservative in finite samples.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Choosing the Wasserstein Radius", "weight": 1.0} -->

Alternatively, the radius may be selected by validation or treated as a design parameter controlling the trade-off between robustness and conservativeness, or calibrated around a fitted center to cover the unknown distribution. For any fixed radius $r$, the threshold $\Quant_{1-\delta}(R^{1:K})+r$ still guarantees coverage uniformly over $\mathcal{M}^{r}(\widehat{\mathbb{P}}_{K})$. However, if $r$ is selected heuristically, the high-probability coverage guarantee for the true distribution $\mathbb{P}$ does not follow.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Choosing the Wasserstein Radius", "weight": 1.0} -->

CP provides another useful reference for the scale of the radius. Whenever the CP estimator $\bar{\alpha}_{\mathrm{CP}}$ is finite, define its effective value-space correction as Thus, $r_{\mathrm{CP}}$ translates CP's quantile-level inflation into an equivalent value-space correction for the realized calibration sample. It may therefore serve as a reference or initialization when selecting a practical DRO radius. Importantly, it is not generally a certified Wasserstein radius: CP controls the target quantile, but does not guarantee that the distribution $\mathbb{P}$ lies in $\mathcal{M}^{r_{\mathrm{CP}}}(\widehat{\mathbb{P}}_{K})$ with high probability.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Choosing the Wasserstein Radius", "weight": 1.0} -->

To interpret the scale of this correction, let $\epsilon_{K}:=\sqrt{\ln(1/\beta)/(2K)}$, and suppose that $\mathbb{P}$ has a continuous density $f$ that is positive near its $(1-\delta)$-quantile $\alpha$. A first-order quantile approximation gives: Hence, the conversion from CP's level correction to a value-space radius depends on the local density near the target quantile. For the special case $\mathbb{P}=\mathrm{Uniform}$, where $f(\alpha)=1$, this reduces to $r_{\mathrm{CP}}\approx\epsilon_{K}$. For general distributions, no distribution-free constant conversion exists.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Illustrative Examples", "weight": 1.0} -->

We now use simple scalar distributions to illustrate the finite-sample mechanisms identified in the preceding analysis. The examples visualize how sample size, the shape of the score distribution, and the choice of Wasserstein radius affect the CP and DRO quantile estimators. Their purpose is to isolate and explain these theoretical effects in controlled settings, rather than to evaluate performance on a particular application. The studies in Section 6, instead, examine the same methods on more realistic problems.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Illustrative Examples", "weight": 1.0} -->

We consider distributions with bounded, unbounded, and truncated supports. Throughout, we set $\delta=0.1$ and $\beta=0.05$. For each distribution and sample size $K$, we repeat the calibration procedure over 500 independent trials, drawing a new calibration set in each trial, and report the mean and standard deviation of the resulting quantile estimates.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Illustrative Examples", "weight": 1.0} -->

Sample size and conservativeness. Figure 2 compares the three CP corrections with the DRO estimator of Lemma 4.7. ‣ 4.2 Distributionally Robust Optimization ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") on $\mathbb{P}=\mathrm{Uniform}$, for which $\inf f=1$ and the true $(1-\delta)$-quantile is $0.9$. Panel (a) shows the non-vacuity thresholds of Table 1: Lemma 4.3. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") becomes finite at $K=29$, whereas Lemmas 4.2. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") and 4.4.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Illustrative Examples", "weight": 1.0} -->

‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") require $K=170$ and $K=172$. The DRO estimator is finite at every $K$, but its certified radius $r_{K}(\beta)=\sqrt{\ln(2/\beta)/(2K)}$ equals $\approx 1.358$ at $K=1$, so the bound it returns is loose until $K$ reaches the hundreds. Panel (b) confirms the ordering predicted by the asymptotic shifts: once all four are available, the certified DRO threshold is the most conservative and Lemma 4.3. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") the tightest.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Illustrative Examples", "weight": 1.0} -->

Effect of the DRO radius. We next compare CP with DRO using the simplified scaling $r_{K}=r_{1}/\sqrt{K}$, which preserves the asymptotic $K^{-1/2}$ rate of Lemma 4.6 while letting $r_{1}$ act as a tunable parameter. Figure 3 shows the comparison on three distributions: $\mathrm{Uniform}$, standard Normal $\mathcal{N}$, and $\mathrm{Beta}$. Across all $r_{1}\in\{0.1,0.5,1,4\}$, DRO converges to the true quantile, with larger $r_{1}$ giving more conservative estimates at small $K$. The Normal needs the largest $r_{1}$: its density at the target quantile is the smallest of the three, so a level correction buys the least threshold there.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Illustrative Examples", "weight": 1.0} -->

For small $r_{1}$, the empirical $(1-\delta)$-quantile is often drawn from samples that miss the upper tail, and the DRO estimate sits below the truth before converging.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Illustrative Examples", "weight": 1.0} -->

Quantitative convergence. Table 3 reports mean estimates of $\bar{\alpha}_{\mathrm{CP}}$ and $\bar{\alpha}_{\mathrm{DRO}}$ (each at a radius whose two-level rate reaches $1-\beta$) at five sizes from $K=1$ to $10^{4}$, across five distributions including Exponential (unbounded) and a Truncated Normal on $$, over 500 independent runs. Two observations emerge: *(i)* DRO yields a finite, usable estimate at $K=1$ for all five distributions, whereas CP is vacuous; *(ii)* at $K=1000$, CP overshoots the true quantile by $4$--$22\%$, with the largest overshoots on heavier-tailed supports (Exp$$: $22\%$; Normal: $21\%$; Truncated Normal: $12\%$; Uniform: $4\%$; Beta: $6\%$).

<!-- chunk {"id": "body-0064", "role": "body", "section": "Illustrative Examples", "weight": 1.0} -->

DRO, at radii that meet the two-level guarantee, stays within $3$--$10\%$ on the same five distributions. The disparity reflects CP's $\sqrt{\ln(1/\beta)/(2K)}$ level correction, which shifts quantile selection deep into the upper tail when the density is small there; DRO's additive radius is symmetric.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Illustrative Examples", "weight": 1.0} -->

Discussion. With an appropriately chosen Wasserstein radius, DRO is competitive with CP and, on heavier tails, tighter than the relaxation-based corrections of Lemmas 4.2. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") and 4.4. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification"). The advantage is most pronounced in two regimes: low $K$, where CP is vacuous; and heavier tails, where CP's level inflation overshoots.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Illustrative Examples", "weight": 1.0} -->

The optimal $r_{1}$ tracks the density at the $(1-\delta)$-quantile: compactly supported distributions whose density stays bounded away from zero there, such as $\mathrm{Uniform}$ and $\mathrm{Beta}$, tolerate small $r_{1}$, whereas the Normal, whose density at the quantile is far smaller, requires a larger one.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Illustrative Examples", "weight": 1.0} -->

However, this comparison is not symmetric in guarantees. CP enjoys a distribution-free finite-sample coverage bound under only the iid assumption, via the DKW level correction $\sqrt{\ln(1/\beta)/(2K)}$. DRO requires the chosen radius to upper-bound $W_{\infty}(\widehat{\mathbb{P}}_{K},\mathbb{P})$ with probability $\geq 1-\beta$. Lemma 4.6 certifies this for bounded densities with $\inf f\geq m>0$, which among our five distributions the Uniform and the truncated Normal satisfy; $\mathrm{Beta}$ has compact support but a density vanishing at the endpoints, while the Normal and Exponential are unbounded. For the others, the simplified scaling $r_{K}=r_{1}/\sqrt{K}$ inherits the asymptotic rate of Lemma 4.6, but $r_{1}$ becomes a heuristic tuning parameter.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Illustrative Examples", "weight": 1.0} -->

The empirical performance in Table 3 is therefore evidence of practical utility, not a finite-sample guarantee.

<!-- chunk {"id": "body-0069", "role": "body", "section": "CP and DRO With Distribution Shift", "weight": 1.0} -->

In this section, we present how to solve Problem 1.b with CP and DRO. Motivated by the calibration-conditional formulation, we seek a threshold $\bar{\alpha}=\bar{\alpha}(R^{1:K})$ that satisfies for a user chosen confidence level $\beta\in$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "CP and DRO With Distribution Shift", "weight": 1.0} -->

In this case, one must additionally account for the discrepancy between $\mathbb{P}$ and $\mathbb{P}_{\mathrm{test}}$. To make the goal in Problem 1.b attainable, this discrepancy must be bounded. We consider two shift models, each an instance of Problem 1 with a different pair $(\dist,\gamma)$: a Wasserstein model, which bounds how far mass moves, and a Lévy--Prokhorov model, which additionally allows a fraction of the mass to move arbitrarily.

<!-- chunk {"id": "body-0071", "role": "body", "section": "CP and DRO With Distribution Shift", "weight": 1.0} -->

The radius $\eta$ controls the amount of calibration-test shift allowed by the model and leads to the additive threshold correction used below. In practice, $\eta$ can be specified from prior knowledge, estimated from additional validation data when available, or treated as a robustness parameter to study the trade-off between validity and conservativeness.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Assumption 5.1", "weight": 1.0} -->

The test distribution is within a $W_{\infty}$-ball of radius $\eta>0$ around the calibration distribution: corresponding to Problem 1 with $\dist=W_{\infty}$ and $\gamma=\eta$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Assumption 5.1", "weight": 1.0} -->

Conformal prediction. Under Assumption 5.1, the shift is absorbed by adding the Wasserstein radius $\eta$ to the calibration-conditional CP threshold.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Lévy--Prokhorov Shift Model", "weight": 1.0} -->

A complementary line of work models test-time shift using the Lévy--Prokhorov (LP) metric, which allows both value-space perturbations and mass displacement. This leads to uncertainty thresholds that combine an additive value correction with a quantile-level correction.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Lévy--Prokhorov Shift Model", "weight": 1.0} -->

As a special case, we first introduce the total variation (TV) distance between two distributions $\mathbb{P},\mathbb{Q}$: Here $\mathds{1}$ denotes the indicator function. Intuitively, $\mathrm{TV}(\mathbb{P},\mathbb{Q})$ is the minimum fraction of mass that must be reassigned to transform $\mathbb{P}$ into $\mathbb{Q}$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Lévy--Prokhorov Shift Model", "weight": 1.0} -->

The Lévy--Prokhorov (LP) distance generalizes the Wasserstein and TV distances by permitting both local and global perturbations. For $\epsilon\geq 0$, let The corresponding LP ambiguity set is This admits a two-step interpretation: (i) each unit of mass under $\mathbb{P}$ can be moved within a radius $\eta$, and (ii) up to a fraction $\rho$ of the total mass may be displaced arbitrarily. Notably, $B_{0,\rho}(\mathbb{P})$ reduces to the TV ball, while $B_{\eta,0}(\mathbb{P})$ reduces to the $W_{\infty}$ ball.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Lévy--Prokhorov Shift Model", "weight": 1.0} -->

The second shift model bounds the LP distance between the calibration and test distributions.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Assumption 5.4", "weight": 1.0} -->

The test distribution is within an LP ball around the calibration distribution: corresponding to Problem 1 with $\dist=\mathrm{LP}_{\eta}$ and $\gamma=\rho$.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Assumption 5.4", "weight": 1.0} -->

Under Assumption 5.4, we restate the LP-robust conformal result of \[5, Cor. 4.2\].

<!-- chunk {"id": "body-0080", "role": "body", "section": "Application Studies in Vision, Language, and Autonomous Driving", "weight": 1.0} -->

In Section 4.5, we studied the behavior of the CP and DRO quantile estimators on scalar distributions. We now turn to four prediction settings in which the score distribution is induced by a model and a dataset.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Application Studies in Vision, Language, and Autonomous Driving", "weight": 1.0} -->

First, we consider image classification (Section 6.1), which offers an i.i.d. baseline with a large discrete label space. Next, we evaluate the shift-aware estimators of Section 5 on the ImageNet-C dataset (Section 6.2), which adds controlled corruptions to the ImageNet validation images to obtain a test set with distribution shift. Multiple-choice question answering (Section 6.3) shrinks the label space to four options, so an estimator can more easily include all four, giving a valid but uninformative prediction set. Finally, we consider a trajectory prediction problem (Section 6.4), in which the discrete label set is replaced by a ball of radius $\bar{\alpha}$, which can grow without bound, so no such limit exists. All four settings use $K=1000$ at $\delta=\beta=0.1$, for which Remark 4.5.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Application Studies in Vision, Language, and Autonomous Driving", "weight": 1.0} -->

‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") gives $K_{\min}=135$ for Lemmas 4.2. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") and 4.4. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification"), so every considered setting has sufficient calibration samples to exceed the vacuity threshold.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Application Studies in Vision, Language, and Autonomous Driving", "weight": 1.0} -->

In each study, we report mean coverage, which tests the marginal guarantee, the two-level rate $\mathbb{P}^{K}\big(\mathbb{P}(R^{}\leq\bar{\alpha})\geq 1-\delta\big)$, which tests the calibration-conditional guarantee, and the prediction-set size needed to attain the guarantees. We compare split CP, which targets marginal coverage only, against the calibration-conditional corrections of Lemmas 4.2. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification"), 4.3. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") and 4.4.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Application Studies in Vision, Language, and Autonomous Driving", "weight": 1.0} -->

‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") and against DRO (Lemma 4.7. ‣ 4.2 Distributionally Robust Optimization ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification")).

<!-- chunk {"id": "body-0085", "role": "body", "section": "Image Classification", "weight": 1.0} -->

For each $(X_{i},Y_{i})\in\mathcal{D}_{\text{cal}}$, define the nonconformity score which measures how nonconforming the true label is with respect to the model's prediction. A small $R^{(i)}$ indicates high confidence in the correct class; a large value corresponds to greater uncertainty or misclassification.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Image Classification", "weight": 1.0} -->

For a new input $x$, our goal is to construct a prediction set $C(x)\subseteq\{1,\dots,N\}$ that contains the true label with probability at least $1-\delta$: under the assumption that calibration and test samples are exchangeable. Coverage alone is trivially achieved by the full label set $C(x)=\{1,\dots,N\}$; the objective is therefore to attain this coverage while keeping the prediction set *as small as possible*. The prediction set is defined as where $\bar{\alpha}$ is a calibrated threshold. Intuitively, $C(x)$ collects all labels whose predicted probabilities exceed $1-\bar{\alpha}$, thereby guaranteeing the finite-sample coverage property $\mathbb{P}(Y_{\text{test}}\in C(X_{\text{test}}))\geq 1-\delta$, regardless of the underlying data distribution or classifier calibration.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Image Classification", "weight": 1.0} -->

In the standard *split conformal prediction* (SCP) framework, this threshold is the empirical quantile which calibrates the model's confidence scores to achieve the desired marginal coverage. In contrast, we can also define $\bar{\alpha}$ according to either the *calibration-conditional* conformal prediction in (8. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification")) and (10. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification")), or the *distributionally robust* variant in (20. ‣ 4.2 Distributionally Robust Optimization ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification")), which strengthen the coverage guarantees under calibration uncertainty.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Image Classification", "weight": 1.0} -->

Experimental setup. We evaluate the CP and DRO estimators on the ImageNet validation set using the pre-trained ResNet-152 classifier. The dataset contains $50000$ samples. We randomly select $K=1000$ samples for calibration and use the remaining $n_{\text{eval}}=49000$ for evaluation. The target miscoverage level is $\delta=0.1$ (i.e., $0.9$ nominal coverage). For the DRO variants we report two Wasserstein radii, $r_{K}\in\{0.02,0.03\}$, spanning the regime where DRO transitions from compact-but-unreliable to conservative-but-bloated prediction sets.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Image Classification", "weight": 1.0} -->

Results. We conduct $1000$ independent trials with different random splits of calibration and evaluation data. Figure 4 reports the mean empirical coverage across trials. As expected, all six methods achieve marginal coverage at or above the nominal $0.9$. The DRO radii shown are design choices rather than the certified $r_{K}(\beta)$, so this is an empirical observation and not a verification of the guarantee.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Image Classification", "weight": 1.0} -->

To evaluate the stronger conditional guarantee, for each trial we test the two-level criterion with $(\delta,\beta)=(0.1,0.1)$. Figure 5 highlights a key limitation of standard SCP: although it achieves the target marginal coverage on average ($0.901$), it satisfies the two-level guarantee with rate only $0.547$. This shortfall arises because SCP does not account for randomness in the calibration scores, limiting its robustness under the stronger conditional criterion. In contrast, both calibration-conditional CP methods (Lemmas 4.2. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") and 4.4.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Image Classification", "weight": 1.0} -->

‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification")) consistently satisfy the two-level guarantee in essentially all trials ($1.000$ and $0.996$), while the DRO variants require a sufficiently large radius ($r_{K}=0.03$ achieves $0.965$, $r_{K}=0.02$ only $0.906$). Lemma 4.3. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") behaves differently from the other two corrections: its condition is exact rather than a relaxation, so its two-level rate stays near the target $1-\beta$ ($0.904$) instead of saturating at $1$, and its sets are correspondingly smaller.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Image Classification", "weight": 1.0} -->

Because coverage is itself estimated on a finite evaluation set, the measured rate of such a tight method sits at the nominal value and can fall marginally on either side of it.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Image Classification", "weight": 1.0} -->

Table 5 shows the conservativeness/robustness trade-off across the methods. The calibration-conditional CP methods (Lemmas 4.2. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") and 4.4. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification")) emerge as the sweet spot because they satisfy the stronger two-level guarantee in essentially all trials while keeping prediction sets small (mean size $2.4$ to $2.7$ out of $1000$ classes), while Lemma 4.3. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") gives up that margin for sets of mean size $2.0$.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Image Classification", "weight": 1.0} -->

Split CP gives the smallest sets (mean $1.8$) but fails the two-level guarantee at rate $0.547$. The DRO variant $r=0.02$ is similarly compact and clears the criterion only marginally ($0.906$). DRO with $r=0.03$ satisfies the guarantee with rate $0.965$ and a comparable mean set size on non-degenerate trials ($3.0$), but in a fraction $0.060$ of trials the calibrated threshold $\bar{\alpha}$ exceeds $1$ and the prediction set degenerates to all $1000$ classes.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Image Classification", "weight": 1.0} -->

This degenerate behavior reflects a structural limitation of the additive form $\bar{\alpha}_{\text{DRO}}=\bar{\alpha}_{\text{emp}}+r$: the nonconformity scores are bounded in $$, so if the empirical quantile $\bar{\alpha}_{\text{emp}}$ is already close to the upper end of its range under moderate calibration noise then an additive offset $r$ can push the threshold past $1$, at which point any class is admitted into the prediction set. Clipping $\bar{\alpha}$ at $1$ does not help because the prediction set $C(x)=\{y:f_{y}(x)\geq 1-\bar{\alpha}\}$ then admits every label, so it remains vacuous. A remedy would instead need a data-adaptive radius that scales with the local score density near the $(1-\delta)$-quantile, with its own validity argument.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Image Classification", "weight": 1.0} -->

Overall, this experiment shows that calibration-conditional CP is the most efficient route to satisfying the two-level guarantee under i.i.d. data.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Image Classification Under Distribution Shift", "weight": 1.0} -->

Problem setup. We next test robustness under distribution shift using ImageNet-C, which applies controlled corruptions to the ImageNet validation images. We use three of its corruption families spanning distinct mechanisms: Gaussian noise, motion blur, and fog, each at the five severity levels defined by ImageNet-C, illustrated in Figure 6.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Image Classification Under Distribution Shift", "weight": 1.0} -->

Experimental setup. In each trial, we draw $K=1000$ clean images for calibration and use the corrupted versions of the remaining $n_{\text{eval}}=49000$ for evaluation. We keep $\delta=0.1$, $\beta=0.1$, and report $200$ independent trials. We compare the five shift-aware estimators of Table 4: CP under $W_{\infty}$ shift (Lemma 5.2. ‣ 5.1 Wasserstein Shift Model ‣ 5 CP and DRO With Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification")), DRO under $W_{\infty}$ shift (Lemma 5.3.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Image Classification Under Distribution Shift", "weight": 1.0} -->

‣ 5.1 Wasserstein Shift Model ‣ 5 CP and DRO With Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification")), the marginal LP-robust CP of (Theorem 5.5), and our calibration-conditional extensions under LP shift (Theorem 5.6 and its DRO counterpart Theorem 5.7. ‣ 5.2 Lévy–Prokhorov Shift Model ‣ 5 CP and DRO With Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification")), together with split CP as a no-adjustment baseline.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Image Classification Under Distribution Shift", "weight": 1.0} -->

The two shift models take different budgets. For the $W_{\infty}$ methods (Lemmas 5.2. ‣ 5.1 Wasserstein Shift Model ‣ 5 CP and DRO With Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") and 5.3. ‣ 5.1 Wasserstein Shift Model ‣ 5 CP and DRO With Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification")) we set $\eta=0.008$. For the LP methods (Theorems 5.5, 5.6 and 5.7.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Image Classification Under Distribution Shift", "weight": 1.0} -->

‣ 5.2 Lévy–Prokhorov Shift Model ‣ 5 CP and DRO With Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification")) we set $\eta=0.002$ and $\rho=0.020$, chosen so that Theorem 5.5 attains $1-\delta$ marginal coverage at severity 1. The $W_{\infty}$ budget is larger because it has no $\rho$ to absorb the level part of the shift.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Image Classification Under Distribution Shift", "weight": 1.0} -->

Results. Figure 7 reports mean coverage versus severity, and Figure 8 the two-level guarantee probability for all three corruptions and five severities. Split CP, which has no shift mechanism, degrades sharply: its mean coverage falls from $0.87$ at severity 1 to $0.50$ at severity 5 (Gaussian noise), and it satisfies the two-level guarantee in essentially no shifted cell. The shift-aware methods hold higher coverage. Among them, Theorem 5.6 is the most robust, maintaining the two-level guarantee at severity 1--2 across all three corruptions.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Image Classification Under Distribution Shift", "weight": 1.0} -->

Table 6 details a representative mild cell (motion blur, severity 1). Two points stand out. First, the marginal method (Theorem 5.5) achieves its target marginal coverage ($0.907$) with small sets (median $2.5$), but satisfies the stronger two-level criterion with rate only $0.745$, which illustrates the gap between marginal robustness and the calibration-conditional guarantee. Second, Theorem 5.6 closes this gap by satisfying the two-level guarantee in all trials with usable prediction sets (median $6.8$ of $1000$ classes, $0.000$ vacuous). Its DRO counterpart (Theorem 5.7.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Image Classification Under Distribution Shift", "weight": 1.0} -->

‣ 5.2 Lévy–Prokhorov Shift Model ‣ 5 CP and DRO With Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification")) shows the limit of the value-space route on a bounded score: it applies the level correction $\rho$ and the additive radius together, which drives $\bar{\alpha}$ past $1$ in $34\%$ of trials even at the reduced radius $r_{K}=0.02$, so its median set of $10.7$ classes is obtained at the cost of frequent degeneracy. On the continuous nuScenes score, the same estimator is instead the tightest of the shift-aware methods (Table 9).

<!-- chunk {"id": "body-0105", "role": "body", "section": "Image Classification Under Distribution Shift", "weight": 1.0} -->

W∞ shift model (Assumption 5.1) Lévy–Prokhorov shift model (Assumption 5.4) Table 6: Results at motion blur severity 1 (K = 1000, δ = 0.1, β = 0.1, 200 trials). The two shift models carry their own budgets, recorded in the (η, ρ) column. “Mean coverage” is the average coverage over trials; ℙK(cov ≥ 1 − δ) is the calibration-conditional success rate ℙK(ℙtest(R ≤ ᾱ) ≥ 1 − δ); “Set size” is the median prediction-set size; “Vac.” is the fraction of trials whose threshold ᾱ exceeds 1. The marginal method (Theorem 5.5) attains marginal coverage (0.907) but not the two-level guarantee (0.745). Theorem 5.6 attains both with usable sets. Its DRO counterpart (Theorem 5.7) meets the guarantee only degenerately on this bounded score: stacking the level correction ρ on the additive radius still pushes ᾱ above 1 in 34% of trials.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Image Classification Under Distribution Shift", "weight": 1.0} -->

The DRO radius is set to rK = 0.02, carried over from Table 5 as the smallest i.i.d. radius meeting the two-level guarantee (it is a design choice in the sense of Section 4.4, not the certified value).

<!-- chunk {"id": "body-0107", "role": "body", "section": "Image Classification Under Distribution Shift", "weight": 1.0} -->

Distribution shift sharpens the i.i.d. findings of Section 6.1. Split CP loses coverage outright. The marginal LP-robust method achieves marginal coverage but not the calibration-conditional guarantee, while Theorem 5.6 delivers the two-level guarantee with usable sets at mild-to-moderate corruption. As severity in the distribution shift grows, all methods degrade. A fixed $(\eta,\rho)$ budget eventually cannot absorb the shift, and a larger budget raises the threshold and so enlarges the prediction sets. Matching the budget to the anticipated shift magnitude, thus, trades efficiency for robustness, with Theorem 5.6 being at the most favorable point of this trade-off.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Language Model Question Answering", "weight": 1.0} -->

Problem setup. We next apply the uncertainty quantification methods to a multiple-choice question answering task using a language model on the MMLU dataset. We evaluate on the standard test split of $14042$ questions across $57$ academic subjects, each with four answer options $\mathcal{Y}=\{A,B,C,D\}$. A pre-trained Qwen2.5-7B-Instruct model reads each question and its four options and produces a probability $f_{y}(x)$ over the options from the next-token logits of the choice letters. This model attains $71.7\%$ top-1 accuracy. As before, we define the nonconformity score as and the prediction set as $C(x)=\{y\in\mathcal{Y}:f_{y}(x)\geq 1-\bar{\alpha}\}$.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Language Model Question Answering", "weight": 1.0} -->

Experimental setup. We pool all $14042$ questions and, in each trial, draw $K=1000$ for calibration and use the remaining $n_{\text{eval}}=13042$ for evaluation, so the calibration and test samples are exchangeable. We set $\delta=0.1$ and $\beta=0.1$, and report $1000$ independent trials. We compare Split CP, the three calibration-conditional CP variants Lemmas 4.2. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification"), 4.3. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") and 4.4.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Language Model Question Answering", "weight": 1.0} -->

‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification")), and the $W_{\infty}$-DRO threshold at radii $r_{K}\in\{0.002,0.003\}$. Because the four-option scores concentrate near $1$, the DRO radii here are an order of magnitude smaller than in the ImageNet study.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Language Model Question Answering", "weight": 1.0} -->

Results. Figure 10 reports the mean empirical coverage across trials and Figure 11 the two-level guarantee probability. As in the image setting, every method attains marginal coverage at or above the nominal level of $0.9$. The two-level guarantee, however, separates the methods sharply (Table 7). Split CP, which controls marginal but not calibration-conditional coverage, attains the target marginal coverage ($0.901$) but satisfies the two-level criterion with rate only $0.557$. The calibration-conditional methods (Lemma 4.2. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification"), Lemma 4.4.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Language Model Question Answering", "weight": 1.0} -->

‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification")) satisfy it in essentially all trials while keeping the prediction sets compact (mean size $\approx 2.0$ of $4$ options), and Lemma 4.3. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") again tracks the nominal level ($0.891$) with the smallest calibration-conditional set ($1.84$). The DRO threshold interpolates between these regimes as $r_{K}$ grows: $r_{K}=0.002$ reaches $0.887$ and $r_{K}=0.003$ reaches $0.955$. This improvement, however, comes from a constant additive radius that inflates every prediction set uniformly.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Language Model Question Answering", "weight": 1.0} -->

Already at $r_{K}=0.003$, DRO returns the full four-option set in a fraction $0.160$ of trials (Table 7), whereas the calibration-conditional methods are never vacuous. The same additive-radius limitation appears in the image experiments (cf. Sections 6.1 and 6.2): a constant $r_{K}$ cannot adapt to the score distribution, and calibration-conditional CP attains the two-level guarantee with smaller sets.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Autonomous Driving Trajectory Prediction", "weight": 1.0} -->

Problem setup. Our final experiment moves from discrete classification to a *continuous-output* task: vehicle trajectory prediction on nuScenes. For each agent, we observe $2$ s of history and predict its position over a $6$ s horizon with a constant velocity-and-heading baseline, which is the standard physics model of the nuScenes prediction challenge. We set the nonconformity score to the final displacement error in meters, the distance between the predicted and true position at horizon $T=6$ s. The prediction set is now a ball of radius $\bar{\alpha}$ around the predicted endpoint, so the analogue of prediction-set size is the calibrated *radius* in meters. Unlike the discrete label sets of Sections 6.1--6.3, there is no finite label space to exhaust. The additive DRO radius simply grows the ball, so the prediction set is never vacuous.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Autonomous Driving Trajectory Prediction", "weight": 1.0} -->

Experimental setup. We score $49787$ agent trajectories from the nuScenes prediction challenge with the constant-velocity-and-heading model. The final displacement error has a median of $9.4$ m, a mean of $11.5$ m, and a $90$th percentile of $23.8$ m. In each of the $1000$ trials, we draw $K=1000$ trajectories for calibration and use the remaining $n_{\text{eval}}=48787$ for evaluation, with $\delta=0.1$ and $\beta=0.1$. We compare Split CP, the three calibration-conditional CP variants, and $W_{\infty}$-DRO at additive radii $r_{K}\in\{1,3\}$ m.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Autonomous Driving Trajectory Prediction", "weight": 1.0} -->

Results. Figure 12 reports the mean empirical coverage across the trials, Figure 13 the two-level guarantee probability, and Table 8 the calibrated radius. The pattern matches the classification and language-model experiments: every method attains marginal coverage at or above the nominal $0.9$ but Split CP, which controls only marginal coverage, satisfies the two-level criterion with rate only $0.554$. The calibration-conditional methods (Lemma 4.2. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification"), Lemma 4.4. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification")) satisfy it in essentially all trials with radii of $26$--$27$ m, while Lemma 4.3.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Autonomous Driving Trajectory Prediction", "weight": 1.0} -->

‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") tracks the nominal level with a $24.8$ m ball, and DRO reaches it once $r\geq 3$ m. The key difference from the discrete settings is the absence of vacuity. As the DRO radius grows from $1$ to $3$ m the calibrated ball grows from $24.9$ to $26.9$ m and never degenerates.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Autonomous Driving Trajectory Prediction", "weight": 1.0} -->

W∞ shift model (Assumption 5.1) Lévy–Prokhorov shift model (Assumption 5.4) Table 9: Maneuver shift on nuScenes (K = 1000, δ = β = 0.1, 1000 trials) with calibration on straight-driving agents and testing on turning agents. As in Table 6, each shift model has a budget η in meters. “Mean coverage” is the average coverage over trials; ℙK(cov ≥ 1 − δ) is the calibration-conditional success rate ℙK(ℙtest{R ≤ ᾱ} ≥ 1 − δ); “Set size” is the calibrated ball radius in meters. The Split CP margin under-covers the shifted population (0.669). The shift-aware estimators recover coverage, with the marginal method (Theorem 5.5) attaining marginal but not two-level coverage and Theorem 5.6 attaining both; its DRO counterpart (Theorem 5.7) attains both with a tighter ball.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Autonomous Driving Trajectory Prediction", "weight": 1.0} -->

Distribution shift. We additionally probe two covariate shifts, calibrating on one subpopulation and testing on another. A *geographic* shift, where we calibrate on Boston and test on Singapore, barely moves the score distribution (the $90$th-percentile error is $23.9$ m versus $23.7$ m) because constant-velocity error depends on agent dynamics rather than city. Thus, we consider a *maneuver* shift, where we calibrate on straight driving and test on turning. Turning roughly doubles the prediction error, raising the $90$th-percentile from $20.2$ to $29.7$ m. The i.i.d. Split CP margin under-covers the turning population at only $0.669$.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Autonomous Driving Trajectory Prediction", "weight": 1.0} -->

Table 9 shows that the shift-aware estimators of Section 6.2 recover coverage, with the same marginal-versus-two-level distinction as the ImageNet-C study (Table 6): the marginal estimator (Theorem 5.5) achieves marginal coverage ($0.905$) but satisfies the two-level guarantee with rate only $0.657$, whereas Theorem 5.6 attains both ($0.969$, $1.000$). Because the score is continuous, the correction enlarges the safety ball smoothly (from $20$ to $30$--$37$ m) rather than collapsing to a vacuous label set seen in classification. The budget behaves differently here. On the bounded ImageNet-C score, set size grows far more slowly in $\rho$ than in $\eta$ (Figure 9), whereas on this unbounded distance score every budget that achieves marginal coverage yields essentially the same ball, $30$--$31$ m, so the two parameters are interchangeable.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Autonomous Driving Trajectory Prediction", "weight": 1.0} -->

This is the density scaling of Section 4.3 in the shifted setting: $\rho$ shifts the quantile level and $\eta$ shifts its value, and the score density at the threshold converts one into the other.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Choosing an Estimator", "weight": 1.0} -->

This section gives guidance on which estimator to use. Although the three applications (Sections 6.1, 6.3 and 6.4) differ in label space and in whether the score is bounded, they rank the CP estimators identically by both set size and two-level rate, so the same guidance applies to all three.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Choosing an Estimator", "weight": 1.0} -->

If only marginal coverage is required, split CP is the standard choice and gives the smallest sets everywhere. However, it does not control coverage for the particular calibration set drawn, and its two-level rate is far below $0.9$ in the three studies.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Choosing an Estimator", "weight": 1.0} -->

Among the calibration-conditional corrections, Lemma 4.3. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") gives the smallest sets, because it solves the beta-function condition exactly, whereas Lemmas 4.2. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") and 4.4. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") relax it. Because Lemma 4.3.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Choosing an Estimator", "weight": 1.0} -->

‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") carries no slack, its two-level rate tracks $1-\beta$ rather than exceeding it and the measured value can fall on either side. Lemmas 4.2. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") and 4.4. ‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") achieve a wide margin at the cost of larger prediction sets, and their level correction is explicit, so it can be allocated across constraints or time steps. Of the two, Lemma 4.4.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Choosing an Estimator", "weight": 1.0} -->

‣ 4.1 Calibration-Conditional Conformal Prediction ‣ 4 CP and DRO Without Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") is preferable once $\delta$ falls below roughly $0.1$.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Choosing an Estimator", "weight": 1.0} -->

Without calibration-test distribution shift, DRO's certified radius gives the larger correction (Sections 4.5 and 6), so CP produces smaller prediction sets and is the preferable choice. DRO is nevertheless preferable in two cases: when $K$ lies below the non-vacuity thresholds, where CP returns no finite estimator at all, and when coverage must hold over an ambiguity set rather than for $\mathbb{P}$ alone. Whether the score is bounded also decides what DRO's additive correction costs: on the continuous nuScenes distance DRO matches the calibration-conditional sets ($26.9$ against $26.8$ m at a two-level rate of $1.000$), whereas on the bounded MMLU score the same correction returns the full label set in a fraction $0.160$ of trials.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Choosing an Estimator", "weight": 1.0} -->

Every shift-aware estimator requires the shift budget as an input: $\eta$ for the $W_{\infty}$ corrections of Lemmas 5.2. ‣ 5.1 Wasserstein Shift Model ‣ 5 CP and DRO With Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") and 5.3. ‣ 5.1 Wasserstein Shift Model ‣ 5 CP and DRO With Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification"), and $(\eta,\rho)$ for the LP estimators. None is assumption-free. When the shift is purely value-space, the $W_{\infty}$ corrections are the tighter choice, as they do not pay for a level perturbation ($31.1$ against $36.7$ m on nuScenes).

<!-- chunk {"id": "body-0129", "role": "body", "section": "Choosing an Estimator", "weight": 1.0} -->

Under the LP model, Theorem 5.5 achieves marginal coverage only ($0.905$, with a two-level rate of $0.657$), whereas Theorem 5.6 and Theorem 5.7. ‣ 5.2 Lévy–Prokhorov Shift Model ‣ 5 CP and DRO With Distribution Shift ‣ A Unified Perspective on Conformal Prediction and Wasserstein Distributionally Robust Optimization for Uncertainty Quantification") achieve both. The choice between those two again follows the score, the latter giving the tighter ball on the continuous nuScenes distance but degenerating on the bounded ImageNet-C score. How to split a given budget between $\eta$ and $\rho$ depends on the score as well: on a bounded score $\rho$ inflates sets far more slowly than $\eta$ (Figure 9), whereas on an unbounded distance score the two are interchangeable, so there $\eta$ may be set directly from the anticipated perturbation.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Conclusions", "weight": 1.0} -->

This article developed a unified probabilistic perspective on conformal prediction (CP) and Wasserstein distributionally robust optimization (DRO), viewing both as procedures that turn finite calibration data into a quantile threshold with finite-sample coverage. The two correct the empirical quantile along different coordinates: CP raises the target quantile level, whereas DRO shifts the quantile value through an ambiguity radius. Making the correspondence precise exposes an asymmetry in what each method certifies. CP's level correction is closed-form and distribution-free, whereas the radius that certifies DRO's coverage depends on a density lower bound that is typically unknown; in return, DRO certifies coverage uniformly over the ambiguity set rather than for the true distribution alone.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In the scalar case, the comparison is exact. The two estimators share the same first-order asymptotic variance and differ only in a deterministic offset. With certified radius, that offset is provably larger for DRO and is governed by a uniform lower bound on the density, whereas CP's is governed by the density at the target quantile.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In the experiments, calibration-conditional CP and DRO attain the two-level guarantee that the standard split-CP baseline fails to meet. Among the methods that meet it, CP produces the smallest prediction sets, while DRO's additive correction is well suited to a continuous score but not to a bounded score, where it can drive the prediction set to vacuity. The same distinction applies to the shift-aware estimators under both shift models. These behaviors are consistent across ImageNet classification, MMLU question answering, and nuScenes trajectory prediction.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Two open problems follow. The first is the DRO radius. The value that certifies coverage depends on unknown properties of the distribution, is provably the looser correction, and can saturate a bounded score. Data-driven and adaptive radii can help, but they require more than the $K$ calibration scores, such as a model for the score distribution or repeated problem instances. The second is the shift budget. Every shift-aware estimator requires it as an input, so none is assumption-free. The open problem is to estimate the budget from data and to account for the estimation error in the guarantee. Beyond these, a further open direction is to propagate the two-level guarantee from coverage into decision-making, e.g., in chance-constrained optimization, model predictive control, and planning, where a calibrated threshold would provide a closed-loop guarantee. Another direction is related to online calibration, where data arrive as a non-stationary stream and the threshold must be updated continually to preserve coverage under drift, as in autonomous systems operating over long horizons.
