<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Risk-aware Product Decisions in A/B Tests with Multiple Metrics

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In the past decade, AB tests have become the standard method for making product decisions in tech companies. They offer a scientific approach to product development, using statistical hypothesis testing to control the risks of incorrect decisions. Typically, multiple metrics are used in AB tests to serve different purposes, such as establishing evidence of success, guarding against regressions, or verifying test validity. To mitigate risks in AB tests with multiple outcomes, it's crucial to adapt the design and analysis to the varied roles of these outcomes. This paper introduces the theoretical framework for decision rules guiding the evaluation of experiments at Spotify. First, we show that if guardrail metrics with non-inferiority tests are used, the significance level does not need to be multiplicity-adjusted for those tests. Second, if the decision rule includes non-inferiority tests, deterioration tests, or tests for quality, the type II error rate must be corrected to guarantee the desired power level for the decision. We propose a decision rule encompassing success, guardrail, deterioration, and quality metrics, employing diverse tests. This is accompanied by a design and analysis plan that mitigates risks across any data-generating process. The theoretical results are demonstrated using Monte Carlo simulations.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Randomized experiments are the gold standard for providing evidence for causal relationships. Modern technology companies use A/B tests, a randomized controlled trial in a digital setting, extensively to evaluate the efficacy of new changes to their products. These products include ride-sharing apps, search engines, streaming services, recommendations, and more. Ultimately, the goal of these experiments is to decide whether or not to release a product change more widely.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most of the literature on statistical inference for randomized experiments focuses on a single hypothesis test of a single outcome, and how to bound the type I and type II error rates for that test. However, experiments are not univariate tests of isolated outcomes. Instead, the risks that matter are the risks of making the incorrect decision for the product. For example, at a tech company like Spotify, we want to limit how often we release product changes that show an improvement when there truly is none, and how often we refrain from releasing changes that lead to improvements but we fail to find. These types of decisions typically include results from several hypothesis tests. Experiments usually involve results for multiple outcomes, and making a single decision based on these multiple outcomes can be challenging. For example, some of the outcomes, what we will refer to as 'metrics', may show improvements, while others show none or even negative effects.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the online experimentation literature, the only aspect of multi-test decision making that is extensively covered is multiple-testing correction. Multiple-testing corrections, such as Bonferroni, Holm and Hommel, bound the type I error rate of an implied decision rule that declares what decision you will make based on the results of the individual hypothesis tests. As we will discuss extensively in this paper, unless your desired decision rule matches the rule implied by the multiple-testing correction, it is typically incorrect.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we show how it is possible to formalize the decision-making process of experiments without leaving the standard hypothesis testing framework. The key to ensuring that you obtain the intended risk bounds for the product decision is to explicitly specify a decision rule. A decision rule exhaustively specifies what product decision you will make based on the results of your experiment. Importantly, to bound the risks of making an erroneous decision, the design and analysis of your experiment must be closely aligned with the decision rule.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Articulating the decision rule is important for several reasons. Being unclear about what outcomes lead to a positive product decision means that there is no mechanism for properly controlling the risks of the experiment at the level that matters to the company, namely the decision to ship the feature or not. Additionally, a lack of an articulated and standardized decision rule can mean that different teams or parts of the organization hold themselves to different standards. Our decision rule framework is a simple but effective approach for combating those issues.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The decision rule framework helps standardize the analysis of experiments and is a useful tool for experimentation platforms. What the decision rule includes can be made more or less flexible. For example, new experiments can be forced to demonstrate that important company metrics are not negatively impacted while selecting the set of metrics that should show an improvement is made completely up to the experimenter. Even if the choice of metrics is completely arbitrary with no metrics made mandatory by the platform, the decision rule approach promotes a shared understanding of what a successful experiment is.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Throughout this paper, and without loss of generality, we only consider experiments with two groups to simplify notation. In addition, we only consider one-sided tests, although more than one one-sided test might be applied to each metric. We limit ourselves to one-sided tests as there must be an intended direction for a change in the metric to map to a measurable improvement in the product. For simplicity, we assume that all metrics improve when they increase. Moreover, we assume that each statistical hypothesis test is valid and achieves its type I and type II error rates exactly if the experiment is designed accordingly.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Related literature", "weight": 1.0} -->

Decision theory is a formal mathematical framework for formalizing decision problems under uncertainty, see e.g. for an introduction. Although this theory is comprehensive and flexible, it is non-trivial for most people, and it moves the decision problem far from the (to most experimenters) familiar hypothesis-testing realm. Since modern tech companies are often having many teams experimenting independently, it is not plausible to have decision theory experts available to all.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Related literature", "weight": 1.0} -->

Another popular alternative for decision making in A/B tests where the goal is to evaluate using several outcomes is to use a so-called overall evaluation criterion (OEC), see e.g. for a recent introduction. An OEC removes the problem with several possibly contradictory results by using just a single metric. This metric can either be a metric that serves as a proxy for all the necessary aspects of the important outcomes, or it is a function, like a linear combination, of a selected set of metrics. Designing an appropriate OEC generally requires prolonged research and strong alignment within the organization. For larger companies, a single OEC may not even suffice because the business itself is diverse. Moreover, if the OEC is a complicated function of several outcomes, it can be difficult for experimenters to understand their results. Even when an OEC is used, it is not common that this metrics include all quality tests and metrics that should not deteriorate.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Related literature", "weight": 1.0} -->

That is, an OEC is typically a metric that trades off various outcomes to define success, but as we will show in the paper, a product decision rule can also explicitly include the efforts to avoid end-user harm and experiment invalidity which in turn affects the power analysis and design of the experiment.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Related literature", "weight": 1.0} -->

In the clinical trial literature (for an overview, see 3, ch. 4; 16), so-called multiple endpoint experiments, are experiments with more than one outcome (metric). The endpoints can be both efficacy (success metrics) and safety endpoints (guardrail metrics). In some trials, there are also primary endpoints and secondary endpoints, where the secondary endpoints are only evaluated if primary endpoints are significantly changed. Clearly, this setting closely resembles the online experimentation setting. Similarly to deciding whether a new drug or treatment is safe and effective, deciding whether to ship a new feature is a composite decision that involves a potentially complex interplay between all endpoints. Various experimental design and analysis methods have been applied in the clinical trial setting: hierarchical testing where primary endpoints are tested before secondary, global assessment measures where the endpoints are aggregated within each patient first then analyzed with standard statistical methods, closed testing where a global null is tested first before proceeding to more specific hypotheses. However, at companies like Spotify, there's a strong need to standardize the design, analysis and decision process of multiple endpoint experiments to allow non-statisticians to evaluate product changes in a safe and efficient way.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Types of metrics and their hypotheses", "weight": 1.0} -->

Throughout the paper, we assume that the aim of the statistical analysis of an experiment is to make a binary decision regarding the success of the treatment. This decision can be e.g. whether or not to go ahead with the next step of validation for a medical treatment, or whether or not to ship a product change. Our goal is to bound the type I and type II error for this decision in repeated experimentation. We will focus on the product decision example, but the results are applicable in a wider, more general setting.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Types of metrics", "weight": 1.0} -->

In modern online experimentation, experiments are evaluated using multiple metrics. Based on the results from each metric, typically estimates of the average treatment effects, the experimenters make a decision whether to ship the feature more widely. The heuristics underlying the decision-making process are seldom transparent. In large organizations, these decision processes often vary substantially from team to team. At Spotify, we have introduced a standardized way of providing a recommendation for a suggested course of action given the outcomes for a set of metrics that belong to different categories. We call this recommendation a shipping recommendation. These recommendations are powered by a decision rule that includes four types of metrics and their associated hypotheses and tests, given by Success metrics. Metrics that we aim to improve, tested with superiority tests.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Types of metrics", "weight": 1.0} -->

Guardrail metrics. Metrics that we do not want to see deteriorate more than a certain threshold, tested with non-inferiority tests.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Types of metrics", "weight": 1.0} -->

Deterioration metrics. Metrics that should not deteriorate, tested with inferiority tests.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Types of metrics", "weight": 1.0} -->

Quality metrics. Metrics that verify the integrity and validity of the experiment itself.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Types of metrics", "weight": 1.0} -->

A metric can belong to multiple categories. For example, at Spotify, all success and guardrail metrics also belong to deterioration metrics. We will elaborate on the details of this in later sections, but the implication is that we monitor all metrics for regressions, even if our goal and hypothesis is for them to improve. Quality metrics are not always metrics in the traditional sense. For example, a crucial experiment-quality metric is the sample ratio mismatch test. This is not a metric in the traditional sense, but rather a goodness of fit test of proportions.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Types of metrics", "weight": 1.0} -->

Music minutes played Podcast minutes played Music minutes played Podcast minutes played Share of users with a crash Sample ratio mismatch Table 1: Example set of metrics for an experiment. The success and guardrail metrics in the experiment appear a second time as deterioration metrics to ensure they are not unknowingly moving in the wrong direction.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Types of metrics", "weight": 1.0} -->

Table 1 shows an example of a set of metrics used in an experiment. In this case, the experiment attempts to increase the minutes played of music, but includes podcast minutes played to verify that overall consumption does not increase at the expense of podcast consumption. Both metrics are also included as deterioration metrics to ensure that they are not moving in the direction that is opposite from what we would expect and hope. Additionally, the share of users that experience a crash is included as deterioration metric. The only quality metric in this case is a sample ratio mismatch metric.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Types of metrics", "weight": 1.0} -->

In the following, we use "inferiority test" to equivalently mean "deterioration test", which, given our standarization that a decrease is a regression, is a test for the deterioration of a metric. With some abuse of language, we sometimes say "metric $x$ was significantly superior" to mean that the "treatment was significantly superior to control with respect to metric $x$".

<!-- chunk {"id": "body-0023", "role": "body", "section": "Hypotheses for different types of metrics", "weight": 1.0} -->

The different categories of metrics serve different purposes, which by extension means that their associated statistical hypotheses are different. Table 2 displays the hypotheses for these categories of metrics used in the decision rules considered in this paper.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Hypotheses for different types of metrics", "weight": 1.0} -->

Effect used for Table 2: Hypotheses for the the three main types of metrics considered in the decision rules, where δ is the estimand, like the average treatment effect, of interest. The hypotheses of the quality tests are left out because they typically are not using the same kind of estimands as the others with varying hypotheses as a consequence. The minimum detectable effect (MDE) is the effect size used for success metrics when designing the experiment. The non-inferiority margin (NIM) is the tolerance level of regression used in the non-inferiority tests used for guardrail metrics. Status quo is not a hypothesis in the traditional sense, but a scenario of interest later in the paper.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Hypotheses for different types of metrics", "weight": 1.0} -->

While the hypotheses are similar------and to some degree even opposites of one another------they give rise to distinct interpretations. For example, the alternative of the non-inferiority test for which we design the experiment to be powered is the null hypothesis for the superiority test, which means that under the null hypothesis a guardrail metric has deteriorated by $NIM$ (non-inferiority margin). We also consider a third hypothesis-like scenario, the "status quo" in which no metric has moved, to facilitate our discussion. The status quo scenario is thus under the alternative for the non-inferiority and under the null hypothesis for the superiority tests and deterioration tests.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Type I and Type II error rates for decision rules including superiority and non-inferiority tests", "weight": 1.0} -->

The categorization of metrics into success, guardrail, deterioration and quality metrics naturally paves the way for a decision rule that combines the results of metrics in each category appropriately. The decision rule, in turn, implies various multiple-testing corrections for the statistical inference to control both the type I and type II error rates of the shipping decision as intended. In this section, we start by establishing some fundamental results for superiority and non-inferiority testing, and, more generally, for union-intersection and intersection-union testing that these rely. These results are then used to construct a decision rule that includes superiority and non-inferiority tests. In subsequent sections, we include deterioration tests and finally quality metrics.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Type I and Type II error rates for decision rules including superiority and non-inferiority tests", "weight": 1.0} -->

The goal of the designs in this paper is to bound the family-wise error rates of the decision. In the following, we focus our discussion on Bonferroni-based adjustments for multiple comparisons that let us use results of individual tests to evaluate the joint global hypothesis. There are two main contributing factors to why we choose this approach: Interpretability is greatly simplified when experimenters can view individual results for metrics (including confidence intervals).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Type I and Type II error rates for decision rules including superiority and non-inferiority tests", "weight": 1.0} -->

By evaluating a global hypothesis consisting of individual of hypotheses for multiple metrics through individual tests, we can fit our framework into a large, scalable experimentation platform where a decision rule approach fits seamlessly into other core experimentation functionality like sequential testing, variance reduction, and more.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Type I and Type II error rates for decision rules including superiority and non-inferiority tests", "weight": 1.0} -->

While other multiple-testing adjustment procedures often are more powerful, they generally achieve more power at the expense of interpretability and ease of understanding. For example, Holm's multiple correction method is generally more powerful than Bonferroni's, but the associated confidence intervals under are more complicated and do not always yield finite bounds. Even when confidence intervals are available, explaining the correction and how it affects the intervals to experimenters is non-trivial.

<!-- chunk {"id": "body-0030", "role": "body", "section": "The composite hypotheses of superiority and non-inferiority tests", "weight": 1.0} -->

To facilitate our discussion about overall decision rules, we first describe the hypotheses for the superiority and non-inferiority tests used for success and guardrail metrics. Let $H_{0}^{(\mathcal{L})}$ be the null hypothesis for a set of tests, where the superscript indicates the type of the tests. We occasionally drop the superscript when it is given by the context. Let $H_{\mathcal{A}}^{(\mathcal{L})}$ be the alternative hypothesis.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Bounding the type I and type II error rates for UI and IU testing", "weight": 1.0} -->

Because the at-least-one testing for superiority is based on the UI testing principle, individual tests must be carried out at an adjusted significance level to ensure that the family-wise error rate is bounded by the nominal significance level. On the other hand, no adjustment is necessary to the nominal power level used when designing the experiment. The at-least-one testing principle implies that the composite test has a family-wise type II error rate that is bounded from above by the nominal level. For the all-or-none testing used to establish non-inferiority, it is not necessary to multiplicity adjust the individual significance level used in the tests.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Bounding the type I and type II error rates for UI and IU testing", "weight": 1.0} -->

The error bounding of the decision rules that we propose in this paper heavily relies on the bounding of error rates for UI and IU testing. Therefore, we establish this more formally below. Let $\theta$ be the parameter of interest, and let $\theta_{0}$ be the parameter value under $H_{0}$ and let $\theta_{\mathcal{A}}$ be the parameter value under $H_{\mathcal{A}}$ for which the power is $1 - \beta$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Bounding the type I and type II error rates for UI and IU testing", "weight": 1.0} -->

For tests that rely on the UI principle, only the individual type I error rate needs to be corrected to bound the overall type I and type II error rates. We formalize this in Lemma 3.1. ‣ 3.2 Bounding the type I and type II error rates for UI and IU testing ‣ 3 Type I and Type II error rates for decision rules including superiority and non-inferiority tests ‣ Risk-aware product decisions in A/B tests with multiple metrics").

<!-- chunk {"id": "body-0034", "role": "body", "section": "Bounding the error rates for a decision rule including both success and guardrail metrics", "weight": 1.0} -->

The decision rule we use combines superiority and non-inferiority testing, and appropriate adjustments to individual-level tests follow immediately from the results of the previous section. Before we discuss these adjustments, we first describe the decision rule.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Decision Rule 1", "weight": 1.0} -->

Ship the change if and only if: at least one success metric is significantly superior all guardrail metrics are significantly non-inferior.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Decision Rule 1", "weight": 1.0} -->

That is, ship if and only if the global superiority/non-inferiority null hypothesis is rejected in favor of the alternative hypothesis.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Decision Rule 1", "weight": 1.0} -->

We can now establish how to adjust Decision Rule 1 to ensure that family-wise type I or type II error rates are not inflated. The decision rule consists of two levels of testing and can be mathematically stated as: The testing problem is thus an intersection-union test consisting of $G + 1$ hypotheses---$G$ hypotheses for the guardrail metrics, and one additional composite hypothesis concerning the at-least-one test for superiority. By applying Lemma 3.1. ‣ 3.2 Bounding the type I and type II error rates for UI and IU testing ‣ 3 Type I and Type II error rates for decision rules including superiority and non-inferiority tests ‣ Risk-aware product decisions in A/B tests with multiple metrics") and 3.2. ‣ 3.2 Bounding the type I and type II error rates for UI and IU testing ‣ 3 Type I and Type II error rates for decision rules including superiority and non-inferiority tests ‣ Risk-aware product decisions in A/B tests with multiple metrics"), we can establish the necessary adjustments for the decision rule, formalized in Proposition 3.1.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Power corrections for non-inferiority testing", "weight": 1.0} -->

Power corrections (or, equivalently, "beta corrections") have, to the best of our knowledge, not been discussed in the online experimentation literature. However, the importance of adjusting power in the presence of IU testing is known in the statistical literature (9; 16; 3, ch. 4). These corrections are crucial to ensure appropriate levels of power when using non-inferiority tests, since the goal is to find evidence for non-inferiority in all tests simultaneously. The intuition for power corrections for multiple guardrails tested with non-inferiority tests is analogous to standard multiple-testing corrections of type I error rates. If, e.g., all guardrail metrics are independent and each guardrail metric has a NIM for which the power is 80%, then the probability that at least one of them is not significantly non-inferior under the alternative quickly goes towards one as the number of guardrail metrics increase. Under independence, the number of significant guardrail metrics out of a total of $G$ guardrail metrics is distributed as ${Bin}{(G,0.8)}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Power corrections for non-inferiority testing", "weight": 1.0} -->

The power for the decision rule, assuming only independent guardrail metrics, is simply $0.8^{G}$, which decays quickly in $G$. Figure 1 displays how the power of the decision rule drops. Already at 10 guardrail metrics, the simultaneous power is less than 11% without adjustment.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Power corrections for non-inferiority testing", "weight": 1.0} -->

For theoretical bounds on the type I and type II error rates for Decision rule 1 under perfect linear correlation and independence, respectively, see appendix Section B.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Extending the decision rule with deterioration and quality metrics", "weight": 1.0} -->

Deterioration tests are inferiority tests that aim to capture regressions in metrics. They can be applied to metrics already present as a success or a guardrail metric, or to metrics that are only included in this category as deterioration metrics. The test checks if the metric is significantly deteriorating. That is, if the treatment group is significantly inferior to the control group with respect to the metric of interest. Deterioration tests for success and guardrail metrics attempt to identify significant regressions, which would, if they exist, speak against the success of the experiment. Neither the superiority test used for success metrics or the non-inferiority test used for guardrail metrics would on its own indicate a regression. Knowing when regressions occur is essential when running experiments.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Extending the decision rule with deterioration and quality metrics", "weight": 1.0} -->

In practice, in addition to success, guardrail and detrioriation metrics, also experiment-quality metrics are used. For example, at Spotify, we include a set of tests and metrics that evaluate the quality of the experiment. These include a test for balanced traffic through a sample ratio mismatch test, and a test for pre-exposure bias. By including deterioration and quality tests in the decision rule, the complexity to manage the risks of an incorrect decision increases. Decision Rule 2 formalizes the complete decision rule that is used at Spotify.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Decision Rule 2", "weight": 1.0} -->

Ship the change if and only if: at least one success metric is significantly superior all guardrail metrics are significantly non-inferior none of the success, guardrail or deterioration metrics are significantly inferior none of the quality tests are significantly rejecting quality That is, ship if and only if the global superiority/non-inferiority null hypothesis is rejected in favor of the alternative hypothesis, the inferiority null hypothesis is not rejected for any metric, and no quality test is significant.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Decision Rule 2", "weight": 1.0} -->

Proposition 4.1 displays the corresponding correction, to bound the error rates of Decision Rule 2.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Monte Carlo simulation study", "weight": 1.0} -->

In this section we run a simulation study to illustrate the empirical error rates for the multi-metric decision rules with and without the alpha and power corrections ^11^1Code for replication can be found at To make the simulation more relevant, all deterioration and quality tests use Group Sequential Tests (GST). All non-inferiority and superiority tests use fixed-horizon $z$-tests. See Appendix C for a discussion about combining sequential tests and fixed horizon tests for the same metric. For the GSTs, we analyze the results 10 times during the data collection at evenly spaced intervals. We generate data from a multivariate normal distribution, and treat the variance as known in the tests to be able to keep the sample size small. We use $S = G = 5$ and $D = Q = 2$, and repeat the simulation 100,000 times for each setting. In all scenarios, $\alpha^{+} = \alpha^{-} = 0.05$ and $\beta = 0.2$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Monte Carlo simulation study", "weight": 1.0} -->

We compare three designs: no correction, only alpha correction, and Proposition 4.1 with Remark A.1. In the simulation study, we vary the following: Hypothesis under which the simulation is performed $H_{0}$: the null of the non-inferiority and superiority tests Status quo: the null of the superiority and the alternative for the non-inferiority tests $H_{1}$: the alternative for non-inferiority and superiority tests Independent: All metrics independent Dependent: All pairwise correlations 0.99 Block 1: all guardrail metrics independent of each other and the success metrics, but all success metrics have pairwise correlation 0.99 Block 2: all success metrics independent of each other and the guardrail metrics, but all guardrail metrics have pairwise correlation 0.99 For all settings, all additional deterioration and quality metrics are generated as independent of each other and all other metrics with a zero effect.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Monte Carlo simulation study", "weight": 1.0} -->

The dependency structures are chosen to illustrate the most extreme situations The naive "Only Alpha" correction is simply dividing alpha on the number of tests, i.e., implies $\alpha^{\ast} = \frac{\alpha}{S + G} = \frac{0.05}{10}$ and $\alpha_{-}^{\ast} = \frac{\alpha_{-}}{S + G + D + Q} = \frac{0.05}{14}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Results", "weight": 1.0} -->

For convenience, the results are split by scenario: $H_{0}$, Status quo, and $H_{1}$. We present the rejection rates for the following groups of tests: $R_{\mathcal{S}}$: superiority tests for success metrics, a rejection means at least one is reject in that replication. $R_{\mathcal{G}}$: non-inferiority tests for guardrail metrics, a rejection means all are rejected in that replication. $R_{\mathcal{D},\mathcal{S}}{\bigcup R_{\mathcal{D},\mathcal{G}}}$: inferiority tests for success and guardrail metrics, a rejection means at least one is rejected in that replication. $R_{\mathcal{D}}{\bigcup R_{\mathcal{Q}}}$: tests for deterioration and quality metrics, a rejection means at least one is rejected in that replication.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Results", "weight": 1.0} -->

We also present the rejection rates for the three decision rules we develop in the paper, however, note that the design is always under Proposition 4.1.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Results under the global $H_{0}$", "weight": 1.0} -->

Table 3 displays the result under the the null hypotheses of the non-inferiority and the superiority tests. As expected, all three decision rules are conservative under all settings. This is explained by two things. First, the power of the deterioration test on the guardrail metrics is very high under the null hypothesis of the non-inferiority tests. Second, the probability of rejecting all guardrail metrics simultaneously is very low, with the exception of when all guardrail metrics are strongly correlated, which is confirmed for the Dependent and Block 1 covariance settings.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Results under the global $H_{0}$", "weight": 1.0} -->

As stated before, the $H_{0}$ scenario is arguably of little practical relevance, because the null hypothesis of the non-inferiority is decided by the experimenter. A more relevant scenario, in our opinion, is the status quo scenario for which the next section displays the results.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Results under status quo", "weight": 1.0} -->

Table 4 displays the result under the the alternative hypothesis of the non-inferiority and the null hypothesis of the superiority tests. The results clearly show that Proposition 4.1 is the correction that has the highest type I error rate, while not crossing the intended $\alpha = 0.05$. The Only Alpha correction bounds the type I error rate, but is conservative due to the lack of simultaneous power for the guardrail metrics. As expected, the addition of the deterioration and quality tests does make the rejection rate more conservative, but on a magnitude that has little practical relevance, especially as compared to, e.g., the impact of including beta corrections in the analysis.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Results under the global $H_{1}$", "weight": 1.0} -->

Table 5 displays the result under the the alternative hypotheses of the non-inferiority and the superiority tests. In this setting, the need for the power correction imposed by Proposition 4.1 is clear. For the other two corrections, the rates with which the guardrail metrics are simultaneously significantly non-inferior ($R_{\mathcal{G}}$) do not reach the intended power of 80%, which implies that neither can the decision rules. In the settings where the guardrail metrics are all independent (Independent, and Block 1), the rejection rate under no correction and the Only Alpha correction are as low as 30% for both decision rules---less than half of the intended power.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Results under the global $H_{1}$", "weight": 1.0} -->

The results under $H_{1}$ show that Proposition 4.1 bounds the error rates also in the worst-case scenarios, which leads to a higher power than desired in the best-case scenarios. For example, Proposition 4.1 ensures that even under the Block 2 covariance matrix, where all guardrail metrics are independent and all success metrics are dependent, the power is above 80%. However, to ensure that level of power under the worst-case scenario, the power instead exceeds 94% in the best-case scenario.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

In this paper, we introduce a decision rule framework that uses the results of multiple frequentist hypothesis tests in an experiment to ultimately make one single decision. The primary area of application of our theory is online controlled experiments, known as A/B tests, that technology companies use to run randomized controlled trials at scale to inform their product decision making. Decision rules help move the focus from the results of individual hypothesis tests to what really matters in the end: the overall conclusion of whether the tested change is good enough to release more widely. By carefully tailoring the decision rules, modern-day experimentation platforms can leverage decision rules to standardize decision making. For example, experimentation platforms can enforce that a new change should only be released widely if there is evidence that the change does not negatively impact important business metrics. Our framework clearly lays out the appropriate adjustments to the experiment design to ensure that the tolerated type I and type II error rates are not exceeded at the experiment level. Experimentation is primarily about understanding and managing risks, and with decision rules we put the risks that are relevant to the business front and center.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

Our decision rules use measured outcomes, known as metrics, that we classify into success metrics, guardrail metrics, deterioration metrics and quality metrics. Success metrics are metrics where we want to see an improvement, and guardrail metrics are metrics where we want to make sure no regression happens. We show that for a decision rule that includes both success metrics and guardrail metrics, we only need to adjust the type I error $\alpha$ used in tests for the number of success metrics. This result stands in contrast to the wide use of multiple correction methods, which generally do not take into account the role of the metrics they adjust. For guardrail metrics, we introduce the concept of $\beta$, or type II, corrections. We show that decision rules may be grossly under-powered without correcting the type II error the experiment is designed to achieve for the number of guardrail metrics. Finally, we introduce deterioration tests and quality tests, such as sample ratio mismatch and tests for pre-exposure bias, to the decision rule, and show how these tests affect the type I and type II errors.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

We combine all of our findings into the decision rule that is used by Spotify's experimentation platform, which includes tests for superiority, non-inferiority, inferiority, and quality. In a Monte Carlo simulation study, we illustrate how the design that our decision rule implies bounds the risks appropriately under various data-generating processes.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

There are many ways to construct decision rules incorporating many metrics, and many ways to control the type I and II errors for them. The decision rules and their corresponding $\alpha$ and $\beta$ corrections that we present in this paper are motivated mainly by simplicity. The straightforward Bonferroni-like corrections are easy to implement, and importantly, easy to explain and understand for most experimenters. In our experience, simplicity is often more important than finding the statistically optimal solution when it comes to experimentation methods that are to be used by many experimenters in large companies.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

Two important aspects of more sophisticated multiple-correction methods e.g., Holm and Hommel, is that they tend to complicate sample size calculations and they do not support straightforward calculation of confidence intervals, if at all. The net effect of using these more sophisticated correction methods is, in our experience, negative as the increased complexity leads to poorer planning of experiments and results that are harder to interpret. An appealing compromise for A/B tests is Nyholt's method that adjusts for the efficient number of independent tests. In Section D in the Appendix, we discuss how Nyholt's method can be used and similarly to we find that for a small number of metrics (5 success and 5 guardrail) the improvement in efficiency is marginal unless the correlation is strong. However, the improvement becomes substantial when the number of correlated metrics is large. In addition, methods other than sophisticated multiple-testing corrections can help increase efficiency, for example multivariate variance reduction via regression adjustment.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

For success metrics it is possible to replace the inferiority tests used in addition to the superiority tests, with non-inferiority tests. Strictly speaking, failing to reject the null of the inferiority test provides no evidence for the null hypothesis, and thus a more formal approach would be to require non-inferiority of all success metrics too. The reason for why inferiority tests are proposed here instead of non-inferiority tests is pragmatic. Using non-inferiority tests would require specifying a non-inferiority margin in addition to the hypothetical effect which would complicate the experiment setup for non-technical experimenters. Any deterioration metric could be replaced by a guardrail metric if the higher standard of non-inferiority tests is desired. Again, we find that having a few business important metrics as automatic deterioration metrics is a reasonable compromise: the experimenter does not need to configure anything for these metrics (no non-inferiority margin), but the company will detect major regressions to these metrics. This is a great example of the trade-off between rigour and not adding too much friction to the product development.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

In our experience, it is always the case that there is information outside the test that decision makers include in their product decision. However, to benefit from A/B testing as a risk management apparatus, we think it is important to move as much as possible into the experiment and explicitly define the decision rule with all the possible aspects in mind. As this paper shows, including caveats for shipping in terms of quality and deterioration tests affect the error rates of the decision. In practice, experimenters hesitate to include certain metrics as guardrail metrics because the sample size needed to power the experiment is too high. If these excluded metrics are still used in the decision making, the effect of the exclusion is only poor management of risk. Including as much as possible in the experiment and its decision rule means a better understanding of the risks you are facing for the the decision you ultimately need to make.
