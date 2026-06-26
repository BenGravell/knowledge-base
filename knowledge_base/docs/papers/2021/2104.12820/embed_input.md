<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Universal Off-Policy Evaluation

Topics include Partial observability.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

When faced with sequential decision-making problems, it is often useful to be able to predict what would happen if decisions were made using a new policy. Those predictions must often be based on data collected under some previously used decision-making rule. Many previous methods enable such off-policy (or counterfactual) estimation of the expected value of a performance measure called the return. In this paper, we take the first steps towards a universal off-policy estimator (UnO) - one that provides off-policy estimates and high-confidence bounds for any parameter of the return distribution. We use UnO for estimating and simultaneously bounding the mean, variance, quantiles/median, inter-quantile range, CVaR, and the entire cumulative distribution of returns. Finally, we also discuss Uno's applicability in various settings, including fully observable, partially observable (i.e., with unobserved confounders), Markovian, non-Markovian, stationary, smoothly non-stationary, and discrete distribution shifts.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Problems requiring sequential decision-making are ubiquitous. When online experimentation is costly or dangerous, it is essential to conduct off-policy evaluation before deploying a new policy; that is, one must leverage existing data collected using some policy $\beta$ (called a behavior policy) to evaluate a performance metric of another policy $\pi$ (called the evaluation policy). For problems with high stakes, such as in terms of health or financial assets, it is also crucial to provide high-confidence bounds on the desired performance metric to ensure reliability and safety.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Perhaps the most widely studied performance metric in the off-policy setting is the expected return. However, this metric can be limiting for many problems of interest. Safety-critical applications, such as automated healthcare, require minimizing the chances of risk-prone outcomes, and so performance metrics such as value at risk (VaR) or conditional value at risk (CVaR) are more appropriate. By contrast, applications like online recommendations are subject to noisy data and call for robust metrics like the median and other quantiles. In order to improve user experiences, applications involving direct human-machine interaction, such as robotics and autonomous driving, focus on minimizing uncertainty in their outcomes and thus use metrics like variance and entropy. Recent work in distributional reinforcement learning (RL) have also investigated estimating the cumulative distribution of returns and its various statistical functionals. While it may even be beneficial to use all of these different metrics simultaneously to inform better decision-making, even individually estimating and bounding any performance metric, other than mean and variance, in the off-policy setting has remained an open problem.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This raises the main question of interest: How do we develop a universal off-policy method---one that can estimate any desired performance metrics and can also provide finite-sample confidence bounds that hold simultaneously with high probability for those metrics?

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prior Work: Off-policy methods can be broadly categorized as model-based or model-free. Model-based methods typically require strong assumptions on the parametric model when statistical guarantees are needed. Further, using model-based approaches to estimate parameters other than the mean can also require estimating the distribution of rewards for every state-action pair in order to obtain the complete return distribution for any policy.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

By contrast, model-free methods are applicable to a wider variety of settings. Unfortunately, the popular technique of using importance-weighted returns only corrects for the mean under the off-policy distribution. Recent work by Chandak et al. provides a specialized extension to only correct for the variance. Outside RL, works in the econometrics and causal inference literature have also considered quantile treatments and inferences on counterfactual distributions, but these methods are not developed for sequential decisions and do not provide any high-confidence bounds with guaranteed coverage. Further, they often mandate stationarity, identically distributed data, and full observability (i.e., no confounding).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Existing frequentist high-confidence bounds are not only specifically designed for either the mean or variance, but also hold only individually. Instead of frequentist intervals, a Bayesian posterior distribution over the mean return and various statistics of that distribution can also be obtained. We are not aware of any method that provides off-policy bounds or even estimates for *any* parameter of the return, while also handling different domain settings that are crucial for RL related tasks. Therefore, a detailed discussion of existing work is deferred to Appendix C.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We take the first steps towards a universal off-policy estimator (UnO) that estimates and bounds the entire distribution of returns, and then derives estimates and simultaneous bounds for all parameters of interest. With UnO, we make the following contributions: A. For any distributional parameter (mean, variance, quantiles, entropy, CVaR, CDF, etc.), we provide an off-policy method to obtain (A.1) model-free estimators; (A.2) high-confidence bounds that have guaranteed coverage simultaneously for all parameters and that, perhaps surprisingly, often nearly match or outperform prior bounds specifically designed for the mean and the variance; and (A.3) approximate bounds using statistical bootstrapping that can often be significantly tighter.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

B. The above advantages hold for (B.1) fully observable and partially observable (i.e., with unobserved confounders) settings, (B.2) Markovian and non-Markovian settings, and (B.3) settings with stationary, smoothly non-stationary, and discrete distribution shifts in a policy's performance.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our method uses importance sampling and thus Requires knowledge of action probabilities under the behavior policy $\beta$, Any outcome under the evaluation policy should have a sufficient probability of occurring under $\beta$, and Variance of our estimators scales exponentially with the horizon length, which may be unavoidable in non-Markovian domains.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notation: For brevity, we first restrict our focus to the stationary setting. In Section 5, we discuss how to tackle non-stationarity and distribution shifts. A partially observable Markov decision process (POMDP) is a tuple $(\mathcal{S},\mathcal{O},\mathcal{A},\mathcal{P},\Omega,\mathcal{R},\gamma,d_{0})$, where $\mathcal{S}$ is the set of states, $\mathcal{O}$ is the set of observations, $\mathcal{A}$ is the set of actions, $\mathcal{P}$ is the transition function, $\Omega$ is the observation function, $\mathcal{R}$ is the reward function, $\gamma \in {\lbrack 0,1\rbrack}$ is the discount factor, and $d_{0}$ is the starting state distribution.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although our results extend to the continuous setting, for notational ease, we consider $\mathcal{S},\mathcal{A},\mathcal{O}$, and the set of rewards to be finite. Since the true underlying states are only partially observable, the resulting rewards and transitions from one partially observed state to another are therefore also potentially non-Markovian. We write $S_{t},O_{t},A_{t}$, and $R_{t}$ to denote random variables for state, observation, action, and reward respectively at time $t$. Let $\mathcal{D}$ be a data set ${(H_{i})}_{i = 1}^{n}$ collected using behavior policies ${(\beta_{i})}_{i = 1}^{n}$, where each $H_{i}$ denotes the observed trajectory $(O_{0},A_{0},{\beta{(\left.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since the set of observations, actions, and rewards are finite, and $T$ is finite, the total number of possible trajectories is finite. Let $\mathcal{X}$ be the finite set of returns corresponding to these trajectories. Let $\mathcal{H}_{\pi}$ be the set of all possible trajectories for any policy $\pi$. Sometimes, to make the dependence explicit, we write $g{(h)}$ to denote the return of trajectory $h$. Further, to ensure that samples in $\mathcal{D}$ are informative, we make a standard assumption that any outcome under $\pi$ has sufficient probability of occurring under $\beta$ (see Appendix B.1 for further discussion of assumptions in general),

<!-- chunk {"id": "body-0015", "role": "body", "section": "Idea Summary", "weight": 1.0} -->

For the desired universal method, instead of considering each parameter individually, we suggest estimating the entire cumulative distribution function (CDF) of returns first: Any distributional parameter, $\psi{(F_{\pi})}$, can then be estimated from the estimate of $F_{\pi}$. However, we only have off-policy data from a behavior policy $\beta$, and the typical use of importance sampling only corrects for the mean return. To overcome this, we propose an estimator ${\hat{F}}_{n}$ that uses importance sampling from the perspective of the CDF to correct for the entire distribution of returns. The CDF estimate, ${\hat{F}}_{n}$, is then used to obtain a plug-in estimator $\psi{({\hat{F}}_{n})}$ for any distributional parameter $\psi{(F_{\pi})}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Idea Summary", "weight": 1.0} -->

Next, we show that this CDF-centric perspective provides the additional advantage that, if we can compute a $1 - \delta$ confidence band $\mathcal{F}:{{\mathbb{R}}\rightarrow 2^{\mathbb{R}}}$ such that then a $1 - \delta$ upper (or lower) high-confidence bound on any parameter, $\psi{(F_{\pi})}$, can be obtained by searching for a function $F$ that maximizes (or minimizes) $\psi{(F)}$ and ${\forall\nu} \in {\mathbb{R}}$ has ${F{(\nu)}} \in {\mathcal{F}{(\nu)}}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "UnO: Universal Off-Policy Estimator", "weight": 1.0} -->

In the on-policy setting, one approach for estimating any parameter of returns, $G_{\pi}$, might be to first estimate its cumulative distribution $F_{\pi}$ and then use that to estimate its parameter $\psi{(F_{\pi})}$. However, doing this in the off-policy setting requires additional consideration as the entire distribution of the observed returns needs to be adjusted to estimate $F_{\pi}$ since the data is collected using behavior policies that can be different from the evaluation policy $\pi$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "UnO: Universal Off-Policy Estimator", "weight": 1.0} -->

We begin by observing that ${\forall\nu} \in {{\mathbb{R}},{F_{\pi}{(\nu)}}}$ can be expanded using the fact that the probability that the return $G_{\pi}$ equals $x$ is the sum of the probabilities of the trajectories $H_{\pi}$ whose return equals $x$, where $\mathbb{1}_{A} = 1$ if $A$ is true and 0 otherwise. Now, observing that the indicator function can be one for at most a single value less than $\nu$ as $g{(h)}$ is a deterministic scalar given $h$, can be expressed as, where the red color is used to highlight changes. Now, from \\threfass:support as ${{\forall\beta},\mathcal{H}_{\pi}} \subseteq \mathcal{H}_{\beta}$,^11^1Results can be extended to hybrid probability measures using Radon-Nikodym derivatives.

<!-- chunk {"id": "body-0019", "role": "body", "section": "UnO: Universal Off-Policy Estimator", "weight": 1.0} -->

The form of $F_{\pi}{(\nu)}$ in is beneficial as it suggests a way to not only perform off-policy corrections for one specific parameter, as in prior works, but for the entire cumulative distribution function (CDF) of return $G_{\pi}$. Formally, let $\rho_{i} ≔ {\prod_{j = 0}^{T}\frac{\pi{(\left. A_{j} \middle| O_{j} \right.)}}{\beta_{i}{(\left. A_{j} \middle| O_{j} \right.)}}}$ denote the importance ratio for $H_{i}$, which is equal to ${\Pr{({H_{\pi} = h})}}/{\Pr{({H_{\beta} = h})}}$ (see Appendix D).

<!-- chunk {"id": "body-0020", "role": "body", "section": "UnO: Universal Off-Policy Estimator", "weight": 1.0} -->

Then, based, we propose the following non-parametric and model-free estimator for $F_{\pi}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Notice that the value of ${\hat{F}}_{n}{(\nu)}$ can be more than one, even though $F_{\pi}{(\nu)}$ cannot have a value greater than one for any $\nu \in {\mathbb{R}}$. This is an expected property of estimators based on importance sampling (IS). For example, the IS estimates of expected return during off-policy mean estimation can be smaller or larger than the smallest and largest possible return when $\rho > 1$. \\thlabelrem:geq1 Having an estimator ${\hat{F}}_{n}$ of $F_{\pi}$, any parameter $\psi{(F_{\pi})}$ can now be estimated using $\psi{({\hat{F}}_{n})}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 1", "weight": 1.0} -->

However, some parameters like the mean $\mu_{\pi}$, variance $\sigma_{\pi}^{2}$, and entropy $\mathcal{H}_{\pi}$, are naturally defined using the probability distribution $\text{d}F_{\pi}$ instead of the cumulative distribution $F_{\pi}$. Similarly, parameters like the $\alpha$-quantile $Q_{\pi}^{\alpha}$ and inter-quantile range (which provide tail-robust measures for the mean and deviation from the mean) and conditional value at risk $\text{CVaR}_{\pi}^{\alpha}$ (which is a tail-sensitive measure) are defined using the inverse CDF $F_{\pi}^{- 1}{(\alpha)}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Therefore, let ${(G_{(i)})}_{i = 1}^{n}$ be the order statistics for samples ${(G_{i})}_{i = 1}^{n}$ and $G_{} ≔ G_{\min}$. Then, we define the off-policy estimator of the inverse CDF for all $\alpha \in {\lbrack 0,1\rbrack}$, and the probability distribution estimator $d{\hat{F}}_{n}$ as, where ${\text{d}{\hat{F}}_{n}{(\nu)}} ≔ 0$ if $\nu \neq G_{(i)}$ for any $i \in {(1,\ldots,n)}$. Using, we now define off-policy estimators for parameters like the mean, variance, quantiles, and CVaR (see Appendix E.1 for more details on these).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 1", "weight": 1.0} -->

This procedure can be generalized to any other parameter of $F_{\pi}$ for which a sample estimator $\psi{({\hat{F}}_{n})}$ can be directly created using ${\hat{F}}_{n}$ as a plug-in estimator for $F_{\pi}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Let $H_{i}$ be the observed trajectory for the $G_{i}$ that gets mapped to $G_{(i)}$ when computing the order statistics. Note that $\text{d}{\hat{F}}_{n}{(G_{(i)})}$ equals $\rho_{i}/n$ for this $H_{i}$. This implies that the estimator for the mean, $\mu_{\pi}{({\hat{F}}_{n})}$, reduces exactly to the existing full-trajectory-based IS estimator.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Notice that many parameters and their sample estimates discussed above are nonlinear in $F_{\pi}$ and ${\hat{F}}_{n}$, respectively (the mean is one exception). Therefore, even though ${\hat{F}}_{n}$ is an unbiased estimator of $F_{\pi}$, the sample estimator, $\psi{({\hat{F}}_{n})}$, may be a biased estimator of $\psi{(F_{\pi})}$. This is expected behavior because even in the on-policy setting it is not possible to get unbiased estimates of some parameters (e.g., standard deviation), and UnO reduces to the on-policy setting when $\pi = \beta$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 2", "weight": 1.0} -->

However, perhaps surprisingly, we establish in the following section that even when $\psi{({\hat{F}}_{n})}$ is a biased estimator of $\psi{(F_{\pi})}$, high-confidence upper and lower bounds can still be computed for both $F_{\pi}$ and $\psi{(F_{\pi})}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "High-Confidence Bounds for UnO", "weight": 1.0} -->

Off-policy estimators are typically prone to high variance, and when the domain can be non-Markovian, the curse of horizon might be unavoidable. For critical applications, this might be troublesome and thus necessitates obtaining confidence intervals to determine how much our estimates can be trusted. Therefore, in this section, we aim to construct a set of possible CDFs $\mathcal{F}:{{\mathbb{R}}\rightarrow 2^{\mathbb{R}}}$, called a confidence band, such that the true $F_{\pi}{(\nu)}$ is within the set $\mathcal{F}{(\nu)}$ with high probability, i.e., ${\Pr{({{\forall\nu} \in {\mathbb{R}}},{{F_{\pi}{(\nu)}} \in {\mathcal{F}{(\nu)}}})}} \geq {1 - \delta}$, for any $\delta \in {(0,1\rbrack}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "High-Confidence Bounds for UnO", "weight": 1.0} -->

Subsequently, we develop finite-sample bounds for any parameter $\psi{(F_{\pi})}$ using $\mathcal{F}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "High-Confidence Bounds for UnO", "weight": 1.0} -->

In the on-policy setting, $\mathcal{F}$ can be constructed using the DKW inequality and its tight constants. However, its applicability to the off-policy setting is unclear as (a) unlike the on-policy CDF estimate, the "steps" of an off-policy CDF estimate are not of equal heights, (b) the "steps" do not sum to one (see Figure 2) and the maximum height of the steps need not be known either, and (c) DKW assumes samples are identically distributed, however, off-policy data $\mathcal{D}$ might be collected using multiple different behavior policies. This raises the question: How do we obtain $\mathcal{F}$ in the off-policy setting?

<!-- chunk {"id": "body-0031", "role": "body", "section": "High-Confidence Bounds for UnO", "weight": 1.0} -->

Before constructing a confidence band $\mathcal{F}$, let us first focus on obtaining bounds for a single point, $F_{\pi}{(\kappa)}$. Let $X ≔ {\rho{(\mathbb{1}_{\{{G \leq \kappa}\}})}}$. Then, from \\threfthm:Funbiased, we have that ${{\mathbb{E}}_{\mathcal{D}}{\lbrack X\rbrack}} = {F_{\pi}{(\kappa)}}$. This implies that a confidence interval for the mean of $X$ provides a confidence interval for $F_{\pi}{(\kappa)}$. Using this observation, existing confidence intervals for the mean of a bounded random variable can be directly applied to $X$ to obtain a confidence interval for $F_{\pi}{(\kappa)}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "High-Confidence Bounds for UnO", "weight": 1.0} -->

For example, Thomas et al. present tight bounds for the mean of IS-based random variables by mitigating the variance resulting from the heavy tails associated with IS; we use their method on ${\hat{F}}_{n}{(\kappa)}$ to bound $F_{\pi}{(\kappa)}$. Alternatively, recent work by Kuzborskij et al. can potentially be used with a WIS-based $F_{\pi}$ estimate.

<!-- chunk {"id": "body-0033", "role": "body", "section": "High-Confidence Bounds for UnO", "weight": 1.0} -->

Before moving further, we introduce some additional notation. Let ${(\kappa_{i})}_{i = 1}^{K}$ be any $K$ "key points" and let $\text{CI}_{-}{(\kappa_{i},\delta_{i})}$ and $\text{CI}_{+}{(\kappa_{i},\delta_{i})}$ be the lower and the upper confidence bounds on $F_{\pi}{(\kappa_{i})}$ constructed at each key point using the observation made in the previous paragraph, such that We now use the following observation to obtain a band, $\mathcal{F}$, that contains $F_{\pi}$ with high confidence.

<!-- chunk {"id": "body-0034", "role": "body", "section": "High-Confidence Bounds for UnO", "weight": 1.0} -->

\begin{cases} {\min\limits_{\kappa_{i}\geq\nu}\text{CI}_{+}{(\kappa_{i},\delta_{i})}} & {\text{otherwise}.} Figure 2: An illustration of F̂n (in black) using five return samples and the confidence band ℱ (red shaded region) computed using with confidence intervals (red lines) at three key points (κi)i = 13. Notice that the vertical “steps” in F̂n can be of different heights and their total can be greater than 1 due to importance weighting. However, since we know that Fπ is never greater than 1, ℱ can be clipped at 1.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Notice that any choice of ${(\kappa_{i})}_{i = 1}^{K}$ results in a valid band $\mathcal{F}$. However, $\mathcal{F}$ can be made tighter by optimizing over the choice of ${(\kappa_{i})}_{i = 1}^{K}$. In Appendix E.5, we present one such method using cross-validation to minimize the area enclosed within $\mathcal{F}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Having obtained a high-confidence band for $F_{\pi}$, we now discuss how high-confidence bounds for any parameter $\psi{(F_{\pi})}$ can be obtained using this band. Formally, with a slight overload of notation let $\mathcal{F}$ be the set of all possible CDFs bounded between $F_{-}$ and $F_{+}$, that is, This band $\mathcal{F}$ contains many possible CDFs, one of which is $F_{\pi}$ with high probability.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 4", "weight": 1.0} -->

Perhaps surprisingly, even though $\psi{({\hat{F}}_{n})}$ may be biased, we can obtain high-confidence bounds with guaranteed coverage on any $\psi{(F_{\pi})}$ using the confidence band $\mathcal{F}$. In fact, confidence bounds for *all* parameters computed using hold *simultaneously* with probability at least $1 - \delta$ as they are all derived from the same confidence band, $\mathcal{F}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 4", "weight": 1.0} -->

Unlike the bounds, BCa-based bounds do not offer guaranteed coverage and need to be computed individually for each parameter $\psi$. However, they can be combined with UnO to get significantly tighter bounds with less data, albeit without guaranteed coverage.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Confounding, Distributional Shifts, and Smooth Non-Stationarities", "weight": 1.0} -->

A particular advantage of UnO is the remarkable simplicity with which the estimates and bounds for $F_{\pi}$ or $\psi{(F_{\pi})}$ can be extended to account for confounding, distributional shifts, and smooth non-stationarities that are prevalent in real-world applications.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Confounding, Distributional Shifts, and Smooth Non-Stationarities", "weight": 1.0} -->

Confounding / Partial Observability: Estimator ${\hat{F}}_{n}$ in accounts for partial observability when both $\pi$ and $\beta$ have the same observation set. However, in systems like automated loan approval, data might have been collected using a behavior policy $\beta$ dependent on sensitive attributes like race and gender that may no longer be allowable under modern laws. This can make the available observation, $\overset{\sim}{O}$, for an evaluation policy $\pi$ different from the observations, $O$, for $\beta$, which may also have been a partial observation of the underlying true state $S$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Confounding, Distributional Shifts, and Smooth Non-Stationarities", "weight": 1.0} -->

However, an advantage of many such automated systems (e.g., online recommendation, automated healthcare, robotics) is the direct availability of behavior probabilities $\beta_{i}{(\left. A \middle| O \right.)}$. In Appendix D, we provide generalized proofs for all the earlier results, showing that access to $\beta_{i}{(\left. A \middle| O \right.)}$ allows UnO to handle various sources of confounding even when $\overset{\sim}{O} \neq O$, without requiring any additional adjustments. When $\beta_{i}{(\left. A \middle| O \right.)}$ is not available, we allude to possible alternatives in Appendix B.1.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Confounding, Distributional Shifts, and Smooth Non-Stationarities", "weight": 1.0} -->

Distribution Shifts: Many practical applications exhibit distribution shifts that might be discrete or abrupt. One example is when a medical treatment developed for one demographic is applied to another. To tackle discrete distributional shifts, let $F_{\pi}^{}$ and $F_{\pi}^{}$ denote the CDFs of returns under policy $\pi$ in the first and the second domain, respectively. To make the problem tractable, similar to prior work on characterizing distribution shifts, we assume that the Kolmogorov-Smirnov distance between $F_{\pi}^{}$ and $F_{\pi}^{}$ is bounded.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

In particular, we propose using wild bootstrap, which provides approximate CIs with finite sample error of $O{(L^{- {1/2}})}$ while also handling non-normality and heteroskedasticity, which would occur when dealing with IS-based estimates resulting from different behavior polices. See Appendix E.6 for more details. Finally, using the bounds obtained using wild bootstrap at multiple key points, an entire confidence band can be obtained as discussed in Section 4.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Empirical Studies", "weight": 1.0} -->

In this section, we provide empirical support for the established theoretical results for the proposed UnO estimator and high-confidence bounds. To do so, we use the following domains: An open source implementation of the FDA-approved type-$1$ diabetes treatment simulator, A stationary and a non-stationary recommender system domain, and A continuous-state Gridworld with partial observability, where data is collected using multiple behavior policies. Detailed description for domains and the procedures for obtaining $\pi$ and $\beta$ are provided in Appendix F.1; code is also publicly available here. In the following, we discuss four primary takeaway results.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Empirical Studies", "weight": 1.0} -->

\(A\) Characteristics of the UnO estimator: Figure 4 reinforces the universality of UnO. As can be seen, UnO can accurately estimate the entire CDF and a wide range of its parameters: mean, variance, quantile, and CVaR.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Empirical Studies", "weight": 1.0} -->

\(B\) Comparison of UnO with prior work: Recent works for bounding the mean assume no confounding and Markovian structure. Therefore, for a fair comparison, we resort to the method of Thomas et al. that can provide tight bounds even when the domain is non-Markovian or has confounding (partial observability). Perhaps surprisingly, Figure 4 shows that the proposed guaranteed coverage bounds, termed UnO-CI here, can be competitive with this existing specialized bound, termed Baseline-CI here, for the mean. In fact, UnO-CI can often require an order of magnitude less data compared to the specialized bounds for variance; we refer readers to Appendix F.2 for a discussion on potential reasons. This suggests that the universality of UnO can be beneficial even when only one specific parameter is of interest.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Empirical Studies", "weight": 1.0} -->

\(C\) Finite-sample confidence bounds for other parameters using UnO: Figure 4 demonstrates that UnO-CI also successfully addresses the open question of providing guaranteed coverage bounds for multiple parameters simultaneously without additional applications of the union bound. As expected, bounds for parameters like variance and CVaR that depend heavily on the distribution tails take more samples to shrink than bounds on other parameters (like the median \[quantile($0.5$)\]). Additional discussion on the observed trends for the bounds is provided in Appendix F.2.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Empirical Studies", "weight": 1.0} -->

The proposed UnO-Boot bounds, as discussed in Section 3.1, are approximate and might not always hold with the specified probability. However, they stand out by providing significantly tighter, and thus more practicable, confidence intervals.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Empirical Studies", "weight": 1.0} -->

\(D\) Results for non-stationary settings: Results for this setting are presented in Figure 5. As discussed earlier, online recommendation systems for tutorials, movies, advertisements and other products are ubiquitous. However, the popular assumption of stationarity is seldom applicable to these systems. In particular, personalizing for each user is challenging in such settings as interests of a user for different items among the recommendable products fluctuate over time. For an example, in the context of online shopping, interests of customers can vary based on seasonality or other unknown factors. To abstract such settings, in this domain the reward (interest of the user) associated with each item changes over time. See Figure 5 (top row) for visualization of the domain, for different "speeds" (degrees of non-stationarity).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Empirical Studies", "weight": 1.0} -->

In all the settings with different speeds, a uniformly random policy was used as a behavior policy $\beta$ to collect data for $1000$ episodes. To test the efficacy of UnO, when the future domain can be different from the past domains, the evaluation policy was chosen to be a near-optimal policy for the future episode: $1000 + 1$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have taken the first steps towards developing a *universal off-policy estimator* (UnO), closing the open question of whether it is possible to estimate and provide finite-sample bounds (that hold with high probability) for any parameter of the return distribution in the off-policy setting, with minimal assumptions on the domain. Now, without being restricted to the most common and basic parameters, researchers and practitioners can fully characterize the (potentially dangerous or costly) behavior of a policy without having to deploy it.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion", "weight": 1.5} -->

There are many new questions regarding how UnO can be improved for policy evaluation by further reducing data requirements or weakening assumptions. Using UnO for policy improvement also remains an interesting future direction. Subsequent to this work, Huang et al. showed how models can be used to obtain UnO-style doubly robust estimators along with its convergence rates in the contextual bandit setting. This allows their method to also provide finite-sample uniform CDF bounds for a broad class of Lipschitz risk functionals.
