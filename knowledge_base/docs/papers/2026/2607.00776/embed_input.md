<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Safe motion planning in dynamic environments requires reasoning about the uncertainty in predicted obstacle motion without sacrificing real-time performance. Existing conformal approaches conformalize a scalar score that aggregates per-obstacle prediction errors, losing spatial coherence and scaling poorly with scene density. We instead conformalize the entire predicted distance field at once. This functional conformal prediction (FCP) framework yields a distribution-free, field-level lower bound, from which safety follows uniformly: any trajectory satisfying the resulting constraint is certified safe, independent of how the control space is sampled. The key enabler is that the residual distance field is empirically low-rank and approximately time-invariant, which makes the bound decomposable in coefficient space. An envelope is fitted offline via functional PCA and a Gaussian-mixture inductive conformal procedure, then refined online by a lightweight adaptive functional conformal (AFCP) update on a low-dimensional vector. This keeps the per-step cost largely insensitive to obstacle count and retains long-run field coverage under distribution shift. We embed the envelope as a tightened safety constraint in a sampling-based model predictive controller, FCP-MPC.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

On the ETH-UCY pedestrian benchmarks and a dense 3D quadrotor task with up to 280 dynamic obstacles, FCP-MPC attains a favorable balance of safety, feasibility, and efficiency, reaching goals where pointwise and egocentric conformal baselines become too conservative or too expensive, while keeping per-step computation far below online uncertainty-reasoning baselines.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous robots are increasingly asked to operate in environments shared with pedestrians, vehicles, and other moving agents, where safe behavior depends on anticipating how the surrounding world will evolve. The future occupancy of such an environment is unobservable at planning time, so it must be forecast from past observations, and any motion planner that consumes these forecasts inherits their errors. The central difficulty is therefore not prediction or planning in isolation but the coupling of the two: a controller must account for the uncertainty in predicted obstacle motion tightly enough to remain safe, yet cheaply enough to close the loop in real time and in densely populated scenes. Achieving both at once, with quantitative safety guarantees, is the problem we address.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A large body of work embeds prediction uncertainty directly into the planning objective or constraints. Chance-constrained formulations bound the probability of collision, and risk-sensitive and distributionally robust planners hedge against tail events or worst-case obstacle distributions. These methods deliver strong guarantees, but at a price. They typically require committing to an ambiguity set or a parametric/moment-based description of the prediction error, and the associated worst-case optimization is solved online, which grows costly as scene density rises. Conformal prediction (CP) offers a complementary, distribution-free route. Rather than constructing such a set or estimating moments, it turns the raw errors of an arbitrary, black-box predictor into sets with finite-sample coverage. CP has been applied to planning among dynamic agents, to perception-based navigation, and to decision-theoretic control under imperfect predictions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite their appeal, most existing CP approaches to motion planning share a common structural limitation. They conformalize a *scalar* score, such as a per-obstacle radius or a per-state margin, and recompute it point-wise online. The online cost then grows with the number of obstacles and the planning horizon, precisely the regime in which real-time safety matters most. Moreover, certifying safety over a *region* rather than at a point requires a worst-case score, which is generally intractable to enforce exactly and is approximated heavily in practice. What is conformalized is thus either cheap but spatially incoherent, or faithful but unaffordable online.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our point of departure is a representational one. The error of a predicted distance field is not an arbitrary high-dimensional object. Across a scene it is spatially structured and admits an accurate low-dimensional representation. We verify this empirically on the ETH--UCY benchmark, where the residual distance field is approximately time-invariant and low-rank, with a handful of functional principal components capturing most of its variance. This structure suggests treating the prediction error as a *function* over the workspace rather than as a collection of scalars, and conformalizing the entire spatial field at once. Doing so yields a continuous, queryable safety envelope instead of a patchwork of point-wise inflations, and we exploit two consequences throughout. First, the certificate is defined over the entire field, so any trajectory satisfying the constraint is safe regardless of how controls are sampled. Second, because the field is low-rank and approximately time-invariant, the envelope admits an offline--online decomposition that separates the expensive conformalization from real-time planning, keeping the per-step cost largely insensitive to the number of obstacles.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Building on this insight, we introduce a functional conformal prediction (FCP) framework that produces a field-level lower bound on the predicted distance field. We expand the residual field in a data-driven basis obtained by functional principal component analysis, and conformalize the prediction error in the resulting coefficient space with a Gaussian-mixture inductive conformal procedure. This yields a distribution-free envelope available in closed form, as a support function over a union of ellipsoids. The envelope is fitted once, offline, from a large calibration set; online, it is refined by an adaptive functional conformal (AFCP) update that rescales the envelope through a single scalar per horizon step. We embed the conformalized lower bound as a tightened safety constraint in a sampling-based model predictive controller, FCP-MPC, and prove asymptotic closed-loop safety both under exchangeability and, through the online adaptation, under distribution shift.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The contributions of this paper are as follows.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We formulate prediction-uncertainty quantification for safe planning as a functional conformal problem on the residual distance field, yielding a distribution-free, field-level lower bound that is continuous and queryable rather than point-wise. Because the certificate is defined over the whole field, it holds for any trajectory satisfying the constraint, independent of the control sampler.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We establish asymptotic closed-loop safety for the hard-constrained MPC whenever the conformalized field satisfies long-run coverage, instantiated with split CP under exchangeability and an adaptive fieldwise update for non-exchangeable streams. We further certify the soft-penalty deployment, which stays safe up to a slack that vanishes as the penalty weight grows and degrades gracefully where the feasible set is empty.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

To make this field-level bound real-time, we decompose it in coefficient space: a GMM-based inductive conformal envelope is fitted once offline, while online a single low-dimensional adaptive update absorbs distribution shift, keeping per-step computation low and largely decoupled from obstacle count.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate on the ETH--UCY pedestrian benchmarks and a dense 3D quadrotor task with up to 280 dynamic obstacles that FCP-MPC attains a favorable balance of safety, feasibility, and efficiency. Its per-step cost stays largely insensitive to obstacle count and scales to high densities, where online uncertainty-reasoning baselines become either too conservative to reach the goal or too expensive to meet the real-time budget.^11^1Our code is available at

<!-- chunk {"id": "body-0014", "role": "body", "section": "Navigation in Dynamic Environments: Perception and Prediction", "weight": 1.0} -->

Safe operation in dynamic environments has classically been decomposed into estimating the evolving occupancy of the world and planning against it. A large body of work tracks moving obstacles by coupling simultaneous localization and mapping with multi-object tracking, or maintains dynamic occupancy representations through particle-based grids and random-finite-set filters, with continuous particle-based mapping pushed to real-time dense settings. In parallel, distance fields, whether learned or fused online from depth sensing, have become a favored geometric layer for their smooth, queryable structure. Our formulation inherits this representational viewpoint: rather than reasoning over raw occupancy, we operate directly on the predicted distance field, and we further treat the prediction error of that field as the object to be quantified. On the forecasting side, learned trajectory predictors such as Trajectron++ supply the multi-step obstacle motion that our planner consumes, and their residual errors are precisely what a safety layer must account.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Risk-Aware and Distributionally Robust Motion Planning", "weight": 1.0} -->

A complementary line of research embeds uncertainty directly into the planning objective or constraints. Chance-constrained formulations bound the probability of collision and have been studied extensively, from convex path planning with obstacles to probabilistic collision checking and planning in dynamic, uncertain environments. Because exact verification of collision constraints against non-convex moving obstacles is generally intractable, these methods typically approximate the free space or the obstacle set, e.g., by unions of convex regions, or accept conservative encodings of the nonconvex feasible set. Risk-sensitive planners instead optimize coherent risk measures such as the conditional value-at-risk, while distributionally robust approaches hedge against the worst-case distribution within an ambiguity set. The distributionally robust risk map, for instance, certifies CVaR-type safety even when the obstacle motion distribution is only imperfectly learned.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Risk-Aware and Distributionally Robust Motion Planning", "weight": 1.0} -->

These methods deliver strong guarantees, but the guarantee is only as good as the chosen set or error model, and calibrating it, e.g., selecting a Wasserstein radius or moment bounds, is itself nontrivial. The resulting min--max problem is moreover solved at planning time, so its cost compounds as the obstacle count grows. We share these safety concerns but trade this online worst-case optimization for an offline statistical procedure: a distribution-free conformal envelope is calibrated once, ahead of deployment, leaving only a lightweight coefficient-space update to run online. We do not claim an empirical advantage over distributionally robust planners, and a direct comparison under matched safety levels is left to future work; rather, we position FCP-MPC as a cheaper-online, finite-sample alternative.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Conformal Prediction for Safe Planning and Navigation", "weight": 1.0} -->

Conformal prediction (CP) has recently emerged as a distribution-free route to provable safety, converting heuristic predictor errors into sets with finite-sample coverage. In robotics it has been applied to planning among dynamic agents, to perception-based navigation with statistical assurances, and to decision-theoretic and ensemble-based control under imperfect predictions, with extensions to conformalized semantic maps. Adaptive conformal prediction further relaxes the exchangeability requirement, sustaining long-run coverage under distribution shift, and underlies online conformal schemes for motion planning. Most of these approaches, however, conformalize a scalar score online, whose cost grows with obstacle count and horizon. Moreover, the worst-case score definitions they require to certify safety over a region become intractable to enforce exactly.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Conformal Prediction for Safe Planning and Navigation", "weight": 1.0} -->

In contrast, we adopt the functional CP perspective and treat the residual distance field as a single element of a function space, conformalized as one object rather than point by point. This directly addresses both limitations. First, region-level safety holds by construction: the envelope covers the whole field, so no per-region worst-case score, the quantity prior CP methods cannot enforce exactly, is ever needed. Second, the functional object is low-rank, which functional PCA makes explicit; the few coefficients that describe it are what the controller conformalizes, so the safety check no longer scales with the number of obstacles.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Conformal Prediction for Safe Planning and Navigation", "weight": 1.0} -->

Most closely related is the egocentric conformal prediction (ECP) framework, our ECP-MPC baseline. ECP shares our premise of scoring how much closer obstacles are than predicted, rather than inflating a scalar margin for every obstacle, but it attaches that score to each robot *state* and conformalizes it online. Its uncertainty reasoning therefore runs in the planning loop and scales with the number of states queried, degrading as obstacle density grows (Section 8 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")). We instead conformalize the residual field as one functional object computed offline, so the certificate holds for any sampled trajectory (Theorems 2.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Conformal Prediction for Safe Planning and Navigation", "weight": 1.0} -->

‣ 7.1 Base Safety Guarantee via Functional Coverage ‣ 7 Safety Analysis and Asymptotic Guarantees ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")--3.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Conformal Prediction for Safe Planning and Navigation", "weight": 1.0} -->

‣ 7.2 Robust Guarantee Under Online Adaptation ‣ 7 Safety Analysis and Asymptotic Guarantees ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) and the per-step cost is essentially independent of how many obstacles or states the scene contains.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Split Conformal Prediction", "weight": 1.0} -->

Given exchangeable samples $\{z_{n}\}_{n=1}^{N}$ and a nonconformity score $s(\cdot)\in\mathbb{R}$ (larger meaning a worse fit), fix a target miscoverage level $\alpha\in$ and set where the $+\infty$ term supplies the finite-sample correction. For a fresh exchangeable sample $z_{N+1}$, with no assumption on the data distribution beyond exchangeability.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Adaptive Conformal Prediction", "weight": 1.0} -->

When the stream is non-exchangeable (e.g. under distribution shifts), the marginal guarantee (1 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) may fail. Adaptive conformal prediction (ACP) instead enforces a *long-run* guarantee by updating the threshold online from the observed miscoverage: with step size $\gamma>0$ and $\mathrm{err}_{t}=\mathbb{I}[\,s_{t}>\hat{q}_{t}\,]$, which drives the empirical miscoverage $\tfrac{1}{T}\sum_{t}\mathrm{err}_{t}$ to $\alpha$ for an arbitrary, even adversarial, sequence.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Let $\mathcal{Q}$ be the configuration space of a robot, and $\mathrm{x}=\mathrm{x}(\mathrm{q})\in\mathcal{X}\subseteq\mathbb{R}^{d}$ the position in the (compact) world $\mathcal{X}$ corresponding to $\mathrm{q}\in\mathcal{Q}$ through the forward kinematics, with $d=2$ or $3$. We write $\mathcal{A}=\mathcal{A}(\mathrm{q})\subseteq\mathcal{X}$ for the robot's footprint, a closed set, at configuration $\mathrm{q}$, and $\mathcal{A}_{t}\coloneqq\mathcal{A}(\mathrm{q}_{t})$. With control input $\mathrm{u}\in\mathcal{U}$, the robot evolves as The environment is dynamic.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Over a time window $t=0,\ldots,T$, let $\mathcal{O}_{t}\subseteq\mathcal{X}$ denote the union of moving obstacles at time $t$, typically realized as an occupancy map and *completely unknown* at planning time. We model $\{\mathcal{O}_{t}\}_{t=0}^{T}$ as a set-valued random process whose randomness captures the environmental variation, and assume each $\mathcal{O}_{t}$ is independent of $\mathrm{q}_{0},\mathrm{u}_{0},\ldots,\mathrm{q}_{t}$, so that the robot's motion does not influence the occupancy.^22^2Extending this to bidirectional robot--agent interaction is left as future work.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Problem 1 (Motion Planning with Probabilistic Safety Guarantee)", "weight": 1.0} -->

Design a policy $\mathrm{u}_{t}=\pi(\mathrm{q}_{t},\mathcal{H}_{t})$ that solves Here safety is required at the *per-step* level. That is, each step is collision-free with probability at least $1-\alpha$, which is the guarantee our conformal construction certifies in the closed loop (Theorems 2. ‣ 7.1 Base Safety Guarantee via Functional Coverage ‣ 7 Safety Analysis and Asymptotic Guarantees ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")--3.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem 1 (Motion Planning with Probabilistic Safety Guarantee)", "weight": 1.0} -->

‣ 7.2 Robust Guarantee Under Online Adaptation ‣ 7 Safety Analysis and Asymptotic Guarantees ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")). Throughout, we set the conformal miscoverage level to this same $\alpha$, so that a field-coverage guarantee at level $1-\alpha$ translates directly into per-step safety at level $1-\alpha$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem 1 (Motion Planning with Probabilistic Safety Guarantee)", "weight": 1.0} -->

The condition $\mathcal{A}_{t}\cap\mathcal{O}_{t}=\varnothing$ may be strengthened into where $\delta>0$ is a user-specified margin between $\mathcal{A}_{t}$ and $\mathcal{O}_{t}$. Since $\mathcal{O}_{t}$ is generally non-convex, exact verification of this condition is intractable even when $\mathcal{A}_{t}$ is a convex polytope. A typical remedy is to approximate $\mathcal{O}_{t}$ or the free space $\mathcal{X}\setminus\mathcal{O}_{t}$ by a union of convex regions.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problem 1 (Motion Planning with Probabilistic Safety Guarantee)", "weight": 1.0} -->

Instead of inheriting this assumption, we assume the footprint $\mathcal{A}(\mathrm{q})$ is a ball of radius $r_{\text{robot}}$ centered at $\mathrm{x}(\mathrm{q})$: and (4 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) reduces to a single query of $D(\cdot,\mathcal{O}_{t})$ at the center $\mathrm{x}_{t}$. The condition (1.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Problem 1 (Motion Planning with Probabilistic Safety Guarantee)", "weight": 1.0} -->

‣ 4 Problem Formulation ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) is now translated into To solve Problem 1.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Problem 1 (Motion Planning with Probabilistic Safety Guarantee)", "weight": 1.0} -->

‣ 4 Problem Formulation ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173."), the policy $\pi$ should incorporate the information collected up to $t$, $\mathcal{H}_{t}\coloneqq(\mathcal{O}_{0},\ldots,\mathcal{O}_{t})$, to secure future safety while maintaining deployment efficiency.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Problem 1 (Motion Planning with Probabilistic Safety Guarantee)", "weight": 1.0} -->

A feasible approach is to define $\pi(\mathrm{q}_{t},\mathcal{H}_{t})$ as the solution of the following MPC problem: where $(\mathrm{x}_{t+1|t},\ldots,\mathrm{x}_{t+N|t})$ is a path planned at $t$ from $\mathrm{x}_{t}$ and $\mathcal{H}_{t}$, and $(\mathcal{O}_{t+1|t},\ldots,\mathcal{O}_{t+N|t})$ are *predicted* occupancies at $t+1,\ldots,t+N$ from $\mathcal{H}_{t}$.^33^3While $\mathcal{O}_{t}$ is partially observable in practice, we assume full observability throughout.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Problem 1 (Motion Planning with Probabilistic Safety Guarantee)", "weight": 1.0} -->

Under partial observability, one may instead use a *conservative* estimate $\hat{\mathcal{O}}_{t}\supseteq\mathcal{O}_{t}$ that treats occluded and unknown space as occupied, and choose $\mathbf{x}^{\text{ref}}$ to balance exploration and efficiency via a *frontier* method. Since this only inflates the distance-field estimate, all theoretical claims remain valid at the cost of added conservativeness. A full treatment of partial observability is left as future work. The objective $\mathfrak{L}$ is defined as Several approaches are available for computing the predicted occupancies $\mathcal{O}_{t+i|t}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Problem 1 (Motion Planning with Probabilistic Safety Guarantee)", "weight": 1.0} -->

One common and mature route is to estimate the kinematic states of dynamic agents by detection and tracking of the dynamic agents from $\mathcal{H}_{t}$, then apply motion prediction models to predict their future motions, which is back-projected into $\mathcal{X}$ to infer $(\mathcal{O}_{t+1|t},\ldots,\mathcal{O}_{t+N|t})$. An alternative is end-to-end prediction, deploying a model that consumes raw lidar scans and predicts future shapes directly. We adhere to the former.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Problem 1 (Motion Planning with Probabilistic Safety Guarantee)", "weight": 1.0} -->

Since the predictions are imperfect, the associated distance functions may deviate from the true occupancies of the environment. Abbreviating $D_{t+i|t}(\mathrm{x})\coloneqq D(\mathrm{x},\mathcal{O}_{t+i|t})$, we define the *score function* as When $S_{t+i|t}(\mathrm{x})>0$, the predicted distance exceeds the true one: the obstacle is in fact closer than predicted, so the prediction *overestimates* safety at $\mathrm{x}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Problem 1 (Motion Planning with Probabilistic Safety Guarantee)", "weight": 1.0} -->

Correcting this underestimation of risk is exactly what is needed to enforce (6 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")), and is the target of our conformal construction.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Problem 1 (Motion Planning with Probabilistic Safety Guarantee)", "weight": 1.0} -->

Remark on what is proven. The constraint (6 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) (equivalently the per-step chance constraint in (1. ‣ 4 Problem Formulation ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173."))) states the desired *per-step* safety semantics, i.e., a bound on the probability of collision at each individual step.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Problem 1 (Motion Planning with Probabilistic Safety Guarantee)", "weight": 1.0} -->

Our formal guarantees do *not* certify this per-step probability pointwise in time. Rather, they establish its *long-run empirical* closed-loop counterpart for the receding-horizon controller: the time-averaged frequency of collision-free steps is at least $1-\alpha$ with probability one (Theorems 2. ‣ 7.1 Base Safety Guarantee via Functional Coverage ‣ 7 Safety Analysis and Asymptotic Guarantees ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")--3.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Problem 1 (Motion Planning with Probabilistic Safety Guarantee)", "weight": 1.0} -->

‣ 7.2 Robust Guarantee Under Online Adaptation ‣ 7 Safety Analysis and Asymptotic Guarantees ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Why Functional Conformal Prediction?", "weight": 1.0} -->

In contrast to prior conformal-prediction approaches in robotics, where a single scalar score function is typically considered, the error signal $S_{t+i|t}$ here is *functional*. Each $S_{t+i\mid t}\colon\mathcal{X}\to\mathbb{R}$ is an element of the Hilbert space $\mathscr{H}:=L^{2}(\mathcal{X})$, not a scalar. This motivates a CP framework tailored to such functional objects, namely functional conformal prediction (FCP). Conformalizing the field as a whole is what yields a certificate that holds for any trajectory satisfying it, independent of the sampler (Section 7 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Why Functional Conformal Prediction?", "weight": 1.0} -->

Its *practicality*, in turn, rests on two empirical properties of the residual field, which we verify on the ETH--UCY benchmark.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Why Functional Conformal Prediction?", "weight": 1.0} -->

First, the residual field is approximately *time-invariant*: per-cell residual statistics from two temporally disjoint halves of each scene agree closely, so $S_{t+i\mid t}\stackrel{{\scriptstyle d}}{{\approx}}S_{t^{\prime}+i\mid t^{\prime}}$ for $t\neq t^{\prime}$. Second, the field is *low-rank*: a few functional principal components already capture most of its variance, so it admits the compact expansion: with FPCA modes $\{\psi_{k}\}_{k=1}^{r}\subset L^{2}(\mathcal{X})$ that are stable across $t$. The uncertainty is thus spatially structured and compressible, even though it is not reducible to a simple geometric cue such as path curvature or visitation density.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Why Functional Conformal Prediction?", "weight": 1.0} -->

These two properties, which we quantify on the ETH--UCY benchmark in Section 8.3 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") (Figs.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Why Functional Conformal Prediction?", "weight": 1.0} -->

3 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") and 5 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")), are exactly what make the field-level envelope cheap to deploy.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Why Functional Conformal Prediction?", "weight": 1.0} -->

The modes $\{\psi_{k}\}$ and the resulting envelope $\mathsf{U}_{t+i|t}$ are estimated once, offline, while online the controller merely evaluates $\mathsf{U}_{t+i|t}(\mathrm{x})$ point-wise along its rollouts, keeping the per-step cost low. To be self-contained, we now explain how FCP turns these prediction errors into a safety margin.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Sketch of Core Pipeline", "weight": 1.0} -->

Our goal is to construct a high-probability upper bound $\mathsf{U}_{t+i\mid t}$ for $S_{t+i|t}$: Once such $\mathsf{U}_{t+i|t}$ is identified, it yields a probabilistic lower bound of $D_{t+i}$: We then replace the constraint (7 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) by However, directly computing such a bound in the infinite-dimensional Hilbert space $\mathscr{H}$ is generally intractable and often unnecessary. Instead, we leverage the functional conformal prediction framework and bound a finite-dimensional projection of $S_{t+i\mid t}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Sketch of Core Pipeline", "weight": 1.0} -->

We adopt a *divide-and-conquer* strategy. Decompose where $\breve{S}_{t+i|t}$ is a *finite-dimensional* projection of $S_{t+i|t}$, constructed in Section 5.3 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.").

<!-- chunk {"id": "body-0048", "role": "body", "section": "FCP-Based Upper Bound", "weight": 1.0} -->

The most intricate part of the pipeline is constructing the finite-dimensional projection $\breve{S}_{t+i|t}$ of $S_{t+i|t}$ and its high-confidence upper bound $\breve{\mathsf{U}}_{t+i|t}$. We define a $p_{i}$-dimensional subspace $\mathscr{V}_{i}\subset\mathscr{H}$ and let where $\Pi_{\mathscr{V}_{i}}:\mathscr{H}\to\mathscr{V}_{i}$ denotes the projection operator. It then remains to find a confidence set $\mathscr{T}_{t+i|t}$ satisfying a distribution-free coverage guarantee of the form where $\mathscr{T}_{t+i\mid t}\subset\mathscr{V}_{i}$ is a conformal prediction set on the projected space.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Data-driven basis functions", "weight": 1.0} -->

In our setting, the projection subspace $\mathscr{V}_{i}\subset\mathscr{H}$ is learned from data at each horizon index $i=1,\ldots,N$ via functional principal components. Let $\{S^{(n)}_{t+i\mid t}\}_{n=1}^{N}$ denote a collection of score functions at step $i$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Data-driven basis functions", "weight": 1.0} -->

We choose an orthonormal basis $\{\psi_{i,j}\}_{j=1}^{p_{i}}$ spanning $\mathscr{V}_{i}$ as the $p_{i}$ leading principal components of this sample, in the standard $L^{2}$ sense, and collect the basis evaluations at $\mathrm{x}$ into the vector For any $S\in\mathscr{H}$, its coefficient vector in this basis is so that the projection admits the expansion The dimension $p_{i}$ of $\mathscr{V}_{i}$ may be fixed or selected from the sample size and a target approximation accuracy; we treat it as a modeling parameter.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Inductive conformal prediction in coefficient space", "weight": 1.0} -->

We adopt the inductive conformal predictor (ICP) framework to conformalize a high-density region in coefficient space. We split the coefficient samples $\{\xi^{(n)}\}_{n=1}^{N}$ into a training subset and a calibration subset Cal. A parametric conformity score $g(\xi)$ is fitted on the training subset, and a threshold is chosen using the empirical quantile on the calibration subset.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Gaussian mixture model and ellipsoidal coefficient regions", "weight": 1.0} -->

We model the distribution of the projected coefficients $\xi\in\mathbb{R}^{p_{i}}$ using a $K$-component Gaussian mixture model (GMM). Specifically, we fit the mixture weights $\widehat{\pi}_{k}$, means $\widehat{\mu}_{k}$, and covariance matrices $\widehat{\Sigma}_{k}$ to the training coefficients and obtain the estimated density where $\mathcal{N}(\cdot;\mu,\Sigma)$ denotes the multivariate Gaussian density (not to be confused with the FPCA basis functions $\psi_{i,j}$).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conformity score", "weight": 1.0} -->

Following the construction in Eqs. -- of, we define a max-component pseudo-density conformity score from the fitted GMM parameters: This score assigns higher conformity to coefficients lying in high-density regions of at least one mixture component, thereby yielding ellipsoidal regions in the coefficient space.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conformity score", "weight": 1.0} -->

Let $\{\xi^{(n)}\}_{n\in\mathsf{Cal}}$ be the coefficients of the calibration set and define Then the ICP prediction set in coefficient space is where $\xi_{t+i\mid t}\coloneqq\xi_{i}(S_{t+i\mid t})$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conformity score", "weight": 1.0} -->

We derive a high-confidence upper bound of $\breve{S}_{t+i|t}$ as Since $\breve{S}_{t+i|t}(\mathrm{x})=\xi_{t+i\mid t}^{\top}\psi_{i}(\mathrm{x})$, the coverage (17 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) immediately gives It turns out that $\breve{\mathsf{U}}_{t+i|t}$ admits a closed-form expression whose detailed derivation is given in Appendix A ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conformity score", "weight": 1.0} -->

No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.").

<!-- chunk {"id": "body-0057", "role": "body", "section": "Bounding Projection Residuals", "weight": 1.0} -->

To translate coefficient-space uncertainty back to the original discretized function, we account for the projection residual in sup norm.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Bounding Projection Residuals", "weight": 1.0} -->

Define the reconstruction error for sample $y^{(n)}$ by Using the calibration split, we set the projection residual to the conformal quantile where the $+\infty$ term supplies the finite-sample correction, which yields By a union bound over the two events (18 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) and (21 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")), each holding with probability at least $1-\alpha/2$, the decomposition (13 grants funded by MSIT

<!-- chunk {"id": "body-0059", "role": "body", "section": "Bounding Projection Residuals", "weight": 1.0} -->

No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) and the envelope (14 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) yield the desired coverage guarantee (10 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) at level

<!-- chunk {"id": "body-0060", "role": "body", "section": "Bounding Projection Residuals", "weight": 1.0} -->

Remark on practical implementation. The projection coefficients $\xi_{i,j}(S)=\langle S,\psi_{i,j}\rangle$ generally require integration over $\mathcal{X}$, which is expensive when $S$ is only available through costly distance-transform evaluations on a fine grid. Therefore, in implementation we approximate the projection (and its point-wise evaluations) using only finitely many grid points $\bar{\mathcal{X}}\subset\mathcal{X}$. For later use, we define the *discretization resolution* of $\bar{\mathcal{X}}$ as which is finite since $\mathcal{X}$ is bounded.

<!-- chunk {"id": "body-0061", "role": "body", "section": "FCP-Informed Safe Motion Planning", "weight": 1.0} -->

We now embed the conformalized distance lower bound into a receding-horizon motion planner, following the safe-planning template of but adapting it to our *fieldwise* representation. The conformalization is performed over the entire field offline and cached in compact coefficient form; online, the controller neither re-fits the GMM nor recomputes per-point distances, but consults the cached field and applies a lightweight scalar update that also absorbs any deployment-time distribution shift (Section 6.3 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")). Beyond keeping the per-step cost low, this hands the planner a continuous, queryable safety field, directly suited to scoring the many candidate rollouts of an MPC step.

<!-- chunk {"id": "body-0062", "role": "body", "section": "FCP-Informed Safe Motion Planning", "weight": 1.0} -->

Figure 1 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") summarizes the pipeline.

<!-- chunk {"id": "body-0063", "role": "body", "section": "MPC Formulation", "weight": 1.0} -->

Incorporating the conformalized constraint (12 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) into (7 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) leads to the following MPC formulation: where $\delta_{d}>0$ is the discretization resolution of $\mathcal{X}$ defined in (22 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National

<!-- chunk {"id": "body-0064", "role": "body", "section": "MPC Formulation", "weight": 1.0} -->

University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")), and $\bar{\mathrm{x}}_{t+i|t}$ denotes the *projection* of $\mathrm{x}_{t+i|t}=\mathrm{x}(\mathrm{q}_{t+i|t})$ onto the finite set $\bar{\mathcal{X}}$: To solve this, a sampling-based MPC, such as model predictive path integral (MPPI), can be used as an affordable implementation.^44^4In implementation we enforce a horizon-dependent margin $\rho_{i}=r_{\text{robot}}+\delta+\delta_{d}-\Delta_{i}$ with $\Delta_{i}=\tfrac{1}{2}\,a_{\mathrm{lat}}\bigl((i-1)\Delta t\bigr)^{2}$

<!-- chunk {"id": "body-0065", "role": "body", "section": "MPC Formulation", "weight": 1.0} -->

($a_{\mathrm{lat}}=v_{\max}\omega_{\max}$ in 2D), the lateral distance the robot can deviate by step $i$ (cf.).

<!-- chunk {"id": "body-0066", "role": "body", "section": "MPC Formulation", "weight": 1.0} -->

Subtracting it relaxes the margin at far horizons, where the robot can still steer clear. Since $\Delta_{1}=0$, the applied step keeps full clearance, so the guarantees of Section 7 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") are unaffected.

<!-- chunk {"id": "body-0067", "role": "body", "section": "MPC Formulation", "weight": 1.0} -->

Hard constraints vs. soft penalization. While theoretically favorable, the conformalized constraints (23 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) may still produce extremely small feasible sets when $i$ is large. Moreover, the fieldwise conformalization is more than a binary feasibility test: at every point it furnishes a signed, continuous margin. This motivates the notion of *soft constraints*. Instead of enforcing the hard constraints explicitly, we fold them into the MPC objective as a graded term that penalizes violations.

<!-- chunk {"id": "body-0068", "role": "body", "section": "MPC Formulation", "weight": 1.0} -->

Specifically, we define so that the constraint (23 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) is identical to $g_{t+i|t}(\mathrm{x})\leq 0$. The soft version of the MPC is then where $\mathfrak{L}_{w}$ is defined as for a user-defined constant $w>0$. The penalty term discourages incursions into the conformalized unsafe region ($g_{t+i|t}>0$).

<!-- chunk {"id": "body-0069", "role": "body", "section": "MPC Formulation", "weight": 1.0} -->

The weight $w>0$ is fixed rather than adapted, so (25 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) is a quadratic-penalty relaxation of its hard counterpart (23 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")): its minimizer approaches the hard-constrained solution as $w\to\infty$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "MPC Formulation", "weight": 1.0} -->

For finite $w$, it stays well-defined even where the hard feasible set is empty, replacing the strict closed-loop guarantee with one that holds up to a controllable slack vanishing as $w\to\infty$ (Theorem 4. ‣ 7.3 Safety of the Soft Deployment ‣ 7 Safety Analysis and Asymptotic Guarantees ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")). We compare both formulations in our 2D pedestrian experiments.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Stage 1: Offline Initialization", "weight": 1.0} -->

The key design principle is to separate the field-level *statistical initialization*, computed once offline, from the *lightweight adaptation* performed online. Offline, we exploit a large calibration set and a flexible GMM to construct the most accurate initial envelope possible, a cost paid only *once*, before deployment. Online, the GMM is never evaluated; the controller instead adapts the cached envelope directly from streaming residual observations and a prescribed target violation level.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Stage 1: Offline Initialization", "weight": 1.0} -->

During the offline stage, we assume access to $n_{\mathsf{Cal}}$ independent snapshots of the environment, from which we obtain the dataset for the $i$-th planning step: We then apply FPCA to obtain an orthonormal basis $\{\psi_{i,1},\dots,\psi_{i,p_{i}}\},$ which produces the coefficient vector of each $S\in\mathcal{D}_{\mathsf{Cal},i}$ according to (16 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")).

<!-- chunk {"id": "body-0073", "role": "body", "section": "Stage 1: Offline Initialization", "weight": 1.0} -->

Remark on exchangeability of the calibration set. The split-conformal coverage (1 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) assumes the calibration and test residual fields are exchangeable. In practice the calibration fields $\{S^{(j)}_{t+i\mid t}\}$ are extracted from overlapping prediction windows of a limited number of recordings, so temporally adjacent samples are correlated and exchangeability holds only approximately. We mitigate this by subsampling across time when forming $\mathcal{D}_{\mathsf{Cal},i}$ to decorrelate successive fields.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Stage 1: Offline Initialization", "weight": 1.0} -->

Furthermore, since the formal offline guarantee heavily relies on this assumption, we treat the field coverage of Appendix B grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") as the operative empirical check. The online adaptive update, which makes no exchangeability assumption, is a further safeguard against any residual violation.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Stage 1: Offline Initialization", "weight": 1.0} -->

Using the coefficient dataset $\{\xi_{i}(S_{t+i|t}^{(j)})\}_{j=1}^{n_{\mathsf{Cal}}},$ we fit a Gaussian mixture model and apply the coefficient-space conformal construction of Section 5.3.1 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.").

<!-- chunk {"id": "body-0076", "role": "body", "section": "Stage 1: Offline Initialization", "weight": 1.0} -->

This yields the mixture parameters $\{\widehat{\pi}_{i,k},\widehat{\mu}_{i,k},\widehat{\Sigma}_{i,k}\}_{k=1}^{K}$, the conformal level $\lambda_{i}$ (and hence the per-component radii $r_{i,k}\equiv r_{i,k}(\lambda_{i})$ of (38 ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173."))), and the projection residual $\varepsilon_{i}$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Stage 1: Offline Initialization", "weight": 1.0} -->

For each horizon index $i$, we cache the offline tuple the full collection of horizon-indexed tuples cached by the controller. Crucially, after deployment the online controller only *evaluates* the closed-form envelope (19 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) from these cached parameters and never *re-fits* the GMM.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Stage 1: Offline Initialization", "weight": 1.0} -->

In practice, two grids $\widehat{\mu}_{i,k}^{\top}\psi_{i}(\cdot)$ and $(\psi_{i}(\cdot)^{\top}\widehat{\Sigma}_{i,k}\psi_{i}(\cdot))^{1/2}$ are precomputed once, so an envelope update reduces to recombining them with the (scalar-)adapted radii.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Stage 2: Online Adaptation", "weight": 1.0} -->

Once the robot starts moving, the cached envelope is adapted online through a single scalar per horizon index, in the spirit of adaptive conformal prediction. Because the upper envelope (19 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) is controlled by the radii $r_{i,k}$, we introduce an adjustable multiplier $c_{t+i|t}$ on those radii, and define the *parameterized* upper envelope for $c\geq 0$ (and $\mathsf{U}_{t+i|t}(\mathrm{x};c)\coloneqq\mathsf{U}_{t+i|t}(\mathrm{x};0)$ for $c<0$).

<!-- chunk {"id": "body-0080", "role": "body", "section": "Stage 2: Online Adaptation", "weight": 1.0} -->

The original envelope is recovered at $c=1$: $\mathsf{U}_{t+i|t}(\mathrm{x})=\mathsf{U}_{t+i|t}(\mathrm{x};1)$. Defining the smallest multiplier that covers the realized field, we take the violation indicator which, by (28 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")), is equivalent to This keeps the band a valid envelope at all times and yields a clean coverage event.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Stage 2: Online Adaptation", "weight": 1.0} -->

At time $t$, once a realized residual field $S_{t+i|t}$ matures for horizon index $i$, we evaluate the indicator (29 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) on the discretization grid $\bar{\mathcal{X}}$ alone (cost $O(Kp_{i}|\bar{\mathcal{X}}|)$, with no full-field reconstruction and no GMM re-fit), and update the multiplier as Here $c_{t+i|t}$ is the multiplier applied to horizon $i$ at planning time $t$; once the corresponding residual matures, it is updated to $c_{t+1+i|t+1}$ for use at the next planning time.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Stage 2: Online Adaptation", "weight": 1.0} -->

The envelope inflates when the realized miscoverage exceeds $\alpha$ and contracts otherwise, driving the long-run miscoverage to $\alpha$. Note that the residual of a prediction made at time $t$ for horizon $i$ becomes available only at time $t+i$, after the environment state has been observed; the AFCP update therefore uses delayed feedback, without access to future information.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Stage 2: Online Adaptation", "weight": 1.0} -->

The corresponding online envelope simply rescales the cached radii, Thus, offline GMM fitting only initializes the cached parameters, while online adaptation moves a single scalar $c_{t+i|t}$ (initialized at $c_{i|0}=1$), recomputed against the precomputed grids of (26 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) without re-evaluating the GMM.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Stage 2: Online Adaptation", "weight": 1.0} -->

The following theorem is an immediate consequence of \[15, Proposition 4.1\].

<!-- chunk {"id": "body-0085", "role": "body", "section": "Safety Analysis and Asymptotic Guarantees", "weight": 1.0} -->

This section establishes the safety guarantees of the proposed framework. A key advantage of the functional formulation is that safety holds *at every point of the field*, for *any* planned trajectory satisfying the tightened conformal constraint, independent of how the control space is sampled, because the bound is certified over the entire field rather than along a single path.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Safety Analysis and Asymptotic Guarantees", "weight": 1.0} -->

We first present the base safety theorem, assuming the functional envelope covers the true score. We then extend it to a robust guarantee for dynamic environments through the online adaptive update, and finally certify the soft-penalty deployment used in dense scenes.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Base Safety Guarantee via Functional Coverage", "weight": 1.0} -->

The following theorem shows that if the spatial envelope asymptotically covers the true score, the closed-loop system is safe.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Robust Guarantee Under Online Adaptation", "weight": 1.0} -->

Theorem 2. ‣ 7.1 Base Safety Guarantee via Functional Coverage ‣ 7 Safety Analysis and Asymptotic Guarantees ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") establishes the foundational logic mapping functional coverage to point-wise safety. In offline CP, the exact coverage equality $\lim_{T\to\infty}\dots=1-\alpha$ relies on exchangeability of the calibration and test data. In dynamic environments, however, unforeseen distribution shifts can invalidate this assumption.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Robust Guarantee Under Online Adaptation", "weight": 1.0} -->

To robustify the framework, we drop exchangeability and employ the AFCP method of Section 6.3 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173."). The following theorem extends the guarantee to dynamic, non-exchangeable environments.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Safety of the Soft Deployment", "weight": 1.0} -->

Theorem 2. ‣ 7.1 Base Safety Guarantee via Functional Coverage ‣ 7 Safety Analysis and Asymptotic Guarantees ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") certifies the *hard* feasibility filter.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Safety of the Soft Deployment", "weight": 1.0} -->

We now show that the *soft* deployment (25 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")), the variant we recommend in dense scenes where the hard feasible set is frequently empty, admits the same safety conclusion up to a controllable slack that vanishes as the penalty weight grows.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Safety of the Soft Deployment", "weight": 1.0} -->

Throughout, $z=(\mathbf{q},\mathbf{u})$ denotes the (dynamically feasible) decision variable, $z_{w}$ a minimizer of the soft program (25 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) with weight $w$, $\mathrm{x}^{w}_{t+1|t}$ the first planned position it applies, and $\bar{\mathrm{x}}^{w}_{t+1|t}\in\bar{\mathcal{X}}$ its grid projection.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Planar Navigation with Pedestrians", "weight": 1.0} -->

We first evaluate FCP-MPC on the ETH--UCY pedestrian benchmark, a standard collection of recorded human-crowd trajectories comprising five scenes that span a range of crowd densities. In each scene, a robot with a circular footprint of radius $r_{\mathrm{robot}}=0.4$ m navigates toward a fixed goal while the recorded pedestrians act as the dynamic obstacles $\mathcal{O}_{t}$. The robot follows the unicycle dynamics driven by the sampling-based controller of Section 6 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173."), implemented with MPPI using 1,200 sampled rollouts over a horizon of $N=12$ steps at a planning period $\Delta t=0.4$ s.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Planar Navigation with Pedestrians", "weight": 1.0} -->

All controllers are implemented in Python (NumPy) and run on an Apple M4 with $16$ GB of unified memory; reported control times are wall-clock per planning step.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Planar Navigation with Pedestrians", "weight": 1.0} -->

At each planning step the controller consumes multi-step pedestrian forecasts from Trajectron++. The residual between the predicted and realized distance fields is exactly the quantity our functional conformal layer corrects. Following Section 6.3 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173."), the envelope is conformalized once offline, per horizon index, from a held-out calibration split ($30\%$ of each scene's residual-field samples) at the target miscoverage level $\alpha=0.1$, using $K=7$ GMM components and $p_{i}=5$ FPCA modes per step.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Planar Navigation with Pedestrians", "weight": 1.0} -->

When enabled, the online AFCP update (30 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) drives the realized miscoverage toward $\alpha=0.1$. The conformal field is discretized on a $128\times 128$ workspace grid, giving a discretization resolution $\delta_{d}\approx 0.18$--$0.27$ m across scenes (22 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")).

<!-- chunk {"id": "body-0097", "role": "body", "section": "Planar Navigation with Pedestrians", "weight": 1.0} -->

The resulting offline tuple collection $\{\Pi_{i}\}_{i=1}^{N}$ (27 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) occupies only $\approx 5$ MB, after which the online controller merely consults this cached field.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Planar Navigation with Pedestrians", "weight": 1.0} -->

We deploy the same offline field in two ways, as a hard feasibility filter (FCP-MPC (hard)) and as a soft penalty (FCP-MPC (soft)), and compare against three baselines run under the identical planner: ACP-MPC, CC-MPC, and ECP-MPC. To keep the comparison about the conformal *construction* rather than its tuning, every method shares this identical goal-anchored planner and is calibrated to the *same* target miscoverage level $\alpha=0.1$. Each baseline retains its own native conformal parameters (its per-obstacle or per-state radius and adaptive step size) set to that level, so the conservativeness we report for ACP and ECP reflects their score construction rather than an unfavorable hyperparameter choice.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Planar Navigation with Pedestrians", "weight": 1.0} -->

Each episode terminates when the robot reaches the goal within $0.6$ m or a step budget of $100$ steps ($300$ for the larger univ scene) is exhausted (reported as "timeout"). We report four closed-loop metrics: (i) collision rate, (ii) infeasible rate, (iii) steps-to-goal, and (iv) per-step control time (ms). A collision is recorded when the distance from the robot to the nearest pedestrian falls below $r_{\mathrm{safe}}=r_{\mathrm{robot}}+r_{\mathrm{obs}}\approx 1.11$ m (with $r_{\mathrm{obs}}=1/\sqrt{2}$ m); the soft-penalty methods carry no infeasible rate by construction (N/A). Collision rate, infeasible rate, and steps-to-goal are reported as mean $\pm$ standard deviation over $10$ independent MPPI sampler seeds, each re-randomizing the sampling-based rollouts.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Planar Navigation with Pedestrians", "weight": 1.0} -->

For each seed we first average over the scene's evaluation windows ($3$ windows per scene), and the seed spread then quantifies the closed-loop controller's run-to-run variability. Table 1 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") reports the quantitative results and Fig. 8 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") shows representative closed-loop trajectories.

<!-- chunk {"id": "body-0101", "role": "body", "section": "3D Quadrotor Benchmark", "weight": 1.0} -->

We evaluate FCP-MPC in a physics-based quadrotor navigation task implemented in PyBullet. We set $\mathcal{Q}=\mathbb{R}^{3}$, with $\mathrm{q}\in\mathcal{Q}$ the center of mass (CoM) of the quadrotor, which is velocity-controlled: The quadrotor has radius $r_{\text{robot}}=0.1$ and is equipped with a low-level PID controller running at 240 Hz, while the high-level MPC planner operates at a slower planning period $\Delta t=0.1\,\mathrm{s}$.

<!-- chunk {"id": "body-0102", "role": "body", "section": "3D Quadrotor Benchmark", "weight": 1.0} -->

Since $\Delta t$ is much larger than the PID control period, the quadrotor dynamics may be approximated by a first-order integrator, $\mathrm{q}_{t+1}=\mathrm{q}_{t}+\Delta t\cdot\mathrm{u}_{t}.$ Within a bounded 3D workspace we spawn $N_{\text{obs}}$ spherical dynamic obstacles of radius $0.2$. Each obstacle is a kinematic agent with stochastic mode switching among several motion patterns, including constant-velocity, turning, wandering, and stop-and-go behaviors. Additive process noise is applied to the obstacle dynamics, inducing increasing prediction uncertainty over the planning horizon. At each planning step, the controller receives recent obstacle state histories and predicted obstacle trajectories over a horizon $N=12$; a constant-velocity predictor serves as the base prediction model, and prediction noise is injected to emulate prediction errors.

<!-- chunk {"id": "body-0103", "role": "body", "section": "3D Quadrotor Benchmark", "weight": 1.0} -->

Oracle future trajectories are used solely for evaluation and metric computation, and the "oracle future noise" reported in Section 8.5 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") perturbs these evaluation-only futures.

<!-- chunk {"id": "body-0104", "role": "body", "section": "3D Quadrotor Benchmark", "weight": 1.0} -->

The planner samples endpoint candidates and generates smooth quintic polynomial trajectories in $\mathbb{R}^{3}$. Unsafe trajectories are filtered by the conformal lower-bound constraint, and the minimum-cost feasible one is selected. Each episode terminates once the robot reaches the goal within $0.25\,\mathrm{m}$ or a maximum step limit is reached.

<!-- chunk {"id": "body-0105", "role": "body", "section": "3D Quadrotor Benchmark", "weight": 1.0} -->

Due to the higher-dimensional workspace and the abundance of free space in 3D, we deploy a *fully offline* functional conformal envelope here: unlike the 2D case, excessive conservativeness does not immediately block progress, so the conformalized worst-case envelope can be enforced directly without online adaptation. The field is discretized on a $40\times 40\times 40$ grid over the $10\times 10\times 8$ m workspace, giving $\delta_{d}=0.208$ m (22 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")). The cached tuples $\{\Pi_{i}\}_{i=1}^{N}$ again occupy only a few megabytes, so online deployment reduces to point-wise queries of this stored field.

<!-- chunk {"id": "body-0106", "role": "body", "section": "3D Quadrotor Benchmark", "weight": 1.0} -->

We use the same closed-loop metrics as in the 2D study: collision rate, infeasible rate, steps-to-goal, and per-step control time, with collision now recorded when the minimum robot--obstacle distance violates $r_{\mathrm{safe}}$. All metrics are averaged over the evaluated seeds.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Properties of the Residual Field", "weight": 1.0} -->

We first examine the two properties of the residual field that justify conformalizing the envelope offline (Section 5.1 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")).

<!-- chunk {"id": "body-0108", "role": "body", "section": "Properties of the Residual Field", "weight": 1.0} -->

Figures 3 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") and 4 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") establish *time-invariance*: per-cell residual statistics estimated from two temporally disjoint halves of each scene agree closely (cell-mean correlation $r=0.71$--$0.91$ across eth, univ, and hotel), so the field is a stable property of the scene rather than of a particular time.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Properties of the Residual Field", "weight": 1.0} -->

Figures 5 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") and 6 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") establish *low rank*: an FPCA of the residual fields finds that $5$--$7$ components already explain $90\%$ of the variance on most scenes, with smooth, scene-frame leading eigenfunctions.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Properties of the Residual Field", "weight": 1.0} -->

Together these confirm that the field is spatially structured and compressible, without reducing to a simple geometric cue such as path curvature or visitation density, which is what lets an offline-conformalized envelope transfer online at low cost.

<!-- chunk {"id": "body-0111", "role": "body", "section": "2D Pedestrian Navigation", "weight": 1.0} -->

Table 1 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") reports quantitative results on the ETH--UCY pedestrian datasets, and Fig. 8 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") shows representative closed-loop trajectories of FCP-MPC and the baselines. Several consistent trends emerge across all scenes.

<!-- chunk {"id": "body-0112", "role": "body", "section": "2D Pedestrian Navigation", "weight": 1.0} -->

The baselines trade off along a single axis. CC-MPC has a zero infeasible rate by construction and attains low collision rates, but is conservative and slow, trading progress for caution. Specifically, it times out in the most crowded scenes (univ, zara2). ECP-MPC incurs substantially higher online cost than the other methods ($40$--$83$ ms versus a few milliseconds for FCP-MPC), though it stays below the $0.4$ s planning period in this 2D benchmark. ACP-MPC is cheap and attains low collisions on some scenes, but its scalar online adaptation leaves high infeasible rates and frequent timeouts in dense, dynamic scenes.

<!-- chunk {"id": "body-0113", "role": "body", "section": "2D Pedestrian Navigation", "weight": 1.0} -->

FCP-MPC exposes a clear safety--feasibility trade-off between its two deployments of the same offline field. The *hard* variant enforces the envelope as a feasibility filter and inherits the closed-loop guarantee: collisions stay competitive in the more open scenes (e.g., eth), but the worst-case envelope compounds over the horizon, leaving a non-zero infeasible rate and higher collisions in the densest scenes (univ, zara1). The *soft* variant removes infeasibility on every scene and gives the shortest paths (lowest steps-to-goal on all five scenes), at the cost of a modest collision rate. Both keep the control time far below ECP-MPC (a few milliseconds vs. tens), because the uncertainty is quantified offline and the controller only evaluates the cached conformal field online.

<!-- chunk {"id": "body-0114", "role": "body", "section": "2D Pedestrian Navigation", "weight": 1.0} -->

Where the hard variant's collisions come. The closed-loop guarantee of Theorem 2.

<!-- chunk {"id": "body-0115", "role": "body", "section": "2D Pedestrian Navigation", "weight": 1.0} -->

‣ 7.1 Base Safety Guarantee via Functional Coverage ‣ 7 Safety Analysis and Asymptotic Guarantees ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") applies only on steps where the hard-constrained MPC (23 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) is feasible, whereas the collision rates in Table 1 grants funded by MSIT No. 2022-0-00124,

<!-- chunk {"id": "body-0116", "role": "body", "section": "2D Pedestrian Navigation", "weight": 1.0} -->

No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") are computed over the *full* episode, including fallback (brake-to-hover) steps taken after infeasibility that lie outside the theorem's premise.

<!-- chunk {"id": "body-0117", "role": "body", "section": "2D Pedestrian Navigation", "weight": 1.0} -->

Two distinct mechanisms inflate the hard variant's full-episode collisions in the dense scenes, and we separate them rather than attribute everything to fallback. Restricting the collision rate to the steps where the certified filter is actually feasible, it falls within the target $\alpha=0.1$ on *every* scene ($0.000$, $0.006$, $0.026$, $0.027$, $0.044$ on eth, hotel, univ, zara1, zara2; Table 3 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")), well below the full-episode rates.

<!-- chunk {"id": "body-0118", "role": "body", "section": "2D Pedestrian Navigation", "weight": 1.0} -->

The excess is carried by the post-infeasibility fallback steps, whose collision rate is $0.33$--$0.37$ on the dense scenes, rather than by failures of the certified filter where it is active.

<!-- chunk {"id": "body-0119", "role": "body", "section": "2D Pedestrian Navigation", "weight": 1.0} -->

The soft variant tells a complementary story. It collides at a broadly uniform $0.17$--$0.19$ across scenes (hotel lower, $0.045$) rather than concentrating in the harder ones. Since the field coverage meets the target throughout (Appendix B grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")), this reflects a progress--safety trade-off of the penalty, not envelope undercoverage (Section 9 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")).

<!-- chunk {"id": "body-0120", "role": "body", "section": "2D Pedestrian Navigation", "weight": 1.0} -->

Effect of online envelope adaptation. The offline functional envelope is conformalized once on held-out data. Online adaptation is an *optional* refinement that, in the spirit of adaptive conformal prediction, rescales the cached radii through a single scalar $c_{t+i|t}$ per horizon index via (30 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")), driving the realized miscoverage toward $\alpha$ without re-fitting the GMM.

<!-- chunk {"id": "body-0121", "role": "body", "section": "2D Pedestrian Navigation", "weight": 1.0} -->

Table 2 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") isolates its effect, and the changes are small: the hard-constraint collision and infeasible rates shift only marginally, mostly a slight increase that stays within one standard deviation, and the soft variant, already feasible by construction, shifts only slightly. This in-distribution neutrality is expected, since the offline-conformalized envelope already satisfies the required coverage, so the online update neither helps nor hurts materially when deployment matches calibration.

<!-- chunk {"id": "body-0122", "role": "body", "section": "2D Pedestrian Navigation", "weight": 1.0} -->

Because it merely recombines the precomputed grids of Section 5.2 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173."), it adds only a few milliseconds per step and stays below the cost of ECP-MPC. This sets up the deployment-time density shift of Section 8.6 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173."), where calibration and deployment intentionally differ and the update becomes consequential.

<!-- chunk {"id": "body-0123", "role": "body", "section": "3D Quadrotor Navigation", "weight": 1.0} -->

Recall the 3D setup of Section 8.2 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173."): a PyBullet quadrotor threading spherical dynamic obstacles under a constant-velocity predictor, the planner replanning every $\Delta t=0.1$ s.

<!-- chunk {"id": "body-0124", "role": "body", "section": "3D Quadrotor Navigation", "weight": 1.0} -->

Table 4 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") reports closed-loop results at $N_{\text{obs}}=280$ dynamic obstacles with noisy predictions (prediction noise $0.2$, obstacle process noise $0.22$, oracle future noise $0.2$), averaged over $17$ seeds. Because absolute timings depend on hardware and implementation, we report per-step control time to compare how each method's cost *scales* with $N_{\mathrm{obs}}$ on a common platform, not to assert an absolute real-time threshold.

<!-- chunk {"id": "body-0125", "role": "body", "section": "3D Quadrotor Navigation", "weight": 1.0} -->

Since all controllers share the same goal-anchored planner, the differences in Table 4 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") stem from the conformal method alone. They fall along two axes: (i) how conservative each safety construction is, i.e., whether the robot reaches the goal at all, and (ii) how expensive it is per step.

<!-- chunk {"id": "body-0126", "role": "body", "section": "3D Quadrotor Navigation", "weight": 1.0} -->

The two baselines that enforce uncertainty as a *hard* exclusion never reach the goal. ACP-MPC inflates a scalar conformal radius around each obstacle and ECP-MPC conformalizes an egocentric score at each robot state; both fly the full horizon, but their inflation is too conservative to thread $280$ moving obstacles, so they time out on every seed. FCP-MPC (hard) enforces the *same* style of hard feasibility filter and inherits the guarantee of Theorems 2. ‣ 7.1 Base Safety Guarantee via Functional Coverage ‣ 7 Safety Analysis and Asymptotic Guarantees ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")--3.

<!-- chunk {"id": "body-0127", "role": "body", "section": "3D Quadrotor Navigation", "weight": 1.0} -->

‣ 7.2 Robust Guarantee Under Online Adaptation ‣ 7 Safety Analysis and Asymptotic Guarantees ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173."), but over a conformal *field* rather than per-obstacle inflation. This is markedly less conservative, yet at this extreme density even it eventually exhausts the feasible set and times out. No hard filter clears $280$ obstacles, but our field bound is the least conservative of the three and runs at the lowest per-step cost of any method, whereas ECP-MPC is by far the most expensive.

<!-- chunk {"id": "body-0128", "role": "body", "section": "3D Quadrotor Navigation", "weight": 1.0} -->

Relaxing the bound from a constraint to a penalty restores progress. CC-MPC, a purely soft formulation with no spatial uncertainty model, reaches the goal on 41% of seeds but is slow and less safe. FCP-MPC (soft) applies the same conformal field as a penalty and is the strongest method overall: it reaches the goal on every seed in the fewest steps, removes infeasibility by construction, and attains the lowest collision rate of any goal-reaching method, at $74.8$ ms per step on our platform (which is $32\times$ faster than ECP-MPC). Unlike the baselines, its per-step cost does not grow with $N_{\mathrm{obs}}$.

<!-- chunk {"id": "body-0129", "role": "body", "section": "3D Quadrotor Navigation", "weight": 1.0} -->

Reducing the workspace to $N_{\mathrm{obs}}=50$ (Table 5 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) confirms that conservativeness, not the planner, drives these outcomes. With ample free space, FCP-MPC (hard) now threads the field on $88\%$ of seeds and FCP-MPC (soft) again reaches every seed at the lowest collision rate, and CC-MPC also reaches the goal. ACP- and ECP-MPC, however, still time out on every seed, since their per-obstacle and egocentric inflation stays too tight even when space is plentiful.

<!-- chunk {"id": "body-0130", "role": "body", "section": "3D Quadrotor Navigation", "weight": 1.0} -->

We return to this density trend in Section 9 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.").

<!-- chunk {"id": "body-0131", "role": "body", "section": "3D Quadrotor Navigation", "weight": 1.0} -->

Fig. 9 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") illustrates the conformal bound in 3D, and Fig. 10 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") compares closed-loop trajectories across three seeds: FCP-MPC (soft) reaches the goal along the shortest trajectories, whereas ACP-MPC and ECP-MPC time out short of it, and CC-MPC reaches the goal only along substantially longer paths and at a per-step cost that rises with

<!-- chunk {"id": "body-0132", "role": "body", "section": "3D Quadrotor Navigation", "weight": 1.0} -->

Scalability. Figure 11 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") reports the mean per-step control time as $N_{\mathrm{obs}}$ grows from $10$ to $280$. Because FCP-MPC checks safety by querying a *cached conformal field* rather than re-evaluating distances to every obstacle, its per-step cost is largely insensitive to $N_{\text{obs}}$ and remains the lowest of all methods across the range. The baselines instead scale with the obstacle count: CC- and ACP-MPC rise from tens of milliseconds to nearly $100$ ms at $N_{\mathrm{obs}}=280$.

<!-- chunk {"id": "body-0133", "role": "body", "section": "3D Quadrotor Navigation", "weight": 1.0} -->

ECP-MPC, which also performs point-wise conformal reasoning across obstacles and horizon steps, is one to two orders of magnitude slower throughout with a cost that also grows in $N_{\mathrm{obs}}$. This difference is structural: FCP-MPC's per-step safety check is a single cached-field query, $O$ in the obstacle count, whereas ACP- and CC-MPC are $O(N_{\mathrm{obs}})$ and ECP-MPC is $O(N_{\mathrm{obs}}H)$ per step, independent of hardware and implementation.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Field Coverage under Deployment-Time Density Shift", "weight": 1.0} -->

A central claim of our framework is that the online update sustains the field-coverage guarantee when the deployment stream drifts from the offline calibration data. We test this directly with a *density shift*: the functional envelope is conformalized once, offline, at $N_{\mathrm{obs}}=50$, then deployed at higher densities ($N_{\mathrm{obs}}\in\{50,80,120\}$) without re-fitting. A denser min-of-distances field switches its nearest-obstacle identity more often, so the constant-velocity predictor is systematically wrong at more locations and the realized residual field deviates increasingly from the offline calibration.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Field Coverage under Deployment-Time Density Shift", "weight": 1.0} -->

Table 6 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") reports the realized field coverage at the applied step, measured as the $\forall\mathrm{x}\in\bar{\mathcal{X}}$ event of Theorem 2.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Field Coverage under Deployment-Time Density Shift", "weight": 1.0} -->

‣ 7.1 Base Safety Guarantee via Functional Coverage ‣ 7 Safety Analysis and Asymptotic Guarantees ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173."). With a *static* projection slack $\varepsilon_{i}$, the offline envelope fails to cover the full-field event and degrades as density grows ($0.080\!\to\!0.034$): the fixed slack budgets only for the projection residual seen offline, whereas the deviations realized at test time exceed it.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Field Coverage under Deployment-Time Density Shift", "weight": 1.0} -->

Adapting $\varepsilon_{i}$ online by the projection-slack recursion (32 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) (Corollary 1 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) restores the target $1-\alpha=0.9$ coverage and *holds it across all densities*.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Field Coverage under Deployment-Time Density Shift", "weight": 1.0} -->

Notably, collisions remain small across all densities and both settings, including the static configuration whose coverage collapses. There, receding-horizon replanning corrects each transient envelope violation at the next observation, before it becomes a collision. Safety and field coverage thus come apart in this regime: coverage is sufficient for safety but not, here, necessary. We take up what the coverage certificate buys, once the feedback structure already absorbs most of the coverage loss, in Section 9 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.").

<!-- chunk {"id": "body-0139", "role": "body", "section": "Discussion", "weight": 1.5} -->

Enforcing the safety bound in 2D. The 2D benchmarks isolate how the conformal lower bound should be *used* once it has been constructed. The hard variant enforces the bound as a feasibility filter and thus carries the closed-loop guarantee. As the worst-case envelope compounds over the horizon, however, it can become overconservative, leaving a non-zero infeasible rate and higher collisions in the harder scenes. The soft variant resolves this by treating the bound as a penalty rather than a hard constraint: it yields the shortest paths, trading a small, density-independent collision cost for that progress (Table 1 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")).

<!-- chunk {"id": "body-0140", "role": "body", "section": "Discussion", "weight": 1.5} -->

The optional online adaptation of (30 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")) is a low-cost refinement whose effect on these in-distribution benchmarks is marginal and scene-dependent (Table 2 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")): the offline-conformalized envelope does the heavy lifting when deployment matches calibration.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Discussion", "weight": 1.5} -->

Its value appears instead under distribution shift, which we examine separately in Section 8.6 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173."). Both variants reuse the offline conformal prediction, so any online cost is only a few milliseconds, far below the tens required by ECP-MPC's explicit online uncertainty reasoning. These pedestrian experiments thus exercise the fieldwise conformal prediction where free space is scarce, complementing the open 3D study discussed next.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Discussion", "weight": 1.5} -->

Separating conformal prediction from real-time planning in 3D. The two ways the baselines fail, conservativeness and computation cost (Section 8.5 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")), share the same cause: they quantify uncertainty *online*, per obstacle or per robot state. This is both costly at runtime and forces a locally tight margin around every object. FCP instead estimates the conformal *field* once offline. At runtime, a single cached-field query suffices, and the result is far less conservative because the bound is reasoned globally over space rather than inflated object by object. This is why FCP is at once the cheapest method and the only conformal construction whose hard filter clears the field when free space is adequate.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Discussion", "weight": 1.5} -->

Certified hard filter vs. practical soft deployment. The same offline field can be deployed in two ways (Section 6.1 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")). As a *hard* filter it carries the formal coverage guarantee of Theorems 2.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Discussion", "weight": 1.5} -->

‣ 7.1 Base Safety Guarantee via Functional Coverage ‣ 7 Safety Analysis and Asymptotic Guarantees ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")--3.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Discussion", "weight": 1.5} -->

‣ 7.2 Robust Guarantee Under Online Adaptation ‣ 7 Safety Analysis and Asymptotic Guarantees ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173."), at the price of conservativeness that grows with density: the infeasible rate rises from $0.353$ at $N_{\mathrm{obs}}=50$, where the filter still reaches the goal on $88\%$ of seeds at the lowest per-step cost of any method, to $0.833$ at $N_{\mathrm{obs}}=280$, where the worst-case envelope leaves so few feasible candidates that the planner stalls and times out.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Discussion", "weight": 1.5} -->

As a *soft* penalty the field carries a slightly weaker but still formal guarantee (Theorem 4. ‣ 7.3 Safety of the Soft Deployment ‣ 7 Safety Analysis and Asymptotic Guarantees ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.")): on feasible steps it is safe up to a slack that vanishes as $w\to\infty$, and elsewhere it degrades gracefully to the least-violating plan.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Discussion", "weight": 1.5} -->

Which branch of the soft guarantee applies depends on the density. The *exact* branch presumes a non-empty hard feasible set at every step, and this premise is itself empirically violated at $N_{\mathrm{obs}}=280$ (hard infeasible rate $0.833$). The assurance we actually rely on there is therefore the *degradation* branch of Theorem 4.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Discussion", "weight": 1.5} -->

‣ 7.3 Safety of the Soft Deployment ‣ 7 Safety Analysis and Asymptotic Guarantees ‣ From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion PlanningThis work was supported in part by the Information and Communications Technology Planning and Evaluation (IITP) grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") together with the empirical per-step coverage of Section 8.6 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173."), while the clean $1-\alpha$ statement governs the moderate-density regime in which the hard filter remains feasible.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Discussion", "weight": 1.5} -->

Empirically, the soft deployment removes infeasibility entirely and attains the lowest collision rate among goal-reaching methods ($0.028$ at $N_{\text{obs}}=280$, within $\alpha=0.1$), reaching the goal on every seed at both densities. Notably, FCP-MPC stays within the target miscoverage level *while actively traversing* the dense field, whereas ACP's low collision count reflects a controller that never threads it, and ECP is both slow and over-conservative. We attribute this reliable goal-reaching to the spatial coherence of the field-level bound, which exposes globally safe corridors rather than forcing locally conservative, point-wise reasoning.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Discussion", "weight": 1.5} -->

On the value of coverage in closed-loop scenarios. Section 8.6 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") shows that closed-loop replanning absorbs *most* of a coverage loss: even when the static envelope's field coverage collapses, the realized collision rate stays low because receding-horizon correction catches transient violations at the next observation. It does not, however, catch *all* of them, as the static configuration's small but nonzero collisions in Table 6 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") indicate.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Discussion", "weight": 1.5} -->

It is therefore worth stating precisely what the field-coverage guarantee and the AFCP update provide that feedback alone does not. First, the coverage guarantee is *planner-agnostic*: every feasible candidate at a step is safe, whereas a low closed-loop collision rate only certifies that the executed trajectories happened to avoid contact, with no assurance under a different sampler, seed, or planner. Second, it is *pre-hoc*: it prevents violations from arising in the first place, whereas closed-loop correction is reactive and presumes that the next observation arrives, and a feasible escape exists, before a transient violation becomes a collision. Our fast, open, and slow-obstacle settings largely satisfy these recovery assumptions, which is why feedback suffices here; under high travel speed, tight corridors, or sensing latency they may fail, and the pre-hoc guarantee is what remains.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Discussion", "weight": 1.5} -->

The residual collisions already visible in Table 6 grants funded by MSIT No. 2022-0-00124, No. 2022-0-00480 and No. RS-2021-II211343, Artificial Intelligence Graduate School Program (Seoul National University), and the National Research Foundation of Korea (NRF) grant funded by MSIT No. RS-2026-25477173.") are a mild instance of this gap; a dedicated study of the non-recoverable regime is left to future work.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Discussion", "weight": 1.5} -->

This fixes the role of each deployment. The hard filter is the *exactly* certified variant, appropriate when free space is adequate; the soft penalty is the deployment we recommend in the densest scenes, where strict enforcement is too conservative to make progress; and the online update may be engaged where the formal guarantee is wanted, or disengaged where closed-loop correction suffices and feasibility is at a premium. The hard/soft and AFCP-on/off choices thus fall on one axis: the framework selects, by deployment context, how much of its safety to take as a proactive certificate versus closed-loop correction, rather than committing to one everywhere.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented a functional conformal prediction framework that conformalizes a high-confidence lower bound of the predicted distance field and enforces it as a tightened safety constraint within a sampling-based model predictive controller, FCP-MPC. By conformalizing uncertainty at the level of the spatial *field* rather than at individual states or trajectories, the method reasons about safety globally: the resulting certificate holds for any trajectory satisfying it, independent of the control sampler. Because the residual field is low-rank and approximately time-invariant, its offline--online decomposition keeps per-step computation low, with a GMM-based envelope fitted offline and only a single scalar per horizon index refined online by a lightweight adaptive update. We established asymptotic closed-loop safety both under exchangeability and, through the online adaptation, under distribution shift. Across the ETH--UCY pedestrian benchmarks and a dense 3D quadrotor task with up to $280$ moving obstacles, FCP-MPC attained a favorable balance of safety, feasibility, and efficiency. Its per-step cost stayed largely insensitive to obstacle count, scaling far more gracefully than online uncertainty-reasoning baselines.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Limitations and future work. Because the conformalized envelope bounds the worst case, the hard-constrained variant remains conservative and can still report a non-zero infeasible rate in the densest 2D scenes; the soft and online-adapted variants mitigate, but do not eliminate, this trade-off. Our guarantees further assume a *fixed* functional basis. Relaxing these assumptions and learning the basis online, folding perception and state-estimation error into the same conformal pipeline, and extending the method to richer robot and obstacle dynamics are all promising directions.
