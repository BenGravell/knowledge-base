<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Safety Evaluation of Motion Plans Using Trajectory Predictors as Forward Reachable Set Estimators

Topics include Vehicles, Safety, Bayesian methods, Datasets, Out-of-distribution generalization, FRS, OOD.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The advent of end-to-end autonomy stacks - often lacking interpretable intermediate modules - has placed an increased burden on ensuring that the final output, i.e., the motion plan, is safe in order to validate the safety of the entire stack. This requires a safety monitor that is both complete (able to detect all unsafe plans) and sound (does not flag safe plans). In this work, we propose a principled safety monitor that leverages modern multi-modal trajectory predictors to approximate forward reachable sets (FRS) of surrounding agents. By formulating a convex program, we efficiently extract these data-driven FRSs directly from the predicted state distributions, conditioned on scene context such as lane topology and agent history. To ensure completeness, we leverage conformal prediction to calibrate the FRS and guarantee coverage of ground-truth trajectories with high probability. To preserve soundness in out-of-distribution (OOD) scenarios or under predictor failure, we introduce a Bayesian filter that dynamically adjusts the FRS conservativeness based on the predictor's observed performance.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We then assess the safety of the ego vehicle's motion plan by checking for intersections with these calibrated FRSs, ensuring the plan remains collision-free under plausible future behaviors of others. Extensive experiments on the nuScenes dataset show our approach significantly improves soundness while maintaining completeness, offering a practical and reliable safety monitor for learned autonomy stacks.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Classical planning stacks come in various shapes and forms, but, importantly, they share the characteristic of optimizing an interpretable cost function which allows reasoning about the plan's safety during synthesis. With the ever-increasing adoption of learning-based planners and end-to-end robot stacks, safe-by-construction planning has become extremely challenging, if not outright impossible. Therefore, safety monitors for motion plans have grown in prominence for ensuring that these often uninterpretable learning-based plans are safe. Like any effective monitor, a safety monitor should satisfy two key properties: completeness (it must flag all unsafe plans) and soundness (it must not flag safe ones). Our objective in this paper is to develop a method that can improve on the soundness of reachability-based safety monitors without compromising on completeness.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We achieve this by reinterpreting trajectory predictors - typically generative models trained to forecast future agent behavior conditioned on histories and scene context (e.g., lane graphs, traffic signals) - as data-driven forward reachable set (FRS) estimators. These predictors, often instantiated as Gaussian Mixture Models (GMMs), implicitly learn a stochastic model of agent dynamics from logged driving data. Our key insight is that we can extract a probabilistic FRS by solving an optimization problem that identifies the smallest-volume set that captures a desired amount of probability mass under the learned distribution.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Leveraging the fact that many modern trajectory predictors output GMMs on the future states, we formulate a convex relaxation of this problem that allows us to efficiently compute tight reachable sets that are significantly less conservative than traditional worst-case reachability approaches. However, these learned distributions are subject to modeling error and may fail to capture the true dynamics, especially under distribution shift.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

To combat learning errors, we use conformal prediction (CP) to calibrate the FRS. Rather than inflating the predicted sets indiscriminately, CP allows us to scale the covariance of each GMM component just enough to ensure that the reachable set covers the ground-truth trajectory with a user-specified error rate. Our overall algorithm to extract the FRS is called FORCE-OPT, which stands for FOrward Reachable sets from Conformal Estimation and convex OPTimization.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Although FORCE-OPT comes with a probabilistic guarantee on covering the ground truth when operating within the calibration distribution, it may still degrade in the presence of distribution shift. To handle this, we introduce a Bayesian filtering mechanism that monitors the consistency between predicted and observed agent behavior, adjusting the FRS conservativeness on the fly based on our confidence in the trajectory predictor.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

This main contributions of the paper are: (i) We provide a rigorous formulation of the problem of estimating FRS from trajectory predictors. (ii) We introduce FORCE-OPT, an efficient algorithm that combines convex optimization and conformal prediction to compute calibrated, data-driven FRS from GMM-based predictors. (iii) We incorporate a belief-based Bayesian filtering mechanism that adapts the reachable set dynamically to account for predictor reliability under distribution shift. (iv) Through testing on nuScenes, real-world driving dataset, we demonstrate that FORCE-OPT achieves the best balance of false positive and false negative rates, outperforming both conservative baselines and uncalibrated learned methods.

<!-- chunk {"id": "body-0010", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

Control-Theoretic Safety Evaluators. Classical approaches for safety evaluation of motion plans have relied on control-theoretic tools such as formal verification, which provide mathematical guarantees that a system satisfies a predefined set of safety specifications. While rigorous, these methods often fall short when applied to modern robotic systems that encounter large uncertainties and operate in high-dimensional, stochastic environments. To handle this imminent uncertainty, reachability-based techniques---including those based on zonotopes, Hamilton-Jacobi formulations, or sums-of-squares ---aim to characterize the set of all future states a system can reach under bounded disturbances. However, their worst-case assumptions often lead to overly conservative safety bounds that limit practical usability. Furthermore, these methods typically struggle to incorporate rich sensory inputs (e.g., images, LiDAR) and contextual cues that modern autonomous systems depend. High-dimensional observations are often abstracted through models or simplifying assumptions are made, reducing the granularity of the safety assessment. A common alternative to handling the difficult-to-model uncertainties in the real world is through data-driven methods.

<!-- chunk {"id": "body-0011", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

One such approach, tailored towards multi-agent settings, is to leverage learning-based trajectory predictors, as we will discuss next.

<!-- chunk {"id": "body-0012", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

Trajectory Prediction-based Safety Evaluators. Motivated by the limitations of worst-case control-theoretic safety evaluators, there has been growing interest in safety evaluation frameworks built on top of learning-based trajectory predictors. Although trajectory predictors were devised to aid with planning, they have found widespread use in other applications, such as failure monitoring, mining interactive scenarios, and assessing planner safety which is of primary interest to us in this paper. Trajectory predictors are often used to identify reachable zones for other agents that the motion plan should stay out of, violation of which is considered to trigger a safety failure; see for a survey. Methods in this category include those that use trajectory predictors to guide controllability bounds on other agents to be used in a classical reachability formulation and those that directly extract a reachable zone for contender agents from the predictor. In the latter category, approaches have explored fitting zonotopes to prediction outputs for estimating reachable sets, leveraged conformal prediction, and solved a probabilistic optimization on the output distribution of the predictor.

<!-- chunk {"id": "body-0013", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

However, many of these approaches require sampling which is computationally expensive, lack multi-modality, or lack calibration of the predictors resulting in learning-errors affecting the quality of the FRS. The approach presented in this paper is computationally efficient, accounts for multi-modality in predictions, calibrates the predictions to mitigate the impact of learning errors, and performs a belief-based FRS adaptation to impart some degree of OOD robustness.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Equivalence of Deterministic and Stochastic Notions of FRS", "weight": 1.0} -->

We now present a rigorous mathematical framework to bridge the probabilistic and deterministic definitions of FRS. While the former is characteristic of contemporary trajectory forecasting literature, the latter is fundamental to control-theoretic safety analysis.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Equivalence of Deterministic and Stochastic Notions of FRS", "weight": 1.0} -->

In practice, however, the precise control sets $\mathcal{U}_{i}$ and disturbance sets $\mathcal{W}_{i}$ are unknown and influenced by hard-to-model aspects such as driver intent, road geometry, and local context. Classical reachability methods often adopt worst-case assumptions over these sets, resulting in overly conservative FRSs. Such assumptions are unnecessarily pessimistic - for instance, it is unreasonable to expect that a stopped vehicle at a red light will suddenly accelerate through the intersection while the traffic light is still red. A more realistic alternative is to infer the agent's behavior from data. In what follows, we introduce a probabilistic formulation of the FRS that facilitates using data-driven trajectory predictors to estimate likely future states of an agent, thereby, reducing the conservatism of the FRS.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Equivalence of Deterministic and Stochastic Notions of FRS", "weight": 1.0} -->

We now reformulate the FRS using a probabilistic lens, as inspired by prior work. As we highlight later in this paper, this probabilistic viewpoint is readily compatible with modern multi-modal trajectory predictors. Let $vol$ represent the volume (Lebesgue measure) of a measurable set $\omega \in \Omega$, where $\Omega$ is the collection of all measurable subsets of $\mathcal{X}$. Let $\mu_{t}:{\Omega\rightarrow{\lbrack 0,1\rbrack}}$ represent a probability measure describing the distribution over the agent's state at time $t$. This measure arises as the push-forward of absolutely continuous probability distributions over the sequences of control and disturbance inputs, with support on $\mathcal{U}_{i}$ and $\mathcal{W}_{i}$, mapped through the composed dynamics.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Equivalence of Deterministic and Stochastic Notions of FRS", "weight": 1.0} -->

Intuitively, returns the smallest (i.e., minimal-volume) set that captures all the future states of the agent under the distribution $\mu_{t}$. Remarkably, this probabilistic formulation is equivalent to the classical deterministic definition in almost everywhere (i.e., excluding a set of measure zero) as formalized in the following theorem.

<!-- chunk {"id": "body-0018", "role": "body", "section": "FORCE-OPT", "weight": 1.0} -->

We now present FORCE-OPT, our algorithm for estimating FRS from trajectory predictors and calibrating them using conformal prediction. FORCE-OPT combines learned generative models with convex optimization to efficiently compute calibrated FRSs, and uses Bayesian filtering to hedge against out-of-distribution (OOD) deployment failures.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Trajectory Predictors", "weight": 1.0} -->

Without loss of generality, let the current time be $0$. Denote the state of all agents in the scene by $\xi \in \mathcal{X}^{n_{agents}}$, and their historical trajectories over a horizon $H$ by $\xi_{{- H}:0} \in \mathcal{X}^{Hn_{agents}}$. Let $m \in \mathcal{M}$ represent map and other contextual scene information. A traffic scene is then denoted by $s:={(\xi_{{- H}:0},m)} \in \mathcal{X}^{H} \times \mathcal{M} =:\mathcal{S}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-B Extracting FRS from Trajectory Predictors", "weight": 1.0} -->

We treat ${\hat{\mu}}_{t}$ as a learned approximation of the push-forward distribution $\mu_{t}$. However, given that GMMs have an unbounded support, these measures make it infeasible to find a bounded set $\omega$ satisfying ${{\hat{\mu}}_{t}{(\omega)}} = 1$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B Extracting FRS from Trajectory Predictors", "weight": 1.0} -->

Ideally, we would choose a $\tau$ that is very close to 1. However, at this level of generality, this problem is very challenging to solve. Leveraging the fact that the distribution over each timestep is a GMM, we solve a tractable proxy for this problem by restricting the search to unions of sub-level sets of the GMM modes. For a given mode ${\hat{\mu}}_{t,i}$, define the Mahalanobis energy function ${V_{i}{(x)}}:={{({x - {\overline{x}}_{i}})}^{T}\Sigma_{i}^{- 1}{({x - {\overline{x}}_{i}})}}$, and its sublevel set ${E_{i}{(c_{i})}}:={\{ x:{{V_{i}{(x)}} \leq c_{i}}\}}$ for $c_{i} \geq 0$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B Extracting FRS from Trajectory Predictors", "weight": 1.0} -->

The resulting FRS is $E^{\ast} = {\bigcup_{i = 1}^{K}{E_{i}{(c_{i}^{\ast})}}}$. Although $E^{\ast}$ is not necessarily the smallest such set, it is a feasible solution to, and tight in practice. When $\mathcal{X} \subseteq {\mathbb{R}}^{2}$, it takes the form of a convex optimization, as detailed in the following theorem.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-C Conformalizing FRS from Trajectory Predictors", "weight": 1.0} -->

The FRS obtained from ) assumes the predictor's distribution ${\hat{\mu}}_{t}$ closely matches the true transition dynamics. In reality, due to modeling choices and limited training data, ${\hat{\mu}}_{t}$ may fail to cover the true ground-truth distribution. We address this by applying split conformal prediction to calibrate the reachable set to achieve high-probability coverage of the ground truth future.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-C Conformalizing FRS from Trajectory Predictors", "weight": 1.0} -->

We calibrate our FRS by scaling the covariance of the GMM modes.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-C Conformalizing FRS from Trajectory Predictors", "weight": 1.0} -->

where $s$ is the scene information as defined in Section IV-A and $E^{\ast}{({\{\Sigma_{i}\}}_{i = 1}^{K})}$ be the FRS obtained by solving ) for GMM covariances ${\{\Sigma_{i}\}}_{i = 1}^{K}$. Thanks to Corollary ‣ IV-B Extracting FRS from Trajectory Predictors ‣ IV FORCE-OPT ‣ Safety Evaluation of Motion Plans Using Trajectory Predictors as Forward Reachable Set Estimators"), we only need to solve ) once to obtain $c_{i}^{\ast}$, after which we can compute $\psi{(s,x)}$ analytically: ${\psi{(s,x)}} = {\min{\{{\left. {{V_{i}{(x)}}/c_{i}^{\ast}} \middle| i \right.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-C Conformalizing FRS from Trajectory Predictors", "weight": 1.0} -->

= 1},\cdots,K\}}}$ where $V_{i}$ is as defined in Section IV-B for $\Sigma_{i}$ that are outputted by the trajectory predictor.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-D Hedging Against OOD Failures via Bayesian Filtering", "weight": 1.0} -->

The conformalization process in Section IV-C allows FORCE-OPT to provide statistical guarantees on the coverage of predicted reachable sets. However, these guarantees hold only under the assumption that test-time inputs are drawn independently and identically (IID) from the same distribution as the calibration data. In practice---especially in autonomous driving---this assumption is often violated, and distribution shift can cause these guarantees to break down.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-D Hedging Against OOD Failures via Bayesian Filtering", "weight": 1.0} -->

To address this challenge, we augment FORCE-OPT with a Bayesian filtering mechanism that dynamically adjusts uncertainty in the reachable set when the trajectory predictor appears unreliable. Specifically, we introduce a model confidence parameter $\beta \in {\lbrack\beta_{\text{low}},\beta_{\text{high}}\rbrack}$ that reflects our trust in the predictor. This parameter scales the covariance of the GMMs used in the FRS adaptively, effectively dilating the predicted reachable sets to reflect greater uncertainty..

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-D Hedging Against OOD Failures via Bayesian Filtering", "weight": 1.0} -->

To track this confidence online, we adopt the Bayesian update scheme proposed. At each timestep $t$, we maintain a belief distribution over $\beta$, denoted by $\text{bel}^{t}{(\beta)}$. The belief is initialized uniformly: ${bel^{0}{(\beta_{low})}} = {bel^{0}{(\beta_{high})}} = 0.5$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-D Hedging Against OOD Failures via Bayesian Filtering", "weight": 1.0} -->

where $\overset{\sim}{\beta} \in {\{\beta_{\text{low}},\beta_{\text{high}}\}}$. Here $\varphi{(x,{GMM{( \cdot )}})}$ denotes the likelihood of state $x$ under the given GMM. Note that the GMM covariances are already scaled by the conformal calibration factor $\eta$; the inverse $\beta$ scaling further adjusts the uncertainty based on current trust in the predictor. Finally, we compute the effective model confidence as the expected value under the belief: $\hat{\beta} = {{\mathbb{E}}{\lbrack\beta\rbrack}}$, and use this $\hat{\beta}$ to further scale the covariances of the distribution to adjust the final FRS returned by FORCE-OPT.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-D Hedging Against OOD Failures via Bayesian Filtering", "weight": 1.0} -->

While conformal prediction provides statistical guarantees on coverage, these guarantees hold only in the average case. It does not account for rare but high-impact failures that may lie in the tails of the distribution. To address such worst-case scenarios, we incorporate techniques from Hamilton-Jacobi (HJ) reachability analysis. Specifically, when the online model confidence $\beta$ drops below a critical threshold, it indicates that the predictor may be operating outside the distribution represented by the calibration dataset. These are precisely the conditions under which FORCE-OPT becomes vulnerable to long-tailed failure modes.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-D Hedging Against OOD Failures via Bayesian Filtering", "weight": 1.0} -->

To mitigate this risk, we employ two fallback mechanisms based on reachability theory: (i) a Parameterized FRS that adapts to observed uncertainty levels, and (ii) a Worst-Case FRS that assumes bounded adversarial disturbances. These fallback strategies are activated when $\beta$ falls below the specified threshold. We explore the behavior and trade-offs of these approaches in detail in the results section, particularly in the context of different predictor types.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-D Hedging Against OOD Failures via Bayesian Filtering", "weight": 1.0} -->

The belief update mechanism and switching strategy allow FORCE-OPT to maintain tight, calibrated bounds in-distribution, while conservatively hedging against uncertainty in out-of-distribution or low-confidence scenarios.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

We now present an empirical evaluation of FORCEOPT to assess its effectiveness in safety-critical motion planning. Our experiments are designed to address the following key research questions: (Q1) How effective is FORCE-OPT at balancing completeness and soundness of safety evaluation for autonomous driving? (Q2) Do the belief-based extensions of FORCE-OPT result in more robust monitoring in out-of-distribution operation? (Q3) How effectively can FORCE-OPT and its extensions leverage multimodality of trajectory prediction? (Q4) Does FORCE-OPT offer a computational advantage that might enable online deployment?

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-A Datasets", "weight": 1.0} -->

To answer the above questions, we evaluate FORCE-OPT's performance on nuScenes, a large-scale autonomous driving dataset. The nuScenes dataset includes approximately 15 hours of expert-labeled driving data in Boston and Singapore. We train the Autobots predictor on the training split of Singapore and then test it on the test splits of both cities. This setup allows us to test the performance of our approach on in distribution (ID) where the model is trained and tested on the same city as well as out-of-distribution (OOD) where the model is tested on a city different from the one it is trained.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-B Synthetic Unsafe Data Generation", "weight": 1.0} -->

Although nuScenes provides diverse testing conditions, all the driving data available in the dataset is inherently safe, which makes it challenging to assess the monitor's ability to detect potential safety violations. To remedy this, we synthetically generate unsafe scenarios by modifying scenes within the nuScenes dataset. Specifically, we identify potential intersections between the trajectories of the ego vehicle and a surrounding agent, defining the point of closest approach $p_{c}$ as the collision point. Let the ego and the contender arrive at $p_{c}$ at times $t_{e}$ and $t_{o}$, respectively. We use a bicycle dynamics model for the ego vehicle and optimize its trajectory using Sequential Least Squares Programming (SLSQP) to force it to reach $p_{c}$ at $t_{o}$, while obeying initial conditions and physical constraints. The resulting trajectory of the ego vehicle, along with the original trajectory of the contender, constitutes a synthesized unsafe scenario. This yields plausible but unsafe plans, which serve as ground truth for evaluating false negative rates.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-C Metrics", "weight": 1.0} -->

The primary objective of this paper is to assess the safety of motion plans. To that end, we focus on two broad categories of metrics: completeness and soundness. These metrics evaluate on a per-frame basis how effectively and reliably a safety assessment algorithm captures true safety violations while minimizing over-conservatism.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-C Metrics", "weight": 1.0} -->

Coverage (Cov): The fraction of ground-truth future trajectories that fall within the predicted reachable set. High coverage indicates that the predicted FRS captures the actual future behavior well.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-C Metrics", "weight": 1.0} -->

False Negative Rate (FNR): The proportion of true collision cases (from synthesized unsafe data) that are not flagged by the monitor.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-C Metrics", "weight": 1.0} -->

Soundness is evaluated using the False Positive Rate (FPR): The fraction of safe scenarios that are incorrectly flagged as unsafe. A low FPR indicates soundness, avoiding unnecessary interventions.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-C Metrics", "weight": 1.0} -->

Balance between Completeness and Soundness is evaluated using the *Balanced Error Rate (BER)*: Arithmetic mean of FPR and FNR effectively capturing the tradeoff between them.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-C Metrics", "weight": 1.0} -->

Uncalibrated Trajectory Predictor
Calibrated Trajectory Predictor with Conformal Prediction

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-D Baselines and Variants", "weight": 1.0} -->

Uncalibrated Trajectory Predictor: The methods that fall under this class directly use the trajectory predictor without calibrating them. 99% CI: The original predictor where the sets occupy 99% of GMM probability mass. $E = {\bigcup_{i = 1}^{K}{E_{i}{(C)}}}$ where C = value at 99th Percentile of a $\chi^{2}$ distribution. Parametric Worst Case-FRS (pWC-FRS): We obtain the control bounds as the $3\sigma$ (or 99% confidence interval) support of the Gaussian control distribution for each mode predicted by a trajectory predictor and then estimate a worst-case FRS for each mode and take the union of the sets. (the parameter is the velocity and the control bound of he agent) Nakamura et al.: Adapts FRS via belief tracking of a trajectory predictor's performance. In this case the control bounds enclose the 3% probaility mass around the mean of the normal distribution predicted by the trajectory predictor.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-D Baselines and Variants", "weight": 1.0} -->

Calibrated Trajectory Predictor: The methods within this class leverage trajectory predictors that are calibrated using CP. We use a dataset with a cardinality of 35220 for calibration and set the desired coverage probability in CP to 0.95. Lindemann et al.: Provides coverage guarantees via conformalization between the highest likelihood trajectory and the ground truth. FORCE-OPT (Ours): Solves the convex optimization from Sec. IV-B using GMMs from learned predictors, along with the calibration schemes in Sec.IV-C. FORCE-OPT + belief: Additionally adjusts the GMM covariances of FORCE-OPT using Bayesian filtering approach in Sec. IV-D. For this and all the subsequent methods that use belief-based adaptation, we set $\beta_{low} = 0.3$ and $\beta_{high} = 1$. FORCE-OPT + pWC-FRS: A hybrid approach that switches from FORCE-OPT to Parametric WC-FRS when $\beta < 0.75$ indicating a drop in the predictor's performance.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-D Baselines and Variants", "weight": 1.0} -->

FORCE-OPT + WC-FRS: This approach switches from FORCE-OPT to worst-case FRS when $\beta < 0.75$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-D Baselines and Variants", "weight": 1.0} -->

Data-Free: This category contains only one baseline metric Worst Case FRS (WC-FRS) which computes worst-case FRS assuming 4D Dubins vehicle dynamics with bounded control inputs.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-E Results and Discussion", "weight": 1.0} -->

The results for in-distribution evaluation of all approaches discussed in Section V-D are summarized in Table I, while those for OOD are summarized in Table II ‣ V-E Results and Discussion ‣ V Experimental Results ‣ Safety Evaluation of Motion Plans Using Trajectory Predictors as Forward Reachable Set Estimators").

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-E1 Balance between Completeness and Soundness (Q1)", "weight": 1.0} -->

From Table I we observe that FORCE-OPT achieves the lowest BER, indicating the best balance between FPR and FNR. The metrics that use CP-based calibration on the trajectory predictor have a significantly lower FNR at the expense of a slightly higher FPR than the ones that do not calibrate the predictor, generally indicating that the trajectory predictor without calibration tends to be over-optimistic in safety assessment missing out safety critical events, highlighting the importance of calibrating the trajectory predictor---one exception to this observation is the parametric FRS that counters the uncalibrated predictor's over-optimism by plugging the predicted control bounds to solve for the worst-case FRS. We also note that FORCE-OPT and its belief-based extensions, in comparison to, have a lower FPR while maintaining a similar FNR and higher coverage rates.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-E1 Balance between Completeness and Soundness (Q1)", "weight": 1.0} -->

These additional gains are the outcome of the Theorem ‣ III Equivalence of Deterministic and Stochastic Notions of FRS ‣ Safety Evaluation of Motion Plans Using Trajectory Predictors as Forward Reachable Set Estimators")-inspired convex optimization ) that more precisely models the forward reachable space while leveraging multi-modality; this is discussed in greater detail in Section V-E3 ‣ V-E Results and Discussion ‣ V Experimental Results ‣ Safety Evaluation of Motion Plans Using Trajectory Predictors as Forward Reachable Set Estimators"). FORCE-OPT has lower FPR and slightly worse FNR than its belief-based variants, which is in alignment with our expectations as the belief-based approaches introduce greater conservatism in the event when the predictor's performance deteriorates.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-E1 Balance between Completeness and Soundness (Q1)", "weight": 1.0} -->

Uncalibrated Trajectory Predictor
Calibrated Trajectory Predictor with Conformal Prediction

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-E2 Out-of-distribution Robustness (Q2)", "weight": 1.0} -->

The belief-based adaptation mechanism enables smooth adjustment to uncertain contexts without excessive conservatism, as evidenced by the fact that the performance of the belief-based variants of FORCE-OPT remains similar between Tables I and II ‣ V-E Results and Discussion ‣ V Experimental Results ‣ Safety Evaluation of Motion Plans Using Trajectory Predictors as Forward Reachable Set Estimators") and the best performing metric according to BER in Table II ‣ V-E Results and Discussion ‣ V Experimental Results ‣ Safety Evaluation of Motion Plans Using Trajectory Predictors as Forward Reachable Set Estimators") is FORCE-OPT + pWC-FRS.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-E2 Out-of-distribution Robustness (Q2)", "weight": 1.0} -->

Comparing the results in Table I (ID) and Table II ‣ V-E Results and Discussion ‣ V Experimental Results ‣ Safety Evaluation of Motion Plans Using Trajectory Predictors as Forward Reachable Set Estimators") (OOD), we also observe that the metrics that use an uncalibrated trajectory predictor suffer a drop in performance, especially with the FNR which jumps from 33.33% and 36.36% (ID) to 51.85% and 55.56% (OOD) for 99% CI and, respectively---as before, parametric FRS is an exception to this for the same reason mentioned in Section V-E1 ‣ V-E Results and Discussion ‣ V Experimental Results ‣ Safety Evaluation of Motion Plans Using Trajectory Predictors as Forward Reachable Set Estimators"). On the other hand, the approaches that use the calibrated trajectory predictor exhibit stronger OOD robustness; albeit, there is a modest increase in the FNR for all these approaches. Unsurprisingly, the performance of Worst-Case FRS is unaffected by the distribution shift.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-E3 Impact of Multi-modality (Q3)", "weight": 1.0} -->

One of the key strengths of FORCE-OPT is its ability to systematically integrate probabilities from multiple prediction modes. To study the impact of multi-modality, we ablate the performance of the metrics in Section V-D that can handle multimodality, i.e., 99% CI, parametric FRS, FORCE-OPT and its belief-based variants, on the Singapore dataset against the number of GMM modes. As the number of modes increase from one to five, we observe that the BER drops for all methods other than pWC-FRS Fig. 2(a) ‣ V-E Results and Discussion ‣ V Experimental Results ‣ Safety Evaluation of Motion Plans Using Trajectory Predictors as Forward Reachable Set Estimators").

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-E3 Impact of Multi-modality (Q3)", "weight": 1.0} -->

The drop in BER in different methods is fueled by different reasons: for 99% CI, the BER improves because the FNR improves with more modes Fig. 2(c) ‣ V-E Results and Discussion ‣ V Experimental Results ‣ Safety Evaluation of Motion Plans Using Trajectory Predictors as Forward Reachable Set Estimators"), while for FORCE-OPT and its variants the BER improvement arises from an improvement in the FPR Fig. 2(b) ‣ V-E Results and Discussion ‣ V Experimental Results ‣ Safety Evaluation of Motion Plans Using Trajectory Predictors as Forward Reachable Set Estimators"). At first look, it is indeed surprising that more modes result in a lower FPR for FORCE-OPT; however, this counter-intuitive outcome is the result of the fact that greater multi-modality requires smaller set inflations via CP, as evidenced by the fact that the $\alpha$'s decrease as the number of modes increase, as shown in Table III ‣ V-E Results and Discussion ‣ V Experimental Results ‣ Safety Evaluation of Motion Plans Using Trajectory Predictors as Forward Reachable Set Estimators").

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-E3 Impact of Multi-modality (Q3)", "weight": 1.0} -->

If a mode other than the most-likely one is nearer to the ground truth in the calibration set, then the amount of set inflation needed to cover that ground-truth position would have to be less than the inflation needed for the most-likely mode that is further away. Overall, our ablations suggest that greater multi-modality promotes better safety assessment by allowing us to reason about multiple plausible future outcomes which could be closer to the ground truth behavior than whatever the model deems to be the most likely.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-E4 Compuational Efficiency (Q4)", "weight": 1.0} -->

In Table IV ‣ V-E Results and Discussion ‣ V Experimental Results ‣ Safety Evaluation of Motion Plans Using Trajectory Predictors as Forward Reachable Set Estimators"), we show the computation time for all the methods presented in Section V-D along with their performance on BER in Tables I and II ‣ V-E Results and Discussion ‣ V Experimental Results ‣ Safety Evaluation of Motion Plans Using Trajectory Predictors as Forward Reachable Set Estimators"). FORCE-OPT demonstrates fast runtimes while achieving strong BER results in both ID and OOD settings, outperforming faster baselines such as 99% CI and. Notably, adding belief tracking adds negligible overhead---FORCE-OPT + belief is only 0.001 seconds slower than FORCE-OPT alone. With the exception of FORCE-OPT + pWC-FRS, all other variants of FORCE-OPT are faster than 0.1 seconds, suggesting that these algorithms are well-suited for deployment in real-time, safety-critical applications.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

This paper introduced FORCE-OPT, a principled framework for evaluating the safety of motion plans using trajectory predictors as estimators of forward reachable sets. By combining convex optimization, conformal prediction, and Bayesian filtering, our method generates calibrated uncertainty sets that balance completeness (low false negatives) with soundness (low false positives). Empirical results on nuScenes demonstrate that FORCE-OPT significantly outperforms both conservative model-based and raw learning-based baselines, while gracefully handling out-of-distribution scenarios. We believe FORCE-OPT offers a promising building block for runtime safety monitoring in learned autonomy stacks.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

4This work opens up several directions for exploration: (i) While the trajectory predictor conditions on scene context, FORCE-OPT itself operates independently for each agent when computing FRS. Joint multi-agent reachability, especially in dense traffic scenarios with interdependent behaviors, remains an open direction. (ii) Trajectory predictors are trained to distributionally mimic the observed data, not to facilitate the extraction of FRS. Training a neural FRS generator that directly outputs sets is another exciting open direction.
